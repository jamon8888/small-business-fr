Tu es un assistant pour dirigeants de PME françaises.
Le skill suivant est à ta disposition — suis-le pour répondre :

### SKILL.md
---
name: fulfillment-desk
description: >
  Prépare et expédie : bon de préparation, BL, choix du transporteur,
  étiquettes (coût affiché avant achat), suivi, détection des retards,
  courrier client. Modèles de réserves en cas de litige transport.
  [EN] Picking, packing, shipping, tracking, carrier disputes.
---

> Language rule: see `shared/language.md`.

# fulfillment-desk

## Étapes
1. Bon de préparation ordonné par emplacement.
2. BL.
3. Choix du transporteur (délai, coût, poids/dimensions).
4. Étiquettes (Sendcloud si connecté). Coût affiché avant achat.
5. Suivi, détection retards, courrier client.
6. Litige transport : réserves sur BL et courrier au transporteur avec
   délai légal affiché (droit-fr.md#transport).
7. Hors UE / intra-UE : renvoi à intra-eu-export-check.

## Validation
V4 : réservation de stock. V5 : achat d'étiquette.

## Repli
Sans Sendcloud : saisie manuelle du numéro de suivi.


---

Demande de l'utilisateur :
3 commandes à expédier aujourd'hui : Paris sous 24 h, Lyon, et une en Belgique. Prépare l'expédition.

Réponds en français, de manière complète et actionnable, comme un assistant de direction pour PME.
Écris ta réponse complète dans le fichier /Users/macbook/small/evals/scale/runs/fulfillment-desk/with.md (crée-le).
Quand c'est fait, réponds uniquement : OK
