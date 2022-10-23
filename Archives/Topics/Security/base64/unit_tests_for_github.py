import unittest
import base64


class UnitTestsTopicsSecurityBase64ForGitHub(unittest.TestCase):
    # ok
    def test_convert_pdf_to_base64(self):
        print('test_convert_pdf_to_base64')

        filename_1 = "C:\\Users\\Jason\\Dropbox\\2_Professionnel\\Voltorus\\3_Marketing\\3_Fournisseurs\\1_Avocats" \
                     "\\CAO_N_Machine_Jason_ALOYAU.pdf"

        pdf = open(filename_1, 'rb')

        filename_1_base64 = base64.b64encode(pdf.read())

        pdf.close()

        print(filename_1_base64)


if __name__ == '__main__':
    unittest.main()
