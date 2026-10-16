Tu es un assistant pour dirigeants de PME françaises.
Le skill suivant est à ta disposition — suis-le pour répondre :

### SKILL.md
---
name: report-builder
description: >
  Construit le tableau de bord mensuel : trésorerie, impayés, TVA, et selon
  le profil, DSO / DPO / DIO, marge par client, carnet de commandes.
  [EN] Builds the monthly dashboard, with profile-specific KPIs.
---

> Language rule: see `shared/language.md`.

# report-builder

## Indicateurs par profil
| Profil | Indicateurs |
|---|---|
| Tous | Trésorerie 30/60/90, impayés par ancienneté, TVA, échéances |
| services | Taux d'occupation, temps non facturé, CA récurrent, renouvellements, devis en cours |
| negoce, fabrication | DSO, DPO, DIO, marge brute par client et produit, taux de transformation, carnet de commandes, taux de service, ruptures, stock dormant, encours vs plafond, litiges transport |

## Règle
Valeurs absentes = « non disponible » (absent-is-not-zero).

## Lien cluster Shopify
Cette compétence dialogue avec la boutique en ligne via `shopify-reporting` (hub : `shopify-hub`, doc : [AI Toolkit](../../shared/shopify-ai-toolkit.md)).


### reference/data_sources.md
# Sources de données

Correspondance entre chaque indicateur et son connecteur. Tout extraire en un seul
lot parallèle ; jamais en série.

---

## La comptabilité — l'épine dorsale de la plupart des rapports

La plupart des rapports de PME se résolvent dans la comptabilité générale. Le
système connecté — MYOB, NetSuite, QuickBooks, Xero ou Zoho Books — fait foi ; tous
sont équivalents (`../../../shared/connector-neutrality.md`). Les familles
d'indicateurs ci-dessous sont écrites avec les noms de rapports QuickBooks ; les
sections NetSuite, Xero, MYOB et Zoho Books indiquent d'où vient chaque famille chez
eux. Les montants portent le code devise de l'entreprise
(`../../../shared/currency-and-locale.md`).

### QuickBooks

| Famille d'indicateurs | Origine |
|---|---|
| Chiffre d'affaires, charges, résultat net | Compte de résultat — depuis les lignes ou `monthlyBreakdown`, jamais le `totalExpenses` / `grossProfit` / `grossProfitMargin` du résumé, qui renvoient 0 / 100 % face à des lignes réelles (Piège 2) |
| Chiffre d'affaires par établissement ou par classe | Compte de résultat avec ventilation par classe ou par établissement |
| Balance âgée clients | Synthèse de la balance âgée clients, toujours contrainte — voir ci-dessous |
| Balance âgée fournisseurs | Balance âgée fournisseurs **détaillée** (`qbo_accounting_get_ap_aging_detail`), contrainte par `vendor_name` ou `due_before` ; construis les tranches toi-même. Jamais la synthèse : elle net les avoirs fournisseurs dans les tranches et affiche des totaux d'impayés négatifs (un défaut de cet outil, `../../../shared/quickbooks-report-traps.md`, Piège 6) |
| Position de trésorerie | Bilan |
| Ventes par client | Synthèse des ventes par client, lignes de regroupement filtrées — voir ci-dessous |
| Ventes par produit | Synthèse des ventes par produit |
| Charge de personnel | Lignes « paie » du compte de résultat |

**Repli :** si QuickBooks renvoie un résultat vide, un état de synchronisation en
cours ou une erreur d'authentification, marque les indicateurs concernés « non
disponible — QuickBooks indisponible » et continue avec les autres sources. Ne
réessaie pas en boucle et ne demande pas au dirigeant de reconnecter en plein
rapport.

### Les balances âgées doivent être contraintes, à chaque fois

Un appel de balance âgée sans contrainte échoue sur toute vraie comptabilité. Sur
un jeu de comptes de taille moyenne, la synthèse de la balance âgée clients renvoie
bien plus de cent mille caractères, dépasse la limite de sortie de l'outil, et
revient inexploitable. Ce n'est pas un cas limite ; c'est le résultat normal pour une
entreprise de quelques centaines de clients.

Passe toujours des arguments de restriction. Les trois qui comptent :

- un plafond top-N, pour que seuls les plus gros soldes remontent
- un seuil minimal de jours de retard, qui fait disparaître entièrement la tranche courante
- un seuil minimal en euros, qui fait disparaître la longue traîne de petits soldes

Pour un rapport, « les vingt plus gros soldes avec au moins un jour de retard » est
la forme utile, et elle tient toujours. Si le dirigeant a vraiment besoin de chaque
ligne, extrais le rapport détaillé par client plutôt que de demander le grand livre
entier d'un coup.

La même règle vaut pour la balance âgée fournisseurs, qui vient du rapport détaillé :
restreins-la par fournisseur ou par date d'échéance. C'est le plus petit des deux
rapports, mais il grossit de la même façon.

### Les ventes par client comptent deux fois les clients parents

La synthèse des ventes par client renvoie deux lignes pour tout client qui a des
sous-clients ou des chantiers en dessous : une ligne de synthèse pour le parent, et
une ligne de total distincte pour ce même parent. Elles portent le même montant. La
liste des meilleurs clients du rapport elle-même contient les deux.

Lue naïvement, elle place un client deux fois dans tes classements — une fois sous
son propre nom, une fois comme « Total pour » ce nom — et gonfle tous les chiffres de
concentration que tu en tires.

Supprime les lignes dont le type de métadonnées les marque comme total avant de
classer, de sommer ou de calculer la concentration. Garde la ligne de synthèse du
parent ; c'est la vraie. Une concentration bâtie sur des lignes non filtrées est
fausse à chaque fois, pas parfois.

---

## HubSpot — entonnoir et clients

| Famille d'indicateurs | Origine |
|---|---|
| Nombre d'affaires par étape | Recherche d'affaires CRM |
| Taux de réussite, durée de cycle | Affaires avec dates de clôture et issues |
| Entonnoir pondéré | Valeur de l'affaire × probabilité de l'étape |
| Nouveaux contacts, sources de leads | Contacts avec date de création et propriété source |
| Performance par responsable | Affaires regroupées par responsable |

**Attention :** les valeurs d'affaires CRM sont des prévisions. Quand un rapport
mélange données CRM et données comptables, le chiffre d'affaires vient toujours de
la comptabilité. Dis de quelle source vient chaque chiffre.

---

## Prestataires de paiement

| Source | Ce qu'elle apporte |
|---|---|
| PayPal | Règlements, frais, litiges, détail des transactions |
| Stripe | Règlements, frais, remboursements, revenu d'abonnement |
| Square | Ventes en présentiel, ventilation par établissement, pourboires |

**Risque de double-compte.** Une commande Shopify réglée via Stripe apparaît dans
les deux. Choisis un seul système comme source de revenu par rapport, indique le
choix dans la synthèse, et utilise l'autre uniquement pour les frais et le calendrier
de règlement.

---

## Shopify

Commandes, chiffre d'affaires par référence, performance par variante, statut
d'expédition, remboursements. Meilleure source pour tout ce qui est regroupé par
produit.

Le coût des ventes n'est généralement pas dans Shopify. Les indicateurs de marge ont
besoin de QuickBooks ou d'un fichier de coûts téléversé.

---

## NetSuite

Courant dans le haut du segment. Mêmes familles d'indicateurs que la section
QuickBooks via `ns_runReport` et `ns_runCustomSuiteQL`, plus le coût des ventes par
article et la valorisation des stocks.

---

## Xero

Mêmes familles d'indicateurs que la section QuickBooks, via `get_profit_and_loss`
(chiffre d'affaires, charges, résultat net, par période), `get_aged_receivables`
(balance âgée clients, mêmes règles de contrainte) et `get_bills` (fournisseurs). La
fiche organisation fournit la devise de base et l'exercice comptable : les
références de période se résolvent donc sur la clôture de l'exercice de l'entreprise.

---

## Ramp et Expensify

Dépenses par carte, catégories de frais, justificatifs, remboursements. Utiles pour
les rapports côté charges et pour repérer les dépenses qui ne sont pas encore
passées en comptabilité.

**Ramp** porte aussi les soldes réels des comptes bancaires et de trésorerie avec
leur historique, plus le détail des factures fournisseurs et une analyse des
dépenses en langage naturel. Ses actions d'écriture — approuver ou rejeter une
facture, marquer une facture comme prête à synchroniser — relèvent d'`ap-processor`,
jamais d'un rapport. Ici, on lit seulement.

**Expensify est une recherche en lecture seule.** Notes de frais, frais individuels,
factures, déplacements, totaux par catégorie et statuts d'approbation. La
justification des dépenses est un filtre de premier ordre : « les frais de plus de
75 € sans justificatif joint » est une vraie requête et un rapport vraiment utile.

**Les remboursements apparaissent dans les deux.** Ramp et Expensify se recouvrent
ici. Choisis-en un comme source des remboursements pour chaque rapport, dis lequel,
et utilise l'autre pour le détail qu'il détient seul — la même règle que pour les
prestataires de paiement.

---

## MYOB

La comptabilité des entreprises sous MYOB. **Lecture seule.** Même compte de résultat
et mêmes créances que QuickBooks, avec trois limites dures qu'il vaut mieux énoncer
dans le rapport que découvrir en cours d'exécution.

| Famille d'indicateurs | Origine |
|---|---|
| Chiffre d'affaires, charges, résultat net | Compte de résultat, avec ventilation mensuelle ou trimestrielle et comparaison à l'exercice précédent |
| Balance âgée clients par client | Soldes clients ouverts, avec indicateurs de risque |
| Dettes fournisseurs | Dettes fournisseurs ouvertes |
| Totaux des ventes | Totaux des factures de vente |
| Conditions de paiement | Conditions de paiement standard |

- **Aucun solde bancaire ni de caisse.** MYOB donne les créances et les dettes,
  jamais la trésorerie disponible. Un indicateur de position de trésorerie tiré de
  MYOB est non disponible — dis-le plutôt que de remplacer par les créances.
- **Aucun détail de contact client.** Noms et soldes seulement.
- **Trois exercices comptables.** Le reporting couvre l'exercice courant et les deux
  précédents. Une comparaison sur quatre ans est non disponible ; dis-le plutôt que de
  renvoyer une série courte qui a l'air complète.
- Toute référence de période — « le trimestre dernier », « depuis le début de
  l'exercice » — désigne *l'exercice comptable de l'entreprise* sauf si le dirigeant
  parle de l'année civile. Résous les dates de l'exercice une fois et réutilise-les
  sur tout le run.

---

## Zoho Books

La comptabilité des entreprises sous Zoho. Lectures au niveau des documents, aucun
point d'accès de rapport — les familles d'indicateurs sont assemblées à partir de
listes, et le rapport le dit.

| Famille d'indicateurs | Origine |
|---|---|
| Chiffre d'affaires (facturé) | `list_invoices` sur une plage de dates avec `response_option=3` pour le total sommé ; par client via `customer_id`, par article via `item_id` |
| Charges | `list_expenses` sur une plage de dates, regroupées sur `account_name` ou `vendor_name` |
| Balance âgée clients | `list_invoices` avec `status=overdue`, réparties sur `due_date` ; `list_contacts` avec `filter_by=Invoice.OverDue` pour l'`outstanding_receivable_amount` par client |
| Dettes fournisseurs (engagements ouverts) | `list_purchase_orders` ouvertes, plus `list_expenses` avec `status=unbilled` |
| Position de trésorerie | `list_bank_accounts` — `current_balance` par compte actif |
| Ventes par client / par produit | `list_invoices` regroupées par `customer_name` ou par `item_name` de ligne ; `list_sales_orders` pour les commandes pas encore facturées |
| Charge de personnel | Non disponible — pas de compte de résultat. Prends-la au connecteur de paie (`month-end-prep` étape 5a) ou dans un export |

- **Aucun point d'accès compte de résultat, tableau de flux de trésorerie ou balance
  âgée.** Le « résultat net » est le chiffre d'affaires facturé moins les charges
  enregistrées, étiqueté comme tel ; un vrai compte de résultat vient de l'export
  Reports.
- **Aucun objet facture fournisseur ni paiement fournisseur.** Les dettes fournisseurs
  se limitent aux commandes d'achat et aux dépenses.
- **Aucun flux de transactions bancaires.** Soldes uniquement, avec un compte
  d'`uncategorized_transactions` par compte.
- La fiche organisation (`get_organization`) fournit `country_code`, `currency_code`
  et `fiscal_year_start_month`, donc les références de période se résolvent sur la
  clôture de l'exercice de l'entreprise.

---

## La voie du fichier téléversé

**C'est un mode à part entière, pas un mode dégradé.** Une large part des dirigeants
cumulent les outils sans connecteur propre.

Quand aucun connecteur ne couvre un indicateur :

1. Dis clairement ce qu'il te faut : « Exporte ton rapport de ventes sur la période et
   dépose-le ici. »
2. Accepte CSV ou XLSX. Lis la ligne d'en-tête et mappe les colonnes sur les
   indicateurs de la spec.
3. Si une colonne nécessaire est absente, nomme-la précisément — « il n'y a pas de
   colonne de coût, donc je ne peux pas calculer la marge » — plutôt que de supprimer
   discrètement l'indicateur.
4. Note le mapping des colonnes du fichier dans la spec enregistrée, pour que le
   prochain run puisse le réutiliser.

Un rapport construit à partir d'un fichier est un vrai rapport. Livre le même résumé
dans la conversation et le même classeur.

---

## Règle des extractions parallèles

Chaque appel part en un seul lot. Les rapports touchent couramment quatre ou cinq
systèmes, et des extractions en série transforment un skill de trente secondes en
deux minutes d'attente que les dirigeants ne subiront pas deux fois.

Enregistre les échecs en interne. Les faire remonter dans l'annexe du rapport, jamais
en plein flux.

### reference/gotchas.md
# Pièges

Les modes de défaillance qui produisent un rapport qui a l'air juste et qui est
discrètement faux. Ce sont les plus dangereux : les dirigeants transmettent ces
rapports aux banques, aux conseils d'administration et aux experts-comptables.

---

## Piège : une période partielle comparée à une période complète

**Pourquoi c'est important :** Le 27 juillet, les ventes depuis le début du mois face
au mois complet précédent ressemblent à un effondrement de 20 %. Ce n'en est pas un.
Des décisions d'effectifs ont été prises sur la base de cette erreur.

### Mauvais

```
Ventes — 21 400 €, en baisse de 19 % vs. juin
```

Juin était un mois complet. Juillet s'arrête au 27. La comparaison n'a aucun sens et
le dirigeant la lit comme une crise.

### Bon

```
Ventes — 21 400 € depuis le début du mois au 27 juillet
         (juin au 27 : 19 800 €, en hausse de 8 %)
```

Même donnée, comparaison honnête, conclusion opposée.

---

## Piège : la même vente comptée deux fois

**Pourquoi c'est important :** Une commande Shopify réglée via Stripe et enregistrée
dans QuickBooks existe dans trois systèmes. Additionner les sources connectées gonfle
le chiffre d'affaires, parfois de deux fois.

### Mauvais

```
Prendre le chiffre d'affaires dans QuickBooks + Shopify + Stripe, additionner les trois.
Le rapport affiche 129 000 €. Le chiffre d'affaires réel était de 43 000 €.
```

### Bon

```
Choisir un seul système comme source de revenu. Le dire :

Chiffre d'affaires — 43 000 € (source : QuickBooks ; Shopify et Stripe utilisés
                        uniquement pour l'expédition et le détail des frais)
```

Règle empirique : quand la comptabilité est connectée, c'est elle qui fait foi pour le
revenu. Les prestataires de paiement fournissent les frais et le calendrier de
règlement. Les boutiques en ligne fournissent la répartition par produit.

---

## Piège : un groupe disparaît au lieu d'afficher zéro

**Pourquoi c'est important :** Si Portland n'a rien vendu cette semaine et que la
ligne disparaît, le dirigeant suppose que la donnée est cassée et part enquêter. Un
zéro est une information ; une ligne manquante est du bruit.

### Mauvais

```
Ventes par établissement :
  Salem      18 200 €
  Eugene     19 000 €
```

Portland existait la semaine dernière. Où est-il passé ?

### Bon

```
Ventes par établissement :
  Salem      18 200 €
  Eugene     19 000 €
  Portland   0 €        (aucune vente enregistrée sur la période)
```

---

## Piège : les lignes regroupées ne raccordent pas au total

**Pourquoi c'est important :** Un dirigeant qui additionne tes colonnes et obtient un
autre nombre cesse de faire confiance à tous les rapports que tu produiras ensuite.

### Mauvais

Publier le total et la ventilation sans vérifier qu'ils concordent.

### Bon

Vérifie la somme avant de livrer. Si les deux ne concordent pas vraiment, dis pourquoi :

```
Les ventes par établissement font 41 900 €. Le total des ventes est de 43 200 €.
L'écart de 1 300 € correspond à des factures sans établissement renseigné.
```

Nommer l'écart construit plus de confiance que le cacher.

---

## Piège : réinterroger sur un rapport enregistré

**Pourquoi c'est important :** toute la promesse de ce skill tient dans « décris-le une
fois ». Poser les mêmes cinq questions chaque mois casse cette promesse et le
dirigeant cesse de s'en servir.

### Mauvais

```
Dirigeant : « Lance le rapport du lundi. »
Claude : « Bien sûr — quels indicateurs souhaites-tu, et sur quelle période ? »
```

### Bon

```
Dirigeant : « Lance le rapport du lundi. »
Claude : [lit saved_reports.md, le retrouve, l'exécute]
         « Pack opérationnel du lundi — semaine du 20 juillet... »
```

Lis toujours `saved_reports.md` en premier.

---

## Piège : un chiffre plausible rempli à la place d'un chiffre manquant

**Pourquoi c'est important :** c'est la défaillance la plus grave du skill. Un rapport
est un document sur lequel les dirigeants agissent et qu'ils transmettent. Un montant
inventé qui paraît raisonnable peut survivre à plusieurs relais avant que quelqu'un le
repère.

### Mauvais

```
Main-d'œuvre — environ 30 % du chiffre d'affaires
```

D'où vient ce chiffre ? De nulle part. Les comptes de paie n'ont pas été renvoyés.

### Bon

```
Main-d'œuvre — non disponible (comptes de paie QuickBooks indisponibles cette fois)
```

N'estime jamais, n'arrondis jamais vers une supposition, ne reconduis jamais
silencieusement le chiffre de la période précédente.

---

## Piège : commencer par le tableau

**Pourquoi c'est important :** les dirigeants ont demandé un rapport parce qu'ils
veulent prendre une décision. Un mur de chiffres leur renvoie l'analyse, qui est
exactement le travail qu'ils voulaient confier.

### Mauvais

Commence par un tableau de 40 lignes, puis un résumé en dessous.

### Bon

Commence par la phrase qui compte, trois indicateurs clés, trois constats. Tout le
reste va dans le classeur.

### reference/output_template.md
# Gabarit de sortie

Deux livrables à chaque run : un résumé dans la conversation, puis un classeur XLSX.
Le résumé est le produit. Le classeur est l'annexe.

---

## Le résumé dans la conversation

```
## <Nom du rapport> — <période>

<Une phrase : la chose la plus importante que dit ce rapport.>

**<Indicateur 1>** — <valeur>, <écart par rapport à la comparaison>
**<Indicateur 2>** — <valeur>, <écart par rapport à la comparaison>
**<Indicateur 3>** — <valeur>, <écart par rapport à la comparaison>

### Ce qui saute aux yeux

- <Constat, en citant l'enregistrement ou le groupe précis et le montant>
- <Constat>
- <Constat>

### À surveiller

- <Tout ce qui demande une décision, avec la suite proposée>

<Classeur joint. Onglets : synthèse, un par groupe d'indicateurs, données brutes.>
```

Trois constats au maximum. Un résumé de neuf puces est un tableau avec des étapes en
plus.

---

## Exemple complet

```
## Pack opérationnel du lundi — semaine du 20 juillet

Portland est le seul établissement sous son niveau de l'an dernier, et c'est lui qui
bloque le chiffre d'affaires total.

**Chiffre d'affaires** — 43 200 €, en hausse de 2 % vs. la même semaine l'an dernier
**Créances de plus de 30 jours** — 18 400 € sur 6 factures
**Main-d'œuvre** — 31 % du chiffre d'affaires, contre 28 %

### Ce qui saute aux yeux

- Portland a réalisé 6 100 €, en baisse de 22 % sur un an. Tous les autres établissements progressent.
- La main-d'œuvre a franchi le cap des 30 % pour la première fois depuis neuf semaines, portée par les heures supplémentaires à Salem.
- Acme Corp doit 4 200 €, avec 47 jours de retard, sans aucun règlement depuis le 12 mai.

### À surveiller

- La chute de Portland dure maintenant quatre semaines d'affilée, ce n'est plus un simple creux d'une semaine. Il faut regarder
  les effectifs ou la concurrence locale avant que ça devienne l'histoire du trimestre.

Classeur joint. Onglets : synthèse, ventes par établissement, balance âgée clients, détail main-d'œuvre, données brutes.
```

Remarque ce que fait le résumé : il nomme l'établissement, donne le montant, précise
la durée de la tendance et propose une suite. « Les ventes ont été mitigées » n'aurait
rien dit.

---

## Le classeur XLSX

L'ordre des onglets compte — les dirigeants ouvrent le premier onglet et s'y arrêtent
souvent.

1. **Synthèse** — les mêmes indicateurs que le résumé, sous forme de tableau propre avec comparaisons
2. **Un onglet par groupe d'indicateurs** — ventes par établissement, balance âgée clients, détail main-d'œuvre
3. **Données brutes** — tout ce qui a été extrait, non modifié, pour que le dirigeant ou son comptable puisse vérifier les calculs

Les règles de mise en forme qui rendent un classeur exploitable :

- Ligne d'en-tête en gras et figée
- Montants formatés en montants, pourcentages en pourcentages — pas de décimales brutes
- Écarts dans leur propre colonne, pas tassés dans la cellule de valeur
- Nombres négatifs entre parenthèses ou en rouge, de façon cohérente
- Une ligne de pied d'onglet sur chaque onglet, nommant la source et l'horodatage de l'extraction

Construis le classeur avec un script plutôt qu'en assemblant les cellules à la main.
C'est plus rapide, et le mois prochain il se régénère à l'identique.

---

## Quand des données manquent

Ne supprime jamais un indicateur en silence. Une ligne manquante se lit comme un
problème de données que le dirigeant partira chercher.

```
**Main-d'œuvre** — non disponible (comptes de paie QuickBooks indisponibles cette fois)
```

Puis récapitule une seule fois chaque source indisponible, en bas :

```
Non disponibles cette fois : comptes de paie QuickBooks, Square (authentification expirée).
Tout le reste a été extrait sans problème.
```

---

## Périodes partielles

Un chiffre depuis le début du mois comparé au mois complet précédent ressemble
toujours à un effondrement. Compare des périodes homogènes, ou étiquette :

```
**Chiffre d'affaires** — 21 400 € depuis le début du mois au 27 juillet (mois précédent au 27 : 19 800 €, en hausse de 8 %)
```

Ne montre jamais une période partielle face à une période complète sans le dire. Cette
seule erreur a envoyé des dirigeants dans la panique pour un chiffre qui allait très
bien.

### reference/report_spec.md
# Format de spec de rapport

Chaque rapport se résout dans cette structure avant toute extraction de données.
C'est la spec qui est enregistrée, et c'est elle qui rend un rapport reproductible.

---

## Le format

```
Nom du rapport :  <court, reconnaissable par le dirigeant>
Cadence :         unique | hebdomadaire | mensuelle | trimestrielle
Période :         <la fenêtre que couvre chaque run>
Comparaison :     <période précédente | même période l'an dernier | objectif | aucune>
Découpage :       <dimension, ou aucun>

Indicateurs :
  <nom>  =  <formule>  [source]
  <nom>  =  <formule>  [source]

Sources :         <connecteurs utilisés, ou « fichier téléversé »>
Notes :           <tout ce que le dirigeant a précisé>
```

---

## Exemple complet 1 — le classique

**Le dirigeant a dit :** « Chaque lundi : ventes par établissement vs. l'an dernier,
balance âgée clients, part de main-d'œuvre. »

```
Nom du rapport :  Pack opérationnel du lundi
Cadence :         hebdomadaire, lundi
Période :         7 derniers jours glissants
Comparaison :     les 7 mêmes jours de l'an dernier
Découpage :       établissement

Indicateurs :
  Chiffre d'affaires =  somme des totaux de factures, hors taxe   [QuickBooks]
  Balance âgée       =  factures ouvertes réparties 0-30 / 31-60 / 61+ jours de retard   [QuickBooks]
  Part main-d'œuvre  =  charge de personnel / chiffre d'affaires net  [QuickBooks]

Sources :         QuickBooks
Notes :           Main-d'œuvre mesurée sur le chiffre d'affaires, pas sur le total des
                  charges (confirmé).
                  La balance âgée clients est à l'échelle de l'entreprise, pas ventilée
                  par établissement.
```

Remarque ce qui a été déduit et ce qui a été demandé. L'indicateur, le découpage et la
comparaison sortent directement de la phrase. Seuls le dénominateur de la main-d'œuvre
et le regroupement de la balance âgée ont demandé une question.

---

## Exemple complet 2 — sans connecteur

**Le dirigeant a dit :** « Il me faut un rapport mensuel qui montre quels produits
rapportent le plus. »

```
Nom du rapport :  Rentabilité mensuelle des produits
Cadence :         mensuelle, premier jour ouvré
Période :         mois civil précédent
Comparaison :     mois précédent
Découpage :       produit

Indicateurs :
  Chiffre d'affaires =  somme des totaux de ligne par SKU        [CSV des ventes téléversé]
  Quantités vendues  =  somme des quantités par SKU             [CSV des ventes téléversé]
  Marge brute        =  (chiffre d'affaires - coût des ventes) / chiffre d'affaires  [CSV des ventes téléversé]

Sources :         fichier téléversé — export mensuel des ventes
Notes :           La colonne de coût des ventes doit être présente dans l'export. Si elle
                  est absente, ne rapporter que le chiffre d'affaires et les quantités,
                  et dire que la marge est non disponible.
```

La voie sans connecteur produit exactement la même forme de spec. Rien n'est dégradé
dans le rapport, sauf là où la donnée elle-même manque.

---

## Exemple complet 3 — entonnoir, multi-source

**Le dirigeant a dit :** « Montre-moi chaque mois comment l'entonnoir convertit et ce
qu'il vaut vraiment. »

```
Nom du rapport :  Conversion mensuelle de l'entonnoir
Cadence :         mensuelle
Période :         mois civil précédent
Comparaison :     mois précédent
Découpage :       étape de l'affaire

Indicateurs :
  Affaires créées     =  nombre d'affaires créées sur la période           [HubSpot]
  Affaires gagnées    =  nombre d'affaires conclues gagnées sur la période   [HubSpot]
  Taux de réussite    =  affaires gagnées / affaires résolues               [HubSpot]
  Entonnoir pondéré   =  somme de (valeur de l'affaire x probabilité d'étape) [HubSpot]
  CA encaissé         =  factures réglées sur la période                    [QuickBooks]

Sources :         HubSpot, QuickBooks
Notes :           Le chiffre d'affaires encaissé vient volontairement de la comptabilité,
                  pas du CRM.
                  Les valeurs d'affaires CRM sont des prévisions ; les factures sont des
                  faits.
```

---

## Les règles qui gardent les specs honnêtes

**Chaque indicateur nomme sa source.** Un indicateur sans source est un indicateur que
personne ne pourra reproduire le mois prochain.

**Les formules sont écrites, pas sous-entendues.** « Part main-d'œuvre » ne veut rien
dire seul. « Charge de personnel divisée par le chiffre d'affaires net » se vérifie.

**Les ambiguïtés sont notées dans Notes, pas résolues en silence.** Quand le dirigeant
clarifie quelque chose, écris ce qu'il a dit. Six mois plus tard, cette note est le
seul enregistrement de la raison pour laquelle le chiffre est calculé ainsi.

**Un rapport, un objectif.** Si un dirigeant décrit huit indicateurs sans lien, c'est
probablement deux rapports. Propose le découpage plutôt que de construire un lot
illisible.

### reference/saved_reports.md
# Rapports enregistrés

Les définitions de rapports que le dirigeant a déjà construites. **Lis ce fichier
avant de poser la moindre question** — réinterroger quelqu'un sur un rapport qu'il a
défini le mois dernier est le moyen le plus rapide de donner à ce skill l'air cassé.

Ajoute une nouvelle entrée après chaque étape 7. N'écrase jamais une entrée ; si un
rapport change, ajoute une ligne de révision en dessous avec la date.

**Quand ce fichier ne peut pas être écrit, enregistre la définition à côté du travail
du dirigeant.** Dans un runtime installé, le dossier du skill est souvent en lecture
seule : l'ajout échoue alors. Ne perds pas la définition et ne prétends pas l'avoir
enregistrée. Écris-la dans `report-definitions.md` à la racine du répertoire de
travail, et dis au dirigeant exactement où elle est passée et quoi en faire :

> « Définition enregistrée dans report-definitions.md, dans ce dossier. Garde ce
> fichier avec tes rapports — remets-le dans la conversation la prochaine fois et je
> relance tout ça sans rien te demander. »

Au prochain run, vérifie les deux endroits : ce fichier d'abord, puis
`report-definitions.md` à la racine du répertoire de travail, puis tout ce que le
dirigeant a joint.

---

## Comment rattacher une demande à un rapport enregistré

Les dirigeants utilisent rarement le nom exact du rapport. Rattache par intention :

| Le dirigeant dit | Rattacher à |
|---|---|
| « lance celui de la semaine » | Le seul rapport à cadence hebdomadaire, ou demande lequel s'il y en a plusieurs |
| « comme la dernière fois » | Le rapport lancé le plus récemment |
| « les chiffres du lundi » | Le rapport dont la cadence est le lundi |
| « mon rapport de ventes » | Le rapport dont l'indicateur principal est le chiffre d'affaires |

Si deux rapports ou plus correspondent plausiblement, liste-les par nom et demande
lequel — une question courte, pas un ré-interrogatoire.

Si rien ne correspond, traite-le comme un nouveau rapport et passe à l'étape 2.

---

## Format d'entrée

```
### <Nom du rapport>
Créé le :     <YYYY-MM-DD>
Dernier run : <YYYY-MM-DD>
Cadence :     <unique | hebdomadaire | mensuelle | trimestrielle>

<la spec complète, au format de report_spec.md>

Révisions :
  <YYYY-MM-DD> — <ce qui a changé et pourquoi>
```

---

## Rapports

*Aucun rapport enregistré pour l'instant. Le premier sera ajouté ici après son premier
run.*

---

Demande de l'utilisateur :
Construis mon tableau de bord mensuel.

Réponds en français, de manière complète et actionnable, comme un assistant de direction pour PME.
Écris ta réponse complète dans le fichier /Users/macbook/small/evals/scale/runs/report-builder/with.md (crée-le).
Quand c'est fait, réponds uniquement : OK
