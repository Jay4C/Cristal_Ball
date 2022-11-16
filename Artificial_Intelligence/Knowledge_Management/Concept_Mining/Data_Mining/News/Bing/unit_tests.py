import time
import unittest
import requests
import xlsxwriter
from bs4 import BeautifulSoup
import json


class UnitTestsDataMiningBing(unittest.TestCase):
    def test_extract_phone_number_from_one_company(self):
        print('test_extract_phone_number_from_one_company')

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        time.sleep(3)

        search = "Valois Energie Senlis".lower().replace(" ", "%20")

        url = "https://www.bing.com/search?q=" + search

        html = requests.get(url, headers=headers)

        soup = BeautifulSoup(html.content, 'html.parser')

        if soup.select_one("#IconItem_5") is not None:
            telephone = soup.select_one("#IconItem_5").find("a").text
            print("telephone : " + telephone)
        else:
            print("no telephone")

    def test_extract_phone_number_from_biogas_sites(self):
        print('test_extract_phone_number_from_one_company')

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        workbook = xlsxwriter.Workbook("telephones_entreprises_biogas.xlsx")

        worksheet = workbook.add_worksheet('data')

        worksheet.write(0, 0, 'nom_du_projet')
        worksheet.write(0, 1, 'telephone')

        row = 1

        telephones_entreprises = []

        f = open('les-sites-dinjection-de-biomethane-en-france.json', "r")
        data = json.loads(f.read())
        for feature in data['features']:
            search = feature['properties']['nom_du_projet'].lower().replace(" ", "%20")

            url = "https://www.bing.com/search?q=" + search

            html = requests.get(url, headers=headers)

            soup = BeautifulSoup(html.content, 'html.parser')

            if soup.select_one("#IconItem_5") is not None:
                telephone = soup.select_one("#IconItem_5").find("a").text

                print("telephone : " + telephone)

                x = {
                    'nom_du_projet': feature['properties']['nom_du_projet'],
                    'telephone': telephone,
                }

                telephones_entreprises.append(x)
            else:
                print("no telephone")

                x = {
                    'nom_du_projet': feature['properties']['nom_du_projet'],
                    'telephone': '',
                }

                telephones_entreprises.append(x)

        f.close()

        for telephone in telephones_entreprises:
            worksheet.write(row, 0, telephone.get('nom_du_projet'))
            worksheet.write(row, 1, telephone.get('telephone'))

            row += 1

        workbook.close()


if __name__ == '__main__':
    unittest.main()
