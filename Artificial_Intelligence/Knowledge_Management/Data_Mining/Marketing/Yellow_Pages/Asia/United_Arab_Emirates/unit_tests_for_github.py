import time
import warnings
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
from requests_tor import RequestsTor
import requests
import unittest
import subprocess


class UnitTestsDataMinerYellowPagesUnitedArabEmirates(unittest.TestCase):
    #
    def test_extract_the_company_name_from_one_page_result(self):
        print('test_extract_the_company_name_from_one_page_result')

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = 'https://www.yellow-pages.ae/company/1477385680.shtml'

        rt = requests
        # rt = RequestsTor()

        html = rt.get(url, headers=headers).content
        print(html)

        time.sleep(3)

        soup = BeautifulSoup(html, 'html.parser')

        if soup.find("div", {'class': 'company-slider-content'}) is not None:
            company_name = soup.find_all("div", {'class': 'company-slider-content'})[0].find_all('h1')[0].text
            print("company_name : " + str(company_name))
        else:
            print("no company_name")


class UnitTestsDataMinerYellowPagesUnitedArabEmiratesWithSelenium(unittest.TestCase):
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
        browser = webdriver.Firefox(
            executable_path='C:\\Users\\Jason\\Dropbox\\1_Personnel\\1_Recurrentes\\3_Outils_Numeriques\\GitHub\\Cristal_Ball\\geckodriver.exe'
        )

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get(url)

        time.sleep(5)

    # ok
    def test_extract_the_company_name_from_one_page(self):
        print('test_extract_the_company_name_from_one_page')

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

        company_name = browser.find_element(
            by=By.XPATH,
            value="/html/body/div[2]/header/div[2]/div[2]/div[2]/div[1]/div/h1"
        ).text

        print("company_name : " + str(company_name))

    # ok
    def test_extract_the_phone_number_from_one_page(self):
        print('test_extract_the_phone_number_from_one_page')

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

        phone_number = browser.find_element(
            by=By.XPATH,
            value="/html/body/div/div/div/div/div[2]/div/div[2]/ul/li[5]"
        ).text.replace('Phone', '')

        print("phone_number : " + str(phone_number))

    # ok
    def test_extract_the_city_from_one_page(self):
        print('test_extract_the_city_from_one_page')

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

        city = browser.find_element(
            by=By.XPATH,
            value="/html/body/div/div/div/div/div[2]/div/div[2]/ul/li[1]"
        ).text.replace('City', '').replace('\n', '')

        print("city : " + str(city))

        browser.quit()

    # ok
    def test_extract_the_address_from_one_page(self):
        print('test_extract_the_address_from_one_page')

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

        address = browser.find_element(
            by=By.XPATH,
            value="/html/body/div/div/div/div/div[2]/div/div[2]/ul/li[2]"
        ).text.replace('Address', '').replace('\n', '')

        print("address : " + str(address))

        browser.quit()

    # ok
    def test_extract_the_zip_code_from_one_page(self):
        print('test_extract_the_zip_code_from_one_page')

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

        zip_code = browser.find_element(
            by=By.XPATH,
            value="/html/body/div/div/div/div/div[2]/div/div[2]/ul/li[3]"
        ).text.replace('ZIP Code', '').replace('\n', '')

        print("zip_code : " + str(zip_code))

        browser.quit()

    # ok
    def test_extract_the_po_box_from_one_page(self):
        print('test_extract_the_po_box_from_one_page')

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

        po_box = browser.find_element(
            by=By.XPATH,
            value="/html/body/div/div/div/div/div[2]/div/div[2]/ul/li[4]"
        ).text.replace('Po Box', '').replace('\n', '')

        print("Po Box : " + str(po_box))

        browser.quit()

    # ok
    def test_extract_the_company_details_from_one_page(self):
        print('test_extract_the_company_details_from_one_page')

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

        company_name = browser.find_element(
            by=By.XPATH,
            value="/html/body/div[2]/header/div[2]/div[2]/div[2]/div[1]/div/h1"
        ).text

        print("company_name : " + str(company_name))

        phone_number = browser.find_element(
            by=By.XPATH,
            value="/html/body/div/div/div/div/div[2]/div/div[2]/ul/li[5]"
        ).text.replace('Phone', '').replace('\n', '')

        print("phone_number : " + str(phone_number))

        city = browser.find_element(
            by=By.XPATH,
            value="/html/body/div/div/div/div/div[2]/div/div[2]/ul/li[1]"
        ).text.replace('City', '').replace('\n', '')

        print("city : " + str(city))

        address = browser.find_element(
            by=By.XPATH,
            value="/html/body/div/div/div/div/div[2]/div/div[2]/ul/li[2]"
        ).text.replace('Address', '').replace('\n', '')

        print("address : " + str(address))

        zip_code = browser.find_element(
            by=By.XPATH,
            value="/html/body/div/div/div/div/div[2]/div/div[2]/ul/li[3]"
        ).text.replace('ZIP Code', '').replace('\n', '')

        print("zip_code : " + str(zip_code))

        po_box = browser.find_element(
            by=By.XPATH,
            value="/html/body/div/div/div/div/div[2]/div/div[2]/ul/li[4]"
        ).text.replace('Po Box', '').replace('\n', '')

        print("Po Box : " + str(po_box))

        browser.quit()

    # ok
    def test_extract_all_urls_company_from_one_page_result(self):
        print('test_extract_all_urls_company_from_one_page_result')

        url = 'https://www.yellow-pages.ae/index.php/Terms::gold/page::1/hpp::20/'

        time.sleep(5)

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

        if browser.find_element(by=By.CLASS_NAME, value='post-read-more') is not None:
            all_urls = browser.find_elements(by=By.CLASS_NAME, value='post-read-more')

            for url in all_urls:
                link = url.get_attribute('href')
                print('link : ' + link)
        else:
            print('no a class post-read-more')

        browser.quit()

    # ok
    def test_extract_the_number_of_companies(self):
        print('test_extract_the_number_of_companies')

        url = 'https://www.yellow-pages.ae/index.php/Terms::gold/page::1/hpp::20/'

        time.sleep(5)

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

        if browser.find_element(by=By.CLASS_NAME, value='comments') is not None:
            number_of_companies = browser.find_element(by=By.CLASS_NAME, value='comments').text
            print('number_of_companies : ' + str(number_of_companies))
        else:
            print('no span class comments')

        browser.quit()

    # ok
    def test_extract_the_number_of_page_result_from_one_page(self):
        print('test_extract_the_number_of_page_result_from_one_page')

        url = 'https://www.yellow-pages.ae/index.php/Terms::gold/page::1/hpp::20/'

        time.sleep(5)

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

        if browser.find_element(by=By.CLASS_NAME, value='comments') is not None:
            number_of_pages = 0

            number_of_pages_with_coma = int(browser.find_element(by=By.CLASS_NAME, value='comments')
                                            .text
                                            .split("OF")[1]
                                            .replace(" ", "")
                                            ) / 20

            if int(str(number_of_pages_with_coma).split(".")[1][:1]) < 5:
                number_of_pages += round(number_of_pages_with_coma) + 1
                print('number_of_pages : ' + str(number_of_pages))
            elif int(str(number_of_pages_with_coma).split(".")[1][:1]) >= 5:
                number_of_pages += round(number_of_pages_with_coma)
                print('number_of_pages : ' + str(number_of_pages))
        else:
            print('no span class comments')

        browser.quit()


if __name__ == '__main__':
    unittest.main()
