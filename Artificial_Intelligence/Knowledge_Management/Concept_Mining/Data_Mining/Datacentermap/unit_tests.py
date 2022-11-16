import time
import unittest
import requests
from bs4 import BeautifulSoup
import xlsxwriter


class UnitTestsDataMiningDatacentermap(unittest.TestCase):
    def test_extract_one_contact_from_one_country_and_one_city(self):
        print('test_extract_one_contact_from_one_country_and_one_city')

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        time.sleep(3)

        url = "https://www.datacentermap.com/france/paris/"

        html = requests.get(url, headers=headers)

        soup = BeautifulSoup(html.content, 'html.parser')

        if soup.find("div", {'class': 'DCColumn1'}) is not None:
            contacts = soup.find_all("div", {'class': 'DCColumn1'})

            for contact in contacts:
                print(
                    "contact : " + contact.text
                    .replace('Visit website', '')
                    .replace('»', '')
                    .replace('View profile', '')
                    .replace('	', '')
                )
        else:
            print("no contact")

    def test_extract_urls_city_from_one_country(self):
        print("test_extract_urls_city_from_one_country")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        time.sleep(3)

        url = "https://www.datacentermap.com/france/"

        html = requests.get(url, headers=headers)

        soup = BeautifulSoup(html.content, 'html.parser')

        if soup.find("div", {'class': 'column1'}) is not None:
            all_a = soup.find("div", {'class': 'column1'}).find_all('a')

            for a in all_a:
                print(
                    "url : https://www.datacentermap.com" + a.get('href')
                )

        if soup.find("div", {'class': 'column2'}) is not None:
            all_a = soup.find("div", {'class': 'column2'}).find_all('a')

            for a in all_a:
                print(
                    "url : https://www.datacentermap.com" + a.get('href')
                )

        if soup.find("div", {'class': 'column3'}) is not None:
            all_a = soup.find("div", {'class': 'column3'}).find_all('a')

            for a in all_a:
                print(
                    "url : https://www.datacentermap.com" + a.get('href')
                )

    def test_extract_urls_countries_from_the_main_page(self):
        print("test_extract_urls_countries_from_the_main_page")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        time.sleep(3)

        url = "https://www.datacentermap.com/datacenters.html"

        html = requests.get(url, headers=headers)

        soup = BeautifulSoup(html.content, 'html.parser')

        if soup.find("div", {'class': 'column1'}) is not None:
            all_a = soup.find("div", {'class': 'column1'}).find_all('a')

            for a in all_a:
                print(
                    "url : https://www.datacentermap.com" + a.get('href')
                )

        if soup.find("div", {'class': 'column2'}) is not None:
            all_a = soup.find("div", {'class': 'column2'}).find_all('a')

            for a in all_a:
                print(
                    "url : https://www.datacentermap.com" + a.get('href')
                )

        if soup.find("div", {'class': 'column3'}) is not None:
            all_a = soup.find("div", {'class': 'column3'}).find_all('a')

            for a in all_a:
                print(
                    "url : https://www.datacentermap.com" + a.get('href')
                )

    def test_extract_one_contact_from_all_countries_into_excel(self):
        print("test_extract_one_contact_from_all_countries")

        filename = "Worldwide_contacts_data_centers.xlsx"

        workbook = xlsxwriter.Workbook(filename)

        worksheet = workbook.add_worksheet('data')

        cell_format_yellow = workbook.add_format(
            {
                'bg_color': 'yellow',
                'border': 1,
                'align': 'justify',
                'valign': 'top'
            }
        )

        worksheet.write(0, 0, 'company_name', cell_format_yellow)
        worksheet.write(0, 1, 'postal_address', cell_format_yellow)
        worksheet.write(0, 2, 'phone_number', cell_format_yellow)
        worksheet.write(0, 3, 'website', cell_format_yellow)
        worksheet.write(0, 4, 'email', cell_format_yellow)
        worksheet.write(0, 5, 'region', cell_format_yellow)
        worksheet.write(0, 6, 'activity', cell_format_yellow)
        worksheet.write(0, 7, 'country', cell_format_yellow)
        worksheet.write(0, 8, 'notes', cell_format_yellow)

        cell_format_orange = workbook.add_format(
            {
                'bg_color': 'orange',
                'border': 1,
                'align': 'justify',
                'valign': 'top'
            }
        )

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        time.sleep(3)

        url = "https://www.datacentermap.com/datacenters.html"

        html = requests.get(url, headers=headers)

        soup_main_page = BeautifulSoup(html.content, 'html.parser')

        i = 1

        if soup_main_page.find("div", {'class': 'column1'}) is not None:
            all_a = soup_main_page.find("div", {'class': 'column1'}).find_all('a')

            for a in all_a:
                print(
                    "url : https://www.datacentermap.com" + a.get('href')
                )

                headers = {
                    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
                }

                time.sleep(3)

                url = "https://www.datacentermap.com" + a.get('href')

                html = requests.get(url, headers=headers)

                soup_all_country = BeautifulSoup(html.content, 'html.parser')

                if soup_all_country.find("div", {'class': 'column1'}) is not None:
                    all_a = soup_all_country.find("div", {'class': 'column1'}).find_all('a')

                    for a in all_a:
                        print(
                            "url : https://www.datacentermap.com" + a.get('href')
                        )

                        country = a.get('href')

                        url = "https://www.datacentermap.com" + a.get('href')

                        html = requests.get(url, headers=headers)

                        soup_city = BeautifulSoup(html.content, 'html.parser')

                        if soup_city.find("div", {'class': 'column1'}) is not None:
                            all_a = soup_city.find("div", {'class': 'column1'}).find_all('a')

                            for a in all_a:
                                print(
                                    "url : https://www.datacentermap.com" + a.get('href')
                                )

                                city = a.get('href')

                                url = "https://www.datacentermap.com" + a.get('href')

                                html = requests.get(url, headers=headers)

                                soup_contact = BeautifulSoup(html.content, 'html.parser')

                                if soup_contact.find("div", {'class': 'DCColumn1'}) is not None:
                                    contacts = soup_contact.find_all("div", {'class': 'DCColumn1'})

                                    for contact in contacts:
                                        print(
                                            "contact : " + contact.text
                                            .replace('Visit website', '')
                                            .replace('»', '')
                                            .replace('View profile', '')
                                            .replace('	', '')
                                        )

                                        contact_company = contact.text\
                                            .replace('Visit website', '')\
                                            .replace('»', '')\
                                            .replace('View profile', '')\
                                            .replace('	', '')

                                        worksheet.write(i, 0, contact_company, cell_format_orange)
                                        worksheet.write(i, 1, '', cell_format_orange)
                                        worksheet.write(i, 2, '', cell_format_orange)
                                        worksheet.write(i, 3, '', cell_format_orange)
                                        worksheet.write(i, 4, '', cell_format_orange)
                                        worksheet.write(i, 5, city, cell_format_orange)
                                        worksheet.write(i, 6, 'data center', cell_format_orange)
                                        worksheet.write(i, 7, country, cell_format_orange)
                                        worksheet.write(i, 8, '', cell_format_orange)

                                        i += 1
                                else:
                                    print("no contact")

                        if soup_city.find("div", {'class': 'column2'}) is not None:
                            all_a = soup_city.find("div", {'class': 'column2'}).find_all('a')

                            for a in all_a:
                                print(
                                    "url : https://www.datacentermap.com" + a.get('href')
                                )

                                city = a.get('href')

                                url = "https://www.datacentermap.com" + a.get('href')

                                html = requests.get(url, headers=headers)

                                soup_contact = BeautifulSoup(html.content, 'html.parser')

                                if soup_contact.find("div", {'class': 'DCColumn1'}) is not None:
                                    contacts = soup_contact.find_all("div", {'class': 'DCColumn1'})

                                    for contact in contacts:
                                        print(
                                            "contact : " + contact.text
                                            .replace('Visit website', '')
                                            .replace('»', '')
                                            .replace('View profile', '')
                                            .replace('	', '')
                                        )

                                        contact_company = contact.text\
                                            .replace('Visit website', '')\
                                            .replace('»', '')\
                                            .replace('View profile', '')\
                                            .replace('	', '')

                                        worksheet.write(i, 0, contact_company, cell_format_orange)
                                        worksheet.write(i, 1, '', cell_format_orange)
                                        worksheet.write(i, 2, '', cell_format_orange)
                                        worksheet.write(i, 3, '', cell_format_orange)
                                        worksheet.write(i, 4, '', cell_format_orange)
                                        worksheet.write(i, 5, city, cell_format_orange)
                                        worksheet.write(i, 6, 'data center', cell_format_orange)
                                        worksheet.write(i, 7, country, cell_format_orange)
                                        worksheet.write(i, 8, '', cell_format_orange)

                                        i += 1
                                else:
                                    print("no contact")

                        if soup_city.find("div", {'class': 'column3'}) is not None:
                            all_a = soup_city.find("div", {'class': 'column3'}).find_all('a')

                            for a in all_a:
                                print(
                                    "url : https://www.datacentermap.com" + a.get('href')
                                )

                                city = a.get('href')

                                url = "https://www.datacentermap.com" + a.get('href')

                                html = requests.get(url, headers=headers)

                                soup_contact = BeautifulSoup(html.content, 'html.parser')

                                if soup_contact.find("div", {'class': 'DCColumn1'}) is not None:
                                    contacts = soup_contact.find_all("div", {'class': 'DCColumn1'})

                                    for contact in contacts:
                                        print(
                                            "contact : " + contact.text
                                            .replace('Visit website', '')
                                            .replace('»', '')
                                            .replace('View profile', '')
                                            .replace('	', '')
                                        )

                                        contact_company = contact.text\
                                            .replace('Visit website', '')\
                                            .replace('»', '')\
                                            .replace('View profile', '')\
                                            .replace('	', '')

                                        worksheet.write(i, 0, contact_company, cell_format_orange)
                                        worksheet.write(i, 1, '', cell_format_orange)
                                        worksheet.write(i, 2, '', cell_format_orange)
                                        worksheet.write(i, 3, '', cell_format_orange)
                                        worksheet.write(i, 4, '', cell_format_orange)
                                        worksheet.write(i, 5, city, cell_format_orange)
                                        worksheet.write(i, 6, 'data center', cell_format_orange)
                                        worksheet.write(i, 7, country, cell_format_orange)
                                        worksheet.write(i, 8, '', cell_format_orange)

                                        i += 1
                                else:
                                    print("no contact")

                if soup_all_country.find("div", {'class': 'column2'}) is not None:
                    all_a = soup_all_country.find("div", {'class': 'column2'}).find_all('a')

                    for a in all_a:
                        print(
                            "url : https://www.datacentermap.com" + a.get('href')
                        )

                        country = a.get('href')

                        url = "https://www.datacentermap.com" + a.get('href')

                        html = requests.get(url, headers=headers)

                        soup_city = BeautifulSoup(html.content, 'html.parser')

                        if soup_city.find("div", {'class': 'column1'}) is not None:
                            all_a = soup_city.find("div", {'class': 'column1'}).find_all('a')

                            for a in all_a:
                                print(
                                    "url : https://www.datacentermap.com" + a.get('href')
                                )

                                city = a.get('href')

                                url = "https://www.datacentermap.com" + a.get('href')

                                html = requests.get(url, headers=headers)

                                soup_contact = BeautifulSoup(html.content, 'html.parser')

                                if soup_contact.find("div", {'class': 'DCColumn1'}) is not None:
                                    contacts = soup_contact.find_all("div", {'class': 'DCColumn1'})

                                    for contact in contacts:
                                        print(
                                            "contact : " + contact.text
                                            .replace('Visit website', '')
                                            .replace('»', '')
                                            .replace('View profile', '')
                                            .replace('	', '')
                                        )

                                        contact_company = contact.text\
                                            .replace('Visit website', '')\
                                            .replace('»', '')\
                                            .replace('View profile', '')\
                                            .replace('	', '')

                                        worksheet.write(i, 0, contact_company, cell_format_orange)
                                        worksheet.write(i, 1, '', cell_format_orange)
                                        worksheet.write(i, 2, '', cell_format_orange)
                                        worksheet.write(i, 3, '', cell_format_orange)
                                        worksheet.write(i, 4, '', cell_format_orange)
                                        worksheet.write(i, 5, city, cell_format_orange)
                                        worksheet.write(i, 6, 'data center', cell_format_orange)
                                        worksheet.write(i, 7, country, cell_format_orange)
                                        worksheet.write(i, 8, '', cell_format_orange)

                                        i += 1
                                else:
                                    print("no contact")

                        if soup_city.find("div", {'class': 'column2'}) is not None:
                            all_a = soup_city.find("div", {'class': 'column2'}).find_all('a')

                            for a in all_a:
                                print(
                                    "url : https://www.datacentermap.com" + a.get('href')
                                )

                                city = a.get('href')

                                url = "https://www.datacentermap.com" + a.get('href')

                                html = requests.get(url, headers=headers)

                                soup_contact = BeautifulSoup(html.content, 'html.parser')

                                if soup_contact.find("div", {'class': 'DCColumn1'}) is not None:
                                    contacts = soup_contact.find_all("div", {'class': 'DCColumn1'})

                                    for contact in contacts:
                                        print(
                                            "contact : " + contact.text
                                            .replace('Visit website', '')
                                            .replace('»', '')
                                            .replace('View profile', '')
                                            .replace('	', '')
                                        )

                                        contact_company = contact.text\
                                            .replace('Visit website', '')\
                                            .replace('»', '')\
                                            .replace('View profile', '')\
                                            .replace('	', '')

                                        worksheet.write(i, 0, contact_company, cell_format_orange)
                                        worksheet.write(i, 1, '', cell_format_orange)
                                        worksheet.write(i, 2, '', cell_format_orange)
                                        worksheet.write(i, 3, '', cell_format_orange)
                                        worksheet.write(i, 4, '', cell_format_orange)
                                        worksheet.write(i, 5, city, cell_format_orange)
                                        worksheet.write(i, 6, 'data center', cell_format_orange)
                                        worksheet.write(i, 7, country, cell_format_orange)
                                        worksheet.write(i, 8, '', cell_format_orange)

                                        i += 1
                                else:
                                    print("no contact")

                        if soup_city.find("div", {'class': 'column3'}) is not None:
                            all_a = soup_city.find("div", {'class': 'column3'}).find_all('a')

                            for a in all_a:
                                print(
                                    "url : https://www.datacentermap.com" + a.get('href')
                                )

                                city = a.get('href')

                                url = "https://www.datacentermap.com" + a.get('href')

                                html = requests.get(url, headers=headers)

                                soup_contact = BeautifulSoup(html.content, 'html.parser')

                                if soup_contact.find("div", {'class': 'DCColumn1'}) is not None:
                                    contacts = soup_contact.find_all("div", {'class': 'DCColumn1'})

                                    for contact in contacts:
                                        print(
                                            "contact : " + contact.text
                                            .replace('Visit website', '')
                                            .replace('»', '')
                                            .replace('View profile', '')
                                            .replace('	', '')
                                        )

                                        contact_company = contact.text\
                                            .replace('Visit website', '')\
                                            .replace('»', '')\
                                            .replace('View profile', '')\
                                            .replace('	', '')

                                        worksheet.write(i, 0, contact_company, cell_format_orange)
                                        worksheet.write(i, 1, '', cell_format_orange)
                                        worksheet.write(i, 2, '', cell_format_orange)
                                        worksheet.write(i, 3, '', cell_format_orange)
                                        worksheet.write(i, 4, '', cell_format_orange)
                                        worksheet.write(i, 5, city, cell_format_orange)
                                        worksheet.write(i, 6, 'data center', cell_format_orange)
                                        worksheet.write(i, 7, country, cell_format_orange)
                                        worksheet.write(i, 8, '', cell_format_orange)

                                        i += 1
                                else:
                                    print("no contact")

                if soup_all_country.find("div", {'class': 'column3'}) is not None:
                    all_a = soup_all_country.find("div", {'class': 'column3'}).find_all('a')

                    for a in all_a:
                        print(
                            "url : https://www.datacentermap.com" + a.get('href')
                        )

                        country = a.get('href')

                        url = "https://www.datacentermap.com" + a.get('href')

                        html = requests.get(url, headers=headers)

                        soup_city = BeautifulSoup(html.content, 'html.parser')

                        if soup_city.find("div", {'class': 'column1'}) is not None:
                            all_a = soup_city.find("div", {'class': 'column1'}).find_all('a')

                            for a in all_a:
                                print(
                                    "url : https://www.datacentermap.com" + a.get('href')
                                )

                                city = a.get('href')

                                url = "https://www.datacentermap.com" + a.get('href')

                                html = requests.get(url, headers=headers)

                                soup_contact = BeautifulSoup(html.content, 'html.parser')

                                if soup_contact.find("div", {'class': 'DCColumn1'}) is not None:
                                    contacts = soup_contact.find_all("div", {'class': 'DCColumn1'})

                                    for contact in contacts:
                                        print(
                                            "contact : " + contact.text
                                            .replace('Visit website', '')
                                            .replace('»', '')
                                            .replace('View profile', '')
                                            .replace('	', '')
                                        )

                                        contact_company = contact.text\
                                            .replace('Visit website', '')\
                                            .replace('»', '')\
                                            .replace('View profile', '')\
                                            .replace('	', '')

                                        worksheet.write(i, 0, contact_company, cell_format_orange)
                                        worksheet.write(i, 1, '', cell_format_orange)
                                        worksheet.write(i, 2, '', cell_format_orange)
                                        worksheet.write(i, 3, '', cell_format_orange)
                                        worksheet.write(i, 4, '', cell_format_orange)
                                        worksheet.write(i, 5, city, cell_format_orange)
                                        worksheet.write(i, 6, 'data center', cell_format_orange)
                                        worksheet.write(i, 7, country, cell_format_orange)
                                        worksheet.write(i, 8, '', cell_format_orange)

                                        i += 1
                                else:
                                    print("no contact")

                        if soup_city.find("div", {'class': 'column2'}) is not None:
                            all_a = soup_city.find("div", {'class': 'column2'}).find_all('a')

                            for a in all_a:
                                print(
                                    "url : https://www.datacentermap.com" + a.get('href')
                                )

                                city = a.get('href')

                                url = "https://www.datacentermap.com" + a.get('href')

                                html = requests.get(url, headers=headers)

                                soup_contact = BeautifulSoup(html.content, 'html.parser')

                                if soup_contact.find("div", {'class': 'DCColumn1'}) is not None:
                                    contacts = soup_contact.find_all("div", {'class': 'DCColumn1'})

                                    for contact in contacts:
                                        print(
                                            "contact : " + contact.text
                                            .replace('Visit website', '')
                                            .replace('»', '')
                                            .replace('View profile', '')
                                            .replace('	', '')
                                        )

                                        contact_company = contact.text\
                                            .replace('Visit website', '')\
                                            .replace('»', '')\
                                            .replace('View profile', '')\
                                            .replace('	', '')

                                        worksheet.write(i, 0, contact_company, cell_format_orange)
                                        worksheet.write(i, 1, '', cell_format_orange)
                                        worksheet.write(i, 2, '', cell_format_orange)
                                        worksheet.write(i, 3, '', cell_format_orange)
                                        worksheet.write(i, 4, '', cell_format_orange)
                                        worksheet.write(i, 5, city, cell_format_orange)
                                        worksheet.write(i, 6, 'data center', cell_format_orange)
                                        worksheet.write(i, 7, country, cell_format_orange)
                                        worksheet.write(i, 8, '', cell_format_orange)

                                        i += 1
                                else:
                                    print("no contact")

                        if soup_city.find("div", {'class': 'column3'}) is not None:
                            all_a = soup_city.find("div", {'class': 'column3'}).find_all('a')

                            for a in all_a:
                                print(
                                    "url : https://www.datacentermap.com" + a.get('href')
                                )

                                city = a.get('href')

                                url = "https://www.datacentermap.com" + a.get('href')

                                html = requests.get(url, headers=headers)

                                soup_contact = BeautifulSoup(html.content, 'html.parser')

                                if soup_contact.find("div", {'class': 'DCColumn1'}) is not None:
                                    contacts = soup_contact.find_all("div", {'class': 'DCColumn1'})

                                    for contact in contacts:
                                        print(
                                            "contact : " + contact.text
                                            .replace('Visit website', '')
                                            .replace('»', '')
                                            .replace('View profile', '')
                                            .replace('	', '')
                                        )

                                        contact_company = contact.text\
                                            .replace('Visit website', '')\
                                            .replace('»', '')\
                                            .replace('View profile', '')\
                                            .replace('	', '')

                                        worksheet.write(i, 0, contact_company, cell_format_orange)
                                        worksheet.write(i, 1, '', cell_format_orange)
                                        worksheet.write(i, 2, '', cell_format_orange)
                                        worksheet.write(i, 3, '', cell_format_orange)
                                        worksheet.write(i, 4, '', cell_format_orange)
                                        worksheet.write(i, 5, city, cell_format_orange)
                                        worksheet.write(i, 6, 'data center', cell_format_orange)
                                        worksheet.write(i, 7, country, cell_format_orange)
                                        worksheet.write(i, 8, '', cell_format_orange)

                                        i += 1
                                else:
                                    print("no contact")

        if soup_main_page.find("div", {'class': 'column2'}) is not None:
            all_a = soup_main_page.find("div", {'class': 'column2'}).find_all('a')

            for a in all_a:
                print(
                    "url : https://www.datacentermap.com" + a.get('href')
                )

                headers = {
                    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
                }

                time.sleep(3)

                url = "https://www.datacentermap.com" + a.get('href')

                html = requests.get(url, headers=headers)

                soup_all_country = BeautifulSoup(html.content, 'html.parser')

                if soup_all_country.find("div", {'class': 'column1'}) is not None:
                    all_a = soup_all_country.find("div", {'class': 'column1'}).find_all('a')

                    for a in all_a:
                        print(
                            "url : https://www.datacentermap.com" + a.get('href')
                        )

                        country = a.get('href')

                        url = "https://www.datacentermap.com" + a.get('href')

                        html = requests.get(url, headers=headers)

                        soup_city = BeautifulSoup(html.content, 'html.parser')

                        if soup_city.find("div", {'class': 'column1'}) is not None:
                            all_a = soup_city.find("div", {'class': 'column1'}).find_all('a')

                            for a in all_a:
                                print(
                                    "url : https://www.datacentermap.com" + a.get('href')
                                )

                                city = a.get('href')

                                url = "https://www.datacentermap.com" + a.get('href')

                                html = requests.get(url, headers=headers)

                                soup_contact = BeautifulSoup(html.content, 'html.parser')

                                if soup_contact.find("div", {'class': 'DCColumn1'}) is not None:
                                    contacts = soup_contact.find_all("div", {'class': 'DCColumn1'})

                                    for contact in contacts:
                                        print(
                                            "contact : " + contact.text
                                            .replace('Visit website', '')
                                            .replace('»', '')
                                            .replace('View profile', '')
                                            .replace('	', '')
                                        )

                                        contact_company = contact.text\
                                            .replace('Visit website', '')\
                                            .replace('»', '')\
                                            .replace('View profile', '')\
                                            .replace('	', '')

                                        worksheet.write(i, 0, contact_company, cell_format_orange)
                                        worksheet.write(i, 1, '', cell_format_orange)
                                        worksheet.write(i, 2, '', cell_format_orange)
                                        worksheet.write(i, 3, '', cell_format_orange)
                                        worksheet.write(i, 4, '', cell_format_orange)
                                        worksheet.write(i, 5, city, cell_format_orange)
                                        worksheet.write(i, 6, 'data center', cell_format_orange)
                                        worksheet.write(i, 7, country, cell_format_orange)
                                        worksheet.write(i, 8, '', cell_format_orange)

                                        i += 1
                                else:
                                    print("no contact")

                        if soup_city.find("div", {'class': 'column2'}) is not None:
                            all_a = soup_city.find("div", {'class': 'column2'}).find_all('a')

                            for a in all_a:
                                print(
                                    "url : https://www.datacentermap.com" + a.get('href')
                                )

                                city = a.get('href')

                                url = "https://www.datacentermap.com" + a.get('href')

                                html = requests.get(url, headers=headers)

                                soup_contact = BeautifulSoup(html.content, 'html.parser')

                                if soup_contact.find("div", {'class': 'DCColumn1'}) is not None:
                                    contacts = soup_contact.find_all("div", {'class': 'DCColumn1'})

                                    for contact in contacts:
                                        print(
                                            "contact : " + contact.text
                                            .replace('Visit website', '')
                                            .replace('»', '')
                                            .replace('View profile', '')
                                            .replace('	', '')
                                        )

                                        contact_company = contact.text\
                                            .replace('Visit website', '')\
                                            .replace('»', '')\
                                            .replace('View profile', '')\
                                            .replace('	', '')

                                        worksheet.write(i, 0, contact_company, cell_format_orange)
                                        worksheet.write(i, 1, '', cell_format_orange)
                                        worksheet.write(i, 2, '', cell_format_orange)
                                        worksheet.write(i, 3, '', cell_format_orange)
                                        worksheet.write(i, 4, '', cell_format_orange)
                                        worksheet.write(i, 5, city, cell_format_orange)
                                        worksheet.write(i, 6, 'data center', cell_format_orange)
                                        worksheet.write(i, 7, country, cell_format_orange)
                                        worksheet.write(i, 8, '', cell_format_orange)

                                        i += 1
                                else:
                                    print("no contact")

                        if soup_city.find("div", {'class': 'column3'}) is not None:
                            all_a = soup_city.find("div", {'class': 'column3'}).find_all('a')

                            for a in all_a:
                                print(
                                    "url : https://www.datacentermap.com" + a.get('href')
                                )

                                city = a.get('href')

                                url = "https://www.datacentermap.com" + a.get('href')

                                html = requests.get(url, headers=headers)

                                soup_contact = BeautifulSoup(html.content, 'html.parser')

                                if soup_contact.find("div", {'class': 'DCColumn1'}) is not None:
                                    contacts = soup_contact.find_all("div", {'class': 'DCColumn1'})

                                    for contact in contacts:
                                        print(
                                            "contact : " + contact.text
                                            .replace('Visit website', '')
                                            .replace('»', '')
                                            .replace('View profile', '')
                                            .replace('	', '')
                                        )

                                        contact_company = contact.text\
                                            .replace('Visit website', '')\
                                            .replace('»', '')\
                                            .replace('View profile', '')\
                                            .replace('	', '')

                                        worksheet.write(i, 0, contact_company, cell_format_orange)
                                        worksheet.write(i, 1, '', cell_format_orange)
                                        worksheet.write(i, 2, '', cell_format_orange)
                                        worksheet.write(i, 3, '', cell_format_orange)
                                        worksheet.write(i, 4, '', cell_format_orange)
                                        worksheet.write(i, 5, city, cell_format_orange)
                                        worksheet.write(i, 6, 'data center', cell_format_orange)
                                        worksheet.write(i, 7, country, cell_format_orange)
                                        worksheet.write(i, 8, '', cell_format_orange)

                                        i += 1
                                else:
                                    print("no contact")

                if soup_all_country.find("div", {'class': 'column2'}) is not None:
                    all_a = soup_all_country.find("div", {'class': 'column2'}).find_all('a')

                    for a in all_a:
                        print(
                            "url : https://www.datacentermap.com" + a.get('href')
                        )

                        country = a.get('href')

                        url = "https://www.datacentermap.com" + a.get('href')

                        html = requests.get(url, headers=headers)

                        soup_city = BeautifulSoup(html.content, 'html.parser')

                        if soup_city.find("div", {'class': 'column1'}) is not None:
                            all_a = soup_city.find("div", {'class': 'column1'}).find_all('a')

                            for a in all_a:
                                print(
                                    "url : https://www.datacentermap.com" + a.get('href')
                                )

                                city = a.get('href')

                                url = "https://www.datacentermap.com" + a.get('href')

                                html = requests.get(url, headers=headers)

                                soup_contact = BeautifulSoup(html.content, 'html.parser')

                                if soup_contact.find("div", {'class': 'DCColumn1'}) is not None:
                                    contacts = soup_contact.find_all("div", {'class': 'DCColumn1'})

                                    for contact in contacts:
                                        print(
                                            "contact : " + contact.text
                                            .replace('Visit website', '')
                                            .replace('»', '')
                                            .replace('View profile', '')
                                            .replace('	', '')
                                        )

                                        contact_company = contact.text\
                                            .replace('Visit website', '')\
                                            .replace('»', '')\
                                            .replace('View profile', '')\
                                            .replace('	', '')

                                        worksheet.write(i, 0, contact_company, cell_format_orange)
                                        worksheet.write(i, 1, '', cell_format_orange)
                                        worksheet.write(i, 2, '', cell_format_orange)
                                        worksheet.write(i, 3, '', cell_format_orange)
                                        worksheet.write(i, 4, '', cell_format_orange)
                                        worksheet.write(i, 5, city, cell_format_orange)
                                        worksheet.write(i, 6, 'data center', cell_format_orange)
                                        worksheet.write(i, 7, country, cell_format_orange)
                                        worksheet.write(i, 8, '', cell_format_orange)

                                        i += 1
                                else:
                                    print("no contact")

                        if soup_city.find("div", {'class': 'column2'}) is not None:
                            all_a = soup_city.find("div", {'class': 'column2'}).find_all('a')

                            for a in all_a:
                                print(
                                    "url : https://www.datacentermap.com" + a.get('href')
                                )

                                city = a.get('href')

                                url = "https://www.datacentermap.com" + a.get('href')

                                html = requests.get(url, headers=headers)

                                soup_contact = BeautifulSoup(html.content, 'html.parser')

                                if soup_contact.find("div", {'class': 'DCColumn1'}) is not None:
                                    contacts = soup_contact.find_all("div", {'class': 'DCColumn1'})

                                    for contact in contacts:
                                        print(
                                            "contact : " + contact.text
                                            .replace('Visit website', '')
                                            .replace('»', '')
                                            .replace('View profile', '')
                                            .replace('	', '')
                                        )

                                        contact_company = contact.text\
                                            .replace('Visit website', '')\
                                            .replace('»', '')\
                                            .replace('View profile', '')\
                                            .replace('	', '')

                                        worksheet.write(i, 0, contact_company, cell_format_orange)
                                        worksheet.write(i, 1, '', cell_format_orange)
                                        worksheet.write(i, 2, '', cell_format_orange)
                                        worksheet.write(i, 3, '', cell_format_orange)
                                        worksheet.write(i, 4, '', cell_format_orange)
                                        worksheet.write(i, 5, city, cell_format_orange)
                                        worksheet.write(i, 6, 'data center', cell_format_orange)
                                        worksheet.write(i, 7, country, cell_format_orange)
                                        worksheet.write(i, 8, '', cell_format_orange)

                                        i += 1
                                else:
                                    print("no contact")

                        if soup_city.find("div", {'class': 'column3'}) is not None:
                            all_a = soup_city.find("div", {'class': 'column3'}).find_all('a')

                            for a in all_a:
                                print(
                                    "url : https://www.datacentermap.com" + a.get('href')
                                )

                                city = a.get('href')

                                url = "https://www.datacentermap.com" + a.get('href')

                                html = requests.get(url, headers=headers)

                                soup_contact = BeautifulSoup(html.content, 'html.parser')

                                if soup_contact.find("div", {'class': 'DCColumn1'}) is not None:
                                    contacts = soup_contact.find_all("div", {'class': 'DCColumn1'})

                                    for contact in contacts:
                                        print(
                                            "contact : " + contact.text
                                            .replace('Visit website', '')
                                            .replace('»', '')
                                            .replace('View profile', '')
                                            .replace('	', '')
                                        )

                                        contact_company = contact.text\
                                            .replace('Visit website', '')\
                                            .replace('»', '')\
                                            .replace('View profile', '')\
                                            .replace('	', '')

                                        worksheet.write(i, 0, contact_company, cell_format_orange)
                                        worksheet.write(i, 1, '', cell_format_orange)
                                        worksheet.write(i, 2, '', cell_format_orange)
                                        worksheet.write(i, 3, '', cell_format_orange)
                                        worksheet.write(i, 4, '', cell_format_orange)
                                        worksheet.write(i, 5, city, cell_format_orange)
                                        worksheet.write(i, 6, 'data center', cell_format_orange)
                                        worksheet.write(i, 7, country, cell_format_orange)
                                        worksheet.write(i, 8, '', cell_format_orange)

                                        i += 1
                                else:
                                    print("no contact")

                if soup_all_country.find("div", {'class': 'column3'}) is not None:
                    all_a = soup_all_country.find("div", {'class': 'column3'}).find_all('a')

                    for a in all_a:
                        print(
                            "url : https://www.datacentermap.com" + a.get('href')
                        )

                        country = a.get('href')

                        url = "https://www.datacentermap.com" + a.get('href')

                        html = requests.get(url, headers=headers)

                        soup_city = BeautifulSoup(html.content, 'html.parser')

                        if soup_city.find("div", {'class': 'column1'}) is not None:
                            all_a = soup_city.find("div", {'class': 'column1'}).find_all('a')

                            for a in all_a:
                                print(
                                    "url : https://www.datacentermap.com" + a.get('href')
                                )

                                city = a.get('href')

                                url = "https://www.datacentermap.com" + a.get('href')

                                html = requests.get(url, headers=headers)

                                soup_contact = BeautifulSoup(html.content, 'html.parser')

                                if soup_contact.find("div", {'class': 'DCColumn1'}) is not None:
                                    contacts = soup_contact.find_all("div", {'class': 'DCColumn1'})

                                    for contact in contacts:
                                        print(
                                            "contact : " + contact.text
                                            .replace('Visit website', '')
                                            .replace('»', '')
                                            .replace('View profile', '')
                                            .replace('	', '')
                                        )

                                        contact_company = contact.text\
                                            .replace('Visit website', '')\
                                            .replace('»', '')\
                                            .replace('View profile', '')\
                                            .replace('	', '')

                                        worksheet.write(i, 0, contact_company, cell_format_orange)
                                        worksheet.write(i, 1, '', cell_format_orange)
                                        worksheet.write(i, 2, '', cell_format_orange)
                                        worksheet.write(i, 3, '', cell_format_orange)
                                        worksheet.write(i, 4, '', cell_format_orange)
                                        worksheet.write(i, 5, city, cell_format_orange)
                                        worksheet.write(i, 6, 'data center', cell_format_orange)
                                        worksheet.write(i, 7, country, cell_format_orange)
                                        worksheet.write(i, 8, '', cell_format_orange)

                                        i += 1
                                else:
                                    print("no contact")

                        if soup_city.find("div", {'class': 'column2'}) is not None:
                            all_a = soup_city.find("div", {'class': 'column2'}).find_all('a')

                            for a in all_a:
                                print(
                                    "url : https://www.datacentermap.com" + a.get('href')
                                )

                                city = a.get('href')

                                url = "https://www.datacentermap.com" + a.get('href')

                                html = requests.get(url, headers=headers)

                                soup_contact = BeautifulSoup(html.content, 'html.parser')

                                if soup_contact.find("div", {'class': 'DCColumn1'}) is not None:
                                    contacts = soup_contact.find_all("div", {'class': 'DCColumn1'})

                                    for contact in contacts:
                                        print(
                                            "contact : " + contact.text
                                            .replace('Visit website', '')
                                            .replace('»', '')
                                            .replace('View profile', '')
                                            .replace('	', '')
                                        )

                                        contact_company = contact.text\
                                            .replace('Visit website', '')\
                                            .replace('»', '')\
                                            .replace('View profile', '')\
                                            .replace('	', '')

                                        worksheet.write(i, 0, contact_company, cell_format_orange)
                                        worksheet.write(i, 1, '', cell_format_orange)
                                        worksheet.write(i, 2, '', cell_format_orange)
                                        worksheet.write(i, 3, '', cell_format_orange)
                                        worksheet.write(i, 4, '', cell_format_orange)
                                        worksheet.write(i, 5, city, cell_format_orange)
                                        worksheet.write(i, 6, 'data center', cell_format_orange)
                                        worksheet.write(i, 7, country, cell_format_orange)
                                        worksheet.write(i, 8, '', cell_format_orange)

                                        i += 1
                                else:
                                    print("no contact")

                        if soup_city.find("div", {'class': 'column3'}) is not None:
                            all_a = soup_city.find("div", {'class': 'column3'}).find_all('a')

                            for a in all_a:
                                print(
                                    "url : https://www.datacentermap.com" + a.get('href')
                                )

                                city = a.get('href')

                                url = "https://www.datacentermap.com" + a.get('href')

                                html = requests.get(url, headers=headers)

                                soup_contact = BeautifulSoup(html.content, 'html.parser')

                                if soup_contact.find("div", {'class': 'DCColumn1'}) is not None:
                                    contacts = soup_contact.find_all("div", {'class': 'DCColumn1'})

                                    for contact in contacts:
                                        print(
                                            "contact : " + contact.text
                                            .replace('Visit website', '')
                                            .replace('»', '')
                                            .replace('View profile', '')
                                            .replace('	', '')
                                        )

                                        contact_company = contact.text\
                                            .replace('Visit website', '')\
                                            .replace('»', '')\
                                            .replace('View profile', '')\
                                            .replace('	', '')

                                        worksheet.write(i, 0, contact_company, cell_format_orange)
                                        worksheet.write(i, 1, '', cell_format_orange)
                                        worksheet.write(i, 2, '', cell_format_orange)
                                        worksheet.write(i, 3, '', cell_format_orange)
                                        worksheet.write(i, 4, '', cell_format_orange)
                                        worksheet.write(i, 5, city, cell_format_orange)
                                        worksheet.write(i, 6, 'data center', cell_format_orange)
                                        worksheet.write(i, 7, country, cell_format_orange)
                                        worksheet.write(i, 8, '', cell_format_orange)

                                        i += 1
                                else:
                                    print("no contact")

        if soup_main_page.find("div", {'class': 'column3'}) is not None:
            all_a = soup_main_page.find("div", {'class': 'column3'}).find_all('a')

            for a in all_a:
                print(
                    "url : https://www.datacentermap.com" + a.get('href')
                )

                headers = {
                    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
                }

                time.sleep(3)

                url = "https://www.datacentermap.com" + a.get('href')

                html = requests.get(url, headers=headers)

                soup_all_country = BeautifulSoup(html.content, 'html.parser')

                if soup_all_country.find("div", {'class': 'column1'}) is not None:
                    all_a = soup_all_country.find("div", {'class': 'column1'}).find_all('a')

                    for a in all_a:
                        print(
                            "url : https://www.datacentermap.com" + a.get('href')
                        )

                        country = a.get('href')

                        url = "https://www.datacentermap.com" + a.get('href')

                        html = requests.get(url, headers=headers)

                        soup_city = BeautifulSoup(html.content, 'html.parser')

                        if soup_city.find("div", {'class': 'column1'}) is not None:
                            all_a = soup_city.find("div", {'class': 'column1'}).find_all('a')

                            for a in all_a:
                                print(
                                    "url : https://www.datacentermap.com" + a.get('href')
                                )

                                city = a.get('href')

                                url = "https://www.datacentermap.com" + a.get('href')

                                html = requests.get(url, headers=headers)

                                soup_contact = BeautifulSoup(html.content, 'html.parser')

                                if soup_contact.find("div", {'class': 'DCColumn1'}) is not None:
                                    contacts = soup_contact.find_all("div", {'class': 'DCColumn1'})

                                    for contact in contacts:
                                        print(
                                            "contact : " + contact.text
                                            .replace('Visit website', '')
                                            .replace('»', '')
                                            .replace('View profile', '')
                                            .replace('	', '')
                                        )

                                        contact_company = contact.text\
                                            .replace('Visit website', '')\
                                            .replace('»', '')\
                                            .replace('View profile', '')\
                                            .replace('	', '')

                                        worksheet.write(i, 0, contact_company, cell_format_orange)
                                        worksheet.write(i, 1, '', cell_format_orange)
                                        worksheet.write(i, 2, '', cell_format_orange)
                                        worksheet.write(i, 3, '', cell_format_orange)
                                        worksheet.write(i, 4, '', cell_format_orange)
                                        worksheet.write(i, 5, city, cell_format_orange)
                                        worksheet.write(i, 6, 'data center', cell_format_orange)
                                        worksheet.write(i, 7, country, cell_format_orange)
                                        worksheet.write(i, 8, '', cell_format_orange)

                                        i += 1
                                else:
                                    print("no contact")

                        if soup_city.find("div", {'class': 'column2'}) is not None:
                            all_a = soup_city.find("div", {'class': 'column2'}).find_all('a')

                            for a in all_a:
                                print(
                                    "url : https://www.datacentermap.com" + a.get('href')
                                )

                                city = a.get('href')

                                url = "https://www.datacentermap.com" + a.get('href')

                                html = requests.get(url, headers=headers)

                                soup_contact = BeautifulSoup(html.content, 'html.parser')

                                if soup_contact.find("div", {'class': 'DCColumn1'}) is not None:
                                    contacts = soup_contact.find_all("div", {'class': 'DCColumn1'})

                                    for contact in contacts:
                                        print(
                                            "contact : " + contact.text
                                            .replace('Visit website', '')
                                            .replace('»', '')
                                            .replace('View profile', '')
                                            .replace('	', '')
                                        )

                                        contact_company = contact.text\
                                            .replace('Visit website', '')\
                                            .replace('»', '')\
                                            .replace('View profile', '')\
                                            .replace('	', '')

                                        worksheet.write(i, 0, contact_company, cell_format_orange)
                                        worksheet.write(i, 1, '', cell_format_orange)
                                        worksheet.write(i, 2, '', cell_format_orange)
                                        worksheet.write(i, 3, '', cell_format_orange)
                                        worksheet.write(i, 4, '', cell_format_orange)
                                        worksheet.write(i, 5, city, cell_format_orange)
                                        worksheet.write(i, 6, 'data center', cell_format_orange)
                                        worksheet.write(i, 7, country, cell_format_orange)
                                        worksheet.write(i, 8, '', cell_format_orange)

                                        i += 1
                                else:
                                    print("no contact")

                        if soup_city.find("div", {'class': 'column3'}) is not None:
                            all_a = soup_city.find("div", {'class': 'column3'}).find_all('a')

                            for a in all_a:
                                print(
                                    "url : https://www.datacentermap.com" + a.get('href')
                                )

                                city = a.get('href')

                                url = "https://www.datacentermap.com" + a.get('href')

                                html = requests.get(url, headers=headers)

                                soup_contact = BeautifulSoup(html.content, 'html.parser')

                                if soup_contact.find("div", {'class': 'DCColumn1'}) is not None:
                                    contacts = soup_contact.find_all("div", {'class': 'DCColumn1'})

                                    for contact in contacts:
                                        print(
                                            "contact : " + contact.text
                                            .replace('Visit website', '')
                                            .replace('»', '')
                                            .replace('View profile', '')
                                            .replace('	', '')
                                        )

                                        contact_company = contact.text\
                                            .replace('Visit website', '')\
                                            .replace('»', '')\
                                            .replace('View profile', '')\
                                            .replace('	', '')

                                        worksheet.write(i, 0, contact_company, cell_format_orange)
                                        worksheet.write(i, 1, '', cell_format_orange)
                                        worksheet.write(i, 2, '', cell_format_orange)
                                        worksheet.write(i, 3, '', cell_format_orange)
                                        worksheet.write(i, 4, '', cell_format_orange)
                                        worksheet.write(i, 5, city, cell_format_orange)
                                        worksheet.write(i, 6, 'data center', cell_format_orange)
                                        worksheet.write(i, 7, country, cell_format_orange)
                                        worksheet.write(i, 8, '', cell_format_orange)

                                        i += 1
                                else:
                                    print("no contact")

                if soup_all_country.find("div", {'class': 'column2'}) is not None:
                    all_a = soup_all_country.find("div", {'class': 'column2'}).find_all('a')

                    for a in all_a:
                        print(
                            "url : https://www.datacentermap.com" + a.get('href')
                        )

                        country = a.get('href')

                        url = "https://www.datacentermap.com" + a.get('href')

                        html = requests.get(url, headers=headers)

                        soup_city = BeautifulSoup(html.content, 'html.parser')

                        if soup_city.find("div", {'class': 'column1'}) is not None:
                            all_a = soup_city.find("div", {'class': 'column1'}).find_all('a')

                            for a in all_a:
                                print(
                                    "url : https://www.datacentermap.com" + a.get('href')
                                )

                                city = a.get('href')

                                url = "https://www.datacentermap.com" + a.get('href')

                                html = requests.get(url, headers=headers)

                                soup_contact = BeautifulSoup(html.content, 'html.parser')

                                if soup_contact.find("div", {'class': 'DCColumn1'}) is not None:
                                    contacts = soup_contact.find_all("div", {'class': 'DCColumn1'})

                                    for contact in contacts:
                                        print(
                                            "contact : " + contact.text
                                            .replace('Visit website', '')
                                            .replace('»', '')
                                            .replace('View profile', '')
                                            .replace('	', '')
                                        )

                                        contact_company = contact.text\
                                            .replace('Visit website', '')\
                                            .replace('»', '')\
                                            .replace('View profile', '')\
                                            .replace('	', '')

                                        worksheet.write(i, 0, contact_company, cell_format_orange)
                                        worksheet.write(i, 1, '', cell_format_orange)
                                        worksheet.write(i, 2, '', cell_format_orange)
                                        worksheet.write(i, 3, '', cell_format_orange)
                                        worksheet.write(i, 4, '', cell_format_orange)
                                        worksheet.write(i, 5, city, cell_format_orange)
                                        worksheet.write(i, 6, 'data center', cell_format_orange)
                                        worksheet.write(i, 7, country, cell_format_orange)
                                        worksheet.write(i, 8, '', cell_format_orange)

                                        i += 1
                                else:
                                    print("no contact")

                        if soup_city.find("div", {'class': 'column2'}) is not None:
                            all_a = soup_city.find("div", {'class': 'column2'}).find_all('a')

                            for a in all_a:
                                print(
                                    "url : https://www.datacentermap.com" + a.get('href')
                                )

                                city = a.get('href')

                                url = "https://www.datacentermap.com" + a.get('href')

                                html = requests.get(url, headers=headers)

                                soup_contact = BeautifulSoup(html.content, 'html.parser')

                                if soup_contact.find("div", {'class': 'DCColumn1'}) is not None:
                                    contacts = soup_contact.find_all("div", {'class': 'DCColumn1'})

                                    for contact in contacts:
                                        print(
                                            "contact : " + contact.text
                                            .replace('Visit website', '')
                                            .replace('»', '')
                                            .replace('View profile', '')
                                            .replace('	', '')
                                        )

                                        contact_company = contact.text\
                                            .replace('Visit website', '')\
                                            .replace('»', '')\
                                            .replace('View profile', '')\
                                            .replace('	', '')

                                        worksheet.write(i, 0, contact_company, cell_format_orange)
                                        worksheet.write(i, 1, '', cell_format_orange)
                                        worksheet.write(i, 2, '', cell_format_orange)
                                        worksheet.write(i, 3, '', cell_format_orange)
                                        worksheet.write(i, 4, '', cell_format_orange)
                                        worksheet.write(i, 5, city, cell_format_orange)
                                        worksheet.write(i, 6, 'data center', cell_format_orange)
                                        worksheet.write(i, 7, country, cell_format_orange)
                                        worksheet.write(i, 8, '', cell_format_orange)

                                        i += 1
                                else:
                                    print("no contact")

                        if soup_city.find("div", {'class': 'column3'}) is not None:
                            all_a = soup_city.find("div", {'class': 'column3'}).find_all('a')

                            for a in all_a:
                                print(
                                    "url : https://www.datacentermap.com" + a.get('href')
                                )

                                city = a.get('href')

                                url = "https://www.datacentermap.com" + a.get('href')

                                html = requests.get(url, headers=headers)

                                soup_contact = BeautifulSoup(html.content, 'html.parser')

                                if soup_contact.find("div", {'class': 'DCColumn1'}) is not None:
                                    contacts = soup_contact.find_all("div", {'class': 'DCColumn1'})

                                    for contact in contacts:
                                        print(
                                            "contact : " + contact.text
                                            .replace('Visit website', '')
                                            .replace('»', '')
                                            .replace('View profile', '')
                                            .replace('	', '')
                                        )

                                        contact_company = contact.text\
                                            .replace('Visit website', '')\
                                            .replace('»', '')\
                                            .replace('View profile', '')\
                                            .replace('	', '')

                                        worksheet.write(i, 0, contact_company, cell_format_orange)
                                        worksheet.write(i, 1, '', cell_format_orange)
                                        worksheet.write(i, 2, '', cell_format_orange)
                                        worksheet.write(i, 3, '', cell_format_orange)
                                        worksheet.write(i, 4, '', cell_format_orange)
                                        worksheet.write(i, 5, city, cell_format_orange)
                                        worksheet.write(i, 6, 'data center', cell_format_orange)
                                        worksheet.write(i, 7, country, cell_format_orange)
                                        worksheet.write(i, 8, '', cell_format_orange)

                                        i += 1
                                else:
                                    print("no contact")

                if soup_all_country.find("div", {'class': 'column3'}) is not None:
                    all_a = soup_all_country.find("div", {'class': 'column3'}).find_all('a')

                    for a in all_a:
                        print(
                            "url : https://www.datacentermap.com" + a.get('href')
                        )

                        country = a.get('href')

                        url = "https://www.datacentermap.com" + a.get('href')

                        html = requests.get(url, headers=headers)

                        soup_city = BeautifulSoup(html.content, 'html.parser')

                        if soup_city.find("div", {'class': 'column1'}) is not None:
                            all_a = soup_city.find("div", {'class': 'column1'}).find_all('a')

                            for a in all_a:
                                print(
                                    "url : https://www.datacentermap.com" + a.get('href')
                                )

                                city = a.get('href')

                                url = "https://www.datacentermap.com" + a.get('href')

                                html = requests.get(url, headers=headers)

                                soup_contact = BeautifulSoup(html.content, 'html.parser')

                                if soup_contact.find("div", {'class': 'DCColumn1'}) is not None:
                                    contacts = soup_contact.find_all("div", {'class': 'DCColumn1'})

                                    for contact in contacts:
                                        print(
                                            "contact : " + contact.text
                                            .replace('Visit website', '')
                                            .replace('»', '')
                                            .replace('View profile', '')
                                            .replace('	', '')
                                        )

                                        contact_company = contact.text\
                                            .replace('Visit website', '')\
                                            .replace('»', '')\
                                            .replace('View profile', '')\
                                            .replace('	', '')

                                        worksheet.write(i, 0, contact_company, cell_format_orange)
                                        worksheet.write(i, 1, '', cell_format_orange)
                                        worksheet.write(i, 2, '', cell_format_orange)
                                        worksheet.write(i, 3, '', cell_format_orange)
                                        worksheet.write(i, 4, '', cell_format_orange)
                                        worksheet.write(i, 5, city, cell_format_orange)
                                        worksheet.write(i, 6, 'data center', cell_format_orange)
                                        worksheet.write(i, 7, country, cell_format_orange)
                                        worksheet.write(i, 8, '', cell_format_orange)

                                        i += 1
                                else:
                                    print("no contact")

                        if soup_city.find("div", {'class': 'column2'}) is not None:
                            all_a = soup_city.find("div", {'class': 'column2'}).find_all('a')

                            for a in all_a:
                                print(
                                    "url : https://www.datacentermap.com" + a.get('href')
                                )

                                city = a.get('href')

                                url = "https://www.datacentermap.com" + a.get('href')

                                html = requests.get(url, headers=headers)

                                soup_contact = BeautifulSoup(html.content, 'html.parser')

                                if soup_contact.find("div", {'class': 'DCColumn1'}) is not None:
                                    contacts = soup_contact.find_all("div", {'class': 'DCColumn1'})

                                    for contact in contacts:
                                        print(
                                            "contact : " + contact.text
                                            .replace('Visit website', '')
                                            .replace('»', '')
                                            .replace('View profile', '')
                                            .replace('	', '')
                                        )

                                        contact_company = contact.text \
                                            .replace('Visit website', '') \
                                            .replace('»', '') \
                                            .replace('View profile', '') \
                                            .replace('	', '')

                                        worksheet.write(i, 0, contact_company, cell_format_orange)
                                        worksheet.write(i, 1, '', cell_format_orange)
                                        worksheet.write(i, 2, '', cell_format_orange)
                                        worksheet.write(i, 3, '', cell_format_orange)
                                        worksheet.write(i, 4, '', cell_format_orange)
                                        worksheet.write(i, 5, city, cell_format_orange)
                                        worksheet.write(i, 6, 'data center', cell_format_orange)
                                        worksheet.write(i, 7, country, cell_format_orange)
                                        worksheet.write(i, 8, '', cell_format_orange)

                                        i += 1
                                else:
                                    print("no contact")

                        if soup_city.find("div", {'class': 'column3'}) is not None:
                            all_a = soup_city.find("div", {'class': 'column3'}).find_all('a')

                            for a in all_a:
                                print(
                                    "url : https://www.datacentermap.com" + a.get('href')
                                )

                                city = a.get('href')

                                url = "https://www.datacentermap.com" + a.get('href')

                                html = requests.get(url, headers=headers)

                                soup_contact = BeautifulSoup(html.content, 'html.parser')

                                if soup_contact.find("div", {'class': 'DCColumn1'}) is not None:
                                    contacts = soup_contact.find_all("div", {'class': 'DCColumn1'})

                                    for contact in contacts:
                                        print(
                                            "contact : " + contact.text
                                            .replace('Visit website', '')
                                            .replace('»', '')
                                            .replace('View profile', '')
                                            .replace('	', '')
                                        )

                                        contact_company = contact.text\
                                            .replace('Visit website', '')\
                                            .replace('»', '')\
                                            .replace('View profile', '')\
                                            .replace('	', '')

                                        worksheet.write(i, 0, contact_company, cell_format_orange)
                                        worksheet.write(i, 1, '', cell_format_orange)
                                        worksheet.write(i, 2, '', cell_format_orange)
                                        worksheet.write(i, 3, '', cell_format_orange)
                                        worksheet.write(i, 4, '', cell_format_orange)
                                        worksheet.write(i, 5, city, cell_format_orange)
                                        worksheet.write(i, 6, 'data center', cell_format_orange)
                                        worksheet.write(i, 7, country, cell_format_orange)
                                        worksheet.write(i, 8, '', cell_format_orange)

                                        i += 1
                                else:
                                    print("no contact")

        workbook.close()

    def test_extract_contacts_from_one_country_and_one_city_into_excel(self):
        print('test_extract_one_contact_from_one_country_and_one_city')

        filename = "france_paris_contacts_data_centers.xlsx"

        url = "https://www.datacentermap.com/france/paris/"

        city = "paris"

        country = "france"

        workbook = xlsxwriter.Workbook(filename)

        worksheet = workbook.add_worksheet('data')

        cell_format_yellow = workbook.add_format(
            {
                'bg_color': 'yellow',
                'border': 1,
                'align': 'justify',
                'valign': 'top'
            }
        )

        worksheet.write(0, 0, 'company_name', cell_format_yellow)
        worksheet.write(0, 1, 'postal_address', cell_format_yellow)
        worksheet.write(0, 2, 'phone_number', cell_format_yellow)
        worksheet.write(0, 3, 'website', cell_format_yellow)
        worksheet.write(0, 4, 'email', cell_format_yellow)
        worksheet.write(0, 5, 'region', cell_format_yellow)
        worksheet.write(0, 6, 'activity', cell_format_yellow)
        worksheet.write(0, 7, 'country', cell_format_yellow)
        worksheet.write(0, 8, 'notes', cell_format_yellow)

        i = 1

        cell_format_orange = workbook.add_format(
            {
                'bg_color': 'orange',
                'border': 1,
                'align': 'justify',
                'valign': 'top'
            }
        )

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        time.sleep(3)

        html = requests.get(url, headers=headers)

        soup = BeautifulSoup(html.content, 'html.parser')

        if soup.find("div", {'class': 'DCColumn1p'}) is not None:
            contacts = soup.find_all("div", {'class': 'DCColumn1p'})

            for contact in contacts:
                print(
                    "contact : " + contact.text
                    .replace('Visit website', '')
                    .replace('»', '')
                    .replace('View profile', '')
                    .replace('	', '')
                )

                contact_company = contact.text \
                    .replace('Visit website', '') \
                    .replace('»', '') \
                    .replace('View profile', '') \
                    .replace('	', '')

                worksheet.write(i, 0, contact_company, cell_format_orange)
                worksheet.write(i, 1, '', cell_format_orange)
                worksheet.write(i, 2, '', cell_format_orange)
                worksheet.write(i, 3, '', cell_format_orange)
                worksheet.write(i, 4, '', cell_format_orange)
                worksheet.write(i, 5, city, cell_format_orange)
                worksheet.write(i, 6, 'data center', cell_format_orange)
                worksheet.write(i, 7, country, cell_format_orange)
                worksheet.write(i, 8, '', cell_format_orange)

                i += 1
        else:
            print("no contact")

        if soup.find("div", {'class': 'DCColumn1'}) is not None:
            contacts = soup.find_all("div", {'class': 'DCColumn1'})

            for contact in contacts:
                print(
                    "contact : " + contact.text
                    .replace('Visit website', '')
                    .replace('»', '')
                    .replace('View profile', '')
                    .replace('	', '')
                )

                contact_company = contact.text \
                    .replace('Visit website', '') \
                    .replace('»', '') \
                    .replace('View profile', '') \
                    .replace('	', '')

                worksheet.write(i, 0, contact_company, cell_format_orange)
                worksheet.write(i, 1, '', cell_format_orange)
                worksheet.write(i, 2, '', cell_format_orange)
                worksheet.write(i, 3, '', cell_format_orange)
                worksheet.write(i, 4, '', cell_format_orange)
                worksheet.write(i, 5, city, cell_format_orange)
                worksheet.write(i, 6, 'data center', cell_format_orange)
                worksheet.write(i, 7, country, cell_format_orange)
                worksheet.write(i, 8, '', cell_format_orange)

                i += 1
        else:
            print("no contact")

        workbook.close()


if __name__ == '__main__':
    unittest.main()
