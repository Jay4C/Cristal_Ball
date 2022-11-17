import unittest
import xlrd
import pdfkit
import datetime
from datetime import datetime as dt
import os
from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter


class UnitTestsReportingBusinessPlan(unittest.TestCase):
    def test_business_plan(self):
        print("test_business_plan")

        location = ("A:\\1_Professionnel\\1_Holomorphe\\1_Administration\\1_Comptabilite_Fiscalite\\Business_Plan.xls")

        workbook = xlrd.open_workbook(location)

        sheet = workbook.sheet_by_name("Data")

        # Informations generales entreprise
        denomination_sociale = "S.A.S.U. à capital variable HOLOMORPHE"
        capital_social = "100 euros"
        adresse_siege_social = "31 Avenue de Ségur - ABC LIV Ségur - 75007 Paris"
        siret = "88363255600014"
        rcs = "R.C.S. PARIS - Greffe du Tribunal de Commerce de PARIS"
        activite = "Commerce de gros (commerce interentreprises) de produits chimiques"
        code_naf = "4675Z"
        numero_tva_intracommunataire = "FR06883632556"
        president = "Mr "
        date_immatriculation = "26 Mai 2020"

        # Rapport
        body = '<!doctype html>' + \
               '<html lang="en">' + \
               '<head>' + \
               '<meta charset="utf-8">' + \
               '<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">' + \
               '<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css" integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">' + \
               '<title>Livre_Inventaire</title>' + \
               '</head>' + \
               '<body>' + \
               '<div class="container">' + \
               '<div class="card text-center">' + \
               '<div class="card-header text-center">Business plan</div>' + \
               '<div class="card-body">' + \
               '<h6>Dénomination sociale : ' + denomination_sociale + ' / Capital social : ' \
               + capital_social + '</h6>' + \
               '<h6>Adresse du siège social : ' + adresse_siege_social + ' / SIRET : ' \
               + siret + '</h6>' + \
               '<h6>Registre de Commerce et des Sociétés : ' + rcs + '</h6>' + \
               '<h6>Activité : ' + activite + ' / Code NAF : ' + code_naf + '</h6>' + \
               '<h6>N° TVA intracommunataire : ' + numero_tva_intracommunataire + ' / Président : ' \
               + president + ' / Date immatriculation : ' + date_immatriculation + '</h6>' + \
               '<br>' + \
               '<br>' + \
               '<div class="card border-dark">' + \
               '<h5 class="card-header border-dark text-center">' + \
               'Business plan de la société Holomorphe' + \
               '</h5>' + \
               '<div class="card-body border-dark">' + \
               '<!-- Présentation du projet -->'+ \
               '<div class="card border-dark">' + \
               '<h5 class="card-header border-dark text-center">' + \
               'Présentation du projet' + \
               '</h5>' + \
               '<div class="card-body border-dark">' + \
               '<h5>' + \
               'Nature du projet :' + \
               '</h5>' + \
               '<br>' + \
               '<h5>' + \
               'Idientité du porteur du projet : ' + \
               '</h5>' + \
               '<br>' + \
               '<h5>' + \
               "Informations du réseau d'accompagnement :" + \
               '</h5>' + \
               '<br>' + \
               '<h5>' + \
               "Informations sur l'expert-comptable :" + \
               '</h5>' + \
               '<br>' + \
               '<div class="card border-dark">' + \
               '<h5 class="card-header border-dark text-center">' + \
               'Fiche synthétique du projet' + \
               '</h5>' + \
               '<div class="card-body border-dark">' + \
               '<h5>' + \
               'Nature du projet (création / reprise) :' + \
               '</h5>' + \
               '<br>' + \
               '<h5>' + \
               'Enseigne commerciale : ' + \
               '</h5>' + \
               '<br>' + \
               '<h5>' + \
               'Forme juridique : ' + \
               '</h5>' + \
               '<br>' + \
               '<h5>' + \
               'Type de projet : ' + \
               '</h5>' + \
               '<br>' + \
               '<h5>' + \
               'Activité : ' + \
               '</h5>' + \
               '<br>' + \
               '<h5>' + \
               'Clientèle : ' + \
               '</h5>' + \
               '<br>' + \
               '<h5>' + \
               "Chiffre d'affaires : " + \
               '</h5>' + \
                  '<br>' + \
                  '<h5>' + \
                    'Mon apport : ' + \
                  '</h5>' + \
                  '<br>' + \
                  '<h5>' + \
                    'Mon dernier salaire / mon salaire la 1ère année du projet :' + \
                  '</h5>' + \
                  '<br>' + \
                  '<h5>' + \
                    'Mes besoins de financement : ' + \
                    '<br>' + \
                    '- Investissement matériel (véhicule, machines, bâtiments…) : ' + \
                    '<br>' + \
                    '- Fonds de commerce, Pas de porte :' + \
                    '<br>' + \
                    '- Localisation :' + \
                  '</h5>' + \
                  '<br>' + \
                  '<h5>' + \
                    'Mes besoins de cautionnement :' + \
                  '</h5>' + \
                  '<br>' + \
                  '<h5>' + \
                    "Organismes d’aide à la création/reprise :" + \
                  '</h5>' + \
                '</div>' + \
              '</div>' + \
              '<br>' + \
              '<div class="card border-dark">' + \
                '<h5 class="card-header border-dark text-center">' + \
                  'Le point sur ma situation' + \
                '</h5>' + \
                '<div class="card-body border-dark">' + \
                  '<div class="card border-dark">' + \
                    '<h5 class="card-header border-dark text-center">' + \
                    '</h5>' + \
                    '<div class="card-body border-dark">' + \
                      '<h5>' + \
                      '</h5>' + \
                    '</div>' + \
                  '</div>' + \
                  '<br>' + \
                  '<div class="card border-dark">' + \
                    '<h5 class="card-header border-dark text-center">' + \
                      "Ma situation familiale : régime matrimonial, nombre d’enfants" + \
                    '</h5>' + \
                    '<div class="card-body border-dark">' + \
                      '<h5>' + \
                      '</h5>' + \
                    '</div>' + \
                  '</div>' + \
                '</div>' + \
              '</div>' + \
              '<br>' + \
              '<div class="card border-dark">' + \
                '<h5 class="card-header border-dark text-center">' + \
                  'Moi (précisions de la répartition de mes biens)' + \
                '</h5>' + \
                '<div class="card-body border-dark">' + \
                  '<h5>' + \
                    'Financier' + \
                  '</h5>' + \
                  '<br>' + \
                  '<table class="table table-striped table-bordered">' + \
                    '<thead>' + \
                      '<tr>' + \
                        '<th scope="col">Patrimoine privé / Détail et valorisation</th>' + \
                        '<th scope="col">Si crédits, capital restant dû</th>' + \
                        '<th scope="col">Mensualités du crédit</th>' + \
                      '</tr>' + \
                    '</thead>' + \
                    '<tbody>' + \
                      '<tr>' + \
                        '<td></td>' + \
                        '<td></td>' + \
                        '<td></td>' + \
                      '</tr>' + \
                    '</tbody>' + \
                  '</table>' + \
                  '<br>' + \
                  '<h5>' + \
                    'Immobilier' + \
                  '</h5>' + \
                  '<br>' + \
                  '<table class="table table-striped table-bordered">' + \
                    '<thead>' + \
                      '<tr>' + \
                        '<th scope="col">Patrimoine privé / Détail et valorisation</th>' + \
                        '<th scope="col">Si crédits, capital restant dû</th>' + \
                        '<th scope="col">Mensualités du crédit</th>' + \
                      '</tr>' + \
                    '</thead>' + \
                    '<tbody>' + \
                      '<tr>' + \
                        '<td></td>' + \
                        '<td></td>' + \
                        '<td></td>' + \
                      '</tr>' + \
                    '</tbody>' + \
                  '</table>' + \
                  '<br>' + \
                  '<h5>' + \
                    'Autres' + \
                  '</h5>' + \
                  '<br>' + \
                  '<table class="table table-striped table-bordered">' + \
                    '<thead>' + \
                      '<tr>' + \
                        '<th scope="col">Patrimoine privé / Détail et valorisation</th>' + \
                        '<th scope="col">Si crédits, capital restant dû</th>' + \
                        '<th scope="col">Mensualités du crédit</th>' + \
                      '</tr>' + \
                    '</thead>' + \
                    '<tbody>' + \
                      '<tr>' + \
                        '<td></td>' + \
                        '<td></td>' + \
                        '<td></td>' + \
                      '</tr>' + \
                    '</tbody>' + \
                  '</table>' + \
                '</div>' + \
              '</div>' + \
              '<br>' + \
              '<div class="card border-dark">' + \
                '<h5 class="card-header border-dark text-center">' + \
                  'Mes associés (avec % de parts significatif)' + \
                '</h5>' + \
                '<div class="card-body border-dark">' + \
                  '<h5>' + \
                    "Je n'ai pas d'associés." + \
                  '</h5>' + \
                '</div>' + \
              '</div>' + \
              '<br>' + \
              '<div class="card border-dark">' + \
                '<h5 class="card-header border-dark text-center">' + \
                  'Mes compétences' + \
                '</h5>' + \
                '<div class="card-body border-dark">' + \
                  '<table class="table table-striped table-bordered">' + \
                    '<thead>' + \
                      '<tr>' + \
                        '<th scope="col">Techniques</th>' + \
                        '<th scope="col">Gestion</th>' + \
                        '<th scope="col">Commerciales</th>' + \
                      '</tr>' + \
                    '</thead>' + \
                    '<tbody>' + \
                      '<tr>' + \
                        '<td></td>' + \
                        '<td></td>' + \
                        '<td></td>' + \
                      '</tr>' + \
                    '</tbody>' + \
                  '</table>' + \
                '</div>' + \
              '</div>' + \
              '<br>' + \
              '<div class="card border-dark">' + \
                '<h5 class="card-header border-dark text-center">' + \
                  'Mes motivations' + \
                '</h5>' + \
                '<div class="card-body border-dark">' + \
                  '<h5>' + \
                  '</h5>' + \
                '</div>' + \
              '</div>' + \
            '</div>' + \
          '</div>' + \
          '<br>' + \
          '<br>' + \
          '<!-- Marché -->' + \
          '<div class="card border-dark">' + \
            '<h5 class="card-header border-dark text-center">' + \
              'Marché' + \
            '</h5>' + \
            '<div class="card-body border-dark text-center">' + \
              '<div class="card border-dark">' + \
                '<h5 class="card-header border-dark text-center">' + \
                  'Marché visé, segmentation' + \
                  '<br>' + \
                '</h5>' + \
                '<div class="card-body border-dark">' + \
                  '<h5>' + \
                  '</h5>' + \
                '</div>' + \
              '</div>' + \
              '<br>' + \
              '<div class="card border-dark">' + \
              '<h5 class="card-header border-dark text-center">' + \
                  'Marché de niche ou très concurrentiel' + \
                  '<br>' + \
                '</h5>' + \
                '<div class="card-body border-dark">' + \
                '<h5>' + \
                  '</h5>' + \
                '</div>' + \
              '</div>' + \
              '<br>' + \
              '<div class="card border-dark">' + \
                '<h5 class="card-header border-dark text-center">' + \
                  'Clientèle potentielle et localisation géographique' + \
                  '<br>' + \
                '</h5>' + \
                '<div class="card-body border-dark">' + \
                  '<h5>' + \
                  '</h5>' + \
                '</div>' + \
              '</div>' + \
              '<br>' + \
              '<div class="card border-dark">' + \
                '<h5 class="card-header border-dark text-center">' + \
                  'Évolution (croissance en nombre, pouvoir d’achat)' + \
                  '<br>' + \
                '</h5>' + \
                '<div class="card-body border-dark">' + \
                  '<h5>' + \
                  '</h5>' + \
                '</div>' + \
              '</div>' + \
              '<br>' + \
              '<div class="card border-dark">' + \
                '<h5 class="card-header border-dark text-center">' + \
                  "Barrière à l’entrée" + \
                  '<br>' + \
                '</h5>' + \
                '<div class="card-body border-dark">' + \
                  '<h5>' + \
                  '</h5>' + \
                '</div>' + \
              '</div>' + \
              '<br>' + \
              '<div class="card border-dark">' + \
                '<h5 class="card-header border-dark text-center">' + \
                  'Concurrence' + \
                  '<br>' + \
                '</h5>' + \
                '<div class="card-body border-dark">' + \
                  '<table class="table table-striped table-bordered">' + \
                    '<thead>' + \
                      '<tr>' + \
                        '<th scope="col">Entreprise</th>' + \
                        '<th scope="col">Localisation</th>' + \
                        '<th scope="col">Type de produit, description</th>' + \
                        '<th scope="col">Chiffre d’affaires</th>' + \
                        '<th scope="col">Image</th>' + \
                        '<th scope="col">Part de marché</th>' + \
                      '</tr>' + \
                    '</thead>' + \
                    '<tbody>' + \
                      '<tr>' + \
                        '<td></td>' + \
                        '<td></td>' + \
                        '<td></td>' + \
                        '<td></td>' + \
                        '<td></td>' + \
                        '<td></td>' + \
                      '</tr>' + \
                      '<tr>' + \
                        '<td></td>' + \
                        '<td></td>' + \
                        '<td></td>' + \
                        '<td></td>' + \
                        '<td></td>' + \
                        '<td></td>' + \
                      '</tr>' + \
                      '<tr>' + \
                        '<td></td>' + \
                        '<td></td>' + \
                        '<td></td>' + \
                        '<td></td>' + \
                        '<td></td>' + \
                        '<td></td>' + \
                      '</tr>' + \
                    '</tbody>' + \
                  '</table>' + \
                '</div>' + \
              '</div>' + \
              '<br>' + \
              '<div class="card border-dark">' + \
                '<h5 class="card-header border-dark text-center">' + \
                  'Positionnement par rapport aux concurrents' + \
                  '<br>' + \
                '</h5>' + \
                '<div class="card-body border-dark">' + \
                  '<h5>' + \
                  '</h5>' + \
                '</div>' + \
              '</div>' + \
              '<br>' + \
              '<div class="card border-dark">' + \
                '<h5 class="card-header border-dark text-center">' + \
                  'Part de marché estimée' + \
                '</h5>' + \
                '<div class="card-body border-dark">' + \
                  '<h5>' + \
                  '</h5>' + \
                '</div>' + \
              '</div>' + \
              '<br>' + \
              '<div class="card border-dark">' + \
                '<h5 class="card-header border-dark text-center">' + \
                  'La demande' + \
                '</h5>' + \
                '<div class="card-body border-dark">' + \
                  '<div class="card border-dark">' + \
                    '<h5 class="card-header border-dark text-center">' + \
                      'Quelles sont les caractéristiques de la demande ? - Le produit/service répond à quels besoins des clients ?' + \
                    '</h5>' + \
                    '<div class="card-body border-dark">' + \
                      '<h5>' + \
                      '</h5>' + \
                    '</div>' + \
                  '</div>' + \
                  '<br>' + \
                  '<div class="card border-dark">' + \
                    '<h5 class="card-header border-dark text-center">' + \
                      'Estimation du nombre de clients, zone de chalandise…' + \
                    '</h5>' + \
                    '<div class="card-body border-dark">' + \
                      '<h5>' + \
                      '</h5>' + \
                    '</div>' + \
                  '</div>' + \
                  '<br>' + \
                  '<div class="card border-dark">' + \
                    '<h5 class="card-header border-dark text-center">' + \
                      '- Tendances de ces dernières années, actuelles et à venir (augmentation, stagnation), modification des attentes…' + \
                    '</h5>' + \
                    '<div class="card-body border-dark">' + \
                      '<h5>' + \
                      '</h5>' + \
                    '</div>' + \
                  '</div>' + \
                  '<br>' + \
                  '<div class="card border-dark">' + \
                    '<h5 class="card-header border-dark text-center">' + \
                      "- Volume de consommation - taux d’équipement" + \
                    '</h5>' + \
                    '<div class="card-body border-dark">' + \
                      '<h5>' + \
                      '</h5>' + \
                    '</div>' + \
                  '</div>' + \
                '</div>' + \
              '</div>' + \
              '<br>' + \
              '<div class="card border-dark">' + \
                '<h5 class="card-header border-dark text-center">' + \
                  "L’environnement" + \
                  '<br>' + \
                '</h5>' + \
                '<div class="card-body border-dark">' + \
                  '<h5>' + \
                  '</h5>' + \
                '</div>' + \
              '</div>' + \
            '</div>' + \
          '</div>' + \
          '<br>' + \
          '<br>' + \
          '<!-- Produits et services -->' + \
          '<div class="card border-dark">' + \
            '<h5 class="card-header border-dark text-center">' + \
              'Produits et services' + \
            '</h5>' + \
            '<div class="card-body border-dark">' + \
              '<div class="card border-dark">' + \
                '<h5 class="card-header border-dark text-center">' + \
                  'Description du ou des produits & services' + \
                  '<br>' + \
                '</h5>' + \
                '<div class="card-body border-dark">' + \
                  '<h6>' + \
                  '</h6>' + \
                '</div>' + \
              '</div>' + \
              '<br>' + \
              '<div class="card border-dark">' + \
                '<h5 class="card-header border-dark text-center">' + \
                  'Avantages concurrentiels' + \
                  '<br>' + \
                '</h5>' + \
                '<div class="card-body border-dark">' + \
                  '<h6>' + \
                  '</h6>' + \
                '</div>' + \
              '</div>' + \
              '<br>' + \
              '<div class="card border-dark">' + \
                '<h5 class="card-header border-dark text-center">' + \
                  'Stade de mise au point' + \
                  '<br>' + \
                '</h5>' + \
                '<div class="card-body border-dark">' + \
                '</div>' + \
              '</div>' + \
              '<br>' + \
              '<div class="card border-dark">' + \
                '<h5 class="card-header border-dark text-center">' + \
                  'Fabrication : conception et développement des produits' + \
                '</h5>' + \
                '<div class="card-body border-dark">' + \
                  '<div class="card border-dark">' + \
                    '<h5 class="card-header border-dark text-center">' + \
                      'En interne, sous-traitance, au coup par coup ?' + \
                    '</h5>' + \
                    '<div class="card-body border-dark">' + \
                      '<h6>' + \
                      '</h6>' + \
                    '</div>' + \
                  '</div>' + \
                  '<br>' + \
                  '<div class="card border-dark">' + \
                    '<h5 class="card-header border-dark text-center">' + \
                      'Moyens nécessaires' + \
                    '</h5>' + \
                    '<div class="card-body border-dark">' + \
                      '<h6>' + \
                      '</h6>' + \
                    '</div>' + \
                  '</div>' + \
                '</div>' + \
              '</div>' + \
              '<br>' + \
              '<div class="card border-dark">' + \
                '<h5 class="card-header border-dark text-center">' + \
                  'Propriété industrielle : Brevet, Marque, Licence' + \
                '</h5>' + \
                '<div class="card-body border-dark">' + \
                  '<h6>' + \
                  '</h6>' + \
                '</div>' + \
              '</div>' + \
              '<br>' + \
              '<div class="card border-dark">' + \
                '<h5 class="card-header border-dark text-center">' + \
                  'Etendue géographique de la couverture de votre brevet' + \
                  '<br>' + \
                '</h5>' + \
                '<div class="card-body border-dark">' + \
                  '<h6>' + \
                  '</h6>' + \
                '</div>' + \
              '</div>' + \
              '<br>' + \
              '<div class="card border-dark">' + \
                '<h5 class="card-header border-dark text-center">' + \
                  'Coût direct de production' + \
                '</h5>' + \
                '<div class="card-body border-dark">' + \
                  '<h6>' + \
                  '</h6>' + \
                '</div>' + \
              '</div>' + \
              '<br>' + \
              '<div class="card border-dark">' + \
                '<h5 class="card-header border-dark text-center">' + \
                  'Prix' + \
                  '<br>' + \
                '</h5>' + \
                '<div class="card-body border-dark">' + \
                  '<h6>' + \
                  '</h6>' + \
                '</div>' + \
              '</div>' + \
            '</div>' + \
          '</div>' + \
          '<br>' + \
          '<br>' + \
          '<!-- Ma stratégie -->' + \
          '<div class="card border-dark">' + \
            '<h5 class="card-header border-dark text-center">' + \
              'Ma stratégie' + \
            '</h5>' + \
            '<div class="card-body border-dark">' + \
              '<div class="card border-dark">' + \
                '<h5 class="card-header border-dark text-center">' + \
                  'Approche marketing' + \
                  '<br>' + \
                '</h5>' + \
                '<div class="card-body border-dark">' + \
                  '<h6>' + \
                  '</h6>' + \
                '</div>' + \
              '</div>' + \
              '<br>' + \
              '<div class="card border-dark">' + \
                '<h5 class="card-header border-dark text-center">' + \
                  'Politique de publicité, promotion, communication' + \
                '</h5>' + \
                '<div class="card-body border-dark">' + \
                  '<div class="card border-dark">' + \
                    '<h5 class="card-header border-dark text-center">' + \
                    '</h5>' + \
                    '<div class="card-body border-dark">' + \
                      '<h6>' + \
                      '</h6>' + \
                    '</div>' + \
                  '</div>' + \
                  '<br>' + \
                  '<div class="card border-dark">' + \
                    '<h5 class="card-header border-dark text-center">' + \
                    '</h5>' + \
                    '<div class="card-body border-dark">' + \
                      '<h6>' + \
                      '</h6>' + \
                      '<br>' + \
                      '<table class="table table-striped table-bordered">' + \
                        '<thead>' + \
                          '<tr>' + \
                            '<th scope="col">Descriptif des actions</th>' + \
                            '<th scope="col">Objectifs des actions</th>' + \
                            '<th scope="col">Coût estimé</th>' + \
                          '</tr>' + \
                        '</thead>' + \
                        '<tbody>' + \
                          '<tr>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                        '</tbody>' + \
                      '</table>' + \
                    '</div>' + \
                  '</div>' + \
                '</div>' + \
              '</div>' + \
              '<br>' + \
              '<div class="card border-dark">' + \
                '<h5 class="card-header border-dark text-center">' + \
                  'Stratégie commerciale' + \
                  '<br>' + \
                '</h5>' + \
                '<div class="card-body border-dark">' + \
                  '<h6>' + \
                  '</h6>' + \
                '</div>' + \
              '</div>' + \
              '<br>' + \
              '<div class="card border-dark">' + \
                '<h5 class="card-header border-dark text-center">' + \
                  'Canaux de distribution' + \
                '</h5>' + \
                '<div class="card-body border-dark">' + \
                  '<div class="card border-dark">' + \
                    '<h5 class="card-header border-dark text-center">' + \
                      'Quel(s) type(s) de moyens de distribution comptez-vous utiliser ?' + \
                      '<br>' + \
                    '</h5>' + \
                    '<div class="card-body border-dark">' + \
                      '<h6>' + \
                      '</h6>' + \
                    '</div>' + \
                  '</div>' + \
                  '<br>' + \
                  '<div class="card border-dark">' + \
                    '<h5 class="card-header border-dark text-center">' + \
                    '</h5>' + \
                    '<div class="card-body border-dark">' + \
                      '<h6>' + \
                      '</h6>' + \
                    '</div>' + \
                  '</div>' + \
                  '<br>' + \
                  '<div class="card border-dark">' + \
                    '<h5 class="card-header border-dark text-center">' + \
                    '</h5>' + \
                    '<div class="card-body border-dark">' + \
                      '<h6>' + \
                      '</h6>' + \
                    '</div>' + \
                  '</div>' + \
                '</div>' + \
              '</div>' + \
              '<br>' + \
              '<div class="card border-dark">' + \
                '<h5 class="card-header border-dark text-center">' + \
                  'Stratégie moyen terme' + \
                  '<br>' + \
                '</h5>' + \
                '<div class="card-body border-dark">' + \
                  '<h6>' + \
                  '</h6>' + \
                '</div>' + \
              '</div>' + \
              '<br>' + \
              '<div class="card border-dark">' + \
                '<h5 class="card-header border-dark text-center">' + \
                  'Planning de démarrage' + \
                '</h5>' + \
                '<div class="card-body border-dark">' + \
                  '<div class="card border-dark">' + \
                    '<h5 class="card-header border-dark text-center">' + \
                      'Implantation immobilière' + \
                    '</h5>' + \
                    '<div class="card-body border-dark">' + \
                      '<h6>' + \
                      '</h6>' + \
                    '</div>' + \
                  '</div>' + \
                  '<br>' + \
                  '<div class="card border-dark">' + \
                    '<h5 class="card-header border-dark text-center">' + \
                      'Acquisitions de matériels' + \
                    '</h5>' + \
                    '<div class="card-body border-dark">' + \
                      '<h6>' + \
                      '</h6>' + \
                    '</div>' + \
                  '</div>' + \
                  '<br>' + \
                  '<div class="card border-dark">' + \
                    '<h5 class="card-header border-dark text-center">' + \
                      'Mobiliers, agencement' + \
                    '</h5>' + \
                    '<div class="card-body border-dark">' + \
                      '<h6>' + \
                      '</h6>' + \
                    '</div>' + \
                  '</div>' + \
                '</div>' + \
              '</div>' + \
              '<br>' + \
              '<div class="card border-dark">' + \
                '<h5 class="card-header border-dark text-center">' + \
                  'Votre équipe' + \
                '</h5>' + \
                '<div class="card-body border-dark">' + \
                  '<div class="card border-dark">' + \
                    '<h5 class="card-header border-dark text-center">' + \
                    '</h5>' + \
                    '<div class="card-body border-dark">' + \
                      '<table class="table table-striped table-bordered">' + \
                        '<thead>' + \
                          '<tr>' + \
                            '<th scope="col">Embauche</th>' + \
                            '<th scope="col">Fonction</th>' + \
                            '<th scope="col">Coût prévisionnel</th>' + \
                          '</tr>' + \
                        '</thead>' + \
                        '<tbody>' + \
                          '<tr>' + \
                            '<td>1ère année</th>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>2ème année</th>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>3ème année</th>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                        '</tbody>' + \
                      '</table>' + \
                    '</div>' + \
                  '</div>' + \
                  '<br>' + \
                  '<div class="card border-dark">' + \
                    '<h5 class="card-header border-dark text-center">' + \
                      'Quelle sera votre organisation ?' + \
                    '</h5>' + \
                    '<div class="card-body border-dark">' + \
                      '<h6>' + \
                      '</h6>' + \
                    '</div>' + \
                  '</div>' + \
                  '<br>' + \
                  '<div class="card border-dark">' + \
                    '<h5 class="card-header border-dark text-center">' + \
                      'Les actions de formations à prévoir' + \
                    '</h5>' + \
                    '<div class="card-body border-dark">' + \
                      '<table class="table table-striped table-bordered">' + \
                        '<thead>' + \
                          '<tr>' + \
                            '<th scope="col">Compétences à acquérir</th>' + \
                            '<th scope="col">Profil</th>' + \
                            '<th scope="col">Coût</th>' + \
                          '</tr>' + \
                        '</thead>' + \
                        '<tbody>' + \
                          '<tr>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                        '</tbody>' + \
                      '</table>' + \
                    '</div>' + \
                  '</div>' + \
                '</div>' + \
              '</div>' + \
              '<br>' + \
              '<div class="card border-dark">' + \
                '<h5 class="card-header border-dark text-center">' + \
                  'Aspect juridique' + \
                  '<br>' + \
                  'Forme juridique de votre entreprise :' + \
                '</h5>' + \
                '<div class="card-body border-dark">' + \
                  '<h6>' + \
                  '</h6>' + \
                '</div>' + \
              '</div>' + \
            '</div>' + \
          '</div>' + \
          '<br>' + \
          '<br>' + \
          '<!-- Données financières -->' + \
          '<div class="card border-dark">' + \
            '<h5 class="card-header border-dark text-center">' + \
              'Données financières' + \
            '</h5>' + \
            '<div class="card-body border-dark">' + \
              '<div class="card border-dark">' + \
                '<h5 class="card-header border-dark text-center">' + \
                  'Prix de vente, coûts, seuil de rentabilité' + \
                '</h5>' + \
                '<div class="card-body border-dark">' + \
                  '<div class="card border-dark">' + \
                    '<h5 class="card-header border-dark text-center">' + \
                      'Explications des hypothèses retenues dans votre compte de résultat prévisionnel' + \
                      '<br>' + \
                    '</h5>' + \
                    '<div class="card-body border-dark">' + \
                      '<h6>' + \
                      '</h6>' + \
                    '</div>' + \
                  '</div>' + \
                  '<br>' + \
                  '<div class="card border-dark">' + \
                    '<h5 class="card-header border-dark text-center">' + \
                      'Détermination du seuil de rentabilité' + \
                      '<br>' + \
                      "Il s’agit ici de trouver le point mort, c'est-à-dire le montant minimal de ventes" + \
                      "qu’il faut impérativement réaliser au cours de l’année d’activité pour au moins pouvoir payer vos charges." + \
                    '</h5>' + \
                    '<div class="card-body border-dark">' + \
                      '<table class="table table-striped table-bordered">' + \
                        '<thead>' + \
                          '<tr>' + \
                            '<th scope="col"></th>' + \
                            '<th scope="col">Année 1</th>' + \
                            '<th scope="col">Année 2</th>' + \
                            '<th scope="col">Année 3</th>' + \
                          '</tr>' + \
                        '</thead>' + \
                        '<tbody>' + \
                          '<tr>' + \
                            "<td>Chiffre d’affaires HT (CA)</td>" + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Charges Variables (CV)</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Charges fixes (CF)</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Total des charges</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Marge sur Coût Variable (MCV) = Valeur (CA HT - CV)</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Taux de MCV ((MCV/CA)*100)</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Seuil de rentabilité – Point Mort (CF/Taux de MCV)</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                        '</tbody>' + \
                      '</table>' + \
                    '</div>' + \
                  '</div>' + \
                '</div>' + \
              '</div>' + \
              '<br>' + \
              '<div class="card border-dark">' + \
                '<h5 class="card-header border-dark text-center">' + \
                  'Activité, CA, marges' + \
                '</h5>' + \
                '<div class="card-body border-dark">' + \
                  '<table class="table table-striped table-bordered">' + \
                    '<thead>' + \
                      '<tr>' + \
                        '<th scope="col"></th>' + \
                        '<th scope="col">Année 1</th>' + \
                        '<th scope="col">Année 2</th>' + \
                        '<th scope="col">Année 3</th>' + \
                      '</tr>' + \
                    '</thead>' + \
                    '<tbody>' + \
                      '<tr class="table-active">' + \
                        '<td>Activité (nombres)</td>' + \
                        '<td></td>' + \
                        '<td></td>' + \
                        '<td></td>' + \
                      '</tr>' + \
                      '<tr>' + \
                        '<td>Produit 1</td>' + \
                        '<td></td>' + \
                        '<td></td>' + \
                        '<td></td>' + \
                      '</tr>' + \
                      '<tr>' + \
                        '<td>Produit 2</td>' + \
                        '<td></td>' + \
                        '<td></td>' + \
                        '<td></td>' + \
                      '</tr>' + \
                      '<tr class="table-active">' + \
                        "<td>Chiffre d'Affaires (HT)</td>" + \
                        '<td></td>' + \
                        '<td></td>' + \
                        '<td></td>' + \
                      '</tr>' + \
                      '<tr>' + \
                        '<td>Produit 1</td>' + \
                        '<td></td>' + \
                        '<td></td>' + \
                        '<td></td>' + \
                      '</tr>' + \
                      '<tr>' + \
                        '<td>Produit 2</td>' + \
                        '<td></td>' + \
                        '<td></td>' + \
                        '<td></td>' + \
                      '</tr>' + \
                      '<tr class="table-active">' + \
                        '<td>Prix de Vente Unitaire Moyen</td>' + \
                        '<td></td>' + \
                        '<td></td>' + \
                        '<td></td>' + \
                      '</tr>' + \
                      '<tr>' + \
                        '<td>Produit 1</td>' + \
                        '<td></td>' + \
                        '<td></td>' + \
                        '<td></td>' + \
                      '</tr>' + \
                      '<tr>' + \
                        '<td>Produit 2</td>' + \
                        '<td></td>' + \
                        '<td></td>' + \
                        '<td></td>' + \
                      '</tr>' + \
                      '<tr class="table-active">' + \
                        '<td>Prix de Revient Unitaire</td>' + \
                        '<td></td>' + \
                        '<td></td>' + \
                        '<td></td>' + \
                      '</tr>' + \
                      '<tr>' + \
                        '<td>Produit 1</td>' + \
                        '<td></td>' + \
                        '<td></td>' + \
                        '<td></td>' + \
                      '</tr>' + \
                      '<tr>' + \
                        '<td>Produit 2</td>' + \
                        '<td></td>' + \
                        '<td></td>' + \
                        '<td></td>' + \
                      '</tr>' + \
                      '<tr class="table-active">' + \
                        '<td>Prix de Revient Global</td>' + \
                        '<td></td>' + \
                        '<td></td>' + \
                        '<td></td>' + \
                      '</tr>' + \
                      '<tr>' + \
                        '<td>Produit 1</td>' + \
                        '<td></td>' + \
                        '<td></td>' + \
                        '<td></td>' + \
                      '</tr>' + \
                      '<tr>' + \
                        '<td>Produit 2</td>' + \
                        '<td></td>' + \
                        '<td></td>' + \
                        '<td></td>' + \
                      '</tr>' + \
                      '<tr class="table-active">' + \
                        '<td>Marge</td>' + \
                        '<td></td>' + \
                        '<td></td>' + \
                        '<td></td>' + \
                      '</tr>' + \
                      '<tr>' + \
                        '<td>Produit 1</td>' + \
                        '<td></td>' + \
                        '<td></td>' + \
                        '<td></td>' + \
                      '</tr>' + \
                      '<tr>' + \
                        '<td>Produit 2</td>' + \
                        '<td></td>' + \
                        '<td></td>' + \
                        '<td></td>' + \
                      '</tr>' + \
                    '</tbody>' + \
                  '</table>' + \
                '</div>' + \
              '</div>' + \
              '<br>' + \
              '<div class="card border-dark">' + \
                '<h5 class="card-header border-dark text-center">' + \
                  'Compte de Résultat Prévisionnel simplifié sur 3 ans' + \
                '</h5>' + \
                '<div class="card-body border-dark">' + \
                  '<table class="table table-striped table-bordered">' + \
                    '<thead>' + \
                      '<tr>' + \
                        '<th scope="col"></th>' + \
                        '<th scope="col">Année 1</th>' + \
                        '<th scope="col">Année 2</th>' + \
                        '<th scope="col">Année 3</th>' + \
                      '</tr>' + \
                    '</thead>' + \
                    '<tbody>' + \
                      '<tr>' + \
                        '<td>1. Ventes de marchandises</td>' + \
                        '<td></td>' + \
                        '<td></td>' + \
                        '<td></td>' + \
                      '</tr>' + \
                      '<tr>' + \
                        '<td>2. Production</td>' + \
                        '<td></td>' + \
                        '<td></td>' + \
                        '<td></td>' + \
                      '</tr>' + \
                      '<tr class="table-active">' + \
                        "<td>Chiffre d'Affaires (CA) (CA = 1+2)</td>" + \
                        '<td></td>' + \
                        '<td></td>' + \
                        '<td></td>' + \
                      '</tr>' + \
                      '<tr>' + \
                        '<td>3. Achats de marchandises et variation de stock</td>' + \
                        '<td></td>' + \
                        '<td></td>' + \
                        '<td></td>' + \
                      '</tr>' + \
                      '<tr class="table-active">' + \
                        '<td>Marge Brute (MB) (MB = CA-3)</td>' + \
                        '<td></td>' + \
                        '<td></td>' + \
                        '<td></td>' + \
                      '</tr>' + \
                      '<tr>' + \
                        '<td>4. Loyer et charges locatives</td>' + \
                        '<td></td>' + \
                        '<td></td>' + \
                        '<td></td>' + \
                      '</tr>' + \
                      '<tr>' + \
                        '<td>5. Honoraires et assurances</td>' + \
                        '<td></td>' + \
                        '<td></td>' + \
                        '<td></td>' + \
                      '</tr>' + \
                      '<tr>' + \
                        '<td>6. Publicité et frais commerciaux</td>' + \
                        '<td></td>' + \
                        '<td></td>' + \
                        '<td></td>' + \
                      '</tr>' + \
                      '<tr>' + \
                        '<td>7. Loyers de crédit bail</td>' + \
                        '<td></td>' + \
                        '<td></td>' + \
                        '<td></td>' + \
                      '</tr>' + \
                      '<tr>' + \
                        '<td>8. Fournitures et autres charges</td>' + \
                        '<td></td>' + \
                        '<td></td>' + \
                        '<td></td>' + \
                      '</tr>' + \
                      '<tr class="table-active">' + \
                        '<td>Valeur Ajoutée (VA) (VA= MB - 4 - 5 - 6 - 7 – 8)</td>' + \
                        '<td></td>' + \
                        '<td></td>' + \
                        '<td></td>' + \
                      '</tr>' + \
                      '<tr>' + \
                        '<td>9. Salaires et charges sociales</td>' + \
                        '<td></td>' + \
                        '<td></td>' + \
                        '<td></td>' + \
                      '</tr>' + \
                      '<tr>' + \
                        '<td>10. Impôts et Taxes</td>' + \
                        '<td></td>' + \
                        '<td></td>' + \
                        '<td></td>' + \
                      '</tr>' + \
                      '<tr class="table-active">' + \
                        "<td>Excédent Brut d'Exploitation (EBE) (EBE= VA - 9 - 10)</td>" + \
                        '<td></td>' + \
                        '<td></td>' + \
                        '<td></td>' + \
                      '</tr>' + \
                      '<tr>' + \
                        '<td>11. Dotations aux amortissements</td>' + \
                        '<td></td>' + \
                        '<td></td>' + \
                        '<td></td>' + \
                      '</tr>' + \
                      '<tr>' + \
                        '<td>12. Dotations aux provisions</td>' + \
                        '<td></td>' + \
                        '<td></td>' + \
                        '<td></td>' + \
                      '</tr>' + \
                      '<tr class="table-active">' + \
                        "<td>Résultats d'Exploitation (RE) (RE = EBE - 11 - 12)</td>" + \
                        '<td></td>' + \
                        '<td></td>' + \
                        '<td></td>' + \
                      '</tr>' + \
                      '<tr>' + \
                        '<td>13. Frais financiers</td>' + \
                        '<td></td>' + \
                        '<td></td>' + \
                        '<td></td>' + \
                      '</tr>' + \
                      '<tr>' + \
                        '<td>14. Produits Financiers</td>' + \
                        '<td></td>' + \
                        '<td></td>' + \
                        '<td></td>' + \
                      '</tr>' + \
                      '<tr class="table-active">' + \
                        '<td>Résultats Courant Avant Impôts (RCAI) - (RCAI = RE - 13 + 14)</td>' + \
                        '<td></td>' + \
                        '<td></td>' + \
                        '<td></td>' + \
                      '</tr>' + \
                      '<tr>' + \
                        '<td>15. Impôts sur les bénéfices</td>' + \
                        '<td></td>' + \
                        '<td></td>' + \
                        '<td></td>' + \
                      '</tr>' + \
                      '<tr>' + \
                        '<td>16. Dividendes</td>' + \
                        '<td></td>' + \
                        '<td></td>' + \
                        '<td></td>' + \
                      '</tr>' + \
                      '<tr class="table-active">' + \
                        '<td>Résultat Net (RN) (RN = RCAI – 15 – 16)</td>' + \
                        '<td></td>' + \
                        '<td></td>' + \
                        '<td></td>' + \
                      '</tr>' + \
                      '<tr class="table-active">' + \
                        "<td>Capacité d'Autofinancement (CAF) (CAF = RN +11 + 12)</td>" + \
                        '<td></td>' + \
                        '<td></td>' + \
                        '<td></td>' + \
                      '</tr>' + \
                    '</tbody>' + \
                  '</table>' + \
                '</div>' + \
              '</div>' + \
              '<br>' + \
              '<div class="card border-dark">' + \
                '<h5 class="card-header border-dark text-center">' + \
                  'Tableau Emplois-Ressources' + \
                '</h5>' + \
                '<div class="card-body border-dark">' + \
                  '<div class="card border-dark">' + \
                    '<h5 class="card-header border-dark text-center">' + \
                      'Mes investissements' + \
                      '<br>' + \
                      'Liste des investissements nécessaires à votre activité :' + \
                    '</h5>' + \
                    '<div class="card-body border-dark">' + \
                      '<table class="table table-striped table-bordered">' + \
                        '<thead>' + \
                          '<tr>' + \
                            '<th scope="col">Description investissement (utilisation…)</th>' + \
                            '<th scope="col">Coût (HT) y compris les frais d' + "'installation</th>" + \
                            '<th scope="col">Durée de vie de l' + "'investissement</th>" + \
                          '</tr>' + \
                        '</thead>' + \
                        '<tbody>' + \
                          '<tr>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                        '</tbody>' + \
                      '</table>' + \
                    '</div>' + \
                  '</div>' + \
                  '<br>' + \
                  '<div class="card border-dark">' + \
                    '<h5 class="card-header border-dark text-center">' + \
                      'Mes ressources' + \
                    '</h5>' + \
                    '<div class="card-body border-dark">' + \
                      '<div class="card border-dark">' + \
                        '<h5 class="card-header border-dark text-center">' + \
                          '1. Apports' + \
                          '<br>' + \
                          'En nature : apport de matériel, local, brevet…' + \
                        '</h5>' + \
                        '<div class="card-body border-dark">' + \
                          '<table class="table table-striped table-bordered">' + \
                            '<thead>' + \
                              '<tr>' + \
                                '<th scope="col">Nature / Commentaires</th>' + \
                                '<th scope="col">Montant</th>' + \
                              '</tr>' + \
                            '</thead>' + \
                            '<tbody>' + \
                              '<tr>' + \
                                '<td></td>' + \
                                '<td></td>' + \
                              '</tr>' + \
                            '</tbody>' + \
                          '</table>' + \
                        '</div>' + \
                      '</div>' + \
                      '<br>' + \
                      '<div class="card border-dark">' + \
                        '<h5 class="card-header border-dark text-center">' + \
                          '1. Apports' + \
                          '<br>' + \
                          'En numéraire :' + \
                        '</h5>' + \
                        '<div class="card-body border-dark">' + \
                          '<table class="table table-striped table-bordered">' + \
                            '<thead>' + \
                              '<tr>' + \
                                '<th scope="col">Nature / Commentaires</th>' + \
                                '<th scope="col">Montant</th>' + \
                              '</tr>' + \
                            '</thead>' + \
                            '<tbody>' + \
                              '<tr>' + \
                                '<td></td>' + \
                                '<td></td>' + \
                              '</tr>' + \
                            '</tbody>' + \
                          '</table>' + \
                        '</div>' + \
                      '</div>' + \
                      '<br>' + \
                      '<div class="card border-dark">' + \
                        '<h5 class="card-header border-dark text-center">' + \
                          '2. Subventions et/ou aides' + \
                        '</h5>' + \
                        '<div class="card-body border-dark">' + \
                          '<table class="table table-striped table-bordered">' + \
                            '<thead>' + \
                              '<tr>' + \
                                '<th scope="col">Organismes</th>' + \
                                '<th scope="col">Types aides</th>' + \
                                '<th scope="col">Montant</th>' + \
                                '<th scope="col">Date de perception</th>' + \
                              '</tr>' + \
                            '</thead>' + \
                            '<tbody>' + \
                              '<tr>' + \
                                '<td></td>' + \
                                '<td></td>' + \
                                '<td></td>' + \
                                '<td></td>' + \
                              '</tr>' + \
                            '</tbody>' + \
                          '</table>' + \
                        '</div>' + \
                      '</div>' + \
                      '<br>' + \
                      '<div class="card border-dark">' + \
                        '<h5 class="card-header border-dark text-center">' + \
                          '3. Emprunts bancaires' + \
                        '</h5>' + \
                        '<div class="card-body border-dark">' + \
                          '<table class="table table-striped table-bordered">' + \
                            '<thead>' + \
                              '<tr>' + \
                                '<th scope="col">Nature</th>' + \
                                '<th scope="col">Montant</th>' + \
                                '<th scope="col">Durée</th>' + \
                                '<th scope="col">Différé</th>' + \
                                '<th scope="col">Amortissements</th>' + \
                              '</tr>' + \
                            '</thead>' + \
                            '<tbody>' + \
                              '<tr>' + \
                                '<td></td>' + \
                                '<td></td>' + \
                                '<td></td>' + \
                                '<td></td>' + \
                                '<td></td>' + \
                              '</tr>' + \
                              '<tr>' + \
                                '<td></td>' + \
                                '<td></td>' + \
                                '<td></td>' + \
                                '<td></td>' + \
                                '<td></td>' + \
                              '</tr>' + \
                              '<tr>' + \
                                '<td></td>' + \
                                '<td></td>' + \
                                '<td></td>' + \
                                '<td></td>' + \
                                '<td></td>' + \
                              '</tr>' + \
                            '</tbody>' + \
                          '</table>' + \
                        '</div>' + \
                      '</div>' + \
                    '</div>' + \
                  '</div>' + \
                  '<br>' + \
                  '<div class="card border-dark">' + \
                    '<h5 class="card-header border-dark text-center">' + \
                      'Le financement de mon activité' + \
                      '<br>' + \
                      '<br>' + \
                      'Afin de déterminer les capitaux dont vous avez besoin, il faut intégrer dans vos prévisions le financement' + \
                      "de votre cycle d’exploitation et de votre cycle commercial." + \
                      "Ce besoin de financement, appelé Besoin en Fonds de Roulement, est lié à la vie de l’entreprise et" + \
                      "provient du décalage entre les dépenses engagées et frais d’installation la 1ère année (achats de matières" + \
                      "premières, de marchandises, frais de fabrication) et la réalisation effective des ventes." + \
                      "Il faut donc aussi financer le stock et les crédits accordés à vos clients et prendre en compte les crédits" + \
                      "que vous accordent vos fournisseurs, permettant de diminuer ce besoin." + \
                      '<br>' + \
                      "Evaluation de votre besoin en fonds de roulement (BFR) : Moyennes calculées en fonction de vos prévisions" + \
                      "de chiffre d’affaires et de délais créances clients et dettes fournisseurs" + \
                      '<br>' + \
                      'Modalité de détermination du BFR :' + \
                    '</h5>' + \
                    '<div class="card-body border-dark">' + \
                      '<table class="table table-striped table-bordered">' + \
                        '<thead>' + \
                          '<tr>' + \
                            '<th scope="col"></th>' + \
                            '<th scope="col">Année 1</th>' + \
                            '<th scope="col">Année 2</th>' + \
                            '<th scope="col">Année 3</th>' + \
                          '</tr>' + \
                        '</thead>' + \
                        '<tbody>' + \
                          '<tr>' + \
                            '<td>Achats consommés + sous traitance en % du CA HT</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Délai moyen de paiement des fournisseurs et sous-traitants en nombre de mois</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            "<td>Stock matières premières en nombre de mois d'achat</td>" + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Stock produits en cours: durée moyenne du cycle de fabrication en nombre de mois</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Stock produits finis en nombre de mois de vente</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Délai moyen de règlement des clients en mois</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                        '</tbody>' + \
                      '</table>' + \
                      '<br>' + \
                      '<table class="table table-striped table-bordered">' + \
                        '<thead>' + \
                          '<tr>' + \
                            '<th scope="col"></th>' + \
                            '<th scope="col">Année 1</th>' + \
                            '<th scope="col">Année 2</th>' + \
                            '<th scope="col">Année 3</th>' + \
                          '</tr>' + \
                        '</thead>' + \
                        '<tbody>' + \
                          '<tr class="table-active">' + \
                            '<td>RESSOURCES</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Fournisseurs TTC</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Accomptes clients TTC</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr class="table-info">' + \
                            '<td>1. TOTAL RESSOURCES</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr class="table-active">' + \
                            '<td>EMPLOIS</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Stock matières</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Produits en cours</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Produits finis</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr class="table-success">' + \
                            '<td>Total stock HT (encours moyen)</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr class="table-success">' + \
                            '<td>Clients TTC (encours moyen)</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr class="table-info">' + \
                            '<td>2. TOTAL EMPLOIS</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr class="table-active">' + \
                            '<td>BESOINS EN FONDS DE ROULEMENT (2-1)</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                        '</tbody>' + \
                      '</table>' + \
                      '<br>' + \
                      '<h6>' + \
                      '</h6>' + \
                    '</div>' + \
                  '</div>' + \
                  '<br>' + \
                  '<div class="card border-dark">' + \
                    '<h5 class="card-header border-dark text-center">' + \
                      'Plan de financement à 3 ans : Tableau Emplois/Ressources' + \
                    '</h5>' + \
                    '<div class="card-body border-dark">' + \
                      '<table class="table table-striped table-bordered">' + \
                        '<thead>' + \
                          '<tr>' + \
                            '<th scope="col"></th>' + \
                            '<th scope="col">Année 1</th>' + \
                            '<th scope="col">Année 2</th>' + \
                            '<th scope="col">Année 3</th>' + \
                          '</tr>' + \
                        '</thead>' + \
                        '<tbody>' + \
                          '<tr class="table-active">' + \
                            '<td>EMPLOIS</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr class="table-success">' + \
                            '<td>Immobilisations incorporelles HT</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Frais de premier établissement</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Recherche et développement</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Fonds de commerce</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Droit au bail</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr class="table-success">' + \
                            '<td>Immobilisations corporelles HT</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Terrains</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Bâtiments</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Frais installation et aménagements</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Matériel informatique et outillage</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Matériel de bureau et mobilier</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr class="table-success">' + \
                            '<td>Immobilisations financières</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr class="table-success">' + \
                            '<td>Besoin en fonds de roulement An 1</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr class="table-success">' + \
                            '<td>Variations du BFR An 2 et An 3</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr class="table-success">' + \
                            '<td>Distribution de dividendes</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr class="table-success">' + \
                            '<td>Remboursement emprunts (capital)</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr class="table-info">' + \
                            '<td>TOTAL DES BESOINS</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr class="table-active">' + \
                            '<td>RESSOURCES</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr class="table-success">' + \
                            '<td>Capitaux propres</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>En nature</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>En numéraire</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr class="table-success">' + \
                            '<td>Subventions équipement</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr class="table-success">' + \
                            '<td>Comptes courants associés</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr class="table-success">' + \
                            '<td>Emprunt bancaire à MLT</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr class="table-success">' + \
                            '<td>Concours bancaire à court terme</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr class="table-success">' + \
                            '<td>Capacité autofinancement</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr class="table-info">' + \
                            '<td>TOTAL DES RESSOURCES</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr class="table-active">' + \
                            '<td>DIFFERENCES ANNUELLES</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr class="table-active">' + \
                            '<td>DIFFERENCES CUMULEES</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                        '</tbody>' + \
                      '</table>' + \
                    '</div>' + \
                  '</div>' + \
                  '<br>' + \
                  '<div class="card border-dark">' + \
                    '<h5 class="card-header border-dark text-center">' + \
                      'Mon plan de trésorerie' + \
                    '</h5>' + \
                    '<div class="card-body border-dark">' + \
                      '<h6>' + \
                        'Premier trimestre' + \
                      '</h6>' + \
                      '<br>' + \
                      '<table class="table table-striped table-bordered">' + \
                        '<thead>' + \
                          '<tr>' + \
                            '<th scope="col"></th>' + \
                            '<th scope="col">Janvier</th>' + \
                            '<th scope="col">Février</th>' + \
                            '<th scope="col">Mars</th>' + \
                          '</tr>' + \
                        '</thead>' + \
                        '<tbody>' + \
                          '<tr class="table-active">' + \
                            '<td>Solde début</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr class="table-active">' + \
                            '<td>ENCAISSEMENTS</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Clients</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Encaissement TVA</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Remboursement CIR</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Apports capitaux</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Emprunts</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Apports Perso C/C</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>actes accomplis C/C</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Subventions</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr class="table-info">' + \
                            '<td>TOTAL ENCAISSEMENTS</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr class="table-active">' + \
                            '<td>DECAISSEMENTS</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Eau, Electricité</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Fournitures entretien</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Fournitures administratives</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Autres matières & fournitures</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Locations immobiliéres</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Locations logiciels</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Entretien et réparations</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Assurances</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Documentations</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Rému. intermédiaires So.</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Honoraires</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Frais actes et contentieux</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Publicité</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Voyages et déplacements</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Missions & réceptions</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Frais PTT</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Services bancaires</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Cotisations</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>TVA</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Impôts et taxes</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Appointements Nets</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Charges sociales</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Autres ch. de personnel</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Redevances</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Ch. Div. Gest. Courants</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Intérêts emprunts</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Intérêts Comptes Courants</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Intérêts /concours bancaires CT</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Remboursements Emprunts</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Remboursements Compte courant</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Impôts sur les sociétés</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Fourniss. Immob</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Caution locaux</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr class="table-success">' + \
                            '<td>Concours bancaire à court terme</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr class="table-success">' + \
                            '<td>Capacité autofinancement</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr class="table-info">' + \
                            '<td>TOTAL DECAISSEMENTS</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr class="table-active">' + \
                            '<td>SOLDE FIN</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                        '</tbody>' + \
                      '</table>' + \
                      '<br>' + \
                      '<br>' + \
                      '<h6>' + \
                        'Deuxième trimestre' + \
                      '</h6>' + \
                      '<br>' + \
                      '<table class="table table-striped table-bordered">' + \
                        '<thead>' + \
                          '<tr>' + \
                            '<th scope="col"></th>' + \
                            '<th scope="col">Avril</th>' + \
                            '<th scope="col">Mai</th>' + \
                            '<th scope="col">Juin</th>' + \
                          '</tr>' + \
                        '</thead>' + \
                        '<tbody>' + \
                          '<tr class="table-active">' + \
                            '<td>Solde début</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr class="table-active">' + \
                            '<td>ENCAISSEMENTS</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Clients</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Encaissement TVA</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Remboursement CIR</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Apports capitaux</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Emprunts</td>' + \
                            '<td></td' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Apports Perso C/C</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>actes accomplis C/C</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Subventions</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr class="table-info">' + \
                            '<td>TOTAL ENCAISSEMENTS</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr class="table-active">' + \
                            '<td>DECAISSEMENTS</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Eau, Electricité</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Fournitures entretien</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Fournitures administratives</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Autres matières & fournitures</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Locations immobiliéres</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Locations logiciels</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Entretien et réparations</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Assurances</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Documentations</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Rému. intermédiaires So.</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Honoraires</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Frais actes et contentieux</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Publicité</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Voyages et déplacements</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Missions & réceptions</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Frais PTT</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Services bancaires</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Cotisations</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>TVA</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Impôts et taxes</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Appointements Nets</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Charges sociales</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Autres ch. de personnel</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Redevances</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Ch. Div. Gest. Courants</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Intérêts emprunts</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Intérêts Comptes Courants</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Intérêts /concours bancaires CT</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Remboursements Emprunts</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Remboursements Compte courant</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Impôts sur les sociétés</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Fourniss. Immob</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Caution locaux</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr class="table-success">' + \
                            '<td>Concours bancaire à court terme</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr class="table-success">' + \
                            '<td>Capacité autofinancement</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr class="table-info">' + \
                            '<td>TOTAL DECAISSEMENTS</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr class="table-active">' + \
                            '<td>SOLDE FIN</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                        '</tbody>' + \
                      '</table>' + \
                      '<br>' + \
                      '<br>' + \
                      '<h6>' + \
                        'Troisième trimestre' + \
                      '</h6>' + \
                      '<br>' + \
                      '<table class="table table-striped table-bordered">' + \
                        '<thead>' + \
                          '<tr>' + \
                            '<th scope="col"></th>' + \
                            '<th scope="col">Juillet</th>' + \
                            '<th scope="col">Août</th>' + \
                            '<th scope="col">Septembre</th>' + \
                          '</tr>' + \
                        '</thead>' + \
                        '<tbody>' + \
                          '<tr class="table-active">' + \
                            '<td>Solde début</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr class="table-active">' + \
                            '<td>ENCAISSEMENTS</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Clients</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Encaissement TVA</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Remboursement CIR</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Apports capitaux</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Emprunts</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Apports Perso C/C</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>actes accomplis C/C</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Subventions</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr class="table-info">' + \
                            '<td>TOTAL ENCAISSEMENTS</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr class="table-active">' + \
                            '<td>DECAISSEMENTS</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Eau, Electricité</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Fournitures entretien</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Fournitures administratives</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Autres matières & fournitures</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Locations immobiliéres</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Locations logiciels</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Entretien et réparations</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Assurances</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Documentations</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Rému. intermédiaires So.</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Honoraires</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Frais actes et contentieux</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Publicité</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Voyages et déplacements</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Missions & réceptions</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Frais PTT</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Services bancaires</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Cotisations</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>TVA</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Impôts et taxes</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Appointements Nets</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Charges sociales</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Autres ch. de personnel</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Redevances</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Ch. Div. Gest. Courants</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Intérêts emprunts</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Intérêts Comptes Courants</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Intérêts /concours bancaires CT</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Remboursements Emprunts</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Remboursements Compte courant</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Impôts sur les sociétés</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Fourniss. Immob</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Caution locaux</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr class="table-success">' + \
                            '<td>Concours bancaire à court terme</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr class="table-success">' + \
                            '<td>Capacité autofinancement</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr class="table-info">' + \
                            '<td>TOTAL DECAISSEMENTS</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr class="table-active">' + \
                            '<td>SOLDE FIN</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                        '</tbody>' + \
                      '</table>' + \
                      '<br>' + \
                      '<br>' + \
                      '<h6>' + \
                        'Quatrième trimestre' + \
                      '</h6>' + \
                      '<br>' + \
                      '<table class="table table-striped table-bordered">' + \
                        '<thead>' + \
                          '<tr>' + \
                            '<th scope="col"></th>' + \
                            '<th scope="col">Octobre</th>' + \
                            '<th scope="col">Novembre</th>' + \
                            '<th scope="col">Décembre</th>' + \
                          '</tr>' + \
                        '</thead>' + \
                        '<tbody>' + \
                          '<tr class="table-active">' + \
                            '<td>Solde début</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr class="table-active">' + \
                            '<td>ENCAISSEMENTS</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Clients</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Encaissement TVA</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Remboursement CIR</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Apports capitaux</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Emprunts</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Apports Perso C/C</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>actes accomplis C/C</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Subventions</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr class="table-info">' + \
                            '<td>TOTAL ENCAISSEMENTS</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr class="table-active">' + \
                            '<td>DECAISSEMENTS</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Eau, Electricité</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Fournitures entretien</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Fournitures administratives</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Autres matières & fournitures</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Locations immobiliéres</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Locations logiciels</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Entretien et réparations</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Assurances</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Documentations</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Rému. intermédiaires So.</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Honoraires</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Frais actes et contentieux</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Publicité</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Voyages et déplacements</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Missions & réceptions</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Frais PTT</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Services bancaires</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Cotisations</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>TVA</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Impôts et taxes</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Appointements Nets</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Charges sociales</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Autres ch. de personnel</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Redevances</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Ch. Div. Gest. Courants</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Intérêts emprunts</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Intérêts Comptes Courants</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Intérêts /concours bancaires CT</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Remboursements Emprunts</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Remboursements Compte courant</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Impôts sur les sociétés</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Fourniss. Immob</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr>' + \
                            '<td>Caution locaux</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr class="table-success">' + \
                            '<td>Concours bancaire à court terme</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr class="table-success">' + \
                            '<td>Capacité autofinancement</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr class="table-info">' + \
                            '<td>TOTAL DECAISSEMENTS</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                          '<tr class="table-active">' + \
                            '<td>SOLDE FIN</td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                            '<td></td>' + \
                          '</tr>' + \
                        '</tbody>' + \
                      '</table>' + \
                    '</div>' + \
                  '</div>' + \
                  '<br>' + \
                  '<div class="card border-dark">' + \
                    '<h5 class="card-header border-dark text-center">' + \
                      'Vérification équilibre de vos prévisionnels' + \
                    '</h5>' + \
                    '<div class="card-body border-dark">' + \
                      '<div class="card border-dark">' + \
                        '<h5 class="card-header border-dark text-center">' + \
                          'Equilibre financier de votre projet' + \
                          '<br>' + \
                          'Pour vous donner toutes les chances de réussir, il est préférable de vérifier un principe simple de gestion : ' + \
                          'Le financement de vos investissements est-il assuré par des ressources correspondantes ? ' + \
                          '<br>' + \
                          'Calcul du fonds de roulement (Financement stables – emplois stables) :' + \
                        '</h5>' + \
                        '<div class="card-body border-dark">' + \
                          '<h6>' + \
                          '</h6>' + \
                        '</div>' + \
                      '</div>' + \
                      '<br>' + \
                      '<div class="card border-dark">' + \
                        '<h5 class="card-header border-dark text-center">' + \
                          'La différence entre votre Fonds de roulement et votre besoin en fonds de roulement donne ainsi' + \
                          'le niveau de votre trésorerie.' + \
                          '<br>' + \
                          'Calcul de votre trésorerie prévisionnelle (FR – BFR)' + \
                        '</h5>' + \
                        '<div class="card-body border-dark">' + \
                          '<h6>' + \
                          '</h6>' + \
                          '<br>' + \
                          '<br>' + \
                          '<h6>' + \
                            'Si votre solde de trésorerie est négatif, vous pouvez augmenter les ressources' + \
                            'stables (apports personnels et/ou emprunts long terme), diminuer vos investissements' + \
                            'ou influer sur votre cycle de production et/ou votre cycle commercial (négociation de délais de règlement…).' + \
                          '</h6>' + \
                        '</div>' + \
                      '</div>' + \
                      '<br>' + \
                      '<div class="card border-dark">' + \
                        '<h5 class="card-header border-dark text-center">' + \
                          'Rentabilité prévue de votre activité' + \
                          '<br>' + \
                          'La capacité d’autofinancement : Elle représente les ressources supplémentaires disponibles dues' + \
                          'à votre activité, c’est donc votre capacité à investir et à rembourser vos emprunts.' + \
                          'Calcul simplifié de votre capacité d’autofinancement (CAF) (Bénéfice net après impôt ' + \
                          'dotations aux amortissements et provisions – reprises)' + \
                        '</h5>' + \
                        '<div class="card-body border-dark">' + \
                          '<h6>' + \
                          '</h6>' + \
                        '</div>' + \
                      '</div>' + \
                      '<br>' + \
                      '<div class="card border-dark">' + \
                        '<h5 class="card-header border-dark text-center">' + \
                          'La rentabilité exploitation : Elle vous permettra de connaître évolution de votre' + \
                          'rentabilité et de comparer vos prévisionnels aux normes de votre secteur d’activité.' + \
                          '<br>' + \
                          'Calcul de votre rentabilité d’exploitation (CAF / valeur ajoutée)' + \
                        '</h5>' + \
                        '<div class="card-body border-dark">' + \
                          '<h6>' + \
                          '</h6>' + \
                        '</div>' + \
                      '</div>' + \
                    '</div>' + \
                  '</div>' + \
                  '<br>' + \
                  '<div class="card border-dark">' + \
                    '<h5 class="card-header border-dark text-center">' + \
                      'Tableau récapitulatif des besoins et moyens de financement' + \
                    '</h5>' + \
                    '<div class="card-body border-dark">' + \
                      '<div class="card border-dark">' + \
                        '<h5 class="card-header border-dark text-center">' + \
                          'Pour les investissements' + \
                        '</h5>' + \
                        '<div class="card-body border-dark">' + \
                          '<table class="table table-striped table-bordered">' + \
                            '<thead>' + \
                              '<tr>' + \
                                '<th scope="col">Utilisation</th>' + \
                                '<th scope="col">Coût de l’investissement</th>' + \
                                '<th scope="col">Montant des prêts sollicités</th>' + \
                                '<th scope="col">Durée souhaitée</th>' + \
                              '</tr>' + \
                            '</thead>' + \
                            '<tbody>' + \
                              '<tr>' + \
                                '<td>Immobilier</td>' + \
                                '<td></td>' + \
                                '<td></td>' + \
                                '<td></td>' + \
                              '</tr>' + \
                              '<tr>' + \
                                '<td>Achat de fonds de commerce</td>' + \
                                '<td></td>' + \
                                '<td></td>' + \
                                '<td></td>' + \
                              '</tr>' + \
                              '<tr>' + \
                                '<td>Matériels industriels</td>' + \
                                '<td></td>' + \
                                '<td></td>' + \
                                '<td></td>' + \
                              '</tr>' + \
                              '<tr>' + \
                                '<td>Véhicules</td>' + \
                                '<td></td>' + \
                                '<td></td>' + \
                                '<td></td>' + \
                              '</tr>' + \
                              '<tr>' + \
                                '<td>Autres</td>' + \
                                '<td></td>' + \
                                '<td></td>' + \
                                '<td></td>' + \
                              '</tr>' + \
                            '</tbody>' + \
                          '</table>' + \
                        '</div>' + \
                      '</div>' + \
                      '<br>' + \
                      '<div class="card border-dark">' + \
                        '<h5 class="card-header border-dark text-center">' + \
                          'Pour la gestion quotidienne' + \
                        '</h5>' + \
                        '<div class="card-body border-dark">' + \
                          '<table class="table table-striped table-bordered">' + \
                            '<thead>' + \
                              '<tr>' + \
                                '<th scope="col">Types de financement court terme</th>' + \
                                '<th scope="col">Montant demandé</th>' + \
                              '</tr>' + \
                            '</thead>' + \
                            '<tbody>' + \
                              '<tr>' + \
                                '<td></td>' + \
                                '<td></td>' + \
                              '</tr>' + \
                              '<tr>' + \
                                '<td></td>' + \
                                '<td></td>' + \
                              '</tr>' + \
                              '<tr>' + \
                                '<td></td>' + \
                                '<td></td>' + \
                              '</tr>' + \
                              '<tr>' + \
                                '<td></td>' + \
                                '<td></td>' + \
                              '</tr>' + \
                            '</tbody>' + \
                          '</table>' + \
                        '</div>' + \
                      '</div>' + \
                      '<br>' + \
                      '<div class="card border-dark">' + \
                        '<h5 class="card-header border-dark text-center">' + \
                          'Pour un cautionnement bancaire' + \
                        '</h5>' + \
                        '<div class="card-body border-dark">' + \
                          '<table class="table table-striped table-bordered">' + \
                            '<thead>' + \
                              '<tr>' + \
                                '<th scope="col">Type de cautionnement</th>' + \
                                '<th scope="col">Montant</th>' + \
                                '<th scope="col">Bénéficiaires</th>' + \
                              '</tr>' + \
                            '</thead>' + \
                            '<tbody>' + \
                              '<tr>' + \
                                '<td></td>' + \
                                '<td></td>' + \
                                '<td></td>' + \
                              '</tr>' + \
                            '</tbody>' + \
                          '</table>' + \
                        '</div>' + \
                      '</div>' + \
                    '</div>' + \
                  '</div>' + \
                  '<br>' + \
                  '<div class="card border-dark">' + \
                    '<h5 class="card-header border-dark text-center">' + \
                      'Garanties proposées' + \
                      '<br>' + \
                      'Selon les montants sollicités, votre apport, la nature du projet, des garanties vous seront demandées :' + \
                      'caution solidaire, nantissement de titres, intervention d’une société de cautionnement, mutuel…' + \
                      'Avez-vous prévu cet aspect de votre dossier et quelles sont les garanties que vous pourriez apporter ?' + \
                    '</h5>' + \
                    '<div class="card-body border-dark">' + \
                      '<h6>' + \
                      '</h6>' + \
                    '</div>' + \
                  '</div>' + \
                  '<br>' + \
                  '<div class="card border-dark">' + \
                    '<h5 class="card-header border-dark text-center">' + \
                      'Mes autres besoins' + \
                    '</h5>' + \
                    '<div class="card-body border-dark">' + \
                      '<div class="card border-dark">' + \
                        '<h5 class="card-header border-dark text-center">' + \
                          'Gestion quotidienne' + \
                        '</h5>' + \
                        '<div class="card-body border-dark">' + \
                          '<table class="table table-striped table-bordered">' + \
                            '<thead>' + \
                              '<tr>' + \
                                '<th scope="col">Mes besoins</th>' + \
                                '<th scope="col">Mes solutions</th>' + \
                              '</tr>' + \
                            '</thead>' + \
                            '<tbody>' + \
                              '<tr class="table-active">' + \
                                '<td>Encaisser votre chiffre d’affaires</td>' + \
                                '<td></td>' + \
                              '</tr>' + \
                              '<tr>' + \
                                '<td>Encaisser des chèques</td>' + \
                                '<td></td>' + \
                              '</tr>' + \
                              '<tr>' + \
                                '<td>Encaisser des effets</td>' + \
                                '<td></td>' + \
                              '</tr>' + \
                              '<tr>' + \
                                '<td>Encaisser des espèces</td>' + \
                                '<td></td>' + \
                              '</tr>' + \
                              '<tr>' + \
                                '<td>Encaisser des paiements par carte bancaire</td>' + \
                                '<td></td>' + \
                              '</tr>' + \
                              '<tr class="table-active">' + \
                                '<td>Régler vos dépenses</td>' + \
                                '<td></td>' + \
                              '</tr>' + \
                              '<tr>' + \
                                '<td>Achats stratégiques</td>' + \
                                '<td></td>' + \
                              '</tr>' + \
                              '<tr>' + \
                                '<td>Dépenses courantes</td>' + \
                                '<td></td>' + \
                              '</tr>' + \
                              '<tr class="table-active">' + \
                                '<td>Gérer ses comptes</td>' + \
                                '<td></td>' + \
                              '</tr>' + \
                              '<tr>' + \
                                '<td>Internet</td>' + \
                                '<td></td>' + \
                              '</tr>' + \
                              '<tr>' + \
                                '<td>Télétransmission</td>' + \
                                '<td></td>' + \
                              '</tr>' + \
                              '<tr>' + \
                                '<td>Téléphone</td>' + \
                                '<td></td>' + \
                              '</tr>' + \
                              '<tr class="table-active">' + \
                                '<td>Optimisation de la trésorerie</td>' + \
                                '<td></td>' + \
                              '</tr>' + \
                              '<tr>' + \
                                '<td>Besoin de crédit Court Terme</td>' + \
                                '<td></td>' + \
                              '</tr>' + \
                              '<tr>' + \
                                '<td>Excédent de trésorerie</td>' + \
                                '<td></td>' + \
                              '</tr>' + \
                            '</tbody>' + \
                          '</table>' + \
                        '</div>' + \
                      '</div>' + \
                      '<br>' + \
                      '<div class="card border-dark">' + \
                        '<h5 class="card-header border-dark text-center">' + \
                          "S’assurer" + \
                        '</h5>' + \
                        '<div class="card-body border-dark">' + \
                          '<table class="table table-striped table-bordered">' + \
                            '<thead>' + \
                              '<tr>' + \
                                '<th scope="col">Mes besoins</th>' + \
                                '<th scope="col">Mes solutions</th>' + \
                              '</tr>' + \
                            '</thead>' + \
                            '<tbody>' + \
                              '<tr>' + \
                                "<td>S'assurer à titre professionnel</td>" + \
                                '<td></td>' + \
                              '</tr>' + \
                              '<tr>' + \
                                "<td>S'assurer à titre privé</td>" + \
                                '<td></td>' + \
                              '</tr>' + \
                              '<tr>' + \
                                '<td>Couvrir ses dépenses de santé</td>' + \
                                '<td></td>' + \
                              '</tr>' + \
                              '<tr>' + \
                                '<td>Garantir sa famille</td>' + \
                                '<td></td>' + \
                              '</tr>' + \
                            '</tbody>' + \
                          '</table>' + \
                        '</div>' + \
                      '</div>' + \
                      '<br>' + \
                      '<div class="card border-dark">' + \
                        '<h5 class="card-header border-dark text-center">' + \
                          "Bénéficier d’outils de rémunération fiscalement avantageux" + \
                        '</h5>' + \
                        '<div class="card-body border-dark">' + \
                          '<table class="table table-striped table-bordered">' + \
                            '<thead>' + \
                              '<tr>' + \
                                '<th scope="col">Besoins</th>' + \
                                '<th scope="col">Type de produits</th>' + \
                              '</tr>' + \
                            '</thead>' + \
                            '<tbody>' + \
                              '<tr>' + \
                                '<td>Motiver ses salariés et se rémunérer</td>' + \
                                '<td></td>' + \
                              '</tr>' + \
                              '<tr>' + \
                                '<td>Constituer sa retraite</td>' + \
                                '<td></td>' + \
                              '</tr>' + \
                            '</tbody>' + \
                          '</table>' + \
                        '</div>' + \
                      '</div>' + \
                    '</div>' + \
                  '</div>' + \
                '</div>' + \
              '</div>' + \
              '<br>' + \
              '<div class="card border-dark">' + \
                '<h5 class="card-header border-dark text-center">' + \
                  'Etat avancement du projet' + \
                '</h5>' + \
                '<div class="card-body border-dark">' + \
                  '<div class="card border-dark">' + \
                    '<h5 class="card-header border-dark text-center">' + \
                      'Démarches administratives' + \
                    '</h5>' + \
                    '<div class="card-body border-dark">' + \
                      '<div class="card border-dark">' + \
                        '<h5 class="card-header border-dark text-center">' + \
                          'Immatriculation' + \
                        '</h5>' + \
                        '<div class="card-body border-dark">' + \
                          '<h6>' + \
                          '</h6>' + \
                        '</div>' + \
                      '</div>' + \
                      '<br>' + \
                      '<div class="card border-dark">' + \
                        '<h5 class="card-header border-dark text-center">' + \
                          'Autres : Dépôt de nom…' + \
                        '</h5>' + \
                        '<div class="card-body border-dark">' + \
                          '<h6>' + \
                          '</h6>' + \
                        '</div>' + \
                      '</div>' + \
                    '</div>' + \
                  '</div>' + \
                  '<br>' + \
                  '<div class="card border-dark">' + \
                    '<h5 class="card-header border-dark text-center">' + \
                      'Démarches commerciales' + \
                    '</h5>' + \
                    '<div class="card-body border-dark">' + \
                      '<div class="card border-dark">' + \
                        '<h5 class="card-header border-dark text-center">' + \
                          'Clients, fournisseurs, franchiseurs, prescripteurs' + \
                        '</h5>' + \
                        '<div class="card-body border-dark">' + \
                          '<h6>' + \
                          '</h6>' + \
                        '</div>' + \
                      '</div>' + \
                      '<br>' + \
                      '<div class="card border-dark">' + \
                        '<h5 class="card-header border-dark text-center">' + \
                          'Local, bâtiment, négociation de rachat' + \
                        '</h5>' + \
                        '<div class="card-body border-dark">' + \
                          '<h6>' + \
                          '</h6>' + \
                        '</div>' + \
                      '</div>' + \
                      '<br>' + \
                      '<div class="card border-dark">' + \
                        '<h5 class="card-header border-dark text-center">' + \
                          'Création de support de communication' + \
                        '</h5>' + \
                        '<div class="card-body border-dark">' + \
                          '<h6>' + \
                          '</h6>' + \
                        '</div>' + \
                      '</div>' + \
                    '</div>' + \
                  '</div>' + \
                  '<br>' + \
                  '<div class="card border-dark">' + \
                    '<h5 class="card-header border-dark text-center">' + \
                      'Démarches de recherche de financement' + \
                    '</h5>' + \
                    '<div class="card-body border-dark">' + \
                      '<div class="card border-dark">' + \
                        '<h5 class="card-header border-dark text-center">' + \
                          'Auprès des banquiers' + \
                        '</h5>' + \
                        '<div class="card-body border-dark">' + \
                          '<table class="table table-striped table-bordered">' + \
                            '<thead>' + \
                              '<tr>' + \
                                '<th scope="col">Qui ?</th>' + \
                                '<th scope="col">Quelles demandes ?</th>' + \
                                '<th scope="col">Quels résultats</th>' + \
                              '</tr>' + \
                            '</thead>' + \
                            '<tbody>' + \
                              '<tr>' + \
                                '<td></td>' + \
                                '<td></td>' + \
                                '<td></td>' + \
                              '</tr>' + \
                            '</tbody>' + \
                          '</table>' + \
                        '</div>' + \
                      '</div>' + \
                      '<br>' + \
                      '<div class="card border-dark">' + \
                        '<h5 class="card-header border-dark text-center">' + \
                          'Auprès d’organismes d’aides' + \
                        '</h5>' + \
                        '<div class="card-body border-dark">' + \
                          '<table class="table table-striped table-bordered">' + \
                            '<thead>' + \
                              '<tr>' + \
                                '<th scope="col">Qui ?</th>' + \
                                '<th scope="col">Quelles demandes ?</th>' + \
                                '<th scope="col">Quels résultats</th>' + \
                              '</tr>' + \
                            '</thead>' + \
                            '<tbody>' + \
                              '<tr>' + \
                                '<td></td>' + \
                                '<td></td>' + \
                                '<td></td>' + \
                              '</tr>' + \
                            '</tbody>' + \
                          '</table>' + \
                        '</div>' + \
                      '</div>' + \
                      '<br>' + \
                      '<div class="card border-dark">' + \
                        '<h5 class="card-header border-dark text-center">' + \
                          'Participation à des concours de créateurs' + \
                        '</h5>' + \
                        '<div class="card-body border-dark">' + \
                          '<table class="table table-striped table-bordered">' + \
                            '<thead>' + \
                              '<tr>' + \
                                '<th scope="col">Qui ?</th>' + \
                                '<th scope="col">Quelles demandes ?</th>' + \
                                '<th scope="col">Quels résultats</th>' + \
                              '</tr>' + \
                            '</thead>' + \
                            '<tbody>' + \
                              '<tr>' + \
                                '<td></td>' + \
                                '<td></td>' + \
                                '<td></td>' + \
                              '</tr>' + \
                            '</tbody>' + \
                          '</table>' + \
                        '</div>' + \
                      '</div>' + \
                    '</div>' + \
                  '</div>' + \
                '</div>' + \
              '</div>' + \
              '<br>' + \
              '<div class="card border-dark">' + \
                '<h5 class="card-header border-dark text-center">' + \
                  'Pièces à joindre au dossier' + \
                  '<br>' + \
                  'Pour répondre à votre projet dans les meilleurs délais, nous avons besoin des documents listés ci-après.' + \
                '</h5>' + \
                '<div class="card-body border-dark">' + \
                  '<h6>' + \
                    'Pour tous les projets d’installation' + \
                  '</h6>' + \
                  '<br>' + \
                  '<table class="table table-striped table-bordered">' + \
                    '<thead>' + \
                      '<tr>' + \
                        '<th scope="col">Documents</th>' + \
                        '<th scope="col">Disponible ?</th>' + \
                      '</tr>' + \
                    '</thead>' + \
                    '<tbody>' + \
                      '<tr>' + \
                        '<td>Prévisionnel sur 3 ans (compte de résultat, plan de financement, tableau de trésorerie)</td>' + \
                        '<td></td>' + \
                      '</tr>' + \
                      '<tr>' + \
                        '<td>Statuts ou projet de statuts</td>' + \
                        '<td></td>' + \
                      '</tr>' + \
                      '<tr>' + \
                        '<td>K Bis provisoire ou définitif *</td>' + \
                        '<td></td>' + \
                      '</tr>' + \
                      '<tr>' + \
                        '<td>Curriculum Vitae du/des porteurs du projet</td>' + \
                        '<td></td>' + \
                      '</tr>' + \
                      '<tr>' + \
                        '<td>Justificatif de apport personnel</td>' + \
                        '<td></td>' + \
                      '</tr>' + \
                      '<tr>' + \
                        '<td>Devis ou factures pro forma éventuels</td>' + \
                        '<td></td>' + \
                      '</tr>' + \
                      '<tr>' + \
                        '<td>Bail commercial (ou projet de bail) **</td>' + \
                        '<td></td>' + \
                      '</tr>' + \
                    '</tbody>' + \
                  '</table>' + \
                  '<br>' + \
                  '<br>' + \
                  '<h6>' + \
                    'Compléments à fournir pour une franchise' + \
                  '</h6>' + \
                  '<br>' + \
                  '<table class="table table-striped table-bordered">' + \
                    '<thead>' + \
                      '<tr>' + \
                        '<th scope="col">Documents</th>' + \
                        '<th scope="col">Disponible ?</th>' + \
                      '</tr>' + \
                    '</thead>' + \
                    '<tbody>' + \
                      '<tr>' + \
                        '<td>Document information précontractuel (DIP)</td>' + \
                        '<td></td>' + \
                      '</tr>' + \
                      '<tr>' + \
                        '<td>Pré contrat</td>' + \
                        '<td></td>' + \
                      '</tr>' + \
                    '</tbody>' + \
                  '</table>' + \
                  '<br>' + \
                  '<br>' + \
                  '<h6>' + \
                    'Compléments à fournir pour une reprise entreprise' + \
                  '</h6>' + \
                  '<br>' + \
                  '<table class="table table-striped table-bordered">' + \
                    '<thead>' + \
                      '<tr>' + \
                        '<th scope="col">Documents</th>' + \
                        '<th scope="col">Disponible ?</th>' + \
                      '</tr>' + \
                    '</thead>' + \
                    '<tbody>' + \
                      '<tr>' + \
                        '<td>Compromis de vente ou protocole de cession de parts ou d’actions</td>' + \
                        '<td></td>' + \
                      '</tr>' + \
                      '<tr>' + \
                        '<td>Méthodes de valorisation de la société</td>' + \
                        '<td></td>' + \
                      '</tr>' + \
                      '<tr>' + \
                        '<td>Documents comptables des 3 dernières années de la société reprise</td>' + \
                        '<td></td>' + \
                      '</tr>' + \
                      '<tr>' + \
                        '<td>Protocole de garantie actif/passif</td>' + \
                        '<td></td>' + \
                      '</tr>' + \
                    '</tbody>' + \
                  '</table>' + \
                  '<br>' + \
                  '<br>' + \
                  '<h6>' + \
                    'Autres documents' + \
                  '</h6>' + \
                  '<br>' + \
                  '<table class="table table-striped table-bordered">' + \
                    '<thead>' + \
                      '<tr>' + \
                        '<th scope="col">Documents</th>' + \
                        '<th scope="col">Disponible ?</th>' + \
                      '</tr>' + \
                    '</thead>' + \
                    '<tbody>' + \
                      '<tr>' + \
                        '<td>Avis imposition des deux dernières années</td>' + \
                        '<td></td>' + \
                      '</tr>' + \
                      '<tr>' + \
                        '<td>Trois derniers bulletins de salaire (si vous êtes actuellement salarié)</td>' + \
                        '<td></td>' + \
                      '</tr>' + \
                      '<tr>' + \
                        '<td>Justificatifs de vos autres revenus et patrimoine</td>' + \
                        '<td></td>' + \
                      '</tr>' + \
                      '<tr>' + \
                        '<td>Justificatif de vos charges et encours de prêt à titre personnel</td>' + \
                        '<td></td>' + \
                      '</tr>' + \
                      '<tr>' + \
                        '<td>Rapport Direction Service Vétérinaire (pour les métiers de bouche)</td>' + \
                        '<td></td>' + \
                      '</tr>' + \
                    '</tbody>' + \
                  '</table>' + \
                  '<br>' + \
                  '<br>' + \
                  '<h6>' + \
                    "Et si vous n'êtes pas client du Crédit Agricole" + \
                  '</h6>' + \
                  '<br>' + \
                  '<table class="table table-striped table-bordered">' + \
                    '<thead>' + \
                      '<tr>' + \
                        '<th scope="col">Documents</th>' + \
                        '<th scope="col">Disponible ?</th>' + \
                      '</tr>' + \
                    '</thead>' + \
                    '<tbody>' + \
                      '<tr>' + \
                        "<td>Pièce d’identité et justificatifs de domicile de moins de trois mois</td>" + \
                        '<td></td>' + \
                      '</tr>' + \
                      '<tr>' + \
                        '<td>Relevés de compte des trois derniers mois</td>' + \
                        '<td></td>' + \
                      '</tr>' + \
                    '</tbody>' + \
                  '</table>' + \
                  '<br>' + \
                  '<br>' + \
                  '<h6>' + \
                    '* Si vous allez procéder à votre immatriculation, pensez à déposer le montant de votre capital dans une' + \
                    'banque qui vous fournira une attestation de dépot de capital social.' + \
                    '<br>' + \
                    "** Si votre bail est proche de sa date d’expiration, la banque pourra vous demander une lettre" + \
                    'de promesse de renouvellement émanant du bailleur.' + \
                  '</h6>' + \
                '</div>' + \
              '</div>' + \
            '</div>' + \
          '</div>' + \
        '</div>' + \
      '</div>' + \
      '<br>'\
      '<br>' + \
                '</div>' + \
                '</div>' + \
                '</div>' + \
                '<br>' + \
                '<script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>' + \
                '<script src="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ho+j7jyWK8fNQe+A12Hb8AhRq26LrZ/JpcUGGOn+Y7RsweNrtN/tE3MoK7ZeZDyx" crossorigin="anonymous"></script>' + \
                '</body>' + \
                '</html>'

        excel_date_1 = round(float(str(workbook.sheet_by_name("Informations_Entreprise")
                                       .cell_value(9, 1)).split(".")[0]))

        python_date = xlrd.xldate_as_tuple(excel_date_1, 0)

        x = datetime.datetime(python_date[0], python_date[1], python_date[2])

        clos_le = x.strftime("%d/%m/%Y")

        options = {
            'page-size': 'A4',
            'header-right': 'Société HOLOMORPHE [SIREN : 883 632 556]',
            'header-left': 'Exercice clos le ' + clos_le,
            'footer-left': "Business plan",
            'footer-right': '[page] sur [topage]'
        }

        path_wkthmltopdf = "C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe"
        config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
        pdfkit.from_string(body, "Business_Plan\\Business_Plan.pdf", configuration=config, options=options)

        filename = "Business_Plan\\Business_Plan.pdf"

        date_of_today = dt.today().strftime('%d_%m_%Y')

        filename_to_sign = filename.split(".pdf")[0] + "_" + date_of_today + ".pdf"

        try:
            packet = io.BytesIO()

            # create a new PDF with Reportlab
            can = canvas.Canvas(packet, pagesize=letter)
            can.setFontSize(8)

            x_coord = 5.9 * 72

            y_coord = 0.14 * 72

            date_of_signature = dt.today().strftime('%d/%m/%Y')

            # Insérer la valeur "Fait à Epinay-sur-Seine (), le dd/mm/YYYY.".
            can.drawString(x_coord, y_coord, "Fait à Epinay-sur-Seine (93800), le " + date_of_signature + ".")

            # Insérer la valeur "Lu et approuvé.".
            can.drawString(x_coord, y_coord - 8, "Lu et approuvé.")

            can.save()

            # move to the beginning of the StringIO buffer
            packet.seek(0)
            new_pdf = PdfFileReader(packet)

            # read your existing PDF
            existing_pdf = PdfFileReader(open(filename, "rb"))

            page_number = existing_pdf.getNumPages()

            output = PdfFileWriter()

            # add the "text" (which is the new pdf) on the existing page
            last_page = existing_pdf.getPage(page_number - 1)
            last_page.mergePage(new_pdf.getPage(0))

            # add every pages of existing_pdf except the last page to output
            for i in range(0, page_number - 1):
                output.addPage(existing_pdf.getPage(i))

            output.addPage(last_page)

            # finally, write "output" to a real file
            output_stream = open(filename_to_sign, "wb")
            output.write(output_stream)
            output_stream.close()

            signature = "A:\\2_Personnel\\2_Non_Recurrentes\\62_Sign\\ma_signature_v2.png"

            pdf = PdfFileReader(open(filename_to_sign, 'rb'))

            page_number = pdf.getNumPages()

            x_coord = 4.4 * 72

            y_coord = 0.03 * 72

            width = 100

            height = round(0.55 * 72)

            os.system("signpdf " + str(filename_to_sign) + " " + str(signature) + " --coords " + str(page_number) + "x"
                      + str(round(x_coord)) + "x" + str(round(y_coord)) + "x" + str(width) + "x" + str(height))
        except Exception as e:
            print("error : " + str(e))


if __name__ == '__main__':
    unittest.main()
