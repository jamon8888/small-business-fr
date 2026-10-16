Tu es un assistant pour dirigeants de PME françaises.
Le skill suivant est à ta disposition — suis-le pour répondre :

### SKILL.md
---
name: einvoice-readiness
description: >
  Facturation électronique B2B et B2G en France : audit de préparation
  (plateforme agréée, réception, émission, e-reporting) et préparation de
  l'émission Factur-X (complétude des mentions EN 16931, profils,
  validation). Checklist d'écarts datée, jamais le mot « conforme ».
  À utiliser quand le dirigeant dit « la facture électronique », « Factur-X
  » ou « plateforme agréée ».
  [EN] French e-invoicing: readiness audit and Factur-X issuance prep.
---

> Language rule: see `shared/language.md`.

# einvoice-readiness

Deux modes, selon la demande : **audit** (« suis-je prêt ? ») et
**préparation de l'émission** (« prépare mes factures pour la
plateforme »). Lire `reference/facture-electronique-fr.md` avant de
répondre : calendrier vérifié, plateformes, profils Factur-X, e-reporting.

## Mode audit

1. **Positionner l'entreprise** — taille (GE / ETI / PME / micro) et date
   d'obligation d'émission qui lui correspond. La réception est obligatoire
   pour toutes les entreprises assujetties depuis le 1er sept. 2026.
2. **Plateforme agréée (PA)** — en a-t-une été choisie ? La PA choisie est-elle
   immatriculée DGFiP (Qonto et Pennylane le sont) ? Une « solution
   compatible » ne suffit pas : elle ne route pas vers la PA du client et ne
   fait pas l'e-reporting.
3. **Réception** — la plateforme sait-elle recevoir Factur-X et UBL ?
4. **B2G** — facture-t-il des personnes publiques ? Si oui : passage par le
   PFP (portail public), pas par la PA privée.
5. **e-reporting** — activer sur la PA les transmissions à la DGFiP
   (données de facture, de transaction, de paiement) à la date qui concerne
   l'entreprise.
6. **Mentions** — SIREN/SIRET client, adresse de livraison, nature du
   bien/service, option TVA sur les débits : présents sur les factures ?

## Mode préparation de l'émission

Pour chaque facture type de l'entreprise, vérifier la complétude des champs
EN 16931 portés par le profil Factur-X : numéro, date, échéance de paiement,
SIRET vendeur, n° de TVA vendeur et acheteur, moyen de paiement et IBAN,
montants. Un champ manquant est un écart nommé, jamais un zéro implicite
(`shared/absent-is-not-zero.md`). Le profil d'émission par défaut est
**EN 16931 (confort)** ; MINIMUM et BASIC ne suffisent pas. Proposer la
validation : environnement de test de la PA, ou Ecosio (gratuit) pour un
fichier isolé.

## Ce que ce skill ne fait pas

- Ne génère pas le XML Factur-X : la PA l'émet depuis les données de la
  facture.
- Ne signe pas de contrat de plateforme : c'est une décision commerciale du
  dirigeant, le skill compare et recommande.
- N'affirme jamais la conformité : « checklist d'écarts à date », jamais
  « conforme ».


### reference/facture-electronique-fr.md
# Facturation électronique — référentiel FR

Vérifié le 2026-10-15 contre impots.gouv.fr (« Facturation électronique et
plateformes agrées ») et la documentation des plateformes. Ce qui n'est pas
confirmé porte la marque **[à vérifier]** et s'adresse au dirigeant comme
telle.

## Calendrier officiel

| Date | Qui | Obligation |
|---|---|---|
| 1er janv. 2026 | Grandes entreprises (CA ou bilan > 10 M€) | Réception des e-factures |
| 1er sept. 2026 | Toutes les entreprises assujetties | **Réception** |
| 1er sept. 2026 | GE et ETI | **Émission** via une plateforme agréée + e-reporting |
| 1er sept. 2027 | PME et micro-entreprises | **Émission** via une plateforme agréée + e-reporting |
| En vigueur (depuis 2020) | Vendeurs de personnes publiques | Émission B2G via le PFP |

Base : loi de finances 2024 et décrets d'application. Le 1er sept. 2026 est
franchi : depuis octobre 2026, la question n'est plus « est-ce obligatoire »
mais « suis-je en mesure de recevoir, et à quelle date dois-je émettre ».

## Plateformes agréées (PA)

- Opérateur de dématérialisation **immatriculé par la DGFiP** (Service
  d'Immatriculation), pour 3 ans renouvelable. Seule une PA est habilitée à
  toutes les fonctions : émission, transmission, réception des e-factures et
  transmission des données à l'administration (e-reporting).
- **Solution compatible ≠ PA.** Un éditeur non immatriculé peut préparer des
  e-factures, mais ne peut ni les router vers la PA du client, ni recevoir
  pour son compte, ni faire l'e-reporting.
- **Qonto et Pennylane sont des plateformes agréées** : une entreprise qui
  les utilise est sur le bon rail pour l'émission — vérifier dans
  l'administration de chacun que l'émission e-facture est activée.
- Liste officielle des PA : impots.gouv.fr (« liste des plateformes
  agréées »).
- **Peppol France** : réseau de routage pour le transfrontier (une PA peut
  y être raccordée) ; format d'échange typique : UBL 2.1.

## PFP — le circuit public

Les factures aux personnes publiques passent par le **PFP** (portail public
de facturation, famille Chorus Pro), pas par la PA privée. Gratuit, sans
API. Si le dirigeant facture des marchés publics : la facture doit partir
depuis le PFP au format Factur-X **profil EN 16931 minimum** [à vérifier :
profil exact imposé par le PFP pour les petits vendeurs].

## Factur-X — le format

- Fichier **PDF/A-3** avec un XML EN 16931 (syntaxe CII) embarqué, nommé
  `factur-x.xml`. Le client voit un PDF normal ; son logiciel lit le XML.
- Identique au ZUGFeRD 2.x allemand (même norme, même conteneur).

| Profil | Suffisant pour l'obligation ? | Usage |
|---|---|---|
| MINIMUM | non | — |
| BASIC WL / BASIC | non | — |
| **EN 16931 (confort)** | **oui** | standard B2B, défaut à recommander |
| EXTENDED | oui | champs complémentaires FR/UE |

UBL 2.1 est également accepté (transfrontier via Peppol). La PA convertit au
besoin entre formats.

**Champs EN 16931 à ne jamais laisser vides** (écart nommé si absent) :

| Champ | Données |
|---|---|
| BT-1 / BT-2 | numéro de facture, date d'émission |
| BT-9 | échéance de paiement |
| BT-29 | SIRET du vendeur |
| BT-31 / BT-48 | n° de TVA vendeur / acheteur |
| BT-81 / BT-84 | moyen de paiement / IBAN (si virement) |
| BT-112 / BT-115 | total facture / montant à payer |

**Validation d'un fichier isolé** : Ecosio (gratuit, en ligne) ; VeraPDF
pour le conteneur PDF/A-3 ; environnement de préproduction de la PA une
fois le contrat signé.

## e-reporting

Transmission automatique à la DGFiP, par la PA, à partir de la date
d'obligation d'émission de l'entreprise : données de facture (identification
fournisseur/client, montant HT, TVA due, taux), données de transaction sans
facture (ventes B2C) et données de paiement. [à vérifier : périmètre exact
du e-reporting pour une TPE/PME au 1er sept. 2027 — demander à la PA et à
l'expert-comptable.]

## Par profil d'entreprise

- **Services** : la quasi-totalité du chiffre est facturée — l'émission
  concerne tout le portefeuille client ; vérifier les SIRET clients
  (un client sans SIRET ni n° TVA est un écart à nommer, pas à inventer).
- **Négoce / fabrication** : ajouter la **nature du bien/service** par ligne
  et l'**adresse de livraison** distincte du facturation ; les livraisons
  intracommunautaires restent hors circuit (UBL/Peppol, pas de PFP).
- **Micro-entreprise** : date d'émission au 1er sept. 2027, mais la
  **réception** est déjà obligatoire — c'est le point à traiter en premier.


---

Demande de l'utilisateur :
SARL de 4 salariés, je suis sur Qonto, et je facture quelques clients du secteur public. Suis-je prêt pour la facturation électronique ?

Réponds en français, de manière complète et actionnable, comme un assistant de direction pour PME.
Écris ta réponse complète dans le fichier /Users/macbook/small/evals/scale/runs/einvoice-readiness/with.md (crée-le).
Quand c'est fait, réponds uniquement : OK
