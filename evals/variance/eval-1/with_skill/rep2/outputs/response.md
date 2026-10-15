# Plan de relance — 3 clients, 16 440 € TTC

*Chiffres repris tels que vous me les avez donnés. Référence temporelle : 15 octobre 2026. Aucun document comptable n'est connecté à cette session — je le précise parce que ça change la première étape du plan.*

---

## Par quoi je commence

Par **Menuiserie Bertrand** — mais pas par son email. La première chose à faire, c'est de **lire vos créances au grand livre** avant de rédiger quoi que ce soit.

La raison est simple et c'est le seul vrai risque de la journée : le seul échec vraiment destructeur, c'est d'envoyer une relance à un client qui a payé lundi et dont le virement n'est pas encore rapproché. Ça tombe précisément sur vos bons payeurs, et c'est ce qu'ils racontent aux autres. Sur 12 400 €, c'est le genre de message qui vous coûte un client.

Donc : **étape 0 = le contrôle « payé dans les 14 derniers jours »**, puis Bertrand, puis le reste. Le détail de chaque étape est plus bas.

---

## 1. Le classement

| Client | Retard | Montant TTC | Part de l'encours | Échéance reconstituée | Niveau |
|---|---|---|---|---|---|
| Menuiserie Bertrand | 47 j | 12 400 € | **75,4 %** | 29 août 2026 | **3** — ferme + pénalités + indemnité 40 € |
| Atelier Vert | 22 j | 3 150 € | 19,2 % | 23 septembre 2026 | **2** — ferme, conditions + pénalités |
| Cabinet Leroux | 9 j | 890 € | 5,4 % | 6 octobre 2026 | **2** — ferme, conditions + pénalités |
| **Total** | | **16 440 €** | 100 % | | |

Les dates d'échéance sont **reconstituées** à partir des retards que vous m'avez donnés — elles doivent être confirmées sur les factures avant envoi, l'ancienneté fait foi sur le grand livre, pas sur un souvenir.

**Deux points sur ce tableau :**

- **Bertrand n'est pas en mise en demeure.** Le niveau 4 se déclenche au-delà de 60 jours. À 47 jours, il est au niveau 3, et une mise en demeure ne se rédige que si vous la demandez explicitement. Vous ne l'avez pas demandée, je ne la rédige pas. Il reste 13 jours avant le seuil.
- **Son poids décide de l'ordre, pas son ancienneté.** À lui seul, Bertrand pèse 75 % de l'encours. Atelier Vert et Leroux peuvent attendre 48 h sans coût ; pas lui.

---

## 2. Étape 0 — le contrôle bloquant

Avant la moindre rédaction, sur **les trois** clients :

| Vérification | Fenêtre | Résultat attendu |
|---|---|---|
| Règlements PayPal | 7 jours (3 si limitation de débit) | |
| Règlements Stripe / Square / Shopify | 14 jours | |
| Rapprochement avec le grand livre | sur la période | |

Rapprochement sur l'email en priorité ; à défaut sur le nom, et dans ce cas je le marque « rapprochement par nom seulement — à vérifier ».

Si l'un des trois affiche un règlement récent, le client passe en **« possiblement payé — à vérifier »** et **je ne rédige rien pour lui** jusqu'à ce que le rapprochement soit fait.

Trois points de vigilance sur ce contrôle :

- **Le grand livre seul ne suffit pas.** Un règlement par chèque ou par virement n'apparaît pas chez PayPal, et inversement. Il faut croiser les deux.
- **Même facture dans deux systèmes ?** Si Stripe et le grand livre portent la même facture, ça ne fait qu'une relance, pas deux. Rapprochement sur le numéro de facture, sinon sur montant + date d'échéance.
- **Comptes internes et de test.** Certains paramétrages font apparaître vos propres comptes dans les créances clients. J'écarte les clients dont l'email est sur votre domaine, et je vous signale tout nom contenant « Test », « Internal » ou « Demo ».

---

## 3. Les contrôles avant envoi

| # | Contrôle | À faire quoi |
|---|---|---|
| 1 | **Encours / plafond** | Je n'ai pas vos plafonds. Si Bertrand est proche du sien, ce n'est plus une relance mais une décision de crédit → `credit-desk`. À 12 400 €, c'est à vérifier avant l'envoi, pas après. |
| 2 | **Assurance-crédit** | Si `credit_insured = oui`, confirmer que la créance est bien couverte. |
| 3 | **Procédure collective** | Recherche BODACC sur les trois. Si l'un apparaît en procédure collective, il **sort du circuit de relance courant** et part vers `credit-desk`. Sur un client à 47 jours, c'est le contrôle le plus important du lot. |
| 4 | **Regroupement** | Une seule relance par client. Si « 12 400 € » couvre plusieurs factures, ça part dans **un seul email** avec la liste des numéros et le total — jamais deux emails au même destinataire dans le même lot. |
| 5 | **Ton** | Vouvoiement, formules françaises. |
| 6 | **Langue** | Français. |

---

## 4. L'ordre que je propose

1. **Lire les créances au grand livre** — balance âgée, numéros de facture, dates d'échéance, conditions de règlement, plafond d'encours, flag assurance-crédit.
2. **Lancer le contrôle « payé dans les 14 derniers jours »** sur les trois clients, toutes sources connectées.
3. **Écarter** tout client payé ou en procédure collective, et me le signaler nommément.
4. **Fixer le ton de chacun** à partir de son historique de règlement sur 12 mois (voir §6).
5. **Rédiger les trois brouillons**, un par client, avec les mentions légales obligatoires.
6. **Vous les présenter un par un**, dans l'ordre ci-dessous. Vous validez, j'envoie le premier, on passe au suivant. Aucun envoi groupé sans votre accord.

**Ordre d'envoi :** Bertrand → Atelier Vert → Leroux.

Bertrand en premier parce que c'est 75 % de la somme en jeu et qu'il est le seul à se rapprocher d'un changement de régime juridique de la créance. Leroux en dernier : à 9 jours et 890 €, c'est une relance de fait, pas une vraie pression — l'envoyer trop tôt brouille le message.

---

## 5. Les trois brouillons

> **Ton retenu : neutre, professionnel.** Raison : je n'ai pas votre historique de règlement, donc aucun score. Le défaut en l'absence d'historique est `occasionally-late` → ton neutre, sans formule de politesse excessive, sans reproche. J'ai laissé en clair ce qui change si le score réel est `repeat-late` (voir §6).
>
> **Un seul appel à l'action par email.** Comme les coordonnées bancaires (IBAN, 4 derniers caractères) sont une mention obligatoire, c'est l'IBAN qui fait l'appel. Si l'une de ces factures dispose d'une page de règlement hébergée, le lien la remplace et l'IBAN disparaît.

---

### 1. Menuiserie Bertrand — 12 400 € TTC, 47 jours

**Objet :** `Relance : factures n° […] et […] — 12 400 € échues`

> Bonjour [Prénom],
>
> La facture n° […] d'un montant de 12 400 € TTC était échue le 29 août 2026, soit 47 jours de retard.
>
> *(S'il y a plusieurs factures échues : la facture n° […] du [date] pour […] € et la facture n° […] du [date] pour […] €, soit un total de 12 400 € TTC échu, la plus ancienne depuis le 29 août 2026.)*
>
> Nos conditions de règlement prévoient des pénalités de retard de […] € ainsi qu'une indemnité forfaitaire de 40 € pour frais de recouvrement, qui s'ajoutent au montant ci-dessus. Le détail figure sur la facture.
>
> Pour régler, merci de nous adresser un virement sur le compte […], IBAN se terminant par […].
>
> Si un élément de cette facture vous semble inexact, répondez à ce message et je le vérifie immédiatement.
>
> Cordialement,
> [Votre nom]

**À modifier si le score est `repeat-late` :** objet → `Échéance dépassée : factures n° […] — 12 400 € (47 jours de retard)`, et ajout d'une phrase d'échéance unique — « Merci de régler avant le 29 octobre 2026. »

**Point d'attention :** si vous faites un lien de paiement plutôt qu'un virement, le montant du lien doit être de **12 400 € + pénalités + 40 €**, pas 12 400 €. Une relance qui envoie le client sur une page de règlement au sous-montant est un appel à ne pas rater.

---

### 2. Atelier Vert — 3 150 € TTC, 22 jours

**Objet :** `Relance : facture n° […] — 3 150 € échue`

> Bonjour [Prénom],
>
> La facture n° […] d'un montant de 3 150 € TTC était échue le 23 septembre 2026, soit 22 jours de retard.
>
> Nos conditions de règlement prévoient des pénalités de retard de […] € ainsi qu'une indemnité forfaitaire de 40 € pour frais de recouvrement, qui s'ajoutent au montant ci-dessus. Le détail figure sur la facture.
>
> Pour régler, merci de nous adresser un virement sur le compte […], IBAN se terminant par […].
>
> Si un élément de cette facture vous semble inexact, répondez à ce message et je le vérifie immédiatement.
>
> Cordialement,
> [Votre nom]

**À modifier si le score est `repeat-late` :** objet → `Échéance dépassée : facture n° […] — 3 150 € (22 jours de retard)`, plus la même phrase d'échéance.

---

### 3. Cabinet Leroux — 890 € TTC, 9 jours

**Objet :** `Relance : facture n° […] — 890 € échue`

> Bonjour [Prénom],
>
> La facture n° […] d'un montant de 890 € TTC était échue le 6 octobre 2026, soit 9 jours de retard.
>
> Nos conditions de règlement prévoient des pénalités de retard de […] € ainsi qu'une indemnité forfaitaire de 40 € pour frais de recouvrement, qui s'ajoutent au montant ci-dessus. Le détail figure sur la facture.
>
> Pour régler, merci de nous adresser un virement sur le compte […], IBAN se terminant par […].
>
> Si un élément de cette facture vous semble inexact, répondez à ce message et je le vérifie immédiatement.
>
> Cordialement,
> [Votre nom]

**À modifier si le score est `good-payer` :** objet → `Petit rappel : facture n° […] — 890 €`, et ajout d'une phrase de reconnaissance (« Je sais que l'agenda se charge… ») plus la porte de sortie « si le paiement est déjà en route, merci de ne pas tenir compte de ce message ».

---

### Sur les mentions légales

- **Pénalités** : taux de 3 × le taux d'intérêt légal (C. com. L441-10, D441-5). Je laisse le montant en `[…]` plutôt que de le calculer à l'aveugle — il dépend du taux applicable à la date de la facture, et un taux contractuel supérieur à 3 × le taux légal doit être ramené à ce plafond. Avec vos trois échéances et vos conditions de règlement, je le calcule juste une fois les factures confirmées.
- **Indemnité de 40 €** : due de plein droit en cas de retard, mention obligatoire.
- **Escompte** : absent des trois brouillons faute de savoir s'il s'applique. S'il existe, il doit figurer sur la facture — dites-le moi et je l'ajoute.
- Montants en euros TTC ; l'anti-hasard veut que je précise que les 40 € sont hors taxes et que la TVA de la facture s'y applique.

---

## 6. Le ton : ce que le grand livre décidera

Je n'ai pas votre historique de règlement, donc je n'ai posé aucun score et j'ai écrit en neutre par défaut. C'est le seul élément qui pourrait faire passer un brouillon en cordial ou en ferme, et ça change le texte plus que tout le reste. Sur 12 mois, avec au moins 3 factures au dossier :

| Score | Critère | Ton qui en découle |
|---|---|---|
| `good-payer` | payé à la date ou en avance sur ≥ 75 % des factures | cordial — présume un oubli |
| `occasionally-late` | en retard sur 25 à 50 %, ou moins de 3 factures à l'historique | neutre — les faits, sans jugement |
| `repeat-late` | en retard sur plus de 50 % | ferme — une échéance, sans accusation |

Deux détails qui comptent : « dans les délais » veut dire **règlement reçu au plus tard à la date d'échéance**. Et c'est le score du **client** qui commande le ton, pas celui de la facture la plus échue.

Sur Bertrand, un seul point révélateur suffit : **combien de fois sur les cinq dernières factures a-t-il payé en retard ?** Si c'est trois ou plus, sa relance passe en ferme avec une échéance au 29 octobre, et là l'encours justifie qu'on en parle aussi à votre assurance-crédit.

---

## 7. Le registre

Il n'existe pas encore de profil de registre dans votre dossier, et les trois brouillons ci-dessus sont écrits dans un français neutre standard. **Je ne devine pas votre voix** — une relance correctement ferme mais qui ne sonne pas comme vous sera réécrite à la main, et c'est exactement le résultat que ce travail sert à éviter.

Si vous me collez **trois emails que vous avez envoyés etDont vous êtes satisfait**, je construis le profil une fois pour toutes et les trois messages seront repris à votre ton : votre formule d'appel, votre signature, votre longueur de phrase, et surtout vos expressions habituelles — et les mots que vous n'utilisez jamais.

---

## Ce qu'il me manque pour passer à l'envoi

1. **La source des créances** — un grand livre connecté, ou à défaut un export CSV : numéro de facture, date d'échéance, montant, contact, conditions de règlement.
2. **Précision sur « 12 400 € »** : une facture ou un cumul ? Même question pour les deux autres.
3. **Les 4 derniers caractères de l'IBAN**, ou votre confirmation qu'il vaut mieux un lien de paiement.
4. **Les emails des trois contacts** et le prénom d'ouverture de chacun.
5. **Les plafonds d'encours** et le flag assurance-crédit des trois clients.
6. **Le taux de pénalité de retard** de vos factures, ou votre confirmation que j'applique 3 × le taux d'intérêt légal.
7. **Trois emails de vous** pour le registre.

---

## Ce qui n'a pas été fait

Rien n'a été envoyé, aucun brouillon n'a été mis en file dans un client de courrier, aucun outil n'a été appelé. Les trois textes ci-dessus sont des brouillons en attente de votre validation. Aucune relance ne partira sans votre accord, et par lot — une par une.

*Référence juridique : les montants de pénalités et d'indemnité sont à faire confirmer par votre expert-comptable avant publication (base vérifiée au 14 octobre 2026, C. com. L441-10 et D441-5). La procédure collective reste le point le plus sensible à vérifier sur Bertrand avant tout envoi.*