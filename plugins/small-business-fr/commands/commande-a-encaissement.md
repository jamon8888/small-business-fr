---
description: Chaîne commande-à-encaissement — devis → commande → crédit → expédition → facture → encaissement
argument-hint: "[--du AAAA-MM-JJ] [--au AAAA-MM-JJ] [--client <nom>]"
---
Lance la chaîne `order-to-cash` : `catalog-quote` → `order-intake` →
`credit-desk` → `fulfillment-desk` → `devis-facture-fr` → `invoice-chase`.
Traduis `--du` → `--from`, `--au` → `--to`, `--client` → `--customer`.
Valide à chaque étape. Réponds en français.
