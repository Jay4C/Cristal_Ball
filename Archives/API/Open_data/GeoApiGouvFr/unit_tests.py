import unittest
import requests
import json


# https://geo.api.gouv.fr/decoupage-administratif
class UnitTestsGeoApiGouvFrDecoupageAdministrativeCommunes(unittest.TestCase):
    def test_communes(self):
        print("test_communes")

        url = "https://geo.api.gouv.fr/communes?fields=nom,code,codesPostaux,codeDepartement,codeRegion,population,centre&format=json&geometry=centre"

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)

        print(json.loads(response.text))

    def test_afficher_code_insee_communes(self):
        print("test_afficher_code_insee_communes")

        url = "https://geo.api.gouv.fr/communes?fields=code,codesPostaux&format=json&geometry=centre"

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)

        print(json.loads(response.text))

    def test_recuperer_les_informations_concernant_une_commune(self):
        print("test_recuperer_les_informations_concernant_une_commune")

        url = "https://geo.api.gouv.fr/communes/95127?fields=nom,code,codesPostaux,codeDepartement,codeRegion,population&format=json&geometry=centre"

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)

        commune = ''

        commune += json.loads(response.text)
        print(commune)

        code_insee_departement = commune['codeDepartement']
        print("code_insee_departement : " + str(code_insee_departement))

        code_insee_commune = commune['code']
        print("code_insee_commune : " + str(code_insee_commune))

        population = commune['population']
        print("population : " + str(population))

    def test_rechercher_une_commune_avec_son_code_postal(self):
        print("test_rechercher_une_commune_avec_son_code_postal")

        url = "https://geo.api.gouv.fr/communes?codePostal=93260"

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)

        print(json.loads(response.text))

    def test_afficher_le_code_insee_d_une_commune_avec_son_code_postal_depuis_contact_excel(self):
        print("test_rechercher_une_commune_avec_son_code_postal")

        contact_excel = "Localisation20 r Villegranges, 93260 LES LILAS".split(",")[1].replace(' ', '')[:5]

        print("contact_excel : " + contact_excel)

        url = "https://geo.api.gouv.fr/communes?codePostal=" + contact_excel

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)

        code_insee_commune = json.loads(response.text)[0]['code']

        print("code_insee_commune : " + str(code_insee_commune))

    def test_afficher_le_code_insee_d_une_commune_avec_son_code_postal(self):
        print("test_afficher_le_code_insee_d_une_commune_avec_son_code_postal")

        url = "https://geo.api.gouv.fr/communes?codePostal=95800 "

        payload = {}
        headers = {}

        response = requests.request("GET", url.replace(" ", ""), headers=headers, data=payload)

        code_insee_commune = json.loads(response.text)[0]['code']

        print(code_insee_commune)

    def test_afficher_la_population_d_une_commune_avec_son_code_postal(self):
        print("test_afficher_la_population_d_une_commune_avec_son_code_postal")

        url = "https://geo.api.gouv.fr/communes?codePostal=78810 "

        payload = {}
        headers = {}

        response = requests.request("GET", url.replace(" ", ""), headers=headers, data=payload)

        population = json.loads(response.text)[0]['population']

        print(population)

    def test_afficher_le_code_region_d_une_commune_avec_son_code_postal(self):
        print("test_afficher_la_region_d_une_commune_avec_son_code_postal")

        url = "https://geo.api.gouv.fr/communes?codePostal=78810"

        payload = {}
        headers = {}

        response = requests.request("GET", url.replace(" ", ""), headers=headers, data=payload)

        codeRegion = json.loads(response.text)[0]['codeRegion']

        print(codeRegion)

    def test_rechercher_une_commune_avec_son_code_postal_et_son_nom(self):
        print("test_rechercher_une_commune_avec_son_code_postal")

        nom = "Cergy"

        url = "https://geo.api.gouv.fr/communes?codePostal=95800"

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)

        informations_pour_une_commune_avec_son_code_postal = response.json()

        for commune in informations_pour_une_commune_avec_son_code_postal:
            if commune['nom'] == nom:
                print(commune)


class UnitTestsGeoApiGouvFrDecoupageAdministrativeDepartements(unittest.TestCase):
    def test_renvoi_les_communes_pour_un_departement(self):
        print("test_renvoi_les_communes_pour_un_departement")

        url = "https://geo.api.gouv.fr/departements/77/communes?fields=nom,code,codesPostaux,codeDepartement,codeRegion,population&format=json&geometry=centre"

        payload = {}

        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)

        print(response.json())

        # print(json.loads(response.text))

    def test_renvoi_les_communes_pour_une_region(self):
        print("test_renvoi_les_communes_pour_une_region")

        url = "https://geo.api.gouv.fr/regions/11/communes?fields=code,nom,codesPostaux,codeDepartement,codeRegion,population&format=json"

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)

        print(json.loads(response.text))

    def test_rechercher_des_departements(self):
        print("test_rechercher_des_departements")

        url = "https://geo.api.gouv.fr/departements?fields=code,nom,codeRegion,region&format=json"

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)

        print(json.loads(response.text))

    def test_recuperer_les_informations_concernant_un_departement(self):
        print("test_recuperer_les_informations_concernant_un_departement")

        url = "https://geo.api.gouv.fr/departements/75?fields=code,nom,codeRegion,region&format=json"

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)

        print(json.loads(response.text))

    def test_renvoi_les_departements_dans_une_region(self):
        print("test_renvoi_les_departements_dans_une_region")

        url = "https://geo.api.gouv.fr/regions/11/departements?fields=code,nom,codeRegion,region&format=json"

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)

        print(json.loads(response.text))

    def test_rechercher_des_regions(self):
        print("test_rechercher_des_regions")

        url = "https://geo.api.gouv.fr/regions?fields=code,nom,codeDepartement&format=json"

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)

        print(json.loads(response.text))

    def test_afficher_les_regions_pour_annuaire_service_public(self):
        print("test_rechercher_des_regions")

        url = "https://geo.api.gouv.fr/regions?fields=code,nom,codeDepartement&format=json"

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)

        regions = json.loads(response.text)

        for region in regions:
            nom_region = region['nom'].lower()\
                .replace('î', 'i')\
                .replace('é', 'e')\
                .replace('è', 'e')\
                .replace('à', 'a')\
                .replace('ô', 'o')\
                .replace("'", '-')\
                .replace(' ', '-')
            print(nom_region)

    def test_afficher_les_departements_de_chaque_region_pour_annuaire_service_public(self):
        print("test_afficher_les_departements_de_chaque_region_pour_annuaire_service_public")

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
                nom_departement = departement['nom'].lower()\
                    .replace('î', 'i')\
                    .replace('é', 'e')\
                    .replace('è', 'e')\
                    .replace('à', 'a')\
                    .replace('ô', 'o')\
                    .replace("'", '-')\
                    .replace(' ', '-')
                print("region : " + nom_region + " - departement : " + nom_departement)

    def test_afficher_les_code_insee_communes_de_chaque_departement_pour_annuaire_service_public(self):
        print("test_afficher_les_code_insee_communes_de_chaque_departement_pour_annuaire_service_public")

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

                    print("region : " + nom_region
                          + " - departement : " + nom_departement
                          + " - code insee commune : " + code_insee_commune)

    def test_recuperer_les_informations_concernant_une_region(self):
        print("test_recuperer_les_informations_concernant_une_region")

        url = "https://geo.api.gouv.fr/regions/11?fields=code,nom&format=json"

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)

        print(json.loads(response.text))

    def test_recuperer_le_nom_concernant_une_region(self):
        print("test_recuperer_les_informations_concernant_une_region")

        url = "https://geo.api.gouv.fr/regions/11?fields=code,nom&format=json"

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)

        nomRegion = json.loads(response.text)["nom"]

        print(nomRegion)

    def test_communes_avec_moins_de_1000_habitants(self):
        print("test_communes_avec_moins_de_1000_habitants")

        url = "https://geo.api.gouv.fr/communes?fields=nom,code,codesPostaux,codeDepartement,codeRegion,population&format=json&geometry=centre"

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)

        communes = response.json()

        for commune in communes:
            try:
                if commune['population'] < 1000:
                    print(commune)
            except Exception as e:
                print("error : " + str(e))

    def test_communes_avec_plus_de_20000_habitants(self):
        print("test_communes_avec_plus_de_20000_habitants")

        url = "https://geo.api.gouv.fr/communes?fields=nom,code,codesPostaux,codeDepartement,codeRegion,population&format=json&geometry=centre"

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)

        communes = response.json()

        for commune in communes:
            try:
                if commune['population'] > 20000:
                    print(commune['nom'].lower()
                          .replace(' ', '-')
                          .replace('ê', 'e')
                          .replace('é', '')
                          .replace('è', '')
                          .replace('à', 'a')
                          .replace('â', 'a')
                          .replace('ô', 'o')
                          )
            except Exception as e:
                print("error : " + str(e))

    def test_afficher_code_insee_communes_avec_moins_de_1000_habitants(self):
        print("test_afficher_code_insee_communes_avec_moins_de_1000_habitants")

        url = "https://geo.api.gouv.fr/communes?fields=nom,code,codesPostaux,codeDepartement,codeRegion,population&format=json&geometry=centre"

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)

        communes = response.json()

        for commune in communes:
            try:
                if commune['population'] < 1000:
                    print(" code insee : " + commune['code'])
            except Exception as e:
                print("error : " + str(e))

    def test_afficher_code_departement_avec_des_communes_avec_moins_de_1000_habitants(self):
        print("test_afficher_code_insee_communes_avec_moins_de_1000_habitants")

        url = "https://geo.api.gouv.fr/communes?fields=nom,code,codesPostaux,codeDepartement,codeRegion,population&format=json&geometry=centre"

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)

        communes = response.json()

        for commune in communes:
            try:
                if commune['population'] < 1000:
                    print(" code insee departement : " + commune['codeDepartement'])
            except Exception as e:
                print("error : " + str(e))


if __name__ == '__main__':
    unittest.main()
