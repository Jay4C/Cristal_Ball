import unittest
import time
from pywinauto.application import Application
import pywinauto.keyboard
import pywinauto.mouse
import pywinauto.base_wrapper
import pywinauto.timings
import os


class UnitTestsDesktopAutomationFree(unittest.TestCase):
    def test_display_consumption(self):
        print("test_display_consumption")

        app = Application(backend="uia")

        app.start("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")

        time.sleep(6)

        pywinauto.keyboard.send_keys("https://mobile.free.fr/account/")

        time.sleep(3)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(5)

        # Click on the Identifiant input
        pywinauto.mouse.click(button='left', coords=(1000, 390))

        time.sleep(3)

        # Insert Identifiant
        pywinauto.keyboard.send_keys('')

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert M_D_P
        pywinauto.keyboard.send_keys("")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(10)

        # Click on the Deconnexion button
        pywinauto.mouse.click(button='left', coords=(150, 220))

        time.sleep(3)

        # Close the browser
        pywinauto.keyboard.send_keys('%{F4}')

        time.sleep(3)

        print("ccleaner running")
        os.system("set ccleaner='C:\\Program Files\\CCleaner\\CCleaner.exe'")
        os.system("start ccleaner /AUTO")

        time.sleep(5)

    def test_display_messagerie_vocal(self):
        print("test_display_messagerie_vocal")

        app = Application(backend="uia")

        app.start("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")

        time.sleep(6)

        pywinauto.keyboard.send_keys("https://mobile.free.fr/account/")

        time.sleep(3)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(5)

        # Click on the Identifiant input
        pywinauto.mouse.click(button='left', coords=(1000, 390))

        time.sleep(3)

        # Insert Identifiant
        pywinauto.keyboard.send_keys('')

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Insert M_D_P
        pywinauto.keyboard.send_keys("")

        time.sleep(3)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(10)

        # Click on the "Messagerie vocal" button
        pywinauto.mouse.click(button='left', coords=(120, 370))

        time.sleep(3)

        print("ccleaner running")
        os.system("set ccleaner='C:\\Program Files\\CCleaner\\CCleaner.exe'")
        os.system("start ccleaner /AUTO")

        time.sleep(5)


if __name__ == '__main__':
    unittest.main()
