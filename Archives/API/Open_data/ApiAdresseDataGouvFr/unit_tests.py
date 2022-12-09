import unittest
import requests
import json


# https://api-adresse.data.gouv.fr
class UnitTestsApiAdresseDataGouvFrCommunes(unittest.TestCase):
    # ok
    def test_reverse(self):
        print("test_reverse")

        lat = "43.6022532"

        lon = "3.878677"

        url = "https://api-adresse.data.gouv.fr/reverse/?lon=" + lon + "&lat=" + lat

        payload = {}

        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)

        print(json.loads(response.text))

    #
    def test_reverse_for_address(self):
        print("test_reverse_for_address")

        lat = "43.6022532"

        lon = "3.878677"

        url = "https://api-adresse.data.gouv.fr/reverse/?lon=" + lon + "&lat=" + lat

        response = requests.request("GET", url)

        address = json.loads(response.text)['features'][0]['properties']['label']

        print(address)

    # ok
    def test_reverse_name_region(self):
        print("test_reverse_name_region")

        lat = "43.6022532"

        lon = "3.878677"

        url_building = "https://api-adresse.data.gouv.fr/reverse/?lon=" + lon + "&lat=" + lat

        code_postale = json.loads(requests.request("GET", url_building).text)['features'][0]['properties']['postcode']

        url_code_postale = "https://geo.api.gouv.fr/communes?codePostal=" + str(code_postale)

        code_region = json.loads(requests.request("GET", url_code_postale.replace(" ", "")).text)[0]['codeRegion']

        url_region = "https://geo.api.gouv.fr/regions/" + str(code_region) + "?fields=code,nom&format=json"

        nom_region = json.loads(requests.request("GET", url_region).text)["nom"]

        print(nom_region)


if __name__ == '__main__':
    unittest.main()
