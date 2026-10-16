# Clôture de juin — traitement des 3 opérations bancaires non imputées

## 1. Diagnostic : ce qu'il faut savoir avant d'agir

Vous avez 3 opérations bancaires non imputées au moment de la clôture de juin, dont un virement entrant de **3 400 €** qui regroupe **4 paiements de clients distincts**. C'est une situation classique (regroupement de paiements par un client ou un tiers, absence de références sur le libellé). L'objectif : **imputer proprement avant de clôturer**, sans forcer ni bloquer la clôture.

Règle de base : une opération non imputée au moment de la clôture doit soit être réglée, soit être **documentée et provisionnée en compte de transit**, jamais laissée « en l'air » ni comptabilisée par approximation.

## 2. Traiter le virement de 3 400 € regroupant 4 paiements clients

### Étape 1 — Identifier les 4 paiements (J)
1. Rapprocher le virement avec le **relève des créances clients** : vérifier les 4 factures dont l'échéance tombe fin juin.
2. Croiser avec les **confirmations de paiement** envoyées par les clients ou le tiers qui a regroupé les paiements (e-mail, relevé, pièce jointe au virement).
3. Si les références ne sont pas sur le libellé du virement : contacter les clients concernés ou l'intermédiaire pour obtenir la répartition exacte (montant + référence facture pour chacun).

### Étape 2 — Vérifier la cohérence des montants
- Somme des 4 paiements clients identifiés doit être **égale à 3 400 €**.
- Points de vigilance : avoirs déduits, escomptes, arrondis, frais de virement prélevés sur le montant brut. Si la somme ne tombe pas à 3 400 € exacts, identifier l'écart avant d'imputer (ne jamais « arrondir » en silence).

### Étape 3 — Imputer le virement en 4 écritures de rapprochement
Dans votre logiciel comptable, imputer le virement bancaire **une fois** au crédit du compte 512 (Banque), et au débit :
- 4 lignes débit, une par client, pour le montant exact de chaque paiement (avec référence facture).

Exemple de structure de l'écriture :

| Compte | Libellé | Débit | Crédit |
|---|---|---:|---:|
| 512 Banque | Virement réceptionné le 30/06 | | 3 400,00 |
| 411 Client A — FV-2026-0142 |  | 1 200,00 | |
| 411 Client B — FV-2026-0157 |  | 800,00 | |
| 411 Client C — FV-2026-0161 |  | 700,00 | |
| 411 Client D — FV-2026-0168 |  | 700,00 | |

- Les 4 comptes clients sont soldés (ou réduits du montant payé) au 30/06.
- Le rapprochement bancaire du 30/06 est **équilibré** sur cette opération.

### Étape 4 — Si l'identification n'est pas possible avant la clôture
- Ne **bloquez pas** la clôture : immobiliser le virement en **486 Transitoire / opérations en attente** avec un libellé explicite (« Virement 3 400 € du 30/06 — 4 paiements clients à identifier »).
- Joindre le dossier (relevé bancaire + courriers d'échange) au fichier de clôture.
- S'engager par écrit (mail à soi-même / note de suivi) à l'imputer **avant le 10/07**, puis reclasser vers les 4 comptes clients.

## 3. Traiter les 2 autres opérations non imputées

Pour chacune, appliquer la même logique en 4 questions :
1. **Qu'est-ce que c'est ?** (virement sortant, prélèvement, frais bancaires, virement d'un client inconnu…)
2. **Quelle pièce justificative existe-t-elle ?** (ordre de virement, contrat, e-mail)
3. **À quelle écriture comptable doit-elle être rattachée ?** (fournisseur, charge, taxe, capital…)
4. **Si impossible d'ici la clôture** → immobiliser en 486 avec libellé explicite + échéance de résolution (J+10 max).

Cas fréquents à vérifier en priorité :
- **Frais bancaires** (commissions, tenue de compte) → imputer en 627 (frais de banque), ce n'est jamais « anormal ».
- **Prélèvement SEPA d'un fournisseur** sans référence → vérifier la facture correspondante, puis imputer au compte 401.
- **Virement sortant** vers un compte à terme ou un compte séparé → imputer au compte de trésorerie concerné (512, 516, 518…), pas en frais.

## 4. Clôturer proprement

1. **Relève bancaire complète au 30/06** : toutes les opérations du mois sont soit imputées, soit immobilisées en 486 avec traçabilité.
2. **Rapprochement bancaire équilibré** : soldes bancaires comptables = soldes relevés bancaires au 30/06 (à la date de coupure choisie).
3. **Tableau de suivi des non-imputés** : dresser une liste des 3 opérations (montant, nature, action, responsable, date limite). Ce tableau part avec le dossier de clôture.
4. **Vérifier les impacts sur les états** : le BFR (créances clients correctement réduites de 3 400 €), la trésorerie, et le tableau de vieillissement des créances.
5. **Archiver** : relevé bancaire de juin + preuve des 4 paiements clients (références factures) dans le dossier comptable.

## 5. Éviter que ça se reproduisse en juillet

- **Rapprochement bancaire hebdomadaire** (ou en continu si le logiciel le permet) au lieu d'un rattrapage de fin de mois : les non-imputés s'identifient facilement quand ils sont récents.
- **Libellés normalisés** : demander aux clients (ou au tiers regroupant) de toujours inclure le n° de facture dans le libellé du virement — mention à ajouter au pied de vos factures.
- **Compte de transit unique et suivi** : un seul 486, revu à chaque début de mois, jamais laissé s'accumuler.
- **Règle simple** : aucune opération bancaire ne reste non imputée plus de 10 jours ouvrés sans note de suivi datée.

## En résumé — checklist d'action pour aujourd'hui

- [ ] Identifier les 4 clients derrière le virement de 3 400 € (relevé + courriers + appel si besoin)
- [ ] Vérifier que la somme des 4 paiements = 3 400 € exactement
- [ ] Imputer le virement en 4 écritures (crédit 512, débits 411) avec références factures
- [ ] Qualifier et imputer les 2 autres opérations (frais, fournisseurs, transferts internes)
- [ ] Ce qui reste non imputé → 486 + note de suivi avec échéance J+10
- [ ] Équilibrer le rapprochement bancaire au 30/06
- [ ] Dresser le tableau des non-imputés et l'archiver avec la clôture
- [ ] Poser la routine de rapprochement hebdomadaire pour juillet
