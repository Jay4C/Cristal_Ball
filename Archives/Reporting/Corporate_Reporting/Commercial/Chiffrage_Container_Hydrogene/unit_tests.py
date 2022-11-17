import unittest
import pdfkit
import xlrd


class chiffrage_container_hydrogen(unittest.TestCase):
    def test_chiffrage_container_hydrogen(self):
        print("test_chiffrage_container_hydrogen")

        location = ("A:\\1_Professionnel\\1_Holomorphe\\2_Archives\\4_Management\\Management_Des_Operations.xls")

        workbook = xlrd.open_workbook(location)

        sheet_electrolyseur_type_3 = workbook.sheet_by_name("Electrolyseur_Type_3")

        sheet_container_hydrogene_type_3 = workbook.sheet_by_name("Container_Hydrogene_Type_3")

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

        body = '<!doctype html>' + \
               '<html lang="en">' + \
               '<head>' + \
               '<meta charset="utf-8">' + \
               '<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">' + \
               '<link rel="stylesheet" ' \
               'href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css" ' \
               'integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" ' \
               'crossorigin="anonymous">' + \
               '<title>Chiffrage_Container_Hydrogene</title>' + \
               '</head>' + \
               '<body>' + \
               '<div class="container">' + \
               '<div class="card text-center">' + \
               '<div class="card-header text-center">Chiffrage d' + "'un container hydrogène" + '</div>' + \
               '<div class="card-body">' + \
               '<h6>Dénomination sociale : ' + denomination_sociale + ' / Capital social : ' \
               + capital_social + '</h6>' + \
               '<h6>Adresse du siège social : ' + adresse_siege_social + ' / SIRET : ' \
               + siret + '</h6>' + \
               '<h6>Registre de Commerce et des Sociétés : ' + rcs + '</h6>' + \
               '<h6>Activité : ' + activite + ' / Code NAF : ' + code_naf + '</h6>' + \
               '<h6>N° TVA intracommunataire : ' + numero_tva_intracommunataire + ' / Président : ' \
               + president + ' / Date immatriculation : ' + date_immatriculation + '</h6>' + \
               '<br>'

        body += '<div class="card text-center">' + \
                '<div class="card-header">' + \
                '<h6>Chiffrage d' + "'un électrolyseur de Stanley Meyer" + '</h6>' + \
                '</div>' + \
                '<div class="card-body">' + \
                '<h6>Entrées</h6>' + \
                '<table class ="table table-striped table-bordered">' + \
                '<thead>' + \
                '<tr>' + \
                '<th scope="col">' + sheet_electrolyseur_type_3.cell_value(1, 0) + '</th>' + \
                '<th scope="col">' + sheet_electrolyseur_type_3.cell_value(1, 1) + '</th>' + \
                '<th scope="col">' + sheet_electrolyseur_type_3.cell_value(1, 2) + '</th>' + \
                '<th scope="col">' + sheet_electrolyseur_type_3.cell_value(1, 3) + '</th>' + \
                '<th scope="col">' + sheet_electrolyseur_type_3.cell_value(1, 4) + '</th>' + \
                '<th scope="col">' + sheet_electrolyseur_type_3.cell_value(1, 5) + '</th>' + \
                '<th scope="col">' + sheet_electrolyseur_type_3.cell_value(1, 6) + '</th>' + \
                '<th scope="col">' + sheet_electrolyseur_type_3.cell_value(1, 7) + '</th>' + \
                '<th scope="col">' + sheet_electrolyseur_type_3.cell_value(1, 8) + '</th>' + \
                '<th scope="col">' + sheet_electrolyseur_type_3.cell_value(1, 9) + '</th>' + \
                '<th scope="col">' + sheet_electrolyseur_type_3.cell_value(1, 10) + '</th>' + \
                '<th scope="col">' + sheet_electrolyseur_type_3.cell_value(1, 11) + '</th>' + \
                '</tr>' + \
                '</thead>' + \
                '<tbody>'

        start_electrolyseur = int(sheet_electrolyseur_type_3.cell_value(0, 24)) - 1

        end_electrolyseur = int(sheet_electrolyseur_type_3.cell_value(0, 26))

        for i in range(start_electrolyseur, end_electrolyseur):
            body += '<tr>' + \
                    '<td>' + str(sheet_electrolyseur_type_3.cell_value(i, 0)) + '</td>' + \
                    '<td>' + str(round(sheet_electrolyseur_type_3.cell_value(i, 1), 2)) + '</td>' + \
                    '<td>' + str(round(sheet_electrolyseur_type_3.cell_value(i, 2), 2)) + '</td>' + \
                    '<td>' + str(sheet_electrolyseur_type_3.cell_value(i, 3)) + '</td>' + \
                    '<td>' + str(round(sheet_electrolyseur_type_3.cell_value(i, 4), 2)) + '</td>' + \
                    '<td>' + str(round(sheet_electrolyseur_type_3.cell_value(i, 5), 2)) + '</td>' + \
                    '<td>' + str(sheet_electrolyseur_type_3.cell_value(i, 6)) + '</td>' + \
                    '<td>' + str(round(sheet_electrolyseur_type_3.cell_value(i, 7), 2)) + '</td>' + \
                    '<td>' + str(round(sheet_electrolyseur_type_3.cell_value(i, 8), 2)) + '</td>' + \
                    '<td>' + str(round(sheet_electrolyseur_type_3.cell_value(i, 9), 2)) + '</td>' + \
                    '<td>' + str(round(sheet_electrolyseur_type_3.cell_value(i, 10), 2)) + '</td>' + \
                    '<td>' + str(sheet_electrolyseur_type_3.cell_value(i, 11)) + '</td>' + \
                    '</tr>'

        body += '</tbody>' + \
                '</table >' + \
                '<br>' + \
                '<br>' + \
                '<h6>Sorties</h6>' + \
                '<table class ="table table-striped table-bordered">' + \
                '<thead>' + \
                '<tr>' + \
                '<th scope="col">' + sheet_container_hydrogene_type_3.cell_value(1, 13) + '</th>' + \
                '<th scope="col">' + sheet_container_hydrogene_type_3.cell_value(1, 14) + '</th>' + \
                '<th scope="col">' + sheet_container_hydrogene_type_3.cell_value(1, 15) + '</th>' + \
                '<th scope="col">' + sheet_container_hydrogene_type_3.cell_value(1, 16) + '</th>' + \
                '<th scope="col">' + sheet_container_hydrogene_type_3.cell_value(1, 17) + '</th>' + \
                '<th scope="col">' + sheet_container_hydrogene_type_3.cell_value(1, 18) + '</th>' + \
                '<th scope="col">' + sheet_container_hydrogene_type_3.cell_value(1, 19) + '</th>' + \
                '<th scope="col">' + sheet_container_hydrogene_type_3.cell_value(1, 20) + '</th>' + \
                '<th scope="col">' + sheet_container_hydrogene_type_3.cell_value(1, 21) + '</th>' + \
                '</tr>' + \
                '</thead>' + \
                '<tbody>' + \
                '<tr>' + \
                '<td>' + str(sheet_electrolyseur_type_3.cell_value(2, 13)) + '</td>' + \
                '<td>' + str(round(sheet_electrolyseur_type_3.cell_value(2, 14), 2)) + '</td>' + \
                '<td>' + str(round(sheet_electrolyseur_type_3.cell_value(2, 15), 2)) + '</td>' + \
                '<td>' + str(round(sheet_electrolyseur_type_3.cell_value(2, 16), 2)) + '</td>' + \
                '<td>' + str(round(sheet_electrolyseur_type_3.cell_value(2, 17), 2)) + '</td>' + \
                '<td>' + str(round(sheet_electrolyseur_type_3.cell_value(2, 18), 2)) + '</td>' + \
                '<td>' + str(round(sheet_electrolyseur_type_3.cell_value(2, 19), 2)) + '</td>' + \
                '<td>' + str(round(sheet_electrolyseur_type_3.cell_value(2, 20), 2)) + '</td>' + \
                '<td>' + str(round(sheet_electrolyseur_type_3.cell_value(2, 21), 2)) + '</td>' + \
                '</tr>' + \
                '</tbody>' + \
                '</table >' + \
                '</div>' + \
                '</div>' + \
                '<br>'

        body += '<div class="card text-center">' + \
                '<div class="card-header">' + \
                '<h6>Chiffrage d' + "'un container hydrogène" + '</h6>' + \
                '</div>' + \
                '<div class="card-body">' + \
                '<h6>Entrées</h6>' + \
                '<table class ="table table-striped table-bordered">' + \
                '<thead>' + \
                '<tr>' + \
                '<th scope="col">' + sheet_container_hydrogene_type_3.cell_value(1, 0) + '</th>' + \
                '<th scope="col">' + sheet_container_hydrogene_type_3.cell_value(1, 1) + '</th>' + \
                '<th scope="col">' + sheet_container_hydrogene_type_3.cell_value(1, 2) + '</th>' + \
                '<th scope="col">' + sheet_container_hydrogene_type_3.cell_value(1, 3) + '</th>' + \
                '<th scope="col">' + sheet_container_hydrogene_type_3.cell_value(1, 4) + '</th>' + \
                '<th scope="col">' + sheet_container_hydrogene_type_3.cell_value(1, 5) + '</th>' + \
                '<th scope="col">' + sheet_container_hydrogene_type_3.cell_value(1, 6) + '</th>' + \
                '<th scope="col">' + sheet_container_hydrogene_type_3.cell_value(1, 7) + '</th>' + \
                '<th scope="col">' + sheet_container_hydrogene_type_3.cell_value(1, 8) + '</th>' + \
                '<th scope="col">' + sheet_container_hydrogene_type_3.cell_value(1, 9) + '</th>' + \
                '<th scope="col">' + sheet_container_hydrogene_type_3.cell_value(1, 10) + '</th>' + \
                '<th scope="col">' + sheet_container_hydrogene_type_3.cell_value(1, 11) + '</th>' + \
                '</tr>' + \
                '</thead>' + \
                '<tbody>'

        start_container_hydrogene = int(sheet_container_hydrogene_type_3.cell_value(0, 24)) - 1

        end_container_hydrogene = int(sheet_container_hydrogene_type_3.cell_value(0, 26))

        for i in range(start_container_hydrogene, end_container_hydrogene):
            body += '<tr>' + \
                    '<td>' + str(sheet_container_hydrogene_type_3.cell_value(i, 0)) + '</td>' + \
                    '<td>' + str(round(sheet_container_hydrogene_type_3.cell_value(i, 1), 2)) + '</td>' + \
                    '<td>' + str(round(sheet_container_hydrogene_type_3.cell_value(i, 2), 2)) + '</td>' + \
                    '<td>' + str(sheet_container_hydrogene_type_3.cell_value(i, 3)) + '</td>' + \
                    '<td>' + str(round(sheet_container_hydrogene_type_3.cell_value(i, 4), 2)) + '</td>' + \
                    '<td>' + str(round(sheet_container_hydrogene_type_3.cell_value(i, 5), 2)) + '</td>' + \
                    '<td>' + str(sheet_container_hydrogene_type_3.cell_value(i, 6)) + '</td>' + \
                    '<td>' + str(round(sheet_container_hydrogene_type_3.cell_value(i, 7), 2)) + '</td>' + \
                    '<td>' + str(round(sheet_container_hydrogene_type_3.cell_value(i, 8), 2)) + '</td>' + \
                    '<td>' + str(round(sheet_container_hydrogene_type_3.cell_value(i, 9), 2)) + '</td>' + \
                    '<td>' + str(round(sheet_container_hydrogene_type_3.cell_value(i, 10), 2)) + '</td>' + \
                    '<td>' + str(sheet_container_hydrogene_type_3.cell_value(i, 11)) + '</td>' + \
                    '</tr>'

        body += '</tbody>' + \
                '</table >' + \
                '<br>' + \
                '<br>' + \
                '<h6>Sorties</h6>' + \
                '<table class ="table table-striped table-bordered">' + \
                '<thead>' + \
                '<tr>' + \
                '<th scope="col">' + sheet_container_hydrogene_type_3.cell_value(1, 13) + '</th>' + \
                '<th scope="col">' + sheet_container_hydrogene_type_3.cell_value(1, 14) + '</th>' + \
                '<th scope="col">' + sheet_container_hydrogene_type_3.cell_value(1, 15) + '</th>' + \
                '<th scope="col">' + sheet_container_hydrogene_type_3.cell_value(1, 16) + '</th>' + \
                '<th scope="col">' + sheet_container_hydrogene_type_3.cell_value(1, 17) + '</th>' + \
                '<th scope="col">' + sheet_container_hydrogene_type_3.cell_value(1, 18) + '</th>' + \
                '<th scope="col">' + sheet_container_hydrogene_type_3.cell_value(1, 19) + '</th>' + \
                '<th scope="col">' + sheet_container_hydrogene_type_3.cell_value(1, 20) + '</th>' + \
                '<th scope="col">' + sheet_container_hydrogene_type_3.cell_value(1, 21) + '</th>' + \
                '</tr>' + \
                '</thead>' + \
                '<tbody>' + \
                '<tr>' + \
                '<td>' + str(sheet_container_hydrogene_type_3.cell_value(2, 13)) + '</td>' + \
                '<td>' + str(round(sheet_container_hydrogene_type_3.cell_value(2, 14), 2)) + '</td>' + \
                '<td>' + str(round(sheet_container_hydrogene_type_3.cell_value(2, 15), 2)) + '</td>' + \
                '<td>' + str(round(sheet_container_hydrogene_type_3.cell_value(2, 16), 2)) + '</td>' + \
                '<td>' + str(round(sheet_container_hydrogene_type_3.cell_value(2, 17), 2)) + '</td>' + \
                '<td>' + str(round(sheet_container_hydrogene_type_3.cell_value(2, 18), 2)) + '</td>' + \
                '<td>' + str(round(sheet_container_hydrogene_type_3.cell_value(2, 19), 2)) + '</td>' + \
                '<td>' + str(round(sheet_container_hydrogene_type_3.cell_value(2, 20), 2)) + '</td>' + \
                '<td>' + str(round(sheet_container_hydrogene_type_3.cell_value(2, 21), 2)) + '</td>' + \
                '</tr>' + \
                '</tbody>' + \
                '</table >' + \
                '</div>' + \
                '</div>' + \
                '<br>'

        body += '<br>' + \
                '</div>' + \
                '</div>' + \
                '</div>' + \
                '<br>' + \
                '<script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" ' \
                'integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" ' \
                'crossorigin="anonymous"></script>' + \
                '<script src="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/js/bootstrap.bundle.min.js" ' \
                'integrity="sha384-ho+j7jyWK8fNQe+A12Hb8AhRq26LrZ/JpcUGGOn+Y7RsweNrtN/tE3MoK7ZeZDyx" ' \
                'crossorigin="anonymous"></script>' + \
                '</body>' + \
                '</html>'

        options = {
            'page-size': 'A4',
            'header-center': "Chiffrage d'un container hydrogène",
            'footer-right': '[page] sur [topage]',
            'footer-left': 'Société Holomorphe [SIREN : 883632556]'
        }

        path_wkthmltopdf = "C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe"
        config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
        pdfkit.from_string(body, "Container_Hydrogene\\Chiffrage.pdf", configuration=config,
                           options=options)


if __name__ == '__main__':
    unittest.main()
