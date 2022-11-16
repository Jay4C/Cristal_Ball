import time
import pymysql
from bs4 import BeautifulSoup
import requests
import unittest
from requests_tor import RequestsTor


class UnitTestsDataMinerTorMetrics(unittest.TestCase):
    def test_get_ip_information_with_clear_web(self):
        print("test_get_ip_information_with_clear_web")

        url = "https://metrics.torproject.org/rs.html#search/89.163.249.192"

        payload = {}

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        # Request the content of a page from the url
        html = requests.request("GET", url, headers=headers, data=payload)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.content, 'html.parser')

        print(html.content)

    def test_get_ip_information_with_dark_web(self):
        print("test_get_ip_information_with_dark_web")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://metrics.torproject.org/rs.html#search/89.163.249.192"

        rt = RequestsTor()

        html_with_tor = rt.get(url, headers=headers)

        # Parse the content of html_doc
        soup = BeautifulSoup(html_with_tor.content, 'html.parser')

        print(html_with_tor.content)


if __name__ == '__main__':
    unittest.main()
