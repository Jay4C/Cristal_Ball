import unittest
import time
import warnings
from selenium import webdriver


class UnitTestsWebAutomationPropollerAds(unittest.TestCase):
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
        browser.get('https://publishers.propellerads.com/#/signIn')

        time.sleep(15)

        email_input = browser.find_element_by_xpath(
            "//input[@id='username']"
        )
        email_input.clear()
        email_input.send_keys("")

        time.sleep(5)

        password_input = browser.find_element_by_xpath(
            "//input[@id='password']"
        )
        password_input.clear()
        password_input.send_keys("")

        time.sleep(5)

        log_in_button = browser.find_element_by_xpath(
            "//button[@id='login-signin-button']"
        )
        log_in_button.click()

        time.sleep(5)


if __name__ == '__main__':
    unittest.main()
