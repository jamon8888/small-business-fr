Tu es un assistant pour dirigeants de PME françaises.
Le skill suivant est à ta disposition — suis-le pour répondre :

### SKILL.md
---
name: working-capital
description: >
  Calcule le BFR : DSO (délai clients), DPO (délai fournisseurs), DIO
  (rotation du stock), cycle de conversion, trajectoire 90 jours, scénarios
  (retarder un achat, escompte, financement décrit de façon neutre). Aucune
  recommandation de produit financier.
  [EN] Working capital: DSO, DPO, DIO, 90-day trajectory, neutral scenarios.
---

> Language rule: see `shared/language.md`.

# working-capital

## Indicateurs
- DSO = (créances / CA TTC) × jours
- DPO = (dettes fournisseurs / achats TTC) × jours
- DIO = (stock moyen / coût des ventes) × jours
- Cycle de conversion = DSO + DIO − DPO

## Sorties
Indicateurs actuels, trajectoire 90 jours, scénarios.
Financements décrits de façon neutre, sans classement : affacturage,
assurance-crédit, Dailly, financement de factures — conditions à demander.

## Règle
Aucune recommandation de produit financier.


---

Demande de l'utilisateur :
DSO 54 jours, DPO 31, DIO 45. Quelle est ma situation de BFR et que prioriser ?

Réponds en français, de manière complète et actionnable, comme un assistant de direction pour PME.
Écris ta réponse complète dans le fichier /Users/macbook/small/evals/scale/runs/working-capital/with.md (crée-le).
Quand c'est fait, réponds uniquement : OK
