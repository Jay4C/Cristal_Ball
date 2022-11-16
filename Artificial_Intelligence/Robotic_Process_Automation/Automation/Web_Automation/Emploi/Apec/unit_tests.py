import subprocess
import unittest
import time
import warnings
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import requests
from bs4 import BeautifulSoup


class UnitTestsWebAutomationApec(unittest.TestCase):
    # ok
    def test_kill_some_processes(self):
        print("test_kill_some_processes")

        subprocess.call("taskkill /F /IM geckodriver.exe")
        subprocess.call("taskkill /F /IM firefox.exe")

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
            executable_path='..\\geckodriver.exe'
        )

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get('https://www.apec.fr/')

        time.sleep(15)

        refuser_tous_les_cookies_button = browser.find_element_by_id(
            "onetrust-reject-all-handler"
        )
        refuser_tous_les_cookies_button.click()
        print("refuser_tous_les_cookies_button.click()")

        time.sleep(10)

        mon_espace_button = browser.find_element_by_xpath(
            "/html/body/header/nav/div/ul/li[3]/a"
        )
        mon_espace_button.click()
        print('mon_espace_button.click()')

        time.sleep(5)

        identifiant_input = browser.find_element_by_xpath(
            "/html/body/div[1]/div/div[1]/div/form/div[3]/input"
        )
        identifiant_input.send_keys("")
        print("identifiant_input.send_keys()")

        time.sleep(5)

        mot_de_passe_input = browser.find_element_by_xpath(
            "/html/body/div[1]/div/div[1]/div/form/div[4]/input"
        )
        mot_de_passe_input.send_keys("")
        print("mot_de_passe_input.send_keys()")

        time.sleep(5)

        se_connecter_button = browser.find_element_by_xpath(
            "/html/body/div[1]/div/div[1]/div/form/button"
        )
        se_connecter_button.click()
        print('se_connecter_button.click()')

        time.sleep(10)

    #
    def test_send_my_cv_for_one_ad_without_headless(self):
        print("test_send_my_cv_for_one_ad_without_headless")

        time.sleep(5)

        warnings.filterwarnings(
            action="ignore",
            message="unclosed",
            category=ResourceWarning
        )

        time.sleep(5)

        # with Firefox
        browser = webdriver.Firefox(
            executable_path='..\\geckodriver.exe'
        )

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get('')

        time.sleep(15)

        refuser_tous_les_cookies_button = browser.find_element_by_id(
            "onetrust-reject-all-handler"
        )
        refuser_tous_les_cookies_button.click()
        print("refuser_tous_les_cookies_button.click()")

        time.sleep(10)

    #
    def test_send_my_cv_for_one_ad_with_headless(self):
        print("test_send_my_cv_for_one_ad_with_headless")

    #
    def test_send_my_cv_for_several_ads_with_headless_with_web_scraping(self):
        print("test_send_my_cv_for_several_ads_with_headless_with_web_scraping")


if __name__ == '__main__':
    unittest.main()
