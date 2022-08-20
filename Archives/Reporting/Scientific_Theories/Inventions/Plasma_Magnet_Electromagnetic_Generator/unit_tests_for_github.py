import unittest
import numpy as np
import matplotlib.pyplot as plt
import math


class UnitTestsReportingScientificTheoriesInventionsPMEGForGitHub(unittest.TestCase):
    # ok
    def test_plot_u1_function(self):
        print('test_plot_u1_function')

        plot = 'plot_of_u1_function.jpg'

        # Constants
        mu_0 = 4 * np.pi * math.pow(10, -7)
        f_0 = math.pow(10, 6)
        omega_0 = 2 * np.pi * f_0
        t_0 = 1/f_0
        i_0 = 120 * math.pow(10, -3)
        d_vis = 22 * math.pow(10, -3)
        # Constants

        t = np.linspace(0, t_0, int(math.pow(10, 3)))

        y = (- i_0 * mu_0 * omega_0 * np.sin(omega_0 * t))/(np.pi * d_vis)

        plt.plot(t, y)

        plt.title("Plot of U1(t) function")

        plt.xlabel("Values of t")

        plt.ylabel("Values of y")

        plt.savefig(plot, bbox_inches='tight', dpi=150)

        plt.show()

    # ok
    def test_plot_i1_function(self):
        print('test_plot_i1_function')

        plot = 'plot_i1_function.jpg'

        # Constants
        mu_b = 4 * np.pi * math.pow(10, -7)
        f_0 = math.pow(10, 6)
        omega_0 = 2 * np.pi * f_0
        t_0 = 1/f_0
        b_0 = math.pow(10, 1)
        b_1 = math.pow(10, 1)
        b_2 = math.pow(10, 1)
        l_b = 10 * math.pow(10, -2)
        n_b = 100
        # Constants

        t = np.linspace(0, t_0, int(math.pow(10, 3)))

        y = (- l_b * (b_0 * np.cos(omega_0 * t) + b_1 + b_2))/(mu_b * math.pow(n_b, 2))

        plt.plot(t, y)

        plt.title("Plot of I1(t) function")

        plt.xlabel("Values of t")

        plt.ylabel("Values of y")

        plt.savefig(plot, bbox_inches='tight', dpi=150)

        plt.show()

    # ok
    def test_plot_pma_function(self):
        print('test_plot_pma_function')

        plot = 'plot_pma_function.jpg'

        # Constants
        mu_0 = 4 * np.pi * math.pow(10, -7)
        mu_b = 4 * np.pi * math.pow(10, -7)
        f_0 = math.pow(10, 6)
        omega_0 = 2 * np.pi * f_0
        t_0 = 1/f_0
        i_0 = 120 * math.pow(10, -3)
        b_1 = math.pow(10, 1)
        b_2 = math.pow(10, 1)
        l_b = 10 * math.pow(10, -2)
        n_b = 100
        s_b = math.pow(10, -2)
        d_vis = 22 * math.pow(10, -3)
        # Constants

        t = np.linspace(0, t_0, int(math.pow(10, 3)))

        y = ((- i_0 * mu_0 * omega_0 * l_b * s_b * np.sin(omega_0 * t)) * ((i_0 * mu_0 * np.cos(omega_0 * t))/np.pi
                                                                           * d_vis + b_1 + b_2))/(np.pi * d_vis * mu_b
                                                                                                  * math.pow(n_b, 2))

        plt.plot(t, y)

        plt.title("Plot of Pma(t) function")

        plt.xlabel("Values of t")

        plt.ylabel("Values of y")

        plt.savefig(plot, bbox_inches='tight', dpi=150)

        plt.show()

    # ok
    def test_plot_cop_function(self):
        print('test_plot_cop_function')

        plot = 'plot_cop_function.jpg'

        # Constants
        mu_0 = 4 * np.pi * math.pow(10, -7)
        mu_b = 4 * np.pi * math.pow(10, -7)
        f_0 = math.pow(10, 6)
        omega_0 = 2 * np.pi * f_0
        t_0 = 1/f_0
        i_0 = 120 * math.pow(10, -3)
        u_0 = math.pow(10, 4)
        b_1 = math.pow(10, 1)
        b_2 = math.pow(10, 1)
        l_b = 10 * math.pow(10, -2)
        n_b = 100
        s_b = math.pow(10, -2)
        d_vis = 22 * math.pow(10, -3)
        # Constants

        t = np.linspace(0, t_0, int(math.pow(10, 3)))

        y = (- mu_0 * omega_0 * l_b * s_b * np.tan(omega_0 * t) * ((i_0 * mu_0 * np.cos(omega_0 * t))/(np.pi * d_vis)
                                                                   + b_1 + b_2))/(np.pi * d_vis * mu_b
                                                                                  * math.pow(n_b, 2) * u_0
                                                                                  * np.cos(omega_0 * t))

        plt.plot(t, y)

        plt.title("Plot of COP function")

        plt.xlabel("Values of t")

        plt.ylabel("Values of y")

        plt.savefig(plot, bbox_inches='tight', dpi=150)

        plt.show()


if __name__ == '__main__':
    unittest.main()
