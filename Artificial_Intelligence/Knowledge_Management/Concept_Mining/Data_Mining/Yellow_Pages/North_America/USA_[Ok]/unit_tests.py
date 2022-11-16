from bs4 import BeautifulSoup
import requests
import time
import pymysql.cursors
import unittest
from validate_email import validate_email

password = 'azerAZER123098,,,'


class UnitTestsDataMinerYellowPagesUsa(unittest.TestCase):
    def test_web_scraper_email_usa(self):
        def web_scraper_email_usa():
            activites = [
                {'id': '1',
                 'url': 'https://www.yellowpages.com/search?search_terms=Temporary+Employment+Agencies&geo_location_terms='},
                {'id': '2', 'url': 'https://www.yellowpages.com/search?search_terms=real+estate&geo_location_terms='},
                {'id': '3', 'url': 'https://www.yellowpages.com/search?search_terms=Recruiter&geo_location_terms='},
                {'id': '4', 'url': 'https://www.yellowpages.com/search?search_terms=software&geo_location_terms='},
                {'id': '5', 'url': 'https://www.yellowpages.com/search?search_terms=hotel&geo_location_terms='},
                {'id': '6',
                 'url': 'https://www.yellowpages.com/search?search_terms=social+landlord&geo_location_terms='},
                {'id': '7', 'url': 'https://www.yellowpages.com/search?search_terms=cleaning&geo_location_terms='},
                {'id': '8', 'url': 'https://www.yellowpages.com/search?search_terms=Charities&geo_location_terms='},
                {'id': '9', 'url': 'https://www.yellowpages.com/search?search_terms=financial&geo_location_terms='},
                {'id': '10', 'url': 'https://www.yellowpages.com/search?search_terms=restaurant&geo_location_terms='},
                {'id': '11', 'url': 'https://www.yellowpages.com/search?search_terms=building&geo_location_terms='},
                {'id': '12', 'url': 'https://www.yellowpages.com/search?search_terms=hairdresser&geo_location_terms='},
                {'id': '13', 'url': 'https://www.yellowpages.com/search?search_terms=florist&geo_location_terms='},
                {'id': '14', 'url': 'https://www.yellowpages.com/search?search_terms=locksmith&geo_location_terms='},
                {'id': '15', 'url': 'https://www.yellowpages.com/search?search_terms=bakery&geo_location_terms='},
                {'id': '16', 'url': 'https://www.yellowpages.com/search?search_terms=insurance&geo_location_terms='},
                {'id': '17', 'url': 'https://www.yellowpages.com/search?search_terms=Pharmacies&geo_location_terms='},
                {'id': '18', 'url': 'https://www.yellowpages.com/search?search_terms=movers&geo_location_terms='},
                {'id': '19', 'url': 'https://www.yellowpages.com/search?search_terms=electricity&geo_location_terms='},
                {'id': '20', 'url': 'https://www.yellowpages.com/search?search_terms=plumbing&geo_location_terms='},
                {'id': '21', 'url': 'https://www.yellowpages.com/search?search_terms=security&geo_location_terms='},
                {'id': '22', 'url': 'https://www.yellowpages.com/search?search_terms=attorney&geo_location_terms='},
                {'id': '23', 'url': 'https://www.yellowpages.com/search?search_terms=bank&geo_location_terms='},
                {'id': '24', 'url': 'https://www.yellowpages.com/search?search_terms=mechanic&geo_location_terms='},
                {'id': '25', 'url': 'https://www.yellowpages.com/search?search_terms=dentist&geo_location_terms='},
                {'id': '26', 'url': 'https://www.yellowpages.com/search?search_terms=doctor&geo_location_terms='},
                {'id': '27', 'url': 'https://www.yellowpages.com/search?search_terms=accountant&geo_location_terms='},
                {'id': '28',
                 'url': 'https://www.yellowpages.com/search?search_terms=Grocery+Stores&geo_location_terms='},
                {'id': '29', 'url': 'https://www.yellowpages.com/search?search_terms=notary&geo_location_terms='},
                {'id': '30', 'url': 'https://www.yellowpages.com/search?search_terms=jewellery&geo_location_terms='},
                {'id': '31', 'url': 'https://www.yellowpages.com/search?search_terms=tailors&geo_location_terms='},
                {'id': '32', 'url': 'https://www.yellowpages.com/search?search_terms=butcher&geo_location_terms='},
                {'id': '33', 'url': 'https://www.yellowpages.com/search?search_terms=library&geo_location_terms='},
                {'id': '34', 'url': 'https://www.yellowpages.com/search?search_terms=Architects&geo_location_terms='}
            ]

            capitales_du_monde = [
                {'id': '2', 'nom': 'New+York%2C+NY'},
                # {'id': '4', 'nom': 'Chicago%2C+IL'},
                # {'id': '5', 'nom': 'Atlanta%2C+GA'},
                # {'id': '6', 'nom': 'Houston%2C+TX'},
                # {'id': '7', 'nom': 'Los+Angeles%2C+CA'},
                # {'id': '9', 'nom': 'Albany%2C+NY'},
                # {'id': '36', 'nom': 'Montgomery%2C+AL'},
                # {'id': '37', 'nom': 'Birmingham%2C+AL'},
                # {'id': '38', 'nom': 'Juneau%2C+AK'},
                # {'id': '39', 'nom': 'Anchorage%2C+AK'},
                # {'id': '40', 'nom': 'Phoenix%2C+AZ'},
                # {'id': '41', 'nom': 'Little+Rock%2C+AR'},
                # {'id': '42', 'nom': 'Sacramento%2C+CA'},
                # {'id': '43', 'nom': 'Denver%2C+CO'},
                # {'id': '44', 'nom': 'Hartford%2C+CT'},
                # {'id': '45', 'nom': 'Bridgeport%2C+CT'},
                # {'id': '46', 'nom': 'Dover%2C+DE'},
                # {'id': '47', 'nom': 'Wilmington%2C+DE'},
                # {'id': '48', 'nom': 'Tallahassee%2C+FL'},
                # {'id': '49', 'nom': 'Jacksonville%2C+FL'},
                # {'id': '50', 'nom': 'Honolulu%2C+HI'},
                # {'id': '51', 'nom': 'Boise%2C+ID'},
                # {'id': '52', 'nom': 'Springfield%2C+IL'},
                # {'id': '53', 'nom': 'Indianapolis%2C+IN'},
                # {'id': '54', 'nom': 'Des+Moines%2C+IA'},
                # {'id': '55', 'nom': 'Topeka%2C+KS'},
                # {'id': '56', 'nom': 'Wichita%2C+KS'},
                # {'id': '57', 'nom': 'Frankfort%2C+KY'},
                # {'id': '58', 'nom': 'Louisville%2C+KY'},
                # {'id': '59', 'nom': 'Baton+Rouge%2C+LA'},
                # {'id': '60', 'nom': 'New+Orleans%2C+LA'},
                # {'id': '61', 'nom': 'Augusta%2C+ME'},
                # {'id': '62', 'nom': 'Portland%2C+ME'},
                # {'id': '63', 'nom': 'Annapolis%2C+MD'},
                # {'id': '64', 'nom': 'Baltimore%2C+MD'},
                # {'id': '65', 'nom': 'Boston%2C+MA'},
                # {'id': '66', 'nom': 'Lansing%2C+MI'},
                # {'id': '67', 'nom': 'Detroit%2C+MI'},
                # {'id': '68', 'nom': 'Saint+Paul%2C+MN'},
                # {'id': '69', 'nom': 'Minneapolis%2C+MN'},
                # {'id': '70', 'nom': 'Jackson%2C+MS'},
                # {'id': '71', 'nom': 'Jefferson+City%2C+MO'},
                # {'id': '72', 'nom': 'Kansas+City%2C+MO'},
                # {'id': '73', 'nom': 'Helena%2C+MT'},
                # {'id': '74', 'nom': 'Billings%2C+MT'},
                # {'id': '75', 'nom': 'Lincoln%2C+NE'},
                # {'id': '76', 'nom': 'Omaha%2C+NE'},
                # {'id': '77', 'nom': 'Carson+City%2C+NV'},
                # {'id': '78', 'nom': 'Las+Vegas%2C+NV'},
                # {'id': '79', 'nom': 'Concord%2C+NH'},
                # {'id': '80', 'nom': 'Manchester%2C+NH'}
                # {'id': '81', 'nom': 'Trenton%2C+NJ'},
                # {'id': '82', 'nom': 'Newark%2C+NJ'},
                # {'id': '83', 'nom': 'Santa+Fe%2C+NM'},
                # {'id': '84', 'nom': 'Albuquerque%2C+NM'},
                # {'id': '85', 'nom': 'Raleigh%2C+NC'},
                # {'id': '86', 'nom': 'Charlotte%2C+NC'},
                # {'id': '87', 'nom': 'Bismarck%2C+ND'},
                # {'id': '88', 'nom': 'Columbus%2C+OH'},
                # {'id': '89', 'nom': 'Oklahoma+City%2C+OK'},
                # {'id': '90', 'nom': 'Salem%2C+OR'},
                # {'id': '91', 'nom': 'Portland%2C+OR'},
                # {'id': '92', 'nom': 'Harrisburg%2C+PA'},
                # {'id': '93', 'nom': 'Philadelphia%2C+PA'},
                # {'id': '94', 'nom': 'Providence%2C+RI'},
                # {'id': '95', 'nom': 'Columbia%2C+SC'},
                # {'id': '96', 'nom': 'Pierre%2C+SD'},
                # {'id': '97', 'nom': 'Sioux+Falls%2C+SD'},
                # {'id': '98', 'nom': 'Nashville%2C+TN'},
                # {'id': '99', 'nom': 'Memphis%2C+TN'},
                # {'id': '100', 'nom': 'Austin%2C+TX'},
                # {'id': '101', 'nom': 'Salt+Lake+City%2C+UT'},
                # {'id': '102', 'nom': 'Montpelier%2C+VT'},
                # {'id': '103', 'nom': 'Burlington%2C+VT'},
                # {'id': '104', 'nom': 'Richmond%2C+VA'},
                # {'id': '105', 'nom': 'Olympia%2C+WA'},
                # {'id': '106', 'nom': 'Seattle%2C+WA'},
                # {'id': '107', 'nom': 'Charleston%2C+WV'},
                # {'id': '108', 'nom': 'Madison%2C+WI'},
                # {'id': '109', 'nom': 'Milwaukee%2C+WI'},
                # {'id': '110', 'nom': 'Cheyenne%2C+WY'}
            ]

            try:
                for capitale_du_monde in capitales_du_monde:
                    for activite in activites:
                        i_1 = 0

                        i = 1

                        var = 1

                        while var == 1 and i < 102:
                            try:
                                url = activite.get('url') + capitale_du_monde.get('nom') + "&page=" + str(i)

                                # Request the content of a page from the url
                                html = requests.get(url)

                                time.sleep(3)

                                # Parse the content of html_doc
                                soup = BeautifulSoup(html.content, 'html.parser')

                                print(url)

                                if soup.find("a", {"class", "business-name"}) is None:
                                    print('sorry there is nothing')
                                    break
                                else:
                                    try:
                                        for link in soup.find_all("a", {"class": "business-name"}):
                                            i_1 += 1

                                            # Request the content of a page from the url
                                            url_page = "https://www.yellowpages.com" + link.get('href')

                                            html_doc = requests.get(url_page)

                                            time.sleep(3)

                                            # Parse the content of html_doc
                                            soup_link = BeautifulSoup(html_doc.content, 'html.parser')

                                            if soup_link.find("a", {"class": "email-business"}) is not None:
                                                email_business = soup_link.select(".email-business")[0].get('href')[7:]

                                                suffixes = [
                                                    "contact@",
                                                    "client@",
                                                    "clients@",
                                                    "sav@",
                                                    "customer@",
                                                    "fournisseur@",
                                                    "fournisseurs@",
                                                    "provider@",
                                                    "investisseur@",
                                                    "investor@",
                                                    "info@",
                                                    "accueil@",
                                                    "home@",
                                                    "compta@",
                                                    "rh@",
                                                    "marketing@",
                                                    "infos@",
                                                    "Info@",
                                                    "informations@",
                                                    "secretariat@",
                                                    "agence@",
                                                    "bienvenue@",
                                                    "direction@",
                                                    "comptabilite@",
                                                    "administration@",
                                                    "finances@",
                                                    "commercial@",
                                                    "communication@",
                                                    "magasin@",
                                                    "sales@",
                                                    "boutique@",
                                                    "commande@",
                                                    "studio@",
                                                    "export@",
                                                    "maintenance@",
                                                    "production@",
                                                    "logistique@",
                                                    "exploitation@",
                                                    "be@",
                                                    "etudes@",
                                                    "methode@",
                                                    "maintenance@",
                                                    "production@",
                                                    "logistique@",
                                                    "exploitation@",
                                                    "drh@",
                                                    "qualite@",
                                                    "recrutement@",
                                                    "formation@",
                                                    "ce@",
                                                    "chsct@",
                                                    "qse@",
                                                    "handicap@",
                                                    "webmaster@",
                                                    "dsi@",
                                                    "mail@",
                                                    "admin@",
                                                    "web@",
                                                    "support@",
                                                    "hotel@",
                                                    "reservation@",
                                                    "reservations@",
                                                    "reception@",
                                                    "restaurant@",
                                                    "resa@",
                                                    "camping@",
                                                    "welcome@",
                                                    "hr@",
                                                    "agency@"
                                                ]

                                                for suffix in suffixes:
                                                    email = str(suffix + email_business.split("@")[1])

                                                    try:
                                                        is_valid = validate_email(
                                                            email_address=email,
                                                            check_regex=True,
                                                            check_mx=True,
                                                            from_address='jason.aymerick.jean.aloyau@gmail.com',
                                                            helo_host='smtp.gmail.com',
                                                            smtp_timeout=10,
                                                            dns_timeout=10,
                                                            use_blacklist=True
                                                        )

                                                        if is_valid:
                                                            try:
                                                                # Connect to the database
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
                                                                            capitale_du_monde.get('id'),
                                                                            email))
                                                                        connection.commit()
                                                                        print(str(i_1) + " The record is stored : "
                                                                              + str(email))
                                                                        connection.close()
                                                                    except Exception as e:
                                                                        print(str(i_1) + " The record already exists : "
                                                                              + str(email) + " " + str(e))
                                                                        connection.close()
                                                            except Exception as e:
                                                                print("Problem connection MySQL : " + str(e))
                                                        else:
                                                            print(
                                                                str(i_1) + " The email : " + email + " doesn't exist.")
                                                    except Exception as e:
                                                        print(str(
                                                            i_1) + " An error with the email : " + email + " " + str(e))
                                            else:
                                                print(str(i_1) + " no email business")
                                    except Exception as e:
                                        print("There is an error connection at url_page : " + str(e))
                            except Exception as e:
                                print("There is an error connection at url : " + str(e))

                            i += 1
            finally:
                print('done')

        web_scraper_email_usa()

    # table : contacts_for_b2b_contact_data_for_datarade

    # region : myself
    # activity : myself
    # country : myself

    # company_name : ok
    def test_extract_company_name_from_one_result(self):
        print("test_extract_company_name_from_one_result")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://www.yellowpages.com/los-angeles-ca/mip/reliable-resources-inc-21956875?lid=1002007260971"

        time.sleep(3)

        html = requests.get(url, headers=headers)

        soup = BeautifulSoup(html.content, 'html.parser')

        # company_name
        company_name = ""

        if soup.find('h1', {'class': 'dockable business-name'}) is not None:
            company_name += str(soup.find('h1', {'class': 'dockable business-name'}).text.lower())

            print("company_name : " + company_name)
        else:
            print('no company_name')

    # postal_address : ok
    def test_extract_postal_address_from_one_result(self):
        print("test_extract_postal_address_from_one_result")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://www.yellowpages.com/los-angeles-ca/mip/reliable-resources-inc-21956875?lid=1002007260971"

        time.sleep(3)

        html = requests.get(url, headers=headers)

        soup = BeautifulSoup(html.content, 'html.parser')

        # postal_address
        postal_address = ""

        if soup.find('span', {'class': 'address'}) is not None:
            postal_address += str(soup.find('span', {'class': 'address'}).text
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

    # phone_number : ok
    def test_extract_phone_number_from_one_result(self):
        print("test_extract_phone_number_from_one_result")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://www.yellowpages.com/los-angeles-ca/mip/reliable-resources-inc-21956875?lid=1002007260971"

        time.sleep(3)

        html = requests.get(url, headers=headers)

        soup = BeautifulSoup(html.content, 'html.parser')

        # phone_number
        phone_number = ""

        if soup.find('a', {'class': 'phone dockable'}) is not None:
            phone_number += str(soup.find('a', {'class': 'phone dockable'}).get('href').lower()
                                .replace("\n", " / ")
                                .replace("\t", " / ")
                                )

            print("phone_number : " + phone_number)
        else:
            print("no phone_number business")

    # website : ok
    def test_extract_website_from_one_result(self):
        print("test_extract_email_from_one_result")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://www.yellowpages.com/los-angeles-ca/mip/recruiting-resources-561337842"

        time.sleep(3)

        html = requests.get(url, headers=headers)

        soup = BeautifulSoup(html.content, 'html.parser')

        # website
        website = ""

        if soup.find("a", {'class': 'website-link dockable'}) is not None:
            website += str(
                soup.find("a", {'class': 'website-link dockable'}).get("href").lower()
            )

            print("website : " + website)
        else:
            print("no website business")

    # email : ok
    def test_extract_email_from_one_result(self):
        print("test_extract_email_from_one_result")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://www.yellowpages.com/los-angeles-ca/mip/reliable-resources-inc-21956875?lid=1002007260971"

        time.sleep(3)

        html = requests.get(url, headers=headers)

        soup = BeautifulSoup(html.content, 'html.parser')

        # email
        email = ""

        if soup.find("a", {'class': 'email-business'}) is not None:
            email += str(
                soup.find("a", {'class': 'email-business'})
                .get("href")
                .lower()
                .replace('mailto:', '')
            )

            print("email : " + email)
        else:
            print("no email business")

    # ok
    def test_extract_the_number_of_pages(self):
        print("test_extract_the_number_of_pages")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://www.yellowpages.com/search?search_terms=Recruiting%20Resources&geo_location_terms=Los%20Angeles%2C%20CA"

        time.sleep(3)

        html = requests.get(url, headers=headers)

        soup = BeautifulSoup(html.content, 'html.parser')

        # number_of_pages
        number_of_pages = 0

        if soup.find("div", {"class": "pagination"}) is not None:
            number_of_pages_with_coma = int(soup.find("div", {"class": "pagination"}).find("span")
                                            .text
                                            .split("of")[1]
                                            .replace(" ", "")
                                            ) / 30

            if int(str(number_of_pages_with_coma).split(".")[1][:1]) < 5:
                number_of_pages += round(number_of_pages_with_coma) + 1
                print('number_of_pages : ' + str(number_of_pages))
            elif int(str(number_of_pages_with_coma).split(".")[1][:1]) >= 5:
                number_of_pages += round(number_of_pages_with_coma)
                print('number_of_pages : ' + str(number_of_pages))
        else:
            print("error pages")

    # ok
    def test_extract_each_url_contact_from_all_pages_of_results_for_one_activity_and_one_capital(self):
        print("test_extract_each_url_contact_from_all_pages_of_results_for_one_activity_and_one_capital")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        activity = "Recruiting%20Resources"

        city = "Los%20Angeles%2C%20CA"

        country = "USA"

        url_page = "https://www.yellowpages.com/search?search_terms=" + activity \
                   + "&geo_location_terms=" + city

        time.sleep(2)

        html = requests.get(url_page, headers=headers)

        soup = BeautifulSoup(html.content, 'html.parser')

        # number_of_pages
        number_of_pages = 0

        if soup.find("div", {"class": "pagination"}) is not None:
            number_of_pages_with_coma = int(soup.find("div", {"class": "pagination"}).find("span")
                                            .text
                                            .split("of")[1]
                                            .replace(" ", "")
                                            ) / 30

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
                url_results = url_page + "&page=" + str(i)

                print(url_results)

                time.sleep(2)

                html = requests.get(url_results, headers=headers)

                soup = BeautifulSoup(html.content, 'html.parser')

                if soup.find("a", {'class': 'business-name'}) is not None:
                    all_a = soup.find_all("a", {'class': 'business-name'})

                    for a in all_a:
                        i_1 += 1

                        url = "https://www.yellowpages.com" + a.get('href')

                        time.sleep(2)

                        print('url : ' + url)

    # ok
    def test_extract_each_contact_from_all_pages_of_results_for_one_activity_and_one_capital_into_mysql(self):
        print("test_extract_each_contact_from_all_pages_of_results_for_one_activity_and_one_capital_into_mysql")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        activity = "Recruiting%20Resources"

        city = "Los%20Angeles%2C%20CA"

        country = "USA"

        url_page = "https://www.yellowpages.com/search?search_terms=" + activity \
                   + "&geo_location_terms=" + city

        time.sleep(2)

        html = requests.get(url_page, headers=headers)

        soup = BeautifulSoup(html.content, 'html.parser')

        # number_of_pages
        number_of_pages = 0

        if soup.find("div", {"class": "pagination"}) is not None:
            number_of_pages_with_coma = int(soup.find("div", {"class": "pagination"}).find("span")
                                            .text
                                            .split("of")[1]
                                            .replace(" ", "")
                                            ) / 30

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
                url_results = url_page + "&page=" + str(i)

                print("url_results : " + url_results)

                time.sleep(2)

                html_results = requests.get(url_results, headers=headers)

                soup_results = BeautifulSoup(html_results.content, 'html.parser')

                if soup_results.find("a", {'class': 'business-name'}) is not None:
                    all_a = soup_results.find_all("a", {'class': 'business-name'})

                    for a in all_a:
                        i_1 += 1

                        url_contact = "https://www.yellowpages.com" + a.get('href')

                        time.sleep(2)

                        html_contact = requests.get(url_contact, headers=headers)

                        soup_contact = BeautifulSoup(html_contact.content, 'html.parser')

                        # company_name
                        company_name = ""

                        if soup_contact.find('h1', {'class': 'dockable business-name'}) is not None:
                            company_name += str(soup_contact.find('h1', {'class': 'dockable business-name'}).text.lower())
                        else:
                            print('no company_name')

                        # postal_address
                        postal_address = ""

                        if soup_contact.find('span', {'class': 'address'}) is not None:
                            postal_address += str(soup_contact.find('span', {'class': 'address'}).text
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

                        if soup_contact.find('a', {'class': 'phone dockable'}) is not None:
                            phone_number += str(soup_contact.find('a', {'class': 'phone dockable'}).get('href').lower()
                                                .replace("\n", " / ")
                                                .replace("\t", " / ")
                                                )
                        else:
                            print("no phone_number business")

                        # website
                        website = ""

                        if soup_contact.find("a", {'class': 'website-link dockable'}) is not None:
                            website += str(
                                soup_contact.find("a", {'class': 'website-link dockable'}).get("href").lower()
                            )
                        else:
                            print("no website business")

                        # email
                        email = ""

                        if soup_contact.find("a", {'class': 'email-business'}) is not None:
                            email += str(
                                soup_contact.find("a", {'class': 'email-business'})
                                    .get("href")
                                    .lower()
                                    .replace('mailto:', '')
                            )
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
                            password=password,
                            db='contacts_professionnels',
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor
                        )

                        with connection.cursor() as cursor:
                            try:
                                sql = "INSERT INTO contacts_for_b2b_contact_data_for_datarade " \
                                      "(company_name, postal_address, phone_number, " \
                                      "website, email, region, " \
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

                                print("The record is stored : " + str(i_1) + " contact_b2b : " + str(contact_b2b))

                                connection.close()
                            except Exception as e:
                                print("The record already exists : " + str(e))
                                connection.close()
                else:
                    print("no a class companyName")
        else:
            if soup.find("a", {'class': 'business-name'}) is not None:
                all_a = soup.find_all("a", {'class': 'business-name'})

                for a in all_a:
                    i_1 += 1

                    url_contact = "https://www.yellowpages.com" + a.get('href')

                    time.sleep(2)

                    html_contact = requests.get(url_contact, headers=headers)

                    soup_contact = BeautifulSoup(html_contact.content, 'html.parser')

                    # company_name
                    company_name = ""

                    if soup_contact.find('h1', {'class': 'dockable business-name'}) is not None:
                        company_name += str(soup_contact.find('h1', {'class': 'dockable business-name'}).text.lower())
                    else:
                        print('no company_name')

                    # postal_address
                    postal_address = ""

                    if soup_contact.find('span', {'class': 'address'}) is not None:
                        postal_address += str(soup_contact.find('span', {'class': 'address'}).text
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

                    if soup_contact.find('a', {'class': 'phone dockable'}) is not None:
                        phone_number += str(soup_contact.find('a', {'class': 'phone dockable'}).get('href').lower()
                                            .replace("\n", " / ")
                                            .replace("\t", " / ")
                                            )
                    else:
                        print("no phone_number business")

                    # website
                    website = ""

                    if soup_contact.find("a", {'class': 'website-link dockable'}) is not None:
                        website += str(
                            soup_contact.find("a", {'class': 'website-link dockable'}).get("href").lower()
                        )
                    else:
                        print("no website business")

                    # email
                    email = ""

                    if soup_contact.find("a", {'class': 'email-business'}) is not None:
                        email += str(
                            soup_contact.find("a", {'class': 'email-business'})
                                .get("href")
                                .lower()
                                .replace('mailto:', '')
                        )
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
                        password=password,
                        db='contacts_professionnels',
                        charset='utf8mb4',
                        cursorclass=pymysql.cursors.DictCursor
                    )

                    with connection.cursor() as cursor:
                        try:
                            sql = "INSERT INTO contacts_for_b2b_contact_data_for_datarade " \
                                  "(company_name, postal_address, phone_number, " \
                                  "website, email, region, " \
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

                            print("The record is stored : " + str(i_1) + " contact_b2b : " + str(contact_b2b))

                            connection.close()
                        except Exception as e:
                            print("The record already exists : " + str(e))
                            connection.close()
            else:
                print("no a class companyName")

    # ok
    def test_extract_each_email_from_all_pages_of_results_for_all_activities_and_all_capitals_into_mysql(self):
        print("test_extract_each_email_from_all_pages_of_results_for_all_activities_and_all_capitals_into_mysql")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        activites = [
            {'id': '1', 'url': 'Temporary+Employment+Agencies', 'start': 8},
            {'id': '2', 'url': 'real+estate', 'start': 1},
            {'id': '3', 'url': 'Recruiter', 'start': 1},
            {'id': '4', 'url': 'software', 'start': 1},
            {'id': '5', 'url': 'hotel', 'start': 1},
            {'id': '6', 'url': 'social+landlord', 'start': 1},
            {'id': '7', 'url': 'cleaning', 'start': 1},
            {'id': '8', 'url': 'Charities', 'start': 1},
            {'id': '9', 'url': 'financial', 'start': 1},
            {'id': '10', 'url': 'restaurant', 'start': 1},
            {'id': '11', 'url': 'building', 'start': 1},
            {'id': '12', 'url': 'hairdresser', 'start': 1},
            {'id': '13', 'url': 'florist', 'start': 1},
            {'id': '14', 'url': 'locksmith', 'start': 1},
            {'id': '15', 'url': 'bakery', 'start': 1},
            {'id': '16', 'url': 'insurance', 'start': 1},
            {'id': '17', 'url': 'Pharmacies', 'start': 1},
            {'id': '18', 'url': 'movers', 'start': 1},
            {'id': '19', 'url': 'electricity', 'start': 1},
            {'id': '20', 'url': 'plumbing', 'start': 1},
            {'id': '21', 'url': 'security', 'start': 1},
            {'id': '22', 'url': 'attorney', 'start': 1},
            {'id': '23', 'url': 'bank', 'start': 1},
            {'id': '24', 'url': 'mechanic', 'start': 1},
            {'id': '25', 'url': 'dentist', 'start': 1},
            {'id': '26', 'url': 'doctor', 'start': 1},
            {'id': '27', 'url': 'accountant', 'start': 1},
            {'id': '28', 'url': 'Grocery+Stores', 'start': 1},
            {'id': '29', 'url': 'notary', 'start': 1},
            {'id': '30', 'url': 'jewellery', 'start': 1},
            {'id': '31', 'url': 'tailors', 'start': 1},
            {'id': '32', 'url': 'butcher', 'start': 1},
            {'id': '33', 'url': 'library', 'start': 1},
            {'id': '34', 'url': 'Architects', 'start': 1},
            {'id': '36', 'url': 'Cement', 'start': 1},  # cement
            {'id': '37', 'url': 'Heating', 'start': 1},  # heating
            {'id': '38', 'url': 'Boat', 'start': 1},  # boat
            {'id': '39', 'url': 'Cold', 'start': 1},  # cold
            {'id': '40', 'url': 'Car', 'start': 1},
            {'id': '41', 'url': 'Steel', 'start': 1},  # steel
            {'id': '42', 'url': 'Chemicals', 'start': 1},  # chemicals
            {'id': '43', 'url': 'Gas', 'start': 1},  # gas
            {'id': '44', 'url': 'Gold', 'start': 1},  # gold
            {'id': '45', 'url': 'Energy', 'start': 1}
        ]

        capitales_du_monde = [
            {'id': '2', 'nom': 'New+York%2C+NY'},
            # {'id': '4', 'nom': 'Chicago%2C+IL'},
            # {'id': '5', 'nom': 'Atlanta%2C+GA'},
            # {'id': '6', 'nom': 'Houston%2C+TX'},
            # {'id': '7', 'nom': 'Los+Angeles%2C+CA'},
            # {'id': '9', 'nom': 'Albany%2C+NY'},
            # {'id': '36', 'nom': 'Montgomery%2C+AL'},
            # {'id': '37', 'nom': 'Birmingham%2C+AL'},
            # {'id': '38', 'nom': 'Juneau%2C+AK'},
            # {'id': '39', 'nom': 'Anchorage%2C+AK'},
            # {'id': '40', 'nom': 'Phoenix%2C+AZ'},
            # {'id': '41', 'nom': 'Little+Rock%2C+AR'},
            # {'id': '42', 'nom': 'Sacramento%2C+CA'},
            # {'id': '43', 'nom': 'Denver%2C+CO'},
            # {'id': '44', 'nom': 'Hartford%2C+CT'},
            # {'id': '45', 'nom': 'Bridgeport%2C+CT'},
            # {'id': '46', 'nom': 'Dover%2C+DE'},
            # {'id': '47', 'nom': 'Wilmington%2C+DE'},
            # {'id': '48', 'nom': 'Tallahassee%2C+FL'},
            # {'id': '49', 'nom': 'Jacksonville%2C+FL'},
            # {'id': '50', 'nom': 'Honolulu%2C+HI'},
            # {'id': '51', 'nom': 'Boise%2C+ID'},
            # {'id': '52', 'nom': 'Springfield%2C+IL'},
            # {'id': '53', 'nom': 'Indianapolis%2C+IN'},
            # {'id': '54', 'nom': 'Des+Moines%2C+IA'},
            # {'id': '55', 'nom': 'Topeka%2C+KS'},
            # {'id': '56', 'nom': 'Wichita%2C+KS'},
            # {'id': '57', 'nom': 'Frankfort%2C+KY'},
            # {'id': '58', 'nom': 'Louisville%2C+KY'},
            # {'id': '59', 'nom': 'Baton+Rouge%2C+LA'},
            # {'id': '60', 'nom': 'New+Orleans%2C+LA'},
            # {'id': '61', 'nom': 'Augusta%2C+ME'},
            # {'id': '62', 'nom': 'Portland%2C+ME'},
            # {'id': '63', 'nom': 'Annapolis%2C+MD'},
            # {'id': '64', 'nom': 'Baltimore%2C+MD'},
            # {'id': '65', 'nom': 'Boston%2C+MA'},
            # {'id': '66', 'nom': 'Lansing%2C+MI'},
            # {'id': '67', 'nom': 'Detroit%2C+MI'},
            # {'id': '68', 'nom': 'Saint+Paul%2C+MN'},
            # {'id': '69', 'nom': 'Minneapolis%2C+MN'},
            # {'id': '70', 'nom': 'Jackson%2C+MS'},
            # {'id': '71', 'nom': 'Jefferson+City%2C+MO'},
            # {'id': '72', 'nom': 'Kansas+City%2C+MO'},
            # {'id': '73', 'nom': 'Helena%2C+MT'},
            # {'id': '74', 'nom': 'Billings%2C+MT'},
            # {'id': '75', 'nom': 'Lincoln%2C+NE'},
            # {'id': '76', 'nom': 'Omaha%2C+NE'},
            # {'id': '77', 'nom': 'Carson+City%2C+NV'},
            # {'id': '78', 'nom': 'Las+Vegas%2C+NV'},
            # {'id': '79', 'nom': 'Concord%2C+NH'},
            # {'id': '80', 'nom': 'Manchester%2C+NH'}
            # {'id': '81', 'nom': 'Trenton%2C+NJ'},
            # {'id': '82', 'nom': 'Newark%2C+NJ'},
            # {'id': '83', 'nom': 'Santa+Fe%2C+NM'},
            # {'id': '84', 'nom': 'Albuquerque%2C+NM'},
            # {'id': '85', 'nom': 'Raleigh%2C+NC'},
            # {'id': '86', 'nom': 'Charlotte%2C+NC'},
            # {'id': '87', 'nom': 'Bismarck%2C+ND'},
            # {'id': '88', 'nom': 'Columbus%2C+OH'},
            # {'id': '89', 'nom': 'Oklahoma+City%2C+OK'},
            # {'id': '90', 'nom': 'Salem%2C+OR'},
            # {'id': '91', 'nom': 'Portland%2C+OR'},
            # {'id': '92', 'nom': 'Harrisburg%2C+PA'},
            # {'id': '93', 'nom': 'Philadelphia%2C+PA'},
            # {'id': '94', 'nom': 'Providence%2C+RI'},
            # {'id': '95', 'nom': 'Columbia%2C+SC'},
            # {'id': '96', 'nom': 'Pierre%2C+SD'},
            # {'id': '97', 'nom': 'Sioux+Falls%2C+SD'},
            # {'id': '98', 'nom': 'Nashville%2C+TN'},
            # {'id': '99', 'nom': 'Memphis%2C+TN'},
            # {'id': '100', 'nom': 'Austin%2C+TX'},
            # {'id': '101', 'nom': 'Salt+Lake+City%2C+UT'},
            # {'id': '102', 'nom': 'Montpelier%2C+VT'},
            # {'id': '103', 'nom': 'Burlington%2C+VT'},
            # {'id': '104', 'nom': 'Richmond%2C+VA'},
            # {'id': '105', 'nom': 'Olympia%2C+WA'},
            # {'id': '106', 'nom': 'Seattle%2C+WA'},
            # {'id': '107', 'nom': 'Charleston%2C+WV'},
            # {'id': '108', 'nom': 'Madison%2C+WI'},
            # {'id': '109', 'nom': 'Milwaukee%2C+WI'},
            # {'id': '110', 'nom': 'Cheyenne%2C+WY'}
        ]

        try:
            for capitale in capitales_du_monde:
                for activite in activites:
                    activity = activite.get("url")

                    city = capitale.get('nom')

                    country = "usa"

                    url_page = "https://www.yellowpages.com/search?search_terms=" + activity \
                               + "&geo_location_terms=" + city

                    time.sleep(2)

                    html = requests.get(url_page, headers=headers)

                    soup = BeautifulSoup(html.content, 'html.parser')

                    # number_of_pages
                    number_of_pages = 0

                    if soup.find("div", {"class": "pagination"}) is not None:
                        number_of_pages_with_coma = int(soup.find("div", {"class": "pagination"}).find("span")
                                                        .text
                                                        .split("of")[1]
                                                        .replace(" ", "")
                                                        ) / 30

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
                        for i in range(activite.get('start'), number_of_pages + 1):
                            url_results = url_page + "&page=" + str(i)

                            print("url_results : " + url_results)

                            time.sleep(2)

                            html_results = requests.get(url_results, headers=headers)

                            soup_results = BeautifulSoup(html_results.content, 'html.parser')

                            if soup_results.find("a", {'class': 'business-name'}) is not None:
                                all_a = soup_results.find_all("a", {'class': 'business-name'})

                                for a in all_a:
                                    i_1 += 1

                                    url_contact = "https://www.yellowpages.com" + a.get('href')

                                    time.sleep(2)

                                    html_contact = requests.get(url_contact, headers=headers)

                                    soup_contact = BeautifulSoup(html_contact.content, 'html.parser')

                                    # company_name
                                    company_name = ""

                                    if soup_contact.find('h1', {'class': 'dockable business-name'}) is not None:
                                        company_name += str(
                                            soup_contact.find('h1', {'class': 'dockable business-name'}).text.lower())
                                    else:
                                        print('no company_name')

                                    # postal_address
                                    postal_address = ""

                                    if soup_contact.find('span', {'class': 'address'}) is not None:
                                        postal_address += str(soup_contact.find('span', {'class': 'address'}).text
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

                                    if soup_contact.find('a', {'class': 'phone dockable'}) is not None:
                                        phone_number += str(
                                            soup_contact.find('a', {'class': 'phone dockable'}).get('href').lower()
                                            .replace("\n", " / ")
                                            .replace("\t", " / ")
                                            )
                                    else:
                                        print("no phone_number business")

                                    # website
                                    website = ""

                                    if soup_contact.find("a", {'class': 'website-link dockable'}) is not None:
                                        website += str(
                                            soup_contact.find("a", {'class': 'website-link dockable'}).get(
                                                "href").lower()
                                        )
                                    else:
                                        print("no website business")

                                    # email
                                    email = ""

                                    if soup_contact.find("a", {'class': 'email-business'}) is not None:
                                        email += str(
                                            soup_contact.find("a", {'class': 'email-business'})
                                                .get("href")
                                                .lower()
                                                .replace('mailto:', '')
                                        )
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
                                        password=password,
                                        db='contacts_professionnels',
                                        charset='utf8mb4',
                                        cursorclass=pymysql.cursors.DictCursor
                                    )

                                    with connection.cursor() as cursor:
                                        try:
                                            sql = "INSERT INTO contacts_for_b2b_contact_data_for_datarade " \
                                                  "(company_name, postal_address, phone_number, " \
                                                  "website, email, region, " \
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

                                            print("The record is stored : " + str(i_1) + " contact_b2b : " + str(
                                                contact_b2b))

                                            connection.close()
                                        except Exception as e:
                                            print("The record already exists : " + str(e))
                                            connection.close()
                            else:
                                print("no a class companyName")
                    else:
                        if soup.find("a", {'class': 'business-name'}) is not None:
                            all_a = soup.find_all("a", {'class': 'business-name'})

                            for a in all_a:
                                i_1 += 1

                                url_contact = "https://www.yellowpages.com" + a.get('href')

                                time.sleep(2)

                                html_contact = requests.get(url_contact, headers=headers)

                                soup_contact = BeautifulSoup(html_contact.content, 'html.parser')

                                # company_name
                                company_name = ""

                                if soup_contact.find('h1', {'class': 'dockable business-name'}) is not None:
                                    company_name += str(
                                        soup_contact.find('h1', {'class': 'dockable business-name'}).text.lower())
                                else:
                                    print('no company_name')

                                # postal_address
                                postal_address = ""

                                if soup_contact.find('span', {'class': 'address'}) is not None:
                                    postal_address += str(soup_contact.find('span', {'class': 'address'}).text
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

                                if soup_contact.find('a', {'class': 'phone dockable'}) is not None:
                                    phone_number += str(
                                        soup_contact.find('a', {'class': 'phone dockable'}).get('href').lower()
                                        .replace("\n", " / ")
                                        .replace("\t", " / ")
                                        )
                                else:
                                    print("no phone_number business")

                                # website
                                website = ""

                                if soup_contact.find("a", {'class': 'website-link dockable'}) is not None:
                                    website += str(
                                        soup_contact.find("a", {'class': 'website-link dockable'}).get("href").lower()
                                    )
                                else:
                                    print("no website business")

                                # email
                                email = ""

                                if soup_contact.find("a", {'class': 'email-business'}) is not None:
                                    email += str(
                                        soup_contact.find("a", {'class': 'email-business'})
                                            .get("href")
                                            .lower()
                                            .replace('mailto:', '')
                                    )
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
                                    password=password,
                                    db='contacts_professionnels',
                                    charset='utf8mb4',
                                    cursorclass=pymysql.cursors.DictCursor
                                )

                                with connection.cursor() as cursor:
                                    try:
                                        sql = "INSERT INTO contacts_for_b2b_contact_data_for_datarade " \
                                              "(company_name, postal_address, phone_number, " \
                                              "website, email, region, " \
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
                                            "The record is stored : " + str(i_1) + " contact_b2b : " + str(contact_b2b))

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
