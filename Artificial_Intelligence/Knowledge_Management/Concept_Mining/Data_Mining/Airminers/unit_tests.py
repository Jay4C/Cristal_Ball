import unittest
import time
import requests
from bs4 import BeautifulSoup
import warnings
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import xlsxwriter


class UnitTestsDataMiningAirminers(unittest.TestCase):
    # no
    def test_extract_all_company_into_excel(self):
        print("test_extract_all_company_into_excel")

        url = "https://airminers.org/explore"

        html = requests.get(url)

        time.sleep(5)

        soup = BeautifulSoup(html.content, 'html.parser')

        print(html.content)

        if soup.find("a", {'class': "Startups-card-link"}) is not None:
            all_links = soup.find_all("a", {'class': "Startups-card-link"})

            for link in all_links:
                print("link : " + link.get('href'))
        else:
            print("no offres")

    # ok
    def test_extract_all_company_into_excel_from_selenium_headless(self):
        print("test_extract_all_company_into_excel_from_selenium_headless")

        time.sleep(5)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(5)

        # with Firefox
        options = Options()
        options.headless = True
        browser = webdriver.Firefox(executable_path='..\\geckodriver.exe', options=options)

        time.sleep(5)

        # maximize window
        browser.maximize_window()
        print("browser.maximize_window()")

        time.sleep(5)

        # open
        browser.get("https://airminers.org/explore")
        print("browser.get()")

        time.sleep(15)

        try:
            filename = "contacts_airminers.xlsx"

            workbook = xlsxwriter.Workbook(filename)

            worksheet = workbook.add_worksheet('Data')

            worksheet.write(0, 0, 'Company')
            worksheet.write(0, 1, 'Website')
            worksheet.write(0, 2, 'Email')

            if browser.find_element_by_class_name("Startups-card-link") is not None:
                all_links = browser.find_elements_by_class_name("Startups-card-link")

                i = 1

                for link in all_links:
                    company = link.get_attribute('href').replace('https://', '').replace('https://en.', '')\
                        .replace('http://', '')\
                        .replace('.com', '').replace('.net', '').replace('.ca', '').replace('airminers.org', '')\
                        .replace('/', '').replace('fi', '').replace('pt', '').replace('www.', '').replace('io', '')\
                        .replace('.tech', '').replace('.earth', '').replace('.cc', '').replace('.today', '')\
                        .replace('.co', '').replace(".ai", '').replace('.org', '').replace('.house', '').replace('.at', '')\
                        .replace(".ru", '').replace(".co.uk", '').replace(".au", '')

                    website = link.get_attribute('href')

                    email = "'info@" \
                            + link.get_attribute('href').replace('https://', '').replace('https://en.', '')\
                                .replace('http://', '').replace('www.', '').replace('/', '') \
                            + "',"

                    worksheet.write(i, 0, company)

                    worksheet.write(i, 1, website)

                    worksheet.write(i, 2, email)

                    i += 1

                    print('link ' + str(i) + ' : ' + link.get_attribute('href'))
            else:
                print("no links")

            workbook.close()

            time.sleep(5)

            browser.quit()
            print('browser.quit()')
        except Exception as e:
            print('error : ' + str(e))

            browser.quit()
            print('browser.quit()')


if __name__ == '__main__':
    unittest.main()
