import time
import warnings
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
import unittest
import subprocess


class UnitTestsRPAWAMarketingYPUnitedArabEmirates(unittest.TestCase):
    # ok
    def test_close_all_processes(self):
        print('test_close_all_processes')

        subprocess.run('taskkill /f /im firefox.exe')
        subprocess.run('taskkill /f /im geckodriver.exe')

    # ok
    def test_open_one_page(self):
        print('test_open_one_page')

        url = 'https://www.yellow-pages.ae/company/1477385680.shtml'

        time.sleep(5)

        warnings.filterwarnings(
            action="ignore",
            message="unclosed",
            category=ResourceWarning
        )

        time.sleep(5)

        # with Firefox
        options = Options()
        options.headless = False
        browser = webdriver.Firefox(
            executable_path='C:\\Users\\Jason\\Dropbox\\1_Personnel\\1_Recurrentes\\3_Outils_Numeriques\\GitHub'
                            '\\Cristal_Ball\\geckodriver.exe',
            options=options
        )

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get(url)

        time.sleep(5)

    # ok
    def test_submit_a_request_for_one_page(self):
        print('test_submit_a_request_for_one_page')

        url = 'https://www.yellow-pages.ae/company/1447234986.shtml'

        time.sleep(5)

        warnings.filterwarnings(
            action="ignore",
            message="unclosed",
            category=ResourceWarning
        )

        time.sleep(5)

        # with Firefox
        options = Options()
        options.headless = False
        browser = webdriver.Firefox(
            executable_path='C:\\Users\\Jason\\Dropbox\\1_Personnel\\1_Recurrentes\\3_Outils_Numeriques\\GitHub'
                            '\\Cristal_Ball\\geckodriver.exe',
            options=options
        )

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get(url)

        time.sleep(5)

        # Click on the 'I agree' button
        i_agree_button = browser.find_element(
            by=By.XPATH,
            value="/html/body/div[1]/div/div/div[2]/button[1]"
        )
        i_agree_button.click()
        print('i_agree_button.click() clicked')

        time.sleep(5)

        # Click on the 'Contact' button
        contact_button = browser.find_element(
            by=By.XPATH,
            value="/html/body/div[2]/div/div/div/div[2]/div/ul/li[3]/a"
        )
        contact_button.click()
        print('i_agree_button.click() clicked')

        time.sleep(5)

        # Insert your first and last name
        first_and_last_name_input = browser.find_element(
            by=By.XPATH,
            value='//*[@id="name"]'
        )
        first_and_last_name_input.clear()
        first_and_last_name_input.send_keys('Jason ALOYAU')
        print("first_and_last_name_input.send_keys('Jason ALOYAU')")

        time.sleep(5)

        # Insert your email address
        email_address_input = browser.find_element(
            by=By.XPATH,
            value='//*[@id="email"]'
        )
        email_address_input.clear()
        email_address_input.send_keys('jason.aloyau@outlook.fr')
        print("email_address_input.send_keys('jason.aloyau@outlook.fr')")

        time.sleep(5)

        # Insert your business name
        business_name_input = browser.find_element(
            by=By.XPATH,
            value='//*[@id="field2"]'
        )
        business_name_input.clear()
        business_name_input.send_keys('Voltorus')
        print("business_name_input.send_keys('Voltorus')")

        time.sleep(5)

        # Insert your website
        website_input = browser.find_element(
            by=By.XPATH,
            value='//*[@id="url"]'
        )
        website_input.clear()
        website_input.send_keys('https://holomorphe.wordpress.com/')
        print("website_input.send_keys('https://holomorphe.wordpress.com/')")

        time.sleep(5)

        # Insert your country
        browser.find_element(
            by=By.XPATH,
            value='/html/body/div[2]/div/div/div/div[1]/div/div/div[3]/div/div/form/center/table/tbody/tr[5]/td[2]/div/a/span[2]'
        ).click()
        time.sleep(3)
        country_input = browser.find_element(
            by=By.XPATH,
            value='//*[@id="s2id_autogen7_search"]'
        )
        country_input.clear()
        country_input.send_keys('France')
        time.sleep(3)
        country_input.send_keys(Keys.ENTER)
        print("country_input.send_keys('France')")

        time.sleep(5)

        # Insert your request
        request_input = browser.find_element(
            by=By.XPATH,
            value='//*[@id="description"]'
        )
        request_input.clear()
        request_input.send_keys('Hello. Do you buy gold please ? Do you pay in EUR ? Kind regards. Phone number '
                                ': +33.7.49.16.33.29')
        print("request_input.send_keys('request')")

        time.sleep(5)

        # Delete the Element <div id="select2-drop-mask" class="select2-drop-mask">
        browser.execute_script("document.getElementById('select2-drop-mask').remove();")

        time.sleep(3)

        # Click on the 'My free request is not advertising, promotion or a jobapplication.' checkbox
        free_request_checkbox = browser.find_element(
            by=By.XPATH,
            value="/html/body/div[2]/div/div/div/div[1]/div/div/div[3]/div/div/form/center/table/tbody/tr[8]/td/input[1]"
        )
        free_request_checkbox.click()
        print('free_request_checkbox.click()')

        time.sleep(5)

        # Click on the 'I accept the terms of use and privacy policy of sjn AG.' checkbox
        accept_terms_checkbox = browser.find_element(
            by=By.XPATH,
            value="/html/body/div[2]/div/div/div/div[1]/div/div/div[3]/div/div/form/center/table/tbody/tr[8]/td/input[2]"
        )
        accept_terms_checkbox.click()
        print('accept_terms_checkbox.click()')

        time.sleep(5)

        # Click on the 'Send your message' button
        send_your_message_button = browser.find_element(
            by=By.XPATH,
            value="/html/body/div[2]/div/div/div/div[1]/div/div/div[3]/div/div/form/center/table/tbody/tr[9]/td/center/input[9]"
        )
        send_your_message_button.click()
        print('send_your_message_button.click()')

        time.sleep(5)

        print(browser.find_element(by=By.XPATH, value='/html/body').text.replace('\n', ''))

    # ok
    def test_submit_requests_for_all_companies_for_selling_gold(self):
        print('test_submit_requests_for_all_companies_for_selling_gold')

        warnings.filterwarnings(
            action="ignore",
            message="unclosed",
            category=ResourceWarning
        )

        time.sleep(5)

        # with Firefox
        options = Options()
        options.headless = True
        browser = webdriver.Firefox(
            executable_path='C:\\Users\\Jason\\Dropbox\\1_Personnel\\1_Recurrentes\\3_Outils_Numeriques\\GitHub'
                            '\\Cristal_Ball\\geckodriver.exe',
            options=options
        )

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get('https://www.yellow-pages.ae')

        time.sleep(5)

        # Click on the 'I agree' button
        i_agree_button = browser.find_element(
            by=By.XPATH,
            value="/html/body/div[1]/div/div/div[2]/button[1]"
        )
        i_agree_button.click()
        print('i_agree_button.click() clicked')

        time.sleep(5)

        number_of_pages = 48

        for i in range(43, number_of_pages + 1):
            url_page = 'https://www.yellow-pages.ae/index.php/Terms::gold/page::' + str(i) + '/hpp::20/'
            print('url_page : ' + url_page)

            # open
            browser.get(url_page)

            time.sleep(5)

            urls = []

            if browser.find_element(by=By.CLASS_NAME, value='post-read-more') is not None:
                all_urls = browser.find_elements(by=By.CLASS_NAME, value='post-read-more')

                for url_1 in all_urls:
                    link = url_1.get_attribute('href')

                    if link not in urls:
                        urls.append(link)
            else:
                print('no a class post-read-more')

            for url in urls:
                try:
                    print(url)

                    time.sleep(3)

                    browser.get(url)

                    time.sleep(5)

                    # Click on the 'Contact' button
                    try:
                        contact_button = browser.find_element(
                            by=By.XPATH,
                            value="/html/body/div[2]/div/div/div/div[2]/div/ul/li[3]/a"
                        )
                        contact_button.click()
                        print('contact_button.click() clicked')
                    except Exception as e:
                        print('error : ' + str(e))
                        contact_button = browser.find_element(
                            by=By.XPATH,
                            value="/html/body/div[1]/div/div/div/div[2]/div/ul/li[3]/a"
                        )
                        contact_button.click()
                        print('contact_button.click() clicked')

                    time.sleep(5)

                    # Insert your first and last name
                    first_and_last_name_input = browser.find_element(
                        by=By.XPATH,
                        value='//*[@id="name"]'
                    )
                    first_and_last_name_input.clear()
                    first_and_last_name_input.send_keys('Jason ALOYAU')
                    print("first_and_last_name_input.send_keys('Jason ALOYAU')")

                    time.sleep(5)

                    # Insert your email address
                    email_address_input = browser.find_element(
                        by=By.XPATH,
                        value='//*[@id="email"]'
                    )
                    email_address_input.clear()
                    email_address_input.send_keys('jason.aloyau@outlook.fr')
                    print("email_address_input.send_keys('jason.aloyau@outlook.fr')")

                    time.sleep(5)

                    # Insert your business name
                    business_name_input = browser.find_element(
                        by=By.XPATH,
                        value='//*[@id="field2"]'
                    )
                    business_name_input.clear()
                    business_name_input.send_keys('Voltorus')
                    print("business_name_input.send_keys('Voltorus')")

                    time.sleep(5)

                    # Insert your website
                    website_input = browser.find_element(
                        by=By.XPATH,
                        value='//*[@id="url"]'
                    )
                    website_input.clear()
                    website_input.send_keys('https://holomorphe.wordpress.com/')
                    print("website_input.send_keys('https://holomorphe.wordpress.com/')")

                    time.sleep(5)

                    # Insert your country
                    try:
                        browser.find_element(
                            by=By.XPATH,
                            value='/html/body/div[2]/div/div/div/div[1]/div/div/div[3]/div/div/form/center/table/tbody/tr[5]/td[2]/div/a/span[2]'
                        ).click()
                        time.sleep(3)
                        country_input = browser.find_element(
                            by=By.XPATH,
                            value='//*[@id="s2id_autogen7_search"]'
                        )
                        country_input.clear()
                        country_input.send_keys('France')
                        time.sleep(3)
                        country_input.send_keys(Keys.ENTER)
                        print("country_input.send_keys('France')")
                    except Exception as e:
                        print('error insert your country : ' + str(e))
                        browser.find_element(
                            by=By.XPATH,
                            value='/html/body/div/div/div/div/div[1]/div/div/div[3]/div/div/form/center/table/tbody/tr[5]/td[2]/div/a/span[2]').click()
                        time.sleep(3)
                        country_input = browser.find_element(
                            by=By.XPATH,
                            value='//*[@id="s2id_autogen7_search"]'
                        )
                        country_input.clear()
                        country_input.send_keys('France')
                        time.sleep(3)
                        country_input.send_keys(Keys.ENTER)
                        print("country_input.send_keys('France')")

                    time.sleep(5)

                    # Insert your request
                    request_input = browser.find_element(
                        by=By.XPATH,
                        value='//*[@id="description"]'
                    )
                    request_input.clear()
                    request_input.send_keys(
                        'Hello. Do you buy gold please ? Do you pay in EUR ? Kind regards.')
                    print("request_input.send_keys('request')")

                    time.sleep(5)

                    # Delete the Element <div id="select2-drop-mask" class="select2-drop-mask">
                    browser.execute_script("document.getElementById('select2-drop-mask').remove();")

                    time.sleep(3)

                    # Click on the 'My free request is not advertising, promotion or a jobapplication.' checkbox
                    try:
                        free_request_checkbox = browser.find_element(
                            by=By.XPATH,
                            value="/html/body/div[2]/div/div/div/div[1]/div/div/div[3]/div/div/form/center/table/tbody/tr[8]/td/input[1]"
                        )
                        free_request_checkbox.click()
                        print('free_request_checkbox.click()')
                    except Exception as e:
                        print('error free_request_checkbox : ' + str(e))
                        free_request_checkbox = browser.find_element(
                            by=By.XPATH,
                            value="/html/body/div[1]/div/div/div/div[1]/div/div/div[3]/div/div/form/center/table/tbody/tr[8]/td/input[1]"
                        )
                        free_request_checkbox.click()
                        print('free_request_checkbox.click()')

                    time.sleep(3)

                    # Click on the 'I accept the terms of use and privacy policy of sjn AG.' checkbox
                    try:
                        accept_terms_checkbox = browser.find_element(
                            by=By.XPATH,
                            value="/html/body/div[2]/div/div/div/div[1]/div/div/div[3]/div/div/form/center/table/tbody/tr[8]/td/input[2]"
                        )
                        accept_terms_checkbox.click()
                        print('accept_terms_checkbox.click()')
                    except Exception as e:
                        print('error accept_terms_checkbox : ' + str(e))
                        accept_terms_checkbox = browser.find_element(
                            by=By.XPATH,
                            value="/html/body/div[1]/div/div/div/div[1]/div/div/div[3]/div/div/form/center/table/tbody/tr[8]/td/input[2]"
                        )
                        accept_terms_checkbox.click()
                        print('accept_terms_checkbox.click()')

                    time.sleep(5)

                    # Click on the 'Send your message' button
                    try:
                        send_your_message_button = browser.find_element(
                            by=By.XPATH,
                            value="/html/body/div[2]/div/div/div/div[1]/div/div/div[3]/div/div/form/center/table/tbody/tr[9]/td/center/input[9]"
                        )
                        send_your_message_button.click()
                        print('send_your_message_button.click()')
                    except Exception as e:
                        print('error send_your_message_button : ' + str(e))
                        send_your_message_button = browser.find_element(
                            by=By.XPATH,
                            value="/html/body/div[1]/div/div/div/div[1]/div/div/div[3]/div/div/form/center/table/tbody/tr[9]/td/center/input[9]"
                        )
                        send_your_message_button.click()
                        print('send_your_message_button.click()')

                    time.sleep(5)

                    print(browser.find_element(by=By.XPATH, value='/html/body').text.replace('\n', ''))

                    time.sleep(5)
                except Exception as e:
                    print('error : ' + str(e))

        browser.quit()


if __name__ == '__main__':
    unittest.main()
