import json
import unittest
import pymysql
import requests
from bs4 import BeautifulSoup
import xlsxwriter
import time
from requests_tor import RequestsTor

password = 'azerAZER123098,,,'


class UnitTestsAnnuaireServicePublic(unittest.TestCase):
    def test_extract_nom(self):
        print("test_extract_nom")

        url_result = "https://lannuaire.service-public.fr/la-reunion/reunion/mairie-97409-01"

        # Request the content of a page from the url
        html = requests.get(url_result)

        time.sleep(3)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.content, 'html.parser')

        if soup.select_one("#contentTitle") is not None:
            print("title : " + soup.select_one("#contentTitle").text)
        else:
            print("no title")

    def test_extract_adresse_postale(self):
        print("test_extract_adresse_postale")

        url_result = "https://lannuaire.service-public.fr/la-reunion/reunion/mairie-97409-01"

        # Request the content of a page from the url
        html = requests.get(url_result)

        time.sleep(3)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.content, 'html.parser')

        if soup.find("div", {'itemprop': 'address'}) is not None:
            adresse_postale = soup.find("div", {'itemprop': 'address'}).find('p', {'class': 'mb-map'})\
                .text\
                .replace("\n", " ")\
                .replace('\t', " ")\
                .replace("Afficher la carte", "")

            print("adresse postale : " + adresse_postale)
        else:
            print("no adresse postale")

    def test_extract_telephone(self):
        print("test_extract_telephone")

        url_result = "https://lannuaire.service-public.fr/la-reunion/reunion/mairie-97409-01"

        # Request the content of a page from the url
        html = requests.get(url_result)

        time.sleep(3)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.content, 'html.parser')

        # telephone
        if soup.select_one("#contentPhone_1") is not None:
            telephone = soup.select_one("#contentPhone_1").text

            print("telephone : " + telephone)
        else:
            print("no telephone")

    def test_extract_site_internet(self):
        print("test_extract_site_internet")

        url_result = "https://lannuaire.service-public.fr/la-reunion/reunion/mairie-97409-01"

        # Request the content of a page from the url
        html = requests.get(url_result)

        time.sleep(3)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.content, 'html.parser')

        # site internet
        if soup.select_one("#websites") is not None:
            website = soup.select_one("#websites").text

            print("website : " + website)
        else:
            print("no website")

    def test_extract_mail(self):
        print("test_extract_mail")

        url_result = "https://lannuaire.service-public.fr/la-reunion/reunion/mairie-97409-01"

        # Request the content of a page from the url
        html = requests.get(url_result)

        time.sleep(3)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.content, 'html.parser')

        # mail
        if soup.find("a", {'class': 'send-mail'}) is not None:
            content_contact_email = soup.find("a", {'class': 'send-mail'})\
                .text\
                .replace("\n", "")

            print("content_contact_email : " + content_contact_email)
        else:
            print("no content_contact_email")

    # ok
    def test_extract_one_mail_into_mysql_with_dark_web(self):
        print("test_extract_one_mail_into_mysql_with_dark_web")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/51.0.2704.103'
        }

        url_result = "https://lannuaire.service-public.fr/gouvernement/administration-centrale-ou-ministere_172120"

        rt = RequestsTor()

        html_with_tor = rt.get(url_result, headers=headers)

        time.sleep(3)

        soup = BeautifulSoup(html_with_tor.content, 'html.parser')

        # email
        if soup.find("p", {'itemprop': 'email'}) is not None:
            emails = soup.find_all("p", {'itemprop': 'email'})

            for email in emails:
                contact_email = email.find('a').text.replace("\n", "").replace(" ", "")

                x = {
                    'email': contact_email
                }

                try:
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
                            sql = "INSERT INTO `emails_annuaire_service_public` (`email`) VALUE (%s)"

                            cursor.execute(sql, (
                                x.get('email')
                            ))

                            connection.commit()

                            print("email " + str(contact_email) + " : ok")

                            connection.close()
                        except Exception as e:
                            print("The record already exists for : " + str(contact_email) + " : " + str(e))
                            connection.close()
                except Exception as e:
                    print("Problem connection MySQL : " + str(e))
        else:
            print("no email")

    # ok
    def test_extract_emails_into_mysql_with_dark_web(self):
        print("test_extract_emails_into_mysql_with_dark_web")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/51.0.2704.103'
        }

        for i in range(0, 2000001):
            url_result = "https://lannuaire.service-public.fr/gouvernement/administration-centrale-ou-ministere_" \
                         + str(i)

            rt = RequestsTor()

            html_with_tor = rt.get(url_result, headers=headers)

            soup = BeautifulSoup(html_with_tor.content, 'html.parser')

            # email
            if soup.find("p", {'itemprop': 'email'}) is not None:
                emails = soup.find_all("p", {'itemprop': 'email'})

                for email in emails:
                    contact_email = email.find('a').text.replace("\n", "").replace(" ", "")

                    x = {
                        'email': contact_email
                    }

                    try:
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
                                sql = "INSERT INTO `emails_annuaire_service_public` (`email`) VALUE (%s)"

                                cursor.execute(sql, (
                                    x.get('email')
                                ))

                                connection.commit()

                                print("email " + str(contact_email) + " : ok")

                                connection.close()
                            except Exception as e:
                                print("The record already exists for : " + str(contact_email) + " : " + str(e))
                                connection.close()
                    except Exception as e:
                        print("Problem connection MySQL : " + str(e))
            else:
                print("no email")

    # ok
    def test_extract_emails_into_mysql_with_clear_web(self):
        print("test_extract_emails_into_mysql_with_clear_web")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/51.0.2704.103'
        }

        for i in range(2885, 2000001):
            try:
                url_result = "https://lannuaire.service-public.fr/gouvernement/administration-centrale-ou-ministere_" \
                             + str(i)

                print(url_result)

                html = requests.get(url_result, headers=headers)

                soup = BeautifulSoup(html.content, 'html.parser')

                # email
                if soup.find("p", {'itemprop': 'email'}) is not None:
                    emails = soup.find_all("p", {'itemprop': 'email'})

                    for email in emails:
                        contact_email = email.find('a').text.replace("\n", "").replace(" ", "")

                        x = {
                            'email': contact_email
                        }

                        try:
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
                                    sql = "INSERT INTO `emails_annuaire_service_public` (`email`) VALUE (%s)"

                                    cursor.execute(sql, (
                                        x.get('email')
                                    ))

                                    connection.commit()

                                    print("email " + str(contact_email) + " : ok")

                                    connection.close()
                                except Exception as e:
                                    print("The record already exists for : " + str(contact_email) + " : " + str(e))
                                    connection.close()
                        except Exception as e:
                            print("Problem connection MySQL : " + str(e))
                else:
                    print("no email")
            except Exception as e:
                print("error : " + str(e))

    def test_extract_horaires_ouverture(self):
        print("test_extract_horaires_ouverture")

        url_result = "https://lannuaire.service-public.fr/la-reunion/reunion/mairie-97409-01"

        # Request the content of a page from the url
        html = requests.get(url_result)

        time.sleep(3)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.content, 'html.parser')

        # horaires ouverture
        horaires_ouverture = ''
        if soup.find("div", {'itemprop': 'hoursAvailable'}) is not None:
            horaires_ouverture += soup.find("div", {'itemprop': 'hoursAvailable'})\
                .text\
                .replace("\n", "")

            print("horaires ouverture : " + horaires_ouverture)
        else:
            print("no horaires ouverture")

    def test_extract_information_for_one_contact(self):
        print('test_extract_information_for_one_contact')

        url_result = "https://lannuaire.service-public.fr/la-reunion/reunion/mairie-97409-01"

        # Request the content of a page from the url
        html = requests.get(url_result)

        time.sleep(3)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.content, 'html.parser')

        # nom
        nom = ""
        if soup.select_one("#contentTitle") is not None:
            nom += soup.select_one("#contentTitle").text
        else:
            print("no title")

        # adresse postale
        adresse_postale = ""
        if soup.find("div", {'itemprop': 'address'}) is not None:
            adresse_postale += soup.find("div", {'itemprop': 'address'}).find('p', {'class': 'mb-map'})\
                .text\
                .replace("\n", " ")\
                .replace('\t', " ")\
                .replace("Afficher la carte", "")
        else:
            print("no adresse postale")

        # telephone
        telephone = ""
        if soup.select_one("#contentPhone_1") is not None:
            telephone += soup.select_one("#contentPhone_1").text
        else:
            print("no telephone")

        # site internet
        website = ""
        if soup.select_one("#websites") is not None:
            website += soup.select_one("#websites").text
        else:
            print("no website")

        # email
        email = ""
        if soup.find("a", {'class': 'send-mail'}) is not None:
            email += soup.find("a", {'class': 'send-mail'})\
                .text\
                .replace("\n", "")
        else:
            print("no content_contact_email")

        # horaires ouverture
        horaires_ouverture = ''
        if soup.find("div", {'itemprop': 'hoursAvailable'}) is not None:
            horaires_ouverture += soup.find("div", {'itemprop': 'hoursAvailable'})\
                .text\
                .replace("\n", "")

            print("horaires ouverture : " + horaires_ouverture)
        else:
            print("no horaires ouverture")

        x = {
                'nom': nom,
                'adresse_postale': adresse_postale,
                'telephone': telephone,
                'website': website,
                'email': email,
                'horaires_ouverture': horaires_ouverture
            }

        print("contact ville : " + str(x))

    def test_extract_list_of_contacts_for_all_pages(self):
        print("test_extract_list_of_contacts_for_all_pages")

        url_list = "https://lannuaire.service-public.fr/recherche?where=ile%20de%20france&whoWhat=pr%C3%A9fecture&page="

        number_of_pages = 8

        i = 1

        for x in range(1, number_of_pages + 1):
            # Request the content of a page from the url
            html_list = requests.get(url_list)

            time.sleep(3)

            # Parse the content of html_doc
            soup = BeautifulSoup(html_list.content, 'html.parser')

            if soup.find("ul", {"class", "result-list"}) is not None:
                all_li = soup.find("ul", {"class", "result-list"}).find_all("li", {"class", "result-item"})

                for li in all_li:
                    lien = li.find("a").get("href")

                    html_lien = requests.get(lien)

                    time.sleep(3)

                    # Parse the content of html_doc
                    soup_lien = BeautifulSoup(html_lien.content, 'html.parser')

                    title = ""
                    adresse_postale = ""
                    telephone = ""
                    website = ""
                    content_contact_email = ""

                    if soup_lien.select_one("#contentTitle") is not None:
                        title += soup_lien.select_one("#contentTitle").text
                    else:
                        print(str(i) + " no title")

                    if soup_lien.select_one("#officialAddress") is not None:
                        adresse_postale += soup_lien.select_one("#officialAddress").text.replace("\n", " ").replace(
                            "Afficher la carte", "")
                    else:
                        print(str(i) + " no adresse postale")

                    if soup_lien.select_one("#contentPhone_1") is not None:
                        telephone += soup_lien.select_one("#contentPhone_1").text
                    else:
                        print(str(i) + " no telephone")

                    if soup_lien.select_one("#websites") is not None:
                        website += soup_lien.select_one("#websites").text
                    else:
                        print(str(i) + " no website")

                    if soup_lien.select_one("#contentContactEmail") is not None:
                        content_contact_email += "'" + soup_lien.select_one("#contentContactEmail").text\
                            .replace("        Courriel : ", "") \
                            .replace("      ", "") \
                            .replace("\n", "") + "',"
                    else:
                        print(str(i) + " no content_contact_email")

                    print(str(i) + " contact : "
                          + title + " / "
                          + adresse_postale + " / "
                          + telephone + " / "
                          + website + " / "
                          + content_contact_email)

                    i += 1
            else:
                print("no ul class result-list")

    def test_extract_contacts_for_excel_for_all_pages(self):
        print("test_extract_list_of_contacts_for_all_pages")

        url_list = "https://lannuaire.service-public.fr/recherche?where=ile%20de%20france&whoWhat=pr%C3%A9fecture&page="

        number_of_pages = 8

        i = 1

        contacts = []

        for x in range(1, number_of_pages + 1):
            # Request the content of a page from the url
            html_list = requests.get(url_list)

            time.sleep(2)

            # Parse the content of html_doc
            soup = BeautifulSoup(html_list.content, 'html.parser')

            if soup.find("ul", {"class", "result-list"}) is not None:
                all_li = soup.find("ul", {"class", "result-list"}).find_all("li", {"class", "result-item"})

                for li in all_li:
                    lien = li.find("a").get("href")

                    html_lien = requests.get(lien)

                    time.sleep(2)

                    # Parse the content of html_doc
                    soup_lien = BeautifulSoup(html_lien.content, 'html.parser')

                    title = ""
                    adresse_postale = ""
                    telephone = ""
                    website = ""
                    content_contact_email = ""

                    if soup_lien.select_one("#contentTitle") is not None:
                        title += soup_lien.select_one("#contentTitle").text
                    else:
                        print(str(i) + " no title")

                    if soup_lien.select_one("#officialAddress") is not None:
                        adresse_postale += soup_lien.select_one("#officialAddress").text.replace("\n", " ").replace(
                            "Afficher la carte", "")
                    else:
                        print(str(i) + " no adresse postale")

                    if soup_lien.select_one("#contentPhone_1") is not None:
                        telephone += soup_lien.select_one("#contentPhone_1").text
                    else:
                        print(str(i) + " no telephone")

                    if soup_lien.select_one("#websites") is not None:
                        website += soup_lien.select_one("#websites").text
                    else:
                        print(str(i) + " no website")

                    if soup_lien.select_one("#contentContactEmail") is not None:
                        content_contact_email += "'" + soup_lien.select_one("#contentContactEmail").text\
                            .replace("        Courriel : ", "") \
                            .replace("      ", "") \
                            .replace("\n", "") + "',"
                    else:
                        print(str(i) + " no content_contact_email")

                    print(str(i) + " contact : "
                          + title + " / "
                          + adresse_postale + " / "
                          + telephone + " / "
                          + website + " / "
                          + content_contact_email)

                    contact = {
                        "title": title,
                        "adresse_postale": adresse_postale,
                        "telephone": telephone,
                        "website": website,
                        "content_contact_email": content_contact_email
                    }

                    contacts.append(contact)

                    i += 1

            else:
                print("no ul class result-list")

        # Create a workbook and add a worksheet
        workbook = xlsxwriter.Workbook('a_s_p_pref_i_d_f.xlsx')
        worksheet = workbook.add_worksheet('data')

        worksheet.write(0, 0, 'title')
        worksheet.write(0, 1, 'adresse_postale')
        worksheet.write(0, 2, 'telephone')
        worksheet.write(0, 3, 'website')
        worksheet.write(0, 4, 'content_contact_email')

        row = 1

        for one_contact in contacts:
            # title
            worksheet.write(row, 0, one_contact.get('title'))

            # adresse_postale
            worksheet.write(row, 1, one_contact.get('adresse_postale'))

            # telephone
            worksheet.write(row, 2, one_contact.get('telephone'))

            # website
            worksheet.write(row, 3, one_contact.get('website'))

            # content_contact_email
            worksheet.write(row, 4, one_contact.get('content_contact_email'))

            row += 1

        workbook.close()

    # ok
    def test_extract_contacts_for_excel_for_all_mairies_in_mysql(self):
        print("test_extract_contacts_for_excel_for_all_mairies_in_mysql")

        url_regions = "https://geo.api.gouv.fr/regions?fields=code,nom,codeDepartement&format=json"

        payload = {}

        headers = {}

        response = requests.request("GET", url_regions, headers=headers, data=payload)

        regions = json.loads(response.text)

        for region in regions:
            code_region = str(region['code'])

            nom_region = region['nom'].lower()\
                .replace('î', 'i')\
                .replace('é', 'e')\
                .replace('è', 'e')\
                .replace('à', 'a')\
                .replace('ô', 'o')\
                .replace("'", '-')\
                .replace(' ', '-')

            url_departements = "https://geo.api.gouv.fr/regions/" + code_region + "/departements?fields=code,nom,codeRegion,region&format=json"

            payload = {}

            headers = {}

            response = requests.request("GET", url_departements, headers=headers, data=payload)

            departements = json.loads(response.text)

            for departement in departements:
                code_departement = departement['code']

                nom_departement = departement['nom'].lower()\
                    .replace('î', 'i')\
                    .replace('é', 'e')\
                    .replace('è', 'e')\
                    .replace('à', 'a')\
                    .replace('ô', 'o')\
                    .replace("'", '-')\
                    .replace(' ', '-')

                url_communes = "https://geo.api.gouv.fr/departements/" + code_departement + "/communes?fields=nom,code,codesPostaux,codeDepartement,codeRegion,population&format=json&geometry=centre"

                payload = {}

                headers = {}

                response = requests.request("GET", url_communes, headers=headers, data=payload)

                communes = json.loads(response.text)

                for commune in communes:
                    code_insee_commune = commune['code']

                    url_result = "https://lannuaire.service-public.fr/" + nom_region + "/" + nom_departement \
                                 + "/mairie-" + code_insee_commune + "-01"

                    # Request the content of a page from the url
                    html = requests.get(url_result)

                    # Parse the content of html_doc
                    soup = BeautifulSoup(html.content, 'html.parser')

                    # nom
                    nom = ""
                    if soup.select_one("#contentTitle") is not None:
                        nom += soup.select_one("#contentTitle").text
                    else:
                        print("no title")

                    # adresse postale
                    adresse_postale = ""
                    if soup.find("div", {'itemprop': 'address'}) is not None:
                        adresse_postale += soup.find("div", {'itemprop': 'address'}).find('p', {'class': 'mb-map'})\
                            .text\
                            .replace("\n", " ")\
                            .replace('\t', " ")\
                            .replace("Afficher la carte", "")
                    else:
                        print("no adresse postale")

                    # telephone
                    telephone = ""
                    if soup.select_one("#contentPhone_1") is not None:
                        telephone += soup.select_one("#contentPhone_1").text
                    else:
                        print("no telephone")

                    # site internet
                    website = ""
                    if soup.select_one("#websites") is not None:
                        website += soup.select_one("#websites").text
                    else:
                        print("no website")

                    # email
                    email = ""
                    if soup.find("a", {'class': 'send-mail'}) is not None:
                        email += soup.find("a", {'class': 'send-mail'})\
                            .text\
                            .replace("\n", "")
                    else:
                        print("no content_contact_email")

                    # horaires ouverture
                    horaires_ouverture = ''
                    if soup.find("div", {'itemprop': 'hoursAvailable'}) is not None:
                        horaires_ouverture += soup.find("div", {'itemprop': 'hoursAvailable'})\
                            .text\
                            .replace("\n", "")

                        print("horaires ouverture : " + horaires_ouverture)
                    else:
                        print("no horaires ouverture")

                    x = {
                            'nom': nom,
                            'adresse_postale': adresse_postale,
                            'telephone': telephone,
                            'website': website,
                            'email': email,
                            'horaires_ouverture': horaires_ouverture
                        }

                    try:
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
                                sql = "INSERT INTO `contacts_pour_mairies` (" \
                                      "`nom`, " \
                                      "`adresse_postale`, " \
                                      "`telephone`, " \
                                      "`website`, " \
                                      "`email`, " \
                                      "`horaires_ouverture`) VALUE (%s, %s, %s, %s, %s, %s)"

                                cursor.execute(sql, (
                                    x.get('nom'),
                                    x.get('adresse_postale'),
                                    x.get('telephone'),
                                    x.get('website'),
                                    x.get('email'),
                                    x.get('horaires_ouverture')
                                ))

                                connection.commit()

                                print(url_result + " : ok")

                                connection.close()
                            except Exception as e:
                                print("The record already exists for : " + url_result + " : " + str(e))
                                connection.close()
                    except Exception as e:
                        print("Problem connection MySQL : " + str(e))

    def test_xlsxwriter(self):
        print("test_xlsxwriter")

        workbook = xlsxwriter.Workbook('hello.xlsx')
        worksheet = workbook.add_worksheet('data')

        worksheet.write('A1', 'Hello world')

        workbook.close()


if __name__ == '__main__':
    unittest.main()
