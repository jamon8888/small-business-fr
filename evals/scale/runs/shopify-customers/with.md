# Segmentation de la base clients — offre privée « clients fidèles »

Objectif : isoler les clients fidèles de votre boutique (4 800 clients) pour constituer un segment prêt à recevoir une offre privée. Voici le plan complet, segment par segment, avec les tags à valider en une passe avant application.

> Note de méthode : les effectifs ci-dessous sont **estimations** calées sur les benchmarks e-commerce typiques (taux de réachat 12 mois ≈ 25–30 %, core fidèle ≈ 10–15 % de la base pour ~40 % du CA). L'étape 1 ci-dessous sert à les remplacer par vos chiffres réels — la structure des segments, elle, ne change pas.

---

## Étape 1 — Lire la base (diagnostic à 30 jours de votre admin Shopify)

Dans *Shopify → Clients → Analytique* (ou export interne à la boutique, sans envoi hors boutique), relever :

- **Volume** : 4 800 clients au total.
- **Répartition par nombre d'achats** (fenêtre 12 mois glissants) — estimation indicative :

| Nombre d'achats sur 12 mois | Clients (est.) | Part |
|---|---|---|
| 1 seul achat | 3 460 | 72 % |
| 2 achats | 800 | 17 % |
| 3 achats | 390 | 8 % |
| 4 achats ou plus | 150 | 3 % |

- **Taux de réachat** : ≈ 28 % (≈ 1 340 clients avec 2+ achats sur 12 mois) — cohérent avec le benchmark Shopify de ~28 %.
- **Panier moyen** : à relever (je pars d'une hypothèse de 62 € pour calibrer le critère M — remplacez par votre valeur réelle).
- **Ancienneté** : proportion de clients avec un 1er achat depuis moins de 90 jours.

Si le taux de réachat réel est très différent de ~28 % (par ex. < 15 %), les segments « fidèle » se rétrécissent : on resserre les critères plutôt qu'on ne les relâche, pour que l'offre privée reste exclusive.

---

## Étape 2 — La segmentation RFM et les tags

**Échelles de scoring** (fenêtre de référence : 12 mois glissants, calculés par la boutique) :

- **R — Récence** : jours depuis le dernier achat. R5 ≤ 60 j · R3 61–120 j · R1 121–240 j · R0 > 240 j.
- **F — Fréquence** : nombre de commandes sur 12 mois. F5 ≥ 4 · F4 = 3 · F3 = 2 · F1 = 1.
- **M — Montant** : total dépensé sur 12 mois. M5 = quartile supérieur · M3 ≥ moyenne · M1 < moyenne.

**Carte des segments** (couvre 100 % de la base ; les effectifs sont des estimations à confirmer à l'étape 1) :

| # | Segment | Critères écrits (12 mois) | Tag | Taille (est.) |
|---|---|---|---|---|
| 1 | **Champions** | R ≤ 60 j **et** F ≥ 4 **et** M en quartile supérieur | `fidèle-champion` | ~350 (7 %) |
| 2 | **Fidèles réguliers** | R ≤ 120 j **et** F = 3–4 **et** M ≥ moyenne | `fidèle-regulier` | ~450 (9 %) |
| 3 | **Fidèles potentiels** | R ≤ 120 j **et** F = 2 **et** M ≥ moyenne | `fidèle-potentiel` | ~700 (15 %) |
| 4 | **Fidèles en risque** | F ≥ 3 **et** R entre 121 et 240 j | `fidèle-en-risque` | ~350 (7 %) |
| 5 | **Nouveaux clients** | 1er achat depuis moins de 90 j | `nouveau-client` | ~900 (19 %) |
| 6 | **Dormants** | R > 240 j **et** F ≤ 1 | `dormant` | ~2 050 (43 %) |

Lecture : les segments 1+2 forment le **cœur fidèle** (~800 clients, ≈ 17 % de la base). C'est le public de votre offre privée : ils achètent souvent, récemment, et dépensent au-dessus de la moyenne — typiquement 40–45 % de votre chiffre d'affaires.

**Le tag de ciblage de l'offre privée** :

- `offre-privee` = clients tags `fidèle-champion` **ou** `fidèle-regulier` (~800 clients). C'est ce tag que `shopify-marketing` va consommer pour l'envoi de l'offre.

Décisions de périmètre à valider avec vous :

1. **Inclure les « fidèles en risque » (~350) dans l'offre privée ?** Ma recommandation : **non** — ils sont en phase de désengagement ; l'offrir une offre privée sans relance adaptée, c'est gaspiller l'exclusivité. Mieux vaut les passer au skill `reactivate` avec une relance dédiée.
2. **Inclure les « fidèles potentiels » (~700) ?** Recommandation : **non** pour la première vague. Ils sont la vague 2 (on leur donne un goût de l'offre privée en les invitant à franchir le cap de 3 achats) — cela protège le sentiment d'exclusivité.
3. **Un client peut avoir plusieurs tags** (ex. `fidèle-champion` + `offre-privee`). C'est voulu : les tags des segments 1–4 sont descriptifs, `offre-privee` est le tag d'action.

---

## Étape 3 — Plan de tags à valider (une passe)

Validez ce plan en une fois, puis on applique :

| Tag | Rôle | Action |
|---|---|---|
| `fidèle-champion` | descriptif | appliquer |
| `fidèle-regulier` | descriptif | appliquer |
| `fidèle-potentiel` | descriptif | appliquer |
| `fidèle-en-risque` | descriptif | appliquer |
| `nouveau-client` | descriptif | appliquer |
| `dormant` | descriptif | appliquer |
| `offre-privee` | **action** (ciblage) | appliquer aux seuls champion + régulier |

Règle de non-régression : si un client sort du périmètre (ex. n'achète plus), on lui **retire le tag** à la prochaine ré-exécution — aucun client n'est jamais supprimé de la base.

---

## Étape 4 — Application et contrôle

1. **Application** : dans *Shopify → Clients*, appliquer les tags segment par segment (sélection par filtre + tag en lot), ou via l'API clients de votre boutique si vous avez une app de segmentation — tout se passe dans la boutique.
2. **Relire l'échantillon** : tirer 20–30 clients au hasard dans `offre-privee` et vérifier à l'œil : dernier achat récent ? 3+ commandes sur 12 mois ? Panier au-dessus de la moyenne ? Si un échantillon sort du périmètre, on corrige le critère avant le lancement.
3. **Contrôle croisé** : comparer la taille mesurée de `offre-privee` à l'estimation (~800). Écart > 30 % → on recalcule les seuils (le segment est « flou » et on le reformule, on ne le lance pas tel quel).

---

## Étape 5 — Livrable : carte des segments prêts pour `shopify-marketing`

| Tag à cibler | Public | Effectif (est.) | Usage proposé |
|---|---|---|---|
| `offre-privee` | Champions + fidèles réguliers | ~800 | **Offre privée** : accès anticipé (48 h avant tout le monde), -15 % ou livraison offerte, produit/édition réservée |
| `fidèle-potentiel` | 2 achats, récents, valeur ≥ moyenne | ~700 | Vague 2 : invitation conditionnée au 3e achat |
| `fidèle-en-risque` | 3+ achats, absent de 4 à 8 mois | ~350 | Passer au skill `reactivate` (relance dédiée, pas l'offre privée) |
| `nouveau-client` | 1er achat < 90 j | ~900 | Parcours de bienvenue (skill `shopify-marketing`) |
| `dormant` | absent de 8+ mois | ~2 050 | Campagne de réactivation différée (skill `reactivate`) |

**Ce skill ne fait aucun envoi** : il a préparé les segments. C'est `shopify-marketing` qui consommera `offre-privee` pour la campagne.

---

## Conformité (RGPD)

- Tous les calculs RFM, tags et ciblages se font **dans votre boutique Shopify** : aucune donnée client n'est exportée vers un outil tiers. Si vous souhaitez un jour un export (Excel, outil d'e-mailing externe), c'est une validation explicite de votre part, au préalable.
- Les tags sont des métadonnées de ciblage attachées au client dans votre boutique ; ils ne créent aucune donnée nouvelle hors boutique.

## Prochaines étapes

1. Confirmez les trois décisions de périmètre (en risque / potentiels / vague 2) — ou dites « validé tel quel ».
2. Je lance l'étape 1 sur vos chiffres réels pour remplacer les estimations.
3. Une fois le plan de tags validé : application en une passe, contrôle de l'échantillon, puis remise des segments à `shopify-marketing` pour construire l'offre privée.
