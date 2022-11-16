import unittest
import time
from pywinauto.application import Application
import pywinauto.keyboard
import pywinauto.mouse
import pywinauto.base_wrapper
import pywinauto.timings
import os


class UnitTestsDesktopAutomationMalt(unittest.TestCase):
    # ok
    def test_update_my_disponibility(self):
        print("test_update_my_disponibility")

        app = Application(backend="uia")

        app.start("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")

        time.sleep(6)

        pywinauto.keyboard.send_keys("https://www.malt.fr/")

        time.sleep(3)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(15)

        # Click on the "Tout accepter" button
        pywinauto.mouse.click(button='left', coords=(1130, 680))

        time.sleep(10)

        # Click on the "Me connecter" button
        pywinauto.mouse.click(button='left', coords=(1100, 100))

        time.sleep(10)

        # Click on the "Email" input
        pywinauto.mouse.click(button='left', coords=(500, 530))

        time.sleep(5)

        # Insert my 'email'
        pywinauto.keyboard.send_keys('.@holomorphe.com')

        time.sleep(5)

        # Tab to the password
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(5)

        # Insert password
        pywinauto.keyboard.send_keys('')

        time.sleep(5)

        # Tab to the password
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(5)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(10)

        # Click on the "Mon espace freelance" button
        pywinauto.mouse.click(button='left', coords=(1100, 105))

        time.sleep(10)

        # Click on the "Modifier mon profil" button
        pywinauto.mouse.click(button='left', coords=(1100, 210))

        time.sleep(5)

        # Click on the "Editer ma disponibilité" button
        pywinauto.mouse.click(button='left', coords=(1100, 340))

        time.sleep(5)

        # Click on the "Êtes-vous disponible pour recevoir des propositions ?" button
        pywinauto.mouse.click(button='left', coords=(400, 340))

        time.sleep(5)

        # Click on the "A quelle fréquence ? (obligatoire)" button
        pywinauto.mouse.click(button='left', coords=(500, 430))

        time.sleep(5)

        # Select the "A temps plein" choice
        pywinauto.mouse.click(button='left', coords=(500, 495))

        time.sleep(5)

        # Click on the "Valider" button
        pywinauto.mouse.click(button='left', coords=(530, 510))

        time.sleep(5)

        # Click on the "Wheel" button
        pywinauto.mouse.click(button='left', coords=(1250, 110))

        time.sleep(5)

        # Click on the "Deconnexion" button
        pywinauto.mouse.click(button='left', coords=(1130, 310))

        time.sleep(10)

        # Close the browser
        pywinauto.keyboard.send_keys('^w')

        time.sleep(5)

        print("ccleaner running")
        os.system("set ccleaner='C:\\Program Files\\CCleaner\\CCleaner.exe'")
        os.system("start ccleaner /AUTO")

        time.sleep(5)

    # ok
    def test_connecter(self):
        print("test_connecter")

        app = Application(backend="uia")

        app.start("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")

        time.sleep(6)

        pywinauto.keyboard.send_keys("https://www.malt.fr/")

        time.sleep(3)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(15)

        # Click on the "Tout accepter" button
        pywinauto.mouse.click(button='left', coords=(1130, 680))

        time.sleep(10)

        # Click on the "Me connecter" button
        pywinauto.mouse.click(button='left', coords=(1100, 100))

        time.sleep(10)

        # Click on the "Email" input
        pywinauto.mouse.click(button='left', coords=(500, 530))

        time.sleep(5)

        # Insert my 'email'
        pywinauto.keyboard.send_keys('.@holomorphe.com')

        time.sleep(5)

        # Tab to the password
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(5)

        # Insert password
        pywinauto.keyboard.send_keys('')

        time.sleep(5)

        # Tab to the password
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(5)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(10)

        print("ccleaner running")
        os.system("set ccleaner='C:\\Program Files\\CCleaner\\CCleaner.exe'")
        os.system("start ccleaner /AUTO")

        time.sleep(5)


if __name__ == '__main__':
    unittest.main()
