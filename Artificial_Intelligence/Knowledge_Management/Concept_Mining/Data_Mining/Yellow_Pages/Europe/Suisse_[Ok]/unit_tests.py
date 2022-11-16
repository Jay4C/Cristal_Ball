import unittest
from bs4 import BeautifulSoup
import requests
import time
import pymysql.cursors
from requests_tor import RequestsTor
import xlsxwriter

password = 'azerAZER123098,,,'


class UnitTestsDataMinerYellowPagesSuisseWithClearWeb(unittest.TestCase):
    def test_web_scraper_email_suisse_1(self):
        connection = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            password='',
            db='contacts_professionnels',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )

        """
        
        """

        activites = [
            # {'id': '1', 'url': 'https://tel.local.ch/en/q/?what=Temporary+and+permanent+employment&where='},
            # {'id': '2', 'url': 'https://tel.local.ch/en/q/?what=real+estate&where='},
            # {'id': '3', 'url': 'https://tel.local.ch/en/q/?what=recruiters&where='},
            # {'id': '4', 'url': 'https://tel.local.ch/en/q/?what=software&where='},
            # {'id': '5', 'url': 'https://tel.local.ch/en/q/?what=hotel&where='},
            # {'id': '6', 'url': 'https://tel.local.ch/en/q/?what=landlord&where='},
            # {'id': '7', 'url': 'https://tel.local.ch/en/q/?what=Cleaning+company&where='},
            # {'id': '8', 'url': 'https://tel.local.ch/en/q/?what=Charitable&where='},
            # {'id': '9', 'url': 'https://tel.local.ch/en/q/?what=Financial+services&where='},
            # {'id': '10', 'url': 'https://tel.local.ch/en/q/?what=Restaurant&where='},
            # {'id': '11', 'url': 'https://tel.local.ch/en/q/?what=building&where='},
            # {'id': '12', 'url': 'https://tel.local.ch/en/q/?what=Hairdresser&where='},
            # {'id': '13', 'url': 'https://tel.local.ch/en/q/?what=Florist&where='},
            # {'id': '14', 'url': 'https://tel.local.ch/en/q/?what=Locksmith&where='},
            # {'id': '15', 'url': 'https://tel.local.ch/en/q/?what=bakery&where='},
            # {'id': '16', 'url': 'https://tel.local.ch/en/q/?what=Insurance&where='},
            # {'id': '17', 'url': 'https://tel.local.ch/en/q/?what=Pharmacy&where='},
            # {'id': '18', 'url': 'https://tel.local.ch/en/q/?what=Movers&where='},
            # {'id': '19', 'url': 'https://tel.local.ch/en/q/?what=Electricity&where='},
            # {'id': '20', 'url': 'https://tel.local.ch/en/q/?what=Construction+plumbers&where='},
            # {'id': '21', 'url': 'https://tel.local.ch/en/q/?what=Security+services&where='},
            # {'id': '22', 'url': 'https://tel.local.ch/en/q/?what=attorney&where='},
            # {'id': '23', 'url': 'https://tel.local.ch/en/q/?what=bank&where='},
            # {'id': '24', 'url': 'https://tel.local.ch/en/q/?what=mechanic&where='},
            # {'id': '25', 'url': 'https://tel.local.ch/en/q/?what=Dentist&where='},
            # {'id': '26', 'url': 'https://tel.local.ch/en/q/?what=doctors&where='},
            # {'id': '27', 'url': 'https://tel.local.ch/en/q/?what=Accounting&where='},
            # {'id': '28', 'url': 'https://tel.local.ch/en/q/?what=Grocery+store&where='},
            # {'id': '29', 'url': 'https://tel.local.ch/en/q/?what=notary&where='},
            # {'id': '30', 'url': 'https://tel.local.ch/en/q/?what=Jewellery&where='},
            # {'id': '31', 'url': 'https://tel.local.ch/en/q/?what=Tailors&where='},
            # {'id': '32', 'url': 'https://tel.local.ch/en/q/?what=butcher&where='},
            # {'id': '33', 'url': 'https://tel.local.ch/en/q/?what=Library&where='},
            # {'id': '34', 'url': 'https://tel.local.ch/en/q/?what=architect&where='},
            {'id': '36', 'url': 'https://tel.local.ch/en/q?what=cement&where='}, # cement
            {'id': '37', 'url': 'https://tel.local.ch/en/q?what=heating&where='}, # heating
            {'id': '38', 'url': 'https://tel.local.ch/en/q?what=naval&where='}, # naval
            {'id': '39', 'url': 'https://tel.local.ch/en/q?what=cold&where='}, # cold
            {'id': '41', 'url': 'https://tel.local.ch/en/q?what=steel&where='}, # steel
            {'id': '42', 'url': 'https://tel.local.ch/en/q?what=chemicals&where='}, # chemicals
            {'id': '43', 'url': 'https://tel.local.ch/en/q?what=gas&where='}, # gas
            {'id': '44', 'url': 'https://tel.local.ch/en/q?what=goldsmith&where='} # gold
        ]

        capitales = [
            {'id': '1', 'nom': 'berne', 'pays': 'suisse'},
            {'id': '2', 'nom': 'altdorf', 'pays': 'suisse'},
            {'id': '3', 'nom': 'schwytz', 'pays': 'suisse'},
            {'id': '4', 'nom': 'sarnen', 'pays': 'suisse'},
            {'id': '5', 'nom': 'stans', 'pays': 'suisse'},
            {'id': '6', 'nom': 'glaris', 'pays': 'suisse'},
            {'id': '7', 'nom': 'zoug', 'pays': 'suisse'},
            {'id': '8', 'nom': 'fribourg', 'pays': 'suisse'},
            {'id': '9', 'nom': 'soleure', 'pays': 'suisse'},
            {'id': '10', 'nom': 'bale', 'pays': 'suisse'},
            {'id': '11', 'nom': 'liestal', 'pays': 'suisse'},
            {'id': '12', 'nom': 'schaffhouse', 'pays': 'suisse'},
            {'id': '13', 'nom': 'herisau', 'pays': 'suisse'},
            {'id': '14', 'nom': 'appenzell', 'pays': 'suisse'},
            {'id': '15', 'nom': 'saint-gall', 'pays': 'suisse'},
            {'id': '16', 'nom': 'coire', 'pays': 'suisse'},
            {'id': '17', 'nom': 'aarau', 'pays': 'suisse'},
            {'id': '18', 'nom': 'frauenfeld', 'pays': 'suisse'},
            {'id': '19', 'nom': 'bellinzone', 'pays': 'suisse'},
            {'id': '20', 'nom': 'lausanne', 'pays': 'suisse'},
            {'id': '21', 'nom': 'sion', 'pays': 'suisse'},
            {'id': '22', 'nom': 'neuchatel', 'pays': 'suisse'},
            {'id': '23', 'nom': 'geneve', 'pays': 'suisse'},
            {'id': '24', 'nom': 'delemont', 'pays': 'suisse'},
        ]

        try:
            for activite in activites:
                for capitale in capitales:
                    i = 1

                    var = 1

                    while var == 1:
                        url = activite.get('url') + str(capitale.get('nom')) + "+(Canton)&page=" + str(i)
                        
                        print(url)

                        # Request the content of a page from the url of contacts
                        html = requests.get(url)

                        time.sleep(5)

                        # Parse the content of html
                        soup = BeautifulSoup(html.content, 'html.parser')

                        if soup.find("a", {"title": "E-Mail"}) is None:
                            print(soup.find('h2', {'class': 'lui-margin-vertical-zero'}).text)
                            break

                        else:
                            for a in soup.find_all("a", {"title": "E-Mail"}):
                                email_business = a.get('href')[7:]

                                email = "info@" + str(email_business.split("@")[1])

                                with connection.cursor() as cursor:
                                    try:
                                        sql = "INSERT INTO `emails` (`id_activite`, `id_capitale_du_monde`, `email`) " \
                                              "VALUE (%s, %s, %s)"
                                        cursor.execute(sql, (activite.get('id'), capitale.get('id'), email))
                                        connection.commit()
                                        print("The record is stored : " + str(email))

                                    except Exception as e:
                                        print("The record already exists : " + str(email) + " " + str(e))

                        i += 1
        finally:
            connection.close()
            print("finally ok")

    def test_sorry(self):
        url = "https://tel.local.ch/en/q/?what=Restaurant&where=Zurich+(Canton)&page=423"
        #url = "https://tel.local.ch/en/q/?what=Restaurant&where=Zurich+(Canton)&page=42"

        # Request the content of a page from the url of contacts
        html = requests.get(url)

        # Parse the content of html
        soup = BeautifulSoup(html.content, 'html.parser')

        if soup.find("a", {"title": "E-Mail"}) is None:
            print(soup.find('h2', {'class': 'lui-margin-vertical-zero'}).text[:6])
        else:
            print('good')

    def test_web_scraper_email_suisse_2(self):
        print("test_web_scraper_email_suisse_2")

        connection = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            password='',
            db='contacts_professionnels',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )

        activites = [
            # {'id': '1', 'url': 'https://tel.local.ch/en/q/?what=Temporary+and+permanent+employment&where='},
            # {'id': '2', 'url': 'https://tel.local.ch/en/q/?what=real+estate&where='},
            # {'id': '3', 'url': 'https://tel.local.ch/en/q/?what=recruiters&where='},
            # {'id': '4', 'url': 'https://tel.local.ch/en/q/?what=software&where='},
            # {'id': '5', 'url': 'https://tel.local.ch/en/q/?what=hotel&where='},
            # {'id': '6', 'url': 'https://tel.local.ch/en/q/?what=landlord&where='},
            # {'id': '7', 'url': 'https://tel.local.ch/en/q/?what=Cleaning+company&where='},
            # {'id': '8', 'url': 'https://tel.local.ch/en/q/?what=Charitable&where='},
            # {'id': '9', 'url': 'https://tel.local.ch/en/q/?what=Financial+services&where='},
            # {'id': '10', 'url': 'https://tel.local.ch/en/q/?what=Restaurant&where='},
            # {'id': '11', 'url': 'https://tel.local.ch/en/q/?what=building&where='},
            # {'id': '12', 'url': 'https://tel.local.ch/en/q/?what=Hairdresser&where='},
            # {'id': '13', 'url': 'https://tel.local.ch/en/q/?what=Florist&where='},
            # {'id': '14', 'url': 'https://tel.local.ch/en/q/?what=Locksmith&where='},
            # {'id': '15', 'url': 'https://tel.local.ch/en/q/?what=bakery&where='},
            # {'id': '16', 'url': 'https://tel.local.ch/en/q/?what=Insurance&where='},
            # {'id': '17', 'url': 'https://tel.local.ch/en/q/?what=Pharmacy&where='},
            # {'id': '18', 'url': 'https://tel.local.ch/en/q/?what=Movers&where='},
            # {'id': '19', 'url': 'https://tel.local.ch/en/q/?what=Electricity&where='},
            # {'id': '20', 'url': 'https://tel.local.ch/en/q/?what=Construction+plumbers&where='},
            # {'id': '21', 'url': 'https://tel.local.ch/en/q/?what=Security+services&where='},
            # {'id': '22', 'url': 'https://tel.local.ch/en/q/?what=attorney&where='},
            # {'id': '23', 'url': 'https://tel.local.ch/en/q/?what=bank&where='},
            # {'id': '24', 'url': 'https://tel.local.ch/en/q/?what=mechanic&where='},
            # {'id': '25', 'url': 'https://tel.local.ch/en/q/?what=Dentist&where='},
            # {'id': '26', 'url': 'https://tel.local.ch/en/q/?what=doctors&where='},
            # {'id': '27', 'url': 'https://tel.local.ch/en/q/?what=Accounting&where='},
            # {'id': '28', 'url': 'https://tel.local.ch/en/q/?what=Grocery+store&where='},
            # {'id': '29', 'url': 'https://tel.local.ch/en/q/?what=notary&where='},
            # {'id': '30', 'url': 'https://tel.local.ch/en/q/?what=Jewellery&where='},
            # {'id': '31', 'url': 'https://tel.local.ch/en/q/?what=Tailors&where='},
            # {'id': '32', 'url': 'https://tel.local.ch/en/q/?what=butcher&where='},
            # {'id': '33', 'url': 'https://tel.local.ch/en/q/?what=Library&where='},
            # {'id': '34', 'url': 'https://tel.local.ch/en/q/?what=architect&where='},
            {'id': '36', 'url': 'https://tel.local.ch/en/q?what=cement&where='}, # cement
            {'id': '37', 'url': 'https://tel.local.ch/en/q?what=heating&where='}, # heating
            {'id': '38', 'url': 'https://tel.local.ch/en/q?what=naval&where='}, # naval
            {'id': '39', 'url': 'https://tel.local.ch/en/q?what=cold&where='}, # cold
            {'id': '41', 'url': 'https://tel.local.ch/en/q?what=steel&where='}, # steel
            {'id': '42', 'url': 'https://tel.local.ch/en/q?what=chemicals&where='}, # chemicals
            {'id': '43', 'url': 'https://tel.local.ch/en/q?what=gas&where='}, # gas
            {'id': '44', 'url': 'https://tel.local.ch/en/q?what=goldsmith&where='} # gold
        ]

        capitales = [
            {'id': '8', 'nom': 'Zurich'},
            {'id': '10', 'nom': 'Bern'},
            {'id': '11', 'nom': 'Lucerne'},
            {'id': '12', 'nom': 'Uri'},
            {'id': '13', 'nom': 'Schwytz'},
            {'id': '14', 'nom': 'Obwald'},
            {'id': '15', 'nom': 'Nidwald'},
            {'id': '16', 'nom': 'Glaris'},
            {'id': '17', 'nom': 'Zoug'},
            {'id': '18', 'nom': 'Fribourg'},
            {'id': '19', 'nom': 'Soleure'},
            {'id': '20', 'nom': 'Bâle-Ville'},
            {'id': '21', 'nom': 'Bâle-Campagne'},
            {'id': '22', 'nom': 'Schaffhouse'},
            {'id': '23', 'nom': 'Appenzell+Outer+Rhodes'},
            {'id': '24', 'nom': 'Appenzell+Inner+Rhodes'},
            {'id': '25', 'nom': 'Saint-Gall'},
            {'id': '26', 'nom': 'Grisons'},
            {'id': '27', 'nom': 'Argovie'},
            {'id': '28', 'nom': 'Thurgovie'},
            {'id': '29', 'nom': 'Tessin'},
            {'id': '30', 'nom': 'Vaud'},
            {'id': '31', 'nom': 'Valais'},
            {'id': '32', 'nom': 'Neuchâtel'},
            {'id': '33', 'nom': 'Genève'},
            {'id': '34', 'nom': 'Jura'}
        ]

        try:
            for activite in activites:
                for capitale in capitales:

                    i = 1

                    var = 1

                    while var == 1:
                        url = activite.get('url') + str(capitale.get('nom')) + "+(Canton)&page=" + str(i)

                        print(url)

                        # Request the content of a page from the url of contacts
                        html = requests.get(url)

                        time.sleep(3)

                        # Parse the content of html
                        soup = BeautifulSoup(html.content, 'html.parser')

                        if soup.find("a", {"title": "E-Mail"}) is None:
                            print(soup.find('h2', {'class': 'lui-margin-vertical-zero'}).text)
                            break

                        else:
                            i_1 = 1

                            for a in soup.find_all("a", {"title": "E-Mail"}):
                                email_business = a.get('href')[7:]

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
                                    "finance@"
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

                                email = ""

                                for suffix in suffixes:
                                    email = str(suffix + str(email_business.split("@")[1]))

                                    with connection.cursor() as cursor:
                                        try:
                                            sql = "INSERT INTO `emails` (`id_activite`, `id_capitale_du_monde`, `email`) " \
                                                  "VALUE (%s, %s, %s)"

                                            cursor.execute(sql, (activite.get('id'), capitale.get('id'), email))

                                            connection.commit()

                                            print(str(i_1) + " The record is stored : " + str(email))
                                        except Exception as e:
                                            print(str(i_1) + " The record already exists : " + str(email) + " - " + str(e))

                                i_1 += 1

                        i += 1
        finally:
            connection.close()
            print("finally ok")


class UnitTestsDataMinerYellowPagesSuisseWithDarkWeb(unittest.TestCase):
    # table : contacts_for_b2b_contact_data_for_datarade

    # region : myself
    # activity : myself
    # country : myself

    # company_name : ok
    def test_extract_company_name_from_one_result_with_dark_web(self):
        print("test_extract_company_name_from_one_result_with_dark_web")

        url = "https://www.local.ch/en/d/geneve/1201/oriental-cuisine/chez-sami-GjNYsR8iF4sjkMJxH_1Kfw"

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        rt = RequestsTor()

        html_with_tor = rt.get(url, headers=headers)

        # Parse the content of html_doc
        soup = BeautifulSoup(html_with_tor.content, 'html.parser')

        # company_name
        company_name = ""

        if soup.find('span', {'itemprop': 'name'}) is not None:
            company_name += str(soup.find('span', {'itemprop': 'name'}).text.lower())

            print("company_name : " + company_name)
        else:
            print("no company_name business")

    # postal_address : ok
    def test_extract_postal_address_from_one_result_with_dark_web(self):
        print("test_extract_postal_address_from_one_result_with_dark_web")

        url = "https://www.local.ch/en/d/geneve/1201/oriental-cuisine/chez-sami-GjNYsR8iF4sjkMJxH_1Kfw"

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        rt = RequestsTor()

        html_with_tor = rt.get(url, headers=headers)

        # Parse the content of html_doc
        soup = BeautifulSoup(html_with_tor.content, 'html.parser')

        # postal_address
        postal_address = ""

        if soup.find('div', {'class': 'address-container lui-margin-bottom-s'}) is not None:
            postal_address += str(soup.find('div', {'class': 'address-container lui-margin-bottom-s'})
                                  .text
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
    def test_extract_phone_number_from_one_result_with_dark_web(self):
        print("test_extract_phone_number_from_one_result_with_dark_web")

        url = "https://www.local.ch/en/d/geneve/1201/oriental-cuisine/chez-sami-GjNYsR8iF4sjkMJxH_1Kfw"

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        rt = RequestsTor()

        html_with_tor = rt.get(url, headers=headers)

        # Parse the content of html_doc
        soup = BeautifulSoup(html_with_tor.content, 'html.parser')

        # phone_number
        phone_number = ""

        if soup.find('a', {'data-kpi-type': 'call'}) is not None:
            phone_number += str(
                soup.find('a', {'data-kpi-type': 'call'}).get('href')
                    .lower()
                    .replace("\n", " / ")
                    .replace("\t", " / ")
                    .replace("tel:", "")
            )

            print("phone_number : " + phone_number)
        else:
            print("no phone_number business")

    # website : ok
    def test_extract_website_from_one_result_with_dark_web(self):
        print("test_extract_website_from_one_result_with_dark_web")

        url = "https://www.local.ch/en/d/geneve/1201/oriental-cuisine/chez-sami-GjNYsR8iF4sjkMJxH_1Kfw"

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        rt = RequestsTor()

        html_with_tor = rt.get(url, headers=headers)

        # Parse the content of html_doc
        soup = BeautifulSoup(html_with_tor.content, 'html.parser')

        # website
        website = ""

        if soup.find('a', {'data-kpi-type': 'url'}) is not None:
            website += soup.find('a', {'data-kpi-type': 'url'}).get("href")

            print("website : " + website)
        else:
            print("no website business")

    # email : ok
    def test_extract_email_from_one_result_with_dark_web(self):
        print("test_extract_email_from_one_result_with_dark_web")

        url = "https://www.local.ch/en/d/geneve/1201/oriental-cuisine/chez-sami-GjNYsR8iF4sjkMJxH_1Kfw"

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        rt = RequestsTor()

        html_with_tor = rt.get(url, headers=headers)

        # Parse the content of html_doc
        soup = BeautifulSoup(html_with_tor.content, 'html.parser')

        # email
        email = ""

        if soup.find('a', {'data-kpi-type': 'url'}) is not None:
            email += "info@" + soup.find('a', {'data-kpi-type': 'url'}).get("href") \
                .replace('https://www.', '') \
                .replace('http://www.', '') \
                .replace('www.', '') \
                .replace('https://', '') \
                .replace('http://', '') \
                .split('/')[0]

            print("email : " + email)
        else:
            print("no email business")

    # ok
    def test_extract_each_contact_from_one_page_of_results_for_one_activity_and_one_capital_into_mysql(self):
        print("test_extract_each_contact_from_one_page_of_results_for_one_activity_and_one_capital_into_mysql")

        activity = "hotel"

        city = "berne"

        country = "suisse"

        url = "https://www.local.ch/en/q/" + city + "/" + activity + "?page=1"

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        rt = RequestsTor()

        html_with_tor = rt.get(url, headers=headers)

        # Parse the content of html_doc
        soup = BeautifulSoup(html_with_tor.content, 'html.parser')

        if soup.find("a", {'class': 'card-info clearfix js-gtm-event'}) is not None:
            all_a = soup.find_all("a", {'class': 'card-info clearfix js-gtm-event'})

            for a in all_a:
                url_a = a.get('href')

                time.sleep(2)

                rt = RequestsTor()

                html_a = rt.get(url_a, headers=headers)

                # Parse the content of html_doc
                soup_a = BeautifulSoup(html_a.content, 'html.parser')

                # company_name
                company_name = ""

                if soup_a.find('span', {'itemprop': 'name'}) is not None:
                    company_name += str(soup_a.find('span', {'itemprop': 'name'}).text.lower())
                else:
                    print("no company_name business")

                # postal_address
                postal_address = ""

                if soup_a.find('div', {'class': 'address-container lui-margin-bottom-s'}) is not None:
                    postal_address += str(soup_a.find('div', {'class': 'address-container lui-margin-bottom-s'})
                                          .text
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

                if soup_a.find('a', {'data-kpi-type': 'call'}) is not None:
                    phone_number += str(
                        soup_a.find('a', {'data-kpi-type': 'call'}).get('href').lower().replace("\n", " / ")
                            .replace("\t", " / ")
                            .replace("tel:", "")
                    )
                else:
                    print("no phone_number business")

                # website
                website = ""

                if soup_a.find('a', {'data-kpi-type': 'url'}) is not None:
                    website += soup_a.find('a', {'data-kpi-type': 'url'}).get("href")
                else:
                    print("no website business")

                # email
                email = ""

                if soup_a.find('a', {'data-kpi-type': 'url'}) is not None:
                    email += "info@" + soup_a.find('a', {'data-kpi-type': 'url'}).get("href") \
                        .replace('https://www.', '') \
                        .replace('http://www.', '') \
                        .replace('www.', '') \
                        .replace('https://', '') \
                        .replace('http://', '') \
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
                    password=password,
                    db='contacts_professionnels',
                    charset='utf8mb4',
                    cursorclass=pymysql.cursors.DictCursor
                )

                with connection.cursor() as cursor:
                    try:
                        sql = "INSERT INTO contacts_for_b2b_contact_data_for_datarade " \
                              "(company_name, " \
                              "postal_address, " \
                              "phone_number, " \
                              "website, " \
                              "email, " \
                              "region, " \
                              "activity, " \
                              "country) " \
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

                        print("The record is stored : "
                              "contacts_for_b2b_contact_data_for_datarade : " + str(contact_b2b)
                              )

                        connection.close()
                    except Exception as e:
                        print("The record already exists : " + str(e))
                        connection.close()
        else:
            print("no a class card-info clearfix js-gtm-event")

    # ok
    def test_extract_each_contact_from_all_pages_of_results_for_one_activity_and_one_capital_into_mysql(self):
        print("test_extract_each_contact_from_all_pages_of_results_for_one_activity_and_one_capital_into_mysql")

        activity = "hotel"

        city = "berne"

        country = "suisse"

        url = "https://www.local.ch/en/q/" + city + "/" + activity + "?page=1"

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        rt = RequestsTor()

        html_with_tor = rt.get(url, headers=headers)

        # Parse the content of html_doc
        soup = BeautifulSoup(html_with_tor.content, 'html.parser')

        number_of_pages = 0

        if soup.find("h1", {"class": "search-header-results-title lui-margin-top-zero lui-margin-bottom-s"}) is not None:
            number_of_pages_with_coma = int(soup.find("h1", {"class": "search-header-results-title lui-margin-top-zero lui-margin-bottom-s"})
                                            .text
                                            .replace(" results for " + activity + " in " + city, "")
                                            ) / 10

            if int(str(number_of_pages_with_coma).split(".")[1][:1]) < 5:
                number_of_pages += round(number_of_pages_with_coma) + 1
                print('number_of_pages : ' + str(number_of_pages))
            elif int(str(number_of_pages_with_coma).split(".")[1][:1]) >= 5:
                number_of_pages += round(number_of_pages_with_coma)
                print('number_of_pages : ' + str(number_of_pages))
        else:
            print("error pages")

        i_1 = 0

        for i in range(1, number_of_pages + 1):
            url = "https://www.local.ch/en/q/" + city + "/" + activity + "?page=" + str(i)

            headers = {
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
                              '(KHTML, like Gecko) Chrome/51.0.2704.103'
            }

            rt = RequestsTor()

            html_with_tor = rt.get(url, headers=headers)

            # Parse the content of html_doc
            soup = BeautifulSoup(html_with_tor.content, 'html.parser')

            if soup.find("a", {'class': 'card-info clearfix js-gtm-event'}) is not None:
                all_a = soup.find_all("a", {'class': 'card-info clearfix js-gtm-event'})

                for a in all_a:
                    url_a = a.get('href')

                    time.sleep(2)

                    rt = RequestsTor()

                    html_a = rt.get(url_a, headers=headers)

                    # Parse the content of html_doc
                    soup_a = BeautifulSoup(html_a.content, 'html.parser')

                    # company_name
                    company_name = ""

                    if soup_a.find('span', {'itemprop': 'name'}) is not None:
                        company_name += str(soup_a.find('span', {'itemprop': 'name'}).text.lower())
                    else:
                        print("no company_name business")

                    # postal_address
                    postal_address = ""

                    if soup_a.find('div', {'class': 'address-container lui-margin-bottom-s'}) is not None:
                        postal_address += str(soup_a.find('div', {'class': 'address-container lui-margin-bottom-s'})
                                              .text
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

                    if soup_a.find('a', {'data-kpi-type': 'call'}) is not None:
                        phone_number += str(
                            soup_a.find('a', {'data-kpi-type': 'call'}).get('href').lower().replace("\n", " / ")
                                .replace("\t", " / ")
                                .replace("tel:", "")
                        )
                    else:
                        print("no phone_number business")

                    # website
                    website = ""

                    if soup_a.find('a', {'data-kpi-type': 'url'}) is not None:
                        website += soup_a.find('a', {'data-kpi-type': 'url'}).get("href")
                    else:
                        print("no website business")

                    # email
                    email = ""

                    if soup_a.find('a', {'data-kpi-type': 'url'}) is not None:
                        email += "info@" + soup_a.find('a', {'data-kpi-type': 'url'}).get("href") \
                            .replace('https://www.', '') \
                            .replace('http://www.', '') \
                            .replace('www.', '') \
                            .replace('https://', '') \
                            .replace('http://', '') \
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
                        password=password,
                        db='contacts_professionnels',
                        charset='utf8mb4',
                        cursorclass=pymysql.cursors.DictCursor
                    )

                    with connection.cursor() as cursor:
                        try:
                            sql = "INSERT INTO contacts_for_b2b_contact_data_for_datarade " \
                                  "(company_name, " \
                                  "postal_address, " \
                                  "phone_number, " \
                                  "website, " \
                                  "email, " \
                                  "region, " \
                                  "activity, " \
                                  "country) " \
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
                                str(i_1) +
                                " _ The record is stored : "
                                "contacts_for_b2b_contact_data_for_datarade : "
                                + str(contact_b2b)
                                )

                            connection.close()

                            i_1 += 1
                        except Exception as e:
                            print("The record already exists : " + str(e))
                            connection.close()
            else:
                print("no a class card-info clearfix js-gtm-event")

    # ok
    def test_extract_each_contact_from_all_pages_of_results_for_all_activities_and_all_capitals_into_mysql(self):
        print("test_extract_each_contact_from_all_pages_of_results_for_all_activities_and_all_capitals_into_mysql")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        activites = [
            {'id': '1', 'url': 'employment', 'start': 1},  # Temporary employment agencies
            {'id': '2', 'url': 'real-estate', 'start': 1},  # Real estate
            {'id': '3', 'url': 'recruitment', 'start': 1},  # Recruiter
            {'id': '4', 'url': 'software', 'start': 1},  # software
            {'id': '5', 'url': 'hotel', 'start': 1},  # hotel
            {'id': '6', 'url': 'social', 'start': 1},  # social landlord
            {'id': '7', 'url': 'cleaning', 'start': 1},  # cleaning
            {'id': '8', 'url': 'charity', 'start': 1},  # charity
            {'id': '9', 'url': 'financial', 'start': 1},  # financial
            {'id': '10', 'url': 'restaurant', 'start': 1},  # restaurant
            {'id': '11', 'url': 'building', 'start': 1},  # building
            {'id': '12', 'url': 'hairdresser', 'start': 1},  # hairdresser
            {'id': '13', 'url': 'florist', 'start': 1},  # florist
            {'id': '14', 'url': 'locksmith', 'start': 1},  # locksmith
            {'id': '15', 'url': 'bakery', 'start': 1},  # bakery
            {'id': '16', 'url': 'insurance', 'start': 1},  # insurance
            {'id': '17', 'url': 'pharmacy', 'start': 1},  # pharmacy
            {'id': '18', 'url': 'mover', 'start': 1},  # mover
            {'id': '19', 'url': 'electricity', 'start': 1},  # electricity
            {'id': '20', 'url': 'plumbing', 'start': 1},  # plumbing
            {'id': '21', 'url': 'security', 'start': 1},  # security
            {'id': '22', 'url': 'attorney', 'start': 1},  # attorney
            {'id': '23', 'url': 'bank', 'start': 1},  # bank
            {'id': '24', 'url': 'garage', 'start': 1},  # garage
            {'id': '25', 'url': 'dentist', 'start': 1},  # dentist
            {'id': '26', 'url': 'doctor', 'start': 1},  # doctor
            {'id': '27', 'url': 'accountant', 'start': 1},  # accountant
            {'id': '28', 'url': 'grocery', 'start': 1},  # grocery stores
            {'id': '29', 'url': 'notary', 'start': 1},  # notary
            {'id': '30', 'url': 'jewellery', 'start': 1},  # jewellery
            {'id': '31', 'url': 'tailor', 'start': 1},  # tailor
            {'id': '32', 'url': 'butcher', 'start': 1},  # butcher
            {'id': '33', 'url': 'library', 'start': 1},  # library
            {'id': '34', 'url': 'architect', 'start': 1},  # architect
            {'id': '36', 'url': 'cement', 'start': 1},  # cement
            {'id': '37', 'url': 'heating', 'start': 1},  # heating
            {'id': '38', 'url': 'boat', 'start': 1},  # boat
            {'id': '39', 'url': 'cold', 'start': 1},  # cold
            {'id': '41', 'url': 'steel', 'start': 1},  # steel
            {'id': '42', 'url': 'chemical', 'start': 1},  # chemical
            {'id': '43', 'url': 'gas', 'start': 1},  # gas
            {'id': '44', 'url': 'gold', 'start': 1},  # gold
            {'id': '45', 'url': 'energy', 'start': 1},  # energy
            {'id': '46', 'appellation': 'commune', 'start': 1}, # commune
        ]

        capitales_du_monde = [
            {'id': '1', 'nom': 'berne', 'pays': 'suisse'},
            {'id': '2', 'nom': 'altdorf', 'pays': 'suisse'},
            {'id': '3', 'nom': 'schwytz', 'pays': 'suisse'},
            {'id': '4', 'nom': 'sarnen', 'pays': 'suisse'},
            {'id': '5', 'nom': 'stans', 'pays': 'suisse'},
            {'id': '6', 'nom': 'glaris', 'pays': 'suisse'},
            {'id': '7', 'nom': 'zoug', 'pays': 'suisse'},
            {'id': '8', 'nom': 'fribourg', 'pays': 'suisse'},
            {'id': '9', 'nom': 'soleure', 'pays': 'suisse'},
            {'id': '10', 'nom': 'bale', 'pays': 'suisse'},
            {'id': '11', 'nom': 'liestal', 'pays': 'suisse'},
            {'id': '12', 'nom': 'schaffhouse', 'pays': 'suisse'},
            {'id': '13', 'nom': 'herisau', 'pays': 'suisse'},
            {'id': '14', 'nom': 'appenzell', 'pays': 'suisse'},
            {'id': '15', 'nom': 'saint-gall', 'pays': 'suisse'},
            {'id': '16', 'nom': 'coire', 'pays': 'suisse'},
            {'id': '17', 'nom': 'aarau', 'pays': 'suisse'},
            {'id': '18', 'nom': 'frauenfeld', 'pays': 'suisse'},
            {'id': '19', 'nom': 'bellinzone', 'pays': 'suisse'},
            {'id': '20', 'nom': 'lausanne', 'pays': 'suisse'},
            {'id': '21', 'nom': 'sion', 'pays': 'suisse'},
            {'id': '22', 'nom': 'neuchatel', 'pays': 'suisse'},
            {'id': '23', 'nom': 'geneve', 'pays': 'suisse'},
            {'id': '24', 'nom': 'delemont', 'pays': 'suisse'},
        ]

        try:
            for capitale in capitales_du_monde:
                for activite in activites:
                    start = activite.get('start')

                    activity = activite.get('url')

                    city = capitale.get('nom')

                    country = capitale.get('pays')

                    url = "https://www.local.ch/en/q/" + city + "/" + activity + "?page=1"

                    rt = RequestsTor()

                    html_with_tor = rt.get(url, headers=headers)

                    # Parse the content of html_doc
                    soup = BeautifulSoup(html_with_tor.content, 'html.parser')

                    number_of_pages = 0

                    if soup.find("h1", {
                        "class": "search-header-results-title lui-margin-top-zero lui-margin-bottom-s"}) is not None:
                        number_of_pages_with_coma = int(soup.find("h1", {
                            "class": "search-header-results-title lui-margin-top-zero lui-margin-bottom-s"})
                                                        .text
                                                        .replace(" results for " + activity + " in " + city, "")
                                                        ) / 10

                        if int(str(number_of_pages_with_coma).split(".")[1][:1]) < 5:
                            number_of_pages += round(number_of_pages_with_coma) + 1
                            print('number_of_pages : ' + str(number_of_pages))
                        elif int(str(number_of_pages_with_coma).split(".")[1][:1]) >= 5:
                            number_of_pages += round(number_of_pages_with_coma)
                            print('number_of_pages : ' + str(number_of_pages))
                    else:
                        print("error pages")

                    i_1 = 0

                    for i in range(start, number_of_pages + 1):
                        url = "https://www.local.ch/en/q/" + city + "/" + activity + "?page=" + str(i)

                        headers = {
                            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
                                          '(KHTML, like Gecko) Chrome/51.0.2704.103'
                        }

                        rt = RequestsTor()

                        html_with_tor = rt.get(url, headers=headers)

                        # Parse the content of html_doc
                        soup = BeautifulSoup(html_with_tor.content, 'html.parser')

                        if soup.find("a", {'class': 'card-info clearfix js-gtm-event'}) is not None:
                            all_a = soup.find_all("a", {'class': 'card-info clearfix js-gtm-event'})

                            for a in all_a:
                                url_a = a.get('href')

                                time.sleep(2)

                                rt = RequestsTor()

                                html_a = rt.get(url_a, headers=headers)

                                # Parse the content of html_doc
                                soup_a = BeautifulSoup(html_a.content, 'html.parser')

                                # company_name
                                company_name = ""

                                if soup_a.find('span', {'itemprop': 'name'}) is not None:
                                    company_name += str(soup_a.find('span', {'itemprop': 'name'}).text.lower())
                                else:
                                    print("no company_name business")

                                # postal_address
                                postal_address = ""

                                if soup_a.find('div', {'class': 'address-container lui-margin-bottom-s'}) is not None:
                                    postal_address += str(
                                        soup_a.find('div', {'class': 'address-container lui-margin-bottom-s'})
                                        .text
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

                                if soup_a.find('a', {'data-kpi-type': 'call'}) is not None:
                                    phone_number += str(
                                        soup_a.find('a', {'data-kpi-type': 'call'})
                                            .get('href')
                                            .lower().replace("\n", " / ")
                                            .replace("\t", " / ")
                                            .replace("tel:", "")
                                    )
                                else:
                                    print("no phone_number business")

                                # website
                                website = ""

                                if soup_a.find('a', {'data-kpi-type': 'url'}) is not None:
                                    website += soup_a.find('a', {'data-kpi-type': 'url'}).get("href")
                                else:
                                    print("no website business")

                                # email
                                email = ""

                                if soup_a.find('a', {'data-kpi-type': 'url'}) is not None:
                                    email += "info@" + soup_a.find('a', {'data-kpi-type': 'url'}).get("href") \
                                        .replace('https://www.', '') \
                                        .replace('http://www.', '') \
                                        .replace('www.', '') \
                                        .replace('https://', '') \
                                        .replace('http://', '') \
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
                                    password=password,
                                    db='contacts_professionnels',
                                    charset='utf8mb4',
                                    cursorclass=pymysql.cursors.DictCursor
                                )

                                with connection.cursor() as cursor:
                                    try:
                                        sql = "INSERT INTO contacts_for_b2b_contact_data_for_datarade " \
                                              "(company_name, " \
                                              "postal_address, " \
                                              "phone_number, " \
                                              "website, " \
                                              "email, " \
                                              "region, " \
                                              "activity, " \
                                              "country) " \
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
                                            str(i_1) +
                                            " _ The record is stored : "
                                            "contacts_for_b2b_contact_data_for_datarade : "
                                            + str(contact_b2b)
                                        )

                                        connection.close()

                                        i_1 += 1
                                    except Exception as e:
                                        print("The record already exists : " + str(e))
                                        connection.close()
                        else:
                            print("no a class card-info clearfix js-gtm-event")
        except Exception as e:
            print("main error : " + str(e))

    # ok
    def test_extract_each_contact_from_all_pages_of_results_for_all_activities_and_all_capitals_from_canton_into_mysql(self):
        print("test_extract_each_contact_from_all_pages_of_results_for_all_activities_and_all_capitals_from_canton_into_mysql")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        activites = [
            {'id': '46', 'url': 'commune', 'start': 1},  # commune
        ]

        capitales_du_monde = [
            {'id': '1', 'nom': 'berne', 'pays': 'suisse'},
            {'id': '2', 'nom': 'altdorf', 'pays': 'suisse'},
            {'id': '3', 'nom': 'schwytz', 'pays': 'suisse'},
            {'id': '4', 'nom': 'sarnen', 'pays': 'suisse'},
            {'id': '5', 'nom': 'stans', 'pays': 'suisse'},
            {'id': '6', 'nom': 'glaris', 'pays': 'suisse'},
            {'id': '7', 'nom': 'zoug', 'pays': 'suisse'},
            {'id': '8', 'nom': 'fribourg', 'pays': 'suisse'},
            {'id': '9', 'nom': 'soleure', 'pays': 'suisse'},
            {'id': '10', 'nom': 'bale', 'pays': 'suisse'},
            {'id': '11', 'nom': 'liestal', 'pays': 'suisse'},
            {'id': '12', 'nom': 'schaffhouse', 'pays': 'suisse'},
            {'id': '13', 'nom': 'herisau', 'pays': 'suisse'},
            {'id': '14', 'nom': 'appenzell', 'pays': 'suisse'},
            {'id': '15', 'nom': 'saint-gall', 'pays': 'suisse'},
            {'id': '16', 'nom': 'coire', 'pays': 'suisse'},
            {'id': '17', 'nom': 'aarau', 'pays': 'suisse'},
            {'id': '18', 'nom': 'frauenfeld', 'pays': 'suisse'},
            {'id': '19', 'nom': 'bellinzone', 'pays': 'suisse'},
            {'id': '20', 'nom': 'lausanne', 'pays': 'suisse'},
            {'id': '21', 'nom': 'sion', 'pays': 'suisse'},
            {'id': '22', 'nom': 'neuchatel', 'pays': 'suisse'},
            {'id': '23', 'nom': 'geneve', 'pays': 'suisse'},
            {'id': '24', 'nom': 'delemont', 'pays': 'suisse'},
        ]

        try:
            for capitale in capitales_du_monde:
                for activite in activites:
                    start = activite.get('start')

                    activity = activite.get('url')

                    city = capitale.get('nom') + " (Canton)"

                    country = capitale.get('pays')

                    url = "https://www.local.ch/fr/q/" + city + "/" + activity + "?page=1"

                    rt = RequestsTor()

                    html_with_tor = rt.get(url, headers=headers)

                    # Parse the content of html_doc
                    soup = BeautifulSoup(html_with_tor.content, 'html.parser')

                    number_of_pages = 0

                    if soup.find("h1", {
                        "class": "search-header-results-title lui-margin-top-zero lui-margin-bottom-s"}) is not None:
                        number_of_pages_with_coma = int(soup.find("h1", {
                            "class": "search-header-results-title lui-margin-top-zero lui-margin-bottom-s"})
                                                        .text
                                                        .replace(" résultats pour " + activity + " à " + city, "")
                                                        ) / 10

                        if int(str(number_of_pages_with_coma).split(".")[1][:1]) < 5:
                            number_of_pages += round(number_of_pages_with_coma) + 1
                            print('number_of_pages : ' + str(number_of_pages))
                        elif int(str(number_of_pages_with_coma).split(".")[1][:1]) >= 5:
                            number_of_pages += round(number_of_pages_with_coma)
                            print('number_of_pages : ' + str(number_of_pages))
                    else:
                        print("error pages")

                    i_1 = 0

                    for i in range(start, number_of_pages + 1):
                        url = "https://www.local.ch/fr/q/" + city + "/" + activity + "?page=" + str(i)

                        headers = {
                            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
                                          '(KHTML, like Gecko) Chrome/51.0.2704.103'
                        }

                        rt = RequestsTor()

                        html_with_tor = rt.get(url, headers=headers)

                        # Parse the content of html_doc
                        soup = BeautifulSoup(html_with_tor.content, 'html.parser')

                        if soup.find("a", {'class': 'card-info clearfix js-gtm-event'}) is not None:
                            all_a = soup.find_all("a", {'class': 'card-info clearfix js-gtm-event'})

                            for a in all_a:
                                url_a = a.get('href')

                                time.sleep(2)

                                rt = RequestsTor()

                                html_a = rt.get(url_a, headers=headers)

                                # Parse the content of html_doc
                                soup_a = BeautifulSoup(html_a.content, 'html.parser')

                                # company_name
                                company_name = ""

                                if soup_a.find('span', {'itemprop': 'name'}) is not None:
                                    company_name += str(soup_a.find('span', {'itemprop': 'name'}).text.lower())
                                else:
                                    print("no company_name business")

                                # postal_address
                                postal_address = ""

                                if soup_a.find('div', {'class': 'address-container lui-margin-bottom-s'}) is not None:
                                    postal_address += str(
                                        soup_a.find('div', {'class': 'address-container lui-margin-bottom-s'})
                                        .text
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

                                if soup_a.find('a', {'data-kpi-type': 'call'}) is not None:
                                    phone_number += str(
                                        soup_a.find('a', {'data-kpi-type': 'call'})
                                            .get('href')
                                            .lower().replace("\n", " / ")
                                            .replace("\t", " / ")
                                            .replace("tel:", "")
                                    )
                                else:
                                    print("no phone_number business")

                                # website
                                website = ""

                                if soup_a.find('a', {'data-kpi-type': 'url'}) is not None:
                                    website += soup_a.find('a', {'data-kpi-type': 'url'}).get("href")
                                else:
                                    print("no website business")

                                # email
                                email = ""

                                if soup_a.find('a', {'data-kpi-type': 'url'}) is not None:
                                    email += "info@" + soup_a.find('a', {'data-kpi-type': 'url'}).get("href") \
                                        .replace('https://www.', '') \
                                        .replace('http://www.', '') \
                                        .replace('www.', '') \
                                        .replace('https://', '') \
                                        .replace('http://', '') \
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
                                    password=password,
                                    db='contacts_professionnels',
                                    charset='utf8mb4',
                                    cursorclass=pymysql.cursors.DictCursor
                                )

                                with connection.cursor() as cursor:
                                    try:
                                        sql = "INSERT INTO contacts_for_b2b_contact_data_for_datarade " \
                                              "(company_name, " \
                                              "postal_address, " \
                                              "phone_number, " \
                                              "website, " \
                                              "email, " \
                                              "region, " \
                                              "activity, " \
                                              "country) " \
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
                                            str(i_1) +
                                            " _ The record is stored : "
                                            "contacts_for_b2b_contact_data_for_datarade : "
                                            + str(contact_b2b)
                                        )

                                        connection.close()

                                        i_1 += 1
                                    except Exception as e:
                                        print("The record already exists : " + str(e))
                                        connection.close()
                        else:
                            print("no a class card-info clearfix js-gtm-event")
        except Exception as e:
            print("main error : " + str(e))


class UnitTestsDataMinerPointsContactsCantonaux(unittest.TestCase):
    def test_extract_contacts(self):
        print("test_extract_contacts")

        filename = "Contacts_cantons_suisse.xlsx"

        workbook = xlsxwriter.Workbook(filename)

        worksheet = workbook.add_worksheet('data')

        cell_format_yellow = workbook.add_format(
            {
                'bg_color': 'yellow',
                'border': 1,
                'align': 'justify',
                'valign': 'top'
            }
        )

        worksheet.write(0, 0, 'canton', cell_format_yellow)
        worksheet.write(0, 1, 'website', cell_format_yellow)
        worksheet.write(0, 2, 'email', cell_format_yellow)
        worksheet.write(0, 3, 'telephone', cell_format_yellow)

        cell_format_orange = workbook.add_format(
            {
                'bg_color': 'orange',
                'border': 1,
                'align': 'justify',
                'valign': 'top'
            }
        )

        url = "https://covid19.easygov.swiss/fr/casderigueur-cantons/"

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        rt = RequestsTor()

        html_with_tor = rt.get(url, headers=headers)

        soup = BeautifulSoup(html_with_tor.content, 'html.parser')

        if soup.find('tr') is not None:
            all_tr = soup.find_all("tr")

            i = 1

            for tr in all_tr:
                try:
                    canton = tr.find_all('td')[0].text
                    website = tr.find_all('td')[1].find('a').get('href')
                    courriel = "'info@" + tr.find_all('td')[2].text.split('@')[1] + "',"
                    telephone = tr.find_all('td')[3].text

                    worksheet.write(i, 0, canton, cell_format_orange)
                    worksheet.write(i, 1, website, cell_format_orange)
                    worksheet.write(i, 2, courriel, cell_format_orange)
                    worksheet.write(i, 3, telephone, cell_format_orange)

                    i += 1
                except Exception as e:
                    print("error : " + str(e))
        else:
            print("no tr")

        workbook.close()


if __name__ == '__main__':
    unittest.main()
