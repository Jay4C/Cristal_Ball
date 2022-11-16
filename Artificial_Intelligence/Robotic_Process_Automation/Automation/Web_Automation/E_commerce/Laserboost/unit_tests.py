import unittest
import time
import warnings
from selenium import webdriver


class UnitTestsWebAutomationLaserboost(unittest.TestCase):
    # ok
    def test_open_a_page(self):
        print('test_open_a_page')

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
        browser.get('https://www.laserboost.com/')

        time.sleep(5)

    # ok
    def test_se_connecter(self):
        print('test_se_connecter')

        email = ".@outlook.fr"

        password = ""

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
        browser.get('https://www.laserboost.com/')

        time.sleep(5)

        # Click on the "Accept" button
        accept_button = browser.find_element_by_xpath(
            '//*[@id="cookie_action_close_header"]'
        )
        accept_button.click()

        time.sleep(10)

        # Click on the "Account" button
        account_button = browser.find_element_by_xpath(
            "/html/body/div[1]/div/section/div/div/div[3]/div/div/section[1]/div/div/div[4]/div/div/div/div"
            "/div/a/span/span[2]"
        )
        account_button.click()

        time.sleep(10)

        # Insert the "E-Mail Address" input
        adresse_email_input = browser.find_element_by_xpath(
            '//*[@id="email"]'
        )
        adresse_email_input.send_keys(email)
        time.sleep(10)

        # Insert the "Password" input
        mot_de_passe_input = browser.find_element_by_xpath(
            '//*[@id="password"]'
        )
        mot_de_passe_input.send_keys(password)
        time.sleep(10)

        # Click on the "Log in" button
        log_in_button = browser.find_element_by_xpath(
            '/html/body/section/div/div/div/form/div[5]/button'
        )
        log_in_button.click()
        time.sleep(10)

    # ok
    def test_online_quote_1mm(self):
        print('test_online_quote_1mm')

        email = ".@outlook.fr"

        password = ""

        file = "A:\\1_Professionnel\\1_Holomorphe\\2_Archives\\2_Outils_Numeriques\\My_Tools\\Test\\Service" \
                    "\\Archives\\CAO\\3_My_Inventions\\Vibrating_Magnet_Electromagnetic_Generator" \
                    "\\Flower\\Version_3\\part_support.dxf"

        number_parts = 10

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
        browser.get('https://www.laserboost.com/')

        time.sleep(5)

        # Click on the "Accept" button
        accept_button = browser.find_element_by_xpath(
            '//*[@id="cookie_action_close_header"]'
        )
        accept_button.click()

        time.sleep(10)

        # Click on the "Account" button
        account_button = browser.find_element_by_xpath(
            "/html/body/div[1]/div/section/div/div/div[3]/div/div/section[1]/div/div/div[4]/div/div/div/div"
            "/div/a/span/span[2]"
        )
        account_button.click()

        time.sleep(10)

        # Insert the "E-Mail Address" input
        adresse_email_input = browser.find_element_by_xpath(
            '//*[@id="email"]'
        )
        adresse_email_input.send_keys(email)
        time.sleep(10)

        # Insert the "Password" input
        mot_de_passe_input = browser.find_element_by_xpath(
            '//*[@id="password"]'
        )
        mot_de_passe_input.send_keys(password)
        time.sleep(10)

        # Click on the "Log in" button
        log_in_button = browser.find_element_by_xpath(
            '/html/body/section/div/div/div/form/div[5]/button'
        )
        log_in_button.click()
        time.sleep(10)

        # Click on the "Online quote" button
        online_quote_button = browser.find_element_by_xpath(
            '/html/body/nav/div/div[3]/div[2]/ul/li[1]/a'
        )
        online_quote_button.click()
        time.sleep(10)

        # Insert the file
        file_input = browser.find_element_by_xpath(
            '/html/body/input'
        )
        file_input.send_keys(file)
        time.sleep(10)

        # Click on the 'carbon steel' select
        select_carbon_steel_button = browser.find_element_by_xpath(
            '/html/body/form/section/div[2]/div[2]/div/div[2]/div[2]/select/option[2]'
        )
        select_carbon_steel_button.click()
        print("select_carbon_steel_button.click()")
        time.sleep(5)

        # Click on the 'Carbon Steel - DC01 - 1mm to 3mm' select
        select_carbon_steel_dc01_1mm_to_3mm_button = browser.find_element_by_xpath(
            '/html/body/form/section/div[2]/div[2]/div/div[2]/div[2]/div[1]/select/option[2]'
        )
        select_carbon_steel_dc01_1mm_to_3mm_button.click()
        print("select_carbon_steel_dc01_1mm_to_3mm_button.click()")
        time.sleep(5)

        # Insert the number of parts
        number_parts_input = browser.find_element_by_xpath(
            '/html/body/form/section/div[2]/div[2]/div/div[2]/div[3]/div[1]/div[1]/div[2]/input'
        )
        number_parts_input.clear()
        number_parts_input.send_keys(number_parts)
        time.sleep(10)

        # Click on the 'Price per unit' text
        price_per_unit_input = browser.find_element_by_xpath(
            '/html/body/form/section/div[2]/div[2]/div/div[2]/div[3]/div[2]/div[2]/input'
        )
        price_per_unit_input.click()
        print("price_per_unit_input.click()")
        time.sleep(5)

        # Click on the 'select shipping' button
        select_shipping_button = browser.find_element_by_xpath(
            '/html/body/form/div/button'
        )
        select_shipping_button.click()
        print("select_shipping_button.click()")
        time.sleep(10)

        # Click on the 'select free shipping' button
        select_free_shipping_button = browser.find_element_by_xpath(
            '/html/body/section/form/div[1]/div[1]/div[5]/div[4]/div/label'
        )
        select_free_shipping_button.click()
        print("select_free_shipping_button.click()")
        time.sleep(10)

        # Click on the 'select shipping address' button
        select_shipping_address_button = browser.find_element_by_xpath(
            '/html/body/section/form/div[2]/button'
        )
        select_shipping_address_button.click()
        print("select_shipping_address_button.click()")
        time.sleep(10)

    # ok
    def test_online_quote_5mm(self):
        print('test_online_quote_5mm')

        email = ".@outlook.fr"

        password = ""

        file = "A:\\1_Professionnel\\1_Holomorphe\\2_Archives\\2_Outils_Numeriques\\My_Tools\\Test\\Service" \
                    "\\Archives\\CAO\\3_My_Inventions\\Vibrating_Magnet_Electromagnetic_Generator" \
                    "\\Flower\\Version_6\\part_support.dxf"

        number_parts = 13

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
        browser.get('https://www.laserboost.com/')

        time.sleep(5)

        # Click on the "Accept" button
        accept_button = browser.find_element_by_xpath(
            '//*[@id="cookie_action_close_header"]'
        )
        accept_button.click()

        time.sleep(10)

        # Click on the "Account" button
        account_button = browser.find_element_by_xpath(
            "/html/body/div[1]/div/section/div/div/div[3]/div/div/section[1]/div/div/div[4]/div/div/div/div"
            "/div/a/span/span[2]"
        )
        account_button.click()

        time.sleep(10)

        # Insert the "E-Mail Address" input
        adresse_email_input = browser.find_element_by_xpath(
            '//*[@id="email"]'
        )
        adresse_email_input.send_keys(email)
        time.sleep(10)

        # Insert the "Password" input
        mot_de_passe_input = browser.find_element_by_xpath(
            '//*[@id="password"]'
        )
        mot_de_passe_input.send_keys(password)
        time.sleep(10)

        # Click on the "Log in" button
        log_in_button = browser.find_element_by_xpath(
            '/html/body/section/div/div/div/form/div[5]/button'
        )
        log_in_button.click()
        time.sleep(10)

        # Click on the "Online quote" button
        online_quote_button = browser.find_element_by_xpath(
            '/html/body/nav/div/div[3]/div[2]/ul/li[1]/a'
        )
        online_quote_button.click()
        time.sleep(10)

        # Insert the file
        file_input = browser.find_element_by_xpath(
            '/html/body/input'
        )
        file_input.send_keys(file)
        time.sleep(10)

        # Click on the 'carbon steel' select
        select_carbon_steel_button = browser.find_element_by_xpath(
            '/html/body/form/section/div[2]/div[2]/div/div[2]/div[2]/select/option[2]'
        )
        select_carbon_steel_button.click()
        print("select_carbon_steel_button.click()")
        time.sleep(5)

        # Click on the 'Carbon Steel - DD11 S235JR – Unfinished (4mm to 6mm)' select
        select_carbon_steel_dd11_4mm_to_6mm_button = browser.find_element_by_xpath(
            '/html/body/form/section/div[2]/div[2]/div/div[2]/div[2]/div[1]/select/option[6]'
        )
        select_carbon_steel_dd11_4mm_to_6mm_button.click()
        print("select_carbon_steel_dd11_4mm_to_6mm_button.click()")
        time.sleep(5)

        # Click on the '5mm' button
        mm5_button = browser.find_element_by_xpath(
            '/html/body/form/section/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/label[2]'
        )
        mm5_button.click()
        print("mm5_button.click()")
        time.sleep(5)

        # Insert the number of parts
        number_parts_input = browser.find_element_by_xpath(
            '/html/body/form/section/div[2]/div[2]/div/div[2]/div[3]/div[1]/div[1]/div[2]/input'
        )
        number_parts_input.clear()
        number_parts_input.send_keys(number_parts)
        time.sleep(10)

        # Click on the 'Price per unit' text
        price_per_unit_input = browser.find_element_by_xpath(
            '/html/body/form/section/div[2]/div[2]/div/div[2]/div[3]/div[2]/div[2]/input'
        )
        price_per_unit_input.click()
        print("price_per_unit_input.click()")
        time.sleep(5)

        # Click on the 'select shipping' button
        select_shipping_button = browser.find_element_by_xpath(
            '/html/body/form/div/button'
        )
        select_shipping_button.click()
        print("select_shipping_button.click()")
        time.sleep(10)

        # Click on the 'select free shipping' button
        select_free_shipping_button = browser.find_element_by_xpath(
            '/html/body/section/form/div[1]/div[1]/div[5]/div[4]/div/label'
        )
        select_free_shipping_button.click()
        print("select_free_shipping_button.click()")
        time.sleep(10)

        # Click on the 'select shipping address' button
        select_shipping_address_button = browser.find_element_by_xpath(
            '/html/body/section/form/div[2]/button'
        )
        select_shipping_address_button.click()
        print("select_shipping_address_button.click()")
        time.sleep(10)


if __name__ == '__main__':
    unittest.main()
