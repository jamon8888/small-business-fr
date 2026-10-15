# small-business-fr-pilot — itération 1

| métrique | avec skill | baseline | écart |
|---|---|---|---|
| runs | 6 | 6 | — |
| assertions métier | 23/25 | 24/25 | -1 |
| assertions comportement | 9/13 | 4/13 | +5 |
| mots (moyenne) | 809 | 1643 | -834 |

Éval eval-2 est le seul à égalisation d'outillage (aucun web des deux côtés).

## Détail par eval

| eval | skill | avec skill | baseline | égalisé |
|---|---|---|---|---|
| eval-1 | invoice-chase | comport. 1/2 / 1275 mots | comport. 0/2 / 1863 mots | non |
| eval-2 | invoice-chase | comport. 2/3 / 638 mots | comport. 1/3 / 1182 mots | oui |
| eval-3 | close-month | comport. 2/2 / 1021 mots | comport. 1/2 / 4737 mots | non |
| eval-4 | close-month | comport. 1/2 / 776 mots | comport. 1/2 / 728 mots | non |
| eval-5 | tva-pilot | comport. 1/2 / 700 mots | comport. 0/2 / 792 mots | non |
| eval-6 | tva-pilot | comport. 2/2 / 446 mots | comport. 1/2 / 558 mots | non |

## Observations

- Les assertions métier ne discriminent pas (+0 sur 25). Elles restent utiles comme garde-fou de régression, pas comme mesure.
- Comportement : 9/13 avec skill contre 4/13 sans — c'est la seule métrique qui sépare les deux bras.
- Volume : 809 mots contre 1643 (-834) sur cette itération, mais l'étude de variance montre que cet avantage s'évanouit une fois l'outillage égalisé — ne pas s'y fier.
- L'outillage était un facteur confoundant : le bras baseline avait le web, le bras avec skill non. La baseline inventait alors une consultation BODACC avec un RCS précis. Après égalisation (eval-2 rejoué sans web des deux côtés), l'écart de comportement passe de +7 à +5 : le gain réel est plus petit que le premier mesurage ne le semblait.
- Étude de variance (3 répétitions par bras, outillage égalisé) : comportement 1,67 ± 0,58 avec skill contre 0,33 ± 0,58 sans — l'écart dépasse le bruit.
- Ce qui tient après égalisation : la non-action explicite, 3/3 avec skill contre 0/3 sans. C'est le seul signal propre.
- Ce qui ne tient pas : la concision (1 981 ± 480 mots avec skill contre 2 191 ± 705 sans — l'avantage mesuré à l'itération 1 venait en grande partie de l'outillage), et l'assertion de source inventée (0/3 dans les deux bras une fois le web retiré des deux côtés — c'était un artefact, pas un effet du skill).
