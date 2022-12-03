import unittest
import os


class UnitTestsDirectoryManagement(unittest.TestCase):
    # ok
    def test_remove_file(self):
        print("test_remove_file")

        directory = "A:\\GitHub\\My_Own_Data\\"
        file = "3_Old_Archive/2_Personnel/2_Non_Recurrentes/58_Mes_Etudes_Scolaires/ESILV/Cours/Cours S10/2_Stage_De_Fin_D_Etudes/16_Agronergy_IT/html/export/composer.lock".replace("/", "\\")
        filename = directory + file
        os.remove(filename)

    # ok
    def test_remove_files(self):
        print("test_remove_files")

        directory = "A:\\GitHub\\My_Own_Data\\"

        files = [

        ]

        for file in files:
            try:
                filename = directory + file.replace("/", "\\")
                os.remove(filename)
            except Exception as e:
                print('error : ' + str(e))


if __name__ == '__main__':
    unittest.main()
