import unittest
import time
import warnings
from selenium import webdriver
from selenium.webdriver.common.by import By


class UnitTestsWebAutomationSculpteo(unittest.TestCase):
    # ok
    def test_open_a_page(self):
        print('test_open_a_page')

        time.sleep(5)

        warnings.filterwarnings(
            action="ignore",
            message="unclosed",
            category=ResourceWarning
        )

        time.sleep(5)

        # with Firefox
        browser = webdriver.Firefox(
            executable_path='..\\..\\geckodriver.exe'
        )

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get('https://www.sculpteo.com/fr/')

        time.sleep(5)

    # ok
    def test_se_connecter(self):
        print('test_se_connecter')

        email = ""

        password = ""

        time.sleep(5)

        warnings.filterwarnings(
            action="ignore",
            message="unclosed",
            category=ResourceWarning
        )

        time.sleep(5)

        # with Firefox
        browser = webdriver.Firefox(
            executable_path='..\\..\\geckodriver.exe'
        )

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get('https://www.sculpteo.com/fr/')

        time.sleep(5)

        # Click on the "Continuer sans accepter" button
        continuer_sans_accepter_button = browser.find_element_by_xpath(
            "/html/body/div[1]/div[1]/div/div[1]/div[1]/span"
        )
        continuer_sans_accepter_button.click()

        time.sleep(10)

        # Click on the "Connectez-vous" button
        connectez_vous_button = browser.find_element_by_xpath(
            "/html/body/header/div[2]/div[1]/div/div[2]/span[1]/a"
        )
        connectez_vous_button.click()

        time.sleep(10)

        # Insert the "Adresse email" input
        adresse_email_input = browser.find_element_by_xpath(
            '//*[@id="id_username"]'
        )
        adresse_email_input.send_keys(email)
        time.sleep(10)

        # Insert the "Mot de passe" input
        mot_de_passe_input = browser.find_element_by_xpath(
            '//*[@id="id_password"]'
        )
        mot_de_passe_input.send_keys(password)
        time.sleep(10)

        # Click on the "Connectez_vous" button
        connectez_vous_button_1 = browser.find_element_by_xpath(
            '/html/body/div[2]/div[2]/div[1]/div/div/div/div[2]/form/div[3]/input'
        )
        connectez_vous_button_1.click()
        time.sleep(10)

    # ok
    def test_transferer_un_fichier(self):
        print('test_transferer_un_fichier')

        email = ""

        password = ""

        file_path = "C:\\Users\\Jason\\Documents\\Devs\\Cristal_Ball\\Archives\\CAO\\Mercorus\\Version_5\\Stl" \
                    "\\part_bottom_support.stl"

        time.sleep(5)

        warnings.filterwarnings(
            action="ignore",
            message="unclosed",
            category=ResourceWarning
        )

        time.sleep(5)

        # with Firefox
        browser = webdriver.Firefox(
            executable_path='C:\\Users\\Jason\\Documents\Devs\\Cristal_Ball\\geckodriver.exe'
        )

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get('https://www.sculpteo.com/fr/')
        print("browser.get('https://www.sculpteo.com/fr/')")

        time.sleep(5)

        # Click on the "Continuer sans accepter" button
        continuer_sans_accepter_button = browser.find_element(
            by=By.XPATH,
            value="/html/body/div[1]/div[1]/div/div[1]/div[1]/span"
        )
        continuer_sans_accepter_button.click()
        print("continuer_sans_accepter_button.click()")

        time.sleep(10)

        # Click on the "Connectez-vous" button
        connectez_vous_button = browser.find_element(
            by=By.XPATH,
            value="/html/body/header/div[2]/div[1]/div/div[2]/span[1]/a"
        )
        connectez_vous_button.click()
        print("connectez_vous_button.click()")

        time.sleep(10)

        # Insert the "Adresse email" input
        adresse_email_input = browser.find_element(
            by=By.XPATH,
            value='//*[@id="id_username"]'
        )
        adresse_email_input.send_keys(email)
        print("adresse_email_input.send_keys(email)")

        time.sleep(10)

        # Insert the "Mot de passe" input
        mot_de_passe_input = browser.find_element(
            by=By.XPATH,
            value='//*[@id="id_password"]'
        )
        mot_de_passe_input.send_keys(password)
        print("mot_de_passe_input.send_keys(password)")

        time.sleep(10)

        # Click on the "Connectez_vous" button
        connectez_vous_button_1 = browser.find_element(
            by=By.XPATH,
            value='/html/body/div[2]/div[2]/div[1]/div/div/div/div[2]/form/div[3]/input'
        )
        connectez_vous_button_1.click()
        print("connectez_vous_button_1.click()")

        time.sleep(10)

        # Click on the "Transférer un fichier" button
        transferer_un_fichier_button = browser.find_element(
            by=By.XPATH,
            value='/html/body/div[1]/div[2]/div/div/a'
        )
        transferer_un_fichier_button.click()
        print("transferer_un_fichier_button.click()")

        time.sleep(10)

        # Click on the "Privé" button
        prive_button = browser.find_element(
            by=By.XPATH,
            value='/html/body/div[1]/div/div[1]/form/div[2]/div[1]/label[2]'
        )
        prive_button.click()
        print("prive_button.click()")

        time.sleep(10)

        # Click on the "sélectionner un fichier à transférer" button
        selectionner_un_fichier_a_transferer_button = browser.find_element(
            by=By.XPATH,
            value='/html/body/input[2]'
        )
        selectionner_un_fichier_a_transferer_button.send_keys(file_path)
        print('selectionner_un_fichier_a_transferer_button.send_keys(file_path)')

        time.sleep(30)

        # Click on the "Suivant" button
        suivant_button = browser.find_element(
            by=By.XPATH,
            value='/html/body/div[1]/div/div[1]/form/div[5]/div[1]/div/span[2]/a'
        )
        suivant_button.click()
        print('suivant_button.click()')

        time.sleep(10)


if __name__ == '__main__':
    unittest.main()
