import unittest
import time
from pywinauto.application import Application
import pywinauto.keyboard
import pywinauto.mouse
import pywinauto.base_wrapper
import pywinauto.timings
import os


class UnitTestsDesktopAutomationInfogreffe(unittest.TestCase):
    def test_declarer_comptes_sociaux_holomorphe(self):
        print("test_declarer_comptes_sociaux_holomorphe")

        path_folder = "1_Exercice_01_04_2020__31_12_2020"

        time.sleep(7)

        app = Application(backend="uia")

        app.start("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")

        time.sleep(7)

        pywinauto.keyboard.send_keys("https://www.infogreffe.fr/formalites-entreprise/depot-des-comptes.html")

        time.sleep(7)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(7)

        # Click on the "Refuser tout" button
        pywinauto.mouse.click(button='left', coords=(720, 500))

        time.sleep(7)

        # Click on the screen
        pywinauto.mouse.click(button='left', coords=(700, 500))

        time.sleep(7)

        # Press the 'Down' button in 7 times
        pywinauto.keyboard.send_keys('{DOWN 7}')

        time.sleep(7)

        # Click on the "Fireshot" button
        pywinauto.mouse.click(button='left', coords=(1140, 50))

        time.sleep(7)

        # Click on the "Capture entire page" button
        pywinauto.mouse.click(button='left', coords=(1020, 110))

        time.sleep(10)

        # Click on the "Save to PDF" button
        pywinauto.mouse.click(button='left', coords=(1160, 330))

        time.sleep(7)

        # Click on the bar to select the folder
        pywinauto.mouse.click(button='left', coords=(380, 50))

        time.sleep(7)

        # Enter the path folder
        pywinauto.keyboard.send_keys("A:\\1_Professionnel\\1_Holomorphe\\1_Administration\\2_Gestion_Declarations_Administratives\\1_Recurrentes\\5_Infogreffe\\4_Approbation_Comptes_Sociaux\\" + path_folder + "\\Screenshot")

        time.sleep(7)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(7)

        # Click on the 'Nom du fichier :' bar
        pywinauto.mouse.click(button='left', coords=(260, 375))

        time.sleep(7)

        # Press the 'Ctrl+A'
        pywinauto.keyboard.send_keys('^a')

        time.sleep(7)

        # Insert the 'Page_1.pdf'
        pywinauto.keyboard.send_keys('Page_1.pdf')

        time.sleep(7)

        # Click on the 'Enregistrer' button
        pywinauto.mouse.click(button='left', coords=(510, 445))

        time.sleep(7)

        # Close the onglet
        pywinauto.keyboard.send_keys('^w')

        time.sleep(7)

        # Click on the screen
        pywinauto.mouse.click(button='left', coords=(500, 10))

        time.sleep(7)

        # Click on the 'Déposer des comptes' button
        pywinauto.mouse.click(button='left', coords=(760, 350))

        time.sleep(7)

        # Click on the screen
        pywinauto.mouse.click(button='left', coords=(680, 450))

        time.sleep(7)

        # Press the 'Down' button in 3 times
        pywinauto.keyboard.send_keys('{DOWN 3}')

        time.sleep(7)

        # Click on the 'Identifiant' input
        pywinauto.mouse.click(button='left', coords=(360, 355))

        time.sleep(7)

        # Insert on the "Identifiant"
        pywinauto.keyboard.send_keys(".@outlook.fr")

        time.sleep(7)

        # Press on the "Tab" button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(7)

        # Insert on the "Mot de passe"
        pywinauto.keyboard.send_keys("")

        time.sleep(7)

        # Click on the 'Valider' button
        pywinauto.mouse.click(button='left', coords=(425, 470))

        time.sleep(10)

        # Click on the 'Numéro d'identification de l'entreprise (n° SIREN)' input
        pywinauto.mouse.click(button='left', coords=(610, 525))

        time.sleep(7)

        # Insert the "Numéro d'identification de l'entreprise (n° SIREN)"
        pywinauto.keyboard.send_keys("")

        time.sleep(7)

        # Click on the 'Rechercher' button
        pywinauto.mouse.click(button='left', coords=(1030, 530))

        time.sleep(7)

        # Press the 'Down' button in 5 times
        pywinauto.keyboard.send_keys('{DOWN 5}')

        time.sleep(7)

        # Click on the "Fireshot" button
        pywinauto.mouse.click(button='left', coords=(1140, 50))

        time.sleep(7)

        # Click on the "Capture entire page" button
        pywinauto.mouse.click(button='left', coords=(1020, 110))

        time.sleep(10)

        # Click on the "Save to PDF" button
        pywinauto.mouse.click(button='left', coords=(1160, 330))

        time.sleep(7)

        # Click on the bar to select the folder
        pywinauto.mouse.click(button='left', coords=(380, 50))

        time.sleep(7)

        # Enter the path folder
        pywinauto.keyboard.send_keys(
            "A:\\1_Professionnel\\1_Holomorphe\\1_Administration\\2_Gestion_Declarations_Administratives\\1_Recurrentes\\5_Infogreffe\\4_Approbation_Comptes_Sociaux\\" + path_folder + "\\Screenshot")

        time.sleep(7)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(7)

        # Click on the 'Nom du fichier :' bar
        pywinauto.mouse.click(button='left', coords=(260, 375))

        time.sleep(7)

        # Press the 'Ctrl+A'
        pywinauto.keyboard.send_keys('^a')

        time.sleep(7)

        # Insert the 'Page_2.pdf'
        pywinauto.keyboard.send_keys('Page_2.pdf')

        time.sleep(7)

        # Click on the 'Enregistrer' button
        pywinauto.mouse.click(button='left', coords=(510, 445))

        time.sleep(7)

        # Close the onglet
        pywinauto.keyboard.send_keys('^w')

        time.sleep(7)

        # Click on the screen
        pywinauto.mouse.click(button='left', coords=(500, 10))

        time.sleep(7)

        # Click on the 'Etape suivante' button
        pywinauto.mouse.click(button='left', coords=(1060, 560))

        time.sleep(7)

        # Click on the 'Votre référence' input
        pywinauto.mouse.click(button='left', coords=(690, 480))

        time.sleep(7)

        # Insert the 'Votre référence'
        pywinauto.keyboard.send_keys('Holomorphe2020')

        time.sleep(7)

        # Click on the 'Exercice du' input
        pywinauto.mouse.click(button='left', coords=(380, 680))

        time.sleep(7)

        # Insert the 'Exercice du'
        pywinauto.keyboard.send_keys('01/04/2020')

        time.sleep(7)

        # Click on the 'Au' input
        pywinauto.mouse.click(button='left', coords=(570, 680))

        time.sleep(7)

        # Insert the 'Au'
        pywinauto.keyboard.send_keys('31/12/2020')

        time.sleep(7)

        # Click on the screen
        pywinauto.mouse.click(button='left', coords=(860, 680))

        time.sleep(7)

        # Press the 'Down' button in 6 times
        pywinauto.keyboard.send_keys('{DOWN 6}')

        time.sleep(7)

        # Click on the 'L'associé unique, personne physique, est le président' checkbox
        pywinauto.mouse.click(button='left', coords=(280, 235))

        time.sleep(7)

        # Click on the 'Je déclare, en application de l'article L.123-16-1 du code de commerce,
        # ne pas être tenu d'établir une annexe' checkbox
        pywinauto.mouse.click(button='left', coords=(280, 270))

        time.sleep(7)

        # Click on the 'Je certifie avoir pris connaissance des conditions de dépôt des comptes
        # dématérialisés et accepte les termes de cet accord *' checkbox
        pywinauto.mouse.click(button='left', coords=(280, 340))

        time.sleep(7)

        # Click on the 'Option exercée en application de l'article L.232-25 du code de commerce :' checkbox
        pywinauto.mouse.click(button='left', coords=(280, 305))

        time.sleep(7)

        # Click on the 'Comptes déposés non rendus publics. Visualiser les conditions' checkbox
        pywinauto.mouse.click(button='left', coords=(295, 330))

        time.sleep(7)

        # Click on the "Fireshot" button
        pywinauto.mouse.click(button='left', coords=(1140, 50))

        time.sleep(7)

        # Click on the "Capture entire page" button
        pywinauto.mouse.click(button='left', coords=(1020, 110))

        time.sleep(10)

        # Click on the "Save to PDF" button
        pywinauto.mouse.click(button='left', coords=(1160, 330))

        time.sleep(7)

        # Click on the bar to select the folder
        pywinauto.mouse.click(button='left', coords=(380, 50))

        time.sleep(7)

        # Enter the path folder
        pywinauto.keyboard.send_keys(
            "A:\\1_Professionnel\\1_Holomorphe\\1_Administration\\2_Gestion_Declarations_Administratives\\1_Recurrentes\\5_Infogreffe\\4_Approbation_Comptes_Sociaux\\" + path_folder + "\\Screenshot")

        time.sleep(7)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(7)

        # Click on the 'Nom du fichier :' bar
        pywinauto.mouse.click(button='left', coords=(260, 375))

        time.sleep(7)

        # Press the 'Ctrl+A'
        pywinauto.keyboard.send_keys('^a')

        time.sleep(7)

        # Insert the 'Page_3.pdf'
        pywinauto.keyboard.send_keys('Page_3.pdf')

        time.sleep(7)

        # Click on the 'Enregistrer' button
        pywinauto.mouse.click(button='left', coords=(510, 445))

        time.sleep(7)

        # Close the onglet
        pywinauto.keyboard.send_keys('^w')

        time.sleep(7)

        # Click on the screen
        pywinauto.mouse.click(button='left', coords=(500, 10))

        time.sleep(7)

        # Click on the 'Etape suivante' checkbox
        pywinauto.mouse.click(button='left', coords=(1070, 520))

        time.sleep(7)

        # Click on the screen
        pywinauto.mouse.click(button='left', coords=(1200, 530))

        time.sleep(7)

        # Press the 'Down' button in 6 times
        pywinauto.keyboard.send_keys('{DOWN 6}')

        time.sleep(7)

        # Click on the 'Autres documents à ajouter (selon les cas)' button
        pywinauto.mouse.click(button='left', coords=(340, 345))

        time.sleep(7)

        # Click on the 'Ajouter' button for 'Bilan (actif, passif) et compte de résultat'
        pywinauto.mouse.click(button='left', coords=(1050, 130))

        time.sleep(7)

        # Click on the bar to select the folder
        pywinauto.mouse.click(button='left', coords=(380, 50))

        time.sleep(7)

        # Enter the path folder
        pywinauto.keyboard.send_keys("A:\\1_Professionnel\\1_Holomorphe\\1_Administration\\2_Gestion_Declarations_Administratives\\1_Recurrentes\\5_Infogreffe\\4_Approbation_Comptes_Sociaux\\" + path_folder)

        time.sleep(7)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(7)

        # Click on the 'Nom du fichier :' bar
        pywinauto.mouse.click(button='left', coords=(260, 415))

        time.sleep(7)

        # Press the 'Ctrl+A'
        pywinauto.keyboard.send_keys('^a')

        time.sleep(7)

        # Insert the 'Bilan_Compte_Resultat.pdf'
        pywinauto.keyboard.send_keys('Bilan_Compte_Resultat.pdf')

        time.sleep(7)

        # Click on the 'Ouvrir' button
        pywinauto.mouse.click(button='left', coords=(510, 445))

        time.sleep(25)

        # Click on the 'Ajouter' button for 'Inventaire'
        pywinauto.mouse.click(button='left', coords=(1050, 175))

        time.sleep(7)

        # Click on the bar to select the folder
        pywinauto.mouse.click(button='left', coords=(380, 50))

        time.sleep(7)

        # Enter the path folder
        pywinauto.keyboard.send_keys("A:\\1_Professionnel\\1_Holomorphe\\1_Administration\\2_Gestion_Declarations_Administratives\\1_Recurrentes\\5_Infogreffe\\4_Approbation_Comptes_Sociaux\\" + path_folder)

        time.sleep(7)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(7)

        # Click on the 'Nom du fichier :' bar
        pywinauto.mouse.click(button='left', coords=(260, 415))

        time.sleep(7)

        # Press the 'Ctrl+A'
        pywinauto.keyboard.send_keys('^a')

        time.sleep(7)

        # Insert the 'Inventaire.pdf'
        pywinauto.keyboard.send_keys('Inventaire.pdf')

        time.sleep(7)

        # Click on the 'Ouvrir' button
        pywinauto.mouse.click(button='left', coords=(510, 445))

        time.sleep(25)

        # Click on the 'Ajouter' button for 'Attestation de conformité des documents comptables
        # ( télécharger le modèle )'
        pywinauto.mouse.click(button='left', coords=(1050, 215))

        time.sleep(7)

        # Click on the bar to select the folder
        pywinauto.mouse.click(button='left', coords=(380, 50))

        time.sleep(7)

        # Enter the path folder
        pywinauto.keyboard.send_keys("A:\\1_Professionnel\\1_Holomorphe\\1_Administration\\2_Gestion_Declarations_Administratives\\1_Recurrentes\\5_Infogreffe\\4_Approbation_Comptes_Sociaux\\" + path_folder)

        time.sleep(7)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(7)

        # Click on the 'Nom du fichier :' bar
        pywinauto.mouse.click(button='left', coords=(260, 415))

        time.sleep(7)

        # Press the 'Ctrl+A'
        pywinauto.keyboard.send_keys('^a')

        time.sleep(7)

        # Insert the 'Conformite_Comptables.pdf'
        pywinauto.keyboard.send_keys('Conformite_Comptables.pdf')

        time.sleep(7)

        # Click on the 'Ouvrir' button
        pywinauto.mouse.click(button='left', coords=(510, 445))

        time.sleep(25)

        # Click on the 'Ajouter' button for 'Déclaration de confidentialité des comptes annuels
        # ( télécharger le modèle )'
        pywinauto.mouse.click(button='left', coords=(1050, 260))

        time.sleep(7)

        # Click on the bar to select the folder
        pywinauto.mouse.click(button='left', coords=(380, 50))

        time.sleep(7)

        # Enter the path folder
        pywinauto.keyboard.send_keys("A:\\1_Professionnel\\1_Holomorphe\\1_Administration\\2_Gestion_Declarations_Administratives\\1_Recurrentes\\5_Infogreffe\\4_Approbation_Comptes_Sociaux\\" + path_folder)

        time.sleep(7)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(7)

        # Click on the 'Nom du fichier :' bar
        pywinauto.mouse.click(button='left', coords=(260, 415))

        time.sleep(7)

        # Press the 'Ctrl+A'
        pywinauto.keyboard.send_keys('^a')

        time.sleep(7)

        # Insert the 'Declaration_Confidentialite_Comptes_Annuels.pdf'
        pywinauto.keyboard.send_keys('Declaration_Confidentialite_Comptes_Annuels.pdf')

        time.sleep(7)

        # Click on the 'Ouvrir' button
        pywinauto.mouse.click(button='left', coords=(510, 445))

        time.sleep(25)

        # Click on the 'Ajouter' button for 'PV d'Assemblée (proposition et résolution d'affectation votée)'
        pywinauto.mouse.click(button='left', coords=(1050, 340))

        time.sleep(7)

        # Click on the bar to select the folder
        pywinauto.mouse.click(button='left', coords=(380, 50))

        time.sleep(7)

        # Enter the path folder
        pywinauto.keyboard.send_keys("A:\\1_Professionnel\\1_Holomorphe\\1_Administration\\2_Gestion_Declarations_Administratives\\1_Recurrentes\\5_Infogreffe\\4_Approbation_Comptes_Sociaux\\" + path_folder)

        time.sleep(7)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(7)

        # Click on the 'Nom du fichier :' bar
        pywinauto.mouse.click(button='left', coords=(260, 415))

        time.sleep(7)

        # Press the 'Ctrl+A'
        pywinauto.keyboard.send_keys('^a')

        time.sleep(7)

        # Insert the 'P_V_A_C_Annuels.pdf'
        pywinauto.keyboard.send_keys('P_V_A_C_Annuels.pdf')

        time.sleep(7)

        # Click on the 'Ouvrir' button
        pywinauto.mouse.click(button='left', coords=(510, 445))

        time.sleep(25)

        # Click on the 'Ajouter' button for 'Rapport de gestion'
        pywinauto.mouse.click(button='left', coords=(1050, 385))

        time.sleep(7)

        # Click on the bar to select the folder
        pywinauto.mouse.click(button='left', coords=(380, 50))

        time.sleep(7)

        # Enter the path folder
        pywinauto.keyboard.send_keys("A:\\1_Professionnel\\1_Holomorphe\\1_Administration\\2_Gestion_Declarations_Administratives\\1_Recurrentes\\5_Infogreffe\\4_Approbation_Comptes_Sociaux\\" + path_folder)

        time.sleep(7)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(7)

        # Click on the 'Nom du fichier :' bar
        pywinauto.mouse.click(button='left', coords=(260, 415))

        time.sleep(7)

        # Press the 'Ctrl+A'
        pywinauto.keyboard.send_keys('^a')

        time.sleep(7)

        # Insert the 'Rapport_Gestion.pdf'
        pywinauto.keyboard.send_keys('Rapport_Gestion.pdf')

        time.sleep(7)

        # Click on the 'Ouvrir' button
        pywinauto.mouse.click(button='left', coords=(510, 445))

        time.sleep(25)

        # Click on the "Fireshot" button
        pywinauto.mouse.click(button='left', coords=(1140, 50))

        time.sleep(7)

        # Click on the "Capture entire page" button
        pywinauto.mouse.click(button='left', coords=(1020, 110))

        time.sleep(10)

        # Click on the "Save to PDF" button
        pywinauto.mouse.click(button='left', coords=(1160, 330))

        time.sleep(7)

        # Click on the bar to select the folder
        pywinauto.mouse.click(button='left', coords=(380, 50))

        time.sleep(7)

        # Enter the path folder
        pywinauto.keyboard.send_keys(
            "A:\\1_Professionnel\\1_Holomorphe\\1_Administration\\2_Gestion_Declarations_Administratives\\1_Recurrentes\\5_Infogreffe\\4_Approbation_Comptes_Sociaux\\" + path_folder + "\\Screenshot")

        time.sleep(7)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(7)

        # Click on the 'Nom du fichier :' bar
        pywinauto.mouse.click(button='left', coords=(260, 375))

        time.sleep(7)

        # Press the 'Ctrl+A'
        pywinauto.keyboard.send_keys('^a')

        time.sleep(7)

        # Insert the 'Page_4.pdf'
        pywinauto.keyboard.send_keys('Page_4.pdf')

        time.sleep(7)

        # Click on the 'Enregistrer' button
        pywinauto.mouse.click(button='left', coords=(510, 445))

        time.sleep(7)

        # Close the onglet
        pywinauto.keyboard.send_keys('^w')

        time.sleep(7)

        # Click on the screen
        pywinauto.mouse.click(button='left', coords=(500, 10))

        time.sleep(7)

        # Click on the 'Etape suivante' button
        pywinauto.mouse.click(button='left', coords=(1060, 540))

        time.sleep(7)

        # Press the 'Down' button in 5 times
        pywinauto.keyboard.send_keys('{DOWN 5}')

        time.sleep(7)

        # Click on the 'J'atteste avoir visualisé mon dépôt et vérifié les informations saisies.' checkbox
        pywinauto.mouse.click(button='left', coords=(280, 390))

        time.sleep(7)

        # Click on the 'Visualiser mon dépôt' button
        pywinauto.mouse.click(button='left', coords=(680, 310))

        time.sleep(30)

        # Click on the 'File downloaded' button
        #pywinauto.mouse.click(button='left', coords=(100, 700))

        time.sleep(5)

        print("ccleaner running")
        os.system("set ccleaner='C:\\Program Files\\CCleaner\\CCleaner.exe'")
        os.system("start ccleaner /AUTO")

        time.sleep(7)


if __name__ == '__main__':
    unittest.main()
