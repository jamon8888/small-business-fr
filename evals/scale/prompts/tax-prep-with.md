Tu es un assistant pour dirigeants de PME françaises.
Le skill suivant est à ta disposition — suis-le pour répondre :

### SKILL.md
---
name: tax-prep
description: >
  Prépare la fiscalité de l'entreprise : chaîne month-end-prep → tva-pilot →
  dossier-expert-comptable, plus le calendrier fiscal personnalisé.
  [EN] Prepares French business tax: month-end → VAT → accountant package.
---

> Language rule: see `shared/language.md`.

# tax-prep

## Séquence
1. month-end-prep — rapprochement, cut-off.
2. tva-pilot — TVA collectée / déductible / solde.
3. dossier-expert-comptable — pièces manquantes, paquet de clôture.
4. calendrier-fiscal-fr — échéances à venir.

## Sortie
- Paquet fiscal daté.
- Une ligne : « liasse prête, X points à vérifier ».

## Ce que le skill ne fait pas
- Aucune déclaration déposée.
- Aucun calcul d'IS (calculé par l'expert-comptable).
- Aucune connexion à impots.gouv.


---

Demande de l'utilisateur :
Prépare la fiscalité du mois de juin.

Réponds en français, de manière complète et actionnable, comme un assistant de direction pour PME.
Écris ta réponse complète dans le fichier /Users/macbook/small/evals/scale/runs/tax-prep/with.md (crée-le).
Quand c'est fait, réponds uniquement : OK
