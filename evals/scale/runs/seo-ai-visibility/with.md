# Être trouvable à Lyon — audit de visibilité (recherche + IA) et corrections

D'abord le cadre, en une ligne : ce que je peux faire, c'est vérifier que les moteurs de recherche et les assistants IA peuvent **atteindre** ton site, le **lire** sans JavaScript, et **restituer tes faits correctement** (horaires, zone, prix). Personne ne peut faire *recommander* une entreprise par une IA, et quiconque vend ça ne vend rien. Tout ce qui suit relève de l'indexabilité, de la structure et de l'exactitude — pas de l'influence.

## Ce que j'ai exploré, et ce que je n'ai pas pu vérifier

Tu m'as dit : plombier à Lyon, site en ligne, **aucune fiche Google**. Sans l'URL du site et le nom commercial, je n'ai pas pu récupérer les pages, le `robots.txt`, le HTML brut ni les données structurées existantes. Voici donc ce qui est **acté** et ce qui sera **vérifié** dès que j'ai l'URL :

- **Acté dès maintenant :** aucune fiche Google Business Profile. C'est un constat majeur — la recherche locale et les assistants s'appuient très fortement dessus, et une entreprise absente de la fiche est presque invisible sur « plombier Lyon », quelle que soit la qualité du site.
- **À vérifier sur ton site dès que j'ai l'URL :** règles du `robots.txt` (les robots d'IA sont-ils bloqués par mégarde ?), contenu visible dans le HTML brut sans JavaScript, balises title / méta-descriptions / H1, données structurées existantes, présence d'un `llms.txt`, cohérence des coordonnées (un seul téléphone, une seule adresse, des horaires identiques partout).

Je te renvoie la liste des contrôles page par page dans l'annexe — ce n'est pas un verdict, c'est la checklist qui sera exécutée sur le site réel.

## En une phrase

Ton problème principal n'est probablement pas le site : c'est l'absence de fiche Google — la source que lisent à la fois Google et les assistants — plus, très probablement, des robots d'IA bloqués par une ligne de `robots.txt` et zéro donnée structurée.

## Corrige ces cinq points, dans cet ordre

| # | Constat | Impact | Effort |
|---|---------|--------|--------|
| 1 | **Aucune fiche Google Business Profile** — le site seul ne suffit pas pour « plombier Lyon » | Élevé | Moyen (1 à 2 h) |
| 2 | **robots.txt à vérifier** — si une règle globale `Disallow: /` y figure, elle bloque ClaudeBot, GPTBot, PerplexityBot et les autres | Élevé | Petit (10 min) |
| 3 | **Données structurées schema.org absentes** (à confirmer sur le site) — les faits doivent être explicites pour les machines | Élevé | Petit (1 h) |
| 4 | **Facts clairs** : zone d'intervention en noms d'arrondissements, horaires, vraies fourchettes de prix, carte pro — au même endroit, cohérents | Élevé | Petit (30 min) |
| 5 | **Aucun `llms.txt`** (c'est le cas de l'immense majorité des sites) | Moyen | Petit (20 min) |

Les autres constats (titres, méta-descriptions, contenu des pages) seront notés et classés de la même façon une fois le site exploré — ils iront en annexe.

> Note sur le point 2 : débloquer les robots d'IA, c'est un **choix**, pas un réglage par défaut. Cela veut dire que les assistants pourront lire ton contenu. Si tu as une raison de les bloquer (contenu propriétaire), dis-le-moi et on ne touche à rien.

---

## Les fichiers, prêts à coller

Chaque bloc ci-dessous est copiable tel quel. Les passages entre crochets `[...]` sont des **trous visibles** : je ne remplace jamais un fait non confirmé par une devinette. Ils seront remplacés par les six éléments que je te demande à la fin.

### 1. `robots.txt` corrigé (à la racine du site)

```
User-agent: *
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: GPTBot
Allow: /

User-agent: OAI-SearchBot
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: Google-Extended
Allow: /

User-agent: Applebot-Extended
Allow: /

User-agent: Bingbot
Allow: /

Sitemap: https://[votre-site.fr]/sitemap.xml
```

À valider d'abord par toi (point 2 ci-dessus) ; ensuite c'est une mise à jour d'un seul fichier. Si ton objectif réel serait au contraire d'empêcher un accès, ce n'est pas `robots.txt` qui le fait — c'est un blocage côté serveur, et on ne le fait pas ici.

### 2. `llms.txt` (à la racine du site)

```
# [NOM DE L'ENTREPRISE]

> Plombier à Lyon : dépannage, débouchage, installation de sanitaires
> et de salle de bain. Intervention dans les 9 arrondissements et la
> métropole lyonnaise.

## Ce que nous faisons
- Dépannage plomberie : fuites, WC, robinetterie, chaudières
- Débouchage de canalisations (WC, évier, douche, colonne)
- Installation de sanitaires et rénovation de salle de bain
- Urgences [7 JOURS SUR 7 — À CONFIRMER]

## Où nous intervenons
Lyon : 1er, 2e, 3e, 4e, 5e, 6e, 7e, 8e, 9e arrondissements,
ainsi que Villeurbanne, Caluire-et-Cuire, Vaulx-en-Velin, Bron,
Oullins et Tassin-la-Dunguin. [LISTE À CONFIRMER]

## Horaires
[HORAIRES À CONFIRMER — ex. : lundi-vendredi 8h-18h, samedi 9h-12h]

## Tarifs
Débouchage simple : à partir de [PRIX À CONFIRMER] € TTC.
Tarif horaire : [PRIX À CONFIRMER] € HT.
Devis gratuit avant toute intervention.

## Références
Artisan du BTP, carte professionnelle CMA : [N° À CONFIRMER].
Assuré RC Pro. [ANNEE DE CREATION À CONFIRMER]

## Contact
Téléphone : [04 XX XX XX XX — À CONFIRMER]
E-mail : [E-MAIL — À CONFIRMER]
Adresse : [ADRESSE — À CONFIRMER]

## Pages clés
- Prestations : https://[votre-site.fr]/services
- Débouchage : https://[votre-site.fr]/debouchage
- Urgence : https://[votre-site.fr]/urgence
- Contact : https://[votre-site.fr]/contact
```

C'est une convention récente, pas une norme imposée : ça ne change pas magiquement ce que les assistants disent, mais ça leur donne une source nette en vingt minutes. Et chaque ligne ici, c'est quelque chose qu'un assistant peut répéter à un client — une heure fausse ou un numéro périmé fait des dégâts directs.

### 3. Données structurées (JSON-LD schema.org), prêtes à coller dans le `<head>`

**Entreprise — page d'accueil et page contact** (pas de type « Plumber » dans schema.org ; `HomeAndConstructionBusiness` est le sous-type adapté) :

```json
{
  "@context": "https://schema.org",
  "@type": "HomeAndConstructionBusiness",
  "name": "[NOM DE L'ENTREPRISE]",
  "description": "Plombier à Lyon : dépannage, débouchage de canalisations, installation de sanitaires et de salle de bain, dans les 9 arrondissements et la métropole.",
  "url": "https://[votre-site.fr]",
  "telephone": "[+33 4 XX XX XX XX — À CONFIRMER]",
  "email": "[E-MAIL — À CONFIRMER]",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "[ADRESSE — À CONFIRMER]",
    "addressLocality": "Lyon",
    "addressRegion": "Auvergne-Rhône-Alpes",
    "postalCode": "[6900X — À CONFIRMER]",
    "addressCountry": "FR"
  },
  "areaServed": [
    "Lyon 1er", "Lyon 2e", "Lyon 3e", "Lyon 4e", "Lyon 5e",
    "Lyon 6e", "Lyon 7e", "Lyon 8e", "Lyon 9e",
    "Villeurbanne", "Caluire-et-Cuire", "Vaulx-en-Velin",
    "Bron", "Oullins", "Tassin-la-Dunguin"
  ],
  "openingHoursSpecification": [
    {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday"],
      "opens": "[08:00 — À CONFIRMER]",
      "closes": "[18:00 — À CONFIRMER]"
    }
  ],
  "priceRange": "€€"
}
```

**Prestation — page « Débouchage »** (un bloc `Service` par page de prestation) :

```json
{
  "@context": "https://schema.org",
  "@type": "Service",
  "name": "Débouchage de canalisations à Lyon",
  "serviceType": "Débouchage WC, évier, douche et colonnes",
  "provider": { "@id": "https://[votre-site.fr]/#business" },
  "areaServed": "Lyon et métropole",
  "description": "Débouchage manuel, mécanique et haute pression. Devis gratuit avant intervention."
}
```

**FAQ — section questions-réponses réelles** (on ne balise une `FAQPage` que si la FAQ existe réellement sur la page) :

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Combien coûte un débouchage de WC à Lyon ?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Un débouchage simple (WC, évier, siphon) est facturé entre [PRIX À CONFIRMER] € et [PRIX À CONFIRMER] € TTC. Le débouchage mécanique va jusqu'à [PRIX À CONFIRMER] € et l'hydrocurage par camion de [PRIX À CONFIRMER] € à [PRIX À CONFIRMER] € selon l'accès à la canalisation. Le devis est donné avant l'intervention."
      }
    },
    {
      "@type": "Question",
      "name": "Intervenez-vous dans mon arrondissement à Lyon ?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Oui, nous intervenons dans les 9 arrondissements de Lyon ainsi qu'à Villeurbanne, Caluire-et-Cuire, Vaulx-en-Velin, Bron, Oullins et Tassin-la-Dunguin. [LISTE À CONFIRMER]"
      }
    },
    {
      "@type": "Question",
      "name": "En combien de temps pouvez-vous intervenir en urgence ?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "[DÉLAI DE RÉPONSE À CONFIRMER — ex. : en général sous 2 h pendant les horaires d'ouverture, le jour même en dehors. Si nous ne pouvons pas tenir ce délai, nous vous le disons au téléphone.]"
      }
    }
  ]
}
```

Deux règles que je respecte : on ne balise que ce qui est **visible** sur la page, et on ne balise que ce qui est **vrai**. Pas de `AggregateRating` tant que des avis réels ne sont pas collectés et affichés sur le site.

### 4. Titres et méta-descriptions réécrits

| Page | Titre (≤ 60 car.) | Méta-description (≤ 155 car.) |
|------|-------------------|--------------------------------|
| Accueil | Plombier à Lyon — dépannage et urgences \| [ENTREPRISE] | Dépannage, débouchage et installation de plomberie dans les 9 arrondissements de Lyon et la métropole. Devis gratuit. [PRIX À CONFIRMER] |
| Débouchage | Débouchage WC et canalisation à Lyon — à partir de [X] € \| [ENTREPRISE] | Débouchage WC, évier et colonnes dans tout Lyon. Manuel, mécanique ou haute pression. Devis avant travaux, [PRIX À CONFIRMER] € TTC en intervention simple. |
| Urgence | Plombier d'urgence à Lyon — intervention en [X] h \| [ENTREPRISE] | Fuite, WC bouché, eau qui coule : appel au [04 … — À CONFIRMER]. Intervention en [X h — À CONFIRMER], 7j/7 [À CONFIRMER]. |
| Services | Plomberie à Lyon : dépannage, installation, salle de bain \| [ENTREPRISE] | Toutes les prestations de plomberie : fuites, sanitaires, robinetterie, chauffage. Artisan CMA [N° — À CONFIRMER], assuré, dans toute la métropole lyonnaise. |
| Contact | Contact — Plombier à Lyon \| [ENTREPRISE] | Téléphone : [04 … — À CONFIRMER]. Horaires : [HORAIRES — À CONFIRMER]. Lyon et métropole. Réponse rapide à vos demandes de devis. |

Le principe : le titre commence par ce que le client cherche, la description contient un fait exploitable (zone, prix, délai) — pas d'adjectifs.

---

## Un exemple de contenu de page qui répond aux vraies questions

Structure type pour la page « Débouchage » : réponse dans les deux premières phrases, puis les détails, puis le contexte, puis une seule étape suivante. Les fourchettes ci-dessous sont des **références de marché à Lyon en 2025-2026** (débouchage simple 100-180 € TTC, mécanique jusqu'à 250-300 €, hydrocurage 200-600 €, tarif horaire artisan 40-80 € HT avec une majoration de 30 à 50 % sur Lyon) — elles te servent de repère pour m'indiquer **tes** prix réels, que seuls toi et ton grille tarifaire pouvez fournir.

```
## Combien coûte un débouchage à Lyon ?

Un débouchage simple (WC, évier, siphon) est facturé entre [PRIX À CONFIRMER] €
et [PRIX À CONFIRMER] € TTC. Le débouchage mécanique — furet ou spirale — va
jusqu'à [PRIX À CONFIRMER] € quand le bouchon est en profondeur. L'hydrocurage,
qui nécessite un camion avec pompe haute pression, se chiffre entre
[PRIX À CONFIRMER] € et [PRIX À CONFIRMER] € selon l'accès à la canalisation.
Le prix est annoncé au téléphone et confirmé par devis avant que nous n'y
touchions.

## Intervenir dans quel secteur ?

Tous les arrondissements de Lyon, de la presqu'île (2e) aux coteaux (7e),
ainsi que Villeurbanne, Caluire-et-Cuire, Vaulx-en-Velin, Bron, Oullins et
Tassin-la-Dunguin. [LISTE À CONFIRMER]

## En combien de temps pour une urgence ?

[DÉLAI À CONFIRMER]

## Et si ce n'est pas un bouchon ?

Si l'obstruction est solide (gravats, racines), le débouchage simple ne
suffit pas. Dans ce cas nous proposons une inspection caméra
([PRIX À CONFIRMER] €) pour voir exactement où est le problème et éviter de
refaire intervenir deux fois.

Un bouchon qui revient souvent ? Appelez le [04 … — À CONFIRMER] : on regarde
ce qui se passe et on vous dit ce que ça va coûter avant de commencer.
```

---

## La présence hors site — là où ton problème commence vraiment

**1. La fiche Google Business Profile (priorité n° 1).** Procédure :

1. Créer un compte sur `business.google.com` avec l'adresse e-mail du business.
2. « Ajouter votre établissement » : nom exact (identique au site, caractère pour caractère), adresse, téléphone, catégorie principale **Plombier** + catégories secondaires (ex. « Entreprise de travaux de plomberie », « Service de dépannage d'urgence »).
3. Horaires exacts, site web, photos de l'atelier et de chantiers.
4. Vérification : en général une carte postale envoyée à l'adresse (1 à 2 semaines), vidéo ou téléphone possible selon le cas. **C'est pour ça que l'adresse doit être exacte.**
5. Ensuite : répondre aux avis, publier des photos régulièrement, et tenir la fiche à jour.

Règle d'or : nom, adresse et téléphone **identiques caractère pour caractère** entre le site, la fiche Google et tous les annuaires. Les incohérences sont l'une des premières causes d'une entreprise décrite de travers — par Google comme par les assistants.

**2. Les annuaires que lisent les assistants et la recherche :**

- Pages Jaunes (fiche complète, mêmes coordonnées)
- 118000, 360info
- Annuaire de la Chambre de Métiers et de l'Artisanat (CMA) de ton secteur — tu as ta carte pro, la fiche doit y être
- Houzz (référencement fort pour les artisans du bâtiment)
- Plateforme d'avis où tes clients laissent spontanément des avis (Google avant tout)

Je ne crée pas d'avis et je ne recommande aucune incitation aux avis : des avis récents et authentiques, collectés naturellement, c'est ce qui compte.

---

## Le test assistant — à lancer dès que j'ai le nom

Dès que tu me donnes le nom commercial et l'URL, je pose les questions qu'un client poserait, avec plusieurs formulations, et je consigne mot pour mot ce qui revient :

1. « Qui fait du débouchage de canalisations à Lyon ? »
2. « Plombier d'urgence Lyon 6e, WC bouché, qui appeler ? »
3. « [NOM DE L'ENTREPRISE] Lyon » — et je vérifie quels horaires, quelle adresse et quel numéro l'assistant restitue, puis je les compare aux tiens.

Deux choses à savoir avant de lire les résultats : **ces réponses changent d'une exécution à l'autre** et d'un assistant à l'autre. C'est un instantané, pas un classement — je ne calcule aucun score. C'est le troisième type de question (le nom direct) qui rapporte le plus : c'est là qu'une erreur précise — un samedi « fermé » alors que tu ouvres, un numéro périmé — se voit, et ça, ce sont de vrais appels perdus.

---

## Ce dont j'ai besoin de toi (une seule fois, en lot)

Pour remplir les trous et publier les fichiers ci-dessus, six éléments confirmés :

1. **Le nom commercial et l'URL du site** — pour lancer l'exploration complète (robots.txt, HTML brut, schema, pages)
2. **Téléphone, e-mail, adresse** — ceux qui doivent apparaître partout, identiques
3. **Les horaires** — jours, heures, et si tu es ouvert le samedi
4. **Tes vraies fourchettes de prix** — débouchage simple, mécanique, hydrocurage, tarif horaire, inspection caméra
5. **Le numéro de carte pro CMA** tel qu'il doit s'afficher
6. **L'année de création** — et la liste exacte des communes où tu te déplaces (et celles où tu ne vas pas)

Tant qu'une réponse ne revient pas, le texte garde un trou visible (« PRIX À CONFIRMER ») plutôt qu'une devinette. Un prix inventé sur une page en ligne, au nom de ton entreprise, non.

---

## Ce que je ne promets pas

Ces corrections réparent des choses objectivement cassées — une fiche Google absente, probablement des robots bloqués, des faits à structurer. Ce qu'elles ne peuvent pas faire, c'est promettre une position dans Google ou une réponse d'un assistant : personne ne contrôle cela. La visibilité bouge lentement : **rien ne changera d'aspect pendant une trentaine de jours**, alors ne va pas vérifier chaque semaine. Je relance l'audit complet — exploration du site, les mêmes trois questions assistant, cohérence des fiches — **dans 30 jours**, et on compare l'instantané à celui-là.

## Et ensuite

L'audit a posé le diagnostic : ta fiche Google est le premier mur, et le site a tout ce qu'il faut pour être lisible par les machines dès que les fichiers ci-dessus sont en place. L'étape la plus utile maintenant, c'est de mettre le contenu au travail — dis-moi **« fais le contenu »** et on rédige les pages qui répondent aux vraies questions de tes clients (débouchage, urgence, devis) avec les prix que tu confirmes. Et si tu veux voir ce que ton site renvoie en ce moment, **« ma publicité fonctionne-t-elle ? »** ouvre le volet mesure.
