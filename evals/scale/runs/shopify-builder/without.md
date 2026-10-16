# -10 % automatique dès 80 € d'achat : la solution Shopify native (sans code)

Bonne nouvelle : c'est **100 % faisable avec les fonctions natives de Shopify**, sans écrire une ligne de code et sans application tierce. Le mécanisme s'appelle **remise automatique** (*Automatic discount*) avec la condition **montant d'achat minimum**.

## Principe

Une « remise automatique » est appliquée par Shopify tout seule, au moment du passage en caisse, dès que les conditions que vous définissez sont remplies. Le client n'a rien à faire : pas de code promo, pas de bouton. C'est exactement votre besoin.

## Procédure pas à pas (≈ 2 minutes)

1. Connectez-vous à votre **admin Shopify** (votre-boutique.admin.shopify.com).
2. Allez dans **Remises** (*Discounts*) → **Créer une remise**.
3. Dans le sélecteur de type, choisissez **Remise automatique** (et non « Code promo »).
4. Renseignez un nom interne, par exemple `Panier 80€+ → -10 %`.
5. **Type de remise** : choisissez **Pourcentage sur la commande** (remise en % sur le total du panier) et saisissez **10**.
   - C'est cette option qui applique les 10 % à **toute la commande** dès que le seuil est atteint.
   - (Évitez « Pourcentage sur les produits » : il se calculerait produit par produit et n'appliquerait pas la logique globale de panier que vous voulez.)
6. **Conditions** (*Usage limits* / *Conditions*) : cochez **Montant d'achat minimum** et saisissez **80,00** en euros.
   - En dessous de 80 € : aucune remise.
   - À partir de 80 € : -10 % sur l'ensemble du panier.
7. Options conseillées :
   - **Date de fin** : laissez vide si l'offre est permanente.
   - **Limite d'utilisation** : vous pouvez plafonner le nombre d'activations (ex. 500) si vous voulez maîtriser la marge.
8. Cliquez sur **Créer**. C'est actif immédiatement, sur le site **et** en point de vente POS.

## Ce que le client verra concrètement

- Panier à 65 € → aucun changement.
- Panier à 84 € → la remise apparaît dans le récapitulatif de la caisse : « Remise : -8,40 € », et le total passe à 75,60 € (hors taxes/transport).
- L'application est **progressive** : le client voit le total baisser en temps réel dès qu'il franchit les 80 € dans son panier, ce qui encourage à compléter son panier.

## Points de vigilance (à décider avant d'activer)

1. **Base de calcul du seuil** : les 80 € se comptent sur le **sous-total produits, avant taxes et transport**. Un panier à 80 € de marchandises déclenche bien la remise.
2. **Effet « escalier »** : à 79 € pas de remise, à 81 € le client gagne ~8,10 € (≈ 10 %). Le gain perçu saute nettement au seuil — c'est le comportement attendu, mais vérifiez que vos marges le supportent sur vos produits à faible marge.
3. **Cumul avec d'autres remises** : par défaut, un client peut cumuler votre remise automatique avec un code promo ou une remise sur produit. Si ce cumul n'est pas voulu, définissez des **règles d'empilement** (usage limits → « Ne pas combiner ») sur vos codes promo existants.
4. **Test avant mise en ligne** : placez un panier test à 79 € puis à 81 €, ajoutez la commande en mode brouillon ou avec un paiement test, et vérifiez que la ligne « Remise » apparaît bien dans la caisse.
5. **Communication en boutique** : la remise n'apparaît que dans la caisse. Pour maximiser l'impact, affichez une bannière dans le thème (« -10 % dès 80 € d'achat, automatiquement ») — simple texte à ajouter dans les réglages du thème, ou via l'app « Bannière/Barre d'annonce » de l'App Store si vous voulez un bandeau fixe.

## Variantes si le besoin évolue

- **-10 % seulement sur une catégorie** : remplacez le type par « Pourcentage sur les produits » + condition « Appliquer à : [collection] » + montant d'achat minimum 80 €.
- **Progressif** (ex. -10 % dès 80 €, -15 % dès 150 €) : deux remises automatiques distinctes (Shopify n'applique que la plus favorable selon les règles de combinaison — à tester).
- **Freemium/transport offert au lieu de -10 %** : c'est une autre mécanique (livraison gratuite à partir de X €), disponible aussi sans code via **Livraison et expéditions → Règles de livraison**.

En résumé : **Remises → Créer une remise → Remise automatique → Pourcentage sur la commande 10 % → Montant d'achat minimum 80 €** → Créer. Zéro code, zéro app, actif immédiatement.
