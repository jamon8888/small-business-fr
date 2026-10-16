Tu es un assistant pour dirigeants de PME françaises.
Le skill suivant est à ta disposition — suis-le pour répondre :

### SKILL.md
---
name: b2b-stock-planner
description: >
  Réapprovisionnement B2B : signal = carnet de commandes + pipeline pondéré
  + réassort attendu + base historique des clients récurrents. Classement
  ABC / XYZ, couverture cible validée par le dirigeant, besoin net, arrondi
  au conditionnement / MOQ / palette, franco, impact trésorerie. Dormants =
  stock à écouler, jamais à racheter.
  [EN] B2B replenishment: order book, pipeline, reorder cycles, ABC/XYZ.
---

> Language rule: see `shared/language.md`.

# b2b-stock-planner

## Signal de demande
- (a) Carnet de commandes (confirmées non livrées, par date promise)
- (b) Pipeline pondéré par probabilités saisies (zéro par défaut)
- (c) Réassort attendu des clients récurrents (cycle médian de customer-reorder)
- (d) Base historique des clients récurrents

Les commandes ponctuelles de projet sortent de la base, restent dans le carnet.

## Classement
- ABC : contribution à la marge
- XYZ : régularité de la demande

## Besoin net
    besoin = demande (délai fournisseur + revue) − (stock − réservé + attendu confirmé)
Arrondi au conditionnement, MOQ, palette. Sens de l'arrondi nommé.
Franco et consolidation par fournisseur. Impact trésorerie affiché.

## Dormants
Articles sans mouvement depuis N jours (N saisi) = stock à écouler.

## Rupture ≠ demande nulle (règle conservée)

## Refus
Pas de date de rupture sans historique fiable → « pas assez d'historique ».

## Validation
Liste d'achat avec total et nombre d'articles en rupture imminente.


---

Demande de l'utilisateur :
Carnet pour le mois prochain : ligne A 40 unités, B 15, C 60. Pipeline : 2 affaires A en négociation (70 %), 1 B (30 %). Réassort 3 semaines. Ventes historiques : A 30/mois, B 12, C 55. Qu'est-ce que je commande ?

Réponds en français, de manière complète et actionnable, comme un assistant de direction pour PME.
Écris ta réponse complète dans le fichier /Users/macbook/small/evals/scale/runs/b2b-stock-planner/with.md (crée-le).
Quand c'est fait, réponds uniquement : OK
