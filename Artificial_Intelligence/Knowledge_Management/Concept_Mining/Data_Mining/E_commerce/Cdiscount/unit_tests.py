import unittest
import time
import requests
from bs4 import BeautifulSoup


class UnitTestsDataMiningCdiscount(unittest.TestCase):
    #
    def test_request_one_page(self):
        print("test_request_one_page")

        url = ""

        # Request the content of a page from the url
        html = requests.get(url)

        time.sleep(3)

        print(html.content)


if __name__ == '__main__':
    unittest.main()
