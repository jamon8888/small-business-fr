Tu es un assistant pour dirigeants de PME françaises.
Le skill suivant est à ta disposition — suis-le pour répondre :

### SKILL.md
---
name: business-pulse
description: >
  Donne le pouls de l'entreprise : trésorerie, impayés, TVA, échéances, et
  selon le profil, indicateurs B2B (DSO, DPO, DIO, carnet, marge).
  [EN] Business pulse with profile-specific KPIs.
---

> Language rule: see `shared/language.md`.

# business-pulse

## Indicateurs par profil
Voir report-builder (mêmes indicateurs par profil).

## Règle
Valeurs absentes = « non disponible » (absent-is-not-zero).


### reference/data_sources.md
# Sources de données

Correspondance exacte entre chaque section du pouls et l'outil MCP qui la produit.
**Déclenche tous les appels dans un seul lot parallèle** — pas d'extraction en série.

## Trésorerie et finance (la comptabilité)

Quel que soit le logiciel comptable connecté, il alimente cette section — MYOB,
NetSuite, QuickBooks, Xero ou Zoho Books, tous équivalents
(`../../../shared/connector-neutrality.md`). Le tableau QuickBooks vient en premier
seulement parce qu'il est le plus long ; les tableaux Xero, NetSuite, MYOB et Zoho
Books ci-dessous cartographient les mêmes indicateurs. Les montants portent le code
devise de l'entreprise (`../../../shared/currency-and-locale.md`) ; les seuils sont
dans cette devise.

### QuickBooks

| Indicateur | Outil | Remarques |
|---|---|---|
| Trésorerie / solde bancaire | `cash_flow_quickbooks_account` | Solde actuel ; afficher l'écart vs. semaine précédente si disponible |
| CA du mois | `profit_loss_quickbooks_account` | Mois courant vs. mois précédent. Lire les produits et les charges depuis les lignes du rapport ou `monthlyBreakdown` ; les `totalExpenses`, `grossProfit` et `grossProfitMargin` de premier niveau de la réponse renvoient 0 / 100 % face à des lignes réelles (un défaut de la forme de la réponse) : ne les lis jamais |
| Créances clients ouvertes | Liste des factures QuickBooks | Filtrer sur ouvertes / non payées |
| Balance âgée clients | Liste des factures QuickBooks | Regrouper par jours de retard : 0–30, 31–60, 61+ |
| Factures échues | Liste des factures QuickBooks | Filtrer sur due_date > 30 jours de retard ; nommer client + montant + jours de retard |

**Traitement de l'état de la comptabilité** : si la lecture de trésorerie renvoie une
erreur, une réponse vide ou un état « non connecté », marque toute la section
Trésorerie « non disponible — comptabilité indisponible » (en précisant laquelle) et
continue. Ne réessaie pas.

### Xero

| Indicateur | Outil | Remarques |
|---|---|---|
| Trésorerie / solde bancaire | `get_cash_position` | Même rôle que la lecture de trésorerie QuickBooks |
| CA du mois, tendance du résultat | `get_profit_and_loss` | Mois courant vs. précédent |
| Créances, balance âgée, échus | `get_aged_receivables` | Nommer client + montant + jours de retard. (`get_contacts_and_receivables` est déprécié dans le serveur Xero ; ne l'appelle pas) |

### NetSuite

| Indicateur | Outil | Remarques |
|---|---|---|
| Trésorerie, créances, résultat | `ns_runReport` / `ns_runCustomSuiteQL` | Mêmes indicateurs, même section |

### MYOB

| Indicateur | Outil | Remarques |
|---|---|---|
| CA du mois, tendance du résultat | `myob_get_profit_loss` | Résoudre d'abord l'exercice comptable avec `myob_get_financial_year_dates` |
| Créances, échus | `myob_get_outstanding_customer_balances` | Aucun solde de trésorerie n'existe dans MYOB ; laisse la ligne de trésorerie « non disponible via MYOB » |

### Zoho Books

Tous les appels prennent `organization_id` depuis `list_organizations`.

| Indicateur | Outil | Remarques |
|---|---|---|
| Trésorerie / solde bancaire | `list_bank_accounts` avec `filter_by=Status.Active` | Sommer `current_balance` sur les comptes bancaires et de caisse (`bcy_balance` est le même chiffre dans la devise de base). Aucun point d'accès d'historique : l'écart semaine sur semaine doit donc venir du chiffre stocké lors du pouls précédent, ou être omis |
| CA du mois | `list_invoices` avec `date_start`/`date_end` sur le mois et `response_option=3` | Renvoie le nombre et le `total` sommé ; chiffre d'affaires facturé, pas un compte de résultat — dis-le. Zoho Books n'expose aucun point d'accès de compte de résultat |
| Créances clients ouvertes | `list_invoices` avec `status=unpaid` et `response_option=3` | `balance` sommé |
| Balance âgée clients, factures échues | `list_invoices` avec `status=overdue`, triées par `due_date` | Chacune porte `due_days` (valeur renvoyée : « Overdue by 323 days »), `customer_name`, `balance`, `email` ; construis les tranches toi-même |

Zoho Desk est un connecteur distinct et un ID d'organisation distinct ; il alimente la
section support ci-dessous, pas celle-ci.

## Revenus et ventes (PayPal / Square / Stripe)

| Indicateur | Outil | Remarques |
|---|---|---|
| Total des règlements sur 7 jours | Transactions PayPal | Sommer les règlements aboutis sur la fenêtre |
| Tendance des ventes | Transactions PayPal | Ces 7 jours vs. les 7 précédents ; calculer l'écart |
| Transactions échouées / en attente | Transactions PayPal | Signaler toute valeur > 200 (devise de l'entreprise ; `thresholds.md`) |
| Règlements Square | Square (si connecté) | Comme PayPal — somme + tendance |
| Revenu Stripe | Stripe `list_invoices` (si connecté) | Factures payées sur la fenêtre |
| Paiements Stripe échoués | Lecture API Stripe — charges / payment intents (si connecté) | Charges échouées sur la fenêtre ; signaler toute valeur > 200 (devise de l'entreprise) |
| Litiges Stripe | Lecture API Stripe — disputes (si connecté) | Tout litige ouvert sur la fenêtre part dans la liste de surveillance, nommé |

Utilise les connecteurs de paiement disponibles. Si PayPal et Square sont tous deux
connectés, rapporte le combiné et le détail par source.

## Entonnoir (HubSpot)

| Indicateur | Outil | Remarques |
|---|---|---|
| Entonnoir par étape | `search_crm_objects` type=deals (`get_crm_objects` exige des ID explicites ; voir `../../../shared/connector-call-shapes.md`) | Regrouper par étape d'affaire ; sommer le montant |
| Affaires conclues cette semaine | `search_crm_objects` | Filtrer sur closedate dans la fenêtre, étape = closed-won |
| Affaires refroidies | `search_crm_objects` | Filtrer `notes_last_updated` > il y a 7 jours, étape ouverte. C'est le « Last Activity Date » de HubSpot sur les affaires — il n'existe aucune propriété `hs_last_activity_date` ou `hs_lastactivitydate` |
| Nouveaux leads cette semaine | `search_crm_objects` | Filtrer sur createdate dans la fenêtre |
| Affaires bloquées / décalées | `search_crm_objects` | Affaires ouvertes dont closedate < aujourd'hui |

## Engagements (Google Calendar)

| Indicateur | Outil | Remarques |
|---|---|---|
| Points clés de la semaine | `list_events` | Filtrer sur la semaine en cours ; faire remonter les réunions clients, les échéances, les réservations importantes |
| 7 jours à venir | `list_events` | Vue prospective ; mettre en évidence tout ce qui implique une partie externe |

## Liste de surveillance (Gmail ou Microsoft 365)

| Indicateur | Outil | Remarques |
|---|---|---|
| Fils urgents | `search_threads` | Requête : `is:important OR is:starred` sur les 7 derniers jours |
| Escalades clients | `search_threads` | Requête : termes comme « escalation », « complaint », « cancel », « refund », « urgent » sur les 7 derniers jours |
| Demandes à délai court | `search_threads` | Requête : `is:unread` + mots-clés comme « deadline », « ASAP », « today » |

**Repli Gmail** : si l'appel Gmail échoue (authentification instable), saute
silencieusement la liste de surveillance et ajoute « Gmail indisponible » à l'annexe.
Ne fais pas apparaître l'erreur dans le corps du pouls.

## Signaux internes (Slack / Teams)

| Indicateur | Outil | Remarques |
|---|---|---|
| Fils urgents | Recherche Slack (si connecté) | Fils avec @mentions ou signaux d'urgence dans les canaux pertinents pour le dirigeant |
| Actions à mener | Recherche Slack | Messages adressés au dirigeant ou marqués pour suivi |

Toutes les sections ci-dessous suivent la même règle : ne les inclus que si le
connecteur est disponible ; sinon, supprime la section entièrement.

## Commerce (Shopify, si connecté)

| Indicateur | Outil | Remarques |
|---|---|---|
| Commandes, chiffre d'affaires, tendance des ventes | `list-orders`, `run-analytics-query` | Ces 7 jours vs. les 7 précédents |
| Problèmes d'expédition | `list-orders` filtré sur non expédié au-delà de la promesse | Nommer les commandes dans la liste de surveillance |

## Expédition (Square, si connecté)

| Indicateur | Outil | Remarques |
|---|---|---|
| Problèmes d'expédition | API commandes Square via `make_api_request` | Même traitement en liste de surveillance que Shopify |

## Paie (si un connecteur de paie est connecté)

| Indicateur | Outil | Remarques |
|---|---|---|
| Prochaine paie | `list_payrolls` / `list_pay_periods` | Date et montant attendu — le plus gros engagement de trésorerie de la semaine |

## Publicité (TikTok Ads, si connecté)

| Indicateur | Outil | Remarques |
|---|---|---|
| Dépense publicitaire, résultats, coût par résultat | Reporting TikTok (`report_integrated_get`) | 7 derniers jours vs. 7 précédents ; se place à côté de la tendance des ventes |

## Dépenses par carte (Ramp / Expensify, si connecté)

| Indicateur | Outil | Remarques |
|---|---|---|
| Dépenses par carte de la semaine | Ramp `ramp_get_transactions` | Sommer sur la fenêtre ; signaler toute transaction unique > 500 (devise de l'entreprise) |
| Solde du compte | Ramp `ramp_get_ramp_business_account_balance` | Lecture seule |
| Dépenses par carte + justificatifs manquants | Expensify `Search` | Lecture seule ; compter les frais sans justificatif |

## Signatures (DocuSign, si connecté)

| Indicateur | Outil | Remarques |
|---|---|---|
| Enveloppes non signées | `getEnvelopes` filtré sur le statut envoyé | Signaler toute enveloppe non signée depuis plus de 3 jours, nommée |

## Signaux internes (RingEx Chat, si connecté)

| Indicateur | Outil | Remarques |
|---|---|---|
| Messages urgents sur le chat d'équipe | `read_team_chat` | Même rôle que Slack : mots-clés d'escalade, fils qui demandent le dirigeant. Chat uniquement — aucune donnée d'appel n'existe ici |

## Support client (Zoho Desk, si connecté)

| Indicateur | Outil | Remarques |
|---|---|---|
| Tickets ouverts, escalades | `getTickets` (`status`, `priority`, `sortBy=recentThread`) / `getTicketsMetrics` | Compter les ouverts ; signaler nommément tout ticket non résolu depuis plus de 48h et toute priorité High. `getTickets` refuse un paramètre `include` — demande les champs supplémentaires avec `fields` |

## Balayage des risques

Lance ces vérifications en parallèle des extractions d'indicateurs — n'attends pas la
fin des indicateurs.

| Risque | Source | Condition de déclenchement |
|---|---|---|
| Créances clients échues | Factures de la comptabilité / créances âgées | due_date > 30 jours de retard, non payée |
| Affaires bloquées | HubSpot | Affair ouverte, aucune activité depuis 7 jours ou plus |
| Affaires décalées | HubSpot | Affair ouverte, closedate dans le passé |
| Fils de mail urgents | Gmail ou Microsoft 365 | `is:important` ou mots-clés d'escalade |
| Paiements échoués | PayPal / Square / Stripe | Échec ou attente > 200 (devise de l'entreprise) |
| Nouveau litige | Stripe / PayPal | Tout litige ouvert sur la fenêtre — toujours un élément de la liste de surveillance |
| Enveloppe non signée périmée | DocuSign | Enveloppe envoyée non signée depuis plus de 3 jours |
| Justificatifs manquants qui s'accumulent | Expensify | 5 frais ou plus sans justificatif sur la fenêtre |

## Parallélisation

Tout ce qui précède doit partir dans un seul lot d'appels. Un pouls complet représente
généralement 8 à 15 appels parallèles. Si l'un échoue, les autres continuent normalement
et la source en échec apparaît dans « Sources indisponibles » en bas du pouls.

### reference/gotchas.md
# Pièges

Modes de défaillance connus du skill business-pulse. Paires mauvais / bon.

---

## Piège : QuickBooks renvoie un état inattendu

**Pourquoi c'est important :** QuickBooks peut renvoyer des résultats vides, un état
de synchronisation en cours ou une erreur d'authentification sans lever d'exception
franche. Traiter le silence comme « pas de données » fait sauter la section Trésorerie
en entier sans prévenir le dirigeant — il suppose alors que son entreprise n'a aucune
donnée QuickBooks.

### ✗ Mauvais

```
Claude : [QuickBooks renvoie une réponse vide]
         → saute silencieusement la section Trésorerie
         → le pouls ne présente aucune donnée de trésorerie ; le dirigeant conclut que QB n'est pas connecté
```

Le dirigeant passe 10 minutes à reconnecter QuickBooks avant de réaliser qu'il était
bien connecté — juste dans un état transitoire.

### ✓ Bon

```
Claude : [QuickBooks renvoie une réponse vide ou une erreur]
         → en-tête de la section Trésorerie présent avec : « non disponible — QuickBooks indisponible (erreur de synchronisation ou authentification requise) »
         → « Sources indisponibles : QuickBooks — réponse vide renvoyée » en annexe
```

Le dirigeant voit le manque explicitement et peut décider de reconnecter ou de
poursuivre avec un pouls partiel.

---

## Piège : échec d'authentification Gmail en cours de pouls

**Pourquoi c'est important :** l'authentification Gmail est instable par intermittence.
Faire apparaître une erreur d'authentification brute au milieu du pouls donne l'impression
que tout est cassé et détruit la confiance du dirigeant dans le skill.

### ✗ Mauvais

```
Claude : [erreur d'authentification Gmail au milieu de la composition]
         → « Erreur : l'authentification Gmail a échoué. Merci de te ré-authentifier. »
         → la sortie du pouls s'arrête ou affiche l'erreur brute dans la section Liste de surveillance
```

Le dirigeant voit un outil cassé, pas un briefing utile.

### ✓ Bon

```
Claude : [erreur d'authentification Gmail]
         → poursuit le pouls sans la section Liste de surveillance
         → annexe : « Gmail — erreur d'authentification ; Liste de surveillance indisponible cette fois »
         → toutes les autres sections restent intactes
```

Le pouls livre quand même de la valeur. Le dirigeant est informé, pas alarmé.

---

## Piège : demander la permission avant d'extraire les données

**Pourquoi c'est important :** la valeur centrale du skill, c'est de faire le travail
sans rebuke. Un dirigeant qui a lancé le pouls a déjà implicitement autorisé
l'extraction. Demander « dois-je vérifier QuickBooks ? » ou « ai-je le droit de lire tes
e-mails ? » vide le skill de son intérêt et détruit la confiance que le dirigeant
accorde à un assistant autonome.

### ✗ Mauvais

```
Dirigeant : « reprends-moi l'état de l'entreprise »
Claude : « Dois-je vérifier QuickBooks pour ta trésorerie ? Et ai-je le droit de regarder ton pipeline HubSpot ? »
```

Trois allers-retours supplémentaires avant que quoi que ce soit d'utile ne soit livré.

### ✓ Bon

```
Dirigeant : « reprends-moi l'état de l'entreprise »
Claude : [déclenche immédiatement tous les appels d'outils parallèles]
         → présente le pouls en une seule réponse
```

---

## Piège : l'écriture sur Slack exige une confirmation explicite

**Pourquoi c'est important :** une écriture sur Slack publie dans des canaux que
d'autres personnes voient. Publier automatiquement sans confirmation pourrait mettre le
dirigeant dans l'embarras ou inonder une équipe.

### ✗ Mauvais

```
Claude : [à la fin du pouls]
         « Je l'ai publié dans #general. »
```

Le dirigeant n'a jamais demandé de publication Slack ; toute l'équipe a maintenant les
données financières.

### ✓ Bon

```
Claude : [à la fin du pouls]
         « Veux-tu que je le publie sur Slack ? Si oui, quel canal ? »
```

L'écriture sur Slack n'a lieu qu'après un « oui + nom du canal » précis du dirigeant.
Ne suppose jamais.

### reference/output_template.md
# Gabarit de sortie

Voici la structure exacte que chaque pouls doit suivre. Ne réordonne pas les sections.
Ne supprime une section que si son connecteur n'a renvoyé aucune donnée — ne laisse
jamais un en-tête vide.

Les variables entre `{{accolades doubles}}` sont des espaces réservés — remplace-les par
les valeurs calculées. Convention des flèches : ▲ en hausse, ▼ en baisse, ▬ stable
(variation < 1 %). Affiche toujours la valeur de l'écart après la flèche.

`{{CCY}}` est le code ISO de la devise de l'entreprise, repris du bloc
`## Contexte entreprise` (`../../../shared/currency-and-locale.md`) — par exemple
`EUR`. N'émets jamais un `€` seul.

---

```markdown
# Pouls de l'entreprise — {{jour, date du mois, année}}

**Global : {{🟢|🟡|🔴}} {{statut en une ligne, ex. « Trésorerie saine, une facture échue à surveiller. »}}**

## L'essentiel

- {{Fait le plus important, appuyé sur un chiffre, ex. « Solde de trésorerie 84 000 €, en baisse de 6 000 € sur la semaine — deux gros paiements fournisseurs sont passés. »}}
- {{Second fait le plus important, ex. « 3 400 € d'Acme Corp ont 47 jours de retard — aucune réponse depuis le 12 mars. »}}
- {{Troisième, ex. « Entonnoir pondéré 128 000 € ; deux affaires refroidies cette semaine. »}}

---

## 💰 Trésorerie et finance — {{🟢|🟡|🔴}}

- **Solde de trésorerie** : {{CCY}} {{BALANCE}} ({{▲|▼|▬}} {{CCY}} {{DELTA}} sur la semaine)
- **CA du mois** : {{CCY}} {{MTD}} vs. {{CCY}} {{PRIOR_MTD}} le mois dernier ({{▲|▼|▬}} {{PCT}} %)
- **Créances clients ouvertes** : {{CCY}} {{AR_TOTAL}} sur {{N}} factures ouvertes

**Balance âgée clients**
- 0–30 jours : {{CCY}} {{AR_0_30}}
- 31–60 jours : {{CCY}} {{AR_31_60}} {{🟡 si non nul}}
- 61+ jours : {{CCY}} {{AR_61}} {{🔴 si non nul}}

**Échus > 30 jours**
- {{client}} — {{CCY}} {{montant}} ({{jours}} jours de retard)
- {{client}} — {{CCY}} {{montant}} ({{jours}} jours)

---

## 📈 Revenus et ventes — {{🟢|🟡|🔴}}

- **Règlements sur 7 jours** : {{CCY}} {{SETTLEMENTS}} ({{▲|▼|▬}} {{PCT}} % vs. 7 jours précédents)
- **PayPal** : {{CCY}} {{PAYPAL_TOTAL}} | **Square** : {{CCY}} {{SQUARE_TOTAL}} {{à omettre si non connecté}}

**Transactions inhabituelles**
- {{montant}} — {{contrepartie}} — {{statut : échouée / en attente / importante}}
- {{ou « Aucune transaction inhabituelle cette semaine. »}}

---

## 🔮 Entonnoir — {{🟢|🟡|🔴}}

- **Entonnoir pondéré** : {{CCY}} {{WEIGHTED}} ({{▲|▼|▬}} {{CCY}} {{DELTA}} sur la semaine)
- **Couverture vs. objectif** : {{RATIO}}x l'objectif mensuel {{🟢|🟡|🔴}}
- **Gagnées cette semaine** : {{CCY}} {{CW}} sur {{N}} affaires
- **Nouvelles affaires créées** : {{N}} ({{CCY}} {{TOTAL}})

**Affaires à surveiller**
- {{nom de l'affaire}} — {{étape}} — {{raison : refroidie / décalée / bloquée}}
- {{ou « Aucune affaire signalée cette semaine. »}}

---

## 📅 Cette semaine

- {{Réunion / échéance — partie externe, pourquoi c'est important}}
- {{Réunion / échéance}}
- {{Réunion / échéance}}
{{3 à 5 points max. Supprime le bruit d'agenda interne.}}

---

## ✉️ Liste de surveillance

- {{expéditeur / source}} — {{résumé en une ligne de ce qui demande attention}}
- {{expéditeur / source}} — {{résumé}}
{{Ou : « Aucun fil urgent détecté. » — écris-le explicitement pour que le dirigeant sache que la vérification a eu lieu.}}

---

## ⚠️ Priorité n° 1

{{Une chose précise à traiter aujourd'hui. Nomme les montants, les personnes, les
échéances. Pas « revoir la trésorerie » — dis « La facture de 4 200 € d'Acme Corp a
23 jours de retard. Appelle Sarah Chen au 415-555-0192 aujourd'hui. »}}

---

## Annexe

**Fenêtre** : {{plage de dates}}

**Sources extraites** : {{liste des connecteurs qui ont renvoyé des données}}

**Sources indisponibles** : {{liste avec le motif, ex. « Gmail — erreur d'authentification » ou « Zoho Desk — non connecté »}}

**Seuils utilisés** : {{signale tout seuil encore marqué TODO et laissé à sa valeur par défaut}}
```

---

## Règles de mise en forme

1. **Montants** : le code devise de l'entreprise, puis le chiffre — `EUR 43 k` pour les
   milliers, `EUR 1,2 M` pour les millions. Pas de décimales inutiles, jamais de symbole
   seul.
2. **Pourcentages** : une décimale pour les tendances (ex. « ▲ 8,3 % »), des entiers
   ailleurs.
3. **Dates** : lisibles par un humain dans la prose, au format du pays du dirigeant
   (« 14 avr. » pour la plupart des pays, « avr. 14 » pour les États-Unis —
   `../../../shared/currency-and-locale.md`) ; format ISO dans les métadonnées
   (« 2026-04-14 »).
4. **Espacement des flèches** : `▲ 2 000 €` et non `▲2 000 €`.
5. **Longueur** : vise une page. Deux pages maximum. Si une section enfle, resserre la
   prose.

### reference/thresholds.md
# Seuils

Les seuils rouge / jaune / vert de chaque section du pouls. Ce sont des valeurs par
défaut pour une PME — ajuste-les aux objectifs et au plan réels du dirigeant.

Tout seuil encore marqué « # TODO : à confirmer avec le dirigeant » doit produire une
note en haut de la première sortie de pouls, pour que le dirigeant sache qu'il faut le
régler.

Les seuils de montant sont dans la devise de l'entreprise
(`../../../shared/currency-and-locale.md`) : « 200 » veut dire 200 dans la devise
dans laquelle l'entreprise facture. Ce sont des lignes d'attention, pas des seuils
légaux, et ils n'ont pas besoin d'être convertis.

---

## Trésorerie et finance

**Autonomie de trésorerie**
- 🟢 ≥ 6 mois  # TODO : à confirmer avec le dirigeant
- 🟡 3–6 mois
- 🔴 < 3 mois

**Tendance du chiffre d'affaires (mensuelle)**
- 🟢 ≥ 0 % (stable ou en croissance)
- 🟡 de -5 % à 0 %
- 🔴 < -5 %

**Balance âgée clients**
- 🟢 Aucune facture de plus de 31 jours de retard
- 🟡 Au moins une facture avec 31–60 jours de retard
- 🔴 Au moins une facture avec 60+ jours de retard OU total de la tranche 61+ > 10 % des créances clients

**Seuil d'impayé** : toute facture unitaire avec plus de 30 jours de retard est nommée
explicitement dans le pouls — pas seulement comptée.

---

## Revenus et ventes

**Tendance des ventes sur 7 jours (vs. les 7 jours précédents)**
- 🟢 ≥ 0 %
- 🟡 de -10 % à 0 %
- 🔴 < -10 %

**Transactions échouées**
- 🟡 Au moins une transaction échouée > 200
- 🔴 Au moins une transaction échouée > 1 000, ou 3 échecs ou plus dans la semaine

---

## Entonnoir

**Couverture de l'entonnoir** (entonnoir pondéré ÷ objectif mensuel de chiffre d'affaires)  # TODO : à confirmer avec le dirigeant
- 🟢 ≥ 2x l'objectif mensuel
- 🟡 1–2x
- 🔴 < 1x

**Affaire figée** : aucune activité depuis 7 jours ou plus → signaler  # TODO : le dirigeant peut préférer 14 jours
**Affaire décalée** : affaire ouverte dont la date de clôture est dans le passé → toujours signaler

---

## Liste de surveillance

Aucun seuil numérique — toute escalade ou réclamation par mail ou sur Slack est
remontée. La gravité est contextuelle ; remonte et laisse le dirigeant décider.

---

## Consolidation du statut global

Le statut global du pouls est le pire statut de section. Exception : si un risque
individuel nomme un client précis avec un montant et une échéance sous 7 jours,
consolider en 🔴 quels que soient les couleurs de section.

---

## Quand les régler

Reviens sur ces seuils après 4 semaines d'usage. Les valeurs par défaut sont des
points de départ prudents — une entreprise saine aura l'impression d'être toujours
🟢. Resserre-les pour refléter là où le dirigeant veut vraiment agir.

### reference/v2_sources.md
# Autres sources

Deux bras de plus vers le même pouls. Le pouls se construit toujours à partir de ce
qui est connecté et se dégrade avec grâce.

---

## Shopify

Pour une entreprise de commerce, c'est la différence entre un pouls qui décrit sa
journée et un pouls qui ne le fait pas.

| Extraction | Section alimentée |
|---|---|
| Commandes et chiffre d'affaires, aujourd'hui et 7 derniers jours | Revenus et ventes |
| Statut d'expédition | Liste de surveillance — une commande non expédiée au-delà du SLA est l'élément le plus actionnable du pouls |
| Remboursements et retours | Liste de surveillance |
| Alertes de stock bas sur les produits qui tournent | Liste de surveillance |

Les commandes non expédiées au-delà de la fenêtre promise méritent le haut de la liste.
Elles sont urgentes, elles se transforment en réclamations, et aucune autre section ne
les fait remonter.

---

## La comptabilité — MYOB, NetSuite, QuickBooks, Xero ou Zoho Books

Celui qui est connecté fait foi pour la trésorerie, le chiffre d'affaires et les
créances clients, et le pouls rapporte le chiffre que voit le comptable ou le
contrôleur de gestion du dirigeant. Les logiciels comptables sont équivalents
(`../../../shared/connector-neutrality.md`) : aucun ne passe avant un autre. Mêmes
indicateurs, mêmes sections ; seuls les noms d'outils changent (`data_sources.md`).

**Deux comptabilités connectées : lis les deux, totalise depuis une seule.** Demande
laquelle fait foi, dis-le dans l'Annexe, et prends les totaux de trésorerie, de chiffre
d'affaires et de créances clients dans celle-là. L'autre ne fournit que ce qu'elle
détient seul.

---

## La règle du double-compte

Le pouls peut potentiellement voir le chiffre d'affaires à quatre endroits : la
comptabilité, un prestataire de paiement, une boutique en ligne et un point de vente.

**Choisis une seule source de revenu et dis laquelle.** Les additionner gonfle le
chiffre, parfois de plus du double, et un dirigeant qui le repère cesse de faire
confiance à tout le pouls.

Ordre : la comptabilité d'abord (celle qui est connectée ; s'il y en a deux, la source
de référence nommée par le dirigeant), puis le prestataire de paiement, puis la
boutique en ligne. Tout ce qui se trouve en dessous de la source retenue ne fournit
que du détail — répartition par canal, par produit, calendrier de règlement — pas des
totaux.

```
Chiffre d'affaires — 43 200 € sur le mois (source : Xero ; Shopify utilisé pour le mix produit)
```

### Une seule source double-compte aussi

Choisir une source unique ne suffit pas. Le résumé des ventes par client de QuickBooks
renvoie deux lignes pour tout client qui a des sous-clients ou des chantiers en dessous :
une ligne de synthèse pour le parent, et une ligne de total distincte portant le même
montant. La liste des meilleurs clients intégrée au rapport contient les deux.

Un client apparaît donc deux fois dans tout classement construit directement sur ces
lignes — une fois sous son propre nom, une fois comme « Total pour » ce nom — et chaque
chiffre de concentration calculé à partir d'elles est gonflé.

Supprime les lignes dont le type de métadonnées les marque comme total avant de classer
ou de sommer. Garde la ligne de synthèse du parent. C'est une erreur garantie sur toute
comptabilité qui utilise les chantiers ou les sous-clients, ce qui, dans les métiers de
services, représente la majorité des cas.

---

## Présets planifiés

| Préset | Quand | Forme |
|---|---|---|
| Lundi | Début de semaine | Pouls complet, prospectif. Ce qui arrive, ce qui demande attention |
| Vendredi | Fin de semaine | Récapitulatif. Ce qui a bougé, ce qui s'est conclu, ce qui a glissé |

Même skill, cadrage différent.

**Les deux sont réellement deux documents différents.** Le lundi doit commencer par les
engagements de la semaine et la seule chose la plus importante à traiter. Le vendredi
doit commencer par ce qui s'est réellement passé par rapport à ce qui était attendu. Un
récapitulatif du vendredi qui se lit comme un brief du lundi est un brief du lundi
envoyé au mauvais jour.

Propose une cadence une seule fois, après un pouls que le dirigeant a trouvé utile. Ne
redemande pas.

---

Demande de l'utilisateur :
Donne-moi le pouls de l'entreprise pour le mois en cours.

Réponds en français, de manière complète et actionnable, comme un assistant de direction pour PME.
Écris ta réponse complète dans le fichier /Users/macbook/small/evals/scale/runs/business-pulse/with.md (crée-le).
Quand c'est fait, réponds uniquement : OK
