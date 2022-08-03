import time
import unittest
import requests
from bs4 import BeautifulSoup


class UnitTestsDataMiningWikipediaCoal(unittest.TestCase):
    # ok
    def test_extract_the_list_of_countries_by_coal_proven_reserves(self):
        print('test_extract_the_list_of_countries_by_coal_proven_reserves')

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://en.wikipedia.org/wiki/List_of_countries_by_coal_reserves"

        # Request the content of a page from the url
        html = requests.get(url, headers=headers)

        # print(html.content)

        time.sleep(3)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.content, 'html.parser')

        data = []

        if soup.find_all("tbody")[2] is not None:
            all_tr = soup.find_all("tbody")[2].find_all("tr")

            for tr in all_tr:
                if tr.find('td'):
                    rank = tr.find_all('td')[0].text.replace('\xa0', '').replace('\n', '') \
                        .replace('\u202f*', '')

                    country_region = tr.find_all('td')[1].text.replace('\xa0', '').replace('\n', '')\
                        .replace('\u202f*', '')

                    anthracite_and_bituminous_in_tonnes = tr.find_all('td')[2].text.replace(',', '')\
                        .replace('\n', '').replace('[contradictory]', '').replace(' (2019)', '')\
                        .replace(' (2020)', '').replace(' (2021)', '').replace(' (2022)', '')

                    anthracite_and_bituminous_in_percentage = tr.find_all('td')[3].text.replace('%', '')\
                        .replace('\n', '')

                    subbituminous_and_lignite_in_tonnes = tr.find_all('td')[4].text.replace(',', '') \
                        .replace('\n', '').replace('[contradictory]', '').replace(' (2019)', '')\
                        .replace(' (2020)', '').replace(' (2021)', '').replace(' (2022)', '')

                    subbituminous_and_lignite_in_percentage = tr.find_all('td')[5].text.replace('%', '')\
                        .replace('\n', '')

                    total_in_tonnes = tr.find_all('td')[6].text.replace(',', '') \
                        .replace('\n', '').replace('[contradictory]', '').replace(' (2019)', '')\
                        .replace(' (2020)', '').replace(' (2021)', '').replace(' (2022)', '')

                    total_in_percentage = tr.find_all('td')[7].text.replace('%', '').replace('\n', '')

                    data_element = {
                        'rank': rank,
                        'country_region': country_region,
                        'anthracite_and_bituminous_in_tonnes': anthracite_and_bituminous_in_tonnes,
                        'anthracite_and_bituminous_in_percentage': anthracite_and_bituminous_in_percentage,
                        'subbituminous_and_lignite_in_tonnes': subbituminous_and_lignite_in_tonnes,
                        'subbituminous_and_lignite_in_percentage': subbituminous_and_lignite_in_percentage,
                        'total_in_tonnes': total_in_tonnes,
                        'total_in_percentage': total_in_percentage
                    }

                    data.append(data_element)

                    print(str(data_element) + ",")
        else:
            print("no tbody")

    # ok
    def test_extract_the_list_of_countries_by_coal_consumption(self):
        print('test_extract_the_list_of_countries_by_coal_consumption')

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://en.wikipedia.org/wiki/Coal#Major_consumers"

        # Request the content of a page from the url
        html = requests.get(url, headers=headers)

        # print(html.content)

        time.sleep(3)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.content, 'html.parser')

        data = []

        if soup.find_all("tbody")[5] is not None:
            all_tr = soup.find_all("tbody")[5].find_all("tr")

            for tr in all_tr:
                if tr.find('td'):
                    country_region = tr.find_all('td')[0].text.replace('\xa0', '').replace('\n', '')

                    coal_consumption_in_millions_tonnes_in_2008 = tr.find_all('td')[1].text\
                        .replace(',', '').replace('\n', '')

                    coal_consumption_in_millions_tonnes_in_2009 = tr.find_all('td')[2].text \
                        .replace(',', '').replace('\n', '')

                    coal_consumption_in_millions_tonnes_in_2010 = tr.find_all('td')[3].text \
                        .replace(',', '').replace('\n', '')

                    coal_consumption_in_millions_tonnes_in_2011 = tr.find_all('td')[4].text \
                        .replace(',', '').replace('\n', '')

                    coal_consumption_in_millions_tonnes_in_2012 = tr.find_all('td')[5].text \
                        .replace(',', '').replace('\n', '')

                    coal_consumption_in_millions_tonnes_in_2013 = tr.find_all('td')[6].text \
                        .replace(',', '').replace('\n', '')

                    coal_consumption_in_millions_tonnes_in_2014 = tr.find_all('td')[7].text \
                        .replace(',', '').replace('\n', '')

                    coal_consumption_in_millions_tonnes_in_2015 = tr.find_all('td')[8].text \
                        .replace(',', '').replace('\n', '').split('=')[1].replace(' ', '')

                    coal_consumption_in_millions_tonnes_in_2016 = tr.find_all('td')[9].text \
                        .replace(',', '').replace('\n', '').split('=')[1].replace(' ', '')

                    share_in_percentage = tr.find_all('td')[10].text.replace(',', '').replace('\n', '').replace('%', '')

                    data_element = {
                        'country_region': country_region,
                        'coal_consumption_in_millions_tonnes_in_2008': coal_consumption_in_millions_tonnes_in_2008,
                        'coal_consumption_in_millions_tonnes_in_2009': coal_consumption_in_millions_tonnes_in_2009,
                        'coal_consumption_in_millions_tonnes_in_2010': coal_consumption_in_millions_tonnes_in_2010,
                        'coal_consumption_in_millions_tonnes_in_2011': coal_consumption_in_millions_tonnes_in_2011,
                        'coal_consumption_in_millions_tonnes_in_2012': coal_consumption_in_millions_tonnes_in_2012,
                        'coal_consumption_in_millions_tonnes_in_2013': coal_consumption_in_millions_tonnes_in_2013,
                        'coal_consumption_in_millions_tonnes_in_2014': coal_consumption_in_millions_tonnes_in_2014,
                        'coal_consumption_in_millions_tonnes_in_2015': coal_consumption_in_millions_tonnes_in_2015,
                        'coal_consumption_in_millions_tonnes_in_2016': coal_consumption_in_millions_tonnes_in_2016,
                        'share_in_percentage': share_in_percentage,
                    }

                    data.append(data_element)

                    print(str(data_element) + ",")
        else:
            print("no tbody")

    # ok
    def test_extract_the_list_of_countries_by_coal_production(self):
        print('test_extract_the_list_of_countries_by_coal_production')

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://en.wikipedia.org/wiki/List_of_countries_by_coal_production"

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
                    country_region = tr.find_all('td')[0].text.replace('\xa0', '').replace('\n', '').replace('[7]', '')

                    coal_production_in_million_tonnes_in_2020 = tr.find_all('td')[1].text.replace(',', '')\
                        .replace('\n', '')

                    coal_production_in_million_tonnes_in_2019 = tr.find_all('td')[2].text.replace(',', '') \
                        .replace('\n', '')

                    coal_production_in_million_tonnes_in_2018 = tr.find_all('td')[3].text.replace(',', '') \
                        .replace('\n', '')

                    coal_production_in_million_tonnes_in_2017 = tr.find_all('td')[4].text.replace(',', '') \
                        .replace('\n', '')

                    coal_production_in_million_tonnes_in_2016 = tr.find_all('td')[5].text.replace(',', '') \
                        .replace('\n', '')

                    coal_production_in_million_tonnes_in_2015 = tr.find_all('td')[6].text.replace(',', '') \
                        .replace('\n', '')

                    coal_production_in_million_tonnes_in_2014 = tr.find_all('td')[7].text.replace(',', '') \
                        .replace('\n', '')

                    coal_production_in_million_tonnes_in_2013 = tr.find_all('td')[8].text.replace(',', '') \
                        .replace('\n', '')

                    coal_production_in_million_tonnes_in_2007 = tr.find_all('td')[9].text.replace(',', '') \
                        .replace('\n', '')

                    data_element = {
                        'country_region': country_region,
                        'coal_production_in_million_tonnes_in_2020': coal_production_in_million_tonnes_in_2020,
                        'coal_production_in_million_tonnes_in_2019': coal_production_in_million_tonnes_in_2019,
                        'coal_production_in_million_tonnes_in_2018': coal_production_in_million_tonnes_in_2018,
                        'coal_production_in_million_tonnes_in_2017': coal_production_in_million_tonnes_in_2017,
                        'coal_production_in_million_tonnes_in_2016': coal_production_in_million_tonnes_in_2016,
                        'coal_production_in_million_tonnes_in_2015': coal_production_in_million_tonnes_in_2015,
                        'coal_production_in_million_tonnes_in_2014': coal_production_in_million_tonnes_in_2014,
                        'coal_production_in_million_tonnes_in_2013': coal_production_in_million_tonnes_in_2013,
                        'coal_production_in_million_tonnes_in_2007': coal_production_in_million_tonnes_in_2007,
                    }

                    data.append(data_element)

                    print(str(data_element) + ",")
        else:
            print("no tbody")

    # ok
    def test_extract_the_list_of_countries_by_coal_imports(self):
        print('test_extract_the_list_of_countries_by_coal_imports')

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://en.wikipedia.org/wiki/Coal#Major_importers"

        # Request the content of a page from the url
        html = requests.get(url, headers=headers)

        time.sleep(3)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.content, 'html.parser')

        data = []

        if soup.find_all("tbody")[7] is not None:
            all_tr = soup.find_all("tbody")[7].find_all("tr")

            for tr in all_tr:
                if tr.find('td'):
                    country_region = tr.find_all('td')[0].text.replace('\xa0', '').replace('\n', '').replace(',', '')

                    imports_of_coal_in_millions_tonnes_in_2008 = tr.find_all('td')[1].text.replace('\xa0', '')\
                        .replace('\n', '').replace(',', '')

                    data_element = {
                        'country_region': country_region,
                        'imports_of_coal_in_millions_tonnes_in_2008': imports_of_coal_in_millions_tonnes_in_2008
                    }

                    data.append(data_element)

                    print(str(data_element) + ",")
        else:
            print("no tbody")

    # ok
    def test_extract_the_list_of_countries_by_coal_exports(self):
        print('test_extract_the_list_of_countries_by_coal_exports')

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://en.wikipedia.org/wiki/Coal#Major_exporters"

        # Request the content of a page from the url
        html = requests.get(url, headers=headers)

        # print(html.content)

        time.sleep(3)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.content, 'html.parser')

        data = []

        if soup.find_all("tbody")[6] is not None:
            all_tr = soup.find_all("tbody")[6].find_all("tr")

            for tr in all_tr:
                if tr.find('td'):
                    country_region = tr.find_all('td')[0].text.replace('\xa0', '').replace('\n', '').replace(',', '')

                    exports_of_coal_in_millions_tonnes_in_2008 = tr.find_all('td')[1].text.replace('\xa0', '')\
                        .replace('\n', '').replace(',', '')

                    data_element = {
                        'country_region': country_region,
                        'exports_of_coal_in_millions_tonnes_in_2008': exports_of_coal_in_millions_tonnes_in_2008,
                    }

                    data.append(data_element)

                    print(str(data_element) + ",")
        else:
            print("no tbody")


if __name__ == '__main__':
    unittest.main()
