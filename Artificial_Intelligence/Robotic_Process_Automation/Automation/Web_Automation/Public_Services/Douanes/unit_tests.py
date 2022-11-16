import unittest
import time
import warnings
from selenium import webdriver

mois = "6_Juin_Pour_Mai_[Neant]"
annee = "3_Annee_2022"
i = mois[0]


class UnitTestsWebAutomationDouanes(unittest.TestCase):
    # ok
    def test_open_one_page(self):
        print("test_open_one_page_for_dsn_test")

        url = 'https://www.douane.gouv.fr/'

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

        url = 'https://www.douane.gouv.fr/'

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
            '/html/body/div[1]/div/div/div[1]/div/div[3]/button[2]'
        )
        tout_refuser_button.click()
        print("tout_refuser_button.click()")

        time.sleep(5)

        # Click on the 'Se connecter' button
        se_connecter_button = browser.find_element_by_xpath(
            '/html/body/div[2]/header/div/div/div[2]/div/div/div/div/ul/li[1]/a'
        )
        se_connecter_button.click()
        print("se_connecter_button.click()")

        time.sleep(10)

        # Insert the "Identifiant" text
        identifiant_input = browser.find_element_by_xpath(
            '//*[@id="loginIdentifiant"]'
        )
        identifiant_input.clear()
        identifiant_input.send_keys(identifiant)
        print('identifiant_input.send_keys(identifiant)')

        time.sleep(5)

        # Insert the "password" text
        password_input = browser.find_element_by_xpath(
            '//*[@id="loginMotdepasse"]'
        )
        password_input.clear()
        password_input.send_keys(password)
        print('password_input.send_keys(password)')

        time.sleep(5)

        # Click on the 'Me connecter' button
        me_connecter_button = browser.find_element_by_xpath(
            '/html/body/main/section/div/div/form/div/div[1]/fieldset/div/div[5]/div/button'
        )
        me_connecter_button.click()
        print("me_connecter_button.click()")

        time.sleep(10)

    # ok
    def test_deb_sans_reponse(self):
        print("test_deb_sans_reponse")

        identifiant = ""

        password = ""

        url = 'https://www.douane.gouv.fr/'

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
            '/html/body/div[1]/div/div/div[1]/div/div[3]/button[2]'
        )
        tout_refuser_button.click()
        print("tout_refuser_button.click()")

        time.sleep(5)

        # Click on the 'Se connecter' button
        se_connecter_button = browser.find_element_by_xpath(
            '/html/body/div[2]/header/div/div/div[2]/div/div/div/div/ul/li[1]/a'
        )
        se_connecter_button.click()
        print("se_connecter_button.click()")

        time.sleep(10)

        # Insert the "Identifiant" text
        identifiant_input = browser.find_element_by_xpath(
            '//*[@id="loginIdentifiant"]'
        )
        identifiant_input.clear()
        identifiant_input.send_keys(identifiant)
        print('identifiant_input.send_keys(identifiant)')

        time.sleep(5)

        # Insert the "password" text
        password_input = browser.find_element_by_xpath(
            '//*[@id="loginMotdepasse"]'
        )
        password_input.clear()
        password_input.send_keys(password)
        print('password_input.send_keys(password)')

        time.sleep(5)

        # Click on the 'Me connecter' button
        me_connecter_button = browser.find_element_by_xpath(
            '/html/body/main/section/div/div/form/div/div[1]/fieldset/div/div[5]/div/button'
        )
        me_connecter_button.click()
        print("me_connecter_button.click()")

        time.sleep(15)

        # Click on the 'DEB' button
        deb_button = browser.find_element_by_xpath(
            '/html/body/main/div[3]/section[1]/div/div/section/ul/li[1]/div/a/div'
        )
        deb_button.click()
        print("deb_button.click()")

        time.sleep(15)

        # Save screenshot
        browser.save_screenshot(
            "A:\\1_Professionnel\\1_Holomorphe\\1_Administration\\2_Gestion_Declarations_Administratives"
            "\\1_Recurrentes\\3_Douanes\\1_Declaration_Intracommunautaires\\1_DEB\\"
            + annee
            + "\\"
            + mois
            + "\\Page_1.png"
        )

        time.sleep(5)

        # Switch to the new window
        window_after = browser.window_handles[1]
        browser.switch_to.window(window_after)
        print("browser.switch_to.window(window_after)")

        time.sleep(5)

        # open to https://www.douane.gouv.fr/debweb/cf.srv?etape=preTeleprocedurePostBascule
        browser.get("https://www.douane.gouv.fr/debweb/cf.srv?etape=preTeleprocedurePostBascule")
        print('browser.get(url)')

        time.sleep(5)

        # Save screenshot
        browser.save_screenshot(
            "A:\\1_Professionnel\\1_Holomorphe\\1_Administration\\2_Gestion_Declarations_Administratives"
            "\\1_Recurrentes\\3_Douanes\\1_Declaration_Intracommunautaires\\1_DEB\\"
            + annee
            + "\\"
            + mois
            + "\\Page_2.png"
        )

        time.sleep(5)

        # Click on the 'mois sans réponse' button
        mois_sans_reponse_button = browser.find_element_by_xpath(
            '/html/body/table/tbody/tr/td/table[2]/tbody/tr/td[1]/table/tbody/tr/td/ul/ul[1]/li[2]/a'
        )
        mois_sans_reponse_button.click()
        print("mois_sans_reponse_button.click()")

        time.sleep(5)

        # Click on the 'Pas de réponse statistique à l'introduction' button
        pas_de_reponse_statistique_introduction_button = browser.find_element_by_xpath(
            '/html/body/form[1]/table[4]/tbody/tr/td[2]/ul/li[1]/input'
        )
        pas_de_reponse_statistique_introduction_button.click()
        print("pas_de_reponse_statistique_introduction_button.click()")

        time.sleep(5)

        # Click on the 'Pas de réponse statistique à l'expédition' button
        pas_de_reponse_statistique_expedition_button = browser.find_element_by_xpath(
            '/html/body/form[1]/table[4]/tbody/tr/td[2]/ul/li[2]/input'
        )
        pas_de_reponse_statistique_expedition_button.click()
        print("pas_de_reponse_statistique_expedition_button.click()")

        time.sleep(5)

        # Click on the 'Annee' button
        select_annee_button = browser.find_element_by_xpath(
            '/html/body/form[1]/table[3]/tbody/tr[1]/td[2]/select/option[2]'
        )
        select_annee_button.click()
        print("select_annee_button.click()")

        time.sleep(5)

        # Click on the 'Mois' button
        select_mois_button = browser.find_element_by_xpath(
            '/html/body/form[1]/table[3]/tbody/tr[2]/td[2]/select/option[' + str(i) + ']'
        )
        select_mois_button.click()
        print("select_mois_button.click()")

        time.sleep(10)

        # Save screenshot
        browser.save_screenshot(
            "A:\\1_Professionnel\\1_Holomorphe\\1_Administration\\2_Gestion_Declarations_Administratives"
            "\\1_Recurrentes\\3_Douanes\\1_Declaration_Intracommunautaires\\1_DEB\\"
            + annee
            + "\\"
            + mois
            + "\\Page_3.png"
        )

        time.sleep(5)

        # Click on the 'Enregistrer' button
        enregistrer_button = browser.find_element_by_xpath(
            '//*[@id="suivant"]'
        )
        enregistrer_button.click()
        print("enregistrer_button.click()")

        time.sleep(5)

        # Save screenshot
        browser.save_screenshot(
            "A:\\1_Professionnel\\1_Holomorphe\\1_Administration\\2_Gestion_Declarations_Administratives"
            "\\1_Recurrentes\\3_Douanes\\1_Declaration_Intracommunautaires\\1_DEB\\"
            + annee
            + "\\"
            + mois
            + "\\Page_4.png"
        )

        time.sleep(10)

        # Click on the 'Lister les deb à zero' button
        lister_deb_a_zero_button = browser.find_element_by_xpath(
            '//*[@id="suivant"]'
        )
        lister_deb_a_zero_button.click()
        print("lister_deb_a_zero_button.click()")

        time.sleep(5)

        # Click on the 'Annee - Deb a zero' button
        select_annee_deb_a_zero_button = browser.find_element_by_xpath(
            '/html/body/form/table[3]/tbody/tr[1]/td[2]/select/option[2]'
        )
        select_annee_deb_a_zero_button.click()
        print("select_annee_deb_a_zero_button.click()")

        time.sleep(5)

        # Click on the 'Mois - Deb a zero' button
        select_mois_deb_a_zero_button = browser.find_element_by_xpath(
            '/html/body/form/table[3]/tbody/tr[2]/td[2]/select/option[' + str(i) + ']'
        )
        select_mois_deb_a_zero_button.click()
        print("select_mois_deb_a_zero_button.click()")

        time.sleep(10)

        # Click on the 'Lister les déclarations' button
        lister_les_declarations_button = browser.find_element_by_xpath(
            '//*[@id="suivant"]'
        )
        lister_les_declarations_button.click()
        print("lister_les_declarations_button.click()")

        time.sleep(7)

        # Save screenshot
        browser.save_screenshot(
            "A:\\1_Professionnel\\1_Holomorphe\\1_Administration\\2_Gestion_Declarations_Administratives"
            "\\1_Recurrentes\\3_Douanes\\1_Declaration_Intracommunautaires\\1_DEB\\"
            + annee
            + "\\"
            + mois
            + "\\Page_5.png"
        )

        time.sleep(10)


if __name__ == '__main__':
    unittest.main()
