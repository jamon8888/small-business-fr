# Sage 100 Compta → faire arriver vos données mensuelles dans le plugin

Vous avez raison : il n'existe pas de connecteur officiel pour Sage 100. Pas de panique — c'est un cas classique, et il a une solution propre. Voici comment on procède.

## 1. D'abord, bornons le besoin

« Mes données mensuelles » n'a pas de fin définie : un ERP, c'est une quarantaine de choses possibles, et la réponse diffère pour chacune. Ce qu'on va brancher, c'est **un seul export, précis et testable** :

> **Exporter chaque fin de mois l'encours clients (factures non soldées) de Sage 100 Comptabilité, pour que le plugin ait la vision réelle de votre trésorerie et de vos relances.**

C'est le plus utile en compta pour le plugin, c'est un seul fichier, et c'est faisable dès ce mois-ci. Si votre besoin de départ est autre chose (balance générale, compte de résultat, un module particulier), dites-le-moi et on borne sur ça — mais un seul endpoint à la fois, pas « tout Sage ».

## 2. Ce que j'ai vérifié, dans l'ordre

| Chemin | Résultat |
|---|---|
| Annuaire des connecteurs Claude | Rien pour Sage 100. Votre constat est exact. |
| Zapier | « Sage » existe sur Zapier, mais c'est la famille cloud internationale (Sage Intacct, Sage Business Cloud) — **pas** votre Sage 100 classique en local. Pas une correspondance : même nom, produit différent. |
| API documentée | Sage 100 n'expose pas d'API REST publique documentée (les intégrations passent par des partenaires ou des offres supérieures selon les versions). À savoir, mais ce n'est pas un chemin de construction — on ne code pas à la main contre une API que personne ne maintient ici. |
| **Export CSV planifié** | **Oui.** Sage 100 Comptabilité sait exporter l'encours clients en CSV (et dans beaucoup de versions, planifier l'envoi). C'est le chemin. |

**La conclusion en trois lignes :**

- **Coût : zéro.** Pas d'offre Zapier, pas de facturation à la tâche, rien qui ne s'ajoute à vos abonnements.
- **Effort : une trentaine de minutes** de votre côté pour la première fois, puis une minute par mois.
- **Blocage : un geste manuel mensuel** (sauf si votre version planifie l'export automatiquement), et une latence de fin de mois — vos données arrivent au moment de la clôture, pas en temps réel.

## 3. La recette, concrètement

**Votre côté (deux fois la première fois, une fois par mois ensuite) :**

1. Dans Sage 100 Comptabilité, en fin de mois : exporter **l'encours clients** (factures non soldées, avec leur soldé) au format **CSV** — encodage UTF-8, séparateur `;`, montants en euros avec 2 décimales.
2. Déposer le fichier au même endroit chaque mois (le dossier de dépôt du plugin, ou la boîte e-mail surveillée qu'on vous donne), avec le mois dans le nom : `sage100-encours-2026-10.csv`.

**Mon côté (automatique, sans rien à configurer de votre part) :**

3. Je pars le fichier selon le modèle de données canonique du plugin. Voici le mapping que j'applique, pour que vous sachiez exactement ce qui est lu :

| Colonne du CSV Sage 100 | Utilisée comme |
|---|---|
| N° facture | `invoice_id` |
| Code / raison sociale du client | `customer_id` / `name` |
| Date de facture | `invoice_date` |
| Date d'échéance | `due_date` |
| Montant HT | `amount_ht` |
| TVA | `vat` |
| Montant TTC | `amount_ttc` |
| Montant payé | `paid_amount` |

Les règles que j'applique : une colonne manquante me sera demandée **une fois**, puis mémorisée ; une colonne absente est traitée comme « absent », **jamais comme zéro** ; chaque fichier porte sa date d'arrêt (as-of), reprise dans les sorties ; montants en EUR, HT par défaut.

**Côté sécurité, c'est le chemin le plus propre qui existe ici** : aucun mot de passe, aucun jeton, aucun compte à connecter — un fichier de données que vous déposez vous-même. Il n'y a rien à révoquer, et rien qui ne puisse fuiter par une conversation.

## 4. Premier test, sur vos vraies données

Au premier dépôt, je vous montre exactement ce que j'ai extrait — par exemple les trois plus gros soldés — et je vous demande : **est-ce correct ? manque-t-il quelque chose que vous attendiez à voir ?** C'est la seule façon de confirmer que le mapping a bien lu vos vraies données et que rien n'a été silencieusement déplacé d'une colonne. On ne passe en mode mensulier que quand vous avez validé ce premier passage.

## 5. Ce que ça débloque, et comment ça peut casser

**Ce qui débloque maintenant :** votre suivi de trésorerie, vos listes de relance et vos rapports mensuels peuvent s'appuyer sur les vrais soldés clients Sage 100, dès la fin du mois. Côté plugin, Sage 100 rejoint ses pairs de la catégorie compta comme un égal — le CSV n'est que le tuyau par lequel il passe, pas un label de qualité.

**Comment ça peut casser** (autantdans votre intérêt de le savoir maintenant) :

- **L'export n'arrive pas** — c'est la panne principale, et elle est silencieuse par nature. J'intègre un contrôle de péremption : si le fichier est plus vieux que l'intervalle attendu (~35 jours), je le dis expressément — « données Sage 100 périmées, dernier export du … » — au lieu de vous servir des chiffres d'octobre comme s'ils étaient d'aujourd'hui. Une sortie vide ou ancienne sera toujours nommée comme panne, pas laissée pour compte.
- **Sage change le format du CSV** lors d'une mise à jour : les en-têtes de colonnes changent et le mapping s'égare. La signature : des champs qui sautent ou des montants qui ne correspondent plus. On le détecte au test et ça se répare en quelques minutes.
- **L'encodage** (accents, `€`) : vérifié une fois au premier passage, ensuite c'est stable.

Ce que ça ne fait **pas** : lire Sage 100 en temps réel, écrire dedans, ou toucher aux autres modules (stock, immobilisations). Ce connecteur atteint l'encours clients mensuel, rien d'autre — c'est volontaire.

## 6. Et ensuite ?

Le connecteur est enregistré pour que les skills du plugin s'en servent. Trois pistes naturelles, dans l'ordre du plus utile :

1. **« Construis-moi un rapport mensuel »** — un rapport de trésorerie et de relance construit sur cet encours, chaque début de mois.
2. **« Fais-moi un brief »** — intégrer les soldés clients à l'instantané quotidien du plugin.
3. **« Automatiser ça »** — transformer le flux export → analyse en skill nommé qui tourne tout seul.

Dites-moi lequel vous voulez d'abord, ou confirmez simplement le périmètre de l'étape 1 et on part sur le premier test avec vos vraies données.
