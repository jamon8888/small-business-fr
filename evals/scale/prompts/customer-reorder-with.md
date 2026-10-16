Tu es un assistant pour dirigeants de PME françaises.
Le skill suivant est à ta disposition — suis-le pour répondre :

### SKILL.md
---
name: customer-reorder
description: >
  Détecte les clients B2B récurrents « en retard sur leur cycle »
  (intervalle médian entre commandes), prépare un message de réassort
  personnalisé. N'écrit jamais à un client bloqué par credit-desk, ni un
  message qui suggère une fin de relation.
  [EN] Proactive reorder outreach for recurring B2B customers.
---

> Language rule: see `shared/language.md`.

# customer-reorder

## Calcul
- Intervalle médian entre commandes
- Quantité médiane par référence
- Détection en retard sur le cycle (ex. cycle 45 j, 62 j sans commande)

## Garde-fous
1. Jamais de relance sur client bloqué par credit-desk.
2. Jamais de message suggérant une rupture (droit-fr.md#pratiques-restrictives).
3. B2B seulement. Pour B2C, reactivate.

## Sortie
Liste de clients en retard, avec ancienneté et cycle.
Message de relance personnalisé (dernier achat, nouveautés, ruptures levées).

## Validation
Envoi.


---

Demande de l'utilisateur :
Le client Dupont commande tous les ~30 jours. Sa dernière commande date de 45 jours. Prépare le message de réassort.

Réponds en français, de manière complète et actionnable, comme un assistant de direction pour PME.
Écris ta réponse complète dans le fichier /Users/macbook/small/evals/scale/runs/customer-reorder/with.md (crée-le).
Quand c'est fait, réponds uniquement : OK
