# Shopify — AI Toolkit

Source unique de vérité pour parler à la boutique. Documentation officielle :
https://shopify.dev/docs/apps/build/ai-toolkit

## Ce que c'est
L'AI Toolkit officiel de Shopify apporte trois couches :
1. Le serveur MCP `shopify-dev-mcp` : documentation à jour et surfaces
   développeur accessibles à l'agent.
2. Le skill `shopify` : couvre GraphQL Admin API, Shopify Functions, Polaris,
   Liquid, Hydrogen et Shopify CLI. L'agent ne charge la guidance d'une
   surface que quand la tâche l'exige.
3. Le plugin `shopify-ai-toolkit` (mise à jour automatique).

## Installation (3 options)
- Plugin complet (Claude Code) :
  `claude plugin install shopify-ai-toolkit@claude-plugins-official`
- Serveur MCP seul :
  `claude mcp add --transport stdio shopify-dev-mcp -- npx -y @shopify/dev-mcp@latest`
- Skills seuls : `npx skills add Shopify/shopify-ai-toolkit`
  (puis `npx skills update` pour rester à jour)

## Serveur MCP dans ce plugin
Déclaré dans `.mcp.json` :
```json
"shopify-dev-mcp": {"command": "npx", "args": ["-y", "@shopify/dev-mcp@latest"]}
```
Si le serveur est indisponible (pas de Node, pas de réseau) : repli sur le
connecteur `shopify` déjà présent (lecture) ou sur le mode « coller » —
l'export CSV de l'admin Shopify est collé ou déposé, les skills le traitent.
On le dit explicitement, on ne simule jamais.

## Pilote de la boutique : Shopify CLI (`store auth` / `store execute`)
Le canal principal du toolkit pour agir sur la boutique :
- `shopify store auth --store <domaine> --scopes <scopes>` — authentifie
  la session CLI sur la boutique, avec les scopes minimaux validés.
- `shopify store execute --store <domaine> --query '...'` — exécute du
  GraphQL Admin :
  - lecture seule → sans `--allow-mutations` ;
  - mutation → `--allow-mutations` obligatoire ;
  - `--query-file` pour les longues requêtes.
- Scopes : le minimum validé (read_products, write_products,
  read_inventory, write_inventory, read_reports…) — jamais de scope large
  par confort.
- Le GraphQL est validé contre l'Admin API avant exécution : le toolkit
  embarque les schémas jusqu'à la version 2026-10.

Alternative hors CLI : token d'application personnalisée (Admin → Apps →
Développement) sur `https://<store>.myshopify.com/admin/api/<version>/graphql.json`.
Le token reste dans l'environnement du dirigeant : jamais dans un fichier
du plugin, jamais dans la conversation.

## ShopifyQL (rapports)
Ventes, commandes, revenu, conversion, tendances : les questions
d'analyse se posent en **ShopifyQL** (langage type SQL de Shopify),
exécuté via le champ `shopifyqlQuery` de l'Admin GraphQL dans le même
flux `store execute` (lecture seule, scope `read_reports`). C'est le
moteur du skill `shopify-reporting`.

## Confidentialité
Les scripts du toolkit envoient par défaut des télémétries d'usage à
shopify.dev. Désactivation : `OPT_OUT_INSTRUMENTATION=true` ou un fichier
vide `~/.config/shopify-ai-toolkit/opt-out`. À proposer au dirigeant à
l'installation.

## Politique lecture / écriture
- Lecture (produits, commandes, stock, clients, rapports) : libre sur demande.
- Écriture (prix, tags, remises, expédition, thème) : toujours validée
  avant, en une passe, avec le diff de ce qui va changer.
- Destructif (suppression, annulation, remboursement) : double confirmation
  + montant concerné affiché.

## Le cluster
`shopify-hub` orchestre 8 skills couvrant tous les domaines de la boutique.
Les tâches développeur (apps, thèmes, fonctions) vont à `shopify-builder`.
