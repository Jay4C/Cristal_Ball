import unittest
import time
import warnings
from selenium import webdriver


class UnitTestsWebAutomationMonoprixPlus(unittest.TestCase):
    # ok
    def test_open_one_page(self):
        print("test_open_one_page")

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        # with Firefox
        browser = webdriver.Firefox(executable_path='..\\geckodriver.exe')

        time.sleep(10)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get('https://www.monoprix.fr/lh/login')
        print("page opened")


if __name__ == '__main__':
    unittest.main()
