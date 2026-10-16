Tu es un assistant pour dirigeants de PME françaises.
Le skill suivant est à ta disposition — suis-le pour répondre :

### SKILL.md
---
name: cash-flow-snapshot
description: >
  Prévoit la trésorerie à 30, 60 et 90 jours : encaissements attendus,
  décaissements (prélèvements SEPA, salaires, TVA, fournisseurs), et pour
  les profils à stock, les indicateurs DSO / DPO / DIO.
  [EN] 30/60/90-day cash forecast; DSO/DPO/DIO for stock profiles.
---

> Language rule: see `shared/language.md`.

# cash-flow-snapshot

## Sources
- Qonto (MCP officiel) pour les mouvements et prélèvements SEPA planifiés.
- Grand livre (Pennylane) ou CSV receivables + orders + purchase_orders.

## Indicateurs FR (profils à stock)
- DSO = (créances clients / CA TTC) × jours
- DPO = (dettes fournisseurs / achats TTC) × jours
- DIO = (stock moyen / coût des ventes) × jours
- Cycle de conversion = DSO + DIO − DPO

Afficher ces indicateurs uniquement pour Profil = negoce | fabrication | mixte.
Pour Profil = services, DIO n'est pas affiché.

## Règle
Les prélèvements SEPA (Qonto) sont lus depuis les scheduled transactions,
jamais devinés.

## Repli
CSV receivables + orders + purchase_orders.

## Lien cluster Shopify
Cette compétence dialogue avec la boutique en ligne via `shopify-reporting` (hub : `shopify-hub`, doc : [AI Toolkit](../../shared/shopify-ai-toolkit.md)).


### reference/examples/worked-example.md
# Exemple détaillé — cash-flow-snapshot

**Scénario :** petite entreprise de services. QuickBooks + PayPal connectés. Trois
clients actifs, une paie mensuelle, un loyer de bureau.

---

## Données d'entrée (extraites des connecteurs)

**Balance âgée des créances clients (QuickBooks) :**

| Client       | Facture | Montant   | Échéance | Jours d'encours |
|---|---|---|---|---|
| Acme Corp    | INV-112 | 8 400 €   | 10 avril | 12              |
| BlueSky LLC  | INV-108 | 14 200 €  | 22 avril | 0               |
| Crestwood Inc| INV-115 | 6 000 €   | 5 mai    | —               |

**Délai de règlement historique (d'après les règlements PayPal) :**

| Client       | Délai moyen | Écart-type | Paiements à l'historique |
|---|---|---|---|
| Acme Corp    | 18 jours    | 4 jours    | 11                      |
| BlueSky LLC  | 7 jours     | 2 jours    | 8                       |
| Crestwood Inc| 12 jours    | 5 jours    | 6                       |

**Coûts fixes (dettes fournisseurs récurrentes QuickBooks) :**
- Paie : 22 000 € — le 15 avril
- Loyer : 3 200 € — le 1er mai
- Abonnements logiciels : 480 € — le 1er mai

---

## Sortie de l'étape 3 — dates d'encaissement ajustées

| Client       | Montant facture | Date d'encaissement ajustée | Notes                          |
|---|---|---|---|
| Acme Corp    | 8 400 €         | 28 avril                    | Échéance 10 avril + délai moyen 18 j |
| BlueSky LLC  | 14 200 €        | 29 avril                    | Échéance 22 avril + délai moyen 7 j  |
| Crestwood Inc| 6 000 €         | 17 mai                      | Échéance 5 mai + délai moyen 12 j    |

---

## Sortie de l'étape 4 — prévision 30/60/90 jours

Calcul de la borne de confiance :
- Écart-type moyen pondéré : 3,6 jours
- Délai moyen pondéré : 12,7 jours
- band_pct = 3,6 / 12,7 = **28,3 %**

| Fenêtre | Encaissements attendus | Décaissements attendus | Net        | Bas (−28 %) | Haut (+28 %) |
|---|---|---|---|---|---|
| 0–30 j    | 22 600 €      | 22 000 €      | +600 €    | −5 928 €    | +7 128 €     |
| 31–60 j   | 6 000 €       | 3 680 €       | +2 320 €  | +1 670 €    | +2 970 €     |
| 61–90 j   | 0 €           | 0 €           | 0 €       | —           | —            |

---

## Sortie de l'étape 5 — risques signalés

1. **Tension sur la paie :** la paie (22 000 €) tombe le 15 avril. Encaissements sur la
   borne basse jusqu'au 14 avril : 0 € (les deux encaissements clients tombent les
   28–29 avril). Risque de déficit : jusqu'à 22 000 €.
   *Recommandation : confirmer le calendrier d'encaissement avec Acme et BlueSky
   avant le 14 avril.*

2. **Risque payeur tardif :** Acme Corp paie historiquement avec 18 jours de retard.
   Sa facture de 8 400 € (échue le 10 avril) glisse au 28 avril — après la paie.

---

## Sortie de l'étape 6 — résumé dans le fil de discussion

```
Flux de trésorerie — 23 avril → 21 juillet 2026
Sources : QuickBooks, PayPal

              Attendu    Bas        Haut
Net 30 jours : +600 €     −5 928 €   +7 128 €
Net 60 jours : +2 320 €   +1 670 €   +2 970 €
Net 90 jours : 0 €        —          —

⚠ 2 risques signalés :
  • Tension sur la paie : la paie de 22 000 € tombe le 15 avril ; les encaissements
    clients ne rentrent pas avant les 28–29 avril. Risque de déficit sur la borne
    basse : jusqu'à 22 000 €.
  • Payeur tardif : Acme Corp (délai moyen de 18 jours) décale 8 400 € au-delà de
    la date de paie.

Borne de confiance : ±28 % (d'après la variance historique des règlements sur
3 clients).

Cette prévision s'appuie sur les créances clients et les dettes fournisseurs
QuickBooks et sur l'historique de règlement PayPal. Elle ne remplace pas un conseil
comptable — vérifie avec ton expert-comptable avant toute décision de financement.
```

**XLSX :** `cash-flow-snapshot-2026-04-23.xlsx` — onglets Synthèse / Détail / Risques.

### reference/gotchas.md
# Pièges — cash-flow-snapshot

Cas limites connus et modes d'échec des connecteurs.

---

## 1. La balance âgée des créances clients QuickBooks inclut des factures déjà encaissées

**Mauvais :** intégrer des factures totalement payées dans le rapport de balance
âgée gonfle les projections d'encaissements. QuickBooks affiche parfois des factures
à solde nul dans ses exports de balance âgée.

**Bon :** filtre les lignes de créances clients sur `balance_due > 0` avant de
calculer les encaissements. Si le connecteur n'expose pas balance_due, soustrais les
règlements PayPal/Stripe connus du total de la facture avant de l'inclure.

---

## 2. Le délai de règlement PayPal varie selon le type de transaction

**Mauvais :** supposer que tous les encaissements PayPal sont réglés en 1 à 2 jours
ouvrés. PayPal retient les fonds différemment selon les litiges, les nouveaux
vendeurs et les transactions de forte valeur — une hypothèse de règlement uniforme
produit un calendrier d'encaissements trop confiant.

**Bon :** calcule le délai de règlement à partir des paires réelles
`transaction_date` → `completed_date` dans l'historique des transactions PayPal.
Utilise la moyenne et l'écart-type calculés, par client ou par type de transaction.

---

## 3. Les noms de colonnes CSV sont incohérents d'un export comptable à l'autre

**Mauvais :** exiger des noms de colonnes exacts comme « Date », « Amount », « Type ».
Les exports CSV de QuickBooks utilisent « Transaction Date », « Amount », «
Transaction Type ». Wave utilise « Date », « Amount », « Account Type ». Un parsing
rigide échoue silencieusement.

**Bon :** fais un rapprochement approximatif des en-têtes de colonnes (date →
transaction date → txn date ; amount → débit/crédit ; type → catégorie → account
type). Montre la ligne d'en-tête à l'utilisateur et fais confirmer le mapping avant
de calculer — une question vaut mieux qu'une prévision fausse et silencieuse.

---

## 4. Des coûts fixes cachés dans des écritures fournisseurs ponctuelles

**Mauvais :** ne récupérer que les lignes récurrentes étiquetées « recurring » dans
QuickBooks. Beaucoup de petites entreprises n'étiquettent pas leurs coûts fixes de
façon homogène — le loyer peut apparaître chaque mois comme une facture fournisseur
isolée.

**Bon :** cherche les écritures fournisseurs qui apparaissent sur 3 mois consécutifs
ou plus avec le même fournisseur et un montant similaire (± 10 %). Traite-les comme
des coûts fixes récurrents dans la prévision. Montre la liste à l'utilisateur : « je
les traite comme des coûts fixes mensuels — est-ce que ça te paraît juste ? »

---

## 5. La formule de la borne de confiance casse quand le délai moyen de paiement vaut zéro

**Mauvais :** diviser l'écart-type par un délai moyen de 0 (par exemple les clients qui
paient immédiatement, comme sur Square POS) provoque une division par zéro ou une
borne infinie.

**Bon :** si le délai moyen est ≤ 1 jour, fixe band_pct à 5 % (faible variance,
règlement quasi immédiat). Ne tente pas la division.

### reference/v2_sources.md
# Plus de sources

D'autres sources de données alimentent le même modèle de prévision. La logique ne
change pas — elles élargissent ce que le modèle peut voir.

Récupère tout en un seul lot parallèle. Une prévision qui touche cinq systèmes en
série est une prévision que le dirigeant arrête d'attendre.

---

## Grands livres — celui qui est connecté

Les grands livres sont équivalents (`../../../shared/connector-neutrality.md`).
Celui qui est connecté fournit les branches comptables.

| Source | Ce qu'elle fournit |
|---|---|
| MYOB | **Les branches créances clients et dettes fournisseurs uniquement** — lecture seule, pas de soldes bancaires ni de caisse, et les remontées couvrent trois exercices |
| NetSuite | Créances clients, dettes fournisseurs, coûts fixes et solde de trésorerie, via les rapports et SuiteQL |
| QuickBooks | Balance âgée des créances clients ; dettes fournisseurs en deux appels : la ligne « dettes fournisseurs » du bilan pour le total, et `qbo_accounting_get_ap_aging_detail` avec `due_before` positionné sur l'horizon de prévision pour le calendrier des sorties (lignes réparties par date d'échéance, avoirs gardés à part) ; le résumé de la balance âgée fournisseurs net les avoirs et devient négatif, il ne sert donc jamais de source, et un appel de détail sans contrainte déborde (Piège 1). Plus les coûts récurrents et le bilan |
| Xero | Créances clients ventilées, factures fournisseurs, soldes des comptes bancaires et dossier de l'organisation (devise, exercice comptable) |
| Zoho Books | Trésorerie via `list_bank_accounts` (`current_balance`, sommé sur les comptes actifs) ; créances clients via `list_invoices` `status=unpaid` avec la `due_date` de chaque facture (`response_option=1` pour le solde sommé) ; dettes fournisseurs via les `list_purchase_orders` ouvertes plus `list_expenses` `status=unbilled` ; dossier de l'organisation via `get_organization`. **Pas d'objet facture fournisseur ni de rapport de trésorerie :** les coûts fixes récurrents viennent du dirigeant ou des dépenses récurrentes, et la prévision se construit à partir des dates d'échéance des factures et des dates de livraison attendues des commandes, pas d'une projection comptable — dis-le dans la ligne des sources |

**Deux grands livres connectés : lis les deux, totalise sur un seul.** Demande lequel
fait foi, dis-le dans la sortie, et prends tous les totaux (solde d'ouverture, créances
clients, dettes fournisseurs) sur celui-là. Ne lis l'autre que pour les détails qu'il
détient seul. N'additionne jamais le même chiffre sur deux grands livres.

**MYOB est le seul grand livre qui ne peut pas fournir le solde d'ouverture.**
Récupère-lui la balance âgée des créances clients, les dettes fournisseurs, les
totaux de ventes et les conditions de règlement standard, puis demande au dirigeant
le solde bancaire ou prends-le chez un prestataire de paiement. Intituler la prévision
« pas de solde d'ouverture — variation nette uniquement » est le résultat honnête
quand personne ne peut en fournir un.

Depuis le grand livre : balance âgée des créances clients avec dates d'échéance,
dettes fournisseurs avec dates d'échéance, coûts fixes récurrents et solde de
trésorerie.

---

## Shopify — calendrier des encaissements

Pour une entreprise de commerce, c'est souvent le plus gros encaissement à lui seul,
et il n'arrive pas au moment de la commande.

Récupère les commandes, les versements et le calendrier de versement. C'est l'écart
entre la date de commande et la date de versement qui compte — une entreprise avec
40 000 € de commandes cette semaine et un délai de versement de deux jours a une
vision à 30 jours très différente d'une entreprise réglée chaque semaine.

Modélise les dates de versement, pas les dates de commande. Utiliser les dates de
commande produit une prévision optimiste d'exactement le délai de règlement, à chaque
fois.

**Les versements peuvent être illisibles.** Les scopes du connecteur Shopify
excluent Shopify Payments : les lectures de versements échouent alors que les commandes
réussissent. Quand c'est le cas, demande au dirigeant son calendrier de versement
(quotidien, hebdomadaire, le délai en jours) et modélise à partir de là, et dis dans la
ligne Sources que le calendrier vient du dirigeant. N'infère jamais un délai de
règlement à partir des dates de commande ni de la norme d'une autre boutique.

---

## Ramp — la dépense qui n'a pas encore atterri

La raison la plus fréquente pour laquelle une prévision de trésorerie est
discrètement fausse : des dépenses par carte déjà engagées mais pas encore saisies
dans les livres.

Récupère les transactions par carte en cours et les dépenses non soumises. Ajoute-les
comme un décaissement connu même quand elles n'ont pas encore d'écriture comptable.

**Ramp répond aussi à la question du solde d'ouverture.** Il expose les soldes des
comptes professionnels et de trésorerie avec leur historique. Pour un dirigeant qui
banque chez Ramp, cela transforme « qu'y a-t-il dans le compte là, tout de suite »
en une valeur sourcée — et c'est toute la différence entre une réponse sur la paie et
une supposition sur la paie.

Les remboursements récupérés depuis Ramp peuvent aussi vivre dans l'outil de dépenses
du dirigeant (Expensify). Ne les compte qu'une fois.

Dis ce qui a été ajouté et d'où il vient :

```
Les décaissements incluent 4 180 € de dépenses par carte venant de Ramp qui ne
sont pas encore arrivées dans QuickBooks. Sans elles, cette prévision serait
optimiste d'environ 4 000 €.
```

Cette phrase est souvent la ligne la plus utile de toute la sortie.

---

## Ce qui ne change pas

- Les bornes de confiance viennent toujours de la variance historique de paiement de
  chaque client
- Les indicateurs de risque nomment toujours le client concerné, le montant et le
  nombre de jours de retard
- Le chemin CSV reste entièrement pris en charge et produit toujours la même prévision
- N'invente jamais un chiffre. Une source qui n'a rien renvoyé est signalée par son
  nom comme indisponible

---

## Rapporter les sources

Dis toujours ce sur quoi la prévision a été construite. Les dirigeants emportent ces
documents chez leurs prêteurs, et « d'après QuickBooks et les versements Shopify
jusqu'au 27 juil. » est ce qui la rend défendable.

Recense aussi tout ce qui est indisponible :

```
Construit à partir de : QuickBooks (créances clients, dettes fournisseurs, coûts
fixes), Shopify (calendrier de versement), Ramp (dépenses par carte non saisies).
Indisponible ce passage : Stripe — authentification expirée. Tout revenu Stripe est
absent de ces encaissements.
```

La seconde moitié compte plus que la première. Un dirigeant qui sait ce qui manque
peut juger le chiffre. Celui qui l'ignore lui fera une confiance totale.

---

Demande de l'utilisateur :
Cash en banque : 18 400 €. Encaissements attendus : 9 200 € ce mois, 14 600 € le mois prochain. Décaissements : salaires 7 800 €/mois, TVA 2 150 € en septembre, fournisseur 6 300 € dans 30 jours. Où en serai-je dans 90 jours ?

Réponds en français, de manière complète et actionnable, comme un assistant de direction pour PME.
Écris ta réponse complète dans le fichier /Users/macbook/small/evals/scale/runs/cash-flow-snapshot/with.md (crée-le).
Quand c'est fait, réponds uniquement : OK
