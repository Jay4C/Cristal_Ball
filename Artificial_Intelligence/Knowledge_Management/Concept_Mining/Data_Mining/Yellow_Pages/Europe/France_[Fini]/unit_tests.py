import json
import os
import subprocess
from selenium.webdriver.firefox.options import Options
import xlsxwriter
from bs4 import BeautifulSoup
import requests
import time
import pymysql.cursors
import unittest
from validate_email import validate_email
import xlrd
import warnings
from selenium import webdriver
from base64 import urlsafe_b64decode

password = 'azerAZER123098,,,'


class UnitTestsDataMiningYellowPagesFrance(unittest.TestCase):
    def test_print_html(self):
        print('test_print_html')

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://www.pagesjaunes.fr/pros/detail?bloc_id=FCP06923089CLIENTDA3000004C0001&no_sequence=1&code_rubrique=16053100"

        # Request the content of a page from the url
        html = requests.get(url, headers=headers)

        print(html.text)

    def test_extract_one_email(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://www.pagesjaunes.fr/pros/detail?bloc_id=FCP06923089CLIENTDA3000004C0001&no_sequence=1&code_rubrique=16053100"

        # Request the content of a page from the url
        html = requests.get(url, headers=headers)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.content, 'html.parser')

        if soup.select_one("#teaser-footer") is not None:
            if soup.select_one("#teaser-footer").find("div", {'class': 'zone-coordonnees'}) is not None:
                if soup.select_one("#teaser-footer").find("div", {'class': 'zone-coordonnees'}) \
                        .find('div', {'class': 'lvs-container marg-btm-s'}) is not None:
                    if soup.select_one("#teaser-footer").find("div", {'class': 'zone-coordonnees'}) \
                            .find("div", {'class': 'lvs-container marg-btm-s'}).find("a") is not None:

                        email = "contact@" + soup \
                            .select_one("#teaser-footer") \
                            .find("div", {'class': 'zone-coordonnees'}) \
                            .find("div", {'class': 'lvs-container marg-btm-s'}) \
                            .find("a") \
                            .get("href") \
                            .replace(" nouvelle fenêtre", "") \
                            .replace("https://www.", "") \
                            .replace("http://www.", "") \
                            .replace("https://", "") \
                            .replace("http://", "")

                        print("email : " + str(email))
                    else:
                        print("a : no email business")
                else:
                    print("lvs-container marg-btm-s : no email business")
            else:
                print("zone-coordonnees : no email business")
        else:
            print("teaser-footer : no email business")

    def test_extract_url_for_all_page_of_results_for_one_activity_and_capital(self):
        print("test_extract_url_for_all_page_of_results_for_one_activity_and_capital")

        try:
            url_of_one_page_of_results = "https://www.pagesjaunes.fr/annuaire/chercherlespros?quoiqui=comptable&ou=Paris%20%2875%29&idOu=L07505600&proximite=0&quoiQuiInterprete=comptable&contexte=fVIK9BsX77ZcJI7BdVaQfZm0pk1HqOwSREm4eF/eFefkpIXHrdTdDqmfqUEyp24j5FJxmqvp2aAm4C%2BLM%2BIj4BeZMbwlFgk4CeI566ac52s%3D&page=2"

            time.sleep(2)

            html_of_one_page_of_results = requests.get(url_of_one_page_of_results)

            soup_of_one_page_of_results = BeautifulSoup(html_of_one_page_of_results.text, 'html.parser')

            i_1 = 1

            if soup_of_one_page_of_results.select_one("#listResults").select("ul")[0].find("li") is not None:
                all_li = soup_of_one_page_of_results \
                    .select_one("#listResults") \
                    .select("ul")[0] \
                    .find_all('li', {'class': 'bi-bloc'})

                for i in range(0, len(all_li)):
                    try:
                        if all_li[i].find("h3", {"class": "company-name noTrad"}) is not None:
                            if all_li[i].find("h3", {"class": "company-name noTrad"}).select("a")[0].get('href') == "#":
                                json_bloc = json.loads(all_li[i].get('data-pjtoggleclasshisto'))

                                bloc_id = json_bloc["idbloc"]["id_bloc"]

                                no_sequence = json_bloc["idbloc"]["no_sequence"]

                                json_code_rubrique = json.loads(all_li[i].select("div")[0].get(
                                    'data-pjinfosaccengage-rmk-connexefd-' + bloc_id.lower()))

                                code_rubrique = json_code_rubrique["kAN9ProToUserInfo"]

                                url_page_1 = 'https://www.pagesjaunes.fr/pros/detail?bloc_id=' + bloc_id + \
                                             '&no_sequence=' + no_sequence + '&code_rubrique=' + code_rubrique

                                print(url_page_1)
                            else:
                                try:
                                    url_page_2 = 'https://www.pagesjaunes.fr' + all_li[i] \
                                        .find("h3", {"class": "company-name noTrad"}) \
                                        .select("a")[0].get('href')

                                    print(url_page_2)
                                except Exception as e:
                                    print("error url_page_2 : " + str(e))
                        else:
                            print(str(i_1) + " no h3 class company-name noTrad")
                    except Exception as e:
                        print(str(i_1) + " error 1 : " + str(e))

                    i_1 += 1
            else:
                print('sorry there is nothing')

        except Exception as e:
            print(str(e))

    def test_extract_emails_from_all_page_of_results_for_one_activity_and_capital(self):
        try:
            activity = "hotel"
            city = "Ile-de-France"
            numero_page = "1"

            url_search = "https://www.pagesjaunes.fr/annuaire/chercherlespros?quoiqui=" \
                         + activity + "&ou=" + city + "&idOu=L07505600&proximite=0&quoiQuiInterprete=" \
                         + city + "&contexte=fVIK9BsX77ZcJI7BdVaQfZm0pk1HqOwSREm4eF/eFefkpIXHrdTdDqmfqUEyp24j5FJxmqvp2aAm4C%2BLM%2BIj4BeZMbwlFgk4CeI566ac52s%3D" \
                         + "&page=" + numero_page

            html_search = requests.get(url_search)
            soup_search = BeautifulSoup(html_search.content, 'html.parser')

            number_of_pages = 0

            if soup_search.select_one("#SEL-nbresultat") is not None:
                number_of_pages_with_coma = int(soup_search
                                                .select_one("#SEL-nbresultat")
                                                .text
                                                .replace(" ", "")
                                                ) / 20

                if int(str(number_of_pages_with_coma).split(".")[1][:1]) < 5:
                    number_of_pages += round(number_of_pages_with_coma) + 1
                    if number_of_pages > 100:
                        number_of_pages = 100
                        print('number_of_pages : ' + str(number_of_pages))
                    else:
                        print('number_of_pages : ' + str(number_of_pages))

                elif int(str(number_of_pages_with_coma).split(".")[1][:1]) >= 5:
                    number_of_pages += round(number_of_pages_with_coma)
                    if number_of_pages > 100:
                        number_of_pages = 100
                        print('number_of_pages : ' + str(number_of_pages))
                    else:
                        print('number_of_pages : ' + str(number_of_pages))
            else:
                print("there is no results")

            i_1 = 0

            if number_of_pages > 1:
                for i in range(1, number_of_pages + 1):
                    url_of_one_page_of_results = "https://www.pagesjaunes.fr/annuaire/chercherlespros?quoiqui=" \
                                                 + activity + "&ou=" + city + "&idOu=L07505600&proximite=0&quoiQuiInterprete=" \
                                                 + city + "&contexte=fVIK9BsX77ZcJI7BdVaQfZm0pk1HqOwSREm4eF/eFefkpIXHrdTdDqmfqUEyp24j5FJxmqvp2aAm4C%2BLM%2BIj4BeZMbwlFgk4CeI566ac52s%3D" \
                                                 + "&page=" + str(i)

                    print(url_of_one_page_of_results)

                    time.sleep(2)

                    html_of_one_page_of_results = requests.get(url_of_one_page_of_results)

                    soup_of_one_page_of_results = BeautifulSoup(html_of_one_page_of_results.content, 'html.parser')

                    if soup_of_one_page_of_results.select_one("#listResults").find("ul").find("li") is not None:
                        all_article = soup_of_one_page_of_results.select_one("#listResults").find("ul").find_all('li')

                        for i in range(0, len(all_article)):
                            i_1 += 1

                            try:
                                if all_article[i].find("div", {"class": "zone-bi"}) \
                                        .find("header", {"class": "v-card"}) \
                                        .find("div", {"class": "row-denom"}) \
                                        .find("div", {"class": "denomination"}) \
                                        .find("h3", {"class": "company-name"}) is not None:
                                    if all_article[i].find("div", {"class": "zone-bi"}) \
                                            .find("header", {"class": "v-card"}) \
                                            .find("div", {"class": "row-denom"}) \
                                            .find("div", {"class": "denomination"}) \
                                            .find("h3", {"class": "company-name"}).select("a")[0].get('href') == "#":
                                        json_bloc = json.loads(all_article[i].get('data-pjtoggleclasshisto'))

                                        bloc_id = json_bloc["idbloc"]["id_bloc"]

                                        no_sequence = json_bloc["idbloc"]["no_sequence"]

                                        json_code_rubrique = json.loads(all_article[i].select("div")[0].get(
                                            'data-pjinfosaccengage-rmk-connexefd-' + bloc_id.lower()))

                                        code_rubrique = json_code_rubrique["kAN9ProToUserInfo"]

                                        url_page = 'https://www.pagesjaunes.fr/pros/detail?bloc_id=' + bloc_id + \
                                                   '&no_sequence=' + no_sequence + '&code_rubrique=' + code_rubrique

                                        time.sleep(2)

                                        # Request the content of a page from the url
                                        html = requests.get(url_page)

                                        # Parse the content of html_doc
                                        soup = BeautifulSoup(html.content, 'html.parser')

                                        if soup \
                                                .select_one("#teaser-footer") is not None:
                                            if soup \
                                                    .select_one("#teaser-footer") \
                                                    .find("div", {'class': 'zone-coordonnees'}) is not None:
                                                if soup \
                                                        .select_one("#teaser-footer") \
                                                        .find("div", {'class': 'zone-coordonnees'}) \
                                                        .find("div",
                                                              {'class': 'lvs-container marg-btm-s'}) is not None:
                                                    if soup \
                                                            .select_one("#teaser-footer") \
                                                            .find("div", {'class': 'zone-coordonnees'}) \
                                                            .find("div", {'class': 'lvs-container marg-btm-s'}) \
                                                            .find("a") is not None:

                                                        email = "contact@" + soup \
                                                            .select_one("#teaser-footer") \
                                                            .find("div", {'class': 'zone-coordonnees'}) \
                                                            .find("div", {'class': 'lvs-container marg-btm-s'}) \
                                                            .find("a") \
                                                            .get("title") \
                                                            .replace(" nouvelle fenêtre", "") \
                                                            .replace("www.", "") \
                                                            .replace("http://", "") \
                                                            .replace("https://", "")

                                                        try:
                                                            if validate_email(email) != False:
                                                                print(
                                                                    str(
                                                                        i_1) + " The email : " + email + " does exist.")
                                                            else:
                                                                print(
                                                                    str(
                                                                        i_1) + " The email : " + email + " doesn't exist.")
                                                        except Exception as e:
                                                            print("validate_email 1 : " + str(e))
                                                    else:
                                                        print(str(i_1) + " a : no email business")
                                                else:
                                                    print(
                                                        str(i_1) + " lvs-container marg-btm-s : no email business")
                                            else:
                                                print(str(i_1) + " zone-coordonnees : no email business")
                                        else:
                                            print(str(i_1) + " teaser-footer : no email business")
                                    else:
                                        try:
                                            url_page = 'https://www.pagesjaunes.fr' + all_article[i] \
                                                .find("h3", {"class": "company-name noTrad"}) \
                                                .select("a")[0].get('href')

                                            time.sleep(2)

                                            # Request the content of a page from the url
                                            html = requests.get(url_page)

                                            # Parse the content of html_doc
                                            soup = BeautifulSoup(html.content, 'html.parser')

                                            if soup \
                                                    .select_one("#teaser-footer") is not None:
                                                if soup \
                                                        .select_one("#teaser-footer") \
                                                        .find("div", {'class': 'zone-coordonnees'}) is not None:
                                                    if soup \
                                                            .select_one("#teaser-footer") \
                                                            .find("div", {'class': 'zone-coordonnees'}) \
                                                            .find('div',
                                                                  {
                                                                      'class': 'lvs-container marg-btm-s'}) is not None:
                                                        if soup \
                                                                .select_one("#teaser-footer") \
                                                                .find("div", {'class': 'zone-coordonnees'}) \
                                                                .find("div", {'class': 'lvs-container marg-btm-s'}) \
                                                                .find("a") is not None:

                                                            email = "contact@" + soup \
                                                                .select_one("#teaser-footer") \
                                                                .find("div", {'class': 'zone-coordonnees'}) \
                                                                .find("div", {'class': 'lvs-container marg-btm-s'}) \
                                                                .find("a") \
                                                                .get("title") \
                                                                .replace(" nouvelle fenêtre", "") \
                                                                .replace("www.", "") \
                                                                .replace("http://", "") \
                                                                .replace("https://", "")

                                                            try:
                                                                if validate_email(email, verify=True) != False:
                                                                    print(
                                                                        str(
                                                                            i_1) + " The email : " + email + " does exist.")
                                                                else:
                                                                    print(
                                                                        str(
                                                                            i_1) + " The email : " + email + " doesn't exist.")
                                                            except Exception as e:
                                                                print("validate_email 2 : " + str(e))
                                                        else:
                                                            print(str(i_1) + " a : no email business")
                                                    else:
                                                        print(
                                                            str(
                                                                i_1) + " lvs-container marg-btm-s : no email business")
                                                else:
                                                    print(str(i_1) + " zone-coordonnees : no email business")
                                            else:
                                                print(str(i_1) + " teaser-footer : no email business")
                                        except Exception as e:
                                            print(str(e))
                                else:
                                    print(str(i_1) + " no company-name noTrad")
                            except Exception as e:
                                print("error 1 : " + str(e))
                    else:
                        print('sorry there is nothing')
            else:
                print("number of pages < 1")
        except Exception as e:
            print(str(e))

    def test_extract_emails_from_all_page_of_results_for_all_activities_and_capitals(self):
        activites = [
            # {'id': '1', 'url': 'agence%20interim'},
            # {'id': '2', 'url': 'agence%20immobiliere'},
            # {'id': '3', 'url': 'cabinet%20de%20recrutement'},
            # {'id': '4', 'url': 'editeur%20de%20logiciel'},
            # {'id': '5', 'url': 'hotel'},
            # {'id': '6', 'url': 'bailleur%20social'},
            # {'id': '7', 'url': 'entreprise%20de%20nettoyage'},
            # {'id': '8', 'url': 'associations'},
            # {'id': '9', 'url': 'etablissement%20financier'},
            # {'id': '10', 'url': 'restaurant'},
            # {'id': '11', 'url': 'entreprise%20du%20batiment'},
            # {'id': '12', 'url': 'coiffeur'},
            # {'id': '13', 'url': 'fleuriste'},
            # {'id': '14', 'url': 'serrurier'},
            # {'id': '15', 'url': 'boulangerie'},
            # {'id': '16', 'url': 'assurance'},
            # {'id': '17', 'url': 'pharmacie'},
            # {'id': '18', 'url': 'entreprise%20de%20demenagement'},
            # {'id': '19', 'url': 'electricite'},
            # {'id': '20', 'url': 'plomberie'},
            # {'id': '21', 'url': 'entreprise%20de%20securite'},
            # {'id': '22', 'url': 'avocat'},
            # {'id': '23', 'url': 'banque'},
            # {'id': '24', 'url': 'garage'},
            # {'id': '25', 'url': 'dentiste'},
            # {'id': '26', 'url': 'docteur'},
            # {'id': '27', 'url': 'comptable'},
            # {'id': '28', 'url': 'supermarche'},
            # {'id': '29', 'url': 'notaire'},
            # {'id': '30', 'url': 'bijoutier'},
            # {'id': '31', 'url': 'couturier'},
            # {'id': '32', 'url': 'boucher'},
            # {'id': '33', 'url': 'librairie'},
            # {'id': '34', 'url': 'architecte'},
            # {'id': '36', 'url': 'cimenterie'},
            # {'id': '37', 'url': 'chauffage'},
            # {'id': '38', 'url': 'naval'},
            # {'id': '39', 'url': 'froid'},
            {'id': '41', 'url': 'sidérurgie'},
            {'id': '42', 'url': 'industrie chimique'},
            # {'id': '43', 'url': 'gaz'}
        ]

        capitales_du_monde = [
            {'id': '1', 'nom': 'Ile-de-France'},# Paris
            {'id': '3', 'nom': 'Provence-Alpes-Côte-d%27Azur'},# Marseille
            {'id': '437', 'nom': 'Auvergne-Rhône-Alpes'},# Lyon
            {'id': '438', 'nom': 'Bourgogne-Franche-Comté'},  # Dijon
            {'id': '439', 'nom': 'Bretagne'},  # Rennes
            {'id': '440', 'nom': 'Centre-Val-de-Loire'},  # Orléans
            {'id': '441', 'nom': 'Corse'},  # Ajaccio
            {'id': '442', 'nom': 'Grand-Est'},  # Strasbourg
            {'id': '443', 'nom': 'Hauts-de-France'},  # Lille
            {'id': '444', 'nom': 'Normandie'},  # Rouen
            {'id': '445', 'nom': 'Nouvelle-Aquitaine'},  # Bordeaux
            {'id': '446', 'nom': 'Occitanie'},  # Toulouse
            {'id': '447', 'nom': 'Pays%20de%20la%20Loire'},  # Nantes
            {'id': '448', 'nom': 'Guadeloupe'},  # Basse-Terre
            {'id': '449', 'nom': 'Martinique'},  # Fort-de-France
            {'id': '450', 'nom': 'Guyane'},  # Cayenne
            {'id': '451', 'nom': 'La%20Réunion%20%28974%29'},  # Saint-Denis
            {'id': '452', 'nom': 'Mayotte'},  # Dzaoudzi
        ]

        try:
            for capitale in capitales_du_monde:
                for activite in activites:
                    try:
                        activity = activite.get("url")

                        city = capitale.get("nom")

                        numero_page = "1"

                        url_search = "https://www.pagesjaunes.fr/annuaire/chercherlespros?quoiqui=" \
                                     + activity + "&ou=" + city + "&idOu=R11&proximite=0&quoiQuiInterprete=" \
                                     + activity + "&contexte=CU31h/LZPsHhqC/oDx4Upw%3D%3D" \
                                     + "&page=" + numero_page

                        time.sleep(3)

                        html_search = requests.get(url_search)

                        soup_search = BeautifulSoup(html_search.text, 'html.parser')

                        number_of_pages = 0

                        if soup_search.select_one("#SEL-nbresultat") is not None:
                            number_of_pages_with_coma = int(soup_search
                                                            .select_one("#SEL-nbresultat")
                                                            .text
                                                            .replace(" ", "")
                                                            ) / 20

                            if int(str(number_of_pages_with_coma).split(".")[1][:1]) < 5:
                                number_of_pages += round(number_of_pages_with_coma) + 1
                                if number_of_pages > 100:
                                    number_of_pages = 100
                                    print('number_of_pages : ' + str(number_of_pages))
                                else:
                                    print('number_of_pages : ' + str(number_of_pages))

                            elif int(str(number_of_pages_with_coma).split(".")[1][:1]) >= 5:
                                number_of_pages += round(number_of_pages_with_coma)
                                if number_of_pages > 100:
                                    number_of_pages = 100
                                    print('number_of_pages : ' + str(number_of_pages))
                                else:
                                    print('number_of_pages : ' + str(number_of_pages))
                        else:
                            print("there is no results")

                        i_1 = 0

                        for i in range(1, number_of_pages + 1):
                            url_of_one_page_of_results = "https://www.pagesjaunes.fr/annuaire" \
                                                         "/chercherlespros?quoiqui=" \
                                                         + activity + "&ou=" + city \
                                                         + "&idOu=R11&proximite=0&quoiQuiInterprete=" \
                                                         + activity + "&contexte=CU31h/LZPsHhqC/oDx4Upw%3D%3D" \
                                                         + "&page=" + str(i)

                            print(url_of_one_page_of_results)

                            time.sleep(3)

                            html_of_one_page_of_results = requests.get(url_of_one_page_of_results)

                            soup_of_one_page_of_results = BeautifulSoup(html_of_one_page_of_results.content,
                                                                        'html.parser')

                            if soup_of_one_page_of_results \
                                    .select_one("#listResults") \
                                    .select("ul")[0] \
                                    .find("li", {"class": "bi-bloc"}) is not None:
                                all_li = soup_of_one_page_of_results \
                                    .select_one("#listResults") \
                                    .select("ul")[0] \
                                    .find_all("li", {"class": "bi-bloc"})

                                for i in range(0, len(all_li)):
                                    i_1 += 1

                                    try:
                                        if all_li[i].find("h3", {"class": "company-name noTrad"}) is not None:
                                            if all_li[i].find("h3", {"class": "company-name noTrad"}).select("a")[0] \
                                                    .get('href') == "#":
                                                json_bloc = json.loads(all_li[i].get('data-pjtoggleclasshisto'))

                                                bloc_id = json_bloc["idbloc"]["id_bloc"]

                                                no_sequence = json_bloc["idbloc"]["no_sequence"]

                                                json_code_rubrique = json.loads(
                                                    all_li[i]
                                                        .select("div")[0]
                                                        .get('data-pjinfosaccengage-rmk-connexefd-' + bloc_id.lower()))

                                                code_rubrique = json_code_rubrique["kAN9ProToUserInfo"]

                                                url_page = 'https://www.pagesjaunes.fr/pros/detail?bloc_id=' \
                                                           + bloc_id + \
                                                           '&no_sequence=' + no_sequence \
                                                           + '&code_rubrique=' + code_rubrique

                                                time.sleep(3)

                                                # Request the content of a page from the url
                                                html = requests.get(url_page)

                                                # Parse the content of html_doc
                                                soup = BeautifulSoup(html.content, 'html.parser')

                                                if soup \
                                                        .select_one("#teaser-footer") is not None:
                                                    if soup \
                                                            .select_one("#teaser-footer") \
                                                            .find("div",
                                                                  {'class': 'zone-coordonnees'}) is not None:
                                                        if soup \
                                                                .select_one("#teaser-footer") \
                                                                .find("div", {'class': 'zone-coordonnees'}) \
                                                                .find("div", {
                                                            'class': 'lvs-container marg-btm-s'}) is not None:
                                                            if soup \
                                                                    .select_one("#teaser-footer") \
                                                                    .find("div", {'class': 'zone-coordonnees'}) \
                                                                    .find("div", {'class': 'lvs-container marg-btm-s'}) \
                                                                    .find("a") is not None:

                                                                email_business = soup \
                                                                    .select_one("#teaser-footer") \
                                                                    .find("div", {'class': 'zone-coordonnees'}) \
                                                                    .find("div", {'class': 'lvs-container marg-btm-s'}) \
                                                                    .find("a") \
                                                                    .find("span", {"class": "value"}).text \
                                                                    .replace(" nouvelle fenêtre", "") \
                                                                    .replace("www.", "") \
                                                                    .replace("http://", "") \
                                                                    .replace("https://", "") \
                                                                    .split("/")[0] \
                                                                    .replace('/', '')

                                                                try:
                                                                    email = "contact@" + email_business

                                                                    try:
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
                                                                                        capitale.get(
                                                                                            'id'),
                                                                                        email))
                                                                                    connection.commit()
                                                                                    print(str(
                                                                                        i_1) + " The record is stored : "
                                                                                          + str(email))
                                                                                    connection.close()
                                                                                except Exception as e:
                                                                                    print(str(
                                                                                        i_1) + " The record already exists : "
                                                                                          + str(
                                                                                        email) + " " + str(
                                                                                        e))
                                                                                    connection.close()
                                                                        except Exception as e:
                                                                            print("Problem connection MySQL : "
                                                                                  + str(e))
                                                                    except Exception as e:
                                                                        print(str(i_1)
                                                                              + " An error with the email : "
                                                                              + email
                                                                              + " "
                                                                              + str(e))
                                                                except Exception as e:
                                                                    print("error validate_email 1 : " + str(e))
                                                            else:
                                                                print(str(i_1) + " a : no email business")
                                                        else:
                                                            print(str(
                                                                i_1) + " lvs-container marg-btm-s : no email business")
                                                    else:
                                                        print(str(i_1) + " zone-coordonnees : no email business")
                                                else:
                                                    print(str(i_1) + " teaser-footer : no email business")
                                            else:
                                                try:
                                                    url_page = 'https://www.pagesjaunes.fr' + all_li[i] \
                                                        .find("h3", {"class": "company-name noTrad"}) \
                                                        .select("a")[0].get('href')

                                                    time.sleep(3)

                                                    # Request the content of a page from the url
                                                    html = requests.get(url_page)

                                                    # Parse the content of html_doc
                                                    soup = BeautifulSoup(html.content, 'html.parser')

                                                    if soup \
                                                            .select_one("#teaser-footer") is not None:
                                                        if soup \
                                                                .select_one("#teaser-footer") \
                                                                .find("div", {'class': 'zone-coordonnees'}) is not None:
                                                            if soup \
                                                                    .select_one("#teaser-footer") \
                                                                    .find("div", {'class': 'zone-coordonnees'}) \
                                                                    .find('div', {
                                                                'class': 'lvs-container marg-btm-s'}) is not None:
                                                                if soup \
                                                                        .select_one("#teaser-footer") \
                                                                        .find("div", {'class': 'zone-coordonnees'}) \
                                                                        .find("div",
                                                                              {'class': 'lvs-container marg-btm-s'}) \
                                                                        .find("a") is not None:

                                                                    email_business = soup \
                                                                        .select_one("#teaser-footer") \
                                                                        .find("div", {'class': 'zone-coordonnees'}) \
                                                                        .find("div",
                                                                              {'class': 'lvs-container marg-btm-s'}) \
                                                                        .find("a") \
                                                                        .find("span", {"class": "value"}).text \
                                                                        .replace(" nouvelle fenêtre", "") \
                                                                        .replace("www.", "") \
                                                                        .replace("http://", "") \
                                                                        .replace("https://", "") \
                                                                        .split("/")[0] \
                                                                        .replace('/', '')

                                                                    try:
                                                                        email = "contact@" + email_business

                                                                        try:
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

                                                                                        cursor.execute(sql,
                                                                                                       (
                                                                                                       activite.get(
                                                                                                           'id'),
                                                                                                       capitale.get(
                                                                                                           'id'),
                                                                                                       email))

                                                                                        connection.commit()

                                                                                        print(str(i_1)
                                                                                              + " The record is stored : "
                                                                                              + str(email))
                                                                                        connection.close()
                                                                                    except Exception as e:
                                                                                        print(str(i_1)
                                                                                              + " The record already exists : "
                                                                                              + str(email)
                                                                                              + " "
                                                                                              + str(e))

                                                                                        connection.close()
                                                                            except Exception as e:
                                                                                print("Problem connection MySQL : "
                                                                                      + str(e))
                                                                        except Exception as e:
                                                                            print(str(i_1)
                                                                                  + " An error with the email : "
                                                                                  + email
                                                                                  + " " + str(e))
                                                                    except Exception as e:
                                                                        print("validate_email 2 : " + str(e))
                                                                else:
                                                                    print(str(i_1) + " a : no email business")
                                                            else:
                                                                print(str(
                                                                    i_1) + " lvs-container marg-btm-s : no email business")
                                                        else:
                                                            print(str(i_1) + " zone-coordonnees : no email business")
                                                    else:
                                                        print(str(i_1) + " teaser-footer : no email business")
                                                except Exception as e:
                                                    print(str(e))
                                        else:
                                            print(str(i_1) + " no company-name noTrad")
                                    except Exception as e:
                                        print("error 1 : " + str(e))
                            else:
                                print('sorry there is nothing')
                    except Exception as e:
                        print("error : " + str(e))
        finally:
            print('done')

    def test_extract_corporation_name_from_one_page(self):
        print("test_extract_corporation_name_from_one_page")

        try:
            url = "https://www.pagesjaunes.fr/pros/detail?bloc_id=01845539000002C0001&no_sequence=1&code_rubrique=16057200"

            # Request the content of a page from the url
            html = requests.get(url)

            # Parse the content of html_doc
            soup = BeautifulSoup(html.content, 'html.parser')

            if soup.find('div', {'class': 'denom'}) is not None:
                raison_sociale = soup.find('div', {'class': 'denom'}).text
                print("raison sociale : " + raison_sociale)
            else:
                print('nom non présent')

        except Exception as e:
            print("error url : " + str(e))

    def test_extract_corporation_address_from_one_page(self):
        print("test_extract_corporation_address_from_one_page")

        try:
            url = "https://www.pagesjaunes.fr/pros/detail?bloc_id=01845539000002C0001&no_sequence=1&code_rubrique=16057200"

            # Request the content of a page from the url
            html = requests.get(url)

            # Parse the content of html_doc
            soup = BeautifulSoup(html.content, 'html.parser')

            if soup.find('a', {'class': 'streetAddress'}) is not None:
                adresse_postale = soup.find('a', {'class': 'streetAddress'}).text
                print("adresse postale : " + adresse_postale)
            else:
                print('adresse_postale non présent')

        except Exception as e:
            print("error url : " + str(e))

    def test_extract_corporation_phone_number_from_one_page(self):
        print("test_extract_corporation_phone_number_from_one_page")

        try:
            url = "https://www.pagesjaunes.fr/pros/detail?bloc_id=01845539000002C0001&no_sequence=1&code_rubrique=16057200"

            # Request the content of a page from the url
            html = requests.get(url)

            # Parse the content of html_doc
            soup = BeautifulSoup(html.content, 'html.parser')

            if soup.find('span', {'class': 'coord-numero'}) is not None:
                phone_number = soup.find('span', {'class': 'coord-numero'}).text
                print("phone number : " + phone_number)
            else:
                print('phone_number non présent')

        except Exception as e:
            print("error url : " + str(e))

    def test_extract_corporation_website_from_one_page(self):
        print("test_extract_corporation_website_from_one_page")

        try:
            url = "https://www.pagesjaunes.fr/pros/detail?bloc_id=01845539000002C0001&no_sequence=1&code_rubrique=16057200"

            # Request the content of a page from the url
            html = requests.get(url)

            # Parse the content of html_doc
            soup = BeautifulSoup(html.content, 'html.parser')

            if soup.find('div', {'class': 'lvs-container marg-btm-s'}) \
                    .find('a') \
                    .find('span', {'class': 'value'}) is not None:
                website = soup.find('div', {'class': 'lvs-container marg-btm-s'}) \
                    .find('a') \
                    .find('span', {'class': 'value'}).text
                print("website : " + website)
            else:
                print('nom non présent')

        except Exception as e:
            print("error url : " + str(e))

    def test_extract_corporation_information_from_one_page(self):
        print("test_extract_corporation_information_from_one_page")

        try:
            url = "https://www.pagesjaunes.fr/pros/detail?bloc_id=01845539000002C0001&no_sequence=1&code_rubrique=16057200"

            # Request the content of a page from the url
            html = requests.get(url)

            # Parse the content of html_doc
            soup = BeautifulSoup(html.content, 'html.parser')

            raison_sociale = ""
            adresse_postale = ""
            phone_number = ""
            website = ""

            # raison sociale
            if soup.find('div', {'class': 'denom'}) is not None:
                raison_sociale = soup.find('div', {'class': 'denom'}).text.replace("\n", "")
            else:
                print('nom non présent')

            # adresse_postale
            if soup.find('a', {'class': 'streetAddress'}) is not None:
                adresse_postale = soup.find('a', {'class': 'streetAddress'}).text.replace("\n", "")
            else:
                print('adresse_postale non présent')

            # phone_number
            if soup.find('span', {'class': 'coord-numero'}) is not None:
                phone_number = soup.find('span', {'class': 'coord-numero'}).text.replace("\n", "")
            else:
                print('phone_number non présent')

            # website
            if soup.find('div', {'class': 'lvs-container marg-btm-s'}) \
                    .find('a') \
                    .find('span', {'class': 'value'}) is not None:
                website = soup.find('div', {'class': 'lvs-container marg-btm-s'}) \
                    .find('a') \
                    .find('span', {'class': 'value'}).text.replace("\n", "")
            else:
                print('website non présent')

            # a Python object (dict):
            x = {
                "raison_sociale": raison_sociale,
                "adresse_postale": adresse_postale,
                "phone_number": phone_number,
                "website": website
            }

            print(x.get('raison_sociale'))

        except Exception as e:
            print("error url : " + str(e))

    def test_extract_corporations_information_into_excel_file_for_all_corporations(self):
        print("test_extract_corporations_information_into_excel_file_for_all_corporations")

        corporations_list = []

        url = "https://www.pagesjaunes.fr/annuaire/chercherlespros?quoiqui=carrefour%20city&ou=Ile-de-France&proximite=0&quoiQuiInterprete=carrefour%20city&contexte=6zhlyKVZg73zvZWeqdhTPA%3D%3D&idOu=R11&page="

        try:
            numero_page = "1"

            url_search = url + numero_page

            time.sleep(3)

            html_search = requests.get(url_search)

            soup_search = BeautifulSoup(html_search.content, 'html.parser')

            number_of_pages = 0

            if soup_search.select_one("#SEL-nbresultat") is not None:
                number_of_pages_with_coma = int(soup_search
                                                .select_one("#SEL-nbresultat")
                                                .text
                                                .replace(" ", "")
                                                ) / 20

                if int(str(number_of_pages_with_coma).split(".")[1][:1]) < 5:
                    number_of_pages += round(number_of_pages_with_coma) + 1
                    if number_of_pages > 100:
                        number_of_pages = 100
                        print('number_of_pages : ' + str(number_of_pages))
                    else:
                        print('number_of_pages : ' + str(number_of_pages))

                elif int(str(number_of_pages_with_coma).split(".")[1][:1]) >= 5:
                    if int(str(number_of_pages_with_coma).split(".")[0]) == 0:
                        number_of_pages += round(number_of_pages_with_coma) + 1
                        if number_of_pages > 100:
                            number_of_pages = 100
                            print('number_of_pages : ' + str(number_of_pages))
                        else:
                            print('number_of_pages : ' + str(number_of_pages))
                    else:
                        number_of_pages += round(number_of_pages_with_coma)
                        if number_of_pages > 100:
                            number_of_pages = 100
                            print('number_of_pages : ' + str(number_of_pages))
                        else:
                            print('number_of_pages : ' + str(number_of_pages))
            else:
                print("there is no results")

            i_1 = 0

            if number_of_pages >= 1:
                for i in range(1, number_of_pages + 1):
                    try:
                        url_of_one_page_of_results = url + str(i)

                        print(url_of_one_page_of_results)

                        time.sleep(3)

                        html_of_one_page_of_results = requests.get(url_of_one_page_of_results)

                        soup_of_one_page_of_results = BeautifulSoup(html_of_one_page_of_results.content, 'html.parser')

                        if soup_of_one_page_of_results.select_one("#listResults").select("ul")[0].find("li", {
                            "class": "bi-bloc"}) is not None:
                            all_li = soup_of_one_page_of_results.select_one("#listResults").select("ul")[0].find_all(
                                "li", {"class": "bi-bloc"})

                            for i in range(0, len(all_li)):
                                i_1 += 1

                                try:
                                    if all_li[i].find("h3", {"class": "company-name noTrad"}) is not None:
                                        if all_li[i].find("h3", {"class": "company-name noTrad"}) \
                                                .select("a")[0].get('href') == "#":
                                            try:
                                                json_bloc = json.loads(
                                                    all_li[i].get('data-pjtoggleclasshisto'))

                                                bloc_id = json_bloc["idbloc"]["id_bloc"]

                                                no_sequence = json_bloc["idbloc"]["no_sequence"]

                                                json_code_rubrique = json.loads(all_li[i].select("div")[0].get(
                                                    'data-pjinfosaccengage-rmk-connexefd-' + bloc_id.lower()))

                                                code_rubrique = json_code_rubrique["kAN9ProToUserInfo"]

                                                time.sleep(3)

                                                url_page_1 = 'https://www.pagesjaunes.fr/pros/detail?bloc_id=' + bloc_id + \
                                                             '&no_sequence=' + no_sequence + '&code_rubrique=' + code_rubrique

                                                # Request the content of a page from the url
                                                html = requests.get(url_page_1)

                                                # Parse the content of html_doc
                                                soup = BeautifulSoup(html.content, 'html.parser')

                                                raison_sociale = ""
                                                adresse_postale = ""
                                                phone_number = ""
                                                website = ""
                                                email = ""

                                                try:
                                                    # raison sociale
                                                    if soup.find('div', {'class': 'denom'}) is not None:
                                                        raison_sociale = soup.find('div', {'class': 'denom'}) \
                                                            .text \
                                                            .replace("\n", "")
                                                    else:
                                                        print('raison sociale non présent')
                                                except Exception as e:
                                                    print("error url_page_1 raison sociale : " + str(e))

                                                try:
                                                    # adresse_postale
                                                    if soup.find('a', {'class': 'streetAddress'}) is not None:
                                                        adresse_postale = soup.find('a', {
                                                            'class': 'streetAddress'}).text.replace("\n", "")
                                                    else:
                                                        print('adresse_postale non présent')
                                                except Exception as e:
                                                    print("error url_page_1 adresse_postale : " + str(e))

                                                try:
                                                    # phone_number
                                                    if soup.find('span', {'class': 'coord-numero'}) is not None:
                                                        phone_number = soup.find('span',
                                                                                 {
                                                                                     'class': 'coord-numero'}).text.replace(
                                                            "\n", "")
                                                    else:
                                                        print('phone_number non présent')
                                                except Exception as e:
                                                    print("error url_page_1 phone_number : " + str(e))

                                                try:
                                                    # website
                                                    if soup.find('div', {'class': 'lvs-container marg-btm-s'}) \
                                                            .find('a') \
                                                            .find('span', {'class': 'value'}) is not None:
                                                        website = soup.find('div',
                                                                            {'class': 'lvs-container marg-btm-s'}) \
                                                            .find('a') \
                                                            .find('span', {'class': 'value'}).text.replace("\n", "")
                                                    else:
                                                        print('website non présent')
                                                except Exception as e:
                                                    print("error url_page_1 website : " + str(e))

                                                try:
                                                    # email
                                                    if soup \
                                                            .select_one("#teaser-footer") is not None:
                                                        if soup \
                                                                .select_one("#teaser-footer") \
                                                                .find("div", {'class': 'zone-coordonnees'}) is not None:
                                                            if soup \
                                                                    .select_one("#teaser-footer") \
                                                                    .find("div", {'class': 'zone-coordonnees'}) \
                                                                    .find("div",
                                                                          {
                                                                              'class': 'lvs-container marg-btm-s'}) is not None:
                                                                if soup \
                                                                        .select_one("#teaser-footer") \
                                                                        .find("div", {'class': 'zone-coordonnees'}) \
                                                                        .find("div",
                                                                              {'class': 'lvs-container marg-btm-s'}) \
                                                                        .find("a") is not None:

                                                                    email = "contact@" + soup \
                                                                        .select_one("#teaser-footer") \
                                                                        .find("div", {'class': 'zone-coordonnees'}) \
                                                                        .find("div",
                                                                              {'class': 'lvs-container marg-btm-s'}) \
                                                                        .find("a") \
                                                                        .find("span", {"class": "value"}).text \
                                                                        .replace(" nouvelle fenêtre", "") \
                                                                        .replace("www.", "") \
                                                                        .replace("http://", "") \
                                                                        .replace("https://", "") \
                                                                        .split('/')[0] \
                                                                        .replace('/', '')

                                                                else:
                                                                    print(str(i_1) + " a : no email business")
                                                            else:
                                                                print(
                                                                    str(
                                                                        i_1) + " lvs-container marg-btm-s : no email business")
                                                        else:
                                                            print(str(i_1) + " zone-coordonnees : no email business")
                                                    else:
                                                        print(str(i_1) + " teaser-footer : no email business")
                                                except Exception as e:
                                                    print("error url_page_1 email : " + str(e))

                                                # a Python object (dict):
                                                x = {
                                                    "raison_sociale": raison_sociale,
                                                    "adresse_postale": adresse_postale,
                                                    "phone_number": phone_number,
                                                    "website": website,
                                                    "email": "'" + email + "',",
                                                    "lien_page_jaune": url_page_1
                                                }

                                                print(str(i_1)
                                                      + " corporation : "
                                                      + x.get('raison_sociale')
                                                      + " ; "
                                                      + x.get('adresse_postale')
                                                      + " ; "
                                                      + x.get('phone_number')
                                                      + " ; "
                                                      + x.get('website')
                                                      + " ; "
                                                      + x.get('email'))

                                                corporations_list.append(x)
                                            except Exception as e:
                                                print("error url_page_1 : " + str(e))
                                        else:
                                            try:
                                                url_page_2 = 'https://www.pagesjaunes.fr' + all_li[i] \
                                                    .find("h3", {"class": "company-name noTrad"}) \
                                                    .select("a")[0].get('href')

                                                time.sleep(3)

                                                # Request the content of a page from the url
                                                html = requests.get(url_page_2)

                                                # Parse the content of html_doc
                                                soup = BeautifulSoup(html.content, 'html.parser')

                                                raison_sociale = ""
                                                adresse_postale = ""
                                                phone_number = ""
                                                website = ""
                                                email = ""

                                                try:
                                                    # raison sociale
                                                    if soup.find('div', {'class': 'denom'}) is not None:
                                                        raison_sociale = soup.find('div',
                                                                                   {'class': 'denom'}).text.replace(
                                                            "\n", "")
                                                    else:
                                                        print('raison sociale non présent')
                                                except Exception as e:
                                                    print("error url_page_2 raison sociale : " + str(e))

                                                try:
                                                    # adresse_postale
                                                    if soup.find('a', {'class': 'streetAddress'}) is not None:
                                                        adresse_postale = soup.find('a', {
                                                            'class': 'streetAddress'}).text.replace("\n", "")
                                                    else:
                                                        print('adresse_postale non présent')
                                                except Exception as e:
                                                    print("error url_page_2 adresse_postale : " + str(e))

                                                try:
                                                    # phone_number
                                                    if soup.find('span', {'class': 'coord-numero'}) is not None:
                                                        phone_number = soup.find('span',
                                                                                 {
                                                                                     'class': 'coord-numero'}).text.replace(
                                                            "\n", "")
                                                    else:
                                                        print('phone_number non présent')
                                                except Exception as e:
                                                    print("error url_page_2 phone_number : " + str(e))

                                                try:
                                                    # website
                                                    if soup.find('div', {'class': 'lvs-container marg-btm-s'}) \
                                                            .find('a') \
                                                            .find('span', {'class': 'value'}) is not None:
                                                        website = soup.find('div',
                                                                            {'class': 'lvs-container marg-btm-s'}) \
                                                            .find('a') \
                                                            .find('span', {'class': 'value'}).text.replace("\n", "")
                                                    else:
                                                        print('website non présent')
                                                except Exception as e:
                                                    print("error url_page_2 website : " + str(e))

                                                try:
                                                    # email
                                                    if soup \
                                                            .select_one("#teaser-footer") is not None:
                                                        if soup \
                                                                .select_one("#teaser-footer") \
                                                                .find("div", {'class': 'zone-coordonnees'}) is not None:
                                                            if soup \
                                                                    .select_one("#teaser-footer") \
                                                                    .find("div", {'class': 'zone-coordonnees'}) \
                                                                    .find("div",
                                                                          {
                                                                              'class': 'lvs-container marg-btm-s'}) is not None:
                                                                if soup \
                                                                        .select_one("#teaser-footer") \
                                                                        .find("div", {'class': 'zone-coordonnees'}) \
                                                                        .find("div",
                                                                              {'class': 'lvs-container marg-btm-s'}) \
                                                                        .find("a") is not None:

                                                                    email = "contact@" + soup \
                                                                        .select_one("#teaser-footer") \
                                                                        .find("div", {'class': 'zone-coordonnees'}) \
                                                                        .find("div",
                                                                              {'class': 'lvs-container marg-btm-s'}) \
                                                                        .find("a") \
                                                                        .find("span", {"class": "value"}).text \
                                                                        .replace(" nouvelle fenêtre", "") \
                                                                        .replace("www.", "") \
                                                                        .replace("http://", "") \
                                                                        .replace("https://", "") \
                                                                        .split('/')[0] \
                                                                        .replace('/', '')

                                                                else:
                                                                    print(str(i_1) + " a : no email business")
                                                            else:
                                                                print(
                                                                    str(
                                                                        i_1) + " lvs-container marg-btm-s : no email business")
                                                        else:
                                                            print(str(i_1) + " zone-coordonnees : no email business")
                                                    else:
                                                        print(str(i_1) + " teaser-footer : no email business")
                                                except Exception as e:
                                                    print("error url_page_2 email : " + str(e))

                                                # a Python object (dict):
                                                x = {
                                                    "raison_sociale": raison_sociale,
                                                    "adresse_postale": adresse_postale,
                                                    "phone_number": phone_number,
                                                    "website": website,
                                                    "email": "'" + email + "',",
                                                    "lien_page_jaune": url_page_2
                                                }

                                                print(str(i_1)
                                                      + " corporation : "
                                                      + x.get('raison_sociale')
                                                      + " ; "
                                                      + x.get('adresse_postale')
                                                      + " ; "
                                                      + x.get('phone_number')
                                                      + " ; "
                                                      + x.get('website')
                                                      + " ; "
                                                      + x.get('email'))

                                                corporations_list.append(x)
                                            except Exception as e:
                                                print("error url_page_2 : " + str(e))
                                    else:
                                        print(str(i_1) + " no company-name noTrad")
                                except Exception as e:
                                    print("error for all_article : " + str(e))
                        else:
                            print('sorry there is nothing')
                    except Exception as e:
                        print("error page number : " + str(i) + " : " + str(e))
            else:
                print("number of pages < 1")

            # Create a workbook and add a worksheet
            workbook = xlsxwriter.Workbook('carrefour_city__ile_de_france.xlsx')

            worksheet = workbook.add_worksheet('data')

            worksheet.write(0, 0, 'raison sociale')
            worksheet.write(0, 1, 'adresse postale')
            worksheet.write(0, 2, 'telephone')
            worksheet.write(0, 3, 'site internet')
            worksheet.write(0, 4, 'email')

            row = 1

            # Iterate over the data and write it out row by row.
            for corporation in corporations_list:
                # raison_sociale
                worksheet.write(row, 0, corporation.get('raison_sociale'))

                # adresse_postale
                worksheet.write(row, 1, corporation.get('adresse_postale'))

                # phone_number
                worksheet.write(row, 2, corporation.get('phone_number'))

                # website
                worksheet.write(row, 3, corporation.get('website'))

                # email
                worksheet.write(row, 4, corporation.get('email'))

                # lien_page_jaune
                # worksheet.write(row, 5, corporation.get('lien_page_jaune'))

                row += 1

            workbook.close()
        except Exception as e:
            print(str(e))

    def test_extract_contacts_into_excel_with_the_presence_of_chairman(self):
        print("test_extract_contacts_into_excel_with_the_presence_of_chairman")

        corporations_list = []

        url = ""

        filename = 'agence_marketing__.xlsx'

        try:
            numero_page = "1"

            url_search = url + numero_page

            html_search = requests.get(url_search)
            soup_search = BeautifulSoup(html_search.content, 'html.parser')

            number_of_pages = 0

            if soup_search.select_one("#SEL-nbresultat") is not None:
                number_of_pages_with_coma = int(soup_search
                                                .select_one("#SEL-nbresultat")
                                                .text
                                                .replace(" ", "")
                                                ) / 20

                if int(str(number_of_pages_with_coma).split(".")[1][:1]) < 5:
                    number_of_pages += round(number_of_pages_with_coma) + 1
                    if number_of_pages > 100:
                        number_of_pages = 100
                        print('number_of_pages : ' + str(number_of_pages))
                    else:
                        print('number_of_pages : ' + str(number_of_pages))

                elif int(str(number_of_pages_with_coma).split(".")[1][:1]) >= 5:
                    number_of_pages += round(number_of_pages_with_coma)
                    if number_of_pages > 100:
                        number_of_pages = 100
                        print('number_of_pages : ' + str(number_of_pages))
                    else:
                        print('number_of_pages : ' + str(number_of_pages))
            else:
                print("there is no results")

            i_1 = 0

            if number_of_pages >= 1:
                for i in range(1, number_of_pages + 1):
                    url_of_one_page_of_results = url + str(i)

                    print(url_of_one_page_of_results)

                    time.sleep(2)

                    html_of_one_page_of_results = requests.get(url_of_one_page_of_results)
                    soup_of_one_page_of_results = BeautifulSoup(html_of_one_page_of_results.content, 'html.parser')

                    if soup_of_one_page_of_results.select_one("#listResults").find("article") is not None:
                        all_article = soup_of_one_page_of_results.select("#listResults")[0].find_all('article')

                        for i in range(0, len(all_article)):
                            i_1 += 1

                            try:
                                if all_article[i].find("h2", {"class": "company-name noTrad"}) is not None:
                                    if all_article[i].find("h2", {"class": "company-name noTrad"}) \
                                            .select("a")[0].get('href') == "#":
                                        try:
                                            json_bloc = json.loads(
                                                all_article[i].get('data-pjtoggleclasshisto'))

                                            bloc_id = json_bloc["idbloc"]["id_bloc"]

                                            no_sequence = json_bloc["idbloc"]["no_sequence"]

                                            json_code_rubrique = json.loads(all_article[i].select("div")[0].get(
                                                'data-pjinfosaccengage-rmk-connexefd-' + bloc_id.lower()))

                                            code_rubrique = json_code_rubrique["kAN9ProToUserInfo"]

                                            time.sleep(2)

                                            url_page_1 = 'https://www.pagesjaunes.fr/pros/detail?bloc_id=' + bloc_id + \
                                                         '&no_sequence=' + no_sequence + '&code_rubrique=' + code_rubrique

                                            # Request the content of a page from the url
                                            html = requests.get(url_page_1)

                                            # Parse the content of html_doc
                                            soup = BeautifulSoup(html.content, 'html.parser')

                                            raison_sociale = ""
                                            adresse_postale = ""
                                            phone_number = ""
                                            website = ""
                                            email = ""
                                            presence = ""

                                            # raison sociale
                                            try:
                                                if soup.find('div', {'class': 'denom'}) is not None:
                                                    raison_sociale = soup.find('div', {'class': 'denom'}).text.replace(
                                                        "\n", "")
                                                else:
                                                    print('raison sociale non présent')
                                            except Exception as e:
                                                print("error url_page_1 raison sociale : " + str(e))

                                            # adresse_postale
                                            try:
                                                if soup.find('a', {'class': 'streetAddress'}) is not None:
                                                    adresse_postale = soup.find('a', {
                                                        'class': 'streetAddress'}).text.replace("\n", "")
                                                else:
                                                    print('adresse_postale non présent')
                                            except Exception as e:
                                                print("error url_page_1 adresse_postale : " + str(e))

                                            # phone_number
                                            try:
                                                if soup.find('span', {'class': 'coord-numero'}) is not None:
                                                    phone_number = soup.find('span',
                                                                             {'class': 'coord-numero'}).text.replace(
                                                        "\n", "")
                                                else:
                                                    print('phone_number non présent')
                                            except Exception as e:
                                                print("error url_page_1 phone_number : " + str(e))

                                            # website
                                            try:
                                                if soup.find('div', {'class': 'lvs-container marg-btm-s'}) \
                                                        .find('a') \
                                                        .find('span', {'class': 'value'}) is not None:
                                                    website = soup.find('div', {'class': 'lvs-container marg-btm-s'}) \
                                                        .find('a') \
                                                        .find('span', {'class': 'value'}).text.replace("\n", "")
                                                else:
                                                    print('website non présent')
                                            except Exception as e:
                                                print("error url_page_1 website : " + str(e))

                                            # email
                                            try:
                                                if soup \
                                                        .select_one("#teaser-footer") is not None:
                                                    if soup \
                                                            .select_one("#teaser-footer") \
                                                            .find("div", {'class': 'zone-coordonnees'}) is not None:
                                                        if soup \
                                                                .select_one("#teaser-footer") \
                                                                .find("div", {'class': 'zone-coordonnees'}) \
                                                                .find("div",
                                                                      {
                                                                          'class': 'lvs-container marg-btm-s'}) is not None:
                                                            if soup \
                                                                    .select_one("#teaser-footer") \
                                                                    .find("div", {'class': 'zone-coordonnees'}) \
                                                                    .find("div", {'class': 'lvs-container marg-btm-s'}) \
                                                                    .find("a") is not None:

                                                                email = "contact@" + soup \
                                                                    .select_one("#teaser-footer") \
                                                                    .find("div", {'class': 'zone-coordonnees'}) \
                                                                    .find("div", {'class': 'lvs-container marg-btm-s'}) \
                                                                    .find("a") \
                                                                    .get("title") \
                                                                    .replace(" nouvelle fenêtre", "") \
                                                                    .replace("www.", "") \
                                                                    .replace("http://", "") \
                                                                    .replace("https://", "") \
                                                                    .split('/')[0]

                                                            else:
                                                                print(str(i_1) + " a : no email business")
                                                        else:
                                                            print(
                                                                str(
                                                                    i_1) + " lvs-container marg-btm-s : no email business")
                                                    else:
                                                        print(str(i_1) + " zone-coordonnees : no email business")
                                                else:
                                                    print(str(i_1) + " teaser-footer : no email business")
                                            except Exception as e:
                                                print("error url_page_1 email : " + str(e))

                                            # presence of the chairman
                                            try:
                                                if soup.find("div", {"class": "dirigeants"}) is not None:
                                                    presence = "yes"
                                                else:
                                                    presence = "no"
                                            except Exception as e:
                                                print("error url_page_1 presence : " + str(e))

                                            # a Python object (dict):
                                            x = {
                                                "raison_sociale": raison_sociale,
                                                "adresse_postale": adresse_postale,
                                                "phone_number": phone_number,
                                                "website": website,
                                                "email": email,
                                                "presence": presence,
                                                "page_jaune": url_page_1
                                            }

                                            print(str(i_1)
                                                  + " corporation : " + x.get('raison_sociale')
                                                  + " ; presence of the chairman : " + x.get('presence'))

                                            corporations_list.append(x)
                                        except Exception as e:
                                            print("error url_page_1 : " + str(e))
                                    else:
                                        try:
                                            url_page_2 = 'https://www.pagesjaunes.fr' + all_article[i] \
                                                .find("h2", {"class": "company-name noTrad"}) \
                                                .select("a")[0].get('href')

                                            time.sleep(2)

                                            # Request the content of a page from the url
                                            html = requests.get(url_page_2)

                                            # Parse the content of html_doc
                                            soup = BeautifulSoup(html.content, 'html.parser')

                                            raison_sociale = ""
                                            adresse_postale = ""
                                            phone_number = ""
                                            website = ""
                                            email = ""
                                            presence = ""

                                            # raison sociale
                                            try:
                                                if soup.find('div', {'class': 'denom'}) is not None:
                                                    raison_sociale = soup.find('div', {'class': 'denom'}).text.replace(
                                                        "\n", "")
                                                else:
                                                    print('raison sociale non présent')
                                            except Exception as e:
                                                print("error url_page_2 raison sociale : " + str(e))

                                            # adresse_postale
                                            try:
                                                if soup.find('a', {'class': 'streetAddress'}) is not None:
                                                    adresse_postale = soup.find('a', {
                                                        'class': 'streetAddress'}).text.replace("\n", "")
                                                else:
                                                    print('adresse_postale non présent')
                                            except Exception as e:
                                                print("error url_page_2 adresse_postale : " + str(e))

                                            # phone_number
                                            try:
                                                if soup.find('span', {'class': 'coord-numero'}) is not None:
                                                    phone_number = soup.find('span',
                                                                             {'class': 'coord-numero'}).text.replace(
                                                        "\n", "")
                                                else:
                                                    print('phone_number non présent')
                                            except Exception as e:
                                                print("error url_page_2 phone_number : " + str(e))

                                            # website
                                            try:
                                                if soup.find('div', {'class': 'lvs-container marg-btm-s'}) \
                                                        .find('a') \
                                                        .find('span', {'class': 'value'}) is not None:
                                                    website = soup.find('div', {'class': 'lvs-container marg-btm-s'}) \
                                                        .find('a') \
                                                        .find('span', {'class': 'value'}).text.replace("\n", "")
                                                else:
                                                    print('website non présent')
                                            except Exception as e:
                                                print("error url_page_2 website : " + str(e))

                                            # email
                                            try:
                                                if soup \
                                                        .select_one("#teaser-footer") is not None:
                                                    if soup \
                                                            .select_one("#teaser-footer") \
                                                            .find("div", {'class': 'zone-coordonnees'}) is not None:
                                                        if soup \
                                                                .select_one("#teaser-footer") \
                                                                .find("div", {'class': 'zone-coordonnees'}) \
                                                                .find("div",
                                                                      {
                                                                          'class': 'lvs-container marg-btm-s'}) is not None:
                                                            if soup \
                                                                    .select_one("#teaser-footer") \
                                                                    .find("div", {'class': 'zone-coordonnees'}) \
                                                                    .find("div", {'class': 'lvs-container marg-btm-s'}) \
                                                                    .find("a") is not None:

                                                                email = "contact@" + soup \
                                                                    .select_one("#teaser-footer") \
                                                                    .find("div", {'class': 'zone-coordonnees'}) \
                                                                    .find("div", {'class': 'lvs-container marg-btm-s'}) \
                                                                    .find("a") \
                                                                    .get("title") \
                                                                    .replace(" nouvelle fenêtre", "") \
                                                                    .replace("www.", "") \
                                                                    .replace("http://", "") \
                                                                    .replace("https://", "")

                                                            else:
                                                                print(str(i_1) + " a : no email business")
                                                        else:
                                                            print(
                                                                str(
                                                                    i_1) + " lvs-container marg-btm-s : no email business")
                                                    else:
                                                        print(str(i_1) + " zone-coordonnees : no email business")
                                                else:
                                                    print(str(i_1) + " teaser-footer : no email business")
                                            except Exception as e:
                                                print("error url_page_2 email : " + str(e))

                                            # presence of the chairman
                                            try:
                                                if soup.find("div", {"class": "dirigeants"}) is not None:
                                                    presence = "yes"
                                                else:
                                                    presence = "no"
                                            except Exception as e:
                                                print("error url_page_1 presence : " + str(e))

                                            # a Python object (dict):
                                            x = {
                                                "raison_sociale": raison_sociale,
                                                "adresse_postale": adresse_postale,
                                                "phone_number": phone_number,
                                                "website": website,
                                                "email": email,
                                                "presence": presence,
                                                "page_jaune": url_page_2
                                            }

                                            print(str(i_1)
                                                  + " corporation : " + x.get('raison_sociale')
                                                  + " ; presence of the chairman : " + x.get('presence'))

                                            corporations_list.append(x)
                                        except Exception as e:
                                            print("error url_page_2 : " + str(e))
                                else:
                                    print(str(i_1) + " no company-name noTrad")
                            except Exception as e:
                                print("error for all_article : " + str(e))
                    else:
                        print('sorry there is nothing')
            else:
                print("number of pages < 1")

            # Create a workbook and add a worksheet.
            workbook = xlsxwriter.Workbook(filename)
            worksheet = workbook.add_worksheet('data')

            worksheet.write(0, 0, 'raison_sociale')
            worksheet.write(0, 1, 'adresse_postale')
            worksheet.write(0, 2, 'phone_number')
            worksheet.write(0, 3, 'website')
            worksheet.write(0, 4, 'email')
            worksheet.write(0, 5, 'presence')
            worksheet.write(0, 6, 'page_jaune')

            row = 1

            # Iterate over the data and write it out row by row.
            for corporation in corporations_list:
                # raison_sociale
                worksheet.write(row, 0, corporation.get('raison_sociale'))

                # adresse_postale
                worksheet.write(row, 1, corporation.get('adresse_postale'))

                # phone_number
                worksheet.write(row, 2, corporation.get('phone_number'))

                # website
                worksheet.write(row, 3, corporation.get('website'))

                # email
                worksheet.write(row, 4, corporation.get('email'))

                # presence
                worksheet.write(row, 5, corporation.get('presence'))

                # page jaune
                worksheet.write(row, 6, corporation.get('page_jaune'))

                row += 1

            workbook.close()

        except Exception as e:
            print(str(e))

    def test_extract_siren_of_one_company(self):
        print("test_extract_siren_of_a_company")

        try:
            url = "https://www.pagesjaunes.fr/pros/02425036"

            headers = {
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
            }

            # Request the content of a page from the url
            html = requests.get(url, headers=headers)

            # Parse the content of html_doc
            soup = BeautifulSoup(html.content, 'html.parser')

            if soup.find('dl', {'class': 'info-entreprise'}) is not None:
                siren = soup.find('dl', {'class': 'info-entreprise'}).find_all("dd")[0].text\
                    .replace('\t', '')\
                    .replace('\n', '')\
                    .replace('\r', '')

                print("siren : " + siren)
            else:
                print('siren non présent')

        except Exception as e:
            print("error url : " + str(e))

    def test_extract_activite_of_one_company(self):
        print("test_extract_activite_of_one_company")

        try:
            url = "https://www.pagesjaunes.fr/pros/detail?bloc_id=07961857000003C0001&no_sequence=1&code_rubrique=30053200"

            # Request the content of a page from the url
            html = requests.get(url)

            # Parse the content of html_doc
            soup = BeautifulSoup(html.content, 'html.parser')

            if soup.find('span', {'class': 'activite'}) is not None:
                activite = soup.find('span', {'class': 'activite'}).text

                print("activite : " + activite)
            else:
                print('activite non présent')
        except Exception as e:
            print("error url : " + str(e))

    def test_extract_contacts_into_excel_with_the_presence_of_chairman_for_all_regions(self):
        print("test_extract_contacts_into_excel_with_the_presence_of_chairman_for_all_regions")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        elements = [
            {
                'url': 'https://www.pagesjaunes.fr/annuaire/chercherlespros?quoiqui=verrerie%20industrielle&ou=Auvergne-Rh%C3%B4ne-Alpes&idOu=R84&proximite=0&quoiQuiInterprete=verrerie%20industrielle&contexte=X2%2BePT1IHwsJq0AO8Kjrxg%3D%3D&page=',
                'region': 'Auvergne-Rhône-Alpes'
            },
            {
                'url': '',
                'region': 'Bourgogne-Franche-Comté'
            },
            {
                'url': '',
                'region': 'Bretagne'
            },
            {
                'url': '',
                'region': 'Centre-Val de Loire'
            },
            {
                'url': '',
                'region': 'Corse'
            },
            {
                'url': '',
                'region': 'Grand-Est'
            },
            {
                'url': '',
                'region': 'Hauts-de-France'
            },
            {
                'url': '',
                'region': 'Ile-de-France'
            },
            {
                'url': '',
                'region': 'Normandie'
            },
            {
                'url': '',
                'region': 'Nouvelle-Aquitaine'
            },
            {
                'url': '',
                'region': 'Occitanie'
            },
            {
                'url': '',
                'region': 'Pays de la Loire'
            },
            {
                'url': '',
                'region': 'Provence-Alpes-Côte Azur'
            },
            {
                'url': '',
                'region': 'Guadeloupe'
            },
            {
                'url': '',
                'region': 'Martinique'
            },
            {
                'url': '',
                'region': 'Guyane'
            },
            {
                'url': '',
                'region': 'La Réunion'
            },
            {
                'url': '',
                'region': 'Mayotte'
            }
        ]

        corporations_list = []

        filename = "Contacts_.xlsx"

        for element in elements:
            try:
                numero_page = "1"

                url_search = element.get('url') + numero_page

                time.sleep(5)

                html_search = requests.get(url_search, headers=headers)

                soup_search = BeautifulSoup(html_search.content, 'html.parser')

                number_of_pages = 0

                if soup_search.select_one("#SEL-nbresultat") is not None:
                    print("résultats : " + str(soup_search.select_one("#SEL-nbresultat").text))

                    number_of_pages_with_coma = int(soup_search
                                                    .select_one("#SEL-nbresultat")
                                                    .text
                                                    .replace(" ", "")
                                                    ) / 20

                    print("number_of_pages_with_coma : " + str(number_of_pages_with_coma))

                    if int(str(number_of_pages_with_coma).split(".")[1][:1]) < 5:
                        number_of_pages += round(number_of_pages_with_coma) + 1
                        if number_of_pages > 100:
                            number_of_pages = 100
                            print('number_of_pages : ' + str(number_of_pages))
                        else:
                            print('number_of_pages : ' + str(number_of_pages))

                    elif int(str(number_of_pages_with_coma).split(".")[1][:1]) >= 5:
                        number_of_pages += round(number_of_pages_with_coma)
                        if number_of_pages > 100:
                            number_of_pages = 100
                            print('number_of_pages : ' + str(number_of_pages))
                        else:
                            print('number_of_pages : ' + str(number_of_pages))
                else:
                    print("there is no results")

                i_1 = 0

                if number_of_pages >= 1:
                    for i in range(1, number_of_pages + 1):
                        url_of_one_page_of_results = element.get('url') + str(i)

                        print(url_of_one_page_of_results)

                        time.sleep(5)

                        html_of_one_page_of_results = requests.get(url_of_one_page_of_results, headers=headers)

                        soup_of_one_page_of_results = BeautifulSoup(html_of_one_page_of_results.content, 'html.parser')

                        if soup_of_one_page_of_results.select_one("#listResults").find("li", {
                            "class": "bi-bloc"}) is not None:
                            all_li = soup_of_one_page_of_results.select_one("#listResults").find_all('li', {
                                "class": "bi-bloc"})

                            for i in range(0, len(all_li)):
                                i_1 += 1

                                try:
                                    if all_li[i].find("h3", {"class": "company-name noTrad"}) is not None:
                                        if all_li[i].find("h3", {"class": "company-name noTrad"}) \
                                                .select("a")[0].get('href') == "#":
                                            try:
                                                json_bloc = json.loads(
                                                    all_li[i].get('data-pjtoggleclasshisto'))

                                                bloc_id = json_bloc["idbloc"]["id_bloc"]

                                                no_sequence = json_bloc["idbloc"]["no_sequence"]

                                                json_code_rubrique = json.loads(all_li[i].select("div")[0].get(
                                                    'data-pjinfosaccengage-rmk-connexefd-' + bloc_id.lower()))

                                                code_rubrique = json_code_rubrique["kAN9ProToUserInfo"]

                                                url_page_1 = 'https://www.pagesjaunes.fr/pros/detail?bloc_id=' + bloc_id + \
                                                             '&no_sequence=' + no_sequence + '&code_rubrique=' + code_rubrique

                                                time.sleep(5)

                                                # Request the content of a page from the url
                                                html = requests.get(url_page_1, headers=headers)

                                                # Parse the content of html_doc
                                                soup = BeautifulSoup(html.content, 'html.parser')

                                                raison_sociale = ""
                                                adresse_postale = ""
                                                phone_number = ""
                                                website = ""
                                                email = ""
                                                presence = ""
                                                activite = ""

                                                # raison sociale
                                                try:
                                                    if soup.find('div', {'class': 'denom'}) is not None:
                                                        raison_sociale = soup.find('div',
                                                                                   {'class': 'denom'}).text.replace(
                                                            "\n", "")
                                                    else:
                                                        print('raison sociale non présent')
                                                except Exception as e:
                                                    print("error url_page_1 raison sociale : " + str(e))

                                                # adresse_postale
                                                try:
                                                    if soup.find('a', {'class': 'streetAddress'}) is not None:
                                                        adresse_postale = soup.find('a', {
                                                            'class': 'streetAddress'}).text.replace("\n", "")
                                                    else:
                                                        print('adresse_postale non présent')
                                                except Exception as e:
                                                    print("error url_page_1 adresse_postale : " + str(e))

                                                # phone_number
                                                try:
                                                    if soup.find('span', {'class': 'coord-numero'}) is not None:
                                                        phone_number = soup.find('span',
                                                                                 {
                                                                                     'class': 'coord-numero'}).text.replace(
                                                            "\n", "")
                                                    else:
                                                        print('phone_number non présent')
                                                except Exception as e:
                                                    print("error url_page_1 phone_number : " + str(e))

                                                # website
                                                try:
                                                    if soup.find('div', {'class': 'lvs-container marg-btm-s'}) \
                                                            .find('a') \
                                                            .find('span', {'class': 'value'}) is not None:
                                                        website = soup.find('div',
                                                                            {'class': 'lvs-container marg-btm-s'}) \
                                                            .find('a') \
                                                            .find('span', {'class': 'value'}).text.replace("\n", "")
                                                    else:
                                                        print('website non présent')
                                                        website = ''
                                                except Exception as e:
                                                    print("error url_page_1 website : " + str(e))

                                                # email
                                                try:
                                                    if soup \
                                                            .select_one("#teaser-footer") is not None:
                                                        if soup \
                                                                .select_one("#teaser-footer") \
                                                                .find("div", {'class': 'zone-coordonnees'}) is not None:
                                                            if soup \
                                                                    .select_one("#teaser-footer") \
                                                                    .find("div", {'class': 'zone-coordonnees'}) \
                                                                    .find("div",
                                                                          {
                                                                              'class': 'lvs-container marg-btm-s'}) is not None:
                                                                if soup \
                                                                        .select_one("#teaser-footer") \
                                                                        .find("div", {'class': 'zone-coordonnees'}) \
                                                                        .find("div",
                                                                              {'class': 'lvs-container marg-btm-s'}) \
                                                                        .find("a") is not None:

                                                                    email = "'contact@" + soup \
                                                                        .select_one("#teaser-footer") \
                                                                        .find("div", {'class': 'zone-coordonnees'}) \
                                                                        .find("div",
                                                                              {'class': 'lvs-container marg-btm-s'}) \
                                                                        .find("a") \
                                                                        .find("span", {"class": "value"}).text \
                                                                        .replace(" nouvelle fenêtre", "") \
                                                                        .replace("www.", "") \
                                                                        .replace("http://", "") \
                                                                        .replace("https://", "") \
                                                                        .split('/')[0] \
                                                                        .replace('/', '') + "',"

                                                                else:
                                                                    print(str(i_1) + " a : no email business")
                                                            else:
                                                                print(str(i_1)
                                                                      + " lvs-container marg-btm-s : no email business")
                                                        else:
                                                            print(str(i_1) + " zone-coordonnees : no email business")
                                                    else:
                                                        print(str(i_1) + " teaser-footer : no email business")
                                                except Exception as e:
                                                    print("error url_page_1 email : " + str(e))

                                                # presence of the chairman
                                                try:
                                                    if soup.find("div", {"class": "dirigeants"}) is not None:
                                                        presence = "yes"
                                                    else:
                                                        presence = "no"
                                                except Exception as e:
                                                    print("error url_page_1 presence : " + str(e))

                                                # activite
                                                try:
                                                    if soup.find('span', {'class': 'activite'}) is not None:
                                                        activite = soup.find('span', {'class': 'activite'}).text
                                                    else:
                                                        print('activite 1 non présent')
                                                        activite = ''
                                                except Exception as e:
                                                    print("error activite 1 : " + str(e))

                                                # a Python object (dict):
                                                x = {
                                                    "raison_sociale": raison_sociale,
                                                    "adresse_postale": adresse_postale,
                                                    "phone_number": phone_number,
                                                    "website": website,
                                                    "email": email,
                                                    "presence": presence,
                                                    "page_jaune": url_page_1,
                                                    "region": element.get('region'),
                                                    "activite": activite
                                                }

                                                print(str(i_1)
                                                      + " corporation : " + x.get('raison_sociale')
                                                      + " ; presence of the chairman : " + x.get('presence')
                                                      + " ; activite : " + x.get('activite'))

                                                corporations_list.append(x)
                                            except Exception as e:
                                                print("error url_page_1 : " + str(e))
                                        else:
                                            try:
                                                url_page_2 = 'https://www.pagesjaunes.fr' + all_li[i] \
                                                    .find("h3", {"class": "company-name noTrad"}) \
                                                    .select("a")[0].get('href')

                                                time.sleep(5)

                                                # Request the content of a page from the url
                                                html = requests.get(url_page_2, headers=headers)

                                                # Parse the content of html_doc
                                                soup = BeautifulSoup(html.content, 'html.parser')

                                                raison_sociale = ""
                                                adresse_postale = ""
                                                phone_number = ""
                                                website = ""
                                                email = ""
                                                presence = ""
                                                activite = ""

                                                # raison sociale
                                                try:
                                                    if soup.find('div', {'class': 'denom'}) is not None:
                                                        raison_sociale = soup.find('div',
                                                                                   {'class': 'denom'}).text.replace(
                                                            "\n", "")
                                                    else:
                                                        print('raison sociale non présent')
                                                except Exception as e:
                                                    print("error url_page_2 raison sociale : " + str(e))

                                                # adresse_postale
                                                try:
                                                    if soup.find('a', {'class': 'streetAddress'}) is not None:
                                                        adresse_postale = soup.find('a', {
                                                            'class': 'streetAddress'}).text.replace("\n", "")
                                                    else:
                                                        print('adresse_postale non présent')
                                                except Exception as e:
                                                    print("error url_page_2 adresse_postale : " + str(e))

                                                # phone_number
                                                try:
                                                    if soup.find('span', {'class': 'coord-numero'}) is not None:
                                                        phone_number = soup.find('span',
                                                                                 {
                                                                                     'class': 'coord-numero'}).text.replace(
                                                            "\n", "")
                                                    else:
                                                        print('phone_number non présent')
                                                except Exception as e:
                                                    print("error url_page_2 phone_number : " + str(e))

                                                # website
                                                try:
                                                    if soup.find('div', {'class': 'lvs-container marg-btm-s'}) \
                                                            .find('a') \
                                                            .find('span', {'class': 'value'}) is not None:
                                                        website = soup.find('div',
                                                                            {'class': 'lvs-container marg-btm-s'}) \
                                                            .find('a') \
                                                            .find('span', {'class': 'value'}).text.replace("\n", "")
                                                    else:
                                                        print('website non présent')
                                                        website = ''
                                                except Exception as e:
                                                    print("error url_page_2 website : " + str(e))

                                                # email
                                                try:
                                                    if soup \
                                                            .select_one("#teaser-footer") is not None:
                                                        if soup \
                                                                .select_one("#teaser-footer") \
                                                                .find("div", {'class': 'zone-coordonnees'}) is not None:
                                                            if soup \
                                                                    .select_one("#teaser-footer") \
                                                                    .find("div", {'class': 'zone-coordonnees'}) \
                                                                    .find("div",
                                                                          {
                                                                              'class': 'lvs-container marg-btm-s'}) is not None:
                                                                if soup \
                                                                        .select_one("#teaser-footer") \
                                                                        .find("div", {'class': 'zone-coordonnees'}) \
                                                                        .find("div",
                                                                              {'class': 'lvs-container marg-btm-s'}) \
                                                                        .find("a") is not None:

                                                                    email = "'contact@" + soup \
                                                                        .select_one("#teaser-footer") \
                                                                        .find("div", {'class': 'zone-coordonnees'}) \
                                                                        .find("div",
                                                                              {'class': 'lvs-container marg-btm-s'}) \
                                                                        .find("a") \
                                                                        .find("span", {"class": "value"}).text \
                                                                        .replace(" nouvelle fenêtre", "") \
                                                                        .replace("www.", "") \
                                                                        .replace("http://", "") \
                                                                        .replace("https://", "") \
                                                                        .split('/')[0] \
                                                                        .replace('/', '') + "',"

                                                                else:
                                                                    print(str(i_1) + " a : no email business")
                                                            else:
                                                                print(str(i_1)
                                                                      + " lvs-container marg-btm-s : no email business")
                                                        else:
                                                            print(str(i_1) + " zone-coordonnees : no email business")
                                                    else:
                                                        print(str(i_1) + " teaser-footer : no email business")
                                                except Exception as e:
                                                    print("error url_page_2 email : " + str(e))

                                                # presence of the chairman
                                                try:
                                                    if soup.find("div", {"class": "dirigeants"}) is not None:
                                                        presence = "yes"
                                                    else:
                                                        presence = "no"
                                                except Exception as e:
                                                    print("error url_page_2 presence : " + str(e))

                                                # activite
                                                try:
                                                    if soup.find('span', {'class': 'activite'}) is not None:
                                                        activite = soup.find('span', {'class': 'activite'}).text
                                                    else:
                                                        print('activite 2 non présent')
                                                        activite = ''
                                                except Exception as e:
                                                    print("error activite 2 : " + str(e))

                                                # a Python object (dict):
                                                x = {
                                                    "raison_sociale": raison_sociale,
                                                    "adresse_postale": adresse_postale,
                                                    "phone_number": phone_number,
                                                    "website": website,
                                                    "email": email,
                                                    "presence": presence,
                                                    "page_jaune": url_page_2,
                                                    "region": element.get('region'),
                                                    "activite": activite
                                                }

                                                print(str(i_1)
                                                      + " corporation : " + x.get('raison_sociale')
                                                      + " ; presence of the chairman : " + x.get('presence')
                                                      + " ; activite : " + x.get('activite'))

                                                corporations_list.append(x)
                                            except Exception as e:
                                                print("error url_page_2 : " + str(e))
                                    else:
                                        print(str(i_1) + " no h3 class company-name noTrad")
                                except Exception as e:
                                    print("error for all_article : " + str(e))
                        else:
                            print('sorry there is nothing')
                else:
                    print("number of pages < 1")
            except Exception as e:
                print(str(e))

        # Create a workbook and add a worksheet.
        workbook = xlsxwriter.Workbook(filename)

        worksheet = workbook.add_worksheet('France')

        worksheet.write(0, 0, 'raison_sociale')
        worksheet.write(0, 1, 'adresse_postale')
        worksheet.write(0, 2, 'phone_number')
        worksheet.write(0, 3, 'website')
        worksheet.write(0, 4, 'email')
        worksheet.write(0, 5, 'presence_chairman')
        worksheet.write(0, 6, 'page_jaune')
        worksheet.write(0, 7, 'region')
        worksheet.write(0, 8, 'activite')

        row = 1

        cell_color_orange = workbook.add_format()
        cell_color_orange.set_bg_color('orange')
        cell_color_orange.set_border(1)
        cell_color_orange.set_text_wrap()

        # Iterate over the data and write it out row by row.
        for corporation in corporations_list:
            # raison_sociale
            worksheet.write(row, 0, corporation.get('raison_sociale'), cell_color_orange)

            # adresse_postale
            worksheet.write(row, 1, corporation.get('adresse_postale'), cell_color_orange)

            # phone_number
            worksheet.write(row, 2, corporation.get('phone_number'), cell_color_orange)

            # website
            worksheet.write(row, 3, corporation.get('website'), cell_color_orange)

            # email
            worksheet.write(row, 4, corporation.get('email'), cell_color_orange)

            # presence
            worksheet.write(row, 5, corporation.get('presence'), cell_color_orange)

            # page jaune
            worksheet.write(row, 6, corporation.get('page_jaune'), cell_color_orange)

            # region
            worksheet.write(row, 7, corporation.get('region'), cell_color_orange)

            # activite
            worksheet.write(row, 8, corporation.get('activite'), cell_color_orange)

            row += 1

        workbook.close()

    def test_extract_contacts_into_excel_with_the_presence_of_chairman_for_all_regions_into_mysql(self):
        print("test_extract_contacts_into_excel_with_the_presence_of_chairman_for_all_regions")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        elements = [
            {
                'url': 'https://www.pagesjaunes.fr/annuaire/chercherlespros?quoiqui=agroalimentaire&ou=Auvergne-Rh%C3%B4ne-Alpes&proximite=0&quoiQuiInterprete=agroalimentaire&contexte=wgqzCXZLOwMqe%2BiLZ8Y1Bw%3D%3D&idOu=R84&page=',
                'region': 'Auvergne-Rhône-Alpes',
                'start': '1'
            },
            {
                'url': '',
                'region': 'Bourgogne-Franche-Comté',
                'start': '1'
            },
            {
                'url': '',
                'region': 'Bretagne',
                'start': '1'
            },
            {
                'url': '',
                'region': 'Centre-Val de Loire',
                'start': '1'
            },
            {
                'url': '',
                'region': 'Corse',
                'start': '1'
            },
            {
                'url': '',
                'region': 'Grand-Est',
                'start': '1'
            },
            {
                'url': '',
                'region': 'Hauts-de-France',
                'start': '1'
            },
            {
                'url': '',
                'region': 'Ile-de-France',
                'start': '1'
            },
            {
                'url': '',
                'region': 'Normandie',
                'start': '1'
            },
            {
                'url': '',
                'region': 'Nouvelle-Aquitaine',
                'start': '1'
            },
            {
                'url': '',
                'region': 'Occitanie',
                'start': '1'
            },
            {
                'url': '',
                'region': 'Pays de la Loire'
            },
            {
                'url': '',
                'region': 'Provence-Alpes-Côte Azur'
            },
            {
                'url': '',
                'region': 'Guadeloupe'
            },
            {
                'url': '',
                'region': 'Martinique'
            },
            {
                'url': '',
                'region': 'Guyane'
            },
            {
                'url': '',
                'region': 'La Réunion'
            },
            {
                'url': '',
                'region': 'Mayotte'
            }
        ]

        for element in elements:
            try:
                numero_page = "1"

                url_search = element.get('url') + numero_page

                time.sleep(5)

                html_search = requests.get(url_search, headers=headers)

                soup_search = BeautifulSoup(html_search.content, 'html.parser')

                number_of_pages = 0

                if soup_search.select_one("#SEL-nbresultat") is not None:
                    print("résultats : " + str(soup_search.select_one("#SEL-nbresultat").text))

                    number_of_pages_with_coma = int(soup_search
                                                    .select_one("#SEL-nbresultat")
                                                    .text
                                                    .replace(" ", "")
                                                    ) / 20

                    print("number_of_pages_with_coma : " + str(number_of_pages_with_coma))

                    if int(str(number_of_pages_with_coma).split(".")[1][:1]) < 5:
                        number_of_pages += round(number_of_pages_with_coma) + 1
                        if number_of_pages > 100:
                            number_of_pages = 100
                            print('number_of_pages : ' + str(number_of_pages))
                        else:
                            print('number_of_pages : ' + str(number_of_pages))
                    elif int(str(number_of_pages_with_coma).split(".")[1][:1]) >= 5:
                        number_of_pages += round(number_of_pages_with_coma)
                        if number_of_pages > 100:
                            number_of_pages = 100
                            print('number_of_pages : ' + str(number_of_pages))
                        else:
                            print('number_of_pages : ' + str(number_of_pages))
                else:
                    print("there is no results")

                i_1 = 0

                if number_of_pages >= 1:
                    for i in range(int(element.get('start')), number_of_pages + 1):
                        url_of_one_page_of_results = element.get('url') + str(i)

                        print(url_of_one_page_of_results)

                        time.sleep(5)

                        html_of_one_page_of_results = requests.get(url_of_one_page_of_results, headers=headers)

                        soup_of_one_page_of_results = BeautifulSoup(html_of_one_page_of_results.content, 'html.parser')

                        if soup_of_one_page_of_results.select_one("#listResults").find("li", {
                            "class": "bi-bloc"}) is not None:
                            all_li = soup_of_one_page_of_results.select_one("#listResults").find_all('li', {
                                "class": "bi-bloc"})

                            for i in range(0, len(all_li)):
                                i_1 += 1

                                try:
                                    if all_li[i].find("h3", {"class": "company-name noTrad"}) is not None:
                                        if all_li[i].find("h3", {"class": "company-name noTrad"}) \
                                                .select("a")[0].get('href') == "#":
                                            try:
                                                json_bloc = json.loads(all_li[i].get('data-pjtoggleclasshisto'))

                                                bloc_id = json_bloc["idbloc"]["id_bloc"]

                                                no_sequence = json_bloc["idbloc"]["no_sequence"]

                                                """
                                                json_code_rubrique = json.loads(all_li[i].select("div")[0].get(
                                                    'data-pjinfosaccengage-rmk-connexefd-' + bloc_id.lower()))

                                                code_rubrique = json_code_rubrique["kAN9ProToUserInfo"]                                                
                                                """

                                                url_page_1 = 'https://www.pagesjaunes.fr/pros/detail?bloc_id=' \
                                                             + bloc_id + '&no_sequence=' + no_sequence

                                                # + '&code_rubrique='  + code_rubrique

                                                time.sleep(5)

                                                html = requests.get(url_page_1, headers=headers)

                                                soup = BeautifulSoup(html.content, 'html.parser')

                                                raison_sociale = ""
                                                adresse_postale = ""
                                                phone_number = ""
                                                website = ""
                                                email = ""
                                                presence = ""
                                                activite = ""
                                                siren = ""
                                                lien_societe_com = ""
                                                president = ""

                                                # raison sociale
                                                try:
                                                    if soup.find('div', {'class': 'denom'}) is not None:
                                                        raison_sociale = soup.find('div',
                                                                                   {'class': 'denom'}).text.replace(
                                                            "\n", "")
                                                    else:
                                                        print('raison sociale non présent')
                                                except Exception as e:
                                                    print("error url_page_1 raison sociale : " + str(e))

                                                # adresse_postale
                                                try:
                                                    if soup.find('a', {'class': 'streetAddress'}) is not None:
                                                        adresse_postale = soup.find('a', {
                                                            'class': 'streetAddress'}).text.replace("\n", "")
                                                    else:
                                                        print('adresse_postale non présent')
                                                except Exception as e:
                                                    print("error url_page_1 adresse_postale : " + str(e))

                                                # phone_number
                                                try:
                                                    if soup.find('span', {'class': 'coord-numero'}) is not None:
                                                        phone_number = soup.find('span',
                                                                                 {
                                                                                     'class': 'coord-numero'}).text.replace(
                                                            "\n", "")
                                                    else:
                                                        print('phone_number non présent')
                                                except Exception as e:
                                                    print("error url_page_1 phone_number : " + str(e))

                                                # website
                                                try:
                                                    if soup.find('div', {'class': 'lvs-container marg-btm-s'}) \
                                                            .find('a') \
                                                            .find('span', {'class': 'value'}) is not None:
                                                        website = soup.find('div',
                                                                            {'class': 'lvs-container marg-btm-s'}) \
                                                            .find('a') \
                                                            .find('span', {'class': 'value'}).text.replace("\n", "")
                                                    else:
                                                        print('website non présent')
                                                        website = ''
                                                except Exception as e:
                                                    print("error url_page_1 website : " + str(e))

                                                # email
                                                try:
                                                    if soup \
                                                            .select_one("#teaser-footer") is not None:
                                                        if soup \
                                                                .select_one("#teaser-footer") \
                                                                .find("div", {'class': 'zone-coordonnees'}) is not None:
                                                            if soup \
                                                                    .select_one("#teaser-footer") \
                                                                    .find("div", {'class': 'zone-coordonnees'}) \
                                                                    .find("div",
                                                                          {
                                                                              'class': 'lvs-container marg-btm-s'}) is not None:
                                                                if soup \
                                                                        .select_one("#teaser-footer") \
                                                                        .find("div", {'class': 'zone-coordonnees'}) \
                                                                        .find("div",
                                                                              {'class': 'lvs-container marg-btm-s'}) \
                                                                        .find("a") is not None:

                                                                    email = "'contact@" + soup \
                                                                        .select_one("#teaser-footer") \
                                                                        .find("div", {'class': 'zone-coordonnees'}) \
                                                                        .find("div",
                                                                              {'class': 'lvs-container marg-btm-s'}) \
                                                                        .find("a") \
                                                                        .find("span", {"class": "value"}).text \
                                                                        .replace(" nouvelle fenêtre", "") \
                                                                        .replace("www.", "") \
                                                                        .replace("http://", "") \
                                                                        .replace("https://", "") \
                                                                        .split('/')[0] \
                                                                        .replace('/', '') + "',"

                                                                else:
                                                                    print(str(i_1) + " a : no email business")
                                                            else:
                                                                print(str(i_1)
                                                                      + " lvs-container marg-btm-s : no email business")
                                                        else:
                                                            print(str(i_1) + " zone-coordonnees : no email business")
                                                    else:
                                                        print(str(i_1) + " teaser-footer : no email business")
                                                except Exception as e:
                                                    print("error url_page_1 email : " + str(e))

                                                # presence of the chairman
                                                try:
                                                    if soup.find("div", {"class": "dirigeants"}) is not None:
                                                        presence = "yes"
                                                    else:
                                                        presence = "no"
                                                except Exception as e:
                                                    print("error url_page_1 presence : " + str(e))

                                                # activite
                                                try:
                                                    if soup.find('span', {'class': 'activite'}) is not None:
                                                        activite = soup.find('span', {'class': 'activite'}).text
                                                    else:
                                                        print('activite 1 non présent')
                                                        activite = ''
                                                except Exception as e:
                                                    print("error activite 1 : " + str(e))

                                                # siren
                                                # lien_societe_com
                                                try:
                                                    if soup.find('dl', {'class': 'info-entreprise'}) is not None:
                                                        siren = soup.find('dl', {'class': 'info-entreprise'})\
                                                            .find_all("dd")[0].text.replace('\t', '')\
                                                            .replace('\n', '')\
                                                            .replace('\r', '')

                                                        lien_societe_com = "https://www.societe.com/cgi-bin/search?champs=" + siren

                                                        # president
                                                        payload = {}

                                                        headers = {
                                                            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
                                                        }

                                                        time.sleep(10)

                                                        html_societe_com = requests.request("GET",
                                                                                lien_societe_com,
                                                                                headers=headers,
                                                                                data=payload)

                                                        soup_societe_com = BeautifulSoup(html_societe_com.content, 'html.parser')

                                                        for i_2 in range(1, 20):
                                                            if soup_societe_com.select_one("#dir" + str(i_2)) is not None:
                                                                president = soup_societe_com.select_one("#dir" + str(i_2)) \
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
                                                    else:
                                                        print('siren non présent')
                                                except Exception as e:
                                                    print("error siren : " + str(e))

                                                x = {
                                                    "raison_sociale": raison_sociale,
                                                    "adresse_postale": adresse_postale,
                                                    "phone_number": phone_number,
                                                    "website": website,
                                                    "email": email,
                                                    "presence": presence,
                                                    "page_jaune": url_page_1,
                                                    "region": element.get('region'),
                                                    "activite": activite,
                                                    "siren": siren,
                                                    "lien_societe_com": lien_societe_com,
                                                    "president": president
                                                }

                                                try:
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
                                                            sql = "INSERT INTO `contacts_pour_excel` (" \
                                                                  "`raison_sociale`, " \
                                                                  "`adresse_postale`, " \
                                                                  "`phone_number`, " \
                                                                  "`website`, " \
                                                                  "`email`, " \
                                                                  "`presence`, " \
                                                                  "`page_jaune`, " \
                                                                  "`region`, " \
                                                                  "`activite`, " \
                                                                  "`siren`, " \
                                                                  "`lien_societe_com`, " \
                                                                  "`president`) VALUE (%s, %s, %s, %s, %s, %s, %s, " \
                                                                  "%s, %s, %s, %s, %s)"

                                                            cursor.execute(sql, (
                                                                x.get('raison_sociale'),
                                                                x.get('adresse_postale'),
                                                                x.get('phone_number'),
                                                                x.get('website'),
                                                                x.get('email'),
                                                                x.get('presence'),
                                                                x.get('page_jaune'),
                                                                x.get('region'),
                                                                x.get('activite'),
                                                                x.get('siren'),
                                                                x.get('lien_societe_com'),
                                                                x.get('president')
                                                            ))

                                                            connection.commit()

                                                            print(str(i_1)
                                                                  + " corporation : " + x.get('raison_sociale')
                                                                  + " ; presence of the chairman : " + x.get('presence')
                                                                  + " ; activite : " + x.get('activite')
                                                                  + " ; siren : " + x.get('siren')
                                                                  + " ; president : " + x.get('president'))

                                                            connection.close()
                                                        except Exception as e:
                                                            print(str(i_1) + " The record already exists : " + str(e))
                                                            connection.close()
                                                except Exception as e:
                                                    print("Problem connection MySQL : " + str(e))
                                            except Exception as e:
                                                print("error url_page_1 : " + str(e))
                                        else:
                                            try:
                                                url_page_2 = 'https://www.pagesjaunes.fr' + all_li[i] \
                                                    .find("h3", {"class": "company-name noTrad"}) \
                                                    .select("a")[0].get('href')

                                                time.sleep(5)

                                                html = requests.get(url_page_2, headers=headers)

                                                soup = BeautifulSoup(html.content, 'html.parser')

                                                raison_sociale = ""
                                                adresse_postale = ""
                                                phone_number = ""
                                                website = ""
                                                email = ""
                                                presence = ""
                                                activite = ""
                                                siren = ""
                                                lien_societe_com = ""
                                                president = ""

                                                # raison sociale
                                                try:
                                                    if soup.find('div', {'class': 'denom'}) is not None:
                                                        raison_sociale = soup.find('div',
                                                                                   {'class': 'denom'}).text.replace(
                                                            "\n", "")
                                                    else:
                                                        print('raison sociale non présent')
                                                except Exception as e:
                                                    print("error url_page_2 raison sociale : " + str(e))

                                                # adresse_postale
                                                try:
                                                    if soup.find('a', {'class': 'streetAddress'}) is not None:
                                                        adresse_postale = soup.find('a', {
                                                            'class': 'streetAddress'}).text.replace("\n", "")
                                                    else:
                                                        print('adresse_postale non présent')
                                                except Exception as e:
                                                    print("error url_page_2 adresse_postale : " + str(e))

                                                # phone_number
                                                try:
                                                    if soup.find('span', {'class': 'coord-numero'}) is not None:
                                                        phone_number = soup.find('span',
                                                                                 {
                                                                                     'class': 'coord-numero'}).text.replace(
                                                            "\n", "")
                                                    else:
                                                        print('phone_number non présent')
                                                except Exception as e:
                                                    print("error url_page_2 phone_number : " + str(e))

                                                # website
                                                try:
                                                    if soup.find('div', {'class': 'lvs-container marg-btm-s'}) \
                                                            .find('a') \
                                                            .find('span', {'class': 'value'}) is not None:
                                                        website = soup.find('div',
                                                                            {'class': 'lvs-container marg-btm-s'}) \
                                                            .find('a') \
                                                            .find('span', {'class': 'value'}).text.replace("\n", "")
                                                    else:
                                                        print('website non présent')
                                                        website = ''
                                                except Exception as e:
                                                    print("error url_page_2 website : " + str(e))

                                                # email
                                                try:
                                                    if soup \
                                                            .select_one("#teaser-footer") is not None:
                                                        if soup \
                                                                .select_one("#teaser-footer") \
                                                                .find("div", {'class': 'zone-coordonnees'}) is not None:
                                                            if soup \
                                                                    .select_one("#teaser-footer") \
                                                                    .find("div", {'class': 'zone-coordonnees'}) \
                                                                    .find("div",
                                                                          {
                                                                              'class': 'lvs-container marg-btm-s'}) is not None:
                                                                if soup \
                                                                        .select_one("#teaser-footer") \
                                                                        .find("div", {'class': 'zone-coordonnees'}) \
                                                                        .find("div",
                                                                              {'class': 'lvs-container marg-btm-s'}) \
                                                                        .find("a") is not None:

                                                                    email = "'contact@" + soup \
                                                                        .select_one("#teaser-footer") \
                                                                        .find("div", {'class': 'zone-coordonnees'}) \
                                                                        .find("div",
                                                                              {'class': 'lvs-container marg-btm-s'}) \
                                                                        .find("a") \
                                                                        .find("span", {"class": "value"}).text \
                                                                        .replace(" nouvelle fenêtre", "") \
                                                                        .replace("www.", "") \
                                                                        .replace("http://", "") \
                                                                        .replace("https://", "") \
                                                                        .split('/')[0] \
                                                                        .replace('/', '') + "',"

                                                                else:
                                                                    print(str(i_1) + " a : no email business")
                                                            else:
                                                                print(str(i_1)
                                                                      + " lvs-container marg-btm-s : no email business")
                                                        else:
                                                            print(str(i_1) + " zone-coordonnees : no email business")
                                                    else:
                                                        print(str(i_1) + " teaser-footer : no email business")
                                                except Exception as e:
                                                    print("error url_page_2 email : " + str(e))

                                                # presence of the chairman
                                                try:
                                                    if soup.find("div", {"class": "dirigeants"}) is not None:
                                                        presence = "yes"
                                                    else:
                                                        presence = "no"
                                                except Exception as e:
                                                    print("error url_page_2 presence : " + str(e))

                                                # activite
                                                try:
                                                    if soup.find('span', {'class': 'activite'}) is not None:
                                                        activite = soup.find('span', {'class': 'activite'}).text
                                                    else:
                                                        print('activite 2 non présent')
                                                        activite = ''
                                                except Exception as e:
                                                    print("error activite 2 : " + str(e))

                                                # siren
                                                # lien_societe_com
                                                try:
                                                    if soup.find('dl', {'class': 'info-entreprise'}) is not None:
                                                        siren = soup.find('dl', {'class': 'info-entreprise'}) \
                                                            .find_all("dd")[0].text.replace('\t', '') \
                                                            .replace('\n', '') \
                                                            .replace('\r', '')

                                                        lien_societe_com = "https://www.societe.com/cgi-bin/search?champs=" + siren

                                                        # president
                                                        payload = {}

                                                        headers = {
                                                            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
                                                        }

                                                        time.sleep(10)

                                                        # Request the content of a page from the url
                                                        html_societe_com = requests.request("GET",
                                                                                            lien_societe_com,
                                                                                            headers=headers,
                                                                                            data=payload)

                                                        # Parse the content of html_doc
                                                        soup_societe_com = BeautifulSoup(html_societe_com.content, 'html.parser')

                                                        for i_2 in range(1, 20):
                                                            if soup_societe_com.select_one("#dir" + str(i_2)) is not None:
                                                                president = soup_societe_com.select_one("#dir" + str(i_2)) \
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
                                                    else:
                                                        print('siren non présent')
                                                except Exception as e:
                                                    print("error siren : " + str(e))

                                                # a Python object (dict):
                                                x = {
                                                    "raison_sociale": raison_sociale,
                                                    "adresse_postale": adresse_postale,
                                                    "phone_number": phone_number,
                                                    "website": website,
                                                    "email": email,
                                                    "presence": presence,
                                                    "page_jaune": url_page_2,
                                                    "region": element.get('region'),
                                                    "activite": activite,
                                                    "siren": siren,
                                                    "lien_societe_com": lien_societe_com,
                                                    "president": president
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
                                                            sql = "INSERT INTO `contacts_pour_excel` (" \
                                                                  "`raison_sociale`, " \
                                                                  "`adresse_postale`, " \
                                                                  "`phone_number`, " \
                                                                  "`website`, " \
                                                                  "`email`, " \
                                                                  "`presence`, " \
                                                                  "`page_jaune`, " \
                                                                  "`region`, " \
                                                                  "`activite`, " \
                                                                  "`siren`, " \
                                                                  "`lien_societe_com`, " \
                                                                  "`president`) VALUE (%s, %s, %s, %s, %s, %s, %s, " \
                                                                  "%s, %s, %s, %s, %s)"

                                                            cursor.execute(sql, (
                                                                x.get('raison_sociale'),
                                                                x.get('adresse_postale'),
                                                                x.get('phone_number'),
                                                                x.get('website'),
                                                                x.get('email'),
                                                                x.get('presence'),
                                                                x.get('page_jaune'),
                                                                x.get('region'),
                                                                x.get('activite'),
                                                                x.get('siren'),
                                                                x.get('lien_societe_com'),
                                                                x.get('president')
                                                            ))

                                                            connection.commit()

                                                            print(str(i_1)
                                                                  + " corporation : " + x.get('raison_sociale')
                                                                  + " ; presence of the chairman : " + x.get('presence')
                                                                  + " ; activite : " + x.get('activite')
                                                                  + " ; siren : " + x.get('siren'))

                                                            connection.close()
                                                        except Exception as e:
                                                            print(str(i_1) + " The record already exists : " + str(e))
                                                            connection.close()
                                                except Exception as e:
                                                    print("Problem connection MySQL : " + str(e))
                                            except Exception as e:
                                                print("error url_page_2 : " + str(e))
                                    else:
                                        print(str(i_1) + " no h3 class company-name noTrad")
                                except Exception as e:
                                    print("error for all_article : " + str(e))
                        else:
                            print('sorry there is nothing')
                else:
                    print("number of pages < 1")
            except Exception as e:
                print(str(e))

    def test_extract_all_corporations_for_hydrogen_in_industries(self):
        print("test_extract_all_corporations_for_hydrogen")

        filename = "Contacts_Industries_Chimiques_A_Contacter.xls"

        workbook = xlsxwriter.Workbook(filename)

        worksheet = workbook.add_worksheet('France')

        worksheet.write(0, 0, 'raison_sociale')
        worksheet.write(0, 1, 'adresse_postale')
        worksheet.write(0, 2, 'phone_number')
        worksheet.write(0, 3, 'website')
        worksheet.write(0, 4, 'email')
        worksheet.write(0, 5, 'presence')
        worksheet.write(0, 6, 'page_jaune')
        worksheet.write(0, 7, 'region')
        worksheet.write(0, 8, 'siren')
        worksheet.write(0, 9, 'email_retour_telephonique')

        location_of_the_source_file = ("Contacts_Industries_Chimiques.xls")

        wb = xlrd.open_workbook(location_of_the_source_file)

        sheet = wb.sheet_by_name("France")

        try:
            for i in range(1, 1611):
                try:
                    if sheet.cell_value(i, 3) != "":
                        try:
                            url_search = ""

                            if "http://" not in sheet.cell_value(i, 3):
                                url_search += "http://" + sheet.cell_value(i, 3)
                            else:
                                url_search += sheet.cell_value(i, 3)

                            html_search = requests.get(url_search, timeout=10)

                            print("cell " + str(i) + " - " + url_search + " request ok")

                            soup_search = BeautifulSoup(html_search.content, 'html.parser')

                            matches = [
                                "hydrogen",
                                "H2",
                                "h2",
                                "gaz",
                                "gas"
                                "hydrogène",
                                "ammonia",
                                "ammoniac",
                                "ammoniaque",
                                "ammonium",
                                "NH3",
                                "nh3",
                                "fertilisant",
                                "fertilisants",
                                "fertilizer",
                                "fertilizers",
                                "alimentaire",
                                "nourriture"
                                "food",
                                "Haber",
                                "Bosch"
                            ]

                            if any(x in str(soup_search.lower()) for x in matches):
                                # raison_sociale
                                worksheet.write(i, 0, sheet.cell_value(i, 0))

                                # adresse_postale
                                worksheet.write(i, 1, sheet.cell_value(i, 1))

                                # phone_number
                                worksheet.write(i, 2, sheet.cell_value(i, 2))

                                # website
                                worksheet.write(i, 3, sheet.cell_value(i, 3))

                                # email
                                worksheet.write(i, 4, sheet.cell_value(i, 4))

                                # presence
                                worksheet.write(i, 5, sheet.cell_value(i, 5))

                                # page jaune
                                worksheet.write(i, 6, sheet.cell_value(i, 6))

                                # region
                                worksheet.write(i, 7, sheet.cell_value(i, 7))

                                # siren
                                worksheet.write(i, 8, sheet.cell_value(i, 8))

                                # email_retour_telephonique
                                worksheet.write(i, 9, sheet.cell_value(i, 9))
                        except Exception as e:
                            print("error url_search : " + str(e))
                    else:
                        print("cell " + str(i) + " - no url")
                except Exception as e:
                    print("error sheet.cell_value(i, 3) : " + str(e))
        except Exception as e:
            print("error fo : " + str(e))

        workbook.close()

    def test_extract_all_corporations_for_mercury_in_industries(self):
        print("test_extract_all_corporations_for_mercury_in_industries")

        filename = "Contacts_Industries_Chimiques_Mercure_A_Contacter.xls"

        workbook = xlsxwriter.Workbook(filename)

        worksheet = workbook.add_worksheet('France')

        worksheet.write(0, 0, 'raison_sociale')
        worksheet.write(0, 1, 'adresse_postale')
        worksheet.write(0, 2, 'phone_number')
        worksheet.write(0, 3, 'website')
        worksheet.write(0, 4, 'email')
        worksheet.write(0, 5, 'presence')
        worksheet.write(0, 6, 'page_jaune')
        worksheet.write(0, 7, 'region')
        worksheet.write(0, 8, 'siren')
        worksheet.write(0, 9, 'email_retour_telephonique')

        location_of_the_source_file = ("Contacts_Industries_Chimiques.xls")

        wb = xlrd.open_workbook(location_of_the_source_file)

        sheet = wb.sheet_by_name("France")

        try:
            for i in range(1, 1611):
                try:
                    if sheet.cell_value(i, 3) != "":
                        try:
                            url_search = ""

                            if "http://" not in sheet.cell_value(i, 3):
                                url_search += "http://" + sheet.cell_value(i, 3)
                            else:
                                url_search += sheet.cell_value(i, 3)

                            html_search = requests.get(url_search, timeout=10)

                            print("cell " + str(i) + " - " + url_search + " request ok")

                            soup_search = BeautifulSoup(html_search.content, 'html.parser')

                            matches = [
                                "mercure",
                                "mercury",
                                "huile de paraffine"
                            ]

                            if any(x in str(soup_search.lower()) for x in matches):
                                # raison_sociale
                                worksheet.write(i, 0, sheet.cell_value(i, 0))

                                # adresse_postale
                                worksheet.write(i, 1, sheet.cell_value(i, 1))

                                # phone_number
                                worksheet.write(i, 2, sheet.cell_value(i, 2))

                                # website
                                worksheet.write(i, 3, sheet.cell_value(i, 3))

                                # email
                                worksheet.write(i, 4, sheet.cell_value(i, 4))

                                # presence
                                worksheet.write(i, 5, sheet.cell_value(i, 5))

                                # page jaune
                                worksheet.write(i, 6, sheet.cell_value(i, 6))

                                # region
                                worksheet.write(i, 7, sheet.cell_value(i, 7))

                                # siren
                                worksheet.write(i, 8, sheet.cell_value(i, 8))

                                # email_retour_telephonique
                                worksheet.write(i, 9, sheet.cell_value(i, 9))
                        except Exception as e:
                            print("error url_search : " + str(e))
                    else:
                        print("cell " + str(i) + " - no url")
                except Exception as e:
                    print("error sheet.cell_value(i, 3) : " + str(e))
        except Exception as e:
            print("error fo : " + str(e))

        workbook.close()

    def test_extract_all_coporations_for_hydrogen_in_insurances_from_one_url(self):
        print("test_extract_all_coporations_for_hydrogen_in_insurances_from_one_url")

        filename = "Contacts_Assurances_A_Contacter.xlsx"

        workbook = xlsxwriter.Workbook(filename)

        worksheet = workbook.add_worksheet('France')

        worksheet.write(0, 0, 'raison_sociale')
        worksheet.write(0, 1, 'adresse_postale')
        worksheet.write(0, 2, 'phone_number')
        worksheet.write(0, 3, 'website')
        worksheet.write(0, 4, 'email')
        worksheet.write(0, 5, 'presence')
        worksheet.write(0, 6, 'page_jaune')
        worksheet.write(0, 7, 'region')
        worksheet.write(0, 8, 'siren')
        worksheet.write(0, 9, 'activite')
        worksheet.write(0, 10, 'lien_societe_com')

        location_of_the_source_file = ("Contacts_Assurances_Ile_De_France.xlsx")

        wb = xlrd.open_workbook(location_of_the_source_file)

        sheet = wb.sheet_by_name("France")

        for i in range(1, 2001):
            time.sleep(2)

            if sheet.cell_value(i, 3) != "":
                try:
                    url_search = ""

                    if "http://" not in sheet.cell_value(i, 3):
                        url_search += "http://" + sheet.cell_value(i, 3)
                    else:
                        url_search += sheet.cell_value(i, 3)

                    print("cell " + str(i) + " - " + url_search)

                    html_search = requests.get(url_search, timeout=10)

                    soup_search = BeautifulSoup(html_search.content, 'html.parser')

                    matches = [
                        "hydrogen",
                        "H2",
                        "h2",
                        "gaz"
                        "hydrogène",
                        "industrie",
                        "entreprise",
                        "professionnel",
                        "multirisque",
                        "multi-risque",
                        "bien",
                        "usine",
                        "chimie",
                        "chimique",
                        "chimi"
                    ]

                    if any(x in soup_search for x in matches):
                        # raison_sociale
                        worksheet.write(i, 0, sheet.cell_value(i, 0))

                        # adresse_postale
                        worksheet.write(i, 1, sheet.cell_value(i, 1))

                        # phone_number
                        worksheet.write(i, 2, sheet.cell_value(i, 2))

                        # website
                        worksheet.write(i, 3, sheet.cell_value(i, 3))

                        # email
                        worksheet.write(i, 4, sheet.cell_value(i, 4))

                        # presence
                        worksheet.write(i, 5, sheet.cell_value(i, 5))

                        # page jaune
                        worksheet.write(i, 6, sheet.cell_value(i, 6))

                        # region
                        worksheet.write(i, 7, sheet.cell_value(i, 7))

                        # siren
                        worksheet.write(i, 8, sheet.cell_value(i, 8))

                        # activite
                        worksheet.write(i, 9, sheet.cell_value(i, 9))

                        # lien_societe_com
                        worksheet.write(i, 10, sheet.cell_value(i, 10))
                except Exception as e:
                    print("error url_search : " + str(e))
            else:
                print("cell " + str(i) + " - no url")

        workbook.close()

    def test_extract_big_companies_from_all_page_of_results_for_all_activities_and_capitals(self):
        """
        {'id': '1', 'url': 'agence%20interim', 'start': 71},
            {'id': '2', 'url': 'agence%20immobiliere', 'start': 1},
            {'id': '3', 'url': 'cabinet%20de%20recrutement', 'start': 1},
            {'id': '4', 'url': 'editeur%20de%20logiciel', 'start': 1},
            {'id': '5', 'url': 'hotel', 'start': 1},
            {'id': '6', 'url': 'bailleur%20social', 'start': 1},
            {'id': '7', 'url': 'entreprise%20de%20nettoyage', 'start': 1},
            {'id': '8', 'url': 'associations', 'start': 1},
            {'id': '9', 'url': 'etablissement%20financier', 'start': 1},
            {'id': '10', 'url': 'restaurant', 'start': 1},
            {'id': '11', 'url': 'entreprise%20du%20batiment', 'start': 1},
            {'id': '12', 'url': 'coiffeur', 'start': 1},
            {'id': '13', 'url': 'fleuriste', 'start': 1},
            {'id': '14', 'url': 'serrurier', 'start': 1},
            {'id': '15', 'url': 'boulangerie', 'start': 1},
            {'id': '16', 'url': 'assurance', 'start': 1},
            {'id': '17', 'url': 'pharmacie', 'start': 1},
            {'id': '18', 'url': 'entreprise%20de%20demenagement', 'start': 1},
                        {'id': '19', 'url': 'electricite', 'start': 56},
            {'id': '20', 'url': 'plomberie', 'start': 1},
            {'id': '21', 'url': 'entreprise%20de%20securite', 'start': 1},
            {'id': '22', 'url': 'avocat', 'start': 1},
        """

        activites = [
            {'id': '23', 'url': 'banque', 'start': 24},
            {'id': '24', 'url': 'garage', 'start': 1},
            {'id': '25', 'url': 'dentiste', 'start': 1},
            {'id': '26', 'url': 'docteur', 'start': 1},
            {'id': '27', 'url': 'comptable', 'start': 1},
            {'id': '28', 'url': 'supermarche', 'start': 1},
            {'id': '29', 'url': 'notaire', 'start': 1},
            {'id': '30', 'url': 'bijoutier', 'start': 1},
            {'id': '31', 'url': 'couturier', 'start': 1},
            {'id': '32', 'url': 'boucher', 'start': 1},
            {'id': '33', 'url': 'librairie', 'start': 1},
            {'id': '34', 'url': 'architecte', 'start': 1},
            {'id': '36', 'url': 'cimenterie', 'start': 1},
            {'id': '37', 'url': 'chauffage', 'start': 1},
            {'id': '38', 'url': 'naval', 'start': 1},
            {'id': '39', 'url': 'froid', 'start': 1},
            {'id': '41', 'url': 'sidérurgie', 'start': 1},
            {'id': '42', 'url': 'industrie chimique', 'start': 1},
            {'id': '43', 'url': 'gaz', 'start': 1},
            {'id': '44', 'url': 'or', 'start': 1}
        ]

        capitales_du_monde = [
            {'id': '1', 'nom': 'Ile-de-France'},# Paris
        ]

        """
                    {'id': '3', 'nom': 'Provence-Alpes-Côte-d%27Azur'},# Marseille
            {'id': '437', 'nom': 'Auvergne-Rhône-Alpes'},# Lyon
            {'id': '438', 'nom': 'Bourgogne-Franche-Comté'},  # Dijon
            {'id': '439', 'nom': 'Bretagne'},  # Rennes
            {'id': '440', 'nom': 'Centre-Val-de-Loire'},  # Orléans
            {'id': '441', 'nom': 'Corse'},  # Ajaccio
            {'id': '442', 'nom': 'Grand-Est'},  # Strasbourg
            {'id': '443', 'nom': 'Hauts-de-France'},  # Lille
            {'id': '444', 'nom': 'Normandie'},  # Rouen
            {'id': '445', 'nom': 'Nouvelle-Aquitaine'},  # Bordeaux
            {'id': '446', 'nom': 'Occitanie'},  # Toulouse
            {'id': '447', 'nom': 'Pays%20de%20la%20Loire'},  # Nantes
            {'id': '448', 'nom': 'Guadeloupe'},  # Basse-Terre
            {'id': '449', 'nom': 'Martinique'},  # Fort-de-France
            {'id': '450', 'nom': 'Guyane'},  # Cayenne
            {'id': '451', 'nom': 'La%20Réunion%20%28974%29'},  # Saint-Denis
            {'id': '452', 'nom': 'Mayotte'},  # Dzaoudzi
        """

        try:
            for capitale in capitales_du_monde:
                for activite in activites:
                    try:
                        activity = activite.get("url")

                        city = capitale.get("nom")

                        numero_page = "1"

                        url_search = "https://www.pagesjaunes.fr/annuaire/chercherlespros?quoiqui=" \
                                     + activity + "&ou=" + city + "&idOu=R11&proximite=0&quoiQuiInterprete=" \
                                     + activity + "&contexte=CU31h/LZPsHhqC/oDx4Upw%3D%3D" \
                                     + "&page=" + numero_page

                        html_search = requests.get(url_search)

                        soup_search = BeautifulSoup(html_search.text, 'html.parser')

                        number_of_pages = 0

                        if soup_search.select_one("#SEL-nbresultat") is not None:
                            number_of_pages_with_coma = int(soup_search
                                                            .select_one("#SEL-nbresultat")
                                                            .text
                                                            .replace(" ", "")
                                                            ) / 20

                            if int(str(number_of_pages_with_coma).split(".")[1][:1]) < 5:
                                number_of_pages += round(number_of_pages_with_coma) + 1
                                if number_of_pages > 100:
                                    number_of_pages = 100
                                    print('number_of_pages : ' + str(number_of_pages))
                                else:
                                    print('number_of_pages : ' + str(number_of_pages))

                            elif int(str(number_of_pages_with_coma).split(".")[1][:1]) >= 5:
                                number_of_pages += round(number_of_pages_with_coma)
                                if number_of_pages > 100:
                                    number_of_pages = 100
                                    print('number_of_pages : ' + str(number_of_pages))
                                else:
                                    print('number_of_pages : ' + str(number_of_pages))
                        else:
                            print("there is no results")

                        i_1 = 0

                        for i in range(activite.get('start'), number_of_pages + 1):
                            url_of_one_page_of_results = "https://www.pagesjaunes.fr/annuaire" \
                                                         "/chercherlespros?quoiqui=" \
                                                         + activity + "&ou=" + city \
                                                         + "&idOu=R11&proximite=0&quoiQuiInterprete=" \
                                                         + activity + "&contexte=CU31h/LZPsHhqC/oDx4Upw%3D%3D" \
                                                         + "&page=" + str(i)

                            print(url_of_one_page_of_results)

                            html_of_one_page_of_results = requests.get(url_of_one_page_of_results)

                            soup_of_one_page_of_results = BeautifulSoup(html_of_one_page_of_results.content,
                                                                        'html.parser')

                            if soup_of_one_page_of_results \
                                    .select_one("#listResults") \
                                    .select("ul")[0] \
                                    .find("li", {"class": "bi-bloc"}) is not None:
                                all_li = soup_of_one_page_of_results \
                                    .select_one("#listResults") \
                                    .select("ul")[0] \
                                    .find_all("li", {"class": "bi-bloc"})

                                for i in range(0, len(all_li)):
                                    i_1 += 1

                                    try:
                                        if all_li[i].find("h3", {"class": "company-name noTrad"}) is not None:
                                            if all_li[i].find("h3", {"class": "company-name noTrad"}).select("a")[0] \
                                                    .get('href') == "#":
                                                json_bloc = json.loads(all_li[i].get('data-pjtoggleclasshisto'))

                                                bloc_id = json_bloc["idbloc"]["id_bloc"]

                                                no_sequence = json_bloc["idbloc"]["no_sequence"]

                                                json_code_rubrique = json.loads(
                                                    all_li[i]
                                                        .select("div")[0]
                                                        .get('data-pjinfosaccengage-rmk-connexefd-' + bloc_id.lower()))

                                                code_rubrique = json_code_rubrique["kAN9ProToUserInfo"]

                                                url_page = 'https://www.pagesjaunes.fr/pros/detail?bloc_id=' \
                                                           + bloc_id + \
                                                           '&no_sequence=' + no_sequence \
                                                           + '&code_rubrique=' + code_rubrique

                                                time.sleep(2)

                                                # Request the content of a page from the url
                                                html = requests.get(url_page)

                                                # Parse the content of html_doc
                                                soup = BeautifulSoup(html.content, 'html.parser')

                                                # telephone
                                                telephone = ""
                                                try:
                                                    if soup.find('span', {'class': 'coord-numero'}) is not None:
                                                        telephone += soup.find('span',
                                                                               {
                                                                                   'class': 'coord-numero'}).text.replace(
                                                            "\n", "")
                                                    else:
                                                        print('phone_number non présent')
                                                except Exception as e:
                                                    print("error url_page_1 phone_number : " + str(e))

                                                # siren
                                                try:
                                                    if soup.find('dl', {'class': 'info-entreprise'}) is not None:
                                                        siren = soup.find('dl', {'class': 'info-entreprise'})\
                                                            .find_all("dd")[0].text.replace('\t', '')\
                                                            .replace('\n', '')\
                                                            .replace('\r', '')

                                                        raison_sociale = ""
                                                        adresse_postale = ""
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
                                                                soup.select_one(
                                                                    "#trancheeff-histo-description") is not None:
                                                            # tranche_effectif
                                                            tranche_effectif += soup.select_one(
                                                                "#trancheeff-histo-description") \
                                                                .text \
                                                                .replace('  ', '') \
                                                                .replace('\n', '') \
                                                                .replace('\t', '') \
                                                                .replace('\r', '')

                                                            # capital_social
                                                            capital_social += int(
                                                                soup.select_one("#capital-histo-description") \
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
                                                                    'president': president,
                                                                    'telephone': telephone
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
                                                                                  "`president`, " \
                                                                                  "`telephone`) VALUE (%s, %s, %s, %s, %s, %s, %s, %s)"

                                                                            cursor.execute(sql, (
                                                                                x.get('raison_sociale'),
                                                                                x.get('adresse_postale'),
                                                                                x.get('siren'),
                                                                                x.get('activite'),
                                                                                x.get('capital_social'),
                                                                                x.get('tranche_effectif'),
                                                                                x.get('president'),
                                                                                x.get('telephone')
                                                                            ))

                                                                            connection.commit()

                                                                            print(str(i_1) + ' siren ' + x.get(
                                                                                'siren') + ' : big company')

                                                                            connection.close()
                                                                        except Exception as e:
                                                                            print(str(i_1) +
                                                                                " The record already exists (siren : " + siren
                                                                                + ") : " + str(e))
                                                                            connection.close()
                                                                except Exception as e:
                                                                    print(str(i_1) + " Problem connection MySQL (siren : " + siren
                                                                          + ") : " + str(e))
                                                            else:
                                                                print(str(i_1) + ' siren ' + siren + ' : no big company')
                                                        else:
                                                            print(str(i_1) + ' siren ' + siren + ' : no information')
                                                    else:
                                                        print(str(i_1) + ' siren non présent')
                                                except Exception as e:
                                                    print(str(i_1) + " error siren : " + str(e))
                                            else:
                                                try:
                                                    url_page = 'https://www.pagesjaunes.fr' + all_li[i] \
                                                        .find("h3", {"class": "company-name noTrad"}) \
                                                        .select("a")[0].get('href')

                                                    time.sleep(2)

                                                    # Request the content of a page from the url
                                                    html = requests.get(url_page)

                                                    # Parse the content of html_doc
                                                    soup = BeautifulSoup(html.content, 'html.parser')

                                                    # telephone
                                                    telephone = ""
                                                    try:
                                                        if soup.find('span', {'class': 'coord-numero'}) is not None:
                                                            telephone += soup.find('span',
                                                                                     {
                                                                                         'class': 'coord-numero'}).text.replace(
                                                                "\n", "")
                                                        else:
                                                            print('phone_number non présent')
                                                    except Exception as e:
                                                        print("error url_page_1 phone_number : " + str(e))

                                                    # siren
                                                    try:
                                                        if soup.find('dl', {'class': 'info-entreprise'}) is not None:
                                                            siren = soup.find('dl', {'class': 'info-entreprise'}) \
                                                                .find_all("dd")[0].text.replace('\t', '') \
                                                                .replace('\n', '') \
                                                                .replace('\r', '')

                                                            raison_sociale = ""
                                                            adresse_postale = ""
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
                                                            html = requests.request("GET", url, headers=headers,
                                                                                    data=payload)

                                                            # Parse the content of html_doc
                                                            soup = BeautifulSoup(html.content, 'html.parser')

                                                            if soup.select_one("#capital-histo-description") is not None \
                                                                    and \
                                                                    soup.select_one(
                                                                        "#trancheeff-histo-description") is not None:
                                                                # tranche_effectif
                                                                tranche_effectif += soup.select_one(
                                                                    "#trancheeff-histo-description") \
                                                                    .text \
                                                                    .replace('  ', '') \
                                                                    .replace('\n', '') \
                                                                    .replace('\t', '') \
                                                                    .replace('\r', '')

                                                                # capital_social
                                                                capital_social += int(
                                                                    soup.select_one("#capital-histo-description") \
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
                                                                    if soup.select_one(
                                                                            "#ape-histo-description") is not None:
                                                                        activite += soup.select_one(
                                                                            "#ape-histo-description") \
                                                                            .text \
                                                                            .replace('  ', '') \
                                                                            .replace('\n', '') \
                                                                            .replace('\t', '') \
                                                                            .replace('\r', '')

                                                                    # president
                                                                    for i in range(1, 20):
                                                                        if soup.select_one("#dir" + str(i)) is not None:
                                                                            president += \
                                                                            soup.select_one("#dir" + str(i)) \
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
                                                                        'president': president,
                                                                        'telephone': telephone
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
                                                                                      "`president`, " \
                                                                                      "`telephone`) VALUE (%s, %s, %s, %s, %s, %s, %s, %s)"

                                                                                cursor.execute(sql, (
                                                                                    x.get('raison_sociale'),
                                                                                    x.get('adresse_postale'),
                                                                                    x.get('siren'),
                                                                                    x.get('activite'),
                                                                                    x.get('capital_social'),
                                                                                    x.get('tranche_effectif'),
                                                                                    x.get('president'),
                                                                                    x.get('telephone')
                                                                                ))

                                                                                connection.commit()

                                                                                print(str(i_1) + ' siren ' + x.get(
                                                                                    'siren') + ' : big company')

                                                                                connection.close()
                                                                            except Exception as e:
                                                                                print(str(i_1) +
                                                                                      " The record already exists (siren : " + siren
                                                                                      + ") : " + str(e))
                                                                                connection.close()
                                                                    except Exception as e:
                                                                        print(str(
                                                                            i_1) + " Problem connection MySQL (siren : " + siren
                                                                              + ") : " + str(e))
                                                                else:
                                                                    print(str(
                                                                        i_1) + ' siren ' + siren + ' : no big company')
                                                            else:
                                                                print(
                                                                    str(i_1) + ' siren ' + siren + ' : no information')
                                                        else:
                                                            print(str(i_1) + ' siren non présent')
                                                    except Exception as e:
                                                        print(str(i_1) + " error siren : " + str(e))
                                                except Exception as e:
                                                    print(str(i_1) + " error url_page 2 : " + str(e))
                                        else:
                                            print(str(i_1) + " no company-name noTrad")
                                    except Exception as e:
                                        print(str(i_1) + " error 1 : " + str(e))
                            else:
                                print('sorry there is nothing')
                    except Exception as e:
                        print("error : " + str(e))
        finally:
            print('done')


class UnitTestsDataMiningYellowPagesFranceWithRpaWithoutHeadless(unittest.TestCase):
    # ok
    def test_open_one_page_without_headless(self):
        print('test_open_one_page_without_headless')

        time.sleep(5)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(5)

        # with Firefox
        browser = webdriver.Firefox(executable_path='..\\..\\..\\geckodriver.exe')

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get('https://www.pagesjaunes.fr/pros/detail?bloc_id=FCP06923089CLIENTDA3000004C0001&no_sequence=1&code_rubrique=16053100')

        time.sleep(15)

    # ok
    def test_extract_the_website_from_one_page_without_headless(self):
        print('test_extract_the_website_from_one_page_without_headless')

        time.sleep(5)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(5)

        # with Firefox
        browser = webdriver.Firefox(executable_path='..\\..\\..\\geckodriver.exe')

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get('https://www.pagesjaunes.fr/pros/detail?bloc_id=FCP06923089CLIENTDA3000004C0001&no_sequence=1&code_rubrique=16053100')

        time.sleep(15)

        # Click on the "Continuer sans accepter" button
        continuer_sans_accepter_button = browser.find_element_by_xpath(
            "/html/body/div[1]/div/div/div/div/div/span"
        )
        continuer_sans_accepter_button.click()
        print('continuer_sans_accepter_button clicked')

        time.sleep(10)

        # Print the website
        try:
            website_text = browser.find_element_by_xpath(
                "/html/body/main/div[2]/section/div[6]/div[1]/div[2]/div/div/div[4]/a"
            ).text
            print('website_text : ' + str(website_text))
        except Exception as e:
            print("error website : " + str(e))

        time.sleep(5)

        browser.quit()

    # ok
    def test_extract_the_email_from_one_page_without_headless(self):
        print('test_extract_the_email_from_one_page_without_headless')

        time.sleep(5)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(5)

        # with Firefox
        browser = webdriver.Firefox(executable_path='..\\..\\..\\geckodriver.exe')

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get('https://www.pagesjaunes.fr/pros/detail?bloc_id=FCP06923089CLIENTDA3000004C0001&no_sequence=1&code_rubrique=16053100')

        time.sleep(15)

        # Click on the "Continuer sans accepter" button
        continuer_sans_accepter_button = browser.find_element_by_xpath(
            "/html/body/div[1]/div/div/div/div/div/span"
        )
        continuer_sans_accepter_button.click()
        print('continuer_sans_accepter_button clicked')

        time.sleep(10)

        # Print the email
        try:
            email_text = "'contact@" + browser.find_element_by_xpath(
                "/html/body/main/div[2]/section/div[6]/div[1]/div[2]/div/div/div[4]/a"
            ).text\
                .replace("https://www.", "")\
                .replace("http://www.", "")\
                .replace("https://", "")\
                .replace("http://", "") + "',"
            print('email_text : ' + str(email_text))
        except Exception as e:
            print("error email_text : " + str(e))

        time.sleep(5)

        browser.quit()

    # ok
    def test_extract_corporation_name_from_one_page_without_headless(self):
        print("test_extract_corporation_name_from_one_page_without_headless")

        try:
            time.sleep(5)

            warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

            time.sleep(5)

            # with Firefox
            browser = webdriver.Firefox(executable_path='..\\..\\..\\geckodriver.exe')

            time.sleep(5)

            # maximize window
            browser.maximize_window()

            time.sleep(5)

            # open
            browser.get('https://www.pagesjaunes.fr/pros/detail?bloc_id=FCP06923089CLIENTDA3000004C0001&no_sequence=1&code_rubrique=16053100')

            time.sleep(15)

            # Click on the "Continuer sans accepter" button
            continuer_sans_accepter_button = browser.find_element_by_xpath(
                "/html/body/div[1]/div/div/div/div/div/span"
            )
            continuer_sans_accepter_button.click()
            print('continuer_sans_accepter_button clicked')

            time.sleep(10)

            # Print the corporation_name
            try:
                corporation_name_text = browser.find_element_by_xpath(
                    "/html/body/main/div[2]/section/div[2]/div[1]/div[1]/div/div[1]/h1"
                ).text
                print('corporation_name_text : ' + str(corporation_name_text))
            except Exception as e:
                print("error corporation_name_text : " + str(e))

            time.sleep(5)

            browser.quit()
        except Exception as e:
            print("error url : " + str(e))

    # ok
    def test_extract_corporation_address_from_one_page_without_headless(self):
        print("test_extract_corporation_address_from_one_page_without_headless")

        try:
            time.sleep(5)

            warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

            time.sleep(5)

            # with Firefox
            browser = webdriver.Firefox(executable_path='..\\..\\..\\geckodriver.exe')

            time.sleep(5)

            # maximize window
            browser.maximize_window()

            time.sleep(5)

            # open
            browser.get('https://www.pagesjaunes.fr/pros/detail?bloc_id=FCP06923089CLIENTDA3000004C0001&no_sequence=1&code_rubrique=16053100')

            time.sleep(15)

            # Click on the "Continuer sans accepter" button
            continuer_sans_accepter_button = browser.find_element_by_xpath(
                "/html/body/div[1]/div/div/div/div/div/span"
            )
            continuer_sans_accepter_button.click()
            print('continuer_sans_accepter_button clicked')

            time.sleep(10)

            try:
                # Print the corporation_address
                corporation_address_text = browser.find_element_by_xpath(
                    "/html/body/main/div[2]/section/div[6]/div[1]/div[2]/div/div/div[2]/a[1]"
                ).text
                print('corporation_address_text : ' + str(corporation_address_text))
            except Exception as e:
                print("error corporation_address_text : " + str(e))

            time.sleep(5)

            browser.quit()
        except Exception as e:
            print("error url : " + str(e))

    # ok
    def test_extract_corporation_phone_number_from_one_page_without_headless(self):
        print("test_extract_corporation_phone_number_from_one_page_without_headless")

        try:
            time.sleep(5)

            warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

            time.sleep(5)

            # with Firefox
            browser = webdriver.Firefox(executable_path='..\\..\\..\\geckodriver.exe')

            time.sleep(5)

            # maximize window
            browser.maximize_window()

            time.sleep(5)

            # open
            browser.get('https://www.pagesjaunes.fr/pros/detail?bloc_id=FCP06923089CLIENTDA3000004C0001&no_sequence=1&code_rubrique=16053100')

            time.sleep(15)

            # Click on the "Continuer sans accepter" button
            continuer_sans_accepter_button = browser.find_element_by_xpath(
                "/html/body/div[1]/div/div/div/div/div/span"
            )
            continuer_sans_accepter_button.click()
            print('continuer_sans_accepter_button clicked')

            time.sleep(10)

            # Print the corporation_phone_number
            try:
                corporation_phone_number_text = browser.find_element_by_xpath(
                    "/html/body/main/div[2]/section/div[6]/div[1]/div[2]/div/div/div[1]/div/span/span[2]"
                ).text
                print('corporation_phone_number_text : ' + str(corporation_phone_number_text))
            except Exception as e:
                print('error corporation_phone_number_text : ' + str(e))

            time.sleep(5)

            browser.quit()
        except Exception as e:
            print("error url : " + str(e))

    # ok
    def test_extract_siren_from_one_page_without_headless(self):
        print("test_extract_siren_from_one_page_without_headless")

        try:
            time.sleep(5)

            warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

            time.sleep(5)

            # with Firefox
            browser = webdriver.Firefox(executable_path='..\\..\\..\\geckodriver.exe')

            time.sleep(5)

            # maximize window
            browser.maximize_window()

            time.sleep(5)

            # open
            browser.get('https://www.pagesjaunes.fr/pros/detail?bloc_id=FCP06923089CLIENTDA3000004C0001&no_sequence=1&code_rubrique=16053100')

            time.sleep(15)

            # Click on the "Continuer sans accepter" button
            continuer_sans_accepter_button = browser.find_element_by_xpath(
                "/html/body/div[1]/div/div/div/div/div/span"
            )
            continuer_sans_accepter_button.click()
            print('continuer_sans_accepter_button clicked')

            time.sleep(10)

            try:
                # Click on the "Informations financières et juridiques" button
                informations_financieres_juridiques_button = browser.find_element_by_xpath(
                    "/html/body/main/div[2]/section/div[6]/div[1]/div[12]/h2/button"
                )
                informations_financieres_juridiques_button.click()

                time.sleep(10)

                # Print the siren
                siren_text = browser.find_element_by_xpath(
                    "/html/body/main/div[2]/section/div[6]/div[1]/div[12]/div/dl[2]/dd[1]/strong"
                ).text
                print('siren_text : ' + str(siren_text))
            except Exception as e:
                print('error siren_text : ' + str(e))

            time.sleep(5)

            browser.quit()
        except Exception as e:
            print("error url : " + str(e))

    # ok
    def test_extract_activite_from_one_page_without_headless(self):
        print("test_extract_activite_from_one_page_without_headless")

        try:
            time.sleep(5)

            warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

            time.sleep(5)

            # with Firefox
            browser = webdriver.Firefox(executable_path='..\\..\\..\\geckodriver.exe')

            time.sleep(5)

            # maximize window
            browser.maximize_window()

            time.sleep(5)

            # open
            browser.get('https://www.pagesjaunes.fr/pros/detail?bloc_id=FCP06923089CLIENTDA3000004C0001&no_sequence=1&code_rubrique=16053100')

            time.sleep(15)

            # Click on the "Continuer sans accepter" button
            continuer_sans_accepter_button = browser.find_element_by_xpath(
                "/html/body/div[1]/div/div/div/div/div/span"
            )
            continuer_sans_accepter_button.click()
            print('continuer_sans_accepter_button clicked')

            time.sleep(10)

            try:
                # Print the activite_text
                activite_text = browser.find_element_by_xpath(
                    "/html/body/main/div[2]/section/div[2]/div[1]/div[1]/div/div[2]/div"
                ).text
                print('activite_text : ' + str(activite_text))
            except Exception as e:
                print('error activite_text : ' + str(e))

            time.sleep(5)

            browser.quit()
        except Exception as e:
            print("error url : " + str(e))

    # ok
    def test_extract_the_president_of_one_company_from_one_page_without_headless(self):
        print("test_extract_the_president_of_one_company_from_one_page_without_headless")

        siren = ""

        try:
            time.sleep(5)

            warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

            time.sleep(5)

            # with Firefox
            browser = webdriver.Firefox(executable_path='..\\..\\..\\geckodriver.exe')

            time.sleep(5)

            # maximize window
            browser.maximize_window()

            time.sleep(5)

            # open
            browser.get('https://www.pagesjaunes.fr/pros/detail?bloc_id=FCP06923089CLIENTDA3000004C0001&no_sequence=1&code_rubrique=16053100')

            time.sleep(15)

            # Click on the "Continuer sans accepter" button
            continuer_sans_accepter_button = browser.find_element_by_xpath(
                "/html/body/div[1]/div/div/div/div/div/span"
            )
            continuer_sans_accepter_button.click()
            print('continuer_sans_accepter_button clicked')

            time.sleep(10)

            try:
                # Click on the "Informations financières et juridiques" button
                informations_financieres_juridiques_button = browser.find_element_by_xpath(
                    "/html/body/main/div[2]/section/div[6]/div[1]/div[12]/h2/button"
                )
                informations_financieres_juridiques_button.click()

                time.sleep(10)

                # Print the siren
                siren += browser.find_element_by_xpath(
                    "/html/body/main/div[2]/section/div[6]/div[1]/div[12]/div/dl[2]/dd[1]/strong"
                ).text
                print('siren : ' + str(siren))

                if siren == '':
                    url = "https://www.societe.com/cgi-bin/search?champs=" + siren

                    payload = {}

                    headers = {
                        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
                    }

                    # Request the content of a page from the url
                    html = requests.request("GET", url, headers=headers, data=payload)

                    # Parse the content of html_doc
                    soup = BeautifulSoup(html.content, 'html.parser')

                    for i in range(1, 20):
                        if soup.select_one("#dir" + str(i)) is not None:
                            president = soup.select_one("#dir" + str(i)) \
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
            except Exception as e:
                print('error siren : ' + str(e))

            time.sleep(5)

            browser.quit()
        except Exception as e:
            print("error url : " + str(e))

    # ok
    def test_extract_all_url_company_for_one_page_of_companies_for_one_activity_and_one_capital_without_headless(self):
        print("test_extract_all_url_company_for_one_page_of_companies_for_one_activity_and_one_capital_without_headless")

        try:
            url_of_one_page_of_companies = "https://www.pagesjaunes.fr/annuaire/chercherlespros?quoiqui=engrais" \
                                           "&ou=Ile-de-France&idOu=R11&proximite=0&quoiQuiInterprete=engrais" \
                                           "&contexte=RAW9Pw1FgkFLRnXqiDngwQ%3D%3D&page=2"

            urls_company = []

            time.sleep(5)

            warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

            time.sleep(5)

            # with Firefox
            browser = webdriver.Firefox(executable_path='..\\..\\..\\geckodriver.exe')

            time.sleep(5)

            # maximize window
            browser.maximize_window()

            time.sleep(5)

            # open
            browser.get(url_of_one_page_of_companies)

            time.sleep(15)

            # Click on the "Continuer sans accepter" button
            continuer_sans_accepter_button = browser.find_element_by_xpath(
                "/html/body/div[1]/div/div/div/div/div/span"
            )
            continuer_sans_accepter_button.click()
            print('continuer_sans_accepter_button clicked')

            time.sleep(10)

            try:
                # Print all url_company
                i_1 = 0

                all_li = browser.find_elements_by_class_name('bi-bloc')

                for i in range(0, len(all_li)):
                    try:
                        if all_li[i].find_element_by_class_name("company-name") is not None:
                            if all_li[i].find_element_by_class_name("company-name").find_elements_by_tag_name("a")[0].get_attribute('href') == "#":
                                try:
                                    json_bloc = json.loads(all_li[i].get('data-pjtoggleclasshisto'))

                                    bloc_id = json_bloc["idbloc"]["id_bloc"]

                                    no_sequence = json_bloc["idbloc"]["no_sequence"]

                                    json_code_rubrique = json.loads(all_li[i].select("div")[0].get(
                                        'data-pjinfosaccengage-rmk-connexefd-' + bloc_id.lower()))

                                    code_rubrique = json_code_rubrique["kAN9ProToUserInfo"]

                                    url_page_1 = 'https://www.pagesjaunes.fr/pros/detail?bloc_id=' + bloc_id + \
                                                 '&no_sequence=' + no_sequence + '&code_rubrique=' + code_rubrique

                                    urls_company.append(url_page_1)
                                except Exception as e:
                                    print('error url_page_1 : ' + str(e))
                            else:
                                try:
                                    url_page_2 = all_li[i].find_element_by_class_name("company-name").find_elements_by_tag_name("a")[0].get_attribute('href')

                                    urls_company.append(url_page_2)
                                except Exception as e:
                                    print("error url_page_2 : " + str(e))
                        else:
                            print(str(i_1) + " no h3 class company-name noTrad")
                    except Exception as e:
                        print(str(i_1) + " error 1 : " + str(e))

                    i_1 += 1
            except Exception as e:
                print('error url_company : ' + str(e))

            time.sleep(5)

            browser.quit()

            for url_company in urls_company:
                print('company : ' + str(url_company))
        except Exception as e:
            print("error url : " + str(e))

    # ok
    def test_print_the_number_of_pages_for_one_activity_and_one_capital_without_headless(self):
        print("test_print_the_number_of_pages_for_one_activity_and_one_capital_without_headless")

        number_of_pages = 0

        url_of_one_page_of_companies = "https://www.pagesjaunes.fr/annuaire/chercherlespros?quoiqui=engrais" \
                                       "&ou=Ile-de-France&idOu=R11&proximite=0&quoiQuiInterprete=engrais" \
                                       "&contexte=RAW9Pw1FgkFLRnXqiDngwQ%3D%3D&page=2"

        time.sleep(5)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(5)

        # with Firefox
        browser = webdriver.Firefox(executable_path='..\\..\\..\\geckodriver.exe')

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get(url_of_one_page_of_companies)

        time.sleep(15)

        # Click on the "Continuer sans accepter" button
        continuer_sans_accepter_button = browser.find_element_by_xpath(
            "/html/body/div[1]/div/div/div/div/div/span"
        )
        continuer_sans_accepter_button.click()
        print('continuer_sans_accepter_button clicked')

        time.sleep(10)

        if browser.find_element_by_id("SEL-nbresultat") is not None:
            number_of_pages_with_coma = int(browser.find_element_by_id("SEL-nbresultat")
                                            .text
                                            .replace(" ", "")
                                            ) / 20

            if int(str(number_of_pages_with_coma).split(".")[1][:1]) < 5:
                number_of_pages += round(number_of_pages_with_coma) + 1
                if number_of_pages > 100:
                    number_of_pages = 100
                    print('number_of_pages : ' + str(number_of_pages))
                else:
                    print('number_of_pages : ' + str(number_of_pages))

            elif int(str(number_of_pages_with_coma).split(".")[1][:1]) >= 5:
                if int(str(number_of_pages_with_coma).split(".")[0]) == 0:
                    number_of_pages += round(number_of_pages_with_coma) + 1
                    if number_of_pages > 100:
                        number_of_pages = 100
                        print('number_of_pages : ' + str(number_of_pages))
                    else:
                        print('number_of_pages : ' + str(number_of_pages))
                else:
                    number_of_pages += round(number_of_pages_with_coma)
                    if number_of_pages > 100:
                        number_of_pages = 100
                        print('number_of_pages : ' + str(number_of_pages))
                    else:
                        print('number_of_pages : ' + str(number_of_pages))
        else:
            print("there is no results")

        time.sleep(5)

        browser.quit()

    # ok
    def test_extract_contacts_for_all_regions_and_one_activity_into_mysql_without_headless(self):
        print("test_extract_contacts_for_all_regions_and_one_activity_into_mysql_without_headless")

        elements = [
            {
                'url': 'https://www.pagesjaunes.fr/annuaire/chercherlespros?quoiqui=engrais&ou=Auvergne-Rh%C3%B4ne-Alpes&idOu=R84&proximite=0&quoiQuiInterprete=engrais&contexte=BspvYw24EqaRgAK3nLYtXA%3D%3D&page=',
                'region': 'Auvergne-Rhône-Alpes',
                'start': '1'
            },
            {
                'url': '',
                'region': 'Bourgogne-Franche-Comté',
                'start': '1'
            },
            {
                'url': '',
                'region': 'Bretagne',
                'start': '1'
            },
            {
                'url': '',
                'region': 'Centre-Val de Loire',
                'start': '1'
            },
            {
                'url': '',
                'region': 'Corse',
                'start': '1'
            },
            {
                'url': '',
                'region': 'Grand-Est',
                'start': '1'
            },
            {
                'url': '',
                'region': 'Hauts-de-France',
                'start': '1'
            },
            {
                'url': '',
                'region': 'Ile-de-France',
                'start': '1'
            },
            {
                'url': '',
                'region': 'Normandie',
                'start': '1'
            },
            {
                'url': '',
                'region': 'Nouvelle-Aquitaine',
                'start': '1'
            },
            {
                'url': '',
                'region': 'Occitanie',
                'start': '1'
            },
            {
                'url': '',
                'region': 'Pays de la Loire',
                'start': '1'
            },
            {
                'url': '',
                'region': 'Provence-Alpes-Côte Azur',
                'start': '1'
            },
            {
                'url': '',
                'region': 'Guadeloupe',
                'start': '1'
            },
            {
                'url': '',
                'region': 'Martinique',
                'start': '1'
            },
            {
                'url': '',
                'region': 'Guyane',
                'start': '1'
            },
            {
                'url': '',
                'region': 'La Réunion',
                'start': '1'
            },
            {
                'url': '',
                'region': 'Mayotte',
                'start': '1'
            }
        ]

        for element in elements:
            try:
                # numero_page
                numero_page = "1"

                number_of_pages = 0

                url_of_one_page_of_companies = element.get('url') + str(numero_page)

                time.sleep(5)

                warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

                time.sleep(5)

                # with Firefox
                browser = webdriver.Firefox(executable_path='..\\..\\..\\geckodriver.exe')

                time.sleep(5)

                # maximize window
                browser.maximize_window()

                time.sleep(5)

                # open
                browser.get(url_of_one_page_of_companies)

                time.sleep(15)

                # Click on the "Continuer sans accepter" button
                continuer_sans_accepter_button = browser.find_element_by_xpath(
                    "/html/body/div[1]/div/div/div/div/div/span"
                )
                continuer_sans_accepter_button.click()
                print('continuer_sans_accepter_button clicked')

                time.sleep(10)

                if browser.find_element_by_id("SEL-nbresultat") is not None:
                    number_of_pages_with_coma = int(browser.find_element_by_id("SEL-nbresultat")
                                                    .text
                                                    .replace(" ", "")
                                                    ) / 20

                    if int(str(number_of_pages_with_coma).split(".")[1][:1]) < 5:
                        number_of_pages += round(number_of_pages_with_coma) + 1
                        if number_of_pages > 100:
                            number_of_pages = 100
                            print('number_of_pages : ' + str(number_of_pages))
                        else:
                            print('number_of_pages : ' + str(number_of_pages))
                    elif int(str(number_of_pages_with_coma).split(".")[1][:1]) >= 5:
                        if int(str(number_of_pages_with_coma).split(".")[0]) == 0:
                            number_of_pages += round(number_of_pages_with_coma) + 1
                            if number_of_pages > 100:
                                number_of_pages = 100
                                print('number_of_pages : ' + str(number_of_pages))
                            else:
                                print('number_of_pages : ' + str(number_of_pages))
                        else:
                            number_of_pages += round(number_of_pages_with_coma)
                            if number_of_pages > 100:
                                number_of_pages = 100
                                print('number_of_pages : ' + str(number_of_pages))
                            else:
                                print('number_of_pages : ' + str(number_of_pages))
                else:
                    print("there is no results")

                time.sleep(5)
                
                browser.quit()
                print("browser closed url_of_one_page_of_companies")

                time.sleep(5)

                subprocess.call("taskkill /F /IM geckodriver.exe")
                subprocess.call("taskkill /F /IM firefox.exe")

                time.sleep(10)

                print("ccleaner running url_of_one_page_of_companies")
                os.system("set ccleaner='C:\\Program Files\\CCleaner\\CCleaner.exe'")
                os.system("start ccleaner /AUTO")

                time.sleep(20)

                i_1 = 0

                if number_of_pages >= 1:
                    for i in range(int(element.get('start')), number_of_pages + 1):
                        # url_of_one_page_of_companies_v1
                        try:
                            url_of_one_page_of_companies_v1 = element.get('url') + str(i)

                            print('url_of_one_page_of_companies_v1 : ' + str(url_of_one_page_of_companies_v1))

                            urls_company = []

                            time.sleep(5)

                            warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

                            time.sleep(5)

                            # with Firefox
                            browser = webdriver.Firefox(executable_path='..\\..\\..\\geckodriver.exe')

                            time.sleep(5)

                            # maximize window
                            browser.maximize_window()

                            time.sleep(5)

                            # open
                            browser.get(url_of_one_page_of_companies_v1)
                            print("browser.get(url_of_one_page_of_companies_v1)")

                            time.sleep(15)

                            # Click on the "Continuer sans accepter" button
                            continuer_sans_accepter_button = browser.find_element_by_xpath(
                                "/html/body/div[1]/div/div/div/div/div/span"
                            )
                            continuer_sans_accepter_button.click()
                            print('continuer_sans_accepter_button clicked')

                            time.sleep(10)

                            try:
                                all_li = browser.find_elements_by_class_name('bi-bloc')

                                for i in range(0, len(all_li)):
                                    try:
                                        if all_li[i].find_element_by_class_name("company-name") is not None:
                                            if all_li[i].find_element_by_class_name("company-name").find_elements_by_tag_name("a")[0].get_attribute('href') == "#":
                                                try:
                                                    json_bloc = json.loads(all_li[i].get('data-pjtoggleclasshisto'))

                                                    bloc_id = json_bloc["idbloc"]["id_bloc"]

                                                    no_sequence = json_bloc["idbloc"]["no_sequence"]

                                                    json_code_rubrique = json.loads(all_li[i].select("div")[0].get(
                                                        'data-pjinfosaccengage-rmk-connexefd-' + bloc_id.lower()))

                                                    code_rubrique = json_code_rubrique["kAN9ProToUserInfo"]

                                                    url_page_1 = 'https://www.pagesjaunes.fr/pros/detail?bloc_id=' + bloc_id + \
                                                                 '&no_sequence=' + no_sequence + '&code_rubrique=' + code_rubrique

                                                    urls_company.append(url_page_1)
                                                except Exception as e:
                                                    print('error url_page_1 : ' + str(e))
                                            else:
                                                try:
                                                    url_page_2 = all_li[i].find_element_by_class_name(
                                                        "company-name").find_elements_by_tag_name("a")[0].get_attribute(
                                                        'href')

                                                    urls_company.append(url_page_2)
                                                except Exception as e:
                                                    print("error url_page_2 : " + str(e))
                                        else:
                                            print(str(i_1) + " no h3 class company-name noTrad")
                                    except Exception as e:
                                        print(str(i_1) + " error 1 : " + str(e))
                            except Exception as e:
                                print('error url_company : ' + str(e))

                            time.sleep(5)

                            browser.quit()
                            print('browser closed url_of_one_page_of_companies_v1')

                            time.sleep(5)

                            subprocess.call("taskkill /F /IM geckodriver.exe")
                            subprocess.call("taskkill /F /IM firefox.exe")

                            time.sleep(10)

                            print("ccleaner running url_of_one_page_of_companies_v1")
                            os.system("set ccleaner='C:\\Program Files\\CCleaner\\CCleaner.exe'")
                            os.system("start ccleaner /AUTO")

                            time.sleep(20)

                            for url_company in urls_company:
                                print('url_company : ' + str(url_company))

                                time.sleep(5)

                                warnings.filterwarnings(action="ignore",
                                                        message="unclosed",
                                                        category=ResourceWarning)

                                time.sleep(5)

                                # with Firefox
                                browser = webdriver.Firefox(executable_path='..\\..\\..\\geckodriver.exe')

                                time.sleep(5)

                                # maximize window
                                browser.maximize_window()

                                time.sleep(5)

                                # open
                                browser.get(url_company)
                                print('browser.get(url_company)')

                                time.sleep(20)

                                # Click on the "Continuer sans accepter" button
                                continuer_sans_accepter_button = browser.find_element_by_xpath(
                                    "/html/body/div[1]/div/div/div/div/div/span"
                                )
                                continuer_sans_accepter_button.click()
                                print('continuer_sans_accepter_button clicked')

                                time.sleep(10)

                                try:
                                    raison_sociale = ""
                                    adresse_postale = ""
                                    phone_number = ""
                                    website = ""
                                    email = ""
                                    presence = ""
                                    activite = ""
                                    siren = ""
                                    lien_societe_com = ""
                                    president = ""

                                    # raison sociale
                                    try:
                                        raison_sociale += browser.find_element_by_xpath(
                                            "/html/body/main/div[2]/section/div[2]/div[1]/div[1]/div/div[1]/h1"
                                        ).text
                                        print('raison_sociale : ' + str(raison_sociale))
                                    except Exception as e:
                                        print("error raison_sociale : " + str(e))

                                    # adresse_postale
                                    try:
                                        adresse_postale += browser.find_element_by_xpath(
                                            "/html/body/main/div[2]/section/div[6]/div[1]/div[2]/div/div/div[2]/a[1]"
                                        ).text
                                        print('adresse_postale : ' + str(adresse_postale))
                                    except Exception as e:
                                        print("error adresse_postale : " + str(e))

                                    # phone_number
                                    try:
                                        phone_number += browser.find_element_by_xpath(
                                            "/html/body/main/div[2]/section/div[6]/div[1]/div[2]/div/div/div[1]/div/span/span[2]"
                                        ).text
                                        print('phone_number : ' + str(phone_number))
                                    except Exception as e:
                                        print('error phone_number : ' + str(e))

                                    # website
                                    try:
                                        website += browser.find_element_by_xpath(
                                            "/html/body/main/div[2]/section/div[6]/div[1]/div[2]/div/div/div[4]/a"
                                        ).text
                                        print('website : ' + str(website))
                                    except Exception as e:
                                        print("error website : " + str(e))

                                    # email
                                    try:
                                        email += "'contact@" + browser.find_element_by_xpath(
                                            "/html/body/main/div[2]/section/div[6]/div[1]/div[2]/div/div/div[4]/a"
                                        ).text \
                                            .replace("https://www.", "") \
                                            .replace("http://www.", "") \
                                            .replace("https://", "") \
                                            .replace("http://", "") + "',"
                                        print('email : ' + str(email))
                                    except Exception as e:
                                        print("error email : " + str(e))

                                    # activite
                                    try:
                                        activite += browser.find_element_by_xpath(
                                            "/html/body/main/div[2]/section/div[2]/div[1]/div[1]/div/div[2]/div"
                                        ).text
                                        print('activite : ' + str(activite))
                                    except Exception as e:
                                        print('error activite : ' + str(e))

                                    # siren
                                    try:
                                        # Click on the "Informations financières et juridiques" button
                                        informations_financieres_juridiques_button = browser.find_element_by_xpath(
                                            "/html/body/main/div[2]/section/div[6]/div[1]/div[12]/h2/button"
                                        )
                                        informations_financieres_juridiques_button.click()

                                        time.sleep(10)

                                        siren += browser.find_element_by_xpath(
                                            "/html/body/main/div[2]/section/div[6]/div[1]/div[12]/div/dl[2]/dd[1]/strong"
                                        ).text
                                        print('siren : ' + str(siren))
                                    except Exception as e:
                                        print('error siren : ' + str(e))

                                    # lien_societe_com
                                    # presence of the chairman
                                    try:
                                        informations_financieres_juridiques_button = browser.find_element_by_xpath(
                                            "/html/body/main/div[2]/section/div[6]/div[1]/div[12]/h2/button"
                                        )
                                        informations_financieres_juridiques_button.click()

                                        time.sleep(10)

                                        siren += browser.find_element_by_xpath(
                                            "/html/body/main/div[2]/section/div[6]/div[1]/div[12]/div/dl[2]/dd[1]/strong"
                                        ).text

                                        if siren != '':
                                            lien_societe_com += "https://www.societe.com/cgi-bin/search?champs=" + siren
                                            print("lien_societe_com : " + str(lien_societe_com))

                                            payload = {}

                                            headers = {
                                                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
                                            }

                                            # Request the content of a page from the url
                                            html = requests.request("GET", lien_societe_com, headers=headers, data=payload)

                                            # Parse the content of html_doc
                                            soup = BeautifulSoup(html.content, 'html.parser')

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
                                                        presence += "oui"
                                                        break
                                                else:
                                                    print('no president')
                                                    presence += "non"
                                    except Exception as e:
                                        print('error lien_societe_com : ' + str(e))

                                    x = {
                                        "raison_sociale": raison_sociale,
                                        "adresse_postale": adresse_postale,
                                        "phone_number": phone_number,
                                        "website": website,
                                        "email": email,
                                        "presence": presence,
                                        "page_jaune": url_company,
                                        "region": element.get('region'),
                                        "activite": activite,
                                        "siren": siren,
                                        "lien_societe_com": lien_societe_com,
                                        "president": president
                                    }

                                    try:
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
                                                sql = "INSERT INTO `contacts_pour_excel` (" \
                                                      "`raison_sociale`, " \
                                                      "`adresse_postale`, " \
                                                      "`phone_number`, " \
                                                      "`website`, " \
                                                      "`email`, " \
                                                      "`presence`, " \
                                                      "`page_jaune`, " \
                                                      "`region`, " \
                                                      "`activite`, " \
                                                      "`siren`, " \
                                                      "`lien_societe_com`, " \
                                                      "`president`) VALUE (%s, %s, %s, %s, %s, %s, %s, " \
                                                      "%s, %s, %s, %s, %s)"

                                                cursor.execute(sql, (
                                                    x.get('raison_sociale'),
                                                    x.get('adresse_postale'),
                                                    x.get('phone_number'),
                                                    x.get('website'),
                                                    x.get('email'),
                                                    x.get('presence'),
                                                    x.get('page_jaune'),
                                                    x.get('region'),
                                                    x.get('activite'),
                                                    x.get('siren'),
                                                    x.get('lien_societe_com'),
                                                    x.get('president')
                                                ))

                                                connection.commit()

                                                print(str(i_1)
                                                      + " corporation : " + x.get('raison_sociale')
                                                      + " ; presence of the chairman : " + x.get('presence')
                                                      + " ; activite : " + x.get('activite')
                                                      + " ; siren : " + x.get('siren')
                                                      + " ; president : " + x.get('president'))

                                                connection.close()
                                            except Exception as e:
                                                print(str(i_1) + " The record already exists : " + str(e))
                                                connection.close()
                                    except Exception as e:
                                        print("Problem connection MySQL : " + str(e))
                                except Exception as e:
                                    print("error url_page_1 : " + str(e))

                                browser.quit()
                                print("browser closed url_company")

                                time.sleep(5)

                                subprocess.call("taskkill /F /IM geckodriver.exe")
                                subprocess.call("taskkill /F /IM firefox.exe")

                                time.sleep(10)

                                print("ccleaner running url_company")
                                os.system("set ccleaner='C:\\Program Files\\CCleaner\\CCleaner.exe'")
                                os.system("start ccleaner /AUTO")

                                time.sleep(20)

                                i_1 += 1
                        except Exception as e:
                            print("error url_of_one_page_of_companies : " + str(e))
                else:
                    print("number of pages < 1")
            except Exception as e:
                print("error element : " + str(e))


class UnitTestsDataMiningYellowPagesFranceWithRpaWithHeadless(unittest.TestCase):
    # ok
    def test_open_one_page_with_headless(self):
        print('test_open_one_page_with_headless')

        time.sleep(5)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(5)

        # with Firefox
        options = Options()
        options.headless = True
        browser = webdriver.Firefox(executable_path='..\\..\\..\\geckodriver.exe', options=options)

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get(
            'https://www.pagesjaunes.fr/pros/detail?bloc_id=FCP06923089CLIENTDA3000004C0001&no_sequence=1&code_rubrique=16053100')
        print('browser get')

        time.sleep(15)

        browser.quit()
        print("browser.quit()")

    # ok
    def test_extract_the_website_from_one_page_with_headless(self):
        print('test_extract_the_website_from_one_page_with_headless')

        url = "https://www.pagesjaunes.fr/pros/56959397"

        time.sleep(5)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(5)

        # with Firefox
        options = Options()
        options.headless = True
        browser = webdriver.Firefox(executable_path='..\\..\\..\\geckodriver.exe', options=options)

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get(url)
        print('browser.get(url)')

        time.sleep(15)

        # Click on the "Continuer sans accepter" button
        continuer_sans_accepter_button = browser.find_element_by_xpath(
            "/html/body/div[1]/div/div/div/div/div/span"
        )
        continuer_sans_accepter_button.click()
        print('continuer_sans_accepter_button clicked')

        time.sleep(10)

        # Print the website
        try:
            website_text = browser.find_element_by_xpath(
                "/html/body/main/div[2]/section/div[6]/div[1]/div[1]/div/div/div[3]/a/span[2]"
            ).text
            print('website_text : ' + str(website_text))
        except Exception as e:
            print("error website : " + str(e))

        time.sleep(5)

        browser.quit()
        print("browser.quit()")

    # ok
    def test_extract_the_email_from_one_page_with_headless(self):
        print('test_extract_the_email_from_one_page_with_headless')

        url = "https://www.pagesjaunes.fr/pros/56959397"

        time.sleep(5)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(5)

        # with Firefox
        options = Options()
        options.headless = True
        browser = webdriver.Firefox(executable_path='..\\..\\..\\geckodriver.exe', options=options)

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get(url)
        print('browser.get(url)')

        time.sleep(15)

        # Click on the "Continuer sans accepter" button
        continuer_sans_accepter_button = browser.find_element_by_xpath(
            "/html/body/div[1]/div/div/div/div/div/span"
        )
        continuer_sans_accepter_button.click()
        print('continuer_sans_accepter_button clicked')

        time.sleep(10)

        # Print the email
        try:
            email_text = "'contact@" + browser.find_element_by_xpath(
                "/html/body/main/div[2]/section/div[6]/div[1]/div[1]/div/div/div[3]/a/span[2]"
            ).text \
                .replace("https://www.", "") \
                .replace("http://www.", "") \
                .replace("https://", "") \
                .replace("http://", "") + "',"
            print('email_text : ' + str(email_text))
        except Exception as e:
            print("error email_text : " + str(e))

        time.sleep(5)

        browser.quit()

    # ok
    def test_extract_corporation_name_from_one_page_with_headless(self):
        print("test_extract_corporation_name_from_one_page_with_headless")

        url = "https://www.pagesjaunes.fr/pros/56959397"

        try:
            time.sleep(5)

            warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

            time.sleep(5)

            # with Firefox
            options = Options()
            options.headless = True
            browser = webdriver.Firefox(
                executable_path='..\\..\\..\\geckodriver.exe',
                options=options
            )

            time.sleep(5)

            # maximize window
            browser.maximize_window()

            time.sleep(5)

            # open
            browser.get(url)
            print('browser.get(url)')

            time.sleep(15)

            # Click on the "Continuer sans accepter" button
            continuer_sans_accepter_button = browser.find_element_by_xpath(
                "/html/body/div[1]/div/div/div/div/div/span"
            )
            continuer_sans_accepter_button.click()
            print('continuer_sans_accepter_button clicked')

            time.sleep(10)

            # Print the corporation_name
            try:
                corporation_name_text = browser.find_element_by_xpath(
                    "/html/body/main/div[2]/section/div[2]/div[1]/div[1]/div/div[1]/h1"
                ).text
                print('corporation_name_text : ' + str(corporation_name_text))
            except Exception as e:
                print("error corporation_name_text : " + str(e))

            time.sleep(5)

            browser.quit()
            print('browser.quit()')
        except Exception as e:
            print("error url : " + str(e))

    # ok
    def test_extract_corporation_address_from_one_page_with_headless(self):
        print("test_extract_corporation_address_from_one_page_with_headless")

        url = "https://www.pagesjaunes.fr/pros/56959397"

        try:
            time.sleep(5)

            warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

            time.sleep(5)

            # with Firefox
            options = Options()
            options.headless = True
            browser = webdriver.Firefox(executable_path='..\\..\\..\\geckodriver.exe', options=options)

            time.sleep(5)

            # maximize window
            browser.maximize_window()

            time.sleep(5)

            # open
            browser.get(url)
            print('browser.get(url)')

            time.sleep(15)

            # Click on the "Continuer sans accepter" button
            continuer_sans_accepter_button = browser.find_element_by_xpath(
                "/html/body/div[1]/div/div/div/div/div/span"
            )
            continuer_sans_accepter_button.click()
            print('continuer_sans_accepter_button clicked')

            time.sleep(10)

            try:
                # Print the corporation_address
                corporation_address_text = browser.find_element_by_xpath(
                    "/html/body/main/div[2]/section/div[6]/div[1]/div[1]/div/div/div[2]/a[1]"
                ).text
                print('corporation_address_text : ' + str(corporation_address_text))
            except Exception as e:
                print("error corporation_address_text : " + str(e))

            time.sleep(5)

            browser.quit()
            print('browser.quit()')
        except Exception as e:
            print("error url : " + str(e))

    # ok
    def test_extract_corporation_phone_number_from_one_page_with_headless(self):
        print("test_extract_corporation_phone_number_from_one_page_with_headless")

        url = "https://www.pagesjaunes.fr/pros/56959397"

        try:
            time.sleep(5)

            warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

            time.sleep(5)

            # with Firefox
            options = Options()
            options.headless = True
            browser = webdriver.Firefox(executable_path='..\\..\\..\\geckodriver.exe', options=options)

            time.sleep(5)

            # maximize window
            browser.maximize_window()

            time.sleep(5)

            # open
            browser.get(url)
            print("browser.get(url)")

            time.sleep(15)

            try:
                # Click on the "Continuer sans accepter" button
                continuer_sans_accepter_button = browser.find_element_by_xpath(
                    "/html/body/div[1]/div/div/div/div/div/span"
                )
                continuer_sans_accepter_button.click()
                print('continuer_sans_accepter_button clicked')
            except Exception as e:
                print('error continuer_sans_accepter_button : ' + str(e))

            time.sleep(10)

            try:
                # Click on the "Afficher le numéro" button
                afficher_le_numero_button = browser.find_element_by_xpath(
                    "/html/body/main/div[2]/section/div[6]/div[1]/div[1]/div/div/div[1]/a"
                )
                afficher_le_numero_button.click()
                print("afficher_le_numero_button.click()")
            except Exception as e:
                print("error afficher_le_numero_button : " + str(e))

            time.sleep(15)

            # Print the corporation_phone_number
            try:
                # corporation_phone_number_text
                corporation_phone_number_text = browser.find_element_by_class_name(
                    "coord-numero"
                ).text
                print('corporation_phone_number_text : ' + str(corporation_phone_number_text))
            except Exception as e:
                print('error corporation_phone_number_text : ' + str(e))

            time.sleep(5)

            browser.quit()
            print('browser.quit()')
        except Exception as e:
            print("error url : " + str(e))

    # ok
    def test_extract_siren_from_one_page_with_headless(self):
        print("test_extract_siren_from_one_page_with_headless")

        url = "https://www.pagesjaunes.fr/pros/56959397"

        try:
            time.sleep(5)

            warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

            time.sleep(5)

            # with Firefox
            options = Options()
            options.headless = True
            browser = webdriver.Firefox(executable_path='..\\..\\..\\geckodriver.exe', options=options)

            time.sleep(5)

            # maximize window
            browser.maximize_window()

            time.sleep(5)

            # open
            browser.get(url)
            print('browser.get(url)')

            time.sleep(15)

            # Click on the "Continuer sans accepter" button
            continuer_sans_accepter_button = browser.find_element_by_xpath(
                "/html/body/div[1]/div/div/div/div/div/span"
            )
            continuer_sans_accepter_button.click()
            print('continuer_sans_accepter_button clicked')

            time.sleep(10)

            try:
                # Click on the "Informations financières et juridiques" button
                informations_financieres_juridiques_button = browser.find_element_by_xpath(
                    "/html/body/main/div[2]/section/div[6]/div[1]/div[11]/h2/button"
                )
                informations_financieres_juridiques_button.click()

                time.sleep(10)

                # Print the siren
                siren_text = browser.find_element_by_xpath(
                    "/html/body/main/div[2]/section/div[6]/div[1]/div[11]/div/dl[2]/dd[1]/strong"
                ).text
                print('siren_text : ' + str(siren_text))
            except Exception as e:
                print('error siren_text : ' + str(e))

            time.sleep(5)

            browser.quit()
            print('browser.quit()')
        except Exception as e:
            print("error url : " + str(e))

    # ok
    def test_extract_activite_from_one_page_with_headless(self):
        print("test_extract_activite_from_one_page_with_headless")

        url = "https://www.pagesjaunes.fr/pros/56959397"

        try:
            time.sleep(5)

            warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

            time.sleep(5)

            # with Firefox
            options = Options()
            options.headless = True
            browser = webdriver.Firefox(executable_path='..\\..\\..\\geckodriver.exe', options=options)

            time.sleep(5)

            # maximize window
            browser.maximize_window()

            time.sleep(5)

            # open
            browser.get(url)
            print("browser.get(url)")

            time.sleep(15)

            # Click on the "Continuer sans accepter" button
            continuer_sans_accepter_button = browser.find_element_by_xpath(
                "/html/body/div[1]/div/div/div/div/div/span"
            )
            continuer_sans_accepter_button.click()
            print('continuer_sans_accepter_button clicked')

            time.sleep(10)

            try:
                # Print the activite_text
                activite_text = browser.find_element_by_xpath(
                    "/html/body/main/div[2]/section/div[2]/div[1]/div[1]/div/div[2]/div/span"
                ).text
                print('activite_text : ' + str(activite_text))
            except Exception as e:
                print('error activite_text : ' + str(e))

            time.sleep(5)

            browser.quit()
            print('browser.quit()')
        except Exception as e:
            print("error url : " + str(e))

    # ok
    def test_extract_the_president_of_one_company_from_one_page_with_headless(self):
        print("test_extract_the_president_of_one_company_from_one_page_with_headless")

        siren = ""

        url = "https://www.pagesjaunes.fr/pros/56959397"

        try:
            time.sleep(5)

            warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

            time.sleep(5)

            # with Firefox
            options = Options()
            options.headless = True
            browser = webdriver.Firefox(executable_path='..\\..\\..\\geckodriver.exe', options=options)

            time.sleep(5)

            # maximize window
            browser.maximize_window()

            time.sleep(5)

            # open
            browser.get(url)
            print("browser.get(url)")

            time.sleep(15)

            # Click on the "Continuer sans accepter" button
            continuer_sans_accepter_button = browser.find_element_by_xpath(
                "/html/body/div[1]/div/div/div/div/div/span"
            )
            continuer_sans_accepter_button.click()
            print('continuer_sans_accepter_button clicked')

            time.sleep(10)

            try:
                # Click on the "Informations financières et juridiques" button
                informations_financieres_juridiques_button = browser.find_element_by_xpath(
                    "/html/body/main/div[2]/section/div[6]/div[1]/div[11]/h2/button"
                )
                informations_financieres_juridiques_button.click()

                time.sleep(10)

                # Print the siren
                siren += browser.find_element_by_xpath(
                    "/html/body/main/div[2]/section/div[6]/div[1]/div[11]/div/dl[2]/dd[1]/strong"
                ).text
                print('siren : ' + str(siren))

                if siren != '':
                    url = "https://www.societe.com/cgi-bin/search?champs=" + siren

                    payload = {}

                    headers = {
                        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '
                                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                                      'Chrome/51.0.2704.103'
                    }

                    # Request the content of a page from the url
                    html = requests.request("GET", url, headers=headers, data=payload)

                    # Parse the content of html_doc
                    soup = BeautifulSoup(html.content, 'html.parser')

                    for i in range(1, 20):
                        if soup.select_one("#dir" + str(i)) is not None:
                            president = soup.select_one("#dir" + str(i)) \
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
            except Exception as e:
                print('error siren : ' + str(e))

            time.sleep(5)

            browser.quit()
            print('browser.quit()')
        except Exception as e:
            print("error url : " + str(e))

    # ok
    def test_extract_all_url_company_for_one_page_of_companies_for_one_activity_and_one_capital_with_headless(self):
        print("test_extract_all_url_company_for_one_page_of_companies_for_one_activity_and_one_capital_with_headless")

        try:
            url_of_one_page_of_companies = "https://www.pagesjaunes.fr/annuaire/chercherlespros?quoiqui=centre%20formation&ou=La%20R%C3%A9union%20%28974%29&idOu=D974&proximite=0&quoiQuiInterprete=centre%20formation&contexte=KJgk20GZy5wkoY7jbFyG/FVzcTliZBwRE8ILzRtG9neMLeyin%2BWE3eZTfwZaF9sLKr/IpvAYckulUL9HYtwr29Bs4Pvf7kaod2TdkwFfQ48%3D&page=2"

            urls_company = []

            time.sleep(5)

            warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

            time.sleep(5)

            # with Firefox
            options = Options()
            options.headless = True
            browser = webdriver.Firefox(executable_path='..\\..\\..\\geckodriver.exe', options=options)

            time.sleep(5)

            # maximize window
            browser.maximize_window()

            time.sleep(5)

            # open
            browser.get(url_of_one_page_of_companies)

            time.sleep(15)

            try:
                # Click on the "Continuer sans accepter" button
                continuer_sans_accepter_button = browser.find_element_by_xpath(
                    "/html/body/div[1]/div/div/div/div/div/span"
                )
                continuer_sans_accepter_button.click()
                print('continuer_sans_accepter_button clicked')
            except Exception as e:
                print('error continuer_sans_accepter_button : ' + str(e))

            time.sleep(10)

            try:
                # Print all url_company
                i_1 = 0

                all_li = browser.find_elements_by_class_name('bi-generic')

                for i in range(0, len(all_li)):
                    try:
                        if all_li[i].find_element_by_class_name("bi-content") is not None:
                            if all_li[i].find_element_by_class_name("bi-content").find_elements_by_tag_name("a")[0]\
                                    .get_attribute('href') == "#":
                                try:
                                    # json_bloc = json.loads(all_li[i].get('data-pjtoggleclasshisto'))
                                    # bloc_id = json_bloc["idbloc"]["id_bloc"]
                                    # no_sequence = json_bloc["idbloc"]["no_sequence"]
                                    # json_code_rubrique = json.loads(all_li[i].select("div")[0].get('data-pjinfosaccengage-rmk-connexefd-' + bloc_id.lower()))
                                    # code_rubrique = json_code_rubrique["kAN9ProToUserInfo"]
                                    # url_page_1 = 'https://www.pagesjaunes.fr/pros/detail?bloc_id=' + bloc_id + '&no_sequence=' + no_sequence + '&code_rubrique=' + code_rubrique

                                    json_bloc_url = json.loads(all_li[i].find_element_by_class_name("bi-with-visual")
                                                               .find_elements_by_tag_name("a")[0].get('data-pjlb'))

                                    url_encoded = json_bloc_url['url']

                                    url_decoded = urlsafe_b64decode(url_encoded)

                                    url_page_1 = str(url_decoded)
                                    # url_page_1 = 'https://www.pagesjaunes.fr' + str(url_decoded)

                                    urls_company.append(url_page_1)
                                except Exception as e:
                                    print('error url_page_1 : ' + str(e))
                            else:
                                try:
                                    # url_page_2 = 'https://www.pagesjaunes.fr' + all_li[i].find_element_by_class_name("bi-content").find_elements_by_tag_name("a")[0].get_attribute('href')
                                    url_page_2 = all_li[i].find_element_by_class_name("bi-content").find_elements_by_tag_name("a")[0].get_attribute('href')

                                    urls_company.append(url_page_2)
                                except Exception as e:
                                    print("error url_page_2 : " + str(e))
                        else:
                            print(str(i_1) + " no div class bi-with-visual")
                    except Exception as e:
                        print(str(i_1) + " error 1 : " + str(e))

                    i_1 += 1
            except Exception as e:
                print('error url_company : ' + str(e))

            time.sleep(5)

            browser.quit()
            print('browser.quit()')

            for url_company in urls_company:
                print('company : ' + str(url_company))
        except Exception as e:
            print("error url : " + str(e))

    # ok
    def test_print_the_number_of_pages_for_one_activity_and_one_capital_with_headless(self):
        print("test_print_the_number_of_pages_for_one_activity_and_one_capital_with_headless")

        number_of_pages = 0

        url_of_one_page_of_companies = "https://www.pagesjaunes.fr/annuaire/chercherlespros?quoiqui=" \
                                       "centre%20formation&ou=La%20R%C3%A9union%20%28974%29&idOu=" \
                                       "D974&proximite=0&quoiQuiInterprete=centre%20formation&contexte=" \
                                       "iv4kmy%2Bx5dZ/pXOgvoQS7A%3D%3D&page=2"

        time.sleep(5)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(5)

        # with Firefox
        options = Options()
        options.headless = True
        browser = webdriver.Firefox(executable_path='..\\..\\..\\geckodriver.exe', options=options)

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get(url_of_one_page_of_companies)

        time.sleep(15)

        # Click on the "Continuer sans accepter" button
        continuer_sans_accepter_button = browser.find_element_by_xpath(
            "/html/body/div[1]/div/div/div/div/div/span"
        )
        continuer_sans_accepter_button.click()
        print('continuer_sans_accepter_button clicked')

        time.sleep(10)

        if browser.find_element_by_id("SEL-nbresultat") is not None:
            number_of_pages_with_coma = int(browser.find_element_by_id("SEL-nbresultat")
                                            .text
                                            .replace(" ", "")
                                            ) / 20

            if int(str(number_of_pages_with_coma).split(".")[1][:1]) < 5:
                number_of_pages += round(number_of_pages_with_coma) + 1
                if number_of_pages > 100:
                    number_of_pages = 100
                    print('number_of_pages : ' + str(number_of_pages))
                else:
                    print('number_of_pages : ' + str(number_of_pages))

            elif int(str(number_of_pages_with_coma).split(".")[1][:1]) >= 5:
                if int(str(number_of_pages_with_coma).split(".")[0]) == 0:
                    number_of_pages += round(number_of_pages_with_coma) + 1
                    if number_of_pages > 100:
                        number_of_pages = 100
                        print('number_of_pages : ' + str(number_of_pages))
                    else:
                        print('number_of_pages : ' + str(number_of_pages))
                else:
                    number_of_pages += round(number_of_pages_with_coma)
                    if number_of_pages > 100:
                        number_of_pages = 100
                        print('number_of_pages : ' + str(number_of_pages))
                    else:
                        print('number_of_pages : ' + str(number_of_pages))
        else:
            print("there is no results")

        time.sleep(5)

        browser.quit()
        print('browser.quit()')

    #
    def test_extract_contacts_for_all_regions_and_one_activity_into_mysql_with_headless(self):
        print("test_extract_contacts_for_all_regions_and_one_activity_into_mysql_with_headless")

        """
        {
            'url': '',
            'region': 'Auvergne-Rhône-Alpes',
            'start': '1'
        },
        {
            'url': '',
            'region': 'Bourgogne-Franche-Comté',
            'start': '1'
        },
        {
            'url': '',
            'region': 'Bretagne',
            'start': '1'
        },
        {
            'url': '',
            'region': 'Centre-Val de Loire',
            'start': '1'
        },
        {
            'url': '',
            'region': 'Corse',
            'start': '1'
        },
        {
            'url': '',
            'region': 'Grand-Est',
            'start': '1'
        },
        {
            'url': '',
            'region': 'Hauts-de-France',
            'start': '1'
        },
        {
            'url': '',
            'region': 'Ile-de-France',
            'start': '1'
        },
        {
            'url': '',
            'region': 'Normandie',
            'start': '1'
        },
        {
            'url': '',
            'region': 'Nouvelle-Aquitaine',
            'start': '1'
        },
        {
            'url': '',
            'region': 'Occitanie',
            'start': '1'
        },
        {
            'url': '',
            'region': 'Pays de la Loire',
            'start': '1'
        },
        {
            'url': '',
            'region': 'Provence-Alpes-Côte Azur',
            'start': '1'
        },
        {
            'url': '',
            'region': 'Guadeloupe',
            'start': '1'
        },
        {
            'url': '',
            'region': 'Martinique',
            'start': '1'
        },
        {
            'url': '',
            'region': 'Guyane',
            'start': '1'
        },
        """

        elements = [
            {
                'url': 'https://www.pagesjaunes.fr/annuaire/chercherlespros?quoiqui=centre%20de%20formation&ou=La%20R%C3%A9union%20%28974%29&idOu=D974&proximite=0&quoiQuiInterprete=centre%20de%20formation&contexte=BpABNrX5iwjFFSh4j05ybB65/mUAOqTlMq/5TDTlgMq/NQZLeCO2HS5gKeT1MxB0jgaFPN2l%2BfETPZzcuF0sqQbkCJ9D1JVfCoZvFr65OGc%3D&page=',
                'region': 'La Réunion',
                'start': '1'
            },
        ]

        """
        {
            'url': '',
            'region': 'Mayotte',
            'start': '1'
        }
        """

        for element in elements:
            try:
                # numero_page
                numero_page = "1"

                number_of_pages = 0

                url_of_one_page_of_companies = element.get('url') + str(numero_page)

                time.sleep(5)

                warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

                time.sleep(5)

                # with Firefox
                options = Options()
                options.headless = True
                browser = webdriver.Firefox(executable_path='..\\..\\..\\geckodriver.exe', options=options)

                time.sleep(5)

                # maximize window
                browser.maximize_window()

                time.sleep(5)

                # open
                browser.get(url_of_one_page_of_companies)

                time.sleep(15)

                try:
                    # Click on the "Continuer sans accepter" button
                    continuer_sans_accepter_button = browser.find_element_by_xpath(
                        "/html/body/div[1]/div/div/div/div/div/span"
                    )
                    continuer_sans_accepter_button.click()
                    print('continuer_sans_accepter_button clicked')
                except Exception as e:
                    print('error continuer_sans_accepter_button : ' + str(e))

                time.sleep(10)

                if browser.find_element_by_id("SEL-nbresultat") is not None:
                    number_of_pages_with_coma = int(browser.find_element_by_id("SEL-nbresultat")
                                                    .text
                                                    .replace(" ", "")
                                                    ) / 20

                    if int(str(number_of_pages_with_coma).split(".")[1][:1]) < 5:
                        number_of_pages += round(number_of_pages_with_coma) + 1
                        if number_of_pages > 100:
                            number_of_pages = 100
                            print('number_of_pages : ' + str(number_of_pages))
                        else:
                            print('number_of_pages : ' + str(number_of_pages))
                    elif int(str(number_of_pages_with_coma).split(".")[1][:1]) >= 5:
                        if int(str(number_of_pages_with_coma).split(".")[0]) == 0:
                            number_of_pages += round(number_of_pages_with_coma) + 1
                            if number_of_pages > 100:
                                number_of_pages = 100
                                print('number_of_pages : ' + str(number_of_pages))
                            else:
                                print('number_of_pages : ' + str(number_of_pages))
                        else:
                            number_of_pages += round(number_of_pages_with_coma)
                            if number_of_pages > 100:
                                number_of_pages = 100
                                print('number_of_pages : ' + str(number_of_pages))
                            else:
                                print('number_of_pages : ' + str(number_of_pages))
                else:
                    print("there is no results")

                time.sleep(5)

                browser.quit()
                print("browser quitted url_of_one_page_of_companies")

                time.sleep(5)

                i_1 = 0

                if number_of_pages >= 1:
                    for i in range(int(element.get('start')), number_of_pages + 1):
                        # url_of_one_page_of_companies_v1
                        try:
                            url_of_one_page_of_companies_v1 = element.get('url') + str(i)

                            print('url_of_one_page_of_companies_v1 : ' + str(url_of_one_page_of_companies_v1))

                            time.sleep(5)

                            warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

                            time.sleep(5)

                            # with Firefox
                            options = Options()
                            options.headless = True
                            browser = webdriver.Firefox(executable_path='..\\..\\..\\geckodriver.exe', options=options)

                            time.sleep(5)

                            # maximize window
                            browser.maximize_window()

                            time.sleep(5)

                            # open
                            browser.get(url_of_one_page_of_companies_v1)
                            print("browser.get(url_of_one_page_of_companies_v1)")

                            time.sleep(15)

                            try:
                                # Click on the "Continuer sans accepter" button
                                continuer_sans_accepter_button = browser.find_element_by_xpath(
                                    "/html/body/div[1]/div/div/div/div/div/span"
                                )
                                continuer_sans_accepter_button.click()
                                print('continuer_sans_accepter_button clicked')
                            except Exception as e:
                                print('error continuer_sans_accepter_button : ' + str(e))

                            time.sleep(10)

                            urls_company = []

                            try:
                                # Print all url_company
                                i_1 = 0

                                all_li = browser.find_elements_by_class_name('bi-generic')

                                for i in range(0, len(all_li)):
                                    try:
                                        if all_li[i].find_element_by_class_name("bi-content") is not None:
                                            if all_li[i].find_element_by_class_name(
                                                    "bi-content").find_elements_by_tag_name("a")[0] \
                                                    .get_attribute('href') == "#":
                                                try:
                                                    # json_bloc = json.loads(all_li[i].get('data-pjtoggleclasshisto'))
                                                    # bloc_id = json_bloc["idbloc"]["id_bloc"]
                                                    # no_sequence = json_bloc["idbloc"]["no_sequence"]
                                                    # json_code_rubrique = json.loads(all_li[i].select("div")[0].get('data-pjinfosaccengage-rmk-connexefd-' + bloc_id.lower()))
                                                    # code_rubrique = json_code_rubrique["kAN9ProToUserInfo"]
                                                    # url_page_1 = 'https://www.pagesjaunes.fr/pros/detail?bloc_id=' + bloc_id + '&no_sequence=' + no_sequence + '&code_rubrique=' + code_rubrique

                                                    json_bloc_url = json.loads(
                                                        all_li[i].find_element_by_class_name("bi-with-visual")
                                                        .find_elements_by_tag_name("a")[0].get('data-pjlb'))

                                                    url_encoded = json_bloc_url['url']

                                                    url_decoded = urlsafe_b64decode(url_encoded)

                                                    url_page_1 = str(url_decoded)
                                                    # url_page_1 = 'https://www.pagesjaunes.fr' + str(url_decoded)

                                                    urls_company.append(url_page_1)
                                                except Exception as e:
                                                    print('error url_page_1 : ' + str(e))
                                            else:
                                                try:
                                                    # url_page_2 = 'https://www.pagesjaunes.fr' + all_li[i].find_element_by_class_name("bi-content").find_elements_by_tag_name("a")[0].get_attribute('href')

                                                    url_page_2 = all_li[i].find_element_by_class_name(
                                                        "bi-content").find_elements_by_tag_name("a")[0].get_attribute(
                                                        'href')

                                                    urls_company.append(url_page_2)
                                                except Exception as e:
                                                    print("error url_page_2 : " + str(e))
                                        else:
                                            print(str(i_1) + " no div class bi-with-visual")
                                    except Exception as e:
                                        print(str(i_1) + " error 1 : " + str(e))

                                    i_1 += 1
                            except Exception as e:
                                print('error url_company : ' + str(e))

                            time.sleep(5)

                            browser.quit()
                            print('browser closed url_of_one_page_of_companies_v1')

                            time.sleep(5)

                            for url_company in urls_company:
                                print('url_company : ' + str(url_company))

                                time.sleep(5)

                                warnings.filterwarnings(action="ignore",
                                                        message="unclosed",
                                                        category=ResourceWarning)

                                time.sleep(5)

                                # with Firefox
                                options = Options()
                                options.headless = True
                                browser = webdriver.Firefox(executable_path='..\\..\\..\\geckodriver.exe',
                                                            options=options)

                                time.sleep(5)

                                # maximize window
                                browser.maximize_window()

                                time.sleep(5)

                                # open
                                browser.get(url_company)
                                print('browser.get(url_company)')

                                time.sleep(20)

                                try:
                                    # Click on the "Continuer sans accepter" button
                                    continuer_sans_accepter_button = browser.find_element_by_xpath(
                                        "/html/body/div[1]/div/div/div/div/div/span"
                                    )
                                    continuer_sans_accepter_button.click()
                                    print('continuer_sans_accepter_button clicked')
                                except Exception as e:
                                    print('error continuer_sans_accepter_button : ' + str(e))

                                time.sleep(10)

                                try:
                                    raison_sociale = ""
                                    adresse_postale = ""
                                    phone_number = ""
                                    website = ""
                                    email = ""
                                    presence = ""
                                    activite = ""
                                    siren = ""
                                    lien_societe_com = ""
                                    president = ""

                                    # raison sociale
                                    try:
                                        raison_sociale += browser.find_element_by_xpath(
                                            "/html/body/main/div[2]/section/div[2]/div[1]/div[1]/div/div[1]/h1"
                                        ).text
                                    except Exception as e:
                                        print("error corporation_name_text : " + str(e))

                                    # adresse_postale
                                    try:
                                        # Print the corporation_address
                                        adresse_postale += browser.find_element_by_xpath(
                                            "/html/body/main/div[2]/section/div[6]/div[1]/div[1]/div/div/div[2]/a[1]"
                                        ).text
                                    except Exception as e:
                                        print("error corporation_address_text : " + str(e))

                                    # phone_number
                                    try:
                                        # corporation_phone_number_text
                                        phone_number += browser.find_element_by_class_name(
                                            "coord-numero"
                                        ).text
                                    except Exception as e:
                                        print('error corporation_phone_number_text : ' + str(e))

                                    # website
                                    try:
                                        website += browser.find_element_by_xpath(
                                            "/html/body/main/div[2]/section/div[6]/div[1]/div[1]/div/div/div[3]/a/span[2]"
                                        ).text
                                    except Exception as e:
                                        print("error website : " + str(e))

                                    # email
                                    try:
                                        email += "'contact@" + browser.find_element_by_xpath(
                                            "/html/body/main/div[2]/section/div[6]/div[1]/div[1]/div/div/div[3]/a/span[2]"
                                        ).text \
                                            .replace("https://www.", "") \
                                            .replace("http://www.", "") \
                                            .replace("https://", "") \
                                            .replace("http://", "") + "',"
                                    except Exception as e:
                                        print("error email_text : " + str(e))

                                    # activite
                                    try:
                                        # Print the activite_text
                                        activite += browser.find_element_by_xpath(
                                            "/html/body/main/div[2]/section/div[2]/div[1]/div[1]/div/div[2]/div/span"
                                        ).text
                                    except Exception as e:
                                        print('error activite_text : ' + str(e))

                                    # siren
                                    try:
                                        # Click on the "Informations financières et juridiques" button
                                        informations_financieres_juridiques_button = browser.find_element_by_xpath(
                                            "/html/body/main/div[2]/section/div[6]/div[1]/div[11]/h2/button"
                                        )
                                        informations_financieres_juridiques_button.click()

                                        time.sleep(10)

                                        # Print the siren
                                        siren += browser.find_element_by_xpath(
                                            "/html/body/main/div[2]/section/div[6]/div[1]/div[11]/div/dl[2]/dd[1]/strong"
                                        ).text
                                    except Exception as e:
                                        print('error siren_text : ' + str(e))

                                    # lien_societe_com
                                    # presence of the chairman
                                    try:
                                        if siren != '':
                                            url = "https://www.societe.com/cgi-bin/search?champs=" + siren

                                            payload = {}

                                            headers = {
                                                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '
                                                              'AppleWebKit/537.36 (KHTML, like Gecko) '
                                                              'Chrome/51.0.2704.103'
                                            }

                                            # Request the content of a page from the url
                                            html = requests.request("GET", url, headers=headers, data=payload)

                                            # Parse the content of html_doc
                                            soup = BeautifulSoup(html.content, 'html.parser')

                                            for i in range(1, 20):
                                                if soup.select_one("#dir" + str(i)) is not None:
                                                    president = soup.select_one("#dir" + str(i)) \
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
                                    except Exception as e:
                                        print('error siren : ' + str(e))

                                    x = {
                                        "raison_sociale": raison_sociale,
                                        "adresse_postale": adresse_postale,
                                        "phone_number": phone_number,
                                        "website": website,
                                        "email": email,
                                        "presence": presence,
                                        "page_jaune": url_company,
                                        "region": element.get('region'),
                                        "activite": activite,
                                        "siren": siren,
                                        "lien_societe_com": lien_societe_com,
                                        "president": president
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
                                                sql = "INSERT INTO `contacts_pour_excel` (" \
                                                      "`raison_sociale`, " \
                                                      "`adresse_postale`, " \
                                                      "`phone_number`, " \
                                                      "`website`, " \
                                                      "`email`, " \
                                                      "`presence`, " \
                                                      "`page_jaune`, " \
                                                      "`region`, " \
                                                      "`activite`, " \
                                                      "`siren`, " \
                                                      "`lien_societe_com`, " \
                                                      "`president`) VALUE (%s, %s, %s, %s, %s, %s, %s, " \
                                                      "%s, %s, %s, %s, %s)"

                                                cursor.execute(sql, (
                                                    x.get('raison_sociale'),
                                                    x.get('adresse_postale'),
                                                    x.get('phone_number'),
                                                    x.get('website'),
                                                    x.get('email'),
                                                    x.get('presence'),
                                                    x.get('page_jaune'),
                                                    x.get('region'),
                                                    x.get('activite'),
                                                    x.get('siren'),
                                                    x.get('lien_societe_com'),
                                                    x.get('president')
                                                ))

                                                connection.commit()

                                                print(str(i_1)
                                                      + " corporation : " + x.get('raison_sociale')
                                                      + " ; presence of the chairman : " + x.get('presence')
                                                      + " ; activite : " + x.get('activite')
                                                      + " ; siren : " + x.get('siren')
                                                      + " ; president : " + x.get('president'))

                                                connection.close()
                                            except Exception as e:
                                                print(str(i_1) + " The record already exists : " + str(e))
                                                connection.close()
                                    except Exception as e:
                                        print("Problem connection MySQL : " + str(e))
                                except Exception as e:
                                    print("error url_page_1 : " + str(e))

                                browser.quit()
                                print("browser closed url_company")

                                time.sleep(5)

                                i_1 += 1
                        except Exception as e:
                            print("error url_of_one_page_of_companies : " + str(e))
                else:
                    print("number of pages < 1")
            except Exception as e:
                print("error element : " + str(e))


if __name__ == '__main__':
    unittest.main()
