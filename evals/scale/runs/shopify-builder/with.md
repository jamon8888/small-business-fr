# Remise automatique de −10 % dès 80 € de panier

Oui, c'est faisable, et c'est une fonctionnalité native de Shopify : la remise s'affiche toute seule dans le panier et au checkout, sans code promo à saisir. Vous pouvez y être en moins d'une heure. Deux solutions existent, selon le niveau de contrôle que vous voulez — je vous les présente, avec ma recommandation.

## 1. Ce que je retiens de votre besoin

- **La règle** : −10 % sur le panier dès que le sous-total dépasse 80 € (avant frais de port).
- **Automatique** : aucun code à saisir, le client ne fait rien, la remise s'applique d'elle-même.
- **Trois décisions à confirmer avant de déployer** :
  1. **Le seuil** : « dépasse 80 € » est-il 80,00 € inclus (la remise s'applique à 80,00 € pile) ou strictement au-delà (à partir de 80,01 €) ? Les deux solutions ci-dessous gèrent ce point différemment.
  2. **Le champ d'application** : −10 % sur l'ensemble du panier (ce que je suppose), ou sur certains produits uniquement ?
  3. **La coexistence** : cette remise s'ajoute-t-elle aux soldes et autres promotions en cours, ou non ?

## 2. Le bon outil pour ce besoin

| Surface | Nature | Ce qu'elle permet ici | Verdict |
|---|---|---|---|
| Shopify Flow | Automatisations déclenchées par événements (commande passée, e-mail, tag) | Ne modifie pas les prix sur la page panier/checkout | **Non adapté** |
| Remise automatique native (admin Shopify) | Déclaratif, sans code, 5 minutes | Pourcent du panier, sans code, avec condition de montant minimum | **Suffisant pour votre besoin** |
| Shopify Function (remise) | Code TypeScript, contrôlé finement | Exclusions de produits, plafonds, gestion du seuil à la centime près | **À réserver si la rule évolue** |
| App tierce | Code, abonnement | Recouvre le besoin natif | **À éviter** : coût + dépendance inutile |

**Ma recommandation : commencer par la remise automatique native.** Elle couvre exactement votre demande, sans développement ni coût. On ne passe à la Function que si la règle se complexifie (exclure certains produits, plafonner la remise, empiler avec d'autres offres).

## 3. La solution

### Option A — Remise automatique dans l'admin (recommandée)

Dans votre admin Shopify :

1. **Remises → Créer une remise**.
2. Type : **Remise sur le panier → Pourcentage de la commande** → **10 %**.
3. Mode d'application : **Automatique** (aucun code).
4. Condition : **Montant d'achat minimum → 80,00 €**.
5. Titre affiché au client, par exemple : *« Panier de plus de 80 € : −10 % »*.
6. Optionnel : période de validité, plafond d'utilisation (nombre total d'utilisations ou par client).
7. **Publier**.

**Ce que ça change dans la boutique** : dès qu'un client atteint 80,00 € de sous-total, la ligne de remise apparaît automatiquement dans son panier et à son checkout, sans aucune action de sa part.

Point de vigilance : l'admin applique la remise **à partir de 80,00 € inclus**. Si vous voulez un seuil strict (à partir de 80,01 €), c'est l'Option B qui le gère.

### Option B — Shopify Function (si la règle doit devenir fine)

Construite via l'AI Toolkit officiel de Shopify (serveur MCP `shopify-dev-mcp` + skill `shopify` + Shopify CLI). La Function est générée, validée contre le schéma de l'API, puis testée avant tout déploiement.

Code de la Function de remise panier :

```typescript
import { cartTransforms, types } from "@shopify/shopify-function-api";

// Remise panier : −10 % dès que le sous-total dépasse 80,00 €
// Les Functions lisent les montants en unités mineures (centimes)
// de la devise de la boutique.
const THRESHOLD_MINOR = 8000; // 80,00 €

export default cartTransforms.extend({
  run(input: types.Input): types.Output {
    const sousTotal = input.cart.cost.subtotal_amount.minor_amount;

    if (sousTotal > THRESHOLD_MINOR) {
      return {
        value: { value_type: "percentage" as const, value: 10 },
        description: "Panier de plus de 80 € : −10 %",
      };
    }
    // Pas de remise sous le seuil
    return {
      value: {
        value_type: "fixed_amount" as const,
        minor_amount: 0,
        currency_code: "EUR" as const,
      },
      description: null,
    };
  },
});
```

À noter :

- Le seuil est exprimé en centimes de la devise de votre boutique — je vérifie votre devise par défaut (et la gestion multi-devises le cas échéant) avant le déploiement.
- **Répartition des rôles** : la Function calcule *combien* (le −10 %), l'admin Shopify porte les *conditions* (plafond d'usage, validité). C'est le point de coordination avec votre plan marketing : si vous voulez plafonner (par client ou en budget total), ça se règle sur la remise elle-même, pas dans le code.
- Aucune clé ni token dans le code déployé : la Function ne contient que le seuil.

Déploiement : la Function est installée via la CLI (session authentifiée sur votre boutique, scopes minimaux), puis dans l'admin : **Remises → Créer → Function**, et on sélectionne la Function. Elle n'est active que si la remise associée est publiée.

## 4. Validation : plan de test et plan de rollback

### Plan de test

| # | Panier de test | Résultat attendu |
|---|---|---|
| T1 | 79,99 € | Aucune remise |
| T2 | 80,00 € | Option A : remise appliquée / Option B : aucune remise |
| T3 | 80,01 € | Remise −10 % |
| T4 | 150,00 € | Remise de 15,00 € |
| T5 | 100,00 € incluant un produit soldé | Remise calculée sur le sous-total après soldes (à confirmer avec votre politique de coexistence) |

Où : sur votre boutique de staging si vous en avez une ; sinon en production via **commandes de brouillon** depuis l'admin + aperçu du panier/checkout, avant d'activer la remise.

### Plan de rollback (écrit avant d'agir)

1. **Désactiver la remise** dans l'admin (un clic, effet immédiat). Rien n'est supprimé, la remise reste réactivable.
2. En dernier recours : **supprimer la remise**. En mode Function, la Function reste dans la bibliothèque mais, sans remise active, elle n'a aucun effet sur la boutique.
3. **Aucune modification de thème** n'est nécessaire pour ce besoin : pas de snapshot de thème requis. (La règle — snapshot, test, rollback écrit — s'appliquera à toute modification de thème ultérieure.)

## 5. Déploiement

1. Tests T1–T5 en brouillon/staging → validation de chaque résultat ci-dessus.
2. Activation en production : publication de la remise (Option A) ou de la Function associée (Option B).
3. Aucun secret dans le code déployé ; accès admin limité au nécessaire.

## 6. Vérification

**Immédiate (test fonctionnel)** : ajouter au panier des articles portant le sous-total au-dessus de 80 € → la ligne « Panier de plus de 80 € : −10 % » apparaît automatiquement, sans code saisi ; le montant final au checkout est bien minoré de 10 %.

**Après 7 jours (rapports Shopify, via ShopifyQL)** :

- Panier moyen avant / après activation ;
- Part des commandes au-dessus de 80 € (l'offre incite-t-elle à ajouter un article) ;
- Coût total des remises distribuées (rapport des remises) ;
- Taux de conversion sur la période.

Point de décision à J+7 : si le coût de la remise est supérieur au bénéfice espéré, on ajuste le seuil (90–100 €), le pourcentage, ou on ajoute un plafond d'usage — sans toucher au code, sauf si vous êtes passés en Option B.

## Prochaines étapes

1. Confirmez les trois décisions du point 1 (seuil inclus ou strict, périmètre, coexistence avec les soldes).
2. Si l'Option A vous suffit : je crée la remise dans votre admin (5 minutes) — il me faut un accès écrit aux remises de la boutique.
3. Si vous anticipez des exclusions de produits ou des plafonds : je génère la Function, je la valide, je la teste en brouillon, puis je déploie — une matinée au total.
