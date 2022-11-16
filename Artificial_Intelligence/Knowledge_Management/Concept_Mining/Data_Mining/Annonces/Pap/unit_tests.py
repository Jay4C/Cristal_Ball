import unittest
import requests
from bs4 import BeautifulSoup
import xlsxwriter


class UnitTestsWebScraperPap(unittest.TestCase):
    def test_extract_one_phone_number_from_one_ad(self):
        try:
            url_ad = "https://www.pap.fr/annonces/bureaux-paris-16e-r427800161"

            # Request the content of a page from the url
            html = requests.get(url_ad)

            # Parse the content of html
            soup = BeautifulSoup(html.content, 'html.parser')

            try:
                if soup.find("div", {"class": "sidebar"}) is not None:
                    if soup.find("div", {"class": "sidebar"}).find("p", {"class": "h3 txt-indigo"}) is not None:
                        phone_number = soup\
                            .find("div", {"class": "sidebar"})\
                            .find("p", {"class": "h3 txt-indigo"})\
                            .text\
                            .replace("\n", "")\
                            .replace(".", "")

                        print("phone number : " + phone_number)

                    else:
                        print("no p class h3 txt-indigo")
                else:
                    print("no div class sidebar")
            except Exception as e:
                print("Exception div classsidebar : " + str(e))
        except Exception as e:
            print("Exception url_phone_book : " + str(e))


if __name__ == '__main__':
    unittest.main()
