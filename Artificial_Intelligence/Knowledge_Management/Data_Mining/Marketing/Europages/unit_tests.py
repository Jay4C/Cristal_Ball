import time
import ssl
import warnings
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
from requests_tor import RequestsTor
import unittest
import subprocess
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem
from lxml import etree
from OpenSSL import SSL
import pymongo


class UnitTestsDataMinerMarketingEuropages(unittest.TestCase):
    # ok
    def test_close_all_processes(self):
        print('test_close_all_processes')

        subprocess.run('taskkill /f /im firefox.exe')
        subprocess.run('taskkill /f /im geckodriver.exe')

    # ok
    def test_extract_the_company_name_from_one_page_result(self):
        print('test_extract_the_company_name_from_one_page_result')

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

        url = 'https://www.europages.fr/SBATRAFOTECH-GMBH/DEU443327-00101.html'

        # rt = requests
        rt = RequestsTor()

        html = rt.get(url, headers=headers).content

        time.sleep(3)

        soup = BeautifulSoup(html, 'html.parser')

        dom = etree.HTML(str(soup))

        company_name = ''

        try:
            company_name += dom.xpath('/html/body/div[1]/div/div/div[1]/div[1]/div[2]/div[2]/div[1]/header/h1')[0].text.replace('\n', '').replace('    ', '')
            print("company_name : " + str(company_name))
        except Exception as e:
            print('error company_name : ' + str(e))

    # ok
    def test_extract_the_country_from_one_page_result(self):
        print('test_extract_the_country_from_one_page_result')

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

        url = 'https://www.europages.fr/SBATRAFOTECH-GMBH/DEU443327-00101.html'

        # rt = requests
        rt = RequestsTor()

        html = rt.get(url, headers=headers).content

        time.sleep(3)

        soup = BeautifulSoup(html, 'html.parser')

        dom = etree.HTML(str(soup))

        country = ''

        try:
            country += dom.xpath('/html/body/div[1]/div/div/div[1]/div[1]/div[2]/div[2]/div[1]/header/div[1]/p[1]/span[2]')[0].text.replace('\n', '').replace('    ', '')
            print("country : " + str(country))
        except Exception as e:
            print('error country : ' + str(e))

    # ok
    def test_extract_the_main_activity_from_one_page_result(self):
        print('test_extract_the_main_activity_from_one_page_result')

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

        url = 'https://www.europages.fr/SBATRAFOTECH-GMBH/DEU443327-00101.html'

        # rt = requests
        rt = RequestsTor()

        html = rt.get(url, headers=headers).content

        time.sleep(3)

        soup = BeautifulSoup(html, 'html.parser')

        dom = etree.HTML(str(soup))

        main_activity = ''

        try:
            main_activity += dom.xpath('/html/body/div[1]/div/div/div[1]/div[1]/div[2]/div[2]/div[1]/header/div[1]/p[2]/span[2]')[0].text.replace('\n', '').replace('    ', '')
            print("main_activity : " + str(main_activity))
        except Exception as e:
            print('error main_activity : ' + str(e))

    # ok
    def test_extract_the_address_from_one_page_result(self):
        print('test_extract_the_address_from_one_page_result')

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

        url = 'https://www.europages.fr/SBATRAFOTECH-GMBH/DEU443327-00101.html'

        # rt = requests
        rt = RequestsTor()

        html = rt.get(url, headers=headers).content

        time.sleep(3)

        soup = BeautifulSoup(html, 'html.parser')

        address = ''

        try:
            if soup.find('div', {'class': 'v-card__text'}) is not None:
                address += soup.find_all('div', {'class': 'v-card__text'})[0].text\
                    .replace('Adresse', '')\
                    .replace('\n', '')
                print("address : " + str(address))
        except Exception as e:
            print('error address : ' + str(e))

    # ok
    def test_extract_the_website_from_one_page_result(self):
        print('test_extract_the_website_from_one_page_result')

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

        url = 'https://www.europages.fr/SBATRAFOTECH-GMBH/DEU443327-00101.html'

        # rt = requests
        rt = RequestsTor()

        html = rt.get(url, headers=headers).content

        time.sleep(3)

        soup = BeautifulSoup(html, 'html.parser')

        dom = etree.HTML(str(soup))

        website = ''

        try:
            website += dom.xpath('/html/body/div[1]/div/div/div[1]/div[1]/div[2]/div[2]/div[1]/aside/div/div[1]/div[4]/a[1]/@href')[0]
            print("website : " + str(website))
        except Exception as e:
            print('error website : ' + str(e))

    # ok
    def test_extract_the_email_from_one_page_result(self):
        print('test_extract_the_email_from_one_page_result')

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

        url = 'https://www.europages.fr/SBATRAFOTECH-GMBH/DEU443327-00101.html'

        rt = RequestsTor()

        html = rt.get(url, headers=headers).content

        time.sleep(3)

        soup = BeautifulSoup(html, 'html.parser')

        dom = etree.HTML(str(soup))

        email = ''

        try:
            email += "'info@" + dom.xpath('/html/body/div[1]/div/div/div[1]/div[1]/div[2]/div[2]/div[1]/aside/div/div[1]/div[4]/a[1]/@href')[0].replace('https://www.', '').replace('http://www.', '') + "',"
            print("email : " + str(email))
        except Exception as e:
            print('error email : ' + str(e))

    # ok
    def test_open_one_page_with_selenium(self):
        print('test_open_one_page_with_selenium')

        url = 'https://www.europages.fr/SBATRAFOTECH-GMBH/DEU443327-00101.html'

        time.sleep(5)

        warnings.filterwarnings(
            action="ignore",
            message="unclosed",
            category=ResourceWarning
        )

        time.sleep(5)

        # with Firefox
        browser = webdriver.Firefox(
            executable_path='C:\\Users\\Jason\\Dropbox\\1_Personnel\\1_Recurrentes\\3_Outils_Numeriques\\GitHub\\Cristal_Ball\\geckodriver.exe'
        )

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get(url)

        time.sleep(5)

    # ok
    def test_extract_the_phone_number_from_one_page_result_with_selenium(self):
        print('test_extract_the_phone_number_from_one_page_result_with_selenium')

        url = 'https://www.europages.fr/SBATRAFOTECH-GMBH/DEU443327-00101.html'

        time.sleep(5)

        warnings.filterwarnings(
            action="ignore",
            message="unclosed",
            category=ResourceWarning
        )

        time.sleep(5)

        # with Firefox
        options = Options()
        options.headless = True
        browser = webdriver.Firefox(
            executable_path='C:\\Users\\Jason\\Dropbox\\1_Personnel\\1_Recurrentes\\3_Outils_Numeriques\\GitHub'
                            '\\Cristal_Ball\\geckodriver.exe',
            options=options
        )

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get(url)

        time.sleep(5)

        # Click on the 'Afficher les détails' button
        afficher_les_details_button = browser.find_element(
            by=By.XPATH,
            value='//*[@id="cookiescript_manage_wrap"]'
        )
        afficher_les_details_button.click()
        print('afficher_les_details_button.click() clicked')

        time.sleep(5)

        # Click on the 'Sauvegarder mes préférences' button
        sauvegarder_mes_preferences_button = browser.find_element(
            by=By.XPATH,
            value='//*[@id="cookiescript_save"]'
        )
        sauvegarder_mes_preferences_button.click()
        print('sauvegarder_mes_preferences_button.click() clicked')

        time.sleep(5)

        # Click on the 'Téléphone' button
        telephone_button = browser.find_element(
            by=By.XPATH,
            value='/html/body/div[1]/div/div/div[1]/div[1]/div[2]/div[2]/div[1]/aside/div/div[1]/div[4]/button'
        )
        telephone_button.click()
        print('telephone_button.click() clicked')

        time.sleep(5)

        # Click on the 'Afficher le numéro' button
        afficher_le_numero_button = browser.find_element(
            by=By.XPATH,
            value='/html/body/div[1]/div/div/div[4]/div/div/div[2]/div/div[1]/div/button'
        )
        afficher_le_numero_button.click()
        print('afficher_le_numero_button.click() clicked')

        time.sleep(5)

        # Phone number text
        phone_number_text = browser.find_element(
            by=By.XPATH,
            value='/html/body/div[1]/div/div/div[4]/div/div/div[2]/div/div[1]/div/button/span/span'
        ).text

        print("phone_number_text : " + str(phone_number_text))

        time.sleep(5)

        browser.quit()

    # ok
    def test_extract_all_the_urls_company_from_one_page_results(self):
        print('test_extract_all_the_urls_company_from_one_page_results')

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

        url = "https://www.europages.fr/entreprises/cat-1-g%C3%A9n%C3%A9rateurs%20d'%C3%A9lectricit%C3%A9/" \
              "fabricant%20producteur/pg-2/g%C3%A9n%C3%A9rateurs%20d'%C3%A9lectricit%C3%A9.html"

        rt = RequestsTor()

        html = rt.get(url, headers=headers).content

        time.sleep(3)

        soup = BeautifulSoup(html, 'html.parser')

        if soup.find('a', {'class', 'ep-ecard-serp__epage-link'}) is not None:
            urls = soup.find_all('a', {'class': 'ep-ecard-serp__epage-link'})

            for url in urls:
                link = 'https://www.europages.fr' + url.get('href')
                print('link : ' + link)
        else:
            print('no urls')

    # ok
    def test_extract_the_number_of_page_result_from_one_page(self):
        print('test_extract_the_number_of_page_result_from_one_page')

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

        url = "https://www.europages.fr/entreprises/cat-1-g%C3%A9n%C3%A9rateurs%20d'%C3%A9lectricit%C3%A9/" \
              "fabricant%20producteur/pg-1/g%C3%A9n%C3%A9rateurs%20d'%C3%A9lectricit%C3%A9.html"

        rt = RequestsTor()

        html = rt.get(url, headers=headers).content

        time.sleep(3)

        soup = BeautifulSoup(html, 'html.parser')

        if soup.find('span', {'class', 'ep-big-tab-button__count'}) is not None:
            number_of_pages = 0

            number_of_pages_with_coma = int(
                soup.find('span', {'class', 'ep-big-tab-button__count'}).text.replace(" ", "")
            ) / 30

            if int(str(number_of_pages_with_coma).split(".")[1][:1]) < 5:
                number_of_pages += round(number_of_pages_with_coma) + 1
                print('number_of_pages : ' + str(number_of_pages))
            elif int(str(number_of_pages_with_coma).split(".")[1][:1]) >= 5:
                number_of_pages += round(number_of_pages_with_coma)
                print('number_of_pages : ' + str(number_of_pages))
        else:
            print('no span class ep-big-tab-button__count')

    # ok
    def test_extract_all_the_urls_company_from_all_page_results(self):
        print('test_extract_all_the_urls_company_from_all_page_results')

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

        url_activity = "https://www.europages.fr/entreprises/cat-1-g%C3%A9n%C3%A9rateurs%20d'%C3%A9lectricit%C3%A9/" \
              "fabricant%20producteur/pg-1/g%C3%A9n%C3%A9rateurs%20d'%C3%A9lectricit%C3%A9.html"

        rt = RequestsTor()

        html_activity = rt.get(url_activity, headers=headers).content

        time.sleep(3)

        soup_activity = BeautifulSoup(html_activity, 'html.parser')

        number_of_pages = 0

        if soup_activity.find('span', {'class', 'ep-big-tab-button__count'}) is not None:
            number_of_pages_with_coma = int(
                soup_activity.find('span', {'class', 'ep-big-tab-button__count'}).text.replace(" ", "")
            ) / 30

            if int(str(number_of_pages_with_coma).split(".")[1][:1]) < 5:
                number_of_pages += round(number_of_pages_with_coma) + 1
                print('number_of_pages : ' + str(number_of_pages))
            elif int(str(number_of_pages_with_coma).split(".")[1][:1]) >= 5:
                number_of_pages += round(number_of_pages_with_coma)
                print('number_of_pages : ' + str(number_of_pages))
        else:
            print('no span class ep-big-tab-button__count')

        for i in range(1, number_of_pages + 1):
            user_agent = user_agent_rotator.get_random_user_agent()

            headers = {
                'User-Agent': user_agent
            }

            url_page_result = "https://www.europages.fr/entreprises/cat-1-g%C3%A9n%C3%A9rateurs%20d'%C3%A9lectricit%C3%A9/" \
              "fabricant%20producteur/pg-" + str(i) + "/g%C3%A9n%C3%A9rateurs%20d'%C3%A9lectricit%C3%A9.html"

            print('url_page_result : ' + url_page_result)

            html_page_result = rt.get(url_page_result, headers=headers).content

            time.sleep(3)

            soup_page_result = BeautifulSoup(html_page_result, 'html.parser')

            if soup_page_result.find('a', {'class', 'ep-ecard-serp__epage-link'}) is not None:
                urls = soup_page_result.find_all('a', {'class': 'ep-ecard-serp__epage-link'})

                for url in urls:
                    link = 'https://www.europages.fr' + url.get('href')
                    print('link : ' + link)
            else:
                print('no urls')

    # ok
    def test_extract_all_details_for_one_company_into_mongodb(self):
        print('test_extract_all_details_for_one_company_into_mongodb')

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

        url = 'https://www.europages.fr/SBATRAFOTECH-GMBH/DEU443327-00101.html'

        rt = RequestsTor()

        html = rt.get(url, headers=headers).content

        time.sleep(3)

        soup = BeautifulSoup(html, 'html.parser')

        dom = etree.HTML(str(soup))

        company_name = ''
        country = ''
        main_activity = ''
        address = ''
        website = ''
        email = ''
        phone_number = ''

        try:
            company_name += dom.xpath('/html/body/div[1]/div/div/div[1]/div[1]/div[2]/div[2]/div[1]/header/h1')[
                0].text.replace('\n', '').replace('    ', '')
        except Exception as e:
            print('error company_name : ' + str(e))

        try:
            country += dom.xpath('/html/body/div[1]/div/div/div[1]/div[1]/div[2]/div[2]/div[1]/header/div[1]/p[1]/span[2]')[0].text.replace('\n', '').replace('    ', '')
        except Exception as e:
            print('error country : ' + str(e))

        try:
            main_activity += dom.xpath('/html/body/div[1]/div/div/div[1]/div[1]/div[2]/div[2]/div[1]/header/div[1]/p[2]/span[2]')[0].text.replace('\n', '').replace('    ', '')
        except Exception as e:
            print('error main_activity : ' + str(e))

        try:
            if soup.find('div', {'class': 'v-card__text'}) is not None:
                address += soup.find_all('div', {'class': 'v-card__text'})[0].text\
                    .replace('Adresse', '')\
                    .replace('\n', '')
        except Exception as e:
            print('error address : ' + str(e))

        try:
            website += dom.xpath('/html/body/div[1]/div/div/div[1]/div[1]/div[2]/div[2]/div[1]/aside/div/div[1]/div[4]/a[1]/@href')[0]
        except Exception as e:
            print('error website : ' + str(e))

        try:
            email += "'info@" + dom.xpath('/html/body/div[1]/div/div/div[1]/div[1]/div[2]/div[2]/div[1]/aside/div/div[1]/div[4]/a[1]/@href')[0]\
                .replace('https://www.', '')\
                .replace('http://www.', '') + "',"
        except Exception as e:
            print('error email : ' + str(e))

        time.sleep(5)

        warnings.filterwarnings(
            action="ignore",
            message="unclosed",
            category=ResourceWarning
        )

        time.sleep(5)

        # with Firefox
        options = Options()
        options.headless = True
        browser = webdriver.Firefox(
            executable_path='C:\\Users\\Jason\\Dropbox\\1_Personnel\\1_Recurrentes\\3_Outils_Numeriques\\GitHub'
                            '\\Cristal_Ball\\geckodriver.exe',
            options=options
        )

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get(url)

        time.sleep(5)

        # Click on the 'Afficher les détails' button
        try:
            afficher_les_details_button = browser.find_element(
                by=By.XPATH,
                value='//*[@id="cookiescript_manage_wrap"]'
            )
            afficher_les_details_button.click()
            print('afficher_les_details_button.click() clicked')
        except Exception as e:
            print('error afficher_les_details_button : ' + str(e))

        time.sleep(5)

        # Click on the 'Sauvegarder mes préférences' button
        try:
            sauvegarder_mes_preferences_button = browser.find_element(
                by=By.XPATH,
                value='//*[@id="cookiescript_save"]'
            )
            sauvegarder_mes_preferences_button.click()
            print('sauvegarder_mes_preferences_button.click() clicked')
        except Exception as e:
            print('error sauvegarder_mes_preferences_button : ' + str(e))

        time.sleep(5)

        # Click on the 'Téléphone' button
        try:
            telephone_button = browser.find_element(
                by=By.XPATH,
                value='/html/body/div[1]/div/div/div[1]/div[1]/div[2]/div[2]/div[1]/aside/div/div[1]/div[4]/button'
            )
            telephone_button.click()
            print('telephone_button.click() clicked')
        except Exception as e:
            print('error telephone_button : ' + str(e))

        time.sleep(5)

        # Click on the 'Afficher le numéro' button
        try:
            afficher_le_numero_button = browser.find_element(
                by=By.XPATH,
                value='/html/body/div[1]/div/div/div[4]/div/div/div[2]/div/div[1]/div/button'
            )
            afficher_le_numero_button.click()
            print('afficher_le_numero_button.click() clicked')
        except Exception as e:
            print('error afficher_le_numero_button : ' + str(e))

        time.sleep(5)

        # Phone number text
        try:
            phone_number += browser.find_element(
                by=By.XPATH,
                value='/html/body/div[1]/div/div/div[4]/div/div/div[2]/div/div[1]/div/button/span/span'
            ).text
        except Exception as e:
            print('error phone_number : ' + str(e))

        time.sleep(5)

        browser.quit()

        time.sleep(5)

        company_details = {
            'company_name': company_name,
            'country': country,
            'main_activity': main_activity,
            'address': address,
            'website': website,
            'email': email,
            'phone_number': phone_number
        }

        # Credentials
        host = "localhost"
        port = 27017
        username = ""
        password = ""
        uri = "mongodb://" + username + ":" + password + "@" + host + ":" + str(port)
        myclient = pymongo.MongoClient(uri)
        companydb = myclient["companydb"]
        europages = companydb["europages"]
        europages.insert_one(company_details)
        myclient.close()
        print(company_details)

    # ok
    def test_extract_all_details_for_all_company_from_all_page_results_into_mongodb(self):
        print('test_extract_all_details_for_all_company_from_all_page_results_into_mongodb')

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

        url_activity = "https://www.europages.fr/entreprises/cat-1-g%C3%A9n%C3%A9rateurs%20d'%C3%A9lectricit%C3%A9/" \
              "fabricant%20producteur/pg-1/g%C3%A9n%C3%A9rateurs%20d'%C3%A9lectricit%C3%A9.html"

        rt = RequestsTor()

        html_activity = rt.get(url_activity, headers=headers).content

        time.sleep(3)

        soup_activity = BeautifulSoup(html_activity, 'html.parser')

        number_of_pages = 0

        if soup_activity.find('span', {'class', 'ep-big-tab-button__count'}) is not None:
            number_of_pages_with_coma = int(
                soup_activity.find('span', {'class', 'ep-big-tab-button__count'}).text.replace(" ", "")
            ) / 30

            if int(str(number_of_pages_with_coma).split(".")[1][:1]) < 5:
                number_of_pages += round(number_of_pages_with_coma) + 1
                print('number_of_pages : ' + str(number_of_pages))
            elif int(str(number_of_pages_with_coma).split(".")[1][:1]) >= 5:
                number_of_pages += round(number_of_pages_with_coma)
                print('number_of_pages : ' + str(number_of_pages))
        else:
            print('no span class ep-big-tab-button__count')

        for i in range(1, number_of_pages + 1):
            user_agent = user_agent_rotator.get_random_user_agent()

            headers = {
                'User-Agent': user_agent
            }

            url_page_result = "https://www.europages.fr/entreprises/cat-1-g%C3%A9n%C3%A9rateurs%20d'%C3%A9lectricit%C3%A9/" \
              "fabricant%20producteur/pg-" + str(i) + "/g%C3%A9n%C3%A9rateurs%20d'%C3%A9lectricit%C3%A9.html"

            print('url_page_result : ' + url_page_result)

            html_page_result = rt.get(url_page_result, headers=headers).content

            time.sleep(3)

            soup_page_result = BeautifulSoup(html_page_result, 'html.parser')

            if soup_page_result.find('a', {'class', 'ep-ecard-serp__epage-link'}) is not None:
                urls = soup_page_result.find_all('a', {'class': 'ep-ecard-serp__epage-link'})

                for url in urls:
                    url_company = 'https://www.europages.fr' + url.get('href')

                    print('url_company : ' + url_company)

                    html_company = rt.get(url_company, headers=headers).content

                    time.sleep(3)

                    soup_company = BeautifulSoup(html_company, 'html.parser')

                    dom = etree.HTML(str(soup_company))

                    company_name = ''
                    country = ''
                    main_activity = ''
                    address = ''
                    website = ''
                    email = ''
                    phone_number = ''

                    try:
                        company_name += \
                        dom.xpath('/html/body/div[1]/div/div/div[1]/div[1]/div[2]/div[2]/div[1]/header/h1')[
                            0].text.replace('\n', '').replace('    ', '')
                    except Exception as e:
                        print('error company_name : ' + str(e))

                    try:
                        country += dom.xpath(
                            '/html/body/div[1]/div/div/div[1]/div[1]/div[2]/div[2]/div[1]/header/div[1]/p[1]/span[2]')[
                            0].text.replace('\n', '').replace('    ', '')
                    except Exception as e:
                        print('error country : ' + str(e))

                    try:
                        main_activity += dom.xpath(
                            '/html/body/div[1]/div/div/div[1]/div[1]/div[2]/div[2]/div[1]/header/div[1]/p[2]/span[2]')[
                            0].text.replace('\n', '').replace('    ', '')
                    except Exception as e:
                        print('error main_activity : ' + str(e))

                    try:
                        if soup_company.find('div', {'class': 'v-card__text'}) is not None:
                            address += soup_company.find_all('div', {'class': 'v-card__text'})[0].text \
                                .replace('Adresse', '') \
                                .replace('\n', '')
                    except Exception as e:
                        print('error address : ' + str(e))

                    try:
                        website += dom.xpath(
                            '/html/body/div[1]/div/div/div[1]/div[1]/div[2]/div[2]/div[1]/aside/div/div[1]/div[4]/a[1]/@href')[
                            0]
                    except Exception as e:
                        print('error website : ' + str(e))

                    try:
                        email += "'info@" + dom.xpath(
                            '/html/body/div[1]/div/div/div[1]/div[1]/div[2]/div[2]/div[1]/aside/div/div[1]/div[4]/a[1]/@href')[
                            0] \
                            .replace('https://www.', '') \
                            .replace('http://www.', '') + "',"
                    except Exception as e:
                        print('error email : ' + str(e))

                    time.sleep(5)

                    warnings.filterwarnings(
                        action="ignore",
                        message="unclosed",
                        category=ResourceWarning
                    )

                    time.sleep(5)

                    # with Firefox
                    options = Options()
                    options.headless = True
                    browser = webdriver.Firefox(
                        executable_path='C:\\Users\\Jason\\Dropbox\\1_Personnel\\1_Recurrentes\\3_Outils_Numeriques\\GitHub'
                                        '\\Cristal_Ball\\geckodriver.exe',
                        options=options
                    )

                    time.sleep(5)

                    # maximize window
                    browser.maximize_window()

                    time.sleep(5)

                    # open
                    browser.get(url_company)

                    time.sleep(5)

                    # Click on the 'Afficher les détails' button
                    try:
                        afficher_les_details_button = browser.find_element(
                            by=By.XPATH,
                            value='//*[@id="cookiescript_manage_wrap"]'
                        )
                        afficher_les_details_button.click()
                        print('afficher_les_details_button.click() clicked')
                    except Exception as e:
                        print('error afficher_les_details_button : ' + str(e))

                    time.sleep(5)

                    # Click on the 'Sauvegarder mes préférences' button
                    try:
                        sauvegarder_mes_preferences_button = browser.find_element(
                            by=By.XPATH,
                            value='//*[@id="cookiescript_save"]'
                        )
                        sauvegarder_mes_preferences_button.click()
                        print('sauvegarder_mes_preferences_button.click() clicked')
                    except Exception as e:
                        print('error sauvegarder_mes_preferences_button : ' + str(e))

                    time.sleep(5)

                    # Click on the 'Téléphone' button
                    try:
                        telephone_button = browser.find_element(
                            by=By.XPATH,
                            value='/html/body/div[1]/div/div/div[1]/div[1]/div[2]/div[2]/div[1]/aside/div/div[1]/div[4]/button'
                        )
                        telephone_button.click()
                        print('telephone_button.click() clicked')
                    except Exception as e:
                        print('error telephone_button : ' + str(e))

                    time.sleep(5)

                    # Click on the 'Afficher le numéro' button
                    try:
                        afficher_le_numero_button = browser.find_element(
                            by=By.XPATH,
                            value='/html/body/div[1]/div/div/div[4]/div/div/div[2]/div/div[1]/div/button'
                        )
                        afficher_le_numero_button.click()
                        print('afficher_le_numero_button.click() clicked')
                    except Exception as e:
                        print('error afficher_le_numero_button : ' + str(e))

                    time.sleep(5)

                    # Phone number text
                    try:
                        phone_number += browser.find_element(
                            by=By.XPATH,
                            value='/html/body/div[1]/div/div/div[4]/div/div/div[2]/div/div[1]/div/button/span/span'
                        ).text
                    except Exception as e:
                        print('error phone_number : ' + str(e))

                    time.sleep(5)

                    browser.quit()

                    time.sleep(5)

                    company_details = {
                        'company_name': company_name,
                        'country': country,
                        'main_activity': main_activity,
                        'address': address,
                        'website': website,
                        'email': email,
                        'phone_number': phone_number
                    }

                    # Credentials
                    host = "localhost"
                    port = 27017
                    username = ""
                    password = ""
                    uri = "mongodb://" + username + ":" + password + "@" + host + ":" + str(port)
                    myclient = pymongo.MongoClient(uri)
                    companydb = myclient["companydb"]
                    europages = companydb["europages"]
                    europages.insert_one(company_details)
                    myclient.close()
                    print(company_details)
            else:
                print('no urls')


if __name__ == '__main__':
    unittest.main()
