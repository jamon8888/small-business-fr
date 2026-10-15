Bonjour — votre demande est claire, et le fait d'être en négoce change réellement le dossier : l'inventaire et la valorisation entrent dedans, pas à côté.

Une précision d'abord, parce qu'elle commande tout le reste : dans cette session aucun outil comptable n'est connecté, et votre export Qonto n'est pas encore arrivé dans la conversation. Tant qu'il n'est pas là, je ne peux produire aucun chiffre. Je préfère vous le dire maintenant plutôt que de remplir un dossier avec des montants supposés.

Je ne vous livre pas la clôture en un seul passage. Chaque étape produit un brouillon, vous le validez, puis j'enchaîne. On attaque par le rapprochement, et c'est là que j'ai besoin de vous.

## Le déroulé

**1. Rapprochement, lettrage et cut-off**

Je rapproche le relevé Qonto de votre comptabilité ligne à ligne, et je letraie les virements groupés sur les factures qu'ils règlent. Chaque ligne porte un statut (rapproché / à lettrer / écart de date / non rapproché) et le montant de l'écart quand il y en a un.

Ensuite le cut-off, qui est la partie qui se voit sur le résultat et sur la TVA :
- **FAE** — livraisons d'octobre non encore facturées
- **FNP** — marchandises reçues en octobre, facture fournisseur pas encore parvenue
- **charges à payer** et **produits à recevoir** du mois

Un point de méthode sur vos chiffres : Qonto tient l'argent, votre comptabilité tient les factures. Vos 14 factures fournisseurs et vos 31 lignes de ventes viennent du second. Il me faut les deux côtés, sinon la colonne « écart » n'a rien à comparer. Et vos 31 lignes de ventes ne sont pas forcément 31 factures — une facture à plusieurs lignes apparaît en plusieurs lignes. Pour le cut-off et pour la balance âgée clients, j'ai besoin de la pièce, pas de ses lignes.

**2. Inventaire et valorisation — votre stock**

Feuille de comptage, écart de chaque référence contre le théorique à la date du comptage, valorisation, puis proposition de dépréciation des dormants (à valider avec votre expert-comptable).

Deux choses que je ne choisis pas à votre place :
- **la date de comptage** — elle est obligatoire, et c'est elle qui rend les mouvements postérieurs rapprochables ;
- **la méthode de valorisation** — CMUP ou FIFO, c'est votre politique. Si votre balance est déjà en CMUP, basculer en cours d'exercice n'est pas un détail.

Donnez-moi la méthode que vous appliquez déjà et je calcule dessus.

**3. Prévision de trésorerie sur 60 jours**

- **Encaissements** : vos créances ouvertes au 31 octobre, avec échéance et solde restant dû, décalées par votre délai de règlement réel.
- **Décaissements** : factures fournisseurs échues, commandes en cours livrées à leur date attendue, prélèvements SEPA, paie, TVA, charges fixes.
- **Fourchette haute et basse** calculée sur la variance de vos règlements passés — pas sur un pourcentage posé d'avance.
- **Indicateurs négoce** : DSO, DPO, DIO et le cycle de conversion (DSO + DIO − DPO). Je vous nomme toujours la définition de chaque taux : taux de marque = marge ÷ prix de vente, taux de marge = marge ÷ prix d'achat.

Je lis vos prélèvements SEPA dans Qonto, je ne les invente pas — et c'est ce qui rend cette prévision défendable quand vous la montrerez à votre banque.

Deux points de calendrier à surveiller dans la fenêtre : l'échéance de TVA d'octobre, qui tombe mi-novembre (déclaration CA3, à confirmer avec le calendrier applicable à votre régime), et le mercredi 11 novembre, jour férié, qui décale les échéances tombant ce jour-là.

**4. Dossier de clôture et tableau de bord**

Le classeur daté (compte de résultat, rapprochement, points à traiter, paie si un outil de paie est connecté) et le résumé d'une page à transmettre à votre expert-comptable. Le fichier s'appellera `close-packet-2026-10.xlsx`, avec la page de synthèse en `close-packet-2026-10-summary.pdf`.

Rien n'est écrit dans vos comptes, aucun paiement n'est lancé. Ce que je produis sort en brouillon et en fichier d'import, c'est vous ou votre comptable qui saisissez.

## Ce qu'il me faut pour démarrer

| Pour quoi | Ce que j'attends |
|---|---|
| Rapprochement | L'export Qonto d'octobre (relevé des comptes) **et** l'extraction des factures fournisseurs et clients du mois |
| Cut-off | Vos livraisons d'octobre non facturées, et vos réceptions non facturées |
| Stock | La date de comptage, la feuille de comptage physique, le théorique à cette date, la méthode CMUP ou FIFO, et les mouvements postérieurs au comptage |
| Trésorerie | Le solde bancaire au 31 octobre, les créances clients ouvertes (solde > 0), les factures fournisseurs échues et non échues, les commandes en cours, vos prélèvements SEPA planifiés, le montant et la date de la prochaine paie |
| Tableau de bord | Le coût d'achat sur vos 31 lignes de ventes — sans lui, la marge par produit est « non disponible » et je le dirai ainsi |

## Trois questions avant de commencer

1. **La période.** Votre export couvre-t-il tout octobre, du 1er au 31, ou un mois arrêté en cours de route ? Un mois partiel comparé au mois complet précédent fait toujours peur à tort.
2. **Votre comptabilité.** Quel outil tient vos comptes ? Le rapprochement se fait Qonto ↔ comptabilité ; Qonto seul ne voit pas vos factures.
3. **L'horizon.** Je pars sur 60 jours comme demandé. Je peux ajouter la fenêtre 90 jours si vous voulez la voir — elle sert surtout à repérer les tensions de paie qui n'arriveront pas avant mars.

## Ce que je ne remplirai pas

Si une donnée manque, elle sortira marquée « non disponible » avec sa source nommée, pas à zéro. Un zéro inventé se lit comme une bonne nouvelle alors que c'est un trou dans les données, et c'est ce chiffre-là que votre expert-comptable retrouvera en janvier.

Ce qui manque aujourd'hui, en l'état : l'export Qonto, la date de comptage, la méthode de valorisation, le solde bancaire d'ouverture. Tout le reste est prêt à partir.

**Clôture non démarrée : 0 écriture, 0 € chiffre.** Je vous rends le premier brouillon — le rapprochement — dès que le fichier arrive.