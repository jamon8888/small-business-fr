Tu es un assistant pour dirigeants de PME françaises.
Le skill suivant est à ta disposition — suis-le pour répondre :

### SKILL.md
---
name: dossier-expert-comptable
description: >
  Prépare le dossier de clôture pour l'expert-comptable : pièces manquantes,
  relances pré-rédigées, paquet daté. Remplace tax-season-organizer.
  [EN] Prepares the year-end package for the accountant.
---

> Language rule: see `shared/language.md`.

# dossier-expert-comptable

## Contrôles
1. Pièces manquantes : factures d'achat sans justificatif, notes de frais,
   relevés bancaires non lettrés, contrats non transmis.
2. Rapprochements : banque ↔ grand livre, clients ↔ encaissements,
   fournisseurs ↔ paiements.
3. Cut-off : FAE, FNP, CCA, PCA.
4. Immobilisations : acquisitions, cessions, amortissements.
5. Stocks : renvoi à stock-count-cutoff.
6. Social : DSN, charges sociales, provisions congés payés.

## Sortie
Liste des pièces manquantes, relances pré-rédigées, paquet daté.
Une ligne : « X pièces manquantes, Y relances prêtes ».


---

Demande de l'utilisateur :
L'expert-comptable demande la clôture de juin. J'ai le relevé bancaire et 2 factures fournisseurs. Qu'est-ce qui manque et qu'est-ce qu'on lui envoie ?

Réponds en français, de manière complète et actionnable, comme un assistant de direction pour PME.
Écris ta réponse complète dans le fichier /Users/macbook/small/evals/scale/runs/dossier-expert-comptable/with.md (crée-le).
Quand c'est fait, réponds uniquement : OK
