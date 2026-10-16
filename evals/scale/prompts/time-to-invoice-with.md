Tu es un assistant pour dirigeants de PME françaises.
Le skill suivant est à ta disposition — suis-le pour répondre :

### SKILL.md
---
name: time-to-invoice
description: >
  Facture le temps passé, les jalons ou le forfait : lit le relevé de temps
  (CSV, calendrier, export), contrôle les taux horaires du devis, les
  dépassements, le temps non facturable, déduit les acomptes déjà facturés,
  applique la mention de TVA (encaissement ou débits).
  [EN] Invoices time-and-materials, milestones, or fixed fee.
---

> Language rule: see `shared/language.md`.

# time-to-invoice

## Contrôles
1. Taux horaires cohérents avec le devis
2. Dépassements de budget signalés
3. Temps non facturable exclu
4. Acomptes déjà facturés déduits
5. Mention de TVA : encaissement ou débits, selon l'option

## Sortie
Projet de facture (via devis-facture-fr).

## Validation
Émission.


---

Demande de l'utilisateur :
Relevé de temps : 12 h sur l'intervention, le devis prévoyait 10 h à 650 €/h. Le client a validé le démarrage. Je facture ?

Réponds en français, de manière complète et actionnable, comme un assistant de direction pour PME.
Écris ta réponse complète dans le fichier /Users/macbook/small/evals/scale/runs/time-to-invoice/with.md (crée-le).
Quand c'est fait, réponds uniquement : OK
