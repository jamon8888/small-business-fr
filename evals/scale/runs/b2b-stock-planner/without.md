# Recommandation de commande — mois prochain

## Méthode

Pour chaque ligne, le besoin de commande = **carnet de commandes + pipeline pondéré par probabilité + couverture de sécurité (3 semaines de ventes moyennes) − stock disponible actuel**.

> ⚠️ Vous n'avez pas communiqué votre stock actuel ni vos stocks de sécurité par ligne. Les chiffres ci-dessous supposent un stock à zéro : retirez simplement votre stock disponible pour obtenir la commande nette.

## Calculs détaillés

| Ligne | Carnet | Pipeline pondéré | Sécurité (3 sem.) | Besoin total |
|-------|--------|------------------|-------------------|--------------|
| **A** | 40 | 2 × 70 % = 1,4 | 30/mois × 0,75 = 22,5 | **63,9 → 64** |
| **B** | 15 | 1 × 30 % = 0,3 | 12/mois × 0,75 = 9,0 | **24,3 → 24** |
| **C** | 60 | — | 55/mois × 0,75 = 41,25 | **101,25 → 101** |

## Commande recommandée

- **Ligne A : 64 unités**
- **Ligne B : 24 unités**
- **Ligne C : 101 unités**

## Points d'attention pour la direction

1. **Ligne C est un point de friction** : le carnet (60) dépasse de près de 9 % la vente historique mensuelle (55). C'est un bon signal, mais vérifiez que le réassort de 3 semaines tient — à 55–60 unités/mois, c'est l'article le plus exposé à une rupture.
2. **Ligne B** : le pipeline est faible (1 affaire à 30 %). La recommandation repose surtout sur le carnet + sécurité. Si l'affaire en négociation est perdue, vous restez largement couvert (seuil de 9 unités de sécurité).
3. **Ajustez au stock réel** : si vous avez déjà, par exemple, 20 unités de C en stock, commandez 81 au lieu de 101.
4. **Prochaine itération** : refaites ce calcul mi-mois, car 3 semaines de délai signifient que la demande du mois prochain commencera à se manifester dès maintenant (nouveaux carnets + avancement du pipeline).
