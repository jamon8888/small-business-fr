# « mes marges Shopify » — ton vendredi à venir

Bonne nouvelle : c'est un candidat parfait. Tu le refais chaque semaine, la séquence est toujours la même, et ça te prend du temps que tu peux mesurer. C'est exactement ce pour quoi un skill nommé existe — et tu peux le déclencher par son nom chaque vendredi, ou le laisser tourner sans toi.

Voici comment on va procéder : je confirme ce que je comprends, je te pose cinq questions, et ensuite je construis.

## Ce que je crois comprendre

```
1. Chaque vendredi, tu exportes tes ventes Shopify (un export de la boutique)
2. Tu rapproches ces ventes de tes coûts d'achat
3. Tu calcules la marge, à la main, dans un tableur
4. À la fin, il y a un résultat que tu regardes (et peut-être que tu partages)
```

C'est ça ? Et les cinq questions ci-dessous, parce que chaque réponse change la façon dont le skill est écrit.

## Les cinq questions

Réponds en pensant au vendredi dernier, concrètement — les détails réels valent mieux que la description d'habitude.

1. **Quel export, exactement ?** Reprends-moi la dernière fois : qu'as-tu ouvert en premier ? Quelle plage de dates exportes-tu (la semaine écoulée ? lundi à dimanche ?), et tu obtiens quoi, un CSV depuis Shopify ?
2. **Où sont tes coûts d'achat ?** Dans quel fichier vivent-ils, et comment trouves-tu aujourd'hui le coût d'un produit donné — y a-t-il déjà une colonne produit qui relie les deux ?
3. **Que met-tu dans la marge ?** Chiffre d'affaires moins coût d'achat, point ? Ou bien tu déduis aussi les frais Shopify, le port, les retours ? C'est une règle du skill, il faut que je la code exactement comme toi.
4. **Qu'existe-t-il à la fin, et qui le voit ?** Un fichier Excel que tu gardes ? Un message que tu envoyes à quelqu'un ? Le skill doit savoir s'il s'arrête sur un fichier interne ou s'il rédige un envoi.
5. **Les deux questions qui comptent le plus :** qu'est-ce qui a mal tourné la dernière fois que ça s'est mal passé (un produit qui paraissait rentable et ne l'était pas ?) — et qu'est-ce que tu ne voudrais **jamais** voir faire tout seul par ce skill ? En bonus : combien de temps ça te prend aujourd'hui, à la main ? C'est le chiffre qu'on te rappellera quand ce sera réglé.

## À quoi ressemblera le skill (brouillon à corriger)

Voici la forme que je vais écrire une fois tes réponses posées — dis-moi ce qui ne va pas plutôt que de deviner :

- **Fixe** : la séquence — exporter les ventes de la semaine, rapprocher des coûts d'achat, calculer la marge par produit, signaler les cas qui dérapent, produire ta sortie habituelle.
- **Variable** : les dates, les produits, les montants, le fichier du jour. Rien de ce qui était vrai le vendredi dernier ne sera codé en dur.
- **Règles** : ce que tes réponses 3 et 5 m'apprendront — les frais à déduire, les seuils sous lesquels tu veux être prévenu.
- **Une seule porte de validation** : si la sortie part vers quelqu'un (un e-mail, un message), le skill s'arrêtera là et te dira combien d'écarts, sur quels produits, pour quel montant, avant de l'envoyer. S'il produit juste un fichier pour toi, il tournera sans demander rien du tout.

Je n'écris pas le `SKILL.md` définitif avant tes réponses — un brouillon bâti sur des hypothèses figerait les mauvaises. Mais cette forme, oui ou non et corrections.

## Le déclencheur

- **Nom** : « **mes marges Shopify** » — ce que tu dirais, exactement, pour le lancer.
- **Horizon** : **chaque vendredi matin**, avant que tu n'aies l'habitude d'ouvrir la boutique. C'est une tâche récurrente, donc elle sera planifiée : tu ne la lanceras même plus, elle arrivera.

## Ensuite, une fois tes réponses posées

1. **Le test** : je le lance sur le cas du vendredi dernier — celui que tu viens de faire à la main — et je te montre les deux sorties côte à côte. S'il retrouve tes mêmes marges et te signale ce que tu avais repéré, tu pourras le laisser tourner sans le vérifier à chaque fois. S'il y a un écart, je corrige le skill et je relance.
2. **L'enregistrement** : je l'ajoute au routeur avec tes formulations (« mes marges Shopify », « le fichier Shopify de la semaine »…) et je fixe la planification du vendredi matin.
3. **Le partage** : s'il doit en produire pour l'équipe, on verra ensemble ce que ça signifie — car un skill qui envoie quelque chose, partagé à quelqu'un qui n'en connaît pas les hypothèses, mérite d'être passé en brouillon.

## Si ça dépasse ce skill

- Si ton export Shopify nécessite un accès qu'on n'a pas encore : « **connecte-moi mon Shopify** ».
- Si la sortie doit nourrir ton tableau de suivi hebdomadaire : « **fais-moi le brief** » ou « **brief du lundi** ».

Réponds aux cinq questions — une phrase par réponse suffit — et j'écris le skill.
