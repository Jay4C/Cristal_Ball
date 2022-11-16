import unittest
import time
from pywinauto.application import Application
import pywinauto.keyboard
import pywinauto.mouse
import pywinauto.base_wrapper
import pywinauto.timings
import os

mois = "4_Avril_Pour_Mars"


class UnitTestsDesktopAutomationDGFIP(unittest.TestCase):
    # ok
    def test_se_connecter(self):
        print("test_se_connecter")

        app = Application(backend="uia")

        app.start("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")

        time.sleep(6)

        pywinauto.keyboard.send_keys("https://www.impots.gouv.fr/portail/")

        time.sleep(3)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(5)

        # Click on the "Votre espace professionnel" button
        pywinauto.mouse.click(button='left', coords=(1110, 160))

        time.sleep(5)

        # Click on the "Adresse électronique" input
        pywinauto.mouse.click(button='left', coords=(200, 340))

        time.sleep(5)

        # Insert the 'email'
        pywinauto.keyboard.send_keys("")

        time.sleep(5)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(5)

        # Insert the 'M_D_P'
        pywinauto.keyboard.send_keys("")

        time.sleep(5)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(5)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(10)

    # ok
    def test_declarer_revenus_capitaux_mobiliers_neant(self):
        print("test_declarer_revenus_capitaux_mobiliers_neant")

        x_revenus_capitaux_mobiliers_button = 600

        y_revenus_capitaux_mobiliers_button = 520

        x_fireshot = 1240

        y_fireshot = 50

        path_folder = "3_Annee_2022\\" + mois

        app = Application(backend="uia")

        app.start("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")

        time.sleep(6)

        pywinauto.keyboard.send_keys("https://www.impots.gouv.fr/portail/")

        time.sleep(3)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(5)

        # Click on the "Votre espace professionnel" button
        pywinauto.mouse.click(button='left', coords=(1110, 160))

        time.sleep(5)

        # Click on the "Adresse électronique" input
        pywinauto.mouse.click(button='left', coords=(200, 340))

        time.sleep(5)

        # Insert the 'email'
        pywinauto.keyboard.send_keys(".@outlook.fr")

        time.sleep(5)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(5)

        # Insert the 'M_D_P'
        pywinauto.keyboard.send_keys("")

        time.sleep(5)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(5)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(10)

        # Click on the "Revenus de capitaux mobiliers" button
        pywinauto.mouse.click(button='left', coords=(x_revenus_capitaux_mobiliers_button,
                                                     y_revenus_capitaux_mobiliers_button))

        time.sleep(5)

        # Click on the "Déclarer" button
        pywinauto.mouse.click(button='left', coords=(690, 410))

        time.sleep(5)

        # Click on the "Fireshot" button
        pywinauto.mouse.click(button='left', coords=(x_fireshot, y_fireshot))

        time.sleep(5)

        # Click on the "Capture entire page" button
        pywinauto.mouse.click(button='left', coords=(x_fireshot, 115))

        time.sleep(10)

        # Click on the "Save to PDF" button
        pywinauto.mouse.click(button='left', coords=(1160, 330))

        time.sleep(5)

        # Click on the bar to select the folder
        pywinauto.mouse.click(button='left', coords=(380, 50))

        time.sleep(5)

        # Enter the path folder
        pywinauto.keyboard.send_keys(
            "A:\\1_Professionnel\\1_Holomorphe\\1_Administration"
            "\\2_Gestion_Declarations_Administratives\\1_Recurrentes\\1_DGFIP"
            "\\7_Declaration_I_D_R__Revenus_Capitaux_Mobiliers\\" + path_folder
        )

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
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(5)

        # Close the onglet
        pywinauto.keyboard.send_keys('^w')

        time.sleep(5)

        # Click on the screen
        pywinauto.mouse.click(button='left', coords=(600, 10))

        time.sleep(5)

        # Click on the 'mois annee' button
        pywinauto.mouse.click(button='left', coords=(250, 575))

        time.sleep(10)

        # Click on the screen
        pywinauto.mouse.click(button='left', coords=(500, 500))

        time.sleep(5)

        # {DOWN} 2 times
        pywinauto.keyboard.send_keys('{DOWN 7}')

        time.sleep(5)

        # Click on the "AB Intérêts, arrérages et produits de toute nature" input
        pywinauto.mouse.click(button='left', coords=(900, 565))

        time.sleep(5)

        # Insert "0"
        pywinauto.keyboard.send_keys('0')

        time.sleep(5)

        # Click on the screen
        pywinauto.mouse.click(button='left', coords=(700, 10))

        time.sleep(5)

        # {DOWN} 50 times
        pywinauto.keyboard.send_keys('{DOWN 65}')

        time.sleep(5)

        # Click on the "Fireshot" button
        pywinauto.mouse.click(button='left', coords=(x_fireshot, y_fireshot))

        time.sleep(5)

        # Click on the "Capture entire page" button
        pywinauto.mouse.click(button='left', coords=(x_fireshot, 115))

        time.sleep(25)

        # Click on the "Save to PDF" button
        pywinauto.mouse.click(button='left', coords=(1160, 330))

        time.sleep(5)

        # Click on the bar to select the folder
        pywinauto.mouse.click(button='left', coords=(380, 50))

        time.sleep(5)

        # Enter the path folder
        pywinauto.keyboard.send_keys(
            "A:\\1_Professionnel\\1_Holomorphe\\1_Administration\\2_Gestion_Declarations_Administratives"
            "\\1_Recurrentes\\1_DGFIP\\7_Declaration_I_D_R__Revenus_Capitaux_Mobiliers\\" + path_folder
        )

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
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(5)

        # Close the onglet
        pywinauto.keyboard.send_keys('^w')

        time.sleep(5)

        # Click on the screen
        pywinauto.mouse.click(button='left', coords=(700, 10))

        time.sleep(5)

        # Click on the 'Valider' button
        pywinauto.mouse.click(button='left', coords=(450, 540))

        time.sleep(5)

        # Click on the screen
        pywinauto.mouse.click(button='left', coords=(700, 10))

        time.sleep(5)

        # {DOWN} 20 times
        pywinauto.keyboard.send_keys('{DOWN 30}')

        time.sleep(5)

        # Click on the "Fireshot" button
        pywinauto.mouse.click(button='left', coords=(x_fireshot, y_fireshot))

        time.sleep(5)

        # Click on the "Capture entire page" button
        pywinauto.mouse.click(button='left', coords=(x_fireshot, 115))

        time.sleep(25)

        # Click on the "Save to PDF" button
        pywinauto.mouse.click(button='left', coords=(1160, 330))

        time.sleep(5)

        # Click on the bar to select the folder
        pywinauto.mouse.click(button='left', coords=(380, 50))

        time.sleep(5)

        # Enter the path folder
        pywinauto.keyboard.send_keys(
            "A:\\1_Professionnel\\1_Holomorphe\\1_Administration\\2_Gestion_Declarations_Administratives"
            "\\1_Recurrentes\\1_DGFIP\\7_Declaration_I_D_R__Revenus_Capitaux_Mobiliers\\" + path_folder
        )

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

        # Insert the 'Page_3.pdf'
        pywinauto.keyboard.send_keys('Page_3.pdf')

        time.sleep(5)

        # Click on the 'Enregistrer' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(5)

        # Close the onglet
        pywinauto.keyboard.send_keys('^w')

        time.sleep(5)

        # Click on the screen
        pywinauto.mouse.click(button='left', coords=(600, 10))

        time.sleep(5)

        # Click on the 'Imprimer' button
        pywinauto.mouse.click(button='left', coords=(700, 460))

        time.sleep(5)

        # Click on the 'Imprimer' button
        pywinauto.mouse.click(button='left', coords=(150, 615))

        time.sleep(5)

        # Click on the bar to select the folder
        pywinauto.mouse.click(button='left', coords=(380, 50))

        time.sleep(5)

        # Enter the path folder
        pywinauto.keyboard.send_keys(
            "A:\\1_Professionnel\\1_Holomorphe\\1_Administration\\2_Gestion_Declarations_Administratives"
            "\\1_Recurrentes\\1_DGFIP\\7_Declaration_I_D_R__Revenus_Capitaux_Mobiliers\\" + path_folder
        )

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

        # Insert the 'Page_4.pdf'
        pywinauto.keyboard.send_keys('Page_4.pdf')

        time.sleep(5)

        # Click on the 'Enregistrer' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(5)

        # Click on the 'Valider' button
        pywinauto.mouse.click(button='left', coords=(860, 460))

        time.sleep(5)

        # Click on the "Fireshot" button
        pywinauto.mouse.click(button='left', coords=(x_fireshot, y_fireshot))

        time.sleep(5)

        # Click on the "Capture entire page" button
        pywinauto.mouse.click(button='left', coords=(x_fireshot, 115))

        time.sleep(25)

        # Click on the "Save to PDF" button
        pywinauto.mouse.click(button='left', coords=(1160, 330))

        time.sleep(5)

        # Click on the bar to select the folder
        pywinauto.mouse.click(button='left', coords=(380, 50))

        time.sleep(5)

        # Enter the path folder
        pywinauto.keyboard.send_keys(
            "A:\\1_Professionnel\\1_Holomorphe\\1_Administration\\2_Gestion_Declarations_Administratives"
            "\\1_Recurrentes\\1_DGFIP\\7_Declaration_I_D_R__Revenus_Capitaux_Mobiliers\\" + path_folder
        )

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

        # Insert the 'Page_5.pdf'
        pywinauto.keyboard.send_keys('Page_5.pdf')

        time.sleep(5)

        # Click on the 'Enregistrer' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(5)

        # Close the onglet
        pywinauto.keyboard.send_keys('^w')

        time.sleep(5)

        # Click on the screen
        pywinauto.mouse.click(button='left', coords=(600, 10))

        time.sleep(5)

        print("ccleaner running")
        os.system("set ccleaner='C:\\Program Files\\CCleaner\\CCleaner.exe'")
        os.system("start ccleaner /AUTO")

        time.sleep(5)

    # ok
    def test_declarer_taxe_sur_les_salaires_neant(self):
        print("test_declarer_taxe_sur_les_salaires_neant")

        x_taxes_sur_les_salaires_button = 575

        y_taxes_sur_les_salaires_button = 635

        x_fireshot = 1240

        y_fireshot = 50

        path_folder = "\\3_Annee_2022\\1_Janvier_Pour_Decembre_2021_[Neant]"

        app = Application(backend="uia")

        app.start("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")

        time.sleep(6)

        pywinauto.keyboard.send_keys("https://www.impots.gouv.fr/portail/")

        time.sleep(3)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(10)

        # Click on the "Votre espace professionnel" button
        pywinauto.mouse.click(button='left', coords=(1110, 160))

        time.sleep(5)

        # Click on the "Adresse électronique" input
        pywinauto.mouse.click(button='left', coords=(200, 345))

        time.sleep(5)

        # Insert the 'email'
        pywinauto.keyboard.send_keys(".@outlook.fr")

        time.sleep(5)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(5)

        # Insert the 'M_D_P'
        pywinauto.keyboard.send_keys("")

        time.sleep(5)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(5)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(10)

        # Click on the screen
        # pywinauto.mouse.click(button='left', coords=(1000, 400))

        # time.sleep(5)

        # {DOWN} 2 times
        # pywinauto.keyboard.send_keys('{DOWN 2}')

        # time.sleep(5)

        # Click on the "Taxe sur les salaires" button
        pywinauto.mouse.click(button='left', coords=(x_taxes_sur_les_salaires_button, y_taxes_sur_les_salaires_button))

        time.sleep(5)

        # Click on the "Fireshot" button
        pywinauto.mouse.click(button='left', coords=(x_fireshot, y_fireshot))

        time.sleep(5)

        # Click on the "Capture entire page" button
        pywinauto.mouse.click(button='left', coords=(x_fireshot, 115))

        time.sleep(5)

        # Click on the "Save to PDF" button
        pywinauto.mouse.click(button='left', coords=(1160, 330))

        time.sleep(5)

        # Click on the bar to select the folder
        pywinauto.mouse.click(button='left', coords=(380, 50))

        time.sleep(5)

        # Enter the path folder
        pywinauto.keyboard.send_keys("A:\\1_Professionnel\\1_Holomorphe\\1_Administration\\2_Gestion_Declarations_Administratives\\1_Recurrentes\\1_DGFIP\\12_Declaration_Taxes_Sur_Les_Salaires" + path_folder)

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
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(5)

        # Close the onglet
        pywinauto.keyboard.send_keys('^w')

        time.sleep(5)

        # Click on the 'Quitter' button
        pywinauto.mouse.click(button='left', coords=(40, 275))

        time.sleep(5)

        # Close the onglet
        pywinauto.keyboard.send_keys('^w')

        time.sleep(5)

        print("ccleaner running")
        os.system("set ccleaner='C:\\Program Files\\CCleaner\\CCleaner.exe'")
        os.system("start ccleaner /AUTO")

        time.sleep(5)

    # ok
    def test_declarer_cvae_neant(self):
        print("test_declarer_cvae")

        x_fireshot = 1240

        y_fireshot = 50

        path_folder = "\\2_Annee_2021\\10_Octobre_Pour_Septembre"

        app = Application(backend="uia")

        app.start("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")

        time.sleep(6)

        pywinauto.keyboard.send_keys("https://www.impots.gouv.fr/portail/")

        time.sleep(3)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(5)

        # Click on the "Votre espace professionnel" button
        pywinauto.mouse.click(button='left', coords=(1110, 160))

        time.sleep(5)

        # Click on the "Adresse électronique" input
        pywinauto.mouse.click(button='left', coords=(160, 370))

        time.sleep(5)

        # Insert the 'email'
        pywinauto.keyboard.send_keys(".@outlook.fr")

        time.sleep(5)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(5)

        # Insert the 'M_D_P'
        pywinauto.keyboard.send_keys("")

        time.sleep(5)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(5)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(10)

        # Click on the screen
        pywinauto.mouse.click(button='left', coords=(1000, 400))

        time.sleep(5)

        # {DOWN} 2 times
        pywinauto.keyboard.send_keys('{DOWN 2}')

        time.sleep(5)

        # Click on the "CVAE" button
        pywinauto.mouse.click(button='left', coords=(500, 500))

        time.sleep(5)

        # Click on the "Déclarer" button
        pywinauto.mouse.click(button='left', coords=(690, 410))

        time.sleep(5)

        # Click on the "Fireshot" button
        pywinauto.mouse.click(button='left', coords=(x_fireshot, y_fireshot))

        time.sleep(5)

        # Click on the "Capture entire page" button
        pywinauto.mouse.click(button='left', coords=(x_fireshot, 115))

        time.sleep(10)

        # Click on the "Save to PDF" button
        pywinauto.mouse.click(button='left', coords=(1160, 330))

        time.sleep(5)

        # Click on the bar to select the folder
        pywinauto.mouse.click(button='left', coords=(380, 50))

        time.sleep(5)

        # Enter the path folder
        pywinauto.keyboard.send_keys("A:\\1_Professionnel\\1_Holomorphe\\1_Administration\\2_Gestion_Declarations_Administratives\\1_Recurrentes\\1_DGFIP\\8_Declaration_C_E_T\\2_C_V_A_E" + path_folder)

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
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(5)

        # Close the onglet
        pywinauto.keyboard.send_keys('^w')

        time.sleep(5)

        # Click on the 'Quitter' button
        pywinauto.mouse.click(button='left', coords=(50, 250))

        time.sleep(5)

        # Click on the 'Quitter' button
        pywinauto.mouse.click(button='left', coords=(40, 275))

        time.sleep(5)

        # Close the onglet
        pywinauto.keyboard.send_keys('^w')

        time.sleep(5)

        print("ccleaner running")
        os.system("set ccleaner='C:\\Program Files\\CCleaner\\CCleaner.exe'")
        os.system("start ccleaner /AUTO")

        time.sleep(5)

    # ok
    def test_declarer_tva_deductible_uniquement(self):
        print("test_declarer_tva_deductible_uniquement")

        x_fireshot = 1240

        y_fireshot = 50

        ligne_20 = "14"

        ligne_22 = "105"

        path_folder = "2_Annee_2021\\9_Septembre_Pour_Aout"

        app = Application(backend="uia")

        app.start("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")

        time.sleep(6)

        pywinauto.keyboard.send_keys("https://www.impots.gouv.fr/portail/")

        time.sleep(3)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(5)

        # Click on the "Votre espace professionnel" button
        pywinauto.mouse.click(button='left', coords=(1110, 160))

        time.sleep(5)

        # Click on the "Adresse électronique" input
        pywinauto.mouse.click(button='left', coords=(200, 340))

        time.sleep(5)

        # Insert the 'email'
        pywinauto.keyboard.send_keys(".@outlook.fr")

        time.sleep(5)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(5)

        # Insert the 'M_D_P'
        pywinauto.keyboard.send_keys("")

        time.sleep(5)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(5)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(10)

        # Click on the screen
        # pywinauto.mouse.click(button='left', coords=(1000, 400))

        # time.sleep(5)

        # {DOWN} 2 times
        # pywinauto.keyboard.send_keys('{DOWN 2}')

        # time.sleep(5)

        # Click on the "TVA" button
        pywinauto.mouse.click(button='left', coords=(500, 570))

        time.sleep(5)

        # Click on the "Fireshot" button
        pywinauto.mouse.click(button='left', coords=(x_fireshot, y_fireshot))

        time.sleep(5)

        # Click on the "Capture entire page" button
        pywinauto.mouse.click(button='left', coords=(x_fireshot, 110))

        time.sleep(10)

        # Click on the "Save to PDF" button
        pywinauto.mouse.click(button='left', coords=(1160, 330))

        time.sleep(5)

        # Click on the bar to select the folder
        pywinauto.mouse.click(button='left', coords=(380, 50))

        time.sleep(5)

        # Enter the path folder
        pywinauto.keyboard.send_keys(
            "A:\\1_Professionnel\\1_Holomorphe\\1_Administration\\2_Gestion_Declarations_Administratives\\1_Recurrentes\\1_DGFIP\\9_Declaration_TVA\\" + path_folder)

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
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(5)

        # Close the onglet
        pywinauto.keyboard.send_keys('^w')

        time.sleep(5)

        # Click on the screen
        pywinauto.mouse.click(button='left', coords=(600, 10))

        time.sleep(5)

        # Click on the "Déclarer" button
        pywinauto.mouse.click(button='left', coords=(690, 410))

        time.sleep(10)

        # Click on the "Fireshot" button
        pywinauto.mouse.click(button='left', coords=(x_fireshot, y_fireshot))

        time.sleep(5)

        # Click on the "Capture entire page" button
        pywinauto.mouse.click(button='left', coords=(x_fireshot, 115))

        time.sleep(10)

        # Click on the "Save to PDF" button
        pywinauto.mouse.click(button='left', coords=(1160, 330))

        time.sleep(5)

        # Click on the bar to select the folder
        pywinauto.mouse.click(button='left', coords=(380, 50))

        time.sleep(5)

        # Enter the path folder
        pywinauto.keyboard.send_keys(
            "A:\\1_Professionnel\\1_Holomorphe\\1_Administration\\2_Gestion_Declarations_Administratives\\1_Recurrentes\\1_DGFIP\\9_Declaration_TVA\\" + path_folder)

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
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(5)

        # Close the onglet
        pywinauto.keyboard.send_keys('^w')

        time.sleep(5)

        # Click on the screen
        pywinauto.mouse.click(button='left', coords=(600, 10))

        time.sleep(5)

        # Click on the 'mois annee' button
        pywinauto.mouse.click(button='left', coords=(130, 440))

        time.sleep(10)

        # Click on the "Fireshot" button
        pywinauto.mouse.click(button='left', coords=(x_fireshot, y_fireshot))

        time.sleep(5)

        # Click on the "Capture entire page" button
        pywinauto.mouse.click(button='left', coords=(x_fireshot, 115))

        time.sleep(10)

        # Click on the "Save to PDF" button
        pywinauto.mouse.click(button='left', coords=(1160, 330))

        time.sleep(5)

        # Click on the bar to select the folder
        pywinauto.mouse.click(button='left', coords=(380, 50))

        time.sleep(5)

        # Enter the path folder
        pywinauto.keyboard.send_keys(
            "A:\\1_Professionnel\\1_Holomorphe\\1_Administration\\2_Gestion_Declarations_Administratives\\1_Recurrentes\\1_DGFIP\\9_Declaration_TVA\\" + path_folder)

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

        # Insert the 'Page_3.pdf'
        pywinauto.keyboard.send_keys('Page_3.pdf')

        time.sleep(5)

        # Click on the 'Enregistrer' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(5)

        # Close the onglet
        pywinauto.keyboard.send_keys('^w')

        time.sleep(5)

        # Click on the screen
        pywinauto.mouse.click(button='left', coords=(600, 10))

        time.sleep(5)

        # Click on the screen
        pywinauto.mouse.click(button='left', coords=(500, 500))

        time.sleep(5)

        # {DOWN} 25 times
        pywinauto.keyboard.send_keys('{DOWN 25}')

        time.sleep(5)

        # Click on the "20 Autres biens et services" input
        pywinauto.mouse.click(button='left', coords=(1130, 150))

        time.sleep(5)

        # Insert the value for "20 Autres biens et services" input
        pywinauto.keyboard.send_keys(ligne_20)

        time.sleep(5)

        # Press 4 times for the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB 4}")

        time.sleep(5)

        # Insert the value for "22 Report du crédit apparaissant ligne 27 de la précédente déclaration" input
        pywinauto.keyboard.send_keys(ligne_22)

        time.sleep(5)

        # Click on the screen
        pywinauto.mouse.click(button='left', coords=(1300, 370))

        time.sleep(5)

        # {DOWN} 11 times
        pywinauto.keyboard.send_keys('{DOWN 11}')

        time.sleep(5)

        # Click on the "Fireshot" button
        pywinauto.mouse.click(button='left', coords=(x_fireshot, y_fireshot))

        time.sleep(5)

        # Click on the "Capture entire page" button
        pywinauto.mouse.click(button='left', coords=(x_fireshot, 115))

        time.sleep(10)

        # Click on the "Save to PDF" button
        pywinauto.mouse.click(button='left', coords=(1160, 330))

        time.sleep(5)

        # Click on the bar to select the folder
        pywinauto.mouse.click(button='left', coords=(380, 50))

        time.sleep(5)

        # Enter the path folder
        pywinauto.keyboard.send_keys(
            "A:\\1_Professionnel\\1_Holomorphe\\1_Administration\\2_Gestion_Declarations_Administratives\\1_Recurrentes\\1_DGFIP\\9_Declaration_TVA\\" + path_folder)

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

        # Insert the 'Page_4.pdf'
        pywinauto.keyboard.send_keys('Page_4.pdf')

        time.sleep(5)

        # Click on the 'Enregistrer' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(5)

        # Close the onglet
        pywinauto.keyboard.send_keys('^w')

        time.sleep(5)

        # Click on the screen
        pywinauto.mouse.click(button='left', coords=(600, 10))

        time.sleep(5)

        # Click on the "Valider" button
        pywinauto.mouse.click(button='left', coords=(560, 670))

        time.sleep(5)

        # Click on the "Oui" button
        pywinauto.mouse.click(button='left', coords=(600, 380))

        time.sleep(5)

        # Click on the "Fireshot" button
        pywinauto.mouse.click(button='left', coords=(x_fireshot, y_fireshot))

        time.sleep(5)

        # Click on the "Capture entire page" button
        pywinauto.mouse.click(button='left', coords=(x_fireshot, 115))

        time.sleep(10)

        # Click on the "Save to PDF" button
        pywinauto.mouse.click(button='left', coords=(1160, 330))

        time.sleep(5)

        # Click on the bar to select the folder
        pywinauto.mouse.click(button='left', coords=(380, 50))

        time.sleep(5)

        # Enter the path folder
        pywinauto.keyboard.send_keys(
            "A:\\1_Professionnel\\1_Holomorphe\\1_Administration\\2_Gestion_Declarations_Administratives\\1_Recurrentes\\1_DGFIP\\9_Declaration_TVA\\" + path_folder)

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

        # Insert the 'Page_5.pdf'
        pywinauto.keyboard.send_keys('Page_5.pdf')

        time.sleep(5)

        # Click on the 'Enregistrer' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(5)

        # Close the onglet
        pywinauto.keyboard.send_keys('^w')

        time.sleep(5)

        # Click on the screen
        pywinauto.mouse.click(button='left', coords=(600, 10))

        time.sleep(5)

        # Click on the screen
        pywinauto.mouse.click(button='left', coords=(500, 500))

        time.sleep(5)

        # {DOWN} 20 times
        pywinauto.keyboard.send_keys('{DOWN 20}')

        time.sleep(5)

        # Click on the "Imprimer" button on the page
        pywinauto.mouse.click(button='left', coords=(690, 580))

        time.sleep(5)

        # Click on the "Imprimer" button on the page "Imprimer"
        pywinauto.mouse.click(button='left', coords=(150, 610))

        time.sleep(5)

        # Click on the bar to select the folder
        pywinauto.mouse.click(button='left', coords=(380, 50))

        time.sleep(5)

        # Enter the path folder
        pywinauto.keyboard.send_keys(
            "A:\\1_Professionnel\\1_Holomorphe\\1_Administration\\2_Gestion_Declarations_Administratives\\1_Recurrentes\\1_DGFIP\\9_Declaration_TVA\\" + path_folder)

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

        # Insert the 'Page_6.pdf'
        pywinauto.keyboard.send_keys('Page_6.pdf')

        time.sleep(5)

        # Click on the 'Enregistrer' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(15)

        # Click on the 'Screen'
        pywinauto.mouse.click(button='left', coords=(500, 500))

        time.sleep(5)

        # Close the PDF file
        pywinauto.keyboard.send_keys('%{F4}')

        time.sleep(5)

        # Click on the 'Valider' button
        pywinauto.mouse.click(button='left', coords=(830, 580))

        time.sleep(5)

        # Click on the "Fireshot" button
        pywinauto.mouse.click(button='left', coords=(x_fireshot, y_fireshot))

        time.sleep(5)

        # Click on the "Capture entire page" button
        pywinauto.mouse.click(button='left', coords=(x_fireshot, 115))

        time.sleep(10)

        # Click on the "Save to PDF" button
        pywinauto.mouse.click(button='left', coords=(1160, 330))

        time.sleep(5)

        # Click on the bar to select the folder
        pywinauto.mouse.click(button='left', coords=(380, 50))

        time.sleep(5)

        # Enter the path folder
        pywinauto.keyboard.send_keys(
            "A:\\1_Professionnel\\1_Holomorphe\\1_Administration\\2_Gestion_Declarations_Administratives\\1_Recurrentes\\1_DGFIP\\9_Declaration_TVA\\" + path_folder)

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

        # Insert the 'Page_7.pdf'
        pywinauto.keyboard.send_keys('Page_7.pdf')

        time.sleep(5)

        # Click on the 'Enregistrer' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(5)

        # Close the onglet
        pywinauto.keyboard.send_keys('^w')

        time.sleep(5)

        # Click on the screen
        pywinauto.mouse.click(button='left', coords=(600, 10))

        time.sleep(5)

        # Click on the 'Signer et envoyer' button
        pywinauto.mouse.click(button='left', coords=(690, 520))

        time.sleep(5)

    # ok
    def test_declarer_dernier_is(self):
        print('test_declarer_dernier_is')

        x_fireshot = 1240

        y_fireshot = 50

        path_folder = "2_Annee_2021\\1_01_04_2020_31_12_2020"

        app = Application(backend="uia")

        app.start("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")

        time.sleep(6)

        pywinauto.keyboard.send_keys("https://www.impots.gouv.fr/portail/")

        time.sleep(3)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(5)

        # Click on the "Votre espace professionnel" button
        pywinauto.mouse.click(button='left', coords=(1110, 160))

        time.sleep(5)

        # Click on the "Adresse électronique" input
        pywinauto.mouse.click(button='left', coords=(200, 340))

        time.sleep(5)

        # Insert the 'email'
        pywinauto.keyboard.send_keys(".@outlook.fr")

        time.sleep(5)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(5)

        # Insert the 'M_D_P'
        pywinauto.keyboard.send_keys("")

        time.sleep(5)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(5)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(10)

        # Click on the "Impots sur les societes" button
        pywinauto.mouse.click(button='left', coords=(550, 555))

        time.sleep(5)

        # Click on the "Fireshot" button
        pywinauto.mouse.click(button='left', coords=(x_fireshot, y_fireshot))

        time.sleep(5)

        # Click on the "Capture entire page" button
        pywinauto.mouse.click(button='left', coords=(x_fireshot, 115))

        time.sleep(10)

        # Click on the "Save to PDF" button
        pywinauto.mouse.click(button='left', coords=(1160, 330))

        time.sleep(5)

        # Click on the bar to select the folder
        pywinauto.mouse.click(button='left', coords=(380, 50))

        time.sleep(5)

        # Enter the path folder
        pywinauto.keyboard.send_keys(
            "A:\\1_Professionnel\\1_Holomorphe\\1_Administration\\2_Gestion_Declarations_Administratives\\1_Recurrentes\\1_DGFIP\\2_Declaration_Impot_Societes\\" + path_folder
        )

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
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(5)

        # Close the onglet
        pywinauto.keyboard.send_keys('^w')

        time.sleep(5)

        # Click on the screen
        pywinauto.mouse.click(button='left', coords=(600, 10))

        time.sleep(5)

        # Click on the "Declarer" button
        pywinauto.mouse.click(button='left', coords=(670, 405))

        time.sleep(10)

        # Click on the "Fireshot" button
        pywinauto.mouse.click(button='left', coords=(x_fireshot, y_fireshot))

        time.sleep(5)

        # Click on the "Capture entire page" button
        pywinauto.mouse.click(button='left', coords=(x_fireshot, 110))

        time.sleep(10)

        # Click on the "Save to PDF" button
        pywinauto.mouse.click(button='left', coords=(1160, 330))

        time.sleep(5)

        # Click on the bar to select the folder
        pywinauto.mouse.click(button='left', coords=(380, 50))

        time.sleep(5)

        # Enter the path folder
        pywinauto.keyboard.send_keys(
            "A:\\1_Professionnel\\1_Holomorphe\\1_Administration\\2_Gestion_Declarations_Administratives\\1_Recurrentes\\1_DGFIP\\2_Declaration_Impot_Societes\\" + path_folder
        )

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
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(5)

        # Close the onglet
        pywinauto.keyboard.send_keys('^w')

        time.sleep(5)

        # Click on the screen
        pywinauto.mouse.click(button='left', coords=(600, 10))

        time.sleep(5)

        # Click on the "Période d'imposition" button
        pywinauto.mouse.click(button='left', coords=(170, 480))

        time.sleep(5)

        # Click on the "Fireshot" button
        pywinauto.mouse.click(button='left', coords=(x_fireshot, y_fireshot))

        time.sleep(5)

        # Click on the "Capture entire page" button
        pywinauto.mouse.click(button='left', coords=(x_fireshot, 110))

        time.sleep(10)

        # Click on the "Save to PDF" button
        pywinauto.mouse.click(button='left', coords=(1160, 330))

        time.sleep(5)

        # Click on the bar to select the folder
        pywinauto.mouse.click(button='left', coords=(380, 50))

        time.sleep(5)

        # Enter the path folder
        pywinauto.keyboard.send_keys(
            "A:\\1_Professionnel\\1_Holomorphe\\1_Administration\\2_Gestion_Declarations_Administratives\\1_Recurrentes\\1_DGFIP\\2_Declaration_Impot_Societes\\" + path_folder
        )

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

        # Insert the 'Page_3.pdf'
        pywinauto.keyboard.send_keys('Page_3.pdf')

        time.sleep(5)

        # Click on the 'Enregistrer' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(5)

        # Close the onglet
        pywinauto.keyboard.send_keys('^w')

        time.sleep(5)

        # Click on the screen
        pywinauto.mouse.click(button='left', coords=(600, 10))

        time.sleep(5)

        # Click on the '139 Impôt sur les sociétés (taux normal à 31%) - 140' input
        pywinauto.mouse.click(button='left', coords=(920, 680))

        time.sleep(5)

        # Insert the value of '139 Impôt sur les sociétés (taux normal à 31%) - 140'
        pywinauto.keyboard.send_keys("0")

        time.sleep(5)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(5)

        # Insert the value of '137 - Impôt sur les sociétés (taux normal à 28%) - 138'
        pywinauto.keyboard.send_keys("0")

        time.sleep(5)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(5)

        # Insert the value of '103 - Impôt sur les sociétés (taux réduit) - 104'
        pywinauto.keyboard.send_keys("0")

        time.sleep(5)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(5)

        # Insert the value of '105 - Impôt sur les plus values nettes'
        pywinauto.keyboard.send_keys("0")

        time.sleep(5)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(5)

        # Insert the value of '106 - Autre impôt à taux particulier'
        pywinauto.keyboard.send_keys("0")

        time.sleep(5)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(5)

        # Insert the value of '35 - MEC - Réduction d'impôt au titre du mécénat au titre de N'
        pywinauto.keyboard.send_keys("0")

        time.sleep(5)

        # créances non reportables et non restituables à déclarer
        creances_non_reportables_non_restituables_declarer = "non"

        if creances_non_reportables_non_restituables_declarer == "oui":
            pywinauto.mouse.click(button='left', coords=(1095, 205))
        else:
            pywinauto.mouse.click(button='left', coords=(1150, 205))

        time.sleep(5)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(5)

        # Insert the value of '40 - Dont montant des dons consentis à des organismes étrangers
        # (situés dans un pays de l'UE ou de l'EEE)'
        pywinauto.keyboard.send_keys("0")

        time.sleep(5)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(5)

        # Insert the value of '109 - MEC - Solde de créance des exercices antérieurs (Exercices N-5 à N-1)'
        pywinauto.keyboard.send_keys("0")

        time.sleep(5)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(5)

        # Insert the value of '64 - CIC - Crédit d'impôt compétitivité Emploi au titre de N'
        pywinauto.keyboard.send_keys("0")

        time.sleep(5)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(5)

        # Insert the value of '65 - Montant du préfinancement'
        pywinauto.keyboard.send_keys("0")

        time.sleep(5)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(5)

        # exercice fiscal de plus de 12 mois et cloturant le 31 décembre
        exercice_fiscal_de_plus_de_12_mois_et_cloturant_le_31_decembre = "non"

        if exercice_fiscal_de_plus_de_12_mois_et_cloturant_le_31_decembre == "oui":
            pywinauto.mouse.click(button='left', coords=(1095, 590))
        else:
            pywinauto.mouse.click(button='left', coords=(1150, 590))

        time.sleep(5)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(5)

        # Insert the value of '110 - CIC - Solde de créance des exercices antérieurs (Exercices N-3 à N-1)'
        pywinauto.keyboard.send_keys("0")

        time.sleep(5)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(5)

        # Insert the value of '33 - COR - Crédit d'impôt pour investissement en CORSE au titre de N'
        pywinauto.keyboard.send_keys("0")

        time.sleep(5)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(5)

        # Insert the value of '111 - COR - Solde de créance des exercices antérieurs (Exercices N-10 à N-1)'
        pywinauto.keyboard.send_keys("0")

        time.sleep(5)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(5)

        # Insert the value of '34 - RAD - Report en arrière de déficits au titre de N'
        pywinauto.keyboard.send_keys("0")

        time.sleep(5)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(5)

        # Insert the value of '112 - RAD - Solde de créance des exercices antérieurs (Exercices N-5 à N-1)'
        pywinauto.keyboard.send_keys("0")

        time.sleep(5)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(5)

        # Insert the value of '31 - CIR - Crédit impôt recherche au titre de N'
        pywinauto.keyboard.send_keys("0")

        time.sleep(5)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(5)

        # Insert the value of '113 - CIR - Solde de créance des exercices antérieurs (Exercices N-3 à N-1)'
        pywinauto.keyboard.send_keys("0")

        time.sleep(5)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(5)

        # Insert the value of '50 - Nouvelles créances non répertoriées au titre de N'
        pywinauto.keyboard.send_keys("")

        time.sleep(5)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(5)

        # Insert the value of '114 - Type de créance portée dans la case 50'
        pywinauto.keyboard.send_keys("")

        time.sleep(5)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(5)

        # Insert the value of '22 - FOR - Crédit d'impôt formation des dirigeants d'entreprise'
        pywinauto.keyboard.send_keys("0")

        time.sleep(5)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(5)

        # Insert the value of '23 - RAC - Crédit pour le rachat d'une entreprise par ses salariés'
        pywinauto.keyboard.send_keys("0")

        time.sleep(5)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(5)

        # Insert the value of '24 - FAM - Crédit d'impôt famille'
        pywinauto.keyboard.send_keys("0")

        time.sleep(5)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(5)

        # Insert the value of '25 - CIN - Crédit d'impôt pour dépenses de production d'oeuvres cinématographiques'
        pywinauto.keyboard.send_keys("0")

        time.sleep(5)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(5)

        # autres créances non reportables et restituables à déclarer
        autres_creances_non_reportables_et_restituables_a_declarer = "non"

        if autres_creances_non_reportables_et_restituables_a_declarer == "oui":
            pywinauto.mouse.click(button='left', coords=(1095, 440))
        else:
            pywinauto.mouse.click(button='left', coords=(1150, 440))

        time.sleep(5)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(5)

        # Insert the value of '69 - Versements effectués (acomptes et/ou soldes) moins remboursements déjà obtenus'
        pywinauto.keyboard.send_keys("0")

        time.sleep(5)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(5)

        # Insert the value of '38 - Montant d'impôt exclu du calcul des acomptes IS'
        pywinauto.keyboard.send_keys("0")

        time.sleep(5)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(5)

        # Click on the screen
        pywinauto.mouse.click(button='left', coords=(1290, 400))

        time.sleep(5)

        # Press the 'UP' button 6 times
        pywinauto.keyboard.send_keys("{UP 6}")

        time.sleep(5)

        # REDEVABLE DE LA CSB
        redevable_de_la_csb = "non"

        if redevable_de_la_csb == "oui":
            pywinauto.mouse.click(button='left', coords=(1095, 385))
        else:
            pywinauto.mouse.click(button='left', coords=(1150, 385))

        time.sleep(5)

        # REDEVABLE DE LA CRL
        redevable_de_la_crl = "non"

        if redevable_de_la_crl == "oui":
            pywinauto.mouse.click(button='left', coords=(1095, 495))
        else:
            pywinauto.mouse.click(button='left', coords=(1150, 495))

        time.sleep(5)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB 4}")

        time.sleep(5)

        # Insert the value of '13 - Montant de l'excédent imputé sur le premier acompte de l'exercice suivant'
        pywinauto.keyboard.send_keys("")

        time.sleep(5)

        # Click on the screen
        pywinauto.mouse.click(button='left', coords=(1300, 605))

        time.sleep(5)

        # Press the 'Down' button in 4 times
        pywinauto.keyboard.send_keys("{DOWN 4}")

        time.sleep(5)

        # Click on the "Fireshot" button
        pywinauto.mouse.click(button='left', coords=(x_fireshot, y_fireshot))

        time.sleep(5)

        # Click on the "Capture entire page" button
        pywinauto.mouse.click(button='left', coords=(x_fireshot, 115))

        time.sleep(10)

        # Click on the "Save to PDF" button
        pywinauto.mouse.click(button='left', coords=(1160, 330))

        time.sleep(5)

        # Click on the bar to select the folder
        pywinauto.mouse.click(button='left', coords=(380, 50))

        time.sleep(5)

        # Enter the path folder
        pywinauto.keyboard.send_keys(
            "A:\\1_Professionnel\\1_Holomorphe\\1_Administration\\2_Gestion_Declarations_Administratives\\1_Recurrentes\\1_DGFIP\\2_Declaration_Impot_Societes\\" + path_folder
        )

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

        # Insert the 'Page_4.pdf'
        pywinauto.keyboard.send_keys('Page_4.pdf')

        time.sleep(5)

        # Click on the 'Enregistrer' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(5)

        # Close the onglet
        pywinauto.keyboard.send_keys('^w')

        time.sleep(5)

        # Click on the screen
        pywinauto.mouse.click(button='left', coords=(600, 10))

        time.sleep(5)

        # Click on the 'Valider' button
        pywinauto.mouse.click(button='left', coords=(560, 670))

        time.sleep(5)

        # Click on the "Fireshot" button
        pywinauto.mouse.click(button='left', coords=(x_fireshot, y_fireshot))

        time.sleep(5)

        # Click on the "Capture entire page" button
        pywinauto.mouse.click(button='left', coords=(x_fireshot, 115))

        time.sleep(10)

        # Click on the "Save to PDF" button
        pywinauto.mouse.click(button='left', coords=(1160, 330))

        time.sleep(5)

        # Click on the bar to select the folder
        pywinauto.mouse.click(button='left', coords=(380, 50))

        time.sleep(5)

        # Enter the path folder
        pywinauto.keyboard.send_keys(
            "A:\\1_Professionnel\\1_Holomorphe\\1_Administration\\2_Gestion_Declarations_Administratives\\1_Recurrentes\\1_DGFIP\\2_Declaration_Impot_Societes\\" + path_folder
        )

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

        # Insert the 'Page_5.pdf'
        pywinauto.keyboard.send_keys('Page_5.pdf')

        time.sleep(5)

        # Click on the 'Enregistrer' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(5)

        # Close the onglet
        pywinauto.keyboard.send_keys('^w')

        time.sleep(5)

        # Click on the screen
        pywinauto.mouse.click(button='left', coords=(600, 10))

        time.sleep(5)

        # Click on the screen
        pywinauto.mouse.click(button='left', coords=(1300, 580))

        time.sleep(5)

        # Press the 'Down' button in 30 times
        pywinauto.keyboard.send_keys('{DOWN 30}')

        time.sleep(5)

        # Click on the "Imprimer" button of the declaration
        pywinauto.mouse.click(button='left', coords=(690, 580))

        time.sleep(5)

        # Click on the "Imprimer" button of the print page
        pywinauto.mouse.click(button='left', coords=(150, 610))

        time.sleep(5)

        # Click on the bar to select the folder
        pywinauto.mouse.click(button='left', coords=(380, 50))

        time.sleep(5)

        # Enter the path folder
        pywinauto.keyboard.send_keys(
            "A:\\1_Professionnel\\1_Holomorphe\\1_Administration\\2_Gestion_Declarations_Administratives\\1_Recurrentes\\1_DGFIP\\2_Declaration_Impot_Societes\\" + path_folder
        )

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

        # Insert the 'Page_6.pdf'
        pywinauto.keyboard.send_keys('Page_6.pdf')

        time.sleep(5)

        # Click on the 'Enregistrer' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(5)

        # Click on the screen
        pywinauto.mouse.click(button='left', coords=(500, 500))

        time.sleep(5)

        # Press the 'Alt+F4'
        pywinauto.keyboard.send_keys('%{F4}')

        time.sleep(5)


if __name__ == '__main__':
    unittest.main()
