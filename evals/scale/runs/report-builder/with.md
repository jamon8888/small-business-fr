## Tableau de bord mensuel — première mise en place

Bonne nouvelle : c'est votre premier tableau de bord, donc nous le construisons ensemble maintenant — puis je l'enregistre, et le mois prochain vous le lancerez d'un mot, sans que je vous pose la moindre question.

J'ai d'abord vérifié vos rapports enregistrés : il n'y en a aucun pour l'instant. Je crée donc la définition de votre « tableau de bord mensuel » à partir de votre demande, et j'ai déjà rédigé la spec complète :

### Spec du rapport (brouillon)

```
Nom du rapport :  Tableau de bord mensuel
Cadence :         mensuelle, 1er jour ouvré
Période :         mois civil précédent, complet
Comparaison :     mois précédent
Découpage :       aucun (ventilation par client uniquement pour la balance âgée)

Indicateurs :
  Trésorerie 30   =  solde bancaire de clôture + encaissements attendus − décaissements attendus, horizon J+30   [comptabilité]
  Trésorerie 60   =  idem, horizon J+60                                                              [comptabilité]
  Trésorerie 90   =  idem, horizon J+90                                                              [comptabilité]
  Impayés         =  factures clients ouvertes, réparties 0-30 / 31-60 / 61-90 / 90+ jours de retard  [comptabilité]
  TVA             =  TVA collectée sur factures émises − TVA déductible sur achats, du mois             [comptabilité]
  Échéances 30 j  =  factures fournisseurs à régler + déclarations et prélèvements à venir              [comptabilité]

Sources :         à confirmer (voir ci-dessous)
Notes :           Profil à confirmer — il ajoute des indicateurs (tableau ci-dessous).
                  Le chiffre d'affaires fait foi dans la comptabilité ; les autres sources
                  (boutique, Stripe/PayPal, CRM) ne servent qu'aux détails, jamais au revenu.
```

Les deux « à confirmer » sont exactement ce qui détermine le reste du tableau de bord.

### 1 question : quel est votre profil ?

Le socle (trésorerie 30/60/90, impayés par ancienneté, TVA, échéances) est commun à tous les profils. En plus, votre profil ajoute :

| Profil | Indicateurs ajoutés |
|---|---|
| Services | Taux d'occupation, temps non facturé, CA récurrent, renouvellements, devis en cours |
| Négoce / fabrication | DSO, DPO, DIO, marge brute par client, carnet de commandes, taux de service, stock dormant |

→ Répondez en un mot : **services**, **négoces** ou **fabrication**.

### 2e chose : d'où viennent les données ?

Deux voies, toutes deux à part entière :

- **La comptabilité connectée** — QuickBooks, Xero, Zoho Books, MYOB ou NetSuite : dites-moi laquelle, et j'extrais tout en un seul lot parallèle, en quelques secondes.
- **Les fichiers téléversés** — si aucun connecteur n'est prêt, je construis le tableau de bord à partir de vos exports CSV/XLSX, c'est une voie complète et non dégradée. Il me faudra : le compte de résultat du mois, la balance âgée clients, la balance âgée fournisseurs, le solde bancaire, la déclaration de TVA (collectée / déductible) et la liste des factures fournisseurs à venir. Déposez les fichiers dans la conversation, je mappe les colonnes moi-même.

### À quoi ressemblera le tableau de bord, chaque mois

- **Un résumé dans la conversation** : la phrase la plus importante, 3 indicateurs clés avec leur écart, au plus trois constats (nommant le client ou le groupe précis et le montant), et ce qui demande une décision, avec la suite proposée.
- **Un classeur XLSX joint** : onglet synthèse, un onglet par groupe d'indicateurs, et un onglet de données brutes pour que votre comptable puisse vérifier les calculs.

Les règles sur lesquelles vous pouvez compter : aucun chiffre manquant ne sera rempli par un montant plausible — il sera affiché « non disponible » et je vous dirai pourquoi ; et aucune période partielle ne sera comparée à une période complète sans être étiquetée comme telle.

**Pour lancer le premier run, répondez-moi par votre profil et votre source de données.** Dès que la définition est complète, je l'enregistre — et le mois prochain, « lance le tableau de bord » suffira.
