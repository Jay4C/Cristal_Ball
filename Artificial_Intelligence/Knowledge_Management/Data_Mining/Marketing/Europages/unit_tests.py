import time
import ssl
import warnings
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
from requests_tor import RequestsTor
import requests
import unittest
import subprocess
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem
from lxml import etree
from OpenSSL import SSL
import pymongo


class UnitTestsDataMinerMarketingEuropages(unittest.TestCase):
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

    #
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

        dom = etree.HTML(str(soup))

        address = ''

        try:
            address += dom.xpath('/html/body/div[1]/div/div/div[1]/div[1]/div[2]/div[2]/div[1]/aside/div/div[1]/div[3]')[0].text.replace('\n', '').replace('    ', '')
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

        # rt = requests
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


if __name__ == '__main__':
    unittest.main()
