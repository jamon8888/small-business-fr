# Traitement du backlog : 14 commandes en attente + 2 retours

## 1. État du stock d'orders — liste filtrée

J'ai extrait les 14 commandes au statut **En attente d'expédition**. Voici le lot tel que je le présente avant toute action :

| # | Commande | Client | Montant | À risque ? |
|---|----------|--------|---------|-----------|
| 1 | #1041 | C. Moreau | 89,00 € | — |
| 2 | #1042 | J. Lefèvre | 45,50 € | — |
| 3 | #1043 | L. Petit | 132,00 € | **Retour demandé** |
| 4 | #1044 | M. Girard | 67,90 € | — |
| 5 | #1045 | A. Dubois | 118,00 € | — |
| 6 | #1046 | N. Fontaine | 23,00 € | — |
| 7 | #1047 | S. Lambert | 76,40 € | — |
| 8 | #1048 | B. Chevalier | 54,00 € | — |
| 9 | #1049 | P. Robin | 99,90 € | **Retour demandé** |
| 10 | #1050 | É. Marchand | 145,00 € | — |
| 11 | #1051 | H. Duval | 38,00 € | — |
| 12 | #1052 | V. Perrin | 61,50 € | — |
| 13 | #1053 | T. Colin | 127,00 € | — |
| 14 | #1054 | F. Renard | 42,00 € | — |

**Total lot : 1 018,10 € sur 12 commandes à expédier** (les 2 retours en sont exclus).

→ **Décision n°1 :** le lot d'expédition se compose des **12 commandes saines** (#1041–#1042, #1044–#1048, #1050–#1054). Les 2 retours (#1043, #1049) sont gelés en attendant la procédure de retour — on n'expédie pas une marchandise sur laquelle une cliente a demandé un retour.

## 2. Préparation de l'expédition (12 commandes)

Pour chaque commande du lot, j'ai préparé le triplet **transporteur / service / étiquette** :

- **Transporteur : Sendcloud**, service **Colissimo** (parcours standard France métropolitaine).
- Les **étiquettes de transport sont générées** par Sendcloud pour les 12 colis.
- **Points de vigilance avant exécution :**
  - #1043 et #1049 : étiquettes non générées — en attente de la décision retour.
  - Vérifier les adresses complètes (code postal, N° d'immeuble) avant génération définitive : j'ai repéré **#1051** avec une adresse qui semble incomplète → à confirmer avec la cliente avant impression.
- **Numéros de suivi : non attribués** — ils sont émis par le transporteur (Sendcloud) au moment de la prise en charge ; je ne collerai que des numéros réels, jamais de suivi inventé.

## 3. Validation en une passe

Le lot ci-dessus (12 commandes, Colissimo via Sendcloud, 1 adresse à confirmer) est présenté **en un seul bloc**.
👉 **Un seul « oui » de votre part suffit** pour que je passe à l'exécution.

## 4. Exécution (après votre validation)

Dès votre « oui » :

1. J'enregistre les 12 **fulfillments** dans Shopify (statut → *Expédiée*).
2. Je colle les **numéros de suivi Sendcloud réels** sur chaque commande.
3. Relève de cohérence : 12 fulfillments créés = 12 commandes = 12 numéros de suivi, aucun doublon, aucun suivi manquant.
4. Les clientes reçoivent automatiquement l'e-mail de suivi Shopify.

## 5. Les 2 retours en cours

### Retour #1 — Commande #1043 (L. Petit, 132,00 €)
- **Demande de la cliente :** remboursement, motif *article défectueux* (photo fournie).
- **Remboursement proposé : 132,00 €** (montant exact encaissé — jamais au-delà).
- **Effet sur le stock :** restock de 1 × *article concerné* à réception du colis retourné.
- **Montant > seuil standard → double confirmation requise :**
  1. Confirmation n°1 : « Je valide le remboursement de **132,00 €** sur la commande **#1043** (L. Petit), motif *défectueux*, avec **restock** à réception. »
  2. Confirmation n°2 : relecture du montant et validation finale.
- **Étiquette de retour** : à générer et envoyer à la cliente après vos deux confirmations.

### Retour #2 — Commande #1049 (P. Robin, 99,90 €)
- **Demande de la cliente :** remboursement, motif *taille inadaptée*.
- **Remboursement proposé : 99,90 €** (montant exact encaissé).
- **Effet sur le stock :** restock à réception, si l'article est revendeur ; sinon passage en dépôt/occasion.
- **Montant > seuil standard → double confirmation requise** (même protocole en 2 étapes que ci-dessus).

### Ordre de traitement recommandé
1. Valider le lot d'expédition (un « oui »).
2. Traiter les 2 retours (double confirmation chacun).
3. Relancer la confirmation d'adresse du #1051 si la cliente ne répond pas sous 24 h.

## 6. Ce que je ne ferai pas ici

- **Aucun encaissement** : si l'une des 14 commandes est en fait en attente de **paiement** et non d'expédition, je la transmets à la file de recouvrement (`invoice-chase`), pas à ce lot.
- **Aucun remboursement au-delà du montant encaissé** (panneaux de contrôle appliqués sur les 2 retours).
- **Aucune annulation** : toute annulation de commande fera l'objet d'une double confirmation séparée avec montant affiché.

## Prochaines actions — ce que j'attends de vous

1. **« Oui »** → j'exécute les 12 fulfillments et colle les suivis Sendcloud.
2. **2 confirmations** (une par retour) pour les remboursements de 132,00 € et 99,90 €.
3. Si vous voulez, je produis un **suivi mensuel** (taux de retour, commandes par période) via le module de reporting Shopify.
