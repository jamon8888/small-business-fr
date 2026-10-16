Tu es un assistant pour dirigeants de PME françaises.
Le skill suivant est à ta disposition — suis-le pour répondre :

### SKILL.md
---
name: credit-desk
description: >
  Calcule l'encours client (factures ouvertes + commandes confirmées non
  facturées), le compare au plafond, classe en vert / vigilance / bloqué,
  contrôle l'assurance-crédit, surveille le BODACC, alerte sur les
  procédures collectives avec checklist datée.
  [EN] Customer credit exposure and risk: limit, insurance, insolvency.
---

> Language rule: see `shared/language.md`.

# credit-desk

## Calcul
Encours = factures ouvertes + commandes confirmées non facturées.
- Vert : < 80 % du plafond
- Vigilance : 80 % ≤ encours < plafond
- Bloqué : ≥ plafond ou alerte BODACC

## Alerte procédure collective — checklist datée [à vérifier avec un avocat]
- Déclaration de créance dans le délai court après BODACC
- Revendication au titre de la réserve de propriété
- Arrêt des livraisons à crédit
- Sortie du circuit de relance courant

## Gate
Tout déblocage de commande est une décision du dirigeant.


---

Demande de l'utilisateur :
Client X : 8 900 € de factures ouvertes et 2 000 € de commandes confirmées non facturées. Son plafond est de 10 000 €. Je confirme la nouvelle commande ?

Réponds en français, de manière complète et actionnable, comme un assistant de direction pour PME.
Écris ta réponse complète dans le fichier /Users/macbook/small/evals/scale/runs/credit-desk/with.md (crée-le).
Quand c'est fait, réponds uniquement : OK
