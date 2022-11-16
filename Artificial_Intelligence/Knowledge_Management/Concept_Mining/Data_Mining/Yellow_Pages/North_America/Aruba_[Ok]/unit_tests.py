from bs4 import BeautifulSoup
import requests
import time
import pymysql.cursors
import unittest


class UnitTestsDataMinerYellowPagesAruba(unittest.TestCase):
    # table : contacts_for_b2b_contact_data_for_datarade

    # region : myself
    # activity : myself
    # country : myself

    # company_name
    def test_extract_company_name_from_one_result_with_clear_web(self):
        print("test_extract_company_name_from_one_result_with_clear_web")

        url = "https://www.findyello.com/aruba/aruba-ocean-villas/profile/"

        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.67'
        }

        time.sleep(2)

        html = requests.get(url, headers=headers)

        soup = BeautifulSoup(html.content, 'html.parser')

        # company_name
        company_name = ""

        if soup.select_one('#name') is not None:
            company_name += str(soup.select_one('#name').text.lower())

            print("company_name 0 : " + company_name)
        else:
            if soup.find('span', {'itemprop': 'name'}) is not None:
                company_name += str(soup.find('span', {'itemprop': 'name'}).text.lower())

                print("company_name 1 : " + company_name)
            else:
                print("no company_name business")

    # postal_address
    def test_extract_postal_address_from_one_result_with_clear_web(self):
        print("test_extract_postal_address_from_one_result_with_clear_web")

        url = "https://www.findyello.com/aruba/aruba-ocean-villas/profile/"

        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.67'
        }

        time.sleep(2)

        html = requests.get(url, headers=headers)

        soup = BeautifulSoup(html.content, 'html.parser')

        # postal_address
        postal_address = ""

        if soup.find('span', {'itemprop': 'streetAddress'}) is not None:
            postal_address += str(soup.find('span', {'itemprop': 'streetAddress'}).text
                                  .lower()
                                  .replace("\t", " ")
                                  .replace("\n", " ")
                                  .replace("\r", " ")
                                  .replace("           ", "")
                                  .replace("    ", "")
                                  )

            print("postal_address : " + str(postal_address))
        else:
            print("no postal_address business")

    # phone_number
    def test_extract_phone_number_from_one_result_with_clear_web(self):
        print("test_extract_phone_number_from_one_result_with_clear_web")

        url = "https://www.findyello.com/aruba/aruba-ocean-villas/profile/"

        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.67'
        }

        time.sleep(2)

        html = requests.get(url, headers=headers)

        soup = BeautifulSoup(html.content, 'html.parser')

        # phone_number
        phone_number = ""

        if soup.select_one('#phone') is not None:
            phone_number += str(
                soup.select_one('#phone').text.lower().replace("\n", " / ").replace("\t", " / "))

            print("phone_number 0 : " + phone_number)
        else:
            if soup.find('span', {'itemprop': 'telephone'}) is not None:
                phone_number += "(+1268) " + str(
                    soup.find('span', {'itemprop': 'telephone'})
                        .text
                        .lower()
                        .replace("\n", " / ")
                        .replace("\t", " / ")
                )

                print("phone_number 1 : " + phone_number)
            else:
                print("no phone_number business")

    # website
    def test_extract_website_from_one_result_with_clear_web(self):
        print("test_extract_website_from_one_result_with_clear_web")

        url = "https://www.findyello.com/aruba/aruba-ocean-villas/profile/"

        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.67'
        }

        time.sleep(2)

        html = requests.get(url, headers=headers)

        soup = BeautifulSoup(html.content, 'html.parser')

        # website
        website = ""

        if soup.find("li", {'class': 'profile-menu-website'}) is not None:
            website += soup \
                .find("li", {'class': 'profile-menu-website'}) \
                .find("a") \
                .get("href") \
                .replace('https://www.findyello.com/redirector.php?yelref=', '') \
                .replace('%2F', '/') \
                .replace('%3A', ':')

            print("website : " + website)
        else:
            print("no website business")

    # email
    def test_extract_email_from_one_result_with_clear_web(self):
        print("test_extract_email_from_one_result_with_clear_web")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://www.findyello.com/aruba/aruba-ocean-villas/profile/"

        time.sleep(2)

        # Request the content of a page from the url
        html = requests.get(url, headers=headers)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.content, 'html.parser')

        # email
        email = ""

        if soup.find("li", {'class': 'profile-menu-website'}) is not None:
            email += "info@" + soup \
                .find("li", {'class': 'profile-menu-website'}) \
                .find("a") \
                .get("href") \
                .replace('https://www.findyello.com/redirector.php?yelref=https%3A%2F%2F', '') \
                .replace('https://www.findyello.com/redirector.php?yelref=http%3A%2F%2F', '') \
                .replace('https://www.findyello.com/redirector.php?yelref=', '') \
                .replace('www.', '') \
                .replace('%2F', '') \
                .split('/')[0]

            print("email : " + email)
        else:
            print("no email business")

    def test_extract_each_email_from_one_page_of_results_for_one_activity_and_one_capital(self):
        print("test_extract_each_email_from_one_page_of_results_for_one_activity_and_one_capital")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://www.findyello.com/aruba/?search=hotel&pageno=1"

        time.sleep(2)

        # Request the content of a page from the url
        html = requests.get(url, headers=headers)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.content, 'html.parser')

        if soup.find("h2", {'class': 'h4'}) is not None:
            all_a = soup.find_all("h2", {'class': 'h4'})

            for a in all_a:
                url = "https://www.findyello.com" + a.find('a').get('href')

                time.sleep(2)

                # Request the content of a page from the url
                html = requests.get(url, headers=headers)

                # Parse the content of html_doc
                soup = BeautifulSoup(html.content, 'html.parser')

                if soup.find("li", {'class': 'profile-menu-website'}) is not None:
                    email = "info@" + soup \
                        .find("li", {'class': 'profile-menu-website'}) \
                        .find("a") \
                        .get("href") \
                        .replace('https://www.findyello.com/redirector.php?yelref=https%3A%2F%2F', '') \
                        .replace('https://www.findyello.com/redirector.php?yelref=http%3A%2F%2F', '') \
                        .replace('https://www.findyello.com/redirector.php?yelref=', '') \
                        .replace('www.', '') \
                        .replace('%2F', '') \
                        .split('/')[0]

                    print("email : " + email)
                else:
                    print("no email business")
        else:
            print("no a class companyName")

    def test_extract_each_email_from_all_pages_of_results_for_one_activity_and_one_capital(self):
        print("test_extract_each_email_from_all_pages_of_results_for_one_activity_and_one_capital")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        activity = "hotel"

        city = "aruba"

        number_of_pages = 0

        url_page = "https://www.findyello.com/" + city + "/?search=" + activity

        time.sleep(2)

        html_search = requests.get(url_page, headers=headers)

        soup = BeautifulSoup(html_search.content, 'html.parser')

        if soup.find("p", {"class": "strong small lighter"}) is not None:
            number_of_pages_with_coma = int(soup.find("p", {"class": "strong small lighter"})
                                            .text
                                            .split("of")[1]
                                            .replace(" ", "")
                                            .replace("Results", "")
                                            ) / 15

            if int(str(number_of_pages_with_coma).split(".")[1][:1]) < 5:
                number_of_pages += round(number_of_pages_with_coma) + 1
                print('number_of_pages : ' + str(number_of_pages))
            elif int(str(number_of_pages_with_coma).split(".")[1][:1]) >= 5:
                number_of_pages += round(number_of_pages_with_coma)
                print('number_of_pages : ' + str(number_of_pages))
        else:
            print("error pages")

        i_1 = 0

        if number_of_pages > 1:
            for i in range(1, number_of_pages + 1):
                if i < 20:
                    url = url_page + "&pageno=" + str(i)

                    print(url)

                    time.sleep(2)

                    # Request the content of a page from the url
                    html = requests.get(url, headers=headers)

                    # Parse the content of html_doc
                    soup = BeautifulSoup(html.content, 'html.parser')

                    if soup.find("h2", {'class': 'h4'}) is not None:
                        all_a = soup.find_all("h2", {'class': 'h4'})

                        for a in all_a:
                            i_1 += 1

                            url = "https://www.findyello.com" + a.find('a').get('href')

                            time.sleep(2)

                            # Request the content of a page from the url
                            html = requests.get(url, headers=headers)

                            # Parse the content of html_doc
                            soup = BeautifulSoup(html.content, 'html.parser')

                            if soup.find("li", {'class': 'profile-menu-website'}) is not None:
                                email = "info@" + soup \
                                    .find("li", {'class': 'profile-menu-website'}) \
                                    .find("a") \
                                    .get("href") \
                                    .replace('https://www.findyello.com/redirector.php?yelref=https%3A%2F%2F', '') \
                                    .replace('https://www.findyello.com/redirector.php?yelref=http%3A%2F%2F', '') \
                                    .replace('https://www.findyello.com/redirector.php?yelref=', '') \
                                    .replace('www.', '') \
                                    .replace('%2F', '') \
                                    .split('/')[0]

                                print(str(i_1) + " email : " + email)
                            else:
                                print(str(i_1) + " no email business")
                    else:
                        print("no a class companyName")
        else:
            if soup.find("h2", {'class': 'h4'}) is not None:
                all_a = soup.find_all("h2", {'class': 'h4'})

                for a in all_a:
                    i_1 += 1

                    url = "https://www.findyello.com" + a.find('a').get('href')

                    time.sleep(2)

                    # Request the content of a page from the url
                    html = requests.get(url, headers=headers)

                    # Parse the content of html_doc
                    soup = BeautifulSoup(html.content, 'html.parser')

                    if soup.find("li", {'class': 'profile-menu-website'}) is not None:
                        email = "info@" + soup \
                            .find("li", {'class': 'profile-menu-website'}) \
                            .find("a") \
                            .get("href") \
                            .replace('https://www.findyello.com/redirector.php?yelref=https%3A%2F%2F', '') \
                            .replace('https://www.findyello.com/redirector.php?yelref=http%3A%2F%2F', '') \
                            .replace('https://www.findyello.com/redirector.php?yelref=', '') \
                            .replace('www.', '') \
                            .replace('%2F', '') \
                            .split('/')[0]

                        print(str(i_1) + " email : " + email)
                    else:
                        print(str(i_1) + " no email business")
            else:
                print("no a class companyName")

    def test_extract_each_email_from_all_pages_of_results_for_all_activities_and_all_capitals(self):
        print("test_extract_each_email_from_all_pages_of_results_for_all_activities_and_all_capitals")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        activites = [
            {'id': '1', 'url': 'employment'},  # Temporary employment agencies
            {'id': '2', 'url': 'real-estate'},  # Real estate
            {'id': '3', 'url': 'recruitment'},  # Recruiter
            {'id': '4', 'url': 'software'},  # software
            {'id': '5', 'url': 'hotel'},  # hotel
            {'id': '6', 'url': 'social'},  # social landlord
            {'id': '7', 'url': 'cleaning'},  # cleaning
            {'id': '8', 'url': 'charity'},  # charity
            {'id': '9', 'url': 'financial'},  # financial
            {'id': '10', 'url': 'restaurant'},  # restaurant
            {'id': '11', 'url': 'building'},  # building
            {'id': '12', 'url': 'hairdresser'},  # hairdresser
            {'id': '13', 'url': 'florist'},  # florist
            {'id': '14', 'url': 'locksmith'},  # locksmith
            {'id': '15', 'url': 'bakery'},  # bakery
            {'id': '16', 'url': 'insurance'},  # insurance
            {'id': '17', 'url': 'pharmacy'},  # pharmacy
            {'id': '18', 'url': 'mover'},  # mover
            {'id': '19', 'url': 'electricity'},  # electricity
            {'id': '20', 'url': 'plumbing'},  # plumbing
            {'id': '21', 'url': 'security'},  # security
            {'id': '22', 'url': 'attorney'},  # attorney
            {'id': '23', 'url': 'bank'},  # bank
            {'id': '24', 'url': 'garage'},  # garage
            {'id': '25', 'url': 'dentist'},  # dentist
            {'id': '26', 'url': 'doctor'},  # doctor
            {'id': '27', 'url': 'accountant'},  # accountant
            {'id': '28', 'url': 'grocery'},  # grocery stores
            {'id': '29', 'url': 'notary'},  # notary
            {'id': '30', 'url': 'jewellery'},  # jewellery
            {'id': '31', 'url': 'tailor'},  # tailor
            {'id': '32', 'url': 'butcher'},  # butcher
            {'id': '33', 'url': 'library'},  # library
            {'id': '34', 'url': 'architect'},  # architect
            {'id': '36', 'url': 'cement'},  # cement
            {'id': '37', 'url': 'heating'},  # heating
            {'id': '38', 'url': 'boat'},  # boat
            {'id': '39', 'url': 'cold'},  # cold
            {'id': '41', 'url': 'steel'},  # steel
            {'id': '42', 'url': 'chemical'},  # chemical
            {'id': '43', 'url': 'gas'},  # gas
            {'id': '44', 'url': 'gold'}  # gold
        ]

        capitales_du_monde = [
            {'id': '936', 'nom': 'aruba', 'pays': 'aruba'},
        ]

        try:
            for capitale in capitales_du_monde:
                for activite in activites:
                    activity = activite.get('url')

                    city = capitale.get('nom')

                    number_of_pages = 0

                    url_page = "https://www.findyello.com/" + city + "/?search=" + activity

                    time.sleep(2)

                    html_search = requests.get(url_page, headers=headers)

                    soup = BeautifulSoup(html_search.content, 'html.parser')

                    if soup.find("p", {"class": "strong small lighter"}) is not None:
                        number_of_pages_with_coma = int(soup.find("p", {"class": "strong small lighter"})
                                                        .text
                                                        .split("of")[1]
                                                        .replace(" ", "")
                                                        .replace("Results", "")
                                                        ) / 15

                        if int(str(number_of_pages_with_coma).split(".")[1][:1]) < 5:
                            number_of_pages += round(number_of_pages_with_coma) + 1
                            print('number_of_pages : ' + str(number_of_pages))
                        elif int(str(number_of_pages_with_coma).split(".")[1][:1]) >= 5:
                            number_of_pages += round(number_of_pages_with_coma)
                            print('number_of_pages : ' + str(number_of_pages))
                    else:
                        print("error pages")

                    i_1 = 0

                    if number_of_pages > 1:
                        for i in range(1, number_of_pages + 1):
                            if i < 20:
                                url = url_page + "&pageno=" + str(i)

                                print(url)

                                time.sleep(2)

                                # Request the content of a page from the url
                                html = requests.get(url, headers=headers)

                                # Parse the content of html_doc
                                soup = BeautifulSoup(html.content, 'html.parser')

                                if soup.find("h2", {'class': 'h4'}) is not None:
                                    all_a = soup.find_all("h2", {'class': 'h4'})

                                    for a in all_a:
                                        i_1 += 1

                                        url = "https://www.findyello.com" + a.find('a').get('href')

                                        time.sleep(2)

                                        # Request the content of a page from the url
                                        html = requests.get(url, headers=headers)

                                        # Parse the content of html_doc
                                        soup = BeautifulSoup(html.content, 'html.parser')

                                        if soup.find("li", {'class': 'profile-menu-website'}) is not None:
                                            email = "info@" + soup \
                                                .find("li", {'class': 'profile-menu-website'}) \
                                                .find("a") \
                                                .get("href") \
                                                .replace(
                                                'https://www.findyello.com/redirector.php?yelref=https%3A%2F%2F', '') \
                                                .replace(
                                                'https://www.findyello.com/redirector.php?yelref=http%3A%2F%2F', '') \
                                                .replace('https://www.findyello.com/redirector.php?yelref=', '') \
                                                .replace('www.', '') \
                                                .replace('%2F', '') \
                                                .split('/')[0]

                                            print(str(i_1) + " email : " + email)

                                            try:
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
                                                        print(str(i_1)
                                                              + " The record is stored : "
                                                              + email)
                                                        connection.close()
                                                    except Exception as e:
                                                        print(str(i_1)
                                                              + " The record already exists : "
                                                              + email
                                                              + " " + str(e))
                                                        connection.close()
                                            except Exception as e:
                                                print(str(i_1) + " An error with the email : " + email + " " + str(e))
                                        else:
                                            print(str(i_1) + " no email business")
                                else:
                                    print("no a class companyName")
                    else:
                        if soup.find("h2", {'class': 'h4'}) is not None:
                            all_a = soup.find_all("h2", {'class': 'h4'})

                            for a in all_a:
                                i_1 += 1

                                url = "https://www.findyello.com" + a.find('a').get('href')

                                time.sleep(2)

                                # Request the content of a page from the url
                                html = requests.get(url, headers=headers)

                                # Parse the content of html_doc
                                soup = BeautifulSoup(html.content, 'html.parser')

                                if soup.find("li", {'class': 'profile-menu-website'}) is not None:
                                    email = "info@" + soup \
                                        .find("li", {'class': 'profile-menu-website'}) \
                                        .find("a") \
                                        .get("href") \
                                        .replace('https://www.findyello.com/redirector.php?yelref=https%3A%2F%2F', '') \
                                        .replace('https://www.findyello.com/redirector.php?yelref=http%3A%2F%2F', '') \
                                        .replace('https://www.findyello.com/redirector.php?yelref=', '') \
                                        .replace('www.', '') \
                                        .replace('%2F', '') \
                                        .split('/')[0]

                                    print(str(i_1) + " email : " + email)

                                    try:
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
                                                print(str(i_1)
                                                      + " The record is stored : "
                                                      + email)
                                                connection.close()
                                            except Exception as e:
                                                print(str(i_1)
                                                      + " The record already exists : "
                                                      + email
                                                      + " " + str(e))
                                                connection.close()
                                    except Exception as e:
                                        print(str(i_1) + " An error with the email : " + email + " " + str(e))
                                else:
                                    print(str(i_1) + " no email business")
                        else:
                            print("no a class companyName")
        except Exception as e:
            print("error : " + str(e))

    def test_extract_each_contact_from_one_page_of_results_for_one_activity_and_one_capital(self):
        print("test_extract_each_email_from_one_page_of_results_for_one_activity_and_one_capital")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        activity = "hotel"

        city = "aruba"

        country = "aruba"

        url = "https://www.findyello.com/" + city + "/?search=" + activity + "&pageno=1"

        time.sleep(2)

        # Request the content of a page from the url
        html = requests.get(url, headers=headers)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.content, 'html.parser')

        if soup.find("h2", {'class': 'h4'}) is not None:
            all_a = soup.find_all("h2", {'class': 'h4'})

            for a in all_a:
                url = "https://www.findyello.com" + a.find('a').get('href')

                time.sleep(2)

                # Request the content of a page from the url
                html = requests.get(url, headers=headers)

                # Parse the content of html_doc
                soup = BeautifulSoup(html.content, 'html.parser')

                # company_name
                company_name = ""

                if soup.select_one('#name') is not None:
                    company_name += str(soup.select_one('#name').text.lower())
                else:
                    if soup.find('span', {'itemprop': 'name'}) is not None:
                        company_name += str(soup.find('span', {'itemprop': 'name'}).text.lower())
                    else:
                        print("no company_name business")

                # postal_address
                postal_address = ""

                if soup.find('span', {'itemprop': 'streetAddress'}) is not None:
                    postal_address += str(soup.find('span', {'itemprop': 'streetAddress'}).text
                                          .lower()
                                          .replace("\t", " ")
                                          .replace("\n", " ")
                                          .replace("\r", " ")
                                          .replace("           ", "")
                                          .replace("    ", "")
                                          )
                else:
                    print("no postal_address business")

                # phone_number
                phone_number = ""

                if soup.select_one('#phone') is not None:
                    phone_number += str(
                        soup.select_one('#phone').text.lower().replace("\n", " / ").replace("\t", " / "))
                else:
                    if soup.find('span', {'itemprop': 'telephone'}) is not None:
                        phone_number += "(+1268) " + str(
                            soup.find('span', {'itemprop': 'telephone'})
                                .text
                                .lower()
                                .replace("\n", " / ")
                                .replace("\t", " / ")
                        )
                    else:
                        print("no phone_number business")

                # website
                website = ""

                if soup.find("li", {'class': 'profile-menu-website'}) is not None:
                    website += soup \
                        .find("li", {'class': 'profile-menu-website'}) \
                        .find("a") \
                        .get("href") \
                        .replace('https://www.findyello.com/redirector.php?yelref=', '') \
                        .replace('%2F', '/') \
                        .replace('%3A', ':')
                else:
                    print("no website business")

                # email
                email = ""

                if soup.find("li", {'class': 'profile-menu-website'}) is not None:
                    email += "info@" + soup \
                        .find("li", {'class': 'profile-menu-website'}) \
                        .find("a") \
                        .get("href") \
                        .replace('https://www.findyello.com/redirector.php?yelref=https%3A%2F%2F', '') \
                        .replace('https://www.findyello.com/redirector.php?yelref=http%3A%2F%2F', '') \
                        .replace('https://www.findyello.com/redirector.php?yelref=', '') \
                        .replace('www.', '') \
                        .replace('%2F', '') \
                        .split('/')[0]
                else:
                    print("no email business")

                contact_b2b = {
                    "company_name": company_name,
                    "postal_address": postal_address,
                    "phone_number": phone_number,
                    "website": website,
                    "email": email,
                    "region": city,
                    "activity": activity,
                    "country": country
                }

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
                        sql = "INSERT INTO contacts_for_b2b_contact_data_for_datarade " \
                              "(company_name, postal_address, phone_number, website, email, region, " \
                              "activity, country) " \
                              "VALUE (%s, %s, %s, %s, %s, %s, %s, %s)"

                        cursor.execute(sql, (
                            contact_b2b.get('company_name'),
                            contact_b2b.get('postal_address'),
                            contact_b2b.get('phone_number'),
                            contact_b2b.get('website'),
                            contact_b2b.get('email'),
                            contact_b2b.get('region'),
                            contact_b2b.get('activity'),
                            contact_b2b.get('country')))

                        connection.commit()

                        print("The record is stored : contacts_for_b2b_contact_data_for_datarade : " + str(contact_b2b))

                        connection.close()
                    except Exception as e:
                        print("The record already exists : " + str(e))
                        connection.close()
        else:
            print("no a class companyName")

    def test_extract_each_contact_from_all_pages_of_results_for_one_activity_and_one_capital(self):
        print("test_extract_each_email_from_all_pages_of_results_for_one_activity_and_one_capital")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        activity = "hotel"

        city = "aruba"

        country = "aruba"

        number_of_pages = 0

        url_page = "https://www.findyello.com/" + city + "/?search=" + activity

        time.sleep(2)

        html_search = requests.get(url_page, headers=headers)

        soup = BeautifulSoup(html_search.content, 'html.parser')

        if soup.find("p", {"class": "strong small lighter"}) is not None:
            number_of_pages_with_coma = int(soup.find("p", {"class": "strong small lighter"})
                                            .text
                                            .split("of")[1]
                                            .replace(" ", "")
                                            .replace("Results", "")
                                            ) / 15

            if int(str(number_of_pages_with_coma).split(".")[1][:1]) < 5:
                number_of_pages += round(number_of_pages_with_coma) + 1
                print('number_of_pages : ' + str(number_of_pages))
            elif int(str(number_of_pages_with_coma).split(".")[1][:1]) >= 5:
                number_of_pages += round(number_of_pages_with_coma)
                print('number_of_pages : ' + str(number_of_pages))
        else:
            print("error pages")

        i_1 = 0

        if number_of_pages > 1:
            for i in range(1, number_of_pages + 1):
                if i < 20:
                    url = url_page + "&pageno=" + str(i)

                    print(url)

                    time.sleep(2)

                    # Request the content of a page from the url
                    html = requests.get(url, headers=headers)

                    # Parse the content of html_doc
                    soup = BeautifulSoup(html.content, 'html.parser')

                    if soup.find("h2", {'class': 'h4'}) is not None:
                        all_a = soup.find_all("h2", {'class': 'h4'})

                        for a in all_a:
                            i_1 += 1

                            url = "https://www.findyello.com" + a.find('a').get('href')

                            time.sleep(2)

                            # Request the content of a page from the url
                            html = requests.get(url, headers=headers)

                            # Parse the content of html_doc
                            soup = BeautifulSoup(html.content, 'html.parser')

                            # company_name
                            company_name = ""

                            if soup.select_one('#name') is not None:
                                company_name += str(soup.select_one('#name').text.lower())
                            else:
                                if soup.find('span', {'itemprop': 'name'}) is not None:
                                    company_name += str(soup.find('span', {'itemprop': 'name'}).text.lower())
                                else:
                                    print("no company_name business")

                            # postal_address
                            postal_address = ""

                            if soup.find('span', {'itemprop': 'streetAddress'}) is not None:
                                postal_address += str(soup.find('span', {'itemprop': 'streetAddress'}).text
                                                      .lower()
                                                      .replace("\t", " ")
                                                      .replace("\n", " ")
                                                      .replace("\r", " ")
                                                      .replace("           ", "")
                                                      .replace("    ", "")
                                                      )
                            else:
                                print("no postal_address business")

                            # phone_number
                            phone_number = ""

                            if soup.select_one('#phone') is not None:
                                phone_number += str(
                                    soup.select_one('#phone').text.lower().replace("\n", " / ").replace("\t", " / "))
                            else:
                                if soup.find('span', {'itemprop': 'telephone'}) is not None:
                                    phone_number += "(+1268) " + str(
                                        soup.find('span', {'itemprop': 'telephone'})
                                            .text
                                            .lower()
                                            .replace("\n", " / ")
                                            .replace("\t", " / ")
                                    )
                                else:
                                    print("no phone_number business")

                            # website
                            website = ""

                            if soup.find("li", {'class': 'profile-menu-website'}) is not None:
                                website += soup \
                                    .find("li", {'class': 'profile-menu-website'}) \
                                    .find("a") \
                                    .get("href") \
                                    .replace('https://www.findyello.com/redirector.php?yelref=', '') \
                                    .replace('%2F', '/') \
                                    .replace('%3A', ':')
                            else:
                                print("no website business")

                            # email
                            email = ""

                            if soup.find("li", {'class': 'profile-menu-website'}) is not None:
                                email += "info@" + soup \
                                    .find("li", {'class': 'profile-menu-website'}) \
                                    .find("a") \
                                    .get("href") \
                                    .replace('https://www.findyello.com/redirector.php?yelref=https%3A%2F%2F', '') \
                                    .replace('https://www.findyello.com/redirector.php?yelref=http%3A%2F%2F', '') \
                                    .replace('https://www.findyello.com/redirector.php?yelref=', '') \
                                    .replace('www.', '') \
                                    .replace('%2F', '') \
                                    .split('/')[0]
                            else:
                                print("no email business")

                            contact_b2b = {
                                "company_name": company_name,
                                "postal_address": postal_address,
                                "phone_number": phone_number,
                                "website": website,
                                "email": email,
                                "region": city,
                                "activity": activity,
                                "country": country
                            }

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
                                    sql = "INSERT INTO contacts_for_b2b_contact_data_for_datarade " \
                                          "(company_name, postal_address, phone_number, website, email, region, " \
                                          "activity, country) " \
                                          "VALUE (%s, %s, %s, %s, %s, %s, %s, %s)"

                                    cursor.execute(sql, (
                                        contact_b2b.get('company_name'),
                                        contact_b2b.get('postal_address'),
                                        contact_b2b.get('phone_number'),
                                        contact_b2b.get('website'),
                                        contact_b2b.get('email'),
                                        contact_b2b.get('region'),
                                        contact_b2b.get('activity'),
                                        contact_b2b.get('country')))

                                    connection.commit()

                                    print("The record is stored : contacts_for_b2b_contact_data_for_datarade : " + str(
                                        contact_b2b))

                                    connection.close()
                                except Exception as e:
                                    print("The record already exists : " + str(e))
                                    connection.close()
                    else:
                        print("no a class companyName")
        else:
            if soup.find("h2", {'class': 'h4'}) is not None:
                all_a = soup.find_all("h2", {'class': 'h4'})

                for a in all_a:
                    i_1 += 1

                    url = "https://www.findyello.com" + a.find('a').get('href')

                    time.sleep(2)

                    # Request the content of a page from the url
                    html = requests.get(url, headers=headers)

                    # Parse the content of html_doc
                    soup = BeautifulSoup(html.content, 'html.parser')

                    # company_name
                    company_name = ""

                    if soup.select_one('#name') is not None:
                        company_name += str(soup.select_one('#name').text.lower())
                    else:
                        if soup.find('span', {'itemprop': 'name'}) is not None:
                            company_name += str(soup.find('span', {'itemprop': 'name'}).text.lower())
                        else:
                            print("no company_name business")

                    # postal_address
                    postal_address = ""

                    if soup.find('span', {'itemprop': 'streetAddress'}) is not None:
                        postal_address += str(soup.find('span', {'itemprop': 'streetAddress'}).text
                                              .lower()
                                              .replace("\t", " ")
                                              .replace("\n", " ")
                                              .replace("\r", " ")
                                              .replace("           ", "")
                                              .replace("    ", "")
                                              )
                    else:
                        print("no postal_address business")

                    # phone_number
                    phone_number = ""

                    if soup.select_one('#phone') is not None:
                        phone_number += str(
                            soup.select_one('#phone').text.lower().replace("\n", " / ").replace("\t", " / "))
                    else:
                        if soup.find('span', {'itemprop': 'telephone'}) is not None:
                            phone_number += "(+1268) " + str(
                                soup.find('span', {'itemprop': 'telephone'})
                                    .text
                                    .lower()
                                    .replace("\n", " / ")
                                    .replace("\t", " / ")
                            )
                        else:
                            print("no phone_number business")

                    # website
                    website = ""

                    if soup.find("li", {'class': 'profile-menu-website'}) is not None:
                        website += soup \
                            .find("li", {'class': 'profile-menu-website'}) \
                            .find("a") \
                            .get("href") \
                            .replace('https://www.findyello.com/redirector.php?yelref=', '') \
                            .replace('%2F', '/') \
                            .replace('%3A', ':')
                    else:
                        print("no website business")

                    # email
                    email = ""

                    if soup.find("li", {'class': 'profile-menu-website'}) is not None:
                        email += "info@" + soup \
                            .find("li", {'class': 'profile-menu-website'}) \
                            .find("a") \
                            .get("href") \
                            .replace('https://www.findyello.com/redirector.php?yelref=https%3A%2F%2F', '') \
                            .replace('https://www.findyello.com/redirector.php?yelref=http%3A%2F%2F', '') \
                            .replace('https://www.findyello.com/redirector.php?yelref=', '') \
                            .replace('www.', '') \
                            .replace('%2F', '') \
                            .split('/')[0]
                    else:
                        print("no email business")

                    contact_b2b = {
                        "company_name": company_name,
                        "postal_address": postal_address,
                        "phone_number": phone_number,
                        "website": website,
                        "email": email,
                        "region": city,
                        "activity": activity,
                        "country": country
                    }

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
                            sql = "INSERT INTO contacts_for_b2b_contact_data_for_datarade " \
                                  "(company_name, postal_address, phone_number, website, email, region, " \
                                  "activity, country) " \
                                  "VALUE (%s, %s, %s, %s, %s, %s, %s, %s)"

                            cursor.execute(sql, (
                                contact_b2b.get('company_name'),
                                contact_b2b.get('postal_address'),
                                contact_b2b.get('phone_number'),
                                contact_b2b.get('website'),
                                contact_b2b.get('email'),
                                contact_b2b.get('region'),
                                contact_b2b.get('activity'),
                                contact_b2b.get('country')))

                            connection.commit()

                            print("The record is stored : contacts_for_b2b_contact_data_for_datarade : " + str(
                                contact_b2b))

                            connection.close()
                        except Exception as e:
                            print("The record already exists : " + str(e))
                            connection.close()
            else:
                print("no a class companyName")

    def test_extract_each_contact_from_all_pages_of_results_for_all_activities_and_all_capitals(self):
        print("test_extract_each_email_from_all_pages_of_results_for_all_activities_and_all_capitals")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        activites = [
            {'id': '1', 'url': 'employment'},  # Temporary employment agencies
            {'id': '2', 'url': 'real-estate'},  # Real estate
            {'id': '3', 'url': 'recruitment'},  # Recruiter
            {'id': '4', 'url': 'software'},  # software
            {'id': '5', 'url': 'hotel'},  # hotel
            {'id': '6', 'url': 'social'},  # social landlord
            {'id': '7', 'url': 'cleaning'},  # cleaning
            {'id': '8', 'url': 'charity'},  # charity
            {'id': '9', 'url': 'financial'},  # financial
            {'id': '10', 'url': 'restaurant'},  # restaurant
            {'id': '11', 'url': 'building'},  # building
            {'id': '12', 'url': 'hairdresser'},  # hairdresser
            {'id': '13', 'url': 'florist'},  # florist
            {'id': '14', 'url': 'locksmith'},  # locksmith
            {'id': '15', 'url': 'bakery'},  # bakery
            {'id': '16', 'url': 'insurance'},  # insurance
            {'id': '17', 'url': 'pharmacy'},  # pharmacy
            {'id': '18', 'url': 'mover'},  # mover
            {'id': '19', 'url': 'electricity'},  # electricity
            {'id': '20', 'url': 'plumbing'},  # plumbing
            {'id': '21', 'url': 'security'},  # security
            {'id': '22', 'url': 'attorney'},  # attorney
            {'id': '23', 'url': 'bank'},  # bank
            {'id': '24', 'url': 'garage'},  # garage
            {'id': '25', 'url': 'dentist'},  # dentist
            {'id': '26', 'url': 'doctor'},  # doctor
            {'id': '27', 'url': 'accountant'},  # accountant
            {'id': '28', 'url': 'grocery'},  # grocery stores
            {'id': '29', 'url': 'notary'},  # notary
            {'id': '30', 'url': 'jewellery'},  # jewellery
            {'id': '31', 'url': 'tailor'},  # tailor
            {'id': '32', 'url': 'butcher'},  # butcher
            {'id': '33', 'url': 'library'},  # library
            {'id': '34', 'url': 'architect'},  # architect
            {'id': '36', 'url': 'cement'},  # cement
            {'id': '37', 'url': 'heating'},  # heating
            {'id': '38', 'url': 'boat'},  # boat
            {'id': '39', 'url': 'cold'},  # cold
            {'id': '41', 'url': 'steel'},  # steel
            {'id': '42', 'url': 'chemical'},  # chemical
            {'id': '43', 'url': 'gas'},  # gas
            {'id': '44', 'url': 'gold'}  # gold
        ]

        capitales_du_monde = [
            {'id': '936', 'nom': 'aruba', 'pays': 'aruba'},
        ]

        try:
            for capitale in capitales_du_monde:
                for activite in activites:
                    activity = activite.get('url')

                    city = capitale.get('nom')

                    country = capitale.get('pays')

                    number_of_pages = 0

                    url_page = "https://www.findyello.com/" + city + "/?search=" + activity

                    time.sleep(2)

                    html_search = requests.get(url_page, headers=headers)

                    soup = BeautifulSoup(html_search.content, 'html.parser')

                    if soup.find("p", {"class": "strong small lighter"}) is not None:
                        number_of_pages_with_coma = int(soup.find("p", {"class": "strong small lighter"})
                                                        .text
                                                        .split("of")[1]
                                                        .replace(" ", "")
                                                        .replace("Results", "")
                                                        ) / 15

                        if int(str(number_of_pages_with_coma).split(".")[1][:1]) < 5:
                            number_of_pages += round(number_of_pages_with_coma) + 1
                            print('number_of_pages : ' + str(number_of_pages))
                        elif int(str(number_of_pages_with_coma).split(".")[1][:1]) >= 5:
                            number_of_pages += round(number_of_pages_with_coma)
                            print('number_of_pages : ' + str(number_of_pages))
                    else:
                        print("error pages")

                    i_1 = 0

                    if number_of_pages > 1:
                        for i in range(1, number_of_pages + 1):
                            if i < 20:
                                url = url_page + "&pageno=" + str(i)

                                print(url)

                                time.sleep(2)

                                # Request the content of a page from the url
                                html = requests.get(url, headers=headers)

                                # Parse the content of html_doc
                                soup = BeautifulSoup(html.content, 'html.parser')

                                if soup.find("h2", {'class': 'h4'}) is not None:
                                    all_a = soup.find_all("h2", {'class': 'h4'})

                                    for a in all_a:
                                        i_1 += 1

                                        url = "https://www.findyello.com" + a.find('a').get('href')

                                        time.sleep(2)

                                        # Request the content of a page from the url
                                        html = requests.get(url, headers=headers)

                                        # Parse the content of html_doc
                                        soup = BeautifulSoup(html.content, 'html.parser')

                                        # company_name
                                        company_name = ""

                                        if soup.select_one('#name') is not None:
                                            company_name += str(soup.select_one('#name').text.lower())
                                        else:
                                            if soup.find('span', {'itemprop': 'name'}) is not None:
                                                company_name += str(
                                                    soup.find('span', {'itemprop': 'name'}).text.lower())
                                            else:
                                                print("no company_name business")

                                        # postal_address
                                        postal_address = ""

                                        if soup.find('span', {'itemprop': 'streetAddress'}) is not None:
                                            postal_address += str(soup.find('span', {'itemprop': 'streetAddress'}).text
                                                                  .lower()
                                                                  .replace("\t", " ")
                                                                  .replace("\n", " ")
                                                                  .replace("\r", " ")
                                                                  .replace("           ", "")
                                                                  .replace("    ", "")
                                                                  )
                                        else:
                                            print("no postal_address business")

                                        # phone_number
                                        phone_number = ""

                                        if soup.select_one('#phone') is not None:
                                            phone_number += str(
                                                soup.select_one('#phone').text.lower().replace("\n", " / ").replace(
                                                    "\t", " / "))
                                        else:
                                            if soup.find('span', {'itemprop': 'telephone'}) is not None:
                                                phone_number += "(+1268) " + str(
                                                    soup.find('span', {'itemprop': 'telephone'})
                                                        .text
                                                        .lower()
                                                        .replace("\n", " / ")
                                                        .replace("\t", " / ")
                                                )
                                            else:
                                                print("no phone_number business")

                                        # website
                                        website = ""

                                        if soup.find("li", {'class': 'profile-menu-website'}) is not None:
                                            website += soup \
                                                .find("li", {'class': 'profile-menu-website'}) \
                                                .find("a") \
                                                .get("href") \
                                                .replace('https://www.findyello.com/redirector.php?yelref=', '') \
                                                .replace('%2F', '/') \
                                                .replace('%3A', ':')
                                        else:
                                            print("no website business")

                                        # email
                                        email = ""

                                        if soup.find("li", {'class': 'profile-menu-website'}) is not None:
                                            email += "info@" + soup \
                                                .find("li", {'class': 'profile-menu-website'}) \
                                                .find("a") \
                                                .get("href") \
                                                .replace(
                                                'https://www.findyello.com/redirector.php?yelref=https%3A%2F%2F', '') \
                                                .replace(
                                                'https://www.findyello.com/redirector.php?yelref=http%3A%2F%2F', '') \
                                                .replace('https://www.findyello.com/redirector.php?yelref=', '') \
                                                .replace('www.', '') \
                                                .replace('%2F', '') \
                                                .split('/')[0]
                                        else:
                                            print("no email business")

                                        contact_b2b = {
                                            "company_name": company_name,
                                            "postal_address": postal_address,
                                            "phone_number": phone_number,
                                            "website": website,
                                            "email": email,
                                            "region": city,
                                            "activity": activity,
                                            "country": country
                                        }

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
                                                sql = "INSERT INTO contacts_for_b2b_contact_data_for_datarade " \
                                                      "(company_name, postal_address, phone_number, website, email, region, " \
                                                      "activity, country) " \
                                                      "VALUE (%s, %s, %s, %s, %s, %s, %s, %s)"

                                                cursor.execute(sql, (
                                                    contact_b2b.get('company_name'),
                                                    contact_b2b.get('postal_address'),
                                                    contact_b2b.get('phone_number'),
                                                    contact_b2b.get('website'),
                                                    contact_b2b.get('email'),
                                                    contact_b2b.get('region'),
                                                    contact_b2b.get('activity'),
                                                    contact_b2b.get('country')))

                                                connection.commit()

                                                print(
                                                    "The record is stored : contacts_for_b2b_contact_data_for_datarade : " + str(
                                                        contact_b2b))

                                                connection.close()
                                            except Exception as e:
                                                print("The record already exists : " + str(e))
                                                connection.close()
                                else:
                                    print("no a class companyName")
                    else:
                        if soup.find("h2", {'class': 'h4'}) is not None:
                            all_a = soup.find_all("h2", {'class': 'h4'})

                            for a in all_a:
                                i_1 += 1

                                url = "https://www.findyello.com" + a.find('a').get('href')

                                time.sleep(2)

                                # Request the content of a page from the url
                                html = requests.get(url, headers=headers)

                                # Parse the content of html_doc
                                soup = BeautifulSoup(html.content, 'html.parser')

                                # company_name
                                company_name = ""

                                if soup.select_one('#name') is not None:
                                    company_name += str(soup.select_one('#name').text.lower())
                                else:
                                    if soup.find('span', {'itemprop': 'name'}) is not None:
                                        company_name += str(
                                            soup.find('span', {'itemprop': 'name'}).text.lower())
                                    else:
                                        print("no company_name business")

                                # postal_address
                                postal_address = ""

                                if soup.find('span', {'itemprop': 'streetAddress'}) is not None:
                                    postal_address += str(soup.find('span', {'itemprop': 'streetAddress'}).text
                                                          .lower()
                                                          .replace("\t", " ")
                                                          .replace("\n", " ")
                                                          .replace("\r", " ")
                                                          .replace("           ", "")
                                                          .replace("    ", "")
                                                          )
                                else:
                                    print("no postal_address business")

                                # phone_number
                                phone_number = ""

                                if soup.select_one('#phone') is not None:
                                    phone_number += str(
                                        soup.select_one('#phone').text.lower().replace("\n", " / ").replace(
                                            "\t", " / "))
                                else:
                                    if soup.find('span', {'itemprop': 'telephone'}) is not None:
                                        phone_number += "(+1268) " + str(
                                            soup.find('span', {'itemprop': 'telephone'})
                                                .text
                                                .lower()
                                                .replace("\n", " / ")
                                                .replace("\t", " / ")
                                        )
                                    else:
                                        print("no phone_number business")

                                # website
                                website = ""

                                if soup.find("li", {'class': 'profile-menu-website'}) is not None:
                                    website += soup \
                                        .find("li", {'class': 'profile-menu-website'}) \
                                        .find("a") \
                                        .get("href") \
                                        .replace('https://www.findyello.com/redirector.php?yelref=', '') \
                                        .replace('%2F', '/') \
                                        .replace('%3A', ':')
                                else:
                                    print("no website business")

                                # email
                                email = ""

                                if soup.find("li", {'class': 'profile-menu-website'}) is not None:
                                    email += "info@" + soup \
                                        .find("li", {'class': 'profile-menu-website'}) \
                                        .find("a") \
                                        .get("href") \
                                        .replace(
                                        'https://www.findyello.com/redirector.php?yelref=https%3A%2F%2F', '') \
                                        .replace(
                                        'https://www.findyello.com/redirector.php?yelref=http%3A%2F%2F', '') \
                                        .replace('https://www.findyello.com/redirector.php?yelref=', '') \
                                        .replace('www.', '') \
                                        .replace('%2F', '') \
                                        .split('/')[0]
                                else:
                                    print("no email business")

                                contact_b2b = {
                                    "company_name": company_name,
                                    "postal_address": postal_address,
                                    "phone_number": phone_number,
                                    "website": website,
                                    "email": email,
                                    "region": city,
                                    "activity": activity,
                                    "country": country
                                }

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
                                        sql = "INSERT INTO contacts_for_b2b_contact_data_for_datarade " \
                                              "(company_name, postal_address, phone_number, website, email, region, " \
                                              "activity, country) " \
                                              "VALUE (%s, %s, %s, %s, %s, %s, %s, %s)"

                                        cursor.execute(sql, (
                                            contact_b2b.get('company_name'),
                                            contact_b2b.get('postal_address'),
                                            contact_b2b.get('phone_number'),
                                            contact_b2b.get('website'),
                                            contact_b2b.get('email'),
                                            contact_b2b.get('region'),
                                            contact_b2b.get('activity'),
                                            contact_b2b.get('country')))

                                        connection.commit()

                                        print(
                                            "The record is stored : contacts_for_b2b_contact_data_for_datarade : " + str(
                                                contact_b2b))

                                        connection.close()
                                    except Exception as e:
                                        print("The record already exists : " + str(e))
                                        connection.close()
                        else:
                            print("no a class companyName")
        except Exception as e:
            print("error : " + str(e))


if __name__ == '__main__':
    unittest.main()
