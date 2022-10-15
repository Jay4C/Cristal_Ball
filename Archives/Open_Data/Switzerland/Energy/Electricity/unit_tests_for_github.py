import unittest
import csv
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import xlsxwriter


class UnitTestsOpenDataSwitzerlandEnergyElectricityForGitHub(unittest.TestCase):
    # ok
    def test_read_csv(self):
        print('test_read_csv')

        # opening the CSV file
        with open('ElectricityProductionPlant.csv', mode='r') as file:
            # reading the CSV file
            csvFile = csv.reader(file)

            # displaying the contents of the CSV file
            for lines in csvFile:
                print(lines)

    # ok
    def test_print_only_canton_geneve(self):
        print('test_read_csv')

        # opening the CSV file

        with open('ElectricityProductionPlant.csv', mode='r', encoding='utf-8') as file:
            # reading the CSV file
            csvFile = csv.reader(file)

            try:
                # displaying the contents of the CSV file
                for lines in csvFile:
                    canton = lines[4]
                    if canton == 'GE':
                        print(lines)
            except Exception as e:
                print("error : " + str(e))

    # ok
    def test_print_only_municipality_geneve(self):
        print('test_print_only_municipality_geneve')

        # opening the CSV file
        with open('ElectricityProductionPlant.csv', mode='r', encoding='utf-8') as file:
            # reading the CSV file
            csvFile = csv.reader(file)

            try:
                # displaying the contents of the CSV file
                for lines in csvFile:
                    municipality = lines[3]
                    if municipality == 'Genève':
                        print(lines)
            except Exception as e:
                print("error : " + str(e))

    # ok
    def test_print_only_municipality_geneve_with_solar_panel_sorted_by_lowest_distance_from_gare_de_geneve(self):
        print('test_print_only_municipality_geneve_sorted_by_lowest_distance_from_gare_de_geneve')

        locations = []

        # opening the CSV file
        with open('ElectricityProductionPlant.csv', mode='r', encoding='utf-8') as file:
            # reading the CSV file
            csvFile = csv.reader(file)

            # displaying the contents of the CSV file
            for lines in csvFile:
                try:
                    municipality = lines[3]
                    solar_panel = lines[9]
                    address = str(lines[1]) + " " + str(lines[2]) + " " + str(lines[3])

                    if municipality == 'Genève' and solar_panel == 'subcat_2':
                        loc = Nominatim(user_agent="GetLoc")

                        get_loc_gare_de_geneve = loc.geocode("Place de Cornavin 7, 1201 Genève, Suisse")
                        gps_coordinates_gare_de_geneve = (
                            get_loc_gare_de_geneve.latitude,
                            get_loc_gare_de_geneve.longitude
                        )

                        get_loc = loc.geocode(address + ", Suisse")
                        gps_coordinates = (get_loc.latitude, get_loc.longitude)

                        # Print the distance calculated in km
                        distance_from_gare_de_geneve = geodesic(gps_coordinates_gare_de_geneve, gps_coordinates).km

                        x = {
                            "address": address,
                            "distance_from_gare_de_geneve": distance_from_gare_de_geneve
                        }

                        print(x)

                        locations.append(x)
                except Exception as e:
                    print("error : " + str(e))

            locations_sorted = sorted(locations, key=lambda item: item.get("distance_from_gare_de_geneve"))

            for loc in locations_sorted:
                print(loc)

    # ok
    def test_print_only_municipality_geneve_with_solar_panel_sorted_by_lowest_distance_from_gare_de_geneve_into_excel(self):
        print('test_print_only_municipality_geneve_sorted_by_lowest_distance_from_gare_de_geneve')

        locations = []

        # Create a workbook and add a worksheet.
        workbook = xlsxwriter.Workbook('data.xlsx')
        worksheet = workbook.add_worksheet('data')

        # Start from the first cell. Rows and columns are zero indexed.
        row = 0
        worksheet.write(row, 0, 'Address')
        worksheet.write(row, 1, 'Distance_from_gare_de_geneve')
        row += 1

        # opening the CSV file
        with open('ElectricityProductionPlant.csv', mode='r', encoding='utf-8') as file:
            # reading the CSV file
            csvFile = csv.reader(file)

            # displaying the contents of the CSV file
            for lines in csvFile:
                try:
                    municipality = lines[3]
                    solar_panel = lines[9]
                    address = str(lines[1]) + " " + str(lines[2]) + " " + str(lines[3])

                    if municipality == 'Genève' and solar_panel == 'subcat_2':
                        loc = Nominatim(user_agent="GetLoc")

                        get_loc_gare_de_geneve = loc.geocode("Place de Cornavin 7, 1201 Genève, Suisse")
                        gps_coordinates_gare_de_geneve = (
                            get_loc_gare_de_geneve.latitude,
                            get_loc_gare_de_geneve.longitude
                        )

                        get_loc = loc.geocode(address + ", Suisse")
                        gps_coordinates = (get_loc.latitude, get_loc.longitude)

                        # Print the distance calculated in km
                        distance_from_gare_de_geneve = geodesic(gps_coordinates_gare_de_geneve, gps_coordinates).km

                        x = {
                            "address": address,
                            "distance_from_gare_de_geneve": distance_from_gare_de_geneve
                        }

                        locations.append(x)

                        print(x)
                except Exception as e:
                    print("error : " + str(e))

        locations_sorted = sorted(locations, key=lambda item: item.get("distance_from_gare_de_geneve"))

        for loc in locations_sorted:
            print(loc)
            worksheet.write(row, 0, loc.get('address'))
            worksheet.write(row, 1, loc.get('distance_from_gare_de_geneve'))
            row += 1

        workbook.close()


if __name__ == '__main__':
    unittest.main()
