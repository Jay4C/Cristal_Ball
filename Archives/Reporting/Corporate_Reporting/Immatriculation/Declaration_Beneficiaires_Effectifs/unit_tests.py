import unittest
from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from datetime import datetime as dt
import os


class UnitTestsDeclarationBeneficiairesEffectifs(unittest.TestCase):
    def test_declaration_beneficiaires_effectifs_mercorus(self):
        packet = io.BytesIO()

        # create a new PDF with Reportlab
        can = canvas.Canvas(packet, pagesize=letter)
        can.setFontSize(8)

        # II. Informations sur le bénéficiaire effectif de la société

        # 1) Informations sur l'identité du bénéficiaire effectif :

        # Cocher la case de la civilité
        can.drawString(round(4.02 * 72), round(8.16 * 72), "X")

        # Insérer le nom de naissance
        can.drawString(round(1.73 * 72), round(8 * 72), "")

        # Insérer le nom d'usage
        can.drawString(round(1.48 * 72), round(7.82 * 72), "")

        # Insérer le pseudonyme
        can.drawString(round(5.19 * 72), round(7.82 * 72), "")

        # Insérer le prénom principal
        can.drawString(round(1.65 * 72), round(7.64 * 72), "")

        # Insérer les autres prénoms
        can.drawString(round(5.38 * 72), round(7.64 * 72), "")

        # Insérer la date de naissance
        can.drawString(round(1.17 * 72), round(7.46 * 72), "")

        # Insérer le lieu de naissance
        can.drawString(round(2 * 72), round(7.46 * 72), "Saint-Louis (97450)")

        # Insérer le département / le pays
        can.drawString(round(5.55 * 72), round(7.46 * 72), "Ile de la Réunion (974) / France")

        # Insérer la nationalité
        can.drawString(round(1.34 * 72), round(7.29 * 72), "Française")

        # Insérer l'adresse du domicile
        can.drawString(round(1.88 * 72), round(7.12 * 72), " Etage 1 Appartement 6")

        # Insérer le code postal
        can.drawString(round(1.38 * 72), round(6.94 * 72), "93800")

        # Insérer la commune
        can.drawString(round(2.48 * 72), round(6.94 * 72), "Epinay-sur-Seine")

        # Insérer le pays
        can.drawString(round(5.16 * 72), round(6.94 * 72), "France")

        # 1) Informations sur l'identité du bénéficiaire effectif :

        # 2) Informations sur les modalités du contrôle exercé par le bénéficiaire effectif sur la société

        # (R. 561-1 du code monétaire et financier)
        # Cocher la case a) Détention:
        can.drawString(round(0.85 * 72), round(6.11 * 72), "X")

        # Cocher la case (directe de plus de 25% du capital.)
        can.drawString(round(1.25 * 72), round(5.79 * 72), "X")

        # Insérer le pourcentage total du capital
        can.drawString(round(6.77 * 72), round(5.8 * 72), "100,00")

        # Cocher la case (directe de plus de 25% des droits de vote.)
        can.drawString(round(1.25 * 72), round(5.47 * 72), "X")

        # Insérer le pourcentage total des droits de vote
        can.drawString(round(6.77 * 72), round(5.46 * 72), "100,00")

        # 2) Informations sur les modalités du contrôle exercé par le bénéficiaire effectif sur la société
        # (R. 561-1 du code monétaire et financier)

        # 3) Date à laquelle la personne est devenue bénéficiaire effectif de la société :

        # Insérer la date à laquelle la personne est devenue bénéficiaire effectif de la société
        can.drawString(round(5.67 * 72), round(2.94 * 72), dt.today().strftime('%d/%m/%Y'))

        # 3) Date à laquelle la personne est devenue bénéficiaire effectif de la société :

        # II. Informations sur le bénéficiaire effectif de la société

        # III. Autres informations

        # Cocher la case (Il n'existe pas de bénéficiaire effectif autre que celui mentionné dans ce document.)
        can.drawString(round(0.95 * 72), round(2.29 * 72), "X")

        # III. Autres informations

        # Insérer le lieu de signature
        can.drawString(round(1.46 * 72), round(0.95 * 72), "Epinay-sur-Seine (93800)")

        # Insérer la date de signature
        can.drawString(round(4.28 * 72), round(0.95 * 72), dt.today().strftime('%d/%m/%Y'))

        # Insérer le Nom, prénom du représentant légal
        can.drawString(round(3.19 * 72), round(0.78 * 72), "")

        can.save()

        # move to the beginning of the StringIO buffer
        packet.seek(0)
        new_pdf = PdfFileReader(packet)

        # read your existing PDF
        existing_pdf = PdfFileReader(open("Declaration_Beneficiaires_Effectifs.pdf", "rb"))

        output = PdfFileWriter()

        # add the "watermark" (which is the new pdf) on the existing page
        page = existing_pdf.getPage(0)
        page.mergePage(new_pdf.getPage(0))
        output.addPage(page)

        # finally, write "output" to a real file
        output_file = "Mercorus\\Declaration_Beneficiaires_Effectifs_" + dt.today().strftime('%d_%m_%Y') + ".pdf"
        output_stream = open(output_file, "wb")
        output.write(output_stream)
        output_stream.close()

        try:
            signature = "A:\\2_Personnel\\2_Non_Recurrentes\\62_Sign\\ma_signature_v2.png"

            pdf = PdfFileReader(open(output_file, 'rb'))

            page_number = pdf.getNumPages()

            x_coord = round(6.67 * 72)

            y_coord = round(0.78 * 72)

            width = 100

            height = round(0.4 * 72)

            os.system("signpdf " + str(output_file) + " " + str(signature) + " --coords " + str(page_number) + "x"
                      + str(x_coord) + "x" + str(y_coord) + "x" + str(width) + "x" + str(height))
        except Exception as e:
            print("error : " + str(e))


if __name__ == '__main__':
    unittest.main()
