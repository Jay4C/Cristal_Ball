import time
import unittest
import requests
from bs4 import BeautifulSoup


class UnitTestsDataMiningWikipediaElectricity(unittest.TestCase):
    # ok
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

    # ok
    def test_extract_the_list_of_countries_by_electricity_producion(self):
        print('test_extract_the_list_of_countries_by_electricity_producion')

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://en.wikipedia.org/wiki/List_of_countries_by_electricity_production"

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
                    country_region = ''

                    if tr.find_all('th')[0].find('b') is not None:
                        country_region += tr.find_all('th')[0].find('b').text.replace('\xa0', '').replace('\n', '')
                    else:
                        country_region += tr.find_all('th')[0].find('a').text.replace('\xa0', '').replace('\n', '')

                    electricity_production_in_gwh = tr.find_all('td')[0].find('span').text.replace(',', '')\
                        .replace('\n', '').replace('[contradictory]', '')
                    year = tr.find_all('td')[1].find('span').text.replace(' est.', '').replace('\n', '')\
                        .replace('[1]', '')

                    data_element = {
                        'country_region': country_region,
                        'electricity_production_in_gwh': electricity_production_in_gwh,
                        'year': year
                    }

                    data.append(data_element)

                    print(str(data_element) + ",")
        else:
            print("no tbody")

    # ok
    def test_extract_the_list_of_countries_by_electricity_producion_by_source(self):
        print('test_extract_the_list_of_countries_by_electricity_producion_by_source')

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://en.wikipedia.org/wiki/List_of_countries_by_electricity_production"

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
                    country_region = ''

                    try:
                        if tr.find_all('th')[0].find('a') is not None:
                            country_region += tr.find_all('th')[0].find('a').text.replace('\xa0', '').replace('\n', '')
                        else:
                            country_region += tr.find_all('th')[0].find('b').text.replace('\xa0', '').replace('\n', '')
                    except Exception as e:
                        print('error : ' + str(e))

                    electricity_production_in_twh = tr.find_all('td')[0].text.replace(',', '').replace('\n', '')

                    # fossil
                    coal = tr.find_all('td')[1].text.replace(',', '').replace('\n', '')
                    natural_gas = tr.find_all('td')[2].text.replace(',', '').replace('\n', '')
                    oil = tr.find_all('td')[3].text.replace(',', '').replace('\n', '')
                    sub_total_fossil = tr.find_all('td')[4].text.replace(',', '').replace('\n', '')

                    # renewable
                    hydro = tr.find_all('td')[5].text.replace(',', '').replace('\n', '')
                    other_renewable = tr.find_all('td')[6].text.replace(',', '').replace('\n', '')
                    sub_total_renewable = tr.find_all('td')[7].text.replace(',', '').replace('\n', '')

                    # nuclear
                    nuclear = tr.find_all('td')[8].text.replace(' est.', '').replace('\n', '')

                    data_element = {
                        'country_region': country_region,
                        'electricity_production_in_twh': electricity_production_in_twh,
                        'fossil': {
                            'coal': coal,
                            'natural_gas': natural_gas,
                            'oil': oil,
                            'sub_total_fossil': sub_total_fossil
                        },
                        'renewable': {
                            'hydro': hydro,
                            'other_renewable': other_renewable,
                            'sub_total_renewable': sub_total_renewable
                        },
                        'nuclear': nuclear
                    }

                    data.append(data_element)

                    print(str(data_element) + ",")
        else:
            print("no tbody")

    # ok
    def test_extract_the_list_of_countries_by_renewable_electricity_producion(self):
        print('test_extract_the_list_of_countries_by_renewable_electricity_producion')

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://en.wikipedia.org/wiki/List_of_countries_by_renewable_electricity_production"

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
                    country_region = ''

                    try:
                        if tr.find_all('th')[0].find('a') is not None:
                            country_region += tr.find_all('th')[0].find('a').text.replace('\xa0', '')\
                                .replace('\n', '').replace(' *', '')
                        else:
                            country_region += tr.find_all('th')[0].find('b').text.replace('\xa0', '').replace('\n', '')\
                                .replace(' *', '')
                    except Exception as e:
                        print('error : ' + str(e))

                    year = tr.find_all('td')[0].text.replace(',', '').replace('\n', '')
                    total_in_gwh = tr.find_all('td')[1].text.replace(',', '').replace('\n', '')
                    total_re_in_gwh = tr.find_all('td')[2].text.replace(',', '').replace('\n', '')
                    percentage_of_re_in_total = tr.find_all('td')[3].text.replace(',', '').replace('\n', '')

                    # hydropower
                    hydropower_in_gwh = tr.find_all('td')[4].text.replace(',', '').replace('\n', '')
                    hydropower_in_percentage_of_total = tr.find_all('td')[5].text.replace(',', '').replace('\n', '')
                    hydropower_in_percentage_of_re = tr.find_all('td')[6].text.replace(',', '').replace('\n', '')

                    # wind_power
                    wind_power_in_gwh = tr.find_all('td')[7].text.replace(',', '').replace('\n', '')
                    wind_power_in_percentage_of_total = tr.find_all('td')[8].text.replace(',', '').replace('\n', '')
                    wind_power_in_percentage_of_re = tr.find_all('td')[9].text.replace(',', '').replace('\n', '')

                    # biomass
                    biomass_in_gwh = tr.find_all('td')[10].text.replace(',', '').replace('\n', '')
                    biomass_in_percentage_of_total = tr.find_all('td')[11].text.replace(',', '').replace('\n', '')
                    biomass_in_percentage_of_re = tr.find_all('td')[12].text.replace(',', '').replace('\n', '')

                    # solar_power
                    solar_power_in_gwh = tr.find_all('td')[13].text.replace(',', '').replace('\n', '')
                    solar_power_in_percentage_of_total = tr.find_all('td')[14].text.replace(',', '').replace('\n', '')
                    solar_power_in_percentage_of_re = tr.find_all('td')[15].text.replace(',', '').replace('\n', '')

                    # geothermal
                    geothermal_in_gwh = tr.find_all('td')[16].text.replace(',', '').replace('\n', '')
                    geothermal_in_percentage_of_total = tr.find_all('td')[17].text.replace(',', '').replace('\n', '')
                    geothermal_in_percentage_of_re = tr.find_all('td')[18].text.replace(',', '').replace('\n', '')

                    data_element = {
                        'country_region': country_region,
                        'year': year,
                        'total_in_gwh': total_in_gwh,
                        'total_re_in_gwh': total_re_in_gwh,
                        'percentage_of_re_in_total': percentage_of_re_in_total,
                        'hydropower': {
                            'hydropower_in_gwh': hydropower_in_gwh,
                            'hydropower_in_percentage_of_total': hydropower_in_percentage_of_total,
                            'hydropower_in_percentage_of_re': hydropower_in_percentage_of_re
                        },
                        'wind_power': {
                            'wind_power_in_gwh': wind_power_in_gwh,
                            'wind_power_in_percentage_of_total': wind_power_in_percentage_of_total,
                            'wind_power_in_percentage_of_re': wind_power_in_percentage_of_re
                        },
                        'biomass': {
                            'biomass_in_gwh': biomass_in_gwh,
                            'biomass_in_percentage_of_total': biomass_in_percentage_of_total,
                            'biomass_in_percentage_of_re': biomass_in_percentage_of_re
                        },
                        'solar_power': {
                            'solar_power_in_gwh': solar_power_in_gwh,
                            'solar_power_in_percentage_of_total': solar_power_in_percentage_of_total,
                            'solar_power_in_percentage_of_re': solar_power_in_percentage_of_re
                        },
                        'geothermal': {
                            'geothermal_in_gwh': geothermal_in_gwh,
                            'geothermal_in_percentage_of_total': geothermal_in_percentage_of_total,
                            'geothermal_in_percentage_of_re': geothermal_in_percentage_of_re
                        }
                    }

                    data.append(data_element)

                    print(str(data_element) + ",")
        else:
            print("no tbody")

    # ok
    def test_extract_the_list_of_countries_by_electricity_imports(self):
        print('test_extract_the_list_of_countries_by_electricity_imports')

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://en.wikipedia.org/wiki/List_of_countries_by_electricity_imports"

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
                    country_region_1 = ''
                    country_region_2 = ''

                    if tr.find_all('td')[0].find('i') is not None:
                        country_region_1 += tr.find_all('td')[0].find('i').text.replace('\xa0', '').replace('\n', '')
                    else:
                        country_region_1 += tr.find_all('td')[0].find('a').text.replace('\xa0', '').replace('\n', '')

                    electricity_imports_in_gwh_mostly_in_2007 = tr.find_all('td')[1].text.replace(',', '')\
                        .replace('\n', '').replace('[contradictory]', '')

                    if tr.find_all('td')[2].find('i') is not None:
                        country_region_2 += tr.find_all('td')[2].find('i').text.replace('\xa0', '').replace('\n', '')\
                            .lower().capitalize()
                    else:
                        country_region_2 += tr.find_all('td')[2].text.replace('\xa0', '').replace('\n', '')\
                            .lower().capitalize()

                    electricity_imports_in_gwh_in_last_date = tr.find_all('td')[3].text.replace(',', '') \
                        .replace('\n', '').replace('[contradictory]', '')

                    last_date = tr.find_all('td')[4].text.replace(' est.', '').replace('\n', '')\
                        .replace('[1]', '').replace(' est.', '')

                    data_element = {
                        'country_region_1': country_region_1,
                        'electricity_imports_in_gwh_mostly_in_2007': electricity_imports_in_gwh_mostly_in_2007,
                        'country_region_2': country_region_2,
                        'electricity_imports_in_gwh_in_last_date': electricity_imports_in_gwh_in_last_date,
                        'last_date': last_date
                    }

                    data.append(data_element)

                    print(str(data_element) + ",")
        else:
            print("no tbody")

    # ok
    def test_extract_the_list_of_countries_by_electricity_exports(self):
        print('test_extract_the_list_of_countries_by_electricity_exports')

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://en.wikipedia.org/wiki/List_of_countries_by_electricity_exports"

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
                    country_region = ''

                    rank = tr.find_all('td')[0].text.replace('\xa0', '').replace('\n', '')

                    country_region += tr.find_all('td')[1].find('a').text.replace('\xa0', '').replace('\n', '')

                    electricity_exports_in_gwh = tr.find_all('td')[2].text.replace(',', '')\
                        .replace('\n', '').replace('[contradictory]', '')

                    date_of_information = tr.find_all('td')[3].text.replace(' est.', '').replace('\n', '')\
                        .replace('[1]', '').replace(' est.', '').replace('FY ', '')

                    data_element = {
                        'rank': rank,
                        'country_region': country_region,
                        'electricity_exports_in_gwh': electricity_exports_in_gwh,
                        'date_of_information': date_of_information
                    }

                    data.append(data_element)

                    print(str(data_element) + ",")
        else:
            print("no tbody")


if __name__ == '__main__':
    unittest.main()
