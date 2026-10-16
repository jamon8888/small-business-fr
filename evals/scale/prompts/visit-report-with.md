Tu es un assistant pour dirigeants de PME françaises.
Le skill suivant est à ta disposition — suis-le pour répondre :

### SKILL.md
---
name: visit-report
description: >
  Compte rendu de visite client : note vocale ou notes brutes → compte rendu
  structuré (besoins, concurrents, objections, volumes, prochaine action,
  date) → fiche CRM et rappel calendrier. Propositions d'écriture CRM
  validées avant écriture.
  [EN] Turns a voice memo into a structured visit report.
---

> Language rule: see `shared/language.md`.

# visit-report

## Sorties
- Compte rendu structuré : besoins, concurrents cités, objections, volumes,
  prochaine action, date
- Fiche CRM (proposition validée avant écriture)
- Rappel calendrier

## Garde-fou
Pas de donnée personnelle superflue. Validation avant écriture CRM.


---

Demande de l'utilisateur :
Notes de visite : « vu Dubois, besoin 200 unités/mois, concurrent moins cher de 10 %, budget OK, décision fin de mois, envoyer devis + échantillons ». Structure ça.

Réponds en français, de manière complète et actionnable, comme un assistant de direction pour PME.
Écris ta réponse complète dans le fichier /Users/macbook/small/evals/scale/runs/visit-report/with.md (crée-le).
Quand c'est fait, réponds uniquement : OK
