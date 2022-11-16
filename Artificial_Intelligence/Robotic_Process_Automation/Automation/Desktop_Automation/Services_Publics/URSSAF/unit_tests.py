import unittest
import time
from pywinauto.application import Application
import pywinauto.keyboard
import pywinauto.mouse
import pywinauto.base_wrapper
import pywinauto.timings
import os

mois = "6_Juin"
annee = "3_Annee_2022"


class UnitTestsDesktopAutomationURSSAF(unittest.TestCase):
    # ok
    def test_se_connecter(self):
        print("test_se_connecter")

        time.sleep(6)

        app = Application(backend="uia")

        app.start("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")

        time.sleep(6)

        pywinauto.keyboard.send_keys("https://www.urssaf.fr/portail/home/connectez-vous.html")

        time.sleep(5)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(15)

        # Click on the "Tout refuser" button
        pywinauto.mouse.click(button='left', coords=(830, 635))

        time.sleep(5)

        # Click on the "Siret" button
        pywinauto.mouse.click(button='left', coords=(240, 540))

        time.sleep(5)

        # Insert Siret
        pywinauto.keyboard.send_keys('')

        time.sleep(5)

        # Tab to the password
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(5)

        # Insert password
        pywinauto.keyboard.send_keys('')

        time.sleep(5)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(10)

    # ok
    def test_declarer_cotisations_neant(self):
        print("test_declarer_cotisations_neant")

        x_fireshot = 1240

        time.sleep(6)

        path_folder = annee + "\\" + mois

        app = Application(backend="uia")

        app.start("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")

        time.sleep(6)

        pywinauto.keyboard.send_keys("https://www.urssaf.fr/portail/home/connectez-vous.html")

        time.sleep(5)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(15)

        # Click on the "Tout refuser" button
        pywinauto.mouse.click(button='left', coords=(830, 635))

        time.sleep(5)

        # Click on the "Siret" button
        pywinauto.mouse.click(button='left', coords=(240, 540))

        time.sleep(5)

        # Insert Siret
        pywinauto.keyboard.send_keys('')

        time.sleep(5)

        # Tab to the password
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(5)

        # Insert password
        pywinauto.keyboard.send_keys('')

        time.sleep(5)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(10)

        # Click on the "Fireshot" button
        pywinauto.mouse.click(button='left', coords=(x_fireshot, 50))

        time.sleep(6)

        # Click on the "Capture entire page" button
        pywinauto.mouse.click(button='left', coords=(1030, 110))

        time.sleep(10)

        # Click on the "Save to PDF" button
        pywinauto.mouse.click(button='left', coords=(1160, 330))

        time.sleep(5)

        # Click on the bar to select the folder
        pywinauto.mouse.click(button='left', coords=(380, 50))

        time.sleep(5)

        # Enter the path folder
        pywinauto.keyboard.send_keys("A:\\1_Professionnel\\1_Holomorphe\\1_Administration\\2_Gestion_Declarations_Administratives\\1_Recurrentes\\4_URSSAF\\3_Compte\\3_Declarer_Les_Cotisations\\" + path_folder)

        time.sleep(5)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(5)

        # Click on the 'Nom du fichier :' bar
        pywinauto.mouse.click(button='left', coords=(260, 375))

        time.sleep(5)

        # Press the 'Ctrl+A'
        pywinauto.keyboard.send_keys('^a')

        time.sleep(5)

        # Insert the 'Page_1.pdf'
        pywinauto.keyboard.send_keys('Page_1.pdf')

        time.sleep(5)

        # Click on the 'Enregistrer' button
        pywinauto.mouse.click(button='left', coords=(510, 445))

        time.sleep(5)

        # Click on the 'Cross' button to hide downloaded files
        pywinauto.mouse.click(button='left', coords=(1345, 700))

        time.sleep(5)

        # Close the onglet
        pywinauto.keyboard.send_keys('^w')

        time.sleep(5)

        # Click on the screen
        pywinauto.mouse.click(button='left', coords=(500, 200))

        time.sleep(5)

        # {DOWN} 4 times
        pywinauto.keyboard.send_keys('{DOWN 4}')

        time.sleep(5)

        # Click on the "Declarer des cotisations" button
        pywinauto.mouse.click(button='left', coords=(1100, 420))

        time.sleep(5)

        # Click on the "Fireshot" button
        pywinauto.mouse.click(button='left', coords=(x_fireshot, 50))

        time.sleep(5)

        # Click on the "Capture entire page" button
        pywinauto.mouse.click(button='left', coords=(1020, 110))

        time.sleep(10)

        # Click on the "Save to PDF" button
        pywinauto.mouse.click(button='left', coords=(1160, 330))

        time.sleep(5)

        # Click on the bar to select the folder
        pywinauto.mouse.click(button='left', coords=(380, 50))

        time.sleep(5)

        # Enter the path folder
        pywinauto.keyboard.send_keys("A:\\1_Professionnel\\1_Holomorphe\\1_Administration\\2_Gestion_Declarations_Administratives\\1_Recurrentes\\4_URSSAF\\3_Compte\\3_Declarer_Les_Cotisations\\" + path_folder)

        time.sleep(5)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(5)

        # Click on the 'Nom du fichier :' bar
        pywinauto.mouse.click(button='left', coords=(260, 375))

        time.sleep(5)

        # Press the 'Ctrl+A'
        pywinauto.keyboard.send_keys('^a')

        time.sleep(5)

        # Insert the 'Page_2.pdf'
        pywinauto.keyboard.send_keys('Page_2.pdf')

        time.sleep(5)

        # Click on the 'Enregistrer' button
        pywinauto.mouse.click(button='left', coords=(510, 445))

        time.sleep(5)

        # Click on the 'Cross' button to hide downloaded files
        pywinauto.mouse.click(button='left', coords=(1345, 700))

        time.sleep(5)

        # Close the onglet
        pywinauto.keyboard.send_keys('^w')

        time.sleep(5)

        # Click on the 'ON / OFF' button
        pywinauto.mouse.click(button='left', coords=(860, 180))

        time.sleep(5)

        # Close the browser
        pywinauto.keyboard.send_keys('^w')

        time.sleep(5)

        print("ccleaner running")
        os.system("set ccleaner='C:\\Program Files\\CCleaner\\CCleaner.exe'")
        os.system("start ccleaner /AUTO")

        time.sleep(5)

    # ok
    def test_payer_cotisations_neant(self):
        print("test_payer_cotisations_neant")

        x_fireshot = 1240

        time.sleep(6)

        path_folder = annee + "\\" + mois

        app = Application(backend="uia")

        app.start("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")

        time.sleep(6)

        pywinauto.keyboard.send_keys("https://www.urssaf.fr/portail/home/connectez-vous.html")

        time.sleep(5)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(15)

        # Click on the "Tout refuser" button
        pywinauto.mouse.click(button='left', coords=(830, 635))

        time.sleep(5)

        # Click on the "Siret" button
        pywinauto.mouse.click(button='left', coords=(240, 540))

        time.sleep(5)

        # Insert Siret
        pywinauto.keyboard.send_keys('')

        time.sleep(5)

        # Tab to the password
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(5)

        # Insert password
        pywinauto.keyboard.send_keys('')

        time.sleep(5)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(10)

        # Click on the "Fireshot" button
        pywinauto.mouse.click(button='left', coords=(x_fireshot, 50))

        time.sleep(6)

        # Click on the "Capture entire page" button
        pywinauto.mouse.click(button='left', coords=(1030, 110))

        time.sleep(10)

        # Click on the "Save to PDF" button
        pywinauto.mouse.click(button='left', coords=(1160, 330))

        time.sleep(5)

        # Click on the bar to select the folder
        pywinauto.mouse.click(button='left', coords=(380, 50))

        time.sleep(5)

        # Enter the path folder
        pywinauto.keyboard.send_keys(
            "A:\\1_Professionnel\\1_Holomorphe\\1_Administration\\2_Gestion_Declarations_Administratives"
            "\\1_Recurrentes\\4_URSSAF\\3_Compte\\1_Payer_Les_Cotisations\\" + path_folder)

        time.sleep(5)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(5)

        # Click on the 'Nom du fichier :' bar
        pywinauto.mouse.click(button='left', coords=(260, 375))

        time.sleep(5)

        # Press the 'Ctrl+A'
        pywinauto.keyboard.send_keys('^a')

        time.sleep(5)

        # Insert the 'Page_1.pdf'
        pywinauto.keyboard.send_keys('Page_1.pdf')

        time.sleep(5)

        # Click on the 'Enregistrer' button
        pywinauto.mouse.click(button='left', coords=(510, 445))

        time.sleep(5)

        # Click on the 'Cross' button to hide downloaded files
        pywinauto.mouse.click(button='left', coords=(1345, 700))

        time.sleep(5)

        # Close the onglet
        pywinauto.keyboard.send_keys('^w')

        time.sleep(5)

        # Click on the screen
        pywinauto.mouse.click(button='left', coords=(500, 200))

        time.sleep(5)

        # Move the mouse on the "Compte" button
        pywinauto.mouse.click(button='left', coords=(380, 380))

        time.sleep(5)

        # Click on the "Payer les cotisations" button
        pywinauto.mouse.click(button='left', coords=(840, 450))

        time.sleep(5)

        # Click on the "Fireshot" button
        pywinauto.mouse.click(button='left', coords=(x_fireshot, 50))

        time.sleep(5)

        # Click on the "Capture entire page" button
        pywinauto.mouse.click(button='left', coords=(1020, 110))

        time.sleep(10)

        # Click on the "Save to PDF" button
        pywinauto.mouse.click(button='left', coords=(1160, 330))

        time.sleep(5)

        # Click on the bar to select the folder
        pywinauto.mouse.click(button='left', coords=(380, 50))

        time.sleep(5)

        # Enter the path folder
        pywinauto.keyboard.send_keys("A:\\1_Professionnel\\1_Holomorphe\\1_Administration\\2_Gestion_Declarations_Administratives\\1_Recurrentes\\4_URSSAF\\3_Compte\\1_Payer_Les_Cotisations\\" + path_folder)

        time.sleep(5)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(5)

        # Click on the 'Nom du fichier :' bar
        pywinauto.mouse.click(button='left', coords=(260, 375))

        time.sleep(5)

        # Press the 'Ctrl+A'
        pywinauto.keyboard.send_keys('^a')

        time.sleep(5)

        # Insert the 'Page_2.pdf'
        pywinauto.keyboard.send_keys('Page_2.pdf')

        time.sleep(5)

        # Click on the 'Enregistrer' button
        pywinauto.mouse.click(button='left', coords=(510, 445))

        time.sleep(5)

        # Click on the 'Cross' button to hide downloaded files
        pywinauto.mouse.click(button='left', coords=(1345, 700))

        time.sleep(5)

        # Close the onglet
        pywinauto.keyboard.send_keys('^w')

        time.sleep(5)

        # Click on the 'ON / OFF' button
        pywinauto.mouse.click(button='left', coords=(860, 180))

        time.sleep(5)

        # Close the browser
        pywinauto.keyboard.send_keys('^w')

        time.sleep(5)

        print("ccleaner running")
        os.system("set ccleaner='C:\\Program Files\\CCleaner\\CCleaner.exe'")
        os.system("start ccleaner /AUTO")

        time.sleep(5)

    # ok
    def test_payer_les_dettes_neant(self):
        print("test_payer_les_dettes_neant")

        x_fireshot = 1240

        time.sleep(6)

        path_folder = annee + "\\" + mois

        app = Application(backend="uia")

        app.start("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")

        time.sleep(6)

        pywinauto.keyboard.send_keys("https://www.urssaf.fr/portail/home/connectez-vous.html")

        time.sleep(5)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(15)

        # Click on the "Tout refuser" button
        pywinauto.mouse.click(button='left', coords=(830, 635))

        time.sleep(5)

        # Click on the "Siret" button
        pywinauto.mouse.click(button='left', coords=(240, 540))

        time.sleep(5)

        # Insert Siret
        pywinauto.keyboard.send_keys('')

        time.sleep(5)

        # Tab to the password
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(5)

        # Insert password
        pywinauto.keyboard.send_keys('')

        time.sleep(5)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(10)

        # Click on the "Fireshot" button
        pywinauto.mouse.click(button='left', coords=(x_fireshot, 50))

        time.sleep(6)

        # Click on the "Capture entire page" button
        pywinauto.mouse.click(button='left', coords=(1030, 110))

        time.sleep(10)

        # Click on the "Save to PDF" button
        pywinauto.mouse.click(button='left', coords=(1160, 330))

        time.sleep(5)

        # Click on the bar to select the folder
        pywinauto.mouse.click(button='left', coords=(380, 50))

        time.sleep(5)

        # Enter the path folder
        pywinauto.keyboard.send_keys("A:\\1_Professionnel\\1_Holomorphe\\1_Administration\\2_Gestion_Declarations_Administratives\\1_Recurrentes\\4_URSSAF\\3_Compte\\16_Payer_Les_Dettes\\" + path_folder)

        time.sleep(5)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(5)

        # Click on the 'Nom du fichier :' bar
        pywinauto.mouse.click(button='left', coords=(260, 375))

        time.sleep(5)

        # Press the 'Ctrl+A'
        pywinauto.keyboard.send_keys('^a')

        time.sleep(5)

        # Insert the 'Page_1.pdf'
        pywinauto.keyboard.send_keys('Page_1.pdf')

        time.sleep(5)

        # Click on the 'Enregistrer' button
        pywinauto.mouse.click(button='left', coords=(510, 445))

        time.sleep(5)

        # Click on the 'Cross' button to hide downloaded files
        pywinauto.mouse.click(button='left', coords=(1345, 700))

        time.sleep(5)

        # Close the onglet
        pywinauto.keyboard.send_keys('^w')

        time.sleep(5)

        # Click on the screen
        pywinauto.mouse.click(button='left', coords=(500, 200))

        time.sleep(5)

        # Move the mouse on the "Compte" button
        pywinauto.mouse.click(button='left', coords=(380, 380))

        time.sleep(5)

        # Click on the "Payer les dettes" button
        pywinauto.mouse.click(button='left', coords=(830, 470))

        time.sleep(5)

        # Click on the "Fireshot" button
        pywinauto.mouse.click(button='left', coords=(x_fireshot, 50))

        time.sleep(5)

        # Click on the "Capture entire page" button
        pywinauto.mouse.click(button='left', coords=(1020, 110))

        time.sleep(10)

        # Click on the "Save to PDF" button
        pywinauto.mouse.click(button='left', coords=(1160, 330))

        time.sleep(5)

        # Click on the bar to select the folder
        pywinauto.mouse.click(button='left', coords=(380, 50))

        time.sleep(5)

        # Enter the path folder
        pywinauto.keyboard.send_keys("A:\\1_Professionnel\\1_Holomorphe\\1_Administration\\2_Gestion_Declarations_Administratives\\1_Recurrentes\\4_URSSAF\\3_Compte\\16_Payer_Les_Dettes\\" + path_folder)

        time.sleep(5)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(5)

        # Click on the 'Nom du fichier :' bar
        pywinauto.mouse.click(button='left', coords=(260, 375))

        time.sleep(5)

        # Press the 'Ctrl+A'
        pywinauto.keyboard.send_keys('^a')

        time.sleep(5)

        # Insert the 'Page_2.pdf'
        pywinauto.keyboard.send_keys('Page_2.pdf')

        time.sleep(5)

        # Click on the 'Enregistrer' button
        pywinauto.mouse.click(button='left', coords=(510, 445))

        time.sleep(5)

        # Click on the 'Cross' button to hide downloaded files
        pywinauto.mouse.click(button='left', coords=(1345, 700))

        time.sleep(5)

        # Close the onglet
        pywinauto.keyboard.send_keys('^w')

        time.sleep(5)

        # Click on the 'ON / OFF' button
        pywinauto.mouse.click(button='left', coords=(860, 180))

        time.sleep(5)

        # Close the browser
        pywinauto.keyboard.send_keys('^w')

        time.sleep(5)

        print("ccleaner running")
        os.system("set ccleaner='C:\\Program Files\\CCleaner\\CCleaner.exe'")
        os.system("start ccleaner /AUTO")

        time.sleep(5)


if __name__ == '__main__':
    unittest.main()
