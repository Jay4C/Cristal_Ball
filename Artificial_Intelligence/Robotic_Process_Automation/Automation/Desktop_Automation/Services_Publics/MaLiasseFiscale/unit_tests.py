import unittest
import time
from pywinauto.application import Application
import pywinauto.keyboard
import pywinauto.mouse
import pywinauto.base_wrapper
import pywinauto.timings
import os


class UnitTestsMaLiasseFiscale(unittest.TestCase):
    def test_remplir_ma_liasse_fiscale_2050_holomorphe(self):
        print("test_remplir_ma_liasse_fiscale_2050_holomorphe")

        time.sleep(6)

        app = Application(backend="uia")

        app.start("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")

        time.sleep(6)

        pywinauto.keyboard.send_keys("https://maliassefiscale.fr/Account/Login")

        time.sleep(6)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(6)

        # Click on the "Courrier électronique" input
        pywinauto.mouse.click(button='left', coords=(280, 310))

        time.sleep(6)

        # Insert the "Courrier électronique"
        pywinauto.keyboard.send_keys('.@outlook.fr')

        time.sleep(6)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(6)

        # Insert the "Mot de passe"
        pywinauto.keyboard.send_keys('')

        time.sleep(6)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(6)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(6)

        # Click on the "Completer" button
        pywinauto.mouse.click(button='left', coords=(1030, 480))

        time.sleep(6)

        # Press the 'Down' button in 10 times
        pywinauto.keyboard.send_keys("{DOWN 10}")

        time.sleep(6)

        # Click on the "Remplir" button for "2050 - Déclaration de résultat et annexes fiscales (Réél)"
        pywinauto.mouse.click(button='left', coords=(1190, 415))

        time.sleep(6)

        # Page 1

        # Press the 'Down' button in 7 times
        pywinauto.keyboard.send_keys("{DOWN 7}")

        time.sleep(6)

        # Click on the "AA - 1" input
        pywinauto.mouse.click(button='left', coords=(700, 475))

        time.sleep(3)

        # Insert the 'AA - 1' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Insert the 'AB - 1' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'AC - 2' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Insert the 'CX - 1' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'CQ - 2' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Insert the 'AF - 1' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'AG - 2' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Insert the 'AH - 1' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'AI - 2' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Insert the 'AJ - 1' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'AK - 2' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Insert the 'AL - 1' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'AM - 2' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Insert the 'AN - 1' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'AO - 2' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Insert the 'AP - 1' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'AQ - 2' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Insert the 'AR - 1' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'AS - 2' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Insert the 'AT - 1' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'AU - 2' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Insert the 'AV - 1' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'AW - 2' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Insert the 'AX - 1' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'AY - 2' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Insert the 'CS - 1' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'CT - 2' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Insert the 'CU - 1' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'CV - 2' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Insert the 'BB - 1' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'BC - 2' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Insert the 'BD - 1' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'BE - 2' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Insert the 'BH - 1' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'BI - 2' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Insert the 'BL - 1' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'BM - 2' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Insert the 'BN - 1' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'BO - 2' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Insert the 'BP - 1' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'BQ - 2' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Insert the 'BR - 1' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'BS - 2' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Insert the 'BT - 1' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'BU - 2' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Insert the 'BV - 1' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'BW - 2' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Insert the 'BX - 1' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'BY - 2' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Insert the 'BZ - 1' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'CA - 2' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Insert the 'CB - 1' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'CC - 2' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Insert the 'dont actions propres:' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'CD - 1' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'CE - 2' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Insert the 'CF - 1' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'CG - 2' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Insert the 'CH - 1' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'CI - 2' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Insert the 'CW - 1' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Insert the 'CM - 1' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Insert the 'CN - 1' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Insert the 'Renvois:(1) dont droit au bail:'
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'CP' input
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'Immobilisations :' input
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'Stocks :' input
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'Créances :' input
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'CR' input
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Click on the screen
        pywinauto.mouse.click(button='left', coords=(1270, 350))

        time.sleep(3)

        # Press the 'Down' button in 6 times
        pywinauto.keyboard.send_keys("{DOWN 6}")

        time.sleep(5)

        # Click on the "Enregistrer" button
        pywinauto.mouse.click(button='left', coords=(1200, 570))

        time.sleep(3)

        # Click on the "Next page" button
        pywinauto.mouse.click(button='left', coords=(405, 330))

        time.sleep(3)

        # Page 2

        # Click on the "Capital social ou individuel (1) * (Dont versé : )" input
        pywinauto.mouse.click(button='left', coords=(530, 660))

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'DA' input
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'DB' input
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'EK' input
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'DC' input
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'DD' input
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'DE' input
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'B1' input
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'DF' input
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'EJ' input
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'DG' input
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'DH' input
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'DI' input
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'DJ' input
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'DK' input
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Insert the 'DM' input
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'DN' input
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Insert the 'DP' input
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'DQ' input
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Insert the 'DS' input
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'DT' input
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'DU' input
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'EI' input
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'DV' input
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'DW' input
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'DX' input
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'DY' input
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'DZ' input
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'EA' input
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'EB' input
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Insert the 'ED' input
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Insert the '1B' input
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '1C' input
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '1D' input
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '1E' input
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'EF' input
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'EG' input
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'EH' input
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Click on the screen
        pywinauto.mouse.click(button='left', coords=(1230, 490))

        time.sleep(3)

        # Press the 'Down' button in 15 times
        pywinauto.keyboard.send_keys("{DOWN 15}")

        time.sleep(3)

        # Click on the "Enregistrer" button
        pywinauto.mouse.click(button='left', coords=(1200, 570))

        time.sleep(3)

        # Click on the "Next page" button
        pywinauto.mouse.click(button='left', coords=(405, 330))

        time.sleep(3)

        # Page 3

        # Click on the "FA" input
        pywinauto.mouse.click(button='left', coords=(665, 665))

        time.sleep(3)

        # Insert the 'FA' input
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'FB' input
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Insert the 'FD' input
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'FE' input
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Insert the 'FG' input
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'FH' input
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Insert the 'FG' input
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'FH' input
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Press the 'Enter' button for FJ
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Press the 'Enter' button for FK
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Press the 'Enter' button for FL
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Insert the 'FM' input
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'FN' input
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'FO' input
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'FP' input
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'FQ' input
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Insert the 'FS' input
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'FT' input
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'FU' input
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'FV' input
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'FW' input
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'FX' input
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'FY' input
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'FZ' input
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'GA' input
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'GB' input
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'GC' input
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'GD' input
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'GE' input
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Press the 'Enter' button for 'GF'
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Press the 'Enter' button for 'GG'
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Insert the 'GH' input
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'GI' input
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'GJ' input
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'GK' input
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'GL' input
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'GM' input
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'GN' input
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'GO' input
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Press the 'Enter' button for 'GP'
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Insert the 'GQ' input
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'GR' input
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'GS' input
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'GT' input
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Press the 'Enter' button for 'GU'
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Press the 'Enter' button for 'GV'
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Press the 'Enter' button for 'GW'
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Click on the "Enregistrer" button
        pywinauto.mouse.click(button='left', coords=(1200, 570))

        time.sleep(5)

        # Click on the "Next page" button
        pywinauto.mouse.click(button='left', coords=(405, 330))

        time.sleep(5)

        # Page 4

        # Click on the "HA" input
        pywinauto.mouse.click(button='left', coords=(1040, 640))

        time.sleep(3)

        # Insert the 'HA' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'HB' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'HC' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Press the 'Enter' button for 'HD'
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'HE' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'HF' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'HG' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Press the 'Enter' button for 'HH'
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Insert the 'HI' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'HJ' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'HK' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Press the 'Enter' button for 'HL'
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Press the 'Enter' button for 'HM'
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Press the 'Enter' button for 'HN'
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Insert the 'HO' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'HY' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '1G' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'HP' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'HQ' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'HQ' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '1H' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '1J' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '1K' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'HX' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'A1' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'A2' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'A3' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'A4' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'A6' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'A9' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'RC' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'RD' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'A5' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'A7' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'A8' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Click on the "Enregistrer" button
        pywinauto.mouse.click(button='left', coords=(1200, 570))

        time.sleep(3)

        # Click on the "Next page" button
        pywinauto.mouse.click(button='left', coords=(405, 330))

        time.sleep(3)

        # Page 5

        # Press the 'Down' button in 10 times
        pywinauto.keyboard.send_keys("{DOWN 2}")

        time.sleep(3)

        # Click on the "CZ =" button
        pywinauto.mouse.click(button='left', coords=(705, 605))

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Press the 'Enter' button for 'D8'
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Press the 'Enter' button for 'D9'
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Press the 'Enter' button for 'KD'
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Press the 'Enter' button for 'KE'
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Press the 'Enter' button for 'KF'
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Insert the 'KG' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'KH' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'KI' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'L9' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'KJ' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'KK' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'KL' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'M1' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'KM' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'KN' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'KO' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'M2' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'KP' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'KQ' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'KR' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'M3' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'KS' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'KT' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'KU' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'KV' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'KW' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'KX' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'KY' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'KZ' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'LA' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'LB' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'LC' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'LD' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'LE' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'LF' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'LG' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'LH' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'LI' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'LJ' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'LK' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'LL' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'LM' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Press the 'Enter' button for 'LN'
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Press the 'Enter' button for 'L0'
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Press the 'Enter' button for 'LP'
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Insert the '8G' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '8M' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '8T' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '8U' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '8V' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '8W' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '1P' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '1R' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '1S' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '1T' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '1U' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '1V' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Press the 'Enter' button for 'LQ'
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Press the 'Enter' button for 'LR'
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Press the 'Enter' button for 'LS'
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Press the 'Enter' button for '/oG'
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Press the 'Enter' button for '/oH'
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Press the 'Enter' button for '/oJ'
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Press the 'Enter' button for 'IN'
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Press the 'Enter' button for 'C/o'
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Press the 'Enter' button for 'D/o'
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Press the 'Enter' button for 'D7'
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Press the 'Enter' button for 'IO'
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Press the 'Enter' button for 'LV'
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Press the 'Enter' button for 'LW'
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Press the 'Enter' button for '1X'
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Insert the 'IP' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'LX' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'LY' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'LZ' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'IQ' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'MA' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'MB' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'MC' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'IR' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'MD' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'ME' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'MF' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'IS' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'MG' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'MH' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'MI' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'IT' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'MJ' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'MK' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'ML' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'IU' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)
        
        # Insert the 'MM' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'MO' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'IV' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'MP' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'MQ' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'MR' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'IW' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'MS' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'MT' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'MU' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'IX' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'MV' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'MW' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'MX' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'MY' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'MZ' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'NA' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'NB' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'NC' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'ND' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'NE' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'NF' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Press the 'Enter' button for 'IY'
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Press the 'Enter' button for 'NG'
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Press the 'Enter' button for 'NH'
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Press the 'Enter' button for 'NI'
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Insert the 'IZ' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '/oU' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'M7' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '/oW' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'I/o' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '/oX' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '/oY' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '/oZ' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'I1' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '2B' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '2C' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '2D' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'I2' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '2E' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '2F' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '2G' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Press the 'Enter' button for 'I3'
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Press the 'Enter' button for 'NJ'
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Press the 'Enter' button for 'NK'
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Press the 'Enter' button for '2H'
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Press the 'Enter' button for 'I4'
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Press the 'Enter' button for '/oK'
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Press the 'Enter' button for '/oL'
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Press the 'Enter' button for '/oM'
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Click on the "Enregistrer" button
        pywinauto.mouse.click(button='left', coords=(1200, 570))

        time.sleep(3)

        # Click on the "Next page" button
        pywinauto.mouse.click(button='left', coords=(405, 330))

        time.sleep(3)

        # Page 6

        # Press the 'Down' button in 10 times
        pywinauto.keyboard.send_keys("{DOWN 8}")

        time.sleep(3)

        # Click on the "1-1" input
        pywinauto.mouse.click(button='left', coords=(400, 470))

        time.sleep(3)

        # Insert the '1-1' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '1-2' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '1-3' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '1-4' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '1-5' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '1-6' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '2-1' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '2-2' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '2-3' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '2-4' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '2-5' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '2-6' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Insert the '3-1' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '3-2' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '3-3' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '3-4' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '3-5' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '3-6' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '4-1' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '4-2' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '4-3' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '4-4' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '4-5' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '4-6' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '5-1' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '5-2' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '5-3' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '5-4' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '5-5' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '5-6' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '6-1' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '6-2' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '6-3' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '6-4' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '6-5' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '6-6' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '7-1' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '7-2' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '7-3' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '7-4' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '7-5' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '7-6' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '8-1' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '8-2' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '8-3' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '8-4' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '8-5' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '8-6' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '9-1' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '9-2' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '9-3' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '9-4' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '9-5' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '9-6' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Press the 'Enter' button for '10-1'
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Press the 'Enter' button for '10-2'
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Press the 'Enter' button for '10-3'
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Press the 'Enter' button for '10-4'
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Press the 'Enter' button for '10-5'
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Press the 'Enter' button for '10-6'
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Insert the 'Cadre B - 1' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'Cadre B - 2' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'Cadre B - 3' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Click on the "Enregistrer" button
        pywinauto.mouse.click(button='left', coords=(1200, 570))

        time.sleep(3)

        # Click on the "Next page" button
        pywinauto.mouse.click(button='left', coords=(405, 330))

        time.sleep(3)

        # Page 7

        # Click on the "CY - =" button
        pywinauto.mouse.click(button='left', coords=(530, 710))

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Press the 'Enter' button for "EL"
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Press the 'Enter' button for "EM"
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Press the 'Enter' button for "EN"
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Press the 'Enter' button for "PE"
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Press the 'Enter' button for "PF"
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Press the 'Enter' button for "PG"
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Press the 'Enter' button for "PH"
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Insert the 'PI' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)
        
        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'PJ' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'PK' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'PL' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'PM' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'PN' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'PO' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'PQ' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'PR' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'PS' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'PT' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'PU' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'PV' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'PW' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'PX' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'PY' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'PZ' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'QA' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'QB' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'QC' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'QD' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'QE' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'QF' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'QG' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'QH' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'QI' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'QJ' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'QK' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'QL' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'QM' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'QN' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'QO' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'QP' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'QR' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'QS' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'QT' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Press the 'Enter' button for 'QU'
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Press the 'Enter' button for 'QV'
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Press the 'Enter' button for 'QW'
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Press the 'Enter' button for 'QX'
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Press the 'Enter' button for '/oN'
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Press the 'Enter' button for '/oP'
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Press the 'Enter' button for '/oQ'
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Press the 'Enter' button for '/oR'
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Press the 'Enter' button for 'M9'
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Press the 'Enter' button for 'N1'
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Press the 'Enter' button for 'N2'
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Press the 'Enter' button for 'N3'
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Press the 'Enter' button for 'N4'
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Press the 'Enter' button for 'N5'
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Press the 'Enter' button for 'N6'
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Press the 'Enter' button for 'N7'
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Press the 'Enter' button for 'N8'
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Press the 'Enter' button for 'P6'
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Press the 'Enter' button for 'P7'
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Press the 'Enter' button for 'P8'
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Press the 'Enter' button for 'P9'
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Press the 'Enter' button for 'Q1'
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Insert the 'Q2' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'Q3' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'Q4' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'Q5' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'Q6' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'Q7' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'Q8' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'Q9' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'R1' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'R2' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'R3' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'R4' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'R5' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'R6' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'R7' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'R8' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'R9' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'S1' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'S2' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'S3' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'S4' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'S5' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'S6' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'S7' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'S8' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'S9' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'T1' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'T2' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'T3' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'T4' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'T5' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'T6' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'T7' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'T8' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'T9' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'U1' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'U2' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'U3' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'U4' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'U5' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'U6' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)
        
        # Insert the 'U7' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'U8' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'U9' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'V1' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'V2' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'V3' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'V4' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'V5' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'V6' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'V7' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'V8' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'V9' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'W1' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'W2' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'W3' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'W4' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'W5' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'W6' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'W7' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'W8' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'W9' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'X1' value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Press the 'Enter' button for 'X2'
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Press the 'Enter' button for 'X3'
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Press the 'Enter' button for 'X4'
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Press the 'Enter' button for 'X5'
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Press the 'Enter' button for 'X6'
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Press the 'Enter' button for 'X7'
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Press the 'Enter' button for 'X8'
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Press the 'Enter' button for 'NL'
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Press the 'Enter' button for 'NM'
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Press the 'Enter' button for 'NO'
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Press the 'Enter' button for 'NP'
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Press the 'Enter' button for 'NQ'
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Press the 'Enter' button for 'NR'
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Press the 'Enter' button for 'NS'
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Press the 'Enter' button for 'NT'
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Press the 'Enter' button for 'NU'
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Press the 'Enter' button for 'NV'
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Press the 'Enter' button for 'NW'
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Press the 'Enter' button for 'NY'
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Press the 'Enter' button for 'NZ'
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Insert the '1-1' value in cadre c
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '1-2' value in cadre c
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'Z9' value in cadre c
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'Z8' value in cadre c
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '2-1' value in cadre c
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '2-2' value in cadre c
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'SP' value in cadre c
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'SR' value in cadre c
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Click on the "Enregistrer" button
        pywinauto.mouse.click(button='left', coords=(1200, 570))

        time.sleep(3)

        # Click on the "Next page" button
        pywinauto.mouse.click(button='left', coords=(405, 330))

        time.sleep(3)

        # Page 8

        # Click on the "3T" input
        pywinauto.mouse.click(button='left', coords=(575, 705))

        time.sleep(3)

        # Insert the '3T' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'TA' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'TB' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'TC' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '3U' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'TD' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'TE' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'TF' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '3V' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'TG' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'TH' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'TI' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '3X' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'TM' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'TN' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'TO' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'D3' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'D4' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'D5' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'D6' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'IJ' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'IK' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'IL' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'IM' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '3Y' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'TP' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'TQ' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'TR' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Press the 'Enter' button for '3Z'
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)
        
        # Press the 'Enter' button for 'TS'
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Press the 'Enter' button for 'TT'
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Press the 'Enter' button for 'TU'
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Insert the '4A' input
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '4B' input
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '4C' input
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '4D' input
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '4E' input
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '4F' input
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '4G' input
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '4H' input
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '4J' input
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '4K' input
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '4L' input
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '4M' input
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)
        
        # Insert the '4N' input
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '4P' input
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '4R' input
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '4S' input
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '4T' input
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '4U' input
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '4V' input
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '4W' input
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)
        
        # Insert the '4X' input
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '4Y' input
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)
        
        # Insert the '4Z' input
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '5A' input
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)
        
        # Insert the '5B' input
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '5C' input
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '5D' input
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '5E' input
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '5F' input
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '5H' input
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '5J' input
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '5K' input
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'EO' input
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'EP' input
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'EQ' input
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'ER' input
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '5R' input
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '5S' input
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '5T' input
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '5U' input
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '5V' input
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)
        
        # Insert the '5W' input
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '5X' input
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '5Y' input
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Press the "Enter" button for '5Z'
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Press the "Enter" button for 'TV'
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Press the "Enter" button for 'TW'
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Press the "Enter" button for 'TX'
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Insert the "6A" input
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the "6B" input
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the "6C" input
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the "6D" input
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the "6E" input
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the "6F" input
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the "6G" input
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the "6H" input
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the "/o2" input
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the "/o3" input
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the "/o4" input
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the "/o5" input
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the "9U" input
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the "9V" input
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the "9W" input
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the "9X" input
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the "/o6" input
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the "/o7" input
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the "/o8" input
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the "/o9" input
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the "6N" input
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the "6P" input
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the "6R" input
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the "6S" input
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the "6T" input
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the "6U" input
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the "6V" input
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the "6W" input
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the "6X" input
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the "6Y" input
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the "6Z" input
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the "7A" input
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Press the "Enter" button for "7B"
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Press the "Enter" button for "TY"
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Press the "Enter" button for "TZ"
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Press the "Enter" button for "UA"
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Press the "Enter" button for "7C"
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Press the "Enter" button for "UB"
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Press the "Enter" button for "UC"
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Press the "Enter" button for "UD"
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Insert the "UE" value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)
        
        # Insert the "UF" value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the "UG" value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the "UH" value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the "UJ" value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the "UK" value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the "10" value
        pywinauto.keyboard.send_keys('0')

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Click on the "Enregistrer" button
        pywinauto.mouse.click(button='left', coords=(1200, 570))

        time.sleep(3)

        # Click on the "Next page" button
        pywinauto.mouse.click(button='left', coords=(405, 330))

        time.sleep(3)

        # Page 9

        # Click on the "UL" input
        pywinauto.mouse.click(button='left', coords=(770, 670))

        time.sleep(3)

        # Insert the "UL" value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the "UM" value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the "UN" value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the "UP" value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)
        
        # Insert the "UR" value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the "US" value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the "UT" value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)
        
        # Insert the "VA - 2" value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the "UW" value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the "VA - 1" value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the "UV" value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the "VA - 3" value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the "UX - 1" value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the "UX - 2" value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the "UX - 3" value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)
        
        # Insert the "UO" value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the "Z1 - 1" value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the "Z1 - 2" value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the "Z1 - 3" value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the "UY - 1" value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the "UY - 2" value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the "UY - 3" value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the "UZ - 1" value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the "UZ - 2" value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the "UZ - 3" value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the "VM - 1" value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the "VM - 2" value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the "VM - 3" value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the "VB - 1" value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the "VB - 2" value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the "VB - 3" value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the "VN - 1" value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the "VN - 2" value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the "VN - 3" value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the "VP - 1" value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the "VP - 2" value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the "VP - 3" value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the "VC - 1" value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the "VC - 2" value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the "VC - 3" value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the "VR - 1" value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the "VR - 2" value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the "VR - 3" value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the "VS - 1" value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the "VS - 2" value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the "VS - 3" value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Press the 'ENTER' button for "VT"
        pywinauto.keyboard.send_keys("{ENTER}")

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Press the 'ENTER' button for "VU"
        pywinauto.keyboard.send_keys("{ENTER}")

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Press the 'ENTER' button for "VV"
        pywinauto.keyboard.send_keys("{ENTER}")

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)
        
        # Insert the 'VD' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'VE' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'VF' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '7Y - 1' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '7Y - 2' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '7Y - 3' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '7Y - 4' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '7Z - 1' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '7Z - 2' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '7Z - 3' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '7Z - 4' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'VG - 1' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'VG - 2' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'VG - 3' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'VG - 4' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'VH - 1' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'VH - 2' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'VH - 3' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'VH - 4' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '8A - 1' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '8A - 2' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '8A - 3' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '8A - 4' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '8B - 1' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '8B - 2' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '8B - 3' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '8B - 4' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '8C - 1' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '8C - 2' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '8C - 3' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '8C - 4' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '8D - 1' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '8D - 2' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '8D - 3' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '8D - 4' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '8E - 1' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '8E - 2' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '8E - 3' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '8E - 4' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'VW - 1' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'VW - 2' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'VW - 3' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'VW - 4' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'VX - 1' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'VX - 2' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'VX - 3' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'VX - 4' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'VQ - 1' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'VQ - 2' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'VQ - 3' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'VQ - 4' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '8J - 1' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '8J - 2' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '8J - 3' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '8J - 4' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'VI - 1' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'VI - 2' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'VI - 3' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'VI - 4' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '8K - 1' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '8K - 2' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '8K - 3' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '8K - 4' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'Z2 - 1' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'Z2 - 2' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'Z2 - 3' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'Z2 - 4' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '8L - 1' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '8L - 2' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '8L - 3' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '8L - 4' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Press the 'Enter' button for "VY"
        pywinauto.keyboard.send_keys("{ENTER}")

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Press the 'Enter' button for "VZ - 2"
        pywinauto.keyboard.send_keys("{ENTER}")

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Press the 'Enter' button for "VZ - 3"
        pywinauto.keyboard.send_keys("{ENTER}")

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Press the 'Enter' button for "VZ - 4"
        pywinauto.keyboard.send_keys("{ENTER}")

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Insert the 'VJ' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'VL' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'VK' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Click on the "Enregistrer" button
        pywinauto.mouse.click(button='left', coords=(1200, 570))

        time.sleep(3)

        # Click on the "Next page" button
        pywinauto.mouse.click(button='left', coords=(405, 330))

        time.sleep(3)

        # Page 10

        # Click on the "WA" input
        pywinauto.mouse.click(button='left', coords=(990, 585))

        time.sleep(3)

        # Insert the 'WA' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'WB' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)
        
        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'PP' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'WD' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'WE' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'XE' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'WF' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'WG' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'WI' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'XX' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)
        
        # Insert the 'XW' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'WJ' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'XZ' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'XY' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)
        
        # Insert the 'I7' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'WL' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'L7' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'K7' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'I8' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'ZN' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'WN' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'WO' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'XR' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)
        
        # Insert the 'SU' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'SW' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'WQ' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'SX' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'M8' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Insert the 'WR' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'WS' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'WT' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'WU' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'WV' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'WH' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'WP' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'WW' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'XB' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'I6' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'WZ' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '2A' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'XA' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'ZY' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'XD' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'K9' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'L2' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'L5' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'XF' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'K3' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'PA' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '/oV' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '1F' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'XC' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'PC' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'XS' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'ZI' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'XG' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'XH' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'XI' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'XJ' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'ZL' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'XL' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'XN' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'XO' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'Y1' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'Y3' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'X9' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'RA' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'RB' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'Y2' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'ZX' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'YA' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'YB' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'YH' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'YC' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'YD' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'PB' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'YI' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'YL' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Click on the "Enregistrer" button
        pywinauto.mouse.click(button='left', coords=(1200, 570))

        time.sleep(3)

        # Click on the "Next page" button
        pywinauto.mouse.click(button='left', coords=(405, 330))

        time.sleep(3)

        # Page 11

        # Click on the "K4" input
        pywinauto.mouse.click(button='left', coords=(1030, 660))

        time.sleep(3)

        # Insert the 'K4' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'K5' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'K6' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'YJ' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'YK' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'ZT' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Insert the 'YN' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Insert the 'YO' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'L1 - Montant au début de l'exercice' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'L1 - Imputations' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'L1 - Montant net à la fin de l'exercice' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'ZW' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'ZV' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Click on the "Enregistrer" button
        pywinauto.mouse.click(button='left', coords=(1200, 570))

        time.sleep(3)

        # Click on the "Next page" button
        pywinauto.mouse.click(button='left', coords=(405, 330))

        time.sleep(3)

        # Page 12

        # Click on the "/oC" input
        pywinauto.mouse.click(button='left', coords=(640, 630))

        time.sleep(3)

        # Insert the '/oC' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'ZB' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'ZD' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '/oD' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'ZE' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'ZF' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '/oE' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'ZG' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Insert the '/oF' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Insert the 'J7' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'YQ' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'YR' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'YS' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'YT' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'J8' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'XQ' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'YU' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'SS' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'YV' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'ES' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'ST' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'ZJ' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'YW' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'ZS' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '9Z' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'YX' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'YY' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'YZ' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '/oB' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '/oS' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'ZK' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'XP' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Press the 'Enter' in 2 times
        pywinauto.keyboard.send_keys("{ENTER 2}")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'JA' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'JK' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'JL' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'JM' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'JC' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'JD' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'JN' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'JO' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'JP' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'JF' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Insert the 'JJ' value
        pywinauto.keyboard.send_keys("")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'RG' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'RH' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Click on the "Enregistrer" button
        pywinauto.mouse.click(button='left', coords=(1200, 570))

        time.sleep(3)

        # Click on the "Page 1" button
        pywinauto.mouse.click(button='left', coords=(440, 295))

        time.sleep(3)

        print("ccleaner running")
        os.system("set ccleaner='C:\\Program Files\\CCleaner\\CCleaner.exe'")
        os.system("start ccleaner /AUTO")

        time.sleep(3)

    def test_remplir_ma_liasse_fiscale_2059_holomorphe(self):
        print('test_declarer_ma_liasse_fiscale_2059_holomorphe')

        time.sleep(6)

        app = Application(backend="uia")

        app.start("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")

        time.sleep(6)

        pywinauto.keyboard.send_keys("https://maliassefiscale.fr/Account/Login")

        time.sleep(6)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(6)

        # Click on the "Courrier électronique" input
        pywinauto.mouse.click(button='left', coords=(280, 310))

        time.sleep(6)

        # Insert the "Courrier électronique"
        pywinauto.keyboard.send_keys('.@outlook.fr')

        time.sleep(6)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(6)

        # Insert the "Mot de passe"
        pywinauto.keyboard.send_keys('')

        time.sleep(6)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(6)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(6)

        # Click on the "Completer" button
        pywinauto.mouse.click(button='left', coords=(1030, 480))

        time.sleep(6)

        # Press the 'Down' button in 10 times
        pywinauto.keyboard.send_keys("{DOWN 10}")

        time.sleep(6)

        # Click on the "Remplir" button for "2059 - Complément à la déclaration d'impôt sur les sociétés"
        pywinauto.mouse.click(button='left', coords=(1200, 465))

        time.sleep(6)

        # Page 1

        # Click on the "Neant" button
        pywinauto.mouse.click(button='left', coords=(1030, 535))

        time.sleep(3)

        # Click on the "Continuer" button
        pywinauto.mouse.click(button='left', coords=(900, 340))

        time.sleep(3)

        # Click on the "Enregistrer" button
        pywinauto.mouse.click(button='left', coords=(1200, 300))

        time.sleep(3)

        # Click on the "Next page" button
        pywinauto.mouse.click(button='left', coords=(770, 300))

        time.sleep(3)

        # Page 2

        # Click on the "Neant" button
        pywinauto.mouse.click(button='left', coords=(1110, 550))

        time.sleep(3)

        # Click on the "Continuer" button
        pywinauto.mouse.click(button='left', coords=(900, 340))

        time.sleep(3)

        # Click on the "Enregistrer" button
        pywinauto.mouse.click(button='left', coords=(1200, 300))

        time.sleep(3)

        # Click on the "Next page" button
        pywinauto.mouse.click(button='left', coords=(770, 300))

        time.sleep(3)

        # Page 3

        # Click on the "Neant" button
        pywinauto.mouse.click(button='left', coords=(1110, 555))

        time.sleep(3)

        # Click on the "Continuer" button
        pywinauto.mouse.click(button='left', coords=(900, 340))

        time.sleep(3)

        # Click on the "Enregistrer" button
        pywinauto.mouse.click(button='left', coords=(1200, 300))

        time.sleep(3)

        # Click on the "Next page" button
        pywinauto.mouse.click(button='left', coords=(770, 300))

        time.sleep(3)

        # Page 4

        # Click on the "Neant" button
        pywinauto.mouse.click(button='left', coords=(1115, 590))

        time.sleep(3)

        # Click on the "Continuer" button
        pywinauto.mouse.click(button='left', coords=(900, 340))

        time.sleep(3)

        # Click on the "Enregistrer" button
        pywinauto.mouse.click(button='left', coords=(1200, 300))

        time.sleep(3)

        # Click on the "Next page" button
        pywinauto.mouse.click(button='left', coords=(770, 300))

        time.sleep(3)

        # Page 5

        # Click on the "YP" input
        pywinauto.mouse.click(button='left', coords=(1030, 630))

        time.sleep(3)

        # Insert the "YP" value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the "YF" value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the "YG" value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the "RL" value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Click on the screen
        pywinauto.mouse.click(button='left', coords=(1230, 770))

        time.sleep(3)

        # Press the 'DOWN' button in 2 times
        pywinauto.keyboard.send_keys("{DOWN 12}")

        time.sleep(3)

        # Click on the "OA" input
        pywinauto.mouse.click(button='left', coords=(1100, 180))

        time.sleep(3)

        # Insert the "OA" value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Click on the "OK" input
        pywinauto.mouse.click(button='left', coords=(1100, 205))

        time.sleep(3)

        # Insert the "OK" value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Click on the "OL" input
        pywinauto.mouse.click(button='left', coords=(1100, 235))

        time.sleep(3)

        # Insert the "OL" value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Click on the "OT" input
        pywinauto.mouse.click(button='left', coords=(1100, 255))

        time.sleep(3)

        # Insert the "OT" value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the "TAB" button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Press the "Enter" button
        pywinauto.keyboard.send_keys("{ENTER}")

        time.sleep(3)

        # Click on the "OH" input
        pywinauto.mouse.click(button='left', coords=(1100, 335))

        time.sleep(3)

        # Insert the "OH" value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Click on the "OE" input
        pywinauto.mouse.click(button='left', coords=(1100, 360))

        time.sleep(3)

        # Insert the "OE" value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Click on the "OF" input
        pywinauto.mouse.click(button='left', coords=(1100, 385))

        time.sleep(3)

        # Insert the "OF" value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Click on the "OD" input
        pywinauto.mouse.click(button='left', coords=(1100, 410))

        time.sleep(3)

        # Insert the "OD" value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Click on the "OI" input
        pywinauto.mouse.click(button='left', coords=(1100, 430))

        time.sleep(3)

        # Insert the "OI" value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Click on the "XT" input
        pywinauto.mouse.click(button='left', coords=(1100, 455))

        time.sleep(3)

        # Insert the "XT" value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Click on the "OM" input
        pywinauto.mouse.click(button='left', coords=(1100, 480))

        time.sleep(3)

        # Insert the "OM" value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Click on the screen
        pywinauto.mouse.click(button='left', coords=(1240, 480))

        time.sleep(3)

        # Press the "Down" button in 7 times
        pywinauto.keyboard.send_keys("{DOWN 7}")

        time.sleep(3)

        # Click on the "ON" input
        pywinauto.mouse.click(button='left', coords=(1100, 180))

        time.sleep(3)

        # Insert the "ON" value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Click on the "OQ" input
        pywinauto.mouse.click(button='left', coords=(1100, 205))

        time.sleep(3)

        # Insert the "OQ" value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Click on the "OR" input
        pywinauto.mouse.click(button='left', coords=(1100, 230))

        time.sleep(3)

        # Insert the "OR" value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Click on the "OS" input
        pywinauto.mouse.click(button='left', coords=(1100, 260))

        time.sleep(3)

        # Insert the "OS" value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Click on the "OZ" input
        pywinauto.mouse.click(button='left', coords=(1100, 290))

        time.sleep(3)

        # Insert the "OZ" value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Click on the "OW" input
        pywinauto.mouse.click(button='left', coords=(1100, 315))

        time.sleep(3)

        # Insert the "OW" value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Click on the "OU" input
        pywinauto.mouse.click(button='left', coords=(1100, 340))

        time.sleep(3)

        # Insert the "OU" value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Click on the "O9" input
        pywinauto.mouse.click(button='left', coords=(1100, 365))

        time.sleep(3)

        # Insert the "O9" value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Click on the "OY" input
        pywinauto.mouse.click(button='left', coords=(1100, 390))

        time.sleep(3)

        # Insert the "OY" value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Click on the "OJ" input
        pywinauto.mouse.click(button='left', coords=(1100, 415))

        time.sleep(3)

        # Insert the "OJ" value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Click on the "OG" input
        pywinauto.mouse.click(button='left', coords=(1100, 470))

        time.sleep(3)

        # Insert the "OG" value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Click on the "SA" input
        pywinauto.mouse.click(button='left', coords=(1100, 530))

        time.sleep(3)

        # Insert the "SA" value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Click on the screen
        pywinauto.mouse.click(button='left', coords=(1230, 540))

        time.sleep(3)

        # Press the 'DOWN' button in 7 times
        pywinauto.keyboard.send_keys("{DOWN 7}")

        time.sleep(3)

        # Click on the "EV" checkbox
        pywinauto.mouse.click(button='left', coords=(630, 280))

        time.sleep(3)

        # Click on the "GX" input
        pywinauto.mouse.click(button='left', coords=(640, 305))

        time.sleep(3)

        # Insert the "GX" value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Click on the "EY" input
        pywinauto.mouse.click(button='left', coords=(1030, 305))

        time.sleep(3)

        # Insert the "EY" value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Click on the "HX" input
        pywinauto.mouse.click(button='left', coords=(1030, 330))

        time.sleep(3)

        # Insert the "HX" value
        pywinauto.keyboard.send_keys("")

        time.sleep(3)

        # Click on the "GY" input
        pywinauto.mouse.click(button='left', coords=(390, 360))

        time.sleep(3)

        # Insert the "GY" value
        pywinauto.keyboard.send_keys("01/04/2020")

        time.sleep(3)

        # Click on the "GZ" input
        pywinauto.mouse.click(button='left', coords=(670, 360))

        time.sleep(3)

        # Insert the "GZ" value
        pywinauto.keyboard.send_keys("31/12/2020")

        time.sleep(3)

        # Click on the "HR" input
        pywinauto.mouse.click(button='left', coords=(400, 385))

        time.sleep(3)

        # Insert the "HR" value
        pywinauto.keyboard.send_keys("")

        time.sleep(3)

        # Click on the screen
        pywinauto.mouse.click(button='left', coords=(1270, 380))

        time.sleep(3)

        # Press the 'DOWN' button in 5 times
        pywinauto.keyboard.send_keys("{DOWN 5}")

        time.sleep(3)

        # Click on the "Enregistrer" button
        pywinauto.mouse.click(button='left', coords=(1200, 605))

        time.sleep(3)

        # Click on the "Next page" button
        pywinauto.mouse.click(button='left', coords=(770, 300))

        time.sleep(3)

        # Page 6

        # Press the 'DOWN' button in 23 times
        pywinauto.keyboard.send_keys("{DOWN 23}")

        time.sleep(3)

        # Click on the "Titre" input
        pywinauto.mouse.click(button='left', coords=(300, 215))

        time.sleep(3)

        # Insert the "Titre" value
        pywinauto.keyboard.send_keys("M")

        time.sleep(3)

        # Click on the "Nom patronymique" input
        pywinauto.mouse.click(button='left', coords=(555, 215))

        time.sleep(3)

        # Insert the "Nom patronymique" value
        pywinauto.keyboard.send_keys("ALOYAU")

        time.sleep(3)

        # Click on the "Prénom(s)" input
        pywinauto.mouse.click(button='left', coords=(915, 215))

        time.sleep(3)

        # Insert the "Prénom(s)" value
        pywinauto.keyboard.send_keys("Jason Aymérick Jean Claudius")

        time.sleep(3)

        # Click on the "% de détention" input
        pywinauto.mouse.click(button='left', coords=(855, 250))

        time.sleep(3)

        # Insert the "% de détention" value
        pywinauto.keyboard.send_keys("100")

        time.sleep(3)

        # Click on the "Nb de parts ou actions" input
        pywinauto.mouse.click(button='left', coords=(1075, 250))

        time.sleep(3)

        # Insert the "Nb de parts ou actions" value
        pywinauto.keyboard.send_keys("50")

        time.sleep(3)

        # Click on the "Date de naissance" input
        pywinauto.mouse.click(button='left', coords=(420, 280))

        time.sleep(3)

        # Insert the "Date de naissance" value
        pywinauto.keyboard.send_keys("11/11/1993")

        time.sleep(3)

        # Click on the "N° département de naissance" input
        pywinauto.mouse.click(button='left', coords=(665, 280))

        time.sleep(3)

        # Insert the "N° département de naissance" value
        pywinauto.keyboard.send_keys("974")

        time.sleep(3)

        # Click on the "Commune de naissance" input
        pywinauto.mouse.click(button='left', coords=(800, 280))

        time.sleep(3)

        # Insert the "Commune de naissance" value
        pywinauto.keyboard.send_keys("Saint-Louis (97450)")

        time.sleep(3)

        # Click on the "Pays de naissance" input
        pywinauto.mouse.click(button='left', coords=(1070, 280))

        time.sleep(3)

        # Insert the "Pays de naissance" value
        pywinauto.keyboard.send_keys("fr")
        pywinauto.keyboard.send_keys("{ENTER}")

        time.sleep(3)

        # Click on the "Adresse de domicile - N°" input
        pywinauto.mouse.click(button='left', coords=(370, 310))

        time.sleep(3)

        # Insert the "Adresse de domicile - N°" value
        pywinauto.keyboard.send_keys("6")

        time.sleep(3)

        # Click on the "Adresse de domicile - Voie" input
        pywinauto.mouse.click(button='left', coords=(670, 310))

        time.sleep(3)

        # Insert the "Adresse de domicile - Voie" value
        pywinauto.keyboard.send_keys("Avenue Léon Blum - Etage Appartement 6")

        time.sleep(3)

        # Click on the "Adresse de domicile - Code postal" input
        pywinauto.mouse.click(button='left', coords=(380, 345))

        time.sleep(3)

        # Insert the "Adresse de domicile - Code postal" value
        pywinauto.keyboard.send_keys("93800")

        time.sleep(3)

        # Click on the "Adresse de domicile - Commune" input
        pywinauto.mouse.click(button='left', coords=(665, 354))

        time.sleep(3)

        # Insert the "Adresse de domicile - Commune" value
        pywinauto.keyboard.send_keys("Epinay-sur-Seine")

        time.sleep(3)

        # Click on the "Adresse de domicile - Pays" input
        pywinauto.mouse.click(button='left', coords=(1000, 345))

        time.sleep(3)

        # Insert the "Adresse de domicile - Pays" value
        pywinauto.keyboard.send_keys("fr")
        pywinauto.keyboard.send_keys("{ENTER}")

        time.sleep(3)

        # Click on the screen
        pywinauto.mouse.click(button='left', coords=(1250, 440))

        time.sleep(3)

        # Press the "DOWN" button in 8 times
        pywinauto.keyboard.send_keys("{DOWN 8}")

        time.sleep(3)

        # Click on the "Enregistrer" button
        pywinauto.mouse.click(button='left', coords=(1200, 605))

        time.sleep(3)

        # Click on the "Next page" button
        pywinauto.mouse.click(button='left', coords=(770, 300))

        time.sleep(3)

        # Page 7

        # Click on the "Neant" button
        pywinauto.mouse.click(button='left', coords=(1115, 555))

        time.sleep(3)

        # Click on the "Continuer" button
        pywinauto.mouse.click(button='left', coords=(900, 330))

        time.sleep(3)
        
        # Click on the "Enregistrer" button
        pywinauto.mouse.click(button='left', coords=(1200, 290))

        time.sleep(3)

        # Click on the "Next page" button
        pywinauto.mouse.click(button='left', coords=(770, 300))

        time.sleep(3)

        # Page 8

        # Click on the "Neant" button
        pywinauto.mouse.click(button='left', coords=(1160, 635))

        time.sleep(3)

        # Click on the "Enregistrer" button
        pywinauto.mouse.click(button='left', coords=(1200, 290))

        time.sleep(3)

        print("ccleaner running")
        os.system("set ccleaner='C:\\Program Files\\CCleaner\\CCleaner.exe'")
        os.system("start ccleaner /AUTO")

        time.sleep(3)

    def test_remplir_ma_liasse_fiscale_2065_holomorphe(self):
        print("test_declarer_ma_liasse_fiscale_2065_holomorphe")

        time.sleep(6)

        app = Application(backend="uia")

        app.start("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")

        time.sleep(3)

        pywinauto.keyboard.send_keys("https://maliassefiscale.fr/Account/Login")

        time.sleep(3)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(6)

        # Click on the "Courrier électronique" input
        pywinauto.mouse.click(button='left', coords=(280, 310))

        time.sleep(3)

        # Insert the "Courrier électronique"
        pywinauto.keyboard.send_keys('.@outlook.fr')

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the "Mot de passe"
        pywinauto.keyboard.send_keys('')

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(6)

        # Click on the "Completer" button
        pywinauto.mouse.click(button='left', coords=(1030, 480))

        time.sleep(6)

        # Press the 'Down' button in 10 times
        pywinauto.keyboard.send_keys("{DOWN 10}")

        time.sleep(6)

        # Click on the "Remplir" button for "2065 - Déclaration d'impôt sur les sociétés"
        pywinauto.mouse.click(button='left', coords=(1200, 520))

        time.sleep(6)

        # Page 1

        # Click on the "Régime réel normal" checkbox
        pywinauto.mouse.click(button='left', coords=(1195, 625))

        time.sleep(3)

        # Press the 'Down' button in 10 times
        pywinauto.keyboard.send_keys("{DOWN 10}")

        time.sleep(3)

        # Click on the "N° voie + type et nom de voie" input
        pywinauto.mouse.click(button='left', coords=(725, 245))

        time.sleep(3)

        # Insert the 'N° voie + type et nom de voie' value
        pywinauto.keyboard.send_keys("31 Avenue de Ségur - ABC LIV")

        time.sleep(3)

        # Click on the "Lieu-dit, hameau" input
        pywinauto.mouse.click(button='left', coords=(710, 270))

        time.sleep(3)

        # Insert the 'Lieu-dit, hameau' value
        pywinauto.keyboard.send_keys("")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'Code' value
        pywinauto.keyboard.send_keys("75007")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'Ville' value
        pywinauto.keyboard.send_keys("Paris")

        time.sleep(3)

        # Click on the "Pays" list
        pywinauto.mouse.click(button='left', coords=(1140, 270))

        time.sleep(3)

        # Insert the 'Pays' value
        pywinauto.keyboard.send_keys("fr")
        pywinauto.keyboard.send_keys("{ENTER}")

        time.sleep(3)

        # Click on the "Activités exercées" input
        pywinauto.mouse.click(button='left', coords=(380, 500))

        time.sleep(3)

        # Insert the 'Activités exercées' value
        pywinauto.keyboard.send_keys("Commerce de gros de produits chimiques, Edition de logiciels")

        time.sleep(3)

        # Click on the "Bénéfice imposable à 28%" input
        pywinauto.mouse.click(button='left', coords=(950, 550))

        time.sleep(3)

        # Insert the 'Bénéfice imposable à 28%' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Click on the screen
        pywinauto.mouse.click(button='left', coords=(1280, 550))

        time.sleep(3)

        # Press the 'Down' button in 20 times
        pywinauto.keyboard.send_keys("{DOWN 20}")

        time.sleep(3)

        # Click on the "L'entreprise dispose-t-elle d'une comptabilité informatisée ?" list
        pywinauto.mouse.click(button='left', coords=(620, 245))

        time.sleep(3)

        # Choose "Oui"
        pywinauto.keyboard.send_keys("o")
        pywinauto.keyboard.send_keys("{ENTER}")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'Si oui, indication du logiciel utilisé' input
        pywinauto.keyboard.send_keys("Logiciel maison (Open office Calc / Python)")

        time.sleep(3)

        # Click on the "Professionnel de l'expertise comptable - Nom, Prénoms" input
        pywinauto.mouse.click(button='left', coords=(205, 370))

        time.sleep(3)

        # Insert the 'Professionnel de l'expertise comptable - Nom, Prénoms' input
        pywinauto.keyboard.send_keys("ALOYAU Jason")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'Professionnel de l'expertise comptable - Adresse' input
        pywinauto.keyboard.send_keys("6 Avenue Léon Blum - Etage 1 Appartement 6")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'Professionnel de l'expertise comptable - Code' input
        pywinauto.keyboard.send_keys("93800")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'Professionnel de l'expertise comptable - Ville' input
        pywinauto.keyboard.send_keys("Epinay-sur-Seine")

        time.sleep(3)

        # Click on the "Professionnel de l'expertise comptable - Pays" input
        pywinauto.mouse.click(button='left', coords=(205, 395))

        time.sleep(3)

        # Insert the 'Professionnel de l'expertise comptable - Pays' input
        pywinauto.keyboard.send_keys("fr")
        pywinauto.keyboard.send_keys("{ENTER}")

        time.sleep(3)

        # Click on the "Professionnel de l'expertise comptable - Telephone" input
        pywinauto.mouse.click(button='left', coords=(530, 395))

        time.sleep(3)

        # Insert the 'Professionnel de l'expertise comptable - Telephone' input
        pywinauto.keyboard.send_keys("0749163329")

        time.sleep(3)

        # Click on the "Identité du déclarant - Date de naissance" input
        pywinauto.mouse.click(button='left', coords=(740, 435))

        time.sleep(3)

        # Insert the 'Identité du déclarant - Date de naissance' input
        pywinauto.keyboard.send_keys("11/11/1993")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'Identité du déclarant - Lieu' input
        pywinauto.keyboard.send_keys("Saint-Louis (97450)")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'Identité du déclarant - Qualité' input
        pywinauto.keyboard.send_keys("Président")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'Identité du déclarant - Nom du signataire' input
        pywinauto.keyboard.send_keys("ALOYAU Jason")

        time.sleep(3)

        # Click on the "Enregistrer" button
        pywinauto.mouse.click(button='left', coords=(1200, 600))

        time.sleep(3)

        # Click on the "Next page" button
        pywinauto.mouse.click(button='left', coords=(675, 330))

        time.sleep(3)

        # Page 2

        time.sleep(3)

        # Click on the "a" input
        pywinauto.mouse.click(button='left', coords=(640, 540))

        time.sleep(3)

        # Insert the "a" value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the "b" value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the "c" value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the "d" value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the "i" value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the "j" value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 1 time
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Press the 'ENTER' button in 1 time
        pywinauto.keyboard.send_keys("{ENTER}")

        time.sleep(3)

        # Click on the screen
        pywinauto.mouse.click(button='left', coords=(1280, 450))

        time.sleep(3)

        # Press the 'DOWN' button in 25 times
        pywinauto.keyboard.send_keys("{DOWN 25}")

        time.sleep(3)

        # Click on the "Enregistrer" button
        pywinauto.mouse.click(button='left', coords=(1200, 600))

        time.sleep(3)

    def test_declarer_ma_liasse_fiscale_2050_holomorphe_neant(self):
        print("test_declarer_ma_liasse_fiscale_2050_holomorphe_neant")

        time.sleep(6)

        app = Application(backend="uia")

        app.start("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")

        time.sleep(6)

        pywinauto.keyboard.send_keys("https://maliassefiscale.fr/Account/Login")

        time.sleep(6)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(6)

        # Click on the "Courrier électronique" input
        pywinauto.mouse.click(button='left', coords=(280, 310))

        time.sleep(6)

        # Insert the "Courrier électronique"
        pywinauto.keyboard.send_keys('.@outlook.fr')

        time.sleep(6)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(6)

        # Insert the "Mot de passe"
        pywinauto.keyboard.send_keys('')

        time.sleep(6)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(6)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(6)

        # Click on the "Completer" button
        pywinauto.mouse.click(button='left', coords=(1030, 480))

        time.sleep(6)

        # Press the 'Down' button in 10 times
        pywinauto.keyboard.send_keys("{DOWN 10}")

        time.sleep(3)

        # Click on the "Remplir" button for "2050 - Déclaration de résultat et annexes fiscales (Réél)"
        pywinauto.mouse.click(button='left', coords=(1200, 415))

        time.sleep(6)

        # Page 1

        # Click on the "Neant" button
        pywinauto.mouse.click(button='left', coords=(1155, 600))

        time.sleep(3)

        # Click on the "Continuer" button
        pywinauto.mouse.click(button='left', coords=(900, 340))

        time.sleep(3)

        # Click on the "Enregistrer" button
        pywinauto.mouse.click(button='left', coords=(1200, 300))

        time.sleep(3)

        # Click on the "Next page" button
        pywinauto.mouse.click(button='left', coords=(400, 330))

        time.sleep(3)

        # Page 2

        # Click on the "Neant" button
        pywinauto.mouse.click(button='left', coords=(1100, 600))

        time.sleep(3)

        # Click on the "Continuer" button
        pywinauto.mouse.click(button='left', coords=(900, 340))

        time.sleep(3)

        # Click on the "Enregistrer" button
        pywinauto.mouse.click(button='left', coords=(1200, 300))

        time.sleep(3)

        # Click on the "Next page" button
        pywinauto.mouse.click(button='left', coords=(400, 330))

        time.sleep(3)

        # Page 3

        # Click on the "Neant" button
        pywinauto.mouse.click(button='left', coords=(1095, 585))

        time.sleep(3)

        # Click on the "Continuer" button
        pywinauto.mouse.click(button='left', coords=(900, 340))

        time.sleep(3)

        # Click on the "Enregistrer" button
        pywinauto.mouse.click(button='left', coords=(1200, 300))

        time.sleep(3)

        # Click on the "Next page" button
        pywinauto.mouse.click(button='left', coords=(400, 330))

        time.sleep(3)

        # Page 4

        # Click on the "Neant" button
        pywinauto.mouse.click(button='left', coords=(1095, 590))

        time.sleep(3)

        # Click on the "Continuer" button
        pywinauto.mouse.click(button='left', coords=(900, 340))

        time.sleep(3)

        # Click on the "Enregistrer" button
        pywinauto.mouse.click(button='left', coords=(1200, 300))

        time.sleep(3)

        # Click on the "Next page" button
        pywinauto.mouse.click(button='left', coords=(400, 330))

        time.sleep(3)

        # Page 5

        # Click on the "Neant" button
        pywinauto.mouse.click(button='left', coords=(1105, 580))

        time.sleep(3)

        # Click on the "Continuer" button
        pywinauto.mouse.click(button='left', coords=(900, 340))

        time.sleep(3)

        # Click on the "Enregistrer" button
        pywinauto.mouse.click(button='left', coords=(1200, 300))

        time.sleep(3)

        # Click on the "Next page" button
        pywinauto.mouse.click(button='left', coords=(400, 330))

        time.sleep(3)

        # Page 6

        # Click on the "Neant" button
        pywinauto.mouse.click(button='left', coords=(1115, 665))

        time.sleep(3)

        # Click on the "Continuer" button
        pywinauto.mouse.click(button='left', coords=(900, 340))

        time.sleep(3)

        # Click on the "Enregistrer" button
        pywinauto.mouse.click(button='left', coords=(1200, 300))

        time.sleep(3)

        # Click on the "Next page" button
        pywinauto.mouse.click(button='left', coords=(400, 330))

        time.sleep(3)

        # Page 7

        # Click on the "Neant" button
        pywinauto.mouse.click(button='left', coords=(1100, 595))

        time.sleep(3)

        # Click on the "Continuer" button
        pywinauto.mouse.click(button='left', coords=(900, 340))

        time.sleep(3)

        # Click on the "Enregistrer" button
        pywinauto.mouse.click(button='left', coords=(1200, 300))

        time.sleep(3)

        # Click on the "Next page" button
        pywinauto.mouse.click(button='left', coords=(400, 330))

        time.sleep(3)

        # Page 8

        # Click on the "Neant" button
        pywinauto.mouse.click(button='left', coords=(1110, 595))

        time.sleep(3)

        # Click on the "Continuer" button
        pywinauto.mouse.click(button='left', coords=(900, 340))

        time.sleep(3)

        # Click on the "Enregistrer" button
        pywinauto.mouse.click(button='left', coords=(1200, 300))

        time.sleep(3)

        # Click on the "Next page" button
        pywinauto.mouse.click(button='left', coords=(400, 330))

        time.sleep(3)

        # Page 9

        # Click on the "Neant" button
        pywinauto.mouse.click(button='left', coords=(1130, 600))

        time.sleep(3)

        # Click on the "Continuer" button
        pywinauto.mouse.click(button='left', coords=(900, 340))

        time.sleep(3)

        # Click on the "Enregistrer" button
        pywinauto.mouse.click(button='left', coords=(1200, 300))

        time.sleep(3)

        # Click on the "Next page" button
        pywinauto.mouse.click(button='left', coords=(400, 330))

        time.sleep(3)

        # Page 10

        # Click on the "WA" input
        pywinauto.mouse.click(button='left', coords=(990, 585))

        time.sleep(3)

        # Insert the 'WA' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'WB' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'PP' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'WD' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'WE' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'XE' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'WF' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'WG' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'WI' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'XX' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'XW' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'WJ' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'XZ' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'XY' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'I7' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'WL' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'L7' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'K7' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'I8' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'ZN' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'WN' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'WO' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'XR' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'SU' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'SW' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'WQ' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'SX' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'M8' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        # Insert the 'WR' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'WS' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'WT' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'WU' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'WV' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'WH' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'WP' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'WW' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'XB' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'I6' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'WZ' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '2A' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'XA' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'ZY' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'XD' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'K9' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'L2' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'L5' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'XF' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'K3' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'PA' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '/oV' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the '1F' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'XC' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'PC' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'XS' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'ZI' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'XG' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'XH' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'XI' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'XJ' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'ZL' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'XL' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'XN' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'XO' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'Y1' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'Y3' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'X9' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'RA' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'RB' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'Y2' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'ZX' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'YA' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'YB' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'YH' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'YC' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'YD' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'PB' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'YI' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert the 'YL' value
        pywinauto.keyboard.send_keys("0")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Click on the "Enregistrer" button
        pywinauto.mouse.click(button='left', coords=(1200, 570))

        time.sleep(3)

        # Click on the "Next page" button
        pywinauto.mouse.click(button='left', coords=(405, 330))

        time.sleep(3)

        # Page 11

        # Click on the "Neant" button
        pywinauto.mouse.click(button='left', coords=(1115, 600))

        time.sleep(3)

        # Click on the "Continuer" button
        pywinauto.mouse.click(button='left', coords=(900, 340))

        time.sleep(3)

        # Click on the "Enregistrer" button
        pywinauto.mouse.click(button='left', coords=(1200, 300))

        time.sleep(3)

        # Click on the "Next page" button
        pywinauto.mouse.click(button='left', coords=(400, 330))

        time.sleep(3)

        # Page 12

        # Click on the "Neant" button
        pywinauto.mouse.click(button='left', coords=(1110, 590))

        time.sleep(3)

        # Click on the "Continuer" button
        pywinauto.mouse.click(button='left', coords=(900, 340))

        time.sleep(3)

        # Click on the "Enregistrer" button
        pywinauto.mouse.click(button='left', coords=(1200, 300))

        time.sleep(3)

    def test_declarer_ma_liasse_fiscale_2059_holomorphe_neant(self):
        print("test_declarer_ma_liasse_fiscale_2059_holomorphe_neant")

        time.sleep(6)

        app = Application(backend="uia")

        app.start("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")

        time.sleep(6)

        pywinauto.keyboard.send_keys("https://maliassefiscale.fr/Account/Login")

        time.sleep(6)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(6)

        # Click on the "Courrier électronique" input
        pywinauto.mouse.click(button='left', coords=(280, 310))

        time.sleep(6)

        # Insert the "Courrier électronique"
        pywinauto.keyboard.send_keys('.@outlook.fr')

        time.sleep(6)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(6)

        # Insert the "Mot de passe"
        pywinauto.keyboard.send_keys('')

        time.sleep(6)

        # Press the 'Tab' button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(6)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(6)

        # Click on the "Completer" button
        pywinauto.mouse.click(button='left', coords=(1030, 480))

        time.sleep(6)

        # Press the 'Down' button in 10 times
        pywinauto.keyboard.send_keys("{DOWN 10}")

        time.sleep(3)

        # Click on the "Remplir" button for "2059 - Complément à la déclaration d'impôt sur les sociétés"
        pywinauto.mouse.click(button='left', coords=(1200, 470))

        time.sleep(6)

        # Page 1

        # Click on the "Neant" button
        pywinauto.mouse.click(button='left', coords=(1035, 540))

        time.sleep(3)

        # Click on the "Continuer" button
        pywinauto.mouse.click(button='left', coords=(900, 340))

        time.sleep(3)

        # Click on the "Enregistrer" button
        pywinauto.mouse.click(button='left', coords=(1200, 300))

        time.sleep(3)

        # Click on the "Next page" button
        pywinauto.mouse.click(button='left', coords=(770, 300))

        time.sleep(3)

        # Page 2

        # Click on the "Neant" button
        pywinauto.mouse.click(button='left', coords=(1115, 550))

        time.sleep(3)

        # Click on the "Continuer" button
        pywinauto.mouse.click(button='left', coords=(900, 340))

        time.sleep(3)

        # Click on the "Enregistrer" button
        pywinauto.mouse.click(button='left', coords=(1200, 300))

        time.sleep(3)

        # Click on the "Next page" button
        pywinauto.mouse.click(button='left', coords=(770, 300))

        time.sleep(3)

        # Page 3

        # Click on the "Neant" button
        pywinauto.mouse.click(button='left', coords=(1110, 555))

        time.sleep(3)

        # Click on the "Continuer" button
        pywinauto.mouse.click(button='left', coords=(900, 340))

        time.sleep(3)

        # Click on the "Enregistrer" button
        pywinauto.mouse.click(button='left', coords=(1200, 300))

        time.sleep(3)

        # Click on the "Next page" button
        pywinauto.mouse.click(button='left', coords=(770, 300))

        time.sleep(3)

        # Page 4

        # Click on the "Neant" button
        pywinauto.mouse.click(button='left', coords=(1115, 590))

        time.sleep(3)

        # Click on the "Continuer" button
        pywinauto.mouse.click(button='left', coords=(900, 340))

        time.sleep(3)

        # Click on the "Enregistrer" button
        pywinauto.mouse.click(button='left', coords=(1200, 300))

        time.sleep(3)

        # Click on the "Next page" button
        pywinauto.mouse.click(button='left', coords=(770, 300))

        time.sleep(3)

        # Page 5

        # Click on the "Neant" button
        pywinauto.mouse.click(button='left', coords=(1095, 560))

        time.sleep(3)

        # Click on the "Continuer" button
        pywinauto.mouse.click(button='left', coords=(900, 340))

        time.sleep(3)

        # Click on the "Enregistrer" button
        pywinauto.mouse.click(button='left', coords=(1200, 300))

        time.sleep(3)

        # Click on the "Next page" button
        pywinauto.mouse.click(button='left', coords=(770, 300))

        time.sleep(3)

        # Page 6

        # Click on the "Neant" button
        pywinauto.mouse.click(button='left', coords=(1110, 545))

        time.sleep(3)

        # Click on the "Continuer" button
        pywinauto.mouse.click(button='left', coords=(900, 340))

        time.sleep(3)

        # Click on the "Enregistrer" button
        pywinauto.mouse.click(button='left', coords=(1200, 300))

        time.sleep(3)

        # Click on the "Next page" button
        pywinauto.mouse.click(button='left', coords=(770, 300))

        time.sleep(3)

        # Page 7

        # Click on the "Neant" button
        pywinauto.mouse.click(button='left', coords=(1115, 555))

        time.sleep(3)

        # Click on the "Continuer" button
        pywinauto.mouse.click(button='left', coords=(900, 340))

        time.sleep(3)

        # Click on the "Enregistrer" button
        pywinauto.mouse.click(button='left', coords=(1200, 300))

        time.sleep(3)

        # Click on the "Next page" button
        pywinauto.mouse.click(button='left', coords=(770, 300))

        time.sleep(3)

        # Page 8

        # Click on the "Neant" button
        pywinauto.mouse.click(button='left', coords=(1160, 635))

        time.sleep(3)

        # Click on the "Continuer" button
        pywinauto.mouse.click(button='left', coords=(900, 340))

        time.sleep(3)

        # Click on the "Enregistrer" button
        pywinauto.mouse.click(button='left', coords=(1200, 300))

        time.sleep(3)


if __name__ == '__main__':
    unittest.main()
