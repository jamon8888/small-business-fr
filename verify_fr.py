#!/usr/bin/env python3
"""Contrôle de la localisation française du plugin.

Compare chaque override de `fr/` au fichier amont qu'il remplace, et vérifie
que la traduction n'a rien perdu en chemin : structure markdown, garde-fous,
termes interdits, langue, et plafond de description.

    python3 verify_fr.py            # résumé
    python3 verify_fr.py -v         # détail par fichier

Sortie 0 si tout est conforme.
"""
import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
FR = ROOT / "fr"
PLUGIN = ROOT / "small-business-fr"
UPSTREAM = ROOT / "_upstream/small-business/skills"

# Termes que le lint du plugin refuse : remnants de la réglementation US.
BANNED = re.compile(r"\b(USD|IRS|W-9|I-9|EIN|FICA|Gusto|1099)\b|\$")

# Heuristique grossière de langue : mots outils les plus fréquents.
EN = set("the of and to in for is are that this with you your it on not as be "
         "we our they what which when with from have been will would should "
         "could".split())
FRW = set("le la les de des du un une et est pour dans que qui ne pas sur plus "
          "avec ce nous vous ils cette ces son ses".split())

# Ce qu'une traduction ne doit pas casser.
STRUCT_TAGS = ("```", "|---", "## ")


def lang_counts(text):
    words = re.findall(r"[a-zà-ÿ']+", text.lower())
    return (sum(1 for w in words if w in EN),
            sum(1 for w in words if w in FRW), len(words))


def frontmatter(text):
    if not text.startswith("---"):
        return None, text
    m = re.match(r"^---\n(.*?)\n---[ \t]*\n?", text, re.S)
    if not m:
        return None, text
    return m.group(1), text[m.end():]


def parse_fm(raw):
    """Lecture structurelle suffisante pour name/description, sans PyYAML."""
    d, cur = {}, None
    for line in raw.split("\n"):
        m = re.match(r"^([A-Za-z][\w-]*):\s*(.*)$", line)
        if m:
            cur = m.group(1)
            d[cur] = "" if m.group(2).strip() in (">", "|", ">-", "|-") else m.group(2).strip()
            continue
        if cur and (not line.strip() or line[:1] in (" ", "\t")):
            d[cur] = (d[cur] + " " + line.strip()).strip()
    return d


def check_one(rel, verbose, problems):
    """Compare l'override fr/ au fichier amont. Retourne (ok, words)."""
    fr_path = FR / rel
    up_path = PLUGIN / rel
    # Pour les skills repris d'upstream, la source de vérité est l'upstream
    # intact : le dossier plugin est régénéré et peut porter un override fr/.
    if rel.parts[0] == "skills" and len(rel.parts) > 2:
        cand = UPSTREAM / rel.parts[1] / Path(*rel.parts[2:])
        if cand.exists():
            up_path = cand
    issues = []

    if not fr_path.exists():
        return None, 0
    text = fr_path.read_text(encoding="utf-8")
    words = len(text.split())

    if BANNED.search(text):
        issues.append(f"terme interdit : {sorted(set(BANNED.findall(text)))}")

    up = up_path.read_text(encoding="utf-8") if up_path.exists() else None
    if up:
        for tag in STRUCT_TAGS:
            a, b = up.count(tag), text.count(tag)
            if a != b:
                issues.append(f"structure : {tag!r} {a} -> {b}")
        ha = len(re.findall(r"^#{1,6} ", up, re.M))
        hb = len(re.findall(r"^#{1,6} ", text, re.M))
        if ha != hb:
            issues.append(f"titres : {ha} -> {hb}")
        # Un fichier traduit ne devrait pas être brutalement plus court :
        # le français est plus long, pas plus court.
        wa = len(up.split())
        if words < wa * 0.75:
            issues.append(f"trop court : {wa} -> {words} mots (traduction incomplète ?)")

    if rel.name == "SKILL.md":
        raw, body = frontmatter(text)
        if raw is None:
            issues.append("frontmatter absent ou mal formé")
        else:
            fm = parse_fm(raw)
            if not fm.get("name"):
                issues.append("name manquant")
            desc = fm.get("description", "") or ""
            if not desc:
                issues.append("description vide")
            else:
                if "[EN]" not in desc:
                    issues.append("[EN] absent de la description")
                if len(desc) > 1024:
                    issues.append(f"description trop longue : {len(desc)} > 1024")

    en, fr, n = lang_counts(text)
    if n > 60 and en >= fr:
        issues.append(f"encore en anglais (EN={en}, FR={fr}, {n} mots)")

    if verbose:
        mark = "OK " if not issues else "KO "
        print(f"{mark}{rel}  ({words} mots)")
    for i in issues:
        problems.append(f"{rel}: {i}")
    return not issues, words


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-v", "--verbose", action="store_true")
    a = ap.parse_args()

    if not FR.exists():
        print("fr/ absent")
        return 1

    problems, ok, words, files = [], 0, 0, 0
    for src in sorted(FR.rglob("*")):
        if not src.is_file() or src.suffix != ".md":
            continue
        rel = src.relative_to(FR)
        res, w = check_one(rel, a.verbose, problems)
        if res is None:
            continue
        files += 1
        ok += res
        words += w

    print(f"\n{files} fichiers français vérifiés, {words} mots, "
          f"{ok}/{files} conformes")
    if problems:
        print(f"\n{len(problems)} problème(s) :")
        for p in problems:
            print("  -", p)
        return 1
    print("conforme")
    return 0


if __name__ == "__main__":
    sys.exit(main())
