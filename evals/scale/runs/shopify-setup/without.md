# Connexion de votre plugin à ma-boutique.myshopify.com : guide d'installation et de vérification

## 1. Ce qu'il faut installer

### A. Créer l'application Shopify (côté développeur du plugin)
1. **Compte développeur Shopify** : si le plugin est une app interne (usage propre à votre boutique), créez une **application privée** directement depuis l'admin Shopify :
   - `https://ma-boutique.myshopify.com/admin/settings/apps/private`
   - Fournir un nom, activer l'accès en **API GraphQL Admin** (et/ou REST selon le besoin du plugin).
2. **Si le plugin est une app publique** (distribué via l'App Store) : la connexion passe par un flux **OAuth** — vous installez l'app depuis l'App Store, autorisez les permissions, et Shopify génère automatiquement un **access token** (ou, en mode "online", un code d'autorisation à échanger contre un token).

### B. L'access token (la clé du lien)
- **App privée** : token `shpat_...` (Shopify Access Token) généré à la création de l'app. À transmettre au plugin par **variable d'environnement ou fichier de configuration chiffré**, jamais en clair dans le code.
- **App publique / OAuth** : le plugin doit implémenter le flux complet :
  1. Redirection vers `https://ma-boutique.myshopify.com/admin/oauth/install?client_id=...&scope=...&redirect_uri=...`
  2. Vous autorisez, Shopify renvoie un `code` vers votre `redirect_uri`
  3. Le plugin échange le code contre un `access_token` via `POST /admin/oauth/access_token`

### C. Scopes (permissions) à demander — le point le plus important
Pour **piloter le catalogue et les commandes**, l'app doit demander exactement ces scopes (ni plus, pour la sécurité) :

| Scope | Rôle |
|---|---|
| `read_products` | Lire le catalogue |
| `write_products` | Créer/modifier/supprimer produits, variantes, images |
| `read_orders` | Lire les commandes |
| `write_orders` | Modifier les commandes (adresse, statuts, annulation) |
| `read_fulfillments` + `write_fulfillments` | Si le plugin pilote l'expédition |
| `read_customers` | Si le plugin croise commandes et clients |
| `read_shop` | Renseignements de base sur la boutique |

Règle d'or : **principe du moindre privilège**. Ne demander que ce qui est strictement nécessaire — cela accélère aussi la validation Shopify si l'app est publique.

## 2. Ce qu'il faut vérifier après l'installation

### Vérification 1 — Connexion API
- Tester une requête de lecture simple :
  - GraphQL : `query { shop { name } }` vers `https://ma-boutique.myshopify.com/admin/api/2025-01/graphql.json`
  - ou REST : `GET /admin/api/2025-01/products.json?limit=1`
- ✅ Si la boutique renvoie ses données : connexion OK.
- ❌ `401 Unauthorized` → token invalide ou expiré.
- ❌ `403 Forbidden` → token valide mais scope manquant → corriger les scopes et réinstaller.

### Vérification 2 — Version de l'API
- Vérifier que le plugin utilise une **version d'API encore supportée** (Shopify déprecate les versions anciennes à chaque release annuelle : 2024-10, 2025-01, 2025-04, 2025-10…). Un plugin qui pointe vers une version dépréciée fonctionne encore un temps puis casse silencieusement.
- Action : aligner le plugin sur la **dernière version stable** (ex. `2025-10` ou la plus récente disponible au moment de l'installation).

### Vérification 3 — Parité du catalogue
- Exporter 5 à 10 produits de test depuis le plugin et vérifier :
  - titres, descriptions, prix (attention aux décimales et au **arrondis**), monnaie
  - SKU et barcodes (GTIN) — source de vérité : **l'admin Shopify doit rester la source unique** si vous voulez éviter les conflits de synchronisation
  - images (URLs, ordres, image principale)
  - variantes et niveaux de stock
- Vérifier le **sens de la synchronisation** : si le plugin écrit vers Shopify, confirmer qu'une modification faite dans l'admin Shopify remplace bien l'état côté plugin (sinon vous risquez d'écraser des saisies humaines).

### Vérification 4 — Commandes
- Créer une **commande de test** (boutique en mode test/bacsandbox, ou commande réelle de 1 € si impossible) et vérifier :
  - le plugin voit la commande (`orders` en lecture)
  - le plugin peut mettre à jour l'adresse de livraison et le statut
  - les remboursements et annulations remontent correctement
- ⚠️ Ne tester jamais la modification de commandes en production avant d'avoir validé sur commande de test.

### Vérification 5 — Webhooks (si le plugin doit réagir en temps réel)
- Dans l'admin Shopify (`Paramètres → Applications → [votre app] → Webhooks`), vérifier que les événements sont enregistrés :
  - `orders/create`, `orders/updated`, `orders/cancelled`
  - `products/create`, `products/update`, `products/delete`
- **Exiger un secret de signature** : Shopify signe chaque webhook avec HMAC-SHA256. Le plugin doit vérifier la signature `X-Shopify-Hmac-Sha256` sur chaque appel, sinon n'importe qui qui découvre votre URL peut forger des événements.
- Vérifier que l'URL de webhook est en **HTTPS** (obligatoire) et que le plugin répond **`200` en moins de 10 secondes** (traiter la charge en asynchrone, sinon Shopify marque le webhook en échec et espacera les envois).

### Vérification 6 — Limites de débit (rate limits)
- **GraphQL** : système de "throttling" par coût de requête (budget 100 points/second, stocké sur 50). Un plugin qui pousse 500 produits en boucle serrée va être refusé avec des erreurs 429.
- **REST** : 40 requêtes/second par app (10/s en lecture sur certains endpoints).
- Action : vérifier que le plugin implémente du **backoff exponentiel** sur les 429, et que les synchronisations de masse sont paginées (`limit` + `pageInfo`/`next_page` en GraphQL) et espacées.

### Vérification 7 — Sécurité
- [ ] Token stocké hors du code (variable d'env, coffre de secrets)
- [ ] TLS obligatoire sur toutes les requêtes (pas d'HTTP en clair)
- [ ] Scopes au minimum nécessaire (revue de la liste ci-dessus)
- [ ] Journalisation des écritures vers Shopify (qui/quand/quoi) — indispensable pour auditer un désaccord de stock
- [ ] Rotation du token prévue : en cas de fuite ou de changement de fournisseur, régénérer depuis l'admin sans réinstaller

## 3. Checklist récapitulative

| # | Contrôle | Statut |
|---|---|---|
| 1 | App créée (privée ou publique), access token généré | ☐ |
| 2 | Scopes catalogue + commandes demandés et acceptés | ☐ |
| 3 | Requête de lecture `shop` réussie | ☐ |
| 4 | Version d'API supportée | ☐ |
| 5 | Sync catalogue testée sur 5–10 produits | ☐ |
| 6 | Commande de test créée, modifiée, annulée via le plugin | ☐ |
| 7 | Webhooks enregistrés + signature HMAC vérifiée | ☐ |
| 8 | Gestion des 429 / pagination en place | ☐ |
| 9 | Token hors code, HTTPS partout, journal des écritures | ☐ |

## 4. Pièges fréquents à éviter

1. **Double source de vérité** : si le plugin et l'admin Shopify sont tous deux éditables sans règle claire, le stock et les prix vont diverger. Décider explicitement : Shopify = source de vérité, ou le plugin = source de vérité (dans ce cas, les écritures directes dans l'admin doivent être désactivées sur les champs synchronisés).
2. **Monnaie et décimales** : l'API GraphQL exprime les prix en `MoneyV3` (chaîne, ex. `"49.90"`). Un plugin qui travaille en centiens ou en float va créer des arrondis qui s'accumulent.
3. **Tokens en dur** : le token d'une app privée Shopify est un accès total aux scopes de l'app. Le traiter comme un mot de passe.
4. **Oublier le sandbox** : Shopify permet de tester sur une **boutique de développement** (compte développeur gratuit) avant de toucher à `ma-boutique.myshopify.com`. Le faire systématiquement.
5. **Webhooks sans signature** : c'est le trou de sécurité le plus courant sur les intégrations Shopify.

## 5. Prochaines étapes recommandées

1. Créer l'app dans l'admin avec les scopes listés ci-dessus.
2. Configurer le plugin avec le token et la version d'API, en environnement de **développement** d'abord.
3. Faire passer la checklist ci-dessus en mode test.
4. Basculer en production, commencer par la **lecture seule** (24 h de surveillance), puis activer les **écritures catalogue**, puis les **écritures commandes**.
5. Mettre en place une surveillance : alerte si le nombre d'appels 4xx/5xx vers l'API augmente, et journal des dernières écritures consultable.

En résumé : l'installation tient en **une app + un token + les bons scopes** ; la robustesse tient en **webhooks signés, limites de débit gérées, et une source de vérité unique**. Si ces cinq points sont couverts, votre plugin pilotera le catalogue et les commandes de ma-boutique.myshopify.com en production sans incident majeur.
