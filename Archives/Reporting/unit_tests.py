import io
import unittest
from PyPDF2 import PdfFileReader, PdfFileWriter
import os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from datetime import datetime


class UnitTestsReporting(unittest.TestCase):
    def test_display_the_number_of_pages_from_pdf_file(self):
        print('test_display_the_number_of_pages_from_pdf_file')

        pdf = PdfFileReader(open('Corporate_Reporting\\Bilan\\Bilan\\Bilan_S_D.pdf', 'rb'))

        print('The Bilan_S_D.pdf has : ' + str(pdf.getNumPages()) + ' pages.')

    def test_place_my_first_signature_on_the_last_page_of_one_pdf_file(self):
        print('test_place_my_signature_on_the_last_page_of_one_pdf_file')

        filename = "A:\\1_Professionnel\\1_Holomorphe\\2_Archives\\2_Outils_Numeriques\\Python__Flask__Cristal_Ball\\" \
                   "Test\\Service\\Archives\\Reporting\\Corporate_Reporting\\Bilan\\Bilan\\Bilan_S_D.pdf"

        signature = "A:\\2_Personnel\\2_Non_Recurrentes\\62_Sign\\ma_signature_manuscrite.png"

        pdf = PdfFileReader(open(filename, 'rb'))

        page_number = pdf.getNumPages()

        x_coord = 4.5 * 72

        y_coord = 0.3 * 72

        width = 100

        height = 100

        os.system("signpdf " + str(filename) + " " + str(signature) + " --coords " + str(page_number) + "x"
                  + str(round(x_coord)) + "x" + str(round(y_coord)) + "x" + str(width) + "x" + str(height) + " --date")

    def test_place_my_second_signature_on_the_last_page_of_one_pdf_file(self):
        print('test_place_my_signature_on_the_last_page_of_one_pdf_file')

        filename = "A:\\1_Professionnel\\1_Holomorphe\\2_Archives\\2_Outils_Numeriques\\Python__Flask__Cristal_Ball\\" \
                   "Test\\Service\\Archives\\Reporting\\Corporate_Reporting\\Bilan\\Bilan\\Bilan_S_D.pdf"

        signature = "A:\\2_Personnel\\2_Non_Recurrentes\\62_Sign\\ma_signature_v1.png"

        pdf = PdfFileReader(open(filename, 'rb'))

        page_number = pdf.getNumPages()

        x_coord = 4.5 * 72

        y_coord = 0.3 * 72

        width = 100

        height = 50

        os.system("signpdf " + str(filename) + " " + str(signature) + " --coords " + str(page_number) + "x"
                  + str(round(x_coord)) + "x" + str(round(y_coord)) + "x" + str(width) + "x" + str(height))

    def test_add_text_on_the_last_page_of_one_pdf_file_for_date_and_location_of_one_signature(self):
        print('test_add_text_on_the_last_page_of_one_pdf_file_for_date_and_location_of_one_signature')

        packet = io.BytesIO()

        # create a new PDF with Reportlab
        can = canvas.Canvas(packet, pagesize=letter)
        can.setFontSize(8)

        x_coord = 5.9 * 72

        y_coord = 0.14 * 72

        date_of_signature = datetime.today().strftime('%d/%m/%Y')

        # Insérer la valeur "Fait à Epinay-sur-Seine (), le dd/mm/YYYY.".
        can.drawString(x_coord, y_coord, "Fait à Epinay-sur-Seine (93800), le " + date_of_signature + ".")

        # Insérer la valeur "Lu et approuvé.".
        can.drawString(x_coord, y_coord - 8, "Lu et approuvé.")

        can.save()

        # move to the beginning of the StringIO buffer
        packet.seek(0)
        new_pdf = PdfFileReader(packet)

        # read your existing PDF
        filename = "A:\\1_Professionnel\\1_Holomorphe\\2_Archives\\2_Outils_Numeriques\\Python__Flask__Cristal_Ball\\" \
                   "Test\\Service\\Archives\\Reporting\\Corporate_Reporting\\Bilan\\Bilan\\Bilan_S_D.pdf"
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
        date_of_today = datetime.today().strftime('%d_%m_%Y')
        output_stream = open(filename.split(".pdf")[0] + "_" + date_of_today + ".pdf", "wb")
        output.write(output_stream)
        output_stream.close()

    def test_add_text_and_signature_on_the_last_page_of_one_pdf_file_for_date_and_location_of_one_signature(self):
        print('test_add_text_and_signature_on_the_last_page_of_one_pdf_file_for_date_and_location_of_one_signature')

        filename = "A:\\1_Professionnel\\1_Holomorphe\\2_Archives\\2_Outils_Numeriques\\Python__Flask__Cristal_Ball\\" \
                   "Test\\Service\\Archives\\Reporting\\Corporate_Reporting\\Bilan\\Bilan\\Bilan_S_D.pdf"

        date_of_today = datetime.today().strftime('%d_%m_%Y')

        filename_to_sign = filename.split(".pdf")[0] + "_" + date_of_today + ".pdf"

        try:
            packet = io.BytesIO()

            # create a new PDF with Reportlab
            can = canvas.Canvas(packet, pagesize=letter)
            can.setFontSize(8)

            x_coord = 5.9 * 72

            y_coord = 0.14 * 72

            date_of_signature = datetime.today().strftime('%d/%m/%Y')

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

            signature = "A:\\2_Personnel\\2_Non_Recurrentes\\62_Sign\\ma_signature_v1.png"

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
