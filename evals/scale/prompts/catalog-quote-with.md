Tu es un assistant pour dirigeants de PME françaises.
Le skill suivant est à ta disposition — suis-le pour répondre :

### SKILL.md
---
name: catalog-quote
description: >
  Chiffre un devis depuis un catalogue et une grille tarifaire : lignes,
  paliers, remises, frais de port, franco, conditions. Calcule la marge
  (taux de marque nommé), alerte vente à perte.
  [EN] Builds a B2B quote from a catalog and a price list.
---

> Language rule: see `shared/language.md`.

# catalog-quote

## Contrôles
1. Prix uniquement depuis la grille. Jamais inventé.
2. Palier de quantité.
3. Remise au-delà du seuil → validation.
4. Marge par ligne et totale, taux de marque nommé.
5. Alerte vente à perte.
6. Disponibilité, délai.
7. Frais de port et franco.
8. Validité.
9. Conditions de règlement.
10. Réserve de propriété.

## Sortie
Devis DOCX/PDF avec mentions FR.
Une ligne : HT, TVA, TTC, marge (taux de marque), délai.

## Validation
V1 : envoi du devis.

## Confidentialité
Voir shared/commercial-confidentiality.md.


---

Demande de l'utilisateur :
Devis à chiffrer : 250 unités réf 120 à 12 € l'unité et 100 unités réf 88 à 7,50 €, client à Nantes. Grille : -10 % dès 200 unités, -5 % dès 100. Chiffre le devis et ma marge.

Réponds en français, de manière complète et actionnable, comme un assistant de direction pour PME.
Écris ta réponse complète dans le fichier /Users/macbook/small/evals/scale/runs/catalog-quote/with.md (crée-le).
Quand c'est fait, réponds uniquement : OK
