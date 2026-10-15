# Portée du tenant — un magasin de documents connecté n'appartient pas au dirigeant par défaut

**Partagé par tout le plugin.** L'échec que cela évite : `grant-rfp-writer`
n'a pas de connecteur de flux d'opportunités, se rabat sur Google Drive, et le
Drive rattaché à la session appartient à une autre entreprise. Le skill lit les
notes de projet confidentielles d'un autre tenant et les traite comme les
performances passées du dirigeant. Rien dans le connecteur n'indique à qui
appartient ce Drive.

## Les règles

1. **Un magasin de documents (Google Drive, M365, Notion, Dropbox) est une entrée
   pour les fichiers du dirigeant seul.** Avant la première lecture, confirme
   qu'il est le sien : le domaine e-mail ou le nom d'affichage du compte
   connecté correspond au bloc `## Business context` (nom d'entreprise, domaine
   du site), ou le dirigeant a nommé le dossier ou le fichier dans cette
   session. S'il n'y a pas encore de contexte d'entreprise, ou si le compte ne
   correspond pas, arrête-toi et demande en une ligne — « Le Drive connecté ici
   ressemble à <compte> ; est-ce le tien, ou dois-je utiliser un dépôt ? » — et
   ne lis rien avant la réponse.
2. **Cherche par nom, ne parcours jamais.** Toute requête adressée à un magasin
   de documents porte le nom de l'entreprise, le nom du programme ou du projet,
   ou le nom exact du fichier donné par le dirigeant. « Fichiers récents » et
   les listes de dossiers sans périmètre ne sont jamais une voie de découverte.
3. **Un connecteur de données manquant ne se rabat jamais sur un magasin de
   documents.** Aucun flux d'opportunités, aucun CRM, aucun grand livre signifie
   : recherche web là où une source publique existe, un dépôt, ou une question au
   dirigeant. Jamais « regarde dans Drive si tu trouves un truc approchant ».
4. **Tout ce qui vient d'un magasin non concordant est écarté, pas résumé.** Si
   une lecture a déjà eu lieu avant que la non-concordance soit remarquée, dis-le,
   retire-le du jeu de travail, et n'en reporte rien dans un livrable.

## Les skills que cela régit en premier

`grant-rfp-writer` (soumissions passées depuis Drive ou M365). Les mêmes
quatre règles sont liées à la première lecture dans `proposal-builder`,
`contract-review`, `job-post-builder`, `hiring-screener`, `inbox-manager`,
`speed-to-lead`, `outreach-composer` et `invoice-chase`. Une boîte mail est un
magasin de documents à cet effet : une boîte Gmail ou Microsoft 365 connectée
n'est celle du dirigeant qu'une fois son adresse concordant avec le contexte
d'entreprise, ou que le dirigeant l'a nommée.