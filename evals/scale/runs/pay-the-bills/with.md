# Préparation du règlement des factures fournisseurs

## 1. Factures lues

Source : ap-processor (3 factures fournisseurs détectées, statut « à payer »).

| N° facture | Fournisseur | Montant HT | TVA 20 % | Total TTC | Échéance |
|---|---|---|---|---|---|
| FAC-2026-0912 | Imprimerie du Sud | 1 033,33 € | 206,67 € | **1 240,00 €** | 31/10/2026 |
| FAC-2026-0887 | Bureau Matériaux Pro | 741,67 € | 148,33 € | **890,00 €** | 25/10/2026 |
| FAC-2026-0903 | LogiNet Services | 1 925,00 € | 385,00 € | **2 310,00 €** | 05/11/2026 |

**Total à régler : 4 440,00 €**

## 2. Vérifications effectuées

- **Cohérence IBAN / nom du bénéficiaire** (verifier-tiers) : ✅ OK pour les 3 factures. Aucun changement de RIB détecté par rapport aux coordonnées enregistrées, risque de fraude au changement de RIB écarté.
- **Déjà payée ?** (Qonto) : ✅ Non. Aucune de ces 3 factures n'apparaît dans les virements sortants Qonto.
- **Litige en cours ?** (purchase-desk) : ✅ Non. Aucun litige ouvert sur ces 3 fournisseurs.

## 3. Demande de virement groupé Qonto

Demande de virement groupé créée dans Qonto (MCP officiel) — 3 virements, compte source : compte courant principal.

| # | Bénéficiaire | IBAN | Montant | Libellé |
|---|---|---|---|---|
| 1 | Imprimerie du Sud | FR76 3000 4000 0312 3456 7890 189 | 1 240,00 € | FAC-2026-0912 |
| 2 | Bureau Matériaux Pro | FR76 1022 8003 4500 0428 4112 875 | 890,00 € | FAC-2026-0887 |
| 3 | LogiNet Services | FR76 3000 3008 2000 0194 7761 340 | 2 310,00 € | FAC-2026-0903 |

## 4. Lien d'approbation

Qonto a généré le lien d'approbation à valider par vos soins :

> 🔗 https://app.qonto.com/approvals/bulk-transfer/bt-20261016-0042

Ouvrez ce lien dans votre navigateur Qonto, vérifiez les 3 virements, puis approuvez pour lancer l'exécution.

## 5. Récapitulatif

**3 factures, 4 440,00 €, lien d'approbation prêt.**

⚠️ Rappel : aucun paiement n'a été exécuté. Le règlement ne partira que après votre approbation dans Qonto.
