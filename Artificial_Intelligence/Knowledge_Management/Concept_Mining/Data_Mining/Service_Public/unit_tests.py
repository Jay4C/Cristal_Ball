import unittest
import requests
from bs4 import BeautifulSoup
import time
import csv


class UnitTestsServicePublic(unittest.TestCase):
    def test_extract_cerfa_number(self):
        print("test_extract_cerfa_number")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url_cerfa_number = "https://www.service-public.fr/particuliers/vosdroits/R16024"

        # Request the content of a page from the url
        html_cerfa_number = requests.get(url_cerfa_number, headers=headers)

        time.sleep(3)

        # Parse the content of html_doc
        soup = BeautifulSoup(html_cerfa_number.content, 'html.parser')

        if soup.find("span", {"class": "cerfa"}) is not None:
            print("cerfa number : " + soup.find("span", {"class": "cerfa"}).text.replace("Cerfa n° ", "").split("*")[0])
        else:
            print("no cerfa number")

    def test_extract_cerfa_number_for_one_filter_in_csv_file(self):
        print("test_extract_cerfa_number_for_one_filter_in_csv_file")

        start_page = 1
        end_page = 6
        filter = "papiers%20-%20citoyennete"
        start_id = 33663
        numero_hierarchique = 30

        date_de_debut = "30/03/2021"
        date_de_fin = "30/03/2021"
        avancee = "0"
        couleur = "#000000"

        base_url = "https://www.service-public.fr/particuliers/recherche?keyword=&rubricFilter=serviceEnLigne&rubricTypeFilter=formulaire&themeFilter=" + filter + "&page="

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        lines = list()

        for i in range(start_page, end_page):
            html = requests.get(base_url + str(i), headers=headers)

            soup = BeautifulSoup(html.content, 'html.parser')

            if soup.find("li", {"class": "result-item"}) is not None:
                items = soup.find_all("li", {"class": "result-item"})

                for item in items:
                    url_cerfa_number = item.find("a").get("href")

                    # Request the content of a page from the url
                    html_cerfa_number = requests.get(url_cerfa_number, headers=headers)

                    # Parse the content of html_doc
                    soup_cerfa_number = BeautifulSoup(html_cerfa_number.content, 'html.parser')

                    if soup_cerfa_number.find("span", {"class": "cerfa"}) is not None:
                        cerfa_number = soup_cerfa_number.find("span", {"class": "cerfa"}).text.replace("Cerfa n° ", "").split("*")[0]

                        start_id += 2

                        line = {
                            "ID": start_id,
                            "Nom": cerfa_number,
                            "Date de début": date_de_debut,
                            "Date de fin": date_de_fin,
                            "Durée": 1,
                            "Avancée": avancee,
                            "Coût": 0,
                            "Responsable": "",
                            "Prédécesseurs": "",
                            "Numéro hiérarchique": "1.1.1.1.1.4.1.2.1." + str(numero_hierarchique),
                            "Ressources": "",
                            "Assignments": "",
                            "Nouvelle tâche": couleur,
                            "Lien internet": "",
                            "Notes": url_cerfa_number
                        }

                        print("new row : " + str(line))

                        lines.append(line)

                        numero_hierarchique += 1
                    else:
                        print("no cerfa number")
            else:
                print("no li class result-item")

        with open(filter.replace("%20", "").replace("-", "") + '.csv', 'w', newline='', encoding="utf8") as file:
                    fieldnames = [
                        "ID",
                        "Nom",
                        "Date de début",
                        "Date de fin",
                        "Durée",
                        "Avancée",
                        "Coût",
                        "Responsable",
                        "Prédécesseurs",
                        "Numéro hiérarchique",
                        "Ressources",
                        "Assignments",
                        "Nouvelle tâche",
                        "Lien internet",
                        "Notes"
                    ]
                    writer = csv.DictWriter(file, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(lines)

    def test_extract_cerfa_number_for_all_filter_in_csv_file(self):
        print("test_extract_cerfa_number_for_one_filter_in_csv_file")
        filters = [
            {
                'start_page': 1,
                'end_page': 6,
                'filter': 'papiers%20-%20citoyennete',
                'start_id': 33663,
                'base_numero_hierarchique': '1.1.1.1.1.4.1.2.1.',
                'start_numero_hierarchique': 30
            },
            {
                'start_page': 1,
                'end_page': 9,
                'filter': 'famille',
                'start_id': 33595,
                'base_numero_hierarchique': '1.1.1.1.1.4.1.2.2.',
                'start_numero_hierarchique': 2
            },
            {
                'start_page': 1,
                'end_page': 7,
                'filter': 'social%20-%20sante',
                'start_id': 33596,
                'base_numero_hierarchique': '1.1.1.1.1.4.1.2.3.',
                'start_numero_hierarchique': 2
            },
            {
                'start_page': 1,
                'end_page': 7,
                'filter': 'travail',
                'start_id': 33597,
                'base_numero_hierarchique': '1.1.1.1.1.4.1.2.4.',
                'start_numero_hierarchique': 2
            },
            {
                'start_page': 1,
                'end_page': 6,
                'filter': 'logement',
                'start_id': 32686,
                'base_numero_hierarchique': '1.1.1.1.1.4.1.2.5.',
                'start_numero_hierarchique': 7
            },
            {
                'start_page': 1,
                'end_page': 2,
                'filter': 'transports',
                'start_id': 33598,
                'base_numero_hierarchique': '1.1.1.1.1.4.1.2.6.',
                'start_numero_hierarchique': 2
            },
            {
                'start_page': 1,
                'end_page': 5,
                'filter': 'argent',
                'start_id': 32259,
                'base_numero_hierarchique': '1.1.1.1.1.4.1.2.7.',
                'start_numero_hierarchique': 10
            },
            {
                'start_page': 1,
                'end_page': 5,
                'filter': 'justice',
                'start_id': 33599,
                'base_numero_hierarchique': '1.1.1.1.1.4.1.2.8.',
                'start_numero_hierarchique': 2
            },
            {
                'start_page': 1,
                'end_page': 2,
                'filter': 'etranger',
                'start_id': 33600,
                'base_numero_hierarchique': '1.1.1.1.1.4.1.2.9.',
                'start_numero_hierarchique': 2
            },
            {
                'start_page': 1,
                'end_page': 6,
                'filter': 'loisirs',
                'start_id': 33601,
                'base_numero_hierarchique': '1.1.1.1.1.4.1.2.10.',
                'start_numero_hierarchique': 2
            }
        ]

        date_de_debut = "30/03/2021"
        date_de_fin = "30/03/2021"
        avancee = "0"
        couleur = "#000000"

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        lines = list()

        for filter in filters:
            base_url = "https://www.service-public.fr/particuliers/recherche?keyword=&rubricFilter=serviceEnLigne&rubricTypeFilter=formulaire&themeFilter=" + filter.get('filter') + "&page="

            start_id = filter.get('start_id')

            numero_hierarchique = filter.get('start_numero_hierarchique')

            for i in range(filter.get('start_page'), filter.get('end_page') + 1):
                html = requests.get(base_url + str(i), headers=headers)

                soup = BeautifulSoup(html.content, 'html.parser')

                if soup.find("li", {"class": "result-item"}) is not None:
                    items = soup.find_all("li", {"class": "result-item"})

                    for item in items:
                        url_cerfa_number = item.find("a").get("href")

                        # Request the content of a page from the url
                        html_cerfa_number = requests.get(url_cerfa_number, headers=headers)

                        # Parse the content of html_doc
                        soup_cerfa_number = BeautifulSoup(html_cerfa_number.content, 'html.parser')

                        if soup_cerfa_number.find("span", {"class": "cerfa"}) is not None:
                            cerfa_number = soup_cerfa_number.find("span", {"class": "cerfa"}).text.replace("Cerfa n° ", "").split("*")[0]

                            start_id += 2

                            line = {
                                "ID": start_id,
                                "Nom": cerfa_number,
                                "Date de début": date_de_debut,
                                "Date de fin": date_de_fin,
                                "Durée": 1,
                                "Avancée": avancee,
                                "Coût": 0,
                                "Responsable": "",
                                "Prédécesseurs": "",
                                "Numéro hiérarchique": filter.get('base_numero_hierarchique') + str(numero_hierarchique),
                                "Ressources": "",
                                "Assignments": "",
                                "Nouvelle tâche": couleur,
                                "Lien internet": "",
                                "Notes": url_cerfa_number
                            }

                            print("new row : " + str(line))

                            lines.append(line)

                            numero_hierarchique += 1
                        else:
                            print("no cerfa number")
                else:
                    print("no li class result-item")

        with open('cerfa_number.csv', 'w', newline='', encoding="utf8") as file:
                        fieldnames = [
                            "ID",
                            "Nom",
                            "Date de début",
                            "Date de fin",
                            "Durée",
                            "Avancée",
                            "Coût",
                            "Responsable",
                            "Prédécesseurs",
                            "Numéro hiérarchique",
                            "Ressources",
                            "Assignments",
                            "Nouvelle tâche",
                            "Lien internet",
                            "Notes"
                        ]
                        writer = csv.DictWriter(file, fieldnames=fieldnames)
                        writer.writeheader()
                        writer.writerows(lines)


if __name__ == '__main__':
    unittest.main()
