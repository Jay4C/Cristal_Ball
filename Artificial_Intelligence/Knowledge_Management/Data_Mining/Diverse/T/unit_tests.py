import time
import warnings
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
import unittest
import subprocess

username = ""
password = ""


class UnitTestsDataMiningDiverseT(unittest.TestCase):
    # ok
    def test_close_all_processes(self):
        print('test_close_all_processes')

        subprocess.run('taskkill /f /im firefox.exe')
        subprocess.run('taskkill /f /im geckodriver.exe')

    # ok
    def test_open_one_page(self):
        print('test_open_one_page')

        url = 'https://www.tecice.com/login.php?location=%2F'

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
            executable_path='C:\\Users\\\\Jason\\Documents\\Devs\\Cristal_Ball\\geckodriver.exe',
            options=options
        )

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get(url)

        time.sleep(5)

    # ok
    def test_connect(self):
        print('test_connect')

        url = "https://www.tecice.com/pages/parc.php?parc=34"

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
            executable_path='C:\\Users\\\\Jason\\Documents\\Devs\\Cristal_Ball\\geckodriver.exe',
            options=options
        )

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get(url)

        time.sleep(10)

        # Insert the email
        username_input = browser.find_element(
            by=By.XPATH,
            value="/html/body/div[1]/form/input[1]"
        )
        username_input.send_keys(username)

        time.sleep(1)

        # Insert the password
        password_input = browser.find_element(
            by=By.XPATH,
            value="/html/body/div[1]/form/input[2]"
        )
        password_input.send_keys(password)
        time.sleep(2)
        password_input.send_keys(Keys.ENTER)

        time.sleep(1)

    # ok
    def test_extract_data_flops_energtic_intensive_buildings(self):
        print('test_extract_data_flops_energtic_intensive_buildings')

        url = "https://www.tecice.com/pages/parc.php?parc=34"

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
            executable_path='C:\\Users\\\\Jason\\Documents\\Devs\\Cristal_Ball\\geckodriver.exe',
            options=options
        )

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get(url)

        time.sleep(10)

        # Insert the email
        username_input = browser.find_element(
            by=By.XPATH,
            value="/html/body/div[1]/form/input[1]"
        )
        username_input.send_keys(username)

        time.sleep(1)

        # Insert the password
        password_input = browser.find_element(
            by=By.XPATH,
            value="/html/body/div[1]/form/input[2]"
        )
        password_input.send_keys(password)
        time.sleep(2)
        password_input.send_keys(Keys.ENTER)

        time.sleep(40)

        building_names = browser.find_elements(
            by=By.TAG_NAME,
            value="text"
        )

        for building_name in building_names:
            print(building_name.text)


if __name__ == '__main__':
    unittest.main()
