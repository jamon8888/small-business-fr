# Clôture de juin — 3 opérations bancaires non imputées

Bonne nouvelle : 3 opérations non imputées en fin de mois, ce n'est pas une erreur, c'est du lettrage restant. Le virement groupé de 3 400 € est précisément le cas le plus typique : on ne le « raccorde » pas en bloc, on le **décompose** puis on lettre chaque paiement sur sa facture client. Voici la marche à suivre, dans l'ordre.

## 1. Lettrage du virement groupé de 3 400 € (priorité)

**Le principe :** une seule ligne bancaire à 3 400 € correspond, au grand livre, à **4 encaissements clients distincts**. L'objectif est de transformer cette ligne en 4 paiements, chacun lettré sur sa facture.

**Concrètement :**

1. **Lister les 4 paiements.** Ouvrir le relevé du virement (votre banque le décompose généralement, sinon le rapport du prestataire de paiement l'affiche). Pour chaque paiement : client, montant, date.
2. **Repérer la facture correspondante** pour chacun des 4 clients : la facture émise, exigible, réglée ce jour-là.
3. **Vérifier l'addition.** La somme des 4 paiements doit égaler 3 400 € — ou 3 400 € + les frais de traitement du prestataire s'il les a prélevés sur le virement.

À titre d'exemple, la décomposition s'écrit ainsi :

| Client | Facture | Montant |
|---|---|---|
| Atelier Martin | F-0612 | 1 250,00 EUR |
| Boulangerie Duval | F-0589 | 880,50 EUR |
| SARL Lefèvre | F-0621 | 975,00 EUR |
| Ventes comptantes | — | 294,50 EUR |
| **Total** | | **3 400,00 EUR** |

4. **Lettrer** : associer chaque paiement à sa facture dans le grand livre. Une fois les 4 lettrages faits, la ligne de 3 400 € est imputée à 100 % et ne figure plus parmi les non imputées.

**Si l'addition ne tombe pas juste (écart > 0,50 EUR) :**

- **L'écart correspond aux frais du prestataire** (Stripe, PayPal, Square…) : c'est attendu. Imputer les frais au compte de frais de commission et considérer le virement comme rapproché — ne pas le signaler comme erreur.
- **Un des 4 paiements est un remboursement** (montant négatif) : le lettrer sur l'avoir client correspondant, jamais sur le dépôt.
- **Un client reste inidentifiable** : c'est un point ouvert. Je le passe en liste des « points à traiter » du paquet de clôture, je ne le laisse pas disparaître.

**Piège à éviter :** 4 lignes de même fournisseur ou de même client, même date, montants différents, n'ont rien d'un doublon. C'est la ventilation d'une seule transaction — ne jamais la signaler comme saisie en double.

## 2. Les deux autres opérations non imputées

Pour chacune, la même logique en trois temps :

1. **Identifier la nature** : paiement fournisseur, encaissement client, prélèvement, dépense carte, virement interne.
2. **Trouver le document de rattachement** : la facture fournisseur payée, la facture client encaissée, la note de frais.
3. **Lettrer** : associer l'opération bancaire au document.

Deux cas particuliers :

- Si une opération est le règlement d'une **facture fournisseur pas encore saisie**, saisir la facture d'abord, lettrer ensuite.
- Si une opération ne peut pas être identifiée : donnez-moi la date, le montant et le libellé, je la piste. Si elle reste inidentifiable, elle part dans la feuille « Points à traiter » du paquet de clôture, avec une mention explicite — jamais supprimée discrètement.

## 3. Puis on poursuit la clôture de juin

Dès que les 3 opérations sont lettrées, le rapprochement bancaire est propre. Il reste le reste de la séquence de clôture :

1. **Cut-off**
   - **FAE (factures à établir)** : livraisons de juin non encore facturées → émettre les factures pour que le chiffre d'affaires soit bien au bon mois.
   - **FNP (factures non parvenues)** : achats réceptionnés en juin, facture fournisseur pas encore reçue → inscrire un estimatif pour que la charge soit au bon mois.
   - **PCA / CCA** simples, à mettre à jour.
2. **Stocks** (si profil négoce ou fabrication) : coupure du stock — renvoi à la procédure de comptage et cut-off des stocks.
3. **Social** : charges sociales du mois et provision des congés payés.

## 4. Sorties de la clôture

À l'issue de ces étapes, je génère le **paquet de clôture daté** (classeur xlsx — compte de résultat, rapprochement, points à traiter — et résumé PDF d'une page, nommés au format ISO 8601), et je vous en donne le récapitulatif en une ligne :

> « X écritures, Y EUR traités, Z points à vérifier. »

Tout point ouvert que vous avez choisi de reporter y figurera dans la feuille « Points à traiter », visible par votre comptable. C'est aussi pour cela qu'il faut acquitter chaque signalement avant l'export — soit en le résolvant, soit en le reportant explicitement.

## En résumé

1. **Décomposer** le virement de 3 400 € en ses 4 paiements et lettrer chacun sur sa facture client.
2. **Lettrer** les 2 autres opérations (identifier, trouver le document, associer).
3. **Enchaîner** sur le cut-off (FAE / FNP), les stocks si applicable, et le social.
4. **Clôturer** avec le paquet daté et le récapitulatif en une ligne.

**Ce dont j'ai besoin de vous :** la liste des 4 paiements constituant le virement de 3 400 € (ou le rapport de votre prestataire de paiement), et la description des 2 autres opérations non imputées (date, montant, libellé). Dès que c'est fourni, je fais le lettrage et je poursuis la clôture.
