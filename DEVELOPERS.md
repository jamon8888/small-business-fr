# small-business-fr — dépôt de build

Génère le plugin Claude Code **small-business-fr** : édition française du plugin
Anthropic `small-business`, pour les TPE et PME françaises.

```bash
python3 build.py            # assemble + zippe
python3 build.py --clean    # repart de zéro
python3 build.py --no-zip   # assemble sans zipper

python3 production_check.py # porte de qualité (10 contrôles)
python3 verify_fr.py        # parité de traduction, détail par fichier
```

## Disposition

| Chemin | Rôle |
|---|---|
| `build.py` | générateur unique. Aucune logique de plugin n'est écrite à la main en dehors |
| `fr/` | sources françaises (167 fichiers, ~174 000 mots) |
| `_upstream/` | dépôt Anthropic extrait du zip, source de verdad des skills repris |
| `small-business-fr/` | **sortie de build.** Effacée et régénérée à chaque run — ne jamais l'éditer |
| `small-business-fr.zip` | paquet distribuable |
| `evals/` | évaluation pilote (voir plus bas) |

> Règle qui a coûté le plus cher à apprendre : `small-business-fr/` est une
> sortie. Un agent qui y écrit semble réussir et son travail disparaît au build
> suivant. Tout se modifie dans `build.py` ou `fr/`.

## Pipeline

1. copie les skills repris d'`_upstream/` (corps anglais) + les `shared/` communs
2. réécrit les skills cœur en français (`patch_deep_skills`)
3. patche les descriptions, la devise, les renvois de commandes
4. applique `fr/**` par-dessus le plugin généré
5. replie les notes de tête sous le frontmatter
6. lint, tests, `UPSTREAM.md`, rapport de couverture, zip

## Invariants vérifiés à chaque build

`scripts/lint.py` échoue si l'un de ces points casse :

- le fichier ne commence pas par `---` (frontmatter illisible par le loader)
- clé de frontmatter hors `name / description / license / allowed-tools / metadata / compatibility`
- `[EN]` absent de la **description** (et pas seulement du fichier)
- description > 1024 caractères
- terme US (`USD`, `I-9`, `IRS`, `Gusto`…) dans `skills/` **ou `shared/`**
- lien markdown interne non résolu
- `/commande` citée mais absente de `commands/`
- cible `→ skill` morte dans le routeur
- connecteur FR obligatoire absent, connecteur US résiduel présent dans `.mcp.json`

`production_check.py` ajoute : build déterministe, anglais résiduel sur tout
l'arbre, exactitude de `UPSTREAM.md`, propreté du zip.

## Bugs historiques (à ne pas réintroduire)

- **Frontmatter cassé sur les 65 skills** : `add-language-header.py` prependait
  un `>` au-dessus du `---`. Tout le plugin était illisible.
- **Corps dupliqué** : `rewrite_description()` recollait `lines[b:]` puis
  `lines[end:]`, écrivant chaque section deux fois pour 6 skills.
- **8 fichiers référencés jamais livrés**, dont 3 `shared/` lus par tous les
  skills à chaque exécution.
- **11 renvois de commandes en anglais** dans `connector-map.md`, alors que le
  plugin ne livre que des commandes françaises.
- **`plan-payroll` supprimé de la construction** alors que le routeur y
  renvoyait les requêtes « paie ».
- **Aucun LICENSE** alors que `plugin.json` annonce Apache-2.0 sur du travail
  dérivé Apache-2.0.

## Évaluation

```bash
python3 grade_evals.py      # note domain + comportement
python3 variance_evals.py   # 3 répétitions, outillage égalisé
python3 benchmark_evals.py  # benchmark.json / .md
```

Résultat à jour dans `evals/pilot-workspace/iteration-1/benchmark.md`, revue
HTML dans `evals/pilot-workspace/review.html`.

Trois choses à savoir avant de s'appuyer dessus :

1. Les assertions **métier** ne discriminent pas (+0 sur 25). Gardez-les comme
   garde-fou de régression, pas comme mesure.
2. Les assertions de **comportement** discriminent (9/13 contre 4/13).
3. **L'outillage doit être égalisé.** Au premier passage le bras baseline avait
   le web et pas l'autre, ce qui produisait un écart de +7 puis de +5 une fois
   corrigé, et une fausse « source inventée » qui était un artefact.

Après égalisation, le seul signal robuste est la **non-action explicite**
(3/3 contre 0/3). L'avantage de concision mesuré au premier passage disparaît
(1 981 ± 480 mots avec skill contre 2 191 ± 705 sans).

## Limites connues

- La traduction est vérifiée **structurellement** (titres, tableaux, fences,
  identifiants, termes interdits), pas relue ligne à ligne par un francophone.
- `invoice-chase`, `contract-review`, `hiring-screener` portent du droit
  français. Les articles cités (`L441-10`, `D441-5`, `L624-16`…) sont vérifiés,
  mais **une relecture par un juriste reste le bon geste** avant diffusion.
- L'optimiseur de descriptions (`run_loop.py`) n'a pas été exécuté : il exige
  la CLI `claude`, absente de cette machine.
- 6 évaluations, 3 répétitions : suffisant pour constater un signal, insuffisant
  pour le généraliser aux 65 skills.
