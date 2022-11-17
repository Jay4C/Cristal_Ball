import unittest
from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from datetime import datetime as dt
import os


class UnitTestsDeclarationNonCondamnation(unittest.TestCase):
    def test_declaration_non_condamnation_mercorus(self):
        packet = io.BytesIO()

        # create a new PDF with Reportlab
        can = canvas.Canvas(packet, pagesize=letter)
        can.setFontSize(8)

        # Insérer le nom
        can.drawString(round(1.56 * 72), round(8.3 * 72), "")

        # Insérer les prénoms
        can.drawString(round(1.56 * 72), round(8.02 * 72), "")

        # Insérer le docmicile
        can.drawString(round(1.56 * 72), round(7.61 * 72), " Etage 1 Appartement 6 93800 Epinay-sur-Seine")

        # Insérer la date de naissance
        can.drawString(round(1.39 * 72), round(7.32 * 72), "")

        # Insérer le lieu de naissance
        can.drawString(round(3.58 * 72), round(7.32 * 72), "Saint-Louis (97450)")

        # Rayer la mention inutile
        can.drawString(round(1 * 72), round(6.94 * 72), "XXXXX")

        # Insérer le nom du père et prénoms
        can.drawString(round(2.02 * 72), round(6.94 * 72), "")

        # Insérer le nom de naissance de la mère et prénoms
        can.drawString(round(1.32 * 72), round(6.59 * 72), "")

        # Insérer le lieu de signature
        can.drawString(round(1.80 * 72), round(4.85 * 72), "Epinay-sur-Seine (93800)")

        # Insérer la date de signature
        can.drawString(round(5.60 * 72), round(4.85 * 72), dt.today().strftime('%d/%m/%Y'))

        can.save()

        # move to the beginning of the StringIO buffer
        packet.seek(0)
        new_pdf = PdfFileReader(packet)

        # read your existing PDF
        existing_pdf = PdfFileReader(open("Declaration_Non_Condamnation.pdf", "rb"))

        output = PdfFileWriter()

        # add the "watermark" (which is the new pdf) on the existing page
        page = existing_pdf.getPage(0)
        page.mergePage(new_pdf.getPage(0))
        output.addPage(page)

        # finally, write "output" to a real file
        output_file = "Mercorus\\Declaration_Non_Condamnation_" + dt.today().strftime('%d_%m_%Y') + ".pdf"
        output_stream = open(output_file, "wb")
        output.write(output_stream)
        output_stream.close()

        try:
            signature = "A:\\2_Personnel\\2_Non_Recurrentes\\62_Sign\\ma_signature_v2.png"

            pdf = PdfFileReader(open(output_file, 'rb'))

            page_number = pdf.getNumPages()

            x_coord = round(4.43 * 72)

            y_coord = round(3.89 * 72)

            width = 100

            height = round(0.55 * 72)

            os.system("signpdf " + str(output_file) + " " + str(signature) + " --coords " + str(page_number) + "x"
                      + str(x_coord) + "x" + str(y_coord) + "x" + str(width) + "x" + str(height))
        except Exception as e:
            print("error : " + str(e))


if __name__ == '__main__':
    unittest.main()
