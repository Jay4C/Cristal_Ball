import unittest
from requests_tor import RequestsTor


# https://opendata.reseaux-energies.fr/
class UnitTestsOpenDataReseauxEnergiesForElectricityForGitHub(unittest.TestCase):
    # ok
    def test_lignes_aeriennes_rte(self):
        print("test_lignes_aeriennes_rte")

        endpoint = "https://odre.opendatasoft.com"

        url = endpoint + "/api/records/1.0/search/?dataset=lignes-aeriennes-rte&q=&rows=11"

        headers = {
            'Content-Type': 'text/json',
        }

        rt = RequestsTor()

        r = rt.get(url, headers=headers)

        data = r.json()

        print(data)

    # ok
    def test_registre_national_installation_production_stockage_electricite_agrege(self):
        print("test_registre_national_installation_production_stockage_electricite_agrege")

        url = "https://odre.opendatasoft.com/api/records/1.0/search/?dataset=registre-national-installation-production-stockage-electricite-agrege&q=&sort=codeinseecommune&facet=commune&facet=epci&facet=departement&facet=region&facet=datemiseenservice&facet=filiere&facet=combustible&facet=combustiblessecondaires&facet=technologie&facet=regime&facet=gestionnaire"

        headers = {
            'Content-Type': 'text/json',
        }

        rt = RequestsTor()

        r = rt.get(url, headers=headers)

        data = r.json()

        print(data)


if __name__ == '__main__':
    unittest.main()
