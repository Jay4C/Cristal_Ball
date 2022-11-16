import time
from bs4 import BeautifulSoup
import requests
import pymysql.cursors
import unittest
from validate_email import validate_email
from fake_useragent import UserAgent


class UnitTestsDataMinerYellowPagesHongrie(unittest.TestCase):
    def test_extract_one_email(self):
        url = "https://aranyoldalak.hu/szallashelyek-es-vendeglatok-es-turizmus/szallodak/hotel-papillon7.htm"

        ua = UserAgent()
        ua.update()
        header = {'User-Agent': str(ua.chrome)}

        # Request the content of a page from the url
        html = requests.get(url, headers=header)
        print(html.content)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.content, 'html.parser')

        if soup.find('span', {'itemprop': 'email'}) is not None:
            email = "info@" + soup.find('span', {'itemprop': 'email'}).get('content').split("@")[1]
            print("email : " + email)
        else:
            print('no email business')

    def test_extract_emails_from_all_page_of_results_for_one_activity_and_capital(self):
        activity = "https://aranyoldalak.hu/ingatlan-penz-es-jog-tanacsadas/uegyved"
        city = "budapest"
        url_search = activity + "/" + city + "/"
        html_search = requests.get(url_search)
        print(html_search.content)
        soup_search = BeautifulSoup(html_search.content, 'html.parser')
        number_of_pages = 0

        if soup_search.find('div', {'class': 'list-ordering'}) is not None:
            if soup_search.find('div', {'class': 'list-ordering'})\
                    .find('span', {'class': 'label counter hidden-xs'}) is not None:
                number_of_pages += int(soup_search.find('div', {'class': 'list-ordering clearfix'})
                                       .find('span', {'class': 'label counter hidden-xs'}).text
                                       .replace(' oldal', '').split("/")[1])
                print('number of pages : ' + str(number_of_pages))
            else:
                print("no counter")
        else:
            print("no list ordering")

        i_1 = 0

        if number_of_pages > 1:
            for i in range(1, number_of_pages+1):
                url_of_one_page_of_results = activity + "/" + city + "/" + str(i) + "-oldal/"
                print(url_of_one_page_of_results)
                time.sleep(2)
                html_of_one_page_of_results = requests.get(url_of_one_page_of_results)
                soup_of_one_page_of_results = BeautifulSoup(html_of_one_page_of_results.content, 'html.parser')

                if soup_of_one_page_of_results.find('div', {'class': 'content-item'}) is not None:
                    for result_item in soup_of_one_page_of_results.find_all('div', {'class': 'content-item'}):
                        if result_item.find('div', {'class': 'profile-card-data'}) is not None:
                            i_1 += 1

                            url_result = "https://aranyoldalak.hu" + result_item\
                                .find('div', {'class': 'profile-card-data'})\
                                .find('h3', {'class': 'profile-card-title'})\
                                .find('a')\
                                .get('href')

                            # Request the content of a page from the url
                            html = requests.get(url_result)

                            # Parse the content of html_doc
                            soup = BeautifulSoup(html.content, 'html.parser')

                            if soup.find('span', {'itemprop': 'email'}) is not None:
                                email = "info@" + soup.find('span', {'itemprop': 'email'})\
                                    .get('content')\
                                    .split("@")[1]
                                print(str(i_1) + " email : " + email)
                            else:
                                print(str(i_1) + " no email business")
                        else:
                            print(str(i_1) + " no url")
                else:
                    print('sorry there is nothing')

    def test_extract_emails_from_all_page_of_results_for_all_activities_and_capitals(self):
        activites = [
            {'id': '1', 'url': 'labour'}
            # {'id': '2', 'url': 'real+estate'},
            # {'id': '3', 'url': 'recruitment'},
            # {'id': '4', 'url': 'software'},
            # {'id': '5', 'url': 'hotel'},
            # {'id': '6', 'url': 'landlord'},
            # {'id': '7', 'url': 'cleaning'},
            # {'id': '8', 'url': 'association'},
            # {'id': '9', 'url': 'financial'},
            # {'id': '10', 'url': 'restaurant'},
            # {'id': '11', 'url': 'building'},
            # {'id': '12', 'url': 'hairdresser'},
            # {'id': '13', 'url': 'florist'},
            # {'id': '14', 'url': 'locksmith'},
            # {'id': '15', 'url': 'bakery'},
            # {'id': '16', 'url': 'insurance'},
            # {'id': '17', 'url': 'pharmacy'},
            # {'id': '18', 'url': 'moving'},
            # {'id': '19', 'url': 'electricity'},
            # {'id': '20', 'url': 'plumbing'},
            # {'id': '21', 'url': 'security'},
            # {'id': '22', 'url': 'lawyer'},
            # {'id': '23', 'url': 'bank'},
            # {'id': '24', 'url': 'garage'},
            # {'id': '25', 'url': 'dentist'},
            # {'id': '26', 'url': 'doctor'},
            # {'id': '27', 'url': 'accounting'},
            # {'id': '28', 'url': 'store'},
            # {'id': '29', 'url': 'notary'},
            # {'id': '30', 'url': 'jeweller'},
            # {'id': '31', 'url': 'tailor'},
            # {'id': '32', 'url': 'meat'},
            # {'id': '33', 'url': 'library'},
            # {'id': '34', 'url': 'architect'}
        ]

        capitales_du_monde = [
            {'id': '238', 'nom': 'gibraltar'}
        ]

        try:
            for capitale in capitales_du_monde:
                for activite in activites:
                    try:
                        activity = activite.get('url')
                        url_search = "https://gibyellow.gi/result?type=business&query=" + activity + "&page=1"
                        html_search = requests.get(url_search)
                        soup_search = BeautifulSoup(html_search.content, 'html.parser')
                        number_of_pages = 0

                        if soup_search.select_one('#result-header') is not None:
                            if soup_search.select_one('#result-header').find('em') is not None:
                                number_of_pages_with_coma = int(soup_search.select_one('#result-header')
                                                                .find('em')
                                                                .text
                                                                .replace("(", "")
                                                                .replace(" results)", "")) / 10

                                if int(str(number_of_pages_with_coma).split(".")[1][:1]) < 5:
                                    number_of_pages += round(number_of_pages_with_coma) + 1
                                    print('number_of_pages : ' + str(number_of_pages))

                                elif int(str(number_of_pages_with_coma).split(".")[1][:1]) >= 5:
                                    number_of_pages += round(number_of_pages_with_coma)
                                    print('number_of_pages : ' + str(number_of_pages))
                            else:
                                print("no text result header")
                        else:
                            print("no result header")

                        i_1 = 0

                        for i in range(1, number_of_pages + 1):
                            url_of_one_page_of_results = url_search[:-1] + str(i)
                            print(url_of_one_page_of_results)
                            time.sleep(2)
                            html_of_one_page_of_results = requests.get(url_of_one_page_of_results)
                            soup_of_one_page_of_results = BeautifulSoup(html_of_one_page_of_results.content,
                                                                        'html.parser')

                            if soup_of_one_page_of_results.find('div', {'class': 'panel'}) is not None:
                                for result_item in soup_of_one_page_of_results.find_all('div', {'class': 'panel'}):
                                    if result_item.find('a', {'class': 'btn btn-warning yellow'}) is not None:
                                        i_1 += 1

                                        url_result = result_item\
                                            .find('a', {'class': 'btn btn-warning yellow'})\
                                            .get('href')

                                        # Request the content of a page from the url
                                        html = requests.get(url_result)

                                        # Parse the content of html_doc
                                        soup = BeautifulSoup(html.content, 'html.parser')

                                        if soup.find('p', {'itemprop': 'email'}) is not None:
                                            if soup.find('p', {'itemprop': 'email'}).find('a') is not None:
                                                email = "info@" + soup\
                                                    .find('p', {'itemprop': 'email'})\
                                                    .find('a')\
                                                    .text\
                                                    .split("@")[1]

                                                try:
                                                    if validate_email(email, verify=True) != False:

                                                        connection = pymysql.connect(
                                                            host='localhost',
                                                            port=3306,
                                                            user='root',
                                                            password='v2HJJzexYxlp0D0So77ztwMOKEKu97@@@@@@',
                                                            db='contacts_professionnels',
                                                            charset='utf8mb4',
                                                            cursorclass=pymysql.cursors.DictCursor
                                                        )

                                                        with connection.cursor() as cursor:
                                                            try:
                                                                sql = "INSERT INTO `emails` (" \
                                                                      "`id_activite`, " \
                                                                      "`id_capitale_du_monde`, " \
                                                                      "`email`) VALUE (%s, %s, %s)"
                                                                cursor.execute(sql, (
                                                                    activite.get('id'),
                                                                    capitale.get('id'),
                                                                    email))
                                                                connection.commit()
                                                                print(str(i_1) + " The record is stored : " + email)
                                                                connection.close()
                                                            except:
                                                                print(
                                                                    str(i_1) + " The record already exists : " + email)
                                                                connection.close()
                                                    else:
                                                        print(str(i_1) + " The email : " + email + " doesn't exist.")
                                                except:
                                                    print(str(i_1) + " An error with the email : " + email)
                                            else:
                                                print(str(i_1) + ' no email business 2')
                                        else:
                                            print(str(i_1) + ' no email business 1')
                                    else:
                                        print("no more info")
                            else:
                                print('sorry there is nothing')
                    except:
                        print("There is an error connection at url")
        finally:
            print('done')


if __name__ == '__main__':
    unittest.main()
