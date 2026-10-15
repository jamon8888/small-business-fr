# Facture du 28/09 passée sur octobre : comment rattraper

Ce que vous décrivez s'appelle un **écart de cut-off** : l'opération est bien de septembre (fait générateur au 28/09), mais elle a été saisie sur le mois d'octobre. C'est une erreur de date de saisie, pas une erreur sur le fond — donc cela se corrige par une écriture ciblée, sans reprise générale.

## La règle à retenir

C'est **la date de la facture / de l'opération (28/09)** qui détermine l'imputation sur l'exercice, pas le jour où vous avez fait la saisie. Tant que la facture porte le 28/09, la vente appartient à septembre.

## Option recommandée : une écriture d'OD de cut-off au 30/09

Dans le journal « Opérations diverses », datée du 30/09, avec un libellé explicite type *« Régularisation de cut-off – facture du 28/09 »* et la facture en pièce jointe :

| Compte | Libellé | Débit | Crédit |
|---|---|---|---|
| 706 | Ventes de biens / prestations (HT) | XX | |
| 445711 | TVA collectée (7 %, 10 % ou 20 %) | YY | |
| 412 | Clients – factures à établir | | XX + YY |

Puis, dans le mois où la facture est réellement éditée (octobre), l'OD s'extourne :

- la facture réelle : `411 / 706 / 445711`
- l'OD d'extourne : `412 / 706 / 445711`

Résultat : **septembre porte la vente**, octobre est neutre sur 706 et 445711, et les comptes clients 411 / 412 retombent à zéro. Pas de double comptabilisation, et chaque ligne a une pièce justificative.

## Si vous êtes en TVA « option débits » (prestations)

Pour des prestations de services, la TVA est exigible à l'encaissement : l'OD de septembre porte alors **le HT seul** (`706 / 412`), et la TVA sera déclarée dans la CA3 du mois où vous encaissez. Vérifiez votre option avant d'ajouter une ligne 44571.

## TVA : deux cas à distinguer

1. **La CA3 de septembre n'est pas encore déposée** → l'OD entre dans la déclaration de septembre. C'est le plus propre, faites-le maintenant.
2. **La CA3 de septembre est déjà déposée** → on ne modifie pas une déclaration. Vous déclarez la TVA en octobre et vous notez l'écart de quelques jours (intérêts de retard de 0,25 %/mois, plafonnés à 5 % du montant). Si c'est une **facture de période** (prestation continue du 1er au 30/09) et non une facture unitaire, aucun impact : la déclaration suit toujours la date de facture, pas la date d'édition.

## Impact sur le résultat

Aucun impact sur le **résultat annuel** : c'est un transfert entre deux mois du même exercice. Seuls votre résultat du mois de septembre et vos déclarations de TVA sont à corriger.

## Pièges à éviter

- **Ne faites pas** l'OD en septembre *et* laissez la facture telle quelle en octobre sans extourne : octobre resterait faux (vente en double dans l'année, soldes clients qui ne tombent pas à zéro).
- N'attendez pas la clôture annuelle pour le mentionner : plus c'est tôt, plus c'est lisible.
- N'éditer pas une nouvelle facture « corrigée » : vous créeriez une seconde facture et un doublon client. Une facture portant la date du 28/09, éditée en octobre, est parfaitement régulière.

## Profitez-en pour balayer le même risque

Un export des factures de septembre et octobre, et cherchez toutes celles dont la **date de facture** est antérieure au 1er du mois d'enregistrement :

- côté ventes : c'est le cas que vous venez de corriger ;
- côté achats : une prestation reçue en septembre et facturée en octobre s'impute aussi en septembre (à traiter en 401 / 609, ou en 6xx / 4452 selon votre option).

## Selon votre logiciel

Beaucoup d'outils de gestion (type Pennylane, Sage, etc.) permettent de **saisir directement la facture dans le mois de septembre** avec sa date du 28/09, tant que la période n'est pas verrouillée : c'est encore plus simple que l'OD. Si la période est déjà clôturée dans le logiciel, faites l'OD ci-dessus. Vérifiez ensuite que l'export de la balance générale de septembre reflète bien la vente.

---

En résumé : une écriture d'OD de cut-off au 30/09 (HT + TVA, crédit 412 « factures à établir »), extournée à l'édition de la facture — et un contrôle des autres factures à cheval sur la période.