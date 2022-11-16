import unittest
import time
import warnings
from selenium import webdriver


class UnitTestsWebAutomationLeboncoin(unittest.TestCase):
    def test_open_one_page(self):
        print("test_open_one_page")

        time.sleep(1)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(1)

        # with Firefox
        browser = webdriver.Firefox(executable_path='geckodriver.exe')

        time.sleep(1)

        # maximize window
        browser.maximize_window()

        time.sleep(1)

        # open
        browser.get('https://www.leboncoin.fr/ventes_immobilieres/1792671613.htm?ac=558505705')

        time.sleep(5)

        continuer_sans_accepter = browser.find_element_by_id("didomi-notice-disagree-button")
        continuer_sans_accepter.click()


if __name__ == '__main__':
    unittest.main()
