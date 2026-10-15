# Neutralité des connecteurs — règle de tout le plugin

Portée : **chaque skill, commande, fichier de référence et parcours
d'onboarding.** C'est le positionnement d'Anthropic pour le plugin, pas une
préférence maison : c'est la boîte à outils du dirigeant qui décide de ce qui
est appelé. Le plugin ne décide jamais de quel fournisseur le dirigeant
devrait avoir.

---

## La règle

**Les connecteurs d'une même catégorie sont pairs.** Un grand livre est un
grand livre. Un CRM est un CRM. Une boîte mail est une boîte mail. Aucun
skill n'en nomme un comme défaut, principal, celui qui prime, fournisseur de
repli, alternatif, ou chemin secondaire. Nomme ce qui est connecté, et tourne
dessus.

Les catégories où cela s'applique, et les connecteurs de chacune à ce jour
(alphabétique, qui est l'ordre que toutes les listes du plugin utilisent quand
plusieurs sont nommés) :

| Catégorie | Connecteurs |
|---|---|
| Grand livre comptable | MYOB, NetSuite, QuickBooks, Xero, Zoho Books |
| CRM | HubSpot, Monday.com, Salesforce, Zoho CRM |
| Données prospects et enrichissement | Apollo, Clay |
| Mail | Gmail, Microsoft 365 |
| Calendrier | Google Calendar |
| Paie | QuickBooks Payroll |
| Paiements | PayPal, Square, Stripe |
| Boutique en ligne et point de vente (tient commandes et stock) | Shopify, Square |
| Fichiers | Google Drive, Microsoft 365 |
| Support | Zoho Desk |

Salesforce est atteint comme connecteur personnalisé que le dirigeant ajoute
(son serveur Headless 360 a une adresse par organisation et un client OAuth),
pas via le manifeste du plugin ; une fois ajouté, il est pair comme les
autres. Un connecteur qui n'est pas dans ce tableau est atteint via
`build-connector`, qui consulte d'abord l'annuaire des connecteurs et
connecte via Zapier sinon. Une fois connecté, il rejoint sa catégorie comme
pair.

---

## Ce que « pairs » veut dire en pratique

**Le blocage est par catégorie, jamais par fournisseur.** Un skill qui a
besoin d'un grand livre dit « un grand livre (MYOB, NetSuite, QuickBooks,
Xero ou Zoho Books) », et n'importe lequel d'entre eux ouvre la porte. La
carte des connecteurs du routeur est écrite de la même façon.

**Deux connectés dans une catégorie : lis les deux, totalise depuis un.**
Chaque connecteur apporte ce qu'il détient en propre. Tout chiffre qui doit
venir d'une seule place — un solde de trésorerie, un total de revenus, un
chiffre de créances — vient de celui que le dirigeant nomme comme source de
référence pour ce run, et la sortie le dit. Ne totalise jamais le même
chiffre sur deux connecteurs : c'est un double comptage. Le choix multiple de
l'Étape 5 du routeur est le moyen par lequel le dirigeant le nomme ; la
réponse tient pour la session et peut être stockée dans le contexte
entreprise.

**Les limites de capacité s'énoncent en capacités, pas en jugements.** « Ce
connecteur n'a pas de chemin d'écriture de factures fournisseurs, donc les
écritures sont exportées pour saisie » est une capacité. « Xero est en
lecture seule ici, mieux si QuickBooks est en cours de migration » est un
classement. Écris la première espèce. Quand un connecteur ne peut vraiment pas
faire une partie d'un skill (MYOB ne tient pas de solde de trésorerie ; un
grand livre en lecture seule ne peut pas passer un journal ; Zoho Books ne
tient pas d'objet facture fournisseur, pas de flux bancaire, pas d'endpoints
de rapport), dis ce qu'il ne peut pas faire et ce que le skill fait à la
place, en une ligne, sans le comparer à un autre fournisseur.

**Les connecteurs à crédits disent le prix avant de dépenser.** Un
connecteur de données prospects facture des crédits par ligne enrichie. Un
skill qui en utilise un nomme le nombre de lignes et demande une fois par run
avant d'enrichir. C'est une porte d'approbation, pas un classement.

**Les notes techniques propres à un fournisseur sont permises.** Un fichier
comme `shared/quickbooks-report-traps.md` documente un comportement réel d'un
connecteur. Ce n'est pas une préférence ; c'est un piège. Garde-les,
étiquette-les comme propres au connecteur, et ajoute des fichiers frères pour
les autres connecteurs au fil de la découverte de leurs pièges.

**Les exemples travaillés peuvent nommer un fournisseur.** Un exemple doit
tourner sur quelque chose. Nommer QuickBooks dans une transcription est
correct ; dire « connectons QuickBooks d'abord » comme conseil, non. Les
exemples montrent l'outil du dirigeant en train d'être utilisé, jamais en
train d'être choisi à sa place.

---

## Un connecteur, deux enregistrements

Le manifeste du plugin (`.mcp.json`) déclare chaque connecteur de la carte
du routeur pour que la page plugin de Cowork puisse les lister. Cowork
enregistre chaque serveur déclaré sous le nom du plugin —
`small-business:trello`, `small-business:hubspot` — et ne le fusionne pas
toujours avec le même produit que le dirigeant a déjà connecté à son propre
compte. Par exemple, un dirigeant ayant Trello branché peut voir à la fois
`Trello` (autorisé) et `small-business:trello` (non autorisé). Même produit,
même serveur, deux entrées.

**L'identité, c'est le produit, pas l'enregistrement.** `small-business:<nom>`
et `<nom>` sont un seul connecteur. Règles, dans l'ordre :

1. **Appelle l'entrée autorisée.** Si les deux le sont, utilise l'entrée
   compte du dirigeant : elle a déjà le consentement, et elle survit à un
   désinstall du plugin. N'appelle jamais les deux.
2. **Deux entrées ne font pas deux connecteurs.** La règle « deux connectés
   dans une catégorie » ci-dessus est pour deux fournisseurs (deux grands
   livres, deux CRM). Deux enregistrements d'un même fournisseur ne
   déclenchent jamais la question de la source de référence.
3. **Une copie plugin non autorisée n'est pas « non connecté ».** Quand
   l'entrée du dirigeant est en vie, le connecteur est connecté, point final.
   Ne le signale pas manquant, ne demande pas au dirigeant d'autoriser la
   copie du plugin, ne l'envoie pas vers l'onglet Connecteurs pour un outil
   qui marche déjà.
4. **Quand seule la copie plugin existe et qu'elle n'est pas autorisée,**
   c'est le chemin ordinaire « connecte-le ». Dis une fois que le dirigeant
   peut l'autoriser depuis l'onglet Connecteurs du plugin ou ajouter le
   connecteur directement à son compte ; les deux marchent, aucun ne prime
   sur l'autre.
5. **Le texte dirigé vers le dirigeant nomme le produit.** « Trello », jamais
   `small-business:trello`. La ligne `Connected tools` du contexte entreprise
   ne stocke que des noms de produits, si bien qu'un skill ultérieur n'hérite
   jamais d'un nom d'enregistrement.
6. **Les préfixes de noms d'outils diffèrent.** Un outil en portée plugin
   s'appelle `mcp__plugin_small-business_<server>__<tool>` ; celui du
   dirigeant s'appelle `mcp__<Server>__<tool>`. Tout ce qui matche sur les
   noms d'outils doit matcher les deux formes.

Ce que cette règle ne peut pas faire : faire afficher une seule entrée par
Cowork. C'est un comportement de plateforme. Jusqu'à ce que cela change, le
plugin se comporte correctement avec une entrée, deux, ou deux dont une non
autorisée.

---

## Onboarding et routeur

- **Demande, ne recommande jamais.** L'onboarding demande ce que le dirigeant
  utilise pour la comptabilité, les clients, le mail. Il ne propose pas de
  fournisseur. Si le dirigeant n'a pas d'outil dans une catégorie, le chemin
  zéro-connecteur de la recette tourne et la catégorie est nommée (« quand tu
  choisiras un outil de comptabilité, connecte-le et ça ira plus profond »),
  sans nom de produit attaché.
- **On l'a, ou on le connecte, ou on replie.** Dans cet ordre, dit une fois,
  avec le compromis en une ligne. Ne vends jamais un outil concurrent parce
  que le nôtre manque.
- **Le routeur privilégie ce qui est connecté.** Ses règles de l'Étape 5 le
  disent déjà. La règle de neutralité ajoute : quand rien n'est connecté dans
  une catégorie, le routeur nomme la catégorie et le repli, pas un
  fournisseur à aller acheter.

---

## Ce que cette règle ne change pas

- **Les portes d'approbation.** Neutre ne veut pas permissif. Chaque écriture
  a toujours besoin de son oui.
- **L'honnêteté sur la portée.** Un skill construit pour le régime fiscal
  d'un pays le dit (`shared/currency-and-locale.md`). C'est une déclaration de
  portée, pas un classement de fournisseurs.

---

## Mots à éviter entre connecteurs d'une même catégorie

défaut · principal · prime sur · repli (comme étiquette de fournisseur) ·
secondaire · alternatif · moindre · chemin de secours · celui que la plupart
des dirigeants utilisent · préféré

Utilise à la place : « celui qui est connecté », « le grand livre connecté »,
« un grand livre (MYOB, NetSuite, QuickBooks, Xero ou Zoho Books) », « celui
que le dirigeant a nommé source de référence ».
