# Faire arriver vos données Sage 100 dans le plugin, sans connecteur dédié

Bonne nouvelle : l'absence de connecteur Sage 100 n'est pas un blocage. Sage 100 est une application poste de travail classique, et elle expose ses données de plusieurs manières. Voici les pistes, classées de la plus simple à la plus robuste, avec un chemin recommandé.

## 1. L'export standard (le point de départ)

Sage 100 Comptabilité permet d'exporter ses données au format **CSV / Excel** :

- **Grand livre**, **balance**, **balance âgée** : menus *Éditions / Rapports → Bilans et états financiers*, puis impression vers Excel/CSV.
- **Journal des écritures** : *Éditions → Journaux*, export Excel.
- **États financiers** (bilan, compte de résultat) : même chemin, au format Excel.

**Procédure mensuelle type :**
1. À la clôture du mois, lancez l'édition de la **balance** et du **compte de résultat** (format Excel).
2. Renommez le fichier selon une convention fixe, par ex. `Sage100_2026-10_balance.xlsx`.
3. Importez ce fichier dans le plugin (fonction d'import manuel).

**Points de vigilance :**
- Validez avec votre comptable quels exports exacts le plugin doit consommer (balance ? comptes synthétiques ? écritures en détail ?). C'est cette décision qui détermine la qualité de ce que le plugin affichera.
- Conservez la **même structure** à chaque mois : mêmes colonnes, mêmes libellés. C'est ce qui rend l'import fiable d'un mois sur l'autre.
- Exportez en **UTF-8 avec séparateur ;** (point-virgule) pour les CSV, afin d'éviter les problèmes d'encodage des accents.

## 2. Automatiser l'export mensuel (si le manuel vous pèse)

Si vous faites ce travail chaque mois, deux options :

- **Demander à votre éditeur/prestataire Sage** si une édition peut être planifiée automatiquement (certaines installations Sage 100 sur réseau le permettent via des tâches planifiées sur le poste de travail du comptable, qui génère le fichier dans un dossier réseau).
- **Un petit script** sur le poste qui tourne Sage 100 (sous Windows) qui lance l'édition et dépose le fichier dans un dossier que le plugin peut lire. C'est une prestation simple pour un intégrateur Sage, typiquement quelques heures de travail.

⚠️ **Ne touchez pas à la base de données Sage directement.** Sage 100 stocke ses données dans un format propriétaire (base locale ou SQL Server selon la version). Y lire « en dur » fragilise la tenue comptable et casse la garantie. La porte d'entrée propre, c'est toujours les éditions/exports officiels.

## 3. L'API Sage (à terme, pour un flux propre)

Sage propose des connecteurs et des API (notamment pour l'écosystème Sage, via des passerelles type **Sage Connector** ou des interfaces EDI/API selon les produits). Le point important pour vous :

- L'éligibilité dépend de votre **version exacte de Sage 100** et de votre **contrat de maintenance**.
- La bonne question à poser à votre **prestataire Sage local** : « quelle est la solution officielle pour extraire mensuellement la balance et le compte de résultat de ma version de Sage 100 vers un outil tiers ? » Ils ont les références exactes et sauront vous dire si c'est faisable proprement sur votre installation.

C'est l'option la plus élégante, mais souvent plus coûteuse et plus lente à mettre en place. Commencez par l'export standard.

## 4. Ce que je vous recommande concrètement

1. **Cette semaine** : identifiez les 2 à 3 exports exacts dont le plugin a besoin (balance mensuelle, compte de résultat, et éventuellement les dettes/creances clients-fournisseurs).
2. **À la prochaine clôture mensuelle** : faites le premier export manuel, importez-le dans le plugin, et vérifiez que les chiffres s'affichent correctement.
3. **Avec votre comptable/prestataire Sage** : posez la question de l'automatisation (édition planifiée ou script) pour enlever le geste manuel, et demandez s'il existe une interface officielle sur votre version.

En une journée de préparation, vous pouvez avoir un flux mensuel fiable, entièrement manuel si nécessaire. L'automatisation est une amélioration, pas un prérequis.

Dites-moi quels sont les chiffres clés que le plugin doit afficher (trésorerie, CA, marge, encours…) et je vous prépare la liste exacte des exports Sage 100 à produire chaque mois.
