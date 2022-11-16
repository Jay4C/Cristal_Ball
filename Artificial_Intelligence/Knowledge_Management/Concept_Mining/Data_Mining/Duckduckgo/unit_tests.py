import time
import unittest
import warnings

import requests
from bs4 import BeautifulSoup
from requests_tor import RequestsTor
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


class UnitTestsDataMiningDuckduckgo(unittest.TestCase):
    def test_extract_the_link_of_the_first_result(self):
        print("test_extract_the_link_of_the_first_result")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        search = "ceo, kingspan group plc"

        url = "https://duckduckgo.com/?q=" + search

        html = requests.get(url=url, headers=headers)

        soup = BeautifulSoup(html.text, 'html.parser')

        if soup.find('div', {'class': 'result'}) is not None:
            website = soup.find_all('div', {'class': 'result'})[0].get('data-domain')
            email = "'info@" + website.replace('www.', '') + "',"

            x = {
                "website": website,
                "email": email
            }

            print("x : " + str(x))

    def test_extract_the_link_of_the_first_result_with_tor(self):
        print("test_extract_the_link_of_the_first_result_with_tor")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        rt = RequestsTor()

        search = "ceo, kingspan group plc"

        url = "https://duckduckgo.com/?q=" + search

        html_with_tor = rt.get(url=url, headers=headers)

        rt.new_id()

        print(html_with_tor.text)

        soup = BeautifulSoup(html_with_tor.text, 'html.parser')

        if soup.find('div', {'class': 'result'}) is not None:
            website = soup.find_all('div', {'class': 'result'})[0].get('data-domain')
            email = "'info@" + website.replace('www.', '') + "',"

            x = {
                "website": website,
                "email": email
            }

            print("x : " + str(x))

    def test_extract_the_link_of_the_first_result_with_selenium(self):
        print("test_extract_the_link_of_the_first_result_with_selenium")

        time.sleep(5)

        search = "ceo, kingspan group plc"

        url = "https://duckduckgo.com/?q=" + search

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(5)

        binary = FirefoxBinary(r"C:\Users\DELL\Desktop\Tor Browser\Browser\firefox.exe")

        profile = FirefoxProfile(r"C:\Users\DELL\Desktop\Tor Browser\Browser\TorBrowser\Data\Browser\profile.default")

        tor_proxy = "127.0.0.1:9150"

        firefox_options = Options()
        firefox_options.headless = True
        firefox_options.add_argument('--proxy-server=socks5://%s' % tor_proxy)
        browser = webdriver.Firefox(firefox_profile=profile, firefox_binary=binary,
                                    executable_path='..\\geckodriver.exe', options=firefox_options)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get(url)
        print("page opened")

        time.sleep(15)

        website = browser.find_element_by_xpath(
            '//*[@id="r1-0"]'
        ).get_attribute('data-domain')

        email = "'info@" + website.replace('www.', '') + "',"

        x = {
            'website': website,
            'email': email
        }

        print('x : ' + str(x))

        browser.close()
        print("browser closed")

        for i1 in range(10):
            browser.service.process.kill()
            browser.service.process.terminate()
            print("browser service process killed : "
                  + str(i1))

        time.sleep(5)


if __name__ == '__main__':
    unittest.main()
