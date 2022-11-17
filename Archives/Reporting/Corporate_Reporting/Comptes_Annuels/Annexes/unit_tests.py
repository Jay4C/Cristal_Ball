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


class Annexe_Holomorphe(unittest.TestCase):
    def test_annexe_tableau_des_immobilisations_s_b(self):
        print("test_annexe_tableau_des_immobilisations_s_b")

        annee = "2020"
        
        location = ("A:\\1_Professionnel\\1_Holomorphe\\1_Administration\\1_Comptabilite_Fiscalite\\1_Annee_2020\\Consolidation_Comptable_Fiscale_2020.xls")

        workbook = xlrd.open_workbook(location)

        sheet = workbook.sheet_by_name("Annexe_T_D_I_S_B")

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
               '<title>Annexe_T_D_I_S_B</title>' + \
               '</head>' + \
               '<body>' + \
               '<div class="container">' + \
               '<div class="card text-center">' + \
               '<div class="card-header text-center">Annexe : Tableau des immobilisations en système de base</div>' + \
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
               '<h4>' + str(sheet.cell_value(0, 0)) + '</h4>' + \
               '<br>' + \
               '<table class="table table-bordered">' + \
               '<thead>' + \
               '<tr>' + \
               '<th scope="col">' + str(sheet.cell_value(1, 0)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(1, 1)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(1, 2)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(1, 3)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(1, 4)) + '</th>' + \
               '</tr>' + \
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
               '<td><i>' + str(sheet.cell_value(3, 0)) + '</i></td>' + \
               '<td>' + str(sheet.cell_value(3, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(3, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(3, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(3, 4)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i>' + str(sheet.cell_value(4, 0)) + '</i></td>' + \
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
               '<td><i><b>' + str(sheet.cell_value(6, 0)) + '</b></i></td>' + \
               '<td>' + str(sheet.cell_value(6, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(6, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(6, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(6, 4)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="5">' + str(sheet.cell_value(7, 0)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="5">' + str(sheet.cell_value(8, 0)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="5">' + str(sheet.cell_value(9, 0)) + '</td>' + \
               '</tr>' + \
               '</tbody>' + \
               '</table>' + \
               '<br>' + \
               '<br>' + \
               '<h4>' + str(sheet.cell_value(11, 0)) + '</h4>' + \
               '<br>' + \
               '<table class="table table-bordered">' + \
               '<thead>' + \
               '<tr>' + \
               '<th scope="col" colspan="5">' + str(sheet.cell_value(12, 0)) + '</th>' + \
               '</tr>' + \
               '<tr>' + \
               '<th scope="col" colspan="5">' + str(sheet.cell_value(13, 0)) + '</th>' + \
               '</tr>' + \
               '<tr>' + \
               '<th scope="col" colspan="5">' + str(sheet.cell_value(14, 0)) + '</th>' + \
               '</tr>' + \
               '<tr>' + \
               '<th scope="col" colspan="2">' + str(sheet.cell_value(15, 0)) + '</th>' + \
               '<th scope="col" colspan="3">' + str(sheet.cell_value(15, 2)) + '</th>' + \
               '</tr>' + \
               '<tr>' + \
               '<th scope="col">' + str(sheet.cell_value(16, 0)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(16, 1)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(16, 2)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(16, 3)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(16, 4)) + '</th>' + \
               '</tr>' + \
               '</thead>' + \
               '<tbody>' + \
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
               '<td>' + str(sheet.cell_value(20, 0)) + '</td>' + \
               '<td>' + str(sheet.cell_value(20, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(20, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(20, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(20, 4)) + '</td>' + \
               '</tr>' + \
               '</tbody>' + \
               '</table>' +\
                '<br>' + \
               '<table class="table table-bordered">' + \
               '<thead>' + \
               '<tr>' + \
               '<th scope="col" colspan="5">' + str(sheet.cell_value(21, 0)) + '</th>' + \
               '</tr>' + \
               '<tr>' + \
               '<th scope="col" colspan="5">' + str(sheet.cell_value(22, 0)) + '</th>' + \
               '</tr>' + \
               '<tr>' + \
               '<th scope="col" colspan="5">' + str(sheet.cell_value(23, 0)) + '</th>' + \
               '</tr>' + \
               '<tr>' + \
               '<th scope="col" colspan="2">' + str(sheet.cell_value(24, 0)) + '</th>' + \
               '<th scope="col" colspan="3">' + str(sheet.cell_value(24, 2)) + '</th>' + \
               '</tr>' + \
               '<tr>' + \
               '<th scope="col">' + str(sheet.cell_value(25, 0)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(25, 1)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(25, 2)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(25, 3)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(25, 4)) + '</th>' + \
               '</tr>' + \
               '</thead>' + \
               '<tbody>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(26, 0)) + '</td>' + \
               '<td>' + str(sheet.cell_value(26, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(26, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(26, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(26, 4)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(27, 0)) + '</td>' + \
               '<td>' + str(sheet.cell_value(27, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(27, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(27, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(27, 4)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(28, 0)) + '</td>' + \
               '<td>' + str(sheet.cell_value(28, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(28, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(28, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(28, 4)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(29, 0)) + '</td>' + \
               '<td>' + str(sheet.cell_value(29, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(29, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(29, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(29, 4)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(30, 0)) + '</td>' + \
               '<td>' + str(sheet.cell_value(30, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(30, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(30, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(30, 4)) + '</td>' + \
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

        excel_date_1 = round(float(str(workbook.sheet_by_name("Informations_Entreprise").cell_value(9, 1)).split(".")[0]))

        python_date = xlrd.xldate_as_tuple(excel_date_1, 0)

        x = datetime.datetime(python_date[0], python_date[1], python_date[2])

        clos_le = x.strftime("%d/%m/%Y")

        options = {
            'page-size': 'A4',
            'header-right': 'Société HOLOMORPHE [SIREN : 883 632 556]',
            'header-left': 'Exercice clos le ' + clos_le,
            'footer-left': "Annexe : Tableau des immobilisations \n en système de base de l'exercice " + str(round(float(str(workbook.sheet_by_name("Informations_Entreprise").cell_value(8, 1)).split(".")[0]))),
            'footer-right': '[page] sur [topage]'
        }

        path_wkthmltopdf = "C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe"
        
        config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
        
        pdfkit.from_string(body, "Holomorphe\\Annee_" + annee + "\\Annexe_T_D_I_S_B\\Annexe_T_D_I_S_B.pdf", configuration=config, options=options)

        filename = "Holomorphe\\Annee_" + annee + "\\Annexe_T_D_I_S_B\\Annexe_T_D_I_S_B.pdf"

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

    def test_annexe_tableau_des_amortissements_s_b(self):
        print("test_annexe_tableau_des_amortissements_s_b")
        
        annee = "2020"
        
        location = ("A:\\1_Professionnel\\1_Holomorphe\\1_Administration\\1_Comptabilite_Fiscalite\\1_Annee_2020\\Consolidation_Comptable_Fiscale_2020.xls")

        workbook = xlrd.open_workbook(location)

        sheet = workbook.sheet_by_name("Annexe_T_D_A_S_B")

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
               '<title>Annexe_T_D_A_S_B</title>' + \
               '</head>' + \
               '<body>' + \
               '<div class="container">' + \
               '<div class="card text-center">' + \
               '<div class="card-header text-center">Annexe : Tableau des amortissements en système de base</div>' + \
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
               '<h4>' + str(sheet.cell_value(0, 0)) + '</h4>' + \
               '<br>' + \
               '<table class="table table-bordered">' + \
               '<thead>' + \
               '<tr>' + \
               '<th scope="col">' + str(sheet.cell_value(1, 0)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(1, 1)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(1, 2)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(1, 3)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(1, 4)) + '</th>' + \
               '</tr>' + \
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
               '<td><i>' + str(sheet.cell_value(3, 0)) + '</i></td>' + \
               '<td>' + str(sheet.cell_value(3, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(3, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(3, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(3, 4)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i>' + str(sheet.cell_value(4, 0)) + '</i></td>' + \
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
               '<td><i><b>' + str(sheet.cell_value(6, 0)) + '</b></i></td>' + \
               '<td>' + str(sheet.cell_value(6, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(6, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(6, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(6, 4)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="5">' + str(sheet.cell_value(7, 0)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="5">' + str(sheet.cell_value(8, 0)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="5">' + str(sheet.cell_value(9, 0)) + '</td>' + \
               '</tr>' + \
               '</tbody>' + \
               '</table>' + \
               '<br>' + \
               '<h4>' + str(sheet.cell_value(11, 0)) + '</h4>' + \
               '<br>' + \
               '<table class="table table-bordered">' + \
               '<thead>' + \
               '<tr>' + \
               '<th scope="col" colspan="5">' + str(sheet.cell_value(12, 0)) + '</th>' + \
               '</tr>' + \
               '<tr>' + \
               '<th scope="col" colspan="5">' + str(sheet.cell_value(13, 0)) + '</th>' + \
               '</tr>' + \
               '<tr>' + \
               '<th scope="col" colspan="5">' + str(sheet.cell_value(14, 0)) + '</th>' + \
               '</tr>' + \
               '<tr>' + \
               '<th scope="col">' + str(sheet.cell_value(15, 0)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(15, 1)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(15, 2)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(15, 3)) + '</th>' + \
               '</tr>' + \
               '</thead>' + \
               '<tbody>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(16, 0)) + '</td>' + \
               '<td>' + str(sheet.cell_value(16, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(16, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(16, 3)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(17, 0)) + '</td>' + \
               '<td>' + str(sheet.cell_value(17, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(17, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(17, 3)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(18, 0)) + '</td>' + \
               '<td>' + str(sheet.cell_value(18, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(18, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(18, 3)) + '</td>' + \
               '</tr>' + \
               '</tbody>' + \
               '</table>' + \
               '<br>' + \
               '<table class="table table-bordered">' + \
               '<thead>' + \
               '<tr>' + \
               '<th scope="col" colspan="4">' + str(sheet.cell_value(19, 0)) + '</th>' + \
               '</tr>' + \
               '<tr>' + \
               '<th scope="col" colspan="4">' + str(sheet.cell_value(20, 0)) + '</th>' + \
               '</tr>' + \
               '<tr>' + \
               '<th scope="col">' + str(sheet.cell_value(21, 0)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(21, 1)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(21, 2)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(21, 3)) + '</th>' + \
               '</tr>' + \
               '</thead>' + \
               '<tbody>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(22, 0)) + '</td>' + \
               '<td>' + str(sheet.cell_value(22, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(22, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(22, 3)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(23, 0)) + '</td>' + \
               '<td>' + str(sheet.cell_value(23, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(23, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(23, 3)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(24, 0)) + '</td>' + \
               '<td>' + str(sheet.cell_value(24, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(24, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(24, 3)) + '</td>' + \
               '</tr>' + \
               '</tbody>' + \
               '</table>' + \
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
            'footer-left': "Annexe : Tableau des amortissements en \n système de base de l'exercice " + str(round(float(str(workbook.sheet_by_name("Informations_Entreprise").cell_value(8, 1)).split(".")[0]))),
            'footer-right': '[page] sur [topage]'
        }

        path_wkthmltopdf = "C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe"
        
        config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
        
        pdfkit.from_string(body, "Holomorphe\\Annee_" + annee + "\\Annexe_T_D_A_S_B\\Annexe_T_D_A_S_B.pdf", configuration=config, options=options)

        filename = "Holomorphe\\Annee_" + annee + "\\Annexe_T_D_A_S_B\\Annexe_T_D_A_S_B.pdf"

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

    def test_annexe_tableau_des_depreciations_s_b(self):
        print("test_annexe_tableau_des_depreciations_s_b")
        
        annee = "2020"
        
        location = ("A:\\1_Professionnel\\1_Holomorphe\\1_Administration\\1_Comptabilite_Fiscalite\\1_Annee_2020\\Consolidation_Comptable_Fiscale_2020.xls")

        workbook = xlrd.open_workbook(location)

        sheet = workbook.sheet_by_name("Annexe_T_D_D_S_B")

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
               '<title>Annexe_T_D_D_S_B</title>' + \
               '</head>' + \
               '<body>' + \
               '<div class="container">' + \
               '<div class="card text-center">' + \
               '<div class="card-header text-center">Annexe : Tableau des dépréciations en système de base</div>' + \
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
               '<th scope="col" colspan="5">' + str(sheet.cell_value(0, 0)) + '</th>' + \
               '</tr>' + \
               '<tr>' + \
               '<th scope="col">' + str(sheet.cell_value(1, 0)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(1, 1)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(1, 2)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(1, 3)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(1, 4)) + '</th>' + \
               '</tr>' + \
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
               '<td><i>' + str(sheet.cell_value(3, 0)) + '</i></td>' + \
               '<td>' + str(sheet.cell_value(3, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(3, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(3, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(3, 4)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i>' + str(sheet.cell_value(4, 0)) + '</i></td>' + \
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
               '<td><i>' + str(sheet.cell_value(6, 0)) + '</i></td>' + \
               '<td>' + str(sheet.cell_value(6, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(6, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(6, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(6, 4)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i>' + str(sheet.cell_value(7, 0)) + '</i></td>' + \
               '<td>' + str(sheet.cell_value(7, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(7, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(7, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(7, 4)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i><b>' + str(sheet.cell_value(8, 0)) + '</b></i></td>' + \
               '<td>' + str(sheet.cell_value(8, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(8, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(8, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(8, 4)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="5">' + str(sheet.cell_value(9, 0)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="5">' + str(sheet.cell_value(10, 0)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="5">' + str(sheet.cell_value(11, 0)) + '</td>' + \
               '</tr>' + \
               '</tbody>' + \
               '</table>' + \
               '</div>' + \
               '</div>' + \
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
            'footer-left': "Annexe : Tableau des dépréciations en système \n de base de l'exercice " + str(round(float(str(workbook.sheet_by_name("Informations_Entreprise").cell_value(8, 1)).split(".")[0]))),
            'footer-right': '[page] sur [topage]'
        }

        path_wkthmltopdf = "C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe"
        config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
        pdfkit.from_string(body, "Holomorphe\\Annee_" + annee + "\\Annexe_T_D_D_S_B\\Annexe_T_D_D_S_B.pdf", configuration=config, options=options)

        filename = "Holomorphe\\Annee_" + annee + "\\Annexe_T_D_D_S_B\\Annexe_T_D_D_S_B.pdf"

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

    def test_annexe_tableau_des_provisions_s_b(self):
        print("test_annexe_tableau_des_provisions_s_b")
        
        annee = "2020"
        
        location = ("A:\\1_Professionnel\\1_Holomorphe\\1_Administration\\1_Comptabilite_Fiscalite\\1_Annee_2020\\Consolidation_Comptable_Fiscale_2020.xls")

        workbook = xlrd.open_workbook(location)

        sheet = workbook.sheet_by_name("Annexe_T_D_P_S_B")

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
               '<title>Annexe_T_D_P_S_B</title>' + \
               '</head>' + \
               '<body>' + \
               '<div class="container">' + \
               '<div class="card text-center">' + \
               '<div class="card-header text-center">Annexe : Tableau des provisions en système de base</div>' + \
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
               '<th scope="col" colspan="5">' + str(sheet.cell_value(1, 0)) + '</th>' + \
               '</tr>' + \
               '<tr>' + \
               '<th scope="col">' + str(sheet.cell_value(2, 0)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(2, 1)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(2, 2)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(2, 3)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(2, 4)) + '</th>' + \
               '</tr>' + \
               '<tr>' + \
               '<th scope="col">' + str(sheet.cell_value(3, 0)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(3, 1)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(3, 2)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(3, 3)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(3, 4)) + '</th>' + \
               '</tr>' + \
               '</thead>' + \
               '<tbody>' + \
               '<tr>' + \
               '<td><i>' + str(sheet.cell_value(4, 0)) + '</i></td>' + \
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
               '<td><i>' + str(sheet.cell_value(6, 0)) + '</i></td>' + \
               '<td>' + str(sheet.cell_value(6, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(6, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(6, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(6, 4)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i><b>' + str(sheet.cell_value(7, 0)) + '</b></i></td>' + \
               '<td>' + str(sheet.cell_value(7, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(7, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(7, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(7, 4)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="5">' + str(sheet.cell_value(8, 0)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="5">' + str(sheet.cell_value(9, 0)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="5">' + str(sheet.cell_value(10, 0)) + '</td>' + \
               '</tr>' + \
               '</tbody>' + \
               '</table>' + \
               '<br>' + \
               '<h4>' + str(sheet.cell_value(12, 0)) + '</h4>' + \
               '<br>' + \
               '<table class="table table-bordered">' + \
               '<thead>' + \
               '<tr>' + \
               '<th scope="col" colspan="4">' + str(sheet.cell_value(13, 0)) + '</th>' + \
               '</tr>' + \
               '<tr>' + \
               '<th scope="col" colspan="4">' + str(sheet.cell_value(14, 0)) + '</th>' + \
               '</tr>' + \
               '<tr>' + \
               '<th scope="col">' + str(sheet.cell_value(15, 0)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(15, 1)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(15, 2)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(15, 3)) + '</th>' + \
               '</tr>' + \
               '</thead>' + \
               '<tbody>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(16, 0)) + '</td>' + \
               '<td>' + str(sheet.cell_value(16, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(16, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(16, 3)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(17, 0)) + '</td>' + \
               '<td>' + str(sheet.cell_value(17, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(17, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(17, 3)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '</tbody>' + \
               '</table>' + \
              '<br>' + \
               '<table class="table table-bordered">' + \
               '<thead>' + \
               '<tr>' + \
               '<th scope="col" colspan="4">' + str(sheet.cell_value(18, 0)) + '</th>' + \
               '</tr>' + \
               '<tr>' + \
               '<th scope="col" colspan="4">' + str(sheet.cell_value(19, 0)) + '</th>' + \
               '</tr>' + \
               '<tr>' + \
               '<th scope="col">' + str(sheet.cell_value(20, 0)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(20, 1)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(20, 2)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(20, 3)) + '</th>' + \
               '</tr>' + \
               '</thead>' + \
               '<tbody>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(21, 0)) + '</td>' + \
               '<td>' + str(sheet.cell_value(21, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(21, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(21, 3)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(22, 0)) + '</td>' + \
               '<td>' + str(sheet.cell_value(22, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(22, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(22, 3)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
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
            'footer-left': "Annexe : Tableau des provisions en système \n de base de l'exercice " + str(round(float(str(workbook.sheet_by_name("Informations_Entreprise").cell_value(8, 1)).split(".")[0]))),
            'footer-right': '[page] sur [topage]'
        }

        path_wkthmltopdf = "C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe"
        
        config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
        
        pdfkit.from_string(body, "Holomorphe\\Annee_" + annee + "\\Annexe_T_D_P_S_B\\Annexe_T_D_P_S_B.pdf", configuration=config, options=options)

        filename = "Holomorphe\\Annee_" + annee + "\\Annexe_T_D_P_S_B\\Annexe_T_D_P_S_B.pdf"

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

    def test_annexe_etat_des_creances_et_des_dettes_a_la_cloture_de_l_exercice_s_b(self):
        print("test_annexe_etat_des_creances_et_des_dettes_a_la_cloture_de_l_exercice_s_b")
        
        annee = "2020"
        
        location = ("A:\\1_Professionnel\\1_Holomorphe\\1_Administration\\1_Comptabilite_Fiscalite\\1_Annee_2020\\Consolidation_Comptable_Fiscale_2020.xls")

        workbook = xlrd.open_workbook(location)

        sheet = workbook.sheet_by_name("Annexe__E_C_D_C_D_L_E_S_B")

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
           '<title>Annexe__E_C_D_C_D_L_E_S_B</title>' + \
           '</head>' + \
           '<body>' + \
           '<div class="container">' + \
           '<div class="card text-center">' + \
           '<div class="card-header text-center">Annexe : Etat des échéances des créances et des dettes à la clôture de l' + "'" + 'exercice</div>' + \
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
           '<th scope="col" colspan="9">' + str(sheet.cell_value(0, 0)) + '</th>' + \
           '</tr>' + \
           '<tr>' + \
           '<th scope="col">' + str(sheet.cell_value(1, 0)) + '</th>' + \
           '<th scope="col">' + str(sheet.cell_value(1, 1)) + '</th>' + \
           '<th scope="col">' + str(sheet.cell_value(1, 2)) + '</th>' + \
           '<th scope="col">' + str(sheet.cell_value(1, 3)) + '</th>' + \
           '<th scope="col">' + str(sheet.cell_value(1, 4)) + '</th>' + \
           '<th scope="col">' + str(sheet.cell_value(1, 5)) + '</th>' + \
           '<th scope="col">' + str(sheet.cell_value(1, 6)) + '</th>' + \
           '<th scope="col">' + str(sheet.cell_value(1, 7)) + '</th>' + \
           '<th scope="col">' + str(sheet.cell_value(1, 8)) + '</th>' + \
           '</tr>' + \
           '</thead>' + \
           '<tbody>' + \
           '<tr>' + \
           '<td><b>' + str(sheet.cell_value(2, 0)) + '</b></td>' + \
           '<td>' + str(sheet.cell_value(2, 1)) + '</td>' + \
           '<td>' + str(sheet.cell_value(2, 2)) + '</td>' + \
           '<td>' + str(sheet.cell_value(2, 3)) + '</td>' + \
           '<td><b>' + str(sheet.cell_value(2, 4)) + '</b></td>' + \
           '<td>' + str(sheet.cell_value(2, 5)) + '</td>' + \
           '<td>' + str(sheet.cell_value(2, 6)) + '</td>' + \
           '<td>' + str(sheet.cell_value(2, 7)) + '</td>' + \
           '<td>' + str(sheet.cell_value(2, 8)) + '</td>' + \
           '</tr>' + \
        '<tr>' + \
        '<td><i>' + str(sheet.cell_value(3, 0)) + '</i></td>' + \
        '<td>' + str(sheet.cell_value(3, 1)) + '</td>' + \
        '<td>' + str(sheet.cell_value(3, 2)) + '</td>' + \
        '<td>' + str(sheet.cell_value(3, 3)) + '</td>' + \
        '<td><b>' + str(sheet.cell_value(3, 4)) + '</b></td>' + \
        '<td>' + str(sheet.cell_value(3, 5)) + '</td>' + \
        '<td>' + str(sheet.cell_value(3, 6)) + '</td>' + \
        '<td>' + str(sheet.cell_value(3, 7)) + '</td>' + \
        '<td>' + str(sheet.cell_value(3, 8)) + '</td>' + \
        '</tr>' + \
        '<tr>' + \
        '<td><i>' + str(sheet.cell_value(4, 0)) + '</i></td>' + \
        '<td>' + str(sheet.cell_value(4, 1)) + '</td>' + \
        '<td>' + str(sheet.cell_value(4, 2)) + '</td>' + \
        '<td>' + str(sheet.cell_value(4, 3)) + '</td>' + \
        '<td><b>' + str(sheet.cell_value(4, 4)) + '</b></td>' + \
        '<td>' + str(sheet.cell_value(4, 5)) + '</td>' + \
        '<td>' + str(sheet.cell_value(4, 6)) + '</td>' + \
        '<td>' + str(sheet.cell_value(4, 7)) + '</td>' + \
        '<td>' + str(sheet.cell_value(4, 8)) + '</td>' + \
        '</tr>' + \
        '<tr>' + \
        '<td><i>' + str(sheet.cell_value(5, 0)) + '</i></td>' + \
        '<td>' + str(sheet.cell_value(5, 1)) + '</td>' + \
        '<td>' + str(sheet.cell_value(5, 2)) + '</td>' + \
        '<td>' + str(sheet.cell_value(5, 3)) + '</td>' + \
        '<td><i>' + str(sheet.cell_value(5, 4)) + '</i></td>' + \
        '<td>' + str(sheet.cell_value(5, 5)) + '</td>' + \
        '<td>' + str(sheet.cell_value(5, 6)) + '</td>' + \
        '<td>' + str(sheet.cell_value(5, 7)) + '</td>' + \
        '<td>' + str(sheet.cell_value(5, 8)) + '</td>' + \
        '</tr>' + \
        '<tr>' + \
        '<td><b>' + str(sheet.cell_value(6, 0)) + '</b></td>' + \
        '<td>' + str(sheet.cell_value(6, 1)) + '</td>' + \
        '<td>' + str(sheet.cell_value(6, 2)) + '</td>' + \
        '<td>' + str(sheet.cell_value(6, 3)) + '</td>' + \
        '<td><i>' + str(sheet.cell_value(6, 4)) + '</i></td>' + \
        '<td>' + str(sheet.cell_value(6, 5)) + '</td>' + \
        '<td>' + str(sheet.cell_value(6, 6)) + '</td>' + \
        '<td>' + str(sheet.cell_value(6, 7)) + '</td>' + \
        '<td>' + str(sheet.cell_value(6, 8)) + '</td>' + \
        '</tr>' + \
        '<tr>' + \
        '<td><i>' + str(sheet.cell_value(7, 0)) + '</i></td>' + \
        '<td>' + str(sheet.cell_value(7, 1)) + '</td>' + \
        '<td>' + str(sheet.cell_value(7, 2)) + '</td>' + \
        '<td>' + str(sheet.cell_value(7, 3)) + '</td>' + \
        '<td><b>' + str(sheet.cell_value(7, 4)) + '</b></td>' + \
        '<td>' + str(sheet.cell_value(7, 5)) + '</td>' + \
        '<td>' + str(sheet.cell_value(7, 6)) + '</td>' + \
        '<td>' + str(sheet.cell_value(7, 7)) + '</td>' + \
        '<td>' + str(sheet.cell_value(7, 8)) + '</td>' + \
        '</tr>' + \
        '<tr>' + \
        '<td><i>' + str(sheet.cell_value(8, 0)) + '</i></td>' + \
        '<td>' + str(sheet.cell_value(8, 1)) + '</td>' + \
        '<td>' + str(sheet.cell_value(8, 2)) + '</td>' + \
        '<td>' + str(sheet.cell_value(8, 3)) + '</td>' + \
        '<td><b>' + str(sheet.cell_value(8, 4)) + '</b></td>' + \
        '<td>' + str(sheet.cell_value(8, 5)) + '</td>' + \
        '<td>' + str(sheet.cell_value(8, 6)) + '</td>' + \
        '<td>' + str(sheet.cell_value(8, 7)) + '</td>' + \
        '<td>' + str(sheet.cell_value(8, 8)) + '</td>' + \
        '</tr>' + \
        '<tr>' + \
        '<td><i>' + str(sheet.cell_value(9, 0)) + '</i></td>' + \
        '<td>' + str(sheet.cell_value(9, 1)) + '</td>' + \
        '<td>' + str(sheet.cell_value(9, 2)) + '</td>' + \
        '<td>' + str(sheet.cell_value(9, 3)) + '</td>' + \
        '<td><b>' + str(sheet.cell_value(9, 4)) + '</b></td>' + \
        '<td>' + str(sheet.cell_value(9, 5)) + '</td>' + \
        '<td>' + str(sheet.cell_value(9, 6)) + '</td>' + \
        '<td>' + str(sheet.cell_value(9, 7)) + '</td>' + \
        '<td>' + str(sheet.cell_value(9, 8)) + '</td>' + \
        '</tr>' + \
        '<tr>' + \
        '<td><i>' + str(sheet.cell_value(10, 0)) + '</i></td>' + \
        '<td>' + str(sheet.cell_value(10, 1)) + '</td>' + \
        '<td>' + str(sheet.cell_value(10, 2)) + '</td>' + \
        '<td>' + str(sheet.cell_value(10, 3)) + '</td>' + \
        '<td><b>' + str(sheet.cell_value(10, 4)) + '</b></td>' + \
        '<td>' + str(sheet.cell_value(10, 5)) + '</td>' + \
        '<td>' + str(sheet.cell_value(10, 6)) + '</td>' + \
        '<td>' + str(sheet.cell_value(10, 7)) + '</td>' + \
        '<td>' + str(sheet.cell_value(10, 8)) + '</td>' + \
        '</tr>' + \
        '<tr>' + \
        '<td>' + str(sheet.cell_value(11, 0)) + '</td>' + \
        '<td>' + str(sheet.cell_value(11, 1)) + '</td>' + \
        '<td>' + str(sheet.cell_value(11, 2)) + '</td>' + \
        '<td>' + str(sheet.cell_value(11, 3)) + '</td>' + \
        '<td><b>' + str(sheet.cell_value(11, 4)) + '</b></td>' + \
        '<td>' + str(sheet.cell_value(11, 5)) + '</td>' + \
        '<td>' + str(sheet.cell_value(11, 6)) + '</td>' + \
        '<td>' + str(sheet.cell_value(11, 7)) + '</td>' + \
        '<td>' + str(sheet.cell_value(11, 8)) + '</td>' + \
        '</tr>' + \
        '<tr>' + \
        '<td>' + str(sheet.cell_value(12, 0)) + '</td>' + \
        '<td>' + str(sheet.cell_value(12, 1)) + '</td>' + \
        '<td>' + str(sheet.cell_value(12, 2)) + '</td>' + \
        '<td>' + str(sheet.cell_value(12, 3)) + '</td>' + \
        '<td><b>' + str(sheet.cell_value(12, 4)) + '</b></td>' + \
        '<td>' + str(sheet.cell_value(12, 5)) + '</td>' + \
        '<td>' + str(sheet.cell_value(12, 6)) + '</td>' + \
        '<td>' + str(sheet.cell_value(12, 7)) + '</td>' + \
        '<td>' + str(sheet.cell_value(12, 8)) + '</td>' + \
        '</tr>' + \
        '<tr>' + \
        '<td><b><i>' + str(sheet.cell_value(13, 0)) + '</i></b></td>' + \
        '<td>' + str(sheet.cell_value(13, 1)) + '</td>' + \
        '<td>' + str(sheet.cell_value(13, 2)) + '</td>' + \
        '<td>' + str(sheet.cell_value(13, 3)) + '</td>' + \
        '<td><b><i>' + str(sheet.cell_value(13, 4)) + '</i></b></td>' + \
        '<td>' + str(sheet.cell_value(13, 5)) + '</td>' + \
        '<td>' + str(sheet.cell_value(13, 6)) + '</td>' + \
        '<td>' + str(sheet.cell_value(13, 7)) + '</td>' + \
        '<td>' + str(sheet.cell_value(13, 8)) + '</td>' + \
        '</tr>' + \
        '<tr>' + \
        '<td colspan="4">' + str(sheet.cell_value(14, 0)) + '</td>' + \
        '<td colspan="5">' + str(sheet.cell_value(14, 4)) + '</td>' + \
        '</tr>' + \
        '<tr>' + \
        '<td colspan="4">' + str(sheet.cell_value(15, 0)) + '</td>' + \
        '<td colspan="5">' + str(sheet.cell_value(15, 4)) + '</td>' + \
        '</tr>' + \
        '<tr>' + \
        '<td colspan="4"></td>' + \
        '<td colspan="5">' + str(sheet.cell_value(16, 4)) + '</td>' + \
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
           'footer-left': "Annexe : Etat des échéances des créances \n et des dettes à la clôture de l'exercice " + str(round(float(str(workbook.sheet_by_name("Informations_Entreprise").cell_value(8, 1)).split(".")[0]))),
           'footer-right': '[page] sur [topage]'
        }

        path_wkthmltopdf = "C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe"
        
        config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
        
        pdfkit.from_string(body, "Holomorphe\\Annee_" + annee + "\\Annexe__E_C_D_C_D_L_E_S_B\\Annexe__E_C_D_C_D_L_E_S_B.pdf", configuration=config, options=options)

        filename = "Holomorphe\\Annee_" + annee + "\\Annexe__E_C_D_C_D_L_E_S_B\\Annexe__E_C_D_C_D_L_E_S_B.pdf"

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

    def test_annexe_tableau_des_filiales_et_participations_s_b(self):
        print("test_annexe_tableau_des_filiales_et_participations_s_b")
        
        annee = "2020"
        
        location = ("A:\\1_Professionnel\\1_Holomorphe\\1_Administration\\1_Comptabilite_Fiscalite\\1_Annee_2020\\Consolidation_Comptable_Fiscale_2020.xls")

        workbook = xlrd.open_workbook(location)

        sheet = workbook.sheet_by_name("Annexe_T_D_F_E_P_S_B")

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
               '<title>Annexe_T_D_F_E_P_S_B</title>' + \
               '</head>' + \
               '<body>' + \
               '<div class="container">' + \
               '<div class="card text-center">' + \
               '<div class="card-header text-center">Annexe : Tableau des filiales et participations en système en base</div>' + \
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
               '<th scope="col" colspan="12">' + str(sheet.cell_value(0, 0)) + '</th>' + \
               '</tr>' + \
               '<tr>' + \
               '<th scope="col" colspan="12">' + str(sheet.cell_value(1, 0)) + '</th>' + \
               '</tr>' + \
               '<tr>' + \
               '<th scope="col">' + str(sheet.cell_value(2, 0)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(2, 1)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(2, 2)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(2, 3)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(2, 4)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(2, 5)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(2, 6)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(2, 7)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(2, 8)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(2, 9)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(2, 10)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(2, 11)) + '</th>' + \
               '</tr>' + \
               '</thead>' + \
               '<tbody>' + \
               '<tr>' + \
               '<td><b>' + str(sheet.cell_value(3, 0)) + '</b></td>' + \
               '<td>' + str(sheet.cell_value(3, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(3, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(3, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(3, 4)) + '</td>' + \
               '<td>' + str(sheet.cell_value(3, 5)) + '</td>' + \
               '<td>' + str(sheet.cell_value(3, 6)) + '</td>' + \
               '<td>' + str(sheet.cell_value(3, 7)) + '</td>' + \
               '<td>' + str(sheet.cell_value(3, 8)) + '</td>' + \
               '<td>' + str(sheet.cell_value(3, 9)) + '</td>' + \
               '<td>' + str(sheet.cell_value(3, 10)) + '</td>' + \
               '<td>' + str(sheet.cell_value(3, 11)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i>' + str(sheet.cell_value(4, 0)) + '</i></td>' + \
               '<td>' + str(sheet.cell_value(4, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(4, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(4, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(4, 4)) + '</td>' + \
               '<td>' + str(sheet.cell_value(4, 5)) + '</td>' + \
               '<td>' + str(sheet.cell_value(4, 6)) + '</td>' + \
               '<td>' + str(sheet.cell_value(4, 7)) + '</td>' + \
               '<td>' + str(sheet.cell_value(4, 8)) + '</td>' + \
               '<td>' + str(sheet.cell_value(4, 9)) + '</td>' + \
               '<td>' + str(sheet.cell_value(4, 10)) + '</td>' + \
               '<td>' + str(sheet.cell_value(4, 11)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i>' + str(sheet.cell_value(5, 0)) + '</i></td>' + \
               '<td>' + str(sheet.cell_value(5, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(5, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(5, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(5, 4)) + '</td>' + \
               '<td>' + str(sheet.cell_value(5, 5)) + '</td>' + \
               '<td>' + str(sheet.cell_value(5, 6)) + '</td>' + \
               '<td>' + str(sheet.cell_value(5, 7)) + '</td>' + \
               '<td>' + str(sheet.cell_value(5, 8)) + '</td>' + \
               '<td>' + str(sheet.cell_value(5, 9)) + '</td>' + \
               '<td>' + str(sheet.cell_value(5, 10)) + '</td>' + \
               '<td>' + str(sheet.cell_value(5, 11)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><b>' + str(sheet.cell_value(6, 0)) + '</b></td>' + \
               '<td>' + str(sheet.cell_value(6, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(6, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(6, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(6, 4)) + '</td>' + \
               '<td>' + str(sheet.cell_value(6, 5)) + '</td>' + \
               '<td>' + str(sheet.cell_value(6, 6)) + '</td>' + \
               '<td>' + str(sheet.cell_value(6, 7)) + '</td>' + \
               '<td>' + str(sheet.cell_value(6, 8)) + '</td>' + \
               '<td>' + str(sheet.cell_value(6, 9)) + '</td>' + \
               '<td>' + str(sheet.cell_value(6, 10)) + '</td>' + \
               '<td>' + str(sheet.cell_value(6, 11)) + '</td>' + \
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
               '<td>' + str(sheet.cell_value(7, 8)) + '</td>' + \
               '<td>' + str(sheet.cell_value(7, 9)) + '</td>' + \
               '<td>' + str(sheet.cell_value(7, 10)) + '</td>' + \
               '<td>' + str(sheet.cell_value(7, 11)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><u>' + str(sheet.cell_value(8, 0)) + '</u></td>' + \
               '<td>' + str(sheet.cell_value(8, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(8, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(8, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(8, 4)) + '</td>' + \
               '<td>' + str(sheet.cell_value(8, 5)) + '</td>' + \
               '<td>' + str(sheet.cell_value(8, 6)) + '</td>' + \
               '<td>' + str(sheet.cell_value(8, 7)) + '</td>' + \
               '<td>' + str(sheet.cell_value(8, 8)) + '</td>' + \
               '<td>' + str(sheet.cell_value(8, 9)) + '</td>' + \
               '<td>' + str(sheet.cell_value(8, 10)) + '</td>' + \
               '<td>' + str(sheet.cell_value(8, 11)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><u>' + str(sheet.cell_value(9, 0)) + '</u></td>' + \
               '<td>' + str(sheet.cell_value(9, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(9, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(9, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(9, 4)) + '</td>' + \
               '<td>' + str(sheet.cell_value(9, 5)) + '</td>' + \
               '<td>' + str(sheet.cell_value(9, 6)) + '</td>' + \
               '<td>' + str(sheet.cell_value(9, 7)) + '</td>' + \
               '<td>' + str(sheet.cell_value(9, 8)) + '</td>' + \
               '<td>' + str(sheet.cell_value(9, 9)) + '</td>' + \
               '<td>' + str(sheet.cell_value(9, 10)) + '</td>' + \
               '<td>' + str(sheet.cell_value(9, 11)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i>' + str(sheet.cell_value(10, 0)) + '</i></td>' + \
               '<td>' + str(sheet.cell_value(10, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(10, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(10, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(10, 4)) + '</td>' + \
               '<td>' + str(sheet.cell_value(10, 5)) + '</td>' + \
               '<td>' + str(sheet.cell_value(10, 6)) + '</td>' + \
               '<td>' + str(sheet.cell_value(10, 7)) + '</td>' + \
               '<td>' + str(sheet.cell_value(10, 8)) + '</td>' + \
               '<td>' + str(sheet.cell_value(10, 9)) + '</td>' + \
               '<td>' + str(sheet.cell_value(10, 10)) + '</td>' + \
               '<td>' + str(sheet.cell_value(10, 11)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><u>' + str(sheet.cell_value(11, 0)) + '</u></td>' + \
               '<td>' + str(sheet.cell_value(11, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(11, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(11, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(11, 4)) + '</td>' + \
               '<td>' + str(sheet.cell_value(11, 5)) + '</td>' + \
               '<td>' + str(sheet.cell_value(11, 6)) + '</td>' + \
               '<td>' + str(sheet.cell_value(11, 7)) + '</td>' + \
               '<td>' + str(sheet.cell_value(11, 8)) + '</td>' + \
               '<td>' + str(sheet.cell_value(11, 9)) + '</td>' + \
               '<td>' + str(sheet.cell_value(11, 10)) + '</td>' + \
               '<td>' + str(sheet.cell_value(11, 11)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><u>' + str(sheet.cell_value(12, 0)) + '</u></td>' + \
               '<td>' + str(sheet.cell_value(12, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(12, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(12, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(12, 4)) + '</td>' + \
               '<td>' + str(sheet.cell_value(12, 5)) + '</td>' + \
               '<td>' + str(sheet.cell_value(12, 6)) + '</td>' + \
               '<td>' + str(sheet.cell_value(12, 7)) + '</td>' + \
               '<td>' + str(sheet.cell_value(12, 8)) + '</td>' + \
               '<td>' + str(sheet.cell_value(12, 9)) + '</td>' + \
               '<td>' + str(sheet.cell_value(12, 10)) + '</td>' + \
               '<td>' + str(sheet.cell_value(12, 11)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="12">' + str(sheet.cell_value(13, 0)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="12">' + str(sheet.cell_value(14, 0)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="12">' + str(sheet.cell_value(15, 0)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="12">' + str(sheet.cell_value(16, 0)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="12">' + str(sheet.cell_value(17, 0)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="12">' + str(sheet.cell_value(18, 0)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="12">' + str(sheet.cell_value(19, 0)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="12">' + str(sheet.cell_value(20, 0)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="12">' + str(sheet.cell_value(21, 0)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="12">' + str(sheet.cell_value(22, 0)) + '</td>' + \
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
               'footer-left': "Annexe : Tableau des filiales et participations \n en système en base de l'exercice " + str(round(float(str(workbook.sheet_by_name("Informations_Entreprise").cell_value(8, 1)).split(".")[0]))),
               'footer-right': '[page] sur [topage]'
        }

        path_wkthmltopdf = "C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe"
        
        config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
        
        pdfkit.from_string(body, "Holomorphe\\Annee_" + annee + "\\Annexe_T_D_F_E_P_S_B\\Annexe_T_D_F_E_P_S_B.pdf", configuration=config, options=options)

        filename = "Holomorphe\\Annee_" + annee + "\\Annexe_T_D_F_E_P_S_B\\Annexe_T_D_F_E_P_S_B.pdf"

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

    def test_annexe_tableau_du_portefeuille_de_tiap_s_b(self):
        print("test_annexe_tableau_du_portefeuille_de_tiap_s_b")
        
        annee = "2020"
        
        location = ("A:\\1_Professionnel\\1_Holomorphe\\1_Administration\\1_Comptabilite_Fiscalite\\1_Annee_2020\\Consolidation_Comptable_Fiscale_2020.xls")

        workbook = xlrd.open_workbook(location)

        sheet = workbook.sheet_by_name("Annexe_T_D_P_D_T_S_B")

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
               '<title>Annexe_T_D_P_D_T_S_B</title>' + \
               '</head>' + \
               '<body>' + \
               '<div class="container">' + \
               '<div class="card text-center">' + \
               '<div class="card-header text-center">Annexe : Tableau du portefeuille de TIAP en système en base</div>' + \
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
               '<th scope="col" colspan="7">' + str(sheet.cell_value(0, 0)) + '</th>' + \
               '</tr>' + \
               '<tr>' + \
               '<th scope="col" colspan="7">' + str(sheet.cell_value(1, 0)) + '</th>' + \
               '</tr>' + \
               '<tr>' + \
               '<th scope="col">' + str(sheet.cell_value(2, 0)) + '</th>' + \
               '<th scope="col" colspan="3">' + str(sheet.cell_value(2, 1)) + '</th>' + \
               '<th scope="col" colspan="3">' + str(sheet.cell_value(2, 4)) + '</th>' + \
               '</tr>' + \
               '<tr>' + \
               '<th scope="col">' + str(sheet.cell_value(3, 0)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(3, 1)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(3, 2)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(3, 3)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(3, 4)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(3, 5)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(3, 6)) + '</th>' + \
               '</tr>' + \
               '<tr>' + \
               '<th scope="col" colspan="7">' + str(sheet.cell_value(4, 0)) + '</th>' + \
               '</tr>' + \
               '</thead>' + \
               '<tbody>' + \
               '<tr>' + \
               '<td><b>' + str(sheet.cell_value(5, 0)) + '</b></td>' + \
               '<td>' + str(sheet.cell_value(5, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(5, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(5, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(5, 4)) + '</td>' + \
               '<td>' + str(sheet.cell_value(5, 5)) + '</td>' + \
               '<td>' + str(sheet.cell_value(5, 6)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><b>' + str(sheet.cell_value(6, 0)) + '</b></td>' + \
               '<td>' + str(sheet.cell_value(6, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(6, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(6, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(6, 4)) + '</td>' + \
               '<td>' + str(sheet.cell_value(6, 5)) + '</td>' + \
               '<td>' + str(sheet.cell_value(6, 6)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><b>' + str(sheet.cell_value(7, 0)) + '</b></td>' + \
               '<td>' + str(sheet.cell_value(7, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(7, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(7, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(7, 4)) + '</td>' + \
               '<td>' + str(sheet.cell_value(7, 5)) + '</td>' + \
               '<td>' + str(sheet.cell_value(7, 6)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><b>' + str(sheet.cell_value(8, 0)) + '</b></td>' + \
               '<td>' + str(sheet.cell_value(8, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(8, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(8, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(8, 4)) + '</td>' + \
               '<td>' + str(sheet.cell_value(8, 5)) + '</td>' + \
               '<td>' + str(sheet.cell_value(8, 6)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><b>' + str(sheet.cell_value(9, 0)) + '</b></td>' + \
               '<td>' + str(sheet.cell_value(9, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(9, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(9, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(9, 4)) + '</td>' + \
               '<td>' + str(sheet.cell_value(9, 5)) + '</td>' + \
               '<td>' + str(sheet.cell_value(9, 6)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><b>' + str(sheet.cell_value(10, 0)) + '</b></td>' + \
               '<td>' + str(sheet.cell_value(10, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(10, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(10, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(10, 4)) + '</td>' + \
               '<td>' + str(sheet.cell_value(10, 5)) + '</td>' + \
               '<td>' + str(sheet.cell_value(10, 6)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><b><i>' + str(sheet.cell_value(11, 0)) + '</i></b></td>' + \
               '<td>' + str(sheet.cell_value(11, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(11, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(11, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(11, 4)) + '</td>' + \
               '<td>' + str(sheet.cell_value(11, 5)) + '</td>' + \
               '<td>' + str(sheet.cell_value(11, 6)) + '</td>' + \
               '</tr>' + \
               '</tbody>' + \
               '</table>' + \
               '<br>' + \
               '<table class="table table-bordered">' + \
               '<thead>' + \
               '<tr>' + \
               '<th scope="col" colspan="3">' + str(sheet.cell_value(13, 0)) + '</th>' + \
               '</tr>' + \
               '<tr>' + \
               '<th scope="col" colspan="3">' + str(sheet.cell_value(14, 0)) + '</th>' + \
               '</tr>' + \
               '<tr>' + \
               '<th scope="col">' + str(sheet.cell_value(15, 0)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(15, 1)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(15, 2)) + '</th>' + \
               '</tr>' + \
               '</thead>' + \
               '<tbody>' + \
               '<tr>' + \
               '<td><b>' + str(sheet.cell_value(16, 0)) + '</b></td>' + \
               '<td>' + str(sheet.cell_value(16, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(16, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><b>' + str(sheet.cell_value(17, 0)) + '</b></td>' + \
               '<td>' + str(sheet.cell_value(17, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(17, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><b>' + str(sheet.cell_value(18, 0)) + '</b></td>' + \
               '<td>' + str(sheet.cell_value(18, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(18, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><b>' + str(sheet.cell_value(19, 0)) + '</b></td>' + \
               '<td>' + str(sheet.cell_value(19, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(19, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><b>' + str(sheet.cell_value(20, 0)) + '</b></td>' + \
               '<td>' + str(sheet.cell_value(20, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(20, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i>' + str(sheet.cell_value(21, 0)) + '</i></td>' + \
               '<td>' + str(sheet.cell_value(21, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(21, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i>' + str(sheet.cell_value(22, 0)) + '</i></td>' + \
               '<td>' + str(sheet.cell_value(22, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(22, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><b>' + str(sheet.cell_value(23, 0)) + '</b></td>' + \
               '<td>' + str(sheet.cell_value(23, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(23, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><b>' + str(sheet.cell_value(24, 0)) + '</b></td>' + \
               '<td>' + str(sheet.cell_value(24, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(24, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i>' + str(sheet.cell_value(25, 0)) + '</i></td>' + \
               '<td>' + str(sheet.cell_value(25, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(25, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i>' + str(sheet.cell_value(26, 0)) + '</i></td>' + \
               '<td>' + str(sheet.cell_value(26, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(26, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><b>' + str(sheet.cell_value(27, 0)) + '</b></td>' + \
               '<td>' + str(sheet.cell_value(27, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(27, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><b><i>' + str(sheet.cell_value(28, 0)) + '</i></b></td>' + \
               '<td>' + str(sheet.cell_value(28, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(28, 2)) + '</td>' + \
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
               'footer-left': "Annexe : Tableau du portefeuille de TIAP en \n système en base de l'exercice " + str(round(float(str(workbook.sheet_by_name("Informations_Entreprise").cell_value(8, 1)).split(".")[0]))),
               'footer-right': '[page] sur [topage]'
        }

        path_wkthmltopdf = "C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe"
        
        config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
        
        pdfkit.from_string(body, "Holomorphe\\Annee_" + annee + "\\Annexe_T_D_P_D_T_S_B\\Annexe_T_D_P_D_T_S_B.pdf", configuration=config, options=options)

        filename = "Holomorphe\\Annee_" + annee + "\\Annexe_T_D_P_D_T_S_B\\Annexe_T_D_P_D_T_S_B.pdf"

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

    def test_annexe_determination_de_la_capacite_d_autofinancement_s_d(self):
        print("test_annexe_determination_de_la_capacite_d_autofinancement_s_d")
        
        annee = "2020"
        
        location = ("A:\\1_Professionnel\\1_Holomorphe\\1_Administration\\1_Comptabilite_Fiscalite\\1_Annee_2020\\Consolidation_Comptable_Fiscale_2020.xls")

        workbook = xlrd.open_workbook(location)

        sheet = workbook.sheet_by_name("Annexe_D_D_L_C_D_A_S_D")

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
               '<title>Annexe_D_D_L_C_D_A_S_D</title>' + \
               '</head>' + \
               '<body>' + \
               '<div class="container">' + \
               '<div class="card text-center">' + \
               '<div class="card-header text-center">Annexe : Détermination de la capacité d' + "'autofinancement" + ' en système développé</div>' + \
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
               '</tr>' + \
               '</thead>' + \
               '<tbody>' + \
               '<tr>' + \
               '<td><b>' + str(sheet.cell_value(1, 0)) + '</b></td>' + \
               '<td>' + str(sheet.cell_value(1, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(1, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><b>' + str(sheet.cell_value(2, 0)) + '</b></td>' + \
               '<td>' + str(sheet.cell_value(2, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(2, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><b>' + str(sheet.cell_value(3, 0)) + '</b></td>' + \
               '<td>' + str(sheet.cell_value(3, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(3, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><b>' + str(sheet.cell_value(4, 0)) + '</b></td>' + \
               '<td>' + str(sheet.cell_value(4, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(4, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><b>' + str(sheet.cell_value(5, 0)) + '</b></td>' + \
               '<td>' + str(sheet.cell_value(5, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(5, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><b>' + str(sheet.cell_value(6, 0)) + '</b></td>' + \
               '<td>' + str(sheet.cell_value(6, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(6, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><b>' + str(sheet.cell_value(7, 0)) + '</b></td>' + \
               '<td>' + str(sheet.cell_value(7, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(7, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><b>' + str(sheet.cell_value(8, 0)) + '</b></td>' + \
               '<td>' + str(sheet.cell_value(8, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(8, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><b>' + str(sheet.cell_value(9, 0)) + '</b></td>' + \
               '<td>' + str(sheet.cell_value(9, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(9, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><b>' + str(sheet.cell_value(10, 0)) + '</b></td>' + \
               '<td>' + str(sheet.cell_value(10, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(10, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><b>' + str(sheet.cell_value(11, 0)) + '</b></td>' + \
               '<td>' + str(sheet.cell_value(11, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(11, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><b><i>' + str(sheet.cell_value(12, 0)) + '</i></b></td>' + \
               '<td>' + str(sheet.cell_value(12, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(12, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="3">' + str(sheet.cell_value(13, 0)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="3">' + str(sheet.cell_value(14, 0)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="3">' + str(sheet.cell_value(15, 0)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="3">' + str(sheet.cell_value(16, 0)) + '</td>' + \
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
               'footer-left': "Annexe : Détermination de la capacité \n d'autofinancement de l'exercice " + str(round(float(str(workbook.sheet_by_name("Informations_Entreprise").cell_value(8, 1)).split(".")[0]))),
               'footer-right': '[page] sur [topage]'
        }
        
        path_wkthmltopdf = "C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe"
        
        config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
        
        pdfkit.from_string(body, "Holomorphe\\Annee_" + annee + "\\Annexe_D_D_L_C_D_A_S_D\\Annexe_D_D_L_C_D_A_S_D.pdf", configuration=config, options=options)

        filename = "Holomorphe\\Annee_" + annee + "\\Annexe_D_D_L_C_D_A_S_D\\Annexe_D_D_L_C_D_A_S_D.pdf"

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

    def test_annexe_tableau_des_soldes_intermediaires_de_gestion_s_d(self):
        print("test_annexe_tableau_des_soldes_intermediaires_de_gestion_s_d")
        
        annee = "2020"
        
        location = ("A:\\1_Professionnel\\1_Holomorphe\\1_Administration\\1_Comptabilite_Fiscalite\\1_Annee_2020\\Consolidation_Comptable_Fiscale_2020.xls")

        workbook = xlrd.open_workbook(location)

        sheet = workbook.sheet_by_name("Annexe__T_D_S_I_D_G_S_D")

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
               '<title>Annexe__T_D_S_I_D_G_S_D</title>' + \
               '</head>' + \
               '<body>' + \
               '<div class="container">' + \
               '<div class="card text-center">' + \
               '<div class="card-header text-center">Annexe : Tableau des soldes intermédiaires de gestion en système développé</div>' + \
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
               '<th scope="col" colspan="7">' + str(sheet.cell_value(0, 0)) + '</th>' + \
               '</tr>' + \
               '<tr>' + \
               '<th scope="col">' + str(sheet.cell_value(1, 0)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(1, 1)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(1, 2)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(1, 3)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(1, 4)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(1, 5)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(1, 6)) + '</th>' + \
               '</tr>' + \
               '</thead>' + \
               '<tbody>' + \
               '<tr>' + \
               '<td><b>' + str(sheet.cell_value(2, 0)) + '</b></td>' + \
               '<td>' + str(sheet.cell_value(2, 1)) + '</td>' + \
               '<td><b>' + str(sheet.cell_value(2, 2)) + '</b></td>' + \
               '<td>' + str(sheet.cell_value(2, 3)) + '</td>' + \
               '<td><b><i>' + str(sheet.cell_value(2, 4)) + '</i></b></td>' + \
               '<td>' + str(sheet.cell_value(2, 5)) + '</td>' + \
               '<td>' + str(sheet.cell_value(2, 6)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><b>' + str(sheet.cell_value(3, 0)) + '</b></td>' + \
               '<td>' + str(sheet.cell_value(3, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(3, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(3, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(3, 4)) + '</td>' + \
               '<td>' + str(sheet.cell_value(3, 5)) + '</td>' + \
               '<td>' + str(sheet.cell_value(3, 6)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><b>' + str(sheet.cell_value(4, 0)) + '</b></td>' + \
               '<td>' + str(sheet.cell_value(4, 1)) + '</td>' + \
               '<td><b>' + str(sheet.cell_value(4, 2)) + '</b></td>' + \
               '<td>' + str(sheet.cell_value(4, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(4, 4)) + '</td>' + \
               '<td>' + str(sheet.cell_value(4, 5)) + '</td>' + \
               '<td>' + str(sheet.cell_value(4, 6)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><b>' + str(sheet.cell_value(5, 0)) + '</b></td>' + \
               '<td>' + str(sheet.cell_value(5, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(5, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(5, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(5, 4)) + '</td>' + \
               '<td>' + str(sheet.cell_value(5, 5)) + '</td>' + \
               '<td>' + str(sheet.cell_value(5, 6)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><b><i>' + str(sheet.cell_value(6, 0)) + '</i></b></td>' + \
               '<td>' + str(sheet.cell_value(6, 1)) + '</td>' + \
               '<td><b><i>' + str(sheet.cell_value(6, 2)) + '</i></b></td>' + \
               '<td>' + str(sheet.cell_value(6, 3)) + '</td>' + \
               '<td><b><i>' + str(sheet.cell_value(6, 4)) + '</i></b></td>' + \
               '<td>' + str(sheet.cell_value(6, 5)) + '</td>' + \
               '<td>' + str(sheet.cell_value(6, 6)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><b>' + str(sheet.cell_value(7, 0)) + '</b></td>' + \
               '<td>' + str(sheet.cell_value(7, 1)) + '</td>' + \
               '<td><b>' + str(sheet.cell_value(7, 2)) + '</b></td>' + \
               '<td>' + str(sheet.cell_value(7, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(7, 4)) + '</td>' + \
               '<td>' + str(sheet.cell_value(7, 5)) + '</td>' + \
               '<td>' + str(sheet.cell_value(7, 6)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><b>' + str(sheet.cell_value(8, 0)) + '</b></td>' + \
               '<td>' + str(sheet.cell_value(8, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(8, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(8, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(8, 4)) + '</td>' + \
               '<td>' + str(sheet.cell_value(8, 5)) + '</td>' + \
               '<td>' + str(sheet.cell_value(8, 6)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><b><i>' + str(sheet.cell_value(9, 0)) + '</i></b></td>' + \
               '<td>' + str(sheet.cell_value(9, 1)) + '</td>' + \
               '<td><b><i>' + str(sheet.cell_value(9, 2)) + '</i></b></td>' + \
               '<td>' + str(sheet.cell_value(9, 3)) + '</td>' + \
               '<td><b><i>' + str(sheet.cell_value(9, 4)) + '</i></b></td>' + \
               '<td>' + str(sheet.cell_value(9, 5)) + '</td>' + \
               '<td>' + str(sheet.cell_value(9, 6)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><b>' + str(sheet.cell_value(10, 0)) + '</b></td>' + \
               '<td>' + str(sheet.cell_value(10, 1)) + '</td>' + \
               '<td><b>' + str(sheet.cell_value(10, 2)) + '</b></td>' + \
               '<td>' + str(sheet.cell_value(10, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(10, 4)) + '</td>' + \
               '<td>' + str(sheet.cell_value(10, 5)) + '</td>' + \
               '<td>' + str(sheet.cell_value(10, 6)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><b>' + str(sheet.cell_value(11, 0)) + '</b></td>' + \
               '<td>' + str(sheet.cell_value(11, 1)) + '</td>' + \
               '<td><b>' + str(sheet.cell_value(11, 2)) + '</b></td>' + \
               '<td>' + str(sheet.cell_value(11, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(11, 4)) + '</td>' + \
               '<td>' + str(sheet.cell_value(11, 5)) + '</td>' + \
               '<td>' + str(sheet.cell_value(11, 6)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><b><i>' + str(sheet.cell_value(12, 0)) + '</i></b></td>' + \
               '<td>' + str(sheet.cell_value(12, 1)) + '</td>' + \
               '<td><b><i>' + str(sheet.cell_value(12, 2)) + '</i></b></td>' + \
               '<td>' + str(sheet.cell_value(12, 3)) + '</td>' + \
               '<td><b><i>' + str(sheet.cell_value(12, 4)) + '</i></b></td>' + \
               '<td>' + str(sheet.cell_value(12, 5)) + '</td>' + \
               '<td>' + str(sheet.cell_value(12, 6)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><b>' + str(sheet.cell_value(13, 0)) + '</b></td>' + \
               '<td>' + str(sheet.cell_value(13, 1)) + '</td>' + \
               '<td><b>' + str(sheet.cell_value(13, 2)) + '</b></td>' + \
               '<td>' + str(sheet.cell_value(13, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(13, 4)) + '</td>' + \
               '<td>' + str(sheet.cell_value(13, 5)) + '</td>' + \
               '<td>' + str(sheet.cell_value(13, 6)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><b>' + str(sheet.cell_value(14, 0)) + '</b></td>' + \
               '<td>' + str(sheet.cell_value(14, 1)) + '</td>' + \
               '<td><b>' + str(sheet.cell_value(14, 2)) + '</b></td>' + \
               '<td>' + str(sheet.cell_value(14, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(14, 4)) + '</td>' + \
               '<td>' + str(sheet.cell_value(14, 5)) + '</td>' + \
               '<td>' + str(sheet.cell_value(14, 6)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><b>' + str(sheet.cell_value(15, 0)) + '</b></td>' + \
               '<td>' + str(sheet.cell_value(15, 1)) + '</td>' + \
               '<td><b>' + str(sheet.cell_value(15, 2)) + '</b></td>' + \
               '<td>' + str(sheet.cell_value(15, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(15, 4)) + '</td>' + \
               '<td>' + str(sheet.cell_value(15, 5)) + '</td>' + \
               '<td>' + str(sheet.cell_value(15, 6)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><b><i>' + str(sheet.cell_value(16, 0)) + '</i></b></td>' + \
               '<td>' + str(sheet.cell_value(16, 1)) + '</td>' + \
               '<td><b><i>' + str(sheet.cell_value(16, 2)) + '</i></b></td>' + \
               '<td>' + str(sheet.cell_value(16, 3)) + '</td>' + \
               '<td><b><i>' + str(sheet.cell_value(16, 4)) + '</i></b></td>' + \
               '<td>' + str(sheet.cell_value(16, 5)) + '</td>' + \
               '<td>' + str(sheet.cell_value(16, 6)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><b>' + str(sheet.cell_value(17, 0)) + '</b></td>' + \
               '<td>' + str(sheet.cell_value(17, 1)) + '</td>' + \
               '<td><b>' + str(sheet.cell_value(17, 2)) + '</b></td>' + \
               '<td>' + str(sheet.cell_value(17, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(17, 4)) + '</td>' + \
               '<td>' + str(sheet.cell_value(17, 5)) + '</td>' + \
               '<td>' + str(sheet.cell_value(17, 6)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><b>' + str(sheet.cell_value(18, 0)) + '</b></td>' + \
               '<td>' + str(sheet.cell_value(18, 1)) + '</td>' + \
               '<td><b>' + str(sheet.cell_value(18, 2)) + '</b></td>' + \
               '<td>' + str(sheet.cell_value(18, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(18, 4)) + '</td>' + \
               '<td>' + str(sheet.cell_value(18, 5)) + '</td>' + \
               '<td>' + str(sheet.cell_value(18, 6)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><b>' + str(sheet.cell_value(19, 0)) + '</b></td>' + \
               '<td>' + str(sheet.cell_value(19, 1)) + '</td>' + \
               '<td><b>' + str(sheet.cell_value(19, 2)) + '</b></td>' + \
               '<td>' + str(sheet.cell_value(19, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(19, 4)) + '</td>' + \
               '<td>' + str(sheet.cell_value(19, 5)) + '</td>' + \
               '<td>' + str(sheet.cell_value(19, 6)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><b><i>' + str(sheet.cell_value(20, 0)) + '</i></b></td>' + \
               '<td>' + str(sheet.cell_value(20, 1)) + '</td>' + \
               '<td><b><i>' + str(sheet.cell_value(20, 2)) + '</i></b></td>' + \
               '<td>' + str(sheet.cell_value(20, 3)) + '</td>' + \
               '<td><b><i>' + str(sheet.cell_value(20, 4)) + '</i></b></td>' + \
               '<td>' + str(sheet.cell_value(20, 5)) + '</td>' + \
               '<td>' + str(sheet.cell_value(20, 6)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><b>' + str(sheet.cell_value(21, 0)) + '<b></td>' + \
               '<td>' + str(sheet.cell_value(21, 1)) + '</td>' + \
               '<td><b>' + str(sheet.cell_value(21, 2)) + '<b></td>' + \
               '<td>' + str(sheet.cell_value(21, 3)) + '</td>' + \
               '<td><b><i>' + str(sheet.cell_value(21, 4)) + '</i></b></td>' + \
               '<td>' + str(sheet.cell_value(21, 5)) + '</td>' + \
               '<td>' + str(sheet.cell_value(21, 6)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><b>' + str(sheet.cell_value(22, 0)) + '</b></td>' + \
               '<td>' + str(sheet.cell_value(22, 1)) + '</td>' + \
               '<td><b>' + str(sheet.cell_value(22, 2)) + '</b></td>' + \
               '<td>' + str(sheet.cell_value(22, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(22, 4)) + '</td>' + \
               '<td>' + str(sheet.cell_value(22, 5)) + '</td>' + \
               '<td>' + str(sheet.cell_value(22, 6)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><b>' + str(sheet.cell_value(23, 0)) + '</b></td>' + \
               '<td>' + str(sheet.cell_value(23, 1)) + '</td>' + \
               '<td><b>' + str(sheet.cell_value(23, 2)) + '</b></td>' + \
               '<td>' + str(sheet.cell_value(23, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(23, 4)) + '</td>' + \
               '<td>' + str(sheet.cell_value(23, 5)) + '</td>' + \
               '<td>' + str(sheet.cell_value(23, 6)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(24, 0)) + '</td>' + \
               '<td>' + str(sheet.cell_value(24, 1)) + '</td>' + \
               '<td><b>' + str(sheet.cell_value(24, 2)) + '</b></td>' + \
               '<td>' + str(sheet.cell_value(24, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(24, 4)) + '</td>' + \
               '<td>' + str(sheet.cell_value(24, 5)) + '</td>' + \
               '<td>' + str(sheet.cell_value(24, 6)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(25, 0)) + '</td>' + \
               '<td>' + str(sheet.cell_value(25, 1)) + '</td>' + \
               '<td><b>' + str(sheet.cell_value(25, 2)) + '</b></td>' + \
               '<td>' + str(sheet.cell_value(25, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(25, 4)) + '</td>' + \
               '<td>' + str(sheet.cell_value(25, 5)) + '</td>' + \
               '<td>' + str(sheet.cell_value(25, 6)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><b><i>' + str(sheet.cell_value(26, 0)) + '</i></b></td>' + \
               '<td>' + str(sheet.cell_value(26, 1)) + '</td>' + \
               '<td><b><i>' + str(sheet.cell_value(26, 2)) + '</i></b></td>' + \
               '<td>' + str(sheet.cell_value(26, 3)) + '</td>' + \
               '<td><b><i>' + str(sheet.cell_value(26, 4)) + '</i></b></td>' + \
               '<td>' + str(sheet.cell_value(26, 5)) + '</td>' + \
               '<td>' + str(sheet.cell_value(26, 6)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><b>' + str(sheet.cell_value(27, 0)) + '</b></td>' + \
               '<td>' + str(sheet.cell_value(27, 1)) + '</td>' + \
               '<td><b>' + str(sheet.cell_value(27, 2)) + '</b></td>' + \
               '<td>' + str(sheet.cell_value(27, 3)) + '</td>' + \
               '<td><b><i>' + str(sheet.cell_value(27, 4)) + '</i></b></td>' + \
               '<td>' + str(sheet.cell_value(27, 5)) + '</td>' + \
               '<td>' + str(sheet.cell_value(27, 6)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="7">' + str(sheet.cell_value(28, 0)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="7">' + str(sheet.cell_value(29, 0)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="7">' + str(sheet.cell_value(30, 0)) + '</td>' + \
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
        translator = Translator(to_lang="French")
        python_date = xlrd.xldate_as_tuple(excel_date_1, 0)
        x = datetime.datetime(python_date[0], python_date[1], python_date[2])
        clos_le = translator.translate(x.strftime("%A")).title() \
                  + " " \
                  + x.strftime("%d") \
                  + " " \
                  + translator.translate(x.strftime("%B")).title() \
                  + " " \
                  + x.strftime("%Y")

        options = {
               'page-size': 'A4',
               'header-right': 'Société HOLOMORPHE [SIREN : 883 632 556]',
               'header-left': 'Exercice clos le ' + clos_le,
               'footer-left': "Annexe : Tableau des soldes intermédiaires de gestion de l'exercice " + str(round(float(str(workbook.sheet_by_name("Informations_Entreprise").cell_value(8, 1)).split(".")[0]))),
               'footer-right': '[page] sur [topage]'
        }

        path_wkthmltopdf = "C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe"
        
        config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
        
        pdfkit.from_string(body, "Holomorphe\\Annee_" + annee + "\\Annexe__T_D_S_I_D_G_S_D\\Annexe__T_D_S_I_D_G_S_D.pdf", configuration=config, options=options)

        filename = "Holomorphe\\Annee_" + annee + "\\Annexe__T_D_S_I_D_G_S_D\\Annexe__T_D_S_I_D_G_S_D.pdf"

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

    def test_annexe_modeles_de_tableau_des_emplois_et_des_ressources_tableau_de_financement_en_compte_s_d(self):
        print("test_annexe_modeles_de_tableau_des_emplois_et_des_ressources_tableau_de_financement_en_compte_s_d")

        annee = "2020"

        location = ("A:\\1_Professionnel\\1_Holomorphe\\1_Administration\\1_Comptabilite_Fiscalite\\1_Annee_2020\\Consolidation_Comptable_Fiscale_2020.xls")

        workbook = xlrd.open_workbook(location)

        sheet = workbook.sheet_by_name("Annexe_T_E_R__T_D_F_E_C_S_D")

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
               '<title>Annexe_T_E_R__T_D_F_E_C_S_D</title>' + \
               '</head>' + \
               '<body>' + \
               '<div class="container">' + \
               '<div class="card text-center">' + \
               '<div class="card-header text-center">Annexe : Tableau de financement en compte en système développé</div>' + \
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
               '<th scope="col" colspan="6">' + str(sheet.cell_value(0, 0)) + '</th>' + \
               '</tr>' + \
               '<tr>' + \
               '<th scope="col">' + str(sheet.cell_value(1, 0)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(1, 1)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(1, 2)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(1, 3)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(1, 4)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(1, 5)) + '</th>' + \
               '</tr>' + \
               '</thead>' + \
               '<tbody>' + \
               '<tr>' + \
               '<td><b>' + str(sheet.cell_value(2, 0)) + '</b></td>' + \
               '<td>' + str(sheet.cell_value(2, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(2, 2)) + '</td>' + \
               '<td><b>' + str(sheet.cell_value(2, 3)) + '</b></td>' + \
               '<td>' + str(sheet.cell_value(2, 4)) + '</td>' + \
               '<td>' + str(sheet.cell_value(2, 5)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><b>' + str(sheet.cell_value(3, 0)) + '</b></td>' + \
               '<td>' + str(sheet.cell_value(3, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(3, 2)) + '</td>' + \
               '<td><b>' + str(sheet.cell_value(3, 3)) + '</b></td>' + \
               '<td>' + str(sheet.cell_value(3, 4)) + '</td>' + \
               '<td>' + str(sheet.cell_value(3, 5)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i>' + str(sheet.cell_value(4, 0)) + '</i></td>' + \
               '<td>' + str(sheet.cell_value(4, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(4, 2)) + '</td>' + \
               '<td><i>' + str(sheet.cell_value(4, 3)) + '</i></td>' + \
               '<td>' + str(sheet.cell_value(4, 4)) + '</td>' + \
               '<td>' + str(sheet.cell_value(4, 5)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i>' + str(sheet.cell_value(5, 0)) + '</i></td>' + \
               '<td>' + str(sheet.cell_value(5, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(5, 2)) + '</td>' + \
               '<td><u>' + str(sheet.cell_value(5, 3)) + '</u></td>' + \
               '<td>' + str(sheet.cell_value(5, 4)) + '</td>' + \
               '<td>' + str(sheet.cell_value(5, 5)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i>' + str(sheet.cell_value(6, 0)) + '</i></td>' + \
               '<td>' + str(sheet.cell_value(6, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(6, 2)) + '</td>' + \
               '<td><u>' + str(sheet.cell_value(6, 3)) + '</u></td>' + \
               '<td>' + str(sheet.cell_value(6, 4)) + '</td>' + \
               '<td>' + str(sheet.cell_value(6, 5)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><b>' + str(sheet.cell_value(7, 0)) + '</b></td>' + \
               '<td>' + str(sheet.cell_value(7, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(7, 2)) + '</td>' + \
               '<td><i>' + str(sheet.cell_value(7, 3)) + '</i></td>' + \
               '<td>' + str(sheet.cell_value(7, 4)) + '</td>' + \
               '<td>' + str(sheet.cell_value(7, 5)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><b>' + str(sheet.cell_value(8, 0)) + '</b></td>' + \
               '<td>' + str(sheet.cell_value(8, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(8, 2)) + '</td>' + \
               '<td><b>' + str(sheet.cell_value(8, 3)) + '</b></td>' + \
               '<td>' + str(sheet.cell_value(8, 4)) + '</td>' + \
               '<td>' + str(sheet.cell_value(8, 5)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(9, 0)) + '</td>' + \
               '<td>' + str(sheet.cell_value(9, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(9, 2)) + '</td>' + \
               '<td><i>' + str(sheet.cell_value(9, 3)) + '</i></td>' + \
               '<td>' + str(sheet.cell_value(9, 4)) + '</td>' + \
               '<td>' + str(sheet.cell_value(9, 5)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(10, 0)) + '</td>' + \
               '<td>' + str(sheet.cell_value(10, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(10, 2)) + '</td>' + \
               '<td><i>' + str(sheet.cell_value(10, 3)) + '</i></td>' + \
               '<td>' + str(sheet.cell_value(10, 4)) + '</td>' + \
               '<td>' + str(sheet.cell_value(10, 5)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><b>' + str(sheet.cell_value(11, 0)) + '</b></td>' + \
               '<td>' + str(sheet.cell_value(11, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(11, 2)) + '</td>' + \
               '<td><b>' + str(sheet.cell_value(11, 3)) + '</b></td>' + \
               '<td>' + str(sheet.cell_value(11, 4)) + '</td>' + \
               '<td>' + str(sheet.cell_value(11, 5)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><b><i>' + str(sheet.cell_value(12, 0)) + '</i></b></td>' + \
               '<td>' + str(sheet.cell_value(12, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(12, 2)) + '</td>' + \
               '<td><b><i>' + str(sheet.cell_value(12, 3)) + '</i></b></td>' + \
               '<td>' + str(sheet.cell_value(12, 4)) + '</td>' + \
               '<td>' + str(sheet.cell_value(12, 5)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><b><i>' + str(sheet.cell_value(13, 0)) + '</i></b></td>' + \
               '<td>' + str(sheet.cell_value(13, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(13, 2)) + '</td>' + \
               '<td><b><i>' + str(sheet.cell_value(13, 3)) + '</i></b></td>' + \
               '<td>' + str(sheet.cell_value(13, 4)) + '</td>' + \
               '<td>' + str(sheet.cell_value(13, 5)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="6">' + str(sheet.cell_value(14, 0)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="6">' + str(sheet.cell_value(15, 0)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="6">' + str(sheet.cell_value(16, 0)) + '</td>' + \
               '</tr>' + \
               '</tbody>' + \
               '</table>' + \
               '<br>' + \
               '<table class="table table-bordered">' + \
               '<thead>' + \
               '<tr>' + \
               '<th scope="col" colspan="5">' + str(sheet.cell_value(18, 0)) + '</th>' + \
               '</tr>' + \
               '<tr>' + \
               '<th scope="col">' + str(sheet.cell_value(19, 0)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(19, 1)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(19, 2)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(19, 3)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(19, 4)) + '</th>' + \
               '</tr>' + \
               '</thead>' + \
               '<tbody>' + \
               '<tr>' + \
               '<td colspan="5"><b>' + str(sheet.cell_value(20, 0)) + '</b></td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i>' + str(sheet.cell_value(21, 0)) + '</i></td>' + \
               '<td>' + str(sheet.cell_value(21, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(21, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(21, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(21, 4)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><u>' + str(sheet.cell_value(22, 0)) + '</u></td>' + \
               '<td>' + str(sheet.cell_value(22, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(22, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(22, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(22, 4)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><u>' + str(sheet.cell_value(23, 0)) + '</u></td>' + \
               '<td>' + str(sheet.cell_value(23, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(23, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(23, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(23, 4)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><u>' + str(sheet.cell_value(24, 0)) + '</u></td>' + \
               '<td>' + str(sheet.cell_value(24, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(24, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(24, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(24, 4)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i>' + str(sheet.cell_value(25, 0)) + '</i></td>' + \
               '<td>' + str(sheet.cell_value(25, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(25, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(25, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(25, 4)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><u>' + str(sheet.cell_value(26, 0)) + '</u></td>' + \
               '<td>' + str(sheet.cell_value(26, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(26, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(26, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(26, 4)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><u>' + str(sheet.cell_value(27, 0)) + '</u></td>' + \
               '<td>' + str(sheet.cell_value(27, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(27, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(27, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(27, 4)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><b><i>' + str(sheet.cell_value(28, 0)) + '</i></b></td>' + \
               '<td>' + str(sheet.cell_value(28, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(28, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(28, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(28, 4)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="5"><b>' + str(sheet.cell_value(29, 0)) + '</b></td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="5"><i>' + str(sheet.cell_value(30, 0)) + '</i></td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><u>' + str(sheet.cell_value(31, 0)) + '</u></td>' + \
               '<td>' + str(sheet.cell_value(31, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(31, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(31, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(31, 4)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><u>' + str(sheet.cell_value(32, 0)) + '</u></td>' + \
               '<td>' + str(sheet.cell_value(32, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(32, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(32, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(32, 4)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><b><i>' + str(sheet.cell_value(33, 0)) + '</i></b></td>' + \
               '<td>' + str(sheet.cell_value(33, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(33, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(33, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(33, 4)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><b>' + str(sheet.cell_value(34, 0)) + '</b></td>' + \
               '<td>' + str(sheet.cell_value(34, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(34, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(34, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(34, 4)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><b><i>' + str(sheet.cell_value(35, 0)) + '</i></b></td>' + \
               '<td>' + str(sheet.cell_value(35, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(35, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(35, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(35, 4)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><b><i>' + str(sheet.cell_value(36, 0)) + '</i></b></td>' + \
               '<td>' + str(sheet.cell_value(36, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(36, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(36, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(36, 4)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="5"><b><i>' + str(sheet.cell_value(37, 0)) + '</i></b></td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><b><i>' + str(sheet.cell_value(38, 0)) + '</i></b></td>' + \
               '<td>' + str(sheet.cell_value(38, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(38, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(38, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(38, 4)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i>' + str(sheet.cell_value(39, 0)) + '</i></td>' + \
               '<td>' + str(sheet.cell_value(39, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(39, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(39, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(39, 4)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i>' + str(sheet.cell_value(40, 0)) + '</i></td>' + \
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
               '<td><b><i>' + str(sheet.cell_value(42, 0)) + '</i></b></td>' + \
               '<td>' + str(sheet.cell_value(42, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(42, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(42, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(42, 4)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><b>' + str(sheet.cell_value(43, 0)) + '</b></td>' + \
               '<td>' + str(sheet.cell_value(43, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(43, 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(43, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(43, 4)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="5"><b><i>' + str(sheet.cell_value(44, 0)) + '</i></b></td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="3"><b><i>' + str(sheet.cell_value(45, 0)) + '</i></b></td>' + \
               '<td>' + str(sheet.cell_value(45, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(45, 4)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="5"><b><i>' + str(sheet.cell_value(46, 0)) + '</i></b></td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="3"><b><i>' + str(sheet.cell_value(47, 0)) + '</i></b></td>' + \
               '<td>' + str(sheet.cell_value(47, 3)) + '</td>' + \
               '<td>' + str(sheet.cell_value(47, 4)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="5">' + str(sheet.cell_value(48, 0)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="5">' + str(sheet.cell_value(49, 0)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="5">' + str(sheet.cell_value(50, 0)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="5">' + str(sheet.cell_value(51, 0)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="5">' + str(sheet.cell_value(52, 0)) + '</td>' + \
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
               'footer-left': "Annexe : Tableau de financement en compte en \n système développé de l'exercice " + str(round(float(str(workbook.sheet_by_name("Informations_Entreprise").cell_value(8, 1)).split(".")[0]))),
               'footer-right': '[page] sur [topage]'
        }

        path_wkthmltopdf = "C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe"

        config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)

        pdfkit.from_string(body, "Holomorphe\\Annee_" + annee + "\\Annexe_T_E_R__T_D_F_E_C_S_D\\Annexe_T_E_R__T_D_F_E_C_S_D.pdf", configuration=config, options=options)

        filename = "Holomorphe\\Annee_" + annee + "\\Annexe_T_E_R__T_D_F_E_C_S_D\\Annexe_T_E_R__T_D_F_E_C_S_D.pdf"

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

    def test_annexe_modeles_de_tableau_des_emplois_et_des_ressources_tableau_de_financement_en_liste_s_d(self):
        print("test_annexe_modeles_de_tableau_des_emplois_et_des_ressources_tableau_de_financement_en_liste_s_d")
        
        annee = "2020"
        
        location = ("A:\\1_Professionnel\\1_Holomorphe\\1_Administration\\1_Comptabilite_Fiscalite\\1_Annee_2020\\Consolidation_Comptable_Fiscale_2020.xls")

        workbook = xlrd.open_workbook(location)

        sheet = workbook.sheet_by_name("Annexe__T_E_R___T_D_F_E_L_S_D")

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
           '<title>Annexe__T_E_R___T_D_F_E_L_S_D</title>' + \
           '</head>' + \
           '<body>' + \
           '<div class="container">' + \
           '<div class="card text-center">' + \
           '<div class="card-header text-center">Annexe : Tableau de financement en liste en système développé</div>' + \
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
           '<th scope="col" colspan="3">' + str(sheet.cell_value(0, 0)) + '</th>' + \
           '</tr>' + \
           '<tr>' + \
           '<th scope="col">' + str(sheet.cell_value(1, 0)) + '</th>' + \
           '<th scope="col">' + str(sheet.cell_value(1, 1)) + '</th>' + \
           '<th scope="col">' + str(sheet.cell_value(1, 2)) + '</th>' + \
           '</tr>' + \
           '</thead>' + \
           '<tbody>' + \
           '<tr>' + \
           '<td colspan="3"><b>' + str(sheet.cell_value(2, 0)) + '</b></td>' + \
           '</tr>' + \
           '<tr>' + \
           '<td><i>' + str(sheet.cell_value(3, 0)) + '</i></td>' + \
           '<td>' + str(sheet.cell_value(3, 1)) + '</td>' + \
           '<td>' + str(sheet.cell_value(3, 2)) + '</td>' + \
           '</tr>' + \
               '<tr>' + \
               '<td><i>' + str(sheet.cell_value(4, 0)) + '</i></td>' + \
               '<td>' + str(sheet.cell_value(4, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(4, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><u>' + str(sheet.cell_value(5, 0)) + '</u></td>' + \
               '<td>' + str(sheet.cell_value(5, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(5, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><u><i>' + str(sheet.cell_value(6, 0)) + '</i></u></td>' + \
               '<td>' + str(sheet.cell_value(6, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(6, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><u><i>' + str(sheet.cell_value(7, 0)) + '</i></u></td>' + \
               '<td>' + str(sheet.cell_value(7, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(7, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><u>' + str(sheet.cell_value(8, 0)) + '</u></td>' + \
               '<td>' + str(sheet.cell_value(8, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(8, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i>' + str(sheet.cell_value(9, 0)) + '</i></td>' + \
               '<td>' + str(sheet.cell_value(9, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(9, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><u>' + str(sheet.cell_value(10, 0)) + '</u></td>' + \
               '<td>' + str(sheet.cell_value(10, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(10, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><u>' + str(sheet.cell_value(11, 0)) + '</u></td>' + \
               '<td>' + str(sheet.cell_value(11, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(11, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><u>' + str(sheet.cell_value(12, 0)) + '</u></td>' + \
               '<td>' + str(sheet.cell_value(12, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(12, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><b><i>' + str(sheet.cell_value(13, 0)) + '</i></b></td>' + \
               '<td>' + str(sheet.cell_value(13, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(13, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="3"><b>' + str(sheet.cell_value(14, 0)) + '</b></td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i>' + str(sheet.cell_value(15, 0)) + '</i></td>' + \
               '<td>' + str(sheet.cell_value(15, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(15, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i>' + str(sheet.cell_value(16, 0)) + '</i></td>' + \
               '<td>' + str(sheet.cell_value(16, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(16, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><u>' + str(sheet.cell_value(17, 0)) + '</u></td>' + \
               '<td>' + str(sheet.cell_value(17, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(17, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><u>' + str(sheet.cell_value(18, 0)) + '</u></td>' + \
               '<td>' + str(sheet.cell_value(18, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(18, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><u>' + str(sheet.cell_value(19, 0)) + '</u></td>' + \
               '<td>' + str(sheet.cell_value(19, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(19, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i>' + str(sheet.cell_value(20, 0)) + '</i></td>' + \
               '<td>' + str(sheet.cell_value(20, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(20, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i>' + str(sheet.cell_value(21, 0)) + '</i></td>' + \
               '<td>' + str(sheet.cell_value(21, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(21, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i>' + str(sheet.cell_value(22, 0)) + '</i></td>' + \
               '<td>' + str(sheet.cell_value(22, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(22, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><b>' + str(sheet.cell_value(23, 0)) + '</b></td>' + \
               '<td>' + str(sheet.cell_value(23, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(23, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="3"><b><i>' + str(sheet.cell_value(24, 0)) + '</i></b></td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><b><i>' + str(sheet.cell_value(25, 0)) + '</i></b></td>' + \
               '<td>' + str(sheet.cell_value(25, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(25, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="3"><b><i>' + str(sheet.cell_value(26, 0)) + '</i></b></td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><b><i>' + str(sheet.cell_value(27, 0)) + '</i></b></td>' + \
               '<td>' + str(sheet.cell_value(27, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(27, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="3">' + str(sheet.cell_value(28, 0)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="3">' + str(sheet.cell_value(29, 0)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="3">' + str(sheet.cell_value(30, 0)) + '</td>' + \
               '</tr>' + \
               '</tbody>' + \
           '</table>' + \
           '<br>' + \
               '<table class="table table-bordered">' + \
               '<thead>' + \
               '<tr>' + \
               '<th scope="col">' + str(sheet.cell_value(32, 0)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(32, 1)) + '</th>' + \
               '<th scope="col">' + str(sheet.cell_value(32, 2)) + '</th>' + \
               '</tr>' + \
               '</thead>' + \
               '<tbody>' + \
               '<tr>' + \
               '<td><b>' + str(sheet.cell_value(33, 0)) + '</b></td>' + \
               '<td>' + str(sheet.cell_value(33, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(33, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i>' + str(sheet.cell_value(34, 0)) + '</i></td>' + \
               '<td>' + str(sheet.cell_value(34, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(34, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><u>' + str(sheet.cell_value(35, 0)) + '</u></td>' + \
               '<td>' + str(sheet.cell_value(35, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(35, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><u>' + str(sheet.cell_value(36, 0)) + '</u></td>' + \
               '<td>' + str(sheet.cell_value(36, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(36, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><u>' + str(sheet.cell_value(37, 0)) + '</u></td>' + \
               '<td>' + str(sheet.cell_value(37, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(37, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i>' + str(sheet.cell_value(38, 0)) + '</i></td>' + \
               '<td>' + str(sheet.cell_value(38, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(38, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><u>' + str(sheet.cell_value(39, 0)) + '</u></td>' + \
               '<td>' + str(sheet.cell_value(39, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(39, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><u>' + str(sheet.cell_value(40, 0)) + '</u></td>' + \
               '<td>' + str(sheet.cell_value(40, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(40, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="3"><b><i>' + str(sheet.cell_value(41, 0)) + '</i></b></td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><b><i>' + str(sheet.cell_value(42, 0)) + '</i></b></td>' + \
               '<td>' + str(sheet.cell_value(42, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(42, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="3"><b><i>' + str(sheet.cell_value(43, 0)) + '</i></b></td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i><b>' + str(sheet.cell_value(44, 0)) + '</b></i></td>' + \
               '<td>' + str(sheet.cell_value(44, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(44, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="3"><b>' + str(sheet.cell_value(45, 0)) + '</b></td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i>' + str(sheet.cell_value(46, 0)) + '</i></td>' + \
               '<td>' + str(sheet.cell_value(46, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(46, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i>' + str(sheet.cell_value(47, 0)) + '</i></td>' + \
               '<td>' + str(sheet.cell_value(47, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(47, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="3"><b><i>' + str(sheet.cell_value(48, 0)) + '</i></b></td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><b><i>' + str(sheet.cell_value(49, 0)) + '</i></b></td>' + \
               '<td>' + str(sheet.cell_value(49, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(49, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="3"><i><b>' + str(sheet.cell_value(50, 0)) + '</b></i></td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i><b>' + str(sheet.cell_value(51, 0)) + '</b></i></td>' + \
               '<td>' + str(sheet.cell_value(51, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(51, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="3"><b>' + str(sheet.cell_value(52, 0)) + '</b></td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i>' + str(sheet.cell_value(53, 0)) + '</i></td>' + \
               '<td>' + str(sheet.cell_value(53, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(53, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i>' + str(sheet.cell_value(54, 0)) + '</i></td>' + \
               '<td>' + str(sheet.cell_value(54, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(54, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i><b>' + str(sheet.cell_value(55, 0)) + '</b></i></td>' + \
               '<td>' + str(sheet.cell_value(55, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(55, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i><b>' + str(sheet.cell_value(56, 0)) + '</b></i></td>' + \
               '<td>' + str(sheet.cell_value(56, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(56, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i><b>' + str(sheet.cell_value(57, 0)) + '</b></i></td>' + \
               '<td>' + str(sheet.cell_value(57, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(57, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="3"><i><b>' + str(sheet.cell_value(58, 0)) + '</b></i></td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td><i><b>' + str(sheet.cell_value(59, 0)) + '</b></i></td>' + \
               '<td>' + str(sheet.cell_value(59, 1)) + '</td>' + \
               '<td>' + str(sheet.cell_value(59, 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="3">' + str(sheet.cell_value(60, 0)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="3">' + str(sheet.cell_value(61, 0)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="3">' + str(sheet.cell_value(62, 0)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="3">' + str(sheet.cell_value(63, 0)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="3">' + str(sheet.cell_value(64, 0)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="3">' + str(sheet.cell_value(65, 0)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="3">' + str(sheet.cell_value(66, 0)) + '</td>' + \
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
           'footer-left': "Annexe : Tableau de financement en liste \n en système développé de l'exercice " + str(round(float(str(workbook.sheet_by_name("Informations_Entreprise").cell_value(8, 1)).split(".")[0]))),
           'footer-right': '[page] sur [topage]'
        }

        path_wkthmltopdf = "C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe"

        config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)

        pdfkit.from_string(body, "Holomorphe\\Annee_" + annee + "\\Annexe__T_E_R___T_D_F_E_L_S_D\\Annexe__T_E_R___T_D_F_E_L_S_D.pdf", configuration=config, options=options)

        filename = "Holomorphe\\Annee_" + annee + "\\Annexe__T_E_R___T_D_F_E_L_S_D\\Annexe__T_E_R___T_D_F_E_L_S_D.pdf"

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
