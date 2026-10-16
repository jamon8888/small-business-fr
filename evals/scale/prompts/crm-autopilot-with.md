Tu es un assistant pour dirigeants de PME françaises.
Le skill suivant est à ta disposition — suis-le pour répondre :

### SKILL.md
---
name: crm-autopilot
description: >
  Met à jour le CRM : Sellsy, Axonaut, noCRM, Pipedrive en pairs. Ajoute
  SIREN, effectif, forme juridique, commercial affecté, grille, plafond.
  RGPD dans les notes.
  [EN] Updates the CRM: Sellsy, Axonaut, noCRM, Pipedrive.
---

> Language rule: see `shared/language.md`.

# crm-autopilot

## Connecteurs
Sellsy, Axonaut, noCRM.io, Pipedrive, HubSpot, Salesforce.

## Champs B2B à ajouter
siren, effectif, forme_juridique, commercial_affecte, grille_tarifaire,
plafond_encours, assurance_credit.

## RGPD
- Minimisation des données dans les notes.
- Pas de donnée personnelle superflue.
- Durée de conservation respectée.

## Lien cluster Shopify
Cette compétence dialogue avec la boutique en ligne via `shopify-customers` (hub : `shopify-hub`, doc : [AI Toolkit](../../shared/shopify-ai-toolkit.md)).


### reference/cleanup-checklist.md
# Liste de contrôle du nettoyage

Les champs que le skill `crm-autopilot` vérifie lors du nettoyage d'une affaire, plus les éléments de preuve nécessaires pour signaler chacun. Il s'exécute quand l'utilisateur dit « nettoie HubSpot », « nettoie Salesforce » ou « cette affaire est-elle à jour », sur une affaire précise.

Passe en revue chaque point. Présente les constats sous forme de liste de contrôle ; n'écris que ce que l'utilisateur approuve.

**Les noms de champs ci-dessous sont ceux de HubSpot.** Sur Salesforce, les mêmes vérifications lisent ces champs sur `Opportunity`, via le flux discover → describe → dispatch_readonly décrit dans `salesforce-fields.md` :

| Vérification | HubSpot | Salesforce |
|---|---|---|
| 1. Dernière activité | `notes_last_updated` | `LastActivityDate` (null = rien de jamais journalisé) |
| 2. Prochaine étape | `hs_next_step` | `NextStep` |
| 3. Étape | `dealstage` | `StageName` — signalée uniquement, jamais écrite |
| 4. Date de closing | `closedate` | `CloseDate` |
| 5. Montant | `amount` | `Amount` — signalé uniquement, jamais écrit |
| 6. Contacts rattachés | rattachements de l'affaire | sous-requête `OpportunityContactRoles` ; une personne manquante est créée comme `Contact` (ou signalée comme un `Lead` existant non converti) avant qu'un rôle soit proposé |
| 7. Notes | notes portées sur l'affaire | enregistrements `Task` et `Event` rattachés à l'opportunity ; une note de clarification est une nouvelle `Task` avec `Status` = Completed, jamais une modification |

## 1. Date de dernière activité

**Vérification :** le `notes_last_updated` de l'affaire est-il plus ancien que la dernière interaction réelle (email ou réunion) impliquant ses contacts rattachés ?

**Éléments de preuve à signaler :** un fil d'emails ou un événement d'agenda de moins de 14 jours avec l'un des contacts de l'affaire, plus récent que `notes_last_updated`.

**Action proposée :** proposer de journaliser l'activité manquante. Ne marque pas l'affaire elle-même ; journaliser l'activité met `notes_last_updated` à jour automatiquement.

## 2. Champ prochaine étape (`hs_next_step`)

**Vérification :** le `hs_next_step` actuel reflète-t-il toujours ce qui a été convenu lors du dernier email ou de la dernière réunion ?

**Éléments de preuve à signaler :** le champ indique « envoyer la grille tarifaire » et un email ultérieur montre que la grille a bien été envoyée. Ou le champ est vide alors qu'une réunion récente a explicitement fixé une action suivante.

**Action proposée :** proposer une nouvelle valeur (ou une valeur vide si l'étape est franchie). Affiche l'actuel → le proposé côte à côte.

## 3. Étape de l'affaire (`dealstage`)

**Vérification :** les interactions récentes laissent-elles penser que l'affaire a changé d'étape — par exemple proposition envoyée, contrat signé, perdue face à un concurrent ?

**Éléments de preuve à signaler :** une formulation explicite dans les notes d'email ou de réunion comme « nous avançons », « nous avons signé », « nous sommes allés chez [concurrent] », ou un changement de rythme dans les réunions.

**Action proposée :** **signaler uniquement — ne jamais changer d'étape automatiquement.** Mets les éléments de preuve en avant et laisse l'utilisateur décider.

## 4. Date de closing (`closedate`)

**Vérification :** le dernier email ou la dernière réunion fait-il référence à un calendrier révisé qui contredit le `closedate` actuel ?

**Éléments de preuve à signaler :** des formulations comme « ça glisse au T3 », « nous signerons d'ici la fin du mois », ou « décalé jusqu'au prochain trimestre ».

**Action proposée :** proposer une date mise à jour. Affiche l'actuelle → la proposée.

## 5. Montant (`amount`)

**Vérification :** le dernier email ou la dernière réunion mentionne-t-il une taille d'affaire différente ?

**Éléments de preuve à signaler :** une révision explicite des tarifs dans un email de tarification, un périmètre élargi en réunion, ou un périmètre réduit que le client a accepté.

**Action proposée :** proposer un montant mis à jour. Affiche l'actuel → le proposé.

## 6. Contacts rattachés

**Vérification :** y a-t-il des personnes participant à des emails ou réunions récents avec les contacts de l'affaire qui ne soient pas elles-mêmes rattachées à l'affaire ?

**Éléments de preuve à signaler :** une copie d'un email ou un participant de réunion dont le domaine correspond au domaine d'un contact existant de l'affaire, sans que la personne figure sur l'affaire.

**Action proposée :** proposer d'ajouter le ou les contacts manquants à l'affaire. Crée d'abord le contact dans le CRM s'il n'existe pas encore (sur Salesforce : un `Contact`, puis un `OpportunityContactRole` ; les deux annoncés avant écriture).

## 7. Hygiène des notes

**Vérification :** y a-t-il des notes ou des activités de plus de 90 jours qui contredisent explicitement l'état actuel de l'affaire ?

**Éléments de preuve à signaler :** une note indiquant « client perdu » sur une affaire encore à une étape ouverte, ou une note mentionnant un montant de contrat périmé.

**Action proposée :** ajouter une nouvelle note clarifiant l'état actuel — **ne modifie ni ne supprime jamais** l'ancienne note. Ajoute, ne réécris pas l'historique.

## Format de sortie

Présente les constats sous forme de liste numérotée, chaque point indiquant :
- Ce qui a été signalé
- Les éléments de preuve (objet d'email + date, ou titre de réunion + date)
- L'action proposée (ou « signalement seul » pour les changements d'étape)

Demande ensuite une approbation point par point ou en bloc. N'écris que ce qui est approuvé.

### reference/examples/cleanup-deal.md
# Exemple : nettoyer une affaire périmée

Scénario déroulé pour le chemin nettoyage — l'utilisateur demande au skill d'auditer une affaire précise, le skill remonte les constats et attend une approbation.

## Préparation

- Affaire : « Acme Q2 Expansion » — étape « Proposal Sent », montant 18 000 €, date de closing le 15 mai, prochaine étape « envoyer la grille tarifaire », `notes_last_updated` il y a 22 jours
- L'affaire a deux contacts rattachés : Sarah Lin et Ben Rivera
- Les 14 derniers jours d'emails avec Sarah comprennent un fil daté du 18 avril intitulé « Re: Acme pricing » dans lequel Sarah a confirmé la grille tarifaire et dit « nous signerons dès que notre revue juridique sera terminée, mi-juin »
- Un événement d'agenda du 20 avril intitulé « Acme — legal review walkthrough » incluait une nouvelle personne, `maria.chen@acme.com`, qui n'est ni dans HubSpot ni sur l'affaire
- Aucun email, réunion ou note ne suggère que l'affaire a changé d'étape

## Ce que dit l'utilisateur

> « Nettoie l'affaire Acme Q2 Expansion. »

## Comportement du skill

**Étape 1 — Identifier l'intention.**
Chemin nettoyage, limité à une affaire nommée.

**Étape 2 — Rassembler le contexte.**
Récupère l'enregistrement de l'affaire. Récupère les fils d'emails des 14 derniers jours impliquant Sarah et Ben. Récupère les événements d'agenda de la même période.

**Étape 3 — Résoudre.**
Affaire explicitement nommée — aucune résolution nécessaire. Contacts présents sur les emails et réunions récents : Sarah (sur l'affaire), Ben (sur l'affaire), Maria Chen (pas sur l'affaire, pas dans HubSpot).

**Étape 4 — Parcourir la liste de contrôle du nettoyage.**

Le skill n'écrit RIEN pour l'instant. Produit cette liste de contrôle :

> **Revue du nettoyage — Acme Q2 Expansion**
>
> **1. Date de dernière activité.** L'affaire indique 22 jours. Activité plus récente trouvée : email du 18 avril de Sarah (« Re: Acme pricing »), réunion du 20 avril (« Acme — legal review walkthrough »). Rien n'est journalisé dans HubSpot.
> **→ Propose :** Journaliser l'email du 18 avril et la réunion du 20 avril comme activités sur cette affaire.
>
> **2. Champ prochaine étape.** Actuellement « envoyer la grille tarifaire ». L'email du 18 avril montre que la grille a été envoyée et confirmée par Sarah.
> **→ Propose :** `hs_next_step` : « envoyer la grille tarifaire » → « attendre la validation de la revue juridique ».
>
> **3. Étape de l'affaire.** Actuellement « Proposal Sent ». Aucun élément ne indique un mouvement d'étape — Sarah a dit qu'ils signeront *après* la revue juridique. L'étape est cohérente avec la réalité.
> **→ Signalement uniquement — aucun changement.**
>
> **4. Date de closing.** Actuellement le 15 mai. L'email de Sarah du 18 avril dit « mi-juin ».
> **→ Propose :** `closedate` : 15 mai → 15 juin.
>
> **5. Montant.** Actuellement 18 000 €. L'email du 18 avril confirme 50 sièges à 360 € = 18 000 €. Aucun changement nécessaire.
> **→ Aucune action.**
>
> **6. Contacts rattachés.** Maria Chen (`maria.chen@acme.com`) a participé à la réunion de revue juridique du 20 avril. Pas sur l'affaire, pas dans HubSpot.
> **→ Propose :** Créer le contact et le rattacher à l'affaire.
>
> **7. Hygiène des notes.** Aucune note contradictoire trouvée sur les 90 derniers jours.
> **→ Aucune action.**
>
> > J'approuve les points 1, 2, 4 et 6 pour l'écriture ? Ou précise lesquels.

**Étape 5 — Porte d'approbation.**
Attend l'utilisateur. L'utilisateur répond : « *Oui pour tous sauf 4 — laisse la date de closing tranquille, elle est peut-être optimiste.* »

**Étape 6 — Exécuter les points approuvés.**
- Journalise l'email du 18 avril comme activité email
- Journalise la réunion du 20 avril comme activité d'appel avec les participants Sarah, Ben et Maria (nouvellement créée)
- Met à jour `hs_next_step` en « attendre la validation de la revue juridique »
- Ne met PAS à jour `closedate`
- Crée le contact Maria Chen et le rattache à l'affaire

**Compte rendu.**

> Modifications écrites sur Acme Q2 Expansion :
> - Activités email du 18 avril et appel du 20 avril journalisés
> - Prochaine étape mise à jour en « attendre la validation de la revue juridique »
> - Contact Maria Chen (maria.chen@acme.com) créé et ajouté à l'affaire
> - Date de closing inchangée, conformément à ta décision.
> - L'étape de l'affaire a été signalée comme cohérente avec la réalité — aucun changement nécessaire.
> [HubSpot : Acme Q2 Expansion]

## Ce que cet exemple illustre

- Chaque vérification de champ de `../cleanup-checklist.md` appliquée à une seule affaire
- Cadrage côte à côte actuel → proposé pour chaque changement proposé
- Changement d'étape correctement retenu comme simple signalement
- L'utilisateur approuve des points de façon sélective — le skill respecte exactement la sélection
- Création du contact intégrée au même cycle d'approbation

### reference/examples/log-call-happy-path.md
# Exemple : journaliser un appel avec un contact manquant

Scénario déroulé pour le chemin appel — l'événement d'agenda compte trois participants, dont un n'est pas encore dans HubSpot.

## Préparation

- L'utilisateur vient de terminer un Google Meet de 30 minutes intitulé « Acme — technical deep dive » à 10h00
- Participants sur l'invitation d'agenda : l'utilisateur, `sarah.lin@acme.com`, `ben.rivera@acme.com`
- Sarah Lin est un contact HubSpot existant sur l'affaire « Acme Q2 Expansion »
- Ben Rivera n'est PAS dans HubSpot
- L'affaire Acme Q2 Expansion est la seule affaire ouverte de Sarah

## Ce que dit l'utilisateur

> « Journalise cet appel. »

## Comportement du skill

**Étape 1 — Identifier l'intention.**
Chemin appel. Aucun événement nommé — repli sur la réunion terminée la plus récente, dans les dernières 24 heures.

**Étape 2 — Rassembler le contexte.**
Retrouve l'événement « Acme — technical deep dive » de 10h00. Confirme avec l'utilisateur avant d'aller plus loin :

> « Je journalise l'appel "Acme — technical deep dive" de ce matin à 10h00 — c'est bien ça ? »

L'utilisateur confirme.

Lit les détails de l'événement : 30 minutes, participants externes `sarah.lin@acme.com` et `ben.rivera@acme.com`. Aucune description sur l'événement.

**Étape 3 — Résoudre le contact et l'affaire.**
- Recherche `sarah.lin@acme.com` → existe (Sarah Lin, sur Acme Q2 Expansion).
- Recherche `ben.rivera@acme.com` → n'existe pas.
- Annonce la création du contact :

> « Ben Rivera (ben.rivera@acme.com) n'est pas dans HubSpot. Je crée le contact et je le rattache à l'affaire Acme Q2 Expansion. »

Crée le contact avec `email`, `firstname: Ben`, `lastname: Rivera`, `company: Acme` (déduit du domaine de l'email). Le rattache à l'affaire.

Résolution de l'affaire : la seule affaire ouverte de Sarah est Acme Q2 Expansion — correspondance sans ambiguïté.

**Étape 4 — Exécuter.**
Écrit une activité d'appel sur Acme Q2 Expansion :
- `hs_call_title` : Acme — technical deep dive
- `hs_call_body` : « Réunion tenue ; notes à ajouter. » (Aucune description sur l'événement d'agenda ; la valeur provisoire est signalée à l'utilisateur pour qu'il sache qu'il faut ajouter du détail.)
- `hs_call_duration` : 30 min
- `hs_timestamp` : 10h00 aujourd'hui
- Contacts rattachés : Sarah Lin, Ben Rivera
- Affaire rattachée : Acme Q2 Expansion

**Étape 5 — Porte d'approbation.**
Création du contact annoncée avant écriture. L'écriture de l'activité est faite dans le flux, conformément à la demande explicite « journalise cet appel » de l'utilisateur.

**Étape 6 — Rendre compte.**

> Activité d'appel journalisée sur Acme Q2 Expansion :
> « Acme — technical deep dive » (30 min, 10h00)
> Contact créé : Ben Rivera (ben.rivera@acme.com) — rattaché à l'affaire.
> Le corps de l'appel est une valeur provisoire — ajoute tes notes si tu veux les voir sur la chronologie de l'affaire.
> [HubSpot : Acme Q2 Expansion]

## Ce que cet exemple illustre

- Repli sur la réunion la plus récente quand l'utilisateur ne précise pas d'événement
- Confirmation avant d'agir sur un contexte déduit
- Création de contact avec entreprise déduite du domaine de l'email
- Corps provisoire avec notification de l'utilisateur quand il n'existe pas de notes de réunion
- Rattachement de plusieurs contacts (existant + nouvellement créé) à la même activité

### reference/examples/log-email-happy-path.md
# Exemple : journaliser un email sur une affaire existante (cas nominal)

Scénario déroulé pour le chemin email — le contact existe, l'affaire se résout sans ambiguïté, l'activité se journalise proprement.

## Préparation

- L'utilisateur consulte un fil d'emails dont l'objet est « Acme Q2 pricing follow-up »
- Le fil contient trois messages entre l'utilisateur et `sarah.lin@acme.com` sur les deux derniers jours
- `sarah.lin@acme.com` est un contact existant dans HubSpot
- Elle est rattachée à exactement une affaire ouverte : « Acme Q2 Expansion » (proposition envoyée, 18 000 €, date de closing le 15 mai)

## Ce que dit l'utilisateur

> « Ajoute ce fil à l'affaire. »

## Comportement du skill

**Étape 1 — Identifier l'intention.**
Chemin email (l'utilisateur a dit « ce fil »).

**Étape 2 — Rassembler le contexte.**
Lit le fil. Objet : « Acme Q2 pricing follow-up. » Dernier message (hier, 16h12) de Sarah : « *Confirmé, 50 sièges à 360 €/siège, ça marche. J'envoie le cahier des charges signé vendredi.* » Contact externe principal : `sarah.lin@acme.com`.

**Étape 3 — Résoudre le contact et l'affaire.**
Recherche `sarah.lin@acme.com` → le contact existe (Sarah Lin, Acme Corp). Trouve les affaires ouvertes rattachées à elle : exactement une, « Acme Q2 Expansion ». La correspondance est sans ambiguïté.

**Étape 4 — Exécuter.**
Écrit une activité email sur Acme Q2 Expansion :
- `hs_email_subject` : Acme Q2 pricing follow-up
- `hs_email_text` : « Sarah a confirmé 50 sièges à 360 €/siège (18 000 €). Cahier des charges signé vendredi. »
- `hs_timestamp` : hier, 16h12
- Contact rattaché : Sarah Lin
- Affaire rattachée : Acme Q2 Expansion

**Étape 5 — Porte d'approbation.**
Le contact existait déjà, pas d'annonce de création nécessaire. L'écriture de l'activité se fait dans le flux — pas de porte séparée puisque l'utilisateur l'a explicitement demandée.

**Étape 6 — Rendre compte.**

> Activité email journalisée sur Acme Q2 Expansion :
> « Sarah a confirmé 50 sièges à 360 €/siège (18 000 €). Cahier des charges signé vendredi. »
> Horodatage hier 16h12. Aucun contact créé — Sarah était déjà sur l'affaire.
> [HubSpot : Acme Q2 Expansion]

## Ce qui en fait le cas nominal

- Rattachement à une affaire unique et sans ambiguïté — aucun rapprochement approximatif nécessaire
- Le contact existait déjà — pas de flux de création
- L'objet du fil est explicite — utilisable tel quel comme titre d'activité
- Le résumé porte sur les décisions et les chiffres, pas sur la transcription complète du fil

### reference/gotchas.md
# Pièges

Les cas limites où le skill `crm-autopilot` a le plus de chances de produire de mauvaises données dans le CRM. Chaque entrée suit le schéma Bon / Mauvais.

---

## Piège : créer un contact en double quand l'email est déjà dans HubSpot avec une casse différente

**Pourquoi c'est important :** HubSpot dédoublonne sur correspondance exacte d'email. `Sarah.Lin@acme.com` et `sarah.lin@acme.com` sont traités comme distincts, et un dirigeant qui a déjà créé l'un verra apparaître un doublon silencieux. Cela détruit la confiance que le dirigeant porte au skill.

### ✗ Mauvais

> Recherche de `Sarah.Lin@acme.com` dans HubSpot — aucun résultat. Création d'un nouveau contact : Sarah Lin (Sarah.Lin@acme.com).

Le nouveau contact est créé ; le contact `sarah.lin@acme.com` existant du dirigeant a désormais un doublon.

### ✓ Bon

> Recherche de `sarah.lin@acme.com` dans HubSpot (insensible à la casse) — aucun résultat. Création d'un nouveau contact : Sarah Lin (sarah.lin@acme.com). Annoncée avant écriture.

Normalise toujours l'email en minuscules avant la recherche. Annonce la création pour que le dirigeant puisse rattraper les oublis.

---

## Piège : écrire le fil d'emails complet comme corps de l'activité

**Pourquoi c'est important :** les activités HubSpot sont des surfaces de signal à parcourir rapidement, pas des archives de transcriptions. Un fil de 12 messages collé dans le corps de l'activité ne sert à rien ; un résumé de trois phrases sur ce qui a été convenu est actionnable.

### ✗ Mauvais

> **Corps de l'activité :**
> *De : Sarah Lin — jeu. 9 avr.…*
> *Bonjour ! Je reviens vers toi après notre appel ; voici les spécifications que nous avons évoquées…*
> *[1 200 mots de plus]*

Le dirigeant passe dessus à chaque fois.

### ✓ Bon

> **Corps de l'activité :** Sarah a confirmé le périmètre de l'extension du T2 — 50 sièges, 18 000 € de CA annuel, démarrage le 1er juin. Elle enverra le cahier des charges signé d'ici vendredi. Aucune question ouverte.

Le résumé nomme les décisions, les chiffres et la prochaine étape.

---

## Piège : créer automatiquement une affaire quand la bonne ne peut pas être résolue

**Pourquoi c'est important :** les affaires en double sont très difficiles à démêler dans HubSpot — elles divisent l'historique d'activité, brouillent les rapports, et le dirigeant s'en rend compte en général des semaines plus tard, quand une prévision ne colle pas.

### ✗ Mauvais

> Aucune affaire ouverte trouvée pour Sarah Lin chez Acme. Création d'une nouvelle affaire : « Acme — nouvelle opportunité », et journalisation de l'appel dessus.

Il y a maintenant deux affaires Acme, et le dirigeant n'a aucune idée de laquelle est la vraie.

### ✓ Bon

> Aucune affaire ouverte trouvée pour Sarah Lin chez Acme. Sur quelle affaire dois-je journaliser cela ? Options : (1) Extension Acme T2 (close-won en février), (2) Renouvellement Acme 2027 (ouverte). Ou veux-tu ne rien journaliser pour l'instant ?

Demande. Ne crée jamais une affaire à la place du dirigeant.

---

## Piège : résoudre contre un portail vide

**Pourquoi c'est important :** un portail HubSpot tout neuf renvoie zéro contact et zéro affaire, et chaque étape de résolution « échoue » ensuite d'une manière qui ressemble à un problème de données. Le skill se met à proposer des contacts à créer et des affaires où journaliser, et le dirigeant se retrouve avec un CRM rempli par un passage de journalisation au lieu de l'être par sa propre configuration.

### ✗ Mauvais

> Aucun contact trouvé pour sarah@acme.com. Création du contact. Aucune affaire ouverte trouvée — sur quelle affaire dois-je journaliser cela ? (aucune listée)

Le portail ne contient rien. Il n'y a aucune affaire à choisir.

### ✓ Bon

> Ton CRM ne contient encore ni contacts ni affaires — il a l'air tout neuf. Je peux garder ce journal d'appels dans le CRM tableur jusqu'à ce qu'il soit alimenté (sur HubSpot, je peux aussi lancer sa configuration). Tu préfères lequel ?

Vérifie d'abord les compteurs (étape 3). Un portail vide est une question de configuration, pas un problème de résolution. N'utilise pas l'indicateur `onboarded` de `get_user_details` comme test : un portail rempli de contacts peut toujours renvoyer `onboarded: false`. L'indicateur dit si la configuration guidée de HubSpot a été exécutée, pas s'il y a des données.

---

## Piège : proposer un changement d'étape d'affaire sur la base du langage d'un email

**Pourquoi c'est important :** « nous avançons » dans un email ne signifie pas toujours « passer en close-won ». Les clients le disent quand ils avancent dans leur évaluation, ou dans une étape d'achats. Le dirigeant a un contexte que le skill n'a pas. Faire avancer l'étape automatiquement est destructeur pour le pipeline.

### ✗ Mauvais

> L'email de Sarah indique « nous avançons ». Proposition de passer `dealstage` → Closed Won. Écriture immédiate.

### ✓ Bon

> Signalement : l'email du 18 avril de Sarah (« nous avançons dans l'évaluation d'Anthropic ») peut indiquer un mouvement d'étape. L'étape actuelle est « Proposal Sent ». Veux-tu la faire avancer ? Je ne changerai pas l'étape sans ton accord explicite.

Mets les éléments de preuve en avant, retiens l'écriture.

---

## Piège : écraser une prochaine étape définie par le dirigeant pendant le nettoyage

**Pourquoi c'est important :** le dirigeant a pu fixer une prochaine étape qui traduit un contexte que le skill ne voit pas — un appel téléphonique, un fil Slack, une note privée. L'écraser parce qu'un email récent suggère autre chose efface un vrai travail.

### ✗ Mauvais

> `hs_next_step` indique actuellement « attendre la revue juridique ». Le dernier email de Sarah indique « planifions la revue tarifaire ». Mise à jour de `hs_next_step` en « planifier la revue tarifaire ».

### ✓ Bon

> `hs_next_step` indique actuellement « attendre la revue juridique » (défini par toi il y a 3 jours). L'email de Sarah du 19 avril suggère qu'une revue tarifaire est également nécessaire. Je propose d'ajouter ou de remplacer ? Actuel → Proposé : « attendre la revue juridique » → « attendre la revue juridique ; puis planifier la revue tarifaire. » Tu approuves ?

Affiche la valeur actuelle, propose explicitement le changement, attends l'approbation.

### reference/hubspot-fields.md
# Champs et types d'activité HubSpot

Les objets, propriétés et types d'activité HubSpot précis que le skill `crm-autopilot` lit et écrit. Seuls les champs listés ici sont dans le périmètre de ce skill — tout le reste de HubSpot reste intact.

## Contacts — écriture

| Champ         | Usage                                                                                  |
|---------------|----------------------------------------------------------------------------------------|
| `email`       | Identifiant principal pour la recherche et le dédoublonnage. Toujours renseigné à la création.  |
| `firstname`   | Renseigné depuis la signature d'email ou l'invitation d'agenda si elle est disponible. Laisser vide si inconnu.      |
| `lastname`    | Renseigné depuis la signature d'email ou l'invitation d'agenda si elle est disponible. Laisser vide si inconnu.      |
| `company`     | Renseigné depuis le domaine de l'email ou l'organisation de l'invitation d'agenda si elle est disponible.                 |

N'écris aucune autre propriété contact. Le responsable, l'étape du cycle de vie et la source du lead sont des champs gérés par l'utilisateur — ne les écrase jamais.

## Contacts — lecture (pour la recherche)

| Champ         | Usage                                                              |
|---------------|--------------------------------------------------------------------|
| `email`       | Clé de recherche. Correspondance exacte, insensible à la casse.                          |
| `firstname` · `lastname` · `company` | Montrés à l'utilisateur lors de la résolution d'ambiguïtés. |
| `hs_object_id`| Sert au rattachement avec les affaires et les activités.                    |

## Deals — lecture (tous les chemins de nettoyage et de résolution)

| Champ                       | Usage                                                    |
|-----------------------------|----------------------------------------------------------|
| `dealname`                  | Montré à l'utilisateur ; sert au rapprochement approximatif avec l'objet de l'email ou le sujet de la réunion |
| `dealstage`                 | Lecture seule pendant le nettoyage — signaler les écarts, ne jamais modifier |
| `amount`                    | Lu pendant le nettoyage ; signaler si un email ou une réunion récent laisse entendre un changement |
| `closedate`                 | Lu pendant le nettoyage ; signaler s'il n'est plus à jour                    |
| `hs_next_step`              | Lu et mis à jour proposé pendant le nettoyage                    |
| `hubspot_owner_id`          | Montré à l'utilisateur ; jamais modifié                     |
| `notes_last_updated`        | Sert à repérer les affaires périmées. C'est le « Last Activity Date » de HubSpot sur l'objet deal. Il n'existe pas de propriété `hs_lastactivitydate` — n'en cherche pas |
| Contacts rattachés         | Sert à déterminer si les participants d'un email ou d'une réunion récente figurent sur l'affaire |

## Deals — écriture (chemin de nettoyage uniquement, avec approbation)

| Champ           | Règle                                                             |
|-----------------|------------------------------------------------------------------|
| `hs_next_step`  | Proposer des mises à jour ; écrire uniquement sur approbation explicite de l'utilisateur          |
| `closedate`     | Proposer des mises à jour ; écrire uniquement sur approbation explicite de l'utilisateur          |
| `amount`        | Proposer des mises à jour ; écrire uniquement sur approbation explicite de l'utilisateur          |
| Rattachement de contact  | Proposer d'ajouter les participants manquants à l'affaire ; écrire uniquement après approbation |

**N'écris jamais** `dealstage`, `pipeline`, `hubspot_owner_id` ni aucune propriété personnalisée pendant le nettoyage. Ces champs sont gérés par le dirigeant.

## Activities — écriture

| Type d'activité                  | Utilisé par        | Champs renseignés                                                               |
|--------------------------------|----------------|--------------------------------------------------------------------------|
| Engagement email (`EMAIL`)     | Chemin email     | `hs_email_subject` (objet du fil), `hs_email_text` (résumé, pas le fil complet), `hs_timestamp` (horodatage du dernier message), contact(s) + affaire rattachés |
| Engagement appel (`CALL`)       | Chemin appel      | `hs_call_title` (titre de l'événement), `hs_call_body` (résumé), `hs_call_duration` (depuis l'agenda), `hs_timestamp` (début de l'événement), contact(s) + affaire rattachés |
| Note (`NOTE`)                  | Chemin nettoyage   | `hs_note_body` (pour signaler quelque chose à revoir plus tard qui n'entre dans aucun champ) |

Utilise le vocabulaire d'engagement standard de HubSpot. N'invente pas de types d'activité personnalisés.

## Règles de rattachement

- Toute activité doit être rattachée à l'affaire ET à au moins un contact.
- Si un contact est créé à la volée pendant le journalisement d'une activité, rattache-le à l'affaire dans la même opération, afin que l'activité apparaisse sur les deux chronologies, contact et affaire.
- Ne rattache pas un contact à une affaire pendant un flux de journalisation d'activité, sauf si ce contact participe réellement au fil d'emails ou à la réunion concerné.

### reference/lightweight_crm.md
# Le CRM léger

Pour les dirigeants qui n'ont aucun CRM — une large part de ce segment. Leur dire d'acheter HubSpot n'est pas une réponse, et c'est précisément le moment où le skill cesserait d'être utile.

Construis-leur un CRM dans un tableur ou dans Notion, et tiens-le exactement de la même manière.

---

## Où il vit

**Google Sheets ou Excel** — le choix par défaut. Tout dirigeant peut l'ouvrir, le partager et l'emporter avec lui.

**Notion** — quand ils l'utilisent déjà. Mieux pour les notes, moins bon pour tout ce qui est numérique.

**Monday.com** — quand ils l'utilisent déjà, et le plus solide des trois. Les éléments du board font office
d'enregistrements, les mises à jour par colonne fonctionnent, et la chronologie du contact contient déjà
les emails, les appels, les réunions et les notes. Lecture et écriture dans les deux cas. Si le dirigeant
est dans Monday.com tous les jours, tenir ses boards à jour vaut mieux que construire un tableur qu'il
oubliera d'ouvrir.

**Un fichier local** — quand rien n'est connecté. Ça fonctionne quand même.

Demande une fois, puis arrête de demander.

---

## Structure

Quatre onglets. Résiste à l'envie d'en ajouter — chaque champ supplémentaire est un champ qui devient
périmé et qui donne au tableur l'air d'un devoir à la maison.

### Contacts

| Colonne | Notes |
|---|---|
| Nom | |
| Entreprise | |
| Email | |
| Téléphone | |
| Fonction | |
| Premier contact | Date |
| Dernier contact | Mis à jour automatiquement à chaque activité journalisée |
| Notes | |

### Affaires

| Colonne | Notes |
|---|---|
| Affaire | Nom court que le dirigeant reconnaît |
| Entreprise | |
| Contact | |
| Montant | |
| Étape | N'en garde que quatre : Nouveau, Devis envoyé, Gagnée, Perdue |
| Prochaine étape | La colonne la plus importante |
| Date de prochaine étape | |
| Dernière activité | Mise à jour automatiquement |
| Source | Comment ils ont connu l'entreprise |
| Notes | |

**Quatre étapes, pas huit.** Les dirigeants sans CRM n'ont pas besoin d'une taxonomie de pipeline ; ils ont
besoin de savoir quoi faire ensuite. Davantage d'étapes, c'est davantage d'enregistrements qui traînent
dans la mauvaise.

### Activité

| Colonne | Notes |
|---|---|
| Date | Quand c'est arrivé, pas quand c'est journalisé |
| Type | Email, appel, réunion, note |
| Contact | |
| Affaire | |
| Résumé | Trois à cinq lignes |
| Prochaine étape définie | Oui ou non |

Ajout uniquement. Ne modifie jamais l'historique — cet onglet est la trace sur laquelle le dirigeant s'appuie
quand il ne se souvient plus de ce qui a été convenu.

### File

Une vue filtrée, pas un quatrième jeu de données : toutes les affaires ouvertes sans prochaine étape, ou
dont la date de prochaine étape est dépassée. C'est l'onglet que le dirigeant ouvre réellement.

---

## Le tenir à jour

Identique au chemin HubSpot. Mêmes modes, mêmes portes d'approbation, mêmes règles.

- Journaliser l'activité à partir des emails, de l'agenda et des transcriptions
- Mettre à jour Dernier contact et Dernière activité automatiquement
- Proposer les changements de champs, ne jamais écrire l'étape ni le montant sans approbation
- Rédiger des relances sur les affaires en sommeil
- Tenir la file à jour

La seule vraie différence, c'est que résoudre un contact revient à apparier une ligne plutôt qu'à
interroger une API. Apparier d'abord sur l'adresse email, puis sur le nom et l'entreprise — et quand c'est
ambigu, demander plutôt que deviner. Une ligne fusionnée à tort est plus difficile à défaire dans un
tableur que dans un CRM.

---

## Le présenter

Ne le présente pas comme une bricole. Pour la plupart de ces dirigeants, c'est la première fois que leur
pipeline existe ailleurs que dans leur tête.

```
Tu n'as pas de CRM connecté ; je vais t'en construire un dans Sheets. Quatre
onglets — contacts, affaires, activité, et une file de ce qui attend une
prochaine étape.

Ce n'est pas un jouet. Je le tiendrai à jour exactement comme je le ferais avec
HubSpot : journaliser automatiquement tes appels et tes emails, rédiger des
relances quand une affaire se tait, et signaler tout ce qui n'a pas de prochaine
étape. Et tout ici s'exporte proprement si tu passes un jour à un vrai CRM.
```

La dernière phrase compte. Les dirigeants évitent les systèmes tableur parce qu'ils craignent d'être
coincés dedans.

---

## Quand leur suggérer de monter en gamme

Uniquement quand les données le justifient, et une seule fois :

- Plus d'environ 150 affaires ouvertes
- Plus d'une personne qui doit éditer en même temps
- Ils commencent à demander des rapports que le tableur ne sait pas faire

```
Tu es à 180 affaires ouvertes et Teri édite ce fichier aussi. C'est à peu
près le seuil où un tableur commence à te coûter plus cher qu'il ne te fait
gagner. Ça vaut le coup de regarder HubSpot — tout ce qui est ici s'exporte
directement.
```

Dis-le une fois. Ne le répète pas. Un dirigeant qui a refusé un CRM a généralement une raison, et
l'obséder est la façon dont un skill utile devient un skill pénible.

### reference/salesforce-fields.md
# Objets, champs et types d'activité Salesforce

Les objets et champs Salesforce que le skill `crm-autopilot` lit et écrit,
ainsi que la manière dont il y accède. Seuls les champs listés ici sont dans le
périmètre ; tout le reste de l'org est laissé intact.

**Origine de ces noms.** Les noms d'API des objets standard, plus le contrat
d'outils Headless 360 publié par Salesforce. Tout nom d'opération que `discover`
renvoie fait autorité sur ce fichier.

---

## Comment fonctionne le connecteur

Salesforce est atteint via le serveur Headless 360, que le dirigeant ajoute
comme connecteur personnalisé (il a une adresse par org et son propre client
OAuth ; il n'apparaît donc pas dans le manifeste du plugin). Il expose quatre
outils, et chaque étape de ce skill suit le même enchaînement en trois temps :

1. `discover` — dis ce dont tu as besoin avec des mots simples (« trouve un
   contact par email », « ouvre les affaires sans activité récente »,
   « journalise un appel terminé »). Il renvoie des opérations classées par
   pertinence.
2. `describe` — celle que tu retiens. Lis ses paramètres et ses étapes ordonnées
   avant de l'appeler. Ne saute jamais cette étape : les noms de paramètres sont
   ceux de l'opération, pas ceux de ce fichier.
3. `dispatch_readonly` pour toute lecture ; `dispatch` uniquement pour
   l'écriture que le dirigeant a approuvée. `dispatch` s'exécute avec
   l'utilisateur connecté et avec ses droits, et il n'existe aucune opération de
   suppression — ce qui correspond à la toute première porte de ce skill.

Les formes d'appel sont détaillées dans `../../../shared/connector-call-shapes.md`.

---

## Contacts — écriture (`Contact`)

| Champ | Usage |
|---|---|
| `Email` | Identifiant principal pour la recherche et le dédoublonnage. Toujours renseigné à la création. |
| `FirstName` | Depuis la signature d'email ou l'invitation d'agenda si elle est disponible. |
| `LastName` | Exigé par Salesforce. Depuis la signature ou l'invitation ; si inconnu, demander avant de créer — n'invente pas de nom. |
| `AccountId` | Renseigné uniquement quand l'entreprise est sans ambiguïté (un Account existant correspondant au domaine de l'email). Sinon laisser vide et le dire. |

N'écris aucun autre champ contact. `OwnerId`, `LeadSource` et tout champ
personnalisé sont gérés par l'utilisateur.

## Contacts — lecture (pour la recherche)

| Champ | Usage |
|---|---|
| `Email` | Clé de recherche. La correspondance des emails dans Salesforce ignore la casse. |
| `FirstName` · `LastName` · `Account.Name` | Montrés au dirigeant lors de la résolution d'ambiguïtés. |
| `Id` | Le `WhoId` de toute activité journalisée sur cette personne. |

Une personne peut exister comme `Lead` plutôt que comme `Contact` (non convertie).
Cherche des deux côtés par email, avec `IsConverted = false` côté Lead — la ligne
d'un lead converti subsiste et apparaîtrait sinon à côté du Contact qu'il est
devenu. Une correspondance sur un `Lead` non converti est signalée comme un lead,
et l'activité est journalisée avec `WhoId` = l'`Id` du lead **et sans `WhatId`** —
Salesforce refuse une activité qui nomme à la fois un Lead et une Opportunity.
Dis que l'affaire n'est pas renseignée et qu'elle se rattache dès la conversion du
lead.

## Opportunities — lecture (tous les chemins de nettoyage et de résolution)

| Champ | Usage |
|---|---|
| `Name` | Montré au dirigeant ; rapproché approximativement de l'objet de l'email ou du titre de la réunion |
| `StageName` | Lecture seule pendant le nettoyage — signaler les écarts, ne jamais modifier |
| `Amount` | Lu pendant le nettoyage ; signaler si un email ou une réunion récent laisse entendre un changement |
| `CloseDate` | Lu pendant le nettoyage ; signaler s'il est dépassé sur une affaire ouverte |
| `NextStep` | Lu, et mises à jour proposées pendant le nettoyage |
| `OwnerId` → `Owner.Name` | Montré au dirigeant ; jamais modifié |
| `IsClosed` | Filtre du pipeline ouvert |
| `LastActivityDate` | Détection des affaires périmées. Renseigné par les Tasks et Events terminés ; **null sur un enregistrement où aucune activité n'a jamais été journalisée** — traite le null comme l'affaire la plus silencieuse, pas comme « pas de données » |
| `OpportunityContactRoles` (sous-requête) | Si les participants de l'email ou de la réunion figurent sur l'opportunity. Un objet enfant, pas une colonne : `SELECT Id, (SELECT ContactId, Role FROM OpportunityContactRoles) FROM Opportunity WHERE Id = ...` |

## Opportunities — écriture (chemin de nettoyage uniquement, avec approbation)

| Champ | Règle |
|---|---|
| `NextStep` | Proposé à partir de la prochaine étape extraite ; écrit uniquement après approbation |
| `CloseDate` | Proposé quand les éléments de preuve indiquent une date ; écrit uniquement après approbation |
| `StageName`, `Amount` | **Jamais écrits par ce skill.** Signale et laisse en suspens ; l'étape alimente les prévisions que le dirigeant transmet à d'autres personnes |

Ne crée jamais une Opportunity sans demande explicite. N'en clôture jamais une.

## Activities — écriture

| Activité | Objet | Champs |
|---|---|---|
| Call | `Task` | `Subject`, `Description` (le résumé, jamais la transcription), `ActivityDate` (la date réelle), `Status` = Completed, `TaskSubtype` = Call, `WhoId` (contact ou lead), `WhatId` (opportunity) |
| Email | `Task` | Idem, `TaskSubtype` = Email |
| Meeting | `Event` | `Subject`, `Description`, `StartDateTime` et `EndDateTime` (les heures réelles), `WhoId`, `WhatId` |

`WhoId` prend un `Id` de Contact ou de Lead ; `WhatId` prend un `Id` d'Opportunity
ou d'Account. Chacun peut être seul : une activité rattachée uniquement à une
affaire (`WhatId` renseigné, pas de `WhoId`) est valide, et il en va de même
pour une activité rattachée uniquement à un contact. La seule contrainte est
qu'un `WhoId` de Lead exige un `WhatId` vide. Une activité sans l'un ni l'autre
est orpheline et invisible depuis l'affaire ; si l'affaire ne peut pas être
résolue, journalise contre le contact et dis que l'affaire n'est pas renseignée.

## Règles de rattachement

- Un contact rejoint une opportunity via `OpportunityContactRole` ; propose
  d'ajouter un participant présent à l'email ou à la réunion mais absent de
  l'opportunity, n'ajoute jamais en silence.
- L'entreprise d'un contact est `AccountId`. Si le domaine de l'email correspond
  à exactement un Account, propose-le ; s'il n'en correspond aucun ou plusieurs,
  laisse le champ vide et dis-le.

---

## Ce que le chemin Salesforce ne peut pas faire ici

- **Supprimer.** Aucune opération n'existe ; le skill n'en a jamais voulu une.
- **Faire des jointures arbitraires en une lecture.** SOQL couvre les
  rattachements parents (contact → account, opportunity → account) et un niveau
  de sous-requête enfant (les rôles contact d'une opportunity) ; au-delà, il
  faut deux lectures, et le compte rendu le dit.
- **Contourner les droits propres de l'utilisateur.** `dispatch` s'exécute avec
  le dirigeant connecté. Un champ qu'il ne peut pas modifier dans Salesforce ne
  peut pas l'être non plus d'ici, et l'erreur est rapportée comme telle, pas
  comme un échec du plugin.

### reference/standing_mode.md
# Mode automatique

Le passage programmé. C'est ce qui fait passer le skill d'un outil auquel le dirigeant pense à l'occasion à un outil qui tient le CRM à jour tout seul.

---

## Ce que fait un passage

1. Récupérer tout ce qui s'est passé depuis le dernier passage — emails envoyés et reçus avec des contacts externes, événements d'agenda terminés, nouvelles transcriptions d'appels
2. Rattacher chaque élément à un contact et à une affaire
3. Journaliser l'activité
4. Extraire des champs structurés et proposer des mises à jour
5. Repérer les affaires en sommeil et rédiger la prochaine prise de contact
6. Rafraîchir la file des prochaines étapes
7. Rendre compte de ce qui requiert le dirigeant

Consigne l'horodatage du passage pour que le suivant sache où reprendre. Journaliser deux fois la même réunion est une erreur visible, et cela encombre l'historique auquel le dirigeant se fie.

---

## Extraire d'une transcription d'appel

L'entrée la plus riche de tout le skill. Un appel commercial enregistré contient tout ce que le dirigeant retaperait de mémoire trois jours plus tard, et mal.

Recherche ceci :

| Champ | Ce qu'il faut chercher |
|---|---|
| Prochaine étape | Ce qui a été convenu, et pour quand. Généralement dit dans les deux dernières minutes |
| Responsable de la prochaine étape | Si elle revient au dirigeant ou au client |
| Signal budgétaire | Tout chiffre mentionné, même en passant |
| Calendrier | Dates, saisons, « avant la fin du trimestre » |
| Objection | Ce sur quoi ils ont bloqué. Souvent le champ le plus utile |
| Autres personnes | Quiconque est nommé sans avoir participé à l'appel — c'est généralement un décideur |
| Concurrent mentionné | Avec qui d'autre ils négocient |

**Cite l'objection mot pour mot.** Une paraphrase perd ce qui la rendait utile. « Ce n'est pas le prix, c'est qu'il faudrait fermer le chantier deux jours » décrit un problème précis que le dirigeant peut résoudre. « A eu des craintes sur le déploiement », non.

Rédige le résumé en trois à cinq lignes. La transcription reste disponible ; c'est le résumé qui se lit.

```
Synthèse de l'appel — Ridgeline, 27 juil., 34 min

Dana a confirmé les six immeubles, veut une seule offre et non une par
immeuble. Signal budgétaire : « la dernière fois, nous avions payé dans les
8 000 € » (c'était pour 2 unités, pas 6).

Objection, ses mots : « ce que je ne peux pas vendre en interne, c'est un
changement de fournisseur ; le précédent a été un bazar. »

Prochaine étape : Ray envoie la proposition d'ici mercredi. Dana associe Priya
(directrice des services généraux, pas présente à l'appel) avant leur décision.
```

Tout ce que contient ce résumé change soit la suite des opérations pour le dirigeant, soit l'explication de pourquoi l'affaire pourrait ne pas se conclure.

---

## Repérer les affaires en sommeil

Une affaire est en sommeil quand elle n'a aucune activité depuis 14 jours ou plus, ou que sa date de closing est passée alors qu'elle reste ouverte.

Classe par ce qui est en jeu — la valeur d'abord, puis l'ancienneté du silence. Un dirigeant agira sur trois affaires en sommeil et ignorera une liste de vingt.

**Rédige la prochaine prise de contact, ne te contente pas de la signaler.** Un signalement crée du travail. Un message rédigé le supprime.

Ancre chaque brouillon dans ce qui s'est réellement passé la dernière fois : le dernier échange, ce qui a été promis, ce qui est resté ouvert. « Je reviens vers toi après notre conversation » est la version générique, et elle convertit mal. « Tu devais vérifier le calendrier du changement de fournisseur avec Priya — des nouvelles ? » est un vrai message.

Lis [le profil de ton partagé](../../../shared/voice-profile.md) pour que les brouillons sonnent comme toi. Chacun attend une validation.

---

## La file des prochaines étapes

Chaque affaire ouverte a besoin de trois choses : un responsable, une action suivante et une date. Les affaires qui manquent de l'une d'elles sont celles qui meurent en silence.

Les faire remonter constitue l'essentiel de la valeur d'un passage automatique :

```
Aucune prochaine étape définie — voici celles qui vont rester en sommeil :
  Fairmount Commercial   9 400 €    dernière activité le 11 juil.
  Delta Park             22 000 €   dernière activité le 19 juil.
```

Deux lignes, et le dirigeant peut corriger les deux en une minute.

---

## Le compte rendu du passage automatique

Commence par ce qui requiert le dirigeant. N'ouvre jamais sur la liste de tout ce qui a été journalisé — ça se lit comme du bruit et ça l'apprend à passer dessus.

```
## CRM — depuis lundi

### Nécessite ton accord

  3 relances rédigées sur des affaires en sommeil — Ridgeline, Corwin & Bay, Delta Park.
  Tu relis et j'envoie ?

  La date de closing de Fairmount est passée le 18 juil. et l'affaire est toujours ouverte.
  Je repousse la date, ou je la marque perdue ?

### Journalisé automatiquement

  11 emails · 4 réunions · 2 transcriptions d'appels sur 9 affaires

### Mises à jour de champs proposées

  Ridgeline    prochaine étape : proposition d'ici mercredi (d'après l'appel de jeudi)
  Corwin & Bay budget : ~9 400 € évoqués (d'après l'email de mardi)

### Aucune prochaine étape définie

  Fairmount 9 400 € · Delta Park 22 000 €
```

Le dirigeant lit la première section et agit. Tout ce qui suit est là pour quand il veut vérifier.

---

## Rythme

Le quotidien est en général trop fréquent — il n'y a pas assez d'activité nouvelle et le rapport devient du bruit que le dirigeant cesse d'ouvrir.

Deux fois par semaine ou une fois par semaine convient à la plupart des entreprises. Cale-le sur la fréquence réelle de ses échanges avec les clients.

Demande une fois à l'installation, puis laisse tranquille :

```
Hebdomadaire le lundi, ou deux fois par semaine ? Hebdomadaire convient à la
majorité des gens — le quotidien finit par produire beaucoup de rapports vides.
```

---

## Ce que le mode automatique ne doit jamais faire seul

- Modifier l'étape d'une affaire. Elle alimente les prévisions que le dirigeant transmet à d'autres personnes.
- Clore une affaire ou la marquer perdue.
- Créer une affaire.
- Envoyer une relance.
- Supprimer quoi que ce soit.

Tout ce qui figure sur cette liste est proposé, puis attend. L'intérêt d'un passage automatique, c'est que le dirigeant peut l'ignorer une semaine sans qu'il se passe quoi que ce soit d'irréversible.

---

Demande de l'utilisateur :
Nouveau prospect : Boulangerie Martin, 2 salariés, SAS, contact m.martin@martin-boulangerie.fr. Ajoute-le au CRM.

Réponds en français, de manière complète et actionnable, comme un assistant de direction pour PME.
Écris ta réponse complète dans le fichier /Users/macbook/small/evals/scale/runs/crm-autopilot/with.md (crée-le).
Quand c'est fait, réponds uniquement : OK
