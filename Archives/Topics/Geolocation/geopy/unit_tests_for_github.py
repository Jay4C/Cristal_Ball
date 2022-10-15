import unittest
from geopy.geocoders import Nominatim
from geopy.distance import geodesic


class UnitTestsTopicsGeolocationGeopyForGitHub(unittest.TestCase):
    # ok
    def test_get_gps_coordinates_location(self):
        print('test_get_gps_coordinates_location')

        # calling the Nominatim tool
        loc = Nominatim(user_agent="GetLoc")

        # entering the location name
        get_loc = loc.geocode("Chemin William-Lescaze 8 1203 Genève")

        # printing address
        print(get_loc.address)

        # printing latitude and longitude
        print("Latitude = ", get_loc.latitude)
        print("Longitude = ", get_loc.longitude)

    # ok
    def test_calculate_distance_between_two_points(self):
        print("test_calculate_distance_between_two_points")

        # calling the Nominatim tool
        loc = Nominatim(user_agent="GetLoc")

        get_loc_gare_de_geneve = loc.geocode("Place de Cornavin 7, 1201 Genève, Suisse")
        gps_coordinates_gare_de_geneve = (get_loc_gare_de_geneve.latitude, get_loc_gare_de_geneve.longitude)

        get_loc = loc.geocode("Avenue Louis-Casaï 80, 1209 Genève, Suisse")
        gps_coordinates = (get_loc.latitude, get_loc.longitude)

        # Print the distance calculated in km
        print(geodesic(gps_coordinates_gare_de_geneve, gps_coordinates).km)


if __name__ == '__main__':
    unittest.main()
