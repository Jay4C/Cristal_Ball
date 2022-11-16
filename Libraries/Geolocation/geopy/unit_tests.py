import unittest
from geopy.geocoders import Nominatim


class UnitTestsGeopy(unittest.TestCase):
    # get gps coordinates : ok
    def test_get_gps_coordinates_from_address(self):
        print('test_get_gps_coordinates_from_address')

        # calling the Nominatim tool
        loc = Nominatim(user_agent="GetLoc")

        # entering the location name
        getLoc = loc.geocode("Place de Cornavin 7 1201 Genève Suisse")

        # printing address
        print(getLoc.address)

        # printing latitude and longitude
        print("Latitude = ", getLoc.latitude, "\n")
        print("Longitude = ", getLoc.longitude)

        print(str(getLoc.latitude) + ", " + str(getLoc.longitude))


if __name__ == '__main__':
    unittest.main()
