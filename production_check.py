#!/usr/bin/env python3
"""Porte de qualité — une commande, tous les contrôles.

    python3 production_check.py

Regroupe ce qui était dispersé entre `verify_fr.py`, `scripts/lint.py` et des
commandes ad hoc, et couvre tout l'arbre du plugin — pas seulement `skills/`,
ce qui a laissé passer sept fichiers partagés restés en anglais.
"""
import hashlib
import os
import re
import subprocess
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PLUGIN = ROOT / "small-business-fr"
ZIP = ROOT / "small-business-fr.zip"
VENV = Path("/private/var/folders/w7/6rt7vbvd7bqbx0q2zdmnfvm40000gn/T/opencode/yv/bin/python")
SC = ROOT / ".claude/plugins/skill-creator/skills/skill-creator"

FRW = set("le la les de des du un une et est pour dans que qui ne pas sur plus "
          "avec ce nous vous ils cette ces son ses".split())
ENW = set("the of and to in for is are that this with you your it on not as be "
          "we our they what which when with from have been will would should "
          "could".split())
US = re.compile(r"\b(USD|IRS|W-9|I-9|EIN|FICA|Gusto|1099)\b")

results = []


def validator_python():
    """Un interpréteur avec PyYAML : variable d'env, venv connu, ou l'actuel."""
    cands = ([os.environ["VALIDATOR_PYTHON"]]
             if os.environ.get("VALIDATOR_PYTHON") else []) + [str(VENV), sys.executable]
    for c in cands:
        p = Path(c)
        if not p.exists():
            continue
        r = subprocess.run([str(p), "-c", "import yaml"], capture_output=True)
        if r.returncode == 0:
            return p
    return None


def check(name, ok, detail=""):
    results.append((name, ok, detail))
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f" — {detail}" if detail else ""))
    return ok


def build():
    subprocess.run([sys.executable, "build.py", "--clean"],
                   cwd=ROOT, stdout=subprocess.DEVNULL,
                   stderr=subprocess.DEVNULL, check=False)


def tree_hash():
    h = hashlib.sha256()
    for p in sorted(PLUGIN.rglob("*")):
        if p.is_file():
            h.update(p.name.encode())
            h.update(p.read_bytes())
    return h.hexdigest()


def main():
    if not PLUGIN.exists():
        build()

    # 1. reproductibilité
    build()
    a = tree_hash()
    build()
    check("build déterministe", a == tree_hash(), "deux builds identiques")

    # 2. lint du plugin
    r = subprocess.run([sys.executable, "scripts/lint.py"],
                       cwd=PLUGIN, capture_output=True, text=True)
    check("lint du plugin", r.returncode == 0,
          r.stdout.strip().splitlines()[-1] if r.stdout.strip() else "")

    # 3. parité de traduction
    r = subprocess.run([sys.executable, "verify_fr.py"],
                       cwd=ROOT, capture_output=True, text=True)
    check("parité fr/", r.returncode == 0,
          r.stdout.strip().splitlines()[-2] if r.stdout.strip() else "")

    # 4. validateur skill-creator
    # Copie vandorée dans tools/ (fonctionne en CI), sinon install locale.
    script = next((p for p in (ROOT / "tools/quick_validate.py",
                                SC / "scripts/quick_validate.py")
                   if p.exists()), None)
    vp = validator_python()
    if vp is None or script is None:
        check("validateur skill-creator", True,
              "SKIP — PyYAML ou validateur manquant (pip install pyyaml)")
    else:
        ok = bad = 0
        for d in sorted((PLUGIN / "skills").iterdir()):
            if not d.is_dir():
                continue
            rr = subprocess.run([str(vp), str(script), str(d)],
                                capture_output=True)
            ok, bad = (ok + 1, bad) if rr.returncode == 0 else (ok, bad + 1)
        check("validateur skill-creator", bad == 0, f"{ok} OK / {bad} FAIL")

    # 5. anglais résiduel — TOUT l'arbre, pas seulement skills/
    # data-model.md est un dictionnaire de colonnes : les clés canoniques de
    # gauche sont anglaises par conception (le fichier le dit en tête), la
    # prose est en français. L'heuristique ne peut pas le juger.
    EXEMPT = {"shared/data-model.md"}
    md = sorted(PLUGIN.rglob("*.md"))
    eng = []
    for p in md:
        rel = str(p.relative_to(PLUGIN))
        if rel in EXEMPT:
            continue
        w = re.findall(r"[a-zà-ÿ']+", p.read_text(encoding="utf-8").lower())
        if len(w) > 60 and sum(1 for x in w if x in ENW) >= sum(1 for x in w if x in FRW):
            eng.append(rel)
    check("aucun fichier en anglais", not eng,
          "; ".join(eng[:5]) if eng else f"{len(md)} fichiers .md")

    # 6. termes US résiduels
    us = [str(p.relative_to(PLUGIN)) for p in md
          if US.search(p.read_text(encoding="utf-8"))]
    check("aucun terme US", not us, "; ".join(us[:5]) if us else "")

    # 7. liens internes
    bad = 0
    for p in md:
        t = p.read_text(encoding="utf-8")
        for m in re.finditer(r"\[[^\]]*\]\(([^)]+)\)", t):
            g = m.group(1).split("#")[0].strip()
            if not g or g.startswith(("http", "mailto:")) or "..." in g:
                continue
            if not (p.parent / g).resolve().exists():
                bad += 1
    check("liens internes", bad == 0, f"{bad} cassé(s)")

    # 8. cible du routeur
    skills = {d.name for d in (PLUGIN / "skills").iterdir() if d.is_dir()}
    router = PLUGIN / "skills/smb-router/SKILL.md"
    dead = [m.group(1) for m in
            (re.search(r"→\s*([a-z][a-z0-9]*(?:-[a-z0-9]+)+)\s*$", l)
             for l in router.read_text(encoding="utf-8").splitlines())
            if m and m.group(1) not in skills]
    check("routeur sans cible morte", not dead, ", ".join(dead))

    # 9. documentation honnête
    up = PLUGIN / "UPSTREAM.md"
    nums = re.findall(r"- (\d+) skills, (\d+) commandes",
                      up.read_text(encoding="utf-8") if up.exists() else "")
    real = (str(len(skills)), str(len(list((PLUGIN / "commands").glob("*.md")))))
    check("UPSTREAM.md exact", bool(nums) and nums[0] == real,
          f"annonce {nums[0] if nums else '?'}, réel {real}")

    # 10. paquet
    if ZIP.exists():
        with zipfile.ZipFile(ZIP) as z:
            names = z.namelist()
        stray = [n for n in names
                 if re.search(r"(^|/)(_upstream|fr/|evals/|\.git)", n)]
        check("paquet propre", not stray,
              f"{len(names)} entrées, {len(stray)} parasite(s)")
        check("LICENSE inclus", any(n.endswith("LICENSE") for n in names))

    passed = sum(1 for _, ok, _ in results if ok)
    print(f"\n{passed}/{len(results)} contrôles passés")
    return 0 if passed == len(results) else 1


if __name__ == "__main__":
    sys.exit(main())
