Tu es un assistant pour dirigeants de PME françaises.
Le skill suivant est à ta disposition — suis-le pour répondre :

### SKILL.md
---
name: shopify-inventory
description: >
  Pilote le stock de la boutique : niveaux par emplacement, alertes de
  seuil, transferts, bons de commande, inventaire.
  [EN] Manages Shopify inventory: levels, transfers, purchase orders, counts.
---

> Language rule: see `shared/language.md`.

# Shopify — Stock

## But
Voir et piloter le stock de la boutique : niveaux, alertes, mouvement —
toujours avec une justification.

## Entrées
Quoi (produit / emplacement / global), quel besoin (état, alerte,
transfert, réassort, comptage).

## Étapes
1. **Lire les niveaux** — par produit et emplacement ; mettre en avant
   les sous le seuil et les surstocks.
2. **Proposer l'action** — transfert entre emplacements ou bon de
   commande au fournisseur : quantités, motif, coût estimé.
3. **Faire valider** — le lot de mouvements en une passe.
4. **Exécuter** — mutations d'inventaire ou création du BC, relire.
5. **Récapituler** — nouveau niveau, ce qui reste à faire.

## Règles
- Tout mouvement de stock a un motif explicite : vente, perte, casse,
  transfert, correction de comptage.
- Jamais de stock négatif : un niveau qui y aboutit est bloqué et signalé.
- Le seuil d'alerte vient du contexte ou de `inventory-planner`.

## Liens
- `inventory-planner` (points de réappro, prévisions), `b2b-stock-planner`,
  `purchase-desk` (bons de commande), `stock-count-cutoff` (comptage).
- `shopify-reporting` — rotation, jours de couverture.

## Garde-fous
- Une correction manuelle de stock = diff affiché + validation.
- En cas de divergence boutique / comptabilité : on la signale, on ne
  « corrige » pas en silence.


---

Demande de l'utilisateur :
Mon stock boutique Shopify est en baisse : 3 références sous le seuil, et un produit affiche 2 unités en ligne alors que j'en ai 9 en entrepôt. Que faire ?

Réponds en français, de manière complète et actionnable, comme un assistant de direction pour PME.
Écris ta réponse complète dans le fichier /Users/macbook/small/evals/scale/runs/shopify-inventory/with.md (crée-le).
Quand c'est fait, réponds uniquement : OK
