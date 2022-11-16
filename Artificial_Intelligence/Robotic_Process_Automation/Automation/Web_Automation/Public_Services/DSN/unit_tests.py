import unittest
import time
import warnings
from selenium import webdriver

annee = "3_Annee_2022"
mois = "4_Avril_Pour_Mars"


class UnitTestsWebAutomationDSNWithoutHeadless(unittest.TestCase):
    # ok
    def test_open_one_page_for_dsn_test(self):
        print("test_open_one_page_for_dsn_test")

        url = 'https://test.net-entreprises.fr/'

        time.sleep(5)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(5)

        # with Firefox
        browser = webdriver.Firefox(executable_path='..\\..\\geckodriver.exe')

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get(url)
        print('browser.get(url)')

        time.sleep(15)

    # ok
    def test_connect(self):
        print("test_connect")

        url = 'https://test.net-entreprises.fr/'
        siret = ''
        nom = ''
        prenom = ''
        mot_de_passe = ''

        time.sleep(5)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(5)

        # with Firefox
        browser = webdriver.Firefox(executable_path='..\\..\\geckodriver.exe')

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get(url)
        print('browser.get(url)')

        time.sleep(15)

        # Click on the 'Tout refuser' button
        tout_refuser_button = browser.find_element_by_xpath(
            '/html/body/div[5]/div/div[1]/p[3]/button[2]'
        )
        tout_refuser_button.click()
        print('tout_refuser_button.click()')

        time.sleep(5)

        # Click on the 'Votre compte' button
        votre_compte_button = browser.find_element_by_xpath(
            '/html/body/header/label[3]'
        )
        votre_compte_button.click()
        print('votre_compte_button.click()')

        time.sleep(5)

        # Insert the 'siret_input' text
        siret_input = browser.find_element_by_xpath(
            '//*[@id="menu-login__siret"]'
        )
        siret_input.clear()
        siret_input.send_keys(siret)
        print("siret_input.send_keys(siret)")

        time.sleep(5)

        # Insert the 'nom_input' text
        nom_input = browser.find_element_by_xpath(
            '//*[@id="menu-login__nom"]'
        )
        nom_input.clear()
        nom_input.send_keys(nom)
        print("nom_input.send_keys(nom)")

        time.sleep(5)

        # Insert the 'prenom_input' text
        prenom_input = browser.find_element_by_xpath(
            '//*[@id="menu-login__prenom"]'
        )
        prenom_input.clear()
        prenom_input.send_keys(prenom)
        print("prenom_input.send_keys(prenom)")

        time.sleep(5)

        # Insert the 'mot_de_passe_input' text
        mot_de_passe_input = browser.find_element_by_xpath(
            '//*[@id="menu-login__password"]'
        )
        mot_de_passe_input.clear()
        mot_de_passe_input.send_keys(mot_de_passe)
        print("mot_de_passe_input.send_keys(mot_de_passe)")

        time.sleep(5)

        # Click on the 'je_me_connecte_button' button
        je_me_connecte_button = browser.find_element_by_xpath(
            "/html/body/div[2]/div/div[3]/div[2]/form/button"
        )
        je_me_connecte_button.click()
        print('je_me_connecte_button.click()')

        time.sleep(10)

    #
    def test_recuperer_dernier_dsn_test_internet(self):
        print("test_recuperer_dernier_dsn_test_internet")

        url = 'https://test.net-entreprises.fr/'
        siret = ''
        nom = ''
        prenom = ''
        mot_de_passe = ''
        folder = "A:\\1_Professionnel\\1_Holomorphe\\1_Administration\\2_Gestion_Declarations_Administratives" \
                 "\\1_Recurrentes\\2_Net_Entreprises__DSN\\5_Depots_Fichiers_DSN\\3_Tests\\" \
                 + annee + "\\" + mois

        time.sleep(5)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(5)

        # with Firefox
        browser = webdriver.Firefox(executable_path='..\\..\\geckodriver.exe')

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get(url)
        print('browser.get(url)')

        time.sleep(15)

        # Click on the 'Tout refuser' button
        tout_refuser_button = browser.find_element_by_xpath(
            '/html/body/div[5]/div/div[1]/p[3]/button[2]'
        )
        tout_refuser_button.click()
        print('tout_refuser_button.click()')

        time.sleep(5)

        # Click on the 'Votre compte' button
        votre_compte_button = browser.find_element_by_xpath(
            '/html/body/header/label[3]'
        )
        votre_compte_button.click()
        print('votre_compte_button.click()')

        time.sleep(5)

        # Insert the 'siret_input' text
        siret_input = browser.find_element_by_xpath(
            '//*[@id="menu-login__siret"]'
        )
        siret_input.clear()
        siret_input.send_keys(siret)
        print("siret_input.send_keys(siret)")

        time.sleep(5)

        # Insert the 'nom_input' text
        nom_input = browser.find_element_by_xpath(
            '//*[@id="menu-login__nom"]'
        )
        nom_input.clear()
        nom_input.send_keys(nom)
        print("nom_input.send_keys(nom)")

        time.sleep(5)

        # Insert the 'prenom_input' text
        prenom_input = browser.find_element_by_xpath(
            '//*[@id="menu-login__prenom"]'
        )
        prenom_input.clear()
        prenom_input.send_keys(prenom)
        print("prenom_input.send_keys(prenom)")

        time.sleep(5)

        # Insert the 'mot_de_passe_input' text
        mot_de_passe_input = browser.find_element_by_xpath(
            '//*[@id="menu-login__password"]'
        )
        mot_de_passe_input.clear()
        mot_de_passe_input.send_keys(mot_de_passe)
        print("mot_de_passe_input.send_keys(mot_de_passe)")

        time.sleep(5)

        # Click on the 'je_me_connecte_button' button
        je_me_connecte_button = browser.find_element_by_xpath(
            "/html/body/div[2]/div/div[3]/div[2]/form/button"
        )
        je_me_connecte_button.click()
        print('je_me_connecte_button.click()')

        time.sleep(10)

        # Click on the 'pilote_dsn_rg_button' button
        pilote_dsn_rg_button = browser.find_element_by_xpath(
            '/html/body/div[1]/main/div/div[2]/div/div/div/div[1]'
        )
        pilote_dsn_rg_button.click()
        print('pilote_dsn_rg_button.click()')

        time.sleep(10)

        # save_screenshot Page_1
        browser.save_screenshot(
            folder + "\\Page_1.png"
        )
        print('save_screenshot Page_1')

        time.sleep(5)

        # Click on the 'glass_button_1' button
        glass_button_1 = browser.find_element_by_xpath(
            '/html/body/table/tbody/tr[3]/td[2]/div[7]/div/table/tbody/tr[1]/td[5]/a'
        )
        glass_button_1.click()
        print('glass_button_1.click()')

        time.sleep(10)

        # save_screenshot Page_2
        browser.save_screenshot(
            folder + "\\Page_2.png"
        )
        print('save_screenshot Page_2')

        time.sleep(5)

        # Click on the 'downloads_button' button
        downloads_button = browser.find_element_by_xpath(
            '/html/body/table/tbody/tr[3]/td[2]/div[5]/a'
        )
        downloads_button.click()
        print('downloads_button.click()')

        time.sleep(10)

        # Download files
        for i in range(0, 31):
            # Click on the 'download_button' button
            download_button = browser.find_element_by_xpath(
                '/html/body/table/tbody/tr[3]/td[2]/div[5]/div[2]/img[3]'
            )
            download_button.click()
            print('download_button.click()')

            time.sleep(5)

            # Click on the 'next_button' button
            next_button = browser.find_element_by_xpath(
                '/html/body/table/tbody/tr[3]/td[2]/div[5]/div[2]/img[2]'
            )
            next_button.click()
            print('next_button.click()')

            time.sleep(5)

        # Click on the 'downloads_button' button
        downloads_button = browser.find_element_by_xpath(
            '/html/body/table/tbody/tr[3]/td[2]/div[5]/a'
        )
        downloads_button.click()
        print('downloads_button.click()')

        time.sleep(10)

        # Click on the 'glass_button_2' button
        glass_button_2 = browser.find_element_by_xpath(
            '/html/body/table/tbody/tr[3]/td[2]/div[5]/div[3]/span[7]/a'
        )
        glass_button_2.click()
        print('glass_button_2.click()')

        time.sleep(10)

        # save_screenshot Page_3
        browser.save_screenshot(
            folder + "\\Page_3.png"
        )
        print('save_screenshot Page_2')

        time.sleep(5)


if __name__ == '__main__':
    unittest.main()
