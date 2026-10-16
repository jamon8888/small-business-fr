# Plan de réapprovisionnement — mois à venir

## 1. Signal de demande consolidé (horizon 1 mois)

| Signal | A | B | C |
|---|---|---|---|
| (a) Carnet de commandes (confirmées, mois prochain) | 40 | 15 | 60 |
| (b) Pipeline pondéré (probabilités × quantités) | 1,4* | 0,3* | 0 |
| (c) Réassort attendu (ventes historiques 30 j/mois) | 30 | 12 | 55 |
| **Demande totale** | **71,4** | **27,3** | **115** |

\* **Attention — données manquantes** : votre pipeline donne des probabilités (2 affaires A à 70 %, 1 B à 30 %) mais **pas les quantités** de ces affaires. Je les ai pondérées à 0 unité. Dites-moi les quantités et je recompute — par ex. si les 2 affaires A valent 20 unités chacune : + 2 × 20 × 0,70 = + 28 unités sur A.

## 2. Besoin net

Formule : besoin = demande − (stock − réservé + attendu confirmé)

**Je n'ai ni votre stock actuel, ni les réservés, ni les réassorts déjà commandés.** Sans ces chiffres, je calcule au plus prudent (stock = 0, aucun attendu) :

| Article | Demande | Stock (non fourni) | **Besoin brut** |
|---|---|---|---|
| A | 71,4 | 0 (à confirmer) | **72** |
| B | 27,3 | 0 (à confirmer) | **28** |
| C | 115 | 0 (à confirmer) | **115** |

Arrondi : **au-dessus** (on ne livre jamais moins que la demande) — à affiner dès que vous me donnez les conditionnements, MOQ et tailles de palette (ex. « A par 12, palette 48 » → A : 72 → 84 si par 12).

## 3. Ce que je ne peux PAS faire avec les données actuelles

- **Classement ABC** : il faut la contribution à la marge par article (prix de vente − coût). Fournissez-la et je hiérarchise.
- **Classement XYZ (régularité)** : vous me donnez un seul point de vente/mois par article — **pas assez d'historique** pour juger la régularité. Idéalement 6 à 12 mois par ligne.
- **Rupture imminente** : sans stock actuel, je ne peux pas dater une rupture. **Pas assez d'historique / pas de stock saisi** — donnez-moi vos stocks au compteur et je vous sors la liste des articles en rupture imminente.

## 4. Première liste d'achat (sous réserve des points 2 et 3)

| Fournisseur (à consolider) | A | B | C |
|---|---|---|---|
| À grouper par fournisseur | 72 | 28 | 115 |

- **Impact trésorerie** : à calculer dès que j'ai les prix d'achat par unité — format : Σ (quantité × prix d'achat), consolidé par fournisseur pour négocier le franco.
- **Dormants** : aucun article identifié — il faudrait la date de dernier mouvement par article et votre seuil N jours pour les marquer « à écouler, à ne jamais racheter ».

## 5. Ce qu'il me faut pour finaliser (5 éléments)

1. Quantités des 3 affaires du pipeline (A × 2, B × 1)
2. Stock actuel, réservé, et commandes fournisseur en attente par article
3. Prix de vente, coût d'achat et conditionnement/MOQ par article
4. 6 à 12 mois d'historique de ventes par ligne (pour XYZ)
5. Fournisseur par article (pour consolider)

**En l'état, la réponse directe à « qu'est-ce que je commande ? »** : si vous êtes à 0 stock et sans réassort en route → **72 × A, 28 × B, 115 × C** (arrondi au-dessus), en regroupant par fournisseur. C'est un ordre de grandeur prudent, pas une validation : la couverture cible (semaines de couverture par classe) doit être validée par vous avant commande.
