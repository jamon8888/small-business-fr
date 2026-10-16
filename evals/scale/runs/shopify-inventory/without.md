# Diagnostic et plan d'action — Stock Shopify en baisse

## En résumé

Vous avez deux problèmes distincts à traiter, et il ne faut pas les confondre :

1. **3 références sous leur seuil de stock** → c'est un problème de **réapprovisionnement** (il faut commandeter).
2. **1 produit affiché à 2 unités en ligne alors que vous en avez 9 en entrepôt** → c'est un problème de **synchronisation** entre votre entrepôt et la boutique (les 7 unités manquantes ne sont pas visibles par Shopify).

Traiter le n°2 d'abord : s'il est mal réglé, il fausse la lecture de tout le reste, y compris vos 3 références en alerte.

---

## 1. Le désaccord 2 (en ligne) vs 9 (en entrepôt)

C'est le symptôme le plus révélateur. L'entrepôt détient 9 unités, la boutique n'en compte que 2. Les causes les plus fréquentes, dans l'ordre :

### A. L'emplacement « Entrepôt » n'est pas rattaché au canal en ligne
C'est la cause n°1. Dans Shopify, chaque produit puise son stock disponible dans un ou plusieurs **emplacements (locations)**. Si l'entrepôt n'est pas activé pour le canal « Boutique en ligne » (ou si le produit n'est pas assigné à cet emplacement), la boutique ne voit que l'inventaire de l'emplacement qui l'est (souvent le stock de la boutique physique, ici 2 unités).

**À vérifier :**
- *Paramètres > Inventaire* : confirmez que l'emplacement « Entrepôt » est bien listé et actif.
- Sur la fiche du produit concerné : *Inventaire > Emplacements* — vérifiez que l'entrepôt apparaît avec 9 unités et qu'il est rattaché au canal Boutique en ligne.

### B. Désynchronisation / retard de sync
Si vous alimentez Shopify depuis un logiciel de gestion (WMS, tableur, ERP) via l'API ou une app de sync, le flux peut être en panne ou en retard. Les 7 unités ont peut-être été saisis dans l'entrepôt sans remontée.

**À vérifier :**
- Regardez l'horodatage de la dernière mise à jour d'inventaire sur le produit.
- Testez une mise à jour manuelle : changez la quantité de 9 à 10 puis re-sauvegardez, et observez si la boutique passe à 10. Si oui, le canal de sync est la cause ; s'il reste figé, c'est le rattachement d'emplacement (cause A).

### C. Saisie manuelle erronée ou double emplacement
Quelqu'un a pu saisir 2 à la main au lieu de 9, ou le stock est réparti entre deux emplacements (2 à la boutique + 7 ailleurs, non synchronisés).

### Action immédiate (aujourd'hui)
1. Allez sur *Produits > [produit concerné] > Inventaire*.
2. Corrigez la quantité totale affichée pour la boutique en ligne à **9** (ou alignez l'emplacement entrepôt sur 9).
3. Enregistrez. Vérifiez côté client que la fiche produit affiche bien la disponibilité correcte.
4. Notez la cause racine identifiée (A, B ou C) — c'est elle qui conditionne la prévention ci-dessous.

> Point d'attention : si ce produit est très demandé, le risque d'une survente (promettre plus que vous n'avez) est faible ici puisque vous sous-affichez, mais le risque est commercial : vous vendez à 2 unités ce qui devrait en être 9, et vous perdez des ventes. Corrigez dans la journée.

---

## 2. Les 3 références sous le seuil

Un produit « sous le seuil » veut dire que son stock est passé sous le **niveau de stock minimum** défini (votre point de réapprovisionnement). C'est un signal d'achat, pas une urgence absolue — sauf si la rotation est rapide.

### Actions
1. **Priorisez par l'urgence réelle**, pas par l'ordre d'affichage. Pour chacune des 3 références, croisez :
   - la quantité restante,
   - le rythme de vente (ventes / semaine),
   - le délai de réapprovisionnement de votre fournisseur (lead time).
   
   Formule simple d'alerte : si *stock restant < (rythme hebdo × semaines de délai fournisseur) + marge de sécurité*, la commande doit partir **maintenant**.

2. **Créez les bons de commande (purchase orders)** dans *Inventaire > Bons de commande*, en regroupant les 3 références par fournisseur si possible pour négocier un transport / condition.

3. **Vérifiez que le seuil est juste.** Un seuil trop bas déclenche l'alerte trop tard, après que vous ayez déjà stock sec. Pour chaque référence, le seuil doit couvrir : *délai fournisseur (en unités vendues pendant ce délai) + marge de sécurité*. Ajustez le seuil de stock bas de chaque produit (*Produit > Inventaire > Seuil de stock bas*) si besoin.

4. **Évitez le stock sec entre-temps.** Pour une référence critique en attente de réassort :
   - si vous avez d'autres emplacements avec du stock, activez-les pour le canal en ligne ;
   - sinon, envisagez temporairement de mettre le produit en « précommande » / délai d'expédition annoncé, ou de le masquer, plutôt que d'afficher « en stock » puis d'annuler des commandes clients.

---

## 3. Prévention structurelle (à mettre en place cette semaine)

Pour ne plus subir ce genre d'alerte :

1. **Cadrage des emplacements.** Liste claire de vos emplacements (boutique, entrepôt, dépôt) et règle unique : chaque emplacement qui alimente la boutique en ligne est explicitement rattaché au canal en ligne. C'est ce qui évite de refaire le problème « 2 au lieu de 9 ».

2. **Fiabiliser la synchro.** Si un logiciel gère l'entrepôt, vérifiez que la synchro d'inventaire est active, testée régulièrement, et dotée d'une alerte de rupture de sync (ex. « dernière sync il y a plus de 24 h »). Évitez les saisies manuelles d'inventaire à la main sur Shopify si un flux automatique existe — c'est la source classique de divergence.

3. **Seuils de stock bas cohérents.** Passez en revue les seuils des 3 références (et, par extension, de vos références à fort chiffre) pour qu'ils reflètent délai fournisseur + marge de sécurité.

4. **Routine de contrôle.** Un point inventaire récurrent (hebdo, 10 min) :
   - références sous seuil → déclencher le bon de commande ;
   - écarts entre stock comptable (entrepôt) et stock Shopify → investiguer la synchro.

5. **Règle de garde anti-survente.** Si un produit bascule à 0 ou sous le seuil critique, définissez ce qui s'affiche au client (épuisé, précommande, délai) pour protéger l'expérience client et éviter les annulations.

---

## Ordre de passage recommandé

| Priorité | Action | Quand |
|---|---|---|
| 1 | Corriger l'affichage du produit (2 → 9) et identifier la cause racine (rattachement emplacement / synchro / saisie) | Aujourd'hui |
| 2 | Commander les 3 références sous seuil (bons de commande), priorisées par urgence réelle | Aujourd'hui / demain |
| 3 | Ajuster les seuils de stock bas des 3 références | Cette semaine |
| 4 | Fiabiliser la synchro entrepôt → Shopify + cadrage des emplacements | Cette semaine |
| 5 | Mettre en place le point inventaire hebdo | Semaine prochaine |

Le point clé : **ne traitez pas « stock en baisse » comme un seul problème.** C'est un problème commercial (réassortir les 3 références) et un problème de données (réconcilier l'entrepôt et la boutique). Le second, s'il n'est pas corrigé à la racine, va continuer à fausser votre lecture du premier.
