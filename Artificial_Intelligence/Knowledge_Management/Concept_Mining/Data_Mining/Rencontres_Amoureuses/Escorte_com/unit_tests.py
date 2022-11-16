import unittest
import time
import pymysql
from bs4 import BeautifulSoup
import requests
import json
import xlsxwriter
from requests_tor import RequestsTor


class UnitTestsEscorteComWithClearWeb(unittest.TestCase):
    #
    def test_extract_one_phone_number(self):
        url_result = 'https://www.escorte.com/escort/Bianca69-3454'

        # Request the content of a page from the url
        html = requests.get(url_result)

        time.sleep(3)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.content, 'html.parser')

        if soup.find("div", {"class", "phone"}) is None:
            print("sorry there is no phone number")

        else:
            show_number = soup.find("div", {"class", "phone"})\
                .find("a")\
                .get("onclick")\
                .replace("showNumber(", "")\
                .replace(")", "")\
                .replace(";", "")

            print("showNumber : " + show_number)

            url_phone_number = "https://www.escorte.com/escort/get_phone/" + show_number

            payload = {}
            headers = {
                'Host': 'www.escorte.com',
                'Referer': url_result,
                'Connection': 'keep-alive',
                'Accept': '*/*',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'en-US,en;q=0.5',
                'TE': 'Trailers',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:68.0) Gecko/20100101 Firefox/68.0',
                'X-Requested-With': 'XMLHttpRequest'
            }

            response = requests.request("GET", url_phone_number, headers=headers, data=payload)

            data = response.text\
                .replace("", "")\
                .replace("�", "")\
                .replace("", "")

            json_data = json.loads(data)

            phone_number = json_data["ok"]\
                .replace("+", "00")\
                .replace(" ", "")

            print("phone_number : " + phone_number)

    def test_extract_all_url_escorts_from_one_search(self):
        url_search = 'https://www.escorte.com/escorts/paris/1er-arrondissement-du-louvre/'

        # Request the content of a page from the url
        html = requests.get(url_search)

        time.sleep(3)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.content, 'html.parser')

        if soup.find("div", {"class", "col-xs-4 escort"}) is None:
            print("sorry there is no escorts")

        else:
            url_escorts = soup.find_all("div", {"class", "col-xs-4 escort"})

            for url_escort in url_escorts:
                print("https://www.escorte.com" + url_escort.find("a").get("href"))

    def test_extract_all_phone_number_from_one_search(self):
        url_search = 'https://www.escorte.com/escorts/paris/1er-arrondissement-du-louvre/'

        # Request the content of a page from the url
        html_search = requests.get(url_search)

        time.sleep(3)

        # Parse the content of html_doc
        soup = BeautifulSoup(html_search.content, 'html.parser')

        if soup.find("div", {"class", "col-xs-4 escort"}) is None:
            print("sorry there is no escorts")

        else:
            url_escorts = soup.find_all("div", {"class", "col-xs-4 escort"})

            for url_escort in url_escorts:
                url_result = "https://www.escorte.com" + url_escort.find("a").get("href")

                # Request the content of a page from the url
                html_result = requests.get(url_result)

                time.sleep(3)

                # Parse the content of html_doc
                soup = BeautifulSoup(html_result.content, 'html.parser')

                if soup.find("div", {"class", "phone"}) is None:
                    print("sorry there is no phone number")

                else:
                    show_number = soup.find("div", {"class", "phone"})\
                        .find("a")\
                        .get("onclick")\
                        .replace("showNumber(", "")\
                        .replace(")", "")\
                        .replace(";", "")

                    url_phone_number = "https://www.escorte.com/escort/get_phone/" + show_number

                    payload = {}

                    headers = {
                        'Host': 'www.escorte.com',
                        'Referer': url_result,
                        'Connection': 'keep-alive',
                        'Accept': '*/*',
                        'Accept-Encoding': 'gzip, deflate, br',
                        'Accept-Language': 'en-US,en;q=0.5',
                        'TE': 'Trailers',
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:68.0) Gecko/20100101 Firefox/68.0',
                        'X-Requested-With': 'XMLHttpRequest'
                    }

                    response = requests.request("GET", url_phone_number, headers=headers, data=payload)

                    data = response.text\
                        .replace("", "")\
                        .replace("�", "")\
                        .replace("", "")

                    try:
                        json_data = json.loads(data)

                        if "ok" in json_data:
                            if not (json_data.get('ok') is None):
                                phone_number = json_data.get('ok')\
                                    .replace("+", "00")\
                                    .replace(" ", "")\
                                    .replace("-", "")

                                if phone_number[:4] == "0033":
                                    print("phone_number : " + phone_number)

                            else:
                                print("Key ok has no value")
                        else:
                            print("Key ok doesn't exist in JSON data")
                    except Exception as e:
                        print("probleme with json_data : " + str(e))

    def test_extract_all_phone_number_from_one_search_into_excel(self):
        url_search = 'https://www.escorte.com/escorts/paris/8eme-arrondissement-de-l-elysee/#age=2&is_smoking=2&is_drinking=3'

        filename = url_search.split("https://www.escorte.com/escorts/")[1][:10]\
            .replace("-", "")\
            .replace("_", "")\
            .replace("/", "")

        # Create a workbook and add a worksheet.
        workbook = xlsxwriter.Workbook(filename + '.xlsx')
        worksheet = workbook.add_worksheet()

        # Start from the first cell. Rows and columns are zero indexed.
        row = 0
        col = 0

        # Request the content of a page from the url
        html_search = requests.get(url_search)

        time.sleep(3)

        # Parse the content of html_doc
        soup = BeautifulSoup(html_search.content, 'html.parser')

        if soup.find("div", {"class", "col-xs-4 escort"}) is None:
            print("sorry there is no escorts")

        else:
            url_escorts = soup.find_all("div", {"class", "col-xs-4 escort"})

            for url_escort in url_escorts:
                url_result = "https://www.escorte.com" + url_escort.find("a").get("href")

                # Request the content of a page from the url
                html_result = requests.get(url_result)

                time.sleep(3)

                # Parse the content of html_doc
                soup = BeautifulSoup(html_result.content, 'html.parser')

                if soup.find("div", {"class", "phone"}) is None:
                    print("sorry there is no phone number")

                else:
                    show_number = soup.find("div", {"class", "phone"}) \
                        .find("a") \
                        .get("onclick") \
                        .replace("showNumber(", "") \
                        .replace(")", "") \
                        .replace(";", "")

                    url_phone_number = "https://www.escorte.com/escort/get_phone/" + show_number

                    payload = {}
                    headers = {
                        'Host': 'www.escorte.com',
                        'Referer': url_result,
                        'Connection': 'keep-alive',
                        'Accept': '*/*',
                        'Accept-Encoding': 'gzip, deflate, br',
                        'Accept-Language': 'en-US,en;q=0.5',
                        'TE': 'Trailers',
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:68.0) Gecko/20100101 Firefox/68.0',
                        'X-Requested-With': 'XMLHttpRequest'
                    }

                    response = requests.request("GET", url_phone_number, headers=headers, data=payload)

                    data = response.text \
                        .replace("", "") \
                        .replace("�", "") \
                        .replace("", "")

                    try:
                        json_data = json.loads(data)

                        if "ok" in json_data:
                            if not (json_data.get('ok') is None):
                                phone_number = json_data.get('ok') \
                                    .replace("+", "00") \
                                    .replace(" ", "") \
                                    .replace("-", "")

                                if phone_number[:4] == "0033":
                                    print("phone_number : " + phone_number)

                                    # Iterate over the data and write it out row by row.
                                    worksheet.write(row, col, url_result)
                                    worksheet.write(row, col + 1, phone_number)
                                    row += 1

                            else:
                                print("Key ok has no value")
                        else:
                            print("Key ok doesn't exist in JSON data")
                    except:
                        print("probleme with json_data")

        workbook.close()

    def test_extract_all_phone_number_from_urls_into_mysql(self):
        urls_search = [
            "https://www.escorte.com/escorts/paris/1er-arrondissement-du-louvre/"
        ]

        url = "https://geo.api.gouv.fr/communes?fields=nom,code,codesPostaux,codeDepartement,codeRegion,population&format=json&geometry=centre"

        response = requests.request("GET", url)

        communes = response.json()

        for commune in communes:
            try:
                if commune['population'] > 15000:
                    ville = commune['nom'].lower().replace(' ', '-').replace('ê', 'e').replace('é', 'e')\
                        .replace('è', 'e')\
                        .replace('à', 'a')\
                        .replace('â', 'a')\
                        .replace('ô', 'o')

                    urls_search.append("https://www.escorte.com/escorts/" + ville)
            except Exception as e:
                print("error : " + str(e))

        for url_search in urls_search:
            html_search = requests.get(url_search)

            time.sleep(3)

            soup = BeautifulSoup(html_search.content, 'html.parser')

            if soup.find("div", {"class", "col-xs-4 escort"}) is None:
                print("sorry there is no escorts")
            else:
                url_escorts = soup.find_all("div", {"class", "col-xs-4 escort"})

                for url_escort in url_escorts:
                    url_result = "https://www.escorte.com" + url_escort.find("a").get("href")

                    html_result = requests.get(url_result)

                    time.sleep(3)

                    soup = BeautifulSoup(html_result.content, 'html.parser')

                    if soup.find("div", {"class", "phone"}) is None:
                        print("sorry there is no phone number")

                    else:
                        show_number = soup.find("div", {"class", "phone"}) \
                            .find("a") \
                            .get("onclick") \
                            .replace("showNumber(", "") \
                            .replace(")", "") \
                            .replace(";", "")

                        url_phone_number = "https://www.escorte.com/escort/get_phone/" + show_number

                        payload = {}

                        headers = {
                            'Host': 'www.escorte.com',
                            'Referer': url_result,
                            'Connection': 'keep-alive',
                            'Accept': '*/*',
                            'Accept-Encoding': 'gzip, deflate, br',
                            'Accept-Language': 'en-US,en;q=0.5',
                            'TE': 'Trailers',
                            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:68.0) Gecko/20100101 Firefox/68.0',
                            'X-Requested-With': 'XMLHttpRequest'
                        }

                        response = requests.request("GET", url_phone_number, headers=headers, data=payload)

                        data = response.text \
                            .replace("", "") \
                            .replace("�", "") \
                            .replace("", "")

                        try:
                            json_data = json.loads(data)

                            if "ok" in json_data:
                                if not (json_data.get('ok') is None):
                                    phone_number = json_data.get('ok') \
                                        .replace("+", "00") \
                                        .replace(" ", "") \
                                        .replace("-", "")

                                    if phone_number[:4] == "0033":
                                        print("phone_number : " + phone_number)

                                        try:
                                            connection = pymysql.connect(
                                                host='localhost',
                                                port=3306,
                                                user='root',
                                                password='8h0NEJkEf3lyCBUoPQwCHSu@@@@@@@',
                                                db='rencontres_amoureuses',
                                                charset='utf8mb4',
                                                cursorclass=pymysql.cursors.DictCursor
                                            )

                                            with connection.cursor() as cursor:
                                                try:
                                                    sql = "INSERT INTO `rencontres_amoureuses_telephone` (`telephone`) VALUE (%s)"

                                                    cursor.execute(sql, phone_number)

                                                    connection.commit()

                                                    connection.close()

                                                    print('telephone ' + phone_number + ' : ok')
                                                except Exception as e:
                                                    print("The record already exists (telephone " + phone_number + ") : " + str(e))
                                                    connection.close()
                                        except Exception as e:
                                            print("Problem connection MySQL : " + str(e))
                                else:
                                    print("Key ok has no value")
                            else:
                                print("Key ok doesn't exist in JSON data")
                        except Exception as e:
                            print("probleme with json_data : " + str(e))


class UnitTestsEscorteComWithDarkWeb(unittest.TestCase):
    # ok
    def test_extract_one_phone_number(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url_result = 'https://www.escorte.com/escort/Bianca69-3454'

        rt = RequestsTor()

        html_with_tor = rt.get(url_result, headers=headers)

        time.sleep(3)

        # Parse the content of html_doc
        soup = BeautifulSoup(html_with_tor.content, 'html.parser')

        if soup.find("div", {"class", "phone"}) is None:
            print("sorry there is no phone number")

        else:
            show_number = soup.find("div", {"class", "phone"})\
                .find("a")\
                .get("onclick")\
                .replace("showNumber(", "")\
                .replace(")", "")\
                .replace(";", "")

            print("showNumber : " + show_number)

            url_phone_number = "https://www.escorte.com/escort/get_phone/" + show_number

            payload = {}
            headers = {
                'Host': 'www.escorte.com',
                'Referer': url_result,
                'Connection': 'keep-alive',
                'Accept': '*/*',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'en-US,en;q=0.5',
                'TE': 'Trailers',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:68.0) Gecko/20100101 Firefox/68.0',
                'X-Requested-With': 'XMLHttpRequest'
            }

            response = requests.request("GET", url_phone_number, headers=headers, data=payload)

            data = response.text\
                .replace("", "")\
                .replace("�", "")\
                .replace("", "")

            json_data = json.loads(data)

            phone_number = json_data["ok"]\
                .replace("+", "00")\
                .replace(" ", "")

            print("phone_number : " + phone_number)

    # ok
    def test_extract_all_url_escorts_from_one_search(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url_search = 'https://www.escorte.com/escorts/paris/1er-arrondissement-du-louvre/'

        rt = RequestsTor()

        html_with_tor = rt.get(url_search, headers=headers)

        time.sleep(3)

        # Parse the content of html_doc
        soup = BeautifulSoup(html_with_tor.content, 'html.parser')

        if soup.find("div", {"class", "col-xs-4 escort"}) is None:
            print("sorry there is no escorts")

        else:
            url_escorts = soup.find_all("div", {"class", "col-xs-4 escort"})

            for url_escort in url_escorts:
                print("https://www.escorte.com" + url_escort.find("a").get("href"))

    # ok
    def test_extract_all_phone_number_from_one_search(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url_search = 'https://www.escorte.com/escorts/paris/1er-arrondissement-du-louvre/'

        rt = RequestsTor()

        html_with_tor = rt.get(url_search, headers=headers)

        time.sleep(3)

        # Parse the content of html_doc
        soup = BeautifulSoup(html_with_tor.content, 'html.parser')

        if soup.find("div", {"class", "col-xs-4 escort"}) is None:
            print("sorry there is no escorts")

        else:
            url_escorts = soup.find_all("div", {"class", "col-xs-4 escort"})

            for url_escort in url_escorts:
                url_result = "https://www.escorte.com" + url_escort.find("a").get("href")

                # Request the content of a page from the url
                html_result = requests.get(url_result)

                time.sleep(3)

                # Parse the content of html_doc
                soup = BeautifulSoup(html_result.content, 'html.parser')

                if soup.find("div", {"class", "phone"}) is None:
                    print("sorry there is no phone number")

                else:
                    show_number = soup.find("div", {"class", "phone"})\
                        .find("a")\
                        .get("onclick")\
                        .replace("showNumber(", "")\
                        .replace(")", "")\
                        .replace(";", "")

                    url_phone_number = "https://www.escorte.com/escort/get_phone/" + show_number

                    payload = {}

                    headers = {
                        'Host': 'www.escorte.com',
                        'Referer': url_result,
                        'Connection': 'keep-alive',
                        'Accept': '*/*',
                        'Accept-Encoding': 'gzip, deflate, br',
                        'Accept-Language': 'en-US,en;q=0.5',
                        'TE': 'Trailers',
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:68.0) Gecko/20100101 Firefox/68.0',
                        'X-Requested-With': 'XMLHttpRequest'
                    }

                    response = requests.request("GET", url_phone_number, headers=headers, data=payload)

                    data = response.text\
                        .replace("", "")\
                        .replace("�", "")\
                        .replace("", "")

                    try:
                        json_data = json.loads(data)

                        if "ok" in json_data:
                            if not (json_data.get('ok') is None):
                                phone_number = json_data.get('ok')\
                                    .replace("+", "00")\
                                    .replace(" ", "")\
                                    .replace("-", "")

                                if phone_number[:4] == "0033":
                                    print("phone_number : " + phone_number)

                            else:
                                print("Key ok has no value")
                        else:
                            print("Key ok doesn't exist in JSON data")
                    except Exception as e:
                        print("probleme with json_data : " + str(e))

    #
    def test_extract_all_phone_number_from_urls_into_mysql(self):
        urls_search = [
            "https://www.escorte.com/escorts/paris/1er-arrondissement-du-louvre/",
        ]

        url = "https://geo.api.gouv.fr/communes?fields=nom,code,codesPostaux,codeDepartement,codeRegion," \
              "population&format=json&geometry=centre"

        response = requests.request("GET", url)

        communes = response.json()

        for commune in communes:
            try:
                if commune['population'] > 15000:
                    ville = commune['nom'].lower().replace(' ', '-').replace('ê', 'e').replace('é', 'e')\
                        .replace('è', 'e')\
                        .replace('à', 'a')\
                        .replace('â', 'a')\
                        .replace('ô', 'o')

                    urls_search.append("https://www.escorte.com/escorts/" + ville)
            except Exception as e:
                print("error : " + str(e))

        for url_search in urls_search:
            html_search = requests.get(url_search)

            time.sleep(3)

            soup = BeautifulSoup(html_search.content, 'html.parser')

            if soup.find("div", {"class", "col-xs-4 escort"}) is None:
                print("sorry there is no escorts")
            else:
                url_escorts = soup.find_all("div", {"class", "col-xs-4 escort"})

                for url_escort in url_escorts:
                    url_result = "https://www.escorte.com" + url_escort.find("a").get("href")

                    html_result = requests.get(url_result)

                    time.sleep(3)

                    soup = BeautifulSoup(html_result.content, 'html.parser')

                    if soup.find("div", {"class", "phone"}) is None:
                        print("sorry there is no phone number")
                    else:
                        show_number = soup.find("div", {"class", "phone"}) \
                            .find("a") \
                            .get("onclick") \
                            .replace("showNumber(", "") \
                            .replace(")", "") \
                            .replace(";", "")

                        url_phone_number = "https://www.escorte.com/escort/get_phone/" + show_number

                        payload = {}

                        headers = {
                            'Host': 'www.escorte.com',
                            'Referer': url_result,
                            'Connection': 'keep-alive',
                            'Accept': '*/*',
                            'Accept-Encoding': 'gzip, deflate, br',
                            'Accept-Language': 'en-US,en;q=0.5',
                            'TE': 'Trailers',
                            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:68.0) Gecko/20100101 Firefox/68.0',
                            'X-Requested-With': 'XMLHttpRequest'
                        }

                        response = requests.request("GET", url_phone_number, headers=headers, data=payload)

                        data = response.text \
                            .replace("", "") \
                            .replace("�", "") \
                            .replace("", "")

                        try:
                            json_data = json.loads(data)

                            if "ok" in json_data:
                                if not (json_data.get('ok') is None):
                                    phone_number = json_data.get('ok') \
                                        .replace("+", "00") \
                                        .replace(" ", "") \
                                        .replace("-", "")

                                    if phone_number[:4] == "0033":
                                        print("phone_number : " + phone_number)

                                        try:
                                            connection = pymysql.connect(
                                                host='localhost',
                                                port=3306,
                                                user='root',
                                                password='8h0NEJkEf3lyCBUoPQwCHSu@@@@@@@',
                                                db='rencontres_amoureuses',
                                                charset='utf8mb4',
                                                cursorclass=pymysql.cursors.DictCursor
                                            )

                                            with connection.cursor() as cursor:
                                                try:
                                                    sql = "INSERT INTO `rencontres_amoureuses_telephone` " \
                                                          "(`telephone`) VALUE (%s)"

                                                    cursor.execute(sql, phone_number)

                                                    connection.commit()

                                                    connection.close()

                                                    print('telephone ' + phone_number + ' : ok')
                                                except Exception as e:
                                                    print("The record already exists (telephone " + phone_number + ") : " + str(e))
                                                    connection.close()
                                        except Exception as e:
                                            print("Problem connection MySQL : " + str(e))
                                else:
                                    print("Key ok has no value")
                            else:
                                print("Key ok doesn't exist in JSON data")
                        except Exception as e:
                            print("probleme with json_data : " + str(e))

if __name__ == '__main__':
    unittest.main()
