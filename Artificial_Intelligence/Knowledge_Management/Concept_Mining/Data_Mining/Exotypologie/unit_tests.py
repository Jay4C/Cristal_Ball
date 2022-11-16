from bs4 import BeautifulSoup
import json
import unittest
from requests_tor import RequestsTor


class Unit_Tests_Data_Miner_Exotypologie(unittest.TestCase):
    def test_get_urls_with_dark_web(self):
        print("test_get_urls_with_dark_web")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://exotypologie.wordpress.com/"

        rt = RequestsTor()

        html_with_tor = rt.get(url, headers=headers)

        soup = BeautifulSoup(html_with_tor.content, 'html.parser')

        i = 1

        if soup.find('a') is not None:
            all_a = soup.find_all('a')

            for a in all_a:
                x = str({
                    'title': str(i) + "_exotypologie",
                    'url': a.get('href')
                }) + ","

                print(x)

                i += 1


if __name__ == '__main__':
    unittest.main()
