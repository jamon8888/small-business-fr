# Clôture d'octobre + prévision de trésorerie 60 jours

**Où on en est.** Je n'ai pas encore votre export Qonto. Plutôt que de me contenter de vous répondre « envoyez-moi le fichier », je vous livre maintenant le dossier de clôture **au forme exacte** : chaque poste à traiter dans l'ordre, les contrôles à passer sur vos 14 factures et vos 31 lignes de ventes, la liste des écritures d'OTC, les dates fiscales qui tombent entre octobre et décembre, et la trame de prévision de trésorerie sur 60 jours, prête à remplir. Il ne vous reste qu'à injecter les chiffres — et ils me sontDemandés en bas de page.

**Deux règles de jeu, d'emblée :**
- Rien ne sera payé, publié ni déclaré sans votre feu vert. Ce qui suit est de la préparation et de l'analyse, pas de l'exécution.
- Vous avez une comptabilité externalisée ou pas ? Ça ne change rien à la méthode, mais ça change qui fait quoi. Je pose la question plus bas.

**Une remarque de calendrier.** Nous sommes le 15 octobre : le mois n'est pas terminé. Deux options, et je vous conseille la première :
1. **Clôture provisoire au 15/10 + clôture définitive au 31/10.** C'est ce que je recommande. La provisoire fiabilise le lettrage (c'est le seul poste qui prend du temps et qui ne s'arrête jamais), vous repérez les problème de stock et de créances en avance, et le 31/10 il ne reste que la saisie et les écritures d'OTC.
2. **Attendre le 31/10** et tout faire d'un bloc. Plus rapide sur le papier, mais vous telephonesz vos clients et vos fournisseurs le 3 novembre pouracheter l'ordre du mois.

Je pars ci-dessous sur la clôture **définitive au 31/10**, et je vous signale à chaque étape ce qui se traite déjà en provisoire.

---

## Étape 1 — Ce qu'il me faut de vous pour passer en chiffres

| # | Élément | Pourquoi | Où je l'utilise |
|---|---|---|---|
| 1 | **Export Qonto CSV**, période **01/10 → 31/10**, sur **tous les comptes** (compte courant + carte(s) + compte réserve si vous en avez un). Idéalement aussi l'export de septembre pour justifier les flux d'octobre. | La base du lettrage. | § 2.1 |
| 2 | **Balance générale provisoire au 31/10** (Excel, tous comptes) | Contrôle de cohérence : la balance doit tomber juste. | § 2.7 |
| 3 | Vos **14 factures fournisseurs** : n° de facture, date de facture, date de livraison/réception, fournisseur, montant HT, mode de règlement, délai de paiement, statut (échue/non échue) | Le cut-off fournisseurs, la balance âgée, la prévision. | § 2.2, § 3 |
| 4 | Vos **31 lignes de ventes** : date, client, montant HT, TVA, statut (facturé / encaissé / non facturé), mode de règlement | Le cut-off clients et la prévision d'encaissement. | § 2.3, § 3 |
| 5 | **Situation du stock au 31/10** : quantités × coût d'achat, par famille ou rayon. À défaut, le dernier inventaire physique + le flux des mouvements d'octobre. | Le poste le plus sensible en négoce. | § 2.4 |
| 6 | **Échéancier des charges fixes** d'octobre à janvier : loyer, énergie, télécom, assurances, licences/SaaS, transport/livraison, honoraires, abonnement Qonto | 60 jours de prévision sans ça, c'est de la fiction. | § 3.2 |
| 7 | **Paie d'octobre** : net à payer, date de virement, provisions (congés payés, participation) | Sortie de cash récurrente et massive. | § 2.5, § 3.2 |
| 8 | **Emprunts en cours** : capital restant dû, mensualité, assurance emprunteur, date des prochaines échéances | Une échéance non vue dans une prévision 60 jours, c'est le bug classique. | § 3.2 |
| 9 | Le nom de votre **outil de comptabilité** (Qonto Comptabilité, Pennylane, Sage, Cegid, autre) | Le lettrage se fait dedans, pas dans un tableur. | § 2.1 |

Format idéal : n'importe quel export ou tableau, je m'adapte. Je n'ai besoin d'aucun accès à votre banque — et je n'en demanderai pas.

---

## Étape 2 — Le dossier de clôture

### 2.0 Le calendrier, en 10 jours de travail

| Jour | Étape | Charge |
|---|---|---|
| J+1 | Export du flux bancaire du mois, clôture du mois dans l'outil de compta, lettrage : traitement des suggestions | ½ j |
| J+2 | **Contrôle des non-lettrés** — le cœur du travail | ½ j |
| J+2–3 | Fournisseurs : lettrage, cut-off, factures à payer, avoirs | ¼ j |
| J+3–4 | Clients : lettrage, créances douteuses, préparation des relances | ¼ j |
| J+4–5 | Stock : mise à jour, contrôle d'inventaire, test de dépréciation | ¼ j |
| J+5–6 | Autres écritures d'OTC : paie, emprunts, subventions, immobilisations, frais de banque | ¼ j |
| J+6 | Étalonnage : balance générale, balance âgée clients et fournisseurs, analytique | ¼ j |
| J+7 | Saisie des écritures d'OTC + validation | ¼ j |
| J+8 | Revue en double (vous + votre comptable si externalisé) + publication comptable | ½ j |
| J+9 | Prévision de trésorerie 60 jours | ½ j |
| J+10 | Note de clôture d'une page | ¼ j |

Pour un mois « normal », comptez **1,5 jour**. Le seul poste qui peut déraper, c'est le lettrage bancaire — d'où l'intérêt de la clôture provisoire au 15/10.

### 2.1 Lettrage bancaire — le geste n° 1, tout le reste en découle

C'est le seul travail non automatisable, et celui qui conditionne l'exactitude de tout ce qui suit. Procédure :

1. Exporter le flux du mois **depuis Qonto** (Transactions → Exporter, en CSV).
2. Clôturer le mois dans l'outil de comptabilité, puis **importer** le flux.
3. **Traiter les suggestions de lettrage** proposées par l'outil. Trois issues possibles par opération : lettrée, refusée avec motif, non lettrée.
4. **Rapprochement bancaire** : le solde du relevé au 31/10 doit être **identique** au solde du compte banque à la balance. Au centime. Si ce n'est pas le cas, vous avez soit une opération non importée, soit un doublon.
5. **Contrôle du mois suivant** : ouvrez le flux du 1er novembre et vérifiez qu'il ne contient **aucune opération datée d'octobre**. Une recette encaissée en octobre mais enregistrée en novembre (et inversement) est l'erreur la plus coûteuse en clôture.

**Le livrable de cette étape est un tableau des non-lettrés**, avec pour chaque ligne : date, montant, libellé, montant probable, motif du non-lettre. Sans ce tableau, vous ne clôturez pas : vous<constatez.

Les motifs de non-lettre à surveiller spécifiquement en négoce :
- **Virements fournisseurs reçus en double** (le même règlement splité en deux lignes, ou deux factures réglées par un seul virement) — très fréquent quand on paie par lot.
- **Frais bancaires et commissions** mal identifiés (abonnement Qonto, frais de tenue).
- **Règlements cartes** : le flux carte arrive avec un décalage de 1 à 3 jours par rapport à la date de transaction. Sans retraitement, votre chiffre d'affaires de clôture est faux.
- **Virements reçus non identifiés** (le client paie « facture 1234 » ou rien du tout).

### 2.2 Fournisseurs — vos 14 factures

Triez les 14 factures en trois piles :

**Pile A — lettrées.** Montant, date de règlement réelle. C'est votre base de prévision d'encaissement/décaissement la plus fiable.

**Pile B — non lettrées mais échues.** Ce sont des factures que vous devez régler dans les 15 jours. Elles pèsent lourd dans la prévision de trésorerie 60 jours : une facture échue non réglée, c'est de la trésorerie immobilisée et, à terme, des pénalités de retard. Chaque ligne doit avoir **une date de règlement prévisionnelle**.

**Pile C — non lettrées, non échues.** Facture reçue, échéance future. Vous surveillez l'échéance.

**Les 5 contrôles à passer sur ces 14 factures :**

1. **Cut-off / date de décompte.** Une facture d'achat du mois est celle dont la **marchandise a été livrée** au 31/10, pas celle qui est datée du mois. Une facture du 28/10 livrée le 4/11 appartient à novembre. Vérifiez que votre fournisseur n'a pas « antidaté » pour faire passer une commande avant la fin du mois.
2. **Factures à payer non reçues (à payer).** Faites le reverse de l'audit : à partir des commandes livrées et non encore facturées au 31/10, reconstituez les factures que vous devez payer. C'est ce montant qui va apparaître dans votre trésorerie de novembre-décembre et qu'on oublie presque toujours.
3. **Avoirs à obtenir.** Litiges, retours, erreurs de prix, achats non conformes, remises quantitative. Un avoir non réclamé est du résultat perdu. C'est le corollaire du contrôle n°2.
4. **Doublons.** Numéro de facture en double, ou même facture saisie deux fois avec des libellés différents. Le contrôle infaillible : trier par fournisseur + montant + nombre de jours d'écart.
5. **Cohérence avec la balance âgée.** Le total de votre balance âgée fournisseurs au 31/10 doit être **égal** au solde du compte 401 à la balance générale. Écart = facture omise ou lettrage fantôme.

### 2.3 Clients — vos 31 lignes

Triez les 31 lignes en quatre piles :

**Pile A — facturé et encaissé.** Base de votre chiffre d'affaires encaissé du mois. C'est votre repère le plus fiable.

**Pile B — facturé, non encaissé.** Ce sont vos créances. Chacune avec une date d'encaissement **réaliste**, pas théorique.

**Pile C — non facturé (à facturer).** Commandes livrées en octobre, pas encore facturées. Vous devez les facturer en novembre : c'est du chiffre d'affaires d'octobre non constaté. Sans ça, votre marge d'octobre est fausse et vos acomptes d'IS le seront aussi.

**Pile D — avoirs à émettre.** Retours clients, remises accordées, litiges. Même logique que les avoirs fournisseurs, dans l'autre sens.

**Les 5 contrôles :**

1. **Le grand équilibre du mois.** Cette égalité doit être **vraie** :
   > Chiffre d'affaires TTC encaissé sur le mois
   > + chiffre d'affaires TTC facturé mais non encaissé
   > **= chiffre d'affaires TTC facturé du mois** (hors avoirs)

   Si elle ne tombe pas juste, vous avez un problème de cut-off de ventes ou d'avoirs mal passés. Refaites-la, elle vaut un quart d'heure et elle attrape l'essentiel des erreurs.
2. **Créances douteuses — à faire à CHAQUE clôture mensuelle, pas une fois l'an.** C'est le point le plus souvent oublié en PME. Vous devez provisionner les créances dont le recouvrement est devenu douteux, et ce calcul se refait tous les mois (la provision bouge d'un mois à l'autre). Sur vos 31 lignes, isolez celles de plus de 60 jours et cherchez au moins un élément concret (litige, retard de livraison, client en redressement) avant de provisionner ou non. Une provision sur une créance réellement encaissée ensuite, c'est une reprise à faire : ça fait du bruit pour rien, mais ça se rattrape.
3. **Balance âgée clients alignée sur le 411.** Même exigence d'égalité que côté fournisseurs.
4. **Préparation des relances de novembre.** La clôture est le bon moment pour le faire : vous avez l'âge de chaque créance en main. Un rappel amical à J+2 sur les créances de 30 jours fait plus effet qu'une relance à 60 jours.
5. **Subrogation et délégation de paiement.** Si vous êtes payé directement par le assureur, le factor ou le donneur d'ordre sur une facture à vous, ce n'est pas un encaissement de client : c'est un emprunt court. Traitez-le comme tel dans la prévision de trésorerie.

### 2.4 Stock — votre point critique, en négoce

C'est le poste qui distingue une clôture correcte d'une clôture « à peu près ». Quatre contrôles.

**a) La méthode de valorisation doit être formalisée et appliquée sans interruption.**
PEPS/PUMP, CUMP ou valeur de réalisation. Si votre méthode n'est pas écrite quelque part et appliquée tous les mois de la même façon, vous êtes en train de faire du résultat à la demande. On acte ça en clôture, une fois pour toutes.

**b) L'écart d'inventaire.** À chaque mois, comparez le stock théorique (mouvements du mois) au stock physique. Toute différence va au compte d'écarts d'inventaire. **Ne la laissez pas rester en suspens d'un mois sur l'autre** : un écart d'inventaire qui traîne devient ingérable et, en cas de contrôle, l'administration le requalifie.

**c) Le test de dépréciation, à chaque clôture mensuelle.** Vous devez comparer, pour chaque famille de stock :
> **coût de revient** (coût d'achat + frais d'achat + frais de distribution affectés)
> **vs prix de vente HT réaliste**
Si le prix de vente ne couvre plus le coût de revient, il y a dépréciation à constituer. Même principe en cas de hausse des prix : la dépréciation reste obligatoire dès lors que la valeur de réalisation est inférieure au coût.

**Le forfait d'ancienneté — à connaître, c'est un vrai montant.** Pour les marchandises **non alimentaires** dont l'ancienneté dépasse un an, l'administration retient fiscalement :

| Ancienneté | Dépréciation minimale retenue |
|---|---|
| 1 à 2 ans | 25 % |
| 2 à 3 ans | 50 % |
| plus de 3 ans | 100 % |

Vous pouvez déprécier davantage (et la différence n'est déductible que si elle est justifiée), mais pas moins. **Et attention : le stock non déprécié à due concurrence de la baisse est réintégré dans la base de l'impôt sur les sociétés.** Autrement dit, ne pas provisionner, ce n'est pas « ne rien payer » — c'est « payer plus tard, sans deduction ». C'est l'erreur la plus coûteuse du dossier.

**d) L'inventaire physique annuel reste obligatoire**, avec une procédure écrite et un procès-verbal signé puis approuvé. Levez une date fixe chaque année (décembre ou janvier, hors pic d'activité), faites compter par someone qui ne tient pas la comptabilité, et faites **approuver le PV**. Ce n'est pas négociable en contrôle.

### 2.5 Les autres postes d'octobre qu'on oublie

- **Paie.** Bulletin d'octobre validé. Provision pour **congés payés** — et le double comptage à éviter : les congés payés *acquis* et les congés payés *pris* doivent être tous deux comptabilisés, sinon votre besoin en fonds de roulement est faux et votre prévision de trésorerie de décembre est fausse.
- **Emprunts.** Intérêts, échéance de capital, assurance emprunteur, commissions de garantie. Notez la **date effective** de l'échéance (le jour de valeur n'est pas toujours le jour d'échéance).
- **Subventions.** Subvention d'investissement : à reprendre sur la durée. Subvention d'exploitation : reprise sur la durée prévue. Une subvention encaissée mais non reprise vous coûte du résultat chaque mois.
- **Immobilisations.** Ce qui est en cours entre en immobilisation (pas en charge). Le calcul des amortissements du mois est à faire sur les newly mises en service.
- **Frais de banque.** Abonnement Qonto, frais de tenue, commissions. Petits montants mais il y en a partout, et ils sont rarement lettrés.
- **Comptes courants d'associés.** Intérêts (les plafonds de déduction évoluent, à vérifier), relevés signés, apports en compte courant.
- **Régularisation de la trésorerie et des frais de découvert.**

### 2.6 Les écritures d'OTC (opérations de clôture)

La liste complète, à passer en octobre :

| # | Écriture | Impact |
|---|---|---|
| 1 | Écart d'inventaire sur marchandises | Stock ↓, résultat ↓ |
| 2 | Dotation aux dépréciations de stock (compte 39) | Résultat ↓ |
| 3 | Reprise de dépréciation de stock (variation du mois) | Résultat ↑ |
| 4 | Dotation aux dépréciations de créances clients (compte 39) | Résultat ↓ |
| 5 | Reprise de dépréciation de créances | Résultat ↑ |
| 6 | Pertes de créances irrécouvrables constatées (compte 654) | Résultat ↓ |
| 7 | Factures à établir (ventes livrées non facturées) | CA ↑, créance ↑ |
| 8 | Factures à payer / produits à recevoir (achats non facturés) | Charge ↑, dette ↑ |
| 9 | Avoirs à émettre clients / avoirs à recevoir fournisseurs | Résultat ↓ |
| 10 | Charges constatées d'avance (assurances, abonnements payés d'avance) | Charge ↓, actif ↓ |
| 11 | Produits constatés d'avance | Résultat ↓ |
| 12 | Intérêts de cours d'exercice (emprunts, découverts, comptes courants) | Charge ↓ |
| 13 | Régularisation TVA (si mensualisée) | Balance TVA |
| 14 | Provision pour congés payés | Résultat ↓ |
| 15 | Reprise de la provision sur voyages/missions | Résultat ↑ |

### 2.7 Le contrôle final : 6 égalités qui doivent tomber juste

1. **Total balance générale = total balance.** Toujours, mais on le vérifie quand même.
2. **Balance âgée clients = solde du compte 411.**
3. **Balance âgée fournisseurs = solde du compte 401.**
4. **Solde bancaire du relevé = solde du compte banque à la balance.**
5. **Stock théorique final = stock physique + stock en transit properlyysté (approvisionnement en cours non réceptionné).**
6. **CA TTC encaissé + CA TTC non encaissé = CA TTC facturé** (§ 2.3, contrôle 1).

Si une seule de ces six lignes ne tombe pas juste, on ne publie pas.

### 2.8 Les dates à ne pas rater entre octobre et décembre

Ces dates-là sont réelles et indépendantes de la clôture comptable. Les voici pour que vous les mettiez dans votre agenda :

| Échéance | Date | Détail |
|---|---|---|
| DSN (paie d'octobre) | **avant le 5 novembre** | Retenue à la source IR + cotisations. Déclaration et paiement. |
| CA3 mensuelle (TVA d'octobre) | **19 novembre** | Si vous êtes en TVA mensuelle. |
| Acompte de TVA (si régime trimestriel) | **21 janvier** (+21 avril, 21 juillet, 21 octobre) | Sur la base de la TVA de l'année précédente. |
| **Acompte d'IS** | **1er décembre** | Les sociétés à l'IS versent 3 acomptes : **50 % au 1er mars, 25 % au 1er juin, 25 % au 1er décembre**, calculés sur l'IS de l'exercice précédent (arrondi au millier supérieur). Donc **25 % de votre IS 2025 tombent le 1er décembre**. À vérifier sur votre dernier avis d'imposition et votre propre échéancier. |
| CFE | acomptes **d'octobre** (selon votre zone), solde | L'automne est la période. |
| Taxe foncière | **novembre** | Selon l'échéance du rôle. |

Deux rappels utiles : la **CVAE n'existe plus** (supprimée à partir de 2023), ne la cherchez pas dans vos formulaires. Et la **TVA sur véhicules de tourisme affectés à un usage mixte** est plafonnée — 9 900 € HT par an et par véhicule, et **41 890 € HT** pour les véhicules achetés ou pris en location (crédit-bail, location) — plafond en vigueur depuis le 1er janvier 2022, à faire figurer dans votre politique de déduction. À confirmer sur la documentation en vigueur à la date de votre clôture.

### 2.9 Ce que vous obtenez à la fin : la liasse

12 fichiers, tous générés depuis vos données :

1. Balance générale au 31/10 (tous comptes, contrôle d'équilibre)
2. Balance âgée clients au 31/10 + plan de relance
3. Balance âgée fournisseurs au 31/10 + échéancier de paiement
4. Tableau des non-lettrés bancaires avec motifs
5. Journal des écritures d'OTC du mois, justifié
6. Test de dépréciation de stock par famille, avec l'ancienneté
7. Suivi de l'inventaire (stock théorique / physique / écart)
8. Tableau des factures à établir et à payer
9. Tableau des créances douteuses (dotation / reprise du mois)
10. Prévision de trésorerie 60 jours, 3 scénarios
11. Tableau des échéances fiscales novembre-décembre
12. **Note de clôture d'une page** : ce qui a bougé vs octobre, écarts d'inventaire, provisions, alertes, et les 3 décisions à prendre en novembre

---

## Étape 3 — Prévision de trésorerie sur 60 jours (1er novembre → 30 décembre)

### 3.1 La méthode

- **Méthode directe**, par **semaine** : 8 semaines pleines + une période résiduelle de 4 jours (27–30 décembre).
- **Point de départ = le solde bancaire réel du compte Qonto au 31/10.** Celui de la banque, pas celui de la comptabilité. Si les deux diffèrent, c'est qu'il reste des non-lettrés : on ne lance pas une prévision sur un faux point de départ.
- **Une ligne « solde de sécurité » à 0 €** en fin de ligne, systématiquement. Une prévision sans ligne de sécurité est une prévision qui se ment à elle-même : les petits flux s'annulent toujours un peu.
- **Trois scénarios**, pas un : bas / central / haut. En négoce, l'écart entre le scénario bas et le haut est souvent de 30 à 50 % de l'enjeu. Une prévision à un seul scénario ne sert à rien pour décider.
- **Chaque flux daté par sa date de règlement**, jamais par sa date de facture. C'est l'erreur n°1.

### 3.2 Les flux à modéliser

**Encaissements**

| Flux | Origine du chiffre | Comment être réaliste |
|---|---|---|
| Créances clients échues en nov.–déc. | Balance âgée du 31/10 | Date d'échéance réelle + 2 à 5 jours de délai de gestion bancaire + 3 jours ouvrés de règlement effective (le règlement n'arrive pas le jour de l'échéance) |
| Créances en retard à relancer | Balance âgée > 60 j | Ne comptez que 30 à 50 % du montant, selon votre historique réel de relance |
| Subventions / aides encaissées | Contrats signés, échéancier réel | Ne projetez que ce qui est contractualisé. Un « on devrait avoir » n'est pas un encaissement. |
| Cessions d'actifs, remboursements, avoirs reçus | Acte signé | Rare, mais à intégrer |

**Décaissements**

| Flux | Origine du chiffre | Piège à éviter |
|---|---|---|
| **Fournisseurs — échéances réelles** | Vos 14 factures + le reverse audit des factures non reçues | Une facture d'octobre payée en décembre sort **en décembre**, pas en octobre |
| **Stock — le réapprovisionnement** | Capacité d'achat mensuelle × ratio de couverture cible | **C'est LE flux décisif sur 60 jours en négoce.** Si votre stock baisse en octobre, vos achats d'octobre se paient en novembre. Si votre couverture est à 60 jours, ce sont 2 mois de chiffre d'affaires au coût d'achat qui sortent. Beaucoup de prévisions échouent là. |
| **Paie** | Net + charges patronales + DSN + provisions | Le mois de décembre inclut souvent un 13e mois, des primes, ou une seasonality forte : vérifiez. |
| **Charges fixes** | Échéancier récurrent | Loyer, énergie, télécom, assurances, SaaS, transport/livraison, honoraires, abonnement Qonto, site e-commerce. |
| **TVA et impôts** | Calendrier § 2.8 | La TVA n'est pas une trésorerie neutre : elle sort en bloc, souvent un mois de chiffre d'affaires TTC. |
| **Acompte d'IS du 1er décembre** | § 2.8 | Souvent oublié dans les prévisions de fin d'année. |
| **Emprunts** | Tableau d'amortissement | Capital + intérêts + assurance. Vérifiez la date effective. |
| **Dirigeant** | Rémunération + **dividendes** | **Un dividende n'est décaissable qu'après décision de l'assemblée (ou du président pour la SARL).** Sans décision, le compte « dividendes à payer » existe mais la trésorerie ne bougera pas. Dans une prévision 60 jours qui contient fin d'année, c'est un piège. |
| **Divers** | Voyages, événements, investissements légers | Mettez une ligne « divers » même si elle est petite : elle absorbe les imprévus. |

### 3.3 Le tableau (structure)

| Période | Enc. clients | Enc. autres | **T. encaiss.** | Déc. fournisseurs | Déc. stock | Paie | Charges fixes | Impôts/TVA | Financement | Autre | **T. décaiss.** | **Solde** | **Solde cumulé** |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| S1 — 1/11 au 7/11 | | | | | | | | | | | | | |
| S2 — 8/11 au 14/11 | | | | | | | | | | | | | |
| S3 — 15/11 au 21/11 | | | | | | | | | | | | | |
| S4 — 22/11 au 28/11 | | | | | | | | | | | | | |
| S5 — 29/11 au 5/12 | | | | | | | | | | | | | |
| S6 — 6/12 au 12/12 | | | | | | | | | | | | | |
| S7 — 13/12 au 19/12 | | | | | | | | | | | | | |
| S8 — 20/12 au 26/12 | | | | | | | | | | | | | |
| S9 — 27/12 au 30/12 | | | | | | | | | | | | | |
| **Solde de sécurité** | | | | | | | | | | | | **0,00** | |

Dupliquez ce tableau trois fois : scénario bas, central, haut.

**Exemple de paramétrage des scénarios** (à calibrer sur votre historique, ces valeurs sont des ordres de grandeur de marché, pas vos données) :
- **Bas** : clients paient à 45 jours, 20 % des créances > 60 jours ne rentrent pas sur l'horizon, aucun encaissement de subvention.
- **Central** : clients paient à 30 jours + 5 jours de gestion, 10 % de retard moyen.
- **Haut** : clients paient à 30 jours, tout le soldable rentré.

### 3.4 Les seuils d'alerte

Une prévision sans seuil d'alerte est un exercice de style. Posez trois règles **avant** d'avoir le résultat :

1. **Seuil de vigilance** : si le solde cumulé passe sous X € pendant plus de N jours → alerte.
2. **Seuil d'urgence** : si le solde passe sous 0 → décision à prendre dans les 48 h.
3. **Le plancher** : si le solde ne retombe jamais sous Y € (votre trésorerie de sécurité cible).

Et préparez **par avance** la liste des leviers, activés dans l'ordre :
1. Décaler le règlement d'un fournisseur non stratégique (attention : incidence sur la relation, et risque de perte de remises).
2. Activer ou monter la ligne de découvert / réserve (Qonto).
3. Demander un acompte à un client au lieu d'attendre le règlement complet.
4. Affacturer une créance (si le montant le justifie).
5. Accélérer le réapprovisionnement contre remise fournisseur pour libérer du cash à terme (logique inverse, à cas particular).

### 3.5 Les 5 questions de contrôle de la prévision

1. Le solde de départ est-il le solde **bancaire** au 31/10, pas le solde comptable ?
2. **Ai-je inclus le réapprovisionnement de stock ?**
3. Chaque flux est-il daté par sa date de **règlement**, pas par sa date de facture ?
4. Mes créances clients sont-elles crédibles — ai-je confronté le scénario central à mon historique réel de retard de paiement ?
5. La ligne « solde de sécurité » est-elle à 0 ?

Si les 5 réponses sont oui, la prévision est honnête.

---

## Étape 4 — Les points que je vous demande de trancher

1. **Comptabilité externalisée ou pas ?** Si oui, à qui, et je cible ma note de clôture dessus.
2. **Quel logiciel de comptabilité ?** Le lettrage se fait dedans.
3. **Méthode de valorisation du stock** : PEPS, CUMP ou autre ? Formalisée ou non ?
4. **Régime TVA** : mensuel ou trimestriel ? Full assujetti ou prorata de déduction ?
5. **Délai de paiement clients moyen réel** (jours de retard constatés sur les 12 derniers mois) — c'est le paramètre le plus important de toute la prévision.
6. **Emprunts en cours** : principales échéances de novembre-décembre.
7. **Dividendes envisagés** en fin d'année ? Si oui, décision d'AG à caler sur le calendrier.
8. **État du stock** : en hausse, en baisse, ou stable par rapport à septembre ?

---

## Ce que je vous livre une fois vos données reçues

- **Dans les 24 h** : la balance générale, les deux balances âgées, le tableau des non-lettrés, le journal des écritures d'OTC, et la **note de clôture d'une page** avec les alertes.
- **En parallèle** : la **prévision de trésorerie 60 jours** en 3 scénarios, avec les seuils d'alerte et les leviers d'action.
- **À la demande** : la trame de relance clients (prête à envoyer), le tableau de suivi du stock par famille, et le tableau de suivi des échéances fiscales.

Dites-moi simplement quand vous avez pu déposer l'export Qonto et les deux listes (14 fournisseurs / 31 ventes) — même en brouillon, même en photo lisible, je m'adapte — et je vous passe le dossier en chiffres dès le lendemain.

Et si vous voulez la **clôture provisoire au 15/10**, dites-le maintenant : c'est le bon créneau, et on gagne beaucoup sur le lettrage de novembre.