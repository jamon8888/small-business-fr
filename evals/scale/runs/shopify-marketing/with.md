# Promo collection « Automne » — -15 % sur 10 jours

Plan de lancement complet, prêt pour validation en une passe.

---

## 1. Diagnostic — le levier et le segment

| Question | Réponse |
|---|---|
| Objectif | Faire décoller les ventes de la collection « Automne » |
| Levier retenu | **Code de remise à -15 %** limité à la collection « Automne » |
| Pourquoi ce levier | Un code plafonné est le levier le plus traçable (on attribue chaque vente à la promo) et le plus facile à stopper à J+7. La livraison gratuite ne serait pertinente que si le panier moyen est sous le seuil de rentabilité du transport — à vérifier, mais hors périmètre de cette promo. |
| Segment ciblé | **Clients existants** (liste e-mail boutique) en priorité — ils ont le plus haut taux de conversion ; visiteurs du site en appui (code affiché sur la collection et la page d'accueil). |
| Garde-fou respecté | ⚠️ **Une seule campagne active par objectif** : avant de créer, vérifiez dans Shopify qu'aucune autre promo ne cible « décoller les ventes » (remises actives dans *Boutique en ligne → Remises*). S'il en existe une, on l'arrête d'abord. |

---

## 2. L'offre — rédigée

| Élément | Valeur |
|---|---|
| Type | Remise en pourcentage : **-15 %** |
| Forme | Code `AUTUMNE15` |
| Périmètre | Produits de la collection « Automne » uniquement (pas le reste du catalogue) |
| Cumul | Non cumulable avec d'autres remises ; non applicable aux produits déjà en solde |
| **Plafond (obligatoire)** | **500 utilisations MAX** ET expiration à la fin de la période — aucun code illimité |
| Dates | **Samedi 17 octobre 2026, 9 h 00 → Dimanche 26 octobre 2026, 23 h 59** (10 jours) |
| Visibilité du code | Bannière sur la page collection « Automne » + page d'accueil + e-mails (ci-dessous) |

---

## 3. Contrôle de la marge

Méthode : la remise coûte 15 % du prix de vente TTC sur chaque produit éligible.

- **Hypothèse à vérifier avec vos chiffres réels** (via *Shopify → Analyse → Marges* ou vos prix d'achat) : marge brute de la collection ≈ **45 %** (standard mode/produits PME).
- Marge brute après remise : 45 % × 0,85 ≈ **38 %** → **au-dessus du seuil d'alerte (30 %) : aucune alerte, validation possible.**

Règle : si votre marge brute réelle sur la collection est **inférieure à ~35 %**, la remise passe sous 30 % de marge → je vous alerte avant de créer quoi que ce soit (règle : jamais de remise sous le coût de revient sans alerte explicite).

**Coût estimé de la remise** (scénario moyen, à recalibrer avec vos données) :

| Hypothèse | Valeur |
|---|---|
| Panier moyen collection | 65 € (benchmark e-commerce France 2025 : 62 € — Fevad) |
| Uses attendus sur 10 jours | 200 (sur un plafond de 500) |
| **Coût de la remise** | 200 × 65 € × 15 % ≈ **1 950 €** |
| CA généré attendu | ≈ 13 000 € |

---

## 4. Validation — en une passe

> **À valider en bloc :** code `AUTUMNE15`, -15 % sur la collection « Automne » uniquement, non cumulable, **plafonné à 500 uses**, du **17/10/2026 9 h 00** au **26/10/2026 23 h 59**, bannière sur la collection + page d'accueil, 2 e-mails aux clients existants (J1 et J8), mesure à **J+7 (mercredi 24/10)**.

Répondez :
1. ✅ **Validé tel quel** → je crée tout dans la boutique.
2. 🔧 **Modifiez X** (valeur, dates, plafond, code) → je corrige puis recrée.
3. 📊 **Donnez-moi la marge brute réelle de la collection et la taille de votre liste e-mail** → je recalcule le contrôle de marge et le plafond avant de créer.

---

## 5. Création dans la boutique (à exécuter après validation)

**a) Le discount** — *Shopify Admin → Boutique en ligne → Remises → Créer une remise* :
1. Type : **code promo** → `AUTUMNE15`
2. Valeur : **15 % de réduction**, applicabilité : **produits → collection « Automne »**
3. Non cumulable avec d'autres remises
4. Plafond : **limiter à 500 utilisations**
5. Période de validité : 17/10/2026 09:00 → 26/10/2026 23:59
6. **Relire la fiche créée** (périmètre, dates, plafond) avant d'activer — vérifier avec un test panier à 0,01 € sur un produit de la collection que la remise s'applique, puis vider le panier de test.

**b) La campagne visuelle** :
- Bannière sur la page collection « Automne » : « Automne à -15 % — code AUTUMNE15 — jusqu'au 26 octobre »
- Bloc bannière sur la page d'accueil (même message, durée identique)
- Pas d'annonce publique du code avant le 17/10 à 9 h (le code n'est actif que dans la fenêtre ci-dessus)

**c) Les e-mails** — je ne les envoie pas ; la liste et les copies ci-dessous vous sont livrées **prêtes à coller dans votre outil e-mail** :

**E-mail 1 — J1 (samedi 17/10, 9 h 30) — segment : clients existants**
- Objet : `Votre code Automne : -15 % dès ce matin`
- Corps : « L'automne est arrivé. Pendant 10 jours seulement, toute la collection Automne est à -15 % avec le code **AUTUMNE15**. Il vous attend sur la page collection. Offre limitée : le code s'arrête le 26 octobre à minuit. → [Découvrir la collection Automne] »

**E-mail 2 — J8 (jeudi 22/10, 18 h) — segment : clients existants n'ayant pas utilisé le code**
- Objet : `Encore 48 h pour -15 % sur l'Automne`
- Corps : « Votre code **AUTUMNE15** expirera dimanche 26 octobre à minuit. -15 % sur toute la collection Automne, jusqu'à épuisement des 500 utilisations. → [Utiliser mon code] »

---

## 6. Mesure à J+7 — mercredi 24 octobre 2026

Extraction dans *Shopify → Analyse* (ou `shopify-reporting`) pour la journée 17→24/10, filtre code `AUTUMNE15` :

| Indicateur | Cible | Règle de décision |
|---|---|---|
| Uses du code | ≥ 100 (50 % du total attendu) | < 50 uses → **arrêter l'e-mail J8 et la bannière d'accueil**, garder uniquement la collection |
| Taux de conversion (paniers code / visites collection) | ≥ 2,5 % | < 1,5 % → **arrêter la promo à J+7**, ne pas attendre la fin des 10 jours |
| Panier moyen des ventes promo | ≥ 60 € | < 45 € → vérifier que la remise n'érode pas la marge nette |
| Marge nette des ventes promo | ≥ 30 % | < 30 % → **arrêter immédiatement** (règle de marge) |

Garde-fou : **on arrête ce qui ne marche pas** — le J+7 est le point de décision, pas le 26/10. Un arrêt anticipé ne coûte rien : le code se désactive en 1 clic dans l'admin.

---

### Prochaine action
Confirmez-moi : **marge brute réelle de la collection + taille de votre liste e-mail** (si vous les avez), et votre feu vert « validé tel quel ». Dès réception, je crée le discount et la bannière, et je vous livre la liste e-mail segmentée prête à envoyer.
