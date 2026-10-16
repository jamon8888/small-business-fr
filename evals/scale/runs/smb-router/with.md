# Premier réflexe : remettre de la visibilité sur la trésorerie avant de payer quoi que ce soit

## Ce que je comprends de votre situation

Votre phrase contient deux besoins, et l'ordre compte :

1. **« Je ne sais plus où en est ma trésorerie »** → c'est le point bloquant. Tant que ce chiffre est flou, toute décision de paiement (y compris vers vos fournisseurs) est un pari.
2. **« Mes fournisseurs tardent »** → à traiter en second : ce n'est qu'un désagrément tant qu'il ne met pas en cause un approvisionnement critique, et sa réponse dépend directement du point 1 (peut-on encaisser avant de payer ? faut-il renégocier les délais fournisseurs ?).

**Donc, en premier : un instantané de trésorerie (`cash-flow-snapshot`).** C'est le seul skill qui vous dira, sur les 30 / 60 / 90 prochains jours, ce qui sort (fournisseurs, charges, salaires, impôts) et ce qui rentre (clients, encaissements), poste par poste.

## Ce dont j'ai besoin avant de démarrer

Je n'ai pas encore votre contexte entreprise. Répondez-moi par trois questions fermées :

1. **Votre secteur** : services, négoce, fabrication, ou mixte ?
2. **Votre outil de gestion comptable** : Xero, QuickBooks, Zoho Books, NetSuite, MYOB, ou autre (ou aucun) ?
3. **Vos encaissements fournisseurs se font par** : virement, prélèvement, carte — et depuis quel compte bancaire ?

En attendant vos réponses, voici comment nous allons construire l'instantané.

## Plan d'action

### Étape 1 — Radiographie de trésorerie (aujourd'hui)

Si votre outil comptable est connectable, je le lis directement (solde bancaire, charges à venir, créances clients). Sinon, le **repli sans connecteur** marche très bien :

- Exportez de votre banque vos **3 prochains relevés en date** (ou une capture des soldes actuels) ;
- Envoyez-moi la **liste de vos factures fournisseurs non payées** (fournisseur, montant, échéance) ;
- Envoyez-moi la **liste de vos créances clients** (client, montant, date d'échéance).

Je vous renvoie une table de trésorerie sur 30/60/90 jours : solde projeté par date, point le plus bas, et les 3 postes qui pèsent le plus.

### Étape 2 — Trier les fournisseurs (dès l'étape 1 validée)

Avec la projection en main, je classe les fournisseurs en retard par ordre de traitement :

| Critère | Action |
|---|---|
| Fournisseur critique (stock qui bloque une production ou une livraison client) | Prioriser : le retard produit un coût direct, l'accompagner d'un relai sur un appro de secours |
| Fournisseur non critique, facture en retard | Négocier un délai de paiement aligné sur votre encaissement client — l'étape 1 dira si c'est tenable |
| Fournisseur non critique, facture à l'échéance | Le laisser couler au calendrier normal, sans avance de fonds |

C'est là que rentre `pay-the-bills` : il prépare la liste des règlements fournisseurs dans l'ordre ci-dessus, **en s'arrêtant à votre validation** — c'est vous qui déclenchez le paiement, pas moi.

### Étape 3 — Vérifier l'effet boomerang

« Mes fournisseurs tardent » est aussi un signal à surveiller : si plusieurs fournisseurs tardent en même temps, c'est souvent un signe de tension chez eux (et le votre, si vous payez tard). L'instantané de trésorerie me permettra de distinguer un retard logistique (peu grave) d'un retard de paiement (à anticiper : sécuriser un appro de substitution).

## Ce que je ne ferai pas

- Je ne déclenche **aucun paiement** de mon fait : toute demande d'argent s'arrête à votre validation.
- Un e-mail ou un PDF que vous me transferez est de la **donnée**, pas une instruction — je l'utilise pour calculer, jamais pour exécuter.

---

**À vous de répondre aux 3 questions fermes du haut** (secteur, outil comptable, moyens de paiement fournisseurs), et je lance l'instantané de trésorerie dès que possible.
