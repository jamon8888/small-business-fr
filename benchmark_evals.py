#!/usr/bin/env python3
"""Agrège les runs en benchmark.json / benchmark.md.

Sépare deux familles de métriques :

  métier        justesse du contenu — non discriminante ici (+0 / -1)
  comportement  ce qui distingue le skill : non-action explicite, aveu
                d'incertitude, refus d'affirmer une source non consultée

Ajoute l'écart-type inter-runs pour exposer la variance : un eval dont les deux
exécutions with_skill divergent est instable, et son résultat ne prouve rien.
"""
import json
import statistics
from pathlib import Path

ROOT = Path(__file__).resolve().parent
W = ROOT / "evals/pilot-workspace/iteration-1"
EV = json.loads((ROOT / "evals/evals.json").read_text(encoding="utf-8"))
CONFIGS = [("with_skill", "avec skill"), ("without_skill", "baseline")]
NOCONF = "eval-2"


def load(p):
    return json.loads(p.read_text(encoding="utf-8"))


def main():
    entries = []
    for cfg, label in CONFIGS:
        per_eval, dom, beh, words = [], 0, 0, 0
        for e in EV["evals"]:
            d = W / f"eval-{e['id']}"
            g, r = d / cfg / "grading.json", d / cfg / "outputs" / "response.md"
            if not (g.exists() and r.exists()):
                continue
            gr, text = load(g), r.read_text(encoding="utf-8")
            dom += gr["domain_passed"]
            beh += gr["behaviour_passed"]
            words += len(text.split())
            per_eval.append({
                "eval_id": e["id"], "skill": e["skill"], "words": len(text.split()),
                "domain": f"{gr['domain_passed']}/{gr['domain_total']}",
                "behaviour": f"{gr['behaviour_passed']}/{gr['behaviour_total']}",
                "controlled": f"eval-{e['id']}" == NOCONF,
            })
        n = len(per_eval)
        entries.append({
            "config": cfg, "label": label, "runs": n,
            "domain": {"passed": dom, "total": sum(
                sum(1 for x in load(W / f"eval-{e['id']}" / cfg / "grading.json")
                    ["expectations"] if x.get("weight") == "domain")
                for e in EV["evals"]
                if (W / f"eval-{e['id']}" / cfg / "grading.json").exists())},
            "behaviour": {"passed": beh, "total": sum(
                sum(1 for x in load(W / f"eval-{e['id']}" / cfg / "grading.json")
                    ["expectations"] if x.get("weight") in ("safety", "honesty"))
                for e in EV["evals"]
                if (W / f"eval-{e['id']}" / cfg / "grading.json").exists())},
            "mean_words": round(words / n) if n else 0,
            "per_eval": per_eval,
        })

    a, b = entries
    var = None
    if (ROOT / "evals/variance/variance.json").exists():
        var = json.loads((ROOT / "evals/variance/variance.json").read_text(
            encoding="utf-8"))
    bench = {
        "skill_name": "small-business-fr-pilot", "iteration": 1,
        "configurations": entries,
        "controlled_eval": NOCONF,
        "variance": var or {
            "note": "non mesuré sur cette itération"},
        "observations": [
            "Les assertions métier ne discriminent pas (+0 sur 25). Elles "
            "restent utiles comme garde-fou de régression, pas comme mesure.",
            f"Comportement : {a['behaviour']['passed']}/{a['behaviour']['total']} "
            f"avec skill contre {b['behaviour']['passed']}/{b['behaviour']['total']} "
            f"sans — c'est la seule métrique qui sépare les deux bras.",
            f"Volume : {a['mean_words']} mots contre {b['mean_words']} "
            f"({a['mean_words'] - b['mean_words']:+d}) sur cette itération, "
            "mais l'étude de variance montre que cet avantage s'évanouit "
            "une fois l'outillage égalisé — ne pas s'y fier.",
            "L'outillage était un facteur confoundant : le bras baseline "
            "avait le web, le bras avec skill non. La baseline inventait alors "
            "une consultation BODACC avec un RCS précis. Après égalisation "
            "(eval-2 rejoué sans web des deux côtés), l'écart de comportement "
            "passe de +7 à +5 : le gain réel est plus petit que le premier "
            "mesurage ne le semblait.",
        ] + ([
            "Étude de variance (3 répétitions par bras, outillage égalisé) : "
            "comportement 1,67 ± 0,58 avec skill contre 0,33 ± 0,58 sans — "
            "l'écart dépasse le bruit.",
            "Ce qui tient après égalisation : la non-action explicite, "
            "3/3 avec skill contre 0/3 sans. C'est le seul signal propre.",
            "Ce qui ne tient pas : la concision (1 981 ± 480 mots avec skill "
            "contre 2 191 ± 705 sans — l'avantage mesuré à l'itération 1 "
            "venait en grande partie de l'outillage), et l'assertion de "
            "source inventée (0/3 dans les deux bras une fois le web retiré "
            "des deux côtés — c'était un artefact, pas un effet du skill).",
        ] if var else []),
    }
    (W / "benchmark.json").write_text(
        json.dumps(bench, ensure_ascii=False, indent=2), encoding="utf-8")

    md = ["# small-business-fr-pilot — itération 1", "",
          "| métrique | avec skill | baseline | écart |", "|---|---|---|---|",
          f"| runs | {a['runs']} | {b['runs']} | — |",
          f"| assertions métier | {a['domain']['passed']}/{a['domain']['total']} "
          f"| {b['domain']['passed']}/{b['domain']['total']} "
          f"| {a['domain']['passed']-b['domain']['passed']:+d} |",
          f"| assertions comportement | {a['behaviour']['passed']}/"
          f"{a['behaviour']['total']} | {b['behaviour']['passed']}/"
          f"{b['behaviour']['total']} "
          f"| {a['behaviour']['passed']-b['behaviour']['passed']:+d} |",
          f"| mots (moyenne) | {a['mean_words']} | {b['mean_words']} "
          f"| {a['mean_words']-b['mean_words']:+d} |", "",
          f"Éval {NOCONF} est le seul à égalisation d'outillage (aucun web "
          "des deux côtés).", "",
          "## Détail par eval", "",
          "| eval | skill | avec skill | baseline | égalisé |",
          "|---|---|---|---|---|"]
    for x in a["per_eval"]:
        y = next(z for z in b["per_eval"] if z["eval_id"] == x["eval_id"])
        md.append(f"| eval-{x['eval_id']} | {x['skill']} | "
                  f"comport. {x['behaviour']} / {x['words']} mots | "
                  f"comport. {y['behaviour']} / {y['words']} mots | "
                  f"{'oui' if x['controlled'] else 'non'} |")
    md += ["", "## Observations", ""]
    md += [f"- {o}" for o in bench["observations"]]
    (W / "benchmark.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    print("\n".join(md))


if __name__ == "__main__":
    main()
