# Benchmark de scale — small-business-fr

Évaluation de scale sur les 62 skills non couverts par le pilot (invoice-chase, close-month, tva-pilot). Un cas par skill, deux bras (with_skill / without_skill). Toutes les assertions sont déterministes (regex) : `assertions` = justesse métier (garde-fous de régression), `behaviour` = comportements qui distinguent le skill (non-action explicite, pas de source inventée). common_behaviour s'ajoute aux behaviour de chaque cas.

| Configuration | Runs | Métier (domain) | Comportement (behaviour) | Mots/moy.
|---|---|---|---|---|
| avec skill | 62 | 196/202 | 70/125 | 887 |
| sans skill | 62 | 175/202 | 63/125 | 963 |

## Par skill (avec skill − sans skill)

| Skill | Métier avec | Métier sans | Δ métier | Comport. avec | Comport. sans | Δ comport. |
|---|---|---|---|---|---|---|
| ad-manager | 3/3 | 3/3 | +0 | 2/2 | 1/2 | +1 |
| aides-et-marches-fr | 3/3 | 2/3 | +1 | 1/2 | 1/2 | +0 |
| ap-processor | 2/4 | 2/4 | +0 | 2/2 | 1/2 | +1 |
| b2b-stock-planner | 2/3 | 2/3 | +0 | 1/2 | 1/2 | +0 |
| brand-style | 3/3 | 3/3 | +0 | 1/2 | 1/2 | +0 |
| build-agent | 3/3 | 3/3 | +0 | 1/2 | 1/2 | +0 |
| build-connector | 3/3 | 1/3 | +2 | 2/2 | 1/2 | +1 |
| business-pulse | 2/3 | 2/3 | +0 | 1/2 | 1/2 | +0 |
| calendrier-fiscal-fr | 4/4 | 4/4 | +0 | 1/2 | 1/2 | +0 |
| call-list | 3/3 | 3/3 | +0 | 2/2 | 1/2 | +1 |
| canva-creator | 3/3 | 3/3 | +0 | 1/2 | 1/2 | +0 |
| cash-flow-snapshot | 4/4 | 4/4 | +0 | 1/2 | 1/2 | +0 |
| catalog-quote | 4/4 | 4/4 | +0 | 1/2 | 1/2 | +0 |
| content-strategy | 3/3 | 2/3 | +1 | 1/2 | 1/2 | +0 |
| contract-review | 4/4 | 3/4 | +1 | 2/2 | 1/2 | +1 |
| credit-desk | 3/3 | 3/3 | +0 | 1/2 | 1/2 | +0 |
| crm-autopilot | 3/3 | 1/3 | +2 | 1/2 | 1/2 | +0 |
| customer-reorder | 3/3 | 3/3 | +0 | 1/2 | 1/2 | +0 |
| devis-facture-fr | 4/4 | 3/4 | +1 | 1/2 | 1/2 | +0 |
| dossier-expert-comptable | 3/3 | 2/3 | +1 | 1/2 | 1/2 | +0 |
| einvoice-readiness | 4/4 | 4/4 | +0 | 1/2 | 1/2 | +0 |
| fulfillment-desk | 4/4 | 4/4 | +0 | 1/2 | 1/2 | +0 |
| grow-pipeline | 3/3 | 3/3 | +0 | 1/2 | 2/2 | -1 |
| growth-pulse | 2/2 | 2/2 | +0 | 1/2 | 1/2 | +0 |
| hiring-screener | 3/3 | 3/3 | +0 | 1/2 | 1/2 | +0 |
| inbox-manager | 3/3 | 3/3 | +0 | 1/2 | 1/2 | +0 |
| intra-eu-export-check | 4/4 | 3/4 | +1 | 1/2 | 1/2 | +0 |
| inventory-planner | 3/3 | 2/3 | +1 | 1/2 | 1/2 | +0 |
| job-post-builder | 4/4 | 4/4 | +0 | 1/2 | 1/2 | +0 |
| lead-finder | 3/3 | 3/3 | +0 | 1/2 | 1/2 | +0 |
| lead-triage | 3/3 | 2/3 | +1 | 1/2 | 1/2 | +0 |
| marketing-monday | 3/3 | 3/3 | +0 | 1/2 | 1/2 | +0 |
| micro-entrepreneur | 3/3 | 3/3 | +0 | 1/2 | 1/2 | +0 |
| monday-brief | 4/4 | 3/4 | +1 | 1/2 | 1/2 | +0 |
| month-end-prep | 3/3 | 1/3 | +2 | 1/2 | 1/2 | +0 |
| order-intake | 4/4 | 4/4 | +0 | 1/2 | 1/2 | +0 |
| outreach-composer | 3/3 | 1/3 | +2 | 1/2 | 1/2 | +0 |
| pay-the-bills | 3/3 | 3/3 | +0 | 1/2 | 1/2 | +0 |
| payroll-prep | 4/4 | 4/4 | +0 | 1/2 | 1/2 | +0 |
| pricing-desk | 4/4 | 4/4 | +0 | 1/2 | 1/2 | +0 |
| product-compliance | 3/3 | 3/3 | +0 | 1/2 | 1/2 | +0 |
| proposal-builder | 3/3 | 3/3 | +0 | 1/2 | 1/2 | +0 |
| purchase-desk | 3/3 | 2/3 | +1 | 1/2 | 1/2 | +0 |
| quote-followup | 4/4 | 4/4 | +0 | 1/2 | 1/2 | +0 |
| reactivate | 3/3 | 3/3 | +0 | 1/2 | 1/2 | +0 |
| renewal-watch | 3/3 | 3/3 | +0 | 1/2 | 1/2 | +0 |
| report-builder | 3/3 | 2/3 | +1 | 1/2 | 1/2 | +0 |
| report-pack | 3/3 | 3/3 | +0 | 1/2 | 1/2 | +0 |
| restock | 2/3 | 2/3 | +0 | 1/2 | 1/2 | +0 |
| review-reputation | 3/3 | 3/3 | +0 | 1/2 | 1/2 | +0 |
| seo-ai-visibility | 3/3 | 3/3 | +0 | 2/2 | 1/2 | +1 |
| smb-onboard | 2/3 | 2/3 | +0 | 1/3 | 1/3 | +0 |
| smb-router | 3/3 | 3/3 | +0 | 2/2 | 1/2 | +1 |
| social-content-engine | 3/3 | 2/3 | +1 | 2/2 | 1/2 | +1 |
| speed-to-lead | 3/3 | 3/3 | +0 | 1/2 | 1/2 | +0 |
| stock-count-cutoff | 4/4 | 4/4 | +0 | 1/2 | 1/2 | +0 |
| tax-prep | 3/3 | 3/3 | +0 | 1/2 | 1/2 | +0 |
| ticket-deflector | 3/3 | 3/3 | +0 | 1/2 | 1/2 | +0 |
| time-to-invoice | 3/3 | 3/3 | +0 | 1/2 | 1/2 | +0 |
| verifier-tiers | 3/3 | 2/3 | +1 | 1/2 | 1/2 | +0 |
| visit-report | 4/4 | 4/4 | +0 | 1/2 | 1/2 | +0 |
| working-capital | 3/3 | 3/3 | +0 | 1/2 | 1/2 | +0 |
