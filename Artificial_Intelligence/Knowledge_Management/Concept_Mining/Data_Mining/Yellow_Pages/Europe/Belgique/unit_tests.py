import time
from bs4 import BeautifulSoup
import requests
import pymysql.cursors
import unittest


class UnitTestsDataMinerYellowPagesBelgique(unittest.TestCase):
    def test_extract_one_email(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = ""

        # Request the content of a page from the url
        html = requests.get(url, headers=headers)

        print(html.content)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.content, 'html.parser')

        if soup.find('a', {'class': 'detail-btn'}) is not None:
            email = "info@" + soup.find('a', {'class': 'detail-btn-email elogin-email-detail'}).get('href').split("@")[1]
            print("email : " + email)
        else:
            print('no email business')


if __name__ == '__main__':
    unittest.main()
