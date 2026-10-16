Tu es un assistant pour dirigeants de PME françaises.
Le skill suivant est à ta disposition — suis-le pour répondre :

### SKILL.md
---
name: inventory-planner
description: >
  Détermine quoi recommander et quand, à partir de ce qui se vend vraiment :
  récupère l'historique des ventes et le stock physique depuis Shopify, Square,
  NetSuite ou un CSV déposé, calcule la vitesse sur 7 et 28 jours par référence,
  projette une date de rupture prudente, dimensionne une quantité de
  réapprovisionnement à 60 jours, et rédige les bons de commande et les mails
  fournisseurs pour la couvrir. Signale le surstock, le stock dormant et les
  articles à vitesse nulle comme des rotulants à écouler. Rien n'est commandé et
  aucun fournisseur n'est contacté sans validation. Saisis-le dès que le stock
  arrive — « que dois-je recommander », « vais-je manquer », « on manque
  toujours de filtres », « combien d'argent dort dans l'entrepôt », « qu'est-ce
  qui ne bouge pas ».
  [EN] Reach for this whenever stock comes up — "what do I need to
  reorder," "am I going to run out," "what is not moving."
allowed-tools: Read, WebFetch
---

> Language rule: see `shared/language.md`.
> Note : pour les profils negoce et fabrication, utiliser
> b2b-stock-planner et procure-to-pay à la place.

# Planificateur de stock

Achète ce qui se vend, avant que ça manque, et arrête d'acheter ce qui ne se vend pas.

Le stock, c'est de l'argent que le dirigeant a déjà dépensé. Deux choses tournent mal : manquer de l'article que les clients étaient venus chercher, et rester assis sur une palette de quelque chose que personne ne veut. Les deux se voient dans l'historique des ventes bien avant de devenir un problème, et c'est exactement ce que ce skill lit.

## Étape 1 — Obtenir les ventes et le stock

**Préféré :** Shopify pour les ventes et les niveaux de stock. Square et NetSuite fonctionnent de la même façon.

**Repli, entièrement pris en charge :** un CSV d'historique de ventes plus un comptage de stock physique. Deux fichiers, ou un seul avec les deux. Ce chemin fonctionne sans aucun connecteur et donne la même sortie. Beaucoup d'entreprises comptent sur une ardoise, et c'est une entrée légitime.

Il te faut, par référence : le SKU, le nom, les unités vendues par date, le stock physique actuel, le coût unitaire, le prix unitaire, le fournisseur, et le délai si connu. Un délai manquant se demande une fois et se mémorise — voir `reference/data_sources.md`.

**Dis à quelle date se rapporte le comptage.** Un chiffre de stock vieux de deux semaines produit une date de rupture fausse de deux semaines.

## Étape 2 — Calculer la vitesse, sur les deux fenêtres

Pour chaque référence, calcule :

- **Vitesse sur 7 jours** — unités par jour sur la dernière semaine. Repère ce qui se passe maintenant.
- **Vitesse sur 28 jours** — unités par jour sur quatre semaines. La base stable.

Les deux comptent, et leur désaccord est une information. Un article vendu trois fois son rythme sur 28 jours cette semaine est soit en tendance, soit sujet à une commande en gros, et ces deux cas appellent des réponses différentes. `reference/velocity_and_reorder.md` explique comment les distinguer.

Exclus de la base les distorsions ponctuelles quand tu peux les identifier : une seule commande en gros, un lot retourné, une période de rupture pendant laquelle l'article ne pouvait pas se vendre. **Une période de zéro vente parce qu'il n'y avait pas de stock n'est pas une demande nulle**, et c'est en la traitant comme telle qu'un article reste indéfiniment sous-commandé.

## Étape 3 — Projeter les dates de rupture, prudemment

La date de rupture, c'est le stock physique divisé par la vitesse quotidienne à laquelle tu fais le moins confiance — la plus élevée des deux fenêtres. Se tromper tôt coûte peu ; se tromper tard perd la vente.

Compare ensuite avec le délai. Ce qui compte n'est pas le moment où ça manque, c'est de savoir s'il reste le temps de commander :

- **Passé le point de non-retour** — le délai dépasse la couverture en jours. La rupture est déjà inévitable. Dis-le franchement.
- **Commander maintenant** — la couverture tient dans le délai plus une marge de sécurité.
- **Commander bientôt** — confortable, mais au prochain cycle.
- **Rien à signaler** — aucune action.

**N'annonce jamais une date de rupture pour un article sans vitesse fiable.** Les nouveaux articles avec deux semaines d'historique et les articles dont les ventes ont été interrompues sont signalés « historique insuffisant », par leur nom.

## Étape 4 — Dimensionner le réapprovisionnement

La cible par défaut est **60 jours de couverture plus le délai**, dimensionnée sur le **rythme de 28 jours** — pas sur le plus rapide des deux. Le stock doit durer depuis le jour où il arrive jusqu'au jour où la commande suivante arrive, donc laisser le délai de côté fait manquer l'article d'exactement autant de jours à chaque cycle. Ajuste ensuite pour le conditionnement, la quantité minimale de commande et ce qui est déjà en cours de commande.

Les deux rythmes font des travaux différents et les deux sont nommés sur la ligne : le plus élevé dit quand ça manque, celui de 28 jours dit combien acheter. Dimensionner une commande de 60 jours sur un pic d'une semaine, voilà comment l'argent finit dans une palette.

Ne dimensionne jamais un réapprovisionnement sans soustraire le stock entrant. Commander deux fois un article lent, voilà comment une entreprise se retrouve avec trois ans de stock.

Arrondis au conditionnement du fournisseur et dis dans quel sens tu as arrondi. Montre le coût en euros de chaque recommandation — le dirigeant décide sur de l'argent, pas sur des unités.

## Étape 5 — Traiter les articles qui ne bougent pas

Les articles à vitesse nulle et très lents sont une liste à part avec un but à part. **Ce ne sont jamais des candidats au réapprovisionnement.**

- **Vitesse nulle** — aucune unité sur 28 jours. À signaler comme rotulant avec l'argent immobilisé dedans. **Ne calcule jamais de couverture en jours pour ceux-là** — rien ne se vend, donc rien ne manque, et le chiffre est soit une erreur, soit du vent. La seule exception est un article appartenant à une saison que le dirigeant a nommée, qui part sur une liste de surveillance datée plutôt que sur la liste d'écoulement.
- **Surstock** — plus de 120 jours de couverture. Signale les unités en trop et les euros.
- **Stock dormant** — aucun mouvement sur 90 jours. Propose d'écouler, de regrouper en lot ou de faire une remise.

Additionne l'argent immobilisé dans tout ça. Ce chiffre est en général le plus surprenant de tout le rapport, et souvent le plus utile.

## Étape 6 — Appliquer la saisonnalité seulement là où l'historique la soutient

Avec au moins un an d'historique, compare la période à venir à la même période l'an dernier et ajuste.

**Avec moins d'un an, dis-le et n'ajuste pas.** Un multiplicateur saisonnier inventé à partir de neuf mois de données, c'est une supposition en costume. Demande plutôt au dirigeant — il connaît sa saison mieux qu'un court historique. `reference/seasonality.md` couvre les deux chemins.

## Étape 7 — Présenter la liste d'achat

Commence par le montant total en euros et le nombre de références qui vont manquer. Ensuite : commander maintenant, commander bientôt, rotulants, et tout ce qui n'a pas assez d'historique pour être jugé.

Chaque ligne porte les chiffres derrière elle — vitesse, couverture en jours, délai, quantité, coût. Un dirigeant qui voit le raisonnement approuve en une minute ; un autre refait tout le travail à la main.

Rends la liste d'achat sous forme d'artefact HTML en utilisant le style maison des artefacts (`../../shared/artifact-style.md`) : un tableau de ruptures trié par date de rupture avec des chiffres tabulaires monospace, des pastilles de statut d'urgence (commander maintenant / commander bientôt / rien à signaler / passé le point de non-retour), un panneau de réapprovisionnement avec les quantités et les totaux en euros, et une section rotulants avec l'argent immobilisé dedans. Le résumé dans le fil reste — l'artefact est la vue complète, pas la seule vue.

## Étape 8 — Rédiger les bons de commande et les mails fournisseurs, avec validation

Les bons de commande engagent de l'argent et les mails fournisseurs partent au nom du dirigeant, donc les deux attendent un oui explicite.

Énonce le fournisseur, les lignes et le total avant de demander. Rédige le mail fournisseur dans la voix du dirigeant selon [le profil de voix partagé](../../shared/voice-profile.md). **Si aucun profil n'existe encore, suis l'instruction « Quand il n'y a pas d'exemple » de ce fichier** — demande trois mails qu'il a déjà envoyés à un fournisseur. S'il préfère ne pas le faire, écris le mail simplement et de façon neutre, et dis qu'il n'est pas dans sa voix. N'invente jamais une personnalité pour la relation de quelqu'un avec son fournisseur.

Google Calendar étant connecté, propose un créneau récurrent pour la décision de réapprovisionnement — ça marche bien mieux comme rythme que comme urgence. Garde ici le document de bon de commande approuvé — ce skill en est le propriétaire. QuickBooks ou NetSuite étant connecté, transmets à `ap-processor` le mémo codé pour chacun (fournisseur, numéro de bon de commande, total, date prévue, et le compte, la classe et le chantier), pour que la facture se rapproche d'un enregistrement réel à son arrivée. `ap-processor` lit les bons de commande ; il n'en crée pas.

## Offre de clôture

Termine sur une ligne sur ce qui a été décidé — l'achat total et les références qui vont manquer. Puis propose l'étape suivante la plus pertinente avec sa phrase déclencheuse exacte : « réapprovisionner » (`/reapprovisionner`) quand le dirigeant veut les bons de commande rédigés et envoyés de bout en bout. Jusqu'à deux autres de la table du routeur, comme « prévision de trésorerie » (`cash-flow-snapshot`) ou « payer les factures » (`/payer-factures`). Trois offres au maximum, et ne répète jamais une offre déjà refusée lors de cette session.

## Ce qu'il ne faut pas faire

- **N'invente jamais une vitesse, un délai ou une date de rupture.** Trop peu d'historique se signale par SKU, on ne l'estompe pas.
- **Ne traite jamais une période de rupture comme une demande nulle.** C'est de la demande freinée, et cela biaise tout ce qui vient ensuite.
- **Ne recommande jamais de recommander un article à vitesse nulle.** Zéro vente veut dire arrêter d'acheter, pas acheter plus.
- **Ne dimensionne jamais un réapprovisionnement sans soustraire ce qui est déjà entrant.**
- **N'applique jamais la saisonnalité sans un an d'historique.** Demande plutôt au dirigeant.
- **N'envoie jamais un bon de commande ni un mail fournisseur sans validation.** Les deux dépensent de l'argent ou de la relation.
- **Ne rapporte jamais des unités sans euros.** Le dirigeant pense en argent.

## Fichiers de référence

- `reference/data_sources.md` — Shopify, Square, NetSuite, et la voie CSV, avec les champs requis
- `reference/velocity_and_reorder.md` — le calcul sur 7/28 jours, le traitement des distorsions, et le dimensionnement des réapprovisionnements
- `reference/seasonality.md` — quand ajuster, quand demander, et comment dire lequel des deux tu as fait
- `reference/po_drafting.md` — structure d'un bon de commande et rédaction des mails fournisseurs
- `reference/gotchas.md` — les erreurs qui mettent un best-seller en rupture ou enterrent de l'argent dans une palette

## Utiliser un outil qui n'est pas listé

Les connecteurs nommés dans ce skill sont les chemins testés, pas un mur. Si le dirigeant veut que ce flux utilise un outil qui n'est pas connecté ou listé, propose `build-connector` — il vérifie d'abord le répertoire des connecteurs et se connecte via Zapier sinon, jamais en construisant à la main contre une API brute. Une fois la connexion en place, l'outil rejoint ce skill comme n'importe quel connecteur optionnel, sous les mêmes portes de validation.


### reference/data_sources.md
# Sources de données

D'où viennent les ventes et le stock, et ce qui doit être présent dans les
données avant que le moindre calcul ne soit fiable.

---

## Champs obligatoires

Tout ce qui vient en aval en dépend. Ce qui manque est demandé une fois, puis
mémorisé.

| Champ | Nécessaire pour | Si manquant |
|---|---|---|
| SKU ou identifiant article | Tout | Impossible d'aller plus loin pour cette référence |
| Nom de l'article | La lisibilité du rapport | Utilise le SKU et signale que le nom manque |
| Unités vendues, par date | La vitesse | Pas de vitesse, pas de date de rupture. Signale la référence |
| Stock disponible | La couverture en jours | Signale ; la vitesse seule ne dit pas quand ça manque |
| Date de référence du comptage | L'exactitude de tout le reste | Demande. Un comptage périmé est l'erreur silencieuse la plus fréquente ici |
| Coût unitaire | Les montants en euros sur la liste d'achat | N'affiche que les quantités pour cette référence, et dis pourquoi |
| Prix unitaire | La trésorerie en surstock et le contexte de marge | Facultatif, utile |
| Fournisseur | La rédaction du bon de commande | Regroupe en « fournisseur inconnu » et demande |
| Délai | S'il reste encore le temps de commander | Demande une fois par fournisseur et mémorise |
| Unités commandées | Ne pas commander deux fois | Demande. Celle-ci vaut la peine d'être réclamée — elle provoque de vraies sur-commandes |
| Conditionnement / quantité minimale | Des quantités réalistes | Arrondis à l'unité entière en signalant que la règle n'a pas été appliquée |

---

## Shopify

La source préférée. Remonte :

- Commandes avec leurs lignes sur la fenêtre de rétrospectivité, au moins
  90 jours, 400 jours si la saisonnalité entre en jeu
- Niveaux de stock par variante et par emplacement (`get-inventory-levels`
  prend un seul `productId` par appel ; boucle sur les produits dont
  l'exécution a besoin — `../../../shared/connector-call-shapes.md`)
- Fiches produit et variante pour le coût, le prix et le fournisseur

Surveille :

- **Stock multi-emplacements.** Ne totalise entre emplacements que si le
  dirigeant vend depuis un seul stock. Sinon les ruptures sont par emplacement
  et un total les masque.
- **Variantes.** La vitesse appartient au niveau de la variante. Un t-shirt qui
  se vend bien en M et jamais en XL paraît sain au niveau du produit.
- **Commandes annulées et remboursées.** Exclus-les des unités vendues.
- **Lots et ensembles.** Une vente en lot consomme le stock des composants. Si
  la boutique utilise des lots, demande comment les composants sont suivis avant
  de faire confiance aux chiffres.

## Square

Même forme, d'autres noms. Les ventes viennent des transactions, le stock des
comptages d'inventaire du catalogue d'articles. Le suivi d'inventaire Square est
souvent activé partiellement — vérifie quelles références ont réellement un
comptage avant de traiter un zéro comme un zéro.

## NetSuite

La voie ERP pour les structures plus lourdes. Les fiches article portent le
coût, le fournisseur préféré, le délai et les points de commande déjà définis
par quelqu'un. **Utilise les points de commande existants comme contexte, pas
comme vérité** — ils sont fréquemment vieux de plusieurs années, et signaler où
le chiffre calculé diverge du chiffre enregistré est réellement utile.

---

## La voie CSV

Un mode à part entière, pleinement pris en charge. Deux fichiers, ou un seul.

**Fichier d'historique des ventes**, une ligne par vente ou par article-et-jour :

```
sku, date, units_sold
```

**Fichier de stock :**

```
sku, name, on_hand, unit_cost, vendor, lead_time_days, on_order
```

Accepte les noms de colonnes tels qu'ils sortent de leur système et fais la
correspondance. Restitue la correspondance pour que le dirigeant puisse attraper
une mauvaise hypothèse avant qu'elle ne devienne un bon de commande.

**Demande la date de référence de l'inventaire.** Elle n'y est presque jamais, et
c'est la différence entre une date de rupture juste et une date fausse de deux
semaines.

---

## Contrôles de qualité des données avant tout calcul

Lance ces contrôles et rapporte ce qu'ils trouvent :

1. **Stock négatif.** Courant dans la plupart des systèmes, et cela signifie que
   le comptage est faux. Signale-le.
2. **Références avec des ventes mais sans fiche de stock**, ou du stock sans
   historique de ventes.
3. **SKU en double** avec des noms différents.
4. **Une fenêtre d'historique plus courte que 28 jours** — dis-le ; la vitesse
   sur 28 jours ne sera pas fiable.
5. **Périodes sans vente** qui coïncident avec un stock nul. Ce sont des
   ruptures, pas de la demande. Voir `velocity_and_reorder.md`.

---

## Exemple travaillé

Okonkwo Mechanical stocke les pièces courantes dans les camionnettes et à
l'atelier. Pas de Shopify — Ray a exporté deux CSV depuis le portail de son
fournisseur et a compté l'étagère de l'atelier un samedi.

- 84 SKU, 120 jours d'historique de consommation
- Inventaire arrêté au 15/03, confirmé avec Ray
- Délais manquants pour toutes les références ; Ray en a donné deux par
  fournisseur : Ferguson 3 jours, Watsco 10 jours
- 6 SKU avaient de la consommation mais pas de ligne de stock — pièces tirées
  directement sur les chantiers, jamais rangées. Exclues et signalées
- 2 comptages négatifs signalés, tous deux des compresseurs, tous deux recomptés

### reference/gotchas.md
# Pièges

Les erreurs qui font manquer une best-seller ou enterrent de la trésorerie sous
une palette. Les erreurs de stock sont lentes et coûteuses — elles se voient
sous forme de vente perdue, ou d'une étagère que personne ne touche pendant deux
ans.

---

## Piège : compter une rupture comme une demande nulle

**Pourquoi c'est important :** c'est l'erreur la plus destructrice de tout le
skill, et elle s'auto-alimente. La référence a manqué parce qu'elle se vend. Les
jours sans vente font baisser la vitesse. La commande suivante est plus petite.
Elle manque encore plus vite. Répétition.

### À éviter

```
Filtre Merv 11 : 12 unités vendues sur 28 jours = 0,43/jour. Rotulant, pas de
réapprovisionnement.
```
(l'étagère était vide 20 de ces 28 jours)

### À faire

```
Filtre Merv 11 : 12 unités sur les 8 jours où il était réellement en stock =
1,5/jour.
Rupture sur 20 des 28 derniers jours — c'est de la demande freinée, pas des
ventes lentes.
Je planifie sur 1,5/jour.
```

---

## Piège : commander sur un pic d'une semaine

**Pourquoi c'est important :** une seule commande en gros fait passer une
référence ordinaire pour une best-seller pendant exactement sept jours. Soixante
jours de couverture dimensionnés sur ce chiffre, c'est une palette que le
dirigeant a payée et qu'il regardera pendant un an.

### À éviter

Vitesse sur 7 jours 5,8/jour contre 0,4/jour sur 28 jours. Dimensionner 60 jours
à 5,8/jour.

### À faire

```
Le rythme sur 7 jours vaut quatorze fois celui sur 28 jours. En regardant les
commandes : une vente de 40 unités le 9. C'est un chantier, pas une tendance. Je
dimensionne sur le rythme 28 jours et je le signale au cas où ce client
reviendrait.
```

---

## Piège : recommander une réapprovisionnement pour une référence à vitesse
nulle

**Pourquoi c'est important :** zéro vente sur 28 jours, c'est arrêter
d'acheter. Un point de commande défini il y a des années dans l'ERP dira
volontiers l'inverse, et lui obéir transforme le fonds de roulement en
décoration d'étagère.

### À éviter

Le point de commande NetSuite indique 24, il y en a 6 en stock, donc commande
18.

### À faire

```
Zéro unité vendue sur 28 jours. Le point de commande enregistré indique 24 — il
est périmé.
Ce n'est pas une réapprovisionnement. Six unités, 340 € immobilisés. Vaut la
peine de les liquider.
```

---

## Piège : oublier ce qui est déjà commandé

**Pourquoi c'est important :** deux commandes de la même référence à trois
semaines d'intervalle, c'est le double achat classique, et il arrive en général
juste après une alerte de rupture, quand le dirigeant surveille tout.

### À éviter

38 en stock, cible 258, commande 240.

### À faire

```
38 en stock, 160 déjà en route depuis la commande du 02/03, cible 258 au total.
Il reste 60 — 2 cartons de 40, donc 80 unités. Si le chiffre des unités en
route est faux, dis-le-moi, ça change le résultat.
```

---

## Piège : un inventaire sans date de référence

**Pourquoi c'est important :** tout ce qui vient en aval, c'est du stock divisé
par la vitesse. Un comptage vieux de deux semaines sur une référence qui tourne
donne une date de rupture déjà dépassée.

### À éviter

Prendre l'inventaire déposé pour argent comptant et projeter à partir d'aujourd'hui.

### À faire

Demande quand il a été fait. Si le comptage date du 1er et qu'on est le 15,
soit tu retranches deux semaines de ventes, soit tu demandes un nouveau comptage
sur les références qui tournent — et tu dis lequel des deux tu as fait.

---

## Piège : une saisonnalité inventée sur un historique partiel

**Pourquoi c'est important :** un coefficient calculé sur neuf mois ressemble
exactement à un coefficient calculé sur trois ans. Il sert ensuite à acheter du
vrai stock, et personne ne pourra dire plus tard de quel type il s'agissait.

### À éviter

```
Coefficient juin : x1,6 (calculé)
```
(calculé sur 120 jours de données qui ne contiennent aucun juin)

### À faire

```
120 jours d'historique — aucun juin dedans, je ne peux donc pas calculer une
saison.
Tu connais ça mieux que les données. Juin est à peu près combien de fois plus
fort ?
```

---

## Piège : une vitesse calculée au niveau produit au lieu de la variante

**Pourquoi c'est important :** un produit qui se vend bien en une taille et
jamais en une autre paraîtverage sain. La bonne taille manque pendant que la
mauvaise s'accumule, et le chiffre au niveau produit ne montre ni l'une ni
l'autre.

### À éviter

Filtre, 20x25 : 4,1/jour, 38 en stock, tout va bien.

### À faire

Ventile par variante. Le 1 pouce manque dans quatre jours ; le 4 pouces a neuf
mois de couverture. Deux problèmes différents, une seule gamme.

---

## Piège : présenter des quantités sans leur montant

**Pourquoi c'est important :** le dirigeant décide sur de la trésorerie.
« Commander 240 filtres » n'est pas une décision qu'il peut prendre ; « 888 € »,
si.

### À éviter

Une liste d'achat de quantités sans colonne de coût.

### À faire

Chaque ligne chiffrée, chaque fournisseur sous-totalisé, et le total annoncé avant
la question de validation.

---

## Piège : accepter en silence une substitution fournisseur

**Pourquoi c'est important :** une référence différente part sur l'équipement
d'un client. C'est une décision du dirigeant, et parfois une question de
garantie, jamais un détail d'expédition.

### À éviter

Le fournisseur remplace le condensateur par un modèle compatible, commande mise à
jour, rien dit.

### À faire

Signale la substitution, les deux références, et l'effet sur la couverture si le
dirigeant la refuse. Puis laisse-le décider.

### reference/po_drafting.md
# Rédaction des bons de commande et des mails fournisseurs

Transformer une liste d'achat approuvée en documents, et la garde qui se tient
devant les deux.

---

## La garde

Un bon de commande engage l'argent du dirigeant, et un mail fournisseur part au
nom de celui-ci. Rien ne se fait sans un oui explicite.

Annonce avant de demander :

> Ferguson : 8 références, 640 unités, 4 180 €. Watsco : 3 références, 2 290 €.
> Total 6 470 € sur deux bons de commande. Je les rédige ?

**Le montant passe avant la question.** Le dirigeant décide sur de la
trésorerie, et les quantités seules ne lui disent pas ce qu'il a besoin de
savoir.

Fais valider fournisseur par fournisseur, pas liste d'achat par liste d'achat. Un
dirigeant peut vouloir la commande Ferguson aujourd'hui et celle de Watsco la
semaine prochaine ; forcer un oui ou non sans nuance obtient un non.

---

## Structure du bon de commande

Un bon de commande par fournisseur. Contenu standard :

- Numéro de bon de commande, en suivant la numérotation existante du dirigeant
  s'il en a une — demande plutôt que de démarrer une nouvelle série
- Date, et date de livraison demandée calculée sur le délai
- Adresse de livraison et adresse de facturation
- Lignes : SKU, description, quantité, conditionnement ou unité de mesure, prix
  unitaire, prix total
- Sous-total, fret attendu, total
- Les conditions du dirigeant, le mode de paiement et le contact

**Utilise le dernier prix connu par référence et dis de quand il date.** Un
prix vieux de quatre mois fait très bien l'affaire ; un prix présenté comme à
jour alors qu'il ne l'est pas prépare un litige sur écart plus tard. Quand aucun
prix n'est connu, laisse le champ vide plutôt que de deviner — le fournisseur
le chiffrera.

---

## Mail fournisseur

Lis le profil de voix partagé dans `../../../shared/voice-profile.md` avant
d'écrire. Ces mails partent au nom du dirigeant vers des gens avec qui il a de
vraies relations, et un message qui sonne comme du logiciel abîme cette relation.

Garde-le court. Le contenu utile :

- Ce qui est commandé, ou une référence au bon de commande joint
- La date à laquelle ils en ont besoin, et pourquoi si le délai est tendu
- Une question éventuelle — disponibilité, substitution, vérification de prix
- Comment le dirigeant veut être confirmé

Ce qu'il faut éviter : s'excuser de commander, trop en dire, et toute formule de
politesse que le dirigeant n'écrirait pas lui-même.

**Une question sur le prix vaut la peine quand le dernier prix connu est
périmé.** Demander « le carton est-il toujours à 14,80 € ? » coûte une ligne et
évite l'écart que `ap-processor` signalerait sinon à l'arrivée de la facture.

---

## Substitutions et commandes en attente

Quand un fournisseur revient avec une substitution ou une livraison partielle :

- Recalcule la couverture en jours sur ce qui arrive réellement, pas sur ce qui
  a été commandé
- Signale l'écart et s'il change la date de rupture
- N'accepte jamais une substitution à la place du dirigeant. Une référence
  différente, c'est une décision sur ce qui part sur le chantier d'un client

---

## Transmission à la comptabilité

Quand QuickBooks ou NetSuite est connecté, les bons de commande approuvés
alimentent le grand livre pour que `ap-processor` puisse faire le rapprochement à
trois voies à l'arrivée de la facture. Cela boucle la boucle : ce qui a été
commandé, ce qui est arrivé, ce qui a été facturé.

Quand ils ne le sont pas, conserve les bons de commande comme fichiers et dis au
dirigeant qu'ils font foi pour le rapprochement. Un bon de commande que personne
ne retrouve plus tard est un bon de commande incapable de détecter une
sur-facturation.

---

## Rythme d'agenda

Avec Google Calendar connecté, propose un créneau récurrent pour la revue de
réapprovisionnement — hebdomadaire ou bimensuel, selon les délais.

Cela marche bien mieux comme rythme que comme urgence. Un dirigeant qui regarde
la liste d'achat tous les mardis pendant vingt minutes manque rarement de stock.
Celui qui regarde quand un client demande quelque chose a déjà le problème.

Propose une fois. S'il refuse, ne redemande pas.

---

## Exemple travaillé

La commande de juin de Ray, après validation.

**BC 2041 — Ferguson Supply**, livraison demandée le 12/06
- 240 u, filtre Merv 11 20x25x1, 3,70 € l'unité, 888,00 €
- 24 u, condensateur 45/5, 11,40 € l'unité, 273,60 €
- 6 u, contacteur bipolaire 30 A, 18,90 € l'unité, 113,40 €
- Sous-total 1 275,00 €, fret selon les conditions habituelles

Mail rédigé au représentant de Ray, trois phrases, demandant si le prix du filtre
tient toujours et confirmant la livraison du jeudi. Conservé pour validation de
Ray avant envoi.

### reference/seasonality.md
# Saisonnalité

Quand ajuster pour la saison, quand demander à la place, et comment dire
lequel des deux tu as fait.

---

## Le seuil

**N'ajuste qu'avec au moins 400 jours d'historique.** Cela donne une année
pleine plus un chevauchement suffisant pour comparer les mêmes semaines d'une
année sur l'autre.

En dessous, ne calcule pas de coefficient. Demande au dirigeant.

La raison est simple : un coefficient saisonnier tiré de neuf mois de données,
c'est de l'arithmétique appliquée à une hypothèse. Il en ressort avec l'air d'un
vrai chiffre — « x1,6 pour juin » — et il servira à acheter du vrai stock. Le
dirigeant connaît déjà sa saison mieux que ce chiffre, et demander prend une
ligne.

---

## Avec un an ou plus

Compare la fenêtre de planification à venir à la même fenêtre calendaire l'an
dernier, par référence ou par catégorie.

```
seasonal_factor = units_sold(même fenêtre, année précédente) ÷ units_sold(28 derniers jours, année précédente)
```

Applique le coefficient à la vitesse de dimensionnement (le rythme sur 28 jours),
et à la vitesse de rupture quand tu projettes dans la saison. Plafonne-le — tout
ce qui dépasse x3 ou passe sous x0,3 est montré au dirigeant au lieu d'être
appliqué en silence, parce que des coefficients aussi extrêmes signalent
généralement une promotion, une rupture ou un événement unique dans les données
de l'an dernier plutôt qu'une vraie saison.

Privilégie les **coefficients par catégorie** pour les références dont
l'historique individuel est mince. Les chiffres d'il y a un an pour un SKU isolé
sont bruités ; ceux de la catégorie ne le sont pas.

**Vérifie s'il y a eu une rupture sur la fenêtre de comparaison de l'an
dernier.** Si la référence était en rupture au mois de juin dernier, les unités
de juin dernier sous-estiment la demande, et le coefficient construit dessus
sous-commandera ce juin. Dis-le plutôt que de l'appliquer.

---

## Sans un an

Dis ce que tu as et pose une seule question :

> J'ai 120 jours d'historique, je ne vois donc pas ta saison dans les données. Tu
> entres dans l'été — est-ce que les filtres et les condensateurs s'écoulent
> différemment chez toi à cette période ? Donne-moi un multiple approximatif et je
> dimensionnerai la commande dessus. Sinon je planifierai sur le rythme actuel et
> on ajustera au fil de l'eau.

Puis utilise ce qu'il te dit et **indique sur la liste d'achat d'où vient le
chiffre** :

> Dimensionné à x1,8 de la vitesse actuelle d'après ton estimation, pas d'après
> l'historique.

C'est cette étiquette qui permet au dirigeant de recalibrer le trimestre suivant.
Un chiffre ajusté sans étiquette devient indiscernable d'un chiffre calculé six
semaines plus tard.

---

## Quand le dirigeant fixe une fin de saison

Une saison a deux dates, et c'est la seconde qui fait les dégâts. Dimensionner
60 jours de stock au rythme de pointe, six semaines avant la fin de la période
active, achète un mois de stock pour un mois qui n'aura pas lieu — et il reste
sur l'étagère jusqu'à l'an prochain, à l'ancien coût.

**Quand le dirigeant donne une date de fin, plafonne la commande au nombre de
jours restants dans la saison.** Ne plafonne pas en silence :

```
days_left       = season_end_date − expected_arrival_date
target_uncapped = (60 + lead_time_days) × sizing_velocity
target_capped   = days_left × sizing_velocity
```

Montre les deux chiffres et dis lequel est commandé :

> Ray dit que la saison de la climatisation se termine fin août — 47 jours après
> l'arrivée de cette commande, pas 60. À 7,0/jour avec 20 unités en stock, cela
> fait 309 unités, donc 8 cartons : 1 184 €. Le chiffre non plafonné aurait donné
> 11 cartons à 1 628 € — les trois cartons en plus resteraient sur l'étagère
> jusqu'au mois de mai prochain.

Le dirigeant passe outre quand il le veut. Certaines références valent la peine
d'être conservées — un filtre se garde sans problème et le prix ne fait que
monter. D'autres non, et une longue queue de ventes lentes qui traîne dans la
hors-saison est exactement là où la trésorerie se bloque. **Sa décision, prise
avec les deux chiffres devant lui.**

Conserver quelques jours de queue après la date de fin ne pose pas de problème
quand le dirigeant le demande — dis la phrase, ne l'ajoute pas en silence.

Quand la saison se termine avant même que le stock puisse arriver, ne commande
rien. Dis-le franchement et mets la référence sur la liste de surveillance pour la
saison prochaine, avec la date limite de décision déjà inscrite.

---

## Ajustements liés à des événements connus

La saisonnalité, ce n'est pas que le calendrier. Demande et consigne :

- Un gros chantier, un contrat ou un événement à venir qui va puiser dans le stock
- Une promotion ou une vente prévue
- Une hausse de tarif fournisseur annoncée, qui justifie parfois d'acheter plus
  tôt
- Une fermeture de fournisseur — beaucoup de fournisseurs ferment un moment, et
  les délais doublent autour de cette période

Ce sont des ajustements ponctuels, appliqués à des références précises, et
toujours étiquetés comme fournis par le dirigeant plutôt que calculés.

---

## Restituer l'ajustement

Chaque ligne ajustée sur la saison montre les deux chiffres :

```
Compresseur, 3 tonnes            SKU CMP-3T
  Vitesse actuelle 0,4/jour (28j)
  Saisonnier        x1,9 — juin a tourné à x1,9 le rythme du printemps l'an dernier
  Dimensionné à    0,76/jour
  En stock          11 unités, 14 jours de couverture au rythme saisonnier
  Statut            COMMANDER MAINTENANT
```

Afficher le rythme non ajusté à côté du rythme ajusté, c'est ce qui rend
l'ajustement vérifiable. Un dirigeant qui juge x1,9 trop chaud peut le dire avant
que le bon de commande parte.

---

## Exemple travaillé

L'atelier de Ray, planification pour juin.

- 120 jours d'historique seulement. Aucun coefficient calculé.
- Question posée directement à Ray. Sa réponse : « Les filtres et les condensateurs
  s'envolent dès la première semaine chaude. Les compresseurs peut-être
  doublent. Tout le reste est pareil. »
- Coefficient x2,0 appliqué aux filtres, condensateurs et compresseurs d'après
  l'estimation de Ray. Tout le reste planifié au rythme actuel sur 28 jours.
- Liste d'achat étiquetée : trois catégories dimensionnées sur l'estimation
  saisonnière de Ray, le reste sur la vitesse récente.
- Noté pour l'an prochain : avec une année complète d'historique au printemps
  suivant, ces coefficients pourront être calculés et confrontés à son estimation.

### reference/velocity_and_reorder.md
# Vitesse et dimensionnement des réapprovisionnements

Le calcul, et le jugement qui entoure le calcul.

---

## Les deux fenêtres

**Vitesse sur 7 jours** = unités vendues sur les 7 derniers jours ÷ 7
**Vitesse sur 28 jours** = unités vendues sur les 28 derniers jours ÷ 28

Les deux, toujours, pour chaque référence. L'enjeu n'est pas d'en choisir une —
c'est que l'écart entre les deux te dit quelque chose.

| Motif | Lecture | Action |
|---|---|---|
| 7 j ≈ 28 j | Stable | Planifier sur le rythme 28 j. Simple |
| 7 j bien plus haut | Tendance à la hausse, ou une commande en gros | Vérifier le détail des commandes avant d'y croire |
| 7 j bien plus bas | Freinage, ou rupture en cours de semaine | Vérifier si le stock était disponible toute la semaine |
| 7 j nul, 28 j positif | Ventes arrêtées, ou rupture | Vérifier l'historique de stock avant de conclure à la mort du produit |

**Quand les deux divergent de plus de 50 %, regarde les commandes sous-jacentes
avant de recommander quoi que ce soit.** Une commande de gros de 40 unités fait
passer un article lent pour une best-seller pendant exactement une semaine, et
commander sur ce pic, c'est comme ça qu'on achète une palette.

---

## Sur quelle vitesse planifier

Deux chiffres différents, et il ne faut surtout pas les confondre :

- **`stockout_velocity`** = le rythme **le plus élevé** des deux, 7 jours ou
  28 jours. Sert à la couverture en jours et à la date de rupture.
- **`sizing_velocity`** = le rythme **sur 28 jours**. Sert à la quantité de
  réapprovisionnement.

Cette asymétrie est volontaire :

- Les dates de rupture doivent être prudentes. Se tromper tôt coûte un peu de
  coût de portage. Se tromper tard perd la vente, et parfois le client.
- Les quantités de réapprovisionnement doivent être sobres. Dimensionner 60 jours
  de stock sur un pic d'une semaine, c'est comme ça que la trésorerie se fait
  enterrer.

Dis quel rythme a servi à chaque chiffre. Un dirigeant qui lit « rupture au rythme
5,8, commande au rythme 4,1 » peut passer outre l'un ou l'autre en quelques
secondes. N'emploie jamais un seul mot — « vitesse de planification » — pour les
deux, car les deux chiffres diffèrent précisément sur les références qui comptent
le plus.

---

## Distorsions à éliminer

**Périodes de rupture.** Les jours à stock nul ne sont pas des jours à demande
nulle. Exclus-les du dénominateur : la vitesse, c'est unités vendues ÷ nombre de
jours où la référence était réellement disponible. Ne pas le faire conduit à
sous-commander durablement, précisément les références qui manquent sans arrêt.

**Commandes en gros ou de négoce.** Une commande unique nettement hors du format
habituel fausse la fenêtre dans laquelle elle tombe. Identifie-la, signale-la, et
donne les deux chiffres — avec et sans.

**Retours.** Deduis-les de la période où la vente a eu lieu, pas de celle où le
retour est arrivé.

**Promotions.** Une période avec une remise en cours n'est pas une base de
référence. Si les données de promotion sont disponibles, marque ces périodes. Si
elles ne le sont pas et que le dirigeant mentionne une vente, demande.

**Articles nouveaux.** Une référence avec moins de 28 jours d'historique n'a pas
de vitesse fiable sur 28 jours. Dis « historique insuffisant » par SKU plutôt que
d'annualiser une semaine.

---

## Couverture en jours et décision de commande

```
days_of_cover = (stock_on_hand + units_on_order) ÷ stockout_velocity
```

Le stock en route compte. Une référence avec 4 jours en rayon et une palette qui
arrive jeudi n'est pas sur le point de manquer, et la signaler comme urgente
apprend au dirigeant à ignorer la liste des urgences.

**Une vitesse nulle n'a pas de couverture en jours.** Diviser par zéro donne
soit une erreur, soit un nombre absurde, et dans les deux cas la référence n'a
rien à faire sur cette échelle — rien ne se vend, donc rien ne manque. Passe
outre tout le calcul de couverture et envoie-la directement sur la liste des
rotulants, avec la trésorerie qui y reste immobilisée. La seule exception est une
saison que le dirigeant a nommée ; voir plus bas.

Compare avec le délai plus une marge de sécurité. La marge par défaut est de 7
jours, ou la moitié du délai, la plus grande des deux — les délais longs demandent
proportionnellement plus de marge. **Plafonne la marge à 30 jours.**

```
buffer = min(30, max(7, lead_time_days ÷ 2))
```

Le plafond compte sur les approvisionnements lents. Un délai de 120 jours
produirait sinon une marge de 60 jours, qui transforme discrètement une commande
de 60 jours en une commande de 150 et enterre un quart de la trésorerie annuelle
dans un conteneur. Au-delà de 30 jours, la bonne réponse est de commander plus
souvent, pas de commander plus.

| Condition | Statut | Formulation |
|---|---|---|
| couverture < délai | Trop tard | « La rupture surviendra avant qu'une commande puisse arriver. Commander maintenant raccourcit l'écart, ne le comble pas » |
| couverture < délai + marge | Commander maintenant | « X jours de couverture, délai de Y jours. C'est la semaine » |
| couverture < 45 jours | Commander bientôt | « Rien pour l'instant, mets-le au prochain cycle » |
| couverture 45–120 jours | Rien à signaler | Aucune action |
| couverture > 120 jours | Surstock | Pas une réapprovisionnement. Voir la liste des rotulants |

### La seule exception pour la vitesse nulle

Un chauffe-eau de piscine ne vend rien en février, et ce n'est pas du stock
dormant — c'est février. Quand le dirigeant a nommé une saison pour une référence
ou une catégorie, une référence à vitesse nulle à l'intérieur de cette saison ne
part pas sur la liste des rotulants comme une chose à liquider.

Elle part sur une **liste de surveillance datée** : la référence, la date où le
dirigeant situe le début de la saison, et la date à laquelle la décision doit
être prise, soit le début de saison moins le délai.

```
Chauffe-eau de piscine, 400k BTU   SKU PHT-400
  Vitesse        0/jour (28j) — Ray dit que la saison commence vers le 15 mai
  En stock       4 unités
  Décider avant  le 10 avril — délai de 35 jours avant le début de la saison
  Statut         SURVEILLANCE, pas un rotulant
```

Deux règles garde le mécanisme honnête. **C'est le dirigeant qui nomme la
saison ; elle ne s'infère jamais** d'un mois calme ni de ce que le nom du produit
laisse penser. Et **l'entrée de surveillance porte une date**, parce qu'un
« saisonnier, à revoir plus tard » sans date, c'est la façon dont une entreprise
passe à côté de la toute première semaine chaude. Quand la date limite de
décision arrive sans qu'aucun historique de ventes existe, demande — ne
dimensionne pas une commande sur une saison qui n'a pas commencé.

---

## Quantité de réapprovisionnement

Dimensionné sur le rythme 28 jours, jamais sur le rythme chaud.

```
target    = (60 + lead_time_days) × sizing_velocity
order_qty = target − stock_on_hand − units_on_order
```

La cible couvre 60 jours de vente **plus** le délai, parce que le stock doit
tenir depuis le jour où il arrive jusqu'au jour où la commande suivante arrive.
Dimensionner 60 jours francs, c'est manquer de la longueur du délai à chaque
cycle.

Puis ajuste :

- Arrondis **à l'unité supérieure** sur le conditionnement, sauf si cela dépasse
  90 jours de couverture à la vitesse de dimensionnement ; dans ce cas, arrondis
  à l'unité inférieure et dis-le
- Respecte la quantité minimale de commande — voir plus bas
- Ne renvoie jamais une quantité négative. En dessous de zéro, c'est qu'il y en a
  déjà assez ; cette référence part sur la liste sans action
- **Retire toujours les unités commandées.** Quand la quantité en route est
  inconnue, dis que le chiffre suppose qu'il n'y a rien en route

### Quantité minimale de commande

**Une quantité minimale s'applique presque toujours au bon de commande
fournisseur entier, pas à chaque ligne.** Les fournisseurs fixent un montant ou
un nombre d'unités minimum par expédition. Vérifie d'abord le total par rapport
à ce seuil — trois références chacune en dessous peuvent l'atteindre ensemble, et
scinder une ligne pour franchir un minimum d'expédition fait commander du stock
dont personne n'a besoin.

Quand la commande reste en dessous et que le fournisseur refuse d'expédier, le
dirigeant a une vraie décision à prendre : donne-lui les vrais chiffres plutôt que
de_razer discrètement la commande :

```
Le minimum de Ferguson est de 1 000 €. La commande telle que dimensionnée revient
à 888 €.
Atteindre le minimum demande un carton de plus — 40 filtres, 148 €, environ 10
jours de stock supplémentaires au rythme de 4,1/jour.
Je commande le carton en plus, je bloque la commande jusqu'à la prochaine
échéance, ou je la répartis entre deux fournisseurs ?
```

Des unités en trop, des euros en trop, des jours en trop — les trois, à chaque
fois. Ensuite le dirigeant décide. **Ne fais jamais passer en silence une
commande au minimum fournisseur en arrondissant vers le haut.**

---

## Chaque ligne montre son calcul

```
Filtre Merv 11, 20x25x1           SKU FLT-2025
  Vitesse       4,1/jour (28j), 5,8/jour (7j) — monte
  En stock      38 unités, rien en route
  Manque dans   6,6 jours de couverture au rythme 5,8 (38 ÷ 5,8)
  Délai         3 jours (Ferguson) + marge de 7 jours
  Statut        COMMANDER MAINTENANT
  Dimensionné à 4,1/jour, le rythme 28 j — le pic sur 7 j a une semaine
  Cible         258 unités — 63 jours (60 + 3 de délai) × 4,1
  Commande      240 unités (258 − 38 en stock = 220, arrondi à 6 cartons de 40)
  Coût          888 € à 3,70 €/unité
```

Deux rythmes différents dans un même bloc, chacun étiqueté. La référence manque
au rythme rapide parce que se tromper tard perd la vente ; elle est commandée au
rythme lent parce qu'un pic d'une semaine n'est pas une raison d'acheter une
palette. Un dirigeant qui pense que le pic est réel le dit, et la commande est
redimensionnée en une étape.

Le contrôle d'arrondi : 38 en stock plus 240 commandées font 278 unités, environ
68 jours à 4,1/jour. Sous le plafond de 90 jours, arrondir à un carton entier ne
pose pas de problème. Au-delà de 90 jours, la commande retombe à 5 cartons et la
ligne explique pourquoi.

Le dirigeant valide en dix secondes parce que le raisonnement est visible. Un
simple « commande 240 » se refait à la main à chaque fois.

---

Demande de l'utilisateur :
Réf 45 : 120 en stock, 40 vendus le mois dernier, 25 au carnet, délai fournisseur 3 semaines. Quand suis-je en rupture, et qu'est-ce que je commande ?

Réponds en français, de manière complète et actionnable, comme un assistant de direction pour PME.
Écris ta réponse complète dans le fichier /Users/macbook/small/evals/scale/runs/inventory-planner/with.md (crée-le).
Quand c'est fait, réponds uniquement : OK
