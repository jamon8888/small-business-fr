Tu es un assistant pour dirigeants de PME françaises.
Le skill suivant est à ta disposition — suis-le pour répondre :

### SKILL.md
---
name: job-post-builder
description: >
  Rédige une offre d'emploi : CDI / CDD / alternance, convention collective,
  rémunération brute annuelle, mention H/F. Modèle de promesse d'embauche à
  faire relire. Signature Yousign ou DocuSign.
  [EN] Builds a French job posting: CDI/CDD, collective agreement, salary,
  H/F mention.
---

> Language rule: see `shared/language.md`.

# job-post-builder

## Structure de l'offre
- Intitulé du poste (avec mention H/F).
- Type de contrat : CDI, CDD, alternance, stage.
- Convention collective applicable.
- Rémunération : brute annuelle (ou taux horaire).
- Lieu de travail.
- Missions principales.
- Profil recherché (compétences, expérience).
- Processus de recrutement.

## Modèle de promesse d'embauche
Fournir un modèle, avec la mention : « à faire relire par un juriste avant
envoi ».

## Signature
Yousign ou DocuSign si connecté. Sinon : impression, signature manuscrite,
scan.

## Sortie
- Offre d'emploi (DOCX, PDF).
- Promesse d'embauche (modèle).
- Une ligne : « offre prête, X points à vérifier ».

## Repli
Sans connecteur : DOCX local.


### reference/docusign-routing.md
# Acheminer la lettre de proposition vers DocuSign

Phase 6 uniquement, et seulement si l'utilisateur a choisi DocuSign en Phase 1.

Passe par Claude dans Chrome pour piloter l'interface de DocuSign, afin que le dirigeant
n'ait pas à toucher DocuSign à la main.

---

## La règle absolue

**L'enveloppe est enregistrée comme brouillon et jamais envoyée.** La Phase 6 ne franchit
pas « Save as draft » sans que l'utilisateur ait explicitement confirmé qu'il a relu
l'enveloppe et veut qu'elle parte. Une lettre de proposition qui arrive chez un candidat
avant que le dirigeant l'ait lue est irrécupérable.

---

## Pourquoi le navigateur et pas l'API

L'API DocuSign n'accepte un document que depuis un modèle déjà présent dans le compte, ou
depuis une URL qu'elle peut récupérer sans identifiants. Elle n'accepte pas de téléversement
de fichier. Une lettre de proposition nomme une personne et indique sa rémunération : la
mettre en ligne à une adresse accessible publiquement pour satisfaire le connecteur n'est
une option à aucun moment.

Le parcours navigateur contourne cela : le fichier est téléversé depuis la session
connectée de l'utilisateur, et rien n'est jamais publié. C'est pourquoi cette phase est
écrite comme un parcours d'interface.

---

## Le parcours navigateur

1. Navigue vers `https://app.docusign.com`. L'utilisateur doit déjà être connecté. Si un
   écran de connexion apparaît, mets-toi en pause et demande-lui de se connecter, puis
   continue.
2. Clique sur **Start**, puis **Send an Envelope**. Selon la version de l'interface, le
   libellé peut être **New** ou **Use a Template**.
3. **Téléverse la lettre de proposition.** Clique sur « Upload Documents » et téléverse le
   fichier `[Role]-Offer-Letter.docx` créé en Phase 5.
4. **Ajoute le signataire.** Dans Recipients, ajoute le candidat comme signataire avec le
   rôle « Signer ». Demande son nom et son adresse e-mail s'ils n'ont pas déjà été fournis.
5. **Ajoute l'expéditeur en copie (CC)** si l'utilisateur souhaite un exemplaire. Demande-lui
   en cas de doute.
6. **Renseigne l'objet :** `Offre d'embauche — [Intitulé du poste] chez [Nom de l'entreprise]`
7. **Ajoute un message.** Deux lignes chaleureuses au candidat, par son prénom : satisfait
   de prolonger l'offre, à relire et signer quand il peut, questions bienvenues.
8. **Place les champs de signature.** Sur le document, place un champ Signature et un champ
   Date Signed sur la ligne d'acceptation du candidat, en bas de la lettre.
9. **Enregistre comme brouillon.** N'envoie pas.

Puis transmets le lien du brouillon et demande à l'utilisateur de vérifier le placement des
signatures et de confirmer ici quand il est prêt à envoyer.

---

## Solution de repli

Si DocuSign est indisponible ou si le parcours navigateur échoue à une étape, rédige un
brouillon d'e-mail via le connecteur mail connecté (Gmail ou Microsoft 365), avec la lettre
de proposition en pièce jointe et une note demandant de la téléverser manuellement dans
DocuSign.

**Montre le brouillon à l'utilisateur avant l'envoi.** Le repli ne baisse pas le niveau
d'approbation ; c'est la même barrière, atteinte autrement.

Si aucune des deux voies ne fonctionne, le `.docx` sur le disque constitue un résultat
complet. Dis que l'acheminement n'a pas eu lieu et remets le fichier.

### reference/examples/worked-example.md
# Exemple travaillé : Senior Product Manager

## Entrée

Message de l'utilisateur :
> « Nous devons recruter un Senior Product Manager pour notre équipe paiements. Il/elle portera
> la feuille de route de notre expérience de paiement. Nous voulons 5 ans minimum d'expérience
> en product management, idéalement avec un background fintech ou paiements. Télétravail possible,
> Paris de préférence. Rémunération : 160 000 – 185 000 € brut annuel. Trois tours d'entretien :
> présélection par le recruteur, approfondissement avec le responsable du recrutement, et un jury
> avec deux seniors PM. Envoie la proposition par DocuSign quand on y sera. »

---

## Phase 1 — Ce que Claude extrait

| Champ | Valeur |
|---|---|
| Intitulé du poste | Senior Product Manager |
| Équipe / périmètre | Équipe paiements |
| Responsabilités clés | Porter la feuille de route de l'expérience de paiement |
| Indispensables | 5 ans minimum d'expérience en product management |
| Souhaitables | Background fintech ou paiements |
| Lieu | Télétravail possible, Paris de préférence |
| Rémunération | 160 000 – 185 000 € brut annuel |
| Processus d'entretien | 3 tours : présélection recruteur, approfondissement RR, jury de 2 seniors PM |
| Remise de l'offre | DocuSign |

Claude confirme et pose exactement une question :
> « C'est noté — dossier de recrutement pour un senior PM sur l'équipe paiements,
> 160 000 – 185 000 €, télétravail, Paris. Une question avant de commencer : as-tu une offre
> d'emploi ou un modèle de lettre de proposition que je devrais utiliser comme point de
> départ, ou je construis de zéro ? »

---

## Sortie attendue

### `Senior-PM-Job-Post.docx`

La structure suit `../job-post-structure.md` :

1. **Accroche d'ouverture** — Pourquoi ce poste existe maintenant : l'équipe paiements
   industrialise l'expérience de paiement et a besoin de quelqu'un qui porte la feuille de
   route de bout en bout.
2. **À propos de l'entreprise** — 3 à 4 phrases (Claude demande ou déduit du contexte).
3. **À propos du poste** — À quoi ressemble la réussite dans 12 mois : un paiement plus
   rapide et plus fiable, avec un taux de conversion mesurablement supérieur.
4. **Ce que tu feras** — 5 à 6 puces, menées par des verbes d'action (par exemple « Porte
   la feuille de route du paiement, de la découverte au lancement… »).
5. **Ce que nous cherchons** — Requis : 5 ans minimum d'expérience PM, aisance avec la
   donnée, forte communication écrite. Souhaité : expérience du domaine fintech ou
   paiements.
6. **Rémunération** — 160 000 – 185 000 € de salaire brut annuel.
7. **Comment postuler** — Une phrase.

Longueur cible : 500 à 650 mots.

---

### `Senior-PM-Interview-Guide.docx`

La structure suit `../interview-guide-structure.md` :

- **Résumé du poste** — un paragraphe qui rappelle aux intervieweurs ce qu'ils évaluent.
- **Carte des étapes** — 3 étapes, un intervieweur par étape, une compétence par étape.
- **Étape 1 : présélection recruteur** — Communication, adéquation de base, logistique.
  Les questions portent sur le récit de carrière et la logistique (rémunération, date de
  début, organisation du télétravail).
- **Étape 2 : approfondissement avec le responsable du recrutement** — Prise en charge de la
  feuille de route, contexte des paiements, priorisation sous contrainte. 5 à 6 questions
  comportementales ; 2 à 3 relances chacune.
- **Étape 3 : jury de deux seniors PM** — Réparti entre les deux membres. Le membre A porte
  le jugement produit (comment ils arbitrent) ; le membre B porte la collaboration
  transverse (comment ils travaillent avec l'ingénierie et le design). Les questions sont
  attribuées à l'avance pour que le candidat n'ait pas à répondre deux fois à la même chose.
- **Grille de notation** — Ancres 1/3/5 écrites spécifiquement pour un PM paiements (pas
  génériques). Exemple pour « Prise en charge » : 5 = a identifié de lui-même un mode de
  défaillance du paiement que personne ne lui avait demandé de suivre, a piloté le correctif,
  a documenté pour l'équipe.
- **Guide de débrief** — Les intervieweurs partagent leurs notes avant la discussion ; le
  débrief se concentre sur les notes divergentes.

---

### `Senior-PM-Offer-Letter.docx`

Fondé sur `../offer-letter-template.md`. Pré-rempli dès que la donnée existe :

| Champ | Valeur |
|---|---|
| `[INTITULÉ DU POSTE]` | Senior Product Manager |
| `[SALAIRE ANNUEL]` | `160 000 – 185 000 € — confirmer le montant exact avec la RH avant l'envoi` |
| `[NOM COMPLET DU CANDIDAT]` | Laisser vide |
| `[DATE DE DÉBUT PROPOSÉE]` | Laisser vide |
| `[DATE D'EXPIRATION DE L'OFFRE]` | Laisser vide |
| Clause de résiliation à tout moment | Incluse |
| Mention de relecture juridique | Incluse |

---

## Phase 6 — Parcours navigateur attendu

1. Claude navigue vers `https://app.docusign.com` et vérifie l'état de connexion.
2. Clique sur « Start → Send an Envelope ».
3. Téléverse `Senior-PM-Offer-Letter.docx`.
4. Demande : « Quel est le nom complet et l'adresse e-mail du candidat ? »
5. Ajoute le candidat comme Signer ; ajoute l'utilisateur en CC si demandé.
6. Renseigne l'objet : `Offre d'embauche — Senior Product Manager chez [Nom de l'entreprise]`.
7. Place les champs Signature et Date Signed sur la ligne d'acceptation.
8. Enregistre comme brouillon — N'envoie PAS.
9. Renvoie l'URL du brouillon et dit à l'utilisateur de relire avant de confirmer l'envoi.

**Critères de réussite :** l'utilisateur ouvre l'URL du brouillon, voit le placement correct
des signatures, et peut envoyer en un clic. Le statut de l'enveloppe reste « Draft » tant
que l'utilisateur n'agit pas.

### reference/existing-document-merge.md
# Travailler à partir d'un document que l'utilisateur a déjà

La même règle gouverne les Phases 3, 4 et 5. Si la Phase 2 a trouvé une offre d'emploi, un
guide d'entretien ou une lettre de proposition existants, ce document est le modèle
structurel.

---

## La règle

**Le format de l'utilisateur fait foi. Le fichier de référence est une liste de contrôle,
pas une instruction de remplacement.**

Reprends ses noms de sections, son ordre, son ton, et les formules d'usage qu'il a
établies — description de l'entreprise, texte sur les avantages, formulation « comment
postuler », blocs de signature, clauses juridiques. Quelqu'un qui a déjà arrêté un format
l'a fait pour une raison, et une réécriture silencieuse donne l'impression que la compétence
en sait plus que lui.

---

## L'étape de fusion

1. Mets les sections du document existant en regard du fichier de référence correspondant.
2. Identifie ce que la référence contient et que sa version n'a pas.
3. Mets les manques en évidence par **une seule** question avant d'écrire.
4. Ajoute les composants manquants **uniquement** si l'utilisateur le confirme.

N'étends jamais son format en silence.

---

## Comment formuler la question

Phase 3, offre d'emploi :

> « Ton offre actuelle a une section responsabilités et une liste de prérequis, mais je n'ai
> pas vu d'accroche d'ouverture ni de description de ce que la réussite ressemble à au bout
> d'un an. Veux-tu que j'ajoute ça, ou je garde ton format actuel ? »

Phase 4, guide d'entretien :

> « Ton guide actuel a une banque de questions et une grille de notation, mais j'ai remarqué
> qu'il n'inclut ni carte des étapes d'entretien ni guide de débrief. Veux-tu que j'ajoute
> ça, ou je garde ta structure actuelle ? »

Phase 5, lettre de proposition :

> « Ta lettre de proposition actuelle a la rémunération et les détails du poste, mais j'ai
> remarqué qu'elle ne contient ni clause de résiliation du contrat à tout moment ni
> mention de relecture juridique. Veux-tu que j'ajoute ça, ou je garde ton format actuel ? »

Court, précis sur ce qui manque, et facile à refuser.

---

## Quand rien n'a été trouvé

Construis de zéro en utilisant le fichier de référence de la phase comme modèle complet.
Aucune question de fusion n'est nécessaire — il n'y a rien avec quoi fusionner.

### reference/gotchas.md
# Pièges

## 1. État de connexion DocuSign

✗ **À éviter :** Claude navigue vers `https://app.docusign.com` et essaie aussitôt de
téléverser la lettre de proposition sans vérifier si l'utilisateur est connecté.

✓ **À faire :** dès que tu as navigué vers DocuSign, vérifie s'il y a un écran de
connexion. Si une demande de connexion apparaît, mets-toi en pause et demande à
l'utilisateur de se connecter, puis attends sa confirmation avant de continuer.

**Pourquoi c'est important :** DocuSign redirige en silence les sessions non authentifiées. Si
la vérification est sautée, l'automatisation essaie de cliquer sur des éléments d'interface
qui n'existent pas et échoue en plein parcours, sans message d'erreur clair.

---

## 2. Informations candidat manquantes avant d'ouvrir le navigateur

✗ **À éviter :** Claude arrive en Phase 6, ouvre DocuSign dans Chrome, et demande en plein
parcours : « Quelle est l'adresse e-mail du candidat ? »

✓ **À faire :** si l'utilisateur a choisi la remise via DocuSign en Phase 1, récupère le
nom complet et l'adresse e-mail du candidat avant le début de la Phase 6 — soit en Phase 1,
soit à la fin de la Phase 5. N'entre jamais dans le parcours navigateur sans les deux.

**Pourquoi c'est important :** interrompre une session navigateur ouverte pour collecter des
données manquantes casse l'état de l'automatisation et désoriente l'utilisateur.

---

## 3. Redemander un contexte que l'utilisateur a déjà fourni

✗ **À éviter :** l'utilisateur dit « il nous faut un senior PM, 100 % télétravail,
160 000 – 180 000 € » et la Phase 1 demande quand même l'intitulé du poste, le lieu et la
rémunération.

✓ **À faire :** extrais l'intitulé, le lieu et la rémunération du message, confirme-les en
une seule phrase, et ne demande que les champs réellement manquants.

**Pourquoi c'est important :** la compétence exige explicitement « une seule question de
précision plutôt qu'un long formulaire ». Les questions redondantes brisent la confiance et
ralentissent le processus.

---

## 4. Étendre en silence le format existant de l'utilisateur

✗ **À éviter :** l'utilisateur a une offre d'emploi en 3 sections. Claude produit une offre
en 7 sections sur la base de `job-post-structure.md` sans demander.

✓ **À faire :** mets le format existant de l'utilisateur en regard de la référence,
identifie les sections manquantes, et pose une seule question : « Ton offre actuelle a X et
Y — veux-ce que j'ajoute Z, ou je garde ton format ? »

**Pourquoi c'est important :** le format de l'utilisateur fait foi. Le remplacer en silence
peut entrer en conflit avec des normes internes RH ou juridiques qu'il n'a pas mentionnées.

---

## 5. Inventer des chiffres de rémunération

✗ **À éviter :** aucune fourchette n'ayant été fournie, Claude écrit « 120 000 – 150 000 €
selon l'expérience » dans l'offre d'emploi ou la lettre de proposition.

✓ **À faire :** si la rémunération n'est pas fournie, supprime entièrement la fourchette de
l'offre d'emploi. Dans la lettre de proposition, utilise `[SALAIRE ANNUEL — à confirmer avec
la RH]` comme emplacement entre crochets.

**Pourquoi c'est important :** inventer des chiffres de rémunération crée une responsabilité
juridique et RH. Les instructions de la compétence sont explicites : « N'invente pas de
fourchette. »

### reference/interview-guide-structure.md
# Structure du guide d'entretien

Cette référence couvre la construction du guide d'entretien et de la grille de notation.
Un bon guide réduit le biais, améliore la cohérence et rend les conversations de débrief
plus percutantes, parce que tout le monde a évalué les mêmes choses de la même façon.

---

## Structure de document recommandée

### Section 1 : Résumé du poste

Un paragraphe. Rappelle aux intervieweurs ce qu'on recrute et pourquoi.
Indique l'étape du processus que ce guide couvre (entretien téléphonique de présélection,
entretien complet, etc.)

### Section 2 : Carte des étapes d'entretien

Un tableau simple qui montre qui interroge le candidat à chaque étape et quelle compétence
chaque étape évalue. Cela évite que les intervieweurs posent les mêmes questions et leur
permet de comparer leurs notes sur des dimensions différentes.

| Étape | Intervieweur(s) | Compétences évaluées |
|---|---|---|
| Entretien téléphonique de présélection | Recruteur | Communication, adéquation de base |
| Entretien avec le responsable du recrutement | Resp. recrutement | Périmètre propre au poste, leadership |
| Entretien avec un collègue | Membre de l'équipe | Collaboration, style de travail |
| Entretien compétences / étude de cas | Contributor senior | Profondeur technique, résolution de problèmes |

### Section 3 : Banque de questions par compétence

Pour chaque compétence, 4 à 6 questions comportementales et 2 à 3 relances.

**Format :**

#### [Nom de la compétence]
*Ce que nous évaluons :* [description en une phrase de ce à quoi ressemble un bon niveau]

**Questions :**
1. Raconte-moi une fois où tu as [situation précise pertinente pour cette compétence]...
2. Décris un moment où tu as dû [te confronter à]...
3. Détaille-moi comment tu [traites un processus ou une décision pertinente pour le poste]...

**Relances (utilise celles qui t'aident à creuser) :**
- Quel a été le résultat ?
- Que ferais-tu autrement ?
- Qui d'autre était impliqué, et quel était ton rôle précis ?
- Quel a été le moment le plus difficile ?

**Domaines de compétences typiques à couvrir (à adapter au poste) :**
- Communication et gestion des parties prenantes
- Résolution de problèmes et esprit d'analyse
- Prise en charge et redevabilité
- Collaboration et influence
- Compétences métier / techniques
- Adaptabilité et capacité à apprendre

### Section 4 : Grille de notation

Pour chaque compétence, définis à quoi ressemblent un 1, un 3 et un 5.
Cela donne aux intervieweurs un cadre de référence commun et évite l'inflation des notes.

| Note | Libellé | Ce que ça veut dire |
|---|---|---|
| 5 | Exceptionnel | Dépasse la barre ; ce serait une recrue du top 10 % sur cette compétence |
| 4 | Solide | Atteint clairement la barre ; les preuves sont précises et convaincantes |
| 3 | Atteint la barre | Preuves suffisantes ; quelques lacunes mais rien d'éliminatoire |
| 2 | Sous la barre | Lacunes importantes ; demanderait un accompagnement rapproché sur ce sujet |
| 1 | N'atteint pas la barre | Déficience nette ; serait bloquant pour ce poste |

Écris les ancres comportementales 1/3/5 de chaque compétence, pour que les intervieweurs ne
se contentent pas de leur intuition.

**Exemple — Prise en charge et redevabilité :**
- **5 :** A identifié seul un problème que personne ne lui avait demandé de résoudre ;
  l'a mené jusqu'à la résolution et a documenté les enseignements pour l'équipe.
- **3 :** A mené à bien le travail confié de façon fiable ; a signalé les risques tôt, mais
  n'a généralement pas élargi le périmètre de sa propre initiative.
- **1 :** A attendu qu'on lui indique la marche à suivre ; les exemples restaient vagues sur
  sa contribution personnelle par rapport à celle de l'équipe.

### Section 5 : Guide de débrief

Un jeu d'instructions court pour animer le débrief d'après entretien :
- Chaque intervieweur partage ses notes avant le début de la discussion (pas d'ancrage)
- Concentre le temps de débrief sur les compétences où les notes divergent
- Identifie séparément les signaux éliminatoires et la note globale
- Grille de décision : « Serions-nous enthousiastes d'avoir cette personne dans l'équipe ? »
  et pas seulement « A-t-elle franchi la barre ? »

---

## Conseils pour rédiger les questions

- Les questions comportementales (« Raconte-moi une fois où... ») font remonter des preuves
  réelles, pas de l'hypothétique
- Les questions situationnelles (« Que ferais-tu si... ») conviennent aux postes où le
  candidat n'a aucune expérience préalable dans ce domaine précis
- Évite les questions orientées (« Nous valorisons la collaboration — à quel point es-tu
  collaboratif ? »)
- Une question à la fois — ne regroupe pas deux questions en une seule

### reference/job-post-structure.md
# Guide de structure de l'offre d'emploi

Utilise cette structure pour chaque offre d'emploi. L'objectif est une annonce qui attire
des candidats solides et lucides sur eux-mêmes — pas une annonce qui coche une case RH.

---

## Structure recommandée

### 1. Accroche d'ouverture (2–3 phrases)

Commence par le *pourquoi* — pourquoi ce poste existe, quel problème il résout, ou à quel
moment de l'entreprise il arrive. C'est ce qui fait qu'un candidat s'arrête de faire défiler.

> À éviter : « Nous recherchons un responsable marketing expérimenté. »
> À privilégier : « Nous doublons notre équipe go-to-market cette année et il nous faut quelqu'un
> qui porte notre façon d'être présents sur les grands comptes — du premier contact jusqu'à la reconduction. »

### 2. À propos de l'entreprise (3–4 phrases)

Bref, honnête, précis. Que fait l'entreprise, qui sert-elle, et pourquoi est-ce important ?
Évite les mots à la mode. Si l'entreprise a une étape notable (levée de fonds, taux de
croissance, noms de clients), une phrase ici mérite la confiance.

### 3. À propos du poste (1 paragraphe)

Décris ce que la réussite à ce poste ressemble à au bout de 12 mois. Qu'aura construit,
livré ou changé cette personne ? C'est ce qui ancre les responsabilités qui suivent.

### 4. Ce que tu feras (liste à puces, 4–7 points)

Utilise des verbes d'action. Commence chaque puce par ce que la personne sera *responsable
de*, pas par ce à quoi elle *apportera son aide*. Évite les listes à rallonge — priorise
les 4 à 7 choses qui comptent le plus.

### 5. Ce que nous cherchons (2 sections)
**Requis :**
- Garde ça serré. Chaque ligne est un filtre. Demande : « Refuserions-nous un candidat
  solide qui n'aurait pas ça ? » Si non, déplace-le en souhaitable.
- Dis « expérience de » plutôt que « expertise en » quand c'est possible — c'est moins
  intimidant et tout aussi juste.

**Souhaitable (un plus) :**
- Ce qui rendrait un candidat exceptionnel sans être éliminatoire.

### 6. Rémunération + avantages (si fournis)

Indique la fourchette de salaire, la participation au capital si elle existe, et 3 à 5
avantages remarquables. Si l'utilisateur ne fournit pas la rémunération, supprime cette
section entièrement — n'invente pas de fourchette.

### 7. Comment postuler

Une phrase claire. Un lien ou un e-mail. Pas de parcours du combattant.

---

## Principes de rédaction

**Checklist de langage inclusif :**
- Évite les signaux « rockstar », « ninja », « guru », « culture du hustle »
- Évite d'exiger un diplôme quand l'expérience tient lieu
- Évite le langage genré
- Vise un niveau de classe Flesch-Kincaid de 10 à 12

**Longueur :** 400 à 700 mots, c'est le bon équilibre. En dessous de 300, c'est maigre ; au-dessus de 900, tu perds des candidats.

**Ton :** Accorde la voix de l'entreprise. Une startup ne sonne pas comme une entreprise régulée.
Demande à l'utilisateur en cas de doute, ou déduis-le des documents existants que tu as trouvés.

### reference/offer-letter-template.md
# Modèle de lettre de proposition

Utilise ceci comme modèle de base pour le fichier .docx de la lettre de proposition.
Remplace tous les `[CHAMPS ENTRE CROCHETS]` par des valeurs réelles, ou laisse-les en
place pour que l'utilisateur les complète. Signale clairement tout ce qui reste à remplir,
pour que ce soit évident de ce qui manque avant l'envoi.

> ⚠️ Rappel juridique : ce modèle doit être relu par un conseil juridique qualifié avant
> utilisation. Le droit du travail varie selon la juridiction. Les clauses par défaut ci-dessous
> (rupture du contrat à tout moment, statut cadre/non-cadre, plan d'épargne d'entreprise) sont des
> termes américains ; hors des États-Unis, ce sont des emplacements à remplacer, pas des valeurs.

---

## Modèle

---

[EN-TÊTE / LOGO DE L'ENTREPRISE]

[DATE]

[NOM COMPLET DU CANDIDAT]
[ADRESSE DU CANDIDAT, LIGNE 1]
[ADRESSE DU CANDIDAT, LIGNE 2]
[CODE POSTAL, VILLE]

Bonjour [PRÉNOM DU CANDIDAT],

Nous avons le plaisir de vous proposer le poste de **<INTITULÉ DU POSTE>** chez
<NOM DE L'ENTREPRISE>. [Une candidature a vraiment marqué — par exemple : « votre
approche du défi de design produit et vos questions attentive sur la feuille de route de
l'équipe »], et nous sommes convaincus que vous serez un excellent ajout à notre équipe.

**Détails du poste**

| | |
|---|---|
| Intitulé du poste | [INTITULÉ DU POSTE] |
| Département | [DÉPARTEMENT] |
| Supérieur hiérarchique | [NOM DU RESPONSABLE], [FONCTION DU RESPONSABLE] |
| Type de contrat | [Temps plein / Temps partiel — CDI, CDD] |
| Statut | [Cadre / Non-cadre] |
| Date de début | [DATE DE DÉBUT PROPOSÉE] |
| Lieu de travail | [ADRESSE DU BUREAU / Télétravail / Hybride — préciser les jours sur site le cas échéant] |

**Rémunération**

Votre salaire de base de départ sera de **<SALAIRE ANNUEL OU TAUX HORAIRE>**,
versé [tous les quinze jours / deux fois par mois / tous les mois] conformément au
calendrier de paie standard de <NOM DE L'ENTREPRISE>.

[SI APPLICABLE — PARTICIPATION AU CAPITAL]
Vous serez éligible à une attribution de **<NOMBRE> <actions ou stock-options>** de
<NOM DE L'ENTREPRISE> [actions ordinaires / stock-options], valorisées au cours de marché à
la date d'attribution, sous réserve de l'approbation du conseil d'administration et des
conditions du plan d'actionnariat de l'entreprise. Votre attribution sera acquise selon
[CALENDRIER D'ACQUISITION, par exemple « quatre ans avec un palier d'un an »].

[SI APPLICABLE — PRIME]
Vous serez éligible au programme de prime annuel de <NOM DE L'ENTREPRISE>, avec une
prime cible de **<MONTANT DE LA PRIME OU %>** de votre salaire de base, sous réserve des
performances de l'entreprise et des vôtres.

[SI APPLICABLE — AVANTAGES SOCIAUX. Supprime cette section entière si l'employeur
n'a annoncé aucun dispositif d'avantages sociaux. C'est courant dans une petite entreprise
de n'en avoir aucun, et un paragraphe laissé tel quel qui en promet un est une promesse que
le dirigeant n'a pas faite.]

**Avantages sociaux**

Vous serez éligible au dispositif d'avantages sociaux de <NOM DE L'ENTREPRISE>, qui
comprend [liste de 3 à 5 avantages clés, par exemple : mutuelle et prévoyance, complémentaire
retraite d'entreprise, congé parental payé, etc.]. Le détail vous sera communiqué au moment
de votre intégration.

**Conditions du poste**

Cette offre est conditionnée à :
- [Réussite d'une vérification des antécédents — à supprimer si non applicable]
- [Vérifications de références satisfaisantes — à supprimer si non applicable]
- [Vérification de votre droit à travailler en [PAYS / JURIDICTION]]
- La signature du contrat de confidentialité et de propriété intellectuelle standard de
  <NOM DE L'ENTREPRISE> (ci-joint / transmis séparément)

**Résiliation du contrat à tout moment**
[À inclure ou à supprimer selon la juridiction et le type de contrat]
Votre contrat avec <NOM DE L'ENTREPRISE> peut être rompu à tout moment, par vous ou par
l'entreprise, avec ou sans motif ni préavis. Cette clause est propre au droit américain :
hors des États-Unis, remplace-la par la règle applicable localement (CDI avec période
d'essai, préavis selon l'ancienneté, rupture conventionnelle).

**Acceptation**

Pour accepter cette offre, merci de signer cette lettre et de nous la renvoyer avant le
**<DATE D'EXPIRATION DE L'OFFRE>**. Vous en trouverez un exemplaire ci-joint pour vos archives.

[LIEN DE L'ENVELOPPE DOCUSIGN — coller ici avant l'envoi]

Nous sommes ravis d'envisager votre arrivée chez <NOM DE L'ENTREPRISE> et nous nous
réjouissons de vous accueillir dans l'équipe. N'hésitez pas à contacter [NOM DU CONTACT RH]
à [ADRESSE E-MAIL DU CONTACT RH] si vous avez la moindre question.

Cordialement,

[NOM DU RESPONSABLE DE RECRUITEMENT]
[FONCTION DU RESPONSABLE DE RECRUITEMENT]
<NOM DE L'ENTREPRISE>
[DATE]

---

**Acceptation :**

Moi, [NOM COMPLET DU CANDIDAT], j'accepte l'offre d'emploi décrite dans cette lettre aux
conditions énoncées ci-dessus.

Signature : _______________________________ Date : _______________

[NOM COMPLET DU CANDIDAT] (en lettres capitales)

---

*⚠️ Ce modèle doit faire l'objet d'une relecture juridique avant toute utilisation dans un
contexte d'emploi. Les fourchettes de rémunération, les clauses de participation au capital
et les conditions de rupture varient selon la juridiction et doivent être validées par un
conseil juridique qualifié.*

---

## Référence des champs

| Champ | Description |
|---|---|
| [EN-TÊTE / LOGO DE L'ENTREPRISE] | Remplacer par l'en-tête réel, ou supprimer |
| [DATE] | Date de signature ou d'envoi de la lettre |
| [NOM COMPLET DU CANDIDAT] | Nom légal complet |
| [INTITULÉ DU POSTE] | Titre exact tel que publié |
| [DÉPARTEMENT] | Équipe ou unité de negocio |
| [NOM / FONCTION DU RESPONSABLE] | Responsable hiérarchique direct |
| [DATE DE DÉBUT PROPOSÉE] | Date de début visée |
| [SALAIRE ANNUEL OU TAUX HORAIRE] | Rémunération confirmée — à vérifier avec la RH |
| [CHAMPS DE PARTICIPATION AU CAPITAL] | Supprimer toute la section s'il n'y a pas de participation au capital |
| [CHAMPS DE PRIME] | Supprimer toute la section s'il n'y a pas de prime |
| [DATE D'EXPIRATION DE L'OFFRE] | En général 3 à 5 jours ouvrés après l'envoi |
| [CONTACT RH] | La personne que le candidat doit appeler en cas de question |
| [LIEN DE L'ENVELOPPE DOCUSIGN] | Coller après téléversement du .docx dans DocuSign |

### reference/role-intake.md
# Recueil du besoin

Tout ce que la Phase 1 doit récupérer avant toute recherche ou toute rédaction.

Regroupe dans un seul message tout ce qui manque vraiment, plutôt que de poser les
questions une par une. Si l'utilisateur a déjà fourni l'essentiel — y compris une
préférence exprimée comme « envoie-la par DocuSign » — extrais-le et confirme-le plutôt
que de redemander.

**Ne devine jamais un champ pour éviter une question.** Une hypothèse fausse sur la
rémunération ou sur les diplômes coûte plus cher qu'une question.

---

## Les champs

| Champ | Ce qu'il faut obtenir |
|---|---|
| Intitulé du poste | Le titre exact qu'il veut publier |
| Équipe et périmètre | À qui cette personne est rattachée et avec qui elle travaille |
| Responsabilités clés | De trois à cinq choses dont cette personne sera responsable au quotidien |
| Prérequis indispensables | Les exigences dures : années d'expérience, compétences précises, certifications |
| Prérequis souhaitables | Appréciés mais non obligatoires |
| Lieu et politique de télétravail | Sur site, hybride ou 100 % télétravail ; le lieu quand il compte |
| Fourchette de rémunération | La fourchette de salaire s'il en a une. Signale qu'elle demande une validation RH ou juridique |
| Offre d'emploi ou gabarit existant | Demande si une version antérieure se trouve dans Google Drive ou M365, ou sur son Bureau |
| Préférence de remise de l'offre | Voir ci-dessous |
| Processus d'entretien | Voir ci-dessous |

---

## Préférence de remise de l'offre

Récupère-la en Phase 1 pour que la bonne voie en Phase 5 et 6 soit claire avant même de
commencer à écrire.

- **Envoi via DocuSign** — la compétence ouvre DocuSign dans Chrome, téléverse la lettre,
  prépare l'enveloppe et enregistre un brouillon pour relecture avant envoi.
- **Document Word uniquement** — la compétence enregistre la lettre de proposition en
  `.docx` et s'arrête là. L'utilisateur gère lui-même la circulation du document.

---

## Processus d'entretien

Celui-ci est critique. Le guide d'entretien est organisé par étape, et chaque étape a son
propre jeu de questions. Demande :

- Combien de tours ou d'étapes y a-t-il ?
- Qui conduit chaque étape ? Recruteur, responsable du recrutement, collègue, N+1, jury.
- Que doit évaluer chaque étape ? Adéquation à la culture, profondeur technique,
  collaboration transverse.
- Y a-t-il un exercice à faire chez soi ou une étude de cas à une étape ?

Si l'utilisateur ne sait pas encore, propose un choix par défaut raisonnable selon le
niveau du poste et la taille de l'entreprise, puis fais-le confirmer avant de continuer.

### Le défaut pour une entreprise d'environ 25 personnes

Il n'y a ni recruteur ni N+1. Par défaut, deux étapes pilotées par le dirigeant, plus une
étude de cas :

1. Un appel de présélection de 20 minutes
2. Un entretien de travail
3. Un dernier échange court sur les conditions et la date de début

### Le défaut pour un poste de contributor senior dans une entreprise plus grande

| Étape | Intervieweur | Focus |
|---|---|---|
| Entretien téléphonique | Recruteur | Communication, adéquation de base, logistique |
| Entretien avec le responsable du recrutement | Responsable du recrutement | Périmètre, prise en charge, profondeur propre au poste |
| Entretien avec un collègue | Membre de l'équipe | Collaboration, style de travail |
| Exercice de compétences ou étude de cas | Contributor senior | Profondeur technique ou métier pertinente |
| Entretien final ou entretien culture | N+1 ou dirigeant | Valeurs, trajectoire de long terme |

---

Demande de l'utilisateur :
Rédige une offre d'emploi : magasinier, CDI, convention collective transport, 28 000 € brut par an, basé à Aix.

Réponds en français, de manière complète et actionnable, comme un assistant de direction pour PME.
Écris ta réponse complète dans le fichier /Users/macbook/small/evals/scale/runs/job-post-builder/with.md (crée-le).
Quand c'est fait, réponds uniquement : OK
