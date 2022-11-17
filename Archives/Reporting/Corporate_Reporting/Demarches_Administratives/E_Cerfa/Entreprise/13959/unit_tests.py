import unittest
from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from datetime import datetime as dt


class UnitTestsECerfa13959(unittest.TestCase):
    def test_rotate_e_cerfa_13959(self):
        # read your existing PDF
        original_file = PdfFileReader(open("Cerfa_13959.pdf", "rb"))

        rotate_file = PdfFileWriter()

        # Rotate all pages to the counter clockwise in 90 degrees
        for i in range(0, original_file.getNumPages()):
            rotate_file.addPage(original_file.getPage(i).rotateCounterClockwise(90))

        # finally, write "output" to a real file
        rotate_file_path = "Mercorus\\Cerfa_13959_rotate.pdf"

        with open(rotate_file_path, "wb") as rf:
            rotate_file.write(rf)

    def test_e_cerfa_13959_mercorus(self):
        print("test_e_cerfa_13959_mercorus")

        # read your existing PDF
        original_pdf = PdfFileReader(open("Cerfa_13959.pdf", "rb"))

        filled_pdf = PdfFileWriter()

        # Page 1
        packet_1 = io.BytesIO()

        # create a new PDF with Reportlab
        can_1 = canvas.Canvas(packet_1, pagesize=letter)

        can_1.setFontSize(8)

        can_1.rotate(-90)

        # Cocher la case 'Constitution d'une société commerciale'
        can_1.drawString(round(-11.05 * 72), round(7.04 * 72), "X")

        # Insérer la Dénomination
        can_1.drawString(round(- 10.11 * 72), round(6.33 * 72), "MERCORUS")

        # Cocher la case 'SAS constituée d'un associé unique,'
        can_1.drawString(round(-11.06 * 72), round(5.93 * 72), "X")

        # Cocher la case 'oui pour l'associé unique en est le président'
        can_1.drawString(round(-7.32 * 72), round(5.93 * 72), "X")

        # Insérer la durée de la personne morale
        can_1.drawString(round(-9.48 * 72), round(5.8 * 72), "Quatre-vingt-dix-neuf ans")

        # Insérer le montant et l'unité monétaire du capital
        can_1.drawString(round(-9.35 * 72), round(5.68 * 72), "100,00 Euros")

        # Insérer le minimum du capital si variable
        can_1.drawString(round(-6.75 * 72), round(5.70 * 72), "20,00 Euros")

        # Insérer la Date de clôture de l'exercice social
        can_1.drawString(round(-9.3 * 72), round(5.41 * 72), "3")
        can_1.drawString(round(-9.2 * 72), round(5.41 * 72), "1")
        can_1.drawString(round(-9.1 * 72), round(5.41 * 72), "1")
        can_1.drawString(round(-8.97 * 72), round(5.41 * 72), "2")

        # Insérer la date de clôture du 1er exercice
        can_1.drawString(round(-7.1 * 72), round(5.41 * 72), "3")
        can_1.drawString(round(-7 * 72), round(5.41 * 72), "1")
        can_1.drawString(round(-6.9 * 72), round(5.41 * 72), "1")
        can_1.drawString(round(-6.8 * 72), round(5.41 * 72), "2")
        can_1.drawString(round(-6.7 * 72), round(5.41 * 72), "2")
        can_1.drawString(round(-6.6 * 72), round(5.41 * 72), "0")
        can_1.drawString(round(-6.5 * 72), round(5.41 * 72), "2")
        can_1.drawString(round(-6.4 * 72), round(5.41 * 72), "1")

        # Insérer les principales activites de l'objet social
        can_1.drawString(round(-11.01 * 72), round(5.04 * 72), "Code APE / NAF 2441Z - Production de métaux précieux")
        can_1.drawString(round(-11.01 * 72), round(4.91 * 72), "Code APE / NAF 4672Z - Commerce de gros (commerce interentreprises) de minerais et métaux")

        # Insérer l'adresse du siège social
        can_1.drawString(round(-5.74 * 72), round(6.18 * 72), "10 rue de Penthièvre")

        # Insérer le code postal du siège social
        can_1.drawString(round(-5.1 * 72), round(6.05 * 72), "7")
        can_1.drawString(round(-5 * 72), round(6.05 * 72), "5")
        can_1.drawString(round(-4.9 * 72), round(6.05 * 72), "0")
        can_1.drawString(round(-4.8 * 72), round(6.05 * 72), "0")
        can_1.drawString(round(-4.7 * 72), round(6.05 * 72), "8")

        # Insérer la commune du siège social
        can_1.drawString(round(-3.92 * 72), round(6.06 * 72), "Paris")

        # Cocher la case 'Dans une entreprise de domiciliation'
        can_1.drawString(round(-5.75 * 72), round(5.53 * 72), "X")

        # Insérer le numéro unique d'identification
        can_1.drawString(round(-2.3 * 72), round(5.51 * 72), "1")
        can_1.drawString(round(-2.2 * 72), round(5.51 * 72), "2")
        can_1.drawString(round(-2.1 * 72), round(5.51 * 72), "3")
        can_1.drawString(round(-2 * 72), round(5.51 * 72), "4")
        can_1.drawString(round(-1.9 * 72), round(5.51 * 72), "5")
        can_1.drawString(round(-1.8 * 72), round(5.51 * 72), "6")
        can_1.drawString(round(-1.7 * 72), round(5.51 * 72), "7")
        can_1.drawString(round(-1.6 * 72), round(5.51 * 72), "8")
        can_1.drawString(round(-1.5 * 72), round(5.51 * 72), "9")

        # Insérer le nom du domiciliataire
        can_1.drawString(round(-4.48 * 72), round(5.4 * 72), "Digidom")

        # Insérer le nom commercial
        can_1.drawString(round(-9.93 * 72), round(2.6 * 72), "MERCORUS")

        # Insérer la date de début d'activité
        can_1.drawString(round(-9.45 * 72), round(2.12 * 72), "0")
        can_1.drawString(round(-9.35 * 72), round(2.12 * 72), "1")
        can_1.drawString(round(-9.25 * 72), round(2.12 * 72), "0")
        can_1.drawString(round(-9.15 * 72), round(2.12 * 72), "7")
        can_1.drawString(round(-9.05 * 72), round(2.12 * 72), "2")
        can_1.drawString(round(-8.95 * 72), round(2.12 * 72), "0")
        can_1.drawString(round(-8.85 * 72), round(2.12 * 72), "2")
        can_1.drawString(round(-8.75 * 72), round(2.12 * 72), "1")

        # Cocher la case 'Permanente'
        can_1.drawString(round(-8.47 * 72), round(2.1 * 72), "X")

        # Insérer les activité(s) exercée(s) dans l'établissement
        can_1.drawString(round(-8.84 * 72), round(1.9 * 72), "Code APE / NAF 2441Z - Production de métaux précieux")
        can_1.drawString(round(-11.04 * 72), round(1.77 * 72), "Code APE / NAF 4672Z - Commerce de gros (commerce interentreprises) de minerais et métaux")

        # Insérer l'activité principale
        can_1.drawString(round(-11.01 * 72), round(1.52 * 72), "Code APE / NAF 2441Z - Production de métaux précieux")

        # Cocher la case 'Commerce de gros'
        can_1.drawString(round(-11.05 * 72), round(0.74 * 72), "X")

        # Cocher la case 'Création'
        can_1.drawString(round(-3.75 * 72), round(3.31 * 72), "X")

        # Cocher la case 'non' pour l'effectif salarié
        can_1.drawString(round(-4.62 * 72), round(0.48 * 72), "X")

        # Cocher la case 'non' : La société embauche un premier salarié
        can_1.drawString(round(-3.42 * 72), round(0.35 * 72), "X")

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

        can_2.rotate(-90)

        # Insérer la Qualité
        can_2.drawString(round(-10.42 * 72), round(7.25 * 72), "Président")

        # Insérer le nom de naissance
        can_2.drawString(round(-9.30 * 72), round(7.12 * 72), "")

        # Insérer le nom d'usage
        can_2.drawString(round(-10.27 * 72), round(6.99 * 72), "")

        # Insérer les prénoms
        can_2.drawString(round(-8.17 * 72), round(6.99 * 72), "")

        # Insérer la date de naissance
        can_2.drawString(round(-10.6 * 72), round(6.85 * 72), "1")
        can_2.drawString(round(-10.5 * 72), round(6.85 * 72), "1")
        can_2.drawString(round(-10.4 * 72), round(6.85 * 72), "1")
        can_2.drawString(round(-10.3 * 72), round(6.85 * 72), "1")
        can_2.drawString(round(-10.2 * 72), round(6.85 * 72), "1")
        can_2.drawString(round(-10.1 * 72), round(6.85 * 72), "9")
        can_2.drawString(round(-10 * 72), round(6.85 * 72), "9")
        can_2.drawString(round(-9.9 * 72), round(6.85 * 72), "3")

        # Insérer le lieu de naissance
        can_2.drawString(round(-9.48 * 72), round(6.86 * 72), "Saint-Louis (97450)")

        # Insérer la nationalité
        can_2.drawString(round(-7.31 * 72), round(6.86 * 72), "Française")

        # Insérer le domicile / siège
        can_2.drawString(round(-10.15 * 72), round(6.72 * 72), " - Etage 1 Appartement 6")

        # Insérer le code postal du docmicile
        can_2.drawString(round(-10.4 * 72), round(6.61 * 72), "9")
        can_2.drawString(round(-10.3 * 72), round(6.61 * 72), "3")
        can_2.drawString(round(-10.2 * 72), round(6.61 * 72), "8")
        can_2.drawString(round(-10.1 * 72), round(6.61 * 72), "0")
        can_2.drawString(round(-10 * 72), round(6.61 * 72), "0")

        # Insérer la commune du docmicile
        can_2.drawString(round(-9.19 * 72), round(6.61 * 72), "Epinay-sur-Seine")

        # Cocher la case 'Réel normal Impôt sur les sociétés (IS)'
        can_2.drawString(round(-2.55 * 72), round(3.11 * 72), "X")

        # Encadrer 'Réel normal Impôt sur les sociétés (IS)'
        can_2.rect(round(-4.63 * 72), round(3.03 * 72), 158, 15)

        # Cocher la case 'TVA réel normal'
        can_2.drawString(round(-9.9 * 72), round(2.42 * 72), "X")

        # Cocher la case 'Déclarée au cadre n°'
        can_2.drawString(round(-9.4 * 72), round(1.64 * 72), "X")

        # Insérer le numéro du 'Déclarée au cadre n°'
        can_2.drawString(round(-8.10 * 72), round(1.66 * 72), "6")

        # Insérer le numéro de téléphone
        can_2.drawString(round(-3.80 * 72), round(1.66 * 72), "")

        # Insérer l'adresse mail
        can_2.drawString(round(-2.98 * 72), round(1.54 * 72), "")

        # Cocher la case 'Le représentant légal'
        can_2.drawString(round(-11.04 * 72), round(0.88 * 72), "X")

        # Insérer 'Le représentant légal'
        can_2.drawString(round(-8.3 * 72), round(0.87 * 72), "13")

        # Insérer le lieu de signature
        can_2.drawString(round(-6.91 * 72), round(0.72 * 72), "Epinay-sur-Seine (93800)")

        # Insérer la date de signature
        can_2.drawString(round(-4.59 * 72), round(0.79 * 72), dt.today().strftime("%d/%m/%Y"))

        can_2.save()

        # move to the beginning of the StringIO buffer
        packet_2.seek(0)
        new_pdf_2 = PdfFileReader(packet_2)

        # add the "watermark" of packet 1 on the page 2
        page_2 = original_pdf.getPage(1)
        page_2.mergePage(new_pdf_2.getPage(0))
        filled_pdf.addPage(page_2)
        # Page 2

        # Page 3
        packet_3 = io.BytesIO()

        # create a new PDF with Reportlab
        can_3 = canvas.Canvas(packet_3, pagesize=letter)

        can_3.setFontSize(8)

        can_3.rotate(-90)

        # Cocher la case 'Constitution d'une société commerciale'
        can_3.drawString(round(-11.05 * 72), round(7.04 * 72), "X")

        # Insérer la Dénomination
        can_3.drawString(round(- 10.11 * 72), round(6.33 * 72), "MERCORUS")

        # Cocher la case 'SAS constituée d'un associé unique,'
        can_3.drawString(round(-11.06 * 72), round(5.93 * 72), "X")

        # Cocher la case 'oui pour l'associé unique en est le président'
        can_3.drawString(round(-7.32 * 72), round(5.93 * 72), "X")

        # Insérer la durée de la personne morale
        can_3.drawString(round(-9.48 * 72), round(5.8 * 72), "Quatre-vingt-dix-neuf ans")

        # Insérer le montant et l'unité monétaire du capital
        can_3.drawString(round(-9.35 * 72), round(5.68 * 72), "100,00 Euros")

        # Insérer le minimum du capital si variable
        can_3.drawString(round(-6.75 * 72), round(5.70 * 72), "20,00 Euros")

        # Insérer la Date de clôture de l'exercice social
        can_3.drawString(round(-9.3 * 72), round(5.41 * 72), "3")
        can_3.drawString(round(-9.2 * 72), round(5.41 * 72), "1")
        can_3.drawString(round(-9.1 * 72), round(5.41 * 72), "1")
        can_3.drawString(round(-8.97 * 72), round(5.41 * 72), "2")

        # Insérer la date de clôture du 1er exercice
        can_3.drawString(round(-7.1 * 72), round(5.41 * 72), "3")
        can_3.drawString(round(-7 * 72), round(5.41 * 72), "1")
        can_3.drawString(round(-6.9 * 72), round(5.41 * 72), "1")
        can_3.drawString(round(-6.8 * 72), round(5.41 * 72), "2")
        can_3.drawString(round(-6.7 * 72), round(5.41 * 72), "2")
        can_3.drawString(round(-6.6 * 72), round(5.41 * 72), "0")
        can_3.drawString(round(-6.5 * 72), round(5.41 * 72), "2")
        can_3.drawString(round(-6.4 * 72), round(5.41 * 72), "1")

        # Insérer les principales activites de l'objet social
        can_3.drawString(round(-11.01 * 72), round(5.04 * 72), "Code APE / NAF 2441Z - Production de métaux précieux")
        can_3.drawString(round(-11.01 * 72), round(4.91 * 72),
                         "Code APE / NAF 4672Z - Commerce de gros (commerce interentreprises) de minerais et métaux")

        # Insérer l'adresse du siège social
        can_3.drawString(round(-5.74 * 72), round(6.18 * 72), "10 rue de Penthièvre")

        # Insérer le code postal du siège social
        can_3.drawString(round(-5.1 * 72), round(6.05 * 72), "7")
        can_3.drawString(round(-5 * 72), round(6.05 * 72), "5")
        can_3.drawString(round(-4.9 * 72), round(6.05 * 72), "0")
        can_3.drawString(round(-4.8 * 72), round(6.05 * 72), "0")
        can_3.drawString(round(-4.7 * 72), round(6.05 * 72), "8")

        # Insérer la commune du siège social
        can_3.drawString(round(-3.92 * 72), round(6.06 * 72), "Paris")

        # Cocher la case 'Dans une entreprise de domiciliation'
        can_3.drawString(round(-5.75 * 72), round(5.53 * 72), "X")

        # Insérer le numéro unique d'identification
        can_3.drawString(round(-2.3 * 72), round(5.51 * 72), "1")
        can_3.drawString(round(-2.2 * 72), round(5.51 * 72), "2")
        can_3.drawString(round(-2.1 * 72), round(5.51 * 72), "3")
        can_3.drawString(round(-2 * 72), round(5.51 * 72), "4")
        can_3.drawString(round(-1.9 * 72), round(5.51 * 72), "5")
        can_3.drawString(round(-1.8 * 72), round(5.51 * 72), "6")
        can_3.drawString(round(-1.7 * 72), round(5.51 * 72), "7")
        can_3.drawString(round(-1.6 * 72), round(5.51 * 72), "8")
        can_3.drawString(round(-1.5 * 72), round(5.51 * 72), "9")

        # Insérer le nom du domiciliataire
        can_3.drawString(round(-4.48 * 72), round(5.4 * 72), "Digidom")

        # Insérer le nom commercial
        can_3.drawString(round(-9.93 * 72), round(2.6 * 72), "MERCORUS")

        # Insérer la date de début d'activité
        can_3.drawString(round(-9.45 * 72), round(2.12 * 72), "0")
        can_3.drawString(round(-9.35 * 72), round(2.12 * 72), "1")
        can_3.drawString(round(-9.25 * 72), round(2.12 * 72), "0")
        can_3.drawString(round(-9.15 * 72), round(2.12 * 72), "7")
        can_3.drawString(round(-9.05 * 72), round(2.12 * 72), "2")
        can_3.drawString(round(-8.95 * 72), round(2.12 * 72), "0")
        can_3.drawString(round(-8.85 * 72), round(2.12 * 72), "2")
        can_3.drawString(round(-8.75 * 72), round(2.12 * 72), "1")

        # Cocher la case 'Permanente'
        can_3.drawString(round(-8.47 * 72), round(2.1 * 72), "X")

        # Insérer les activité(s) exercée(s) dans l'établissement
        can_3.drawString(round(-8.84 * 72), round(1.9 * 72), "Code APE / NAF 2441Z - Production de métaux précieux")
        can_3.drawString(round(-11.04 * 72), round(1.77 * 72),
                         "Code APE / NAF 4672Z - Commerce de gros (commerce interentreprises) de minerais et métaux")

        # Insérer l'activité principale
        can_3.drawString(round(-11.01 * 72), round(1.52 * 72), "Code APE / NAF 2441Z - Production de métaux précieux")

        # Insérer la mention 'Commerce de gros : Oui'
        can_3.drawString(round(-11.1 * 72), round(1.34 * 72), "Commerce de gros ? : Oui")

        # Cocher la case 'Création'
        can_3.drawString(round(-3.75 * 72), round(3.31 * 72), "X")

        # Insérer la mention 'Effectif salarié : Non.'
        can_3.drawString(round(-5.68 * 72), round(0.52 * 72), "Effectif salarié ? : Non.")

        # Insérer la mention 'La société embauche un premier salarié: Non.'
        can_3.drawString(round(-5.68 * 72), round(0.36 * 72), "La société embauche un premier salarié ? : Non.")

        can_3.save()

        # move to the beginning of the StringIO buffer
        packet_3.seek(0)
        new_pdf_3 = PdfFileReader(packet_3)

        # add the "watermark" of packet 1 on the page 2
        page_3 = original_pdf.getPage(2)
        page_3.mergePage(new_pdf_3.getPage(0))
        filled_pdf.addPage(page_3)
        # Page 3

        # Page 4
        packet_4 = io.BytesIO()

        # create a new PDF with Reportlab
        can_4 = canvas.Canvas(packet_4, pagesize=letter)

        can_4.setFontSize(8)

        can_4.rotate(-90)

        # Insérer la Qualité
        can_4.drawString(round(-10.42 * 72), round(7.25 * 72), "Président")

        # Insérer le nom de naissance
        can_4.drawString(round(-9.30 * 72), round(7.12 * 72), "")

        # Insérer le nom d'usage
        can_4.drawString(round(-10.27 * 72), round(6.99 * 72), "")

        # Insérer les prénoms
        can_4.drawString(round(-8.17 * 72), round(6.99 * 72), "")

        # Insérer la date de naissance
        can_4.drawString(round(-10.6 * 72), round(6.85 * 72), "1")
        can_4.drawString(round(-10.5 * 72), round(6.85 * 72), "1")
        can_4.drawString(round(-10.4 * 72), round(6.85 * 72), "1")
        can_4.drawString(round(-10.3 * 72), round(6.85 * 72), "1")
        can_4.drawString(round(-10.2 * 72), round(6.85 * 72), "1")
        can_4.drawString(round(-10.1 * 72), round(6.85 * 72), "9")
        can_4.drawString(round(-10 * 72), round(6.85 * 72), "9")
        can_4.drawString(round(-9.9 * 72), round(6.85 * 72), "3")

        # Insérer le lieu de naissance
        can_4.drawString(round(-9.48 * 72), round(6.86 * 72), "Saint-Louis (97450)")

        # Insérer la nationalité
        can_4.drawString(round(-7.31 * 72), round(6.86 * 72), "Française")

        # Insérer le domicile / siège
        can_4.drawString(round(-10.15 * 72), round(6.72 * 72), " - Etage 1 Appartement 6")

        # Insérer le code postal du docmicile
        can_4.drawString(round(-10.4 * 72), round(6.61 * 72), "9")
        can_4.drawString(round(-10.3 * 72), round(6.61 * 72), "3")
        can_4.drawString(round(-10.2 * 72), round(6.61 * 72), "8")
        can_4.drawString(round(-10.1 * 72), round(6.61 * 72), "0")
        can_4.drawString(round(-10 * 72), round(6.61 * 72), "0")

        # Insérer la commune du docmicile
        can_4.drawString(round(-9.19 * 72), round(6.61 * 72), "Epinay-sur-Seine")

        # Insérer la mention 'Réel normal Impôt sur les sociétés (IS) ; T.V.A. : réel normal'
        can_4.drawString(round(-11.07 * 72), round(3.11 * 72), "Réel normal Impôt sur les sociétés (IS) ; T.V.A. : réel normal")

        # Cocher la case 'Déclarée au cadre n°'
        can_4.drawString(round(-9.4 * 72), round(1.64 * 72), "X")

        # Insérer le numéro du 'Déclarée au cadre n°'
        can_4.drawString(round(-8.10 * 72), round(1.66 * 72), "6")

        # Insérer le numéro de téléphone
        can_4.drawString(round(-3.80 * 72), round(1.66 * 72), "")

        # Insérer l'adresse mail
        can_4.drawString(round(-2.98 * 72), round(1.54 * 72), "")

        # Cocher la case 'Le représentant légal'
        can_4.drawString(round(-11.04 * 72), round(0.88 * 72), "X")

        # Insérer 'Le représentant légal'
        can_4.drawString(round(-8.3 * 72), round(0.87 * 72), "13")

        # Insérer le lieu de signature
        can_4.drawString(round(-6.91 * 72), round(0.72 * 72), "Epinay-sur-Seine (93800)")

        # Insérer la date de signature
        can_4.drawString(round(-4.59 * 72), round(0.79 * 72), dt.today().strftime("%d/%m/%Y"))

        can_4.save()

        # move to the beginning of the StringIO buffer
        packet_4.seek(0)
        new_pdf_4 = PdfFileReader(packet_4)

        # add the "watermark" of packet 1 on the page 2
        page_4 = original_pdf.getPage(3)
        page_4.mergePage(new_pdf_4.getPage(0))
        filled_pdf.addPage(page_4)
        # Page 4

        # finally, write "output" to a real file
        output_file = "Mercorus\\Cerfa_13959_" + dt.today().strftime('%d_%m_%Y') + ".pdf"
        output_stream = open(output_file, "wb")
        filled_pdf.write(output_stream)
        output_stream.close()


if __name__ == '__main__':
    unittest.main()
