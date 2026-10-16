# Diagnostic du stock Shopify — action immédiate

## 1. Lecture des niveaux (aujourd'hui)

**Emplacements** : Boutique en ligne (site) · Entrepôt (Lyon)

| Réf. | Produit | En ligne | Entrepôt | Total | Seuil | Statut |
|------|---------|---------:|---------:|------:|------:|--------|
| A-102 | Bougie cire d'abeille 220 g | 2 | 9 | 11 | 10 | ⚠️ **Divergence** (2 en ligne / 9 en entrepôt) |
| B-204 | Savon surgras — Karité | 4 | 6 | 10 | 12 | 🔴 Sous le seuil |
| C-311 | Coffret découverte (3 savons) | 1 | 5 | 6 | 8 | 🔴 Sous le seuil |
| D-405 | Huile de massage 100 ml | 3 | 4 | 7 | 8 | 🔴 Sous le seuil |
| E-501 | Soin corps Beurre de karité | 22 | 30 | 52 | 25 | ✅ OK |
| F-618 | Savon — Lavande | 40 | 55 | 95 | 30 | 🟠 Surstock (~110 j de couverture) |

Les 3 références sous le seuil : **B-204, C-311, D-405**.

## 2. Analyse de la divergence (réf. A-102)

- En ligne : 2 unités. Entrepôt physiquement : 9 unités. **Différence = 7 unités non suivies** en ligne.
- Causes les plus probables, à vérifier avant toute correction :
  1. Les 7 unités n'ont **jamais été comptabilisées** en stock Shopify (réception non saisis, ou BC reçu non réceptionné) ;
  2. Des ventes ont été enregistrées hors Shopify (B2B, marché, échantillons) sans décrément ;
  3. Un lot de casse/perte non déclaré.
- **Règle respectée** : je ne « corrige » pas en silence. Toute correction manuelle passe par un **diff affiché + votre validation**, et la divergence boutique ↔ comptabilité sera signalée (voir §5).

## 3. Actions proposées — lot unique à valider en une passe

### A. Transfert en ligne — réf. A-102 (bougie 220 g)
- **Mouvement** : ajustement du stock en ligne de 2 → 9 (+7 unités).
- **Motif** : correction de comptage / alignement sur l'état physique réel de l'entrepôt.
- **Précondition** : vérifier que les 7 unités n'ont pas déjà été vendues hors ligne (historique B2B des 30 derniers jours).
- **Coût estimé** : 0 € (interne).

### B. Transferts d'entrepôt → boutique (réappro du site)
| Réf. | Quantité | Motif | Coût estimé |
|------|---------:|-------|-----------:|
| B-204 | +8 unités | Ramener le site à 12 unités (seuil) | 24 € (port + manipulation) |
| C-311 | +7 unités | Remonter au seuil de 8 | 21 € |
| D-405 | +5 unités | Remonter au seuil de 8 | 15 € |

### C. Bons de commande fournisseurs (couverture ~4 semaines)
| Réf. | Quantité | Fournisseur | Coût HT estimé | Délai |
|------|---------:|------------|--------------:|------|
| B-204 | 60 | Savonnerie du Sud (MOQ 60) | 330 € | 10 j |
| C-311 | 40 | Assemblage interne (kit) | 280 € | 5 j |
| D-405 | 48 | Huileries Provence (MOQ 48) | 420 € | 15 j |
| A-102 | 40 | Cire d'abeille — Cires Alpines | 360 € | 12 j |

> A-102 est inclus : même si le total (11) est au-dessus du seuil, la rotation actuelle (~3 u/sem) amène le stock sous seuil sous 2 semaines.

## 4. Validation

Répondez avec l'une de ces instructions :
- **« GO A+B »** → j'exécute les transferts et la correction A-102 (sans commander) ;
- **« GO A+B+C »** → tout, y compris la création des 4 bons de commande ;
- **« GO B+C »** → sans la correction A-102 (je m'occupe du diff manuellement) ;
- ou des ajustements de quantités.

À votre validation, j'exécute les mutations d'inventaire / création des BC en un seul passage, puis je relis les niveaux.

## 5. Récapitulatif — état d'après exécution (prévisionnel GO A+B+C)

| Réf. | En ligne après | Total après | Seuil | Situation |
|------|---------------:|------------:|------:|-----------|
| A-102 | 9 | 11 (+40 en BC) | 10 | Aligné |
| B-204 | 12 | 18 (+60 en BC) | 12 | Aligné |
| C-311 | 8 | 13 (+40 en BC) | 8 | Aligné |
| D-405 | 8 | 12 (+48 en BC) | 8 | Aligné |

**Reste à faire après exécution :**
1. **Signaler la divergence comptable** : les 7 unités de A-102 n'ont pas de flux cohérent entre boutique et comptabilité → à fiabiliser avec votre comptable (réception manquante vs ventes hors Shopify), et non « corrigé » sans piste ;
2. Réceptionner les BC à leur arrivée et confirmer la disponibilité en ligne ;
3. Examiner le surstock F-618 (95 u, ~110 j de couverture) : promotion ou transfert B2B pour libérer du cash avant de commander de la lavande.
