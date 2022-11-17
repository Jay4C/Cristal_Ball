import unittest
import xlrd
import pdfkit


class Facturation(unittest.TestCase):
    def test_facturation(self):
        print("test_facturation")

        location = ("A:\\1_Professionnel\\1_Holomorphe\\1_Administration\\1_Comptabilite_Et_Fiscalite\\1_Annee_2020\\Consolidation_Comptable_Et_Fiscale.xls")

        workbook = xlrd.open_workbook(location)

        sheet = workbook.sheet_by_name("Facturation")

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
               '<title>Plan_De_Compte_General_S_D</title>' + \
               '</head>' + \
               '<body>' + \
               '<div class="container">' + \
               '<div class="card text-center">' + \
               '<div class="card-header text-center">Facturation</div>' + \
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
               '<tbody>' + \
               '<tr>' + \
               '<td colspan="2"><b>' + str(sheet.cell_value(2, 0)) + '</b></td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><b>' + str(sheet.cell_value(3, 0)) + '</b></td>' + \
               '<td>' + str(sheet.cell_value(3, 1)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><b>' + str(sheet.cell_value(4, 0)) + '</b></td>' + \
               '<td>' + str(sheet.cell_value(4, 1)) + '</td>' + \
               '</tr>' + \
               '</tbody>' + \
               '</table>' + \
               '<br>' + \
               '<table class="table table-bordered">' + \
               '<tbody>' + \
               '<tr>' + \
               '<td colspan="2"><b>' + str(sheet.cell_value(6, 0)) + '</b></td>' + \
               '</tr>'

        for i in range(7, 14):
            body += '<tr>' + \
                    '<td><b>' + str(sheet.cell_value(i, 0)) + '</b></td>' + \
                    '<td>' + str(sheet.cell_value(i, 1)) + '</td>' + \
                    '</tr>'

        body += '</tbody>' + \
                '</table>'

        body += '<br>' + \
                '<table class="table table-bordered">' + \
                '<tbody>' + \
                '<tr>' + \
                '<td colspan="2"><b>' + str(sheet.cell_value(15, 0)) + '</b></td>' + \
                '</tr>'

        for i in range(16, 25):
            body += '<tr>' + \
                    '<td><b>' + str(sheet.cell_value(i, 0)) + '</b></td>' + \
                    '<td>' + str(sheet.cell_value(i, 1)) + '</td>' + \
                    '</tr>'

        body += '</tbody>' + \
                '</table>'

        body += '<br>' + \
                '<table class="table table-bordered">' + \
                '<tbody>'

        for i in range(26, 30):
            body += '<tr>' + \
                    '<td><b>' + str(sheet.cell_value(i, 0)) + '</b></td>' + \
                    '<td>' + str(sheet.cell_value(i, 1)) + '</td>' + \
                    '</tr>'

        body += '</tbody>' + \
                '</table>'

        body += '<br>' + \
                '<table class="table table-bordered">' + \
                '<tbody>' + \
                '<tr>' + \
                '<td><b>' + str(sheet.cell_value(31, 0)) + '</b></td>' + \
                '<td><b>' + str(sheet.cell_value(31, 1)) + '</b></td>' + \
                '<td><b>' + str(sheet.cell_value(31, 2)) + '</b></td>' + \
                '</tr>' + \
                '</tbody>' + \
                '</table>' + \
                '<br>'

        body += '<br>' + \
                '<table class="table table-bordered">' + \
                '<tbody>' + \
                '<tr>' + \
                '<td><b>' + str(sheet.cell_value(33, 0)) + '</b></td>' + \
                '<td>' + str(sheet.cell_value(33, 1)) + '</td>' + \
                '<td>' + str(sheet.cell_value(33, 2)) + '</td>' + \
                '<td>' + str(sheet.cell_value(33, 3)) + '</td>' + \
                '<td>' + str(sheet.cell_value(33, 4)) + '</td>' + \
                '<td>' + str(sheet.cell_value(33, 5)) + '</td>' + \
                '</tr>' + \
                '</tbody>' + \
                '</table>' + \
                '<br>'

        body += '<br>' + \
                '<table class="table table-bordered">' + \
                '<tbody>' + \
                '<tr>' + \
                '<td><b>' + str(sheet.cell_value(35, 0)) + '</b></td>' + \
                '<td><b>' + str(sheet.cell_value(35, 1)) + '</b></td>' + \
                '<td><b>' + str(sheet.cell_value(35, 2)) + '</b></td>' + \
                '</tr>' + \
                '<tr>' + \
                '<td><b>' + str(sheet.cell_value(36, 0)) + '</b></td>' + \
                '<td><b>' + str(sheet.cell_value(36, 1)) + '</b></td>' + \
                '<td><b>' + str(sheet.cell_value(36, 2)) + '</b></td>' + \
                '</tr>' + \
                '</tbody>' + \
                '</table>' + \
                '<br>'

        body += '<br>' + \
                '<table class="table table-bordered">' + \
                '<tbody>' + \
                '<tr>' + \
                '<td><b>' + str(sheet.cell_value(38, 0)) + '</b></td>' + \
                '<td><b>' + str(sheet.cell_value(38, 1)) + '</b></td>' + \
                '<td><b>' + str(sheet.cell_value(38, 2)) + '</b></td>' + \
                '<td><b>' + str(sheet.cell_value(38, 3)) + '</b></td>' + \
                '<td><b>' + str(sheet.cell_value(38, 4)) + '</b></td>' + \
                '<td><b>' + str(sheet.cell_value(38, 5)) + '</b></td>' + \
                '<td><b>' + str(sheet.cell_value(38, 6)) + '</b></td>' + \
                '<td><b>' + str(sheet.cell_value(38, 7)) + '</b></td>' + \
                '<td><b>' + str(sheet.cell_value(38, 8)) + '</b></td>' + \
                '<td><b>' + str(sheet.cell_value(38, 9)) + '</b></td>' + \
                '</tr>'

        start = 39
        end = 39

        for i in range(start, end + 1):
            body += '<tr>' + \
                    '<td>' + str(sheet.cell_value(i, 0)) + '</td>' + \
                    '<td>' + str(sheet.cell_value(i, 1)) + '</td>' + \
                    '<td>' + str(sheet.cell_value(i, 2)) + '</td>' + \
                    '<td>' + str(sheet.cell_value(i, 3)) + '</td>' + \
                    '<td>' + str(sheet.cell_value(i, 4)) + '</td>' + \
                    '<td>' + str(sheet.cell_value(i, 5)) + '</td>' + \
                    '<td>' + str(sheet.cell_value(i, 6)) + '</td>' + \
                    '<td>' + str(sheet.cell_value(i, 7)) + '</td>' + \
                    '<td>' + str(sheet.cell_value(i, 8)) + '</td>' + \
                    '<td>' + str(sheet.cell_value(i, 9)) + '</td>' + \
                    '</tr>'

        body += '</tbody>' + \
                '</table>' + \
                '<br>'

        body += '<br>' + \
                '</div>' + \
                '</div>' + \
                '</div>' + \
                '<br>' + \
                '<script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>' + \
                '<script src="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ho+j7jyWK8fNQe+A12Hb8AhRq26LrZ/JpcUGGOn+Y7RsweNrtN/tE3MoK7ZeZDyx" crossorigin="anonymous"></script>' + \
                '</body>' + \
                '</html>'

        date_facturation = str(sheet.cell_value(4, 1))
        numero_facture = str(sheet.cell_value(3, 1))

        options = {
            'page-size': 'A4',
            'header-right': 'Société HOLOMORPHE [SIREN : 883 632 556]',
            'header-left': date_facturation,
            'footer-left': "Facture n° " + numero_facture,
            'footer-right': '[page] sur [topage]'
        }
        path_wkthmltopdf = "C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe"
        config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
        pdfkit.from_string(body,
                           "Facturation\\Facture_" + numero_facture + ".pdf",
                           configuration=config,
                           options=options)


if __name__ == '__main__':
    unittest.main()
