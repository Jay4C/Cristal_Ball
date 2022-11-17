import unittest
from PyPDF2 import PdfFileWriter, PdfFileReader
import os

annee = "Annee_2021"

bilan_s_d_folder = "A:\\1_Professionnel\\1_Holomorphe\\2_Archives\\2_Outils_Numeriques\\My_Tools" \
                   "\\Test\\Service\\Archives\\Reporting\\Corporate_Reporting\\Comptes_Annuels" \
                   "\\Bilan\\Holomorphe\\" + annee + "\\B_S_D"

compte_de_resultat_s_d_folder = "A:\\1_Professionnel\\1_Holomorphe\\2_Archives\\2_Outils_Numeriques\\My_Tools" \
                                  "\\Test\\Service\\Archives\\Reporting\\Corporate_Reporting\\Comptes_Annuels" \
                                  "\\Compte_De_Resultat\\Holomorphe\\" + annee + "\\C_D_R_S_D"

# finally, write "output" to a real file
exercice = "2_Exercice_01_01_2021__31_12_2021"


class UnitTestsBilanCompteResultatHolomorphe(unittest.TestCase):
    # ok
    def test_bilan_compte_resultat_s_d_b(self):
        print("test_bilan_compte_resultat_s_d_b")

        bilan_s_d_folder_files = os.listdir(bilan_s_d_folder)

        bilan_s_d_filename = ""

        for f in bilan_s_d_folder_files:
            if "signed" in f:
                bilan_s_d_filename += f
                print("bilan_s_d_filename : " + bilan_s_d_filename)

        compte_de_resultat_s_d_folder_files = os.listdir(compte_de_resultat_s_d_folder)

        compte_de_resultat_filename = ""

        for f in compte_de_resultat_s_d_folder_files:
            if "signed" in f:
                compte_de_resultat_filename += f
                print("compte_de_resultat_filename : " + compte_de_resultat_filename)

        output = PdfFileWriter()

        # Bilan systeme de développé
        bilan_s_d_b = bilan_s_d_folder + "\\" + bilan_s_d_filename

        bilan_s_d_b_pdf = PdfFileReader(open(bilan_s_d_b, "rb"))

        for i in range(0, bilan_s_d_b_pdf.getNumPages()):
            output.addPage(bilan_s_d_b_pdf.getPage(i))

        # Compte de resultat système développé
        compte_de_resultat_s_d = compte_de_resultat_s_d_folder + "\\" + compte_de_resultat_filename

        compte_de_resultat_s_d_b_pdf = PdfFileReader(open(compte_de_resultat_s_d, "rb"))

        for i in range(0, compte_de_resultat_s_d_b_pdf.getNumPages()):
            output.addPage(compte_de_resultat_s_d_b_pdf.getPage(i))

        output_stream = open("A:\\1_Professionnel\\1_Holomorphe\\1_Administration"
                             "\\2_Gestion_Declarations_Administratives\\1_Recurrentes\\5_Infogreffe"
                             "\\4_Approbation_Comptes_Sociaux\\" + exercice + "\\Bilan_Compte_Resultat_"
                             + annee + "_HOLOMORPHE.pdf",
                             "wb")
        output.write(output_stream)
        output_stream.close()


if __name__ == '__main__':
    unittest.main()
