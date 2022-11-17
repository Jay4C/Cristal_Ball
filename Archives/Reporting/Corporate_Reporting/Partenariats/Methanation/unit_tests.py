import unittest
from PyPDF2 import PdfFileWriter, PdfFileReader


class UnitTestsPartenariatMethanation(unittest.TestCase):
    # ok
    def test_machine_gravitationnelle(self):
        print("test_machine_gravitationnelle")

        location = "Methanation"

        title_file = "Machine_Gravitationnelle_[Holomorphe].pdf"

        output = PdfFileWriter()

        # isometric
        isometric = "A:\\1_Professionnel\\1_Holomorphe\\2_Archives\\2_Outils_Numeriques" \
                    "\\Python__Flask__Cristal_Ball\\Test\\Service\\Archives\\Reporting" \
                    "\\Corporate_Reporting\\Partenariats" \
                    "\\" + str(location) + "\\Isometric.pdf"

        isometric_pdf = PdfFileReader(open(isometric, "rb"))

        for i in range(0, isometric_pdf.getNumPages()):
            output.addPage(isometric_pdf.getPage(i))

        # face
        face = "A:\\1_Professionnel\\1_Holomorphe\\2_Archives\\2_Outils_Numeriques" \
               "\\Python__Flask__Cristal_Ball\\Test\\Service\\Archives\\Reporting" \
               "\\Corporate_Reporting\\Partenariats" \
               "\\" + str(location) + "\\Face.pdf"

        face_pdf = PdfFileReader(open(face, "rb"))

        for i in range(0, face_pdf.getNumPages()):
            output.addPage(face_pdf.getPage(i))

        # droite
        droite = "A:\\1_Professionnel\\1_Holomorphe\\2_Archives\\2_Outils_Numeriques" \
                 "\\Python__Flask__Cristal_Ball\\Test\\Service\\Archives\\Reporting" \
                 "\\Corporate_Reporting\\Partenariats" \
                 "\\" + str(location) + "\\Droite.pdf"

        droite_pdf = PdfFileReader(open(droite, "rb"))

        for i in range(0, droite_pdf.getNumPages()):
            output.addPage(droite_pdf.getPage(i))

        # gauche
        gauche = "A:\\1_Professionnel\\1_Holomorphe\\2_Archives\\2_Outils_Numeriques" \
                 "\\Python__Flask__Cristal_Ball\\Test\\Service\\Archives\\Reporting" \
                 "\\Corporate_Reporting\\Partenariats" \
                 "\\" + str(location) + "\\Gauche.pdf"

        gauche_pdf = PdfFileReader(open(gauche, "rb"))

        for i in range(0, gauche_pdf.getNumPages()):
            output.addPage(gauche_pdf.getPage(i))

        # dessus
        dessus = "A:\\1_Professionnel\\1_Holomorphe\\2_Archives\\2_Outils_Numeriques" \
                 "\\Python__Flask__Cristal_Ball\\Test\\Service\\Archives\\Reporting" \
                 "\\Corporate_Reporting\\Partenariats" \
                 "\\" + str(location) + "\\Dessus.pdf"

        dessus_pdf = PdfFileReader(open(dessus, "rb"))

        for i in range(0, dessus_pdf.getNumPages()):
            output.addPage(dessus_pdf.getPage(i))

        # dessous
        dessous = "A:\\1_Professionnel\\1_Holomorphe\\2_Archives\\2_Outils_Numeriques" \
                  "\\Python__Flask__Cristal_Ball\\Test\\Service\\Archives\\Reporting" \
                  "\\Corporate_Reporting\\Partenariats" \
                  "\\" + str(location) + "\\Dessous.pdf"

        dessous_pdf = PdfFileReader(open(dessous, "rb"))

        for i in range(0, dessous_pdf.getNumPages()):
            output.addPage(dessous_pdf.getPage(i))

        # arriere
        arriere = "A:\\1_Professionnel\\1_Holomorphe\\2_Archives\\2_Outils_Numeriques" \
                  "\\Python__Flask__Cristal_Ball\\Test\\Service\\Archives\\Reporting" \
                  "\\Corporate_Reporting\\Partenariats" \
                  "\\" + str(location) + "\\Arriere.pdf"

        arriere_pdf = PdfFileReader(open(arriere, "rb"))

        for i in range(0, arriere_pdf.getNumPages()):
            output.addPage(arriere_pdf.getPage(i))

        # finally, write "output" to a real file
        file_location = "A:\\1_Professionnel\\1_Holomorphe\\2_Archives\\2_Outils_Numeriques" \
                        "\\Python__Flask__Cristal_Ball\\Test\\Service\\Archives\\Reporting" \
                        "\\Corporate_Reporting\\Partenariats" \
                        "\\" + str(location)
        output_stream = open(file_location + "\\" + title_file, "wb")
        output.write(output_stream)
        output_stream.close()

    # ok
    def test_gravitational_engine(self):
        print("test_gravitational_engine")

        location = "Methanation"

        title_file = "Gravitational_Engine_[Holomorphe].pdf"

        output = PdfFileWriter()

        # isometric
        isometric = "A:\\1_Professionnel\\1_Holomorphe\\2_Archives\\2_Outils_Numeriques" \
                    "\\Python__Flask__Cristal_Ball\\Test\\Service\\Archives\\Reporting" \
                    "\\Corporate_Reporting\\Partenariats" \
                    "\\" + str(location) + "\\Isometric.pdf"

        isometric_pdf = PdfFileReader(open(isometric, "rb"))

        for i in range(0, isometric_pdf.getNumPages()):
            output.addPage(isometric_pdf.getPage(i))

        # face
        face = "A:\\1_Professionnel\\1_Holomorphe\\2_Archives\\2_Outils_Numeriques" \
               "\\Python__Flask__Cristal_Ball\\Test\\Service\\Archives\\Reporting" \
               "\\Corporate_Reporting\\Partenariats" \
               "\\" + str(location) + "\\Face.pdf"

        face_pdf = PdfFileReader(open(face, "rb"))

        for i in range(0, face_pdf.getNumPages()):
            output.addPage(face_pdf.getPage(i))

        # droite
        droite = "A:\\1_Professionnel\\1_Holomorphe\\2_Archives\\2_Outils_Numeriques" \
                 "\\Python__Flask__Cristal_Ball\\Test\\Service\\Archives\\Reporting" \
                 "\\Corporate_Reporting\\Partenariats" \
                 "\\" + str(location) + "\\Droite.pdf"

        droite_pdf = PdfFileReader(open(droite, "rb"))

        for i in range(0, droite_pdf.getNumPages()):
            output.addPage(droite_pdf.getPage(i))

        # gauche
        gauche = "A:\\1_Professionnel\\1_Holomorphe\\2_Archives\\2_Outils_Numeriques" \
                 "\\Python__Flask__Cristal_Ball\\Test\\Service\\Archives\\Reporting" \
                 "\\Corporate_Reporting\\Partenariats" \
                 "\\" + str(location) + "\\Gauche.pdf"

        gauche_pdf = PdfFileReader(open(gauche, "rb"))

        for i in range(0, gauche_pdf.getNumPages()):
            output.addPage(gauche_pdf.getPage(i))

        # dessus
        dessus = "A:\\1_Professionnel\\1_Holomorphe\\2_Archives\\2_Outils_Numeriques" \
                 "\\Python__Flask__Cristal_Ball\\Test\\Service\\Archives\\Reporting" \
                 "\\Corporate_Reporting\\Partenariats" \
                 "\\" + str(location) + "\\Dessus.pdf"

        dessus_pdf = PdfFileReader(open(dessus, "rb"))

        for i in range(0, dessus_pdf.getNumPages()):
            output.addPage(dessus_pdf.getPage(i))

        # dessous
        dessous = "A:\\1_Professionnel\\1_Holomorphe\\2_Archives\\2_Outils_Numeriques" \
                  "\\Python__Flask__Cristal_Ball\\Test\\Service\\Archives\\Reporting" \
                  "\\Corporate_Reporting\\Partenariats" \
                  "\\" + str(location) + "\\Dessous.pdf"

        dessous_pdf = PdfFileReader(open(dessous, "rb"))

        for i in range(0, dessous_pdf.getNumPages()):
            output.addPage(dessous_pdf.getPage(i))

        # arriere
        arriere = "A:\\1_Professionnel\\1_Holomorphe\\2_Archives\\2_Outils_Numeriques" \
                  "\\Python__Flask__Cristal_Ball\\Test\\Service\\Archives\\Reporting" \
                  "\\Corporate_Reporting\\Partenariats" \
                  "\\" + str(location) + "\\Arriere.pdf"

        arriere_pdf = PdfFileReader(open(arriere, "rb"))

        for i in range(0, arriere_pdf.getNumPages()):
            output.addPage(arriere_pdf.getPage(i))

        # finally, write "output" to a real file
        file_location = "A:\\1_Professionnel\\1_Holomorphe\\2_Archives\\2_Outils_Numeriques" \
                        "\\Python__Flask__Cristal_Ball\\Test\\Service\\Archives\\Reporting" \
                        "\\Corporate_Reporting\\Partenariats" \
                        "\\" + str(location)
        output_stream = open(file_location + "\\" + title_file, "wb")
        output.write(output_stream)
        output_stream.close()


if __name__ == '__main__':
    unittest.main()
