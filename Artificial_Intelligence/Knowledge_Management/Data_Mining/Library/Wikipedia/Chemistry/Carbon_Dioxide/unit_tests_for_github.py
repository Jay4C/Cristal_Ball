import time
import unittest
import requests
from bs4 import BeautifulSoup


class UnitTestsDataMiningWikipediaChemistryCarbonDioxide(unittest.TestCase):
    # ok
    def test_extract_the_list_of_countries_by_carbon_dioxide_emissions(self):
        print('test_extract_the_list_of_countries_by_carbon_dioxide_emissions')

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://en.wikipedia.org/wiki/List_of_countries_by_carbon_dioxide_emissions"

        # Request the content of a page from the url
        html = requests.get(url, headers=headers)

        # print(html.content)

        time.sleep(3)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.content, 'html.parser')

        data = []

        if soup.find_all("tbody")[1] is not None:
            all_tr = soup.find_all("tbody")[1].find_all("tr")

            for tr in all_tr:
                if tr.find('td'):
                    country_region = tr.find_all('td')[0].text.replace('\xa0', '').replace('\n', '')\
                        .replace('\u202f*', '').replace('(OPEC)', '')

                    fossil_co2_emissions_in_million_tons_in_1990 = tr.find_all('td')[1].text.replace(',', '')\
                        .replace('\n', '')

                    fossil_co2_emissions_in_million_tons_in_2005 = tr.find_all('td')[2].text.replace(',', '') \
                        .replace('\n', '')

                    fossil_co2_emissions_in_million_tons_in_2017 = tr.find_all('td')[3].text.replace(',', '') \
                        .replace('\n', '')

                    fossil_co2_emissions_in_2017 = tr.find_all('td')[4].text.replace(',', '') \
                        .replace('\n', '')

                    fossil_co2_emissions_for_2017_versus_1990_change = tr.find_all('td')[5].text.replace(',', '') \
                        .replace('\n', '')

                    fossil_co2_emissions_in_2017_per_land_area_in_tons_co2_per_km2_per_year = tr.find_all('td')[6].text\
                        .replace(',', '').replace('\n', '')

                    fossil_co2_emissions_in_2017_per_capita_in_tons_co2_per_capita_per_year = tr.find_all('td')[7].text\
                        .replace(',', '').replace('\n', '')

                    fossil_co2_emissions_in_2018_total_including_lucf = tr.find_all('td')[8].text \
                        .replace(',', '').replace('\n', '')

                    fossil_co2_emissions_in_2018_total_excluding_lucf = tr.find_all('td')[9].text \
                        .replace(',', '').replace('\n', '')

                    data_element = {
                        'country_region': country_region,
                        'fossil_co2_emissions_in_million_tons_in_1990': fossil_co2_emissions_in_million_tons_in_1990,
                        'fossil_co2_emissions_in_million_tons_in_2005': fossil_co2_emissions_in_million_tons_in_2005,
                        'fossil_co2_emissions_in_million_tons_in_2017': fossil_co2_emissions_in_million_tons_in_2017,
                        'fossil_co2_emissions_in_2017': fossil_co2_emissions_in_2017,
                        'fossil_co2_emissions_for_2017_versus_1990_change':
                            fossil_co2_emissions_for_2017_versus_1990_change,
                        'fossil_co2_emissions_in_2017_per_land_area_in_tons_co2_per_km2_per_year':
                            fossil_co2_emissions_in_2017_per_land_area_in_tons_co2_per_km2_per_year,
                        'fossil_co2_emissions_in_2017_per_capita_in_tons_co2_per_capita_per_year':
                            fossil_co2_emissions_in_2017_per_capita_in_tons_co2_per_capita_per_year,
                        'fossil_co2_emissions_in_2018_total_including_lucf':
                            fossil_co2_emissions_in_2018_total_including_lucf,
                        'fossil_co2_emissions_in_2018_total_excluding_lucf':
                            fossil_co2_emissions_in_2018_total_excluding_lucf
                    }

                    data.append(data_element)

                    print(str(data_element) + ",")
        else:
            print("no tbody")


if __name__ == '__main__':
    unittest.main()
