import os
import signal
import subprocess
import unittest
import time
import warnings
from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from requests_tor import RequestsTor
from bs4 import BeautifulSoup
from pywinauto.application import Application
import wmi
import pywinauto.mouse


class UnitTestsWebAutomationYellowPagesCanadaWithDarkWebWithoutHeadless(unittest.TestCase):
    # ok
    def test_insert_the_email_for_one_company_without_headless_with_dark_web(self):
        print('test_insert_the_email_for_one_company_without_headless_with_dark_web')

        time.sleep(5)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(5)

        binary = FirefoxBinary(r"C:\Users\DELL\Desktop\Tor Browser\Browser\firefox.exe")

        profile = FirefoxProfile(r"C:\Users\DELL\Desktop\Tor Browser\Browser\TorBrowser\Data\Browser\profile.default")

        tor_proxy = "127.0.0.1:9150"

        firefox_options = Options()
        # firefox_options.headless = True
        firefox_options.add_argument('--proxy-server=socks5://%s' % tor_proxy)
        browser = webdriver.Firefox(
            firefox_profile=profile,
            firefox_binary=binary,
            executable_path='..\\..\\..\\geckodriver.exe',
            options=firefox_options
        )

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get('https://www.yellowpages.ca/bus/Ontario/Whitby/Ontario-Shores-Centre-for-Mental-Health-'
                    'Sciences/6707729.html?what=Hospital&where=Toronto+ON&useContext=true')

        time.sleep(15)

        # click on the message button
        message_button = browser.find_element_by_xpath(
            "/html/body/div[2]/div[3]/div/div[1]/div[2]/div[1]/div[2]/div[1]/div/ul/li[2]/a"
        )
        message_button.click()

        time.sleep(10)

        # insert the email
        try:
            email_input = browser.find_element_by_xpath(
                '//*[@id="emailMessage"]'
            )
            email_input.clear()
            email_input.send_keys(
                ".@holomorphe.com"
            )
            print("email inserted")
        except Exception as e:
            print('error email inserted : ' + str(e))

        time.sleep(10)

        browser.close()

        subprocess.call("taskkill /F /IM firefox.exe")

        os.system("set ccleaner='C:\\Program Files\\CCleaner\\CCleaner.exe'")

        os.system("start ccleaner /AUTO")

    # ok
    def test_insert_the_email_for_one_company_without_headless_with_clear_web(self):
        print('test_insert_the_email_for_one_company_without_headless_with_clear_web')

        time.sleep(5)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(5)

        firefox_options = Options()
        # firefox_options.headless = True
        browser = webdriver.Firefox(
            executable_path='..\\..\\..\\geckodriver.exe',
            options=firefox_options
        )

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get('https://www.yellowpages.ca/bus/Ontario/Whitby/Ontario-Shores-Centre-for-Mental-Health-'
                    'Sciences/6707729.html?what=Hospital&where=Toronto+ON&useContext=true')

        time.sleep(15)

        # click on the message button
        message_button = browser.find_element_by_xpath(
            "/html/body/div[2]/div[3]/div/div[1]/div[2]/div[1]/div[2]/div[1]/div/ul/li[2]/a"
        )
        message_button.click()

        time.sleep(10)

        # insert the email
        try:
            email_input = browser.find_element_by_xpath(
                '//*[@id="emailMessage"]'
            )
            email_input.clear()
            email_input.send_keys(
                ".@holomorphe.com"
            )
            print("email inserted")
        except Exception as e:
            print('error email inserted : ' + str(e))

        time.sleep(10)

        browser.close()

        subprocess.call("taskkill /F /IM firefox.exe")
        subprocess.call("taskkill /F /IM geckodriver.exe")

        os.system("set ccleaner='C:\\Program Files\\CCleaner\\CCleaner.exe'")

        os.system("start ccleaner /AUTO")

    # ok
    def test_insert_the_first_name_for_one_company_without_headless_with_dark_web(self):
        print('test_insert_the_first_name_for_one_company_without_headless_with_dark_web')

        time.sleep(5)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(5)

        binary = FirefoxBinary(r"C:\Users\DELL\Desktop\Tor Browser\Browser\firefox.exe")

        profile = FirefoxProfile(r"C:\Users\DELL\Desktop\Tor Browser\Browser\TorBrowser\Data\Browser\profile.default")

        tor_proxy = "127.0.0.1:9150"

        firefox_options = Options()
        # firefox_options.headless = True
        firefox_options.add_argument('--proxy-server=socks5://%s' % tor_proxy)
        browser = webdriver.Firefox(
            firefox_profile=profile,
            firefox_binary=binary,
            executable_path='..\\..\\..\\geckodriver.exe',
            options=firefox_options
        )

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get('https://www.yellowpages.ca/bus/Ontario/Whitby/Ontario-Shores-Centre-for-Mental-Health-'
                    'Sciences/6707729.html?what=Hospital&where=Toronto+ON&useContext=true')

        time.sleep(15)

        # click on the message button
        message_button = browser.find_element_by_xpath(
            "/html/body/div[2]/div[3]/div/div[1]/div[2]/div[1]/div[2]/div[1]/div/ul/li[2]/a"
        )
        message_button.click()

        time.sleep(10)

        # insert the first name
        try:
            first_name_input = browser.find_element_by_xpath(
                '//*[@id="firstNameMessage"]'
            )
            first_name_input.clear()
            first_name_input.send_keys(
                ""
            )
            print("first_name_input inserted")
        except Exception as e:
            print('error first_name_input inserted : ' + str(e))

        time.sleep(10)

        browser.close()

    # ok
    def test_insert_the_last_name_for_one_company_without_headless_with_dark_web(self):
        print('test_insert_the_last_name_for_one_company_without_headless_with_dark_web')

        time.sleep(5)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(5)

        binary = FirefoxBinary(r"C:\Users\DELL\Desktop\Tor Browser\Browser\firefox.exe")

        profile = FirefoxProfile(r"C:\Users\DELL\Desktop\Tor Browser\Browser\TorBrowser\Data\Browser\profile.default")

        tor_proxy = "127.0.0.1:9150"

        firefox_options = Options()
        # firefox_options.headless = True
        firefox_options.add_argument('--proxy-server=socks5://%s' % tor_proxy)
        browser = webdriver.Firefox(
            firefox_profile=profile,
            firefox_binary=binary,
            executable_path='..\\..\\..\\geckodriver.exe',
            options=firefox_options
        )

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get('https://www.yellowpages.ca/bus/Ontario/Whitby/Ontario-Shores-Centre-for-Mental-Health-'
                    'Sciences/6707729.html?what=Hospital&where=Toronto+ON&useContext=true')

        time.sleep(15)

        # click on the message button
        message_button = browser.find_element_by_xpath(
            "/html/body/div[2]/div[3]/div/div[1]/div[2]/div[1]/div[2]/div[1]/div/ul/li[2]/a"
        )
        message_button.click()

        time.sleep(10)

        # insert the last name
        try:
            last_name_input = browser.find_element_by_xpath(
                '//*[@id="lastNameMessage"]'
            )
            last_name_input.clear()
            last_name_input.send_keys(
                ""
            )
            print("last_name_input inserted")
        except Exception as e:
            print('error last_name_input inserted : ' + str(e))

        time.sleep(10)

        browser.close()

    # ok
    def test_count_characters_of_the_message(self):
        print('test_count_characters_of_the_message')

        text = "Hello,\n\n" \
            "Firstly, I would like to offer you some computer aided design files with an open source software " \
            "license for building free energy generators for producing electricity without coal, wood, oil, " \
            "fossil fuel, natural gas, biomass, solar energy, wind energy or geothermal energy.\n\n" \
            "Secondly, this kind of electricity generator extracts energy from zero point energy " \
            "field with a magnetic resonance phenomenon and these systems are open thermodynamic systems.\n\n" \
            "After, we can make them operational at any point of the universe, " \
            "and even in a underground facility, a submarine, a boat, a plane and even a satellite.\n\n" \
            "Then, we can find one free energy generator at the following link : " \
            "https://patents.google.com/patent/US20020125774A1/en?oq=US20020125774A1.\n\n" \
            "Best regards,\n\n" \
            "Mr  \n" \
            "CEO of Holomorphe\n" \
            "Headquarter : 31 Avenue de Ségur 75007 Paris\n" \
            "Website : https://www.holomorphe.com/chemical-products/cad-stanley-meyer-water-electrolyser\n" \
            "GitHub : https://github.com/Jay4C/Free-energy-devices"

        if len(text) < 1000:
            print("length text good : " + str(len(text)))
        else:
            print("length text bad : " + str(len(text)))

    # ok
    def test_insert_the_message_for_one_company_without_headless_with_dark_web(self):
        print('test_insert_the_message_for_one_company_without_headless_with_dark_web')

        time.sleep(5)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(5)

        binary = FirefoxBinary(r"C:\Users\DELL\Desktop\Tor Browser\Browser\firefox.exe")

        profile = FirefoxProfile(r"C:\Users\DELL\Desktop\Tor Browser\Browser\TorBrowser\Data\Browser\profile.default")

        tor_proxy = "127.0.0.1:9150"

        firefox_options = Options()
        # firefox_options.headless = True
        firefox_options.add_argument('--proxy-server=socks5://%s' % tor_proxy)
        browser = webdriver.Firefox(
            firefox_profile=profile,
            firefox_binary=binary,
            executable_path='..\\..\\..\\geckodriver.exe',
            options=firefox_options
        )

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get('https://www.yellowpages.ca/bus/Ontario/Whitby/Ontario-Shores-Centre-for-Mental-Health-'
                    'Sciences/6707729.html?what=Hospital&where=Toronto+ON&useContext=true')

        time.sleep(15)

        # click on the message button
        message_button = browser.find_element_by_xpath(
            "/html/body/div[2]/div[3]/div/div[1]/div[2]/div[1]/div[2]/div[1]/div/ul/li[2]/a"
        )
        message_button.click()

        time.sleep(10)

        # insert the message
        try:
            message_input = browser.find_element_by_xpath(
                '//*[@id="contentMessage"]'
            )
            message_input.clear()

            text = "Hello,\n\n" \
                   "Firstly, I would like to offer you some computer aided design files with an open source software " \
                   "license for building free energy generators for producing electricity without coal, wood, oil, " \
                   "fossil fuel, natural gas, biomass, solar energy, wind energy or geothermal energy.\n\n" \
                   "Secondly, this kind of electricity generator extracts energy from zero point energy " \
                   "field with a magnetic resonance phenomenon and these systems are open thermodynamic systems.\n\n" \
                   "After, we can make them operational at any point of the universe, " \
                   "and even in an underground facility, a submarine, a boat, a plane and even a satellite.\n\n" \
                   "Then, we can find one free energy generator at the following link : " \
                   "https://patents.google.com/patent/US20020125774A1/en?oq=US20020125774A1.\n\n" \
                   "Best regards,\n\n" \
                   "Mr  \n" \
                   "CEO of Holomorphe\n" \
                   "Headquarter : 31 Avenue de Ségur 75007 Paris\n" \
                   "Website : https://www.holomorphe.com/chemical-products/cad-stanley-meyer-water-electrolyser\n" \
                   "GitHub : https://github.com/Jay4C/Free-energy-devices"

            message_input.send_keys(
                text
            )
            print("message_input inserted")
        except Exception as e:
            print('error last_name_input inserted : ' + str(e))

        time.sleep(15)

    # ok
    def test_send_a_message_for_one_company_without_headless_with_dark_web(self):
        print("test_send_a_message_for_one_company_without_headless_with_dark_web")

        time.sleep(5)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(5)

        binary = FirefoxBinary(r"C:\Users\DELL\Desktop\Tor Browser\Browser\firefox.exe")

        profile = FirefoxProfile(r"C:\Users\DELL\Desktop\Tor Browser\Browser\TorBrowser\Data\Browser\profile.default")

        tor_proxy = "127.0.0.1:9150"

        firefox_options = Options()
        # firefox_options.headless = True
        firefox_options.add_argument('--proxy-server=socks5://%s' % tor_proxy)
        browser = webdriver.Firefox(
            firefox_profile=profile,
            firefox_binary=binary,
            executable_path='..\\..\\..\\geckodriver.exe',
            options=firefox_options
        )

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get('https://www.yellowpages.ca/bus/Ontario/Toronto/Valu-Mart/4135684.html?what=Grocery+Stores&where=Toronto+ON&useContext=true')
        print('page opened')

        time.sleep(25)

        # click on the message button
        message_button = browser.find_element_by_xpath(
            "/html/body/div[2]/div[3]/div/div[1]/div[2]/div[1]/div[2]/div[1]/div/ul/li[2]/a"
        )
        message_button.click()

        time.sleep(10)

        # insert the email
        try:
            email_input = browser.find_element_by_xpath(
                '//*[@id="emailMessage"]'
            )
            email_input.clear()
            email_input.send_keys(
                ".@holomorphe.com"
            )
            print("email inserted")
        except Exception as e:
            print('error email inserted : ' + str(e))

        time.sleep(10)

        # insert the first name
        try:
            first_name_input = browser.find_element_by_xpath(
                '//*[@id="firstNameMessage"]'
            )
            first_name_input.clear()
            first_name_input.send_keys(
                "Jason"
            )
            print("first_name_input inserted")
        except Exception as e:
            print('error first_name_input inserted : ' + str(e))

        time.sleep(10)

        # insert the last name
        try:
            last_name_input = browser.find_element_by_xpath(
                '//*[@id="lastNameMessage"]'
            )
            last_name_input.clear()
            last_name_input.send_keys(
                ""
            )
            print("last_name_input inserted")
        except Exception as e:
            print('error last_name_input inserted : ' + str(e))

        time.sleep(10)

        # insert the message
        try:
            message_input = browser.find_element_by_xpath(
                '//*[@id="contentMessage"]'
            )
            message_input.clear()

            text = "Hello,\n\n" \
                   "Firstly, I would like to offer you some computer aided design files with an open source software " \
                   "license for building free energy generators for producing electricity without coal, wood, oil, " \
                   "fossil fuel, natural gas, biomass, solar energy, wind energy or geothermal energy.\n\n" \
                   "Secondly, this kind of electricity generator extracts energy from zero point energy " \
                   "field with a magnetic resonance phenomenon and these systems are open thermodynamic systems.\n\n" \
                   "After, we can make them operational at any point of the universe, " \
                   "and even in an underground facility, a submarine, a boat, a plane and even a satellite.\n\n" \
                   "Then, we can find one free energy generator at the following link : " \
                   "https://patents.google.com/patent/US20020125774A1/en?oq=US20020125774A1.\n\n" \
                   "Best regards,\n\n" \
                   "Mr  \n" \
                   "CEO of Holomorphe\n" \
                   "Headquarter : 31 Avenue de Ségur 75007 Paris\n" \
                   "Website : https://www.holomorphe.com/chemical-products/cad-stanley-meyer-water-electrolyser\n" \
                   "GitHub : https://github.com/Jay4C/Free-energy-devices"

            message_input.send_keys(
                text
            )
            print("message_input inserted")
        except Exception as e:
            print('error last_name_input inserted : ' + str(e))

        time.sleep(10)

        # click on the 'send' button
        try:
            n = 3
            actions = ActionChains(browser)
            actions.send_keys(Keys.TAB * n)

            time.sleep(5)

            actions.send_keys(Keys.ENTER)
            actions.perform()

            time.sleep(10)
            print("send button pressed")
        except Exception as e:
            print("error send button : " + str(e))

        time.sleep(10)

        print("ccleaner running")
        os.system("set ccleaner='C:\\Program Files\\CCleaner\\CCleaner.exe'")
        os.system("start ccleaner /AUTO")

        time.sleep(10)

        browser.close()


class UnitTestsWebAutomationYellowPagesCanadaWithDarkWebWithHeadless(unittest.TestCase):
    # ok
    def test_print_the_pid_of_the_process_for_one_company_with_headless_with_dark_web(self):
        print('test_print_the_pid_of_the_process_for_one_company_with_headless_with_dark_web')

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        binary = FirefoxBinary(r"C:\Users\DELL\Desktop\Tor Browser\Browser\firefox.exe")

        profile = FirefoxProfile(r"C:\Users\DELL\Desktop\Tor Browser\Browser\TorBrowser\Data\Browser\profile.default")

        tor_proxy = "127.0.0.1:9150"

        firefox_options = Options()
        firefox_options.headless = True
        firefox_options.add_argument('--proxy-server=socks5://%s' % tor_proxy)
        browser = webdriver.Firefox(
            firefox_profile=profile,
            firefox_binary=binary,
            executable_path='..\\..\\..\\geckodriver.exe',
            options=firefox_options
        )

        # maximize window
        browser.maximize_window()

        time.sleep(10)

        # open
        browser.get('https://www.yellowpages.ca/bus/Ontario/Toronto/Osteo-At-Home/101917660.html'
                    '?what=Hospital&where=Toronto+ON&useContext=true')

        time.sleep(15)
        print("page opened")

        # click on the message button
        message_button = browser.find_element_by_xpath(
            "/html/body/div[2]/div[3]/div/div[1]/div[2]/div[1]/div[2]/div[1]/div/ul/li[2]/a"
        )
        message_button.click()
        print("message_button pressed")

        time.sleep(10)

        # insert the email
        try:
            email_input = browser.find_element_by_xpath(
                '//*[@id="emailMessage"]'
            )
            email_input.clear()
            email_input.send_keys(
                ".@holomorphe.com"
            )
            print("email inserted")
        except Exception as e:
            print('error email inserted : ' + str(e))

        time.sleep(5)

        browser_pid_1 = browser.service.process.pid
        print("browser_pid_1 : " + str(browser_pid_1))

        time.sleep(5)

        browser.close()
        print("browser closed")

        time.sleep(5)

        os.kill(int(browser_pid_1), signal.SIGTERM)
        browser.service.process.kill()
        browser.service.process.terminate()
        print("browser service process killed")

        time.sleep(5)

    # ok
    def test_insert_the_email_for_one_company_with_headless_with_dark_web(self):
        print('test_insert_the_email_for_one_company_with_headless_with_dark_web')

        time.sleep(5)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(5)

        binary = FirefoxBinary(r"C:\Users\DELL\Desktop\Tor Browser\Browser\firefox.exe")

        profile = FirefoxProfile(r"C:\Users\DELL\Desktop\Tor Browser\Browser\TorBrowser\Data\Browser\profile.default")

        tor_proxy = "127.0.0.1:9150"

        firefox_options = Options()
        firefox_options.headless = True
        firefox_options.add_argument('--proxy-server=socks5://%s' % tor_proxy)
        browser = webdriver.Firefox(
            firefox_profile=profile,
            firefox_binary=binary,
            executable_path='..\\..\\..\\geckodriver.exe',
            options=firefox_options
        )

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get('https://www.yellowpages.ca/bus/Ontario/Toronto/Osteo-At-Home/101917660.html'
                    '?what=Hospital&where=Toronto+ON&useContext=true')

        time.sleep(15)

        # click on the message button
        message_button = browser.find_element_by_xpath(
            "/html/body/div[2]/div[3]/div/div[1]/div[2]/div[1]/div[2]/div[1]/div/ul/li[2]/a"
        )
        message_button.click()

        time.sleep(10)

        # insert the email
        try:
            email_input = browser.find_element_by_xpath(
                '//*[@id="emailMessage"]'
            )
            email_input.clear()
            email_input.send_keys(
                ".@holomorphe.com"
            )
            print("email inserted")
        except Exception as e:
            print('error email inserted : ' + str(e))

        time.sleep(10)

        browser.close()

    # ok
    def test_insert_the_first_name_for_one_company_with_headless_with_dark_web(self):
        print('test_insert_the_first_name_for_one_company_with_headless_with_dark_web')

        time.sleep(5)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(5)

        binary = FirefoxBinary(r"C:\Users\DELL\Desktop\Tor Browser\Browser\firefox.exe")

        profile = FirefoxProfile(r"C:\Users\DELL\Desktop\Tor Browser\Browser\TorBrowser\Data\Browser\profile.default")

        tor_proxy = "127.0.0.1:9150"

        firefox_options = Options()
        firefox_options.headless = True
        firefox_options.add_argument('--proxy-server=socks5://%s' % tor_proxy)
        browser = webdriver.Firefox(
            firefox_profile=profile,
            firefox_binary=binary,
            executable_path='..\\..\\..\\geckodriver.exe',
            options=firefox_options
        )

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get('https://www.yellowpages.ca/bus/Ontario/Toronto/Osteo-At-Home/101917660.html'
                    '?what=Hospital&where=Toronto+ON&useContext=true')

        time.sleep(15)

        # click on the message button
        message_button = browser.find_element_by_xpath(
            "/html/body/div[2]/div[3]/div/div[1]/div[2]/div[1]/div[2]/div[1]/div/ul/li[2]/a"
        )
        message_button.click()

        time.sleep(10)

        # insert the first name
        try:
            first_name_input = browser.find_element_by_xpath(
                '//*[@id="firstNameMessage"]'
            )
            first_name_input.clear()
            first_name_input.send_keys(
                ""
            )
            print("first_name_input inserted")
        except Exception as e:
            print('error first_name_input inserted : ' + str(e))

        time.sleep(10)

        browser.close()

    # ok
    def test_insert_the_last_name_for_one_company_with_headless_with_dark_web(self):
        print('test_insert_the_last_name_for_one_company_with_headless_with_dark_web')

        time.sleep(5)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(5)

        binary = FirefoxBinary(r"C:\Users\DELL\Desktop\Tor Browser\Browser\firefox.exe")

        profile = FirefoxProfile(r"C:\Users\DELL\Desktop\Tor Browser\Browser\TorBrowser\Data\Browser\profile.default")

        tor_proxy = "127.0.0.1:9150"

        firefox_options = Options()
        firefox_options.headless = True
        firefox_options.add_argument('--proxy-server=socks5://%s' % tor_proxy)
        browser = webdriver.Firefox(
            firefox_profile=profile,
            firefox_binary=binary,
            executable_path='..\\..\\..\\geckodriver.exe',
            options=firefox_options
        )

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get('https://www.yellowpages.ca/bus/Ontario/Toronto/Osteo-At-Home/101917660.html'
                    '?what=Hospital&where=Toronto+ON&useContext=true')

        time.sleep(15)

        # click on the message button
        message_button = browser.find_element_by_xpath(
            "/html/body/div[2]/div[3]/div/div[1]/div[2]/div[1]/div[2]/div[1]/div/ul/li[2]/a"
        )
        message_button.click()

        time.sleep(10)

        # insert the last name
        try:
            last_name_input = browser.find_element_by_xpath(
                '//*[@id="lastNameMessage"]'
            )
            last_name_input.clear()
            last_name_input.send_keys(
                ""
            )
            print("last_name_input inserted")
        except Exception as e:
            print('error last_name_input inserted : ' + str(e))

        time.sleep(10)

        browser.close()

    # ok
    def test_insert_the_message_for_one_company_with_headless_with_dark_web(self):
        print('test_insert_the_message_for_one_company_with_headless_with_dark_web')

        time.sleep(5)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(5)

        binary = FirefoxBinary(r"C:\Users\DELL\Desktop\Tor Browser\Browser\firefox.exe")

        profile = FirefoxProfile(r"C:\Users\DELL\Desktop\Tor Browser\Browser\TorBrowser\Data\Browser\profile.default")

        tor_proxy = "127.0.0.1:9150"

        firefox_options = Options()
        firefox_options.headless = True
        firefox_options.add_argument('--proxy-server=socks5://%s' % tor_proxy)
        browser = webdriver.Firefox(
            firefox_profile=profile,
            firefox_binary=binary,
            executable_path='..\\..\\..\\geckodriver.exe',
            options=firefox_options
        )

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get('https://www.yellowpages.ca/bus/Ontario/Toronto/Osteo-At-Home/101917660.html'
                    '?what=Hospital&where=Toronto+ON&useContext=true')

        time.sleep(15)

        # click on the message button
        message_button = browser.find_element_by_xpath(
            "/html/body/div[2]/div[3]/div/div[1]/div[2]/div[1]/div[2]/div[1]/div/ul/li[2]/a"
        )
        message_button.click()

        time.sleep(10)

        # insert the message
        try:
            message_input = browser.find_element_by_xpath(
                '//*[@id="contentMessage"]'
            )
            message_input.clear()

            text = "Hello,\n\n" \
                   "Firstly, I would like to offer you some computer aided design files with an open source software " \
                   "license for building free energy generators for producing electricity without coal, wood, oil, " \
                   "fossil fuel, natural gas, biomass, solar energy, wind energy or geothermal energy.\n\n" \
                   "Secondly, this kind of electricity generator extracts energy from zero point energy " \
                   "field with a magnetic resonance phenomenon and these systems are open thermodynamic systems.\n\n" \
                   "After, we can make them operational at any point of the universe, " \
                   "and even in an underground facility, a submarine, a boat, a plane and even a satellite.\n\n" \
                   "Then, we can find one free energy generator at the following link : " \
                   "https://patents.google.com/patent/US20020125774A1/en?oq=US20020125774A1.\n\n" \
                   "Best regards,\n\n" \
                   "Mr  \n" \
                   "CEO of Holomorphe\n" \
                   "Headquarter : 31 Avenue de Ségur 75007 Paris\n" \
                   "Website : https://www.holomorphe.com/chemical-products/cad-stanley-meyer-water-electrolyser\n" \
                   "GitHub : https://github.com/Jay4C/Free-energy-devices"

            message_input.send_keys(
                text
            )
            print("message_input inserted")
        except Exception as e:
            print('error last_name_input inserted : ' + str(e))

        time.sleep(15)

    # ok
    def test_send_a_message_for_one_company_with_headless_with_dark_web(self):
        print("test_send_a_message_for_one_company_with_headless_with_dark_web")

        time.sleep(5)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(5)

        binary = FirefoxBinary(r"C:\Users\DELL\Desktop\Tor Browser\Browser\firefox.exe")

        profile = FirefoxProfile(r"C:\Users\DELL\Desktop\Tor Browser\Browser\TorBrowser\Data\Browser\profile.default")

        tor_proxy = "127.0.0.1:9150"

        firefox_options = Options()
        firefox_options.headless = True
        firefox_options.add_argument('--proxy-server=socks5://%s' % tor_proxy)
        browser = webdriver.Firefox(
            firefox_profile=profile,
            firefox_binary=binary,
            executable_path='..\\..\\..\\geckodriver.exe',
            options=firefox_options
        )

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get('https://www.yellowpages.ca/bus/Ontario/Toronto/The-Goods/100419030.html?what=Grocery+Stores&where=Toronto+ON&useContext=true')
        print('page opened')

        time.sleep(20)

        # click on the message button
        message_button = browser.find_element_by_xpath(
            "/html/body/div[2]/div[3]/div/div[1]/div[2]/div[1]/div[2]/div[1]/div/ul/li[2]/a"
        )
        message_button.click()

        time.sleep(10)

        # insert the email
        try:
            email_input = browser.find_element_by_xpath(
                '//*[@id="emailMessage"]'
            )
            email_input.clear()
            email_input.send_keys(
                ".@holomorphe.com"
            )
            print("email inserted")
        except Exception as e:
            print('error email inserted : ' + str(e))

        time.sleep(10)

        # insert the first name
        try:
            first_name_input = browser.find_element_by_xpath(
                '//*[@id="firstNameMessage"]'
            )
            first_name_input.clear()
            first_name_input.send_keys(
                ""
            )
            print("first_name_input inserted")
        except Exception as e:
            print('error first_name_input inserted : ' + str(e))

        time.sleep(10)

        # insert the last name
        try:
            last_name_input = browser.find_element_by_xpath(
                '//*[@id="lastNameMessage"]'
            )
            last_name_input.clear()
            last_name_input.send_keys(
                ""
            )
            print("last_name_input inserted")
        except Exception as e:
            print('error last_name_input inserted : ' + str(e))

        time.sleep(10)

        # insert the message
        try:
            message_input = browser.find_element_by_xpath(
                '//*[@id="contentMessage"]'
            )
            message_input.clear()

            text = "Hello,\n\n" \
                   "Firstly, I would like to offer you some computer aided design files with an open source software " \
                   "license for building free energy generators for producing electricity without coal, wood, oil, " \
                   "fossil fuel, natural gas, biomass, solar energy, wind energy or geothermal energy.\n\n" \
                   "Secondly, this kind of electricity generator extracts energy from zero point energy " \
                   "field with a magnetic resonance phenomenon and these systems are open thermodynamic systems.\n\n" \
                   "After, we can make them operational at any point of the universe, " \
                   "and even in an underground facility, a submarine, a boat, a plane and even a satellite.\n\n" \
                   "Then, we can find one free energy generator at the following link : " \
                   "https://patents.google.com/patent/US20020125774A1/en?oq=US20020125774A1.\n\n" \
                   "Best regards,\n\n" \
                   "Mr  \n" \
                   "CEO of Holomorphe\n" \
                   "Headquarter : 31 Avenue de Ségur 75007 Paris\n" \
                   "Website : https://www.holomorphe.com/chemical-products/cad-stanley-meyer-water-electrolyser\n" \
                   "GitHub : https://github.com/Jay4C/Free-energy-devices"

            message_input.send_keys(
                text
            )
            print("message_input inserted")
        except Exception as e:
            print('error last_name_input inserted : ' + str(e))

        time.sleep(10)

        # click on the 'send' button
        try:
            n = 3
            actions = ActionChains(browser)
            actions.send_keys(Keys.TAB * n)

            time.sleep(5)

            actions.send_keys(Keys.ENTER)
            actions.perform()

            time.sleep(10)
            print("send button pressed")
        except Exception as e:
            print("error send button : " + str(e))

        time.sleep(10)

        print("ccleaner running")
        os.system("set ccleaner='C:\\Program Files\\CCleaner\\CCleaner.exe'")
        os.system("start ccleaner /AUTO")

        time.sleep(10)

        browser.close()

    # ok
    def test_send_a_message_for_all_companies_from_all_pages_of_results_for_all_activities_and_capitals_with_dark_web_for_rpa(self):
        print('test_send_a_message_for_all_companies_from_all_pages_of_results_for_all_activities_and_capitals_with_dark_web_for_rpa')

        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
            }

            """
            {'id': '1', 'url': 'agence+de+placement'},
            {'id': '2', 'url': 'agence+immobilière'},
            {'id': '3', 'url': "recrutement"},
            {'id': '4', 'url': 'logiciel'},
            {'id': '5', 'url': 'hotel'},
            {'id': '6', 'url': 'social'},
            {'id': '7', 'url': 'nettoyage'},
            {'id': '8', 'url': 'association'},
            {'id': '9', 'url': 'etablissement+financier'},
            {'id': '10', 'url': 'restaurant'}, 
            {'id': '11', 'url': 'batiment'},
            {'id': '12', 'url': 'coiffeur'},
            {'id': '13', 'url': 'fleuriste'},
            {'id': '14', 'url': 'serrurier'},
            {'id': '15', 'url': 'boulangerie'},
            {'id': '16', 'url': 'assurance'},
            {'id': '17', 'url': 'pharmacie'},
            {'id': '18', 'url': 'demenagement'},
            {'id': '19', 'url': 'electricite'},
            {'id': '20', 'url': 'plomberie'},
            {'id': '21', 'url': 'securite'},
            {'id': '22', 'url': 'avocat'},
            {'id': '23', 'url': 'banque'},
            {'id': '24', 'url': 'garage'},
            {'id': '25', 'url': 'dentiste'},
            """

            activites = [
                {'id': '26', 'url': 'docteur'},
            ]

            """
            {'id': '27', 'url': 'comptable'},
            {'id': '28', 'url': 'supermarche'},
            {'id': '29', 'url': 'notaire'},
            {'id': '30', 'url': 'bijoutier'},
            {'id': '31', 'url': 'couturier'},
            {'id': '32', 'url': 'boucherie'},
            {'id': '33', 'url': 'librairie'},
            {'id': '34', 'url': 'architecte'},
            {'id': '36', 'url': 'ciment'},
            {'id': '37', 'url': 'chauffage'},
            {'id': '38', 'url': 'bateau'},
            {'id': '39', 'url': 'climatisation'},
            {'id': '41', 'url': 'acier'},
            {'id': '42', 'url': 'produits+chimiques'},
            {'id': '43', 'url': 'gaz'},
            {'id': '44', 'url': 'achat+or'}
            """

            capitales_du_monde = [
                {'id': '473', 'nom': 'Edmonton+AB', 'pays': 'Canada'}, #edmonton
            ]

            """
            {'id': '474', 'nom': 'Victoria+BC', 'pays': 'Canada'}, #victoria
            {'id': '475', 'nom': 'Winnipeg+MB', 'pays': 'Canada'}, #winnipeg
            {'id': '476', 'nom': 'Fredericton+NB', 'pays': 'Canada'}, #fredericton
            {'id': '477', 'nom': 'Aeroport+De+Saint-Jean-De-Terre-Neuve+St+Johns+NL', 'pays': 'Canada'}, #saint john
            {'id': '478', 'nom': 'Halifax+NS', 'pays': 'Canada'}, #halifax
            {'id': '479', 'nom': 'Yellowknife+NT', 'pays': 'Canada'}, #yellowknife
            {'id': '480', 'nom': 'Iqaluit+NU', 'pays': 'Canada'}, #iqaluit
            {'id': '481', 'nom': 'Toronto+ON', 'pays': 'Canada'}, #toronto
            {'id': '482', 'nom': 'Charlottetown+PE', 'pays': 'Canada'}, #charlottetown
            {'id': '483', 'nom': 'Quebec+QC', 'pays': 'Canada'}, #quebec
            {'id': '484', 'nom': 'Regina+SK', 'pays': 'Canada'}, #regina
            {'id': '485', 'nom': 'Whitehorse+YT', 'pays': 'Canada'} #whitehorse
            """

            for capitale in capitales_du_monde:
                for activite in activites:
                    try:
                        activity = activite.get('url')

                        city = capitale.get('nom')

                        url_search = "https://www.yellowpages.ca/search/si/1/" \
                                     + activity + "/" + city

                        rt = RequestsTor()

                        html_search = rt.get(url_search, headers=headers)

                        rt.new_id()

                        soup_search = BeautifulSoup(html_search.content, 'html.parser')

                        number_of_pages = 0

                        # find the number of pages
                        try:
                            if soup_search.find("span", {"class": "pageCount"}) is not None:
                                try:
                                    if soup_search.find("span", {"class": "pageCount"}).find("span") is not None:
                                        number_of_pages += int(soup_search
                                                               .find("span", {"class": "pageCount"})
                                                               .find_all("span")[1]
                                                               .text)
                                        print("number_of_pages : " + str(number_of_pages))
                                    else:
                                        print("no span")
                                except Exception as e:
                                    print("error span : " + str(e))
                            else:
                                print("no span class pageCount")
                        except Exception as e:
                            print("error span class pageCount : " + str(e))

                        if number_of_pages > 1:
                            for i in range(60, number_of_pages + 1):
                                try:
                                    url_of_one_page_of_results = "https://www.yellowpages.ca/search/si/" \
                                                                 + str(i) + "/" \
                                                                 + activity + "/" \
                                                                 + city

                                    print(url_of_one_page_of_results)

                                    time.sleep(3)

                                    rt = RequestsTor()

                                    html_of_one_page_of_results = rt.get(url_of_one_page_of_results, headers=headers)

                                    rt.new_id()

                                    soup_of_one_page_of_results = BeautifulSoup(html_of_one_page_of_results.content,
                                                                                'html.parser')

                                    try:
                                        if soup_of_one_page_of_results \
                                                .find("div", {"class": "resultList"}) is not None:
                                            try:
                                                if soup_of_one_page_of_results \
                                                        .find("div", {"class": "resultList"}) \
                                                        .find("div", {"class": "listing"}) is not None:

                                                    all_listing = soup_of_one_page_of_results \
                                                        .find("div", {"class": "resultList"}) \
                                                        .find_all("div", {"class": "listing"})

                                                    for listing in all_listing:
                                                        try:
                                                            if listing.find("a", {"class": "listing__name--link"}) is not None:
                                                                website = "https://www.yellowpages.ca" + listing \
                                                                    .find("a", {"class": "listing__name--link"}) \
                                                                    .get("href")

                                                                try:
                                                                    url_1 = website

                                                                    print(url_1)

                                                                    time.sleep(3)

                                                                    rt = RequestsTor()

                                                                    html = rt.get(url_1, headers=headers)

                                                                    rt.new_id()

                                                                    soup = BeautifulSoup(html.content, 'html.parser')

                                                                    if soup.find('li', {
                                                                        'class': 'mlr__item--message'}) is not None:
                                                                        print('yes message button')

                                                                        time.sleep(5)

                                                                        warnings.filterwarnings(action="ignore",
                                                                                                message="unclosed",
                                                                                                category=ResourceWarning)

                                                                        time.sleep(5)

                                                                        binary = FirefoxBinary(
                                                                            r"C:\Users\DELL\Desktop\Tor Browser\Browser\firefox.exe")

                                                                        profile = FirefoxProfile(
                                                                            r"C:\Users\DELL\Desktop\Tor Browser\Browser\TorBrowser\Data\Browser\profile.default")

                                                                        tor_proxy = "127.0.0.1:9150"

                                                                        firefox_options = Options()
                                                                        firefox_options.headless = True
                                                                        firefox_options.add_argument(
                                                                            '--proxy-server=socks5://%s' % tor_proxy)
                                                                        browser = webdriver.Firefox(
                                                                            firefox_profile=profile,
                                                                            firefox_binary=binary,
                                                                            executable_path='geckodriver.exe',
                                                                            options=firefox_options
                                                                        )

                                                                        # maximize window
                                                                        browser.maximize_window()

                                                                        time.sleep(5)

                                                                        # open
                                                                        browser.get(url_1)
                                                                        print('page opened')

                                                                        time.sleep(20)

                                                                        # click on the message button
                                                                        message_button = browser.find_element_by_xpath(
                                                                            "/html/body/div[2]/div[3]/div/div[1]/div[2]/div[1]/div[2]/div[1]/div/ul/li[2]/a"
                                                                        )
                                                                        message_button.click()

                                                                        time.sleep(10)

                                                                        # insert the email
                                                                        try:
                                                                            email_input = browser.find_element_by_xpath(
                                                                                '//*[@id="emailMessage"]'
                                                                            )
                                                                            email_input.clear()
                                                                            email_input.send_keys(
                                                                                ".@holomorphe.com"
                                                                            )
                                                                            print("email inserted")
                                                                        except Exception as e:
                                                                            print('error email inserted : ' + str(e))

                                                                        time.sleep(10)

                                                                        # insert the first name
                                                                        try:
                                                                            first_name_input = browser.find_element_by_xpath(
                                                                                '//*[@id="firstNameMessage"]'
                                                                            )
                                                                            first_name_input.clear()
                                                                            first_name_input.send_keys(
                                                                                ""
                                                                            )
                                                                            print("first_name_input inserted")
                                                                        except Exception as e:
                                                                            print(
                                                                                'error first_name_input inserted : ' + str(
                                                                                    e))

                                                                        time.sleep(10)

                                                                        # insert the last name
                                                                        try:
                                                                            last_name_input = browser.find_element_by_xpath(
                                                                                '//*[@id="lastNameMessage"]'
                                                                            )
                                                                            last_name_input.clear()
                                                                            last_name_input.send_keys(
                                                                                ""
                                                                            )
                                                                            print("last_name_input inserted")
                                                                        except Exception as e:
                                                                            print(
                                                                                'error last_name_input inserted : ' + str(
                                                                                    e))

                                                                        time.sleep(10)

                                                                        # insert the message
                                                                        try:
                                                                            message_input = browser.find_element_by_xpath(
                                                                                '//*[@id="contentMessage"]'
                                                                            )
                                                                            message_input.clear()

                                                                            text = "Hello,\n\n" \
                                                                                   "Firstly, I would like to offer you some computer aided design files with an open source software " \
                                                                                   "license for building free energy generators for producing electricity without coal, wood, oil, " \
                                                                                   "fossil fuel, natural gas, biomass, solar energy, wind energy or geothermal energy.\n\n" \
                                                                                   "Secondly, this kind of electricity generator extracts energy from zero point energy " \
                                                                                   "field with a magnetic resonance phenomenon and these systems are open thermodynamic systems.\n\n" \
                                                                                   "After, we can make them operational at any point of the universe, " \
                                                                                   "and even in an underground facility, a submarine, a boat, a plane and even a satellite.\n\n" \
                                                                                   "Then, we can find one free energy generator at the following link : " \
                                                                                   "https://patents.google.com/patent/US20020125774A1/en?oq=US20020125774A1.\n\n" \
                                                                                   "Best regards,\n\n" \
                                                                                   "Mr \n" \
                                                                                   "CEO of Holomorphe\n" \
                                                                                   "Headquarter : 31 Avenue de Ségur 75007 Paris\n" \
                                                                                   "Website : https://www.holomorphe.com/chemical-products/cad-stanley-meyer-water-electrolyser\n" \
                                                                                   "GitHub : https://github.com/Jay4C/Free-energy-devices"

                                                                            message_input.send_keys(
                                                                                text
                                                                            )
                                                                            print("message_input inserted")
                                                                        except Exception as e:
                                                                            print(
                                                                                'error last_name_input inserted : ' + str(
                                                                                    e))

                                                                        time.sleep(10)

                                                                        # click on the 'send' button
                                                                        try:
                                                                            n = 3
                                                                            actions = ActionChains(browser)
                                                                            actions.send_keys(Keys.TAB * n)

                                                                            time.sleep(5)

                                                                            actions.send_keys(Keys.ENTER)
                                                                            actions.perform()

                                                                            time.sleep(10)
                                                                            print("send button pressed")
                                                                        except Exception as e:
                                                                            print("error send button : " + str(e))

                                                                        time.sleep(30)

                                                                        browser.close()
                                                                        print("browser closed")

                                                                        time.sleep(5)

                                                                        subprocess.call("taskkill /F /IM firefox.exe")
                                                                        app = Application(backend='uia')
                                                                        app.start(
                                                                            "C:\\Users\\DELL\\Desktop\\Tor Browser\\Browser\\firefox.exe")
                                                                        time.sleep(10)
                                                                        pywinauto.mouse.click(button='left',
                                                                                              coords=(900, 50))

                                                                        time.sleep(5)

                                                                        print("ccleaner running")
                                                                        os.system(
                                                                            "set ccleaner='C:\\Program Files\\CCleaner\\CCleaner.exe'")
                                                                        os.system("start ccleaner /AUTO")

                                                                        time.sleep(60)

                                                                        print('\n')
                                                                    else:
                                                                        print('no message button')
                                                                        print('\n')
                                                                except Exception as e:
                                                                    print("error url : " + str(e))

                                                                    time.sleep(5)

                                                                    subprocess.call("taskkill /F /IM firefox.exe")
                                                                    app = Application(backend='uia')
                                                                    app.start(
                                                                        "C:\\Users\\DELL\\Desktop\\Tor Browser\\Browser\\firefox.exe")
                                                                    time.sleep(10)
                                                                    pywinauto.mouse.click(button='left',
                                                                                          coords=(900, 50))

                                                                    time.sleep(5)

                                                                    print("ccleaner running")
                                                                    os.system(
                                                                        "set ccleaner='C:\\Program Files\\CCleaner\\CCleaner.exe'")
                                                                    os.system("start ccleaner /AUTO")

                                                                    time.sleep(60)

                                                                    print('\n')
                                                            else:
                                                                print("no a class listing__name--link")
                                                        except Exception as e:
                                                            print("no a class listing__name--link : " + str(e))
                                                else:
                                                    print("no listing")
                                            except Exception as e:
                                                print("error  : " + str(e))
                                        else:
                                            print("no resultList")
                                    except Exception as e:
                                        print("error div class resultList : " + str(e))
                                except Exception as e:
                                    print("error url_of_one_page_of_results : " + str(e))
                        else:
                            try:
                                url_of_one_page_of_results = "https://www.yellowpages.ca/search/si/1/" \
                                                             + activity + "/" \
                                                             + city

                                print(url_of_one_page_of_results)

                                time.sleep(3)

                                rt = RequestsTor()

                                html_of_one_page_of_results = rt.get(url_of_one_page_of_results, headers=headers)

                                rt.new_id()

                                soup_of_one_page_of_results = BeautifulSoup(html_of_one_page_of_results.content,
                                                                            'html.parser')

                                try:
                                    if soup_of_one_page_of_results \
                                            .find("div", {"class": "resultList"}) is not None:
                                        try:
                                            if soup_of_one_page_of_results \
                                                    .find("div", {"class": "resultList"}) \
                                                    .find("div", {"class": "listing"}) is not None:

                                                all_listing = soup_of_one_page_of_results \
                                                    .find("div", {"class": "resultList"}) \
                                                    .find_all("div", {"class": "listing"})

                                                for listing in all_listing:
                                                    try:
                                                        if listing.find("a", {"class": "listing__name--link"}) is not None:
                                                            website = "https://www.yellowpages.ca" + listing \
                                                                .find("a", {"class": "listing__name--link"}) \
                                                                .get("href")

                                                            try:
                                                                url_2 = website

                                                                print(url_2)

                                                                time.sleep(3)

                                                                rt = RequestsTor()

                                                                html = rt.get(url_2, headers=headers)

                                                                rt.new_id()

                                                                soup = BeautifulSoup(html.content, 'html.parser')

                                                                if soup.find('li', {'class': 'mlr__item--message'}) is not None:
                                                                    print('yes message button')

                                                                    time.sleep(5)

                                                                    warnings.filterwarnings(action="ignore",
                                                                                            message="unclosed",
                                                                                            category=ResourceWarning)

                                                                    time.sleep(5)

                                                                    binary = FirefoxBinary(
                                                                        r"C:\Users\DELL\Desktop\Tor Browser\Browser\firefox.exe")

                                                                    profile = FirefoxProfile(
                                                                        r"C:\Users\DELL\Desktop\Tor Browser\Browser\TorBrowser\Data\Browser\profile.default")

                                                                    tor_proxy = "127.0.0.1:9150"

                                                                    firefox_options = Options()
                                                                    firefox_options.headless = True
                                                                    firefox_options.add_argument(
                                                                        '--proxy-server=socks5://%s' % tor_proxy)
                                                                    browser = webdriver.Firefox(
                                                                        firefox_profile=profile,
                                                                        firefox_binary=binary,
                                                                        executable_path='geckodriver.exe',
                                                                        options=firefox_options
                                                                    )

                                                                    # maximize window
                                                                    browser.maximize_window()

                                                                    time.sleep(5)

                                                                    # open
                                                                    browser.get(url_2)
                                                                    print('page opened')

                                                                    time.sleep(20)

                                                                    # click on the message button
                                                                    message_button = browser.find_element_by_xpath(
                                                                        "/html/body/div[2]/div[3]/div/div[1]/div[2]/div[1]/div[2]/div[1]/div/ul/li[2]/a"
                                                                    )
                                                                    message_button.click()

                                                                    time.sleep(10)

                                                                    # insert the email
                                                                    try:
                                                                        email_input = browser.find_element_by_xpath(
                                                                            '//*[@id="emailMessage"]'
                                                                        )
                                                                        email_input.clear()
                                                                        email_input.send_keys(
                                                                            ".@holomorphe.com"
                                                                        )
                                                                        print("email inserted")
                                                                    except Exception as e:
                                                                        print('error email inserted : ' + str(e))

                                                                    time.sleep(10)

                                                                    # insert the first name
                                                                    try:
                                                                        first_name_input = browser.find_element_by_xpath(
                                                                            '//*[@id="firstNameMessage"]'
                                                                        )
                                                                        first_name_input.clear()
                                                                        first_name_input.send_keys(
                                                                            ""
                                                                        )
                                                                        print("first_name_input inserted")
                                                                    except Exception as e:
                                                                        print(
                                                                            'error first_name_input inserted : ' + str(
                                                                                e))

                                                                    time.sleep(10)

                                                                    # insert the last name
                                                                    try:
                                                                        last_name_input = browser.find_element_by_xpath(
                                                                            '//*[@id="lastNameMessage"]'
                                                                        )
                                                                        last_name_input.clear()
                                                                        last_name_input.send_keys(
                                                                            ""
                                                                        )
                                                                        print("last_name_input inserted")
                                                                    except Exception as e:
                                                                        print('error last_name_input inserted : ' + str(
                                                                            e))

                                                                    time.sleep(10)

                                                                    # insert the message
                                                                    try:
                                                                        message_input = browser.find_element_by_xpath(
                                                                            '//*[@id="contentMessage"]'
                                                                        )
                                                                        message_input.clear()

                                                                        text = "Hello,\n\n" \
                                                                               "Firstly, I would like to offer you some computer aided design files with an open source software " \
                                                                               "license for building free energy generators for producing electricity without coal, wood, oil, " \
                                                                               "fossil fuel, natural gas, biomass, solar energy, wind energy or geothermal energy.\n\n" \
                                                                               "Secondly, this kind of electricity generator extracts energy from zero point energy " \
                                                                               "field with a magnetic resonance phenomenon and these systems are open thermodynamic systems.\n\n" \
                                                                               "After, we can make them operational at any point of the universe, " \
                                                                               "and even in an underground facility, a submarine, a boat, a plane and even a satellite.\n\n" \
                                                                               "Then, we can find one free energy generator at the following link : " \
                                                                               "https://patents.google.com/patent/US20020125774A1/en?oq=US20020125774A1.\n\n" \
                                                                               "Best regards,\n\n" \
                                                                               "Mr \n" \
                                                                               "CEO of Holomorphe\n" \
                                                                               "Headquarter : 31 Avenue de Ségur 75007 Paris\n" \
                                                                               "Website : https://www.holomorphe.com/chemical-products/cad-stanley-meyer-water-electrolyser\n" \
                                                                               "GitHub : https://github.com/Jay4C/Free-energy-devices"

                                                                        message_input.send_keys(
                                                                            text
                                                                        )
                                                                        print("message_input inserted")
                                                                    except Exception as e:
                                                                        print('error last_name_input inserted : ' + str(
                                                                            e))

                                                                    time.sleep(10)

                                                                    # click on the 'send' button
                                                                    try:
                                                                        n = 3
                                                                        actions = ActionChains(browser)
                                                                        actions.send_keys(Keys.TAB * n)

                                                                        time.sleep(5)

                                                                        actions.send_keys(Keys.ENTER)
                                                                        actions.perform()

                                                                        time.sleep(10)
                                                                        print("send button pressed")
                                                                    except Exception as e:
                                                                        print("error send button : " + str(e))

                                                                    time.sleep(30)

                                                                    browser.close()
                                                                    print("browser closed")

                                                                    time.sleep(5)

                                                                    subprocess.call("taskkill /F /IM firefox.exe")
                                                                    app = Application(backend='uia')
                                                                    app.start("C:\\Users\\DELL\\Desktop\\Tor Browser\\Browser\\firefox.exe")
                                                                    time.sleep(10)
                                                                    pywinauto.mouse.click(button='left',
                                                                                          coords=(900, 50))

                                                                    time.sleep(5)

                                                                    print("ccleaner running")
                                                                    os.system(
                                                                        "set ccleaner='C:\\Program Files\\CCleaner\\CCleaner.exe'")
                                                                    os.system("start ccleaner /AUTO")

                                                                    time.sleep(60)

                                                                    print('\n')
                                                                else:
                                                                    print('no message button')
                                                                    print('\n')
                                                            except Exception as e:
                                                                print("error url : " + str(e))

                                                                time.sleep(5)

                                                                subprocess.call("taskkill /F /IM firefox.exe")
                                                                app = Application(backend='uia')
                                                                app.start(
                                                                    "C:\\Users\\DELL\\Desktop\\Tor Browser\\Browser\\firefox.exe")
                                                                time.sleep(10)
                                                                pywinauto.mouse.click(button='left',
                                                                                      coords=(900, 50))

                                                                time.sleep(5)

                                                                print("ccleaner running")
                                                                os.system(
                                                                    "set ccleaner='C:\\Program Files\\CCleaner\\CCleaner.exe'")
                                                                os.system("start ccleaner /AUTO")

                                                                time.sleep(60)

                                                                print('\n')
                                                        else:
                                                            print("no a class listing__name--link")
                                                    except Exception as e:
                                                        print("no a class listing__name--link : " + str(e))
                                            else:
                                                print("no listing")
                                        except Exception as e:
                                            print("error  : " + str(e))
                                    else:
                                        print("no resultList")
                                except Exception as e:
                                    print("error div class resultList : " + str(e))
                            except Exception as e:
                                print("error url_of_one_page_of_results : " + str(e))
                    except Exception as e:
                        print("error url_search : " + str(e))
        finally:
            print('done')

    # ok
    def test_send_a_message_for_all_companies_from_all_pages_of_results_for_all_activities_and_capitals_with_clear_web_for_rpa(self):
        print('test_send_a_message_for_all_companies_from_all_pages_of_results_for_all_activities_and_capitals_with_dark_web_for_rpa')

        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
            }

            """
            {'id': '1', 'url': 'agence+de+placement'},
            {'id': '2', 'url': 'agence+immobilière'},
            {'id': '3', 'url': "recrutement"},
            {'id': '4', 'url': 'logiciel'},
            {'id': '5', 'url': 'hotel'},
            {'id': '6', 'url': 'social'},
            {'id': '7', 'url': 'nettoyage'},
            {'id': '8', 'url': 'association'},
            {'id': '9', 'url': 'etablissement+financier'},
            {'id': '10', 'url': 'restaurant'}, 
            {'id': '11', 'url': 'batiment'},
            {'id': '12', 'url': 'coiffeur'},
            {'id': '13', 'url': 'fleuriste'},
            {'id': '14', 'url': 'serrurier'},
            {'id': '15', 'url': 'boulangerie'},
            {'id': '16', 'url': 'assurance'},
            {'id': '17', 'url': 'pharmacie'},
            {'id': '18', 'url': 'demenagement'},
            {'id': '19', 'url': 'electricite'},
            {'id': '20', 'url': 'plomberie'},
            {'id': '21', 'url': 'securite'},
            {'id': '22', 'url': 'avocat'},
            {'id': '23', 'url': 'banque'},
            {'id': '24', 'url': 'garage'},
            {'id': '25', 'url': 'dentiste'},
            """

            activites = [
                {'id': '26', 'url': 'docteur'},
            ]

            """
            {'id': '27', 'url': 'comptable'},
            {'id': '28', 'url': 'supermarche'},
            {'id': '29', 'url': 'notaire'},
            {'id': '30', 'url': 'bijoutier'},
            {'id': '31', 'url': 'couturier'},
            {'id': '32', 'url': 'boucherie'},
            {'id': '33', 'url': 'librairie'},
            {'id': '34', 'url': 'architecte'},
            {'id': '36', 'url': 'ciment'},
            {'id': '37', 'url': 'chauffage'},
            {'id': '38', 'url': 'bateau'},
            {'id': '39', 'url': 'climatisation'},
            {'id': '41', 'url': 'acier'},
            {'id': '42', 'url': 'produits+chimiques'},
            {'id': '43', 'url': 'gaz'},
            {'id': '44', 'url': 'achat+or'}
            """

            capitales_du_monde = [
                {'id': '473', 'nom': 'Edmonton+AB', 'pays': 'Canada'}, #edmonton
            ]

            """
            {'id': '474', 'nom': 'Victoria+BC', 'pays': 'Canada'}, #victoria
            {'id': '475', 'nom': 'Winnipeg+MB', 'pays': 'Canada'}, #winnipeg
            {'id': '476', 'nom': 'Fredericton+NB', 'pays': 'Canada'}, #fredericton
            {'id': '477', 'nom': 'Aeroport+De+Saint-Jean-De-Terre-Neuve+St+Johns+NL', 'pays': 'Canada'}, #saint john
            {'id': '478', 'nom': 'Halifax+NS', 'pays': 'Canada'}, #halifax
            {'id': '479', 'nom': 'Yellowknife+NT', 'pays': 'Canada'}, #yellowknife
            {'id': '480', 'nom': 'Iqaluit+NU', 'pays': 'Canada'}, #iqaluit
            {'id': '481', 'nom': 'Toronto+ON', 'pays': 'Canada'}, #toronto
            {'id': '482', 'nom': 'Charlottetown+PE', 'pays': 'Canada'}, #charlottetown
            {'id': '483', 'nom': 'Quebec+QC', 'pays': 'Canada'}, #quebec
            {'id': '484', 'nom': 'Regina+SK', 'pays': 'Canada'}, #regina
            {'id': '485', 'nom': 'Whitehorse+YT', 'pays': 'Canada'} #whitehorse
            """

            for capitale in capitales_du_monde:
                for activite in activites:
                    try:
                        activity = activite.get('url')

                        city = capitale.get('nom')

                        url_search = "https://www.yellowpages.ca/search/si/1/" \
                                     + activity + "/" + city

                        rt = RequestsTor()

                        html_search = rt.get(url_search, headers=headers)

                        rt.new_id()

                        soup_search = BeautifulSoup(html_search.content, 'html.parser')

                        number_of_pages = 0

                        # find the number of pages
                        try:
                            if soup_search.find("span", {"class": "pageCount"}) is not None:
                                try:
                                    if soup_search.find("span", {"class": "pageCount"}).find("span") is not None:
                                        number_of_pages += int(soup_search
                                                               .find("span", {"class": "pageCount"})
                                                               .find_all("span")[1]
                                                               .text)
                                        print("number_of_pages : " + str(number_of_pages))
                                    else:
                                        print("no span")
                                except Exception as e:
                                    print("error span : " + str(e))
                            else:
                                print("no span class pageCount")
                        except Exception as e:
                            print("error span class pageCount : " + str(e))

                        if number_of_pages > 1:
                            for i in range(60, number_of_pages + 1):
                                try:
                                    url_of_one_page_of_results = "https://www.yellowpages.ca/search/si/" \
                                                                 + str(i) + "/" \
                                                                 + activity + "/" \
                                                                 + city

                                    print(url_of_one_page_of_results)

                                    time.sleep(3)

                                    rt = RequestsTor()

                                    html_of_one_page_of_results = rt.get(url_of_one_page_of_results, headers=headers)

                                    rt.new_id()

                                    soup_of_one_page_of_results = BeautifulSoup(html_of_one_page_of_results.content,
                                                                                'html.parser')

                                    try:
                                        if soup_of_one_page_of_results \
                                                .find("div", {"class": "resultList"}) is not None:
                                            try:
                                                if soup_of_one_page_of_results \
                                                        .find("div", {"class": "resultList"}) \
                                                        .find("div", {"class": "listing"}) is not None:

                                                    all_listing = soup_of_one_page_of_results \
                                                        .find("div", {"class": "resultList"}) \
                                                        .find_all("div", {"class": "listing"})

                                                    for listing in all_listing:
                                                        try:
                                                            if listing.find("a", {"class": "listing__name--link"}) is not None:
                                                                website = "https://www.yellowpages.ca" + listing \
                                                                    .find("a", {"class": "listing__name--link"}) \
                                                                    .get("href")

                                                                try:
                                                                    url_1 = website

                                                                    print(url_1)

                                                                    time.sleep(3)

                                                                    rt = RequestsTor()

                                                                    html = rt.get(url_1, headers=headers)

                                                                    rt.new_id()

                                                                    soup = BeautifulSoup(html.content, 'html.parser')

                                                                    if soup.find('li', {
                                                                        'class': 'mlr__item--message'}) is not None:
                                                                        print('yes message button')

                                                                        time.sleep(5)

                                                                        warnings.filterwarnings(action="ignore",
                                                                                                message="unclosed",
                                                                                                category=ResourceWarning)

                                                                        time.sleep(5)

                                                                        firefox_options = Options()
                                                                        firefox_options.headless = True
                                                                        browser = webdriver.Firefox(
                                                                            executable_path='..\\..\\..\\geckodriver.exe',
                                                                            options=firefox_options
                                                                        )

                                                                        # maximize window
                                                                        browser.maximize_window()

                                                                        time.sleep(5)

                                                                        # open
                                                                        browser.get(url_1)
                                                                        print('page opened')

                                                                        time.sleep(20)

                                                                        # click on the message button
                                                                        message_button = browser.find_element_by_xpath(
                                                                            "/html/body/div[2]/div[3]/div/div[1]/div[2]/div[1]/div[2]/div[1]/div/ul/li[2]/a"
                                                                        )
                                                                        message_button.click()

                                                                        time.sleep(10)

                                                                        # insert the email
                                                                        try:
                                                                            email_input = browser.find_element_by_xpath(
                                                                                '//*[@id="emailMessage"]'
                                                                            )
                                                                            email_input.clear()
                                                                            email_input.send_keys(
                                                                                ".@holomorphe.com"
                                                                            )
                                                                            print("email inserted")
                                                                        except Exception as e:
                                                                            print('error email inserted : ' + str(e))

                                                                        time.sleep(10)

                                                                        # insert the first name
                                                                        try:
                                                                            first_name_input = browser.find_element_by_xpath(
                                                                                '//*[@id="firstNameMessage"]'
                                                                            )
                                                                            first_name_input.clear()
                                                                            first_name_input.send_keys(
                                                                                ""
                                                                            )
                                                                            print("first_name_input inserted")
                                                                        except Exception as e:
                                                                            print(
                                                                                'error first_name_input inserted : ' + str(
                                                                                    e))

                                                                        time.sleep(10)

                                                                        # insert the last name
                                                                        try:
                                                                            last_name_input = browser.find_element_by_xpath(
                                                                                '//*[@id="lastNameMessage"]'
                                                                            )
                                                                            last_name_input.clear()
                                                                            last_name_input.send_keys(
                                                                                ""
                                                                            )
                                                                            print("last_name_input inserted")
                                                                        except Exception as e:
                                                                            print(
                                                                                'error last_name_input inserted : ' + str(
                                                                                    e))

                                                                        time.sleep(10)

                                                                        # insert the message
                                                                        try:
                                                                            message_input = browser.find_element_by_xpath(
                                                                                '//*[@id="contentMessage"]'
                                                                            )
                                                                            message_input.clear()

                                                                            text = "Hello,\n\n" \
                                                                                   "Firstly, I would like to offer you some computer aided design files with an open source software " \
                                                                                   "license for building free energy generators for producing electricity without coal, wood, oil, " \
                                                                                   "fossil fuel, natural gas, biomass, solar energy, wind energy or geothermal energy.\n\n" \
                                                                                   "Secondly, this kind of electricity generator extracts energy from zero point energy " \
                                                                                   "field with a magnetic resonance phenomenon and these systems are open thermodynamic systems.\n\n" \
                                                                                   "After, we can make them operational at any point of the universe, " \
                                                                                   "and even in an underground facility, a submarine, a boat, a plane and even a satellite.\n\n" \
                                                                                   "Then, we can find one free energy generator at the following link : " \
                                                                                   "https://patents.google.com/patent/US20020125774A1/en?oq=US20020125774A1.\n\n" \
                                                                                   "Best regards,\n\n" \
                                                                                   "Mr  \n" \
                                                                                   "CEO of Holomorphe\n" \
                                                                                   "Headquarter : 31 Avenue de Ségur 75007 Paris\n" \
                                                                                   "Website : https://www.holomorphe.com/chemical-products/cad-stanley-meyer-water-electrolyser\n" \
                                                                                   "GitHub : https://github.com/Jay4C/Free-energy-devices"

                                                                            message_input.send_keys(
                                                                                text
                                                                            )
                                                                            print("message_input inserted")
                                                                        except Exception as e:
                                                                            print(
                                                                                'error last_name_input inserted : ' + str(
                                                                                    e))

                                                                        time.sleep(10)

                                                                        # click on the 'send' button
                                                                        try:
                                                                            n = 3
                                                                            actions = ActionChains(browser)
                                                                            actions.send_keys(Keys.TAB * n)

                                                                            time.sleep(5)

                                                                            actions.send_keys(Keys.ENTER)
                                                                            actions.perform()

                                                                            time.sleep(10)
                                                                            print("send button pressed")
                                                                        except Exception as e:
                                                                            print("error send button : " + str(e))

                                                                        time.sleep(30)

                                                                        browser.close()
                                                                        print("browser closed")

                                                                        time.sleep(5)

                                                                        subprocess.call("taskkill /F /IM geckodriver.exe")
                                                                        subprocess.call("taskkill /F /IM firefox.exe")

                                                                        time.sleep(10)

                                                                        app = Application(backend='uia')
                                                                        app.start(
                                                                            "C:\\Users\\DELL\\Desktop\\Tor Browser\\Browser\\firefox.exe")
                                                                        time.sleep(10)
                                                                        pywinauto.mouse.click(button='left',
                                                                                              coords=(900, 50))

                                                                        time.sleep(5)

                                                                        print("ccleaner running")
                                                                        os.system(
                                                                            "set ccleaner='C:\\Program Files\\CCleaner\\CCleaner.exe'")
                                                                        os.system("start ccleaner /AUTO")

                                                                        time.sleep(60)

                                                                        print('\n')
                                                                    else:
                                                                        print('no message button')
                                                                        print('\n')
                                                                except Exception as e:
                                                                    print("error url : " + str(e))

                                                                    time.sleep(5)

                                                                    subprocess.call("taskkill /F /IM geckodriver.exe")
                                                                    subprocess.call("taskkill /F /IM firefox.exe")

                                                                    time.sleep(10)

                                                                    app = Application(backend='uia')
                                                                    app.start(
                                                                        "C:\\Users\\DELL\\Desktop\\Tor Browser\\Browser\\firefox.exe")
                                                                    time.sleep(10)
                                                                    pywinauto.mouse.click(button='left',
                                                                                          coords=(900, 50))

                                                                    time.sleep(5)

                                                                    print("ccleaner running")
                                                                    os.system(
                                                                        "set ccleaner='C:\\Program Files\\CCleaner\\CCleaner.exe'")
                                                                    os.system("start ccleaner /AUTO")

                                                                    time.sleep(60)

                                                                    print('\n')
                                                            else:
                                                                print("no a class listing__name--link")
                                                        except Exception as e:
                                                            print("no a class listing__name--link : " + str(e))
                                                else:
                                                    print("no listing")
                                            except Exception as e:
                                                print("error  : " + str(e))
                                        else:
                                            print("no resultList")
                                    except Exception as e:
                                        print("error div class resultList : " + str(e))
                                except Exception as e:
                                    print("error url_of_one_page_of_results : " + str(e))
                        else:
                            try:
                                url_of_one_page_of_results = "https://www.yellowpages.ca/search/si/1/" \
                                                             + activity + "/" \
                                                             + city

                                print(url_of_one_page_of_results)

                                time.sleep(3)

                                rt = RequestsTor()

                                html_of_one_page_of_results = rt.get(url_of_one_page_of_results, headers=headers)

                                rt.new_id()

                                soup_of_one_page_of_results = BeautifulSoup(html_of_one_page_of_results.content,
                                                                            'html.parser')

                                try:
                                    if soup_of_one_page_of_results \
                                            .find("div", {"class": "resultList"}) is not None:
                                        try:
                                            if soup_of_one_page_of_results \
                                                    .find("div", {"class": "resultList"}) \
                                                    .find("div", {"class": "listing"}) is not None:

                                                all_listing = soup_of_one_page_of_results \
                                                    .find("div", {"class": "resultList"}) \
                                                    .find_all("div", {"class": "listing"})

                                                for listing in all_listing:
                                                    try:
                                                        if listing.find("a", {"class": "listing__name--link"}) is not None:
                                                            website = "https://www.yellowpages.ca" + listing \
                                                                .find("a", {"class": "listing__name--link"}) \
                                                                .get("href")

                                                            try:
                                                                url_2 = website

                                                                print(url_2)

                                                                time.sleep(3)

                                                                rt = RequestsTor()

                                                                html = rt.get(url_2, headers=headers)

                                                                rt.new_id()

                                                                soup = BeautifulSoup(html.content, 'html.parser')

                                                                if soup.find('li', {'class': 'mlr__item--message'}) is not None:
                                                                    print('yes message button')

                                                                    time.sleep(5)

                                                                    warnings.filterwarnings(action="ignore",
                                                                                            message="unclosed",
                                                                                            category=ResourceWarning)

                                                                    time.sleep(5)

                                                                    firefox_options = Options()
                                                                    firefox_options.headless = True
                                                                    browser = webdriver.Firefox(
                                                                        executable_path='..\\..\\..\\geckodriver.exe',
                                                                        options=firefox_options
                                                                    )

                                                                    # maximize window
                                                                    browser.maximize_window()

                                                                    time.sleep(5)

                                                                    # open
                                                                    browser.get(url_2)
                                                                    print('page opened')

                                                                    time.sleep(20)

                                                                    # click on the message button
                                                                    message_button = browser.find_element_by_xpath(
                                                                        "/html/body/div[2]/div[3]/div/div[1]/div[2]/div[1]/div[2]/div[1]/div/ul/li[2]/a"
                                                                    )
                                                                    message_button.click()

                                                                    time.sleep(10)

                                                                    # insert the email
                                                                    try:
                                                                        email_input = browser.find_element_by_xpath(
                                                                            '//*[@id="emailMessage"]'
                                                                        )
                                                                        email_input.clear()
                                                                        email_input.send_keys(
                                                                            ".@holomorphe.com"
                                                                        )
                                                                        print("email inserted")
                                                                    except Exception as e:
                                                                        print('error email inserted : ' + str(e))

                                                                    time.sleep(10)

                                                                    # insert the first name
                                                                    try:
                                                                        first_name_input = browser.find_element_by_xpath(
                                                                            '//*[@id="firstNameMessage"]'
                                                                        )
                                                                        first_name_input.clear()
                                                                        first_name_input.send_keys(
                                                                            ""
                                                                        )
                                                                        print("first_name_input inserted")
                                                                    except Exception as e:
                                                                        print(
                                                                            'error first_name_input inserted : ' + str(
                                                                                e))

                                                                    time.sleep(10)

                                                                    # insert the last name
                                                                    try:
                                                                        last_name_input = browser.find_element_by_xpath(
                                                                            '//*[@id="lastNameMessage"]'
                                                                        )
                                                                        last_name_input.clear()
                                                                        last_name_input.send_keys(
                                                                            ""
                                                                        )
                                                                        print("last_name_input inserted")
                                                                    except Exception as e:
                                                                        print('error last_name_input inserted : ' + str(
                                                                            e))

                                                                    time.sleep(10)

                                                                    # insert the message
                                                                    try:
                                                                        message_input = browser.find_element_by_xpath(
                                                                            '//*[@id="contentMessage"]'
                                                                        )
                                                                        message_input.clear()

                                                                        text = "Hello,\n\n" \
                                                                               "Firstly, I would like to offer you some computer aided design files with an open source software " \
                                                                               "license for building free energy generators for producing electricity without coal, wood, oil, " \
                                                                               "fossil fuel, natural gas, biomass, solar energy, wind energy or geothermal energy.\n\n" \
                                                                               "Secondly, this kind of electricity generator extracts energy from zero point energy " \
                                                                               "field with a magnetic resonance phenomenon and these systems are open thermodynamic systems.\n\n" \
                                                                               "After, we can make them operational at any point of the universe, " \
                                                                               "and even in an underground facility, a submarine, a boat, a plane and even a satellite.\n\n" \
                                                                               "Then, we can find one free energy generator at the following link : " \
                                                                               "https://patents.google.com/patent/US20020125774A1/en?oq=US20020125774A1.\n\n" \
                                                                               "Best regards,\n\n" \
                                                                               "Mr  \n" \
                                                                               "CEO of Holomorphe\n" \
                                                                               "Headquarter : 31 Avenue de Ségur 75007 Paris\n" \
                                                                               "Website : https://www.holomorphe.com/chemical-products/cad-stanley-meyer-water-electrolyser\n" \
                                                                               "GitHub : https://github.com/Jay4C/Free-energy-devices"

                                                                        message_input.send_keys(
                                                                            text
                                                                        )
                                                                        print("message_input inserted")
                                                                    except Exception as e:
                                                                        print('error last_name_input inserted : ' + str(
                                                                            e))

                                                                    time.sleep(10)

                                                                    # click on the 'send' button
                                                                    try:
                                                                        n = 3
                                                                        actions = ActionChains(browser)
                                                                        actions.send_keys(Keys.TAB * n)

                                                                        time.sleep(5)

                                                                        actions.send_keys(Keys.ENTER)
                                                                        actions.perform()

                                                                        time.sleep(10)
                                                                        print("send button pressed")
                                                                    except Exception as e:
                                                                        print("error send button : " + str(e))

                                                                    time.sleep(30)

                                                                    browser.close()
                                                                    print("browser closed")

                                                                    time.sleep(5)

                                                                    subprocess.call("taskkill /F /IM geckodriver.exe")
                                                                    subprocess.call("taskkill /F /IM firefox.exe")

                                                                    time.sleep(10)

                                                                    app = Application(backend='uia')
                                                                    app.start(
                                                                        "C:\\Users\\DELL\\Desktop\\Tor Browser\\Browser\\firefox.exe")
                                                                    time.sleep(10)
                                                                    pywinauto.mouse.click(button='left',
                                                                                          coords=(900, 50))

                                                                    time.sleep(5)

                                                                    print("ccleaner running")
                                                                    os.system(
                                                                        "set ccleaner='C:\\Program Files\\CCleaner\\CCleaner.exe'")
                                                                    os.system("start ccleaner /AUTO")

                                                                    time.sleep(60)

                                                                    print('\n')
                                                                else:
                                                                    print('no message button')
                                                                    print('\n')
                                                            except Exception as e:
                                                                print("error url : " + str(e))

                                                                time.sleep(5)

                                                                subprocess.call("taskkill /F /IM geckodriver.exe")
                                                                subprocess.call("taskkill /F /IM firefox.exe")

                                                                time.sleep(10)

                                                                app = Application(backend='uia')
                                                                app.start(
                                                                    "C:\\Users\\DELL\\Desktop\\Tor Browser\\Browser\\firefox.exe")
                                                                time.sleep(10)
                                                                pywinauto.mouse.click(button='left',
                                                                                      coords=(900, 50))

                                                                time.sleep(5)

                                                                print("ccleaner running")
                                                                os.system(
                                                                    "set ccleaner='C:\\Program Files\\CCleaner\\CCleaner.exe'")
                                                                os.system("start ccleaner /AUTO")

                                                                time.sleep(60)

                                                                print('\n')
                                                        else:
                                                            print("no a class listing__name--link")
                                                    except Exception as e:
                                                        print("no a class listing__name--link : " + str(e))
                                            else:
                                                print("no listing")
                                        except Exception as e:
                                            print("error  : " + str(e))
                                    else:
                                        print("no resultList")
                                except Exception as e:
                                    print("error div class resultList : " + str(e))
                            except Exception as e:
                                print("error url_of_one_page_of_results : " + str(e))
                    except Exception as e:
                        print("error url_search : " + str(e))
        finally:
            print('done')

    # ok
    def test_kill_firefox_process_1(self):
        print('test_kill_firefox_process')
        subprocess.call("taskkill /F /IM firefox.exe")
        app = Application(backend='uia')
        app.start("C:\\Users\\DELL\\Desktop\\Tor Browser\\Browser\\firefox.exe")
        time.sleep(10)
        pywinauto.mouse.click(button='left', coords=(900, 50))

    # ok
    def test_kill_firefox_process_2(self):
        print('test_kill_firefox_process_2')

        name = 'firefox.exe'

        i = 0

        # Initializing the wmi object
        f = wmi.WMI()

        # Iterating through all the
        # running processes
        for process in f.Win32_Process():

            # Checking whether the process
            # name matches our specified name
            if process.name == name and i < 4:
                # If the name matches,
                # terminate the process
                process.Terminate()

                i += 1


class UnitTestsWebAutomationYellowPagesCanadaWithClearWeb(unittest.TestCase):
    # ok
    def test_insert_the_email_for_one_company_with_clear_web(self):
        print('test_insert_the_email_for_one_company_with_clear_web')

        time.sleep(5)

        warnings.filterwarnings(
            action="ignore",
            message="unclosed",
            category=ResourceWarning
        )

        time.sleep(5)

        firefox_options = Options()
        firefox_options.headless = False
        browser = webdriver.Firefox(
            executable_path='..\\..\\..\\..\\geckodriver.exe',
            options=firefox_options
        )

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get('https://www.yellowpages.ca/bus/Ontario/Whitby/Ontario-Shores-Centre-for-Mental-Health-'
                    'Sciences/6707729.html?what=Hospital&where=Toronto+ON&useContext=true')

        time.sleep(15)

        # click on the message button
        message_button = browser.find_element_by_xpath(
            "/html/body/div[2]/div[3]/div/div[1]/div[2]/div[1]/div[2]/div[1]/div/ul/li[2]/a"
        )
        message_button.click()

        time.sleep(10)

        # insert the email
        try:
            email_input = browser.find_element_by_xpath(
                '//*[@id="emailMessage"]'
            )
            email_input.clear()
            email_input.send_keys(
                ".@outlook.fr"
            )
            print("email inserted")
        except Exception as e:
            print('error email inserted : ' + str(e))

        time.sleep(10)

        browser.quit()
        print('browser.quit()')

    # ok
    def test_insert_the_first_name_for_one_company_with_clear_web(self):
        print('test_insert_the_first_name_for_one_company_with_clear_web')

        time.sleep(5)

        warnings.filterwarnings(
            action="ignore",
            message="unclosed",
            category=ResourceWarning
        )

        time.sleep(5)

        firefox_options = Options()
        firefox_options.headless = False
        browser = webdriver.Firefox(
            executable_path='..\\..\\..\\..\\geckodriver.exe',
            options=firefox_options
        )

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get('https://www.yellowpages.ca/bus/Ontario/Whitby/Ontario-Shores-Centre-for-Mental-Health-'
                    'Sciences/6707729.html?what=Hospital&where=Toronto+ON&useContext=true')

        time.sleep(15)

        # click on the message button
        message_button = browser.find_element_by_xpath(
            "/html/body/div[2]/div[3]/div/div[1]/div[2]/div[1]/div[2]/div[1]/div/ul/li[2]/a"
        )
        message_button.click()

        time.sleep(10)

        # insert the first name
        try:
            first_name_input = browser.find_element_by_xpath(
                '//*[@id="firstNameMessage"]'
            )
            first_name_input.clear()
            first_name_input.send_keys(
                ""
            )
            print("first_name_input inserted")
        except Exception as e:
            print('error first_name_input inserted : ' + str(e))

        time.sleep(10)

        browser.quit()
        print("browser.quit()")

    # ok
    def test_insert_the_last_name_for_one_company_with_clear_web(self):
        print('test_insert_the_last_name_for_one_company_with_clear_web')

        time.sleep(5)

        warnings.filterwarnings(
            action="ignore",
            message="unclosed",
            category=ResourceWarning
        )

        time.sleep(5)

        firefox_options = Options()
        firefox_options.headless = False
        browser = webdriver.Firefox(
            executable_path='..\\..\\..\\..\\geckodriver.exe',
            options=firefox_options
        )

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get('https://www.yellowpages.ca/bus/Ontario/Whitby/Ontario-Shores-Centre-for-Mental-Health-'
                    'Sciences/6707729.html?what=Hospital&where=Toronto+ON&useContext=true')

        time.sleep(15)

        # click on the message button
        message_button = browser.find_element_by_xpath(
            "/html/body/div[2]/div[3]/div/div[1]/div[2]/div[1]/div[2]/div[1]/div/ul/li[2]/a"
        )
        message_button.click()

        time.sleep(10)

        # insert the last name
        try:
            last_name_input = browser.find_element_by_xpath(
                '//*[@id="lastNameMessage"]'
            )
            last_name_input.clear()
            last_name_input.send_keys(
                ""
            )
            print("last_name_input inserted")
        except Exception as e:
            print('error last_name_input inserted : ' + str(e))

        time.sleep(10)

        browser.quit()
        print('browser.quit()')

    # ok
    def test_count_characters_of_the_message(self):
        print('test_count_characters_of_the_message')

        text = "Hello,\n\n" \
               "First of all, I built a machine called 'Vibrating magnet electromagnetic generator' " \
               "for the generation of electricity by extracting magnetic energy from permanent magnets.\n\n" \
               "My invention doesn't require oil, gas, coal, solar energy, wind energy, geothermal energy or " \
               "hydraulic energy to operate, and it has no parts in motion.\n\n" \
               "After, I can design my invention to your energy needs for the internal purposes of your company, " \
               "and you can reach me at anytime at the phone number below for asking me more information about " \
               "my invention.\n\n" \
               "Besides, you can have a look to my invention on my LinkedIn profile at the link below.\n\n" \
               "Looking forward for your return, please believe, my sincere greetings.\n\n" \
               " \n" \
               "CEO of  company\n" \
               "Phone : \n" \
               "Headquarter : Geneva in Switzerland\n" \
               "LinkedIn : https://www.linkedin.com/in/jason-aloyau-531727239/\n" \
               "GitHub : https://github.com/Jay4C"

        if len(text) < 1000:
            print("length text good : " + str(len(text)))
        else:
            print("length text bad : " + str(len(text)))

    # ok
    def test_insert_the_message_for_one_company_with_clear_web(self):
        print('test_insert_the_message_for_one_company_with_clear_web')

        time.sleep(5)

        warnings.filterwarnings(
            action="ignore",
            message="unclosed",
            category=ResourceWarning
        )

        time.sleep(5)

        firefox_options = Options()
        firefox_options.headless = False
        browser = webdriver.Firefox(
            executable_path='..\\..\\..\\..\\geckodriver.exe',
            options=firefox_options
        )

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get('https://www.yellowpages.ca/bus/Ontario/Whitby/Ontario-Shores-Centre-for-Mental-Health-'
                    'Sciences/6707729.html?what=Hospital&where=Toronto+ON&useContext=true')

        time.sleep(15)

        # click on the message button
        message_button = browser.find_element_by_xpath(
            "/html/body/div[2]/div[3]/div/div[1]/div[2]/div[1]/div[2]/div[1]/div/ul/li[2]/a"
        )
        message_button.click()

        time.sleep(10)

        # insert the message
        try:
            message_input = browser.find_element_by_xpath(
                '//*[@id="contentMessage"]'
            )
            message_input.clear()

            text = "Hello,\n\n" \
                   "First of all, I built a machine called 'Vibrating magnet electromagnetic generator' " \
                   "for the generation of electricity by extracting magnetic energy from permanent magnets.\n\n" \
                   "My invention doesn't require oil, gas, coal, solar energy, wind energy, geothermal energy or " \
                   "hydraulic energy to operate, and it has no parts in motion.\n\n" \
                   "After, I can design my invention to your energy needs for the internal purposes of your company, " \
                   "and you can reach me at anytime at the phone number below for asking me more information about " \
                   "my invention.\n\n" \
                   "Besides, you can have a look to my invention on my LinkedIn profile at the link below.\n\n" \
                   "Looking forward for your return, please believe, my sincere greetings.\n\n" \
                   " \n" \
                   "CEO of  company\n" \
                   "Phone : \n" \
                   "Headquarter : Geneva in Switzerland\n" \
                   "LinkedIn : https://www.linkedin.com/in/jason-aloyau-531727239/\n" \
                   "GitHub : https://github.com/Jay4C"

            message_input.send_keys(
                text
            )
            print("message_input inserted")
        except Exception as e:
            print('error last_name_input inserted : ' + str(e))

        time.sleep(10)

        browser.quit()
        print('browser.quit()')

    #
    def test_insert_the_file_for_one_company_with_clear_web(self):
        print('test_insert_the_file_for_one_company_with_clear_web')

        time.sleep(5)

        warnings.filterwarnings(
            action="ignore",
            message="unclosed",
            category=ResourceWarning
        )

        time.sleep(5)

        firefox_options = Options()
        firefox_options.headless = False
        browser = webdriver.Firefox(
            executable_path='..\\..\\..\\..\\geckodriver.exe',
            options=firefox_options
        )

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get('https://www.yellowpages.ca/bus/Ontario/Whitby/Ontario-Shores-Centre-for-Mental-Health-'
                    'Sciences/6707729.html?what=Hospital&where=Toronto+ON&useContext=true')

        time.sleep(15)

        file = "C:\\Users\\DELL\\Documents\\Outils\\Desktop_Automation\\assembly_vmeg.png"

        # click on the message button
        message_button = browser.find_element_by_xpath(
            "/html/body/div[2]/div[3]/div/div[1]/div[2]/div[1]/div[2]/div[1]/div/ul/li[2]/a"
        )
        message_button.click()

        time.sleep(10)

        # insert on the file
        file_upload = browser.find_element_by_xpath(
            '//*[@id="uploadfiles"]'
        )
        file_upload.send_keys(file)

        time.sleep(10)

        browser.quit()
        print('browser.quit()')

    # ok
    def test_send_a_message_for_one_company_with_clear_web(self):
        print("test_send_a_message_for_one_company_with_clear_web")

        time.sleep(5)

        warnings.filterwarnings(
            action="ignore",
            message="unclosed",
            category=ResourceWarning
        )

        time.sleep(5)

        firefox_options = Options()
        firefox_options.headless = False
        browser = webdriver.Firefox(
            executable_path='..\\..\\..\\..\\geckodriver.exe',
            options=firefox_options
        )

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get('https://www.yellowpages.ca/bus/Ontario/Toronto/The-Big-Carrot-Danforth-Community-Market/102254127.html?what=Restaurant&where=Toronto+ON&useContext=true')
        print('page opened')

        time.sleep(15)

        # click on the message button
        message_button = browser.find_element_by_xpath(
            "/html/body/div[2]/div[3]/div/div[1]/div[2]/div[1]/div[2]/div[1]/div/ul/li[2]/a"
        )
        message_button.click()

        time.sleep(10)

        # insert the email
        try:
            email_input = browser.find_element_by_xpath(
                '//*[@id="emailMessage"]'
            )
            email_input.clear()
            email_input.send_keys(
                ".@outlook.fr"
            )
            print("email inserted")
        except Exception as e:
            print('error email inserted : ' + str(e))

        time.sleep(10)

        # insert the first name
        try:
            first_name_input = browser.find_element_by_xpath(
                '//*[@id="firstNameMessage"]'
            )
            first_name_input.clear()
            first_name_input.send_keys(
                ""
            )
            print("first_name_input inserted")
        except Exception as e:
            print('error first_name_input inserted : ' + str(e))

        time.sleep(10)

        # insert the last name
        try:
            last_name_input = browser.find_element_by_xpath(
                '//*[@id="lastNameMessage"]'
            )
            last_name_input.clear()
            last_name_input.send_keys(
                ""
            )
            print("last_name_input inserted")
        except Exception as e:
            print('error last_name_input inserted : ' + str(e))

        time.sleep(10)

        # insert the message
        try:
            message_input = browser.find_element_by_xpath(
                '//*[@id="contentMessage"]'
            )
            message_input.clear()

            text = "Hello,\n\n" \
                   "First of all, I built a machine called 'Vibrating magnet electromagnetic generator' " \
                   "for the generation of electricity by extracting magnetic energy from permanent magnets.\n\n" \
                   "My invention doesn't require oil, gas, coal, solar energy, wind energy, geothermal energy or " \
                   "hydraulic energy to operate, and it has no parts in motion.\n\n" \
                   "After, I can design my invention to your energy needs for the internal purposes of your company, " \
                   "and you can reach me at anytime at the phone number below for asking me more information about " \
                   "my invention.\n\n" \
                   "Besides, you can have a look to my invention on my LinkedIn profile at the link below.\n\n" \
                   "Looking forward for your return, please believe, my sincere greetings.\n\n" \
                   " \n" \
                   "CEO of  company\n" \
                   "Phone : 00.33.7.45.75.27.00\n" \
                   "Headquarter : Geneva in Switzerland\n" \
                   "LinkedIn : https://www.linkedin.com/in/jason-aloyau-531727239/\n" \
                   "GitHub : https://github.com/Jay4C"

            message_input.send_keys(
                text
            )

            print("message_input inserted")
        except Exception as e:
            print('error last_name_input inserted : ' + str(e))

        time.sleep(10)

        # click on the "Yes" checkbox
        yes_checkbox = browser.find_element_by_xpath(
            '//*[@id="agreementMessage"]'
        )
        yes_checkbox.click()
        print('yes_checkbox.click()')

        time.sleep(10)

        # click on the "Send the copy of the message" checkbox
        copy_checkbox = browser.find_element_by_xpath(
            '//*[@id="sendCopy"]'
        )
        copy_checkbox.click()
        print('copy_checkbox.click()')

        time.sleep(10)

        # click on the 'send' button
        send_button = browser.find_element_by_xpath(
            '/html/body/div[5]/div/div/div/div[2]/form/div[8]/button'
        )
        send_button.click()
        print('send_button.click()')

        time.sleep(10)

        # Print the success
        success = browser.find_element_by_xpath(
            "/html/body/div[5]/div/div/div/div[2]/div[2]"
        ).get_attribute("data-msg-name")
        print('success : ' + str(success))

        time.sleep(10)

        print("ccleaner running")
        os.system("set ccleaner='C:\\Program Files\\CCleaner\\CCleaner.exe'")
        os.system("start ccleaner /AUTO")

        time.sleep(10)

        browser.quit()
        print('browser.quit()')

    # ok
    def test_send_a_message_for_companies_with_clear_web(self):
        print('test_send_a_message_for_companies_with_clear_web')

        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
            }

            activites = [
                {'id': '1', 'url': 'agence+de+placement', 'start': 1},
                # {'id': '2', 'url': 'agence+immobilière', 'start': 1},
                # {'id': '3', 'url': "recrutement", 'start': 1},
                # {'id': '4', 'url': 'logiciel', 'start': 1},
                # {'id': '5', 'url': 'hotel', 'start': 1},
                # {'id': '6', 'url': 'social', 'start': 1},
                # {'id': '7', 'url': 'nettoyage', 'start': 1},
                # {'id': '8', 'url': 'association', 'start': 1},
                # {'id': '9', 'url': 'etablissement+financier', 'start': 1},
                # {'id': '10', 'url': 'restaurant', 'start': 1},
                # {'id': '11', 'url': 'batiment', 'start': 1},
                # {'id': '12', 'url': 'coiffeur', 'start': 1},
                # {'id': '13', 'url': 'fleuriste', 'start': 1},
                # {'id': '14', 'url': 'serrurier', 'start': 1},
                # {'id': '15', 'url': 'boulangerie', 'start': 1},
                # {'id': '16', 'url': 'assurance', 'start': 1},
                # {'id': '17', 'url': 'pharmacie', 'start': 1},
                # {'id': '18', 'url': 'demenagement', 'start': 1},
                # {'id': '19', 'url': 'electricite', 'start': 1},
                # {'id': '20', 'url': 'plomberie', 'start': 1},
                # {'id': '21', 'url': 'securite', 'start': 1},
                # {'id': '22', 'url': 'avocat', 'start': 1},
                # {'id': '23', 'url': 'banque', 'start': 1},
                # {'id': '24', 'url': 'garage', 'start': 1},
                # {'id': '25', 'url': 'dentiste', 'start': 1},
                # {'id': '26', 'url': 'docteur', 'start': 1},
                # {'id': '27', 'url': 'comptable', 'start': 1},
                # {'id': '28', 'url': 'supermarche', 'start': 1},
                # {'id': '29', 'url': 'notaire', 'start': 1},
                # {'id': '30', 'url': 'bijoutier', 'start': 1},
                # {'id': '31', 'url': 'couturier', 'start': 1},
                # {'id': '32', 'url': 'boucherie', 'start': 1},
                # {'id': '33', 'url': 'librairie', 'start': 1},
                # {'id': '34', 'url': 'architecte', 'start': 1}
                # {'id': '36', 'url': 'ciment', 'start': 1},
                # {'id': '37', 'url': 'chauffage', 'start': 1},
                # {'id': '38', 'url': 'bateau', 'start': 1},
                # {'id': '39', 'url': 'climatisation', 'start': 1},
                # {'id': '41', 'url': 'acier', 'start': 1},
                # {'id': '42', 'url': 'produits+chimiques', 'start': 1},
                # {'id': '43', 'url': 'gaz', 'start': 1},
                # {'id': '44', 'url': 'achat+or', 'start': 1},
                # {'id': '45', 'url': 'énergie', 'start': 1},
                # {'id': '46', 'url': 'agriculteur', 'start': 1},
            ]

            capitales_du_monde = [
                {'id': '473', 'nom': 'Edmonton+AB', 'pays': 'Canada'}, #edmonton
                # {'id': '474', 'nom': 'Victoria+BC', 'pays': 'Canada'}, #victoria
                # {'id': '475', 'nom': 'Winnipeg+MB', 'pays': 'Canada'}, #winnipeg
                # {'id': '476', 'nom': 'Fredericton+NB', 'pays': 'Canada'}, #fredericton
                # {'id': '477', 'nom': 'Aeroport+De+Saint-Jean-De-Terre-Neuve+St+Johns+NL', 'pays': 'Canada'}, #saint john
                # {'id': '478', 'nom': 'Halifax+NS', 'pays': 'Canada'}, #halifax
                # {'id': '479', 'nom': 'Yellowknife+NT', 'pays': 'Canada'}, #yellowknife
                # {'id': '480', 'nom': 'Iqaluit+NU', 'pays': 'Canada'}, #iqaluit
                # {'id': '481', 'nom': 'Toronto+ON', 'pays': 'Canada'}, #toronto
                # {'id': '482', 'nom': 'Charlottetown+PE', 'pays': 'Canada'}, #charlottetown
                # {'id': '483', 'nom': 'Quebec+QC', 'pays': 'Canada'}, #quebec
                # {'id': '484', 'nom': 'Regina+SK', 'pays': 'Canada'}, #regina
                # {'id': '485', 'nom': 'Whitehorse+YT', 'pays': 'Canada'} #whitehorse
            ]

            for capitale in capitales_du_monde:
                for activite in activites:
                    try:
                        activity = activite.get('url')
                        city = capitale.get('nom')
                        url_search = "https://www.pagesjaunes.ca/search/si/1/" \
                                     + activity + "/" + city

                        rt = RequestsTor()

                        html_search = rt.get(url_search, headers=headers)

                        rt.new_id()

                        soup_search = BeautifulSoup(html_search.content, 'html.parser')

                        number_of_pages = 0

                        # find the number of pages
                        try:
                            if soup_search.find("span", {"class": "pageCount"}) is not None:
                                try:
                                    if soup_search.find("span", {"class": "pageCount"}).find("span") is not None:
                                        number_of_pages += int(soup_search
                                                               .find("span", {"class": "pageCount"})
                                                               .find_all("span")[1]
                                                               .text)
                                        print("number_of_pages : " + str(number_of_pages))
                                    else:
                                        print("no span")
                                except Exception as e:
                                    print("error span : " + str(e))
                            else:
                                print("no span class pageCount")
                        except Exception as e:
                            print("error span class pageCount : " + str(e))

                        i_1 = 0

                        if number_of_pages > 1:
                            for i in range(activite.get('start'), number_of_pages + 1):
                                try:
                                    url_of_one_page_of_results = "https://www.pagesjaunes.ca/search/si/" \
                                                                 + str(i) + "/" \
                                                                 + activity + "/" \
                                                                 + city

                                    print(url_of_one_page_of_results)

                                    time.sleep(3)

                                    rt = RequestsTor()

                                    html_of_one_page_of_results = rt.get(url_of_one_page_of_results, headers=headers)

                                    rt.new_id()

                                    soup_of_one_page_of_results = BeautifulSoup(html_of_one_page_of_results.content,
                                                                                'html.parser')

                                    try:
                                        if soup_of_one_page_of_results \
                                                .find("div", {"class": "resultList"}) is not None:
                                            try:
                                                if soup_of_one_page_of_results \
                                                        .find("div", {"class": "resultList"}) \
                                                        .find("div", {"class": "listing"}) is not None:

                                                    all_listing = soup_of_one_page_of_results \
                                                        .find("div", {"class": "resultList"}) \
                                                        .find_all("div", {"class": "listing"})

                                                    for listing in all_listing:
                                                        i_1 += 1

                                                        try:
                                                            if listing.find("a", {
                                                                "class": "listing__name--link"}) is not None:
                                                                website = "https://www.pagesjaunes.ca" + listing \
                                                                    .find("a", {"class": "listing__name--link"}) \
                                                                    .get("href")

                                                                try:
                                                                    url_contact = website

                                                                    print(url_contact)

                                                                    time.sleep(3)

                                                                    rt = RequestsTor()

                                                                    html_contact = rt.get(url_contact, headers=headers)

                                                                    rt.new_id()

                                                                    soup = BeautifulSoup(html_contact.content, 'html.parser')

                                                                    if soup.find('li', {
                                                                        'class': 'mlr__item--message'}) is not None:
                                                                        print('yes message button')
                                                                        print('\n')

                                                                        time.sleep(5)

                                                                        warnings.filterwarnings(
                                                                            action="ignore",
                                                                            message="unclosed",
                                                                            category=ResourceWarning
                                                                        )

                                                                        time.sleep(5)

                                                                        firefox_options = Options()
                                                                        firefox_options.headless = True
                                                                        browser = webdriver.Firefox(
                                                                            executable_path='..\\..\\..\\..\\geckodriver.exe',
                                                                            options=firefox_options
                                                                        )

                                                                        # maximize window
                                                                        browser.maximize_window()

                                                                        time.sleep(5)

                                                                        # open
                                                                        browser.get(url_contact)
                                                                        print('page opened')

                                                                        time.sleep(15)

                                                                        # click on the message button
                                                                        message_button = browser.find_element_by_xpath(
                                                                            "/html/body/div[2]/div[3]/div/div[1]/div[2]/div[1]/div[2]/div[1]/div/ul/li[2]/a"
                                                                        )
                                                                        message_button.click()

                                                                        time.sleep(10)

                                                                        # insert the email
                                                                        try:
                                                                            email_input = browser.find_element_by_xpath(
                                                                                '//*[@id="emailMessage"]'
                                                                            )
                                                                            email_input.clear()
                                                                            email_input.send_keys(
                                                                                ".@outlook.fr"
                                                                            )
                                                                            print("email inserted")
                                                                        except Exception as e:
                                                                            print('error email inserted : ' + str(e))

                                                                        time.sleep(10)

                                                                        # insert the first name
                                                                        try:
                                                                            first_name_input = browser.find_element_by_xpath(
                                                                                '//*[@id="firstNameMessage"]'
                                                                            )
                                                                            first_name_input.clear()
                                                                            first_name_input.send_keys(
                                                                                ""
                                                                            )
                                                                            print("first_name_input inserted")
                                                                        except Exception as e:
                                                                            print(
                                                                                'error first_name_input inserted : ' + str(
                                                                                    e))

                                                                        time.sleep(10)

                                                                        # insert the last name
                                                                        try:
                                                                            last_name_input = browser.find_element_by_xpath(
                                                                                '//*[@id="lastNameMessage"]'
                                                                            )
                                                                            last_name_input.clear()
                                                                            last_name_input.send_keys(
                                                                                ""
                                                                            )
                                                                            print("last_name_input inserted")
                                                                        except Exception as e:
                                                                            print(
                                                                                'error last_name_input inserted : ' + str(
                                                                                    e))

                                                                        time.sleep(10)

                                                                        # insert the message
                                                                        try:
                                                                            message_input = browser.find_element_by_xpath(
                                                                                '//*[@id="contentMessage"]'
                                                                            )
                                                                            message_input.clear()

                                                                            text = "Hello,\n\n" \
                                                                                   "First of all, I built a machine called 'Vibrating magnet electromagnetic generator' " \
                                                                                   "for the generation of electricity by extracting magnetic energy from permanent magnets.\n\n" \
                                                                                   "My invention doesn't require oil, gas, coal, solar energy, wind energy, geothermal energy or " \
                                                                                   "hydraulic energy to operate, and it has no parts in motion.\n\n" \
                                                                                   "After, I can design my invention to your energy needs for the internal purposes of your company, " \
                                                                                   "and you can reach me at anytime at the phone number below for asking me more information about " \
                                                                                   "my invention.\n\n" \
                                                                                   "Besides, you can have a look to my invention on my LinkedIn profile at the link below.\n\n" \
                                                                                   "Looking forward for your return, please believe, my sincere greetings.\n\n" \
                                                                                   " \n" \
                                                                                   "CEO of ALOYAU company\n" \
                                                                                   "Phone : 00.33.7.45.75.27.00\n" \
                                                                                   "Headquarter : Geneva in Switzerland\n" \
                                                                                   "LinkedIn : https://www.linkedin.com/in/jason-aloyau-531727239/\n" \
                                                                                   "GitHub : https://github.com/Jay4C"

                                                                            message_input.send_keys(
                                                                                text
                                                                            )

                                                                            print("message_input inserted")
                                                                        except Exception as e:
                                                                            print('error last_name_input inserted '
                                                                                  ': ' + str(e))

                                                                        time.sleep(10)

                                                                        # click on the "Yes" checkbox
                                                                        yes_checkbox = browser.find_element_by_xpath(
                                                                            '//*[@id="agreementMessage"]'
                                                                        )
                                                                        yes_checkbox.click()
                                                                        print('yes_checkbox.click()')

                                                                        time.sleep(10)

                                                                        # click on the "Send the copy of the message"
                                                                        # checkbox
                                                                        copy_checkbox = browser.find_element_by_xpath(
                                                                            '//*[@id="sendCopy"]'
                                                                        )
                                                                        copy_checkbox.click()
                                                                        print('copy_checkbox.click()')

                                                                        time.sleep(10)

                                                                        # click on the 'send' button
                                                                        try:
                                                                            send_button = browser.find_element_by_xpath(
                                                                                '/html/body/div[5]/div/div/div/div[2]/form/div[6]/button'
                                                                            )
                                                                            send_button.click()
                                                                            print('send_button.click()')
                                                                        except Exception as e:
                                                                            print("error send_button : " + str(e))

                                                                        time.sleep(10)

                                                                        # Print the success
                                                                        try:
                                                                            success = browser.find_element_by_xpath(
                                                                                "/html/body/div[5]/div/div/div/div[2]/div[2]"
                                                                            ).get_attribute("data-msg-name")
                                                                            print('success : ' + str(success))
                                                                        except Exception as e:
                                                                            print('error success : ' + str(e))

                                                                        time.sleep(10)

                                                                        print("ccleaner running")
                                                                        os.system("set ccleaner='C:\\Program Files\\CCleaner\\CCleaner.exe'")
                                                                        os.system("start ccleaner /AUTO")

                                                                        time.sleep(10)

                                                                        browser.quit()
                                                                        print('browser.quit()')
                                                                    else:
                                                                        print('no message button')
                                                                        print('\n')
                                                                except Exception as e:
                                                                    print("error url : " + str(e))
                                                            else:
                                                                print("")
                                                        except Exception as e:
                                                            print("no a class listing__name--link : " + str(e))
                                                else:
                                                    print("no listing")
                                            except Exception as e:
                                                print("error  : " + str(e))
                                        else:
                                            print("no resultList")
                                    except Exception as e:
                                        print("error div class resultList : " + str(e))
                                except Exception as e:
                                    print("error url_of_one_page_of_results : " + str(e))
                        else:
                            try:
                                url_of_one_page_of_results = "https://www.pagesjaunes.ca/search/si/1/" \
                                                             + activity + "/" \
                                                             + city

                                print(url_of_one_page_of_results)

                                time.sleep(3)

                                rt = RequestsTor()

                                html_of_one_page_of_results = rt.get(url_of_one_page_of_results, headers=headers)

                                rt.new_id()

                                soup_of_one_page_of_results = BeautifulSoup(html_of_one_page_of_results.content,
                                                                            'html.parser')

                                try:
                                    if soup_of_one_page_of_results \
                                            .find("div", {"class": "resultList"}) is not None:
                                        try:
                                            if soup_of_one_page_of_results \
                                                    .find("div", {"class": "resultList"}) \
                                                    .find("div", {"class": "listing"}) is not None:

                                                all_listing = soup_of_one_page_of_results \
                                                    .find("div", {"class": "resultList"}) \
                                                    .find_all("div", {"class": "listing"})

                                                for listing in all_listing:
                                                    i_1 += 1

                                                    try:
                                                        if listing.find("a",
                                                                        {"class": "listing__name--link"}) is not None:
                                                            website = "https://www.pagesjaunes.ca" + listing \
                                                                .find("a", {"class": "listing__name--link"}) \
                                                                .get("href")

                                                            try:
                                                                url_contact = website

                                                                time.sleep(3)

                                                                rt = RequestsTor()

                                                                html_contact = rt.get(
                                                                    url_contact,
                                                                    headers=headers
                                                                )

                                                                rt.new_id()

                                                                soup = BeautifulSoup(html_contact.content, 'html.parser')

                                                                if soup.find('li', {
                                                                    'class': 'mlr__item--message'}) is not None:
                                                                    print('yes message button')
                                                                    print('\n')

                                                                    time.sleep(5)

                                                                    warnings.filterwarnings(
                                                                        action="ignore",
                                                                        message="unclosed",
                                                                        category=ResourceWarning
                                                                    )

                                                                    time.sleep(5)

                                                                    firefox_options = Options()
                                                                    firefox_options.headless = True
                                                                    browser = webdriver.Firefox(
                                                                        executable_path='..\\..\\..\\..\\geckodriver.exe',
                                                                        options=firefox_options
                                                                    )

                                                                    # maximize window
                                                                    browser.maximize_window()

                                                                    time.sleep(5)

                                                                    # open
                                                                    browser.get(url_contact)
                                                                    print('page opened')

                                                                    time.sleep(15)

                                                                    # click on the message button
                                                                    message_button = browser.find_element_by_xpath(
                                                                        "/html/body/div[2]/div[3]/div/div[1]/div[2]/div[1]/div[2]/div[1]/div/ul/li[2]/a"
                                                                    )
                                                                    message_button.click()

                                                                    time.sleep(10)

                                                                    # insert the email
                                                                    try:
                                                                        email_input = browser.find_element_by_xpath(
                                                                            '//*[@id="emailMessage"]'
                                                                        )
                                                                        email_input.clear()
                                                                        email_input.send_keys(
                                                                            ".@outlook.fr"
                                                                        )
                                                                        print("email inserted")
                                                                    except Exception as e:
                                                                        print('error email inserted : ' + str(e))

                                                                    time.sleep(10)

                                                                    # insert the first name
                                                                    try:
                                                                        first_name_input = browser.find_element_by_xpath(
                                                                            '//*[@id="firstNameMessage"]'
                                                                        )
                                                                        first_name_input.clear()
                                                                        first_name_input.send_keys(
                                                                            ""
                                                                        )
                                                                        print("first_name_input inserted")
                                                                    except Exception as e:
                                                                        print(
                                                                            'error first_name_input inserted : ' + str(
                                                                                e))

                                                                    time.sleep(10)

                                                                    # insert the last name
                                                                    try:
                                                                        last_name_input = browser.find_element_by_xpath(
                                                                            '//*[@id="lastNameMessage"]'
                                                                        )
                                                                        last_name_input.clear()
                                                                        last_name_input.send_keys(
                                                                            ""
                                                                        )
                                                                        print("last_name_input inserted")
                                                                    except Exception as e:
                                                                        print(
                                                                            'error last_name_input inserted : ' + str(
                                                                                e))

                                                                    time.sleep(10)

                                                                    # insert the message
                                                                    try:
                                                                        message_input = browser.find_element_by_xpath(
                                                                            '//*[@id="contentMessage"]'
                                                                        )
                                                                        message_input.clear()

                                                                        text = "Hello,\n\n" \
                                                                               "First of all, I built a machine called 'Vibrating magnet electromagnetic generator' " \
                                                                               "for the generation of electricity by extracting magnetic energy from permanent magnets.\n\n" \
                                                                               "My invention doesn't require oil, gas, coal, solar energy, wind energy, geothermal energy or " \
                                                                               "hydraulic energy to operate, and it has no parts in motion.\n\n" \
                                                                               "After, I can design my invention to your energy needs for the internal purposes of your company, " \
                                                                               "and you can reach me at anytime at the phone number below for asking me more information about " \
                                                                               "my invention.\n\n" \
                                                                               "Besides, you can have a look to my invention on my LinkedIn profile at the link below.\n\n" \
                                                                               "Looking forward for your return, please believe, my sincere greetings.\n\n" \
                                                                               " \n" \
                                                                               "CEO of ALOYAU company\n" \
                                                                               "Phone : 00.33.7.45.75.27.00\n" \
                                                                               "Headquarter : Geneva in Switzerland\n" \
                                                                               "LinkedIn : https://www.linkedin.com/in/jason-aloyau-531727239/\n" \
                                                                               "GitHub : https://github.com/Jay4C"

                                                                        message_input.send_keys(
                                                                            text
                                                                        )

                                                                        print("message_input inserted")
                                                                    except Exception as e:
                                                                        print('error last_name_input inserted '
                                                                              ': ' + str(e))

                                                                    time.sleep(10)

                                                                    # click on the "Yes" checkbox
                                                                    yes_checkbox = browser.find_element_by_xpath(
                                                                        '//*[@id="agreementMessage"]'
                                                                    )
                                                                    yes_checkbox.click()
                                                                    print('yes_checkbox.click()')

                                                                    time.sleep(10)

                                                                    # click on the "Send the copy of the message"
                                                                    # checkbox
                                                                    copy_checkbox = browser.find_element_by_xpath(
                                                                        '//*[@id="sendCopy"]'
                                                                    )
                                                                    copy_checkbox.click()
                                                                    print('copy_checkbox.click()')

                                                                    time.sleep(10)

                                                                    # click on the 'send' button
                                                                    try:
                                                                        send_button = browser.find_element_by_xpath(
                                                                            '/html/body/div[5]/div/div/div/div[2]/form/div[6]/button'
                                                                        )
                                                                        send_button.click()
                                                                        print('send_button.click()')
                                                                    except Exception as e:
                                                                        print("error send_button : " + str(e))

                                                                    time.sleep(10)

                                                                    # Print the success
                                                                    try:
                                                                        success = browser.find_element_by_xpath(
                                                                            "/html/body/div[5]/div/div/div/div[2]/div[2]"
                                                                        ).get_attribute("data-msg-name")
                                                                        print('success : ' + str(success))
                                                                    except Exception as e:
                                                                        print('error success : ' + str(e))

                                                                    time.sleep(10)

                                                                    print("ccleaner running")
                                                                    os.system(
                                                                        "set ccleaner='C:\\Program Files\\CCleaner\\CCleaner.exe'")
                                                                    os.system("start ccleaner /AUTO")

                                                                    time.sleep(10)

                                                                    browser.quit()
                                                                    print('browser.quit()')
                                                                else:
                                                                    print('no message button')
                                                                    print('\n')
                                                            except Exception as e:
                                                                print("error url : " + str(e))
                                                        else:
                                                            print("a class listing__name--link")
                                                    except Exception as e:
                                                        print("no a class listing__name--link : " + str(e))
                                            else:
                                                print("no listing")
                                        except Exception as e:
                                            print("error  : " + str(e))
                                    else:
                                        print("no resultList")
                                except Exception as e:
                                    print("error div class resultList : " + str(e))
                            except Exception as e:
                                print("error url_of_one_page_of_results : " + str(e))
                    except Exception as e:
                        print("error url_search : " + str(e))
        finally:
            print('done')

    # ok
    def test_send_a_message_for_companies_for_selling_electricity_with_clear_web(self):
        print('test_send_a_message_for_companies_for_selling_electricity_with_clear_web')

        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '
                              'AppleWebKit/537.36 (KHTML, like Gecko) '
                              'Chrome/51.0.2704.103'
            }

            activites = [
                {'id': '1', 'url': 'agence+de+placement', 'start': 1},
                # {'id': '2', 'url': 'agence+immobilière', 'start': 1},
                # {'id': '3', 'url': "recrutement", 'start': 1},
                # {'id': '4', 'url': 'logiciel', 'start': 1},
                # {'id': '5', 'url': 'hotel', 'start': 1},
                # {'id': '6', 'url': 'social', 'start': 1},
                # {'id': '7', 'url': 'nettoyage', 'start': 1},
                # {'id': '8', 'url': 'association', 'start': 1},
                # {'id': '9', 'url': 'etablissement+financier', 'start': 1},
                # {'id': '10', 'url': 'restaurant', 'start': 1},
                # {'id': '11', 'url': 'batiment', 'start': 1},
                # {'id': '12', 'url': 'coiffeur', 'start': 1},
                # {'id': '13', 'url': 'fleuriste', 'start': 1},
                # {'id': '14', 'url': 'serrurier', 'start': 1},
                # {'id': '15', 'url': 'boulangerie', 'start': 1},
                # {'id': '16', 'url': 'assurance', 'start': 1},
                # {'id': '17', 'url': 'pharmacie', 'start': 1},
                # {'id': '18', 'url': 'demenagement', 'start': 1},
                # {'id': '19', 'url': 'electricite', 'start': 1},
                # {'id': '20', 'url': 'plomberie', 'start': 1},
                # {'id': '21', 'url': 'securite', 'start': 1},
                # {'id': '22', 'url': 'avocat', 'start': 1},
                # {'id': '23', 'url': 'banque', 'start': 1},
                # {'id': '24', 'url': 'garage', 'start': 1},
                # {'id': '25', 'url': 'dentiste', 'start': 1},
                # {'id': '26', 'url': 'docteur', 'start': 1},
                # {'id': '27', 'url': 'comptable', 'start': 1},
                # {'id': '28', 'url': 'supermarche', 'start': 1},
                # {'id': '29', 'url': 'notaire', 'start': 1},
                # {'id': '30', 'url': 'bijoutier', 'start': 1},
                # {'id': '31', 'url': 'couturier', 'start': 1},
                # {'id': '32', 'url': 'boucherie', 'start': 1},
                # {'id': '33', 'url': 'librairie', 'start': 1},
                # {'id': '34', 'url': 'architecte', 'start': 1}
                # {'id': '36', 'url': 'ciment', 'start': 1},
                # {'id': '37', 'url': 'chauffage', 'start': 1},
                # {'id': '38', 'url': 'bateau', 'start': 1},
                # {'id': '39', 'url': 'climatisation', 'start': 1},
                # {'id': '41', 'url': 'acier', 'start': 1},
                # {'id': '42', 'url': 'produits+chimiques', 'start': 1},
                # {'id': '43', 'url': 'gaz', 'start': 1},
                # {'id': '44', 'url': 'achat+or', 'start': 1},
                # {'id': '45', 'url': 'énergie', 'start': 1},
                # {'id': '46', 'url': 'agriculteur', 'start': 1},
            ]

            capitales_du_monde = [
                {'id': '473', 'nom': 'Edmonton+AB', 'pays': 'Canada'}, #edmonton
                # {'id': '474', 'nom': 'Victoria+BC', 'pays': 'Canada'}, #victoria
                # {'id': '475', 'nom': 'Winnipeg+MB', 'pays': 'Canada'}, #winnipeg
                # {'id': '476', 'nom': 'Fredericton+NB', 'pays': 'Canada'}, #fredericton
                # {'id': '477', 'nom': 'Aeroport+De+Saint-Jean-De-Terre-Neuve+St+Johns+NL', 'pays': 'Canada'}, #saint john
                # {'id': '478', 'nom': 'Halifax+NS', 'pays': 'Canada'}, #halifax
                # {'id': '479', 'nom': 'Yellowknife+NT', 'pays': 'Canada'}, #yellowknife
                # {'id': '480', 'nom': 'Iqaluit+NU', 'pays': 'Canada'}, #iqaluit
                # {'id': '481', 'nom': 'Toronto+ON', 'pays': 'Canada'}, #toronto
                # {'id': '482', 'nom': 'Charlottetown+PE', 'pays': 'Canada'}, #charlottetown
                # {'id': '483', 'nom': 'Quebec+QC', 'pays': 'Canada'}, #quebec
                # {'id': '484', 'nom': 'Regina+SK', 'pays': 'Canada'}, #regina
                # {'id': '485', 'nom': 'Whitehorse+YT', 'pays': 'Canada'} #whitehorse
            ]

            for capitale in capitales_du_monde:
                for activite in activites:
                    try:
                        activity = activite.get('url')

                        city = capitale.get('nom')

                        url_search = "https://www.pagesjaunes.ca/search/si/1/" \
                                     + activity + "/" + city

                        rt = RequestsTor()

                        html_search = rt.get(url_search, headers=headers)

                        rt.new_id()

                        soup_search = BeautifulSoup(html_search.content, 'html.parser')

                        number_of_pages = 0

                        # find the number of pages
                        try:
                            if soup_search.find("span", {"class": "pageCount"}) is not None:
                                try:
                                    if soup_search.find("span", {"class": "pageCount"}).find("span") is not None:
                                        number_of_pages += int(soup_search
                                                               .find("span", {"class": "pageCount"})
                                                               .find_all("span")[1]
                                                               .text)
                                        print("number_of_pages : " + str(number_of_pages))
                                    else:
                                        print("no span")
                                except Exception as e:
                                    print("error span : " + str(e))
                            else:
                                print("no span class pageCount")
                        except Exception as e:
                            print("error span class pageCount : " + str(e))

                        i_1 = 0

                        if number_of_pages > 1:
                            for i in range(activite.get('start'), number_of_pages + 1):
                                try:
                                    url_of_one_page_of_results = "https://www.pagesjaunes.ca/search/si/" \
                                                                 + str(i) + "/" \
                                                                 + activity + "/" \
                                                                 + city

                                    print(url_of_one_page_of_results)

                                    time.sleep(3)

                                    rt = RequestsTor()

                                    html_of_one_page_of_results = rt.get(url_of_one_page_of_results, headers=headers)

                                    rt.new_id()

                                    soup_of_one_page_of_results = BeautifulSoup(html_of_one_page_of_results.content,
                                                                                'html.parser')

                                    try:
                                        if soup_of_one_page_of_results \
                                                .find("div", {"class": "resultList"}) is not None:
                                            try:
                                                if soup_of_one_page_of_results \
                                                        .find("div", {"class": "resultList"}) \
                                                        .find("div", {"class": "listing"}) is not None:

                                                    all_listing = soup_of_one_page_of_results \
                                                        .find("div", {"class": "resultList"}) \
                                                        .find_all("div", {"class": "listing"})

                                                    for listing in all_listing:
                                                        i_1 += 1

                                                        try:
                                                            if listing.find("a", {
                                                                "class": "listing__name--link"}) is not None:
                                                                website = "https://www.pagesjaunes.ca" + listing \
                                                                    .find("a", {"class": "listing__name--link"}) \
                                                                    .get("href")

                                                                try:
                                                                    url_contact = website

                                                                    print(url_contact)

                                                                    time.sleep(3)

                                                                    rt = RequestsTor()

                                                                    html_contact = rt.get(url_contact, headers=headers)

                                                                    rt.new_id()

                                                                    soup = BeautifulSoup(html_contact.content, 'html.parser')

                                                                    if soup.find('li', {
                                                                        'class': 'mlr__item--message'}) is not None:
                                                                        print('yes message button')
                                                                        print('\n')

                                                                        time.sleep(5)

                                                                        warnings.filterwarnings(
                                                                            action="ignore",
                                                                            message="unclosed",
                                                                            category=ResourceWarning
                                                                        )

                                                                        time.sleep(5)

                                                                        firefox_options = Options()
                                                                        firefox_options.headless = False
                                                                        browser = webdriver.Firefox(
                                                                            executable_path='..\\..\\..\\..\\geckodriver.exe',
                                                                            options=firefox_options
                                                                        )

                                                                        # maximize window
                                                                        browser.maximize_window()

                                                                        time.sleep(5)

                                                                        # open
                                                                        browser.get(url_contact)
                                                                        print('page opened')

                                                                        time.sleep(15)

                                                                        # click on the message button
                                                                        message_button = browser.find_element_by_xpath(
                                                                            "/html/body/div[2]/div[3]/div/div[1]/div[2]/div[1]/div[2]/div[1]/div/ul/li[2]/a"
                                                                        )
                                                                        message_button.click()

                                                                        time.sleep(10)

                                                                        # insert the email
                                                                        try:
                                                                            email_input = browser.find_element_by_xpath(
                                                                                '//*[@id="emailMessage"]'
                                                                            )
                                                                            email_input.clear()
                                                                            email_input.send_keys(
                                                                                ".@outlook.fr"
                                                                            )
                                                                            print("email inserted")
                                                                        except Exception as e:
                                                                            print('error email inserted : ' + str(e))

                                                                        time.sleep(10)

                                                                        # insert the first name
                                                                        try:
                                                                            first_name_input = browser.find_element_by_xpath(
                                                                                '//*[@id="firstNameMessage"]'
                                                                            )
                                                                            first_name_input.clear()
                                                                            first_name_input.send_keys(
                                                                                ""
                                                                            )
                                                                            print("first_name_input inserted")
                                                                        except Exception as e:
                                                                            print(
                                                                                'error first_name_input inserted : ' + str(
                                                                                    e))

                                                                        time.sleep(10)

                                                                        # insert the last name
                                                                        try:
                                                                            last_name_input = browser.find_element_by_xpath(
                                                                                '//*[@id="lastNameMessage"]'
                                                                            )
                                                                            last_name_input.clear()
                                                                            last_name_input.send_keys(
                                                                                ""
                                                                            )
                                                                            print("last_name_input inserted")
                                                                        except Exception as e:
                                                                            print(
                                                                                'error last_name_input inserted : ' + str(
                                                                                    e))

                                                                        time.sleep(10)

                                                                        # insert the message
                                                                        try:
                                                                            message_input = browser.find_element_by_xpath(
                                                                                '//*[@id="contentMessage"]'
                                                                            )
                                                                            message_input.clear()

                                                                            text = "Hello,\n\n" \
                                                                                   "First of all, I built a machine called 'Vibrating magnet electromagnetic generator' " \
                                                                                   "for the generation of electricity by extracting magnetic energy from permanent magnets.\n\n" \
                                                                                   "My invention doesn't require oil, gas, coal, solar energy, wind energy, geothermal energy or " \
                                                                                   "hydraulic energy to operate, and it has no parts in motion.\n\n" \
                                                                                   "After, I am looking for a location with a partner for installing my machine to supply electricity to the public electricity grid for selling electricity to an electricity provider in partnership with your company.\n\n" \
                                                                                   "Besides, you can have a look to my invention on my LinkedIn profile at the link below.\n\n" \
                                                                                   "My question is :\n" \
                                                                                   "Is it possible to be in partnership with your company for selling electricity please ?\n\n" \
                                                                                   "Looking forward for your return, please believe, my sincere greetings.\n\n" \
                                                                                   " \n" \
                                                                                   "Phone : 00.33.7.45.75.27.00\n" \
                                                                                   "LinkedIn : https://www.linkedin.com/in/jason-aloyau-531727239/\n" \
                                                                                   "GitHub : https://github.com/Jay4C\n" \
                                                                                   "Malt : https://www.malt.fr/profile/jasonaloyau"

                                                                            message_input.send_keys(
                                                                                text
                                                                            )

                                                                            print("message_input inserted")
                                                                        except Exception as e:
                                                                            print('error last_name_input inserted '
                                                                                  ': ' + str(e))

                                                                        time.sleep(10)

                                                                        # click on the "Yes" checkbox
                                                                        yes_checkbox = browser.find_element_by_xpath(
                                                                            '//*[@id="agreementMessage"]'
                                                                        )
                                                                        yes_checkbox.click()
                                                                        print('yes_checkbox.click()')

                                                                        time.sleep(10)

                                                                        # click on the "Send the copy of the message"
                                                                        # checkbox
                                                                        copy_checkbox = browser.find_element_by_xpath(
                                                                            '//*[@id="sendCopy"]'
                                                                        )
                                                                        copy_checkbox.click()
                                                                        print('copy_checkbox.click()')

                                                                        time.sleep(10)

                                                                        # click on the 'send' button
                                                                        try:
                                                                            send_button = browser.find_element_by_xpath(
                                                                                '/html/body/div[5]/div/div/div/div[2]/form/div[6]/button'
                                                                            )
                                                                            send_button.click()
                                                                            print('send_button.click()')
                                                                        except Exception as e:
                                                                            print("error send_button : " + str(e))

                                                                        time.sleep(10)

                                                                        # Print the success
                                                                        try:
                                                                            success = browser.find_element_by_xpath(
                                                                                "/html/body/div[5]/div/div/div/div[2]/div[2]"
                                                                            ).get_attribute("data-msg-name")
                                                                            print('success : ' + str(success))
                                                                        except Exception as e:
                                                                            print('error success : ' + str(e))

                                                                        time.sleep(10)

                                                                        print("ccleaner running")
                                                                        os.system("set ccleaner='C:\\Program Files\\CCleaner\\CCleaner.exe'")
                                                                        os.system("start ccleaner /AUTO")

                                                                        time.sleep(10)

                                                                        browser.quit()
                                                                        print('browser.quit()')
                                                                    else:
                                                                        print('no message button')
                                                                        print('\n')
                                                                except Exception as e:
                                                                    print("error url : " + str(e))
                                                            else:
                                                                print("")
                                                        except Exception as e:
                                                            print("no a class listing__name--link : " + str(e))
                                                else:
                                                    print("no listing")
                                            except Exception as e:
                                                print("error  : " + str(e))
                                        else:
                                            print("no resultList")
                                    except Exception as e:
                                        print("error div class resultList : " + str(e))
                                except Exception as e:
                                    print("error url_of_one_page_of_results : " + str(e))
                        else:
                            try:
                                url_of_one_page_of_results = "https://www.pagesjaunes.ca/search/si/1/" \
                                                             + activity + "/" \
                                                             + city

                                print(url_of_one_page_of_results)

                                time.sleep(3)

                                rt = RequestsTor()

                                html_of_one_page_of_results = rt.get(url_of_one_page_of_results, headers=headers)

                                rt.new_id()

                                soup_of_one_page_of_results = BeautifulSoup(html_of_one_page_of_results.content,
                                                                            'html.parser')

                                try:
                                    if soup_of_one_page_of_results \
                                            .find("div", {"class": "resultList"}) is not None:
                                        try:
                                            if soup_of_one_page_of_results \
                                                    .find("div", {"class": "resultList"}) \
                                                    .find("div", {"class": "listing"}) is not None:

                                                all_listing = soup_of_one_page_of_results \
                                                    .find("div", {"class": "resultList"}) \
                                                    .find_all("div", {"class": "listing"})

                                                for listing in all_listing:
                                                    i_1 += 1

                                                    try:
                                                        if listing.find("a",
                                                                        {"class": "listing__name--link"}) is not None:
                                                            website = "https://www.pagesjaunes.ca" + listing \
                                                                .find("a", {"class": "listing__name--link"}) \
                                                                .get("href")

                                                            try:
                                                                url_contact = website

                                                                time.sleep(3)

                                                                rt = RequestsTor()

                                                                html_contact = rt.get(
                                                                    url_contact,
                                                                    headers=headers
                                                                )

                                                                rt.new_id()

                                                                soup = BeautifulSoup(html_contact.content, 'html.parser')

                                                                if soup.find('li', {
                                                                    'class': 'mlr__item--message'}) is not None:
                                                                    print('yes message button')
                                                                    print('\n')

                                                                    time.sleep(5)

                                                                    warnings.filterwarnings(
                                                                        action="ignore",
                                                                        message="unclosed",
                                                                        category=ResourceWarning
                                                                    )

                                                                    time.sleep(5)

                                                                    firefox_options = Options()
                                                                    firefox_options.headless = False
                                                                    browser = webdriver.Firefox(
                                                                        executable_path='..\\..\\..\\..\\geckodriver.exe',
                                                                        options=firefox_options
                                                                    )

                                                                    # maximize window
                                                                    browser.maximize_window()

                                                                    time.sleep(5)

                                                                    # open
                                                                    browser.get(url_contact)
                                                                    print('page opened')

                                                                    time.sleep(15)

                                                                    # click on the message button
                                                                    message_button = browser.find_element_by_xpath(
                                                                        "/html/body/div[2]/div[3]/div/div[1]/div[2]/div[1]/div[2]/div[1]/div/ul/li[2]/a"
                                                                    )
                                                                    message_button.click()

                                                                    time.sleep(10)

                                                                    # insert the email
                                                                    try:
                                                                        email_input = browser.find_element_by_xpath(
                                                                            '//*[@id="emailMessage"]'
                                                                        )
                                                                        email_input.clear()
                                                                        email_input.send_keys(
                                                                            ".@outlook.fr"
                                                                        )
                                                                        print("email inserted")
                                                                    except Exception as e:
                                                                        print('error email inserted : ' + str(e))

                                                                    time.sleep(10)

                                                                    # insert the first name
                                                                    try:
                                                                        first_name_input = browser.find_element_by_xpath(
                                                                            '//*[@id="firstNameMessage"]'
                                                                        )
                                                                        first_name_input.clear()
                                                                        first_name_input.send_keys(
                                                                            ""
                                                                        )
                                                                        print("first_name_input inserted")
                                                                    except Exception as e:
                                                                        print(
                                                                            'error first_name_input inserted : ' + str(
                                                                                e))

                                                                    time.sleep(10)

                                                                    # insert the last name
                                                                    try:
                                                                        last_name_input = browser.find_element_by_xpath(
                                                                            '//*[@id="lastNameMessage"]'
                                                                        )
                                                                        last_name_input.clear()
                                                                        last_name_input.send_keys(
                                                                            ""
                                                                        )
                                                                        print("last_name_input inserted")
                                                                    except Exception as e:
                                                                        print(
                                                                            'error last_name_input inserted : ' + str(
                                                                                e))

                                                                    time.sleep(10)

                                                                    # insert the message
                                                                    try:
                                                                        message_input = browser.find_element_by_xpath(
                                                                            '//*[@id="contentMessage"]'
                                                                        )
                                                                        message_input.clear()

                                                                        text = "Hello,\n\n" \
                                                                               "First of all, I built a machine called 'Vibrating magnet electromagnetic generator' " \
                                                                               "for the generation of electricity by extracting magnetic energy from permanent magnets.\n\n" \
                                                                               "My invention doesn't require oil, gas, coal, solar energy, wind energy, geothermal energy or " \
                                                                               "hydraulic energy to operate, and it has no parts in motion.\n\n" \
                                                                               "After, I am looking for a location with a partner for installing my machine to supply electricity to the public electricity grid for selling electricity to an electricity provider in partnership with your company.\n\n" \
                                                                               "Besides, you can have a look to my invention on my LinkedIn profile at the link below.\n\n" \
                                                                               "My question is :\n" \
                                                                               "Is it possible to be in partnership with your company for selling electricity please ?\n\n" \
                                                                               "Looking forward for your return, please believe, my sincere greetings.\n\n" \
                                                                               " \n" \
                                                                               "Phone : 00.33.7.45.75.27.00\n" \
                                                                               "LinkedIn : https://www.linkedin.com/in/jason-aloyau-531727239/\n" \
                                                                               "GitHub : https://github.com/Jay4C\n" \
                                                                               "Malt : https://www.malt.fr/profile/jasonaloyau"

                                                                        message_input.send_keys(
                                                                            text
                                                                        )

                                                                        print("message_input inserted")
                                                                    except Exception as e:
                                                                        print('error last_name_input inserted '
                                                                              ': ' + str(e))

                                                                    time.sleep(10)

                                                                    # click on the "Yes" checkbox
                                                                    yes_checkbox = browser.find_element_by_xpath(
                                                                        '//*[@id="agreementMessage"]'
                                                                    )
                                                                    yes_checkbox.click()
                                                                    print('yes_checkbox.click()')

                                                                    time.sleep(10)

                                                                    # click on the "Send the copy of the message"
                                                                    # checkbox
                                                                    copy_checkbox = browser.find_element_by_xpath(
                                                                        '//*[@id="sendCopy"]'
                                                                    )
                                                                    copy_checkbox.click()
                                                                    print('copy_checkbox.click()')

                                                                    time.sleep(10)

                                                                    # click on the 'send' button
                                                                    try:
                                                                        send_button = browser.find_element_by_xpath(
                                                                            '/html/body/div[5]/div/div/div/div[2]/form/div[6]/button'
                                                                        )
                                                                        send_button.click()
                                                                        print('send_button.click()')
                                                                    except Exception as e:
                                                                        print("error send_button : " + str(e))

                                                                    time.sleep(10)

                                                                    # Print the success
                                                                    try:
                                                                        success = browser.find_element_by_xpath(
                                                                            "/html/body/div[5]/div/div/div/div[2]/div[2]"
                                                                        ).get_attribute("data-msg-name")
                                                                        print('success : ' + str(success))
                                                                    except Exception as e:
                                                                        print('error success : ' + str(e))

                                                                    time.sleep(10)

                                                                    print("ccleaner running")
                                                                    os.system(
                                                                        "set ccleaner='C:\\Program Files\\CCleaner\\CCleaner.exe'")
                                                                    os.system("start ccleaner /AUTO")

                                                                    time.sleep(10)

                                                                    browser.quit()
                                                                    print('browser.quit()')
                                                                else:
                                                                    print('no message button')
                                                                    print('\n')
                                                            except Exception as e:
                                                                print("error url : " + str(e))
                                                        else:
                                                            print("a class listing__name--link")
                                                    except Exception as e:
                                                        print("no a class listing__name--link : " + str(e))
                                            else:
                                                print("no listing")
                                        except Exception as e:
                                            print("error  : " + str(e))
                                    else:
                                        print("no resultList")
                                except Exception as e:
                                    print("error div class resultList : " + str(e))
                            except Exception as e:
                                print("error url_of_one_page_of_results : " + str(e))
                    except Exception as e:
                        print("error url_search : " + str(e))
        finally:
            print('done')


if __name__ == '__main__':
    unittest.main()
