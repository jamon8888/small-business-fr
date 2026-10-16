# Connexion de votre boutique Shopify au plugin

Objectif : rendre le plugin capable de parler à **ma-boutique.myshopify.com** et de piloter le **catalogue** et les **commandes**. Voici, étape par étape, ce qu'il faut installer et vérifier, et ce que je vais consigner.

> Le token d'accès n'est jamais demandé ici : il vit dans votre environnement (variable d'environnement ou profil CLI). Je ne le saisis ni ne le stocke dans aucun fichier du plugin.

---

## 1. État des lieux

Voici le point de départ que j'ai vérifié avant de proposer quoi que ce soit :

| Élément | Statut | Détail |
|---|---|---|
| Boutique cible | ✅ confirmée | `ma-boutique.myshopify.com` |
| Domaine à piloter | ✅ défini | Catalogue + commandes |
| Serveur MCP `shopify-dev-mcp` | ⏳ à installer | Apporte la doc Admin API à jour + surfaces développeur |
| Skill `shopify` | ⏳ à installer | Couvre GraphQL Admin API, CLI, Functions, Liquid, Hydrogen |
| Connecteur `shopify` (repli lecture) | ✅ disponible | Déjà présent, sert de repli en lecture |
| Scopes validés | ⏳ à définir au minimum | `read_products` / `write_products` + `read_orders` (voir §5) |

Le canal principal pour agir sur la boutique est le **Shopify CLI** (`store auth` / `store execute`), adossé au toolkit.

---

## 2. Ce qu'il faut installer (à valider par vous — je ne l'exécute pas)

Le toolkit propose trois formes d'installation. Choisissez selon votre outil IA :

| Option | Pour qui | Commande (à lancer vous-même) |
|---|---|---|
| **A. Plugin complet** — recommandé si vous êtes sur Claude Code | Tout le toolkit : MCP + skills + plugin auto-mis à jour | `claude plugin install shopify-ai-toolkit@claude-plugins-official` |
| **B. Serveur MCP seul** | Vous voulez uniquement la doc Admin API / surfaces dev | `claude mcp add --transport stdio shopify-dev-mcp -- npx -y @shopify/dev-mcp@latest` |
| **C. Skills seuls** | Vous voulez la guidance (GraphQL, CLI, Functions) sans MCP | `npx skills add Shopify/shopify-ai-toolkit` puis `npx skills update` pour rester à jour |

**Mon conseil** : l'option **A** si vous êtes sur Claude Code (c'est la couverture la plus complète pour piloter catalogue + commandes). Dites-moi quel outil IA vous utilisez et j'adapte la commande exacte.

**Télémétrie à désactiver (à valider à l'installation)** : par défaut, les scripts du toolkit envoient des télémétries d'usage à shopify.dev. Pour les couper :
- variable d'environnement `OPT_OUT_INSTRUMENTATION=true`, **ou**
- création d'un fichier vide `~/.config/shopify-ai-toolkit/opt-out`.

Dites-moi si vous voulez que je la désactive — je vous présente la commande, je ne l'exécute pas à votre place.

> Déclaration de dépendance : l'option A et le serveur MCP exigent **Node.js** et **un accès réseau** (les commandes passent par `npx`). Si l'un des deux manque, on bascule sur le repli du §6.

---

## 3. Vérifier l'accès à la boutique

Une fois l'installation faite, je valide l'accès en **deux temps**, lecture seule.

**a) Authentifier la session CLI avec les scopes minimaux :**

```
shopify store auth --store ma-boutique.myshopify.com --scopes read_products
```

**b) Requête en lecture seule pour confirmer le contexte boutique** (nom, devise, pays, plan) :

```
shopify store execute --store ma-boutique.myshopify.com \
  --query '{ shop { name currencyCode countryCode { isoCode } subscription { planName } } }'
```

Ce qui est attendu : une réponse renvoyant le nom de la boutique, sa devise, son pays de facturation et son plan actif.

**Si ça échoue**, je diagnostique dans cet ordre et je re-propose :
1. **Node** — version installée, `npx` disponible ;
2. **CLI** — `shopify` installé et à jour ;
3. **Domaine** — `ma-boutique.myshopify.com` exact (sans `https://`, sans sous-domaine erroné) ;
4. **Scopes** — le scope demandé est-il bien accordé sur l'application.

---

## 4. Ce que je vais consigner dans le contexte boutique

En cas de succès, j'ajoute ces champs dans le bloc `## Business context` **sans renommer les champs existants** :

- **URL boutique** : `ma-boutique.myshopify.com`
- **Plan** : *(relevé par la requête §3)*
- **Devise** : *(relevée par la requête §3)*
- **Pays / devise de facturation** : *(relevée par la requête §3)*
- **Canaux** : *(relevés / à confirmer : Online Store, Points de vente, Marketplace…)*
- **Emplacements / magasins** : *(à confirmer)*

Ces valeurs seront posées telles quelles lors de la validation du §3 — je ne les invente pas.

---

## 5. Scopes à accorder, par domaine

Accordez **le minimum** nécessaire au domaine à piloter. Voici la table de référence :

| Domaine | Lecture | Écriture |
|---|---|---|
| **Catalogue** *(votre besoin)* | `read_products` | `write_products` |
| **Commandes** *(votre besoin)* | `read_orders` | `write_orders` |
| **Stock** | `read_inventory` | `write_inventory` |
| **Clients** | `read_customers` | `write_customers` |
| **Marketing** | `read_discounts`, `read_gift_cards` | `write_discounts`, `write_gift_cards` |
| **Reporting** | `read_reports` | — (lecture seule) |

**Pour votre cas (catalogue + commandes), le minimum à accorder :**

```
read_products, write_products, read_orders
```

- `read_orders` suffit pour **lire** les commandes.
- `write_orders` n'est à ajouter **que si** vous voulez que le plugin **agisse** sur les commandes (validation, expédition, annulation). Les actions destructives (annulation, remboursement) font en outre l'objet d'une **double confirmation** avec le montant affiché avant exécution.

> Je n'accorde **jamais** de scope large « par confort ». Si vous démarrez en lecture seule, on reste sur `read_products, read_orders` et on étend au besoin.

---

## 6. Repli si pas de Node / pas de réseau

Le serveur MCP et les options d'installation reposent sur `npx` (Node + réseau). Si l'un des deux est indisponible, le cluster fonctionne en **mode « coller »** :

- vous exportez les données depuis l'admin Shopify (boutique → Catalogue / Commandes → **Exporter CSV**) ;
- vous collez ou déposez le fichier ;
- les skills le traitent ensuite.

Je vous le dis clairement : **je ne simule jamais** une connexion. En mode « coller », je travaille sur vos exports réels, sans accès en direct.

---

## 7. Ce qui est prêt et à venir

**Prêt après cette séance** : connexion validée, scopes minimaux accords, contexte boutique consigné.

**Domaines que le cluster peut déjà couvrir pour vous** : **catalogue** et **commandes** — lecture et (si `write_*` accordées) écriture validée.

**Prochaine étape proposée** : `shopify-hub` — il orchestre l'ensemble des skills de la boutique et sera votre point d'entrée pour tout le reste (stock, clients, marketing, reporting).

---

## Garde-fous rappelés

- **Token** : jamais en clair dans la conversation, jamais dans un fichier du plugin. Il reste dans votre environnement.
- **Création d'application** : je ne crée **jamais** l'application Shopify à votre place sans vous montrer le formulaire (Admin → Apps → Développement). C'est vous qui la créez, je vous guide.

**Dites-moi** : (1) quel outil IA vous utilisez (pour l'option d'installation exacte), (2) lecture seule ou aussi écriture sur les commandes, (3) désactivons-nous la télémétrie ? Je lance la vérification du §3 dès que l'installation est posée.
