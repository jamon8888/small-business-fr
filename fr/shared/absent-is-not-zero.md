# L'absent n'est pas zéro

La façon la plus commune, de loin, pour ces skills de produire une réponse
fausse et assurée.

Chaque défaut ci-dessous apparaît contre un connecteur réel, pas contre des
fixtures, et la raison est structurelle : **les fixtures sont complets par
construction, et les données réelles sont pleines de trous.** Un trou se lit
comme une bonne nouvelle, à moins que le skill ne soit averti du contraire.

---

## La forme du problème

Un champ revient vide, à zéro, tronqué ou non suivi. Le skill le lit comme un
fait sur l'entreprise, et non comme un fait sur les données. La réponse qui en
sort est propre, assurée, et fausse dans le sens qui cache le problème — le
pire des sens, parce que rien n'a l'air d'avoir besoin d'être vérifié.

| Ce que les données ont fait | Ce que le skill a conclu | Ce qui était vrai |
|---|---|---|
| Rapport de créances tronqué aux 10 premières lignes | Total des créances : 25 907 € | 37 055 €, et la seule dette à 91 jours manquait |
| Synthèse du compte de résultat sans les charges | Zéro charges, marge brute 100 % | 984 591 € de charges dans les lignes en dessous |
| Horodatage d'une réponse daté dans le futur | Prospect le plus chaud du pipeline | Fiche corrompue, aucun contact récent du tout |
| Date d'activité absente sur une opportunité | Opportunité fraîche, pipeline propre | Jamais touchée par personne, jamais |
| Recherche par étiquette via un ID sans résultat | Aucun prospect dans la boîte | 201 demandes réelles sous cette étiquette |
| Suivi de stock désactivé pour une variante | Produit que personne n'achète, jamais de réassort | Café le plus vendu du catalogue |
| Quatre paies antérieures non traitées | Une seule paie à échoir | Quatre périodes où personne n'a été payé |
| Champ de revenus renvoyant `0.0` | L'entreprise ne gagne rien | Le fournisseur de données n'a pas de chiffre pour elle |
| Solde du processeur `available: 0` | Pas d'argent chez ce processeur | 3 071 € en attente, en arrive dans deux jours |

Neuf occurrences, neuf connecteurs différents, une même erreur.

---

## La règle

**Avant de reporter un chiffre, demande-toi ce qui ferait qu'il ait cette
allure si l'entreprise va bien, et ce qui ferait qu'il ait cette allure si les
données sont cassées. Si tu ne sais pas distinguer les deux, dis-le, au lieu
d'en choisir un.**

Concrètement, dans l'ordre de fréquence où cela mord :

1. **Un appel contraint ou paginé décrit sa propre tranche, jamais le tout.**
   Les totaux viennent d'une source non contrainte — une ligne du bilan, un
   comptage complet — ou ils sont étiquetés partiels. Ne présente jamais une
   synthèse top-N comme un total de livres.

2. **Un objet de synthèse est une commodité, pas une source.** Quand un
   payload propose à la fois une synthèse et les lignes dont elle a été
   calculée, totalise les lignes. Plusieurs connecteurs livrent des synthèses
   qui contredisent leurs propres lignes.

3. **Zéro et absent sont des faits différents, et la plupart des API les
   confondent.** Un revenu de `0.0`, une date vide, un comptage `null` —
   décide lequel est plausible. Une entreprise sans revenu est rare ; un
   fournisseur de données sans chiffre est courant. Quand le zéro est
   implausible, lis-le comme inconnu et dis inconnu.

4. **Vide n'est pas frais.** Une fiche sans date d'activité n'a jamais été
   touchée, ce qui est le pire des cas, pas le plus sain. Les comparaisons de
   dates excluent silencieusement les champs vides, si bien que les fiches les
   plus en difficulté sortent de la liste même construite pour les trouver.
   Range l'absent au-dessus de la date la plus ancienne, et nomme-le
   différemment.

5. **Une date postérieure à aujourd'hui est corrompue.** Le score de
   récence la lit comme maximale, si bien que les mauvaises fiches remontent
   en tête. Compare chaque date à aujourd'hui avant de la scorer, et traite
   tout ce qui est dans le futur comme vide.

6. **Un résultat vide et une requête échouée ont la même apparence.**
   Recoupe avant de ne rien signaler : si une recherche par étiquette renvoie
   zéro alors que l'étiquette annonce des messages, c'est la requête qui est
   fausse, pas la boîte. « Aucun résultat » est une affirmation sur
   l'entreprise et mérite le même examen que toute autre.

7. **Deux comptages qui se contredisent sont une trouvaille, pas une erreur
   d'arrondi.** Quand deux endpoints décrivent la même chose et diffèrent d'un
   ordre de grandeur, l'un des deux mesure autre chose. Dis lequel tu as
   utilisé et pourquoi, plutôt que de choisir en silence.

---

## Bien le dire

Le dirigeant n'a pas besoin du mécanisme. Il a besoin de savoir quels chiffres
sont fiables.

> *« Tes livres montrent 37 055 € dus par 20 clients. Un seul compte, Pearl
> Street Bistro, est à 91 jours de retard pour 467 € — c'est la seule dette
> vraiment ancienne. »*

Pas « les créances sont à 25 907 € », qui était vrai de la tranche et faux de
l'entreprise.

> *« Le rapport de stock de Shopify montre bien moins d'unités vendues que son
> rapport de ventes, donc le suivi semble désactivé sur la plupart des
> variantes. J'ai utilisé les chiffres de ventes pour la vélocité et les
> chiffres de stock uniquement pour le stock en main. »*

Une phrase, et le dirigeant sait exactement à quel point faire confiance au
chiffre.

Quand quelque chose ne peut vraiment pas être déterminé, dis-le et arrête-toi.
**Un trou nommé est utile. Un zéro fabriqué est pire que le silence**, parce
que le dirigeant agit dessus — et ces sorties sont transmises à des banques,
des conseils et des comptables.

---

## Occurrences propres à un connecteur

Le détail vit avec le connecteur qui lui appartient :

- `quickbooks-report-traps.md` — objets de synthèse contredisant leurs propres
  lignes
- `gmail-inbox-traps.md` — requêtes par étiquette, bruit de machine et
  identifiants
