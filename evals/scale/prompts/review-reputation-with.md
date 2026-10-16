Tu es un assistant pour dirigeants de PME françaises.
Le skill suivant est à ta disposition — suis-le pour répondre :

### SKILL.md
---
name: review-reputation
description: >
  Suit les avis clients : Google Business Profile, Trustpilot, Avis Vérifiés,
  TripAdvisor. Retire Yelp. À utiliser quand le dirigeant dit « les avis
  clients », « ma réputation ».
  [EN] Tracks customer reviews: Google, Trustpilot, Avis Vérifiés, TripAdvisor.
---

> Language rule: see `shared/language.md`.

# review-reputation

## Sources FR
- Google Business Profile
- Trustpilot
- Avis Vérifiés
- TripAdvisor (si applicable)

## Retirer
Yelp (non pertinent en France).

## Sortie
- Synthèse des avis par source.
- Brouillons de réponse aux avis négatifs (validation avant envoi).


### reference/churn-signals.md
# Clients silencieux et reconquête

La plupart des clients ne se plaignent pas avant de partir. Ils s'arrêtent,
c'est tout. Les trouver est un travail de données, pas un travail de sentiment.

---

## Fixe le rythme par client, pas par entreprise

Un client est silencieux quand son intervalle s'est étiré bien au-delà de *son
propre* intervalle normal. Comparer tout le monde à une moyenne unique de
l'entreprise produit une liste pleine de clients annuels parfaitement
satisfaits.

Pour chaque client ayant trois commandes ou interventions ou plus :

```
intervalle normal du client = écart médian entre ses propres commandes
silencieux                   = écart actuel > 2× son intervalle normal
disparu                     = écart actuel > 3× son intervalle normal
```

En dessous de trois commandes, il n'y a pas de rythme à mesurer. Compare plutôt
ces clients à la médiane de l'entreprise et signale-les comme une estimation dans
le rapport.

| Client | Intervalle normal | Écart actuel | Lecture |
|---|---|---|---|
| Dana R. | 3 mois | 7 mois | Silence prolongé — vaut un appel |
| Kirby St. LLC | 12 mois | 13 mois | Normal — ne pas déranger |
| M. Alvarez | 6 semaines | 5 mois | Disparition — à reconquérir |

---

## Classe par ce que la relation valait

Trie la liste des silencieux par la valeur passée, pas par la durée du silence.
Le dirigeant a le temps pour quinze conversations, pas deux cents, et les quinze
doivent être celles qui comptent.

Valeur, par ordre d'utilité : le chiffre d'affaires cumulé, puis la fréquence de
commande, puis le montant de la commande la plus récente. Utilise ce que les
données connectées soutiennent réellement et dis laquelle tu as utilisée.

**Le signal le plus fort est un couple :** un client qui a laissé un avis négatif
puis a arrêté de commander. Mets ceux-là en tête de liste quel que soit leur
valeur. Ils ont dit à l'entreprise exactement ce qui n'allait pas puis sont partis
quand même, et ce sont les plus récupérables, parce que la correction est déjà
connue.

---

## Les habitudes de commande Shopify comme signal d'opinion

Le comportement précède les avis de plusieurs semaines. Le lire tôt est la seule
chance de corriger quelque chose avant que ça ne devienne public.

À faire remonter :

- **Un délai de traitement qui s'allonge** sur une période. Compare la fenêtre à
  la précédente et rapporte les deux chiffres.
- **Des remboursements répétés sur un même produit** ou une même plage de dates.
  Trois remboursements sur le même SKU, c'est un problème de produit, pas trois
  personnes mécontentes.
- **Des expéditions partielles ou fractionnées** en hausse. Elles génèrent des
  « où est le reste de ma commande » une ou deux semaines plus tard.
- **Les clients de première commande qui ne sont jamais revenus**, en part de la
  fenêtre.

Rapporte ce que les données montrent, et rien au-delà. Si les motifs de
remboursement ne sont pas enregistrés dans les données, dis qu'ils sont
indisponibles plutôt que de déduire pourquoi les gens ont demandé à être
remboursés.

---

## Concevoir la reconquête

Un message par client, qui fait référence à quelque chose de réel : ce qu'il a
acheté, ce qui a été corrigé, la saison où son équipement est révisé. Un e-mail
générique « vous nous manque », c'est exactement ce qu'ils suppriment déjà.

Confirme ce que le dirigeant peut réellement tenir avant de rédiger. N'invente
jamais une remise, un avoir, un service offert ou un créneau prioritaire.
Demande :

```
Avant que je rédige — qu'est-ce qui est réellement sur la table pour une
reconquête ?

  Quelque chose comme une remise ou un contrôle offert
  Un simple mot personnel, sans offre
  Un appel de toi plutôt qu'un e-mail

Pour les quatre clients les plus valorisés, je suggérerais l'appel. Un e-mail à
quelqu'un qui a dépensé 9 000 € chez toi se lit comme un envoi de masse.
```

**Force de l'offre par segment :**

| Segment | Ce qui fonctionne d'habitude |
|---|---|
| Forte valeur, avis négatif laissé | Un appel personnel. Aucune offre en amont — l'excuse est l'offre |
| Forte valeur, aucune réclamation | Un mot du dirigeant, qui cite la dernière intervention |
| Valeur moyenne, activité saisonnière | Un rappel au bon moment, aucune remise nécessaire |
| Faible valeur, acheteur unique | Une seule offre peu coûteuse, puis on arrête |

**Arrête après un.** Une deuxième et une troisième tentative auprès de quelqu'un
qui n'a pas répondu abîme la marque et, pour l'e-mail, abîme la délivrabilité
pour tout le monde. Un bon message, puis on le laisse tranquille.

---

## Approbation

Chaque reconquête est rédigée pour approbation et envoyée une par une. Le
dirigeant approuve le message et l'offre qu'il contient. Une offre qui part avant
que le dirigeant ait accepté de la tenir transforme un problème de perte de
client en problème de remboursement.

### reference/examples/example-report.md
# Exemple travaillé — Okonkwo Mechanical

Ray Okonkwo demande : « Que dit-on de nous ? Notre note Google a baissé et je ne
sais pas pourquoi. »

HubSpot et PayPal sont connectés. Gmail est connecté. Shopify non. Les avis
Google viennent d'un export que Ray a téléchargé ; Yelp a été lu depuis le web.

---

## Avis et réputation — du 28 avril au 27 juillet 2026

**Note Google : 4,3 (34 avis), en baisse depuis 4,6 sur les 90 jours
précédents.** Yelp affiche 4,0 sur 11 avis visibles. Ce sont deux populations
distinctes et elles ne sont pas moyennées ensemble.

### Sources tirées

```
Avis Google (export)          14 sur la fenêtre
Yelp (web, partiel)           6   — la page n'affiche que les plus récents
Litiges PayPal                2
Tickets HubSpot               9
Fils Gmail                   11
Commandes Shopify             —   non connecté
```

Yelp est partiel : la page publique pagine et les avis plus anciens n'étaient pas
lisibles. L'export Google est complet pour la fenêtre.

---

### Thèmes

**1. Les attentes de pièces sans nouvelles (11 signaux)**

> « J'ai attendu neuf jours pour une pièce et j'ai dû appeler trois fois pour
> avoir des nouvelles. »
> — [Google, 1★, 12 juil.]

> « Personne ne nous a dit que la pièce était en rupture. Nous l'avons su quand
> nous avons appelé. »
> — [Ticket HubSpot, 30 juin]

> « Toujours rien sur la soufflante. Troisième semaine. » — [Gmail, 3 juil.]

**2. Les doubles réservations de planning (6 signaux)**

> « Ils nous ont réservé le jeudi, puis ont appelé le jeudi matin pour
> décaler. »
> — [Google, 3★, 18 juin]

> « Pose parfaite, planning catastrophe. Deux reports. » — [Yelp, 3★, 2 juil.]

**3. Les techniciens eux-mêmes, régulièrement félicités (9 signaux)**

> « Marcus s'est faufilé dans un vide sanitaire où je n'enverrais personne. Ça
> tourne parfaitement. »
> — [Google, 5★, 20 juil.]

> « La personne qui est venue a vraiment expliqué ce qui n'allait pas. Rare. »
> — [Gmail, 12 juin]

La baisse de la note ne porte pas sur le travail. Chaque avis négatif de la
fenêtre porte sur l'attente ou le planning ; c'est le travail lui-même que les
gens félicitent.

---

### Avis qui attendent une réponse

Trois sans réponse, du plus ancien au plus récent.

```
★★★☆☆  Google · 18 juin · T. Whitfield
« Ils nous ont réservé le jeudi, puis ont appelé le jeudi matin pour
décaler. »

Brouillon de réponse :
  Décaler un chantier le jeudi matin, ce n'est pas suffisant, et c'est notre
  faute. Nous sommes passés depuis à un appel de confirmation la veille pour
  que ça n'arrive plus. Merci pour ce mot honnête. — Ray

Je publie, je modifie, ou je passe ?
```

```
★☆☆☆☆  Google · 12 juil. · Dana R.
« J'ai attendu neuf jours pour une pièce et j'ai dû appeler trois fois pour
avoir des nouvelles. »

Brouillon de réponse :
  Neuf jours pour un moteur de soufflante, c'est trop long, et vous n'auriez pas
  dû avoir à nous relancer pour avoir des nouvelles. Nous avons changé notre
  façon de commander les pièces pour que ça ne se reproduise pas. Appelez-moi au
  06 12 34 56 78 et je réparerai cette attente. — Ray

Je publie, je modifie, ou je passe ?
```

```
★★★★★  Google · 20 juil. · L. Okafor
« Marcus s'est faufilé dans un vide sanitaire où je n'enverrais personne. Ça
tourne parfaitement. »

Brouillon de réponse :
  Merci — je transmets à Marcus. Il avait mentionné ce vide sanitaire. Fais-nous
  signe quand il sera temps pour la révision d'automne. — Ray

Je publie, je modifie, ou je passe ?
```

Ray approuve les trois, un par un. La réponse du 12 juillet est modifiée en
premier : il remplace « nous avons changé notre façon de commander les pièces »
par « nous commandons maintenant la pièce avant le départ du technicien », parce
que c'est ce qui a réellement changé. Cette correction rejoint les notes du
profil vocal.

---

### Clients silencieux

Classés par chiffre d'affaires cumulé. Le rythme est l'écart médian entre les
interventions, propre à chaque client ; les clients annuels ne sont donc pas sur
cette liste.

| Client | Normal | Écart actuel | Cumul | Note |
|---|---|---|---|---|
| Dana R. | 3 mois | 7 mois | 9 140 € | A laissé l'avis d'une étoile du 12 juil. |
| M. Alvarez | 6 semaines | 5 mois | 4 300 € | La dernière intervention était un report |
| Bellhaven Apts | 4 mois | 9 mois | 3 880 € | Aucune réclamation au dossier |

Dana est en tête quel que soit son montant : elle a dit à l'entreprise ce qui
n'allait pas puis s'est arrêtée. Ce couple est le signal de départ le plus net
dans les données.

Avant de rédiger quoi que ce soit :

```
Qu'est-ce qui est sur la table pour une reconquête ?

  Quelque chose comme une remise ou un contrôle offert
  Un simple mot personnel, sans offre
  Un appel de toi

Pour Dana, je suggérerais l'appel plutôt qu'un e-mail. Elle a dépensé 9 000 €
chez toi et vient de laisser une étoile — un e-mail se lit comme un envoi de
masse.
```

Ray choisit l'appel pour Dana, un mot pour les deux autres, et autorise un
contrôle d'automne offert pour Bellhaven. Rien n'est rédigé tant qu'il ne l'a pas
dit, et rien ne part tant qu'il n'a pas approuvé chaque message.

---

### Fais ces trois choses cette semaine

1. **Appelle Dana R.** C'est la cliente silencieuse la plus valorisée, et
   l'attente de pièces en est la raison. Son avis est aussi celui qui tire la
   moyenne Google vers le bas.
2. **Commande les pièces avant le départ du technicien.** Onze signaux
   répartis sur trois sources remontent au même manque, et c'est toute la raison
   du mouvement de la note.
3. **Confirme chaque chantier la veille.** Six signaux de planification, tous
   évitables avec un seul appel par chantier.

### reference/gotchas.md
# Pièges — review-reputation

## Piège : publier une réponse publique sans approbation

**Pourquoi c'est important :** une réponse à un avis est définitive, publique, et
attribuée au dirigeant par son nom. Elle est lue par chaque futur client qui
trouve cet avis. Il n'existe aucune version de « on s'en occupera au prochain
passage » qui rattrape cela.

### ✗ À éviter

Rédiger huit réponses, les publier toutes, puis montrer au dirigeant ce qui est
parti.

### ✓ À faire

Présente chaque brouillon à côté de l'avis auquel il répond et obtiens un « oui »
sur celui-là avant de le publier. Approuve un par un — une approbation par lot
sur huit réponses publiques, c'est comme ça qu'une mauvaise se met en ligne.

---

## Piège : mélanger les moyennes de notes entre plateformes

**Pourquoi c'est important :** le 4,3 de Google et le 4,0 de Yelp décrivent des
populations d'auteurs d'avis différentes. Une moyenne des deux est un nombre qui
n'existe nulle part, et le dirigeant le répétera à un client ou l'imprimera sur
un camion.

### ✗ À éviter

> Votre note globale est de 4,2 sur 45 avis.

### ✓ À faire

> Google : 4,3 (34 avis), en baisse depuis 4,6 le trimestre dernier.
> Yelp : 4,0 (11 visibles). Pools d'auteurs d'avis différents — pas de moyenne.

---

## Piège : traiter une extraction web partielle comme un relevé complet

**Pourquoi c'est important :** les pages d'avis publiques paginent, tronquent et
réordonnent. Un rapport bâti sur la première page se lit comme la vue d'ensemble,
donc le dirigeant conclut qu'il n'y a aucune nouvelle réclamation alors qu'il y
en a trois en page deux.

### ✗ À éviter

> Yelp, avis : 6

### ✓ À faire

> Yelp (web, partiel) : 6 — la page n'affiche que les plus récents

Puis demande un export une seule fois. Cela prend deux minutes au dirigeant et
corrige chaque exécution ensuite.

---

## Piège : classer les clients silencieux par le silence seul

**Pourquoi c'est important :** une liste triée par le plus long intervalle se
remplit de clients annuels parfaitement satisfaits et d'acheteurs uniques qui ne
reviendraient pas. Le dirigeant travaille le haut de la liste, la trouve inutile,
et cesse de s'en servir.

### ✗ À éviter

Trier tous les clients par le nombre de jours depuis la dernière commande et
remettre 200 noms.

### ✓ À faire

Mesure chaque client par rapport à son propre intervalle médian, puis classe par
valeur passée. Quinze noms que le dirigeant appellera vraiment valent mieux que
deux cents qu'il n'appellera pas. Mets en tête quiconque a laissé un mauvais avis
puis s'est tu, quelle que soit sa valeur — ils ont dit ce qui n'allait pas et
sont partis quand même.

---

## Piège : offrir une remise que le dirigeant n'a jamais autorisée

**Pourquoi c'est important :** un message de reconquête qui promet 20 % de
réduction est un engagement que le dirigeant devra tenir une fois le message
arrivé. Le rédiger avant d'avoir demandé transforme un problème de perte de
client en problème de marge, et le dirigeant l'apprend quand le client
l'utilise.

### ✗ À éviter

> Bonjour Dana — vous nous avez manqué. Voici 20 % de réduction sur votre
> prochaine intervention.

Personne n'a accepté 20 %.

### ✓ À faire

Demande ce qui est sur la table avant de rédiger : une offre, un simple mot, ou
un appel du dirigeant. Rédige uniquement dans les limites de cette réponse, et
dis clairement quand un appel vaut mieux qu'un bon de réduction — un e-mail à
quelqu'un qui a dépensé 9 000 € chez toi se lit comme un envoi de masse.

---

## Piège : discuter avec un auteur d'avis en public

**Pourquoi c'est important :** le public n'est pas l'auteur de l'avis. C'est le
prochain client qui lit l'échange et qui décide comment cette entreprise se
comporte quand on la provoque. Une réfutation correcte et bien étayée fait quand
même perdre ce lecteur.

### ✗ À éviter

> Nos registres montrent que le technicien est arrivé dans le créneau prévu et
> que notre politique indique clairement que les commandes de pièces prennent
> 5 à 7 jours ouvrés.

### ✓ À faire

Corrige un seul point factuel, propose un vrai canal de contact, et arrête-toi.
Moins de 60 mots. Si l'avis enfreint les règles de la plateforme, explique
honnêtement au dirigeant la voie de suppression — y compris que la plupart des
demandes sont rejetées — plutôt que de promettre qu'il sera retiré.

---

## Piège : limites de débit de PayPal sur les requêtes de litiges

**Pourquoi c'est important :** l'API des litiges PayPal bride fortement sur les
plages de dates qui contiennent beaucoup de litiges. Des nouvelles tentatives
silencieuses font perdre le temps de l'utilisateur sans aucun retour.

### ✗ À éviter

Réessayer 3× automatiquement sans retour. L'utilisateur voit un indicateur de
chargement pendant plus de 30 secondes avant une erreur.

### ✓ À faire

À la première erreur de limite de débit, saute PayPal, ajoute
`PayPal : limité — non inclus` à la section Sources, et continue avec les autres
connecteurs. Mentionne que l'utilisateur peut réessayer avec une plage de dates
plus étroite.

---

## Piège : citations verbatim paraphrasées ou résumées

**Pourquoi c'est important :** le dirigeant doit voir les mots exacts du client —
pas l'interprétation de Claude. La paraphrase détruit la crédibilité du rapport.

### ✗ À éviter

**Thème : livraison lente** (8 signaux)
> Les clients ont signalé que les livraisons arrivaient plus tard que prévu.

### ✓ À faire

**Thème : livraison lente** (8 signaux)
> « Commandé il y a 2 semaines et toujours rien — c'est inacceptable. » — [Gmail]
> « Le colis avait 10 jours de retard et le support n'a jamais répondu. » — [Zoho Desk]

---

## Piège : HubSpot qui renvoie 0 tickets, traité comme une erreur

**Pourquoi c'est important :** les portails de test et les nouveaux comptes ont
légitimement 0 ticket. Afficher un avertissement crée du bruit et érode la
confiance.

### ✗ À éviter

> ⚠️ HubSpot a renvoyé 0 ticket. Vérifie ta connexion ou tes permissions.

### ✓ À faire

Note `HubSpot tickets: 0` dans la section Sources et continue. Ne signale un
problème de connecteur que si l'authentification elle-même échoue.

---

## Piège : liste de mots-clés Gmail trop étroite

**Pourquoi c'est important :** les clients n'utilisent pas les mots-clés de
réclamation standard. Une expérience à une étoile ressort souvent sous « ça a
pris une éternité » ou « jamais deux fois », pas « déçu ».

### ✗ À éviter

Chercher uniquement : `remboursement annulation mécontent`

### ✓ À faire

Utilise la liste de départ complète dans `sources.md`, qui contient des
formulations comme « ça a pris une éternité » et « jamais deux fois ». Laisse
l'extraction des thèmes filtrer le signal du bruit — trop en inclure coûte moins
cher qu'un thème manqué.

### reference/response-patterns.md
# Réponses aux avis

Chaque réponse est rédigée pour approbation et publiée seulement après que le
dirigeant l'a lue. Une réponse publique ne peut pas être rattrapée.

Lis `../../../shared/voice-profile.md` avant de rédiger. Ces réponses partent au
nom du dirigeant, en public, définitivement. Une voix devinée est pire ici que
nulle part ailleurs dans le plugin.

**Moins de 60 mots.** Une longue réponse se lit comme une dispute, quoi qu'elle
dise.

---

## Avis négatif

Quatre parties, dans l'ordre :

1. **Nomme la chose précise.** Pas « nous sommes désolés pour votre expérience ».
   « Vous avez attendu neuf jours pour une pièce » — l'auteur de l'avis doit voir
   qu'il a été lu.
2. **Dis ce qui a changé,** si quelque chose a réellement changé. Si rien n'a
   changé, passe là-dessus plutôt que d'inventer une politique.
3. **Fais passer hors ligne avec un vrai canal.** Un nom et un numéro, pas
   « veuillez nous contacter ».
4. **Arrête.** Aucune explication de politique, aucun contexte sur le niveau
   d'activité de la saison.

### ✗ À éviter

> Nous sommes désolés que vous viviez cela. Nos registres montrent que le
> technicien est arrivé dans le créneau prévu et que notre politique indique
> clairement que les commandes de pièces prennent 5 à 7 jours ouvrés. Nous misons
> tout sur la qualité du service client et espérons que vous nousaccorderez une
> seconde chance.

Défensif, oppose la politique à quelqu'un qui est contrarié, et se lit comme une
réfutation pour chaque futur client qui le trouve.

### ✓ À faire

> Neuf jours pour un moteur de soufflante, c'est trop long, et vous n'auriez pas
> dû avoir à nous relancer pour avoir des nouvelles. Nous avons changé notre
> façon de commander les pièces pour que ça ne se reproduise pas. Appelez-moi
> directement au 06 12 34 56 78 et je réparerai cette attente.
> — Ray

---

## Avis positif

Court, précis, et manifestement écrit par une personne. Remercie pour ce qu'ils
ont réellement mentionné. Un « Merci pour les 5 étoiles ! » copié-collé sous
quatorze avis d'affilée dit à chaque lecteur que les réponses sont automatiques.

### ✓ À faire

> Merci Dana. Marcus a dit que le vide sanitaire était serré — content que ça
> tourne bien. Fais-nous signe quand il sera temps pour la révision d'automne.
> — Ray

---

## Avis mitigé

Réponds honnêtement aux deux moitiés. Les dirigeants ont tendance à ne répondre
qu'au compliment, ce qui se lit comme une façon d'esquiver la réclamation.

### ✓ À faire

> Merci pour vos mots aimables sur l'installation. Vous avez raison sur la
> planification — nous avons fait deux chantiers en même temps ce jeudi-là et
> vous l'avez payé. Nous sommes passés depuis à un appel de confirmation le jour
> même. — Ray

---

## Avis injuste ou faux

Reste calme, corrige le seul point factuel, et arrête-toi. Le public n'est pas
l'auteur de l'avis ; c'est le prochain client qui lit l'échange, et il regarde
comment l'entreprise se comporte sous provocation.

### ✓ À faire

> Nous n'avons aucune trace d'un déplacement à cette adresse, il s'agit peut-être
> d'une confusion avec une autre entreprise. Si nous avons travaillé pour vous,
> appelez-moi au 06 12 34 56 78 et je vais régler ça. — Ray

**Escalade.** Demander le retrait ne vaut la peine que si l'avis enfreint
clairement les règles de la plateforme — mauvais établissement, aucune
transaction réelle, attaques personnelles, ou conflit d'intérêts évident.
Explique au dirigeant où se situe réellement le seuil de la plateforme, que la
plupart des demandes sont rejetées, et qu'une réponse publique calme fait
généralement plus de bien qu'un combat pour le retrait. Ne dis jamais au dirigeant
qu'un avis sera retiré ; c'est la plateforme qui décide.

---

## Flux d'approbation

Présente chaque brouillon avec l'avis auquel il répond, pour que le dirigeant les
juge ensemble :

```
★☆☆☆☆  Google · 12 juil. · Dana R.
« J'ai attendu neuf jours pour une pièce et j'ai dû appeler trois fois pour
avoir des nouvelles. »

Brouillon de réponse :
  Neuf jours pour un moteur de soufflante, c'est trop long, et vous n'auriez pas
  dû avoir à nous relancer pour avoir des nouvelles. Nous avons changé notre
  façon de commander les pièces pour que ça ne se reproduise pas. Appelez-moi
  directement au 06 12 34 56 78 et je réparerai cette attente. — Ray

Je publie, je modifie, ou je passe ?
```

Approuve un par un. Une approbation par lot sur huit réponses publiques, c'est
comme ça qu'une mauvaise se met en ligne.

---

## Calendrier

Réponds aux avis négatifs sous deux ou trois jours. Une réclamation traitée
rapidement se lit comme une entreprise qui fait attention ; les mêmes mots un
mois plus tard se lisent comme de la gestion de crise.

Ne réponds pas à un avis auquel le dirigeant a déjà répondu. Vérifie s'il existe
déjà une réponse du dirigeant avant de rédiger quoi que ce soit.

### reference/sources.md
# Sources

Un seul socle obligatoire, tout le reste l'approfondit. Le skill fonctionne dès
le premier jour sans rien de connecté.

| Source | Statut | Ce qu'elle apporte |
|---|---|---|
| Un CRM (HubSpot, Monday.com, Salesforce, Zoho CRM), un connecteur de paiement (PayPal, Square, Stripe), **ou** une boutique en ligne (Shopify, Square) | Obligatoire — l'une des trois catégories | Tickets et retours ; litiges et remboursements ; ou historique des commandes (qui a acheté quoi et quand) plus les habitudes de traitement et de remboursement |
| Support desk (Zoho Desk) | Facultatif | Tickets par client, priorité et statut — les réclamations dans les mots du client |
| Gmail | Facultatif | Le langage des réclamations et des compliments dans les fils |
| Recherche web | Toujours disponible | Les avis publiquement visibles sur Google Business Profile, Trustpilot, Avis Vérifiés et Facebook ; Yelp seulement en dernier recours (marginal en France) |
| Avis collés ou exportés | Toujours disponible | La meilleure source qui soit, avec dates et notes |

---

## Avis publics

**Préféré : un export.** Google Business Profile, Trustpilot et Yelp permettent
tous au dirigeant de télécharger ses avis. Yelp reste marginal en France — le
SKILL.md le signale explicitement — ne le consulte que si aucune autre source
n'a rien donné. Un export porte la note, la date, le nom de l'auteur et le texte
intégral, et il inclut les avis que la page publique
fait disparaître par pagination. Demande-en un la première fois que ce skill
s'exécute ; cela prend deux minutes au dirigeant et améliore chaque exécution
ensuite.

**Solution de repli : ce qui est visible sur le web.** Récupère les pages d'avis
publiques de l'entreprise et lis ce qui s'affiche. C'est réellement utile et
réellement partiel — les pages tronquent, paginent et réordonnent. Dis-le dans la
section Sources plutôt que de présenter une extraction partielle comme complète.

**Également valable : du texte collé.** Le dirigeant colle des avis dans la
conversation. Étiquette-les `[Review]` comme n'importe quelle autre source et
utilise-les.

Pour compter, ne fais jamais la moyenne des notes entre sources. La moyenne de
Google et celle de Yelp sont deux chiffres sur deux populations différentes, et un
dirigeant qui répète un chiffre fusionné à un client aura tort.

---

## Litiges et tickets

**Litiges PayPal.** Récupère les litiges ouverts sur la fenêtre. PayPal bride
fortement sur les plages de dates larges. À la première erreur de limite de débit,
arrête-toi, note `PayPal : limité — non inclus` dans Sources, et continue. Ne
réessaie pas en silence ; propose plutôt une fenêtre plus étroite.

**Litiges et remboursements Stripe.** `GET /v1/disputes` créés sur la fenêtre
(via `stripe_api_read`), avec `reason` et `status` ; `GET /v1/refunds` pour la
même fenêtre, puisqu'une série de remboursements sur un même produit est un thème
avant d'être un avis. L'`evidence_details.due_by` d'un litige est une échéance —
fais remonter toute échéance ouverte dans la liste « fais ces trois choses ».

**Litiges Square.** Le point de terminaison des litiges via `make_api_request`
pour la fenêtre. Même traitement que Stripe.

**Tickets et retours HubSpot.** Récupère les tickets ouverts et récemment clos,
plus les retours envoyés. Zéro ticket est un état légitime pour un portail neuf ou
de petite taille — note `HubSpot tickets: 0` et passe à autre chose. Ne signale
un problème de connecteur que lorsque l'authentification elle-même échoue.

**Tickets Zoho Desk.** `getTickets` sur la fenêtre (`receivedInDays` 30 ou 90
pour correspondre ; tri par `recentThread`), puis `getThreads` sur ceux dont
l'objet se lit comme une réclamation, pour le verbatim. `getTicketsMetrics` donne
les compteurs ouverts, en retard et en attente pour l'en-tête. Les tickets
ouverts de priorité High appartiennent au décompte Litiges et tickets, pas
seulement à la liste des thèmes. `getTickets` refuse un paramètre `include` —
demande des champs supplémentaires avec `fields`.

---

## E-mail

Cherche sur la fenêtre les fils contenant du langage de réclamation et de
compliment. Liste de départ, volontairement large :

```
remboursement  annulation  mécontent  problème  souci  déçu  frustré  cassé
retard  lent  raté  manquant  jamais deux fois  une éternité  merci  sauveur
recommandé  super travail
```

Les clients utilisent rarement le mot « déçu ». Ils écrivent « une éternité » et
« jamais deux fois ». Trop inclure coûte peu ici, parce que l'extraction des
thèmes filtre le bruit ; une liste de mots-clés étroite perd en silence des
thèmes entiers.

Récupère l'objet et une ou deux phrases des mots du client — assez pour citer
verbatim plus tard.

---

## Shopify

Traité dans `churn-signals.md`. En bref : les commandes, les délais de
traitement et les remboursements, lus comme un comportement plutôt que comme une
opinion.

---

## Rapporter ce que tu as obtenu

Chaque exécution se termine par un bloc Sources honnête. Les décomptes, et les
échecs nommés :

```
Sources tirées — 28 avril au 27 juillet

  Avis Google (export)         14
  Yelp (web, partiel)           6   — marginal en France, et la page n'affiche que les plus récents
  Litiges Stripe                3
  Remboursements Stripe         7
  Tickets HubSpot               0
  Tickets Zoho Desk            12   — 2 ouverts, priorité High
  Fils Gmail                   11
  Commandes Shopify            182
```

Nomme le connecteur qui a réellement été lu sur chaque ligne (l'exemple
ci-dessus est une entreprise Stripe et Zoho Desk ; une entreprise PayPal et
HubSpot liste ceux-là). Le tiret compte autant que les chiffres. Une source qui
manque ressemble exactement à une source sans rien de grave, à moins qu'on la
nomme.

---

Demande de l'utilisateur :
Avis Google 2 étoiles : « livraison en retard de 4 jours, produit correct ». Comment répondre ?

Réponds en français, de manière complète et actionnable, comme un assistant de direction pour PME.
Écris ta réponse complète dans le fichier /Users/macbook/small/evals/scale/runs/review-reputation/with.md (crée-le).
Quand c'est fait, réponds uniquement : OK
