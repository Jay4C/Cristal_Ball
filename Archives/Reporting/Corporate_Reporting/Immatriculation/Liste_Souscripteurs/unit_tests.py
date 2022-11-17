import unittest
from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from datetime import datetime as dt
import os


class UnitTestsListeSouscripteurs(unittest.TestCase):
    def test_liste_souscripteurs_mercorus(self):
        packet = io.BytesIO()

        # create a new PDF with Reportlab
        can = canvas.Canvas(packet, pagesize=letter)
        can.setFontSize(8)

        # Insérer la Dénomination
        can.drawString(round(2.09 * 72), round(10.55 * 72), "MERCORUS")

        # Insérer la Forme juridique
        can.drawString(round(2.18 * 72), round(10.24 * 72), "Société par actions simplifiée unipersonnelle à capital variable")

        # Insérer le Capital - 1
        can.drawString(round(1.58 * 72), round(9.95 * 72), "100,00 Euros")

        # Insérer le Siège social
        can.drawString(round(1.91 * 72), round(9.64 * 72), "10 rue de Penthièvre 75008 Paris")

        # Insérer le Capital - 2
        can.drawString(round(4.44 * 72), round(8.68 * 72), "100,00 Euros")

        # Insérer le Nombre d'actions
        can.drawString(round(4.84 * 72), round(8.36 * 72), "50")

        # Insérer la Valeur nominale
        can.drawString(round(4.77 * 72), round(8.06 * 72), "2,00 Euros")

        # Premier souscripteur
        # Insérer le Nom, Prénom et Adresse des Souscripteurs
        can.drawString(round(1.08 * 72), round(6.6 * 72), " / ")
        can.drawString(round(1.08 * 72), round(6.45 * 72), " Etage 1 Appartement 6")
        can.drawString(round(1.08 * 72), round(6.25 * 72), "93800 Epinay-sur-Seine")

        # Insérer le Nombre d'actions souscrites
        can.drawString(round(3.95 * 72), round(6.41 * 72), "50")

        # Insérer la Valeur nominale des actions souscrites
        can.drawString(round(5.1 * 72), round(6.41 * 72), "2,00 Euros")

        # Insérer le Montant des versements
        can.drawString(round(6.4 * 72), round(6.41 * 72), "100,00 Euros")
        # Premier souscripteur

        # Insérer le Total des actions souscrites
        can.drawString(round(3.95 * 72), round(4.18 * 72), "50")

        # Insérer le Total des versements
        can.drawString(round(6.4 * 72), round(3.79 * 72), "100,00 Euros")

        # Insérer le Nom de la société
        can.drawString(round(1.01 * 72), round(2.87 * 72), "Société par actions simplifiée unipersonnelle à capital variable MERCORUS")

        # Insérer la somme de versement
        can.drawString(round(3.93 * 72), round(2.55 * 72), "100,00 Euros")

        # Insérer le certificateur
        can.drawString(round(5.68 * 72), round(2.27 * 72), "onsieur ALOYAU Jason")
        can.drawString(round(1.01 * 72), round(2 * 72), ", Président de la société par actions simplifiée "
                                                        "unipersonnelle à capital variable MERCORUS en formation.")

        # Insérer le lieu de signature
        can.drawString(round(4.59 * 72), round(1.65 * 72), "Epinay-sur-Seine (93800)")

        # Insérer le jour de la date de signature
        can.drawString(round(4.38 * 72), round(1.33 * 72), dt.today().strftime('%d'))

        # Insérer le mois de la date de signature
        can.drawString(round(4.84 * 72), round(1.33 * 72), dt.today().strftime('%m'))

        # Insérer l'année de la date de signature
        can.drawString(round(5.30 * 72), round(1.33 * 72), dt.today().strftime('%Y'))

        can.save()

        # move to the beginning of the StringIO buffer
        packet.seek(0)
        new_pdf = PdfFileReader(packet)

        # read your existing PDF
        existing_pdf = PdfFileReader(open("Liste_Souscripteurs.pdf", "rb"))

        output = PdfFileWriter()

        # add the "watermark" (which is the new pdf) on the existing page
        page = existing_pdf.getPage(0)
        page.mergePage(new_pdf.getPage(0))
        output.addPage(page)

        # finally, write "output" to a real file
        output_file = "Mercorus\\Liste_Souscripteurs_" + dt.today().strftime('%d_%m_%Y') + ".pdf"
        output_stream = open(output_file, "wb")
        output.write(output_stream)
        output_stream.close()

        try:
            signature = "A:\\2_Personnel\\2_Non_Recurrentes\\62_Sign\\ma_signature_v2.png"

            pdf = PdfFileReader(open(output_file, 'rb'))

            page_number = pdf.getNumPages()

            x_coord = round(4.15 * 72)

            y_coord = round(0.6 * 72)

            width = 100

            height = round(0.55 * 72)

            os.system("signpdf " + str(output_file) + " " + str(signature) + " --coords " + str(page_number) + "x"
                      + str(x_coord) + "x" + str(y_coord) + "x" + str(width) + "x" + str(height))
        except Exception as e:
            print("error : " + str(e))


if __name__ == '__main__':
    unittest.main()
