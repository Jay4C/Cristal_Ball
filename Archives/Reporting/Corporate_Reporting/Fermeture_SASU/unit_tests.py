import unittest
import pdfkit
from datetime import datetime as dt
import os, shutil
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from PyPDF2 import PdfFileReader, PdfFileWriter


class Fermeture_Holomorphe(unittest.TestCase):
    # ok
    def test_proces_verbal_dissolution(self):
        print("test_proces_verbal_dissolution")

        body = """
        <!doctype html>
        <html lang="en">
          <head>
            <!-- Required meta tags -->
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">

            <!-- Bootstrap CSS -->
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/css/bootstrap.min.css" 
            rel="stylesheet" integrity="sha384-BmbxuPwQa2lc/FVzBcNJ7UAyJxM6wuqIj61tLrc4wSX0szH/Ev+nYRRuWlolflfl" 
            crossorigin="anonymous">

            <title>Procès-verbal de dissolution de la S.A.S.U. HOLOMORPHE</title>
          </head>
          <body>
            <div class="container">

                <br>

                <div class="card text-center">
                  <div class="card-header">
                    Informations générales de la société Holomorphe
                  </div>
                  <div class="card-body">
                    <ul class="list-group list-group-flush">
                      <li class="list-group-item">
                        Dénomination sociale : S.A.S.U. à capital variable HOLOMORPHE / Capital social : 100 euros
                      </li>
                      <li class="list-group-item">
                        Adresse du siège social : 31 Avenue de Ségur - ABC LIV Ségur - 75007 Paris 
                        / Siret : 88363255600014
                      </li>
                      <li class="list-group-item">
                        Registre du commerce et des sociétés : R.C.S. PARIS - 
                        Greffe du Tribunal de Commerce de PARIS
                      </li>
                      <li class="list-group-item">
                        Activités : Commerce de gros de produits chimiques - Edition de logiciels applicatifs 
                        / Code NAF : 4675Z
                      </li>
                      <li class="list-group-item">
                        Numero TVA intracommunataire : FR06883632556 / Président : Monsieur  
                        / Date d'immatriculation : 26 Mai 2020
                      </li>
                    </ul>
                  </div>
                </div>

                <br>
                
                <!-- Procès-verbal de dissolution de la société HOLOMORPHE -->
                <div class="card text-center">
                  <div class="card-header">
                    Procès-verbal de dissolution de la société par actions simplifiée unipersonnelle à capital 
                    variable HOLOMORPHE
                  </div>
                  <div class="card-body">
                    <h6>
                        Vu l'article 1844-7 du Code civil,
                        <br>
                        Vu les articles L237-1 à L237-13 du Code de commerce concernant les dispositions générales de 
                        la liquidation,
                        <br>
                        Vu la loi n°2019-1479 du 28 décembre 2019 de finances pour 2020,
                    </h6>
                    
                    <br>
                    
                    <h6>
                        Monsieur  demeurant au 6 Avenue Léon Blum 93800 
                        Epinay-sur-Seine, actionnaire unique de la société par actions simplifiée unipersonnelle à 
                        capital variable HOLOMORPHE, a pris les décisions concernant l'ordre du jour suivant:
                        <br>
                        - Dissolution anticipée de la société par actions simplifiée unipersonnelle à capital variable 
                        HOLOMORPHE ;
                        <br>
                        - Nomination du liquidateur de la société par actions simplifiée unipersonnelle à capital 
                        variable HOLOMORPHE ;
                        <br>
                        - Rémunération du liquidateur de la société par actions simplifiée unipersonnelle à capital 
                        variable HOLOMORPHE.
                    </h6>
                    
                    <br>
                    
                    <!-- Première résolution -->
                    <div class="card text-center">
                      <div class="card-header">
                        Première résolution
                      </div>
                      <div class="card-body">
                        L'actionnaire unique de la société par actions simplifiée unipersonnelle à capital variable 
                        HOLOMORPHE décide de la dissolution anticipée de la société par actions simplifiée 
                        unipersonnelle à capital variable HOLOMORPHE et sa liquidation amiable conformément 
                        aux dispositions des articles L237-1 à 237-13 du Code de commerce.
                        
                        <br>
                        <br>
                        
                        La société par actions simplifiée unipersonnelle à capital variable HOLOMORPHE subsistera 
                        pour les besoins de la liquidation et jusqu'à la clôture de celle-ci.
                        
                        <br>
                        <br>
                        
                        Durant cette période, la dénomination sociale de la société par actions simplifiée 
                        unipersonnelle à capital variable HOLOMORPHE sera suivie de la mention "société en 
                        liquidation". Cette mention ainsi que le nom du liquidateur devront figurer sur tous les 
                        documents et actes destinés au tiers.
                        
                        <br>
                        <br>
                        
                        Le siège social de la liquidation de la société par actions simplifiée unipersonnelle à 
                        capital variable HOLOMORPHE est fixé au 31 Avenue de Ségur 75007 Paris.
                      </div>
                    </div>
                    <!-- Première résolution -->
                    
                    <br>
                    
                    <!-- Deuxième résolution -->
                    <div class="card text-center">
                      <div class="card-header">
                        Deuxième résolution
                      </div>
                      <div class="card-body">
                        L'actionnaire unique de la société par actions simplifiée unipersonnelle à capital variable 
                        HOLOMORPHE sera désigné en qualité de liquidateur de la société par actions simplifiée 
                        unipersonnelle à capital variable HOLOMORPHE et pour une durée de deux mois.
                        
                        <br>
                        <br>
                        
                        Dans les deux mois de sa nomination, le liquidateur de la société par actions simplifiée 
                        unipersonnelle à capital variable HOLOMORPHE doit faire un rapport sur la situation 
                        comptable de la société par actions simplifiée unipersonnelle à capital variable HOLOMORPHE, 
                        sur la poursuite des opérations de liquidation de la société par actions simplifiée 
                        unipersonnelle à capital variable HOLOMORPHE et sur le délai nécessaire pour les terminer.
                        
                        <br>
                        <br>
                        
                        L'actionnaire unique de la société par actions simplifiée unipersonnelle à capital variable 
                        HOLOMORPHE décide que le liquidateur de la société par actions simplifiée unipersonnelle à 
                        capital variable HOLOMORPHE n'a pas droit, en contrepartie de l'exercice de son mandat, 
                        à une rémunération.
                        
                        <br>
                        <br>
                        
                        Monsieur  déclare accepter ses fonctions de liquidateur de 
                        la société par actions simplifiée unipersonnelle à capital variable HOLOMORPHE et certifie ne 
                        pas être sous le coup des interdictions prévues par les lois et règlements en vigueur.
                      </div>
                    </div>
                    <!-- Deuxième résolution -->
                    
                    <br>
                    
                    <!-- Troisième résolution -->
                    <div class="card text-center">
                      <div class="card-header">
                        Troisième résolution
                      </div>
                      <div class="card-body">
                        L'actionnaire unique de la société par actions simplifiée unipersonnelle à capital variable 
                        HOLOMORPHE donne au liquidateur de la société par actions simplifiée unipersonnelle à capital 
                        variable HOLOMORPHE les pouvoirs les plus étendus pour mener à bien sa mission, 
                        c'est-à-dire réaliser l'actif, payer le passif et répartir le solde, sous réserve 
                        des dispositions des articles L237-1 et suivants du Code de commerce.
                      </div>
                    </div>
                    <!-- Troisième résolution -->
                    
                    <br>
                    
                    <!-- Quatrième résolution -->
                    <div class="card text-center">
                      <div class="card-header">
                        Quatrième résolution
                      </div>
                      <div class="card-body">
                        Tous pouvoirs sont attribués au liquidateur de la société par actions simplifiée 
                        unipersonnelle à capital variable HOLOMORPHE pour effectuer les formalités légales afférentes 
                        aux décisions adoptées ci-dessus.
                        
                        <br>
                        <br>
                        
                        L'ordre du jour étant épuisé, la séance est levée.
                        
                        <br>
                        <br>
                        
                        De tout ce qui précède, il a été dressé le présent procès-verbal de dissolution de la société 
                        par actions simplifiée unipersonnelle à capital variable HOLOMORPHE signé par l'actionnaire 
                        unique de la société par actions simplifiée unipersonnelle à capital variable HOLOMORPHE. 
                      </div>
                    </div>
                    <!-- Quatrième résolution -->
                    
                    <br>
                    
                    <!-- L'actionnaire unique -->
                    <div class="card text-center">
                      <div class="card-header">
                        L'actionnaire unique de la société par actions simplifiée unipersonnelle à capital variable 
                        HOLOMORPHE
                      </div>
                      <div class="card-body">
                        Monsieur , l'actionnaire unique de la société par actions 
                        simplifiée unipersonnelle à capital variable HOLOMORPHE.
                      </div>
                    </div>
                    <!-- L'actionnaire unique -->
                    
                    <br>
                  </div>
                </div>
                <!-- Procès-verbal de dissolution de la société HOLOMORPHE -->
                
                <br>

              </div>

              <br>

            </div>

            <br>

            <!-- Option 1: Bootstrap Bundle with Popper -->
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/js/bootstrap.bundle.min.js" 
            integrity="sha384-b5kHyXgcpbZJO/tY9Ul7kGkf1S0CWuKcCD38l8YkeH8z8QjE0GmW1gYU5S9FOnJ0" 
            crossorigin="anonymous"></script>
          </body>
        </html>
        """

        options = {
            'page-size': 'A4',
            'footer-left': 'Société HOLOMORPHE [SIREN : 883 632 556]',
            'header-center': "Procès-verbal de dissolution de la S.A.S.U.A.C.V. HOLOMORPHE",
            'footer-right': '[page] sur [topage]'
        }

        path_wkthmltopdf = "C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe"

        config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)

        pdfkit.from_string(body,
                           "PV_Dissolution\\P_V_Dissolution_[HOLOMORPHE].pdf",
                           configuration=config,
                           options=options)

        filename = "PV_Dissolution\\P_V_Dissolution_[HOLOMORPHE].pdf"

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

        # P_V_Dissolution
        proces_verbal_dissolution_folder = "PV_Dissolution"

        proces_verbal_dissolution_folder_files = os.listdir(proces_verbal_dissolution_folder)

        proces_verbal_dissolution_filename = ""

        for f in proces_verbal_dissolution_folder_files:
            if "signed" in f:
                proces_verbal_dissolution_filename += f
                print("proces_verbal_dissolution_filename : "
                      + proces_verbal_dissolution_filename)
                break

        proces_verbal_dissolution = proces_verbal_dissolution_folder + "\\" + proces_verbal_dissolution_filename

        shutil.copy(
            proces_verbal_dissolution,
            "PV_Dissolution\\PV_Dissolution_HOLOMORPHE.pdf"
        )

    # not ok
    def test_split_scan_pv_de_dissolution_holomorphe_v1(self):
        print('test_split_scan_pv_de_dissolution_holomorphe')

        folder_split = 'A:\\1_Professionnel\\1_Holomorphe\\2_Archives\\5_Non_Prioritaires\\2_Fermeture_SASU' \
                       '\\2_PV_Dissolution\\Split'

        pdf_document = "A:\\1_Professionnel\\1_Holomorphe\\2_Archives\\5_Non_Prioritaires\\2_Fermeture_SASU" \
                       "\\2_PV_Dissolution\\PV_DE_DISSOLUTION_HOLOMORPHE.pdf"

        pdf = PdfFileReader(pdf_document)

        for page in range(pdf.getNumPages()):
            pdf_writer = PdfFileWriter

            pdf_writer.addPage(pdf.getPage(page))

            output_filename = folder_split + "\\page_{}.pdf".format(page + 1)

            with open(output_filename, "wb") as out:
                pdf_writer.write(out)

                print("Created : ", output_filename)

    # ok
    def test_split_scan_pv_de_dissolution_holomorphe_v2(self):
        print("test_split_scan_pv_de_dissolution_holomorphe_v2")

        pdf_document = "A:\\1_Professionnel\\1_Holomorphe\\2_Archives\\5_Non_Prioritaires\\2_Fermeture_SASU" \
                       "\\2_PV_Dissolution\\PV_DE_DISSOLUTION_HOLOMORPHE.pdf"

        folder_split = 'A:\\1_Professionnel\\1_Holomorphe\\2_Archives\\5_Non_Prioritaires\\2_Fermeture_SASU' \
                       '\\2_PV_Dissolution\\Split'

        inputpdf = PdfFileReader(open(pdf_document, "rb"))

        for i in range(inputpdf.numPages):
            output = PdfFileWriter()

            output.addPage(inputpdf.getPage(i))

            with open(folder_split + "\\Page_%s.pdf" % i, "wb") as outputStream:
                output.write(outputStream)

    #
    def test_proces_verbal_liquidation(self):
        print("test_proces_verbal_liquidation")

        body = """
        <!doctype html>
        <html lang="en">
          <head>
            <!-- Required meta tags -->
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">

            <!-- Bootstrap CSS -->
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/css/bootstrap.min.css" 
            rel="stylesheet" integrity="sha384-BmbxuPwQa2lc/FVzBcNJ7UAyJxM6wuqIj61tLrc4wSX0szH/Ev+nYRRuWlolflfl" 
            crossorigin="anonymous">

            <title>Procès-verbal de liquidation de la S.A.S.U. HOLOMORPHE</title>
          </head>
          <body>
            <div class="container">

                <br>

                <div class="card text-center">
                  <div class="card-header">
                    Informations générales de la société Holomorphe
                  </div>
                  <div class="card-body">
                    <ul class="list-group list-group-flush">
                      <li class="list-group-item">
                        Dénomination sociale : S.A.S.U. à capital variable HOLOMORPHE / Capital social : 100 euros
                      </li>
                      <li class="list-group-item">
                        Adresse du siège social : 31 Avenue de Ségur - ABC LIV Ségur - 75007 Paris 
                        / Siret : 88363255600014
                      </li>
                      <li class="list-group-item">
                        Registre du commerce et des sociétés : R.C.S. PARIS - 
                        Greffe du Tribunal de Commerce de PARIS
                      </li>
                      <li class="list-group-item">
                        Activités : Commerce de gros de produits chimiques - Edition de logiciels applicatifs 
                        / Code NAF : 4675Z
                      </li>
                      <li class="list-group-item">
                        Numero TVA intracommunataire : FR06883632556 / Président : Monsieur  
                        / Date d'immatriculation : 26 Mai 2020
                      </li>
                    </ul>
                  </div>
                </div>

                <br>

                <!-- Procès-verbal de liquidation de la société HOLOMORPHE -->
                <div class="card text-center">
                  <div class="card-header">
                    Procès-verbal de liquidation de la société par actions simplifiée unipersonnelle à capital 
                    variable HOLOMORPHE
                  </div>
                  <div class="card-body">
                    <h6>
                        Vu l'article 1844-7 du Code civil,
                        <br>
                        Vu les articles L237-1 à L237-13 du Code de commerce concernant les dispositions générales de 
                        la liquidation,
                        <br>
                        Vu la loi n°2019-1479 du 28 décembre 2019 de finances pour 2020,
                    </h6>

                    <br>

                    <h6>
                        Monsieur , associé unique de la société par actions 
                        simplifiée unipersonnelle à capital variable HOLOMORPHE demeurant au 6 Avenue Léon Blum 93800 
                        Epinay-sur-Seine, a pris les décisions suivantes :
                        <br>
                        – Approbation des comptes de liquidation de la société par actions simplifiée unipersonnelle 
                        à capital variable HOLOMORPHE ;
                        <br>
                        – Répartition du solde de liquidation de la société par actions simplifiée unipersonnelle 
                        à capital variable HOLOMORPHE ;
                        <br>
                        – Constatation de la clôture des opérations de liquidation de la société par actions 
                        simplifiée unipersonnelle à capital variable HOLOMORPHE ;
                        <br>
                        – Pouvoir en vue d'accomplir les formalités pour le compte de la société par actions 
                        simplifiée unipersonnelle à capital variable HOLOMORPHE.
                    </h6>

                    <br>

                    <!-- Première décision  -->
                    <div class="card text-center">
                      <div class="card-header">
                        Première décision – Approbation des comptes de liquidation de la société par actions 
                        simplifiée unipersonnelle à capital variable HOLOMORPHE
                      </div>
                      <div class="card-body">
                        Monsieur , associé unique de la société par actions 
                        simplifiée unipersonnelle à capital variable HOLOMORPHE, approuve les opérations de liquidation 
                        de la société par actions simplifiée unipersonnelle à capital variable HOLOMORPHE ainsi 
                        que les comptes définitifs de la société par actions simplifiée unipersonnelle à capital 
                        variable HOLOMORPHE qui en résultent, faisant ressortir un solde [« Négatif » ou « Positif »] 
                        de [Montant du solde] euros.
                      </div>
                    </div>
                    <!-- Première décision -->

                    <br>

                    <!-- Deuxième décision -->
                    <div class="card text-center">
                      <div class="card-header">
                        Deuxième décision - Répartition du solde de liquidation de la société par actions simplifiée 
                        unipersonnelle à capital variable HOLOMORPHE
                      </div>
                      <div class="card-body">
                        L'associé unique de la société par actions simplifiée unipersonnelle à capital variable 
                        HOLOMORPHE décide de répartir le solde [« Négatif » ou « Positif »] de liquidation de la 
                        société par actions simplifiée unipersonnelle à capital variable HOLOMORPHE s'élevant à 
                        [Montant du solde] de la façon suivante : [« attribution au profit de l'associé unique de la 
                        société par actions simplifiée unipersonnelle à capital variable HOLOMORPHE » 
                        en cas de boni ou « remboursement partiel des titres souscrits à hauteur de [Montant remboursé] 
                        euros » en cas de mali].
                      </div>
                    </div>
                    <!-- Deuxième décision -->

                    <br>

                    <!-- Troisième décision -->
                    <div class="card text-center">
                      <div class="card-header">
                        Troisième décision - Clôture définitive des opérations de liquidation de la société par 
                        actions simplifiée unipersonnelle à capital variable HOLOMORPHE
                      </div>
                      <div class="card-body">
                        L'associé unique de la société par actions simplifiée unipersonnelle à capital variable 
                        HOLOMORPHE donne quitus au liquidateur de la société par actions simplifiée unipersonnelle à 
                        capital variable HOLOMORPHE de sa gestion et le décharge de son mandat. 
                        
                        <br>
                        <br>
                        
                        L'associé unique de la société par actions simplifiée unipersonnelle à capital variable 
                        HOLOMORPHE constate la fin des opérations de liquidation de la société par actions simplifiée 
                        unipersonnelle à capital variable HOLOMORPHE et prononce la clôture définitive de la 
                        liquidation de la société par actions simplifiée unipersonnelle à capital variable 
                        HOLOMORPHE.
                        
                        <br>
                        <br>
                        
                        Par conséquent, la personnalité morale de la société par actions simplifiée unipersonnelle à 
                        capital variable HOLOMORPHE cesse d'exister à compter de ce jour.
                      </div>
                    </div>
                    <!-- Troisième décision -->

                    <br>

                    <!-- Quatrième décision -->
                    <div class="card text-center">
                      <div class="card-header">
                        Quatrième décision - Pouvoir en vue d'accomplir les formalités pour le compte de la 
                        société par actions simplifiée unipersonnelle à capital variable HOLOMORPHE
                      </div>
                      <div class="card-body">
                        L'associé unique de la société par actions simplifiée unipersonnelle à capital variable 
                        HOLOMORPHE donne tous pouvoirs à Monsieur  pour effectuer 
                        les formalités légales afférentes aux décisions adoptées ci-dessus.
                        
                        <br>
                        <br>
                        
                        De tout ce qui précède, il a été dressé le présent procès-verbal de liquidation de la 
                        société par actions simplifiée unipersonnelle à capital variable HOLOMORPHE signé par 
                        l'associé unique de la société par actions simplifiée unipersonnelle à capital variable 
                        HOLOMORPHE et consigné dans le registre spécial prévu par la Loi.
                      </div>
                    </div>
                    <!-- Quatrième décision -->

                    <br>

                    <!-- L'actionnaire unique -->
                    <div class="card text-center">
                      <div class="card-header">
                        L'actionnaire unique de la société par actions simplifiée unipersonnelle à capital variable 
                        HOLOMORPHE
                      </div>
                      <div class="card-body">
                        Monsieur , l'actionnaire unique de la société par actions 
                        simplifiée unipersonnelle à capital variable HOLOMORPHE.
                      </div>
                    </div>
                    <!-- L'actionnaire unique -->

                    <br>
                  </div>
                </div>
                <!-- Procès-verbal de liquidation de la société HOLOMORPHE -->

                <br>

              </div>

              <br>

            </div>

            <br>

            <!-- Option 1: Bootstrap Bundle with Popper -->
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/js/bootstrap.bundle.min.js" 
            integrity="sha384-b5kHyXgcpbZJO/tY9Ul7kGkf1S0CWuKcCD38l8YkeH8z8QjE0GmW1gYU5S9FOnJ0" 
            crossorigin="anonymous"></script>
          </body>
        </html>
        """

        options = {
            'page-size': 'A4',
            'footer-left': 'Société HOLOMORPHE [SIREN : 883 632 556]',
            'header-center': "Procès-verbal de liquidation de la S.A.S.U.A.C.V. HOLOMORPHE",
            'footer-right': '[page] sur [topage]'
        }

        path_wkthmltopdf = "C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe"

        config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)

        pdfkit.from_string(body,
                           "PV_Liquidation\\P_V_Liquidation_[HOLOMORPHE].pdf",
                           configuration=config,
                           options=options)

        filename = "PV_Liquidation\\P_V_Liquidation_[HOLOMORPHE].pdf"

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

        # PV_Liquidation
        proces_verbal_liquidation_folder = "PV_Liquidation"

        proces_verbal_liquidation_folder_files = os.listdir(proces_verbal_liquidation_folder)

        proces_verbal_liquidation_filename = ""

        for f in proces_verbal_liquidation_folder_files:
            if "signed" in f:
                proces_verbal_liquidation_filename += f
                print("proces_verbal_liquidation_filename : "
                      + proces_verbal_liquidation_filename)
                break

        proces_verbal_dissolution = proces_verbal_liquidation_folder + "\\" + proces_verbal_liquidation_filename

        shutil.copy(
            proces_verbal_dissolution,
            "PV_Liquidation\\PV_Liquidation_HOLOMORPHE.pdf"
        )


if __name__ == '__main__':
    unittest.main()
