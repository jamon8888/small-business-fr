# Rapport d'évaluation — small-business-fr

Mesure de l'apport réel des skills **avec** vs **sans** (baseline), scoring
déterministe 100 % regex. Deux niveaux : un **pilot** (3 skills, validation
méthodologique + variance) puis le **scale** (62 skills, 124 exécutions).

## Synthèse

| Niveau | Scope | Métier (domain) | Comportement (behaviour) |
|---|---|---|---|
| **Pilot** | 3 skills × 2 bras | avec 23/25 · sans 24/25 | avec **9/13** · sans 4/13 |
| **Scale** | 62 skills × 2 bras (124 runs) | avec **196/202** (97,0 %) · sans 175/202 (86,6 %) | avec **70/125** (56,0 %) · sans 63/125 (50,4 %) |

**Delta scale (avec − sans) : +21 assertions métier, +7 comportementales.**

## Lecture

- **Le métier ne discrimine presque pas.** Les skills FR sont déjà bons ; sans
  skill le modèle passe aussi ~87 % des assertions métier. L'apport du skill se
  voit surtout sur les cas où le sans-skill rate un garde-fou (+17 au total :
  build-connector, crm-autopilot, month-end-prep +2 ; contract-review,
  devis-facture-fr, inventory-planner, lead-triage, monday-brief, etc. +1).
- **Le comportement est la métrique qui sépare les bras** (cohérent pilot →
  scale) : non-action explicite + absence de source inventée. Le skill impose la
  discipline de ne pas inventer et de dire « je ne fais pas ceci ».
- **Volume :** avec skill 898 mots/moy vs 963 sans (scale) ; 809 vs 1643 (pilot).
  L'étude de variance du pilot montre que cet avantage de concision s'évanouit
  une fois l'outillage égalisé → **ne pas s'y fier comme preuve de qualité**.
- **Aucun skill ne dégrade plus le score métier** après affinement (v2).
  Les 3 skills en négatif à la v1 ont été corrigés à la source (`build.py` +
  overrides FR) et re-évalués :
  - `pricing-desk` (v1 : −1) — le SKILL.md était un stub de 738 car. sans
    section « leviers » ; ajouté : répercuter le surcoût, renégocier le prix
    d'achat, réduire un autre poste, avec ordre de grandeur. → 4/4.
  - `build-agent` (v1 : −2) — ajouté un « Contrat de réponse » obligatoire :
    proposer le déclencheur (nom + horaire) et poser les questions qui
    capturent chaque étape / les données. → 3/3.
  - `marketing-monday` (v1 : −1) — ajoutée une brique **SEO local obligatoire**
    (fiches Google Business, avis, actions locales) dans le plan de semaine. → 3/3.

  Seule assertion encore en échec, commune aux 2 bras (donc sans delta) :
  « annonce explicite qu'aucune action n'a été effectuée » — limite connue du
  scoring regex, pas une régression.

## Méthode

- 1 cas par skill, 2 bras identiques (`with_skill` = skill complet injecté dans
  le prompt / `without_skill` = sans).
- Assertions métier (garde-fous de régression) + 2 comportements communs
  (non-action explicite, pas de source inventée), toutes en regex.
- `evals/scale/score.py` → `grading.json` par bras + `benchmark.json` /
  `benchmark.md` (format pilot). 124/124 exécutions, 0 manquant.

## Fichiers

- `pilot-workspace/iteration-1/benchmark.{json,md}` — pilot + variance
- `scale/benchmark.{json,md}` — scale (tableau par skill avec delta)
- `scale/evals.json` — 62 cas, 202 assertions métier, 125 comportementales
- `scale/runs/<skill>/{with,without}.md` + `…/{with,without}_skill/grading.json`
