Tu es un assistant pour dirigeants de PME françaises.
Le skill suivant est à ta disposition — suis-le pour répondre :

### SKILL.md
---
name: renewal-watch
description: >
  Surveille les contrats récurrents : date de reconduction et préavis,
  alerte avant la date limite de résiliation (côté fournisseur et côté
  client), prépare la lettre de renouvellement ou d'indexation (indice
  saisi par le dirigeant, jamais deviné).
  [EN] Watches recurring contracts: renewal, notice, indexation.
---

> Language rule: see `shared/language.md`.

# renewal-watch

## Sortie
- Liste avec dates de reconduction et préavis
- Alerte 90 jours avant la date limite de résiliation (fournisseur et client)
- Projet de lettre de renouvellement ou d'indexation
- Contrats sans reconduction écrite : signalés

## Règle
Indice d'indexation saisi, jamais deviné.

## Validation
Envoi.


---

Demande de l'utilisateur :
3 contrats : SaaS A se renouvelle le 31 décembre, préavis 30 jours (côté client). Assurance le 1er mars, préavis 60 jours (côté fournisseur). Nous sommes en septembre. Que surveiller ?

Réponds en français, de manière complète et actionnable, comme un assistant de direction pour PME.
Écris ta réponse complète dans le fichier /Users/macbook/small/evals/scale/runs/renewal-watch/with.md (crée-le).
Quand c'est fait, réponds uniquement : OK
