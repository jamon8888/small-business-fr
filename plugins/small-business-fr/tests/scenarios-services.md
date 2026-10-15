# Scénarios services — §16.1

1. « Qui me doit de l'argent ? » → invoice-chase ; trois relances graduées
   avec pénalités et 40 €, rien d'envoyé sans accord.
2. /preparer-paie --horizon 60 --date-paie 2026-10-30 →
   payroll-prep (mêmes paramètres, aucun calcul social).
3. Mêmes demandes en anglais : comportement d'origine inchangé.
4. Aucune sortie ne contient « Step 1 », « Gate » ni un extrait anglais.
5. SAS à l'IS, TVA trimestrielle : « paie les fournisseurs » → imputation
   PCG, demande de virement groupé Qonto, lien d'approbation, aucun paiement.
6. Micro-entrepreneur : « combien de TVA ? » → franchise en base, distance
   au seuil, pas de CA3.
7. Prestation avec acompte : time-to-invoice déduit l'acompte.
8. renewal-watch : alerte 90 jours avant la date limite ; indice saisi.
