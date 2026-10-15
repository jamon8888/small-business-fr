#!/usr/bin/env python3
"""Plie les notes de tête (règle de langue, notes de périmètre) sous le
frontmatter YAML.

Un SKILL.md doit commencer par `---`, sinon le frontmatter n'est pas du
frontmatter et les chargeurs de skills le lisent comme du corps. Les notes
`>` écrites avant le frontmatter sont donc remontées juste après le `---`
de fermeture. Idempotent.
"""
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
NOTE = "> Language rule: see `shared/language.md`."

def process(p):
    lines = p.read_text(encoding="utf-8").split("\n")
    head, i = [], 0
    while i < len(lines) and (lines[i].startswith(">") or not lines[i].strip()):
        h = lines[i].strip()
        if lines[i].startswith(">") and "shared/language.md" not in h:
            head.append(h)
        i += 1
    rest = lines[i:]
    if any("shared/language.md" in l for l in rest[:40]):
        return False
    start = next((j for j, l in enumerate(rest) if l.strip() == "---"), None)
    if start is None:
        return False
    end = next(j for j in range(start + 1, len(rest)) if rest[j].strip() == "---")
    new = rest[:end + 1] + ["", NOTE] + head + rest[end + 1:]
    p.write_text("\n".join(new), encoding="utf-8")
    return True

def main():
    n = sum(process(p) for p in sorted((ROOT/"skills").rglob("SKILL.md")))
    print(f"header set in {n} files")
if __name__ == "__main__": main()
