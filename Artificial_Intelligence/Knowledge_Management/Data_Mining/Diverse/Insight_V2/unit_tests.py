import unittest
from requests_tor import RequestsTor
from bs4 import BeautifulSoup
import time
from lxml import etree


url = ""


class UnitTestsDataMiningInsightV2WithDarkWeb(unittest.TestCase):
    # ok
    def test_extract_the_content(self):
        print('test_extract_the_content')

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        rt = RequestsTor()

        html = rt.get(url, headers=headers, verify=False).content

        time.sleep(3)

        print(html)

    # ok
    def test_extract_the_title_insight(self):
        print('test_extract_the_title_insight')

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        rt = RequestsTor()

        html = rt.get(url, headers=headers, verify=False).content

        time.sleep(3)

        soup = BeautifulSoup(html, 'html.parser')

        dom = etree.HTML(str(soup))

        try:
            title = dom.xpath('/html/body/div[2]/div/div/div[2]/div/div/div/div/div/div[1]/h1')[0].text
            print("title : " + str(title))
        except Exception as e:
            print('error title : ' + str(e))


if __name__ == '__main__':
    unittest.main()
