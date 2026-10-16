Tu es un assistant pour dirigeants de PME françaises.
Le skill suivant est à ta disposition — suis-le pour répondre :

### SKILL.md
---
name: calendrier-fiscal-fr
description: >
  Échéancier fiscal et social personnalisé : TVA, acomptes d'IS, CFE, liasse,
  URSSAF, taxe d'apprentissage. Dates sourcées dans droit-fr.md, jamais de
  mémoire. À utiliser quand le dirigeant dit « mes échéances ».
  [EN] Personalized French tax and social calendar.
---

> Language rule: see `shared/language.md`.

# calendrier-fiscal-fr

## Entrées
Régime fiscal, Régime de TVA, Périodicité TVA, Forme juridique, salariés,
exercice.

## Échéances (exemples)
- TVA : mensuelle ou trimestrielle (15 jan/avr/juil/oct) ; CA12 annuelle
- IS : acomptes 15 mars / 15 juin / 15 sept / 15 déc ; solde au 15 du 4e mois
- CFE : 15 décembre
- URSSAF : mensuelle ou trimestrielle
- DSN : mensuelle

## Règle
Chaque ligne porte sa source (droit-fr.md#clé). Non vérifiée → [à vérifier].

## Sortie
Calendrier daté FR. Export possible vers cash-flow-snapshot et payroll-prep.


---

Demande de l'utilisateur :
SARL au réel, exercice 2026. Quelles sont mes principales échéances fiscales et sociales à venir ?

Réponds en français, de manière complète et actionnable, comme un assistant de direction pour PME.
Écris ta réponse complète dans le fichier /Users/macbook/small/evals/scale/runs/calendrier-fiscal-fr/with.md (crée-le).
Quand c'est fait, réponds uniquement : OK
