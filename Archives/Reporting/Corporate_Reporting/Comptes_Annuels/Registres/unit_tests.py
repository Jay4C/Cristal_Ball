import unittest
import xlrd
import pdfkit
import datetime
from datetime import datetime as dt
import os, shutil
from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

annee = "2021"

location = (
    "A:\\1_Professionnel\\1_Holomorphe\\1_Administration\\1_Comptabilite_Fiscalite\\2_Annee_2021"
    "\\Consolidation_Comptable_Fiscale_2021.xls"
)

exercice = "2_Exercice_01_01_2021__31_12_2021"


class Registres_Holomorphe(unittest.TestCase):
    #
    def test_liste_actionnaires(self):
        print("test_liste_actionnaires")

        annee = "2020"

        location = ("A:\\1_Professionnel\\1_Holomorphe\\1_Administration\\1_Comptabilite_Fiscalite\\1_Annee_2020\\Consolidation_Comptable_Fiscale_2020.xls")

        workbook = xlrd.open_workbook(location)

        sheet = workbook.sheet_by_name("Liste_Des_Actionnaires")

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
               '<title>Liste_Des_Actionnaires</title>' + \
               '</head>' + \
               '<body>' + \
               '<div class="container">' + \
               '<div class="card text-center">' + \
               '<div class="card-header text-center">Liste des actionnaires</div>' + \
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

        body += '<table class="table table-bordered">' + \
                '<tbody>' + \
                '<tr>' + \
                '<td><b>' + str(sheet.cell_value(1, 0)) + '</b></td>' + \
                '<td>' + str(sheet.cell_value(1, 1)) + '</td>' + \
                '</tr>' + \
                '</tbody>' + \
                '</table>' + \
                '<br>' + \
                '<table class="table table-bordered">' + \
                '<tbody>' + \
                '<tr>' + \
                '<td colspan="2"><b>' + str(sheet.cell_value(3, 0)) + '</b></td>' + \
                '</tr>' + \
                '<tr>' + \
                '<td><b>' + str(sheet.cell_value(4, 0)) + '</b></td>' + \
                '<td><b>' + str(sheet.cell_value(4, 1)) + '</b></td>' + \
                '</tr>' + \
                '<tr>' + \
                '<td>' + str(sheet.cell_value(5, 0)) + '</td>' + \
                '<td>' + str(sheet.cell_value(5, 1)) + '</td>' + \
                '</tr>' + \
                '</tbody>' + \
                '</table>' + \
                '<br>' + \
                '<table class="table table-bordered">' + \
                '<tbody>' + \
                '<tr>' + \
                '<td colspan="4"><b>' + str(sheet.cell_value(7, 0)) + '</b></td>' + \
                '</tr>' + \
                '<tr>' + \
                '<td><b>' + str(sheet.cell_value(8, 0)) + '</b></td>' + \
                '<td><b>' + str(sheet.cell_value(8, 1)) + '</b></td>' + \
                '<td><b>' + str(sheet.cell_value(8, 2)) + '</b></td>' + \
                '<td><b>' + str(sheet.cell_value(8, 3)) + '</b></td>' + \
                '</tr>'

        start = 9
        end = 9

        for i in range(start, end + 1):
            body += '<tr>' + \
                    '<td>' + str(sheet.cell_value(i, 0)) + '</td>' + \
                    '<td>' + str(sheet.cell_value(i, 1)) + '</td>' + \
                    '<td>' + str(sheet.cell_value(i, 2)) + '</td>' + \
                    '<td>' + str(sheet.cell_value(i, 3)) + '</td>' + \
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

        excel_date_1 = round(float(str(workbook.sheet_by_name("Informations_Entreprise")
                                       .cell_value(9, 1)).split(".")[0]))

        python_date = xlrd.xldate_as_tuple(excel_date_1, 0)

        x = datetime.datetime(python_date[0], python_date[1], python_date[2])

        clos_le = x.strftime("%d/%m/%Y")

        options = {
            'page-size': 'A4',
            'header-right': 'Société HOLOMORPHE [SIREN : 883 632 556]',
            'header-left': 'Exercice clos le ' + clos_le,
            'footer-left': "Liste des actionnaires de \n l'exercice " + str(round(float(str(workbook.sheet_by_name("Informations_Entreprise").cell_value(8, 1)).split(".")[0]))),
            'footer-right': '[page] sur [topage]'
        }

        path_wkthmltopdf = "C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe"

        config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)

        pdfkit.from_string(body,
                           "Liste_Actionnaires\\Holomorphe\\Annee_" + annee + "\\Liste_Actionnaires.pdf",
                           configuration=config,
                           options=options)

        filename = "Liste_Actionnaires\\Holomorphe\\Annee_" + annee + "\\Liste_Actionnaires.pdf"

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

    #
    def test_registre_mouvements_titres(self):
        print("test_registre_mouvements_titres")

        annee = "2020"

        location = ("A:\\1_Professionnel\\1_Holomorphe\\1_Administration\\1_Comptabilite_Fiscalite\\1_Annee_2020\\Consolidation_Comptable_Fiscale_2020.xls")

        workbook = xlrd.open_workbook(location)

        sheet = workbook.sheet_by_name("Registre_Mouvements_Titres")

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
               '<title>Registre_Mouvements_Titres</title>' + \
               '</head>' + \
               '<body>' + \
               '<div class="container">' + \
               '<div class="card text-center">' + \
               '<div class="card-header text-center">Registre de mouvements de titres</div>' + \
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

        body += '<table class="table table-bordered">' + \
                '<tbody>' + \
                '<tr>'

        for i in range(0, 16):
            body += '<td><b>' + str(sheet.cell_value(1, i)) + '</b></td>'

        body += '</tr>'

        start = 2
        end = 2

        for r in range(start, end + 1):
            body += '<tr>'

            for i in range(0, 16):
                body += '<td>' + str(sheet.cell_value(r, i)).replace(".0", "") + '</td>'

            body += '</tr>'

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

        excel_date_1 = round(float(str(workbook.sheet_by_name("Informations_Entreprise")
                                       .cell_value(9, 1)).split(".")[0]))

        python_date = xlrd.xldate_as_tuple(excel_date_1, 0)

        x = datetime.datetime(python_date[0], python_date[1], python_date[2])

        clos_le = x.strftime("%d/%m/%Y")

        options = {
            'page-size': 'A4',
            'orientation': 'Landscape',
            'header-right': 'Société HOLOMORPHE [SIREN : 883 632 556]',
            'header-left': 'Exercice clos le ' + clos_le,
            'footer-left': "Registre des mouvements de titres de \n l'exercice " + str(round(float(str(workbook.sheet_by_name("Informations_Entreprise").cell_value(8, 1)).split(".")[0]))),
            'footer-right': '[page] sur [topage]'
        }

        path_wkthmltopdf = "C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe"

        config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)

        pdfkit.from_string(body,
                           "Registre_Mouvements_Titres\\Holomorphe\\Annee_" + annee + "\\Registre_Mouvements_Titres.pdf",
                           configuration=config,
                           options=options)

        filename = "Registre_Mouvements_Titres\\Holomorphe\\Annee_" + annee + "\\Registre_Mouvements_Titres.pdf"

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

    #
    def test_registre_beneficiaires_effectifs(self):
        print("test_registre_beneficiaires_effectifs")

        annee = "2020"

        location = ("A:\\1_Professionnel\\1_Holomorphe\\1_Administration\\1_Comptabilite_Fiscalite\\1_Annee_2020\\Consolidation_Comptable_Fiscale_2020.xls")

        workbook = xlrd.open_workbook(location)

        sheet = workbook.sheet_by_name("Registre_Beneficiaires_Effectifs")

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
               '<title>Registre_Beneficiaires_Effectifs</title>' + \
               '</head>' + \
               '<body>' + \
               '<div class="container">' + \
               '<div class="card text-center">' + \
               '<div class="card-header text-center">Registre des bénéficiaires effectifs</div>' + \
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

        body += '<table class="table table-bordered">' + \
                '<tbody>' + \
                '<tr>'

        for i in range(0, 15):
            body += '<td><b>' + str(sheet.cell_value(1, i)) + '</b></td>'

        body += '</tr>'

        start = 2
        end = 2

        for r in range(start, end + 1):
            body += '<tr>'

            for i in range(0, 15):
                body += '<td>' + str(sheet.cell_value(r, i)) + '</td>'

            body += '</tr>'

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

        excel_date_1 = round(float(str(workbook.sheet_by_name("Informations_Entreprise")
                                       .cell_value(9, 1)).split(".")[0]))

        python_date = xlrd.xldate_as_tuple(excel_date_1, 0)

        x = datetime.datetime(python_date[0], python_date[1], python_date[2])

        clos_le = x.strftime("%d/%m/%Y")

        options = {
            'page-size': 'A4',
            'orientation': 'Landscape',
            'header-right': 'Société HOLOMORPHE [SIREN : 883 632 556]',
            'header-left': 'Exercice clos le ' + clos_le,
            'footer-left': "Registre des bénéficiaires effectifs de \n l'exercice " + str(round(float(str(workbook.sheet_by_name("Informations_Entreprise").cell_value(8, 1)).split(".")[0]))),
            'footer-right': '[page] sur [topage]'
        }

        path_wkthmltopdf = "C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe"

        config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)

        pdfkit.from_string(body,
                           "Registre_Beneficiaires_Effectifs\\Holomorphe\\Annee_" + annee + "\\Registre_Beneficiaires_Effectifs.pdf",
                           configuration=config,
                           options=options)

        filename = "Registre_Beneficiaires_Effectifs\\Registre_Beneficiaires_Effectifs.pdf"

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

    #
    def test_proces_verbal_decisions_associe_unique_sasu(self):
        print("test_proces_verbal_decisions_associe_unique_sasu")

        workbook = xlrd.open_workbook(location)

        sheet = workbook.sheet_by_name("Proces_Verbal_Descisions_Associe_Unique")

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

        # Report
        body = '<!doctype html>' + \
               '<html lang="en">' + \
               '<head>' + \
               '<meta charset="utf-8">' + \
               '<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">' + \
               '<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css" integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">' + \
               '<title>Proces_Verbal_Descisions_Associe_Unique</title>' + \
               '</head>' + \
               '<body>' + \
               '<div class="container">' + \
               '<div class="card text-center">' + \
               '<div class="card-header text-center">Procès verbal des déscisions de l' + "'" + 'associé unique</div>' + \
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

        body += '<h6>' + \
                str(sheet.cell_value(2, 0)) + \
                ' demeurant au ' + str(sheet.cell_value(5, 0)) + \
                ", associé unique de la société HOLOMORPHE, " \
                "a pris les décisions concernant l'ordre du jour suivant:" + \
                '<br>' + \
                '- Description de la décision : ' + str(sheet.cell_value(8, 0)) + \
                '<br>' + \
                '- Modification de l’article [' + str(sheet.cell_value(11, 0)) + '] des statuts : ' + \
                str(sheet.cell_value(12, 0)) + \
                '</h6>' + \
                '<br>' + \
                '<h6>Première résolution [à adapter à la décision] : ' + str(sheet.cell_value(14, 0)) + '</h6>' + \
                '<br>' + \
                '<h6>Deuxième résolution [à adapter à la décision] : ' + str(sheet.cell_value(16, 0)) + '</h6>' + \
                '<br>' + \
                '<h6>Troisième résolution [à adapter à la décision] : ' + str(sheet.cell_value(18, 0)) + '</h6>' + \
                '<br>' + \
                '<h6>L’associé unique, ' + str(sheet.cell_value(21, 0)) + '</h6>'

        body += '<br>' + \
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
            'orientation': 'Landscape',
            'header-right': 'Société HOLOMORPHE [SIREN : 883 632 556]',
            'header-left': 'Exercice clos le ' + clos_le,
            'footer-left': "Procès verbal des décisions de l'associé unique de \n l'exercice " + str(round(float(str(workbook.sheet_by_name("Informations_Entreprise").cell_value(8, 1)).split(".")[0]))),
            'footer-right': '[page] sur [topage]'
        }

        path_wkthmltopdf = "C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe"

        config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)

        pdfkit.from_string(body,
                           "PV_D_Associe_Unique\\Holomorphe\\" + annee + "\\PV_D_Associe_Unique.pdf",
                           configuration=config,
                           options=options)

        filename = "PV_D_Associe_Unique\\Holomorphe\\" + annee + "\\PV_D_Associe_Unique.pdf"

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

        # PV_D_Associe_Unique
        proces_verbal_decisions_associe_unique_folder = "PV_D_Associe_Unique\\Holomorphe\\" + annee

        proces_verbal_decisions_associe_unique_folder_files = os.listdir(proces_verbal_decisions_associe_unique_folder)

        proces_verbal_decisions_associe_unique_filename = ""

        for f in proces_verbal_decisions_associe_unique_folder_files:
            if "signed" in f:
                proces_verbal_decisions_associe_unique_filename += f
                print("proces_verbal_decisions_associe_unique_filename : "
                      + proces_verbal_decisions_associe_unique_filename)
                break

        proces_verbal_decisions_associe_unique = proces_verbal_decisions_associe_unique_folder + "\\" \
                                                 + proces_verbal_decisions_associe_unique_filename

        exercice = "1_Exercice_01_04_2020__31_12_2020"

        shutil.copy(proces_verbal_decisions_associe_unique, "A:\\1_Professionnel\\1_Holomorphe\\1_Administration\\2_Gestion_Declarations_Administratives"
            "\\1_Recurrentes\\5_Infogreffe\\4_Approbation_Comptes_Sociaux\\"
            + exercice + "\\PV_Decisions_Associe_Unique.pdf")

    # ok
    def test_proces_verbal_approbation_des_comptes_annuels(self):
        print("test_proces_verbal_approbation_des_comptes_annuels")

        workbook = xlrd.open_workbook(location)

        sheet = workbook.sheet_by_name("Proces_Verbal_Approbation_Comptes_Annuels")

        # Informations generales entreprise
        denomination_sociale = "S.A.S.U. à capital variable HOLOMORPHE"
        capital_social = "100 euros"
        adresse_siege_social = "31 Avenue de Ségur - ABC LIV Ségur - 75007 Paris"
        siret = "88363255600014"
        rcs = "R.C.S. PARIS - Greffe du Tribunal de Commerce de PARIS"
        activite = "Commerce de gros (commerce interentreprises) de produits chimiques"
        code_naf = "4675Z"
        numero_tva_intracommunataire = "FR06883632556"
        president = "Monsieur "
        date_immatriculation = "26 Mai 2020"

        # Rapport
        body = '<!doctype html>' + \
               '<html lang="en">' + \
               '<head>' + \
               '<meta charset="utf-8">' + \
               '<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">' + \
               '<link rel="stylesheet" ' \
               'href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css" ' \
               'integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" ' \
               'crossorigin="anonymous">' + \
               '<title>Proces_Verbal_Approbation_Comptes_Annuels</title>' + \
               '</head>' + \
               '<body>' + \
               '<div class="container">' + \
               '<div class="card text-center">' + \
               '<div class="card-header text-center">Procès verbal d' + "'" + 'approbation des comptes annuels et d' \
               + "'" + 'affectation du résultat</div>' + \
               '<div class="card-body">' + \
               '<h6>Dénomination sociale : ' + denomination_sociale + ' / Capital social : ' \
               + capital_social + '</h6>' + \
               '<h6>Adresse du siège social : ' + adresse_siege_social + ' / SIRET : ' \
               + siret + '</h6>' + \
               '<h6>Registre de Commerce et des Sociétés : ' + rcs + '</h6>' + \
               '<h6>Activité : ' + activite + ' / Code NAF : ' + code_naf + '</h6>' + \
               '<h6>N° TVA intracommunataire : ' + numero_tva_intracommunataire + ' / Président : ' \
               + president + " / Date d'immatriculation : " + date_immatriculation + '</h6>' + \
               '<br>'

        body += '<h6>' + \
                str(sheet.cell_value(2, 0,)) + \
                ' demeurant au ' + \
                str(sheet.cell_value(5, 0)) + \
                ", associé unique de la société Holomorphe, a pris les décisions concernant l'ordre du jour suivant: " + \
                '<br>' + \
                '- Description des décisions : ' + \
                str(sheet.cell_value(8, 0)) + \
                '<br>' + \
                '- Modification des statuts : ' + str(sheet.cell_value(11, 0)) + \
                str(sheet.cell_value(12, 0)) + \
                '</h6>' + \
                '<br>'

        body += '<h6>' + \
                'Première résolution : approbation des comptes annuels' + \
                '<br>' + \
                "L'associé unique approuve les comptes de l’exercice clos en " + \
                str(sheet.cell_value(16, 0)) + \
                ' et se soldant par ' + \
                str(sheet.cell_value(18, 0)) + ' ' + str(round(sheet.cell_value(20, 0), 2)) + ' euros.' + \
                '</h6>' + \
                '<br>'

        body += '<h6>' + \
                'Deuxième résolution : affectation du résultat' + \
                '<br>' + \
                str(sheet.cell_value(23, 0)) + ' ' + str(round(sheet.cell_value(25, 0), 2)) \
                + ' euros, de la manière suivante : ' + \
                '<br>' + \
                '- 5 % à la réserve légale, soit ' + str(round(sheet.cell_value(29, 0), 2)) + ' euros ;' + \
                '<br>' + \
                '- le solde aux réserves ordinaires, soit ' + str(round(sheet.cell_value(33, 0), 2)) + ' euros.' \
                '</h6>' + \
                '<br>'

        body += '<h6>' + \
                str(sheet.cell_value(36, 0)) + \
                '</h6>' + \
                '<br>'

        body += '<h6>' + \
                "L'associé unique, " + \
                str(sheet.cell_value(39, 0)) + \
                '</h6>'

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

        excel_date_1 = round(float(str(workbook.sheet_by_name("Informations_Entreprise")
                                       .cell_value(9, 1)).split(".")[0]))

        python_date = xlrd.xldate_as_tuple(excel_date_1, 0)

        x = datetime.datetime(python_date[0], python_date[1], python_date[2])

        clos_le = x.strftime("%d/%m/%Y")

        options = {
            'page-size': 'A4',
            'orientation': 'Landscape',
            'header-right': 'Société HOLOMORPHE [SIREN : 883 632 556]',
            'header-left': 'Exercice clos le ' + clos_le,
            'footer-left': "Procès verbal d'approbation des comptes annuels de \n l'exercice " + str(round(float(str(workbook.sheet_by_name("Informations_Entreprise").cell_value(8, 1)).split(".")[0]))),
            'footer-right': '[page] sur [topage]'
        }

        path_wkthmltopdf = "C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe"

        config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)

        pdfkit.from_string(body,
                           "P_V_A_C_Annuels\\Holomorphe\\Annee_" + annee + "\\P_V_A_C_Annuels.pdf",
                           configuration=config,
                           options=options)

        filename = "P_V_A_C_Annuels\\Holomorphe\\Annee_" + annee + "\\P_V_A_C_Annuels.pdf"

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

        # P_V_A_C_Annuels
        proces_verbal_decisions_associe_unique_folder = "P_V_A_C_Annuels\\Holomorphe\\Annee_" + annee

        proces_verbal_decisions_associe_unique_folder_files = os.listdir(proces_verbal_decisions_associe_unique_folder)

        proces_verbal_decisions_associe_unique_filename = ""

        for f in proces_verbal_decisions_associe_unique_folder_files:
            if "signed" in f:
                proces_verbal_decisions_associe_unique_filename += f
                print("proces_verbal_decisions_associe_unique_filename : "
                      + proces_verbal_decisions_associe_unique_filename)
                break

        proces_verbal_decisions_associe_unique = proces_verbal_decisions_associe_unique_folder + "\\" \
                                                 + proces_verbal_decisions_associe_unique_filename

        shutil.copy(
            proces_verbal_decisions_associe_unique,
            "A:\\1_Professionnel\\1_Holomorphe\\1_Administration\\2_Gestion_Declarations_Administratives"
            "\\1_Recurrentes\\5_Infogreffe\\4_Approbation_Comptes_Sociaux\\"
            + exercice
            + "\\P_V_A_C_Annuels_Annee_" + annee + "_HOLOMORPHE.pdf"
        )

    # ok
    def test_declaration_confidentialite_des_comptes(self):
        print("test_declaration_confidentialite_des_comptes")

        workbook = xlrd.open_workbook(location)

        sheet = workbook.sheet_by_name("Declaration_Confidentialite_Comptes_Annuels_Micro_Entreprises")

        # Informations generales entreprise
        denomination_sociale = "S.A.S.U. à capital variable HOLOMORPHE"
        capital_social = "100 euros"
        adresse_siege_social = "31 Avenue de Ségur - ABC LIV Ségur - 75007 Paris"
        siret = "88363255600014"
        rcs = "R.C.S. PARIS - Greffe du Tribunal de Commerce de PARIS"
        activite = "Commerce de gros (commerce interentreprises) de produits chimiques"
        code_naf = "4675Z"
        numero_tva_intracommunataire = "FR06883632556"
        president = "Monsieur "
        date_immatriculation = "26 Mai 2020"

        # Rapport
        body = '<!doctype html>' + \
               '<html lang="en">' + \
               '<head>' + \
               '<meta charset="utf-8">' + \
               '<meta name="viewport" ' \
               'content="width=device-width, initial-scale=1, shrink-to-fit=no">' + \
               '<link rel="stylesheet" ' \
               'href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css" ' \
               'integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" ' \
               'crossorigin="anonymous">' + \
               '<title>Declaration_Confidentialite_Comptes_Annuels_Micro_Entreprises</title>' + \
               '</head>' + \
               '<body>' + \
               '<div class="container">' + \
               '<div class="card text-center">' + \
               '<div class="card-header text-center">Déclaration de confidentialité des comptes annuels</div>' + \
               '<div class="card-body">' + \
               '<h6>Dénomination sociale : ' + denomination_sociale + ' / Capital social : ' \
               + capital_social + '</h6>' + \
               '<h6>Adresse du siège social : ' + adresse_siege_social + ' / SIRET : ' \
               + siret + '</h6>' + \
               '<h6>Registre de Commerce et des Sociétés : ' + rcs + '</h6>' + \
               '<h6>Activité : ' + activite + ' / Code NAF : ' + code_naf + '</h6>' + \
               '<h6>N° TVA intracommunataire : ' + numero_tva_intracommunataire + ' / Président : ' \
               + president + " / Date d'immatriculation : " + date_immatriculation + '</h6>' + \
               '<br>'

        body += '<h6>' + \
                'Objet de la déclaration : ' + \
                '<br>' + \
                "L'associé unique déclare que les comptes annuels de l'exercice clos en date " + \
                str(sheet.cell_value(11, 0)) + \
                " et qui sont déposés en annexe au registre du commerce et des sociétés ne seront pas rendus publics " \
                "en application de l'article L232-25 du code de commerce et du premier alinéa de l'article " \
                "L524-6-6 du code rural et de la pêche maritime." + \
                '</h6>' + \
                '<br>'

        body += '<h6>' + \
                'Engagement du déclarant : ' + \
                '<br>' + \
                "Le soussigné atteste sur l'honneur que les renseignements contenus dans la présente déclaration " \
                "sont exacts et que la société susvisée répond à la définition des micro-entreprises au " \
                "sens de l'article L123-16-1 du code de commerce, n'est pas mentionnée à l'article " \
                "L123-16-2 et n'a pas pour activité la gestion des titres de participations et de valeurs " \
                "mobilières." + \
                '<br>' + \
                "Toute fausse déclaration de confidentialité des comptes annuels constitue un faux et un usage de " \
                "faux passible des peines d'amende et d'emprisonnement prévues aux articles 441-1 et suivants du " \
                "code pénal." + \
                '</h6>' + \
                '<br>'

        body += '<h6>' + \
                "L'associé unique, Monsieur " + \
                '</h6>'

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

        excel_date_1 = round(float(str(workbook.sheet_by_name("Informations_Entreprise").cell_value(9, 1))
                                   .split(".")[0]))

        python_date = xlrd.xldate_as_tuple(excel_date_1, 0)

        x = datetime.datetime(python_date[0], python_date[1], python_date[2])

        clos_le = x.strftime("%d/%m/%Y")

        options = {
            'page-size': 'A4',
            'orientation': 'Landscape',
            'header-right': 'Société HOLOMORPHE [SIREN : 883 632 556]',
            'header-left': 'Exercice clos le ' + clos_le,
            'footer-left': "Déclaration de confidentialité des comptes annuels de \n l'exercice "
                           + str(round(float(str(workbook.sheet_by_name("Informations_Entreprise").cell_value(8, 1)).split(".")[0]))),
            'footer-right': '[page] sur [topage]'
        }

        path_wkthmltopdf = "C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe"

        config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)

        pdfkit.from_string(body,
                           "D_C_C_A\\Holomorphe\\" + annee + "\\D_C_Comptes_Annuels.pdf",
                           configuration=config,
                           options=options)

        filename = "D_C_C_A\\Holomorphe\\" + annee + "\\D_C_Comptes_Annuels.pdf"

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

            # Insérer la valeur "Fait à Paris (75007), le dd/mm/YYYY.".
            can.drawString(
                x_coord,
                y_coord,
                "Fait à Paris (75007), le " + date_of_signature + "."
            )

            # Insérer la valeur "Lu et approuvé.".
            can.drawString(
                x_coord,
                y_coord - 8,
                "Lu et approuvé."
            )

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

        # d_c_c_a
        d_c_c_a_folder = "D_C_C_A\\Holomorphe\\" + annee

        d_c_c_a_folder_files = os.listdir(d_c_c_a_folder)

        d_c_c_a_filename = ""

        for f in d_c_c_a_folder_files:
            if "signed" in f:
                d_c_c_a_filename += f
                print("d_c_c_a_filename : "
                      + d_c_c_a_filename)
                break

        d_c_c_a = d_c_c_a_folder + "\\" + d_c_c_a_filename

        shutil.copy(
            d_c_c_a,
            "A:\\1_Professionnel\\1_Holomorphe\\1_Administration\\2_Gestion_Declarations_Administratives"
            "\\1_Recurrentes\\5_Infogreffe\\4_Approbation_Comptes_Sociaux\\"
            + exercice
            + "\\Declaration_Confidentialite_Comptes_Annuels_"
            + annee
            + "_HOLOMORPHE.pdf"
        )


if __name__ == '__main__':
    unittest.main()
