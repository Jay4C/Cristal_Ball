import unittest
import time
from pywinauto.application import Application
import pywinauto.keyboard
import pywinauto.mouse
import pywinauto.base_wrapper
import pywinauto.timings


class UnitTestsDesktopAutomationDouanes(unittest.TestCase):
    # ok
    def test_se_connecter_au_deb(self):
        print("test_se_connecter_au_deb")

        identifiant = ""

        password = ""

        app = Application(backend="uia")

        app.start("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")

        time.sleep(6)

        pywinauto.keyboard.send_keys("https://www.douane.gouv.fr/")

        time.sleep(3)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(5)

        # Click on the "Se connecter" button
        pywinauto.mouse.click(button='left', coords=(1040, 160))

        time.sleep(10)

        # Click on the "Identifiant" input
        pywinauto.mouse.click(button='left', coords=(200, 390))

        time.sleep(5)

        # Insert the 'Identifiant'
        pywinauto.keyboard.send_keys(identifiant)

        time.sleep(5)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(5)

        # Insert the 'M_D_P'
        pywinauto.keyboard.send_keys(password)

        time.sleep(5)

        # Press the 'Tab' button 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(5)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(15)

        # Press the 'DOWN' button 2 times
        pywinauto.keyboard.send_keys("{DOWN 2}")

        time.sleep(15)

        # Click on the "Déclaration d'Echanges de Biens" button
        pywinauto.mouse.click(button='left', coords=(200, 420))

        time.sleep(15)

        # Click on the "Vos DEB en ligne" button
        pywinauto.mouse.click(button='left', coords=(90, 305))

        time.sleep(5)

        # Click on the "Mois sans déclaration" button
        pywinauto.mouse.click(button='left', coords=(150, 305))

        time.sleep(5)


if __name__ == '__main__':
    unittest.main()
