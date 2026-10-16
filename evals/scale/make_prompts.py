#!/usr/bin/env python3
"""Génère les 124 fichiers de consigne (62 skills × 2 bras) pour l'évaluation de scale.

Le sous-agent lit son fichier de consigne : il ne voit que sa tâche, ce qui
garde le contexte de la session de dispatch mince. Les deux bras sont
parfaitement symétriques sauf l'injection du skill (c'est l'unique variable).
"""
import json
import pathlib

ROOT = pathlib.Path("/Users/macbook/small")
PLUGIN = ROOT / "small-business-fr" / "skills"
SCALE = ROOT / "evals" / "scale"
PROMPTS = SCALE / "prompts"
RUNS = SCALE / "runs"


def skill_content(skill: str) -> str:
    sdir = PLUGIN / skill
    parts = []
    for f in sorted(sdir.rglob("*.md")):
        parts.append(f"### {f.relative_to(sdir)}\n{f.read_text(encoding='utf-8')}")
    return "\n\n".join(parts)


def main() -> None:
    ev = json.loads((SCALE / "evals.json").read_text(encoding="utf-8"))
    PROMPTS.mkdir(parents=True, exist_ok=True)
    n = 0
    for e in ev["evals"]:
        skill = e["skill"]
        out_with = RUNS / skill / "with.md"
        out_without = RUNS / skill / "without.md"
        out_with.parent.mkdir(parents=True, exist_ok=True)

        with_p = (
            "Tu es un assistant pour dirigeants de PME françaises.\n"
            "Le skill suivant est à ta disposition — suis-le pour répondre :\n\n"
            f"{skill_content(skill)}\n\n"
            f"---\n\nDemande de l'utilisateur :\n{e['prompt']}\n\n"
            f"Réponds en français, de manière complète et actionnable, comme un "
            f"assistant de direction pour PME.\n"
            f"Écris ta réponse complète dans le fichier {out_with} (crée-le).\n"
            "Quand c'est fait, réponds uniquement : OK\n"
        )
        without_p = (
            "Tu es un assistant pour dirigeants de PME françaises.\n\n"
            f"Demande de l'utilisateur :\n{e['prompt']}\n\n"
            f"Réponds en français, de manière complète et actionnable, comme un "
            f"assistant de direction pour PME.\n"
            f"Écris ta réponse complète dans le fichier {out_without} (crée-le).\n"
            "Quand c'est fait, réponds uniquement : OK\n"
        )
        (PROMPTS / f"{skill}-with.md").write_text(with_p, encoding="utf-8")
        (PROMPTS / f"{skill}-without.md").write_text(without_p, encoding="utf-8")
        n += 2
    print(f"OK — {n} fichiers de consigne dans {PROMPTS}")


if __name__ == "__main__":
    main()
