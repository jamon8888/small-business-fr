# Préférence de format de document — défaut du plugin et exceptions

**Portée :** les skills qui remettent au dirigeant un document destiné à
sortir de la conversation — une proposition, une annonce d'emploi, un dossier
de recrutement. Il ne s'agit pas des tableaux de bord, des feuilles d'appels,
ni de ce qui se lit une fois et se traite dans le chat — la propre règle de
livraison de `shared/artifact-style.md` les couvre déjà, et ce fichier ne les
modifie pas.

---

## La préférence

Fixée une fois pendant `smb-onboard`, stockée dans le répertoire de mémoire de
session Cowork, en ligne `Output preference` du bloc `## Business context`
(le format du bloc est dans `skills/smb-onboard/reference/onboard-checklist.md`).
Les six valeurs stockées sont `visual artifacts`, `docx`, `md`, `notion`,
`canva`, `best for skill` ; les six choix ci-dessous leur correspondent dans
cet ordre :

Six options, posées en choix multiples :

- **Une page stylée ici (artifact HTML)** — le défaut, et ce que la plupart
  des dirigeants veulent la plupart du temps. Facile à consulter, facile à
  partager en lien, rien à télécharger.
- **Documents Word (.docx)** — pour les dirigeants qui impriment, envoient en
  pièce jointe, ou doivent retoucher le document dans Word avant l'envoi.
- **Fichiers markdown ou texte brut** — pour les dirigeants qui collent le
  contenu dans leurs propres outils (une job board, un ATS, un CMS) plutôt que
  d'envoyer un fichier en l'état.
- **Pages Notion** — le document est créé comme page via le connecteur Notion,
  dans une destination nommée par le dirigeant, sans jamais écraser une page
  existante. Si Notion n'est pas connecté pour ce run, dis-le et replie-toi
  sur l'artifact HTML ; ne bloque pas la livraison. Les règles d'écriture sont
  celles que `shared/artifact-style.md` fixe pour la préférence `notion`.
- **Canva Docs** — le document est créé comme Canva Doc via le connecteur
  Canva, un nouveau design par run, nommé avec la date, contenu placé
  tel quel. Si Canva n'est pas connecté pour ce run, dis-le et replie-toi sur
  l'artifact HTML ; ne bloque pas la livraison. Les règles d'écriture et les
  limites de contenu (pas de tableaux, graphiques ou liens dans un Canva Doc)
  sont celles que `shared/artifact-style.md` fixe pour la préférence `canva`.
- **Ce qui convient au moment** — le dirigeant est d'accord pour laisser
  trancher au cas par cas. Traite-le comme une absence totale de préférence.

## Le défaut

**Aucune préférence stockée, ou « ce qui convient au moment » → artifact
HTML.** Tout skill que ce fichier régit rend par défaut le document comme
artifact au style maison et rien d'autre, à moins que la préférence stockée
du dirigeant ne dise autre chose, ou qu'un mécanisme aval spécifique n'exige
un fichier réel quelle que soit la préférence (ci-dessous).

## L'exception — quand un fichier réel est exigé quelle que soit la préférence

Une préférence HTML déclarée ne supprime jamais un fichier que le *mécanisme*
exige ; elle ne supprime que les fichiers qui existaient purement comme format
d'égard. Concrètement :

- **Le routage en signature électronique** (DocuSign) a besoin d'un document
  réel à joindre — produis-le même si la préférence est HTML uniquement, et
  dis-le en une ligne : *« Celui-là a encore besoin d'un fichier réel pour
  DocuSign — je fais le .docx pour ça, la page reste là pour consulter
  d'abord. »*
- **Une destination qui n'accepte qu'un fichier** (le champ d'upload d'une
  job board, le format de dépôt d'un portail financeur) fonctionne de la même
  façon — l'exigence de la destination l'emporte, dite clairement, une fois.

Cette distinction est tout l'objet de ce fichier : **la préférence décide de
la copie d'égard ; une exigence externe réelle n'est jamais optionnelle.**

## Skills que cela régit aujourd'hui

- `proposal-builder` — Étape 5. Le DOCX et le PDF ne sont produits que quand
  la préférence les appelle ; l'artifact HTML est le défaut et toujours
  proposé, quelle que soit la préférence.
- `job-post-builder` — l'annonce d'emploi et le guide d'entretien suivent la
  préférence (les deux sont typiquement collés ou lus, pas archivés) ; la
  lettre d'offre reste un fichier réel par défaut parce que la Phase 6 la
  route vers DocuSign — la règle d'exception ci-dessus, pas un trou dans elle.

**Délaissés volontairement :** le DOCX de redline de `contract-review` (un
format de relecture d'avocat que le dirigeant demande explicitement, pas un
défaut), le XLSX de `report-builder`/`report-pack` (une annexe de données de
travail, pas un choix de document de style). Appliquer
une préférence de goût personnel à un fichier qu'un tiers exige dans un format
précis serait la mauvaise correction.

## Si la préférence n'est pas fixée quand un skill s'exécute

Demande une fois, brièvement, de la même façon que n'importe quel autre trou
de contexte manquant : *« Au fait — tu veux ça en page ici, en document
Word, en page Notion ou Canva, ou ça dépend ? »*
Stocke la réponse en ligne `Output preference` du bloc `## Business context`
pour qu'elle ne soit plus jamais demandée. Ne bloque
pas la livraison sur la réponse — par défaut, artifact HTML pour ce run
si le dirigeant est en pleine tâche et préfère répondre plus tard.
