import unittest
import time
import requests
from bs4 import BeautifulSoup
import pymysql
import pymysql.cursors


class UnitTestsDataMiningAdecco(unittest.TestCase):
    # ok
    def test_extract_all_urls_from_one_result_page(self):
        print("test_extract_all_urls_from_one_result_page")

        url_result_page = "https://www.adecco.fr/resultats-offres-emploi?pageNum=2"

        # Request the content of a page from the url
        html = requests.get(url_result_page)

        time.sleep(3)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.content, 'html.parser')

        if soup.find("a", {'data-bind': "init,attr: { 'href': NavigationUrl }, click: $root.viewJobDetails.bind('    '.trimEnd())"}) is not None:
            all_urls = soup.find_all("a", {'data-bind': "init,attr: { 'href': NavigationUrl }, click: $root.viewJobDetails.bind('    '.trimEnd())"})

            i = 1

            for url in all_urls:
                print("link " + str(i) + " : " + url.get('href'))

                i += 1
        else:
            print("no offres")

    # ok
    def test_extract_all_urls_from_all_result_pages(self):
        print("test_extract_all_urls_from_all_result_pages")

        for i1 in range(1, 6195):
            url_result_page = "https://www.adecco.fr/resultats-offres-emploi?pageNum=" + str(i1)

            print("url_result_page : " + url_result_page)

            # Request the content of a page from the url
            html = requests.get(url_result_page)

            time.sleep(5)

            # Parse the content of html_doc
            soup = BeautifulSoup(html.content, 'html.parser')

            if soup.find("a", {'data-bind': "init,attr: { 'href': NavigationUrl }, click: $root.viewJobDetails.bind('    '.trimEnd())"}) is not None:
                all_urls = soup.find_all("a", {'data-bind': "init,attr: { 'href': NavigationUrl }, click: $root.viewJobDetails.bind('    '.trimEnd())"})

                i = 1

                for url in all_urls:
                    print("link " + str(i) + " : " + url.get('href'))

                    i += 1
            else:
                print("no offres")

    # ok
    def test_extract_all_urls_from_all_result_pages_into_mysql(self):
        print("test_extract_all_urls_from_all_result_pages_into_mysql")

        i = 1

        for i1 in range(1, 6195):
            url_result_page = "https://www.adecco.fr/resultats-offres-emploi?pageNum=" + str(i1)

            print("url_result_page : " + url_result_page)

            # Request the content of a page from the url
            html = requests.get(url_result_page)

            time.sleep(5)

            # Parse the content of html_doc
            soup = BeautifulSoup(html.content, 'html.parser')

            if soup.find("a", {'data-bind': "init,attr: { 'href': NavigationUrl }, click: $root.viewJobDetails.bind('    '.trimEnd())"}) is not None:
                all_urls = soup.find_all("a", {'data-bind': "init,attr: { 'href': NavigationUrl }, click: $root.viewJobDetails.bind('    '.trimEnd())"})

                for url in all_urls:
                    x = {
                        'url': url.get('href')
                    }

                    try:
                        connection = pymysql.connect(
                            host='localhost',
                            port=3306,
                            user='root',
                            password='azerAZER123098,,,',
                            db='adecco',
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor
                        )

                        with connection.cursor() as cursor:
                            try:
                                sql = "INSERT INTO `urls` (`url`) VALUE (%s)"

                                cursor.execute(sql, (
                                    x.get('url')
                                ))

                                connection.commit()

                                print(str(i) + ' _ Url : ' + x.get('url') + ' : ok')

                                connection.close()
                            except Exception as e:
                                print(str(i) + " _ The record already exists (url " + x.get('url') + ") : " + str(e))
                                connection.close()
                    except Exception as e:
                        print(str(i) + " _ Problem connection MySQL : " + str(e))

                    i += 1
            else:
                print("no offres")


if __name__ == '__main__':
    unittest.main()
