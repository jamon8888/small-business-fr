# Export des variables de paie — Juillet

**Salarié :** [ID Salarie 0042 — M. DURAND J.]
**Période :** 1er – 31 juillet
**Contrat :** CDI, 150 h / mois
**Salaire de base mensuel :** 2 250,00 € (15,00 € / h)

## 1. Tableau des variables à saisir

| Variable | Valeur | Libellé / destination |
|---|---|---|
| Heures travaillées | 158 | Heures de présence |
| Heures contractuelles | 150 | Référence contrat |
| Heures supplémentaires | 8 | HS 1ère tranche, majoration 10 % |
| Primes heures supp. | 96,00 € | Salaire des 8 HS (8 × 12,00 €) |
| Majoration heures supp. | 12,00 € | 8 × 1,50 € (10 % min. légal) |
| Congés payés — prise | 2 jours | Solde CP |
| Congés payés — acquisition | 1,67 j | 2 j ouvrés travaillés × 50 % (art. L3141-3) |
| Titres-restaurant | 10 jours | 7,00 € / jour |
| Titres-restaurant — part employeur | 35,00 € | 10 × 3,50 € |
| Titres-restaurant — retenue salariale | 35,00 € | 10 × 3,50 € |

## 2. Détail des calculs

**Heures supplémentaires (8 h)**
- Taux horaire : 2 250,00 € ÷ 150 h = 15,00 €
- HS payées majorées de 10 % (taux minimum légal, art. L3121-4) : 8 h × 16,50 € = **132,00 €**
  - dont salaire de base des 8 h : 120,00 €
  - dont majoration : 12,00 €
- ⚠️ Si l'accord d'entreprise fixe une majoration supérieure (ex. 25 %), recalculer : 8 × 18,75 € = 150,00 €.

**Congés payés**
- Prise : 2 jours → aucune incidence sur le salaire (le CP est payé).
- Acquisition du mois : 1,67 jour (proportional au mois travaillé, au-delà des 8 semaines d'ancienneté).
- Solde CP : solde d'ouverture + 1,67 − 2,00 = **solde de clôture** (à vérifier dans le logiciel, ex. 24,00 + 1,67 − 2,00 = 23,67 j).

**Titres-restaurant (10 jours)**
- Valeur : 10 × 7,00 € = 70,00 € de titres
- Part salariale (50 %) : **− 35,00 €** (retenue sur salaire)
- Part employeur : 35,00 € (charge patronale, hors assiette SS)
- Plafond de non-imposition respecté (7,00 € < plafond 2026).

## 3. Synthesis du bulletin

| Poste | Montant |
|---|---|
| Salaire de base (150 h) | 2 250,00 € |
| Heures supplémentaires (8 h majorées) | + 132,00 € |
| **Brut prévisionnel** | **2 382,00 €** |
| Retenue titres-restaurant | − 35,00 € |
| Cotisations salariales | (calculées par le logiciel) |

## 4. Format export (CSV)

```csv
id_salarie;variable;valeur;unite;commentaire
0042;heures_travaillees;158;h;
0042;heures_contractuelles;150;h;
0042;heures_supp;8;h;tranche 1
0042;majoration_hs;12,00;eur;10 %
0042;conges_pries;2;jours;
0042;conges_acquis;1,67;jours;
0042;titres_repas_jours;10;jours;
0042;titres_repas_employeur;35,00;eur;
0042;titres_repas_retenue;35,00;eur;
```

## 5. Vérifications avant validation

- [ ] Confirmer la majoration de HS effective (10 % légal vs accord d'entreprise)
- [ ] Vérifier que le solde CP d'ouverture est suffisant (≥ 2 jours)
- [ ] Confirmer le barème titres-restaurant (7,00 €/jour, partage 50/50)
- [ ] Saisir les variables **avant** la date de calcul de la paie
- [ ] Relire le bulletin : brut 2 382,00 €, retenue TR 35,00 €
