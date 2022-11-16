import unittest
import time
from pywinauto.application import Application
import pywinauto.keyboard
import pywinauto.mouse
import pywinauto.base_wrapper
import pywinauto.timings


class UnitTestsDesktopAutomationLeroyMerlin(unittest.TestCase):
    def test_se_connecter(self):
        print("test_se_connecter")

        time.sleep(5)

        app = Application(backend="uia")

        app.start("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")

        time.sleep(5)

        pywinauto.keyboard.send_keys("https://www.leroymerlin.fr/")

        time.sleep(5)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(15)

        # Click on the "continuer sans accepter" button
        pywinauto.mouse.click(button='left', coords=(960, 130))

        time.sleep(10)

        # Click on the "me connecter" button
        pywinauto.mouse.click(button='left', coords=(1150, 150))

        time.sleep(10)

        # Click on the "email" input
        pywinauto.mouse.click(button='left', coords=(560, 460))

        time.sleep(10)

        # Insert the 'email'
        pywinauto.keyboard.send_keys(".@outlook.fr")

        time.sleep(10)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys("{ENTER}")

        time.sleep(10)

        # Insert the 'M_D_P'
        pywinauto.keyboard.send_keys("")

        time.sleep(10)

        # Press the 'ENTER' button
        pywinauto.keyboard.send_keys("{ENTER}")

        time.sleep(10)

    def test_acheter_un_produit(self):
        print("test_acheter_un_produit")

        quantite = "1"

        url_produit = "https://www.leroymerlin.fr/produits/electricite-domotique/rallonge-multiprise-enrouleur-et-cable-electrique/fil-et-cable-electrique-gaine-prefilee-et-cable-internet/fil-et-cable-electrique/fil-electrique-1-5-mm2-h07vu-en-couronne-de-100m-bleu-70398552.html"

        path_folder = "1_Annee_2021\\5_Fil_Electrique_100m_1-5mm2_07_10_2021"

        full_path_folder = "A:\\2_Personnel\\1_Recurrentes\\3_Mes_Achats_En_Ligne\\15_Leroy_Merlin\\2_Mes_Achats\\" + path_folder

        x_capture = 1240

        # visible : 140
        # entier : 120
        y_capture_ecran = 140

        # informations bancaires
        numero_de_la_carte = ""
        code_de_verification_de_la_carte = ""
        date_expiration_mois = 11

        time.sleep(5)

        app = Application(backend="uia")

        app.start("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")

        time.sleep(5)

        pywinauto.keyboard.send_keys(url_produit)

        time.sleep(5)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(15)

        # Click on the "continuer sans accepter" button
        pywinauto.mouse.click(button='left', coords=(960, 130))

        time.sleep(10)

        # Click on the "Fireshot" button
        pywinauto.mouse.click(button='left', coords=(x_capture, 50))

        time.sleep(5)

        # Click on the "Capture page" button
        pywinauto.mouse.click(button='left', coords=(x_capture, y_capture_ecran))

        time.sleep(10)

        # Click on the "Save to PDF" button
        pywinauto.mouse.click(button='left', coords=(1160, 330))

        time.sleep(5)

        # Click on the bar to select the folder
        pywinauto.mouse.click(button='left', coords=(380, 50))

        time.sleep(5)

        # Enter the path folder
        pywinauto.keyboard.send_keys(full_path_folder)

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
        pywinauto.mouse.click(button='left', coords=(700, 10))

        time.sleep(5)

        # Click on the "Prix" title
        pywinauto.mouse.click(button='left', coords=(835, 435))

        time.sleep(10)

        # Click on the "DOWN" in 3 times
        pywinauto.keyboard.send_keys('{DOWN 3}')

        time.sleep(10)

        # Click on the "Quantite" in 1 time
        pywinauto.mouse.click(button='left', coords=(870, 590))

        time.sleep(10)

        # Press the 'Ctrl+A'
        pywinauto.keyboard.send_keys('^a')

        time.sleep(5)

        # Insert the "Quantite"
        pywinauto.keyboard.send_keys(quantite)

        time.sleep(5)

        # Click on the "screen"
        pywinauto.mouse.click(button='left', coords=(1320, 350))

        time.sleep(10)

        # Click on the "Ajouter au panier" button
        pywinauto.mouse.click(button='left', coords=(1100, 590))

        time.sleep(10)

        # Click on the "Fireshot" button
        pywinauto.mouse.click(button='left', coords=(x_capture, 50))

        time.sleep(5)

        # Click on the "Capture page" button
        pywinauto.mouse.click(button='left', coords=(x_capture, y_capture_ecran))

        time.sleep(10)

        # Click on the "Save to PDF" button
        pywinauto.mouse.click(button='left', coords=(1160, 330))

        time.sleep(5)

        # Click on the bar to select the folder
        pywinauto.mouse.click(button='left', coords=(380, 50))

        time.sleep(5)

        # Enter the path folder
        pywinauto.keyboard.send_keys(full_path_folder)

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

        # Click on the "Voir mon panier" button
        pywinauto.mouse.click(button='left', coords=(250, 450))

        time.sleep(5)

        # Click on the "Fireshot" button
        pywinauto.mouse.click(button='left', coords=(x_capture, 50))

        time.sleep(5)

        # Click on the "Capture page" button
        pywinauto.mouse.click(button='left', coords=(x_capture, y_capture_ecran))

        time.sleep(10)

        # Click on the "Save to PDF" button
        pywinauto.mouse.click(button='left', coords=(1160, 330))

        time.sleep(5)

        # Click on the bar to select the folder
        pywinauto.mouse.click(button='left', coords=(380, 50))

        time.sleep(5)

        # Enter the path folder
        pywinauto.keyboard.send_keys(full_path_folder)

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
        pywinauto.mouse.click(button='left', coords=(700, 10))

        time.sleep(5)

        # Click on the "Valider mon panier" button
        pywinauto.mouse.click(button='left', coords=(1100, 530))

        time.sleep(5)

        # Click on the "Fireshot" button
        pywinauto.mouse.click(button='left', coords=(x_capture, 50))

        time.sleep(5)

        # Click on the "Capture page" button
        pywinauto.mouse.click(button='left', coords=(x_capture, y_capture_ecran))

        time.sleep(10)

        # Click on the "Save to PDF" button
        pywinauto.mouse.click(button='left', coords=(1160, 330))

        time.sleep(5)

        # Click on the bar to select the folder
        pywinauto.mouse.click(button='left', coords=(380, 50))

        time.sleep(5)

        # Enter the path folder
        pywinauto.keyboard.send_keys(full_path_folder)

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
        pywinauto.mouse.click(button='left', coords=(700, 10))

        time.sleep(5)

        # Click on the "Livraison en point relais" button
        pywinauto.mouse.click(button='left', coords=(700, 500))

        time.sleep(5)

        # Click on the "Continuer" button
        pywinauto.mouse.click(button='left', coords=(1100, 560))

        time.sleep(5)

        # Click on the "Email" input
        pywinauto.mouse.click(button='left', coords=(600, 400))

        time.sleep(5)

        # Insert the 'email'
        pywinauto.keyboard.send_keys(".@outlook.fr")

        time.sleep(10)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys("{ENTER}")

        time.sleep(10)

        # Insert the 'M_D_P'
        pywinauto.keyboard.send_keys("")

        time.sleep(10)

        # Press the 'ENTER' button
        pywinauto.keyboard.send_keys("{ENTER}")

        time.sleep(10)

        # Click on the "Votre code postal" input
        pywinauto.mouse.click(button='left', coords=(300, 475))

        time.sleep(10)

        # Insert the 'Votre code postal'
        pywinauto.keyboard.send_keys("")

        time.sleep(10)

        # Click on the "OK" button
        pywinauto.mouse.click(button='left', coords=(590, 475))

        time.sleep(10)

        # Click on the screen
        pywinauto.mouse.click(button='left', coords=(700, 450))

        time.sleep(10)

        # Press "DOWN" in 2 times
        pywinauto.keyboard.send_keys("{DOWN 2}")

        time.sleep(10)

        # Click on the "Exo monde relais" checkbox
        pywinauto.mouse.click(button='left', coords=(320, 560))

        time.sleep(10)

        # Click on the "Fireshot" button
        pywinauto.mouse.click(button='left', coords=(x_capture, 50))

        time.sleep(5)

        # Click on the "Capture page" button
        pywinauto.mouse.click(button='left', coords=(x_capture, y_capture_ecran))

        time.sleep(10)

        # Click on the "Save to PDF" button
        pywinauto.mouse.click(button='left', coords=(1160, 330))

        time.sleep(5)

        # Click on the bar to select the folder
        pywinauto.mouse.click(button='left', coords=(380, 50))

        time.sleep(5)

        # Enter the path folder
        pywinauto.keyboard.send_keys(full_path_folder)

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
        pywinauto.mouse.click(button='left', coords=(700, 10))

        time.sleep(5)

        # Click on the "Continuer" button
        pywinauto.mouse.click(button='left', coords=(1140, 400))

        time.sleep(10)

        # Click on the "Carte bancaire" button
        pywinauto.mouse.click(button='left', coords=(140, 330))

        time.sleep(10)

        # Click on the "Fireshot" button
        pywinauto.mouse.click(button='left', coords=(x_capture, 50))

        time.sleep(5)

        # Click on the "Capture page" button
        pywinauto.mouse.click(button='left', coords=(x_capture, y_capture_ecran))

        time.sleep(10)

        # Click on the "Save to PDF" button
        pywinauto.mouse.click(button='left', coords=(1160, 330))

        time.sleep(5)

        # Click on the bar to select the folder
        pywinauto.mouse.click(button='left', coords=(380, 50))

        time.sleep(5)

        # Enter the path folder
        pywinauto.keyboard.send_keys(full_path_folder)

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

        time.sleep(5)

        # Click on the screen
        pywinauto.mouse.click(button='left', coords=(700, 10))

        time.sleep(5)

        # Click on the "Régler" button
        pywinauto.mouse.click(button='left', coords=(540, 540))

        time.sleep(10)

        # Click on the "Titulaire de la carte" button
        pywinauto.mouse.click(button='left', coords=(360, 360))

        time.sleep(10)

        # Insert the "Titulaire de la carte"
        pywinauto.keyboard.send_keys('Mr ')

        time.sleep(10)

        # Press tab button
        pywinauto.keyboard.send_keys('{VK_TAB}')

        time.sleep(10)

        # Insert "Numéro de la carte"
        pywinauto.keyboard.send_keys(numero_de_la_carte)

        time.sleep(10)

        # Press tab button
        pywinauto.keyboard.send_keys('{VK_TAB}')

        time.sleep(10)

        # Press down button to select the date_expiration_mois
        pywinauto.keyboard.send_keys('{DOWN ' + str(date_expiration_mois) + '}')

        time.sleep(10)

        # Press tab button
        pywinauto.keyboard.send_keys('{VK_TAB}')

        time.sleep(10)

        # Press down button to select the date_expiration_annee
        pywinauto.keyboard.send_keys('{DOWN}')

        time.sleep(10)

        # Press tab button
        pywinauto.keyboard.send_keys('{VK_TAB}')

        time.sleep(10)

        # Insert the code de verification de la carte
        pywinauto.keyboard.send_keys(code_de_verification_de_la_carte)

        time.sleep(10)

        # Click on the "Fireshot" button
        pywinauto.mouse.click(button='left', coords=(x_capture, 50))

        time.sleep(5)

        # Click on the "Capture page" button
        pywinauto.mouse.click(button='left', coords=(x_capture, y_capture_ecran))

        time.sleep(10)

        # Click on the "Save to PDF" button
        pywinauto.mouse.click(button='left', coords=(1160, 330))

        time.sleep(5)

        # Click on the bar to select the folder
        pywinauto.mouse.click(button='left', coords=(380, 50))

        time.sleep(5)

        # Enter the path folder
        pywinauto.keyboard.send_keys(full_path_folder)

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
        pywinauto.mouse.click(button='left', coords=(700, 10))

        time.sleep(5)

        # Press tab button
        pywinauto.keyboard.send_keys('{VK_TAB 2}')

        time.sleep(10)

        # Press tab button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(10)


if __name__ == '__main__':
    unittest.main()
