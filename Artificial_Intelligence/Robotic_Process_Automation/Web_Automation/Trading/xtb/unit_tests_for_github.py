import time
import warnings
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import unittest
import subprocess


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
            executable_path='C:\\Users\\Jason\\Dropbox\\1_Personnel\\1_Recurrentes\\3_Outils_Numeriques\\GitHub'
                            '\\Cristal_Ball\\geckodriver.exe',
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

        email = ''
        password = ''

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
            executable_path='C:\\Users\\Jason\\Dropbox\\1_Personnel\\1_Recurrentes\\3_Outils_Numeriques\\GitHub'
                            '\\Cristal_Ball\\geckodriver.exe',
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

        email = ''
        password = ''

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
            executable_path='C:\\Users\\Jason\\Dropbox\\1_Personnel\\1_Recurrentes\\3_Outils_Numeriques\\GitHub'
                            '\\Cristal_Ball\\geckodriver.exe',
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

    #
    def test_place_an_order_of_forex_pair_on_xstation5(self):
        print('test_place_an_order_of_forex_pair_on_xstation5')

        url = 'https://xstation5.xtb.com/?branch=fr#/_/login'

        email = ''
        password = ''

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
            executable_path='C:\\Users\\Jason\\Dropbox\\1_Personnel\\1_Recurrentes\\3_Outils_Numeriques\\GitHub'
                            '\\Cristal_Ball\\geckodriver.exe',
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

        time.sleep(10)

        try:
            # Click on the 'Cross' button
            cross_button = browser.find_element(
                by=By.XPATH,
                value='/html/body/div[1]/div[2]/div[5]/div/div/div[1]/div'
            )
            cross_button.click()
        except Exception as e:
            print('error : ' + str(e))

        time.sleep(7)

        # Insert the type of forex pair
        forex_pair_input = browser.find_element(
            by=By.XPATH,
            value='/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div/div[1]/div[3]/div/div/div/div[2]/div/div/div/div/div[2]/input'
        )
        forex_pair_input.clear()
        forex_pair_input.send_keys('EURUSD')

        time.sleep(5)

        # Click on the "Ouvrir le ticket d'ordre" button
        ticket_ordre_button = browser.find_element(
            by=By.XPATH,
            value='/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div/div[1]/div[3]/div/div/div/div[2]/div/div/div/div/div[1]/div[1]/div[1]/div/div[3]/button[3]'
        )
        ticket_ordre_button.click()

        time.sleep(5)

        # Click on the "Exécution instantanée" button
        execution_instantanee_button = browser.find_element(
            by=By.XPATH,
            value='/html/body/div[1]/div[2]/div[5]/div[1]/div/div[3]/ul/li[1]'
        )
        execution_instantanee_button.click()

        time.sleep(5)


if __name__ == '__main__':
    unittest.main()
