import unittest
from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from datetime import datetime as dt
import os, shutil

annee = "Annee_2021"

exercice = "2_Exercice_01_01_2021__31_12_2021"


class UnitTestsAttestationConformiteDocumentsComptables(unittest.TestCase):
    # ok
    def test_remplir_attestation_conformite_documents_comptables_holomorphe(self):
        packet = io.BytesIO()

        # create a new PDF with Reportlab
        can = canvas.Canvas(packet, pagesize=letter)
        can.setFontSize(8)

        # Insérer les informations de la société
        can.drawString(
            round(1 * 72),
            round(10.2 * 72),
            "HOLOMORPHE, société par actions simplifiée unipersonnelle à capital variable de 100 Euros"
        )
        can.drawString(
            round(1 * 72),
            round(10 * 72),
            "Siège social : 31 Avenue de Ségur 75007 PARIS / SIREN : 883632556"
        )
        can.drawString(
            round(1 * 72),
            round(9.8 * 72),
            "Code NAF/APE : 4675Z (commerce de gros (commerce interentreprises) de produits chimiques)"
        )

        # Cocher la case 'par son représentant légal (Qualité et identité)'
        can.drawString(
            round(1.03 * 72),
            round(9.22 * 72),
            "X"
        )

        # Insérer la qualité et l'identité du représentant légal
        can.drawString(
            round(4.57 * 72),
            round(9.22 * 72),
            "Monsieur , Président de la S.A.S.U.A.C.V. HOLOMORPHE"
        )

        # Insérer le nom
        can.drawString(
            round(1.7 * 72),
            round(6.94 * 72),
            ""
        )

        # Insérer le prénom
        can.drawString(
            round(1.7 * 72),
            round(6.75 * 72),
            ""
        )

        # Insérer l'adresse
        can.drawString(
            round(2.97 * 72),
            round(6.57 * 72),
            " - Etage 1 Appartement 6 - 93800 Epinay-sur-Seine"
        )

        # Insérer la date de signature et le lieu de signature
        can.drawString(
            round(1 * 72),
            round(5.2 * 72),
            "Fait à Paris (75007), le " + dt.today().strftime('%d/%m/%Y') + "."
        )

        can.save()

        # move to the beginning of the StringIO buffer
        packet.seek(0)
        new_pdf = PdfFileReader(packet)

        # read your existing PDF
        existing_pdf = PdfFileReader(open("Conformite_Comptables.pdf", "rb"))

        output = PdfFileWriter()

        # add the "watermark" (which is the new pdf) on the existing page
        page = existing_pdf.getPage(0)
        page.mergePage(new_pdf.getPage(0))
        output.addPage(page)

        # finally, write "output" to a real file
        output_file = "Holomorphe\\" \
                      + annee \
                      + "\\Conformite_Comptables_" \
                      + dt.today().strftime('%d_%m_%Y') \
                      + annee \
                      + "_HOLOMORPHE.pdf"
        output_stream = open(output_file, "wb")
        output.write(output_stream)
        output_stream.close()

        try:
            signature = "A:\\2_Personnel\\2_Non_Recurrentes\\62_Sign\\ma_signature_v2.png"

            pdf = PdfFileReader(open(output_file, 'rb'))

            page_number = pdf.getNumPages()

            x_coord = round(1 * 72)

            y_coord = round(4.4 * 72)

            width = 100

            height = round(0.55 * 72)

            os.system("signpdf " + str(output_file) + " " + str(signature) + " --coords " + str(page_number) + "x"
                      + str(x_coord) + "x" + str(y_coord) + "x" + str(width) + "x" + str(height))
        except Exception as e:
            print("error : " + str(e))

        # conformite_comptables
        conformite_comptables_folder = "Holomorphe\\" + annee

        conformite_comptables_folder_files = os.listdir(conformite_comptables_folder)

        conformite_comptables_filename = ""

        for f in conformite_comptables_folder_files:
            if "signed" in f:
                conformite_comptables_filename += f
                print("conformite_comptables_filename : " + conformite_comptables_filename)
                break

        conformite_comptables = conformite_comptables_folder + "\\" + conformite_comptables_filename

        shutil.copy(
            conformite_comptables,
            "A:\\1_Professionnel\\1_Holomorphe\\1_Administration\\2_Gestion_Declarations_Administratives"
            "\\1_Recurrentes\\5_Infogreffe\\4_Approbation_Comptes_Sociaux\\"
            + exercice
            + "\\Conformite_Comptables_"
            + annee
            + "_HOLOMORPHE.pdf"
        )


if __name__ == '__main__':
    unittest.main()
