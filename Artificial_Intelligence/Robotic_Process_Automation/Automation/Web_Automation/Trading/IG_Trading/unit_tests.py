import unittest
import time
import warnings
from selenium import webdriver


class UnitTestsWebAutomationIgTrading(unittest.TestCase):
    # ok
    def test_se_connecter(self):
        print("test_se_connecter")

        time.sleep(5)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(5)

        # with Firefox
        browser = webdriver.Firefox(executable_path='..\\geckodriver.exe')

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get('https://www.ig.com/fr/login')

        time.sleep(15)

        j_accepte_button = browser.find_element_by_xpath(
            "//a[@href='#information-banner-dismiss'][@class='button  button-blue js_target']"
        )
        j_accepte_button.click()

        time.sleep(5)

        email_input = browser.find_element_by_xpath(
            "//input[@id='account_id']"
        )
        email_input.clear()
        email_input.send_keys("")

        time.sleep(5)

        password_input = browser.find_element_by_xpath(
            "//input[@id='nonEncryptedPassword']"
        )
        password_input.clear()
        password_input.send_keys("")

        time.sleep(5)

        connexion_button = browser.find_element_by_xpath(
            "//input[@id='loginbutton']"
        )
        connexion_button.click()

        time.sleep(5)

    # ok
    def test_compte_demo_cfd_forex_eur_usd_place_one_order(self):
        print("test_compte_demo_cfd_forex_eur_usd_place_one_order")

        time.sleep(5)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(5)

        # with Firefox
        browser = webdriver.Firefox(executable_path='..\\geckodriver.exe')

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get('https://www.ig.com/fr/login')

        time.sleep(15)

        j_accepte_button = browser.find_element_by_xpath(
            "//a[@href='#information-banner-dismiss'][@class='button  button-blue js_target']"
        )
        j_accepte_button.click()

        time.sleep(5)

        email_input = browser.find_element_by_xpath(
            "//input[@id='account_id']"
        )
        email_input.clear()
        email_input.send_keys("")

        time.sleep(5)

        password_input = browser.find_element_by_xpath(
            "//input[@id='nonEncryptedPassword']"
        )
        password_input.clear()
        password_input.send_keys("")

        time.sleep(5)

        connexion_button = browser.find_element_by_xpath(
            "//input[@id='loginbutton']"
        )
        connexion_button.click()

        time.sleep(10)

        jason_aloyau_demo_button = browser.find_element_by_xpath(
            "//network-profile[@class='network-strip-item network-profile']"
        )
        jason_aloyau_demo_button.click()

        time.sleep(10)

        cfd_demo_button = browser.find_element_by_xpath(
            "//name[@title='CFD']"
        )
        cfd_demo_button.click()

        time.sleep(10)

        vente_button = browser.find_element_by_xpath(
            "//div[@id='ember100']"
        )
        vente_button.click()

        time.sleep(10)

        quantite_input = browser.find_element_by_xpath(
            "//input[@id='ember109']"
        )
        quantite_input.clear()
        quantite_input.send_keys("1")

        time.sleep(10)

        stop_normal_input = browser.find_element_by_xpath(
            "//input[@id='ember120']"
        )
        stop_normal_input.clear()
        stop_normal_input.send_keys("10")

        time.sleep(10)

        limite_input = browser.find_element_by_xpath(
            "//input[@id='ember131']"
        )
        limite_input.clear()
        limite_input.send_keys("10")

        time.sleep(10)

        placer_un_ordre_button = browser.find_element_by_xpath(
            "//button[@data-automation='ig-action-submit-button']"
        )
        placer_un_ordre_button.click()

        time.sleep(10)


if __name__ == '__main__':
    unittest.main()
