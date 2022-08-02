import time
import unittest
import requests
from bs4 import BeautifulSoup


class UnitTestsDataMiningWikipediaNaturalGas(unittest.TestCase):
    # ok
    def test_extract_the_list_of_countries_by_natural_gas_proven_reserves(self):
        print('test_extract_the_list_of_countries_by_natural_gas_proven_reserves')

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://en.wikipedia.org/wiki/List_of_countries_by_natural_gas_proven_reserves"

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
                    country_region = tr.find_all('td')[0].text.replace('\xa0', '').replace('\n', '')\
                        .replace('\u202f*', '')
                    us_eia_start_of_2021 = tr.find_all('td')[1].text.replace(',', '')\
                        .replace('\n', '').replace('[contradictory]', '').replace(' (2019)', '').replace(' (2020)', '')\
                        .replace(' (2021)', '').replace(' (2022)', '')
                    opec_start_of_2018 = tr.find_all('td')[2].text.replace(' est.', '').replace('\n', '')
                    bp_start_of_2018 = tr.find_all('td')[3].text.replace('\n', '').replace('[4]', '').replace('[5]', '')\
                        .replace('[6]', '').replace(',', '')
                    other = tr.find_all('td')[4].text.replace(',', '').replace('\n', '')
                    production_in_cubic_km_per_year_in_2020 = tr.find_all('td')[5].text.replace('\n', '')\
                        .replace(' est.', '').replace(' (2019)', '').replace(' (2020)', '').replace(' (2021)', '')\
                        .replace(' (2022)', '')
                    years_of_production_in_reserve = tr.find_all('td')[6].text\
                        .replace('\n', '').replace(',', '').replace(' (2019)', '').replace(' (2020)', '')\
                        .replace(' (2021)', '').replace(' (2022)', '')

                    data_element = {
                        'country_region': country_region,
                        'us_eia_start_of_2021': us_eia_start_of_2021,
                        'opec_start_of_2018': opec_start_of_2018,
                        'bp_start_of_2018': bp_start_of_2018,
                        'other': other,
                        'production_in_cubic_km_per_year_in_2020': production_in_cubic_km_per_year_in_2020,
                        'years_of_production_in_reserve': years_of_production_in_reserve
                    }

                    data.append(data_element)

                    print(str(data_element) + ",")
        else:
            print("no tbody")

    # ok
    def test_extract_the_list_of_countries_by_natural_gas_consumption(self):
        print('test_extract_the_list_of_countries_by_natural_gas_consumption')

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://en.wikipedia.org/wiki/List_of_countries_by_natural_gas_consumption"

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
                    country_region = tr.find_all('td')[0].text.replace('\xa0', '').replace('\n', '')
                    natural_gas_consumption_in_million_cubic_meter_per_year = tr.find_all('td')[1].text\
                        .replace(',', '').replace('\n', '').replace('[contradictory]', '')
                    date_of_information = tr.find_all('td')[2].text.replace(' est.', '').replace('\n', '')

                    data_element = {
                        'country_region': country_region,
                        'natural_gas_consumption_in_million_cubic_meter_per_year':
                            natural_gas_consumption_in_million_cubic_meter_per_year,
                        'date_of_information': date_of_information
                    }

                    data.append(data_element)

                    print(str(data_element) + ",")
        else:
            print("no tbody")

    # ok
    def test_extract_the_list_of_countries_by_natural_gas_production(self):
        print('test_extract_the_list_of_countries_by_natural_gas_production')

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://en.wikipedia.org/wiki/List_of_countries_by_natural_gas_production"

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
                    rank = tr.find_all('td')[0].text.replace('\xa0', '').replace('\n', '')
                    country_region = tr.find_all('td')[1].text.replace('\xa0', '').replace('\n', '')
                    continent = tr.find_all('td')[2].text.replace(',', '').replace('\n', '')\
                        .replace('[contradictory]', '')
                    annual_ng_production_in_million_cubic_meter = tr.find_all('td')[2].text\
                        .replace(' est.', '').replace('\n', '').replace('[1]', '')
                    date_of_information = tr.find_all('td')[3].text \
                        .replace(' est.', '').replace('\n', '').replace('[1]', '')

                    data_element = {
                        'rank': rank,
                        'country_region': country_region,
                        'continent': continent,
                        'annual_ng_production_in_million_cubic_meter': annual_ng_production_in_million_cubic_meter,
                        'date_of_information': date_of_information
                    }

                    data.append(data_element)

                    print(str(data_element) + ",")
        else:
            print("no tbody")

    # ok
    def test_extract_the_list_of_countries_by_natural_gas_imports(self):
        print('test_extract_the_list_of_countries_by_natural_gas_imports')

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://en.wikipedia.org/wiki/List_of_countries_by_natural_gas_imports"

        # Request the content of a page from the url
        html = requests.get(url, headers=headers)

        time.sleep(3)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.content, 'html.parser')

        data = []

        if soup.find_all("tbody")[1] is not None:
            all_tr = soup.find_all("tbody")[1].find_all("tr")

            for tr in all_tr:
                if tr.find('td'):
                    country_region = tr.find_all('td')[0].text.replace('\xa0', '').replace('\n', '')

                    natural_gas_for_imports_in_cubic_meter_per_year = tr.find_all('td')[1].text.replace(',', '')\
                        .replace('\n', '').replace('[contradictory]', '')

                    date_of_information = tr.find_all('td')[2].text.replace(',', '') \
                        .replace('\n', '').replace('[contradictory]', '').replace(' est.', '')

                    data_element = {
                        'country_region': country_region,
                        'natural_gas_for_imports_in_cubic_meter_per_year':
                            natural_gas_for_imports_in_cubic_meter_per_year,
                        'date_of_information': date_of_information
                    }

                    data.append(data_element)

                    print(str(data_element) + ",")
        else:
            print("no tbody")

    # ok
    def test_extract_the_list_of_countries_by_natural_gas_exports(self):
        print('test_extract_the_list_of_countries_by_natural_gas_exports')

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://en.wikipedia.org/wiki/List_of_countries_by_natural_gas_exports"

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
                    country_region = tr.find_all('td')[0].text.replace('\xa0', '').replace('\n', '')\
                        .replace('\u202f*', '')

                    natural_gas_exports_in_cubic_meter_per_year = tr.find_all('td')[1].text.replace(',', '')\
                        .replace('\n', '').replace('[contradictory]', '')

                    date_of_information = tr.find_all('td')[2].text.replace(' est.', '').replace('\n', '')\
                        .replace('[1]', '').replace(' est.', '').replace('FY ', '')

                    data_element = {
                        'country_region': country_region,
                        'natural_gas_exports_in_cubic_meter_per_year': natural_gas_exports_in_cubic_meter_per_year,
                        'date_of_information': date_of_information
                    }

                    data.append(data_element)

                    print(str(data_element) + ",")
        else:
            print("no tbody")


if __name__ == '__main__':
    unittest.main()
