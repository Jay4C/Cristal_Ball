import time
from bs4 import BeautifulSoup
import requests
import pymysql.cursors
import unittest
from validate_email import validate_email


class UnitTestsDataMinerYellowPagesMonaco(unittest.TestCase):
    def test_extract_emails_from_all_page_of_results_for_one_activity_and_capital(self):
        url_search = "https://www.pagesjaunesmonaco.com/fr/monaco/restaurant/1/"
        html_search = requests.get(url_search)
        soup_search = BeautifulSoup(html_search.content, 'html.parser')

        number_of_pages = 0

        if soup_search.find('span', {'class': 'nbChars3 pull-right'}) is not None:
            number_of_pages_with_coma = int(soup_search.find('span', {'class': 'nbChars3 pull-right'})
                                            .text.replace(" résultats", "")) / 6

            if int(str(number_of_pages_with_coma).split(".")[1][:1]) < 5:
                number_of_pages += round(int(soup_search.find('span', {'class': 'nbChars3 pull-right'})
                                             .text.replace(" résultats", "")) / 6) + 1
                print('number_of_pages : ' + str(number_of_pages))

            elif int(str(number_of_pages_with_coma).split(".")[1][:1]) >= 5:
                number_of_pages += round(int(soup_search.find('span', {'class': 'nbChars3 pull-right'})
                                             .text.replace(" résultats", "")) / 6)
                print('number_of_pages : ' + str(number_of_pages))

        i_1 = 0

        for i in range(1, number_of_pages + 1):
            print("page : " + str(i))
            url_of_one_page_of_results = url_search[:-2] + str(i) + "/"
            print("url : " + url_of_one_page_of_results)
            time.sleep(2)

            # probleme de requete des contenus des pages
            html_of_one_page_of_results = requests.get(url_of_one_page_of_results)
            soup_of_one_page_of_results = BeautifulSoup(html_of_one_page_of_results.content, 'html.parser')

            if soup_of_one_page_of_results.find('div', {'class': 'col-sm-8 info-client col-result'}) is not None:
                results = soup_of_one_page_of_results.find_all('div', {'class': 'col-sm-8 info-client col-result'})
                print(results)
                for result in results:
                    if result.find('a') is not None:
                        all_a = result.find_all('a')
                        for each_a in all_a:
                            if each_a.get('href')[:7] == "mailto:":
                                email = "contact@" + each_a.get('href')[:7].split("@")[1]
                                print("email " + str(i_1) + " : " + email)
                                break

                            if each_a.get('href')[:33] != "https://www.pagesjaunesmonaco.com"\
                                    and each_a.get('href')[:4] != "tel:":
                                email = "contact@" + each_a.get('href')\
                                    .replace("http://www.", "")\
                                    .replace("https://www.", "")\
                                    .replace("www.", "")\
                                    .replace("/en", "")\
                                    .replace("/", "")
                                print("email " + str(i_1) + " : " + email)
                                break
                            else:
                                print("no email business")

                        i_1 += 1

                    else:
                        print('no tag a')
            else:
                print('sorry there is nothing')


if __name__ == '__main__':
    unittest.main()
