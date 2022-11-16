import unittest
import time
from pywinauto.application import Application
import pywinauto.keyboard
import pywinauto.mouse
import pywinauto.base_wrapper
import pywinauto.timings
import os


class UnitTestsDesktopAutomationGmail(unittest.TestCase):
    def test_activate_or_deactivate_imap(self):
        print("test_activate_or_deactivate_imap")

        time.sleep(6)

        app = Application(backend="uia")

        app.start("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")

        time.sleep(6)

        pywinauto.keyboard.send_keys("https://mail.google.com/mail?hl=fr")

        time.sleep(3)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(10)

        # Insert the 'Email' value
        pywinauto.keyboard.send_keys('..@gmail.com')

        time.sleep(3)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Password' value
        pywinauto.keyboard.send_keys('')

        time.sleep(3)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(20)

        # Click on the "J icon"
        pywinauto.mouse.click(button='left', coords=(1335, 100))

        time.sleep(10)

        # Click on the "Gérer votre compte Google"
        pywinauto.mouse.click(button='left', coords=(1180, 320))

        time.sleep(10)

        # Click on the "Sécurité"
        pywinauto.mouse.click(button='left', coords=(100, 305))

        time.sleep(10)

        # Click on the "Down" several times
        pywinauto.keyboard.send_keys('{DOWN 21}')

        time.sleep(10)

        # Click on the "Activer ou désactiver l'accès IMAP"
        pywinauto.mouse.click(button='left', coords=(450, 280))

        time.sleep(10)

        # Click on the "Paramètres "Autoriser les applications moins sécurisées"
        pywinauto.mouse.click(button='left', coords=(755, 405))

        time.sleep(10)

        # Click on the "Bouton retour"
        pywinauto.mouse.click(button='left', coords=(260, 160))

        time.sleep(10)

        # Close the window
        pywinauto.keyboard.send_keys('^w')

        time.sleep(10)

        # Click on the "J icon"
        pywinauto.mouse.click(button='left', coords=(1335, 100))

        time.sleep(10)

        # Click on the "Deconnexion"
        pywinauto.mouse.click(button='left', coords=(1180, 450))

        time.sleep(10)

        # Click on the "Supprimer un compte"
        pywinauto.mouse.click(button='left', coords=(620, 420))

        time.sleep(10)

        # Click on the "Supprimer le compte"
        pywinauto.mouse.click(button='left', coords=(855, 350))

        time.sleep(10)

        # Click on the "Oui, supprimer"
        pywinauto.mouse.click(button='left', coords=(760, 500))

        time.sleep(10)

        # Close the window
        pywinauto.keyboard.send_keys('^w')

        time.sleep(10)

        print("ccleaner running")
        os.system("set ccleaner='C:\\Program Files\\CCleaner\\CCleaner.exe'")
        os.system("start ccleaner /AUTO")

        time.sleep(5)

    def test_connect(self):
        print("test_connect")

        time.sleep(6)

        app = Application(backend="uia")

        app.start("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")

        time.sleep(6)

        pywinauto.keyboard.send_keys("https://mail.google.com/mail?hl=fr")

        time.sleep(3)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(10)

        # Insert the 'Email' value
        pywinauto.keyboard.send_keys('..@gmail.com')

        time.sleep(3)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Press the 'Password' value
        pywinauto.keyboard.send_keys('')

        time.sleep(3)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(20)

        print("ccleaner running")
        os.system("set ccleaner='C:\\Program Files\\CCleaner\\CCleaner.exe'")
        os.system("start ccleaner /AUTO")

        time.sleep(5)

    def test_effacer_tous_les_messages_depuis_Tous_les_messages(self):
        print("test_effacer_tous_les_messages_depuis_Tous_les_messages")

        time.sleep(5)

        app = Application(backend="uia")

        app.start("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")

        time.sleep(10)

        pywinauto.keyboard.send_keys("https://mail.google.com/mail?hl=fr")

        time.sleep(5)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(10)

        # Insert the 'Email' value
        pywinauto.keyboard.send_keys('..@gmail.com')

        time.sleep(5)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(5)

        # Press the 'Password' value
        pywinauto.keyboard.send_keys('')

        time.sleep(5)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(20)

        # Press Plus button
        pywinauto.mouse.click(button='left', coords=(100, 390))

        time.sleep(5)

        # Down to Tous les messages
        pywinauto.mouse.click(button='left', coords=(250, 375))

        time.sleep(5)

        # Click on Tous les messages
        pywinauto.mouse.click(button='left', coords=(100, 290))

        time.sleep(5)

        for i in range(40):
            # Click on Select all button
            pywinauto.mouse.click(button='left', coords=(280, 160))

            time.sleep(10)

            # Click on Delete button
            pywinauto.mouse.click(button='left', coords=(430, 160))

            time.sleep(30)

            # Click on Tous les messages
            pywinauto.mouse.click(button='left', coords=(100, 290))

            time.sleep(40)

        print("ccleaner running")
        os.system("set ccleaner='C:\\Program Files\\CCleaner\\CCleaner.exe'")
        os.system("start ccleaner /AUTO")

        time.sleep(5)

    def test_effacer_tous_les_messages_depuis_Corbeille(self):
        print("test_effacer_tous_les_messages_depuis_Corbeille")

        time.sleep(5)

        app = Application(backend="uia")

        app.start("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")

        time.sleep(10)

        pywinauto.keyboard.send_keys("https://mail.google.com/mail?hl=fr")

        time.sleep(5)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(10)

        # Insert the 'Email' value
        pywinauto.keyboard.send_keys('..@gmail.com')

        time.sleep(5)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(5)

        # Press the 'Password' value
        pywinauto.keyboard.send_keys('')

        time.sleep(5)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(20)

        # Press Plus button
        pywinauto.mouse.click(button='left', coords=(100, 390))

        time.sleep(5)

        # Down to Corbeille
        pywinauto.mouse.click(button='left', coords=(250, 385))

        time.sleep(5)

        # Click on Corbeille
        pywinauto.mouse.click(button='left', coords=(100, 350))

        time.sleep(5)

        for i in range(40):
            # Click on Select all button
            pywinauto.mouse.click(button='left', coords=(280, 160))

            time.sleep(10)

            # Click on "Supprimer définitivement" button
            pywinauto.mouse.click(button='left', coords=(400, 155))

            time.sleep(60)

            # Click on Corbeille
            pywinauto.mouse.click(button='left', coords=(100, 350))

            time.sleep(30)

        print("ccleaner running")
        os.system("set ccleaner='C:\\Program Files\\CCleaner\\CCleaner.exe'")
        os.system("start ccleaner /AUTO")

        time.sleep(5)


if __name__ == '__main__':
    unittest.main()
