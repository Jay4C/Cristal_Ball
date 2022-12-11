import subprocess
import unittest
import time
import warnings
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

username = ""

password = ""


class UnitTestsWebAutomationCdw(unittest.TestCase):
    # ok
    def test_open_a_page(self):
        print("test_open_a_page")

        url_page = "/"

        time.sleep(5)

        warnings.filterwarnings(
            action="ignore",
            message="unclosed",
            category=ResourceWarning
        )

        time.sleep(5)

        # with Firefox
        options = Options()
        options.headless = False
        browser = webdriver.Firefox(
            executable_path='A:\\GitHub\\Cristal_Ball\\geckodriver.exe',
            options=options
        )

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get(url_page)

    # ok
    def test_connect(self):
        print("test_connect")

        url_page = ""

        time.sleep(5)

        warnings.filterwarnings(
            action="ignore",
            message="unclosed",
            category=ResourceWarning
        )

        time.sleep(5)

        # with Firefox
        options = Options()
        options.headless = False
        browser = webdriver.Firefox(
            executable_path='A:\\GitHub\\Cristal_Ball\\geckodriver.exe',
            options=options
        )

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get(url_page)

        time.sleep(10)

        connexion_button = browser.find_element(
            by=By.XPATH,
            value="/html/body/nav/div/div[2]/ul[2]/div/a"
        )
        connexion_button.click()

        time.sleep(7)

        identifiant_input = browser.find_element(
            by=By.XPATH,
            value="/html/body/div[1]/div[2]/div/div[1]/div/div/div[2]/form/div[1]/input"
        )
        identifiant_input.clear()
        identifiant_input.send_keys(username)
        print('identifiant_input send_keys')

        time.sleep(5)

        password_input = browser.find_element(
            by=By.XPATH,
            value="/html/body/div[1]/div[2]/div/div[1]/div/div/div[2]/form/div[2]/input"
        )
        password_input.clear()
        password_input.send_keys(password)
        print('password_input send_keys')

        time.sleep(3)

        password_input.send_keys(Keys.ENTER)

        time.sleep(10)

    #
    def test_extract_one_name(self):
        print("test_extract_one_name")

        url_page = ""

        time.sleep(5)

        warnings.filterwarnings(
            action="ignore",
            message="unclosed",
            category=ResourceWarning
        )

        time.sleep(5)

        # with Firefox
        options = Options()
        options.headless = False
        browser = webdriver.Firefox(
            executable_path='A:\\GitHub\\Cristal_Ball\\geckodriver.exe',
            options=options
        )

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get(url_page)

        time.sleep(10)

        connexion_button = browser.find_element(
            by=By.XPATH,
            value="/html/body/nav/div/div[2]/ul[2]/div/a"
        )
        connexion_button.click()

        time.sleep(7)

        identifiant_input = browser.find_element(
            by=By.XPATH,
            value="/html/body/div[1]/div[2]/div/div[1]/div/div/div[2]/form/div[1]/input"
        )
        identifiant_input.clear()
        identifiant_input.send_keys(username)
        print('identifiant_input send_keys')

        time.sleep(5)

        password_input = browser.find_element(
            by=By.XPATH,
            value="/html/body/div[1]/div[2]/div/div[1]/div/div/div[2]/form/div[2]/input"
        )
        password_input.clear()
        password_input.send_keys(password)
        print('password_input send_keys')

        time.sleep(3)

        password_input.send_keys(Keys.ENTER)

        time.sleep(10)

        browser.get("/recherche-intell.php")

        time.sleep(10)

        recherche_button = browser.find_element(
            by=By.XPATH,
            value='//*[@id="cmdRechercheRapide"]'
        )
        recherche_button.click()

        time.sleep(7)

        affichage_images = browser.find_element(
            by=By.XPATH,
            value="/html/body/div[1]/div[1]/div[4]/div/div/div/div/div[1]/div/div[1]/div[2]/a[2]"
        )
        affichage_images.click()

        time.sleep(5)

        try:
            imgthumb_elements = browser.find_elements(
                by=By.CLASS_NAME,
                value='imgthumb'
            )

            print(f'imgthumb_elements {imgthumb_elements}')
        except Exception as e:
            print(f'error {e}')

        time.sleep(7)

        menu_button = browser.find_element(
            by=By.XPATH,
            value='//*[@id="monmenubt"]'
        )
        menu_button.click()

        time.sleep(5)

        signout_button = browser.find_element(
            by=By.XPATH,
            value='//*[@id="monmenubt"]'
        )
        signout_button.click()

        time.sleep(5)

        browser.quit()


if __name__ == '__main__':
    unittest.main()
