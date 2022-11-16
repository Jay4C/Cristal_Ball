import unittest
import time
import warnings
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


class UnitTestsWebAutomationNoIP(unittest.TestCase):
    def test_update_hostname_without_headless(self):
        print("test_update_hostname_without_headless")

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        # with Firefox
        browser = webdriver.Firefox(executable_path='..\\geckodriver.exe')

        time.sleep(10)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get('https://www.noip.com/')
        print("page opened")

        time.sleep(10)

        # Click on the 'Sign in' button
        sign_in_button = browser.find_element_by_xpath(
            "/html/body/section[2]/div/ul/li[1]/a"
        )
        sign_in_button.click()
        print("sign_in_button clicked")

        time.sleep(10)

        # Insert the email
        email_input = browser.find_element_by_xpath(
            "/html/body/section[4]/div/div/div[2]/form/input[1]"
        )
        email_input.clear()
        email_input.send_keys(".@holomorphe.com")
        print("email_input inserted")

        time.sleep(10)

        # Insert the password
        password_input = browser.find_element_by_xpath(
            "/html/body/section[4]/div/div/div[2]/form/input[2]"
        )
        password_input.clear()
        password_input.send_keys("")
        print("password_input inserted")

        time.sleep(10)

        # Click on the 'Sign in v1' button
        sign_in_v1_button = browser.find_element_by_xpath(
            "/html/body/section[4]/div/div/div[2]/form/button"
        )
        sign_in_v1_button.click()
        print("sign_in_v1_button clicked")

        time.sleep(15)

        # Open the "https://my.noip.com/dynamic-dns"
        browser.get("https://my.noip.com/dynamic-dns")

        time.sleep(10)

        # Click on the "modify_hostname_button" button
        modify_hostname_button = browser.find_element_by_xpath(
            "/html/body/div[2]/div/div/div[3]/div[1]/div[2]/div/div/div[1]/div[1]/table/tbody/tr/td[5]/button"
        )
        modify_hostname_button.click()
        print("hostname_button clicked")

        time.sleep(10)

        # Click on the "update" button
        update_button = browser.find_element_by_xpath(
            "/html/body/div[2]/div/div/div[3]/div[4]/div/div/div/div[4]/button[1]/div"
        )
        update_button.click()
        print("update_button clicked")

        time.sleep(10)

        # Open the "https://my.noip.com/logout"
        browser.get("https://my.noip.com/logout")

        time.sleep(10)

        browser.close()
        print("browser closed")

    def test_update_hostname_with_headless(self):
        print("test_update_hostname_with_headless")

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        # with Firefox
        options = Options()
        options.headless = True
        browser = webdriver.Firefox(executable_path='..\\geckodriver.exe', options=options)

        time.sleep(10)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get('https://www.noip.com/')
        print("page opened")

        time.sleep(10)

        # Click on the 'Sign in' button
        sign_in_button = browser.find_element_by_xpath(
            "/html/body/section[2]/div/ul/li[1]/a"
        )
        sign_in_button.click()
        print("sign_in_button clicked")

        time.sleep(10)

        # Insert the email
        email_input = browser.find_element_by_xpath(
            "/html/body/section[4]/div/div/div[2]/form/input[1]"
        )
        email_input.clear()
        email_input.send_keys(".@holomorphe.com")
        print("email_input inserted")

        time.sleep(10)

        # Insert the password
        password_input = browser.find_element_by_xpath(
            "/html/body/section[4]/div/div/div[2]/form/input[2]"
        )
        password_input.clear()
        password_input.send_keys("")
        print("password_input inserted")

        time.sleep(10)

        # Click on the 'Sign in v1' button
        sign_in_v1_button = browser.find_element_by_xpath(
            "/html/body/section[4]/div/div/div[2]/form/button"
        )
        sign_in_v1_button.click()
        print("sign_in_v1_button clicked")

        time.sleep(15)

        # Open the "https://my.noip.com/dynamic-dns"
        browser.get("https://my.noip.com/dynamic-dns")
        print("https://my.noip.com/dynamic-dns opened")

        time.sleep(10)

        # Click on the "modify_hostname_button" button
        modify_hostname_button = browser.find_element_by_xpath(
            "/html/body/div[2]/div/div/div[3]/div[1]/div[2]/div/div/div[1]/div[1]/table/tbody/tr/td[5]/button"
        )
        modify_hostname_button.click()
        print("hostname_button clicked")

        time.sleep(10)

        # Click on the "update" button
        update_button = browser.find_element_by_xpath(
            "/html/body/div[2]/div/div/div[3]/div[4]/div/div/div/div[4]/button[1]/div"
        )
        update_button.click()
        print("update_button clicked")

        time.sleep(10)

        # Open the "https://my.noip.com/logout"
        browser.get("https://my.noip.com/logout")
        print("https://my.noip.com/logout opened")

        time.sleep(10)

        browser.close()
        print("browser closed")


if __name__ == '__main__':
    unittest.main()
