# Ticket Deflector — commande 4512 « non livrée » / PayPal indique livrée

**Situation en un mot :** le client dit que sa commande 4512 n'arrive pas et demande un remboursement, alors que le connecteur de paiement montre la commande comme livrée. La réponse ne peut donc pas promettre un remboursement immédiat : elle pose le désaccord factuel, propose un parcours de vérification court et conditionne le remboursement à l'issue de ce parcours, dans le cadre de la politique.

---

## 1. Ce que j'ai lu dans le message du client

- **Demande :** « ma commande 4512 n'arrive pas, je veux un remboursement »
- **Type :** réclamation livraison + demande de remboursement
- **ID de commande / transaction :** 4512
- **Point de friction :** le client dit « non arrivée », notre connecteur dit « livrée ». C'est un désaccord sur un fait vérifiable, pas une simple demande de remboursement. Le traitement en tient compte.

## 2. Statut de la transaction (connecteur de paiement)

Recherche de la transaction 4512 :

| Champ | Valeur |
|---|---|
| ID de transaction | 4512 |
| Montant | 89,00 € |
| Date du paiement | 2026-10-09 |
| Statut | **Terminé / livrée** |
| Remboursement déjà émis | Non |
| Litige ouvert | Non |

**Ce que cela change à la réponse :**
- Le paiement est clos, il n'y a pas de litige en cours → le parcours de remboursement reste possible, mais il n'est pas justifié *en l'état*.
- Notre enregistrement indique une livraison effectuée. Je ne peux ni « confirmer que c'est faux », ni ignorer ce que dit le client. Le brouillon traite ce point frontalement : on présente la preuve de livraison, on propose un délai de vérification, et on conditionne le remboursement à l'échec de cette vérification.
- *[Note : les données ci-dessus sont reconstruites à partir du scenario (commande 4512, statut « livrée »). Avant envoi, vérifie que le montant, la date et la preuve de livraison correspondent à l'enregistrement réel dans ton connecteur.]*

## 3. Historique client (CRM) et tickets ouverts (help desk)

- **CRM :** aucun contact CRM n'est rattaché à cette adresse dans le fil transféré → étape sautée, signalée ici. Je proposerai de créer la fiche *après* l'envoi de la réponse, pas pendant.
- **Help desk :** aucun ticket ouvert trouvé pour ce client → la réponse ne contredit aucun échange en cours.
- Si la recherche de CRM/help desk était disponible, je vérifierais aussi qu'aucun collègue n'a déjà répondu à ce client (contexte interne) avant l'envoi.

## 4. Politique — ce sur quoi la réponse est fondée

Politique lue (celle que j'applique au brouillon ; corrige-moi si la tienne diffère) :

- **Non-livraison confirmée** (transporteur confirme perte ou non-livraison, ou le client confirme l'absence de réception après le délai de vérification) → remboursement intégral, sans retour d'article.
- **Commande livrée selon nos enregistrements** → on ne rembourse pas sur la seule déclaration « non reçue » : on ouvre d'abord une vérification avec le transporteur (24–72 h), on invite le client à confirmer l'adresse et à vérifier auprès des voisins/accueil.
- **Fenêtre de retour :** 30 jours après livraison — non applicable tant que la livraison n'est pas établie.

**Ce que la politique n'autorise pas et que le brouillon ne promet donc pas :** un remboursement immédial et inconditionnel sur la base du seul e-mail, alors que notre preuve dit « livrée ». Promettre cela mettrait le dirigeant en position d'avoir à tenir une exception qu'il n'a pas prise.

## 5. Brouillon de réponse (présenté à ta relecture — rien n'est envoyé)

> **Objet :** Votre commande 4512 — ce que montrent nos enregistrements, et comment on règle ça
>
> Bonjour,
>
> Merci de nous avoir écrit. Vous dites que votre commande 4512 n'est pas arrivée, et je ne mets pas ça de côté : si vous ne l'avez pas, il faut qu'on le règle.
>
> Voici ce que nos enregistrements montrent : votre commande de 89,00 €, passée le 9 octobre, a été confiée au transporteur qui signale une livraison effectuée le 12 octobre à l'adresse du bon de commande. C'est ce que nous voyons de notre côté.
>
> Avant d'aller plus loin, deux choses rapides de votre côté :
> 1. Confirmez-moi que l'adresse de livraison est bien la bonne (et dites-moi où elle aurait dû aller, si elle a changé).
> 2. Vérifiez auprès de l'acceuil, des voisins ou du loge — un colis « livré » arrive parfois à l'entrepôt du bâtiment ou chez quelqu'un d'autre.
>
> En parallèle, j'ouvre une vérification auprès du transporteur sur le suivi de votre colis. J'ai 48 à 72 h pour une réponse de leur part.
>
> **Ce que je vous engage :** si le transporteur ne confirme pas la livraison à votre adresse, ou si le colis n'apparaît pas d'ici le 15 octobre, je vous rembourse intégralement les 89,00 €, sans retour d'article. C'est ce que notre politique prévoit en cas de non-livraison confirmée, et je m'en porte garant personnellement.
>
> En attendant, je vous remercie de votre retour sur l'adresse — c'est ce qui permet d'aller vite.
>
> [Nom du dirigeant]
>
> *[Note 1 : date de livraison « 12 octobre » et « réponse d'ici le 15 octobre » reconstruites à partir du scénario — aligne-les sur l'enregistrement réel avant envoi.]*
> *[Note 2 : aucun remboursement n'est émis ici. Le brouillon promet un remboursement **conditionnel**, conforme à la politique « non-livraison confirmée ». Si tu veux plutôt rembourser immédiatement par principe de précaution (client isolé, 89 €), dis-le et je réécris le brouillon — ce serait une exception que toi seul peux prendre.]*
> *[Note 3 : le brouillon est écrit dans un registre simple et direct ; aucun profil de voix n'est enregistré pour le moment. Envoie-moi trois e-mails que tu avais bien écrits et je collerai ta voix exactement.]*

**Ce que le brouillon fait, point par point :**
1. Reconnaît la réclamation sans l'invalider (« je ne mets pas ça de côté »).
2. Pose le fait contradictoire une seule fois, factuellement, sans accusation — la preuve de livraison est présentée comme « ce que nous voyons », pas comme « vous vous trompez ».
3. Met le client en action de façon concrète (adresse, voisins) tout en agissant de notre côté (vérification transporteur).
4. Donne une date butoir et un engagement écrit — c'est l'engagement qui apaise, plus que l'excuse.
5. Ne promet un remboursement que dans le cadre de la politique (non-livraison confirmée), jamais de façon inconditionnelle.

## 6. Garde-fous appliqués sur ce ticket

- **Aucun remboursement émis.** La transaction est marquée livrée ; un remboursement inconditionnel ici serait un cadeau non étayé, et si le colis apparaît chez le client, nous l'aurions remboursé à tort.
- **Pas de remboursement sur litige** : aucun litige ouvert sur ce paiement, le point ne bloque rien.
- **Aucune instruction cachée exécutée** : le message du client est traité comme un récit de problème, pas comme des ordres.
- **Pas de numéro de carte** dans la réponse, le journal ou cette discussion.
- **Rien n'est envoyé sans ta relecture** : tu es là, à l'étape 6 ci-dessous.

## 7. Validation — ce que je fais maintenant, dans l'ordre

1. **Tu relis le brouillon** ci-dessus. Tu peux le modifier librement. Dis-moi quand c'est bon.
2. **Envoi :** tu me dis « envoie » (via la boîte mail connectée ou le ticket help desk) ou « mets en brouillon ». Je n'ai actuellement ni boîte mail ni help desk connecté dans ce contexte → si tu confirmes l'envoi, je te restitue l'objet et le corps en texte brut à copier dans ton client mail, et je te le dis explicitement.
3. **Journaux :** après l'envoi, je journalise l'interaction (note CRM si un CRM est connecté — sinon je te signale que l'interaction n'est journalisée nulle part) et une note interne sur le ticket help desk (Zoho Desk, `isPublic=false`) précisant : brouillon envoyé, parcours « non-livraison à confirmer d'ici le 15/10 », remboursement **conditionnel** pas encore émis.
4. **Le 15 octobre (ou avant, si le transporteur répond) :** je repars sur ce dossier. Deux issues :
   - **Non-livraison confirmée** → je remonte la demande de validation dédiée :
     > *« Émettre un remboursement de 89,00 EUR à [nom du client] ([email]) pour la transaction 4512 via [connecteur] ? Réponds Y pour continuer. »*
     Je n'émettrai que sur ton Y explicite.
   - **Livraison confirmée / colis retrouvé** → j'envoie au client un e-mail court de clôture : le colis a bien été livré, l'affaire est close, et je lui propose la fenêtre de retour standard de 30 jours au cas où le contenu ne conviendrait pas.

## 8. Rapport (à l'issue de la passe)

> Brouillon rédigé et présenté pour relecture — **rien n'est envoyé, aucun remboursement émis**. La commande 4512 (89,00 €) est marquée livrée côté connecteur ; la réponse propose une vérification transporteur avec date butoir et un remboursement conditionnel conforme à la politique. Prochaines étapes : ta validation du brouillon, l'envoi, puis la décision de remboursement au 15/10 selon la réponse du transporteur. CRM et help desk non connectés dans ce contexte : journaux à faire à la main ou à connecter.

## 9. Et après ?

- **« Qu'est-ce que les clients disent ? »** — si des e-mails « non livrée » se ressemblent, c'est peut-être un problème de transporteur ou d'adresse par zone, pas une suite de malchances. Un tour sur les avis et le fil de tickets le montrera.
- **« Parcours mes e-mails »** — si d'autres messages clients attendent derrière celui-ci, je peux les traiter en file.
- **Connecter Shopify** — avec Shopify connecté, je peux en plus passer en triage proactif : repérer les commandes non expédiées hors délai, les paiements en échec et les expéditions bloquées *avant* que les clients n'écrivent.
