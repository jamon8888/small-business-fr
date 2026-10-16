Bonjour,

Bonne question — « piloter la boutique » couvre bien cinq domaines distincts (catalogue, stock, commandes, clients, ventes), et il y a un bon point de départ : **la connexion à la boutique**. Voici où on en est et par où je vous propose de commencer.

## 1. État des lieux — ce qui est prêt, ce qui manque

Avant de toucher quoi que ce soit à ma-boutique.myshopify.com, j'ai vérifié l'environnement :

- **URL de la boutique** : connue (ma-boutique.myshopify.com) ✅
- **Serveur MCP `shopify-dev-mcp`** : non disponible dans mon environnement actuel ❌
- **Connecteur `shopify` (repli en lecture)** : non disponible ❌
- **Token d'application et scopes** : inconnus ❌
- **Contexte boutique** : absent — je n'ai encore lu aucune donnée de votre boutique

Concrètement : je ne peux pas encore parler à votre boutique. Il n'y a donc pas de chiffres à vous donner pour l'instant, et je ne vais pas en inventer. **La première étape est donc la connexion** — c'est ce qui débloque tout le reste, y compris les cinq domaines que vous visez.

## 2. Plan proposé (à votre validation avant toute action)

**Étape 1 — Connecter la boutique**
Je vous guide pour :
1. Créer une application personnalisée dans l'admin Shopify (Paramètres → Applications → Développement → « Créer une application personnalisée »),
2. Y accorder les scopes de lecture nécessaires : produits, commandes, stock, clients, rapports — et les scopes d'écriture correspondants seulement si vous le souhaitez,
3. Installer le toolkit AI de Shopify (3 options : plugin complet, serveur MCP seul, ou skills seuls).

Votre token restera dans votre environnement : jamais dans un fichier, jamais dans nos échanges.
**Repli si l'installation n'est pas possible chez vous** : un mode « coller » reste disponible — vous exportez les données de l'admin (CSV) et vous me les transmettez, je les traite en lecture. C'est moins fluide mais ça fonctionne dès aujourd'hui.

**Étape 2 — Diagnostic de base (lecture seule)**
Une passe de lecture unique sur les cinq domaines, pour poser un état de base chiffré :
- **Catalogue** : nombre de produits/variantes, collections, produits inactifs, prix et fiches (SEO) à défaut ;
- **Stock** : niveaux par produit, références en rupture ou quasi-rupture, risque de surstock ;
- **Commandes** : volume récent, statuts bloqués (payées non expédiées, expédition en attente), retours/remboursements en cours ;
- **Clients** : base clients, segmentation (nouveaux vs récurrents), concentration du chiffre par client ;
- **Ventes** : CA, panier moyen, KPIs de la boutique sur la période récente — avec la définition de chaque ratio de marge que j'indiquerai.

Cette étape est **stricte en lecture** : aucune modification de la boutique.

**Étape 3 — Rythme de pilotage**
Sur la base du diagnostic, je vous propose un plan d'action priorisé par domaine, puis un rythme de suivi :
- point régulier des indicateurs (lecture libre sur demande) ;
- toute **écriture** (prix, tags, remises, expédition, thème…) vous est soumise avec le détail exact de ce qui va changer, et n'est exécutée qu'après votre validation ;
- toute action **destructive** (suppression, annulation, remboursement) fait l'objet d'une double confirmation avec le montant affiché.

## 3. Ce dont j'ai besoin de votre part

1. **Valider ce plan** (ou me dire ce que vous voulez ajuster — par exemple si vous voulez d'abord l'un des cinq domaines uniquement) ;
2. **Réserver 15 minutes** pour la création de l'application personnalisée dans votre admin, je vous accompagne pas à pas ;
3. Me confirmer la **période de référence** pour le diagnostic (30 jours glissants, 90 jours, depuis l'ouverture ?).

Dès votre validation, je lance l'étape 1 et je reviens vers vous pour le diagnostic. Par où je commence ?
