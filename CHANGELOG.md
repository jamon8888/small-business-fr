# Changelog

## v1.2.0-fr.1 — 2026-10-16

### Ajouté
- **Cluster Shopify (9 skills)** — piloter une boutique Shopify complète via
  l'AI Toolkit officiel de Shopify (serveur MCP `shopify-dev-mcp`, skill
  `shopify`, GraphQL Admin API) :
  - `shopify-hub` — point d'entrée, vérifie l'AI Toolkit, route par domaine
  - `shopify-setup` — connexion : installation du toolkit, accès, scopes,
    contexte boutique
  - `shopify-catalog` — produits, variantes, collections, SEO, prix
  - `shopify-orders` — commandes, expédition, retours, remboursements
  - `shopify-inventory` — niveaux par emplacement, transferts, réassort
  - `shopify-customers` — segments, tags, RFM, fidélité
  - `shopify-marketing` — remises, codes, campagnes, mesure J+7
  - `shopify-reporting` — set de 10 rapports (pulse, marge, P&L, TVA…)
  - `shopify-builder` — Flow, Functions, thème (Liquid/Polaris), apps
- `shared/shopify-ai-toolkit.md` — doc unique de vérité, alignée sur le
  repo officiel (verrouillage du workflow réel) : installation du
  toolkit, serveur MCP, **`shopify store auth` / `store execute`**
  (GraphQL Admin, scopes minimaux, `--allow-mutations`), **ShopifyQL**
  pour les rapports, opt-out des télémétries
- Serveur MCP `shopify-dev-mcp` déclaré dans `.mcp.json`
- Routeur : section « Shopify (boutique en ligne) » + 3 règles de
  désambiguïsation (stock / produits / promo)
- **Liens bidirectionnels** : les 12 skills concernés (inventory-planner,
  crm-autopilot, growth-pulse, fulfillment-desk, marketing-monday,
  business-pulse, order-intake, catalog-quote, pricing-desk, ticket-deflector,
  cash-flow-snapshot, report-builder) pointent vers leur équivalent boutique
- `smb-onboard` : la vente en ligne n'est plus « hors périmètre »

### Évaluation de scale étendue
- 71 skills × 2 bras = 142 exécutions (9 cas Shopify ajoutés)
- Avec skill **222/229** (96,9 %) vs sans **197/229** (86,0 %) →
  Δ métier **+25**, comportement **+7**
- Cluster Shopify : **26/27 avec vs 22/27 sans (Δ +4)**, aucun skill en négatif

## v1.1.1-fr.1 — 2026-10-16

### Modifié
- **3 skills affinés** après l'évaluation de scale (avec / sans skill) — ils
  étaient les seuls en négatif sur le score métier :
  - `pricing-desk` : stub de 738 car. complété — section « quand la marge bouge »
    (impact chiffré avant/après + leviers classés : répercuter, renégocier le
    prix d'achat, réduire un poste, arrêter/déclasser)
  - `build-agent` : « Contrat de réponse » obligatoire — proposer le déclencheur
    (nom + horaire) et poser les questions qui capturent chaque étape / les données
  - `marketing-monday` : brique **SEO local** obligatoire dans le plan de semaine
    (fiches Google Business, avis, actions locales)

### Ajouté
- **Évaluation de scale publiée** : `evals/scale/` (62 skills × 2 bras = 124
  exécutions, scoring déterministe 100 % regex) + `evals/REPORT.md`
  - Résultat : avec skill **196/202** métier vs sans **175/202** (Δ +21) ;
    comportement 70/125 vs 63/125 (Δ +7)
  - Plus gros gains : build-connector, crm-autopilot, month-end-prep (+2)

## v1.1.0-fr.1 — 2026-10-15

### Ajouté
- **Facturation électronique complète** : `einvoice-readiness` réécrit avec un
  mode **audit** (plateforme agréée, réception, B2G via PFP, e-reporting,
  mentions) et un mode **préparation de l'émission** (complétude des champs
  EN 16931 du Factur-X)
- Référentiel `einvoice-readiness/reference/facture-electronique-fr.md` :
  calendrier officiel vérifié le 2026-10-15 (impots.gouv.fr), plateformes
  agréées vs solutions compatibles, profils Factur-X, champs BT obligatoires
- Routeur : les demandes « Factur-X », « plateforme agréée », « PFP » routent
  vers `einvoice-readiness`

### Modifié
- `calendrier-fiscal-fr` : la ligne facturation électronique est confirmée
  (réception 09/2026, émission GE/ETI 09/2026, PME 09/2027) — plus de
  « à revérifier »
- `devis-facture-fr` : renvoi vers `einvoice-readiness` pour le Factur-X au
  lieu de « pas de Factur-X en v1 »

## v1.0.0-fr.1 — 2026-10-15

### Ajouté
- Édition française complète du plugin `small-business` d'Anthropic
  (v1.35.1) : **65 skills, 39 commandes**, 167 fichiers traduits
  (~174 000 mots)
- 24 connecteurs dont les français : **Qonto, Pennylane, Sendcloud**
- Droits français : article L441-10 / D441-5 (indemnité de recouvrement
  40 €), L624-16 (réserve de propriété), calendrier fiscal FR, Bloctel,
  facturation électronique
- 7 documents partagés traduits (sécurité des contenus non fiables,
  « l'absent n'est pas zéro », neutralité des connecteurs, style d'artifact…)
- Porte de qualité : `production_check.py` (11 contrôles) + `verify_fr.py`
  (parité structurelle) + lint du plugin
- Marketplace installable sur Claude Code, Cowork, Claude Desktop

### Retiré (skills US sans équivalent FR)
- `tax-season-organizer`, `grant-rfp-writer`
