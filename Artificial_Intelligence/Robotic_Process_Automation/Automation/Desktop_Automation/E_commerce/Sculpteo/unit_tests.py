import unittest
import time
from pywinauto.application import Application
import pywinauto.keyboard
import pywinauto.mouse
import pywinauto.base_wrapper
import pywinauto.timings
import os


class UnitTestsDesktopAutomationSculpteo(unittest.TestCase):
    # ok
    def test_chiffrer_une_piece_pour_holomorphe(self):
        print("test_chiffrer_une_piece_pour_holomorphe")

        filename = "part_equerre_assemblage_laser_cutting_v2.dxf"

        patent = "Version_3"

        folder_path = "2_Specials\\Edwin_Gray_Power_Tube\\" + patent

        time.sleep(6)

        app = Application(backend="uia")

        app.start("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")

        time.sleep(6)

        pywinauto.keyboard.send_keys("https://www.sculpteo.com/fr/")

        time.sleep(3)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(15)

        # Click on the "Tout refuser"
        pywinauto.mouse.click(button='left', coords=(780, 660))

        time.sleep(10)

        # Click on the "Connectez-vous"
        pywinauto.mouse.click(button='left', coords=(1040, 110))

        time.sleep(10)

        # Click on the "Email"
        pywinauto.mouse.click(button='left', coords=(520, 310))

        time.sleep(10)

        # Insert the 'Email' value
        pywinauto.keyboard.send_keys('.@outlook.fr')

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys('{VK_TAB}')

        time.sleep(3)

        # Press the 'Password' value
        pywinauto.keyboard.send_keys('')

        time.sleep(3)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(10)

        # Click on the "Transférer un fichier"
        pywinauto.mouse.click(button='left', coords=(670, 370))

        time.sleep(10)

        # Click on the "Visibilité - Privé"
        pywinauto.mouse.click(button='left', coords=(520, 350))

        time.sleep(10)

        # Click on the "Sélectionner un fichier à transférer"
        pywinauto.mouse.click(button='left', coords=(670, 520))

        time.sleep(10)

        # Click on the bar folder
        pywinauto.mouse.click(button='left', coords=(370, 50))

        time.sleep(5)

        # Insert the folder path
        pywinauto.keyboard.send_keys("A:\\1_Professionnel\\1_Holomorphe\\2_Archives\\2_Outils_Numeriques"
                                     "\\Python__Flask__Cristal_Ball\\Test\\Service\\Archives\\CAO\\" + folder_path)

        time.sleep(5)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(5)

        # Click on the bar file
        pywinauto.mouse.click(button='left', coords=(270, 415))

        time.sleep(5)

        # Press the 'Ctrl + a' button
        pywinauto.keyboard.send_keys('^a')

        time.sleep(5)

        # Insert the folder path
        pywinauto.keyboard.send_keys(filename)

        time.sleep(5)

        # Click on the "Ouvrir" button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(15)

        # Click on the "Suivant" button
        pywinauto.mouse.click(button='left', coords=(1160, 440))

        time.sleep(20)

        print("ccleaner running")
        os.system("set ccleaner='C:\\Program Files\\CCleaner\\CCleaner.exe'")
        os.system("start ccleaner /AUTO")

        time.sleep(5)


if __name__ == '__main__':
    unittest.main()
