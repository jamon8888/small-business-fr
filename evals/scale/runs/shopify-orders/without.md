# Prise en charge de 14 commandes en attente + 2 demandes de retour

## Vue d'ensemble

Vous avez 14 commandes en statut **En attente d'expédition** (unpaid/fulfillment ouvert) et 2 clientes qui demandent un retour. Le point clé à comprendre d'abord : **un retour n'a de sens que sur un article déjà reçu** (ou en cours de livraison si vous le cassez). Tant que les colis ne sont pas expédiés, les 2 demandes « de retour » sont en réalité des **demandes d'annulation** — et c'est un autre traitement, plus simple et moins coûteux.

---

## 1. D'abord : clarifier les 2 demandes de retour

Pour chacune des 2 clientes, identifiez d'abord la situation :

- **Le colis n'est pas encore expédié** → c'est une annulation, pas un retour.
- **Le colis a été expédié** (un des 14 a peut-être déjà été expédié sans que vous ayez mis à jour le statut) → c'est un retour classique.

### Cas A : annulation avant expédition (le plus probable)

1. **Répondez à la cliente dans l'heure** (e-mail ou chat) : confirmée l'annulation, précisez que le remboursement interviendra sous 5 à 10 jours ouvrés selon le moyen de paiement.
2. **Dans Shopify** :
   - *Commandes* → sélectionnez la commande → **Annuler l'expédition** si elle était marquée expédiée, puis **Annuler la commande**.
   - Le paiement est automatiquement remboursé (rachat du paiement) si la commande était payée ; si elle était en pré-autorisation, la réservation est libérée.
3. **Réservez le stock** : l'annulation réintègre l'article au stock disponible (à vérifier si vous avez un app d'inventaire tiers comme Inventory Planner ou une sync ERP).
4. **Marquez la commande avec une note interne** : « Annulée le 16/10 – retour client souhaité – remboursée ».

### Cas B : retour sur un colis déjà expédié

1. **Répondez à la cliente** avec :
   - le motif accepté (conformité, dommage, erreur de votre part → frais à votre charge ; simple changement d'avis → selon votre politique).
   - l'adresse de retour et le bon de retour (RMA) : générez un numéro RMA simple (ex. `RMA-2026-1014`).
   - le délai de retour accepté (standard : 14 jours en France) et la politique de remboursement (remboursement intégral vs avoir, déductif des frais de port aller selon votre politique).
2. **Dans Shopify** :
   - Créez un **brouillon de remboursement** : *Commandes* → commande → **Rembourser** → sélectionnez les articles + la quantité, cochez « Rembourser les frais de port » si c'est votre politique.
   - **N'exécutez pas le remboursement tant que le colis retour n'est pas reçu** (sauf politique de remboursement à l'expédition du retour, plus généreuse mais risquée sur la fraude).
3. **À réception du colis** : contrôlez l'état (usage, complétude, étiquette) puis validez le remboursement. Shopify rembourse automatiquement le canal d'origine (Carte Bleue, PayPal, Apple Pay…) ; comptez 3 à 10 jours ouvrés avant que la cliente le voie, ce qui est à anticiper dans votre message.

> **Astuce** : si vous n'avez pas de process RMA, commencez par un simple tableau (notion/Google Sheets) : n° RMA, commande, article, motif, date de demande, date de réception, statut remboursement. C'est suffisant pour 2 retours ; vous industrialiserez plus tard (app Loop, Return Prime…).

---

## 2. Gérer les 14 commandes en attente d'expédition

Objectif : **vidanger la file sous 48 h** et mettre en place un réflexe de suivi pour ne plus jamais voir ça s'accumuler.

### Tri immédiat (15 min)

Dans *Commandes → En attente d'expédition*, classez par priorité :

1. **Commandes payées** (la grande majorité) → à traiter en premier.
2. **Commandes non payées** (rachat au clic) → envoyez un e-mail de relance automatique (Shopify l'envoie par défaut 24 h après ; vérifiez que la template est bien activée dans *Paramètres → E-mails*, sinon elles seront annulées automatiquement au bout de la durée configurée, par défaut 3 jours).
3. **Commandes en précommande ou avec note client** → à traiter selon la consigne (retard annoncé, cadeau, etc.).

### Expédition

- **Sélectionnez les commandes** → **Expédier** → saisissez le numéro de suivi par lot (l'option « Numéro de suivi en vrac » permet d'expédier plusieurs commandes d'un coup avec un seul n° de suivi si c'est un colis groupé).
- **Marquage expédié = e-mail automatique au client** : c'est votre engagement de délai (votre page FAQ et vos e-mails de confirmation promettent X jours ; tenez-le).
- Si vous utilisez un transporteur (Colissimo, Mondial Relay, DPD…) : générez les étiquettes en lot depuis l'app du transporteur dans le Shopify App Store, imprimez, collez, déposez. Pour 14 colis, une sortie au point de dépôt suffit.

### Vérifications avant expédition (check-list express)

- [ ] Les 2 commandes concernées par les demandes de retour sont-elles bien **exclues** du lot à expédier ?
- [ ] Les articles des 14 sont-ils en stock (l'écran d'expédition le signale si l'inventaire est insuffisant) ?
- [ ] Adresses complètes et sans faute (casse, « c/o », adresse pro vs perso) ?
- [ ] N° de suivi correct et cohérent avec le transporteur choisi ?

### Après expédition

- Vérifiez que l'e-mail de confirmation d'expédition est bien parti (le client le voit dans sa commande).
- Notez la date de livraison estimée affichée (Shopify le calcule via le transporteur si l'app est branchée).

---

## 3. Mettre en place le réflexe de suivi (10 min, une fois pour toutes)

Le vrai problème n'est pas ces 14 commandes mais le fait qu'elles aient pu s'accumuler :

1. **Vue de contrôle quotidienne** : dans *Commandes*, filtrez par « En attente d'expédition » et fixez un créneau fixe (ex. 9 h 30, 30 min) pour traiter la file. À votre volume (14 commandes en retard = anormal), 1 passage/jour suffit ; à 50+/jour, passez à 2.
2. **Alerte e-mail** : *Paramètres → E-mails* → activez l'e-mail de nouvelle commande à vous (ou au responsable), pour ne plus découvrir les commandes en retard.
3. **Délai client explicite** : votre page « Livraison » et vos e-mails promettent un délai (ex. expédié sous 24/48 h). Si la réalité ne permet pas de le tenir, ajustez le message au client plutôt que d'encaisser les réclamations.
4. **Reporting hebdo** (5 min le vendredi) : commandes en attente, délais moyens d'expédition, retours de la semaine. C'est ce que vous regarderez en réunion d'équipe ou pour la trésorerie (les retours = sorties de trésorerie à anticiper).

---

## 4. Séquence d'actions résumée (ordre de priorité)

| # | Action | Durée | Où |
|---|--------|-------|----|
| 1 | Contacter les 2 clientes : qualifier retour vs annulation, envoyer RMA ou confirmation d'annulation | 20 min | E-mail |
| 2 | Annuler les 2 commandes (cas A) ou créer les RMA (cas B) | 10 min | Shopify → Commandes |
| 3 | Trier les 12 commandes restantes : payées / non payées | 5 min | Shopify → Commandes |
| 4 | Relancer les non payées, laisser annuler les anciennes | 5 min | Shopify (auto) |
| 5 | Générer les étiquettes, expédier, coller les n° de suivi | 30–45 min | App transporteur + Shopify |
| 6 | Activer l'alerte « nouvelle commande » + créneau quotidien de traitement | 10 min | Shopify → Paramètres |

**Total : moins de 2 h pour remettre la boutique à zéro**, et un système en place pour que les 14 n'aient plus lieu d'être.

---

## Points de vigilance

- **Ne remboursez jamais manuellement en double** (ex. via votre compte bancaire ET via le rachat Shopify) : double sortante et client mécontent.
- **Le remboursement « non remboursable »** : certaines cartes ou certains moyens de paiement (virement, certains portefeuilles) ne peuvent pas être rachetés par Shopify — dans ce cas, remboursez par avoir ou virement manuel, et notez-le sur la commande.
- **Fiscalité** : un retour/annulation est une annulation de vente en comptabilité (pas un « coût ») ; conservez vos RMA, ils servent de pièce justificative.
- **Si la file dépasse régulièrement 2 jours** : c'est un signal de capacité (stock, préparation, transporteur) à traiter — pas un problème de diligence.
