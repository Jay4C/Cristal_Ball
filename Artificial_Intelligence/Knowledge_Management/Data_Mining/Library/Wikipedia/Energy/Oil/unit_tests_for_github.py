import time
import unittest
import requests
from bs4 import BeautifulSoup


class UnitTestsDataMiningWikipediaOil(unittest.TestCase):
    # ok
    def test_extract_the_list_of_countries_by_oil_proven_reserves(self):
        print('test_extract_the_list_of_countries_by_oil_proven_reserves')

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://en.wikipedia.org/wiki/List_of_countries_by_proven_oil_reserves"

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
                    country_region = tr.find_all('th')[0].text.replace('\xa0', '').replace('\n', '')\
                        .replace('\u202f*', '').replace('(OPEC)', '')

                    proven_reserves_by_us_eia_in_millions_of_barrels = tr.find_all('td')[0].text.replace(',', '')\
                        .replace('\n', '')

                    proven_reserves_by_opec_in_millions_of_barrels = tr.find_all('td')[1].text.replace(',', '')\
                        .replace('\n', '')

                    proven_reserves_by_bp_in_millions_of_barrels = tr.find_all('td')[2].text.replace(',', '') \
                        .replace('\n', '')

                    proven_reserves_by_others_in_millions_of_barrels = tr.find_all('td')[3].text.replace(',', '')\
                        .replace('\n', '')

                    oil_production_in_2020_in_barrel_per_day = tr.find_all('td')[4].text.replace(',', '') \
                        .replace('\n', '')

                    years_of_production_in_reserve = tr.find_all('td')[5].text.replace(',', '').replace('\n', '')

                    data_element = {
                        'country_region': country_region,
                        'proven_reserves_by_us_eia_in_millions_of_barrels':
                            proven_reserves_by_us_eia_in_millions_of_barrels,
                        'proven_reserves_by_opec_in_millions_of_barrels':
                            proven_reserves_by_opec_in_millions_of_barrels,
                        'proven_reserves_by_bp_in_millions_of_barrels':
                            proven_reserves_by_bp_in_millions_of_barrels,
                        'proven_reserves_by_others_in_millions_of_barrels':
                            proven_reserves_by_others_in_millions_of_barrels,
                        'oil_production_in_2020_in_barrel_per_day': oil_production_in_2020_in_barrel_per_day,
                        'years_of_production_in_reserve': years_of_production_in_reserve
                    }

                    data.append(data_element)

                    print(str(data_element) + ",")
        else:
            print("no tbody")

    # ok
    def test_extract_the_list_of_countries_by_oil_consumption(self):
        print('test_extract_the_list_of_countries_by_oil_consumption')

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://en.wikipedia.org/wiki/List_of_countries_by_oil_consumption"

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
                    rank = tr.find_all('td')[0].text.replace(',', '').replace('\n', '')

                    country_region = tr.find_all('td')[1].text.replace('\xa0', '').replace('\n', '')

                    oil_consumption_in_barrel_per_day = tr.find_all('td')[2].text.replace(',', '')\
                        .replace('\n', '').replace('[4]', '').replace('[5]', '').replace('[6]', '')

                    year_of_consumption = tr.find_all('td')[3].text.replace(',', '').replace('\n', '')\
                        .replace(' est.', '')

                    share_in_percentage = tr.find_all('td')[4].text.replace(',', '.').replace('\n', '')

                    data_element = {
                        'rank': rank,
                        'country_region': country_region,
                        'oil_consumption_in_barrel_per_day': oil_consumption_in_barrel_per_day,
                        'year_of_consumption': year_of_consumption,
                        'share_in_percentage': share_in_percentage,
                    }

                    data.append(data_element)

                    print(str(data_element) + ",")
        else:
            print("no tbody")

    # ok
    def test_extract_the_list_of_countries_by_oil_production(self):
        print('test_extract_the_list_of_countries_by_oil_production')

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://en.wikipedia.org/wiki/List_of_countries_by_oil_production"

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
                        .replace(' (OPEC)', '')

                    oil_production_in_2021_in_barrel_per_day = tr.find_all('td')[1].text.replace(',', '')\
                        .replace('\n', '')

                    oil_production_per_capita_in_2017_in_barrel_per_day_per_million_of_people = tr.find_all('td')[2]\
                        .text.replace(',', '').replace('\n', '')

                    data_element = {
                        'country_region': country_region,
                        'oil_production_in_2021_in_barrel_per_day': oil_production_in_2021_in_barrel_per_day,
                        'oil_production_per_capita_in_2017_in_barrel_per_day_per_million_of_people':
                            oil_production_per_capita_in_2017_in_barrel_per_day_per_million_of_people,
                    }

                    data.append(data_element)

                    print(str(data_element) + ",")
        else:
            print("no tbody")

    # ok
    def test_extract_the_list_of_countries_by_oil_imports(self):
        print('test_extract_the_list_of_countries_by_oil_imports')

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://en.wikipedia.org/wiki/List_of_countries_by_oil_imports"

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
                    country_region = tr.find_all('td')[0].text.replace('\xa0', '').replace('\n', '').replace(',', '')

                    crude_oil_imports_in_barrel_per_day = tr.find_all('td')[1].text.replace('\xa0', '')\
                        .replace('\n', '').replace(',', '')

                    year_of_information = tr.find_all('td')[2].text.replace('\xa0', '') \
                        .replace('\n', '').replace(',', '').replace('[3]', '').replace('[4]', '')

                    data_element = {
                        'country_region': country_region,
                        'crude_oil_imports_in_barrel_per_day': crude_oil_imports_in_barrel_per_day,
                        'year_of_information': year_of_information
                    }

                    data.append(data_element)

                    print(str(data_element) + ",")
        else:
            print("no tbody")

    # ok
    def test_extract_the_list_of_countries_by_oil_exports(self):
        print('test_extract_the_list_of_countries_by_oil_exports')

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://en.wikipedia.org/wiki/List_of_countries_by_oil_exports"

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
                        .replace(',', '').replace(' (OPEC)', '')

                    oil_exports_in_barrel_per_day = tr.find_all('td')[1].text.replace('\xa0', '')\
                        .replace('\n', '').replace(',', '')

                    date_of_information = tr.find_all('td')[2].text.replace('\xa0', '') \
                        .replace('\n', '').replace(',', '').replace(' est.', '').replace(' est', '')

                    data_element = {
                        'country_region': country_region,
                        'oil_exports_in_barrel_per_day': oil_exports_in_barrel_per_day,
                        'date_of_information': date_of_information,
                    }

                    data.append(data_element)

                    print(str(data_element) + ",")
        else:
            print("no tbody")

    # ok
    def test_extract_the_list_of_countries_by_oil(self):
        print('test_extract_the_list_of_countries_by_oil')

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://en.wikipedia.org/wiki/Oil_by_country"

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
                    rank = tr.find_all('td')[0].text.replace('\xa0', '').replace('\n', '') \
                        .replace(',', '').replace(' (OPEC)', '')

                    country_region = tr.find_all('td')[1].text.replace('\xa0', '').replace('\n', '')\
                        .replace(',', '').replace(' (OPEC)', '')

                    proven_reserves_in_barrel = tr.find_all('td')[2].text.replace('\xa0', '')\
                        .replace('\n', '').replace(',', '')

                    date_of_information_for_proven_reserves = tr.find_all('td')[3].text.replace('\xa0', '') \
                        .replace('\n', '').replace(',', '').replace(' est.', '').replace(' est', '')

                    production_in_barrel_per_day = tr.find_all('td')[4].text.replace('\xa0', '') \
                        .replace('\n', '').replace(',', '')

                    date_of_information_for_production = tr.find_all('td')[5].text.replace('\xa0', '') \
                        .replace('\n', '').replace(',', '').replace(' est.', '').replace(' est', '')

                    consumption_in_barrel_per_day = tr.find_all('td')[6].text.replace('\xa0', '') \
                        .replace('\n', '').replace(',', '')

                    date_of_information_for_consumption = tr.find_all('td')[7].text.replace('\xa0', '') \
                        .replace('\n', '').replace(',', '').replace(' est.', '').replace(' est', '')

                    exports_in_barrel_per_day = tr.find_all('td')[8].text.replace('\xa0', '') \
                        .replace('\n', '').replace(',', '')

                    date_of_information_for_exports = tr.find_all('td')[9].text.replace('\xa0', '') \
                        .replace('\n', '').replace(',', '').replace(' est.', '').replace(' est', '')

                    imports_in_barrel_per_day = tr.find_all('td')[10].text.replace('\xa0', '') \
                        .replace('\n', '').replace(',', '')

                    date_of_information_for_imports = tr.find_all('td')[11].text.replace('\xa0', '') \
                        .replace('\n', '').replace(',', '').replace(' est.', '').replace(' est', '')

                    data_element = {
                        'rank': rank,
                        'country_region': country_region,
                        'proven_reserves_in_barrel': proven_reserves_in_barrel,
                        'date_of_information_for_proven_reserves': date_of_information_for_proven_reserves,
                        'production_in_barrel_per_day': production_in_barrel_per_day,
                        'date_of_information_for_production': date_of_information_for_production,
                        'consumption_in_barrel_per_day': consumption_in_barrel_per_day,
                        'date_of_information_for_consumption': date_of_information_for_consumption,
                        'exports_in_barrel_per_day': exports_in_barrel_per_day,
                        'date_of_information_for_exports': date_of_information_for_exports,
                        'imports_in_barrel_per_day': imports_in_barrel_per_day,
                        'date_of_information_for_imports': date_of_information_for_imports,
                    }

                    data.append(data_element)

                    print(str(data_element) + ",")
        else:
            print("no tbody")


if __name__ == '__main__':
    unittest.main()
