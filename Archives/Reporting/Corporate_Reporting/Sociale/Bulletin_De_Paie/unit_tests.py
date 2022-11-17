import unittest
import xlrd
import pdfkit


class BulletinDePaie(unittest.TestCase):
    def test_bulletin_de_paie(self):
        print("test_bulletin_de_paie")

        location = ("A:\\1_Professionnel\\1_Holomorphe\\1_Administration\\1_Comptabilite_Et_Fiscalite\\1_Annee_2020\\Consolidation_Comptable_Et_Fiscale.xls")

        workbook = xlrd.open_workbook(location)

        sheet = workbook.sheet_by_name("Bulletin_De_Paie")

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
               '<div class="card-header text-center">Bulletin de paie</div>' + \
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
               '<td colspan="2"><b>' + str(sheet.cell_value(1, 0)) + '</b></td>' + \
               '<td colspan="4"><b>' + str(sheet.cell_value(1, 2)) + '</b></td>' + \
               '</tr>'

        for i in range(2, 7):
            body += '<tr>' + \
                    '<td><b>' + str(sheet.cell_value(i, 0)).replace(".0", "") + '</b></td>' + \
                    '<td>' + str(sheet.cell_value(i, 1)).replace(".0", "") + '</td>' + \
                    '<td><b>' + str(sheet.cell_value(i, 2)).replace(".0", "") + '</b></td>' + \
                    '<td>' + str(sheet.cell_value(i, 3)).replace(".0", "") + '</td>' + \
                    '<td><b>' + str(sheet.cell_value(i, 4)).replace(".0", "") + '</b></td>' + \
                    '<td>' + str(sheet.cell_value(i, 5)).replace(".0", "") + '</td>' + \
                    '</tr>'

        body += '<tr>' + \
                '<td><b>' + str(sheet.cell_value(7, 0)) + '</b></td>' + \
                '<td>' + str(sheet.cell_value(7, 1)) + '</td>' + \
                '</tr>' + \
                '<tr>' + \
                '<td colspan="8"></td>' + \
                '</tr>' + \
                '<tr>' + \
                '<td><b>' + str(sheet.cell_value(9, 0)) + '</b></td>' + \
                '<td><b>' + str(sheet.cell_value(9, 1)) + '</b></td>' + \
                '<td>' + str(sheet.cell_value(9, 2)) + '</td>' + \
                '</tr>'

        for i in range(10, 13):
            body += '<tr>' + \
                    '<td><b>' + str(sheet.cell_value(i, 0)).replace(".0", "") + '</b></td>' + \
                    '<td>' + str(sheet.cell_value(i, 1)).replace(".0", "") + '</td>' + \
                    '<td><b>' + str(sheet.cell_value(i, 2)).replace(".0", "") + '</b></td>' + \
                    '<td>' + str(sheet.cell_value(i, 3)).replace(".0", "") + '</td>' + \
                    '</tr>'

        body += '<tr>' + \
                '<td colspan="8"></td>' + \
                '</tr>' + \
                '<tr>' + \
                '<td colspan="6"><b>' + str(sheet.cell_value(14, 0)) + '</b></td>' + \
                '</tr>' + \
                '<tr>' + \
                '<td><b>' + str(sheet.cell_value(15, 0)) + '</b></td>' + \
                '<td>' + str(round(float(str(sheet.cell_value(15, 1))), 2)) + '</td>' + \
                '<td colspan="2"><b>' + str(sheet.cell_value(15, 2)) + '</b></td>' + \
                '<td colspan="2"><b>' + str(sheet.cell_value(15, 4)) + '</b></td>' + \
                '</tr>' + \
                '<tr>' + \
                '<td><b>' + str(sheet.cell_value(16, 0)) + '</b></td>' + \
                '<td><b>' + str(sheet.cell_value(16, 1)) + '</b></td>' + \
                '<td><b>' + str(sheet.cell_value(16, 2)) + '</b></td>' + \
                '<td><b>' + str(sheet.cell_value(16, 3)) + '</b></td>' + \
                '<td><b>' + str(sheet.cell_value(16, 4)) + '</b></td>' + \
                '<td><b>' + str(sheet.cell_value(16, 5)) + '</b></td>' + \
                '</tr>'

        for i in range(17, 37):
            body += '<tr>' + \
                    '<td><b>' + str(sheet.cell_value(i, 0)) + '</b></td>' + \
                    '<td>' + str(round(float(str(sheet.cell_value(i, 1))), 7)) + '</td>' + \
                    '<td>' + str(round(float(str(sheet.cell_value(i, 2))), 7)) + '</td>' + \
                    '<td>' + str(round(float(str(sheet.cell_value(i, 3))), 7)) + '</td>' + \
                    '<td>' + str(round(float(str(sheet.cell_value(i, 4))), 7)) + '</td>' + \
                    '<td>' + str(round(float(str(sheet.cell_value(i, 5))), 7)) + '</td>' + \
                    '</tr>'

        body += '<tr>' + \
                '<td colspan="3"><b>' + str(sheet.cell_value(37, 0)) + '</b></td>' + \
                '<td>' + str(round(float(str(sheet.cell_value(37, 3))), 2)) + '</td>' + \
                '<td><b>' + str(sheet.cell_value(37, 4)) + '</b></td>' + \
                '<td>' + str(round(float(str(sheet.cell_value(37, 5))), 2)) + '</td>' + \
                '</tr>'

        for i in range(38, 43):
            body += '<tr>' + \
                    '<td colspan="5"><b>' + str(sheet.cell_value(i, 0)) + '</b></td>' + \
                    '<td>' + str(round(float(str(sheet.cell_value(i, 5))), 2)) + '</td>' + \
                    '</tr>'

        body += '<tr>' + \
                '<td colspan="8"></td>' + \
                '</tr>' + \
                '<tr>' + \
                '<td><b>' + str(sheet.cell_value(44, 0)) + '</b></td>' + \
                '<td>' + str(round(float(str(sheet.cell_value(44, 1))), 7)) + '</td>' + \
                '</tr>' + \
                '<tr>' + \
                '<td colspan="8"></td>' + \
                '</tr>' + \
                '<tr>' + \
                '<td><b>' + str(sheet.cell_value(46, 0)) + '</b></td>' + \
                '<td><b>' + str(sheet.cell_value(46, 1)) + '</b></td>' + \
                '<td><b>' + str(sheet.cell_value(46, 2)) + '</b></td>' + \
                '<td><b>' + str(sheet.cell_value(46, 3)) + '</b></td>' + \
                '</tr>' + \
                '<tr>' + \
                '<td>' + str(sheet.cell_value(47, 0)) + '</td>' + \
                '<td>' + str(round(float(str(sheet.cell_value(47, 1))), 2)) + '</td>' + \
                '<td>' + str(round(float(str(sheet.cell_value(47, 1))), 7)) + '</td>' + \
                '<td>' + str(round(float(str(sheet.cell_value(47, 1))), 2)) + '</td>' + \
                '</tr>' + \
                '<tr>' + \
                '<td colspan="8"></td>' + \
                '</tr>' + \
                '<tr>' + \
                '<td><b>' + str(sheet.cell_value(49, 0)) + '</b></td>' + \
                '<td><b>' + str(sheet.cell_value(49, 1)) + '</b></td>' + \
                '<td><b>' + str(sheet.cell_value(49, 2)) + '</b></td>' + \
                '<td><b>' + str(sheet.cell_value(49, 3)) + '</b></td>' + \
                '<td><b>' + str(sheet.cell_value(49, 4)) + '</b></td>' + \
                '<td><b>' + str(sheet.cell_value(49, 5)) + '</b></td>' + \
                '</tr>'

        for i in range(50, 53):
            body += '<tr>' + \
                    '<td>' + str(sheet.cell_value(i, 0)) + '</td>' + \
                    '<td>' + str(round(float(str(sheet.cell_value(i, 1))), 2)) + '</td>' + \
                    '<td>' + str(round(float(str(sheet.cell_value(i, 2))), 2)) + '</td>' + \
                    '<td>' + str(round(float(str(sheet.cell_value(i, 3))), 2)) + '</td>' + \
                    '<td>' + str(sheet.cell_value(i, 4)) + '</td>' + \
                    '<td>' + str(round(float(str(sheet.cell_value(i, 5))), 2)) + '</td>' + \
                    '</tr>'

        body += '<tr>' + \
                '<td colspan="8"></td>' + \
                '</tr>' + \
                '<tr>' + \
                '<td colspan="2"><b>' + str(sheet.cell_value(54, 0)) + '<b></td>' + \
                '</tr>' + \
                '<tr>' + \
                '<td><b>' + str(sheet.cell_value(55, 0)) + '</b></td>' + \
                '<td>' + str(round(float(str(sheet.cell_value(55, 1))), 2)) + '</td>' + \
                '</tr>' + \
                '<tr>' + \
                '<td><b>' + str(sheet.cell_value(56, 0)) + '</b></td>' + \
                '<td>' + str(round(float(str(sheet.cell_value(56, 1))), 2)) + '</td>' + \
                '</tr>' + \
                '<tr>' + \
                '<td colspan="8"></td>' + \
                '</tr>' + \
                '<tr>' + \
                '<td><b>' + str(sheet.cell_value(58, 0)) + '</b></td>' + \
                '<td><b>' + str(sheet.cell_value(58, 1)) + '</b></td>' + \
                '<td><b>' + str(sheet.cell_value(58, 2)) + '</b></td>' + \
                '</tr>' + \
                '<tr>' + \
                '<td>' + str(round(float(str(sheet.cell_value(59, 0))), 2)) + '</td>' + \
                '<td>' + str(round(float(str(sheet.cell_value(59, 1))), 2)) + '</td>' + \
                '<td>' + str(round(float(str(sheet.cell_value(59, 2))), 2)) + '</td>' + \
                '</tr>' + \
                '<tr>' + \
                '<td colspan="8"></td>' + \
                '</tr>' + \
                '<tr>' + \
                '<td><b>' + str(sheet.cell_value(61, 0)) + '</b></td>' + \
                '<td><b>' + str(sheet.cell_value(61, 1)) + '</b></td>' + \
                '<td><b>' + str(sheet.cell_value(61, 2)) + '</b></td>' + \
                '<td><b>' + str(sheet.cell_value(61, 3)) + '</b></td>' + \
                '<td><b>' + str(sheet.cell_value(61, 4)) + '</b></td>' + \
                '<td><b>' + str(sheet.cell_value(61, 5)) + '</b></td>' + \
                '<td><b>' + str(sheet.cell_value(61, 6)) + '</b></td>' + \
                '<td><b>' + str(sheet.cell_value(61, 7)) + '</b></td>' + \
                '<td><b>' + str(sheet.cell_value(61, 8)) + '</b></td>' + \
                '</tr>'

        for i in range(62, 64):
            body += '<tr>' + \
                    '<td>' + str(sheet.cell_value(i, 0)) + '</td>' + \
                    '<td>' + str(round(float(str(sheet.cell_value(i, 1))), 2)) + '</td>' + \
                    '<td>' + str(round(float(str(sheet.cell_value(i, 2))), 2)) + '</td>' + \
                    '<td>' + str(sheet.cell_value(i, 3)) + '</td>' + \
                    '<td>' + str(sheet.cell_value(i, 4)) + '</td>' + \
                    '<td>' + str(round(float(str(sheet.cell_value(i, 5))), 2)) + '</td>' + \
                    '<td>' + str(round(float(str(sheet.cell_value(i, 6))), 2)) + '</td>' + \
                    '<td>' + str(round(float(str(sheet.cell_value(i, 7))), 2)) + '</td>' + \
                    '<td>' + str(round(float(str(sheet.cell_value(i, 8))), 2)) + '</td>' + \
                    '</tr>'

        body += '<tr>' + \
                '<td colspan="8"></td>' + \
                '</tr>' + \
                '<tr>' + \
                '<td colspan="8"><b>' + str(sheet.cell_value(65, 0)) + '</b></td>' + \
                '</tr>' + \
                '<tr>' + \
                '<td colspan="8"><b>' + str(sheet.cell_value(66, 0)) + '</b></td>' + \
                '</tr>'

        body += '</tbody>' + \
                '</table>' + \
                '<br>' + \
                '</div>' + \
                '</div>' + \
                '</div>' + \
                '<br>' + \
                '<script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>' + \
                '<script src="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ho+j7jyWK8fNQe+A12Hb8AhRq26LrZ/JpcUGGOn+Y7RsweNrtN/tE3MoK7ZeZDyx" crossorigin="anonymous"></script>' + \
                '</body>' + \
                '</html>'

        options = {
            'page-size': 'A4',
            'header-center': 'Société HOLOMORPHE [SIREN : 883 632 556]',
            'footer-left': 'Bulletin de paie de ' + str(sheet.cell_value(2, 3)) + " du " + str(sheet.cell_value(9, 2)),
            'footer-right': '[page] sur [topage]'
        }
        path_wkthmltopdf = "C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe"
        config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
        pdfkit.from_string(body,
                           "Bulletin_De_Paie\\Bulletin_De_Paie_"
                           + str(sheet.cell_value(4, 3)).replace(".0", "")
                           + "_" + str(sheet.cell_value(0, 2)).replace(".0", "")
                           + "_" + str(sheet.cell_value(0, 4)).replace(".0", "") + ".pdf",
                           configuration=config,
                           options=options)


if __name__ == '__main__':
    unittest.main()
