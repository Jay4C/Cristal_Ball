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


class EnregistrementsComptables(unittest.TestCase):
    def test_cadre_comptable_s_d(self):
        print("test_cadre_comptable_s_d")

        location = ("A:\\1_Professionnel\\1_Holomorphe\\1_Administration\\1_Comptabilite_Fiscalite\\1_Annee_2020\\Consolidation_Comptable_Fiscale_2020.xls")

        workbook = xlrd.open_workbook(location)

        sheet = workbook.sheet_by_name("Cadre_Comptable_S_D")

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
               '<title>Cadre_Comptable_S_D</title>' + \
               '</head>' + \
               '<body>' + \
               '<div class="container">' + \
               '<div class="card text-center">' + \
               '<div class="card-header text-center">Cadre comptable en système développé</div>' + \
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
               '<h4>' + str(sheet.cell_value(0, 0)) + '</h4>' + \
               '<br>' + \
               '<table class="table table-bordered">' + \
               '<thead>' + \
               '<tr>' + \
               '<th scope="col" colspan="3">' + str(sheet.cell_value(1, 0)) + '</th>' + \
               '</tr>' + \
               '<tr>' + \
               '<th scope="col">' + str(sheet.cell_value(2, 0)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(2, 1)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(2, 2)) + '</th>' + \
               '</tr>' + \
               '</thead>' + \
               '<tbody>'

        for i in range(3, 13):
            body += '<tr>' \
                    + '<td>' + str(round(sheet.cell_value(i, 0))) + '</td>' \
                    + '<td>' + str(sheet.cell_value(i, 1)) + '</td>' \
                    + '<td>' + str(round(float(sheet.cell_value(i, 2)), 2)) + '</td>' \
                    + '</tr>'

        body += '<tr>' + \
                '<td colspan="2"><b><i>' + str(sheet.cell_value(13, 0)) + '</i></b></td>' + \
                '<td>' + str(round(float(sheet.cell_value(13, 2)), 2)) + '</td>' + \
                '</tr>' + \
                '</tbody>' + \
                '</table>' + \
                '<br>' + \
               '<table class="table table-bordered">' + \
               '<thead>' + \
               '<tr>' + \
               '<th scope="col" colspan="3">' + str(sheet.cell_value(14, 0)) + '</th>' + \
               '</tr>' + \
               '<tr>' + \
               '<th scope="col">' + str(sheet.cell_value(15, 0)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(15, 1)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(15, 2)) + '</th>' + \
               '</tr>' + \
               '</thead>' + \
               '<tbody>'

        for i in range(16, 26):
            body += '<tr>' + \
                    '<td>' + str(round(sheet.cell_value(i, 0))) + '</td>' + \
                    '<td>' + str(sheet.cell_value(i, 1)) + '</td>' + \
                    '<td>' + str(round(float(sheet.cell_value(i, 2)), 2)) + '</td>' + \
                    '</tr>'

        body += '<tr>' + \
               '<td colspan="2"><b><i>' + str(sheet.cell_value(26, 0)) + '</i></b></td>' + \
               '<td>' + str(round(float(sheet.cell_value(26, 2)), 2)) + '</td>' + \
               '</tr>' + \
               '</tbody>' + \
               '</table>' + \
               '<br>' + \
               '<table class="table table-bordered">' + \
               '<thead>' + \
               '<tr>' + \
               '<th scope="col" colspan="3">' + str(sheet.cell_value(27, 0)) + '</th>' + \
               '</tr>' + \
               '<tr>' + \
               '<th scope="col">' + str(sheet.cell_value(28, 0)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(28, 1)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(28, 2)) + '</th>' + \
               '</tr>' + \
               '</thead>' + \
               '<tbody>'

        for i in range(29, 39):
            body += '<tr>' + \
                    '<td>' + str(round(sheet.cell_value(i, 0))) + '</td>' + \
                    '<td>' + str(sheet.cell_value(i, 1)) + '</td>' + \
                    '<td>' + str(round(float(sheet.cell_value(i, 2)), 2)) + '</td>' + \
                    '</tr>'

        body += '<tr>' + \
                '<td colspan="2"><b><i>' + str(sheet.cell_value(39, 0)) + '</i></b></td>' + \
                '<td>' + str(round(float(sheet.cell_value(39, 2)), 2)) + '</td>' + \
                '</tr>' + \
                '</tbody>' + \
                '</table>' + \
                '<br>' + \
                '<table class="table table-bordered">' + \
                '<thead>' + \
                '<tr>' + \
                '<th scope="col" colspan="3">' + str(sheet.cell_value(40, 0)) + '</th>' + \
                '</tr>' + \
                '<tr>' + \
                '<th scope="col">' + str(sheet.cell_value(41, 0)) + '</th>' + \
                '<th scope="col">' + str(sheet.cell_value(41, 1)) + '</th>' + \
                '<th scope="col">' + str(sheet.cell_value(41, 2)) + '</th>' + \
                '</tr>' + \
                '</thead>' + \
                '<tbody>'

        for i in range(42, 52):
            body += '<tr>' + \
                    '<td>' + str(round(sheet.cell_value(i, 0))) + '</td>' + \
                    '<td>' + str(sheet.cell_value(i, 1)) + '</td>' + \
                    '<td>' + str(round(float(sheet.cell_value(i, 2)), 2)) + '</td>' + \
                    '</tr>'

        body += '<tr>' + \
                '<td colspan="2"><b><i>' + str(sheet.cell_value(52, 0)) + '</i></b></td>' + \
                '<td>' + str(round(float(sheet.cell_value(52, 2)), 2)) + '</td>' + \
                '</tr>' + \
                '</tbody>' + \
                '</table>' + \
                '<br>' + \
                '<table class="table table-bordered">' + \
                '<thead>' + \
               '<tr>' + \
               '<th scope="col" colspan="3">' + str(sheet.cell_value(53, 0)) + '</th>' + \
               '</tr>' + \
               '<tr>' + \
               '<th scope="col">' + str(sheet.cell_value(54, 0)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(54, 1)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(54, 2)) + '</th>' + \
               '</tr>' + \
               '</thead>' + \
               '<tbody>'

        for i in range(55, 65):
            body += '<tr>' + \
                    '<td>' + str(round(sheet.cell_value(i, 0))) + '</td>' + \
                    '<td>' + str(sheet.cell_value(i, 1)) + '</td>' + \
                    '<td>' + str(round(float(sheet.cell_value(i, 2)), 2)) + '</td>' + \
                    '</tr>'

        body += '<tr>' + \
                '<td colspan="2"><b><i>' + str(sheet.cell_value(65, 0)) + '</i></b></td>' + \
                '<td>' + str(round(float(sheet.cell_value(65, 2)), 2)) + '</td>' + \
                '</tr>' + \
                '</tbody>' + \
                '</table>' + \
                '<br>' + \
                '<h4>' + str(sheet.cell_value(0, 4)) + '</h4>' + \
                '<br>' + \
                '<table class="table table-bordered">' + \
                '<thead>' + \
                '<tr>' + \
                '<th scope="col" colspan="3">' + str(sheet.cell_value(1, 4)) + '</th>' + \
                '</tr>' + \
                '<tr>' + \
                '<th scope="col">' + str(sheet.cell_value(2, 4)) + '</th>' + \
                '<th scope="col">' + str(sheet.cell_value(2, 5)) + '</th>' + \
                '<th scope="col">' + str(sheet.cell_value(2, 6)) + '</th>' + \
                '</tr>' + \
                '</thead>' + \
                '<tbody>'

        for i in range(3, 14):
            body += '<tr>' + \
                    '<td>' + str(round(sheet.cell_value(i, 4))) + '</td>' + \
                    '<td>' + str(sheet.cell_value(i, 5)) + '</td>' + \
                    '<td>' + str(round(float(sheet.cell_value(i, 6)), 2)) + '</td>' + \
                    '</tr>'

        body += '<tr>' + \
                '<td colspan="2"><b><i>' + str(sheet.cell_value(14, 4)) + '</i></b></td>' + \
                '<td>' + str(round(float(sheet.cell_value(14, 6)), 2)) + '</td>' + \
                '</tr>' + \
                '</tbody>' + \
                '</table>' + \
                '<br>' + \
                '<table class="table table-bordered">' + \
                '<thead>' + \
                '<tr>' + \
                '<th scope="col" colspan="3">' + str(sheet.cell_value(15, 4)) + '</th>' + \
                '</tr>' + \
                '<tr>' + \
                '<th scope="col">' + str(sheet.cell_value(16, 4)) + '</th>' + \
                '<th scope="col">' + str(sheet.cell_value(16, 5)) + '</th>' + \
                '<th scope="col">' + str(sheet.cell_value(16, 6)) + '</th>' + \
                '</tr>' + \
                '</thead>' + \
                '<tbody>'

        for i in range(17, 27):
            body += '<tr>' + \
                    '<td>' + str(round(sheet.cell_value(i, 4))) + '</td>' + \
                    '<td>' + str(sheet.cell_value(i, 5)) + '</td>' + \
                    '<td>' + str(round(float(sheet.cell_value(i, 6)), 2)) + '</td>' + \
                    '</tr>'

        body += '<tr>' + \
                '<td colspan="2"><b><i>' + str(sheet.cell_value(27, 4)) + '</i></b></td>' + \
                '<td>' + str(round(float(sheet.cell_value(27, 6)), 2)) + '</td>' + \
                '</tr>' + \
                '</tbody>' + \
                '</table>' + \
                '<br>' + \
                '<h4>' + str(sheet.cell_value(0, 8)) + '</h4>' + \
                '<br>' + \
                '<table class="table table-bordered">' + \
                '<thead>' + \
                '<tr>' + \
                '<th scope="col" colspan="3">' + str(sheet.cell_value(1, 8)) + '</th>' + \
                '</tr>' + \
                '<tr>' + \
                '<th scope="col">' + str(sheet.cell_value(2, 8)) + '</th>' + \
                '<th scope="col">' + str(sheet.cell_value(2, 9)) + '</th>' + \
                '<th scope="col">' + str(sheet.cell_value(2, 10)) + '</th>' + \
                '</tr>' + \
                '</thead>' + \
                '<tbody>'

        for i in range(3, 6):
            body += '<tr>' + \
                    '<td>' + str(round(sheet.cell_value(i, 8))) + '</td>' + \
                    '<td>' + str(sheet.cell_value(i, 9)) + '</td>' + \
                    '<td>' + str(round(float(sheet.cell_value(i, 10)), 2)) + '</td>' + \
                    '</tr>'

        body += '<tr>' + \
                '<td colspan="2"><b><i>' + str(sheet.cell_value(6, 8)) + '</i></b></td>' + \
                '<td>' + str(sheet.cell_value(6, 10)) + '</td>' + \
                '</tr>' + \
                '</tbody>' + \
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

        excel_date_1 = round(
            float(str(workbook.sheet_by_name("Informations_Entreprise").cell_value(9, 1)).split(".")[0]))

        python_date = xlrd.xldate_as_tuple(excel_date_1, 0)

        x = datetime.datetime(python_date[0], python_date[1], python_date[2])

        clos_le = x.strftime("%d/%m/%Y")

        options = {
            'page-size': 'A4',
            'header-right': 'Société HOLOMORPHE [SIREN : 883 632 556]',
            'header-left': 'Exercice clos le ' + clos_le,
            'footer-left': "Cadre comptable en système \n développé de l'exercice " + str(round(float(str(workbook.sheet_by_name("Informations_Entreprise").cell_value(8, 1)).split(".")[0]))),
            'footer-right': '[page] sur [topage]'
        }

        path_wkthmltopdf = "C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe"
        config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
        pdfkit.from_string(body, "Enregistrements_Comptables\\Cadre_Comptable_S_D\\Cadre_Comptable_S_D.pdf", configuration=config, options=options)

        filename = "Enregistrements_Comptables\\Cadre_Comptable_S_D\\Cadre_Comptable_S_D.pdf"

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

    def test_livre_journal(self):
        print("test_livre_journal")

        location = ("A:\\1_Professionnel\\1_Holomorphe\\1_Administration\\1_Comptabilite_Fiscalite\\1_Annee_2020\\Consolidation_Comptable_Fiscale_2020.xls")

        workbook = xlrd.open_workbook(location)

        sheet = workbook.sheet_by_name("Livre_Journal")

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

        nb_rows = 151

        # Rapport
        body = '<!doctype html>' + \
               '<html lang="en">' + \
               '<head>' + \
               '<meta charset="utf-8">' + \
               '<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">' + \
               '<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css" integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">' + \
               '<title>Livre_Journal</title>' + \
               '</head>' + \
               '<body>' + \
               '<div class="container">' + \
               '<div class="card text-center">' + \
               '<div class="card-header text-center">Livre-journal</div>' + \
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
               '<h5>' + str(sheet.cell_value(0, 5)) + ' = ' + str(round(float(sheet.cell_value(1, 5)), 2)) + '</h5>' + \
               '<h5>' + str(sheet.cell_value(0, 6)) + ' = ' + str(round(float(sheet.cell_value(1, 6)), 2)) + '</h5>' + \
               '<br>' + \
               '<br>' + \
               '<h4><u>Partie 1</u></h4>' + \
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
               '</tr>' + \
               '</thead>' + \
               '<tbody>'

        for i in range(3, nb_rows):
            if str(sheet.cell_value(i, 1)) == '':
                body += '<tr>' + \
                        '<td colspan="9"><b>' + str(sheet.cell_value(i, 0)) + '</b></td>' + \
                        '</tr>'

            elif str(sheet.cell_value(i, 1)) != '':
                excel_date = int(str(sheet.cell_value(i, 1)).split(".")[0])

                python_date = xlrd.xldate_as_tuple(excel_date, 0)

                x = datetime.datetime(python_date[0], python_date[1], python_date[2])

                date_accounting = x.strftime("%d/%m/%Y")

                body += '<tr>' + \
                        '<td>' + str(sheet.cell_value(i, 0)).split(".")[0] + '</td>' + \
                        '<td>' + date_accounting + '</td>' + \
                        '<td>' + str(round(float(sheet.cell_value(i, 2)))) + '</td>' + \
                        '<td>' + str(sheet.cell_value(i, 3)) + '</td>' + \
                        '<td>' + str(sheet.cell_value(i, 4)) + '</td>' + \
                        '<td>' + str(round(float(sheet.cell_value(i, 5)), 2)) + '</td>' + \
                        '<td>' + str(round(float(sheet.cell_value(i, 6)), 2)) + '</td>' + \
                        '</tr>'

        body += '</tbody>' + \
                '</table>' + \
                '<br>' + \
                '<br>' + \
                '<h4><u>Partie 2</u></h4>' + \
                '<br>' + \
                '<table class="table table-bordered">' + \
                '<thead>' + \
                '<tr>' + \
                '<th scope="col">' + str(sheet.cell_value(2, 0)) + '</th>' + \
                '<th scope="col">' + str(sheet.cell_value(2, 7)) + '</th>' + \
                '<th scope="col">' + str(sheet.cell_value(2, 8)) + '</th>' + \
                '</tr>' + \
                '</thead>' + \
                '<tbody>'

        for i in range(3, nb_rows):
            if str(sheet.cell_value(i, 1)) == '':
                body += '<tr>' + \
                        '<td colspan="9"><b>' + str(sheet.cell_value(i, 0)) + '</b></td>' + \
                        '</tr>'

            elif str(sheet.cell_value(i, 1)) != '':
                body += '<tr>' + \
                        '<td>' + str(sheet.cell_value(i, 0)).split(".")[0] + '</td>' + \
                        '<td>' + str(sheet.cell_value(i, 7)) + '</td>' + \
                        '<td>' + str(sheet.cell_value(i, 8)) + '</td>' + \
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

        excel_date_1 = round(
            float(str(workbook.sheet_by_name("Informations_Entreprise").cell_value(9, 1)).split(".")[0]))

        python_date = xlrd.xldate_as_tuple(excel_date_1, 0)

        x = datetime.datetime(python_date[0], python_date[1], python_date[2])

        clos_le = x.strftime("%d/%m/%Y")

        options = {
            'page-size': 'A4',
            'header-right': 'Société HOLOMORPHE [SIREN : 883 632 556]',
            'header-left': 'Exercice clos le ' + clos_le,
            'footer-left': "Livre-journal de l'exercice " + str(round(float(str(workbook.sheet_by_name("Informations_Entreprise").cell_value(8, 1)).split(".")[0]))),
            'footer-right': '[page] sur [topage]'
        }

        path_wkthmltopdf = "C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe"
        config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
        pdfkit.from_string(body, "Enregistrements_Comptables\\Livre_Journal\\Livre_Journal.pdf", configuration=config, options=options)

        filename = "Enregistrements_Comptables\\Livre_Journal\\Livre_Journal.pdf"

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

    def test_grand_livre_general(self):
        print("test_grand_livre_general")

        location = ("A:\\1_Professionnel\\1_Holomorphe\\1_Administration\\1_Comptabilite_Fiscalite\\1_Annee_2020\\Consolidation_Comptable_Fiscale_2020.xls")

        workbook = xlrd.open_workbook(location)

        sheet = workbook.sheet_by_name("Grand_Livre_General")

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

        nb_c = 17

        nb_r = 40

        body = '<!doctype html>' + \
               '<html lang="en">' + \
               '<head>' + \
               '<meta charset="utf-8">' + \
               '<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">' + \
               '<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css" integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">' + \
               '<title>Grand_Livre_General</title>' + \
               '</head>' + \
               '<body>' + \
               '<div class="container">' + \
               '<div class="card text-center">' + \
               '<div class="card-header text-center">Grand livre journal</div>' + \
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
               '<th scope="col">' + str(sheet.cell_value(0, 0)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(0, 1)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(0, 2)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(0, 3)) + '</th>' + \
               '</tr>' + \
               '</thead>' + \
               '<tbody>'

        for i in range(1, 8):
            body += '<tr>' + \
                    '<td>' + str(sheet.cell_value(i, 0)).split(".")[0] + '</td>' + \
                    '<td>' + str(round(float(sheet.cell_value(i, 1)), 2)) + '</td>' + \
                    '<td>' + str(round(float(sheet.cell_value(i, 2)), 2)) + '</td>' + \
                    '<td>' + str(round(float(sheet.cell_value(i, 3)), 2)) + '</td>' + \
                    '</tr>'

        body += '<tr>' + \
                '<td><b>' + str(sheet.cell_value(8, 0)).split(".")[0] + '</b></td>' + \
                '<td><b>' + str(round(float(sheet.cell_value(8, 1)), 2)) + '</b></td>' + \
                '<td><b>' + str(round(float(sheet.cell_value(8, 2)), 2)) + '</b></td>' + \
                '<td><b>' + str(round(float(sheet.cell_value(8, 3)), 2)) + '</b></td>' + \
                '</tr>' + \
                '</tbody>' + \
                '</table>' + \
                '<br>' + \
                '<br>'

        for c in range(0, nb_c):
            try:
                c0 = c*9 + 5
                c1 = c*9 + 6
                c2 = c*9 + 7
                c3 = c*9 + 8
                c4 = c*9 + 9
                c5 = c*9 + 10
                c6 = c*9 + 11
                c7 = c*9 + 12

                body += '<table class="table table-bordered">' + \
                   '<thead>' + \
                   '<tr>' + \
                   '<th scope="col" colspan="4">Total du compte</th>' + \
                   '<th scope="col"><i>' + str(round(float(sheet.cell_value(0, c4)), 2)) + '</i></th>' + \
                   '<th scope="col"><i>' + str(round(float(sheet.cell_value(0, c5)), 2)) + '</i></th>' + \
                   '<th scope="col"><i>' + str(round(float(sheet.cell_value(0, c6)), 2)) + '</i></th>' + \
                   '<th scope="col">Code du lettrage</th>' + \
                   '</tr>' + \
                   '<tr>' + \
                   '<th scope="col">Numéro du compte du plan de compte général</th>' + \
                   '<th scope="col"><i>' + str(round(float(sheet.cell_value(1, c1)), 2)).split(".")[0] + '</i></th>' + \
                   '<th scope="col">Intitulé du compte du plan de compte général</th>' + \
                   '<th scope="col"><i>' + str(sheet.cell_value(1, c3)) + '</i></th>' + \
                   '<th scope="col">Débit (Entrée de valeurs) [€]</th>' + \
                   '<th scope="col">Crédit (Sortie de valeurs) [€]</th>' + \
                   '<th scope="col">Solde progressif [€]</th>' + \
                   '<th scope="col">-</th>' + \
                   '</tr>' + \
                   '<tr>' + \
                   '<th scope="col">Date de l' + "'opération" + '</th>' + \
                   '<th scope="col">Type de journal</th>' + \
                   '<th scope="col">Numéro d' + "'enregistrement ou pièce</th>" + \
                   '<th scope="col">Libellé</th>' + \
                   '<th scope="col" colspan="4">Ecritures des débits, crédits, soldes progressif et lettrages</th>' + \
                   '</tr>' + \
                   '</thead>' + \
                   '<tbody>'

                for r in range(3, nb_r):
                    try:
                        if str(sheet.cell_value(r, c0)) != '':
                            excel_date = round(float(str(sheet.cell_value(r, c0)).split(".")[0]))

                            python_date = xlrd.xldate_as_tuple(excel_date, 0)

                            x = datetime.datetime(python_date[0], python_date[1], python_date[2])

                            date_accounting = x.strftime("%d/%m/%Y")

                            body += '<tr>' + \
                                    '<td>' + date_accounting + '</td>' + \
                                    '<td>' + str(sheet.cell_value(r, c1)) + '</td>' + \
                                    '<td>' + str(sheet.cell_value(r, c2)).split(".")[0] + '</td>' + \
                                    '<td>' + str(sheet.cell_value(r, c3)) + '</td>' + \
                                    '<td>' + str(round(float(sheet.cell_value(r, c4)), 2)) + '</td>' + \
                                    '<td>' + str(round(float(sheet.cell_value(r, c5)), 2)) + '</td>' + \
                                    '<td>' + str(round(float(sheet.cell_value(r, c6)), 2)) + '</td>' + \
                                    '<td>' + str(sheet.cell_value(r, c7)) + '</td>' + \
                                    '<tr>'
                        else:
                            break

                    except Exception as e:
                        print("error 1 : " + str(e))
                        break

                body += '</tbody>' + \
                        '</table>' + \
                        '<br>' + \
                        '<br>'

            except Exception as e:
                print("error 2 : " + str(e))
                break

        body += '<br>' + \
                '</div>' + \
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
            'footer-left': "Grand livre journal de l'exercice " + str(round(float(str(workbook.sheet_by_name("Informations_Entreprise").cell_value(8, 1)).split(".")[0]))),
            'footer-right': '[page] sur [topage]'
        }

        path_wkthmltopdf = "C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe"
        config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
        pdfkit.from_string(body, "Enregistrements_Comptables\\Grand_Livre_General\\Grand_Livre_General.pdf", configuration=config, options=options)

        filename = "Enregistrements_Comptables\\Grand_Livre_General\\Grand_Livre_General.pdf"

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
