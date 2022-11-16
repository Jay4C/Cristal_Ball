import time
import unittest
import warnings

from bs4 import BeautifulSoup
import requests
import pymysql.cursors
import xlsxwriter
from requests_tor import RequestsTor
from selenium import webdriver
from selenium.webdriver import FirefoxProfile
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.options import Options


class UnitTestsDataMiningBMeeting(unittest.TestCase):
    def test_display_all_participants(self):
        print("test_display_all_participants")

        urls = [
        ]

        for url in urls:
            print(url)

            headers = {
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
            }

            html = requests.get(url, headers=headers)

            soup = BeautifulSoup(html.text, 'html.parser')

            if soup.find("em") is not None:
                all_em = soup.find_all("em")

                for em in all_em:
                    participant = em.text.lower()

                    print("participant : " + participant)

    def test_display_all_participants_with_tor(self):
        print("test_display_all_participants_with_tor")

        urls = [
        ]

        for url in urls:
            print(url)

            headers = {
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
            }

            rt = RequestsTor()

            html_with_tor = rt.get(url, headers=headers)

            soup = BeautifulSoup(html_with_tor.text, 'html.parser')

            if soup.find("em") is not None:
                all_em = soup.find_all("em")

                for em in all_em:
                    participant = em.text.lower()

                    print("participant : " + participant)

    def test_extract_all_participants(self):
        print("test_extract_all_participants")

        urls = [
        ]

        for url in urls:
            print(url)

            headers = {
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
            }

            html = requests.get(url, headers=headers)

            soup = BeautifulSoup(html.text, 'html.parser')

            if soup.find("em") is not None:
                all_em = soup.find_all("em")

                for em in all_em:
                    company = em.text.lower()

                    x = {
                        'company': company
                    }

                    try:
                        # Connect to the database
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
                                sql = "INSERT INTO `b_meeting` (`company`) VALUE (%s)"

                                cursor.execute(sql, x.get('company'))

                                connection.commit()

                                print('company : ' + x.get('company') + ' : ok')

                                connection.close()
                            except Exception as e:
                                print("The record already exists (company " + x.get('company') + ") : " + str(e))
                                connection.close()
                    except Exception as e:
                        print("Problem connection MySQL : " + str(e))

    def test_extract_all_participants_into_excel(self):
        print('test_extract_all_participants_into_excel')

        workbook = xlsxwriter.Workbook("contact_b_meeting_v2.xlsx")

        worksheet = workbook.add_worksheet('data')

        cell_format_yellow = workbook.add_format(
            {
                'bg_color': 'yellow',
                'border': 1,
                'align': 'justify',
                'valign': 'top'
            }
        )

        cell_format_green = workbook.add_format(
            {
                'bg_color': 'green',
                'border': 1,
                'align': 'justify',
                'valign': 'top'
            }
        )

        i = 1

        worksheet.write(0, 0, 'etablissment', cell_format_yellow)
        worksheet.write(0, 1, 'website', cell_format_yellow)
        worksheet.write(0, 2, 'email', cell_format_yellow)

        urls = [
            "https://www.bilderbergmeetings.org/meetings/meeting-2019/participants-2019",
            "https://www.bilderbergmeetings.org/meetings/meeting-2018/participants-2018",
            "https://www.bilderbergmeetings.org/meetings/meeting-2017/participants-2017",
            "https://www.bilderbergmeetings.org/meetings/meeting-2016/participants-2016-1"
        ]

        for url in urls:
            print(url)

            headers = {
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
            }

            rt = RequestsTor()

            html_with_tor = rt.get(url, headers=headers)

            soup = BeautifulSoup(html_with_tor.text, 'html.parser')

            if soup.find("em") is not None:
                all_em = soup.find_all("em")

                for em in all_em:
                    participant = em.text.lower()

                    print("participant : " + participant)

                    time.sleep(5)

                    search = participant

                    url = "https://duckduckgo.com/?q=" + search

                    warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

                    time.sleep(5)

                    binary = FirefoxBinary(r"C:\Users\DELL\Desktop\Tor Browser\Browser\firefox.exe")

                    profile = FirefoxProfile(
                        r"C:\Users\DELL\Desktop\Tor Browser\Browser\TorBrowser\Data\Browser\profile.default")

                    tor_proxy = "127.0.0.1:9150"

                    firefox_options = Options()
                    firefox_options.headless = True
                    firefox_options.add_argument('--proxy-server=socks5://%s' % tor_proxy)
                    browser = webdriver.Firefox(firefox_profile=profile, firefox_binary=binary,
                                                executable_path='..\\geckodriver.exe', options=firefox_options)

                    # maximize window
                    browser.maximize_window()

                    time.sleep(5)

                    # open
                    browser.get(url)
                    print("page opened")

                    time.sleep(15)

                    website = browser.find_element_by_xpath(
                        '//*[@id="r1-0"]'
                    ).get_attribute('data-domain')

                    email = "'info@" + website.replace('www.', '') + "',"

                    x = {
                        'website': website,
                        'email': email
                    }

                    print('x : ' + str(x))

                    worksheet.write(i, 0, participant, cell_format_green)
                    worksheet.write(i, 1, x.get('website'), cell_format_green)
                    worksheet.write(i, 2, x.get('email'), cell_format_green)

                    browser.close()
                    print("browser closed")

                    for i1 in range(10):
                        browser.service.process.kill()
                        browser.service.process.terminate()
                        print("browser service process killed : "
                              + str(i1))

                    time.sleep(5)

                    i += 1

        workbook.close()


if __name__ == '__main__':
    unittest.main()
