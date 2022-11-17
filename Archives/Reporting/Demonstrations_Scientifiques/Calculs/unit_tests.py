import numpy as np
import matplotlib.pyplot as plt
import gzip
import json
import os
import unittest
import math
import requests


class UnitTestsCalculsChasCampbellGravitationalEngine(unittest.TestCase):
    # ok
    def test_calculate_the_length_of_the_part_steel_box_tube_for_support_elevator_flywheel(self):
        print('test_calculate_the_length_of_the_part_steel_box_tube_for_support_elevator_flywheel')

        L_flywheel = 1000
        h_tube = 50
        number_of_weights = 1
        h_ecrou = 10
        s_rondelle_10m = 2

        L_elevator = round(math.sqrt(math.pow(L_flywheel/2, 2)
                                     + math.pow(h_tube/2 + number_of_weights * (h_tube/2)
                                                + h_ecrou + s_rondelle_10m + h_tube, 2)) + 50 * 3) + 1

        print('L_elevator : ' + str(L_elevator))

    # ok
    def test_calculate_the_length_of_the_part_steel_box_tube_for_support_link_flywheel(self):
        print('test_calculate_the_length_of_the_part_steel_box_tube_for_support_link_flywheel')

        L_flywheel = 1000
        s_rondelle_20m = 3
        h_ecrou = 20
        L_moyeu_amovible_volant_inertie = 22.2
        h1_palier = 38

        L_link = round((L_flywheel/2 + 10 - 38 - 10 - h_ecrou - s_rondelle_20m - L_moyeu_amovible_volant_inertie -
                        s_rondelle_20m - h_ecrou) * 2 + h1_palier) + 1

        print('L_link : ' + str(L_link))


class UnitTestsCalculsMotionlessElectromagneticGenerator(unittest.TestCase):
    # ok
    def test_calculate_the_current_of_the_coil_1(self):
        print('test_calculate_the_current_of_the_coil_1')

        I_coil_2 = 4.35
        U_coil_2 = 230
        P_coil_2 = 1000
        l_magnet = 3 * math.pow(10, -3)
        d_magnet = 8 * math.pow(10, -3)
        N_coil_1 = 20
        N_coil_2 = 200
        l_coil_1 = 20 * math.pow(10, -3)
        l_coil_2 = 50 * math.pow(10, -3)
        mu_coil_1 = 5000
        mu_coil_2 = mu_coil_1
        mu_magnet = mu_coil_2

        I_coil_1 = round((l_coil_1 * mu_coil_2 * math.pow(N_coil_2, 2) * I_coil_2)/((1 + mu_magnet) * mu_coil_1 *
                                                                                    N_coil_1 * math.pi * l_coil_2), 2)

        print('I_coil_1 : ' + str(I_coil_1))

    # ok
    def test_calculate_the_diameter_of_the_coil_2(self):
        print('test_calculate_the_diameter_of_the_coil_2')

        U_coil_2 = 230
        P_coil_2 = 500
        I_coil_2 = P_coil_2/U_coil_2
        l_magnet = 3 * math.pow(10, -3)
        d_magnet = 8 * math.pow(10, -3)
        N_coil_1 = 10
        N_coil_2 = 200
        l_coil_1 = 20 * math.pow(10, -3)
        l_coil_2 = 100 * math.pow(10, -3)
        mu_coil_1 = 5000
        mu_coil_2 = mu_coil_1
        mu_magnet = mu_coil_2

        h_tube = 8.1 * math.pow(10, -3)

        radius_box = math.sqrt(math.pow(h_tube / 2, 2) + math.pow(h_tube / 2, 2)) + 1

        d_coil_1 = radius_box * 2

        I_coil_1 = round((l_coil_1 * mu_coil_2 * math.pow(N_coil_2, 2) * I_coil_2)/((1 + mu_magnet) * mu_coil_1 *
                                                                                    N_coil_1 * math.pi * l_coil_2), 2)

        d_coil_2 = math.sqrt(
            ((1 + mu_magnet) * mu_coil_1 * math.pow(N_coil_1, 2) * math.pow(d_coil_1, 2)
             * I_coil_1 * l_coil_2)/(I_coil_2 * l_coil_1 * mu_coil_2 * math.pow(N_coil_2, 2))
        )

        print('d_coil_2 : ' + str(d_coil_2))


class UnitTestsCalculsForTwoVariablesFunction(unittest.TestCase):
    # ok
    def test_f1(self):
        print("test_f1")

        filename = "function_with_two_variables_of_f1"

        def function_with_two_variables(x, y):
            return 2 * x ** 2 - x * y ** 2 + 2 * y ** 2

        x = np.linspace(-400, 400, 100)
        y = np.linspace(-400, 400, 100)

        X, Y = np.meshgrid(x, y)
        Z = function_with_two_variables(X, Y)

        fig = plt.figure(figsize=(10, 7))

        ax = plt.axes(projection='3d')
        ax.plot_surface(X, Y, Z, rstride=5, cstride=5, cmap='cool')
        ax.set_title("Surface Bonus", fontsize=13)
        ax.set_xlabel('x', fontsize=11)
        ax.set_ylabel('y', fontsize=11)
        ax.set_zlabel('Z', fontsize=11)
        plt.show()
        fig.savefig("F_Two_Variables\\" + filename)

    # ok
    def test_f2(self):
        print("test_f2")

        filename = "function_with_two_variables_of_f2"

        def function_with_two_variables(x, y):
            return x**2 + y**2

        x = np.linspace(-400, 400, 100)
        y = np.linspace(-400, 400, 100)

        X, Y = np.meshgrid(x, y)
        Z = function_with_two_variables(X, Y)

        fig = plt.figure(figsize=(10, 7))

        ax = plt.axes(projection='3d')
        ax.plot_surface(X, Y, Z, rstride=5, cstride=5, cmap='cool')
        ax.set_title("Surface Bonus", fontsize=13)
        ax.set_xlabel('x', fontsize=11)
        ax.set_ylabel('y', fontsize=11)
        ax.set_zlabel('Z', fontsize=11)
        plt.show()
        fig.savefig("F_Two_Variables\\" + filename)

    # ok
    def test_f3(self):
        print("test_f3")

        filename = "function_with_two_variables_of_f3"

        def function_with_two_variables(x, y):
            return y**2 - x**2

        x = np.linspace(-400, 400, 100)
        y = np.linspace(-400, 400, 100)

        X, Y = np.meshgrid(x, y)
        Z = function_with_two_variables(X, Y)

        fig = plt.figure(figsize=(10, 7))

        ax = plt.axes(projection='3d')
        ax.plot_surface(X, Y, Z, rstride=5, cstride=5, cmap='cool')
        ax.set_title("Surface Bonus", fontsize=13)
        ax.set_xlabel('x', fontsize=11)
        ax.set_ylabel('y', fontsize=11)
        ax.set_zlabel('Z', fontsize=11)
        plt.show()
        fig.savefig("F_Two_Variables\\" + filename)


class UnitTestsGeometry(unittest.TestCase):
    # ok
    def test_calculate_the_distance_between_two_gps_points_with_the_law_of_sinus(self):
        print("test_calculate_the_distance_between_two_gps_points_with_the_law_of_sinus")

        # phi : latitude et lambda : longitude

        coordinates_a = [55.739399, 37.592572]

        coordinates_b = [55.735632, 37.678367]

        r = 6372.795477598

        distance_between_a_and_b = r * math.acos(math.sin((math.pi * coordinates_a[0])/180)*math.sin((math.pi * coordinates_b[0])/180)
                                                 + math.cos((math.pi * coordinates_a[0])/180)*math.cos((math.pi * coordinates_b[0])/180)*
                                                 math.cos((math.pi * coordinates_b[1])/180 - (math.pi * coordinates_a[1])/180))

        print("distance_between_a_and_b : " + str(distance_between_a_and_b) + " kms")

    # ok
    def test_calculate_the_distance_between_two_gps_points_with_pythagore(self):
        print("test_calculate_the_distance_between_two_gps_points_with_pythagore")

        # phi : latitude et lambda : longitude

        coordinates_a = [55.739399, 37.592572]

        coordinates_b = [55.735632, 37.678367]

        k = 1.852 * 60

        x = (coordinates_b[1] - coordinates_a[1])*math.cos((math.pi/180)*((coordinates_a[0] + coordinates_b[0])/2))

        y = (coordinates_b[0] - coordinates_a[0])

        z = math.sqrt(math.pow(x, 2) + math.pow(y, 2))

        d = k * z

        print("distance_between_a_and_b : " + str(d) + " kms")

    # ok
    def test_calculate_the_distance_between_two_gps_points_with_haversine(self):
        print("test_calculate_the_distance_between_two_gps_points_with_haversine")

        # phi : latitude et lambda : longitude

        coordinates_a = [55.739399, 37.592572]

        coordinates_b = [55.735632, 37.678367]

        r = 6372.795477598

        a = math.pow(math.sin((math.pi/180)*((coordinates_b[0] - coordinates_a[0])/2)), 2) + \
            math.cos((math.pi/180)*coordinates_a[0])*math.cos((math.pi/180)*coordinates_b[0])\
            * math.pow(math.sin((math.pi/180)*((coordinates_b[1] - coordinates_a[1])/2)), 2)

        c = 2 * math.atan(math.sqrt(a/(1-a)))

        d = r * c

        print("distance_between_a_and_b : " + str(d) + " kms")

    # ok
    def test_calculate_the_distance_between_one_point_from_gare_geneva_with_haversine(self):
        print("test_calculate_the_distance_between_two_gps_points_with_haversine")

        # phi : latitude et lambda : longitude

        # Gare de Genève
        coordinates_a = [46.2107481, 6.1432885]

        # Coordonnées de la destination
        coordinates_b = [46.2054285, 6.1211963]

        r = 6372.795477598

        a = math.pow(math.sin((math.pi/180)*((coordinates_b[0] - coordinates_a[0])/2)), 2) + \
            math.cos((math.pi/180)*coordinates_a[0])*math.cos((math.pi/180)*coordinates_b[0])\
            * math.pow(math.sin((math.pi/180)*((coordinates_b[1] - coordinates_a[1])/2)), 2)

        c = 2 * math.atan(math.sqrt(a/(1-a)))

        d = r * c

        print("distance_between_a_and_b : " + str(d) + " kms")

    # ok
    def test_convert_spherique_coordinates_to_cartesiennes_coordinates_for_one_point(self):
        print("test_convert_spherique_coordinates_to_cartesiennes_coordinates_for_one_point")

        # latitude and longitude

        spheriques_coordinates = [55.739399, 37.592572]

        r = 6372.795477598

        x = r * math.cos((math.pi/180)*spheriques_coordinates[0])*math.cos((math.pi/180)*spheriques_coordinates[1])

        y = r * math.cos((math.pi/180)*spheriques_coordinates[0]) * math.sin((math.pi/180)*spheriques_coordinates[1])

        z = r * math.sin((math.pi/180)*spheriques_coordinates[0])

        cartesiennes_coordinates = [x, y, z]

        print("spheriques_coordinates of " + str(spheriques_coordinates) + " in cartesiennes_coordinates is : " + str(cartesiennes_coordinates))

    # ok
    def test_convert_spherique_coordinates_to_cartesiennes_coordinates_for_one_irregular_polygon(self):
        print("test_convert_spherique_coordinates_to_cartesiennes_coordinates_for_one_irregular_polygon")

        # open data (coordinates [longitude, latitude])

        spheriques_coordinates_for_one_irregular_polygon = [[[6.1055132138, 49.2613410884], [6.1054032167, 49.2614320883], [6.1050093722, 49.2617634105], [6.1037109583, 49.2631004489], [6.102905707, 49.2641809734], [6.1024951006, 49.2651721682], [6.1019456221, 49.2663234729], [6.1016670436, 49.2668353465], [6.1011728852, 49.2674661197], [6.1010377333, 49.2675964467], [6.100773898, 49.2677129886], [6.1002005343, 49.2678033], [6.0955101152, 49.2684743688], [6.0909523008, 49.2690887738], [6.0883123008, 49.2696116271], [6.0866025671, 49.270080929], [6.0844158257, 49.2706208823], [6.0825968134, 49.2710110519], [6.0818331769, 49.2711394238], [6.0810940362, 49.2711484117], [6.0808535582, 49.2710582926], [6.0797739922, 49.270730504], [6.0782792187, 49.2708406352], [6.0756589659, 49.2711674786], [6.0730400527, 49.2714942301], [6.0725373255, 49.2715484214], [6.0691596423, 49.2719016113], [6.0685734331, 49.2719624082], [6.067772706, 49.2720457518], [6.0659841291, 49.272233373], [6.065620721, 49.2722722982], [6.0656348621, 49.2722557453], [6.0662072739, 49.2718003725], [6.0677212415, 49.2707164943], [6.0705373709, 49.2683885308], [6.0740082405, 49.2643155789], [6.0756918354, 49.2614234579], [6.0797578467, 49.261122658], [6.0807591618, 49.2603953496], [6.0814359986, 49.2597132099], [6.0828315021, 49.2563560019], [6.0829515206, 49.2561100251], [6.08296013, 49.256000946], [6.0829605587, 49.2558929758], [6.0834642576, 49.2556965649], [6.0848817525, 49.2556117248], [6.0857049414, 49.2557939841], [6.0908407193, 49.2555085976], [6.0931601169, 49.2556119577], [6.0955867043, 49.2559212439], [6.1000642601, 49.2571044246], [6.1029317601, 49.2589397599], [6.1050272562, 49.2612834286], [6.1055132138, 49.2613410884]]]

        number_of_points_of_the_polygon_in_spheric = len(spheriques_coordinates_for_one_irregular_polygon[0])

        print("number_of_points_of_the_polygon_in_spheric : " + str(number_of_points_of_the_polygon_in_spheric))

        cartesiennes_coordinates_for_all_points = []

        cartesiennes_coordinates_for_one_irregular_polygon = [cartesiennes_coordinates_for_all_points]

        for point in spheriques_coordinates_for_one_irregular_polygon[0]:
            spheriques_coordinates = [point[1], point[0]]

            r = 6372.795477598

            x = r * math.cos((math.pi / 180) * spheriques_coordinates[0]) * math.cos(
                (math.pi / 180) * spheriques_coordinates[1])

            y = r * math.cos((math.pi / 180) * spheriques_coordinates[0]) * math.sin(
                (math.pi / 180) * spheriques_coordinates[1])

            z = r * math.sin((math.pi / 180) * spheriques_coordinates[0])

            cartesiennes_coordinates_of_point = [x, y, z]

            cartesiennes_coordinates_for_all_points.append(cartesiennes_coordinates_of_point)

        number_of_points_of_the_polygon_in_cartesiennes = len(cartesiennes_coordinates_for_one_irregular_polygon[0])

        print("number_of_points_of_the_polygon_in_cartesiennes : " + str(number_of_points_of_the_polygon_in_cartesiennes))

        print("cartesiennes_coordinates_for_one_irregular_polygon : " + str(cartesiennes_coordinates_for_one_irregular_polygon))

    # ok
    def test_calculate_the_area_for_one_irregular_polygon_with_cartesiennes_coordinates(self):
        print("test_calculate_the_area_for_one_irregular_polygon_with_cartesiennes_coordinates")

        # open data (coordinates [longitude, latitude])

        spheriques_coordinates_for_one_irregular_polygon = [[[6.1055132138, 49.2613410884], [6.1054032167, 49.2614320883], [6.1050093722, 49.2617634105], [6.1037109583, 49.2631004489], [6.102905707, 49.2641809734], [6.1024951006, 49.2651721682], [6.1019456221, 49.2663234729], [6.1016670436, 49.2668353465], [6.1011728852, 49.2674661197], [6.1010377333, 49.2675964467], [6.100773898, 49.2677129886], [6.1002005343, 49.2678033], [6.0955101152, 49.2684743688], [6.0909523008, 49.2690887738], [6.0883123008, 49.2696116271], [6.0866025671, 49.270080929], [6.0844158257, 49.2706208823], [6.0825968134, 49.2710110519], [6.0818331769, 49.2711394238], [6.0810940362, 49.2711484117], [6.0808535582, 49.2710582926], [6.0797739922, 49.270730504], [6.0782792187, 49.2708406352], [6.0756589659, 49.2711674786], [6.0730400527, 49.2714942301], [6.0725373255, 49.2715484214], [6.0691596423, 49.2719016113], [6.0685734331, 49.2719624082], [6.067772706, 49.2720457518], [6.0659841291, 49.272233373], [6.065620721, 49.2722722982], [6.0656348621, 49.2722557453], [6.0662072739, 49.2718003725], [6.0677212415, 49.2707164943], [6.0705373709, 49.2683885308], [6.0740082405, 49.2643155789], [6.0756918354, 49.2614234579], [6.0797578467, 49.261122658], [6.0807591618, 49.2603953496], [6.0814359986, 49.2597132099], [6.0828315021, 49.2563560019], [6.0829515206, 49.2561100251], [6.08296013, 49.256000946], [6.0829605587, 49.2558929758], [6.0834642576, 49.2556965649], [6.0848817525, 49.2556117248], [6.0857049414, 49.2557939841], [6.0908407193, 49.2555085976], [6.0931601169, 49.2556119577], [6.0955867043, 49.2559212439], [6.1000642601, 49.2571044246], [6.1029317601, 49.2589397599], [6.1050272562, 49.2612834286], [6.1055132138, 49.2613410884]]]

        cartesiennes_coordinates_for_all_points = []

        cartesiennes_coordinates_for_one_irregular_polygon = [cartesiennes_coordinates_for_all_points]

        for point in spheriques_coordinates_for_one_irregular_polygon[0]:
            spheriques_coordinates = [point[1], point[0]]

            r = 6372.795477598

            x = r * math.cos((math.pi / 180) * spheriques_coordinates[0]) * math.cos(
                (math.pi / 180) * spheriques_coordinates[1])

            y = r * math.cos((math.pi / 180) * spheriques_coordinates[0]) * math.sin(
                (math.pi / 180) * spheriques_coordinates[1])

            z = r * math.sin((math.pi / 180) * spheriques_coordinates[0])

            cartesiennes_coordinates_of_point = [x, y, z]

            cartesiennes_coordinates_for_all_points.append(cartesiennes_coordinates_of_point)

        area = 0

        for i in range(0, len(cartesiennes_coordinates_for_one_irregular_polygon[0]) - 1):
            area += (cartesiennes_coordinates_for_one_irregular_polygon[0][i][0] * cartesiennes_coordinates_for_one_irregular_polygon[0][i+1][1]
                     - cartesiennes_coordinates_for_one_irregular_polygon[0][i+1][0] * cartesiennes_coordinates_for_one_irregular_polygon[0][i][1])

        area = area/2

        print("area_for_one_irregular_polygon : " + str(round(area, 3)) + " km^2")

    # ok
    def test_calculate_the_gravity_center_for_one_irregular_polygon_with_cartesiennes_coordinates(self):
        print("test_calculate_the_gravity_center_for_one_irregular_polygon_with_cartesiennes_coordinates")

        # open data (coordinates [longitude, latitude])

        spheriques_coordinates_for_one_irregular_polygon = [[[6.1055132138, 49.2613410884], [6.1054032167, 49.2614320883], [6.1050093722, 49.2617634105], [6.1037109583, 49.2631004489], [6.102905707, 49.2641809734], [6.1024951006, 49.2651721682], [6.1019456221, 49.2663234729], [6.1016670436, 49.2668353465], [6.1011728852, 49.2674661197], [6.1010377333, 49.2675964467], [6.100773898, 49.2677129886], [6.1002005343, 49.2678033], [6.0955101152, 49.2684743688], [6.0909523008, 49.2690887738], [6.0883123008, 49.2696116271], [6.0866025671, 49.270080929], [6.0844158257, 49.2706208823], [6.0825968134, 49.2710110519], [6.0818331769, 49.2711394238], [6.0810940362, 49.2711484117], [6.0808535582, 49.2710582926], [6.0797739922, 49.270730504], [6.0782792187, 49.2708406352], [6.0756589659, 49.2711674786], [6.0730400527, 49.2714942301], [6.0725373255, 49.2715484214], [6.0691596423, 49.2719016113], [6.0685734331, 49.2719624082], [6.067772706, 49.2720457518], [6.0659841291, 49.272233373], [6.065620721, 49.2722722982], [6.0656348621, 49.2722557453], [6.0662072739, 49.2718003725], [6.0677212415, 49.2707164943], [6.0705373709, 49.2683885308], [6.0740082405, 49.2643155789], [6.0756918354, 49.2614234579], [6.0797578467, 49.261122658], [6.0807591618, 49.2603953496], [6.0814359986, 49.2597132099], [6.0828315021, 49.2563560019], [6.0829515206, 49.2561100251], [6.08296013, 49.256000946], [6.0829605587, 49.2558929758], [6.0834642576, 49.2556965649], [6.0848817525, 49.2556117248], [6.0857049414, 49.2557939841], [6.0908407193, 49.2555085976], [6.0931601169, 49.2556119577], [6.0955867043, 49.2559212439], [6.1000642601, 49.2571044246], [6.1029317601, 49.2589397599], [6.1050272562, 49.2612834286], [6.1055132138, 49.2613410884]]]

        cartesiennes_coordinates_for_all_points = []

        cartesiennes_coordinates_for_one_irregular_polygon = [cartesiennes_coordinates_for_all_points]

        for point in spheriques_coordinates_for_one_irregular_polygon[0]:
            spheriques_coordinates = [point[1], point[0]]

            r = 6372.795477598

            x = r * math.cos((math.pi / 180) * spheriques_coordinates[0]) * math.cos(
                (math.pi / 180) * spheriques_coordinates[1])

            y = r * math.cos((math.pi / 180) * spheriques_coordinates[0]) * math.sin(
                (math.pi / 180) * spheriques_coordinates[1])

            z = r * math.sin((math.pi / 180) * spheriques_coordinates[0])

            cartesiennes_coordinates_of_point = [x, y, z]

            cartesiennes_coordinates_for_all_points.append(cartesiennes_coordinates_of_point)

        gravity_x = 0

        gravity_y = 0

        area = 0

        for i in range(0, len(cartesiennes_coordinates_for_one_irregular_polygon[0]) - 1):
            area += (cartesiennes_coordinates_for_one_irregular_polygon[0][i][0] * cartesiennes_coordinates_for_one_irregular_polygon[0][i+1][1]
                     - cartesiennes_coordinates_for_one_irregular_polygon[0][i+1][0] * cartesiennes_coordinates_for_one_irregular_polygon[0][i][1])

        area = area/2

        for i in range(0, len(cartesiennes_coordinates_for_one_irregular_polygon[0]) - 1):
            gravity_x += (cartesiennes_coordinates_for_one_irregular_polygon[0][i][0] + cartesiennes_coordinates_for_one_irregular_polygon[0][i+1][0])\
                         * (cartesiennes_coordinates_for_one_irregular_polygon[0][i][0]*cartesiennes_coordinates_for_one_irregular_polygon[0][i+1][1]
                            - cartesiennes_coordinates_for_one_irregular_polygon[0][i+1][0]*cartesiennes_coordinates_for_one_irregular_polygon[0][i][1])

        for i in range(0, len(cartesiennes_coordinates_for_one_irregular_polygon[0]) - 1):
            gravity_y += (cartesiennes_coordinates_for_one_irregular_polygon[0][i][1] + cartesiennes_coordinates_for_one_irregular_polygon[0][i+1][1])\
                         * (cartesiennes_coordinates_for_one_irregular_polygon[0][i][0]*cartesiennes_coordinates_for_one_irregular_polygon[0][i+1][1]
                            - cartesiennes_coordinates_for_one_irregular_polygon[0][i+1][0]*cartesiennes_coordinates_for_one_irregular_polygon[0][i][1])

        gravity_x = gravity_x/(6*area)

        gravity_y = gravity_y/(6*area)

        print("(gravity_x, gravity_y) : (" + str(gravity_x) + ", " + str(gravity_y) + ")")

    # ok
    def test_calculate_the_distance_between_two_gravities_with_cartesiennes_coordinates(self):
        print('test_calculate_the_distance_between_two_gravities_with_cartesiennes_coordinates')

        def calculate_gravity_center(coordinates_parcelle):
            # open data (coordinates [longitude, latitude])

            spheriques_coordinates_for_one_irregular_polygon = coordinates_parcelle

            cartesiennes_coordinates_for_all_points = []

            cartesiennes_coordinates_for_one_irregular_polygon = [cartesiennes_coordinates_for_all_points]

            for point in spheriques_coordinates_for_one_irregular_polygon[0]:
                spheriques_coordinates = [point[1], point[0]]

                r = 6372.795477598

                x = r * math.cos((math.pi / 180) * spheriques_coordinates[0]) * math.cos(
                    (math.pi / 180) * spheriques_coordinates[1])

                y = r * math.cos((math.pi / 180) * spheriques_coordinates[0]) * math.sin(
                    (math.pi / 180) * spheriques_coordinates[1])

                z = r * math.sin((math.pi / 180) * spheriques_coordinates[0])

                cartesiennes_coordinates_of_point = [x, y, z]

                cartesiennes_coordinates_for_all_points.append(cartesiennes_coordinates_of_point)

            gravity_x = 0

            gravity_y = 0

            area = 0

            for i in range(0, len(cartesiennes_coordinates_for_one_irregular_polygon[0]) - 1):
                area += (cartesiennes_coordinates_for_one_irregular_polygon[0][i][0] *
                         cartesiennes_coordinates_for_one_irregular_polygon[0][i + 1][1]
                         - cartesiennes_coordinates_for_one_irregular_polygon[0][i + 1][0] *
                         cartesiennes_coordinates_for_one_irregular_polygon[0][i][1])

            area = area / 2

            for i in range(0, len(cartesiennes_coordinates_for_one_irregular_polygon[0]) - 1):
                gravity_x += (cartesiennes_coordinates_for_one_irregular_polygon[0][i][0] +
                              cartesiennes_coordinates_for_one_irregular_polygon[0][i + 1][0]) \
                             * (cartesiennes_coordinates_for_one_irregular_polygon[0][i][0] *
                                cartesiennes_coordinates_for_one_irregular_polygon[0][i + 1][1]
                                - cartesiennes_coordinates_for_one_irregular_polygon[0][i + 1][0] *
                                cartesiennes_coordinates_for_one_irregular_polygon[0][i][1])

            for i in range(0, len(cartesiennes_coordinates_for_one_irregular_polygon[0]) - 1):
                gravity_y += (cartesiennes_coordinates_for_one_irregular_polygon[0][i][1] +
                              cartesiennes_coordinates_for_one_irregular_polygon[0][i + 1][1]) \
                             * (cartesiennes_coordinates_for_one_irregular_polygon[0][i][0] *
                                cartesiennes_coordinates_for_one_irregular_polygon[0][i + 1][1]
                                - cartesiennes_coordinates_for_one_irregular_polygon[0][i + 1][0] *
                                cartesiennes_coordinates_for_one_irregular_polygon[0][i][1])

            gravity_x = gravity_x / (6 * area)

            gravity_y = gravity_y / (6 * area)

            gravity_center = [gravity_x, gravity_y]

            return gravity_center

        coordinates_parcelle_a = [[[6.1055132138, 49.2613410884], [6.1054032167, 49.2614320883], [6.1050093722, 49.2617634105],
                 [6.1037109583, 49.2631004489], [6.102905707, 49.2641809734], [6.1024951006, 49.2651721682],
                 [6.1019456221, 49.2663234729], [6.1016670436, 49.2668353465], [6.1011728852, 49.2674661197],
                 [6.1010377333, 49.2675964467], [6.100773898, 49.2677129886], [6.1002005343, 49.2678033],
                 [6.0955101152, 49.2684743688], [6.0909523008, 49.2690887738], [6.0883123008, 49.2696116271],
                 [6.0866025671, 49.270080929], [6.0844158257, 49.2706208823], [6.0825968134, 49.2710110519],
                 [6.0818331769, 49.2711394238], [6.0810940362, 49.2711484117], [6.0808535582, 49.2710582926],
                 [6.0797739922, 49.270730504], [6.0782792187, 49.2708406352], [6.0756589659, 49.2711674786],
                 [6.0730400527, 49.2714942301], [6.0725373255, 49.2715484214], [6.0691596423, 49.2719016113],
                 [6.0685734331, 49.2719624082], [6.067772706, 49.2720457518], [6.0659841291, 49.272233373],
                 [6.065620721, 49.2722722982], [6.0656348621, 49.2722557453], [6.0662072739, 49.2718003725],
                 [6.0677212415, 49.2707164943], [6.0705373709, 49.2683885308], [6.0740082405, 49.2643155789],
                 [6.0756918354, 49.2614234579], [6.0797578467, 49.261122658], [6.0807591618, 49.2603953496],
                 [6.0814359986, 49.2597132099], [6.0828315021, 49.2563560019], [6.0829515206, 49.2561100251],
                 [6.08296013, 49.256000946], [6.0829605587, 49.2558929758], [6.0834642576, 49.2556965649],
                 [6.0848817525, 49.2556117248], [6.0857049414, 49.2557939841], [6.0908407193, 49.2555085976],
                 [6.0931601169, 49.2556119577], [6.0955867043, 49.2559212439], [6.1000642601, 49.2571044246],
                 [6.1029317601, 49.2589397599], [6.1050272562, 49.2612834286], [6.1055132138, 49.2613410884]]]

        coordinates_parcelle_b = [[[4.9177958,46.1828466],[4.9177914,46.1828627],[4.9177359,46.1828569],[4.9177716,46.1827215],[4.9178048,46.182725],[4.9177737,46.1828443],[4.9177958,46.1828466]]]

        gravity_center_parcelle_a = calculate_gravity_center(coordinates_parcelle_a)

        gravity_center_parcelle_b = calculate_gravity_center(coordinates_parcelle_b)

        d = math.sqrt(math.pow((gravity_center_parcelle_b[0] - gravity_center_parcelle_a[0]), 2)
                      + math.pow((gravity_center_parcelle_b[1] - gravity_center_parcelle_a[1]), 2))

        print('distance between these two gravity center : ' + str(d) + " kms")

    # ok
    def test_check_the_presence_of_buildings_in_one_land_from_json_files(self):
        print('test_check_the_presence_of_buildings_in_one_land_from_json_files')

        f = open('cadastre-01001-parcelles.json', "r")
        data = json.loads(f.read())
        for feature in data['features']:
            try:
                lon_parcelle = float(feature["geometry"]["coordinates"][0][0][0])
                lat_parcelle = float(feature["geometry"]["coordinates"][0][0][1])

                # phi : latitude et lambda : longitude

                coordinates_parcelle = [lat_parcelle, lon_parcelle]

                f1 = open('cadastre-01001-batiments.json', "r")
                data1 = json.loads(f1.read())
                for feature1 in data1['features']:
                    try:
                        lon_batiment = float(feature1["geometry"]["coordinates"][0][0][0][0])
                        lat_batiment = float(feature1["geometry"]["coordinates"][0][0][0][1])

                        coordinates_batiment = [lat_batiment, lon_batiment]

                        r = 6372.795477598

                        a = math.pow(
                            math.sin((math.pi / 180) * ((coordinates_batiment[0] - coordinates_parcelle[0]) / 2)), 2) + \
                            math.cos((math.pi / 180) * coordinates_parcelle[0]) * math.cos(
                            (math.pi / 180) * coordinates_batiment[0]) \
                            * math.pow(
                            math.sin((math.pi / 180) * ((coordinates_batiment[1] - coordinates_parcelle[1]) / 2)), 2)

                        c = 2 * math.atan(math.sqrt(a / (1 - a)))

                        d = round(float(r * c), 2)

                        if d < float(0.04):
                            print("parcelle numéro : " + str(feature['properties']['prefixe']
                                                             + feature['properties']['section']
                                                             + feature['properties']['numero']
                                                             ) + " has buildings at : " + str(d) + " kms")
                            break
                        else:
                            print("parcelle numéro : " + str(feature['properties']['prefixe']
                                                             + feature['properties']['section']
                                                             + feature['properties']['numero']
                                                             ) + " buildings not yet at : " + str(d) + " kms")
                    except Exception as e:
                        print("error feature1 : " + str(e))
                f1.close()
            except Exception as e:
                print('error : ' + str(e))
        f.close()

    # ok
    def test_check_the_presence_of_buildings_in_one_land_from_json_files_url(self):
        print('test_check_the_presence_of_buildings_in_one_land_from_json_files_url')

        lon_parcelle = 4.9199294
        lat_parcelle = 46.1804076

        prefixe = "000"
        section = "A"
        numero = "842"

        # phi : latitude et lambda : longitude

        coordinates_parcelle = [lat_parcelle, lon_parcelle]

        url = "https://api-adresse.data.gouv.fr/reverse/?lon=" + str(lon_parcelle) + "&lat=" + str(lat_parcelle)

        response = requests.request("GET", url)

        json_format = json.loads(response.text)

        about = "batiments"

        code_insee_commune = json_format['features'][0]['properties']['citycode']

        code_insee_departement = code_insee_commune[:2]

        url_zip_file_for_batiments = "https://cadastre.data.gouv.fr/data/etalab-cadastre/latest/geojson/communes/" \
                                     + code_insee_departement + "/" \
                                     + code_insee_commune + "/cadastre-" + code_insee_commune + "-" + about + ".json.gz"

        resp = requests.get(url_zip_file_for_batiments, stream=True)

        # donwload gz file
        batiment_gz_filename = "cadastre-" + code_insee_commune + "-" + about + ".json.gz"
        gz_file = open(batiment_gz_filename, 'wb')
        gz_file.write(resp.content)
        gz_file.close()

        # extract json file
        input_file = gzip.GzipFile(batiment_gz_filename, 'rb')
        s = input_file.read()
        input_file.close()

        batiment_json_filename = batiment_gz_filename[:-3]
        output_file = open(batiment_json_filename, 'wb')
        output_file.write(s)
        output_file.close()

        f1 = open(batiment_json_filename, "r")
        data1 = json.loads(f1.read())
        for feature1 in data1['features']:
            try:
                lon_batiment = float(feature1["geometry"]["coordinates"][0][0][0][0])
                lat_batiment = float(feature1["geometry"]["coordinates"][0][0][0][1])

                coordinates_batiment = [lat_batiment, lon_batiment]

                r = 6372.795477598

                a = math.pow(
                    math.sin((math.pi / 180) * ((coordinates_batiment[0] - coordinates_parcelle[0]) / 2)), 2) + \
                    math.cos((math.pi / 180) * coordinates_parcelle[0]) * math.cos(
                    (math.pi / 180) * coordinates_batiment[0]) \
                    * math.pow(
                    math.sin((math.pi / 180) * ((coordinates_batiment[1] - coordinates_parcelle[1]) / 2)), 2)

                c = 2 * math.atan(math.sqrt(a / (1 - a)))

                d = round(float(r * c), 2)

                if d <= float(0.02):
                    print("parcelle numéro : " + str(prefixe + section + numero)
                          + " has buildings at : " + str(d) + " kms")
                    break
                else:
                    print("parcelle numéro : " + str(prefixe + section + numero)
                          + " buildings not yet at : " + str(d) + " kms")
            except Exception as e:
                print("error feature1 : " + str(e))
        f1.close()

        # delete gz file and json file for batiments
        os.remove(batiment_gz_filename)
        os.remove(batiment_json_filename)


class UnitTestsPhysicsElectrical(unittest.TestCase):
    # ok
    def test_calculate_the_maximal_length_of_the_wire_for_electrical_transformers(self):
        print('test_calculate_the_maximal_length_of_the_wire_for_electrical_transformers')

        # The maximal length of the wire in mm.
        maximal_wire_length = 0

        # The number of steps of the coil.
        m = 8

        # The maximal diameter of the wire in mm.
        gamma = 3.38

        # The maximal radius of the core in mm.
        r = 28.7/2

        # The maximal number of turns around the core.
        n_max_core = 151

        for n in range(0, m):
            print('n : ' + str(n))
            maximal_wire_length += 2*math.pi*(r + n*gamma)*n_max_core

        print('maximal_wire_length : ' + str(maximal_wire_length) + ' mm')
        print('maximal_wire_length : ' + str(float(maximal_wire_length)/1000) + ' m')


if __name__ == '__main__':
    unittest.main()
