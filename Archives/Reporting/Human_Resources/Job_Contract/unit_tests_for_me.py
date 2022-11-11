import unittest
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4


class UnitTestsReportingHumanResourcesJobContractForMe(unittest.TestCase):
    #
    def test_job_contract_for_paraphe(self):
        print('test_job_contract_for_paraphe')

        c = canvas.Canvas("Contrat_De_Travail_Jason_ALOYAU.pdf", pagesize=A4)
        c.save()


if __name__ == '__main__':
    unittest.main()
