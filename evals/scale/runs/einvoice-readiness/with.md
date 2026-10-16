# Audit de préparation — facturation électronique (B2B + B2G)

**Objectif** : situer votre position au 15 octobre 2026 et dresser la checklist d'écarts datée avant vos deux échéances. Je ne certifie pas la conformité : il s'agit d'une checklist d'écarts à date, à faire valider par votre PA (Qonto) et votre expert-comptable.

## 1. Où vous en êtes sur le calendrier

| Échéance | Ce qui vous concerne |
|---|---|
| 1er sept. 2026 — **déjà passée** | **Réception** des e-factures : obligatoire depuis le 1er sept. 2026 pour toutes les entreprises assujetties, PME comprises. C'est votre point le plus urgent. |
| 1er sept. 2027 | **Émission** de vos factures B2B via une plateforme agréée + **e-reporting** à la DGFiP. |
| Déjà en vigueur | **B2G** : vos factures aux personnes publiques passent par le **PFP** (portail public de facturation, famille Chorus Pro), pas par Qonto. |

## 2. Plateforme agréée : Qonto est sur le bon rail

- Qonto est **immatriculée DGFiP** comme plateforme agréée : c'est le bon opérateur pour l'émission, la réception et l'e-reporting.
- **Action n° 1** : vérifier dans l'administration Qonto que la **réception** des e-factures (Factur-X et UBL) est activée pour votre compte. C'est le point qui vous concerne déjà (obligation de réception depuis le 1er sept. 2026).
- **Action n° 2** : vérifier que l'**émission** e-facture est activée (elle peut être activée en amont de votre échéance du 1er sept. 2027 pour tester en conditions réelles).
- Demander à Qonto la **liste des fonctions activables** : émission, réception, e-reporting.

## 3. B2G : vos clients publics ne passent pas par Qonto

Vous facturez « quelques clients du secteur public » : ces factures **doivent partir depuis le PFP** (portail public de facturation), au format Factur-X, **profil EN 16931 minimum** [à vérifier : profil exact imposé par le PFP pour les petits vendeurs].

- **Action n° 3** : si ce n'est pas déjà fait, vous **immatriculer sur le PFP** (gratuit, sans API). Le PFP est un circuit distinct de votre PA : Qonto ne route pas vos factures vers vos clients publics.
- Les factures B2G au PFP sont déjà **obligatoires aujourd'hui** pour les vendeurs de personnes publiques (en vigueur depuis 2020) — à confirmer précisément avec le PFP selon votre situation.

## 4. Checklist d'écarts à date (15 octobre 2026)

| # | Point | Statut | À faire |
|---|---|---|---|
| 1 | Réception e-factures (obligatoire depuis le 1er sept. 2026) | **À vérifier** | Activer la réception Factur-X + UBL dans Qonto |
| 2 | Émission via PA (échéance 1er sept. 2027) | En préparation | Activer l'émission e-facture dans Qonto |
| 3 | B2G via PFP (déjà en vigueur) | **À vérifier** | S'immatriculer sur le PFP et y facturer les clients publics |
| 4 | e-reporting DGFiP (à compter du 1er sept. 2027) | À activer plus tard | Activer sur Qonto : données de facture, de transaction (ventes B2C sans facture) et de paiement. [à vérifier : périmètre exact du e-reporting pour une TPE/PME au 1er sept. 2027 — demander à Qonto et à votre expert-comptable.] |
| 5 | Mentions EN 16931 sur vos factures | **À vérifier facture par facture** | Voir point 5 ci-dessous |

## 5. Mentions à contrôler sur vos factures (complétude EN 16931)

Pour chaque type de facture que vous émettez, vérifier la présence de ces champs — **un champ manquant est un écart nommé, jamais un zéro implicite** :

- **N° de facture et date d'émission**
- **Échéance de paiement**
- **SIRET du vendeur** (le vôtre)
- **N° de TVA vendeur et acheteur**
- **Moyen de paiement et IBAN** (si virement)
- **Total facture et montant à payer**

Points spécifiques à votre situation :

- **SIRET / n° TVA des clients** : un client sans SIRET ni n° de TVA est un **écart à nommer**, pas à inventer. Faire la liste de vos clients et identifier ceux pour lesquels il manque des identifiants (contact client pour les compléter, ou mention explicite du cas).
- Si vous vendez des biens avec livraison : ajouter la **nature du bien/service** par ligne et l'**adresse de livraison** (distincte du facturation).
- En cas de **débits** : vérifier le traitement de l'option TVA.

Le profil d'émission à viser : **EN 16931 (confort)** — MINIMUM et BASIC ne suffisent pas.

## 6. Valider avant de basculer

- **Fichier isolé** : tester la validité d'une facture Factur-X sur **Ecosio** (gratuit, en ligne) ; VeraPDF pour le conteneur PDF/A-3.
- **En conditions réelles** : utiliser l'**environnement de préproduction/test de Qonto** une fois l'émission activée.
- Le XML Factur-X est **émis par Qonto** depuis vos données de facture : vous n'avez pas à produire de XML vous-même — votre travail, c'est la **complétude des données source** (point 5).

## Récapitulatif des actions, par ordre

1. **Maintenant** : activer la **réception** e-factures dans Qonto (obligation dépassée).
2. **Maintenant** : traiter le circuit **PFP** pour vos clients publics (immatriculation, facturation au format Factur-X EN 16931 minimum via le PFP).
3. **Avant le 1er sept. 2027** : activer l'**émission** dans Qonto, contrôler les mentions EN 16931 sur vos factures types, valider un échantillon sur Ecosio puis en préproduction Qonto.
4. **Au 1er sept. 2027** : activer l'**e-reporting** sur Qonto (périmètre à confirmer avec Qonto et votre expert-comptable).
5. **Pilotage** : refaire cette checklist à 3 mois pour suivre la réduction des écarts.
