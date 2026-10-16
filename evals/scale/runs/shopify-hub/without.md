# Pilotage de votre boutique Shopify — plan d'action

Très bien : votre boutique `ma-boutique.myshopify.com` tourne déjà, et vous voulez une gouvernance claire sur les 5 piliers (catalogue, stock, commandes, clients, ventes). Voici comment je propose de structurer le pilotage, du diagnostic initial jusqu'au rythme de suivi.

## 1. Par où commencer : le diagnostic initial (semaine 1)

Avant d'optimiser quoi que ce soit, il faut une photo d'état de la boutique. Concrètement :

1. **Accès à l'admin** : `ma-boutique.myshopify.com/admin` — je vérifie les rôles et permissions des équipes (Propriétaire / Admin / Restreint) dans *Paramètres → Personnel*.
2. **Audit du catalogue** :
   - Nombre de produits et de variantes, part de produits « inactifs » ou sans stock,
   - Complétude des fiches : photos, descriptions, poids, SKU, catégories, balises,
   - Canaux actifs (boutique en ligne, Marketplace, Instagram, POS…) et cohérence des prix par canal.
3. **Audit du stock** :
   - Produits en rupture ou quasi en rupture,
   - Produits dormant (0 vente depuis 60/90 jours),
   - Fiabilité des quantités (écart entre théorique et réel) et existence d'alertes de seuil.
4. **Audit des commandes** :
   - Volume moyen quotidien, temps de préparation, taux de retours/refunds,
   - Commandes bloquées (paiement en attente, fraude, adresse invalide).
5. **Audit des ventes et des clients** :
   - CA 3 derniers mois, panier moyen, conversion,
   - Répartition nouveaux / clients fidèles,
   - Segments clients existants et emails/marketing connectés.

**Livrable de la semaine 1** : un rapport d'état des lieux avec les 5 à 10 priorités classées par impact (revenus, ruptures, cash immobilisé) et un plan d'action 30 jours.

## 2. Le pilotage au quotidien — le catalogue

- **Rituels** : en revue hebdo, on vérifie les nouveautés, les promotions en cours et les fins de stock prévues.
- **Qualité des fiches** : chaque produit doit avoir un SKU unique, un poids (pour les frais de port), au moins 2-3 photos, une description avec bénéfices + caractéristiques, une catégorie et des balises cohérentes.
- **Hygiène** : les produits non vendus depuis 90 jours sont soit réactivés (prix, visuel, page), soit mis en promotion pour les écouler, soit désactivés.
- **Saisonnalité** : calendrier des mises à jour (nouveautés 4-6 semaines avant la saison, soldes planifiées).

## 3. Le pilotage du stock

C'est souvent le point le plus sensible : le stock, c'est du cash immobilisé.

- **Indicateurs clés** :
  - *Jours de stock restant* (Days of inventory remaining) — alerte si < 15 jours sur un best-seller,
  - *Sell-through rate* par produit — < 50 % sur 60 jours = produit à réévaluer,
  - *Analyse ABC* : les produits A (top 20 % qui font 80 % du CA) ne doivent jamais être en rupture.
- **Règles de seuils** : chaque variante reçoit un stock minimal (réapprovisionnement) et un stock maximal. Shopify envoie des alertes automatiques quand un seuil est franchi.
- **Réapprovisionnement** : calcul simple par variante = ventes moyennes journalières × délai fournisseur + marge de sécurité. On produit une proposition de commande fournisseur hebdo.
- **Comptage physique** : un inventaire tournant mensuel (par lot de 20-30 références) plutôt qu'un grand inventaire annuel, avec ajustements tracés.
- **Outils** : les rapports intégrés Shopify (Stock, Ventes de stock, Valeur du stock de fin de mois) ; en option une app d'optimisation du réassort si le catalogue dépasse ~200 références actives.

## 4. Le pilotage des commandes

- **Objectif** : aucune commande ne « dort ». Récupération du taux de commandes non expédiées > 48 h.
- **Rituels** : revue quotidienne des commandes ouvertes (10-15 min), avec vérification des cas particuliers (paiement en échec, adresse suspecte, note client).
- **Indicateurs** :
  - Délai moyen commande → expédition,
  - Taux de retours et motifs de retour (top 3 motifs à traiter en priorité),
  - Taux d'annulation.
- **Automatisation** : avec Shopify Flow, on peut automatiser les tâches répétitives — par ex. étiqueter les commandes à risque, notifier l'équipe en cas de stock bas sur une commande, créer un bon de retour.

## 5. Le pilotage des clients

- **Segmentation** : on met en place 4 segments minimaux —
  1. Nouveaux clients (30 jours),
  2. Clients actifs (achat < 90 jours),
  3. Clients dormants (90-180 jours),
  4. Clients perdus (> 180 jours).
- **Indicateurs** :
  - Part du CA faite par les clients récurrents (à suivre chaque mois),
  - Taux d'achat répété et délai moyen entre deux achats (il définit le calendrier de relance),
  - Valeur client moyenne par segment.
- **Actions types** :
  - Email « bienvenue » + suivi post-achat (J+7) pour les nouveaux,
  - Relance dormants avec une offre ciblée,
  - Programme fidélité si le réachat est un axe de croissance,
  - Traitement des avis clients et des demandes de service client dans les 24 h.
- **Canal** : Shopify Email (ou votre outil d'emailing) connecté au CRM Shopify.

## 6. Le pilotage des ventes

- **Tableau de bord mensuel** (à partir des rapports intégrés Shopify) :
  - CA, nombre de commandes, panier moyen, marge,
  - Taux de conversion et trafic par canal,
  - CA par canal de vente, par collection, par pays,
  - Nouveaux vs clients récurrents.
- **Rythme de lecture** :
  - **Quotidien (10 min)** : commandes du jour, ruptures, anomalies,
  - **Hebdo (30 min)** : CA semaine, top 10 produits, stock critique, retours,
  - **Mensuel (1-2 h)** : bilan complet vs objectifs, décisions de réassort, ajustements prix/promos, plan du mois suivant.
- **Objectifs** : on fixe un CA mensuel cible et on suit l'écart chaque semaine, avec des contre-mesures documentées.

## 7. Plan 30 jours proposé

| Semaine | Actions |
|---|---|
| S1 | Diagnostic complet + rapport d'état des lieux + priorités |
| S2 | Hygiène catalogue (SKUs, fiches, produits dormants) + mise en place des seuils d'alerte stock |
| S3 | Rituels de pilotage en place (quotidien/hebdo) + automatisations Shopify Flow + segmentation clients |
| S4 | Premier bilan mensuel, plan de réassort, plan d'actions du mois suivant |

## 8. Ce dont j'ai besoin de votre part pour démarrer

1. Un compte d'accès à l'admin Shopify (je recommande un rôle « Admin » dédié à l'assistant, pas le compte propriétaire).
2. Vos objectifs : CA mensuel cible, marges visées, priorités (croissance, cash, marges ?).
3. Vos délais fournisseurs habituels (pour les calculs de réassort).
4. Vos outils existants : emailing, facturation, comptabilité (ex. : comment exportez-vous le CA vers votre comptable ?).

**Ma recommandation de départ** : on commence par le diagnostic de la semaine 1. C'est lui qui dira si l'urgence est le stock (ruptures sur les best-sellers), le catalogue (fiches qui ne convertissent pas) ou les clients (pas de relance, pas de fidélisation). On pilote ensuite avec les rituels quotidiens et hebdomadaires décrits ci-dessus, et on revient chaque mois sur les chiffres.

Dites-moi quand vous êtes prêt et je vous prépare la check-list d'audit détaillée.
