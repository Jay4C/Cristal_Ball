import unittest
import time
from pywinauto.application import Application
import pywinauto.keyboard
import pywinauto.mouse
import pywinauto.base_wrapper
import pywinauto.timings
import os
import xlrd


class UnitTestsDesktopAutomationGeoportail(unittest.TestCase):
    def test_afficher_des_parcelles_methane(self):
        print("test_afficher_des_parcelles_methane")

        app = Application(backend="uia")

        app.start("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")

        time.sleep(6)

        workbook = xlrd.open_workbook("A:\\1_Professionnel\\1_Holomorphe\\2_Archives\\3_Etude_De_Marches\\8_Etudes_Des_Marches_Immobiliers\\Parcelles_Methane_France_Biogas_Ou_Train.xls")

        time.sleep(3)

        worksheet = workbook.sheet_by_name('ile de france')

        start = 865

        end = 889

        pywinauto.keyboard.send_keys("https://www.geoportail.gouv.fr/carte")

        time.sleep(3)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(10)

        # Click left on "Search" button
        pywinauto.mouse.click(button='left', coords=(680, 90))

        time.sleep(3)

        for i in range(start, end):
            time.sleep(3)

            # Insert Coordinates
            pywinauto.keyboard.send_keys(
                str(worksheet.cell_value(i, 6)).replace(' ', '{VK_SPACE}')
            )

            time.sleep(5)

            # Press the 'Enter' button
            pywinauto.keyboard.send_keys('{ENTER}')

            time.sleep(15)

            # Double-Click left to zoom
            pywinauto.mouse.double_click(button='left', coords=(700, 400))

            time.sleep(3)

            # Double-Click left to zoom
            pywinauto.mouse.double_click(button='left', coords=(700, 400))

            time.sleep(30)

            # Click left on "Search" button
            pywinauto.mouse.click(button='left', coords=(680, 90))

            time.sleep(3)

            # Press Ctrl+a
            pywinauto.keyboard.send_keys('^a')

            time.sleep(3)

        print("ccleaner running")
        os.system("set ccleaner='C:\\Program Files\\CCleaner\\CCleaner.exe'")
        os.system("start ccleaner /AUTO")

        time.sleep(5)


if __name__ == '__main__':
    unittest.main()
