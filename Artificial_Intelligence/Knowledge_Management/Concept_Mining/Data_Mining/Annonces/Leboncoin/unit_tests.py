import time
import unittest
from bs4 import BeautifulSoup
import requests
import json
import xlsxwriter
import pymysql.cursors


class UnitTestsDataMiningLeboncoin(unittest.TestCase):
    def test_extract_the_title_of_the_ad(self):
        print('test_extract_the_title_of_the_ad')

        cookie = "__Secure-InstanceId=daaa5092-79b4-4631-a45c-e63de8a11fa2; sq=ca=12_s; utag_main=v_id:0178a323963a0020ce991c3b38cc03083001907b0086e$_sn:3$_ss:0$_st:1617778355415$_pn:3%3Bexp-session$ses_id:1617776472449%3Bexp-session; uuid=d9c7dadf-0224-4592-9de9-9541a88d99fe; datadome=Eh6c13gd71GrXbQ.DG2_zPdXsg74FLe~W_DYrsNkvimnV0E2InIccpe88l6QNI0lIy9YYYN_8uda8IljmGAI.lhNdpgpMD7joJbDcDx73J"

        try:
            url_ad = 'https://www.leboncoin.fr/ventes_immobilieres/1656695264.htm?ac=558505705'

            headers = {
                'authority': 'www.leboncoin.fr',
                'method': 'GET',
                'path': url_ad.replace('https://www.leboncoin.fr', ''),
                'scheme': 'https',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'fr,fr-FR;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
                'cache-control': 'max-age=0',
                'cookie': cookie,
                'dnt': '1',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'none',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.54'
            }

            response = requests.get(url_ad, headers=headers)

            soup = BeautifulSoup(response.text, 'html.parser')

            try:
                if soup.find("h1", {"data-qa-id": "adview_title"}) is not None:
                    title = soup.find("h1", {"data-qa-id": "adview_title"}).text
                    print("title : " + title)
                else:
                    print("no title")
            except Exception as e:
                print("error title : " + str(e))
        except Exception as e:
            print("error request url_ad : " + str(e))

    def test_extract_the_price_of_the_ad(self):
        print('test_extract_the_price_of_the_ad')

        try:
            url_ad = 'https://www.leboncoin.fr/ventes_immobilieres/1930964997.htm?ac=558505705'

            headers = {
                'authority': 'www.leboncoin.fr',
                'method': 'GET',
                'path': url_ad.replace('https://www.leboncoin.fr', ''),
                'scheme': 'https',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'fr,fr-FR;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
                'cache-control': 'max-age=0',
                'cookie': '__Secure-InstanceId=cc56ea7d-a44d-47cb-a2f3-1305700071a7; atidvisitor=%7B%22name%22%3A%22atidvisitor%22%2C%22val%22%3A%7B%22vrn%22%3A%22-562498-%22%2C%22an%22%3A%22NaN%22%2C%22ac%22%3A%22%22%7D%2C%22options%22%3A%7B%22path%22%3A%22%2F%22%2C%22session%22%3A15724800%2C%22end%22%3A15724800%7D%7D; ry_ry-l3b0nco_realytics=eyJpZCI6InJ5XzdGQ0FEMzgyLTVFOEQtNDlGOC1CNzY5LTI3OTg1MzUyNkZCRSIsImNpZCI6bnVsbCwiZXhwIjoxNjQ3NjAyNDYwODgzLCJjcyI6bnVsbH0%3D; ry_ry-l3b0nco_so_realytics=eyJpZCI6InJ5XzdGQ0FEMzgyLTVFOEQtNDlGOC1CNzY5LTI3OTg1MzUyNkZCRSIsImNpZCI6bnVsbCwib3JpZ2luIjp0cnVlLCJyZWYiOm51bGwsImNvbnQiOm51bGwsIm5zIjpmYWxzZX0%3D; uuid=8d770939-aa5f-43a3-a355-33ded9f62220; user_search_config={"sort_by":"price","sort_order":"desc"}; datadome=O.sju8RJyX62RZhkFcj9BD~yGZT4omiTF5kP~bo9fL~FRF8YIEBDMLF1QbZ.j_sARHkflTAwSibodP~JqQSgjTXUL1YJdEm2F_YTBxqGud; utag_main=v_id:017845113865001f64e88cefdc9103082001907a0086e$_sn:2$_ss:0$_st:1616082152219$_pn:8%3Bexp-session$ses_id:1616080197381%3Bexp-session',
                'dnt': '1',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'none',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.54'
            }

            # Request the content of a page from the url
            response = requests.get(url_ad, headers=headers)

            # Parse the content of html_doc
            soup = BeautifulSoup(response.text, 'html.parser')

            try:
                if soup.find("div", {"data-qa-id": "adview_price"}) is not None:
                    price = soup.find("div", {"data-qa-id": "adview_price"}).text
                    print("price : " + price)
                else:
                    print("no price")
            except Exception as e:
                print("error price : " + str(e))
        except Exception as e:
            print("error request url_ad : " + str(e))

    def test_extract_the_location_of_the_ad_option_1(self):
        print('test_extract_the_location_of_the_ad')

        cookie = '__Secure-InstanceId=daaa5092-79b4-4631-a45c-e63de8a11fa2; sq=ca=12_s; user_search_config={"sort_by":"price","sort_order":"asc"}; datadome=Rrm4~owhCRuvPzj3zwzHODCHx7d1P8N2iRfNWMJK0EkZH8qA38I~GDkWBoreQLeT3XHq~creltDd3ntIjsCfD_oc42HT7ZofcKOq8V-l2W; utag_main=v_id:0178a323963a0020ce991c3b38cc03083001907b0086e$_sn:2$_ss:0$_st:1617731138730$_pn:2%3Bexp-session$ses_id:1617729279184%3Bexp-session'

        try:
            url_ad = 'https://www.leboncoin.fr/ventes_immobilieres/1957461390.htm?ac=558505705'

            headers = {
                'authority': 'www.leboncoin.fr',
                'method': 'GET',
                'path': url_ad.replace('https://www.leboncoin.fr', ''),
                'scheme': 'https',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'fr,fr-FR;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
                'cache-control': 'max-age=0',
                'cookie': cookie,
                'dnt': '1',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'none',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.54'
            }

            response = requests.get(url_ad, headers=headers)

            soup = BeautifulSoup(response.text, 'html.parser')

            try:
                if soup.find("div", {"class": "css-iel3r1"}) is not None:
                    location_city = soup.find("div", {"class": "css-iel3r1"}).text.split("·")[-1].split(" ")[0].replace(" ", "").replace("\n", "").replace(" ", "")

                    location_postal_code = soup.find("div", {"class": "css-iel3r1"}).text.split("·")[-1].split(" ")[1].replace(" ", "").replace("\n", "").replace(" ", "")

                    print("location_city : " + location_city + " / location_postal_code : " + location_postal_code)
                else:
                    print("no price")
            except Exception as e:
                print("error price : " + str(e))
        except Exception as e:
            print("error request url_ad : " + str(e))

    def test_extract_the_location_of_the_ad_option_2(self):
        print('test_extract_the_location_of_the_ad_option_2')

        cookie = '__Secure-InstanceId=daaa5092-79b4-4631-a45c-e63de8a11fa2; sq=ca=12_s; uuid=bd4c49c8-8756-411d-a629-88aee164e908; utag_main=v_id:0178a323963a0020ce991c3b38cc03083001907b0086e$_sn:4$_ss:0$_st:1617783300505$_pn:6%3Bexp-session$ses_id:1617780938808%3Bexp-session; datadome=8gUViXvs_x2lPLVv~C8eiLNGfErdvQSpc.xQs.rPou~ustC7mL~ePO7EBFiX6lRFYAGnTZOWcQrvNp7kGBNC3UU-Y0VA.Q5xN3HfXGMUIg'

        url_ad = 'https://www.leboncoin.fr/ventes_immobilieres/1958428502.htm?ac=558505705'

        try:
            headers = {
                'authority': 'www.leboncoin.fr',
                'method': 'GET',
                'path': url_ad.replace('https://www.leboncoin.fr', ''),
                'scheme': 'https',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'fr,fr-FR;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
                'cache-control': 'max-age=0',
                'cookie': cookie,
                'dnt': '1',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'none',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.54'
            }

            response = requests.get(url_ad, headers=headers)

            soup = BeautifulSoup(response.text, 'html.parser')

            try:
                if soup.find("li", {"data-qa-id": "breadcrumb-item-4"}) is not None:
                    location = soup.find("li", {"data-qa-id": "breadcrumb-item-4"}).text\
                        .replace(" ", "")\
                        .replace("\t", "")\
                        .replace("\n", "")\
                        .replace("\r", "")

                    code_postal = location[len(location)-5:]

                    print("location_code_postal : " + code_postal)
                else:
                    print("no location_city")
            except Exception as e:
                print("error location_city : " + str(e))
        except Exception as e:
            print("error request url_ad : " + str(e))

    def test_extract_the_surface_of_the_ad(self):
        print('test_extract_the_surface_of_the_ad')

        try:
            url_ad = 'https://www.leboncoin.fr/ventes_immobilieres/1930964997.htm?ac=558505705'

            headers = {
                'authority': 'www.leboncoin.fr',
                'method': 'GET',
                'path': url_ad.replace('https://www.leboncoin.fr', ''),
                'scheme': 'https',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'fr,fr-FR;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
                'cache-control': 'max-age=0',
                'cookie': '__Secure-InstanceId=cc56ea7d-a44d-47cb-a2f3-1305700071a7; atidvisitor=%7B%22name%22%3A%22atidvisitor%22%2C%22val%22%3A%7B%22vrn%22%3A%22-562498-%22%2C%22an%22%3A%22NaN%22%2C%22ac%22%3A%22%22%7D%2C%22options%22%3A%7B%22path%22%3A%22%2F%22%2C%22session%22%3A15724800%2C%22end%22%3A15724800%7D%7D; ry_ry-l3b0nco_realytics=eyJpZCI6InJ5XzdGQ0FEMzgyLTVFOEQtNDlGOC1CNzY5LTI3OTg1MzUyNkZCRSIsImNpZCI6bnVsbCwiZXhwIjoxNjQ3NjAyNDYwODgzLCJjcyI6bnVsbH0%3D; ry_ry-l3b0nco_so_realytics=eyJpZCI6InJ5XzdGQ0FEMzgyLTVFOEQtNDlGOC1CNzY5LTI3OTg1MzUyNkZCRSIsImNpZCI6bnVsbCwib3JpZ2luIjp0cnVlLCJyZWYiOm51bGwsImNvbnQiOm51bGwsIm5zIjpmYWxzZX0%3D; uuid=8d770939-aa5f-43a3-a355-33ded9f62220; user_search_config={"sort_by":"price","sort_order":"desc"}; datadome=O.sju8RJyX62RZhkFcj9BD~yGZT4omiTF5kP~bo9fL~FRF8YIEBDMLF1QbZ.j_sARHkflTAwSibodP~JqQSgjTXUL1YJdEm2F_YTBxqGud; utag_main=v_id:017845113865001f64e88cefdc9103082001907a0086e$_sn:2$_ss:0$_st:1616082152219$_pn:8%3Bexp-session$ses_id:1616080197381%3Bexp-session',
                'dnt': '1',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'none',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.54'
            }

            # Request the content of a page from the url
            response = requests.get(url_ad, headers=headers)

            # Parse the content of html_doc
            soup = BeautifulSoup(response.text, 'html.parser')

            try:
                if soup.find("div", {"class": "css-iel3r1"}) is not None:
                    surface = soup.find("div", {"class": "css-iel3r1"}).text.split("·")[0]
                    print("surface : " + surface)
                else:
                    print("no price")
            except Exception as e:
                print("error price : " + str(e))
        except Exception as e:
            print("error request url_ad : " + str(e))

    def test_extract_the_description_of_the_ad(self):
        print('test_extract_the_description_of_the_ad')

        url_ad = 'https://www.leboncoin.fr/ventes_immobilieres/1656695264.htm?ac=558505705'

        cookie = '__Secure-InstanceId=daaa5092-79b4-4631-a45c-e63de8a11fa2; sq=ca=12_s; utag_main=v_id:0178a323963a0020ce991c3b38cc03083001907b0086e$_sn:3$_ss:0$_st:1617778355415$_pn:3%3Bexp-session$ses_id:1617776472449%3Bexp-session; uuid=d9c7dadf-0224-4592-9de9-9541a88d99fe; datadome=Eh6c13gd71GrXbQ.DG2_zPdXsg74FLe~W_DYrsNkvimnV0E2InIccpe88l6QNI0lIy9YYYN_8uda8IljmGAI.lhNdpgpMD7joJbDcDx73J'

        try:
            headers = {
                'authority': 'www.leboncoin.fr',
                'method': 'GET',
                'path': url_ad.replace('https://www.leboncoin.fr', ''),
                'scheme': 'https',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'fr,fr-FR;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
                'cache-control': 'max-age=0',
                'cookie': cookie,
                'dnt': '1',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'none',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.54'
            }

            response = requests.get(url_ad, headers=headers)

            soup = BeautifulSoup(response.text, 'html.parser')

            try:
                if soup.find("div", {"data-qa-id": "adview_description_container"}) is not None:
                    description = soup.find("div", {"data-qa-id": "adview_description_container"})\
                        .text.replace("\n", "").replace("\t", "").replace("\r", "")
                    print("description : " + description)
                else:
                    print("no description")
            except Exception as e:
                print("error description : " + str(e))
        except Exception as e:
            print("error request url_ad : " + str(e))

    def test_extract_all_ads_from_one_page(self):
        print('test_extract_all_ads_from_one_page')

        cookie = '__Secure-InstanceId=c6628435-f8d2-4856-aae7-a92294df87dd; ry_ry-l3b0nco_realytics=eyJpZCI6InJ5XzYwMjQwMjI1LTc2NjItNDlFOS1CREE4LTdFRkY4MDY0RTIzNiIsImNpZCI6bnVsbCwiZXhwIjoxNjU1NjYyNTg4MDM1LCJjcyI6bnVsbH0%3D; ry_ry-l3b0nco_so_realytics=eyJpZCI6InJ5XzYwMjQwMjI1LTc2NjItNDlFOS1CREE4LTdFRkY4MDY0RTIzNiIsImNpZCI6bnVsbCwib3JpZ2luIjp0cnVlLCJyZWYiOm51bGwsImNvbnQiOm51bGwsIm5zIjpmYWxzZX0%3D; didomi_token=eyJ1c2VyX2lkIjoiMTdhMjU3Y2YtNjVkNS02MjNlLThkOGItOTNiOGFlNGQ4OTBkIiwiY3JlYXRlZCI6IjIwMjEtMDYtMTlUMTg6MTc6NTQuNzc1WiIsInVwZGF0ZWQiOiIyMDIxLTA2LTE5VDE4OjE3OjU0Ljc3NVoiLCJ2ZW5kb3JzIjp7ImRpc2FibGVkIjpbImFtYXpvbiIsInNhbGVzZm9yY2UiLCJnb29nbGUiLCJjOm5leHQtcGVyZm9ybWFuY2UiLCJjOmNvbGxlY3RpdmUtaGhTWXRSVm4iLCJjOnJvY2t5b3UiLCJjOnB1Ym9jZWFuLWI2QkpNdHNlIiwiYzpydGFyZ2V0LUdlZk1WeWlDIiwiYzpzY2hpYnN0ZWQtTVFQWGFxeWgiLCJjOmdyZWVuaG91c2UtUUtiR0JrczQiLCJjOnJlYWx6ZWl0Zy1iNktDa3h5ViIsImM6dmlkZW8tbWVkaWEtZ3JvdXAiLCJjOnN3aXRjaC1jb25jZXB0cyIsImM6bHVjaWRob2xkLXlmdGJXVGY3IiwiYzpsZW1vbWVkaWEtemJZaHAyUWMiLCJjOnlvcm1lZGlhcy1xbkJXaFF5UyIsImM6c2Fub21hIiwiYzpyYWR2ZXJ0aXMtU0pwYTI1SDgiLCJjOnF3ZXJ0aXplLXpkbmdFMmh4IiwiYzp2ZG9waWEiLCJjOnJldmxpZnRlci1jUnBNbnA1eCIsImM6cmVzZWFyY2gtbm93IiwiYzp3aGVuZXZlcm0tOFZZaHdiMlAiLCJjOmFkbW90aW9uIiwiYzp3b29iaSIsImM6c2hvcHN0eWxlLWZXSksyTGlQIiwiYzp0aGlyZHByZXNlLVNzS3dtSFZLIiwiYzpiMmJtZWRpYS1wUVRGZ3lXayIsImM6cHVyY2giLCJjOmxpZmVzdHJlZXQtbWVkaWEiLCJjOnN5bmMtbjc0WFFwcmciLCJjOmludG93b3dpbi1xYXp0NXRHaSIsImM6ZGlkb21pIiwiYzpyYWRpdW1vbmUiLCJjOmFkb3Rtb2IiLCJjOmFiLXRhc3R5IiwiYzpncmFwZXNob3QiLCJjOmFkbW9iIiwiYzphZGFnaW8iLCJjOmxiY2ZyYW5jZSJdfSwicHVycG9zZXMiOnsiZGlzYWJsZWQiOlsicGVyc29ubmFsaXNhdGlvbmNvbnRlbnUiLCJwZXJzb25uYWxpc2F0aW9ubWFya2V0aW5nIiwicHJpeCIsIm1lc3VyZWF1ZGllbmNlIiwiZXhwZXJpZW5jZXV0aWxpc2F0ZXVyIl19LCJ2ZW5kb3JzX2xpIjp7ImRpc2FibGVkIjpbImdvb2dsZSJdfSwidmVyc2lvbiI6MiwiYWMiOiJBQUFBLkFBQUEifQ==; euconsent-v2=CPIDhA8PIDhA8AHABBENBcCgAAAAAAAAAAAAAAAAAABigYIABwAEgANAAeABSADAAMgAigBSAFQALAAYgA1gB8AH8AQgBDACYAFoALkAXgBfgDCAMQAZgA2gB4AD1AH8AggBCwCNAI4ASYAlQBMwCfAKAAUgAqABWgCygFuAXEAygDLgGaAZ0A0wDVAGwANoAcEA4gDkAHMAOyAd4B4QDzAPSAfIB9AD8AH_AQUBBoCEgIUARAAjABHICSgJMASuAloCXAEwAJvATwBPgCggFFAKQAUsAqIBV4CugK-AWaAtAC0gFzgLsAu4BeQC-AF-AMCAYQAxUBnAGdANAAacA1oBtADeAHCgOaA5wB1QDsgHbAO-AeIA9YB7YD9AP2Af8BAgCBwEGAISAQuAh8BEoCLAEcQI6AjsBHoCQQEhgJFASiAlSBLwEvwJhAmIBM0CbAJtATuAn8BQoCiAFFAKMgUcBSACmYFNgU4Ap8BUQCpIFWgVeArMBW0CxALFgWOBZMCywLMAWcAtEBasC1wLYAW4AuCBcYFyQLmAugBdcC7QLugXmBesC9wL7AYEAwqBhoGHwMUAxUBjUDHgMgAZEAyUBlcDMAMxAZpAzgDOYGeAZ9A0EDQgGigNPga0BrcDXQNeAbAA2QBtQDbQG4ANygboBusDfQN-gcIBw0DiQOKAccA5IBykDmAOZAc8A6eB1oHYAO4Ad2A72B4QHhgPQgemB6kD1gPYAe4A94B8AD4gHzgPpAfZA-8D8BgL4AA4ACQAHgAUgAwADIAIoAUgBUACwAGIANQAfwBCAEMAJgAUwAuABegDCAMQAZgA2wB_AIKARoBHgCTAEqAJmAT4BQACkAFQAK0AWUAtwC4AGPAMoAywBnQDTANUAbQA4IBxAHIAOYAdkA7wDwgHmAekA-gD8AH_AQkBCgCIAESAIwARwAkoBKwCWgEwAJvATwBPgCggFFAKQAUsAqIBVwCtwFdAV8AsQBZgC5wF2AXcAvIBfAC_AGEAMVAZwBnQDQQGmAacA1oBtADeAHCgOaA5wB1QDsgHbAO-AeIA9YB7QD5AH7AQIAgcBCQCFwEPgIlARYAjiBHQEdgI9ASCAkMBIoCTgEogJUgS8BL8CYQJiATNAmwCbQE4gJ3AT-AoUBRACigFGQKOApABTMCmwKcgU8BT4CogFSQKtAq8BWYCtgFiQLHAsmBZYFmALOAWiAtWBa4FsQLbAtwBcAC44FzAXQAuuBdoF3QLyAvSBe4F8AL7AYEAwoBhoDD4GKAYqAxoBjwDIAGRAMlAZWAzEBmkDOAM5gZ4Bn0DQQNCAaKA0-BrQGtgNdAbAA2SBtQG2ANwgboBusDfQN-gcIBwwDiQHHAOSAcpA5gDmQHPAOngdaB2ADuAHdgO9geEB4YD0IHpgepA9YD2AHuAPeAfAA-IB84D6QH2QPvA_AgDnAADAAcACQAFgANAAeABQAC0AGQAaAA6ACIAEgAKgAWAAuABiAD-AIIAhwBMAE0AKYAVQArgBcgC8AL8AYQBiADMAGgANoAbwA7gB6gD-AQIAi4BGgEeAJEASYAlYBPgFAAKQAVAAqgBWwCxALKAW4BcgC-AGEAMSAZQBlwDNAM6AaYBqgDYAG1AN8A4ABxADkgHMAc4A7IB3gHhAPMA9AB7QD5APwAf4BBYCEgIUARAAikBGAEZAI4ASUAlIBKwCXAEwgJuAnABPACfAFBAKGAUWApACkgFLAKeAVEAq4BWQCtwFdAV8AsQBZoC0ALSAXOAuwC7gF5AL4AX4AwABhADFAGZgM4AzoBoIDTANOAasA1oBtADeAHCAObAdQB1QDrgHZAO2Ad8A8QB6ID1APWAe2A_ID-AIAAQIAgcBCcCFwIYAQ-AiGBEoETAIsgRwBHcCPQI-gSCBIoCTgEogJUASuAlqBLwEvwJhAmIBMwCaYE2ATaAnEBO4Cf4FCAUKAoiBRgFIQKSApOBTIFOQKeAp8BUQCpIFWgVeArMBW0CvgK_gWIBYsCxwLJgWWBZgCzgFogLTAWrAtcC3AFvALggXGBckC5wLogXWBdwC8gF6QL2Av2BgIGBgMKgYYBh4DEoGKAYqAxoBjwDIAGRAMlAZOAysBloDMQGaQM3Az-BoIGhQNEA0UBo8DSQNLAaeA1OBqoGrQNaA1sBrsDXwNhAbJA2sDbAG3ANwgboBusDeQN6gb6Bv0DgAOBgcIBwwDiQHGAOOAclA5gDmYHPAc-A6OB0oHTwOpA6qB1gHYAO1AdwA7uB3oHfAPBgeGB4gDx4HkgeVA84D0YHpgepA9YD2IHuAe9A-AD4oHzgfSA-wB-A.YAAAAAAAAAAA; include_in_experiment=false; sq=ca=12_s; atauthority=%7B%22name%22%3A%22atauthority%22%2C%22val%22%3A%7B%22authority_name%22%3A%22cnil%22%2C%22visitor_mode%22%3A%22exempt%22%7D%2C%22options%22%3A%7B%22end%22%3A%222022-07-19T18%3A25%3A03.461Z%22%2C%22path%22%3A%22%2F%22%7D%7D; utag_main=v_id:017a257cf4470005528ef933cbd303083001907b0086e$_sn:1$_ss:0$_pn:5%3Bexp-session$_st:1624128903498$ses_id:1624126583879%3Bexp-session; datadome=AtQBbWVpPBsS6M0v_T.zwQNPvKhQ2uhr8x.euyDm-huLUivYdSNaTqE7C~2IFTgMYWIe_dz2-xMtuLmCXOmLSbCQdbNMO-U1XBIKihwtNA'

        try:
            urls_ads_from_one_page = 'https://www.leboncoin.fr/recherche?category=9&locations=r_12&sort=price&order=asc&real_estate_type=3&immo_sell_type=old&price=51000-200000&square=1000-max&page=1'

            headers = {
                'authority': 'www.leboncoin.fr',
                'method': 'GET',
                'path': urls_ads_from_one_page.replace('https://www.leboncoin.fr', ''),
                'scheme': 'https',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'fr,fr-FR;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
                'cache-control': 'max-age=0',
                'cookie': cookie,
                'dnt': '1',
                'if-none-match': '595e8-PxHUoOtVSx5GtnlwiOTxISsUrak',
                'sec-ch-ua': '" Not;A Brand";v="99", "Microsoft Edge";v="91", "Chromium";v="91"',
                'sec-ch-ua-mobile': '?0',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'none',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36 Edg/91.0.864.48'
            }

            # Request the content of a page from the url
            response = requests.get(urls_ads_from_one_page, headers=headers)

            print(response.text)

            # Parse the content of html_doc
            soup = BeautifulSoup(response.text, 'html.parser')

            try:
                if soup.find("a", {"data-qa-id": "aditem_container"}) is not None:
                    all_a = soup.find_all("a", {"data-qa-id": "aditem_container"})

                    for i in range(0, len(all_a)):
                        print("ad " + str(i) + " : https://www.leboncoin.fr" + all_a[i].get("href"))
                else:
                    print("no a data-qa-id")
            except Exception as e:
                print("error price : " + str(e))
        except Exception as e:
            print("error request url_ad : " + str(e))

    def test_extract_all_ads_from_all_pages(self):
        print('test_extract_all_ads_from_all_pages')

        cookie = '__Secure-InstanceId=daaa5092-79b4-4631-a45c-e63de8a11fa2; sq=ca=12_s; utag_main=v_id:0178a323963a0020ce991c3b38cc03083001907b0086e$_sn:2$_ss:0$_st:1617731551464$_pn:5%3Bexp-session$ses_id:1617729279184%3Bexp-session; uuid=7f20b9f3-c56b-4a49-a70e-0064a786da3f; datadome=LxVc2bIrcpZvnHs8mB2xDb1ExQiqXwQkBAI~O2I_51vKu.C2LQSDUI8qU8JcGmRnPAyuC6ZS5aYYc2U~h4hnOzYt8LgWFr.hieCMbrLxsD'

        i_1 = 0

        try:
            urls_ads_from_page_one = 'https://www.leboncoin.fr/recherche?category=9&locations=r_12&real_estate_type=3&square=500-max&page=1'

            headers_urls_ads_from_one_page = {
                'authority': 'www.leboncoin.fr',
                'method': 'GET',
                'path': urls_ads_from_page_one.replace('https://www.leboncoin.fr', ''),
                'scheme': 'https',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'fr,fr-FR;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
                'cache-control': 'max-age=0',
                'cookie': cookie,
                'dnt': '1',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'none',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.54'
            }

            # Request the content of a page from the url
            response = requests.get(urls_ads_from_page_one, headers=headers_urls_ads_from_one_page)

            # Parse the content of html_doc
            soup_urls_ads_from_one_page = BeautifulSoup(response.text, 'html.parser')

            number_of_pages = 0

            if soup_urls_ads_from_one_page.find("span", {"class": "_3Ce01 _137P- P4PEa _35DXM"}) is not None:
                number_of_pages_with_coma = int(soup_urls_ads_from_one_page.find("span", {"class": "_3Ce01 _137P- P4PEa _35DXM"})
                                                .text
                                                .replace(" ", "")
                                                .replace("results", "")
                                                ) / 35

                if int(str(number_of_pages_with_coma).split(".")[1][:1]) < 5:
                    number_of_pages += round(number_of_pages_with_coma) + 1
                    print('number_of_pages : ' + str(number_of_pages))
                elif int(str(number_of_pages_with_coma).split(".")[1][:1]) >= 5:
                    number_of_pages += round(number_of_pages_with_coma)
                    print('number_of_pages : ' + str(number_of_pages))
            else:
                print("error pages")

            try:
                for i_page in range(1, number_of_pages + 1):
                    urls_ads_from_one_page = urls_ads_from_page_one[:-1] + str(i_page)

                    print(urls_ads_from_one_page)

                    headers_urls_ads_from_one_page = {
                        'authority': 'www.leboncoin.fr',
                        'method': 'GET',
                        'scheme': 'https',
                        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                        'accept-encoding': 'gzip, deflate, br',
                        'accept-language': 'fr,fr-FR;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
                        'cache-control': 'max-age=0',
                        'cookie': cookie,
                        'dnt': '1',
                        'sec-fetch-dest': 'document',
                        'sec-fetch-mode': 'navigate',
                        'sec-fetch-site': 'none',
                        'sec-fetch-user': '?1',
                        'upgrade-insecure-requests': '1',
                        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.54'
                    }

                    time.sleep(3)

                    # Request the content of a page from the url
                    response = requests.get(urls_ads_from_one_page, headers=headers_urls_ads_from_one_page)

                    # Parse the content of html_doc
                    soup = BeautifulSoup(response.text, 'html.parser')

                    if soup.find("a", {"data-qa-id": "aditem_container"}) is not None:
                        all_a = soup.find_all("a", {"data-qa-id": "aditem_container"})

                        for a in range(0, len(all_a)):
                            print("ad " + str(i_1) + " : https://www.leboncoin.fr" + all_a[a].get("href"))

                            i_1 += 1
                    else:
                        print("no a data-qa-id aditem_container")
            except Exception as e:
                print("error for : " + str(e))
        except Exception as e:
            print("error request url_ad : " + str(e))

    def test_extract_all_ads_from_all_pages_with_postal_code(self):
        print('test_extract_all_ads_from_all_pages_with_postal_code')

        cookie = '__Secure-InstanceId=daaa5092-79b4-4631-a45c-e63de8a11fa2; sq=ca=12_s; utag_main=v_id:0178a323963a0020ce991c3b38cc03083001907b0086e$_sn:2$_ss:0$_st:1617731551464$_pn:5%3Bexp-session$ses_id:1617729279184%3Bexp-session; uuid=7f20b9f3-c56b-4a49-a70e-0064a786da3f; datadome=LxVc2bIrcpZvnHs8mB2xDb1ExQiqXwQkBAI~O2I_51vKu.C2LQSDUI8qU8JcGmRnPAyuC6ZS5aYYc2U~h4hnOzYt8LgWFr.hieCMbrLxsD'

        i_1 = 0

        try:
            urls_ads_from_page_one = 'https://www.leboncoin.fr/recherche?category=9&locations=r_12&real_estate_type=3&price=min-25000&page=1'

            headers_urls_ads_from_one_page = {
                'authority': 'www.leboncoin.fr',
                'method': 'GET',
                'path': urls_ads_from_page_one.replace('https://www.leboncoin.fr', ''),
                'scheme': 'https',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'fr,fr-FR;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
                'cache-control': 'max-age=0',
                'cookie': cookie,
                'dnt': '1',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'none',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.54'
            }

            # Request the content of a page from the url
            response = requests.get(urls_ads_from_page_one, headers=headers_urls_ads_from_one_page)

            # Parse the content of html_doc
            soup_urls_ads_from_one_page = BeautifulSoup(response.text, 'html.parser')

            number_of_pages = 0

            if soup_urls_ads_from_one_page.find("span", {"class": "_3Ce01 _137P- P4PEa _35DXM"}) is not None:
                number_of_pages_with_coma = int(soup_urls_ads_from_one_page.find("span", {"class": "_3Ce01 _137P- P4PEa _35DXM"})
                                                .text
                                                .replace(" ", "")
                                                .replace("results", "")
                                                ) / 35

                if int(str(number_of_pages_with_coma).split(".")[1][:1]) < 5:
                    number_of_pages += round(number_of_pages_with_coma) + 1
                    print('number_of_pages : ' + str(number_of_pages))
                elif int(str(number_of_pages_with_coma).split(".")[1][:1]) >= 5:
                    number_of_pages += round(number_of_pages_with_coma)
                    print('number_of_pages : ' + str(number_of_pages))
            else:
                print("error pages")

            try:
                for i_page in range(1, number_of_pages + 1):
                    urls_ads_from_one_page = urls_ads_from_page_one[:-1] + str(i_page)

                    print(urls_ads_from_one_page)

                    headers_urls_ads_from_one_page = {
                        'authority': 'www.leboncoin.fr',
                        'method': 'GET',
                        'scheme': 'https',
                        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                        'accept-encoding': 'gzip, deflate, br',
                        'accept-language': 'fr,fr-FR;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
                        'cache-control': 'max-age=0',
                        'cookie': cookie,
                        'dnt': '1',
                        'sec-fetch-dest': 'document',
                        'sec-fetch-mode': 'navigate',
                        'sec-fetch-site': 'none',
                        'sec-fetch-user': '?1',
                        'upgrade-insecure-requests': '1',
                        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.54'
                    }

                    time.sleep(3)

                    response = requests.get(urls_ads_from_one_page, headers=headers_urls_ads_from_one_page)

                    soup = BeautifulSoup(response.text, 'html.parser')

                    if soup.find("a", {"data-qa-id": "aditem_container"}) is not None:
                        all_a = soup.find_all("a", {"data-qa-id": "aditem_container"})

                        for a in all_a:
                            i_1 += 1

                            try:
                                url_ad = "https://www.leboncoin.fr" + a.get("href")

                                print(str(i_1) + " : " + url_ad)

                                headers_url_ad = {
                                    'authority': 'www.leboncoin.fr',
                                    'method': 'GET',
                                    'path': url_ad.replace('https://www.leboncoin.fr', ''),
                                    'scheme': 'https',
                                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                                    'accept-encoding': 'gzip, deflate, br',
                                    'accept-language': 'fr,fr-FR;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
                                    'cache-control': 'max-age=0',
                                    'cookie': cookie,
                                    'dnt': '1',
                                    'sec-fetch-dest': 'document',
                                    'sec-fetch-mode': 'navigate',
                                    'sec-fetch-site': 'none',
                                    'sec-fetch-user': '?1',
                                    'upgrade-insecure-requests': '1',
                                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.54'
                                }

                                time.sleep(3)

                                response_url_ad = requests.get(url_ad, headers=headers_url_ad)

                                soup_url_ad = BeautifulSoup(response_url_ad.text, 'html.parser')

                                try:
                                    if soup_url_ad.find("div", {"class": "css-iel3r1"}) is not None:
                                        location_postal_code = soup_url_ad.find("div", {"class": "css-iel3r1"}).text\
                                            .split("·")[-1].split(" ")[1].replace(" ", "").replace("\n", "").replace(" ", "")

                                        print(str(i_1) + " ; url_ad : " + url_ad + " ; location_postal_code : " + location_postal_code)
                                    else:
                                        print(str(i_1) + " : no location code postal")
                                except Exception as e:
                                    print(str(i_1) + " : error location code postal : " + str(e))
                            except Exception as e:
                                print(str(i_1) + " : error request url_ad : " + str(e))
                    else:
                        print("no a data-qa-id aditem_container")
            except Exception as e:
                print("error for : " + str(e))
        except Exception as e:
            print("error request url_ad : " + str(e))

    def test_extract_all_lands_with_at_least_10000_square_meter_from_all_pages(self):
        print('test_extract_all_ads_from_all_pages')

        cookie = '__Secure-InstanceId=63bc4677-82f8-4b9b-87cb-dde71e8166eb; ry_ry-l3b0nco_realytics=eyJpZCI6InJ5XzI0NEEyRDRFLTczQ0YtNEM1Ni05QzQzLUEyODM2RUVCMTgwOSIsImNpZCI6bnVsbCwiZXhwIjoxNjQ4ODI5MTE1OTU4LCJjcyI6bnVsbH0%3D; didomi_token=eyJ1c2VyX2lkIjoiMTc4OGUyZTctOGMzNy02ZjcyLTg5NzgtZWM2ODg5MjY0ODZhIiwiY3JlYXRlZCI6IjIwMjEtMDQtMDFUMTY6MDU6MTcuNDYyWiIsInVwZGF0ZWQiOiIyMDIxLTA0LTAxVDE2OjA1OjE3LjQ2MloiLCJ2ZW5kb3JzIjp7ImRpc2FibGVkIjpbImFtYXpvbiIsInNhbGVzZm9yY2UiLCJnb29nbGUiLCJjOm5leHQtcGVyZm9ybWFuY2UiLCJjOmNvbGxlY3RpdmUtaGhTWXRSVm4iLCJjOnJvY2t5b3UiLCJjOnB1Ym9jZWFuLWI2QkpNdHNlIiwiYzpydGFyZ2V0LUdlZk1WeWlDIiwiYzpzY2hpYnN0ZWQtTVFQWGFxeWgiLCJjOmdyZWVuaG91c2UtUUtiR0JrczQiLCJjOnJlYWx6ZWl0Zy1iNktDa3h5ViIsImM6dmlkZW8tbWVkaWEtZ3JvdXAiLCJjOnN3aXRjaC1jb25jZXB0cyIsImM6bHVjaWRob2xkLXlmdGJXVGY3IiwiYzpsZW1vbWVkaWEtemJZaHAyUWMiLCJjOnlvcm1lZGlhcy1xbkJXaFF5UyIsImM6c2Fub21hIiwiYzpyYWR2ZXJ0aXMtU0pwYTI1SDgiLCJjOnF3ZXJ0aXplLXpkbmdFMmh4IiwiYzp2ZG9waWEiLCJjOnJldmxpZnRlci1jUnBNbnA1eCIsImM6cmVzZWFyY2gtbm93IiwiYzp3aGVuZXZlcm0tOFZZaHdiMlAiLCJjOmFkbW90aW9uIiwiYzp3b29iaSIsImM6c2hvcHN0eWxlLWZXSksyTGlQIiwiYzp0aGlyZHByZXNlLVNzS3dtSFZLIiwiYzpiMmJtZWRpYS1wUVRGZ3lXayIsImM6cHVyY2giLCJjOmxpZmVzdHJlZXQtbWVkaWEiLCJjOnN5bmMtbjc0WFFwcmciLCJjOmludG93b3dpbi1xYXp0NXRHaSIsImM6ZGlkb21pIiwiYzpyYWRpdW1vbmUiLCJjOmFkb3Rtb2IiLCJjOmFiLXRhc3R5IiwiYzpncmFwZXNob3QiLCJjOmFkbW9iIiwiYzphZGFnaW8iLCJjOmxiY2ZyYW5jZSJdfSwicHVycG9zZXMiOnsiZGlzYWJsZWQiOlsicGVyc29ubmFsaXNhdGlvbmNvbnRlbnUiLCJwZXJzb25uYWxpc2F0aW9ubWFya2V0aW5nIiwicHJpeCIsIm1lc3VyZWF1ZGllbmNlIiwiZXhwZXJpZW5jZXV0aWxpc2F0ZXVyIl19LCJ2ZW5kb3JzX2xpIjp7ImVuYWJsZWQiOlsiZ29vZ2xlIl19LCJ2ZXJzaW9uIjoyLCJhYyI6IkFBQUEuREUyQXdBRUlBZm9CaFFEeEFIbUFTU0Frc0NKSUhFQU9yQWlEQkZLQ0tnRW00SnZBVGtBdHJCYmVDNHdGeVFMbGdZREF3aUJpYUFBQSJ9; euconsent-v2=CPD-1hnPD-1hnAHABBENBTCgAAAAAHLAAAAAAAAOdAJMNS-AATEscCSaNKoUQIQriQqAUAFFCMLRNYQEjgp2VwEeoIEACA1ARgRAgxBRiwCAAACAJCIgBADwQCIAiAQAAgBUgIQAESAALACwMAgAFANCgAigCECQgiMCo5TAgIkWignkDAAIAAAAAAAAAAAAAAAQAxQLgAA4ACQAGgAPAApABgAGQARQApACoAFgAMQAawA-AD-AIQAhgBMAC0AFyALwAvwBhAGIAMwAbQA8AB6gD-AQQAhQBFQCNAI4ASYAlQBMwCfAKAAUgAqABWgCygFuAXEAygDLgGaAZ0A0wDVAGwANoAcEA4gDkAHMAOyAd4B4QDzAPSAfIB9AD8AH_AQUBBoCEgIUARAAjABHICSgJMASuAloCXAEwAJvATwBPgCggFFAKQAUsAqIBV4CugK-AWaAtAC0gFzgLsAu4BeQC-AF-AMCAYQAxUBnAGdANAAacA1oBtADeAHCgOaA5wB1QDsgHbAO-AeIA9YB7YD9AP2Af8BAgCBwEGAISAQuAh8BEoCLAEcQI6AjsBHoCQQEhgJFASiAlSBLwEvwJhAmIBM0CbAJtATuAn8BQoCiAFFAKMgUcBSACmYFNgU4Ap8BUQCpIFWgVeArMBW0CxALFgWOBZMCywLMAWcAtEBasC1wLYAW4AuCBcYFyQLmAugBdcC7QLugXmBesC9wL7AYEAwqBhoGHwMUAxUBjUDHgMgAZEAyUBlcDMAMxAZpAzgDOYGeAZ9A0EDQgGigNPga0BrcDXQNeAbIA2oBtoDcAG5QN0A3WBvoG_QOEA4aBxIHFAOOAckA5SBzAHMgOeAdPA60DsAHcAO7Ad7A8IDwwHoQPTA9QYCzAAOAAkAB4AFIAMAAyACKAFIAVAAsABiADUAH8AQgBDACYAFMALgAXoAwgDEAGYANsAfwCCgEaAR4AkwBKgCZgE-AUAApABUACtAFlALcAuABjwDKAMsAZ0A0wDVAG0AOCAcQByADmAHZAO8A8IB5gHpAPoA_AB_wEJAQoAiABEgCMAEcAJKASsAloBMACbwE8AT4AoIBRQCkAFLAKiAVcArcBXQFfALEAWYAucBdgF3ALyAXwAvwBhADFQGcAZ0A0EBpgGnANaAbQA3gBwoDmgOcAdUA7IB2wDvgHiAPWAe0A-QB-wECAIHAQkAhcBD4CJQEWAI4gR0BHYCPQEggJDASKAk4BKICVIEvAS_AmECYgEzQJsAm0BOICdwE_gKFAUQAooBRkCjgKQAUzApsCnIFPAU-AqIBUkCrQKvAVmArYBYkCxwLJgWWBZgCzgFogLVgWuBbEC2wLcAXAAuOBcwF0ALrgXaBd0C8gL0gXuBfAC-wGBAMKAYaAw-BigGKgMaAY8AyABkQDJQGVgMxAZpAzgDOYGeAZ9A0EDQgGigNPga0BroDZIG1AbYA3CBugG6wN9A36BwgHDAOJAccA5IBykDmAOZAc8A6eB1oHYAO4Ad2A72B4QHhgPQgemB6hAHAAAGAA4AEgALAAaAA8ACgAFoAMgA0AB0AEQAJAAVAAsABcADEAH8AQQBDgCYAJoAUwAqgBXAC5AF4AX4AwgDEAGYANAAbQA3gB6gD-AQIAi4BGgEeAJEASYAlYBPgFAAKQAVAAqgBWwCxALKAW4BcgC-AGEAMSAZQBlwDNAM6AaYBqgDYAG1AN8A4ABxADkgHMAc4A7IB3gHhAPMA9AB7QD5APwAf4BBYCEgIUARAAikBGAEZAI4ASUAlIBKwCXAEwgJuAnABPACfAFBAKGAUWApACkgFLAKeAVEAq4BWQCtwFdAV8AsQBZoC0ALSAXOAuwC7gF5AL4AX4AwABhADFAGZgM4AzoBoIDTANOAasA1oBtADeAHCAObAdQB1QDrgHZAO2Ad8A8QB6ID1APWAe2A_ID-AIAAQIAgcBCcCFwIYAQ-AiGBEoETAIsgRwBHcCPQI-gSCBIoCTgEogJUASuAlqBLwEvwJhAmIBMwCaYE2ATaAnEBO4Cf4FCAUKAoiBRgFIQKSApOBTIFOQKeAp8BUQCpIFWgVeArMBW0CvgK_gWIBYsCxwLJgWWBZgCzgFogLTAWrAtcC3AFvALggXGBckC5wLogXWBdwC8gF6QL2Av2BgIGBgMKgYYBh4DEoGKAYqAxoBjwDIAGRAMlAZOAysBloDMQGaQM3Az-BoIGhQNEA0UBo8DSQNLAaeA1OBqoGrQNaA10Br4DYQGyQNrA2wBtwDcIG6AbrA3kDeoG-gb9A4ADgYHCAcMA4kBxgDjgHJQOYA5mBzwHPgOjgdKB08DqQOqgdYB2ADtQHcAO7gd6B3wDwYHhgeIA8eB5IHlQPOA9GB6YHqAAA.YAAADlgAAAAA; sq=ca=12_s; uuid=329ea780-e23e-4a7a-95d6-42e5809a9590; atauthority=%7B%22name%22%3A%22atauthority%22%2C%22val%22%3A%7B%22authority_name%22%3A%22cnil%22%2C%22visitor_mode%22%3A%22exempt%22%7D%2C%22options%22%3A%7B%22end%22%3A%222022-05-03T16%3A49%3A50.229Z%22%2C%22path%22%3A%22%2F%22%7D%7D; utag_main=v_id:01788e2e77c300068bd1607ce78703082001907a0086e$_sn:1$_ss:0$_pn:6%3Bexp-session$_st:1617297591309$ses_id:1617293113283%3Bexp-session; ry_ry-l3b0nco_so_realytics=eyJpZCI6InJ5XzI0NEEyRDRFLTczQ0YtNEM1Ni05QzQzLUEyODM2RUVCMTgwOSIsImNpZCI6bnVsbCwib3JpZ2luIjpmYWxzZSwicmVmIjpudWxsLCJjb250IjpudWxsLCJucyI6ZmFsc2V9; datadome=P.ET0cit9RXOIGczOmrCZJgZvwj5Fru_9hvFKNjJr7s_Xfvij0567n63a.kr5V9uHeRiKESHAjrumWkR4E5LG0iFh~us0COUR9m9X4Jf3i'

        urls_ads_from_page_one = 'https://www.leboncoin.fr/recherche?category=9&locations=r_12&sort=price&order=asc&real_estate_type=3&square=500-max&page=1'

        i_1 = 0

        try:
            headers_urls_ads_from_one_page = {
                'authority': 'www.leboncoin.fr',
                'method': 'GET',
                'path': urls_ads_from_page_one.replace('https://www.leboncoin.fr', ''),
                'scheme': 'https',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'fr,fr-FR;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
                'cache-control': 'max-age=0',
                'cookie': cookie,
                'dnt': '1',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'none',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.54'
            }

            # Request the content of a page from the url
            response = requests.get(urls_ads_from_page_one, headers=headers_urls_ads_from_one_page)

            # Parse the content of html_doc
            soup_urls_ads_from_one_page = BeautifulSoup(response.text, 'html.parser')

            number_of_pages = 0

            if soup_urls_ads_from_one_page.find("span", {"class": "_3Ce01 _137P- P4PEa _35DXM"}) is not None:
                number_of_pages_with_coma = int(soup_urls_ads_from_one_page.find("span", {"class": "_3Ce01 _137P- P4PEa _35DXM"})
                                                .text
                                                .replace(" ", "")
                                                .replace("results", "")
                                                ) / 35

                if int(str(number_of_pages_with_coma).split(".")[1][:1]) < 5:
                    number_of_pages += round(number_of_pages_with_coma) + 1
                    print('number_of_pages : ' + str(number_of_pages))
                elif int(str(number_of_pages_with_coma).split(".")[1][:1]) >= 5:
                    number_of_pages += round(number_of_pages_with_coma)
                    print('number_of_pages : ' + str(number_of_pages))
            else:
                print("error pages")

            try:
                for i_page in range(1, number_of_pages + 1):
                    urls_ads_from_one_page = urls_ads_from_page_one[:-1] + str(i_page)

                    print(urls_ads_from_one_page)

                    headers_urls_ads_from_one_page = {
                        'authority': 'www.leboncoin.fr',
                        'method': 'GET',
                        'scheme': 'https',
                        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                        'accept-encoding': 'gzip, deflate, br',
                        'accept-language': 'fr,fr-FR;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
                        'cache-control': 'max-age=0',
                        'cookie': cookie,
                        'dnt': '1',
                        'sec-fetch-dest': 'document',
                        'sec-fetch-mode': 'navigate',
                        'sec-fetch-site': 'none',
                        'sec-fetch-user': '?1',
                        'upgrade-insecure-requests': '1',
                        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.54'
                    }

                    time.sleep(3)

                    # Request the content of a page from the url
                    response = requests.get(urls_ads_from_one_page, headers=headers_urls_ads_from_one_page)

                    # Parse the content of html_doc
                    soup = BeautifulSoup(response.text, 'html.parser')

                    if soup.find("a", {"data-qa-id": "aditem_container"}) is not None:
                        all_a = soup.find_all("a", {"data-qa-id": "aditem_container"})

                        for a in all_a:
                            url_ad = "https://www.leboncoin.fr" + a.get("href")

                            i_1 += 1

                            try:
                                headers = {
                                    'authority': 'www.leboncoin.fr',
                                    'method': 'GET',
                                    'path': url_ad.replace('https://www.leboncoin.fr', ''),
                                    'scheme': 'https',
                                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                                    'accept-encoding': 'gzip, deflate, br',
                                    'accept-language': 'fr,fr-FR;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
                                    'cache-control': 'max-age=0',
                                    'cookie': cookie,
                                    'dnt': '1',
                                    'sec-fetch-dest': 'document',
                                    'sec-fetch-mode': 'navigate',
                                    'sec-fetch-site': 'none',
                                    'sec-fetch-user': '?1',
                                    'upgrade-insecure-requests': '1',
                                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.54'
                                }

                                time.sleep(5)

                                response = requests.get(url_ad, headers=headers)

                                soup = BeautifulSoup(response.text, 'html.parser')

                                try:
                                    if soup.find("div", {"class": "css-iel3r1"}) is not None:
                                        surface = soup.find("div", {"class": "css-iel3r1"}).text.split("·")[0]\
                                            .replace(" m²", "").replace(" ", "").replace("Pièce", "")

                                        if int(surface) >= 10000:
                                            print("ad " + str(i_1) + " : " + url_ad + " / surface : " + surface)
                                    else:
                                        print("no price")
                                except Exception as e:
                                    print("error price : " + str(e))
                            except Exception as e:
                                print("error request url_ad : " + str(e))
                    else:
                        print("no a data-qa-id aditem_container")
            except Exception as e:
                print("error for : " + str(e))
        except Exception as e:
            print("error request url_ad : " + str(e))

    def test_extract_suitable_lands_for_headquarters(self):
        print("test_extract_suitable_lands_for_headquarters")

        cookie = '__Secure-InstanceId=daaa5092-79b4-4631-a45c-e63de8a11fa2; sq=ca=12_s; uuid=d9c7dadf-0224-4592-9de9-9541a88d99fe; datadome=JIekCi~V4jFInllRclkGSt6lwQ_~b4T-D~yYrMwIz4sAC.c72dHfZ2fRREzQ_95hyQ.7.pJncHZ_w8Eslcm1wYJHOcd~OkKuC~sb_gxGFB; utag_main=v_id:0178a323963a0020ce991c3b38cc03083001907b0086e$_sn:3$_ss:0$_st:1617780058787$_pn:5%3Bexp-session$ses_id:1617776472449%3Bexp-session'

        urls_ads_from_page_one = 'https://www.leboncoin.fr/recherche?category=9&locations=r_12&real_estate_type=3&price=min-50000&square=500-max&page=1'

        print('Process array_code_insee_commune_with_train_station_for_travellers starting')
        array_code_insee_commune_train_station_travellers = []
        f = open('gares_ferroviaires_de_tous_types_exploitees_ou_non.json', "r")
        data = json.loads(f.read())
        for feature in data:
            code_postal = feature['fields']['cp']

            nom = feature['fields']['ville']

            url = "https://geo.api.gouv.fr/communes?codePostal=" + str(code_postal)

            payload = {}
            headers = {}

            response = requests.request("GET", url, headers=headers, data=payload)

            informations_pour_une_commune_avec_son_code_postal = response.json()

            for commune in informations_pour_une_commune_avec_son_code_postal:
                if commune['nom'] == nom and 'Voyageur' in feature['fields']['nature']:
                    array_code_insee_commune_train_station_travellers.append(str(commune['code']))
        f.close()
        print('Process array_code_insee_commune_with_train_station_for_travellers ok')

        print('Process array_code_insee_commune_desservies_par_gaz starting')
        array_code_insee_commune_desservies_par_gaz = []
        f = open('communes-desservies-en-gaz.json', "r")
        data = json.loads(f.read())
        for feature in data['features']:
            code_insee_commune = feature['properties']['code_insee_commune'][1:]
            array_code_insee_commune_desservies_par_gaz.append(str(code_insee_commune))
        f.close()
        print('Process array_code_insee_commune_desservies_par_gaz ok')

        i_1 = 0

        try:
            headers_urls_ads_from_one_page = {
                'authority': 'www.leboncoin.fr',
                'method': 'GET',
                'path': urls_ads_from_page_one.replace('https://www.leboncoin.fr', ''),
                'scheme': 'https',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'fr,fr-FR;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
                'cache-control': 'max-age=0',
                'cookie': cookie,
                'dnt': '1',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'none',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.54'
            }

            response = requests.get(urls_ads_from_page_one, headers=headers_urls_ads_from_one_page)

            soup_urls_ads_from_one_page = BeautifulSoup(response.text, 'html.parser')

            number_of_pages = 0

            if soup_urls_ads_from_one_page.find("span", {"class": "_3Ce01 _137P- P4PEa _35DXM"}) is not None:
                number_of_pages_with_coma = int(soup_urls_ads_from_one_page.find("span", {"class": "_3Ce01 _137P- P4PEa _35DXM"})
                                                .text
                                                .replace(" ", "")
                                                .replace("results", "")
                                                ) / 35

                if int(str(number_of_pages_with_coma).split(".")[1][:1]) < 5:
                    number_of_pages += round(number_of_pages_with_coma) + 1
                    print('number_of_pages : ' + str(number_of_pages))
                elif int(str(number_of_pages_with_coma).split(".")[1][:1]) >= 5:
                    number_of_pages += round(number_of_pages_with_coma)
                    print('number_of_pages : ' + str(number_of_pages))
            else:
                print("error pages")

            try:
                for i_page in range(1, number_of_pages + 1):
                    urls_ads_from_one_page = urls_ads_from_page_one[:-1] + str(i_page)

                    print(urls_ads_from_one_page)

                    headers_urls_ads_from_one_page = {
                        'authority': 'www.leboncoin.fr',
                        'method': 'GET',
                        'scheme': 'https',
                        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                        'accept-encoding': 'gzip, deflate, br',
                        'accept-language': 'fr,fr-FR;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
                        'cache-control': 'max-age=0',
                        'cookie': cookie,
                        'dnt': '1',
                        'sec-fetch-dest': 'document',
                        'sec-fetch-mode': 'navigate',
                        'sec-fetch-site': 'none',
                        'sec-fetch-user': '?1',
                        'upgrade-insecure-requests': '1',
                        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.54'
                    }

                    time.sleep(5)

                    response = requests.get(urls_ads_from_one_page, headers=headers_urls_ads_from_one_page)

                    soup = BeautifulSoup(response.text, 'html.parser')

                    if soup.find("a", {"data-qa-id": "aditem_container"}) is not None:
                        all_a = soup.find_all("a", {"data-qa-id": "aditem_container"})

                        for a in all_a:
                            i_1 += 1

                            try:
                                url_ad = "https://www.leboncoin.fr" + a.get("href")

                                print(str(i_1) + " : " + url_ad)

                                headers_url_ad = {
                                    'authority': 'www.leboncoin.fr',
                                    'method': 'GET',
                                    'path': url_ad.replace('https://www.leboncoin.fr', ''),
                                    'scheme': 'https',
                                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                                    'accept-encoding': 'gzip, deflate, br',
                                    'accept-language': 'fr,fr-FR;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
                                    'cache-control': 'max-age=0',
                                    'cookie': cookie,
                                    'dnt': '1',
                                    'sec-fetch-dest': 'document',
                                    'sec-fetch-mode': 'navigate',
                                    'sec-fetch-site': 'none',
                                    'sec-fetch-user': '?1',
                                    'upgrade-insecure-requests': '1',
                                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.54'
                                }

                                time.sleep(5)

                                response_url_ad = requests.get(url_ad, headers=headers_url_ad)

                                soup_url_ad = BeautifulSoup(response_url_ad.text, 'html.parser')

                                title = ""

                                try:
                                    if soup_url_ad.find("h1", {"data-qa-id": "adview_title"}) is not None:
                                        title += soup_url_ad.find("h1", {"data-qa-id": "adview_title"}).text.lower()
                                    else:
                                        print("no title")
                                except Exception as e:
                                    print("error title : " + str(e))

                                description = ""

                                try:
                                    if soup_url_ad.find("div", {"data-qa-id": "adview_description_container"}) is not None:
                                        description += soup_url_ad.find("div", {"data-qa-id": "adview_description_container"}) \
                                            .text.replace("\n", "").replace("\t", "").replace("\r", "").lower()
                                    else:
                                        print("no description")
                                except Exception as e:
                                    print("error description : " + str(e))

                                code_postal = ""

                                try:
                                    if soup_url_ad.find("li", {"data-qa-id": "breadcrumb-item-4"}) is not None:
                                        location = soup_url_ad.find("li", {"data-qa-id": "breadcrumb-item-4"}).text \
                                            .replace(" ", "") \
                                            .replace("\t", "") \
                                            .replace("\n", "") \
                                            .replace("\r", "")

                                        code_postal += location[len(location) - 5:]
                                    else:
                                        print("no location_city")
                                except Exception as e:
                                    print("error location_city : " + str(e))

                                try:
                                    response = requests.request("GET", "https://geo.api.gouv.fr/communes?codePostal=" + code_postal)

                                    code_insee_commune = json.loads(response.text)[0]['code']

                                    population = json.loads(response.text)[0]['population']

                                    print(str(i_1) + " : " + url_ad + " / " + str(code_postal)
                                          + " / population : " + str(population))

                                    if code_insee_commune in array_code_insee_commune_train_station_travellers\
                                            and\
                                            code_insee_commune in array_code_insee_commune_desservies_par_gaz\
                                            and\
                                            population <= 1000\
                                            and\
                                            ("loisir" not in description
                                             or "non constructible" not in description
                                             or "boisé" not in description)\
                                            and\
                                            ("loisir" not in title
                                             or "non constructible" not in title
                                             or "boisé" not in title):
                                        print(str(i_1) + " url_ad : " + url_ad + " good")
                                    else:
                                        print(str(i_1) + " : bad")
                                except Exception as e:
                                    print(str(i_1) + " : error location code postal : " + str(e))
                            except Exception as e:
                                print(str(i_1) + " : error request url_ad : " + str(e))
                    else:
                        print("no a data-qa-id aditem_container")
            except Exception as e:
                print("error for : " + str(e))
        except Exception as e:
            print("error request url_ad : " + str(e))

    def test_extract_suitable_lands_for_headquarters_for_excel(self):
        print("test_extract_suitable_lands_for_headquarters_for_excel")

        cookie = '__Secure-InstanceId=509c491d-5f2e-44aa-b23a-a2db484459a9; utag_main=v_id:0178ad44bb91000a96a60c7c78c703083007807b0086e$_sn:1$_ss:0$_pn:2%3Bexp-session$_st:1617816467514$ses_id:1617814666129%3Bexp-session; didomi_token=eyJ1c2VyX2lkIjoiMTc4YWQ0NGItOWNiNC02MDA2LTg1N2UtNmY3ZWY1ZjY2NTE0IiwiY3JlYXRlZCI6IjIwMjEtMDQtMDdUMTY6NTc6NTQuNjY1WiIsInVwZGF0ZWQiOiIyMDIxLTA0LTA3VDE2OjU3OjU0LjY2NVoiLCJ2ZW5kb3JzIjp7ImRpc2FibGVkIjpbImFtYXpvbiIsInNhbGVzZm9yY2UiLCJnb29nbGUiLCJjOm5leHQtcGVyZm9ybWFuY2UiLCJjOmNvbGxlY3RpdmUtaGhTWXRSVm4iLCJjOnJvY2t5b3UiLCJjOnB1Ym9jZWFuLWI2QkpNdHNlIiwiYzpydGFyZ2V0LUdlZk1WeWlDIiwiYzpzY2hpYnN0ZWQtTVFQWGFxeWgiLCJjOmdyZWVuaG91c2UtUUtiR0JrczQiLCJjOnJlYWx6ZWl0Zy1iNktDa3h5ViIsImM6dmlkZW8tbWVkaWEtZ3JvdXAiLCJjOnN3aXRjaC1jb25jZXB0cyIsImM6bHVjaWRob2xkLXlmdGJXVGY3IiwiYzpsZW1vbWVkaWEtemJZaHAyUWMiLCJjOnlvcm1lZGlhcy1xbkJXaFF5UyIsImM6c2Fub21hIiwiYzpyYWR2ZXJ0aXMtU0pwYTI1SDgiLCJjOnF3ZXJ0aXplLXpkbmdFMmh4IiwiYzp2ZG9waWEiLCJjOnJldmxpZnRlci1jUnBNbnA1eCIsImM6cmVzZWFyY2gtbm93IiwiYzp3aGVuZXZlcm0tOFZZaHdiMlAiLCJjOmFkbW90aW9uIiwiYzp3b29iaSIsImM6c2hvcHN0eWxlLWZXSksyTGlQIiwiYzp0aGlyZHByZXNlLVNzS3dtSFZLIiwiYzpiMmJtZWRpYS1wUVRGZ3lXayIsImM6cHVyY2giLCJjOmxpZmVzdHJlZXQtbWVkaWEiLCJjOnN5bmMtbjc0WFFwcmciLCJjOmludG93b3dpbi1xYXp0NXRHaSIsImM6ZGlkb21pIiwiYzpyYWRpdW1vbmUiLCJjOmFkb3Rtb2IiLCJjOmFiLXRhc3R5IiwiYzpncmFwZXNob3QiLCJjOmFkbW9iIiwiYzphZGFnaW8iLCJjOmxiY2ZyYW5jZSJdfSwicHVycG9zZXMiOnsiZGlzYWJsZWQiOlsicGVyc29ubmFsaXNhdGlvbmNvbnRlbnUiLCJwZXJzb25uYWxpc2F0aW9ubWFya2V0aW5nIiwicHJpeCIsIm1lc3VyZWF1ZGllbmNlIiwiZXhwZXJpZW5jZXV0aWxpc2F0ZXVyIl19LCJ2ZW5kb3JzX2xpIjp7ImVuYWJsZWQiOlsiZ29vZ2xlIl19LCJ2ZXJzaW9uIjoyLCJhYyI6IkFBQUEuREUyQXdBRUlBZm9CaFFEeEFIbUFTU0Frc0NKSUhFQU9yQWlEQkZLQ0tnRW00SnZBVGtBdHJCYmVDNHdGeVFMbGdZREF3aUJpYUFBQSJ9; euconsent-v2=CPESu27PESu27AHABBENBUCgAAAAAHLAAAAAAAAOdAJMNS-AATEscCSaNKoUQIQrCQqAUAFFCMLRNYQEjgp2VwEeoIEACE1ARgRAgxBRiwCAAQCAJCIgBADwQCIAiAQAAgBUgIQAESAALACwMAgAFANCgAigCECQgiMCo5TAgIkWignkDAAIAAAAAAAAAAAAAAAQAxQLkAA4ACQAGgAPAApABgAGQARQApACoAFgAMQAawA-AD-AIQAhgBMAC0AFyALwAvwBhAGIAMwAbQA8AB6gD-AQQAhYBGgEcAJMASoAmYBPgFAAKQAVAArQBZQC3ALiAZQBlwDNAM6AaYBqgDYAG0AOCAcQByADmAHZAO8A8IB5gHpAPkA-gB-AD_gIKAg0BCQEKAIgARgAjkBJQEmAJXAS0BLgCYAE3gJ4AnwBQQCigFIAKWAVEAq8BXQFfALNAWgBaQC5wF2AXcAvIBfAC_AGBAMIAYqAzgDOgGgANOAa0A2gBvADhQHNAc4A6oB2QDtgHfAPEAesA9sB-gH7AP-AgQBA4CDAEJAIXAQ-AiUBFgCOIEdAR2Aj0BIICQwEigJRASpAl4CX4EwgTEAmaBNgE2gJ3AT-AoUBRACigFGQKOApABTMCmwKcAU-AqIBUkCrQKvAVmAraBYgFiwLHAsmBZYFmALOAWiAtWBa4FsALcAXBAuMC5IFzAXQAuuBdoF3QLzAvWBe4F9gMCAYVAw0DD4GKAYqAxqBjwGQAMiAZKAyuBmAGYgM0gZwBnMDPAM-gaCBoQDRQGnwNaA1uBroGvANgAbIA2oBtoDcAG5QN0A3WBvoG_QOEA4aBxIHFAOOAckA5SBzAHMgOeAdPA60DsAHcAO7Ad7A8IDwwHoQPTA9QB6wwFqAAcABIADwAKQAYABkAEUAKQAqABYADEAGoAP4AhACGAEwAKYAXAAvQBhAGIAMwAbYA_gEFAI0AjwBJgCVAEzAJ8AoABSACoAFaALKAW4BcADHgGUAZYAzoBpgGqANoAcEA4gDkAHMAOyAd4B4QDzAPSAfQB-AD_gISAhQBEACJAEYAI4ASUAlYBLQCYAE3gJ4AnwBQQCigFIAKWAVEAq4BW4CugK-AWIAswBc4C7ALuAXkAvgBfgDCAGKgM4AzoBoIDTANOAa0A2gBvADhQHNAc4A6oB2QDtgHfAPEAesA9oB8gD9gIEAQOAhIBC4CHwESgIsARxAjoCOwEegJBASGAkUBJwCUQEqQJeAl-BMIExAJmgTYBNoCcQE7gJ_AUKAogBRQCjIFHAUgApmBTYFOQKeAp8BUQCpIFWgVeArMBWwCxIFjgWTAssCzAFnALRAWrAtcC2IFtgW4AuABccC5gLoAXXAu0C7oF5AXpAvcC-AF9gMCAYUAw0Bh8DFAMVAY0Ax4BkADIgGSgMrAZiAzSBnAGcwM8Az6BoIGhANFAafA1oDXQGwANkgbUBtgDcIG6AbrA30DfoHCAcMA4kBxwDkgHKQOYA5kBzwDp4HWgdgA7gB3YDvYHhAeGA9CB6YHqAPWIA4AAAwAHAAkABYADQAHgAUAAtABkAGgAOgAiABIACoAFgALgAYgA_gCCAIcATABNACmAFUAK4AXIAvAC_AGEAYgAzABoADaAG8APUAfwCBAEXAI0AjwBIgCTAErAJ8AoABSACoAFUAK2AWIBZQC3ALkAXwAwgBiQDKAMuAZoBnQDTANUAbAA2oBvgHAAOIAckA5gDnAHZAO8A8IB5gHoAPaAfIB-AD_AILAQkBCgCIAEUgIwAjIBHACSgEpAJWAS4AmEBNwE4AJ4AT4AoIBQwCiwFIAUkApYBTwCogFXAKyAVuAroCvgFiALNAWgBaQC5wF2AXcAvIBfAC_AGAAMIAYoAzMBnAGdANBAaYBpwDVgGtANoAbwA4QBzYDqAOqAdcA7IB2wDvgHiAPRAeoB6wD2wH5AfwBAACBAEDgITgQuBDACHwEQwIlAiYBFkCOAI7gR6BH0CQQJFAScAlEBKgCVwEtQJeAl-BMIExAJmATTAmwCbQE4gJ3AT_AoQChQFEQKMApCBSQFJwKZApyBTwFPgKiAVJAq0CrwFZgK2gV8BX8CxALFgWOBZMCywLMAWcAtEBaYC1YFrgW4At4BcEC4wLkgXOBdEC6wLuAXkAvSBewF-wMBAwMBhUDDAMPAYlAxQDFQGNAMeAZAAyIBkoDJwGVgMtAZiAzSBm4GfwNBA0KBogGigNHgaSBpYDTwGpwNVA1aBrQGuwNfA2EBskDawNsAbcA3CBugG6wN5A3qBvoG_QOAA4GBwgHDAOJAcYA44ByUDmAOZgc8Bz4Do4HSgdPA6kDqoHWAdgA7UB3ADu4Hegd8A8GB4YHiAPHgeSB5UDzgPRgemB6gD1gAAA.YAAADlgAAAAA; datadome=EDPQ-CF1007.FKA3dW.Ylfa~PI94VPGo8ddS2PHNoFwM71OB7kXY-0sLF-cI9gIxpPrVMn0d~D2tm6FyceZNPd4ATGKQvt1iLcogHWHDa0'

        urls_ads_from_page_one = 'https://www.leboncoin.fr/recherche?category=9&locations=r_12&real_estate_type=3&price=50000-100000&square=500-max&page=1'

        workbook = xlsxwriter.Workbook('suitable_lands_for_headquarters.xlsx')

        worksheet = workbook.add_worksheet()

        row = 0

        worksheet.write(row, 0, "url_ad")

        worksheet.write(row, 1, "code_postal")

        worksheet.write(row, 2, "population")

        print('Process array_code_insee_commune_with_train_station_for_travellers starting')
        array_code_insee_commune_train_station_travellers = []
        f = open('gares_ferroviaires_de_tous_types_exploitees_ou_non.json', "r")
        data = json.loads(f.read())
        for feature in data:
            code_postal = feature['fields']['cp']

            nom = feature['fields']['ville']

            url = "https://geo.api.gouv.fr/communes?codePostal=" + str(code_postal)

            payload = {}
            headers = {}

            response = requests.request("GET", url, headers=headers, data=payload)

            informations_pour_une_commune_avec_son_code_postal = response.json()

            for commune in informations_pour_une_commune_avec_son_code_postal:
                if commune['nom'] == nom and 'Voyageur' in feature['fields']['nature']:
                    array_code_insee_commune_train_station_travellers.append(str(commune['code']))
        f.close()
        print('Process array_code_insee_commune_with_train_station_for_travellers ok')

        print('Process array_code_insee_commune_desservies_par_gaz starting')
        array_code_insee_commune_desservies_par_gaz = []
        f = open('communes-desservies-en-gaz.json', "r")
        data = json.loads(f.read())
        for feature in data['features']:
            code_insee_commune = feature['properties']['code_insee_commune'][1:]
            array_code_insee_commune_desservies_par_gaz.append(str(code_insee_commune))
        f.close()
        print('Process array_code_insee_commune_desservies_par_gaz ok')

        i_1 = 0

        try:
            headers_urls_ads_from_one_page = {
                'authority': 'www.leboncoin.fr',
                'method': 'GET',
                'path': urls_ads_from_page_one.replace('https://www.leboncoin.fr', ''),
                'scheme': 'https',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'fr,fr-FR;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
                'cache-control': 'max-age=0',
                'cookie': cookie,
                'dnt': '1',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'none',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.54'
            }

            time.sleep(5)

            response = requests.get(urls_ads_from_page_one, headers=headers_urls_ads_from_one_page)

            soup_urls_ads_from_one_page = BeautifulSoup(response.text, 'html.parser')

            number_of_pages = 0

            if soup_urls_ads_from_one_page.find("span", {"class": "_3Ce01 _137P- P4PEa _35DXM"}) is not None:
                number_of_pages_with_coma = int(soup_urls_ads_from_one_page.find("span", {"class": "_3Ce01 _137P- P4PEa _35DXM"})
                                                .text
                                                .replace(" ", "")
                                                .replace("results", "")
                                                ) / 35

                if int(str(number_of_pages_with_coma).split(".")[1][:1]) < 5:
                    number_of_pages += round(number_of_pages_with_coma) + 1
                    print('number_of_pages : ' + str(number_of_pages))
                elif int(str(number_of_pages_with_coma).split(".")[1][:1]) >= 5:
                    number_of_pages += round(number_of_pages_with_coma)
                    print('number_of_pages : ' + str(number_of_pages))
            else:
                print("error pages")

            try:
                for i_page in range(1, number_of_pages + 1):
                    urls_ads_from_one_page = urls_ads_from_page_one[:-1] + str(i_page)

                    print(urls_ads_from_one_page)

                    headers_urls_ads_from_one_page = {
                        'authority': 'www.leboncoin.fr',
                        'method': 'GET',
                        'scheme': 'https',
                        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                        'accept-encoding': 'gzip, deflate, br',
                        'accept-language': 'fr,fr-FR;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
                        'cache-control': 'max-age=0',
                        'cookie': cookie,
                        'dnt': '1',
                        'sec-fetch-dest': 'document',
                        'sec-fetch-mode': 'navigate',
                        'sec-fetch-site': 'none',
                        'sec-fetch-user': '?1',
                        'upgrade-insecure-requests': '1',
                        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.54'
                    }

                    time.sleep(5)

                    response = requests.get(urls_ads_from_one_page, headers=headers_urls_ads_from_one_page)

                    soup = BeautifulSoup(response.text, 'html.parser')

                    if soup.find("a", {"data-qa-id": "aditem_container"}) is not None:
                        all_a = soup.find_all("a", {"data-qa-id": "aditem_container"})

                        for a in all_a:
                            i_1 += 1

                            row += 1

                            try:
                                url_ad = "https://www.leboncoin.fr" + a.get("href")

                                print(str(i_1) + " : " + url_ad)

                                headers_url_ad = {
                                    'authority': 'www.leboncoin.fr',
                                    'method': 'GET',
                                    'path': url_ad.replace('https://www.leboncoin.fr', ''),
                                    'scheme': 'https',
                                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                                    'accept-encoding': 'gzip, deflate, br',
                                    'accept-language': 'fr,fr-FR;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
                                    'cache-control': 'max-age=0',
                                    'cookie': cookie,
                                    'dnt': '1',
                                    'sec-fetch-dest': 'document',
                                    'sec-fetch-mode': 'navigate',
                                    'sec-fetch-site': 'none',
                                    'sec-fetch-user': '?1',
                                    'upgrade-insecure-requests': '1',
                                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.54'
                                }

                                time.sleep(5)

                                response_url_ad = requests.get(url_ad, headers=headers_url_ad)

                                soup_url_ad = BeautifulSoup(response_url_ad.text, 'html.parser')

                                title = ""

                                try:
                                    if soup_url_ad.find("h1", {"data-qa-id": "adview_title"}) is not None:
                                        title += soup_url_ad.find("h1", {"data-qa-id": "adview_title"}).text.lower()
                                    else:
                                        print("no title")
                                except Exception as e:
                                    print("error title : " + str(e))

                                description = ""

                                try:
                                    if soup_url_ad.find("div", {"data-qa-id": "adview_description_container"}) is not None:
                                        description += soup_url_ad.find("div", {"data-qa-id": "adview_description_container"}) \
                                            .text.replace("\n", "").replace("\t", "").replace("\r", "").lower()
                                    else:
                                        print("no description")
                                except Exception as e:
                                    print("error description : " + str(e))

                                code_postal = ""

                                try:
                                    if soup_url_ad.find("li", {"data-qa-id": "breadcrumb-item-4"}) is not None:
                                        location = soup_url_ad.find("li", {"data-qa-id": "breadcrumb-item-4"}).text \
                                            .replace(" ", "") \
                                            .replace("\t", "") \
                                            .replace("\n", "") \
                                            .replace("\r", "")

                                        code_postal += location[len(location) - 5:]
                                    else:
                                        print("no location_city")
                                except Exception as e:
                                    print("error location_city : " + str(e))

                                try:
                                    response = requests.request("GET", "https://geo.api.gouv.fr/communes?codePostal=" + code_postal)

                                    code_insee_commune = json.loads(response.text)[0]['code']

                                    population = json.loads(response.text)[0]['population']

                                    print(str(i_1) + " : " + url_ad + " / " + str(code_postal)
                                          + " / population : " + str(population))

                                    if code_insee_commune in array_code_insee_commune_train_station_travellers\
                                            and\
                                            code_insee_commune in array_code_insee_commune_desservies_par_gaz\
                                            and\
                                            population <= 1000\
                                            and\
                                            ("loisir" not in description
                                             or "non constructible" not in description
                                             or "boisé" not in description)\
                                            and\
                                            ("loisir" not in title
                                             or "non constructible" not in title
                                             or "boisé" not in title):
                                        print(str(i_1) + " url_ad : " + url_ad + " good")

                                        worksheet.write(row, 0, url_ad)

                                        worksheet.write(row, 1, code_postal)

                                        worksheet.write(row, 1, population)
                                    else:
                                        print(str(i_1) + " : bad")
                                except Exception as e:
                                    print(str(i_1) + " : error location code postal : " + str(e))
                            except Exception as e:
                                print(str(i_1) + " : error request url_ad : " + str(e))
                    else:
                        print("no a data-qa-id aditem_container")
            except Exception as e:
                print("error for : " + str(e))
        except Exception as e:
            print("error request url_ad : " + str(e))

        workbook.close()

    def test_extract_suitable_lands_for_headquarters_for_mysql(self):
        print("test_extract_suitable_lands_for_headquarters_for_mysql")

        cookie = ''

        urls_ads_from_page_one = ''

        print('Process array_code_insee_commune_with_train_station_for_travellers starting')
        array_code_insee_commune_train_station_travellers = []
        f = open('gares_ferroviaires_de_tous_types_exploitees_ou_non.json', "r")
        data = json.loads(f.read())
        for feature in data:
            code_postal = feature['fields']['cp']

            nom = feature['fields']['ville']

            url = "https://geo.api.gouv.fr/communes?codePostal=" + str(code_postal)

            payload = {}
            headers = {}

            response = requests.request("GET", url, headers=headers, data=payload)

            informations_pour_une_commune_avec_son_code_postal = response.json()

            for commune in informations_pour_une_commune_avec_son_code_postal:
                if commune['nom'] == nom and 'Voyageur' in feature['fields']['nature']:
                    array_code_insee_commune_train_station_travellers.append(str(commune['code']))
        f.close()
        print('Process array_code_insee_commune_with_train_station_for_travellers ok')

        print('Process array_code_insee_commune_desservies_par_gaz starting')
        array_code_insee_commune_desservies_par_gaz = []
        f = open('communes-desservies-en-gaz.json', "r")
        data = json.loads(f.read())
        for feature in data['features']:
            code_insee_commune = feature['properties']['code_insee_commune'][1:]
            array_code_insee_commune_desservies_par_gaz.append(str(code_insee_commune))
        f.close()
        print('Process array_code_insee_commune_desservies_par_gaz ok')

        i_1 = 0

        try:
            headers_urls_ads_from_one_page = {
                'authority': 'www.leboncoin.fr',
                'method': 'GET',
                'path': urls_ads_from_page_one.replace('https://www.leboncoin.fr', ''),
                'scheme': 'https',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'fr,fr-FR;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
                'cache-control': 'max-age=0',
                'cookie': cookie,
                'dnt': '1',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'none',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.54'
            }

            time.sleep(5)

            response = requests.get(urls_ads_from_page_one, headers=headers_urls_ads_from_one_page)

            soup_urls_ads_from_one_page = BeautifulSoup(response.text, 'html.parser')

            number_of_pages = 0

            if soup_urls_ads_from_one_page.find("span", {"class": "_3Ce01 _137P- P4PEa _35DXM"}) is not None:
                number_of_pages_with_coma = int(soup_urls_ads_from_one_page.find("span", {"class": "_3Ce01 _137P- P4PEa _35DXM"})
                                                .text
                                                .replace(" ", "")
                                                .replace("results", "")
                                                ) / 35

                if int(str(number_of_pages_with_coma).split(".")[1][:1]) < 5:
                    number_of_pages += round(number_of_pages_with_coma) + 1
                    print('number_of_pages : ' + str(number_of_pages))
                elif int(str(number_of_pages_with_coma).split(".")[1][:1]) >= 5:
                    number_of_pages += round(number_of_pages_with_coma)
                    print('number_of_pages : ' + str(number_of_pages))
            else:
                print("error pages")

            try:
                for i_page in range(1, number_of_pages + 1):
                    urls_ads_from_one_page = urls_ads_from_page_one[:-1] + str(i_page)

                    print(urls_ads_from_one_page)

                    headers_urls_ads_from_one_page = {
                        'authority': 'www.leboncoin.fr',
                        'method': 'GET',
                        'scheme': 'https',
                        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                        'accept-encoding': 'gzip, deflate, br',
                        'accept-language': 'fr,fr-FR;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
                        'cache-control': 'max-age=0',
                        'cookie': cookie,
                        'dnt': '1',
                        'sec-fetch-dest': 'document',
                        'sec-fetch-mode': 'navigate',
                        'sec-fetch-site': 'none',
                        'sec-fetch-user': '?1',
                        'upgrade-insecure-requests': '1',
                        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.54'
                    }

                    time.sleep(5)

                    response = requests.get(urls_ads_from_one_page, headers=headers_urls_ads_from_one_page)

                    soup = BeautifulSoup(response.text, 'html.parser')

                    if soup.find("a", {"data-qa-id": "aditem_container"}) is not None:
                        all_a = soup.find_all("a", {"data-qa-id": "aditem_container"})

                        for a in all_a:
                            i_1 += 1

                            try:
                                url_ad = "https://www.leboncoin.fr" + a.get("href")

                                print(str(i_1) + " : " + url_ad)

                                headers_url_ad = {
                                    'authority': 'www.leboncoin.fr',
                                    'method': 'GET',
                                    'path': url_ad.replace('https://www.leboncoin.fr', ''),
                                    'scheme': 'https',
                                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                                    'accept-encoding': 'gzip, deflate, br',
                                    'accept-language': 'fr,fr-FR;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
                                    'cache-control': 'max-age=0',
                                    'cookie': cookie,
                                    'dnt': '1',
                                    'sec-fetch-dest': 'document',
                                    'sec-fetch-mode': 'navigate',
                                    'sec-fetch-site': 'none',
                                    'sec-fetch-user': '?1',
                                    'upgrade-insecure-requests': '1',
                                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.54'
                                }

                                time.sleep(5)

                                response_url_ad = requests.get(url_ad, headers=headers_url_ad)

                                soup_url_ad = BeautifulSoup(response_url_ad.text, 'html.parser')

                                title = ""

                                try:
                                    if soup_url_ad.find("h1", {"data-qa-id": "adview_title"}) is not None:
                                        title += soup_url_ad.find("h1", {"data-qa-id": "adview_title"}).text.lower()
                                    else:
                                        print("no title")
                                except Exception as e:
                                    print("error title : " + str(e))

                                description = ""

                                try:
                                    if soup_url_ad.find("div", {"data-qa-id": "adview_description_container"}) is not None:
                                        description += soup_url_ad.find("div", {"data-qa-id": "adview_description_container"}) \
                                            .text.replace("\n", "").replace("\t", "").replace("\r", "").lower()
                                    else:
                                        print("no description")
                                except Exception as e:
                                    print("error description : " + str(e))

                                code_postal = ""

                                try:
                                    if soup_url_ad.find("li", {"data-qa-id": "breadcrumb-item-4"}) is not None:
                                        location = soup_url_ad.find("li", {"data-qa-id": "breadcrumb-item-4"}).text \
                                            .replace(" ", "") \
                                            .replace("\t", "") \
                                            .replace("\n", "") \
                                            .replace("\r", "")

                                        code_postal += location[len(location) - 5:]
                                    else:
                                        print("no location_city")
                                except Exception as e:
                                    print("error location_city : " + str(e))

                                try:
                                    response = requests.request("GET", "https://geo.api.gouv.fr/communes?codePostal=" + code_postal)

                                    code_insee_commune = json.loads(response.text)[0]['code']

                                    population = json.loads(response.text)[0]['population']

                                    print(str(i_1) + " : " + url_ad + " / " + str(code_postal)
                                          + " / population : " + str(population))

                                    if code_insee_commune in array_code_insee_commune_train_station_travellers\
                                            and\
                                            code_insee_commune in array_code_insee_commune_desservies_par_gaz\
                                            and\
                                            population <= 1000\
                                            and\
                                            ("loisir" not in description
                                             or "non constructible" not in description
                                             or "boisé" not in description)\
                                            and\
                                            ("loisir" not in title
                                             or "non constructible" not in title
                                             or "boisé" not in title):
                                        print(str(i_1) + " url_ad : " + url_ad + " good")

                                        try:
                                            connection = pymysql.connect(
                                                host='localhost',
                                                port=3306,
                                                user='root',
                                                password='8h0NEJkEf3lyCBUoPQwCHSu@@@@@@@',
                                                db='contacts_professionnels',
                                                charset='utf8mb4',
                                                cursorclass=pymysql.cursors.DictCursor
                                            )

                                            with connection.cursor() as cursor:
                                                try:
                                                    sql = "insert into annonces_immobilieres " \
                                                          "(url_ad, code_postal, population) value (%s, %s, %s)"

                                                    cursor.execute(sql, (url_ad, code_postal, population))

                                                    connection.commit()

                                                    connection.close()
                                                except Exception as e:
                                                    print("The record already exists : " + str(e))
                                                    connection.close()
                                        except Exception as e:
                                            print('There is a problem : ' + str(e))
                                    else:
                                        print(str(i_1) + " : bad")
                                except Exception as e:
                                    print(str(i_1) + " : error location code postal : " + str(e))
                            except Exception as e:
                                print(str(i_1) + " : error request url_ad : " + str(e))
                    else:
                        print("no a data-qa-id aditem_container")
            except Exception as e:
                print("error for : " + str(e))
        except Exception as e:
            print("error request url_ad : " + str(e))

    def test_extract_suitable_houses_for_headquarters_for_mysql(self):
        print("test_extract_suitable_houses_for_headquarters_for_mysql")

        cookie = ''

        urls_ads_from_page_one = ''

        print('Process array_code_insee_commune_with_train_station_for_travellers starting')
        array_code_insee_commune_train_station_travellers = []
        f = open('gares_ferroviaires_de_tous_types_exploitees_ou_non.json', "r")
        data = json.loads(f.read())
        for feature in data:
            code_postal = feature['fields']['cp']

            nom = feature['fields']['ville']

            url = "https://geo.api.gouv.fr/communes?codePostal=" + str(code_postal)

            payload = {}
            headers = {}

            response = requests.request("GET", url, headers=headers, data=payload)

            informations_pour_une_commune_avec_son_code_postal = response.json()

            for commune in informations_pour_une_commune_avec_son_code_postal:
                if commune['nom'] == nom and 'Voyageur' in feature['fields']['nature']:
                    array_code_insee_commune_train_station_travellers.append(str(commune['code']))
        f.close()
        print('Process array_code_insee_commune_with_train_station_for_travellers ok')

        print('Process array_code_insee_commune_desservies_par_gaz starting')
        array_code_insee_commune_desservies_par_gaz = []
        f = open('communes-desservies-en-gaz.json', "r")
        data = json.loads(f.read())
        for feature in data['features']:
            code_insee_commune = feature['properties']['code_insee_commune'][1:]
            array_code_insee_commune_desservies_par_gaz.append(str(code_insee_commune))
        f.close()
        print('Process array_code_insee_commune_desservies_par_gaz ok')

        i_1 = 0

        try:
            headers_urls_ads_from_one_page = {
                'authority': 'www.leboncoin.fr',
                'method': 'GET',
                'path': urls_ads_from_page_one.replace('https://www.leboncoin.fr', ''),
                'scheme': 'https',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'fr,fr-FR;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
                'cache-control': 'max-age=0',
                'cookie': cookie,
                'dnt': '1',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'none',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.54'
            }

            time.sleep(10)

            response = requests.get(urls_ads_from_page_one, headers=headers_urls_ads_from_one_page)

            soup_urls_ads_from_one_page = BeautifulSoup(response.text, 'html.parser')

            number_of_pages = 0

            if soup_urls_ads_from_one_page.find("span", {"class": "_3Ce01 _137P- P4PEa _35DXM"}) is not None:
                number_of_pages_with_coma = int(soup_urls_ads_from_one_page.find("span", {"class": "_3Ce01 _137P- P4PEa _35DXM"})
                                                .text
                                                .replace(" ", "")
                                                .replace("results", "")
                                                ) / 35

                if int(str(number_of_pages_with_coma).split(".")[1][:1]) < 5:
                    number_of_pages += round(number_of_pages_with_coma) + 1
                    print('number_of_pages : ' + str(number_of_pages))
                elif int(str(number_of_pages_with_coma).split(".")[1][:1]) >= 5:
                    number_of_pages += round(number_of_pages_with_coma)
                    print('number_of_pages : ' + str(number_of_pages))
            else:
                print("error pages")

            try:
                for i_page in range(1, number_of_pages + 1):
                    urls_ads_from_one_page = urls_ads_from_page_one[:-1] + str(i_page)

                    print(urls_ads_from_one_page)

                    headers_urls_ads_from_one_page = {
                        'authority': 'www.leboncoin.fr',
                        'method': 'GET',
                        'scheme': 'https',
                        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                        'accept-encoding': 'gzip, deflate, br',
                        'accept-language': 'fr,fr-FR;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
                        'cache-control': 'max-age=0',
                        'cookie': cookie,
                        'dnt': '1',
                        'sec-fetch-dest': 'document',
                        'sec-fetch-mode': 'navigate',
                        'sec-fetch-site': 'none',
                        'sec-fetch-user': '?1',
                        'upgrade-insecure-requests': '1',
                        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.54'
                    }

                    time.sleep(10)

                    response = requests.get(urls_ads_from_one_page, headers=headers_urls_ads_from_one_page)

                    soup = BeautifulSoup(response.text, 'html.parser')

                    if soup.find("a", {"data-qa-id": "aditem_container"}) is not None:
                        all_a = soup.find_all("a", {"data-qa-id": "aditem_container"})

                        for a in all_a:
                            i_1 += 1

                            try:
                                url_ad = "https://www.leboncoin.fr" + a.get("href")

                                print(str(i_1) + " : " + url_ad)

                                headers_url_ad = {
                                    'authority': 'www.leboncoin.fr',
                                    'method': 'GET',
                                    'path': url_ad.replace('https://www.leboncoin.fr', ''),
                                    'scheme': 'https',
                                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                                    'accept-encoding': 'gzip, deflate, br',
                                    'accept-language': 'fr,fr-FR;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
                                    'cache-control': 'max-age=0',
                                    'cookie': cookie,
                                    'dnt': '1',
                                    'sec-fetch-dest': 'document',
                                    'sec-fetch-mode': 'navigate',
                                    'sec-fetch-site': 'none',
                                    'sec-fetch-user': '?1',
                                    'upgrade-insecure-requests': '1',
                                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.54'
                                }

                                time.sleep(10)

                                response_url_ad = requests.get(url_ad, headers=headers_url_ad)

                                soup_url_ad = BeautifulSoup(response_url_ad.text, 'html.parser')

                                title = ""

                                try:
                                    if soup_url_ad.find("h1", {"data-qa-id": "adview_title"}) is not None:
                                        title += soup_url_ad.find("h1", {"data-qa-id": "adview_title"}).text.lower()
                                    else:
                                        print("no title")
                                except Exception as e:
                                    print("error title : " + str(e))

                                description = ""

                                try:
                                    if soup_url_ad.find("div", {"data-qa-id": "adview_description_container"}) is not None:
                                        description += soup_url_ad.find("div", {"data-qa-id": "adview_description_container"}) \
                                            .text.replace("\n", "").replace("\t", "").replace("\r", "").lower()
                                    else:
                                        print("no description")
                                except Exception as e:
                                    print("error description : " + str(e))

                                code_postal = ""

                                try:
                                    if soup_url_ad.find("li", {"data-qa-id": "breadcrumb-item-4"}) is not None:
                                        location = soup_url_ad.find("li", {"data-qa-id": "breadcrumb-item-4"}).text \
                                            .replace(" ", "") \
                                            .replace("\t", "") \
                                            .replace("\n", "") \
                                            .replace("\r", "")

                                        code_postal += location[len(location) - 5:]
                                    else:
                                        print("no location_city")
                                except Exception as e:
                                    print("error location_city : " + str(e))

                                try:
                                    response = requests.request("GET", "https://geo.api.gouv.fr/communes?codePostal=" + code_postal)

                                    code_insee_commune = json.loads(response.text)[0]['code']

                                    population = json.loads(response.text)[0]['population']

                                    print(str(i_1) + " : " + url_ad + " / " + str(code_postal)
                                          + " / population : " + str(population))

                                    if code_insee_commune in array_code_insee_commune_train_station_travellers\
                                            and\
                                            code_insee_commune in array_code_insee_commune_desservies_par_gaz\
                                            and\
                                            ("box" not in description
                                             or "loisir" not in description
                                             or "cave" not in description
                                             or "recherche" not in description
                                             or "véranda" not in description
                                             or "bateau" not in description
                                             or "péniche" not in description
                                             or "parking" not in description
                                             or "chalet" not in description
                                             or "châlet" not in description
                                             or "peintre" not in description
                                             or "jardin" not in description
                                             or "maisonnette" not in description
                                             or "accession" not in description
                                             or "bureau" not in description
                                             or "bungalow" not in description
                                             or "mobile" not in description
                                             or "étagère" not in description
                                             or "terrain" not in description
                                             or "forêt" not in description
                                             or "enchère" not in description
                                             or "viager" not in description
                                             or "enchere" not in description)\
                                            and\
                                            ("box" not in title
                                             or "loisir" not in title
                                             or "cave" not in title
                                             or "recherche" not in title
                                             or "véranda" not in title
                                             or "bateau" not in title
                                             or "péniche" not in title
                                             or "parking" not in title
                                             or "chalet" not in title
                                             or "châlet" not in title
                                             or "peintre" not in title
                                             or "jardin" not in title
                                             or "maisonnette" not in title
                                             or "accession" not in title
                                             or "bureau" not in title
                                             or "bungalow" not in title
                                             or "mobile" not in title
                                             or "étagère" not in title
                                             or "terrain" not in title
                                             or "forêt" not in title
                                             or "enchère" not in title
                                             or "viager" not in title
                                             or "enchere" not in title):
                                        print(str(i_1) + " url_ad : " + url_ad + " good")

                                        try:
                                            connection = pymysql.connect(
                                                host='localhost',
                                                port=3306,
                                                user='root',
                                                password='8h0NEJkEf3lyCBUoPQwCHSu@@@@@@@',
                                                db='contacts_professionnels',
                                                charset='utf8mb4',
                                                cursorclass=pymysql.cursors.DictCursor
                                            )

                                            with connection.cursor() as cursor:
                                                try:
                                                    sql = "insert into annonces_immobilieres_maisons " \
                                                          "(url_ad_maison, code_postal, population) value (%s, %s, %s)"

                                                    cursor.execute(sql, (url_ad, code_postal, population))

                                                    connection.commit()

                                                    connection.close()
                                                except Exception as e:
                                                    print("The record already exists : " + str(e))
                                                    connection.close()
                                        except Exception as e:
                                            print('There is a problem : ' + str(e))
                                    else:
                                        print(str(i_1) + " : bad")
                                except Exception as e:
                                    print(str(i_1) + " : error location code postal : " + str(e))
                            except Exception as e:
                                print(str(i_1) + " : error request url_ad : " + str(e))
                    else:
                        print("no a data-qa-id aditem_container")
            except Exception as e:
                print("error for : " + str(e))
        except Exception as e:
            print("error request url_ad : " + str(e))


if __name__ == '__main__':
    unittest.main()
