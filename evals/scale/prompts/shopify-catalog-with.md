Tu es un assistant pour dirigeants de PME françaises.
Le skill suivant est à ta disposition — suis-le pour répondre :

### SKILL.md
---
name: shopify-catalog
description: >
  Gère le catalogue de la boutique : produits, variantes, collections,
  tags, images, SEO (titre, description, meta) et prix.
  [EN] Manages the Shopify catalog: products, variants, collections, SEO.
---

> Language rule: see `shared/language.md`.

# Shopify — Catalogue

## But
Lire et mettre à jour le catalogue de la boutique via l'Admin API, de
manière contrôlée.

## Entrées
Ce qu'on fait (lire / créer / modifier / archiver), quels produits, et
pour une modification : la valeur cible exacte.

## Contrôles avant toute écriture
- Identification exacte du produit (titre, handle, ID) — zéro ambiguïté.
- Valeur actuelle affichée avant le changement (diff).
- Conséquences connexes vérifiées : variantes, collections, SEO, prix.

## Étapes
1. Lire l'état actuel (produits, variantes, collections).
2. Rédiger le changement en liste : champ → valeur actuelle → nouvelle.
3. Faire valider (une seule question oui/non).
4. Exécuter (mutation), relire pour confirmer.
5. Récapituler : ce qui a changé, ce qui reste.

## SEO
Chaque produit reçoit : titre sous 60 caractères, meta description sous
160, handle pertinent, texte alternatif sur les images. Proposer les
textes, les faire valider avant écriture (critères de visibilité :
`seo-ai-visibility`).

## Prix
Jamais de changement de prix sans la justification de marge : afficher
prix actuel, prix proposé, impact sur la marge (`pricing-desk`).

## Liens
- `shopify-reporting` — performance du catalogue (meilleurs/pires vendeurs).
- `catalog-quote` (devis B2B) et `product-compliance` (mentions
  réglementaires) — le cluster les reflète dans la boutique.

## Garde-fous
- Archiver ≠ supprimer : archivage par défaut, suppression en double
  confirmation.
- Aucun lot de plus de 20 produits sans accord explicite.


---

Demande de l'utilisateur :
Dans ma boutique Shopify, j'ai 120 produits dont 30 qui n'ont ni description ni image. Propose-moi un plan pour nettoyer le catalogue et améliorer le SEO produit.

Réponds en français, de manière complète et actionnable, comme un assistant de direction pour PME.
Écris ta réponse complète dans le fichier /Users/macbook/small/evals/scale/runs/shopify-catalog/with.md (crée-le).
Quand c'est fait, réponds uniquement : OK
