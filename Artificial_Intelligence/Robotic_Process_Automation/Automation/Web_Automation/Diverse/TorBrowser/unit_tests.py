import os
import unittest
import time
import warnings
from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.options import Options


class UnitTestsWebAutomationTorBrowser(unittest.TestCase):
    # ok
    def test_open_one_page_with_tor(self):
        print('test_open_one_page_with_tor')

        time.sleep(5)

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
        browser.get("https://www.whatismyip.com/")
        print("page opened")

        time.sleep(15)

        my_ip = browser.find_element_by_id(
            "ipv6"
        ).text
        print("my_ip : " + str(my_ip))

        time.sleep(5)

        browser.close()


if __name__ == '__main__':
    unittest.main()
