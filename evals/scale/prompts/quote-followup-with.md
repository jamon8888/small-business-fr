Tu es un assistant pour dirigeants de PME françaises.
Le skill suivant est à ta disposition — suis-le pour répondre :

### SKILL.md
---
name: quote-followup
description: >
  Classe les devis ouverts par montant et ancienneté, propose une relance
  par étape (rappel, levée d'objection, expiration), marque les devis
  expirés. La probabilité est saisie par le dirigeant.
  [EN] Follows up on open quotes.
---

> Language rule: see `shared/language.md`.

# quote-followup

## Règle
Probabilité saisie, jamais inventée.

## Étapes de relance
- J+7 : rappel cordial
- J+15 : levée d'objection
- J+30 : expiration de l'offre

## Sortie
Tableau trié montant × ancienneté, projet de relance par devis.

## Validation
Envoi.


---

Demande de l'utilisateur :
4 devis ouverts : 12 400 € (21 jours), 3 900 € (8 jours), 8 200 € (35 jours, expire dans 2 jours), 1 500 € (3 jours). Par quoi je commence ?

Réponds en français, de manière complète et actionnable, comme un assistant de direction pour PME.
Écris ta réponse complète dans le fichier /Users/macbook/small/evals/scale/runs/quote-followup/with.md (crée-le).
Quand c'est fait, réponds uniquement : OK
