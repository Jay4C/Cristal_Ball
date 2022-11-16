import os
import unittest
import time
import warnings
from selenium import webdriver


class UnitTestsWebAutomationLaserhub(unittest.TestCase):
    #
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
        browser.get('https://app.laserhub.com/login')

        time.sleep(15)

        '''
        cookies_settings = browser.find_element_by_xpath(
            ""
        )
        cookies_settings.click()
        
        time.sleep(10)
        
        email_input = browser.find_element_by_xpath(
            "/html/body/div[1]/div[1]/main/div/div/div/div/div/div/div/div/div/form/div[2]/input[1]"
        )
        email_input.clear()
        email_input.send_keys(".@outlokk.fr")

        time.sleep(5)

        password_input = browser.find_element_by_xpath(
            "/html/body/div[1]/div[1]/main/div/div/div/div/div/div/div/div/div/form/div[2]/input[2]"
        )
        password_input.clear()
        password_input.send_keys("")

        time.sleep(5)

        login_button = browser.find_element_by_xpath(
            "/html/body/div[1]/div[1]/main/div/div/div/div/div/div/div/div/div/form/div[2]/button"
        )
        login_button.click()

        time.sleep(15)

        print("ccleaner running")
        os.system("set ccleaner='C:\\Program Files\\CCleaner\\CCleaner.exe'")
        os.system("start ccleaner /AUTO")

        time.sleep(20)
        '''


if __name__ == '__main__':
    unittest.main()
