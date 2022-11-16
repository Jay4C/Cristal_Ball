import unittest
import time
from pywinauto.application import Application
import pywinauto.keyboard
import pywinauto.mouse
import pywinauto.base_wrapper
import pywinauto.timings
import os


class UnitTestsDesktopAutomationMonoprixADomicile(unittest.TestCase):
    # ok
    def test_faire_les_courses(self):
        print("test_faire_les_courses")

        path_folder = ""

        x_bar_fichier = 370

        y_bar_fichier = 50

        x_capture_visible_page = 1240

        y_capture_visble_page = 145

        x_fireshot_button = 1240

        y_fireshot_button = 50

        y_nom_fichier = 375

        x_nom_fichier = y_nom_fichier

        time.sleep(6)

        app = Application(backend="uia")

        app.start("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")

        time.sleep(6)

        pywinauto.keyboard.send_keys("https://www.monoprix.fr/lh/login")

        time.sleep(3)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(15)

        # Click on the "Continuer sans accepter" button
        pywinauto.mouse.click(button='left', coords=(935, 170))

        time.sleep(5)

        # Click on the "Email" input
        pywinauto.mouse.click(button='left', coords=(310, 450))

        time.sleep(5)

        # Insert the 'Email' value
        pywinauto.keyboard.send_keys('.@outlook.fr')

        time.sleep(3)

        # Press the 'VK_TAB'
        pywinauto.keyboard.send_keys('{VK_TAB}')

        time.sleep(3)

        # Press the 'Password' value
        pywinauto.keyboard.send_keys('')

        time.sleep(3)

        # Press the 'VK_TAB'
        pywinauto.keyboard.send_keys('{VK_TAB}')

        time.sleep(3)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(15)

        # Click on the "J'y vais" button
        pywinauto.mouse.click(button='left', coords=(1070, 85))

        time.sleep(15)

        # Click on the "Fireshot" button
        pywinauto.mouse.click(button='left', coords=(x_fireshot_button, y_fireshot_button))

        time.sleep(5)

        # Click on the "Capture page" button
        pywinauto.mouse.click(button='left', coords=(x_capture_visible_page, y_capture_visble_page))

        time.sleep(10)

        # Click on the "Save to PDF" button
        pywinauto.mouse.click(button='left', coords=(1160, 330))

        time.sleep(5)

        # Click on the bar to select the folder
        pywinauto.mouse.click(button='left', coords=(x_bar_fichier, y_bar_fichier))

        time.sleep(5)

        # Enter the path folder
        pywinauto.keyboard.send_keys(
            "A:\\2_Personnel\\1_Recurrentes\\3_Mes_Achats_En_Ligne\\10_Monoprix_A_Domicile\\2_Courses\\" + path_folder)

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

        # Click on the screen
        pywinauto.mouse.click(button='left', coords=(500, 10))

        time.sleep(5)

        # Click on the "Sélectionner un créneau de livraison" button
        pywinauto.mouse.click(button='left', coords=(1140, 140))

        time.sleep(5)

        # Click on the "Fireshot" button
        pywinauto.mouse.click(button='left', coords=(x_fireshot_button, y_fireshot_button))

        time.sleep(5)

        # Click on the "Capture page" button
        pywinauto.mouse.click(button='left', coords=(x_capture_visible_page, y_capture_visble_page))

        time.sleep(10)

        # Click on the "Save to PDF" button
        pywinauto.mouse.click(button='left', coords=(1160, 330))

        time.sleep(5)

        # Click on the bar to select the folder
        pywinauto.mouse.click(button='left', coords=(x_bar_fichier, y_bar_fichier))

        time.sleep(5)

        # Enter the path folder
        pywinauto.keyboard.send_keys(
            "A:\\2_Personnel\\1_Recurrentes\\3_Mes_Achats_En_Ligne\\10_Monoprix_A_Domicile\\2_Courses\\" + path_folder)

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

        # Click on the screen
        pywinauto.mouse.click(button='left', coords=(500, 10))

        time.sleep(5)

        # Click on the "Livraison à domicile - Sélectionner" button
        pywinauto.mouse.click(button='left', coords=(440, 440))

        time.sleep(5)

        # Click on the "Fireshot" button
        pywinauto.mouse.click(button='left', coords=(x_fireshot_button, y_fireshot_button))

        time.sleep(5)

        # Click on the "Capture page" button
        pywinauto.mouse.click(button='left', coords=(x_capture_visible_page, y_capture_visble_page))

        time.sleep(10)

        # Click on the "Save to PDF" button
        pywinauto.mouse.click(button='left', coords=(1160, 330))

        time.sleep(5)

        # Click on the bar to select the folder
        pywinauto.mouse.click(button='left', coords=(x_bar_fichier, y_bar_fichier))

        time.sleep(5)

        # Enter the path folder
        pywinauto.keyboard.send_keys(
            "A:\\2_Personnel\\1_Recurrentes\\3_Mes_Achats_En_Ligne\\10_Monoprix_A_Domicile\\2_Courses\\" + path_folder)

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

        time.sleep(5)

        # Close the onglet
        pywinauto.keyboard.send_keys('^w')

        time.sleep(5)

        # Click on the screen
        pywinauto.mouse.click(button='left', coords=(500, 10))

        time.sleep(5)

        # Press the "DOWN" button in 3 times
        pywinauto.keyboard.send_keys('{DOWN 3}')

        time.sleep(5)

        # Click on the 'GRATUIT' button
        pywinauto.mouse.click(button='left', coords=(1035, 445))

        time.sleep(5)

        # Click on the "Fireshot" button
        pywinauto.mouse.click(button='left', coords=(x_fireshot_button, y_fireshot_button))

        time.sleep(5)

        # Click on the "Capture page" button
        pywinauto.mouse.click(button='left', coords=(x_capture_visible_page, y_capture_visble_page))

        time.sleep(10)

        # Click on the "Save to PDF" button
        pywinauto.mouse.click(button='left', coords=(1160, 330))

        time.sleep(5)

        # Click on the bar to select the folder
        pywinauto.mouse.click(button='left', coords=(x_bar_fichier, y_bar_fichier))

        time.sleep(5)

        # Enter the path folder
        pywinauto.keyboard.send_keys(
            "A:\\2_Personnel\\1_Recurrentes\\3_Mes_Achats_En_Ligne\\10_Monoprix_A_Domicile\\2_Courses\\" + path_folder)

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

        # Click on the screen
        pywinauto.mouse.click(button='left', coords=(500, 10))

        time.sleep(5)

        # Click on the 'Continuer' button
        pywinauto.mouse.click(button='left', coords=(785, 550))

        time.sleep(5)

        # Click on the "Fireshot" button
        pywinauto.mouse.click(button='left', coords=(x_fireshot_button, y_fireshot_button))

        time.sleep(5)

        # Click on the "Capture page" button
        pywinauto.mouse.click(button='left', coords=(x_capture_visible_page, y_capture_visble_page))

        time.sleep(10)

        # Click on the "Save to PDF" button
        pywinauto.mouse.click(button='left', coords=(1160, 330))

        time.sleep(5)

        # Click on the bar to select the folder
        pywinauto.mouse.click(button='left', coords=(x_bar_fichier, y_bar_fichier))

        time.sleep(5)

        # Enter the path folder
        pywinauto.keyboard.send_keys(
            "A:\\2_Personnel\\1_Recurrentes\\3_Mes_Achats_En_Ligne\\10_Monoprix_A_Domicile\\2_Courses\\" + path_folder)

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

        # Close the onglet
        pywinauto.keyboard.send_keys('^w')

        time.sleep(5)

        # Click on the screen
        pywinauto.mouse.click(button='left', coords=(500, 10))

        time.sleep(5)

        # Click on the 'Liste de courses' button
        pywinauto.mouse.click(button='left', coords=(340, 190))

        time.sleep(5)

        # Click on the "Fireshot" button
        pywinauto.mouse.click(button='left', coords=(x_fireshot_button, y_fireshot_button))

        time.sleep(5)

        # Click on the "Capture page" button
        pywinauto.mouse.click(button='left', coords=(x_capture_visible_page, y_capture_visble_page))

        time.sleep(10)

        # Click on the "Save to PDF" button
        pywinauto.mouse.click(button='left', coords=(1160, 330))

        time.sleep(5)

        # Click on the bar to select the folder
        pywinauto.mouse.click(button='left', coords=(x_bar_fichier, y_bar_fichier))

        time.sleep(5)

        # Enter the path folder
        pywinauto.keyboard.send_keys(
            "A:\\2_Personnel\\1_Recurrentes\\3_Mes_Achats_En_Ligne\\10_Monoprix_A_Domicile\\2_Courses\\" + path_folder)

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

        # Close the onglet
        pywinauto.keyboard.send_keys('^w')

        time.sleep(5)

        # Click on the screen
        pywinauto.mouse.click(button='left', coords=(500, 10))

        time.sleep(5)

        # Click on the 'Ajouter tout' button
        pywinauto.mouse.click(button='left', coords=(750, 470))

        time.sleep(25)

        # Press the "DOWN" in 2 times
        pywinauto.keyboard.send_keys('{DOWN 2}')

        time.sleep(5)

        # Click on the 'Monoprix Eau de source 5l' input
        pywinauto.mouse.click(button='left', coords=(700, 560))

        time.sleep(5)

        # Insert the "Monoprix Eau de source 5l" value
        pywinauto.keyboard.send_keys('10')

        time.sleep(5)

        # Press the "ENTER"
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(5)

        # Click on the 'Pomme de terre' input
        pywinauto.mouse.click(button='left', coords=(100, 560))

        time.sleep(3)

        # Insert the "Pomme de terre" value
        pywinauto.keyboard.send_keys('10')

        time.sleep(5)

        # Press the "ENTER"
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(5)

        # Click on the 'Carotte' input
        pywinauto.mouse.click(button='left', coords=(300, 560))

        time.sleep(3)

        # Insert the "Carotte" value
        pywinauto.keyboard.send_keys('7')

        time.sleep(5)

        # Press the "ENTER"
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(5)

        # Click on the 'Liquide vaisselle' input
        pywinauto.mouse.click(button='left', coords=(500, 560))

        time.sleep(3)

        # Insert the "Liquide vaisselle" value
        pywinauto.keyboard.send_keys('0')

        time.sleep(5)

        # Press the "ENTER"
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(5)

        # Click on the "Fireshot" button
        pywinauto.mouse.click(button='left', coords=(x_fireshot_button, y_fireshot_button))

        time.sleep(5)

        # Click on the "Capture page" button
        pywinauto.mouse.click(button='left', coords=(x_capture_visible_page, y_capture_visble_page))

        time.sleep(10)

        # Click on the "Save to PDF" button
        pywinauto.mouse.click(button='left', coords=(1160, 330))

        time.sleep(5)

        # Click on the bar to select the folder
        pywinauto.mouse.click(button='left', coords=(x_bar_fichier, y_bar_fichier))

        time.sleep(5)

        # Enter the path folder
        pywinauto.keyboard.send_keys(
            "A:\\2_Personnel\\1_Recurrentes\\3_Mes_Achats_En_Ligne\\10_Monoprix_A_Domicile\\2_Courses\\" + path_folder)

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
        pywinauto.mouse.click(button='left', coords=(500, 10))

        time.sleep(5)

        # Click on the 'Aller au paiement' button
        pywinauto.mouse.click(button='left', coords=(1180, 410))

        time.sleep(20)

        # Click on the 'Poursuivre la commande' button
        pywinauto.mouse.click(button='left', coords=(1240, 690))

        time.sleep(5)

        # Click on the 'Poursuivre la commande' button
        pywinauto.mouse.click(button='left', coords=(1240, 690))

        time.sleep(5)

        # Click on the "Fireshot" button
        pywinauto.mouse.click(button='left', coords=(x_fireshot_button, y_fireshot_button))

        time.sleep(5)

        # Click on the "Capture page" button
        pywinauto.mouse.click(button='left', coords=(x_capture_visible_page, y_capture_visble_page))

        time.sleep(10)

        # Click on the "Save to PDF" button
        pywinauto.mouse.click(button='left', coords=(1160, 330))

        time.sleep(5)

        # Click on the bar to select the folder
        pywinauto.mouse.click(button='left', coords=(x_bar_fichier, y_bar_fichier))

        time.sleep(5)

        # Enter the path folder
        pywinauto.keyboard.send_keys(
            "A:\\2_Personnel\\1_Recurrentes\\3_Mes_Achats_En_Ligne\\10_Monoprix_A_Domicile\\2_Courses\\" + path_folder)

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

        # Insert the 'Page_8.pdf'
        pywinauto.keyboard.send_keys('Page_8.pdf')

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

        # Click on the 'En passant cette commande vous acceptez nos Conditions générales de vente' checkbox
        pywinauto.mouse.click(button='left', coords=(220, 280))

        time.sleep(5)

        print("ccleaner running")
        os.system("set ccleaner='C:\\Program Files\\CCleaner\\CCleaner.exe'")
        os.system("start ccleaner /AUTO")

        time.sleep(5)


if __name__ == '__main__':
    unittest.main()
