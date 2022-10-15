import unittest
import requests
from requests_tor import RequestsTor
from bs4 import BeautifulSoup
import time
from datetime import datetime


class UnitTestsKMDMFinanceFxconvert(unittest.TestCase):
    # ok
    def test_extract_currency_converter(self):
        print('test_extract_currency_converter')

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        currency_1 = 'aed'

        currency_2 = 'usd'

        url = 'https://fxconvert.net/converter/' + currency_1 + '-' + currency_2 + '/1'

        rt = RequestsTor()

        html = rt.get(url, headers=headers).content

        time.sleep(3)

        soup = BeautifulSoup(html, 'html.parser')

        if soup.find("p", {'class': 'convert-result convert-result-from'}) is not None:
            rate = soup.find_all("p", {'class': 'convert-result convert-result-from'})[0].find_all('span')[0].text
            print("rate : " + str(rate))
        else:
            print("no rate")

    # ok
    def test_extract_currency_list(self):
        print('test_extract_currency_list')

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        currency_list = []

        url = 'https://fxconvert.net/calculator'

        rt = RequestsTor()

        html = rt.get(url, headers=headers).content

        time.sleep(3)

        soup = BeautifulSoup(html, 'html.parser')

        if soup.find("tbody") is not None:
            all_tr = soup.find_all("tbody")[0].find_all('tr')

            for tr in all_tr:
                iso_code = tr.find_all('td')[1].text.lower()
                currency_list.append(iso_code)
        else:
            print("no iso_code")

        print(currency_list)

    # ok
    def test_extract_currency_converter_for_all_currency(self):
        print('test_extract_currency_converter_for_all_currency')

        current_datetime = datetime.now()

        print(current_datetime)

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        currency_list = [
            'aed', 'afn', 'all', 'amd', 'ang', 'aoa', 'ars', 'aud', 'awg', 'azn', 'bam', 'bbd', 'bdt', 'bgn', 'bhd',
            'bif', 'bmd', 'bnd', 'bob', 'brl', 'bsd', 'btc', 'btn', 'bwp', 'byn', 'bzd', 'cad', 'cdf', 'chf', 'clf',
            'clp', 'cny', 'cop', 'crc', 'cuc', 'cup', 'cve', 'czk', 'djf', 'dkk', 'dop', 'dzd', 'egp', 'ern', 'etb',
            'eur', 'fjd', 'fkp', 'gbp', 'gel', 'ggp', 'ghs', 'gip', 'gmd', 'gnf', 'gtq', 'gyd', 'hkd', 'hnl', 'hrk',
            'htg', 'huf', 'idr', 'ils', 'imp', 'inr', 'iqd', 'irr', 'isk', 'jep', 'jmd', 'jod', 'jpy', 'kes', 'kgs',
            'khr', 'kmf', 'kpw', 'krw', 'kwd', 'kyd', 'kzt', 'lak', 'lbp', 'lkr', 'lrd', 'lsl', 'lyd', 'mad', 'mdl',
            'mga', 'mkd', 'mmk', 'mnt', 'mop', 'mro', 'mur', 'mvr', 'mwk', 'mxn', 'myr', 'mzn', 'nad', 'ngn', 'nio',
            'nok', 'npr', 'nzd', 'omr', 'pab', 'pen', 'pgk', 'php', 'pkr', 'pln', 'pyg', 'qar', 'ron', 'rsd', 'rub',
            'rwf', 'sar', 'sbd', 'scr', 'sdg', 'sek', 'sgd', 'shp', 'sll', 'sos', 'srd', 'ssp', 'std', 'svc', 'syp',
            'szl', 'thb', 'tjs', 'tmt', 'tnd', 'top', 'try', 'ttd', 'twd', 'tzs', 'uah', 'ugx', 'usd', 'uyu', 'uzs',
            'vnd', 'vuv', 'wst', 'xaf', 'xcd', 'xdr', 'xof', 'xpf', 'yer', 'zar', 'zmw', 'zwl'
        ]

        for currency_1 in currency_list:
            for currency_2 in currency_list:
                try:
                    url = 'https://fxconvert.net/converter/' + currency_1 + '-' + currency_2 + '/1'

                    # rt = RequestsTor()
                    rt = requests

                    html = rt.get(url, headers=headers).content

                    soup = BeautifulSoup(html, 'html.parser')

                    if soup.find("p", {'class': 'convert-result convert-result-from'}) is not None:
                        rate = soup.find_all("p", {'class': 'convert-result convert-result-from'})[0].find_all('span')[
                            0].text
                        print("rate between " + str(currency_1) + " and " + str(currency_2) + " : " + str(rate))
                    else:
                        print("no rate between " + str(currency_1) + " and " + str(currency_2))
                except Exception as e:
                    print('error : ' + str(e))

        current_datetime = datetime.now()

        print(current_datetime)


if __name__ == '__main__':
    unittest.main()
