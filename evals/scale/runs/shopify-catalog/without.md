# Plan de nettoyage du catalogue et amélioration du SEO produit (Shopify)

Contexte : 120 produits, dont 30 sans description ni image. Objectif : rendre le catalogue propre, complet et optimisé pour le référencement naturel.

---

## 1. Diagnostic initial — savoir exactement où en est chaque produit

Avant de toucher quoi que ce soit, il faut une vue d'ensemble précise. Dans Shopify :

**Voyons > Produits** : trier et filtrer pour identifier rapidement les fiches incomplètes.

**Méthode recommandée (la plus fiable) : export CSV**
1. Voyons > Produits > Exporter > Tout, Format CSV.
2. Ouvrir le fichier et repérer à la louche (ou via formules Excel/Sheets) :
   - Les lignes où la colonne **Description** est vide.
   - Les lignes où la colonne **Image** (image principale) est vide.
   - Les lignes avec une **Balise Meta description** vide.
   - Les **balises Meta title** vides ou génériques (par défaut = nom du produit uniquement).
   - Les **variantes** sans photo associée.
3. Créer un tableau de suivi (Excel, Notion, ou Trello) avec pour chaque produit : nom, statut (OK / à compléter), priorisation, responsable, date de traitement.

Cet état des lieux transforme la tâche floue ("nettoyer le catalogue") en une liste de 30 fiches à traiter en priorité + les 90 fiches à fiabiliser.

**Critères d'une fiche "saine" à atteindre :**
- [ ] Image principale (obligatoire) + 2 à 5 photos supplémentaires idéalement
- [ ] Titre clair et contenant le mot-clé principal
- [ ] Description complète (150 à 300 mots minimum)
- [ ] Meta title unique et optimisé
- [ ] Meta description unique et optimisée
- [ ] Catégories/collections cohérentes
- [ ] Tags pertinents
- [ ] Variantes complètes (couleur, taille…)

---

## 2. Priorisation des 30 fiches complètes à traiter

Ne pas traiter les 30 fiches de la même manière. Classer par impact :

| Priorité | Critère | Action |
|----------|---------|--------|
| **P1 – Urgent** | Produit sans image **ni** description ET visible en ligne | Mettre hors ligne immédiatement, ou traiter en 1re semaine |
| **P2 – Important** | Produit sans image ni description, mais avec du trafic ou des ventes | Traiter en 1re semaine |
| **P3 – Moyen** | Fiche incomplète, peu de trafic | Traiter en 2e-3e semaine |
| **P4 – Faible** | Fiche incomplète, aucune vente depuis 3-6 mois | Évaluer si le produit doit être supprimé |

**Règle d'or** : un produit sans image ne doit jamais être visible à la vente. Soit on le compléte, soit on le met hors ligne. Un produit "fantôme" (page accessible mais vide) nuit à l'image de marque et au SEO.

**Décision stratégique sur les 30 produits** : pour chacun, se poser la question "cette référence doit-elle exister ?". Certains produits obsolètes ou à marge nulle peuvent simplement être **supprimés** plutôt que complétés. C'est souvent le meilleur gain : un catalogue plus petit mais de meilleure qualité.

---

## 3. Nettoyer le contenu — descriptions et images

### 3.1. Les images

Standards minimum pour e-commerce :
- **Image principale** : fond neutre/uni, produit bien cadré, minimum **2000×2000 px** (Shopify gère le zoom).
- **Images secondaires** : vue sous plusieurs angles, produit en contexte/usage, détails, dimensions.
- **Format** : JPG (photos) ou PNG (produits avec fond transparent). WebP pour l'optimisation (Shopify gère nativement).
- **Poids** : compresser sous **200-500 Ko par image** (outils : TinyPNG, Squoosh). Les images lourdes dégradent le score PageSpeed.
- **Nommage de fichier** : remplacer `IMG_2345.jpg` par un nom descriptif en minuscules avec tirets : `bott-en-coton-blanc-homme.jpg`.

### 3.2. Les descriptions — structure type

Chaque description doit suivre ce plan (150 à 300 mots) :

1. **Accroche** (1-2 phrases) : bénéfice principal, avec le mot-clé principal.
2. **Description fonctionnelle** : ce qu'est le produit, ses caractéristiques clés.
3. **Bénéfices** : ce que ça apporte au client (pas seulement la liste des specs).
4. **Caractéristiques techniques** : liste à puces (matériaux, dimensions, couleur, etc.).
5. **Appel à l'action** : incitation à l'achat.

Exemple pour un T-shirt :
> "T-shirt en coton bio pour homme — confort durable au quotidien. Confectionné en 100 % coton biologique certifié GOTS, ce t-shirt offre un tombé souple et un toucher doux qui ne déforme pas après le lavage.
> **Caractéristiques :**
> - Coton biologique 180 g/m²
> - Col rond, coupe regular
> - Lavage en machine à 30°
> - Fabriqué en Europe
> Ajoutez-le à votre panier et profitez de la livraison offerte dès 50 € d'achat."

**Points de vigilance SEO dans la description :**
- Mot-clé principal dans les 1-2 premières phrases.
- Variations naturelles du mot-clé (synonymes), sans bourrage.
- Langage orienté bénéfice, pas uniquement technique.
- Une seule balise H1 (le titre du produit) ; utiliser des H2/H3 pour structurer le texte long.

### 3.3. Automatiser à l'échelle (120 produits)

Écrire 120 descriptions à la main est long. Approche pragmatique :
- **Créer 2-3 gabarits** par famille de produits (un gabarit "vêtements", un "accessoires", etc.) avec les champs à personnaliser.
- **Assister par IA** : générer un premier jet de description par produit en fournissant le nom, les caractéristiques et le ton de marque, puis **relire et personnaliser** chaque texte. Ne jamais publier un texte brut non relu.
- **Batch via CSV** : une fois les descriptions écrites, les coller dans le fichier CSV exporté, puis **Importer > Mettre à jour les produits existants** (cocher "Mettre à jour" et importer par ID produit). C'est beaucoup plus rapide que d'édition un par un.

---

## 4. Optimiser le SEO on-page de chaque fiche

Pour chaque produit, 4 balises à soigner :

### 4.1. Meta title (balise title)
- **Longueur** : 50-60 caractères max (sinon tronqué dans Google).
- **Formule** : `Mot-clé principal + Différenciateur | Nom de marque`
- Exemples :
  - `T-shirt Coton Bio Homme – Col Rond | VotreMarque`
  - `Bottines Cuir Tannage végétal – Homme | VotreMarque`
- Un titre **unique** par produit.

### 4.2. Meta description
- **Longueur** : 150-160 caractères.
- **Contenu** : bénéfice + mot-clé + appel à l'action.
- Exemple : `T-shirt en coton bio, coupe regular et confort durable. Livraison offerte dès 50 €. Commandez votre t-shirt coton bio en ligne.`
- Unique par produit. Elle n'influence que marginalement le classement, mais conditionne fortement le **taux de clic** dans les résultats.

### 4.3. Balise alt des images
- Décrire l'image de façon naturelle avec le mot-clé quand c'est pertinent.
- Exemple : `alt="T-shirt en coton bio blanc pour homme, vue de face"`.
- Ne pas bourrer. Une image = une alt précise.

### 4.4. URL (handle)
- Courte, en minuscules, avec tirets, contenant le mot-clé.
- Exemple : `/produits/t-shirt-coton-bio-blanc`
- **Important** : si une URL contient des caractères parasites (ex. `t-shirt-coton-bio-123`), la renommer via **Voyons > Produits > Modifier > Gérer les URL / handle** et créer une **redirection 301** vers l'ancienne URL pour ne pas perdre le référencement acquis.

---

## 5. Structurer le catalogue (collections et navigation)

- **Collections** : regrouper les produits en collections thématiques claires (Homme / Femme / Accessoires ; Nouveautés ; Promotions ; par catégorie). Chaque collection a sa propre page, son propre meta title et sa propre meta description.
- **Hiérarchie** : éviter d'avoir 120 produits dans une seule collection "Tout". Proposer un chemin de navigation en 2-3 niveaux max.
- **Tags** : utiliser de façon cohérente pour alimenter les collections dynamiques (ex. tag `bio` sur tous les produits biologiques).
- **Filtres** : activer les filtres par attribut (couleur, taille, prix) pour améliorer la navigation et créer des pages facettes indexables.

---

## 6. SEO technique — les fondamentaux

- **Balises Hn** : un seul H1 par page produit (le titre).
- **Open Graph / social** : prévoir une meta og:image (Shopify l'utilise pour le partage Facebook/LinkedIn/WhatsApp).
- **Data structuré (Schema.org)** : Shopify génère automatiquement le balisage `Product` (nom, prix, disponibilité, SKU, image) via les JSON-LD. Vérifier dans le code source que ce balisage est bien présent sur les fiches. C'est ce qui alimente les **rich snippets** (étoiles, prix, disponibilité) dans Google.
- **Fichier sitemap** : `votredomaine.com/sitemap.xml` — s'assurer qu'il est déclaré dans Search Console.
- **Google Search Console** : vérifier les pages avec "Aucun résultat" ou "Erreur 4xx", soumettre le sitemap, surveiller les requêtes de recherche par page.
- **Performance** : images compressées (cf. §3.1), thème léger. Un score PageSpeed mobile > 90 est un objectif raisonnable.
- **HTTPS + pas de contenu dupliqué** : un seul domaine (choisir `https://votredomaine.com`, pas `myshop.myshopify.com`), éviter les pages de collection vides qui créent du contenu dupliqué.

---

## 7. Contenu dupliqué et pages à surveiller

- **Pages vides** : collections sans produit, catégories orphelines → les fusionner ou les supprimer avec redirection.
- **Produits dupliqués** : deux fiches pour le même produit (ex. variantes transformées à tort en produits distincts) → fusionner et rediriger.
- **Descriptions identiques** : deux produits avec le même texte → réécrire pour les différencier.

---

## 8. Plan d'action sur 4 semaines

### Semaine 1 — Cadrage + urgence
- [ ] Export CSV complet, tableur de suivi créé.
- [ ] Identifier et **mettre hors ligne** les produits P1 (sans image ET sans description, mais visibles).
- [ ] Décider du sort des 30 produits (compléter vs supprimer).
- [ ] Installer Google Search Console + soumettre le sitemap.

### Semaine 2 — Priorités SEO (P1/P2)
- [ ] Traiter les 10-15 fiches P1/P2 : photos, description, meta title, meta description.
- [ ] Mettre en place les gabarits de description.
- [ ] Corriger les URLs problématiques avec redirections 301.

### Semaine 3 — Catalogue complet (P3)
- [ ] Compléter les fiches P3 par lots de 10-15 (batch via CSV).
- [ ] Structurer les collections + filtres.
- [ ] Vérifier les balises alt sur toutes les images.

### Semaine 4 — Finitions + SEO technique
- [ ] Vérifier le Schema.org / JSON-LD sur un échantillon de fiches.
- [ ] Révision PageSpeed (images, thème).
- [ ] Nettoyage des pages vides/dupliquées avec redirections.
- [ ] Relance en Search Console pour re-crawling.

---

## 9. Mise en place durable (process récurrent)

Le nettoyage ne doit pas se refaire chaque mois. Mettre en place :

- **Check-list qualité "avant mise en ligne"** pour tout nouveau produit :
  - [ ] Image principale + 2+ secondaires
  - [ ] Description complète (150+ mots)
  - [ ] Meta title unique
  - [ ] Meta description unique
  - [ ] URL propre
  - [ ] Balises alt
  - [ ] Bonne collection
- **Revue trimestrielle** : exporter le CSV, vérifier les fiches vides, vérifier les produits sans vente depuis 6 mois (candidats à suppression ou promotion).
- **Rôle dédié** : désigner une personne (même à mi-temps) responsable de la qualité catalogue.

---

## 10. KPIs pour mesurer l'impact

| Indicateur | Où le mesurer | Cible |
|------------|---------------|-------|
| % de fiches complètes (image + description + meta) | Export CSV | 100 % à 1 mois |
| Taux de clic (CTR) moyen sur les fiches produits | Search Console | +20 % à 3 mois |
| Pages indexées | Search Console > Pages | Stable ou en hausse |
| Trafic organique vers /produits/ | Google Analytics | En hausse progressive |
| Score PageSpeed mobile | PageSpeed Insights | > 90 |
| Taux de conversion | Shopify | Stable ou en hausse |
| Part des rich snippets | Search Console > Améliorations | Présence confirmée |

---

## Résumé exécutif

1. **D'abord, diagnostiquer** : exporter le CSV, lister les 30 fiches vides, prioriser.
2. **Mettre hors ligne** les produits sans image visibles à la vente — c'est l'urgence n°1.
3. **Décider** : compléter ou supprimer certains des 30 produits (le plus petit catalogue de meilleure qualité l'emporte).
4. **Compléter** les fiches avec photos + descriptions structurées + meta titles + meta descriptions + balises alt, en utilisant des gabarits et l'import CSV par lots.
5. **Soigner le SEO technique** : URLs propres avec redirections 301, Schema.org, sitemap, Search Console, PageSpeed.
6. **Structurer** les collections et la navigation.
7. **Institutionnaliser** avec une check-list avant mise en ligne et une revue trimestrielle.

Le plus gros levier n'est pas la quantité de texte, c'est **l'uniformité** : 120 fiches au même standard de qualité, toutes indexables, toutes avec les bonnes balises. C'est ce qui transforme un catalogue "en vrac" en un actif de référencement.
