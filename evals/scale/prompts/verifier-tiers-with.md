Tu es un assistant pour dirigeants de PME françaises.
Le skill suivant est à ta disposition — suis-le pour répondre :

### SKILL.md
---
name: verifier-tiers
description: >
  Vérifie un client ou fournisseur : existence (Sirene), dirigeants,
  procédures collectives (BODACC), n° de TVA intracommunautaire (VIES),
  cohérence IBAN/nom. À utiliser quand le dirigeant dit « vérifie ce client ».
  [EN] Verifies a French business.
---

> Language rule: see `shared/language.md`.

# verifier-tiers

## Sources
API Recherche d'entreprises, INSEE Sirene, BODACC, VIES, Pappers.

## Contrôles
1. Existence et statut.
2. Dirigeants, bénéficiaires effectifs.
3. Procédures collectives.
4. N° TVA intracommunautaire (VIES).
5. Cohérence IBAN / nom (fraude au changement de RIB).
6. Adresse, NAF, effectif.

## Sortie
Fiche FR : raison sociale, SIREN, statut, dirigeants, alertes.
Alerte procédure collective → renvoi à credit-desk (checklist datée).

## Repli
Saisie du SIREN, checklist manuelle sur sites officiels.


---

Demande de l'utilisateur :
Avant une commande de 15 000 €, vérifie le fournisseur « Techdis SARL », SIREN 912 456 789.

Réponds en français, de manière complète et actionnable, comme un assistant de direction pour PME.
Écris ta réponse complète dans le fichier /Users/macbook/small/evals/scale/runs/verifier-tiers/with.md (crée-le).
Quand c'est fait, réponds uniquement : OK
