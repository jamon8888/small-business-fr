# Automatiser vos marges Shopify le vendredi : créer le skill `marges-vendredi`

Bonne nouvelle : ce que vous faites chaque vendredi s'automatise en un skill bien nommé. L'idée d'un skill, c'est de transformer une procédure que vous répétez en un "reflexe" que l'agent exécute de bout en bout quand vous le lui demandez. Concrètement, vous créerez un dossier `marges-vendredi` qui contient :

1. **`SKILL.md`** — le cœur du skill. Un fichier texte avec un en-tête (frontmatter) qui le déclare :

```markdown
---
name: marges-vendredi
description: Exporte les ventes Shopify de la semaine et calcule les marges par produit. À utiliser le vendredi pour le point hebdomadaire sur la rentabilité.
---

## Ce que le skill fait
1. Récupère les commandes Shopify de la semaine écoulée (depuis la dernière exécution).
2. Join avec les coûts d'achat des produits (fichier `couts.csv`).
3. Calcule le CA, le coût des marchandises et la marge brute par produit et au total.
4. Écris le rapport dans `rapports/marges-AAAA-MM-JJ.md` (CA, marge brute, taux de marge, top 5 produits rentables, alertes sur les produits à marge négative).

## Règles
- N'invente jamais un coût manquant : liste les produits concernés en fin de rapport.
- Si l'API Shopify est inaccessible, signale-le et n'écris pas de rapport.
```

Le `description` est crucial : c'est ce qui permet à l'agent de savoir *quand* utiliser le skill. Il faut y décrire la tâche en langage naturel ("chaque vendredi", "marges", "Shopify") pour que le skill se déclenche tout seul quand vous dites "fais le point des marges de la semaine".

2. **`couts.csv`** — votre référentiel des coûts d'achat (colongne : identifiant Shopify du produit, titre, coût unitaire). C'est la donnée qui vous est propre et que l'agent ne peut pas deviner.

3. **`scripts/rapport.py`** (ou `.mjs`) — un petit script qui fait le travail : appel à l'API Admin Shopify (token `SHOPIFY_ADMIN_TOKEN` en variable d'environnement) pour lister les commandes de la période, calcul, et génération du fichier Markdown. Le SKILL.md indique à l'agent d'exécuter ce script plutôt que de réinventer la logique à chaque fois.

4. **`rapports/`** — le dossier de sortie, où chaque vendredi le rapport tombe, daté, prêt à vous lire en deux minutes.

## Les 4 étapes pour la mise en place

1. **Préparez vos coûts** : exportez une fois vos coûts d'achat dans `couts.csv`. C'est la seule donnée qui ne sort pas de Shopify.
2. **Créez le skill** : placez le dossier `marges-vendredi` dans le répertoire des skills de votre outil d'agent (par exemple `~/.config/opencode/skills/` pour OpenCode, ou l'équivalent de votre assistant). Demandez à l'agent d'écrire le script : *"Crée le skill marges-vendredi avec SKILL.md, le script d'extraction Shopify et le template de rapport comme décrit ci-dessus."*
3. **Testez une fois, manuellement** : dites "utilise le skill marges-vendredi". Vérifiez le rapport contre vos calculs manuels de la semaine (c'est votre garantie de justesse avant de vous en reposer dessus).
4. **Activez le déclencheur hebdomadaire** : soit vous lancez le skill chaque vendredi en une phrase ("fais les marges de la semaine"), soit vous programmez un rappel automatique — une tâche planifiée (cron/Task Scheduler) qui exécute l'agent avec cette instruction le vendredi matin. Le vendredi devient alors un simple moment de lecture du rapport.

## Ce que vous y gagnez

- **Fini le calcul à la main** : extraction, join, marges, rapport — tout en une phrase.
- **Traçabilité** : un rapport daté chaque semaine, comparable d'une semaine à l'autre.
- **Détection des problèmes** : les produits à marge négative ou le taux de marge en baisse se voient directement dans le rapport, au lieu de rester noyés dans l'export Excel.

## À surveiller

- **Toujours une passe de validation humaine** : le skill calcule, vous décidez (réassort, prix).
- **Gardez le token Shopify secret** : en variable d'environnement, jamais écrit dans le SKILL.md.
- **Mettez à jour `couts.csv`** quand vos coûts changent (fournisseur, change) : c'est votre unique point de maintenance.

En une après-midi d'installation, vous transformez une corvée de 30 minutes chaque vendredi en 2 minutes de lecture.
