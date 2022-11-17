import unittest
import pdfkit
from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from datetime import datetime


class TVA(unittest.TestCase):
    def test_convert_html_to_pdf_from_url(self):
        print("test_convert_html_to_pdf")
        path_wkthmltopdf = "C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe"
        config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
        pdfkit.from_url("https://holomorphe.com/", "out.pdf", configuration=config)

    def test_convert_html_to_pdf_from_plain_html_body(self):
        print("test_convert_html_to_pdf_from_plain_html_body")

        body = """
        <!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css" integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">

    <title>Hello, world!</title>
  </head>
  <body>
    <div class="card">
      <h5 class="card-header">Featured</h5>
      <div class="card-body">
        <h5 class="card-title">Special title treatment</h5>
        <p class="card-text">With supporting text below as a natural lead-in to additional content.</p>
        <a href="#" class="btn btn-primary">Go somewhere</a>
      </div>
    </div>

    <!-- Optional JavaScript; choose one of the two! -->

    <!-- Option 1: jQuery and Bootstrap Bundle (includes Popper) -->
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ho+j7jyWK8fNQe+A12Hb8AhRq26LrZ/JpcUGGOn+Y7RsweNrtN/tE3MoK7ZeZDyx" crossorigin="anonymous"></script>

    <!-- Option 2: jQuery, Popper.js, and Bootstrap JS
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js" integrity="sha384-9/reFTGAW83EW2RDu2S0VKaIzap3H66lZH81PoYlFhbGU+6BZp6G7niu735Sk7lN" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/js/bootstrap.min.js" integrity="sha384-w1Q4orYjBQndcko6MimVbzY0tgp4pWB4lZ7lr30WKz0vr/aWKhXdBNmNb5D92v7s" crossorigin="anonymous"></script>
    -->
  </body>
</html>
        """

        options = {
            'page-size': 'A4'
        }
        path_wkthmltopdf = "C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe"
        config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
        pdfkit.from_string(body, "out.pdf", configuration=config, options=options)

    def test_formulaire_3310_ca3_1_rempli_date_signe(self):
        case_0005 = "Oui"
        case_0010 = "Oui"
        paiement_par_virement_bancaire = "Oui"
        paiement_imputation = "Oui"

        today = datetime.today().strftime('%d/%m/%Y')

        packet = io.BytesIO()

        # create a new PDF with Reportlab
        can = canvas.Canvas(packet, pagesize=letter)
        can.setFontSize(9)

        # Insérer le jour de début de la période de déclaration
        can.drawString(147, 749, "01")

        # Insérer le mois de début de la période de déclaration
        can.drawString(168, 749, "01")

        # Insérer l'année de début de la période de déclaration
        can.drawString(187, 749, "2020")

        # Insérer le jour de fin de la période de déclaration
        can.drawString(217.44, 749, "31")

        # Insérer le mois de fin de la période de déclaration
        can.drawString(238.32, 749, "01")

        # Insérer l'année de fin de la période de déclaration
        can.drawString(257.04, 749, "2020")

        # inserer la dénomination
        can.drawString(280, 660, "HOLOMORPHE")

        # insérer l'adresse du siège social
        can.drawString(280, 620, "31 Avenue de Ségur 75007 Paris")

        # insérer le SIE
        can.drawString(16, 556, "SIE")

        # insérer le Numéro de dossier
        can.drawString(85, 556, "11111")

        # insérer le Clé
        can.drawString(168.5, 556, "Clé")

        # insérer le Période
        can.drawString(200, 556, "Période")

        # insérer le CM
        can.drawString(276.5, 556, "CM")

        # insérer le OPT
        can.drawString(302.5, 556, "OP")

        # insérer le Code service
        can.drawString(325, 556, "123")

        # insérer le Régime
        can.drawString(379.5, 556, "1234")

        # Insérer le 1er chiffre du N° d'identification de l'établissement (SIRET)
        can.drawString(242.7, 533.6, "1")

        # Insérer le 2eme chiffre du N° d'identification de l'établissement (SIRET)
        can.drawString(254.88, 533.6, "1")

        # Insérer le 3eme chiffre du N° d'identification de l'établissement (SIRET)
        can.drawString(265.68, 533.6, "1")

        # Insérer le 4eme chiffre du N° d'identification de l'établissement (SIRET)
        can.drawString(277.2, 533.6, "1")

        # Insérer le 5eme chiffre du N° d'identification de l'établissement (SIRET)
        can.drawString(288.72, 533.6, "1")

        # Insérer le 6eme chiffre du N° d'identification de l'établissement (SIRET)
        can.drawString(298.8, 533.6, "1")

        # Insérer le 7eme chiffre du N° d'identification de l'établissement (SIRET)
        can.drawString(310.32, 533.6, "1")

        # Insérer le 8eme chiffre du N° d'identification de l'établissement (SIRET)
        can.drawString(321.12, 533.6, "1")

        # Insérer le 9eme chiffre du N° d'identification de l'établissement (SIRET)
        can.drawString(333.36, 533.6, "1")

        # Insérer le 10eme chiffre du N° d'identification de l'établissement (SIRET)
        can.drawString(344.16, 533.6, "1")

        # Insérer le 11eme chiffre du N° d'identification de l'établissement (SIRET)
        can.drawString(363.6, 533.6, "1")

        # Insérer le 12eme chiffre du N° d'identification de l'établissement (SIRET)
        can.drawString(372.96, 533.6, "1")

        # Insérer le 13eme chiffre du N° d'identification de l'établissement (SIRET)
        can.drawString(385.2, 533.6, "1")

        # Insérer le 14eme chiffre du N° d'identification de l'établissement (SIRET)
        can.drawString(396, 533.6, "1")

        # Insérer le 15eme chiffre du N° d'identification de l'établissement (SIRET)
        can.drawString(408.24, 533.6, "1")

        # Insérer le 1er chiffre du N° de TVA intracommunautaire (ne concerne pas les DOM)
        can.drawString(244.08, 517, "1")

        # Insérer le 2eme chiffre du N° de TVA intracommunautaire (ne concerne pas les DOM)
        can.drawString(256.32, 517, "1")

        # Insérer le 3eme chiffre du N° de TVA intracommunautaire (ne concerne pas les DOM)
        can.drawString(275.76, 517, "1")

        # Insérer le 4eme chiffre du N° de TVA intracommunautaire (ne concerne pas les DOM)
        can.drawString(288, 517, "1")

        # Insérer le 5eme chiffre du N° de TVA intracommunautaire (ne concerne pas les DOM)
        can.drawString(306.72, 517, "1")

        # Insérer le 6eme chiffre du N° de TVA intracommunautaire (ne concerne pas les DOM)
        can.drawString(317.52, 517, "1")

        # Insérer le 7eme chiffre du N° de TVA intracommunautaire (ne concerne pas les DOM)
        can.drawString(329.04, 517, "1")

        # Insérer le 8eme chiffre du N° de TVA intracommunautaire (ne concerne pas les DOM)
        can.drawString(338.4, 517, "1")

        # Insérer le 9eme chiffre du N° de TVA intracommunautaire (ne concerne pas les DOM)
        can.drawString(349.92, 517, "1")

        # Insérer le 10eme chiffre du N° de TVA intracommunautaire (ne concerne pas les DOM)
        can.drawString(360, 517, "1")

        # Insérer le 11eme chiffre du N° de TVA intracommunautaire (ne concerne pas les DOM)
        can.drawString(373.68, 517, "1")

        # Insérer le 12eme chiffre du N° de TVA intracommunautaire (ne concerne pas les DOM)
        can.drawString(382.32, 517, "1")

        # Insérer le 13eme chiffre du N° de TVA intracommunautaire (ne concerne pas les DOM)
        can.drawString(393.12, 517, "1")

        # Insérer le 14eme chiffre du N° de TVA intracommunautaire (ne concerne pas les DOM)
        can.drawString(404.64, 517, "1")

        # Cocher la case 0005
        if case_0005 == "Oui":
            can.drawString(553, 485, "X")

        # Cocher la case 0010
        if case_0010 == "Oui":
            can.drawString(553, 460, "X")

        # Insérer la date de signature
        can.drawString(44, 418, today)

        # Insérer le téléphone
        can.drawString(61.3, 403, "0751046125")

        # Cocher le paiement par virement bancaire
        if paiement_par_virement_bancaire == "Oui":
            can.drawString(193.68, 373, "X")

        # Cocher le paiement par imputation
        if paiement_imputation == "Oui":
            can.drawString(193.68, 358, "X")

        # Insérer une image pour la signature de 
        can.drawString(138, 405, "")

        can.save()

        # move to the beginning of the StringIO buffer
        packet.seek(0)
        new_pdf = PdfFileReader(packet)

        # read your existing PDF
        existing_pdf = PdfFileReader(open("TVA/Formulaire_3310_CA3/Formulaire_3310_CA3_1.pdf", "rb"))

        output = PdfFileWriter()

        # add the "watermark" (which is the new pdf) on the existing page
        page = existing_pdf.getPage(0)
        page.mergePage(new_pdf.getPage(0))
        output.addPage(page)

        # finally, write "output" to a real file
        output_stream = open("Formulaire_3310_CA3/Formulaire_3310_CA3_1_"
                             + datetime.today().strftime('%d_%m_%Y') + ".pdf", "wb")
        output.write(output_stream)
        output_stream.close()

    def test_formulaire_3310_ca3_2_rempli(self):
        packet = io.BytesIO()

        # create a new PDF with Reportlab
        can = canvas.Canvas(packet, pagesize=letter)
        can.setFontSize(8)

        # Insérer la valeur du numéro 01
        can.drawString(238, 792, "1000000000,00")

        # Insérer la valeur du numéro 02
        can.drawString(238, 779, "1000000000,00")

        # Insérer la valeur du numéro 2A
        can.drawString(238, 757, "1000000000,00")

        # Insérer la valeur du numéro 2B
        can.drawString(238, 727, "1000000000,00")

        # Insérer la valeur du numéro 03
        can.drawString(238, 710, "1000000000,00")

        # Insérer la valeur du numéro 3A
        can.drawString(238, 688, "1000000000,00")

        # Insérer la valeur du numéro 3B
        can.drawString(238, 662, "1000000000,00")

        # Insérer la valeur du numéro 3C
        can.drawString(238, 641, "1000000000,00")

        # Insérer la valeur du numéro 04
        can.drawString(521, 792, "1000000000,00")

        # Insérer la valeur du numéro 05
        can.drawString(521, 779, "1000000000,00")

        # Insérer la valeur du numéro 5A
        can.drawString(521, 757, "1000000000,00")

        # Insérer la valeur du numéro 06
        can.drawString(521, 732, "1000000000,00")

        # Insérer la valeur du numéro 6A
        can.drawString(521, 710, "1000000000,00")

        # Insérer la valeur du numéro 07
        can.drawString(521, 688, "1000000000,00")

        # Insérer la valeur du numéro 7A
        can.drawString(521, 663, "1000000000,00")

        # Insérer la valeur du numéro 7B
        can.drawString(521, 641, "1000000000,00")

        # Insérer la valeur du numéro 08 base hors taxe
        can.drawString(459, 586, "1000000000,00")

        # Insérer la valeur du nunéro 08 taxe due
        can.drawString(520, 586, "1000000000,00")

        # Insérer la valeur du numéro 09 base hors taxe
        can.drawString(459, 573, "1000000000,00")

        # Insérer la valeur du numéro 09 taxe due
        can.drawString(520, 573, "1000000000,00")

        # Insérer la valeur du numéro 9B base hors taxe
        can.drawString(459, 559, "1000000000,00")

        # Insérer la valeur du numéro 9B taxe due
        can.drawString(520, 559, "1000000000,00")

        # Insérer la valeur du numéro 10 base hors taxe
        can.drawString(459, 532, "1000000000,00")

        # Insérer la valeur du numéro 10 taxe due
        can.drawString(520, 532, "1000000000,00")

        # Insérer la valeur du numéro 11 base hors taxe
        can.drawString(459, 519, "1000000000,00")

        # Insérer la valeur du numéro 11 taxe due
        can.drawString(520, 519, "1000000000,00")

        # Insérer la valeur du numéro 12
        can.drawString(37, 505, "Taxe réduit à 10%")

        # Insérer la valeur du numéro 12 base hors taxe
        can.drawString(459, 505, "1000000000,00")

        # Insérer la valeur du numéro 12 taxe due
        can.drawString(520, 505, "1000000000,00")

        # Insérer la valeur du numéro 13 base hors taxe
        can.drawString(459, 478, "1000000000,00")

        # Insérer la valeur du numéro 13 taxe due
        can.drawString(520, 478, "1000000000,00")

        # Insérer la valeur du numéro 14 base hors taxe
        can.drawString(459, 465, "1000000000,00")

        # Insérer la valeur du numéro 14 taxe due
        can.drawString(520, 465, "1000000000,00")

        # Insérer la valeur du numéro 15 taxe due
        can.drawString(520, 451, "1000000000,00")

        # Insérer la valeur du numéro 5B taxe due
        can.drawString(520, 438, "1000000000,00")

        # Insérer la valeur du numéro 16 taxe due
        can.drawString(520, 424, "1000000000,00")

        # Insérer la valeur du numéro 7C taxe due
        can.drawString(520, 406, "1000000000,00")

        # Insérer la valeur du numéro 17 taxe due
        can.drawString(520, 389, "1000000000,00")

        # Insérer la valeur du numéro 18 taxe due
        can.drawString(520, 376, "1000000000,00")

        # Insérer la valeur du numéro 19 taxe due
        can.drawString(520, 349, "1000000000,00")

        # Insérer la valeur du numéro 20 taxe due
        can.drawString(520, 334, "1000000000,00")

        # Insérer la valeur du numéro 21
        can.drawString(211, 313, "1000000000,00")

        # Insérer la valeur du numéro 21 taxe due
        can.drawString(520, 316, "1000000000,00")

        # Insérer la valeur du numéro 22 taxe due
        can.drawString(520, 299, "1000000000,00")

        # Insérer la valeur du numéro 2C taxe due
        can.drawString(520, 285, "1000000000,00")

        # Insérer la valeur du numéro 22A
        can.drawString(243, 263, "100")

        # Insérer la valeur du numéro 23 taxe due
        can.drawString(520, 271, "1000000000,00")

        # Insérer la valeur du numéro 24 taxe due
        can.drawString(520, 255, "1000000000,00")

        # Insérer la valeur du numéro 25
        can.drawString(238, 230, "1000000000,00")

        # Insérer la valeur du numéro 26
        can.drawString(238, 213, "1000000000,00")

        # Insérer la valeur du numério AA
        can.drawString(238, 188, "1000000000,00")

        # Insérer la valeur du numéro 27
        can.drawString(238, 154, "1000000000,00")

        # Insérer la valeur du numéro 28
        can.drawString(522, 230, "1000000000,00")

        # Insérer la valeur du numéro 29
        can.drawString(522, 213, "1000000000,00")

        # Insérer la valeur du numéro AB
        can.drawString(522, 188, "1000000000,00")

        # Insérer la valeur du numéro 32
        can.drawString(509, 138, "1000000000,00")

        can.save()

        # move to the beginning of the StringIO buffer
        packet.seek(0)
        new_pdf = PdfFileReader(packet)

        # read your existing PDF
        existing_pdf = PdfFileReader(open("TVA/Formulaire_3310_CA3/Formulaire_3310_CA3_2.pdf", "rb"))

        output = PdfFileWriter()

        # add the "watermark" (which is the new pdf) on the existing page
        page = existing_pdf.getPage(0)
        page.mergePage(new_pdf.getPage(0))
        output.addPage(page)

        # finally, write "output" to a real file
        output_stream = open("Formulaire_3310_CA3/Formulaire_3310_CA3_2_"
                             + datetime.today().strftime('%d_%m_%Y') + ".pdf", "wb")
        output.write(output_stream)
        output_stream.close()

    def test_formulaire_3310_a_1_rempli_date_signe(self):
        sans_declaration_ca3 = "non"

        packet = io.BytesIO()

        # create a new PDF with Reportlab
        can = canvas.Canvas(packet, pagesize=letter)
        can.setFontSize(8)

        # Ajouter le jour de la date de début de la période de déclaration
        can.drawString(174, 719, "01")

        # Ajouter le mois de la date de début de la période de déclaration
        can.drawString(196, 719, "01")

        # Ajouter l'année de la date de début de la période de déclaration
        can.drawString(222, 719, "2020")

        # Ajouter le jour de la date de fin de la période de déclaration
        can.drawString(264, 719, "31")

        # Ajouter le mois de la date de fin de la période de déclaration
        can.drawString(289, 719, "01")

        # Ajouter l'année de la date de fin de la période de déclaration
        can.drawString(314, 719, "2020")

        # Ajouter l'adresse de l'entreprise
        can.drawString(17, 676, "31 Avenue de Ségur 75007 Paris")

        # Ajouter le numéro de SIREN
        can.drawString(61, 642, "999999999")

        if sans_declaration_ca3 == "oui":
            # Ajouter la date si l'imprimé est souscrit sans la déclaration CA3
            can.drawString(41, 568, datetime.today().strftime('%d/%m/%Y'))

            # Ajouter le téléphone si l'imprimé est souscrit sans la déclaration CA3
            can.drawString(66, 553, "0751046125")

            # Ajouter la signature du Président si l'imprimé est souscrit sans la déclaration CA3
            can.drawString(59, 538, "")

            # Ajouter le paiement par virement bancaire si l'imprimé est souscrit sans la déclaration CA3
            can.drawString(205, 524, "X")

            # Ajouter le paiement par imputation si l'imprimé est souscrit sans la déclaration CA3
            can.drawString(205, 509, "X")

        # Ajouter la valeur 0990 base hors taxe
        can.drawString(338, 429, "1000000000,00")

        # Ajouter la valeur 0990 taxe due
        can.drawString(460, 429, "1000000000,00")

        # Ajouter la valeur 1010 base hors taxe
        can.drawString(338, 400, "1000000000,00")

        # Ajouter la valeur 1010 taxe due
        can.drawString(460, 400, "1000000000,00")

        # Ajoutrer la valeur 1020 base hors taxe
        can.drawString(338, 386, "1000000000,00")

        # Ajouter la valeur 1020 taxe due
        can.drawString(460, 386, "1000000000,00")

        # Ajouter la valeur 1040 base hors taxe
        can.drawString(338, 356, "1000000000,00")

        # Ajouter la valeur 1040 taxe due
        can.drawString(460, 356, "1000000000,00")

        # Ajouter la valeur 1050 base hors taxe
        can.drawString(338, 341, "1000000000,00")

        # Ajouter la valeur 1050 taxe due
        can.drawString(460, 341, "1000000000,00")

        # Ajouter la valeur 1081 base hors taxe
        can.drawString(338, 326, "1000000000,00")

        # Ajouter la valeur 1081 taxe due
        can.drawString(460, 326, "1000000000,00")

        # Ajouter la valeur 1090 base hors taxe
        can.drawString(338, 311, "1000000000,00")

        # Ajouter la valeur 1090 taxe due
        can.drawString(460, 311, "1000000000,00")

        # Ajouter la valeur 1100 base hors taxe
        can.drawString(338, 297, "1000000000,00")

        # Ajouter la valeur 1100 taxe due
        can.drawString(460, 297, "1000000000,00")

        # Ajouter la valeur 1110 base hors taxe
        can.drawString(338, 268, "1000000000,00")

        # Ajouter la valeur 1110 taxe due
        can.drawString(460, 268, "1000000000,00")

        # Ajouter la valeur 1120 base hors taxe
        can.drawString(338, 253, "1000000000,00")

        # Ajouter la valeur 1120 taxe due
        can.drawString(460, 253, "1000000000,00")

        # Ajouter la valeur 1030 base hors taxe
        can.drawString(338, 237, "1000000000,00")

        # Ajouter la valeur 1030 taxe due
        can.drawString(460, 237, "1000000000,00")

        # Ajouter la valeur "Total des lignes 35 à 46" base hors taxe
        can.drawString(338, 223, "1000000000,00")

        # Ajouter la valeur "Total des lignes 35 à 46" taxe due
        can.drawString(460, 223, "1000000000,00")

        can.save()

        # move to the beginning of the StringIO buffer
        packet.seek(0)
        new_pdf = PdfFileReader(packet)

        # read your existing PDF
        existing_pdf = PdfFileReader(open("TVA/Formulaire_3310_A_SD/Formulaire_3310_A_SD_page_1.pdf", "rb"))

        output = PdfFileWriter()

        # add the "watermark" (which is the new pdf) on the existing page
        page = existing_pdf.getPage(0)
        page.mergePage(new_pdf.getPage(0))
        output.addPage(page)

        # finally, write "output" to a real file
        output_stream = open("Formulaire_3310_A_SD/F_3310_A_SD_page_1_"
                             + datetime.today().strftime('%d_%m_%Y') + ".pdf", "wb")
        output.write(output_stream)
        output_stream.close()

    def test_formulaire_3310_a_2_rempli(self):
        packet = io.BytesIO()

        # create a new PDF with Reportlab
        can = canvas.Canvas(packet, pagesize=letter)
        can.setFontSize(8)

        # Ajouter la valeur 4213 net à payer
        can.drawString(477, 800, "1000000000,00")

        # Ajouter la valeur 47 base imposable
        can.drawString(380, 800, "1000000000,00")

        # Ajouter la valeur 48 base imposable
        can.drawString(380, 779, "1000000000,00")

        # Ajouter la valeur 4215 net à payer
        can.drawString(477, 781, "1000000000,00")

        # Ajouter la valeur 4238 net à payer
        # can.drawString(, , "1000000000,00")

        # Ajouter la valeur 4220 net à payer
        # can.drawString(, , "1000000000,00")

        # Ajouter la valeur 3240 net à payer
        # can.drawString(, , "1000000000,00")

        # Ajouter la valeur 4222 net à payer
        # can.drawString(, , "1000000000,00")

        # Ajouter la valeur 4207 net à payer
        # can.drawString(, , "1000000000,00")

        # Ajouter la valeur 55 nombre de kilomètres
        # can.drawString(, , "1000000000,00")

        # Ajouter la valeur 4219 net à payer
        # can.drawString(, , "1000000000,00")

        # Ajouter la valeur 4221 net à payer
        # can.drawString(, , "1000000000,00")

        # Ajouter la valeur 4229 net à payer
        # can.drawString(, , "1000000000,00")

        # Ajouter la valeur 59 base imposable
        # can.drawString(, , "1000000000,00")

        # Ajouter la valeur 60 base imposable
        # can.drawString(, , "1000000000,00")

        # Ajouter la valeur 4228 net à payer
        # can.drawString(, , "1000000000,00")

        # Ajouter la valeur 60A base imposable
        # can.drawString(, , "1000000000,00")

        # Ajouter la valeur 4298 net à payer
        # can.drawString(, , "1000000000,00")

        # Ajouter la valeur 60B base imposable
        # can.drawString(, , "1000000000,00")

        # Ajouter la valeur 4299 net à payer
        # can.drawString(, , "1000000000,00")

        # Ajouter la valeur 4214 net à payer
        # can.drawString(, , "1000000000,00")

        # Ajouter la valeur 4201 net à payer
        # can.drawString(, , "1000000000,00")

        # Ajouter la valeur 4225 net à payer
        # can.drawString(, , "1000000000,00")

        # Ajouter la valeur 4206 net à payer
        # can.drawString(, , "1000000000,00")

        # Ajouter la valeur 64 nombre d'actes
        # can.drawString(, , "1000000000,00")

        # Ajouter la valeur 4226 net à payer
        # can.drawString(, , "1000000000,00")

        # Ajouter la valeur 65 base imposable
        # can.drawString(, , "1000000000,00")

        # Ajouter la valeur 4204 net à payer
        # can.drawString(, , "1000000000,00")

        # Ajouter la valeur 66 nombre de passagers
        # can.drawString(, , "1000000000,00")

        # Ajouter la valeur 4217 net à payer
        # can.drawString(, , "1000000000,00")

        # Ajouter la valeur 68 base imposable
        # can.drawString(, , "1000000000,00")

        # Ajouter la valeur 4239 net à payer
        # can.drawString(, , "1000000000,00")

        # Ajouter la valeur 4288 net à payer
        # can.drawString(, , "1000000000,00")

        # Ajouter la valeur 71 base imposable
        # can.drawString(, , "1000000000,00")

        # Ajouter la valeur 72 base imposable
        # can.drawString(, , "1000000000,00")

        # Ajouter la valeur 4289 net à payer
        # can.drawString(, , "1000000000,00")

        # Ajouter la valeur 4240 net à payer
        # can.drawString(, , "1000000000,00")

        # Ajouter la valeur 75 base imposable
        # can.drawString(, , "1000000000,00")

        # Ajouter la valeur 4236 net à payer
        # can.drawString(, , "1000000000,00")

        # Ajouter la valeur 4241 net à payer
        # can.drawString(, , "1000000000,00")

        # Ajouter la valeur 4242 net à payer
        # can.drawString(, , "1000000000,00")

        # Ajouter la valeur 4243 net à payer
        # can.drawString(, , "1000000000,00")

        # Ajouter la valeur 4244 net à payer
        # can.drawString(, , "1000000000,00")

        # Ajouter la valeur 4245 net à payer
        # can.drawString(, , "1000000000,00")

        # Ajouter la valeur 82 base imposable
        # can.drawString(, , "1000000000,00")

        # Ajouter la valeur 83 base imposable
        # can.drawString(, , "1000000000,00")

        # Ajouter la valeur 4252 net à payer
        # can.drawString(, , "1000000000,00")

        # Ajouter la valeur 4253 net à payer
        # can.drawString(, , "1000000000,00")

        # Ajouter la valeur 4254 net à payer
        # can.drawString(, , "1000000000,00")

        # Ajouter la valeur 4247 net à payer
        # can.drawString(, , "1000000000,00")

        # Ajouter la valeur 4248 net à payer
        # can.drawString(, , "1000000000,00")

        # Ajouter la valeur 4249 net à payer
        # can.drawString(, , "1000000000,00")

        # Ajouter la valeur 87 nombre de tonnes
        # can.drawString(, , "1000000000,00")

        # Ajouter la valeur 4250 net à payer
        # can.drawString(, , "1000000000,00")

        # Ajouter la valeur 88 nombre d'etablissements
        # can.drawString(, , "1000000000,00")

        can.save()

        # move to the beginning of the StringIO buffer
        packet.seek(0)
        new_pdf = PdfFileReader(packet)

        # read your existing PDF
        existing_pdf = PdfFileReader(open("TVA/Formulaire_3310_A_SD/Formulaire_3310_A_SD_page_2.pdf", "rb"))

        output = PdfFileWriter()

        # add the "watermark" (which is the new pdf) on the existing page
        page = existing_pdf.getPage(0)
        page.mergePage(new_pdf.getPage(0))
        output.addPage(page)

        # finally, write "output" to a real file
        output_stream = open("Formulaire_3310_A_SD/F_3310_A_SD_page_2_"
                             + datetime.today().strftime('%d_%m_%Y') + ".pdf", "wb")
        output.write(output_stream)
        output_stream.close()

    def test_formulaire_3310_a_3_rempli(self):
        packet = io.BytesIO()

        # create a new PDF with Reportlab
        can = canvas.Canvas(packet, pagesize=letter)
        can.setFontSize(8)

        # Ajouter la valeur 4273 net à payer
        #can.drawString(, , "")

        # Ajouter la valeur 4274 net à payer
        #can.drawString(, , "")

        # Ajouter la valeur 4268 net à payer
        #can.drawString(, , "")

        # Ajouter la valeur 4270 net à payer
        #can.drawString(, , "")

        # Ajouter la valeur 91 base imposable
        # can.drawString(, , "")

        # Ajouter la valeur 92 base imposable
        # can.drawString(, , "")

        # Ajouter la valeur 4269 net à payer
        # can.drawString(, , "")

        # Ajouter la valeur 4271 net à payer
        # can.drawString(, , "")

        # Ajouter la valeur 93 base imposable
        # can.drawString(, , "")

        # Aouter la valeur 94 base imposable
        # can.drawString(, , "")

        # Ajouter la valeur 4272 net à payer
        # can.drawString(, , "")

        # Ajouter la valeur 4256 net à payer
        # can.drawString(, , "")

        # Ajouter la valeur 4259 net à payer
        # can.drawString(, , "")

        # Ajouter la valeur 4255 net à payer
        # can.drawString(, , "")

        # Ajouter la valeur 96 base imposable
        # can.drawString(, , "")

        # Ajouter la valeur 96 base imposable
        # can.drawString(, , "")

        # Ajouter la valeur 98 base imposbale
        # can.drawString(, , "")

        # Ajouter la valeur 4266 net à payer
        # can.drawString(, , "")

        # Ajouter la valeur 4267 net à payer
        # can.drawString(, , "")

        # Ajouter la valeur 4257 net à payer
        # can.drawString(, , "")

        # Ajouter la valeur 4260 net à payer
        # can.drawString(, , "")

        # Ajouter la valeur 4265 net à payer
        # can.drawString(, , "")

        # Ajouter la valeur 101 base imposable
        # can.drawString(, , "")

        # Ajouter la valeur 102 base imposable
        # can.drawString(, , "")

        # Ajouter la valeur 103 base imposable
        # can.drawString(, , "")

        # Ajouter la valeur 4258 net à payer
        # can.drawString(, , "")

        # Ajouter la valeur 4261 net à payer
        # can.drawString(, , "")

        # Ajouter la valeur 104 base imposable
        # can.drawString(, , "")

        # Ajouter la valeur 105 base imposable
        # can.drawString(, , "")

        # Ajouter la valeur 4264 net à payer
        # can.drawString(, , "")

        # Ajouter la valeur 4263 net à payer
        # can.drawString(, , "")

        # Ajouter la valeur 4281 net à payer
        # can.drawString(, , "")

        # Ajouter la valeur 4282 net à payer
        # can.drawString(, , "")

        # Ajouter la valeur 109 base imposable
        # can.drawString(, , "")

        # Ajouter la valeur 110 base imposable
        # can.drawString(, , "")

        # Ajouter la valeur 4283 net à payer
        # can.drawString(, , "")

        # Ajouter la valeur 111 base imposable
        # can.drawString(, , "")

        # Ajouter la valeur 4284 net à payer
        # can.drawString(, , "")

        # Ajouter la valeur 112 base imposable
        # can.drawString(, , "")

        # Ajouter la valeur 4285 net à payer
        # can.drawString(, , "")

        # Ajouter la valeur 113 base imposable
        # can.drawString(, , "")

        # Ajouter la valeur 4277 net à payer
        # can.drawString(, , "")

        # Ajouter la valeur 115 base imposable
        # can.drawString(, , "")

        # Ajouter la valeur 4278 net à payer
        # can.drawString(, , "")

        # Ajouter la valeur 116 base imposable
        # can.drawString(, , "")

        can.save()

        # move to the beginning of the StringIO buffer
        packet.seek(0)
        new_pdf = PdfFileReader(packet)

        # read your existing PDF
        existing_pdf = PdfFileReader(open("TVA/Formulaire_3310_A_SD/Formulaire_3310_A_SD_page_3.pdf", "rb"))

        output = PdfFileWriter()

        # add the "watermark" (which is the new pdf) on the existing page
        page = existing_pdf.getPage(0)
        page.mergePage(new_pdf.getPage(0))
        output.addPage(page)

        # finally, write "output" to a real file
        output_stream = open("Formulaire_3310_A_SD/Formulaire_3310_A_SD_page_3_"
                             + datetime.today().strftime('%d_%m_%Y') + ".pdf", "wb")
        output.write(output_stream)
        output_stream.close()

    def test_formulaire_3310_a_4_rempli(self):
        packet = io.BytesIO()

        # create a new PDF with Reportlab
        can = canvas.Canvas(packet, pagesize=letter)
        can.setFontSize(8)

        # Ajouter la valeur 4279 net à payer
        # can.drawString(, , "")

        # Ajouter la valeur 117 nombre de véhicules possédés ou loués
        # can.drawString(, , "")

        # Ajouter la valeur 117 nombre de kilomètres remboursés
        # can.drawString(, , "")

        # Ajouter la valeur 4280 net à payer
        # can.drawString(, , "")

        # Ajouter la valeur 118 nombre de véhicules possédés ou loués
        # can.drawString(, , "")

        # Ajouter la valeur 118 nombre de kilomètres remboursés
        # can.drawString(, , "")

        # Ajouter la valeur 4290 net à payer
        # can.drawString(, , "")

        # Ajouter la valeur 119 base imposable
        # can.drawString(, , "")

        # Ajouter la valeur 4291 net à payer
        # can.drawString(, , "")

        # Ajouter la valeur 121_1 code insee de la collectivité
        # can.drawString(, , "")

        # Ajouter la valeur 121_1 montant
        # can.drawString(, , "")

        # Ajouter la valeur 121_2 code insee de la collectivité
        # can.drawString(, , "")

        # Ajouter la valeur 121_2 montant
        # can.drawString(, , "")

        # Ajouter la valeur 121_3  code insee de la collectivité
        # can.drawString(, , "")

        # Ajouter la valeur 121_3 montant
        # can.drawString(, , "")

        # Ajouter la valeur 121_4 code insee de la collectivité
        # can.drawString(, , "")

        # Ajouter la valeur 121_4 montant
        # can.drawString(, , "")

        # Ajouter la valeur 121_5 code insee de la collectivité
        # can.drawString(, , "")

        # Aouter la valeur 121_5 montant
        # can.drawString(, , "")

        # Ajouter la valeur 121_6 code insee de la collectivité
        # can.drawString(, , "")

        # Ajouter la valeur 121_6 montant
        # can.drawString(, , "")

        # Ajouter la valeur 121_7 code insee de la collectivité
        # can.drawString(, , "")

        # Ajouter la valeur 121_7 montant
        # can.drawString(, , "")

        # Ajouter la valeur 121_8 code insee de la collectivité
        # can.drawString(, , "")

        # Ajouter la valeur 121_8 montant
        # can.drawString(, , "")

        # Ajouter la valeur 121_9 code insee de la collectivité
        # can.drawString(, , "")

        # Ajouter la valeur 121_9 montant
        # can.drawString(, , "")

        # Ajouter la valeur 4294 net à payer
        # can.drawString(, , "")

        # Ajouter la valeur 124 nombre d'hectolitres
        # can.drawString(, , "")

        # Ajouter la valeur 4296 net à payer
        # can.drawString(, , "")

        # Ajouter la valeur 125 nombre d'hectolitres
        # can.drawString(, , "")

        # Ajouter la valeur 4295 net à payer
        # can.drawString(, , "")

        # Ajouter la valeur 126 nombre d'hectolitres
        # can.drawString(, , "")

        # Ajouter la valeur 4293 net à payer
        # can.drawString(, , "")

        # Ajouter la valeur 128_1 code insee de la commune
        # can.drawString(, , "")

        # Ajouter la valeur 128_1 nombre d'hectolitres
        # can.drawString(, , "")

        # Ajouter la valeur 128_1 montant
        # can.drawString(, , "")

        # Ajouter la valeur 128_2 code insee de la commune
        # can.drawString(, , "")

        # Ajouter la valeur 128_2 nombre d'hectolitres
        # can.drawString(, , "")

        # Ajouter la valeur 128_2 montant
        # can.drawString(, , "")

        # Ajouter la valeur 128_3 code insee de la commune
        # can.drawString(, , "")

        # Ajouter la valeur 128_3 nombre d'hectolitres
        # can.drawString(, , "")

        # Ajouter la valeur 128_3 montant
        # can.drawString(, , "")

        # Ajouter la valeur 128_4 code insee de la commune
        # can.drawString(, , "")

        # Ajouter la valeur 128_4 nombre d'hectolitres
        # can.drawString(, , "")

        # Ajouter la valeur 128_4 montant
        # can.drawString(, , "")

        # Ajouter la valeur 128_5 code insee de la commune
        # can.drawString(, , "")

        # Ajouter la valeur 128_5 nombre d'hectolitres
        # can.drawString(, , "")

        # Ajouter la valeur 128_5 montant
        # can.drawString(, , "")

        # Ajouter la valeur 128_6 code insee de la commune
        # can.drawString(, , "")

        # Ajouter la valeur 128_6 nombre d'hectolitres
        # can.drawString(, , "")

        # Ajouter la valeur 128_6 montant
        # can.drawString(, , "")

        # Ajouter la valeur 128_7 code insee de la commune
        # can.drawString(, , "")

        # Ajouter la valeur 128_7 nombre d'hectolitres
        # can.drawString(, , "")

        # Ajouter la valeur 128_7 montant
        # can.drawString(, , "")

        # Ajouter la valeur "Total des lignes 47 à 128 (à reporter ligne 29 de la CA3)" net à payer
        # can.drawString(, , "")

        can.save()

        # move to the beginning of the StringIO buffer
        packet.seek(0)
        new_pdf = PdfFileReader(packet)

        # read your existing PDF
        existing_pdf = PdfFileReader(open("TVA/Formulaire_3310_A_SD/Formulaire_3310_A_SD_page_4.pdf", "rb"))

        output = PdfFileWriter()

        # add the "watermark" (which is the new pdf) on the existing page
        page = existing_pdf.getPage(0)
        page.mergePage(new_pdf.getPage(0))
        output.addPage(page)

        # finally, write "output" to a real file
        output_stream = open("Formulaire_3310_A_SD/Formulaire_3310_A_SD_page_4_"
                             + datetime.today().strftime('%d_%m_%Y') + ".pdf", "wb")
        output.write(output_stream)
        output_stream.close()


if __name__ == '__main__':
    unittest.main()
