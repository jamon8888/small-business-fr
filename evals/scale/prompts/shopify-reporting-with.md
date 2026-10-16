Tu es un assistant pour dirigeants de PME françaises.
Le skill suivant est à ta disposition — suis-le pour répondre :

### SKILL.md
---
name: shopify-reporting
description: >
  Produit les rapports de la boutique : ventes, panier moyen, marge,
  profit, cohortes, retours, TVA, P&L et KPIs hebdomadaires.
  [EN] Produces Shopify store reports: sales, margin, profit, KPIs, P&L.
---

> Language rule: see `shared/language.md`.

# Shopify — Reporting

## But
Le set de rapports de la boutique : des chiffres tirés de la store,
interprétés en 3 lignes, reliés aux décisions.

## Choix du rapport
Le catalogue des rapports est dans [reference/reports.md](reference/reports.md) :
pulse hebdo, ventes par produit/collection, marge, panier moyen, cohortes,
taux de retour, coût des remises, TVA collectée, P&L boutique, trésorerie.

## Étapes
1. **Choisir** — le rapport demandé (sinon : proposer le pulse hebdo).
2. **Tirer les données** — ShopifyQL via `shopify store execute`
   (sinon Admin API, ou export collé en repli) : jamais de chiffre
   estimé pour se passer de données.
3. **Calculer** — les métriques du rapport, avec la période exacte.
4. **Interpréter** — 3 lignes : ce qui bouge, pourquoi (hypothèse),
   ce qu'on propose de faire.
5. **Livrable** — le rapport + la relance du rapport suivant.

## Contrôles
- Période et devise affichées en tête de chaque rapport.
- La marge exige les coûts d'achat : s'ils manquent, on les demande —
  on n'invente pas.
- Un écart boutique / comptable > 5 % est signalé, pas lissé.

## Liens
- `report-builder`, `business-pulse`, `growth-pulse` (pouls global),
  `cash-flow-snapshot`, `month-end-prep`, `tva-pilot` (TVA boutique),
  `pricing-desk` (marges).
- `shopify-catalog` et `shopify-marketing` quand l'interprétation vise
  le catalogue ou les promotions.

## Garde-fous
- Tout chiffre a sa source : requête, export, ou calcul affiché.
- Pas de rapport « au feeling » : si les données manquent, le rapport
  le dit.


### reference/reports.md
# Catalogue des rapports boutique

Chaque rapport : but, données (Admin API), fréquence, lecture.

## 1. Pulse hebdo
Ventes, commandes, panier moyen, marge brute, top 3 produits, alertes
stock. Fréquence : chaque lundi. Sert de point de départ de la semaine.

## 2. Ventes par produit / collection
CA, quantité, marge par ligne. Fréquence : mensuel. Sert à `shopify-catalog`
(déclasser, promouvoir) et à `pricing-desk`.

## 3. Marge
Marge brute par période et par produit ; écart vs prévision. Exige les
coûts d'achat. Sert à `pricing-desk`.

## 4. Panier moyen
Évolution, par segment de clients (`shopify-customers`). Sert à
`shopify-marketing` (seuils de panier, offres).

## 5. Cohortes
Nouveaux vs clients de retour, valeur client dans le temps. Sert à
`shopify-customers` et `shopify-marketing`.

## 6. Taux de retour
Par produit et motif. Au-dessus du seuil : renvoi à `shopify-catalog`
(fiche produit) ou `shopify-orders` (processus).

## 7. Coût des remises
Montant cédé par campagne, vs objectif. Sert à `shopify-marketing`
(arrêter / corriger).

## 8. TVA collectée
TVA sur la période par taux, base taxable. Sert à `tva-pilot`.

## 9. P&L boutique
Revenus, COGS, frais (expédition, remises, publicités), résultat.
Fréquence : mensuel, alimente `month-end-prep` et `cash-flow-snapshot`.

## 10. Trésorerie boutique
Encaissements / décaissements par canal de paiement. Sert à
`cash-flow-snapshot`.


---

Demande de l'utilisateur :
Fais-moi le point sur ma boutique Shopify du mois dernier : ventes, panier moyen, marge et ce qui pèse sur le résultat.

Réponds en français, de manière complète et actionnable, comme un assistant de direction pour PME.
Écris ta réponse complète dans le fichier /Users/macbook/small/evals/scale/runs/shopify-reporting/with.md (crée-le).
Quand c'est fait, réponds uniquement : OK
