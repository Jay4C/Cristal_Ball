import warnings
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
from bs4 import BeautifulSoup
import unittest
from requests_tor import RequestsTor


class UnitTestDataMinerWorldmetersWithDarkWeb(unittest.TestCase):
    # ok
    def test_get_us_population(self):
        print("test_get_us_population")

        us_population = 0

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://www.worldometers.info/world-population/us-population/"

        rt = RequestsTor()

        html_with_tor = rt.get(url, headers=headers)

        # Parse the content of html_doc
        soup = BeautifulSoup(html_with_tor.content, 'html.parser')

        element = soup.find('div', {'class': 'col-md-8 country-pop-description'}).find_all('ul')[0].find_all('li')[0]

        if element is not None:
            us_population += float(element.find_all('strong')[1].text.replace(',', ''))

            print('us_population : ' + str(us_population))

    # ok
    def test_get_us_population_live(self):
        print("test_get_us_population_live")

        us_population_live = 0

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
        browser.get('https://www.worldometers.info/world-population/us-population/')
        print("page opened")

        time.sleep(10)

        element = browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div/div[1]/div")

        if element is not None:
            us_population_live += float(element.text.replace(",", ""))

            print("us_population_live : " + str(us_population_live))

        browser.close()


if __name__ == '__main__':
    unittest.main()
