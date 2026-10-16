# Réf 45 — analyse de stock et de réapprovisionnement

**Résumé d'abord :** avec 120 unités en stock, 25 déjà en route et un rythme d'environ 1,3 unité/jour, la référence 45 tient **aux alentours de 100 à 110 jours** — la rupture, si le rythme se maintient, tomberait **vers fin janvier / début février 2027**. **Il n'y a rien à commander maintenant** : vous êtes dans la zone « rien à signaler » (couverture entre 45 et 120 jours). Le bon moment pour commander, c'est le **milieu de décembre 2026**, pour une quantité d'environ **108 unités**. Deux conditions importantes : le comptage de 120 doit être récent, et il me faut votre coût unitaire pour chiffrer tout ça en euros.

---

## 1. Ce que je sais, et ce que je dois vérifier

Ce que vous m'avez donné tient dans un seul point d'historique : « 40 vendus le mois dernier ». C'est insuffisant pour une vitesse fiable au sens du planificateur, et je le dis franchement plutôt que de l'estomper :

- **Vitesse sur 28 jours : indisponible en données brutes.** J'estime à **1,33/jour** (40 unités ÷ 30 jours). C'est une estimation sur un seul point mensager, pas une vitesse mesurée jour par jour.
- **Vitesse sur 7 jours : historique insuffisant.** Je ne peux pas la calculer, et je ne vais pas l'inventer. Elle est pourtant ce qui me dirait si la référence accélère ou décélère *maintenant*.
- **Date de référence du comptage : inconnue.** Un comptage de 120 vieux de deux semaines décale ma date de rupture de deux semaines. Quand avez-vous compté ?
- **Coût unitaire, fournisseur, conditionnement : inconnus.** Je ne peux donc pas chiffrer la recommandation en euros. Donnez-moi le coût d'achat de l'unité (et le fournisseur, s'il a un conditionnement cartons) et j'ajoute les montants dans la minute.

Une vérification de plus vaut la peine : les 40 unités du mois dernier formaient-elles un rythme régulier, ou y a-t-il eu **une grosse commande unique** dedans ? Un seul client qui a pris 20 unités un jour fausse tout : la vitesse réelle serait alors plutôt de 0,8/jour et la couverture bien plus longue. De même, si la référence était **en rupture une partie du mois**, 40 est en dessous de la vraie demande.

## 2. Quand êtes-vous en rupture ?

Calcul, prudemment, en comptant le stock en route (les 25 du carnet arrivent, donc elles couvrent) :

```
Vitesse estimée   1,33/jour (40 unités / 30 jours — estimation, 1 seul point)
Couverture        (120 en stock + 25 en route) ÷ 1,33 ≈ 109 jours
                  (si le mois a tourné à 40/28 = 1,43/jour : ≈ 101 jours)
Rupture projetée  fin janvier – début février 2027, si le rythme tient
```

**En clair : vous n'allez pas manquer à court terme.** C'est le point rassurant de la réponse. Le chiffre porte le caveat affiché : une estimation sur un mois de données, pas une vitesse sur 28 jours mesurée. Avec 28 jours de ventes datées, je vous le remets précis à la date près.

## 3. Statut : rien à signaler — pas de commande cette semaine

- Couverture : **≈ 101 à 109 jours**
- Délai fournisseur : 21 jours (3 semaines)
- Marge de sécurité : 10 jours (la moitié du délai, qui est au-dessus du plancher de 7 jours)
- Seuil d'alerte « commander maintenant » : couverture < 31 jours

À 100+ jours de couverture, vous êtes nettement au-dessus du seuil d'alerte de 31 jours, mais sous le seuil de surstock de 120 jours : zone « **rien à signaler** ». Ne commandez rien aujourd'hui — commander maintenant, c'est acheter du stock pour un mois où vous n'êtes pas encore en danger.

## 4. Qu'est-ce que vous commanderez, et quand

**Quand :** quand la couverture descend sous **31 jours** (délai 21 + marge 10). Au rythme actuel, ça tombe **vers le 15 décembre 2026**. Mettez ce créneau en revue récurrente — c'est le moment où la commande de décembre doit partir, pas plus tôt.

**Combien, au moment de commander :** dimensionné sur le rythme 28 jours, pour 60 jours de couverture **plus** le délai (le stock doit tenir jusqu'à la commande suivante) :

```
Cible     (60 + 21) × 1,33/jour ≈ 108 unités
Commande  108 − stock du moment − unités déjà en route au moment
Coût      ≈ 108 × votre coût unitaire — donnez-moi ce coût et j'affiche les euros
```

J'arrondirai au conditionnement du fournisseur au moment où je l'aurai, et je dirai dans quel sens.

## 5. Ce qu'il me faut pour affiner (demandé une fois, puis mémorisé)

1. **La date du comptage** de 120 unités.
2. **28 jours de ventes datées** (un export de votre système suffit) pour remplacer l'estimation par une vraie vitesse 7/28 jours.
3. **Le coût unitaire** — pour que la recommandation parle en euros.
4. **Le fournisseur et le conditionnement** (cartons de combien ? minimum de commande ?).

Rien n'est commandé et aucun fournisseur n'est contacté : ces chiffres préparent la décision, ils ne la prennent pas.

---

## Prochaines étapes possibles

- **« réapprovisionner » (`/reapprovisionner`)** — je rédige les bons de commande et les mails fournisseurs, avec validation avant envoi.
- **« prévision de trésorerie » (`cash-flow-snapshot`)** — voir où va l'argent des prochains achats.
- **« payer les factures » (`/payer-factures`)** — régler le stock qui arrive.
