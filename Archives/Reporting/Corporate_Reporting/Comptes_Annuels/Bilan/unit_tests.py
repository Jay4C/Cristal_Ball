import unittest
import xlrd
import os.path
from xhtml2pdf import pisa
import pdfkit
from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from datetime import datetime as dt
import xlsxwriter
import datetime
import os

annee = "2021"

location = (
    "A:\\1_Professionnel\\1_Holomorphe\\1_Administration\\1_Comptabilite_Fiscalite\\2_Annee_2021"
    "\\Consolidation_Comptable_Fiscale_2021.xls"
)


class Bilan_Holomorphe(unittest.TestCase):
    # à réparer
    def test_bilan_en_tableau_s_d_b(self):
        print("test_bilan_en_tableau_s_d_b")

        workbook = xlrd.open_workbook(location)

        sheet = workbook.sheet_by_name("Bilan_En_Tableau_S_D_B")

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

        # Reporting
        body = '<!doctype html>' + \
        '<html lang="en">' + \
            '<head>' + \
                '<meta charset="utf-8">' + \
                '<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">' + \
                '<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css" integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">' + \
                '<title>Bilan_En_Tableau_S_D_B</title>' + \
            '</head>' + \
            '<body>' + \
                '<div class="container">' + \
                    '<div class="card text-center">' + \
                        '<div class="card-header text-center">Bilan en tableau en système de base</div>' + \
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
                            '<table class="table table-bordered">' + \
                                '<thead>' + \
                                    '<tr>' + \
                                        '<th scope="col">' + str(sheet.cell_value(2, 0)) + '</th>' + \
                                        '<th scope="col">' + str(sheet.cell_value(2, 1)) + '</th>' + \
                                        '<th scope="col">' + str(sheet.cell_value(2, 2)) + '</th>' + \
                                        '<th scope="col">' + str(sheet.cell_value(2, 3)) + '</th>' + \
                                        '<th scope="col">' + str(sheet.cell_value(2, 4)) + '</th>' + \
                                    '</tr>' + \
                                '</thead>' + \
                                '<tbody>' + \
                                    '<tr>' + \
                                        '<td><b>' + str(sheet.cell_value(3, 0)) + '</b></td>' + \
                                        '<td>' + str(sheet.cell_value(3, 1)) + '</td>' + \
                                        '<td>' + str(sheet.cell_value(3, 2)) + '</td>' + \
                                        '<td>' + str(sheet.cell_value(3, 3)) + '</td>' + \
                                        '<td>' + str(sheet.cell_value(3, 4)) + '</td>' + \
                                    '</tr>' + \
                                    '<tr>' + \
                                        '<td><b>' + str(sheet.cell_value(4, 0)) + '</b></td>' + \
                                        '<td>' + str(sheet.cell_value(4, 1)) + '</td>' + \
                                        '<td>' + str(sheet.cell_value(4, 2)) + '</td>' + \
                                        '<td>' + str(sheet.cell_value(4, 3)) + '</td>' + \
                                        '<td>' + str(sheet.cell_value(4, 4)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                        '<td><i>' + str(sheet.cell_value(5, 0)) + '</i></td>' + \
                                        '<td>' + str(sheet.cell_value(5, 1)) + '</td>' + \
                                        '<td>' + str(sheet.cell_value(5, 2)) + '</td>' + \
                                        '<td>' + str(sheet.cell_value(5, 3)) + '</td>' + \
                                        '<td>' + str(sheet.cell_value(5, 4)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                        '<td>' + str(sheet.cell_value(6, 0)) + '</td>' + \
                                        '<td>' + str(sheet.cell_value(6, 1)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(6, 2)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(6, 3)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(6, 4)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                       '<td>' + str(sheet.cell_value(7, 0)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(7, 1)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(7, 2)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(7, 3)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(7, 4)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                       '<td>' + str(sheet.cell_value(8, 0)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(8, 1)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(8, 2)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(8, 3)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(8, 4)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                       '<td>' + str(sheet.cell_value(9, 0)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(9, 1)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(9, 2)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(9, 3)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(9, 4)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                       '<td>' + str(sheet.cell_value(10, 0)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(10, 1)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(10, 2)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(10, 3)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(10, 4)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                       '<td>' + str(sheet.cell_value(11, 0)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(11, 1)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(11, 2)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(11, 3)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(11, 4)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                       '<td>' + str(sheet.cell_value(12, 0)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(12, 1)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(12, 2)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(12, 3)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(12, 4)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                       '<td><i>' + str(sheet.cell_value(13, 0)) + '</i></td>' + \
                                       '<td>' + str(sheet.cell_value(13, 1)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(13, 2)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(13, 3)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(13, 4)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                       '<td>' + str(sheet.cell_value(14, 0)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(14, 1)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(14, 2)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(14, 3)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(14, 4)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                       '<td>' + str(sheet.cell_value(15, 0)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(15, 1)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(15, 2)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(15, 3)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(15, 4)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                       '<td>' + str(sheet.cell_value(16, 0)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(16, 1)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(16, 2)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(16, 3)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(16, 4)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                       '<td>' + str(sheet.cell_value(17, 0)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(17, 1)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(17, 2)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(17, 3)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(17, 4)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                       '<td>' + str(sheet.cell_value(18, 0)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(18, 1)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(18, 2)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(18, 3)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(18, 4)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                       '<td>' + str(sheet.cell_value(19, 0)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(19, 1)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(19, 2)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(19, 3)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(19, 4)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                       '<td><i>' + str(sheet.cell_value(20, 0)) + '</i></td>' + \
                                       '<td>' + str(sheet.cell_value(20, 1)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(20, 2)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(20, 3)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(20, 4)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                       '<td>' + str(sheet.cell_value(21, 0)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(21, 1)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(21, 2)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(21, 3)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(21, 4)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                       '<td>' + str(sheet.cell_value(22, 0)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(22, 1)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(22, 2)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(22, 3)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(22, 4)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                       '<td>' + str(sheet.cell_value(23, 0)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(23, 1)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(23, 2)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(23, 3)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(23, 4)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                       '<td>' + str(sheet.cell_value(24, 0)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(24, 1)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(24, 2)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(24, 3)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(24, 4)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                       '<td>' + str(sheet.cell_value(25, 0)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(25, 1)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(25, 2)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(25, 3)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(25, 4)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                       '<td>' + str(sheet.cell_value(26, 0)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(26, 1)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(26, 2)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(26, 3)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(26, 4)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                       '<td><b><i>' + str(sheet.cell_value(27, 0)) + '</i></b></td>' + \
                                       '<td>' + str(sheet.cell_value(27, 1)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(27, 2)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(27, 3)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(27, 4)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                        '<td colspan="5">' + str(sheet.cell_value(28, 0)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                        '<td colspan="5">' + str(sheet.cell_value(29, 0)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                        '<td colspan="5">' + str(sheet.cell_value(30, 0)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                        '<td colspan="5">' + str(sheet.cell_value(31, 0)) + '</td>' + \
                                   '</tr>' + \
                                '</tbody>' + \
                            '</table>' + \
                            '<br>' + \
                           '<table class="table table-bordered">' + \
                                '<thead>' + \
                                   '<tr>' + \
                                   '<th scope="col">' + str(sheet.cell_value(33, 0)) + '</th>' + \
                                   '<th scope="col">' + str(sheet.cell_value(33, 1)) + '</th>' + \
                                   '<th scope="col">' + str(sheet.cell_value(33, 2)) + '</th>' + \
                                   '<th scope="col">' + str(sheet.cell_value(33, 3)) + '</th>' + \
                                   '<th scope="col">' + str(sheet.cell_value(33, 4)) + '</th>' + \
                                   '</tr>' + \
                                '</thead>' + \
                                '<tbody>' + \
                                   '<tr>' + \
                                       '<td><b>' + str(sheet.cell_value(34, 0)) + '</b></td>' + \
                                       '<td>' + str(sheet.cell_value(34, 1)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(34, 2)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(34, 3)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(34, 4)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                       '<td><i>' + str(sheet.cell_value(35, 0)) + '</i></td>' + \
                                       '<td>' + str(sheet.cell_value(35, 1)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(35, 2)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(35, 3)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(35, 4)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                       '<td>' + str(sheet.cell_value(36, 0)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(36, 1)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(36, 2)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(36, 3)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(36, 4)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                       '<td>' + str(sheet.cell_value(37, 0)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(37, 1)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(37, 2)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(37, 3)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(37, 4)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                       '<td>' + str(sheet.cell_value(38, 0)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(38, 1)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(38, 2)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(38, 3)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(38, 4)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                       '<td>' + str(sheet.cell_value(39, 0)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(39, 1)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(39, 2)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(39, 3)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(39, 4)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                       '<td>' + str(sheet.cell_value(40, 0)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(40, 1)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(40, 2)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(40, 3)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(40, 4)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                       '<td><i>' + str(sheet.cell_value(41, 0)) + '</i></td>' + \
                                       '<td>' + str(sheet.cell_value(41, 1)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(41, 2)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(41, 3)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(41, 4)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                       '<td>' + str(sheet.cell_value(42, 0)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(42, 1)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(42, 2)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(42, 3)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(42, 4)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                       '<td>' + str(sheet.cell_value(43, 0)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(43, 1)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(43, 2)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(43, 3)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(43, 4)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                       '<td>' + str(sheet.cell_value(44, 0)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(44, 1)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(44, 2)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(44, 3)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(44, 4)) + '</td>' + \
                                   '</tr>' + \
                                       '<tr>' + \
                                       '<td><i>' + str(sheet.cell_value(45, 0)) + '<i></td>' + \
                                       '<td>' + str(sheet.cell_value(45, 1)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(45, 2)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(45, 3)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(45, 4)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                       '<td>' + str(sheet.cell_value(46, 0)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(46, 1)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(46, 2)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(46, 3)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(46, 4)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                       '<td>' + str(sheet.cell_value(47, 0)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(47, 1)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(47, 2)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(47, 3)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(47, 4)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                       '<td>' + str(sheet.cell_value(48, 0)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(48, 1)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(48, 2)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(48, 3)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(48, 4)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                       '<td>' + str(sheet.cell_value(49, 0)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(49, 1)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(49, 2)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(49, 3)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(49, 4)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                       '<td>' + str(sheet.cell_value(50, 0)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(50, 1)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(50, 2)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(50, 3)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(50, 4)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                       '<td><b><i>' + str(sheet.cell_value(51, 0)) + '</i></b></td>' + \
                                       '<td>' + str(sheet.cell_value(51, 1)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(51, 2)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(51, 3)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(51, 4)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                       '<td><b><i>' + str(sheet.cell_value(52, 0)) + '</i></b></td>' + \
                                       '<td>' + str(sheet.cell_value(52, 1)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(52, 2)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(52, 3)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(52, 4)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                       '<td><b><i>' + str(sheet.cell_value(53, 0)) + '</i></b></td>' + \
                                       '<td>' + str(sheet.cell_value(53, 1)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(53, 2)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(53, 3)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(53, 4)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                       '<td><b><i>' + str(sheet.cell_value(54, 0)) + '</i></b></td>' + \
                                       '<td>' + str(sheet.cell_value(54, 1)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(54, 2)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(54, 3)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(54, 4)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                       '<td><b><i>' + str(sheet.cell_value(55, 0)) + '</i></b></td>' + \
                                       '<td>' + str(sheet.cell_value(55, 1)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(55, 2)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(55, 3)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(55, 4)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                        '<td colspan="5">' + str(sheet.cell_value(56, 0)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                        '<td colspan="5">' + str(sheet.cell_value(57, 0)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                        '<td colspan="5">' + str(sheet.cell_value(58, 0)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                        '<td colspan="5">' + str(sheet.cell_value(59, 0)) + '</td>' + \
                                   '</tr>' + \
                                '</tbody>' + \
                            '</table>' + \
                            '<br>' + \
                           '<table class="table table-bordered">' + \
                                '<thead>' + \
                                    '<tr>' + \
                                        '<th scope="col">' + str(sheet.cell_value(61, 0)) + '</th>' + \
                                        '<th scope="col">' + str(sheet.cell_value(61, 1)) + '</th>' + \
                                        '<th scope="col">' + str(sheet.cell_value(61, 2)) + '</th>' + \
                                   '</tr>' + \
                                '</thead>' + \
                                '<tbody>' + \
                                   '<tr>' + \
                                       '<td colspan="3"><b>' + str(sheet.cell_value(62, 0)) + '<b></td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                       '<td><i>' + str(sheet.cell_value(63, 0)) + '</i></td>' + \
                                       '<td>' + str(sheet.cell_value(63, 1)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(63, 2)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                       '<td><i>' + str(sheet.cell_value(64, 0)) + '</i></td>' + \
                                       '<td>' + str(sheet.cell_value(64, 1)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(64, 2)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                       '<td><i>' + str(sheet.cell_value(65, 0)) + '</i></td>' + \
                                       '<td>' + str(sheet.cell_value(65, 1)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(65, 2)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                       '<td><i>' + str(sheet.cell_value(66, 0)) + '</i></td>' + \
                                       '<td>' + str(sheet.cell_value(66, 1)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(66, 2)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                       '<td><i>' + str(sheet.cell_value(67, 0)) + '</i></td>' + \
                                       '<td>' + str(sheet.cell_value(67, 1)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(67, 2)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                       '<td>' + str(sheet.cell_value(68, 0)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(68, 1)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(68, 2)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                       '<td>' + str(sheet.cell_value(69, 0)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(69, 1)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(69, 2)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                       '<td>' + str(sheet.cell_value(70, 0)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(70, 1)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(70, 2)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                       '<td>' + str(sheet.cell_value(71, 0)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(71, 1)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(71, 2)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                       '<td>' + str(sheet.cell_value(72, 0)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(72, 1)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(72, 2)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                       '<td>' + str(sheet.cell_value(73, 0)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(73, 1)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(73, 2)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                       '<td>' + str(sheet.cell_value(74, 0)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(74, 1)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(74, 2)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                       '<td>' + str(sheet.cell_value(75, 0)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(75, 1)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(75, 2)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                       '<td><b><i>' + str(sheet.cell_value(76, 0)) + '</i></b></td>' + \
                                       '<td>' + str(sheet.cell_value(76, 1)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(76, 2)) + '</td>' + \
                                    '</tr>' + \
                                   '<tr>' + \
                                       '<td colspan="3"><b>' + str(sheet.cell_value(77, 0)) + '</b></td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                       '<td>' + str(sheet.cell_value(78, 0)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(78, 1)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(78, 2)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                       '<td>' + str(sheet.cell_value(79, 0)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(79, 1)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(79, 2)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                       '<td><b><i>' + str(sheet.cell_value(80, 0)) + '</i></b></td>' + \
                                       '<td>' + str(sheet.cell_value(80, 1)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(80, 2)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                       '<td colspan="3"><b>' + str(sheet.cell_value(81, 0)) + '</b></td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                       '<td>' + str(sheet.cell_value(82, 0)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(82, 1)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(82, 2)) + '</td>' + \
                                   '</tr>' + \
                                    '<tr>' + \
                                       '<td>' + str(sheet.cell_value(83, 0)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(83, 1)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(83, 2)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                       '<td>' + str(sheet.cell_value(84, 0)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(84, 1)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(84, 2)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                       '<td>' + str(sheet.cell_value(85, 0)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(85, 1)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(85, 2)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                       '<td>' + str(sheet.cell_value(86, 0)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(86, 1)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(86, 2)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                       '<td>' + str(sheet.cell_value(87, 0)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(87, 1)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(87, 2)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                       '<td>' + str(sheet.cell_value(88, 0)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(88, 1)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(88, 2)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                       '<td>' + str(sheet.cell_value(89, 0)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(89, 1)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(89, 2)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                       '<td>' + str(sheet.cell_value(90, 0)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(90, 1)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(90, 2)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                       '<td>' + str(sheet.cell_value(91, 0)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(91, 1)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(91, 2)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                       '<td>' + str(sheet.cell_value(92, 0)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(92, 1)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(92, 2)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                       '<td><b><i>' + str(sheet.cell_value(93, 0)) + '</i></b></td>' + \
                                       '<td>' + str(sheet.cell_value(93, 1)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(93, 2)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                       '<td><b><i>' + str(sheet.cell_value(94, 0)) + '</i></b></td>' + \
                                       '<td>' + str(sheet.cell_value(94, 1)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(94, 2)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                       '<td><b><i>' + str(sheet.cell_value(95, 0)) + '</i></b></td>' + \
                                       '<td>' + str(sheet.cell_value(95, 1)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(95, 2)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                       '<td colspan="3">' + str(sheet.cell_value(96, 0)) + '</td>' + \
                                   '</tr>' + \
                                    '<tr>' + \
                                        '<td colspan="3">' + str(sheet.cell_value(97, 0)) + '</td>' + \
                                    '</tr>' + \
                                    '<tr>' + \
                                        '<td colspan="3">' + str(sheet.cell_value(98, 0)) + '</td>' + \
                                    '</tr>' + \
                                    '<tr>' + \
                                        '<td colspan="3">' + str(sheet.cell_value(99, 0)) + '</td>' + \
                                    '</tr>' + \
                                    '<tr>' + \
                                        '<td colspan="3">' + str(sheet.cell_value(100, 0)) + '</td>' + \
                                    '</tr>' + \
                                    '<tr>' + \
                                        '<td colspan="3">' + str(sheet.cell_value(101, 0)) + '</td>' + \
                                    '</tr>' + \
                                    '<tr>' + \
                                        '<td colspan="3">' + str(sheet.cell_value(102, 0)) + '</td>' + \
                                    '</tr>' + \
                                    '<tr>' + \
                                        '<td colspan="3">' + str(sheet.cell_value(103, 0)) + '</td>' + \
                                    '</tr>' + \
                                    '<tr>' + \
                                        '<td colspan="3">' + str(sheet.cell_value(104, 0)) + '</td>' + \
                                    '</tr>' + \
                                    '<tr>' + \
                                        '<td colspan="3">' + str(sheet.cell_value(105, 0)) + '</td>' + \
                                    '</tr>' + \
                                    '<tr>' + \
                                        '<td colspan="3">' + str(sheet.cell_value(106, 0)) + '</td>' + \
                                    '</tr>' + \
                                '</tbody>' + \
                            '</table>' + \
                            '<br>' + \
                           '<table class="table table-bordered">' + \
                                '<thead>' + \
                                    '<tr>' + \
                                        '<th scope="col">' + str(sheet.cell_value(108, 0)) + '</th>' + \
                                        '<th scope="col">' + str(sheet.cell_value(108, 1)) + '</th>' + \
                                        '<th scope="col">' + str(sheet.cell_value(108, 2)) + '</th>' + \
                                   '</tr>' + \
                                '</thead>' + \
                                '<tbody>' + \
                                   '<tr>' + \
                                        '<td colspan="3"><b>' + str(sheet.cell_value(109, 0)) + '<b></td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                       '<td><i>' + str(sheet.cell_value(110, 0)) + '</i></td>' + \
                                       '<td>' + str(sheet.cell_value(110, 1)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(110, 2)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                       '<td><i>' + str(sheet.cell_value(111, 0)) + '</i></td>' + \
                                       '<td>' + str(sheet.cell_value(111, 1)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(111, 2)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                       '<td><i>' + str(sheet.cell_value(112, 0)) + '</i></td>' + \
                                       '<td>' + str(sheet.cell_value(112, 1)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(112, 2)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                       '<td><i>' + str(sheet.cell_value(113, 0)) + '</i></td>' + \
                                       '<td>' + str(sheet.cell_value(113, 1)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(113, 2)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                       '<td><i>' + str(sheet.cell_value(114, 0)) + '</i></td>' + \
                                       '<td>' + str(sheet.cell_value(114, 1)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(114, 2)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                       '<td>' + str(sheet.cell_value(115, 0)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(115, 1)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(115, 2)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                       '<td>' + str(sheet.cell_value(116, 0)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(116, 1)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(116, 2)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                       '<td>' + str(sheet.cell_value(117, 0)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(117, 1)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(117, 2)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                       '<td>' + str(sheet.cell_value(118, 0)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(118, 1)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(118, 2)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                       '<td>' + str(sheet.cell_value(119, 0)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(119, 1)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(119, 2)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                       '<td>' + str(sheet.cell_value(120, 0)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(120, 1)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(120, 2)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                       '<td>' + str(sheet.cell_value(121, 0)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(121, 1)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(121, 2)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                       '<td>' + str(sheet.cell_value(122, 0)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(122, 1)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(122, 2)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                       '<td><b><i>' + str(sheet.cell_value(123, 0)) + '</i></b></td>' + \
                                       '<td>' + str(sheet.cell_value(123, 1)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(123, 2)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                        '<td colspan="3"><b>' + str(sheet.cell_value(124, 0)) + '</b></td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                       '<td>' + str(sheet.cell_value(125, 0)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(125, 1)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(125, 2)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                       '<td>' + str(sheet.cell_value(126, 0)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(126, 1)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(126, 2)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                       '<td><b><i>' + str(sheet.cell_value(127, 0)) + '</i></b></td>' + \
                                       '<td>' + str(sheet.cell_value(127, 1)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(127, 2)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                        '<td colspan="3"><b>' + str(sheet.cell_value(128, 0)) + '</b></td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                       '<td>' + str(sheet.cell_value(129, 0)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(129, 1)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(129, 2)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                       '<td>' + str(sheet.cell_value(130, 0)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(130, 1)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(130, 2)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                       '<td>' + str(sheet.cell_value(131, 0)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(131, 1)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(131, 2)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                       '<td>' + str(sheet.cell_value(132, 0)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(132, 1)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(132, 2)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                       '<td>' + str(sheet.cell_value(133, 0)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(133, 1)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(133, 2)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                       '<td>' + str(sheet.cell_value(134, 0)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(134, 1)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(134, 2)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                       '<td>' + str(sheet.cell_value(135, 0)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(135, 1)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(135, 2)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                       '<td>' + str(sheet.cell_value(136, 0)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(136, 1)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(136, 2)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                       '<td>' + str(sheet.cell_value(137, 0)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(137, 1)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(137, 2)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                       '<td>' + str(sheet.cell_value(138, 0)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(138, 1)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(138, 2)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                       '<td>' + str(sheet.cell_value(139, 0)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(139, 1)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(139, 2)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                       '<td><b><i>' + str(sheet.cell_value(140, 0)) + '</i></b></td>' + \
                                       '<td>' + str(sheet.cell_value(140, 1)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(140, 2)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                       '<td><b><i>' + str(sheet.cell_value(141, 0)) + '</i></b></td>' + \
                                       '<td>' + str(sheet.cell_value(141, 1)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(141, 2)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                       '<td><b><i>' + str(sheet.cell_value(142, 0)) + '</i></b></td>' + \
                                       '<td>' + str(sheet.cell_value(142, 1)) + '</td>' + \
                                       '<td>' + str(sheet.cell_value(142, 2)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                       '<td colspan="3">' + str(sheet.cell_value(143, 0)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                        '<td colspan="3">' + str(sheet.cell_value(144, 0)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                        '<td colspan="3">' + str(sheet.cell_value(145, 0)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                        '<td colspan="3">' + str(sheet.cell_value(146, 0)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                        '<td colspan="3">' + str(sheet.cell_value(147, 0)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                        '<td colspan="3">' + str(sheet.cell_value(148, 0)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                        '<td colspan="3">' + str(sheet.cell_value(149, 0)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                        '<td colspan="3">' + str(sheet.cell_value(150, 0)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                        '<td colspan="3">' + str(sheet.cell_value(151, 0)) + '</td>' + \
                                   '</tr>' + \
                                   '<tr>' + \
                                        '<td colspan="3">' + str(sheet.cell_value(152, 0)) + '</td>' + \
                                   '</tr>' + \
                                '</tbody>' + \
                            '</table>' + \
                        '</div>' + \
                    '</div>' + \
                '<br>' + \
                '<script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>' + \
                '<script src="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ho+j7jyWK8fNQe+A12Hb8AhRq26LrZ/JpcUGGOn+Y7RsweNrtN/tE3MoK7ZeZDyx" crossorigin="anonymous"></script>' + \
            '</body>' + \
        '</html>'

        excel_date_1 = round(
            float(str(workbook.sheet_by_name("Informations_Entreprise").cell_value(9, 1)).split(".")[0]))

        python_date = xlrd.xldate_as_tuple(excel_date_1, 0)

        x = datetime.datetime(python_date[0], python_date[1], python_date[2])

        clos_le = x.strftime("%d/%m/%Y")

        options = {
            'page-size': 'A4',
            'header-right': 'Société HOLOMORPHE [SIREN : 883 632 556]',
            'header-left': 'Exercice clos le ' + clos_le,
            'footer-left': "Bilan en tableau en système " + "\n" + " de base de l'exercice " + str(round(float(str(workbook.sheet_by_name("Informations_Entreprise").cell_value(8, 1)).split(".")[0]))),
            'footer-right': '[page] sur [topage]'
        }

        path_wkthmltopdf = "C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe"

        config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)

        pdfkit.from_string(body, "Holomorphe\\Annee_" + annee + "\\B_E_T_S_D_B\\Bilan_En_Tableau_S_D_B.pdf", configuration=config, options=options)

        filename = "Holomorphe\\Annee_" + annee + "\\B_E_T_S_D_B\\Bilan_En_Tableau_S_D_B.pdf"

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
            can.drawString(x_coord, y_coord, "Fait à Paris (75007), le " + date_of_signature + ".")

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

    #
    def test_bilan_en_liste_s_d_b(self):
        print("test_bilan_en_liste_s_d_b")

        workbook = xlrd.open_workbook(location)

        sheet = workbook.sheet_by_name("Bilan_En_Liste_S_D_B")

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
               '<title>Bilan_En_Liste_S_D_B</title>' + \
               '</head>' + \
               '<body>' + \
               '<div class="container">' + \
               '<div class="card text-center">' + \
               '<div class="card-header text-center">Bilan en liste en système de base</div>' + \
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
               '<table class="table table-bordered">' + \
               '<thead>' + \
               '<tr>' + \
               '<th scope="col">' + str(sheet.cell_value(2, 0)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(2, 1)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(2, 2)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(2, 3)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(2, 4)) + '</th>' + \
               '</tr>' + \
               '</thead>' + \
               '<tbody>' + \
               '<tr>' + \
               '<td><b>' + str(sheet.cell_value(3, 0)) + '</b></td>' + \
               '<td>' + str(round(sheet.cell_value(3, 1), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(3, 2), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(3, 3), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(3, 4), 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><b>' + str(sheet.cell_value(4, 0)) + '</b></td>' + \
               '<td>' + str(round(sheet.cell_value(4, 1), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(4, 2), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(4, 3), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(4, 4), 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i>' + str(sheet.cell_value(5, 0)) + '</i></td>' + \
               '<td>' + str(round(sheet.cell_value(5, 1), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(5, 2), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(5, 3), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(5, 4), 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(6, 0)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(6, 1), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(6, 2), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(6, 3), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(6, 4), 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(7, 0)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(7, 1), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(7, 2), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(7, 3), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(7, 4), 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(8, 0)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(8, 1), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(8, 2), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(8, 3), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(8, 4), 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(9, 0)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(9, 1), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(9, 2), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(9, 3), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(9, 4), 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(10, 0)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(10, 1), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(10, 2), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(10, 3), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(10, 4), 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(11, 0)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(11, 1), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(11, 2), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(11, 3), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(11, 4), 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(12, 0)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(12, 1), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(12, 2), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(12, 3), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(12, 4), 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i>' + str(sheet.cell_value(13, 0)) + '</i></td>' + \
               '<td>' + str(round(sheet.cell_value(13, 1), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(13, 2), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(13, 3), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(13, 4), 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(14, 0)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(14, 1), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(14, 2), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(14, 3), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(14, 4), 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(15, 0)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(15, 1), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(15, 2), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(15, 3), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(15, 4), 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(16, 0)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(16, 1), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(16, 2), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(16, 3), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(16, 4), 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(17, 0)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(17, 1), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(17, 2), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(17, 3), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(17, 4), 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(18, 0)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(18, 1), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(18, 2), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(18, 3), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(18, 4), 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(19, 0)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(19, 1), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(19, 2), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(19, 3), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(19, 4), 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i>' + str(sheet.cell_value(20, 0)) + '</i></td>' + \
               '<td>' + str(round(sheet.cell_value(20, 1), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(20, 2), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(20, 3), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(20, 4), 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(21, 0)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(21, 1), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(21, 2), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(21, 3), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(21, 4), 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(22, 0)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(22, 1), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(22, 2), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(22, 3), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(22, 4), 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(23, 0)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(23, 1), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(23, 2), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(23, 3), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(23, 4), 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(24, 0)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(24, 1), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(24, 2), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(24, 3), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(24, 4), 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(25, 0)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(25, 1), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(25, 2), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(25, 3), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(25, 4), 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(26, 0)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(26, 1), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(26, 2), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(26, 3), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(26, 4), 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><b><i>' + str(sheet.cell_value(27, 0)) + '</i></b></td>' + \
               '<td>' + str(round(sheet.cell_value(27, 1), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(27, 2), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(27, 3), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(27, 4), 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="5">' + str(sheet.cell_value(28, 0)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="5">' + str(sheet.cell_value(29, 0)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="5">' + str(sheet.cell_value(30, 0)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="5">' + str(sheet.cell_value(31, 0)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="5">' + str(sheet.cell_value(32, 0)) + '</td>' + \
               '</tr>' + \
               '</tbody>' + \
               '</table>' + \
               '<br>' + \
               '<table class="table table-bordered">' + \
               '<thead>' + \
               '<tr>' + \
               '<th scope="col">' + str(sheet.cell_value(33, 0)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(33, 1)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(33, 2)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(33, 3)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(33, 4)) + '</th>' + \
               '</tr>' + \
               '</thead>' + \
               '<tbody>' + \
               '<tr>' + \
               '<td><b>' + str(sheet.cell_value(34, 0)) + '</b></td>' + \
               '<td>' + str(round(sheet.cell_value(34, 1), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(34, 2), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(34, 3), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(34, 4), 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i>' + str(sheet.cell_value(35, 0)) + '</i></td>' + \
               '<td>' + str(round(sheet.cell_value(35, 1), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(35, 2), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(35, 3), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(35, 4), 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(36, 0)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(36, 1), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(36, 2), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(36, 3), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(36, 4), 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(37, 0)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(37, 1), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(37, 2), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(37, 3), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(37, 4), 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(38, 0)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(38, 1), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(38, 2), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(38, 3), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(38, 4), 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(39, 0)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(39, 1), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(39, 2), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(39, 3), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(39, 4), 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(40, 0)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(40, 1), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(40, 2), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(40, 3), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(40, 4), 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i>' + str(sheet.cell_value(41, 0)) + '</i></td>' + \
               '<td>' + str(round(sheet.cell_value(41, 1), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(41, 2), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(41, 3), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(41, 4), 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(42, 0)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(42, 1), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(42, 2), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(42, 3), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(42, 4), 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(43, 0)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(43, 1), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(43, 2), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(43, 3), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(43, 4), 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(44, 0)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(44, 1), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(44, 2), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(44, 3), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(44, 4), 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i>' + str(sheet.cell_value(45, 0)) + '<i></td>' + \
               '<td>' + str(round(sheet.cell_value(45, 1), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(45, 2), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(45, 3), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(45, 4), 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(46, 0)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(46, 1), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(46, 2), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(46, 3), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(46, 4), 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(47, 0)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(47, 1), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(47, 2), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(47, 3), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(47, 4), 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(48, 0)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(48, 1), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(48, 2), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(48, 3), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(48, 4), 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(49, 0)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(49, 1), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(49, 2), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(49, 3), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(49, 4), 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(50, 0)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(50, 1), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(50, 2), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(50, 3), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(50, 4), 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><b><i>' + str(sheet.cell_value(51, 0)) + '</i></b></td>' + \
               '<td>' + str(round(sheet.cell_value(51, 1), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(51, 2), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(51, 3), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(51, 4), 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><b><i>' + str(sheet.cell_value(52, 0)) + '</i></b></td>' + \
               '<td>' + str(round(sheet.cell_value(52, 1), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(52, 2), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(52, 3), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(52, 4), 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><b><i>' + str(sheet.cell_value(53, 0)) + '</i></b></td>' + \
               '<td>' + str(round(sheet.cell_value(53, 1), 2)) + '</td>' + \
               '<td> - </td>' + \
               '<td>' + str(round(sheet.cell_value(53, 3), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(53, 4), 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><b><i>' + str(sheet.cell_value(54, 0)) + '</i></b></td>' + \
               '<td>' + str(round(sheet.cell_value(54, 1), 2)) + '</td>' + \
               '<td> - </td>' + \
               '<td>' + str(round(sheet.cell_value(54, 3), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(54, 4), 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><b><i>' + str(sheet.cell_value(55, 0)) + '</i></b></td>' + \
               '<td>' + str(round(sheet.cell_value(55, 1), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(55, 2), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(55, 3), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(55, 4), 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="5">' + str(sheet.cell_value(56, 0)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="5">' + str(sheet.cell_value(57, 0)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="5">' + str(sheet.cell_value(58, 0)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="5">' + str(sheet.cell_value(59, 0)) + '</td>' + \
               '</tr>' + \
               '</tbody>' + \
               '</table>' + \
               '<br>' + \
               '<table class="table table-bordered">' + \
               '<thead>' + \
               '<tr>' + \
               '<th scope="col">' + str(sheet.cell_value(61, 0)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(61, 1)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(61, 2)) + '</th>' + \
               '</tr>' + \
               '</thead>' + \
               '<tbody>' + \
               '<tr>' + \
               '<td colspan="3"><b>' + str(sheet.cell_value(62, 0)) + '<b></td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i>' + str(sheet.cell_value(63, 0)) + '</i></td>' + \
               '<td>' + str(round(sheet.cell_value(63, 1), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(63, 2), 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i>' + str(sheet.cell_value(64, 0)) + '</i></td>' + \
               '<td>' + str(round(sheet.cell_value(64, 1), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(64, 2), 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i>' + str(sheet.cell_value(65, 0)) + '</i></td>' + \
               '<td>' + str(round(sheet.cell_value(65, 1), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(65, 2), 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i>' + str(sheet.cell_value(66, 0)) + '</i></td>' + \
               '<td>' + str(round(sheet.cell_value(66, 1), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(66, 2), 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i>' + str(sheet.cell_value(67, 0)) + '</i></td>' + \
               '<td>' + str(round(sheet.cell_value(67, 1), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(67, 2), 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i>' + str(sheet.cell_value(68, 0)) + '</i></td>' + \
               '<td>' + str(round(sheet.cell_value(68, 1), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(68, 2), 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i>' + str(sheet.cell_value(69, 0)) + '</i></td>' + \
               '<td>' + str(round(sheet.cell_value(69, 1), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(69, 2), 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i>' + str(sheet.cell_value(70, 0)) + '</i></td>' + \
               '<td>' + str(round(sheet.cell_value(70, 1), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(70, 2), 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i>' + str(sheet.cell_value(71, 0)) + '</i></td>' + \
               '<td>' + str(round(sheet.cell_value(71, 1), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(71, 2), 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i>' + str(sheet.cell_value(72, 0)) + '</i></td>' + \
               '<td>' + str(round(sheet.cell_value(72, 1), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(72, 2), 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i>' + str(sheet.cell_value(73, 0)) + '</i></td>' + \
               '<td>' + str(round(sheet.cell_value(73, 1), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(73, 2), 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><b><i>' + str(sheet.cell_value(74, 0)) + '</i></b></td>' + \
               '<td>' + str(round(sheet.cell_value(74, 1), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(74, 2), 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><b><i>' + str(sheet.cell_value(75, 0)) + '</i></b></td>' + \
               '<td>' + str(round(sheet.cell_value(75, 1), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(75, 2), 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><b><i>' + str(sheet.cell_value(76, 0)) + '</i></b></td>' + \
               '<td>' + str(round(sheet.cell_value(76, 1), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(76, 2), 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="3"><b>' + str(sheet.cell_value(77, 0)) + '</b></td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i>' + str(sheet.cell_value(78, 0)) + '</i></td>' + \
               '<td>' + str(round(sheet.cell_value(78, 1), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(78, 2), 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i>' + str(sheet.cell_value(79, 0)) + '</i></td>' + \
               '<td>' + str(round(sheet.cell_value(79, 1), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(79, 2), 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i>' + str(sheet.cell_value(80, 0)) + '</i></td>' + \
               '<td>' + str(round(sheet.cell_value(80, 1), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(80, 2), 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i>' + str(sheet.cell_value(81, 0)) + '</i></td>' + \
               '<td>' + str(round(sheet.cell_value(81, 1), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(81, 2), 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i>' + str(sheet.cell_value(82, 0)) + '</i></td>' + \
               '<td>' + str(round(sheet.cell_value(82, 1), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(82, 2), 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i>' + str(sheet.cell_value(83, 0)) + '</i></td>' + \
               '<td>' + str(round(sheet.cell_value(83, 1), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(83, 2), 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i>' + str(sheet.cell_value(84, 0)) + '</i></td>' + \
               '<td>' + str(round(sheet.cell_value(84, 1), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(84, 2), 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i>' + str(sheet.cell_value(85, 0)) + '</i></td>' + \
               '<td>' + str(round(sheet.cell_value(85, 1), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(85, 2), 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i>' + str(sheet.cell_value(86, 0)) + '</i></td>' + \
               '<td>' + str(round(sheet.cell_value(86, 1), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(86, 2), 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i>' + str(sheet.cell_value(87, 0)) + '</i></td>' + \
               '<td>' + str(round(sheet.cell_value(87, 1), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(87, 2), 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i>' + str(sheet.cell_value(88, 0)) + '</i></td>' + \
               '<td>' + str(round(sheet.cell_value(88, 1), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(88, 2), 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><b><i>' + str(sheet.cell_value(89, 0)) + '</i></b></td>' + \
               '<td>' + str(round(sheet.cell_value(89, 1), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(89, 2), 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><b><i>' + str(sheet.cell_value(90, 0)) + '</i></b></td>' + \
               '<td>' + str(round(sheet.cell_value(90, 1), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(90, 2), 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="3"><b>' + str(sheet.cell_value(91, 0)) + '</b></td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i>' + str(sheet.cell_value(92, 0)) + '</i></td>' + \
               '<td>' + str(round(sheet.cell_value(92, 1), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(92, 2), 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i>' + str(sheet.cell_value(93, 0)) + '</i></td>' + \
               '<td>' + str(round(sheet.cell_value(93, 1), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(93, 2), 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><b><i>' + str(sheet.cell_value(94, 0)) + '</i></b></td>' + \
               '<td>' + str(round(sheet.cell_value(94, 1), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(94, 2), 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="3">' + str(sheet.cell_value(95, 0)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="3"><b>' + str(sheet.cell_value(96, 0)) + '</b></td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i>' + str(sheet.cell_value(97, 0)) + '</i></td>' + \
               '<td>' + str(round(sheet.cell_value(97, 1), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(97, 2), 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i>' + str(sheet.cell_value(98, 0)) + '</i></td>' + \
               '<td>' + str(round(sheet.cell_value(98, 1), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(98, 2), 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i>' + str(sheet.cell_value(99, 0)) + '</i></td>' + \
               '<td>' + str(round(sheet.cell_value(99, 1), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(99, 2), 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i>' + str(sheet.cell_value(100, 0)) + '</i></td>' + \
               '<td>' + str(round(sheet.cell_value(100, 1), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(100, 2), 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i>' + str(sheet.cell_value(101, 0)) + '</i></td>' + \
               '<td>' + str(round(sheet.cell_value(101, 1), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(101, 2), 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(102, 0)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(102, 1), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(102, 2), 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(103, 0)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(103, 1), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(103, 2), 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(104, 0)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(104, 1), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(104, 2), 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(105, 0)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(105, 1), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(105, 2), 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(106, 0)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(106, 1), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(106, 2), 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(107, 0)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(107, 1), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(107, 2), 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(108, 0)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(108, 1), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(108, 2), 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(109, 0)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(109, 1), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(109, 2), 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><b><i>' + str(sheet.cell_value(110, 0)) + '</i></b></td>' + \
               '<td>' + str(round(sheet.cell_value(110, 1), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(110, 2), 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="3">' + str(sheet.cell_value(111, 0)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="3">' + str(sheet.cell_value(112, 0)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="3">' + str(sheet.cell_value(113, 0)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="3">' + str(sheet.cell_value(114, 0)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="3">' + str(sheet.cell_value(115, 0)) + '</td>' + \
               '</tr>' + \
               '</tbody>' + \
               '</table>' + \
               '<br>' + \
               '<br>'

        body += """
        <div class="card-center">
          <div class="card-header">
             La référence au règlement comptable de l’Autorité des normes comptables appliqué pour l’élaboration 
             des comptes annuels.
          </div>
          <div class="card-body">
            Le règlement n° 2014-03 du 5 juin 2014 de l’Autorité des normes comptables relatif au plan comptable 
            général modifié de la version consolidée au 1 janvier 2019 a été appliqué pour l’élaboration des comptes 
            annuels de la société HOLOMORPHE.
          </div>
        </div>
        <br>
        <br>
        """

        body += """
        <div class="card-center">
          <div class="card-header">
             Le montant global de tout engagement financier, toute garantie ou passifs éventuels qui ne figurent 
             pas au bilan notamment les engagements de crédit-bail, et une indication de la nature et de la forme 
             de toute sûreté réelle.
          </div>
          <div class="card-body">
            0 €
          </div>
        </div>
        <br>
        <br>
        """

        body += """
        <div class="card-center">
          <div class="card-header">
             Les engagements en matière de pension, de compléments de retraite, d’indemnités et d’allocations en 
             raison du départ à la retraite ou avantages similaires des membres ou associés de son personnel ou de 
             ses mandataires sociaux
          </div>
          <div class="card-body">
            0 €
          </div>
        </div>
        <br>
        <br>
        """

        body += """
        <div class="card-center">
          <div class="card-header">
            Les engagements à l’égard d’entreprises liées ou associées.
          </div>
          <div class="card-body">
            0 €
          </div>
        </div>
        <br>
        <br>
        <br>
        """

        body += """
        <div class="card-center">
          <div class="card-header">
             Le montant des avances et crédits alloués aux membres des organes d’administration, de direction ou 
             de surveillance, avec indication des conditions consenties et des remboursements opérés pendant 
             l’exercice, ainsi que du montant des engagements pris pour leur compte.
          </div>
          <div class="card-body">
            0 €
          </div>
        </div>
        <br>
        <br>
        """

        body += '</div>' + \
                '</div>' + \
                '<br>' + \
                '<script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>' + \
                '<script src="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ho+j7jyWK8fNQe+A12Hb8AhRq26LrZ/JpcUGGOn+Y7RsweNrtN/tE3MoK7ZeZDyx" crossorigin="anonymous"></script>' + \
                '</body>' + \
                '</html>'

        excel_date_1 = round(float(str(workbook.sheet_by_name("Informations_Entreprise").cell_value(9, 1)).split(".")[0]))

        python_date = xlrd.xldate_as_tuple(excel_date_1, 0)

        x = datetime.datetime(python_date[0], python_date[1], python_date[2])

        clos_le = x.strftime("%d/%m/%Y")

        options = {
            'page-size': 'A4',
            'header-right': 'Société HOLOMORPHE [SIREN : 883 632 556]',
            'header-left': 'Exercice clos le ' + clos_le,
            'footer-left': "Bilan en liste en système de base de l'exercice " + str(round(float(str(workbook.sheet_by_name("Informations_Entreprise").cell_value(8, 1)).split(".")[0]))),
            'footer-right': '[page] sur [topage]'
        }

        path_wkthmltopdf = "C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe"

        config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)

        pdfkit.from_string(body, "Holomorphe\\Annee_" + annee + "\\B_E_L_S_D_B\\Bilan_En_Liste_S_D_B.pdf", configuration=config, options=options)

        filename = "Holomorphe\\Annee_" + annee + "\\B_E_L_S_D_B\\Bilan_En_Liste_S_D_B.pdf"

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
            can.drawString(x_coord, y_coord, "Fait à Paris (75007), le " + date_of_signature + ".")

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

    #
    def test_bilan_avant_repartition_s_a(self):
        print("test_bilan_avant_repartition_s_a")

        workbook = xlrd.open_workbook(location)

        sheet = workbook.sheet_by_name("Bilan_Avant_Répartition_S_A")

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
               '<title>Bilan_Avant_Repartition_S_A</title>' + \
               '</head>' + \
               '<body>' + \
               '<div class="container">' + \
               '<div class="card text-center">' + \
               '<div class="card-header text-center">Bilan avant répartition en système abrégé</div>' + \
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
               '<table class="table table-bordered">' + \
               '<thead>' + \
               '<tr>' + \
               '<th scope="col">' + str(sheet.cell_value(2, 0)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(2, 1)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(2, 2)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(2, 3)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(2, 4)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(2, 5)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(2, 6)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(2, 7)) + '</th>' + \
               '</tr>' + \
               '</thead>' + \
               '<tbody>' + \
               '<tr>' + \
               '<td colspan="5"><b>' + str(sheet.cell_value(3, 0)) + '</b></td>' + \
               '<td colspan="3"><b>' + str(sheet.cell_value(3, 5)) + '</b></td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i>' + str(sheet.cell_value(4, 0)) + '</i></td>' + \
               '<td>' + str(sheet.cell_value(4, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(4, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(4, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(4, 4)) + '</td>' + \
               '<td><i>' + str(sheet.cell_value(4, 5)) + '</i></td>' + \
               '<td>' + str(sheet.cell_value(4, 6)) + '</td>' + \
               '<td>' + str(sheet.cell_value(4, 7)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(5, 0)) + '</td>' + \
               '<td>' + str(sheet.cell_value(5, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(5, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(5, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(5, 4)) + '</td>' + \
               '<td><i>' + str(sheet.cell_value(5, 5)) + '</i></td>' + \
               '<td>' + str(sheet.cell_value(5, 6)) + '</td>' + \
               '<td>' + str(sheet.cell_value(5, 7)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(6, 0)) + '</td>' + \
               '<td>' + str(sheet.cell_value(6, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(6, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(6, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(6, 4)) + '</td>' + \
               '<td><i>' + str(sheet.cell_value(6, 5)) + '</i></td>' + \
               '<td>' + str(sheet.cell_value(6, 6)) + '</td>' + \
               '<td>' + str(sheet.cell_value(6, 7)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i>' + str(sheet.cell_value(7, 0)) + '</i></td>' + \
               '<td>' + str(sheet.cell_value(7, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(7, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(7, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(7, 4)) + '</td>' + \
               '<td>' + str(sheet.cell_value(7, 5)) + '</td>' + \
               '<td>' + str(sheet.cell_value(7, 6)) + '</td>' + \
               '<td>' + str(sheet.cell_value(7, 7)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i>' + str(sheet.cell_value(8, 0)) + '</i></td>' + \
               '<td>' + str(sheet.cell_value(8, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(8, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(8, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(8, 4)) + '</td>' + \
               '<td>' + str(sheet.cell_value(8, 5)) + '</td>' + \
               '<td>' + str(sheet.cell_value(8, 6)) + '</td>' + \
               '<td>' + str(sheet.cell_value(8, 7)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><b><i>' + str(sheet.cell_value(9, 0)) + '</i></b></td>' + \
               '<td>' + str(sheet.cell_value(9, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(9, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(9, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(9, 4)) + '</td>' + \
               '<td>' + str(sheet.cell_value(9, 5)) + '</td>' + \
               '<td>' + str(sheet.cell_value(9, 6)) + '</td>' + \
               '<td>' + str(sheet.cell_value(9, 7)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="5"><b>' + str(sheet.cell_value(10, 0)) + '</b></td>' + \
               '<td><i>' + str(sheet.cell_value(10, 5)) + '</i></td>' + \
               '<td>' + str(sheet.cell_value(10, 6)) + '</td>' + \
               '<td>' + str(sheet.cell_value(10, 7)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i>' + str(sheet.cell_value(11, 0)) + '</i></td>' + \
               '<td>' + str(sheet.cell_value(11, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(11, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(11, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(11, 4)) + '</td>' + \
               '<td><i>' + str(sheet.cell_value(11, 5)) + '</i></td>' + \
               '<td>' + str(sheet.cell_value(11, 6)) + '</td>' + \
               '<td>' + str(sheet.cell_value(11, 7)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i>' + str(sheet.cell_value(12, 0)) + '</i></td>' + \
               '<td>' + str(sheet.cell_value(12, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(12, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(12, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(12, 4)) + '</td>' + \
               '<td><i>' + str(sheet.cell_value(12, 5)) + '</i></td>' + \
               '<td>' + str(sheet.cell_value(12, 6)) + '</td>' + \
               '<td>' + str(sheet.cell_value(12, 7)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i>' + str(sheet.cell_value(13, 0)) + '</i></td>' + \
               '<td>' + str(sheet.cell_value(13, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(13, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(13, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(13, 4)) + '</td>' + \
               '<td><b><i>' + str(sheet.cell_value(13, 5)) + '</i></b></td>' + \
               '<td>' + str(sheet.cell_value(13, 6)) + '</td>' + \
               '<td>' + str(sheet.cell_value(13, 7)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i>' + str(sheet.cell_value(14, 0)) + '</i></td>' + \
               '<td>' + str(sheet.cell_value(14, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(14, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(14, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(14, 4)) + '</td>' + \
               '<td><b><i>' + str(sheet.cell_value(14, 5)) + '</i></b></td>' + \
               '<td>' + str(sheet.cell_value(14, 6)) + '</td>' + \
               '<td>' + str(sheet.cell_value(14, 7)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(15, 0)) + '</td>' + \
               '<td>' + str(sheet.cell_value(15, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(15, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(15, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(15, 4)) + '</td>' + \
               '<td colspan="3"><b>' + str(sheet.cell_value(15, 5)) + '</b></td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(16, 0)) + '</td>' + \
               '<td>' + str(sheet.cell_value(16, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(16, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(16, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(16, 4)) + '</td>' + \
               '<td><i>' + str(sheet.cell_value(16, 5)) + '</i></td>' + \
               '<td>' + str(sheet.cell_value(16, 6)) + '</td>' + \
               '<td>' + str(sheet.cell_value(16, 7)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i>' + str(sheet.cell_value(17, 0)) + '</i></td>' + \
               '<td>' + str(sheet.cell_value(17, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(17, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(17, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(17, 4)) + '</td>' + \
               '<td><i>' + str(sheet.cell_value(17, 5)) + '</i></td>' + \
               '<td>' + str(sheet.cell_value(17, 6)) + '</td>' + \
               '<td>' + str(sheet.cell_value(17, 7)) + '</td>' + \
               '</tr>' + \
              '<tr>' + \
              '<td><i>' + str(sheet.cell_value(18, 0)) + '</i></td>' + \
              '<td>' + str(sheet.cell_value(18, 1)) + '</td>' + \
              '<td>' + str(sheet.cell_value(18, 2)) + '</td>' + \
              '<td>' + str(sheet.cell_value(18, 3)) + '</td>' + \
              '<td>' + str(sheet.cell_value(18, 4)) + '</td>' + \
              '<td><i>' + str(sheet.cell_value(18, 5)) + '</i></td>' + \
              '<td>' + str(sheet.cell_value(18, 6)) + '</td>' + \
              '<td>' + str(sheet.cell_value(18, 7)) + '</td>' + \
              '</tr>' + \
              '<tr>' + \
              '<td><i>' + str(sheet.cell_value(19, 0)) + '</i></td>' + \
              '<td>' + str(sheet.cell_value(19, 1)) + '</td>' + \
              '<td>' + str(sheet.cell_value(19, 2)) + '</td>' + \
              '<td>' + str(sheet.cell_value(19, 3)) + '</td>' + \
              '<td>' + str(sheet.cell_value(19, 4)) + '</td>' + \
              '<td><i>' + str(sheet.cell_value(19, 5)) + '</i></td>' + \
              '<td>' + str(sheet.cell_value(19, 6)) + '</td>' + \
              '<td>' + str(sheet.cell_value(19, 7)) + '</td>' + \
              '</tr>' + \
              '<tr>' + \
              '<td><i><b>' + str(sheet.cell_value(20, 0)) + '</b></i></td>' + \
              '<td>' + str(sheet.cell_value(20, 1)) + '</td>' + \
              '<td>' + str(sheet.cell_value(20, 2)) + '</td>' + \
              '<td>' + str(sheet.cell_value(20, 3)) + '</td>' + \
              '<td>' + str(sheet.cell_value(20, 4)) + '</td>' + \
              '<td><i><b>' + str(sheet.cell_value(20, 5)) + '</b></i></td>' + \
              '<td>' + str(sheet.cell_value(20, 6)) + '</td>' + \
              '<td>' + str(sheet.cell_value(20, 7)) + '</td>' + \
              '</tr>' + \
              '<tr>' + \
              '<td><i><b>' + str(sheet.cell_value(21, 0)) + '</b></i></td>' + \
              '<td>' + str(sheet.cell_value(21, 1)) + '</td>' + \
              '<td>' + str(sheet.cell_value(21, 2)) + '</td>' + \
              '<td>' + str(sheet.cell_value(21, 3)) + '</td>' + \
              '<td>' + str(sheet.cell_value(21, 4)) + '</td>' + \
              '<td><i><b>' + str(sheet.cell_value(21, 5)) + '</b></i></td>' + \
              '<td>' + str(sheet.cell_value(21, 6)) + '</td>' + \
              '<td>' + str(sheet.cell_value(21, 7)) + '</td>' + \
              '</tr>' + \
              '<tr>' + \
              '<td><i><b>' + str(sheet.cell_value(22, 0)) + '</b></i></td>' + \
              '<td>' + str(sheet.cell_value(22, 1)) + '</td>' + \
              '<td>' + str(sheet.cell_value(22, 2)) + '</td>' + \
              '<td>' + str(sheet.cell_value(22, 3)) + '</td>' + \
              '<td>' + str(sheet.cell_value(22, 4)) + '</td>' + \
              '<td><i><b>' + str(sheet.cell_value(22, 5)) + '</b></i></td>' + \
              '<td>' + str(sheet.cell_value(22, 6)) + '</td>' + \
              '<td>' + str(sheet.cell_value(22, 7)) + '</td>' + \
              '</tr>' + \
              '<tr>' + \
              '<td colspan="8">' + str(sheet.cell_value(23, 0)) + '</td>' + \
              '</tr>' + \
              '<tr>' + \
              '<td colspan="8">' + str(sheet.cell_value(24, 0)) + '</td>' + \
              '</tr>' + \
              '<tr>' + \
              '<td colspan="8">' + str(sheet.cell_value(25, 0)) + '</td>' + \
              '</tr>' + \
              '<tr>' + \
              '<td colspan="8">' + str(sheet.cell_value(26, 0)) + '</td>' + \
              '</tr>' + \
              '<tr>' + \
              '<td colspan="8">' + str(sheet.cell_value(27, 0)) + '</td>' + \
              '</tr>' + \
              '<tr>' + \
              '<td colspan="8">' + str(sheet.cell_value(28, 0)) + '</td>' + \
              '</tr>' + \
              '<tr>' + \
              '<td colspan="8">' + str(sheet.cell_value(29, 0)) + '</td>' + \
              '</tr>' + \
              '<tr>' + \
              '<td colspan="8">' + str(sheet.cell_value(30, 0)) + '</td>' + \
              '</tr>' + \
              '<tr>' + \
              '<td colspan="8">' + str(sheet.cell_value(31, 0)) + '</td>' + \
              '</tr>' + \
              '<tr>' + \
              '<td colspan="8">' + str(sheet.cell_value(32, 0)) + '</td>' + \
              '</tr>' + \
              '</tbody>' + \
               '</table>' + \
               '<br>' + \
               '</div>' + \
               '</div>' + \
               '<br>' + \
               '<script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>' + \
               '<script src="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ho+j7jyWK8fNQe+A12Hb8AhRq26LrZ/JpcUGGOn+Y7RsweNrtN/tE3MoK7ZeZDyx" crossorigin="anonymous"></script>' + \
               '</body>' + \
               '</html>'

        excel_date_1 = round(
            float(str(workbook.sheet_by_name("Informations_Entreprise").cell_value(9, 1)).split(".")[0]))

        python_date = xlrd.xldate_as_tuple(excel_date_1, 0)

        x = datetime.datetime(python_date[0], python_date[1], python_date[2])

        clos_le = x.strftime("%d/%m/%Y")

        options = {
            'page-size': 'A4',
            'header-right': 'Société HOLOMORPHE [SIREN : 883 632 556]',
            'header-left': 'Exercice clos le ' + clos_le,
            'footer-left': "Bilan avant répartition en système \n abrégé de l'exercice " + str(round(float(str(workbook.sheet_by_name("Informations_Entreprise").cell_value(8, 1)).split(".")[0]))),
            'footer-right': '[page] sur [topage]'
        }

        path_wkthmltopdf = "C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe"

        config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)

        pdfkit.from_string(body, "Holomorphe\\Annee_" + annee + "\\B_Av_R_S_A\\Bilan_Avant_Repartition_S_A.pdf", configuration=config, options=options)

        filename = "Holomorphe\\Annee_" + annee + "\\B_Av_R_S_A\\Bilan_Avant_Repartition_S_A.pdf"

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
            can.drawString(x_coord, y_coord, "Fait à Paris (75007), le " + date_of_signature + ".")

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

    #
    def test_bilan_apres_repartition_s_a(self):
        print("test_bilan_apres_repartition_s_a")

        workbook = xlrd.open_workbook(location)

        sheet = workbook.sheet_by_name("Bilan_Apres_Repartition_S_A")

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
               '<title>Bilan_Apres_Repartition_S_A</title>' + \
               '</head>' + \
               '<body>' + \
               '<div class="container">' + \
               '<div class="card text-center">' + \
               '<div class="card-header text-center">Bilan après répartition en système abrégé</div>' + \
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
               '<table class="table table-bordered">' + \
               '<thead>' + \
               '<tr>' + \
               '<th scope="col">' + str(sheet.cell_value(2, 0)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(2, 1)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(2, 2)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(2, 3)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(2, 4)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(2, 5)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(2, 6)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(2, 7)) + '</th>' + \
               '</tr>' + \
               '</thead>' + \
               '<tbody>' + \
               '<tr>' + \
               '<td colspan="5"><b>' + str(sheet.cell_value(3, 0)) + '</b></td>' + \
               '<td colspan="3"><b>' + str(sheet.cell_value(3, 5)) + '</b></td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i>' + str(sheet.cell_value(4, 0)) + '</i></td>' + \
               '<td>' + str(sheet.cell_value(4, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(4, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(4, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(4, 4)) + '</td>' + \
               '<td><i>' + str(sheet.cell_value(4, 5)) + '</i></td>' + \
               '<td>' + str(sheet.cell_value(4, 6)) + '</td>' + \
               '<td>' + str(sheet.cell_value(4, 7)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(5, 0)) + '</td>' + \
               '<td>' + str(sheet.cell_value(5, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(5, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(5, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(5, 4)) + '</td>' + \
               '<td><i>' + str(sheet.cell_value(5, 5)) + '</i></td>' + \
               '<td>' + str(sheet.cell_value(5, 6)) + '</td>' + \
               '<td>' + str(sheet.cell_value(5, 7)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(6, 0)) + '</td>' + \
               '<td>' + str(sheet.cell_value(6, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(6, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(6, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(6, 4)) + '</td>' + \
               '<td><i>' + str(sheet.cell_value(6, 5)) + '</i></td>' + \
               '<td>' + str(sheet.cell_value(6, 6)) + '</td>' + \
               '<td>' + str(sheet.cell_value(6, 7)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i>' + str(sheet.cell_value(7, 0)) + '</i></td>' + \
               '<td>' + str(sheet.cell_value(7, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(7, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(7, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(7, 4)) + '</td>' + \
               '<td>' + str(sheet.cell_value(7, 5)) + '</td>' + \
               '<td>' + str(sheet.cell_value(7, 6)) + '</td>' + \
               '<td>' + str(sheet.cell_value(7, 7)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i>' + str(sheet.cell_value(8, 0)) + '</i></td>' + \
               '<td>' + str(sheet.cell_value(8, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(8, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(8, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(8, 4)) + '</td>' + \
               '<td>' + str(sheet.cell_value(8, 5)) + '</td>' + \
               '<td>' + str(sheet.cell_value(8, 6)) + '</td>' + \
               '<td>' + str(sheet.cell_value(8, 7)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i><b>' + str(sheet.cell_value(9, 0)) + '</b></i></td>' + \
               '<td>' + str(sheet.cell_value(9, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(9, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(9, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(9, 4)) + '</td>' + \
               '<td>' + str(sheet.cell_value(9, 5)) + '</td>' + \
               '<td>' + str(sheet.cell_value(9, 6)) + '</td>' + \
               '<td>' + str(sheet.cell_value(9, 7)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="5"><b>' + str(sheet.cell_value(10, 0)) + '</b></td>' + \
               '<td><i>' + str(sheet.cell_value(10, 5)) + '</i></td>' + \
               '<td>' + str(sheet.cell_value(10, 6)) + '</td>' + \
               '<td>' + str(sheet.cell_value(10, 7)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i>' + str(sheet.cell_value(11, 0)) + '</i></td>' + \
               '<td>' + str(sheet.cell_value(11, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(11, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(11, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(11, 4)) + '</td>' + \
               '<td><i>' + str(sheet.cell_value(11, 5)) + '</i></td>' + \
               '<td>' + str(sheet.cell_value(11, 6)) + '</td>' + \
               '<td>' + str(sheet.cell_value(11, 7)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i>' + str(sheet.cell_value(12, 0)) + '</i></td>' + \
               '<td>' + str(sheet.cell_value(12, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(12, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(12, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(12, 4)) + '</td>' + \
               '<td><i>' + str(sheet.cell_value(12, 5)) + '</i></td>' + \
               '<td>' + str(sheet.cell_value(12, 6)) + '</td>' + \
               '<td>' + str(sheet.cell_value(12, 7)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i>' + str(sheet.cell_value(13, 0)) + '</i></td>' + \
               '<td>' + str(sheet.cell_value(13, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(13, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(13, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(13, 4)) + '</td>' + \
               '<td><i><b>' + str(sheet.cell_value(13, 5)) + '</b></i></td>' + \
               '<td>' + str(sheet.cell_value(13, 6)) + '</td>' + \
               '<td>' + str(sheet.cell_value(13, 7)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i>' + str(sheet.cell_value(14, 0)) + '</i></td>' + \
               '<td>' + str(sheet.cell_value(14, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(14, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(14, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(14, 4)) + '</td>' + \
               '<td><b><i>' + str(sheet.cell_value(14, 5)) + '</i></b></td>' + \
               '<td>' + str(sheet.cell_value(14, 6)) + '</td>' + \
               '<td>' + str(sheet.cell_value(14, 7)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(15, 0)) + '</td>' + \
               '<td>' + str(sheet.cell_value(15, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(15, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(15, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(15, 4)) + '</td>' + \
               '<td colspan="3"><b>' + str(sheet.cell_value(15, 5)) + '</b></td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i>' + str(sheet.cell_value(16, 0)) + '</i></td>' + \
               '<td>' + str(sheet.cell_value(16, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(16, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(16, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(16, 4)) + '</td>' + \
               '<td><i>' + str(sheet.cell_value(16, 5)) + '</i></td>' + \
               '<td>' + str(sheet.cell_value(16, 6)) + '</td>' + \
               '<td>' + str(sheet.cell_value(16, 7)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i>' + str(sheet.cell_value(17, 0)) + '</i></td>' + \
               '<td>' + str(sheet.cell_value(17, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(17, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(17, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(17, 4)) + '</td>' + \
               '<td><i>' + str(sheet.cell_value(17, 5)) + '</i></td>' + \
               '<td>' + str(sheet.cell_value(17, 6)) + '</td>' + \
               '<td>' + str(sheet.cell_value(17, 7)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i>' + str(sheet.cell_value(18, 0)) + '</i></td>' + \
               '<td>' + str(sheet.cell_value(18, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(18, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(18, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(18, 4)) + '</td>' + \
               '<td><i>' + str(sheet.cell_value(18, 5)) + '</i></td>' + \
               '<td>' + str(sheet.cell_value(18, 6)) + '</td>' + \
               '<td>' + str(sheet.cell_value(18, 7)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i>' + str(sheet.cell_value(19, 0)) + '</i></td>' + \
               '<td>' + str(sheet.cell_value(19, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(19, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(19, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(19, 4)) + '</td>' + \
               '<td><i>' + str(sheet.cell_value(19, 5)) + '</i></td>' + \
               '<td>' + str(sheet.cell_value(19, 6)) + '</td>' + \
               '<td>' + str(sheet.cell_value(19, 7)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i><b>' + str(sheet.cell_value(20, 0)) + '</b></i></td>' + \
               '<td>' + str(sheet.cell_value(20, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(20, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(20, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(20, 4)) + '</td>' + \
               '<td><i><b>' + str(sheet.cell_value(20, 5)) + '<b></i></td>' + \
               '<td>' + str(sheet.cell_value(20, 6)) + '</td>' + \
               '<td>' + str(sheet.cell_value(20, 7)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i><b>' + str(sheet.cell_value(21, 0)) + '</b></i></td>' + \
               '<td>' + str(sheet.cell_value(21, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(21, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(21, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(21, 4)) + '</td>' + \
               '<td><i><b>' + str(sheet.cell_value(21, 5)) + '</b></i></td>' + \
               '<td>' + str(sheet.cell_value(21, 6)) + '</td>' + \
               '<td>' + str(sheet.cell_value(21, 7)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i><b>' + str(sheet.cell_value(22, 0)) + '</b></i></td>' + \
               '<td>' + str(sheet.cell_value(22, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(22, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(22, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(22, 4)) + '</td>' + \
               '<td><i><b>' + str(sheet.cell_value(22, 5)) + '</b></i></td>' + \
               '<td>' + str(sheet.cell_value(22, 6)) + '</td>' + \
               '<td>' + str(sheet.cell_value(22, 7)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="8">' + str(sheet.cell_value(23, 0)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="8">' + str(sheet.cell_value(24, 0)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="8">' + str(sheet.cell_value(25, 0)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="8">' + str(sheet.cell_value(26, 0)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="8">' + str(sheet.cell_value(27, 0)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="8">' + str(sheet.cell_value(28, 0)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="8">' + str(sheet.cell_value(29, 0)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="8">' + str(sheet.cell_value(30, 0)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="8">' + str(sheet.cell_value(31, 0)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="8">' + str(sheet.cell_value(32, 0)) + '</td>' + \
               '</tr>' + \
               '</tbody>' + \
               '</table>' + \
               '<br>' + \
               '</div>' + \
               '</div>' + \
               '<br>' + \
               '<script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>' + \
               '<script src="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ho+j7jyWK8fNQe+A12Hb8AhRq26LrZ/JpcUGGOn+Y7RsweNrtN/tE3MoK7ZeZDyx" crossorigin="anonymous"></script>' + \
               '</body>' + \
               '</html>'

        excel_date_1 = round(
            float(str(workbook.sheet_by_name("Informations_Entreprise").cell_value(9, 1)).split(".")[0]))

        python_date = xlrd.xldate_as_tuple(excel_date_1, 0)

        x = datetime.datetime(python_date[0], python_date[1], python_date[2])

        clos_le = x.strftime("%d/%m/%Y")

        options = {
            'page-size': 'A4',
            'header-right': 'Société HOLOMORPHE [SIREN : 883 632 556]',
            'header-left': 'Exercice clos le ' + clos_le,
            'footer-left': "Bilan après répartition en système \n abrégé de l'exercice " + str(round(float(str(workbook.sheet_by_name("Informations_Entreprise").cell_value(8, 1)).split(".")[0]))),
            'footer-right': '[page] sur [topage]'
        }
        path_wkthmltopdf = "C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe"

        config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)

        pdfkit.from_string(body, "Holomorphe\\Annee_" + annee + "\\B_Ap_R_S_A\\Bilan_Apres_Repartition_S_A.pdf", configuration=config, options=options)

        filename = "Holomorphe\\Annee_" + annee + "\\B_Ap_R_S_A\\Bilan_Apres_Repartition_S_A.pdf"

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
            can.drawString(x_coord, y_coord, "Fait à Paris (75007), le " + date_of_signature + ".")

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

    # ok
    def test_bilan_s_d(self):
        print("test_bilan_s_d")

        workbook = xlrd.open_workbook(location)

        sheet = workbook.sheet_by_name("Bilan_S_D")

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
               '<title>Bilan_S_D</title>' + \
               '</head>' + \
               '<body>' + \
               '<div class="container">' + \
               '<div class="card text-center">' + \
               '<div class="card-header text-center">Bilan en système développé</div>' + \
               '<div class="card-body">' + \
               '<h6>Dénomination sociale : ' + denomination_sociale + ' / Capital social : ' \
               + capital_social + '</h6>' + \
               '<h6>Adresse du siège social : ' + adresse_siege_social + ' / SIRET : ' \
               + siret + '</h6>' + \
               '<h6>Registre de Commerce et des Sociétés : ' + rcs + '</h6>' + \
               '<h6>Activité : ' + activite + ' / Code NAF : ' + code_naf + '</h6>' + \
               '<h6>N° TVA intracommunataire : ' + numero_tva_intracommunataire + ' / Président : ' \
               + president + " / Date d'immatriculation : " + date_immatriculation + '</h6>' + \
               '<br>' + \
               '<table class="table table-bordered">' + \
               '<thead>' + \
               '<tr>' + \
               '<th scope="col">' + str(sheet.cell_value(2, 0)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(2, 1)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(2, 2)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(2, 3)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(2, 4)) + '</th>' + \
               '</tr>' + \
               '</thead>' + \
               '<tbody>' + \
               '<tr>' + \
               '<td><b>' + str(sheet.cell_value(3, 0)) + '</b></td>' + \
               '<td>' + str(round(sheet.cell_value(3, 1), 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(3, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(3, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(3, 4)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><b>' + str(sheet.cell_value(4, 0)) + '</b></td>' + \
               '<td>' + str(sheet.cell_value(4, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(4, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(4, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(4, 4)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i>' + str(sheet.cell_value(5, 0)) + '</i></td>' + \
               '<td>' + str(sheet.cell_value(5, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(5, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(5, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(5, 4)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(6, 0)) + '</td>' + \
               '<td>' + str(sheet.cell_value(6, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(6, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(6, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(6, 4)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(7, 0)) + '</td>' + \
               '<td>' + str(sheet.cell_value(7, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(7, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(7, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(7, 4)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(8, 0)) + '</td>' + \
               '<td>' + str(sheet.cell_value(8, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(8, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(8, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(8, 4)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(9, 0)) + '</td>' + \
               '<td>' + str(sheet.cell_value(9, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(9, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(9, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(9, 4)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(10, 0)) + '</td>' + \
               '<td>' + str(sheet.cell_value(10, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(10, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(10, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(10, 4)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(11, 0)) + '</td>' + \
               '<td>' + str(sheet.cell_value(11, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(11, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(11, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(11, 4)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(12, 0)) + '</td>' + \
               '<td>' + str(sheet.cell_value(12, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(12, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(12, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(12, 4)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i>' + str(sheet.cell_value(13, 0)) + '</i></td>' + \
               '<td>' + str(sheet.cell_value(13, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(13, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(13, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(13, 4)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(14, 0)) + '</td>' + \
               '<td>' + str(sheet.cell_value(14, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(14, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(14, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(14, 4)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(15, 0)) + '</td>' + \
               '<td>' + str(sheet.cell_value(15, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(15, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(15, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(15, 4)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(16, 0)) + '</td>' + \
               '<td>' + str(sheet.cell_value(16, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(16, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(16, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(16, 4)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(17, 0)) + '</td>' + \
               '<td>' + str(sheet.cell_value(17, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(17, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(17, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(17, 4)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(18, 0)) + '</td>' + \
               '<td>' + str(sheet.cell_value(18, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(18, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(18, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(18, 4)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(19, 0)) + '</td>' + \
               '<td>' + str(sheet.cell_value(19, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(19, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(19, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(19, 4)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i>' + str(sheet.cell_value(20, 0)) + '</i></td>' + \
               '<td>' + str(sheet.cell_value(20, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(20, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(20, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(20, 4)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(21, 0)) + '</td>' + \
               '<td>' + str(sheet.cell_value(21, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(21, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(21, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(21, 4)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(22, 0)) + '</td>' + \
               '<td>' + str(sheet.cell_value(22, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(22, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(22, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(22, 4)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(23, 0)) + '</td>' + \
               '<td>' + str(sheet.cell_value(23, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(23, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(23, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(23, 4)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(24, 0)) + '</td>' + \
               '<td>' + str(sheet.cell_value(24, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(24, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(24, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(24, 4)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(25, 0)) + '</td>' + \
               '<td>' + str(sheet.cell_value(25, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(25, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(25, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(25, 4)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(26, 0)) + '</td>' + \
               '<td>' + str(sheet.cell_value(26, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(26, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(26, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(26, 4)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><b><i>' + str(sheet.cell_value(27, 0)) + '</i></b></td>' + \
               '<td>' + str(sheet.cell_value(27, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(27, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(27, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(27, 4)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="5">' + str(sheet.cell_value(28, 0)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="5">' + str(sheet.cell_value(29, 0)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="5">' + str(sheet.cell_value(30, 0)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="5">' + str(sheet.cell_value(31, 0)) + '</td>' + \
               '</tr>' + \
               '</tbody>' + \
               '</table>' + \
               '<br>' + \
               '<table class="table table-bordered">' + \
               '<thead>' + \
               '<tr>' + \
               '<th scope="col">' + str(sheet.cell_value(33, 0)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(33, 1)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(33, 2)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(33, 3)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(33, 4)) + '</th>' + \
               '</tr>' + \
               '</thead>' + \
               '<tbody>' + \
               '<tr>' + \
               '<td colspan="5"><b>' + str(sheet.cell_value(34, 0)) + '</b></td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i>' + str(sheet.cell_value(35, 0)) + '</i></td>' + \
               '<td>' + str(sheet.cell_value(35, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(35, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(35, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(35, 4)) + '</td>' + \
               '</tr>' + \
                '<tr>' + \
                '<td>' + str(sheet.cell_value(36, 0)) + '</td>' + \
                '<td>' + str(sheet.cell_value(36, 1)) + '</td>' + \
                '<td>' + str(sheet.cell_value(36, 2)) + '</td>' + \
                '<td>' + str(sheet.cell_value(36, 3)) + '</td>' + \
                '<td>' + str(sheet.cell_value(36, 4)) + '</td>' + \
                '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(37, 0)) + '</td>' + \
               '<td>' + str(sheet.cell_value(37, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(37, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(37, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(37, 4)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(38, 0)) + '</td>' + \
               '<td>' + str(sheet.cell_value(38, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(38, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(38, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(38, 4)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(39, 0)) + '</td>' + \
               '<td>' + str(sheet.cell_value(39, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(39, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(39, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(39, 4)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(40, 0)) + '</td>' + \
               '<td>' + str(sheet.cell_value(40, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(40, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(40, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(40, 4)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i>' + str(sheet.cell_value(41, 0)) + '</i></td>' + \
               '<td>' + str(sheet.cell_value(41, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(41, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(41, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(41, 4)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(42, 0)) + '</td>' + \
               '<td>' + str(sheet.cell_value(42, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(42, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(42, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(42, 4)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(43, 0)) + '</td>' + \
               '<td>' + str(sheet.cell_value(43, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(43, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(43, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(43, 4)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(44, 0)) + '</td>' + \
               '<td>' + str(sheet.cell_value(44, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(44, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(44, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(44, 4)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i>' + str(sheet.cell_value(45, 0)) + '</i></td>' + \
               '<td>' + str(round(sheet.cell_value(45, 1), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(45, 2), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(45, 3), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(45, 4), 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(46, 0)) + '</td>' + \
               '<td>' + str(sheet.cell_value(46, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(46, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(46, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(46, 4)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(47, 0)) + '</td>' + \
               '<td>' + str(sheet.cell_value(47, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(47, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(47, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(47, 4)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(48, 0)) + '</td>' + \
               '<td>' + str(sheet.cell_value(48, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(48, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(48, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(48, 4)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(49, 0)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(49, 1), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(49, 2), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(49, 3), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(49, 4), 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(50, 0)) + '</td>' + \
               '<td>' + str(sheet.cell_value(50, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(50, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(50, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(50, 4)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><b><i>' + str(sheet.cell_value(51, 0)) + '</i></b></td>' + \
               '<td>' + str(round(sheet.cell_value(51, 1), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(51, 2), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(51, 3), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(51, 4), 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><b><i>' + str(sheet.cell_value(52, 0)) + '</i></b></td>' + \
               '<td>' + str(sheet.cell_value(52, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(52, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(52, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(52, 4)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><b><i>' + str(sheet.cell_value(53, 0)) + '</i></b></td>' + \
               '<td>' + str(sheet.cell_value(53, 1)) + '</td>' + \
               '<td> - </td>' + \
               '<td>' + str(sheet.cell_value(53, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(53, 4)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><b><i>' + str(sheet.cell_value(54, 0)) + '</i></b></td>' + \
               '<td>' + str(sheet.cell_value(54, 1)) + '</td>' + \
               '<td> - </td>' + \
               '<td>' + str(sheet.cell_value(54, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(54, 4)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><b><i>' + str(sheet.cell_value(55, 0)) + '</i></b></td>' + \
               '<td>' + str(round(sheet.cell_value(55, 1), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(55, 2), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(55, 3), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(55, 4), 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="5">' + str(sheet.cell_value(56, 0)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="5">' + str(sheet.cell_value(57, 0)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="5">' + str(sheet.cell_value(58, 0)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="5">' + str(sheet.cell_value(59, 0)) + '</td>' + \
               '</tr>' + \
               '</tbody>' + \
               '</table>' + \
               '<br>' + \
               '<table class="table table-bordered">' + \
               '<thead>' + \
               '<tr>' + \
               '<th scope="col">' + str(sheet.cell_value(61, 0)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(61, 1)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(61, 2)) + '</th>' + \
               '</tr>' + \
               '</thead>' + \
               '<tbody>' + \
               '<tr>' + \
               '<td colspan="3"><b>' + str(sheet.cell_value(62, 0)) + '</b></td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i>' + str(sheet.cell_value(63, 0)) + '</i></td>' + \
               '<td>' + str(sheet.cell_value(63, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(63, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i>' + str(sheet.cell_value(64, 0)) + '</i></td>' + \
               '<td>' + str(sheet.cell_value(64, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(64, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i>' + str(sheet.cell_value(65, 0)) + '</i></td>' + \
               '<td>' + str(sheet.cell_value(65, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(65, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i>' + str(sheet.cell_value(66, 0)) + '</i></td>' + \
               '<td>' + str(sheet.cell_value(66, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(66, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i>' + str(sheet.cell_value(67, 0)) + '</i></td>' + \
               '<td>' + str(sheet.cell_value(67, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(67, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(68, 0)) + '</td>' + \
               '<td>' + str(sheet.cell_value(68, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(68, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(69, 0)) + '</td>' + \
               '<td>' + str(sheet.cell_value(69, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(69, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(70, 0)) + '</td>' + \
               '<td>' + str(sheet.cell_value(70, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(70, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(71, 0)) + '</td>' + \
               '<td>' + str(sheet.cell_value(71, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(71, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(72, 0)) + '</td>' + \
               '<td>' + str(sheet.cell_value(72, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(72, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(73, 0)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(73, 1), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(73, 2), 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(74, 0)) + '</td>' + \
               '<td>' + str(sheet.cell_value(74, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(74, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(75, 0)) + '</td>' + \
               '<td>' + str(sheet.cell_value(75, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(75, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><b><i>' + str(sheet.cell_value(76, 0)) + '</i></b></td>' + \
               '<td>' + str(sheet.cell_value(76, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(76, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="3"><b>' + str(sheet.cell_value(77, 0)) + '</b></td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i>' + str(sheet.cell_value(78, 0)) + '</i></td>' + \
               '<td>' + str(sheet.cell_value(78, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(78, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i>' + str(sheet.cell_value(79, 0)) + '</i></td>' + \
               '<td>' + str(sheet.cell_value(79, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(79, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i><b>' + str(sheet.cell_value(80, 0)) + '</b></i></td>' + \
               '<td>' + str(sheet.cell_value(80, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(80, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="3"><b>' + str(sheet.cell_value(81, 0)) + '</b></td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i>' + str(sheet.cell_value(82, 0)) + '</i></td>' + \
               '<td>' + str(sheet.cell_value(82, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(82, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(83, 0)) + '</td>' + \
               '<td>' + str(sheet.cell_value(83, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(83, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(84, 0)) + '</td>' + \
               '<td>' + str(sheet.cell_value(84, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(84, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(85, 0)) + '</td>' + \
               '<td>' + str(sheet.cell_value(85, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(85, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(86, 0)) + '</td>' + \
               '<td>' + str(sheet.cell_value(86, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(86, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(87, 0)) + '</td>' + \
               '<td>' + str(sheet.cell_value(87, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(87, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i>' + str(sheet.cell_value(88, 0)) + '</i></td>' + \
               '<td>' + str(round(sheet.cell_value(88, 1), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(88, 2), 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(89, 0)) + '</td>' + \
               '<td>' + str(sheet.cell_value(89, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(89, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(90, 0)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(90, 1), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(90, 2), 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(91, 0)) + '</td>' + \
               '<td>' + str(sheet.cell_value(91, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(91, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i>' + str(sheet.cell_value(92, 0)) + '</i> </td>' + \
               '<td>' + str(sheet.cell_value(92, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(92, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(93, 0)) + '</td>' + \
               '<td>' + str(sheet.cell_value(93, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(93, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(94, 0)) + '</td>' + \
               '<td>' + str(sheet.cell_value(94, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(94, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(95, 0)) + '</td>' + \
               '<td>' + str(sheet.cell_value(95, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(95, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(96, 0)) + '</td>' + \
               '<td>' + str(sheet.cell_value(96, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(96, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(97, 0)) + '</td>' + \
               '<td>' + str(sheet.cell_value(97, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(97, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><b><i>' + str(sheet.cell_value(98, 0)) + '</i></b></td>' + \
               '<td>' + str(round(sheet.cell_value(98, 1), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(98, 2), 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><b><i>' + str(sheet.cell_value(99, 0)) + '</i></b></td>' + \
               '<td>' + str(sheet.cell_value(99, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(99, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><b><i>' + str(sheet.cell_value(100, 0)) + '</i></b></td>' + \
               '<td>' + str(round(sheet.cell_value(100, 1), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(100, 2), 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="3">' + str(sheet.cell_value(101, 0)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="3">' + str(sheet.cell_value(102, 0)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="3">' + str(sheet.cell_value(103, 0)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="3">' + str(sheet.cell_value(104, 0)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="3">' + str(sheet.cell_value(105, 0)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="3">' + str(sheet.cell_value(106, 0)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="3">' + str(sheet.cell_value(107, 0)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="3">' + str(sheet.cell_value(108, 0)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="3">' + str(sheet.cell_value(109, 0)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="3">' + str(sheet.cell_value(110, 0)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="3">' + str(sheet.cell_value(111, 0)) + '</td>' + \
               '</tr>' + \
               '</tbody>' + \
               '</table>' + \
               '<br>' + \
               '<table class="table table-bordered">' + \
               '<thead>' + \
               '<tr>' + \
               '<th scope="col">' + str(sheet.cell_value(113, 0)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(113, 1)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(113, 2)) + '</th>' + \
               '</tr>' + \
               '</thead>' + \
               '<tbody>' + \
               '<tr>' + \
               '<td><b>' + str(sheet.cell_value(114, 0)) + '</b></td>' + \
              '<td>' + str(sheet.cell_value(114, 1)) + '</td>' + \
              '<td>' + str(sheet.cell_value(114, 2)) + '</td>' + \
              '</tr>' + \
               '<tr>' + \
               '<td><i>' + str(sheet.cell_value(115, 0)) + '</i></td>' + \
               '<td>' + str(sheet.cell_value(115, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(115, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i>' + str(sheet.cell_value(116, 0)) + '</i></td>' + \
               '<td>' + str(sheet.cell_value(116, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(116, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i>' + str(sheet.cell_value(117, 0)) + '</i></td>' + \
               '<td>' + str(sheet.cell_value(117, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(117, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i>' + str(sheet.cell_value(118, 0)) + '</i></td>' + \
               '<td>' + str(sheet.cell_value(118, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(118, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i>' + str(sheet.cell_value(119, 0)) + '</i></td>' + \
               '<td>' + str(sheet.cell_value(119, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(119, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(120, 0)) + '</td>' + \
               '<td>' + str(sheet.cell_value(120, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(120, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(121, 0)) + '</td>' + \
               '<td>' + str(sheet.cell_value(121, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(121, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(122, 0)) + '</td>' + \
               '<td>' + str(sheet.cell_value(122, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(122, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(123, 0)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(123, 1), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(123, 2), 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(124, 0)) + '</td>' + \
               '<td>' + str(sheet.cell_value(124, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(124, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><b>' + str(sheet.cell_value(125, 0)) + '</b></td>' + \
               '<td>' + str(sheet.cell_value(125, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(125, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><b>' + str(sheet.cell_value(126, 0)) + '</b></td>' + \
               '<td>' + str(sheet.cell_value(126, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(126, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><b>' + str(sheet.cell_value(127, 0)) + '</b></td>' + \
               '<td>' + str(sheet.cell_value(127, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(127, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><b><i>' + str(sheet.cell_value(128, 0)) + '</i></b></td>' + \
               '<td>' + str(sheet.cell_value(128, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(128, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="3"><b>' + str(sheet.cell_value(129, 0)) + '</b></td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i>' + str(sheet.cell_value(130, 0)) + '</i></td>' + \
               '<td>' + str(sheet.cell_value(130, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(130, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i>' + str(sheet.cell_value(131, 0)) + '</i></td>' + \
               '<td>' + str(sheet.cell_value(131, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(131, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i><b>' + str(sheet.cell_value(132, 0)) + '</b></i></td>' + \
               '<td>' + str(sheet.cell_value(132, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(132, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="3"><b>' + str(sheet.cell_value(133, 0)) + '</b></td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i>' + str(sheet.cell_value(134, 0)) + '</i></td>' + \
               '<td>' + str(sheet.cell_value(134, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(134, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(135, 0)) + '</td>' + \
               '<td>' + str(sheet.cell_value(135, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(135, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(136, 0)) + '</td>' + \
               '<td>' + str(sheet.cell_value(136, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(136, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(137, 0)) + '</td>' + \
               '<td>' + str(sheet.cell_value(137, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(137, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(138, 0)) + '</td>' + \
               '<td>' + str(sheet.cell_value(138, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(138, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(139, 0)) + '</td>' + \
               '<td>' + str(sheet.cell_value(139, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(139, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i>' + str(sheet.cell_value(140, 0)) + '</i></td>' + \
               '<td>' + str(round(sheet.cell_value(140, 1), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(140, 2), 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(141, 0)) + '</td>' + \
               '<td>' + str(sheet.cell_value(141, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(141, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(142, 0)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(142, 1), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(142, 2), 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(143, 0)) + '</td>' + \
               '<td>' + str(sheet.cell_value(143, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(143, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i>' + str(sheet.cell_value(144, 0)) + '</i> </td>' + \
               '<td>' + str(sheet.cell_value(144, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(144, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(145, 0)) + '</td>' + \
               '<td>' + str(sheet.cell_value(145, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(145, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(146, 0)) + '</td>' + \
               '<td>' + str(sheet.cell_value(146, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(146, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(147, 0)) + '</td>' + \
               '<td>' + str(sheet.cell_value(147, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(147, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(148, 0)) + '</td>' + \
               '<td>' + str(sheet.cell_value(148, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(148, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(149, 0)) + '</td>' + \
               '<td>' + str(sheet.cell_value(149, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(149, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><b><i>' + str(sheet.cell_value(150, 0)) + '</i></b></td>' + \
               '<td>' + str(round(sheet.cell_value(150, 1), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(150, 2), 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><b><i>' + str(sheet.cell_value(151, 0)) + '</i></b></td>' + \
               '<td>' + str(sheet.cell_value(151, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(151, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><b><i>' + str(sheet.cell_value(152, 0)) + '</i></b></td>' + \
               '<td>' + str(round(sheet.cell_value(152, 1), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(152, 2), 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="3">' + str(sheet.cell_value(153, 0)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="3">' + str(sheet.cell_value(154, 0)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="3">' + str(sheet.cell_value(155, 0)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="3">' + str(sheet.cell_value(156, 0)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="3">' + str(sheet.cell_value(157, 0)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="3">' + str(sheet.cell_value(158, 0)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="3">' + str(sheet.cell_value(159, 0)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="3">' + str(sheet.cell_value(160, 0)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="3">' + str(sheet.cell_value(161, 0)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="3">' + str(sheet.cell_value(162, 0)) + '</td>' + \
               '</tr>' + \
               '</tbody>' + \
               '</table>' + \
               '<br>' + \
               '</div>' + \
               '</div>' + \
               '<br>' + \
               '<script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>' + \
               '<script src="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ho+j7jyWK8fNQe+A12Hb8AhRq26LrZ/JpcUGGOn+Y7RsweNrtN/tE3MoK7ZeZDyx" crossorigin="anonymous"></script>' + \
               '</body>' + \
               '</html>'

        excel_date_1 = round(
            float(str(workbook.sheet_by_name("Informations_Entreprise").cell_value(9, 1)).split(".")[0]))

        python_date = xlrd.xldate_as_tuple(excel_date_1, 0)

        x = datetime.datetime(python_date[0], python_date[1], python_date[2])

        clos_le = x.strftime("%d/%m/%Y")

        options = {
            'page-size': 'A4',
            'header-right': 'Société HOLOMORPHE [SIREN : 883 632 556]',
            'header-left': 'Exercice clos le ' + clos_le,
            'footer-left': "Bilan en système développé de l'exercice " + str(round(float(str(workbook.sheet_by_name("Informations_Entreprise").cell_value(8, 1)).split(".")[0]))),
            'footer-right': '[page] sur [topage]'
        }

        path_wkthmltopdf = "C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe"

        config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)

        pdfkit.from_string(
            body,
            "Holomorphe\\Annee_" + annee + "\\B_S_D\\Bilan_S_D.pdf",
            configuration=config,
            options=options
        )

        filename = "Holomorphe\\Annee_" + annee + "\\B_S_D\\Bilan_S_D.pdf"

        date_of_today = dt.today().strftime('%d_%m_%Y')

        filename_to_sign = filename.split(".pdf")[0] + "_" + date_of_today + ".pdf"

        try:
            packet = io.BytesIO()

            # create a new PDF with Reportlab
            can = canvas.Canvas(
                packet,
                pagesize=letter
            )
            can.setFontSize(8)

            x_coord = 5.9 * 72

            y_coord = 0.14 * 72

            date_of_signature = dt.today().strftime('%d/%m/%Y')

            # Insérer la valeur "Fait à Epinay-sur-Seine (), le dd/mm/YYYY.".
            can.drawString(x_coord, y_coord, "Fait à Paris (75007), le " + date_of_signature + ".")

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
