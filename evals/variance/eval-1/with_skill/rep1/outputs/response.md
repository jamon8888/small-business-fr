# Plan de relance — au 15 octobre 2026

Trois lignes à traiter, **EUR 16 440,00 TTC** au total. Les chiffres ci-dessous sont ceux que tu m'as donnés : je n'ai lu aucun document, aucun outil de comptabilité n'est branché dans cette session.

| Client | Ancienneté | Montant TTC | Niveau | Contenu légal |
|---|---|---|---|---|
| Menuiserie Bertrand | 47 j | EUR 12 400,00 | **3** (J+31 → J+60) | Ferme + pénalités + indemnité de 40 € |
| Atelier Vert | 22 j | EUR 3 150,00 | **2** (J+8 → J+30) | Ferme, rappel des conditions + pénalités |
| Cabinet Leroux | 9 j | EUR 890,00 | **2** (J+8 → J+30) | Ferme, rappel des conditions + pénalités |

Menuiserie Bertrand Concentre à lui seul **75 % de l'encours** de la liste. C'est par là que ça commence — mais pas tout de suite, voir ci-dessous.

Deux précisions de méthode avant le plan, parce qu'elles changent le contenu des textes :

- **Le niveau et le ton sont deux choses différentes.** Le niveau décide de ce que la relance doit contenir légalement (pénalités, indemnité). Le ton, lui, vient de l'historique de règlement du client. Avec zéro historique de paiement de ta part, le score par défaut est « payeur irrégulier » et le ton ressort **neutre et factuel** sur les trois. Donne-moi 3 factures réglées par client et je recale : bon payeur → cordial ; plus de la moitié des factures payées en retard → ferme, avec une date d'échéance à énoncer.
- **Pas de mise en demeure.** À 47 jours, Menuiserie Bertrand est au niveau 3, pas au niveau 4 — la mise en demeure se prépare au-delà de 60 jours, et seulement si tu la demandes. Si rien n'a bougé d'ici deux semaines, on en reparle.

---

## Par quoi commencer

**1. D'abord le contrôle « payé dans les 14 derniers jours ».** C'est la seule vraie urgence, et c'est avant la rédaction, pas après. Un client qui a payé vendredi et qui reçoit une relance lundi est le seul échec vraiment destructeur de ce travail — embarrassant, et ça retombe précisément sur ceux qui paient bien. Je vérifie PayPal (fenêtre 7 jours), Stripe, Square et Shopify (14 jours) avant toute envoi. Là je ne peux rien : aucun prestataire de paiement n'est connecté.

**2. Ensuite, le contrôle d'encours sur Menuiserie Bertrand.** À EUR 12 400,00 et 47 jours, il faut savoir avant de rédiger :
- son **plafond d'encours** et son encours actuel (factures ouvertes + commandes confirmées non facturées) ;
- si sa créance est **couverte par l'assurance-crédit** ;
- s'il apparaît au **BODACC**. Si oui, il **sort du circuit de relance courant** : ce n'est plus un email de relance, c'est une déclaration de créance et une éventuelle revendication au titre de la réserve de propriété, avec un délai court à tenir. On le traite à part, en urgence.

**3. Puis les données qui me manquent** (voir section suivante), et seulement ensuite je finalise.

**4. Ordre d'envoi une fois les contrôles passés :** Bertrand d'abord, puis Atelier Vert, puis Cabinet Leroux. Un par un, et tu valides chaque brouillon avant qu'il parte. Jamais de lot groupé sans ton accord.

Sur Leroux : 9 jours, c'est tout jeune et le montant est faible. Tu peux sans doute le laisser mûrir une semaine de plus sans coût — la relance partira plus ferme et sans qu'il ait l'impression d'être harcelé pour EUR 890,00.

---

## Ce qui me manque avant d'envoyer

Rien de tout ça n'est dans ce que tu m'as passé, et chaque relance en a besoin :

- **Le numéro de facture** et **la date d'échéance** de chacune des trois. J'ai **présumé** les échéances à partir de l'ancienneté que tu as donnée (29 août, 23 septembre, 6 octobre) — ce sont des dates calculées, pas vos dates de facture. Confirme-les, et donne-moi les numéros.
- **Le grand livre** qui tient les factures : MYOB, NetSuite, QuickBooks, Xero ou Zoho Books. Dis-moi lequel est branché et je m'y branche ; si aucun ne l'est, un export CSV de tes créances clients (`num_facture`, `client`, `date_echeance`, `montant_ttc`, `montant_paye`) me suffit pour continuer.
- **Les 4 derniers caractères de ton IBAN** — obligatoire dans chaque relance.
- **Ton taux de pénalités de retard**, celui de tes conditions de règlement. Je ne l'ai pas en tête et je ne vais pas te l'avancer de mémoire : les pénalités se calculent sur `montant TTC × taux × jours / 365`, et je te fais le montant exact dès que tu me le donnes.
- **Les conditions d'escompte**, si tu en as. Si tu n'en as pas, dis-le et je supprime la ligne.
- **L'adresse email** de chaque client.

---

## Les trois brouillons

Ton neutre par défaut, un seul appel à l'action par email, vouvoiement. Les `[ ]` sont à compléter avant envoi.

### 1. Menuiserie Bertrand — niveau 3, 47 jours

> **Objet :** Relance : facture n° [n°] — EUR 12 400,00 échue
>
> Bonjour [Prénom, Nom],
>
> La facture n° [n°] d'un montant de EUR 12 400,00 TTC était échue le 29 août 2026, soit 47 jours de retard à ce jour.
>
> À ce jour, je n'ai trace d'aucun règlement sur cette facture. Conformément à nos conditions de règlement, des pénalités de retard au taux de [taux] % s'appliquent depuis la date d'échéance, auxquelles s'ajoute une indemnité forfaitaire de recouvrement de EUR 40,00.
>
> Le règlement est attendu par virement sur notre compte dont l'IBAN se termine par [•••• 0000].
>
> [Si tu as des conditions d'escompte : *Un escompte de [x] % est applicable pour tout règlement effectué avant le [date].*]
>
> Bien cordialement,
> [Prénom Nom]

*Si son historique de paiement confirme des retards répétés, ajoute une seule ligne : « Merci de régler avant le [date]. » C'est la seule différence entre un ton neutre et un ton ferme.*

### 2. Atelier Vert — niveau 2, 22 jours

> **Objet :** Relance : facture n° [n°] — EUR 3 150,00 échue
>
> Bonjour [Prénom, Nom],
>
> La facture n° [n°] d'un montant de EUR 3 150,00 TTC était échue le 23 septembre 2026, soit 22 jours de retard à ce jour.
>
> Nos conditions de règlement prévoient des pénalités de retard au taux de [taux] %, calculées depuis la date d'échéance. Vous pouvez régler par virement sur notre compte dont l'IBAN se termine par [•••• 0000].
>
> Bien cordialement,
> [Prénom Nom]

### 3. Cabinet Leroux — niveau 2, 9 jours

> **Objet :** Relance : facture n° [n°] — EUR 890,00 échue
>
> Bonjour [Prénom, Nom],
>
> La facture n° [n°] d'un montant de EUR 890,00 TTC était échue le 6 octobre 2026, soit 9 jours de retard à ce jour.
>
> Nos conditions de règlement prévoient des pénalités de retard au taux de [taux] %, calculées depuis la date d'échéance. Vous pouvez régler par virement sur notre compte dont l'IBAN se termine par [•••• 0000].
>
> Bien cordialement,
> [Prénom Nom]

---

## Deux remarques pour finir

**Je n'ai écrit qu'un brouillon par client, pas les trois niveaux.** Le geste type serait de te proposer « rappel cordial » / « ferme » / « mise en demeure » pour chaque facture. Je ne l'ai pas fait : envoyer un rappel cordial à quelqu'un 47 jours en retard n'a pas de sens, et le ton doit venir de son historique, pas du niveau d'ancienneté. Si tu veux une version plus douce de Bertrand — quelques lignes d'accroche avant les pénalités — dis-le, je te l'écris. Mais c'est un choix à faire, pas une escalade automatique.

**Il n'existe pas encore de profil de voix pour toi.** C'est ce qui fait qu'une relance bien fondée sera quand même réécrite à la main, parce qu'elle ne sonnera pas comme toi. Trois emails que tu as envoyés à des clients et qui te plaisaient, et je le construis une fois pour toutes.

---

### Base légale

Pénalités de retard et indemnité forfaitaire de 40 € : C. com. L441-10 et D441-5. Délais de paiement : C. com. L441-10 et L443-1.

> **Base légale** — Conformément à nos conditions de règlement, des pénalités de retard au taux de [taux] % s'appliquent depuis la date d'échéance. S'y ajoute une **indemnité forfaitaire de recouvrement de 40 €** due de plein droit en cas de retard de paiement (C. com. L441-10 et D441-5). Je ne chiffre pas le montant total tant que tu ne m'as pas donné ton taux.

---

**Rien n'a été envoyé.** Les trois textes ci-dessus sont des brouillons en attente de ta validation. Je ne dispatcherai le premier qu'après ton accord explicite, et un par un.

*Si la même facture apparaît dans deux systèmes — grand livre et prestataire de paiement — je n'envoie qu'une seule relance et je te le signale.*