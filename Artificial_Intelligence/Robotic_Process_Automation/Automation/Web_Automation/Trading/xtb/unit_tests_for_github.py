import time
import warnings
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import unittest
import subprocess

email = ''
password = ''


class UnitTestsRPAWATradingXtb(unittest.TestCase):
    # ok
    def test_close_all_processes(self):
        print('test_close_all_processes')

        subprocess.run('taskkill /f /im firefox.exe')
        subprocess.run('taskkill /f /im geckodriver.exe')

    # ok
    def test_open_one_page(self):
        print('test_open_one_page')

        url = 'https://www.xtb.com/fr/forex'

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
        browser.get(url)

        time.sleep(10)

        browser.quit()

    # ok
    def test_login_account(self):
        print('test_login_account')

        url = 'https://co.xtb.com/#/login'

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
        browser.get(url)

        time.sleep(10)

        # Insert your email
        email_input = browser.find_element(
            by=By.XPATH,
            value='//*[@id="username"]'
        )
        email_input.clear()
        email_input.send_keys(email)

        time.sleep(5)

        # Insert your password
        password_input = browser.find_element(
            by=By.XPATH,
            value='//*[@id="password"]'
        )
        password_input.clear()
        password_input.send_keys(password)

        time.sleep(5)

        # Click on the 'Se connecter' button
        se_connecter_button = browser.find_element(
            by=By.XPATH,
            value='//*[@id="loginButton"]'
        )
        se_connecter_button.click()

        time.sleep(5)

    # ok
    def test_login_xstation5(self):
        print('test_login_xstation5')

        url = 'https://xstation5.xtb.com/?branch=fr#/_/login'

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
        browser.get(url)

        time.sleep(10)

        # Insert your email
        email_input = browser.find_element(
            by=By.XPATH,
            value='//*[@id="containment-wrapper"]/div[4]/div[1]/div/div[1]/div[2]/div/div/form/div[1]/input'
        )
        email_input.clear()
        email_input.send_keys(email)

        time.sleep(5)

        # Insert your password
        password_input = browser.find_element(
            by=By.XPATH,
            value='//*[@id="containment-wrapper"]/div[4]/div[1]/div/div[1]/div[2]/div/div/form/div[2]/input'
        )
        password_input.clear()
        password_input.send_keys(password)

        time.sleep(5)

        # Click on the 'Se connecter' button
        se_connecter_button = browser.find_element(
            by=By.XPATH,
            value='//*[@id="containment-wrapper"]/div[4]/div[1]/div/div[1]/div[2]/div/div/form/div[4]/input'
        )
        se_connecter_button.click()

        time.sleep(5)

    # ok
    def test_place_one_order_from_execution_instantanee(self):
        print('test_place_one_order_from_execution_instantanee')

        url = 'https://xstation5.xtb.com/?branch=fr#/_/login'

        volume = '0.01'

        # sell
        type_of_order = 'buy'

        type_of_currency = 'EURUSD'

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
        print("browser = webdriver.Firefox")

        time.sleep(5)

        # maximize window
        browser.maximize_window()
        print("browser.maximize_window()")

        time.sleep(5)

        # open
        browser.get(url)
        print("browser.get(url)")

        time.sleep(10)

        # Insert your email
        email_input = browser.find_element(
            by=By.XPATH,
            value='//*[@id="containment-wrapper"]/div[4]/div[1]/div/div[1]/div[2]/div/div/form/div[1]/input'
        )
        email_input.clear()
        email_input.send_keys(email)
        print("email_input.send_keys(email)")

        time.sleep(5)

        # Insert your password
        password_input = browser.find_element(
            by=By.XPATH,
            value='//*[@id="containment-wrapper"]/div[4]/div[1]/div/div[1]/div[2]/div/div/form/div[2]/input'
        )
        password_input.clear()
        password_input.send_keys(password)
        print("password_input.send_keys(password)")

        time.sleep(5)

        # Click on the 'Se connecter' button
        se_connecter_button = browser.find_element(
            by=By.XPATH,
            value='//*[@id="containment-wrapper"]/div[4]/div[1]/div/div[1]/div[2]/div/div/form/div[4]/input'
        )
        se_connecter_button.click()
        print("se_connecter_button.click()")

        time.sleep(10)

        # Insert the type of forex pair
        forex_pair_input = browser.find_element(
            by=By.XPATH,
            value='/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div/div[1]/div[3]/div/div/div/div[2]/div/div/div/div/'
                  'div[2]/input'
        )
        forex_pair_input.clear()
        forex_pair_input.send_keys(type_of_currency)
        print("forex_pair_input.send_keys(type_of_currency)")

        time.sleep(5)

        # Click on the "Ouvrir le ticket d'ordre" button
        ticket_ordre_button = browser.find_element(
            by=By.XPATH,
            value='/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div/div[1]/div[3]/div/div/div/div[2]/div/div/div/div'
                  '/div[1]/div[1]/div[1]/div/div[3]/button[3]'
        )
        ticket_ordre_button.click()
        print("ticket_ordre_button.click()")

        time.sleep(5)

        # Click on the "Exécution instantanée" button
        execution_instantanee_button = browser.find_element(
            by=By.XPATH,
            value='/html/body/div[1]/div[2]/div[5]/div[1]/div/div[3]/ul/li[1]'
        )
        execution_instantanee_button.click()
        print("execution_instantanee_button.click()")

        time.sleep(5)

        # Insert the volume
        volume_input = browser.find_element(
            by=By.XPATH,
            value='/html/body/div[1]/div[2]/div[5]/div[1]/div/div[3]/div/div[1]/div/div/div/div[1]/div/div[2]/div[1]/'
                  'div/form/span/input'
        )
        volume_input.clear()
        volume_input.send_keys(volume)
        print("volume_input.send_keys(volume)")

        time.sleep(5)

        # Click on the type of order
        if type_of_order == "sell":
            type_of_order_button = browser.find_element(
                by=By.XPATH,
                value="/html/body/div[1]/div[2]/div[5]/div[1]/div/div[3]/div/div[1]/div/div/div/div[3]/"
                      "trade-ticket-button[1]"
            )
            type_of_order_button.click()
        else:
            type_of_order_button = browser.find_element(
                by=By.XPATH,
                value="/html/body/div[1]/div[2]/div[5]/div[1]/div/div[3]/div/div[1]/div/div/div/div[3]/"
                      "trade-ticket-button[2]"
            )
            type_of_order_button.click()

        time.sleep(5)


if __name__ == '__main__':
    unittest.main()
