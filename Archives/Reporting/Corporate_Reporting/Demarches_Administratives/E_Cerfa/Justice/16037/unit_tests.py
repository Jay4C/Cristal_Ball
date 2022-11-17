import os
import unittest
from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from datetime import datetime as dt


class UnitTestsECerfa16037(unittest.TestCase):
    def test_e_cerfa_16037_fictif(self):
        print("test_e_cerfa_16037_fictif")

        # read your existing PDF
        original_pdf = PdfFileReader(open("Cerfa_16037.pdf", "rb"))

        filled_pdf = PdfFileWriter()

        # Page 1
        packet_1 = io.BytesIO()

        # create a new PDF with Reportlab
        can_1 = canvas.Canvas(packet_1, pagesize=letter)

        can_1.setFontSize(8)

        # Cocher la cocher la case "Madame"
        can_1.drawString(round(0.64 * 72), round(5.6 * 72), "X")

        # Cocher la cocher la case "Monsieur"
        can_1.drawString(round(2.6 * 72), round(5.6 * 72), "X")

        # Insérer "Votre nom de famille (nom de naissance)"
        can_1.drawString(round(3.78 * 72), round(5.31 * 72), "")

        # Insérer "Votre nom d'usage (exemple : nom d'époux / d'épouse)"
        can_1.drawString(round(4.67 * 72), round(5.05 * 72), "")

        # Insérer "Vos prénoms"
        can_1.drawString(round(1.64 * 72), round(4.77 * 72), "")

        # Insérer "Vos date et lieu de naissance"
        # (chiffre 1 du jour)
        can_1.drawString(round(2.8 * 72), round(4.51 * 72), "")
        # (chiffre 2 du jour)
        can_1.drawString(round(3.01 * 72), round(4.51 * 72), "")
        # (chiffre 1 du mois)
        can_1.drawString(round(3.22 * 72), round(4.51 * 72), "")
        # (chiffre 2 du mois)
        can_1.drawString(round(3.43 * 72), round(4.51 * 72), "")
        # (chiffre 1 de l'année)
        can_1.drawString(round(3.64 * 72), round(4.51 * 72), "")
        # (chiffre 2 de l'année)
        can_1.drawString(round(3.85 * 72), round(4.51 * 72), "")
        # (chiffre 3 de l'année)
        can_1.drawString(round(4.06 * 72), round(4.51 * 72), "")
        # (chiffre 4 de l'année)
        can_1.drawString(round(4.27 * 72), round(4.51 * 72), "")
        # (à)
        can_1.drawString(round(0.96 * 72), round(4.23 * 72), "Saint-Louis (97450)")

        # Insérer "Votre (ou vos) nationalité(s)"
        can_1.drawString(round(2.75 * 72), round(3.95 * 72), "Française")

        # Insérer "Votre adresse"
        can_1.drawString(round(1.71 * 72), round(3.64 * 72), "")

        # Insérer "Complément d'adresse"
        can_1.drawString(round(2.44 * 72), round(3.41 * 72), "Etage 1 Appartement 6")

        # Insérer "Code postal"
        # (Chiffre 1)
        can_1.drawString(round(1.65 * 72), round(3.12 * 72), "9")
        # (Chiffre 2)
        can_1.drawString(round(1.86 * 72), round(3.12 * 72), "3")
        # (Chiffre 3)
        can_1.drawString(round(2.07 * 72), round(3.12 * 72), "8")
        # (Chiffre 4)
        can_1.drawString(round(2.28 * 72), round(3.12 * 72), "0")
        # (Chiffre 5)
        can_1.drawString(round(2.49 * 72), round(3.12 * 72), "0")

        # Insérer "Commune"
        can_1.drawString(round(3.71 * 72), round(3.1 * 72), "Epiany-sur-Seine")

        # Insérer "Pays"
        can_1.drawString(round(1.2 * 72), round(2.82 * 72), "France")

        # "Vous agissez en qualité de"
        # Insérer "Vous agissez en qualité de"
        can_1.drawString(round(2.7 * 72), round(1.81 * 72), "Représentant légal")

        # Cocher la case "De" pour Madame
        can_1.drawString(round(0.64 * 72), round(1.22 * 72), "X")

        # Cocher la case "De" pour Monsieur
        can_1.drawString(round(2.61 * 72), round(1.22 * 72), "X")

        # Insérer "Votre nom de famille (nom de naissance)"
        can_1.drawString(round(3.64 * 72), round(0.95 * 72), "")

        # Insérer "Votre nom d'usage (exemple : nom d'époux / d'épouse)"
        can_1.drawString(round(4.6 * 72), round(0.7 * 72), "")

        can_1.save()

        # move to the beginning of the StringIO buffer
        packet_1.seek(0)
        new_pdf_1 = PdfFileReader(packet_1)

        # add the "watermark" of packet 1 on the page 1
        page_1 = original_pdf.getPage(0)
        page_1.mergePage(new_pdf_1.getPage(0))
        filled_pdf.addPage(page_1)
        # Page 1

        # Page 2
        packet_2 = io.BytesIO()

        # create a new PDF with Reportlab
        can_2 = canvas.Canvas(packet_2, pagesize=letter)

        can_2.setFontSize(8)

        # Insérer "Vos prénoms"
        can_2.drawString(round(1.62 * 72), round(10.9 * 72), "")

        # Insérer "Vos date et lieu de naissance"
        # (chiffre 1 du jour)
        can_2.drawString(round(2.85 * 72), round(10.64 * 72), "")
        # (chiffre 2 du jour)
        can_2.drawString(round(3.05 * 72), round(10.64 * 72), "")
        # (chiffre 1 du mois)
        can_2.drawString(round(3.26 * 72), round(10.64 * 72), "")
        # (chiffre 2 du mois)
        can_2.drawString(round(3.47 * 72), round(10.64 * 72), "")
        # (chiffre 1 de l'année)
        can_2.drawString(round(3.68 * 72), round(10.64 * 72), "")
        # (chiffre 2 de l'année)
        can_2.drawString(round(3.89 * 72), round(10.64 * 72), "")
        # (chiffre 3 de l'année)
        can_2.drawString(round(4.1 * 72), round(10.64 * 72), "")
        # (chiffre 4 de l'année)
        can_2.drawString(round(4.31 * 72), round(10.64 * 72), "")
        # (à)
        can_2.drawString(round(0.85 * 72), round(10.38 * 72), "Saint-Louis (97450)")

        # Insérer "Sa (ou ses) nationalité(s)"
        can_2.drawString(round(2.49 * 72), round(10.05 * 72), "Française")

        # Insérer "Sa profession"
        can_2.drawString(round(1.7 * 72), round(9.8 * 72), "Président")

        # Insérer "Son adresse"
        can_2.drawString(round(1.6 * 72), round(9.5 * 72), "")

        # Insérer "Complément d'adresse"
        can_2.drawString(round(2.37 * 72), round(9.25 * 72), "Etage 1 Appartement 6")

        # Insérer "Code postal"
        # (Chiffre 1)
        can_2.drawString(round(1.65 * 72), round(8.95 * 72), "9")
        # (Chiffre 2)
        can_2.drawString(round(1.86 * 72), round(8.95 * 72), "3")
        # (Chiffre 3)
        can_2.drawString(round(2.07 * 72), round(8.95 * 72), "8")
        # (Chiffre 4)
        can_2.drawString(round(2.28 * 72), round(8.95 * 72), "0")
        # (Chiffre 5)
        can_2.drawString(round(2.49 * 72), round(8.95 * 72), "0")

        # Insérer "Commune"
        can_2.drawString(round(3.73 * 72), round(8.95 * 72), "Epinay-sur-Seine")

        # Insérer "Pays"
        can_2.drawString(round(1.15 * 72), round(8.65 * 72), "France")

        # Si vous agissez en qualité de représentant légal d’une personne morale :
        # Insérer "Forme juridique de la société (SA, SARL, SAS, SNC, EURL, Association, …)"
        can_2.drawString(round(5.80 * 72), round(7.94 * 72), "SASU à capital variable")

        # Insérer "Sa dénomination"
        can_2.drawString(round(1.95 * 72), round(7.63 * 72), "HOLOMORPHE")

        # Insérer "L’adresse du siège social"
        can_2.drawString(round(2.56 * 72), round(7.37 * 72), "31 Avenue de Ségur")

        # Insérer "Complément d’adresse"
        can_2.drawString(round(2.51 * 72), round(7.09 * 72), "ABC Liv")

        # Insérer "Code postal"
        # (Chiffre 1)
        can_2.drawString(round(1.65 * 72), round(6.83 * 72), "7")
        # (Chiffre 2)
        can_2.drawString(round(1.86 * 72), round(6.83 * 72), "5")
        # (Chiffre 3)
        can_2.drawString(round(2.07 * 72), round(6.83 * 72), "0")
        # (Chiffre 4)
        can_2.drawString(round(2.28 * 72), round(6.83 * 72), "0")
        # (Chiffre 5)
        can_2.drawString(round(2.49 * 72), round(6.83 * 72), "7")

        # Insérer "Commune"
        can_2.drawString(round(3.69 * 72), round(6.83 * 72), "Paris")

        # Insérer "Pays"
        can_2.drawString(round(1.15 * 72), round(6.55 * 72), "France")

        # Insérer "Juridiction saisie"
        can_2.drawString(round(2.14 * 72), round(4.93 * 72), "Tribunal de Paris")

        # Insérer "N° Portalis (exemple : DCCN-2-BOC-KK) ou n° du répertoire général"
        can_2.drawString(round(5.61 * 72), round(4.65 * 72), "DCCN-2-BOC-KK")

        # Cocher la case "J’accepte que la procédure référencée ci-dessous se déroule sans audience"
        can_2.drawString(round(0.64 * 72), round(2.28 * 72), "X")

        can_2.save()

        # move to the beginning of the StringIO buffer
        packet_2.seek(0)
        new_pdf_2 = PdfFileReader(packet_2)

        # add the "watermark" of packet 2 on the page 2
        page_2 = original_pdf.getPage(1)
        page_2.mergePage(new_pdf_2.getPage(0))
        filled_pdf.addPage(page_2)
        # Page 2

        # Page 3
        packet_3 = io.BytesIO()

        can_3 = canvas.Canvas(packet_3, pagesize=letter)

        can_3.setFontSize(8)

        # Insérer "Je soussigné(e) (prénom, nom)"
        can_3.drawString(round(2.91 * 72), round(10.17 * 72), "")

        # Insérer "Fait à"
        can_3.drawString(round(1.2 * 72), round(9.55 * 72), "Epinay-sur-Seine (93800)")

        # Insérer "Le"
        # (chiffre 1 du jour)
        can_3.drawString(round(4.36 * 72), round(9.56 * 72), dt.today().strftime("%d")[0])
        # (chiffre 2 du jour)
        can_3.drawString(round(4.51 * 72), round(9.56 * 72), dt.today().strftime("%d")[1])
        # (chiffre 1 du mois)
        can_3.drawString(round(4.7 * 72), round(9.56 * 72), dt.today().strftime("%m")[0])
        # (chiffre 2 du mois)
        can_3.drawString(round(4.86 * 72), round(9.56 * 72), dt.today().strftime("%m")[1])
        # (chiffre 1 de l'année)
        can_3.drawString(round(5.03 * 72), round(9.56 * 72), dt.today().strftime("%Y")[0])
        # (chiffre 2 de l'année)
        can_3.drawString(round(5.19 * 72), round(9.56 * 72), dt.today().strftime("%Y")[1])
        # (chiffre 3 de l'année)
        can_3.drawString(round(5.36 * 72), round(9.56 * 72), dt.today().strftime("%Y")[2])
        # (chiffre 4 de l'année)
        can_3.drawString(round(5.52 * 72), round(9.56 * 72), dt.today().strftime("%Y")[3])

        can_3.save()

        # move to the beginning of the StringIO buffer
        packet_3.seek(0)
        new_pdf_3 = PdfFileReader(packet_3)

        # add the "watermark" of packet 3 on the page 3
        page_3 = original_pdf.getPage(2)
        page_3.mergePage(new_pdf_3.getPage(0))
        filled_pdf.addPage(page_3)
        # Page 3

        # finally, write "output" to a real file
        output_file = "Fictif\\Cerfa_16037_" + dt.today().strftime('%d_%m_%Y') + ".pdf"
        output_stream = open(output_file, "wb")
        filled_pdf.write(output_stream)
        output_stream.close()

        try:
            signature = "A:\\2_Personnel\\2_Non_Recurrentes\\62_Sign\\ma_signature_v2.png"

            pdf = PdfFileReader(open(output_file, 'rb'))

            page_number = pdf.getNumPages()

            x_coord = round(0.7 * 72)

            y_coord = round(8.5 * 72)

            width = 100

            height = round(0.55 * 72)

            os.system("signpdf " + str(output_file) + " " + str(signature) + " --coords " + str(page_number) + "x"
                      + str(x_coord) + "x" + str(y_coord) + "x" + str(width) + "x" + str(height))
        except Exception as e:
            print("error : " + str(e))


if __name__ == '__main__':
    unittest.main()
