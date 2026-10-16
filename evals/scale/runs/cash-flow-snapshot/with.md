# Flux de trésorerie — 15 octobre 2026 → 13 janvier 2027

**Sources :** chiffres fournis directement par le dirigeant (solde bancaire, encaissements attendus, décaissements). Aucun connecteur Qonto, Pennylane ni export CSV n'est connecté pour ce passage — aucune donnée d'historique de règlement disponible, donc **aucune borne de confiance calculée** (je n'invente pas de variance). Les indicateurs DSO / DPO / DIO ne sont pas affichés : pas de profil à stock confirmé, pas de balances âgées sources.

**Point d'attention avant tout :** la TVA de 2 150 € est datée « en septembre » — et nous sommes le **15 octobre**. Cette échéance est passée. Soit elle est déjà payée (elle est exclue de la prévision ci-dessous), soit c'est la prochaine échéance (octobre/novembre) : confirme-le. J'indique dans les risques l'impact si elle n'est pas encore réglée.

---

## Position dans 90 jours : **12 500 €**

Solde de départ : 18 400 € → **12 500 € le 13 janvier 2027**, soit **−5 900 € sur 90 jours** sur les mouvements déclarés.

| Fenêtre | Période | Encaissements | Décaissements | Net | Solde en fin de fenêtre |
|---|---|---|---|---|---|
| 0–30 j | 15 oct → 14 nov | 9 200 € | 14 100 € | **−4 900 €** | 13 500 € |
| 31–60 j | 15 nov → 14 déc | 14 600 € | 7 800 € | **+6 800 €** | 20 300 € |
| 61–90 j | 15 déc → 13 jan | 0 € | 7 800 € | **−7 800 €** | 12 500 € |

### Détail par ligne

**Encaissements**
| Poste | Montant | Fenêtre |
|---|---|---|
| Encaissements du mois (octobre) | 9 200 € | 0–30 j |
| Encaissements du mois suivant (novembre) | 14 600 € | 31–60 j |

**Décaissements**
| Poste | Montant | Date/échéance | Fenêtre |
|---|---|---|---|
| Salaires octobre | 7 800 € | mi-octobre | 0–30 j |
| Fournisseur | 6 300 € | ~14 novembre (« dans 30 jours ») | 0–30 j |
| Salaires novembre | 7 800 € | mi-novembre | 31–60 j |
| Salaires décembre | 7 800 € | mi-décembre | 61–90 j |
| TVA | 2 150 € | « septembre » — **échéance passée, exclue — à confirmer** | — |

---

## ⚠ Risques signalés

1. **Tension immédiate sur les 30 premiers jours :** la fenêtre 0–30 j est déficitaire de **4 900 €** (encaissements 9 200 € contre salaires 7 800 € + fournisseur 6 300 € = 14 100 €). Le solde descend à 13 500 € le 14 novembre. Pas de rupture de trésorerie, mais aucun matelas de repli si l'encaissement d'octobre glisse.
   *Action : vérifier d'où viennent les 9 200 € d'octobre (quels clients, quelles factures) et confirmer leur calendrier d'encaissement avant le 14 novembre.*

2. **La fenêtre 61–90 j dépend entièrement de l'encaissement de novembre :** aucun encaissement n'est identifié entre le 15 décembre et le 13 janvier, alors que les salaires de décembre (7 800 €) sont certains. Si le 14 600 € de novembre est partiellement retardé, le solde de janvier tombe sous 12 500 €.
   *Action : identifier précisément les 14 600 € de novembre et sécuriser l'encaissement avant le 15 décembre (rappel client, virement anticipé si nécessaire).*

3. **TVA à 2 150 € : date incohérente (septembre déjà écoulé).** Si elle n'est pas encore réglée, elle s'ajoute aux décaissements et le solde à 90 jours passe de 12 500 € à **10 350 €**.
   *Action : confirmer le statut de cette TVA avant de figer la prévision.*

4. **Pas de borne de confiance :** sans historique de règlement (Qonto, PayPal, export CSV), je ne peux pas chiffrer la variance d'encaissement. Les montants ci-dessus sont des point estimates — traités comme tels.

---

## À apporter pour affiner la prévision

- **Qonto (MCP officiel) ou export CSV** : les 9 200 € et 14 600 € détaillés par client avec dates d'échéance — je pourrai alors calculer des bornes de confiance réelles et repérer les payeurs tardifs.
- **Confirmation du statut de la TVA** de 2 150 €.
- **Le profil de l'entreprise** (services / négoce / fabrication / mixte) : si à stock, je calcule DSO / DPO / DIO et le cycle de conversion.

---

Cette prévision s'appuie sur les chiffres que tu m'as donnés — pas sur un relevé bancaire ni un grand livre connecté. Elle ne remplace pas un conseil comptable : vérifie avec ton expert-comptable avant toute décision de financement.

*Export possible : `cash-flow-snapshot-2026-10-15.xlsx` (onglets Synthèse / Détail / Risques) sur demande.*
