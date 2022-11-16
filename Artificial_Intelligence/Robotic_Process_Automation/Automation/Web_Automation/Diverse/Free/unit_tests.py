import unittest
import time
import warnings
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class UnitTestsWebAutomationFree(unittest.TestCase):
    # ok
    def test_se_connecter(self):
        print("test_se_connecter")

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
        browser.get('https://mobile.free.fr/account/')

        time.sleep(15)

        identifiant_input = browser.find_element_by_xpath(
            "/html/body/div[1]/div[1]/div/div[4]/div/form/div[1]/label/input"
        )
        identifiant_input.clear()
        identifiant_input.send_keys("")
        print('identifiant_input send_keys')

        time.sleep(5)

        password_input = browser.find_element_by_xpath(
            "/html/body/div[1]/div[1]/div/div[4]/div/form/div[2]/label/input"
        )
        password_input.clear()
        password_input.send_keys("")
        password_input.send_keys(Keys.ENTER)
        print('password_input send_keys')

        time.sleep(20)

    # ok
    def test_display_consumption(self):
        print("test_display_consumption")

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
        browser.get('https://mobile.free.fr/account/')

        time.sleep(15)

        identifiant_input = browser.find_element_by_xpath(
            "/html/body/div[1]/div[1]/div/div[4]/div/form/div[1]/label/input"
        )
        identifiant_input.clear()
        identifiant_input.send_keys("")
        print('identifiant_input send_keys')

        time.sleep(5)

        password_input = browser.find_element_by_xpath(
            "/html/body/div[1]/div[1]/div/div[4]/div/form/div[2]/label/input"
        )
        password_input.clear()
        password_input.send_keys("")
        password_input.send_keys(Keys.ENTER)
        print('password_input send_keys')

        time.sleep(20)

        conso_data = browser.find_element_by_xpath(
            '/html/body/div[1]/div[1]/div/div[4]/div/div/div[2]/div[3]/div[2]/div[1]/div'
        ).text
        print("conso_data : " + str(conso_data))

        time.sleep(10)

        deconnexion_button = browser.find_element_by_xpath(
            '/html/body/div[1]/div[1]/div/nav/div/div/div[2]/a'
        )
        deconnexion_button.click()
        print("deconnexion_button.click()")

        time.sleep(10)

        browser.quit()

    # ok
    def test_display_messagerie_vocal(self):
        print("test_display_messagerie_vocal")

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
        browser.get('https://mobile.free.fr/account/')

        time.sleep(15)

        identifiant_input = browser.find_element_by_xpath(
            "/html/body/div[1]/div[1]/div/div[4]/div/form/div[1]/label/input"
        )
        identifiant_input.clear()
        identifiant_input.send_keys("")
        print('identifiant_input send_keys')

        time.sleep(5)

        password_input = browser.find_element_by_xpath(
            "/html/body/div[1]/div[1]/div/div[4]/div/form/div[2]/label/input"
        )
        password_input.clear()
        password_input.send_keys("")
        password_input.send_keys(Keys.ENTER)
        print('password_input send_keys')

        time.sleep(20)

        messagerie_vocale_button = browser.find_element_by_xpath(
            '/html/body/div[1]/div[1]/div/nav/ul[1]/li[2]/ul/li[4]/a'
        )
        messagerie_vocale_button.click()
        print("messagerie_vocale_button.click()")


if __name__ == '__main__':
    unittest.main()
