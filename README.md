# Petite entreprise (France) — `small-business-fr`

Édition française du plugin [Claude for Small Business](https://www.anthropic.com/news/claude-for-small-business)
d'Anthropic, pour les TPE et PME françaises de 1 à 50 personnes qui vendent des
prestations, des produits à des professionnels (négoce ou fabrication), ou les
deux.

65 skills et 39 commandes, entièrement en français, adaptés au droit français,
à la TVA, à la facturation électronique et aux connecteurs français (Qonto,
Pennylane, Sendcloud).

> Édition communautaire, non publiée ni approuvée par Anthropic.
> Basée sur le plugin `small-business` v1.35.1 (Apache-2.0) — voir LICENSE et NOTICE.

## Installation

Le même plugin s'installe sur les trois surfaces ; les skills et commandes
fonctionnent partout, les hooks et sous-agents tournent dans Cowork et Claude Code.

### Claude Desktop, Cowork et chat web

1. Ouvre le menu **Customize** (barre latérale gauche) → onglet **Plugins**.
   Dans Cowork, ouvre d'abord l'onglet « Cowork », puis **Customize**.
2. Clique sur **Add** → **Add marketplace**.
3. Choisis **Add from a repository** et entre `jamon8888/small-business-fr`.
4. Le plugin **Petite entreprise (France)** apparaît : clique sur **Add**.

### Claude Code (terminal)

```
/plugin marketplace add jamon8888/small-business-fr
/plugin install small-business-fr@small-business-fr
```

### Équipes et Enterprise

Le paquet zip (`small-business-fr.zip`, généré par le build) peut être
uploadé comme plugin personnalisé dans **Customize → Plugins**, ou partagé
directement à un collègue.

## Premiers pas

1. Lance `/demarrer` — le skill d'onboarding pose les bonnes questions
   (activité, taille, outils) et connecte tes services.
2. Ensuite, décris le travail en français naturel, ou tape `/` pour choisir
   une commande.

## Ce qu'il y a dedans

| Domaine | Commandes principales |
|---|---|
| Pilotage | `/brief-lundi`, `/pack-rapports`, `/bfr` |
| Comptabilité | `/cloturer-mois`, `/tva`, `/fiscalite`, `/echeances` |
| Encaissement | `/relancer-clients`, `/encours`, `/verifier-client` |
| Paiements | `/payer-factures` (demande groupée + lien d'approbation) |
| Produits | `/devis`, `/commande-recue`, `/stock`, `/reapprovisionner`, `/facturer-temps` |
| Recrutement | `/preparer-paie` (variables de paie, sans calcul social) |
| Croissance | `/remplir-pipeline`, `/liste-appels`, `/reactiver-clients`, `/lundi-marketing` |
| Démarrage | `/demarrer` |

Le routeur (`smb-router`) choisit le skill adapté quand tu décribes le travail
sans nommer de commande.

## Ce que le plugin ne fait jamais

- Aucune déclaration déposée.
- Aucun paiement exécuté (demande groupée Qonto + lien d'approbation).
- Aucun envoi sans validation.
- Aucun calcul social.
- Aucun chiffre inventé.

## Avertissement

Ni conseil fiscal, ni juridique, ni social. Les articles cités
(`L441-10`, `D441-5`, `L624-16`…) sont vérifiés, mais fais valider tes
situations par ton expert-comptable ou ton avocat.

## Pour les contributeurs

Le build, la localisation et la porte de qualité sont documentés dans
[DEVELOPERS.md](DEVELOPERS.md). En résumé :

```bash
python3 build.py --clean      # régénère le plugin + le zip
python3 production_check.py   # 11 contrôles qualité
```

## Licence

Apache-2.0 — voir [LICENSE](LICENSE) et [NOTICE](NOTICE).
