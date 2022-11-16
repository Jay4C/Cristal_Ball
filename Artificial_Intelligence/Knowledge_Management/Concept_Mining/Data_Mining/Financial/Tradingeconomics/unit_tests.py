import math
from bs4 import BeautifulSoup
import requests
import unittest
from requests_tor import RequestsTor


# https://tradingeconomics.com
class UnitTestsDataMinerTradingecononmicsWithClearWeb(unittest.TestCase):
    # https://tradingeconomics.com/calendar
    def test_extract_data_from_calendar(self):
        print("test_extract_data_from_calendar")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://tradingeconomics.com/calendar"

        # Request the content of a page from the url
        html = requests.get(url, headers=headers)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.content, 'html.parser')

        try:
            if soup.find('tr') is not None:
                all_tr = soup.find_all('tr')

                i = 0

                for tr in all_tr:
                    i += 1

                    try:
                        hour = tr.find_all('td')[0].find('span').text\
                            .replace(' ', '')\
                            .replace('\n', '')\
                            .replace('\r', '')

                        country = tr.find_all('td')[1].find_all('td')[1].text\
                            .replace(' ', '')\
                            .replace('\n', '')\
                            .replace('\r', '')

                        event = tr.find_all('td')[4].text\
                            .replace('\n', '')\
                            .replace('\r', '')

                        actual = tr.find_all('td')[5].text \
                            .replace(' ', '') \
                            .replace('\n', '')\
                            .replace('\r', '')

                        previous = tr.find_all('td')[6].find_all('span')[0].text\
                            .replace(' ', '')\
                            .replace('\n', '')\
                            .replace('\r', '')

                        consensus = tr.find_all('td')[7].text\
                            .replace(' ', '')\
                            .replace('\n', '')\
                            .replace('\r', '')

                        calendar = {
                            'hour': hour,
                            'country': country,
                            'event': event,
                            'actual': actual,
                            'previous': previous,
                            'consensus': consensus
                        }

                        print("calendar " + str(i))
                        print(calendar)
                        print('\n')
                    except Exception as e:
                        print("error from for : " + str(e))
            else:
                print("no tr")
        except Exception as e:
            print("error tr : " + str(e))

    # https://tradingeconomics.com/currencies
    def test_extract_data_from_currencies(self):
        print("test_extract_data_from_currencies")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://tradingeconomics.com/currencies"

        # Request the content of a page from the url
        html = requests.get(url, headers=headers)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.content, 'html.parser')

        try:
            if soup.find('tr') is not None:
                all_tr = soup.find_all('tr')

                i = 0

                for tr in all_tr:
                    i += 1

                    try:
                        major = tr.find_all('td')[1].find('a').find('b').text.replace(' ', '').replace('\n', '').replace('\r', '')
                        price = tr.find_all('td')[2].text.replace(" ", "").replace('\n', '').replace('\r', '')
                        volatility = tr.find_all('td')[3].get('data-value').replace(" ", "").replace('\n', '').replace('\r', '')
                        day = tr.find_all('td')[4].text.replace(" ", "").replace('\n', '').replace('\r', '')
                        weekly = tr.find_all('td')[5].text.replace(" ", "").replace('\n', '').replace('\r', '')
                        monthly = tr.find_all('td')[6].text.replace(" ", "").replace('\n', '').replace('\r', '')
                        ytd = tr.find_all('td')[7].text.replace(" ", "").replace('\n', '').replace('\r', '')
                        date = tr.find_all('td')[8].text.replace(" ", "").replace('\n', '').replace('\r', '')

                        forex_pair = {
                            'major': major,
                            'price': price,
                            'volatility': volatility,
                            'day': day,
                            'weekly': weekly,
                            'monthly': monthly,
                            'ytd': ytd,
                            'date': date
                        }

                        print("pair " + str(i))
                        print(forex_pair)
                        print('\n')
                    except Exception as e:
                        print("error from for")
            else:
                print("no tr")
        except Exception as e:
            print("error tr : " + str(e))

    # https://tradingeconomics.com/stocks
    def test_extract_data_from_stocks(self):
        print('test_extract_data_from_stocks')

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://tradingeconomics.com/stocks"

        # Request the content of a page from the url
        html = requests.get(url, headers=headers)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.content, 'html.parser')

        try:
            if soup.find('tr') is not None:
                all_tr = soup.find_all('tr')

                i = 0

                for tr in all_tr:
                    i += 1

                    try:
                        index = tr.find_all('td')[1].find('a').find('b').text.replace(' ', '').replace('\n', '').replace('\r', '')
                        price = tr.find_all('td')[2].text.replace(" ", "").replace('\n', '').replace('\r', '')
                        volatility = tr.find_all('td')[3].get('data-value').replace(" ", "").replace('\n', '').replace('\r', '')
                        day = tr.find_all('td')[4].text.replace(" ", "").replace('\n', '').replace('\r', '')
                        weekly = tr.find_all('td')[5].text.replace(" ", "").replace('\n', '').replace('\r', '')
                        monthly = tr.find_all('td')[6].text.replace(" ", "").replace('\n', '').replace('\r', '')
                        ytd = tr.find_all('td')[7].text.replace(" ", "").replace('\n', '').replace('\r', '')
                        date = tr.find_all('td')[8].text.replace(" ", "").replace('\n', '').replace('\r', '')

                        stock_index = {
                            'index': index,
                            'price': price,
                            'volatility': volatility,
                            'day': day,
                            'weekly': weekly,
                            'monthly': monthly,
                            'ytd': ytd,
                            'date': date
                        }

                        print("index " + str(i))
                        print(stock_index)
                        print('\n')
                    except Exception as e:
                        print("error from for : " + str(e))
            else:
                print("no tr")
        except Exception as e:
            print("error tr : " + str(e))

    # https://tradingeconomics.com/commodities
    def test_extract_data_from_commodities(self):
        print('test_extract_data_from_commodities')
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://tradingeconomics.com/commodities"

        # Request the content of a page from the url
        html = requests.get(url, headers=headers)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.content, 'html.parser')

        try:
            if soup.find('tr') is not None:
                all_tr = soup.find_all('tr')

                i = 0

                for tr in all_tr:
                    i += 1

                    try:
                        commodity = tr.find_all('td')[1].find('a').find('b').text\
                            .replace(' ', '')\
                            .replace('\n', '')\
                            .replace('\r', '')

                        size = tr.find_all('td')[1].find('div').text\
                            .replace(' ', '')\
                            .replace('\n', '')\
                            .replace('\r', '')

                        price = tr.find_all('td')[2].text\
                            .replace(" ", "")\
                            .replace('\n', '')\
                            .replace('\r', '')

                        volatility = tr.find_all('td')[3].get('data-value')\
                            .replace(" ", "")\
                            .replace('\n', '')\
                            .replace('\r', '')

                        day = tr.find_all('td')[4].text\
                            .replace(" ", "")\
                            .replace('\n', '')\
                            .replace('\r', '')

                        weekly = tr.find_all('td')[5].text\
                            .replace(" ", "")\
                            .replace('\n', '')\
                            .replace('\r', '')

                        monthly = tr.find_all('td')[6].text\
                            .replace(" ", "")\
                            .replace('\n', '')\
                            .replace('\r', '')

                        ytd = tr.find_all('td')[7].text\
                            .replace(" ", "")\
                            .replace('\n', '')\
                            .replace('\r', '')

                        date = tr.find_all('td')[8].text\
                            .replace(" ", "")\
                            .replace('\n', '')\
                            .replace('\r', '')

                        stock_index = {
                            'commodity': commodity,
                            "size": size,
                            'price': price,
                            'volatility': volatility,
                            'day': day,
                            'weekly': weekly,
                            'monthly': monthly,
                            'ytd': ytd,
                            'date': date
                        }

                        print("commodity " + str(i))
                        print(stock_index)
                        print('\n')
                    except Exception as e:
                        print("error from for : " + str(e))
            else:
                print("no tr")
        except Exception as e:
            print("error tr : " + str(e))

    # https://tradingeconomics.com/bonds
    def test_extract_data_from_bonds(self):
        print('test_extract_data_from_bonds')

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://tradingeconomics.com/bonds"

        # Request the content of a page from the url
        html = requests.get(url, headers=headers)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.content, 'html.parser')

        try:
            if soup.find('tr') is not None:
                all_tr = soup.find_all('tr')

                i = 0

                for tr in all_tr:
                    i += 1

                    try:
                        major_10_y = tr.find_all('td')[1].find('a').find('b').text\
                            .replace(' ', '')\
                            .replace('\n', '')\
                            .replace('\r', '')

                        efficiency = tr.find_all('td')[2].text\
                            .replace(" ", "")\
                            .replace('\n', '')\
                            .replace('\r', '')

                        volatility = tr.find_all('td')[3].get('data-value')\
                            .replace(" ", "")\
                            .replace('\n', '')\
                            .replace('\r', '')

                        day = tr.find_all('td')[4].text\
                            .replace(" ", "")\
                            .replace('\n', '')\
                            .replace('\r', '')

                        weekly = tr.find_all('td')[5].text\
                            .replace(" ", "")\
                            .replace('\n', '')\
                            .replace('\r', '')

                        monthly = tr.find_all('td')[6].text\
                            .replace(" ", "")\
                            .replace('\n', '')\
                            .replace('\r', '')

                        ytd = tr.find_all('td')[7].text\
                            .replace(" ", "")\
                            .replace('\n', '')\
                            .replace('\r', '')

                        date = tr.find_all('td')[8].text\
                            .replace(" ", "")\
                            .replace('\n', '')\
                            .replace('\r', '')

                        bond = {
                            'major_10_y': major_10_y,
                            "efficiency": efficiency,
                            'volatility': volatility,
                            'day': day,
                            'weekly': weekly,
                            'monthly': monthly,
                            'ytd': ytd,
                            'date': date
                        }

                        print("bond " + str(i))
                        print(bond)
                        print('\n')
                    except Exception as e:
                        print("error from for : " + str(e))
            else:
                print("no tr")
        except Exception as e:
            print("error tr : " + str(e))

    # https://tradingeconomics.com/earnings
    def test_extract_data_from_earnings(self):
        print("test_extract_data_from_earnings")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://tradingeconomics.com/earnings"

        # Request the content of a page from the url
        html = requests.get(url, headers=headers)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.content, 'html.parser')

        try:
            if soup.find('tr') is not None:
                all_tr = soup.find_all('tr')

                i = 0

                for tr in all_tr:
                    i += 1

                    try:
                        earning_name = tr.find_all('td')[1].find('a').text\
                            .replace(' ', '')\
                            .replace('\n', '')\
                            .replace('\r', '') + " _ " + tr.find_all('td')[1].find('span').text\
                            .replace(' ', '')\
                            .replace('\n', '')\
                            .replace('\r', '')

                        actual = tr.find_all('td')[3].text\
                            .replace(" ", "")\
                            .replace('\n', '')\
                            .replace('\r', '')

                        consensus = tr.find_all('td')[4].text\
                            .replace(" ", "")\
                            .replace('\n', '')\
                            .replace('\r', '')

                        impact = tr.find_all('td')[5].find('div').find('img').get('alt')\
                            .replace(" ", "")\
                            .replace('\n', '')\
                            .replace('\r', '')

                        earning = {
                            'earning_name': earning_name,
                            'actual': actual,
                            'consensus': consensus,
                            'imapct': impact
                        }

                        print("earning " + str(i))
                        print(earning)
                        print('\n')
                    except Exception as e:
                        print("error from for : " + str(e))
            else:
                print("no tr")
        except Exception as e:
            print("error tr : " + str(e))

    # https://tradingeconomics.com/stream
    def test_extract_data_from_news(self):
        print("test_extract_data_from_news")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://tradingeconomics.com/stream"

        # Request the content of a page from the url
        html = requests.get(url, headers=headers)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.content, 'html.parser')

        try:
            if soup.find('ul') is not None:
                all_ul = soup.find_all('ul')

                i = 0

                for ul in all_ul:
                    i += 1

                    try:
                        for li in ul.find_all('li'):
                            news_text = li.text

                            news = {
                                'news_text': news_text
                            }

                            print("news " + str(i))
                            print(news)
                            print('\n')
                    except Exception as e:
                        print("error from for : " + str(e))
            else:
                print("no tr")
        except Exception as e:
            print("error tr : " + str(e))

    # https://tradingeconomics.com/indicators?g=forecast
    def test_extract_data_from_forecast_indicators(self):
        print("test_extract_data_from_forecast_indicators")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://tradingeconomics.com/indicators?g=forecast"

        # Request the content of a page from the url
        html = requests.get(url, headers=headers)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.content, 'html.parser')

        try:
            if soup.find('li', {'class': 'list-group-item'}) is not None:
                all_li = soup.find_all('li', {'class': 'list-group-item'})

                for li in all_li:
                    try:
                        indicator = li.find('a').text
                        link = "https://tradingeconomics.com" + li.find('a').get("href")
                        print(indicator + " : " + link)
                    except Exception as e:
                        print("error from for")
            else:
                print("no tr")
        except Exception as e:
            print("error tr : " + str(e))

    # https://tradingeconomics.com/forecast/currency
    def test_extract_data_from_forecast_currencies(self):
        print("test_extract_data_from_forecast_currencies")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://tradingeconomics.com/forecast/currency"

        # Request the content of a page from the url
        html = requests.get(url, headers=headers)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.content, 'html.parser')

        try:
            if soup.find('tr') is not None:
                all_tr = soup.find_all('tr')

                i = 0

                for tr in all_tr:
                    i += 1

                    try:
                        major = tr.find_all('td')[1].find('a').find('b').text\
                            .replace(' ', '')\
                            .replace('\n', '')\
                            .replace('\r', '')

                        price = tr.find_all('td')[2].text\
                            .replace(" ", "")\
                            .replace('\n', '')\
                            .replace('\r', '')

                        volatility = tr.find_all('td')[3].get('data-value')\
                            .replace(" ", "")\
                            .replace('\n', '')\
                            .replace('\r', '')

                        day = tr.find_all('td')[4].text\
                            .replace(" ", "")\
                            .replace('\n', '')\
                            .replace('\r', '')

                        q1 = tr.find_all('td')[5].text\
                            .replace(" ", "")\
                            .replace('\n', '')\
                            .replace('\r', '')

                        q2 = tr.find_all('td')[6].text\
                            .replace(" ", "")\
                            .replace('\n', '')\
                            .replace('\r', '')

                        q3 = tr.find_all('td')[7].text\
                            .replace(" ", "")\
                            .replace('\n', '')\
                            .replace('\r', '')

                        q4 = tr.find_all('td')[8].text\
                            .replace(" ", "")\
                            .replace('\n', '')\
                            .replace('\r', '')

                        forecast_currency = {
                            'major': major,
                            'price': price,
                            'volatility': volatility,
                            'day': day,
                            'q1': q1,
                            'q2': q2,
                            'q3': q3,
                            'q4': q4
                        }

                        print("forecast_currency " + str(i))
                        print(forecast_currency)
                        print('\n')
                    except Exception as e:
                        print("error from for : " + str(e))
            else:
                print("no tr")
        except Exception as e:
            print("error tr : " + str(e))

    # https://tradingeconomics.com/forecast/commodity
    def test_extract_data_from_forecast_commodities(self):
        print("test_extract_data_from_forecast_commodities")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://tradingeconomics.com/forecast/commodity"

        # Request the content of a page from the url
        html = requests.get(url, headers=headers)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.content, 'html.parser')

        try:
            if soup.find('tr') is not None:
                all_tr = soup.find_all('tr')

                i = 0

                for tr in all_tr:
                    i += 1

                    try:
                        major = tr.find_all('td')[1].find('a').find('b').text\
                            .replace(' ', '')\
                            .replace('\n', '')\
                            .replace('\r', '')

                        price = tr.find_all('td')[2].text\
                            .replace(" ", "")\
                            .replace('\n', '')\
                            .replace('\r', '')

                        volatility = tr.find_all('td')[3].get('data-value')\
                            .replace(" ", "")\
                            .replace('\n', '')\
                            .replace('\r', '')

                        day = tr.find_all('td')[4].text\
                            .replace(" ", "")\
                            .replace('\n', '')\
                            .replace('\r', '')

                        q1 = tr.find_all('td')[5].text\
                            .replace(" ", "")\
                            .replace('\n', '')\
                            .replace('\r', '')

                        q2 = tr.find_all('td')[6].text\
                            .replace(" ", "")\
                            .replace('\n', '')\
                            .replace('\r', '')

                        q3 = tr.find_all('td')[7].text\
                            .replace(" ", "")\
                            .replace('\n', '')\
                            .replace('\r', '')

                        q4 = tr.find_all('td')[8].text\
                            .replace(" ", "")\
                            .replace('\n', '')\
                            .replace('\r', '')

                        forecast_commodity = {
                            'major': major,
                            'price': price,
                            'volatility': volatility,
                            'day': day,
                            'q1': q1,
                            'q2': q2,
                            'q3': q3,
                            'q4': q4
                        }

                        print("forecast_commodity " + str(i))
                        print(forecast_commodity)
                        print('\n')
                    except Exception as e:
                        print("error from for : " + str(e))
            else:
                print("no tr")
        except Exception as e:
            print("error tr : " + str(e))

    # https://tradingeconomics.com/forecast/government-bond-10y
    def test_extract_data_from_forecast_bonds(self):
        print("test_extract_data_from_forecast_bonds")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://tradingeconomics.com/forecast/government-bond-10y"

        # Request the content of a page from the url
        html = requests.get(url, headers=headers)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.content, 'html.parser')

        try:
            if soup.find('tr') is not None:
                all_tr = soup.find_all('tr')

                i = 0

                for tr in all_tr:
                    i += 1

                    try:
                        major = tr.find_all('td')[1].find('a').find('b').text\
                            .replace(' ', '')\
                            .replace('\n', '')\
                            .replace('\r', '')

                        efficiency = tr.find_all('td')[2].text\
                            .replace(" ", "")\
                            .replace('\n', '')\
                            .replace('\r', '')

                        volatility = tr.find_all('td')[3].get('data-value')\
                            .replace(" ", "")\
                            .replace('\n', '')\
                            .replace('\r', '')

                        day = tr.find_all('td')[4].text\
                            .replace(" ", "")\
                            .replace('\n', '')\
                            .replace('\r', '')

                        q1 = tr.find_all('td')[5].text\
                            .replace(" ", "")\
                            .replace('\n', '')\
                            .replace('\r', '')

                        q2 = tr.find_all('td')[6].text\
                            .replace(" ", "")\
                            .replace('\n', '')\
                            .replace('\r', '')

                        q3 = tr.find_all('td')[7].text\
                            .replace(" ", "")\
                            .replace('\n', '')\
                            .replace('\r', '')

                        q4 = tr.find_all('td')[8].text\
                            .replace(" ", "")\
                            .replace('\n', '')\
                            .replace('\r', '')

                        forecast_bond = {
                            'major': major,
                            'efficiency': efficiency,
                            'volatility': volatility,
                            'day': day,
                            'q1': q1,
                            'q2': q2,
                            'q3': q3,
                            'q4': q4
                        }

                        print("forecast_bond " + str(i))
                        print(forecast_bond)
                        print('\n')
                    except Exception as e:
                        print("error from for : " + str(e))
            else:
                print("no tr")
        except Exception as e:
            print("error tr : " + str(e))

    # https://tradingeconomics.com/indicators
    def test_extract_all_indicators_link(self):
        print("test_extract_all_indicators_link")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://tradingeconomics.com/indicators"

        # Request the content of a page from the url
        html = requests.get(url, headers=headers)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.content, 'html.parser')

        try:
            if soup.find('li', {'class': 'list-group-item'}) is not None:
                all_li = soup.find_all('li', {'class': 'list-group-item'})

                for li in all_li:
                    try:
                        indicator = li.find('a').text
                        link = "https://tradingeconomics.com" + li.find('a').get("href")
                        print(indicator + " : " + link)
                    except Exception as e:
                        print("error from for")
            else:
                print("no tr")
        except Exception as e:
            print("error tr : " + str(e))

    # https://tradingeconomics.com/country-list/inflation-rate
    def test_extract_data_of_one_indicator(self):
        print("test_extract_data_of_one_indicator")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://tradingeconomics.com/country-list/inflation-rate"

        # Request the content of a page from the url
        html = requests.get(url, headers=headers)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.content, 'html.parser')

        try:
            if soup.find('tr') is not None:
                all_tr = soup.find_all('tr')

                for tr in all_tr:
                    try:
                        country = tr.find_all('td')[0].find('a').text.replace(' ', '')
                        last = tr.find_all('td')[1].get('data-value')
                        previous = tr.find_all('td')[2].text.replace(' ', '')
                        reference = tr.find_all('td')[3].find('span').text.replace(' ', '')

                        print(country + " - " + last + " - " + previous + " - " + reference)
                    except Exception as e:
                        print("error from for")
            else:
                print("no tr")
        except Exception as e:
            print("error tr : " + str(e))


# Indicators
# Money
# Money Supply M0
class UnitTestDataMinerTradingeconomicsIndicatorsMoneySupplyM0WithDarkWeb(unittest.TestCase):
    # Money Supply M0 for USD
    def test_get_money_supply_m0_for_usd_united_states(self):
        print("test_get_money_supply_m0_for_usd_united_states")

        money_supply_m0 = 0

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://tradingeconomics.com/united-states/money-supply-m0"

        rt = RequestsTor()

        html_with_tor = rt.get(url, headers=headers)

        # Parse the content of html_doc
        soup = BeautifulSoup(html_with_tor.content, 'html.parser')

        element = soup.find('div', id="ctl00_ContentPlaceHolder1_ctl00_ctl00_Panel1")

        if element is not None:
            value = float(element.find('table', {'class': 'table table-hover'})
                          .find_all('tr', {'class': 'datatable-row'})[1].find_all('td')[1].text)

            unit = element\
                .find('table', {'class': 'table table-hover'})\
                .find_all('tr', {'class': 'datatable-row'})[1]\
                .find_all('td')[3]\
                .text\
                .split(' ')[1]

            if unit == "Million":
                money_supply_m0 += value * math.pow(10, 6)
            elif unit == "Billion":
                money_supply_m0 += value * math.pow(10, 9)
            elif unit == "Thousands":
                money_supply_m0 += value * math.pow(10, 3)

            print('money_supply_m0 : ' + str(money_supply_m0))

    def test_get_money_supply_m0_for_usd_belize(self):
        print("test_get_money_supply_m0_for_usd_belize")

        money_supply_m0 = 0

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://tradingeconomics.com/belize/money-supply-m0"

        rt = RequestsTor()

        html_with_tor = rt.get(url, headers=headers)

        # Parse the content of html_doc
        soup = BeautifulSoup(html_with_tor.content, 'html.parser')

        element = soup.find('div', id="ctl00_ContentPlaceHolder1_ctl00_ctl00_Panel1")

        if element is not None:
            value = float(element.find('table', {'class': 'table table-hover'})
                          .find_all('tr', {'class': 'datatable-row'})[1].find_all('td')[1].text)

            unit = element\
                .find('table', {'class': 'table table-hover'})\
                .find_all('tr', {'class': 'datatable-row'})[1]\
                .find_all('td')[3]\
                .text\
                .split(' ')[1]

            if unit == "Million":
                money_supply_m0 += value * math.pow(10, 6)
            elif unit == "Billion":
                money_supply_m0 += value * math.pow(10, 9)
            elif unit == "Thousands":
                money_supply_m0 += value * math.pow(10, 3)

            print('money_supply_m0 : ' + str(money_supply_m0))

    def test_get_money_supply_m0_for_usd_el_salvador(self):
        print("test_get_money_supply_m0_for_usd_el_salvador")

        money_supply_m0 = 0

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://tradingeconomics.com/el-salvador/money-supply-m0"

        rt = RequestsTor()

        html_with_tor = rt.get(url, headers=headers)

        # Parse the content of html_doc
        soup = BeautifulSoup(html_with_tor.content, 'html.parser')

        element = soup.find('div', id="ctl00_ContentPlaceHolder1_ctl00_ctl00_Panel1")

        if element is not None:
            value = float(element.find('table', {'class': 'table table-hover'})
                          .find_all('tr', {'class': 'datatable-row-alternating'})[0]
                          .find_all('td')[1]
                          .text)

            unit = element\
                .find('table', {'class': 'table table-hover'})\
                .find_all('tr', {'class': 'datatable-row-alternating'})[0]\
                .find_all('td')[3]\
                .text\
                .split(' ')[1]

            if unit == "Million":
                money_supply_m0 += value * math.pow(10, 6)
            elif unit == "Billion":
                money_supply_m0 += value * math.pow(10, 9)
            elif unit == "Thousands":
                money_supply_m0 += value * math.pow(10, 3)

            print('money_supply_m0 : ' + str(money_supply_m0))

    # Money Supply M0 for EUR
    def test_get_money_supply_m0_for_eur_finland(self):
        print("test_get_money_supply_m0_for_eur_finland")

        money_supply_m0 = 0

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://tradingeconomics.com/finland/money-supply-m0"

        rt = RequestsTor()

        html_with_tor = rt.get(url, headers=headers)

        # Parse the content of html_doc
        soup = BeautifulSoup(html_with_tor.content, 'html.parser')

        element = soup.find('div', id="ctl00_ContentPlaceHolder1_ctl00_ctl00_Panel1")

        if element is not None:
            value = float(element.find('table', {'class': 'table table-hover'})
                          .find_all('tr', {'class': 'datatable-row-alternating'})[0]
                          .find_all('td')[1]
                          .text)

            unit = element\
                .find('table', {'class': 'table table-hover'})\
                .find_all('tr', {'class': 'datatable-row-alternating'})[0]\
                .find_all('td')[3]\
                .text\
                .split(' ')[1]

            if unit == "Million":
                money_supply_m0 += value * math.pow(10, 6)
            elif unit == "Billion":
                money_supply_m0 += value * math.pow(10, 9)
            elif unit == "Thousands":
                money_supply_m0 += value * math.pow(10, 3)

            print('money_supply_m0 : ' + str(money_supply_m0))

    def test_get_money_supply_m0_for_eur_greece(self):
        print("test_get_money_supply_m0_for_eur_greece")

        money_supply_m0 = 0

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://tradingeconomics.com/greece/money-supply-m0"

        rt = RequestsTor()

        html_with_tor = rt.get(url, headers=headers)

        # Parse the content of html_doc
        soup = BeautifulSoup(html_with_tor.content, 'html.parser')

        element = soup.find('div', id="ctl00_ContentPlaceHolder1_ctl00_ctl00_Panel1")

        if element is not None:
            value = float(element.find('table', {'class': 'table table-hover'})
                          .find_all('tr', {'class': 'datatable-row'})[1]
                          .find_all('td')[1]
                          .text)

            unit = element\
                .find('table', {'class': 'table table-hover'})\
                .find_all('tr', {'class': 'datatable-row'})[1]\
                .find_all('td')[3]\
                .text\
                .split(' ')[1]

            if unit == "Million":
                money_supply_m0 += value * math.pow(10, 6)
            elif unit == "Billion":
                money_supply_m0 += value * math.pow(10, 9)
            elif unit == "Thousands":
                money_supply_m0 += value * math.pow(10, 3)

            print('money_supply_m0 : ' + str(money_supply_m0))

    def test_get_money_supply_m0_for_eur_latvia(self):
        print("test_get_money_supply_m0_for_eur_latvia")

        money_supply_m0 = 0

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://tradingeconomics.com/latvia/money-supply-m0"

        rt = RequestsTor()

        html_with_tor = rt.get(url, headers=headers)

        # Parse the content of html_doc
        soup = BeautifulSoup(html_with_tor.content, 'html.parser')

        element = soup.find('div', id="ctl00_ContentPlaceHolder1_ctl00_ctl00_Panel1")

        if element is not None:
            value = float(element.find('table', {'class': 'table table-hover'})
                          .find_all('tr', {'class': 'datatable-row-alternating'})[0]
                          .find_all('td')[1]
                          .text)

            unit = element\
                .find('table', {'class': 'table table-hover'})\
                .find_all('tr', {'class': 'datatable-row-alternating'})[0]\
                .find_all('td')[3]\
                .text\
                .split(' ')[1]

            if unit == "Million":
                money_supply_m0 += value * math.pow(10, 6)
            elif unit == "Billion":
                money_supply_m0 += value * math.pow(10, 9)
            elif unit == "Thousands":
                money_supply_m0 += value * math.pow(10, 3)

            print('money_supply_m0 : ' + str(money_supply_m0))

    def test_get_money_supply_m0_for_eur_lithuania(self):
        print("test_get_money_supply_m0_for_eur_lithuania")

        money_supply_m0 = 0

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://tradingeconomics.com/lithuania/money-supply-m0"

        rt = RequestsTor()

        html_with_tor = rt.get(url, headers=headers)

        # Parse the content of html_doc
        soup = BeautifulSoup(html_with_tor.content, 'html.parser')

        element = soup.find('div', id="ctl00_ContentPlaceHolder1_ctl00_ctl00_Panel1")

        if element is not None:
            value = float(element.find('table', {'class': 'table table-hover'})
                          .find_all('tr', {'class': 'datatable-row-alternating'})[1]
                          .find_all('td')[1]
                          .text)

            unit = element\
                .find('table', {'class': 'table table-hover'})\
                .find_all('tr', {'class': 'datatable-row-alternating'})[1]\
                .find_all('td')[3]\
                .text\
                .split(' ')[1]

            if unit == "Million":
                money_supply_m0 += value * math.pow(10, 6)
            elif unit == "Billion":
                money_supply_m0 += value * math.pow(10, 9)
            elif unit == "Thousands":
                money_supply_m0 += value * math.pow(10, 3)

            print('money_supply_m0 : ' + str(money_supply_m0))

    def test_get_money_supply_m0_for_eur_luxembourg(self):
        print("test_get_money_supply_m0_for_eur_luxembourg")

        money_supply_m0 = 0

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://tradingeconomics.com/luxembourg/money-supply-m0"

        rt = RequestsTor()

        html_with_tor = rt.get(url, headers=headers)

        # Parse the content of html_doc
        soup = BeautifulSoup(html_with_tor.content, 'html.parser')

        element = soup.find('div', id="ctl00_ContentPlaceHolder1_ctl00_ctl00_Panel1")

        if element is not None:
            value = float(element.find('table', {'class': 'table table-hover'})
                          .find_all('tr', {'class': 'datatable-row-alternating'})[0]
                          .find_all('td')[1]
                          .text)

            unit = element\
                .find('table', {'class': 'table table-hover'})\
                .find_all('tr', {'class': 'datatable-row-alternating'})[0]\
                .find_all('td')[3]\
                .text\
                .split(' ')[1]

            if unit == "Million":
                money_supply_m0 += value * math.pow(10, 6)
            elif unit == "Billion":
                money_supply_m0 += value * math.pow(10, 9)
            elif unit == "Thousands":
                money_supply_m0 += value * math.pow(10, 3)

            print('money_supply_m0 : ' + str(money_supply_m0))

    def test_get_money_supply_m0_for_eur_malta(self):
        print("test_get_money_supply_m0_for_eur_malta")

        money_supply_m0 = 0

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://tradingeconomics.com/malta/money-supply-m0"

        rt = RequestsTor()

        html_with_tor = rt.get(url, headers=headers)

        # Parse the content of html_doc
        soup = BeautifulSoup(html_with_tor.content, 'html.parser')

        element = soup.find('div', id="ctl00_ContentPlaceHolder1_ctl00_ctl00_Panel1")

        if element is not None:
            value = float(element.find('table', {'class': 'table table-hover'})
                          .find_all('tr', {'class': 'datatable-row-alternating'})[0]
                          .find_all('td')[1]
                          .text)

            unit = element\
                .find('table', {'class': 'table table-hover'})\
                .find_all('tr', {'class': 'datatable-row-alternating'})[0]\
                .find_all('td')[3]\
                .text\
                .split(' ')[1]

            if unit == "Million":
                money_supply_m0 += value * math.pow(10, 6)
            elif unit == "Billion":
                money_supply_m0 += value * math.pow(10, 9)
            elif unit == "Thousands":
                money_supply_m0 += value * math.pow(10, 3)

            print('money_supply_m0 : ' + str(money_supply_m0))

    def test_get_money_supply_m0_for_eur_netherlands(self):
        print("test_get_money_supply_m0_for_eur_netherlands")

        money_supply_m0 = 0

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://tradingeconomics.com/netherlands/money-supply-m0"

        rt = RequestsTor()

        html_with_tor = rt.get(url, headers=headers)

        # Parse the content of html_doc
        soup = BeautifulSoup(html_with_tor.content, 'html.parser')

        element = soup.find('div', id="ctl00_ContentPlaceHolder1_ctl00_ctl00_Panel1")

        if element is not None:
            value = float(element.find('table', {'class': 'table table-hover'})
                          .find_all('tr', {'class': 'datatable-row-alternating'})[0]
                          .find_all('td')[1]
                          .text)

            unit = element\
                .find('table', {'class': 'table table-hover'})\
                .find_all('tr', {'class': 'datatable-row-alternating'})[0]\
                .find_all('td')[3]\
                .text\
                .split(' ')[1]

            if unit == "Million":
                money_supply_m0 += value * math.pow(10, 6)
            elif unit == "Billion":
                money_supply_m0 += value * math.pow(10, 9)
            elif unit == "Thousands":
                money_supply_m0 += value * math.pow(10, 3)

            print('money_supply_m0 : ' + str(money_supply_m0))

    def test_get_money_supply_m0_for_eur_portugal(self):
        print("test_get_money_supply_m0_for_eur_portugal")

        money_supply_m0 = 0

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://tradingeconomics.com/portugal/money-supply-m0"

        rt = RequestsTor()

        html_with_tor = rt.get(url, headers=headers)

        # Parse the content of html_doc
        soup = BeautifulSoup(html_with_tor.content, 'html.parser')

        element = soup.find('div', id="ctl00_ContentPlaceHolder1_ctl00_ctl00_Panel1")

        if element is not None:
            value = float(element.find('table', {'class': 'table table-hover'})
                          .find_all('tr', {'class': 'datatable-row'})[0]
                          .find_all('td')[1]
                          .text)

            unit = element\
                .find('table', {'class': 'table table-hover'})\
                .find_all('tr', {'class': 'datatable-row'})[0]\
                .find_all('td')[3]\
                .text\
                .split(' ')[1]

            if unit == "Million":
                money_supply_m0 += value * math.pow(10, 6)
            elif unit == "Billion":
                money_supply_m0 += value * math.pow(10, 9)
            elif unit == "Thousands":
                money_supply_m0 += value * math.pow(10, 3)

            print('money_supply_m0 : ' + str(money_supply_m0))

    def test_get_money_supply_m0_for_eur_slovakia(self):
        print("test_get_money_supply_m0_for_eur_slovakia")

        money_supply_m0 = 0

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://tradingeconomics.com/slovakia/money-supply-m0"

        rt = RequestsTor()

        html_with_tor = rt.get(url, headers=headers)

        # Parse the content of html_doc
        soup = BeautifulSoup(html_with_tor.content, 'html.parser')

        element = soup.find('div', id="ctl00_ContentPlaceHolder1_ctl00_ctl00_Panel1")

        if element is not None:
            value = float(element.find('table', {'class': 'table table-hover'})
                          .find_all('tr', {'class': 'datatable-row-alternating'})[0]
                          .find_all('td')[1]
                          .text)

            unit = element\
                .find('table', {'class': 'table table-hover'})\
                .find_all('tr', {'class': 'datatable-row-alternating'})[0]\
                .find_all('td')[3]\
                .text\
                .split(' ')[1]

            if unit == "Million":
                money_supply_m0 += value * math.pow(10, 6)
            elif unit == "Billion":
                money_supply_m0 += value * math.pow(10, 9)
            elif unit == "Thousands":
                money_supply_m0 += value * math.pow(10, 3)

            print('money_supply_m0 : ' + str(money_supply_m0))

    def test_get_money_supply_m0_for_eur_slovenia(self):
        print("test_get_money_supply_m0_for_eur_slovenia")

        money_supply_m0 = 0

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://tradingeconomics.com/slovenia/money-supply-m0"

        rt = RequestsTor()

        html_with_tor = rt.get(url, headers=headers)

        # Parse the content of html_doc
        soup = BeautifulSoup(html_with_tor.content, 'html.parser')

        element = soup.find('div', id="ctl00_ContentPlaceHolder1_ctl00_ctl00_Panel1")

        if element is not None:
            value = float(element.find('table', {'class': 'table table-hover'})
                          .find_all('tr', {'class': 'datatable-row-alternating'})[0]
                          .find_all('td')[1]
                          .text)

            unit = element\
                .find('table', {'class': 'table table-hover'})\
                .find_all('tr', {'class': 'datatable-row-alternating'})[0]\
                .find_all('td')[3]\
                .text\
                .split(' ')[1]

            if unit == "Million":
                money_supply_m0 += value * math.pow(10, 6)
            elif unit == "Billion":
                money_supply_m0 += value * math.pow(10, 9)
            elif unit == "Thousands":
                money_supply_m0 += value * math.pow(10, 3)

            print('money_supply_m0 : ' + str(money_supply_m0))

    def test_get_money_supply_m0_for_eur_belgium(self):
        print("test_get_money_supply_m0_for_eur_belgium")

        money_supply_m0 = 0

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://tradingeconomics.com/belgium/money-supply-m0"

        rt = RequestsTor()

        html_with_tor = rt.get(url, headers=headers)

        # Parse the content of html_doc
        soup = BeautifulSoup(html_with_tor.content, 'html.parser')

        element = soup.find('div', id="ctl00_ContentPlaceHolder1_ctl00_ctl00_Panel1")

        if element is not None:
            value = float(element.find('table', {'class': 'table table-hover'})
                          .find_all('tr', {'class': 'datatable-row'})[1]
                          .find_all('td')[1]
                          .text)

            unit = element\
                .find('table', {'class': 'table table-hover'})\
                .find_all('tr', {'class': 'datatable-row'})[1]\
                .find_all('td')[3]\
                .text\
                .split(' ')[1]

            if unit == "Million":
                money_supply_m0 += value * math.pow(10, 6)
            elif unit == "Billion":
                money_supply_m0 += value * math.pow(10, 9)
            elif unit == "Thousands":
                money_supply_m0 += value * math.pow(10, 3)

            print('money_supply_m0 : ' + str(money_supply_m0))
# Money Supply M0


# Money Supply M1
class UnitTestDataMinerTradingeconomicsIndicatorsMoneySupplyM1WithDarkWeb(unittest.TestCase):
    # Money Supply M1 for USD
    def test_get_money_supply_m1_for_usd_united_states(self):
        print("test_get_money_supply_m1_for_usd_united_states")

        money_supply_m1 = 0

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://tradingeconomics.com/united-states/money-supply-m1"

        rt = RequestsTor()

        html_with_tor = rt.get(url, headers=headers)

        soup = BeautifulSoup(html_with_tor.content, 'html.parser')

        element = soup.find('div', id="ctl00_ContentPlaceHolder1_ctl00_ctl00_Panel1")

        if element is not None:
            value = float(element.find('table', {'class': 'table table-hover'})
                          .find_all('tr', {'class': 'datatable-row-alternating'})[0]
                          .find_all('td')[1]
                          .text)

            unit = element\
                .find('table', {'class': 'table table-hover'})\
                .find_all('tr', {'class': 'datatable-row-alternating'})[0]\
                .find_all('td')[3]\
                .text\
                .split(' ')[1]

            if unit == "Million":
                money_supply_m1 += value * math.pow(10, 6)
            elif unit == "Billion":
                money_supply_m1 += value * math.pow(10, 9)
            elif unit == "Thousands":
                money_supply_m1 += value * math.pow(10, 3)

            print('money_supply_m1 : ' + str(money_supply_m1))

    def test_get_money_supply_m1_for_usd_belize(self):
        print("test_get_money_supply_m1_for_usd_belize")

        money_supply_m1 = 0

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://tradingeconomics.com/belize/money-supply-m1"

        rt = RequestsTor()

        html_with_tor = rt.get(url, headers=headers)

        soup = BeautifulSoup(html_with_tor.content, 'html.parser')

        element = soup.find('div', id="ctl00_ContentPlaceHolder1_ctl00_ctl00_Panel1")

        if element is not None:
            value = float(element.find('table', {'class': 'table table-hover'})
                          .find_all('tr', {'class': 'datatable-row-alternating'})[0]
                          .find_all('td')[1]
                          .text)

            unit = element\
                .find('table', {'class': 'table table-hover'})\
                .find_all('tr', {'class': 'datatable-row-alternating'})[0]\
                .find_all('td')[3]\
                .text\
                .split(' ')[1]

            if unit == "Million":
                money_supply_m1 += value * math.pow(10, 6)
            elif unit == "Billion":
                money_supply_m1 += value * math.pow(10, 9)
            elif unit == "Thousands":
                money_supply_m1 += value * math.pow(10, 3)

            print('money_supply_m1 : ' + str(money_supply_m1))

    def test_get_money_supply_m1_for_usd_ecuador(self):
        print("test_get_money_supply_m1_for_usd_ecuador")

        money_supply_m1 = 0

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://tradingeconomics.com/ecuador/money-supply-m1"

        rt = RequestsTor()

        html_with_tor = rt.get(url, headers=headers)

        soup = BeautifulSoup(html_with_tor.content, 'html.parser')

        element = soup.find('div', id="ctl00_ContentPlaceHolder1_ctl00_ctl00_Panel1")

        if element is not None:
            value = float(element.find('table', {'class': 'table table-hover'})
                          .find_all('tr', {'class': 'datatable-row'})[1]
                          .find_all('td')[1]
                          .text)

            unit = element\
                .find('table', {'class': 'table table-hover'})\
                .find_all('tr', {'class': 'datatable-row'})[1]\
                .find_all('td')[3]\
                .text\
                .split(' ')[1]

            if unit == "Million":
                money_supply_m1 += value * math.pow(10, 6)
            elif unit == "Billion":
                money_supply_m1 += value * math.pow(10, 9)
            elif unit == "Thousands":
                money_supply_m1 += value * math.pow(10, 3)

            print('money_supply_m1 : ' + str(money_supply_m1))

    def test_get_money_supply_m1_for_usd_el_salvador(self):
        print("test_get_money_supply_m1_for_usd_el_salvador")

        money_supply_m1 = 0

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://tradingeconomics.com/el-salvador/money-supply-m1"

        rt = RequestsTor()

        html_with_tor = rt.get(url, headers=headers)

        soup = BeautifulSoup(html_with_tor.content, 'html.parser')

        element = soup.find('div', id="ctl00_ContentPlaceHolder1_ctl00_ctl00_Panel1")

        if element is not None:
            value = float(element.find('table', {'class': 'table table-hover'})
                          .find_all('tr', {'class': 'datatable-row'})[1]
                          .find_all('td')[1]
                          .text)

            unit = element\
                .find('table', {'class': 'table table-hover'})\
                .find_all('tr', {'class': 'datatable-row'})[1]\
                .find_all('td')[3]\
                .text\
                .split(' ')[1]

            if unit == "Million":
                money_supply_m1 += value * math.pow(10, 6)
            elif unit == "Billion":
                money_supply_m1 += value * math.pow(10, 9)
            elif unit == "Thousands":
                money_supply_m1 += value * math.pow(10, 3)

            print('money_supply_m1 : ' + str(money_supply_m1))

    def test_get_money_supply_m1_for_usd_zimbabwe(self):
        print("test_get_money_supply_m1_for_usd_zimbabwe")

        money_supply_m1 = 0

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://tradingeconomics.com/zimbabwe/money-supply-m1"

        rt = RequestsTor()

        html_with_tor = rt.get(url, headers=headers)

        soup = BeautifulSoup(html_with_tor.content, 'html.parser')

        element = soup.find('div', id="ctl00_ContentPlaceHolder1_ctl00_ctl00_Panel1")

        if element is not None:
            value = float(element.find('table', {'class': 'table table-hover'})
                          .find_all('tr', {'class': 'datatable-row-alternating'})[0]
                          .find_all('td')[1]
                          .text)

            unit = element\
                .find('table', {'class': 'table table-hover'})\
                .find_all('tr', {'class': 'datatable-row-alternating'})[0]\
                .find_all('td')[3]\
                .text\
                .split(' ')[1]

            if unit == "Million":
                money_supply_m1 += value * math.pow(10, 6)
            elif unit == "Billion":
                money_supply_m1 += value * math.pow(10, 9)
            elif unit == "Thousands":
                money_supply_m1 += value * math.pow(10, 3)

            print('money_supply_m1 : ' + str(money_supply_m1))

    # Money Supply M1 for EUR
    def test_get_money_supply_m1_for_eur_euro_area(self):
        print("test_get_money_supply_m1_for_eur_euro_area")

        money_supply_m1 = 0

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://tradingeconomics.com/euro-area/money-supply-m1"

        rt = RequestsTor()

        html_with_tor = rt.get(url, headers=headers)

        soup = BeautifulSoup(html_with_tor.content, 'html.parser')

        element = soup.find('div', id="ctl00_ContentPlaceHolder1_ctl00_ctl00_Panel1")

        if element is not None:
            value = float(element.find('table', {'class': 'table table-hover'})
                          .find_all('tr', {'class': 'datatable-row-alternating'})[0]
                          .find_all('td')[1]
                          .text)

            unit = element\
                .find('table', {'class': 'table table-hover'})\
                .find_all('tr', {'class': 'datatable-row-alternating'})[0]\
                .find_all('td')[3]\
                .text\
                .split(' ')[1]

            if unit == "Million":
                money_supply_m1 += value * math.pow(10, 6)
            elif unit == "Billion":
                money_supply_m1 += value * math.pow(10, 9)
            elif unit == "Thousands":
                money_supply_m1 += value * math.pow(10, 3)

            print('money_supply_m1 : ' + str(money_supply_m1))
# Money Supply M1


# Money Supply M2
class UnitTestDataMinerTradingeconomicsIndicatorsMoneySupplyM2WithDarkWeb(unittest.TestCase):
    # Money Supply M2 for USD
    def test_get_money_supply_m2_for_usd_united_states(self):
        print("test_get_money_supply_m2_for_usd_united_states")

        money_supply_m2 = 0

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://tradingeconomics.com/united-states/money-supply-m2"

        rt = RequestsTor()

        html_with_tor = rt.get(url, headers=headers)

        soup = BeautifulSoup(html_with_tor.content, 'html.parser')

        element = soup.find('div', id="ctl00_ContentPlaceHolder1_ctl00_ctl00_Panel1")

        if element is not None:
            value = float(element.find('table', {'class': 'table table-hover'})
                          .find_all('tr', {'class': 'datatable-row-alternating'})[1]
                          .find_all('td')[1]
                          .text)

            unit = element\
                .find('table', {'class': 'table table-hover'})\
                .find_all('tr', {'class': 'datatable-row-alternating'})[1]\
                .find_all('td')[3]\
                .text\
                .split(' ')[1]

            if unit == "Million":
                money_supply_m2 += value * math.pow(10, 6)
            elif unit == "Billion":
                money_supply_m2 += value * math.pow(10, 9)
            elif unit == "Thousands":
                money_supply_m2 += value * math.pow(10, 3)

            print('money_supply_m2 : ' + str(money_supply_m2))

    def test_get_money_supply_m2_for_usd_zimbabwe(self):
        print("test_get_money_supply_m2_for_usd_zimbabwe")

        money_supply_m2 = 0

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://tradingeconomics.com/zimbabwe/money-supply-m2"

        rt = RequestsTor()

        html_with_tor = rt.get(url, headers=headers)

        soup = BeautifulSoup(html_with_tor.content, 'html.parser')

        element = soup.find('div', id="ctl00_ContentPlaceHolder1_ctl00_ctl00_Panel1")

        if element is not None:
            value = float(element.find('table', {'class': 'table table-hover'})
                          .find_all('tr', {'class': 'datatable-row'})[1]
                          .find_all('td')[1]
                          .text)

            unit = element\
                .find('table', {'class': 'table table-hover'})\
                .find_all('tr', {'class': 'datatable-row'})[1]\
                .find_all('td')[3]\
                .text\
                .split(' ')[1]

            if unit == "Million":
                money_supply_m2 += value * math.pow(10, 6)
            elif unit == "Billion":
                money_supply_m2 += value * math.pow(10, 9)
            elif unit == "Thousands":
                money_supply_m2 += value * math.pow(10, 3)

            print('money_supply_m2 : ' + str(money_supply_m2))

    def test_get_money_supply_m2_for_usd_el_salvador(self):
        print("test_get_money_supply_m2_for_usd_el_salvador")

        money_supply_m2 = 0

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://tradingeconomics.com/el-salvador/money-supply-m2"

        rt = RequestsTor()

        html_with_tor = rt.get(url, headers=headers)

        soup = BeautifulSoup(html_with_tor.content, 'html.parser')

        element = soup.find('div', id="ctl00_ContentPlaceHolder1_ctl00_ctl00_Panel1")

        if element is not None:
            value = float(element.find('table', {'class': 'table table-hover'})
                          .find_all('tr', {'class': 'datatable-row-alternating'})[1]
                          .find_all('td')[1]
                          .text)

            unit = element\
                .find('table', {'class': 'table table-hover'})\
                .find_all('tr', {'class': 'datatable-row-alternating'})[1]\
                .find_all('td')[3]\
                .text\
                .split(' ')[1]

            if unit == "Million":
                money_supply_m2 += value * math.pow(10, 6)
            elif unit == "Billion":
                money_supply_m2 += value * math.pow(10, 9)
            elif unit == "Thousands":
                money_supply_m2 += value * math.pow(10, 3)

            print('money_supply_m2 : ' + str(money_supply_m2))

    def test_get_money_supply_m2_for_usd_ecuador(self):
        print("test_get_money_supply_m2_for_usd_ecuador")

        money_supply_m2 = 0

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://tradingeconomics.com/ecuador/money-supply-m2"

        rt = RequestsTor()

        html_with_tor = rt.get(url, headers=headers)

        soup = BeautifulSoup(html_with_tor.content, 'html.parser')

        element = soup.find('div', id="ctl00_ContentPlaceHolder1_ctl00_ctl00_Panel1")

        if element is not None:
            value = float(element.find('table', {'class': 'table table-hover'})
                          .find_all('tr', {'class': 'datatable-row-alternating'})[1]
                          .find_all('td')[1]
                          .text)

            unit = element\
                .find('table', {'class': 'table table-hover'})\
                .find_all('tr', {'class': 'datatable-row-alternating'})[1]\
                .find_all('td')[3]\
                .text\
                .split(' ')[1]

            if unit == "Million":
                money_supply_m2 += value * math.pow(10, 6)
            elif unit == "Billion":
                money_supply_m2 += value * math.pow(10, 9)
            elif unit == "Thousands":
                money_supply_m2 += value * math.pow(10, 3)

            print('money_supply_m2 : ' + str(money_supply_m2))

    def test_get_money_supply_m2_for_usd_belize(self):
        print("test_get_money_supply_m2_for_usd_belize")

        money_supply_m2 = 0

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://tradingeconomics.com/belize/money-supply-m2"

        rt = RequestsTor()

        html_with_tor = rt.get(url, headers=headers)

        soup = BeautifulSoup(html_with_tor.content, 'html.parser')

        element = soup.find('div', id="ctl00_ContentPlaceHolder1_ctl00_ctl00_Panel1")

        if element is not None:
            value = float(element.find('table', {'class': 'table table-hover'})
                          .find_all('tr', {'class': 'datatable-row-alternating'})[1]
                          .find_all('td')[1]
                          .text)

            unit = element\
                .find('table', {'class': 'table table-hover'})\
                .find_all('tr', {'class': 'datatable-row-alternating'})[1]\
                .find_all('td')[3]\
                .text\
                .split(' ')[1]

            if unit == "Million":
                money_supply_m2 += value * math.pow(10, 6)
            elif unit == "Billion":
                money_supply_m2 += value * math.pow(10, 9)
            elif unit == "Thousands":
                money_supply_m2 += value * math.pow(10, 3)

            print('money_supply_m2 : ' + str(money_supply_m2))

    # Money Supply M2 for EUR
    def test_get_money_supply_m2_for_eur_euro_area(self):
        print("test_get_money_supply_m2_for_eur_euro_area")

        money_supply_m2 = 0

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://tradingeconomics.com/euro-area/money-supply-m2"

        rt = RequestsTor()

        html_with_tor = rt.get(url, headers=headers)

        soup = BeautifulSoup(html_with_tor.content, 'html.parser')

        element = soup.find('div', id="ctl00_ContentPlaceHolder1_ctl00_ctl00_Panel1")

        if element is not None:
            value = float(element.find('table', {'class': 'table table-hover'})
                          .find_all('tr', {'class': 'datatable-row'})[1]
                          .find_all('td')[1]
                          .text)

            unit = element\
                .find('table', {'class': 'table table-hover'})\
                .find_all('tr', {'class': 'datatable-row'})[1]\
                .find_all('td')[3]\
                .text\
                .split(' ')[1]

            if unit == "Million":
                money_supply_m2 += value * math.pow(10, 6)
            elif unit == "Billion":
                money_supply_m2 += value * math.pow(10, 9)
            elif unit == "Thousands":
                money_supply_m2 += value * math.pow(10, 3)

            print('money_supply_m2 : ' + str(money_supply_m2))
# Money Supply M2


# Money Supply M3
class UnitTestDataMinerTradingeconomicsIndicatorsMoneySupplyM3WithDarkWeb(unittest.TestCase):
    # Money Supply M3 for USD
    def test_get_money_supply_m3_for_usd_zimbabwe(self):
        print("test_get_money_supply_m3_for_usd_zimbabwe")

        money_supply_m3 = 0

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://tradingeconomics.com/zimbabwe/money-supply-m3"

        rt = RequestsTor()

        html_with_tor = rt.get(url, headers=headers)

        soup = BeautifulSoup(html_with_tor.content, 'html.parser')

        element = soup.find('div', id="ctl00_ContentPlaceHolder1_ctl00_ctl00_Panel1")

        if element is not None:
            value = float(element.find('table', {'class': 'table table-hover'})
                          .find_all('tr', {'class': 'datatable-row-alternating'})[1]
                          .find_all('td')[1]
                          .text)

            unit = element\
                .find('table', {'class': 'table table-hover'})\
                .find_all('tr', {'class': 'datatable-row-alternating'})[1]\
                .find_all('td')[3]\
                .text\
                .split(' ')[1]

            if unit == "Million":
                money_supply_m3 += value * math.pow(10, 6)
            elif unit == "Billion":
                money_supply_m3 += value * math.pow(10, 9)
            elif unit == "Thousands":
                money_supply_m3 += value * math.pow(10, 3)

            print('money_supply_m3 : ' + str(money_supply_m3))

    def test_get_money_supply_m3_for_usd_el_salvador(self):
        print("test_get_money_supply_m3_for_usd_el_salvador")

        money_supply_m3 = 0

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://tradingeconomics.com/el-salvador/money-supply-m3"

        rt = RequestsTor()

        html_with_tor = rt.get(url, headers=headers)

        soup = BeautifulSoup(html_with_tor.content, 'html.parser')

        element = soup.find('div', id="ctl00_ContentPlaceHolder1_ctl00_ctl00_Panel1")

        if element is not None:
            value = float(element.find('table', {'class': 'table table-hover'})
                          .find_all('tr', {'class': 'datatable-row'})[2]
                          .find_all('td')[1]
                          .text)

            unit = element\
                .find('table', {'class': 'table table-hover'})\
                .find_all('tr', {'class': 'datatable-row'})[2]\
                .find_all('td')[3]\
                .text\
                .split(' ')[1]

            if unit == "Million":
                money_supply_m3 += value * math.pow(10, 6)
            elif unit == "Billion":
                money_supply_m3 += value * math.pow(10, 9)
            elif unit == "Thousands":
                money_supply_m3 += value * math.pow(10, 3)

            print('money_supply_m3 : ' + str(money_supply_m3))

    # Money Supply M3 for EUR
    def test_get_money_supply_m3_for_eur_euro_area(self):
        print("test_get_money_supply_m3_for_eur_euro_area")

        money_supply_m3 = 0

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://tradingeconomics.com/euro-area/money-supply-m2"

        rt = RequestsTor()

        html_with_tor = rt.get(url, headers=headers)

        soup = BeautifulSoup(html_with_tor.content, 'html.parser')

        element = soup.find('div', id="ctl00_ContentPlaceHolder1_ctl00_ctl00_Panel1")

        if element is not None:
            value = float(element.find('table', {'class': 'table table-hover'})
                          .find_all('tr', {'class': 'datatable-row-alternating'})[1]
                          .find_all('td')[1]
                          .text)

            unit = element \
                .find('table', {'class': 'table table-hover'}) \
                .find_all('tr', {'class': 'datatable-row-alternating'})[1] \
                .find_all('td')[3] \
                .text \
                .split(' ')[1]

            if unit == "Million":
                money_supply_m3 += value * math.pow(10, 6)
            elif unit == "Billion":
                money_supply_m3 += value * math.pow(10, 9)
            elif unit == "Thousands":
                money_supply_m3 += value * math.pow(10, 3)

            print('money_supply_m3 : ' + str(money_supply_m3))
# Money Supply M3
# Money


# Population
class UnitTestDataMinerTradingeconomicsIndicatorPopulationWithDarkWeb(unittest.TestCase):
    # EU population
    def test_get_population_for_eu_population(self):
        print("test_get_population_for_eu_population")

        eu_population = 0

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://tradingeconomics.com/euro-area/population"

        rt = RequestsTor()

        html_with_tor = rt.get(url, headers=headers)

        soup = BeautifulSoup(html_with_tor.content, 'html.parser')

        element = soup.find('div', id="ctl00_ContentPlaceHolder1_ctl00_ctl00_Panel1")

        if element is not None:
            value = float(element.find_all('tr', {'class': 'datatable-row'})[4]
                          .find_all('td')[1]
                          .text)

            eu_population = value * math.pow(10, 6)

            print('eu_population : ' + str(eu_population))
# Population
# Indicators


if __name__ == '__main__':
    unittest.main()
