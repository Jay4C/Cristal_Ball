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

annee = "Annee_2021"

location = (
    "A:\\1_Professionnel\\1_Holomorphe\\1_Administration\\1_Comptabilite_Fiscalite"
    "\\2_Annee_2021\\Consolidation_Comptable_Fiscale_2021.xls"
)

# finally, write "output" to a real file
exercice = "2_Exercice_01_01_2021__31_12_2021"


class RapportsDeGestionHolomorphe(unittest.TestCase):
    # ok
    def test_livre_inventaire(self):
        print("test_livre_inventaire")

        workbook = xlrd.open_workbook(location)

        sheet = workbook.sheet_by_name("Livre_Inventaire")

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

        # Report
        body = '<!doctype html>' + \
               '<html lang="en">' + \
               '<head>' + \
               '<meta charset="utf-8">' + \
               '<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">' + \
               '<link rel="stylesheet" ' \
               'href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css" ' \
               'integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" ' \
               'crossorigin="anonymous">' + \
               '<title>Livre_Inventaire</title>' + \
               '</head>' + \
               '<body>' + \
               '<div class="container">' + \
               '<div class="card text-center">' + \
               '<div class="card-header text-center">Livre d' + "'inventaire</div>" + \
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
               '<th scope="col" colspan="5">Livre d' + "'inventaire</th>" + \
               '</tr>' + \
               '<tr>' + \
               '<th scope="col">Date de l' + "'inventaire</th>"

        excel_date_1 = round(float(str(workbook.sheet_by_name("Informations_Entreprise")
                                       .cell_value(9, 1)).split(".")[0]))

        python_date = xlrd.xldate_as_tuple(excel_date_1, 0)

        x = datetime.datetime(python_date[0], python_date[1], python_date[2])

        clos_le = x.strftime("%d/%m/%Y")

        date_inventaire = x.strftime("%d/%m/%Y")

        body += '<th scope="col" colspan="4"><i>' + date_inventaire + '</i></th>' + \
                '</tr>' + \
                '<tr>' + \
                '<th scope="col">Total [€]</th>' + \
                '<th scope="col" colspan="4"><i>' + str(round(float(sheet.cell_value(2, 1)), 2)) + '</i></th>' + \
                '</tr>' + \
                '<tr>' + \
                '<th scope="col">Désignation des articles</th>' + \
                '<th scope="col">Référence</th>' + \
                '<th scope="col">Quantité</th>' + \
                '<th scope="col">Prix unitaire [€]</th>' + \
                '<th scope="col">Prix total [€]</th>' + \
                '</tr>' + \
                '</thead>' + \
                '<tbody>'

        nb_r = 7

        for i in range(4, nb_r):
            try:
                if str(sheet.cell_value(i, 0)) != '':
                    body += '<tr>' + \
                            '<td>' + str(sheet.cell_value(i, 0)) + '</td>' + \
                            '<td>' + str(sheet.cell_value(i, 1)) + '</td>' + \
                            '<td>' + str(round(float(sheet.cell_value(i, 2)), 2)) + '</td>' + \
                            '<td>' + str(round(float(sheet.cell_value(i, 3)), 2)) + '</td>' + \
                            '<td>' + str(round(float(sheet.cell_value(i, 4)), 2)) + '</td>' + \
                            '</tr>'

            except Exception as e:
                print("error 1 : " + str(e))
                break

        body += '</tbody>' + \
                '</table>' + \
                '<br>' + \
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
            'header-right': 'Société HOLOMORPHE [SIREN : 883 632 556]',
            'header-left': 'Exercice clos le ' + clos_le,
            'footer-left': 'Livre d' + "'inventaire de \n l'exercice " + str(round(float(str(workbook.sheet_by_name("Informations_Entreprise").cell_value(8, 1)).split(".")[0]))),
            'footer-right': '[page] sur [topage]'
        }

        path_wkthmltopdf = "C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe"

        config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)

        pdfkit.from_string(
            body,
            "Livre_Inventaire\\Holomorphe\\" + annee + "\\Livre_Inventaire.pdf",
            configuration=config,
            options=options
        )

        filename = "Livre_Inventaire\\Holomorphe\\" + annee + "\\Livre_Inventaire.pdf"

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

        output = PdfFileWriter()

        # Inventaire
        inventaire_folder = "Livre_Inventaire\\Holomorphe\\" + annee

        inventaire_folder_files = os.listdir(inventaire_folder)

        inventaire_filename = ""

        for f in inventaire_folder_files:
            if "signed" in f:
                inventaire_filename += f
                print("inventaire_filename : " + inventaire_filename)

        inventaire = inventaire_folder + "\\" + inventaire_filename

        inventaire_pdf = PdfFileReader(open(inventaire, "rb"))

        for i in range(0, inventaire_pdf.getNumPages()):
            output.addPage(inventaire_pdf.getPage(i))

        output_stream = open(
            "A:\\1_Professionnel\\1_Holomorphe\\1_Administration\\2_Gestion_Declarations_Administratives"
            "\\1_Recurrentes\\5_Infogreffe\\4_Approbation_Comptes_Sociaux\\"
            + exercice + "\\Inventaire_" + annee + "_HOLOMORPHE.pdf",
            "wb")
        output.write(output_stream)
        output_stream.close()

    # ok
    def test_rapport_de_gestion(self):
        print("test_rapport_de_gestion")

        workbook = xlrd.open_workbook(location)

        sheet = workbook.sheet_by_name("Rapport_De_Gestion")

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

        excel_date_1 = round(float(str(workbook.sheet_by_name("Informations_Entreprise").cell_value(9, 1)).split(".")[0]))

        python_date = xlrd.xldate_as_tuple(excel_date_1, 0)

        x = datetime.datetime(python_date[0], python_date[1], python_date[2])

        clos_le = x.strftime("%d/%m/%Y")

        # Report
        body = '<!doctype html>' + \
               '<html lang="en">' + \
               '<head>' + \
               '<meta charset="utf-8">' + \
               '<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">' + \
               '<link rel="stylesheet" ' \
               'href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css" ' \
               'integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" ' \
               'crossorigin="anonymous">' + \
               '<title>Rapport de gestion</title>' + \
               '</head>' + \
               '<body>' + \
               '<div class="container">' + \
               '<div class="card text-center">' + \
               '<div class="card-header text-center">Rapport de gestion</div>' + \
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
                '<h6>' + 'Mesdames, Messieurs,' + '</h6>' + \
                '<br>' + \
                '<h6>' + 'Vu les articles L123-12 à L123-24 du Code de commerce,' + '</h6>' + \
                '<h6>' + 'Vu les articles L232-1 à L232-26 du Code de commerce,' + '</h6>' + \
                '<h6>' + 'Vu les articles L244-1 à L244-4 du Code de commerce,' + '</h6>' + \
                '<h6>' + 'Vu la Loi n° 2018-727 du 10 août 2018 pour un Etat au service d' + "'une société de confiance," + '</h6>' + \
                '<h6>' + 'Vu les articles L441-6-1 et D441-4 du Code de commerce,' + '</h6>' + \
                '<h6>' + 'Vu les articles L441-6-1 et D441-4 du Code de commerce,' + '</h6>' + \
                '<h6>' + 'Vu les articles L441-1 à L441-16 du Code de commerce,' + '</h6>' + \
               '<br>' + \
               '<h6>' + 'J' + "'ai l'honneur de présenter mon rapport de gestion sur les opérations de l’exercice clos le " + \
               clos_le + ', ainsi que sur les comptes annuels (bilan, compte de résultat et annexes) dudit exercice soumis aujourd' + \
               "'hui avec mon approbation.</h6>" + \
               '<br>' + \
               '<br>' + \
               '<h4><b>Présentation des états financiers et activité de la société au cours de l’exercice</b></h4>' + \
               '<br>' + \
                "<h6>Je précise que les états financiers qui sont présentés ne comportent aucune " \
                "modification, en ce qui concerne la présentation des comptes et les méthodes d’évaluation, " \
                "par rapport à l’exercice précédent. Les comptes annuels que je soumets avec mon approbation ont " \
                "été établis conformément aux règles de présentation et aux méthodes d'évaluation prévues par la " \
                "réglementation en vigueur par l'Autorité des normes comptables en vertu de l'ordonnance n° 2009-79 " \
                "du 22 janvier 2009 créant l'Autorité des normes comptables et du décret n° 2010-56 du 15 janvier " \
                "2010 relatif à l'Autorité des normes comptables." \
                "</h6>" + \
                "<h6>Au cours de cet exercice, la société a réalisé un chiffre d'affaires hors taxes s'élevant en " \
                "euros à : " + str(round(float(sheet.cell_value(19, 0)), 2)) + "</h6>" + \
                '<br>' + \
                "<h6>Ce chiffre d'affaires hors taxes est constitué de :</h6>" + \
                '<table class="table table-bordered">' + \
                '<tbody>' + \
                '<tr>' + \
                '<td>Ventes de marchandises [€]</td>' + \
                '<td>' + str(round(float(sheet.cell_value(21, 5)), 2)) + '</td>' + \
                '</tr>' + \
                '<tr>' + \
                '<td>Autres prestations facturées (prestations de services informatique) [€]</td>' + \
                '<td>' + str(round(float(sheet.cell_value(22, 5)), 2)) + '</td>' + \
                '</tr>' + \
                '<tr>' + \
                "<td>Les autres produits d'exploitation [€]</td>" + \
                '<td>' + str(round(float(sheet.cell_value(23, 5)), 2)) + '</td>' + \
                '</tr>' + \
                '</tbody>' + \
                '</table>' + \
                '<br>' + \
                "<h6>En ce qui concerne les charges d'exploitation, elles se décomposent comme suit : </h6>" + \
               '<table class="table table-bordered">' + \
               '<tbody>' + \
               '<tr>' + \
               '<td>Achats [€]</td>' + \
               '<td>' + str(round(float(sheet.cell_value(25, 5)), 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>Autres charges relatives à des prestations externes [€]</td>' + \
               '<td>' + str(round(float(sheet.cell_value(26, 5)), 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               "<td>Charges de personnel [€]</td>" + \
               '<td>' + str(round(float(sheet.cell_value(27, 5)), 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               "<td>Dotation aux amortissements [€]</td>" + \
               '<td>' + str(round(float(sheet.cell_value(28, 5)), 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               "<td>Impôts et taxes [€]</td>" + \
               '<td>' + str(round(float(sheet.cell_value(29, 5)), 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               "<td>Dotation aux provisions [€]</td>" + \
               '<td>' + str(round(float(sheet.cell_value(30, 5)), 2)) + '</td>' + \
               '</tr>' + \
               '</tbody>' + \
               '</table>' + \
               '<br>' + \
               "<h6>Il en résulte que le résultat d'exploitation s'élève en euros à : " \
               + str(round(float(sheet.cell_value(32, 0)), 2)) + "</h6>" + \
               '<br>' + \
               '<h6>Ce montant est ' + str(sheet.cell_value(34, 0)) + \
               ' de ' + str(round(float(sheet.cell_value(36, 0)), 2)) + " % par rapport à celui de l'exercice précédent.</h6>" + \
               '<br>' + \
               "<h6>Cette évolution s'explique par " + str(sheet.cell_value(39, 0)) + '</h6>' + \
               "<br>" + \
               "<h6>Il résulte de ces éléments que le résultat courant avant impôt s'élève en euros à : " + \
               str(round(float(sheet.cell_value(42, 0)), 2)) + "</h6>" + \
               '<br>' + \
               "<h6>Enfin, le résultat exceptionnel s'élève en euros à : " + \
               str(round(float(sheet.cell_value(45, 0)), 2)) + \
               " dont le montant des charges exceptionnelles s'élève en euros à : " + \
               str(round(float(sheet.cell_value(47, 0)), 2)) + \
               " et le montant des produits  exceptionnels s'élève en euros à : " + \
               str(round(float(sheet.cell_value(49, 0)), 2)) + \
               "</h6>" + \
               '<br>' + \
               "<h6>Il résulte de ces éléments que le résultat net réalisé par la société au cours de cet exercice s'élève en euros à : </h6>" + \
               str(round(float(sheet.cell_value(52, 0)), 2)) + \
               "<h6>Par rapport à celui de l'exercice précédent, ce résultat est " + \
               str(sheet.cell_value(54, 0)) + " de " + str(round(float(sheet.cell_value(56, 0)), 2)) + " %. </h6>" + \
               '<br>' + \
               "<h6>L'actif immobilisé s'élève en euros à : " + str(round(float(sheet.cell_value(60, 0)), 2)) + "</h6>" + \
               "<h6>Il est constitué : </h6>" + \
               '<table class="table table-bordered">' + \
               '<tbody>' + \
               '<tr>' + \
               "<td>Immobilisations que la société possédait au début de l'exercice et dont la valeur nette comptable s'élève en euros à : </td>" + \
               '<td>' + str(round(float(sheet.cell_value(62, 5)), 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               "<td>Immobilisations qui ont été acquises en cours d'exercice pour un montant en euros à : </td>" + \
               '<td>' + str(round(float(sheet.cell_value(63, 5)), 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '</tbody>' + \
               '</table>' + \
               '<br>' + \
               "<h6>L'actif circulant s'élève en euros à : " + str(round(float(sheet.cell_value(66, 0)), 2)) + "</h6>" + \
               "<h6>En ce qui concerne l'évolution du passif, il convient d'indiquer que : </h6>" + \
               "<h6>1) Après prise en compte du résultat, les fonds propres se décomposent ainsi : </h6>" + \
               '<table class="table table-bordered">' + \
               '<thead>' + \
               '<tr>' + \
               '<th scope="col">Poste</th>' + \
               '<th scope="col">Exercice 2021</th>' + \
               '<th scope="col">Exercice 2020</th>' + \
               '<th scope="col">Évolution au cours de  l' + "'exercice 2021 par rapport à l'exercice 2020</th>" + \
               '</tr>' + \
               '</thead>' + \
               '<tbody>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(71, 0)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(71, 2), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(71, 4), 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(71, 7)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(72, 0)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(72, 2), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(72, 4), 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(72, 7)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(73, 0)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(73, 2), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(73, 4), 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(73, 7)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(74, 0)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(74, 2), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(74, 4), 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(74, 7)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(75, 0)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(75, 2), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(75, 4), 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(75, 7)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(76, 0)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(76, 2), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(76, 4), 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(76, 7)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(77, 0)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(77, 2), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(77, 4), 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(77, 7)) + '</td>' + \
               '</tr>' + \
               '</tbody>' + \
               '</table>' + \
               "<h6>2) En ce qui concerne les autres postes du passif, ils se décomposent comme suit : </h6>" + \
               '<table class="table table-bordered">' + \
               '<thead>' + \
               '<tr>' + \
               '<th scope="col">Poste</th>' + \
               '<th scope="col">Exercice 2021</th>' + \
               '<th scope="col">Exercice 2020</th>' + \
               '<th scope="col">Évolution au cours de  l' + "'exercice 2021 par rapport à l'exercice 2020</th>" + \
               '</tr>' + \
               '</thead>' + \
               '<tbody>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(80, 0)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(80, 2), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(80, 4), 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(80, 7)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(81, 0)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(81, 2), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(81, 4), 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(81, 7)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(82, 0)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(82, 2), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(82, 4), 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(82, 7)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(83, 0)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(83, 2), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(83, 4), 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(83, 7)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(84, 0)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(84, 2), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(84, 4), 2)) + '</td>' + \
               '<td>' + str(sheet.cell_value(84, 7)) + '</td>' + \
               '</tr>' + \
               '</tbody>' + \
               '</table>' + \
               '<br>' + \
               "<h6>Conformément aux articles L. 441-6-1 et D. 441-4 du Code de commerce, j'informe qu’à " \
               "la clôture de l’exercice, les dettes fournisseurs et clients échues se présentent comme suit.</h6>" + \
               '<table class="table table-bordered">' + \
               '<thead>' + \
               '<tr>' + \
               '<th scope="col">Réglementation</th>' + \
               '<th scope="col" colspan="6">Article D.441 I. 1° : Factures reçues non réglées à la date de clôture de l' + "exercice dont le terme est échu</th>" + \
               '</tr>' + \
               '<tr>' + \
               '<th scope="col">Délais</th>' + \
               '<th scope="col">0 jour</th>' + \
               '<th scope="col">1 à 30 jours</th>' + \
               '<th scope="col">31 à 60 jours</th>' + \
               '<th scope="col">61 à 90 jours</th>' + \
               '<th scope="col">91 et plus jours</th>' + \
               '<th scope="col">Total</th>' + \
               '</tr>' + \
               '</thead>' + \
               '<tbody>' + \
               '<tr>' + \
               '<td colspan="7">' + str(sheet.cell_value(89, 0)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(90, 0)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(90, 1), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(90, 2), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(90, 3), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(90, 4), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(90, 5), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(90, 6), 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(91, 0)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(91, 1), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(91, 2), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(91, 3), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(91, 4), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(91, 5), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(91, 6), 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(92, 0)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(92, 1), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(92, 2), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(92, 3), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(92, 4), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(92, 5), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(92, 6), 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(93, 0)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(93, 1), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(93, 2), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(93, 3), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(93, 4), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(93, 5), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(93, 6), 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="7">' + str(sheet.cell_value(94, 0)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(95, 0)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(95, 1), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(95, 2), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(95, 3), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(95, 4), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(95, 5), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(95, 6), 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td>' + str(sheet.cell_value(96, 0)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(96, 1), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(96, 2), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(96, 3), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(96, 4), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(96, 5), 2)) + '</td>' + \
               '<td>' + str(round(sheet.cell_value(96, 6), 2)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="7">' + str(sheet.cell_value(97, 0)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="3">' + str(sheet.cell_value(98, 0)) + '</td>' + \
               '<td colspan="4">' + str(sheet.cell_value(98, 3)) + '</td>' + \
               '</tr>' + \
               '<tr>' + \
               '<td colspan="7">Délais légaux : 30 Jours.</td>' + \
               '</tr>' + \
               '</tbody>' + \
               '</table>' + \
                "<br>" + \
                '<table class="table table-bordered">' + \
                '<thead>' + \
                '<tr>' + \
                '<th scope="col">Réglementation</th>' + \
                '<th scope="col" colspan="6">Article D.441 I. 1° : Factures émises non réglées à la date de clôture de l' + "'exercice dont le terme est échu</th>" + \
                '</tr>' + \
                '<tr>' + \
                '<th scope="col">Délais</th>' + \
                '<th scope="col">0 jour</th>' + \
                '<th scope="col">1 à 30 jours</th>' + \
                '<th scope="col">31 à 60 jours</th>' + \
                '<th scope="col">61 à 90 jours</th>' + \
                '<th scope="col">91 et plus jours</th>' + \
                '<th scope="col">Total</th>' + \
                '</tr>' + \
                '</thead>' + \
                '<tbody>' + \
                '<tr>' + \
                '<td colspan="7">(A) Tranches de retard de paiement</td>' + \
                '</tr>' + \
                '<tr>' + \
                '<td>' + str(sheet.cell_value(104, 0)) + '</td>' + \
                '<td>' + str(round(sheet.cell_value(104, 1), 2)) + '</td>' + \
                '<td>' + str(round(sheet.cell_value(104, 2), 2)) + '</td>' + \
                '<td>' + str(round(sheet.cell_value(104, 3), 2)) + '</td>' + \
                '<td>' + str(round(sheet.cell_value(104, 4), 2)) + '</td>' + \
                '<td>' + str(round(sheet.cell_value(104, 5), 2)) + '</td>' + \
                '<td>' + str(round(sheet.cell_value(104, 6), 2)) + '</td>' + \
                '</tr>' + \
                '<tr>' + \
                '<td>' + str(sheet.cell_value(105, 0)) + '</td>' + \
                '<td>' + str(round(sheet.cell_value(105, 1), 2)) + '</td>' + \
                '<td>' + str(round(sheet.cell_value(105, 2), 2)) + '</td>' + \
                '<td>' + str(round(sheet.cell_value(105, 3), 2)) + '</td>' + \
                '<td>' + str(round(sheet.cell_value(105, 4), 2)) + '</td>' + \
                '<td>' + str(round(sheet.cell_value(105, 5), 2)) + '</td>' + \
                '<td>' + str(round(sheet.cell_value(105, 6), 2)) + '</td>' + \
                '</tr>' + \
                '<tr>' + \
                '<td>' + str(sheet.cell_value(106, 0)) + '</td>' + \
                '<td>' + str(round(sheet.cell_value(106, 1), 2)) + '</td>' + \
                '<td>' + str(round(sheet.cell_value(106, 2), 2)) + '</td>' + \
                '<td>' + str(round(sheet.cell_value(106, 3), 2)) + '</td>' + \
                '<td>' + str(round(sheet.cell_value(106, 4), 2)) + '</td>' + \
                '<td>' + str(round(sheet.cell_value(106, 5), 2)) + '</td>' + \
                '<td>' + str(round(sheet.cell_value(106, 6), 2)) + '</td>' + \
                '</tr>' + \
                '<tr>' + \
                '<td>' + str(sheet.cell_value(107, 0)) + '</td>' + \
                '<td>' + str(round(sheet.cell_value(107, 1), 2)) + '</td>' + \
                '<td>' + str(round(sheet.cell_value(107, 2), 2)) + '</td>' + \
                '<td>' + str(round(sheet.cell_value(107, 3), 2)) + '</td>' + \
                '<td>' + str(round(sheet.cell_value(107, 4), 2)) + '</td>' + \
                '<td>' + str(round(sheet.cell_value(107, 5), 2)) + '</td>' + \
                '<td>' + str(round(sheet.cell_value(107, 6), 2)) + '</td>' + \
                '</tr>' + \
                '<tr>' + \
                '<td colspan="7">(B) Factures exclues du (A) relatives à des dettes et créances litigieuses ' \
                'ou non comptabilisées</td>' + \
                '</tr>' + \
                '<tr>' + \
                '<td>' + str(sheet.cell_value(109, 0)) + '</td>' + \
                '<td>' + str(round(sheet.cell_value(109, 1), 2)) + '</td>' + \
                '<td>' + str(round(sheet.cell_value(109, 2), 2)) + '</td>' + \
                '<td>' + str(round(sheet.cell_value(109, 3), 2)) + '</td>' + \
                '<td>' + str(round(sheet.cell_value(109, 4), 2)) + '</td>' + \
                '<td>' + str(round(sheet.cell_value(109, 5), 2)) + '</td>' + \
                '<td>' + str(round(sheet.cell_value(109, 6), 2)) + '</td>' + \
                '</tr>' + \
                '<tr>' + \
                '<td>' + str(sheet.cell_value(110, 0)) + '</td>' + \
                '<td>' + str(round(sheet.cell_value(110, 1), 2)) + '</td>' + \
                '<td>' + str(round(sheet.cell_value(110, 2), 2)) + '</td>' + \
                '<td>' + str(round(sheet.cell_value(110, 3), 2)) + '</td>' + \
                '<td>' + str(round(sheet.cell_value(110, 4), 2)) + '</td>' + \
                '<td>' + str(round(sheet.cell_value(110, 5), 2)) + '</td>' + \
                '<td>' + str(round(sheet.cell_value(110, 6), 2)) + '</td>' + \
                '</tr>' + \
                '<tr>' + \
                '<td colspan="7">(C) Délais de paiement de référence utilisés (Contractuel ou délai légal - ' \
                'article L441-6 ou article L443-1 du Code de commerce)</td>' + \
                '</tr>' + \
                '<tr>' + \
                '<td colspan="3">' + str(sheet.cell_value(112, 0)) + '</td>' + \
                '<td colspan="4">' + str(sheet.cell_value(112, 3)) + '</td>' + \
                '</tr>' + \
                '<tr>' + \
                '<td colspan="7">Délais légaux : 30 Jours.</td>' + \
                '</tr>' + \
                '</tbody>' + \
                '</table>' + \
                '<br>' + \
                '<br>' + \
                "<h4><b>Evolution prévisible et perspectives d'avenir</b></h4>" + \
                '<br>' + \
                '<h6>Pour l' + "'exercice à venir, je prévois une " + str(sheet.cell_value(117, 0)) + \
                " du chiffre d’affaires de l'ordre de " + \
                str(round(float(sheet.cell_value(119, 0)), 2)) + " euros à un taux de progression de " + \
                str(round(float(sheet.cell_value(121, 0)), 2)) + " % par rapport à l'exercice précédent.</h6>" + \
                "<br>" + \
                "<br>" + \
                "<h4><b>Evénements importants survenus depuis la clôture de l'exercice</b></h4>" + \
                "<br>" + \
                '<h6>' + str(sheet.cell_value(125, 0)) + '</h6>' + \
                '<br>' + \
                '<br>' + \
                "<h4><b>Activités de recherche et développement</b></h4>" + \
                '<br>' + \
                '<h6>' + str(sheet.cell_value(128, 0)) + '</h6>' + \
                '<br>' + \
                '<br>' + \
                "<h4><b>Prise de participations</b></h4>" + \
                '<br>' + \
                '<h6>' + str(sheet.cell_value(131, 0)) + '</h6>' + \
                '<br>' + \
                '<br>' + \
                "<h4><b>Filiales et participations</b></h4>" + \
                '<br>' + \
                '<h6>' + str(sheet.cell_value(134, 0)) + '</h6>' + \
                '<br>' + \
                '<br>' + \
                "<h4><b>Proposition d’affectation du résultat</b></h4>" + \
                '<br>' + \
                '<h6>' + str(sheet.cell_value(137, 0)) + '</h6>'

        dividende = "non"

        if dividende == "oui":
            body += '<br>' + \
                    '<br>' + \
                    "<h4><b>Dividendes antérieurement distribués</b></h4>" + \
                    '<br>' + \
                    '<h6>' + str(sheet.cell_value(140, 0)) + '</h6>' + \
                    '<br>' + \
                    '<table class="table table-bordered">' + \
                    '<tbody>' + \
                    '<tr>' + \
                    '<td>' + str(sheet.cell_value(141, 0)) + '</td>' + \
                    '<td>' + str(sheet.cell_value(141, 1)) + '</td>' + \
                    '<td>' + str(sheet.cell_value(141, 2)) + '</td>' + \
                    '<td>' + str(sheet.cell_value(141, 3)) + '</td>' + \
                    '<td>' + str(sheet.cell_value(141, 4)) + '</td>' + \
                    '<td>' + str(sheet.cell_value(141, 5)) + '</td>' + \
                    '</tr>' + \
                    '<tr>' + \
                    '<td>' + str(sheet.cell_value(142, 0)) + '</td>' + \
                    '<td>' + str(sheet.cell_value(142, 1)) + '</td>' + \
                    '<td>' + str(sheet.cell_value(142, 2)) + '</td>' + \
                    '<td>' + str(sheet.cell_value(142, 3)) + '</td>' + \
                    '<td>' + str(sheet.cell_value(142, 4)) + '</td>' + \
                    '<td>' + str(sheet.cell_value(142, 5)) + '</td>' + \
                    '</tr>' + \
                    '<tr>' + \
                    '<td>' + str(sheet.cell_value(143, 0)) + '</td>' + \
                    '<td>' + str(sheet.cell_value(143, 1)) + '</td>' + \
                    '<td>' + str(sheet.cell_value(143, 2)) + '</td>' + \
                    '<td>' + str(sheet.cell_value(143, 3)) + '</td>' + \
                    '<td>' + str(sheet.cell_value(143, 4)) + '</td>' + \
                    '<td>' + str(sheet.cell_value(143, 5)) + '</td>' + \
                    '</tr>' + \
                    '</tbody>' + \
                    '</table>'
        else:
            body += '<br>' + \
                    '<br>' + \
                    "<h4><b>Dividendes antérieurement distribués</b></h4>" + \
                    '<br>' + \
                    '<h6>' + str(sheet.cell_value(144, 0)) + '</h6>'

        body += '<br>' + \
                '<br>' + \
                "<h4><b>Dépenses non déductibles fiscalement</b></h4>" + \
                '<br>' + \
                '<h6>' + str(sheet.cell_value(147, 0)) + '</h6>' + \
                '<br>' + \
                '<br>' + \
                "<h4><b>Résolutions proposées et conventions réglementées</b></h4>" + \
                '<br>' + \
                '<h6>' + str(sheet.cell_value(150, 0)) + '</h6>' + \
                '<br>' + \
                '<br>' + \
                "<h4><b>Conclusion</b></h4>" + \
                '<br>' + \
                '<h6>' + str(sheet.cell_value(153, 0)) + '</h6>'

        body += '<br>' + \
                '<br>' + \
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
            'header-right': 'Société HOLOMORPHE [SIREN : 883 632 556]',
            'header-left': 'Exercice clos le ' + clos_le,
            'footer-left': "Rapport de gestion \n de l'exercice " + str(round(float(str(workbook.sheet_by_name("Informations_Entreprise").cell_value(8, 1)).split(".")[0]))),
            'footer-right': '[page] sur [topage]'
        }

        path_wkthmltopdf = "C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe"

        config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)

        pdfkit.from_string(
            body,
            "Rapport_Gestion\\Holomorphe\\" + annee + "\\Rapport_Gestion.pdf",
            configuration=config,
            options=options
        )

        filename = "Rapport_Gestion\\Holomorphe\\" + annee + "\\Rapport_Gestion.pdf"

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

        output = PdfFileWriter()

        # Rapport de gestion
        rapport_de_gestion_folder = "Rapport_Gestion\\Holomorphe\\" + annee

        rapport_de_gestion_folder_files = os.listdir(rapport_de_gestion_folder)

        rapport_de_gestion_filename = ""

        for f in rapport_de_gestion_folder_files:
            if "signed" in f:
                rapport_de_gestion_filename += f
                print("rapport_de_gestion_filename : " + rapport_de_gestion_filename)

        rapport_de_gestion = rapport_de_gestion_folder + "\\" + rapport_de_gestion_filename

        rapport_de_gestion_pdf = PdfFileReader(open(rapport_de_gestion, "rb"))

        for i in range(0, rapport_de_gestion_pdf.getNumPages()):
            output.addPage(rapport_de_gestion_pdf.getPage(i))

        output_stream = open(
            "A:\\1_Professionnel\\1_Holomorphe\\1_Administration\\2_Gestion_Declarations_Administratives"
            "\\1_Recurrentes\\5_Infogreffe\\4_Approbation_Comptes_Sociaux\\"
            + exercice + "\\Rapport_Gestion_" + annee + "_HOLOMORPHE.pdf",
            "wb")
        output.write(output_stream)
        output_stream.close()


if __name__ == '__main__':
    unittest.main()
