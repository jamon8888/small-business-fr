# Segmenter vos 4 800 clients Shopify pour cibler vos fidèles

## L'objectif

Avec 4 800 clients, votre base est à une taille idéale pour faire de la segmentation manuelle et ciblée : c'est trop petit pour se contenter de campagnes de masse, mais assez grand pour que chaque segment mérite une offre sur mesure. Le principe clé : **un client fidèle n'est pas un client qui a acheté beaucoup, c'est un client qui revient, régulièrement, en dépensant de plus en plus.**

## 1. La méthode de segmentation recommandée : le RFM

Le critère universel pour mesurer la fidélité est le modèle **RFM**, qui note chaque client sur 3 dimensions :

| Critère | Signification | Ce qui rend un client « fidèle » |
|---|---|---|
| **R**écence | Date du dernier achat | A acheté récemment (moins de 60 jours) |
| **F**réquence | Nombre de commandes cumulées | Au moins 3 commandes sur 12 mois |
| **M**ontant (M value) | Panier moyen / CA total | Au-dessus de votre panier moyen global |

### Comment l'appliquer concrètement

**Étape 1 — Exportez vos données.** Dans Shopify : `Clients → Tous les clients → Exporter`. Vous obtiendrez le nom, l'email, la date d'inscription, le nombre de commandes et le total dépensé par client. La date du dernier achat s'obtient en croisant avec l'export `Commandes → Exporter` (ou via un app gratuit type *Customer Data Export* / *MESA* pour automatiser le calcul RFM).

**Étape 2 — Calculez vos propres seuils** (les valeurs types ci-dessous sont des points de départ à adapter à votre catalogue et à votre cycle d'achat) :

- **Récence** : dernier achat à moins de **60 jours** = vert ; 60–180 jours = orange ; plus de 180 jours = rouge
- **Fréquence** : **3 commandes ou plus** sur 12 mois = vert ; 2 = orange ; 1 = rouge
- **Montant** : total dépensé **au-dessus de la médiane** de votre base = vert

Avec 4 800 clients, vous obtenez naturellement 8 profils. Voici un profilage réaliste d'une base de cette taille :

## 2. Vos 6 segments et ce que vous en faites

| # | Segment | Profil (RFM) | Taille estimée | Part du CA typique | Action |
|---|---|---|---|---|---|
| 1 | **Champions (fidèles)** | Récents, fréquents, gros paniers | ~350–500 (8–10 %) | ~30–40 % | **Ici : votre offre privée** |
| 2 | **Fidèles stables** | Récents, fréquents, panier moyen | ~600–800 (13–16 %) | ~20 % | Offre privée (deuxième vague) |
| 3 | **Récents actifs** | Achat récent, 1–2 commandes | ~700–900 | ~12 % | Upsell + programme parrainage |
| 4 | **Clients à nourrir** | Achats passés, 3+ commandes, inactifs 6–12 mois | ~400–500 | ~8 % | Relance « on vous manque » |
| 5 | **En dormition** | 1–2 commandes, inactifs 6–12 mois | ~800–1 000 | ~5 % | Campagne win-back standard |
| 6 | **Inactifs / perdus** | Inactifs depuis plus de 12 mois | ~1 200–1 600 | ~3–5 % | Pas dans l'offre privée ; une dernière relance généreuse au maximum |
| 7 | **Nouveaux** | Inscription récente, pas d'achat | ~200–400 | 0 % | Séquence d'onboarding |

**La règle des 20/80 appliquée à votre base** : attendez-vous à ce que les 500–800 clients des segments 1+2 (environ 12–15 % de vos 4 800) représentent près de 50 % de votre chiffre d'affaires. Ce sont eux qui reçoivent l'offre privée.

## 3. Construire l'offre privée pour les Champions

### Pourquoi « privée » fonctionne

L'efficacité d'une offre privée ne vient pas seulement du discount : elle vient du **sentiment d'exclusivité**. Le message doit faire sentir au client qu'il est reconnu pour sa fidélité, pas qu'il a été ciblé pour sa valeur.

### La structure type de l'offre

1. **Un titre qui nomme le statut** : « Réservé à nos clients [Nom de la marque] fidèles » — pas « -20 % pour tous ».
2. **Une reconnaissance chiffrée** : « Vous êtes l'un de nos X clients les plus fidèles, avec Y achats chez nous. Merci. »
3. **L'avantage concret** (choisissez 1 à 2, pas les 4) :
   - Un code promo à **15–20 %** valable 10 jours (plutôt court : l'urgence fait agir) ;
   - Un **accès anticipatif** à une nouvelle collection 48 h avant tout le monde ;
   - Un **cadeau offert** (produit d'appoint, échantillon) au lieu d'un discount — plus mémorable et moins érosif pour la marge ;
   - Une **livraison offerte** sur la commande.
4. **Un appel à l'action unique** : un lien direct vers le catalogue ou la collection.
5. **Une durée limitée** : « valable jusqu'au [date] » — toujours une vraie deadline.

### Ce qu'il faut éviter

- **Ne pas envoyer la même offre que vos campagnes publiques** : si vos Champions voient la promo à -20 % sur votre liste complète, l'offre privée perd tout son sens.
- **Ne pas mixer les segments** dans le même email : un client avec 1 commande ne doit pas recevoir le message réservé aux clients à 10 commandes.
- **Ne pas sur-segmenter** : 3 vagues maximum (Champions → Fidèles stables → à nourrir). Au-delà, vous multipliez le travail sans gain mesurable.

## 4. Le plan d'exécution (1 à 2 semaines)

| Jour | Action | Outil |
|---|---|---|
| J1 | Export clients + commandes depuis Shopify | Shopify admin → Export |
| J2 | Calcul des seuils RFM (Excel/Sheets suffisent à 4 800 lignes) | Google Sheets : VLOOKUP + formules |
| J3 | Nettoyage : supprimer les emails invalides / doublons | Shopify (statut client) + validation |
| J4–J5 | Rédiger les 3 vagues d'emails (Champions / Fidèles / à nourrir) | Votre outil d'emailing (Klaviyo, Omnisend, Mailchimp…) |
| J6 | Créer les 3 listes de diffusion | Import CSV dans l'outil d'emailing |
| J7 | **Vague 1** : envoi aux Champions (le segment 1 uniquement) | |
| J14 | Mesurer : ouverture, clics, conversion, CA généré | |
| J14 | **Vague 2** : mêmes offres élargies aux Fidèles stables | |
| J21 | **Vague 3** : relance à nourrir avec un angle « on vous a manqué » | |
| J30 | Bilan : CA de l'offre privée vs baseline, puis réajuster les seuils RFM | |

## 5. Mesurer si ça a marché

Quatre indicateurs à suivre sur les 30 jours suivant l'envoi :

1. **Taux d'ouverture** des Champions (baseline typique 35–45 % ; viser > 45 % sur ce segment)
2. **Taux de clic** (> 8–10 % sur un segment chaud)
3. **Taux de conversion** du lien vers le site (> 5 % du segment)
4. **CA par client** généré par l'offre vs votre panier moyen global

Si l'offre privée génère un panier moyen supérieur à votre moyenne — c'est fréquent quand on combine exclusivité et deadline — c'est un signal que le format est scalable.

## 6. En faire un système récurrent

- **Recalculer les segments à chaque trimestre** (automatisable avec Klaviyo, Omnisend ou un app type *MESA* : le profil RFM se met à jour tout seul).
- **Ritualiser l'offre** : une offre privée par trimestre, au même moment, devient un rendez-vous que vos fidèles attendent. C'est plus puissant que 12 promos dispersées.
- **Élever les seuils progressivement** : au bout de deux cycles, relevez le barème (ex. : 4 commandes au lieu de 3) pour que le statut « Champion » reste un signal de distinction.

---

### Résumé express

1. Exportez vos 4 800 clients et leurs commandes.
2. Scoring RFM : dernier achat < 60 j + 3+ commandes/12 mois + montant > médiane = **Champions** (~500 clients).
3. Créez 3 listes : Champions / Fidèles stables / À nourrir.
4. Envoyez une offre privée **séquentielle** (champions d'abord, 15–20 % ou cadeau, deadline 10 jours, accès anticipatif en bonus).
5. Mesurez à J14 et J30, puis automatisez le recalcul trimestriel.
