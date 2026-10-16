# Note de vérification fournisseur — Techdis SARL
**Objet :** contrôle préalable avant commande de 15 000 €
**Date :** 16 octobre 2026
**Statut :** 🔴 **NON VERIFIÉ — PAIEMENT À SUSPENDRE**

---

## 1. Conclusion en une phrase

Le SIREN **912 456 789** n'existe **pas** dans les registres officiels français et ne respecte même pas la règle de calcul du numéro SIREN : le fournisseur « Techdis SARL » ne peut être identifié avec les éléments transmis, et la commande de 15 000 € ne doit pas être exécutée avant vérification complète de son identité.

## 2. Résultats des vérifications effectuées

| Contrôle | Source | Résultat |
|---|---|---|
| Existence du SIREN 912 456 789 dans le répertoire SIRENE (INSEE) | Annuaire officiel des entreprises (annuaire-entreprises.data.gouv.fr, DINUM) | **Non retrouvé** |
| Validité du numéro (algorithme de Luhn, contrôle du 9ᵉ chiffre) | Calcul sur le numéro transmis | **Numéro structurellement invalide** (le chiffre de contrôle attendu ne correspond pas au « 9 » transmis) |
| Variante corrigée du numéro (chiffre de contrôle valide) | Annuaire officiel des entreprises | **Également absente** des registres officiels |
| Recherche nominale « Techdis SARL » | Recherche web | Aucune entreprise française correspondante identifiée ; seules des sociétés étrangères homophones (« Tekdis », États-Unis/Australie) et une société parisienne homophone au SIREN différent (« TECDIS », 433 132 230, inactive) apparaissent |

**Lecture pour la direction :** un SIREN qui échoue le test de Luhn n'est pas une simple coquille possible — c'est l'indicateur le plus fort d'un faux identifiant. L'annuaire officiel de l'État qualifie expressément ce type de numéro de « potentiellement frauduleux ».

## 3. Risques identifiés

- **Risques majeurs :**
  - **Usurpation d'identité / facture frauduleuse** : un faux fournisseur avec un SIREN fictif est le schéma classique de l'arnaque à la commande électronique (devis reçu par e-mail, coordonnées bancaires piégées).
  - **Perte des fonds** : sur 15 000 €, un virement vers un compte tiers est irrécupérable une fois exécuté.
  - **Risque comptable et fiscal** : une facture émise par une entité inexistante est indigne de déduction TVA (débitoires à établir en cas de doute sur l'existence du cocontractant).
- **Hypothèse bénigne (à écarter en priorité) :** simple erreur de transcription du SIREN par le service achats ou le commercial.

## 4. Plan d'action — dans l'ordre

**Immédiat (avant tout engagement) :**
1. **Suspendre la commande et toute préparation de paiement** jusqu'à clarification.
2. **Relire la pièce d'origine** (devis, bon de commande, e-mail) : recopier le SIREN d'origine caractère par caractère et le comparer à « 912 456 789 ». Une faute de frappe est possible.
3. **Demander au fournisseur, par le canal habituel** (pas uniquement l'e-mail du devis) :
   - le SIREN exact et le **numéro de TVA intracommunautaire** (format FR + 9 chiffres),
   - un **extrait KBIS** de moins de 3 mois,
   - les statuts si possible.

**Vérifications croisées (1 jour ouvré) :**
4. **Vérifier le numéro de TVA** sur le service public officiel de vérification des identifiants TVA (DGFiP) ou via VIES pour un numéro étranger.
5. **Rechercher le SIREN corrigé** sur annuaire-entreprises.data.gouv.fr : confirmer que la dénomination y figure bien « Techdis SARL », avec adresse et activité cohérentes avec la commande.
6. **Contrôler l'ancienneté du site web** du fournisseur (whois : date de création du domaine) — un domaine créé depuis moins de 6 mois est un signal d'alerte.
7. **Contrôler l'accord entre e-mails et site** : l'expéditeur du devis doit utiliser le domaine du site officiel du fournisseur (et non une adresse gratuite type @gmail.com ou un domaine en .com/.net proche mais distinct du site — « typosquatting »).
8. **Vérifier les coordonnées bancaires** : le titulaire du compte IBAN doit correspondre exactement à la dénomination sociale « Techdis SARL » ; faire confirmer par téléphone, au numéro figurant sur le site officiel (et non le numéro du devis), les RIB transmis.

**Décision :**
- **Si l'identité est confirmée** (SIREN existant, TVA valide, KBIS cohérent) : reprendre la commande avec les garde-fous ci-dessous.
- **Si le moindre point reste incohérent** : **ne pas payer**. En cas de suspicion d'arnaque à la facture, signaler à votre banque (blocage du virement) et, le cas échéant, à la police judiciaire (cellule de lutte contre la fraude). Conserver devis, e-mails et captures d'écran.

**Garde-fous pour la commande de 15 000 € (une fois le fournisseur vérifié) :**
- contrat écrit avec délais, pénalités et conditions de résiliation ;
- **pas d'acompte supérieur à 30 %**, solde à réception et après réception/qualité ;
- paiement par virement au seul RIB vérifié, jamais à un IBAN ayant changé récemment sans justification ;
- facture conforme (mentions légales complètes : dénomination, SIREN, adresse, numéro de TVA, numéro de facture).

## 5. Points de vigilance récurrents (à intégrer dans la procédure achats)

- **Tout nouveau fournisseur** : vérification systématique SIREN + TVA sur les sources officielles **avant** toute commande, quel que soit le montant ;
- toute modification soudaine de RIB = contrôle téléphonique systématique ;
- urgence artificielle (« offre valable 48 h ») + prix nettement inférieur au marché + contact par e-mail seul = trio d'alerte classique.

---
*Sources : annuaire-entreprises.data.gouv.fr (DINUM/INSEE, répertoire SIRENE) — vérification du 16/10/2026 ; algorithme de contrôle de Luhn applicable aux numéros SIREN ; recherche web nominale.*
