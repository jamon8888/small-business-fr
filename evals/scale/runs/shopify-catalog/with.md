# Plan de nettoyage du catalogue Shopify et d'amélioration du SEO produit

## 1. Diagnostic — lecture de l'état actuel

Avant toute écriture, un audit complet est d'abord effectué via l'Admin API (lecture seule, aucune modification). L'audit couvre les 120 produits et produit :

- **Inventaire par état** : produits complets (description + image), produits incomplets (30), produits obsolètes ou en fin de stock.
- **Liste nominative des 30 produits incomplets**, avec pour chacun : titre actuel, handle, ID, prix, collections rattachées, statut (actif/archivé), nombre de variantes.
- **Contrôle SEO** : pour chaque produit, vérification des 4 critères — titre de fiche < 60 caractères, meta description < 160 caractères, handle propre (courts, sans accents, sans chiffres inutiles), texte alternatif présent sur au moins la première image.
- **Contrôle prix** : recensement des produits dont la marge n'est plus défendable (signalé séparément, aucune modification de prix sans justification de marge).

L'audit est restitué sous forme de tableau trié par priorité (produits à archiver d'abord, puis produits à compléter par ordre de potentiel de vente).

## 2. Nettoyage du catalogue — tris à opérer

Les 30 produits sans description ni image sont triés en trois catégories, à valider avec vous à l'issue de l'audit :

| Catégorie | Critère | Action |
|---|---|---|
| A. Produits à archiver | Hors catalogue depuis > 6 mois, plus de stock, remplacements existants | **Archivage** (jamais suppression sans double confirmation) |
| B. Produits à compléter | Toujours vendus ou à fort potentiel | Création de description + ajout d'images + correction SEO |
| C. Produits dupliqués | Variants d'un même produit publié en fiches séparées | Fusion de l'inventaire, archivage de la fiche redondante |

**Règles appliquées :**
- L'archivage est l'action par défaut ; aucune suppression définitive sans double confirmation explicite.
- Aucun lot de plus de **20 produits** n'est traité sans votre accord explicite. Avec 30 produits concernés, le travail est découpé en **2 lots de 15 produits maximum** (catégories A + C d'un côté, catégorie B de l'autre), chacun validé séparément.
- Chaque modification est tracée : champ → valeur actuelle → nouvelle valeur, avec diff affiché avant écriture.

## 3. Plan SEO produit — les 4 corrections à systematiser

Pour chaque produit complété (catégorie B) et pour le reste du catalogue en second passage :

### 3.1 Titre de fiche (< 60 caractères)
Formule : **Marque + Type de produit + Atout principal + Référence taille/coloris si pertinent**.
Exemple : `Mug céramique artisanal La Bouche — motif lavande, 35 cl` (54 car.).

### 3.2 Meta description (< 160 caractères)
Structure : **bénéfice client + détail concret + appel à l'action**.
Exemple : `Mug en céramique artisanale, motif lavande peint à la main. Passe au lave-vaisselle, capacité 35 cl. Livraison 48 h en France. Commandez en ligne.` (148 car.).
Chaque meta description est rédigée en version unique (jamais dupliquée entre produits) et validée avant écriture.

### 3.3 Handles propres
- Un handle = le titre condensé, sans accents, sans espaces, sans numéros de version : `mug-ceramique-lavande-35cl`.
- Un handle est **modifié une seule fois dans la vie du produit** : chaque changement de handle casse l'URL existante et détruit le SEO acquis. Pour les produits déjà en ligne avec du trafic, le handle est conservé et un **redirigement 301** est mis en place si un nettoyage s'avère indispensable.

### 3.4 Images et textes alternatifs
- Minimum 2 images par produit (1 vue principale + 1 en contexte), format 2048 × 2048 px minimum, poids < 200 Ko après compression.
- Texte alternatif descriptif incluant le mot-clé principal : `Mug en céramique motif lavande vu de trois quarts` (jamais de balayage automatique du titre — chaque alt est unique).

## 4. Exemples de réécriture (produits types)

| Produit | Avant | Après (titre) | Après (meta description) |
|---|---|---|---|
| T-shirt noir (ex.) | `Tee shirt noir 15,90` / aucune description | `T-shirt col rond en coton bio — noir, coupe droite` (49) | `T-shirt en coton bio 220 g/m², coupe droite et col rond renforcé. Lavage 30°. Noir intemporel. Livraison 48 h, retours gratuits 30 j.` (132) |
| Vase en verre (ex.) | `Vase` / aucune description, 1 image floue | `Vase en verre soufflé — forme haute, 24 cm` (43) | `Vase en verre soufflé à la main, silhouette haute de 24 cm. Pièce artisanale unique, parfaite pour branches séchées et compositions naturelles.` (137) |

Les textes réels seront proposés produit par produit, avec affichage du contenu actuel, puis validés par vous avant toute écriture.

## 5. Déroulé opérationnel (contrôlé, pas à pas)

1. **Jour 1 — Audit** : lecture des 120 produits, restitution du tableau de tri (A/B/C) et de la liste des non-conformités SEO. Aucune écriture.
2. **Jour 2 — Validation du tri** : une seule question oui/non : « Validez-vous le tri proposé : 8 produits archivés, 2 dupliqués fusionnés, 20 produits à compléter ? »
3. **Jour 2-3 — Lot 1 (≤ 15 produits)** : archivages et fusions. Pour chaque produit : identification exacte (titre + handle + ID), diff affiché, exécution, relire pour confirmer.
4. **Jour 4 — Lot 2 (≤ 15 produits)** : complétion des fiches — descriptions rédigées, images importées, titres, meta descriptions, handles, textes alternatifs. Chaque texte est affiché (actuel → nouveau) avant écriture.
5. **Semaine 2 — Passage SEO sur les 90 produits complets** : contrôle titre/meta/handle/alt des fiches restantes, corrections ciblées par lots de 15, redirigements 301 uniquement si un handle doit bouger.
6. **Clôture — Récapitulatif final** : ce qui a changé (nombres d'archivages, fiches complétées, champs SEO corrigés), ce qui reste (produits en attente de photos, marges à revoir), et mesures de suivi.

## 6. Suivi après nettoyage

- **Performance du catalogue** : suivi des meilleurs et pires vendeurs (skill `shopify-reporting`) à J+14 et J+30 pour mesurer l'effet du nettoyage.
- **Indicateurs SEO** : impressions et CTR des fiches complétées dans Google Search Console à J+30 ; objectif : disparition des fiches sans description des résultats de recherche, CTR stable ou en hausse.
- **Alerte marge** : les produits dont le prix doit être revu sont listés séparément — aucun changement de prix n'est proposé sans justification de marge affichée (prix actuel, prix proposé, impact marge).
- **Règle durable** : tout nouveau produit est soumis au même contrôle 4 critères (titre, meta, handle, alt) avant mise en ligne, pour ne plus réintégrer de fiche incomplète dans le catalogue.

## 7. Ce que je fais maintenant

L'audit en lecture seule de vos 120 produits peut être lancé immédiatement. Il est sans impact sur la boutique : aucun produit, prix, collection ou page SEO n'est modifié à cette étape.
