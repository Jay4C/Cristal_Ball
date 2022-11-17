import unittest
from PyPDF2 import PdfFileWriter, PdfFileReader
from datetime import datetime as dt


class UnitTestsPretAdie(unittest.TestCase):
    def test_pret_adie(self):
        print("test_pret_adie")

        output = PdfFileWriter()

        # Justificatif de revenus
        justificatif_de_revenus = ""

        justificatif_de_revenus_pdf = PdfFileReader(open(justificatif_de_revenus, "rb"))

        for i in range(0, justificatif_de_revenus_pdf.getNumPages()):
            output.addPage(justificatif_de_revenus_pdf.getPage(i))

        # 3 derniers relevés de comptes bancaires personnels et professionnels (si je suis déjà en activité)
        trois_derniers_releves_comptes_bancaires_personnels = ""

        trois_derniers_releves_comptes_bancaires_personnels_pdf = \
            PdfFileReader(open(trois_derniers_releves_comptes_bancaires_personnels, "rb"))

        for i in range(0, trois_derniers_releves_comptes_bancaires_personnels_pdf.getNumPages()):
            output.addPage(trois_derniers_releves_comptes_bancaires_personnels_pdf.getPage(i))

        # 3 derniers relevés de comptes bancaires personnels et professionnels (si je suis déjà en activité)
        trois_derniers_releves_comptes_bancaires_professionnels = ""

        trois_derniers_releves_comptes_bancaires_professionnels_pdf = \
            PdfFileReader(open(trois_derniers_releves_comptes_bancaires_professionnels, "rb"))

        for i in range(0, trois_derniers_releves_comptes_bancaires_professionnels_pdf.getNumPages()):
            output.addPage(trois_derniers_releves_comptes_bancaires_professionnels_pdf.getPage(i))

        # Pièce d’identité
        piece_identite = ""

        piece_identite_pdf = PdfFileReader(open(piece_identite, "rb"))

        for i in range(0, piece_identite_pdf.getNumPages()):
            output.addPage(piece_identite_pdf.getPage(i))

        # Permis de conduire (pour l’achat / réparation d’un véhicule)
        permis_conduire = ""

        permis_conduire_pdf = PdfFileReader(open(permis_conduire, "rb"))

        for i in range(0, permis_conduire_pdf.getNumPages()):
            output.addPage(permis_conduire_pdf.getPage(i))

        # finally, write "output" to a real file
        output_stream = open("Adie\\demande_de_pret_" + dt.today().strftime('%d_%m_%Y') + ".pdf", "wb")
        output.write(output_stream)
        output_stream.close()


if __name__ == '__main__':
    unittest.main()
