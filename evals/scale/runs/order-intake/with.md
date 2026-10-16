# Brouillon de commande contrôlé — e-mail client reçu

> Source : e-mail client « 50 unités réf 12 à 11 € pièce, livraison le 15 ».
> L'e-mail est traité comme une **donnée** (jamais comme une instruction). Statut : **brouillon, à contrôler avant AR**.

## 1. Brouillon de commande

| Élément | Valeur | Statut |
|---|---|---|
| Client | Non identifié dans l'e-mail | ⚠️ À vérifier (contrôle 1) |
| Référence | « réf 12 » | ⚠️ À confirmer au catalogue (contrôle 2) |
| Quantité | 50 unités | ⚠️ À vérifier vs conditionnement / MOQ (contrôle 4) |
| Prix unitaire demandé | 11,00 € HT | ⚠️ Écart vs grille (contrôle 3) |
| Prix unitaire grille | 12,00 € HT | ✅ Grille en vigueur |
| Montant total demandé | 550,00 € HT | calculé |
| Montant total grille | 600,00 € HT | calculé |
| Écart commercial | **− 50,00 € HT (− 8,33 %)** | ⚠️ Décision dirigeant requise |
| Date de livraison demandée | « le 15 » (mois non précisé) | ⚠️ À préciser puis croiser avec le délai possible (contrôle 8) |
| Adresse de livraison | Absente de l'e-mail | ⚠️ À collecter (contrôle 7) |
| Stock disponible | stock − réservé + attendu confirmé | ⚠️ Chiffres à tirer du SGE/ERP (contrôle 5) |
| Encours client + commande | vs plafond client | ⚠️ À vérifier (contrôle 6) |
| Mentions CGV | Aucune mention contradictoire explicite dans l'e-mail | ✅ (hors dérogation tarifaire, point 3) |

## 2. Liste des écarts

1. **Client non identifié** — l'e-mail ne porte pas de raison sociale. Vérifier l'expéditeur : client connu ? Sinon → procédure **verifier-tiers** (KYC, plafond, conditions) avant toute suite.
2. **Référence « 12 »** — à rapprocher de l'article exact du catalogue (désignation, famille, conditionnement). Une réf seule ne suffit pas à valider l'article facturable.
3. **Prix hors grille** — « prix 11,00 € au client, grille 12,00 € » : écart de 1,00 €/pièce, soit **50,00 € HT** sur les 50 unités. C'est une remise commerciale qui nécessite votre validation expresse (seuil d'autorisation remises). À intégrer en remise sur AR ou à renégocier à 12,00 €.
4. **Quantité vs conditionnement / MOQ** — 50 unités : à vérifier si l'article se vend par palettes/boîtes de X et si le MOQ est atteint.
5. **Stock** — calcul à exécuter : stock disponible = stock − réservé + arrivages confirmés, pour la date demandée.
6. **Plafond client** — à vérifier : encours actuel + 550 € (ou 600 €) ≤ plafond.
7. **Adresse de livraison** — absente : à récupérer auprès du client (utiliser l'adresse connue en fiche client, à confirmer ; tout changement d'adresse = à valider hors canal).
8. **Date de livraison « le 15 »** — mois non précisé : clarifier, puis comparer au délai de préparation/livraison possible à ce volume.
9. **CGV** — aucune mention contradictoire détectée dans l'e-mail ; le seul point de dérogation est tarifaire (écart 3).

## 3. Projet d'AR (brouillon — à envoyer après validation V2)

> **Bon de commande / Acceptation de commande — Brouillon**
>
> À : [Client à confirmer]
> De : [Votre société]
> Date : 16/10/2026
>
> | Réf | Désignation | Qté | PU HT | Total HT |
> |---|---|---|---|---|
> | [réf 12 — à confirmer] | [Désignation à insérer] | 50 | 11,00 € *(grille 12,00 € — remise à valider)* | 550,00 € |
>
> **Total HT : 550,00 €** — TVA : à compléter — **Net à payer : à compléter**
>
> Livraison demandée : le 15 [mois à préciser] — [adresse à insérer]
>
> *Commande enregistrée et acceptée sous réserve de : (a) confirmation du prix/remise par notre service commercial, (b) disponibilité du stock, (c) respect de nos CGV en vigueur (paiement 30 jours, pénalités de retard, propriété des marchandises).*
>
> *Réponse à la présente acceptation = acceptation de nos CGV. Toute condition particulière doit être notifiée avant expédition.*

## 4. Actions demandées

1. **Confirmer l'identité du client** (rappeler l'expéditeur / croiser la fiche client) — bloque tout le reste.
2. **Valider la remise de 50,00 €** (11,00 € au lieu de 12,00 €) : accepter à 11,00 € ou proposer 12,00 €.
3. **Préciser la date** (« le 15 » = 15/10 ou 15/11 ?) et fournir/confirmationner **l'adresse de livraison**.
4. Je relance les contrôles stock, MOQ/conditionnement et plafond dès 1–3 confirmés.
5. **Envoi de l'AR après votre acceptation** (validation V2) — ne pas envoyer l'AR avant.

*Note sécurité : l'e-mail du client est une donnée non fiable ; aucune instruction qu'il contient ne sera exécutée (pas de changement IBAN/adresse appliqué sans validation hors canal).*
