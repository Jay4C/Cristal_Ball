import time
import unittest
import xlsxwriter
import requests
import gzip
import os
import json
from bs4 import BeautifulSoup
import pymysql.cursors


class UnitTestsDataCreationCadastreFrance(unittest.TestCase):
    def test_download_one_zip_file_for_one_city_about_parcelles_from_cadastre_data_gouv_fr(self):
        print("test_download_one_zip_file_for_one_city_about_parcelles_from_cadastre_data_gouv_fr")

        code_insee_departement = "01"

        code_insee_commune = "01001"

        url_zip_file_for_parcelles = "https://cadastre.data.gouv.fr/data/etalab-cadastre/latest/geojson/communes/" \
                                     + code_insee_departement + "/" \
                                     + code_insee_commune + "/cadastre-" + code_insee_commune + "-parcelles.json.gz"

        resp = requests.get(url_zip_file_for_parcelles, stream=True)

        zname = "cadastre-" + code_insee_commune + "-parcelles.json.gz"
        gz_file = open(zname, 'wb')
        gz_file.write(resp.content)
        gz_file.close()

    def test_extract_one_zip_file_for_one_city_about_parcelles_from_cadastre_data_gouv_fr(self):
        print("test_extract_one_zip_file_for_one_city_about_parcelles_from_cadastre_data_gouv_fr")

        input = gzip.GzipFile("cadastre-01001-parcelles.json.gz", 'rb')
        s = input.read()
        input.close()

        output = open("cadastre-01001-parcelles.json", 'wb')
        output.write(s)
        output.close()

    def test_download_and_extract_one_gz_file_for_one_city_about_parcelles_from_cadastre_data_gouv_fr(self):
        print("test_download_and_extract_one_gz_file_for_one_city_about_parcelles_from_cadastre_data_gouv_fr")

        about = "parcelles"

        code_insee_departement = "01"

        code_insee_commune = "01001"

        url_zip_file_for_parcelles = "https://cadastre.data.gouv.fr/data/etalab-cadastre/2020-07-01/geojson/communes/" \
                                     + code_insee_departement + "/" \
                                     + code_insee_commune + "/cadastre-" + code_insee_commune + "-" + about + ".json.gz"

        resp = requests.get(url_zip_file_for_parcelles, stream=True)

        # donwload gz file
        gz_filename = "cadastre-" + code_insee_commune + "-" + about + ".json.gz"
        gz_file = open(gz_filename, 'wb')
        gz_file.write(resp.content)
        gz_file.close()

        # extract json file
        input_file = gzip.GzipFile(gz_filename, 'rb')
        s = input_file.read()
        input_file.close()

        output_file = open(gz_filename[:-3], 'wb')
        output_file.write(s)
        output_file.close()

    def test_delete_one_gz_file_for_one_city_about_parcelles_from_cadastre_gouv_fr(self):
        print("test_delete_one_gz_file_for_one_city_about_parcelles_from_cadastre_gouv_fr")

        os.remove("cadastre-01001-parcelles.json.gz")

    def test_download_and_extract_one_gz_file_for_one_city_about_batiments_from_cadastre_data_gouv_fr(self):
        print("test_download_and_extract_one_gz_file_for_one_city_about_batiments_from_cadastre_data_gouv_fr")

        about = "batiments"

        code_insee_departement = "01"

        code_insee_commune = "01001"

        url_zip_file_for_batiments = "https://cadastre.data.gouv.fr/data/etalab-cadastre/latest/geojson/communes/" \
                                     + code_insee_departement + "/" \
                                     + code_insee_commune + "/cadastre-" + code_insee_commune + "-" + about + ".json.gz"

        resp = requests.get(url_zip_file_for_batiments, stream=True)

        # donwload gz file
        gz_filename = "cadastre-" + code_insee_commune + "-" + about + ".json.gz"
        gz_file = open(gz_filename, 'wb')
        gz_file.write(resp.content)
        gz_file.close()

        # extract json file
        input_file = gzip.GzipFile(gz_filename, 'rb')
        s = input_file.read()
        input_file.close()

        output_file = open(gz_filename[:-3], 'wb')
        output_file.write(s)
        output_file.close()

    def test_download_and_extract_one_gz_file_for_one_city_about_feuilles_from_cadastre_data_gouv_fr(self):
        print("test_download_and_extract_one_gz_file_for_one_city_about_feuilles_from_cadastre_data_gouv_fr")

        about = "feuilles"

        code_insee_departement = "01"

        code_insee_commune = "01001"

        url_zip_file_for_batiments = "https://cadastre.data.gouv.fr/data/etalab-cadastre/2020-07-01/geojson/communes/" \
                                     + code_insee_departement + "/" \
                                     + code_insee_commune + "/cadastre-" + code_insee_commune + "-" + about + ".json.gz"

        resp = requests.get(url_zip_file_for_batiments, stream=True)

        # donwload gz file
        gz_filename = "cadastre-" + code_insee_commune + "-" + about + ".json.gz"
        gz_file = open(gz_filename, 'wb')
        gz_file.write(resp.content)
        gz_file.close()

        # extract json file
        input_file = gzip.GzipFile(gz_filename, 'rb')
        s = input_file.read()
        input_file.close()

        output_file = open(gz_filename[:-3], 'wb')
        output_file.write(s)
        output_file.close()

    def test_delete_one_gz_file_for_one_city_about_batiments_from_cadastre_gouv_fr(self):
        print("test_delete_one_gz_file_for_one_city_about_parcelles_from_cadastre_gouv_fr")

        os.remove("cadastre-01001-batiments.json.gz")

    def test_download_and_extract_and_delete_one_gz_file_for_one_city_about_batiments_and_parcelles_into_one_folder_from_cadastre_data_gouv_fr(self):
        print("test_download_and_extract_and_delete_one_gz_file_for_one_city_about_batiments_and_parcelles_into_one_folder_from_cadastre_data_gouv_fr")

        code_insee_departement = "01"

        code_insee_commune = "01001"

        abouts = [
            "parcelles",
            "batiments"
        ]

        # Create target Directory if don't exist
        if not os.path.exists("C:\\Users\\DELL\\Downloads\\Cadastre_Communes\\" + str(code_insee_commune)):
            os.mkdir("C:\\Users\\DELL\\Downloads\\Cadastre_Communes\\" + str(code_insee_commune))
            print("Directory ", "C:\\Users\\DELL\\Downloads\\Cadastre_Communes\\" + str(code_insee_commune), " Created ")
        else:
            print("Directory ", "C:\\Users\\DELL\\Downloads\\Cadastre_Communes\\" + str(code_insee_commune), " already exists")

        for about in abouts:
            url_zip_file = "https://cadastre.data.gouv.fr/data/etalab-cadastre/2020-07-01/geojson/communes/" \
                                         + code_insee_departement + "/" \
                                         + code_insee_commune + "/cadastre-" + code_insee_commune + "-" + about + ".json.gz"

            resp = requests.get(url_zip_file, stream=True)

            # download gz file
            gz_filename = "cadastre-" + code_insee_commune + "-" + about + ".json.gz"
            gz_file = open(gz_filename, 'wb')
            gz_file.write(resp.content)
            gz_file.close()

            # extract json file
            input_file = gzip.GzipFile(gz_filename, 'rb')
            s = input_file.read()
            input_file.close()
            output_file = open("C:\\Users\\DELL\\Downloads\\Cadastre_Communes\\" + str(code_insee_commune) + "\\" + gz_filename[:-3], 'wb')
            output_file.write(s)
            output_file.close()

            # delete gz file
            os.remove(gz_filename)

    def test_download_and_extract_and_delete_one_gz_file_for_some_cities_about_batiments_and_parcelles_into_one_specific_folder_from_cadastre_data_gouv_fr(self):
        print("test_download_and_extract_and_delete_one_gz_file_for_all_cities_with_less_1000_people_about_batiments_and_parcelles_into_one_specific_folder_from_cadastre_data_gouv_fr")

        url = "https://geo.api.gouv.fr/communes?fields=nom,code,codesPostaux,codeDepartement,codeRegion,population&format=json&geometry=centre"

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)

        communes = response.json()

        for commune in communes:
            try:
                if commune['population'] < 100 and commune['code'] != '77304':
                    print("ville : " + commune['nom']
                          + " _ code insee commune : " + commune['code']
                          + " _ population : " + str(commune['population']))

                    code_insee_departement = commune['codeDepartement']

                    code_insee_commune = commune['code']

                    # Create target Directory if don't exist
                    if not os.path.exists("C:\\Users\\DELL\\Downloads\\Cadastre_Communes\\" + str(code_insee_commune)):
                        os.mkdir("C:\\Users\\DELL\\Downloads\\Cadastre_Communes\\" + str(code_insee_commune))
                        print("Directory ", "C:\\Users\\DELL\\Downloads\\Cadastre_Communes\\" + str(code_insee_commune), " Created ")
                    else:
                        print("Directory ", "C:\\Users\\DELL\\Downloads\\Cadastre_Communes\\" + str(code_insee_commune), " already exists")

                    abouts = [
                        "parcelles",
                        "batiments"
                    ]

                    for about in abouts:
                        url_zip_file = "https://cadastre.data.gouv.fr/data/etalab-cadastre/2020-07-01/geojson/communes/" \
                                                     + code_insee_departement + "/" \
                                                     + code_insee_commune + "/cadastre-" \
                                                     + code_insee_commune + "-" + about + ".json.gz"

                        resp = requests.get(url_zip_file, stream=True)

                        # donwload gz file
                        gz_filename = "cadastre-" + code_insee_commune + "-" + about + ".json.gz"
                        gz_file = open(gz_filename, 'wb')
                        gz_file.write(resp.content)
                        gz_file.close()

                        # extract json file
                        input_file = gzip.GzipFile(gz_filename, 'rb')
                        s = input_file.read()
                        input_file.close()
                        output_file = open("C:\\Users\\DELL\\Downloads\\Cadastre_Communes\\"
                                           + str(code_insee_commune) + "\\" + gz_filename[:-3], 'wb')
                        output_file.write(s)
                        output_file.close()

                        # delete gz file
                        os.remove(gz_filename)
            except Exception as e:
                print("error : " + str(e))

    def test_write_url_path_for_some_city_about_batiments_and_parcelles_into_txt_file(self):
        print("test_write_url_path_for_some_city_about_batiments_and_parcelles_into_txt_file")

        # display all directory names for each city from Cadastre_France folder
        directories = os.listdir("C:\\Users\\DELL\\Downloads\\Cadastre_Communes")

        f = open("urls_path.txt", "w")

        for directory in directories:
            path_parcelles = "path('cadastre_" + directory + "_parcelles_json', views.cadastre_" + directory + "_parcelles_json, name='cadastre_" + directory + "_parcelles_json'),"
            path_batiments = "path('cadastre_" + directory + "_batiments_json', views.cadastre_" + directory + "_batiments_json, name='cadastre_" + directory + "_batiments_json'),"

            f.write(path_parcelles + "\n")
            f.write(path_batiments + "\n")

        f.close()

    def test_write_views_functions_for_some_city_about_batiments_and_parcelles_into_txt_file(self):
        print("test_write_views_functions_for_some_city_about_batiments_and_parcelles_into_txt_file")

        # display all directory names for each city from Cadastre_France folder
        directories = os.listdir("C:\\Users\\DELL\\Downloads\\Cadastre_Communes")

        f = open("views_functions.txt", "w")

        for directory in directories:
            # function for parcelles
            f.write("def cadastre_" + directory + "_parcelles_json(request):" + "\n")
            f.write("\t" + "with open('static/contents/static/" + directory + "/cadastre-" + directory + "-parcelles.json') as json_file:" + "\n")
            f.write("\t\t" + "data = json.load(json_file)" + "\n")
            f.write("\t" + "return JsonResponse(data, safe=False)" + "\n\n\n")

            # function for batiments
            f.write("def cadastre_" + directory + "_batiments_json(request):" + "\n")
            f.write("\t" + "with open('static/contents/static/" + directory + "/cadastre-" + directory + "-batiments.json') as json_file:" + "\n")
            f.write("\t\t" + "data = json.load(json_file)" + "\n")
            f.write("\t" + "return JsonResponse(data, safe=False)" + "\n\n\n")

        f.close()

    def test_write_getjson_html_for_some_city_about_batiments_and_parcelles_into_txt_file(self):
        print("test_write_getjson_html_for_some_city_about_batiments_and_parcelles_into_txt_file")

        # display all directory names for each city from Cadastre_France folder
        directories = os.listdir("C:\\Users\\DELL\\Downloads\\Cadastre_Communes")

        f = open("javascript_get_json.txt", "w")

        for directory in directories:
            #  javascript for parcelles
            f.write("// cadastre_" + directory + "_parcelles_json" + "\n")
            f.write('$.getJSON("cadastre_' + directory + '_parcelles_json", function(data_cadastre_' + directory + '_parcelles_json) {' + '\n')
            f.write("\t" + "var features_data_cadastre_" + directory + "_parcelles_json = data_cadastre_" + directory + "_parcelles_json.features;" + "\n")
            f.write("\t" + "L.geoJSON(features_data_cadastre_" + directory + "_parcelles_json, {color: 'blue'}).addTo(lands_for_injecting_gas_in_france_map);" + "\n")
            f.write("});" + "\n\n")

            # javascript for batiments
            f.write("// cadastre_" + directory + "_batiments_json" + "\n")
            f.write('$.getJSON("cadastre_' + directory + '_batiments_json", function(data_cadastre_' + directory + '_batiments_json) {' + '\n')
            f.write("\t" + "var features_data_cadastre_" + directory + "_batiments_json = data_cadastre_" + directory + "_batiments_json.features;" + "\n")
            f.write("\t" + "L.geoJSON(features_data_cadastre_" + directory + "_batiments_json, {color: 'red'}).addTo(lands_for_injecting_gas_in_france_map);" + "\n")
            f.write("});" + "\n\n")

        f.close()

    def test_show_all_cities_with_a_gas_distribution_network_in_france(self):
        print("test_show_all_cities_with_a_gas_network_in_france")

        array_code_insee_commune_desservies_par_gaz = []
        f = open('communes-desservies-en-gaz.json', "r")
        data = json.loads(f.read())
        for feature in data['features']:
            code_insee_commune = feature['properties']['code_insee_commune'][1:]
            array_code_insee_commune_desservies_par_gaz.append(str(code_insee_commune))
            print(str(code_insee_commune))
        f.close()

    def test_show_all_cities_with_some_biogas_stations(self):
        print("test_show_all_cities_with_some_biogas_stations")

        array_code_insee_commune_biogas = []
        f = open('les-sites-dinjection-de-biomethane-en-france.json', "r")
        data = json.loads(f.read())
        for feature in data['features']:
            code_insee_commune = feature['properties']['code_commune']
            array_code_insee_commune_biogas.append(str(code_insee_commune))
            print(str(code_insee_commune))
        f.close()

    def test_show_all_parcelles_with_at_least_1000_square_meters_for_some_departments(self):
        print("test_show_all_parcelles_with_at_least_1000_square_meters")

        url = "https://geo.api.gouv.fr/communes?fields=nom,code,codesPostaux,codeDepartement,codeRegion,population&format=json&geometry=centre"

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)

        communes = response.json()

        departements = ["77", "78", "91", "95"]

        about = "parcelles"

        for commune in communes:
            code_insee_departement = commune['codeDepartement']

            code_insee_commune = commune['code']

            if code_insee_departement in departements:
                url_zip_file_for_parcelles = "https://cadastre.data.gouv.fr/data/etalab-cadastre/2020-07-01/geojson/communes/" \
                                             + code_insee_departement + "/" \
                                             + code_insee_commune + "/cadastre-" + code_insee_commune + "-" + about + ".json.gz"

                resp = requests.get(url_zip_file_for_parcelles, stream=True)

                # donwload gz file
                gz_filename = "cadastre-" + code_insee_commune + "-" + about + ".json.gz"
                gz_file = open(gz_filename, 'wb')
                gz_file.write(resp.content)
                gz_file.close()

                # extract json file
                input_file = gzip.GzipFile(gz_filename, 'rb')
                s = input_file.read()
                input_file.close()
                output_file = open(gz_filename[:-3], 'wb')
                output_file.write(s)
                output_file.close()

                output_file = open(gz_filename[:-3])
                data = json.loads(output_file.read())

                for feature in data['features']:
                    properties = feature['properties']

                    if properties['contenance'] > 1000:
                        print(properties)

                output_file.close()

                # delete gz file and json file
                os.remove(gz_filename[:-3])
                os.remove(gz_filename)

    def test_show_all_cities_with_train_station_for_travellers(self):
        print('test_show_all_cities_with_train_station_for_travellers')

        # array of the cities have at least one train station for travellers
        array_code_insee_commune_with_train_station_for_travellers = []
        f = open('gares_ferroviaires_de_tous_types_exploitees_ou_non.json', "r")
        data = json.loads(f.read())
        for feature in data:
            code_postal = feature['fields']['cp']

            nom = feature['fields']['ville']

            url = "https://geo.api.gouv.fr/communes?codePostal=" + str(code_postal)

            payload = {}
            headers = {}

            response = requests.request("GET", url, headers=headers, data=payload)

            informations_pour_une_commune_avec_son_code_postal = response.json()

            for commune in informations_pour_une_commune_avec_son_code_postal:
                if commune['nom'] == nom and 'Voyageur' in feature['fields']['nature']:
                    array_code_insee_commune_with_train_station_for_travellers.append(str(commune['code']))
                    print(commune)
        f.close()

    def test_show_all_suitable_parcelles_for_injecting_gas_in_france_into_excel_without_archive_url(self):
        print("test_show_all_suitable_parcelles_for_injecting_gas_in_france_into_excel")

        suitable_lands = []

        try:
            # array of the cities connected to a gas grid
            array_code_insee_commune_desservies_par_gaz = []
            f = open('communes-desservies-en-gaz.json', "r")
            data = json.loads(f.read())
            for feature in data['features']:
                code_insee_commune = feature['properties']['code_insee_commune'][1:]
                array_code_insee_commune_desservies_par_gaz.append(str(code_insee_commune))
            f.close()

            # array of the cities that have stations for injecting biogas into a gas grid
            array_code_insee_commune_biogas = []
            f = open('les-sites-dinjection-de-biomethane-en-france.json', "r")
            data = json.loads(f.read())
            for feature in data['features']:
                code_insee_commune = feature['properties']['code_commune']
                array_code_insee_commune_biogas.append(str(code_insee_commune))
            f.close()

            # array of the cities have at least one train station for travellers
            array_code_insee_commune_with_train_station_for_travellers = []
            f = open('gares_ferroviaires_de_tous_types_exploitees_ou_non.json', "r")
            data = json.loads(f.read())
            for feature in data:
                code_postal = feature['fields']['cp']

                nom = feature['fields']['ville']

                url = "https://geo.api.gouv.fr/communes?codePostal=" + str(code_postal)

                payload = {}
                headers = {}

                response = requests.request("GET", url, headers=headers, data=payload)

                informations_pour_une_commune_avec_son_code_postal = response.json()

                for commune in informations_pour_une_commune_avec_son_code_postal:
                    if commune['nom'] == nom and 'Voyageur' in feature['fields']['nature']:
                        array_code_insee_commune_with_train_station_for_travellers.append(str(commune['code']))
            f.close()

            url = "https://geo.api.gouv.fr/communes?fields=nom,code,codesPostaux,codeDepartement,codeRegion,population&format=json&geometry=centre"

            payload = {}

            headers = {}

            response_communes = requests.request("GET", url, headers=headers, data=payload)

            communes = response_communes.json()

            about_parcelles = "parcelles"

            print('start main for loop')

            for commune in communes:
                try:
                    code_insee_departement = commune['codeDepartement']

                    code_insee_commune = commune['code']

                    population = commune['population']

                    # Communes desservies par le gaz : ok
                    # Communes ayant un site de biogaz : ok
                    # Communes ayant moins de 1000 haibtants : ok
                    # Communes ayant au moins une gare de train pour les voyageurs : ok
                    if (code_insee_commune in array_code_insee_commune_desservies_par_gaz) \
                            and ((code_insee_commune in array_code_insee_commune_biogas)
                                 or
                                 (code_insee_commune in array_code_insee_commune_with_train_station_for_travellers)) \
                            and population <= 1000:
                        url_zip_file_for_parcelles = "https://cadastre.data.gouv.fr/data/etalab-cadastre/2020-07-01/geojson/communes/" \
                                                     + code_insee_departement + "/" \
                                                     + code_insee_commune + "/cadastre-" + code_insee_commune \
                                                     + "-" + about_parcelles + ".json.gz"

                        resp = requests.get(url_zip_file_for_parcelles, stream=True)

                        # donwload gz file
                        gz_filename = "cadastre-" + code_insee_commune + "-" + about_parcelles + ".json.gz"
                        gz_file = open(gz_filename, 'wb')
                        gz_file.write(resp.content)
                        gz_file.close()

                        # extract json file
                        input_file = gzip.GzipFile(gz_filename, 'rb')
                        s = input_file.read()
                        input_file.close()
                        output_file = open(gz_filename[:-3], 'wb')
                        output_file.write(s)
                        output_file.close()

                        json_file = open(gz_filename[:-3])
                        data = json.loads(json_file.read())

                        for feature in data['features']:
                            try:
                                properties = feature['properties']

                                coordinates = feature['geometry']['coordinates']

                                # Terrain mesurant au moins 10000 mètres carrés : ok
                                if properties['contenance'] >= 10000:
                                    try:
                                        lon = str(coordinates[0][0][0])

                                        lat = str(coordinates[0][0][1])

                                        url = "https://api-adresse.data.gouv.fr/reverse/?lon=" + lon + "&lat=" + lat

                                        payload = {}

                                        headers = {}

                                        response_adresse_postale_reverse = requests.request("GET", url,
                                                                                            headers=headers,
                                                                                            data=payload)

                                        json_format_adresse_postale_reverse = json.loads(
                                            response_adresse_postale_reverse.text)

                                        if len(json_format_adresse_postale_reverse['features']) != 0:
                                            for feature_adresse in json_format_adresse_postale_reverse['features']:
                                                try:
                                                    if feature_adresse['properties']['label'] != '':
                                                        # A python object (dict):
                                                        x = {
                                                            "adresse_postale": feature_adresse['properties']['label'],
                                                            "prefixe_parcelle": properties['prefixe'],
                                                            "section_parcelle": properties['section'],
                                                            "numero_parcelle": properties['numero'],
                                                            "contenance_parcelle": properties['contenance'],
                                                            "url_geoportail_carte": "https://www.geoportail.gouv.fr/carte",
                                                            "coordonnees_gps": "Coordonnées : " + lat + " " + lon
                                                        }

                                                        print("land : " + x.get('adresse_postale'))

                                                        suitable_lands.append(x)

                                                        break
                                                except Exception as e:
                                                    print('error feature_adresse : ' + str(e))
                                    except Exception as e:
                                        print('error coordinates : ' + str(e))
                            except Exception as e:
                                print('error feature : ' + str(e))

                        json_file.close()

                        # delete gz file and json file
                        os.remove(gz_filename[:-3])
                        os.remove(gz_filename)
                except Exception as e:
                    print("error commune : " + str(e))

            workbook = xlsxwriter.Workbook("Parcelles_RTG.xlsx")

            worksheet = workbook.add_worksheet('data')

            worksheet.write(0, 0, 'adresse postale')
            worksheet.write(0, 1, 'prefixe parcelle')
            worksheet.write(0, 2, 'section parcelle')
            worksheet.write(0, 3, 'numero parcelle')
            worksheet.write(0, 4, 'contenance parcelle')
            worksheet.write(0, 5, 'url geoportail carte')
            worksheet.write(0, 6, 'coordonnees gps')

            row = 1

            for lands in suitable_lands:
                worksheet.write(row, 0, lands['adresse_postale'])
                worksheet.write(row, 1, lands['prefixe_parcelle'])
                worksheet.write(row, 2, lands['section_parcelle'])
                worksheet.write(row, 3, lands['numero_parcelle'])
                worksheet.write(row, 4, lands['contenance_parcelle'])
                worksheet.write(row, 5, lands['url_geoportail_carte'])
                worksheet.write(row, 6, lands['coordonnees_gps'])

                row += 1

            workbook.close()
        except Exception as e:
            print('error main : ' + str(e))

    def test_show_all_suitable_parcelles_for_injecting_gas_in_france_into_excel_with_archive_url(self):
        print("test_show_all_suitable_parcelles_for_injecting_gas_in_france_into_excel")

        try:
            # array of the cities connected to a gas grid
            array_code_insee_commune_desservies_par_gaz = []
            f = open('communes-desservies-en-gaz.json', "r")
            data = json.loads(f.read())
            for feature in data['features']:
                code_insee_commune = feature['properties']['code_insee_commune'][1:]
                array_code_insee_commune_desservies_par_gaz.append(str(code_insee_commune))
            f.close()

            # array of the cities that have stations for injecting biogas into a gas grid
            array_code_insee_commune_biogas = []
            f = open('les-sites-dinjection-de-biomethane-en-france.json', "r")
            data = json.loads(f.read())
            for feature in data['features']:
                code_insee_commune = feature['properties']['code_commune']
                array_code_insee_commune_biogas.append(str(code_insee_commune))
            f.close()

            # array of the cities have at least one train station for travellers
            array_code_insee_commune_with_train_station_for_travellers = []
            f = open('gares_ferroviaires_de_tous_types_exploitees_ou_non.json', "r")
            data = json.loads(f.read())
            for feature in data:
                code_postal = feature['fields']['cp']

                nom = feature['fields']['ville']

                url = "https://geo.api.gouv.fr/communes?codePostal=" + str(code_postal)

                payload = {}
                headers = {}

                response = requests.request("GET", url, headers=headers, data=payload)

                informations_pour_une_commune_avec_son_code_postal = response.json()

                for commune in informations_pour_une_commune_avec_son_code_postal:
                    if commune['nom'] == nom and 'Voyageur' in feature['fields']['nature']:
                        array_code_insee_commune_with_train_station_for_travellers.append(str(commune['code']))
            f.close()

            url = "https://geo.api.gouv.fr/communes?fields=nom,code,codesPostaux,codeDepartement,codeRegion,population&format=json&geometry=centre"

            payload = {}

            headers = {}

            response_communes = requests.request("GET", url, headers=headers, data=payload)

            communes = response_communes.json()

            about_parcelles = "parcelles"

            print('start main for loop')

            workbook = xlsxwriter.Workbook("Parcelles_Injection_Methane_Synthese.xls")

            worksheet = workbook.add_worksheet('data')

            worksheet.write(0, 0, 'adresse postale')
            worksheet.write(0, 1, 'prefixe parcelle')
            worksheet.write(0, 2, 'section parcelle')
            worksheet.write(0, 3, 'numero parcelle')
            worksheet.write(0, 4, 'contenance parcelle')
            worksheet.write(0, 5, 'url geoportail carte')
            worksheet.write(0, 6, 'coordonnees gps')
            worksheet.write(0, 7, 'archive url document urbanisme')

            row = 1

            suitable_lands = []

            for commune in communes:
                try:
                    code_insee_departement = commune['codeDepartement']

                    code_insee_commune = commune['code']

                    population = commune['population']

                    # Communes desservies par le gaz : ok
                    # Communes ayant un site de biogaz : ok
                    # Communes ayant moins de 1000 haibtants : ok
                    # Communes ayant au moins une gare de train pour les voyageurs : ok
                    if (code_insee_commune in array_code_insee_commune_desservies_par_gaz) \
                            and ((code_insee_commune in array_code_insee_commune_biogas)
                                 or
                                 (code_insee_commune in array_code_insee_commune_with_train_station_for_travellers)) \
                            and population <= 1000:
                        url_zip_file_for_parcelles = "https://cadastre.data.gouv.fr/data/etalab-cadastre/2020-07-01/geojson/communes/" \
                                                     + code_insee_departement + "/" \
                                                     + code_insee_commune + "/cadastre-" + code_insee_commune + "-" + about_parcelles + ".json.gz"

                        resp = requests.get(url_zip_file_for_parcelles, stream=True)

                        # donwload gz file
                        gz_filename = "cadastre-" + code_insee_commune + "-" + about_parcelles + ".json.gz"
                        gz_file = open(gz_filename, 'wb')
                        gz_file.write(resp.content)
                        gz_file.close()

                        # extract json file
                        input_file = gzip.GzipFile(gz_filename, 'rb')
                        s = input_file.read()
                        input_file.close()
                        output_file = open(gz_filename[:-3], 'wb')
                        output_file.write(s)
                        output_file.close()

                        json_file = open(gz_filename[:-3])
                        data = json.loads(json_file.read())

                        for feature in data['features']:
                            try:
                                properties = feature['properties']

                                coordinates = feature['geometry']['coordinates']

                                # Terrain mesurant au moins 10000 mètres carrés : ok
                                if properties['contenance'] >= 10000:
                                    # Terrain constructible :
                                    geometry = str(feature['geometry']) \
                                        .replace('{', '%7B') \
                                        .replace('"', '%22') \
                                        .replace(':', '%3A') \
                                        .replace(' ', '%20') \
                                        .replace(',', '%2C') \
                                        .replace('[', '%5B') \
                                        .replace(']', '%5D') \
                                        .replace('}', '%7D')

                                    print(geometry)

                                    base_url = 'https://apicarto.ign.fr/api'

                                    api = '/gpu/document'

                                    url = base_url + api + '?geom=' + geometry

                                    payload = {}

                                    headers = {}

                                    response_document = requests.get(url, headers=headers, data=payload)

                                    json_format_document = json.loads(response_document.text)

                                    for feature_document in json_format_document['features']:
                                        if feature_document['properties']['du_type'] == 'PLU':
                                            id_document = feature_document['properties']['id']

                                            base_url = 'https://www.geoportail-urbanisme.gouv.fr/api'

                                            api = '/document/'

                                            url = base_url + api + id_document + '/details'

                                            payload = {}

                                            headers = {}

                                            response_id_document = requests.get(url, headers=headers, data=payload)

                                            json_format_id_document = json.loads(response_id_document.text)

                                            archive_url = json_format_id_document['archiveUrl']

                                            for coordinate in coordinates[0]:
                                                lon = str(coordinate[0])

                                                lat = str(coordinate[1])

                                                url = "https://api-adresse.data.gouv.fr/reverse/?lon=" + lon + "&lat=" + lat

                                                payload = {}

                                                headers = {}

                                                response_adresse_postale_reverse = requests.request("GET", url,
                                                                                                    headers=headers,
                                                                                                    data=payload)

                                                json_format_adresse_postale_reverse = json.loads(
                                                    response_adresse_postale_reverse.text)

                                                if len(json_format_adresse_postale_reverse['features']) != 0:
                                                    for feature_adresse in json_format_adresse_postale_reverse[
                                                        'features']:
                                                        if feature_adresse['properties']['label'] != '':
                                                            # A python object (dict):
                                                            x = {
                                                                "adresse_postale": feature_adresse['properties'][
                                                                    'label'],
                                                                "prefixe_parcelle": properties['prefixe'],
                                                                "section_parcelle": properties['section'],
                                                                "numero_parcelle": properties['numero'],
                                                                "contenance_parcelle": properties['contenance'],
                                                                "url_geoportail_carte": "https://www.geoportail.gouv.fr/carte",
                                                                "coordonnees_gps": "Coordonnées : " + lat + " " + lon,
                                                                "archive_url": archive_url
                                                            }

                                                            suitable_lands.append(x)

                                                            break
                                                    break

                                    # Terrain n'ayant pas de bâti :
                            except Exception as e:
                                print('error feature : ' + str(e))

                        json_file.close()

                        # delete gz file and json file
                        os.remove(gz_filename[:-3])
                        os.remove(gz_filename)
                except Exception as e:
                    print("error commune : " + str(e))

            for lands in suitable_lands:
                worksheet.write(row, 0, lands['adresse_postale'])
                worksheet.write(row, 1, lands['prefixe_parcelle'])
                worksheet.write(row, 2, lands['section_parcelle'])
                worksheet.write(row, 3, lands['numero_parcelle'])
                worksheet.write(row, 4, lands['contenance_parcelle'])
                worksheet.write(row, 5, lands['url_geoportail_carte'])
                worksheet.write(row, 6, lands['coordonnees_gps'])
                worksheet.write(row, 7, lands['archive_url'])

                row += 1

            workbook.close()
        except Exception as e:
            print('error main : ' + str(e))

    def test_show_all_suitable_biogas_sites_in_excel(self):
        print('test_show_all_suitable_biogas_sites_in_excel')

        workbook = xlsxwriter.Workbook("Sites_Biogas_Partenaires.xlsx")

        worksheet = workbook.add_worksheet('data')

        worksheet.write(0, 0, 'nom_du_projet')
        worksheet.write(0, 1, 'commune')
        worksheet.write(0, 2, 'code_insee_epci')
        worksheet.write(0, 3, 'code_reg')
        worksheet.write(0, 4, 'region')
        worksheet.write(0, 5, 'code_commune')
        worksheet.write(0, 6, 'site')
        worksheet.write(0, 7, 'departement')
        worksheet.write(0, 8, 'grx_demandeur')
        worksheet.write(0, 9, 'date_de_mes')
        worksheet.write(0, 10, 'annee_mes')
        worksheet.write(0, 11, 'code_dep')
        worksheet.write(0, 12, 'capacite_de_production_gwh_an')
        worksheet.write(0, 13, 'adresse_postale')
        worksheet.write(0, 14, 'type_de_reseau')

        row = 1

        # array of the cities have at least one train station for travellers
        array_code_insee_commune_with_train_station_for_travellers = []
        f = open('gares_ferroviaires_de_tous_types_exploitees_ou_non.json', "r")
        data = json.loads(f.read())
        for feature in data:
            code_postal = feature['fields']['cp']

            nom = feature['fields']['ville']

            url = "https://geo.api.gouv.fr/communes?codePostal=" + str(code_postal)

            payload = {}
            headers = {}

            response = requests.request("GET", url, headers=headers, data=payload)

            informations_pour_une_commune_avec_son_code_postal = response.json()

            for commune in informations_pour_une_commune_avec_son_code_postal:
                if commune['nom'] == nom and 'Voyageur' in feature['fields']['nature']:
                    array_code_insee_commune_with_train_station_for_travellers.append(str(commune['code']))
        f.close()

        suitable_sites = []

        f = open('les-sites-dinjection-de-biomethane-en-france.json', "r")
        data = json.loads(f.read())
        for feature in data['features']:
            code_insee_commune = feature['properties']['code_commune']

            if code_insee_commune in array_code_insee_commune_with_train_station_for_travellers:
                lon = str(feature['geometry']['coordinates'][0])

                lat = str(feature['geometry']['coordinates'][1])

                url = "https://api-adresse.data.gouv.fr/reverse/?lon=" + lon + "&lat=" + lat

                payload = {}

                headers = {}

                response = requests.request("GET", url, headers=headers, data=payload)

                json_format = json.loads(response.text)

                adresse_postale = ''

                for feature_adresse in json_format['features']:
                    adresse_postale += ' _ ' + feature_adresse['properties']['label']

                x = {
                    'nom_du_projet': feature['properties']['nom_du_projet'],
                    'commune': feature['properties']['commune'],
                    'code_insee_epci': feature['properties']['code_insee_epci'],
                    'code_reg': feature['properties']['code_reg'],
                    'region': feature['properties']['region'],
                    'code_commune': feature['properties']['code_commune'],
                    'site': feature['properties']['site'],
                    'departement': feature['properties']['departement'],
                    'grx_demandeur': feature['properties']['grx_demandeur'],
                    'date_de_mes': feature['properties']['date_de_mes'],
                    'annee_mes': feature['properties']['annee_mes'],
                    'code_dep': feature['properties']['code_dep'],
                    'capacite_de_production_gwh_an': feature['properties']['capacite_de_production_gwh_an'],
                    'adresse_postale': adresse_postale,
                    'type_de_reseau': feature['properties']['type_de_reseau']
                }

                suitable_sites.append(x)
        f.close()

        for suitable_site in suitable_sites:
            worksheet.write(row, 0, suitable_site.get('nom_du_projet'))
            worksheet.write(row, 1, suitable_site.get('commune'))
            worksheet.write(row, 2, suitable_site.get('code_insee_epci'))
            worksheet.write(row, 3, suitable_site.get('code_reg'))
            worksheet.write(row, 4, suitable_site.get('region'))
            worksheet.write(row, 5, suitable_site.get('code_commune'))
            worksheet.write(row, 6, suitable_site.get('site'))
            worksheet.write(row, 7, suitable_site.get('departement'))
            worksheet.write(row, 8, suitable_site.get('grx_demandeur'))
            worksheet.write(row, 9, suitable_site.get('date_de_mes'))
            worksheet.write(row, 10, suitable_site.get('annee_mes'))
            worksheet.write(row, 11, suitable_site.get('code_dep'))
            worksheet.write(row, 12, suitable_site.get('capacite_de_production_gwh_an'))
            worksheet.write(row, 13, suitable_site.get('adresse_postale'))
            worksheet.write(row, 14, suitable_site.get('type_de_reseau'))

            row += 1

        workbook.close()

    def test_show_all_biogas_sites_in_excel(self):
        print('test_show_all_biogas_sites_in_excel')

        workbook = xlsxwriter.Workbook("Sites_Biogas.xlsx")

        worksheet = workbook.add_worksheet('data')

        worksheet.write(0, 0, 'nom_du_projet')
        worksheet.write(0, 1, 'commune')
        worksheet.write(0, 2, 'code_insee_epci')
        worksheet.write(0, 3, 'code_reg')
        worksheet.write(0, 4, 'region')
        worksheet.write(0, 5, 'code_commune')
        worksheet.write(0, 6, 'site')
        worksheet.write(0, 7, 'departement')
        worksheet.write(0, 8, 'grx_demandeur')
        worksheet.write(0, 9, 'date_de_mes')
        worksheet.write(0, 10, 'annee_mes')
        worksheet.write(0, 11, 'code_dep')
        worksheet.write(0, 12, 'capacite_de_production_gwh_an')
        worksheet.write(0, 13, 'adresse_postale')
        worksheet.write(0, 14, 'type_de_reseau')

        row = 1

        suitable_sites = []

        f = open('les-sites-dinjection-de-biomethane-en-france.json', "r")
        data = json.loads(f.read())
        for feature in data['features']:
            code_insee_commune = feature['properties']['code_commune']

            lon = str(feature['geometry']['coordinates'][0])

            lat = str(feature['geometry']['coordinates'][1])

            url = "https://api-adresse.data.gouv.fr/reverse/?lon=" + lon + "&lat=" + lat

            payload = {}

            headers = {}

            response = requests.request("GET", url, headers=headers, data=payload)

            json_format = json.loads(response.text)

            adresse_postale = ''

            for feature_adresse in json_format['features']:
                adresse_postale += ' _ ' + feature_adresse['properties']['label']

            x = {
                'nom_du_projet': feature['properties']['nom_du_projet'],
                'commune': feature['properties']['commune'],
                'code_insee_epci': feature['properties']['code_insee_epci'],
                'code_reg': feature['properties']['code_reg'],
                'region': feature['properties']['region'],
                'code_commune': feature['properties']['code_commune'],
                'site': feature['properties']['site'],
                'departement': feature['properties']['departement'],
                'grx_demandeur': feature['properties']['grx_demandeur'],
                'date_de_mes': feature['properties']['date_de_mes'],
                'annee_mes': feature['properties']['annee_mes'],
                'code_dep': feature['properties']['code_dep'],
                'capacite_de_production_gwh_an': feature['properties']['capacite_de_production_gwh_an'],
                'adresse_postale': adresse_postale,
                'type_de_reseau': feature['properties']['type_de_reseau']
            }

            suitable_sites.append(x)
        f.close()

        for suitable_site in suitable_sites:
            worksheet.write(row, 0, suitable_site.get('nom_du_projet'))
            worksheet.write(row, 1, suitable_site.get('commune'))
            worksheet.write(row, 2, suitable_site.get('code_insee_epci'))
            worksheet.write(row, 3, suitable_site.get('code_reg'))
            worksheet.write(row, 4, suitable_site.get('region'))
            worksheet.write(row, 5, suitable_site.get('code_commune'))
            worksheet.write(row, 6, suitable_site.get('site'))
            worksheet.write(row, 7, suitable_site.get('departement'))
            worksheet.write(row, 8, suitable_site.get('grx_demandeur'))
            worksheet.write(row, 9, suitable_site.get('date_de_mes'))
            worksheet.write(row, 10, suitable_site.get('annee_mes'))
            worksheet.write(row, 11, suitable_site.get('code_dep'))
            worksheet.write(row, 12, suitable_site.get('capacite_de_production_gwh_an'))
            worksheet.write(row, 13, suitable_site.get('adresse_postale'))
            worksheet.write(row, 14, suitable_site.get('type_de_reseau'))

            row += 1

        workbook.close()

    def test_show_all_suitable_gas_cities_with_contacts_in_excel(self):
        print('test_show_all_suitable_gas_cities_with_contacts_in_excel')

        payload = {}

        headers = {}

        try:
            # array of the cities connected to a gas grid
            array_code_insee_commune_desservies_par_gaz = []
            f = open('communes-desservies-en-gaz.json', "r")
            data = json.loads(f.read())
            for feature in data['features']:
                code_insee_commune = feature['properties']['code_insee_commune'][1:]
                array_code_insee_commune_desservies_par_gaz.append(str(code_insee_commune))
            f.close()

            # array of the cities that have stations for injecting biogas into a gas grid
            array_code_insee_commune_biogas = []
            f = open('les-sites-dinjection-de-biomethane-en-france.json', "r")
            data = json.loads(f.read())
            for feature in data['features']:
                code_insee_commune = feature['properties']['code_commune']
                array_code_insee_commune_biogas.append(str(code_insee_commune))
            f.close()

            # array of the cities have at least one train station for travellers
            array_code_insee_commune_with_train_station_for_travellers = []
            f = open('gares_ferroviaires_de_tous_types_exploitees_ou_non.json', "r")
            data = json.loads(f.read())
            for feature in data:
                code_postal = feature['fields']['cp']

                nom = feature['fields']['ville']

                url = "https://geo.api.gouv.fr/communes?codePostal=" + str(code_postal)

                payload = {}
                headers = {}

                response = requests.request("GET", url, headers=headers, data=payload)

                informations_pour_une_commune_avec_son_code_postal = response.json()

                for commune in informations_pour_une_commune_avec_son_code_postal:
                    if commune['nom'] == nom and 'Voyageur' in feature['fields']['nature']:
                        array_code_insee_commune_with_train_station_for_travellers.append(str(commune['code']))
            f.close()

            url = "https://geo.api.gouv.fr/communes?fields=nom,code,codesPostaux,codeDepartement,codeRegion,population&format=json&geometry=centre"

            response_communes = requests.request("GET", url, headers=headers, data=payload)

            communes = response_communes.json()

            workbook = xlsxwriter.Workbook("Mairies_Methane.xlsx")

            worksheet = workbook.add_worksheet('data')

            worksheet.write(0, 0, 'Mairie')
            worksheet.write(0, 1, 'Adresse postale')
            worksheet.write(0, 2, 'Telephone')
            worksheet.write(0, 3, 'Adresse mail')
            worksheet.write(0, 4, 'Horaire ouverture')
            worksheet.write(0, 5, 'Site internet')

            row = 1

            suitable_cities = []

            about_parcelles = "parcelles"

            print('start main for loop')

            for commune in communes:
                try:
                    population = commune['population']

                    code_insee_commune = commune['code']

                    # Communes desservies par le gaz : ok
                    # Communes ayant un site de biogaz : ok
                    # Communes ayant moins de 1000 haibtants : ok
                    # Communes ayant au moins une gare de train pour les voyageurs : ok
                    if (code_insee_commune in array_code_insee_commune_desservies_par_gaz) \
                            and ((code_insee_commune in array_code_insee_commune_biogas)
                                 or (code_insee_commune in array_code_insee_commune_with_train_station_for_travellers)) \
                            and population <= 1000:
                                code_insee_region = commune['codeRegion']

                                code_insee_departement = commune['codeDepartement']

                                url_departement = "https://geo.api.gouv.fr/departements/" \
                                                  + code_insee_departement \
                                                  + "?fields=code,nom,codeRegion,region&format=json"

                                response_departement = requests.request("GET",
                                                                        url_departement,
                                                                        headers=headers,
                                                                        data=payload)

                                nom_departement = str(json.loads(response_departement.text)['nom']) \
                                    .lower() \
                                    .replace("î", "i") \
                                    .replace(" ", "-") \
                                    .replace("'", "-") \
                                    .replace('é', 'e') \
                                    .replace('ô', 'o') \
                                    .replace('è', 'e') \
                                    .replace('à', 'a')

                                url_region = "https://geo.api.gouv.fr/regions/" \
                                             + code_insee_region \
                                             + "?fields=code,nom&format=json"

                                response_region = requests.request("GET",
                                                                   url_region,
                                                                   headers=headers,
                                                                   data=payload)

                                nom_region = str(json.loads(response_region.text)['nom']) \
                                    .lower() \
                                    .replace("î", "i") \
                                    .replace(" ", "-") \
                                    .replace("'", "-") \
                                    .replace('é', 'e') \
                                    .replace('ô', 'o') \
                                    .replace('è', 'e') \
                                    .replace('à', 'a')

                                url_zip_file_for_parcelles = "https://cadastre.data.gouv.fr/data/etalab-cadastre/2020-07-01/geojson/communes/" \
                                                             + code_insee_departement + "/" \
                                                             + code_insee_commune + "/cadastre-" + code_insee_commune \
                                                             + "-" + about_parcelles + ".json.gz"

                                resp = requests.get(url_zip_file_for_parcelles, stream=True)

                                # donwload gz file
                                gz_filename = "cadastre-" + code_insee_commune + "-" + about_parcelles + ".json.gz"
                                gz_file = open(gz_filename, 'wb')
                                gz_file.write(resp.content)
                                gz_file.close()

                                # extract json file
                                input_file = gzip.GzipFile(gz_filename, 'rb')
                                s = input_file.read()
                                input_file.close()
                                output_file = open(gz_filename[:-3], 'wb')
                                output_file.write(s)
                                output_file.close()

                                json_file = open(gz_filename[:-3])
                                data = json.loads(json_file.read())

                                for feature in data['features']:
                                    try:
                                        properties = feature['properties']

                                        # Terrain mesurant au moins 10000 mètres carrés : ok
                                        if properties['contenance'] >= 10000:
                                            try:
                                                url_mairie = "https://lannuaire.service-public.fr/" + nom_region + "/" \
                                                             + nom_departement + "/mairie-" + code_insee_commune + "-01"

                                                print("suitable city : " + url_mairie)

                                                # Request the content of a page from the url
                                                html = requests.get(url_mairie)

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
                                                    adresse_postale += soup.find("div", {'itemprop': 'address'}).find(
                                                        'p', {
                                                            'class': 'mb-map'}) \
                                                        .text \
                                                        .replace("\n", " ") \
                                                        .replace('\t', " ") \
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
                                                    email += soup.find("a", {'class': 'send-mail'}) \
                                                        .text \
                                                        .replace("\n", "")
                                                else:
                                                    print("no content_contact_email")

                                                # horaires ouverture
                                                horaires_ouverture = ''
                                                if soup.find("div", {'itemprop': 'hoursAvailable'}) is not None:
                                                    horaires_ouverture += soup.find("div",
                                                                                    {'itemprop': 'hoursAvailable'}) \
                                                        .text \
                                                        .replace("\n", "")
                                                else:
                                                    print("no horaires ouverture")

                                                x = {
                                                    'mairie': nom,
                                                    'adresse_postale': adresse_postale,
                                                    'telephone': telephone,
                                                    'adresse_mail': email,
                                                    'horaires_ouverture': horaires_ouverture,
                                                    'website': website
                                                }

                                                print("contact mairie : " + str(x))

                                                suitable_cities.append(x)
                                            except Exception as e:
                                                print('error coordinates : ' + str(e))

                                            break
                                    except Exception as e:
                                        print('error feature : ' + str(e))

                                json_file.close()

                                # delete gz file and json file
                                os.remove(gz_filename[:-3])
                                os.remove(gz_filename)
                except Exception as e:
                    print("error commune : " + str(e))

            for city in suitable_cities:
                worksheet.write(row, 0, city['mairie'])
                worksheet.write(row, 1, city['adresse_postale'])
                worksheet.write(row, 2, city['telephone'])
                worksheet.write(row, 3, "'" + city['adresse_mail'] + "',")
                worksheet.write(row, 4, city['horaires_ouverture'])
                worksheet.write(row, 5, city['website'])

                row += 1

            workbook.close()
        except Exception as e:
            print('error main : ' + str(e))

    def test_show_all_cities_with_a_gas_transport_network_in_france(self):
        print("test_show_all_cities_with_a_gas_transport_network_in_france")

        array_code_insee_communes_desservies_par_reseau_transport_gaz = []

        f = open('trace-du-reseau-grt-250.json', "r")

        data = json.loads(f.read())

        for dataset in data:
            try:
                lon = str(dataset["geometry"]["coordinates"][0])

                lat = str(dataset["geometry"]["coordinates"][1])

                url = "https://api-adresse.data.gouv.fr/reverse/?lon=" + lon + "&lat=" + lat

                payload = {}

                headers = {}

                response = requests.request("GET", url, headers=headers, data=payload)

                json_format = json.loads(response.text)

                code_insee_commune = str(json_format['features'][0]['properties']['citycode'])

                city = str(json_format['features'][0]['properties']['city'])

                print("code_insee_commune : " + code_insee_commune + " _ city : " + city)

                array_code_insee_communes_desservies_par_reseau_transport_gaz.append(code_insee_commune)
            except Exception as e:
                print('error : ' + str(e))

        f.close()

    def test_show_all_suitable_parcelles_for_injecting_gas_in_france_in_gas_transport_network_into_excel_without_archive_url(self):
        print("test_show_all_cities_with_a_gas_transport_network_in_france")

        try:
            # array_code_insee_communes_desservies_par_reseau_transport_gaz
            array_code_insee_communes_desservies_par_reseau_transport_gaz = []
            f = open('trace-du-reseau-grt-250.json', "r")
            data = json.loads(f.read())
            for dataset in data:
                try:
                    lon = str(dataset["geometry"]["coordinates"][0])
                    lat = str(dataset["geometry"]["coordinates"][1])
                    url = "https://api-adresse.data.gouv.fr/reverse/?lon=" + lon + "&lat=" + lat
                    payload = {}
                    headers = {}
                    response = requests.request("GET", url, headers=headers, data=payload)
                    json_format = json.loads(response.text)
                    code_insee_commune = str(json_format['features'][0]['properties']['citycode'])
                    # city = str(json_format['features'][0]['properties']['city'])
                    array_code_insee_communes_desservies_par_reseau_transport_gaz.append(code_insee_commune)
                except Exception as e:
                    print('error : ' + str(e))
            f.close()

            # array of the cities have at least one train station for travellers
            array_code_insee_commune_with_train_station_for_travellers = []
            f = open('gares_ferroviaires_de_tous_types_exploitees_ou_non.json', "r")
            data = json.loads(f.read())
            for feature in data:
                code_postal = feature['fields']['cp']

                nom = feature['fields']['ville']

                url = "https://geo.api.gouv.fr/communes?codePostal=" + str(code_postal)

                payload = {}
                headers = {}

                response = requests.request("GET", url, headers=headers, data=payload)

                informations_pour_une_commune_avec_son_code_postal = response.json()

                for commune in informations_pour_une_commune_avec_son_code_postal:
                    if commune['nom'] == nom and 'Voyageur' in feature['fields']['nature']:
                        array_code_insee_commune_with_train_station_for_travellers.append(str(commune['code']))
            f.close()

            url = "https://geo.api.gouv.fr/communes?fields=nom,code,codesPostaux,codeDepartement,codeRegion,population&format=json&geometry=centre"

            payload = {}

            headers = {}

            response_communes = requests.request("GET", url, headers=headers, data=payload)

            communes = response_communes.json()

            about_parcelles = "parcelles"

            print('start main for loop')

            suitable_lands = []

            for commune in communes:
                try:
                    code_insee_departement = commune['codeDepartement']

                    code_insee_commune = commune['code']

                    population = commune['population']

                    # Communes desservies par le réseau de transport de gaz : ok
                    # Communes ayant au moins une gare de train pour les voyageurs : ok
                    if (code_insee_commune in array_code_insee_commune_with_train_station_for_travellers) \
                            and (code_insee_commune in array_code_insee_communes_desservies_par_reseau_transport_gaz) \
                            and code_insee_departement in ['77', '78', '91', '95'] \
                            and population <= 10000:
                        url_zip_file_for_parcelles = "https://cadastre.data.gouv.fr/data/etalab-cadastre/2020-07-01/geojson/communes/" \
                                                     + code_insee_departement + "/" \
                                                     + code_insee_commune + "/cadastre-" + code_insee_commune \
                                                     + "-" + about_parcelles + ".json.gz"

                        resp = requests.get(url_zip_file_for_parcelles, stream=True)

                        # donwload gz file
                        gz_filename = "cadastre-" + code_insee_commune + "-" + about_parcelles + ".json.gz"
                        gz_file = open(gz_filename, 'wb')
                        gz_file.write(resp.content)
                        gz_file.close()

                        # extract json file
                        input_file = gzip.GzipFile(gz_filename, 'rb')
                        s = input_file.read()
                        input_file.close()
                        output_file = open(gz_filename[:-3], 'wb')
                        output_file.write(s)
                        output_file.close()

                        json_file = open(gz_filename[:-3])
                        data = json.loads(json_file.read())

                        for feature in data['features']:
                            try:
                                properties = feature['properties']

                                coordinates = feature['geometry']['coordinates']

                                # Terrain mesurant au moins 1000 mètres carrés : ok
                                if properties['contenance'] >= 1000:
                                    try:
                                        lon = str(coordinates[0][0][0])

                                        lat = str(coordinates[0][0][1])

                                        url = "https://api-adresse.data.gouv.fr/reverse/?lon=" + lon + "&lat=" + lat

                                        payload = {}

                                        headers = {}

                                        response_adresse_postale_reverse = requests.request("GET", url,
                                                                                            headers=headers,
                                                                                            data=payload)

                                        json_format_adresse_postale_reverse = json.loads(
                                            response_adresse_postale_reverse.text)

                                        if len(json_format_adresse_postale_reverse['features']) != 0:
                                            for feature_adresse in json_format_adresse_postale_reverse['features']:
                                                try:
                                                    if feature_adresse['properties']['label'] != '':
                                                        # A python object (dict):
                                                        x = {
                                                            "adresse_postale": feature_adresse['properties']['label'],
                                                            "prefixe_parcelle": properties['prefixe'],
                                                            "section_parcelle": properties['section'],
                                                            "numero_parcelle": properties['numero'],
                                                            "contenance_parcelle": properties['contenance'],
                                                            "url_geoportail_carte": "https://www.geoportail.gouv.fr/carte",
                                                            "coordonnees_gps": "Coordonnées : " + lat + " " + lon
                                                        }

                                                        print("land : " + x.get('adresse_postale'))

                                                        suitable_lands.append(x)

                                                        break
                                                except Exception as e:
                                                    print('error feature_adresse : ' + str(e))
                                    except Exception as e:
                                        print('error coordinates : ' + str(e))
                            except Exception as e:
                                print('error feature : ' + str(e))

                        json_file.close()

                        # delete gz file and json file
                        os.remove(gz_filename[:-3])
                        os.remove(gz_filename)
                except Exception as e:
                    print("error commune : " + str(e))

            workbook = xlsxwriter.Workbook("Parcelles_RTG.xlsx")

            worksheet = workbook.add_worksheet('data')

            worksheet.write(0, 0, 'adresse postale')
            worksheet.write(0, 1, 'prefixe parcelle')
            worksheet.write(0, 2, 'section parcelle')
            worksheet.write(0, 3, 'numero parcelle')
            worksheet.write(0, 4, 'contenance parcelle')
            worksheet.write(0, 5, 'url geoportail carte')
            worksheet.write(0, 6, 'coordonnees gps')

            row = 1

            for lands in suitable_lands:
                worksheet.write(row, 0, lands['adresse_postale'])
                worksheet.write(row, 1, lands['prefixe_parcelle'])
                worksheet.write(row, 2, lands['section_parcelle'])
                worksheet.write(row, 3, lands['numero_parcelle'])
                worksheet.write(row, 4, lands['contenance_parcelle'])
                worksheet.write(row, 5, lands['url_geoportail_carte'])
                worksheet.write(row, 6, lands['coordonnees_gps'])

                row += 1

            workbook.close()
        except Exception as e:
            print('error main : ' + str(e))

    def test_show_all_suitable_gas_cities_for_rtg_with_contacts_in_excel(self):
        print('test_show_all_suitable_gas_cities_for_rtg_with_contacts_in_excel')

        payload = {}

        headers = {}

        try:
            # array_code_insee_communes_desservies_par_reseau_transport_gaz
            print('starting array_code_insee_communes_desservies_par_reseau_transport_gaz')
            array_code_insee_communes_desservies_par_reseau_transport_gaz = []
            f = open('trace-du-reseau-grt-250.json', "r")
            data = json.loads(f.read())
            for dataset in data:
                try:
                    lon = str(dataset["geometry"]["coordinates"][0])
                    lat = str(dataset["geometry"]["coordinates"][1])
                    url = "https://api-adresse.data.gouv.fr/reverse/?lon=" + lon + "&lat=" + lat
                    payload = {}
                    headers = {}
                    response = requests.request("GET", url, headers=headers, data=payload)
                    json_format = json.loads(response.text)
                    code_insee_commune = str(json_format['features'][0]['properties']['citycode'])
                    array_code_insee_communes_desservies_par_reseau_transport_gaz.append(code_insee_commune)
                    print("code_insee_commune : " + code_insee_commune)
                except Exception as e:
                    print('error : ' + str(e))
            f.close()

            # array of the cities have at least one train station for travellers
            print('starting array_code_insee_commune_with_train_station_for_travellers')
            array_code_insee_commune_with_train_station_for_travellers = []
            f = open('gares_ferroviaires_de_tous_types_exploitees_ou_non.json', "r")
            data = json.loads(f.read())
            for feature in data:
                code_postal = feature['fields']['cp']

                nom = feature['fields']['ville']

                url = "https://geo.api.gouv.fr/communes?codePostal=" + str(code_postal)

                payload = {}
                headers = {}

                response = requests.request("GET", url, headers=headers, data=payload)

                informations_pour_une_commune_avec_son_code_postal = response.json()

                for commune in informations_pour_une_commune_avec_son_code_postal:
                    if commune['nom'] == nom and 'Voyageur' in feature['fields']['nature']:
                        array_code_insee_commune_with_train_station_for_travellers.append(str(commune['code']))
            f.close()

            url = "https://geo.api.gouv.fr/communes?fields=nom,code,codesPostaux,codeDepartement,codeRegion,population&format=json&geometry=centre"

            response_communes = requests.request("GET", url, headers=headers, data=payload)

            communes = response_communes.json()

            workbook = xlsxwriter.Workbook("Mairies_RTG.xlsx")

            worksheet = workbook.add_worksheet('data')

            worksheet.write(0, 0, 'Mairie')
            worksheet.write(0, 1, 'Adresse postale')
            worksheet.write(0, 2, 'Telephone')
            worksheet.write(0, 3, 'Adresse mail')
            worksheet.write(0, 4, 'Horaire ouverture')
            worksheet.write(0, 5, 'Site internet')

            row = 1

            suitable_cities = []

            about_parcelles = "parcelles"

            print('start main for loop')

            for commune in communes:
                try:
                    population = commune['population']

                    code_insee_commune = commune['code']

                    # Communes ayant moins de 10000 haibtants : ok
                    # Communes ayant au moins une gare de train pour les voyageurs : ok
                    # Communes desservies par le réseau de transport de gaz naturel : ok
                    if (code_insee_commune in array_code_insee_communes_desservies_par_reseau_transport_gaz) \
                            and (code_insee_commune in array_code_insee_commune_with_train_station_for_travellers) \
                            and population <= 10000:
                                code_insee_region = commune['codeRegion']

                                code_insee_departement = commune['codeDepartement']

                                url_departement = "https://geo.api.gouv.fr/departements/" \
                                                  + code_insee_departement \
                                                  + "?fields=code,nom,codeRegion,region&format=json"

                                response_departement = requests.request("GET",
                                                                        url_departement,
                                                                        headers=headers,
                                                                        data=payload)

                                nom_departement = str(json.loads(response_departement.text)['nom']) \
                                    .lower() \
                                    .replace("î", "i") \
                                    .replace(" ", "-") \
                                    .replace("'", "-") \
                                    .replace('é', 'e') \
                                    .replace('ô', 'o') \
                                    .replace('è', 'e') \
                                    .replace('à', 'a')

                                url_region = "https://geo.api.gouv.fr/regions/" \
                                             + code_insee_region \
                                             + "?fields=code,nom&format=json"

                                response_region = requests.request("GET",
                                                                   url_region,
                                                                   headers=headers,
                                                                   data=payload)

                                nom_region = str(json.loads(response_region.text)['nom']) \
                                    .lower() \
                                    .replace("î", "i") \
                                    .replace(" ", "-") \
                                    .replace("'", "-") \
                                    .replace('é', 'e') \
                                    .replace('ô', 'o') \
                                    .replace('è', 'e') \
                                    .replace('à', 'a')

                                url_zip_file_for_parcelles = "https://cadastre.data.gouv.fr/data/etalab-cadastre/2020-07-01/geojson/communes/" \
                                                             + code_insee_departement + "/" \
                                                             + code_insee_commune + "/cadastre-" + code_insee_commune \
                                                             + "-" + about_parcelles + ".json.gz"

                                resp = requests.get(url_zip_file_for_parcelles, stream=True)

                                # donwload gz file
                                gz_filename = "cadastre-" + code_insee_commune + "-" + about_parcelles + ".json.gz"
                                gz_file = open(gz_filename, 'wb')
                                gz_file.write(resp.content)
                                gz_file.close()

                                # extract json file
                                input_file = gzip.GzipFile(gz_filename, 'rb')
                                s = input_file.read()
                                input_file.close()
                                output_file = open(gz_filename[:-3], 'wb')
                                output_file.write(s)
                                output_file.close()

                                json_file = open(gz_filename[:-3])
                                data = json.loads(json_file.read())

                                for feature in data['features']:
                                    try:
                                        properties = feature['properties']

                                        # Terrain mesurant au moins 1000 mètres carrés : ok
                                        if properties['contenance'] >= 1000:
                                            try:
                                                url_mairie = "https://lannuaire.service-public.fr/" + nom_region + "/" \
                                                             + nom_departement + "/mairie-" + code_insee_commune + "-01"

                                                print("suitable city : " + url_mairie)

                                                # Request the content of a page from the url
                                                html = requests.get(url_mairie)

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
                                                    adresse_postale += soup.find("div", {'itemprop': 'address'}).find(
                                                        'p', {
                                                            'class': 'mb-map'}) \
                                                        .text \
                                                        .replace("\n", " ") \
                                                        .replace('\t', " ") \
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
                                                    email += soup.find("a", {'class': 'send-mail'}) \
                                                        .text \
                                                        .replace("\n", "")
                                                else:
                                                    print("no content_contact_email")

                                                # horaires ouverture
                                                horaires_ouverture = ''
                                                if soup.find("div", {'itemprop': 'hoursAvailable'}) is not None:
                                                    horaires_ouverture += soup.find("div",
                                                                                    {'itemprop': 'hoursAvailable'}) \
                                                        .text \
                                                        .replace("\n", "")
                                                else:
                                                    print("no horaires ouverture")

                                                x = {
                                                    'mairie': nom,
                                                    'adresse_postale': adresse_postale,
                                                    'telephone': telephone,
                                                    'adresse_mail': email,
                                                    'horaires_ouverture': horaires_ouverture,
                                                    'website': website
                                                }

                                                print("contact mairie : " + str(x))

                                                suitable_cities.append(x)
                                            except Exception as e:
                                                print('error coordinates : ' + str(e))

                                            break

                                    except Exception as e:
                                        print('error feature : ' + str(e))

                                json_file.close()

                                # delete gz file and json file
                                os.remove(gz_filename[:-3])
                                os.remove(gz_filename)
                except Exception as e:
                    print("error commune : " + str(e))

            for city in suitable_cities:
                worksheet.write(row, 0, city['mairie'])
                worksheet.write(row, 1, city['adresse_postale'])
                worksheet.write(row, 2, city['telephone'])
                worksheet.write(row, 3, "'" + city['adresse_mail'] + "',")
                worksheet.write(row, 4, city['horaires_ouverture'])
                worksheet.write(row, 5, city['website'])

                row += 1

            workbook.close()
        except Exception as e:
            print('error main : ' + str(e))

    def test_show_all_suitable_parcelles_for_injecting_gas_in_france_in_gas_transport_network_into_excel_in_zone_urbaine(self):
        print("test_show_all_suitable_parcelles_for_injecting_gas_in_france_in_gas_transport_network_into_excel_in_zone_urbaine")

        try:
            # array_zonages_urbaines
            array_zonages_urbaines = ['AU', 'NA', 'NB', 'U', 'UA', 'UB', 'UC', 'UD', 'UE', 'UI', 'UY', 'UP']

            # array_code_insee_communes_desservies_par_reseau_transport_gaz
            print('starting array_code_insee_communes_desservies_par_reseau_transport_gaz')
            array_code_insee_communes_desservies_par_reseau_transport_gaz = []
            f = open('trace-du-reseau-grt-250.json', "r")
            data = json.loads(f.read())
            for dataset in data:
                try:
                    lon = str(dataset["geometry"]["coordinates"][0])
                    lat = str(dataset["geometry"]["coordinates"][1])
                    url = "https://api-adresse.data.gouv.fr/reverse/?lon=" + lon + "&lat=" + lat
                    payload = {}
                    headers = {}
                    response = requests.request("GET", url, headers=headers, data=payload)
                    json_format = json.loads(response.text)
                    code_insee_commune = str(json_format['features'][0]['properties']['citycode'])
                    print('code_insee_commune : ' + str(code_insee_commune))
                    array_code_insee_communes_desservies_par_reseau_transport_gaz.append(code_insee_commune)
                except Exception as e:
                    print('error : ' + str(e))
            f.close()

            # array of the cities have at least one train station for travellers
            print('starting array_code_insee_commune_with_train_station_for_travellers')
            array_code_insee_commune_with_train_station_for_travellers = []
            f = open('gares_ferroviaires_de_tous_types_exploitees_ou_non.json', "r")
            data = json.loads(f.read())
            for feature in data:
                code_postal = feature['fields']['cp']

                nom = feature['fields']['ville']

                url = "https://geo.api.gouv.fr/communes?codePostal=" + str(code_postal)

                payload = {}
                headers = {}

                response = requests.request("GET", url, headers=headers, data=payload)

                informations_pour_une_commune_avec_son_code_postal = response.json()

                for commune in informations_pour_une_commune_avec_son_code_postal:
                    if commune['nom'] == nom and 'Voyageur' in feature['fields']['nature']:
                        array_code_insee_commune_with_train_station_for_travellers.append(str(commune['code']))
                        print('commune voyageur : ' + str(commune['code']))
                    else:
                        print('commune non voyageur : ' + str(commune['code']))
            f.close()

            url = "https://geo.api.gouv.fr/communes?fields=nom,code,codesPostaux,codeDepartement,codeRegion,population&format=json&geometry=centre"

            payload = {}

            headers = {}

            response_communes = requests.request("GET", url, headers=headers, data=payload)

            communes = response_communes.json()

            about_parcelles = "parcelles"

            print('start main for loop')

            suitable_lands = []

            for commune in communes:
                try:
                    code_insee_departement = commune['codeDepartement']

                    code_insee_commune = commune['code']

                    population = commune['population']

                    # Communes desservies par le réseau de transport de gaz : ok
                    # Communes ayant au moins une gare de train pour les voyageurs : ok
                    if (code_insee_commune in array_code_insee_commune_with_train_station_for_travellers) \
                            and (code_insee_commune in array_code_insee_communes_desservies_par_reseau_transport_gaz) \
                            and population <= 10000:
                        url_zip_file_for_parcelles = "https://cadastre.data.gouv.fr/data/etalab-cadastre/2020-07-01/geojson/communes/" \
                                                     + code_insee_departement + "/" \
                                                     + code_insee_commune + "/cadastre-" + code_insee_commune \
                                                     + "-" + about_parcelles + ".json.gz"

                        resp = requests.get(url_zip_file_for_parcelles, stream=True)

                        # donwload gz file
                        gz_filename = "cadastre-" + code_insee_commune + "-" + about_parcelles + ".json.gz"
                        gz_file = open(gz_filename, 'wb')
                        gz_file.write(resp.content)
                        gz_file.close()

                        # extract json file
                        input_file = gzip.GzipFile(gz_filename, 'rb')
                        s = input_file.read()
                        input_file.close()
                        output_file = open(gz_filename[:-3], 'wb')
                        output_file.write(s)
                        output_file.close()

                        json_file = open(gz_filename[:-3])
                        data = json.loads(json_file.read())

                        for feature in data['features']:
                            try:
                                properties = feature['properties']

                                coordinates = feature['geometry']['coordinates']

                                point_gpu = feature['geometry']['coordinates'][0][0]

                                geometry_gpu = '{"type": "Point", "coordinates": ' + str(point_gpu) + '}' \
                                    .replace('{', '%7B') \
                                    .replace('"', '%22') \
                                    .replace(':', '%3A') \
                                    .replace(' ', '%20') \
                                    .replace(',', '%2C') \
                                    .replace(' ', '%20') \
                                    .replace('[', '%5B') \
                                    .replace(']', '%5D') \
                                    .replace('}', '%7D')

                                base_url_gpu = 'https://apicarto.ign.fr/api'

                                api_gpu = '/gpu/zone-urba'

                                url_gpu = base_url_gpu + api_gpu + '?geom=' + geometry_gpu

                                payload_gpu = {}

                                headers_gpu = {}

                                response_gpu = requests.get(url_gpu, headers=headers_gpu, data=payload_gpu)

                                data_response_gpu = json.loads(response_gpu.text)

                                features1 = data_response_gpu['features']

                                if len(features1) >= 1:
                                    for feature1 in features1:
                                        libelle = feature1['properties']['libelle']
                                        libelong = feature1['properties']['libelong']

                                        # Terrain mesurant au moins 10 000 mètres carrés : ok
                                        # Terrain en zone urbaine uniquement : ok
                                        if properties['contenance'] >= 10000 and \
                                                (str(libelle) in array_zonages_urbaines or "urbain" in str(libelong).lower()):
                                            try:
                                                lon = str(coordinates[0][0][0])

                                                lat = str(coordinates[0][0][1])

                                                url = "https://api-adresse.data.gouv.fr/reverse/?lon=" + lon + "&lat=" + lat

                                                payload = {}

                                                headers = {}

                                                response_adresse_postale_reverse = requests.request("GET", url,
                                                                                                    headers=headers,
                                                                                                    data=payload)

                                                json_format_adresse_postale_reverse = json.loads(
                                                    response_adresse_postale_reverse.text)

                                                if len(json_format_adresse_postale_reverse['features']) != 0:
                                                    for feature_adresse in json_format_adresse_postale_reverse['features']:
                                                        try:
                                                            if feature_adresse['properties']['label'] != '':
                                                                # A python object (dict):
                                                                x = {
                                                                    "adresse_postale": feature_adresse['properties']['label'],
                                                                    "prefixe_parcelle": properties['prefixe'],
                                                                    "section_parcelle": properties['section'],
                                                                    "numero_parcelle": properties['numero'],
                                                                    "contenance_parcelle": properties['contenance'],
                                                                    "url_geoportail_carte": "https://www.geoportail.gouv.fr/carte",
                                                                    "coordonnees_gps": "Coordonnées : " + lat + " " + lon
                                                                }

                                                                print("land : " + x.get('adresse_postale'))

                                                                suitable_lands.append(x)

                                                                break
                                                        except Exception as e:
                                                            print('error feature_adresse : ' + str(e))
                                            except Exception as e:
                                                print('error coordinates : ' + str(e))
                                        else:
                                            print('not suitable land : ' + str(properties['prefixe'] +
                                                                               properties['section'] +
                                                                               properties['numero']))
                                else:
                                    print('no features')
                            except Exception as e:
                                print('error feature : ' + str(e))

                        json_file.close()

                        # delete gz file and json file
                        os.remove(gz_filename[:-3])
                        os.remove(gz_filename)
                    else:
                        print('not suitable commune : ' + str(code_insee_commune))
                except Exception as e:
                    print("error commune : " + str(e))

            workbook = xlsxwriter.Workbook("Parcelles_RTG_Z_U.xlsx")

            worksheet = workbook.add_worksheet('data')

            worksheet.write(0, 0, 'adresse postale')
            worksheet.write(0, 1, 'prefixe parcelle')
            worksheet.write(0, 2, 'section parcelle')
            worksheet.write(0, 3, 'numero parcelle')
            worksheet.write(0, 4, 'contenance parcelle')
            worksheet.write(0, 5, 'url geoportail carte')
            worksheet.write(0, 6, 'coordonnees gps')

            row = 1

            for lands in suitable_lands:
                worksheet.write(row, 0, lands['adresse_postale'])
                worksheet.write(row, 1, lands['prefixe_parcelle'])
                worksheet.write(row, 2, lands['section_parcelle'])
                worksheet.write(row, 3, lands['numero_parcelle'])
                worksheet.write(row, 4, lands['contenance_parcelle'])
                worksheet.write(row, 5, lands['url_geoportail_carte'])
                worksheet.write(row, 6, lands['coordonnees_gps'])

                row += 1

            workbook.close()
        except Exception as e:
            print('error main : ' + str(e))

    def test_show_all_suitable_parcelles_for_injecting_gas_in_france_in_gas_transport_network_into_excel_in_zone_urbaine_for_some_departments_into_mysql(self):
        print("test_show_all_suitable_parcelles_for_injecting_gas_in_france_in_gas_transport_network_into_excel_in_zone_urbaine_for_some_departments_into_mysql")

        try:
            # array_zonages_urbaines
            array_zonages_urbaines = ['AU', 'NA', 'NB', 'U', 'UA', 'UB', 'UC', 'UD', 'UE', 'UI', 'UY', 'UP']

            # array_code_insee_communes_desservies_par_reseau_transport_gaz
            print('starting array_code_insee_communes_desservies_par_reseau_transport_gaz')
            array_code_insee_communes_desservies_par_reseau_transport_gaz = []
            f = open('trace-du-reseau-grt-250.json', "r")
            data = json.loads(f.read())
            for dataset in data:
                try:
                    lon = str(dataset["geometry"]["coordinates"][0])
                    lat = str(dataset["geometry"]["coordinates"][1])
                    url = "https://api-adresse.data.gouv.fr/reverse/?lon=" + lon + "&lat=" + lat
                    payload = {}
                    headers = {}
                    response = requests.request("GET", url, headers=headers, data=payload)
                    json_format = json.loads(response.text)
                    code_insee_commune = str(json_format['features'][0]['properties']['citycode'])
                    print('code_insee_commune : ' + str(code_insee_commune))
                    array_code_insee_communes_desservies_par_reseau_transport_gaz.append(code_insee_commune)
                except Exception as e:
                    print('error : ' + str(e))
            f.close()

            # array of the cities have at least one train station for travellers
            print('starting array_code_insee_commune_with_train_station_for_travellers')
            array_code_insee_commune_with_train_station_for_travellers = []
            f = open('gares_ferroviaires_de_tous_types_exploitees_ou_non.json', "r")
            data = json.loads(f.read())
            for feature in data:
                code_postal = feature['fields']['cp']

                nom = feature['fields']['ville']

                url = "https://geo.api.gouv.fr/communes?codePostal=" + str(code_postal)

                payload = {}
                headers = {}

                response = requests.request("GET", url, headers=headers, data=payload)

                informations_pour_une_commune_avec_son_code_postal = response.json()

                for commune in informations_pour_une_commune_avec_son_code_postal:
                    if commune['nom'] == nom and 'Voyageur' in feature['fields']['nature']:
                        array_code_insee_commune_with_train_station_for_travellers.append(str(commune['code']))
                        print('commune voyageur : ' + str(commune['code']))
                    else:
                        print('commune non voyageur : ' + str(commune['code']))
            f.close()

            departements = ['77', '78', '91', '95']

            for departement in departements:
                url_departement = "https://geo.api.gouv.fr/departements/" + str(departement) \
                                  + "/communes?fields=nom,code,codesPostaux,codeDepartement,codeRegion,population&format=json&geometry=centre"

                payload = {}

                headers = {}

                response_communes = requests.request("GET", url_departement, headers=headers, data=payload)

                communes = response_communes.json()

                about_parcelles = "parcelles"

                print('start main for loop')

                for commune in communes:
                    try:
                        code_insee_departement = commune['codeDepartement']

                        code_insee_commune = commune['code']

                        population = commune['population']

                        # Communes desservies par le réseau de transport de gaz : ok
                        # Communes ayant au moins une gare de train pour les voyageurs : ok
                        if (code_insee_commune in array_code_insee_commune_with_train_station_for_travellers) \
                                and (code_insee_commune in array_code_insee_communes_desservies_par_reseau_transport_gaz) \
                                and population <= 10000:
                            url_zip_file_for_parcelles = "https://cadastre.data.gouv.fr/data/etalab-cadastre/latest/geojson/communes/" \
                                                         + code_insee_departement + "/" \
                                                         + code_insee_commune + "/cadastre-" + code_insee_commune \
                                                         + "-" + about_parcelles + ".json.gz"

                            resp = requests.get(url_zip_file_for_parcelles, stream=True)

                            # donwload gz file
                            gz_filename = "cadastre-" + code_insee_commune + "-" + about_parcelles + ".json.gz"
                            gz_file = open(gz_filename, 'wb')
                            gz_file.write(resp.content)
                            gz_file.close()

                            # extract json file
                            input_file = gzip.GzipFile(gz_filename, 'rb')
                            s = input_file.read()
                            input_file.close()
                            output_file = open(gz_filename[:-3], 'wb')
                            output_file.write(s)
                            output_file.close()

                            json_file = open(gz_filename[:-3])
                            data = json.loads(json_file.read())

                            for feature in data['features']:
                                try:
                                    properties = feature['properties']

                                    coordinates = feature['geometry']['coordinates']

                                    # Terrain mesurant au moins 10 000 mètres carrés : ok
                                    # Terrain en zone urbaine uniquement : ok
                                    if properties['contenance'] >= 10000:
                                        try:
                                            point_gpu = feature['geometry']['coordinates'][0][0]

                                            geometry_gpu = '{"type": "Point", "coordinates": ' + str(point_gpu) + '}'\
                                                .replace('{', '%7B') \
                                                .replace('"', '%22') \
                                                .replace(':', '%3A') \
                                                .replace(' ', '%20') \
                                                .replace(',', '%2C') \
                                                .replace(' ', '%20') \
                                                .replace('[', '%5B') \
                                                .replace(']', '%5D') \
                                                .replace('}', '%7D')

                                            base_url_gpu = 'https://apicarto.ign.fr/api'

                                            api_gpu = '/gpu/zone-urba'

                                            url_gpu = base_url_gpu + api_gpu + '?geom=' + geometry_gpu

                                            payload_gpu = {}

                                            headers_gpu = {}

                                            response_gpu = requests.get(url_gpu, headers=headers_gpu,
                                                                        data=payload_gpu)

                                            data_response_gpu = json.loads(response_gpu.text)

                                            features1 = data_response_gpu['features']

                                            if len(features1) >= 1:
                                                for feature1 in features1:
                                                    typezone = feature1['properties']['typezone']
                                                    libelle = feature1['properties']['libelle']
                                                    libelong = feature1['properties']['libelong']
                                                    urlfic = feature1['properties']['urlfic']

                                                    if libelle is None:
                                                        libelle = 'null'

                                                    if libelong is None:
                                                        libelong = 'null'

                                                    if urlfic is None:
                                                        urlfic = 'null'

                                                    if str(typezone) in array_zonages_urbaines:
                                                        try:
                                                            lon = str(coordinates[0][0][0])

                                                            lat = str(coordinates[0][0][1])

                                                            url_adresse = "https://api-adresse.data.gouv.fr/reverse/?lon=" \
                                                                          + lon + "&lat=" + lat

                                                            payload = {}

                                                            headers = {}

                                                            response_adresse_postale_reverse = requests.request(
                                                                "GET",
                                                                url_adresse,
                                                                headers=headers,
                                                                data=payload)

                                                            json_format_adresse_postale_reverse = json.loads(
                                                                response_adresse_postale_reverse.text)

                                                            if len(json_format_adresse_postale_reverse[
                                                                       'features']) != 0:
                                                                for feature_adresse in json_format_adresse_postale_reverse['features']:
                                                                    try:
                                                                        if feature_adresse['properties']['label'] != '':
                                                                            x = {
                                                                                "adresse_postale": str(feature_adresse['properties']['label']),
                                                                                "prefixe_parcelle": str(properties['prefixe']),
                                                                                "section_parcelle": str(properties['section']),
                                                                                "numero_parcelle": str(properties['numero']),
                                                                                "contenance_parcelle": str(properties['contenance']),
                                                                                "url_geoportail_carte": "https://www.geoportail.gouv.fr/carte",
                                                                                "coordonnees_gps": "Coordonnées : " + lat + " " + lon,
                                                                                "typezone": str(typezone),
                                                                                "libelle": str(libelle),
                                                                                "libelong": str(libelong),
                                                                                "urlfic": str(urlfic)
                                                                            }

                                                                            try:
                                                                                connection = pymysql.connect(
                                                                                    host='localhost',
                                                                                    port=3306,
                                                                                    user='root',
                                                                                    password='8h0NEJkEf3lyCBUoPQwCHSu@@@@@@@',
                                                                                    db='parcelles',
                                                                                    charset='utf8mb4',
                                                                                    cursorclass=pymysql.cursors.DictCursor
                                                                                )

                                                                                with connection.cursor() as cursor:
                                                                                    try:
                                                                                        sql = "insert into parcelles_rtg_z_u " \
                                                                                              "(adresse_postale, " \
                                                                                              "prefixe_parcelle, " \
                                                                                              "section_parcelle, " \
                                                                                              "numero_parcelle, " \
                                                                                              "contenance_parcelle, " \
                                                                                              "url_geoportail_carte, " \
                                                                                              "coordonnees_gps, " \
                                                                                              "typezone, " \
                                                                                              "libelle, " \
                                                                                              "libelong, " \
                                                                                              "urlfic" \
                                                                                              ") " \
                                                                                              "value (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

                                                                                        cursor.execute(sql, (x.get('adresse_postale'),
                                                                                                             x.get('prefixe_parcelle'),
                                                                                                             x.get('section_parcelle'),
                                                                                                             x.get('numero_parcelle'),
                                                                                                             x.get('contenance_parcelle'),
                                                                                                             x.get('url_geoportail_carte'),
                                                                                                             x.get('coordonnees_gps'),
                                                                                                             x.get('typezone'),
                                                                                                             x.get('libelle'),
                                                                                                             x.get('libelong'),
                                                                                                             x.get('urlfic')))

                                                                                        connection.commit()

                                                                                        connection.close()

                                                                                        print("land : " + x.get('adresse_postale') + " : ok")
                                                                                    except Exception as e:
                                                                                        print("The record already "
                                                                                              "exists : " + str(e))
                                                                                        connection.close()
                                                                            except Exception as e:
                                                                                print('There is a problem : ' + str(e))

                                                                            break
                                                                    except Exception as e:
                                                                        print(
                                                                            'error feature_adresse : ' + str(e))
                                                        except Exception as e:
                                                            print('error libelle urbain : ' + str(e))
                                                    else:
                                                        print('ville : ' + str(commune['nom']) + ' , code insee : '
                                                              + str(commune['code']) + ' , not urban land : '
                                                              + str(properties['prefixe'] + properties['section']
                                                                    + properties['numero']) + " _ typezone : " + str(typezone))
                                            else:
                                                print('no features ville : ' + str(commune['nom']) + ' , code insee : '
                                                      + str(commune['code']) + ' , not suitable land : '
                                                      + str(properties['prefixe'] + properties['section']
                                                            + properties['numero']))
                                        except Exception as e:
                                            print('error terrain > 10000 m² : ' + str(e))
                                    else:
                                        print('ville : ' + str(commune['nom'])
                                              + ' , code insee : ' + str(commune['code'])
                                              + ' , not suitable land : '
                                              + str(properties['prefixe']
                                                    + properties['section']
                                                    + properties['numero']) + " < 10000")
                                except Exception as e:
                                    print('error feature : ' + str(e))

                            json_file.close()

                            # delete gz file and json file
                            os.remove(gz_filename[:-3])
                            os.remove(gz_filename)
                        else:
                            print('not suitable commune : ' + str(code_insee_commune))
                    except Exception as e:
                        print("error commune : " + str(e))
        except Exception as e:
            print('error main : ' + str(e))

    def test_show_all_suitable_parcelles_for_injecting_gas_in_france_in_gas_transport_network_into_excel_in_zone_urbaine_for_some_departments_into_mysql_1(self):
        print("test_show_all_suitable_parcelles_for_injecting_gas_in_france_in_gas_transport_network_into_excel_in_zone_urbaine_for_some_departments_into_mysql_1")

        try:
            # array_zonages_urbaines
            array_zonages_urbaines = ['AU', 'NA', 'NB', 'U', 'UA', 'UB', 'UC', 'UD', 'UE', 'UI', 'UY', 'UP']

            departements = ['77', '78', '91', '95']

            for departement in departements:
                url_departement = "https://geo.api.gouv.fr/departements/" + str(departement) \
                                  + "/communes?fields=nom,code,codesPostaux,codeDepartement,codeRegion,population&format=json&geometry=centre"

                payload = {}

                headers = {}

                response_communes = requests.request("GET", url_departement, headers=headers, data=payload)

                communes = response_communes.json()

                about_parcelles = "parcelles"

                print('start main for loop')

                for commune in communes:
                    try:
                        code_insee_departement = commune['codeDepartement']

                        code_insee_commune = commune['code']

                        population = commune['population']

                        if population <= 10000:
                            url_zip_file_for_parcelles = "https://cadastre.data.gouv.fr/data/etalab-cadastre/latest/geojson/communes/" \
                                                         + code_insee_departement + "/" \
                                                         + code_insee_commune + "/cadastre-" + code_insee_commune \
                                                         + "-" + about_parcelles + ".json.gz"

                            resp = requests.get(url_zip_file_for_parcelles, stream=True)

                            # donwload gz file
                            gz_filename = "cadastre-" + code_insee_commune + "-" + about_parcelles + ".json.gz"
                            gz_file = open(gz_filename, 'wb')
                            gz_file.write(resp.content)
                            gz_file.close()

                            # extract json file
                            input_file = gzip.GzipFile(gz_filename, 'rb')
                            s = input_file.read()
                            input_file.close()
                            output_file = open(gz_filename[:-3], 'wb')
                            output_file.write(s)
                            output_file.close()

                            json_file = open(gz_filename[:-3])
                            data = json.loads(json_file.read())

                            for feature in data['features']:
                                try:
                                    properties = feature['properties']

                                    coordinates = feature['geometry']['coordinates']

                                    # Terrain mesurant au moins 10 000 mètres carrés : ok
                                    # Terrain en zone urbaine uniquement : ok
                                    if properties['contenance'] >= 10000:
                                        try:
                                            point_gpu = feature['geometry']['coordinates'][0][0]

                                            geometry_gpu = '{"type": "Point", "coordinates": ' + str(point_gpu) + '}'\
                                                .replace('{', '%7B') \
                                                .replace('"', '%22') \
                                                .replace(':', '%3A') \
                                                .replace(' ', '%20') \
                                                .replace(',', '%2C') \
                                                .replace(' ', '%20') \
                                                .replace('[', '%5B') \
                                                .replace(']', '%5D') \
                                                .replace('}', '%7D')

                                            base_url_gpu = 'https://apicarto.ign.fr/api'

                                            api_gpu = '/gpu/zone-urba'

                                            url_gpu = base_url_gpu + api_gpu + '?geom=' + geometry_gpu

                                            payload_gpu = {}

                                            headers_gpu = {}

                                            response_gpu = requests.get(url_gpu, headers=headers_gpu,
                                                                        data=payload_gpu)

                                            data_response_gpu = json.loads(response_gpu.text)

                                            features1 = data_response_gpu['features']

                                            if len(features1) >= 1:
                                                for feature1 in features1:
                                                    typezone = feature1['properties']['typezone']
                                                    libelle = feature1['properties']['libelle']
                                                    libelong = feature1['properties']['libelong']
                                                    urlfic = feature1['properties']['urlfic']

                                                    if libelle is None:
                                                        libelle = 'null'

                                                    if libelong is None:
                                                        libelong = 'null'

                                                    if urlfic is None:
                                                        urlfic = 'null'

                                                    print('urlfic : ' + str(urlfic))

                                                    if str(typezone) in array_zonages_urbaines:
                                                        try:
                                                            lon = str(coordinates[0][0][0])

                                                            lat = str(coordinates[0][0][1])

                                                            url_adresse = "https://api-adresse.data.gouv.fr/reverse/?lon=" \
                                                                          + lon + "&lat=" + lat

                                                            payload = {}

                                                            headers = {}

                                                            response_adresse_postale_reverse = requests.request(
                                                                "GET",
                                                                url_adresse,
                                                                headers=headers,
                                                                data=payload)

                                                            json_format_adresse_postale_reverse = json.loads(
                                                                response_adresse_postale_reverse.text)

                                                            if len(json_format_adresse_postale_reverse[
                                                                       'features']) != 0:
                                                                for feature_adresse in json_format_adresse_postale_reverse['features']:
                                                                    try:
                                                                        if feature_adresse['properties']['label'] != '':
                                                                            x = {
                                                                                "adresse_postale": str(feature_adresse['properties']['label']),
                                                                                "prefixe_parcelle": str(properties['prefixe']),
                                                                                "section_parcelle": str(properties['section']),
                                                                                "numero_parcelle": str(properties['numero']),
                                                                                "contenance_parcelle": str(properties['contenance']),
                                                                                "url_geoportail_carte": "https://www.geoportail.gouv.fr/carte",
                                                                                "coordonnees_gps": "Coordonnées : " + lat + " " + lon,
                                                                                "typezone": str(typezone),
                                                                                "libelle": str(libelle),
                                                                                "libelong": str(libelong),
                                                                                "urlfic": str(urlfic)
                                                                            }

                                                                            try:
                                                                                connection = pymysql.connect(
                                                                                    host='localhost',
                                                                                    port=3306,
                                                                                    user='root',
                                                                                    password='8h0NEJkEf3lyCBUoPQwCHSu@@@@@@@',
                                                                                    db='parcelles',
                                                                                    charset='utf8mb4',
                                                                                    cursorclass=pymysql.cursors.DictCursor
                                                                                )

                                                                                with connection.cursor() as cursor:
                                                                                    try:
                                                                                        sql = "insert into parcelles_rtg_z_u " \
                                                                                              "(adresse_postale, " \
                                                                                              "prefixe_parcelle, " \
                                                                                              "section_parcelle, " \
                                                                                              "numero_parcelle, " \
                                                                                              "contenance_parcelle, " \
                                                                                              "url_geoportail_carte, " \
                                                                                              "coordonnees_gps, " \
                                                                                              "typezone, " \
                                                                                              "libelle, " \
                                                                                              "libelong, " \
                                                                                              "urlfic" \
                                                                                              ") " \
                                                                                              "value (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

                                                                                        cursor.execute(sql, (x.get('adresse_postale'),
                                                                                                             x.get('prefixe_parcelle'),
                                                                                                             x.get('section_parcelle'),
                                                                                                             x.get('numero_parcelle'),
                                                                                                             x.get('contenance_parcelle'),
                                                                                                             x.get('url_geoportail_carte'),
                                                                                                             x.get('coordonnees_gps'),
                                                                                                             x.get('typezone'),
                                                                                                             x.get('libelle'),
                                                                                                             x.get('libelong'),
                                                                                                             x.get('urlfic')))

                                                                                        connection.commit()

                                                                                        connection.close()

                                                                                        print("land : " + x.get('adresse_postale') + " : ok")
                                                                                    except Exception as e:
                                                                                        print("The record already "
                                                                                              "exists : " + str(e))
                                                                                        connection.close()
                                                                            except Exception as e:
                                                                                print('There is a problem : ' + str(e))

                                                                            break
                                                                    except Exception as e:
                                                                        print(
                                                                            'error feature_adresse : ' + str(e))
                                                        except Exception as e:
                                                            print('error libelle urbain : ' + str(e))
                                                    else:
                                                        print('ville : ' + str(commune['nom']) + ' , code insee : '
                                                              + str(commune['code']) + ' , not urban land : '
                                                              + str(properties['prefixe'] + properties['section']
                                                                    + properties['numero']) + " _ typezone : " + str(typezone))
                                            else:
                                                print('no features ville : ' + str(commune['nom']) + ' , code insee : '
                                                      + str(commune['code']) + ' , not suitable land : '
                                                      + str(properties['prefixe'] + properties['section']
                                                            + properties['numero']))
                                        except Exception as e:
                                            print('error terrain > 10000 m² : ' + str(e))
                                    else:
                                        print('ville : ' + str(commune['nom'])
                                              + ' , code insee : ' + str(commune['code'])
                                              + ' , not suitable land : '
                                              + str(properties['prefixe']
                                                    + properties['section']
                                                    + properties['numero']) + " < 10000")
                                except Exception as e:
                                    print('error feature : ' + str(e))

                            json_file.close()

                            # delete gz file and json file
                            os.remove(gz_filename[:-3])
                            os.remove(gz_filename)
                        else:
                            print('not suitable commune : ' + str(code_insee_commune))
                    except Exception as e:
                        print("error commune : " + str(e))
        except Exception as e:
            print('error main : ' + str(e))

    def test_show_all_suitable_parcelles_for_injecting_gas_in_france_in_gas_transport_network_into_excel_in_zone_urbaine_for_some_departments_into_mysql_2(self):
        print("test_show_all_suitable_parcelles_for_injecting_gas_in_france_in_gas_transport_network_into_excel_in_zone_urbaine_for_some_departments_into_mysql_2")

        try:
            # array_zonages_urbaines
            array_zonages_urbaines = ['AU', 'NA', 'NB', 'U', 'UA', 'UB', 'UC', 'UD', 'UE', 'UI', 'UY', 'UP']

            departements = ['75', '77', '78', '91', '92', '93', '94', '95']

            url = "https://geo.api.gouv.fr/communes?fields=nom,code,codesPostaux,codeDepartement,codeRegion,population&format=json&geometry=centre"

            payload = {}

            headers = {}

            response_communes = requests.request("GET", url, headers=headers, data=payload)

            communes = response_communes.json()

            about_parcelles = "parcelles"

            print('start main for loop')

            for commune in communes:
                try:
                    code_insee_departement = commune['codeDepartement']

                    code_insee_commune = commune['code']

                    population = commune['population']

                    if code_insee_departement not in departements:
                        if population <= 10000:
                            url_zip_file_for_parcelles = "https://cadastre.data.gouv.fr/data/etalab-cadastre/latest/geojson/communes/" \
                                                         + code_insee_departement + "/" \
                                                         + code_insee_commune + "/cadastre-" + code_insee_commune \
                                                         + "-" + about_parcelles + ".json.gz"

                            resp = requests.get(url_zip_file_for_parcelles, stream=True)

                            # donwload gz file
                            gz_filename = "cadastre-" + code_insee_commune + "-" + about_parcelles + ".json.gz"
                            gz_file = open(gz_filename, 'wb')
                            gz_file.write(resp.content)
                            gz_file.close()

                            # extract json file
                            input_file = gzip.GzipFile(gz_filename, 'rb')
                            s = input_file.read()
                            input_file.close()
                            output_file = open(gz_filename[:-3], 'wb')
                            output_file.write(s)
                            output_file.close()

                            json_file = open(gz_filename[:-3])
                            data = json.loads(json_file.read())

                            for feature in data['features']:
                                try:
                                    properties = feature['properties']

                                    coordinates = feature['geometry']['coordinates']

                                    # Terrain mesurant au moins 10 000 mètres carrés : ok
                                    # Terrain en zone urbaine uniquement : ok
                                    if properties['contenance'] >= 10000:
                                        try:
                                            point_gpu = feature['geometry']['coordinates'][0][0]

                                            geometry_gpu = '{"type": "Point", "coordinates": ' + str(point_gpu) + '}'\
                                                .replace('{', '%7B') \
                                                .replace('"', '%22') \
                                                .replace(':', '%3A') \
                                                .replace(' ', '%20') \
                                                .replace(',', '%2C') \
                                                .replace(' ', '%20') \
                                                .replace('[', '%5B') \
                                                .replace(']', '%5D') \
                                                .replace('}', '%7D')

                                            base_url_gpu = 'https://apicarto.ign.fr/api'

                                            api_gpu = '/gpu/zone-urba'

                                            url_gpu = base_url_gpu + api_gpu + '?geom=' + geometry_gpu

                                            payload_gpu = {}

                                            headers_gpu = {}

                                            response_gpu = requests.get(url_gpu, headers=headers_gpu,
                                                                        data=payload_gpu)

                                            data_response_gpu = json.loads(response_gpu.text)

                                            features1 = data_response_gpu['features']

                                            if len(features1) >= 1:
                                                for feature1 in features1:
                                                    typezone = feature1['properties']['typezone']
                                                    libelle = feature1['properties']['libelle']
                                                    libelong = feature1['properties']['libelong']
                                                    urlfic = feature1['properties']['urlfic']

                                                    if libelle is None:
                                                        libelle = 'null'

                                                    if libelong is None:
                                                        libelong = 'null'

                                                    if urlfic is None:
                                                        urlfic = 'null'

                                                    print('urlfic : ' + str(urlfic))

                                                    if str(typezone) in array_zonages_urbaines:
                                                        try:
                                                            lon = str(coordinates[0][0][0])

                                                            lat = str(coordinates[0][0][1])

                                                            url_adresse = "https://api-adresse.data.gouv.fr/reverse/?lon=" \
                                                                          + lon + "&lat=" + lat

                                                            payload = {}

                                                            headers = {}

                                                            response_adresse_postale_reverse = requests.request(
                                                                "GET",
                                                                url_adresse,
                                                                headers=headers,
                                                                data=payload)

                                                            json_format_adresse_postale_reverse = json.loads(
                                                                response_adresse_postale_reverse.text)

                                                            if len(json_format_adresse_postale_reverse[
                                                                       'features']) != 0:
                                                                for feature_adresse in json_format_adresse_postale_reverse['features']:
                                                                    try:
                                                                        if feature_adresse['properties']['label'] != '':
                                                                            x = {
                                                                                "adresse_postale": str(feature_adresse['properties']['label']),
                                                                                "prefixe_parcelle": str(properties['prefixe']),
                                                                                "section_parcelle": str(properties['section']),
                                                                                "numero_parcelle": str(properties['numero']),
                                                                                "contenance_parcelle": str(properties['contenance']),
                                                                                "url_geoportail_carte": "https://www.geoportail.gouv.fr/carte",
                                                                                "coordonnees_gps": "Coordonnées : " + lat + " " + lon,
                                                                                "typezone": str(typezone),
                                                                                "libelle": str(libelle),
                                                                                "libelong": str(libelong),
                                                                                "urlfic": str(urlfic)
                                                                            }

                                                                            try:
                                                                                connection = pymysql.connect(
                                                                                    host='localhost',
                                                                                    port=3306,
                                                                                    user='root',
                                                                                    password='8h0NEJkEf3lyCBUoPQwCHSu@@@@@@@',
                                                                                    db='parcelles',
                                                                                    charset='utf8mb4',
                                                                                    cursorclass=pymysql.cursors.DictCursor
                                                                                )

                                                                                with connection.cursor() as cursor:
                                                                                    try:
                                                                                        sql = "insert into parcelles_rtg_z_u " \
                                                                                              "(adresse_postale, " \
                                                                                              "prefixe_parcelle, " \
                                                                                              "section_parcelle, " \
                                                                                              "numero_parcelle, " \
                                                                                              "contenance_parcelle, " \
                                                                                              "url_geoportail_carte, " \
                                                                                              "coordonnees_gps, " \
                                                                                              "typezone, " \
                                                                                              "libelle, " \
                                                                                              "libelong, " \
                                                                                              "urlfic" \
                                                                                              ") " \
                                                                                              "value (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

                                                                                        cursor.execute(sql, (x.get('adresse_postale'),
                                                                                                             x.get('prefixe_parcelle'),
                                                                                                             x.get('section_parcelle'),
                                                                                                             x.get('numero_parcelle'),
                                                                                                             x.get('contenance_parcelle'),
                                                                                                             x.get('url_geoportail_carte'),
                                                                                                             x.get('coordonnees_gps'),
                                                                                                             x.get('typezone'),
                                                                                                             x.get('libelle'),
                                                                                                             x.get('libelong'),
                                                                                                             x.get('urlfic')))

                                                                                        connection.commit()

                                                                                        connection.close()

                                                                                        print("land : " + x.get('adresse_postale') + " : ok")
                                                                                    except Exception as e:
                                                                                        print("The record already "
                                                                                              "exists : " + str(e))
                                                                                        connection.close()
                                                                            except Exception as e:
                                                                                print('There is a problem : ' + str(e))

                                                                            break
                                                                    except Exception as e:
                                                                        print(
                                                                            'error feature_adresse : ' + str(e))
                                                        except Exception as e:
                                                            print('error libelle urbain : ' + str(e))
                                                    else:
                                                        print('ville : ' + str(commune['nom']) + ' , code insee : '
                                                              + str(commune['code']) + ' , not urban land : '
                                                              + str(properties['prefixe'] + properties['section']
                                                                    + properties['numero']) + " _ typezone : " + str(typezone))
                                            else:
                                                print('no features ville : ' + str(commune['nom']) + ' , code insee : '
                                                      + str(commune['code']) + ' , not suitable land : '
                                                      + str(properties['prefixe'] + properties['section']
                                                            + properties['numero']))
                                        except Exception as e:
                                            print('error terrain > 10000 m² : ' + str(e))
                                    else:
                                        print('ville : ' + str(commune['nom'])
                                              + ' , code insee : ' + str(commune['code'])
                                              + ' , not suitable land : '
                                              + str(properties['prefixe']
                                                    + properties['section']
                                                    + properties['numero']) + " < 10000")
                                except Exception as e:
                                    print('error feature : ' + str(e))

                            json_file.close()

                            # delete gz file and json file
                            os.remove(gz_filename[:-3])
                            os.remove(gz_filename)
                        else:
                            print('not suitable commune : ' + str(code_insee_commune))
                except Exception as e:
                    print("error commune : " + str(e))
        except Exception as e:
            print('error main : ' + str(e))

    def test_show_all_suitable_parcelles_for_injecting_gas_in_france_in_gas_transport_network_into_excel_in_zone_urbaine_for_some_departments_into_mysql_3(self):
        print("test_show_all_suitable_parcelles_for_injecting_gas_in_france_in_gas_transport_network_into_excel_in_zone_urbaine_for_some_departments_into_mysql_3")

        try:
            # array_zonages_urbaines
            array_zonages_urbaines = ['U', 'UA', 'UB', 'UC', 'UD', 'UE', 'UI', 'UY', 'UP']

            # array_code_insee_communes_desservies_par_reseau_transport_gaz
            print('starting array_code_insee_communes_desservies_par_reseau_transport_gaz')
            array_code_insee_communes_desservies_par_reseau_transport_gaz = []
            f = open('trace-du-reseau-grt-250.json', "r")
            data = json.loads(f.read())
            for dataset in data:
                try:
                    lon = str(dataset["geometry"]["coordinates"][0])
                    lat = str(dataset["geometry"]["coordinates"][1])
                    url = "https://api-adresse.data.gouv.fr/reverse/?lon=" + lon + "&lat=" + lat
                    payload = {}
                    headers = {}
                    response = requests.request("GET", url, headers=headers, data=payload)
                    json_format = json.loads(response.text)
                    code_insee_commune = str(json_format['features'][0]['properties']['citycode'])
                    print('code_insee_commune : ' + str(code_insee_commune))
                    array_code_insee_communes_desservies_par_reseau_transport_gaz.append(code_insee_commune)
                except Exception as e:
                    print('error : ' + str(e))
            f.close()

            # array of the cities have at least one train station for travellers
            print('starting array_code_insee_commune_with_train_station_for_travellers')
            array_code_insee_commune_with_train_station_for_travellers = []
            f = open('gares_ferroviaires_de_tous_types_exploitees_ou_non.json', "r")
            data = json.loads(f.read())
            for feature in data:
                code_postal = feature['fields']['cp']

                nom = feature['fields']['ville']

                url = "https://geo.api.gouv.fr/communes?codePostal=" + str(code_postal)

                payload = {}
                headers = {}

                response = requests.request("GET", url, headers=headers, data=payload)

                informations_pour_une_commune_avec_son_code_postal = response.json()

                for commune in informations_pour_une_commune_avec_son_code_postal:
                    if commune['nom'] == nom and 'Voyageur' in feature['fields']['nature']:
                        array_code_insee_commune_with_train_station_for_travellers.append(str(commune['code']))
                        print('commune voyageur : ' + str(commune['code']))
                    else:
                        print('commune non voyageur : ' + str(commune['code']))
            f.close()

            departements = ['77', '78', '91', '95', '75', '92', '93', '94']

            url = "https://geo.api.gouv.fr/communes?fields=nom,code,codesPostaux,codeDepartement,codeRegion,population&format=json&geometry=centre"

            payload = {}

            headers = {}

            response_communes = requests.request("GET", url, headers=headers, data=payload)

            communes = response_communes.json()

            about_parcelles = "parcelles"

            print('start main for loop')

            for commune in communes:
                try:
                    code_insee_departement = commune['codeDepartement']

                    code_insee_commune = commune['code']

                    population = commune['population']

                    # Communes desservies par le réseau de transport de gaz : ok
                    # Communes ayant au moins une gare de train pour les voyageurs : ok
                    if (code_insee_commune in array_code_insee_commune_with_train_station_for_travellers) \
                            and (code_insee_commune in array_code_insee_communes_desservies_par_reseau_transport_gaz) \
                            and population <= 10000\
                            and code_insee_departement not in departements:
                        url_zip_file_for_parcelles = "https://cadastre.data.gouv.fr/data/etalab-cadastre/latest/geojson/communes/" \
                                                     + code_insee_departement + "/" \
                                                     + code_insee_commune + "/cadastre-" + code_insee_commune \
                                                     + "-" + about_parcelles + ".json.gz"

                        resp = requests.get(url_zip_file_for_parcelles, stream=True)

                        # donwload gz file
                        gz_filename = "cadastre-" + code_insee_commune + "-" + about_parcelles + ".json.gz"
                        gz_file = open(gz_filename, 'wb')
                        gz_file.write(resp.content)
                        gz_file.close()

                        # extract json file
                        input_file = gzip.GzipFile(gz_filename, 'rb')
                        s = input_file.read()
                        input_file.close()
                        output_file = open(gz_filename[:-3], 'wb')
                        output_file.write(s)
                        output_file.close()

                        json_file = open(gz_filename[:-3])
                        data = json.loads(json_file.read())

                        for feature in data['features']:
                            try:
                                properties = feature['properties']

                                coordinates = feature['geometry']['coordinates']

                                # Terrain mesurant au moins 10 000 mètres carrés : ok
                                # Terrain en zone urbaine uniquement : ok
                                if properties['contenance'] >= 10000:
                                    try:
                                        point_gpu = feature['geometry']['coordinates'][0][0]

                                        geometry_gpu = '{"type": "Point", "coordinates": ' + str(point_gpu) + '}'\
                                            .replace('{', '%7B') \
                                            .replace('"', '%22') \
                                            .replace(':', '%3A') \
                                            .replace(' ', '%20') \
                                            .replace(',', '%2C') \
                                            .replace(' ', '%20') \
                                            .replace('[', '%5B') \
                                            .replace(']', '%5D') \
                                            .replace('}', '%7D')

                                        base_url_gpu = 'https://apicarto.ign.fr/api'

                                        api_gpu = '/gpu/zone-urba'

                                        url_gpu = base_url_gpu + api_gpu + '?geom=' + geometry_gpu

                                        payload_gpu = {}

                                        headers_gpu = {}

                                        response_gpu = requests.get(url_gpu, headers=headers_gpu,
                                                                    data=payload_gpu)

                                        data_response_gpu = json.loads(response_gpu.text)

                                        features1 = data_response_gpu['features']

                                        if len(features1) >= 1:
                                            for feature1 in features1:
                                                typezone = feature1['properties']['typezone']
                                                libelle = feature1['properties']['libelle']
                                                libelong = feature1['properties']['libelong']
                                                urlfic = feature1['properties']['urlfic']

                                                if libelle is None:
                                                    libelle = 'null'

                                                if libelong is None:
                                                    libelong = 'null'

                                                if urlfic is None:
                                                    urlfic = 'null'

                                                if str(typezone) in array_zonages_urbaines:
                                                    try:
                                                        lon = str(coordinates[0][0][0])

                                                        lat = str(coordinates[0][0][1])

                                                        url_adresse = "https://api-adresse.data.gouv.fr/reverse/?lon=" \
                                                                      + lon + "&lat=" + lat

                                                        payload = {}

                                                        headers = {}

                                                        response_adresse_postale_reverse = requests.request(
                                                            "GET",
                                                            url_adresse,
                                                            headers=headers,
                                                            data=payload)

                                                        json_format_adresse_postale_reverse = json.loads(
                                                            response_adresse_postale_reverse.text)

                                                        if len(json_format_adresse_postale_reverse[
                                                                   'features']) != 0:
                                                            for feature_adresse in json_format_adresse_postale_reverse['features']:
                                                                try:
                                                                    if feature_adresse['properties']['label'] != '':
                                                                        x = {
                                                                            "adresse_postale": str(feature_adresse['properties']['label']),
                                                                            "prefixe_parcelle": str(properties['prefixe']),
                                                                            "section_parcelle": str(properties['section']),
                                                                            "numero_parcelle": str(properties['numero']),
                                                                            "contenance_parcelle": str(properties['contenance']),
                                                                            "url_geoportail_carte": "https://www.geoportail.gouv.fr/carte",
                                                                            "coordonnees_gps": "Coordonnées : " + lat + " " + lon,
                                                                            "typezone": str(typezone),
                                                                            "libelle": str(libelle),
                                                                            "libelong": str(libelong),
                                                                            "urlfic": str(urlfic)
                                                                        }

                                                                        try:
                                                                            connection = pymysql.connect(
                                                                                host='localhost',
                                                                                port=3306,
                                                                                user='root',
                                                                                password='8h0NEJkEf3lyCBUoPQwCHSu@@@@@@@',
                                                                                db='parcelles',
                                                                                charset='utf8mb4',
                                                                                cursorclass=pymysql.cursors.DictCursor
                                                                            )

                                                                            with connection.cursor() as cursor:
                                                                                try:
                                                                                    sql = "insert into parcelles_rtg_z_u " \
                                                                                          "(adresse_postale, " \
                                                                                          "prefixe_parcelle, " \
                                                                                          "section_parcelle, " \
                                                                                          "numero_parcelle, " \
                                                                                          "contenance_parcelle, " \
                                                                                          "url_geoportail_carte, " \
                                                                                          "coordonnees_gps, " \
                                                                                          "typezone, " \
                                                                                          "libelle, " \
                                                                                          "libelong, " \
                                                                                          "urlfic" \
                                                                                          ") " \
                                                                                          "value (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

                                                                                    cursor.execute(sql, (x.get('adresse_postale'),
                                                                                                         x.get('prefixe_parcelle'),
                                                                                                         x.get('section_parcelle'),
                                                                                                         x.get('numero_parcelle'),
                                                                                                         x.get('contenance_parcelle'),
                                                                                                         x.get('url_geoportail_carte'),
                                                                                                         x.get('coordonnees_gps'),
                                                                                                         x.get('typezone'),
                                                                                                         x.get('libelle'),
                                                                                                         x.get('libelong'),
                                                                                                         x.get('urlfic')))

                                                                                    connection.commit()

                                                                                    connection.close()

                                                                                    print("land : " + x.get('adresse_postale') + " : ok")
                                                                                except Exception as e:
                                                                                    print("The record already "
                                                                                          "exists : " + str(e))
                                                                                    connection.close()
                                                                        except Exception as e:
                                                                            print('There is a problem : ' + str(e))

                                                                        break
                                                                except Exception as e:
                                                                    print(
                                                                        'error feature_adresse : ' + str(e))
                                                    except Exception as e:
                                                        print('error libelle urbain : ' + str(e))
                                                else:
                                                    print('ville : ' + str(commune['nom']) + ' , code insee : '
                                                          + str(commune['code']) + ' , not urban land : '
                                                          + str(properties['prefixe'] + properties['section']
                                                                + properties['numero']) + " _ typezone : " + str(typezone))
                                        else:
                                            print('no features ville : ' + str(commune['nom']) + ' , code insee : '
                                                  + str(commune['code']) + ' , not suitable land : '
                                                  + str(properties['prefixe'] + properties['section']
                                                        + properties['numero']))
                                    except Exception as e:
                                        print('error terrain > 10000 m² : ' + str(e))
                                else:
                                    print('ville : ' + str(commune['nom'])
                                          + ' , code insee : ' + str(commune['code'])
                                          + ' , not suitable land : '
                                          + str(properties['prefixe']
                                                + properties['section']
                                                + properties['numero']) + " < 10000")
                            except Exception as e:
                                print('error feature : ' + str(e))

                        json_file.close()

                        # delete gz file and json file
                        os.remove(gz_filename[:-3])
                        os.remove(gz_filename)
                    else:
                        print('not suitable commune : ' + str(code_insee_commune))
                except Exception as e:
                    print("error commune : " + str(e))
        except Exception as e:
            print('error main : ' + str(e))

    def test_show_all_suitable_parcelles_for_injecting_gas_in_france_in_gas_transport_network_into_excel_in_zone_urbaine_for_some_departments_into_mysql_4(self):
        print("test_show_all_suitable_parcelles_for_injecting_gas_in_france_in_gas_transport_network_into_excel_in_zone_urbaine_for_some_departments_into_mysql_4")

        departements = ['77', '78', '91', '95', '75', '92', '93', '94']

        try:
            # array_zonages_urbaines
            array_zonages_urbaines = ['U', 'UA', 'UB', 'UC', 'UD', 'UE', 'UI', 'UY', 'UP']

            # array_code_insee_communes_desservies_par_reseau_transport_gaz
            print('starting array_code_insee_communes_desservies_par_reseau_transport_gaz')
            array_code_insee_communes_desservies_par_reseau_transport_gaz = []
            f = open('trace-du-reseau-grt-250.json', "r")
            data = json.loads(f.read())
            for dataset in data:
                try:
                    lon = str(dataset["geometry"]["coordinates"][0])
                    lat = str(dataset["geometry"]["coordinates"][1])
                    url = "https://api-adresse.data.gouv.fr/reverse/?lon=" + lon + "&lat=" + lat
                    payload = {}
                    headers = {}
                    response = requests.request("GET", url, headers=headers, data=payload)
                    json_format = json.loads(response.text)
                    code_insee_commune = str(json_format['features'][0]['properties']['citycode'])
                    print('code_insee_commune : ' + str(code_insee_commune))
                    array_code_insee_communes_desservies_par_reseau_transport_gaz.append(code_insee_commune)
                except Exception as e:
                    print('error : ' + str(e))
            f.close()

            # array of the cities have at least one train station for travellers
            print('starting array_code_insee_commune_with_train_station_for_travellers')
            array_code_insee_commune_with_train_station_for_travellers = []
            f = open('gares_ferroviaires_de_tous_types_exploitees_ou_non.json', "r")
            data = json.loads(f.read())
            for feature in data:
                code_postal = feature['fields']['cp']

                nom = feature['fields']['ville']

                url = "https://geo.api.gouv.fr/communes?codePostal=" + str(code_postal)

                payload = {}
                headers = {}

                response = requests.request("GET", url, headers=headers, data=payload)

                informations_pour_une_commune_avec_son_code_postal = response.json()

                for commune in informations_pour_une_commune_avec_son_code_postal:
                    if commune['nom'] == nom and 'Voyageur' in feature['fields']['nature']:
                        array_code_insee_commune_with_train_station_for_travellers.append(str(commune['code']))
                        print('commune voyageur : ' + str(commune['code']))
                    else:
                        print('commune non voyageur : ' + str(commune['code']))
            f.close()

            about_parcelles = "parcelles"

            print('start main for loop')

            payload = {}

            headers = {}

            for i in range(1000, 95999):
                try:
                    url = ""

                    if i < 9999:
                        url += "https://geo.api.gouv.fr/communes/0" + str(i) + "?fields=nom,code,codesPostaux," \
                                                                               "codeDepartement,codeRegion,population" \
                                                                               "&format=json&geometry=centre"
                    else:
                        url += "https://geo.api.gouv.fr/communes/" + str(i) + "?fields=nom,code,codesPostaux," \
                                                                              "codeDepartement,codeRegion,population" \
                                                                              "&format=json&geometry=centre"

                    try:
                        response = requests.request("GET", url, headers=headers, data=payload)

                        commune = json.loads(response.text)

                        code_insee_departement = commune['codeDepartement']

                        code_insee_commune = commune['code']

                        population = commune['population']

                        # Communes desservies par le réseau de transport de gaz : ok
                        # Communes ayant au moins une gare de train pour les voyageurs : ok
                        if (code_insee_commune in array_code_insee_commune_with_train_station_for_travellers) \
                                and (
                                code_insee_commune in array_code_insee_communes_desservies_par_reseau_transport_gaz) \
                                and population <= 10000 \
                                and code_insee_departement not in departements:
                            url_zip_file_for_parcelles = "https://cadastre.data.gouv.fr/data/etalab-cadastre/latest/geojson/communes/" \
                                                         + code_insee_departement + "/" \
                                                         + code_insee_commune + "/cadastre-" + code_insee_commune \
                                                         + "-" + about_parcelles + ".json.gz"

                            resp = requests.get(url_zip_file_for_parcelles, stream=True)

                            # donwload gz file
                            gz_filename = "cadastre-" + code_insee_commune + "-" + about_parcelles + ".json.gz"
                            gz_file = open(gz_filename, 'wb')
                            gz_file.write(resp.content)
                            gz_file.close()

                            # extract json file
                            input_file = gzip.GzipFile(gz_filename, 'rb')
                            s = input_file.read()
                            input_file.close()
                            output_file = open(gz_filename[:-3], 'wb')
                            output_file.write(s)
                            output_file.close()

                            json_file = open(gz_filename[:-3])
                            data = json.loads(json_file.read())

                            for feature in data['features']:
                                try:
                                    properties = feature['properties']

                                    coordinates = feature['geometry']['coordinates']

                                    # Terrain mesurant au moins 10 000 mètres carrés : ok
                                    # Terrain en zone urbaine uniquement : ok
                                    if properties['contenance'] >= 10000:
                                        try:
                                            point_gpu = feature['geometry']['coordinates'][0][0]

                                            geometry_gpu = '{"type": "Point", "coordinates": ' + str(point_gpu) + '}' \
                                                .replace('{', '%7B') \
                                                .replace('"', '%22') \
                                                .replace(':', '%3A') \
                                                .replace(' ', '%20') \
                                                .replace(',', '%2C') \
                                                .replace(' ', '%20') \
                                                .replace('[', '%5B') \
                                                .replace(']', '%5D') \
                                                .replace('}', '%7D')

                                            base_url_gpu = 'https://apicarto.ign.fr/api'

                                            api_gpu = '/gpu/zone-urba'

                                            url_gpu = base_url_gpu + api_gpu + '?geom=' + geometry_gpu

                                            payload_gpu = {}

                                            headers_gpu = {}

                                            response_gpu = requests.get(url_gpu, headers=headers_gpu,
                                                                        data=payload_gpu)

                                            data_response_gpu = json.loads(response_gpu.text)

                                            features1 = data_response_gpu['features']

                                            if len(features1) >= 1:
                                                for feature1 in features1:
                                                    typezone = feature1['properties']['typezone']
                                                    libelle = feature1['properties']['libelle']
                                                    libelong = feature1['properties']['libelong']
                                                    urlfic = feature1['properties']['urlfic']

                                                    if libelle is None:
                                                        libelle = 'null'

                                                    if libelong is None:
                                                        libelong = 'null'

                                                    if urlfic is None:
                                                        urlfic = 'null'

                                                    if str(typezone) in array_zonages_urbaines:
                                                        try:
                                                            lon = str(coordinates[0][0][0])

                                                            lat = str(coordinates[0][0][1])

                                                            url_adresse = "https://api-adresse.data.gouv.fr/reverse/?lon=" \
                                                                          + lon + "&lat=" + lat

                                                            payload = {}

                                                            headers = {}

                                                            response_adresse_postale_reverse = requests.request(
                                                                "GET",
                                                                url_adresse,
                                                                headers=headers,
                                                                data=payload)

                                                            json_format_adresse_postale_reverse = json.loads(
                                                                response_adresse_postale_reverse.text)

                                                            if len(json_format_adresse_postale_reverse[
                                                                       'features']) != 0:
                                                                for feature_adresse in \
                                                                json_format_adresse_postale_reverse['features']:
                                                                    try:
                                                                        if feature_adresse['properties']['label'] != '':
                                                                            x = {
                                                                                "adresse_postale": str(
                                                                                    feature_adresse['properties'][
                                                                                        'label']),
                                                                                "prefixe_parcelle": str(
                                                                                    properties['prefixe']),
                                                                                "section_parcelle": str(
                                                                                    properties['section']),
                                                                                "numero_parcelle": str(
                                                                                    properties['numero']),
                                                                                "contenance_parcelle": str(
                                                                                    properties['contenance']),
                                                                                "url_geoportail_carte": "https://www.geoportail.gouv.fr/carte",
                                                                                "coordonnees_gps": "Coordonnées : " + lat + " " + lon,
                                                                                "typezone": str(typezone),
                                                                                "libelle": str(libelle),
                                                                                "libelong": str(libelong),
                                                                                "urlfic": str(urlfic)
                                                                            }

                                                                            try:
                                                                                connection = pymysql.connect(
                                                                                    host='localhost',
                                                                                    port=3306,
                                                                                    user='root',
                                                                                    password='8h0NEJkEf3lyCBUoPQwCHSu@@@@@@@',
                                                                                    db='parcelles',
                                                                                    charset='utf8mb4',
                                                                                    cursorclass=pymysql.cursors.DictCursor
                                                                                )

                                                                                with connection.cursor() as cursor:
                                                                                    try:
                                                                                        sql = "insert into parcelles_rtg_z_u " \
                                                                                              "(adresse_postale, " \
                                                                                              "prefixe_parcelle, " \
                                                                                              "section_parcelle, " \
                                                                                              "numero_parcelle, " \
                                                                                              "contenance_parcelle, " \
                                                                                              "url_geoportail_carte, " \
                                                                                              "coordonnees_gps, " \
                                                                                              "typezone, " \
                                                                                              "libelle, " \
                                                                                              "libelong, " \
                                                                                              "urlfic" \
                                                                                              ") " \
                                                                                              "value (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

                                                                                        cursor.execute(sql, (
                                                                                        x.get('adresse_postale'),
                                                                                        x.get('prefixe_parcelle'),
                                                                                        x.get('section_parcelle'),
                                                                                        x.get('numero_parcelle'),
                                                                                        x.get('contenance_parcelle'),
                                                                                        x.get('url_geoportail_carte'),
                                                                                        x.get('coordonnees_gps'),
                                                                                        x.get('typezone'),
                                                                                        x.get('libelle'),
                                                                                        x.get('libelong'),
                                                                                        x.get('urlfic')))

                                                                                        connection.commit()

                                                                                        connection.close()

                                                                                        print("land : " + x.get(
                                                                                            'adresse_postale') + " : ok")
                                                                                    except Exception as e:
                                                                                        print("The record already "
                                                                                              "exists : " + str(e))
                                                                                        connection.close()
                                                                            except Exception as e:
                                                                                print('There is a problem : ' + str(e))

                                                                            break
                                                                    except Exception as e:
                                                                        print(
                                                                            'error feature_adresse : ' + str(e))
                                                        except Exception as e:
                                                            print('error libelle urbain : ' + str(e))
                                                    else:
                                                        print('ville : ' + str(commune['nom']) + ' , code insee : '
                                                              + str(commune['code']) + ' , not urban land : '
                                                              + str(properties['prefixe'] + properties['section']
                                                                    + properties['numero']) + " _ typezone : " + str(
                                                            typezone))
                                            else:
                                                print('no features ville : ' + str(commune['nom']) + ' , code insee : '
                                                      + str(commune['code']) + ' , not suitable land : '
                                                      + str(properties['prefixe'] + properties['section']
                                                            + properties['numero']))
                                        except Exception as e:
                                            print('error terrain > 10000 m² : ' + str(e))
                                    else:
                                        print('ville : ' + str(commune['nom'])
                                              + ' , code insee : ' + str(commune['code'])
                                              + ' , not suitable land : '
                                              + str(properties['prefixe']
                                                    + properties['section']
                                                    + properties['numero']) + " < 10000")
                                except Exception as e:
                                    print('error feature : ' + str(e))

                            json_file.close()

                            # delete gz file and json file
                            os.remove(gz_filename[:-3])
                            os.remove(gz_filename)
                        else:
                            print('not suitable commune : ' + str(code_insee_commune))
                    except Exception as e:
                        print("error response commune : " + str(e))
                except Exception as e:
                    print("error commune : " + str(e))
        except Exception as e:
            print('error main : ' + str(e))

    def test_show_all_cities_linked_with_a_gas_network_in_france_v1(self):
        print("test_show_all_cities_linked_with_a_gas_network_in_france_v1")

        array_code_insee_commune_desservies_par_gaz_v1 = []
        f = open('communes-desservies-en-gaz_v1.json', "r")
        data = json.loads(f.read())
        for dataset in data:
            code_insee_commune = dataset['fields']['code_insee_commune'][1:]
            array_code_insee_commune_desservies_par_gaz_v1.append(str(code_insee_commune))
            print(str(code_insee_commune))
        f.close()

    def test_show_all_suitable_parcelles_for_injecting_gas_in_france_in_gas_transport_network_into_excel_in_zone_urbaine_for_some_departments_into_mysql_5(self):
        print("test_show_all_suitable_parcelles_for_injecting_gas_in_france_in_gas_transport_network_into_excel_in_zone_urbaine_for_some_departments_into_mysql_4")

        departements = ['77', '78', '91', '95', '75', '92', '93', '94']

        try:
            # array_zonages_urbaines
            array_zonages_urbaines = ['U', 'UA', 'UB', 'UC', 'UD', 'UE', 'UI', 'UY', 'UP']

            # array_code_insee_commune_desservies_par_gaz_v1
            print("starting array_code_insee_commune_desservies_par_gaz_v1")
            array_code_insee_commune_desservies_par_gaz_v1 = []
            f = open('communes-desservies-en-gaz_v1.json', "r")
            data = json.loads(f.read())
            for dataset in data:
                code_insee_commune = dataset['fields']['code_insee_commune'][1:]
                array_code_insee_commune_desservies_par_gaz_v1.append(str(code_insee_commune))
                print("code insee commune array_code_insee_commune_desservies_par_gaz_v1 : " + str(code_insee_commune))
            f.close()

            # array_code_insee_communes_desservies_par_reseau_transport_gaz
            print('starting array_code_insee_communes_desservies_par_reseau_transport_gaz')
            array_code_insee_communes_desservies_par_reseau_transport_gaz = []
            f = open('trace-du-reseau-grt-250.json', "r")
            data = json.loads(f.read())
            for dataset in data:
                try:
                    lon = str(dataset["geometry"]["coordinates"][0])
                    lat = str(dataset["geometry"]["coordinates"][1])
                    url = "https://api-adresse.data.gouv.fr/reverse/?lon=" + lon + "&lat=" + lat
                    payload = {}
                    headers = {}
                    response = requests.request("GET", url, headers=headers, data=payload)
                    json_format = json.loads(response.text)
                    code_insee_commune = str(json_format['features'][0]['properties']['citycode'])
                    print('code_insee_commune : ' + str(code_insee_commune))
                    array_code_insee_communes_desservies_par_reseau_transport_gaz.append(code_insee_commune)
                except Exception as e:
                    print('error : ' + str(e))
            f.close()

            # array of the cities have at least one train station for travellers
            print('starting array_code_insee_commune_with_train_station_for_travellers')
            array_code_insee_commune_with_train_station_for_travellers = []
            f = open('gares_ferroviaires_de_tous_types_exploitees_ou_non.json', "r")
            data = json.loads(f.read())
            for feature in data:
                code_postal = feature['fields']['cp']

                nom = feature['fields']['ville']

                url = "https://geo.api.gouv.fr/communes?codePostal=" + str(code_postal)

                payload = {}
                headers = {}

                response = requests.request("GET", url, headers=headers, data=payload)

                informations_pour_une_commune_avec_son_code_postal = response.json()

                for commune in informations_pour_une_commune_avec_son_code_postal:
                    if commune['nom'] == nom and 'Voyageur' in feature['fields']['nature']:
                        array_code_insee_commune_with_train_station_for_travellers.append(str(commune['code']))
                        print('commune voyageur : ' + str(commune['code']))
                    else:
                        print('commune non voyageur : ' + str(commune['code']))
            f.close()

            about_parcelles = "parcelles"

            print('start main for loop')

            payload = {}

            headers = {}

            for i in range(1000, 95999):
                try:
                    url = ""

                    if i < 9999:
                        url += "https://geo.api.gouv.fr/communes/0" + str(i) + "?fields=nom,code,codesPostaux," \
                                                                               "codeDepartement,codeRegion,population" \
                                                                               "&format=json&geometry=centre"
                    else:
                        url += "https://geo.api.gouv.fr/communes/" + str(i) + "?fields=nom,code,codesPostaux," \
                                                                              "codeDepartement,codeRegion,population" \
                                                                              "&format=json&geometry=centre"

                    try:
                        response = requests.request("GET", url, headers=headers, data=payload)

                        commune = json.loads(response.text)

                        code_insee_departement = commune['codeDepartement']

                        code_insee_commune = commune['code']

                        population = commune['population']

                        # Communes desservies par le réseau de transport de gaz : ok
                        # Communes ayant au moins une gare de train pour les voyageurs : ok
                        if (code_insee_commune in array_code_insee_commune_with_train_station_for_travellers) \
                                and \
                                (
                                        code_insee_commune in array_code_insee_communes_desservies_par_reseau_transport_gaz
                                    or
                                        code_insee_commune in array_code_insee_commune_desservies_par_gaz_v1
                                ) \
                                and population <= 10000 \
                                and code_insee_departement not in departements:
                            url_zip_file_for_parcelles = "https://cadastre.data.gouv.fr/data/etalab-cadastre/latest/geojson/communes/" \
                                                         + code_insee_departement + "/" \
                                                         + code_insee_commune + "/cadastre-" + code_insee_commune \
                                                         + "-" + about_parcelles + ".json.gz"

                            resp = requests.get(url_zip_file_for_parcelles, stream=True)

                            # donwload gz file
                            gz_filename = "cadastre-" + code_insee_commune + "-" + about_parcelles + ".json.gz"
                            gz_file = open(gz_filename, 'wb')
                            gz_file.write(resp.content)
                            gz_file.close()

                            # extract json file
                            input_file = gzip.GzipFile(gz_filename, 'rb')
                            s = input_file.read()
                            input_file.close()
                            output_file = open(gz_filename[:-3], 'wb')
                            output_file.write(s)
                            output_file.close()

                            json_file = open(gz_filename[:-3])
                            data = json.loads(json_file.read())

                            for feature in data['features']:
                                try:
                                    properties = feature['properties']

                                    coordinates = feature['geometry']['coordinates']

                                    # Terrain mesurant au moins 10 000 mètres carrés : ok
                                    # Terrain en zone urbaine uniquement : ok
                                    if properties['contenance'] >= 10000:
                                        try:
                                            point_gpu = feature['geometry']['coordinates'][0][0]

                                            geometry_gpu = '{"type": "Point", "coordinates": ' + str(point_gpu) + '}' \
                                                .replace('{', '%7B') \
                                                .replace('"', '%22') \
                                                .replace(':', '%3A') \
                                                .replace(' ', '%20') \
                                                .replace(',', '%2C') \
                                                .replace(' ', '%20') \
                                                .replace('[', '%5B') \
                                                .replace(']', '%5D') \
                                                .replace('}', '%7D')

                                            base_url_gpu = 'https://apicarto.ign.fr/api'

                                            api_gpu = '/gpu/zone-urba'

                                            url_gpu = base_url_gpu + api_gpu + '?geom=' + geometry_gpu

                                            payload_gpu = {}

                                            headers_gpu = {}

                                            response_gpu = requests.get(url_gpu, headers=headers_gpu,
                                                                        data=payload_gpu)

                                            data_response_gpu = json.loads(response_gpu.text)

                                            features1 = data_response_gpu['features']

                                            if len(features1) >= 1:
                                                for feature1 in features1:
                                                    typezone = feature1['properties']['typezone']
                                                    libelle = feature1['properties']['libelle']
                                                    libelong = feature1['properties']['libelong']
                                                    urlfic = feature1['properties']['urlfic']

                                                    if libelle is None:
                                                        libelle = 'null'

                                                    if libelong is None:
                                                        libelong = 'null'

                                                    if urlfic is None:
                                                        urlfic = 'null'

                                                    if str(typezone) in array_zonages_urbaines:
                                                        try:
                                                            lon = str(coordinates[0][0][0])

                                                            lat = str(coordinates[0][0][1])

                                                            url_adresse = "https://api-adresse.data.gouv.fr/reverse/?lon=" \
                                                                          + lon + "&lat=" + lat

                                                            payload = {}

                                                            headers = {}

                                                            response_adresse_postale_reverse = requests.request(
                                                                "GET",
                                                                url_adresse,
                                                                headers=headers,
                                                                data=payload)

                                                            json_format_adresse_postale_reverse = json.loads(
                                                                response_adresse_postale_reverse.text)

                                                            if len(json_format_adresse_postale_reverse[
                                                                       'features']) != 0:
                                                                for feature_adresse in \
                                                                json_format_adresse_postale_reverse['features']:
                                                                    try:
                                                                        if feature_adresse['properties']['label'] != '':
                                                                            x = {
                                                                                "adresse_postale": str(
                                                                                    feature_adresse['properties'][
                                                                                        'label']),
                                                                                "prefixe_parcelle": str(
                                                                                    properties['prefixe']),
                                                                                "section_parcelle": str(
                                                                                    properties['section']),
                                                                                "numero_parcelle": str(
                                                                                    properties['numero']),
                                                                                "contenance_parcelle": str(
                                                                                    properties['contenance']),
                                                                                "url_geoportail_carte": "https://www.geoportail.gouv.fr/carte",
                                                                                "coordonnees_gps": "Coordonnées : " + lat + " " + lon,
                                                                                "typezone": str(typezone),
                                                                                "libelle": str(libelle),
                                                                                "libelong": str(libelong),
                                                                                "urlfic": str(urlfic)
                                                                            }

                                                                            try:
                                                                                connection = pymysql.connect(
                                                                                    host='localhost',
                                                                                    port=3306,
                                                                                    user='root',
                                                                                    password='8h0NEJkEf3lyCBUoPQwCHSu@@@@@@@',
                                                                                    db='parcelles',
                                                                                    charset='utf8mb4',
                                                                                    cursorclass=pymysql.cursors.DictCursor
                                                                                )

                                                                                with connection.cursor() as cursor:
                                                                                    try:
                                                                                        sql = "insert into parcelles_rtg_z_u " \
                                                                                              "(adresse_postale, " \
                                                                                              "prefixe_parcelle, " \
                                                                                              "section_parcelle, " \
                                                                                              "numero_parcelle, " \
                                                                                              "contenance_parcelle, " \
                                                                                              "url_geoportail_carte, " \
                                                                                              "coordonnees_gps, " \
                                                                                              "typezone, " \
                                                                                              "libelle, " \
                                                                                              "libelong, " \
                                                                                              "urlfic" \
                                                                                              ") " \
                                                                                              "value (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

                                                                                        cursor.execute(sql, (
                                                                                        x.get('adresse_postale'),
                                                                                        x.get('prefixe_parcelle'),
                                                                                        x.get('section_parcelle'),
                                                                                        x.get('numero_parcelle'),
                                                                                        x.get('contenance_parcelle'),
                                                                                        x.get('url_geoportail_carte'),
                                                                                        x.get('coordonnees_gps'),
                                                                                        x.get('typezone'),
                                                                                        x.get('libelle'),
                                                                                        x.get('libelong'),
                                                                                        x.get('urlfic')))

                                                                                        connection.commit()

                                                                                        connection.close()

                                                                                        print("land : " + x.get(
                                                                                            'adresse_postale') + " : ok")
                                                                                    except Exception as e:
                                                                                        print("The record already "
                                                                                              "exists : " + str(e))
                                                                                        connection.close()
                                                                            except Exception as e:
                                                                                print('There is a problem : ' + str(e))

                                                                            break
                                                                    except Exception as e:
                                                                        print(
                                                                            'error feature_adresse : ' + str(e))
                                                        except Exception as e:
                                                            print('error libelle urbain : ' + str(e))
                                                    else:
                                                        print('ville : ' + str(commune['nom']) + ' , code insee : '
                                                              + str(commune['code']) + ' , not urban land : '
                                                              + str(properties['prefixe'] + properties['section']
                                                                    + properties['numero']) + " _ typezone : " + str(
                                                            typezone))
                                            else:
                                                print('no features ville : ' + str(commune['nom']) + ' , code insee : '
                                                      + str(commune['code']) + ' , not suitable land : '
                                                      + str(properties['prefixe'] + properties['section']
                                                            + properties['numero']))
                                        except Exception as e:
                                            print('error terrain > 10000 m² : ' + str(e))
                                    else:
                                        print('ville : ' + str(commune['nom'])
                                              + ' , code insee : ' + str(commune['code'])
                                              + ' , not suitable land : '
                                              + str(properties['prefixe']
                                                    + properties['section']
                                                    + properties['numero']) + " < 10000")
                                except Exception as e:
                                    print('error feature : ' + str(e))

                            json_file.close()

                            # delete gz file and json file
                            os.remove(gz_filename[:-3])
                            os.remove(gz_filename)
                        else:
                            print('not suitable commune : ' + str(code_insee_commune))
                    except Exception as e:
                        print("error response commune : " + str(e))
                except Exception as e:
                    print("error commune : " + str(e))
        except Exception as e:
            print('error main : ' + str(e))

    def test_show_all_suitable_parcelles_for_injecting_gas_in_france_in_gas_transport_network_into_excel_in_zone_urbaine_for_some_departments_into_mysql_6(self):
        print("test_show_all_suitable_parcelles_for_injecting_gas_in_france_in_gas_transport_network_into_excel_in_zone_urbaine_for_some_departments_into_mysql_6")

        departements = ['77', '78', '91', '95', '75', '92', '93', '94']

        try:
            # array_zonages_urbaines
            array_zonages_urbaines = ['U', 'UA', 'UB', 'UC', 'UD', 'UE', 'UI', 'UY', 'UP']

            # array_code_insee_commune_desservies_par_gaz_v1
            print("starting array_code_insee_commune_desservies_par_gaz_v1")
            array_code_insee_commune_desservies_par_gaz_v1 = []
            f = open('communes-desservies-en-gaz_v1.json', "r")
            data = json.loads(f.read())
            for dataset in data:
                code_insee_commune = dataset['fields']['code_insee_commune'][1:]
                array_code_insee_commune_desservies_par_gaz_v1.append(str(code_insee_commune))
                print("code insee commune array_code_insee_commune_desservies_par_gaz_v1 : " + str(code_insee_commune))
            f.close()

            # array_code_insee_communes_desservies_par_reseau_transport_gaz
            print('starting array_code_insee_communes_desservies_par_reseau_transport_gaz')
            array_code_insee_communes_desservies_par_reseau_transport_gaz = []
            f = open('trace-du-reseau-grt-250.json', "r")
            data = json.loads(f.read())
            for dataset in data:
                try:
                    lon = str(dataset["geometry"]["coordinates"][0])
                    lat = str(dataset["geometry"]["coordinates"][1])
                    url = "https://api-adresse.data.gouv.fr/reverse/?lon=" + lon + "&lat=" + lat
                    payload = {}
                    headers = {}
                    response = requests.request("GET", url, headers=headers, data=payload)
                    json_format = json.loads(response.text)
                    code_insee_commune = str(json_format['features'][0]['properties']['citycode'])
                    print('code_insee_commune : ' + str(code_insee_commune))
                    array_code_insee_communes_desservies_par_reseau_transport_gaz.append(code_insee_commune)
                except Exception as e:
                    print('error : ' + str(e))
            f.close()

            about_parcelles = "parcelles"

            print('start main for loop')

            payload = {}

            headers = {}

            for i in range(1000, 95999):
                try:
                    url = ""

                    if i < 9999:
                        url += "https://geo.api.gouv.fr/communes/0" + str(i) + "?fields=nom,code,codesPostaux," \
                                                                               "codeDepartement,codeRegion,population" \
                                                                               "&format=json&geometry=centre"
                    else:
                        url += "https://geo.api.gouv.fr/communes/" + str(i) + "?fields=nom,code,codesPostaux," \
                                                                              "codeDepartement,codeRegion,population" \
                                                                              "&format=json&geometry=centre"

                    try:
                        response = requests.request("GET", url, headers=headers, data=payload)

                        commune = json.loads(response.text)

                        code_insee_departement = commune['codeDepartement']

                        code_insee_commune = commune['code']

                        population = commune['population']

                        # Communes desservies par le réseau de transport de gaz : ok
                        if (code_insee_commune in array_code_insee_communes_desservies_par_reseau_transport_gaz
                            or code_insee_commune in array_code_insee_commune_desservies_par_gaz_v1) \
                                and population <= 10000 \
                                and code_insee_departement not in departements:
                            url_zip_file_for_parcelles = "https://cadastre.data.gouv.fr/data/etalab-cadastre/latest/geojson/communes/" \
                                                         + code_insee_departement + "/" \
                                                         + code_insee_commune + "/cadastre-" + code_insee_commune \
                                                         + "-" + about_parcelles + ".json.gz"

                            resp = requests.get(url_zip_file_for_parcelles, stream=True)

                            # donwload gz file
                            gz_filename = "cadastre-" + code_insee_commune + "-" + about_parcelles + ".json.gz"
                            gz_file = open(gz_filename, 'wb')
                            gz_file.write(resp.content)
                            gz_file.close()

                            # extract json file
                            input_file = gzip.GzipFile(gz_filename, 'rb')
                            s = input_file.read()
                            input_file.close()
                            output_file = open(gz_filename[:-3], 'wb')
                            output_file.write(s)
                            output_file.close()

                            json_file = open(gz_filename[:-3])
                            data = json.loads(json_file.read())

                            for feature in data['features']:
                                try:
                                    properties = feature['properties']

                                    coordinates = feature['geometry']['coordinates']

                                    # Terrain mesurant au moins 10 000 mètres carrés : ok
                                    # Terrain en zone urbaine uniquement : ok
                                    if properties['contenance'] >= 10000:
                                        try:
                                            point_gpu = feature['geometry']['coordinates'][0][0]

                                            geometry_gpu = '{"type": "Point", "coordinates": ' + str(point_gpu) + '}' \
                                                .replace('{', '%7B') \
                                                .replace('"', '%22') \
                                                .replace(':', '%3A') \
                                                .replace(' ', '%20') \
                                                .replace(',', '%2C') \
                                                .replace(' ', '%20') \
                                                .replace('[', '%5B') \
                                                .replace(']', '%5D') \
                                                .replace('}', '%7D')

                                            base_url_gpu = 'https://apicarto.ign.fr/api'

                                            api_gpu = '/gpu/zone-urba'

                                            url_gpu = base_url_gpu + api_gpu + '?geom=' + geometry_gpu

                                            payload_gpu = {}

                                            headers_gpu = {}

                                            response_gpu = requests.get(url_gpu, headers=headers_gpu,
                                                                        data=payload_gpu)

                                            data_response_gpu = json.loads(response_gpu.text)

                                            features1 = data_response_gpu['features']

                                            if len(features1) >= 1:
                                                for feature1 in features1:
                                                    typezone = feature1['properties']['typezone']
                                                    libelle = feature1['properties']['libelle']
                                                    libelong = feature1['properties']['libelong']
                                                    urlfic = feature1['properties']['urlfic']

                                                    if libelle is None:
                                                        libelle = 'null'

                                                    if libelong is None:
                                                        libelong = 'null'

                                                    if urlfic is None:
                                                        urlfic = 'null'

                                                    if str(typezone) in array_zonages_urbaines:
                                                        try:
                                                            lon = str(coordinates[0][0][0])

                                                            lat = str(coordinates[0][0][1])

                                                            url_adresse = "https://api-adresse.data.gouv.fr/reverse/?lon=" \
                                                                          + lon + "&lat=" + lat

                                                            payload = {}

                                                            headers = {}

                                                            response_adresse_postale_reverse = requests.request(
                                                                "GET",
                                                                url_adresse,
                                                                headers=headers,
                                                                data=payload)

                                                            json_format_adresse_postale_reverse = json.loads(
                                                                response_adresse_postale_reverse.text)

                                                            if len(json_format_adresse_postale_reverse[
                                                                       'features']) != 0:
                                                                for feature_adresse in \
                                                                json_format_adresse_postale_reverse['features']:
                                                                    try:
                                                                        if feature_adresse['properties']['label'] != '':
                                                                            x = {
                                                                                "adresse_postale": str(
                                                                                    feature_adresse['properties'][
                                                                                        'label']),
                                                                                "prefixe_parcelle": str(
                                                                                    properties['prefixe']),
                                                                                "section_parcelle": str(
                                                                                    properties['section']),
                                                                                "numero_parcelle": str(
                                                                                    properties['numero']),
                                                                                "contenance_parcelle": str(
                                                                                    properties['contenance']),
                                                                                "url_geoportail_carte": "https://www.geoportail.gouv.fr/carte",
                                                                                "coordonnees_gps": "Coordonnées : " + lat + " " + lon,
                                                                                "typezone": str(typezone),
                                                                                "libelle": str(libelle),
                                                                                "libelong": str(libelong),
                                                                                "urlfic": str(urlfic)
                                                                            }

                                                                            try:
                                                                                connection = pymysql.connect(
                                                                                    host='localhost',
                                                                                    port=3306,
                                                                                    user='root',
                                                                                    password='8h0NEJkEf3lyCBUoPQwCHSu@@@@@@@',
                                                                                    db='parcelles',
                                                                                    charset='utf8mb4',
                                                                                    cursorclass=pymysql.cursors.DictCursor
                                                                                )

                                                                                with connection.cursor() as cursor:
                                                                                    try:
                                                                                        sql = "insert into parcelles_rtg_z_u " \
                                                                                              "(adresse_postale, " \
                                                                                              "prefixe_parcelle, " \
                                                                                              "section_parcelle, " \
                                                                                              "numero_parcelle, " \
                                                                                              "contenance_parcelle, " \
                                                                                              "url_geoportail_carte, " \
                                                                                              "coordonnees_gps, " \
                                                                                              "typezone, " \
                                                                                              "libelle, " \
                                                                                              "libelong, " \
                                                                                              "urlfic" \
                                                                                              ") " \
                                                                                              "value (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

                                                                                        cursor.execute(sql, (
                                                                                        x.get('adresse_postale'),
                                                                                        x.get('prefixe_parcelle'),
                                                                                        x.get('section_parcelle'),
                                                                                        x.get('numero_parcelle'),
                                                                                        x.get('contenance_parcelle'),
                                                                                        x.get('url_geoportail_carte'),
                                                                                        x.get('coordonnees_gps'),
                                                                                        x.get('typezone'),
                                                                                        x.get('libelle'),
                                                                                        x.get('libelong'),
                                                                                        x.get('urlfic')))

                                                                                        connection.commit()

                                                                                        connection.close()

                                                                                        print("land : " + x.get(
                                                                                            'adresse_postale') + " : ok")
                                                                                    except Exception as e:
                                                                                        print("The record already "
                                                                                              "exists : " + str(e))
                                                                                        connection.close()
                                                                            except Exception as e:
                                                                                print('There is a problem : ' + str(e))

                                                                            break
                                                                    except Exception as e:
                                                                        print(
                                                                            'error feature_adresse : ' + str(e))
                                                        except Exception as e:
                                                            print('error libelle urbain : ' + str(e))
                                                    else:
                                                        print('ville : ' + str(commune['nom']) + ' , code insee : '
                                                              + str(commune['code']) + ' , not urban land : '
                                                              + str(properties['prefixe'] + properties['section']
                                                                    + properties['numero']) + " _ typezone : " + str(
                                                            typezone))
                                            else:
                                                print('no features ville : ' + str(commune['nom']) + ' , code insee : '
                                                      + str(commune['code']) + ' , not suitable land : '
                                                      + str(properties['prefixe'] + properties['section']
                                                            + properties['numero']))
                                        except Exception as e:
                                            print('error terrain > 10000 m² : ' + str(e))
                                    else:
                                        print('ville : ' + str(commune['nom'])
                                              + ' , code insee : ' + str(commune['code'])
                                              + ' , not suitable land : '
                                              + str(properties['prefixe']
                                                    + properties['section']
                                                    + properties['numero']) + " < 10000")
                                except Exception as e:
                                    print('error feature : ' + str(e))

                            json_file.close()

                            # delete gz file and json file
                            os.remove(gz_filename[:-3])
                            os.remove(gz_filename)
                        else:
                            print('not suitable commune : ' + str(code_insee_commune))
                    except Exception as e:
                        print("error response commune : " + str(e))
                except Exception as e:
                    print("error commune : " + str(e))
        except Exception as e:
            print('error main : ' + str(e))


if __name__ == '__main__':
    unittest.main()
