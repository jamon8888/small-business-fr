# Changelog

## v1.1.0-fr.1 — 2026-10-15

### Ajouté
- **Facturation électronique complète** : `einvoice-readiness` réécrit avec un
  mode **audit** (plateforme agréée, réception, B2G via PFP, e-reporting,
  mentions) et un mode **préparation de l'émission** (complétude des champs
  EN 16931 du Factur-X)
- Référentiel `einvoice-readiness/reference/facture-electronique-fr.md` :
  calendrier officiel vérifié le 2026-10-15 (impots.gouv.fr), plateformes
  agréées vs solutions compatibles, profils Factur-X, champs BT obligatoires
- Routeur : les demandes « Factur-X », « plateforme agréée », « PFP » routent
  vers `einvoice-readiness`

### Modifié
- `calendrier-fiscal-fr` : la ligne facturation électronique est confirmée
  (réception 09/2026, émission GE/ETI 09/2026, PME 09/2027) — plus de
  « à revérifier »
- `devis-facture-fr` : renvoi vers `einvoice-readiness` pour le Factur-X au
  lieu de « pas de Factur-X en v1 »

## v1.0.0-fr.1 — 2026-10-15

### Ajouté
- Édition française complète du plugin `small-business` d'Anthropic
  (v1.35.1) : **65 skills, 39 commandes**, 167 fichiers traduits
  (~174 000 mots)
- 24 connecteurs dont les français : **Qonto, Pennylane, Sendcloud**
- Droits français : article L441-10 / D441-5 (indemnité de recouvrement
  40 €), L624-16 (réserve de propriété), calendrier fiscal FR, Bloctel,
  facturation électronique
- 7 documents partagés traduits (sécurité des contenus non fiables,
  « l'absent n'est pas zéro », neutralité des connecteurs, style d'artifact…)
- Porte de qualité : `production_check.py` (11 contrôles) + `verify_fr.py`
  (parité structurelle) + lint du plugin
- Marketplace installable sur Claude Code, Cowork, Claude Desktop

### Retiré (skills US sans équivalent FR)
- `tax-season-organizer`, `grant-rfp-writer`
