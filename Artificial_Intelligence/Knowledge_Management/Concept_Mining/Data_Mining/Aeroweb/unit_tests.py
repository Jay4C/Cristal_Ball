import unittest
import time
from bs4 import BeautifulSoup
import xlsxwriter
from requests_tor import RequestsTor


# https://www.aeroweb-fr.net
class UnitTestsDataMiningAerowebFrFromDarkWeb(unittest.TestCase):
    # ok
    def test_extract_all_links_for_each_aeroclub_in_ile_de_france_from_one_page_from_dark_web(self):
        print("test_extract_all_links_for_each_aeroclub_in_ile_de_france_from_one_page_from_dark_web")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://www.aeroweb-fr.net/aeroclubs/pays/fr/region/ile-de-france/1"

        i = 1

        rt = RequestsTor()

        html_with_tor = rt.get(url, headers=headers)

        time.sleep(3)

        soup = BeautifulSoup(html_with_tor.content, 'html.parser')

        if soup.find('a', {'class': 'title'}) is not None:
            all_a = soup.find_all('a', {'class': 'title'})

            for a in all_a:
                link = "https://www.aeroweb-fr.net/" + a.get('href')

                print(str(i) + ' - ' + link)

                i += 1

    # ok
    def test_extract_all_links_for_each_aeroclub_in_ile_de_france_from_all_pages_from_dark_web(self):
        print("test_extract_all_links_for_each_aeroclub_in_ile_de_france_from_all_pages_from_dark_web")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        i = 1

        for i1 in range(1, 7):
            url = "https://www.aeroweb-fr.net/aeroclubs/pays/fr/region/ile-de-france/" + str(i1)

            rt = RequestsTor()

            html_with_tor = rt.get(url, headers=headers)

            soup = BeautifulSoup(html_with_tor.content, 'html.parser')

            if soup.find('a', {'class': 'title'}) is not None:
                all_a = soup.find_all('a', {'class': 'title'})

                for a in all_a:
                    link = "https://www.aeroweb-fr.net" + a.get('href')

                    print(str(i) + ' - ' + link)

                    i += 1

    # ok
    def test_extract_the_name_for_one_aeroclub_in_ile_de_france_from_dark_web(self):
        print("test_extract_the_name_for_one_aeroclub_in_ile_de_france_from_dark_web")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://www.aeroweb-fr.net/aeroclubs/aeroclub-daeroport-de-paris-adp"

        rt = RequestsTor()

        html_with_tor = rt.get(url, headers=headers)

        soup = BeautifulSoup(html_with_tor.content, 'html.parser')

        name = ''

        if soup.find('div', {'class': 'yui-u first'}).find('h1').find('a') is not None:
            name += soup.find('div', {'class': 'yui-u first'}).find('h1').find('a').text
            print('name : ' + str(name))

    # ok
    def test_extract_the_address_for_one_aeroclub_in_ile_de_france_from_dark_web(self):
        print("test_extract_the_address_for_one_aeroclub_in_ile_de_france_from_dark_web")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://www.aeroweb-fr.net/aeroclubs/aeroclub-daeroport-de-paris-adp"

        rt = RequestsTor()

        html_with_tor = rt.get(url, headers=headers)

        soup = BeautifulSoup(html_with_tor.content, 'html.parser')

        address = ''

        if soup.find('div', {'class': 'yui-u first'}).find('p') is not None:
            address += soup.find('div', {'class': 'yui-u first'}).find('p').text.replace('\n', ' ').replace("       ", "")
            print('address : ' + str(address))

    # ok
    def test_extract_the_phone_number_for_one_aeroclub_in_ile_de_france_from_dark_web(self):
        print("test_extract_the_phone_number_for_one_aeroclub_in_ile_de_france_from_dark_web")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://www.aeroweb-fr.net/aeroclubs/aeroclub-daeroport-de-paris-adp"

        rt = RequestsTor()

        html_with_tor = rt.get(url, headers=headers)

        soup = BeautifulSoup(html_with_tor.content, 'html.parser')

        phone_number = ''

        if soup.find('ul', {'class': 'puces'}) is not None:
            all_li = soup.find('ul', {'class': 'puces'}).find_all('li')

            for li in all_li:
                if li.find('strong') is not None:
                    if li.find('strong').text == "Téléphone :":
                        phone_number += li.text
                        print('phone_number : ' + str(phone_number))
                        break

    # ok
    def test_extract_the_fax_number_for_one_aeroclub_in_ile_de_france_from_dark_web(self):
        print("test_extract_the_fax_number_for_one_aeroclub_in_ile_de_france_from_dark_web")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://www.aeroweb-fr.net/aeroclubs/aeroclub-daeroport-de-paris-adp"

        rt = RequestsTor()

        html_with_tor = rt.get(url, headers=headers)

        soup = BeautifulSoup(html_with_tor.content, 'html.parser')

        fax_number = ''

        if soup.find('ul', {'class': 'puces'}) is not None:
            all_li = soup.find('ul', {'class': 'puces'}).find_all('li')

            for li in all_li:
                if li.find('strong') is not None:
                    if li.find('strong').text == "Fax :":
                        fax_number += li.text
                        print('fax_number : ' + str(fax_number))
                        break

    # ok
    def test_extract_the_email_address_for_one_aeroclub_in_ile_de_france_from_dark_web(self):
        print("test_extract_the_email_address_for_one_aeroclub_in_ile_de_france_from_dark_web")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://www.aeroweb-fr.net/aeroclubs/aeroclub-daeroport-de-paris-adp"

        rt = RequestsTor()

        html_with_tor = rt.get(url, headers=headers)

        soup = BeautifulSoup(html_with_tor.content, 'html.parser')

        email_address = ''

        if soup.find('ul', {'class': 'puces'}) is not None:
            all_li = soup.find('ul', {'class': 'puces'}).find_all('li')

            for li in all_li:
                if li.find('strong').find('a') is not None:
                    if li.find('strong').find('a').text == "Adresse email":
                        email_address += "'" + li.find('strong').find('a').get('href').replace('mailto:', '') + "',"
                        print('email_address : ' + str(email_address))
                        break

    # ok
    def test_extract_the_website_for_one_aeroclub_in_ile_de_france_from_dark_web(self):
        print("test_extract_the_website_for_one_aeroclub_in_ile_de_france_from_dark_web")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://www.aeroweb-fr.net/aeroclubs/aeroclub-daeroport-de-paris-adp"

        rt = RequestsTor()

        html_with_tor = rt.get(url, headers=headers)

        soup = BeautifulSoup(html_with_tor.content, 'html.parser')

        website = ''

        if soup.find('ul', {'class': 'puces'}) is not None:
            all_li = soup.find('ul', {'class': 'puces'}).find_all('li')

            for li in all_li:
                if li.find('strong').find('a') is not None:
                    if li.find('strong').find('a').text == "Site Internet":
                        website += li.find('strong').find('a').get('href')
                        print('website : ' + str(website))
                        break

    # ok
    def test_extract_contact_for_each_aeroclub_in_ile_de_france_from_all_pages_from_dark_web(self):
        print("test_extract_contact_for_each_aeroclub_in_ile_de_france_from_all_pages_from_dark_web")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        i = 1

        for i1 in range(1, 7):
            url = "https://www.aeroweb-fr.net/aeroclubs/pays/fr/region/ile-de-france/" + str(i1)

            rt = RequestsTor()

            html_with_tor = rt.get(url, headers=headers)

            soup = BeautifulSoup(html_with_tor.content, 'html.parser')

            if soup.find('a', {'class': 'title'}) is not None:
                all_a = soup.find_all('a', {'class': 'title'})

                for a in all_a:
                    link = "https://www.aeroweb-fr.net" + a.get('href')

                    rt = RequestsTor()

                    html_with_tor_link = rt.get(link, headers=headers)

                    soup_link = BeautifulSoup(html_with_tor_link.content, 'html.parser')

                    name = ''
                    address = ''
                    phone_number = ''
                    fax_number = ''
                    email_address = ''
                    website = ''

                    if soup_link.find('div', {'class': 'yui-u first'}).find('h1').find('a') is not None:
                        name += soup_link.find('div', {'class': 'yui-u first'}).find('h1').find('a').text

                    if soup_link.find('div', {'class': 'yui-u first'}).find('p') is not None:
                        address += soup_link.find('div', {'class': 'yui-u first'}).find('p').text.replace('\n', ' ').replace(
                            "       ", "")

                    if soup_link.find('ul', {'class': 'puces'}) is not None:
                        all_li = soup_link.find('ul', {'class': 'puces'}).find_all('li')

                        for li in all_li:
                            if li.find('strong') is not None:
                                if li.find('strong').text == "Téléphone :":
                                    phone_number += li.text.replace('\r\n', '')
                                    break

                    if soup_link.find('ul', {'class': 'puces'}) is not None:
                        all_li = soup_link.find('ul', {'class': 'puces'}).find_all('li')

                        for li in all_li:
                            if li.find('strong') is not None:
                                if li.find('strong').text == "Fax :":
                                    fax_number += li.text.replace('\r\n', '')
                                    break

                    if soup_link.find('ul', {'class': 'puces'}) is not None:
                        all_li = soup_link.find('ul', {'class': 'puces'}).find_all('li')

                        for li in all_li:
                            if li.find('strong').find('a') is not None:
                                if li.find('strong').find('a').text == "Adresse email":
                                    email_address += "'" + li.find('strong').find('a').get('href').replace('mailto:',
                                                                                                           '') + "',"
                                    break

                    if soup_link.find('ul', {'class': 'puces'}) is not None:
                        all_li = soup_link.find('ul', {'class': 'puces'}).find_all('li')

                        for li in all_li:
                            if li.find('strong').find('a') is not None:
                                if li.find('strong').find('a').text == "Site Internet":
                                    website += li.find('strong').find('a').get('href')
                                    break

                    contact = {
                        'name': name,
                        'address': address,
                        'phone_number': phone_number,
                        'fax_number': fax_number,
                        'email_address': email_address,
                        'website': website
                    }

                    print(str(i) + ' - ' + str(contact))

                    i += 1

    # ok
    def test_extract_contact_for_each_aeroclub_in_ile_de_france_from_all_pages_into_excel_from_dark_web(self):
        print("test_extract_contact_for_each_aeroclub_in_ile_de_france_from_all_pages_into_excel_from_dark_web")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        i = 1

        filename = "contacts_aeroclubs.xlsx"

        workbook = xlsxwriter.Workbook(filename)

        worksheet = workbook.add_worksheet('Data')

        worksheet.write(0, 0, 'name')
        worksheet.write(0, 1, 'address')
        worksheet.write(0, 2, 'phone_number')
        worksheet.write(0, 3, 'fax_number')
        worksheet.write(0, 4, 'email_address')
        worksheet.write(0, 5, 'website')

        for i1 in range(1, 7):
            try:
                url = "https://www.aeroweb-fr.net/aeroclubs/pays/fr/region/ile-de-france/" + str(i1)

                rt = RequestsTor()

                html_with_tor = rt.get(url, headers=headers)

                soup = BeautifulSoup(html_with_tor.content, 'html.parser')

                if soup.find('a', {'class': 'title'}) is not None:
                    all_a = soup.find_all('a', {'class': 'title'})

                    for a in all_a:
                        try:
                            link = "https://www.aeroweb-fr.net" + a.get('href')

                            rt = RequestsTor()

                            html_with_tor_link = rt.get(link, headers=headers)

                            soup_link = BeautifulSoup(html_with_tor_link.content, 'html.parser')

                            name = ''
                            address = ''
                            phone_number = ''
                            fax_number = ''
                            email_address = ''
                            website = ''

                            if soup_link.find('div', {'class': 'yui-u first'}).find('h1').find('a') is not None:
                                name += soup_link.find('div', {'class': 'yui-u first'}).find('h1').find('a').text

                            if soup_link.find('div', {'class': 'yui-u first'}).find('p') is not None:
                                address += soup_link.find('div', {'class': 'yui-u first'}).find('p').text.replace('\n',
                                                                                                                  ' ').replace(
                                    "       ", "")

                            if soup_link.find('ul', {'class': 'puces'}) is not None:
                                all_li = soup_link.find('ul', {'class': 'puces'}).find_all('li')

                                for li in all_li:
                                    if li.find('strong') is not None:
                                        if li.find('strong').text == "Téléphone :":
                                            phone_number += li.text.replace('\r\n', '')
                                            break

                            if soup_link.find('ul', {'class': 'puces'}) is not None:
                                all_li = soup_link.find('ul', {'class': 'puces'}).find_all('li')

                                for li in all_li:
                                    if li.find('strong') is not None:
                                        if li.find('strong').text == "Fax :":
                                            fax_number += li.text.replace('\r\n', '')
                                            break

                            if soup_link.find('ul', {'class': 'puces'}) is not None:
                                all_li = soup_link.find('ul', {'class': 'puces'}).find_all('li')

                                for li in all_li:
                                    if li.find('strong').find('a') is not None:
                                        if li.find('strong').find('a').text == "Adresse email":
                                            email_address += "'" + li.find('strong').find('a').get('href').replace(
                                                'mailto:',
                                                '') + "',"
                                            break

                            if soup_link.find('ul', {'class': 'puces'}) is not None:
                                all_li = soup_link.find('ul', {'class': 'puces'}).find_all('li')

                                for li in all_li:
                                    if li.find('strong').find('a') is not None:
                                        if li.find('strong').find('a').text == "Site Internet":
                                            website += li.find('strong').find('a').get('href')
                                            break

                            contact = {
                                'name': name,
                                'address': address,
                                'phone_number': phone_number,
                                'fax_number': fax_number,
                                'email_address': email_address,
                                'website': website
                            }

                            worksheet.write(i, 0, contact.get('name'))
                            worksheet.write(i, 1, contact.get('address'))
                            worksheet.write(i, 2, contact.get('phone_number'))
                            worksheet.write(i, 3, contact.get('fax_number'))
                            worksheet.write(i, 4, contact.get('email_address'))
                            worksheet.write(i, 5, contact.get('website'))

                            print(str(i) + ' - ' + str(contact))

                            i += 1
                        except Exception as e:
                            print('error link : ' + str(e))
            except Exception as e:
                print('error url : ' + str(e))

        workbook.close()


if __name__ == '__main__':
    unittest.main()
