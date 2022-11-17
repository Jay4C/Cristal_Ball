import unittest
from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from datetime import datetime as dt
import os, shutil

annee = "Annee_2021"

exercice = "2_Exercice_01_01_2021__31_12_2021"

exercice_clos_le = "31 décembre 2021"


class UnitTestsDeclarationConfidentialiteComptesAnnuels(unittest.TestCase):
    # ok
    def test_declaration_confidentialite_comptes_annuels_holomorphe(self):
        packet = io.BytesIO()

        # create a new PDF with Reportlab
        can = canvas.Canvas(packet, pagesize=letter)
        can.setFontSize(8)

        # Insérer la dénomination de la société
        can.drawString(
            round(1.1 * 72),
            round(8.57 * 72),
            "HOLOMORPHE, société par actions simplifiée unipersonnelle à capital variable de 100 Euros"
        )
        can.drawString(
            round(3.1 * 72),
            round(8.38 * 72),
            "SIREN : 883632556 \ Siège social : 31 Avenue de Ségur 75007 PARIS"
        )
        can.drawString(
            round(1.1 * 72),
            round(8 * 72),
            "Monsieur , Président de la S.A.S.U.A.C.V. HOLOMORPHE"
        )

        # Insérer la date de clôture de l'exercice
        can.drawString(
            round(4.83 * 72),
            round(7.25 * 72),
            exercice_clos_le
        )

        # Insérer la date de signature et le lieu de signature
        can.drawString(
            round(1.7 * 72),
            round(4 * 72),
            "Paris (75007)"
        )
        can.drawString(
            round(4.6 * 72),
            round(4 * 72),
            dt.today().strftime('%d/%m/%Y')
        )

        can.save()

        # move to the beginning of the StringIO buffer
        packet.seek(0)
        new_pdf = PdfFileReader(packet)

        # read your existing PDF
        existing_pdf = PdfFileReader(open("D_C_C_A.pdf", "rb"))

        output = PdfFileWriter()

        # add the "watermark" (which is the new pdf) on the existing page
        page = existing_pdf.getPage(0)
        page.mergePage(new_pdf.getPage(0))
        output.addPage(page)

        # finally, write "output" to a real file
        output_file = "Holomorphe\\" \
                      + annee \
                      + "\\Declaration_Confidentialite_Comptes_Annuels_" \
                      + dt.today().strftime('%d_%m_%Y') \
                      + "_" + annee \
                      + "_HOLOMORPHE.pdf"
        output_stream = open(output_file, "wb")
        output.write(output_stream)
        output_stream.close()

        try:
            signature = "A:\\2_Personnel\\2_Non_Recurrentes\\62_Sign\\ma_signature_v2.png"

            pdf = PdfFileReader(open(output_file, 'rb'))

            page_number = pdf.getNumPages()

            x_coord = round(1.25 * 72)

            y_coord = round(2.97 * 72)

            width = 100

            height = round(0.55 * 72)

            os.system("signpdf " + str(output_file) + " " + str(signature) + " --coords " + str(page_number) + "x"
                      + str(x_coord) + "x" + str(y_coord) + "x" + str(width) + "x" + str(height))
        except Exception as e:
            print("error : " + str(e))

        # declaration_conformite
        declaration_conformite_folder = "Holomorphe\\" + annee

        declaration_conformite_folder_files = os.listdir(declaration_conformite_folder)

        declaration_conformite_filename = ""

        for f in declaration_conformite_folder_files:
            if "signed" in f:
                declaration_conformite_filename += f
                print("declaration_conformite_filename : " + declaration_conformite_filename)
                break

        declaration_conformite = declaration_conformite_folder + "\\" + declaration_conformite_filename

        shutil.copy(
            declaration_conformite,
            "A:\\1_Professionnel\\1_Holomorphe\\1_Administration\\2_Gestion_Declarations_Administratives"
            "\\1_Recurrentes\\5_Infogreffe\\4_Approbation_Comptes_Sociaux\\"
            + exercice
            + "\\Declaration_Confidentialite_Comptes_Annuels_"
            + annee
            + "_HOLOMORPHE.pdf"
        )


if __name__ == '__main__':
    unittest.main()
