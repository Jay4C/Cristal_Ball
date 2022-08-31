import time
import unittest
import requests
from bs4 import BeautifulSoup
import xlsxwriter


class UnitTestsDataMiningIndeed(unittest.TestCase):
    def test_extract_all_ad_link_from_one_page(self):
        print('test_extract_all_ad_link_from_one_page')

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://fr.indeed.com/jobs?q=d%C3%A9veloppeur%20python&l=%C3%8Ele-de-France&sc=0kf%3Ajt(permanent)%3B&start=10&vjk=438f7e1a055c9255"

        # Request the content of a page from the url
        html = requests.get(url, headers=headers)

        time.sleep(3)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.content, 'html.parser')

        if soup.find("h2", {"class": "jobTitle"}) is not None:
            all_h2 = soup.find_all("h2", {"class": "jobTitle"})

            for h2 in all_h2:
                link = "https://fr.indeed.com" + h2.find('a').get('href')
                print("link of the ad : " + link)
        else:
            print("no ads")

    def test_extract_all_ad_link_from_one_page_with_python_word_in_title(self):
        print('test_extract_all_ad_link_from_one_page_with_python_word_in_title')

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://fr.indeed.com/jobs?q=d%C3%A9veloppeur%20python&l=%C3%8Ele-de-France&sc=0kf%3Ajt(permanent)%3B&start=10&vjk=438f7e1a055c9255"

        # Request the content of a page from the url
        html = requests.get(url, headers=headers)

        time.sleep(3)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.content, 'html.parser')

        if soup.find("h2", {"class": "jobTitle"}) is not None:
            all_h2 = soup.find_all("h2", {"class": "jobTitle"})

            for h2 in all_h2:
                link = "https://fr.indeed.com" + h2.find('a').get('href')

                if 'python' in h2.find('a').find('span').text.lower():
                    print("yes for the link of the ad : " + link)
                else:
                    print("no for the link of the ad : " + link)
        else:
            print("no ads")

    def test_extract_all_ad_link_from_one_page_with_python_word_in_title_into_excel(self):
        print('test_extract_all_ad_link_from_one_page_with_python_word_in_title_into_excel')

        workbook = xlsxwriter.Workbook('dev_python_links.xlsx')

        worksheet = workbook.add_worksheet('data')

        i_row = 0

        worksheet.write(i_row, 0, 'links')

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://fr.indeed.com/jobs?q=d%C3%A9veloppeur%20python&l=%C3%8Ele-de-France&sc=0kf%3Ajt(permanent)%3B&start=10&vjk=438f7e1a055c9255"

        # Request the content of a page from the url
        html = requests.get(url, headers=headers)

        time.sleep(3)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.content, 'html.parser')

        if soup.find("h2", {"class": "jobTitle"}) is not None:
            all_h2 = soup.find_all("h2", {"class": "jobTitle"})

            for h2 in all_h2:
                link = "https://fr.indeed.com" + h2.find('a').get('href')

                if 'python' in h2.find('a').find('span').text.lower():
                    i_row += 1
                    print("yes for the link of the ad : " + link)
                    worksheet.write(i_row, 0, link)
                else:
                    print("no for the link of the ad : " + link)
        else:
            print("no ads")

        workbook.close()

    def test_extract_all_ad_link_from_all_pages_with_python_word_in_title(self):
        print('test_extract_all_ad_link_from_all_pages_with_python_word_in_title')

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        for i in range(0, 60):
            url = "https://fr.indeed.com/jobs?q=d%C3%A9veloppeur%20python&l=%C3%8Ele-de-France" \
                  "&sc=0kf%3Ajt(permanent)%3B&start=" + str(i*10)

            print('url : ' + url)

            # Request the content of a page from the url
            html = requests.get(url, headers=headers)

            time.sleep(5)

            # Parse the content of html_doc
            soup = BeautifulSoup(html.content, 'html.parser')

            if soup.find("h2", {"class": "jobTitle"}) is not None:
                all_h2 = soup.find_all("h2", {"class": "jobTitle"})

                for h2 in all_h2:
                    link = "https://fr.indeed.com" + h2.find('a').get('href')

                    if 'python' in h2.find('a').find('span').text.lower():
                        print("yes for the link of the ad : " + link)
                    else:
                        print("no for the link of the ad : " + link)
            else:
                print("no ads")

    def test_extract_all_ad_link_from_all_pages_with_python_word_in_title_into_excel(self):
        print('test_extract_all_ad_link_from_all_pages_with_python_word_in_title_into_excel')

        workbook = xlsxwriter.Workbook('dev_python_links.xlsx')

        worksheet = workbook.add_worksheet('data')

        i_row = 0

        worksheet.write(i_row, 0, 'links')

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        for i in range(0, 60):
            url = "https://fr.indeed.com/jobs?q=d%C3%A9veloppeur%20python&l=%C3%8Ele-de-France&sc=0kf%3Ajt(permanent)%3B&start=" + str(i * 10)

            print('url : ' + url)

            # Request the content of a page from the url
            html = requests.get(url, headers=headers)

            time.sleep(7)

            # Parse the content of html_doc
            soup = BeautifulSoup(html.content, 'html.parser')

            if soup.find("h2", {"class": "jobTitle"}) is not None:
                all_h2 = soup.find_all("h2", {"class": "jobTitle"})

                for h2 in all_h2:
                    link = "https://fr.indeed.com" + h2.find('a').get('href')

                    if 'python' in h2.find('a').find('span').text.lower():
                        i_row += 1
                        print("yes for the link of the ad : " + link)
                        worksheet.write(i_row, 0, link)
                    else:
                        print("no for the link of the ad : " + link)
            else:
                print("no ads")

        workbook.close()

    def test_extract_all_ad_link_from_all_pages_into_excel(self):
        print('test_extract_all_ad_link_from_all_pages_into_excel')

        workbook = xlsxwriter.Workbook('all_links.xlsx')

        worksheet = workbook.add_worksheet('data')

        i_row = 0

        worksheet.write(i_row, 0, 'links')

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        for i in range(0, 2):
            url = "https://fr.indeed.com/jobs?q=informatique&l=La%20R%C3%A9union&sc=0kf%3Ajt(permanent)%3B&start=" \
                  + str(i * 10)

            print('url : ' + url)

            # Request the content of a page from the url
            html = requests.get(url, headers=headers)

            time.sleep(7)

            # Parse the content of html_doc
            soup = BeautifulSoup(html.content, 'html.parser')

            if soup.find("h2", {"class": "jobTitle"}) is not None:
                all_h2 = soup.find_all("h2", {"class": "jobTitle"})

                for h2 in all_h2:
                    link = "https://fr.indeed.com" + h2.find('a').get('href')
                    i_row += 1
                    worksheet.write(i_row, 0, link)
                    print('link : ' + link)
            else:
                print("no ads")

        workbook.close()


if __name__ == '__main__':
    unittest.main()
