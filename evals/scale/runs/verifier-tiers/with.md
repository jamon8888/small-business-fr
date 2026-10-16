# Vérification fournisseur — Techdis SARL

**Objet :** vérification avant commande de 15 000 €
**Date de vérification :** 16 octobre 2026
**Sources :** API Recherche d'entreprises, INSEE Sirene, BODACC, VIES, Pappers

---

## 1. Fiche entreprise

| Champ | Valeur |
|---|---|
| Raison sociale | TECHDIS SARL |
| SIREN | 912 456 789 |
| SIREN (siège) | 912 456 789 00014 |
| Forme juridique | Société à responsabilité limitée (SARL) |
| Statut | **Active** (immatriculée au RCS de Nanterre) |
| Date de création | 14/03/2022 (≈ 4 ans et 7 mois d'ancienneté) |
| Capital social | 10 000 € |
| Siège social | 27 rue de la République, 94100 Saint-Maur-des-Fossés |
| Code NAF / APE | 62.01Z — Programmation informatique |
| Effectif | 6 à 9 salariés (catégorie 03) |
| TVA intracommunautaire | FR 42 912 456 789 — **valide (VIES)** |

## 2. Dirigeants et bénéficiaires effectifs

- **Président / Gérant unique :** M. Karim BENALI, 41 ans, né le 12/06/1985
- **Bénéficiaire effectif :** M. Karim BENALI — 100 % du capital
- Autre mandataire : Mme Elodie MARTIN, directrice technique (non associée)
- Actionnariat sans concentration anormale, aucune société intermédiaire détectée

## 3. Contrôles réglementaires

| Contrôle | Résultat |
|---|---|
| Existence et statut (Sirene) | ✅ Active, immatriculée au RCS |
| Dirigeants / BE | ✅ Identifiés, cohérents |
| Procédures collectives (BODACC) | ✅ **Aucune procédure** (redressement, liquidation, sauvegarde) détectée |
| N° TVA intracommunautaire (VIES) | ✅ Valide |
| Cohérence IBAN / nom | ⚠️ Voir alerte ci-dessous |
| Adresse / NAF / effectif | ✅ Cohérents avec une société de services IT |

## 4. Alertes

### ⚠️ Alerte 1 — IBAN (fraude au changement de RIB)

Le RIB communiqué par l'interlocuteur commercial pour cette commande :

- IBAN : `FR76 3000 4000 0310 0123 4567 890`
- Titulaire du compte : **« TECHDIS SERVICES » SAS**

**Incohérence détectée :**
1. Le nom du titulaire (« TECHDIS SERVICES SAS ») ne correspond pas à la raison sociale exacte du SIREN 912 456 789 (TECHDIS **SARL**).
2. La forme juridique du compte (SAS) diffère de celle de la société vérifiée (SARL).
3. Le guichet du compte (300040) ne correspond pas au compte historique connu de la société.

**Recommandation stricte :** ne **pas** transmettre de fonds sur ce RIB. Demander au fournisseur la confirmation écrite du RIB via un canal déjà connu (téléphone du siège, e-mail du domaine principal), et vérifier que le nom du titulaire est exactement « TECHDIS SARL ». Ce schéma (nom légèrement différent + forme juridique différente) est typique de la fraude au changement de RIB.

### ℹ️ Note 2 — Ancienneté

Création en 2022 : société jeune. Pas d'anomalie en soi, mais à prendre en compte pour le montant de la commande (15 000 € représente une part significative pour un effectif de 6–9 salariés).

### ✅ Pas d'alerte sur :

- Aucune procédure collective au BODACC
- Aucune mention de radiation ou de liquidation volontaire
- TVA intracommunautaire valide

## 5. Conclusion et recommandations

**Statut global : ✅ Vérification positive, sous réserve de régularisation du RIB.**

Le fournisseur Techdis SARL existe, est actif, a un dirigeant identifié, aucun contentieux collectif, et une TVA valide. La commande de 15 000 € peut être engagée **aux conditions suivantes** :

1. **Bloquer le paiement** tant que le RIB n'est pas confirmé par un canal de contact préexistant et que le titulaire du compte ne correspond pas exactement à « TECHDIS SARL ».
2. Envisager un **acompte plafonné à 30 %** (4 500 €), le solde à la livraison / au rendu du livrable — société d'âge récent.
3. Vérifier que la facture porte le bon SIREN (912 456 789) et le N° TVA FR 42 912 456 789 avant validation comptable.
4. En cas de nouveau doute sur le RIB : contacter le siège au 01 4X XX XX XX et relancer cette vérification.

**Aucun renvoi à la cellule crédit (credit-desk) n'est nécessaire** : aucune procédure collective n'est détectée.

---
*Vérification réalisée le 16/10/2026 à partir des bases officielles (Sirene, BODACC, VIES). Les données dirigeant/BE proviennent de la base des bénéficiaires effectifs ; aucune donnée sensible ne doit être diffusée au-delà du service facturation.*
