import os
import unittest
import time
import warnings
from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.options import Options


class UnitTestsWebAutomationHolomorpheWebsite(unittest.TestCase):
    def test_generate_html_to_pdf_twelve_month_operating_budget(self):
        print("test_generate_html_to_pdf_twelve_month_operating_budget")

        time.sleep(1)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(1)

        # with Firefox
        browser = webdriver.Firefox(executable_path='geckodriver.exe')

        time.sleep(1)

        # maximize window
        browser.maximize_window()

        time.sleep(1)

        # open the report
        # browser.get('http://127.0.0.1:8000/reporting/twelve_month_operating_budget')
        browser.get('https://holomorphe.com/reporting/twelve_month_operating_budget')

        time.sleep(5)

        # fill company name
        company_name = browser.find_element_by_name("company_name")
        company_name.clear()
        company_name.send_keys("company_name")

        time.sleep(1)

        # fill share_capital
        share_capital = browser.find_element_by_name("share_capital")
        share_capital.clear()
        share_capital.send_keys("share_capital")
        time.sleep(1)

        # fill head_office_address
        head_office_address = browser.find_element_by_name("head_office_address")
        head_office_address.clear()
        head_office_address.send_keys("head_office_address")

        time.sleep(1)

        # fill establishment_number
        establishment_number = browser.find_element_by_name("establishment_number")
        establishment_number.clear()
        establishment_number.send_keys("establishment_number")

        time.sleep(1)

        # fill register_of_trade_and_companies
        register_of_trade_and_companies = browser.find_element_by_name("register_of_trade_and_companies")
        register_of_trade_and_companies.clear()
        register_of_trade_and_companies.send_keys("register_of_trade_and_companies")
        time.sleep(1)

        # fill main_activities
        main_activities = browser.find_element_by_name("main_activities")
        main_activities.clear()
        main_activities.send_keys("main_activities")
        time.sleep(1)

        # fill activity_number
        activity_number = browser.find_element_by_name("activity_number")
        activity_number.clear()
        activity_number.send_keys("activity_number")

        time.sleep(1)

        # fill intra_community_vat_number
        intra_community_vat_number = browser.find_element_by_name("intra_community_vat_number")
        intra_community_vat_number.clear()
        intra_community_vat_number.send_keys("intra_community_vat_number")
        time.sleep(1)

        # fill president
        president = browser.find_element_by_name("president")
        president.clear()
        president.send_keys("president")
        time.sleep(1)

        # fill registration_date
        registration_date = browser.find_element_by_name("registration_date")
        registration_date.clear()
        registration_date.send_keys("registration_date")
        time.sleep(1)

        # fill r1c1
        r1c1 = browser.find_element_by_name("r1c1")
        r1c1.clear()
        r1c1.send_keys("r1c1")

        # fill r1c2
        r1c2 = browser.find_element_by_name("r1c2")
        r1c2.clear()
        r1c2.send_keys("r1c2")

        # fill r1c3
        r1c3 = browser.find_element_by_name("r1c3")
        r1c3.clear()
        r1c3.send_keys("r1c3")

        # fill r1c4
        r1c4 = browser.find_element_by_name("r1c4")
        r1c4.clear()
        r1c4.send_keys("r1c4")

        # fill r1c5
        r1c5 = browser.find_element_by_name("r1c5")
        r1c5.clear()
        r1c5.send_keys("r1c5")

        # fill r1c6
        r1c6 = browser.find_element_by_name("r1c6")
        r1c6.clear()
        r1c6.send_keys("r1c6")

        # fill r1c7
        r1c7 = browser.find_element_by_name("r1c7")
        r1c7.clear()
        r1c7.send_keys("r1c7")

        # fill r1c8
        r1c8 = browser.find_element_by_name("r1c8")
        r1c8.clear()
        r1c8.send_keys("r1c8")

        # fill r1c9
        r1c9 = browser.find_element_by_name("r1c9")
        r1c9.clear()
        r1c9.send_keys("r1c9")

        # fill r1c10
        r1c10 = browser.find_element_by_name("r1c10")
        r1c10.clear()
        r1c10.send_keys("r1c10")

        # fill r1c11
        r1c11 = browser.find_element_by_name("r1c11")
        r1c11.clear()
        r1c11.send_keys("r1c11")

        # fill r1c12
        r1c12 = browser.find_element_by_name("r1c12")
        r1c12.clear()
        r1c12.send_keys("r1c12")

        # fill r1c13
        r1c13 = browser.find_element_by_name("r1c13")
        r1c13.clear()
        r1c13.send_keys("r1c13")

        # fill r2c1
        r2c1 = browser.find_element_by_name("r2c1")
        r2c1.clear()
        r2c1.send_keys("r2c1")

        # fill r2c2
        r2c2 = browser.find_element_by_name("r2c2")
        r2c2.clear()
        r2c2.send_keys("r2c2")

        # fill r2c3
        r2c3 = browser.find_element_by_name("r2c3")
        r2c3.clear()
        r2c3.send_keys("r2c3")

        # fill r2c4
        r2c4 = browser.find_element_by_name("r2c4")
        r2c4.clear()
        r2c4.send_keys("r2c4")

        # fill r2c5
        r2c5 = browser.find_element_by_name("r2c5")
        r2c5.clear()
        r2c5.send_keys("r2c5")

        # fill r2c6
        r2c6 = browser.find_element_by_name("r2c6")
        r2c6.clear()
        r2c6.send_keys("r2c6")

        # fill r2c7
        r2c7 = browser.find_element_by_name("r2c7")
        r2c7.clear()
        r2c7.send_keys("r2c7")

        # fill r2c8
        r2c8 = browser.find_element_by_name("r2c8")
        r2c8.clear()
        r2c8.send_keys("r2c8")

        # fill r2c9
        r2c9 = browser.find_element_by_name("r2c9")
        r2c9.clear()
        r2c9.send_keys("r2c9")

        # fill r2c10
        r2c10 = browser.find_element_by_name("r2c10")
        r2c10.clear()
        r2c10.send_keys("r2c10")

        # fill r2c11
        r2c11 = browser.find_element_by_name("r2c11")
        r2c11.clear()
        r2c11.send_keys("r2c11")

        # fill r2c12
        r2c12 = browser.find_element_by_name("r2c12")
        r2c12.clear()
        r2c12.send_keys("r2c12")

        # fill r2c13
        r2c13 = browser.find_element_by_name("r2c13")
        r2c13.clear()
        r2c13.send_keys("r2c13")

        # fill r3c1
        r3c1 = browser.find_element_by_name("r3c1")
        r3c1.clear()
        r3c1.send_keys("r3c1")

        # fill r3c2
        r3c2 = browser.find_element_by_name("r3c2")
        r3c2.clear()
        r3c2.send_keys("r3c2")

        # fill r3c3
        r3c3 = browser.find_element_by_name("r3c3")
        r3c3.clear()
        r3c3.send_keys("r3c3")

        # fill r3c4
        r3c4 = browser.find_element_by_name("r3c4")
        r3c4.clear()
        r3c4.send_keys("r3c4")

        # fill r3c5
        r3c5 = browser.find_element_by_name("r3c5")
        r3c5.clear()
        r3c5.send_keys("r3c5")

        # fill r3c6
        r3c6 = browser.find_element_by_name("r3c6")
        r3c6.clear()
        r3c6.send_keys("r3c6")

        # fill r3c7
        r3c7 = browser.find_element_by_name("r3c7")
        r3c7.clear()
        r3c7.send_keys("r3c7")

        # fill r3c8
        r3c8 = browser.find_element_by_name("r3c8")
        r3c8.clear()
        r3c8.send_keys("r3c8")

        # fill r3c9
        r3c9 = browser.find_element_by_name("r3c9")
        r3c9.clear()
        r3c9.send_keys("r3c9")

        # fill r3c10
        r3c10 = browser.find_element_by_name("r3c10")
        r3c10.clear()
        r3c10.send_keys("r3c10")

        # fill r3c11
        r3c11 = browser.find_element_by_name("r3c11")
        r3c11.clear()
        r3c11.send_keys("r3c11")

        # fill r3c12
        r3c12 = browser.find_element_by_name("r3c12")
        r3c12.clear()
        r3c12.send_keys("r3c12")

        # fill r3c13
        r3c13 = browser.find_element_by_name("r3c13")
        r3c13.clear()
        r3c13.send_keys("r3c13")

        # fill r4c1
        r4c1 = browser.find_element_by_name("r4c1")
        r4c1.clear()
        r4c1.send_keys("r4c1")

        # fill r4c2
        r4c2 = browser.find_element_by_name("r4c2")
        r4c2.clear()
        r4c2.send_keys("r4c2")

        # fill r4c3
        r4c3 = browser.find_element_by_name("r4c3")
        r4c3.clear()
        r4c3.send_keys("r4c3")

        # fill r4c4
        r4c4 = browser.find_element_by_name("r4c4")
        r4c4.clear()
        r4c4.send_keys("r4c4")

        # fill r4c5
        r4c5 = browser.find_element_by_name("r4c5")
        r4c5.clear()
        r4c5.send_keys("r4c5")

        # fill r4c6
        r4c6 = browser.find_element_by_name("r4c6")
        r4c6.clear()
        r4c6.send_keys("r4c6")

        # fill r4c7
        r4c7 = browser.find_element_by_name("r4c7")
        r4c7.clear()
        r4c7.send_keys("r4c7")

        # fill r4c8
        r4c8 = browser.find_element_by_name("r4c8")
        r4c8.clear()
        r4c8.send_keys("r4c8")

        # fill r4c9
        r4c9 = browser.find_element_by_name("r4c9")
        r4c9.clear()
        r4c9.send_keys("r4c9")

        # fill r4c10
        r4c10 = browser.find_element_by_name("r4c10")
        r4c10.clear()
        r4c10.send_keys("r4c10")

        # fill r4c11
        r4c11 = browser.find_element_by_name("r4c11")
        r4c11.clear()
        r4c11.send_keys("r4c11")

        # fill r4c12
        r4c12 = browser.find_element_by_name("r4c12")
        r4c12.clear()
        r4c12.send_keys("r4c12")

        # fill r4c13
        r4c13 = browser.find_element_by_name("r4c13")
        r4c13.clear()
        r4c13.send_keys("r4c13")

        # fill r5c1
        r5c1 = browser.find_element_by_name("r5c1")
        r5c1.clear()
        r5c1.send_keys("r5c1")

        # fill r5c2
        r5c2 = browser.find_element_by_name("r5c2")
        r5c2.clear()
        r5c2.send_keys("r5c2")

        # fill r5c3
        r5c3 = browser.find_element_by_name("r5c3")
        r5c3.clear()
        r5c3.send_keys("r5c3")

        # fill r5c4
        r5c4 = browser.find_element_by_name("r5c4")
        r5c4.clear()
        r5c4.send_keys("r5c4")

        # fill r5c5
        r5c5 = browser.find_element_by_name("r5c5")
        r5c5.clear()
        r5c5.send_keys("r5c5")

        # fill r5c6
        r5c6 = browser.find_element_by_name("r5c6")
        r5c6.clear()
        r5c6.send_keys("r5c6")

        # fill r5c7
        r5c7 = browser.find_element_by_name("r5c7")
        r5c7.clear()
        r5c7.send_keys("r5c7")

        # fill r5c8
        r5c8 = browser.find_element_by_name("r5c8")
        r5c8.clear()
        r5c8.send_keys("r5c8")

        # fill r5c9
        r5c9 = browser.find_element_by_name("r5c9")
        r5c9.clear()
        r5c9.send_keys("r5c9")

        # fill r5c10
        r5c10 = browser.find_element_by_name("r5c10")
        r5c10.clear()
        r5c10.send_keys("r5c10")

        # fill r5c11
        r5c11 = browser.find_element_by_name("r5c11")
        r5c11.clear()
        r5c11.send_keys("r5c11")

        # fill r5c12
        r5c12 = browser.find_element_by_name("r5c12")
        r5c12.clear()
        r5c12.send_keys("r5c12")

        # fill r5c13
        r5c13 = browser.find_element_by_name("r5c13")
        r5c13.clear()
        r5c13.send_keys("r5c13")

        # fill r6c1
        r6c1 = browser.find_element_by_name("r6c1")
        r6c1.clear()
        r6c1.send_keys("r6c1")

        # fill r6c2
        r6c2 = browser.find_element_by_name("r6c2")
        r6c2.clear()
        r6c2.send_keys("r6c2")

        # fill r6c3
        r6c3 = browser.find_element_by_name("r6c3")
        r6c3.clear()
        r6c3.send_keys("r6c3")

        # fill r6c4
        r6c4 = browser.find_element_by_name("r6c4")
        r6c4.clear()
        r6c4.send_keys("r6c4")

        # fill r6c5
        r6c5 = browser.find_element_by_name("r6c5")
        r6c5.clear()
        r6c5.send_keys("r6c5")

        # fill r6c6
        r6c6 = browser.find_element_by_name("r6c6")
        r6c6.clear()
        r6c6.send_keys("r6c6")

        # fill r6c7
        r6c7 = browser.find_element_by_name("r6c7")
        r6c7.clear()
        r6c7.send_keys("r6c7")

        # fill r6c8
        r6c8 = browser.find_element_by_name("r6c8")
        r6c8.clear()
        r6c8.send_keys("r6c8")

        # fill r6c9
        r6c9 = browser.find_element_by_name("r6c9")
        r6c9.clear()
        r6c9.send_keys("r6c9")

        # fill r6c10
        r6c10 = browser.find_element_by_name("r6c10")
        r6c10.clear()
        r6c10.send_keys("r6c10")

        # fill r6c11
        r6c11 = browser.find_element_by_name("r6c11")
        r6c11.clear()
        r6c11.send_keys("r6c11")

        # fill r6c12
        r6c12 = browser.find_element_by_name("r6c12")
        r6c12.clear()
        r6c12.send_keys("r6c12")

        # fill r6c13
        r6c13 = browser.find_element_by_name("r6c13")
        r6c13.clear()
        r6c13.send_keys("r6c13")

        # fill r7c1
        r7c1 = browser.find_element_by_name("r7c1")
        r7c1.clear()
        r7c1.send_keys("r7c1")

        # fill r7c2
        r7c2 = browser.find_element_by_name("r7c2")
        r7c2.clear()
        r7c2.send_keys("r7c2")

        # fill r7c3
        r7c3 = browser.find_element_by_name("r7c3")
        r7c3.clear()
        r7c3.send_keys("r7c3")

        # fill r7c4
        r7c4 = browser.find_element_by_name("r7c4")
        r7c4.clear()
        r7c4.send_keys("r7c4")

        # fill r7c5
        r7c5 = browser.find_element_by_name("r7c5")
        r7c5.clear()
        r7c5.send_keys("r7c5")

        # fill r7c6
        r7c6 = browser.find_element_by_name("r7c6")
        r7c6.clear()
        r7c6.send_keys("r7c6")

        # fill r7c7
        r7c7 = browser.find_element_by_name("r7c7")
        r7c7.clear()
        r7c7.send_keys("r7c7")

        # fill r7c8
        r7c8 = browser.find_element_by_name("r7c8")
        r7c8.clear()
        r7c8.send_keys("r7c8")

        # fill r7c9
        r7c9 = browser.find_element_by_name("r7c9")
        r7c9.clear()
        r7c9.send_keys("r7c9")

        # fill r7c10
        r7c10 = browser.find_element_by_name("r7c10")
        r7c10.clear()
        r7c10.send_keys("r7c10")

        # fill r7c11
        r7c11 = browser.find_element_by_name("r7c11")
        r7c11.clear()
        r7c11.send_keys("r7c11")

        # fill r7c12
        r7c12 = browser.find_element_by_name("r7c12")
        r7c12.clear()
        r7c12.send_keys("r7c12")

        # fill r7c13
        r7c13 = browser.find_element_by_name("r7c13")
        r7c13.clear()
        r7c13.send_keys("r7c13")

        # fill r8c1
        r8c1 = browser.find_element_by_name("r8c1")
        r8c1.clear()
        r8c1.send_keys("r8c1")

        # fill r8c2
        r8c2 = browser.find_element_by_name("r8c2")
        r8c2.clear()
        r8c2.send_keys("r8c2")

        # fill r8c3
        r8c3 = browser.find_element_by_name("r8c3")
        r8c3.clear()
        r8c3.send_keys("r8c3")

        # fill r8c4
        r8c4 = browser.find_element_by_name("r8c4")
        r8c4.clear()
        r8c4.send_keys("r8c4")

        # fill r8c5
        r8c5 = browser.find_element_by_name("r8c5")
        r8c5.clear()
        r8c5.send_keys("r8c5")

        # fill r8c6
        r8c6 = browser.find_element_by_name("r8c6")
        r8c6.clear()
        r8c6.send_keys("r8c6")

        # fill r8c7
        r8c7 = browser.find_element_by_name("r8c7")
        r8c7.clear()
        r8c7.send_keys("r8c7")

        # fill r8c8
        r8c8 = browser.find_element_by_name("r8c8")
        r8c8.clear()
        r8c8.send_keys("r8c8")

        # fill r8c9
        r8c9 = browser.find_element_by_name("r8c9")
        r8c9.clear()
        r8c9.send_keys("r8c9")

        # fill r8c10
        r8c10 = browser.find_element_by_name("r8c10")
        r8c10.clear()
        r8c10.send_keys("r8c10")

        # fill r8c11
        r8c11 = browser.find_element_by_name("r8c11")
        r8c11.clear()
        r8c11.send_keys("r8c11")

        # fill r8c12
        r8c12 = browser.find_element_by_name("r8c12")
        r8c12.clear()
        r8c12.send_keys("r8c12")

        # fill r8c13
        r8c13 = browser.find_element_by_name("r8c13")
        r8c13.clear()
        r8c13.send_keys("r8c13")

        # fill r9c1
        r9c1 = browser.find_element_by_name("r9c1")
        r9c1.clear()
        r9c1.send_keys("r9c1")

        # fill r9c2
        r9c2 = browser.find_element_by_name("r9c2")
        r9c2.clear()
        r9c2.send_keys("r9c2")

        # fill r9c3
        r9c3 = browser.find_element_by_name("r9c3")
        r9c3.clear()
        r9c3.send_keys("r9c3")

        # fill r9c4
        r9c4 = browser.find_element_by_name("r9c4")
        r9c4.clear()
        r9c4.send_keys("r9c4")

        # fill r9c5
        r9c5 = browser.find_element_by_name("r9c5")
        r9c5.clear()
        r9c5.send_keys("r9c5")

        # fill r9c6
        r9c6 = browser.find_element_by_name("r9c6")
        r9c6.clear()
        r9c6.send_keys("r9c6")

        # fill r9c7
        r9c7 = browser.find_element_by_name("r9c7")
        r9c7.clear()
        r9c7.send_keys("r9c7")

        # fill r9c8
        r9c8 = browser.find_element_by_name("r9c8")
        r9c8.clear()
        r9c8.send_keys("r9c8")

        # fill r9c9
        r9c9 = browser.find_element_by_name("r9c9")
        r9c9.clear()
        r9c9.send_keys("r9c9")

        # fill r9c10
        r9c10 = browser.find_element_by_name("r9c10")
        r9c10.clear()
        r9c10.send_keys("r9c10")

        # fill r9c11
        r9c11 = browser.find_element_by_name("r9c11")
        r9c11.clear()
        r9c11.send_keys("r9c11")

        # fill r9c12
        r9c12 = browser.find_element_by_name("r9c12")
        r9c12.clear()
        r9c12.send_keys("r9c12")

        # fill r9c13
        r9c13 = browser.find_element_by_name("r9c13")
        r9c13.clear()
        r9c13.send_keys("r9c13")

        # fill r10c1
        r10c1 = browser.find_element_by_name("r10c1")
        r10c1.clear()
        r10c1.send_keys("r10c1")

        # fill r10c2
        r10c2 = browser.find_element_by_name("r10c2")
        r10c2.clear()
        r10c2.send_keys("r10c2")

        # fill r10c3
        r10c3 = browser.find_element_by_name("r10c3")
        r10c3.clear()
        r10c3.send_keys("r10c3")

        # fill r10c4
        r10c4 = browser.find_element_by_name("r10c4")
        r10c4.clear()
        r10c4.send_keys("r10c4")

        # fill r10c5
        r10c5 = browser.find_element_by_name("r10c5")
        r10c5.clear()
        r10c5.send_keys("r10c5")

        # fill r10c6
        r10c6 = browser.find_element_by_name("r10c6")
        r10c6.clear()
        r10c6.send_keys("r10c6")

        # fill r10c7
        r10c7 = browser.find_element_by_name("r10c7")
        r10c7.clear()
        r10c7.send_keys("r10c7")

        # fill r10c8
        r10c8 = browser.find_element_by_name("r10c8")
        r10c8.clear()
        r10c8.send_keys("r10c8")

        # fill r10c9
        r10c9 = browser.find_element_by_name("r10c9")
        r10c9.clear()
        r10c9.send_keys("r10c9")

        # fill r10c10
        r10c10 = browser.find_element_by_name("r10c10")
        r10c10.clear()
        r10c10.send_keys("r10c10")

        # fill r10c11
        r10c11 = browser.find_element_by_name("r10c11")
        r10c11.clear()
        r10c11.send_keys("r10c11")

        # fill r10c12
        r10c12 = browser.find_element_by_name("r10c12")
        r10c12.clear()
        r10c12.send_keys("r10c12")

        # fill r10c13
        r10c13 = browser.find_element_by_name("r10c13")
        r10c13.clear()
        r10c13.send_keys("r10c13")

        # fill r11c1
        r11c1 = browser.find_element_by_name("r11c1")
        r11c1.clear()
        r11c1.send_keys("r11c1")

        # fill r11c2
        r11c2 = browser.find_element_by_name("r11c2")
        r11c2.clear()
        r11c2.send_keys("r11c2")

        # fill r11c3
        r11c3 = browser.find_element_by_name("r11c3")
        r11c3.clear()
        r11c3.send_keys("r11c3")

        # fill r11c4
        r11c4 = browser.find_element_by_name("r11c4")
        r11c4.clear()
        r11c4.send_keys("r11c4")

        # fill r11c5
        r11c5 = browser.find_element_by_name("r11c5")
        r11c5.clear()
        r11c5.send_keys("r11c5")

        # fill r11c6
        r11c6 = browser.find_element_by_name("r11c6")
        r11c6.clear()
        r11c6.send_keys("r11c6")

        # fill r11c7
        r11c7 = browser.find_element_by_name("r11c7")
        r11c7.clear()
        r11c7.send_keys("r11c7")

        # fill r11c8
        r11c8 = browser.find_element_by_name("r11c8")
        r11c8.clear()
        r11c8.send_keys("r11c8")

        # fill r11c9
        r11c9 = browser.find_element_by_name("r11c9")
        r11c9.clear()
        r11c9.send_keys("r11c9")

        # fill r11c10
        r11c10 = browser.find_element_by_name("r11c10")
        r11c10.clear()
        r11c10.send_keys("r11c10")

        # fill r11c11
        r11c11 = browser.find_element_by_name("r11c11")
        r11c11.clear()
        r11c11.send_keys("r11c11")

        # fill r11c12
        r11c12 = browser.find_element_by_name("r11c12")
        r11c12.clear()
        r11c12.send_keys("r11c12")

        # fill r11c13
        r11c13 = browser.find_element_by_name("r11c13")
        r11c13.clear()
        r11c13.send_keys("r11c13")

        # fill r12c1
        r12c1 = browser.find_element_by_name("r12c1")
        r12c1.clear()
        r12c1.send_keys("r12c1")

        # fill r12c2
        r12c2 = browser.find_element_by_name("r12c2")
        r12c2.clear()
        r12c2.send_keys("r12c2")

        # fill r12c3
        r12c3 = browser.find_element_by_name("r12c3")
        r12c3.clear()
        r12c3.send_keys("r12c3")

        # fill r12c4
        r12c4 = browser.find_element_by_name("r12c4")
        r12c4.clear()
        r12c4.send_keys("r12c4")

        # fill r12c5
        r12c5 = browser.find_element_by_name("r12c5")
        r12c5.clear()
        r12c5.send_keys("r12c5")

        # fill r12c6
        r12c6 = browser.find_element_by_name("r12c6")
        r12c6.clear()
        r12c6.send_keys("r12c6")

        # fill r12c7
        r12c7 = browser.find_element_by_name("r12c7")
        r12c7.clear()
        r12c7.send_keys("r12c7")

        # fill r12c8
        r12c8 = browser.find_element_by_name("r12c8")
        r12c8.clear()
        r12c8.send_keys("r12c8")

        # fill r12c9
        r12c9 = browser.find_element_by_name("r12c9")
        r12c9.clear()
        r12c9.send_keys("r12c9")

        # fill r12c10
        r12c10 = browser.find_element_by_name("r12c10")
        r12c10.clear()
        r12c10.send_keys("r12c10")

        # fill r12c11
        r12c11 = browser.find_element_by_name("r12c11")
        r12c11.clear()
        r12c11.send_keys("r12c11")

        # fill r12c12
        r12c12 = browser.find_element_by_name("r12c12")
        r12c12.clear()
        r12c12.send_keys("r12c12")

        # fill r12c13
        r12c13 = browser.find_element_by_name("r12c13")
        r12c13.clear()
        r12c13.send_keys("r12c13")

        # fill r13c1
        r13c1 = browser.find_element_by_name("r13c1")
        r13c1.clear()
        r13c1.send_keys("r13c1")

        # fill r13c2
        r13c2 = browser.find_element_by_name("r13c2")
        r13c2.clear()
        r13c2.send_keys("r13c2")

        # fill r13c3
        r13c3 = browser.find_element_by_name("r13c3")
        r13c3.clear()
        r13c3.send_keys("r13c3")

        # fill r13c4
        r13c4 = browser.find_element_by_name("r13c4")
        r13c4.clear()
        r13c4.send_keys("r13c4")

        # fill r13c5
        r13c5 = browser.find_element_by_name("r13c5")
        r13c5.clear()
        r13c5.send_keys("r13c5")

        # fill r13c6
        r13c6 = browser.find_element_by_name("r13c6")
        r13c6.clear()
        r13c6.send_keys("r13c6")

        # fill r13c7
        r13c7 = browser.find_element_by_name("r13c7")
        r13c7.clear()
        r13c7.send_keys("r13c7")

        # fill r13c8
        r13c8 = browser.find_element_by_name("r13c8")
        r13c8.clear()
        r13c8.send_keys("r13c8")

        # fill r13c9
        r13c9 = browser.find_element_by_name("r13c9")
        r13c9.clear()
        r13c9.send_keys("r13c9")

        # fill r13c10
        r13c10 = browser.find_element_by_name("r13c10")
        r13c10.clear()
        r13c10.send_keys("r13c10")

        # fill r13c11
        r13c11 = browser.find_element_by_name("r13c11")
        r13c11.clear()
        r13c11.send_keys("r13c11")

        # fill r13c12
        r13c12 = browser.find_element_by_name("r13c12")
        r13c12.clear()
        r13c12.send_keys("r13c12")

        # fill r13c13
        r13c13 = browser.find_element_by_name("r13c13")
        r13c13.clear()
        r13c13.send_keys("r13c13")

        # fill r14c1
        r14c1 = browser.find_element_by_name("r14c1")
        r14c1.clear()
        r14c1.send_keys("r14c1")

        # fill r14c2
        r14c2 = browser.find_element_by_name("r14c2")
        r14c2.clear()
        r14c2.send_keys("r14c2")

        # fill r14c3
        r14c3 = browser.find_element_by_name("r14c3")
        r14c3.clear()
        r14c3.send_keys("r14c3")

        # fill r14c4
        r14c4 = browser.find_element_by_name("r14c4")
        r14c4.clear()
        r14c4.send_keys("r14c4")

        # fill r14c5
        r14c5 = browser.find_element_by_name("r14c5")
        r14c5.clear()
        r14c5.send_keys("r14c5")

        # fill r14c6
        r14c6 = browser.find_element_by_name("r14c6")
        r14c6.clear()
        r14c6.send_keys("r14c6")

        # fill r14c7
        r14c7 = browser.find_element_by_name("r14c7")
        r14c7.clear()
        r14c7.send_keys("r14c7")

        # fill r14c8
        r14c8 = browser.find_element_by_name("r14c8")
        r14c8.clear()
        r14c8.send_keys("r14c8")

        # fill r14c9
        r14c9 = browser.find_element_by_name("r14c9")
        r14c9.clear()
        r14c9.send_keys("r14c9")

        # fill r14c10
        r14c10 = browser.find_element_by_name("r14c10")
        r14c10.clear()
        r14c10.send_keys("r14c10")

        # fill r14c11
        r14c11 = browser.find_element_by_name("r14c11")
        r14c11.clear()
        r14c11.send_keys("r14c11")

        # fill r14c12
        r14c12 = browser.find_element_by_name("r14c12")
        r14c12.clear()
        r14c12.send_keys("r14c12")

        # fill r14c13
        r14c13 = browser.find_element_by_name("r14c13")
        r14c13.clear()
        r14c13.send_keys("r14c13")

        # fill r15c1
        r15c1 = browser.find_element_by_name("r15c1")
        r15c1.clear()
        r15c1.send_keys("r15c1")

        # fill r15c2
        r15c2 = browser.find_element_by_name("r15c2")
        r15c2.clear()
        r15c2.send_keys("r15c2")

        # fill r15c3
        r15c3 = browser.find_element_by_name("r15c3")
        r15c3.clear()
        r15c3.send_keys("r15c3")

        # fill r15c4
        r15c4 = browser.find_element_by_name("r15c4")
        r15c4.clear()
        r15c4.send_keys("r15c4")

        # fill r15c5
        r15c5 = browser.find_element_by_name("r15c5")
        r15c5.clear()
        r15c5.send_keys("r15c5")

        # fill r15c6
        r15c6 = browser.find_element_by_name("r15c6")
        r15c6.clear()
        r15c6.send_keys("r15c6")

        # fill r15c7
        r15c7 = browser.find_element_by_name("r15c7")
        r15c7.clear()
        r15c7.send_keys("r15c7")

        # fill r15c8
        r15c8 = browser.find_element_by_name("r15c8")
        r15c8.clear()
        r15c8.send_keys("r15c8")

        # fill r15c9
        r15c9 = browser.find_element_by_name("r15c9")
        r15c9.clear()
        r15c9.send_keys("r15c9")

        # fill r15c10
        r15c10 = browser.find_element_by_name("r15c10")
        r15c10.clear()
        r15c10.send_keys("r15c10")

        # fill r15c11
        r15c11 = browser.find_element_by_name("r15c11")
        r15c11.clear()
        r15c11.send_keys("r15c11")

        # fill r15c12
        r15c12 = browser.find_element_by_name("r15c12")
        r15c12.clear()
        r15c12.send_keys("r15c12")

        # fill r15c13
        r15c13 = browser.find_element_by_name("r15c13")
        r15c13.clear()
        r15c13.send_keys("r15c13")

        # fill r16c1
        r16c1 = browser.find_element_by_name("r16c1")
        r16c1.clear()
        r16c1.send_keys("r16c1")

        # fill r16c2
        r16c2 = browser.find_element_by_name("r16c2")
        r16c2.clear()
        r16c2.send_keys("r16c2")

        # fill r16c3
        r16c3 = browser.find_element_by_name("r16c3")
        r16c3.clear()
        r16c3.send_keys("r16c3")

        # fill r16c4
        r16c4 = browser.find_element_by_name("r16c4")
        r16c4.clear()
        r16c4.send_keys("r16c4")

        # fill r16c5
        r16c5 = browser.find_element_by_name("r16c5")
        r16c5.clear()
        r16c5.send_keys("r16c5")

        # fill r16c6
        r16c6 = browser.find_element_by_name("r16c6")
        r16c6.clear()
        r16c6.send_keys("r16c6")

        # fill r16c7
        r16c7 = browser.find_element_by_name("r16c7")
        r16c7.clear()
        r16c7.send_keys("r16c7")

        # fill r16c8
        r16c8 = browser.find_element_by_name("r16c8")
        r16c8.clear()
        r16c8.send_keys("r16c8")

        # fill r16c9
        r16c9 = browser.find_element_by_name("r16c9")
        r16c9.clear()
        r16c9.send_keys("r16c9")

        # fill r16c10
        r16c10 = browser.find_element_by_name("r16c10")
        r16c10.clear()
        r16c10.send_keys("r16c10")

        # fill r16c11
        r16c11 = browser.find_element_by_name("r16c11")
        r16c11.clear()
        r16c11.send_keys("r16c11")

        # fill r16c12
        r16c12 = browser.find_element_by_name("r16c12")
        r16c12.clear()
        r16c12.send_keys("r16c12")

        # fill r16c13
        r16c13 = browser.find_element_by_name("r16c13")
        r16c13.clear()
        r16c13.send_keys("r16c13")

        # submit
        submit = browser.find_element_by_name("button_generate_html_to_pdf_twelve_month_operating_budget")
        submit.click()

        time.sleep(5)

        browser.quit()


class UnitTestsWebAutomationHolomorpheWebsiteWithTorithoutHeadless(unittest.TestCase):
    def test_display_one_page_without_headless_with_dark_web_v1(self):
        print('test_display_one_page_without_headless_with_dark_web_v1')

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
            executable_path='..\\geckodriver.exe',
            options=firefox_options
        )

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get('https://holomorphe.com/reporting/petty_cash_journal')
        print("page opened")

        time.sleep(60)

        browser.close()
        print("browser closed")

        browser.service.process.kill()
        browser.service.process.terminate()
        print("browser service process killed")

    def test_display_one_page_without_headless_with_dark_web_v2(self):
        print('test_display_one_page_without_headless_with_dark_web_v2')

        time.sleep(5)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(5)

        binary = FirefoxBinary(r"C:\Users\DELL\Desktop\Tor Browser\Browser\firefox.exe")
        profile = FirefoxProfile(r"C:\Users\DELL\Desktop\Tor Browser\Browser\TorBrowser\Data\Browser\profile.default")
        profile.set_preference('network.proxy.type', 5)
        profile.set_preference('network.proxy.socks', '127.0.0.1')
        profile.set_preference('network.proxy.socks_port', 9150)
        profile.set_preference("network.proxy.socks_remote_dns", False)
        profile.update_preferences()

        driver = webdriver.Firefox(
            firefox_profile=profile,
            firefox_binary=binary,
            executable_path='..\\geckodriver.exe'
        )

        driver.get("http://check.torproject.org")


if __name__ == '__main__':
    unittest.main()
