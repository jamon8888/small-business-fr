# Style d'artifact — le look maison

**Partagé dans tout le plugin.** Un seul système visuel pour que chaque page
produite par un skill se lise comme le même produit, pas comme quarante-six
produits différents. Lis ceci avant de construire le moindre artifact HTML ;
n'invente pas une nouvelle palette par skill.

**L'enjeu n'est pas la décoration.** Ce sont des outils de back-office pour
un dirigeant de petite entreprise — une feuille d'appels, un instantané de
trésorerie, une liste de réassort. Soigné et lisible bat flamboyant. Pas de
bannières héro, pas de dégradés marketing, pas de grandes déclarations de
mission. Un grand livre, pas une landing page.

**Les montants suivent la devise du dirigeant.** Chaque chiffre affiché par
une page porte le code devise ISO de l'entreprise (`GBP 1,240`, `AUD 18,400`),
lu dans le bloc `## Business context` selon
`shared/currency-and-locale.md`. Les figures en `EUR` des exemples ci-dessous
illustrent la forme, ce ne sont pas un défaut.

---

## Quand utiliser un artifact du tout

Tous les runs de skill n'en ont pas besoin. Va vers une page quand la sortie
est quelque chose que le dirigeant va **reconsulter, imprimer, passer à
quelqu'un d'autre, ou copier-coller depuis** — un tableau de bord, une feuille
d'appels, une checklist, un jeu de recommandations avec du texte à copier.
Évite-le pour un seul chiffre ou une réponse en une ligne ; la réponse du chat
est la livraison, et une page autour d'une phrase est du bruit.

**L'artifact est additif, jamais un remplacement.** Le dirigeant reçoit
toujours la réponse courte dans le chat. La page est là où il va pour la
vue complète.

**La préférence stockée du dirigeant prime sur le défaut.** Vérifie le bloc
`## Business context` à la recherche d'une ligne `Output preference`
(capturée pendant `smb-onboard`). Six valeurs :

- `visual artifacts` (ou absente) — l'artifact au style maison, le défaut.
- `docx` — livre un document DOCX au lieu de la page, et dis que c'est pour
  ça.
- `md` — livre un fichier markdown au lieu de la page, et dis que c'est pour
  ça.
- `notion` — crée la livraison comme page Notion via le connecteur Notion,
  dans l'emplacement de workspace choisi par le dirigeant, et dis que c'est
  pour ça. Créer une page est une écriture : nomme la destination avant de
  créer, et n'écrase jamais une page existante. Si Notion n'est pas connecté
  pour ce run, dis-le et replie-toi sur l'artifact visuel — ne bloque pas la
  livraison.
- `canva` — crée la livraison comme Canva Doc via le connecteur Canva. Le
  chemin est deux appels : `generate-design` avec le type de design `doc`,
  verbatim on, et le contenu complet dans la requête (il renvoie des
  candidats, pas un design), puis `create-design-from-candidate` sur le
  premier candidat, qui renvoie l'id et le lien du design à rendre. Là où le
  connecteur offre `create-design`, utilise-le en place de ce duo. La politique
  est toujours un nouveau design, jamais l'édition d'un existant. Pour le
  nommer, ouvre une transaction avec `read-design`, applique une opération
  `update_title` dans `edit-design` (titre de page, entreprise, date) et
  confirme, si bien que les runs ne se collisionnent jamais. Un Canva Doc
  n'accepte que titres, paragraphes, gras, italiques et listes — transforme
  chaque tableau en liste d'une ligne par rangée, et laisse les graphiques,
  images et liens dehors. Brand kit : la première fois qu'un skill livre vers
  Canva, lance `list-brand-kits`, demande une fois quel kit appliquer (ou
  aucun), et consigne le nom et l'id du kit en ligne `Canva brand kit` du
  profil ; les runs ultérieurs passent cet id comme `brand_kit_id` sans
  demander. Si Canva n'est pas connecté pour ce run, dis-le et replie-toi sur
  l'artifact visuel — ne bloque pas la livraison.
- `best for skill` — le skill décide par livraison : un tableau de bord ou
  un écran se rend en artifact ; tout ce qui est soumis, imprimé ou édité
  ailleurs (une proposition, un récit de candidature, un redline) part au
  format de document que le skill nomme déjà.

Une demande ponctuelle (« donne-moi ça en document Word ») gagne toujours sur
la préférence stockée, pour ce run uniquement.

**Une page, une livraison — ne livre jamais l'HTML deux fois.** Construire
l'artifact peut impliquer d'écrire d'abord un fichier HTML ; ce fichier est
un échafaudage, pas une livraison. Publie l'artifact et arrête-toi. Ne
mets pas aussi le .html en avant comme fichier téléchargeable, ne le joins
pas, ne le propose pas à côté de la page — un dirigeant à qui on remet à la
fois un artifact et un téléchargement HTML identique doit deviner lequel est
le vrai, et la réponse est toujours l'artifact. Le seul fichier qui part à
côté d'un artifact est un format réellement différent que le skill promet
déjà (un classeur XLSX, un redline DOCX, un packet PDF). Une seconde copie de
la même page dans une autre enveloppe ne l'est pas.

---

## Jetons de marque — défaut maison, interchangeables par entreprise

Chaque couleur et police ci-dessous est une propriété CSS custom. **Quand la
marque propre de l'entreprise est connue** — couleurs et logo tirés de leur
site web pendant `smb-onboard` et stockés dans le bloc `## Business context`
de la mémoire de session (ses champs Website / Brand colors / Logo) — remplace
les jetons couleur par les leurs. **Quand elle n'est pas connue,** le défaut
maison s'applique tel quel. Dans les deux cas, les schémas de composants
ci-dessous ne changent jamais ; seules les valeurs des jetons.

**La marque stockée s'applique à tous les artifacts, automatiquement.** Dès
que le bloc `## Business context` porte des Brand colors (et optionnellement
un Logo), chaque page rendue par n'importe quel skill les utilise — le
dirigeant personnalise une fois à l'onboarding et jamais par page. Capturer
cette marque est le travail de `smb-onboard` et ça doit rester sans friction :
un lien de site collé ou une description en mots plats (« vert forêt et
crème »), jamais un code hex, un sélecteur de couleurs ou un upload.

```css
:root {
  /* Palette par défaut maison — à remplacer par les couleurs de marque quand connues */
  --ink: #17211F;        /* texte principal, noir chaud quasi noir */
  --paper: #F4F3EE;      /* fond de page, pierre froide, pas crème */
  --paper-raised: #FFFFFF; /* surfaces de cartes posées sur --paper */
  --line: #DEDCD1;       /* filets de bordures et de règles */
  --accent: #0B6B5C;     /* accent principal — teal de grand livre, assuré */
  --accent-soft: #E4EFEC; /* teinte d'accent pour fonds de pastilles, surlignages */
  --amber: #B9781F;      /* accent secondaire — signal « à revoir » */
  --amber-soft: #F6EBDA;

  /* Sémantique — séparé de l'accent, jamais réaffecté à la marque */
  --good: #2E7D4F;
  --good-soft: #E4F0E8;
  --warn: #B9781F;
  --warn-soft: #F6EBDA;
  --critical: #B3392C;
  --critical-soft: #FBEAE7;

  /* Typographie — à remplacer les noms de famille si l'entreprise a les siens */
  --font-display: 'Zilla Slab', Georgia, 'Times New Roman', serif;
  --font-body: 'Public Sans', -apple-system, BlinkMacSystemFont, sans-serif;
  --font-mono: 'IBM Plex Mono', 'SF Mono', Consolas, monospace;
}

@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
    --ink: #EDEAE2;
    --paper: #14201C;
    --paper-raised: #1B2A25;
    --line: #2C3A34;
    --accent: #4FBFA5;
    --accent-soft: #1E332C;
    --amber: #E0A559;
    --amber-soft: #362A16;
    --good: #6FCB94;
    --good-soft: #1D3226;
    --warn: #E0A559;
    --warn-soft: #362A16;
    --critical: #E37B6B;
    --critical-soft: #3A211C;
  }
}

:root[data-theme="dark"] {
  --ink: #EDEAE2;
  --paper: #14201C;
  --paper-raised: #1B2A25;
  --line: #2C3A34;
  --accent: #4FBFA5;
  --accent-soft: #1E332C;
  --amber: #E0A559;
  --amber-soft: #362A16;
  --good: #6FCB94;
  --good-soft: #1D3226;
  --warn: #E0A559;
  --warn-soft: #362A16;
  --critical: #E37B6B;
  --critical-soft: #3A211C;
}
```

**Les polices se chargent depuis Google Fonts** — l'unique hôte que le sandbox
Artifact autorise :

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Zilla+Slab:wght@500;600&family=Public+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@500&display=swap" rel="stylesheet">
```

Si la police de marque propre de l'entreprise n'est pas sur Google Fonts,
garde le défaut maison plutôt que de lutter contre la CSP — un substitut proche
qui marche bat une police qui échoue à se charger en silence.

**Extraire les jetons de marque pendant l'onboarding.** Quand `smb-onboard`
lit le site web de l'entreprise (voir le workflow de ce skill), tire les
couleurs de fond/accent dominantes et toute font-family que le site déclare.
Montre au dirigeant ce qui a été trouvé — *« Ton site utilise un vert profond
et une serif à chasse large — tu veux que tes rapports matchent ? »* — et
n'applique que sur un oui. Stocke les valeurs résolues dans le bloc
`## Business context` (champs Brand colors / Logo, en ajoutant une ligne
Brand font quand une font-family exploitable a été trouvée) pour que
l'artifact de chaque skill lise les mêmes jetons sans les redériver.

---

## Typographie

- **Display** (`--font-display`) uniquement pour les titres de page et les
  en-têtes de section. Weight 600, `text-wrap: balance`, jamais pour le texte
  courant.
- **Body** (`--font-body`) pour tout ce qui se lit en prose.
- **Mono** (`--font-mono`) pour chaque chiffre qui vit dans une colonne —
  devise, comptages, dates dans un tableau. Appaire avec
  `font-variant-numeric: tabular-nums`.

Garde une échelle typographique et tiens-toi y :

```css
--text-xs: 0.75rem;   --text-sm: 0.875rem;  --text-base: 1rem;
--text-lg: 1.125rem;  --text-xl: 1.375rem;  --text-2xl: 1.75rem;
--text-3xl: 2.25rem;  /* le seul gros chiffre d'un tableau de bord, avec parcimonie */
```

---

## Mise en page — le schéma « carte de grand livre »

Le contenu vit dans des panneaux bordurés (`--paper-raised` sur `--paper`,
`1px solid var(--line)`, `border-radius: 6px` — un rayon léger et délibéré,
pas `rounded-lg` partout par défaut). Les panneaux s'empilent avec `gap`, pas
margin. Les tableaux larges ont leur propre wrapper `overflow-x: auto` pour
que la page ne défile jamais en travers.

```css
.panel {
  background: var(--paper-raised);
  border: 1px solid var(--line);
  border-radius: 6px;
  padding: 1.5rem;
}
.page {
  display: flex;
  flex-direction: column;
  gap: 1.25rem;
  max-width: 840px;
  margin: 0 auto;
  padding: 2rem 1.5rem;
}
```

---

## Composants

### En-tête

Chaque artifact ouvre de la même façon : nom de l'entreprise (ou nom du
plugin si aucun n'est connu encore), le rôle de la page en une ligne, et
quand elle a été générée. Pas de héro, pas d'illustration.

```html
<header class="page-header">
  <div class="brand-mark">RM</div>
  <div>
    <h1>Instantané de trésorerie</h1>
    <p class="meta">Ridgeline Mechanical · Généré le 21 août 2026</p>
  </div>
</header>
```

`.brand-mark` est un monogramme à deux lettres sur fond `--accent-soft`,
texte `--accent`, `--font-display` — la même forme sur chaque page, initiales
tirées du nom de l'entreprise.

### Tuile de statistique

Le chiffre qui compte, en grand, avec une ligne en français courant en
dessous, pas juste une étiquette.

```html
<div class="stat-tile">
  <div class="stat-figure">18 240 €</div>
  <div class="stat-label">Trésorerie en main</div>
  <p class="stat-context">Environ 11 semaines de trésorerie au rythme de consommation actuel.</p>
</div>
```

`.stat-figure` utilise `--font-mono`, `--text-3xl`, `tabular-nums`. La ligne
de contexte est ce qui le rend utile — un chiffre seul n'est pas une réponse.

### Pastille d'état

Un petit tag façon tampon, pas un badge arrondi en pilule — rectangulaire
avec un léger rayon, en majuscules, espace entre lettres. Couleurs
sémantiques uniquement.

```html
<span class="status status--good">Bonne trajectoire</span>
<span class="status status--warn">À revoir</span>
<span class="status status--critical">En retard</span>
```

```css
.status {
  display: inline-block;
  padding: 0.15rem 0.55rem;
  border-radius: 3px;
  font: 600 var(--text-xs) var(--font-body);
  text-transform: uppercase;
  letter-spacing: 0.04em;
}
.status--good { background: var(--good-soft); color: var(--good); }
.status--warn { background: var(--warn-soft); color: var(--warn); }
.status--critical { background: var(--critical-soft); color: var(--critical); }
```

### Tableau

Filets de lignes, pas de grille lourde. Chiffres alignés à droite en
`--font-mono`. Enveloppe dans `.table-scroll` pour la largeur.

```html
<div class="table-scroll">
  <table>
    <thead><tr><th>Client</th><th>Montant</th><th>Jours de retard</th></tr></thead>
    <tbody>
      <tr><td>Corwin & Bay</td><td class="num">1 240 €</td><td class="num">14</td></tr>
    </tbody>
  </table>
</div>
```

### Bloc à copier

Pour un texte que le dirigeant est censé coller ailleurs — un correctif SEO,
un brouillon d'e-mail, une annonce d'emploi. Le bouton copie via l'API
Clipboard avec un repli de sélection manuelle si le sandbox la bloque
(teste — ne suppose pas que ça marche toujours).

```html
<div class="copy-block">
  <button class="copy-btn" onclick="copyBlock(this)">Copier</button>
  <pre>Ajoute ceci à la balise title de ta page d'accueil : « Ridgeline Mechanical — Réparation CVC le jour même, métropole de Denver »</pre>
</div>
<script>
function copyBlock(btn) {
  const text = btn.nextElementSibling.textContent;
  const done = () => { btn.textContent = 'Copié'; setTimeout(() => btn.textContent = 'Copier', 1500); };
  if (navigator.clipboard?.writeText) {
    navigator.clipboard.writeText(text).then(done).catch(() => fallbackSelect(btn));
  } else {
    fallbackSelect(btn);
  }
}
function fallbackSelect(btn) {
  const range = document.createRange();
  range.selectNodeContents(btn.nextElementSibling);
  const sel = window.getSelection();
  sel.removeAllRanges();
  sel.addRange(range);
  btn.textContent = 'Sélectionné — Cmd/Ctrl+C';
}
</script>
```

### Checklist avec progression

Pour un processus de clôture ou une liste d'étapes d'onboarding. Le comptage
se déduit des éléments, jamais tapé à la main, pour qu'il ne puisse pas
dériver hors synchro.

```html
<div class="checklist">
  <p class="checklist-progress">3 sur 9 faits</p>
  <label><input type="checkbox" checked disabled> Flux bancaire rapproché</label>
  <label><input type="checkbox" disabled> Paie comptabilisée</label>
</div>
```

### Pied de page

Chaque artifact finit de la même façon — discret, petit, `--text-xs`, coloré
`--line` :

```html
<footer class="page-footer">Généré par <strong>Instantané de trésorerie</strong> — Petite entreprise</footer>
```

---

## Les deux thèmes, toujours

Suis exactement la structure de jetons ci-dessus : `:root` nu pour le clair,
la media query `prefers-color-scheme` gardée par `:not([data-theme="light"])`,
et `:root[data-theme="dark"]` répétant les mêmes valeurs pour qu'un toggle
explicite gagne dans les deux sens. Chaque composant lit les couleurs depuis
les jetons — jamais de hex littéral dans une règle de composant — si bien
qu'un seul point de remplacement (couleurs de marque, ou le bloc mode sombre)
recolore toute la page correctement.

---

## Ce qu'il ne faut pas faire

- **Ne livre pas la page deux fois.** Publie l'artifact ; ne donne jamais
  aussi le même contenu en fichier .html téléchargeable. Une page, une
  livraison.
- **N'invente pas une nouvelle palette par skill.** Chaque artifact utilise
  ces jetons. Un look ponctuel trahit tout l'intérêt d'un style maison.
- **N'ajoute pas de héro, d'illustration ou de copy marketing.** Ce sont des
  outils de pilotage, pas des pitchs.
- **Ne saute pas le mode sombre.** La moitié de la checklist ci-dessus existe
  pour empêcher une page illisible dans l'autre thème.
- **Ne suppose pas que l'API clipboard marche.** Le sandbox peut la bloquer —
  teste, et livre le repli.
- **Ne laisse pas cette règle faire grossir les fichiers SKILL.md.** L'étape
  de livraison d'un skill est une ligne : « Rend le résultat au style
  d'artifact maison (`../../shared/artifact-style.md`), » avec les composants
  spécifiques nommés. Tout le détail CSS et composants reste dans ce seul
  fichier.

---

## Construction de référence

L'édition amont livre `reference/artifact-example.html` dans ce dossier : une
page complète et fonctionnelle utilisant tous les composants ci-dessus, pour
copier la structure directement. Ce fichier n'est pas inclus dans l'édition
française ; assemble la page à partir des exemples de composants de ce
fichier. Une réserve quand on copie : l'exemple amont est un fichier
autonome avec un squelette doctype/head/body complet pour qu'il s'ouvre dans
un navigateur. Quand la surface de publication enveloppe le contenu dans son
propre squelette de document (l'outil Artifact le fait), copie seulement les
styles et le contenu du body — jamais les balises doctype, html, head ou body
elles-mêmes.
