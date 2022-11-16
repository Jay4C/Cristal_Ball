import unittest
import time
from pywinauto.application import Application
import pywinauto.keyboard
import pywinauto.mouse
import pywinauto.base_wrapper
import pywinauto.timings
import os

path_folder = "4_Annee_2022\\5_Juin\\"
url_achat = ""


class UnitTestsDesktopAutomationCdiscount(unittest.TestCase):
    # ok
    def test_acheter_le_meme_article(self):
        print("test_acheter_le_meme_article")

        email = ".@outlook.fr"

        password = ""

        x_ajouter_au_panier = 1200

        y_ajouter_au_panier = 550

        x_capture_ecran = 1240

        # visible : 145
        # entier : 115
        y_capture_ecran = 145

        # Ajouter plusieurs articles
        ajouter_plusieurs = "non"

        nombre_articles = 1

        x_nom_fichier = 260

        y_nom_fichier = 375

        time.sleep(10)

        app = Application(backend="uia")

        app.start("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")

        time.sleep(10)

        # Enter the url
        pywinauto.keyboard.send_keys(url_achat)

        time.sleep(10)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(10)

        # Click on the "Contineur sans accepter" button
        pywinauto.mouse.click(button='left', coords=(1140, 475))

        time.sleep(10)

        # Click on the "Fireshot" button
        pywinauto.mouse.click(button='left', coords=(x_capture_ecran, 50))

        time.sleep(10)

        # Click on the "Capture page" button
        pywinauto.mouse.click(button='left', coords=(x_capture_ecran, y_capture_ecran))

        # time.sleep(10)

        # Move
        pywinauto.mouse.move(coords=(1140, 10))

        time.sleep(20)

        # Click on the "Save to PDF" button
        pywinauto.mouse.click(button='left', coords=(1160, 330))

        time.sleep(10)

        # Click on the bar to select the folder
        pywinauto.mouse.click(button='left', coords=(380, 50))

        time.sleep(10)

        # Enter the path folder
        pywinauto.keyboard.send_keys("A:\\2_Personnel\\1_Recurrentes\\3_Mes_Achats_En_Ligne\\6_CDiscount\\2_Mes_Achats\\" + path_folder)

        time.sleep(10)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(10)

        # Click on the 'Nom du fichier :' bar
        pywinauto.mouse.click(button='left', coords=(x_nom_fichier, y_nom_fichier))

        time.sleep(10)

        # Press the 'Ctrl+A'
        pywinauto.keyboard.send_keys('^a')

        time.sleep(10)

        # Insert the 'Page_1.pdf'
        pywinauto.keyboard.send_keys('Page_1.pdf')

        time.sleep(10)

        # Click on the 'Enregistrer' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(10)

        # Close the onglet
        pywinauto.keyboard.send_keys('^w')

        time.sleep(10)

        # Click on the screen
        pywinauto.mouse.click(button='left', coords=(500, 10))

        time.sleep(10)

        # Click on the 'Ajouter au panier' button
        pywinauto.mouse.click(button='left', coords=(x_ajouter_au_panier, y_ajouter_au_panier))

        time.sleep(10)

        # Click on the "Fireshot" button
        pywinauto.mouse.click(button='left', coords=(x_capture_ecran, 50))

        time.sleep(10)

        # Click on the "Capture page" button
        pywinauto.mouse.click(button='left', coords=(x_capture_ecran, y_capture_ecran))

        # time.sleep(10)

        # Move
        pywinauto.mouse.move(coords=(1140, 10))

        time.sleep(20)

        # Click on the "Save to PDF" button
        pywinauto.mouse.click(button='left', coords=(1160, 330))

        time.sleep(10)

        # Click on the bar to select the folder
        pywinauto.mouse.click(button='left', coords=(380, 50))

        time.sleep(10)

        # Enter the path folder
        pywinauto.keyboard.send_keys("A:\\2_Personnel\\1_Recurrentes\\3_Mes_Achats_En_Ligne\\6_CDiscount\\2_Mes_Achats\\" + path_folder)

        time.sleep(10)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(10)

        # Click on the 'Nom du fichier :' bar
        pywinauto.mouse.click(button='left', coords=(x_nom_fichier, y_nom_fichier))

        time.sleep(10)

        # Press the 'Ctrl+A'
        pywinauto.keyboard.send_keys('^a')

        time.sleep(10)

        # Insert the 'Page_2.pdf'
        pywinauto.keyboard.send_keys('Page_2.pdf')

        time.sleep(10)

        # Click on the 'Enregistrer' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(10)

        # Close the onglet
        pywinauto.keyboard.send_keys('^w')

        time.sleep(10)

        # Click on the screen
        pywinauto.mouse.click(button='left', coords=(500, 10))

        time.sleep(10)

        # Click on the 'Voir mon panier' button
        pywinauto.mouse.click(button='left', coords=(1200, 390))

        time.sleep(10)

        # Click on the "Fireshot" button
        pywinauto.mouse.click(button='left', coords=(x_capture_ecran, 50))

        time.sleep(10)

        # Click on the "Capture page" button
        pywinauto.mouse.click(button='left', coords=(x_capture_ecran, y_capture_ecran))

        # time.sleep(10)

        # Move
        pywinauto.mouse.move(coords=(1140, 10))

        time.sleep(20)

        # Click on the "Save to PDF" button
        pywinauto.mouse.click(button='left', coords=(1160, 330))

        time.sleep(10)

        # Click on the bar to select the folder
        pywinauto.mouse.click(button='left', coords=(380, 50))

        time.sleep(10)

        # Enter the path folder
        pywinauto.keyboard.send_keys("A:\\2_Personnel\\1_Recurrentes\\3_Mes_Achats_En_Ligne\\6_CDiscount\\2_Mes_Achats\\" + path_folder)

        time.sleep(10)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(10)

        # Click on the 'Nom du fichier :' bar
        pywinauto.mouse.click(button='left', coords=(x_nom_fichier, y_nom_fichier))

        time.sleep(10)

        # Press the 'Ctrl+A'
        pywinauto.keyboard.send_keys('^a')

        time.sleep(10)

        # Insert the 'Page_3.pdf'
        pywinauto.keyboard.send_keys('Page_3.pdf')

        time.sleep(10)

        # Click on the 'Enregistrer' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(10)

        # Close the onglet
        pywinauto.keyboard.send_keys('^w')

        time.sleep(10)

        # Click on the screen
        pywinauto.mouse.click(button='left', coords=(500, 10))

        time.sleep(10)

        if ajouter_plusieurs == "oui":
            if nombre_articles == 2:
                # ajouter nb d'articles
                pywinauto.mouse.click(button='left', coords=(940, 410))

                time.sleep(10)

                # {DOWN} many times
                pywinauto.keyboard.send_keys('{DOWN}')

                time.sleep(10)

                # {DOWN} many times
                pywinauto.keyboard.send_keys('{ENTER}')

                time.sleep(10)

                # Click on the "Fireshot" button
                pywinauto.mouse.click(button='left', coords=(x_capture_ecran, 50))

                time.sleep(10)

                # Click on the "Capture page" button
                pywinauto.mouse.click(button='left', coords=(x_capture_ecran, y_capture_ecran))

                # time.sleep(10)

                # Move
                pywinauto.mouse.move(coords=(1140, 10))

                time.sleep(20)

                # Click on the "Save to PDF" button
                pywinauto.mouse.click(button='left', coords=(1160, 330))

                time.sleep(10)

                # Click on the bar to select the folder
                pywinauto.mouse.click(button='left', coords=(380, 50))

                time.sleep(10)

                # Enter the path folder
                pywinauto.keyboard.send_keys(
                    "A:\\2_Personnel\\1_Recurrentes\\3_Mes_Achats_En_Ligne\\6_CDiscount\\2_Mes_Achats\\" + path_folder)

                time.sleep(10)

                # Press the 'Enter' button
                pywinauto.keyboard.send_keys('{ENTER}')

                time.sleep(10)

                # Click on the 'Nom du fichier :' bar
                pywinauto.mouse.click(button='left', coords=(x_nom_fichier, y_nom_fichier))

                time.sleep(10)

                # Press the 'Ctrl+A'
                pywinauto.keyboard.send_keys('^a')

                time.sleep(10)

                # Insert the 'Page_4.pdf'
                pywinauto.keyboard.send_keys('Page_4.pdf')

                time.sleep(10)

                # Click on the 'Enregistrer' button
                pywinauto.keyboard.send_keys('{ENTER}')

                time.sleep(10)

                # Close the onglet
                pywinauto.keyboard.send_keys('^w')

                time.sleep(10)

                # Click on the screen
                pywinauto.mouse.click(button='left', coords=(500, 10))

                time.sleep(10)
            elif nombre_articles > 2:
                # ajouter nb d'articles
                pywinauto.mouse.click(button='left', coords=(940, 410))

                time.sleep(10)

                # {DOWN} many times
                pywinauto.keyboard.send_keys('{DOWN ' + str(nombre_articles-1) + '}')

                time.sleep(10)

                # {DOWN} many times
                pywinauto.keyboard.send_keys('{ENTER}')

                time.sleep(10)

                # Click on the "Fireshot" button
                pywinauto.mouse.click(button='left', coords=(x_capture_ecran, 50))

                time.sleep(10)

                # Click on the "Capture page" button
                pywinauto.mouse.click(button='left', coords=(x_capture_ecran, y_capture_ecran))

                # time.sleep(10)

                # Move
                pywinauto.mouse.move(coords=(1140, 10))

                time.sleep(20)

                # Click on the "Save to PDF" button
                pywinauto.mouse.click(button='left', coords=(1160, 330))

                time.sleep(10)

                # Click on the bar to select the folder
                pywinauto.mouse.click(button='left', coords=(380, 50))

                time.sleep(10)

                # Enter the path folder
                pywinauto.keyboard.send_keys(
                    "A:\\2_Personnel\\1_Recurrentes\\3_Mes_Achats_En_Ligne\\6_CDiscount\\2_Mes_Achats\\" + path_folder)

                time.sleep(10)

                # Press the 'Enter' button
                pywinauto.keyboard.send_keys('{ENTER}')

                time.sleep(10)

                # Click on the 'Nom du fichier :' bar
                pywinauto.mouse.click(button='left', coords=(x_nom_fichier, y_nom_fichier))

                time.sleep(10)

                # Press the 'Ctrl+A'
                pywinauto.keyboard.send_keys('^a')

                time.sleep(10)

                # Insert the 'Page_4.pdf'
                pywinauto.keyboard.send_keys('Page_4.pdf')

                time.sleep(10)

                # Click on the 'Enregistrer' button
                pywinauto.keyboard.send_keys('{ENTER}')

                time.sleep(10)

                # Close the onglet
                pywinauto.keyboard.send_keys('^w')

                time.sleep(10)

                # Click on the screen
                pywinauto.mouse.click(button='left', coords=(500, 10))

                time.sleep(10)

        # Click on the 'Choisir ma livraison' button
        pywinauto.mouse.click(button='left', coords=(1200, 330))

        time.sleep(10)

        # Click on the 'Email' input
        pywinauto.mouse.click(button='left', coords=(540, 240))

        time.sleep(10)

        # Insert the 'Email'
        pywinauto.keyboard.send_keys(email)

        time.sleep(10)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(10)

        # Insert the 'M_D_P'
        pywinauto.keyboard.send_keys(password)

        time.sleep(10)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(10)

        # Click on the "Fireshot" button
        pywinauto.mouse.click(button='left', coords=(x_capture_ecran, 50))

        time.sleep(10)

        # Click on the "Capture page" button
        pywinauto.mouse.click(button='left', coords=(x_capture_ecran, y_capture_ecran))

        # time.sleep(10)

        # Move
        pywinauto.mouse.move(coords=(1140, 10))

        time.sleep(20)

        # Click on the "Save to PDF" button
        pywinauto.mouse.click(button='left', coords=(1160, 330))

        time.sleep(10)

        # Click on the bar to select the folder
        pywinauto.mouse.click(button='left', coords=(380, 50))

        time.sleep(10)

        # Enter the path folder
        pywinauto.keyboard.send_keys("A:\\2_Personnel\\1_Recurrentes\\3_Mes_Achats_En_Ligne\\6_CDiscount\\2_Mes_Achats\\" + path_folder)

        time.sleep(10)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(10)

        # Click on the 'Nom du fichier :' bar
        pywinauto.mouse.click(button='left', coords=(x_nom_fichier, y_nom_fichier))

        time.sleep(10)

        # Press the 'Ctrl+A'
        pywinauto.keyboard.send_keys('^a')

        time.sleep(10)

        # Insert the 'Page_5.pdf'
        pywinauto.keyboard.send_keys('Page_5.pdf')

        time.sleep(10)

        # Click on the 'Enregistrer' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(10)

        # Close the onglet
        pywinauto.keyboard.send_keys('^w')

        time.sleep(10)

        # Click on the screen
        pywinauto.mouse.click(button='left', coords=(500, 10))

        time.sleep(10)

        print("ccleaner running")
        os.system("set ccleaner='C:\\Program Files\\CCleaner\\CCleaner.exe'")
        os.system("start ccleaner /AUTO")

        time.sleep(10)

    # ok
    def test_acheter_le_meme_vetement(self):
        print("test_acheter_le_meme_article")

        x_capture_ecran = 1100

        y_capture_ecran = 135

        x_ajouter_panier = 1200

        y_ajouter_panier = 555

        path_folder = ""

        app = Application(backend="uia")

        app.start("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")

        time.sleep(6)

        # Enter the url
        pywinauto.keyboard.send_keys("")

        time.sleep(3)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(5)

        # Click on the "Contineur sans accepter" button
        pywinauto.mouse.click(button='left', coords=(1140, 495))

        time.sleep(5)

        # Click on the "Fireshot" button
        pywinauto.mouse.click(button='left', coords=(x_capture_ecran, 50))

        time.sleep(5)

        # Click on the "Capture page" button
        pywinauto.mouse.click(button='left', coords=(x_capture_ecran, y_capture_ecran))

        # time.sleep(10)

        # Move
        pywinauto.mouse.move(coords=(1140, 10))

        time.sleep(20)

        # Click on the "Save to PDF" button
        pywinauto.mouse.click(button='left', coords=(1160, 330))

        time.sleep(5)

        # Click on the bar to select the folder
        pywinauto.mouse.click(button='left', coords=(380, 50))

        time.sleep(5)

        # Enter the path folder
        pywinauto.keyboard.send_keys("A:\\2_Personnel\\1_Recurrentes\\3_Mes_Achats_En_Ligne\\6_CDiscount\\2_Mes_Achats\\" + path_folder)

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
        pywinauto.mouse.click(button='left', coords=(500, 10))

        time.sleep(5)

        # Click on the 'Choisir sa taille' button
        pywinauto.mouse.click(button='left', coords=(570, 680))

        time.sleep(5)

        # {DOWN} 2 times
        pywinauto.keyboard.send_keys('{DOWN 2}')

        time.sleep(5)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(10)

        # Click on the 'Ajouter au panier' button
        pywinauto.mouse.click(button='left', coords=(x_ajouter_panier, y_ajouter_panier))

        time.sleep(10)

        # Click on the "Fireshot" button
        pywinauto.mouse.click(button='left', coords=(x_capture_ecran, 50))

        time.sleep(5)

        # Click on the "Capture page" button
        pywinauto.mouse.click(button='left', coords=(x_capture_ecran, y_capture_ecran))

        # Move
        pywinauto.mouse.move(coords=(1140, 10))

        time.sleep(20)

        # Click on the "Save to PDF" button
        pywinauto.mouse.click(button='left', coords=(1160, 330))

        time.sleep(5)

        # Click on the bar to select the folder
        pywinauto.mouse.click(button='left', coords=(380, 50))

        time.sleep(5)

        # Enter the path folder
        pywinauto.keyboard.send_keys("A:\\2_Personnel\\1_Recurrentes\\3_Mes_Achats_En_Ligne\\6_CDiscount\\2_Mes_Achats\\" + path_folder)

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
        pywinauto.mouse.click(button='left', coords=(500, 10))

        time.sleep(5)

        # Click on the 'Voir mon panier' button
        pywinauto.mouse.click(button='left', coords=(1200, 390))

        time.sleep(10)

        # Click on the "Fireshot" button
        pywinauto.mouse.click(button='left', coords=(x_capture_ecran, 50))

        time.sleep(5)

        # Click on the "Capture page" button
        pywinauto.mouse.click(button='left', coords=(x_capture_ecran, y_capture_ecran))

        # Move
        pywinauto.mouse.move(coords=(1140, 10))

        time.sleep(20)

        # Click on the "Save to PDF" button
        pywinauto.mouse.click(button='left', coords=(1160, 330))

        time.sleep(5)

        # Click on the bar to select the folder
        pywinauto.mouse.click(button='left', coords=(380, 50))

        time.sleep(5)

        # Enter the path folder
        pywinauto.keyboard.send_keys("A:\\2_Personnel\\1_Recurrentes\\3_Mes_Achats_En_Ligne\\6_CDiscount\\2_Mes_Achats\\" + path_folder)

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

        time.sleep(10)

        # Click on the screen
        pywinauto.mouse.click(button='left', coords=(500, 10))

        time.sleep(5)

        # Ajouter plusieurs
        ajouter_plusieurs = "non"

        if ajouter_plusieurs == "oui":
            # ajouter nb d'articles = 5
            pywinauto.mouse.click(button='left', coords=(940, 410))

            time.sleep(5)

            pywinauto.mouse.click(button='left', coords=(940, 505))

            time.sleep(5)

            # Click on the "Fireshot" button
            pywinauto.mouse.click(button='left', coords=(x_capture_ecran, 50))

            time.sleep(5)

            # Click on the "Capture page" button
            pywinauto.mouse.click(button='left', coords=(x_capture_ecran, y_capture_ecran))

            # Move
            pywinauto.mouse.move(coords=(1140, 10))

            time.sleep(20)

            # Click on the "Save to PDF" button
            pywinauto.mouse.click(button='left', coords=(1160, 330))

            time.sleep(5)

            # Click on the bar to select the folder
            pywinauto.mouse.click(button='left', coords=(380, 50))

            time.sleep(5)

            # Enter the path folder
            pywinauto.keyboard.send_keys(
                "A:\\2_Personnel\\1_Recurrentes\\3_Mes_Achats_En_Ligne\\6_CDiscount\\2_Mes_Achats\\" + path_folder)

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

            time.sleep(10)

            # Click on the screen
            pywinauto.mouse.click(button='left', coords=(500, 10))

            time.sleep(5)

        time.sleep(5)

        # Click on the 'Choisir ma livraison' button
        pywinauto.mouse.click(button='left', coords=(1200, 330))

        time.sleep(5)

        # Click on the 'Email' input
        pywinauto.mouse.click(button='left', coords=(540, 240))

        time.sleep(5)

        # Insert the 'Email'
        pywinauto.keyboard.send_keys(".@outlook.fr")

        time.sleep(5)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(5)

        # Insert the 'M_D_P'
        pywinauto.keyboard.send_keys("")

        time.sleep(7)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(10)

        # Click on the "Fireshot" button
        pywinauto.mouse.click(button='left', coords=(x_capture_ecran, 50))

        time.sleep(5)

        # Click on the "Capture page" button
        pywinauto.mouse.click(button='left', coords=(x_capture_ecran, y_capture_ecran))

        # Move
        pywinauto.mouse.move(coords=(1140, 10))

        time.sleep(20)

        # Click on the "Save to PDF" button
        pywinauto.mouse.click(button='left', coords=(1160, 330))

        time.sleep(5)

        # Click on the bar to select the folder
        pywinauto.mouse.click(button='left', coords=(380, 50))

        time.sleep(5)

        # Enter the path folder
        pywinauto.keyboard.send_keys("A:\\2_Personnel\\1_Recurrentes\\3_Mes_Achats_En_Ligne\\6_CDiscount\\2_Mes_Achats\\" + path_folder)

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

        time.sleep(10)

        # Click on the screen
        pywinauto.mouse.click(button='left', coords=(500, 10))

        time.sleep(5)

        # Click on the 'Choisir - Gratuit' button
        pywinauto.mouse.click(button='left', coords=(1250, 420))

        time.sleep(5)

        # Click on the "Fireshot" button
        pywinauto.mouse.click(button='left', coords=(x_capture_ecran, 50))

        time.sleep(5)

        # Click on the "Capture page" button
        pywinauto.mouse.click(button='left', coords=(x_capture_ecran, y_capture_ecran))

        # Move
        pywinauto.mouse.move(coords=(1140, 10))

        time.sleep(20)

        # Click on the "Save to PDF" button
        pywinauto.mouse.click(button='left', coords=(1160, 330))

        time.sleep(5)

        # Click on the bar to select the folder
        pywinauto.mouse.click(button='left', coords=(380, 50))

        time.sleep(5)

        # Enter the path folder
        pywinauto.keyboard.send_keys("A:\\2_Personnel\\1_Recurrentes\\3_Mes_Achats_En_Ligne\\6_CDiscount\\2_Mes_Achats\\" + path_folder)

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

        # Close the onglet
        pywinauto.keyboard.send_keys('^w')

        time.sleep(10)

        # Click on the screen
        pywinauto.mouse.click(button='left', coords=(500, 10))

        time.sleep(5)

        # Click on the 'Choisir - Par cate bancaire' button
        pywinauto.mouse.click(button='left', coords=(940, 550))

        time.sleep(5)

        print("ccleaner running")
        os.system("set ccleaner='C:\\Program Files\\CCleaner\\CCleaner.exe'")
        os.system("start ccleaner /AUTO")

        time.sleep(5)

    # ok
    def test_se_connecter(self):
        print("test_se_connecter")

        time.sleep(5)

        url_connection = "https://order.cdiscount.com/Account/LoginLight.html?referrer="

        app = Application(backend="uia")

        app.start("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")

        time.sleep(10)

        # Enter the url
        pywinauto.keyboard.send_keys(url_connection)

        time.sleep(5)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(10)

        # Click on the "Contineur sans accepter" button
        pywinauto.mouse.click(button='left', coords=(1140, 475))

        time.sleep(10)

        # Click on the 'Email' input
        pywinauto.mouse.click(button='left', coords=(600, 250))

        time.sleep(5)

        # Insert the 'Email'
        pywinauto.keyboard.send_keys("")

        time.sleep(5)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(5)

        # Insert the 'M_D_P'
        pywinauto.keyboard.send_keys("")

        time.sleep(5)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(5)


if __name__ == '__main__':
    unittest.main()
