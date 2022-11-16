import unittest
import time
import requests
from bs4 import BeautifulSoup
import pymysql
import pymysql.cursors


class UnitTestsDataMiningFreelanceInfo(unittest.TestCase):
    # ok
    def test_extract_all_pages_from_one_result_page(self):
        print("test_extract_all_pages_from_one_result_page")

        url_result_page = "https://www.freelance-info.fr/missions?keywords=d%C3%A9veloppeur%20python&page=2"

        # Request the content of a page from the url
        html = requests.get(url_result_page)

        time.sleep(3)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.content, 'html.parser')

        if soup.select("#offre") is not None:
            print("offres ok")

            all_offre = soup.select("#offre")

            i = 1

            for offre in all_offre:
                print("link " + str(i) + " : https://www.freelance-info.fr" + offre.select_one("#titre-mission").find('a').get('href'))

                i += 1
        else:
            print("no offres")

    # ok
    def test_extract_all_pages_from_all_result_page(self):
        print("test_extract_all_pages_from_all_result_page")

        i = 1

        # 24
        for x in range(1, 24):
            print("result page : " + str(x))

            url_result_page = "https://www.freelance-info.fr/missions?keywords=d%C3%A9veloppeur%20python&page=" + str(x)

            # Request the content of a page from the url
            html = requests.get(url_result_page)

            time.sleep(3)

            # Parse the content of html_doc
            soup = BeautifulSoup(html.content, 'html.parser')

            if soup.select("#offre") is not None:
                print("offres ok")

                all_offre = soup.select("#offre")

                for offre in all_offre:
                    print("link " + str(i) + " : https://www.freelance-info.fr"
                          + offre.select_one("#titre-mission").find('a').get('href'))

                    i += 1
            else:
                print("no offres")

    # ok
    def test_extract_email_company_from_one_ad_page(self):
        print("test_extract_email_company_from_one_ad_page")

        url_result_page = "https://www.freelance-info.fr/mission/developpeur-python-back-end-h-f-1654685?hl=d%C3%A9veloppeur%20python"

        # Request the content of a page from the url
        html = requests.get(url_result_page)

        time.sleep(3)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.content, 'html.parser')

        if soup.find("div", {'class': 'textnoir9'}) is not None:
            publication = soup.find("div", {'class': 'textnoir9'}).text.lower()\
                .replace("publiée le ", "").replace("/", "").replace(" par ", "")\
                .replace("0", "").replace("1", "").replace("2", "").replace("3", "").replace("4", "")\
                .replace("5", "").replace("6", "").replace("7", "").replace("8", "").replace("9", "").replace(" ", "")\
                .replace("\n", "")

            email = "contact@" + publication + ".fr"

            print('email : ' + email)
        else:
            print('no div class textnoir9')

    # ok
    def test_extract_all_email_company_from_one_result_page(self):
        print("test_extract_all_pages_from_one_result_page")

        url_result_page = "https://www.freelance-info.fr/missions?keywords=d%C3%A9veloppeur%20python&page=2"

        # Request the content of a page from the url
        html = requests.get(url_result_page)

        time.sleep(3)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.content, 'html.parser')

        if soup.select("#offre") is not None:
            print("offres ok")

            all_offre = soup.select("#offre")

            i = 1

            for offre in all_offre:
                url_ad = "https://www.freelance-info.fr" + offre.select_one("#titre-mission").find('a').get('href')

                print("link " + str(i) + " : " + url_ad)

                i += 1

                # Request the content of a page from the url
                html_ad = requests.get(url_ad)

                time.sleep(3)

                # Parse the content of html_doc
                soup_ad = BeautifulSoup(html_ad.content, 'html.parser')

                if soup_ad.find("div", {'class': 'textnoir9'}) is not None:
                    publication = soup_ad.find("div", {'class': 'textnoir9'}).text.lower() \
                        .replace("publiée le ", "").replace("/", "").replace(" par ", "") \
                        .replace("0", "").replace("1", "").replace("2", "").replace("3", "").replace("4", "") \
                        .replace("5", "").replace("6", "").replace("7", "").replace("8", "").replace("9", "")\
                        .replace(" ", "").replace("\n", "")

                    email = "contact@" + publication + ".fr"

                    print('email ' + str(i) + " : " + email)
                else:
                    print('no div class textnoir9')
        else:
            print("no offres")

    # ok
    def test_extract_all_email_company_from_all_result_page(self):
        print("test_extract_all_email_company_from_all_result_page")

        i = 1

        for x in range(1, 950):
            print("result page : " + str(x))

            url_result_page = "https://www.freelance-info.fr/missions?page=" + str(x)

            # Request the content of a page from the url
            html = requests.get(url_result_page)

            time.sleep(3)

            # Parse the content of html_doc
            soup = BeautifulSoup(html.content, 'html.parser')

            if soup.select("#offre") is not None:
                print("offres ok")

                all_offre = soup.select("#offre")

                for offre in all_offre:
                    url_ad = "https://www.freelance-info.fr" + offre.select_one("#titre-mission").find('a').get('href')

                    print("link " + str(i) + " : " + url_ad)

                    # Request the content of a page from the url
                    html_ad = requests.get(url_ad)

                    time.sleep(3)

                    # Parse the content of html_doc
                    soup_ad = BeautifulSoup(html_ad.content, 'html.parser')

                    if soup_ad.find("div", {'class': 'textnoir9'}) is not None:
                        publication = soup_ad.find("div", {'class': 'textnoir9'}).text.lower() \
                            .replace("publiée le ", "").replace("/", "").replace(" par ", "") \
                            .replace("0", "").replace("1", "").replace("2", "").replace("3", "").replace("4", "") \
                            .replace("5", "").replace("6", "").replace("7", "").replace("8", "").replace("9", "") \
                            .replace(" ", "").replace("\n", "")

                        email = "contact@" + publication + ".fr"

                        print('email ' + str(i) + " : " + email)
                    else:
                        print('no div class textnoir9')

                    i += 1
            else:
                print("no offres")

    # ok
    def test_extract_all_email_company_from_all_result_page_into_mysql(self):
        print("test_extract_all_email_company_from_all_result_page_into_mysql")

        i = 1

        for x in range(1, 950):
            print("result page : " + str(x))

            url_result_page = "https://www.freelance-info.fr/missions?page=" + str(x)

            # Request the content of a page from the url
            html = requests.get(url_result_page)

            time.sleep(3)

            # Parse the content of html_doc
            soup = BeautifulSoup(html.content, 'html.parser')

            if soup.select("#offre") is not None:
                all_offre = soup.select("#offre")

                for offre in all_offre:
                    url_ad = "https://www.freelance-info.fr" + offre.select_one("#titre-mission").find('a').get('href')

                    # Request the content of a page from the url
                    html_ad = requests.get(url_ad)

                    time.sleep(3)

                    # Parse the content of html_doc
                    soup_ad = BeautifulSoup(html_ad.content, 'html.parser')

                    if soup_ad.find("div", {'class': 'textnoir9'}) is not None:
                        publication = soup_ad.find("div", {'class': 'textnoir9'}).text.lower() \
                            .replace("publiée le ", "").replace("/", "").replace(" par ", "") \
                            .replace("0", "").replace("1", "").replace("2", "").replace("3", "").replace("4", "") \
                            .replace("5", "").replace("6", "").replace("7", "").replace("8", "").replace("9", "") \
                            .replace(" ", "").replace("\n", "")

                        email = "contact@" + publication + ".fr"

                        x = {
                            'email': email
                        }

                        try:
                            connection = pymysql.connect(
                                host='localhost',
                                port=3306,
                                user='root',
                                password='azerAZER123098,,,',
                                db='freelance_info',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor
                            )

                            with connection.cursor() as cursor:
                                try:
                                    sql = "INSERT INTO `emails` (`email`) VALUE (%s)"

                                    cursor.execute(sql, (
                                        x.get('email')
                                    ))

                                    connection.commit()

                                    print(str(i) + ' _ Email : ' + x.get('email') + ' : ok')

                                    connection.close()
                                except Exception as e:
                                    print(str(i) + " _ The record already exists (email " + x.get('email')
                                          + ") : "
                                          + str(e))
                                    connection.close()
                        except Exception as e:
                            print(str(i) + " _ Problem connection MySQL : " + str(e))
                    else:
                        print('no div class textnoir9')

                    i += 1
            else:
                print("no offres")

    # ok
    def test_extract_all_url_ad_from_all_result_page_into_mysql(self):
        print("test_extract_all_url_ad_from_all_result_page_into_mysql")

        i = 1

        for x in range(1, 32):
            print("result page : " + str(x))

            url_result_page = "https://www.freelance-info.fr/missions?keywords=d%C3%A9veloppeur%20python&page=" + str(x)

            # Request the content of a page from the url
            html = requests.get(url_result_page)

            time.sleep(3)

            # Parse the content of html_doc
            soup = BeautifulSoup(html.content, 'html.parser')

            if soup.select("#offre") is not None:
                all_offre = soup.select("#offre")

                for offre in all_offre:
                    url_ad = "https://www.freelance-info.fr" + offre.select_one("#titre-mission").find('a').get('href')

                    x = {
                        'url': url_ad
                    }

                    try:
                        connection = pymysql.connect(
                            host='localhost',
                            port=3306,
                            user='root',
                            password='azerAZER123098,,,',
                            db='freelance_info',
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
