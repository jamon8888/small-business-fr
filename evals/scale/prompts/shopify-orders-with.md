Tu es un assistant pour dirigeants de PME françaises.
Le skill suivant est à ta disposition — suis-le pour répondre :

### SKILL.md
---
name: shopify-orders
description: >
  Gère les commandes de la boutique : consultation, statuts, expédition
  (transporteur, suivi), retours et remboursements.
  [EN] Manages Shopify orders: fulfillment, shipping, returns, refunds.
---

> Language rule: see `shared/language.md`.

# Shopify — Commandes

## But
Suivre et traiter les commandes de la boutique : expédier, suivre,
gérer les retours — sans jamais exécuter de paiement.

## Entrées
Période ou liste de commandes, statut visé, ou un cas de retour précis.

## Étapes
1. **Lister / filtrer** — commandes par période, statut, problème
   (en attente, en retard, litige, retour demandé).
2. **Préparer l'expédition** — pour chaque commande à expédier :
   transporteur, service, étiquette. Le numéro de suivi vient du
   transporteur (`sendcloud`, `fulfillment-desk`) — jamais inventé.
3. **Faire valider** — lot d'expéditions présenté en une passe.
4. **Exécuter** — créer les fulfillments, coller les suivi, relire.
5. **Retours** — remboursement : montant exact affiché, restock proposé,
   double confirmation si le montant dépasse le seuil du contexte.

## Contrôles
- Tout remboursement montre : commande, montant, motif, effet sur le stock.
- Annulation de commande : double confirmation + montant.
- Aucune demande de paiement ici : relance de paiement → `invoice-chase`.

## Liens
- `order-intake` (prise de commande B2B), `fulfillment-desk` (expédition),
  `ticket-deflector` (service client), `invoice-chase` (recouvrement),
  `einvoice-readiness` (facture électronique).
- `shopify-reporting` — taux de retour, commandes par période.

## Garde-fous
- Jamais de remboursement au-delà du montant encaissé.
- Lot d'expédition : un seul « oui » suffit, un récapitulatif est affiché.


---

Demande de l'utilisateur :
J'ai 14 commandes en attente d'expédition dans ma boutique Shopify, dont 2 clientes qui réclament un retour. Comment on traite ça ?

Réponds en français, de manière complète et actionnable, comme un assistant de direction pour PME.
Écris ta réponse complète dans le fichier /Users/macbook/small/evals/scale/runs/shopify-orders/with.md (crée-le).
Quand c'est fait, réponds uniquement : OK
