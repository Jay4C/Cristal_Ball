import subprocess
import unittest
import time
import warnings
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class UnitTestsWebAutomationGmail(unittest.TestCase):
    # ok
    def test_kill_some_processes(self):
        print("test_kill_some_processes")

        subprocess.call("taskkill /F /IM geckodriver.exe")
        subprocess.call("taskkill /F /IM firefox.exe")

    # ok
    def test_open_one_page(self):
        print("test_open_one_page")

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
        browser.get('https://accounts.google.com/signin/v2/identifier?service=mail&passive=true&rm=false&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F%3Fhl%3Dfr&ss=1&scc=1&ltmpl=default&ltmplcache=2&hl=fr&emr=1&osid=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin')

        time.sleep(5)


if __name__ == '__main__':
    unittest.main()
