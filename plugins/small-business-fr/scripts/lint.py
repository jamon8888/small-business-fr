#!/usr/bin/env python3
"""Vérifie le plugin produit.

Couvre le contrat de chargement des skills (frontmatter YAML en tête, clés
autorisées, name/description) en plus des règles d'édition FR (devise, termes
US, renvois de commandes, connecteurs).

Utilise PyYAML s'il est installé, sinon retombe sur une lecture structurelle
pour rester exécutable sur un Python minimal.
"""
import json, re, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
ERR = []
US = re.compile(r"\b(1099|IRS|W-9|I-9|EIN|FICA|Gusto|USD)\b")
# « $ » n'est un terme interdit que devant un montant : $ARGUMENTS est le
# jeton de substitution des slash-commands, pas une devise.
DOLLAR = re.compile(r"(?<![A-Za-z])\$(?![A-Z]{3})")
ALLOWED = {"name", "description", "license", "allowed-tools", "metadata", "compatibility"}
try:
    import yaml
except ImportError:
    yaml = None

def err(m): ERR.append(m)

def split_fm(text):
    """Retourne (frontmatter_brut, corps) ou (None, text) si absent."""
    if not text.startswith("---"):
        return None, text
    m = re.match(r"^---\n(.*?)\n---[ \t]*\n?", text, re.S)
    if not m:
        return None, text
    return m.group(1), text[m.end():]

def parse_fm(raw):
    if yaml is not None:
        try:
            return yaml.safe_load(raw), None
        except Exception as e:
            return None, f"YAML invalide: {e}"
    d, cur = {}, None
    for line in raw.split("\n"):
        m = re.match(r"^([A-Za-z][\w-]*):\s*(.*)$", line)
        if m:
            cur = m.group(1); val = m.group(2).strip()
            d[cur] = "" if val in (">", "|", ">-", "|-") else val
            continue
        if cur and (not line.strip() or line[:1] in (" ", "\t")):
            d[cur] = (d[cur] + " " + line.strip()).strip()
    return d, None

def check_frontmatter():
    for p in sorted((ROOT/"skills").rglob("SKILL.md")):
        raw, _ = split_fm(p.read_text(encoding="utf-8"))
        if raw is None:
            err(f"SKILL.md ne commence pas par '---': {p.relative_to(ROOT)}")
            continue
        d, e = parse_fm(raw)
        if e: err(f"{e} dans {p.relative_to(ROOT)}"); continue
        if not isinstance(d, dict):
            err(f"frontmatter non-objet dans {p.relative_to(ROOT)}"); continue
        extra = set(d) - ALLOWED
        if extra:
            err(f"clé(s) inattendue(s) {sorted(extra)} dans {p.relative_to(ROOT)}")
        if not d.get("name"): err(f"name manquant dans {p.relative_to(ROOT)}")
        desc = d.get("description") or ""
        if not desc: err(f"description vide dans {p.relative_to(ROOT)}")
        elif "[EN]" not in desc:
            err(f"[EN] absent de la description dans {p.relative_to(ROOT)}")

def check_names():
    for d in sorted((ROOT/"skills").iterdir()):
        if not d.is_dir(): continue
        p = d/"SKILL.md"
        if not p.exists(): err(f"missing SKILL.md: {d}"); continue
        raw, _ = split_fm(p.read_text(encoding="utf-8"))
        fm, _e = parse_fm(raw) if raw is not None else ({}, None)
        if isinstance(fm, dict) and fm.get("name") != d.name:
            err(f"name mismatch dans {p.relative_to(ROOT)}: {fm.get('name')!r}")

def check_desc():
    for p in (ROOT/"skills").rglob("SKILL.md"):
        if "[EN]" not in p.read_text(encoding="utf-8"):
            err(f"missing [EN] in {p}")

def check_header():
    for p in (ROOT/"skills").rglob("SKILL.md"):
        if "shared/language.md" not in p.read_text(encoding="utf-8"):
            err(f"missing header in {p}")

def check_us():
    # skills/ ET shared/ : les documents partagés sont lus par tous les skills
    # à l'exécution, un terme US qui y survit se propage partout.
    for p in list((ROOT/"skills").rglob("SKILL.md")) + \
            sorted((ROOT/"shared").rglob("*.md")):
        t = p.read_text(encoding="utf-8")
        for m in US.finditer(t):
            err(f"US term {m.group(1)} in {p.relative_to(ROOT)}")
        for m in DOLLAR.finditer(t):
            err(f"montant en dollars dans {p.relative_to(ROOT)}: …{t[max(0,m.start()-30):m.start()+30]}…")

def check_cmd():
    for c in sorted((ROOT/"commands").glob("*.md")):
        for m in re.finditer(r"skill `([a-z0-9-]+)`", c.read_text(encoding="utf-8")):
            if not (ROOT/"skills"/m.group(1)).exists():
                err(f"command {c.name} -> missing skill {m.group(1)}")

def check_mcp():
    d = set(json.loads((ROOT/".mcp.json").read_text())["mcpServers"])
    for n in ("qonto","pennylane","sendcloud"):
        if n not in d: err(f"missing {n} in .mcp.json")
    for n in ("gusto","myob","expensify","ramp","square"):
        if n in d: err(f"should remove {n}")

def check_refs():
    """Chaque renvoi markdown doit résoudre dans le plugin.

    Un skill qui demande de lire un fichier absent oblige le modèle à inventer
    son contenu : on le fait échouer au build plutôt qu'à l'exécution.
    """
    link = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
    for md in sorted(ROOT.rglob("*.md")):
        t = md.read_text(encoding="utf-8")
        for m in link.finditer(t):
            tgt = m.group(1).split("#")[0].strip()
            if not tgt or tgt.startswith(("http", "mailto:", "<")):
                continue
            # « design.canva.ai/... » est une URL tronquée en prose, pas un chemin
            if "..." in tgt or re.match(r"^[a-z0-9-]+(\.[a-z0-9-]+)+", tgt):
                continue
            if not (md.parent / tgt).resolve().exists():
                err(f"lien cassé dans {md.relative_to(ROOT)} -> {tgt}")

def check_cmd_refs():
    """Chaque /commande cité doit exister dans commands/.

    Un slash-command renommé en anglais alors que le plugin ne le livre que en
    français ne résout jamais : le modèle annonce une commande inexistante.
    """
    have = {c.stem for c in (ROOT / "commands").glob("*.md")}
    # Un nom de commande est toujours composé (« /payer-factures »). Exiger un
    # tiret et refuser les voisinages de chemin ou d'URL élimine les faux
    # positifs : /social/posts, /www.exemple.fr, ../../ref/xero-reconcile.
    pat = re.compile(r"(?<![\w./-])/([a-z][a-z0-9]*-[a-z0-9-]+)(?![\w./-])")
    for md in sorted(ROOT.rglob("*.md")):
        t = md.read_text(encoding="utf-8")
        for line in t.splitlines():
            # endpoints d'API : « GET /brand-templates?query=… »
            if re.search(r"\b(GET|POST|PUT|PATCH|DELETE)\s+/", line):
                continue
            for m in pat.finditer(line):
                name = m.group(1)
                if name in have:
                    continue
                err(f"commande inconnue {name!r} citée dans {md.relative_to(ROOT)}")

def check_skill_refs():
    """Chaque skill routé doit exister.

    Le routeur est le seul endroit où un nom faux crée un cul-de-sac
    silencieux. On ne vérifie que lui : ailleurs, un token en kebab-case entre
    accents graves est presque toujours un nom d'outil (Canva, Shopify) ou une
    classe CSS, pas un skill.
    """
    have = {d.name for d in (ROOT / "skills").iterdir() if d.is_dir()}
    router = ROOT / "skills/smb-router/SKILL.md"
    if not router.exists():
        return
    # lignes de routage : « … → nom-du-skill »
    pat = re.compile(r"→\s*([a-z][a-z0-9]*(?:-[a-z0-9]+)+)\s*$")
    for i, line in enumerate(router.read_text(encoding="utf-8").splitlines(), 1):
        m = pat.search(line)
        if m and m.group(1) not in have:
            err(f"le routeur renvoie vers le skill inconnu "
                f"{m.group(1)!r} ({router.relative_to(ROOT)}:{i})")

def main():
    check_frontmatter(); check_names(); check_desc(); check_header()
    check_us(); check_cmd(); check_mcp(); check_refs(); check_cmd_refs()
    check_skill_refs()
    if ERR:
        print(f"{len(ERR)} problems:")
        for e in ERR: print(" -", e)
        sys.exit(1)
    print("lint OK")
if __name__ == "__main__": main()
