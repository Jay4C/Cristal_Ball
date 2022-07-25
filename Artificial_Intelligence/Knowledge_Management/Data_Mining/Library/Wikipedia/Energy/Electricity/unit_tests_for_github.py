import time
import unittest
import requests
from bs4 import BeautifulSoup


class UnitTestsDataMiningWikipediaElectricity(unittest.TestCase):
    def test_extract_the_list_of_countries_by_electricity_consumption(self):
        print('test_extract_the_list_of_countries_by_electricity_consumption')

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://en.wikipedia.org/wiki/List_of_countries_by_electricity_consumption"

        # Request the content of a page from the url
        html = requests.get(url, headers=headers)

        # print(html.content)

        time.sleep(3)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.content, 'html.parser')

        data = []

        if soup.find_all("tbody")[0] is not None:
            all_tr = soup.find_all("tbody")[0].find_all("tr")

            for tr in all_tr:
                if tr.find('td'):
                    rank = tr.find_all('td')[0].text.replace('\n', '')
                    country_region = tr.find_all('td')[1].text.replace('\xa0', '').replace('\n', '')
                    total_electricity_consumption_in_gwh_per_year = tr.find_all('td')[2].text.replace(',', '')\
                        .replace('\n', '').replace('[contradictory]', '')
                    year_of_data = tr.find_all('td')[3].text.replace(' est.', '').replace('\n', '')
                    source = tr.find_all('td')[4].text.replace('\n', '').replace('[4]', '').replace('[5]', '')\
                        .replace('[6]', '')
                    population = tr.find_all('td')[5].text.replace(',', '').replace('\n', '')
                    as_of = tr.find_all('td')[6].text.replace('\n', '').replace(' est.', '')
                    average_electrical_power_per_capita_expressed_in_kwh_per_year = tr.find_all('td')[7].text\
                        .replace('\n', '').replace(',', '')
                    average_electrical_power_per_capita_expressed_in_watts = tr.find_all('td')[8].text\
                        .replace('\n', '').replace(',', '')

                    data_element = {
                        'rank': rank,
                        'country_region': country_region,
                        'total_electricity_consumption_in_gwh_per_year': total_electricity_consumption_in_gwh_per_year,
                        'year_of_data': year_of_data,
                        'source': source,
                        'population': population,
                        'as_of': as_of,
                        'average_electrical_power_per_capita_expressed_in_kwh_per_year':
                            average_electrical_power_per_capita_expressed_in_kwh_per_year,
                        'average_electrical_power_per_capita_expressed_in_watts':
                            average_electrical_power_per_capita_expressed_in_watts
                    }

                    data.append(data_element)

                    print(str(data_element) + ",")
        else:
            print("no tbody")


if __name__ == '__main__':
    unittest.main()
