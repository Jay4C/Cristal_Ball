import os
import unittest
import time
import warnings
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from Screenshot import Screenshot_Clipping
from selenium.webdriver.firefox.options import Options
import pymysql


class UnitTestsWebAutomationDataradePushAnonymousIPData(unittest.TestCase):
    # ok
    def test_count_characters_for_anonymous_ip_data(self):
        print('test_count_characters_for_anonymous_ip_data')

        """
What makes a good product title?

Give your Data Product a title that is keyword search-optimized.

Great Data Product titles have 50 to 150 characters and ideally contain the following details:
- Your Brand Name
- Data Type
- Countries / Geographies
- Volume (e.g. 10M Devices, 5M companies, 20M consumers)
- Key Benefits (e.g.GDPR-compliant, real-time sourced, 10 years historic coverage)

Examples of search optimized Data Product titles:
- Datatrade’s USA C-level executives b2b contact data (e-mail, phone) w/ 300k records
- Datatrade’s Location Data for People Visits to large cities in the UK, 18 months API
- Datatrade’s ESG ratings of Middle East companies with 5 years of history - tickerized
        """
        title = "Holomorphe / Anonymous IP Data / Worldwide / 10M anonymous ips / Tor Network"

        """
How does a good short description look?

This description will be shown on your Data Product card that appears on each filter page. 

Providing a short description of min. 100 characters helps spark further data buyer interest so that they want 
to learn more about it and view it in detail. 

We recommend including these points in your short description:
- Key benefits of your Data Product
- The main attributes of your data
- Coverage (industries, countries)
- Scale & quality indicators
        """
        short_description = "The key benefits of this data product are : unique, no personal data and high volume of " \
                            "records." \
                            "The main attributes of this data product are : anonymous ip address, ip geolocation, " \
                            "country, node type." \
                            "The coverage of this data product is worldwide."

        """
What does a good description look like?

The in-depth product description is your chance to engage with data buyers who want to fully understand a Data 
Product before requesting it. 

By adding search-optimized keywords in the text you can increase the visibility of your Data Products as well.

Try to answer the following questions in your in-depth description:
- What makes your data unique?
- How is the data generally sourced?
- What are the primary use-cases or verticals of this Data Product?
- How does this Data Product fit into your broader data offering ?

Great in-depth descriptions comprise several hundred words. 

Most top performing products on Datarade have a description length between 3000 and 6000 characters.
        """
        in_depth_description = "This data product is unique because the work for this data collection was " \
                               "made by a complex algorithm that uses Tor network. The data was generally sourced " \
                               "from Tor network. The primary use-cases or verticals of this data product are : " \
                               "web traffic analysis, risk management, fraud detection management, cybersecurity threats " \
                               "management, anonymous online action, dark web discovery, dark web services, " \
                               "dark web marketing, dark web e-commerce and online privacy protection."

        if 30 <= len(title) <= 150:
            print('title length is good')
        else:
            print('title length is bad')

        if 80 <= len(short_description) <= 300:
            print('short_description length is good')
        else:
            print('short_description length is bad')

        if 300 <= len(in_depth_description) <= 8000:
            print('in_depth_description length is good')
        else:
            print('in_depth_description length is bad')

    def test_push_one_product_for_anonymous_ip_data(self):
        print("test_push_one_product_for_anonymous_ip_data")

        time.sleep(5)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(5)

        # with Firefox
        browser = webdriver.Firefox(executable_path='..\\geckodriver.exe')

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get('https://datarade.ai/')

        time.sleep(5)

        clear_button = browser.find_element_by_xpath("//button[@data-cf-action='reject'][@aria-label='Deny']")
        clear_button.click()

        time.sleep(5)

        sign_in_button = browser.find_element_by_xpath("//a[@class='navbar__item'][@href='/users/sign_in']")
        sign_in_button.click()

        time.sleep(10)

        work_email_input = browser.find_element_by_xpath("//input[@id='user__email'][@name='user[email]']")
        work_email_input.clear()
        work_email_input.send_keys(""
                                   "")

        time.sleep(5)

        passwrod_input = browser.find_element_by_xpath("//input[@id='user__password'][@name='user[password]']")
        passwrod_input.clear()
        passwrod_input.send_keys("")

        time.sleep(5)

        login_button = browser.find_element_by_xpath("//input[@type='submit'][@name='commit']")
        login_button.click()

        time.sleep(15)

        holomorphe_button = browser.find_element_by_xpath(
            "//a[@class='navbar__item tablet-landscape-hidden'][@href='/my/provider']")
        holomorphe_button.click()

        time.sleep(5)

        new_product_button = browser.find_element_by_xpath(
            "//a[@class='button primary modern small'][@href='/my/provider/data_products/new']")
        new_product_button.click()

        time.sleep(5)

        # 1.Basics
        # Title
        title_input = browser.find_element_by_xpath("//input[@id='data_product__name'][@name='data_product[name]']")
        title_input.clear()
        title = "Holomorphe / Anonymous IP Data / Worldwide / 10M anonymous ips / Tor Network"
        title_input.send_keys(title)

        time.sleep(5)

        # Short Description
        short_description_input = browser.find_element_by_xpath(
            "//textarea[@id='data_product__short_description'][@name='data_product[short_description]']")
        short_description_input.clear()
        short_description = "The key benefits of this data product are : unique, no personal data and high " \
                            "volume of records. The main attributes of this data product are : anonymous ip address, " \
                            "ip geolocation, country, node type. The coverage of this data product is worldwide."
        short_description_input.send_keys(short_description)

        time.sleep(5)

        # In-depth Description
        in_depth_description_input = browser.find_element_by_xpath(
            "//textarea[@id='data_product__description'][@name='data_product[description]']")
        in_depth_description_input.clear()
        in_depth_description = "This data product is unique because the work for this data collection was " \
                               "made by a complex algorithm that uses Tor network. The data was generally sourced " \
                               "from Tor network. The primary use-cases or verticals of this data product are : " \
                               "web traffic analysis, risk management, fraud detection management, cybersecurity threats " \
                               "management, anonymous online action, dark web discovery, dark web services, " \
                               "dark web marketing, dark web e-commerce and online privacy protection."
        in_depth_description_input.send_keys(in_depth_description)

        time.sleep(5)

        # 2.Listing
        listing_button = browser.find_element_by_xpath("//a[@data-tab='listing']")
        listing_button.click()

        time.sleep(5)

        # Data category 1 (Anonymous IP Data)
        # data_category_1_input = browser.find_element_by_xpath("//li[1]/div[@id='field-data_product_category__category_id']/input[@tabindex='0']")
        # data_category_1_input.clear()
        # data_category_1_input.send_keys("Anonymous IP Data")
        # data_category_1_input.send_keys(Keys.ENTER)

        time.sleep(5)

        # check the Small Business checkbox
        small_business_checkbox = browser.find_element_by_xpath(
            "//label[@for='data_product__company_size_ids-1']"
        )
        small_business_checkbox.click()

        time.sleep(5)

        # check the Medium-sized Business checkbox
        medium_sized_business_checkbox = browser.find_element_by_xpath(
            "//label[@for='data_product__company_size_ids-2']"
        )
        medium_sized_business_checkbox.click()

        time.sleep(5)

        # check the Entreprise checkbox
        entreprise_checkbox = browser.find_element_by_xpath(
            "//label[@for='data_product__company_size_ids-3']"
        )
        entreprise_checkbox.click()

        time.sleep(5)

        # Use Cases
        # use_cases_input = browser.find_element_by_xpath("//div[@class='ui fluid search dropdown selection multiple']")
        # use_cases_input.clear()
        # use_cases_input.send_keys("Web Traffic Analysis")
        # use_cases_input.send_keys(Keys.ENTER)

        time.sleep(5)

        # 3. Coverage by myself

        # 4. Volume and quality
        volume_and_quality_button = browser.find_element_by_xpath("//a[@data-tab='volume_and_quality']")
        volume_and_quality_button.click()

        time.sleep(5)

        # Add Volume
        add_volume_button = browser.find_element_by_xpath("//a[@data-association='volume']")
        add_volume_button.click()

        time.sleep(5)

        # Volume input
        volume_input = browser.find_element_by_xpath("//input[@id='data_product_volume__value'][@type='number']")
        volume_input.clear()
        volume_input.send_keys("10000000")

        time.sleep(5)

        # unit_input
        unit_input = browser.find_element_by_xpath("//input[@id='data_product_volume__unit'][@type='text']")
        unit_input.clear()
        unit_input.send_keys("records")

        time.sleep(5)

        # Add Quality Attribute
        add_quality_attribute_button = browser.find_element_by_xpath("//a[@data-association='quality']")
        add_quality_attribute_button.click()

        time.sleep(5)

        # quality in % input
        quality_input = browser.find_element_by_xpath("//input[@id='data_product_quality__percentage'][@type='number']")
        quality_input.clear()
        quality_input.send_keys("100")

        time.sleep(5)

        # unit quality input
        unit_quality_input = browser.find_element_by_xpath("//input[@id='data_product_quality__unit'][@type='text']")
        unit_quality_input.clear()
        unit_quality_input.send_keys("match rate")

        time.sleep(5)

        # 5. Attributes
        attributes_button = browser.find_element_by_xpath("//a[@data-tab='attributes']")
        attributes_button.click()

        time.sleep(5)

        # Add Attribute
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(5)

        # name input
        name_input = browser.find_element_by_xpath(
            "//input[@id='data_product_attribute_spec__name']"
        )
        name_input.clear()
        name_input.send_keys("anonymous_ip_address")

        time.sleep(5)

        # example input
        example_input = browser.find_element_by_xpath(
            "//input[@id='data_product_attribute_spec__example']"
        )
        example_input.clear()
        example_input.send_keys("0.0.0.0")

        time.sleep(5)

        # description input
        description_input = browser.find_element_by_xpath(
            "//input[@id='data_product_attribute_spec__description']"
        )
        description_input.clear()
        description_input.send_keys("An anonymous ip address")

        time.sleep(5)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "//input[@id='data_product_attribute_spec__number_of_records']"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("10000000")

        time.sleep(5)

        # 6. Delivery
        delivery_button = browser.find_element_by_xpath("//a[@class='item'][@data-tab='delivery']")
        delivery_button.click()

        time.sleep(5)

        # Email checkbox
        email_checkbox = browser.find_element_by_xpath("//label[@for='data_product__transfer_method_ids-9']")
        email_checkbox.click()

        time.sleep(5)

        # Json checkbox
        json_checkbox = browser.find_element_by_xpath("//label[@for='data_product__data_format_ids-10']")
        json_checkbox.click()

        time.sleep(5)

        #  xml checkbox
        xml_checkbox = browser.find_element_by_xpath("//label[@for='data_product__data_format_ids-11']")
        xml_checkbox.click()

        time.sleep(5)

        #  csv checkbox
        csv_checkbox = browser.find_element_by_xpath("//label[@for='data_product__data_format_ids-12']")
        csv_checkbox.click()

        time.sleep(5)

        # xls checkbox
        xls_checkbox = browser.find_element_by_xpath("//label[@for='data_product__data_format_ids-13']")
        xls_checkbox.click()

        time.sleep(5)

        # sql checkbox
        sql_checkbox = browser.find_element_by_xpath("//label[@for='data_product__data_format_ids-14']")
        sql_checkbox.click()

        time.sleep(5)

        # on-demand checkbox
        on_demand_checkbox = browser.find_element_by_xpath("//label[@for='data_product__transfer_frequency_ids-10']")
        on_demand_checkbox.click()

        time.sleep(5)

        # 7. Pricing
        pricing_button = browser.find_element_by_xpath("//a[@data-tab='pricing']")
        pricing_button.click()

        time.sleep(5)

        # currency input
        # currency_input = browser.find_element_by_xpath("//div[@class='default text']")
        # currency_input.clear()
        # currency_input.send_keys("EUR")
        # currency_input.send_keys(Keys.ENTER)

        time.sleep(5)

        # One-off purchase checkbox
        one_off_purchase_checkbox = browser.find_element_by_xpath(
            "//label[@for='data_product_pricing_plan__pricing_model_id-1']"
        )
        one_off_purchase_checkbox.click()

        time.sleep(5)

        # starts at one-off purchase input
        starts_at_one_off_purchase_input = browser.find_element_by_xpath(
            "//input[@id='data_product_pricing_plan__starts_at_price']"
        )
        starts_at_one_off_purchase_input.clear()
        starts_at_one_off_purchase_input.send_keys("1000")

        time.sleep(5)


class UnitTestsWebAutomationDataradePushB2BContactData(unittest.TestCase):
    # ok
    def test_count_characters_for_b2b_contact_data(self):
        print('test_count_characters_for_b2b_contact_data')

        """
What makes a good product title?

Give your Data Product a title that is keyword search-optimized.

Great Data Product titles have 50 to 150 characters and ideally contain the following details:
- Your Brand Name
- Data Type
- Countries / Geographies
- Volume (e.g. 10M Devices, 5M companies, 20M consumers)
- Key Benefits (e.g.GDPR-compliant, real-time sourced, 10 years historic coverage)

Examples of search optimized Data Product titles:
- Datatrade’s USA C-level executives b2b contact data (e-mail, phone) w/ 300k records
- Datatrade’s Location Data for People Visits to large cities in the UK, 18 months API
- Datatrade’s ESG ratings of Middle East companies with 5 years of history - tickerized
        """
        pays = "Colombia"

        title = "Holomorphe / B2B Contact Data / Private Company data / " + pays

        """
How does a good short description look?

This description will be shown on your Data Product card that appears on each filter page. 

Providing a short description of min. 100 characters helps spark further data buyer interest so that they want 
to learn more about it and view it in detail. 

We recommend including these points in your short description:
- Key benefits of your Data Product
- The main attributes of your data
- Coverage (industries, countries)
- Scale & quality indicators
        """
        short_description = "The key benefits of this data product are : valuable, affordable and reliable." \
                            "The main attributes of this data product are : company name, postal address, " \
                            "phone number, website, email, region, activity and country." \
                            "The coverage of this data product is : " + pays + "."

        """
What does a good description look like?

The in-depth product description is your chance to engage with data buyers who want to fully understand a Data 
Product before requesting it. 

By adding search-optimized keywords in the text you can increase the visibility of your Data Products as well.

Try to answer the following questions in your in-depth description:
- What makes your data unique?
- How is the data generally sourced?
- What are the primary use-cases or verticals of this Data Product?
- How does this Data Product fit into your broader data offering ?

Great in-depth descriptions comprise several hundred words. 

Most top performing products on Datarade have a description length between 3000 and 6000 characters.
        """
        in_depth_description = "This data product is efficient because the work for this data collection was " \
                               "made by a complex algorithm that uses artificial intelligence to operate. " \
                               "The data was generally sourced from the web. The primary use-cases or verticals of " \
                               "this data product are : direct marketing, digital marketing, email marketing, " \
                               "phone marketing, voice over ip marketing, business strategy, business intelligence, " \
                               "customer segmentation, customer location and activity segmentation. The activities " \
                               "of B2B contact data are : employment agencies, real estate agencies, recruitment " \
                               "agencies, software, hotel, social, cleaning, charity, financial, restaurant, " \
                               "building, hairdresser, florist, locksmith, bakery, insurance, pharmacy, mover, " \
                               "electricity, plumbing, security, attorney, bank, garage, dentist, doctor, " \
                               "accountant, grocery, notary, jewellery, tailor, butcher, library, architect, cement, " \
                               "heating, boat, cold, steel, chemical, gas and gold."

        if 30 <= len(title) <= 150:
            print('title length is good')
        else:
            print('title length is bad')

        if 80 <= len(short_description) <= 300:
            print('short_description length is good')
        else:
            print('short_description length is bad')

        if 300 <= len(in_depth_description) <= 8000:
            print('in_depth_description length is good')
        else:
            print('in_depth_description length is bad')

    # ok
    def test_push_one_product_for_b2b_contact_data_for_cayman_islands(self):
        print("test_push_one_product_for_b2b_contact_data_for_cayman_islands")

        number_of_records = 1368

        indicatif_telephonique = "(+1345) xxx xxxxxx"

        price = "399.99"

        pays = "Cayman Islands"

        region = "Grand Cayman"

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(5)

        # with Firefox
        browser = webdriver.Firefox(executable_path='..\\geckodriver.exe')

        time.sleep(20)

        # maximize window
        browser.maximize_window()

        time.sleep(10)

        # open
        browser.get('https://datarade.ai/')

        time.sleep(15)

        clear_button = browser.find_element_by_xpath("//button[@data-cf-action='reject'][@aria-label='Deny']")
        clear_button.click()

        time.sleep(5)

        sign_in_button = browser.find_element_by_xpath("//a[@class='navbar__item'][@href='/users/sign_in']")
        sign_in_button.click()

        time.sleep(15)

        work_email_input = browser.find_element_by_xpath("//input[@id='user__email'][@name='user[email]']")
        work_email_input.clear()
        work_email_input.send_keys(""
        "")

        time.sleep(5)

        passwrod_input = browser.find_element_by_xpath("//input[@id='user__password'][@name='user[password]']")
        passwrod_input.clear()
        passwrod_input.send_keys("")

        time.sleep(5)

        login_button = browser.find_element_by_xpath("//input[@type='submit'][@name='commit']")
        login_button.click()

        time.sleep(15)

        holomorphe_button = browser.find_element_by_xpath(
            "//a[@class='navbar__item tablet-landscape-hidden'][@href='/my/provider']")
        holomorphe_button.click()

        time.sleep(10)

        new_product_button = browser.find_element_by_xpath(
            "//a[@class='button primary modern small'][@href='/my/provider/data_products/new']")
        new_product_button.click()

        time.sleep(10)

        # 1.Basics
        # Title
        title_input = browser.find_element_by_xpath("//input[@id='data_product__name'][@name='data_product[name]']")
        title_input.clear()

        title = "Holomorphe / B2B Contact Data / Private Company data / " + pays + " / Thousands of companies"

        title_input.send_keys(title)

        time.sleep(5)

        # Short Description
        short_description_input = browser.find_element_by_xpath(
            "//textarea[@id='data_product__short_description'][@name='data_product[short_description]']")
        short_description_input.clear()

        short_description = "The key benefits of this data product are : unique, no personal data and high volume of " \
                            "records. " \
                            "The main attributes of this data product are : company name, postal address, " \
                            "phone number, website, email, region, activity and country. " \
                            "The coverage of this data product is : " + pays + "."

        short_description_input.send_keys(short_description)

        time.sleep(5)

        # In-depth Description
        in_depth_description_input = browser.find_element_by_xpath(
            "//textarea[@id='data_product__description'][@name='data_product[description]']")
        in_depth_description_input.clear()

        in_depth_description = "This data product is unique because the work for this data collection was " \
                               "made by a complex algorithm that uses artificial intelligence to operate. " \
                               "The data was generally sourced " \
                               "from the web. The primary use-cases or verticals of this data product are : " \
                               "direct marketing, digital marketing, email marketing, phone marketing, " \
                               "voice over ip marketing, business strategy, business intelligence, " \
                               "customer segmentation, customer location and activity segmentation."

        in_depth_description_input.send_keys(in_depth_description)

        time.sleep(5)

        # 2.Listing
        listing_button = browser.find_element_by_xpath("//a[@data-tab='listing']")
        listing_button.click()

        time.sleep(5)

        """
        # Data category 1
        data_category_1_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[1]/div/div/input"
        )
        data_category_1_input.clear()
        data_category_1_input.send_keys("B2B Contact Data")
        data_category_1_input.send_keys(Keys.DOWN)
        data_category_1_input.send_keys(Keys.UP)
        data_category_1_input.send_keys(Keys.ENTER)

        time.sleep(5)
        """

        # check the Small Business checkbox
        small_business_checkbox = browser.find_element_by_xpath(
            "//label[@for='data_product__company_size_ids-1']"
        )
        small_business_checkbox.click()

        time.sleep(5)

        # check the Medium-sized Business checkbox
        medium_sized_business_checkbox = browser.find_element_by_xpath(
            "//label[@for='data_product__company_size_ids-2']"
        )
        medium_sized_business_checkbox.click()

        time.sleep(5)

        # check the Entreprise checkbox
        entreprise_checkbox = browser.find_element_by_xpath(
            "//label[@for='data_product__company_size_ids-3']"
        )
        entreprise_checkbox.click()

        time.sleep(5)

        """
        # Use Cases
        use_cases_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]/input"
        )
        use_cases_input.clear()
        use_cases_input.send_keys("Direct Marketing")
        use_cases_input.send_keys(Keys.DOWN)
        use_cases_input.send_keys(Keys.ENTER)

        time.sleep(5)
        """

        # 3. Coverage by myself
        coverage_button = browser.find_element_by_xpath("//a[@data-tab='coverage']")
        coverage_button.click()

        time.sleep(5)

        # Historical Coverage
        historical_coverage_input = browser.find_element_by_xpath(
            '//input[@id="data_product__history"]'
        )
        historical_coverage_input.clear()
        historical_coverage_input.send_keys("1")

        time.sleep(5)

        """
        days_button = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[5]/div/div[2]/div[3]/div[2]/div/div[2]/div[1]"
        )
        days_button.click()

        time.sleep(5)
        """

        # 4. Volume and quality
        volume_and_quality_button = browser.find_element_by_xpath("//a[@data-tab='volume_and_quality']")
        volume_and_quality_button.click()

        time.sleep(5)

        # Add Volume
        add_volume_button = browser.find_element_by_xpath("//a[@data-association='volume']")
        add_volume_button.click()

        time.sleep(5)

        # Volume input
        volume_input = browser.find_element_by_xpath("//input[@id='data_product_volume__value'][@type='number']")
        volume_input.clear()
        volume_input.send_keys(str(number_of_records))

        time.sleep(5)

        # unit_input
        unit_input = browser.find_element_by_xpath("//input[@id='data_product_volume__unit'][@type='text']")
        unit_input.clear()
        unit_input.send_keys("records")

        time.sleep(5)

        # Add Quality Attribute
        add_quality_attribute_button = browser.find_element_by_xpath("//a[@data-association='quality']")
        add_quality_attribute_button.click()

        time.sleep(5)

        # quality in % input
        quality_input = browser.find_element_by_xpath("//input[@id='data_product_quality__percentage'][@type='number']")
        quality_input.clear()
        quality_input.send_keys("90")

        time.sleep(5)

        # unit quality input
        unit_quality_input = browser.find_element_by_xpath("//input[@id='data_product_quality__unit'][@type='text']")
        unit_quality_input.clear()
        unit_quality_input.send_keys("match rate")

        time.sleep(5)

        # 5. Attributes
        attributes_button = browser.find_element_by_xpath("//a[@data-tab='attributes']")
        attributes_button.click()

        time.sleep(5)

        # Add Attribute _ company_name
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(5)

        # name input
        name_input = browser.find_element_by_xpath(
            "//input[@id='data_product_attribute_spec__name']"
        )
        name_input.clear()
        name_input.send_keys("company_name")

        time.sleep(5)

        # example input
        example_input = browser.find_element_by_xpath(
            "//input[@id='data_product_attribute_spec__example']"
        )
        example_input.clear()
        example_input.send_keys("Company A")

        time.sleep(5)

        # description input
        description_input = browser.find_element_by_xpath(
            "//input[@id='data_product_attribute_spec__description']"
        )
        description_input.clear()
        description_input.send_keys("A company name")

        time.sleep(5)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "//input[@id='data_product_attribute_spec__number_of_records']"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys(str(number_of_records))

        time.sleep(5)

        # Add Attribute _ postal_address
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # postal_address input
        postal_address_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[2]/td[2]/div/input"
        )
        postal_address_input.clear()
        postal_address_input.send_keys("postal_address")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[2]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys("1 Street postal address XXX Country")

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[2]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("A postal address")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[2]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys(str(number_of_records))

        time.sleep(10)

        # Add Attribute _ phone_number
        add_attribute_button = browser.find_element_by_xpath(
            "//a[@data-association='attribute_spec']"
        )
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[3]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("phone_number")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[3]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys(str(indicatif_telephonique))

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[3]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("A phone number of the company")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[3]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys(str(number_of_records))

        time.sleep(10)

        # Add Attribute _ website
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[4]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("website")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[4]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys("https://example.co")

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[4]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("A website of the company")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[4]/td[4]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys(str(number_of_records))

        time.sleep(10)

        # Add Attribute _ email
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[5]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("email")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[5]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys("example@example.co")

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[5]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("An email address of the company")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[5]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys(str(number_of_records))

        time.sleep(10)

        # Add Attribute _ region
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[6]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("region")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[6]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys(str(region))

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[6]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("A region name")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[6]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys(str(number_of_records))

        time.sleep(10)

        # Add Attribute _ activity
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[7]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("activity")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[7]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys("Bank")

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[7]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("An activity")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[7]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys(str(number_of_records))

        time.sleep(10)

        # Add Attribute _ country
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[8]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("country")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[8]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys(str(pays))

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[8]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("A country")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[8]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys(str(number_of_records))

        time.sleep(10)

        # 6. Delivery
        delivery_button = browser.find_element_by_xpath("//a[@class='item'][@data-tab='delivery']")
        delivery_button.click()

        time.sleep(5)

        # Email checkbox
        email_checkbox = browser.find_element_by_xpath("//label[@for='data_product__transfer_method_ids-9']")
        email_checkbox.click()

        time.sleep(5)

        # Json checkbox
        json_checkbox = browser.find_element_by_xpath("//label[@for='data_product__data_format_ids-10']")
        json_checkbox.click()

        time.sleep(5)

        #  csv checkbox
        csv_checkbox = browser.find_element_by_xpath("//label[@for='data_product__data_format_ids-12']")
        csv_checkbox.click()

        time.sleep(5)

        # xls checkbox
        xls_checkbox = browser.find_element_by_xpath("//label[@for='data_product__data_format_ids-13']")
        xls_checkbox.click()

        time.sleep(5)

        # sql checkbox
        sql_checkbox = browser.find_element_by_xpath("//label[@for='data_product__data_format_ids-14']")
        sql_checkbox.click()

        time.sleep(5)

        # on-demand checkbox
        on_demand_checkbox = browser.find_element_by_xpath("//label[@for='data_product__transfer_frequency_ids-10']")
        on_demand_checkbox.click()

        time.sleep(5)

        # 7. Pricing
        pricing_button = browser.find_element_by_xpath("//a[@data-tab='pricing']")
        pricing_button.click()

        time.sleep(5)

        """
        # currency input
        currency_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[9]/div/div[2]/div[2]/div/input"
        )
        currency_input.clear()
        currency_input.send_keys("EUR")
        currency_input.send_keys(Keys.ENTER)

        time.sleep(5)
        """

        # One-off purchase checkbox
        one_off_purchase_checkbox = browser.find_element_by_xpath(
            "//label[@for='data_product_pricing_plan__pricing_model_id-1']"
        )
        one_off_purchase_checkbox.click()

        time.sleep(5)

        # starts at one-off purchase input
        starts_at_one_off_purchase_input = browser.find_element_by_xpath(
            "//input[@id='data_product_pricing_plan__starts_at_price']"
        )
        starts_at_one_off_purchase_input.clear()
        starts_at_one_off_purchase_input.send_keys(str(price))

        time.sleep(5)

    # ok
    def test_push_one_product_for_b2b_contact_data_for_british_virgin_islands(self):
        print("test_push_one_product_for_b2b_contact_data_for_british_virgin_islands")

        number_of_records = 478

        indicatif_telephonique = "(+1284) xxx xxxxxx"

        price = "9.99"

        pays = "British Virgin Islands"

        region = "British Virgin Islands"

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(5)

        # with Firefox
        browser = webdriver.Firefox(executable_path='..\\geckodriver.exe')

        time.sleep(20)

        # maximize window
        browser.maximize_window()

        time.sleep(10)

        # open
        browser.get('https://datarade.ai/')

        time.sleep(15)

        clear_button = browser.find_element_by_xpath("//button[@data-cf-action='reject'][@aria-label='Deny']")
        clear_button.click()

        time.sleep(5)

        sign_in_button = browser.find_element_by_xpath("//a[@class='navbar__item'][@href='/users/sign_in']")
        sign_in_button.click()

        time.sleep(15)

        work_email_input = browser.find_element_by_xpath("//input[@id='user__email'][@name='user[email]']")
        work_email_input.clear()
        work_email_input.send_keys(""
        "")

        time.sleep(5)

        passwrod_input = browser.find_element_by_xpath("//input[@id='user__password'][@name='user[password]']")
        passwrod_input.clear()
        passwrod_input.send_keys("")

        time.sleep(5)

        login_button = browser.find_element_by_xpath("//input[@type='submit'][@name='commit']")
        login_button.click()

        time.sleep(15)

        holomorphe_button = browser.find_element_by_xpath(
            "//a[@class='navbar__item tablet-landscape-hidden'][@href='/my/provider']")
        holomorphe_button.click()

        time.sleep(10)

        new_product_button = browser.find_element_by_xpath(
            "//a[@class='button primary modern small'][@href='/my/provider/data_products/new']")
        new_product_button.click()

        time.sleep(10)

        # 1.Basics
        # Title
        title_input = browser.find_element_by_xpath("//input[@id='data_product__name'][@name='data_product[name]']")
        title_input.clear()

        title = "Holomorphe / B2B Contact Data / Private Company data / " + pays

        title_input.send_keys(title)

        time.sleep(5)

        # Short Description
        short_description_input = browser.find_element_by_xpath(
            "//textarea[@id='data_product__short_description'][@name='data_product[short_description]']")
        short_description_input.clear()

        short_description = "The key benefits of this data product are : valuable, affordable and reliable. " \
                            "The main attributes of this data product are : company name, postal address, " \
                            "phone number, website, email, region, activity and country. " \
                            "The coverage of this data product is : " + pays + "."

        short_description_input.send_keys(short_description)

        time.sleep(5)

        # In-depth Description
        in_depth_description_input = browser.find_element_by_xpath(
            "//textarea[@id='data_product__description'][@name='data_product[description]']")
        in_depth_description_input.clear()

        in_depth_description = "This data product is unique because the work for this data collection was " \
                               "made by a complex algorithm that uses artificial intelligence to operate. " \
                               "The data was generally sourced " \
                               "from the web. The primary use-cases or verticals of this data product are : " \
                               "direct marketing, digital marketing, email marketing, phone marketing, " \
                               "voice over ip marketing, business strategy, business intelligence, " \
                               "customer segmentation, customer location and activity segmentation."

        in_depth_description_input.send_keys(in_depth_description)

        time.sleep(5)

        # 2.Listing
        listing_button = browser.find_element_by_xpath("//a[@data-tab='listing']")
        listing_button.click()

        time.sleep(5)

        # check the Small Business checkbox
        small_business_checkbox = browser.find_element_by_xpath(
            "//label[@for='data_product__company_size_ids-1']"
        )
        small_business_checkbox.click()

        time.sleep(5)

        # check the Medium-sized Business checkbox
        medium_sized_business_checkbox = browser.find_element_by_xpath(
            "//label[@for='data_product__company_size_ids-2']"
        )
        medium_sized_business_checkbox.click()

        time.sleep(5)

        # check the Entreprise checkbox
        entreprise_checkbox = browser.find_element_by_xpath(
            "//label[@for='data_product__company_size_ids-3']"
        )
        entreprise_checkbox.click()

        time.sleep(5)

        # 3. Coverage by myself
        coverage_button = browser.find_element_by_xpath("//a[@data-tab='coverage']")
        coverage_button.click()

        time.sleep(5)

        # Historical Coverage
        historical_coverage_input = browser.find_element_by_xpath(
            '//input[@id="data_product__history"]'
        )
        historical_coverage_input.clear()
        historical_coverage_input.send_keys("1")

        time.sleep(5)

        # 4. Volume and quality
        volume_and_quality_button = browser.find_element_by_xpath("//a[@data-tab='volume_and_quality']")
        volume_and_quality_button.click()

        time.sleep(5)

        # Add Volume
        add_volume_button = browser.find_element_by_xpath("//a[@data-association='volume']")
        add_volume_button.click()

        time.sleep(5)

        # Volume input
        volume_input = browser.find_element_by_xpath("//input[@id='data_product_volume__value'][@type='number']")
        volume_input.clear()
        volume_input.send_keys(str(number_of_records))

        time.sleep(5)

        # unit_input
        unit_input = browser.find_element_by_xpath("//input[@id='data_product_volume__unit'][@type='text']")
        unit_input.clear()
        unit_input.send_keys("records")

        time.sleep(5)

        # Add Quality Attribute
        add_quality_attribute_button = browser.find_element_by_xpath("//a[@data-association='quality']")
        add_quality_attribute_button.click()

        time.sleep(5)

        # quality in % input
        quality_input = browser.find_element_by_xpath("//input[@id='data_product_quality__percentage'][@type='number']")
        quality_input.clear()
        quality_input.send_keys("80")

        time.sleep(5)

        # unit quality input
        unit_quality_input = browser.find_element_by_xpath("//input[@id='data_product_quality__unit'][@type='text']")
        unit_quality_input.clear()
        unit_quality_input.send_keys("match rate")

        time.sleep(5)

        # 5. Attributes
        attributes_button = browser.find_element_by_xpath("//a[@data-tab='attributes']")
        attributes_button.click()

        time.sleep(5)

        # Add Attribute _ company_name
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(5)

        # name input
        name_input = browser.find_element_by_xpath(
            "//input[@id='data_product_attribute_spec__name']"
        )
        name_input.clear()
        name_input.send_keys("company_name")

        time.sleep(5)

        # example input
        example_input = browser.find_element_by_xpath(
            "//input[@id='data_product_attribute_spec__example']"
        )
        example_input.clear()
        example_input.send_keys("Company A")

        time.sleep(5)

        # description input
        description_input = browser.find_element_by_xpath(
            "//input[@id='data_product_attribute_spec__description']"
        )
        description_input.clear()
        description_input.send_keys("A company name")

        time.sleep(5)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "//input[@id='data_product_attribute_spec__number_of_records']"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(5)

        # Add Attribute _ postal_address
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # postal_address input
        postal_address_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[2]/td[2]/div/input"
        )
        postal_address_input.clear()
        postal_address_input.send_keys("postal_address")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[2]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys("1 Street postal address XXX Country")

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[2]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("A postal address")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[2]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ phone_number
        add_attribute_button = browser.find_element_by_xpath(
            "//a[@data-association='attribute_spec']"
        )
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[3]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("phone_number")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[3]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys(str(indicatif_telephonique))

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[3]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("A phone number of the company")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[3]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ website
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[4]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("website")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[4]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys("https://example.co")

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[4]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("A website of the company")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[4]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ email
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[5]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("email")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[5]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys("example@example.co")

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[5]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("An email address of the company")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[5]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ region
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[6]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("region")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[6]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys(str(region))

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[6]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("A region name")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[6]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ activity
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[7]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("activity")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[7]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys("Bank")

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[7]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("An activity")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[7]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ country
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[8]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("country")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[8]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys(str(pays))

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[8]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("A country")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[8]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # 6. Delivery
        delivery_button = browser.find_element_by_xpath("//a[@class='item'][@data-tab='delivery']")
        delivery_button.click()

        time.sleep(5)

        # Email checkbox
        email_checkbox = browser.find_element_by_xpath("//label[@for='data_product__transfer_method_ids-9']")
        email_checkbox.click()

        time.sleep(5)

        # Json checkbox
        json_checkbox = browser.find_element_by_xpath("//label[@for='data_product__data_format_ids-10']")
        json_checkbox.click()

        time.sleep(5)

        #  csv checkbox
        csv_checkbox = browser.find_element_by_xpath("//label[@for='data_product__data_format_ids-12']")
        csv_checkbox.click()

        time.sleep(5)

        # xls checkbox
        xls_checkbox = browser.find_element_by_xpath("//label[@for='data_product__data_format_ids-13']")
        xls_checkbox.click()

        time.sleep(5)

        # sql checkbox
        sql_checkbox = browser.find_element_by_xpath("//label[@for='data_product__data_format_ids-14']")
        sql_checkbox.click()

        time.sleep(5)

        # on-demand checkbox
        on_demand_checkbox = browser.find_element_by_xpath("//label[@for='data_product__transfer_frequency_ids-10']")
        on_demand_checkbox.click()

        time.sleep(5)

        # 7. Pricing
        pricing_button = browser.find_element_by_xpath("//a[@data-tab='pricing']")
        pricing_button.click()

        time.sleep(5)

        # One-off purchase checkbox
        one_off_purchase_checkbox = browser.find_element_by_xpath(
            "//label[@for='data_product_pricing_plan__pricing_model_id-1']"
        )
        one_off_purchase_checkbox.click()

        time.sleep(5)

        # starts at one-off purchase input
        starts_at_one_off_purchase_input = browser.find_element_by_xpath(
            "//input[@id='data_product_pricing_plan__starts_at_price']"
        )
        starts_at_one_off_purchase_input.clear()
        starts_at_one_off_purchase_input.send_keys(str(price))

        time.sleep(5)

    # ok
    def test_push_one_product_for_b2b_contact_data_for_canada(self):
        print("test_push_one_product_for_b2b_contact_data_for_canada")

        number_of_records = 29000

        indicatif_telephonique = "(+1) xxx xxxxxx"

        price = "9.99"

        pays = "Canada"

        region = "Victoria, BC"

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(5)

        # with Firefox
        browser = webdriver.Firefox(executable_path='..\\geckodriver.exe')

        time.sleep(20)

        # maximize window
        browser.maximize_window()

        time.sleep(10)

        # open
        browser.get('https://datarade.ai/')

        time.sleep(15)

        clear_button = browser.find_element_by_xpath("//button[@data-cf-action='reject'][@aria-label='Deny']")
        clear_button.click()

        time.sleep(5)

        sign_in_button = browser.find_element_by_xpath("//a[@class='navbar__item'][@href='/users/sign_in']")
        sign_in_button.click()

        time.sleep(15)

        work_email_input = browser.find_element_by_xpath("//input[@id='user__email'][@name='user[email]']")
        work_email_input.clear()
        work_email_input.send_keys(""
        "")

        time.sleep(5)

        passwrod_input = browser.find_element_by_xpath("//input[@id='user__password'][@name='user[password]']")
        passwrod_input.clear()
        passwrod_input.send_keys("")

        time.sleep(5)

        login_button = browser.find_element_by_xpath("//input[@type='submit'][@name='commit']")
        login_button.click()

        time.sleep(15)

        holomorphe_button = browser.find_element_by_xpath(
            "//a[@class='navbar__item tablet-landscape-hidden'][@href='/my/provider']")
        holomorphe_button.click()

        time.sleep(10)

        new_product_button = browser.find_element_by_xpath(
            "//a[@class='button primary modern small'][@href='/my/provider/data_products/new']")
        new_product_button.click()

        time.sleep(10)

        # 1.Basics
        # Title
        title_input = browser.find_element_by_xpath("//input[@id='data_product__name'][@name='data_product[name]']")
        title_input.clear()

        title = "Holomorphe / B2B Contact Data / Private Company data / " + pays

        title_input.send_keys(title)

        time.sleep(5)

        # Short Description
        short_description_input = browser.find_element_by_xpath(
            "//textarea[@id='data_product__short_description'][@name='data_product[short_description]']")
        short_description_input.clear()

        short_description = "The key benefits of this data product are : valuable, affordable and reliable. " \
                            "The main attributes of this data product are : company name, postal address, " \
                            "phone number, website, email, region, activity and country." \
                            "The coverage of this data product is : " + pays + "."

        short_description_input.send_keys(short_description)

        time.sleep(5)

        # In-depth Description
        in_depth_description_input = browser.find_element_by_xpath(
            "//textarea[@id='data_product__description'][@name='data_product[description]']")
        in_depth_description_input.clear()

        in_depth_description = "This data product is unique because the work for this data collection was " \
                               "made by a complex algorithm that uses artificial intelligence to operate. " \
                               "The data was generally sourced from the web. The primary use-cases or verticals " \
                               "of this data product are : " \
                               "direct marketing, digital marketing, email marketing, phone marketing, " \
                               "voice over ip marketing, business strategy, business intelligence, " \
                               "customer segmentation, customer location and activity segmentation."

        in_depth_description_input.send_keys(in_depth_description)

        time.sleep(5)

        # 2.Listing
        listing_button = browser.find_element_by_xpath("//a[@data-tab='listing']")
        listing_button.click()

        time.sleep(5)

        # check the Small Business checkbox
        small_business_checkbox = browser.find_element_by_xpath(
            "//label[@for='data_product__company_size_ids-1']"
        )
        small_business_checkbox.click()

        time.sleep(5)

        # check the Medium-sized Business checkbox
        medium_sized_business_checkbox = browser.find_element_by_xpath(
            "//label[@for='data_product__company_size_ids-2']"
        )
        medium_sized_business_checkbox.click()

        time.sleep(5)

        # check the Entreprise checkbox
        entreprise_checkbox = browser.find_element_by_xpath(
            "//label[@for='data_product__company_size_ids-3']"
        )
        entreprise_checkbox.click()

        time.sleep(5)

        # 3. Coverage by myself
        coverage_button = browser.find_element_by_xpath("//a[@data-tab='coverage']")
        coverage_button.click()

        time.sleep(5)

        # Historical Coverage
        historical_coverage_input = browser.find_element_by_xpath(
            '//input[@id="data_product__history"]'
        )
        historical_coverage_input.clear()
        historical_coverage_input.send_keys("1")

        time.sleep(5)

        # 4. Volume and quality
        volume_and_quality_button = browser.find_element_by_xpath("//a[@data-tab='volume_and_quality']")
        volume_and_quality_button.click()

        time.sleep(5)

        # Add Volume
        add_volume_button = browser.find_element_by_xpath("//a[@data-association='volume']")
        add_volume_button.click()

        time.sleep(5)

        # Volume input
        volume_input = browser.find_element_by_xpath("//input[@id='data_product_volume__value'][@type='number']")
        volume_input.clear()
        volume_input.send_keys(str(number_of_records))

        time.sleep(5)

        # unit_input
        unit_input = browser.find_element_by_xpath("//input[@id='data_product_volume__unit'][@type='text']")
        unit_input.clear()
        unit_input.send_keys("records")

        time.sleep(5)

        # Add Quality Attribute
        add_quality_attribute_button = browser.find_element_by_xpath("//a[@data-association='quality']")
        add_quality_attribute_button.click()

        time.sleep(5)

        # quality in % input
        quality_input = browser.find_element_by_xpath("//input[@id='data_product_quality__percentage'][@type='number']")
        quality_input.clear()
        quality_input.send_keys("90")

        time.sleep(5)

        # unit quality input
        unit_quality_input = browser.find_element_by_xpath("//input[@id='data_product_quality__unit'][@type='text']")
        unit_quality_input.clear()
        unit_quality_input.send_keys("match rate")

        time.sleep(5)

        # 5. Attributes
        attributes_button = browser.find_element_by_xpath("//a[@data-tab='attributes']")
        attributes_button.click()

        time.sleep(5)

        # Add Attribute _ company_name
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(5)

        # name input
        name_input = browser.find_element_by_xpath(
            "//input[@id='data_product_attribute_spec__name']"
        )
        name_input.clear()
        name_input.send_keys("company_name")

        time.sleep(5)

        # example input
        example_input = browser.find_element_by_xpath(
            "//input[@id='data_product_attribute_spec__example']"
        )
        example_input.clear()
        example_input.send_keys("Company A")

        time.sleep(5)

        # description input
        description_input = browser.find_element_by_xpath(
            "//input[@id='data_product_attribute_spec__description']"
        )
        description_input.clear()
        description_input.send_keys("A company name")

        time.sleep(5)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "//input[@id='data_product_attribute_spec__number_of_records']"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(5)

        # Add Attribute _ postal_address
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # postal_address input
        postal_address_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[2]/td[2]/div/input"
        )
        postal_address_input.clear()
        postal_address_input.send_keys("postal_address")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[2]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys("1 Street postal address XXX Country")

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[2]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("A postal address")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[2]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ phone_number
        add_attribute_button = browser.find_element_by_xpath(
            "//a[@data-association='attribute_spec']"
        )
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[3]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("phone_number")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[3]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys(str(indicatif_telephonique))

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[3]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("A phone number of the company")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[3]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ website
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[4]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("website")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[4]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys("https://example.example")

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[4]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("A website of the company")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[4]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ email
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[5]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("email")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[5]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys("example@example.example")

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[5]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("An email address of the company")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[5]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ region
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[6]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("region")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[6]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys(str(region))

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[6]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("A region name")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[6]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ activity
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[7]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("activity")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[7]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys("Bank")

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[7]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("An activity")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[7]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ country
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[8]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("country")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[8]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys(str(pays))

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[8]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("A country")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[8]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # 6. Delivery
        delivery_button = browser.find_element_by_xpath("//a[@class='item'][@data-tab='delivery']")
        delivery_button.click()

        time.sleep(5)

        # Email checkbox
        email_checkbox = browser.find_element_by_xpath("//label[@for='data_product__transfer_method_ids-9']")
        email_checkbox.click()

        time.sleep(5)

        # Json checkbox
        json_checkbox = browser.find_element_by_xpath("//label[@for='data_product__data_format_ids-10']")
        json_checkbox.click()

        time.sleep(5)

        #  csv checkbox
        csv_checkbox = browser.find_element_by_xpath("//label[@for='data_product__data_format_ids-12']")
        csv_checkbox.click()

        time.sleep(5)

        # xls checkbox
        xls_checkbox = browser.find_element_by_xpath("//label[@for='data_product__data_format_ids-13']")
        xls_checkbox.click()

        time.sleep(5)

        # sql checkbox
        sql_checkbox = browser.find_element_by_xpath("//label[@for='data_product__data_format_ids-14']")
        sql_checkbox.click()

        time.sleep(5)

        # on-demand checkbox
        on_demand_checkbox = browser.find_element_by_xpath("//label[@for='data_product__transfer_frequency_ids-10']")
        on_demand_checkbox.click()

        time.sleep(5)

        # 7. Pricing
        pricing_button = browser.find_element_by_xpath("//a[@data-tab='pricing']")
        pricing_button.click()

        time.sleep(5)

        # One-off purchase checkbox
        one_off_purchase_checkbox = browser.find_element_by_xpath(
            "//label[@for='data_product_pricing_plan__pricing_model_id-1']"
        )
        one_off_purchase_checkbox.click()

        time.sleep(5)

        # starts at one-off purchase input
        starts_at_one_off_purchase_input = browser.find_element_by_xpath(
            "//input[@id='data_product_pricing_plan__starts_at_price']"
        )
        starts_at_one_off_purchase_input.clear()
        starts_at_one_off_purchase_input.send_keys(str(price))

        time.sleep(5)

    # ok
    def test_push_one_product_for_b2b_contact_data_for_panama(self):
        print("test_push_one_product_for_b2b_contact_data_for_panama")

        number_of_records = 6991

        indicatif_telephonique = "(+507) xxx xxxxxx"

        price = "9.99"

        pays = "Panama"

        region = "Panama"

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(5)

        # with Firefox
        browser = webdriver.Firefox(executable_path='..\\geckodriver.exe')

        time.sleep(20)

        # maximize window
        browser.maximize_window()

        time.sleep(10)

        # open
        browser.get('https://datarade.ai/')

        time.sleep(15)

        clear_button = browser.find_element_by_xpath("//button[@data-cf-action='reject'][@aria-label='Deny']")
        clear_button.click()

        time.sleep(5)

        sign_in_button = browser.find_element_by_xpath("//a[@class='navbar__item'][@href='/users/sign_in']")
        sign_in_button.click()

        time.sleep(15)

        work_email_input = browser.find_element_by_xpath("//input[@id='user__email'][@name='user[email]']")
        work_email_input.clear()
        work_email_input.send_keys(""
        "")

        time.sleep(5)

        passwrod_input = browser.find_element_by_xpath("//input[@id='user__password'][@name='user[password]']")
        passwrod_input.clear()
        passwrod_input.send_keys("")

        time.sleep(5)

        login_button = browser.find_element_by_xpath("//input[@type='submit'][@name='commit']")
        login_button.click()

        time.sleep(15)

        holomorphe_button = browser.find_element_by_xpath(
            "//a[@class='navbar__item tablet-landscape-hidden'][@href='/my/provider']")
        holomorphe_button.click()

        time.sleep(10)

        new_product_button = browser.find_element_by_xpath(
            "//a[@class='button primary modern small'][@href='/my/provider/data_products/new']")
        new_product_button.click()

        time.sleep(10)

        # 1.Basics
        # Title
        title_input = browser.find_element_by_xpath("//input[@id='data_product__name'][@name='data_product[name]']")
        title_input.clear()

        title = "Holomorphe / B2B Contact Data / Private Company data / " + pays

        title_input.send_keys(title)

        time.sleep(5)

        # Short Description
        short_description_input = browser.find_element_by_xpath(
            "//textarea[@id='data_product__short_description'][@name='data_product[short_description]']")
        short_description_input.clear()

        short_description = "The key benefits of this data product are : valuable, affordable and reliable. " \
                            "The main attributes of this data product are : company name, postal address, " \
                            "phone number, website, email, region, activity and country. " \
                            "The coverage of this data product is : " + pays + "."

        short_description_input.send_keys(short_description)

        time.sleep(5)

        # In-depth Description
        in_depth_description_input = browser.find_element_by_xpath(
            "//textarea[@id='data_product__description'][@name='data_product[description]']")
        in_depth_description_input.clear()

        in_depth_description = "This data product is unique because the work for this data collection was " \
                               "made by a complex algorithm that uses artificial intelligence to operate. " \
                               "The data was generally sourced from the web. The primary use-cases or verticals " \
                               "of this data product are : " \
                               "direct marketing, digital marketing, email marketing, phone marketing, " \
                               "voice over ip marketing, business strategy, business intelligence, " \
                               "customer segmentation, customer location and activity segmentation."

        in_depth_description_input.send_keys(in_depth_description)

        time.sleep(5)

        # 2.Listing
        listing_button = browser.find_element_by_xpath("//a[@data-tab='listing']")
        listing_button.click()

        time.sleep(5)

        # check the Small Business checkbox
        small_business_checkbox = browser.find_element_by_xpath(
            "//label[@for='data_product__company_size_ids-1']"
        )
        small_business_checkbox.click()

        time.sleep(5)

        # check the Medium-sized Business checkbox
        medium_sized_business_checkbox = browser.find_element_by_xpath(
            "//label[@for='data_product__company_size_ids-2']"
        )
        medium_sized_business_checkbox.click()

        time.sleep(5)

        # check the Entreprise checkbox
        entreprise_checkbox = browser.find_element_by_xpath(
            "//label[@for='data_product__company_size_ids-3']"
        )
        entreprise_checkbox.click()

        time.sleep(5)

        # 3. Coverage by myself
        coverage_button = browser.find_element_by_xpath("//a[@data-tab='coverage']")
        coverage_button.click()

        time.sleep(5)

        # Historical Coverage
        historical_coverage_input = browser.find_element_by_xpath(
            '//input[@id="data_product__history"]'
        )
        historical_coverage_input.clear()
        historical_coverage_input.send_keys("1")

        time.sleep(5)

        # 4. Volume and quality
        volume_and_quality_button = browser.find_element_by_xpath("//a[@data-tab='volume_and_quality']")
        volume_and_quality_button.click()

        time.sleep(5)

        # Add Volume
        add_volume_button = browser.find_element_by_xpath("//a[@data-association='volume']")
        add_volume_button.click()

        time.sleep(5)

        # Volume input
        volume_input = browser.find_element_by_xpath("//input[@id='data_product_volume__value'][@type='number']")
        volume_input.clear()
        volume_input.send_keys(str(number_of_records))

        time.sleep(5)

        # unit_input
        unit_input = browser.find_element_by_xpath("//input[@id='data_product_volume__unit'][@type='text']")
        unit_input.clear()
        unit_input.send_keys("records")

        time.sleep(5)

        # Add Quality Attribute
        add_quality_attribute_button = browser.find_element_by_xpath("//a[@data-association='quality']")
        add_quality_attribute_button.click()

        time.sleep(5)

        # quality in % input
        quality_input = browser.find_element_by_xpath("//input[@id='data_product_quality__percentage'][@type='number']")
        quality_input.clear()
        quality_input.send_keys("80")

        time.sleep(5)

        # unit quality input
        unit_quality_input = browser.find_element_by_xpath("//input[@id='data_product_quality__unit'][@type='text']")
        unit_quality_input.clear()
        unit_quality_input.send_keys("match rate")

        time.sleep(5)

        # 5. Attributes
        attributes_button = browser.find_element_by_xpath("//a[@data-tab='attributes']")
        attributes_button.click()

        time.sleep(5)

        # Add Attribute _ company_name
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(5)

        # name input
        name_input = browser.find_element_by_xpath(
            "//input[@id='data_product_attribute_spec__name']"
        )
        name_input.clear()
        name_input.send_keys("company_name")

        time.sleep(5)

        # example input
        example_input = browser.find_element_by_xpath(
            "//input[@id='data_product_attribute_spec__example']"
        )
        example_input.clear()
        example_input.send_keys("Company A")

        time.sleep(5)

        # description input
        description_input = browser.find_element_by_xpath(
            "//input[@id='data_product_attribute_spec__description']"
        )
        description_input.clear()
        description_input.send_keys("A company name")

        time.sleep(5)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "//input[@id='data_product_attribute_spec__number_of_records']"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(5)

        # Add Attribute _ postal_address
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # postal_address input
        postal_address_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[2]/td[2]/div/input"
        )
        postal_address_input.clear()
        postal_address_input.send_keys("postal_address")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[2]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys("1 Street postal address XXX Country")

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[2]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("A postal address")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[2]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ phone_number
        add_attribute_button = browser.find_element_by_xpath(
            "//a[@data-association='attribute_spec']"
        )
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[3]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("phone_number")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[3]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys(str(indicatif_telephonique))

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[3]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("A phone number of the company")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[3]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ website
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[4]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("website")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[4]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys("https://example.example")

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[4]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("A website of the company")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[4]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ email
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[5]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("email")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[5]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys("example@example.example")

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[5]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("An email address of the company")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[5]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ region
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[6]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("region")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[6]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys(str(region))

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[6]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("A region name")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[6]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ activity
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[7]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("activity")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[7]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys("Bank")

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[7]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("An activity")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[7]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ country
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[8]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("country")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[8]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys(str(pays))

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[8]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("A country")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[8]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # 6. Delivery
        delivery_button = browser.find_element_by_xpath("//a[@class='item'][@data-tab='delivery']")
        delivery_button.click()

        time.sleep(5)

        # Email checkbox
        email_checkbox = browser.find_element_by_xpath("//label[@for='data_product__transfer_method_ids-9']")
        email_checkbox.click()

        time.sleep(5)

        # Json checkbox
        json_checkbox = browser.find_element_by_xpath("//label[@for='data_product__data_format_ids-10']")
        json_checkbox.click()

        time.sleep(5)

        #  csv checkbox
        csv_checkbox = browser.find_element_by_xpath("//label[@for='data_product__data_format_ids-12']")
        csv_checkbox.click()

        time.sleep(5)

        # xls checkbox
        xls_checkbox = browser.find_element_by_xpath("//label[@for='data_product__data_format_ids-13']")
        xls_checkbox.click()

        time.sleep(5)

        # sql checkbox
        sql_checkbox = browser.find_element_by_xpath("//label[@for='data_product__data_format_ids-14']")
        sql_checkbox.click()

        time.sleep(5)

        # on-demand checkbox
        on_demand_checkbox = browser.find_element_by_xpath("//label[@for='data_product__transfer_frequency_ids-10']")
        on_demand_checkbox.click()

        time.sleep(5)

        # 7. Pricing
        pricing_button = browser.find_element_by_xpath("//a[@data-tab='pricing']")
        pricing_button.click()

        time.sleep(5)

        # One-off purchase checkbox
        one_off_purchase_checkbox = browser.find_element_by_xpath(
            "//label[@for='data_product_pricing_plan__pricing_model_id-1']"
        )
        one_off_purchase_checkbox.click()

        time.sleep(5)

        # starts at one-off purchase input
        starts_at_one_off_purchase_input = browser.find_element_by_xpath(
            "//input[@id='data_product_pricing_plan__starts_at_price']"
        )
        starts_at_one_off_purchase_input.clear()
        starts_at_one_off_purchase_input.send_keys(str(price))

        time.sleep(5)

    # ok
    def test_push_one_product_for_b2b_contact_data_for_anguilla(self):
        print("test_push_one_product_for_b2b_contact_data_for_anguilla")

        number_of_records = 224

        indicatif_telephonique = "(+1264) xxx xxxxxx"

        price = "1.99"

        pays = "Anguilla"

        region = "Anguilla"

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(5)

        # with Firefox
        browser = webdriver.Firefox(executable_path='..\\geckodriver.exe')

        time.sleep(20)

        # maximize window
        browser.maximize_window()

        time.sleep(10)

        # open
        browser.get('https://datarade.ai/')

        time.sleep(15)

        clear_button = browser.find_element_by_xpath("//button[@data-cf-action='reject'][@aria-label='Deny']")
        clear_button.click()

        time.sleep(5)

        sign_in_button = browser.find_element_by_xpath("//a[@class='navbar__item'][@href='/users/sign_in']")
        sign_in_button.click()

        time.sleep(15)

        work_email_input = browser.find_element_by_xpath("//input[@id='user__email'][@name='user[email]']")
        work_email_input.clear()
        work_email_input.send_keys(""
        "")

        time.sleep(5)

        passwrod_input = browser.find_element_by_xpath("//input[@id='user__password'][@name='user[password]']")
        passwrod_input.clear()
        passwrod_input.send_keys("")

        time.sleep(5)

        login_button = browser.find_element_by_xpath("//input[@type='submit'][@name='commit']")
        login_button.click()

        time.sleep(15)

        holomorphe_button = browser.find_element_by_xpath(
            "//a[@class='navbar__item tablet-landscape-hidden'][@href='/my/provider']")
        holomorphe_button.click()

        time.sleep(10)

        new_product_button = browser.find_element_by_xpath(
            "//a[@class='button primary modern small'][@href='/my/provider/data_products/new']")
        new_product_button.click()

        time.sleep(10)

        # 1.Basics
        # Title
        title_input = browser.find_element_by_xpath("//input[@id='data_product__name'][@name='data_product[name]']")
        title_input.clear()

        title = "Holomorphe / B2B Contact Data / Private Company data / " + pays

        title_input.send_keys(title)

        time.sleep(5)

        # Short Description
        short_description_input = browser.find_element_by_xpath(
            "//textarea[@id='data_product__short_description'][@name='data_product[short_description]']")
        short_description_input.clear()

        short_description = "The key benefits of this data product are : valuable, affordable and reliable. " \
                            "The main attributes of this data product are : company name, postal address, " \
                            "phone number, website, email, region, activity and country. " \
                            "The coverage of this data product is : " + pays + "."

        short_description_input.send_keys(short_description)

        time.sleep(5)

        # In-depth Description
        in_depth_description_input = browser.find_element_by_xpath(
            "//textarea[@id='data_product__description'][@name='data_product[description]']")
        in_depth_description_input.clear()

        in_depth_description = "This data product is unique because the work for this data collection was " \
                               "made by a complex algorithm that uses artificial intelligence to operate. " \
                               "The data was generally sourced from the web. The primary use-cases or verticals " \
                               "of this data product are : " \
                               "direct marketing, digital marketing, email marketing, phone marketing, " \
                               "voice over ip marketing, business strategy, business intelligence, " \
                               "customer segmentation, customer location and activity segmentation."

        in_depth_description_input.send_keys(in_depth_description)

        time.sleep(5)

        # 2.Listing
        listing_button = browser.find_element_by_xpath("//a[@data-tab='listing']")
        listing_button.click()

        time.sleep(5)

        # check the Small Business checkbox
        small_business_checkbox = browser.find_element_by_xpath(
            "//label[@for='data_product__company_size_ids-1']"
        )
        small_business_checkbox.click()

        time.sleep(5)

        # check the Medium-sized Business checkbox
        medium_sized_business_checkbox = browser.find_element_by_xpath(
            "//label[@for='data_product__company_size_ids-2']"
        )
        medium_sized_business_checkbox.click()

        time.sleep(5)

        # check the Entreprise checkbox
        entreprise_checkbox = browser.find_element_by_xpath(
            "//label[@for='data_product__company_size_ids-3']"
        )
        entreprise_checkbox.click()

        time.sleep(5)

        # 3. Coverage by myself
        coverage_button = browser.find_element_by_xpath("//a[@data-tab='coverage']")
        coverage_button.click()

        time.sleep(5)

        # Historical Coverage
        historical_coverage_input = browser.find_element_by_xpath(
            '//input[@id="data_product__history"]'
        )
        historical_coverage_input.clear()
        historical_coverage_input.send_keys("1")

        time.sleep(5)

        # 4. Volume and quality
        volume_and_quality_button = browser.find_element_by_xpath("//a[@data-tab='volume_and_quality']")
        volume_and_quality_button.click()

        time.sleep(5)

        # Add Volume
        add_volume_button = browser.find_element_by_xpath("//a[@data-association='volume']")
        add_volume_button.click()

        time.sleep(5)

        # Volume input
        volume_input = browser.find_element_by_xpath("//input[@id='data_product_volume__value'][@type='number']")
        volume_input.clear()
        volume_input.send_keys(str(number_of_records))

        time.sleep(5)

        # unit_input
        unit_input = browser.find_element_by_xpath("//input[@id='data_product_volume__unit'][@type='text']")
        unit_input.clear()
        unit_input.send_keys("records")

        time.sleep(5)

        # Add Quality Attribute
        add_quality_attribute_button = browser.find_element_by_xpath("//a[@data-association='quality']")
        add_quality_attribute_button.click()

        time.sleep(5)

        # quality in % input
        quality_input = browser.find_element_by_xpath("//input[@id='data_product_quality__percentage'][@type='number']")
        quality_input.clear()
        quality_input.send_keys("80")

        time.sleep(5)

        # unit quality input
        unit_quality_input = browser.find_element_by_xpath("//input[@id='data_product_quality__unit'][@type='text']")
        unit_quality_input.clear()
        unit_quality_input.send_keys("match rate")

        time.sleep(5)

        # 5. Attributes
        attributes_button = browser.find_element_by_xpath("//a[@data-tab='attributes']")
        attributes_button.click()

        time.sleep(5)

        # Add Attribute _ company_name
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(5)

        # name input
        name_input = browser.find_element_by_xpath(
            "//input[@id='data_product_attribute_spec__name']"
        )
        name_input.clear()
        name_input.send_keys("company_name")

        time.sleep(5)

        # example input
        example_input = browser.find_element_by_xpath(
            "//input[@id='data_product_attribute_spec__example']"
        )
        example_input.clear()
        example_input.send_keys("Company A")

        time.sleep(5)

        # description input
        description_input = browser.find_element_by_xpath(
            "//input[@id='data_product_attribute_spec__description']"
        )
        description_input.clear()
        description_input.send_keys("A company name")

        time.sleep(5)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "//input[@id='data_product_attribute_spec__number_of_records']"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(5)

        # Add Attribute _ postal_address
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # postal_address input
        postal_address_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[2]/td[2]/div/input"
        )
        postal_address_input.clear()
        postal_address_input.send_keys("postal_address")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[2]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys("1 Street postal address XXX Country")

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[2]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("A postal address")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[2]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ phone_number
        add_attribute_button = browser.find_element_by_xpath(
            "//a[@data-association='attribute_spec']"
        )
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[3]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("phone_number")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[3]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys(str(indicatif_telephonique))

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[3]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("A phone number of the company")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[3]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ website
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[4]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("website")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[4]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys("https://example.example")

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[4]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("A website of the company")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[4]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ email
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[5]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("email")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[5]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys("example@example.example")

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[5]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("An email address of the company")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[5]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ region
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[6]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("region")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[6]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys(str(region))

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[6]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("A region name")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[6]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ activity
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[7]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("activity")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[7]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys("Bank")

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[7]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("An activity")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[7]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ country
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[8]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("country")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[8]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys(str(pays))

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[8]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("A country")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[8]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # 6. Delivery
        delivery_button = browser.find_element_by_xpath("//a[@class='item'][@data-tab='delivery']")
        delivery_button.click()

        time.sleep(5)

        # Email checkbox
        email_checkbox = browser.find_element_by_xpath("//label[@for='data_product__transfer_method_ids-9']")
        email_checkbox.click()

        time.sleep(5)

        # Json checkbox
        json_checkbox = browser.find_element_by_xpath("//label[@for='data_product__data_format_ids-10']")
        json_checkbox.click()

        time.sleep(5)

        #  csv checkbox
        csv_checkbox = browser.find_element_by_xpath("//label[@for='data_product__data_format_ids-12']")
        csv_checkbox.click()

        time.sleep(5)

        # xls checkbox
        xls_checkbox = browser.find_element_by_xpath("//label[@for='data_product__data_format_ids-13']")
        xls_checkbox.click()

        time.sleep(5)

        # sql checkbox
        sql_checkbox = browser.find_element_by_xpath("//label[@for='data_product__data_format_ids-14']")
        sql_checkbox.click()

        time.sleep(5)

        # on-demand checkbox
        on_demand_checkbox = browser.find_element_by_xpath("//label[@for='data_product__transfer_frequency_ids-10']")
        on_demand_checkbox.click()

        time.sleep(5)

        # 7. Pricing
        pricing_button = browser.find_element_by_xpath("//a[@data-tab='pricing']")
        pricing_button.click()

        time.sleep(5)

        # One-off purchase checkbox
        one_off_purchase_checkbox = browser.find_element_by_xpath(
            "//label[@for='data_product_pricing_plan__pricing_model_id-1']"
        )
        one_off_purchase_checkbox.click()

        time.sleep(5)

        # starts at one-off purchase input
        starts_at_one_off_purchase_input = browser.find_element_by_xpath(
            "//input[@id='data_product_pricing_plan__starts_at_price']"
        )
        starts_at_one_off_purchase_input.clear()
        starts_at_one_off_purchase_input.send_keys(str(price))

        time.sleep(5)

    # ok
    def test_push_one_product_for_b2b_contact_data_for_antigua(self):
        print("test_push_one_product_for_b2b_contact_data_for_antigua")

        number_of_records = 308

        indicatif_telephonique = "(+1268) xxx xxxxxx"

        price = "1.99"

        pays = "Antigua"

        region = "Antigua"

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(5)

        # with Firefox
        browser = webdriver.Firefox(executable_path='..\\geckodriver.exe')

        time.sleep(20)

        # maximize window
        browser.maximize_window()

        time.sleep(10)

        # open
        browser.get('https://datarade.ai/')

        time.sleep(15)

        clear_button = browser.find_element_by_xpath("//button[@data-cf-action='reject'][@aria-label='Deny']")
        clear_button.click()

        time.sleep(5)

        sign_in_button = browser.find_element_by_xpath("//a[@class='navbar__item'][@href='/users/sign_in']")
        sign_in_button.click()

        time.sleep(15)

        work_email_input = browser.find_element_by_xpath("//input[@id='user__email'][@name='user[email]']")
        work_email_input.clear()
        work_email_input.send_keys(""
        "")

        time.sleep(5)

        passwrod_input = browser.find_element_by_xpath("//input[@id='user__password'][@name='user[password]']")
        passwrod_input.clear()
        passwrod_input.send_keys("")

        time.sleep(5)

        login_button = browser.find_element_by_xpath("//input[@type='submit'][@name='commit']")
        login_button.click()

        time.sleep(15)

        holomorphe_button = browser.find_element_by_xpath(
            "//a[@class='navbar__item tablet-landscape-hidden'][@href='/my/provider']")
        holomorphe_button.click()

        time.sleep(10)

        new_product_button = browser.find_element_by_xpath(
            "//a[@class='button primary modern small'][@href='/my/provider/data_products/new']")
        new_product_button.click()

        time.sleep(10)

        # 1.Basics
        # Title
        title_input = browser.find_element_by_xpath("//input[@id='data_product__name'][@name='data_product[name]']")
        title_input.clear()

        title = "Holomorphe / B2B Contact Data / Private Company data / " + pays

        title_input.send_keys(title)

        time.sleep(5)

        # Short Description
        short_description_input = browser.find_element_by_xpath(
            "//textarea[@id='data_product__short_description'][@name='data_product[short_description]']")
        short_description_input.clear()

        short_description = "The key benefits of this data product are : valuable, affordable and reliable. " \
                            "The main attributes of this data product are : company name, postal address, " \
                            "phone number, website, email, region, activity and country. " \
                            "The coverage of this data product is : " + pays + "."

        short_description_input.send_keys(short_description)

        time.sleep(5)

        # In-depth Description
        in_depth_description_input = browser.find_element_by_xpath(
            "//textarea[@id='data_product__description'][@name='data_product[description]']")
        in_depth_description_input.clear()

        in_depth_description = "This data product is unique because the work for this data collection was " \
                               "made by a complex algorithm that uses artificial intelligence to operate. " \
                               "The data was generally sourced from the web. The primary use-cases or verticals " \
                               "of this data product are : " \
                               "direct marketing, digital marketing, email marketing, phone marketing, " \
                               "voice over ip marketing, business strategy, business intelligence, " \
                               "customer segmentation, customer location and activity segmentation."

        in_depth_description_input.send_keys(in_depth_description)

        time.sleep(5)

        # 2.Listing
        listing_button = browser.find_element_by_xpath("//a[@data-tab='listing']")
        listing_button.click()

        time.sleep(5)

        # check the Small Business checkbox
        small_business_checkbox = browser.find_element_by_xpath(
            "//label[@for='data_product__company_size_ids-1']"
        )
        small_business_checkbox.click()

        time.sleep(5)

        # check the Medium-sized Business checkbox
        medium_sized_business_checkbox = browser.find_element_by_xpath(
            "//label[@for='data_product__company_size_ids-2']"
        )
        medium_sized_business_checkbox.click()

        time.sleep(5)

        # check the Entreprise checkbox
        entreprise_checkbox = browser.find_element_by_xpath(
            "//label[@for='data_product__company_size_ids-3']"
        )
        entreprise_checkbox.click()

        time.sleep(5)

        # 3. Coverage by myself
        coverage_button = browser.find_element_by_xpath("//a[@data-tab='coverage']")
        coverage_button.click()

        time.sleep(5)

        # Historical Coverage
        historical_coverage_input = browser.find_element_by_xpath(
            '//input[@id="data_product__history"]'
        )
        historical_coverage_input.clear()
        historical_coverage_input.send_keys("1")

        time.sleep(5)

        # 4. Volume and quality
        volume_and_quality_button = browser.find_element_by_xpath("//a[@data-tab='volume_and_quality']")
        volume_and_quality_button.click()

        time.sleep(5)

        # Add Volume
        add_volume_button = browser.find_element_by_xpath("//a[@data-association='volume']")
        add_volume_button.click()

        time.sleep(5)

        # Volume input
        volume_input = browser.find_element_by_xpath("//input[@id='data_product_volume__value'][@type='number']")
        volume_input.clear()
        volume_input.send_keys(str(number_of_records))

        time.sleep(5)

        # unit_input
        unit_input = browser.find_element_by_xpath("//input[@id='data_product_volume__unit'][@type='text']")
        unit_input.clear()
        unit_input.send_keys("records")

        time.sleep(5)

        # Add Quality Attribute
        add_quality_attribute_button = browser.find_element_by_xpath("//a[@data-association='quality']")
        add_quality_attribute_button.click()

        time.sleep(5)

        # quality in % input
        quality_input = browser.find_element_by_xpath("//input[@id='data_product_quality__percentage'][@type='number']")
        quality_input.clear()
        quality_input.send_keys("80")

        time.sleep(5)

        # unit quality input
        unit_quality_input = browser.find_element_by_xpath("//input[@id='data_product_quality__unit'][@type='text']")
        unit_quality_input.clear()
        unit_quality_input.send_keys("match rate")

        time.sleep(5)

        # 5. Attributes
        attributes_button = browser.find_element_by_xpath("//a[@data-tab='attributes']")
        attributes_button.click()

        time.sleep(5)

        # Add Attribute _ company_name
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(5)

        # name input
        name_input = browser.find_element_by_xpath(
            "//input[@id='data_product_attribute_spec__name']"
        )
        name_input.clear()
        name_input.send_keys("company_name")

        time.sleep(5)

        # example input
        example_input = browser.find_element_by_xpath(
            "//input[@id='data_product_attribute_spec__example']"
        )
        example_input.clear()
        example_input.send_keys("Company A")

        time.sleep(5)

        # description input
        description_input = browser.find_element_by_xpath(
            "//input[@id='data_product_attribute_spec__description']"
        )
        description_input.clear()
        description_input.send_keys("A company name")

        time.sleep(5)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "//input[@id='data_product_attribute_spec__number_of_records']"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(5)

        # Add Attribute _ postal_address
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # postal_address input
        postal_address_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[2]/td[2]/div/input"
        )
        postal_address_input.clear()
        postal_address_input.send_keys("postal_address")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[2]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys("1 Street postal address XXX Country")

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[2]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("A postal address")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[2]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ phone_number
        add_attribute_button = browser.find_element_by_xpath(
            "//a[@data-association='attribute_spec']"
        )
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[3]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("phone_number")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[3]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys(str(indicatif_telephonique))

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[3]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("A phone number of the company")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[3]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ website
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[4]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("website")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[4]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys("https://example.example")

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[4]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("A website of the company")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[4]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ email
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[5]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("email")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[5]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys("example@example.example")

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[5]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("An email address of the company")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[5]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ region
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[6]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("region")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[6]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys(str(region))

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[6]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("A region name")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[6]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ activity
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[7]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("activity")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[7]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys("Bank")

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[7]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("An activity")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[7]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ country
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[8]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("country")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[8]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys(str(pays))

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[8]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("A country")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[8]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # 6. Delivery
        delivery_button = browser.find_element_by_xpath("//a[@class='item'][@data-tab='delivery']")
        delivery_button.click()

        time.sleep(5)

        # Email checkbox
        email_checkbox = browser.find_element_by_xpath("//label[@for='data_product__transfer_method_ids-9']")
        email_checkbox.click()

        time.sleep(5)

        # Json checkbox
        json_checkbox = browser.find_element_by_xpath("//label[@for='data_product__data_format_ids-10']")
        json_checkbox.click()

        time.sleep(5)

        #  csv checkbox
        csv_checkbox = browser.find_element_by_xpath("//label[@for='data_product__data_format_ids-12']")
        csv_checkbox.click()

        time.sleep(5)

        # xls checkbox
        xls_checkbox = browser.find_element_by_xpath("//label[@for='data_product__data_format_ids-13']")
        xls_checkbox.click()

        time.sleep(5)

        # sql checkbox
        sql_checkbox = browser.find_element_by_xpath("//label[@for='data_product__data_format_ids-14']")
        sql_checkbox.click()

        time.sleep(5)

        # on-demand checkbox
        on_demand_checkbox = browser.find_element_by_xpath("//label[@for='data_product__transfer_frequency_ids-10']")
        on_demand_checkbox.click()

        time.sleep(5)

        # 7. Pricing
        pricing_button = browser.find_element_by_xpath("//a[@data-tab='pricing']")
        pricing_button.click()

        time.sleep(5)

        # One-off purchase checkbox
        one_off_purchase_checkbox = browser.find_element_by_xpath(
            "//label[@for='data_product_pricing_plan__pricing_model_id-1']"
        )
        one_off_purchase_checkbox.click()

        time.sleep(5)

        # starts at one-off purchase input
        starts_at_one_off_purchase_input = browser.find_element_by_xpath(
            "//input[@id='data_product_pricing_plan__starts_at_price']"
        )
        starts_at_one_off_purchase_input.clear()
        starts_at_one_off_purchase_input.send_keys(str(price))

        time.sleep(5)

    # ok
    def test_push_one_product_for_b2b_contact_data_for_aruba(self):
        print("test_push_one_product_for_b2b_contact_data_for_aruba")

        number_of_records = 1136

        indicatif_telephonique = "(+297) xxx xxxxxx"

        price = "3.99"

        pays = "Aruba"

        region = "Aruba"

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(5)

        # with Firefox
        browser = webdriver.Firefox(executable_path='..\\geckodriver.exe')

        time.sleep(20)

        # maximize window
        browser.maximize_window()

        time.sleep(10)

        # open
        browser.get('https://datarade.ai/')

        time.sleep(15)

        clear_button = browser.find_element_by_xpath("//button[@data-cf-action='reject'][@aria-label='Deny']")
        clear_button.click()

        time.sleep(5)

        sign_in_button = browser.find_element_by_xpath("//a[@class='navbar__item'][@href='/users/sign_in']")
        sign_in_button.click()

        time.sleep(15)

        work_email_input = browser.find_element_by_xpath("//input[@id='user__email'][@name='user[email]']")
        work_email_input.clear()
        work_email_input.send_keys(""
        "")

        time.sleep(5)

        passwrod_input = browser.find_element_by_xpath("//input[@id='user__password'][@name='user[password]']")
        passwrod_input.clear()
        passwrod_input.send_keys("")

        time.sleep(5)

        login_button = browser.find_element_by_xpath("//input[@type='submit'][@name='commit']")
        login_button.click()

        time.sleep(15)

        holomorphe_button = browser.find_element_by_xpath(
            "//a[@class='navbar__item tablet-landscape-hidden'][@href='/my/provider']")
        holomorphe_button.click()

        time.sleep(10)

        new_product_button = browser.find_element_by_xpath(
            "//a[@class='button primary modern small'][@href='/my/provider/data_products/new']")
        new_product_button.click()

        time.sleep(10)

        # 1.Basics
        # Title
        title_input = browser.find_element_by_xpath("//input[@id='data_product__name'][@name='data_product[name]']")
        title_input.clear()

        title = "Holomorphe / B2B Contact Data / Private Company data / " + pays

        title_input.send_keys(title)

        time.sleep(5)

        # Short Description
        short_description_input = browser.find_element_by_xpath(
            "//textarea[@id='data_product__short_description'][@name='data_product[short_description]']")
        short_description_input.clear()

        short_description = "The key benefits of this data product are : valuable, affordable and reliable. " \
                            "The main attributes of this data product are : company name, postal address, " \
                            "phone number, website, email, region, activity and country. " \
                            "The coverage of this data product is : " + pays + "."

        short_description_input.send_keys(short_description)

        time.sleep(5)

        # In-depth Description
        in_depth_description_input = browser.find_element_by_xpath(
            "//textarea[@id='data_product__description'][@name='data_product[description]']")
        in_depth_description_input.clear()

        in_depth_description = "This data product is unique because the work for this data collection was " \
                               "made by a complex algorithm that uses artificial intelligence to operate. " \
                               "The data was generally sourced from the web. The primary use-cases or verticals " \
                               "of this data product are : " \
                               "direct marketing, digital marketing, email marketing, phone marketing, " \
                               "voice over ip marketing, business strategy, business intelligence, " \
                               "customer segmentation, customer location and activity segmentation."

        in_depth_description_input.send_keys(in_depth_description)

        time.sleep(5)

        # 2.Listing
        listing_button = browser.find_element_by_xpath("//a[@data-tab='listing']")
        listing_button.click()

        time.sleep(5)

        data_catgory_1_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[1]/div/div"
        )
        data_catgory_1_select.click()

        time.sleep(5)

        data_catgory_1_value_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[1]/div/div/div[2]/div[4]"
        )
        data_catgory_1_value_select.click()

        time.sleep(5)

        data_catgory_2_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[2]/div/div"
        )
        data_catgory_2_select.click()

        time.sleep(5)

        data_catgory_2_value_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[2]/div/div/div[2]/div[6]"
        )
        data_catgory_2_value_select.click()

        time.sleep(5)

        data_catgory_3_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[3]/div/div"
        )
        data_catgory_3_select.click()

        time.sleep(5)

        data_catgory_3_value_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[3]/div/div/div[2]/div[15]"
        )
        data_catgory_3_value_select.click()

        time.sleep(5)

        data_catgory_4_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[4]/div/div"
        )
        data_catgory_4_select.click()

        time.sleep(5)

        data_catgory_4_value_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[4]/div/div/div[2]/div[20]"
        )
        data_catgory_4_value_select.click()

        time.sleep(5)

        data_catgory_5_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[5]/div/div"
        )
        data_catgory_5_select.click()

        time.sleep(5)

        data_catgory_5_value_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[5]/div/div/div[2]/div[34]"
        )
        data_catgory_5_value_select.click()

        time.sleep(5)

        # check the Small Business checkbox
        small_business_checkbox = browser.find_element_by_xpath(
            "//label[@for='data_product__company_size_ids-1']"
        )
        small_business_checkbox.click()

        time.sleep(5)

        # check the Medium-sized Business checkbox
        medium_sized_business_checkbox = browser.find_element_by_xpath(
            "//label[@for='data_product__company_size_ids-2']"
        )
        medium_sized_business_checkbox.click()

        time.sleep(5)

        # check the Entreprise checkbox
        entreprise_checkbox = browser.find_element_by_xpath(
            "//label[@for='data_product__company_size_ids-3']"
        )
        entreprise_checkbox.click()

        time.sleep(5)

        use_cases_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]"
        )
        use_cases_select.click()

        time.sleep(5)

        use_case_1_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[33]"
        )
        use_case_1_select.click()

        time.sleep(5)

        use_cases_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]"
        )
        use_cases_select.click()

        time.sleep(5)

        use_case_2_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[37]"
        )
        use_case_2_select.click()

        time.sleep(5)

        use_cases_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]"
        )
        use_cases_select.click()

        time.sleep(5)

        use_case_3_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[122]"
        )
        use_case_3_select.click()

        time.sleep(5)

        use_cases_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]"
        )
        use_cases_select.click()

        time.sleep(5)

        use_case_4_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[135]"
        )
        use_case_4_select.click()

        time.sleep(5)

        use_cases_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]"
        )
        use_cases_select.click()

        time.sleep(5)

        use_case_5_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[139]"
        )
        use_case_5_select.click()

        time.sleep(5)

        # 3. Coverage by myself
        coverage_button = browser.find_element_by_xpath("//a[@data-tab='coverage']")
        coverage_button.click()

        time.sleep(5)

        # Historical Coverage
        historical_coverage_input = browser.find_element_by_xpath(
            '//input[@id="data_product__history"]'
        )
        historical_coverage_input.clear()
        historical_coverage_input.send_keys("1")

        time.sleep(5)

        range_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[5]/div/div[2]/div[3]/div[2]/div"
        )
        range_select.click()

        time.sleep(5)

        weeks_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[5]/div/div[2]/div[3]/div[2]/div/div[2]/div[2]"
        )
        weeks_select.click()

        time.sleep(5)

        # 4. Volume and quality
        volume_and_quality_button = browser.find_element_by_xpath("//a[@data-tab='volume_and_quality']")
        volume_and_quality_button.click()

        time.sleep(5)

        # Add Volume
        add_volume_button = browser.find_element_by_xpath("//a[@data-association='volume']")
        add_volume_button.click()

        time.sleep(5)

        # Volume input
        volume_input = browser.find_element_by_xpath("//input[@id='data_product_volume__value'][@type='number']")
        volume_input.clear()
        volume_input.send_keys(str(number_of_records))

        time.sleep(5)

        # unit_input
        unit_input = browser.find_element_by_xpath("//input[@id='data_product_volume__unit'][@type='text']")
        unit_input.clear()
        unit_input.send_keys("records")

        time.sleep(5)

        # Add Quality Attribute
        add_quality_attribute_button = browser.find_element_by_xpath("//a[@data-association='quality']")
        add_quality_attribute_button.click()

        time.sleep(5)

        # quality in % input
        quality_input = browser.find_element_by_xpath("//input[@id='data_product_quality__percentage'][@type='number']")
        quality_input.clear()
        quality_input.send_keys("80")

        time.sleep(5)

        # unit quality input
        unit_quality_input = browser.find_element_by_xpath("//input[@id='data_product_quality__unit'][@type='text']")
        unit_quality_input.clear()
        unit_quality_input.send_keys("match rate")

        time.sleep(5)

        # 5. Attributes
        attributes_button = browser.find_element_by_xpath("//a[@data-tab='attributes']")
        attributes_button.click()

        time.sleep(5)

        # Add Attribute _ company_name
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(5)

        # name input
        name_input = browser.find_element_by_xpath(
            "//input[@id='data_product_attribute_spec__name']"
        )
        name_input.clear()
        name_input.send_keys("company_name")

        time.sleep(5)

        # example input
        example_input = browser.find_element_by_xpath(
            "//input[@id='data_product_attribute_spec__example']"
        )
        example_input.clear()
        example_input.send_keys("Company A")

        time.sleep(5)

        # description input
        description_input = browser.find_element_by_xpath(
            "//input[@id='data_product_attribute_spec__description']"
        )
        description_input.clear()
        description_input.send_keys("A company name")

        time.sleep(5)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "//input[@id='data_product_attribute_spec__number_of_records']"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(5)

        # Add Attribute _ postal_address
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # postal_address input
        postal_address_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[2]/td[2]/div/input"
        )
        postal_address_input.clear()
        postal_address_input.send_keys("postal_address")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[2]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys("1 Street postal address XXX Country")

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[2]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("A postal address")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[2]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ phone_number
        add_attribute_button = browser.find_element_by_xpath(
            "//a[@data-association='attribute_spec']"
        )
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[3]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("phone_number")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[3]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys(str(indicatif_telephonique))

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[3]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("A phone number of the company")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[3]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ website
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[4]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("website")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[4]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys("https://example.example")

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[4]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("A website of the company")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[4]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ email
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[5]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("email")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[5]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys("example@example.example")

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[5]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("An email address of the company")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[5]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ region
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[6]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("region")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[6]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys(str(region))

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[6]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("A region name")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[6]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ activity
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[7]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("activity")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[7]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys("Bank")

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[7]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("An activity")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[7]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ country
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[8]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("country")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[8]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys(str(pays))

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[8]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("A country")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[8]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # 6. Delivery
        delivery_button = browser.find_element_by_xpath("//a[@class='item'][@data-tab='delivery']")
        delivery_button.click()

        time.sleep(5)

        # Email checkbox
        email_checkbox = browser.find_element_by_xpath("//label[@for='data_product__transfer_method_ids-9']")
        email_checkbox.click()

        time.sleep(5)

        # Json checkbox
        json_checkbox = browser.find_element_by_xpath("//label[@for='data_product__data_format_ids-10']")
        json_checkbox.click()

        time.sleep(5)

        #  csv checkbox
        csv_checkbox = browser.find_element_by_xpath("//label[@for='data_product__data_format_ids-12']")
        csv_checkbox.click()

        time.sleep(5)

        # xls checkbox
        xls_checkbox = browser.find_element_by_xpath("//label[@for='data_product__data_format_ids-13']")
        xls_checkbox.click()

        time.sleep(5)

        # sql checkbox
        sql_checkbox = browser.find_element_by_xpath("//label[@for='data_product__data_format_ids-14']")
        sql_checkbox.click()

        time.sleep(5)

        # on-demand checkbox
        on_demand_checkbox = browser.find_element_by_xpath("//label[@for='data_product__transfer_frequency_ids-10']")
        on_demand_checkbox.click()

        time.sleep(5)

        # 7. Pricing
        pricing_button = browser.find_element_by_xpath("//a[@data-tab='pricing']")
        pricing_button.click()

        time.sleep(5)

        # One-off purchase checkbox
        one_off_purchase_checkbox = browser.find_element_by_xpath(
            "//label[@for='data_product_pricing_plan__pricing_model_id-1']"
        )
        one_off_purchase_checkbox.click()

        time.sleep(5)

        # starts at one-off purchase input
        starts_at_one_off_purchase_input = browser.find_element_by_xpath(
            "//input[@id='data_product_pricing_plan__starts_at_price']"
        )
        starts_at_one_off_purchase_input.clear()
        starts_at_one_off_purchase_input.send_keys(str(price))

        time.sleep(5)

        currency_select = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[9]/div/div[2]/div[2]/div"
        )
        currency_select.click()

        time.sleep(5)

        eur_select = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[9]/div/div[2]/div[2]/div/div[2]/div[2]"
        )
        eur_select.click()

        time.sleep(5)

    # ok
    def test_push_one_product_for_b2b_contact_data_for_bahamas(self):
        print("test_push_one_product_for_b2b_contact_data_for_bahamas")

        number_of_records = 2588

        indicatif_telephonique = "(+1242) xxx xxxxxx"

        price = "3.99"

        pays = "Bahamas"

        region = "Abaco"

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(5)

        # with Firefox
        browser = webdriver.Firefox(executable_path='..\\geckodriver.exe')

        time.sleep(20)

        # maximize window
        browser.maximize_window()

        time.sleep(10)

        # open
        browser.get('https://datarade.ai/')

        time.sleep(15)

        clear_button = browser.find_element_by_xpath("//button[@data-cf-action='reject'][@aria-label='Deny']")
        clear_button.click()

        time.sleep(5)

        sign_in_button = browser.find_element_by_xpath("//a[@class='navbar__item'][@href='/users/sign_in']")
        sign_in_button.click()

        time.sleep(15)

        work_email_input = browser.find_element_by_xpath("//input[@id='user__email'][@name='user[email]']")
        work_email_input.clear()
        work_email_input.send_keys(""
        "")

        time.sleep(5)

        passwrod_input = browser.find_element_by_xpath("//input[@id='user__password'][@name='user[password]']")
        passwrod_input.clear()
        passwrod_input.send_keys("")

        time.sleep(5)

        login_button = browser.find_element_by_xpath("//input[@type='submit'][@name='commit']")
        login_button.click()

        time.sleep(15)

        holomorphe_button = browser.find_element_by_xpath(
            "//a[@class='navbar__item tablet-landscape-hidden'][@href='/my/provider']")
        holomorphe_button.click()

        time.sleep(10)

        new_product_button = browser.find_element_by_xpath(
            "//a[@class='button primary modern small'][@href='/my/provider/data_products/new']")
        new_product_button.click()

        time.sleep(10)

        # 1.Basics
        # Title
        title_input = browser.find_element_by_xpath("//input[@id='data_product__name'][@name='data_product[name]']")
        title_input.clear()

        title = "Holomorphe / B2B Contact Data / Private Company data / " + pays

        title_input.send_keys(title)

        time.sleep(5)

        # Short Description
        short_description_input = browser.find_element_by_xpath(
            "//textarea[@id='data_product__short_description'][@name='data_product[short_description]']")
        short_description_input.clear()

        short_description = "The key benefits of this data product are : valuable, affordable and reliable. " \
                            "The main attributes of this data product are : company name, postal address, " \
                            "phone number, website, email, region, activity and country. " \
                            "The coverage of this data product is : " + pays + "."

        short_description_input.send_keys(short_description)

        time.sleep(5)

        # In-depth Description
        in_depth_description_input = browser.find_element_by_xpath(
            "//textarea[@id='data_product__description'][@name='data_product[description]']")
        in_depth_description_input.clear()

        in_depth_description = "This data product is unique because the work for this data collection was " \
                               "made by a complex algorithm that uses artificial intelligence to operate. " \
                               "The data was generally sourced from the web. The primary use-cases or verticals " \
                               "of this data product are : " \
                               "direct marketing, digital marketing, email marketing, phone marketing, " \
                               "voice over ip marketing, business strategy, business intelligence, " \
                               "customer segmentation, customer location and activity segmentation."

        in_depth_description_input.send_keys(in_depth_description)

        time.sleep(5)

        # 2.Listing
        listing_button = browser.find_element_by_xpath("//a[@data-tab='listing']")
        listing_button.click()

        time.sleep(5)

        data_catgory_1_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[1]/div/div"
        )
        data_catgory_1_select.click()

        time.sleep(5)

        data_catgory_1_value_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[1]/div/div/div[2]/div[4]"
        )
        data_catgory_1_value_select.click()

        time.sleep(5)

        data_catgory_2_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[2]/div/div"
        )
        data_catgory_2_select.click()

        time.sleep(5)

        data_catgory_2_value_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[2]/div/div/div[2]/div[6]"
        )
        data_catgory_2_value_select.click()

        time.sleep(5)

        data_catgory_3_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[3]/div/div"
        )
        data_catgory_3_select.click()

        time.sleep(5)

        data_catgory_3_value_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[3]/div/div/div[2]/div[15]"
        )
        data_catgory_3_value_select.click()

        time.sleep(5)

        data_catgory_4_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[4]/div/div"
        )
        data_catgory_4_select.click()

        time.sleep(5)

        data_catgory_4_value_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[4]/div/div/div[2]/div[20]"
        )
        data_catgory_4_value_select.click()

        time.sleep(5)

        data_catgory_5_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[5]/div/div"
        )
        data_catgory_5_select.click()

        time.sleep(5)

        data_catgory_5_value_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[5]/div/div/div[2]/div[34]"
        )
        data_catgory_5_value_select.click()

        time.sleep(5)

        # check the Small Business checkbox
        small_business_checkbox = browser.find_element_by_xpath(
            "//label[@for='data_product__company_size_ids-1']"
        )
        small_business_checkbox.click()

        time.sleep(5)

        # check the Medium-sized Business checkbox
        medium_sized_business_checkbox = browser.find_element_by_xpath(
            "//label[@for='data_product__company_size_ids-2']"
        )
        medium_sized_business_checkbox.click()

        time.sleep(5)

        # check the Entreprise checkbox
        entreprise_checkbox = browser.find_element_by_xpath(
            "//label[@for='data_product__company_size_ids-3']"
        )
        entreprise_checkbox.click()

        time.sleep(5)

        use_cases_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]"
        )
        use_cases_select.click()

        time.sleep(5)

        use_case_1_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[33]"
        )
        use_case_1_select.click()

        time.sleep(5)

        use_cases_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]"
        )
        use_cases_select.click()

        time.sleep(5)

        use_case_2_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[37]"
        )
        use_case_2_select.click()

        time.sleep(5)

        use_cases_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]"
        )
        use_cases_select.click()

        time.sleep(5)

        use_case_3_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[122]"
        )
        use_case_3_select.click()

        time.sleep(5)

        use_cases_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]"
        )
        use_cases_select.click()

        time.sleep(5)

        use_case_4_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[135]"
        )
        use_case_4_select.click()

        time.sleep(5)

        use_cases_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]"
        )
        use_cases_select.click()

        time.sleep(5)

        use_case_5_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[139]"
        )
        use_case_5_select.click()

        time.sleep(5)

        # 3. Coverage by myself
        coverage_button = browser.find_element_by_xpath("//a[@data-tab='coverage']")
        coverage_button.click()

        time.sleep(5)

        # Historical Coverage
        historical_coverage_input = browser.find_element_by_xpath(
            '//input[@id="data_product__history"]'
        )
        historical_coverage_input.clear()
        historical_coverage_input.send_keys("1")

        time.sleep(5)

        range_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[5]/div/div[2]/div[3]/div[2]/div"
        )
        range_select.click()

        time.sleep(5)

        weeks_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[5]/div/div[2]/div[3]/div[2]/div/div[2]/div[2]"
        )
        weeks_select.click()

        time.sleep(5)

        # 4. Volume and quality
        volume_and_quality_button = browser.find_element_by_xpath("//a[@data-tab='volume_and_quality']")
        volume_and_quality_button.click()

        time.sleep(5)

        # Add Volume
        add_volume_button = browser.find_element_by_xpath("//a[@data-association='volume']")
        add_volume_button.click()

        time.sleep(5)

        # Volume input
        volume_input = browser.find_element_by_xpath("//input[@id='data_product_volume__value'][@type='number']")
        volume_input.clear()
        volume_input.send_keys(str(number_of_records))

        time.sleep(5)

        # unit_input
        unit_input = browser.find_element_by_xpath("//input[@id='data_product_volume__unit'][@type='text']")
        unit_input.clear()
        unit_input.send_keys("records")

        time.sleep(5)

        # Add Quality Attribute
        add_quality_attribute_button = browser.find_element_by_xpath("//a[@data-association='quality']")
        add_quality_attribute_button.click()

        time.sleep(5)

        # quality in % input
        quality_input = browser.find_element_by_xpath("//input[@id='data_product_quality__percentage'][@type='number']")
        quality_input.clear()
        quality_input.send_keys("80")

        time.sleep(5)

        # unit quality input
        unit_quality_input = browser.find_element_by_xpath("//input[@id='data_product_quality__unit'][@type='text']")
        unit_quality_input.clear()
        unit_quality_input.send_keys("match rate")

        time.sleep(5)

        # 5. Attributes
        attributes_button = browser.find_element_by_xpath("//a[@data-tab='attributes']")
        attributes_button.click()

        time.sleep(5)

        # Add Attribute _ company_name
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(5)

        # name input
        name_input = browser.find_element_by_xpath(
            "//input[@id='data_product_attribute_spec__name']"
        )
        name_input.clear()
        name_input.send_keys("company_name")

        time.sleep(5)

        # example input
        example_input = browser.find_element_by_xpath(
            "//input[@id='data_product_attribute_spec__example']"
        )
        example_input.clear()
        example_input.send_keys("Company A")

        time.sleep(5)

        # description input
        description_input = browser.find_element_by_xpath(
            "//input[@id='data_product_attribute_spec__description']"
        )
        description_input.clear()
        description_input.send_keys("A company name")

        time.sleep(5)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "//input[@id='data_product_attribute_spec__number_of_records']"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(5)

        # Add Attribute _ postal_address
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # postal_address input
        postal_address_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[2]/td[2]/div/input"
        )
        postal_address_input.clear()
        postal_address_input.send_keys("postal_address")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[2]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys("1 Street postal address XXX Country")

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[2]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("A postal address")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[2]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ phone_number
        add_attribute_button = browser.find_element_by_xpath(
            "//a[@data-association='attribute_spec']"
        )
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[3]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("phone_number")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[3]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys(str(indicatif_telephonique))

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[3]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("A phone number of the company")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[3]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ website
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[4]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("website")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[4]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys("https://example.example")

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[4]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("A website of the company")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[4]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ email
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[5]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("email")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[5]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys("example@example.example")

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[5]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("An email address of the company")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[5]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ region
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[6]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("region")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[6]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys(str(region))

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[6]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("A region name")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[6]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ activity
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[7]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("activity")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[7]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys("Bank")

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[7]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("An activity")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[7]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ country
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[8]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("country")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[8]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys(str(pays))

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[8]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("A country")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[8]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # 6. Delivery
        delivery_button = browser.find_element_by_xpath("//a[@class='item'][@data-tab='delivery']")
        delivery_button.click()

        time.sleep(5)

        # Email checkbox
        email_checkbox = browser.find_element_by_xpath("//label[@for='data_product__transfer_method_ids-9']")
        email_checkbox.click()

        time.sleep(5)

        # Json checkbox
        json_checkbox = browser.find_element_by_xpath("//label[@for='data_product__data_format_ids-10']")
        json_checkbox.click()

        time.sleep(5)

        #  csv checkbox
        csv_checkbox = browser.find_element_by_xpath("//label[@for='data_product__data_format_ids-12']")
        csv_checkbox.click()

        time.sleep(5)

        # xls checkbox
        xls_checkbox = browser.find_element_by_xpath("//label[@for='data_product__data_format_ids-13']")
        xls_checkbox.click()

        time.sleep(5)

        # sql checkbox
        sql_checkbox = browser.find_element_by_xpath("//label[@for='data_product__data_format_ids-14']")
        sql_checkbox.click()

        time.sleep(5)

        # on-demand checkbox
        on_demand_checkbox = browser.find_element_by_xpath("//label[@for='data_product__transfer_frequency_ids-10']")
        on_demand_checkbox.click()

        time.sleep(5)

        # 7. Pricing
        pricing_button = browser.find_element_by_xpath("//a[@data-tab='pricing']")
        pricing_button.click()

        time.sleep(5)

        # One-off purchase checkbox
        one_off_purchase_checkbox = browser.find_element_by_xpath(
            "//label[@for='data_product_pricing_plan__pricing_model_id-1']"
        )
        one_off_purchase_checkbox.click()

        time.sleep(5)

        # starts at one-off purchase input
        starts_at_one_off_purchase_input = browser.find_element_by_xpath(
            "//input[@id='data_product_pricing_plan__starts_at_price']"
        )
        starts_at_one_off_purchase_input.clear()
        starts_at_one_off_purchase_input.send_keys(str(price))

        time.sleep(5)

        currency_select = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[9]/div/div[2]/div[2]/div"
        )
        currency_select.click()

        time.sleep(5)

        eur_select = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[9]/div/div[2]/div[2]/div/div[2]/div[2]"
        )
        eur_select.click()

        time.sleep(5)

    # ok
    def test_push_one_product_for_b2b_contact_data_for_colombia(self):
        print("test_push_one_product_for_b2b_contact_data_for_colombia")

        number_of_records = 62438

        indicatif_telephonique = "(+57) xxx xxxxxx"

        price = "9.99"

        pays = "Colombia"

        region = "Bogota"

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(5)

        # with Firefox
        browser = webdriver.Firefox(executable_path='..\\geckodriver.exe')

        time.sleep(20)

        # maximize window
        browser.maximize_window()

        time.sleep(10)

        # open
        browser.get('https://datarade.ai/')

        time.sleep(15)

        clear_button = browser.find_element_by_xpath("//button[@data-cf-action='reject'][@aria-label='Deny']")
        clear_button.click()

        time.sleep(5)

        sign_in_button = browser.find_element_by_xpath("//a[@class='navbar__item'][@href='/users/sign_in']")
        sign_in_button.click()

        time.sleep(15)

        work_email_input = browser.find_element_by_xpath("//input[@id='user__email'][@name='user[email]']")
        work_email_input.clear()
        work_email_input.send_keys(""
        "")

        time.sleep(5)

        passwrod_input = browser.find_element_by_xpath("//input[@id='user__password'][@name='user[password]']")
        passwrod_input.clear()
        passwrod_input.send_keys("")

        time.sleep(5)

        login_button = browser.find_element_by_xpath("//input[@type='submit'][@name='commit']")
        login_button.click()

        time.sleep(15)

        holomorphe_button = browser.find_element_by_xpath(
            "//a[@class='navbar__item tablet-landscape-hidden'][@href='/my/provider']")
        holomorphe_button.click()

        time.sleep(10)

        new_product_button = browser.find_element_by_xpath(
            "//a[@class='button primary modern small'][@href='/my/provider/data_products/new']")
        new_product_button.click()

        time.sleep(10)

        # 1.Basics
        # Title
        title_input = browser.find_element_by_xpath("//input[@id='data_product__name'][@name='data_product[name]']")
        title_input.clear()

        title = "Holomorphe / B2B Contact Data / Private Company data / " + pays

        title_input.send_keys(title)

        time.sleep(5)

        # Short Description
        short_description_input = browser.find_element_by_xpath(
            "//textarea[@id='data_product__short_description'][@name='data_product[short_description]']")
        short_description_input.clear()

        short_description = "The key benefits of this data product are : valuable, affordable and reliable. " \
                            "The main attributes of this data product are : company name, postal address, " \
                            "phone number, website, email, region, activity and country. " \
                            "The coverage of this data product is : " + pays + "."

        short_description_input.send_keys(short_description)

        time.sleep(5)

        # In-depth Description
        in_depth_description_input = browser.find_element_by_xpath(
            "//textarea[@id='data_product__description'][@name='data_product[description]']")
        in_depth_description_input.clear()

        in_depth_description = "This data product is efficient because the work for this data collection was " \
                               "made by a complex algorithm that uses artificial intelligence to operate. " \
                               "The data was generally sourced from the web. The primary use-cases or verticals of " \
                               "this data product are : direct marketing, digital marketing, email marketing, " \
                               "phone marketing, voice over ip marketing, business strategy, business intelligence, " \
                               "customer segmentation, customer location and activity segmentation. The activities " \
                               "of B2B contact data are : employment agencies, real estate agencies, recruitment " \
                               "agencies, software, hotel, social, cleaning, charity, financial, restaurant, " \
                               "building, hairdresser, florist, locksmith, bakery, insurance, pharmacy, mover, " \
                               "electricity, plumbing, security, attorney, bank, garage, dentist, doctor, " \
                               "accountant, grocery, notary, jewellery, tailor, butcher, library, architect, cement, " \
                               "heating, boat, cold, steel, chemical, gas and gold."

        in_depth_description_input.send_keys(in_depth_description)

        time.sleep(5)

        # 2.Listing
        listing_button = browser.find_element_by_xpath("//a[@data-tab='listing']")
        listing_button.click()

        time.sleep(5)

        data_catgory_1_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[1]/div/div"
        )
        data_catgory_1_select.click()

        time.sleep(5)

        data_catgory_1_value_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[1]/div/div/div[2]/div[4]"
        )
        data_catgory_1_value_select.click()

        time.sleep(5)

        data_catgory_2_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[2]/div/div"
        )
        data_catgory_2_select.click()

        time.sleep(5)

        data_catgory_2_value_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[2]/div/div/div[2]/div[6]"
        )
        data_catgory_2_value_select.click()

        time.sleep(5)

        data_catgory_3_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[3]/div/div"
        )
        data_catgory_3_select.click()

        time.sleep(5)

        data_catgory_3_value_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[3]/div/div/div[2]/div[15]"
        )
        data_catgory_3_value_select.click()

        time.sleep(5)

        data_catgory_4_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[4]/div/div"
        )
        data_catgory_4_select.click()

        time.sleep(5)

        data_catgory_4_value_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[4]/div/div/div[2]/div[20]"
        )
        data_catgory_4_value_select.click()

        time.sleep(5)

        data_catgory_5_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[5]/div/div"
        )
        data_catgory_5_select.click()

        time.sleep(5)

        data_catgory_5_value_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[5]/div/div/div[2]/div[34]"
        )
        data_catgory_5_value_select.click()

        time.sleep(5)

        # check the Small Business checkbox
        small_business_checkbox = browser.find_element_by_xpath(
            "//label[@for='data_product__company_size_ids-1']"
        )
        small_business_checkbox.click()

        time.sleep(5)

        # check the Medium-sized Business checkbox
        medium_sized_business_checkbox = browser.find_element_by_xpath(
            "//label[@for='data_product__company_size_ids-2']"
        )
        medium_sized_business_checkbox.click()

        time.sleep(5)

        # check the Entreprise checkbox
        entreprise_checkbox = browser.find_element_by_xpath(
            "//label[@for='data_product__company_size_ids-3']"
        )
        entreprise_checkbox.click()

        time.sleep(5)

        use_cases_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]"
        )
        use_cases_select.click()

        time.sleep(5)

        use_case_1_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[33]"
        )
        use_case_1_select.click()

        time.sleep(5)

        use_cases_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]"
        )
        use_cases_select.click()

        time.sleep(5)

        use_case_2_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[37]"
        )
        use_case_2_select.click()

        time.sleep(5)

        use_cases_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]"
        )
        use_cases_select.click()

        time.sleep(5)

        use_case_3_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[122]"
        )
        use_case_3_select.click()

        time.sleep(5)

        use_cases_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]"
        )
        use_cases_select.click()

        time.sleep(5)

        use_case_4_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[135]"
        )
        use_case_4_select.click()

        time.sleep(5)

        use_cases_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]"
        )
        use_cases_select.click()

        time.sleep(5)

        use_case_5_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[139]"
        )
        use_case_5_select.click()

        time.sleep(5)

        # 3. Coverage by myself
        coverage_button = browser.find_element_by_xpath("//a[@data-tab='coverage']")
        coverage_button.click()

        time.sleep(5)

        # Historical Coverage
        historical_coverage_input = browser.find_element_by_xpath(
            '//input[@id="data_product__history"]'
        )
        historical_coverage_input.clear()
        historical_coverage_input.send_keys("1")

        time.sleep(5)

        range_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[5]/div/div[2]/div[3]/div[2]/div"
        )
        range_select.click()

        time.sleep(5)

        weeks_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[5]/div/div[2]/div[3]/div[2]/div/div[2]/div[2]"
        )
        weeks_select.click()

        time.sleep(5)

        # 4. Volume and quality
        volume_and_quality_button = browser.find_element_by_xpath("//a[@data-tab='volume_and_quality']")
        volume_and_quality_button.click()

        time.sleep(5)

        # Add Volume
        add_volume_button = browser.find_element_by_xpath("//a[@data-association='volume']")
        add_volume_button.click()

        time.sleep(5)

        # Volume input
        volume_input = browser.find_element_by_xpath("//input[@id='data_product_volume__value'][@type='number']")
        volume_input.clear()
        volume_input.send_keys(str(number_of_records))

        time.sleep(5)

        # unit_input
        unit_input = browser.find_element_by_xpath("//input[@id='data_product_volume__unit'][@type='text']")
        unit_input.clear()
        unit_input.send_keys("records")

        time.sleep(5)

        # Add Quality Attribute
        add_quality_attribute_button = browser.find_element_by_xpath("//a[@data-association='quality']")
        add_quality_attribute_button.click()

        time.sleep(5)

        # quality in % input
        quality_input = browser.find_element_by_xpath("//input[@id='data_product_quality__percentage'][@type='number']")
        quality_input.clear()
        quality_input.send_keys("80")

        time.sleep(5)

        # unit quality input
        unit_quality_input = browser.find_element_by_xpath("//input[@id='data_product_quality__unit'][@type='text']")
        unit_quality_input.clear()
        unit_quality_input.send_keys("match rate")

        time.sleep(5)

        # 5. Attributes
        attributes_button = browser.find_element_by_xpath("//a[@data-tab='attributes']")
        attributes_button.click()

        time.sleep(5)

        # Add Attribute _ company_name
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(5)

        # name input
        name_input = browser.find_element_by_xpath(
            "//input[@id='data_product_attribute_spec__name']"
        )
        name_input.clear()
        name_input.send_keys("company_name")

        time.sleep(5)

        # example input
        example_input = browser.find_element_by_xpath(
            "//input[@id='data_product_attribute_spec__example']"
        )
        example_input.clear()
        example_input.send_keys("Company A")

        time.sleep(5)

        # description input
        description_input = browser.find_element_by_xpath(
            "//input[@id='data_product_attribute_spec__description']"
        )
        description_input.clear()
        description_input.send_keys("A company name")

        time.sleep(5)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "//input[@id='data_product_attribute_spec__number_of_records']"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(5)

        # Add Attribute _ postal_address
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # postal_address input
        postal_address_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[2]/td[2]/div/input"
        )
        postal_address_input.clear()
        postal_address_input.send_keys("postal_address")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[2]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys("1 Street postal address XXX Country")

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[2]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("A postal address")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[2]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ phone_number
        add_attribute_button = browser.find_element_by_xpath(
            "//a[@data-association='attribute_spec']"
        )
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[3]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("phone_number")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[3]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys(str(indicatif_telephonique))

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[3]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("A phone number of the company")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[3]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ website
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[4]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("website")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[4]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys("https://example.example")

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[4]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("A website of the company")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[4]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ email
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[5]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("email")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[5]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys("example@example.example")

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[5]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("An email address of the company")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[5]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ region
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[6]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("region")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[6]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys(str(region))

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[6]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("A region name")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[6]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ activity
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[7]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("activity")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[7]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys("Bank")

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[7]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("An activity")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[7]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ country
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[8]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("country")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[8]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys(str(pays))

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[8]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("A country")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[8]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # 6. Delivery
        delivery_button = browser.find_element_by_xpath("//a[@class='item'][@data-tab='delivery']")
        delivery_button.click()

        time.sleep(5)

        # Email checkbox
        email_checkbox = browser.find_element_by_xpath("//label[@for='data_product__transfer_method_ids-9']")
        email_checkbox.click()

        time.sleep(5)

        # Json checkbox
        json_checkbox = browser.find_element_by_xpath("//label[@for='data_product__data_format_ids-10']")
        json_checkbox.click()

        time.sleep(5)

        #  csv checkbox
        csv_checkbox = browser.find_element_by_xpath("//label[@for='data_product__data_format_ids-12']")
        csv_checkbox.click()

        time.sleep(5)

        # xls checkbox
        xls_checkbox = browser.find_element_by_xpath("//label[@for='data_product__data_format_ids-13']")
        xls_checkbox.click()

        time.sleep(5)

        # sql checkbox
        sql_checkbox = browser.find_element_by_xpath("//label[@for='data_product__data_format_ids-14']")
        sql_checkbox.click()

        time.sleep(5)

        # on-demand checkbox
        on_demand_checkbox = browser.find_element_by_xpath("//label[@for='data_product__transfer_frequency_ids-10']")
        on_demand_checkbox.click()

        time.sleep(5)

        # 7. Pricing
        pricing_button = browser.find_element_by_xpath("//a[@data-tab='pricing']")
        pricing_button.click()

        time.sleep(5)

        # One-off purchase checkbox
        one_off_purchase_checkbox = browser.find_element_by_xpath(
            "//label[@for='data_product_pricing_plan__pricing_model_id-1']"
        )
        one_off_purchase_checkbox.click()

        time.sleep(5)

        # starts at one-off purchase input
        starts_at_one_off_purchase_input = browser.find_element_by_xpath(
            "//input[@id='data_product_pricing_plan__starts_at_price']"
        )
        starts_at_one_off_purchase_input.clear()
        starts_at_one_off_purchase_input.send_keys(str(price))

        time.sleep(5)

        currency_select = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[9]/div/div[2]/div[2]/div"
        )
        currency_select.click()

        time.sleep(5)

        eur_select = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[9]/div/div[2]/div[2]/div/div[2]/div[2]"
        )
        eur_select.click()

        time.sleep(5)

    # ok
    def test_push_one_product_for_b2b_contact_data_for_bonaire(self):
        print("test_push_one_product_for_b2b_contact_data_for_bonaire")

        number_of_records = 242

        indicatif_telephonique = "(+599) xxx xxxxxx"

        price = "1.99"

        pays = "Bonaire"

        region = "Bonaire"

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(5)

        # with Firefox
        browser = webdriver.Firefox(executable_path='..\\geckodriver.exe')

        time.sleep(20)

        # maximize window
        browser.maximize_window()

        time.sleep(10)

        # open
        browser.get('https://datarade.ai/')

        time.sleep(15)

        clear_button = browser.find_element_by_xpath("//button[@data-cf-action='reject'][@aria-label='Deny']")
        clear_button.click()

        time.sleep(5)

        sign_in_button = browser.find_element_by_xpath("//a[@class='navbar__item'][@href='/users/sign_in']")
        sign_in_button.click()

        time.sleep(15)

        work_email_input = browser.find_element_by_xpath("//input[@id='user__email'][@name='user[email]']")
        work_email_input.clear()
        work_email_input.send_keys(""
        "")

        time.sleep(5)

        passwrod_input = browser.find_element_by_xpath("//input[@id='user__password'][@name='user[password]']")
        passwrod_input.clear()
        passwrod_input.send_keys("")

        time.sleep(5)

        login_button = browser.find_element_by_xpath("//input[@type='submit'][@name='commit']")
        login_button.click()

        time.sleep(15)

        holomorphe_button = browser.find_element_by_xpath(
            "//a[@class='navbar__item tablet-landscape-hidden'][@href='/my/provider']")
        holomorphe_button.click()

        time.sleep(10)

        new_product_button = browser.find_element_by_xpath(
            "//a[@class='button primary modern small'][@href='/my/provider/data_products/new']")
        new_product_button.click()

        time.sleep(10)

        # 1.Basics
        # Title
        title_input = browser.find_element_by_xpath("//input[@id='data_product__name'][@name='data_product[name]']")
        title_input.clear()

        title = "Holomorphe / B2B Contact Data / Private Company data / " + pays

        title_input.send_keys(title)

        time.sleep(5)

        # Short Description
        short_description_input = browser.find_element_by_xpath(
            "//textarea[@id='data_product__short_description'][@name='data_product[short_description]']")
        short_description_input.clear()

        short_description = "The key benefits of this data product are : valuable, affordable and reliable. " \
                            "The main attributes of this data product are : company name, postal address, " \
                            "phone number, website, email, region, activity and country. " \
                            "The coverage of this data product is : " + pays + "."

        short_description_input.send_keys(short_description)

        time.sleep(5)

        # In-depth Description
        in_depth_description_input = browser.find_element_by_xpath(
            "//textarea[@id='data_product__description'][@name='data_product[description]']")
        in_depth_description_input.clear()

        in_depth_description = "This data product is efficient because the work for this data collection was " \
                               "made by a complex algorithm that uses artificial intelligence to operate. " \
                               "The data was generally sourced from the web. The primary use-cases or verticals of " \
                               "this data product are : direct marketing, digital marketing, email marketing, " \
                               "phone marketing, voice over ip marketing, business strategy, business intelligence, " \
                               "customer segmentation, customer location and activity segmentation. The activities " \
                               "of B2B contact data are : employment agencies, real estate agencies, recruitment " \
                               "agencies, software, hotel, social, cleaning, charity, financial, restaurant, " \
                               "building, hairdresser, florist, locksmith, bakery, insurance, pharmacy, mover, " \
                               "electricity, plumbing, security, attorney, bank, garage, dentist, doctor, " \
                               "accountant, grocery, notary, jewellery, tailor, butcher, library, architect, cement, " \
                               "heating, boat, cold, steel, chemical, gas and gold."

        in_depth_description_input.send_keys(in_depth_description)

        time.sleep(5)

        # 2.Listing
        listing_button = browser.find_element_by_xpath("//a[@data-tab='listing']")
        listing_button.click()

        time.sleep(5)

        data_catgory_1_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[1]/div/div"
        )
        data_catgory_1_select.click()

        time.sleep(5)

        data_catgory_1_value_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[1]/div/div/div[2]/div[4]"
        )
        data_catgory_1_value_select.click()

        time.sleep(5)

        data_catgory_2_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[2]/div/div"
        )
        data_catgory_2_select.click()

        time.sleep(5)

        data_catgory_2_value_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[2]/div/div/div[2]/div[6]"
        )
        data_catgory_2_value_select.click()

        time.sleep(5)

        data_catgory_3_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[3]/div/div"
        )
        data_catgory_3_select.click()

        time.sleep(5)

        data_catgory_3_value_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[3]/div/div/div[2]/div[15]"
        )
        data_catgory_3_value_select.click()

        time.sleep(5)

        data_catgory_4_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[4]/div/div"
        )
        data_catgory_4_select.click()

        time.sleep(5)

        data_catgory_4_value_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[4]/div/div/div[2]/div[20]"
        )
        data_catgory_4_value_select.click()

        time.sleep(5)

        data_catgory_5_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[5]/div/div"
        )
        data_catgory_5_select.click()

        time.sleep(5)

        data_catgory_5_value_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[5]/div/div/div[2]/div[34]"
        )
        data_catgory_5_value_select.click()

        time.sleep(5)

        # check the Small Business checkbox
        small_business_checkbox = browser.find_element_by_xpath(
            "//label[@for='data_product__company_size_ids-1']"
        )
        small_business_checkbox.click()

        time.sleep(5)

        # check the Medium-sized Business checkbox
        medium_sized_business_checkbox = browser.find_element_by_xpath(
            "//label[@for='data_product__company_size_ids-2']"
        )
        medium_sized_business_checkbox.click()

        time.sleep(5)

        # check the Entreprise checkbox
        entreprise_checkbox = browser.find_element_by_xpath(
            "//label[@for='data_product__company_size_ids-3']"
        )
        entreprise_checkbox.click()

        time.sleep(5)

        use_cases_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]"
        )
        use_cases_select.click()

        time.sleep(5)

        use_case_1_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[33]"
        )
        use_case_1_select.click()

        time.sleep(5)

        use_cases_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]"
        )
        use_cases_select.click()

        time.sleep(5)

        use_case_2_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[37]"
        )
        use_case_2_select.click()

        time.sleep(5)

        use_cases_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]"
        )
        use_cases_select.click()

        time.sleep(5)

        use_case_3_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[122]"
        )
        use_case_3_select.click()

        time.sleep(5)

        use_cases_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]"
        )
        use_cases_select.click()

        time.sleep(5)

        use_case_4_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[135]"
        )
        use_case_4_select.click()

        time.sleep(5)

        use_cases_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]"
        )
        use_cases_select.click()

        time.sleep(5)

        use_case_5_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[139]"
        )
        use_case_5_select.click()

        time.sleep(5)

        # 3. Coverage by myself
        coverage_button = browser.find_element_by_xpath("//a[@data-tab='coverage']")
        coverage_button.click()

        time.sleep(5)

        # Historical Coverage
        historical_coverage_input = browser.find_element_by_xpath(
            '//input[@id="data_product__history"]'
        )
        historical_coverage_input.clear()
        historical_coverage_input.send_keys("1")

        time.sleep(5)

        range_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[5]/div/div[2]/div[3]/div[2]/div"
        )
        range_select.click()

        time.sleep(5)

        weeks_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[5]/div/div[2]/div[3]/div[2]/div/div[2]/div[2]"
        )
        weeks_select.click()

        time.sleep(5)

        # 4. Volume and quality
        volume_and_quality_button = browser.find_element_by_xpath("//a[@data-tab='volume_and_quality']")
        volume_and_quality_button.click()

        time.sleep(5)

        # Add Volume
        add_volume_button = browser.find_element_by_xpath("//a[@data-association='volume']")
        add_volume_button.click()

        time.sleep(5)

        # Volume input
        volume_input = browser.find_element_by_xpath("//input[@id='data_product_volume__value'][@type='number']")
        volume_input.clear()
        volume_input.send_keys(str(number_of_records))

        time.sleep(5)

        # unit_input
        unit_input = browser.find_element_by_xpath("//input[@id='data_product_volume__unit'][@type='text']")
        unit_input.clear()
        unit_input.send_keys("records")

        time.sleep(5)

        # Add Quality Attribute
        add_quality_attribute_button = browser.find_element_by_xpath("//a[@data-association='quality']")
        add_quality_attribute_button.click()

        time.sleep(5)

        # quality in % input
        quality_input = browser.find_element_by_xpath("//input[@id='data_product_quality__percentage'][@type='number']")
        quality_input.clear()
        quality_input.send_keys("80")

        time.sleep(5)

        # unit quality input
        unit_quality_input = browser.find_element_by_xpath("//input[@id='data_product_quality__unit'][@type='text']")
        unit_quality_input.clear()
        unit_quality_input.send_keys("match rate")

        time.sleep(5)

        # 5. Attributes
        attributes_button = browser.find_element_by_xpath("//a[@data-tab='attributes']")
        attributes_button.click()

        time.sleep(5)

        # Add Attribute _ company_name
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(5)

        # name input
        name_input = browser.find_element_by_xpath(
            "//input[@id='data_product_attribute_spec__name']"
        )
        name_input.clear()
        name_input.send_keys("company_name")

        time.sleep(5)

        # example input
        example_input = browser.find_element_by_xpath(
            "//input[@id='data_product_attribute_spec__example']"
        )
        example_input.clear()
        example_input.send_keys("Company A")

        time.sleep(5)

        # description input
        description_input = browser.find_element_by_xpath(
            "//input[@id='data_product_attribute_spec__description']"
        )
        description_input.clear()
        description_input.send_keys("A company name")

        time.sleep(5)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "//input[@id='data_product_attribute_spec__number_of_records']"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(5)

        # Add Attribute _ postal_address
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # postal_address input
        postal_address_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[2]/td[2]/div/input"
        )
        postal_address_input.clear()
        postal_address_input.send_keys("postal_address")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[2]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys("1 Street postal address XXX Country")

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[2]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("A postal address")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[2]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ phone_number
        add_attribute_button = browser.find_element_by_xpath(
            "//a[@data-association='attribute_spec']"
        )
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[3]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("phone_number")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[3]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys(str(indicatif_telephonique))

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[3]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("A phone number of the company")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[3]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ website
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[4]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("website")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[4]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys("https://example.example")

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[4]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("A website of the company")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[4]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ email
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[5]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("email")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[5]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys("example@example.example")

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[5]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("An email address of the company")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[5]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ region
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[6]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("region")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[6]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys(str(region))

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[6]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("A region name")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[6]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ activity
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[7]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("activity")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[7]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys("Bank")

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[7]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("An activity")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[7]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ country
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[8]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("country")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[8]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys(str(pays))

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[8]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("A country")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[8]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # 6. Delivery
        delivery_button = browser.find_element_by_xpath("//a[@class='item'][@data-tab='delivery']")
        delivery_button.click()

        time.sleep(5)

        # Email checkbox
        email_checkbox = browser.find_element_by_xpath("//label[@for='data_product__transfer_method_ids-9']")
        email_checkbox.click()

        time.sleep(5)

        # Json checkbox
        json_checkbox = browser.find_element_by_xpath("//label[@for='data_product__data_format_ids-10']")
        json_checkbox.click()

        time.sleep(5)

        #  csv checkbox
        csv_checkbox = browser.find_element_by_xpath("//label[@for='data_product__data_format_ids-12']")
        csv_checkbox.click()

        time.sleep(5)

        # xls checkbox
        xls_checkbox = browser.find_element_by_xpath("//label[@for='data_product__data_format_ids-13']")
        xls_checkbox.click()

        time.sleep(5)

        # sql checkbox
        sql_checkbox = browser.find_element_by_xpath("//label[@for='data_product__data_format_ids-14']")
        sql_checkbox.click()

        time.sleep(5)

        # on-demand checkbox
        on_demand_checkbox = browser.find_element_by_xpath("//label[@for='data_product__transfer_frequency_ids-10']")
        on_demand_checkbox.click()

        time.sleep(5)

        # 7. Pricing
        pricing_button = browser.find_element_by_xpath("//a[@data-tab='pricing']")
        pricing_button.click()

        time.sleep(5)

        # One-off purchase checkbox
        one_off_purchase_checkbox = browser.find_element_by_xpath(
            "//label[@for='data_product_pricing_plan__pricing_model_id-1']"
        )
        one_off_purchase_checkbox.click()

        time.sleep(5)

        # starts at one-off purchase input
        starts_at_one_off_purchase_input = browser.find_element_by_xpath(
            "//input[@id='data_product_pricing_plan__starts_at_price']"
        )
        starts_at_one_off_purchase_input.clear()
        starts_at_one_off_purchase_input.send_keys(str(price))

        time.sleep(5)

        currency_select = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[9]/div/div[2]/div[2]/div"
        )
        currency_select.click()

        time.sleep(5)

        eur_select = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[9]/div/div[2]/div[2]/div/div[2]/div[2]"
        )
        eur_select.click()

        time.sleep(5)

    # ok
    def test_push_one_product_for_b2b_contact_data_for_grenada(self):
        print("test_push_one_product_for_b2b_contact_data_for_grenada")

        number_of_records = 830

        indicatif_telephonique = "(+473) xxx xxxxxx"

        price = "1.99"

        pays = "Grenada"

        region = "Grenada"

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(5)

        # with Firefox
        browser = webdriver.Firefox(executable_path='..\\geckodriver.exe')

        time.sleep(20)

        # maximize window
        browser.maximize_window()

        time.sleep(10)

        # open
        browser.get('https://datarade.ai/')

        time.sleep(15)

        clear_button = browser.find_element_by_xpath("//button[@data-cf-action='reject'][@aria-label='Deny']")
        clear_button.click()

        time.sleep(5)

        sign_in_button = browser.find_element_by_xpath("//a[@class='navbar__item'][@href='/users/sign_in']")
        sign_in_button.click()

        time.sleep(15)

        work_email_input = browser.find_element_by_xpath("//input[@id='user__email'][@name='user[email]']")
        work_email_input.clear()
        work_email_input.send_keys(""
        "")

        time.sleep(5)

        passwrod_input = browser.find_element_by_xpath("//input[@id='user__password'][@name='user[password]']")
        passwrod_input.clear()
        passwrod_input.send_keys("")

        time.sleep(5)

        login_button = browser.find_element_by_xpath("//input[@type='submit'][@name='commit']")
        login_button.click()

        time.sleep(15)

        holomorphe_button = browser.find_element_by_xpath(
            "//a[@class='navbar__item tablet-landscape-hidden'][@href='/my/provider']")
        holomorphe_button.click()

        time.sleep(10)

        new_product_button = browser.find_element_by_xpath(
            "//a[@class='button primary modern small'][@href='/my/provider/data_products/new']")
        new_product_button.click()

        time.sleep(10)

        # 1.Basics
        # Title
        title_input = browser.find_element_by_xpath("//input[@id='data_product__name'][@name='data_product[name]']")
        title_input.clear()

        title = "Holomorphe / B2B Contact Data / Private Company data / " + pays

        title_input.send_keys(title)

        time.sleep(5)

        # Short Description
        short_description_input = browser.find_element_by_xpath(
            "//textarea[@id='data_product__short_description'][@name='data_product[short_description]']")
        short_description_input.clear()

        short_description = "The key benefits of this data product are : valuable, affordable and reliable. " \
                            "The main attributes of this data product are : company name, postal address, " \
                            "phone number, website, email, region, activity and country. " \
                            "The coverage of this data product is : " + pays + "."

        short_description_input.send_keys(short_description)

        time.sleep(5)

        # In-depth Description
        in_depth_description_input = browser.find_element_by_xpath(
            "//textarea[@id='data_product__description'][@name='data_product[description]']")
        in_depth_description_input.clear()

        in_depth_description = "This data product is efficient because the work for this data collection was " \
                               "made by a complex algorithm that uses artificial intelligence to operate. " \
                               "The data was generally sourced from the web. The primary use-cases or verticals of " \
                               "this data product are : direct marketing, digital marketing, email marketing, " \
                               "phone marketing, voice over ip marketing, business strategy, business intelligence, " \
                               "customer segmentation, customer location and activity segmentation. The activities " \
                               "of B2B contact data are : employment agencies, real estate agencies, recruitment " \
                               "agencies, software, hotel, social, cleaning, charity, financial, restaurant, " \
                               "building, hairdresser, florist, locksmith, bakery, insurance, pharmacy, mover, " \
                               "electricity, plumbing, security, attorney, bank, garage, dentist, doctor, " \
                               "accountant, grocery, notary, jewellery, tailor, butcher, library, architect, cement, " \
                               "heating, boat, cold, steel, chemical, gas and gold."

        in_depth_description_input.send_keys(in_depth_description)

        time.sleep(5)

        # 2.Listing
        listing_button = browser.find_element_by_xpath("//a[@data-tab='listing']")
        listing_button.click()

        time.sleep(5)

        data_catgory_1_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[1]/div/div"
        )
        data_catgory_1_select.click()

        time.sleep(5)

        data_catgory_1_value_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[1]/div/div/div[2]/div[4]"
        )
        data_catgory_1_value_select.click()

        time.sleep(5)

        data_catgory_2_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[2]/div/div"
        )
        data_catgory_2_select.click()

        time.sleep(5)

        data_catgory_2_value_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[2]/div/div/div[2]/div[6]"
        )
        data_catgory_2_value_select.click()

        time.sleep(5)

        data_catgory_3_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[3]/div/div"
        )
        data_catgory_3_select.click()

        time.sleep(5)

        data_catgory_3_value_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[3]/div/div/div[2]/div[15]"
        )
        data_catgory_3_value_select.click()

        time.sleep(5)

        data_catgory_4_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[4]/div/div"
        )
        data_catgory_4_select.click()

        time.sleep(5)

        data_catgory_4_value_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[4]/div/div/div[2]/div[20]"
        )
        data_catgory_4_value_select.click()

        time.sleep(5)

        data_catgory_5_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[5]/div/div"
        )
        data_catgory_5_select.click()

        time.sleep(5)

        data_catgory_5_value_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[5]/div/div/div[2]/div[34]"
        )
        data_catgory_5_value_select.click()

        time.sleep(5)

        # check the Small Business checkbox
        small_business_checkbox = browser.find_element_by_xpath(
            "//label[@for='data_product__company_size_ids-1']"
        )
        small_business_checkbox.click()

        time.sleep(5)

        # check the Medium-sized Business checkbox
        medium_sized_business_checkbox = browser.find_element_by_xpath(
            "//label[@for='data_product__company_size_ids-2']"
        )
        medium_sized_business_checkbox.click()

        time.sleep(5)

        # check the Entreprise checkbox
        entreprise_checkbox = browser.find_element_by_xpath(
            "//label[@for='data_product__company_size_ids-3']"
        )
        entreprise_checkbox.click()

        time.sleep(5)

        use_cases_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]"
        )
        use_cases_select.click()

        time.sleep(5)

        use_case_1_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[33]"
        )
        use_case_1_select.click()

        time.sleep(5)

        use_cases_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]"
        )
        use_cases_select.click()

        time.sleep(5)

        use_case_2_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[37]"
        )
        use_case_2_select.click()

        time.sleep(5)

        use_cases_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]"
        )
        use_cases_select.click()

        time.sleep(5)

        use_case_3_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[122]"
        )
        use_case_3_select.click()

        time.sleep(5)

        use_cases_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]"
        )
        use_cases_select.click()

        time.sleep(5)

        use_case_4_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[135]"
        )
        use_case_4_select.click()

        time.sleep(5)

        use_cases_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]"
        )
        use_cases_select.click()

        time.sleep(5)

        use_case_5_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[139]"
        )
        use_case_5_select.click()

        time.sleep(5)

        # 3. Coverage by myself
        coverage_button = browser.find_element_by_xpath("//a[@data-tab='coverage']")
        coverage_button.click()

        time.sleep(5)

        # Historical Coverage
        historical_coverage_input = browser.find_element_by_xpath(
            '//input[@id="data_product__history"]'
        )
        historical_coverage_input.clear()
        historical_coverage_input.send_keys("1")

        time.sleep(5)

        range_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[5]/div/div[2]/div[3]/div[2]/div"
        )
        range_select.click()

        time.sleep(5)

        weeks_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[5]/div/div[2]/div[3]/div[2]/div/div[2]/div[2]"
        )
        weeks_select.click()

        time.sleep(5)

        # 4. Volume and quality
        volume_and_quality_button = browser.find_element_by_xpath("//a[@data-tab='volume_and_quality']")
        volume_and_quality_button.click()

        time.sleep(5)

        # Add Volume
        add_volume_button = browser.find_element_by_xpath("//a[@data-association='volume']")
        add_volume_button.click()

        time.sleep(5)

        # Volume input
        volume_input = browser.find_element_by_xpath("//input[@id='data_product_volume__value'][@type='number']")
        volume_input.clear()
        volume_input.send_keys(str(number_of_records))

        time.sleep(5)

        # unit_input
        unit_input = browser.find_element_by_xpath("//input[@id='data_product_volume__unit'][@type='text']")
        unit_input.clear()
        unit_input.send_keys("records")

        time.sleep(5)

        # Add Quality Attribute
        add_quality_attribute_button = browser.find_element_by_xpath("//a[@data-association='quality']")
        add_quality_attribute_button.click()

        time.sleep(5)

        # quality in % input
        quality_input = browser.find_element_by_xpath("//input[@id='data_product_quality__percentage'][@type='number']")
        quality_input.clear()
        quality_input.send_keys("80")

        time.sleep(5)

        # unit quality input
        unit_quality_input = browser.find_element_by_xpath("//input[@id='data_product_quality__unit'][@type='text']")
        unit_quality_input.clear()
        unit_quality_input.send_keys("match rate")

        time.sleep(5)

        # 5. Attributes
        attributes_button = browser.find_element_by_xpath("//a[@data-tab='attributes']")
        attributes_button.click()

        time.sleep(5)

        # Add Attribute _ company_name
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(5)

        # name input
        name_input = browser.find_element_by_xpath(
            "//input[@id='data_product_attribute_spec__name']"
        )
        name_input.clear()
        name_input.send_keys("company_name")

        time.sleep(5)

        # example input
        example_input = browser.find_element_by_xpath(
            "//input[@id='data_product_attribute_spec__example']"
        )
        example_input.clear()
        example_input.send_keys("Company A")

        time.sleep(5)

        # description input
        description_input = browser.find_element_by_xpath(
            "//input[@id='data_product_attribute_spec__description']"
        )
        description_input.clear()
        description_input.send_keys("A company name")

        time.sleep(5)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "//input[@id='data_product_attribute_spec__number_of_records']"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(5)

        # Add Attribute _ postal_address
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # postal_address input
        postal_address_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[2]/td[2]/div/input"
        )
        postal_address_input.clear()
        postal_address_input.send_keys("postal_address")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[2]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys("1 Street postal address XXX Country")

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[2]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("A postal address")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[2]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ phone_number
        add_attribute_button = browser.find_element_by_xpath(
            "//a[@data-association='attribute_spec']"
        )
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[3]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("phone_number")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[3]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys(str(indicatif_telephonique))

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[3]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("A phone number of the company")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[3]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ website
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[4]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("website")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[4]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys("https://example.example")

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[4]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("A website of the company")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[4]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ email
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[5]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("email")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[5]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys("example@example.example")

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[5]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("An email address of the company")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[5]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ region
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[6]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("region")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[6]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys(str(region))

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[6]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("A region name")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[6]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ activity
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[7]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("activity")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[7]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys("Bank")

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[7]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("An activity")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[7]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ country
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[8]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("country")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[8]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys(str(pays))

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[8]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("A country")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[8]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # 6. Delivery
        delivery_button = browser.find_element_by_xpath("//a[@class='item'][@data-tab='delivery']")
        delivery_button.click()

        time.sleep(5)

        # Email checkbox
        email_checkbox = browser.find_element_by_xpath("//label[@for='data_product__transfer_method_ids-9']")
        email_checkbox.click()

        time.sleep(5)

        # Json checkbox
        json_checkbox = browser.find_element_by_xpath("//label[@for='data_product__data_format_ids-10']")
        json_checkbox.click()

        time.sleep(5)

        #  csv checkbox
        csv_checkbox = browser.find_element_by_xpath("//label[@for='data_product__data_format_ids-12']")
        csv_checkbox.click()

        time.sleep(5)

        # xls checkbox
        xls_checkbox = browser.find_element_by_xpath("//label[@for='data_product__data_format_ids-13']")
        xls_checkbox.click()

        time.sleep(5)

        # sql checkbox
        sql_checkbox = browser.find_element_by_xpath("//label[@for='data_product__data_format_ids-14']")
        sql_checkbox.click()

        time.sleep(5)

        # on-demand checkbox
        on_demand_checkbox = browser.find_element_by_xpath("//label[@for='data_product__transfer_frequency_ids-10']")
        on_demand_checkbox.click()

        time.sleep(5)

        # 7. Pricing
        pricing_button = browser.find_element_by_xpath("//a[@data-tab='pricing']")
        pricing_button.click()

        time.sleep(5)

        # One-off purchase checkbox
        one_off_purchase_checkbox = browser.find_element_by_xpath(
            "//label[@for='data_product_pricing_plan__pricing_model_id-1']"
        )
        one_off_purchase_checkbox.click()

        time.sleep(5)

        # starts at one-off purchase input
        starts_at_one_off_purchase_input = browser.find_element_by_xpath(
            "//input[@id='data_product_pricing_plan__starts_at_price']"
        )
        starts_at_one_off_purchase_input.clear()
        starts_at_one_off_purchase_input.send_keys(str(price))

        time.sleep(5)

        currency_select = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[9]/div/div[2]/div[2]/div"
        )
        currency_select.click()

        time.sleep(5)

        eur_select = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[9]/div/div[2]/div[2]/div/div[2]/div[2]"
        )
        eur_select.click()

        time.sleep(5)

    # ok
    def test_push_one_product_for_b2b_contact_data_for_barbados(self):
        print("test_push_one_product_for_b2b_contact_data_for_barbados")

        number_of_records = 2965

        indicatif_telephonique = "(+246) xxx xxxxxx"

        price = "3.99"

        pays = "Barbados"

        region = "Barbados"

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(5)

        # with Firefox
        browser = webdriver.Firefox(executable_path='..\\geckodriver.exe')

        time.sleep(20)

        # maximize window
        browser.maximize_window()

        time.sleep(10)

        # open
        browser.get('https://datarade.ai/')

        time.sleep(15)

        clear_button = browser.find_element_by_xpath("//button[@data-cf-action='reject'][@aria-label='Deny']")
        clear_button.click()

        time.sleep(5)

        sign_in_button = browser.find_element_by_xpath("//a[@class='navbar__item'][@href='/users/sign_in']")
        sign_in_button.click()

        time.sleep(15)

        work_email_input = browser.find_element_by_xpath("//input[@id='user__email'][@name='user[email]']")
        work_email_input.clear()
        work_email_input.send_keys(""
        "")

        time.sleep(5)

        passwrod_input = browser.find_element_by_xpath("//input[@id='user__password'][@name='user[password]']")
        passwrod_input.clear()
        passwrod_input.send_keys("")

        time.sleep(5)

        login_button = browser.find_element_by_xpath("//input[@type='submit'][@name='commit']")
        login_button.click()

        time.sleep(15)

        holomorphe_button = browser.find_element_by_xpath(
            "//a[@class='navbar__item tablet-landscape-hidden'][@href='/my/provider']")
        holomorphe_button.click()

        time.sleep(10)

        new_product_button = browser.find_element_by_xpath(
            "//a[@class='button primary modern small'][@href='/my/provider/data_products/new']")
        new_product_button.click()

        time.sleep(10)

        # 1.Basics
        # Title
        title_input = browser.find_element_by_xpath("//input[@id='data_product__name'][@name='data_product[name]']")
        title_input.clear()

        title = "Holomorphe / B2B Contact Data / Private Company data / " + pays

        title_input.send_keys(title)

        time.sleep(5)

        # Short Description
        short_description_input = browser.find_element_by_xpath(
            "//textarea[@id='data_product__short_description'][@name='data_product[short_description]']")
        short_description_input.clear()

        short_description = "The key benefits of this data product are : valuable, affordable and reliable. " \
                            "The main attributes of this data product are : company name, postal address, " \
                            "phone number, website, email, region, activity and country. " \
                            "The coverage of this data product is : " + pays + "."

        short_description_input.send_keys(short_description)

        time.sleep(5)

        # In-depth Description
        in_depth_description_input = browser.find_element_by_xpath(
            "//textarea[@id='data_product__description'][@name='data_product[description]']")
        in_depth_description_input.clear()

        in_depth_description = "This data product is efficient because the work for this data collection was " \
                               "made by a complex algorithm that uses artificial intelligence to operate. " \
                               "The data was generally sourced from the web. The primary use-cases or verticals of " \
                               "this data product are : direct marketing, digital marketing, email marketing, " \
                               "phone marketing, voice over ip marketing, business strategy, business intelligence, " \
                               "customer segmentation, customer location and activity segmentation. The activities " \
                               "of B2B contact data are : employment agencies, real estate agencies, recruitment " \
                               "agencies, software, hotel, social, cleaning, charity, financial, restaurant, " \
                               "building, hairdresser, florist, locksmith, bakery, insurance, pharmacy, mover, " \
                               "electricity, plumbing, security, attorney, bank, garage, dentist, doctor, " \
                               "accountant, grocery, notary, jewellery, tailor, butcher, library, architect, cement, " \
                               "heating, boat, cold, steel, chemical, gas and gold."

        in_depth_description_input.send_keys(in_depth_description)

        time.sleep(5)

        # 2.Listing
        listing_button = browser.find_element_by_xpath("//a[@data-tab='listing']")
        listing_button.click()

        time.sleep(5)

        data_catgory_1_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[1]/div/div"
        )
        data_catgory_1_select.click()

        time.sleep(5)

        data_catgory_1_value_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[1]/div/div/div[2]/div[4]"
        )
        data_catgory_1_value_select.click()

        time.sleep(5)

        data_catgory_2_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[2]/div/div"
        )
        data_catgory_2_select.click()

        time.sleep(5)

        data_catgory_2_value_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[2]/div/div/div[2]/div[6]"
        )
        data_catgory_2_value_select.click()

        time.sleep(5)

        data_catgory_3_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[3]/div/div"
        )
        data_catgory_3_select.click()

        time.sleep(5)

        data_catgory_3_value_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[3]/div/div/div[2]/div[15]"
        )
        data_catgory_3_value_select.click()

        time.sleep(5)

        data_catgory_4_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[4]/div/div"
        )
        data_catgory_4_select.click()

        time.sleep(5)

        data_catgory_4_value_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[4]/div/div/div[2]/div[20]"
        )
        data_catgory_4_value_select.click()

        time.sleep(5)

        data_catgory_5_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[5]/div/div"
        )
        data_catgory_5_select.click()

        time.sleep(5)

        data_catgory_5_value_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[5]/div/div/div[2]/div[34]"
        )
        data_catgory_5_value_select.click()

        time.sleep(5)

        # check the Small Business checkbox
        small_business_checkbox = browser.find_element_by_xpath(
            "//label[@for='data_product__company_size_ids-1']"
        )
        small_business_checkbox.click()

        time.sleep(5)

        # check the Medium-sized Business checkbox
        medium_sized_business_checkbox = browser.find_element_by_xpath(
            "//label[@for='data_product__company_size_ids-2']"
        )
        medium_sized_business_checkbox.click()

        time.sleep(5)

        # check the Entreprise checkbox
        entreprise_checkbox = browser.find_element_by_xpath(
            "//label[@for='data_product__company_size_ids-3']"
        )
        entreprise_checkbox.click()

        time.sleep(5)

        use_cases_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]"
        )
        use_cases_select.click()

        time.sleep(5)

        use_case_1_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[33]"
        )
        use_case_1_select.click()

        time.sleep(5)

        use_cases_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]"
        )
        use_cases_select.click()

        time.sleep(5)

        use_case_2_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[37]"
        )
        use_case_2_select.click()

        time.sleep(5)

        use_cases_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]"
        )
        use_cases_select.click()

        time.sleep(5)

        use_case_3_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[122]"
        )
        use_case_3_select.click()

        time.sleep(5)

        use_cases_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]"
        )
        use_cases_select.click()

        time.sleep(5)

        use_case_4_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[135]"
        )
        use_case_4_select.click()

        time.sleep(5)

        use_cases_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]"
        )
        use_cases_select.click()

        time.sleep(5)

        use_case_5_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[139]"
        )
        use_case_5_select.click()

        time.sleep(5)

        # 3. Coverage by myself
        coverage_button = browser.find_element_by_xpath("//a[@data-tab='coverage']")
        coverage_button.click()

        time.sleep(5)

        # Historical Coverage
        historical_coverage_input = browser.find_element_by_xpath(
            '//input[@id="data_product__history"]'
        )
        historical_coverage_input.clear()
        historical_coverage_input.send_keys("1")

        time.sleep(5)

        range_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[5]/div/div[2]/div[3]/div[2]/div"
        )
        range_select.click()

        time.sleep(5)

        weeks_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[5]/div/div[2]/div[3]/div[2]/div/div[2]/div[2]"
        )
        weeks_select.click()

        time.sleep(5)

        # 4. Volume and quality
        volume_and_quality_button = browser.find_element_by_xpath("//a[@data-tab='volume_and_quality']")
        volume_and_quality_button.click()

        time.sleep(5)

        # Add Volume
        add_volume_button = browser.find_element_by_xpath("//a[@data-association='volume']")
        add_volume_button.click()

        time.sleep(5)

        # Volume input
        volume_input = browser.find_element_by_xpath("//input[@id='data_product_volume__value'][@type='number']")
        volume_input.clear()
        volume_input.send_keys(str(number_of_records))

        time.sleep(5)

        # unit_input
        unit_input = browser.find_element_by_xpath("//input[@id='data_product_volume__unit'][@type='text']")
        unit_input.clear()
        unit_input.send_keys("records")

        time.sleep(5)

        # Add Quality Attribute
        add_quality_attribute_button = browser.find_element_by_xpath("//a[@data-association='quality']")
        add_quality_attribute_button.click()

        time.sleep(5)

        # quality in % input
        quality_input = browser.find_element_by_xpath("//input[@id='data_product_quality__percentage'][@type='number']")
        quality_input.clear()
        quality_input.send_keys("80")

        time.sleep(5)

        # unit quality input
        unit_quality_input = browser.find_element_by_xpath("//input[@id='data_product_quality__unit'][@type='text']")
        unit_quality_input.clear()
        unit_quality_input.send_keys("match rate")

        time.sleep(5)

        # 5. Attributes
        attributes_button = browser.find_element_by_xpath("//a[@data-tab='attributes']")
        attributes_button.click()

        time.sleep(5)

        # Add Attribute _ company_name
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(5)

        # name input
        name_input = browser.find_element_by_xpath(
            "//input[@id='data_product_attribute_spec__name']"
        )
        name_input.clear()
        name_input.send_keys("company_name")

        time.sleep(5)

        # example input
        example_input = browser.find_element_by_xpath(
            "//input[@id='data_product_attribute_spec__example']"
        )
        example_input.clear()
        example_input.send_keys("Company A")

        time.sleep(5)

        # description input
        description_input = browser.find_element_by_xpath(
            "//input[@id='data_product_attribute_spec__description']"
        )
        description_input.clear()
        description_input.send_keys("A company name")

        time.sleep(5)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "//input[@id='data_product_attribute_spec__number_of_records']"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(5)

        # Add Attribute _ postal_address
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # postal_address input
        postal_address_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[2]/td[2]/div/input"
        )
        postal_address_input.clear()
        postal_address_input.send_keys("postal_address")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[2]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys("1 Street postal address XXX Country")

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[2]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("A postal address")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[2]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ phone_number
        add_attribute_button = browser.find_element_by_xpath(
            "//a[@data-association='attribute_spec']"
        )
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[3]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("phone_number")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[3]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys(str(indicatif_telephonique))

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[3]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("A phone number of the company")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[3]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ website
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[4]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("website")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[4]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys("https://example.example")

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[4]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("A website of the company")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[4]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ email
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[5]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("email")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[5]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys("example@example.example")

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[5]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("An email address of the company")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[5]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ region
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[6]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("region")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[6]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys(str(region))

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[6]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("A region name")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[6]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ activity
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[7]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("activity")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[7]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys("Bank")

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[7]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("An activity")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[7]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ country
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[8]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("country")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[8]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys(str(pays))

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[8]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("A country")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[8]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # 6. Delivery
        delivery_button = browser.find_element_by_xpath("//a[@class='item'][@data-tab='delivery']")
        delivery_button.click()

        time.sleep(5)

        # Email checkbox
        email_checkbox = browser.find_element_by_xpath("//label[@for='data_product__transfer_method_ids-9']")
        email_checkbox.click()

        time.sleep(5)

        # Json checkbox
        json_checkbox = browser.find_element_by_xpath("//label[@for='data_product__data_format_ids-10']")
        json_checkbox.click()

        time.sleep(5)

        #  csv checkbox
        csv_checkbox = browser.find_element_by_xpath("//label[@for='data_product__data_format_ids-12']")
        csv_checkbox.click()

        time.sleep(5)

        # xls checkbox
        xls_checkbox = browser.find_element_by_xpath("//label[@for='data_product__data_format_ids-13']")
        xls_checkbox.click()

        time.sleep(5)

        # sql checkbox
        sql_checkbox = browser.find_element_by_xpath("//label[@for='data_product__data_format_ids-14']")
        sql_checkbox.click()

        time.sleep(5)

        # on-demand checkbox
        on_demand_checkbox = browser.find_element_by_xpath("//label[@for='data_product__transfer_frequency_ids-10']")
        on_demand_checkbox.click()

        time.sleep(5)

        # 7. Pricing
        pricing_button = browser.find_element_by_xpath("//a[@data-tab='pricing']")
        pricing_button.click()

        time.sleep(5)

        # One-off purchase checkbox
        one_off_purchase_checkbox = browser.find_element_by_xpath(
            "//label[@for='data_product_pricing_plan__pricing_model_id-1']"
        )
        one_off_purchase_checkbox.click()

        time.sleep(5)

        # starts at one-off purchase input
        starts_at_one_off_purchase_input = browser.find_element_by_xpath(
            "//input[@id='data_product_pricing_plan__starts_at_price']"
        )
        starts_at_one_off_purchase_input.clear()
        starts_at_one_off_purchase_input.send_keys(str(price))

        time.sleep(5)

        currency_select = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[9]/div/div[2]/div[2]/div"
        )
        currency_select.click()

        time.sleep(5)

        eur_select = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[9]/div/div[2]/div[2]/div/div[2]/div[2]"
        )
        eur_select.click()

        time.sleep(5)

    # ok
    def test_push_one_product_for_b2b_contact_data_for_dominica(self):
        print("test_push_one_product_for_b2b_contact_data_for_dominica")

        number_of_records = 508

        indicatif_telephonique = "(+767) xxx xxxxxx"

        price = "1.99"

        pays = "Dominica"

        region = "Dominica"

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(5)

        # with Firefox
        browser = webdriver.Firefox(executable_path='..\\geckodriver.exe')

        time.sleep(20)

        # maximize window
        browser.maximize_window()

        time.sleep(10)

        # open
        browser.get('https://datarade.ai/')

        time.sleep(15)

        clear_button = browser.find_element_by_xpath("//button[@data-cf-action='reject'][@aria-label='Deny']")
        clear_button.click()

        time.sleep(5)

        sign_in_button = browser.find_element_by_xpath("//a[@class='navbar__item'][@href='/users/sign_in']")
        sign_in_button.click()

        time.sleep(15)

        work_email_input = browser.find_element_by_xpath("//input[@id='user__email'][@name='user[email]']")
        work_email_input.clear()
        work_email_input.send_keys(""
        "")

        time.sleep(5)

        passwrod_input = browser.find_element_by_xpath("//input[@id='user__password'][@name='user[password]']")
        passwrod_input.clear()
        passwrod_input.send_keys("")

        time.sleep(5)

        login_button = browser.find_element_by_xpath("//input[@type='submit'][@name='commit']")
        login_button.click()

        time.sleep(15)

        holomorphe_button = browser.find_element_by_xpath(
            "//a[@class='navbar__item tablet-landscape-hidden'][@href='/my/provider']")
        holomorphe_button.click()

        time.sleep(10)

        new_product_button = browser.find_element_by_xpath(
            "//a[@class='button primary modern small'][@href='/my/provider/data_products/new']")
        new_product_button.click()

        time.sleep(10)

        # 1.Basics
        # Title
        title_input = browser.find_element_by_xpath("//input[@id='data_product__name'][@name='data_product[name]']")
        title_input.clear()

        title = "Holomorphe / B2B Contact Data / Private Company data / " + pays

        title_input.send_keys(title)

        time.sleep(5)

        # Short Description
        short_description_input = browser.find_element_by_xpath(
            "//textarea[@id='data_product__short_description'][@name='data_product[short_description]']")
        short_description_input.clear()

        short_description = "The key benefits of this data product are : valuable, affordable and reliable. " \
                            "The main attributes of this data product are : company name, postal address, " \
                            "phone number, website, email, region, activity and country. " \
                            "The coverage of this data product is : " + pays + "."

        short_description_input.send_keys(short_description)

        time.sleep(5)

        # In-depth Description
        in_depth_description_input = browser.find_element_by_xpath(
            "//textarea[@id='data_product__description'][@name='data_product[description]']")
        in_depth_description_input.clear()

        in_depth_description = "This data product is efficient because the work for this data collection was " \
                               "made by a complex algorithm that uses artificial intelligence to operate. " \
                               "The data was generally sourced from the web. The primary use-cases or verticals of " \
                               "this data product are : direct marketing, digital marketing, email marketing, " \
                               "phone marketing, voice over ip marketing, business strategy, business intelligence, " \
                               "customer segmentation, customer location and activity segmentation. The activities " \
                               "of B2B contact data are : employment agencies, real estate agencies, recruitment " \
                               "agencies, software, hotel, social, cleaning, charity, financial, restaurant, " \
                               "building, hairdresser, florist, locksmith, bakery, insurance, pharmacy, mover, " \
                               "electricity, plumbing, security, attorney, bank, garage, dentist, doctor, " \
                               "accountant, grocery, notary, jewellery, tailor, butcher, library, architect, cement, " \
                               "heating, boat, cold, steel, chemical, gas and gold."

        in_depth_description_input.send_keys(in_depth_description)

        time.sleep(5)

        # 2.Listing
        listing_button = browser.find_element_by_xpath("//a[@data-tab='listing']")
        listing_button.click()

        time.sleep(5)

        data_catgory_1_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[1]/div/div"
        )
        data_catgory_1_select.click()

        time.sleep(5)

        data_catgory_1_value_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[1]/div/div/div[2]/div[4]"
        )
        data_catgory_1_value_select.click()

        time.sleep(5)

        data_catgory_2_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[2]/div/div"
        )
        data_catgory_2_select.click()

        time.sleep(5)

        data_catgory_2_value_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[2]/div/div/div[2]/div[6]"
        )
        data_catgory_2_value_select.click()

        time.sleep(5)

        data_catgory_3_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[3]/div/div"
        )
        data_catgory_3_select.click()

        time.sleep(5)

        data_catgory_3_value_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[3]/div/div/div[2]/div[15]"
        )
        data_catgory_3_value_select.click()

        time.sleep(5)

        data_catgory_4_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[4]/div/div"
        )
        data_catgory_4_select.click()

        time.sleep(5)

        data_catgory_4_value_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[4]/div/div/div[2]/div[20]"
        )
        data_catgory_4_value_select.click()

        time.sleep(5)

        data_catgory_5_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[5]/div/div"
        )
        data_catgory_5_select.click()

        time.sleep(5)

        data_catgory_5_value_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[5]/div/div/div[2]/div[34]"
        )
        data_catgory_5_value_select.click()

        time.sleep(5)

        # check the Small Business checkbox
        small_business_checkbox = browser.find_element_by_xpath(
            "//label[@for='data_product__company_size_ids-1']"
        )
        small_business_checkbox.click()

        time.sleep(5)

        # check the Medium-sized Business checkbox
        medium_sized_business_checkbox = browser.find_element_by_xpath(
            "//label[@for='data_product__company_size_ids-2']"
        )
        medium_sized_business_checkbox.click()

        time.sleep(5)

        # check the Entreprise checkbox
        entreprise_checkbox = browser.find_element_by_xpath(
            "//label[@for='data_product__company_size_ids-3']"
        )
        entreprise_checkbox.click()

        time.sleep(5)

        use_cases_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]"
        )
        use_cases_select.click()

        time.sleep(5)

        use_case_1_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[33]"
        )
        use_case_1_select.click()

        time.sleep(5)

        use_cases_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]"
        )
        use_cases_select.click()

        time.sleep(5)

        use_case_2_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[37]"
        )
        use_case_2_select.click()

        time.sleep(5)

        use_cases_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]"
        )
        use_cases_select.click()

        time.sleep(5)

        use_case_3_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[122]"
        )
        use_case_3_select.click()

        time.sleep(5)

        use_cases_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]"
        )
        use_cases_select.click()

        time.sleep(5)

        use_case_4_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[135]"
        )
        use_case_4_select.click()

        time.sleep(5)

        use_cases_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]"
        )
        use_cases_select.click()

        time.sleep(5)

        use_case_5_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[139]"
        )
        use_case_5_select.click()

        time.sleep(5)

        # 3. Coverage by myself
        coverage_button = browser.find_element_by_xpath("//a[@data-tab='coverage']")
        coverage_button.click()

        time.sleep(5)

        # Historical Coverage
        historical_coverage_input = browser.find_element_by_xpath(
            '//input[@id="data_product__history"]'
        )
        historical_coverage_input.clear()
        historical_coverage_input.send_keys("1")

        time.sleep(5)

        range_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[5]/div/div[2]/div[3]/div[2]/div"
        )
        range_select.click()

        time.sleep(5)

        weeks_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[5]/div/div[2]/div[3]/div[2]/div/div[2]/div[2]"
        )
        weeks_select.click()

        time.sleep(5)

        # 4. Volume and quality
        volume_and_quality_button = browser.find_element_by_xpath("//a[@data-tab='volume_and_quality']")
        volume_and_quality_button.click()

        time.sleep(5)

        # Add Volume
        add_volume_button = browser.find_element_by_xpath("//a[@data-association='volume']")
        add_volume_button.click()

        time.sleep(5)

        # Volume input
        volume_input = browser.find_element_by_xpath("//input[@id='data_product_volume__value'][@type='number']")
        volume_input.clear()
        volume_input.send_keys(str(number_of_records))

        time.sleep(5)

        # unit_input
        unit_input = browser.find_element_by_xpath("//input[@id='data_product_volume__unit'][@type='text']")
        unit_input.clear()
        unit_input.send_keys("records")

        time.sleep(5)

        # Add Quality Attribute
        add_quality_attribute_button = browser.find_element_by_xpath("//a[@data-association='quality']")
        add_quality_attribute_button.click()

        time.sleep(5)

        # quality in % input
        quality_input = browser.find_element_by_xpath("//input[@id='data_product_quality__percentage'][@type='number']")
        quality_input.clear()
        quality_input.send_keys("80")

        time.sleep(5)

        # unit quality input
        unit_quality_input = browser.find_element_by_xpath("//input[@id='data_product_quality__unit'][@type='text']")
        unit_quality_input.clear()
        unit_quality_input.send_keys("match rate")

        time.sleep(5)

        # 5. Attributes
        attributes_button = browser.find_element_by_xpath("//a[@data-tab='attributes']")
        attributes_button.click()

        time.sleep(5)

        # Add Attribute _ company_name
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(5)

        # name input
        name_input = browser.find_element_by_xpath(
            "//input[@id='data_product_attribute_spec__name']"
        )
        name_input.clear()
        name_input.send_keys("company_name")

        time.sleep(5)

        # example input
        example_input = browser.find_element_by_xpath(
            "//input[@id='data_product_attribute_spec__example']"
        )
        example_input.clear()
        example_input.send_keys("Company A")

        time.sleep(5)

        # description input
        description_input = browser.find_element_by_xpath(
            "//input[@id='data_product_attribute_spec__description']"
        )
        description_input.clear()
        description_input.send_keys("A company name")

        time.sleep(5)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "//input[@id='data_product_attribute_spec__number_of_records']"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(5)

        # Add Attribute _ postal_address
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # postal_address input
        postal_address_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[2]/td[2]/div/input"
        )
        postal_address_input.clear()
        postal_address_input.send_keys("postal_address")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[2]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys("1 Street postal address XXX Country")

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[2]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("A postal address")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[2]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ phone_number
        add_attribute_button = browser.find_element_by_xpath(
            "//a[@data-association='attribute_spec']"
        )
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[3]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("phone_number")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[3]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys(str(indicatif_telephonique))

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[3]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("A phone number of the company")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[3]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ website
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[4]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("website")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[4]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys("https://example.example")

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[4]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("A website of the company")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[4]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ email
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[5]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("email")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[5]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys("example@example.example")

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[5]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("An email address of the company")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[5]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ region
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[6]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("region")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[6]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys(str(region))

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[6]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("A region name")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[6]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ activity
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[7]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("activity")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[7]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys("Bank")

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[7]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("An activity")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[7]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ country
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[8]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("country")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[8]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys(str(pays))

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[8]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("A country")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[8]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # 6. Delivery
        delivery_button = browser.find_element_by_xpath("//a[@class='item'][@data-tab='delivery']")
        delivery_button.click()

        time.sleep(5)

        # Email checkbox
        email_checkbox = browser.find_element_by_xpath("//label[@for='data_product__transfer_method_ids-9']")
        email_checkbox.click()

        time.sleep(5)

        # Json checkbox
        json_checkbox = browser.find_element_by_xpath("//label[@for='data_product__data_format_ids-10']")
        json_checkbox.click()

        time.sleep(5)

        #  csv checkbox
        csv_checkbox = browser.find_element_by_xpath("//label[@for='data_product__data_format_ids-12']")
        csv_checkbox.click()

        time.sleep(5)

        # xls checkbox
        xls_checkbox = browser.find_element_by_xpath("//label[@for='data_product__data_format_ids-13']")
        xls_checkbox.click()

        time.sleep(5)

        # sql checkbox
        sql_checkbox = browser.find_element_by_xpath("//label[@for='data_product__data_format_ids-14']")
        sql_checkbox.click()

        time.sleep(5)

        # on-demand checkbox
        on_demand_checkbox = browser.find_element_by_xpath("//label[@for='data_product__transfer_frequency_ids-10']")
        on_demand_checkbox.click()

        time.sleep(5)

        # 7. Pricing
        pricing_button = browser.find_element_by_xpath("//a[@data-tab='pricing']")
        pricing_button.click()

        time.sleep(5)

        # One-off purchase checkbox
        one_off_purchase_checkbox = browser.find_element_by_xpath(
            "//label[@for='data_product_pricing_plan__pricing_model_id-1']"
        )
        one_off_purchase_checkbox.click()

        time.sleep(5)

        # starts at one-off purchase input
        starts_at_one_off_purchase_input = browser.find_element_by_xpath(
            "//input[@id='data_product_pricing_plan__starts_at_price']"
        )
        starts_at_one_off_purchase_input.clear()
        starts_at_one_off_purchase_input.send_keys(str(price))

        time.sleep(5)

        currency_select = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[9]/div/div[2]/div[2]/div"
        )
        currency_select.click()

        time.sleep(5)

        eur_select = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[9]/div/div[2]/div[2]/div/div[2]/div[2]"
        )
        eur_select.click()

        time.sleep(5)

    # ok
    def test_push_one_product_for_b2b_contact_data_for_turks_caicos(self):
        print("test_push_one_product_for_b2b_contact_data_for_turks_caicos")

        number_of_records = 244

        indicatif_telephonique = "(+649) xxx xxxxxx"

        price = "1.99"

        pays = "Turks-Caicos"

        region = "Turks-Caicos"

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(5)

        # with Firefox
        browser = webdriver.Firefox(executable_path='..\\geckodriver.exe')

        time.sleep(20)

        # maximize window
        browser.maximize_window()

        time.sleep(10)

        # open
        browser.get('https://datarade.ai/')

        time.sleep(15)

        clear_button = browser.find_element_by_xpath("//button[@data-cf-action='reject'][@aria-label='Deny']")
        clear_button.click()

        time.sleep(5)

        sign_in_button = browser.find_element_by_xpath("//a[@class='navbar__item'][@href='/users/sign_in']")
        sign_in_button.click()

        time.sleep(15)

        work_email_input = browser.find_element_by_xpath("//input[@id='user__email'][@name='user[email]']")
        work_email_input.clear()
        work_email_input.send_keys(""
        "")

        time.sleep(5)

        passwrod_input = browser.find_element_by_xpath("//input[@id='user__password'][@name='user[password]']")
        passwrod_input.clear()
        passwrod_input.send_keys("")

        time.sleep(5)

        login_button = browser.find_element_by_xpath("//input[@type='submit'][@name='commit']")
        login_button.click()

        time.sleep(15)

        holomorphe_button = browser.find_element_by_xpath(
            "//a[@class='navbar__item tablet-landscape-hidden'][@href='/my/provider']")
        holomorphe_button.click()

        time.sleep(10)

        new_product_button = browser.find_element_by_xpath(
            "//a[@class='button primary modern small'][@href='/my/provider/data_products/new']")
        new_product_button.click()

        time.sleep(10)

        # 1.Basics
        # Title
        title_input = browser.find_element_by_xpath("//input[@id='data_product__name'][@name='data_product[name]']")
        title_input.clear()

        title = "Holomorphe / B2B Contact Data / Private Company data / " + pays

        title_input.send_keys(title)

        time.sleep(5)

        # Short Description
        short_description_input = browser.find_element_by_xpath(
            "//textarea[@id='data_product__short_description'][@name='data_product[short_description]']")
        short_description_input.clear()

        short_description = "The key benefits of this data product are : valuable, affordable and reliable. " \
                            "The main attributes of this data product are : company name, postal address, " \
                            "phone number, website, email, region, activity and country. " \
                            "The coverage of this data product is : " + pays + "."

        short_description_input.send_keys(short_description)

        time.sleep(5)

        # In-depth Description
        in_depth_description_input = browser.find_element_by_xpath(
            "//textarea[@id='data_product__description'][@name='data_product[description]']")
        in_depth_description_input.clear()

        in_depth_description = "This data product is efficient because the work for this data collection was " \
                               "made by a complex algorithm that uses artificial intelligence to operate. " \
                               "The data was generally sourced from the web. The primary use-cases or verticals of " \
                               "this data product are : direct marketing, digital marketing, email marketing, " \
                               "phone marketing, voice over ip marketing, business strategy, business intelligence, " \
                               "customer segmentation, customer location and activity segmentation. The activities " \
                               "of B2B contact data are : employment agencies, real estate agencies, recruitment " \
                               "agencies, software, hotel, social, cleaning, charity, financial, restaurant, " \
                               "building, hairdresser, florist, locksmith, bakery, insurance, pharmacy, mover, " \
                               "electricity, plumbing, security, attorney, bank, garage, dentist, doctor, " \
                               "accountant, grocery, notary, jewellery, tailor, butcher, library, architect, cement, " \
                               "heating, boat, cold, steel, chemical, gas and gold."

        in_depth_description_input.send_keys(in_depth_description)

        time.sleep(5)

        # 2.Listing
        listing_button = browser.find_element_by_xpath("//a[@data-tab='listing']")
        listing_button.click()

        time.sleep(5)

        data_catgory_1_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[1]/div/div"
        )
        data_catgory_1_select.click()

        time.sleep(5)

        data_catgory_1_value_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[1]/div/div/div[2]/div[4]"
        )
        data_catgory_1_value_select.click()

        time.sleep(5)

        data_catgory_2_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[2]/div/div"
        )
        data_catgory_2_select.click()

        time.sleep(5)

        data_catgory_2_value_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[2]/div/div/div[2]/div[6]"
        )
        data_catgory_2_value_select.click()

        time.sleep(5)

        data_catgory_3_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[3]/div/div"
        )
        data_catgory_3_select.click()

        time.sleep(5)

        data_catgory_3_value_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[3]/div/div/div[2]/div[15]"
        )
        data_catgory_3_value_select.click()

        time.sleep(5)

        data_catgory_4_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[4]/div/div"
        )
        data_catgory_4_select.click()

        time.sleep(5)

        data_catgory_4_value_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[4]/div/div/div[2]/div[20]"
        )
        data_catgory_4_value_select.click()

        time.sleep(5)

        data_catgory_5_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[5]/div/div"
        )
        data_catgory_5_select.click()

        time.sleep(5)

        data_catgory_5_value_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[5]/div/div/div[2]/div[34]"
        )
        data_catgory_5_value_select.click()

        time.sleep(5)

        # check the Small Business checkbox
        small_business_checkbox = browser.find_element_by_xpath(
            "//label[@for='data_product__company_size_ids-1']"
        )
        small_business_checkbox.click()

        time.sleep(5)

        # check the Medium-sized Business checkbox
        medium_sized_business_checkbox = browser.find_element_by_xpath(
            "//label[@for='data_product__company_size_ids-2']"
        )
        medium_sized_business_checkbox.click()

        time.sleep(5)

        # check the Entreprise checkbox
        entreprise_checkbox = browser.find_element_by_xpath(
            "//label[@for='data_product__company_size_ids-3']"
        )
        entreprise_checkbox.click()

        time.sleep(5)

        use_cases_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]"
        )
        use_cases_select.click()

        time.sleep(5)

        use_case_1_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[33]"
        )
        use_case_1_select.click()

        time.sleep(5)

        use_cases_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]"
        )
        use_cases_select.click()

        time.sleep(5)

        use_case_2_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[37]"
        )
        use_case_2_select.click()

        time.sleep(5)

        use_cases_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]"
        )
        use_cases_select.click()

        time.sleep(5)

        use_case_3_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[122]"
        )
        use_case_3_select.click()

        time.sleep(5)

        use_cases_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]"
        )
        use_cases_select.click()

        time.sleep(5)

        use_case_4_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[135]"
        )
        use_case_4_select.click()

        time.sleep(5)

        use_cases_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]"
        )
        use_cases_select.click()

        time.sleep(5)

        use_case_5_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[139]"
        )
        use_case_5_select.click()

        time.sleep(5)

        # 3. Coverage by myself
        coverage_button = browser.find_element_by_xpath("//a[@data-tab='coverage']")
        coverage_button.click()

        time.sleep(5)

        # Historical Coverage
        historical_coverage_input = browser.find_element_by_xpath(
            '//input[@id="data_product__history"]'
        )
        historical_coverage_input.clear()
        historical_coverage_input.send_keys("1")

        time.sleep(5)

        range_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[5]/div/div[2]/div[3]/div[2]/div"
        )
        range_select.click()

        time.sleep(5)

        weeks_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[5]/div/div[2]/div[3]/div[2]/div/div[2]/div[2]"
        )
        weeks_select.click()

        time.sleep(5)

        # 4. Volume and quality
        volume_and_quality_button = browser.find_element_by_xpath("//a[@data-tab='volume_and_quality']")
        volume_and_quality_button.click()

        time.sleep(5)

        # Add Volume
        add_volume_button = browser.find_element_by_xpath("//a[@data-association='volume']")
        add_volume_button.click()

        time.sleep(5)

        # Volume input
        volume_input = browser.find_element_by_xpath("//input[@id='data_product_volume__value'][@type='number']")
        volume_input.clear()
        volume_input.send_keys(str(number_of_records))

        time.sleep(5)

        # unit_input
        unit_input = browser.find_element_by_xpath("//input[@id='data_product_volume__unit'][@type='text']")
        unit_input.clear()
        unit_input.send_keys("records")

        time.sleep(5)

        # Add Quality Attribute
        add_quality_attribute_button = browser.find_element_by_xpath("//a[@data-association='quality']")
        add_quality_attribute_button.click()

        time.sleep(5)

        # quality in % input
        quality_input = browser.find_element_by_xpath("//input[@id='data_product_quality__percentage'][@type='number']")
        quality_input.clear()
        quality_input.send_keys("80")

        time.sleep(5)

        # unit quality input
        unit_quality_input = browser.find_element_by_xpath("//input[@id='data_product_quality__unit'][@type='text']")
        unit_quality_input.clear()
        unit_quality_input.send_keys("match rate")

        time.sleep(5)

        # 5. Attributes
        attributes_button = browser.find_element_by_xpath("//a[@data-tab='attributes']")
        attributes_button.click()

        time.sleep(5)

        # Add Attribute _ company_name
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(5)

        # name input
        name_input = browser.find_element_by_xpath(
            "//input[@id='data_product_attribute_spec__name']"
        )
        name_input.clear()
        name_input.send_keys("company_name")

        time.sleep(5)

        # example input
        example_input = browser.find_element_by_xpath(
            "//input[@id='data_product_attribute_spec__example']"
        )
        example_input.clear()
        example_input.send_keys("Company A")

        time.sleep(5)

        # description input
        description_input = browser.find_element_by_xpath(
            "//input[@id='data_product_attribute_spec__description']"
        )
        description_input.clear()
        description_input.send_keys("A company name")

        time.sleep(5)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "//input[@id='data_product_attribute_spec__number_of_records']"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(5)

        # Add Attribute _ postal_address
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # postal_address input
        postal_address_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[2]/td[2]/div/input"
        )
        postal_address_input.clear()
        postal_address_input.send_keys("postal_address")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[2]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys("1 Street postal address XXX Country")

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[2]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("A postal address")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[2]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ phone_number
        add_attribute_button = browser.find_element_by_xpath(
            "//a[@data-association='attribute_spec']"
        )
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[3]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("phone_number")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[3]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys(str(indicatif_telephonique))

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[3]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("A phone number of the company")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[3]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ website
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[4]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("website")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[4]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys("https://example.example")

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[4]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("A website of the company")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[4]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ email
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[5]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("email")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[5]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys("example@example.example")

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[5]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("An email address of the company")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[5]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ region
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[6]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("region")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[6]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys(str(region))

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[6]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("A region name")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[6]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ activity
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[7]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("activity")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[7]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys("Bank")

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[7]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("An activity")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[7]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ country
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[8]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("country")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[8]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys(str(pays))

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[8]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("A country")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[8]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # 6. Delivery
        delivery_button = browser.find_element_by_xpath("//a[@class='item'][@data-tab='delivery']")
        delivery_button.click()

        time.sleep(5)

        # Email checkbox
        email_checkbox = browser.find_element_by_xpath("//label[@for='data_product__transfer_method_ids-9']")
        email_checkbox.click()

        time.sleep(5)

        # Json checkbox
        json_checkbox = browser.find_element_by_xpath("//label[@for='data_product__data_format_ids-10']")
        json_checkbox.click()

        time.sleep(5)

        #  csv checkbox
        csv_checkbox = browser.find_element_by_xpath("//label[@for='data_product__data_format_ids-12']")
        csv_checkbox.click()

        time.sleep(5)

        # xls checkbox
        xls_checkbox = browser.find_element_by_xpath("//label[@for='data_product__data_format_ids-13']")
        xls_checkbox.click()

        time.sleep(5)

        # sql checkbox
        sql_checkbox = browser.find_element_by_xpath("//label[@for='data_product__data_format_ids-14']")
        sql_checkbox.click()

        time.sleep(5)

        # on-demand checkbox
        on_demand_checkbox = browser.find_element_by_xpath("//label[@for='data_product__transfer_frequency_ids-10']")
        on_demand_checkbox.click()

        time.sleep(5)

        # 7. Pricing
        pricing_button = browser.find_element_by_xpath("//a[@data-tab='pricing']")
        pricing_button.click()

        time.sleep(5)

        # One-off purchase checkbox
        one_off_purchase_checkbox = browser.find_element_by_xpath(
            "//label[@for='data_product_pricing_plan__pricing_model_id-1']"
        )
        one_off_purchase_checkbox.click()

        time.sleep(5)

        # starts at one-off purchase input
        starts_at_one_off_purchase_input = browser.find_element_by_xpath(
            "//input[@id='data_product_pricing_plan__starts_at_price']"
        )
        starts_at_one_off_purchase_input.clear()
        starts_at_one_off_purchase_input.send_keys(str(price))

        time.sleep(5)

        currency_select = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[9]/div/div[2]/div[2]/div"
        )
        currency_select.click()

        time.sleep(5)

        eur_select = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[9]/div/div[2]/div[2]/div/div[2]/div[2]"
        )
        eur_select.click()

        time.sleep(5)

    # ok
    def test_push_one_product_for_b2b_contact_data_for_montserrat(self):
        print("test_push_one_product_for_b2b_contact_data_for_montserrat")

        number_of_records = 108

        indicatif_telephonique = "(+1664) xxx xxxxxx"

        price = "0.99"

        pays = "Montserrat"

        region = "Montserrat"

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(5)

        # with Firefox
        browser = webdriver.Firefox(executable_path='..\\geckodriver.exe')

        time.sleep(20)

        # maximize window
        browser.maximize_window()

        time.sleep(10)

        # open
        browser.get('https://datarade.ai/')

        time.sleep(15)

        clear_button = browser.find_element_by_xpath("//button[@data-cf-action='reject'][@aria-label='Deny']")
        clear_button.click()

        time.sleep(5)

        sign_in_button = browser.find_element_by_xpath("//a[@class='navbar__item'][@href='/users/sign_in']")
        sign_in_button.click()

        time.sleep(15)

        work_email_input = browser.find_element_by_xpath("//input[@id='user__email'][@name='user[email]']")
        work_email_input.clear()
        work_email_input.send_keys(""
        "")

        time.sleep(5)

        passwrod_input = browser.find_element_by_xpath("//input[@id='user__password'][@name='user[password]']")
        passwrod_input.clear()
        passwrod_input.send_keys("")

        time.sleep(5)

        login_button = browser.find_element_by_xpath("//input[@type='submit'][@name='commit']")
        login_button.click()

        time.sleep(15)

        holomorphe_button = browser.find_element_by_xpath(
            "//a[@class='navbar__item tablet-landscape-hidden'][@href='/my/provider']")
        holomorphe_button.click()

        time.sleep(10)

        new_product_button = browser.find_element_by_xpath(
            "//a[@class='button primary modern small'][@href='/my/provider/data_products/new']")
        new_product_button.click()

        time.sleep(10)

        # 1.Basics
        # Title
        title_input = browser.find_element_by_xpath("//input[@id='data_product__name'][@name='data_product[name]']")
        title_input.clear()

        title = "Holomorphe / B2B Contact Data / Private Company data / " + pays

        title_input.send_keys(title)

        time.sleep(5)

        # Short Description
        short_description_input = browser.find_element_by_xpath(
            "//textarea[@id='data_product__short_description'][@name='data_product[short_description]']")
        short_description_input.clear()

        short_description = "The key benefits of this data product are : valuable, affordable and reliable. " \
                            "The main attributes of this data product are : company name, postal address, " \
                            "phone number, website, email, region, activity and country. " \
                            "The coverage of this data product is : " + pays + "."

        short_description_input.send_keys(short_description)

        time.sleep(5)

        # In-depth Description
        in_depth_description_input = browser.find_element_by_xpath(
            "//textarea[@id='data_product__description'][@name='data_product[description]']")
        in_depth_description_input.clear()

        in_depth_description = "This data product is efficient because the work for this data collection was " \
                               "made by a complex algorithm that uses artificial intelligence to operate. " \
                               "The data was generally sourced from the web. The primary use-cases or verticals of " \
                               "this data product are : direct marketing, digital marketing, email marketing, " \
                               "phone marketing, voice over ip marketing, business strategy, business intelligence, " \
                               "customer segmentation, customer location and activity segmentation. The activities " \
                               "of B2B contact data are : employment agencies, real estate agencies, recruitment " \
                               "agencies, software, hotel, social, cleaning, charity, financial, restaurant, " \
                               "building, hairdresser, florist, locksmith, bakery, insurance, pharmacy, mover, " \
                               "electricity, plumbing, security, attorney, bank, garage, dentist, doctor, " \
                               "accountant, grocery, notary, jewellery, tailor, butcher, library, architect, cement, " \
                               "heating, boat, cold, steel, chemical, gas and gold."

        in_depth_description_input.send_keys(in_depth_description)

        time.sleep(5)

        # 2.Listing
        listing_button = browser.find_element_by_xpath("//a[@data-tab='listing']")
        listing_button.click()

        time.sleep(5)

        data_catgory_1_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[1]/div/div"
        )
        data_catgory_1_select.click()

        time.sleep(5)

        data_catgory_1_value_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[1]/div/div/div[2]/div[4]"
        )
        data_catgory_1_value_select.click()

        time.sleep(5)

        data_catgory_2_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[2]/div/div"
        )
        data_catgory_2_select.click()

        time.sleep(5)

        data_catgory_2_value_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[2]/div/div/div[2]/div[6]"
        )
        data_catgory_2_value_select.click()

        time.sleep(5)

        data_catgory_3_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[3]/div/div"
        )
        data_catgory_3_select.click()

        time.sleep(5)

        data_catgory_3_value_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[3]/div/div/div[2]/div[15]"
        )
        data_catgory_3_value_select.click()

        time.sleep(5)

        data_catgory_4_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[4]/div/div"
        )
        data_catgory_4_select.click()

        time.sleep(5)

        data_catgory_4_value_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[4]/div/div/div[2]/div[20]"
        )
        data_catgory_4_value_select.click()

        time.sleep(5)

        data_catgory_5_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[5]/div/div"
        )
        data_catgory_5_select.click()

        time.sleep(5)

        data_catgory_5_value_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[5]/div/div/div[2]/div[34]"
        )
        data_catgory_5_value_select.click()

        time.sleep(5)

        # check the Small Business checkbox
        small_business_checkbox = browser.find_element_by_xpath(
            "//label[@for='data_product__company_size_ids-1']"
        )
        small_business_checkbox.click()

        time.sleep(5)

        # check the Medium-sized Business checkbox
        medium_sized_business_checkbox = browser.find_element_by_xpath(
            "//label[@for='data_product__company_size_ids-2']"
        )
        medium_sized_business_checkbox.click()

        time.sleep(5)

        # check the Entreprise checkbox
        entreprise_checkbox = browser.find_element_by_xpath(
            "//label[@for='data_product__company_size_ids-3']"
        )
        entreprise_checkbox.click()

        time.sleep(5)

        use_cases_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]"
        )
        use_cases_select.click()

        time.sleep(5)

        use_case_1_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[33]"
        )
        use_case_1_select.click()

        time.sleep(5)

        use_cases_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]"
        )
        use_cases_select.click()

        time.sleep(5)

        use_case_2_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[37]"
        )
        use_case_2_select.click()

        time.sleep(5)

        use_cases_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]"
        )
        use_cases_select.click()

        time.sleep(5)

        use_case_3_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[122]"
        )
        use_case_3_select.click()

        time.sleep(5)

        use_cases_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]"
        )
        use_cases_select.click()

        time.sleep(5)

        use_case_4_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[135]"
        )
        use_case_4_select.click()

        time.sleep(5)

        use_cases_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]"
        )
        use_cases_select.click()

        time.sleep(5)

        use_case_5_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[139]"
        )
        use_case_5_select.click()

        time.sleep(5)

        # 3. Coverage by myself
        coverage_button = browser.find_element_by_xpath("//a[@data-tab='coverage']")
        coverage_button.click()

        time.sleep(5)

        # Historical Coverage
        historical_coverage_input = browser.find_element_by_xpath(
            '//input[@id="data_product__history"]'
        )
        historical_coverage_input.clear()
        historical_coverage_input.send_keys("1")

        time.sleep(5)

        range_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[5]/div/div[2]/div[3]/div[2]/div"
        )
        range_select.click()

        time.sleep(5)

        weeks_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[5]/div/div[2]/div[3]/div[2]/div/div[2]/div[2]"
        )
        weeks_select.click()

        time.sleep(5)

        # 4. Volume and quality
        volume_and_quality_button = browser.find_element_by_xpath("//a[@data-tab='volume_and_quality']")
        volume_and_quality_button.click()

        time.sleep(5)

        # Add Volume
        add_volume_button = browser.find_element_by_xpath("//a[@data-association='volume']")
        add_volume_button.click()

        time.sleep(5)

        # Volume input
        volume_input = browser.find_element_by_xpath("//input[@id='data_product_volume__value'][@type='number']")
        volume_input.clear()
        volume_input.send_keys(str(number_of_records))

        time.sleep(5)

        # unit_input
        unit_input = browser.find_element_by_xpath("//input[@id='data_product_volume__unit'][@type='text']")
        unit_input.clear()
        unit_input.send_keys("records")

        time.sleep(5)

        # Add Quality Attribute
        add_quality_attribute_button = browser.find_element_by_xpath("//a[@data-association='quality']")
        add_quality_attribute_button.click()

        time.sleep(5)

        # quality in % input
        quality_input = browser.find_element_by_xpath("//input[@id='data_product_quality__percentage'][@type='number']")
        quality_input.clear()
        quality_input.send_keys("80")

        time.sleep(5)

        # unit quality input
        unit_quality_input = browser.find_element_by_xpath("//input[@id='data_product_quality__unit'][@type='text']")
        unit_quality_input.clear()
        unit_quality_input.send_keys("match rate")

        time.sleep(5)

        # 5. Attributes
        attributes_button = browser.find_element_by_xpath("//a[@data-tab='attributes']")
        attributes_button.click()

        time.sleep(5)

        # Add Attribute _ company_name
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(5)

        # name input
        name_input = browser.find_element_by_xpath(
            "//input[@id='data_product_attribute_spec__name']"
        )
        name_input.clear()
        name_input.send_keys("company_name")

        time.sleep(5)

        # example input
        example_input = browser.find_element_by_xpath(
            "//input[@id='data_product_attribute_spec__example']"
        )
        example_input.clear()
        example_input.send_keys("Company A")

        time.sleep(5)

        # description input
        description_input = browser.find_element_by_xpath(
            "//input[@id='data_product_attribute_spec__description']"
        )
        description_input.clear()
        description_input.send_keys("A company name")

        time.sleep(5)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "//input[@id='data_product_attribute_spec__number_of_records']"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(5)

        # Add Attribute _ postal_address
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # postal_address input
        postal_address_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[2]/td[2]/div/input"
        )
        postal_address_input.clear()
        postal_address_input.send_keys("postal_address")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[2]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys("1 Street postal address XXX Country")

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[2]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("A postal address")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[2]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ phone_number
        add_attribute_button = browser.find_element_by_xpath(
            "//a[@data-association='attribute_spec']"
        )
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[3]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("phone_number")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[3]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys(str(indicatif_telephonique))

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[3]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("A phone number of the company")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[3]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ website
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[4]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("website")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[4]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys("https://example.example")

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[4]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("A website of the company")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[4]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ email
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[5]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("email")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[5]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys("example@example.example")

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[5]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("An email address of the company")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[5]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ region
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[6]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("region")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[6]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys(str(region))

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[6]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("A region name")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[6]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ activity
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[7]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("activity")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[7]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys("Bank")

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[7]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("An activity")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[7]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ country
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[8]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("country")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[8]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys(str(pays))

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[8]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("A country")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[8]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # 6. Delivery
        delivery_button = browser.find_element_by_xpath("//a[@class='item'][@data-tab='delivery']")
        delivery_button.click()

        time.sleep(5)

        # Email checkbox
        email_checkbox = browser.find_element_by_xpath("//label[@for='data_product__transfer_method_ids-9']")
        email_checkbox.click()

        time.sleep(5)

        # Json checkbox
        json_checkbox = browser.find_element_by_xpath("//label[@for='data_product__data_format_ids-10']")
        json_checkbox.click()

        time.sleep(5)

        #  csv checkbox
        csv_checkbox = browser.find_element_by_xpath("//label[@for='data_product__data_format_ids-12']")
        csv_checkbox.click()

        time.sleep(5)

        # xls checkbox
        xls_checkbox = browser.find_element_by_xpath("//label[@for='data_product__data_format_ids-13']")
        xls_checkbox.click()

        time.sleep(5)

        # sql checkbox
        sql_checkbox = browser.find_element_by_xpath("//label[@for='data_product__data_format_ids-14']")
        sql_checkbox.click()

        time.sleep(5)

        # on-demand checkbox
        on_demand_checkbox = browser.find_element_by_xpath("//label[@for='data_product__transfer_frequency_ids-10']")
        on_demand_checkbox.click()

        time.sleep(5)

        # 7. Pricing
        pricing_button = browser.find_element_by_xpath("//a[@data-tab='pricing']")
        pricing_button.click()

        time.sleep(5)

        # One-off purchase checkbox
        one_off_purchase_checkbox = browser.find_element_by_xpath(
            "//label[@for='data_product_pricing_plan__pricing_model_id-1']"
        )
        one_off_purchase_checkbox.click()

        time.sleep(5)

        # starts at one-off purchase input
        starts_at_one_off_purchase_input = browser.find_element_by_xpath(
            "//input[@id='data_product_pricing_plan__starts_at_price']"
        )
        starts_at_one_off_purchase_input.clear()
        starts_at_one_off_purchase_input.send_keys(str(price))

        time.sleep(5)

        currency_select = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[9]/div/div[2]/div[2]/div"
        )
        currency_select.click()

        time.sleep(5)

        eur_select = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[9]/div/div[2]/div[2]/div/div[2]/div[2]"
        )
        eur_select.click()

        time.sleep(5)

    # ok
    def test_push_one_product_for_b2b_contact_data_for_trinidad(self):
        print("test_push_one_product_for_b2b_contact_data_for_trinidad")

        number_of_records = 2855

        indicatif_telephonique = "(+1868) xxx xxxxxx"

        price = "1.99"

        pays = "Trinidad and Tobago"

        region = "Trinidad and Tobago"

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(5)

        # with Firefox
        browser = webdriver.Firefox(executable_path='..\\geckodriver.exe')

        time.sleep(20)

        # maximize window
        browser.maximize_window()

        time.sleep(10)

        # open
        browser.get('https://datarade.ai/')

        time.sleep(15)

        clear_button = browser.find_element_by_xpath("//button[@data-cf-action='reject'][@aria-label='Deny']")
        clear_button.click()

        time.sleep(5)

        sign_in_button = browser.find_element_by_xpath("//a[@class='navbar__item'][@href='/users/sign_in']")
        sign_in_button.click()

        time.sleep(15)

        work_email_input = browser.find_element_by_xpath("//input[@id='user__email'][@name='user[email]']")
        work_email_input.clear()
        work_email_input.send_keys(""
        "")

        time.sleep(5)

        passwrod_input = browser.find_element_by_xpath("//input[@id='user__password'][@name='user[password]']")
        passwrod_input.clear()
        passwrod_input.send_keys("")

        time.sleep(5)

        login_button = browser.find_element_by_xpath("//input[@type='submit'][@name='commit']")
        login_button.click()

        time.sleep(15)

        holomorphe_button = browser.find_element_by_xpath(
            "//a[@class='navbar__item tablet-landscape-hidden'][@href='/my/provider']")
        holomorphe_button.click()

        time.sleep(10)

        new_product_button = browser.find_element_by_xpath(
            "//a[@class='button primary modern small'][@href='/my/provider/data_products/new']")
        new_product_button.click()

        time.sleep(10)

        # 1.Basics
        # Title
        title_input = browser.find_element_by_xpath("//input[@id='data_product__name'][@name='data_product[name]']")
        title_input.clear()

        title = "Holomorphe / B2B Contact Data / Private Company data / " + pays

        title_input.send_keys(title)

        time.sleep(5)

        # Short Description
        short_description_input = browser.find_element_by_xpath(
            "//textarea[@id='data_product__short_description'][@name='data_product[short_description]']")
        short_description_input.clear()

        short_description = "The key benefits of this data product are : valuable, affordable and reliable. " \
                            "The main attributes of this data product are : company name, postal address, " \
                            "phone number, website, email, region, activity and country. " \
                            "The coverage of this data product is : " + pays + "."

        short_description_input.send_keys(short_description)

        time.sleep(5)

        # In-depth Description
        in_depth_description_input = browser.find_element_by_xpath(
            "//textarea[@id='data_product__description'][@name='data_product[description]']")
        in_depth_description_input.clear()

        in_depth_description = "This data product is efficient because the work for this data collection was " \
                               "made by a complex algorithm that uses artificial intelligence to operate. " \
                               "The data was generally sourced from the web. The primary use-cases or verticals of " \
                               "this data product are : direct marketing, digital marketing, email marketing, " \
                               "phone marketing, voice over ip marketing, business strategy, business intelligence, " \
                               "customer segmentation, customer location and activity segmentation. The activities " \
                               "of B2B contact data are : employment agencies, real estate agencies, recruitment " \
                               "agencies, software, hotel, social, cleaning, charity, financial, restaurant, " \
                               "building, hairdresser, florist, locksmith, bakery, insurance, pharmacy, mover, " \
                               "electricity, plumbing, security, attorney, bank, garage, dentist, doctor, " \
                               "accountant, grocery, notary, jewellery, tailor, butcher, library, architect, cement, " \
                               "heating, boat, cold, steel, chemical, gas and gold."

        in_depth_description_input.send_keys(in_depth_description)

        time.sleep(5)

        # 2.Listing
        listing_button = browser.find_element_by_xpath("//a[@data-tab='listing']")
        listing_button.click()

        time.sleep(5)

        data_catgory_1_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[1]/div/div"
        )
        data_catgory_1_select.click()

        time.sleep(5)

        data_catgory_1_value_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[1]/div/div/div[2]/div[4]"
        )
        data_catgory_1_value_select.click()

        time.sleep(5)

        data_catgory_2_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[2]/div/div"
        )
        data_catgory_2_select.click()

        time.sleep(5)

        data_catgory_2_value_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[2]/div/div/div[2]/div[6]"
        )
        data_catgory_2_value_select.click()

        time.sleep(5)

        data_catgory_3_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[3]/div/div"
        )
        data_catgory_3_select.click()

        time.sleep(5)

        data_catgory_3_value_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[3]/div/div/div[2]/div[15]"
        )
        data_catgory_3_value_select.click()

        time.sleep(5)

        data_catgory_4_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[4]/div/div"
        )
        data_catgory_4_select.click()

        time.sleep(5)

        data_catgory_4_value_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[4]/div/div/div[2]/div[20]"
        )
        data_catgory_4_value_select.click()

        time.sleep(5)

        data_catgory_5_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[5]/div/div"
        )
        data_catgory_5_select.click()

        time.sleep(5)

        data_catgory_5_value_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[5]/div/div/div[2]/div[34]"
        )
        data_catgory_5_value_select.click()

        time.sleep(5)

        # check the Small Business checkbox
        small_business_checkbox = browser.find_element_by_xpath(
            "//label[@for='data_product__company_size_ids-1']"
        )
        small_business_checkbox.click()

        time.sleep(5)

        # check the Medium-sized Business checkbox
        medium_sized_business_checkbox = browser.find_element_by_xpath(
            "//label[@for='data_product__company_size_ids-2']"
        )
        medium_sized_business_checkbox.click()

        time.sleep(5)

        # check the Entreprise checkbox
        entreprise_checkbox = browser.find_element_by_xpath(
            "//label[@for='data_product__company_size_ids-3']"
        )
        entreprise_checkbox.click()

        time.sleep(5)

        use_cases_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]"
        )
        use_cases_select.click()

        time.sleep(5)

        use_case_1_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[33]"
        )
        use_case_1_select.click()

        time.sleep(5)

        use_cases_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]"
        )
        use_cases_select.click()

        time.sleep(5)

        use_case_2_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[37]"
        )
        use_case_2_select.click()

        time.sleep(5)

        use_cases_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]"
        )
        use_cases_select.click()

        time.sleep(5)

        use_case_3_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[122]"
        )
        use_case_3_select.click()

        time.sleep(5)

        use_cases_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]"
        )
        use_cases_select.click()

        time.sleep(5)

        use_case_4_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[135]"
        )
        use_case_4_select.click()

        time.sleep(5)

        use_cases_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]"
        )
        use_cases_select.click()

        time.sleep(5)

        use_case_5_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[139]"
        )
        use_case_5_select.click()

        time.sleep(5)

        # 3. Coverage by myself
        coverage_button = browser.find_element_by_xpath("//a[@data-tab='coverage']")
        coverage_button.click()

        time.sleep(5)

        # Historical Coverage
        historical_coverage_input = browser.find_element_by_xpath(
            '//input[@id="data_product__history"]'
        )
        historical_coverage_input.clear()
        historical_coverage_input.send_keys("1")

        time.sleep(5)

        range_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[5]/div/div[2]/div[3]/div[2]/div"
        )
        range_select.click()

        time.sleep(5)

        weeks_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[5]/div/div[2]/div[3]/div[2]/div/div[2]/div[2]"
        )
        weeks_select.click()

        time.sleep(5)

        # 4. Volume and quality
        volume_and_quality_button = browser.find_element_by_xpath("//a[@data-tab='volume_and_quality']")
        volume_and_quality_button.click()

        time.sleep(5)

        # Add Volume
        add_volume_button = browser.find_element_by_xpath("//a[@data-association='volume']")
        add_volume_button.click()

        time.sleep(5)

        # Volume input
        volume_input = browser.find_element_by_xpath("//input[@id='data_product_volume__value'][@type='number']")
        volume_input.clear()
        volume_input.send_keys(str(number_of_records))

        time.sleep(5)

        # unit_input
        unit_input = browser.find_element_by_xpath("//input[@id='data_product_volume__unit'][@type='text']")
        unit_input.clear()
        unit_input.send_keys("records")

        time.sleep(5)

        # Add Quality Attribute
        add_quality_attribute_button = browser.find_element_by_xpath("//a[@data-association='quality']")
        add_quality_attribute_button.click()

        time.sleep(5)

        # quality in % input
        quality_input = browser.find_element_by_xpath("//input[@id='data_product_quality__percentage'][@type='number']")
        quality_input.clear()
        quality_input.send_keys("80")

        time.sleep(5)

        # unit quality input
        unit_quality_input = browser.find_element_by_xpath("//input[@id='data_product_quality__unit'][@type='text']")
        unit_quality_input.clear()
        unit_quality_input.send_keys("match rate")

        time.sleep(5)

        # 5. Attributes
        attributes_button = browser.find_element_by_xpath("//a[@data-tab='attributes']")
        attributes_button.click()

        time.sleep(5)

        # Add Attribute _ company_name
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(5)

        # name input
        name_input = browser.find_element_by_xpath(
            "//input[@id='data_product_attribute_spec__name']"
        )
        name_input.clear()
        name_input.send_keys("company_name")

        time.sleep(5)

        # example input
        example_input = browser.find_element_by_xpath(
            "//input[@id='data_product_attribute_spec__example']"
        )
        example_input.clear()
        example_input.send_keys("Company A")

        time.sleep(5)

        # description input
        description_input = browser.find_element_by_xpath(
            "//input[@id='data_product_attribute_spec__description']"
        )
        description_input.clear()
        description_input.send_keys("A company name")

        time.sleep(5)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "//input[@id='data_product_attribute_spec__number_of_records']"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(5)

        # Add Attribute _ postal_address
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # postal_address input
        postal_address_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[2]/td[2]/div/input"
        )
        postal_address_input.clear()
        postal_address_input.send_keys("postal_address")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[2]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys("1 Street postal address XXX Country")

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[2]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("A postal address")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[2]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ phone_number
        add_attribute_button = browser.find_element_by_xpath(
            "//a[@data-association='attribute_spec']"
        )
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[3]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("phone_number")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[3]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys(str(indicatif_telephonique))

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[3]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("A phone number of the company")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[3]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ website
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[4]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("website")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[4]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys("https://example.example")

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[4]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("A website of the company")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[4]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ email
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[5]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("email")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[5]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys("example@example.example")

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[5]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("An email address of the company")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[5]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ region
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[6]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("region")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[6]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys(str(region))

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[6]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("A region name")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[6]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ activity
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[7]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("activity")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[7]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys("Bank")

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[7]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("An activity")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[7]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ country
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[8]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("country")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[8]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys(str(pays))

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[8]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("A country")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[8]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # 6. Delivery
        delivery_button = browser.find_element_by_xpath("//a[@class='item'][@data-tab='delivery']")
        delivery_button.click()

        time.sleep(5)

        # Email checkbox
        email_checkbox = browser.find_element_by_xpath("//label[@for='data_product__transfer_method_ids-9']")
        email_checkbox.click()

        time.sleep(5)

        # Json checkbox
        json_checkbox = browser.find_element_by_xpath("//label[@for='data_product__data_format_ids-10']")
        json_checkbox.click()

        time.sleep(5)

        #  csv checkbox
        csv_checkbox = browser.find_element_by_xpath("//label[@for='data_product__data_format_ids-12']")
        csv_checkbox.click()

        time.sleep(5)

        # xls checkbox
        xls_checkbox = browser.find_element_by_xpath("//label[@for='data_product__data_format_ids-13']")
        xls_checkbox.click()

        time.sleep(5)

        # sql checkbox
        sql_checkbox = browser.find_element_by_xpath("//label[@for='data_product__data_format_ids-14']")
        sql_checkbox.click()

        time.sleep(5)

        # on-demand checkbox
        on_demand_checkbox = browser.find_element_by_xpath("//label[@for='data_product__transfer_frequency_ids-10']")
        on_demand_checkbox.click()

        time.sleep(5)

        # 7. Pricing
        pricing_button = browser.find_element_by_xpath("//a[@data-tab='pricing']")
        pricing_button.click()

        time.sleep(5)

        # One-off purchase checkbox
        one_off_purchase_checkbox = browser.find_element_by_xpath(
            "//label[@for='data_product_pricing_plan__pricing_model_id-1']"
        )
        one_off_purchase_checkbox.click()

        time.sleep(5)

        # starts at one-off purchase input
        starts_at_one_off_purchase_input = browser.find_element_by_xpath(
            "//input[@id='data_product_pricing_plan__starts_at_price']"
        )
        starts_at_one_off_purchase_input.clear()
        starts_at_one_off_purchase_input.send_keys(str(price))

        time.sleep(5)

        currency_select = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[9]/div/div[2]/div[2]/div"
        )
        currency_select.click()

        time.sleep(5)

        eur_select = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[9]/div/div[2]/div[2]/div/div[2]/div[2]"
        )
        eur_select.click()

        time.sleep(5)

    # ok
    def test_push_one_product_for_b2b_contact_data_for_saint_lucia(self):
        print("test_push_one_product_for_b2b_contact_data_for_saint_lucia")

        number_of_records = 1236

        indicatif_telephonique = "(+1758) xxx xxxxxx"

        price = "1.99"

        pays = "Saint-Lucia"

        region = "Saint-Lucia"

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(5)

        # with Firefox
        browser = webdriver.Firefox(executable_path='..\\geckodriver.exe')

        time.sleep(20)

        # maximize window
        browser.maximize_window()

        time.sleep(10)

        # open
        browser.get('https://datarade.ai/')

        time.sleep(15)

        clear_button = browser.find_element_by_xpath("//button[@data-cf-action='reject'][@aria-label='Deny']")
        clear_button.click()

        time.sleep(5)

        sign_in_button = browser.find_element_by_xpath("//a[@class='navbar__item'][@href='/users/sign_in']")
        sign_in_button.click()

        time.sleep(15)

        work_email_input = browser.find_element_by_xpath("//input[@id='user__email'][@name='user[email]']")
        work_email_input.clear()
        work_email_input.send_keys(""
        "")

        time.sleep(5)

        passwrod_input = browser.find_element_by_xpath("//input[@id='user__password'][@name='user[password]']")
        passwrod_input.clear()
        passwrod_input.send_keys("")

        time.sleep(5)

        login_button = browser.find_element_by_xpath("//input[@type='submit'][@name='commit']")
        login_button.click()

        time.sleep(15)

        holomorphe_button = browser.find_element_by_xpath(
            "//a[@class='navbar__item tablet-landscape-hidden'][@href='/my/provider']")
        holomorphe_button.click()

        time.sleep(10)

        new_product_button = browser.find_element_by_xpath(
            "//a[@class='button primary modern small'][@href='/my/provider/data_products/new']")
        new_product_button.click()

        time.sleep(10)

        # 1.Basics
        # Title
        title_input = browser.find_element_by_xpath("//input[@id='data_product__name'][@name='data_product[name]']")
        title_input.clear()

        title = "Holomorphe / B2B Contact Data / Private Company data / " + pays

        title_input.send_keys(title)

        time.sleep(5)

        # Short Description
        short_description_input = browser.find_element_by_xpath(
            "//textarea[@id='data_product__short_description'][@name='data_product[short_description]']")
        short_description_input.clear()

        short_description = "The key benefits of this data product are : valuable, affordable and reliable. " \
                            "The main attributes of this data product are : company name, postal address, " \
                            "phone number, website, email, region, activity and country. " \
                            "The coverage of this data product is : " + pays + "."

        short_description_input.send_keys(short_description)

        time.sleep(5)

        # In-depth Description
        in_depth_description_input = browser.find_element_by_xpath(
            "//textarea[@id='data_product__description'][@name='data_product[description]']")
        in_depth_description_input.clear()

        in_depth_description = "This data product is efficient because the work for this data collection was " \
                               "made by a complex algorithm that uses artificial intelligence to operate. " \
                               "The data was generally sourced from the web. The primary use-cases or verticals of " \
                               "this data product are : direct marketing, digital marketing, email marketing, " \
                               "phone marketing, voice over ip marketing, business strategy, business intelligence, " \
                               "customer segmentation, customer location and activity segmentation. The activities " \
                               "of B2B contact data are : employment agencies, real estate agencies, recruitment " \
                               "agencies, software, hotel, social, cleaning, charity, financial, restaurant, " \
                               "building, hairdresser, florist, locksmith, bakery, insurance, pharmacy, mover, " \
                               "electricity, plumbing, security, attorney, bank, garage, dentist, doctor, " \
                               "accountant, grocery, notary, jewellery, tailor, butcher, library, architect, cement, " \
                               "heating, boat, cold, steel, chemical, gas and gold."

        in_depth_description_input.send_keys(in_depth_description)

        time.sleep(5)

        # 2.Listing
        listing_button = browser.find_element_by_xpath("//a[@data-tab='listing']")
        listing_button.click()

        time.sleep(5)

        data_catgory_1_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[1]/div/div"
        )
        data_catgory_1_select.click()

        time.sleep(5)

        data_catgory_1_value_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[1]/div/div/div[2]/div[4]"
        )
        data_catgory_1_value_select.click()

        time.sleep(5)

        data_catgory_2_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[2]/div/div"
        )
        data_catgory_2_select.click()

        time.sleep(5)

        data_catgory_2_value_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[2]/div/div/div[2]/div[6]"
        )
        data_catgory_2_value_select.click()

        time.sleep(5)

        data_catgory_3_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[3]/div/div"
        )
        data_catgory_3_select.click()

        time.sleep(5)

        data_catgory_3_value_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[3]/div/div/div[2]/div[15]"
        )
        data_catgory_3_value_select.click()

        time.sleep(5)

        data_catgory_4_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[4]/div/div"
        )
        data_catgory_4_select.click()

        time.sleep(5)

        data_catgory_4_value_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[4]/div/div/div[2]/div[20]"
        )
        data_catgory_4_value_select.click()

        time.sleep(5)

        data_catgory_5_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[5]/div/div"
        )
        data_catgory_5_select.click()

        time.sleep(5)

        data_catgory_5_value_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[5]/div/div/div[2]/div[34]"
        )
        data_catgory_5_value_select.click()

        time.sleep(5)

        # check the Small Business checkbox
        small_business_checkbox = browser.find_element_by_xpath(
            "//label[@for='data_product__company_size_ids-1']"
        )
        small_business_checkbox.click()

        time.sleep(5)

        # check the Medium-sized Business checkbox
        medium_sized_business_checkbox = browser.find_element_by_xpath(
            "//label[@for='data_product__company_size_ids-2']"
        )
        medium_sized_business_checkbox.click()

        time.sleep(5)

        # check the Entreprise checkbox
        entreprise_checkbox = browser.find_element_by_xpath(
            "//label[@for='data_product__company_size_ids-3']"
        )
        entreprise_checkbox.click()

        time.sleep(5)

        use_cases_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]"
        )
        use_cases_select.click()

        time.sleep(5)

        use_case_1_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[33]"
        )
        use_case_1_select.click()

        time.sleep(5)

        use_cases_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]"
        )
        use_cases_select.click()

        time.sleep(5)

        use_case_2_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[37]"
        )
        use_case_2_select.click()

        time.sleep(5)

        use_cases_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]"
        )
        use_cases_select.click()

        time.sleep(5)

        use_case_3_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[122]"
        )
        use_case_3_select.click()

        time.sleep(5)

        use_cases_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]"
        )
        use_cases_select.click()

        time.sleep(5)

        use_case_4_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[135]"
        )
        use_case_4_select.click()

        time.sleep(5)

        use_cases_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]"
        )
        use_cases_select.click()

        time.sleep(5)

        use_case_5_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[139]"
        )
        use_case_5_select.click()

        time.sleep(5)

        # 3. Coverage by myself
        coverage_button = browser.find_element_by_xpath("//a[@data-tab='coverage']")
        coverage_button.click()

        time.sleep(5)

        # Historical Coverage
        historical_coverage_input = browser.find_element_by_xpath(
            '//input[@id="data_product__history"]'
        )
        historical_coverage_input.clear()
        historical_coverage_input.send_keys("1")

        time.sleep(5)

        range_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[5]/div/div[2]/div[3]/div[2]/div"
        )
        range_select.click()

        time.sleep(5)

        weeks_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[5]/div/div[2]/div[3]/div[2]/div/div[2]/div[2]"
        )
        weeks_select.click()

        time.sleep(5)

        # 4. Volume and quality
        volume_and_quality_button = browser.find_element_by_xpath("//a[@data-tab='volume_and_quality']")
        volume_and_quality_button.click()

        time.sleep(5)

        # Add Volume
        add_volume_button = browser.find_element_by_xpath("//a[@data-association='volume']")
        add_volume_button.click()

        time.sleep(5)

        # Volume input
        volume_input = browser.find_element_by_xpath("//input[@id='data_product_volume__value'][@type='number']")
        volume_input.clear()
        volume_input.send_keys(str(number_of_records))

        time.sleep(5)

        # unit_input
        unit_input = browser.find_element_by_xpath("//input[@id='data_product_volume__unit'][@type='text']")
        unit_input.clear()
        unit_input.send_keys("records")

        time.sleep(5)

        # Add Quality Attribute
        add_quality_attribute_button = browser.find_element_by_xpath("//a[@data-association='quality']")
        add_quality_attribute_button.click()

        time.sleep(5)

        # quality in % input
        quality_input = browser.find_element_by_xpath("//input[@id='data_product_quality__percentage'][@type='number']")
        quality_input.clear()
        quality_input.send_keys("80")

        time.sleep(5)

        # unit quality input
        unit_quality_input = browser.find_element_by_xpath("//input[@id='data_product_quality__unit'][@type='text']")
        unit_quality_input.clear()
        unit_quality_input.send_keys("match rate")

        time.sleep(5)

        # 5. Attributes
        attributes_button = browser.find_element_by_xpath("//a[@data-tab='attributes']")
        attributes_button.click()

        time.sleep(5)

        # Add Attribute _ company_name
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(5)

        # name input
        name_input = browser.find_element_by_xpath(
            "//input[@id='data_product_attribute_spec__name']"
        )
        name_input.clear()
        name_input.send_keys("company_name")

        time.sleep(5)

        # example input
        example_input = browser.find_element_by_xpath(
            "//input[@id='data_product_attribute_spec__example']"
        )
        example_input.clear()
        example_input.send_keys("Company A")

        time.sleep(5)

        # description input
        description_input = browser.find_element_by_xpath(
            "//input[@id='data_product_attribute_spec__description']"
        )
        description_input.clear()
        description_input.send_keys("A company name")

        time.sleep(5)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "//input[@id='data_product_attribute_spec__number_of_records']"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(5)

        # Add Attribute _ postal_address
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # postal_address input
        postal_address_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[2]/td[2]/div/input"
        )
        postal_address_input.clear()
        postal_address_input.send_keys("postal_address")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[2]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys("1 Street postal address XXX Country")

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[2]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("A postal address")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[2]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ phone_number
        add_attribute_button = browser.find_element_by_xpath(
            "//a[@data-association='attribute_spec']"
        )
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[3]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("phone_number")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[3]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys(str(indicatif_telephonique))

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[3]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("A phone number of the company")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[3]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ website
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[4]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("website")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[4]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys("https://example.example")

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[4]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("A website of the company")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[4]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ email
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[5]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("email")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[5]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys("example@example.example")

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[5]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("An email address of the company")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[5]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ region
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[6]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("region")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[6]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys(str(region))

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[6]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("A region name")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[6]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ activity
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[7]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("activity")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[7]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys("Bank")

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[7]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("An activity")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[7]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ country
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[8]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("country")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[8]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys(str(pays))

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[8]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("A country")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[8]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # 6. Delivery
        delivery_button = browser.find_element_by_xpath("//a[@class='item'][@data-tab='delivery']")
        delivery_button.click()

        time.sleep(5)

        # Email checkbox
        email_checkbox = browser.find_element_by_xpath("//label[@for='data_product__transfer_method_ids-9']")
        email_checkbox.click()

        time.sleep(5)

        # Json checkbox
        json_checkbox = browser.find_element_by_xpath("//label[@for='data_product__data_format_ids-10']")
        json_checkbox.click()

        time.sleep(5)

        #  csv checkbox
        csv_checkbox = browser.find_element_by_xpath("//label[@for='data_product__data_format_ids-12']")
        csv_checkbox.click()

        time.sleep(5)

        # xls checkbox
        xls_checkbox = browser.find_element_by_xpath("//label[@for='data_product__data_format_ids-13']")
        xls_checkbox.click()

        time.sleep(5)

        # sql checkbox
        sql_checkbox = browser.find_element_by_xpath("//label[@for='data_product__data_format_ids-14']")
        sql_checkbox.click()

        time.sleep(5)

        # on-demand checkbox
        on_demand_checkbox = browser.find_element_by_xpath("//label[@for='data_product__transfer_frequency_ids-10']")
        on_demand_checkbox.click()

        time.sleep(5)

        # 7. Pricing
        pricing_button = browser.find_element_by_xpath("//a[@data-tab='pricing']")
        pricing_button.click()

        time.sleep(5)

        # One-off purchase checkbox
        one_off_purchase_checkbox = browser.find_element_by_xpath(
            "//label[@for='data_product_pricing_plan__pricing_model_id-1']"
        )
        one_off_purchase_checkbox.click()

        time.sleep(5)

        # starts at one-off purchase input
        starts_at_one_off_purchase_input = browser.find_element_by_xpath(
            "//input[@id='data_product_pricing_plan__starts_at_price']"
        )
        starts_at_one_off_purchase_input.clear()
        starts_at_one_off_purchase_input.send_keys(str(price))

        time.sleep(5)

        currency_select = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[9]/div/div[2]/div[2]/div"
        )
        currency_select.click()

        time.sleep(5)

        eur_select = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[9]/div/div[2]/div[2]/div/div[2]/div[2]"
        )
        eur_select.click()

        time.sleep(5)

    # ok
    def test_push_one_product_for_b2b_contact_data_for_st_kitts(self):
        print("test_push_one_product_for_b2b_contact_data_for_st_kitts")

        number_of_records = 392

        indicatif_telephonique = "(+1869) xxx xxxxxx"

        price = "1.99"

        pays = "Saint-Kitts"

        region = "Saint-Kitts"

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(5)

        # with Firefox
        browser = webdriver.Firefox(executable_path='..\\geckodriver.exe')

        time.sleep(20)

        # maximize window
        browser.maximize_window()

        time.sleep(10)

        # open
        browser.get('https://datarade.ai/')

        time.sleep(15)

        clear_button = browser.find_element_by_xpath("//button[@data-cf-action='reject'][@aria-label='Deny']")
        clear_button.click()

        time.sleep(5)

        sign_in_button = browser.find_element_by_xpath("//a[@class='navbar__item'][@href='/users/sign_in']")
        sign_in_button.click()

        time.sleep(15)

        work_email_input = browser.find_element_by_xpath("//input[@id='user__email'][@name='user[email]']")
        work_email_input.clear()
        work_email_input.send_keys(""
        "")

        time.sleep(5)

        passwrod_input = browser.find_element_by_xpath("//input[@id='user__password'][@name='user[password]']")
        passwrod_input.clear()
        passwrod_input.send_keys("")

        time.sleep(5)

        login_button = browser.find_element_by_xpath("//input[@type='submit'][@name='commit']")
        login_button.click()

        time.sleep(15)

        holomorphe_button = browser.find_element_by_xpath(
            "//a[@class='navbar__item tablet-landscape-hidden'][@href='/my/provider']")
        holomorphe_button.click()

        time.sleep(10)

        new_product_button = browser.find_element_by_xpath(
            "//a[@class='button primary modern small'][@href='/my/provider/data_products/new']")
        new_product_button.click()

        time.sleep(10)

        # 1.Basics
        # Title
        title_input = browser.find_element_by_xpath("//input[@id='data_product__name'][@name='data_product[name]']")
        title_input.clear()

        title = "Holomorphe / B2B Contact Data / Private Company data / " + pays

        title_input.send_keys(title)

        time.sleep(5)

        # Short Description
        short_description_input = browser.find_element_by_xpath(
            "//textarea[@id='data_product__short_description'][@name='data_product[short_description]']")
        short_description_input.clear()

        short_description = "The key benefits of this data product are : valuable, affordable and reliable. " \
                            "The main attributes of this data product are : company name, postal address, " \
                            "phone number, website, email, region, activity and country. " \
                            "The coverage of this data product is : " + pays + "."

        short_description_input.send_keys(short_description)

        time.sleep(5)

        # In-depth Description
        in_depth_description_input = browser.find_element_by_xpath(
            "//textarea[@id='data_product__description'][@name='data_product[description]']")
        in_depth_description_input.clear()

        in_depth_description = "This data product is efficient because the work for this data collection was " \
                               "made by a complex algorithm that uses artificial intelligence to operate. " \
                               "The data was generally sourced from the web. The primary use-cases or verticals of " \
                               "this data product are : direct marketing, digital marketing, email marketing, " \
                               "phone marketing, voice over ip marketing, business strategy, business intelligence, " \
                               "customer segmentation, customer location and activity segmentation. The activities " \
                               "of B2B contact data are : employment agencies, real estate agencies, recruitment " \
                               "agencies, software, hotel, social, cleaning, charity, financial, restaurant, " \
                               "building, hairdresser, florist, locksmith, bakery, insurance, pharmacy, mover, " \
                               "electricity, plumbing, security, attorney, bank, garage, dentist, doctor, " \
                               "accountant, grocery, notary, jewellery, tailor, butcher, library, architect, cement, " \
                               "heating, boat, cold, steel, chemical, gas and gold."

        in_depth_description_input.send_keys(in_depth_description)

        time.sleep(5)

        # 2.Listing
        listing_button = browser.find_element_by_xpath("//a[@data-tab='listing']")
        listing_button.click()

        time.sleep(5)

        data_catgory_1_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[1]/div/div"
        )
        data_catgory_1_select.click()

        time.sleep(5)

        data_catgory_1_value_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[1]/div/div/div[2]/div[4]"
        )
        data_catgory_1_value_select.click()

        time.sleep(5)

        data_catgory_2_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[2]/div/div"
        )
        data_catgory_2_select.click()

        time.sleep(5)

        data_catgory_2_value_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[2]/div/div/div[2]/div[6]"
        )
        data_catgory_2_value_select.click()

        time.sleep(5)

        data_catgory_3_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[3]/div/div"
        )
        data_catgory_3_select.click()

        time.sleep(5)

        data_catgory_3_value_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[3]/div/div/div[2]/div[15]"
        )
        data_catgory_3_value_select.click()

        time.sleep(5)

        data_catgory_4_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[4]/div/div"
        )
        data_catgory_4_select.click()

        time.sleep(5)

        data_catgory_4_value_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[4]/div/div/div[2]/div[20]"
        )
        data_catgory_4_value_select.click()

        time.sleep(5)

        data_catgory_5_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[5]/div/div"
        )
        data_catgory_5_select.click()

        time.sleep(5)

        data_catgory_5_value_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[5]/div/div/div[2]/div[34]"
        )
        data_catgory_5_value_select.click()

        time.sleep(5)

        # check the Small Business checkbox
        small_business_checkbox = browser.find_element_by_xpath(
            "//label[@for='data_product__company_size_ids-1']"
        )
        small_business_checkbox.click()

        time.sleep(5)

        # check the Medium-sized Business checkbox
        medium_sized_business_checkbox = browser.find_element_by_xpath(
            "//label[@for='data_product__company_size_ids-2']"
        )
        medium_sized_business_checkbox.click()

        time.sleep(5)

        # check the Entreprise checkbox
        entreprise_checkbox = browser.find_element_by_xpath(
            "//label[@for='data_product__company_size_ids-3']"
        )
        entreprise_checkbox.click()

        time.sleep(5)

        use_cases_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]"
        )
        use_cases_select.click()

        time.sleep(5)

        use_case_1_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[33]"
        )
        use_case_1_select.click()

        time.sleep(5)

        use_cases_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]"
        )
        use_cases_select.click()

        time.sleep(5)

        use_case_2_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[37]"
        )
        use_case_2_select.click()

        time.sleep(5)

        use_cases_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]"
        )
        use_cases_select.click()

        time.sleep(5)

        use_case_3_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[122]"
        )
        use_case_3_select.click()

        time.sleep(5)

        use_cases_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]"
        )
        use_cases_select.click()

        time.sleep(5)

        use_case_4_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[135]"
        )
        use_case_4_select.click()

        time.sleep(5)

        use_cases_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]"
        )
        use_cases_select.click()

        time.sleep(5)

        use_case_5_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[139]"
        )
        use_case_5_select.click()

        time.sleep(5)

        # 3. Coverage by myself
        coverage_button = browser.find_element_by_xpath("//a[@data-tab='coverage']")
        coverage_button.click()

        time.sleep(5)

        # Historical Coverage
        historical_coverage_input = browser.find_element_by_xpath(
            '//input[@id="data_product__history"]'
        )
        historical_coverage_input.clear()
        historical_coverage_input.send_keys("1")

        time.sleep(5)

        range_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[5]/div/div[2]/div[3]/div[2]/div"
        )
        range_select.click()

        time.sleep(5)

        weeks_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[5]/div/div[2]/div[3]/div[2]/div/div[2]/div[2]"
        )
        weeks_select.click()

        time.sleep(5)

        # 4. Volume and quality
        volume_and_quality_button = browser.find_element_by_xpath("//a[@data-tab='volume_and_quality']")
        volume_and_quality_button.click()

        time.sleep(5)

        # Add Volume
        add_volume_button = browser.find_element_by_xpath("//a[@data-association='volume']")
        add_volume_button.click()

        time.sleep(5)

        # Volume input
        volume_input = browser.find_element_by_xpath("//input[@id='data_product_volume__value'][@type='number']")
        volume_input.clear()
        volume_input.send_keys(str(number_of_records))

        time.sleep(5)

        # unit_input
        unit_input = browser.find_element_by_xpath("//input[@id='data_product_volume__unit'][@type='text']")
        unit_input.clear()
        unit_input.send_keys("records")

        time.sleep(5)

        # Add Quality Attribute
        add_quality_attribute_button = browser.find_element_by_xpath("//a[@data-association='quality']")
        add_quality_attribute_button.click()

        time.sleep(5)

        # quality in % input
        quality_input = browser.find_element_by_xpath("//input[@id='data_product_quality__percentage'][@type='number']")
        quality_input.clear()
        quality_input.send_keys("80")

        time.sleep(5)

        # unit quality input
        unit_quality_input = browser.find_element_by_xpath("//input[@id='data_product_quality__unit'][@type='text']")
        unit_quality_input.clear()
        unit_quality_input.send_keys("match rate")

        time.sleep(5)

        # 5. Attributes
        attributes_button = browser.find_element_by_xpath("//a[@data-tab='attributes']")
        attributes_button.click()

        time.sleep(5)

        # Add Attribute _ company_name
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(5)

        # name input
        name_input = browser.find_element_by_xpath(
            "//input[@id='data_product_attribute_spec__name']"
        )
        name_input.clear()
        name_input.send_keys("company_name")

        time.sleep(5)

        # example input
        example_input = browser.find_element_by_xpath(
            "//input[@id='data_product_attribute_spec__example']"
        )
        example_input.clear()
        example_input.send_keys("Company A")

        time.sleep(5)

        # description input
        description_input = browser.find_element_by_xpath(
            "//input[@id='data_product_attribute_spec__description']"
        )
        description_input.clear()
        description_input.send_keys("A company name")

        time.sleep(5)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "//input[@id='data_product_attribute_spec__number_of_records']"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(5)

        # Add Attribute _ postal_address
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # postal_address input
        postal_address_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[2]/td[2]/div/input"
        )
        postal_address_input.clear()
        postal_address_input.send_keys("postal_address")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[2]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys("1 Street postal address XXX Country")

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[2]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("A postal address")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[2]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ phone_number
        add_attribute_button = browser.find_element_by_xpath(
            "//a[@data-association='attribute_spec']"
        )
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[3]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("phone_number")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[3]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys(str(indicatif_telephonique))

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[3]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("A phone number of the company")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[3]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ website
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[4]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("website")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[4]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys("https://example.example")

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[4]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("A website of the company")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[4]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ email
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[5]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("email")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[5]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys("example@example.example")

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[5]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("An email address of the company")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[5]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ region
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[6]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("region")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[6]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys(str(region))

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[6]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("A region name")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[6]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ activity
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[7]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("activity")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[7]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys("Bank")

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[7]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("An activity")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[7]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ country
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[8]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("country")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[8]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys(str(pays))

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[8]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("A country")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[8]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # 6. Delivery
        delivery_button = browser.find_element_by_xpath("//a[@class='item'][@data-tab='delivery']")
        delivery_button.click()

        time.sleep(5)

        # Email checkbox
        email_checkbox = browser.find_element_by_xpath("//label[@for='data_product__transfer_method_ids-9']")
        email_checkbox.click()

        time.sleep(5)

        # Json checkbox
        json_checkbox = browser.find_element_by_xpath("//label[@for='data_product__data_format_ids-10']")
        json_checkbox.click()

        time.sleep(5)

        #  csv checkbox
        csv_checkbox = browser.find_element_by_xpath("//label[@for='data_product__data_format_ids-12']")
        csv_checkbox.click()

        time.sleep(5)

        # xls checkbox
        xls_checkbox = browser.find_element_by_xpath("//label[@for='data_product__data_format_ids-13']")
        xls_checkbox.click()

        time.sleep(5)

        # sql checkbox
        sql_checkbox = browser.find_element_by_xpath("//label[@for='data_product__data_format_ids-14']")
        sql_checkbox.click()

        time.sleep(5)

        # on-demand checkbox
        on_demand_checkbox = browser.find_element_by_xpath("//label[@for='data_product__transfer_frequency_ids-10']")
        on_demand_checkbox.click()

        time.sleep(5)

        # 7. Pricing
        pricing_button = browser.find_element_by_xpath("//a[@data-tab='pricing']")
        pricing_button.click()

        time.sleep(5)

        # One-off purchase checkbox
        one_off_purchase_checkbox = browser.find_element_by_xpath(
            "//label[@for='data_product_pricing_plan__pricing_model_id-1']"
        )
        one_off_purchase_checkbox.click()

        time.sleep(5)

        # starts at one-off purchase input
        starts_at_one_off_purchase_input = browser.find_element_by_xpath(
            "//input[@id='data_product_pricing_plan__starts_at_price']"
        )
        starts_at_one_off_purchase_input.clear()
        starts_at_one_off_purchase_input.send_keys(str(price))

        time.sleep(5)

        currency_select = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[9]/div/div[2]/div[2]/div"
        )
        currency_select.click()

        time.sleep(5)

        eur_select = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[9]/div/div[2]/div[2]/div/div[2]/div[2]"
        )
        eur_select.click()

        time.sleep(5)

    # ok
    def test_push_one_product_for_b2b_contact_data_for_jamaica(self):
        print("test_push_one_product_for_b2b_contact_data_for_jamaica")

        number_of_records = 15598

        indicatif_telephonique = "(+1876) xxx xxxxxx"

        price = "1.99"

        pays = "Jamaica"

        region = "Jamaica"

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(5)

        # with Firefox
        browser = webdriver.Firefox(executable_path='..\\geckodriver.exe')

        time.sleep(20)

        # maximize window
        browser.maximize_window()

        time.sleep(10)

        # open
        browser.get('https://datarade.ai/')

        time.sleep(15)

        clear_button = browser.find_element_by_xpath("//button[@data-cf-action='reject'][@aria-label='Deny']")
        clear_button.click()

        time.sleep(5)

        sign_in_button = browser.find_element_by_xpath("//a[@class='navbar__item'][@href='/users/sign_in']")
        sign_in_button.click()

        time.sleep(15)

        work_email_input = browser.find_element_by_xpath("//input[@id='user__email'][@name='user[email]']")
        work_email_input.clear()
        work_email_input.send_keys(""
        "")

        time.sleep(5)

        passwrod_input = browser.find_element_by_xpath("//input[@id='user__password'][@name='user[password]']")
        passwrod_input.clear()
        passwrod_input.send_keys("")

        time.sleep(5)

        login_button = browser.find_element_by_xpath("//input[@type='submit'][@name='commit']")
        login_button.click()

        time.sleep(15)

        holomorphe_button = browser.find_element_by_xpath(
            "//a[@class='navbar__item tablet-landscape-hidden'][@href='/my/provider']")
        holomorphe_button.click()

        time.sleep(10)

        new_product_button = browser.find_element_by_xpath(
            "//a[@class='button primary modern small'][@href='/my/provider/data_products/new']")
        new_product_button.click()

        time.sleep(10)

        # 1.Basics
        # Title
        title_input = browser.find_element_by_xpath("//input[@id='data_product__name'][@name='data_product[name]']")
        title_input.clear()

        title = "Holomorphe / B2B Contact Data / Private Company data / " + pays

        title_input.send_keys(title)

        time.sleep(5)

        # Short Description
        short_description_input = browser.find_element_by_xpath(
            "//textarea[@id='data_product__short_description'][@name='data_product[short_description]']")
        short_description_input.clear()

        short_description = "The key benefits of this data product are : valuable, affordable and reliable. " \
                            "The main attributes of this data product are : company name, postal address, " \
                            "phone number, website, email, region, activity and country. " \
                            "The coverage of this data product is : " + pays + "."

        short_description_input.send_keys(short_description)

        time.sleep(5)

        # In-depth Description
        in_depth_description_input = browser.find_element_by_xpath(
            "//textarea[@id='data_product__description'][@name='data_product[description]']")
        in_depth_description_input.clear()

        in_depth_description = "This data product is efficient because the work for this data collection was " \
                               "made by a complex algorithm that uses artificial intelligence to operate. " \
                               "The data was generally sourced from the web. The primary use-cases or verticals of " \
                               "this data product are : direct marketing, digital marketing, email marketing, " \
                               "phone marketing, voice over ip marketing, business strategy, business intelligence, " \
                               "customer segmentation, customer location and activity segmentation. The activities " \
                               "of B2B contact data are : employment agencies, real estate agencies, recruitment " \
                               "agencies, software, hotel, social, cleaning, charity, financial, restaurant, " \
                               "building, hairdresser, florist, locksmith, bakery, insurance, pharmacy, mover, " \
                               "electricity, plumbing, security, attorney, bank, garage, dentist, doctor, " \
                               "accountant, grocery, notary, jewellery, tailor, butcher, library, architect, cement, " \
                               "heating, boat, cold, steel, chemical, gas and gold."

        in_depth_description_input.send_keys(in_depth_description)

        time.sleep(5)

        # 2.Listing
        listing_button = browser.find_element_by_xpath("//a[@data-tab='listing']")
        listing_button.click()

        time.sleep(5)

        data_catgory_1_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[1]/div/div"
        )
        data_catgory_1_select.click()

        time.sleep(5)

        data_catgory_1_value_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[1]/div/div/div[2]/div[4]"
        )
        data_catgory_1_value_select.click()

        time.sleep(5)

        data_catgory_2_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[2]/div/div"
        )
        data_catgory_2_select.click()

        time.sleep(5)

        data_catgory_2_value_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[2]/div/div/div[2]/div[6]"
        )
        data_catgory_2_value_select.click()

        time.sleep(5)

        data_catgory_3_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[3]/div/div"
        )
        data_catgory_3_select.click()

        time.sleep(5)

        data_catgory_3_value_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[3]/div/div/div[2]/div[15]"
        )
        data_catgory_3_value_select.click()

        time.sleep(5)

        data_catgory_4_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[4]/div/div"
        )
        data_catgory_4_select.click()

        time.sleep(5)

        data_catgory_4_value_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[4]/div/div/div[2]/div[20]"
        )
        data_catgory_4_value_select.click()

        time.sleep(5)

        data_catgory_5_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[5]/div/div"
        )
        data_catgory_5_select.click()

        time.sleep(5)

        data_catgory_5_value_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[5]/div/div/div[2]/div[34]"
        )
        data_catgory_5_value_select.click()

        time.sleep(5)

        # check the Small Business checkbox
        small_business_checkbox = browser.find_element_by_xpath(
            "//label[@for='data_product__company_size_ids-1']"
        )
        small_business_checkbox.click()

        time.sleep(5)

        # check the Medium-sized Business checkbox
        medium_sized_business_checkbox = browser.find_element_by_xpath(
            "//label[@for='data_product__company_size_ids-2']"
        )
        medium_sized_business_checkbox.click()

        time.sleep(5)

        # check the Entreprise checkbox
        entreprise_checkbox = browser.find_element_by_xpath(
            "//label[@for='data_product__company_size_ids-3']"
        )
        entreprise_checkbox.click()

        time.sleep(5)

        use_cases_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]"
        )
        use_cases_select.click()

        time.sleep(5)

        use_case_1_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[33]"
        )
        use_case_1_select.click()

        time.sleep(5)

        use_cases_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]"
        )
        use_cases_select.click()

        time.sleep(5)

        use_case_2_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[37]"
        )
        use_case_2_select.click()

        time.sleep(5)

        use_cases_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]"
        )
        use_cases_select.click()

        time.sleep(5)

        use_case_3_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[122]"
        )
        use_case_3_select.click()

        time.sleep(5)

        use_cases_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]"
        )
        use_cases_select.click()

        time.sleep(5)

        use_case_4_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[135]"
        )
        use_case_4_select.click()

        time.sleep(5)

        use_cases_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]"
        )
        use_cases_select.click()

        time.sleep(5)

        use_case_5_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[139]"
        )
        use_case_5_select.click()

        time.sleep(5)

        # 3. Coverage by myself
        coverage_button = browser.find_element_by_xpath("//a[@data-tab='coverage']")
        coverage_button.click()

        time.sleep(5)

        # Historical Coverage
        historical_coverage_input = browser.find_element_by_xpath(
            '//input[@id="data_product__history"]'
        )
        historical_coverage_input.clear()
        historical_coverage_input.send_keys("1")

        time.sleep(5)

        range_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[5]/div/div[2]/div[3]/div[2]/div"
        )
        range_select.click()

        time.sleep(5)

        weeks_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[5]/div/div[2]/div[3]/div[2]/div/div[2]/div[2]"
        )
        weeks_select.click()

        time.sleep(5)

        # 4. Volume and quality
        volume_and_quality_button = browser.find_element_by_xpath("//a[@data-tab='volume_and_quality']")
        volume_and_quality_button.click()

        time.sleep(5)

        # Add Volume
        add_volume_button = browser.find_element_by_xpath("//a[@data-association='volume']")
        add_volume_button.click()

        time.sleep(5)

        # Volume input
        volume_input = browser.find_element_by_xpath("//input[@id='data_product_volume__value'][@type='number']")
        volume_input.clear()
        volume_input.send_keys(str(number_of_records))

        time.sleep(5)

        # unit_input
        unit_input = browser.find_element_by_xpath("//input[@id='data_product_volume__unit'][@type='text']")
        unit_input.clear()
        unit_input.send_keys("records")

        time.sleep(5)

        # Add Quality Attribute
        add_quality_attribute_button = browser.find_element_by_xpath("//a[@data-association='quality']")
        add_quality_attribute_button.click()

        time.sleep(5)

        # quality in % input
        quality_input = browser.find_element_by_xpath("//input[@id='data_product_quality__percentage'][@type='number']")
        quality_input.clear()
        quality_input.send_keys("80")

        time.sleep(5)

        # unit quality input
        unit_quality_input = browser.find_element_by_xpath("//input[@id='data_product_quality__unit'][@type='text']")
        unit_quality_input.clear()
        unit_quality_input.send_keys("match rate")

        time.sleep(5)

        # 5. Attributes
        attributes_button = browser.find_element_by_xpath("//a[@data-tab='attributes']")
        attributes_button.click()

        time.sleep(5)

        # Add Attribute _ company_name
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(5)

        # name input
        name_input = browser.find_element_by_xpath(
            "//input[@id='data_product_attribute_spec__name']"
        )
        name_input.clear()
        name_input.send_keys("company_name")

        time.sleep(5)

        # example input
        example_input = browser.find_element_by_xpath(
            "//input[@id='data_product_attribute_spec__example']"
        )
        example_input.clear()
        example_input.send_keys("Company A")

        time.sleep(5)

        # description input
        description_input = browser.find_element_by_xpath(
            "//input[@id='data_product_attribute_spec__description']"
        )
        description_input.clear()
        description_input.send_keys("A company name")

        time.sleep(5)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "//input[@id='data_product_attribute_spec__number_of_records']"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(5)

        # Add Attribute _ postal_address
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # postal_address input
        postal_address_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[2]/td[2]/div/input"
        )
        postal_address_input.clear()
        postal_address_input.send_keys("postal_address")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[2]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys("1 Street postal address XXX Country")

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[2]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("A postal address")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[2]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ phone_number
        add_attribute_button = browser.find_element_by_xpath(
            "//a[@data-association='attribute_spec']"
        )
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[3]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("phone_number")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[3]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys(str(indicatif_telephonique))

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[3]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("A phone number of the company")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[3]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ website
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[4]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("website")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[4]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys("https://example.example")

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[4]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("A website of the company")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[4]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ email
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[5]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("email")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[5]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys("example@example.example")

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[5]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("An email address of the company")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[5]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ region
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[6]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("region")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[6]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys(str(region))

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[6]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("A region name")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[6]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ activity
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[7]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("activity")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[7]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys("Bank")

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[7]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("An activity")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[7]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ country
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[8]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("country")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[8]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys(str(pays))

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[8]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("A country")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[8]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # 6. Delivery
        delivery_button = browser.find_element_by_xpath("//a[@class='item'][@data-tab='delivery']")
        delivery_button.click()

        time.sleep(5)

        # Email checkbox
        email_checkbox = browser.find_element_by_xpath("//label[@for='data_product__transfer_method_ids-9']")
        email_checkbox.click()

        time.sleep(5)

        # Json checkbox
        json_checkbox = browser.find_element_by_xpath("//label[@for='data_product__data_format_ids-10']")
        json_checkbox.click()

        time.sleep(5)

        #  csv checkbox
        csv_checkbox = browser.find_element_by_xpath("//label[@for='data_product__data_format_ids-12']")
        csv_checkbox.click()

        time.sleep(5)

        # xls checkbox
        xls_checkbox = browser.find_element_by_xpath("//label[@for='data_product__data_format_ids-13']")
        xls_checkbox.click()

        time.sleep(5)

        # sql checkbox
        sql_checkbox = browser.find_element_by_xpath("//label[@for='data_product__data_format_ids-14']")
        sql_checkbox.click()

        time.sleep(5)

        # on-demand checkbox
        on_demand_checkbox = browser.find_element_by_xpath("//label[@for='data_product__transfer_frequency_ids-10']")
        on_demand_checkbox.click()

        time.sleep(5)

        # 7. Pricing
        pricing_button = browser.find_element_by_xpath("//a[@data-tab='pricing']")
        pricing_button.click()

        time.sleep(5)

        # One-off purchase checkbox
        one_off_purchase_checkbox = browser.find_element_by_xpath(
            "//label[@for='data_product_pricing_plan__pricing_model_id-1']"
        )
        one_off_purchase_checkbox.click()

        time.sleep(5)

        # starts at one-off purchase input
        starts_at_one_off_purchase_input = browser.find_element_by_xpath(
            "//input[@id='data_product_pricing_plan__starts_at_price']"
        )
        starts_at_one_off_purchase_input.clear()
        starts_at_one_off_purchase_input.send_keys(str(price))

        time.sleep(5)

        currency_select = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[9]/div/div[2]/div[2]/div"
        )
        currency_select.click()

        time.sleep(5)

        eur_select = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[9]/div/div[2]/div[2]/div/div[2]/div[2]"
        )
        eur_select.click()

        time.sleep(5)

    # ok
    def test_push_one_product_for_b2b_contact_data_for_belize(self):
        print("test_push_one_product_for_b2b_contact_data_for_belize")

        number_of_records = 1800

        indicatif_telephonique = "(+501) xxx xxxxxx"

        price = "1.99"

        pays = "Belize"

        region = "Belize"

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(5)

        # with Firefox
        browser = webdriver.Firefox(executable_path='..\\geckodriver.exe')

        time.sleep(20)

        # maximize window
        browser.maximize_window()

        time.sleep(10)

        # open
        browser.get('https://datarade.ai/')

        time.sleep(15)

        clear_button = browser.find_element_by_xpath("//button[@data-cf-action='reject'][@aria-label='Deny']")
        clear_button.click()

        time.sleep(5)

        sign_in_button = browser.find_element_by_xpath("//a[@class='navbar__item'][@href='/users/sign_in']")
        sign_in_button.click()

        time.sleep(15)

        work_email_input = browser.find_element_by_xpath("//input[@id='user__email'][@name='user[email]']")
        work_email_input.clear()
        work_email_input.send_keys(""
        "")

        time.sleep(5)

        passwrod_input = browser.find_element_by_xpath("//input[@id='user__password'][@name='user[password]']")
        passwrod_input.clear()
        passwrod_input.send_keys("")

        time.sleep(5)

        login_button = browser.find_element_by_xpath("//input[@type='submit'][@name='commit']")
        login_button.click()

        time.sleep(15)

        holomorphe_button = browser.find_element_by_xpath(
            "//a[@class='navbar__item tablet-landscape-hidden'][@href='/my/provider']")
        holomorphe_button.click()

        time.sleep(10)

        new_product_button = browser.find_element_by_xpath(
            "//a[@class='button primary modern small'][@href='/my/provider/data_products/new']")
        new_product_button.click()

        time.sleep(10)

        # 1.Basics
        # Title
        title_input = browser.find_element_by_xpath("//input[@id='data_product__name'][@name='data_product[name]']")
        title_input.clear()

        title = "Holomorphe / B2B Contact Data / Private Company data / " + pays

        title_input.send_keys(title)

        time.sleep(5)

        # Short Description
        short_description_input = browser.find_element_by_xpath(
            "//textarea[@id='data_product__short_description'][@name='data_product[short_description]']")
        short_description_input.clear()

        short_description = "The key benefits of this data product are : valuable, affordable and reliable. " \
                            "The main attributes of this data product are : company name, postal address, " \
                            "phone number, website, email, region, activity and country. " \
                            "The coverage of this data product is : " + pays + "."

        short_description_input.send_keys(short_description)

        time.sleep(5)

        # In-depth Description
        in_depth_description_input = browser.find_element_by_xpath(
            "//textarea[@id='data_product__description'][@name='data_product[description]']")
        in_depth_description_input.clear()

        in_depth_description = "This data product is efficient because the work for this data collection was " \
                               "made by a complex algorithm that uses artificial intelligence to operate. " \
                               "The data was generally sourced from the web. The primary use-cases or verticals of " \
                               "this data product are : direct marketing, digital marketing, email marketing, " \
                               "phone marketing, voice over ip marketing, business strategy, business intelligence, " \
                               "customer segmentation, customer location and activity segmentation. The activities " \
                               "of B2B contact data are : employment agencies, real estate agencies, recruitment " \
                               "agencies, software, hotel, social, cleaning, charity, financial, restaurant, " \
                               "building, hairdresser, florist, locksmith, bakery, insurance, pharmacy, mover, " \
                               "electricity, plumbing, security, attorney, bank, garage, dentist, doctor, " \
                               "accountant, grocery, notary, jewellery, tailor, butcher, library, architect, cement, " \
                               "heating, boat, cold, steel, chemical, gas and gold."

        in_depth_description_input.send_keys(in_depth_description)

        time.sleep(5)

        # 2.Listing
        listing_button = browser.find_element_by_xpath("//a[@data-tab='listing']")
        listing_button.click()

        time.sleep(5)

        data_catgory_1_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[1]/div/div"
        )
        data_catgory_1_select.click()

        time.sleep(5)

        data_catgory_1_value_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[1]/div/div/div[2]/div[4]"
        )
        data_catgory_1_value_select.click()

        time.sleep(5)

        data_catgory_2_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[2]/div/div"
        )
        data_catgory_2_select.click()

        time.sleep(5)

        data_catgory_2_value_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[2]/div/div/div[2]/div[6]"
        )
        data_catgory_2_value_select.click()

        time.sleep(5)

        data_catgory_3_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[3]/div/div"
        )
        data_catgory_3_select.click()

        time.sleep(5)

        data_catgory_3_value_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[3]/div/div/div[2]/div[15]"
        )
        data_catgory_3_value_select.click()

        time.sleep(5)

        data_catgory_4_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[4]/div/div"
        )
        data_catgory_4_select.click()

        time.sleep(5)

        data_catgory_4_value_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[4]/div/div/div[2]/div[20]"
        )
        data_catgory_4_value_select.click()

        time.sleep(5)

        data_catgory_5_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[5]/div/div"
        )
        data_catgory_5_select.click()

        time.sleep(5)

        data_catgory_5_value_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[5]/div/div/div[2]/div[34]"
        )
        data_catgory_5_value_select.click()

        time.sleep(5)

        # check the Small Business checkbox
        small_business_checkbox = browser.find_element_by_xpath(
            "//label[@for='data_product__company_size_ids-1']"
        )
        small_business_checkbox.click()

        time.sleep(5)

        # check the Medium-sized Business checkbox
        medium_sized_business_checkbox = browser.find_element_by_xpath(
            "//label[@for='data_product__company_size_ids-2']"
        )
        medium_sized_business_checkbox.click()

        time.sleep(5)

        # check the Entreprise checkbox
        entreprise_checkbox = browser.find_element_by_xpath(
            "//label[@for='data_product__company_size_ids-3']"
        )
        entreprise_checkbox.click()

        time.sleep(5)

        use_cases_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]"
        )
        use_cases_select.click()

        time.sleep(5)

        use_case_1_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[33]"
        )
        use_case_1_select.click()

        time.sleep(5)

        use_cases_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]"
        )
        use_cases_select.click()

        time.sleep(5)

        use_case_2_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[37]"
        )
        use_case_2_select.click()

        time.sleep(5)

        use_cases_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]"
        )
        use_cases_select.click()

        time.sleep(5)

        use_case_3_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[122]"
        )
        use_case_3_select.click()

        time.sleep(5)

        use_cases_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]"
        )
        use_cases_select.click()

        time.sleep(5)

        use_case_4_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[135]"
        )
        use_case_4_select.click()

        time.sleep(5)

        use_cases_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]"
        )
        use_cases_select.click()

        time.sleep(5)

        use_case_5_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[139]"
        )
        use_case_5_select.click()

        time.sleep(5)

        # 3. Coverage by myself
        coverage_button = browser.find_element_by_xpath("//a[@data-tab='coverage']")
        coverage_button.click()

        time.sleep(5)

        # Historical Coverage
        historical_coverage_input = browser.find_element_by_xpath(
            '//input[@id="data_product__history"]'
        )
        historical_coverage_input.clear()
        historical_coverage_input.send_keys("1")

        time.sleep(5)

        range_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[5]/div/div[2]/div[3]/div[2]/div"
        )
        range_select.click()

        time.sleep(5)

        weeks_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[5]/div/div[2]/div[3]/div[2]/div/div[2]/div[2]"
        )
        weeks_select.click()

        time.sleep(5)

        # 4. Volume and quality
        volume_and_quality_button = browser.find_element_by_xpath("//a[@data-tab='volume_and_quality']")
        volume_and_quality_button.click()

        time.sleep(5)

        # Add Volume
        add_volume_button = browser.find_element_by_xpath("//a[@data-association='volume']")
        add_volume_button.click()

        time.sleep(5)

        # Volume input
        volume_input = browser.find_element_by_xpath("//input[@id='data_product_volume__value'][@type='number']")
        volume_input.clear()
        volume_input.send_keys(str(number_of_records))

        time.sleep(5)

        # unit_input
        unit_input = browser.find_element_by_xpath("//input[@id='data_product_volume__unit'][@type='text']")
        unit_input.clear()
        unit_input.send_keys("records")

        time.sleep(5)

        # Add Quality Attribute
        add_quality_attribute_button = browser.find_element_by_xpath("//a[@data-association='quality']")
        add_quality_attribute_button.click()

        time.sleep(5)

        # quality in % input
        quality_input = browser.find_element_by_xpath("//input[@id='data_product_quality__percentage'][@type='number']")
        quality_input.clear()
        quality_input.send_keys("80")

        time.sleep(5)

        # unit quality input
        unit_quality_input = browser.find_element_by_xpath("//input[@id='data_product_quality__unit'][@type='text']")
        unit_quality_input.clear()
        unit_quality_input.send_keys("match rate")

        time.sleep(5)

        # 5. Attributes
        attributes_button = browser.find_element_by_xpath("//a[@data-tab='attributes']")
        attributes_button.click()

        time.sleep(5)

        # Add Attribute _ company_name
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(5)

        # name input
        name_input = browser.find_element_by_xpath(
            "//input[@id='data_product_attribute_spec__name']"
        )
        name_input.clear()
        name_input.send_keys("company_name")

        time.sleep(5)

        # example input
        example_input = browser.find_element_by_xpath(
            "//input[@id='data_product_attribute_spec__example']"
        )
        example_input.clear()
        example_input.send_keys("Company A")

        time.sleep(5)

        # description input
        description_input = browser.find_element_by_xpath(
            "//input[@id='data_product_attribute_spec__description']"
        )
        description_input.clear()
        description_input.send_keys("A company name")

        time.sleep(5)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "//input[@id='data_product_attribute_spec__number_of_records']"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(5)

        # Add Attribute _ postal_address
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # postal_address input
        postal_address_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[2]/td[2]/div/input"
        )
        postal_address_input.clear()
        postal_address_input.send_keys("postal_address")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[2]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys("1 Street postal address XXX Country")

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[2]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("A postal address")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[2]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ phone_number
        add_attribute_button = browser.find_element_by_xpath(
            "//a[@data-association='attribute_spec']"
        )
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[3]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("phone_number")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[3]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys(str(indicatif_telephonique))

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[3]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("A phone number of the company")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[3]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ website
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[4]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("website")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[4]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys("https://example.example")

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[4]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("A website of the company")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[4]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ email
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[5]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("email")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[5]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys("example@example.example")

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[5]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("An email address of the company")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[5]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ region
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[6]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("region")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[6]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys(str(region))

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[6]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("A region name")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[6]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ activity
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[7]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("activity")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[7]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys("Bank")

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[7]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("An activity")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[7]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ country
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[8]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("country")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[8]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys(str(pays))

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[8]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("A country")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[8]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # 6. Delivery
        delivery_button = browser.find_element_by_xpath("//a[@class='item'][@data-tab='delivery']")
        delivery_button.click()

        time.sleep(5)

        # Email checkbox
        email_checkbox = browser.find_element_by_xpath("//label[@for='data_product__transfer_method_ids-9']")
        email_checkbox.click()

        time.sleep(5)

        # Json checkbox
        json_checkbox = browser.find_element_by_xpath("//label[@for='data_product__data_format_ids-10']")
        json_checkbox.click()

        time.sleep(5)

        #  csv checkbox
        csv_checkbox = browser.find_element_by_xpath("//label[@for='data_product__data_format_ids-12']")
        csv_checkbox.click()

        time.sleep(5)

        # xls checkbox
        xls_checkbox = browser.find_element_by_xpath("//label[@for='data_product__data_format_ids-13']")
        xls_checkbox.click()

        time.sleep(5)

        # sql checkbox
        sql_checkbox = browser.find_element_by_xpath("//label[@for='data_product__data_format_ids-14']")
        sql_checkbox.click()

        time.sleep(5)

        # on-demand checkbox
        on_demand_checkbox = browser.find_element_by_xpath("//label[@for='data_product__transfer_frequency_ids-10']")
        on_demand_checkbox.click()

        time.sleep(5)

        # 7. Pricing
        pricing_button = browser.find_element_by_xpath("//a[@data-tab='pricing']")
        pricing_button.click()

        time.sleep(5)

        # One-off purchase checkbox
        one_off_purchase_checkbox = browser.find_element_by_xpath(
            "//label[@for='data_product_pricing_plan__pricing_model_id-1']"
        )
        one_off_purchase_checkbox.click()

        time.sleep(5)

        # starts at one-off purchase input
        starts_at_one_off_purchase_input = browser.find_element_by_xpath(
            "//input[@id='data_product_pricing_plan__starts_at_price']"
        )
        starts_at_one_off_purchase_input.clear()
        starts_at_one_off_purchase_input.send_keys(str(price))

        time.sleep(5)

        currency_select = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[9]/div/div[2]/div[2]/div"
        )
        currency_select.click()

        time.sleep(5)

        eur_select = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[9]/div/div[2]/div[2]/div/div[2]/div[2]"
        )
        eur_select.click()

        time.sleep(5)

    # ok
    def test_push_one_product_for_b2b_contact_data_for_st_vincent(self):
        print("test_push_one_product_for_b2b_contact_data_for_st_vincent")

        number_of_records = 611

        indicatif_telephonique = "(+1784) xxx xxxxxx"

        price = "1.99"

        pays = "Saint Vincent and the Grenadines"

        region = "Saint Vincent and the Grenadines"

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(5)

        # with Firefox
        browser = webdriver.Firefox(executable_path='..\\geckodriver.exe')

        time.sleep(20)

        # maximize window
        browser.maximize_window()

        time.sleep(10)

        # open
        browser.get('https://datarade.ai/')

        time.sleep(15)

        clear_button = browser.find_element_by_xpath("//button[@data-cf-action='reject'][@aria-label='Deny']")
        clear_button.click()

        time.sleep(5)

        sign_in_button = browser.find_element_by_xpath("//a[@class='navbar__item'][@href='/users/sign_in']")
        sign_in_button.click()

        time.sleep(15)

        work_email_input = browser.find_element_by_xpath("//input[@id='user__email'][@name='user[email]']")
        work_email_input.clear()
        work_email_input.send_keys(""
        "")

        time.sleep(5)

        passwrod_input = browser.find_element_by_xpath("//input[@id='user__password'][@name='user[password]']")
        passwrod_input.clear()
        passwrod_input.send_keys("")

        time.sleep(5)

        login_button = browser.find_element_by_xpath("//input[@type='submit'][@name='commit']")
        login_button.click()

        time.sleep(15)

        holomorphe_button = browser.find_element_by_xpath(
            "//a[@class='navbar__item tablet-landscape-hidden'][@href='/my/provider']")
        holomorphe_button.click()

        time.sleep(10)

        new_product_button = browser.find_element_by_xpath(
            "//a[@class='button primary modern small'][@href='/my/provider/data_products/new']")
        new_product_button.click()

        time.sleep(10)

        # 1.Basics
        # Title
        title_input = browser.find_element_by_xpath("//input[@id='data_product__name'][@name='data_product[name]']")
        title_input.clear()

        title = "Holomorphe / B2B Contact Data / Private Company data / " + pays

        title_input.send_keys(title)

        time.sleep(5)

        # Short Description
        short_description_input = browser.find_element_by_xpath(
            "//textarea[@id='data_product__short_description'][@name='data_product[short_description]']")
        short_description_input.clear()

        short_description = "The key benefits of this data product are : valuable, affordable and reliable. " \
                            "The main attributes of this data product are : company name, postal address, " \
                            "phone number, website, email, region, activity and country. " \
                            "The coverage of this data product is : " + pays + "."

        short_description_input.send_keys(short_description)

        time.sleep(5)

        # In-depth Description
        in_depth_description_input = browser.find_element_by_xpath(
            "//textarea[@id='data_product__description'][@name='data_product[description]']")
        in_depth_description_input.clear()

        in_depth_description = "This data product is efficient because the work for this data collection was " \
                               "made by a complex algorithm that uses artificial intelligence to operate. " \
                               "The data was generally sourced from the web. The primary use-cases or verticals of " \
                               "this data product are : direct marketing, digital marketing, email marketing, " \
                               "phone marketing, voice over ip marketing, business strategy, business intelligence, " \
                               "customer segmentation, customer location and activity segmentation. The activities " \
                               "of B2B contact data are : employment agencies, real estate agencies, recruitment " \
                               "agencies, software, hotel, social, cleaning, charity, financial, restaurant, " \
                               "building, hairdresser, florist, locksmith, bakery, insurance, pharmacy, mover, " \
                               "electricity, plumbing, security, attorney, bank, garage, dentist, doctor, " \
                               "accountant, grocery, notary, jewellery, tailor, butcher, library, architect, cement, " \
                               "heating, boat, cold, steel, chemical, gas and gold."

        in_depth_description_input.send_keys(in_depth_description)

        time.sleep(5)

        # 2.Listing
        listing_button = browser.find_element_by_xpath("//a[@data-tab='listing']")
        listing_button.click()

        time.sleep(5)

        data_catgory_1_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[1]/div/div"
        )
        data_catgory_1_select.click()

        time.sleep(5)

        data_catgory_1_value_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[1]/div/div/div[2]/div[4]"
        )
        data_catgory_1_value_select.click()

        time.sleep(5)

        data_catgory_2_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[2]/div/div"
        )
        data_catgory_2_select.click()

        time.sleep(5)

        data_catgory_2_value_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[2]/div/div/div[2]/div[6]"
        )
        data_catgory_2_value_select.click()

        time.sleep(5)

        data_catgory_3_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[3]/div/div"
        )
        data_catgory_3_select.click()

        time.sleep(5)

        data_catgory_3_value_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[3]/div/div/div[2]/div[15]"
        )
        data_catgory_3_value_select.click()

        time.sleep(5)

        data_catgory_4_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[4]/div/div"
        )
        data_catgory_4_select.click()

        time.sleep(5)

        data_catgory_4_value_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[4]/div/div/div[2]/div[20]"
        )
        data_catgory_4_value_select.click()

        time.sleep(5)

        data_catgory_5_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[5]/div/div"
        )
        data_catgory_5_select.click()

        time.sleep(5)

        data_catgory_5_value_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[5]/div/div/div[2]/div[34]"
        )
        data_catgory_5_value_select.click()

        time.sleep(5)

        # check the Small Business checkbox
        small_business_checkbox = browser.find_element_by_xpath(
            "//label[@for='data_product__company_size_ids-1']"
        )
        small_business_checkbox.click()

        time.sleep(5)

        # check the Medium-sized Business checkbox
        medium_sized_business_checkbox = browser.find_element_by_xpath(
            "//label[@for='data_product__company_size_ids-2']"
        )
        medium_sized_business_checkbox.click()

        time.sleep(5)

        # check the Entreprise checkbox
        entreprise_checkbox = browser.find_element_by_xpath(
            "//label[@for='data_product__company_size_ids-3']"
        )
        entreprise_checkbox.click()

        time.sleep(5)

        use_cases_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]"
        )
        use_cases_select.click()

        time.sleep(5)

        use_case_1_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[33]"
        )
        use_case_1_select.click()

        time.sleep(5)

        use_cases_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]"
        )
        use_cases_select.click()

        time.sleep(5)

        use_case_2_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[37]"
        )
        use_case_2_select.click()

        time.sleep(5)

        use_cases_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]"
        )
        use_cases_select.click()

        time.sleep(5)

        use_case_3_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[122]"
        )
        use_case_3_select.click()

        time.sleep(5)

        use_cases_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]"
        )
        use_cases_select.click()

        time.sleep(5)

        use_case_4_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[135]"
        )
        use_case_4_select.click()

        time.sleep(5)

        use_cases_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]"
        )
        use_cases_select.click()

        time.sleep(5)

        use_case_5_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[139]"
        )
        use_case_5_select.click()

        time.sleep(5)

        # 3. Coverage by myself
        coverage_button = browser.find_element_by_xpath("//a[@data-tab='coverage']")
        coverage_button.click()

        time.sleep(5)

        # Historical Coverage
        historical_coverage_input = browser.find_element_by_xpath(
            '//input[@id="data_product__history"]'
        )
        historical_coverage_input.clear()
        historical_coverage_input.send_keys("1")

        time.sleep(5)

        range_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[5]/div/div[2]/div[3]/div[2]/div"
        )
        range_select.click()

        time.sleep(5)

        weeks_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[5]/div/div[2]/div[3]/div[2]/div/div[2]/div[2]"
        )
        weeks_select.click()

        time.sleep(5)

        # 4. Volume and quality
        volume_and_quality_button = browser.find_element_by_xpath("//a[@data-tab='volume_and_quality']")
        volume_and_quality_button.click()

        time.sleep(5)

        # Add Volume
        add_volume_button = browser.find_element_by_xpath("//a[@data-association='volume']")
        add_volume_button.click()

        time.sleep(5)

        # Volume input
        volume_input = browser.find_element_by_xpath("//input[@id='data_product_volume__value'][@type='number']")
        volume_input.clear()
        volume_input.send_keys(str(number_of_records))

        time.sleep(5)

        # unit_input
        unit_input = browser.find_element_by_xpath("//input[@id='data_product_volume__unit'][@type='text']")
        unit_input.clear()
        unit_input.send_keys("records")

        time.sleep(5)

        # Add Quality Attribute
        add_quality_attribute_button = browser.find_element_by_xpath("//a[@data-association='quality']")
        add_quality_attribute_button.click()

        time.sleep(5)

        # quality in % input
        quality_input = browser.find_element_by_xpath("//input[@id='data_product_quality__percentage'][@type='number']")
        quality_input.clear()
        quality_input.send_keys("80")

        time.sleep(5)

        # unit quality input
        unit_quality_input = browser.find_element_by_xpath("//input[@id='data_product_quality__unit'][@type='text']")
        unit_quality_input.clear()
        unit_quality_input.send_keys("match rate")

        time.sleep(5)

        # 5. Attributes
        attributes_button = browser.find_element_by_xpath("//a[@data-tab='attributes']")
        attributes_button.click()

        time.sleep(5)

        # Add Attribute _ company_name
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(5)

        # name input
        name_input = browser.find_element_by_xpath(
            "//input[@id='data_product_attribute_spec__name']"
        )
        name_input.clear()
        name_input.send_keys("company_name")

        time.sleep(5)

        # example input
        example_input = browser.find_element_by_xpath(
            "//input[@id='data_product_attribute_spec__example']"
        )
        example_input.clear()
        example_input.send_keys("Company A")

        time.sleep(5)

        # description input
        description_input = browser.find_element_by_xpath(
            "//input[@id='data_product_attribute_spec__description']"
        )
        description_input.clear()
        description_input.send_keys("A company name")

        time.sleep(5)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "//input[@id='data_product_attribute_spec__number_of_records']"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(5)

        # Add Attribute _ postal_address
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # postal_address input
        postal_address_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[2]/td[2]/div/input"
        )
        postal_address_input.clear()
        postal_address_input.send_keys("postal_address")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[2]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys("1 Street postal address XXX Country")

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[2]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("A postal address")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[2]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ phone_number
        add_attribute_button = browser.find_element_by_xpath(
            "//a[@data-association='attribute_spec']"
        )
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[3]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("phone_number")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[3]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys(str(indicatif_telephonique))

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[3]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("A phone number of the company")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[3]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ website
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[4]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("website")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[4]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys("https://example.example")

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[4]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("A website of the company")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[4]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ email
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[5]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("email")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[5]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys("example@example.example")

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[5]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("An email address of the company")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[5]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ region
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[6]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("region")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[6]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys(str(region))

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[6]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("A region name")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[6]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ activity
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[7]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("activity")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[7]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys("Bank")

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[7]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("An activity")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[7]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # Add Attribute _ country
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(10)

        # name input
        name_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[8]/td[2]/div/input"
        )
        name_input.clear()
        name_input.send_keys("country")

        time.sleep(10)

        # example input
        example_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[8]/td[3]/div/input"
        )
        example_input.clear()
        example_input.send_keys(str(pays))

        time.sleep(10)

        # description input
        description_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[8]/td[4]/div/input"
        )
        description_input.clear()
        description_input.send_keys("A country")

        time.sleep(10)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[7]/div/div[2]/table/tbody/tr[8]/td[5]/div/input"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("Several hundreds")

        time.sleep(10)

        # 6. Delivery
        delivery_button = browser.find_element_by_xpath("//a[@class='item'][@data-tab='delivery']")
        delivery_button.click()

        time.sleep(5)

        # Email checkbox
        email_checkbox = browser.find_element_by_xpath("//label[@for='data_product__transfer_method_ids-9']")
        email_checkbox.click()

        time.sleep(5)

        # Json checkbox
        json_checkbox = browser.find_element_by_xpath("//label[@for='data_product__data_format_ids-10']")
        json_checkbox.click()

        time.sleep(5)

        #  csv checkbox
        csv_checkbox = browser.find_element_by_xpath("//label[@for='data_product__data_format_ids-12']")
        csv_checkbox.click()

        time.sleep(5)

        # xls checkbox
        xls_checkbox = browser.find_element_by_xpath("//label[@for='data_product__data_format_ids-13']")
        xls_checkbox.click()

        time.sleep(5)

        # sql checkbox
        sql_checkbox = browser.find_element_by_xpath("//label[@for='data_product__data_format_ids-14']")
        sql_checkbox.click()

        time.sleep(5)

        # on-demand checkbox
        on_demand_checkbox = browser.find_element_by_xpath("//label[@for='data_product__transfer_frequency_ids-10']")
        on_demand_checkbox.click()

        time.sleep(5)

        # 7. Pricing
        pricing_button = browser.find_element_by_xpath("//a[@data-tab='pricing']")
        pricing_button.click()

        time.sleep(5)

        # One-off purchase checkbox
        one_off_purchase_checkbox = browser.find_element_by_xpath(
            "//label[@for='data_product_pricing_plan__pricing_model_id-1']"
        )
        one_off_purchase_checkbox.click()

        time.sleep(5)

        # starts at one-off purchase input
        starts_at_one_off_purchase_input = browser.find_element_by_xpath(
            "//input[@id='data_product_pricing_plan__starts_at_price']"
        )
        starts_at_one_off_purchase_input.clear()
        starts_at_one_off_purchase_input.send_keys(str(price))

        time.sleep(5)

        currency_select = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[9]/div/div[2]/div[2]/div"
        )
        currency_select.click()

        time.sleep(5)

        eur_select = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[9]/div/div[2]/div[2]/div/div[2]/div[2]"
        )
        eur_select.click()

        time.sleep(5)


class UnitTestsWebAutomationDataradePushColdEmailContactData(unittest.TestCase):
    # ok
    def test_count_characters_for_cold_email_contact_data(self):
        print('test_count_characters_for_cold_email_contact_data')

        """
What makes a good product title?

Give your Data Product a title that is keyword search-optimized.

Great Data Product titles have 50 to 150 characters and ideally contain the following details:
- Your Brand Name
- Data Type
- Countries / Geographies
- Volume (e.g. 10M Devices, 5M companies, 20M consumers)
- Key Benefits (e.g.GDPR-compliant, real-time sourced, 10 years historic coverage)

Examples of search optimized Data Product titles:
- Datatrade’s USA C-level executives b2b contact data (e-mail, phone) w/ 300k records
- Datatrade’s Location Data for People Visits to large cities in the UK, 18 months API
- Datatrade’s ESG ratings of Middle East companies with 5 years of history - tickerized
        """
        pays = "Russia"

        title = "Holomorphe / Cold Email Contact Data / Private Company Data / " + pays + " / Thousands of companies"

        """
How does a good short description look?

This description will be shown on your Data Product card that appears on each filter page. 

Providing a short description of min. 100 characters helps spark further data buyer interest so that they want 
to learn more about it and view it in detail. 

We recommend including these points in your short description:
- Key benefits of your Data Product
- The main attributes of your data
- Coverage (industries, countries)
- Scale & quality indicators
        """
        short_description = "The key benefits of this data product are : unique, no personal data and high volume of " \
                            "records." \
                            "The main attribute of this data product are : cold email contact of private company." \
                            "The coverage of this data product is : " + pays + "."

        """
What does a good description look like?

The in-depth product description is your chance to engage with data buyers who want to fully understand a Data 
Product before requesting it. 

By adding search-optimized keywords in the text you can increase the visibility of your Data Products as well.

Try to answer the following questions in your in-depth description:
- What makes your data unique?
- How is the data generally sourced?
- What are the primary use-cases or verticals of this Data Product?
- How does this Data Product fit into your broader data offering ?

Great in-depth descriptions comprise several hundred words. 

Most top performing products on Datarade have a description length between 3000 and 6000 characters.
        """
        in_depth_description = "This data product is unique because the work for this data collection was " \
                               "made by a complex algorithm that uses Tor network. The data was generally sourced " \
                               "from Tor network. The primary use-cases or verticals of this data product are : " \
                               "direct marketing, digital marketing, cold email marketing, " \
                               "business strategy, business intelligence, web traffic analysis and " \
                               "email campaign analysis."

        if 30 <= len(title) <= 150:
            print('title length is good')
        else:
            print('title length is bad')

        if 80 <= len(short_description) <= 300:
            print('short_description length is good')
        else:
            print('short_description length is bad')

        if 300 <= len(in_depth_description) <= 8000:
            print('in_depth_description length is good')
        else:
            print('in_depth_description length is bad')

    # ok
    def test_push_one_product_for_cold_email_contact_data(self):
        print("test_push_one_product_for_cold_email_contact_data")

        pays = "Argentina"

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(5)

        # with Firefox
        browser = webdriver.Firefox(executable_path='..\\geckodriver.exe')

        time.sleep(20)

        # maximize window
        browser.maximize_window()

        time.sleep(10)

        # open
        browser.get('https://datarade.ai/')

        time.sleep(15)

        clear_button = browser.find_element_by_xpath("//button[@data-cf-action='reject'][@aria-label='Deny']")
        clear_button.click()

        time.sleep(5)

        sign_in_button = browser.find_element_by_xpath("//a[@class='navbar__item'][@href='/users/sign_in']")
        sign_in_button.click()

        time.sleep(15)

        work_email_input = browser.find_element_by_xpath("//input[@id='user__email'][@name='user[email]']")
        work_email_input.clear()
        work_email_input.send_keys(""
        "")

        time.sleep(5)

        passwrod_input = browser.find_element_by_xpath("//input[@id='user__password'][@name='user[password]']")
        passwrod_input.clear()
        passwrod_input.send_keys("")

        time.sleep(5)

        login_button = browser.find_element_by_xpath("//input[@type='submit'][@name='commit']")
        login_button.click()

        time.sleep(15)

        holomorphe_button = browser.find_element_by_xpath(
            "//a[@class='navbar__item tablet-landscape-hidden'][@href='/my/provider']")
        holomorphe_button.click()

        time.sleep(10)

        new_product_button = browser.find_element_by_xpath(
            "//a[@class='button primary modern small'][@href='/my/provider/data_products/new']")
        new_product_button.click()

        time.sleep(10)

        # 1.Basics
        # Title
        title_input = browser.find_element_by_xpath("//input[@id='data_product__name'][@name='data_product[name]']")
        title_input.clear()

        title = "Holomorphe / Cold Email Contact Data / Private Company Data / " + pays + " / Thousands of companies"

        title_input.send_keys(title)

        time.sleep(5)

        # Short Description
        short_description_input = browser.find_element_by_xpath(
            "//textarea[@id='data_product__short_description'][@name='data_product[short_description]']")
        short_description_input.clear()

        short_description = "The key benefits of this data product are : unique, no personal data and high volume of " \
                            "records. " \
                            "The main attribute of this data product are : cold email contact of private company. " \
                            "The coverage of this data product is : " + pays + "."

        short_description_input.send_keys(short_description)

        time.sleep(5)

        # In-depth Description
        in_depth_description_input = browser.find_element_by_xpath(
            "//textarea[@id='data_product__description'][@name='data_product[description]']")
        in_depth_description_input.clear()

        in_depth_description = "This data product is unique because the work for this data collection was " \
                               "made by a complex algorithm that uses Tor network. The data was generally sourced " \
                               "from Tor network. The primary use-cases or verticals of this data product are : " \
                               "direct marketing, digital marketing, cold email marketing, " \
                               "business strategy, business intelligence, web traffic analysis and " \
                               "email campaign analysis."

        in_depth_description_input.send_keys(in_depth_description)

        time.sleep(5)

        # 2.Listing
        listing_button = browser.find_element_by_xpath("//a[@data-tab='listing']")
        listing_button.click()

        time.sleep(5)

        # Data category 1 (Anonymous IP Data)
        # data_category_1_input = browser.find_element_by_xpath("//li[1]/div[@id='field-data_product_category__category_id']/input[@tabindex='0']")
        # data_category_1_input.clear()
        # data_category_1_input.send_keys("Anonymous IP Data")
        # data_category_1_input.send_keys(Keys.ENTER)

        time.sleep(5)

        # check the Small Business checkbox
        small_business_checkbox = browser.find_element_by_xpath(
            "//label[@for='data_product__company_size_ids-1']"
        )
        small_business_checkbox.click()

        time.sleep(5)

        # check the Medium-sized Business checkbox
        medium_sized_business_checkbox = browser.find_element_by_xpath(
            "//label[@for='data_product__company_size_ids-2']"
        )
        medium_sized_business_checkbox.click()

        time.sleep(5)

        # check the Entreprise checkbox
        entreprise_checkbox = browser.find_element_by_xpath(
            "//label[@for='data_product__company_size_ids-3']"
        )
        entreprise_checkbox.click()

        time.sleep(5)

        # Use Cases
        # use_cases_input = browser.find_element_by_xpath("//div[@class='ui fluid search dropdown selection multiple']")
        # use_cases_input.clear()
        # use_cases_input.send_keys("Web Traffic Analysis")
        # use_cases_input.send_keys(Keys.ENTER)

        time.sleep(5)

        # 3. Coverage by myself

        # 4. Volume and quality
        volume_and_quality_button = browser.find_element_by_xpath("//a[@data-tab='volume_and_quality']")
        volume_and_quality_button.click()

        time.sleep(5)

        # Add Volume
        add_volume_button = browser.find_element_by_xpath("//a[@data-association='volume']")
        add_volume_button.click()

        time.sleep(5)

        # Volume input
        volume_input = browser.find_element_by_xpath("//input[@id='data_product_volume__value'][@type='number']")
        volume_input.clear()
        volume_input.send_keys("15571")

        time.sleep(5)

        # unit_input
        unit_input = browser.find_element_by_xpath("//input[@id='data_product_volume__unit'][@type='text']")
        unit_input.clear()
        unit_input.send_keys("records")

        time.sleep(5)

        # Add Quality Attribute
        add_quality_attribute_button = browser.find_element_by_xpath("//a[@data-association='quality']")
        add_quality_attribute_button.click()

        time.sleep(5)

        # quality in % input
        quality_input = browser.find_element_by_xpath("//input[@id='data_product_quality__percentage'][@type='number']")
        quality_input.clear()
        quality_input.send_keys("60")

        time.sleep(5)

        # unit quality input
        unit_quality_input = browser.find_element_by_xpath("//input[@id='data_product_quality__unit'][@type='text']")
        unit_quality_input.clear()
        unit_quality_input.send_keys("match rate")

        time.sleep(5)

        # 5. Attributes
        attributes_button = browser.find_element_by_xpath("//a[@data-tab='attributes']")
        attributes_button.click()

        time.sleep(5)

        # Add Attribute _ company_name
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(5)

        # name input
        name_input = browser.find_element_by_xpath(
            "//input[@id='data_product_attribute_spec__name']"
        )
        name_input.clear()
        name_input.send_keys("cold_email")

        time.sleep(5)

        # example input
        example_input = browser.find_element_by_xpath(
            "//input[@id='data_product_attribute_spec__example']"
        )
        example_input.clear()
        example_input.send_keys("info@example.com")

        time.sleep(5)

        # description input
        description_input = browser.find_element_by_xpath(
            "//input[@id='data_product_attribute_spec__description']"
        )
        description_input.clear()
        description_input.send_keys("A cold email of a private argentine company")

        time.sleep(5)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "//input[@id='data_product_attribute_spec__number_of_records']"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("15571")

        time.sleep(5)

        # 6. Delivery
        delivery_button = browser.find_element_by_xpath("//a[@class='item'][@data-tab='delivery']")
        delivery_button.click()

        time.sleep(5)

        # Email checkbox
        email_checkbox = browser.find_element_by_xpath("//label[@for='data_product__transfer_method_ids-9']")
        email_checkbox.click()

        time.sleep(5)

        # Json checkbox
        json_checkbox = browser.find_element_by_xpath("//label[@for='data_product__data_format_ids-10']")
        json_checkbox.click()

        time.sleep(5)

        #  csv checkbox
        csv_checkbox = browser.find_element_by_xpath("//label[@for='data_product__data_format_ids-12']")
        csv_checkbox.click()

        time.sleep(5)

        # xls checkbox
        xls_checkbox = browser.find_element_by_xpath("//label[@for='data_product__data_format_ids-13']")
        xls_checkbox.click()

        time.sleep(5)

        # sql checkbox
        sql_checkbox = browser.find_element_by_xpath("//label[@for='data_product__data_format_ids-14']")
        sql_checkbox.click()

        time.sleep(5)

        # on-demand checkbox
        on_demand_checkbox = browser.find_element_by_xpath("//label[@for='data_product__transfer_frequency_ids-10']")
        on_demand_checkbox.click()

        time.sleep(5)

        # 7. Pricing
        pricing_button = browser.find_element_by_xpath("//a[@data-tab='pricing']")
        pricing_button.click()

        time.sleep(5)

        # currency input
        # currency_input = browser.find_element_by_xpath("//div[@class='default text']")
        # currency_input.clear()
        # currency_input.send_keys("EUR")
        # currency_input.send_keys(Keys.ENTER)

        time.sleep(5)

        # One-off purchase checkbox
        one_off_purchase_checkbox = browser.find_element_by_xpath(
            "//label[@for='data_product_pricing_plan__pricing_model_id-1']"
        )
        one_off_purchase_checkbox.click()

        time.sleep(5)

        # starts at one-off purchase input
        starts_at_one_off_purchase_input = browser.find_element_by_xpath(
            "//input[@id='data_product_pricing_plan__starts_at_price']"
        )
        starts_at_one_off_purchase_input.clear()
        starts_at_one_off_purchase_input.send_keys("199.99")

        time.sleep(5)


class UnitTestsWebAutomationDataradePushComputerAidedDesingSoftware(unittest.TestCase):
    # ok
    def test_count_characters_for_cad_file_for_software(self):
        print('test_count_characters_for_cad_file_for_software')

        """
What makes a good product title?

Give your Data Product a title that is keyword search-optimized.

Great Data Product titles have 50 to 150 characters and ideally contain the following details:
- Your Brand Name
- Data Type
- Countries / Geographies
- Volume (e.g. 10M Devices, 5M companies, 20M consumers)
- Key Benefits (e.g.GDPR-compliant, real-time sourced, 10 years historic coverage)

Examples of search optimized Data Product titles:
- Datatrade’s USA C-level executives b2b contact data (e-mail, phone) w/ 300k records
- Datatrade’s Location Data for People Visits to large cities in the UK, 18 months API
- Datatrade’s ESG ratings of Middle East companies with 5 years of history - tickerized
        """
        pays = "Worldwide"

        patent_number = "US0000011111"

        url_google_patent = "https://www.googlepatents.com"

        title = "Holomorphe / Computer Aided Design Package / Free energy generator (Aether - Zero point energy) / Patent number : " \
                + patent_number + " / " + pays

        """
How does a good short description look?

This description will be shown on your Data Product card that appears on each filter page. 

Providing a short description of min. 100 characters helps spark further data buyer interest so that they want 
to learn more about it and view it in detail. 

We recommend including these points in your short description:
- Key benefits of your Data Product
- The main attributes of your data
- Coverage (industries, countries)
- Scale & quality indicators
        """
        short_description = "This computer aided design package has one STL file and one Python macro " \
                            "script used by FreeCAD software for building machines. This free energy generator " \
                            "can be viewed on the following link of this public patent : " + url_google_patent

        """
What does a good description look like?

The in-depth product description is your chance to engage with data buyers who want to fully understand a Data 
Product before requesting it. 

By adding search-optimized keywords in the text you can increase the visibility of your Data Products as well.

Try to answer the following questions in your in-depth description:
- What makes your data unique?
- How is the data generally sourced?
- What are the primary use-cases or verticals of this Data Product?
- How does this Data Product fit into your broader data offering ?

Great in-depth descriptions comprise several hundred words. 

Most top performing products on Datarade have a description length between 3000 and 6000 characters.
        """
        in_depth_description = "This computer aided design package product is efficient, affordable, valuable, " \
                               "reliable, flexible and portable. The work for this computer aided design package was " \
                               "made by a complex algorithm that uses Python language and FreeCAD software for " \
                               "designing all the parts and the assembly without clicking on the graphical user " \
                               "interface. This computer aided design package product was imagined by the needs of " \
                               "the global econnomy, the industrial needs and the energy needs without " \
                               "coal, oil, natural gas, wood, biomass, solar energy and wind energy. With this " \
                               "machine, we can fight against the global poverty worldwide in some months. " \
                               "The primary use-cases or verticals of this " \
                               "computer aided design package product are : electricity production, business " \
                               "strategy, business intelligence, international marketing, operations management, " \
                               "quality management, product management, industrial processes, manufacturing " \
                               "processes, ethnic marketing and product marketing."

        if 30 <= len(title) <= 150:
            print('title length is good : ' + str(len(title)))
        else:
            print('title length is bad : ' + str(len(title)))

        if 80 <= len(short_description) <= 300:
            print('short_description length is good : ' + str(len(short_description)))
        else:
            print('short_description length is bad : ' + str(len(short_description)))

        if 300 <= len(in_depth_description) <= 8000:
            print('in_depth_description length is good : ' + str(len(in_depth_description)))
        else:
            print('in_depth_description length is bad : ' + str(len(in_depth_description)))

    # ok
    def test_push_one_product_for_cad_file_for_patent_number_us_4661747(self):
        print("test_push_one_product_for_cad_file_for_patent_number_us_4661747")

        number_of_records = 2

        price = "9.99"

        pays = "Worldwide"

        patent_number = "US 4661747"

        holomorphe_viewer = "https://holomorphe.com/cad/patent_us_4661747"

        url_google_patent = "https://patents.google.com/patent/US4661747A/en?oq=US4661747"

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(5)

        # with Firefox
        browser = webdriver.Firefox(executable_path='..\\geckodriver.exe')

        time.sleep(20)

        # maximize window
        browser.maximize_window()

        time.sleep(10)

        # open
        browser.get('https://datarade.ai/')

        time.sleep(15)

        clear_button = browser.find_element_by_xpath("//button[@data-cf-action='reject'][@aria-label='Deny']")
        clear_button.click()

        time.sleep(5)

        sign_in_button = browser.find_element_by_xpath("//a[@class='navbar__item'][@href='/users/sign_in']")
        sign_in_button.click()

        time.sleep(15)

        work_email_input = browser.find_element_by_xpath("//input[@id='user__email'][@name='user[email]']")
        work_email_input.clear()
        work_email_input.send_keys(""
        "")

        time.sleep(5)

        passwrod_input = browser.find_element_by_xpath("//input[@id='user__password'][@name='user[password]']")
        passwrod_input.clear()
        passwrod_input.send_keys("")

        time.sleep(5)

        login_button = browser.find_element_by_xpath("//input[@type='submit'][@name='commit']")
        login_button.click()

        time.sleep(15)

        holomorphe_button = browser.find_element_by_xpath(
            "//a[@class='navbar__item tablet-landscape-hidden'][@href='/my/provider']")
        holomorphe_button.click()

        time.sleep(10)

        new_product_button = browser.find_element_by_xpath(
            "//a[@class='button primary modern small'][@href='/my/provider/data_products/new']")
        new_product_button.click()

        time.sleep(10)

        # 1.Basics
        # Type
        type_software_button = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[3]/div/div[2]/div[1]/div[2]"
        )
        type_software_button.click()

        time.sleep(5)

        # Title
        title_input = browser.find_element_by_xpath("//input[@id='data_product__name'][@name='data_product[name]']")
        title_input.clear()

        title = "Holomorphe / Computer Aided Design Package / Engineering Product / Patent number : " \
                + patent_number + " / " + pays

        title_input.send_keys(title)

        time.sleep(5)

        # Short Description
        short_description_input = browser.find_element_by_xpath(
            "//textarea[@id='data_product__short_description'][@name='data_product[short_description]']")
        short_description_input.clear()

        short_description = "This computer aided design package has one STL file and one Python macro " \
                            "script used by FreeCAD software for building machines. All the parts and the assembly " \
                            "are displayed on the following link : " + holomorphe_viewer

        short_description_input.send_keys(short_description)

        time.sleep(5)

        # In-depth Description
        in_depth_description_input = browser.find_element_by_xpath(
            "//textarea[@id='data_product__description'][@name='data_product[description]']")
        in_depth_description_input.clear()

        in_depth_description = "This computer aided design package product is efficient, affordable, valuable, " \
                               "reliable, flexible and portable. The work for this computer aided design package was " \
                               "made by a complex algorithm that uses Python language and FreeCAD software for " \
                               "designing all the parts and the assembly without clicking on the graphical user " \
                               "interface. This computer aided design package product was imagined by the needs of " \
                               "the global econnomy and the industrial needs. The primary use-cases or verticals of this " \
                               "computer aided design package product are : business strategy, business intelligence, " \
                               "international marketing, operations management, quality management, product management, " \
                               "ethnic marketing and product marketing. The patent is available on the following " \
                               "link : " + url_google_patent + "."

        in_depth_description_input.send_keys(in_depth_description)

        time.sleep(5)

        # 2.Listing
        listing_button = browser.find_element_by_xpath("//a[@data-tab='listing']")
        listing_button.click()

        time.sleep(5)

        data_catgory_1_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[1]/div/div"
        )
        data_catgory_1_select.click()

        time.sleep(5)

        data_catgory_1_value_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[1]/div/div/div[2]/div[4]"
        )
        data_catgory_1_value_select.click()

        time.sleep(5)

        data_catgory_2_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[2]/div/div"
        )
        data_catgory_2_select.click()

        time.sleep(5)

        data_catgory_2_value_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[2]/div/div/div[2]/div[6]"
        )
        data_catgory_2_value_select.click()

        time.sleep(5)

        data_catgory_3_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[3]/div/div"
        )
        data_catgory_3_select.click()

        time.sleep(5)

        data_catgory_3_value_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[3]/div/div/div[2]/div[15]"
        )
        data_catgory_3_value_select.click()

        time.sleep(5)

        data_catgory_4_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[4]/div/div"
        )
        data_catgory_4_select.click()

        time.sleep(5)

        data_catgory_4_value_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[4]/div/div/div[2]/div[20]"
        )
        data_catgory_4_value_select.click()

        time.sleep(5)

        data_catgory_5_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[5]/div/div"
        )
        data_catgory_5_select.click()

        time.sleep(5)

        data_catgory_5_value_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[5]/div/div/div[2]/div[34]"
        )
        data_catgory_5_value_select.click()

        time.sleep(5)

        # check the Small Business checkbox
        small_business_checkbox = browser.find_element_by_xpath(
            "//label[@for='data_product__company_size_ids-1']"
        )
        small_business_checkbox.click()

        time.sleep(5)

        # check the Medium-sized Business checkbox
        medium_sized_business_checkbox = browser.find_element_by_xpath(
            "//label[@for='data_product__company_size_ids-2']"
        )
        medium_sized_business_checkbox.click()

        time.sleep(5)

        # check the Entreprise checkbox
        entreprise_checkbox = browser.find_element_by_xpath(
            "//label[@for='data_product__company_size_ids-3']"
        )
        entreprise_checkbox.click()

        time.sleep(5)

        use_cases_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]"
        )
        use_cases_select.click()

        time.sleep(5)

        use_case_1_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[33]"
        )
        use_case_1_select.click()

        time.sleep(5)

        use_cases_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]"
        )
        use_cases_select.click()

        time.sleep(5)

        use_case_2_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[37]"
        )
        use_case_2_select.click()

        time.sleep(5)

        use_cases_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]"
        )
        use_cases_select.click()

        time.sleep(5)

        use_case_3_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[122]"
        )
        use_case_3_select.click()

        time.sleep(5)

        use_cases_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]"
        )
        use_cases_select.click()

        time.sleep(5)

        use_case_4_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[135]"
        )
        use_case_4_select.click()

        time.sleep(5)

        use_cases_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]"
        )
        use_cases_select.click()

        time.sleep(5)

        use_case_5_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[139]"
        )
        use_case_5_select.click()

        time.sleep(5)

        # 3. Coverage
        coverage_button = browser.find_element_by_xpath("//a[@data-tab='coverage']")
        coverage_button.click()

        time.sleep(5)

        africa_select = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[5]/div/div[2]/div[2]/div/div/div[1]"
        )
        africa_select.click()

        time.sleep(5)

        africa_select_all_button = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[5]/div/div[2]/div[2]/div/div/div[2]/button[1]"
        )
        africa_select_all_button.click()

        time.sleep(5)

        asia_select = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[5]/div/div[2]/div[2]/div/div/div[3]"
        )
        asia_select.click()

        time.sleep(5)

        asia_select_all_button = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[5]/div/div[2]/div[2]/div/div/div[4]/button[1]"
        )
        asia_select_all_button.click()

        time.sleep(5)

        europe_select = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[5]/div/div[2]/div[2]/div/div/div[5]"
        )
        europe_select.click()

        time.sleep(5)

        europe_select_all_button = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[5]/div/div[2]/div[2]/div/div/div[6]/button[1]"
        )
        europe_select_all_button.click()

        time.sleep(5)

        north_america_select = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[5]/div/div[2]/div[2]/div/div/div[7]"
        )
        north_america_select.click()

        time.sleep(5)

        north_america_select_all_button = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[5]/div/div[2]/div[2]/div/div/div[8]/button[1]"
        )
        north_america_select_all_button.click()

        time.sleep(5)

        south_america_select = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[5]/div/div[2]/div[2]/div/div/div[9]"
        )
        south_america_select.click()

        time.sleep(5)

        south_america_select_all_button = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[5]/div/div[2]/div[2]/div/div/div[10]/button[1]"
        )
        south_america_select_all_button.click()

        time.sleep(5)

        oceania_select = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[5]/div/div[2]/div[2]/div/div/div[11]"
        )
        oceania_select.click()

        time.sleep(5)

        oceania_select_all_button = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[5]/div/div[2]/div[2]/div/div/div[12]/button[1]"
        )
        oceania_select_all_button.click()

        time.sleep(5)

        others_select = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[5]/div/div[2]/div[2]/div/div/div[13]"
        )
        others_select.click()

        time.sleep(5)

        others_select_all_button = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[5]/div/div[2]/div[2]/div/div/div[14]/button[1]"
        )
        others_select_all_button.click()

        time.sleep(5)

        # Historical Coverage
        historical_coverage_input = browser.find_element_by_xpath(
            '//input[@id="data_product__history"]'
        )
        historical_coverage_input.clear()
        historical_coverage_input.send_keys("1")

        time.sleep(5)

        range_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[5]/div/div[2]/div[3]/div[2]/div"
        )
        range_select.click()

        time.sleep(5)

        weeks_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[5]/div/div[2]/div[3]/div[2]/div/div[2]/div[2]"
        )
        weeks_select.click()

        time.sleep(5)

        # 4. Volume and quality
        volume_and_quality_button = browser.find_element_by_xpath("//a[@data-tab='volume_and_quality']")
        volume_and_quality_button.click()

        time.sleep(5)

        # Add Volume
        add_volume_button = browser.find_element_by_xpath("//a[@data-association='volume']")
        add_volume_button.click()

        time.sleep(5)

        # Volume input
        volume_input = browser.find_element_by_xpath("//input[@id='data_product_volume__value'][@type='number']")
        volume_input.clear()
        volume_input.send_keys(str(number_of_records))

        time.sleep(5)

        # unit_input
        unit_input = browser.find_element_by_xpath("//input[@id='data_product_volume__unit'][@type='text']")
        unit_input.clear()
        unit_input.send_keys("files")

        time.sleep(5)

        # Add Quality Attribute
        add_quality_attribute_button = browser.find_element_by_xpath("//a[@data-association='quality']")
        add_quality_attribute_button.click()

        time.sleep(5)

        # quality in % input
        quality_input = browser.find_element_by_xpath("//input[@id='data_product_quality__percentage'][@type='number']")
        quality_input.clear()
        quality_input.send_keys("100")

        time.sleep(5)

        # unit quality input
        unit_quality_input = browser.find_element_by_xpath("//input[@id='data_product_quality__unit'][@type='text']")
        unit_quality_input.clear()
        unit_quality_input.send_keys("match rate")

        time.sleep(5)

        # 5. Attributes
        attributes_button = browser.find_element_by_xpath("//a[@data-tab='attributes']")
        attributes_button.click()

        time.sleep(5)

        # Add Attribute _ file
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(5)

        # name input
        name_input = browser.find_element_by_xpath(
            "//input[@id='data_product_attribute_spec__name']"
        )
        name_input.clear()
        name_input.send_keys("file")

        time.sleep(5)

        # example input
        example_input = browser.find_element_by_xpath(
            "//input[@id='data_product_attribute_spec__example']"
        )
        example_input.clear()
        example_input.send_keys("part_support")

        time.sleep(5)

        # description input
        description_input = browser.find_element_by_xpath(
            "//input[@id='data_product_attribute_spec__description']"
        )
        description_input.clear()
        description_input.send_keys("A STL file")

        time.sleep(5)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "//input[@id='data_product_attribute_spec__number_of_records']"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("One")

        time.sleep(5)

        # 6. Delivery
        delivery_button = browser.find_element_by_xpath("//a[@class='item'][@data-tab='delivery']")
        delivery_button.click()

        time.sleep(5)

        # Email checkbox
        email_checkbox = browser.find_element_by_xpath("//label[@for='data_product__transfer_method_ids-9']")
        email_checkbox.click()

        time.sleep(5)

        # Json checkbox
        json_checkbox = browser.find_element_by_xpath("//label[@for='data_product__data_format_ids-10']")
        json_checkbox.click()

        time.sleep(5)

        # on-demand checkbox
        on_demand_checkbox = browser.find_element_by_xpath("//label[@for='data_product__transfer_frequency_ids-10']")
        on_demand_checkbox.click()

        time.sleep(5)

        # 7. Pricing
        pricing_button = browser.find_element_by_xpath("//a[@data-tab='pricing']")
        pricing_button.click()

        time.sleep(5)

        # One-off purchase checkbox
        one_off_purchase_checkbox = browser.find_element_by_xpath(
            "//label[@for='data_product_pricing_plan__pricing_model_id-1']"
        )
        one_off_purchase_checkbox.click()

        time.sleep(5)

        # starts at one-off purchase input
        starts_at_one_off_purchase_input = browser.find_element_by_xpath(
            "//input[@id='data_product_pricing_plan__starts_at_price']"
        )
        starts_at_one_off_purchase_input.clear()
        starts_at_one_off_purchase_input.send_keys(str(price))

        time.sleep(5)

        currency_select = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[9]/div/div[2]/div[2]/div"
        )
        currency_select.click()

        time.sleep(5)

        eur_select = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[9]/div/div[2]/div[2]/div/div[2]/div[2]"
        )
        eur_select.click()

        time.sleep(5)

    # ok
    def test_push_one_product_for_cad_file_for_patent_number_us_6545444(self):
        print("test_push_one_product_for_cad_file_for_patent_number_us_6545444")

        ob = Screenshot_Clipping.Screenshot()

        number_of_records = 2

        price = "9.99"

        pays = "Worldwide"

        patent_number = "US6545444"

        url_google_patent = "https://patents.google.com/patent/US6545444B2/en?oq=US6545444"

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(5)

        # with Firefox
        browser = webdriver.Firefox(executable_path='..\\geckodriver.exe')

        time.sleep(20)

        # maximize window
        browser.maximize_window()

        time.sleep(10)

        # open
        browser.get('https://datarade.ai/')

        time.sleep(15)

        clear_button = browser.find_element_by_xpath("//button[@data-cf-action='reject'][@aria-label='Deny']")
        clear_button.click()

        time.sleep(5)

        sign_in_button = browser.find_element_by_xpath("//a[@class='navbar__item'][@href='/users/sign_in']")
        sign_in_button.click()

        time.sleep(15)

        work_email_input = browser.find_element_by_xpath("//input[@id='user__email'][@name='user[email]']")
        work_email_input.clear()
        work_email_input.send_keys(""
        "")

        time.sleep(5)

        passwrod_input = browser.find_element_by_xpath("//input[@id='user__password'][@name='user[password]']")
        passwrod_input.clear()
        passwrod_input.send_keys("")

        time.sleep(5)

        login_button = browser.find_element_by_xpath("//input[@type='submit'][@name='commit']")
        login_button.click()

        time.sleep(15)

        holomorphe_button = browser.find_element_by_xpath(
            "//a[@class='navbar__item tablet-landscape-hidden'][@href='/my/provider']")
        holomorphe_button.click()

        time.sleep(10)

        new_product_button = browser.find_element_by_xpath(
            "//a[@class='button primary modern small'][@href='/my/provider/data_products/new']")
        new_product_button.click()

        time.sleep(10)

        # 1.Basics
        # Type
        software_button = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[3]/div/div[2]/div[1]/div[2]/div/div"
        )
        software_button.click()

        time.sleep(5)

        # Title
        title_input = browser.find_element_by_xpath("//input[@id='data_product__name'][@name='data_product[name]']")
        title_input.clear()

        title = "Holomorphe / Computer Aided Design Package / Zero point energy generator (Aether) / Patent number : " \
                + patent_number + " / " + pays

        title_input.send_keys(title)

        time.sleep(5)

        # Short Description
        short_description_input = browser.find_element_by_xpath(
            "//textarea[@id='data_product__short_description'][@name='data_product[short_description]']")
        short_description_input.clear()

        short_description = "This computer aided design package has one STL file and one Python macro " \
                            "script used by FreeCAD software for building machines. This free energy generator " \
                            "can be viewed on the following link of this public patent : " + url_google_patent

        short_description_input.send_keys(short_description)

        time.sleep(5)

        # In-depth Description
        in_depth_description_input = browser.find_element_by_xpath(
            "//textarea[@id='data_product__description'][@name='data_product[description]']"
        )
        in_depth_description_input.clear()

        in_depth_description = "This computer aided design package product is efficient, affordable, valuable, " \
                               "reliable, flexible and portable. The work for this computer aided design package was " \
                               "made by a complex algorithm that uses Python language and FreeCAD software for " \
                               "designing all the parts and the assembly without clicking on the graphical user " \
                               "interface. This computer aided design package product was imagined by the needs of " \
                               "the global econnomy and the industrial needs. The primary use-cases or verticals of this " \
                               "computer aided design package product are : business strategy, business intelligence, " \
                               "international marketing, operations management, quality management, product management, " \
                               "ethnic marketing and product marketing."

        in_depth_description_input.send_keys(in_depth_description)

        time.sleep(5)

        # 2.Listing
        listing_button = browser.find_element_by_xpath("//a[@data-tab='listing']")
        listing_button.click()

        time.sleep(5)

        data_catgory_1_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[1]/div/div"
        )
        data_catgory_1_select.click()

        time.sleep(5)

        data_catgory_1_value_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[1]/div/div/div[2]/div[4]"
        )
        data_catgory_1_value_select.click()

        time.sleep(5)

        data_catgory_2_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[2]/div/div"
        )
        data_catgory_2_select.click()

        time.sleep(5)

        data_catgory_2_value_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[2]/div/div/div[2]/div[6]"
        )
        data_catgory_2_value_select.click()

        time.sleep(5)

        data_catgory_3_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[3]/div/div"
        )
        data_catgory_3_select.click()

        time.sleep(5)

        data_catgory_3_value_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[3]/div/div/div[2]/div[15]"
        )
        data_catgory_3_value_select.click()

        time.sleep(5)

        data_catgory_4_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[4]/div/div"
        )
        data_catgory_4_select.click()

        time.sleep(5)

        data_catgory_4_value_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[4]/div/div/div[2]/div[20]"
        )
        data_catgory_4_value_select.click()

        time.sleep(5)

        data_catgory_5_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[5]/div/div"
        )
        data_catgory_5_select.click()

        time.sleep(5)

        data_catgory_5_value_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[5]/div/div/div[2]/div[34]"
        )
        data_catgory_5_value_select.click()

        time.sleep(5)

        # check the Small Business checkbox
        small_business_checkbox = browser.find_element_by_xpath(
            "//label[@for='data_product__company_size_ids-1']"
        )
        small_business_checkbox.click()

        time.sleep(5)

        # check the Medium-sized Business checkbox
        medium_sized_business_checkbox = browser.find_element_by_xpath(
            "//label[@for='data_product__company_size_ids-2']"
        )
        medium_sized_business_checkbox.click()

        time.sleep(5)

        # check the Entreprise checkbox
        entreprise_checkbox = browser.find_element_by_xpath(
            "//label[@for='data_product__company_size_ids-3']"
        )
        entreprise_checkbox.click()

        time.sleep(5)

        use_cases_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]"
        )
        use_cases_select.click()

        time.sleep(5)

        use_case_1_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[33]"
        )
        use_case_1_select.click()

        time.sleep(5)

        use_cases_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]"
        )
        use_cases_select.click()

        time.sleep(5)

        use_case_2_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[37]"
        )
        use_case_2_select.click()

        time.sleep(5)

        use_cases_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]"
        )
        use_cases_select.click()

        time.sleep(5)

        use_case_3_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[122]"
        )
        use_case_3_select.click()

        time.sleep(5)

        use_cases_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]"
        )
        use_cases_select.click()

        time.sleep(5)

        use_case_4_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[135]"
        )
        use_case_4_select.click()

        time.sleep(5)

        use_cases_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]"
        )
        use_cases_select.click()

        time.sleep(5)

        use_case_5_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[139]"
        )
        use_case_5_select.click()

        time.sleep(5)

        # 3. Coverage
        coverage_button = browser.find_element_by_xpath("//a[@data-tab='coverage']")
        coverage_button.click()

        time.sleep(5)

        africa_select = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[5]/div/div[2]/div[2]/div/div/div[1]"
        )
        africa_select.click()

        time.sleep(5)

        africa_select_all_button = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[5]/div/div[2]/div[2]/div/div/div[2]/button[1]"
        )
        africa_select_all_button.click()

        time.sleep(5)

        asia_select = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[5]/div/div[2]/div[2]/div/div/div[3]"
        )
        asia_select.click()

        time.sleep(5)

        asia_select_all_button = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[5]/div/div[2]/div[2]/div/div/div[4]/button[1]"
        )
        asia_select_all_button.click()

        time.sleep(5)

        europe_select = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[5]/div/div[2]/div[2]/div/div/div[5]"
        )
        europe_select.click()

        time.sleep(5)

        europe_select_all_button = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[5]/div/div[2]/div[2]/div/div/div[6]/button[1]"
        )
        europe_select_all_button.click()

        time.sleep(5)

        north_america_select = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[5]/div/div[2]/div[2]/div/div/div[7]"
        )
        north_america_select.click()

        time.sleep(5)

        north_america_select_all_button = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[5]/div/div[2]/div[2]/div/div/div[8]/button[1]"
        )
        north_america_select_all_button.click()

        time.sleep(5)

        south_america_select = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[5]/div/div[2]/div[2]/div/div/div[9]"
        )
        south_america_select.click()

        time.sleep(5)

        south_america_select_all_button = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[5]/div/div[2]/div[2]/div/div/div[10]/button[1]"
        )
        south_america_select_all_button.click()

        time.sleep(5)

        oceania_select = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[5]/div/div[2]/div[2]/div/div/div[11]"
        )
        oceania_select.click()

        time.sleep(5)

        oceania_select_all_button = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[5]/div/div[2]/div[2]/div/div/div[12]/button[1]"
        )
        oceania_select_all_button.click()

        time.sleep(5)

        others_select = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[5]/div/div[2]/div[2]/div/div/div[13]"
        )
        others_select.click()

        time.sleep(5)

        others_select_all_button = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[5]/div/div[2]/div[2]/div/div/div[14]/button[1]"
        )
        others_select_all_button.click()

        time.sleep(5)

        # Historical Coverage
        historical_coverage_input = browser.find_element_by_xpath(
            '//input[@id="data_product__history"]'
        )
        historical_coverage_input.clear()
        historical_coverage_input.send_keys("1")

        time.sleep(5)

        range_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[5]/div/div[2]/div[3]/div[2]/div"
        )
        range_select.click()

        time.sleep(5)

        weeks_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[5]/div/div[2]/div[3]/div[2]/div/div[2]/div[2]"
        )
        weeks_select.click()

        time.sleep(5)

        # 4. Volume and quality
        volume_and_quality_button = browser.find_element_by_xpath("//a[@data-tab='volume_and_quality']")
        volume_and_quality_button.click()

        time.sleep(5)

        # Add Volume
        add_volume_button = browser.find_element_by_xpath("//a[@data-association='volume']")
        add_volume_button.click()

        time.sleep(5)

        # Volume input
        volume_input = browser.find_element_by_xpath("//input[@id='data_product_volume__value'][@type='number']")
        volume_input.clear()
        volume_input.send_keys(str(number_of_records))

        time.sleep(5)

        # unit_input
        unit_input = browser.find_element_by_xpath("//input[@id='data_product_volume__unit'][@type='text']")
        unit_input.clear()
        unit_input.send_keys("files")

        time.sleep(5)

        # Add Quality Attribute
        add_quality_attribute_button = browser.find_element_by_xpath("//a[@data-association='quality']")
        add_quality_attribute_button.click()

        time.sleep(5)

        # quality in % input
        quality_input = browser.find_element_by_xpath("//input[@id='data_product_quality__percentage'][@type='number']")
        quality_input.clear()
        quality_input.send_keys("100")

        time.sleep(5)

        # unit quality input
        unit_quality_input = browser.find_element_by_xpath("//input[@id='data_product_quality__unit'][@type='text']")
        unit_quality_input.clear()
        unit_quality_input.send_keys("match rate")

        time.sleep(5)

        # 5. Attributes
        attributes_button = browser.find_element_by_xpath("//a[@data-tab='attributes']")
        attributes_button.click()

        time.sleep(5)

        # Add Attribute _ file
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(5)

        # name input
        name_input = browser.find_element_by_xpath(
            "//input[@id='data_product_attribute_spec__name']"
        )
        name_input.clear()
        name_input.send_keys("file")

        time.sleep(5)

        # example input
        example_input = browser.find_element_by_xpath(
            "//input[@id='data_product_attribute_spec__example']"
        )
        example_input.clear()
        example_input.send_keys("part_support")

        time.sleep(5)

        # description input
        description_input = browser.find_element_by_xpath(
            "//input[@id='data_product_attribute_spec__description']"
        )
        description_input.clear()
        description_input.send_keys("A STL file")

        time.sleep(5)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "//input[@id='data_product_attribute_spec__number_of_records']"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("One")

        time.sleep(5)

        # 6. Delivery
        delivery_button = browser.find_element_by_xpath("//a[@class='item'][@data-tab='delivery']")
        delivery_button.click()

        time.sleep(5)

        # Email checkbox
        email_checkbox = browser.find_element_by_xpath("//label[@for='data_product__transfer_method_ids-9']")
        email_checkbox.click()

        time.sleep(5)

        # Json checkbox
        json_checkbox = browser.find_element_by_xpath("//label[@for='data_product__data_format_ids-10']")
        json_checkbox.click()

        time.sleep(5)

        # on-demand checkbox
        on_demand_checkbox = browser.find_element_by_xpath("//label[@for='data_product__transfer_frequency_ids-10']")
        on_demand_checkbox.click()

        time.sleep(5)

        # 7. Pricing
        pricing_button = browser.find_element_by_xpath("//a[@data-tab='pricing']")
        pricing_button.click()

        time.sleep(5)

        # One-off purchase checkbox
        one_off_purchase_checkbox = browser.find_element_by_xpath(
            "//label[@for='data_product_pricing_plan__pricing_model_id-1']"
        )
        one_off_purchase_checkbox.click()

        time.sleep(5)

        # starts at one-off purchase input
        starts_at_one_off_purchase_input = browser.find_element_by_xpath(
            "//input[@id='data_product_pricing_plan__starts_at_price']"
        )
        starts_at_one_off_purchase_input.clear()
        starts_at_one_off_purchase_input.send_keys(str(price))

        time.sleep(5)

        currency_select = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[9]/div/div[2]/div[2]/div"
        )
        currency_select.click()

        time.sleep(5)

        eur_select = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[9]/div/div[2]/div[2]/div/div[2]/div[2]"
        )
        eur_select.click()

        time.sleep(5)

        # Create Product
        create_product_button = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[1]/div/button"
        )
        create_product_button.click()

        time.sleep(5)

        full_path_folder = "A:\\1_Professionnel\\1_Holomorphe\\2_Archives\\8_Marketing\\1_Clients\\2_Logiciels" \
                           "\\1_Datarade_[Non_Mail]\\4_Softwares"

        ob.full_Screenshot(browser, save_path=full_path_folder, image_name=patent_number + '.png')

        time.sleep(7)

        # Click on my profile
        profile_button = browser.find_element_by_xpath(
            "/html/body/div/header/div/div/nav[2]/a/div"
        )
        profile_button.click()

        time.sleep(7)

        # Click on the "logout" button
        logout_button = browser.find_element_by_xpath(
            "/html/body/div/header/div/div/nav[2]/div[2]/div[2]/div[1]/div/a"
        )
        logout_button.click()

        time.sleep(7)

        browser.close()

    # ok
    def test_push_one_product_for_cad_file_for_patent_number_us_20020125774A1(self):
        print("test_push_one_product_for_cad_file_for_patent_number_us_20020125774A1")

        ob = Screenshot_Clipping.Screenshot()

        number_of_records = 2

        price = "9.99"

        pays = "Worldwide"

        patent_number = "US20020125774A1"

        url_google_patent = "https://patents.google.com/patent/US20020125774A1/en?oq=US20020125774A1"

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(5)

        # with Firefox
        options = Options()
        options.headless = True
        browser = webdriver.Firefox(executable_path='..\\geckodriver.exe', options=options)

        time.sleep(20)

        # maximize window
        browser.maximize_window()

        time.sleep(10)

        # open
        browser.get('https://datarade.ai/')
        print('open')

        time.sleep(15)

        clear_button = browser.find_element_by_xpath("//button[@data-cf-action='reject'][@aria-label='Deny']")
        clear_button.click()

        time.sleep(5)

        sign_in_button = browser.find_element_by_xpath("//a[@class='navbar__item'][@href='/users/sign_in']")
        sign_in_button.click()

        time.sleep(15)

        work_email_input = browser.find_element_by_xpath("//input[@id='user__email'][@name='user[email]']")
        work_email_input.clear()
        work_email_input.send_keys(""
        "")

        time.sleep(5)

        passwrod_input = browser.find_element_by_xpath("//input[@id='user__password'][@name='user[password]']")
        passwrod_input.clear()
        passwrod_input.send_keys("")

        time.sleep(5)

        login_button = browser.find_element_by_xpath("//input[@type='submit'][@name='commit']")
        login_button.click()

        time.sleep(15)

        print('conected')

        holomorphe_button = browser.find_element_by_xpath(
            "//a[@class='navbar__item tablet-landscape-hidden'][@href='/my/provider']")
        holomorphe_button.click()

        time.sleep(10)

        new_product_button = browser.find_element_by_xpath(
            "//a[@class='button primary modern small'][@href='/my/provider/data_products/new']")
        new_product_button.click()

        time.sleep(10)

        # 1.Basics
        print('1.Basics')

        # Type
        software_button = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[3]/div/div[2]/div[1]/div[2]/div/div"
        )
        software_button.click()

        time.sleep(5)

        # Title
        title_input = browser.find_element_by_xpath("//input[@id='data_product__name'][@name='data_product[name]']")
        title_input.clear()

        title = "Holomorphe / Computer Aided Design Package / Zero point energy generator (Aether) / Patent number : " \
                + patent_number + " / " + pays

        title_input.send_keys(title)

        time.sleep(5)

        # Short Description
        short_description_input = browser.find_element_by_xpath(
            "//textarea[@id='data_product__short_description'][@name='data_product[short_description]']")
        short_description_input.clear()

        short_description = "This computer aided design package has one STL file and one Python macro " \
                            "script used by FreeCAD software for building machines. This free energy generator " \
                            "can be viewed on the following link of this public patent : " + url_google_patent

        short_description_input.send_keys(short_description)

        time.sleep(5)

        # In-depth Description
        in_depth_description_input = browser.find_element_by_xpath(
            "//textarea[@id='data_product__description'][@name='data_product[description]']"
        )
        in_depth_description_input.clear()

        in_depth_description = "This computer aided design package product is efficient, affordable, valuable, " \
                               "reliable, flexible and portable. The work for this computer aided design package was " \
                               "made by a complex algorithm that uses Python language and FreeCAD software for " \
                               "designing all the parts and the assembly without clicking on the graphical user " \
                               "interface. This computer aided design package product was imagined by the needs of " \
                               "the global econnomy and the industrial needs. The primary use-cases or verticals of this " \
                               "computer aided design package product are : business strategy, business intelligence, " \
                               "international marketing, operations management, quality management, product management, " \
                               "ethnic marketing and product marketing."

        in_depth_description_input.send_keys(in_depth_description)

        time.sleep(5)

        # 2.Listing
        print('2.Listing')

        listing_button = browser.find_element_by_xpath("//a[@data-tab='listing']")
        listing_button.click()

        time.sleep(5)

        data_catgory_1_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[1]/div/div"
        )
        data_catgory_1_select.click()

        time.sleep(5)

        data_catgory_1_value_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[1]/div/div/div[2]/div[4]"
        )
        data_catgory_1_value_select.click()

        time.sleep(5)

        data_catgory_2_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[2]/div/div"
        )
        data_catgory_2_select.click()

        time.sleep(5)

        data_catgory_2_value_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[2]/div/div/div[2]/div[6]"
        )
        data_catgory_2_value_select.click()

        time.sleep(5)

        data_catgory_3_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[3]/div/div"
        )
        data_catgory_3_select.click()

        time.sleep(5)

        data_catgory_3_value_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[3]/div/div/div[2]/div[15]"
        )
        data_catgory_3_value_select.click()

        time.sleep(5)

        data_catgory_4_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[4]/div/div"
        )
        data_catgory_4_select.click()

        time.sleep(5)

        data_catgory_4_value_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[4]/div/div/div[2]/div[20]"
        )
        data_catgory_4_value_select.click()

        time.sleep(5)

        data_catgory_5_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[5]/div/div"
        )
        data_catgory_5_select.click()

        time.sleep(5)

        data_catgory_5_value_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[5]/div/div/div[2]/div[34]"
        )
        data_catgory_5_value_select.click()

        time.sleep(5)

        # check the Small Business checkbox
        small_business_checkbox = browser.find_element_by_xpath(
            "//label[@for='data_product__company_size_ids-1']"
        )
        small_business_checkbox.click()

        time.sleep(5)

        # check the Medium-sized Business checkbox
        medium_sized_business_checkbox = browser.find_element_by_xpath(
            "//label[@for='data_product__company_size_ids-2']"
        )
        medium_sized_business_checkbox.click()

        time.sleep(5)

        # check the Entreprise checkbox
        entreprise_checkbox = browser.find_element_by_xpath(
            "//label[@for='data_product__company_size_ids-3']"
        )
        entreprise_checkbox.click()

        time.sleep(5)

        use_cases_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]"
        )
        use_cases_select.click()

        time.sleep(5)

        use_case_1_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[33]"
        )
        use_case_1_select.click()

        time.sleep(5)

        use_cases_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]"
        )
        use_cases_select.click()

        time.sleep(5)

        use_case_2_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[37]"
        )
        use_case_2_select.click()

        time.sleep(5)

        use_cases_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]"
        )
        use_cases_select.click()

        time.sleep(5)

        use_case_3_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[122]"
        )
        use_case_3_select.click()

        time.sleep(5)

        use_cases_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]"
        )
        use_cases_select.click()

        time.sleep(5)

        use_case_4_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[135]"
        )
        use_case_4_select.click()

        time.sleep(5)

        use_cases_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]"
        )
        use_cases_select.click()

        time.sleep(5)

        use_case_5_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[139]"
        )
        use_case_5_select.click()

        time.sleep(5)

        # 3. Coverage
        print('3.Coverage')

        coverage_button = browser.find_element_by_xpath("//a[@data-tab='coverage']")
        coverage_button.click()

        time.sleep(5)

        africa_select = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[5]/div/div[2]/div[2]/div/div/div[1]"
        )
        africa_select.click()

        time.sleep(5)

        africa_select_all_button = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[5]/div/div[2]/div[2]/div/div/div[2]/button[1]"
        )
        africa_select_all_button.click()

        time.sleep(5)

        asia_select = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[5]/div/div[2]/div[2]/div/div/div[3]"
        )
        asia_select.click()

        time.sleep(5)

        asia_select_all_button = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[5]/div/div[2]/div[2]/div/div/div[4]/button[1]"
        )
        asia_select_all_button.click()

        time.sleep(5)

        europe_select = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[5]/div/div[2]/div[2]/div/div/div[5]"
        )
        europe_select.click()

        time.sleep(5)

        europe_select_all_button = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[5]/div/div[2]/div[2]/div/div/div[6]/button[1]"
        )
        europe_select_all_button.click()

        time.sleep(5)

        north_america_select = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[5]/div/div[2]/div[2]/div/div/div[7]"
        )
        north_america_select.click()

        time.sleep(5)

        north_america_select_all_button = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[5]/div/div[2]/div[2]/div/div/div[8]/button[1]"
        )
        north_america_select_all_button.click()

        time.sleep(5)

        south_america_select = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[5]/div/div[2]/div[2]/div/div/div[9]"
        )
        south_america_select.click()

        time.sleep(5)

        south_america_select_all_button = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[5]/div/div[2]/div[2]/div/div/div[10]/button[1]"
        )
        south_america_select_all_button.click()

        time.sleep(5)

        oceania_select = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[5]/div/div[2]/div[2]/div/div/div[11]"
        )
        oceania_select.click()

        time.sleep(5)

        oceania_select_all_button = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[5]/div/div[2]/div[2]/div/div/div[12]/button[1]"
        )
        oceania_select_all_button.click()

        time.sleep(5)

        others_select = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[5]/div/div[2]/div[2]/div/div/div[13]"
        )
        others_select.click()

        time.sleep(5)

        others_select_all_button = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[5]/div/div[2]/div[2]/div/div/div[14]/button[1]"
        )
        others_select_all_button.click()

        time.sleep(5)

        # Historical Coverage
        historical_coverage_input = browser.find_element_by_xpath(
            '//input[@id="data_product__history"]'
        )
        historical_coverage_input.clear()
        historical_coverage_input.send_keys("1")

        time.sleep(5)

        range_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[5]/div/div[2]/div[3]/div[2]/div"
        )
        range_select.click()

        time.sleep(5)

        weeks_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[5]/div/div[2]/div[3]/div[2]/div/div[2]/div[2]"
        )
        weeks_select.click()

        time.sleep(5)

        # 4.Volume and quality
        print('4.Volume and quality')

        volume_and_quality_button = browser.find_element_by_xpath("//a[@data-tab='volume_and_quality']")
        volume_and_quality_button.click()

        time.sleep(5)

        # Add Volume
        add_volume_button = browser.find_element_by_xpath("//a[@data-association='volume']")
        add_volume_button.click()

        time.sleep(5)

        # Volume input
        volume_input = browser.find_element_by_xpath("//input[@id='data_product_volume__value'][@type='number']")
        volume_input.clear()
        volume_input.send_keys(str(number_of_records))

        time.sleep(5)

        # unit_input
        unit_input = browser.find_element_by_xpath("//input[@id='data_product_volume__unit'][@type='text']")
        unit_input.clear()
        unit_input.send_keys("files")

        time.sleep(5)

        # Add Quality Attribute
        add_quality_attribute_button = browser.find_element_by_xpath("//a[@data-association='quality']")
        add_quality_attribute_button.click()

        time.sleep(5)

        # quality in % input
        quality_input = browser.find_element_by_xpath("//input[@id='data_product_quality__percentage'][@type='number']")
        quality_input.clear()
        quality_input.send_keys("100")

        time.sleep(5)

        # unit quality input
        unit_quality_input = browser.find_element_by_xpath("//input[@id='data_product_quality__unit'][@type='text']")
        unit_quality_input.clear()
        unit_quality_input.send_keys("match rate")

        time.sleep(5)

        # 5.Attributes
        print('5.Attributes')

        attributes_button = browser.find_element_by_xpath("//a[@data-tab='attributes']")
        attributes_button.click()

        time.sleep(5)

        # Add Attribute _ file
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(5)

        # name input
        name_input = browser.find_element_by_xpath(
            "//input[@id='data_product_attribute_spec__name']"
        )
        name_input.clear()
        name_input.send_keys("file")

        time.sleep(5)

        # example input
        example_input = browser.find_element_by_xpath(
            "//input[@id='data_product_attribute_spec__example']"
        )
        example_input.clear()
        example_input.send_keys("part_support")

        time.sleep(5)

        # description input
        description_input = browser.find_element_by_xpath(
            "//input[@id='data_product_attribute_spec__description']"
        )
        description_input.clear()
        description_input.send_keys("A STL file")

        time.sleep(5)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "//input[@id='data_product_attribute_spec__number_of_records']"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("One")

        time.sleep(5)

        # 6.Delivery
        print("6.Delivery")

        delivery_button = browser.find_element_by_xpath("//a[@class='item'][@data-tab='delivery']")
        delivery_button.click()

        time.sleep(5)

        # Email checkbox
        email_checkbox = browser.find_element_by_xpath("//label[@for='data_product__transfer_method_ids-9']")
        email_checkbox.click()

        time.sleep(5)

        # Json checkbox
        json_checkbox = browser.find_element_by_xpath("//label[@for='data_product__data_format_ids-10']")
        json_checkbox.click()

        time.sleep(5)

        # on-demand checkbox
        on_demand_checkbox = browser.find_element_by_xpath("//label[@for='data_product__transfer_frequency_ids-10']")
        on_demand_checkbox.click()

        time.sleep(5)

        # 7.Pricing
        print("7.Pricing")

        pricing_button = browser.find_element_by_xpath("//a[@data-tab='pricing']")
        pricing_button.click()

        time.sleep(5)

        # One-off purchase checkbox
        one_off_purchase_checkbox = browser.find_element_by_xpath(
            "//label[@for='data_product_pricing_plan__pricing_model_id-1']"
        )
        one_off_purchase_checkbox.click()

        time.sleep(5)

        # starts at one-off purchase input
        starts_at_one_off_purchase_input = browser.find_element_by_xpath(
            "//input[@id='data_product_pricing_plan__starts_at_price']"
        )
        starts_at_one_off_purchase_input.clear()
        starts_at_one_off_purchase_input.send_keys(str(price))

        time.sleep(5)

        currency_select = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[9]/div/div[2]/div[2]/div"
        )
        currency_select.click()

        time.sleep(5)

        eur_select = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[9]/div/div[2]/div[2]/div/div[2]/div[2]"
        )
        eur_select.click()

        time.sleep(5)

        # Create Product
        create_product_button = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[1]/div/button"
        )
        create_product_button.click()

        time.sleep(5)

        full_path_folder = "A:\\1_Professionnel\\1_Holomorphe\\2_Archives\\8_Marketing\\1_Clients\\2_Logiciels" \
                           "\\1_Datarade_[Non_Mail]\\4_Softwares"

        ob.full_Screenshot(browser, save_path=full_path_folder, image_name=patent_number + '.png')

        time.sleep(7)

        print("Software product created : " + patent_number)

        # Click on my profile
        profile_button = browser.find_element_by_xpath(
            "/html/body/div/header/div/div/nav[2]/a/div"
        )
        profile_button.click()

        time.sleep(7)

        # Click on the "logout" button
        logout_button = browser.find_element_by_xpath(
            "/html/body/div/header/div/div/nav[2]/div[2]/div[2]/div[1]/div/a"
        )
        logout_button.click()

        time.sleep(7)

        browser.close()

        print("disconnected")

    # ok
    def test_push_one_product_for_cad_file_for_patent_number_us_5957(self):
        print("test_push_one_product_for_cad_file_for_patent_number_us_5957")

        ob = Screenshot_Clipping.Screenshot()

        number_of_records = 2

        price = "9.99"

        pays = "Worldwide"

        patent_number = "US5957"

        url_google_patent = "https://patents.google.com/patent/US5957A/en?oq=US5957"

        print("patent_number : " + patent_number)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(5)

        # with Firefox
        options = Options()
        options.headless = True
        browser = webdriver.Firefox(executable_path='..\\geckodriver.exe', options=options)

        time.sleep(20)

        # maximize window
        browser.maximize_window()

        time.sleep(10)

        # open
        browser.get('https://datarade.ai/')
        print('open')

        time.sleep(15)

        clear_button = browser.find_element_by_xpath("//button[@data-cf-action='reject'][@aria-label='Deny']")
        clear_button.click()

        time.sleep(5)

        sign_in_button = browser.find_element_by_xpath("//a[@class='navbar__item'][@href='/users/sign_in']")
        sign_in_button.click()

        time.sleep(15)

        work_email_input = browser.find_element_by_xpath("//input[@id='user__email'][@name='user[email]']")
        work_email_input.clear()
        work_email_input.send_keys(""
        "")

        time.sleep(5)

        passwrod_input = browser.find_element_by_xpath("//input[@id='user__password'][@name='user[password]']")
        passwrod_input.clear()
        passwrod_input.send_keys("")

        time.sleep(5)

        login_button = browser.find_element_by_xpath("//input[@type='submit'][@name='commit']")
        login_button.click()

        time.sleep(15)

        print('conected')

        holomorphe_button = browser.find_element_by_xpath(
            "//a[@class='navbar__item tablet-landscape-hidden'][@href='/my/provider']")
        holomorphe_button.click()

        time.sleep(10)

        new_product_button = browser.find_element_by_xpath(
            "//a[@class='button primary modern small'][@href='/my/provider/data_products/new']")
        new_product_button.click()

        time.sleep(10)

        # 1.Basics
        print('1.Basics')

        # Type
        software_button = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[3]/div/div[2]/div[1]/div[2]/div/div"
        )
        software_button.click()

        time.sleep(5)

        # Title
        title_input = browser.find_element_by_xpath("//input[@id='data_product__name'][@name='data_product[name]']")
        title_input.clear()

        title = "Holomorphe / Computer Aided Design Package / Free energy generator (Aether - Zero point energy) " \
                "/ Patent number : " + patent_number + " / " + pays

        title_input.send_keys(title)

        time.sleep(5)

        # Short Description
        short_description_input = browser.find_element_by_xpath(
            "//textarea[@id='data_product__short_description'][@name='data_product[short_description]']")
        short_description_input.clear()

        short_description = "This computer aided design package has one STL file and one Python macro " \
                            "script used by FreeCAD software for building machines. This free energy generator " \
                            "can be viewed on the following link of this public patent : " + url_google_patent

        short_description_input.send_keys(short_description)

        time.sleep(5)

        # In-depth Description
        in_depth_description_input = browser.find_element_by_xpath(
            "//textarea[@id='data_product__description'][@name='data_product[description]']"
        )
        in_depth_description_input.clear()

        in_depth_description = "This computer aided design package product is efficient, affordable, valuable, " \
                               "reliable, flexible and portable. The work for this computer aided design package was " \
                               "made by a complex algorithm that uses Python language and FreeCAD software for " \
                               "designing all the parts and the assembly without clicking on the graphical user " \
                               "interface. This computer aided design package product was imagined by the needs of " \
                               "the global econnomy, the industrial needs and the energy needs without " \
                               "coal, oil, natural gas, wood, biomass, solar energy and wind energy. With this " \
                               "machine, we can fight against the global poverty worldwide in some months. " \
                               "The primary use-cases or verticals of this " \
                               "computer aided design package product are : electricity production, business " \
                               "strategy, business intelligence, international marketing, operations management, " \
                               "quality management, product management, industrial processes, manufacturing " \
                               "processes, ethnic marketing and product marketing."

        in_depth_description_input.send_keys(in_depth_description)

        time.sleep(5)

        # 2.Listing
        print('2.Listing')

        listing_button = browser.find_element_by_xpath("//a[@data-tab='listing']")
        listing_button.click()

        time.sleep(5)

        data_catgory_1_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[1]/div/div"
        )
        data_catgory_1_select.click()

        time.sleep(5)

        data_catgory_1_value_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[1]/div/div/div[2]/div[4]"
        )
        data_catgory_1_value_select.click()

        time.sleep(5)

        data_catgory_2_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[2]/div/div"
        )
        data_catgory_2_select.click()

        time.sleep(5)

        data_catgory_2_value_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[2]/div/div/div[2]/div[6]"
        )
        data_catgory_2_value_select.click()

        time.sleep(5)

        data_catgory_3_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[3]/div/div"
        )
        data_catgory_3_select.click()

        time.sleep(5)

        data_catgory_3_value_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[3]/div/div/div[2]/div[15]"
        )
        data_catgory_3_value_select.click()

        time.sleep(5)

        data_catgory_4_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[4]/div/div"
        )
        data_catgory_4_select.click()

        time.sleep(5)

        data_catgory_4_value_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[4]/div/div/div[2]/div[20]"
        )
        data_catgory_4_value_select.click()

        time.sleep(5)

        data_catgory_5_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[5]/div/div"
        )
        data_catgory_5_select.click()

        time.sleep(5)

        data_catgory_5_value_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[5]/div/div/div[2]/div[34]"
        )
        data_catgory_5_value_select.click()

        time.sleep(5)

        # check the Small Business checkbox
        small_business_checkbox = browser.find_element_by_xpath(
            "//label[@for='data_product__company_size_ids-1']"
        )
        small_business_checkbox.click()

        time.sleep(5)

        # check the Medium-sized Business checkbox
        medium_sized_business_checkbox = browser.find_element_by_xpath(
            "//label[@for='data_product__company_size_ids-2']"
        )
        medium_sized_business_checkbox.click()

        time.sleep(5)

        # check the Entreprise checkbox
        entreprise_checkbox = browser.find_element_by_xpath(
            "//label[@for='data_product__company_size_ids-3']"
        )
        entreprise_checkbox.click()

        time.sleep(5)

        use_cases_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]"
        )
        use_cases_select.click()

        time.sleep(5)

        use_case_1_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[33]"
        )
        use_case_1_select.click()

        time.sleep(5)

        use_cases_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]"
        )
        use_cases_select.click()

        time.sleep(5)

        use_case_2_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[37]"
        )
        use_case_2_select.click()

        time.sleep(5)

        use_cases_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]"
        )
        use_cases_select.click()

        time.sleep(5)

        use_case_3_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[122]"
        )
        use_case_3_select.click()

        time.sleep(5)

        use_cases_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]"
        )
        use_cases_select.click()

        time.sleep(5)

        use_case_4_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[135]"
        )
        use_case_4_select.click()

        time.sleep(5)

        use_cases_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]"
        )
        use_cases_select.click()

        time.sleep(5)

        use_case_5_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[139]"
        )
        use_case_5_select.click()

        time.sleep(5)

        # 3. Coverage
        print('3.Coverage')

        coverage_button = browser.find_element_by_xpath("//a[@data-tab='coverage']")
        coverage_button.click()

        time.sleep(5)

        africa_select = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[5]/div/div[2]/div[2]/div/div/div[1]"
        )
        africa_select.click()

        time.sleep(5)

        africa_select_all_button = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[5]/div/div[2]/div[2]/div/div/div[2]/button[1]"
        )
        africa_select_all_button.click()

        time.sleep(5)

        asia_select = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[5]/div/div[2]/div[2]/div/div/div[3]"
        )
        asia_select.click()

        time.sleep(5)

        asia_select_all_button = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[5]/div/div[2]/div[2]/div/div/div[4]/button[1]"
        )
        asia_select_all_button.click()

        time.sleep(5)

        europe_select = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[5]/div/div[2]/div[2]/div/div/div[5]"
        )
        europe_select.click()

        time.sleep(5)

        europe_select_all_button = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[5]/div/div[2]/div[2]/div/div/div[6]/button[1]"
        )
        europe_select_all_button.click()

        time.sleep(5)

        north_america_select = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[5]/div/div[2]/div[2]/div/div/div[7]"
        )
        north_america_select.click()

        time.sleep(5)

        north_america_select_all_button = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[5]/div/div[2]/div[2]/div/div/div[8]/button[1]"
        )
        north_america_select_all_button.click()

        time.sleep(5)

        south_america_select = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[5]/div/div[2]/div[2]/div/div/div[9]"
        )
        south_america_select.click()

        time.sleep(5)

        south_america_select_all_button = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[5]/div/div[2]/div[2]/div/div/div[10]/button[1]"
        )
        south_america_select_all_button.click()

        time.sleep(5)

        oceania_select = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[5]/div/div[2]/div[2]/div/div/div[11]"
        )
        oceania_select.click()

        time.sleep(5)

        oceania_select_all_button = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[5]/div/div[2]/div[2]/div/div/div[12]/button[1]"
        )
        oceania_select_all_button.click()

        time.sleep(5)

        others_select = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[5]/div/div[2]/div[2]/div/div/div[13]"
        )
        others_select.click()

        time.sleep(5)

        others_select_all_button = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[5]/div/div[2]/div[2]/div/div/div[14]/button[1]"
        )
        others_select_all_button.click()

        time.sleep(5)

        # Historical Coverage
        historical_coverage_input = browser.find_element_by_xpath(
            '//input[@id="data_product__history"]'
        )
        historical_coverage_input.clear()
        historical_coverage_input.send_keys("1")

        time.sleep(5)

        range_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[5]/div/div[2]/div[3]/div[2]/div"
        )
        range_select.click()

        time.sleep(5)

        weeks_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[5]/div/div[2]/div[3]/div[2]/div/div[2]/div[2]"
        )
        weeks_select.click()

        time.sleep(5)

        # 4.Volume and quality
        print('4.Volume and quality')

        volume_and_quality_button = browser.find_element_by_xpath("//a[@data-tab='volume_and_quality']")
        volume_and_quality_button.click()

        time.sleep(5)

        # Add Volume
        add_volume_button = browser.find_element_by_xpath("//a[@data-association='volume']")
        add_volume_button.click()

        time.sleep(5)

        # Volume input
        volume_input = browser.find_element_by_xpath("//input[@id='data_product_volume__value'][@type='number']")
        volume_input.clear()
        volume_input.send_keys(str(number_of_records))

        time.sleep(5)

        # unit_input
        unit_input = browser.find_element_by_xpath("//input[@id='data_product_volume__unit'][@type='text']")
        unit_input.clear()
        unit_input.send_keys("files")

        time.sleep(5)

        # Add Quality Attribute
        add_quality_attribute_button = browser.find_element_by_xpath("//a[@data-association='quality']")
        add_quality_attribute_button.click()

        time.sleep(5)

        # quality in % input
        quality_input = browser.find_element_by_xpath("//input[@id='data_product_quality__percentage'][@type='number']")
        quality_input.clear()
        quality_input.send_keys("100")

        time.sleep(5)

        # unit quality input
        unit_quality_input = browser.find_element_by_xpath("//input[@id='data_product_quality__unit'][@type='text']")
        unit_quality_input.clear()
        unit_quality_input.send_keys("match rate")

        time.sleep(5)

        # 5.Attributes
        print('5.Attributes')

        attributes_button = browser.find_element_by_xpath("//a[@data-tab='attributes']")
        attributes_button.click()

        time.sleep(5)

        # Add Attribute _ file
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(5)

        # name input
        name_input = browser.find_element_by_xpath(
            "//input[@id='data_product_attribute_spec__name']"
        )
        name_input.clear()
        name_input.send_keys("file")

        time.sleep(5)

        # example input
        example_input = browser.find_element_by_xpath(
            "//input[@id='data_product_attribute_spec__example']"
        )
        example_input.clear()
        example_input.send_keys("part_support")

        time.sleep(5)

        # description input
        description_input = browser.find_element_by_xpath(
            "//input[@id='data_product_attribute_spec__description']"
        )
        description_input.clear()
        description_input.send_keys("A STL file")

        time.sleep(5)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "//input[@id='data_product_attribute_spec__number_of_records']"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("One")

        time.sleep(5)

        # 6.Delivery
        print("6.Delivery")

        delivery_button = browser.find_element_by_xpath("//a[@class='item'][@data-tab='delivery']")
        delivery_button.click()

        time.sleep(5)

        # Email checkbox
        email_checkbox = browser.find_element_by_xpath("//label[@for='data_product__transfer_method_ids-9']")
        email_checkbox.click()

        time.sleep(5)

        # Json checkbox
        json_checkbox = browser.find_element_by_xpath("//label[@for='data_product__data_format_ids-10']")
        json_checkbox.click()

        time.sleep(5)

        # on-demand checkbox
        on_demand_checkbox = browser.find_element_by_xpath("//label[@for='data_product__transfer_frequency_ids-10']")
        on_demand_checkbox.click()

        time.sleep(5)

        # 7.Pricing
        print("7.Pricing")

        pricing_button = browser.find_element_by_xpath("//a[@data-tab='pricing']")
        pricing_button.click()

        time.sleep(5)

        # One-off purchase checkbox
        one_off_purchase_checkbox = browser.find_element_by_xpath(
            "//label[@for='data_product_pricing_plan__pricing_model_id-1']"
        )
        one_off_purchase_checkbox.click()

        time.sleep(5)

        # starts at one-off purchase input
        starts_at_one_off_purchase_input = browser.find_element_by_xpath(
            "//input[@id='data_product_pricing_plan__starts_at_price']"
        )
        starts_at_one_off_purchase_input.clear()
        starts_at_one_off_purchase_input.send_keys(str(price))

        time.sleep(5)

        currency_select = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[9]/div/div[2]/div[2]/div"
        )
        currency_select.click()

        time.sleep(5)

        eur_select = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[9]/div/div[2]/div[2]/div/div[2]/div[2]"
        )
        eur_select.click()

        time.sleep(5)

        # Create Product
        create_product_button = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[1]/div/button"
        )
        create_product_button.click()

        time.sleep(10)

        # full_Screenshot
        full_path_folder = "A:\\1_Professionnel\\1_Holomorphe\\2_Archives\\8_Marketing\\1_Clients\\2_Logiciels" \
                           "\\1_Datarade_[Non_Mail]\\4_Softwares"

        ob.full_Screenshot(browser, save_path=full_path_folder, image_name=patent_number + '.png')

        time.sleep(10)

        print("Software product created : " + patent_number)

        # Click on my profile
        profile_button = browser.find_element_by_xpath(
            "/html/body/div/header/div/div/nav[2]/a/div"
        )
        profile_button.click()

        time.sleep(7)

        # Click on the "logout" button
        logout_button = browser.find_element_by_xpath(
            "/html/body/div/header/div/div/nav[2]/div[2]/div[2]/div[1]/div/a"
        )
        logout_button.click()

        time.sleep(7)

        browser.close()

        print("disconnected")

        time.sleep(15)

    # ok
    def test_push_one_product_for_cad_file_for_patent_number_from_mysql_database_patents(self):
        print("test_push_one_product_for_cad_file_for_patent_number_from_mysql_database_patents")

        connection = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            password='8h0NEJkEf3lyCBUoPQwCHSu@@@@@@@',
            db='patents',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )

        try:
            with connection.cursor() as cursor:
                try:
                    sql = """
                    SELECT DISTINCT * FROM `free_energy_inventions`
                    """

                    cursor.execute(sql)

                    results = cursor.fetchall()

                    number_of_patent = len(results)

                    for i in range(0, number_of_patent):
                        print("patent numero : " + str(i))

                        ob = Screenshot_Clipping.Screenshot()

                        number_of_records = 2

                        price = "9.99"

                        pays = "Worldwide"

                        patent_number = str(results[i].get('patent_number'))

                        url_google_patent = str(results[i].get('url_patent'))

                        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

                        time.sleep(5)

                        # with Firefox
                        options = Options()
                        options.headless = True
                        browser = webdriver.Firefox(executable_path='..\\geckodriver.exe', options=options)

                        time.sleep(20)

                        # maximize window
                        browser.maximize_window()

                        time.sleep(10)

                        # open
                        browser.get('https://datarade.ai/')
                        print('open')

                        time.sleep(15)

                        clear_button = browser.find_element_by_xpath(
                            "//button[@data-cf-action='reject'][@aria-label='Deny']")
                        clear_button.click()

                        time.sleep(5)

                        sign_in_button = browser.find_element_by_xpath(
                            "//a[@class='navbar__item'][@href='/users/sign_in']")
                        sign_in_button.click()

                        time.sleep(15)

                        work_email_input = browser.find_element_by_xpath(
                            "//input[@id='user__email'][@name='user[email]']")
                        work_email_input.clear()
                        work_email_input.send_keys(""
                        "")

                        time.sleep(5)

                        passwrod_input = browser.find_element_by_xpath(
                            "//input[@id='user__password'][@name='user[password]']")
                        passwrod_input.clear()
                        passwrod_input.send_keys("")

                        time.sleep(5)

                        login_button = browser.find_element_by_xpath("//input[@type='submit'][@name='commit']")
                        login_button.click()

                        time.sleep(15)

                        print('conected')

                        # new product
                        browser.get('')

                        # 1.Basics
                        print('1.Basics')

                        # Type
                        software_button = browser.find_element_by_xpath(
                            "/html/body/div[1]/main/div/div/form/div[3]/div/div[2]/div[1]/div[2]/div/div"
                        )
                        software_button.click()

                        time.sleep(5)

                        # Title
                        title_input = browser.find_element_by_xpath(
                            "//input[@id='data_product__name'][@name='data_product[name]']")
                        title_input.clear()

                        title = "Holomorphe / Computer Aided Design Package / Free energy generator (Aether - Zero point energy) " \
                                "/ Patent number : " + patent_number + " / " + pays

                        title_input.send_keys(title)

                        time.sleep(5)

                        # Short Description
                        short_description_input = browser.find_element_by_xpath(
                            "//textarea[@id='data_product__short_description'][@name='data_product[short_description]']")
                        short_description_input.clear()

                        short_description = "This computer aided design package has one STL file and one Python macro " \
                                            "script used by FreeCAD software for building machines. This free energy generator " \
                                            "can be viewed on the following link of this public patent : " + url_google_patent

                        short_description_input.send_keys(short_description)

                        time.sleep(5)

                        # In-depth Description
                        in_depth_description_input = browser.find_element_by_xpath(
                            "//textarea[@id='data_product__description'][@name='data_product[description]']"
                        )
                        in_depth_description_input.clear()

                        in_depth_description = "This computer aided design package product is efficient, affordable, valuable, " \
                                               "reliable, flexible and portable. The work for this computer aided design package was " \
                                               "made by a complex algorithm that uses Python language and FreeCAD software for " \
                                               "designing all the parts and the assembly without clicking on the graphical user " \
                                               "interface. This computer aided design package product was imagined by the needs of " \
                                               "the global econnomy, the industrial needs and the energy needs without " \
                                               "coal, oil, natural gas, wood, biomass, solar energy and wind energy. With this " \
                                               "machine, we can fight against the global poverty worldwide in some months. " \
                                               "The primary use-cases or verticals of this " \
                                               "computer aided design package product are : electricity production, business " \
                                               "strategy, business intelligence, international marketing, operations management, " \
                                               "quality management, product management, industrial processes, manufacturing " \
                                               "processes, ethnic marketing and product marketing."

                        in_depth_description_input.send_keys(in_depth_description)

                        time.sleep(5)

                        # 2.Listing
                        print('2.Listing')

                        listing_button = browser.find_element_by_xpath("//a[@data-tab='listing']")
                        listing_button.click()

                        time.sleep(5)

                        data_catgory_1_select = browser.find_element_by_xpath(
                            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[1]/div/div"
                        )
                        data_catgory_1_select.click()

                        time.sleep(5)

                        data_catgory_1_value_select = browser.find_element_by_xpath(
                            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[1]/div/div/div[2]/div[4]"
                        )
                        data_catgory_1_value_select.click()

                        time.sleep(5)

                        data_catgory_2_select = browser.find_element_by_xpath(
                            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[2]/div/div"
                        )
                        data_catgory_2_select.click()

                        time.sleep(5)

                        data_catgory_2_value_select = browser.find_element_by_xpath(
                            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[2]/div/div/div[2]/div[6]"
                        )
                        data_catgory_2_value_select.click()

                        time.sleep(5)

                        data_catgory_3_select = browser.find_element_by_xpath(
                            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[3]/div/div"
                        )
                        data_catgory_3_select.click()

                        time.sleep(5)

                        data_catgory_3_value_select = browser.find_element_by_xpath(
                            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[3]/div/div/div[2]/div[15]"
                        )
                        data_catgory_3_value_select.click()

                        time.sleep(5)

                        data_catgory_4_select = browser.find_element_by_xpath(
                            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[4]/div/div"
                        )
                        data_catgory_4_select.click()

                        time.sleep(5)

                        data_catgory_4_value_select = browser.find_element_by_xpath(
                            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[4]/div/div/div[2]/div[20]"
                        )
                        data_catgory_4_value_select.click()

                        time.sleep(5)

                        data_catgory_5_select = browser.find_element_by_xpath(
                            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[5]/div/div"
                        )
                        data_catgory_5_select.click()

                        time.sleep(5)

                        data_catgory_5_value_select = browser.find_element_by_xpath(
                            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[5]/div/div/div[2]/div[34]"
                        )
                        data_catgory_5_value_select.click()

                        time.sleep(5)

                        # check the Small Business checkbox
                        small_business_checkbox = browser.find_element_by_xpath(
                            "//label[@for='data_product__company_size_ids-1']"
                        )
                        small_business_checkbox.click()

                        time.sleep(5)

                        # check the Medium-sized Business checkbox
                        medium_sized_business_checkbox = browser.find_element_by_xpath(
                            "//label[@for='data_product__company_size_ids-2']"
                        )
                        medium_sized_business_checkbox.click()

                        time.sleep(5)

                        # check the Entreprise checkbox
                        entreprise_checkbox = browser.find_element_by_xpath(
                            "//label[@for='data_product__company_size_ids-3']"
                        )
                        entreprise_checkbox.click()

                        time.sleep(5)

                        use_cases_select = browser.find_element_by_xpath(
                            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]"
                        )
                        use_cases_select.click()

                        time.sleep(5)

                        use_case_1_select = browser.find_element_by_xpath(
                            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[33]"
                        )
                        use_case_1_select.click()

                        time.sleep(5)

                        use_cases_select = browser.find_element_by_xpath(
                            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]"
                        )
                        use_cases_select.click()

                        time.sleep(5)

                        use_case_2_select = browser.find_element_by_xpath(
                            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[37]"
                        )
                        use_case_2_select.click()

                        time.sleep(5)

                        use_cases_select = browser.find_element_by_xpath(
                            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]"
                        )
                        use_cases_select.click()

                        time.sleep(5)

                        use_case_3_select = browser.find_element_by_xpath(
                            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[122]"
                        )
                        use_case_3_select.click()

                        time.sleep(5)

                        use_cases_select = browser.find_element_by_xpath(
                            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]"
                        )
                        use_cases_select.click()

                        time.sleep(5)

                        use_case_4_select = browser.find_element_by_xpath(
                            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[135]"
                        )
                        use_case_4_select.click()

                        time.sleep(5)

                        use_cases_select = browser.find_element_by_xpath(
                            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]"
                        )
                        use_cases_select.click()

                        time.sleep(5)

                        use_case_5_select = browser.find_element_by_xpath(
                            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[139]"
                        )
                        use_case_5_select.click()

                        time.sleep(5)

                        # 3. Coverage
                        print('3.Coverage')

                        coverage_button = browser.find_element_by_xpath("//a[@data-tab='coverage']")
                        coverage_button.click()

                        time.sleep(5)

                        africa_select = browser.find_element_by_xpath(
                            "/html/body/div/main/div/div/form/div[5]/div/div[2]/div[2]/div/div/div[1]"
                        )
                        africa_select.click()

                        time.sleep(5)

                        africa_select_all_button = browser.find_element_by_xpath(
                            "/html/body/div/main/div/div/form/div[5]/div/div[2]/div[2]/div/div/div[2]/button[1]"
                        )
                        africa_select_all_button.click()

                        time.sleep(5)

                        asia_select = browser.find_element_by_xpath(
                            "/html/body/div/main/div/div/form/div[5]/div/div[2]/div[2]/div/div/div[3]"
                        )
                        asia_select.click()

                        time.sleep(5)

                        asia_select_all_button = browser.find_element_by_xpath(
                            "/html/body/div/main/div/div/form/div[5]/div/div[2]/div[2]/div/div/div[4]/button[1]"
                        )
                        asia_select_all_button.click()

                        time.sleep(5)

                        europe_select = browser.find_element_by_xpath(
                            "/html/body/div/main/div/div/form/div[5]/div/div[2]/div[2]/div/div/div[5]"
                        )
                        europe_select.click()

                        time.sleep(5)

                        europe_select_all_button = browser.find_element_by_xpath(
                            "/html/body/div/main/div/div/form/div[5]/div/div[2]/div[2]/div/div/div[6]/button[1]"
                        )
                        europe_select_all_button.click()

                        time.sleep(5)

                        north_america_select = browser.find_element_by_xpath(
                            "/html/body/div/main/div/div/form/div[5]/div/div[2]/div[2]/div/div/div[7]"
                        )
                        north_america_select.click()

                        time.sleep(5)

                        north_america_select_all_button = browser.find_element_by_xpath(
                            "/html/body/div/main/div/div/form/div[5]/div/div[2]/div[2]/div/div/div[8]/button[1]"
                        )
                        north_america_select_all_button.click()

                        time.sleep(5)

                        south_america_select = browser.find_element_by_xpath(
                            "/html/body/div/main/div/div/form/div[5]/div/div[2]/div[2]/div/div/div[9]"
                        )
                        south_america_select.click()

                        time.sleep(5)

                        south_america_select_all_button = browser.find_element_by_xpath(
                            "/html/body/div/main/div/div/form/div[5]/div/div[2]/div[2]/div/div/div[10]/button[1]"
                        )
                        south_america_select_all_button.click()

                        time.sleep(5)

                        oceania_select = browser.find_element_by_xpath(
                            "/html/body/div/main/div/div/form/div[5]/div/div[2]/div[2]/div/div/div[11]"
                        )
                        oceania_select.click()

                        time.sleep(5)

                        oceania_select_all_button = browser.find_element_by_xpath(
                            "/html/body/div/main/div/div/form/div[5]/div/div[2]/div[2]/div/div/div[12]/button[1]"
                        )
                        oceania_select_all_button.click()

                        time.sleep(5)

                        others_select = browser.find_element_by_xpath(
                            "/html/body/div/main/div/div/form/div[5]/div/div[2]/div[2]/div/div/div[13]"
                        )
                        others_select.click()

                        time.sleep(5)

                        others_select_all_button = browser.find_element_by_xpath(
                            "/html/body/div/main/div/div/form/div[5]/div/div[2]/div[2]/div/div/div[14]/button[1]"
                        )
                        others_select_all_button.click()

                        time.sleep(5)

                        # Historical Coverage
                        historical_coverage_input = browser.find_element_by_xpath(
                            '//input[@id="data_product__history"]'
                        )
                        historical_coverage_input.clear()
                        historical_coverage_input.send_keys("1")

                        time.sleep(5)

                        range_select = browser.find_element_by_xpath(
                            "/html/body/div[1]/main/div/div/form/div[5]/div/div[2]/div[3]/div[2]/div"
                        )
                        range_select.click()

                        time.sleep(5)

                        weeks_select = browser.find_element_by_xpath(
                            "/html/body/div[1]/main/div/div/form/div[5]/div/div[2]/div[3]/div[2]/div/div[2]/div[2]"
                        )
                        weeks_select.click()

                        time.sleep(5)

                        # 4.Volume and quality
                        print('4.Volume and quality')

                        volume_and_quality_button = browser.find_element_by_xpath("//a[@data-tab='volume_and_quality']")
                        volume_and_quality_button.click()

                        time.sleep(5)

                        # Add Volume
                        add_volume_button = browser.find_element_by_xpath("//a[@data-association='volume']")
                        add_volume_button.click()

                        time.sleep(5)

                        # Volume input
                        volume_input = browser.find_element_by_xpath(
                            "//input[@id='data_product_volume__value'][@type='number']")
                        volume_input.clear()
                        volume_input.send_keys(str(number_of_records))

                        time.sleep(5)

                        # unit_input
                        unit_input = browser.find_element_by_xpath(
                            "//input[@id='data_product_volume__unit'][@type='text']")
                        unit_input.clear()
                        unit_input.send_keys("files")

                        time.sleep(5)

                        # Add Quality Attribute
                        add_quality_attribute_button = browser.find_element_by_xpath("//a[@data-association='quality']")
                        add_quality_attribute_button.click()

                        time.sleep(5)

                        # quality in % input
                        quality_input = browser.find_element_by_xpath(
                            "//input[@id='data_product_quality__percentage'][@type='number']")
                        quality_input.clear()
                        quality_input.send_keys("100")

                        time.sleep(5)

                        # unit quality input
                        unit_quality_input = browser.find_element_by_xpath(
                            "//input[@id='data_product_quality__unit'][@type='text']")
                        unit_quality_input.clear()
                        unit_quality_input.send_keys("match rate")

                        time.sleep(5)

                        # 5.Attributes
                        print('5.Attributes')

                        attributes_button = browser.find_element_by_xpath("//a[@data-tab='attributes']")
                        attributes_button.click()

                        time.sleep(5)

                        # Add Attribute _ file
                        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
                        add_attribute_button.click()

                        time.sleep(5)

                        # name input
                        name_input = browser.find_element_by_xpath(
                            "//input[@id='data_product_attribute_spec__name']"
                        )
                        name_input.clear()
                        name_input.send_keys("file")

                        time.sleep(5)

                        # example input
                        example_input = browser.find_element_by_xpath(
                            "//input[@id='data_product_attribute_spec__example']"
                        )
                        example_input.clear()
                        example_input.send_keys("part_support")

                        time.sleep(5)

                        # description input
                        description_input = browser.find_element_by_xpath(
                            "//input[@id='data_product_attribute_spec__description']"
                        )
                        description_input.clear()
                        description_input.send_keys("A STL file")

                        time.sleep(5)

                        # number of Records input
                        number_of_records_input = browser.find_element_by_xpath(
                            "//input[@id='data_product_attribute_spec__number_of_records']"
                        )
                        number_of_records_input.clear()
                        number_of_records_input.send_keys("One")

                        time.sleep(5)

                        # 6.Delivery
                        print("6.Delivery")

                        delivery_button = browser.find_element_by_xpath("//a[@class='item'][@data-tab='delivery']")
                        delivery_button.click()

                        time.sleep(5)

                        # Email checkbox
                        email_checkbox = browser.find_element_by_xpath(
                            "//label[@for='data_product__transfer_method_ids-9']")
                        email_checkbox.click()

                        time.sleep(5)

                        # Json checkbox
                        json_checkbox = browser.find_element_by_xpath(
                            "//label[@for='data_product__data_format_ids-10']")
                        json_checkbox.click()

                        time.sleep(5)

                        # on-demand checkbox
                        on_demand_checkbox = browser.find_element_by_xpath(
                            "//label[@for='data_product__transfer_frequency_ids-10']")
                        on_demand_checkbox.click()

                        time.sleep(5)

                        # 7.Pricing
                        print("7.Pricing")

                        pricing_button = browser.find_element_by_xpath("//a[@data-tab='pricing']")
                        pricing_button.click()

                        time.sleep(5)

                        # One-off purchase checkbox
                        one_off_purchase_checkbox = browser.find_element_by_xpath(
                            "//label[@for='data_product_pricing_plan__pricing_model_id-1']"
                        )
                        one_off_purchase_checkbox.click()

                        time.sleep(5)

                        # starts at one-off purchase input
                        starts_at_one_off_purchase_input = browser.find_element_by_xpath(
                            "//input[@id='data_product_pricing_plan__starts_at_price']"
                        )
                        starts_at_one_off_purchase_input.clear()
                        starts_at_one_off_purchase_input.send_keys(str(price))

                        time.sleep(5)

                        currency_select = browser.find_element_by_xpath(
                            "/html/body/div/main/div/div/form/div[9]/div/div[2]/div[2]/div"
                        )
                        currency_select.click()

                        time.sleep(5)

                        eur_select = browser.find_element_by_xpath(
                            "/html/body/div/main/div/div/form/div[9]/div/div[2]/div[2]/div/div[2]/div[2]"
                        )
                        eur_select.click()

                        time.sleep(5)

                        # Create Product
                        create_product_button = browser.find_element_by_xpath(
                            "/html/body/div/main/div/div/form/div[1]/div/button"
                        )
                        create_product_button.click()

                        time.sleep(10)

                        # full_Screenshot
                        full_path_folder = "A:\\1_Professionnel\\1_Holomorphe\\2_Archives\\8_Marketing\\1_Clients\\2_Logiciels" \
                                           "\\1_Datarade_[Non_Mail]\\4_Softwares"

                        ob.full_Screenshot(browser, save_path=full_path_folder, image_name=patent_number + '.png')

                        time.sleep(10)

                        print("Software product created : " + patent_number)

                        # Click on my profile
                        profile_button = browser.find_element_by_xpath(
                            "/html/body/div/header/div/div/nav[2]/a/div"
                        )
                        profile_button.click()

                        time.sleep(7)

                        # Click on the "logout" button
                        logout_button = browser.find_element_by_xpath(
                            "/html/body/div/header/div/div/nav[2]/div[2]/div[2]/div[1]/div/a"
                        )
                        logout_button.click()

                        time.sleep(7)

                        browser.close()

                        print("disconnected")

                        time.sleep(15)

                        print('\n')

                        print("ccleaner running")
                        os.system("set ccleaner='C:\\Program Files\\CCleaner\\CCleaner.exe'")
                        os.system("start ccleaner /AUTO")

                        time.sleep(60)
                except Exception as e:
                    print("There is an error : " + str(e))
        finally:
            connection.close()
            print('done')


class UnitTestsWebAutomationDataradePushElectronicDesignAutomationSoftware(unittest.TestCase):
    # ok
    def test_count_characters_for_eda_file_for_software(self):
        print('test_count_characters_for_eda_file_for_software')

        """
What makes a good product title?

Give your Data Product a title that is keyword search-optimized.

Great Data Product titles have 50 to 150 characters and ideally contain the following details:
- Your Brand Name
- Data Type
- Countries / Geographies
- Volume (e.g. 10M Devices, 5M companies, 20M consumers)
- Key Benefits (e.g.GDPR-compliant, real-time sourced, 10 years historic coverage)

Examples of search optimized Data Product titles:
- Datatrade’s USA C-level executives b2b contact data (e-mail, phone) w/ 300k records
- Datatrade’s Location Data for People Visits to large cities in the UK, 18 months API
- Datatrade’s ESG ratings of Middle East companies with 5 years of history - tickerized
        """
        pays = "Worldwide"

        patent_number = "US 0000011111"

        holomorphe_viewer = "https://www.holomorphe.com"

        url_google_patent = "https://www.googlepatents.com"

        title = "Holomorphe / Electronic Design Automation Package / Engineering Product / Patent number : " \
                + patent_number + " / " + pays

        """
How does a good short description look?

This description will be shown on your Data Product card that appears on each filter page. 

Providing a short description of min. 100 characters helps spark further data buyer interest so that they want 
to learn more about it and view it in detail. 

We recommend including these points in your short description:
- Key benefits of your Data Product
- The main attributes of your data
- Coverage (industries, countries)
- Scale & quality indicators
        """
        short_description = "This electronic design automation package has one gerber file and one Python macro " \
                            "script used by Skidl software for building netlist. All the components and the circuit " \
                            "are displayed on the following link : " + holomorphe_viewer

        """
What does a good description look like?

The in-depth product description is your chance to engage with data buyers who want to fully understand a Data 
Product before requesting it. 

By adding search-optimized keywords in the text you can increase the visibility of your Data Products as well.

Try to answer the following questions in your in-depth description:
- What makes your data unique?
- How is the data generally sourced?
- What are the primary use-cases or verticals of this Data Product?
- How does this Data Product fit into your broader data offering ?

Great in-depth descriptions comprise several hundred words. 

Most top performing products on Datarade have a description length between 3000 and 6000 characters.
        """
        in_depth_description = "This electronic design automation package product is efficient, affordable, valuable, " \
                               "reliable, flexible and portable. The work for this computer aided design package was " \
                               "made by a complex algorithm that uses Python language and FreeCAD software for " \
                               "designing all the parts and the assembly without clicking on the graphical user " \
                               "interface. This electronic design automation package product was imagined by the needs of " \
                               "the global econnomy and the industrial needs. The primary use-cases or verticals of this " \
                               "computer aided design package product are : business strategy, business intelligence, " \
                               "international marketing, operations management, quality management, product management, " \
                               "ethnic marketing and product marketing. The patent is available on the following " \
                               "link : " + url_google_patent + "."

        if 30 <= len(title) <= 150:
            print('title length is good : ' + str(len(title)))
        else:
            print('title length is bad : ' + str(len(title)))

        if 80 <= len(short_description) <= 300:
            print('short_description length is good : ' + str(len(short_description)))
        else:
            print('short_description length is bad : ' + str(len(short_description)))

        if 300 <= len(in_depth_description) <= 8000:
            print('in_depth_description length is good : ' + str(len(in_depth_description)))
        else:
            print('in_depth_description length is bad : ' + str(len(in_depth_description)))

    #
    def test_push_one_product_for_eda_file_for_patent_number_us_2470118(self):
        print("test_push_one_product_for_eda_file_for_patent_number_us_2470118")

        number_of_records = 2

        price = "9.99"

        pays = "Worldwide"

        patent_number = "US 2470118"

        holomorphe_viewer = "https://holomorphe.com/eda/patent_us_2470118"

        url_google_patent = "https://patents.google.com/patent/US2470118A/en?oq=US2470118"

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(5)

        # with Firefox
        browser = webdriver.Firefox(executable_path='..\\geckodriver.exe')

        time.sleep(20)

        # maximize window
        browser.maximize_window()

        time.sleep(10)

        # open
        browser.get('https://datarade.ai/')

        time.sleep(15)

        clear_button = browser.find_element_by_xpath("//button[@data-cf-action='reject'][@aria-label='Deny']")
        clear_button.click()

        time.sleep(5)

        sign_in_button = browser.find_element_by_xpath("//a[@class='navbar__item'][@href='/users/sign_in']")
        sign_in_button.click()

        time.sleep(15)

        work_email_input = browser.find_element_by_xpath("//input[@id='user__email'][@name='user[email]']")
        work_email_input.clear()
        work_email_input.send_keys(""
        "")

        time.sleep(5)

        passwrod_input = browser.find_element_by_xpath("//input[@id='user__password'][@name='user[password]']")
        passwrod_input.clear()
        passwrod_input.send_keys("")

        time.sleep(5)

        login_button = browser.find_element_by_xpath("//input[@type='submit'][@name='commit']")
        login_button.click()

        time.sleep(15)

        holomorphe_button = browser.find_element_by_xpath(
            "//a[@class='navbar__item tablet-landscape-hidden'][@href='/my/provider']")
        holomorphe_button.click()

        time.sleep(10)

        new_product_button = browser.find_element_by_xpath(
            "//a[@class='button primary modern small'][@href='/my/provider/data_products/new']")
        new_product_button.click()

        time.sleep(10)

        # 1.Basics
        # Type
        software_button = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[3]/div/div[2]/div[1]/div[2]/div/div"
        )
        software_button.click()

        time.sleep(5)

        # Title
        title_input = browser.find_element_by_xpath("//input[@id='data_product__name'][@name='data_product[name]']")
        title_input.clear()

        title = "Holomorphe / Electronic Design Automation Package / Engineering Product / Patent number : " \
                + patent_number + " / " + pays

        title_input.send_keys(title)

        time.sleep(5)

        # Short Description
        short_description_input = browser.find_element_by_xpath(
            "//textarea[@id='data_product__short_description'][@name='data_product[short_description]']")
        short_description_input.clear()

        short_description = "This electronic design automation package has one gerber file and one Python macro " \
                            "script used by Skidl software for building netlist. All the components and the circuit " \
                            "are displayed on the following link : " + holomorphe_viewer

        short_description_input.send_keys(short_description)

        time.sleep(5)

        # In-depth Description
        in_depth_description_input = browser.find_element_by_xpath(
            "//textarea[@id='data_product__description'][@name='data_product[description]']")
        in_depth_description_input.clear()

        in_depth_description = "This electronic design automation package product is efficient, affordable, valuable, " \
                               "reliable, flexible and portable. The work for this computer aided design package was " \
                               "made by a complex algorithm that uses Python language and FreeCAD software for " \
                               "designing all the parts and the assembly without clicking on the graphical user " \
                               "interface. This electronic design automation package product was imagined by the needs of " \
                               "the global econnomy and the industrial needs. The primary use-cases or verticals of this " \
                               "computer aided design package product are : business strategy, business intelligence, " \
                               "international marketing, operations management, quality management, product management, " \
                               "ethnic marketing and product marketing. The patent is available on the following " \
                               "link : " + url_google_patent + "."

        in_depth_description_input.send_keys(in_depth_description)

        time.sleep(5)

        # 2.Listing
        listing_button = browser.find_element_by_xpath("//a[@data-tab='listing']")
        listing_button.click()

        time.sleep(5)

        data_catgory_1_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[1]/div/div"
        )
        data_catgory_1_select.click()

        time.sleep(5)

        data_catgory_1_value_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[1]/div/div/div[2]/div[4]"
        )
        data_catgory_1_value_select.click()

        time.sleep(5)

        data_catgory_2_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[2]/div/div"
        )
        data_catgory_2_select.click()

        time.sleep(5)

        data_catgory_2_value_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[2]/div/div/div[2]/div[6]"
        )
        data_catgory_2_value_select.click()

        time.sleep(5)

        data_catgory_3_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[3]/div/div"
        )
        data_catgory_3_select.click()

        time.sleep(5)

        data_catgory_3_value_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[3]/div/div/div[2]/div[15]"
        )
        data_catgory_3_value_select.click()

        time.sleep(5)

        data_catgory_4_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[4]/div/div"
        )
        data_catgory_4_select.click()

        time.sleep(5)

        data_catgory_4_value_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[4]/div/div/div[2]/div[20]"
        )
        data_catgory_4_value_select.click()

        time.sleep(5)

        data_catgory_5_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[5]/div/div"
        )
        data_catgory_5_select.click()

        time.sleep(5)

        data_catgory_5_value_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[5]/div/div/div[2]/div[34]"
        )
        data_catgory_5_value_select.click()

        time.sleep(5)

        # check the Small Business checkbox
        small_business_checkbox = browser.find_element_by_xpath(
            "//label[@for='data_product__company_size_ids-1']"
        )
        small_business_checkbox.click()

        time.sleep(5)

        # check the Medium-sized Business checkbox
        medium_sized_business_checkbox = browser.find_element_by_xpath(
            "//label[@for='data_product__company_size_ids-2']"
        )
        medium_sized_business_checkbox.click()

        time.sleep(5)

        # check the Entreprise checkbox
        entreprise_checkbox = browser.find_element_by_xpath(
            "//label[@for='data_product__company_size_ids-3']"
        )
        entreprise_checkbox.click()

        time.sleep(5)

        use_cases_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]"
        )
        use_cases_select.click()

        time.sleep(5)

        use_case_1_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[33]"
        )
        use_case_1_select.click()

        time.sleep(5)

        use_cases_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]"
        )
        use_cases_select.click()

        time.sleep(5)

        use_case_2_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[37]"
        )
        use_case_2_select.click()

        time.sleep(5)

        use_cases_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]"
        )
        use_cases_select.click()

        time.sleep(5)

        use_case_3_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[122]"
        )
        use_case_3_select.click()

        time.sleep(5)

        use_cases_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]"
        )
        use_cases_select.click()

        time.sleep(5)

        use_case_4_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[135]"
        )
        use_case_4_select.click()

        time.sleep(5)

        use_cases_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]"
        )
        use_cases_select.click()

        time.sleep(5)

        use_case_5_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[139]"
        )
        use_case_5_select.click()

        time.sleep(5)

        # 3. Coverage
        coverage_button = browser.find_element_by_xpath("//a[@data-tab='coverage']")
        coverage_button.click()

        time.sleep(5)

        africa_select = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[5]/div/div[2]/div[2]/div/div/div[1]"
        )
        africa_select.click()

        time.sleep(5)

        africa_select_all_button = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[5]/div/div[2]/div[2]/div/div/div[2]/button[1]"
        )
        africa_select_all_button.click()

        time.sleep(5)

        asia_select = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[5]/div/div[2]/div[2]/div/div/div[3]"
        )
        asia_select.click()

        time.sleep(5)

        asia_select_all_button = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[5]/div/div[2]/div[2]/div/div/div[4]/button[1]"
        )
        asia_select_all_button.click()

        time.sleep(5)

        europe_select = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[5]/div/div[2]/div[2]/div/div/div[5]"
        )
        europe_select.click()

        time.sleep(5)

        europe_select_all_button = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[5]/div/div[2]/div[2]/div/div/div[6]/button[1]"
        )
        europe_select_all_button.click()

        time.sleep(5)

        north_america_select = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[5]/div/div[2]/div[2]/div/div/div[7]"
        )
        north_america_select.click()

        time.sleep(5)

        north_america_select_all_button = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[5]/div/div[2]/div[2]/div/div/div[8]/button[1]"
        )
        north_america_select_all_button.click()

        time.sleep(5)

        south_america_select = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[5]/div/div[2]/div[2]/div/div/div[9]"
        )
        south_america_select.click()

        time.sleep(5)

        south_america_select_all_button = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[5]/div/div[2]/div[2]/div/div/div[10]/button[1]"
        )
        south_america_select_all_button.click()

        time.sleep(5)

        oceania_select = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[5]/div/div[2]/div[2]/div/div/div[11]"
        )
        oceania_select.click()

        time.sleep(5)

        oceania_select_all_button = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[5]/div/div[2]/div[2]/div/div/div[12]/button[1]"
        )
        oceania_select_all_button.click()

        time.sleep(5)

        others_select = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[5]/div/div[2]/div[2]/div/div/div[13]"
        )
        others_select.click()

        time.sleep(5)

        others_select_all_button = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[5]/div/div[2]/div[2]/div/div/div[14]/button[1]"
        )
        others_select_all_button.click()

        time.sleep(5)

        # Historical Coverage
        historical_coverage_input = browser.find_element_by_xpath(
            '//input[@id="data_product__history"]'
        )
        historical_coverage_input.clear()
        historical_coverage_input.send_keys("1")

        time.sleep(5)

        range_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[5]/div/div[2]/div[3]/div[2]/div"
        )
        range_select.click()

        time.sleep(5)

        weeks_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[5]/div/div[2]/div[3]/div[2]/div/div[2]/div[2]"
        )
        weeks_select.click()

        time.sleep(5)

        # 4. Volume and quality
        volume_and_quality_button = browser.find_element_by_xpath("//a[@data-tab='volume_and_quality']")
        volume_and_quality_button.click()

        time.sleep(5)

        # Add Volume
        add_volume_button = browser.find_element_by_xpath("//a[@data-association='volume']")
        add_volume_button.click()

        time.sleep(5)

        # Volume input
        volume_input = browser.find_element_by_xpath("//input[@id='data_product_volume__value'][@type='number']")
        volume_input.clear()
        volume_input.send_keys(str(number_of_records))

        time.sleep(5)

        # unit_input
        unit_input = browser.find_element_by_xpath("//input[@id='data_product_volume__unit'][@type='text']")
        unit_input.clear()
        unit_input.send_keys("files")

        time.sleep(5)

        # Add Quality Attribute
        add_quality_attribute_button = browser.find_element_by_xpath("//a[@data-association='quality']")
        add_quality_attribute_button.click()

        time.sleep(5)

        # quality in % input
        quality_input = browser.find_element_by_xpath("//input[@id='data_product_quality__percentage'][@type='number']")
        quality_input.clear()
        quality_input.send_keys("100")

        time.sleep(5)

        # unit quality input
        unit_quality_input = browser.find_element_by_xpath("//input[@id='data_product_quality__unit'][@type='text']")
        unit_quality_input.clear()
        unit_quality_input.send_keys("match rate")

        time.sleep(5)

        # 5. Attributes
        attributes_button = browser.find_element_by_xpath("//a[@data-tab='attributes']")
        attributes_button.click()

        time.sleep(5)

        # Add Attribute _ file
        add_attribute_button = browser.find_element_by_xpath("//a[@data-association='attribute_spec']")
        add_attribute_button.click()

        time.sleep(5)

        # name input
        name_input = browser.find_element_by_xpath(
            "//input[@id='data_product_attribute_spec__name']"
        )
        name_input.clear()
        name_input.send_keys("file")

        time.sleep(5)

        # example input
        example_input = browser.find_element_by_xpath(
            "//input[@id='data_product_attribute_spec__example']"
        )
        example_input.clear()
        example_input.send_keys("circuit A")

        time.sleep(5)

        # description input
        description_input = browser.find_element_by_xpath(
            "//input[@id='data_product_attribute_spec__description']"
        )
        description_input.clear()
        description_input.send_keys("A gerber file")

        time.sleep(5)

        # number of Records input
        number_of_records_input = browser.find_element_by_xpath(
            "//input[@id='data_product_attribute_spec__number_of_records']"
        )
        number_of_records_input.clear()
        number_of_records_input.send_keys("One")

        time.sleep(5)

        # 6. Delivery
        delivery_button = browser.find_element_by_xpath("//a[@class='item'][@data-tab='delivery']")
        delivery_button.click()

        time.sleep(5)

        # Email checkbox
        email_checkbox = browser.find_element_by_xpath("//label[@for='data_product__transfer_method_ids-9']")
        email_checkbox.click()

        time.sleep(5)

        # Json checkbox
        json_checkbox = browser.find_element_by_xpath("//label[@for='data_product__data_format_ids-10']")
        json_checkbox.click()

        time.sleep(5)

        # on-demand checkbox
        on_demand_checkbox = browser.find_element_by_xpath("//label[@for='data_product__transfer_frequency_ids-10']")
        on_demand_checkbox.click()

        time.sleep(5)

        # 7. Pricing
        pricing_button = browser.find_element_by_xpath("//a[@data-tab='pricing']")
        pricing_button.click()

        time.sleep(5)

        # One-off purchase checkbox
        one_off_purchase_checkbox = browser.find_element_by_xpath(
            "//label[@for='data_product_pricing_plan__pricing_model_id-1']"
        )
        one_off_purchase_checkbox.click()

        time.sleep(5)

        # starts at one-off purchase input
        starts_at_one_off_purchase_input = browser.find_element_by_xpath(
            "//input[@id='data_product_pricing_plan__starts_at_price']"
        )
        starts_at_one_off_purchase_input.clear()
        starts_at_one_off_purchase_input.send_keys(str(price))

        time.sleep(5)

        currency_select = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[9]/div/div[2]/div[2]/div"
        )
        currency_select.click()

        time.sleep(5)

        eur_select = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[9]/div/div[2]/div[2]/div/div[2]/div[2]"
        )
        eur_select.click()

        time.sleep(5)


class UnitTestsWebAutomationDataradeParts(unittest.TestCase):
    # ok
    def test_se_connecter(self):
        print('test_se_connecter')

        time.sleep(5)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(5)

        # with Firefox
        browser = webdriver.Firefox(executable_path='..\\geckodriver.exe')

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get('https://datarade.ai/')

        time.sleep(5)

        clear_button = browser.find_element_by_xpath("//button[@data-cf-action='reject'][@aria-label='Deny']")
        clear_button.click()

        time.sleep(5)

        sign_in_button = browser.find_element_by_xpath("//a[@class='navbar__item'][@href='/users/sign_in']")
        sign_in_button.click()

        time.sleep(10)

        work_email_input = browser.find_element_by_xpath("//input[@id='user__email'][@name='user[email]']")
        work_email_input.clear()
        work_email_input.send_keys(""
                                   "")

        time.sleep(5)

        passwrod_input = browser.find_element_by_xpath("//input[@id='user__password'][@name='user[password]']")
        passwrod_input.clear()
        passwrod_input.send_keys("")

        time.sleep(5)

        login_button = browser.find_element_by_xpath("//input[@type='submit'][@name='commit']")
        login_button.click()

        time.sleep(15)

        print("ccleaner running")
        os.system("set ccleaner='C:\\Program Files\\CCleaner\\CCleaner.exe'")
        os.system("start ccleaner /AUTO")

        time.sleep(60)

    # ok
    def test_count_characters_for_selling_data_for_b2b_contact_data(self):
        print('test_count_characters_for_selling_data_for_b2b_contact_data')

        """
        Strong messages include:
        - A short description of your proposed product
        - A convincing explanation of how you can fulfill the buyer's requirements
        - Pricing indications, including how these will fit the buyer's given budget
        """

        message = """
Hello,

I would like to sell you a list of B2B contact data with the data attributes (company name, postal address, phone number,
website, email, region, activity, country) totally filled for many companies. 

The activities are : temporary employment agencies, real estate, software, hotel, cleaning services, financial, 
restaurant, building, social landlord, charity, hairdresser, florist, locksmith, bakery, insurance, pharmacy, mover, 
electricity, plumbing, security, attorney, bank, garage, dentist, doctor, accountant, grocery stores, notary, 
jewellery, tailor, butcher, library, architect, cement, heating, boat, cold, steel, chemical, gas and gold.

The dataset entirely covers the country.

The purchase starts at 9.99€ and one record costs 0.01€.

My profile is : https://datarade.ai/data-providers/holomorphe/profile

Kind regards,

Mr 
President of the Holomorphe company
General engineer graduated from the Leonardo da Vinci School of Engineering in Paris La Défense
Headquarters address: 31 Avenue de Ségur 75007 Paris
SIRET: https://www.societe.com/societe/holomorphe-883632556.html
Telephone : +33.7.49.16.33.29
Email : 

Website : https://holomorphe.com
Github : https://github.com/Jay4C
YouTube : https://www.youtube.com/channel/UClK7qVMGyLGEE0uPy7LFGlA

N.B.: Do not hesitate to leave your vocal message in english and I will call you back as soon as possible.
        """

        if 140 <= len(message):
            print('message length is good')
        else:
            print('message length is bad')

    # ok
    def test_propose_a_product(self):
        print("test_propose_a_product")

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(5)

        # with Firefox
        browser = webdriver.Firefox(executable_path='..\\geckodriver.exe')

        time.sleep(10)

        # maximize window
        browser.maximize_window()

        time.sleep(10)

        # open
        browser.get('https://datarade.ai/')

        time.sleep(15)

        clear_button = browser.find_element_by_xpath("//button[@data-cf-action='reject'][@aria-label='Deny']")
        clear_button.click()

        time.sleep(15)

        sign_in_button = browser.find_element_by_xpath("//a[@class='navbar__item'][@href='/users/sign_in']")
        sign_in_button.click()

        time.sleep(15)

        work_email_input = browser.find_element_by_xpath("//input[@id='user__email'][@name='user[email]']")
        work_email_input.clear()
        work_email_input.send_keys(""
        "")

        time.sleep(5)

        passwrod_input = browser.find_element_by_xpath("//input[@id='user__password'][@name='user[password]']")
        passwrod_input.clear()
        passwrod_input.send_keys("")

        time.sleep(5)

        login_button = browser.find_element_by_xpath("//input[@type='submit'][@name='commit']")
        login_button.click()

        time.sleep(15)

        urls = [
            "https://datarade.ai/my/provider/request_postings?hidden=1&page=1&request_posting_filter_form%5Bactive_scope%5D=hidden",
            "https://datarade.ai/my/provider/request_postings?hidden=1&page=2&request_posting_filter_form%5Bactive_scope%5D=hidden",
            "https://datarade.ai/my/provider/request_postings?hidden=1&page=3&request_posting_filter_form%5Bactive_scope%5D=hidden",
            "https://datarade.ai/my/provider/request_postings?hidden=1&page=4&request_posting_filter_form%5Bactive_scope%5D=hidden",
            "https://datarade.ai/my/provider/request_postings?hidden=1&page=5&request_posting_filter_form%5Bactive_scope%5D=hidden"
        ]

        for url in urls:
            for i in range(25):
                # hidden postings
                browser.get(url)

                time.sleep(15)

                if browser.find_element_by_xpath("//a[@class='small modern primary button']") is not None:
                    review_and_propose_a_product_button = browser.find_element_by_xpath(
                        "//a[@class='small modern primary button']"
                    )
                    review_and_propose_a_product_button.click()

                    time.sleep(10)

                    b2b_contact_data_select = browser.find_element_by_xpath(
                        "/html/body/div/main/div/div/div[2]/form/div[1]/div"
                    )
                    b2b_contact_data_select.click()

                    time.sleep(10)

                    panama_contact_data = browser.find_element_by_xpath(
                        "/html/body/div/main/div/div/div[2]/form/div[1]/div/div[2]/div[1]"
                    )
                    panama_contact_data.click()

                    time.sleep(10)

                    message = """Hello,

I would like to sell you a list of B2B contact data with the data attributes (company name, postal address, phone number,
website, email, region, activity, country) totally filled for many companies. 

The activities are : temporary employment agencies, real estate, software, hotel, cleaning services, financial, 
restaurant, building, social landlord, charity, hairdresser, florist, locksmith, bakery, insurance, pharmacy, mover, 
electricity, plumbing, security, attorney, bank, garage, dentist, doctor, accountant, grocery stores, notary, 
jewellery, tailor, butcher, library, architect, cement, heating, boat, cold, steel, chemical, gas and gold.

The dataset entirely covers the country.

The purchase starts at 9.99€ and one record costs 0.01€.

My profile is : https://datarade.ai/data-providers/holomorphe/profile

Kind regards,

Mr 
President of the Holomorphe company
General engineer graduated from the Leonardo da Vinci School of Engineering in Paris La Défense
Headquarters address: 31 Avenue de Ségur 75007 Paris
SIRET: https://www.societe.com/societe/holomorphe-883632556.html
Telephone : +33.7.49.16.33.29
Email : 

Website : https://holomorphe.com
Github : https://github.com/Jay4C
YouTube : https://www.youtube.com/channel/UClK7qVMGyLGEE0uPy7LFGlA

N.B.: Do not hesitate to leave your vocal message in english and I will call you back as soon as possible."""

                    your_message_input = browser.find_element_by_xpath(
                        "//textarea[@id='proposal__message']"
                    )
                    your_message_input.clear()
                    your_message_input.send_keys(message)

                    time.sleep(10)

                    n = 1
                    actions = ActionChains(browser)
                    actions.send_keys(Keys.TAB * n)
                    actions.send_keys(Keys.SPACE)
                    actions.perform()

                    time.sleep(10)

                    submit_proposal_button = browser.find_element_by_xpath(
                        "/html/body/div/main/div/div/div[2]/form/div[5]/input")
                    submit_proposal_button.click()

                    time.sleep(10)
                else:
                    break

    # ok
    def test_select_eur_for_pricing(self):
        print('test_select_eur_for_pricing')

        time.sleep(5)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(5)

        # with Firefox
        browser = webdriver.Firefox(executable_path='..\\geckodriver.exe')

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get('https://datarade.ai/')

        time.sleep(5)

        clear_button = browser.find_element_by_xpath("//button[@data-cf-action='reject'][@aria-label='Deny']")
        clear_button.click()

        time.sleep(5)

        sign_in_button = browser.find_element_by_xpath("//a[@class='navbar__item'][@href='/users/sign_in']")
        sign_in_button.click()

        time.sleep(10)

        work_email_input = browser.find_element_by_xpath("//input[@id='user__email'][@name='user[email]']")
        work_email_input.clear()
        work_email_input.send_keys(""
        "")

        time.sleep(5)

        passwrod_input = browser.find_element_by_xpath("//input[@id='user__password'][@name='user[password]']")
        passwrod_input.clear()
        passwrod_input.send_keys("")

        time.sleep(5)

        login_button = browser.find_element_by_xpath("//input[@type='submit'][@name='commit']")
        login_button.click()

        time.sleep(15)

        browser.get("https://datarade.ai/my/provider/data_products/new?form-tab=pricing")

        time.sleep(10)

        currency_select = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[9]/div/div[2]/div[2]/div"
        )
        currency_select.click()

        time.sleep(5)

        eur_select = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[9]/div/div[2]/div[2]/div/div[2]/div[2]"
        )
        eur_select.click()

        time.sleep(5)

    # ok
    def test_select_historical_coverage_range(self):
        print("test_select_historical_coverage_range")

        time.sleep(5)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(5)

        # with Firefox
        browser = webdriver.Firefox(executable_path='..\\geckodriver.exe')

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get('https://datarade.ai/')

        time.sleep(5)

        clear_button = browser.find_element_by_xpath("//button[@data-cf-action='reject'][@aria-label='Deny']")
        clear_button.click()

        time.sleep(5)

        sign_in_button = browser.find_element_by_xpath("//a[@class='navbar__item'][@href='/users/sign_in']")
        sign_in_button.click()

        time.sleep(10)

        work_email_input = browser.find_element_by_xpath("//input[@id='user__email'][@name='user[email]']")
        work_email_input.clear()
        work_email_input.send_keys(""
        "")

        time.sleep(5)

        passwrod_input = browser.find_element_by_xpath("//input[@id='user__password'][@name='user[password]']")
        passwrod_input.clear()
        passwrod_input.send_keys("")

        time.sleep(5)

        login_button = browser.find_element_by_xpath("//input[@type='submit'][@name='commit']")
        login_button.click()

        time.sleep(15)

        browser.get('https://datarade.ai/my/provider/data_products/new?form-tab=coverage')

        time.sleep(5)

        range_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[5]/div/div[2]/div[3]/div[2]/div"
        )
        range_select.click()

        time.sleep(5)

        weeks_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[5]/div/div[2]/div[3]/div[2]/div/div[2]/div[2]"
        )
        weeks_select.click()

        time.sleep(5)

    # ok
    def test_select_data_categories_in_listing(self):
        print("test_select_data_categories_in_listing")

        time.sleep(5)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(5)

        # with Firefox
        browser = webdriver.Firefox(executable_path='..\\geckodriver.exe')

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get('https://datarade.ai/')

        time.sleep(5)

        clear_button = browser.find_element_by_xpath("//button[@data-cf-action='reject'][@aria-label='Deny']")
        clear_button.click()

        time.sleep(5)

        sign_in_button = browser.find_element_by_xpath("//a[@class='navbar__item'][@href='/users/sign_in']")
        sign_in_button.click()

        time.sleep(10)

        work_email_input = browser.find_element_by_xpath("//input[@id='user__email'][@name='user[email]']")
        work_email_input.clear()
        work_email_input.send_keys(""
        "")

        time.sleep(5)

        passwrod_input = browser.find_element_by_xpath("//input[@id='user__password'][@name='user[password]']")
        passwrod_input.clear()
        passwrod_input.send_keys("")

        time.sleep(5)

        login_button = browser.find_element_by_xpath("//input[@type='submit'][@name='commit']")
        login_button.click()

        time.sleep(15)

        browser.get("https://datarade.ai/my/provider/data_products/new?form-tab=listing")

        time.sleep(5)

        data_catgory_1_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[1]/div/div"
        )
        data_catgory_1_select.click()

        time.sleep(5)

        data_catgory_1_value_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[1]/div/div/div[2]/div[4]"
        )
        data_catgory_1_value_select.click()

        time.sleep(5)

        data_catgory_2_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[2]/div/div"
        )
        data_catgory_2_select.click()

        time.sleep(5)

        data_catgory_2_value_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[2]/div/div/div[2]/div[6]"
        )
        data_catgory_2_value_select.click()

        time.sleep(5)

        data_catgory_3_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[3]/div/div"
        )
        data_catgory_3_select.click()

        time.sleep(5)

        data_catgory_3_value_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[3]/div/div/div[2]/div[15]"
        )
        data_catgory_3_value_select.click()

        time.sleep(5)

        data_catgory_4_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[4]/div/div"
        )
        data_catgory_4_select.click()

        time.sleep(5)

        data_catgory_4_value_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[4]/div/div/div[2]/div[20]"
        )
        data_catgory_4_value_select.click()

        time.sleep(5)

        data_catgory_5_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[5]/div/div"
        )
        data_catgory_5_select.click()

        time.sleep(5)

        data_catgory_5_value_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[1]/ol/li[5]/div/div/div[2]/div[34]"
        )
        data_catgory_5_value_select.click()

        time.sleep(5)

    # ok
    def test_select_use_cases_in_listing(self):
        print("test_select_use_cases_in_listing")

        time.sleep(5)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(5)

        # with Firefox
        browser = webdriver.Firefox(executable_path='..\\geckodriver.exe')

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get('https://datarade.ai/')

        time.sleep(5)

        clear_button = browser.find_element_by_xpath("//button[@data-cf-action='reject'][@aria-label='Deny']")
        clear_button.click()

        time.sleep(5)

        sign_in_button = browser.find_element_by_xpath("//a[@class='navbar__item'][@href='/users/sign_in']")
        sign_in_button.click()

        time.sleep(10)

        work_email_input = browser.find_element_by_xpath("//input[@id='user__email'][@name='user[email]']")
        work_email_input.clear()
        work_email_input.send_keys(""
        "")

        time.sleep(5)

        passwrod_input = browser.find_element_by_xpath("//input[@id='user__password'][@name='user[password]']")
        passwrod_input.clear()
        passwrod_input.send_keys("")

        time.sleep(5)

        login_button = browser.find_element_by_xpath("//input[@type='submit'][@name='commit']")
        login_button.click()

        time.sleep(15)

        browser.get('https://datarade.ai/my/provider/data_products/new?form-tab=listing')

        time.sleep(5)

        use_cases_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]"
        )
        use_cases_select.click()

        time.sleep(5)

        use_case_1_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[33]"
        )
        use_case_1_select.click()

        time.sleep(5)

        use_cases_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]"
        )
        use_cases_select.click()

        time.sleep(5)

        use_case_2_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[37]"
        )
        use_case_2_select.click()

        time.sleep(5)

        use_cases_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]"
        )
        use_cases_select.click()

        time.sleep(5)

        use_case_3_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[122]"
        )
        use_case_3_select.click()

        time.sleep(5)

        use_cases_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]"
        )
        use_cases_select.click()

        time.sleep(5)

        use_case_4_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[135]"
        )
        use_case_4_select.click()

        time.sleep(5)

        use_cases_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]"
        )
        use_cases_select.click()

        time.sleep(5)

        use_case_5_select = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[4]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[139]"
        )
        use_case_5_select.click()

        time.sleep(5)

    # ok
    def test_select_all_coverage_countries(self):
        print("test_select_all_coverage_countries")

        time.sleep(5)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(5)

        # with Firefox
        browser = webdriver.Firefox(executable_path='..\\geckodriver.exe')

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get('https://datarade.ai/')

        time.sleep(5)

        clear_button = browser.find_element_by_xpath("//button[@data-cf-action='reject'][@aria-label='Deny']")
        clear_button.click()

        time.sleep(5)

        sign_in_button = browser.find_element_by_xpath("//a[@class='navbar__item'][@href='/users/sign_in']")
        sign_in_button.click()

        time.sleep(10)

        work_email_input = browser.find_element_by_xpath("//input[@id='user__email'][@name='user[email]']")
        work_email_input.clear()
        work_email_input.send_keys(""
        "")

        time.sleep(5)

        passwrod_input = browser.find_element_by_xpath("//input[@id='user__password'][@name='user[password]']")
        passwrod_input.clear()
        passwrod_input.send_keys("")

        time.sleep(5)

        login_button = browser.find_element_by_xpath("//input[@type='submit'][@name='commit']")
        login_button.click()

        time.sleep(15)

        browser.get('https://datarade.ai/my/provider/data_products/new?form-tab=coverage')

        time.sleep(5)

        africa_select = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[5]/div/div[2]/div[2]/div/div/div[1]"
        )
        africa_select.click()

        time.sleep(5)

        africa_select_all_button = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[5]/div/div[2]/div[2]/div/div/div[2]/button[1]"
        )
        africa_select_all_button.click()

        time.sleep(5)

        asia_select = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[5]/div/div[2]/div[2]/div/div/div[3]"
        )
        asia_select.click()

        time.sleep(5)

        asia_select_all_button = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[5]/div/div[2]/div[2]/div/div/div[4]/button[1]"
        )
        asia_select_all_button.click()

        time.sleep(5)

        europe_select = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[5]/div/div[2]/div[2]/div/div/div[5]"
        )
        europe_select.click()

        time.sleep(5)

        europe_select_all_button = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[5]/div/div[2]/div[2]/div/div/div[6]/button[1]"
        )
        europe_select_all_button.click()

        time.sleep(5)

        north_america_select = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[5]/div/div[2]/div[2]/div/div/div[7]"
        )
        north_america_select.click()

        time.sleep(5)

        north_america_select_all_button = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[5]/div/div[2]/div[2]/div/div/div[8]/button[1]"
        )
        north_america_select_all_button.click()

        time.sleep(5)

        south_america_select = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[5]/div/div[2]/div[2]/div/div/div[9]"
        )
        south_america_select.click()

        time.sleep(5)

        south_america_select_all_button = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[5]/div/div[2]/div[2]/div/div/div[10]/button[1]"
        )
        south_america_select_all_button.click()

        time.sleep(5)

        oceania_select = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[5]/div/div[2]/div[2]/div/div/div[11]"
        )
        oceania_select.click()

        time.sleep(5)

        oceania_select_all_button = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[5]/div/div[2]/div[2]/div/div/div[12]/button[1]"
        )
        oceania_select_all_button.click()

        time.sleep(5)

        others_select = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[5]/div/div[2]/div[2]/div/div/div[13]"
        )
        others_select.click()

        time.sleep(5)

        others_select_all_button = browser.find_element_by_xpath(
            "/html/body/div/main/div/div/form/div[5]/div/div[2]/div[2]/div/div/div[14]/button[1]"
        )
        others_select_all_button.click()

        time.sleep(5)

    # ok
    def test_select_type_software(self):
        print('test_select_type_software')

        time.sleep(5)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(5)

        # with Firefox
        browser = webdriver.Firefox(executable_path='..\\geckodriver.exe')

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get('https://datarade.ai/')

        time.sleep(5)

        clear_button = browser.find_element_by_xpath("//button[@data-cf-action='reject'][@aria-label='Deny']")
        clear_button.click()

        time.sleep(5)

        sign_in_button = browser.find_element_by_xpath("//a[@class='navbar__item'][@href='/users/sign_in']")
        sign_in_button.click()

        time.sleep(10)

        work_email_input = browser.find_element_by_xpath("//input[@id='user__email'][@name='user[email]']")
        work_email_input.clear()
        work_email_input.send_keys(""
        "")

        time.sleep(5)

        passwrod_input = browser.find_element_by_xpath("//input[@id='user__password'][@name='user[password]']")
        passwrod_input.clear()
        passwrod_input.send_keys("")

        time.sleep(5)

        login_button = browser.find_element_by_xpath("//input[@type='submit'][@name='commit']")
        login_button.click()

        time.sleep(15)

        browser.get("https://datarade.ai/my/provider/data_products/new")

        time.sleep(10)

        software_button = browser.find_element_by_xpath(
            "/html/body/div[1]/main/div/div/form/div[3]/div/div[2]/div[1]/div[2]/div/div"
        )
        software_button.click()

        time.sleep(5)


if __name__ == '__main__':
    unittest.main()
