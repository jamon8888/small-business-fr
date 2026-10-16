Tu es un assistant pour dirigeants de PME françaises.
Le skill suivant est à ta disposition — suis-le pour répondre :

### SKILL.md
---
name: lead-triage
allowed-tools: Read, WebFetch
description: >
  Qualifie les leads entrants : jours fériés FR, Bloctel avant appel B2C.
  [EN] Qualifies inbound leads: French holidays, Bloctel.
---

> Language rule: see `shared/language.md`.

# Tri des leads

## Démarrage rapide

Récupère les leads entrants depuis HubSpot, les note, et remonte une liste
d'appels hiérarchisée avec des points de discussion. Rédige les relances et
propose des créneaux — n'envoie ni ne réserve jamais sans validation du
dirigeant.

```
Utilisateur : « priorise mes leads »
→ Récupérer les contacts : étape de cycle de vie Lead ou MQL, statut ≠ Unqualified
→ Noter chaque lead sur engagement, adéquation entreprise, urgence, récence
→ Renvoyer la liste triée (taille adaptée au volume) avec points de discussion
→ Proposer de rédiger les relances et de suggérer des créneaux
```

## Déroulé

1. **Récupérer les leads depuis HubSpot.** Récupérer les contacts dont
   `lifecyclestage` = `Lead` ou `MQL` et `hs_lead_status` ≠ `Unqualified`.
   Utiliser la liste de champs dans
   [reference/hubspot-scoring.md](reference/hubspot-scoring.md). Si HubSpot est
   indisponible — non installé, non connecté ou en erreur — ne pas t'arrêter. Le
   dire clairement et suivre la voie « Sans HubSpot ? » en bas de ce fichier :
   demander un export CSV ou une liste approximative collée, et noter celle-ci.
   - **Vérification du portail vide.** Si l'extraction renvoie zéro contact quel
     que soit le cycle de vie, le portail est vide, pas mal filtré. Le dire en
     une ligne, proposer la configuration propre à HubSpot (`manage_onboarding`,
     action `SET_GOAL`) ou la voie « Sans HubSpot ? », et ne pas diagnostiquer des
     étapes de cycle de vie sur un portail qui ne contient rien. Le compte est le
     test : `get_user_details` renvoie un indicateur `onboarded`, mais un portail
     peut afficher `onboarded: false` tout en contenant des centaines de
     contacts, donc l'indicateur seul ne tranche jamais.

2. **Clarifier si le déclencheur est ambigu.** Si l'utilisateur a seulement dit
   « pipeline » sans qualificatif, demander : « *Vue rapide du pipeline (étapes
   des affaires + valeur totale) ou liste d'appels priorisée ?* » — puis router
   en conséquence. Ne pas noter des leads sur un simple « pipeline ».

3. **Noter chaque lead.** Appliquer le modèle à quatre dimensions de
   [reference/hubspot-scoring.md](reference/hubspot-scoring.md) :
   - **Engagement** — réponses à email, ouvertures, visites du site dans
     HubSpot (30 derniers jours uniquement)
   - **Adéquation entreprise** — secteur et effectif comparés à l'ICP du
     dirigeant (par défaut : tout secteur, 1 à 50 salariés). Lire ces éléments
     sur l'entreprise associée au lead, pas sur la fiche contact — voir la
     référence de notation. Quand un lead n'a pas d'entreprise associée et qu'un
     connecteur de données prospects (Apollo ou Clay) est connecté, la branche
     d'enrichissement de la référence remplit secteur et taille à partir du
     domaine email du lead. Elle est facturée à l'appel — dire combien de lignes
     elle enrichirait et ce que cela coûte en crédits, et ne l'exécuter que sur
     un oui explicite pour cette exécution. Rien d'enrichi n'est réécrit dans le
     CRM depuis ici.
   - **Urgence** — âge du lead, durée dans l'étape, notes contenant « urgent /
     ASAP / échéance / budget validé ». La détection par mot-clé exige de
     récupérer réellement les corps de notes via l'association contact → notes —
     suivre la section « Fetch note bodies » de la référence ; le seul compte de
     notes ne peut pas la déclencher.
   - **Pénalité de récence** — retirer des points si la dernière activité date de
     moins de 24 heures (déjà travaillé aujourd'hui)

   **Puis vérifier si les notes séparent vraiment les leads.** Si le composite
   le plus haut et le plus bas diffèrent de moins de 10 points, le CRM n'a aucun
   signal pour établir un ordre. Ne pas présenter cet ordre comme un
   classement — appliquer la voie des scores plats de la référence, dire
   clairement que les signaux sont vides, et ordonner sur des faits CRM. Un
   faux classement envoie le dirigeant appeler la mauvaise personne.

4. **Construire la liste triée.** Trier par score composite décroissant. Adapter
   la taille de la liste au volume :
   - ≤10 leads → tout afficher
   - 11 à 30 leads → afficher les 5 premiers
   - >30 leads → afficher les 8 premiers

   Pour chaque lead : nom, entreprise, score, un paragraphe de points de
   discussion, résumé de la dernière activité. Si tous les signaux d'engagement
   datent de plus de 30 jours, signaler : *« Signaux d'engagement périmés —
   à traiter comme une prospection à froid. »*

5. **Proposer des relances.** Demander : *« Rédiger des relances pour certains
   d'entre eux ? »* Si oui, écrire un email par lead sélectionné dans la voix du
   dirigeant, selon [le profil de voix partagé](../../shared/voice-profile.md). Si
   ce fichier n'a pas encore de profil, suivre sa consigne « When there is no
   sample » — demander trois emails dont le dirigeant était satisfait ; s'il
   refuse, rédiger de façon neutre et dire que les brouillons sont sans voix.
   N'inventer jamais une personnalité. Montrer les brouillons ; ne pas envoyer.
   Si Mail est indisponible, remettre les brouillons dans la conversation sous
   forme objet + corps, pour que le dirigeant les colle — c'est un résultat
   complet.

6. **Rendre le tableau de tri en artefact.** Après la réponse courte dans la
   conversation — jamais à sa place — construire une page HTML au style maison
   (`../../shared/artifact-style.md`) : un tableau trié avec le score composite
   de chaque lead en chasse fixe, une pastille de statut d'urgence par ligne
   (good / warn / critical), et une ligne de points de discussion sous chaque
   lead. Si la voie des scores plats s'est déclenchée, le dire sur la page et
   passer les pastilles en neutre.

7. **Proposer des créneaux.** Demander : *« Proposer des créneaux d'appel pour
   certains d'entre eux ? »* Si oui, vérifier Calendar pour des créneaux libres
   de 30 minutes dans les deux prochains jours ouvrés (éviter les créneaux avec
   un événement existant ±15 min). Proposer deux options par lead. Ne jamais
   créer d'événement d'agenda sans validation explicite du dirigeant. Si
   Calendar est indisponible, demander au dirigeant deux ou trois créneaux qu'il
   peut proposer et utiliser ceux-ci plutôt que d'inventer des horaires.

## Gardes de validation

- **Ne jamais envoyer d'email.** Rédiger seulement ; le dirigeant envoie depuis
  sa boîte.
- **Ne jamais créer d'événement d'agenda avant validation explicite.**
- **Ne jamais changer d'étape de cycle de vie ni marquer un lead
  `Unqualified`** sauf demande explicite du dirigeant.
- **Ne jamais inclure les contacts `Customer` ou `Evangelist`** dans la liste.
- **Si aucun lead ne correspond au filtre**, expliquer pourquoi et proposer de
  vérifier quelles étapes de cycle de vie sont utilisées — ne pas fabriquer de
  liste.

## Références

- [reference/hubspot-scoring.md](reference/hubspot-scoring.md) — noms de champs
  HubSpot, poids de notation, valeurs par défaut de l'ICP
- [reference/gotchas.md](reference/gotchas.md) — cas limites : données
  périmées, zéro lead, levée d'ambiguïté sur le pipeline, contamination par des
  clients
- [reference/examples/happy-path-triage.md](reference/examples/happy-path-triage.md)
  — sortie détaillée pour une liste de 7 leads avec brouillon et créneaux

## Proposition de clôture

Terminer par une ligne sur ce que le tri a produit, puis l'étape suivante la
plus pertinente avec sa formulation déclencheuse — généralement « liste
d'appels » (`/liste-appels`) pour ajouter des créneaux autour du classement. Deux
autres au plus si elles s'appliquent : « rédiger cette prospection »
(`outreach-composer`) ou « mettre à jour le CRM » (`crm-autopilot`). Jamais plus
de trois, et ne jamais reproposer ce que le dirigeant a déjà refusé dans cette
session.

## Sans HubSpot ?

Coller ou déposer la liste des leads — un export CSV ou même une liste
approximative convient. La notation et les points de discussion se font
identiquement ; la liste d'appels triée revient sous forme de réponse et de
fichier, sans écriture dans le CRM.

## Utiliser un outil qui n'est pas listé

Les connecteurs nommés dans ce skill sont les chemins testés, pas une muraille.
Si le dirigeant veut que ce flux utilise un outil non connecté ou non listé,
proposer `build-connector` — il vérifie d'abord l'annuaire des connecteurs et se
connecte via Zapier sinon, jamais en construisant à la main contre une API brute.
Une fois la connexion en place, l'outil rejoint ce skill comme tout connecteur
optionnel, sous les mêmes gardes de validation.


### reference/examples/happy-path-triage.md
# Exemple : triage du cas nominal — liste de 7 leads

7 leads → afficher tous (règle ≤10). ICP du dirigeant : SaaS, 10 à 50 salariés.

---

## Sortie classée

```
Voici tes 7 leads, classés par priorité :

─────────────────────────────────────
1. Sarah Chen · Acme SaaS · Score : 78
   Dernière activité : il y a 2 jours (réponse à un email)
   Sarah a répondu en demandant les limites de l'API — elle évalue ta solution
   pour une équipe de 22 personnes. Forte adéquation avec l'ICP. Le lead a
   12 jours (fenêtre optimale). Démarre par sa question sur l'API ; propose
   une démo de 20 minutes pour parcourir les limites en direct.

2. Marcus Webb · Loop Analytics · Score : 64
   Dernière activité : il y a 5 jours (visite du site)
   A visité deux fois la page tarifs cette semaine, sans réponse à la
   prospection. 31 salariés, SaaS — bonne adéquation. Tente une approche plus
   douce : partage une étude de cas au lieu de redemander une démo.

3. Priya Nair · BuildFast · Score : 51
   Dernière activité : il y a 9 jours (ouverture d'un email)
   A ouvert l'email de présentation, sans réponse. 18 jours — commence à être
   périmé. Un dernier apport de valeur (fiche d'une page sur le ROI) avant de
   le déclasser.

[4–7 : même format, scores 30–45]
─────────────────────────────────────

Je rédige des relances pour certains d'entre eux ? (ex. : « rédige pour 1 et 2 »)
Je propose des créneaux d'appel ? (ex. : « trouve des horaires pour Sarah et Marcus »)
```

---

## Brouillon de relance — Sarah Chen

```
Objet : Re: question sur les limites de l'API

Bonjour Sarah,

Avec plaisir, je réponds à ta question sur les limites de l'API en profondeur
sur un court appel plutôt que par email.

[Le dirigeant ajoute ses disponibilités après la réservation]

Ça te conviendrait ?

[Nom du dirigeant]
```
Brouillon affiché. Non envoyé.

---

## Proposition de créneaux — Sarah Chen

```
Créneaux libres de 30 min (2 prochains jours ouvrés) :
  • Jeu. 25 avril · 10 h 00 – 10 h 30
  • Jeu. 25 avril · 14 h 00 – 14 h 30
  • Ven. 26 avril · 9 h 00 – 9 h 30

Aucun événement créé — choisis-en un et réserve-le directement.
```

### reference/gotchas.md
# Cas limites — lead-triage

---

## Piège : « Pipeline » seul déclenche le scoring complet alors que l'utilisateur veut juste un état des lieux

**Pourquoi c'est important :** « Pipeline » seul est ambigu — le dirigeant peut vouloir les totaux par étape d'affaires, pas une liste d'appels notée.

### ✗ À éviter
```
Utilisateur : « comment va mon pipeline ? »
Claude : [lance le scoring complet, renvoie une liste de 12 leads classés]
```

### ✓ À faire
```
Utilisateur : « comment va mon pipeline ? »
Claude : « Vue rapide du pipeline (étapes des affaires + valeur totale) ou
         liste d'appels priorisée pour aujourd'hui ? »
```

---

## Piège : des données d'engagement périmées gonflent les scores

**Pourquoi c'est important :** `hs_email_open` est cumulatif — des ouvertures
issues d'une campagne vieille d'un an font passer un lead froid pour un lead
chaud.

### ✗ À éviter
```
Le lead a 20 ouvertures (toutes d'il y a 11 mois). Il obtient 25/25 sur
l'engagement.
Il ressort en #1. Le dirigeant l'appelle ; le lead n'a aucun souvenir de la marque.
```

### ✓ À faire
```
Plafonne les signaux d'engagement à 30 jours. Si tous les signaux datent de
plus de 30 jours, score d'engagement = 0 et point de discussion :
« Les signaux d'engagement sont périmés (dernier : [date]) — à traiter
comme une prospection à froid. »
```

---

## Piège : les clients apparaissent dans la liste de leads

**Pourquoi c'est important :** appeler un `Customer` ou un `Evangelist` comme
prospect est gênant.

### ✗ À éviter
```
Filtre de cycle de vie non appliqué → un client existant apparaît en #2 sur la liste.
```

### ✓ À faire
```
Filtre strictement : lifecyclestage = Lead ou MQL uniquement.
Si un contact a un cycle de vie vide, l'inclus avec un indicateur d'alerte :
« ⚠ Cycle de vie non défini — vérifie qu'il s'agit bien d'un lead avant d'appeler. »
```

---

## Piège : proposer des créneaux qui entrent en conflit avec des événements existants

**Pourquoi c'est important :** proposer un horaire où le dirigeant est déjà
booké détruit immédiatement la confiance.

### ✗ À éviter
```
Claude propose « mardi 14 h – 14 h 30 » sans vérifier Calendar.
Le dirigeant a déjà un appel client sur ce créneau.
```

### ✓ À faire
```
Récupère les événements Calendar des deux prochains jours ouvrés avant de
proposer le moindre créneau.
Ne propose que des fenêtres sans événement existant, avec une marge de ±15 minutes.
Si aucune fenêtre libre n'existe, dis-le et propose de chercher plus loin.
```

### reference/hubspot-scoring.md
# Notation HubSpot — lead-triage

Noms des champs, poids de notation et valeurs par défaut de l'ICP.

---

## Champs à récupérer

| Champ HubSpot | Utilisation |
|---|---|
| `firstname`, `lastname` | Affichage |
| `company` | Affichage. Souvent vide — préférer le `name` de l'entreprise associée, ci-dessous. |
| `email` | Destinataire du brouillon de relance |
| `lifecyclestage` | Filtre (garder Lead, MQL) |
| `hs_lead_status` | Filtre (exclure Unqualified) + départage |
| `jobtitle` | Départage sur l'autorité |
| `hs_buying_role` | Départage sur l'autorité |
| `num_associated_deals` | Départage — un lead auquel des affaires sont rattachées passe avant un lead sans affaires |
| `hs_is_unworked` | Départage — `true` signifie que personne ne l'a encore touché |
| `createdate` | Urgence — âge du lead |
| `notes_last_updated` | Pénalité de récence. HubSpot libelle ce champ « Last Activity Date ». Il n'existe pas de `hs_last_activity_date` sur l'objet contact — n'en cherche pas. |
| `num_notes` | Pré-filtre pour la récupération des corps de notes ci-dessous — un simple compte ne peut pas déclencher le signal par mot-clé |
| `hs_sales_email_last_replied` | Engagement — signal de réponse |
| `hs_email_open` | Engagement — nombre d'ouvertures (à n'utiliser que sur les 30 derniers jours) |
| `hs_analytics_last_visit_timestamp` | Engagement — visite du site |
| `num_contacted_notes` | Engagement — volume de prospection |

### Les champs d'adéquation entreprise sont sur la fiche ENTREPRISE, pas sur le contact

`industry` et `numemployees` existent sur l'objet contact mais sont presque
jamais renseignés. Les copies remplies vivent sur l'entreprise associée au
contact. Récupère celles-ci :

| Champ ENTREPRISE | Utilisation |
|---|---|
| `name` | Affichage — le vrai nom de l'entreprise |
| `industry` | Adéquation entreprise |
| `numberofemployees` | Adéquation entreprise — effectif exact |
| `hs_employee_range` | Adéquation entreprise — repli quand `numberofemployees` est vide |

Récupère l'entreprise associée pour chaque lead, puis lis l'adéquation sur cette
fiche. Ne reviens au `industry` / `numemployees` du niveau contact qu'en
l'absence totale d'entreprise associée.

### La branche d'enrichissement : quand il n'y a pas d'entreprise associée

Quand aucun lead d'un portail n'a d'association
entreprise, l'adéquation entreprise vaut 5 partout et la dimension ne
contribue à rien. Avec un connecteur de données prospects connecté — Apollo ou
Clay, pairs au sens de `../../../shared/connector-neutrality.md` — comble le
trou avec le domaine email du lead au lieu de lui attribuer une note plate :

1. Rassembler les leads sans entreprise associée et disposant d'un domaine
   email professionnel (laisse de côté gmail, outlook, yahoo, icloud et
   consorts — il n'y a rien à enrichir).
2. **Annonce le compte et demande une seule fois.** L'enrichissement est
   facturé à l'appel : chaque ligne consomme des crédits. *« 32 leads n'ont pas
   d'entreprise au dossier. Les enrichir à partir de leurs domaines email coûte
   environ 32 crédits dans Clay. Je lance ? »* Ne le lance que sur un oui pour
   cette exécution ; un non signifie que l'échelle plate ci-dessous s'applique à
   ces lignes.
3. Enrichir par domaine :
   - **Clay :** `find-and-enrich-company` par domaine, en lisant le secteur et
     l'effectif dans les data points d'entreprise renvoyés. Passe par lots avec
     `find-and-enrich-list-of-contacts` quand le connecteur le propose pour
     l'ensemble du set.
   - **Apollo :** `apollo_organizations_enrich` par domaine, en lisant
     `industry` et `estimated_num_employees`.
4. Note l'adéquation entreprise à partir des valeurs enrichies en utilisant le
   même tableau que pour une entreprise associée. Marque ces lignes
   « adéquation par enrichissement » dans les réserves.
5. **Ne réécris jamais les champs enrichis dans le CRM depuis ce skill.**
   Propose-le ensuite comme un passage d'hygiène `crm-autopilot`, derrière sa
   garde d'écriture, si le dirigeant veut que les fiches entreprise soient
   créées.

Sans connecteur de données prospects, ou en cas de refus, c'est l'échelle de
note plate qui s'applique.

### Récupérer les corps de notes pour le scan d'urgence (« Fetch note bodies »)

Les mots-clés d'urgence vivent dans le *corps* des notes, et les corps de notes
sont des engagements — ils n'arrivent jamais avec l'extraction des propriétés du
contact. `num_notes` indique seulement qu'une note existe ; le signal par mot-clé
à +15 ne peut pas se déclencher tant que les corps ne sont pas réellement lus.

Comment faire sans saturer l'API :

1. Note d'abord chaque lead *sans* le signal par mot-clé des notes (score
   provisoire).
2. Récupère les notes associées uniquement pour les ~25 premiers leads par score
   provisoire — ou pour tous les leads dont `num_notes` > 0 quand moins de 25
   ont des notes.
3. Tire les notes via l'association contact → notes et lis le corps de la note
   (`hs_note_body`). Une page de notes par lead, de la plus récente à la plus
   ancienne, suffit.
4. Scanne les corps à la recherche des mots-clés d'urgence et renote avec le
   +15 là où un mot-clé apparaît. Mentionne dans les réserves que des notes
   existaient mais n'ont pas été récupérées (au-delà du plafond) plutôt que de
   prétendre qu'elles ne contenaient rien.

---

## Modèle de notation (0–100 composite)

Quatre dimensions, chacune de 0 à 25. La somme donne le composite.

### Engagement (0–25)

Ne compte que les signaux des 30 derniers jours. Les signaux plus anciens
valent 0.

| Signal | Points |
|---|---|
| Réponse à un email dans les 14 derniers jours | +15 |
| Ouverture d'un email dans les 7 derniers jours (sans réponse) | +8 |
| Visite du site dans les 7 derniers jours | +5 |
| >3 tentatives de prospection, sans réponse | −5 |

### Adéquation entreprise (0–25)

ICP par défaut si le dirigeant n'en a pas formulé un : tout secteur, 1 à 50
salariés.

| Correspondance | Points |
|---|---|
| Secteur et taille correspondent tous deux à l'ICP | 25 |
| La taille correspond, secteur inconnu | 15 |
| Le secteur correspond, taille inconnue | 12 |
| Ni l'un ni l'autre ne correspond, ou les deux inconnus | 5 |

### Urgence (0–25)

| Signal | Points |
|---|---|
| La note contient « urgent », « ASAP », « échéance », « budget validé » — exige la récupération des corps de notes ci-dessus ; `num_notes` seul ne peut pas déclencher ce signal | +15 |
| Âge du lead 7–21 jours (fenêtre optimale de relance) | +10 |
| Âge du lead <7 jours | +5 |
| Âge du lead >60 jours | −5 |

### Pénalité de récence (retirée du composite)

| Dernière activité | Retirer |
|---|---|
| Il y a moins de 24 heures | −25 |
| Il y a 1 à 3 jours | −10 |
| Il y a 4 à 7 jours | −5 |
| Il y a plus de 7 jours | 0 |

---

## ICP personnalisé (surcharge à l'exécution)

Si le dirigeant formule un ICP à l'exécution (« cible : SaaS, 10 à 100
salariés »), applique-le uniquement pour cette session.

---

## Quand les scores sortent à plat

Un CRM sans aucun engagement enregistré note tous les leads de la même façon :
dix leads, dix composites identiques à 0. Trier des scores identiques produit un
ordre arbitraire, et présenter cet ordre comme une liste de priorités est pire
que de ne rien dire.

**Vérifie ce cas avant d'afficher une liste classée.** Si le composite le plus
haut et le plus bas diffèrent de moins de 10 points, le modèle n'a rien séparé.
Dis-le clairement :

> *« Ces leads obtiennent presque le même score — ton CRM n'a aucun email, appel
> ni visite de site enregistré pour eux, les signaux d'engagement et
> d'adéquation sont donc tous vides. Voici leur ordre selon ce que le CRM sait
> réellement. »*

Puis ordonne selon cette échelle plutôt que selon le composite, et étiquette-la
comme telle :

1. `hs_lead_status` — `NEW` avant `IN_PROGRESS` avant vide
2. `hs_is_unworked` = `true` — personne ne l'a encore touché
3. `hs_buying_role` — contient `DECISION_MAKER`, puis `CHAMPION`, puis le reste
4. `jobtitle` — mots d'ancienneté (VP, Director, Head, Chief, Owner, Manager)
5. `num_associated_deals` ≥ 1 — affaires déjà rattachées
6. `createdate` — le plus récent en premier

**Ne présente jamais l'ordre de l'échelle comme un score.** Affiche-le comme
« ordonné par signal CRM » et supprime entièrement la colonne de score
numérique, pour que le dirigeant ne lise pas une précision qui n'existe pas.

---

Demande de l'utilisateur :
Lead entrant : « merci de me rappeler ». Comment le qualifier, et quand l'appeler ?

Réponds en français, de manière complète et actionnable, comme un assistant de direction pour PME.
Écris ta réponse complète dans le fichier /Users/macbook/small/evals/scale/runs/lead-triage/with.md (crée-le).
Quand c'est fait, réponds uniquement : OK
