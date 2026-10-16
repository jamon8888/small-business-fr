#!/usr/bin/env python3
"""Scoreur déterministe de l'évaluation de scale.

Lit runs/<skill>/{with,without}.md, évalue chaque assertion par regex
(`negate: true` = l'assertion passe si le pattern N'apparaît pas), écrit un
grading.json par exécution et agrège benchmark.json (format du pilot) +
benchmark.md (tableau par skill avec le delta with − without).
"""
import json
import re
import sys
from pathlib import Path

SCALE = Path(__file__).resolve().parent
RUNS = SCALE / "runs"


def score_text(txt: str, assertions: list, weight: str) -> list:
    out = []
    for a in assertions:
        hit = re.search(a["pattern"], txt, re.I | re.M) is not None
        passed = (not hit) if a.get("negate") else hit
        out.append({"text": a["text"], "passed": passed, "weight": weight,
                    "evidence": (f"pattern {'ABSENT' if (hit and a.get('negate')) else 'présent' if (hit and not a.get('negate')) else 'absent'}"
                                 f" → {'PASS' if passed else 'FAIL'}")})
    return out


def main() -> None:
    ev = json.loads((SCALE / "evals.json").read_text(encoding="utf-8"))
    configs = {"with_skill": [], "without_skill": []}
    per_skill = {}
    missing = []

    for e in ev["evals"]:
        skill = e["skill"]
        row = {"skill": skill, "domain": [None, None], "behaviour": [None, None]}
        for i, (arm, cfg) in enumerate([("with", "with_skill"), ("without", "without_skill")]):
            f = RUNS / skill / f"{arm}.md"
            if not f.exists():
                missing.append(str(f.relative_to(SCALE)))
                continue
            txt = f.read_text(encoding="utf-8")
            grading = {
                "eval_id": e["id"], "config": cfg, "skill": skill,
                "domain_passed": 0, "domain_total": len(e["assertions"]),
                "behaviour_passed": 0, "behaviour_total": len(e["behaviour"]),
                "expectations": [],
            }
            for entry in score_text(txt, e["assertions"], "domain"):
                grading["expectations"].append(entry)
                grading["domain_passed"] += entry["passed"]
            for entry in score_text(txt, e["behaviour"], "behaviour"):
                grading["expectations"].append(entry)
                grading["behaviour_passed"] += entry["passed"]
            gdir = RUNS / skill / ("with_skill" if arm == "with" else "without_skill")
            gdir.mkdir(parents=True, exist_ok=True)
            (gdir / "grading.json").write_text(
                json.dumps(grading, ensure_ascii=False, indent=1), encoding="utf-8")
            words = len(txt.split())
            configs[cfg].append({
                "eval_id": e["id"], "skill": skill, "words": words,
                "domain": f"{grading['domain_passed']}/{grading['domain_total']}",
                "behaviour": f"{grading['behaviour_passed']}/{grading['behaviour_total']}",
            })
            row["domain"][i] = (grading["domain_passed"], grading["domain_total"])
            row["behaviour"][i] = (grading["behaviour_passed"], grading["behaviour_total"])
        per_skill[skill] = row

    def agg(runs):
        d = sum(int(r["domain"].split("/")[0]) for r in runs)
        dt = sum(int(r["domain"].split("/")[1]) for r in runs)
        b = sum(int(r["behaviour"].split("/")[0]) for r in runs)
        bt = sum(int(r["behaviour"].split("/")[1]) for r in runs)
        return {"domain": {"passed": d, "total": dt},
                "behaviour": {"passed": b, "total": bt},
                "mean_words": round(sum(r["words"] for r in runs) / max(len(runs), 1))}

    benchmark = {
        "skill_name": ev["skill_name"],
        "iteration": 1,
        "note": ev["note"],
        "configurations": [],
    }
    for cfg, label in [("with_skill", "avec skill"), ("without_skill", "sans skill")]:
        runs = configs[cfg]
        c = {"config": cfg, "label": label, "runs": len(runs)}
        c.update(agg(runs))
        c["per_eval"] = sorted(runs, key=lambda r: r["eval_id"])
        benchmark["configurations"].append(c)
    (SCALE / "benchmark.json").write_text(
        json.dumps(benchmark, ensure_ascii=False, indent=1), encoding="utf-8")

    # benchmark.md
    lines = [
        "# Benchmark de scale — small-business-fr",
        "",
        ev["note"],
        "",
        "| Configuration | Runs | Métier (domain) | Comportement (behaviour) | Mots/moy.",
        "|---|---|---|---|---|",
    ]
    for c in benchmark["configurations"]:
        lines.append(f"| {c['label']} | {c['runs']} | "
                     f"{c['domain']['passed']}/{c['domain']['total']} | "
                     f"{c['behaviour']['passed']}/{c['behaviour']['total']} | {c['mean_words']} |")
    lines += ["", "## Par skill (avec skill − sans skill)", "",
              "| Skill | Métier avec | Métier sans | Δ métier | Comport. avec | Comport. sans | Δ comport. |",
              "|---|---|---|---|---|---|---|"]
    delta_d = delta_b = 0
    for skill, row in sorted(per_skill.items()):
        d = f"{row['domain'][0][0]}/{row['domain'][0][1]}" if row["domain"][0] else "—"
        d2 = f"{row['domain'][1][0]}/{row['domain'][1][1]}" if row["domain"][1] else "—"
        b = f"{row['behaviour'][0][0]}/{row['behaviour'][0][1]}" if row["behaviour"][0] else "—"
        b2 = f"{row['behaviour'][1][0]}/{row['behaviour'][1][1]}" if row["behaviour"][1] else "—"
        dd = (row["domain"][0][0] - row["domain"][1][0]) if row["domain"][0] and row["domain"][1] else 0
        db = (row["behaviour"][0][0] - row["behaviour"][1][0]) if row["behaviour"][0] and row["behaviour"][1] else 0
        delta_d += dd
        delta_b += db
        lines.append(f"| {skill} | {d} | {d2} | {dd:+d} | {b} | {b2} | {db:+d} |")
    if missing:
        lines += ["", f"⚠️ {len(missing)} exécutions manquantes :", ""]
        lines += [f"- `{m}`" for m in missing]
    (SCALE / "benchmark.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    withn = benchmark["configurations"][0]
    withoutn = benchmark["configurations"][1]
    print(f"avec skill   : métier {withn['domain']['passed']}/{withn['domain']['total']}, "
          f"comport. {withn['behaviour']['passed']}/{withn['behaviour']['total']}")
    print(f"sans skill   : métier {withoutn['domain']['passed']}/{withoutn['domain']['total']}, "
          f"comport. {withoutn['behaviour']['passed']}/{withoutn['behaviour']['total']}")
    if missing:
        print(f"⚠️ {len(missing)} réponses manquantes")
        sys.exit(1)


if __name__ == "__main__":
    main()
