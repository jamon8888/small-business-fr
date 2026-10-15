# Modèle de données canonique

Clés canoniques en anglais. En-têtes français acceptés en entrée, sorties en
français par défaut.

## customers
customer_id ← id_client / code_client
name ← raison_sociale / nom / client
siren ← siren / siret
vat_number ← n_tva / num_tva / tva_intracom
billing_address ← adresse_facturation
delivery_address ← adresse_livraison
contact_email ← email / courriel
payment_terms ← conditions_reglement
credit_limit ← plafond_encours / encours_max
price_list ← grille / grille_tarifaire
segment ← segment / categorie
sales_rep ← commercial / representant
credit_insured ← assure / assurance_credit
retention_of_title ← reserve_propriete

## catalog
sku ← reference / ref / code_article
name ← designation / libelle
ean ← ean / code_barre / gtin
hs_code ← code_sh / nomenclature_douaniere
sale_unit ← unite_vente / uv
pack_size ← conditionnement / uvc
pallet_qty ← palette / qte_palette
weight_kg ← poids_kg / poids
origin_country ← pays_origine
vat_rate ← taux_tva / tva
unit_cost ← prix_achat / cout_unitaire
supplier_id ← id_fournisseur
lead_time_days ← delai / delai_fournisseur
moq ← moq / minimum_commande / qte_min
shelf_life ← dlc / ddm / peremption
compliance_flags ← conformite

## price_lists
price_list ← grille / tarif
sku ← reference
unit_price ← prix_unitaire / pu
min_qty ← palier / qte_min
discount_pct ← remise / remise_pct
valid_from ← debut_validite / du
valid_to ← fin_validite / au

## orders
order_id ← num_commande
customer_id ← id_client
status ← statut / etat (devis|commande|confirmee|preparee|expediee|facturee|soldee)
order_date ← date_commande
promised_date ← date_promise
sku ← reference
qty ← quantite
delivered_qty ← qte_livree
invoiced_qty ← qte_facturee
unit_price ← prix_unitaire / pu
discount_pct ← remise

## stock
sku ← reference
location ← emplacement / depot
on_hand ← stock_physique / stock
reserved ← reserve
on_order ← en_commande / attendu
count_date ← date_comptage
lot ← lot
expiry ← peremption / dlc

## suppliers / purchase_orders
supplier_id, lead_time_days ← delai, franco_threshold ← franco
po_id ← num_bc, qty_ordered ← qte_commandee, qty_received ← qte_recue,
unit_cost ← prix_achat, expected_date ← date_prevue

## receivables
invoice_id ← num_facture
customer_id ← id_client
invoice_date ← date_facture
due_date ← date_echeance
amount_ht ← montant_ht
vat ← tva
amount_ttc ← montant_ttc
paid_amount ← montant_paye
payment_method ← mode_paiement

## Règles
1. Colonne manquante : demandée une fois, puis mémorisée.
2. Champ absent ≠ zéro (absent-is-not-zero).
3. As-of de chaque fichier demandé et repris dans la sortie.
4. Montants en EUR, HT sauf mention.
