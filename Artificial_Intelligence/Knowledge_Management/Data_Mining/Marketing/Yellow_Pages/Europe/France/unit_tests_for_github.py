import time
import warnings
from bs4 import BeautifulSoup
import requests
import unittest
from selenium import webdriver


class UnitTestsDataMinerYellowPagesFrance(unittest.TestCase):
    def test_extract_the_company_name_from_one_page_result(self):
        print('test_extract_the_company_name_from_one_page_result')

        url = "https://www.pagesjaunes.fr/pros/detail?code_etablissement=09657853&code_localite=D974&code_rubrique=788800"

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        time.sleep(3)

        # Request the content of a page from the url
        html = requests.get(url, headers=headers)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.content, 'html.parser')

        # company name
        if soup.find('div', {'class': 'header-main-infos'}) is not None:
            company_name = soup.find('div', {'class': 'header-main-infos'})\
                .find('div', {'class': 'denom'})\
                .find('h1')\
                .text

            print("company_name : " + company_name)
        else:
            print("no company name business")


class UnitTestsDataMinerYellowPagesFranceWithSelenium(unittest.TestCase):
    def test_extract_the_company_name_from_one_page_result_with_selenium(self):
        print('test_extract_the_company_name_from_one_page_result_with_selenium')

        url = "https://www.pagesjaunes.fr/pros/detail?code_etablissement=09657853&code_localite=D974&code_rubrique=788800"

        time.sleep(5)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(5)

        # with Firefox
        browser = webdriver.Firefox(executable_path='M:\\1_Personnel\\1_Recurrentes\\3_Outils_Numeriques\\GitHub_Jay4C\\Cristal_Ball\\geckodriver.exe')

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get(url)

        time.sleep(5)


if __name__ == '__main__':
    unittest.main()
