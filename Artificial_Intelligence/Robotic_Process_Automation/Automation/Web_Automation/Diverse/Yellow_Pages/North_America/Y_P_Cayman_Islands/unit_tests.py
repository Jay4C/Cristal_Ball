import os
import unittest
import time
import warnings
from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class UnitTestsWebAutomationYellowPagesCaymanIslandsWithClearWeb(unittest.TestCase):
    #
    def test_insert_the_subject_for_one_company_with_clear_web(self):
        print('test_insert_the_subject_for_one_company_with_clear_web')

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
        print('browser.maximize_window()')

        time.sleep(5)

        # open
        url = "https://www.findyello.com/cayman-islands/plantation-village-beach-resort/profile/"
        browser.get(url=url)
        print('browser.get(url=url)')

        time.sleep(15)

        # Insert the subject
        subject_input = browser.find_element_by_xpath(
            "/html/body/div[1]/div[1]/div[2]/div/div[1]/div[4]/form/div[1]/input[1]"
        )
        subject_input.clear()
        subject_input.send_keys(
            ""
        )
        print("subject inserted")

        time.sleep(15)

        browser.close()

        print("ccleaner running")
        os.system("set ccleaner='C:\\Program Files\\CCleaner\\CCleaner.exe'")
        os.system("start ccleaner /AUTO")

        time.sleep(15)

    # ok
    def test_insert_the_name_and_surname_for_one_company_without_headless_with_clear_web(self):
        print('test_insert_the_name_and_surname_for_one_company_without_headless_with_clear_web')

        time.sleep(5)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(5)

        # with Firefox
        browser = webdriver.Firefox(executable_path='..\\..\\..\\geckodriver.exe')

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get('https://www.findyello.com/cayman-islands/christopher-columbus-the/profile/')

        time.sleep(15)

        # insert the name and surname
        try:
            name_and_surname_input = browser.find_element_by_xpath(
                "/html/body/div[1]/div[1]/div[2]/div/div[1]/div[4]/form/div[2]/div[1]/input"
            )
            name_and_surname_input.clear()
            name_and_surname_input.send_keys(
                " "
            )
            print("name and surname inserted")
        except Exception as e:
            print('error name and surname inserted : ' + str(e))

        time.sleep(15)

        browser.close()

        print("ccleaner running")
        os.system("set ccleaner='C:\\Program Files\\CCleaner\\CCleaner.exe'")
        os.system("start ccleaner /AUTO")

        time.sleep(15)

    # ok
    def test_insert_the_phone_number_for_one_company_without_headless_with_clear_web(self):
        print('test_insert_the_phone_number_for_one_company_without_headless_with_clear_web')

        time.sleep(5)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(5)

        # with Firefox
        browser = webdriver.Firefox(executable_path='..\\..\\..\\geckodriver.exe')

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get('https://www.findyello.com/cayman-islands/christopher-columbus-the/profile/')

        time.sleep(15)

        # insert the phone number
        try:
            phone_number_input = browser.find_element_by_xpath(
                "/html/body/div[1]/div[1]/div[2]/div/div[1]/div[4]/form/div[2]/div[2]/input"
            )
            phone_number_input.clear()
            phone_number_input.send_keys(
                ""
            )
            print("phone number inserted")
        except Exception as e:
            print('error phone number inserted : ' + str(e))

        time.sleep(15)

    # ok
    def test_insert_the_email_for_one_company_without_headless_with_clear_web(self):
        print('test_insert_the_email_for_one_company_without_headless_with_clear_web')

        time.sleep(5)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(5)

        # with Firefox
        browser = webdriver.Firefox(executable_path='..\\..\\..\\geckodriver.exe')

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get('https://www.findyello.com/cayman-islands/christopher-columbus-the/profile/')

        time.sleep(15)

        # insert the email
        try:
            email_input = browser.find_element_by_xpath(
                "/html/body/div[1]/div[1]/div[2]/div/div[1]/div[4]/form/div[4]/div/input"
            )
            email_input.clear()
            email_input.send_keys(
                ".@holomorphe.com"
            )
            print("email inserted")
        except Exception as e:
            print('error email inserted : ' + str(e))

        time.sleep(15)

        browser.close()

    # computer vision needed
    def test_click_on_the_anti_robot_button_for_one_company_without_headless_with_clear_web(self):
        print('test_click_on_the_anti_robot_button_for_one_company_without_headless_with_clear_web')

        time.sleep(5)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(5)

        # with Firefox
        browser = webdriver.Firefox(executable_path='..\\..\\..\\geckodriver.exe')

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get('https://www.findyello.com/cayman-islands/doctors-hospital/profile/16-middle-road/')

        time.sleep(15)

        # click on the anti robot button
        try:
            email_input = browser.find_element_by_xpath(
                "/html/body/div[1]/div[1]/div[2]/div/div[1]/div[4]/form/div[4]/div/input"
            )
            email_input.clear()
            email_input.send_keys(
                ".@holomorphe.com"
            )
            print("email inserted")

            time.sleep(5)

            n = 1
            actions = ActionChains(browser)
            actions.send_keys(Keys.TAB * n)
            actions.send_keys(Keys.ENTER)
            actions.perform()
            print("anti robot button clicked")

            time.sleep(5)
        except Exception as e:
            print('error anti robot button clicked : ' + str(e))

        time.sleep(15)

        browser.close()


class UnitTestsWebAutomationYellowPagesCaymanIslandsWithDarkWebWithoutHeadless(unittest.TestCase):
    # ok
    def test_insert_the_subject_for_one_company_without_headless_with_dark_web(self):
        print('test_insert_the_subject_for_one_company_without_headless_with_dark_web')

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
        browser.get('https://www.findyello.com/cayman-islands/christopher-columbus-the/profile/')

        time.sleep(15)

        # insert the subject
        try:
            subject_input = browser.find_element_by_xpath(
                "/html/body/div[1]/div[1]/div[2]/div/div[1]/div[4]/form/div[1]/input[1]"
            )
            subject_input.clear()
            subject_input.send_keys(
                "Holomorphe company - Computer aided design files for free energy generator (Aether - zero point energy "
                "field)"
            )
            print("subject inserted")
        except Exception as e:
            print('error inserted subject : ' + str(e))

        time.sleep(15)

        browser.close()

    # ok
    def test_insert_the_name_and_surname_for_one_company_without_headless_with_dark_web(self):
        print('test_insert_the_name_and_surname_for_one_company_without_headless_with_dark_web')

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
        browser.get('https://www.findyello.com/cayman-islands/christopher-columbus-the/profile/')

        time.sleep(15)

        # insert the name and surname
        try:
            name_and_surname_input = browser.find_element_by_xpath(
                "/html/body/div[1]/div[1]/div[2]/div/div[1]/div[4]/form/div[2]/div[1]/input"
            )
            name_and_surname_input.clear()
            name_and_surname_input.send_keys(
                " "
            )
            print("name and surname inserted")
        except Exception as e:
            print('error name and surname inserted : ' + str(e))

        time.sleep(15)

        browser.close()

    # ok
    def test_insert_the_phone_number_for_one_company_without_headless_with_dark_web(self):
        print('test_insert_the_phone_number_for_one_company_without_headless_with_dark_web')

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
        browser.get('https://www.findyello.com/cayman-islands/christopher-columbus-the/profile/')

        time.sleep(15)

        # insert the phone number
        try:
            phone_number_input = browser.find_element_by_xpath(
                "/html/body/div[1]/div[1]/div[2]/div/div[1]/div[4]/form/div[2]/div[2]/input"
            )
            phone_number_input.clear()
            phone_number_input.send_keys(
                ""
            )
            print("phone number inserted")
        except Exception as e:
            print('error phone number inserted : ' + str(e))

        time.sleep(15)

        browser.close()

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
        browser.get('https://www.findyello.com/cayman-islands/christopher-columbus-the/profile/')

        time.sleep(15)

        # insert the email
        try:
            email_input = browser.find_element_by_xpath(
                "/html/body/div[1]/div[1]/div[2]/div/div[1]/div[4]/form/div[4]/div/input"
            )
            email_input.clear()
            email_input.send_keys(
                ".@holomorphe.com"
            )
            print("email inserted")
        except Exception as e:
            print('error email inserted : ' + str(e))

        time.sleep(15)

        browser.close()

    # non computer vision needed
    def test_click_on_the_anti_robot_button_for_one_company_without_headless_with_dark_web(self):
        print('test_click_on_the_anti_robot_button_for_one_company_without_headless_with_dark_web')

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
        browser.get('https://www.findyello.com/cayman-islands/christopher-columbus-the/profile/')

        time.sleep(15)

        # click on the anti robot button
        try:
            email_input = browser.find_element_by_xpath(
                "/html/body/div[1]/div[1]/div[2]/div/div[1]/div[4]/form/div[4]/div/input"
            )
            email_input.clear()
            email_input.send_keys(
                ".@holomorphe.com"
            )
            print("email inserted")

            time.sleep(5)

            n = 1
            actions = ActionChains(browser)
            actions.send_keys(Keys.TAB * n)
            actions.send_keys(Keys.ENTER)
            actions.perform()
            print("anti robot button clicked")

            time.sleep(5)
        except Exception as e:
            print('error anti robot button clicked : ' + str(e))

        time.sleep(15)

        browser.close()


if __name__ == '__main__':
    unittest.main()
