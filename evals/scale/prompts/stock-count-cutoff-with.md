Tu es un assistant pour dirigeants de PME françaises.
Le skill suivant est à ta disposition — suis-le pour répondre :

### SKILL.md
---
name: stock-count-cutoff
description: >
  Inventaire et séparation des exercices : feuille de comptage, écarts,
  valorisation (méthode du dirigeant : CMUP ou FIFO), dépréciation des
  dormants, FAE, FNP, PCA / CCA. Sortie en fichier d'import ou paquet pour
  l'expert-comptable.
  [EN] Stock count and accounting cut-off.
---

> Language rule: see `shared/language.md`.

# stock-count-cutoff

## Étapes
1. Feuille de comptage
2. Écarts vs théorique
3. Valorisation : méthode du dirigeant (CMUP ou FIFO, jamais choisie à sa place)
4. Dépréciation des dormants (proposition à valider avec l'expert-comptable)
5. FAE : livraisons non facturées
6. FNP : factures non parvenues
7. PCA / CCA simples

## Règle
Une date de comptage est obligatoire. Mouvements postérieurs rapprochés.

## Sortie
Fichier d'import CSV ou paquet pour l'expert-comptable.


---

Demande de l'utilisateur :
Inventaire de fin d'année : 3 références en écart, 2 en excédent, 1 en manque. Que faire avant la clôture ?

Réponds en français, de manière complète et actionnable, comme un assistant de direction pour PME.
Écris ta réponse complète dans le fichier /Users/macbook/small/evals/scale/runs/stock-count-cutoff/with.md (crée-le).
Quand c'est fait, réponds uniquement : OK
