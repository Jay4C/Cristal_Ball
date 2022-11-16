import os
import unittest
import time
from pywinauto.application import Application
import pywinauto.keyboard
import pywinauto.mouse
import pywinauto.base_wrapper
import pywinauto.timings

annee = "3_Annee_2022"
mois = "6_Juin_Pour_Mai"
filename_test = "dsn_test_holomorphe_juin_2022_pour_mai_2022.dsn"
filename_reel = "dsn_reel_holomorphe_juin_2022_pour_mai_2022.dsn"


class UnitTestsDesktopAutomationDSNInternet(unittest.TestCase):
    # ok
    def test_declarer_dsn_test_internet(self):
        print('test_declarer_dsn_test_internet')

        path_folder = annee + "\\" + str(mois)

        filename = filename_test

        x_nom_fichier = 300

        y_nom_fichier = 415

        x_choisir_fichier = 90

        y_choisir_fichier = 490

        time.sleep(6)

        app = Application(backend="uia")

        app.start("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")

        time.sleep(10)

        pywinauto.keyboard.send_keys("https://test.net-entreprises.fr/")

        time.sleep(3)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(10)

        # Click on the "Tout refuser" button
        pywinauto.mouse.click(button='left', coords=(600, 460))

        time.sleep(6)

        # Click on the "Me connecter" button
        pywinauto.mouse.click(button='left', coords=(1200, 110))

        time.sleep(5)

        # Click on the "Siret" input
        pywinauto.mouse.click(button='left', coords=(780, 590))

        time.sleep(5)

        # Insert the Siret
        pywinauto.keyboard.send_keys('')

        time.sleep(5)

        # Click on the "Nom" input
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(5)

        # Insert the Nom
        pywinauto.keyboard.send_keys('')

        time.sleep(5)

        # Click on the "Prénom" input
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(5)

        # Insert the Prénom
        pywinauto.keyboard.send_keys('')

        time.sleep(5)

        # Click on the "Mot de passe" input
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(5)

        # Insert the Mot de passe
        pywinauto.keyboard.send_keys('')

        time.sleep(5)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(5)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(10)

        # Click on the "DSN régime général" button
        pywinauto.mouse.click(button='left', coords=(250, 350))

        time.sleep(10)

        # {DOWN} 4 times
        pywinauto.keyboard.send_keys('{DOWN 4}')

        time.sleep(5)

        # Click on the 'Choisir un fichier' button
        pywinauto.mouse.click(button='left', coords=(x_choisir_fichier, y_choisir_fichier))

        time.sleep(5)

        # Click on the bar to select the folder
        pywinauto.mouse.click(button='left', coords=(380, 50))

        time.sleep(5)

        # Enter the path folder
        pywinauto.keyboard.send_keys(
            "A:\\1_Professionnel\\1_Holomorphe\\1_Administration\\2_Gestion_Declarations_Administratives"
            "\\1_Recurrentes\\2_Net_Entreprises__DSN\\5_Depots_Fichiers_DSN\\3_Tests\\"
            + path_folder
        )

        time.sleep(5)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(5)

        # Click on the 'Nom du fichier :' bar
        pywinauto.mouse.click(button='left', coords=(x_nom_fichier, y_nom_fichier))

        time.sleep(5)

        # Press the 'Ctrl+A'
        pywinauto.keyboard.send_keys('^a')

        time.sleep(5)

        # Insert the 'filename'
        pywinauto.keyboard.send_keys(filename)

        time.sleep(5)

        # Click on the 'Ouvrir' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(5)

        # Click on the 'Envoyer' button
        pywinauto.mouse.click(button='left', coords=(395, 640))

        time.sleep(5)

        print("run_ccleaner")
        os.system("set ccleaner='C:\\Program Files\\CCleaner\\CCleaner.exe'")
        os.system("start ccleaner /AUTO")

    # ok
    def test_declarer_dsn_reel_internet(self):
        print("test_declarer_dsn_reel_internet")

        path_folder = annee + "\\" + str(mois)

        filename = filename_reel

        x_fireshot = 1240

        x_nom_fichier = 300

        y_nom_fichier = 415

        x_choisir_fichier = 90

        y_choisir_fichier = 490

        time.sleep(6)

        app = Application(backend="uia")

        app.start("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")

        time.sleep(7)

        pywinauto.keyboard.send_keys("https://www.net-entreprises.fr/")

        time.sleep(5)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(10)

        # Click on the "Tout refuser" button
        pywinauto.mouse.click(button='left', coords=(600, 460))

        time.sleep(10)

        # Click on the "Me connecter" button
        pywinauto.mouse.click(button='left', coords=(1200, 110))

        time.sleep(10)

        # Click on the "Siret" input
        pywinauto.mouse.click(button='left', coords=(780, 490))

        time.sleep(10)

        # Insert the Siret
        pywinauto.keyboard.send_keys('')

        time.sleep(10)

        # Click on the "Nom" input
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(5)

        # Insert the Nom
        pywinauto.keyboard.send_keys('')

        time.sleep(5)

        # Click on the "Prénom" input
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(5)

        # Insert the Prénom
        pywinauto.keyboard.send_keys('')

        time.sleep(5)

        # Click on the "Mot de passe" input
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(5)

        # Insert the Mot de passe
        pywinauto.keyboard.send_keys('')

        time.sleep(5)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(5)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(10)

        # Click on the "DSN régime général" button
        pywinauto.mouse.click(button='left', coords=(530, 320))

        time.sleep(20)

        # {DOWN} 4 times
        pywinauto.keyboard.send_keys('{DOWN 4}')

        time.sleep(5)

        # Click on the 'Choisir un fichier' button
        pywinauto.mouse.click(button='left', coords=(x_choisir_fichier, y_choisir_fichier))

        time.sleep(5)

        # Click on the bar to select the folder
        pywinauto.mouse.click(button='left', coords=(380, 50))

        time.sleep(5)

        # Enter the path folder
        pywinauto.keyboard.send_keys(
            "A:\\1_Professionnel\\1_Holomorphe\\1_Administration\\2_Gestion_Declarations_Administratives"
            "\\1_Recurrentes"
            "\\2_Net_Entreprises__DSN\\5_Depots_Fichiers_DSN\\2_Reels\\" + path_folder
        )

        time.sleep(5)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(5)

        # Click on the 'Nom du fichier :' bar
        pywinauto.mouse.click(button='left', coords=(260, 415))

        time.sleep(5)

        # Press the 'Ctrl+A'
        pywinauto.keyboard.send_keys('^a')

        time.sleep(5)

        # Insert the 'filename'
        pywinauto.keyboard.send_keys(filename)

        time.sleep(5)

        # Click on the 'Ouvrir' button
        pywinauto.mouse.click(button='left', coords=(515, 445))

        time.sleep(5)

        # Click on the 'Envoyer' button
        pywinauto.mouse.click(button='left', coords=(390, 645))

        time.sleep(5)

        # Click on the "Fireshot" button
        pywinauto.mouse.click(button='left', coords=(x_fireshot, 50))

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
            "A:\\1_Professionnel\\1_Holomorphe\\1_Administration\\2_Gestion_Declarations_Administratives"
            "\\1_Recurrentes\\2_Net_Entreprises__DSN\\5_Depots_Fichiers_DSN\\2_Reels\\" + path_folder
        )

        time.sleep(5)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(5)

        # Click on the 'Nom du fichier :' bar
        pywinauto.mouse.click(button='left', coords=(x_nom_fichier, y_nom_fichier))

        time.sleep(5)

        # Press the 'Ctrl+A'
        pywinauto.keyboard.send_keys('^a')

        time.sleep(5)

        # Insert the 'Page_Reception.pdf'
        pywinauto.keyboard.send_keys('Page_Reception.pdf')

        time.sleep(5)

        # Click on the 'Enregistrer' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(5)

        # Close the onglet
        pywinauto.keyboard.send_keys('^w')

        time.sleep(5)

        # Click on the 'Cross' button
        pywinauto.mouse.click(button='left', coords=(1345, 700))

        time.sleep(5)

        print("run_ccleaner")
        os.system("set ccleaner='C:\\Program Files\\CCleaner\\CCleaner.exe'")
        os.system("start ccleaner /AUTO")

    # ok
    def test_recuperer_dernier_dsn_test_internet(self):
        print('test_recuperer_dernier_dsn_test_internet')

        path_folder = "3_Annee_2022\\" + str(mois)

        x_fireshot = 1240

        x_nom_fichier = 300

        y_nom_fichier = 375

        time.sleep(6)

        app = Application(backend="uia")

        app.start("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")

        time.sleep(6)

        pywinauto.keyboard.send_keys("https://test.net-entreprises.fr/")

        time.sleep(3)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(5)

        # Click on the "Tout refuser" button
        pywinauto.mouse.click(button='left', coords=(600, 460))

        time.sleep(5)

        # Click on the "Me connecter" button
        pywinauto.mouse.click(button='left', coords=(1200, 110))

        time.sleep(5)

        # Click on the "Siret" input
        pywinauto.mouse.click(button='left', coords=(780, 590))

        time.sleep(5)

        # Insert the Siret
        pywinauto.keyboard.send_keys('')

        time.sleep(5)

        # Click on the "Nom" input
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(5)

        # Insert the Nom
        pywinauto.keyboard.send_keys('')

        time.sleep(5)

        # Click on the "Prénom" input
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(5)

        # Insert the Prénom
        pywinauto.keyboard.send_keys('')

        time.sleep(5)

        # Click on the "Mot de passe" input
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(5)

        # Insert the Mot de passe
        pywinauto.keyboard.send_keys('')

        time.sleep(5)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(5)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(10)

        # Click on the "Pilote DSN RG, fonction publique" button
        pywinauto.mouse.click(button='left', coords=(230, 360))

        time.sleep(5)

        # Click on the "Fireshot" button
        pywinauto.mouse.click(button='left', coords=(x_fireshot, 50))

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
            "A:\\1_Professionnel\\1_Holomorphe\\1_Administration\\2_Gestion_Declarations_Administratives"
            "\\1_Recurrentes\\2_Net_Entreprises__DSN\\5_Depots_Fichiers_DSN\\3_Tests\\" + path_folder
        )

        time.sleep(5)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(5)

        # Click on the 'Nom du fichier :' bar
        pywinauto.mouse.click(button='left', coords=(x_nom_fichier, y_nom_fichier))

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

        # Click on the 'Cross' button
        pywinauto.mouse.click(button='left', coords=(1345, 700))

        time.sleep(5)

        # Click on the 'Glass hand' button
        pywinauto.mouse.click(button='left', coords=(730, 550))

        time.sleep(5)

        # Click on the "Fireshot" button
        pywinauto.mouse.click(button='left', coords=(x_fireshot, 50))

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
            "A:\\1_Professionnel\\1_Holomorphe\\1_Administration\\2_Gestion_Declarations_Administratives\\1_Recurrentes\\2_Net_Entreprises__DSN\\5_Depots_Fichiers_DSN\\3_Tests\\" + path_folder)

        time.sleep(5)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(5)

        # Click on the 'Nom du fichier :' bar
        pywinauto.mouse.click(button='left', coords=(x_nom_fichier, y_nom_fichier))

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

        # Click on the 'Cross' button
        pywinauto.mouse.click(button='left', coords=(1345, 700))

        time.sleep(5)

        # Click on the 'Afficher les certificats de conformité' button
        pywinauto.mouse.click(button='left', coords=(450, 450))

        time.sleep(5)

        # Click on the 'Screen'
        pywinauto.mouse.click(button='left', coords=(500, 300))

        time.sleep(5)

        # Print
        pywinauto.keyboard.send_keys('^p')

        time.sleep(5)

        # Click on the 'Imprimer' button
        pywinauto.mouse.click(button='left', coords=(150, 430))

        time.sleep(5)

        # Click on the bar to select the folder
        pywinauto.mouse.click(button='left', coords=(380, 50))

        time.sleep(5)

        # Enter the path folder
        pywinauto.keyboard.send_keys(
            "A:\\1_Professionnel\\1_Holomorphe\\1_Administration\\2_Gestion_Declarations_Administratives\\1_Recurrentes\\2_Net_Entreprises__DSN\\5_Depots_Fichiers_DSN\\3_Tests\\" + path_folder)

        time.sleep(5)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(5)

        # Click on the 'Nom du fichier :' bar
        pywinauto.mouse.click(button='left', coords=(x_nom_fichier, y_nom_fichier))

        time.sleep(5)

        # Press the 'Ctrl+A'
        pywinauto.keyboard.send_keys('^a')

        time.sleep(5)

        # Insert the 'Page_3.pdf'
        pywinauto.keyboard.send_keys('Page_3.pdf')

        time.sleep(5)

        # Click on the 'Enregistrer' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(10)

        # Click on the 'Screen'
        # pywinauto.mouse.click(button='left', coords=(500, 350))
        # time.sleep(5)

        # Close the PDF file
        # pywinauto.keyboard.send_keys('%{F4}')
        # time.sleep(5)

        # Click on the 'Screen'
        pywinauto.mouse.click(button='left', coords=(380, 300))

        time.sleep(5)

        # Close the screen
        pywinauto.keyboard.send_keys('%{F4}')

        time.sleep(5)

        # Click on the 'Télécharger les certificats de conformité'
        pywinauto.mouse.click(button='left', coords=(560, 445))

        time.sleep(5)

        # Click on the 'Autres téléchargements'
        pywinauto.mouse.click(button='left', coords=(580, 445))

        time.sleep(5)

        for i in range(31):
            # Click on the 'Telecharger' button
            pywinauto.mouse.click(button='left', coords=(630, 470))

            time.sleep(5)

            # Click on the 'Right arrow' button
            pywinauto.mouse.click(button='left', coords=(570, 470))

            time.sleep(5)

        # Click on the 'Autres téléchargements'
        pywinauto.mouse.click(button='left', coords=(580, 445))

        time.sleep(5)

        # Click on the 'Glass hand' button
        pywinauto.mouse.click(button='left', coords=(760, 470))

        time.sleep(5)

        # Click on the "Fireshot" button
        pywinauto.mouse.click(button='left', coords=(x_fireshot, 50))

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
            "A:\\1_Professionnel\\1_Holomorphe\\1_Administration\\2_Gestion_Declarations_Administratives\\1_Recurrentes\\2_Net_Entreprises__DSN\\5_Depots_Fichiers_DSN\\3_Tests\\" + path_folder)

        time.sleep(5)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(5)

        # Click on the 'Nom du fichier :' bar
        pywinauto.mouse.click(button='left', coords=(x_nom_fichier, y_nom_fichier))

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

        # Click on the 'Cross' button
        pywinauto.mouse.click(button='left', coords=(1345, 700))

        time.sleep(5)

        # Click on the 'Afficher le certificat de conformité de cette déclaration de TEST' button
        pywinauto.mouse.click(button='left', coords=(390, 455))

        time.sleep(5)

        # Click on the Screen of the pop-up
        pywinauto.mouse.click(button='left', coords=(350, 320))

        time.sleep(5)

        # Print
        pywinauto.keyboard.send_keys('^p')

        time.sleep(5)

        # Click on the 'Imprimer' button
        pywinauto.mouse.click(button='left', coords=(150, 300))

        time.sleep(5)

        # Click on the bar to select the folder
        pywinauto.mouse.click(button='left', coords=(380, 50))

        time.sleep(5)

        # Enter the path folder
        pywinauto.keyboard.send_keys(
            "A:\\1_Professionnel\\1_Holomorphe\\1_Administration\\2_Gestion_Declarations_Administratives\\1_Recurrentes\\2_Net_Entreprises__DSN\\5_Depots_Fichiers_DSN\\3_Tests\\" + path_folder)

        time.sleep(5)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(5)

        # Click on the 'Nom du fichier :' bar
        pywinauto.mouse.click(button='left', coords=(x_nom_fichier, y_nom_fichier))

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

        # Click on the 'Screen'
        # pywinauto.mouse.click(button='left', coords=(500, 350))
        # time.sleep(5)

        # Close the PDF file
        # pywinauto.keyboard.send_keys('%{F4}')
        # time.sleep(5)

        # Click on the Screen of the pop-up
        pywinauto.mouse.click(button='left', coords=(350, 320))

        time.sleep(5)

        # Close the Screen of the pop-up
        pywinauto.keyboard.send_keys('%{F4}')

        time.sleep(5)

        # Click on the 'Accéder au bilan de traitement  de TEST' button
        pywinauto.mouse.click(button='left', coords=(430, 540))

        time.sleep(5)

        # Click on the Screen of the pop-up
        pywinauto.mouse.click(button='left', coords=(300, 300))

        time.sleep(5)

        # Print
        pywinauto.keyboard.send_keys('^p')

        time.sleep(5)

        # Click on the 'Imprimer' button
        pywinauto.mouse.click(button='left', coords=(150, 425))

        time.sleep(5)

        # Click on the bar to select the folder
        pywinauto.mouse.click(button='left', coords=(380, 50))

        time.sleep(5)

        # Enter the path folder
        pywinauto.keyboard.send_keys(
            "A:\\1_Professionnel\\1_Holomorphe\\1_Administration\\2_Gestion_Declarations_Administratives\\1_Recurrentes\\2_Net_Entreprises__DSN\\5_Depots_Fichiers_DSN\\3_Tests\\" + path_folder)

        time.sleep(5)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(5)

        # Click on the 'Nom du fichier :' bar
        pywinauto.mouse.click(button='left', coords=(x_nom_fichier, y_nom_fichier))

        time.sleep(5)

        # Press the 'Ctrl+A'
        pywinauto.keyboard.send_keys('^a')

        time.sleep(5)

        # Insert the 'Page_5.pdf'
        pywinauto.keyboard.send_keys('Page_6.pdf')

        time.sleep(5)

        # Click on the 'Enregistrer' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(5)

        # Click on the 'Screen'
        # pywinauto.mouse.click(button='left', coords=(500, 350))
        # time.sleep(5)

        # Close the PDF file
        # pywinauto.keyboard.send_keys('%{F4}')
        # time.sleep(5)

        # Click on the Screen of the pop-up
        pywinauto.mouse.click(button='left', coords=(350, 320))

        time.sleep(5)

        # Close the Screen of the pop-up
        pywinauto.keyboard.send_keys('%{F4}')

        time.sleep(5)

        # Click on the 'Retour' button
        pywinauto.mouse.click(button='left', coords=(65, 695))

        time.sleep(5)

        # Click on the 'Retour' button
        pywinauto.mouse.click(button='left', coords=(65, 520))

        time.sleep(5)

        # {DOWN} 10 times
        pywinauto.keyboard.send_keys('{DOWN 10}')

        time.sleep(5)

        # Click on the 'Retour' button
        pywinauto.mouse.click(button='left', coords=(65, 695))

        time.sleep(10)

        # Close the onglet
        pywinauto.keyboard.send_keys('^w')

        time.sleep(5)

        print("run_ccleaner")
        os.system("set ccleaner='C:\\Program Files\\CCleaner\\CCleaner.exe'")
        os.system("start ccleaner /AUTO")

    # ok
    def test_recuperer_dernier_dsn_reel_internet(self):
        print("test_recuperer_dernier_dsn_reel_internet")

        path_folder = "3_Annee_2022\\" + str(mois)

        x_fireshot = 1240

        x_nom_fichier = 300

        y_nom_fichier = 375

        time.sleep(6)

        app = Application(backend="uia")

        app.start("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")

        time.sleep(6)

        pywinauto.keyboard.send_keys("https://www.net-entreprises.fr/")

        time.sleep(3)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(10)

        # Click on the "Tout refuser" button
        pywinauto.mouse.click(button='left', coords=(600, 460))

        time.sleep(5)

        # Click on the "Me connecter" button
        pywinauto.mouse.click(button='left', coords=(1200, 110))

        time.sleep(10)

        # Click on the "Siret" input
        pywinauto.mouse.click(button='left', coords=(780, 490))

        time.sleep(5)

        # Insert the Siret
        pywinauto.keyboard.send_keys('')

        time.sleep(5)

        # Click on the "Nom" input
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(5)

        # Insert the Nom
        pywinauto.keyboard.send_keys('')

        time.sleep(5)

        # Click on the "Prénom" input
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(5)

        # Insert the Prénom
        pywinauto.keyboard.send_keys('')

        time.sleep(5)

        # Click on the "Mot de passe" input
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(5)

        # Insert the Mot de passe
        pywinauto.keyboard.send_keys('')

        time.sleep(5)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(5)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(10)

        # Click on the "DSN régime général" button
        pywinauto.mouse.click(button='left', coords=(530, 330))

        time.sleep(5)

        # Click on the "Fireshot" button
        pywinauto.mouse.click(button='left', coords=(x_fireshot, 50))

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
        pywinauto.keyboard.send_keys("A:\\1_Professionnel\\1_Holomorphe\\1_Administration\\2_Gestion_Declarations_Administratives\\1_Recurrentes\\2_Net_Entreprises__DSN\\5_Depots_Fichiers_DSN\\2_Reels\\" + path_folder)

        time.sleep(5)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(5)

        # Click on the 'Nom du fichier :' bar
        pywinauto.mouse.click(button='left', coords=(x_nom_fichier, y_nom_fichier))

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

        # Click on the 'Cross' button
        pywinauto.mouse.click(button='left', coords=(1345, 700))

        time.sleep(5)

        # Click on the 'Glass hand' button
        pywinauto.mouse.click(button='left', coords=(730, 550))

        time.sleep(5)

        # Click on the "Fireshot" button
        pywinauto.mouse.click(button='left', coords=(x_fireshot, 50))

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
            "A:\\1_Professionnel\\1_Holomorphe\\1_Administration\\2_Gestion_Declarations_Administratives\\1_Recurrentes\\2_Net_Entreprises__DSN\\5_Depots_Fichiers_DSN\\2_Reels\\" + path_folder)

        time.sleep(5)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(5)

        # Click on the 'Nom du fichier :' bar
        pywinauto.mouse.click(button='left', coords=(x_nom_fichier, y_nom_fichier))

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

        # Click on the 'Cross' button
        pywinauto.mouse.click(button='left', coords=(1345, 700))

        time.sleep(5)

        # Click on the 'Afficher les certificats de conformité' button
        pywinauto.mouse.click(button='left', coords=(450, 450))

        time.sleep(5)

        # Click on the 'Screen'
        pywinauto.mouse.click(button='left', coords=(380, 300))

        time.sleep(5)

        # Print
        pywinauto.keyboard.send_keys('^p')

        time.sleep(5)

        # Click on the 'Imprimer' button
        pywinauto.mouse.click(button='left', coords=(150, 420))

        time.sleep(5)

        # Click on the bar to select the folder
        pywinauto.mouse.click(button='left', coords=(380, 50))

        time.sleep(5)

        # Enter the path folder
        pywinauto.keyboard.send_keys(
            "A:\\1_Professionnel\\1_Holomorphe\\1_Administration\\2_Gestion_Declarations_Administratives\\1_Recurrentes\\2_Net_Entreprises__DSN\\5_Depots_Fichiers_DSN\\2_Reels\\" + path_folder)

        time.sleep(5)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(5)

        # Click on the 'Nom du fichier :' bar
        pywinauto.mouse.click(button='left', coords=(x_nom_fichier, y_nom_fichier))

        time.sleep(5)

        # Press the 'Ctrl+A'
        pywinauto.keyboard.send_keys('^a')

        time.sleep(5)

        # Insert the 'Page_3.pdf'
        pywinauto.keyboard.send_keys('Page_3.pdf')

        time.sleep(5)

        # Click on the 'Enregistrer' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(10)

        # Click on the 'Screen'
        # pywinauto.mouse.click(button='left', coords=(500, 350))
        # time.sleep(5)

        # Close the PDF file
        # pywinauto.keyboard.send_keys('%{F4}')
        # time.sleep(5)

        # Click on the 'Screen'
        pywinauto.mouse.click(button='left', coords=(380, 300))

        time.sleep(5)

        # Close the screen
        pywinauto.keyboard.send_keys('%{F4}')

        time.sleep(5)

        # Click on the 'Télécharger les certificats de conformité'
        pywinauto.mouse.click(button='left', coords=(560, 445))

        time.sleep(5)

        # Click on the 'Autres téléchargements'
        pywinauto.mouse.click(button='left', coords=(580, 445))

        time.sleep(5)

        for i in range(31):
            # Click on the 'Telecharger' button
            pywinauto.mouse.click(button='left', coords=(630, 470))

            time.sleep(5)

            # Click on the 'Right arrow' button
            pywinauto.mouse.click(button='left', coords=(570, 470))

            time.sleep(5)

        # Click on the 'Autres téléchargements'
        pywinauto.mouse.click(button='left', coords=(580, 445))

        time.sleep(5)

        # Click on the 'Glass hand' button
        pywinauto.mouse.click(button='left', coords=(760, 470))

        time.sleep(5)

        # Click on the "Fireshot" button
        pywinauto.mouse.click(button='left', coords=(x_fireshot, 50))

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
            "A:\\1_Professionnel\\1_Holomorphe\\1_Administration\\2_Gestion_Declarations_Administratives\\1_Recurrentes\\2_Net_Entreprises__DSN\\5_Depots_Fichiers_DSN\\2_Reels\\" + path_folder)

        time.sleep(5)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(5)

        # Click on the 'Nom du fichier :' bar
        pywinauto.mouse.click(button='left', coords=(x_nom_fichier, y_nom_fichier))

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

        # Click on the 'Cross' button
        pywinauto.mouse.click(button='left', coords=(1345, 700))

        time.sleep(5)

        # Click on the 'Afficher le certificat de conformité de cette déclaration de TEST' button
        pywinauto.mouse.click(button='left', coords=(390, 455))

        time.sleep(5)

        # Click on the Screen of the pop-up
        pywinauto.mouse.click(button='left', coords=(350, 320))

        time.sleep(5)

        # Print
        pywinauto.keyboard.send_keys('^p')

        time.sleep(5)

        # Click on the 'Imprimer' button
        pywinauto.mouse.click(button='left', coords=(150, 300))

        time.sleep(5)

        # Click on the bar to select the folder
        pywinauto.mouse.click(button='left', coords=(380, 50))

        time.sleep(5)

        # Enter the path folder
        pywinauto.keyboard.send_keys(
            "A:\\1_Professionnel\\1_Holomorphe\\1_Administration\\2_Gestion_Declarations_Administratives\\1_Recurrentes\\2_Net_Entreprises__DSN\\5_Depots_Fichiers_DSN\\2_Reels\\" + path_folder)

        time.sleep(5)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(5)

        # Click on the 'Nom du fichier :' bar
        pywinauto.mouse.click(button='left', coords=(x_nom_fichier, y_nom_fichier))

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

        # Click on the Screen of the PDF file
        # pywinauto.mouse.click(button='left', coords=(430, 350))
        # time.sleep(5)

        # Close the PDF file
        # pywinauto.keyboard.send_keys('%{F4}')
        # time.sleep(5)

        # Click on the Screen of the pop-up
        pywinauto.mouse.click(button='left', coords=(350, 320))

        time.sleep(5)

        # Close the Screen of the pop-up
        pywinauto.keyboard.send_keys('%{F4}')

        time.sleep(5)

        # Click on the 'Accéder au bilan de traitement  de Reel' button
        pywinauto.mouse.click(button='left', coords=(420, 605))

        time.sleep(5)

        # Click on the Screen of the pop-up
        pywinauto.mouse.click(button='left', coords=(300, 300))

        time.sleep(5)

        # Print
        pywinauto.keyboard.send_keys('^p')

        time.sleep(5)

        # Click on the 'Imprimer' button
        pywinauto.mouse.click(button='left', coords=(150, 425))

        time.sleep(5)

        # Click on the bar to select the folder
        pywinauto.mouse.click(button='left', coords=(380, 50))

        time.sleep(5)

        # Enter the path folder
        pywinauto.keyboard.send_keys(
            "A:\\1_Professionnel\\1_Holomorphe\\1_Administration\\2_Gestion_Declarations_Administratives\\1_Recurrentes\\2_Net_Entreprises__DSN\\5_Depots_Fichiers_DSN\\2_Reels\\" + path_folder)

        time.sleep(5)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(5)

        # Click on the 'Nom du fichier :' bar
        pywinauto.mouse.click(button='left', coords=(x_nom_fichier, y_nom_fichier))

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

        # Click on the 'Screen'
        # pywinauto.mouse.click(button='left', coords=(500, 350))
        # time.sleep(5)

        # Close the PDF file
        # pywinauto.keyboard.send_keys('%{F4}')
        # time.sleep(5)

        # Click on the Screen of the pop-up
        pywinauto.mouse.click(button='left', coords=(350, 320))

        time.sleep(5)

        # Close the Screen of the pop-up
        pywinauto.keyboard.send_keys('%{F4}')

        time.sleep(5)

        # Click on the 'Screen' button
        pywinauto.mouse.click(button='left', coords=(880, 300))

        time.sleep(5)

        # {DOWN} 10 times
        pywinauto.keyboard.send_keys('{DOWN 2}')

        time.sleep(5)

        # Click on the 'Retour' button
        pywinauto.mouse.click(button='left', coords=(60, 600))

        time.sleep(5)

        # Click on the 'Retour' button
        pywinauto.mouse.click(button='left', coords=(60, 520))

        time.sleep(5)

        # {DOWN} 10 times
        pywinauto.keyboard.send_keys('{DOWN 10}')

        time.sleep(5)

        # Click on the 'Retour' button
        pywinauto.mouse.click(button='left', coords=(65, 695))

        time.sleep(10)

        # Click on the 'Se deconnecter' button
        pywinauto.mouse.click(button='left', coords=(1250, 90))

        time.sleep(10)

        # Click on the 'Ok pour se déconnecter' button
        pywinauto.mouse.click(button='left', coords=(770, 160))

        time.sleep(10)

        # Close the onglet
        pywinauto.keyboard.send_keys('^w')

        time.sleep(5)

        print("run_ccleaner")
        os.system("set ccleaner='C:\\Program Files\\CCleaner\\CCleaner.exe'")
        os.system("start ccleaner /AUTO")


class UnitTestsDesktopAutomationDSNLocal(unittest.TestCase):
    # ok
    def test_se_connecter(self):
        print("test_se_connecter")

        app = Application(backend="uia")

        app.start("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")

        time.sleep(7)

        pywinauto.keyboard.send_keys("https://www.net-entreprises.fr/")

        time.sleep(5)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(10)

        # Click on the "Tout refuser" button
        pywinauto.mouse.click(button='left', coords=(600, 460))

        time.sleep(10)

        # Click on the "Me connecter" button
        pywinauto.mouse.click(button='left', coords=(1200, 110))

        time.sleep(10)

        # Click on the "Siret" input
        pywinauto.mouse.click(button='left', coords=(780, 490))

        time.sleep(10)

        # Insert the Siret
        pywinauto.keyboard.send_keys('')

        time.sleep(10)

        # Click on the "Nom" input
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(5)

        # Insert the Nom
        pywinauto.keyboard.send_keys('')

        time.sleep(5)

        # Click on the "Prénom" input
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(5)

        # Insert the Prénom
        pywinauto.keyboard.send_keys('')

        time.sleep(5)

        # Click on the "Mot de passe" input
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(5)

        # Insert the Mot de passe
        pywinauto.keyboard.send_keys('')

        time.sleep(5)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(5)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(10)

        # Click on the "DSN régime général" button
        pywinauto.mouse.click(button='left', coords=(530, 320))

        time.sleep(5)

        print("run_ccleaner")
        os.system("set ccleaner='C:\\Program Files\\CCleaner\\CCleaner.exe'")
        os.system("start ccleaner /AUTO")

    # ok
    def test_dsn_test_local(self):
        print("test_dsn_test_local")

        folder_path = "3_Annee_2022\\2_Fevrier_Pour_Janvier_2021"

        filename = "dsn_test_holomorphe_fev_2022_pour_janv_2022.dsn"

        time.sleep(5)

        # Click on the "Research" bar of Windows
        pywinauto.mouse.click(button='left', coords=(190, 750))

        time.sleep(5)

        # Insert "dsnval"
        pywinauto.keyboard.send_keys("dsnval")

        time.sleep(5)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(25)

        # Click on the "Folder" icon
        pywinauto.mouse.click(button='left', coords=(20, 40))

        time.sleep(5)

        # Click on the "Parcourrir" button
        pywinauto.mouse.click(button='left', coords=(1100, 300))

        time.sleep(5)

        # Click on the bar folder
        pywinauto.mouse.click(button='left', coords=(370, 70))

        time.sleep(5)

        # Insert the folder path
        pywinauto.keyboard.send_keys("A:\\1_Professionnel\\1_Holomorphe\\1_Administration\\2_Gestion_Declarations_Administratives\\1_Recurrentes\\2_Net_Entreprises__DSN\\5_Depots_Fichiers_DSN\\3_Tests\\" + folder_path)

        time.sleep(5)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(5)

        # Click on the bar file
        pywinauto.mouse.click(button='left', coords=(280, 440))

        time.sleep(5)

        # Insert the folder path
        pywinauto.keyboard.send_keys(filename)

        time.sleep(5)

        # Click on the "Ouvrir" button
        pywinauto.mouse.click(button='left', coords=(510, 470))

        time.sleep(5)

        # Click on the "Finish" button
        pywinauto.mouse.click(button='left', coords=(1000, 420))

        time.sleep(5)

        # Click on the "Settings" button
        pywinauto.mouse.click(button='left', coords=(60, 40))

        time.sleep(10)

        # Press Alt+F4
        pywinauto.keyboard.send_keys('%{F4}')

        time.sleep(5)

        print("run_ccleaner")
        os.system("set ccleaner='C:\\Program Files\\CCleaner\\CCleaner.exe'")
        os.system("start ccleaner /AUTO")

    # ok
    def test_dsn_reel_local(self):
        print("test_dsn_reel_local")

        folder_path = "3_Annee_2022\\1_Janvier_Pour_Decembre_2021"

        filename = "dsn_reel_holomorphe_jan_2022_pour_dec_2021.dsn"

        time.sleep(5)

        # Click on the "Research" bar of Windows
        pywinauto.mouse.click(button='left', coords=(190, 750))

        time.sleep(5)

        # Insert "dsnval"
        pywinauto.keyboard.send_keys("dsnval")

        time.sleep(5)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(30)

        # Click on the "Folder" icon
        pywinauto.mouse.click(button='left', coords=(20, 40))

        time.sleep(5)

        # Click on the "Parcourrir" button
        pywinauto.mouse.click(button='left', coords=(1100, 300))

        time.sleep(5)

        # Click on the bar folder
        pywinauto.mouse.click(button='left', coords=(370, 70))

        time.sleep(5)

        # Insert the folder path
        pywinauto.keyboard.send_keys("A:\\1_Professionnel\\1_Holomorphe\\1_Administration\\2_Gestion_Declarations_Administratives\\1_Recurrentes\\2_Net_Entreprises__DSN\\5_Depots_Fichiers_DSN\\2_Reels\\" + folder_path)

        time.sleep(5)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(5)

        # Click on the bar file
        pywinauto.mouse.click(button='left', coords=(280, 440))

        time.sleep(5)

        # Insert the folder path
        pywinauto.keyboard.send_keys(filename)

        time.sleep(5)

        # Click on the "Ouvrir" button
        pywinauto.mouse.click(button='left', coords=(510, 470))

        time.sleep(5)

        # Click on the "Finish" button
        pywinauto.mouse.click(button='left', coords=(1000, 420))

        time.sleep(5)

        # Click on the "Settings" button
        pywinauto.mouse.click(button='left', coords=(60, 40))

        time.sleep(5)

        # Press Alt+F4
        pywinauto.keyboard.send_keys('%{F4}')

        time.sleep(5)

        print("run_ccleaner")
        os.system("set ccleaner='C:\\Program Files\\CCleaner\\CCleaner.exe'")
        os.system("start ccleaner /AUTO")


if __name__ == '__main__':
    unittest.main()
