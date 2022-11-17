import unittest
import xlsxwriter


class GrandLivreJournal(unittest.TestCase):
    # ok
    def test_grand_livre_journal_depuis_livre_journal(self):
        print("test_grand_livre_journal_depuis_livre_journal")

        workbook_to_write = xlsxwriter.Workbook('Grand_Livre_Journal\\grand_livre_journal.xlsx')

        worksheet = workbook_to_write.add_worksheet('data')

        elements = [
            {'start': '', 'end': ''},
        ]

        r = 0

        cell_format = workbook_to_write.add_format(
            {
                'bg_color': 'cyan',
                'border': 1,
                'align': 'justify',
                'valign': 'top'
            }
        )

        for element in elements:
            for i in range(int(element.get('start')), int(element.get('end')) + 1):
                worksheet.write_formula(r, 0, '=Livre_Journal.B' + str(i), cell_format)
                worksheet.write_formula(r, 1, '=Livre_Journal.I' + str(i), cell_format)
                worksheet.write_formula(r, 2, '=Livre_Journal.A' + str(i), cell_format)
                worksheet.write_formula(r, 3, '=Livre_Journal.E' + str(i), cell_format)
                worksheet.write_formula(r, 4, '=Livre_Journal.F' + str(i), cell_format)
                worksheet.write_formula(r, 5, '=Livre_Journal.G' + str(i), cell_format)
                worksheet.write(r, 6, '', cell_format)
                worksheet.write(r, 7, '-', cell_format)
                r += 1

        workbook_to_write.close()

    # ok
    def test_grand_livre_journal_depuis_journal_des_a_nouveaux(self):
        print("test_grand_livre_journal_depuis_journal_des_a_nouveaux")

        workbook_to_write = xlsxwriter.Workbook('Grand_Livre_Journal\\grand_livre_journal_depuis_jdan.xlsx')

        worksheet = workbook_to_write.add_worksheet('data')

        elements = [
            {'start': '5', 'end': '13'},
        ]

        r = 0

        cell_format = workbook_to_write.add_format(
            {
                'bg_color': 'cyan',
                'border': 1,
                'align': 'justify',
                'valign': 'top'
            }
        )

        for element in elements:
            for i in range(int(element.get('start')), int(element.get('end')) + 1):
                worksheet.write_formula(r, 0, '=Journal_Des_A_Nouveaux.B' + str(i), cell_format)
                worksheet.write_formula(r, 1, '=Journal_Des_A_Nouveaux.I' + str(i), cell_format)
                worksheet.write_formula(r, 2, '=Journal_Des_A_Nouveaux.A' + str(i), cell_format)
                worksheet.write_formula(r, 3, '=Journal_Des_A_Nouveaux.E' + str(i), cell_format)
                worksheet.write_formula(r, 4, '=Journal_Des_A_Nouveaux.F' + str(i), cell_format)
                worksheet.write_formula(r, 5, '=Journal_Des_A_Nouveaux.G' + str(i), cell_format)
                worksheet.write(r, 6, '', cell_format)
                worksheet.write(r, 7, '-', cell_format)
                r += 1

        workbook_to_write.close()


if __name__ == '__main__':
    unittest.main()
