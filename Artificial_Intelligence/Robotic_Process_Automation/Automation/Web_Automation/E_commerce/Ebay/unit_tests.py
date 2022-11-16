import unittest
import time
import warnings
from selenium import webdriver


class UnitTestsWebAutomationEbay(unittest.TestCase):
    def test_se_connecter(self):
        print('test_se_connecter')

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
        browser.get('https://www.ebay.fr/')

        time.sleep(5)

        # Click on the "Refuser et savoir plus" button
        refuser_button = browser.find_element_by_xpath(
            "/html/body/div[6]/div[1]/div[2]/div[2]/div[2]/a"
        )
        refuser_button.click()

        time.sleep(10)

        # Click on the "Continuer" button
        continuer_button = browser.find_element_by_xpath(
            "/html/body/div[4]/div/div[2]/section[3]/section/button"
        )
        continuer_button.click()

        time.sleep(10)

        # Click on the "Connectez-vous" button
        connectez_vous_button = browser.find_element_by_xpath(
            "/html/body/header/div/ul[1]/li[1]/span/a"
        )
        connectez_vous_button.click()

        time.sleep(10)

    def test_acheter_un_produit(self):
        print("test_acheter_un_produit")

        url_produit = ""

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
        browser.get(url_produit)

        time.sleep(5)

        # Click on the "Refuser et savoir plus" button
        refuser_button = browser.find_element_by_xpath(
            "/html/body/div[6]/div[1]/div[2]/div[2]/div[2]/a"
        )
        refuser_button.click()

        time.sleep(10)

        # Click on the "Continuer" button
        continuer_button = browser.find_element_by_xpath(
            "/html/body/div[4]/div/div[2]/section[3]/section/button"
        )
        continuer_button.click()

        time.sleep(10)

        """
        print("ccleaner running")
        os.system("set ccleaner='C:\\Program Files\\CCleaner\\CCleaner.exe'")
        os.system("start ccleaner /AUTO")

        time.sleep(60)
        """


if __name__ == '__main__':
    unittest.main()
