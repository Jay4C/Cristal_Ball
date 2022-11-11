import unittest
import pymongo
from requests_tor import RequestsTor
from bs4 import BeautifulSoup
import time
import requests


class UnitTestsDataMiningSMWithDarkWeb(unittest.TestCase):
    # ok
    def test_extract_the_phone_number_from_one_url(self):

        print('test_extract_the_phone_number_from_one_url')

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = ""

        rt = RequestsTor()

        html = rt.get(url, headers=headers).content

        time.sleep(3)

        soup = BeautifulSoup(html, 'html.parser')

        if soup.select("#thephone") is not None:
            pn = soup.select_one("#thephone").text
            print("pn : " + str(pn))
        else:
            print("no pn")

    # ok
    def test_extract_the_city_from_one_url(self):
        print('test_extract_the_city_from_one_url')

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = ""

        rt = RequestsTor()

        html = rt.get(url, headers=headers).content

        time.sleep(3)

        soup = BeautifulSoup(html, 'html.parser')

        if soup.select_one("#table_right").find('ul', {'class', 'working-cities'}).find_all("li")[0].find_all('span')[1] is not None:
            city = soup.select_one("#table_right").find('ul', {'class', 'working-cities'}).find_all("li")[0].find_all('span')[1].text
            print("city : " + str(city))
        else:
            print("no city")

    #
    def test_extract_the_age_from_one_url(self):
        print('test_extract_the_age_from_one_url')

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = ""

        rt = RequestsTor()

        html = rt.get(url, headers=headers).content

        time.sleep(3)

        soup = BeautifulSoup(html, 'html.parser')

        if soup.select_one("#table_left") is not None:
            pn = soup.select_one("#thephone").text
            print("pn : " + str(pn))
        else:
            print("no pn")

    # ok
    def test_extract_dataset_from_one_url(self):
        print('test_extract_dataset_from_one_url')

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = ""

        rt = RequestsTor()

        html = rt.get(url, headers=headers).content

        time.sleep(3)

        soup = BeautifulSoup(html, 'html.parser')

        # dataset
        pn = ""
        city = ""

        if soup.select_one("#table_right").find('ul', {'class', 'working-cities'}).find_all("li")[0].find_all('span')[1] is not None:
            city += soup.select_one("#table_right").find('ul', {'class', 'working-cities'}).find_all("li")[0].find_all('span')[
                1].text

        if soup.select("#thephone") is not None:
            pn += soup.select_one("#thephone").text

        dataset = {
            'url': url,
            'city': city,
            'pn': pn
        }

        print('dataset : ' + str(dataset))

    # ok
    def test_extract_urls_from_one_page(self):
        print("test_extract_urls_from_one_page")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://www.sexemodel.com/profiles/search_box/1/sort/0/city_ids/70869/base_city/1/gender/f/ageend/25/heightstart/135/heightend/190/weightstart/40/weightend/80/distance/0/"

        rt = RequestsTor()

        html = rt.get(url, headers=headers).content

        time.sleep(3)

        soup = BeautifulSoup(html, 'html.parser')

        if soup.find("div", {'class': 'search_user_container'}) is not None:
            all_div = soup.find_all("div", {'class': 'search_user_container'})

            for div in all_div:
                if div.find('a', {'class', 'showname'}) is not None:
                    url = 'https://www.sexemodel.com' + div.find_all('a', {'class', 'showname'})[0].get('href')

                    print('url : ' + str(url))
        else:
            print('no urls')

    # ok
    def test_extract_datasets_for_all_urls_from_one_page(self):
        print('test_extract_datasets_for_all_urls_from_one_page')

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        rt = RequestsTor()

        try:
            page = "https://www.sexemodel.com/profiles/search_box/1/sort/0/city_ids/70869/base_city/1/gender/f/ageend/25/heightstart/135/heightend/190/weightstart/40/weightend/80/distance/0/"

            print('page : ' + str(page))

            html = rt.get(page, headers=headers).content

            time.sleep(3)

            soup = BeautifulSoup(html, 'html.parser')

            if soup.find("div", {'class': 'search_user_container'}) is not None:
                all_div = soup.find_all("div", {'class': 'search_user_container'})

                for div in all_div:
                    try:
                        if div.find('a', {'class', 'showname'}) is not None:
                            url = 'https://www.sexemodel.com' + div.find_all('a', {'class', 'showname'})[0].get('href')

                            html_dataset = rt.get(url, headers=headers).content

                            time.sleep(3)

                            soup_dataset = BeautifulSoup(html_dataset, 'html.parser')

                            # dataset
                            pn = ""
                            city = ""

                            if soup_dataset.select_one("#table_right").find('ul', {'class', 'working-cities'}).find_all("li")[0].find_all('span')[1] is not None:
                                city += soup_dataset.select_one("#table_right").find('ul', {'class', 'working-cities'}).find_all("li")[
                                    0].find_all('span')[
                                    1].text

                            if soup_dataset.select("#thephone") is not None:
                                pn += soup_dataset.select_one("#thephone").text

                            dataset = {
                                'url': url,
                                'city': city,
                                'pn': pn
                            }

                            print('dataset : ' + str(dataset))
                    except Exception as e:
                        print('error div : ' + str(e))
            else:
                print('no urls')
        except Exception as e:
            print('error : ' + str(e))

    # ok
    def test_extract_datasets_for_all_urls_from_one_page_into_mongodb(self):
        print('test_extract_datasets_for_all_urls_from_one_page_into_mongodb')

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        rt = RequestsTor()

        try:
            page = "https://www.sexemodel.com/profiles/search_box/1/sort/0/city_ids/70869/base_city/1/gender/f/ageend/25/heightstart/135/heightend/190/weightstart/40/weightend/80/distance/0/"

            print('page : ' + str(page))

            html = rt.get(page, headers=headers).content

            time.sleep(3)

            soup = BeautifulSoup(html, 'html.parser')

            if soup.find("div", {'class': 'search_user_container'}) is not None:
                all_div = soup.find_all("div", {'class': 'search_user_container'})

                for div in all_div:
                    try:
                        if div.find('a', {'class', 'showname'}) is not None:
                            url = 'https://www.sexemodel.com' + div.find_all('a', {'class', 'showname'})[0].get('href')

                            html_dataset = rt.get(url, headers=headers).content

                            time.sleep(3)

                            soup_dataset = BeautifulSoup(html_dataset, 'html.parser')

                            # dataset
                            pn = ""
                            city = ""

                            if soup_dataset.select_one("#table_right").find('ul', {'class', 'working-cities'}).find_all("li")[0].find_all('span')[1] is not None:
                                city += soup_dataset.select_one("#table_right").find('ul', {'class', 'working-cities'}).find_all("li")[
                                    0].find_all('span')[
                                    1].text

                            if soup_dataset.select("#thephone") is not None:
                                pn += soup_dataset.select_one("#thephone").text

                            dataset = {
                                'url': url,
                                'city': city,
                                'pn': pn
                            }

                            # Credentials
                            host = "localhost"
                            port = 27017
                            username = ""
                            password = ""
                            database = "mesdamesdb"

                            uri = "mongodb://" + username + ":" + password + "@" + host + ":" + str(port) + "/" + database
                            myclient = pymongo.MongoClient(uri)
                            mesdamesdb = myclient["mesdamesdb"]
                            mesdames_c = mesdamesdb["mesdames_c"]
                            mesdames_c.insert_one(dataset)

                            print(str(dataset))

                            myclient.close()
                    except Exception as e:
                        print('error div : ' + str(e))
            else:
                print('no urls')
        except Exception as e:
            print('error : ' + str(e))

    # ok
    def test_extract_urls_from_all_pages(self):
        print('test_extract_urls_from_all_pages')

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        rt = RequestsTor()

        for i in range(1, 7):
            try:
                page = "" + str(i) + ".html"

                print('page : ' + str(page))

                time.sleep(3)

                html = rt.get(page, headers=headers).content

                soup = BeautifulSoup(html, 'html.parser')

                if soup.find("div", {'class': 'search_user_container'}) is not None:
                    all_div = soup.find_all("div", {'class': 'search_user_container'})

                    for div in all_div:
                        if div.find('a', {'class', 'showname'}) is not None:
                            url = '' + div.find_all('a', {'class', 'showname'})[0].get('href')

                            print('url : ' + str(url))
                else:
                    print('no urls')
            except Exception as e:
                print('error : ' + str(e))

    # ok
    def test_extract_datasets_for_urls_from_all_pages(self):
        print('test_extract_datasets_for_urls_from_all_pages')

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        rt = RequestsTor()

        for i in range(1, 7):
            try:
                page = "" + str(i) + ".html"

                print('page : ' + str(page))

                html = rt.get(page, headers=headers).content

                time.sleep(3)

                soup = BeautifulSoup(html, 'html.parser')

                if soup.find("div", {'class': 'search_user_container'}) is not None:
                    all_div = soup.find_all("div", {'class': 'search_user_container'})

                    for div in all_div:
                        try:
                            if div.find('a', {'class', 'showname'}) is not None:
                                url = '' + div.find_all('a', {'class', 'showname'})[0].get('href')

                                html_dataset = rt.get(url, headers=headers).content

                                time.sleep(3)

                                soup_dataset = BeautifulSoup(html_dataset, 'html.parser')

                                # dataset
                                pn = ""
                                city = ""

                                if soup_dataset.select_one("#table_right").find('ul', {'class', 'working-cities'}).find_all("li")[0].find_all('span')[1] is not None:
                                    city += soup_dataset.select_one("#table_right").find('ul', {'class', 'working-cities'}).find_all("li")[
                                        0].find_all('span')[
                                        1].text

                                if soup_dataset.select("#thephone") is not None:
                                    pn += soup_dataset.select_one("#thephone").text

                                dataset = {
                                    'url': url,
                                    'city': city,
                                    'pn': pn
                                }

                                print('dataset : ' + str(dataset))
                        except Exception as e:
                            print('error div : ' + str(e))
                else:
                    print('no urls')
            except Exception as e:
                print('error : ' + str(e))


class UnitTestsDataMiningSMWithClearWeb(unittest.TestCase):
    # ok
    def test_extract_datasets_for_urls_from_all_pages(self):
        print('test_extract_datasets_for_urls_from_all_pages')

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        rt = requests

        for i in range(1, 7):
            try:
                page = "" + str(i) + ".html"

                print('page : ' + str(page))

                html = rt.get(page, headers=headers).content

                time.sleep(3)

                soup = BeautifulSoup(html, 'html.parser')

                if soup.find("div", {'class': 'search_user_container'}) is not None:
                    all_div = soup.find_all("div", {'class': 'search_user_container'})

                    for div in all_div:
                        try:
                            if div.find('a', {'class', 'showname'}) is not None:
                                url = '' + div.find_all('a', {'class', 'showname'})[0].get(
                                    'href')

                                html_dataset = rt.get(url, headers=headers).content

                                time.sleep(3)

                                soup_dataset = BeautifulSoup(html_dataset, 'html.parser')

                                # dataset
                                pn = ""
                                city = ""

                                if soup_dataset.select_one("#table_right").find('ul',
                                                                                {'class', 'working-cities'}).find_all(
                                        "li")[0].find_all('span')[1] is not None:
                                    city += soup_dataset.select_one("#table_right").find('ul', {'class',
                                                                                                'working-cities'}).find_all(
                                        "li")[
                                        0].find_all('span')[
                                        1].text

                                if soup_dataset.select("#thephone") is not None:
                                    pn += soup_dataset.select_one("#thephone").text

                                dataset = {
                                    'url': url,
                                    'city': city,
                                    'pn': pn
                                }

                                print('dataset : ' + str(dataset))
                        except Exception as e:
                            print('error div : ' + str(e))
                else:
                    print('no urls')
            except Exception as e:
                print('error : ' + str(e))

    # ok
    def test_extract_datasets_for_specific_city_from_all_pages(self):
        print('test_extract_datasets_for_specific_city_from_all_pages')

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        rt = RequestsTor()
        # rt = requests

        for i in range(1, 7):
            try:
                page = "" + str(i) + ".html"

                print('page : ' + str(page))

                html = rt.get(page, headers=headers).content

                time.sleep(3)

                soup = BeautifulSoup(html, 'html.parser')

                if soup.find("div", {'class': 'search_user_container'}) is not None:
                    all_div = soup.find_all("div", {'class': 'search_user_container'})

                    for div in all_div:
                        try:
                            if div.find('a', {'class', 'showname'}) is not None:
                                url = '' + div.find_all('a', {'class', 'showname'})[0].get(
                                    'href')

                                html_dataset = rt.get(url, headers=headers).content

                                time.sleep(3)

                                soup_dataset = BeautifulSoup(html_dataset, 'html.parser')

                                # dataset
                                pn = ""
                                city = ""

                                if soup_dataset.select_one("#table_right").find('ul',
                                                                                {'class', 'working-cities'}).find_all(
                                        "li")[0].find_all('span')[1] is not None:
                                    city += soup_dataset.select_one("#table_right").find('ul', {'class',
                                                                                                'working-cities'}).find_all(
                                        "li")[
                                        0].find_all('span')[
                                        1].text

                                    if city == "":
                                        if soup_dataset.select("#thephone") is not None:
                                            pn += soup_dataset.select_one("#thephone").text

                                            dataset = {
                                                'url': url,
                                                'city': city,
                                                'pn': pn
                                            }

                                            print('dataset : ' + str(dataset))
                                    else:
                                        print('not in the city')
                        except Exception as e:
                            print('error div : ' + str(e))
                else:
                    print('no urls')
            except Exception as e:
                print('error : ' + str(e))

    # ok
    def test_extract_datasets_for_specific_city_from_all_pages_into_mongodb(self):
        print('test_extract_datasets_for_specific_city_from_all_pages')

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        rt = RequestsTor()
        # rt = requests

        for i in range(1, 2):
            try:
                page = "" + str(i) + ".html"

                print('page : ' + str(page))

                html = rt.get(page, headers=headers).content

                time.sleep(3)

                soup = BeautifulSoup(html, 'html.parser')

                if soup.find("div", {'class': 'search_user_container'}) is not None:
                    all_div = soup.find_all("div", {'class': 'search_user_container'})

                    for div in all_div:
                        try:
                            if div.find('a', {'class', 'showname'}) is not None:
                                url = '' + div.find_all('a', {'class', 'showname'})[0].get(
                                    'href')

                                html_dataset = rt.get(url, headers=headers).content

                                time.sleep(3)

                                soup_dataset = BeautifulSoup(html_dataset, 'html.parser')

                                # dataset
                                pn = ""
                                city = ""

                                if soup_dataset.select_one("#table_right").find('ul',
                                                                                {'class', 'working-cities'}).find_all(
                                        "li")[0].find_all('span')[1] is not None:
                                    city += soup_dataset.select_one("#table_right").find('ul', {'class',
                                                                                                'working-cities'}).find_all(
                                        "li")[
                                        0].find_all('span')[
                                        1].text

                                    if city == "":
                                        if soup_dataset.select("#thephone") is not None:
                                            pn += soup_dataset.select_one("#thephone").text

                                            dataset = {
                                                'url': url,
                                                'city': city,
                                                'pn': pn
                                            }

                                            myclient = pymongo.MongoClient("mongodb://localhost:27017/")

                                            mesdamesdb = myclient["mesdamesdb"]

                                            mesdames_c = mesdamesdb["mesdames_c"]

                                            mesdames_c.insert_one(dataset)

                                            print(str(dataset))

                                            myclient.close()
                                    else:
                                        print('not in the city')
                        except Exception as e:
                            print('error div : ' + str(e))
                else:
                    print('no urls')
            except Exception as e:
                print('error : ' + str(e))


if __name__ == '__main__':
    unittest.main()
