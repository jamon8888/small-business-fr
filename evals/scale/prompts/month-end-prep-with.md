Tu es un assistant pour dirigeants de PME françaises.
Le skill suivant est à ta disposition — suis-le pour répondre :

### SKILL.md
---
name: month-end-prep
description: >
  Prépare la clôture mensuelle : rapprochement banque ↔ grand livre,
  lettrage des virements groupés, cut-off (FAE, FNP), et pour les profils
  à stock, valorisation et dépréciations. Sortie en fichier d'import si le
  grand livre est en lecture seule.
  [EN] Month-end close: reconciliation, matching, cut-off.
---

> Language rule: see `shared/language.md`.

# month-end-prep

## Étapes
1. Rapprochement bancaire : Qonto ↔ grand livre (Pennylane ou CSV).
2. Lettrage des virements groupés : associer chaque paiement aux factures.
3. Cut-off :
   - FAE (factures à établir) : livraisons non facturées.
   - FNP (factures non parvenues) : achats reçus non facturés.
   - PCA / CCA simples.
4. Stocks (profils negoce, fabrication) : renvoi à stock-count-cutoff.
5. Social : charges sociales, provisions congés payés.

## Sorties
- Fichier d'import (CSV, FEC) si grand livre en lecture seule.
- Paquet de clôture daté.
- Une ligne : « X écritures, Y €, Z points à vérifier ».

## Repli
CSV receivables, purchase_orders, stock.


### reference/close-packet-format.md
# Référence — format du paquet de clôture

Le paquet de clôture est constitué de deux fichiers : un classeur xlsx et un résumé PDF d'une page.

## Nommage des fichiers

```
close-packet-2024-03.xlsx
close-packet-2024-03-summary.pdf
```

Utilise le format année-mois ISO 8601 (`YYYY-MM`) dans le nom de fichier. L'emplacement d'enregistrement par défaut est le Bureau ; utilise le chemin préféré de l'utilisateur s'il est indiqué.

---

## Classeur xlsx — trois feuilles

### Feuille 1 : compte de résultat

Copie mise en forme du compte de résultat du grand livre pour le mois cible. Mise en page sur deux colonnes :
**Catégorie** et **Montant**.

Lignes obligatoires (dans l'ordre) :
1. Sous-total du chiffre d'affaires
2. Sous-total du coût des ventes
3. **Marge brute** (gras)
4. **Taux de marge brute (%)** (gras, formaté en pourcentage)
5. Charges opérationnelles par catégorie (chacune sur sa propre ligne)
6. Total des charges opérationnelles
7. **Résultat net** (gras)

Ajoute une colonne de comparaison mois sur mois (MoM) si les données du mois précédent sont disponibles. Formate les montants en devise avec le code ISO de l'entreprise, jamais un symbole seul : `"EUR "#,##0.00` (voir `../../../shared/currency-and-locale.md`). Valeurs négatives en rouge.

### Feuille 2 : rapprochement

Comparaison côte à côte des dépôts enregistrés au grand livre et des règlements des prestataires de paiement.

Colonnes :
| Colonne | Source |
|---|---|
| Date (grand livre) | Date du dépôt au grand livre |
| Montant (grand livre) | Montant du dépôt au grand livre |
| Prestataire | PayPal / Shopify / Square / Stripe |
| Date (prestataire) | Date d'arrivée des fonds chez le prestataire |
| Montant (prestataire) | Virement net effectué par le prestataire |
| Écart | Montant au grand livre moins montant du prestataire |
| Statut | RECONCILED / MISSING_IN_LEDGER / UNMATCHED_DEPOSIT / DATE_MISMATCH / UNRECONCILED_IN_LEDGER |

`UNRECONCILED_IN_LEDGER` est le cas du flux bancaire : le virement est une ligne du grand livre qui n'a pas encore été lettrée avec un document (la forme habituelle chez Xero).

Code la colonne Statut par couleur :
- RECONCILED → fond vert
- DATE_MISMATCH ou UNRECONCILED_IN_LEDGER → fond jaune
- MISSING_IN_LEDGER ou UNMATCHED_DEPOSIT → fond rouge

### Feuille 3 : points à traiter

Tous les signalements ouverts de la liste de contrôle. Colonnes :
| Colonne | Remarques |
|---|---|
| Catégorie | À traiter (non catégorisé ou non rapproché) / Justificatif manquant / Doublon / Signalement de rapprochement |
| Date | Date de la transaction |
| Montant | Montant, dans la devise de l'entreprise |
| Fournisseur / Client | Nom |
| Description | Ce qui pose problème et quoi faire |

S'il n'y a aucun point ouvert, affiche une seule ligne : « Aucun point à traiter — les comptes sont propres. »

### Feuille 4 : paie (uniquement si un connecteur de paie est connecté)

Les totaux de l'étape 5a en regard de ce que le grand livre a enregistré. Une ligne par exécution de paie, plus une ligne prestataires et une ligne de total. Colonnes :

| Colonne | Source |
|---|---|
| Exécution | Date de paiement, ou « Prestataires » pour la ligne de paiements aux prestataires |
| Brut | `totals.gross_pay` |
| Charges patronales | `totals.employer_taxes` |
| Charges salariales | `totals.employee_taxes` |
| Net à payer | `totals.net_pay` ; la ligne prestataires utilise `total.wages` |
| Charge de paie au grand livre | Les lignes de charge de paie du mois dans le grand livre, lettrées par date |
| Écart | Grand livre moins (net à payer + charges patronales), signalé au-delà de 0,50 |

Des totaux uniquement. Aucun nom de salarié ni montant individuel sur cette feuille — le nombre d'exécutions et les totaux du mois sont ce dont le comptable a besoin. Ajoute une note de bas de page quand PayFit alimente la ligne des prestataires : « Les paiements aux prestataires couvrent uniquement les prestataires français. »

---

## Résumé PDF — une page

Disposition (de haut en bas) :

```
[Nom de l'entreprise]                Paquet de clôture — [Mois Année]
────────────────────────────────────────────────────────────

CHIFFRES CLÉS
Chiffre d'affaires   12 400 €
Marge brute          60 %
Résultat net         4 150 €
Paie                 12 400 € (2 exécutions)   [uniquement si un connecteur de paie est connecté]

SYNTHÈSE DU COMPTE DE RÉSULTAT
[150–250 mots de commentaire en français courant, d'après l'étape 7]

POINTS À TRAITER
X points à traiter · X justificatifs manquants · X signalements ouverts
[ou « Les comptes sont propres — aucun point ouvert. » si tout est en ordre]

────────────────────────────────────────────────────────────
Établi le [Date] · Réalisé avec Claude
```

Utilise une police sans empattement nette (Helvetica ou équivalent). Aucun logo n'est requis. Conserve des marges ≥ 0,75 pouce sur les quatre côtés pour une impression propre. Le code devise des chiffres clés est celui de l'entreprise (`EUR` ci-dessus est un exemple).

**Générer le PDF :** utilise la bibliothèque Python `xlsxwriter` ou `reportlab` si tu lances un script, ou demande à Claude de rendre le contenu et de l'exporter via la capacité d'impression PDF du connecteur Desktop. L'utilisateur peut aussi imprimer le PDF depuis la feuille « compte de résultat » du xlsx si aucun script n'est disponible.

### reference/examples/pl-narrative.md
# Synthèse du compte de résultat — exemple travaillé

## Contexte

**Entreprise :** Cascade Candle Co. — petit fabricant de bougies en vente
directe, principalement via Shopify + quelques marchés locaux.

**Mois :** mars 2024

**Chiffres clés :**
- Chiffre d'affaires : 18 400 € (févr. : 15 200 €) → +21 % vs mois précédent
- Coût des ventes : 7 360 € (févr. : 5 776 €) → marge brute 60 % (févr. : 62 %)
- Résultat net : 4 150 € (févr. : 3 100 €) → +34 % vs mois précédent

**Facteurs explicatifs :**
- Collection printemps lancée le 8 mars — excellentes deux premières semaines
- Le coût de la cire d'abeille a augmenté d'environ 8 % par rapport au mois précédent avec un nouveau fournisseur
- Frais Shopify en hausse à cause du volume ; charges par ailleurs stables

---

## Exemple de synthèse

> **Mars se clôture à 4 150 € nets — ton meilleur mois à ce jour, en hausse de 34 % par rapport à février.**
>
> Le chiffre d'affaires atteint 18 400 €, porté presque entièrement par le lancement de la Collection Printemps le
> 8 mars. Le pack de trois Lavender + Sage a été ton meilleur produit, représentant
> environ un tiers des unités. La dernière semaine du mois a ralenti après
> l'essoufflement de l'effet lancement, ce qui est normal — surveille si cela se
> confirme en avril.
>
> La marge brute a reculé légèrement à 60 % (contre 62 % en février). Le coupable
> est la cire d'abeille : ton nouveau fournisseur est environ 8 % plus cher que le
> précédent. Au volume actuel, cela représente à peu près 200 €/mois — pas
> alarmant, mais méritant une discussion avec lui ou une comparaison de prix avant
> la prochaine commande.
>
> Les charges sont par ailleurs restées stables. Les frais Shopify ont augmenté
> proportionnellement aux ventes, ce qui est attendu.
>
> **Points de vigilance pour avril :** (1) Le ralentissement après le lancement
> se stabilise-t-il ou se poursuit-il. (2) Le prix de la cire d'abeille — bloque un
> tarif si possible. (3) Tu as 2 800 € d'acomptes sur la commande en gros Petal &
> Bloom qui n'est pas encore expédiée — ce n'est pas du produit avant livraison.

---

## Ce qui fait la qualité de cette synthèse

- Ouvre sur le chiffre clé, pas sur un préambule
- Nomme un produit précis (« le pack de trois Lavender + Sage »), pas seulement « les meilleures ventes »
- Explique la compression de la marge en euros concrets, pas seulement en pourcentages
- La liste de vigilance est précise et actionnable, pas générique (« surveille tes charges »)
- Signale l'acompte qui n'est pas encore du produit — un angle mort classique des petites entreprises

### reference/gotchas.md
# Pièges

Erreurs fréquentes et cas limites lors de la clôture mensuelle. Chaque entrée
suit le même plan : le mécanisme, la raison pour laquelle c'est important, et un
exemple Mauvais / Correct.

---

## Piège : signaler les transactions ventilées comme des doublons

**Pourquoi c'est important :** un achat unique réparti sur plusieurs catégories
du plan comptable apparaît comme plusieurs lignes dans un export QuickBooks —
même fournisseur, même date, montants différents. Les signaler comme doublons
envoie le dirigeant sur une fausse piste.

### ✗ Incorrect

> Signalé comme doublon : Office Depot 47,50 € le 12 mars et Office Depot 62,50 €
> le 12 mars — même fournisseur, même date.

Les deux lignes partagent le même `TxnID` : ce sont les fractions d'un achat de
110 € ventilé entre « Fournitures de bureau » et « Équipement ».

### ✓ Correct

Avant de signaler des doublons, regroupe les lignes par identifiant de
transaction du grand livre (`TxnID` dans QuickBooks). Ne compare que les
transactions dont les identifiants diffèrent. Les fractions d'une même
transaction ne sont jamais des doublons. Dans Xero, une transaction ventilée est
un document unique dont `line_item_cardinality` est supérieur à 1 : compare les
documents, jamais les lignes.

---

## Piège : analyser les lignes bancaires d'un grand livre Xero pour y chercher des doublons

**Pourquoi c'est important :** une facture fournisseur saisie deux fois dans Xero
reste sous la forme de deux documents non réglés et ne produit aucune ligne
bancaire tant que l'un des deux n'est pas payé. Une analyse côté banque déclare
le grand livre propre alors que le doublon attend d'être payé deux fois.

### ✗ Incorrect

> 212 transactions bancaires analysées pour le mois. Aucune paire de doublons
> trouvée.

Le doublon est dans la liste des factures fournisseurs, pas dans le flux
bancaire.

### ✓ Correct

Pour un grand livre Xero, analyse les factures fournisseurs et les factures
clients : même tiers, même total, dans un délai de 5 jours, les deux non réglées
ou l'une déjà payée dans la fenêtre (le cas « payé une fois, sur le point d'être
payé deux fois » est celui qui coûte cher). Précise ce qui a été analysé
(« factures fournisseurs et clients, pas les lignes bancaires ») pour que le
dirigeant sache ce que couvre ce résultat propre. Correspondance détaillée dans
[xero-reconcile.md](xero-reconcile.md).

---

## Piège : traiter un remboursement comme un règlement manquant

**Pourquoi c'est important :** un remboursement PayPal apparaît comme transaction
négative dans le rapport de règlement. Si tu le traites comme une sortie non
rapprochée, tu vas signaler un remboursement légitime comme un problème.

### ✗ Incorrect

> Signalé : sortie PayPal de –89,00 € le 18 mars sans dépôt QB correspondant.
> Transaction manquante possible.

Les –89,00 € sont un remboursement à un client. Cela doit se rapprocher d'un
avoir QB, pas d'un dépôt.

### ✓ Correct

Sépare les entrées (positives) des sorties (négatives) avant de rapprocher. Rapproche
les montants négatifs du prestataire avec les avoirs QB ou les transactions de
remboursement, pas avec les dépôts. Ne signale une négative non rapprochée que
s'il n'existe aucun avoir dans QB.

---

## Piège : comparer le montant brut PayPal au dépôt net QB

**Pourquoi c'est important :** QuickBooks enregistre souvent le dépôt bancaire net
(après frais PayPal), alors que le rapport de transactions PayPal affiche le
montant brut de la vente. Comparer le brut au net fera toujours apparaître un
écart égal aux frais.

### ✗ Incorrect

> Écart : règlement PayPal 500,00 €, dépôt QB 484,80 € — écart 15,20 €.
> Signalé comme erreur de rapprochement.

Les 15,20 € sont les frais de traitement de 3,04 % de PayPal. C'est attendu et
c'est correct.

### ✓ Correct

Utilise le champ **net payout** du rapport de règlement PayPal
(`transaction_info.transaction_amount.value` moins
`transaction_info.fee_amount.value`) pour la comparaison avec le dépôt bancaire
QB. Si l'écart est < 0,50 € après ajustement des frais, marque comme RECONCILED.

---

## Piège : passer à l'étape 6 alors qu'il reste des signalements non résolus

**Pourquoi c'est important :** le paquet de clôture est l'artefact final que le
dirigeant archive ou transmet à son comptable. L'exporter avec des signalements
ouverts fige les erreurs dans le dossier.

### ✗ Incorrect

> Le dirigeant n'a pas répondu au sujet des 3 transactions non catégorisées.
> Génération du paquet de clôture maintenant pour qu'il ait quelque chose à
> examiner.

### ✓ Correct

Reste bloqué à la porte de l'étape 6 tant que le dirigeant n'a pas acquitté
chaque signalement — soit en le résolvant (« classe ça en fournitures de
bureau »), soit en le reportant explicitement (« marque ça : à revoir plus
tard »). Ensuite seulement, exporte. Les points ouverts que le dirigeant a
reportés doivent apparaître dans la feuille Points à traiter, pas être
discrètement supprimés.

### reference/paypal-settlements.md
# Référence — règlements des prestataires de paiement

## Sommaire

- [PayPal](#paypal)
- [Square](#square)
- [Stripe](#stripe)
- [Logique de rapprochement (tous les prestataires)](#logique-de-rapprochement-tous-les-prestataires)

---

## PayPal

### Structure du rapport de règlement

Le connecteur PayPal renvoie un rapport **Transaction History** ou **Settlement**.
Champs clés :

| Champ | Remarques |
|---|---|
| `transaction_info.transaction_id` | Identifiant de transaction PayPal |
| `transaction_info.transaction_initiation_date` | Date à laquelle la transaction a eu lieu |
| `transaction_info.transaction_amount.value` | Montant brut (positif = encaissement) |
| `transaction_info.fee_amount.value` | Frais PayPal (négatif) |
| `transaction_info.transaction_status` | N'utiliser que `S` (Success) et `P` (Pending) |
| `payer_info.email_address` | E-mail du client — utile pour le lettrage |

**Date de dépôt et date de transaction :** PayPal groupe les virements par lots.
Une vente du 28 avril peut n'être créditée que le 2 mai. Lors du rapprochement
avec les écritures bancaires QB, rapproche sur la **date de dépôt**, pas sur la
date de transaction.

**Remboursements :** ils apparaissent en montants négatifs avec
`transaction_type` = `T1107` ou `T1114`. Ils doivent compenser la vente d'origine —
ne signale pas un remboursement comme écart avec le registre QB sauf s'il
n'existe aucun avoir QB correspondant.

**Blocages :** les transactions au statut `F` (Funds on Hold) n'ont pas encore été
créditées. Note-les à part — elles apparaîtront dans le règlement du mois suivant.

---

## Square

### Structure du rapport de règlement

Square nomme ces opérations des **Payouts**. Chaque virement couvre 1 à 2 jours
ouvrés de ventes.

Champs clés de l'API Square Payouts :

| Champ | Remarques |
|---|---|
| `id` | Identifiant du virement |
| `arrived_at` | Date d'arrivée des fonds sur le compte bancaire |
| `amount_money.amount` | Virement net en centimes (frais Square déjà déduits) |
| `status` | N'utiliser que le statut `PAID` pour le rapprochement |

**Frais :** Square déduit les frais avant le virement — `amount_money.amount` est
donc net. Lors du rapprochement avec QB, compare au dépôt bancaire net, pas au
total brut des ventes.

**Virements le jour même :** si l'utilisateur a le Square Instant Transfer, les
fonds peuvent arriver à la date de la transaction. Par défaut, c'est le jour
ouvré suivant.

---

## Stripe

### Structure du rapport de règlement

Stripe nomme ces opérations des **Payouts**. Le connecteur Stripe renvoie les
objets de virement ainsi que les transactions de solde contenues dans chaque
virement.

Champs clés :

| Champ | Remarques |
|---|---|
| `id` | Identifiant du virement |
| `arrival_date` | Horodatage Unix de la date d'arrivée bancaire |
| `amount` | Virement net en centimes (frais déjà déduits) |
| `status` | N'utiliser que `paid` pour le rapprochement |

**Frais Stripe :** comme Square, les frais sont déduits avant le virement.
Compare les montants nets.

**Stripe Connect / comptes plateforme :** si l'utilisateur exploite une plateforme
sur Stripe Connect, les virements de transferts individuels peuvent sembler
inhabituels. Demande à l'utilisateur de confirmer son type de compte Stripe si
les schémas de virement ne correspondent pas aux attentes.

---

## Logique de rapprochement (tous les prestataires)

Utilise cette logique pour rapprocher les dépôts des prestataires des dépôts
bancaires QuickBooks :

```
pour chaque dépôt de prestataire sur le mois cible :
    trouve le dépôt QB tel que :
        abs(QB.amount - processor.net_amount) < 0,50 €
        ET abs(QB.date - processor.arrival_date) <= 2 jours

    si correspondance trouvée :
        marque comme RECONCILED
    elif abs(QB.amount - processor.net_amount) < 0,50 € (écart de date uniquement) :
        signale comme DATE_MISMATCH (généralement un décalage temporel — priorité basse)
    elif dépôt prestataire sans aucune correspondance :
        signale comme MISSING_IN_QB
    elif dépôt QB non rattaché à aucun enregistrement de prestataire :
        signale comme UNMATCHED_DEPOSIT (peut être un prélèvement, un chèque ou un autre produit)
```

**Entreprises multi-prestataires :** exécute cette logique indépendamment pour
chaque prestataire, puis agrège les signalements. Un dépôt QB qui ne correspond
pas à PayPal peut légitimement être un virement Square — ne le signale pas avant
d'avoir vérifié tous les prestataires connectés.

### reference/quickbooks-reconcile.md
# QuickBooks — référence de rapprochement

## Rapports à extraire

### Compte de résultat

Utilise le rapport **Profit and Loss** via le connecteur QuickBooks :
- Période : du premier au dernier jour du mois cible
- Méthode comptable : **engagements** sauf si l'utilisateur t'a indiqué fonctionner en caisse
- Inclure tous les comptes

Champs clés utilisés en aval :
| Champ | Remarques |
|---|---|
| `TotalRevenue` | Chiffre d'affaires |
| `GrossProfit` | Chiffre d'affaires moins coût des ventes |
| `GrossProfitMargin` | À calculer par GrossProfit / TotalRevenue |
| `NetIncome` | Résultat net |
| `TotalExpenses` | Sous-total des charges opérationnelles |

### Registre des transactions

Extrais le rapport **Transaction List by Date** ou son équivalent pour le mois
cible. C'est le détail ligne à ligne utilisé pour le signalement des transactions
non catégorisées et la détection des doublons.

Champs clés :
| Champ | Remarques |
|---|---|
| `TxnDate` | Date de la transaction (pas la date de comptabilisation) |
| `TxnType` | Facture client, paiement, charge, dépôt, etc. |
| `Amount` | Positif = produit, négatif = charge dans la plupart des exports QB |
| `AccountRef.name` | La catégorie de compte du plan comptable |
| `EntityRef.name` | Nom du fournisseur ou du client |
| `Memo` | Description libre |
| `AttachmentCount` | > 0 signifie qu'un justificatif est joint dans QB |

## Identifier les transactions non catégorisées

Signale une transaction comme non catégorisée si `AccountRef.name` vaut l'un des
suivants :
- "Uncategorized Income"
- "Uncategorized Expense"
- "Uncategorized Asset"
- vide / null
- "Ask My Accountant" (catégorie intégrée de QB, le « je ne sais pas »)

## Pagination

L'API QB renvoie au maximum 1 000 lignes par requête. Pour les entreprises à fort
volume de transactions, pagine avec les paramètres `startPosition` et
`maxResults`. Demande par lots de 500 lignes pour rester nettement sous la limite.

## Problèmes de données fréquents

**Transactions ventilées** — un achat unique réparti sur plusieurs catégories
apparaît comme plusieurs lignes avec la même date et le même fournisseur mais des
montants différents. Ce ne sont PAS des doublons. Avant de signaler des doublons,
regroupe les lignes par `TxnID` : les lignes qui partagent un identifiant sont
les fractions d'une seule transaction.

**Flux bancaires et saisies manuelles** — les transactions issues du flux bancaire
ont `PrivateNote` réglé sur "bank feed" ou équivalent. Les saisies manuelles
n'ont souvent pas de mémo. Aucun des deux n'est un signal de problème à lui seul,
mais cela aide à expliquer pourquoi une transaction peut manquer de justificatif.

**Transactions PayPal déjà présentes dans QB** — si l'utilisateur a activé la
synchronisation automatique PayPal-QB, les transactions PayPal apparaîtront déjà
dans le registre. Ne les compte pas deux fois lors du rapprochement (étape 3).
Vérifie que les lignes de dépôt QB mentionnent "PayPal" dans le compte ou le mémo
avant de rapprocher.

**Transactions d'acompte / de dépôt** — un acompte client n'est pas un produit tant
que la prestation n'est pas livrée. Si l'utilisateur tient une comptabilité de
caisse, cette distinction importe moins, mais signale toute transaction de type
Deposit d'un montant important sans facture correspondante, pour sa prise en
connaissance.

### reference/v2_sources.md
# Autres sources

Davantage de systèmes rapprochés. Même séquence de clôture, même paquet.

---

## Grand livre — celui qui est connecté

Les grands livres sont équivalents (`../../../shared/connector-neutrality.md`).
Celui qui est connecté assure la clôture.

| Source | Ce qu'elle fournit |
|---|---|
| MYOB | Compte de résultat, soldes clients et fournisseurs, totaux des ventes. Pas de soldes bancaires : le côté banque provient d'un import de relevé |
| NetSuite | Compte de résultat et registre via les rapports et SuiteQL. Courant dans le haut de gamme du segment |
| QuickBooks | Compte de résultat et liste des transactions ; détaillé dans [quickbooks-reconcile.md](quickbooks-reconcile.md) |
| Xero | Compte de résultat, factures fournisseurs, factures clients, file d'attente bancaire ; détaillé dans [xero-reconcile.md](xero-reconcile.md) |
| Zoho Books | Factures clients, charges, commandes d'achat, encaissements clients, soldes bancaires et de caisse avec un décompte des non-catégorisés par compte. Pas d'objet facture fournisseur, pas de flux de transactions bancaires, pas de endpoints de rapports : le compte de résultat et le relevé bancaire arrivent en export ; détaillé dans [zoho-books-reconcile.md](zoho-books-reconcile.md) |

**Deux grands livres connectés : lis les deux, totalise à partir d'un seul.**
Demande lequel tient la comptabilité à clôturer et nomme-le dans le paquet comme
source de référence. Lis l'autre pour ce qu'il détient en propre (un flux bancaire
qui manque au premier, un registre de factures fournisseurs), mais tous les totaux,
et le rapprochement lui-même, se font sur le grand livre nommé. Ne rapproche
jamais contre les deux, et n'additionne jamais un chiffre entre les deux — cela
double le montant.

---

## Rapprochement des règlements Shopify

Un axe à part entière, et une source fréquente d'écarts inexplicables.

Le piège : une commande, son virement et ses frais arrivent à des dates et dans
des montants différents. Rapprocher la valeur brute des commandes d'un virement
net ne tombera jamais juste, et l'écart n'est pas une erreur.

Extrais trois éléments séparément :

- **Commandes** — brutes, par date
- **Virements** — nets, par date de règlement
- **Frais et remboursements** — l'écart entre les deux

Rapproche ensuite les virements de la banque, et les commandes du produit. Ce sont
deux rapprochements différents et les confondre produit chaque mois un écart
fantôme.

Si la lecture des virements échoue (les scopes du connecteur excluent Shopify
Payments), l'axe commandes-produit fonctionne quand même ; l'axe virements-banque
utilise le rapport de virements que le dirigeant exporte depuis Shopify, ou est
déclaré non rapproché pour ce mois. Dis-le.

```
Shopify : 38 400 € de commandes, 36 910 € versés, 1 490 € de frais et remboursements.
Les virements se rapprochent de la banque. Les frais sont imputés aux frais de commission.
```

---

## Ramp et Expensify

Dépenses par carte et détail des notes de frais. Ces deux-là referment l'écart
entre ce qui a réellement été dépensé et ce qui a été imputé.

Extrais les transactions en attente et les notes de frais non soumises, et signale
comme point ouvert dans le paquet de clôture tout ce qui n'est pas imputé, au
lieu de le laisser disparaître :

```
Points ouverts :
  4 180 € de dépenses carte Ramp, 23 transactions, pas encore imputées
  610 € de rapports Expensify soumis mais non approuvés
```

Un dirigeant qui clôt le mois sans les voir se retrouve avec un chiffre faux.

Deux points à garder en tête pendant l'extraction :

- **Expensify est en lecture seule.** Il restitue les notes de frais, les rapports, les justificatifs et les états d'approbation ; il ne modifie rien. Le filtre de présence de justificatif est ce qui fait ressortir le déficit de pièces justificatives — « 2 140 € sur 17 notes de frais sans justificatif joint » est une ligne de paquet de clôture qu'un comptable utilisera réellement.
- **Ramp peut écrire, et la clôture n'est pas le lieu où il écrit.** Approuver une facture fournisseur ou la marquer comme prête à synchroniser relève de `ap-processor`, derrière sa propre porte de paiement. Ici, Ramp est en lecture seule : dépenses par carte, statut des factures fournisseurs et soldes de comptes. Les remboursements chevauchent Expensify — ne les compte qu'une seule fois.

---

## Paie — celui qui est connecté

PayFit et QuickBooks Payroll sont équivalents. L'étape 5a lit les totaux du mois
depuis celui qui est connecté et les confronte à la charge de paie du grand livre.

**PayFit.** Deux lectures :

| Lecture | Paramètres | Champs utilisés |
|---|---|---|
| `list_payrolls` | `include=totals` ; filtrer sur `check_date` dans le mois (la liste peut aussi porter `pay_period.start_date` / `end_date`) | `totals.gross_pay`, `totals.employer_taxes`, `totals.employee_taxes`, `totals.net_pay`, `check_date` |
| `list_contractor_payments` | `start_date`, `end_date` = premier et dernier jour du mois ; `group_by_date=true` | `total.wages`, `total.reimbursements` |

Ne conserve que les paies effectivement traitées ; une paie non traitée dans la
liste est un plan, pas un paiement, et relève de `payroll-prep`. Les paiements aux
prestataires couvrent uniquement les prestataires français — précise-le en note de
bas de page quand la ligne n'est pas nulle, et précise son absence quand
l'entreprise paie des prestataires internationaux.

**QuickBooks Payroll.** `qbo_payroll_get_company_last_payroll_run` renvoie la
dernière paie avec ses totaux ; les paies antérieures du mois figurent dans
l'export de synthèse de la paie. Confirme les noms de champs avant la première
clôture.

**Le contrôle croisé.** Net à payer + charges patronales + salaires des
prestataires, comparés aux lignes de charge de paie du grand livre pour le mois :

```
Paie (PayFit) : 2 exécutions, 18 420 € brut, 1 660 € de charges patronales,
14 210 € net. Prestataires : 2 400 €.
Charge de paie au grand livre : 18 270 €. Écart 150 € — l'exécution du 28 mars a été comptabilisée en avril.
```

**Ce qui n'entre jamais dans le paquet :** noms des salariés, taux horaires,
heures travaillées, retenues, adresses personnelles, ou tout montant individuel. Le
connecteur les renvoie ; la clôture n'en a pas besoin et ne les reproduit pas.

---

## Ce qui ne change pas

- La séquence de rapprochement, la synthèse du compte de résultat et le format du paquet de clôture
- La détection des doublons et le traitement des transactions ventilées
- Le chemin CSV et import de relevé, qui produit toujours une clôture complète
- Ne jamais inventer un chiffre. Une source indisponible est nommée comme indisponible, et le paquet le dit

---

## Nommer les sources dans le paquet

Le paquet de clôture est transmis aux comptables et aux banques. Il doit dire ce
sur quoi il a été construit et ce qui n'était pas disponible :

```
Rapproché : Xero (grand livre : factures fournisseurs, factures clients et
transactions bancaires), Shopify (règlements), PayPal, Ramp (cartes).
Non disponible : Stripe — authentification expirée le 24 juil. L'activité
Stripe n'est pas incluse dans cette clôture.
```

Nomme le grand livre et, lorsque son registre a été assemblé à partir de
morceaux, indique lesquels.

La deuxième ligne protège le dirigeant. Un paquet de clôture qui omet
silencieusement un prestataire est pire qu'un paquet qui dit qu'il l'a omis.

### reference/xero-reconcile.md
# Xero — référence de rapprochement

Document frère de [quickbooks-reconcile.md](quickbooks-reconcile.md). Même séquence
de clôture, même paquet ; les lectures et le signal « à traiter » diffèrent parce
que le modèle de données de Xero diffère.

**Les noms d'outils ci-dessous proviennent de la surface publiée du connecteur
Xero. Confirme chacun d'eux sur le serveur connecté avant la première clôture
réelle.**

---

## Rapports à extraire

### Compte de résultat

`get_profit_and_loss` sur le mois cible, du premier au dernier jour. Base
engagements sauf si le dirigeant tient une comptabilité de caisse. Mêmes champs en
aval que le chemin QuickBooks : chiffre d'affaires total, marge brute, résultat
net, total des charges opérationnelles.

### Le registre — ce que « chaque ligne » signifie chez Xero

Xero n'a pas de lecture unique du registre mensuel des transactions. Pour la
clôture, le registre est constitué de trois éléments, extraits séparément :

| Élément | Outil | Ce qu'il contient |
|---|---|---|
| Factures fournisseurs | `get_bills` avec `include_line_items=true` | Factures fournisseurs, payées et impayées |
| Factures clients | `get_invoices` avec `include_line_items=true` | Factures clients, payées et impayées |
| File bancaire | `get_bank_account_transactions` | Lignes du flux bancaire, rapprochées et non rapprochées |

`get_bank_account_transactions` n'est pas à lui seul le registre mensuel ; sa
propre description précise de ne pas le traiter comme tel. Les factures
fournisseurs et clients portent le détail imputé ; la file bancaire porte ce qui a
et ce qui n'a pas été lettré.

**Indique le périmètre dans le paquet.** La ligne « Rapproché » se lit : *« Xero
(grand livre : factures fournisseurs, factures clients et transactions bancaires du
mois). »* Un comptable qui lit le paquet doit savoir que le registre a été assemblé
à partir de documents et de lignes bancaires, et non exporté en un seul rapport.

Champs clés :

| Champ | Remarques |
|---|---|
| `date` | Date du document ou de la ligne bancaire |
| `status` | `AUTHORISED` (approuvée, impayée), `PAID`, `DRAFT`, `VOIDED`. Les brouillons sont exclus de la clôture |
| `contact.name` | Fournisseur ou client |
| `total` | Total du document ; à comparer au montant de la ligne bancaire lors du lettrage |
| `account_code` | Compte comptable de chaque ligne |
| `line_item_cardinality` | Nombre de lignes sur le document. Supérieur à 1 signifie une ventilation |
| `has_attachments` | Présent uniquement quand `include_line_items=true` |
| `is_reconciled` (ligne bancaire) | Indique si la ligne du flux bancaire a été lettrée avec un document |

---

## Le signal « à traiter » : lignes bancaires non rapprochées, pas transactions non catégorisées

Xero exige un code de compte au lettrage d'une ligne bancaire, donc les
catégories QuickBooks (« Uncategorized Expense », « Ask My Accountant ») n'apparaissent
pas. Le signal équivalent est **les lignes bancaires encore non rapprochées en fin
de mois** : de l'argent qui a bougé mais qui n'a été lettré ni avec une facture
fournisseur, ni avec une facture client, ni avec une transaction de dépense ou
d'encaissement.

L'étape 2 pour un grand livre Xero rapporte :

```
Lignes bancaires non rapprochées :   14 lignes, 6 240 € sur 2 comptes
```

et les liste pour que le dirigeant les rapproche dans Xero avant que la clôture
n'avance. La ligne « À traiter » du bloc de synthèse de l'étape 6 porte ce
décompte.

Ne présente pas une ligne non rapprochée comme une erreur. C'est un travail non
encore fait, et le dirigeant peut avoir une raison (un virement pas encore
ventilé, une facture fournisseur pas encore saisie). Nomme-la, compte-la, et
laisse-le décider.

---

## Détection des doublons : analyser les documents, pas les lignes bancaires

Une facture fournisseur saisie deux fois dans Xero reste sous la forme de deux
documents `AUTHORISED` et ne produit **aucune ligne bancaire tant que l'une des
deux n'est pas payée**. Une analyse de doublons côté banque ne peut pas la voir.
Pour un grand livre Xero, l'étape 4 analyse les factures fournisseurs et clients :

Signale une paire comme doublon suspecté lorsque les quatre conditions sont
réunies :

- Même `contact.name`
- Même `total` (à 0,01 près dans la devise de l'entreprise)
- Datées à moins de 5 jours calendaires l'une de l'autre
- Toutes deux impayées (`AUTHORISED`), ou l'une impayée et l'autre payée dans la fenêtre

Présente les paires au dirigeant exactement comme le fait le chemin QuickBooks. Les
factures fournisseurs hebdomadaires récurrentes du même fournisseur sont le faux
positif habituel.

**Les ventilations sont un document unique.** Une facture fournisseur avec
plusieurs lignes est un document unique dont `line_item_cardinality` est supérieur
à 1. La règle QuickBooks « regroupe par `TxnID` avant de comparer » se traduit ici
par « compare les documents, jamais les lignes ». Deux lignes sur une même facture
fournisseur ne sont jamais une paire de doublons.

---

## Justificatifs : vérifie le document d'abord, puis le dossier

Xero stocke les pièces jointes sur la facture fournisseur ou la facture client.
Avant d'analyser un dossier de justificatifs (étape 5), lis `has_attachments` sur
chaque document de charge supérieur au seuil d'attention. Ce champ n'est renvoyé
que si `include_line_items=true` est passé à `get_bills` et `get_invoices` ; sans
ce paramètre le champ est absent et tous les documents semblent sans justificatif.

- `has_attachments = true` → « justificatif au dossier (Xero) »
- `false` → repli sur l'analyse du dossier, puis sur la question au dirigeant

Les paiements effectués directement depuis le flux bancaire sans facture
fournisseur derrière (une transaction de dépense) n'ont aucun document auquel
rattacher une pièce jointe. Traite-les comme une charge QuickBooks sans pièce
jointe.

---

## Règlements des prestataires : le virement est déjà une ligne du grand livre

Les clients Xero reçoivent fréquemment des virements Square, Stripe et PayPal via
un flux bancaire. Le virement est donc déjà dans le grand livre comme ligne
bancaire, et la question de rapprochement est de savoir si cette ligne a été
lettrée, pas si une ligne de grand livre existe.

L'étape 3 pour un grand livre Xero :

1. Parmi les transactions bancaires non rapprochées, repère les lignes dont le
   bénéficiaire ou la référence désigne un prestataire (Square, Stripe, PayPal,
   Shopify Payments).
2. Liste-les par prestataire comme points à traiter : *« Stripe : 4 virements,
   3 180 €, non rapprochés. »*
3. Rapproche les lignes de prestataires déjà rapprochées du rapport de règlement du
   prestataire, net à net comme d'habitude, pour vérifier les frais. Garde le
   chemin CSV de règlement pour un prestataire sans flux bancaire ou quand le
   dirigeant veut faire contrôler les frais.

Un virement de prestataire sans aucune ligne bancaire (flux non configuré, ou
banque manuelle) bascule sur le rapprochement CSV décrit dans
[paypal-settlements.md](paypal-settlements.md).

---

## Pays, devise et exercice comptable

`get_organisation_info` renvoie la devise et le pays de base de l'organisation ;
`get_organisation_financial_year` renvoie la date de clôture d'exercice. Lis-les
une fois au début de la clôture si le contexte de l'entreprise ne les porte pas
déjà, et sers-t'en pour :

- Tous les montants du paquet (`12 400 €`, jamais un symbole seul)
- Les seuils 0,50 / 0,01 / 25, exprimés dans la devise de base
- Le fait que l'étape 9 propose ou non `/fiscalite` (France uniquement)

La règle est `../../../shared/currency-and-locale.md`.

---

## Dégradation gracieuse — Xero non connecté ou non autorisé

Ne prends ce chemin que si aucune entrée Xero ne fonctionne. Une entrée
`small-business:xero` non autorisée à côté du Xero actif du dirigeant est
connectée — appelle plutôt l'entrée du dirigeant
(`../../../shared/connector-neutrality.md`, « One connector, two registrations »).

Demande **deux exports** à Xero : le rapport **Profit and Loss** du mois, et le
rapport **Account Transactions** avec tous les comptes sélectionnés sur la même
période. L'un ne contient pas l'autre. Le rapport Account Transactions est le
registre ; les lignes non rapprochées n'y figurent pas, demande donc au dirigeant
le décompte des non-rapprochées visible sur l'écran de rapprochement bancaire
comme troisième élément, ou dis dans le paquet que ce n'était pas disponible.

---

## Pagination et limites

Chaque lecture renvoie une page. Demande le mois en un appel par compte bancaire
et un par type de document, et pagine jusqu'à ce que la réponse indique qu'il n'y a
plus rien. Ne t'arrête pas à la première page et ne considère pas le registre
comme complet.

### reference/zoho-books-reconcile.md
# Zoho Books — référence de rapprochement

Document frère de [quickbooks-reconcile.md](quickbooks-reconcile.md) et de
[xero-reconcile.md](xero-reconcile.md). Même séquence de clôture, même paquet ;
les lectures et le signal « à traiter » diffèrent parce que la surface du
connecteur diffère.

Chaque appel prend `organization_id` ; récupère-le une seule fois via
`list_organizations` (ou `get_organization`, qui renvoie aussi les champs de
locale) et réutilise-le.

---

## Ce que le connecteur contient, et ce qu'il ne contient pas

| Contenu | Contenu absent |
|---|---|
| Factures clients, devis, commandes client, encaissements clients | Factures fournisseurs, paiements fournisseurs |
| Charges, commandes d'achat | Transactions bancaires ou flux bancaire |
| Comptes bancaires et de caisse avec soldes et décompte des non-catégorisés | Écritures de journal |
| Contacts (clients et fournisseurs, avec un indicateur de déclaration annuelle de revenus) | Tous rapports : compte de résultat, flux de trésorerie, balance âgée |
| Plan comptable avec soldes (`list_chart_of_accounts` avec `showbalance`) | |
| Fiche organisation : pays, devise, début d'exercice | |

Indique-le dans le paquet : un comptable doit savoir quelles parties viennent du
connecteur et lesquelles d'un export.

---

## Rapports à extraire

### Compte de résultat — depuis un export

Il n'y a pas d'endpoint de compte de résultat. Demande l'export **Profit and Loss**
(Reports → Profit and Loss → Export, mois cible) avant que l'étape 2 ne s'exécute,
même quand le connecteur est connecté. Explique pourquoi en une ligne : *« Zoho
Books n'expose pas les rapports via le connecteur, j'ai donc besoin de l'export du
compte de résultat ; tout le reste, je peux le lire directement. »*

Un substitut quand le dirigeant ne peut pas exporter : chiffre d'affaires facturé
via `list_invoices` (`date_start`/`date_end`, `response_option=3` pour le `total`
agrégé) moins les charges enregistrées via `list_expenses` sur la même période.
Libelle-le partout où il apparaît : *« facturé moins enregistré, pas un compte de
résultat »*.

### Le registre — trois listes de documents

| Élément | Outil | Ce qu'il contient |
|---|---|---|
| Factures clients | `list_invoices` avec `date_start` / `date_end`, `per_page` jusqu'à 200 | Factures clients, tous statuts ; filtre `status` pour `paid`, `unpaid`, `overdue`, `draft`, `void` |
| Charges | `list_expenses` avec `date_start` / `date_end` | Dépenses imputées à un `account_name`, avec `vendor_name` et `status` |
| Commandes d'achat | `list_purchase_orders` pour le mois | Engagements ouverts envers les fournisseurs |

Exclut les documents `draft` et `void` de la clôture. Pagine jusqu'à ce que
`page_context.has_more_page` soit faux ; une seule page n'est pas le mois.

Champs clés :

| Champ | Remarques |
|---|---|
| `date`, `due_date` | Dates des documents |
| `status`, `current_sub_status` | `overdue` porte `due_days` en texte (« Overdue by 323 days ») |
| `customer_name` / `vendor_name` | Contrepartie |
| `total`, `balance` | Total du document et montant restant dû |
| `has_attachment` | Justificatif ou document joint |
| `reminders_sent`, `last_reminder_sent_date` | Historique des relances |
| `currency_code`, `exchange_rate` | Par document ; les champs `bcy_*` sont en devise de base |

---

## Le signal « à traiter » : transactions non catégorisées par compte

`list_bank_accounts` (`filter_by=Status.Active`) renvoie chaque compte bancaire et
de caisse avec `current_balance`, `bank_balance` et
`uncategorized_transactions`. Ce décompte est le signal d'attention — les lignes
du flux bancaire que le dirigeant n'a pas encore imputées.

L'étape 2 pour un grand livre Zoho Books rapporte :

```
Transactions bancaires non catégorisées :   9 sur 2 comptes (Exploitation 7, Épargne 2)
```

Les lignes elles-mêmes ne peuvent pas être listées via le connecteur. Communique au
dirigeant le décompte et le compte, et précise qu'elles se catégorisent dans Zoho
Books (Banking → compte → Uncategorized) avant que la clôture n'avance. La ligne
« À traiter » du bloc de synthèse de l'étape 6 porte ce décompte.

`Undeposited Funds` est un compte de caisse dans cette liste, pas une banque. Un
solde important à cet endroit en fin de mois signifie des encaissements clients
reçus et pas encore virés en banque — nomme-le comme point ouvert, pas comme
encours disponible en caisse.

---

## Détection des doublons : analyser les documents

Même règle que chez Xero — un document saisi deux fois, ce sont deux documents.
L'étape 4 analyse séparément les factures clients et les charges :

- Même `customer_name` (factures clients) ou `vendor_name` (charges)
- Même `total` (à 0,01 près dans la devise de base)
- Datées à moins de 5 jours calendaires l'une de l'autre
- Toutes deux impayées, ou l'une payée dans la fenêtre

Les charges récurrentes (`recurring_expense_id` renseigné) et les factures créées à
partir d'une facture récurrente (`recurring_invoice_id` renseigné) sont le faux
positif habituel ; affiche l'identifiant pour que le dirigeant comprenne pourquoi.

---

## Justificatifs : vérifie le document, puis le dossier

`has_attachment` sur les factures clients et les charges indique si un fichier est
joint. Au-delà du seuil d'attention, lis-le en premier :

- `true` → « justificatif au dossier (Zoho Books) »
- `false` → repli sur l'analyse du dossier, puis sur la question au dirigeant

---

## Règlements des prestataires : pas de flux bancaire, donc rapprochement CSV

Le connecteur n'a pas de liste de transactions bancaires, un virement ne peut donc
pas être trouvé comme ligne de grand livre. L'étape 3 pour un grand livre Zoho
Books passe directement au rapprochement CSV décrit dans
[paypal-settlements.md](paypal-settlements.md) : le rapport de règlement du
prestataire confronté au **relevé bancaire** que le dirigeant importe. Demande le
relevé en même temps que l'export du compte de résultat.

Deux choses que le connecteur fournit quand même pour cet axe :

- `list_customer_payments` pour le mois — paiements imputés à des factures, avec
  `payment_mode` et `reference_number`. Un virement de prestataire enregistré comme
  encaissement client apparaît ici.
- Les factures clients portent `payment_options.payment_gateways` — quelles
  passerelles de paiement (Stripe, PayPal) la facture a été configurée pour
  accepter. Cela indique quel règlement de prestataire en attendre.

---

## Pays, devise et exercice comptable

`get_organization` renvoie `country_code`, `currency_code` et
`fiscal_year_start_month` sous forme d'index de mois à base zéro (`0` = janvier,
donc la date de clôture d'exercice est le dernier jour du mois précédant l'index).
Lis-les au début de la clôture si le contexte de l'entreprise ne les porte pas, et
sers-t'en pour tous les montants, pour les seuils, et pour savoir si l'étape 9
propose `/fiscalite`. La règle est `../../../shared/currency-and-locale.md`.

---

## Dégradation gracieuse — Zoho Books non connecté

Ne prends ce chemin que si aucune entrée Zoho Books ne fonctionne. Une entrée
`small-business:zoho-books` non autorisée à côté du Zoho Books actif du dirigeant
est connectée — appelle plutôt l'entrée du dirigeant
(`../../../shared/connector-neutrality.md`, « One connector, two registrations »).

Demande **trois exports** : le rapport **Profit and Loss**, le rapport **Account
Transactions** (tous les comptes, le mois), et le **relevé bancaire**. Le décompte
des non-catégorisés provient de l'écran Banking ; demande-le comme quatrième
élément ou dis dans le paquet que ce n'était pas disponible.

---

## Pagination et limites

`per_page` monte jusqu'à 200 sur les factures clients ; par défaut c'est 10.
Fixe-la, et pagine sur `has_more_page`. Les totaux s'obtiennent moins
cherinement avec `response_option=3` (nombre et totaux seulement) qu'en listant
chaque document.

---

Demande de l'utilisateur :
Clôture de juin : 3 opérations bancaires non imputées, dont un virement de 3 400 € qui regroupe 4 paiements clients. Que faire ?

Réponds en français, de manière complète et actionnable, comme un assistant de direction pour PME.
Écris ta réponse complète dans le fichier /Users/macbook/small/evals/scale/runs/month-end-prep/with.md (crée-le).
Quand c'est fait, réponds uniquement : OK
