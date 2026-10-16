# Préparation des variables de paie — juillet 2026

## 1. Période de paie (confirmée)

- **Période** : 1er juillet – 31 juillet 2026 (dates incluses)
- **Date de paie** : lundi 3 août 2026 (monte sur la trésorerie d'août, hors charges à payer)
- **Fréquence** : mensuelle
- **Effectif concerné** : 1 salarié à l'horaire, contrat 150 h/mois

Juillet 2026 compte 23 jours ouvrés (lun.–ven.). Le **14 juillet est un mardi**, donc un jour ouvré : selon les usages de votre entreprise, c'est soit un jour de congé payé, soit un jour férié payé. Voir signalement n° 4 ci-dessous.

## 2. Variables collectées

| Variable | Valeur saisie | Relevé |
|---|---|---|
| Heures normales | 150,0 h | Contrat 150 h/mois — conforme |
| Heures supplémentaires | 8,0 h | 158 h travaillées − 150 h de contrat |
| Congés payés | 2 jours = 16,0 h | Hypothèse : 1 jour de congé = 8 h |
| Titres-restaurant | 10 jours | — |

Cohérence du volume : 158 h sur 21 jours de présence (23 jours ouvrés − 2 jours de congé) soit une moyenne de ~7,5 h/jour. C'est un profil plausible, pas un pic.

## 3. Signalements (à traiter avant l'export définitif)

Chacun posé séparément, dans l'ordre des montants en jeu.

**1. Heures supplémentaires (8,0 h) — à confirmer.**
C'est ma première exécution, je n'ai donc pas d'historique de moyenne pour ce salarié. 8 h sur le mois, soit ~1,5 h/semaine, est dans la fourchette habituelle d'un salarié à 150 h qui en fait 158 — mais rien dans le dossier ne l'atteste. Ces 8 h sont-elles réelles et déjà validées, ou y a-t-il un écart de pointage ?
*(Conséquence à valider : les 8 h seront majorées selon la règle en vigueur — voir hypothèse n° 2 ci-dessous. Je ne calcule ni brut ni majoration ici.)*

**2. Solde de congés payés — à vérifier.**
2 jours de congés payés sont déclarés, mais aucun logiciel de paie n'est connecté : je ne peux lire le solde Payfit/Silae. Le solde restant de ce salarié couvre-t-il au moins 2 jours ? Si un logiciel de paie est raccordé, je prendrai le solde depuis la source (jamais une estimation de provision).

**3. Titres-restaurant (10 jours) — règle à confirmer.**
Le salarié a été présent 21 jours sur les 23 ouvrés. 10 titres-restaurant, c'est bien en dessous. Quelle est la règle : 1 titre par journée de présence avec prise de repas sur site ? Si oui, 10 jours paraît bas — c'est la bonne règle appliquée (repas sur site les jours de chantier, par exemple), ou un oubli de saisie ?

**4. Lundi 14 juillet (mardi, jour ouvré) — qualification.**
Le 14 juillet tombe un mardi de travail. Est-il inclus dans les 2 jours de congés payés déclarés, ou traité comme jour férié payé ? Je n'applique aucune politique de majoration de jour férié : aucune règle écrite n'est au dossier, et je n'en suppose pas.

## 4. Hypothèses retenues (à corriger si besoin)

- 1 jour de congé payé = 8 h → 2 jours = 16,0 h.
- Les heures supplémentaires sont calculées **à la semaine** (au-delà de 35 h hebdomadaires), aucune règle du quotient journalier n'étant au dossier. C'est l'hypothèse que j'ai appliquée — corrigez-la en une phrase si votre usage est différent.
- Les congés payés ne comptent pas dans le décompte des heures supplémentaires (règle habituelle, énoncée ici).
- Aucun arrondi appliqué : aucune politique d'arrondi n'est énoncée.

## 5. Export

Fichier créé : **`export-paie-2026-07.csv`** — prêt à importer dans Payfit, Silae, ou à transmettre à l'expert-comptable. Contenu :

```
matricule;nom;prenom;periode_debut;periode_fin;date_paie;heures_normales;heures_supp;conges_payes_jours;conges_payes_heures;titres_restaurant_jours
001;[à confirmer];[à confirmer];2026-07-01;2026-07-31;2026-08-03;150,00;8,00;2;16,00;10
```

Seul point à compléter avant transmission : le nom et prénom du salarié (matricule 001), à reprendre du registre de paie. Si le nom exact est déjà dans votre outil de paie, l'import par matricule suffit.

## 6. Statut

> **1 salarié, 4 variables (heures normales, heures supplémentaires, congés payés, titres-restaurant), prêt pour Payfit.**

4 signalements ouverts (n° 1 à 4). Dites-moi vos réponses et je fige le fichier — c'est le dernier moment où une correction est gratuite avant que ces variables deviennent des bulletins.

## Avertissement

Ce fichier ne contient que des **variables de paie** : heures, absences, congés, titres-restaurant. Aucun calcul de cotisations sociales, aucun net à payer, aucune DSN : cela relève de votre gestionnaire de paie, de Payfit/Silae, ou de votre expert-comptable.
