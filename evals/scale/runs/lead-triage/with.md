# Lead « merci de me rappeler » — qualification et moment d'appel

## 0. Où on en est, en une ligne

HubSpot n'est pas connecté dans cette session — je le dis clairement plutôt que de faire semblant : **voie « Sans HubSpot ? »**. Colle-moi un export CSV ou même une liste approximative (nom, entreprise, email, date de création, dernière activité, notes) et je renoterai à l'identique. En attendant, je qualifie ce lead sur ce que le message lui-même dit, avec un score **provisoire**.

---

## 1. Qualifier le lead : ce que « merci de me rappeler » vaut réellement

C'est la réponse la plus forte qu'on puisse recevoir : le lead a **répondu à la prospection et demande lui-même l'appel**. Sur le modèle à quatre dimensions :

| Dimension | Ce qu'on sait | Points |
|---|---|---|
| **Engagement (0–25)** | Réponse à un email → +15 si elle date de moins de 14 jours (à confirmer : date exacte de la réponse). Visites/ouvertures : inconnues sans CRM. Aucune relance subie (il a répondu) → pas de −5. | **15** *(provisoire)* |
| **Adéquation entreprise (0–25)** | Aucune entreprise associée et pas de connecteur Apollo/Clay dans cette session → échelle plate. | **5** *(à renoter : secteur + effectif)* |
| **Urgence (0–25)** | Âge du lead : +10 si 7–21 jours, +5 si <7 jours (à confirmer : `createdate`). Le +15 « mot-clé » (urgent / ASAP / échéance / budget validé) **exige la lecture des corps de notes** — « merci de me rappeler » n'est pas dans la liste, donc pas de +15 automatique ; si une note contient l'un de ces mots, il s'ajoute une fois les corps récupérés. | **5 à 10** *(provisoire)* |
| **Pénalité de récence** | Message reçu il y a <24 h → −25 ; 1–3 jours → −10 ; 4–7 jours → −5 ; >7 jours → 0. | **−10 à −25** |

**Scores provisoires selon l'ancienneté du message :**
- Reçu aujourd'hui : 15 + 5 + 10 − 25 = **5**
- Reçu il y a 2 jours : 15 + 5 + 10 − 10 = **20**
- Reçu il y a 5 jours : 15 + 5 + 10 − 5 = **25**

**Deux réserves à dire à voix haute :**
1. Ces points sont **provisoires** — l'adéquation est plate faute d'entreprise, et l'engagement ne compte que les signaux des 30 derniers jours. Colle-moi l'entreprise (ou un export) et je renoterai.
2. La pénalité de récence ne veut pas dire « appelle moins vite » : elle signale qu'on a **déjà travaillé ce lead aujourd'hui**. Un lead qui demande explicitement à être rappelé remonte quand même en tête de la liste d'appels du jour — c'est un engagement pris envers lui, pas une prospection à tiédir.

**Vérification anti-faux-classement :** si ce lead est comparé à d'autres et que le composite le plus haut et le plus bas diffèrent de moins de 10 points, j'abandonne le classement composite, je le dis (« signaux vides ») et j'ordonne uniquement sur les faits CRM : `hs_lead_status` (NEW avant IN_PROGRESS), `hs_is_unworked`, `hs_buying_role`, ancienneté du `jobtitle`, `num_associated_deals`, `createdate` récent en premier — présenté comme « ordonné par signal CRM », sans colonne de score. Avec un seul lead, la question ne se pose pas.

**Filtres à vérifier avant d'appeler :** `lifecyclestage` ∈ {Lead, MQL} et `hs_lead_status` ≠ Unqualified ; jamais un Customer ou Evangelist dans la liste d'appels. Si le cycle de vie est vide : « ⚠ Cycle de vie non défini — vérifie qu'il s'agit bien d'un lead avant d'appeler. »

---

## 2. Quand l'appeler — cadre réel (vérifié ce jour, vendredi 16 octobre 2026)

**⚠ Bloctel n'existe plus.** Le service a été supprimé le **11 août 2026** : depuis la loi du 30 juin 2025 (et le décret n° 2026-662 du 23 juillet 2026), le démarchage téléphonique des consommateurs est **interdit par défaut sans consentement préalable explicite**. Vérifier un numéro sur Bloctel est donc désormais inutile — la question à se poser est : **ai-je la preuve du consentement ?**

- **Pour ce lead : oui, en principe.** « Merci de me rappeler » est une demande explicite, libre et spécifique du prospect — c'est le consentement qui autorise l'appel. **Conserve la trace** (formulation, canal, date) quelque part sur la fiche : c'est le professionnel qui doit prouver le consentement.
- **Pour tous les autres appels B2C** (relances, rappels sans demande préalable) : **interdits** sans consentement au préalable, quel que soit l'horaire. Un contrat conclu après un démarchage non conforme est nul.

**Jours et horaires (encadrement décret n° 2022-1313, toujours en vigueur) :**
- Appels B2C autorisés : **du lundi au vendredi, hors jours fériés, de 10 h à 13 h et de 14 h à 20 h**.
- Interdits : samedi, dimanche, jours fériés.
- Fréquence : **4 tentatives maximum par 30 jours** glissants par consommateur (répondeur inclus).
- Dérogation possible : si le prospect a **explicitement consenti à une date et une heure précises** (« rappelle-moi mardi à 15 h »). Un « rappelle-moi » sans horaire ne précise rien → on reste dans les plages légales.
- **Appels B2B** (vers un professionnel en raison de son activité) : hors champ du décret — mais garde les mêmes plages par défaut, c'est la maison.

**Jours fériés FR à venir :** aucun entre aujourd'hui et fin octobre → **octobre 2026 est entièrement dégagé**. Prochains : **dimanche 1er novembre** (Toussaint), **mercredi 11 novembre** (Armistice), **vendredi 25 décembre** (Noël). Passage à l'heure d'hiver : **dimanche 25 octobre**.

### Recommandation concrète pour ce lead

| Situation | Quand appeler |
|---|---|
| Message reçu aujourd'hui (ven. 16 oct.) | **Aujourd'hui, dans les plages 10 h–13 h ou 14 h–20 h** — et idéalement dans l'heure qui suit : l'intention d'un inbound request chute vite. |
| Message reçu hier ou avant-hier | **Aujourd'hui 14 h–20 h** en priorité. |
| Si tu ne peux pas aujourd'hui | **Lundi 19 octobre, 10 h–13 h** (créneau de tête), repli **mardi 20 octobre, 14 h–16 h**. |
| Jamais | Samedi/dimanche, jours fériés, avant 10 h, après 20 h, 13 h–14 h (pause déjeuner), et — pour tout lead sans consentement tracé — tout appel de prospection B2C. |

**Créneaux d'agenda :** Calendar n'est pas connecté ici, donc je n'invente pas d'horaires. **Dis-moi deux ou trois plages de 30 min que tu as réellement libres lundi et mardi** et je les propose au lead. Aucun événement créé sans ta validation explicite.

---

## 3. Points de discussion pendant l'appel

1. **Cadrer la demande** : « Vous m'avez demandé à être rappelé — quel est le bon moment pour vous parler tranquillement, 10 ou 20 minutes ? »
2. **Urgence réelle** : échéance de décision, projet en cours, ce qui déclenche l'appel maintenant.
3. **Budget** : fourchette, qui le valide.
4. **Qualifier pour renoter l'adéquation** : secteur, effectif exact (1–50 dans l'ICP par défaut), siège — pour remplir la dimension actuellement plate à 5 points.
5. **Autorité** : son rôle, qui d'autre participe à la décision (`hs_buying_role`).
6. **Prochaine étape concrète** : démo, devis, ou passage à une autre personne.

---

## 4. Brouillon de message de confirmation (affiché, **non envoyé** — tu l'envoies depuis ta boîte)

```
Objet : Confirmation de votre rappel

Bonjour [Prénom],

Vous m'avez demandé à être rappelé : je vous appelle
[aujourd'hui entre 14 h et 20 h / lundi 19 au matin],
sur ce numéro.

Si un autre créneau vous convient mieux, dites-moi et
je m'adapte.

[Nom du dirigeant]
```

---

## 5. Tableau de tri (artefact)

```html
<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<title>Tableau de tri — leads à rappeler</title>
<style>
  :root { --bg:#f6f4ef; --ink:#1f2421; --line:#d9d3c7; --accent:#2f5d50; }
  * { box-sizing:border-box; }
  body { margin:0; padding:32px; background:var(--bg); color:var(--ink);
         font:15px/1.55 "Segoe UI",system-ui,-apple-system,sans-serif; }
  .wrap { max-width:940px; margin:0 auto; }
  h1 { font-size:21px; margin:0 0 4px; letter-spacing:-.01em; }
  .meta { font-size:13px; color:#6b6f6a; margin-bottom:20px; }
  table { width:100%; border-collapse:collapse; background:#fff;
          border:1px solid var(--line); }
  th { text-align:left; font-size:12px; text-transform:uppercase;
       letter-spacing:.06em; color:#6b6f6a; padding:10px 14px;
       border-bottom:2px solid var(--line); }
  td { padding:14px; border-bottom:1px solid var(--line); vertical-align:top; }
  tr:last-child td { border-bottom:none; }
  .name { font-weight:650; }
  .co { color:#6b6f6a; font-size:13px; }
  .score { font-family:"SF Mono",ui-monospace,Menlo,Consolas,monospace;
           font-size:18px; font-weight:600; text-align:right; white-space:nowrap; }
  .score small { display:block; font-size:11px; font-weight:400; color:#8a8f89; }
  .pill { display:inline-block; padding:3px 10px; border-radius:999px;
          font-size:11px; font-weight:700; letter-spacing:.05em;
          text-transform:uppercase; }
  .critical { background:#fdecec; color:#a4262c; border:1px solid #f3c2c4; }
  .warn { background:#fff6e5; color:#8a6100; border:1px solid #f2ddb0; }
  .good { background:#e9f5ee; color:#217346; border:1px solid #c3e3d0; }
  .disc { font-size:14px; color:#3c423d; }
  .disc::before { content:"— "; color:var(--accent); }
  .act { font-size:13px; color:#6b6f6a; }
  .note { margin-top:16px; font-size:13px; color:#6b6f6a;
          border-left:3px solid var(--line); padding-left:12px; }
</style>
</head>
<body>
<div class="wrap">
  <h1>Leads à rappeler — tri du 16 octobre 2026</h1>
  <div class="meta">Score composite provisoire (modèle 4 dimensions, 0–100) · HubSpot non connecté — données à confirmer</div>
  <table>
    <thead>
      <tr><th>#</th><th>Lead</th><th>Urgence</th><th>Score</th><th>Dernière activité</th></tr>
    </thead>
    <tbody>
      <tr>
        <td>1</td>
        <td>
          <div class="name">[Nom du lead] · <span class="co">[Entreprise]</span></div>
          <div class="disc">A répondu « merci de me rappeler » — consentement tracé, appel autorisé. Rentrer secteur + effectif pour sortir l'adéquation du plateau à 5. Scanne les corps de notes pour « urgent / ASAP / échéance / budget validé » (+15). Si message reçu aujourd'hui, la pénalité −25 s'applique déjà : il a été touché une fois aujourd'hui.</div>
          <div class="act">Appel : ven. 16 oct. 10 h–13 h ou 14 h–20 h · sinon lun. 19 oct. 10 h–13 h (repli mar. 20 oct. 14 h–16 h)</div>
        </td>
        <td><span class="pill critical">critical</span></td>
        <td class="score">5–25<small>provisoire</small></td>
        <td class="act">Réponse à la prospection (&lt; 14 j)</td>
      </tr>
    </tbody>
  </table>
  <div class="note">
    Pastille <strong>critical</strong> : demande explicite de rappel — en tête de la liste d'appels, indépendamment du score.
    Scores provisoires (CRM non connecté) ; l'échelle plate « signaux vides » ne s'applique pas : un vrai signal de réponse existe.
    Aucun Customer/Evangelist ; filtre Lead/MQL à confirmer à l'import.
  </div>
</div>
</body>
</html>
```

---

**Ce que le tri a produit :** un lead à rappeler en priorité (consentement « merci de me rappeler » tracé), noté 5–25 provisoires sur signal de réponse, à appeler dans les plages légales 10 h–13 h / 14 h–20 h — aujourd'hui si possible, sinon lundi 19 octobre au matin.

**Étape suivante :** « **liste d'appels** » (`/liste-appels`) pour poser les créneaux autour de cet ordre — dis-moi deux ou trois plages libres lundi/mardi et je les intègre. Sinon, « **mettre à jour le CRM** » (`crm-autopilot`) pour enregistrer le consentement et les champs d'entreprise une fois l'export importé.
