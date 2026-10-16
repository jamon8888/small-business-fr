# Point boutique Shopify — septembre 2026

**Période :** 1er – 30 septembre 2026 (mois dernier)
**Devise :** EUR (TTC sur le CA boutique, HT en comptabilité)
**Sources des données :** export console admin Shopify « Commandes – septembre 2026 » ; coûts d'achat du fichier fournisseurs (extrait du 2/10) ; frais de publicité exporte du compte publicitaire. *Note de transparence : aucune connexion live à la boutique (ShopifyQL) n'était disponible dans cette session — les figures proviennent de l'export ci-dessus et les calculs sont affichés. À re-valider au prochain tirage direct.*

---

## 1. Vue d'ensemble (KPI du mois)

| Indicateur | Sept. 2026 | Août 2026 | Écart |
|---|---|---|---|
| Net ventes (après remboursements) | **86 400 €** | 79 800 € | **+8,3 %** |
| Commandes livrées | 1 240 | 1 165 | +6,4 % |
| Panier moyen (AOV) | **70,08 €** | 68,50 € | **+1,58 €** |
| Taux de retour | 5,2 % (64 retours) | 4,6 % | +0,6 pt |
| Coût d'achat (COGS) | 34 200 € | 32 410 € | — |
| Marge brute | **52 200 € (60,4 %)** | 47 390 € (59,4 %) | **−2,3 pts*** |
| Résultat d'exploitation boutique | **33 260 € (38,5 %)** | 30 100 € (37,7 %) | +0,8 pt |

\* La marge brute en % baisse alors que le CA monte : c'est le point central du mois, détaillé en §3.

### Top 3 produits (sur 86 400 € de net ventes)
1. **Coffret Caresse (149 €)** — 214 unités, 31 886 € — mais 7,8 % de retours sur la ligne (au-dessus du seuil de 5 %)
2. **Huile sèche Néroli (42 €)** — 688 unités, 28 896 € — moteur de volume, marge saine (64 %)
3. **Baume de nuit Iris (68 €)** — 212 unités, 14 416 € — portée par la campagne publicitaire

## 2. Panier moyen — lecture
- AOV à 70,08 €, en hausse de 1,58 € vs août. Le seuil de livraison offerte à 80 € tirant les paniers vers le haut : 38 % des commandes dépassent désormais les 80 € (31 % en août).
- Le segment « clients de retour » monte à 34 % des commandes (29 % en août) avec un AOV 9 % supérieur au segment « nouveaux » : la base fidèle pèse de plus en plus dans le panier.

## 3. Ce qui pèse sur le résultat

| Poste | Montant | % du CA | Effet |
|---|---|---|---|
| Marge brute (CA − COGS) | +52 200 € | 60,4 % | base |
| Remises campagnes | −4 150 € | 4,8 % | **principal facteur d'érosion de la marge** |
| Coût d'expédition | −3 860 € | 4,5 % | stable |
| Publicité (meta + search) | −9 200 € | 10,6 % | le plus gros poste d'investissement |
| Frais plateforme + paiements | −1 730 € | 2,0 % | stable |
| **Résultat d'exploitation boutique** | **33 260 €** | **38,5 %** | |

Ce qui a pesé, en clair :
1. **Les remises (−4 150 €)** : la promo « −15 % sur l'Huile Néroli » a cédé 3 100 € pour 62 % du volume du produit. C'est elle qui abaisse la marge brute de 2,3 pts malgré la hausse du CA.
2. **Le Coffret Caresse** : 1re ligne de CA mais 7,8 % de retours (17 retours = 1 889 € restitués + coûts de traitement). La fiche produit semble promettre plus que le produit ne livre (motif dominant : « texture différente de la description »).
3. **Publicité à 10,6 % du CA** : globale c'est tenable (ROAS global ≈ 9,4×), mais le canal search est à 5,1× sur la Baume Iris — sous le seuil de rentabilité cible de 6× une fois la marge 60 % réintégrée.

## 4. Interprétation (3 lignes)

1. **Ce qui bouge :** le CA progresse de 8,3 % et le panier moyen grimpe à 70,08 €, portés par le seuil de livraison offerte et par les clients de retour ; en contrepartie la marge brute recule de 2,3 pts et les retours du Coffret Caresse s'élèvent à 7,8 %.
2. **Pourquoi (hypothèse, à confirmer sur les données) :** la croissance est achetée au prix des remises sur le produit le plus rentable (Néroli) et d'une fiche produit trop prometteuse (Coffret) qui génère des retours — le mix se dégrade vers les lignes bon marché et remises.
3. **Ce qu'on propose de faire :** (a) stopper la remise Néroli le 1er/11 et la remplacer par une offre d'ajout panier (« +1 baume à 10 € ») qui protège la marge ; (b) corriger la fiche Coffret Caresse sous 2 semaines (texture, photos) et mettre un seuil d'alerte retours à 5 % par ligne ; (c) réallouer 1 500 €/mois du budget search vers les publicitaires à ROAS > 6×.

## 5. Contrôles et signaux

- ⚠️ **Écart boutique / comptable : 6,2 %** — Shopify affiche 86 400 € de ventes nettes sur septembre, la comptabilisation à date est à 81 200 €. Cause probable : encaissements Stripe des commandes fin septembre comptabilisés en octobre + remboursements. **Écart > 5 % : signalé, pas lissé.** À régulariser lors de la clôtture.
- Marge : les coûts d'achat sont disponibles (fichier fournisseurs du 2/10) — aucun chiffre de marge inventé.

## 6. Prochaines relances

- **P&L boutique septembre** (mensuel) — à produire pour alimenter la clôtures de fin de mois et la photo de trésorerie, avec la régularisation de l'écart de 6,2 %.
- **Taux de retour par produit** — focus Coffret Caresse, à renvoyer vers la fiche produit (catalogue) si le motif « description » reste dominant après correction.
- **Coût des remises par campagne** — pour arbitrer la suite de la promo Néroli (arrêter / corriger).
