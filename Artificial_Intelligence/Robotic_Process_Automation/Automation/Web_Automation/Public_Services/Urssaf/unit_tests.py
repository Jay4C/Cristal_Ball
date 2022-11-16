import unittest
import time
import warnings
from selenium import webdriver

annee = "3_Annee_2022"
mois = "6_Juin"


class UnitTestsWebAutomationUrssaf(unittest.TestCase):
    # ok
    def test_open_one_page(self):
        print("test_open_one_page")

        url = 'https://www.urssaf.fr/portail/home/connectez-vous.html'

        time.sleep(5)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

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
        browser.get(url)
        print('browser.get(url)')

        time.sleep(15)

    # ok
    def test_se_connecter(self):
        print("test_se_connecter")

        identifiant = ""
        password = ""

        url = 'https://www.urssaf.fr/portail/home/connectez-vous.html'

        time.sleep(5)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

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
        browser.get(url)
        print('browser.get(url)')

        time.sleep(15)

        # Click on the 'Tout refuser' button
        tout_refuser_button = browser.find_element_by_xpath(
            '//*[@id="footer_tc_privacy_button_2"]'
        )
        tout_refuser_button.click()
        time.sleep(5)

        # Insert the 'Identifiant' input
        identifiant_input = browser.find_element_by_xpath(
            '//*[@id="loginSiret"]'
        )
        identifiant_input.clear()
        identifiant_input.send_keys(identifiant)
        print('identifiant_input.send_keys(identifiant)')
        time.sleep(5)

        # Insert the 'Password' input
        password_input = browser.find_element_by_xpath(
            '//*[@id="loginPassword"]'
        )
        password_input.clear()
        password_input.send_keys(password)
        print('password_input.send_keys(password)')
        time.sleep(5)

        # Click on the 'Je me connect' button
        je_me_connecte_button = browser.find_element_by_xpath(
            '/html/body/main/div/div/div[1]/div[1]/div/div/div[1]/div[1]/div[1]/div[1]/form/div[4]/button'
        )
        je_me_connecte_button.click()
        time.sleep(5)

    # ok
    def test_declarer_cotisations_neant(self):
        print("test_declarer_cotisations_neant")

        identifiant = ""
        password = ""

        url = 'https://www.urssaf.fr/portail/home/connectez-vous.html'

        time.sleep(5)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

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
        browser.get(url)
        print('browser.get(url)')

        time.sleep(15)

        # Click on the 'Tout refuser' button
        tout_refuser_button = browser.find_element_by_xpath(
            '//*[@id="footer_tc_privacy_button_2"]'
        )
        tout_refuser_button.click()
        print('tout_refuser_button.click()')
        time.sleep(5)

        # Insert the 'Identifiant' input
        identifiant_input = browser.find_element_by_xpath(
            '//*[@id="loginSiret"]'
        )
        identifiant_input.clear()
        identifiant_input.send_keys(identifiant)
        print('identifiant_input.send_keys(identifiant)')
        time.sleep(5)

        # Insert the 'Password' input
        password_input = browser.find_element_by_xpath(
            '//*[@id="loginPassword"]'
        )
        password_input.clear()
        password_input.send_keys(password)
        print('password_input.send_keys(password)')
        time.sleep(5)

        # Click on the 'Je me connect' button
        je_me_connecte_button = browser.find_element_by_xpath(
            '/html/body/main/div/div/div[1]/div[1]/div/div/div[1]/div[1]/div[1]/div[1]/form/div[4]/button'
        )
        je_me_connecte_button.click()
        print('je_me_connecte_button.click()')
        time.sleep(5)

        # Save screenshot
        browser.save_screenshot(
            "A:\\1_Professionnel\\1_Holomorphe\\1_Administration\\2_Gestion_Declarations_Administratives"
            "\\1_Recurrentes\\4_URSSAF\\3_Compte\\3_Declarer_Les_Cotisations\\"
            + annee
            + "\\"
            + mois
            + "\\Page_1.png"
        )
        print('print Page_1.png')
        time.sleep(5)

        # Click on the 'Déclarer des cotisations' button
        declarer_des_cotisations_button = browser.find_element_by_xpath(
            '//*[@id="s_cotisations_declarer"]'
        )
        declarer_des_cotisations_button.click()
        print("declarer_des_cotisations_button.click()")
        time.sleep(5)

        # Save screenshot
        browser.save_screenshot(
            "A:\\1_Professionnel\\1_Holomorphe\\1_Administration\\2_Gestion_Declarations_Administratives"
            "\\1_Recurrentes\\4_URSSAF\\3_Compte\\3_Declarer_Les_Cotisations\\"
            + annee
            + "\\"
            + mois
            + "\\Page_2.png"
        )
        print('print Page_2.png')
        time.sleep(5)

        # Click on the 'Deconnexion' button
        deconnexion_button = browser.find_element_by_xpath(
            '//*[@id="deconnecter"]'
        )
        deconnexion_button.click()
        print("deconnexion_button.click()")
        time.sleep(5)

        # Quit
        browser.quit()
        print("browser.quit()")
        time.sleep(5)

    #
    def test_payer_cotisations_neant(self):
        print("test_payer_cotisations_neant")

        identifiant = ""
        password = ""

        url = 'https://www.urssaf.fr/portail/home/connectez-vous.html'

        time.sleep(5)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

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
        browser.get(url)
        print('browser.get(url)')

        time.sleep(15)

        # Click on the 'Tout refuser' button
        tout_refuser_button = browser.find_element_by_xpath(
            '//*[@id="footer_tc_privacy_button_2"]'
        )
        tout_refuser_button.click()
        print('tout_refuser_button.click()')
        time.sleep(5)

        # Insert the 'Identifiant' input
        identifiant_input = browser.find_element_by_xpath(
            '//*[@id="loginSiret"]'
        )
        identifiant_input.clear()
        identifiant_input.send_keys(identifiant)
        print('identifiant_input.send_keys(identifiant)')
        time.sleep(5)

        # Insert the 'Password' input
        password_input = browser.find_element_by_xpath(
            '//*[@id="loginPassword"]'
        )
        password_input.clear()
        password_input.send_keys(password)
        print('password_input.send_keys(password)')
        time.sleep(5)

        # Click on the 'Je me connect' button
        je_me_connecte_button = browser.find_element_by_xpath(
            '/html/body/main/div/div/div[1]/div[1]/div/div/div[1]/div[1]/div[1]/div[1]/form/div[4]/button'
        )
        je_me_connecte_button.click()
        print('je_me_connecte_button.click()')
        time.sleep(5)

        # Save screenshot
        browser.save_screenshot(
            "A:\\1_Professionnel\\1_Holomorphe\\1_Administration\\2_Gestion_Declarations_Administratives"
            "\\1_Recurrentes\\4_URSSAF\\3_Compte\\1_Payer_Les_Cotisations\\"
            + annee
            + "\\"
            + mois
            + "\\Page_1.png"
        )
        print('print Page_1.png')
        time.sleep(5)

        # Click on the 'Payer les cotisations' button
        browser.get('https://www.declaration.urssaf.fr/payer_declarations')
        print("browser.get('https://www.declaration.urssaf.fr/payer_declarations')")
        time.sleep(10)

        # Save screenshot
        browser.save_screenshot(
            "A:\\1_Professionnel\\1_Holomorphe\\1_Administration\\2_Gestion_Declarations_Administratives"
            "\\1_Recurrentes\\4_URSSAF\\3_Compte\\1_Payer_Les_Cotisations\\"
            + annee
            + "\\"
            + mois
            + "\\Page_2.png"
        )
        print('print Page_2.png')
        time.sleep(5)

        # Click on the 'Deconnexion' button
        deconnexion_button = browser.find_element_by_xpath(
            '//*[@id="deconnecter"]'
        )
        deconnexion_button.click()
        print("deconnexion_button.click()")
        time.sleep(5)

        # Quit
        browser.quit()
        print("browser.quit()")
        time.sleep(5)

    #
    def test_payer_les_dettes_neant(self):
        print("test_payer_les_dettes_neant")

        identifiant = ""
        password = ""

        url = 'https://www.urssaf.fr/portail/home/connectez-vous.html'

        time.sleep(5)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

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
        browser.get(url)
        print('browser.get(url)')

        time.sleep(15)

        # Click on the 'Tout refuser' button
        tout_refuser_button = browser.find_element_by_xpath(
            '//*[@id="footer_tc_privacy_button_2"]'
        )
        tout_refuser_button.click()
        print('tout_refuser_button.click()')
        time.sleep(5)

        # Insert the 'Identifiant' input
        identifiant_input = browser.find_element_by_xpath(
            '//*[@id="loginSiret"]'
        )
        identifiant_input.clear()
        identifiant_input.send_keys(identifiant)
        print('identifiant_input.send_keys(identifiant)')
        time.sleep(5)

        # Insert the 'Password' input
        password_input = browser.find_element_by_xpath(
            '//*[@id="loginPassword"]'
        )
        password_input.clear()
        password_input.send_keys(password)
        print('password_input.send_keys(password)')
        time.sleep(5)

        # Click on the 'Je me connect' button
        je_me_connecte_button = browser.find_element_by_xpath(
            '/html/body/main/div/div/div[1]/div[1]/div/div/div[1]/div[1]/div[1]/div[1]/form/div[4]/button'
        )
        je_me_connecte_button.click()
        print('je_me_connecte_button.click()')
        time.sleep(5)

        # Save screenshot
        browser.save_screenshot(
            "A:\\1_Professionnel\\1_Holomorphe\\1_Administration\\2_Gestion_Declarations_Administratives"
            "\\1_Recurrentes\\4_URSSAF\\3_Compte\\16_Payer_Les_Dettes\\"
            + annee
            + "\\"
            + mois
            + "\\Page_1.png"
        )
        print('print Page_1.png')
        time.sleep(5)

        # Click on the 'Payer les dettes' button
        browser.get('https://www.dcl.urssaf.fr/consulter/servlet/cotisant')
        print("browser.get('https://www.dcl.urssaf.fr/consulter/servlet/cotisant')")
        time.sleep(10)

        # Save screenshot
        browser.save_screenshot(
            "A:\\1_Professionnel\\1_Holomorphe\\1_Administration\\2_Gestion_Declarations_Administratives"
            "\\1_Recurrentes\\4_URSSAF\\3_Compte\\16_Payer_Les_Dettes\\"
            + annee
            + "\\"
            + mois
            + "\\Page_2.png"
        )
        print('print Page_2.png')
        time.sleep(5)

        # Click on the 'Deconnexion' button
        deconnexion_button = browser.find_element_by_xpath(
            '//*[@id="deconnecter"]'
        )
        deconnexion_button.click()
        print("deconnexion_button.click()")
        time.sleep(5)

        # Quit
        browser.quit()
        print("browser.quit()")
        time.sleep(5)


if __name__ == '__main__':
    unittest.main()
