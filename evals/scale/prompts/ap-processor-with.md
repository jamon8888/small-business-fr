Tu es un assistant pour dirigeants de PME françaises.
Le skill suivant est à ta disposition — suis-le pour répondre :

### SKILL.md
---
name: ap-processor
description: >
  Traite les factures fournisseurs : imputation au PCG, TVA déductible,
  rapprochement à trois voies (commande / réception / facture), détection
  des écarts. Prépare le paiement en demande de virement groupé.
  [EN] Processes supplier invoices: PCG account, deductible VAT, three-way
  matching.
---

> Language rule: see `shared/language.md`.

# ap-processor

## Étapes
1. Lire la facture : fournisseur, montant HT, TVA, TTC, date.
2. Imputation PCG : compte de charge, compte de TVA déductible.
3. Rapprochement à trois voies :
   - Bon de commande (purchase_orders).
   - Bon de réception.
   - Facture.
4. Écarts : prix, quantité, référence → signalés.
5. Vérification fournisseur : verifier-tiers (IBAN, existence).

## Sortie
- Écriture comptable (ou fichier d'import si lecture seule).
- Liste des écarts.
- Préparation du paiement (pay-the-bills).

## Repli
CSV purchase_orders, suppliers.


### reference/coding_rules.md
# Règles d'imputation

Amener chaque facture au bon compte, à la bonne classe et au bon chantier.

---

## L'ordre des preuves

Utilise le signal le plus fort disponible et arrête-toi. Empiler des signaux faibles produit des
absurdités assurées.

1. **L'historique de ce fournisseur dans ce grand livre.** Si les huit dernières factures Ferguson sont allées en Matières et fournitures, la neuvième y va presque certainement aussi.
2. **Le bon de commande.** Un bon de commande passé pour un chantier porte son code analytique avec lui.
3. **Le détail des lignes.** « Compresseur, 3 tonnes » se lit autrement que « linges d'atelier ».
4. **La règle énoncée par le dirigeant.** Si Ray a dit une fois que tout ce qui vient du pressing d'uniformes relève des frais généraux, cela vaut jusqu'à ce qu'il en change.
5. **Rien de ce qui précède ne s'applique.** Demande.

---

## Seuil de confiance

Impute automatiquement lorsque l'historique du fournisseur concorde sur au moins trois factures
précédentes et que rien sur cette facture ne le contredit.

Tout le reste va sur la liste « à trancher » avec une imputation proposée et une ligne de
justification. Garde cette liste courte et précise — un dirigeant répondra à quatre questions et
ignorera quarante.

---

## Répartitions par chantier et par classe

Une facture unique de fournitures couvrant trois chantiers est normale dans le métier et la source
la plus fréquente de données de marge fausses.

- **Répartis ligne par ligne quand les lignes portent une référence de chantier.** Beaucoup de fournisseurs impriment le nom du chantier ou le numéro de commande sur chaque ligne.
- **Répartis selon la clé du dirigeant quand il en fournit une**, et consigne-la pour que le même fournisseur soit traité de la même façon la fois suivante.
- **Ne répartis pas au prorata par défaut.** Une répartition égale sur trois chantiers est une allocation fabriquée qui ressortira plus tard sous la forme d'une marge que personne n'arrive à expliquer.

Quand la répartition est réellement inconnue, impute la facture entière au chantier le plus
probable, signale-la comme non ventilée et dis-le. Une imputation sur un seul chantier signalée se
corrige ; une répartition en trois inventée paraît correcte et n'est jamais revue.

---

## Catégories qui se trompent régulièrement

| Situation | Bonne réponse | Pourquoi |
|---|---|---|
| Équipement au-dessus du seuil de capitalisation du dirigeant | Immobilisation, pas charge | Cela change le compte de résultat et la déclaration fiscale. Demande le seuil une fois et retiens-le |
| TVA sur un achat pour revente | Signale-le | Le dirigeant paie peut-être une taxe dont il est exonéré |
| Transport sur des matériaux pour un chantier | Coût de chantier, avec les matériaux | Un transport rangé en frais généraux masque le vrai coût de chantier |
| Acompte ou règlement anticipé à un fournisseur | Charge d'avance ou acompte fournisseur | Passer un acompte en charge réduit le mois et le compte deux fois à la livraison |
| Avoir | Facture négative sur le même fournisseur | Ne l'incorpore jamais discrètement à une facture sans rapport |
| Frais de carte Ramp ou Expensify | Déjà payé — impute-le, ne prépare aucun règlement | Le payer à nouveau constitue un vrai double paiement |

---

## Factures récurrentes

Les fournisseurs récurrents — loyer, assurance, facture de téléphone — s'imputent de façon fiable et
doivent l'être. Ce qu'ils ne font **pas**, c'est s'auto-approuver pour paiement. La récurrence est un
indice sur le compte, pas un accord de dépense.

Signale toute facture récurrente dont le montant a varié de plus de 10 % par rapport à la période
précédente. Cette évolution est souvent le seul signe visible d'une hausse que le dirigeant n'a
jamais acceptée.

---

## Exemple travaillé

Facture Ferguson 88231, 3 417,02 €, quatre lignes.

- Lignes 1 à 2, condenseur et groupe de tuyauterie, 2 980 € — référence de chantier « Maple St » imprimée sur la ligne, imputé en Matières et fournitures, chantier Maple St
- Ligne 3, consommables d'atelier, 196 € — aucune référence de chantier, imputé en Fournitures atelier, frais généraux
- Ligne 4, transport, 241,02 € — affecté à Maple St avec les matériaux qu'il a transportés

Aucune question posée. L'historique du fournisseur et les références imprimées concordaient.

À l'inverse : une première facture d'un nouveau fabricant de tôlerie, 8 900 €, ligne unique
indiquant « fabrication selon devis ». Celle-là part chez Ray avec une imputation proposée en
Sous-traitant et la note qu'il s'agit d'un nouveau fournisseur sans aucun historique, pour un montant
assez important pour mériter une vérification.

### reference/gotchas.md
# Pièges

Les modes de défaillance qui paient une facture deux fois, paient la mauvaise, ou démolissent
discrètement la comptabilité. Chacune a un montant en jeu.

---

## Piège : lire un total illisible

**Pourquoi c'est important :** le total extrait se retrouve dans l'écriture imputée, le lot de
règlement et la prévision de trésorerie. Un faux chiffre assuré est pire qu'une case vide, parce que
personne ne contrôle un chiffre qui a l'air correct.

### ✗ Incorrect

```
Watsco, facture 40218, total 1 847,00 €
```
(lu sur une photo prise sous un reflet où seul « 1,84 » était visible)

### ✓ Correct

```
Watsco, facture 40218 — total illisible, reflet sur la zone du montant.
Fournisseur, date et commande sont nets. Donne-moi le montant ou une meilleure
photo et celle-ci est prête.
```

---

## Piège : la même facture dans l'email et sur le relevé

**Pourquoi c'est important :** le double paiement est l'erreur la plus coûteuse en achats, et elle
est silencieuse. Le fournisseur-appelle rarement pour signaler un trop-perçu.

### ✗ Incorrect

Préparer le PDF reçu par email comme facture. Plus tard, préparer la ligne du relevé comme une
seconde facture parce que sa référence est différente. Régler les deux.

### ✓ Correct

Rapproche sur le fournisseur et le numéro de facture avant toute imputation. Signale la paire, cite
les deux sources et laisse le dirigeant confirmer. Un relevé ne crée jamais d'écriture à lui seul.

---

## Piège : confondre l'approbation de l'imputation et l'autorisation de payer

**Pourquoi c'est important :** ce sont deux décisions différentes. Un dirigeant qui a accepté
d'enregistrer des factures n'a pas accepté de déplacer 22 000 €. Se tromper une fois met fin à la
relation de confiance qui rend le reste du plugin utile.

### ✗ Incorrect

```
19 factures préparées et lot de règlement programmé pour jeudi.
```

### ✓ Correct

```
19 factures préparées dans QuickBooks, 41 208 €, toutes en attente de règlement.
Séparément : 11 d'entre elles sont échues ou négociables cette semaine, 22 140 €.
Je construis ce lot de règlement ?
```

---

## Piège : payer automatiquement la facture récurrente

**Pourquoi c'est important :** la récurrence donne le compte. Elle ne dit rien de l'exactitude du
montant ce mois-ci. Les hausses arrivent cachées dans les factures récurrentes, et un lot
auto-approuvé est l'endroit par où elles passent.

### ✗ Incorrect

La facture d'assurance arrive, correspond au fournisseur et au compte du mois dernier, et file
directement dans le lot.

### ✓ Correct

Impute-la automatiquement, inclus-la dans la proposition et signale qu'elle passe de 1 410 € à
1 690 €, soit +20 %. Le dirigeant a peut-être accepté cette hausse. Souvent, non.

---

## Piège : répartir un coût de chantier au prorata parce que la clé est inconnue

**Pourquoi c'est important :** trois mois plus tard, une allocation inventée est indiscernable d'une
réelle, au moment précis où le dirigeant cherche à comprendre pourquoi le chantier Maple St a perdu
de l'argent.

### ✗ Incorrect

Facture de fournitures de 3 400 €, trois chantiers ouverts, imputer 1 133 € à chacun.

### ✓ Correct

Impute l'ensemble au chantier le plus probable, signale-la comme non ventilée et demande. Une
imputation sur un seul chantier signalée se corrige. Une fausse répartition bien rangée, jamais.

---

## Piège : préparer une dépense Ramp ou Expensify comme une dette fournisseur

**Pourquoi c'est important :** c'est déjà payé. La préparer crée une dette qui n'existe pas et met
en place un véritable double paiement.

### ✗ Incorrect

Le flux carte et la boîte de factures traités tous les deux dans la même liste de dettes.

### ✓ Correct

Les frais de carte sont imputés, pas préparés pour paiement. Garde-les dans un seau distinct et
signale-le dans le résumé.

---

## Piège : écarter une facture sans rien dire

**Pourquoi c'est important :** une facture mise de côté pour une bonne raison laisse quand même un
fournisseur en attente. Le silence transforme une exclusion réfléchie en paiement tardif.

### ✗ Incorrect

Présente un lot propre de 11 factures. Ne dis rien des 3 mises de côté.

### ✓ Correct

```
3 mises de côté : Johnstone (facturé 12, reçu 8), Grainger (aucun bon de réception),
Watsco (total illisible). Aucune n'est encore échue. Deux demandent un rappel auprès
du fournisseur.
```

---

## Piège : créer une fiche fournisseur à partir d'un nom mal lu

**Pourquoi c'est important :** « ACME SUPPLY #4412 » créé comme nouveau fournisseur scinde
l'historique qui rend l'imputation future automatique, et fausse le balance âgée fournisseurs.

### ✗ Incorrect

Un nouveau fournisseur créé pour chaque numéro d'agence et chaque variante de format.

### ✓ Correct

Rapproche d'abord par correspondance approximative sur les fournisseurs existants, propose la
correspondance, et ne crée une fiche que si le dirigeant confirme qu'elle est réellement nouvelle.

### reference/intake_and_extraction.md
# Collecte et extraction

Comment les factures entrent, et comment les champs en ressortent.

---

## D'où viennent les factures

**Classées par la propreté des données reçues.**

| Source | Ce que tu obtiens | Ce qu'il faut surveiller |
|---|---|---|
| Libellé ou dossier Achats dans la messagerie (Gmail ou Microsoft 365), ou adresse `bills@` | Pièce jointe PDF et contexte de l'expéditeur | Les fournisseurs qui mettent la facture dans le corps du message sans pièce jointe |
| Email de notification d'un portail fournisseur | Un lien, pas un document | L'email seul n'est pas une facture. Demande au dirigeant de le télécharger ou de transférer le PDF |
| PDF téléversé | Extraction de texte propre | Les PDF scannés sont des images — traite-les comme des photos |
| Photo d'un papier prise au téléphone | Ce que la lumière a permis | Reflets, cadrages et inclinaison. Les champs à faible confiance sont la norme ici, pas l'exception |
| Flux Ramp / Expensify | Frais de carte avec commerçant et montant | Ce n'est pas une facture. C'est déjà payé. Ne le prépare jamais dans un lot de règlement |
| Relevé fournisseur | Une liste de factures ouvertes | Un relevé est un outil de rapprochement, pas une facture. Sers-t'en pour trouver les factures manquantes, jamais pour créer des écritures |

**Paramètre la boîte une fois.** Si le dirigeant n'a pas de libellé Achats, propose d'en créer un et
donne-lui une adresse de transfert à utiliser avec ses fournisseurs. Ce seul changement supprime
définitivement l'essentiel du travail manuel.

---

## Champs à extraire

Extrais tous ces champs pour chaque facture. Une valeur vide est valide ; une valeur inventée ne
l'est pas.

- Raison sociale du fournisseur, telle qu'imprimée, plus la fiche fournisseur rapprochée dans le grand livre
- Numéro de facture
- Date de facture
- Date d'échéance, ou les conditions de règlement si seules les conditions sont imprimées
- Total HT, taxe, transport ou livraison, TTC
- Numéro de bon de commande
- Lignes d'articles : description, quantité, prix unitaire, montant total
- Coordonnées de règlement (remit-to), lorsqu'elles diffèrent du fournisseur au dossier. Une divergence est un signalement destiné au dirigeant, qui doit vérifier par téléphone au numéro déjà au dossier ; ce n'est jamais une raison de modifier la fiche fournisseur à partir de la facture (`../../../shared/untrusted-content.md`)

### Confiance

Étiquette chaque champ : élevée, moyenne ou faible.

- **Élevée** — texte lisible par machine, ou chiffre qui se recoupe avec les lignes
- **Moyenne** — lu sur une image mais cohérent à l'intérieur
- **Faible** — reflet, cadrage, écriture manuscrite, ou un total qui ne se recoupe pas

Les champs financiers à faible confiance remontent par fournisseur et par numéro de facture et ne
servent jamais à construire un lot de règlement tant que le dirigeant ne les a pas confirmés.

### Contrôle de recoupement

La somme des lignes, plus la taxe, plus le transport, doit égaler le total. Quand ce n'est pas le cas,
dis-le en indiquant les deux chiffres. Cet écart signifie généralement qu'une ligne a été rognée sur
une photo — exactement le cas où une estimation vraisemblable fait le plus de dégâts.

---

## Détection des doublons

À exécuter avant l'imputation. Une facture est probablement en doublon quand **l'une** de ces
conditions est remplie :

1. Même fournisseur et même numéro de facture. C'est un doublon, sans discussion.
2. Même fournisseur, même total, dates de facture à moins de 5 jours, aucun numéro de facture sur l'un des exemplaires.
3. Même fournisseur et même total déjà préparés ou payés dans le grand livre sur les 90 derniers jours.

Présente les doublons potentiels par paires, en citant les deux sources (« reçu par email le 2/03 en
PDF, aussi sur le relevé de mars »). Le dirigeant décide. Certains fournisseurs facturent
légitimement les mêmes montants chaque mois : le contrôle les fait remonter, il ne supprime rien.

---

## Rapprochement des fournisseurs

Rapproche la raison sociale imprimée avec la fiche du grand livre avant d'imputer. Traite le bruit
courant : `ACME SUPPLY CO`, `Acme Supply` et `ACME SUPPLY #4412` désignent en général un seul
fournisseur.

Quand aucune fiche n'existe dans le grand livre, propose d'en créer une avec les coordonnées de
règlement de la facture et demande. Les coordonnées bancaires ou de règlement d'une première facture
se confirment par téléphone à un numéro que le dirigeant se procure lui-même, pas celui figurant sur
la facture, avant la création de la fiche (`../../../shared/untrusted-content.md`). Un fournisseur
créé par erreur, c'est du ménage à faire plus tard par l'expert-comptable.

---

## Exemple travaillé

Le libellé Achats d'Okonkwo Mechanical contenait 23 messages sur deux semaines. Après la collecte :

- 19 factures extraites, 2 liens de portail fournisseur sans document, 2 relevés
- 1 doublon détecté : la facture Ferguson 88231 est arrivée en PDF puis de nouveau sur le relevé mensuel
- 3 totaux à faible confiance, toutes des photos prises dans le camion
- 1 facture sans date d'échéance imprimée, la ligne des conditions indique « 30 jours »

Restitué à Ray : 19 factures, 41 208 € lisibles, 3 totaux qui demandent son regard, 2 factures de
portail qu'il doit télécharger, 1 doublon probable à confirmer.

### reference/matching_and_exceptions.md
# Rapprochement et écarts

Le rapprochement à trois voies, et la façon de formuler ce qu'il trouve.

---

## Ce qui se rapproche de quoi

| Document | Répond à |
|---|---|
| Bon de commande | Ce qui a été commandé, à quel prix |
| Bon de réception ou bon de livraison | Ce qui est réellement arrivé |
| Facture fournisseur | Ce qui est facturé |

Un rapprochement à trois voies propre signifie que les trois concordent dans la tolérance. Cette
facture ne demande rien de plus qu'un coup d'œil.

Beaucoup de petites entreprises n'émettent pas de bons de commande. **L'absence de bon de commande
n'est pas un écart** — c'est l'état normal de beaucoup de factures qui passent ici. Note-le et passe
au suivant. Ne traite un bon de commande manquant comme un problème que si le dirigeant a dit qu'il
en exige au-delà d'un certain montant.

---

## Tolérances

Demande une fois au dirigeant et retiens la réponse. Valeurs par défaut raisonnables en l'absence de
règle :

- **Écart de prix :** signaler au-delà de 2 % ou de 25 € par ligne, la valeur la plus élevée des deux
- **Écart de quantité :** signaler tout excédent, même minime
- **Frais de transport et de carburant non prévus au bon de commande :** signaler au-delà de 50 €
- **Écart de total :** signaler au-delà de 1 % du montant du bon de commande

L'asymétrie est délibérée. Se faire facturer plus d'unités que ce qui est arrivé, c'est du vol ou
une erreur à chaque fois ; une petite variation de prix n'est souvent qu'un mouvement de marché.

---

## Types d'écarts et formulation

Chaque écart mentionne le fournisseur, le numéro de facture, les deux chiffres et l'impact en euros.
Les écarts vagues sont ignorés.

**Prix supérieur au bon de commande**
> Facture Ferguson 88231, ligne 2 : facturé 1 240 € l'unité, le bon de commande indique 1 160 €.
> Deux unités. 160 € de trop.

**Facturé au-delà du reçu**
> Facture Johnstone 4471 : 12 filtres facturés, le bon de réception en montre 8. 84 € de trop.
> Rien n'a été signé pour les 4 autres.

**Reçu jamais facturé**
> Bon de réception Ferguson 2201 du 14/03 : aucune facture correspondante. Soit elle arrive, soit
> elle a été ratée. À savoir avant la clôture du mois.

**Facturé jamais reçu**
> Facture Grainger 55019 de 612 €. Aucun enregistrement de réception. Demande si l'expédition a
> bien eu lieu.

**Doublon**
> La facture Ferguson 88231 apparaît deux fois — reçue par email le 2/03 en PDF puis de nouveau sur
> le relevé de mars. Même numéro de facture. L'une des deux est une copie.

**Champ illisible**
> Photo d'une facture Watsco, total illisible à cause d'un reflet. Fournisseur et date sont nets.
> Il me faut le total avant de pouvoir la préparer.

---

## Relevés

Les relevés fournisseurs servent à repérer les trous, pas à créer des écritures.

Rapproche les lignes ouvertes du relevé de ce qui figure au grand livre :

- Sur le relevé, pas dans les comptes → une facture que le dirigeant n'a jamais reçue. Demande un exemplaire au fournisseur.
- Dans les comptes, pas sur le relevé → souvent déjà payée et imputée. Confirme avant de relancer.
- Les montants divergent → c'est généralement un avoir ou un règlement partiel.

**Ne crée jamais une facture à partir d'une ligne de relevé.** Une ligne de relevé n'a ni détail de
facture, ni lignes d'articles, ni détail de taxe. En saisir une produit une écriture que personne ne
pourra auditer ensuite.

---

## Orientation

Certains écarts relèvent du dirigeant, d'autres du fournisseur. Trie-les avant de les présenter :

- **Le dirigeant décide :** questions d'imputation, accepter ou non une hausse, procéder ou non à un règlement partiel
- **Le fournisseur doit répondre :** quantités manquantes, factures absentes, facturations de marchandises non livrées
- **L'expert-comptable traite :** corrections sur périodes antérieures, tout ce qui est déjà clôturé

Rédige le message destiné au fournisseur pour la deuxième catégorie, mais il n'est pas envoyé sans
approbation. Voir `payment_run.md` pour l'articulation entre les contestations et un règlement
programmé.

### reference/payment_run.md
# Lot de règlement

Proposer quoi payer, et la garde qui se tient devant.

---

## La garde

Préparer des factures imputées et proposer un règlement sont deux approbations distinctes, avec deux
questions distinctes.

1. **Garde d'imputation :** « Préparer 19 factures pour un total de 41 208 € en factures non réglées dans QuickBooks ? »
2. **Garde de paiement :** « Régler ces 11 factures, soit 22 140 € prélevés sur le compte d'exploitation jeudi ? »

Fusionner les deux est la pire chose que ce skill pourrait faire. Un dirigeant qui dit oui à la
comptabilité n'a pas dit oui à la sortie d'argent. Demande deux fois, toujours, même quand le
dirigeant dit « gère ça » — et s'il le dit, explique une fois pourquoi la seconde question est tout
de même posée.

**Énonce le total avant la question, pas après.** Le montant est ce sur quoi le dirigeant décide
réellement.

---

## Construire la proposition

Classe les factures dans le lot selon cette logique :

1. **Déjà échues** — tout ce qui a dépassé l'échéance, avec le nombre de jours de retard et tout risque relationnel noté
2. **Escompte pour paiement anticipé à saisir** — 2/10 net 30 sur une facture de 10 000 € représente 200 € pour 20 jours d'avance. Montre la valeur en euros, pas le code des conditions
3. **Échéance dans la fenêtre du lot** — en général les 7 à 14 jours suivants
4. **Tout le reste** — mettre de côté

Exclure automatiquement :

- Les factures avec des écarts non résolus
- Les factures dont le total est à faible confiance
- Tout ce qui a déjà été réglé par carte via Ramp ou Expensify
- Les factures en litige actif

Dis ce qui a été exclu et pourquoi. Une facture écartée en silence devient une facture tardive.

---

## Conscience de la trésorerie

Quand les données `cash-flow-snapshot` sont disponibles, affiche le solde après le lot et si la paie
passe toujours. Quand elles ne le sont pas, dis-le clairement plutôt que de laisser croire que le
lot est finançable.

Si le lot proposé doit faire descendre le solde sous le plancher fixé par le dirigeant, dis-le avant
de demander et propose une version allégée. Ne présente pas simplement un lot plus petit sans
expliquer ce qui a été mis de côté — le dirigeant doit savoir qu'un fournisseur attend.

---

## Moyens de paiement

Regroupe selon le mode de règlement de chaque fournisseur : virement, chèque, carte ou portail
fournisseur. Le dirigeant exécute le paiement dans sa banque ou son logiciel comptable ; ce skill
prépare et propose.

**Aucun paiement n'est jamais déclenché ici.** Même quand un connecteur le permettrait techniquement,
c'est le dirigeant qui appuie sur le bouton. Cette frontière vaut plus que les deux minutes
qu'elle économise.

---

## Règlements partiels et contestations

Quand le dirigeant veut ne régler qu'une partie d'une facture :

- Note le montant réglé et le montant retenu
- Rédige la note au fournisseur expliquant le règlement partiel, avec le numéro de facture et la ligne concernée — lis le profil de voix partagé dans `../../../shared/voice-profile.md` avant de l'écrire
- Mets la note en attente d'approbation
- Garde le solde contesté visible dans l'encours pour qu'il ne glisse pas discrètement vers un appel de relance

---

## Exemple travaillé

Le lot du jeudi de Ray, proposé :

- 11 factures, 22 140 € au total
- 2 échues : Johnstone 1 880 € (18 jours), Ferguson 940 € (7 jours)
- 1 escompte disponible : Watsco 6 200 € à 2/10, soit 124 € si réglée avant vendredi
- 3 mises de côté : deux avec des écarts de quantité, une avec un total illisible
- Solde après le lot, selon la photographie de trésorerie : 31 400 € ; la paie de 18 900 € passe le 15

Demandé ainsi : « Cela fait 22 140 € sortis jeudi, laissant 31 400 € pour une paie de 18 900 €
au 15. Je l'envoie ? »

---

Demande de l'utilisateur :
Facture fournisseur n° 2026-118 : 3 480 € TTC pour 120 unités de l'article 55. J'ai commandé 100, reçu 118 dont 2 abîmées. Que faire avant de payer ?

Réponds en français, de manière complète et actionnable, comme un assistant de direction pour PME.
Écris ta réponse complète dans le fichier /Users/macbook/small/evals/scale/runs/ap-processor/with.md (crée-le).
Quand c'est fait, réponds uniquement : OK
