# Profil de voix

**Partagé dans tout le plugin.** La voix d'écriture du dirigeant, apprise une
fois à partir d'échantillons réels et réutilisée par tous les skills qui
rédigent quoi que ce soit en son nom.

**Lis ce fichier avant de rédiger au nom du dirigeant.** Si un profil existe
ci-dessous, utilise-le. Le reconstruire à chaque run gaspille le temps du
dirigeant et fait dériver la voix d'un skill à l'autre, ce que les dirigeants
remarquent immédiatement.

Skills qui lisent ce fichier :

| Skill | Rédige |
|---|---|
| `outreach-composer` | Prospection de prospects et séquences de suivi |
| `speed-to-lead` | Réponses instantanées aux demandes entrantes |
| `invoice-chase` | Relances de factures en retard |
| `review-reputation` | Réponses publiques aux avis et offres de reconquête |
| `inbox-manager` | Réponses et brouillons d'e-mails |
| `social-content-engine` | Légendes et textes de posts |
| `ticket-deflector` | Réponses au service client |
| `hiring-screener` | Réponses aux candidats et refus |
| `inventory-planner` | E-mails fournisseurs et notes d'accompagnement des BC |
| `lead-triage` | Brouillons de suivi |

**Une correction faite ici les corrige tous.** C'est tout l'intérêt du partage
— un dirigeant qui supprime « just following up » une fois ne devrait plus
jamais le voir venir d'aucun skill.

Réfère-toi depuis un SKILL.md par chemin relatif : `../../shared/voice-profile.md`

---

## Comment en construire un

**Sources, par ordre de qualité :**

1. Les e-mails envoyés du dirigeant à des clients et prospects — 15 à 30
   messages. Rien d'autre ne s'en approche.
2. E-mails et notes CRM consignés
3. Son site web, sa newsletter ou ses posts sociaux
4. Trois exemples qu'il colle et sur lesquels il était satisfait

**Quoi extraire.** Sois assez précis pour imiter. « Sympa et professionnel »
est inutile ; ça décrit tous les e-mails d'affaires jamais écrits.

| Trait | Quoi capturer |
|---|---|
| Salutation | La forme exacte. « Hi Dana, » vs « Dana — » vs « Good morning Dana, » |
| Signature | Exacte, y compris si le nom est complet ou prénom seul |
| Longueur des phrases | Moyenne, et s'il écrit long ou coupé |
| Contractions | Écris-il « I'll » ou « I will » |
| Points d'exclamation | Fréquence. Certains dirigeants en mettent un par e-mail, d'autres jamais |
| Directesse | Atteint-il la demande en ligne 2 ou ligne 6 |
| Langage produit | Comment il appelle son propre service, dans ses mots |
| Régionalismes | Formules locales, jargon de métier, tout ce qui est caractéristique |
| Formalité | Prénoms immédiatement, titres, ou ni l'un ni l'autre |
| Interdits | Mots et structures absents de tous les échantillons |

**Les interdits comptent le plus.** Si un dirigeant n'a jamais écrit
« circle back », « reach out to see if » ou « hope this finds you well »,
ces expressions sont des indices immédiats qu'un autre a écrit le message.

---

## Format du profil

```
## Profil de voix — <nom du dirigeant>
Construit :    <date>  ·  Sources : <n> e-mails envoyés, <autres sources>
Mis à jour :   <date> — <ce qui a changé>

Salutation :      <forme exacte>
Signature :       <forme exacte>
Phrases :         <courtes/moyennes/longues>, moyenne <n> mots
Contractions :    <oui/non>
Exclamations :    <jamais | rares | fréquentes>
Moment de la demande : <ligne où la demande tombe typiquement>
L'appelle :       <ce qu'il appelle son propre produit ou service>
Formalité :       <description>

Expressions caractéristiques :
  <expressions qu'il utilise réellement, verbatim>

N'utilise jamais :
  <expressions absentes de tous les échantillons>

Échantillon, verbatim :
  <un court e-mail réel de lui, comme point de référence>
```

---

## Exemple travaillé

```
## Profil de voix — Ray Okonkwo, Okonkwo Mechanical
Construit :    2026-07-27  ·  Sources : 22 e-mails envoyés, site web
Mis à jour :   2026-07-27 — initial

Salutation :      « Hi <first name>, » — toujours le prénom, toujours virgule
Signature :       « Thanks, Ray » — jamais « Best, », jamais nom complet
Phrases :         Courtes. Moyenne 11 mots. Souvent des fragments.
Contractions :    Oui, systématiquement. « I'll », « we've », « don't »
Exclamations :    Rares — 2 sur 22 e-mails, tous deux sur des travaux finis
Moment de la demande : ligne 2 ou 3. Il en vient vite au fait.
L'appelle :       « the work », « the job », « a service plan » — jamais « solutions »
Formalité :       Prénoms immédiatement, pas de titres, pas de registre corporate

Expressions caractéristiques :
  « Happy to swing by »
  « Let me know what works »
  « No rush on this »
  « Straight answer: »

N'utilise jamais :
  « reach out »  ·  « circle back »  ·  « touch base »  ·  « hope this finds you well »
  « I wanted to »  ·  « excited to »  ·  « leverage »  ·  « solutions »
  Toute phrase d'environ plus de 25 mots

Échantillon, verbatim :
  Hi Dana,
  Straight answer: yes, we can cover all six buildings on one plan. It'd
  actually be cheaper than the two you have now.
  Happy to swing by Thursday and walk through it. Let me know what works.
  Thanks, Ray
```

Quiconque lit ce profil peut écrire comme Ray. C'est la barre.

---

## Le garder à jour

**Chaque édition du dirigeant est un signal.** Quand il modifie un brouillon,
demande de quoi la modification était, et consigne-la. Une correction faite
une fois ne devrait jamais se faire deux fois.

Ajoute à « Mis à jour » plutôt que d'écraser, pour que le raisonnement reste
visible :

```
Mis à jour : 2026-08-14 — coupé « Just following up » des suivis. Ray : « ça
         sonne comme si j'insistais. » Remplacé par une raison précise
         à chaque fois.
```

---

## Quand il n'y a pas d'échantillon

Dis-le clairement et demande trois e-mails sur lesquels il était satisfait.
Ne devine pas.

Une voix devinée produit exactement le texte générique que le dirigeant est
venu éviter, et c'est au premier brouillon que la confiance dans ce skill
gagne ou se perd.

---

## Profils

*Aucun profil construit pour l'instant. Le premier sera écrit ici.*
