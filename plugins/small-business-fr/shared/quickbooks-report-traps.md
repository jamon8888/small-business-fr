# Pièges des rapports QuickBooks

**Spécifique à un connecteur.** Ce fichier documente le comportement réel d'un
connecteur ; c'est une liste de pièges, pas une préférence pour ou contre
QuickBooks (`connector-neutrality.md`). Pour MYOB, NetSuite et Xero, la même
discipline « lis les lignes » s'applique presque certainement, mais rien ici
n'a été vérifié contre eux.

Sept façons pour un outil QuickBooks de te donner un chiffre faux avec
assurance. Chaque skill qui appelle un outil QuickBooks — rapports, balance
âgée, paie — doit appliquer toutes les règles ci-dessous.

Le fil conducteur : **la réponse de confort d'un outil QuickBooks — un objet
`summary`, un indicateur de préparation — n'est pas fiable quand les lignes
disent le contraire. Totalise les lignes toi-même, et crois l'appel qui a
renvoyé des lignes.**

---

## Piège 1 — un appel contraint présente son propre sous-ensemble comme l'intégralité du grand livre

Les rapports de balance âgée doivent être contraints, sinon ils débordent la
limite de sortie. Mais le bloc `summary` d'un appel contraint est calculé sur
**uniquement les lignes qui sont revenues**, et il n'est pas signalé comme
partiel.

Mesuré sur le même grand livre, le même jour :

| Appel | `summary.totalReceivables` | Clients | Seau 91+ |
|---|---|---|---|
| `top_n = 10` | 25 907,38 € | 10 | 0 € |
| sans `top_n` | 37 054,65 € | 20 | 467,00 € |

L'appel sur les 10 premiers sous-évalue les créances de 30 % et déclare le
seau de 91 jours vide. La seule véritable créance douteuse du livre — le client
que le skill existe pour faire remonter — disparaît en silence. Rien dans la
réponse n'indique que le résultat a été tronqué.

**La règle.** Un appel contraint répond à « qui sont les plus gros
débiteurs », jamais à « quel est le total ». Quand un skill a besoin à la fois
d'une liste classée et d'un total vrai, il fait deux appels :

1. Un appel contraint pour les noms et le classement.
2. Un appel séparé pour le total — la ligne créances clients ou dettes
   fournisseurs du bilan, qui est toujours l'intégralité du livre et toujours
   courte.

Ne cite jamais `summary.totalReceivables` ni `summary.totalPayables` issus d'un
appel contraint. Si seul l'appel contraint est disponible, étiquette le chiffre
« top N uniquement » dans la sortie et dis-le à voix haute.

## Piège 2 — la synthèse du compte de résultat déclare les charges à zéro

La réponse du compte de résultat porte une synthèse de premier niveau qui
contredit ses propres lignes. Par exemple :

- Lignes : `Expenses` total `984 590,63 €`
- Synthèse : `totalExpenses: 0`, `summaryBreakdown.expenses: 0`
- Synthèse : `grossProfit` égal au produit total, `grossProfitMargin: 100`

`netIncome` est juste, parce qu'il est calculé à partir du montant réel des
charges. L'erreur reste donc invisible tant qu'un skill ne lit pas directement
`totalExpenses`, `grossProfit` ou `grossProfitMargin` — et tout skill qui le
fait va rapporter une entreprise sans aucun coût et avec une marge parfaite.

**La règle.** Prends le produit, les charges et le coût des ventes dans les
lignes du rapport, ou dans `monthlyBreakdown`, qui est lui aussi juste. Traite
`totalExpenses`, `grossProfit` et `grossProfitMargin` dans la synthèse comme
non renseignés. Seuls `netIncome` et `totalIncome` peuvent être lus depuis la
synthèse.

**Vérification de cohérence avant de publier le moindre chiffre de marge :**
une marge brute de exactement 100 %, ou une entreprise affichant zéro charge
alors qu'elle a du chiffre d'affaires réel, signifie que ce piège s'est
déclenché. Recalcule depuis les lignes au lieu de le rapporter.

## Piège 3 — les ventes par client comptabilisent deux fois les sociétés mères

La synthèse des ventes par client renvoie deux lignes pour tout client qui a
des sous-clients en dessous : une ligne de synthèse pour le parent, et une ligne
de total distincte qui porte le même chiffre. La liste des meilleurs clients du
rapport lui-même contient les deux.

Lu naïvement, un client apparaît deux fois dans le classement et toute mesure de
concentration qui en dérive est surévaluée. Cela importe surtout là où la
concentration est rapportée à un conseil d'administration.

**La règle.** Écarte les lignes dont le type de métadonnées les marque comme
total avant de classer, de sommer ou de calculer la concentration. Garde la ligne
de synthèse du parent ; c'est la vraie. Les ventes par **produit** ne sont pas
concernées — il n'y a pas de structure parent/enfant.

---

## Piège 4 — les ventes par produit ignorent les dates que tu as demandées

`qbo_accounting_get_sales_by_product_summary` accepte `startDate` et `endDate`
puis les jette. Il renvoie toujours l'exercice en cours, et il le dit
discrètement : la charge utile porte `"period": "This Year"` alors que la
demande portait sur un trimestre.

Même appel, deux plages différentes :

| Plage demandée | Renvoyé |
|---|---|
| 2026-04-01 → 2026-06-30 | 36 587,65 €, 22 unités, `period: "This Year"` |
| 2026-01-01 → 2026-01-31 | 36 587,65 €, 22 unités, `period: "This Year"` |

Identique au centime. Les paramètres ne servent à rien.

C'est pire qu'un total faux, parce que cela détruit toute comparaison bâtie
dessus. Tu demandes ce trimestre et le trimestre précédent, tu obtiens deux fois
le même chiffre, donc **le taux de croissance de chaque produit se calcule
exactement à zéro** et la tendance paraît plate quoi qu'il se soit réellement
passé. Une section « meilleurs et moins bons performers du trimestre » est
silencieusement une liste depuis le début de l'exercice.

**La règle.** Ne présente jamais ce rapport comme couvrant une période. Lis
`period` dans la charge utile et étiquette les chiffres avec ce qui est
réellement revenu. Quand un skill a vraiment besoin du chiffre d'affaires
produit sur une fenêtre — une revue trimestrielle, un cycle de réassort, un
contrôle de prix — va le chercher dans une source qui respecte les dates (la
liste des factures, ou le jeu de données de ventes Shopify pour la part en
ligne) et dis laquelle tu as utilisée. Ne rapporte jamais la croissance produit
d'une période à l'autre à partir de cet appel.

---

## Piège 5 — le détail par produit ne couvre qu'une fraction du chiffre d'affaires

Le même appel renvoie un produit, Wholesale Coffee, à 36 587,65 €. Le compte de
résultat du même trimestre annonce 971 794,04 € de produit. **Le rapport
produit couvre 3,8 % de l'entreprise.** Le reste, c'est du chiffre d'affaires
enregistré sans détail produit — acomptes, écritures journalières, recettes de
café — et c'est invisible pour toute vue au niveau produit.

Rien dans la charge utile ne le dit. `% of Sales` affiche `100.0%`, parce que
cela veut dire 100 % des lignes renvoyées, pas 100 % de l'entreprise.

**La règle.** Avant de raisonner à partir d'une quelconque répartition par
produit, somme-la et compare-la au produit de la même période. Quand la
répartition couvre nettement moins que le compte de résultat, dis quelle part
elle couvre avant la première conclusion :

> *« Le détail par produit couvre 36 588 € sur les 971 794 € du trimestre — environ 4 %.
> Ces classements décrivent uniquement la ligne de vente en gros, pas l'entreprise. »*

Une analyse de marge, une recommandation de prix, ou une section « meilleurs
produits » destinée au conseil construite sur 4 % du chiffre d'affaires tout en
laissant croire qu'elle décrit toute l'entreprise, c'est la même erreur qu'une
marge brute de 100 %, qui arrive par une autre porte.

---

## Piège 6 — la synthèse des dettes fournisseurs compense les avoirs dans les seaux

`qbo_accounting_get_ap_aging_summary` soustrait les avoirs d'un fournisseur
(avoirs, trop-perçus, retours) à l'intérieur des seaux d'ancienneté au lieu de
les afficher séparément. Un fournisseur porteur d'un gros avoir entraîne un
seau entier en négatif, et le total des retards avec lui. Par exemple, un total
en retard de **-10 976,21 €**. L'appel de détail pour la même journée
(`qbo_accounting_get_ap_aging_detail`) liste chaque facture ouverte et chaque avoir
comme sa propre ligne, avec le bon signe.

**La règle.** La synthèse n'est une source pour rien, pas même pour un
classement : ses totaux par fournisseur sont déjà compensés, donc un
fournisseur avec 2,4 M€ en retard et 1,5 M€ d'avoir se classe à 911 k€. Pour ce
qui est en retard, ce qui est dû cette semaine, ce qui est dû à un fournisseur
et qui doit le plus, lis le rapport de détail et totalise les lignes toi-même :
factures par date d'échéance, avoirs gardés à part et rapportés comme avoirs.
Contrainte-le (Piège 1) : `due_before` pour une fenêtre, `vendor_name` pour un
fournisseur ; le total de l'ensemble du livre est la ligne dettes fournisseurs
du bilan. Un chiffre négatif quelque part dans une synthèse signifie que ce
piège s'est déclenché ; dis que le fournisseur porte un avoir plutôt que de
 rapporter de l'argent en retard négatif.

C'est le jumeau côté dettes de la règle « un total fournisseur est un chiffre
net » de `ap-processor`, qui applique la même lecture à toute source
d'ancienneté.

---

## Piège 7 — la préparation de la paie contredit la liste des employés

`qbo_payroll_get_company_payroll_readiness` et `qbo_payroll_get_employees` sont
répondus depuis des endroits différents, et ils se contredisent. Sur une même
entreprise, à la même minute :

| Appel | Réponse |
|---|---|
| `qbo_payroll_get_employees` | `total_count: 50` |
| `qbo_payroll_get_company_payroll_readiness` | `has_employees: false`, `run_payroll_ready: false` |

Ce n'est pas une donnée maigre — cinquante employés sont revenus — c'est
l'outil de préparation qui rapporte un état que son jumeau réfute. C'est une
défaillance différente d'une source de paie qui ne renvoie simplement rien, et
`payroll-prep` traite les deux différemment.

**La règle.** Lis les deux appels. Prends l'effectif dans la liste des employés,
puisque c'est l'appel qui a renvoyé des lignes. Ne prépare jamais une exécution
tant que la préparation dit que ce n'est pas prêt, quoi que dise la liste. Dis
les deux réponses au dirigeant sur une seule ligne pour que la contradiction
soit consignée, et signale-la au connecteur au lieu de la contourner.

---

## Bon à savoir aussi

**Le coût des ventes peut être vide même quand il existe des coûts.** Les
coûts imputés à un compte de charge d'exploitation n'atteignent jamais
`totalCogs`, donc la marge brute s'affiche à 100 % alors que l'entreprise a
clairement des coûts. Quand `totalCogs` vaut 0 et que les charges sont
non nulles, dis que la comptabilité n'a pas de ventilation du coût des ventes
plutôt que de rapporter une marge de 100 %.

**Le connecteur ne peut pas écrire d'achats.** La surface d'écriture de
QuickBooks est uniquement côté ventes : factures, devis, clients, produits, liens
de paiement, factures récurrentes, paie. Il n'y a pas d'outil de création de
facture fournisseur, de fournisseur ni de charge. Un skill ne doit jamais
proposer de saisir une facture fournisseur, de créer un fournisseur ou
d'enregistrer une charge dans QuickBooks — il peut seulement les lire et
préparer le travail ailleurs.