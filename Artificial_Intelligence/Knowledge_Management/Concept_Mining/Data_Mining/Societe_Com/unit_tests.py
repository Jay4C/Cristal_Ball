import time
import pymysql
from bs4 import BeautifulSoup
import requests
import unittest


class UnitTestsDataMinerSocieteCom(unittest.TestCase):
    def test_extract_the_name_of_one_company(self):
        print("test_extract_the_name_of_one_company")

        url = "https://www.societe.com/cgi-bin/search?champs=499234730"

        payload = {}

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        # Request the content of a page from the url
        html = requests.request("GET", url, headers=headers, data=payload)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.content, 'html.parser')

        if soup.select_one("#rensjur") is not None:
            name = soup.select_one("#rensjur").find('td', {'class': 'break-word'}).text
            print("name of the company : " + name)
        else:
            print("name of the company non présent")

    def test_extract_the_postal_address_of_one_company(self):
        print("test_extract_the_postal_address_of_one_company")

        url = "https://www.societe.com/cgi-bin/search?champs=421100645"

        payload = {}

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        # Request the content of a page from the url
        html = requests.request("GET", url, headers=headers, data=payload)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.content, 'html.parser')

        if soup.select_one("#companyAdress") is not None:
            adresse_postale = soup.select_one("#companyAdress")\
                .text\
                .replace('\n', ' ')\
                .replace('\t', ' ')\
                .replace('\r', ' ')

            print('adresse_postale : ' + adresse_postale)
        else:
            print('no adresse_postale')

    def test_extract_the_activity_of_one_company(self):
        print("test_extract_the_activity_of_one_company")

        url = "https://www.societe.com/cgi-bin/search?champs=421100645"

        payload = {}

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        # Request the content of a page from the url
        html = requests.request("GET", url, headers=headers, data=payload)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.content, 'html.parser')

        if soup.select_one("#ape-histo-description") is not None:
            activite = soup.select_one("#ape-histo-description")\
                .text \
                .replace('  ', '') \
                .replace('\n', '')\
                .replace('\t', '')\
                .replace('\r', '')

            print('activite : ' + activite)
        else:
            print('no activite')

    def test_extract_the_capital_social_of_one_company(self):
        print("test_extract_the_capital_social_of_one_company")

        url = "https://www.societe.com/cgi-bin/search?champs=421100645"

        payload = {}

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        # Request the content of a page from the url
        html = requests.request("GET", url, headers=headers, data=payload)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.content, 'html.parser')

        if soup.select_one("#capital-histo-description") is not None:
            capital_social = soup.select_one("#capital-histo-description")\
                .text\
                .replace(' ', '')\
                .replace('\n', '')\
                .replace('\t', '')\
                .replace('\r', '')\
                .replace(',00EURO', '')

            print('capital social : ' + capital_social)
        else:
            print('no capital social')

    def test_extract_the_tranche_effectif_of_one_company(self):
        print("test_extract_the_tranche_effectif_of_one_company")

        url = "https://www.societe.com/cgi-bin/search?champs=421100645"

        payload = {}

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        # Request the content of a page from the url
        html = requests.request("GET", url, headers=headers, data=payload)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.content, 'html.parser')

        if soup.select_one("#trancheeff-histo-description") is not None:
            tranche_effectif = soup.select_one("#trancheeff-histo-description")\
                .text\
                .replace('  ', '')\
                .replace('\n', '')\
                .replace('\t', '')\
                .replace('\r', '')

            print('tranche_effectif : ' + tranche_effectif)
        else:
            print('no tranche_effectif')

    def test_extract_the_president_of_one_company(self):
        print("test_extract_the_president_of_one_company")

        url = "https://www.societe.com/cgi-bin/search?champs=421100645"

        payload = {}

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        # Request the content of a page from the url
        html = requests.request("GET", url, headers=headers, data=payload)

        # print(html.text)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.content, 'html.parser')

        for i in range(1, 20):
            if soup.select_one("#dir" + str(i)) is not None:
                president = soup.select_one("#dir" + str(i))\
                    .find_all('td')[1]\
                    .text\
                    .replace('\n', '')\
                    .replace('\t', '')\
                    .replace('\r', '')

                if president != "":
                    print("president of the company : " + president)
                    break
            else:
                print('no president')

    def test_is_big_company(self):
        print("test_is_big_company")

        raison_sociale = ""
        adresse_postale = ""
        siren = str(4)+str(2)+str(1)+str(1)+str(0)+str(0)+str(6)+str(4)+str(5)
        activite = ""
        capital_social = 0
        tranche_effectif = ""
        president = ""

        url = "https://www.societe.com/cgi-bin/search?champs=" + siren

        payload = {}

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        # Request the content of a page from the url
        html = requests.request("GET", url, headers=headers, data=payload)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.content, 'html.parser')

        if soup.select_one("#capital-histo-description") is not None \
                and \
                soup.select_one("#trancheeff-histo-description") is not None:
            # tranche_effectif
            tranche_effectif += soup.select_one("#trancheeff-histo-description") \
                .text \
                .replace('  ', '') \
                .replace('\n', '') \
                .replace('\t', '') \
                .replace('\r', '')

            # capital_social
            capital_social += int(soup.select_one("#capital-histo-description") \
                .text \
                .replace(' ', '') \
                .replace('\n', '') \
                .replace('\t', '') \
                .replace('\r', '') \
                .replace(',00EURO', ''))

            if capital_social >= 2000000000 or tranche_effectif == "2000 à 4999 salariés":
                # raison_sociale
                if soup.select_one("#rensjur") is not None:
                    raison_sociale += soup\
                        .select_one("#rensjur")\
                        .find('td', {'class': 'break-word'})\
                        .text\
                        .replace(' ', '') \
                        .replace('\n', '') \
                        .replace('\t', '') \
                        .replace('\r', '')
                else:
                    print("name of the company non présent")

                # activite
                if soup.select_one("#ape-histo-description") is not None:
                    activite += soup.select_one("#ape-histo-description") \
                        .text \
                        .replace('  ', '') \
                        .replace('\n', '') \
                        .replace('\t', '') \
                        .replace('\r', '')

                    print('activite : ' + activite)
                else:
                    print('no activite')

                # president
                for i in range(1, 20):
                    if soup.select_one("#dir" + str(i)) is not None:
                        president += soup.select_one("#dir" + str(i)) \
                            .find_all('td')[1] \
                            .text \
                            .replace('\n', '') \
                            .replace('\t', '') \
                            .replace('\r', '')

                        if president != "":
                            print("president of the company : " + president)
                            break
                    else:
                        print('no president')

                x = {
                    'raison_sociale': raison_sociale,
                    'adresse_postale': adresse_postale,
                    'siren': siren,
                    'activite': activite,
                    'capital_social': capital_social,
                    'tranche_effectif': tranche_effectif,
                    'president': president
                }

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
                            sql = "INSERT INTO `grandes_entreprises` (" \
                                  "`raison_sociale`, " \
                                  "`adresse_postale`, " \
                                  "`siren`, " \
                                  "`activite`, " \
                                  "`capital_social`, " \
                                  "`tranche_effectif`, " \
                                  "`president`) VALUE (%s, %s, %s, %s, %s, %s, %s)"

                            cursor.execute(sql, (
                                x.get('raison_sociale'),
                                x.get('adresse_postale'),
                                x.get('siren'),
                                x.get('activite'),
                                x.get('capital_social'),
                                x.get('tranche_effectif'),
                                x.get('president')
                            ))

                            connection.commit()

                            print('siren ' + x.get('siren') + ' : big company')

                            connection.close()
                        except Exception as e:
                            print("The record already exists : " + str(e))
                            connection.close()
                except Exception as e:
                    print("Problem connection MySQL : " + str(e))
            else:
                print('siren ' + siren + ' no big company')
        else:
            print("no information")

    def test_extract_all_big_companies(self):
        print("test_extract_the_president_of_one_company")

        # loop 1
        for l1 in range(0, 9):
            # loop 2
            for l2 in range(0, 9):
                # loop 3
                for l3 in range(0, 9):
                    # loop 4
                    for l4 in range(0, 9):
                        # loop 5
                        for l5 in range(0, 9):
                            # loop 6
                            for l6 in range(0, 9):
                                # loop 7
                                for l7 in range(0, 9):
                                    # loop 8
                                    for l8 in range(0, 9):
                                        # loop 9
                                        for l9 in range(0, 9):
                                            raison_sociale = ""
                                            adresse_postale = ""
                                            siren = str(l1)+str(l2)+str(l3)+str(l4)+str(l5)+str(l6)+str(l7)\
                                                    +str(l8)+str(l9)
                                            activite = ""
                                            capital_social = 0
                                            tranche_effectif = ""
                                            president = ""

                                            url = "https://www.societe.com/cgi-bin/search?champs=" + siren

                                            payload = {}

                                            headers = {
                                                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
                                            }

                                            time.sleep(3)

                                            # Request the content of a page from the url
                                            html = requests.request("GET", url, headers=headers, data=payload)

                                            # Parse the content of html_doc
                                            soup = BeautifulSoup(html.content, 'html.parser')

                                            if soup.select_one("#capital-histo-description") is not None \
                                                    and \
                                                    soup.select_one("#trancheeff-histo-description") is not None:
                                                # tranche_effectif
                                                tranche_effectif += soup.select_one("#trancheeff-histo-description") \
                                                    .text \
                                                    .replace('  ', '') \
                                                    .replace('\n', '') \
                                                    .replace('\t', '') \
                                                    .replace('\r', '')

                                                # capital_social
                                                capital_social += int(soup.select_one("#capital-histo-description") \
                                                                      .text \
                                                                      .replace(' ', '') \
                                                                      .replace('\n', '') \
                                                                      .replace('\t', '') \
                                                                      .replace('\r', '') \
                                                                      .replace(',00EURO', ''))

                                                if capital_social >= 2000000000 or tranche_effectif == "2000 à 4999 salariés":
                                                    # raison_sociale
                                                    if soup.select_one("#rensjur") is not None:
                                                        raison_sociale += soup \
                                                            .select_one("#rensjur") \
                                                            .find('td', {'class': 'break-word'}) \
                                                            .text \
                                                            .replace(' ', '') \
                                                            .replace('\n', '') \
                                                            .replace('\t', '') \
                                                            .replace('\r', '')

                                                    # activite
                                                    if soup.select_one("#ape-histo-description") is not None:
                                                        activite += soup.select_one("#ape-histo-description") \
                                                            .text \
                                                            .replace('  ', '') \
                                                            .replace('\n', '') \
                                                            .replace('\t', '') \
                                                            .replace('\r', '')

                                                    # president
                                                    for i in range(1, 20):
                                                        if soup.select_one("#dir" + str(i)) is not None:
                                                            president += soup.select_one("#dir" + str(i)) \
                                                                .find_all('td')[1] \
                                                                .text \
                                                                .replace('\n', '') \
                                                                .replace('\t', '') \
                                                                .replace('\r', '')

                                                            if president != "":
                                                                break

                                                    x = {
                                                        'raison_sociale': raison_sociale,
                                                        'adresse_postale': adresse_postale,
                                                        'siren': siren,
                                                        'activite': activite,
                                                        'capital_social': capital_social,
                                                        'tranche_effectif': tranche_effectif,
                                                        'president': president
                                                    }

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
                                                                sql = "INSERT INTO `grandes_entreprises` (" \
                                                                      "`raison_sociale`, " \
                                                                      "`adresse_postale`, " \
                                                                      "`siren`, " \
                                                                      "`activite`, " \
                                                                      "`capital_social`, " \
                                                                      "`tranche_effectif`, " \
                                                                      "`president`) VALUE (%s, %s, %s, %s, %s, %s, %s)"

                                                                cursor.execute(sql, (
                                                                    x.get('raison_sociale'),
                                                                    x.get('adresse_postale'),
                                                                    x.get('siren'),
                                                                    x.get('activite'),
                                                                    x.get('capital_social'),
                                                                    x.get('tranche_effectif'),
                                                                    x.get('president')
                                                                ))

                                                                connection.commit()

                                                                print('siren ' + x.get('siren') + ' : big company')

                                                                connection.close()
                                                            except Exception as e:
                                                                print("The record already exists (siren : " + siren
                                                                      + ") : " + str(e))
                                                                connection.close()
                                                    except Exception as e:
                                                        print("Problem connection MySQL (siren : " + siren
                                                              + ") : " + str(e))
                                                else:
                                                    print('siren ' + siren + ' : no big company')
                                            else:
                                                print('siren ' + siren + ' : no information')

    def test_extract_location_from_response_headers(self):
        print("test_extract_location_from_response_headers")

        url = "https://www.societe.com/cgi-bin/search?champs=883632556"

        payload = {}

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        """
                headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'DNT': '1',
            'Host': 'www.societe.com',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
            'Cookie': '__gads=ID=11cba7a89291ea57:T=1596196217:S=ALNI_MbJ7ZDrC-OxBl6od5uoMq5CiwrGqg; euconsent=BO3aEC6O3aEC6CkABAFRDV-AAAAx57_______9_-____9uz_Ov_v_f__33e8__9v_l_7_-___u_-23d4u_1vf99yfmx-7etr3tp_47ues2_Xurf_71__3z3_9pxP78E89r7335EQ_v-_t-b7BCHN_Y2v-8K96lPKACA; pubconsent=BO3aEC6O3aEC6CkABAFRDVAB-AAACAAABgAAAAAAAAAA; crfgL0cSt0r=true; hu45=1',
            'Remote-Address': '62.4.31.3:443',
            'Referrer-Policy': 'no-referrer-when-downgrade'
        }
        """

        # Request the content of a page from the url
        response = requests.request("GET", url, headers=headers, data=payload)

        print("location : " + str(response.headers))


if __name__ == '__main__':
    unittest.main()
