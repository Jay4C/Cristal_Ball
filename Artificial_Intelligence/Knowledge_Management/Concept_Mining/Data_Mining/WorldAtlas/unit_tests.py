import unittest
from bs4 import BeautifulSoup
import requests


class UnitTestsDataMiningWorldAtlas(unittest.TestCase):
    def test_extract_countries_with_death_penalty(self):
        print("test_extract_countries_with_death_penalty")

        url = 'https://www.worldatlas.com/articles/countries-with-capital-punishment.html'

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        html = requests.get(url, headers=headers)

        soup = BeautifulSoup(html.text, 'html.parser')

        if soup.find("table", {"data-role": "table"}) is not None:
            all_tr = soup.find("table", {"data-role": "table"}).find("tbody").find_all("tr")

            for tr in all_tr:
                country = tr.find_all("td")[1].text.lower()

                print("country : " + country)


if __name__ == '__main__':
    unittest.main()
