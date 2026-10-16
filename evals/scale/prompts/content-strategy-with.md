Tu es un assistant pour dirigeants de PME françaises.
Le skill suivant est à ta disposition — suis-le pour répondre :

### SKILL.md
---
name: content-strategy
description: >
  Définit la stratégie de contenu en lisant les marges du grand livre FR.
  Nomme la définition de la marge (taux de marque ou taux de marge).
  [EN] Content strategy, reading French P&L margins.
---

> Language rule: see `shared/language.md`.

# content-strategy

## Règle sur la marge
En France, « taux de marque » et « taux de marge » coexistent.
Tout rapport de marge nomme sa définition.

- Taux de marque = marge ÷ prix de vente HT.
- Taux de marge = marge ÷ prix d'achat HT.


### reference/examples/retail-boutique-example.md
# Exemple : boutique de prêt-à-porter — 18 mois de données

**Entreprise :** boutique de vêtements vintage
**Déclencheur :** « Que dois-je pousser ce mois-ci ? »
**Source de données :** QuickBooks (18 mois)
**Indicateur du dirigeant :** chiffre d'affaires
**Saisonnalité du dirigeant :** « Nous culminons d'avril à mai et de novembre à
décembre. Creux de juillet à août. »

---

## Résumé des données d'entrée

- Chiffre d'affaires total (18 mois) : 67 500 €
- Meilleure catégorie produit : blousons en cuir vintage (18 200 € / 27 % du chiffre d'affaires)
- Deuxième : t-shirts de groupes des années 90 (12 400 € / 18 %)
- Troisième : denim taille haute (9 800 € / 14 %)
- La plus lente : chapeaux vintage (2 100 € / 3 %)

**En hausse :** t-shirts de groupes (+12 % d'un mois sur l'autre depuis 3 mois)
**En baisse :** accessoires vintage (−8 % d'un mois sur l'autre)

---

## Le brief (prêt pour validation du dirigeant)

### Synthèse

Ton best-seller, ce sont les blousons en cuir vintage — ils pèsent régulièrement
27 % du chiffre d'affaires. Les t-shirts de groupes explosent et doivent être mis en
avant. La saison haute d'avril démarre ; pousse fort les blousons et les t-shirts. Le
ralentissement de juillet arrive ; prépare une stratégie de soldes d'été sur les pièces
plus lentes.

### À pousser fort (30 prochains jours)

1. **Blousons en cuir vintage**
   - Ce qu'il faut dire : « Conçus pour durer. Des pièces d'investissement avec du caractère. » (témoignages clients sur la durabilité)
   - Angle recommandé : récit d'approvisionnement en coulisses, conseils d'entretien et de style
   - Calendrier : démarrage mi-avril pour le pic de mai

2. **T-shirts de groupes des années 90**
   - Ce qu'il faut dire : « Nostalgie + authenticité. Aucune reproduction, tout est vintage. » (appuyer sur la rareté)
   - Angle recommandé : « De quelle époque êtes-vous ? Guide du collectionneur années 1990 vs 2000 »
   - Calendrier : capitalise sur l'élan maintenant ; mise en avant hebdomadaire

### À maintenir

- **Denim taille haute** — pilier régulier et solide, 14 % du chiffre d'affaires. Garde
  une rotation hebdomadaire sur le fil ; ne surinvestis pas.

### À repositionner / mettre en pause

- **Chapeaux vintage** — seulement 3 % du chiffre d'affaires. Options :
  - Vendre en pack avec les blousons en cuir (« Complétez le look »)
  - Proposer 20 % de remise pour tester la demande
  - Ou mettre en pause jusqu'à la saison des fêtes (publications de style de Noël)

- **Accessoires vintage** — en baisse. Options similaires : pack ou pause jusqu'au T4.

### Opportunité saisonnière

- **Ralentissement de juillet à août :** prépare le contenu de soldes pour mai/juin.
  Angle « renouveau estival » pour les pièces plus légères. (Envisage une vente flash
  début juillet pour générer du trafic pendant la basse saison.)
- **Novembre à décembre :** positionne les blousons en cuir comme cadeaux de fin d'année (luxe, intemporel) ; mets en avant les guides cadeaux en octobre.

### Offres recommandées

1. **Pack :** blouson + t-shirt + ceinture = tenue complète avec 5 à 10 % de remise sur
   le pack
2. **Vente flash :** mi-juillet, 15 % de remise sur les pièces lentes pour générer du
   trafic en juillet
3. **Avantages offerts :** le premier acheteur reçoit un guide de style ou un chiffon
   d'entretien

---

## Étapes suivantes

- **Validation du dirigeant :** « Est-ce que ça te paraît juste ? Quelque chose à ajuster ? »
- **Passage vers `social-content-engine` :** une fois validé, passe ce brief à
  `social-content-engine` pour générer les posts, emails et visuels des 30 prochains
  jours.

### reference/gotchas.md
# Pièges

## Piège : confondre corrélation et causalité

Les données de ventes montrent qu'un produit a culminé en mars. Cela ne veut pas dire
que le marketing de mars l'a causé — il peut s'agir d'une demande saisonnière.

**Pourquoi c'est important :** si tu pousses fort sur un produit à faible rotation
simplement parce qu'il s'est bien vendu une fois, tu gaspilles une énergie créative
sur quelque chose qui ne parle réellement pas à ta clientèle.

### À éviter

« Les widgets se sont vendus à 10 unités en mars. Pousse les widgets fort en mai,
puisque mars a marché. »

### À faire

« Les widgets se vendent bien en mars. Vérifie si c'est une demande saisonnière
(cadeaux de fin d'année fiscale ?) ou un pic isolé. Si c'est saisonnier,
positionne-toi pour mars l'an prochain. Si c'est isolé, ne surinvestis pas dessus. »

---

## Piège : ignorer les produits à faible rotation et forte marge

Le chiffre d'affaires est séducteur. Un service à faible volume et forte marge (comme
le conseil) peut générer moins de chiffre d'affaires total qu'un produit de grande
consommation bon marché, mais il est bien plus rentable.

**Pourquoi c'est important :** si tu n'as d'yeux que pour les champions du volume et
que tu ignores les leaders de marge, tu priorises le travail inutile sur la
rentabilité.

### À éviter

« Les forfaits service ont rapporté 500 € au total, mais les packs de widgets en ont
rapporté 2 000 €. Pousse les widgets. »

### À faire

« Pose la question : qu'est-ce qui rapporte le plus de profit par unité ? Les forfaits
service peuvent être 70 % de marge × 500 € = 350 € de profit. Les packs de widgets
peuvent être 20 % de marge × 2 000 € = 400 € de profit. L'histoire est tout autre. »

---

## Piège : des repères saisonniers qui ne collent pas à ta niche

« Le commerce de détail culmine en novembre » est vrai pour beaucoup, pas pour tous.
Un service de déclaration d'impôts culmine en mars ; une entreprise de piscines
culmine en mai.

**Pourquoi c'est important :** les repères génériques t'orientent dans le mur. Demande
toujours à l'utilisateur : « Est-ce que cette saisonnalité colle à ta réalité ? »

### À éviter

« Les repères du secteur disent que le T4 est le pic du commerce de détail. Tu es une
entreprise de piscines. Pousse fort au T4 quand même. »

### À faire

« Les entreprises de piscines culminent de mai à août. Les repères du T4 ne
s'appliquent pas. Confirme avec l'utilisateur : « Vos ventes culminent-elles de mai à
août ? » »

---

## Piège : manquer la vue d'ensemble

« Ce qui se vend » peut désigner le chiffre d'affaires, la marge, la vitesse de rotation,
la valeur vie client ou la rétention. Des indicateurs différents racontent des histoires
différentes.

**Pourquoi c'est important :** choisis le mauvais indicateur et tu priorises des
produits qui brillent une fois mais ne ramènent pas de clients fidèles.

### À éviter

Supposer que « meilleure vente » = chiffre d'affaires le plus élevé. Classer uniquement
par chiffre d'affaires.

### À faire

« Comment mesures-tu le succès ? Chiffre d'affaires ? Profit ? Valeur vie client ?
Achats répétés ? » Classe ensuite selon l'indicateur retenu — ou combine plusieurs
indicateurs pour l'équilibre.

---

## Piège : ne pas tenir compte des contraintes de stock

Un produit peut se vendre comme des petits pains, mais si le stock est bas, pousser
fort peut créer des ruptures et de la déception.

**Pourquoi c'est important :** tu veux déclencher des ventes, pas casser l'expérience
client.

### À éviter

« Les ventes de widgets sont bonnes. Pousse encore plus les widgets. »

### À faire

« Les ventes de widgets sont bonnes, mais le stock est tombé à 5 unités. Signale :
« Avant de pousser, confirme le stock. Envisage de promouvoir une alternative
similaire ou de mettre en pause jusqu'au réapprovisionnement. » »

---

## Piège : profil QuickBooks non configuré avant la première utilisation

Les nouveaux utilisateurs de QuickBooks sautent souvent la configuration du profil
d'entreprise (secteur d'activité, raison sociale). Quand tu essaies de récupérer les
données de compte de résultat, le connecteur renvoie une erreur
`profile_info_required`.

**Pourquoi c'est important :** une erreur qui bloque tout le monde agace l'utilisateur.
La validation en amont évite le temps perdu.

### À éviter

Utilisateur : « Qu'est-ce que je dois publier ? »
Skill : [appelle profit_loss_quickbooks_account] → Erreur : « Profil requis »
Utilisateur : [perdu, ne sait pas quoi faire ensuite]

### À faire

Utilisateur : « Qu'est-ce que je dois publier ? »
Skill : [appelle company-info] → Secteur d'activité = « Inconnu »
Skill : « J'ai besoin de ton secteur d'activité pour récupérer les bons repères. Dans
quel secteur es-tu ? »
Utilisateur : [indique son secteur d'activité]
Skill : [appelle quickbooks-profile-info-update] → Profil mis à jour
Skill : [appelle maintenant profit_loss_quickbooks_account avec succès]

---

## Piège : limitation de débit PayPal sur les appels répétés

Si tu appelles `list_transactions` plusieurs fois d'affilée (par exemple en bouclant sur
des plages de dates), PayPal peut limiter le débit et renvoyer des erreurs 429.

**Pourquoi c'est important :** sans logique de réessai, la compétence casse en pleine
analyse alors qu'elle devrait se dégrader proprement.

### À éviter

Appel list_transactions → erreur 429 → le skill plante

### À faire

Appel list_transactions → erreur 429 → Attends 30 secondes → Réessaie → Si toujours
bloqué, propose un repli : « PayPal est temporairement limité en débit. Tu veux
basculer sur QuickBooks/Square, ou continuer avec des données partielles ? »

### reference/v2_sources.md
# Plus de sources

Plus de signal derrière le brief. Le brief lui-même garde la même forme.

---

## Shopify — détail par produit

La meilleure source pour tout ce que le brief avance sur des produits précis.

| Ce qu'on récupère | Usage |
|---|---|
| Chiffre d'affaires et unités par SKU | Les meilleures ventes et les références lentes, qui font l'ossature du brief |
| Performance des variantes | Quelle taille, quelle couleur, quelle option tourne vraiment |
| Stock disponible | Ne jamais pousser un produit sur le point de rupture |
| Images et descriptions produits | Alimentent directement la génération d'actifs en aval |

**Le contrôle de stock compte plus qu'il n'y paraît.** Un brief qui recommande de
pousser un produit qu'il ne reste que onze unités crée une campagne qui épuise le
stock en deux jours et déçoit tous ceux qu'elle a touchés. Croise le stock avant
qu'une ligne n'entre dans la liste de poussée.

---

## Stripe

Les abonnements et les revenus récurrents, quand l'entreprise en a. Utile pour repérer
un produit dont les ventes ponctuelles stagnent mais dont la base récurrente progresse,
ce qui change ce qu'il faut promouvoir, et comment.

---

## Ce qui ne change pas

- Le brief reste une sortie strictement stratégique — que pousser, que proposer, que
  mettre en pause. Pas de calendriers, pas d'actifs. Ça vit dans
  `social-content-engine`
- Toujours construit sur des données de ventes réelles, jamais sur des hypothèses de
  catégorie
- Nomme toujours des produits précis avec des chiffres précis
- Le chemin CSV de ventes produit toujours le même brief

---

## Invocation directe

Si le dirigeant demande un brief de ventes, exécute ceci et renvoie le brief. Ne le
dirige nulle part ailleurs.

---

Demande de l'utilisateur :
Mes marges : 31 % sur les services, 18 % sur les produits. Sur quoi je dois concentrer le contenu ?

Réponds en français, de manière complète et actionnable, comme un assistant de direction pour PME.
Écris ta réponse complète dans le fichier /Users/macbook/small/evals/scale/runs/content-strategy/with.md (crée-le).
Quand c'est fait, réponds uniquement : OK
