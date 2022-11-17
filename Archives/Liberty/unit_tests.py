import json
import unittest
import pymysql.cursors
from bs4 import BeautifulSoup
import requests


class DAO_MySQL(unittest.TestCase):
    def test_list_all_databases(sel):
        print("test_list_all_databases")

        try:
            # Connect to the database
            connection = pymysql.connect(
                host='localhost',
                port=3306,
                user='root',
                password='',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )

            with connection.cursor() as cursor:
                sql = "SHOW DATABASES"
                cursor.execute(sql)
                results = cursor.fetchall()

                for result in results:
                    print(result)

            connection.close()
        except Exception as e:
            print("Error list databases : " + str(e))

    def test_create_database(self):
        print("test_create_database")

        try:
            # Connect to the database
            connection = pymysql.connect(
                host='localhost',
                port=3306,
                user='root',
                password='',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )

            with connection.cursor() as cursor:
                sql = "CREATE DATABASE liberty"
                cursor.execute(sql)
                connection.commit()

            connection.close()
        except Exception as e:
            print("The database already exists : " + str(e))

    def test_list_all_tables(self):
        print("test_list_all_tables")

        try:
            # Connect to the database
            connection = pymysql.connect(
                host='localhost',
                port=3306,
                user='root',
                password='',
                db='liberty',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )

            with connection.cursor() as cursor:
                sql = "SHOW TABLES"
                cursor.execute(sql)
                results = cursor.fetchall()

                for result in results:
                    print(result)
        except Exception as e:
            print("Error test_list_all_tables : " + str(e))

    def test_drop_a_table(self):
        print("test_drop_a_table")

        # Connect to the database
        connection = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            password='',
            db='liberty',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )

        with connection.cursor() as cursor:
            sql = "DROP TABLE countries_with_death_penalty"
            cursor.execute(sql)
            connection.commit()

        connection.close()

    def test_create_table_countries_with_death_penalty(self):
        print("test_create_table_countries_with_death_penalty")

        # Connect to the database
        connection = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            password='',
            db='liberty',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )

        with connection.cursor() as cursor:
            sql = "CREATE TABLE `countries_with_death_penalty` (" \
                  "`id` int NOT NULL AUTO_INCREMENT," \
                  "`country` varchar(255) NOT NULL UNIQUE," \
                  "PRIMARY KEY (`id`)" \
                  ")"
            cursor.execute(sql)
            connection.commit()

        connection.close()

    # https://www.worldatlas.com/articles/countries-with-capital-punishment.html
    def test_insert_countries_with_death_penalty(self):
        print("test_insert_countries_without_death_penalty")

        url = 'https://www.worldatlas.com/articles/countries-with-capital-punishment.html'

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        html = requests.get(url, headers=headers)

        soup = BeautifulSoup(html.text, 'html.parser')

        if soup.find("table", {"data-role": "table"}) is not None:
            all_tr = soup.find("table", {"data-role": "table"}).find("tbody").find_all("tr")

            for tr in all_tr:
                country = tr.find_all("td")[1].text.lower()

                try:
                    # Connect to the database
                    connection = pymysql.connect(
                        host='localhost',
                        port=3306,
                        user='root',
                        password='',
                        db='liberty',
                        charset='utf8mb4',
                        cursorclass=pymysql.cursors.DictCursor
                    )

                    with connection.cursor() as cursor:
                        sql = "INSERT INTO `countries_with_death_penalty` (`country`) VALUES (%s)"
                        cursor.execute(sql, country)
                        connection.commit()

                        print("country : " + country + " inserted.")

                    connection.close()
                except Exception as e:
                    print("The record : " + country + " already exists : " + str(e))

    def test_select_from_countries_with_death_penalty(self):
        print('test_select_from_countries_with_death_penalty')

        connection = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            password='',
            db='liberty',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )

        try:
            with connection.cursor() as cursor:
                try:
                    sql = "SELECT * FROM `countries_with_death_penalty` ORDER BY id ASC"
                    cursor.execute(sql)
                    results = cursor.fetchall()

                    for result in results:
                        print(result.get('country'))

                except Exception as e:
                    print("There is an error : " + str(e))
        finally:
            connection.close()

    def test_create_table_countries_with_zero_income_tax(self):
        print("test_create_table_countries_with_zero_income_tax")

        # Connect to the database
        connection = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            password='',
            db='liberty',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )

        with connection.cursor() as cursor:
            sql = "CREATE TABLE `countries_with_zero_income_tax` (" \
                  "`id` int NOT NULL AUTO_INCREMENT," \
                  "`country` varchar(255) NOT NULL UNIQUE," \
                  "PRIMARY KEY (`id`)" \
                  ")"
            cursor.execute(sql)
            connection.commit()

        connection.close()

    def test_insert_countries_with_zero_income_tax(self):
        print("test_insert_countries_with_zero_income_tax")

        countries = [
            {'country': 'Brunei'},
            {'country': 'Bermuda'},
            {'country': 'Cayman Island'},
            {'country': 'British Virgin Islands'},
            {'country': 'Bahamas'},
            {'country': 'Anguilla'},
            {'country': 'Turks and Caicos'},
            {'country': 'Nevis and St Kitts'},
            {'country': 'Monaco'},
            {'country': 'United Arab Emirates'},
            {'country': 'Saudi Arabia'},
            {'country': 'Oman'},
            {'country': 'Qatar'},
            {'country': 'Bahrain'},
            {'country': 'Kuwait'}
        ]

        for country in countries:
            try:
                # Connect to the database
                connection = pymysql.connect(
                    host='localhost',
                    port=3306,
                    user='root',
                    password='',
                    db='liberty',
                    charset='utf8mb4',
                    cursorclass=pymysql.cursors.DictCursor
                )

                with connection.cursor() as cursor:
                    sql = "INSERT INTO `countries_with_zero_income_tax` (`country`) " \
                          "VALUES (%s)"
                    cursor.execute(sql, country.get('country').lower())

                    connection.commit()

                    print("country : " + country.get('country').lower() + " ok")

                connection.close()
            except Exception as e:
                print("The record : " + country.get('country').lower() + " already exists " + str(e))

    def test_select_from_countries_with_zero_income_tax(self):
        print('test_select_from_countries_with_zero_income_tax')

        connection = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            password='',
            db='liberty',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )

        try:
            with connection.cursor() as cursor:
                try:
                    sql = "SELECT * FROM `countries_with_zero_income_tax`"

                    cursor.execute(sql)

                    results = cursor.fetchall()

                    for result in results:
                        print(result.get('country'))

                except Exception as e:
                    print("There is an error : " + str(e))
        finally:
            connection.close()

    def test_create_table_countries_with_zero_corporation_tax(self):
        print("test_create_table_countries_with_zero_corporation_tax")

        connection = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            password='',
            db='liberty',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )

        with connection.cursor() as cursor:
            sql = "CREATE TABLE `countries_with_zero_corporation_tax` (" \
                  "`id` int NOT NULL AUTO_INCREMENT," \
                  "`country` varchar(300) NOT NULL UNIQUE," \
                  "PRIMARY KEY (`id`)" \
                  ")"
            cursor.execute(sql)
            connection.commit()

        connection.close()

    def test_insert_countries_with_zero_corporation_tax(self):
        print("test_insert_countries_with_zero_corporation_tax")

        countries = [
            {'country': 'Anguilla'},
            {'country': 'Bahamas'},
            {'country': 'Bahrain'},
            {'country': 'Bermuda'},
            {'country': 'Cayman Islands'},
            {'country': 'Estonia'},
            {'country': 'Georgia'},
            {'country': 'Guernsey'},
            {'country': 'Isle of Man'},
            {'country': 'Jersey'},
            {'country': 'Kuwait'},
            {'country': 'Latvia'},
            {'country': 'Saint Kitts and Nevis'},
            {'country': 'Sark'},
            {'country': 'United Arab Emirates'},
            {'country': 'British Virgin Islands'}
        ]

        for country in countries:
            try:
                connection = pymysql.connect(
                    host='localhost',
                    port=3306,
                    user='root',
                    password='',
                    db='liberty',
                    charset='utf8mb4',
                    cursorclass=pymysql.cursors.DictCursor
                )

                with connection.cursor() as cursor:
                    sql = "INSERT INTO `countries_with_zero_corporation_tax` (`country`) " \
                          "VALUES (%s)"
                    cursor.execute(sql, country.get('country').lower())

                    connection.commit()

                    print("country : " + country.get('country').lower() + " ok")

                connection.close()
            except Exception as e:
                print("The record : " + country.get('country').lower() + " already exists " + str(e))

    def test_select_from_countries_with_zero_corporation_tax(self):
        print('test_select_from_countries_with_zero_corporation_tax')

        connection = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            password='',
            db='liberty',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )

        try:
            with connection.cursor() as cursor:
                try:
                    sql = "SELECT * FROM `countries_with_zero_corporation_tax`"

                    cursor.execute(sql)

                    results = cursor.fetchall()

                    for result in results:
                        print(result.get('country'))

                except Exception as e:
                    print("There is an error : " + str(e))
        finally:
            connection.close()

    def test_create_table_countries_with_electricity_production_without_licence(self):
        print("test_create_table_countries_with_electricity_production_without_licence")

        connection = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            password='',
            db='liberty',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )

        with connection.cursor() as cursor:
            sql = "CREATE TABLE `countries_with_electricity_production_without_licence` (" \
                  "`id` int NOT NULL AUTO_INCREMENT," \
                  "`country` varchar(300) NOT NULL UNIQUE," \
                  "PRIMARY KEY (`id`)" \
                  ")"
            cursor.execute(sql)
            connection.commit()

        connection.close()

    def test_insert_countries_with_electricity_production_without_licence(self):
        print("test_insert_countries_with_electricity_production_without_licence")

        countries = [
            {'country': 'Albania'},
            {'country': 'Finland'},
            {'country': 'Montenegro'},
            {'country': 'Republic Tcheque'},
            {'country': 'Roumania'},
            {'country': 'Russia'},
            {'country': 'Switzerland'},
            {'country': 'Kosovo'},
            {'country': 'Saudi Arabia'},
            {'country': 'Armenia'},
            {'country': 'Bangladesh'},
            {'country': 'Brunei'},
            {'country': 'China'},
            {'country': 'North Korea'},
            {'country': 'South Korea'},
            {'country': 'United Arab Emirates'},
            {'country': 'Georgia'},
            {'country': 'India'},
            {'country': 'Indonesia'},
            {'country': 'Jordan'},
            {'country': 'Kazakhstan'},
            {'country': 'Laos'},
            {'country': 'Uzbekistan'},
            {'country': 'Pakistan'},
            {'country': 'Vietnam'},
            {'country': 'South Africa'},
            {'country': 'Eswatini'},
            {'country': 'Gambia'},
            {'country': 'Lesotho'},
            {'country': 'Mozambique'},
            {'country': 'Namibia'},
            {'country': 'Antigua And Barbuda'},
            {'country': 'Argentina'},
            {'country': 'Canada'},
            {'country': 'Chile'},
            {'country': 'Dominican Republic'},
            {'country': 'Dominique'},
            {'country': 'Ecuador'},
            {'country': 'Grenada'},
            {'country': 'Jamaica'},
            {'country': 'Puerto Rico'},
            {'country': 'Cayman Islands'},
            {'country': 'British Virgin Islands'},
            {'country': 'Anguilla'},
            {'country': 'Montserrat'},
            {'country': 'Nauru'},
            {'country': 'New Zealand'},
            {'country': 'Samoa'},
            {'country': 'Tonga'},
            {'country': 'Vanuatu'}
        ]

        for country in countries:
            try:
                connection = pymysql.connect(
                    host='localhost',
                    port=3306,
                    user='root',
                    password='',
                    db='liberty',
                    charset='utf8mb4',
                    cursorclass=pymysql.cursors.DictCursor
                )

                with connection.cursor() as cursor:
                    sql = "INSERT INTO `countries_with_electricity_production_without_licence` (`country`) " \
                          "VALUES (%s)"
                    cursor.execute(sql, country.get('country').lower())

                    connection.commit()

                    print("country '" + country.get('country').lower() + "' : ok")

                connection.close()
            except Exception as e:
                print("The record : " + country.get('country').lower() + " already exists " + str(e))

    def test_select_from_countries_with_electricity_production_without_licence(self):
        print('test_select_from_countries_with_electricity_production_without_licence')

        connection = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            password='',
            db='liberty',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )

        try:
            with connection.cursor() as cursor:
                try:
                    sql = "SELECT * FROM `countries_with_electricity_production_without_licence`"

                    cursor.execute(sql)

                    results = cursor.fetchall()

                    for result in results:
                        print(result.get('country'))

                except Exception as e:
                    print("There is an error : " + str(e))
        finally:
            connection.close()

    def test_create_table_countries_in_minamata_convention(self):
        print("test_create_table_countries_in_minamata_convention")

        connection = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            password='',
            db='liberty',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )

        with connection.cursor() as cursor:
            sql = "CREATE TABLE `countries_in_minamata_convention` (" \
                  "`id` int NOT NULL AUTO_INCREMENT," \
                  "`country` varchar(300) NOT NULL UNIQUE," \
                  "PRIMARY KEY (`id`)" \
                  ")"
            cursor.execute(sql)
            connection.commit()

        connection.close()

    def test_insert_countries_in_minamata_convention(self):
        print('test_insert_countries_in_minamata_convention')

        url = 'http://127.0.0.1:8000/contents/countries_ratified_minamata_convention'

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        html = requests.get(url, headers=headers)

        soup = BeautifulSoup(html.text, 'html.parser')

        if soup.find("td") is not None:
            all_td = soup.find_all("td")

            for td in all_td:
                country = td.text.lower()

                try:
                    connection = pymysql.connect(
                        host='localhost',
                        port=3306,
                        user='root',
                        password='',
                        db='liberty',
                        charset='utf8mb4',
                        cursorclass=pymysql.cursors.DictCursor
                    )

                    with connection.cursor() as cursor:
                        sql = "INSERT INTO `countries_in_minamata_convention` (`country`) VALUES (%s)"

                        cursor.execute(sql, country)

                        connection.commit()

                        print("country : " + country + " inserted")

                    connection.close()
                except Exception as e:
                    print("The record : " + country + " already exists : " + str(e))

    def test_select_from_countries_in_minamata_convention(self):
        print('test_select_from_countries_in_minamata_convention')

        connection = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            password='',
            db='liberty',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )

        try:
            with connection.cursor() as cursor:
                try:
                    sql = "SELECT * FROM `countries_in_minamata_convention`"

                    cursor.execute(sql)

                    results = cursor.fetchall()

                    for result in results:
                        print(result.get('country'))

                except Exception as e:
                    print("There is an error : " + str(e))
        finally:
            connection.close()

    def test_create_table_countries_without_vat(self):
        print("test_create_table_countries_without_vat")

        connection = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            password='',
            db='liberty',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )

        with connection.cursor() as cursor:
            sql = "CREATE TABLE `countries_without_vat` (" \
                  "`id` int NOT NULL AUTO_INCREMENT," \
                  "`country` varchar(300) NOT NULL UNIQUE," \
                  "PRIMARY KEY (`id`)" \
                  ")"

            cursor.execute(sql)

            connection.commit()

        connection.close()

    def test_insert_countries_without_vat(self):
        print('test_insert_countries_without_vat')

        countries = [
            {'country': 'Afghanistan'},
            {'country': 'American Samoa'},
            {'country': 'Anguilla'},
            {'country': 'Bermuda'},
            {'country': 'China Hainan'},
            {'country': 'Cayman Islands'},
            {'country': 'Falkland Islands'},
            {'country': 'Gibraltar'},
            {'country': 'Guernsey'},
            {'country': 'Hong Kong'},
            {'country': 'Kuwait'},
            {'country': 'Macau'},
            {'country': 'Oman'},
            {'country': 'Qatar'},
            {'country': 'San Marino'},
            {'country': 'Sark'}
        ]

        for country in countries:
            try:
                connection = pymysql.connect(
                    host='localhost',
                    port=3306,
                    user='root',
                    password='',
                    db='liberty',
                    charset='utf8mb4',
                    cursorclass=pymysql.cursors.DictCursor
                )

                with connection.cursor() as cursor:
                    sql = "INSERT INTO `countries_without_vat` (`country`) VALUES (%s)"
                    cursor.execute(sql, country.get('country').lower())

                    connection.commit()

                    print("country '" + country.get('country').lower() + "' : ok")

                connection.close()
            except Exception as e:
                print("The record : " + country.get('country').lower() + " already exists " + str(e))

    def test_select_from_countries_without_vat(self):
        print('test_select_from_countries_without_vat')

        connection = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            password='',
            db='liberty',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )

        try:
            with connection.cursor() as cursor:
                try:
                    sql = "SELECT * FROM `countries_without_vat`"

                    cursor.execute(sql)

                    results = cursor.fetchall()

                    for result in results:
                        print(result.get('country'))

                except Exception as e:
                    print("There is an error : " + str(e))
        finally:
            connection.close()

    def test_create_table_countries_with_zero_social_security_tax(self):
        print("test_create_table_countries_with_zero_social_security_tax")

        connection = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            password='',
            db='liberty',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )

        with connection.cursor() as cursor:
            sql = "CREATE TABLE `countries_with_zero_social_security_tax` (" \
                  "`id` int NOT NULL AUTO_INCREMENT," \
                  "`country` varchar(300) NOT NULL UNIQUE," \
                  "PRIMARY KEY (`id`)" \
                  ")"

            cursor.execute(sql)

            connection.commit()

        connection.close()

    def test_insert_countries_with_zero_social_security_tax(self):
        print("test_insert_countries_with_zero_social_security_tax")

        countries = [
            {'country': 'Cayman Islands'},
            {'country': 'Hong Kong'},
            {'country': 'Seychelles'}
        ]

        for country in countries:
            try:
                connection = pymysql.connect(
                    host='localhost',
                    port=3306,
                    user='root',
                    password='',
                    db='liberty',
                    charset='utf8mb4',
                    cursorclass=pymysql.cursors.DictCursor
                )

                with connection.cursor() as cursor:
                    sql = "INSERT INTO `countries_with_zero_social_security_tax` (`country`) VALUES (%s)"

                    cursor.execute(sql, country.get('country').lower())

                    connection.commit()

                    print("country '" + country.get('country').lower() + "' : ok")

                connection.close()
            except Exception as e:
                print("The record : " + country.get('country').lower() + " already exists " + str(e))

    def test_select_from_countries_with_zero_social_security_tax(self):
        print('test_select_from_countries_with_zero_social_security_tax')

        connection = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            password='',
            db='liberty',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )

        try:
            with connection.cursor() as cursor:
                try:
                    sql = "SELECT * FROM `countries_with_zero_social_security_tax`"

                    cursor.execute(sql)

                    results = cursor.fetchall()

                    for result in results:
                        print(result.get('country'))

                except Exception as e:
                    print("There is an error : " + str(e))
        finally:
            connection.close()


class DAO_Neo4j(unittest.TestCase):
    def test_insert_all_free_trade_agreements(self):
        print("test_insert_all_free_trade_agreements")

    def test_insert_all_international_conventions(self):
        print("test_insert_all_international_conventions")

    def test_insert_all_iinternational_treaties(self):
        print("test_insert_all_iinternational_treaties")

    def test_insert_all_administrative_divisions(self):
        print("test_insert_all_administrative_divisions")


class Decisions(unittest.TestCase):
    def test_go_to_these_countries(self):
        print('test_go_to_these_countries')

        connection = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            password='',
            db='liberty',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )

        # variables
        countries_with_death_penalty = []
        with connection.cursor() as cursor:
            try:
                sql = "SELECT * FROM `countries_with_death_penalty`"
                cursor.execute(sql)
                results = cursor.fetchall()

                for result in results:
                    countries_with_death_penalty.append(result.get('country'))
            except Exception as e:
                print("There is an error : " + str(e))

        countries_with_zero_income_tax = []
        with connection.cursor() as cursor:
            try:
                sql = "SELECT * FROM `countries_with_zero_income_tax`"

                cursor.execute(sql)

                results = cursor.fetchall()

                for result in results:
                    countries_with_zero_income_tax.append(result.get('country'))

            except Exception as e:
                print("There is an error : " + str(e))

        countries_with_zero_corporation_tax = []
        with connection.cursor() as cursor:
            try:
                sql = "SELECT * FROM `countries_with_zero_corporation_tax`"

                cursor.execute(sql)

                results = cursor.fetchall()

                for result in results:
                    countries_with_zero_corporation_tax.append(result.get('country'))
            except Exception as e:
                print("There is an error : " + str(e))

        countries_with_electricity_production_without_licence = []
        with connection.cursor() as cursor:
            try:
                sql = "SELECT * FROM `countries_with_electricity_production_without_licence`"

                cursor.execute(sql)

                results = cursor.fetchall()

                for result in results:
                    countries_with_electricity_production_without_licence.append(result.get('country'))
            except Exception as e:
                print("There is an error : " + str(e))

        countries_in_minamata_convention = []
        with connection.cursor() as cursor:
            try:
                sql = "SELECT * FROM `countries_in_minamata_convention`"

                cursor.execute(sql)

                results = cursor.fetchall()

                for result in results:
                    countries_in_minamata_convention.append(result.get('country'))

            except Exception as e:
                print("There is an error : " + str(e))

        countries_without_vat = []
        with connection.cursor() as cursor:
            try:
                sql = "SELECT * FROM `countries_without_vat`"

                cursor.execute(sql)

                results = cursor.fetchall()

                for result in results:
                    countries_without_vat.append(result.get('country'))

            except Exception as e:
                print("There is an error : " + str(e))

        countries_with_zero_social_security_tax = []
        with connection.cursor() as cursor:
            try:
                sql = "SELECT * FROM `countries_with_zero_social_security_tax`"

                cursor.execute(sql)

                results = cursor.fetchall()

                for result in results:
                    countries_with_zero_social_security_tax.append(result.get('country'))

            except Exception as e:
                print("There is an error : " + str(e))
        # variables

        # algorthm
        url = "https://restcountries.eu/rest/v2/all"
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)

        countries = []

        all_countries = json.loads(response.text.encode('utf8'))

        for one_country in all_countries:
            countries.append(one_country['name'].lower())

        for country in countries:
            if (country not in countries_with_death_penalty) \
                    and (country in countries_with_zero_income_tax) \
                    and (country in countries_with_zero_corporation_tax) \
                    and (country in countries_with_electricity_production_without_licence) \
                    and (country not in countries_in_minamata_convention) \
                    and (country in countries_without_vat) \
                    and (country in countries_with_zero_social_security_tax):
                print("country : " + country + " good")
        # algorthm

        connection.close()


if __name__ == '__main__':
    unittest.main()
