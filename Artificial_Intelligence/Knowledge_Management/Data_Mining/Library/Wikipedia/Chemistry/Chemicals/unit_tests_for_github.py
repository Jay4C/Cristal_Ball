import time
import unittest
import requests
from bs4 import BeautifulSoup


class UnitTestsDataMiningWikipediaChemistryChemicals(unittest.TestCase):
    # ok
    def test_extract_the_list_of_chemical_elements(self):
        print('test_extract_the_list_of_chemical_elements')

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://en.wikipedia.org/wiki/List_of_chemical_elements"

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
                    atomic_number = tr.find_all('td')[0].text.replace(',', '').replace('\n', '')

                    symbol = tr.find_all('td')[1].text.replace(',', '').replace('\n', '')

                    name = tr.find_all('td')[2].text.replace(',', '').replace('\n', '')

                    origin_of_name = tr.find_all('td')[3].text.replace(',', '').replace('\n', '')

                    group = tr.find_all('td')[4].text.replace(',', '').replace('\n', '')

                    period = tr.find_all('td')[5].text.replace(',', '').replace('\n', '')

                    block = tr.find_all('td')[6].text.replace(',', '').replace('\n', '')

                    standard_atomic_weight = tr.find_all('td')[7].text.replace(',', '').replace('\n', '')

                    density = tr.find_all('td')[8].text.replace(',', '').replace('\n', '')

                    melting_point = tr.find_all('td')[9].text.replace(',', '').replace('\n', '')

                    boiling_point = tr.find_all('td')[10].text.replace(',', '').replace('\n', '')

                    specific_heat_capacity = tr.find_all('td')[11].text.replace(',', '').replace('\n', '')

                    electronegativity = tr.find_all('td')[12].text.replace(',', '').replace('\n', '')

                    abundance_in_earth_crust = tr.find_all('td')[13].text.replace(',', '').replace('\n', '')

                    origin = tr.find_all('td')[14].text.replace(',', '').replace('\n', '')

                    phase_at_r_t = tr.find_all('td')[15].text.replace(',', '').replace('\n', '')

                    data_element = {
                        'element': {
                            'atomic_number': atomic_number,
                            'symbol': symbol,
                            'name': name
                        },
                        'origin_of_name': origin_of_name,
                        'group': group,
                        'period': period,
                        'block': block,
                        'standard_atomic_weight': standard_atomic_weight,
                        'density': density,
                        'melting_point': melting_point,
                        'boiling_point': boiling_point,
                        'specific_heat_capacity': specific_heat_capacity,
                        'electronegativity': electronegativity,
                        'abundance_in_earth_crust': abundance_in_earth_crust,
                        'origin': origin,
                        'phase_at_r_t': phase_at_r_t
                    }

                    data.append(data_element)

                    print(str(data_element) + ",")
        else:
            print("no tbody")

    # ok
    def test_extract_the_abundance_of_elements_in_earth_crust(self):
        print('test_extract_the_abundance_of_elements_in_earth_crust')

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://en.wikipedia.org/wiki/Abundance_of_elements_in_Earth%27s_crust"

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
                    z = tr.find_all('td')[0].text.replace(',', '').replace('\n', '')

                    name = tr.find_all('td')[1].text.replace(',', '').replace('\n', '')

                    symbol = tr.find_all('td')[2].text.replace(',', '').replace('\n', '')

                    darling = tr.find_all('td')[3].text.replace(',', '').replace('\n', '')

                    barbalace = tr.find_all('td')[4].text.replace(',', '').replace('\n', '')

                    webelements = tr.find_all('td')[5].text.replace(',', '').replace('\n', '')

                    israel_science_and_technology = tr.find_all('td')[6].text.replace(',', '').replace('\n', '')

                    crc = tr.find_all('td')[7].text.replace(',', '').replace('\n', '')

                    annual_production_by_extraction_in_2016_in_tonnes = tr.find_all('td')[8].text.replace(',', '')\
                        .replace('\n', '')

                    data_element = {
                        'element': {
                            'z': z,
                            'name': name,
                            'symbol': symbol
                        },
                        'abundance_by_source_in_ppm': {
                            'darling': darling,
                            'barbalace': barbalace,
                            'webelements': webelements,
                            'israel_science_and_technology': israel_science_and_technology,
                            'crc': crc
                        },
                        'annual_production_by_extraction_in_2016_in_tonnes':
                            annual_production_by_extraction_in_2016_in_tonnes
                    }

                    data.append(data_element)

                    print(str(data_element) + ",")
        else:
            print("no tbody")


if __name__ == '__main__':
    unittest.main()
