import ssl
import time
from bs4 import BeautifulSoup
from requests_tor import RequestsTor
import unittest
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem
from lxml import etree
from OpenSSL import SSL
import pymongo


class UnitTestsDataMinerYellowPagesSuisseWithRequests(unittest.TestCase):
    # ok
    def test_extract_the_company_name_from_one_page(self):
        print('test_extract_the_company_name_from_one_page')

        # User Agent
        software_names = [
            SoftwareName.CHROME.value,
            SoftwareName.YAHOO_SLURP_WEB_CRAWLER_BOT.value,
            SoftwareName.ALEXA_BOT.value,
            SoftwareName.AMAYA.value,
            SoftwareName.AMAZON_API_GATEWAY.value
        ]

        operating_systems = [
            OperatingSystem.WINDOWS.value,
            OperatingSystem.LINUX.value,
            OperatingSystem.ANDROID.value,
            OperatingSystem.BADA.value,
            OperatingSystem.BLACKBERRY.value,
            OperatingSystem.MAC_OS_X.value,
            OperatingSystem.FREEBSD.value
        ]

        user_agent_rotator = UserAgent(
            software_names=software_names,
            operating_systems=operating_systems,
            limit=100
        )
        user_agent = user_agent_rotator.get_random_user_agent()

        headers = {
            'User-Agent': user_agent
        }

        url = 'https://www.local.ch/fr/d/geneve/1204/hotel/hotel-residence-cite-verdaine-jJl9CpCREdpKiHujc3hKug'

        rt = RequestsTor()

        html = rt.get(url, headers=headers)

        time.sleep(3)

        soup = BeautifulSoup(html.content, 'html.parser')

        if soup.find("span", {'itemprop': 'name'}) is not None:
            company_name = soup.find_all("span", {'itemprop': 'name'})[0].text
            print("company_name : " + str(company_name))
        else:
            print("no company_name")

    # ok
    def test_extract_the_address_from_one_page(self):
        print('test_extract_the_address_from_one_page')

        # User Agent
        software_names = [
            SoftwareName.CHROME.value,
            SoftwareName.YAHOO_SLURP_WEB_CRAWLER_BOT.value,
            SoftwareName.ALEXA_BOT.value,
            SoftwareName.AMAYA.value,
            SoftwareName.AMAZON_API_GATEWAY.value
        ]

        operating_systems = [
            OperatingSystem.WINDOWS.value,
            OperatingSystem.LINUX.value,
            OperatingSystem.ANDROID.value,
            OperatingSystem.BADA.value,
            OperatingSystem.BLACKBERRY.value,
            OperatingSystem.MAC_OS_X.value,
            OperatingSystem.FREEBSD.value
        ]

        user_agent_rotator = UserAgent(
            software_names=software_names,
            operating_systems=operating_systems,
            limit=100
        )
        user_agent = user_agent_rotator.get_random_user_agent()

        headers = {
            'User-Agent': user_agent
        }

        url = 'https://www.local.ch/fr/d/geneve/1204/hotel/hotel-residence-cite-verdaine-jJl9CpCREdpKiHujc3hKug'

        rt = RequestsTor()

        html = rt.get(url, headers=headers)

        time.sleep(3)

        soup = BeautifulSoup(html.content, 'html.parser')

        if soup.find("div", {'data-kpi-type': 'address'}) is not None:
            address = soup.find_all("div", {'data-kpi-type': 'address'})[0].text.replace('\n', '')
            print("address : " + str(address))
        else:
            print("no address")

    # ok
    def test_extract_the_phone_number_from_one_page(self):
        print('test_extract_the_phone_number_from_one_page')

        # User Agent
        software_names = [
            SoftwareName.CHROME.value,
            SoftwareName.YAHOO_SLURP_WEB_CRAWLER_BOT.value,
            SoftwareName.ALEXA_BOT.value,
            SoftwareName.AMAYA.value,
            SoftwareName.AMAZON_API_GATEWAY.value
        ]

        operating_systems = [
            OperatingSystem.WINDOWS.value,
            OperatingSystem.LINUX.value,
            OperatingSystem.ANDROID.value,
            OperatingSystem.BADA.value,
            OperatingSystem.BLACKBERRY.value,
            OperatingSystem.MAC_OS_X.value,
            OperatingSystem.FREEBSD.value
        ]

        user_agent_rotator = UserAgent(
            software_names=software_names,
            operating_systems=operating_systems,
            limit=100
        )
        user_agent = user_agent_rotator.get_random_user_agent()

        headers = {
            'User-Agent': user_agent
        }

        url = 'https://www.local.ch/fr/d/geneve/1204/hotel/hotel-residence-cite-verdaine-jJl9CpCREdpKiHujc3hKug'

        rt = RequestsTor()

        html = rt.get(url, headers=headers)

        time.sleep(3)

        soup = BeautifulSoup(html.content, 'html.parser')

        dom = etree.HTML(str(soup))

        phone_number = ""

        try:
            phone_number += dom.xpath('/html/body/div[3]/div/div/div[2]/div/div/div/div[1]/div[2]/div/div/a[2]/@href')[0]
            print("phone_number : " + str(phone_number))
        except Exception as e:
            print('error phone_number : ' + str(e))

    # ok
    def test_extract_the_website_from_one_page(self):
        print('test_extract_the_website_from_one_page')

        context = SSL.Context(SSL.TLSv1_2_METHOD)
        context.minimum_version = ssl.TLSVersion.TLSv1_2
        context.maximum_version = ssl.TLSVersion.TLSv1_3

        # User Agent
        software_names = [
            SoftwareName.CHROME.value,
            SoftwareName.YAHOO_SLURP_WEB_CRAWLER_BOT.value,
            SoftwareName.ALEXA_BOT.value,
            SoftwareName.AMAYA.value,
            SoftwareName.AMAZON_API_GATEWAY.value
        ]

        operating_systems = [
            OperatingSystem.WINDOWS.value,
            OperatingSystem.LINUX.value,
            OperatingSystem.ANDROID.value,
            OperatingSystem.BADA.value,
            OperatingSystem.BLACKBERRY.value,
            OperatingSystem.MAC_OS_X.value,
            OperatingSystem.FREEBSD.value
        ]

        user_agent_rotator = UserAgent(
            software_names=software_names,
            operating_systems=operating_systems,
            limit=100
        )
        user_agent = user_agent_rotator.get_random_user_agent()

        headers = {
            'User-Agent': user_agent
        }

        url = 'https://www.local.ch/fr/d/geneve/1204/hotel/hotel-residence-cite-verdaine-jJl9CpCREdpKiHujc3hKug'

        rt = RequestsTor()

        html = rt.get(url, headers=headers)

        time.sleep(3)

        soup = BeautifulSoup(html.content, 'html.parser')

        dom = etree.HTML(str(soup))

        website = ''

        try:
            website += dom.xpath('/html/body/div[3]/div/div/div[2]/div/div/div/div[1]/div[2]/div/div/a[3]/@href')[0]
            print("website : " + str(website))
        except Exception as e:
            print('error website : ' + str(e))

    # ok
    def test_extract_the_email_from_one_page(self):
        print('test_extract_the_email_from_one_page')

        context = SSL.Context(SSL.TLSv1_2_METHOD)
        context.minimum_version = ssl.TLSVersion.TLSv1_2
        context.maximum_version = ssl.TLSVersion.TLSv1_3

        # User Agent
        software_names = [
            SoftwareName.CHROME.value,
            SoftwareName.YAHOO_SLURP_WEB_CRAWLER_BOT.value,
            SoftwareName.ALEXA_BOT.value,
            SoftwareName.AMAYA.value,
            SoftwareName.AMAZON_API_GATEWAY.value
        ]

        operating_systems = [
            OperatingSystem.WINDOWS.value,
            OperatingSystem.LINUX.value,
            OperatingSystem.ANDROID.value,
            OperatingSystem.BADA.value,
            OperatingSystem.BLACKBERRY.value,
            OperatingSystem.MAC_OS_X.value,
            OperatingSystem.FREEBSD.value
        ]

        user_agent_rotator = UserAgent(
            software_names=software_names,
            operating_systems=operating_systems,
            limit=100
        )
        user_agent = user_agent_rotator.get_random_user_agent()

        headers = {
            'User-Agent': user_agent
        }

        url = 'https://www.local.ch/fr/d/geneve/1204/hotel/hotel-residence-cite-verdaine-jJl9CpCREdpKiHujc3hKug'

        rt = RequestsTor()

        html = rt.get(url, headers=headers)

        time.sleep(3)

        soup = BeautifulSoup(html.content, 'html.parser')

        dom = etree.HTML(str(soup))

        email = ''

        try:
            email += "'" + dom.xpath('/html/body/div[3]/div/div/div[2]/div/div/div/div[1]/div[2]/div/div/a[4]/@href')[0].replace('mailto:', '') + "',"
            print("email : " + str(email))
        except Exception as e:
            print('error email : ' + str(e))

    # ok
    def test_extract_all_urls_from_one_page_result(self):
        print('test_extract_all_urls_from_one_page_result')

        context = SSL.Context(SSL.TLSv1_2_METHOD)
        context.minimum_version = ssl.TLSVersion.TLSv1_2
        context.maximum_version = ssl.TLSVersion.TLSv1_3

        # User Agent
        software_names = [
            SoftwareName.CHROME.value,
            SoftwareName.YAHOO_SLURP_WEB_CRAWLER_BOT.value,
            SoftwareName.ALEXA_BOT.value,
            SoftwareName.AMAYA.value,
            SoftwareName.AMAZON_API_GATEWAY.value
        ]

        operating_systems = [
            OperatingSystem.WINDOWS.value,
            OperatingSystem.LINUX.value,
            OperatingSystem.ANDROID.value,
            OperatingSystem.BADA.value,
            OperatingSystem.BLACKBERRY.value,
            OperatingSystem.MAC_OS_X.value,
            OperatingSystem.FREEBSD.value
        ]

        user_agent_rotator = UserAgent(
            software_names=software_names,
            operating_systems=operating_systems,
            limit=100
        )
        user_agent = user_agent_rotator.get_random_user_agent()

        headers = {
            'User-Agent': user_agent
        }

        url = 'https://www.local.ch/fr/q?what=Electricit%C3%A9%2C+approvisionnement+en&where=Suisse&rid=QTmV&slot=tel&page=2'

        rt = RequestsTor()

        html = rt.get(url, headers=headers)

        time.sleep(3)

        soup = BeautifulSoup(html.content, 'html.parser')

        urls = []

        if soup.find('a', {'class': 'card-info'}) is not None:
            all_a = soup.find_all('a', {'class': 'card-info'})

            for a in all_a:
                url = a.get('href')
                urls.append(url)
        else:
            print('no urls')

        for url in urls:
            print(url)

    # ok
    def test_calculate_the_number_of_pages(self):
        print('test_calculate_the_number_of_pages')

        context = SSL.Context(SSL.TLSv1_2_METHOD)
        context.minimum_version = ssl.TLSVersion.TLSv1_2
        context.maximum_version = ssl.TLSVersion.TLSv1_3

        # User Agent
        software_names = [
            SoftwareName.CHROME.value,
            SoftwareName.YAHOO_SLURP_WEB_CRAWLER_BOT.value,
            SoftwareName.ALEXA_BOT.value,
            SoftwareName.AMAYA.value,
            SoftwareName.AMAZON_API_GATEWAY.value
        ]

        operating_systems = [
            OperatingSystem.WINDOWS.value,
            OperatingSystem.LINUX.value,
            OperatingSystem.ANDROID.value,
            OperatingSystem.BADA.value,
            OperatingSystem.BLACKBERRY.value,
            OperatingSystem.MAC_OS_X.value,
            OperatingSystem.FREEBSD.value
        ]

        user_agent_rotator = UserAgent(
            software_names=software_names,
            operating_systems=operating_systems,
            limit=100
        )
        user_agent = user_agent_rotator.get_random_user_agent()

        headers = {
            'User-Agent': user_agent
        }

        url = 'https://www.local.ch/fr/q/Suisse/Electricit%C3%A9,%20approvisionnement%20en?page=1&rid=QTmV&slot=tel'

        rt = RequestsTor()

        html = rt.get(url, headers=headers)

        time.sleep(3)

        soup = BeautifulSoup(html.content, 'html.parser')

        number_of_pages = 0

        if soup.find('h1', {'class', 'search-header-results-title'}) is not None:
            number_of_pages_with_coma = int(soup.find('h1', {'class', 'search-header-results-title'})
                                            .text
                                            .split(" ")[0]
                                            .replace(" ", "")
                                            ) / 10

            if int(str(number_of_pages_with_coma).split(".")[1][:1]) < 5:
                number_of_pages += round(number_of_pages_with_coma) + 1
                print('number_of_pages : ' + str(number_of_pages))
            elif int(str(number_of_pages_with_coma).split(".")[1][:1]) >= 5:
                number_of_pages += round(number_of_pages_with_coma)
                print('number_of_pages : ' + str(number_of_pages))
        else:
            print('no span class comments')

    # ok
    def test_extract_all_urls_from_all_page_result(self):
        print('test_extract_all_urls_from_all_page_result')

        context = SSL.Context(SSL.TLSv1_2_METHOD)
        context.minimum_version = ssl.TLSVersion.TLSv1_2
        context.maximum_version = ssl.TLSVersion.TLSv1_3

        # User Agent
        software_names = [
            SoftwareName.CHROME.value,
            SoftwareName.YAHOO_SLURP_WEB_CRAWLER_BOT.value,
            SoftwareName.ALEXA_BOT.value,
            SoftwareName.AMAYA.value,
            SoftwareName.AMAZON_API_GATEWAY.value
        ]

        operating_systems = [
            OperatingSystem.WINDOWS.value,
            OperatingSystem.LINUX.value,
            OperatingSystem.ANDROID.value,
            OperatingSystem.BADA.value,
            OperatingSystem.BLACKBERRY.value,
            OperatingSystem.MAC_OS_X.value,
            OperatingSystem.FREEBSD.value
        ]

        user_agent_rotator = UserAgent(
            software_names=software_names,
            operating_systems=operating_systems,
            limit=100
        )
        user_agent = user_agent_rotator.get_random_user_agent()

        headers = {
            'User-Agent': user_agent
        }

        url_first = 'https://www.local.ch/fr/q?what=Electricit%C3%A9%2C+approvisionnement+en&where=Suisse'

        rt = RequestsTor()

        html_first = rt.get(url=url_first, headers=headers)

        time.sleep(3)

        soup_first = BeautifulSoup(html_first.content, 'html.parser')

        number_of_pages = 0

        if soup_first.find('h1', {'class', 'search-header-results-title'}) is not None:
            number_of_pages_with_coma = int(soup_first.find('h1', {'class', 'search-header-results-title'})
                                            .text
                                            .split(" ")[0]
                                            .replace(" ", "")
                                            ) / 10

            if int(str(number_of_pages_with_coma).split(".")[1][:1]) < 5:
                number_of_pages += round(number_of_pages_with_coma) + 1
                print('number_of_pages : ' + str(number_of_pages))
            elif int(str(number_of_pages_with_coma).split(".")[1][:1]) >= 5:
                number_of_pages += round(number_of_pages_with_coma)
                print('number_of_pages : ' + str(number_of_pages))
        else:
            print('no span class comments')

        for i in range(0, number_of_pages + 1):
            url_page = url_first + '&page=' + str(i)

            print(url_page)

            html_contact = rt.get(url=url_page, headers=headers)

            time.sleep(3)

            soup_contact = BeautifulSoup(html_contact.content, 'html.parser')

            urls = []

            if soup_contact.find('a', {'class': 'card-info'}) is not None:
                all_a = soup_contact.find_all('a', {'class': 'card-info'})

                for a in all_a:
                    url = a.get('href')
                    urls.append(url)
            else:
                print('no urls')

            for url in urls:
                print(url)

    # ok
    def test_extract_all_contacts_for_one_activity_and_one_city_from_all_page_result(self):
        print('test_extract_all_contacts_for_one_activity_and_one_city_from_all_page_result')

        context = SSL.Context(SSL.TLSv1_2_METHOD)
        context.minimum_version = ssl.TLSVersion.TLSv1_2
        context.maximum_version = ssl.TLSVersion.TLSv1_3

        # User Agent
        software_names = [
            SoftwareName.CHROME.value,
            SoftwareName.YAHOO_SLURP_WEB_CRAWLER_BOT.value,
            SoftwareName.ALEXA_BOT.value,
            SoftwareName.AMAYA.value,
            SoftwareName.AMAZON_API_GATEWAY.value
        ]

        operating_systems = [
            OperatingSystem.WINDOWS.value,
            OperatingSystem.LINUX.value,
            OperatingSystem.ANDROID.value,
            OperatingSystem.BADA.value,
            OperatingSystem.BLACKBERRY.value,
            OperatingSystem.MAC_OS_X.value,
            OperatingSystem.FREEBSD.value
        ]

        user_agent_rotator = UserAgent(
            software_names=software_names,
            operating_systems=operating_systems,
            limit=100
        )
        user_agent = user_agent_rotator.get_random_user_agent()

        headers = {
            'User-Agent': user_agent
        }

        activity = 'Electricit%C3%A9%2C+approvisionnement+en'

        city = 'Suisse'

        url_first = 'https://www.local.ch/fr/q?what=' + activity + '&where=' + city

        rt = RequestsTor()

        html_first = rt.get(url=url_first, headers=headers)

        time.sleep(3)

        soup_first = BeautifulSoup(html_first.content, 'html.parser')

        number_of_pages = 0

        if soup_first.find('h1', {'class', 'search-header-results-title'}) is not None:
            number_of_pages_with_coma = int(soup_first.find('h1', {'class', 'search-header-results-title'})
                                            .text
                                            .split(" ")[0]
                                            .replace(" ", "")
                                            ) / 10

            if int(str(number_of_pages_with_coma).split(".")[1][:1]) < 5:
                number_of_pages += round(number_of_pages_with_coma) + 1
                print('number_of_pages : ' + str(number_of_pages))
            elif int(str(number_of_pages_with_coma).split(".")[1][:1]) >= 5:
                number_of_pages += round(number_of_pages_with_coma)
                print('number_of_pages : ' + str(number_of_pages))
        else:
            print('no span class comments')

        for i in range(0, number_of_pages + 1):
            url_page = url_first + '&page=' + str(i)

            print(url_page)

            html_page = rt.get(url=url_page, headers=headers)

            time.sleep(3)

            soup_page = BeautifulSoup(html_page.content, 'html.parser')

            urls = []

            if soup_page.find('a', {'class': 'card-info'}) is not None:
                all_a = soup_page.find_all('a', {'class': 'card-info'})

                for a in all_a:
                    url = a.get('href')
                    urls.append(url)
            else:
                print('no urls')

            for url_contact in urls:
                print('url_contact : ' + url_contact)

                html_contact = rt.get(url=url_contact, headers=headers)

                time.sleep(3)

                soup_contact = BeautifulSoup(html_contact.content, 'html.parser')
                dom_contact = etree.HTML(str(soup_contact))

                # Dataset
                company_name = ''
                address = ''
                phone_number = ''
                website = ''
                email = ''

                if soup_contact.find("span", {'itemprop': 'name'}) is not None:
                    company_name += soup_contact.find_all("span", {'itemprop': 'name'})[0].text
                else:
                    print("no company_name")

                if soup_contact.find("div", {'data-kpi-type': 'address'}) is not None:
                    address += soup_contact.find_all("div", {'data-kpi-type': 'address'})[0].text.replace('\n', '')
                else:
                    print("no address")

                try:
                    phone_number += dom_contact.xpath('/html/body/div[3]/div/div/div[2]/div/div/div/div[1]/div[2]/div/div/a[2]/@href')[0]
                except Exception as e:
                    print('error phone_number : ' + str(e))

                try:
                    website += dom_contact.xpath('/html/body/div[3]/div/div/div[2]/div/div/div/div[1]/div[2]/div/div/a[3]/@href')[0]
                except Exception as e:
                    print('error website : ' + str(e))

                try:
                    email += "'" + dom_contact.xpath('/html/body/div[3]/div/div/div[2]/div/div/div/div[1]/div[2]/div/div/a[4]/@href')[0]\
                        .replace('mailto:', '') + "',"
                except Exception as e:
                    print('error email : ' + str(e))

                company_dataset = {
                    'company_name': company_name,
                    'address': address,
                    'phone_number': phone_number,
                    'website': website,
                    'email': email,
                    'activity': activity,
                    'city': city
                }

                print(company_dataset)

    # ok
    def test_extract_all_contacts_for_one_activity_and_one_city_from_all_page_result_into_mongodb(self):
        print('test_extract_all_contacts_for_one_activity_and_one_city_from_all_page_result_into_mongodb')

        activity = ''

        city = 'Genève'

        context = SSL.Context(SSL.TLSv1_2_METHOD)
        context.minimum_version = ssl.TLSVersion.TLSv1_2
        context.maximum_version = ssl.TLSVersion.TLSv1_3

        # User Agent
        software_names = [
            SoftwareName.CHROME.value,
            SoftwareName.YAHOO_SLURP_WEB_CRAWLER_BOT.value,
            SoftwareName.ALEXA_BOT.value,
            SoftwareName.AMAYA.value,
            SoftwareName.AMAZON_API_GATEWAY.value
        ]

        operating_systems = [
            OperatingSystem.WINDOWS.value,
            OperatingSystem.LINUX.value,
            OperatingSystem.ANDROID.value,
            OperatingSystem.BADA.value,
            OperatingSystem.BLACKBERRY.value,
            OperatingSystem.MAC_OS_X.value,
            OperatingSystem.FREEBSD.value
        ]

        user_agent_rotator = UserAgent(
            software_names=software_names,
            operating_systems=operating_systems,
            limit=100
        )
        user_agent = user_agent_rotator.get_random_user_agent()

        headers = {
            'User-Agent': user_agent
        }

        url_first = 'https://www.local.ch/fr/q?what=' + activity + '&where=' + city

        rt = RequestsTor()

        html_first = rt.get(url=url_first, headers=headers)

        time.sleep(3)

        soup_first = BeautifulSoup(html_first.content, 'html.parser')

        number_of_pages = 0

        if soup_first.find('h1', {'class', 'search-header-results-title'}) is not None:
            number_of_pages_with_coma = int(soup_first.find('h1', {'class', 'search-header-results-title'})
                                            .text
                                            .split(" ")[0]
                                            .replace(" ", "")
                                            ) / 10

            if int(str(number_of_pages_with_coma).split(".")[1][:1]) < 5:
                number_of_pages += round(number_of_pages_with_coma) + 1
                print('number_of_pages : ' + str(number_of_pages))
            elif int(str(number_of_pages_with_coma).split(".")[1][:1]) >= 5:
                number_of_pages += round(number_of_pages_with_coma)
                print('number_of_pages : ' + str(number_of_pages))
        else:
            print('no span class comments')

        for i in range(1, number_of_pages + 1):
            url_page = url_first + '&page=' + str(i)

            print(url_page)

            html_page = rt.get(url=url_page, headers=headers)

            time.sleep(3)

            soup_page = BeautifulSoup(html_page.content, 'html.parser')

            urls = []

            if soup_page.find('a', {'class': 'card-info'}) is not None:
                all_a = soup_page.find_all('a', {'class': 'card-info'})

                for a in all_a:
                    url = a.get('href')
                    urls.append(url)
            else:
                print('no urls')

            for url_contact in urls:
                print('url_contact : ' + url_contact)

                html_contact = rt.get(url=url_contact, headers=headers)

                time.sleep(3)

                soup_contact = BeautifulSoup(html_contact.content, 'html.parser')
                dom_contact = etree.HTML(str(soup_contact))

                # Dataset
                company_name = ''
                address = ''
                phone_number = ''
                website = ''
                email = ''

                if soup_contact.find("span", {'itemprop': 'name'}) is not None:
                    company_name += soup_contact.find_all("span", {'itemprop': 'name'})[0].text
                else:
                    print("no company_name")

                if soup_contact.find("div", {'data-kpi-type': 'address'}) is not None:
                    address += soup_contact.find_all("div", {'data-kpi-type': 'address'})[0].text.replace('\n', '')
                else:
                    print("no address")

                try:
                    phone_number += dom_contact.xpath('/html/body/div[3]/div/div/div[2]/div/div/div/div[1]/div[2]/div/div/a[2]/@href')[0]
                except Exception as e:
                    print('error phone_number : ' + str(e))

                try:
                    website += dom_contact.xpath('/html/body/div[3]/div/div/div[2]/div/div/div/div[1]/div[2]/div/div/a[3]/@href')[0]
                except Exception as e:
                    print('error website : ' + str(e))

                try:
                    email += "'" + dom_contact.xpath('/html/body/div[3]/div/div/div[2]/div/div/div/div[1]/div[2]/div/div/a[4]/@href')[0]\
                        .replace('mailto:', '') + "',"
                except Exception as e:
                    print('error email : ' + str(e))

                company_dataset = {
                    'company_name': company_name,
                    'address': address,
                    'phone_number': phone_number,
                    'website': website,
                    'email': email,
                    'activity': activity,
                    'city': city
                }

                # Credentials
                host = "localhost"
                port = 27017
                username = ""
                password = ""
                uri = "mongodb://" + username + ":" + password + "@" + host + ":" + str(port)
                myclient = pymongo.MongoClient(uri)
                companydb = myclient["companydb"]
                switzerland = companydb["switzerland"]
                switzerland.insert_one(company_dataset)
                myclient.close()

                print(company_dataset)


if __name__ == '__main__':
    unittest.main()
