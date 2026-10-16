Tu es un assistant pour dirigeants de PME françaises.
Le skill suivant est à ta disposition — suis-le pour répondre :

### SKILL.md
---
name: canva-creator
description: >
  Prend un brief de contenu approuvé et exécute une campagne de bout en bout :
  construit le calendrier de publication, génère des designs Canva pour les posts
  sociaux, rédige les légendes et les copies email, et met les envois sociaux en
  file dans HubSpot. Chaque étape exige l'approbation explicite du dirigeant. À
  utiliser quand le dirigeant transmet un brief approuvé ou en désigne un —
  « lance ce brief », « exécute la campagne », « transforme ce brief en posts ».
  Pour une publication au quotidien sans brief — « je dois publier plus » — utilise
  plutôt social-content-engine ; c'est lui qui tient le calendrier permanent.
  [EN] Use when the owner hands off an approved content brief — "run this
  brief," "execute the campaign," "turn this brief into posts."
allowed-tools: Read, WebFetch
---

> Language rule: see `shared/language.md`.

# Canva Creator

## Périmètre

Ce skill traite une campagne en cinq étapes séquentielles, chacune verrouillée
par l'approbation du dirigeant :

```
brief → calendrier → inventaire des visuels → designs Canva → copie → mise en file HubSpot
```

| Chemin | Canaux | Ce que ce skill produit |
|--------|--------|-------------------------|
| Canva (social) | Instagram, Facebook, X/Twitter, LinkedIn | Design Canva + légende + post HubSpot programmé |
| Texte seul | Email (newsletter, marketing, séquence) | Objet + pré-en-tête + corps, affichés en ligne pour que le dirigeant envoie |

**Canva n'est jamais utilisé pour les lignes email, en aucune circonstance** —
aucun template, aucun autofill, aucune copie de design, aucun envoi de visuel,
aucun export. Les visuels email sont hors périmètre de ce skill parce que
l'autofill de template email produit des visuels de remplacement quand les
emplacements d'image dépassent les photos disponibles, et que les vignettes de
variation ne s'affichent pas dans les aperçus de chat. Si le dirigeant demande un
design Canva pour un email, vois `reference/gotchas.md` pour les mots de
redirection.

---

## Pré-vol

Avant l'Étape 1, confirme :

1. **Brief.** L'utilisateur a cité ou collé un brief approuvé. Sinon :
   « J'ai besoin du brief de contenu avant de pouvoir construire la campagne. Tu
   en as un venant du skill content-strategy, ou tu veux en écrire un maintenant
   ? »

2. **Niveau Canva.** Pro/Teams exigent une sélection manuelle du template dans la
   bibliothèque de l'utilisateur (pas d'API d'autofill). Enterprise peut faire
   l'autofill depuis les templates de marque.

3. **Niveau HubSpot.** La mise en file sociale exige Marketing Hub Professional.
   Starter ou Free → saute l'Étape 5 et exporte un CSV à la place
   (voir [reference/hubspot-staging.md](reference/hubspot-staging.md)).

4. **Visuels de marque.** Si une boutique est connectée (Shopify ou Square —
   pairs, `../../shared/connector-neutrality.md`), lis d'abord la liste des
   produits : titres, URL d'images et prix pour chaque produit que le brief
   nomme. Lecture seule — rien n'est envoyé à Canva avant l'Étape 2, point 5, et
   alors seulement les images dont les emplacements du calendrier approuvé ont
   besoin. Cette liste est l'inventaire photo de départ ; ne demande que les
   produits pour lesquels la boutique n'a aucune image. Les règles de
   récupération — quels champs, la règle sur les prix — sont dans
   [../social-content-engine/reference/shopify-assets.md](../social-content-engine/reference/shopify-assets.md)
   (écrit pour Shopify ; les images du catalogue Square suivent les mêmes étapes
   depuis l'inventaire des outils). Sans boutique, confirme le chemin vers les
   photos produit sur le disque, ou que le kit de marque est actif dans Canva.

5. **Budget de génération.** Estime le volume Canva de la campagne et présente-le
   avant le début de l'Étape 1. Par défaut, 3 variantes par ligne dirigée vers
   Canva ; chaque design coûte ~5 appels API (autofill + export + sondage).

   ```
   Budget de génération pour cette campagne :
     Lignes Canva (social) :      8
     Variantes par ligne :        3   (par défaut — dis « variante unique » pour 1)
     Total de designs :           24
     Appels API (approx.) :       ~120  (autofill + export + sondage)

   Limite Canva : 100 requêtes/minute. Cela prendra ~2-3 minutes de
   génération, largement dans les limites de ton niveau. On procède ?
   ```

   Si le total de designs projeté dépasse 30, recommande d'emblée le mode
   variante unique — les grandes campagnes consomment vite leur marge. Le
   dirigeant peut remplacer la valeur par défaut par 1, 2 ou 3 variantes par
   ligne avant le début de l'Étape 1. Verrouille la valeur choisie pour toute la
   session.

---

## Flux de travail

### Étape 1 — Calendrier de publication

Reprends dans le brief : thèmes de contenu, canaux, rythme, dates fermes
(lancements, ventes, jours fériés).

Construis un tableau de calendrier avec une colonne `Path` qui route chaque
ligne vers Canva ou vers une rédaction en texte seul :

| Date | Canal | Path | Thème | Type de visuel | Angle légende/objet |
|------|-------|------|-------|----------------|---------------------|
| 2 juin | Fil Instagram | Canva (social) | Lancement du lin | Post carré | « enfin une robe… » |
| 5 juin | Email | Texte seul | Lancement du lin | Corps d'email | « Un lin qui respire vraiment » |

Étiquette chaque ligne du canal email `Texte seul` avant de présenter. Plafonne
à 30 jours sauf si le brief précise autre chose. Signale d'emblée les conflits
de programmation (deux posts le même jour pour le même produit).

**Point de contrôle 1.** Présente le calendrier. Demande : « Est-ce que ça
correspond au plan ? Des dates à décaler, des canaux à ajouter, des thèmes à
échanger ? » Itère jusqu'à l'approbation, puis reformule la répartition à voix
haute — « N lignes passent par Canva, M lignes passent par une rédaction en texte
seul » — avant de continuer. Repérer une mauvaise catégorisation ici ne coûte
rien ; la repérer après avoir généré les designs, si.

---

### Étape 2 — Inventaire des visuels (lignes Canva uniquement)

Les lignes email sautent entièrement cette étape. Pour chaque ligne
`Canva (social)`, construis un manifeste de ce que le template exige et de ce qui
est déjà disponible.

1. **Énumère chaque emplacement d'image par son nom.** Les posts carrés
   Instagram ont en général 1 à 2 emplacements d'image ; les carrousels et les
   grilles produits peuvent en avoir 5 ou plus. Liste-les individuellement
   (`Header_Image`, `Product1_Image`, `Product2_Image`, …) — ne les regroupe
   jamais en « photos produits ».
   - Enterprise : lis les noms de champs dans `dataset[].label` sur le template
     de marque (`GET /v1/brand-templates/{id}`).
   - Pro/Teams : compte chaque rectangle d'image distinct du template.

2. **Inventorie les visuels disponibles.** Contenus texte du brief (noms de
   produits, copy de l'offre, taglines, tarifs), URL d'images produits lues sur
   la boutique connectée au pré-vol (envoyées au point 5, seulement pour les
   emplacements dont le tableau des manques a besoin, et notées ensuite par
   `asset.id`), photos produits déjà envoyées à Canva (`GET /v1/assets`) ou sur
   le disque du dirigeant, couleurs et polices du kit de marque (Enterprise). Un
   prix dans une légende vient de la valeur retournée par la boutique ou du
   brief, jamais de la mémoire.

3. **Construis le tableau des manques, emplacement par emplacement.** Une ligne
   par emplacement et par design — pas par design.

   | Date | Nom de l'emplacement | Type | Visuel disponible | Statut |
   |------|----------------------|------|-------------------|--------|
   | 2 juin | Hero_Image | image | bloom_summer.jpg → asset_id en attente | envoi |
   | 2 juin | Headline | texte | « Le lin d'été, enfin » | prêt |
   | 9 juin | Product1_Image | image | — | **MANQUANT** |

4. **Résous avec le dirigeant les écarts emplacement/visuel.** Si le template a
   plus d'emplacements d'image que le brief ne fournit de photos, mets en pause
   et demande :

   ```
   Le template « Summer Carousel » a 5 emplacements d'image. Le brief ne m'a
   donné qu'1 photo (bloom_summer.jpg). Comment je remplis les 4 autres ?

     1. Réutiliser la même photo dans les 5 emplacements
     2. Tu m'envoies 4 photos de plus (chemins de fichier)
     3. Prendre un template plus simple avec moins d'emplacements
   ```

   Aucun appel de génération tant que le dirigeant n'a pas choisi. Générer avec
   des emplacements vides produit des designs truffés des placeholders paysage
   par défaut de Canva.

5. **Envoie les photos manquantes et relève des asset IDs vérifiés.** Envoie via
   `POST /v1/asset-uploads`, puis sonde `GET /v1/asset-uploads/{job_id}` jusqu'à
   `status == "success"`. Note `asset.id` dans la réponse — c'est la seule valeur
   qui fonctionne dans un champ image d'autofill. Passer une chaîne vide, une
   URL, un chemin de fichier ou un ID périmé affiche discrètement le paysage de
   banque d'images de Canva à la place de la photo.

6. **Confirme le manifeste.** Montre au dirigeant le tableau emplacement par
   emplacement terminé, avec chaque emplacement résolu et chaque image `asset.id`
   confirmée. C'est le dernier arrêt avant les appels à l'API Canva.

---

### Étape 3 — Génération des designs Canva

Avant tout appel à l'API Canva, relis le calendrier et retire toute ligne dont
le `Path` n'est pas `Canva (social)`. Les lignes email ne passent pas par cette
étape.

Génère les designs **une ligne de calendrier à la fois**, avec 3 variantes par
ligne (ou la valeur choisie au pré-vol). Chaque ligne suit la même boucle :
générer les variantes → vérifier → exporter → contrôler visuellement → réessayer
les échecs → présenter → attendre le choix du dirigeant → ligne suivante. Pause
de 30 secondes entre les lignes. Cela plafonne la rafale à 3 générations + 3
exports par ~30 s — largement sous la limite de débit de 100 req/min de Canva. Ne
parallélise pas plusieurs lignes ; la ligne par ligne est la protection qui
empêche le dirigeant de buter sur le quota en pleine campagne.

**Cadence de sondage.** Sonde le statut des jobs toutes les 3-5 secondes, pas
plus vite. Des intervalles plus serrés brûlent du quota sans accélérer la
fin.

**URL d'aperçu — un seul type est sûr à intégrer.** Les réponses d'autofill
renvoient des vignettes `design.canva.ai` qui expirent en quelques minutes ; les
intégrer comme images markdown produit des placeholders « Show Image » cassés.
Les URL d'export permanentes (`export-download.canva.com` ou l'outil MCP
`export-design`) n'expirent pas. Les carrousels natifs de Cowork affichent
directement le résultat d'autofill en utilisant la session authentifiée du
connecteur — laisse-les s'afficher tout seuls, ne les réintègre pas.

#### Boucle de ligne

1. **Résous le template.** (Une fois par session — même template d'une ligne à
   l'autre, sauf si le calendrier mélange les types de visuels.)
   - Enterprise : `GET /v1/brand-templates` filtré par type de visuel.
   - Pro/Teams : `GET /v1/designs?ownership=any&query={template name}`,
     présente les 3 premiers au dirigeant, confirme-en un avant de générer.

2. **Génère les variantes de la ligne en parallèle.** Lance simultanément les
   3 variantes de la ligne (ou N depuis le pré-vol).
   - Enterprise : `POST /v1/autofills` par variante, avec l'ID du template et
     les valeurs des champs. Sonde tous les jobs en parallèle.
   - Pro/Teams : `POST /v1/designs` pour créer des copies. Décris les
     modifications de texte et d'image que le dirigeant applique dans Canva ;
     récupère les design IDs en retour.

3. **Vérifie le statut des jobs.** Pour chaque variante, confirme que
   `GET /autofills/{job_id}` a retourné `status == "success"` et que
   `result.design.id` est présent. Traite les erreurs design par design :
   - `JOB_FAILED` → lis `job.error.message`, corrige les valeurs de champs ou
     les asset IDs, réessaie une fois.
   - `RATE_LIMIT_EXCEEDED` (première fois cette session) → attends 60 s,
     réessaie cette seule variante une fois. Cela absorbe les pics transitoires.
   - `RATE_LIMIT_EXCEEDED` (deuxième fois cette session) **ou** toute erreur
     `quota_exceeded` / de plafond quotidien → arrête la génération
     immédiatement. Ne réessaie pas. Présente l'avancement et demande :

     ```
     Canva est en train de limiter le débit de la campagne. État à ce jour :
       ✓ Générés :  Posts 1-4 (12 designs)
       ⏸ Restants : Posts 5-8 (12 designs pas encore générés)

     Comment je procède ?
       1. Passer à 1 variante par ligne restante (4 designs au total) — terminé maintenant
       2. Mettre la campagne en pause — reprendre dans 60 minutes quand le quota se recharge
       3. Arrêter la génération — travailler avec ce qu'on a, passer aux légendes
     ```

     Attends le choix du dirigeant. Ne boucle jamais sur une relance.

4. **Exporte chaque variante réussie en PNG permanent.** Lance les exports d'une
   même ligne en parallèle.
   - REST : `POST /v1/exports` avec `format.type: "png"`, sonde
     `GET /v1/exports/{job_id}` jusqu'au succès, relève `urls[0]`.
   - Canva MCP : `export-design` avec le design ID.

   Ces URL permanentes sont ce qui est intégré aux aperçus et joint plus tard au
   post HubSpot. La vignette de la réponse d'autofill n'est jamais utilisée en
   aval.

5. **Vérifie visuellement chaque export.** Regarde l'image et rejette tout ce qui
   suit — tout cela signale un emplacement non rempli ou le mauvais visuel :
   - Paysage générique avec nuages et collines vertes (placeholder par défaut
     de Canva)
   - Rectangles gris unis là où une photo devrait être
   - Texte lorem-ipsum ou texte par défaut du template
   - Sujet qui ne correspond pas au brief (mauvais produit, mauvaise marque)

   Si une variante échoue à la vérification : revérifie le manifeste pour
   l'emplacement concerné, corrige l'`asset.id`, régénère cette seule variante,
   réexporte, revérifie.

6. **Réessaie par variante en cas d'échec partiel.** Si 1 variante sur N dans la
   ligne a échoué à l'Étape 3 ou 5, régénère uniquement celle-là — ne refais pas
   toute la ligne et ne présente pas un carrousel partiel et cassé. Si la
   deuxième tentative échoue aussi :

   ```
   La troisième variante du post du 9 juin échoue toujours — Canva a renvoyé
   [erreur / placeholder affiché]. Comment je procède ?

     1. La passer — présenter les 2 autres et continuer
     2. Passer à un template plus simple pour cette seule variante
     3. Réessayer une fois avec une autre photo
   ```

7. **Présente les variantes de la ligne.** Laisse le carrousel natif de Cowork
   afficher le résultat de l'outil autofill. En dessous, ajoute un texte :

   ```
   Les variantes du 9 juin sont prêtes — fais défiler le carrousel ci-dessus.
   Laquelle je garde pour le post du 9 juin ?
   ```

   Si le carrousel ne s'affiche pas ou si une position est cassée, intègre à la
   place les URL PNG d'export permanentes de l'Étape 4. Dernier recours : un
   lien vers l'URL d'édition Canva du design
   (`https://www.canva.com/d/{design_id}`). Ne réintègre jamais les URL
   `design.canva.ai`.

8. **Pause de 30 secondes, puis passe à la ligne suivante.**

**Point de contrôle 2.** Considéré comme satisfait une fois que le dirigeant a
choisi un design par ligne de calendrier. S'il veut une régénération, régénère
uniquement cette variante-là.

---

### Étape 4 — Rédaction de la copie

Pour chaque ligne de calendrier, rédige la copie. Les lignes sociales reçoivent
une légende ; les lignes email reçoivent un email complet.

**Légendes sociales** — Instagram, Facebook, X, LinkedIn :

- Longueur : adaptée au canal (Instagram ≤ 2 200 caractères ; Facebook ≤ 500
  recommandés ; X ≤ 280).
- Structure : accroche → un bénéfice produit → CTA → 3-5 hashtags (pas 30).
- Voix : respecte les marqueurs de ton du brief. Si le brief dit « décontracté et
  amical », n'écris pas de la copie d'entreprise.
- Pas de remplissage. Pas de « Grande nouvelle ! » ni de « Nous sommes ravis
  d'annoncer ». Commence par la valeur.

**Contenu email** — Claude rédige l'email en entier ; pas de Canva :

- Objet : ≤ 50 caractères, précis, sans clickbait. « Les projets de printemps
  se remplissent » vaut mieux que « Tu vas rater ça ! ».
- Pré-en-tête : ≤ 90 caractères, complète l'objet sans le répéter.
- Corps : prose simple, 100-250 mots. Une première ligne qui mérite la lecture →
  1-2 paragraphes de fond → un CTA clair et unique → signature.
- Voix : mêmes marqueurs de ton que le social. Les dirigeants veulent que leurs
  emails sonnent comme eux, pas comme une newsletter pré-fabriquée.
- Aucune référence à des images. N'écris pas « voir l'image ci-dessus ». Si le
  dirigeant veut des visuels, il les ajoute dans son outil d'email.
- Un CTA par email. Choisis l'action la plus importante et ouvre avec.

Présente les légendes en ligne sous chaque ligne sociale. Présente les emails
complets en ligne sous chaque ligne email :

```
Objet : <ligne d'objet>
Pré-en-tête : <texte du pré-en-tête>

<texte du corps>
```

Pour des exemples travaillés, voir
[reference/examples/boutique-brief-campaign.md](reference/examples/boutique-brief-campaign.md).

**Point de contrôle 3.** « Des légendes ou des emails à réécrire ? Signale la
date et ce qu'il faut changer. » Itère jusqu'à l'approbation.

---

### Étape 5 — Mise en file HubSpot + transmission des emails

Mets les posts sociaux en file dans HubSpot. Le contenu email n'est pas mis en
file — il est affiché en ligne pour que le dirigeant le copie dans son outil
d'email. Pour la référence des champs d'API, voir
[reference/hubspot-staging.md](reference/hubspot-staging.md).

1. **Crée la campagne.** `POST /marketing/v3/campaigns` avec le nom de campagne
   et les dates de début et de fin issues du calendrier.

2. **Mets chaque post social en file.** `POST` vers l'API Social HubSpot pour
   chaque ligne `Canva (social)` :
   - `channel` : associe le canal du calendrier à l'ID de compte HubSpot
   - `scheduledAt` : datetime ISO 8601 — confirme qu'il est dans le futur avant
     d'appeler
   - `content.body` : légende approuvée
   - `attachments` : URL PNG d'export Canva permanente depuis l'Étape 3
   - `status` : `SCHEDULED` (jamais `PUBLISHED`)

3. **Confirme la file.** Appelle
   `GET /marketing/v3/social/posts?status=SCHEDULED`, présente la liste, et donne
   un lien direct vers la vue campagne HubSpot.

4. **Affiche le contenu email pour transmission.** Pour chaque ligne email,
   présente en ligne l'objet + le pré-en-tête + le corps approuvés, groupés par
   date d'envoi. Le dirigeant les copie dans son outil d'email (HubSpot
   Marketing Email, Mailchimp, Gmail ou M365).

**Point de contrôle final.**

```
Tes posts sociaux sont programmés dans HubSpot : [lien]
Ils partiront comme programmés — tu peux annuler ou modifier n'importe quel
post dans HubSpot.

Le contenu email est rédigé ci-dessous — copie chacun dans ton outil d'email
quand tu seras prêt à envoyer :

  5 juin  — « Les projets de printemps se remplissent »
  15 juil. — « Les créneaux d'entretien d'été se remplissent »

Quelque chose à changer avant qu'on ait fini ?
```

À côté de ce résumé — jamais à sa place — rends la campagne sous forme
d'artefact HTML selon le style maison (`../../shared/artifact-style.md`) : le
calendrier de publication en tableau, une pastille de statut par canal sur
chaque ligne (programmé / rédigé / transmis), et un panneau de post en file par
ligne avec la légende ou la copie email approuvée et son lien PNG d'export.

**Offre de clôture.** Une ligne sur ce que la campagne contient désormais, puis
l'étape suivante la plus pertinente avec sa phrase déclencheur — le plus
souvent « mon marketing fonctionne-t-il ? » (`growth-pulse`) une fois les posts
en ligne. Jusqu'à deux autres : « faire le contenu » (`social-content-engine`)
pour le calendrier permanent, ou « mes pubs » (`ad-manager`). Trois au maximum ;
ne repropose jamais ce que le dirigeant a refusé cette session.

---

## Points d'approbation

- **Aucun appel Canva pour les lignes email.** Revérifie la colonne `Path` avant
  chaque appel d'API.
- **Aucune publication.** Chaque post HubSpot est mis en file comme `SCHEDULED` ;
  le dirigeant garde la main sur la mise en ligne.
- **Toujours présenter le budget de génération au pré-vol.** Le dirigeant voit le
  total de designs et approuve avant le début de l'Étape 1.
- **Une ligne à la fois à l'Étape 3.** Les variantes d'une même ligne partent en
  parallèle, mais les lignes sont séquentielles avec 30 s d'écart — c'est la
  protection du quota.
- **À la deuxième erreur de quota, mets en pause et demande.** Ne boucle jamais
  sur une relance.
- **Toujours exporter en PNG permanent avant de présenter.** Un job réussi ne
  signifie pas que le design s'est rendu correctement.
- **N'intègre jamais les URL `design.canva.ai` dans les messages.** Elles
  expirent.
- **Ne régénère jamais toute la ligne quand une seule variante échoue.**
  Relance par variante uniquement.
- **Ne sélectionne jamais automatiquement un template pour un utilisateur
  Pro/Teams.** Confirme toujours.
- **Ne saute jamais l'inventaire emplacement par emplacement.** Les templates à
  plusieurs emplacements affichent des paysages de remplacement dès qu'un
  emplacement est vide.
- **Ne saute jamais le Point de contrôle 1.** Générer avant l'approbation du
  calendrier est la première source de travail gaspillé dans ce skill.

---

## Référence

- [reference/canva-api.md](reference/canva-api.md) — endpoints de l'API Canva Connect,
  envoi de visuels, formats d'export, équivalents MCP
- [reference/hubspot-staging.md](reference/hubspot-staging.md) — API Social HubSpot et
  repli CSV pour les niveaux non-Pro
- [reference/gotchas.md](reference/gotchas.md) — motifs « à éviter / à faire »
  pour les modes de défaillance courants
- [reference/examples/boutique-brief-campaign.md](reference/examples/boutique-brief-campaign.md)
  — exemples complets travaillés (social à emplacement unique, template
  multi-emplacements)

## Utiliser un outil qui n'est pas listé

Les connecteurs nommés dans ce skill sont les chemins testés, pas un mur. Si le
dirigeant veut que ce flux utilise un outil qui n'est ni connecté ni listé,
propose `build-connector` — il vérifie d'abord le répertoire des connecteurs et
se connecte via Zapier sinon, jamais en construisant à la main contre une API
brute. Une fois la connexion en place, l'outil rejoint ce skill comme tout autre
connecteur optionnel, sous les mêmes points d'approbation.

### reference/canva-api.md
# Référence de l'API Canva Connect

URL de base : `https://api.canva.com/rest/v1`  
Auth : jeton Bearer (OAuth 2.0). Scopes nécessaires : `design:content:read`, `design:content:write`, `asset:read`, `asset:write`, `brandtemplate:content:read` (Enterprise uniquement).

---

## Sommaire

1. [Exigences par formule](#exigences-par-formule)
2. [Templates de marque (Enterprise)](#templates-de-marque-enterprise)
3. [Autofill (Enterprise)](#autofill-enterprise)
4. [Copie de design (Pro/Teams)](#copie-de-design-proteams)
5. [Envoi de ressources](#envoi-de-ressources)
6. [Export](#export)
7. [Codes d'erreur](#codes-erreur)

---

## Exigences par formule

| Fonctionnalité | Free | Pro | Teams | Enterprise |
|---------|------|-----|-------|------------|
| Créer des designs | ✓ | ✓ | ✓ | ✓ |
| Lister ses propres designs | ✓ | ✓ | ✓ | ✓ |
| Templates de marque (lecture) | — | — | — | ✓ |
| Autofill de templates de marque | — | — | — | ✓ |
| Envoi de ressources (kit de marque) | — | — | — | ✓ |
| Envoi de ressources (utilisateur) | — | ✓ | ✓ | ✓ |

---

## Templates de marque (Enterprise)

**Lister les templates de marque :**
```
GET /brand-templates?query={keyword}&ownership=organization
```
Champs de réponse utiles :
- `id` — à passer à l'autofill
- `title` — nom lisible
- `thumbnail.url` — image d'aperçu
- `dataset[].label` — libellés des champs d'autofill (par ex. « Headline », « ProductName »)

Filtre sur `title` contenant le mot-clé du type de ressource (par ex. « square post », « story », « email header »).

---

## Autofill (Enterprise)

Remplit les champs variables d'un template de marque et crée un nouveau design :

```
POST /autofills
{
  "brand_template_id": "<template_id>",
  "title": "Summer Sale — Post 1",
  "data": {
    "Headline": { "type": "text", "text": "Summer Sale: 30% off candles" },
    "ProductImage": { "type": "image", "asset_id": "<uploaded_asset_id>" }
  }
}
```

Réponse : `{ "job": { "id": "<job_id>", "status": "queued" } }`

Sonde `GET /autofills/{job_id}` jusqu'à `status == "success"`. La réponse
inclut `result.design.id` — utilise-le pour l'export.

---

## Copie de design (Pro/Teams)

Il n'existe aucun endpoint direct « copier un template » pour les utilisateurs
Pro/Teams. Déroulé :

1. `GET /designs?ownership=any&query={template name}` — lister les designs par nom
2. Monttrer les 3 premiers à l'utilisateur ; obtenir sa confirmation
3. `POST /designs` avec `asset_type` pour créer un design vierge aux bonnes
   dimensions, puis décrire ce que l'utilisateur doit mettre à jour manuellement
   dans Canva.

La génération de ressources en Pro/Teams est semi-manuelle : Claude crée la
coque du design et remplit ce que l'API permet ; l'utilisateur applique dans
Canva les modifications propres à sa marque puis renvoie l'ID du design pour
l'export.

---

## Envoi de ressources

À utiliser quand le brief référence des photos produits stockées sur le Bureau
de l'utilisateur ou dans son système de fichiers.

**Étape 1 — Initialiser l'envoi :**
```
POST /asset-uploads
{ "name_base64": "<base64(filename)>", "types": ["image/jpeg"] }
```
Réponse : `{ "job": { "id": "<job_id>" }, "upload_url": "<presigned_s3_url>" }` 

**Étape 2 — Envoyer le fichier :**
```
PUT <upload_url>
Content-Type: image/jpeg
Body: <raw file bytes>
```

**Étape 3 — Sonder jusqu'à disponibilité :**
`GET /asset-uploads/{job_id}` → attendre `status == "success"` → récupérer `asset.id`.

Taille de fichier maximale : 100 MB. Types pris en charge : `image/jpeg`, `image/png`, `image/webp`.

---

## Export

**Pourquoi exporter chaque design :** la vignette renvoyée par l'autofill à
`design.canva.ai/...` est une URL CDN authentifiée de courte durée — elle expire
en quelques minutes et s'affiche comme un placeholder cassé « Afficher l'image »
si on l'intègre dans une image markdown après expiration. La sortie de
`POST /exports` est une **URL permanente**, sûre à intégrer dans les aperçus de
chat, à joindre aux posts HubSpot et à partager avec le dirigeant.

Exporte toujours chaque design après sa génération, avant d'afficher les
aperçus.

```
POST /exports
{
  "design_id": "<design_id>",
  "format": {
    "type": "png",
    "export_quality": "regular",
    "pages": [1]
  }
}
```

Sonde `GET /exports/{job_id}` jusqu'à `status == "success"`. La réponse inclut
`urls[]` — utilise `urls[0]` comme lien d'aperçu et comme URL de pièce jointe
HubSpot.

**Équivalents Canva MCP** (quand tu utilises le connecteur Canva de Cowork au
lieu du REST direct) :

| Besoin | Outil MCP | Retourne |
|------|---------|---------|
| URL d'aperçu permanente | `export-design` | URL de téléchargement permanente (sûre à intégrer) |
| Vignette par page (plus stable que la réponse d'autofill, non permanente) | `get-design-thumbnail` | URL de vignette de page |
| Métadonnées du design uniquement | `get-design` | Titre, propriétaire, nombre de pages, vignette |
| Envoi depuis la machine du dirigeant | `upload-asset-from-url` | `asset_id` (une URL par appel) |

**Choix du format par canal :**

| Canal | Type | Dimensions |
|---------|------|-----------|
| Flux Instagram | `png` | 1080×1080 (carré) |
| Story / couverture Reels Instagram | `png` | 1080×1920 |
| Flux Facebook | `png` | 1200×630 |
| En-tête d'email | `png` | 600×200 |

---

## Limites de débit et budget de génération

**Limite stricte :** 100 requêtes par minute et par token.

**Coût par design :** ~5 appels API — 1 `POST /autofills` + 1 `POST /exports`
+ ~3 tours de sondage (`GET /autofills/{job_id}`, `GET /exports/{job_id}`).
La cadence de sondage doit être de 3 à 5 secondes ; sonder plus vite brûle du
quota sans accélérer l'achèvement.

**Plafond de sécurité :** ~15 à 20 designs par minute laisse une marge
confortable sous le plafond de 100 req/min.

**Rythme recommandé (utilisé à l'Étape 3) :**

```
3 candidats par ligne × 1 ligne à la fois × 30 s d'écart entre les lignes
= 6 designs (~30 appels API) toutes les 30 secondes
= 12 designs / minute, environ la moitié du plafond
```

**Formule de budget en phase préparatoire :**

```
total_designs = (lignes Canva) × (candidats par ligne, 3 par défaut)
total_api_calls ≈ total_designs × 5
generation_time ≈ (total_designs / 12) minutes
```

**Schéma de recul sur `RATE_LIMIT_EXCEEDED` :**

1. Première occurrence dans une session → attendre 60 s, réessayer ce seul
   candidat. Traite l'erreur comme un pic transitoire.
2. Deuxième occurrence dans la même session, ou toute erreur `quota_exceeded` /
   de plafond quotidien → arrêter la génération et afficher l'avancement au
   dirigeant. Ne pas réessayer. Le skill demande au dirigeant s'il faut (a)
   passer à 1 candidat par ligne restante, (b) mettre en pause et reprendre dans
   60 minutes, ou (c) arrêter et passer aux légendes avec ce qui est déjà
   généré.

---

## Codes d'erreur

| Code | Signification | Conduite à tenir |
|------|---------|-----------|
| `PERMISSION_DENIED` | Scope manquant ou mauvaise formule | Vérifie la formule ; demande à l'utilisateur de reconnecter Canva avec les bons scopes |
| `DESIGN_NOT_FOUND` | Mauvais design ID | Reliste les designs et confirme l'ID |
| `AUTOFILL_FIELD_NOT_FOUND` | Nom de champ du template incohérent | Appelle `GET /brand-templates/{id}` et relis `dataset[].label` |
| `RATE_LIMIT_EXCEEDED` | Trop de requêtes | Première occurrence : attendre 60 s, réessayer une fois. Deuxième occurrence : arrêter et demander au dirigeant (voir Limites de débit ci-dessus) |
| `JOB_FAILED` | Échec du job asynchrone | Vérifie `job.error.message` ; cause fréquente : ressource trop volumineuse |

### reference/examples/boutique-brief-campaign.md
# Exemple détaillé : brief boutique → campagne

**Entreprise :** Bloom & Thread — boutique de vêtements pour femmes, Charleston SC  
**Formule Canva :** Teams (pas d'Enterprise)  
**Formule HubSpot :** Marketing Hub Professional  
**Source du brief :** sortie du skill content-strategy (validé par le dirigeant)

---

## Entrée : brief validé (résumé)

```
À pousser fort : robes d'été en lin (meilleure vente, tendance +22 % vs mois précédent)
À maintenir : accessoires
Opportunité saisonnière : transition rentrée (bascule le 15 août)
Offre : 2 robes achetées, 1 accessoire offert (du 1er juin au 31 juillet)
Canaux : flux Instagram, story Instagram, flux Facebook
Rythme : 3× par semaine, lun./mer./ven., 10 h 00 ET
Voix : chaleureuse, conversationnelle, humour léger. Pas de copie d'entreprise.
```

---

## Étape 1 : calendrier de publication (présenté pour approbation)

| Date | Canal | Thème | Type de ressource | Angle légende |
|------|-------|-------|------------------|---------------|
| 2 juin | Flux Instagram | Lancement des robes en lin | Post carré | Présentation produit — « enfin, une robe que tu peux porter partout » |
| 4 juin | Flux Facebook | Robes en lin | Post paysage | Preuve sociale — « la pièce la plus plébiscitée ce printemps » |
| 6 juin | Story Instagram | Offre 2 achetées 1 offert | Story (16:9) | Urgence de l'offre — swipe vers le haut |
| 9 juin | Flux Instagram | Conseil de style lin | Post carré | Pédagogie — « 3 façons de styliser la midi en lin » |
| 11 juin | Flux Facebook | Dans les coulisses | Post paysage | Histoire de marque — comment c'est fabriqué |
| 13 juin | Story Instagram | Inspiration tenue du week-end | Story (16:9) | Mode de vie — « ton samedi, réglé » |
| … | … | … | … | … |

*Dirigeant valide — « décale le 11 juin au 12, je poste sur la promo ce
jour-là. Sinon c'est très bien. »*  
*(Calendrier mis à jour ; passage à l'Étape 2.)*

---

## Étape 2 : génération des ressources Canva (chemin Pro/Teams)

**Échange pour le choix du template :**

```
Claude : J'ai trouvé 3 templates de post carré dans ta bibliothèque Canva :
  1. Boutique Square - Cream  (dernière modification avril 2026)
  2. Summer Promo - Sand      (dernière modification mars 2026)
  3. Product Feature Bold     (dernière modification février 2026)
  Lequel dois-je utiliser pour les posts de flux ?

Dirigeant : Le crème, le n°1.

Claude : Parfait. J'utilise « Boutique Square - Cream » pour tous les posts de flux.
         Je crée les coques de design maintenant — je te donnerai les liens
         pour remplir les photos produits et les textes dans Canva, puis je
         reviendrai te voir pour l'export.
```

*[Designs créés ; le dirigeant remplit tout dans Canva ; il renvoie les design IDs]*

**Sortie d'export :**
```
Export des aperçus...
✓ Post de flux du 2 juin  → https://canva.com/export/abc123.png
✓ Facebook du 4 juin      → https://canva.com/export/def456.png
✓ Story du 6 juin         → https://canva.com/export/ghi789.png
[…]
```

*Dirigeant : « Ils sont super. Vas-y. »*

---

## Étape 3 : légendes rédigées

**2 juin — flux Instagram (lancement des robes en lin)**
```
Enfin, une robe que tu peux porter au marché du producteur *et* au dîner. 🌿

Notre midi en lin vient d'arriver et c'est déjà la pièce la plus demandée
cet été. Respirante, sans effort, et oui — elle a des poches.

Attrape la tienne avant que les tailles partent → lien en bio.

#LinenDress #CharlestonStyle #SummerFashion #BloomAndThread
```

**4 juin — flux Facebook (preuve sociale)**
```
« Je l'ai portée quatre fois cette semaine et je ne regrette absolument rien. »

C'est un vrai avis d'une vraie cliente sur notre midi en lin. Entre nous, ça
ne nous surprend pas. Découvre la collection au lien ci-dessous.
```

**6 juin — story Instagram (offre)**
```
👗 2 robes achetées → 1 accessoire OFFERT

Offre valable du 1er juin au 31 juillet. Ne fais pas la sourde oreille.

Swipe vers le haut pour acheter →
```

*Dirigeant valide avec une modification : « légende du 4 juin — ajoute le prix
à la fin. « 88 €, lien ci-dessous. » »*  
*Légende mise à jour.*

---

## Étape 4 : mise en file HubSpot

**Campagne créée :**
```
Campagne : « Bloom & Thread — Lin d'été 2026 »
Début : 2 juin 2026 | Fin : 31 juillet 2026
Campaign ID : 8a72c1f4...
```

**File planifiée (3 premiers) :**

| Planifié | Canal | Aperçu de la légende | Statut |
|-----------|-------|---------------------|--------|
| 2 juin, 10 h 00 ET | Instagram | « Enfin, une robe que tu peux porter… » | SCHEDULED |
| 4 juin, 10 h 00 ET | Facebook | « Je l'ai portée quatre fois… » | SCHEDULED |
| 6 juin, 10 h 00 ET | Instagram Story | « 2 robes achetées → 1 accessoire OFFERT… » | SCHEDULED |

**Message final au dirigeant :**
```
Ta campagne est mise en file dans HubSpot :
https://app.hubspot.com/content/12345/social/campaigns/8a72c1f4

Les posts se publieront automatiquement à l'heure prévue. Tu peux annuler
ou modifier n'importe quel post dans HubSpot avant sa publication. Un
changement à faire avant qu'on ait fini ?
```

---

## Exemple de contenu email (texte seul — aucun Canva)

Les lignes email sautent entièrement Canva. Claude rédige l'objet, le
pré-en-tête et le corps de l'email en prose simple à l'Étape 3, et le dirigeant
copie le contenu dans son outil d'email quand il est prêt à envoyer.

**Ligne de calendrier :**

| Date | Canal | Thème | Type de ressource | Angle |
|------|-------|-------|------------------|-------|
| 5 juin | Email | Lancement du lin d'été | Email (texte) | Bénéfice client principal + offre |

**Sortie de l'Étape 3 (en ligne, sans Canva) :**

```
Objet : Du lin qui respire vraiment
Pré-en-tête : Nouveautés d'été en lin — plus un petit cadeau si tu en prends deux.

La première série de midi en lin vient d'arriver en boutique. Ce sont des robes
que tu peux porter à un brunch, à un mariage ou à la sortie d'école sans avoir
l'impression d'avoir tranché une question de garde-robe.

Quelques précisions :
  • Tailles XS–XL, quatre coloris
  • Des poches (vraies)
  • 2 robes achetées jusqu'au 31 juillet et on t'offre un accessoire

Passe nous voir au 412 King Street ce week-end, ou commande en ligne ci-dessous.

Découvre la collection lin →
 
— Maya
Bloom & Thread
```

**Transmission à l'Étape 4 :**

```
Tes posts sociaux sont planifiés dans HubSpot : [lien]

Le contenu email du 5 juin est rédigé ci-dessus — copie-le dans ton outil
d'email quand tu seras prêt à envoyer. Nous ne mettons pas les emails en
file directement ; ça te laisse prévisualiser la mise en forme dans ta
plateforme d'envoi avant tout.
```

### reference/gotchas.md
# Pièges

Modes de défaillance courants du skill canva-creator.

---

## Piège : générer un design Canva pour une ligne email

**Pourquoi c'est important :** Canva est totalement hors périmètre pour le
chemin email. L'autofill de template email de Canva produit des visuels de
remplacement (paysages de banque d'images, rectangles vides) dans les tuiles de
grille de services, et les vignettes de variante ne s'affichent pas dans le
chat. Les emails sont en texte seul pour ce skill, sans exception. Générer un
design Canva pour un email — même un seul — enfreint cette règle.

### ✗ Mauvais

```
Le calendrier compte 6 lignes sociales + 2 lignes email.
→ L'Étape 2 génère 6 designs sociaux + 2 designs email.
→ Les designs email partent avec des tuiles de services de remplacement.
```

Ou toute variante : « Je vais générer le template email juste pour te
montrer une référence visuelle », « J'ai trouvé un template email qui pourrait
marcher, tu veux un aperçu ? », « Voici un design Canva pour l'email du
5 juin… » — tout est interdit.

### ✓ Bon

```
Étape 1 : calendrier construit avec la colonne Path.
  - 6 lignes étiquetées Canva (social)
  - 2 lignes étiquetées Texte seul (aucun Canva)
Étape 2 : génère exactement 6 designs Canva. Les lignes email ne passent par
         aucun endpoint Canva.
Étape 3 : rédige 6 légendes sociales + 2 emails complets (objet + pré-en-tête
         + corps) en texte brut.
Étape 4 : met 6 posts sociaux en file dans HubSpot. Affiche les 2 emails en
         ligne pour que le dirigeant les copie dans son outil d'email.
```

Si le dirigeant demande explicitement un design Canva pour un email (« tu peux
me faire une version Canva de l'email du 5 juin ? »), redirige : « Ce skill
garde les emails en texte seul parce que le chemin email Canva produit des
visuels de remplacement. Si tu veux un email conçu sur Canva, construis-le
directement dans Canva et je peux t'aider à rédiger le texte ici. »

---

## Piège : générer sans plan de budget

**Pourquoi c'est important :** Canva plafonne l'usage de l'API à 100 requêtes
par minute et par token, et chaque design coûte ~5 appels (autofill + export +
sondage). Une campagne de 10 lignes avec 4 candidats par ligne génère 40
designs et ~200 appels API — et le calcul empire avec le parallélisme. Sans
budget préparé en amont, le dirigeant bute sur son quota en plein milieu de
campagne, sans chemin de récupération clair, avec quatre posts déjà générés
mais inutilisés.

### ✗ Mauvais

```
Calendrier validé → lance immédiatement 4 candidats × 8 lignes en parallèle
→ ~160 appels API en 90 secondes → RATE_LIMIT_EXCEEDED au post 5 → boucle
de réessais → dirigeant bloqué.
```

### ✓ Bon

```
Phase préparatoire : « 8 lignes Canva × 3 candidats = 24 designs, ~120 appels
API. Je lance avec le défaut de 3 candidats par ligne ? »

Étape 3 : les 3 candidats de la ligne 1 partent en parallèle → pause 30 s →
ligne 2 → pause 30 s → ligne 3 → … terminé à ~12 designs/minute, bien en
dessous du quota.

Si le quota est atteint malgré tout : arrête-toi, affiche l'avancement, demande
au dirigeant s'il faut passer à un seul candidat, mettre en pause une heure, ou
passer aux légendes avec ce qui est fait.
```

---

## Piège : sauter le Point de contrôle 1 (approbation du calendrier) avant de générer les ressources

**Pourquoi c'est important :** générer 10 designs Canva ou plus coûte des
appels API, du temps et l'attention de l'utilisateur. Si le calendrier a les
mauvaises dates, les mauvais canaux, ou si le dirigeant change d'avis sur un
thème, tout ce travail part à la poubelle. Le point de contrôle du calendrier
est l'endroit le moins cher où rattraper un désalignement.

### ✗ Mauvais

Reçois le brief → lance immédiatement `POST /autofills` pour les 12 posts →
présente les designs avant que le dirigeant ait validé le calendrier.

Dirigeant : « Ah attends, je ne voulais aucun post la semaine du 15, je suis
en déplacement. »

### ✓ Bon

Présente d'abord le tableau calendrier. Attends un « c'est bon » explicite
avant d'ouvrir le moindre appel à l'API Canva.

---

## Piège : le template a plus d'emplacements d'image que le brief ne fournit de photos

**Pourquoi c'est important :** les templates sociaux multi-images (carrousels
Instagram, grilles produits) peuvent avoir 3 emplacements d'image ou plus. Quand
le brief ne te donne qu'1 photo et que le template en exige 3, les emplacements
non remplis affichent sans bruit le visuel paysage de la banque d'images Canva
— des nuages génériques et des collines vertes là où il faudrait des photos
produit. Le design paraît « complet » jusqu'à ce que le dirigeant l'ouvre.

(Note : dans ce skill, les lignes email sautent entièrement Canva — voir
l'Étape 3 du SKILL.md. Ce piège ne concerne que les templates sociaux avec
plusieurs emplacements d'image.)

### ✗ Mauvais

Construis le manifeste avec une ligne par design (« Carrousel — a besoin de
Hero_Image »). Envoie l'unique photo. Génère. Le carrousel part avec la
diapositive 1 remplie et les diapositives 2-3 qui montrent toutes deux le même
paysage générique.

### ✓ Bon

Construis le manifeste emplacement par emplacement. Affiche explicitement le
manque :

```
Le template « carousel 3 produits » a 3 emplacements d'image. Le brief ne m'a
donné qu'1 photo. Comment remplir les 2 autres ?

1. Réutiliser la même photo dans les 3 emplacements
2. Je t'envoie 2 photos de plus
3. Choisir un template à une seule image
```

Attends le choix du dirigeant avant de générer. Ne laisse pas partir des
visuels de remplacement.

---

## Piège : se fier à `status: success` sans exporter ni vérifier visuellement

**Pourquoi c'est important :** un job d'autofill réussi signifie que Canva a
accepté la requête et a produit un design — pas que le design contient les
bonnes images. Si un `asset_id` était vide, périmé ou du mauvais type, le job
renvoie quand même `status: success` et le design s'affiche avec les visuels de
remplacement par défaut. Le seul moyen de le savoir, c'est de regarder le
rendu.

### ✗ Mauvais

```
Statut du job : success ✓
result.design.id : présent ✓
→ Présente au dirigeant
```

Résultat : le dirigeant ouvre le carrousel et voit des paysages de banque
d'images dans 3 designs sur 4.

### ✓ Bon

Une fois le job réussi, exporte chaque design en PNG permanent via
`POST /exports` (ou le MCP `export-design`). Regarde chaque PNG et confirme
qu'il contient de vraies ressources — pas le paysage par défaut de Canva, pas
de rectangles gris, pas de texte lorem-ipsum. Ne présente au dirigeant
qu'après une vérification visuelle passée.

---

## Piège : un design d'un lot ne s'affiche pas

**Pourquoi c'est important :** quand 1 design sur 4 d'un lot échoue (erreur de
job, URL d'aperçu expirée, placeholder affiché) et que tu présentes quand même
le carrousel partiel, le dirigeant voit trois vrais designs et un rectangle gris
« Afficher l'image ». Il perd confiance dans tout le reste du carrousel, même
si le reste est bon.

### ✗ Mauvais

```
Les designs de la semaine 1 sont prêts :
[Option A — véritable aperçu]
[Option B — véritable aperçu]
[Option C — véritable aperçu]
[Option D — placeholder « Afficher l'image »]
Lequel dois-je utiliser ?
```

### ✓ Bon

Quand tu repères le design cassé à la vérification du point 6, régénère juste
ce design avec le bon asset_id. Réexporte, revérifie. Ne présente qu'une fois
que les quatre designs du lot ont des aperçus permanents et vérifiés. Si la
seconde tentative échoue aussi, demande au dirigeant s'il faut passer, changer
de template, ou essayer une autre photo.

---

## Piège : générer des ressources sans vérifier que tous les champs d'autofill ont une valeur

**Pourquoi c'est important :** l'autofill de Canva affiche sans bruit des
placeholders vides quand une valeur de champ manque ou que l'`asset_id`
référencé n'existe pas. Le résultat, c'est un template à l'air professionnel
avec des rectangles blancs vides là où devraient être la photo produit et le
titre.

### ✗ Mauvais

Construis le calendrier → lance immédiatement tous les `POST /autofills` en
parallèle → la moitié des designs reviennent avec des placeholders d'image
vides parce que les photos produits n'avaient pas été envoyées d'abord.

### ✓ Bon

Construis le calendrier → inventorie chaque emplacement de champ d'autofill
emplacement par emplacement → envoie les images produits manquantes →
confirme toutes les valeurs de champ avec le dirigeant → puis génère les
designs en parallèle, avec chaque champ pré-rempli.

---

## Piège : passer des valeurs invalides aux champs image d'autofill

**Pourquoi c'est important :** quand un champ image d'autofill reçoit une
chaîne vide, un chemin de fichier, une URL ou un `asset_id` périmé/invalide,
Canva ne remonte pas d'erreur — il affiche sans bruit le placeholder par
défaut du template (par ex. un paysage générique avec nuages et collines). Le
design paraît « terminé » alors que l'image principale est une image de banque
d'images, pas la photo produit du dirigeant.

### ✗ Mauvais

Envoie la photo produit → n'attends pas la fin du job d'envoi → passe le
`job_id` (et non l'`asset.id`) dans les données d'autofill → le design
s'affiche avec un paysage de remplacement au lieu de la photo produit.

### ✓ Bon

Envoie la photo produit via `POST /v1/asset-uploads` → sonde
`GET /v1/asset-uploads/{job_id}` jusqu'à `status == "success"` → extrais
`asset.id` de la réponse → passe cet ID exact dans le champ image d'autofill.
Vérifie que chaque champ image a un `asset.id` confirmé avant d'appeler
`POST /autofills`.

---

## Piège : intégrer les URL de vignettes du CDN Canva dans du markdown

**Pourquoi c'est important :** la réponse d'autofill de Canva renvoie des URL
CDN authentifiées de courte durée, en `design.canva.ai`. Elles expirent en
quelques minutes. Si Claude les intègre comme images markdown
(`![](design.canva.ai/...)`), elles s'affichent comme des placeholders
« Afficher l'image » cassés au moment où le message est montré.

### ✗ Mauvais

Génère 8 designs → intègre manuellement chaque URL de vignette CDN dans la
réponse sous la forme `![Hero 1](https://design.canva.ai/xxx)` → toutes les
images s'affichent en placeholders gris cassés, les URL ayant expiré avant le
rendu.

### ✓ Bon

Soit tu laisses le carrousel natif de Cowork afficher automatiquement le
résultat de l'outil, soit tu exportes chaque design via `POST /exports` et
tu intègres l'URL d'export **permanente**. En dernier recours, mets un lien
vers l'URL d'édition permanente du design
(`https://www.canva.com/d/{design_id}`). Ne réintègre jamais les URL
`design.canva.ai`.

---

## Piège : lister les designs un par un comme blocs d'image individuels

**Pourquoi c'est important :** quand Claude liste chaque design comme un bloc
séparé (« Hero 1 / [image] / Hero 2 / [image] »), les images s'affichent comme
des placeholders gris cassés « Afficher l'image ». Présenter tous les designs
ensemble dans un seul lot groupé déclenche le carrousel côte à côte de Cowork,
qui s'affiche correctement.

### ✗ Mauvais

```
Hero 1 — portfolio multi-biens
[Afficher l'image]
Voir dans Canva : https://canva.com/d/xxx

Hero 2 — étude de cas marché côtier
[Afficher l'image]
Voir dans Canva : https://canva.com/d/yyy
```

### ✓ Bon

Présente tous les designs dans une seule réponse groupée pour qu'ils
s'affichent en carrousel côte à côte. Sous le carrousel, ajoute une seule
invite :

```
Voici 4 designs hero pour la Semaine 1. Fais défiler le carrousel
ci-dessus et dis-moi lequel garder.
```

---

## Piège : générer les designs en séquence au lieu de les paralléliser

**Pourquoi c'est important :** générer les designs un par un oblige le
dirigeant à attendre N allers-retours au lieu d'un seul. Lance toutes les
requêtes de génération d'un lot en une fois et présente le choix après la fin
de tous les jobs.

### ✗ Mauvais

Génère le design 1 → attends → affiche-le → génère le design 2 → attends →
affiche-le → … × 8 designs. Le dirigeant regarde couler un filet pendant 10
minutes.

### ✓ Bon

Lance tous les designs du lot en cours en une fois → sonde tous les jobs en
parallèle → une fois tous les jobs terminés, exporte chacun → vérifie
visuellement → puis présente.

---

## Piège : choisir automatiquement un template de marque pour les utilisateurs Pro/Teams

**Pourquoi c'est important :** les utilisateurs Pro/Teams n'ont pas accès à
l'API des templates de marque. Si Claude devine un template par son nom et
génère avec le mauvais, le dirigeant obtient des design dans les mauvaises
couleurs/polices et doit refaire le travail à la main dans Canva.

### ✗ Mauvais

```
Template « Square Post - Blue » trouvé. Utilisé pour tous les posts de flux.
```
…suivi de 8 designs en bleu alors que la marque est verte.

### ✓ Bon

```
J'ai trouvé 3 templates dans ta bibliothèque Canva qui pourraient convenir
aux posts de flux :
1. Square Post - Blue  (dernière modification mars 2026)
2. Summer Promo - Green  (dernière modification avril 2026)
3. Product Feature Card  (dernière modification janv. 2026)

Lequel dois-je utiliser ?
```

---

## Piège : dérive de la voix des légendes sur un long calendrier

**Pourquoi c'est important :** quand tu rédiges 12 à 20 légendes d'un seul
trait, le ton a tendance à dériver — les premières légendes suivent les
marqueurs de voix du brief, les suivantes glissent vers une copie marketing
générique. Les dirigeants le remarquent immédiatement.

### ✗ Mauvais

Post 1 : « Nos bougies artisanales sont le cadeau d'été parfait 🌿 »
(conforme au brief : « chaleureux, conversationnel »)  
Post 10 : « Sublimez votre ambiance avec notre collection de parfums
artisanaux. » (dérive corporate)

### ✓ Bon

Avant de rédiger, ancre-toi sur 2 à 3 marqueurs de ton du brief (par ex.
« décontracté, amical, humour léger »). Relis la première légende rédigée
avant d'écrire chaque nouvelle. Si le dirigeant signale une legsende au
mauvais ton, relis cette légende et fais-en le point de recalibrage pour les
prochaines.

---

## Piège : mettre des posts HubSpot en file sans vérifier que `scheduledAt` est dans le futur

**Pourquoi c'est important :** HubSpot rejette avec une erreur de validation les
posts dont `scheduledAt` est dans le passé. Si le calendrier a été construit à
une date antérieure et que le dirigeant ne met en file que maintenant, certaines
dates sont peut-être déjà passées.

### ✗ Mauvais

Construit le calendrier le 1er avril pour des posts de juin → le dirigeant
valide le 15 mai → tu essaies de mettre en file sans vérifier → le post du
« 30 avril à 10 h 00 » renvoie une erreur 400.

### ✓ Bon

Avant d'appeler `POST /social/posts`, compare chaque `scheduledAt` à l'heure
UTC actuelle. Si une date de post est déjà passée, affiche-la : « Le post
planifié pour le 30 avril est déjà passé. Je le saute, ou je le reprogramme
pour la semaine prochaine ? »

### reference/hubspot-staging.md
# Référence — mise en file des campagnes HubSpot

Prérequis : **HubSpot Marketing Hub Professional** (ou supérieur).  
URL de base : `https://api.hubapi.com`  
Auth : jeton Bearer (OAuth 2.0 ou jeton d'application privée).

---

## Sommaire

1. [Vérification de la formule](#vérification-de-la-formule)
2. [Créer une campagne](#créer-une-campagne)
3. [Créer un post social](#créer-un-post-social)
4. [Vérifier la file planifiée](#vérifier-la-file-planifiée)
5. [Repli CSV (utilisateurs non-Professional)](#repli-csv-utilisateurs-non-professional)
6. [Référence des champs](#référence-des-champs)

---

## Vérification de la formule

Si tu ne sais pas si l'utilisateur a Marketing Hub Professional :

```
GET /crm/v3/objects/companies?limit=1
```

Vérifie le `subscriptionType` du compte. Si l'API renvoie un 403 sur les
endpoints sociaux, dis à l'utilisateur : « La mise en file de campagnes
HubSpot exige Marketing Hub Professional. Ton offre actuelle ne l'inclut pas. Je
peu exporter un CSV de planification à la place — ça te conviendrait ? »

---

## Créer une campagne

```
POST /marketing/v3/campaigns
{
  "name": "Summer Sale 2026 — Social",
  "startDate": "2026-06-01",
  "endDate":   "2026-06-30",
  "currencyCode": "<Devise issue du bloc Business context, par ex. EUR>",
  "utm": {
    "source": "social",
    "medium": "owned",
    "campaign": "summer-sale-2026"
  }
}
```

Réponse : `{ "id": "<campaign_id>", ... }` — garde-la pour l'association des
posts sociaux.

---

## Créer un post social

Un appel par ligne de calendrier. Mets en file avec `SCHEDULED`, jamais
`PUBLISHED`.

```
POST /marketing/v3/social/posts
{
  "campaignId": "<campaign_id>",
  "channelId":  "<hubspot_channel_id>",
  "content": {
    "body": "<approved caption text>"
  },
  "scheduledAt": "2026-06-03T10:00:00Z",
  "attachments": [
    {
      "url": "<canva_export_png_url>"
    }
  ],
  "status": "SCHEDULED"
}
```

**`channelId`** — l'ID de compte HubSpot Social (pas le nom de la plateforme).
Récupère les comptes connectés :
```
GET /marketing/v3/social/channels
```
Fais la correspondance via `type` (`INSTAGRAM`, `FACEBOOK`, `TWITTER`, `LINKEDIN`) et utilise le champ `id`.

**`scheduledAt`** — doit être dans le futur (par rapport à l'heure de l'appel
API). Utilise midi en heure locale du fuseau du dirigeant, sauf indication
contraire.

---

## Vérifier la file planifiée

Après avoir mis tous les posts en file :

```
GET /marketing/v3/social/posts?status=SCHEDULED&campaignId=<campaign_id>
```

Affiche les résultats dans un tableau : date, canal, 60 premiers caractères de
la légende, statut. Donne l'URL directe de la campagne HubSpot :
`https://app.hubspot.com/content/{portalId}/social/campaigns/{campaign_id}`

Dis à l'utilisateur : « Les posts sont planifiés et se publieront
automatiquement. Tu peux annuler ou modifier n'importe quel post dans HubSpot
avant l'heure d'envoi. »

---

## Repli CSV (utilisateurs non-Professional)

Quand la mise en file HubSpot n'est pas disponible, exporte un CSV que
l'utilisateur pourra importer dans Buffer, Later ou son planificateur de
choix.

En-têtes de colonnes :
```
Date,Time,Channel,Caption,ImageURL,Status
```

Exemple de ligne :
```
2026-06-03,10:00 AM CDT,Instagram,"Summer Sale: 30% off candles ☀️ ...",https://canva.com/export/...,Scheduled
```

Dis à l'utilisateur : « Ton offre HubSpot n'inclut pas la mise en file
sociale, j'ai donc préparé un CSV de planification. Tu peux l'importer dans
Buffer ou Later. [chemin du fichier] »

---

## Référence des champs

| Champ | Type | Notes |
|-------|------|-------|
| `campaignId` | string | UUID renvoyé à la création de la campagne |
| `channelId` | string | Issu de `GET /social/channels` |
| `content.body` | string | Texte de la légende ; 2 000 caractères max |
| `scheduledAt` | ISO 8601 | Doit être dans le futur ; inclure le décalage de fuseau horaire |
| `attachments[].url` | string | URL publique (l'URL d'export Canva convient) |
| `status` | enum | Toujours `"SCHEDULED"` — jamais `"PUBLISHED"` |

---

Demande de l'utilisateur :
Brief approuvé : 3 posts Instagram pour la vente d'été, -20 % du 1er au 15 juillet. Exécute la campagne.

Réponds en français, de manière complète et actionnable, comme un assistant de direction pour PME.
Écris ta réponse complète dans le fichier /Users/macbook/small/evals/scale/runs/canva-creator/with.md (crée-le).
Quand c'est fait, réponds uniquement : OK
