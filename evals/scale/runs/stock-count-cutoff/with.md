# Inventaire de fin d'année — régularisation des écarts avant clôture

**Périmètre :** 3 références en écart au comptage physique (2 excédents, 1 manque).
**Date de comptage (obligatoire) :** 31/12/2025
**Méthode de valorisation :** à votre confirmation (CMUP ou FIFO) — je ne choisis pas à votre place.

---

## 1. Ce qu'il faut faire avant de clôturer — plan d'action

**① Verrouiller la date de comptage & rapprocher les mouvements postérieurs**
C'est la règle n° 1 : sans date de comptage, les écarts ne sont pas fiables. Avant de valider quoi que ce soit, rattachez chaque mouvement de stock (réception, livraison, retour, casse, ajustement) au bon exercice :
- Livraisons / factures entre la date de comptage et aujourd'hui → à déduire ou à rattacher.
- Réceptions arrivées après le comptage → hors inventaire.
- Écarts de bord (écart entre stock théorique logiciel et bordereau de comptage) à re-vérifier.

**② Diagnostiquer chaque écart (cause type)**
Pour chacune des 3 références, identifier la cause avant de comptabiliser :

| Réf | Sens | Écart (u) | Causes probables à vérifier |
|---|---|---|---|
| VSR-0620 | Excédent | +8 | Livraison reçue non enregistrée ; retour client non imputé ; arrondi de bordereau |
| RLM-0608 | Excédent | +5 | Retour fournisseur non comptabilisé ; double réception |
| JNT-1226 | Manque | −6 | Casse / perte non enregistrée ; sortie non tracée ; vol ; erreur de saisie |

Règle de gestion : un écart **identifié et justifié** → corriger le mouvement à l'origine (ex. imputer la livraison manquante). Un écart **non justifié** → passer en écriture d'écart d'inventaire (cf. ③).

**③ Valoriser les écarts — à VOTRE méthode**
Je calcule les deux variantes ; vous validez la méthode :

| Réf | Écart (u) | CMUP (€/u) | Valeur CMUP | FIFO (€/u) | Valeur FIFO | Compte écart |
|---|---|---|---|---|---|---|
| VSR-0620 | +8 | 2,35 | +18,80 | 2,50 | +20,00 | 613 |
| RLM-0608 | +5 | 4,80 | +24,00 | 4,95 | +24,75 | 613 |
| JNT-1226 | −6 | 1,10 | −6,60 | 1,05 | −6,30 | 613 |
| **Net** | | | **+36,20** | | **+38,45** | |

Le compte **613** (Écarts d'inventaire sur stocks de marchandises) est applicable ici, les 3 références étant des marchandises. (Pour un fabricant : 614 matières, 615 en-cours, 616 produits finis / semi-finis.)

**④ Saisir les écritures de régularisation**
Convention PSC : écart créditeur = excédent (gain), écart débiteur = manque (perte).

| Libellé | Compte | Débit | Crédit |
|---|---|---|---|
| Excédent VSR-0620 | 370 Marchandises | 18,80 | — |
| Excédent VSR-0620 | 613 Écarts inv. marchandises | — | 18,80 |
| Excédent RLM-0608 | 370 Marchandises | 24,00 | — |
| Excédent RLM-0608 | 613 Écarts inv. marchandises | — | 24,00 |
| Manque JNT-1226 | 613 Écarts inv. marchandises | 6,60 | — |
| Manque JNT-1226 | 370 Marchandises | — | 6,60 |

*(Montants en CMUP, valeur de travail — à ajuster si vous choisissez FIFO.)*

**⑤ Dépréciation des dormants (proposition — à valider avec l'expert-comptable)**
Si des références n'ont aucun mouvement depuis 12 mois et plus, proposez une dépréciation. Exemple :
- Réf « Biellettes inox 12 mm » : 40 u dormantes depuis 14 mois × 3,50 € = 140,00 € → je propose 50 % = 70,00 €.
- Écriture : **D 681 Dépréciations des stocks 70,00 / C 395 Dépréciation des stocks 70,00.**

⚠️ Ce taux est une proposition : l'expert-comptable l'arbitre (valeur de réalisation probable, état du stock).

**⑥ FAE — Factures À Émettre (livraisons non facturées)**
Côté revenus : toute livraison effectuée mais non facturée à la date de comptage doit être émise.

| Client | Libellé | HT | TVA 20 % | TTC |
|---|---|---|---|---|
| SARL Bricopro | Livraison 29/12 non facturée | 1 250,00 | 250,00 | 1 500,00 |
| Ets Martin | Livraison 30/12 non facturée | 780,00 | 156,00 | 936,00 |

Écrites : **D 441 Clients / C 706 Ventes de marchandises + C 44572 TVA collectée.**

**⑦ FNP — Factures Non Parvenues (achats non facturés)**
Côté achats : toute réception à la date de comptage dont la facture fournisseur n'est pas arrivée doit être estimée.

| Fournisseur | Libellé | Estimation HT |
|---|---|---|
| Groupe Visserie (facture 2026-0891) | Réception 30/12, facture absente | 2 400,00 |
| Industrie Roulements (facture RR-2026-0456) | Réception 28/12, facture absente | 980,00 |

Écrites : **D 607 Achats de marchandises / C 408 Fournisseurs – factures non parvenues.**

**⑧ PCA / CCA**
- **PCA (Prix de Coût d'Acquisition)** : pour un négociant, valorise les marchandises = prix d'achat + frais accessoires supportés (transport, douane). S'applique aux 3 références ci-dessus.
- **CCA (Coût d'Acquisition)** : pour un fabricant, inclut matières + main-d'œuvre + frais indirects.

Vérifiez que le PCA / CAA utilisé au ③ est bien le dernier connu au 31/12 (et non un prix de vente par erreur).

**⑨ Produire le paquet pour l'expert-comptable**
Fichiers ci-dessous (CSV, séparateur `;`, compatible Excel FR) :
- `inventaire_ecarts_31122025.csv` — feuille de comptage + écarts valorisés
- `ecritures_regularisation_31122025.csv` — journal des régularisations
- `fae_fnp_31122025.csv` — FAE / FNP

---

## Fichier 1 — `inventaire_ecarts_31122025.csv`
```
Reference;Designation;Famille;Quantite_theorique;Quantite_comptee;Ecart;Methode;Cout_unitaire_HT;Valeur_ecart_HT;Compte_ecart;Date_comptage
VSR-0620;Vis autotapeuse M6 x 20 mm (boite 100);Marchandises;120;128;+8;CMUP (a confirmer);2,35;+18,80;613;31/12/2025
RLM-0608;Roulement a billes 608 ZZ (boite 10);Marchandises;45;50;+5;CMUP (a confirmer);4,80;+24,00;613;31/12/2025
JNT-1226;Joint torique EPDM 12 x 2,65 (boite 100);Marchandises;200;194;-6;CMUP (a confirmer);1,10;-6,60;613;31/12/2025
```

## Fichier 2 — `ecritures_regularisation_31122025.csv`
```
Date;Libelle;Compte;Designation_compte;Debit;Credit
31/12/2025;Excédent inventaire VSR-0620;370;Marchandises;18,80;
31/12/2025;Excédent inventaire VSR-0620;613;Ecarts inventaire marchandises;;18,80
31/12/2025;Excédent inventaire RLM-0608;370;Marchandises;24,00;
31/12/2025;Excédent inventaire RLM-0608;613;Ecarts inventaire marchandises;;24,00
31/12/2025;Manque inventaire JNT-1226;613;Ecarts inventaire marchandises;6,60;
31/12/2025;Manque inventaire JNT-1226;370;Marchandises;;6,60
31/12/2025;Dépréciation dormants - Biellettes inox 12 mm (proposition);681;Dépréciations des stocks et approvisionnements;70,00;
31/12/2025;Dépréciation dormants - Biellettes inox 12 mm (proposition);395;Dépréciation des stocks et approvisionnements;;70,00
```

## Fichier 3 — `fae_fnp_31122025.csv`
```
Type;Interlocuteur;Reference;Libelle;Date;Montant_HT;TVA;Compte_debit;Compte_credit
FAE;SARL Bricopro;BL-2025-1188;Livraison 29/12 non facturée;29/12/2025;1250,00;250,00;441;706 + 44572
FAE;Ets Martin;BL-2025-1194;Livraison 30/12 non facturée;30/12/2025;780,00;156,00;441;706 + 44572
FNP;Groupe Visserie;2026-0891;Réception 30/12 - facture absente;30/12/2025;2400,00;;607;408
FNP;Industrie Roulements;RR-2026-0456;Réception 28/12 - facture absente;28/12/2025;980,00;;607;408
```

---

## Ce que j'attends de vous avant de finaliser
1. **Confirmez la date de comptage** (ici 31/12/2025).
2. **Choisissez la méthode de valorisation : CMUP ou FIFO** → je régénère les fichiers avec vos montants.
3. **Validez / ajustez les causes** des 3 écarts (justifié → corrige à l'origine ; non justifié → écart d'inventaire).
4. **Validez le taux de dépréciation** des dormants avec votre expert-comptable.
5. **Confirmez le périmètre FAE / FNP** (la liste ci-dessus est une illustration à compléter par vos bordereaux réels).

Après vos validations, le paquet est prêt à transmettre à l'expert-comptable pour la clôture.
