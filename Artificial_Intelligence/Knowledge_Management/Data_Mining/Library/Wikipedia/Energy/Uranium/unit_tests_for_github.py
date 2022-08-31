import time
import unittest
import requests
from bs4 import BeautifulSoup


class UnitTestsDataMiningWikipediaUranium(unittest.TestCase):
    # ok
    def test_extract_the_list_of_countries_by_uranium_proven_reserves(self):
        print('test_extract_the_list_of_countries_by_uranium_proven_reserves')

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://en.wikipedia.org/wiki/List_of_countries_by_uranium_reserves"

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
                    country_region = tr.find_all('th')[0].text.replace('\xa0', '').replace('\n', '')\
                        .replace('\u202f*', '').replace('(OPEC)', '')

                    reserves_as_of_2019 = tr.find_all('td')[0].text.replace(',', '')\
                        .replace('\n', '')

                    historical_production_to_2014 = tr.find_all('td')[1].text.replace(',', '')\
                        .replace('\n', '').replace('[3]', '').replace('[4]', '').replace('[5]', '')

                    data_element = {
                        'country_region': country_region,
                        'reserves_as_of_2019': reserves_as_of_2019,
                        'historical_production_to_2014': historical_production_to_2014
                    }

                    data.append(data_element)

                    print(str(data_element) + ",")
        else:
            print("no tbody")

    # ok
    def test_extract_the_list_of_countries_by_uranium_consumption(self):
        print('test_extract_the_list_of_countries_by_uranium_consumption')

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://www.worldatlas.com/articles/the-leading-uranium-consuming-countries-in-the-world.html"

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

                    uranium_consumption_in_2015_in_1000_metric_tons = tr.find_all('td')[2].text.replace(',', '')\
                        .replace('\n', '').replace('[4]', '').replace('[5]', '').replace('[6]', '')

                    data_element = {
                        'rank': rank,
                        'country_region': country_region,
                        'uranium_consumption_in_2015_in_1000_metric_tons':
                            uranium_consumption_in_2015_in_1000_metric_tons
                    }

                    data.append(data_element)

                    print(str(data_element) + ",")
        else:
            print("no tbody")

    # ok
    def test_extract_the_list_of_countries_by_uranium_production(self):
        print('test_extract_the_list_of_countries_by_uranium_production')

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://en.wikipedia.org/wiki/List_of_countries_by_uranium_production"

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
                    rank = tr.find_all('td')[0].text.replace('\xa0', '').replace('\n', '')

                    country_region = tr.find_all('td')[1].text.replace('\xa0', '').replace('\n', '')

                    uranium_production_in_2018_in_tonnes = tr.find_all('td')[2].text.replace(',', '')\
                        .replace('\n', '').replace('[2]', '').replace('[3]', '')

                    percentage_of_world_production_in_2018 = tr.find_all('td')[3].text.replace(',', '')\
                        .replace('\n', '').replace('%', '').replace('[2]', '').replace('[3]', '')\
                        .replace('< ', '')

                    data_element = {
                        'rank': rank,
                        'country_region': country_region,
                        'uranium_production_in_2018_in_tonnes': uranium_production_in_2018_in_tonnes,
                        'percentage_of_world_production_in_2018': percentage_of_world_production_in_2018,
                    }

                    data.append(data_element)

                    print(str(data_element) + ",")
        else:
            print("no tbody")

    # ok
    def test_extract_the_list_of_countries_by_uranium_imports(self):
        print('test_extract_the_list_of_countries_by_uranium_imports')

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://wits.worldbank.org/trade/comtrade/en/country/ALL/year/2019/tradeflow/Imports/partner/WLD/product/261210"

        # Request the content of a page from the url
        html = requests.get(url, headers=headers)

        time.sleep(3)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.content, 'html.parser')

        data = []

        if soup.find_all("tbody")[0] is not None:
            all_tr = soup.find_all("tbody")[0].find_all("tr")

            for tr in all_tr:
                if tr.find('td'):
                    reporter = tr.find_all('td')[0].text.replace('\xa0', '').replace('\n', '').replace(',', '')

                    trade_flow = tr.find_all('td')[1].text.replace('\xa0', '')\
                        .replace('\n', '').replace(',', '')

                    product_code = tr.find_all('td')[2].text.replace('\xa0', '') \
                        .replace('\n', '').replace(',', '').replace('[3]', '').replace('[4]', '')

                    product_description = tr.find_all('td')[3].text.replace('\xa0', '') \
                        .replace('\n', '').replace(',', '').replace('[3]', '').replace('[4]', '')

                    year = tr.find_all('td')[4].text.replace('\xa0', '') \
                        .replace('\n', '').replace(',', '').replace('[3]', '').replace('[4]', '')

                    partner = tr.find_all('td')[5].text.replace('\xa0', '') \
                        .replace('\n', '').replace(',', '').replace('[3]', '').replace('[4]', '')

                    trade_value_in_thousand_usd = tr.find_all('td')[6].text.replace('\xa0', '') \
                        .replace('\n', '').replace(',', '').replace('[3]', '').replace('[4]', '')

                    quantity = tr.find_all('td')[7].text.replace('\xa0', '') \
                        .replace('\n', '').replace(',', '').replace('[3]', '').replace('[4]', '')

                    quantity_unit = tr.find_all('td')[8].text.replace('\xa0', '') \
                        .replace('\n', '').replace(',', '').replace('[3]', '').replace('[4]', '').lower()

                    data_element = {
                        'reporter': reporter,
                        'trade_flow': trade_flow,
                        'product_code': product_code,
                        'product_description': product_description,
                        'year': year,
                        'partner': partner,
                        'trade_value_in_thousand_usd': trade_value_in_thousand_usd,
                        'quantity': quantity,
                        'quantity_unit': quantity_unit
                    }

                    data.append(data_element)

                    print(str(data_element) + ",")
        else:
            print("no tbody")

    # ok
    def test_extract_the_list_of_countries_by_uranium_exports(self):
        print('test_extract_the_list_of_countries_by_uranium_exports')

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://www.worldstopexports.com/uranium-exports-by-country/#:~:text=Uranium%20Exports%20by%20Country%201%20Kazakhstan%3A%20US%241.5%20billion,South%20Africa%3A%20%247%20million%20%280.2%25%29%20More%20items...%20"

        # Request the content of a page from the url
        html = requests.get(url, headers=headers)

        time.sleep(3)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.content, 'html.parser')

        data = []

        if soup.find_all("ol")[0] is not None:
            all_li = soup.find_all("ol")[0].find_all("li")

            for li in all_li:
                country_region = li.text.split(':')[0]

                value_worth_of_natural_uranium_in_2021 = li.text.split(':')[1].split('(')[0]

                percentage_of_global_exports = li.text.split(':')[1].split('(')[1].split('%')[0]

                data_element = {
                    'country_region': country_region,
                    'value_worth_of_natural_uranium_in_2021': value_worth_of_natural_uranium_in_2021,
                    'percentage_of_global_exports': percentage_of_global_exports,
                }

                data.append(data_element)

                print(str(data_element) + ",")
        else:
            print("no tbody")


if __name__ == '__main__':
    unittest.main()
