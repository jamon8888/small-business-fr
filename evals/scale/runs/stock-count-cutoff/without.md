# Inventaire de fin d'année : traiter les écarts avant la clôture

**Situation** : 3 références en écart — 2 en excédent (comptable < physique) et 1 en manque (comptable > physique). L'objectif est de fiabiliser l'état de stock au 31 décembre avant la clôture, car le stock final alimente directement le résultat (valeur des stocks + coût des marchandises vendues) et la balance comptable.

**Règle d'or** : on ne clôture jamais avec des écarts non résolus. Chaque écart doit se terminer soit par une **rectification du stock comptable** (justifiée et documentée), soit par la **correction d'une écriture comptable** (mouvement que l'on retrouve), jamais par un « écart non identifié » résiduel.

---

## 1. Première action obligatoire : un deuxième comptage contradictoire

Avant toute écriture, re-compter les 3 références selon le protocole d'inventaire :

1. **Re-comptage indépendant** par une personne différente de la première (idéalement 2 personnes, 1 compte + 1 contrôle), sur les 3 références uniquement, en heure de faible circulation.
2. **Vérifier les pièges classiques d'erreur de comptage** :
   - unités de compte incohérentes (pièces / cartons / palettes) — cause n°1 des faux écarts ;
   - stock non « figé » : bons de réception ou de sortie non saisis entre le comptage et le comptable ;
   - stock en transit ou en zone tampon (réception, expédition, retour client) pas encore intégré ;
   - références confondues (références proches, étiquettes anciennes) ;
   - écart entre le date du comptage physique et la date de coupure comptable (31 décembre).
3. **Consigner** : date/heure du comptage, compteurs, méthode, et comparer au stock théorique extrait du logiciel à la même date.

> Si le second comptage annule tout ou partie de l'écart, le problème était comptable (saisie, unité, transit) et se traite dans l'étape 2. Sinon, on passe à l'investigation.

## 2. Chasse aux causes : retrouver les mouvements manquants

Pour chaque référence, reconstituer le **mouvement brut net** depuis le dernier inventaire fiable (ou depuis le début d'exercice) : stock théorique = stock de base + achats – ventes – sorties autres. Comparer au réel et identifier le point de divergence.

### Cas A — Les 2 références en excédent (plus de stock physique que comptable)

Causes typiques à vérifier, par ordre de probabilité :

1. **Réceptions non saisies** : fournisseurs livrés fin d'année, bons de livraison (BL) physiques reçus mais jamais enregistrés en comptabilité (achats et stock non passés). → C'est un problème de **cutoff** : les biens sont présents dans l'entrepôt au 31/12, donc ils **doivent** figurer au stock, même si la facture fournisseur arrive en janvier.
2. **Retours clients** non passés au stock ;
3. **Échanges, échantillons, dons ou transferts internes** (entrepôt ↔ showroom ↔ atelier) non tracés ;
4. **Doubles sorties saisies** dans le logiciel (deux fois la même vente).

**Traitement** : pour chaque excédent dont on retrouve la cause, on **saisit le mouvement manquant** (la réception, le retour), pas un simple « ajustement » au stock. On retrouve alors le BL, on enregistre l'achat en attente de facture (stock à prix d'achat estimé), l'écart disparaît et la balance reste cohérente avec les fournisseurs.

**Piège à éviter** : ne jamais « gonfler » le stock comptable par un ajustement en blind pour masquer l'absence d'écritures. C'est la faute classique qui fausse les comptes fournisseurs et la déduction de TVA.

### Cas B — La référence en manque (moins de stock physique que comptable)

Causes typiques à vérifier :

1. **Ventes ou sorties non saisies** (vente en caisse non enregistrée, casse, panne, démarque) ;
2. **Cassés / non-conformes** mis au rebut sans passage en sortie de stock ;
3. **Vol ou démarre interne** ;
4. **Transfert vers un autre site** (si plusieurs lieux de stockage) non enregistré ;
5. **Expédition du 31/12 non livrée** : le bon de sortie est saisi, la marchandise est encore sur le quai ou en transit → elle doit rester au stock au 31/12.

**Traitement** :
- Si un **mouvement est retrouvé** (vente manquante, casse non passées, transfert non saisi) → saisir le mouvement, l'écart disparaît ;
- Si **aucune cause n'est identifiable** → passer en **démarre** : ajustement au stock comptable avec écriture de contrepassage, et justification écrite de l'investigation (quand, qui, quoi). C'est l'arbitrage de direction : l'écart devient une charge (démarre) au compte de résultat.

## 3. Vérification de cutoff (coupure comptable) au 31 décembre

C'est le point le plus sensible de la clôture. Pour les 3 références, vérifier la cohérence entre **physique** et **comptable** à la date de coupure :

| Situation | Stock physique au 31/12 | Traitement comptable |
|---|---|---|
| BL fournisseur reçu avant le 31/12, facture en janvier | oui | **Inclure au stock** + enregistrement à prix estimé des achats en attente de facture |
| BL fournisseur reçu en janvier | non | Exclure du stock 31/12 (et des achats N) |
| Commande client expédiée le 31/12 | non | Vente et sortie de stock passées (vente constatée) |
| Commande client expédiée en janvier mais comptabilisée le 31/12 | **oui** | Revenir sur la vente : la marchandise est encore en stock au 31/12 → stock inclus, vente reportée à N+1 |
| Retour client réceptionné le 31/12, saisie en janvier | oui | Inclure au stock, retour comptabilisé à la coupure |

**Action concrète** : extraire les 10 derniers jours (28/12–31/12) et les 10 premiers jours de l'exercice suivant (1–10/01) des bons de réception, expédition et factures des 3 références, et les croiser. C'est là que se nichent 80 % des erreurs de fin d'année.

## 4. Traitement comptable à la clôture

Selon l'issue de l'investigation, deux types d'écritures :

1. **Rectification de mouvement retrouvé** (cas le plus fréquent après investigation) :
   - réception non saisie → DR stock / achats (à prix d'achat), en attente de facture ;
   - vente non saisie → annulation de la sortie de stock (et régularisation de la vente si elle concerne N).
2. **Ajustement de démarre / excédent résiduel** (quand aucune cause n'est retrouvée) :
   - manque : débit démarre (615 ou compte de démarre dédié) / crédit stock → **charge sur le résultat** ;
   - excédent sans cause : débit stock / crédit 758 (produit exceptionnel) — **produit non récurrent**, à ne pas systématiser.

**Bonnes pratiques de clôture** :

- Passer ces écritures **avant** l'édition de la balance de clôture, avec un **libellé explicite** par référence (« Écart inventaire N — Réf X : démarre non identifiée, 12 U à 18,50 € ») ;
- Faire **approuver chaque ajustement par la direction** (vous) avec la traçabilité de l'investigation : qui a recompté, quelles causes vérifiées, pourquoi l'écart est maintenu ;
- Vérifier l'impact : stock final, coût des marchandises vendues, résultat, et cohérence des soldes fournisseurs (les achats estimés du 31/12 seront régularisés sur les factures de janvier) ;
- **Valeur nette** : à la clôture, vérifier que chaque référence en stock est valorisée à la plus faible entre coût et valeur de réalisation (dépréciation éventuelle des références en panne de rotation, obsolètes ou cassées) ;
- **Transmettre au commissaire aux comptes** (si vous en avez un) et au comptable une **note d'inventaire** : résultats du comptage, écarts constatés, causes identifiées, ajustements passés, approbation. C'est ce dossier qui sera testé en revue.

**Conséquences à anticiper** :
- un écart non traité = état de stock inexact → coût des marchandises vendu erroné → résultat faussé (sur ou sous-évaluation) ;
- une démarre non documentée sera contestée par le CA ou le commissaire ;
- des stocks en excédent non justifiés font apparaître des actifs fictifs et peuvent fausser la TVA déductible si les réceptions correspondantes n'existent pas.

## 5. Plan d'action récapitulatif (ordre et délais)

| # | Action | Qui | Quand |
|---|---|---|---|
| 1 | Re-comptage contradictoire des 3 références + vérification unités/transit | Responsable magasin + 2e personne | J+1 |
| 2 | Extraction mouvement brut net des 3 références depuis le dernier inventaire | Comptable / gestion stock | J+1 |
| 3 | Investigation des causes (BL non saisis, ventes manquantes, cassés, transferts, retours) | Responsable magasin + comptable | J+2 à J+3 |
| 4 | Coupure 31/12 : croisement des 10 derniers jours N et 10 premiers jours N+1 | Comptable | J+3 |
| 5 | Saisie des mouvements retrouvés + ajustements résiduels en démarre / excédent | Comptable | J+4 |
| 6 | Validation direction (écritures + note d'inventaire + approbations) | Direction | J+5 |
| 7 | Transmission note d'inventaire au CA / commissaire aux comptes | Direction + comptable | avant clôture |
| 8 | Clôture : balance, valeur nette des stocks, écritures de fin d'exercice | Comptable / CA | échéance normale |

## 6. Prévention pour l'exercice suivant

- **Blocage des mouvements pendant le comptage** (figer le stock dans le logiciel au démarrage) ;
- **Saisie des BL à réception** (pas « plus tard ») — c'est la cause n°1 des écarts de cutoff ;
- **Inventaire tournant** : recompter un échantillon de références à risque (à forte rotation, à forte valeur) chaque mois, pour que l'écart annuel reste anecdotique ;
- **Unités de compte normalisées** dans le logiciel, alignées sur les étiquettes ;
- **Seuil d'investigation** : tout écart > seuil (ex. 2 % de la valeur ou 5 unités) déclenche immédiatement l'investigation, pas en fin d'année ;
- **Tracer les zones tampon** (réception, expédition, non-conformes) dans le logiciel comme des emplacements à part entière.

**En résumé** : recompter d'abord (80 % des écarts s'annulent), retrouver les mouvements manquants et les saisir tels quels, traiter les seuls écarts résiduels en démarre documentée avec votre approbation, vérifier la coupure du 31 décembre sur les 10 jours de part et d'autre, et tout consigner dans une note d'inventaire transmise à la comptabilité et au commissaire avant la clôture.
