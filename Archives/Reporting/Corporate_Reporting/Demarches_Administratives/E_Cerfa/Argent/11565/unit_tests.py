import unittest
from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from datetime import datetime as dt
import os


class UnitTestsECerfa11565(unittest.TestCase):
    def test_cerfa_11565_terrains_villaines_sous_bois(self):
        packet = io.BytesIO()

        # Nom, prénom ou dénomination sociale du demandeur
        nom_prenom_denomination_sociale_demandeur = "Monsieur ALOYAU Jason"

        # Adresse du demandeur
        adresse_demandeur = "6 Avenue Léon Blum - Etage 1 Appartement 6"

        # Code postal du demandeur
        code_postal_demandeur = "93800"

        # Commune du demandeur
        commune_demandeur = "Epinay-sur-Seine"

        # Section des références cadastrales
        section_references_cadastrales = "A"

        # Numéro de plan des références cadastrales
        numero_de_plan_references_cadastrales = "279"

        # Adresse de la parcelle des références cadastrales
        adresse_parcelle_references_cadastrales = "25 Rue de Villiers le Sec"

        # create a new PDF with Reportlab
        can = canvas.Canvas(packet, pagesize=letter)
        can.setFontSize(8)

        # Insérer le nom, prénom ou dénomination sociale du demandeur
        can.drawString(round(2.99 * 72), round(9.47 * 72), nom_prenom_denomination_sociale_demandeur)

        # Insérer l'adresse du demandeur
        can.drawString(round(2.99 * 72), round(9.08 * 72), adresse_demandeur)

        # Insérer le code postal du demandeur
        can.drawString(round(3 * 72), round(8.84 * 72), code_postal_demandeur[0])
        can.drawString(round(3.25 * 72), round(8.84 * 72), code_postal_demandeur[1])
        can.drawString(round(3.5 * 72), round(8.84 * 72), code_postal_demandeur[2])
        can.drawString(round(3.75 * 72), round(8.84 * 72), code_postal_demandeur[3])
        can.drawString(round(4 * 72), round(8.84 * 72), code_postal_demandeur[4])

        # Insérer la commune du demandeur
        can.drawString(round(4.35 * 72), round(8.84 * 72), commune_demandeur)

        # Insérer le "Le cas échéant, mandaté par : "
        can.drawString(round(3 * 72), round(8.55 * 72), "")

        # Insérer le département de la "Situation du (des) bien(s)"
        can.drawString(round(3.5 * 72), round(7.71 * 72), "Val d'Oise (95)")

        # Insérer la commune ou arrondissement de la "Situation du (des) bien(s)"
        can.drawString(round(3.5 * 72), round(7.4 * 72), "Villaines-sous-Bois (95570)")

        # Insérer la section des références cadastrales
        can.drawString(round(0.7 * 72), round(6.5 * 72), section_references_cadastrales)

        # Insérer le numéro de plan des références cadastrales
        can.drawString(round(2.42 * 72), round(6.5 * 72), numero_de_plan_references_cadastrales)

        # Insérer l'adresse de la parcelle des références cadastrales
        can.drawString(round(4.3 * 72), round(6.5 * 72), adresse_parcelle_references_cadastrales)

        # Insérer le(s) lot(s) de copropriété des références cadastrales
        can.drawString(round(2.46 * 72), round(6.13 * 72), "")

        # Cocher la case "seule titulaire de droits sur le(s) bien(s)"
        can.drawString(round(0.63 * 72), round(5.66 * 72), "X")

        # Cocher la case "titulaire avec d'autres personnes de droits sur le bien"
        can.drawString(round(0.63 * 72), round(5.47 * 72), "X")

        # Insérer le jour de la date de signature
        can.drawString(round(4.57 * 72), round(1.62 * 72), dt.today().strftime('%d'))

        # Insérer le mois de la date de signature
        can.drawString(round(5.08 * 72), round(1.62 * 72), dt.today().strftime('%m'))

        # Insérer l'année de la date de signature
        can.drawString(round(5.57 * 72), round(1.62 * 72), dt.today().strftime('%Y'))

        can.save()

        # move to the beginning of the StringIO buffer
        packet.seek(0)
        new_pdf = PdfFileReader(packet)

        # read your existing PDF
        existing_pdf = PdfFileReader(open("Cerfa_11565.pdf", "rb"))

        output = PdfFileWriter()

        # add the "watermark" (which is the new pdf) on the existing page
        page = existing_pdf.getPage(0)
        page.mergePage(new_pdf.getPage(0))
        output.addPage(page)

        # finally, write "output" to a real file
        output_file = "Terrains_Villaines_Sous_Bois\\Cerfa_11565_T_VSB_" + section_references_cadastrales + "_" \
                      + numero_de_plan_references_cadastrales + "_" + dt.today().strftime('%d_%m_%Y') + ".pdf"
        output_stream = open(output_file, "wb")
        output.write(output_stream)
        output_stream.close()

        try:
            signature = "A:\\2_Personnel\\2_Non_Recurrentes\\62_Sign\\ma_signature_v2.png"

            pdf = PdfFileReader(open(output_file, 'rb'))

            page_number = pdf.getNumPages()

            x_coord = round(6.25 * 72)

            y_coord = round(0.8 * 72)

            width = 100

            height = round(0.55 * 72)

            os.system("signpdf " + str(output_file) + " " + str(signature) + " --coords " + str(page_number) + "x"
                      + str(x_coord) + "x" + str(y_coord) + "x" + str(width) + "x" + str(height))
        except Exception as e:
            print("error : " + str(e))

    def test_cerfa_11565_terrains_viarmes(self):
        packet = io.BytesIO()

        # Nom, prénom ou dénomination sociale du demandeur
        nom_prenom_denomination_sociale_demandeur = "Monsieur ALOYAU Jason"

        # Adresse du demandeur
        adresse_demandeur = "6 Avenue Léon Blum - Etage 1 Appartement 6"

        # Code postal du demandeur
        code_postal_demandeur = "93800"

        # Commune du demandeur
        commune_demandeur = "Epinay-sur-Seine"

        # Section des références cadastrales
        section_references_cadastrales = "E"

        # Numéro de plan des références cadastrales
        numero_de_plan_references_cadastrales = "199"

        # Adresse de la parcelle des références cadastrales
        adresse_parcelle_references_cadastrales = "5 le grand sentier"

        # create a new PDF with Reportlab
        can = canvas.Canvas(packet, pagesize=letter)
        can.setFontSize(8)

        # Insérer le nom, prénom ou dénomination sociale du demandeur
        can.drawString(round(2.99 * 72), round(9.47 * 72), nom_prenom_denomination_sociale_demandeur)

        # Insérer l'adresse du demandeur
        can.drawString(round(2.99 * 72), round(9.08 * 72), adresse_demandeur)

        # Insérer le code postal du demandeur
        can.drawString(round(3 * 72), round(8.84 * 72), code_postal_demandeur[0])
        can.drawString(round(3.25 * 72), round(8.84 * 72), code_postal_demandeur[1])
        can.drawString(round(3.5 * 72), round(8.84 * 72), code_postal_demandeur[2])
        can.drawString(round(3.75 * 72), round(8.84 * 72), code_postal_demandeur[3])
        can.drawString(round(4 * 72), round(8.84 * 72), code_postal_demandeur[4])

        # Insérer la commune du demandeur
        can.drawString(round(4.35 * 72), round(8.84 * 72), commune_demandeur)

        # Insérer le "Le cas échéant, mandaté par : "
        can.drawString(round(3 * 72), round(8.55 * 72), "")

        # Insérer le département de la "Situation du (des) bien(s)"
        can.drawString(round(3.5 * 72), round(7.71 * 72), "Val d'Oise (95)")

        # Insérer la commune ou arrondissement de la "Situation du (des) bien(s)"
        can.drawString(round(3.5 * 72), round(7.4 * 72), "Viarmes (95270)")

        # Insérer la section des références cadastrales
        can.drawString(round(0.7 * 72), round(6.5 * 72), section_references_cadastrales)

        # Insérer le numéro de plan des références cadastrales
        can.drawString(round(2.42 * 72), round(6.5 * 72), numero_de_plan_references_cadastrales)

        # Insérer l'adresse de la parcelle des références cadastrales
        can.drawString(round(4.3 * 72), round(6.5 * 72), adresse_parcelle_references_cadastrales)

        # Insérer le(s) lot(s) de copropriété des références cadastrales
        can.drawString(round(2.46 * 72), round(6.13 * 72), "")

        # Cocher la case "seule titulaire de droits sur le(s) bien(s)"
        can.drawString(round(0.63 * 72), round(5.66 * 72), "X")

        # Cocher la case "titulaire avec d'autres personnes de droits sur le bien"
        can.drawString(round(0.63 * 72), round(5.47 * 72), "X")

        # Insérer le jour de la date de signature
        can.drawString(round(4.57 * 72), round(1.62 * 72), dt.today().strftime('%d'))

        # Insérer le mois de la date de signature
        can.drawString(round(5.08 * 72), round(1.62 * 72), dt.today().strftime('%m'))

        # Insérer l'année de la date de signature
        can.drawString(round(5.57 * 72), round(1.62 * 72), dt.today().strftime('%Y'))

        can.save()

        # move to the beginning of the StringIO buffer
        packet.seek(0)
        new_pdf = PdfFileReader(packet)

        # read your existing PDF
        existing_pdf = PdfFileReader(open("Cerfa_11565.pdf", "rb"))

        output = PdfFileWriter()

        # add the "watermark" (which is the new pdf) on the existing page
        page = existing_pdf.getPage(0)
        page.mergePage(new_pdf.getPage(0))
        output.addPage(page)

        # finally, write "output" to a real file
        output_file = "Viarmes\\Cerfa_11565_T_95270_" + section_references_cadastrales + "_" \
                      + numero_de_plan_references_cadastrales + "_" + dt.today().strftime('%d_%m_%Y') + ".pdf"
        output_stream = open(output_file, "wb")
        output.write(output_stream)
        output_stream.close()

        try:
            signature = "A:\\2_Personnel\\2_Non_Recurrentes\\62_Sign\\ma_signature_v2.png"

            pdf = PdfFileReader(open(output_file, 'rb'))

            page_number = pdf.getNumPages()

            x_coord = round(6.25 * 72)

            y_coord = round(0.8 * 72)

            width = 100

            height = round(0.55 * 72)

            os.system("signpdf " + str(output_file) + " " + str(signature) + " --coords " + str(page_number) + "x"
                      + str(x_coord) + "x" + str(y_coord) + "x" + str(width) + "x" + str(height))
        except Exception as e:
            print("error : " + str(e))


if __name__ == '__main__':
    unittest.main()
