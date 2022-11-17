import unittest
import pdfkit
from datetime import datetime as dt
import os
from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter


class UnitTestsEtatActesAccomplis(unittest.TestCase):
    def test_etat_actes_accomplis_mercorus(self):
        print("test_etat_actes_accomplis_mercorus")

        body = """
        <!doctype html>
        <html lang="en">
          <head>
            <!-- Required meta tags -->
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
        
            <!-- Bootstrap CSS -->
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-BmbxuPwQa2lc/FVzBcNJ7UAyJxM6wuqIj61tLrc4wSX0szH/Ev+nYRRuWlolflfl" crossorigin="anonymous">
        
            <title>L_Etat_Actes_Accomplis_Mercorus</title>
          </head>
          <body>
            <div class="card text-center">
              <div class="card-header">
                Etat des actes accomplis au nom de la S.A.S.U.A.C.V. MERCORUS en formation (annexé aux statuts)
              </div>
              <div class="card-body">
                <!-- Informations générales de la société MERCORUS -->
                <div class="card text-center">
                  <div class="card-header">
                    Informations générales de la société MERCORUS
                  </div>
                  <div class="card-body">
                    MERCORUS
                    <br>
                    Société par actions simplifiée unipersonnelle à capital variable en cours de formation au capital 
                    social de 100,00 euros
                    <br>
                    Siège social : 10 rue de Penthièvre 75008 Paris
                  </div>
                </div>
                <!-- Informations générales de la société MERCORUS -->
                
                <br>
                <br>
                
                <!-- Responsable de la rédaction -->
                <div class="card text-center">
                  <div class="card-header">
                    Responsable de la rédaction de l'état des actes accomplis au nom de la S.A.S.U.A.C.V. MERCORUS 
                    en formation
                  </div>
                  <div class="card-body">
                    Je soussigné Monsieur  né le 11 novembre 1993 à 
                    Saint-Louis (97450) demeurant au 6 Avenue Léon Blum - Étage 1 Porte 6 - 93800 Épinay-sur-Seine 
                    de nationalité française a établi ainsi qu'il suit l'état des actes accomplis au nom de 
                    la société par actions simplifiée unipersonnelle à capital variable MERCORUS en formation 
                    (annexé aux statuts), qu'il a décidé d'instituer.
                  </div>
                </div>
                <!-- Responsable de la rédaction -->
                
                <br>
                <br>
                
                <!-- Abréviations -->
                <div class="card text-center">
                  <div class="card-header">
                    Abréviations
                  </div>
                  <div class="card-body">
                    L'abréviation «S.A.S.U.A.C.V.» veut dire «Société par actions simplifiée unipersonnelle à 
                    capital variable». 
                    <br>
                    L'abréviation «S.A.S.A.C.V.» veut dire «Société par actions simplifiée à capital variable».
                  </div>
                </div>
                <!-- Abréviations -->
                
                <br>
                <br>
                
                <!-- Actes accomplis -->
                <div class="card text-center">
                  <div class="card-header">
                    Actes accomplis
                  </div>
                  <div class="card-body">
                    Monsieur , né le 11 Novembre 1993 à Saint-Louis (97450), 
                    demeurant au 6 Avenue Léon Blum - Étage 1 Porte 6 - 93800 Épinay-sur-Seine, agissant en qualité de 
                    Président-associé unique de la S.A.S.U.A.C.V. MERCORUS en formation, déclare avoir pris 
                    personnellement, en vue de la création de ladite société, les engagements suivants :
                    
                    <br>
                    <br>
                    
                    - Rédaction, signature et impression en 6 exemplaires des statuts de la  S.A.S.U.A.C.V. 
                    MERCORUS en formation en date du 25 Mars 2021 à Epinay-sur-Seine (93800) ;
                    
                    <br>
                    <br>
                    
                    - Remplissage, signature et impression en 2 exemplaires du formulaire CERFA n°13959*06 de 
                    déclaration de constitution M0 SAS en date du 25 Mars 2021 à Epinay-sur-Seine (93800) ;
                    
                    <br>
                    <br>
                    
                    - Remplissage, signature et impression du formulaire de déclaration sur l'honneur de non 
                    condamnation et de filiation pour la personne physique nommée Monsieur Jason Aymérick Jean 
                    Claudius ALOYAU né le 11 Novembre 1993 à Saint-Louis (97450), demeurant au 6 Avenue Léon Blum 
                    - Étage 1 Porte 6 - 93800 Épinay-sur-Seine en date du 25 Mars 2021 à Epinay-sur-Seine (93800) ;
                    
                    <br>
                    <br>
                    
                    - Impression d'une copie du passeport de Monsieur  en noir 
                    et blanc en date du 25 Mars 2021 à Epinay-sur-Seine (93800) ;
                    
                    <br>
                    <br>
                    
                    – Signature d'un contrat de domiciliation d’entreprises en date du 25 Mars 2021 à Paris (75008)
                    pour domicilier le siège social de la S.A.S.U.A.C.V. MERCORUS en formation au 10 rue de Penthièvre
                    75008 Paris dont le prestataire est : Digidom et le numéro d’agrément préfectoral de la société 
                    Digidom est:  ;
                     
                    <br>
                    <br>
                     
                    - Impression d'une copie du contrat de domiciliation de la S.A.S.U.A.C.V. MERCORUS en formation 
                    en date du 25 Mars 2021 à Paris (75001) ; 
                        
                    <br>
                    <br>
                    
                    -  Retrait d’un chèque de banque d'un montant de 63,13 euros à l'ordre du greffe du tribunal 
                    de commerce de Paris émis par La Banque Postale ANTONY PRINCIPAL 32 RUE AUGUSTE MOUNIE 92160 
                    ANTONY en date du 10 Avril 2021 pour la constitution de la S.A.S.U.A.C.V. MERCORUS 
                    depuis le compte bancaire Livret A dont le numéro de compte est : 124 2770526 D géré par La 
                    Banque Postale dont le titulaire est : Monsieur  né le 11 
                    Novembre 1993 à Saint-Louis (97450), demeurant au 6 Avenue Léon Blum - Étage 1 Porte 6 - 93800 
                    Épinay-sur-Seine ;
                    
                    <br>
                    <br>
                    
                    -  Retrait d’un chèque de banque d'un montant de 100,00 euros à l'ordre de la Caisse des dépôts 
                    et consignations émis par La Banque Postale ANTONY PRINCIPAL 32 RUE AUGUSTE MOUNIE 92160 ANTONY 
                    en date du 10 Avril 2021 pour le dépôt de capital social auprès de la Caisse des dépôts et 
                    consignations depuis le compte bancaire Livret A dont le numéro de compte est : 124 2770526 D 
                    géré par La Banque Postale dont le titulaire est : Monsieur  
                    né le 11 Novembre 1993 à Saint-Louis (97450), demeurant au 6 Avenue Léon Blum - Étage 1 Porte 6 - 
                    93800 Épinay-sur-Seine ;
                    
                    <br>
                    <br>
                    
                    -  Envoi d'une demande de dépôts de capital social pour la constitution du capital social de la 
                    S.A.S.U.A.C.V. MERCORUS en formation auprès de la Caisse des dépôts et consignations pour un 
                    montant de cent euros, ci 100,00 euros en date du 10 Avril 2021 à Épinay-sur-Seine (93800) ;
                    
                    <br>
                    <br>
                    
                    -  Remplissage, signature et impression de la liste des souscripteurs de la S.A.S.U.A.C.V. 
                    MERCORUS en formation en date du 10 Avril 2021 à Paris (75001) ;
                    
                    <br>
                    <br>
                    
                    -  Remplissage, signature et impression du formulaire DBE-S-1 en version du 30/04/2018 pour 
                    lister les bénéficiaires effectifs de la S.A.S.U.A.C.V. MERCORUS en formation en date du 
                    10 Avril 2021 à Paris (75001) ;
                    
                    <br>
                    <br>
                    
                    – Impression du justificatif de domicile de Monsieur  
                    en date du 10 Avril 2021 à Paris (75001) ;
                    
                    <br>
                    <br>
                    
                    – Demande de publication d’un avis dans un journal d'annonces légales 
                    dont le prestataire est: L'Auvergnat de Paris sis au 16 rue Saint Fiacre 75002 
                    Paris en date du 10 Avril 2021 à Paris.
                  </div>
                </div>
                <!-- Actes accomplis -->
                
                <br>
                <br>
                
                <!-- Acceptation de l'état des actes accomplis de la société MERCORUS -->
                <div class="card text-center">
                  <div class="card-header">
                    Acceptation de l'état des actes accomplis au nom de la S.A.S.U.A.C.V. MERCORUS en formation
                  </div>
                  <div class="card-body">
                    En application de l'article L210-6 du code de commerce, le présent état des actes 
                    accomplis reprenant l'énumération intégrale des engagements pris par Monsieur 
                     pour le compte de la S.A.S.U.A.C.V. 
                    MERCORUS en formation, a été révisé par Monsieur Jason Aymérick Jean 
                    Claudius ALOYAU après la signature des statuts en date du 10 Avril 2021 à Paris.
                    
                    <br>
                    <br>
            
                    Selon l’alinéa 3 de l'article R210-6 du code de commerce, l'immatriculation de la 
                    S.A.S.U.A.C.V. HOLOMORPHE au Registre du Commerce et des Sociétés 
                    emportera reprise des engagements souscrits par ladite société.
                  </div>
                </div>
                <!-- Acceptation des statuts de la société MERCORUS -->
                
                <br>
                <br>
                
              </div>
            </div>
            
            <br>
            <br>
            
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/js/bootstrap.bundle.min.js" integrity="sha384-b5kHyXgcpbZJO/tY9Ul7kGkf1S0CWuKcCD38l8YkeH8z8QjE0GmW1gYU5S9FOnJ0" crossorigin="anonymous"></script>
          </body>
        </html>
        """

        options = {
            'page-size': 'A4',
            'header-left': 'Etat des actes accomplis au nom de la S.A.S.U.A.C.V. MERCORUS en formation',
            'footer-left': '[page] sur [topage]'
        }

        path_wkthmltopdf = "C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe"

        config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)

        pdfkit.from_string(body, "Mercorus\\Etat_Actes_Accomplis_Mercorus.pdf", configuration=config, options=options)

        filename = "Mercorus\\Etat_Actes_Accomplis_Mercorus.pdf"

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

            x_coord = round(4.4 * 72)

            y_coord = round(0.03 * 72)

            width = 100

            height = round(0.55 * 72)

            os.system("signpdf " + str(filename_to_sign) + " " + str(signature) + " --coords " + str(page_number) + "x"
                      + str(x_coord) + "x" + str(y_coord) + "x" + str(width) + "x" + str(height))
        except Exception as e:
            print("error : " + str(e))


if __name__ == '__main__':
    unittest.main()
