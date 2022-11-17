import unittest


class Unit_Tests_Infflux(unittest.TestCase):
    def test_tableau_dimension_5_sur_5(self):
        print('test_tableau_dimension_5_sur_5')
        # ALGORITHME //test_tableau_dimension_5_sur_5
        #   <partie déclarations>
        #   VARIABLE liste_coordonnees_cases : [34, 21, 32, 41, 25, 14, 22, 43, 14, 31, 54, 45, 52, 42, 23, 33, 15, 51, 31, 35, 21, 52, 33, 13, 23]
        #   VARIABLE l_c_c : length(liste_coordonnees_cases) : longueur de la liste 'liste_coordonnees_cases'
        #   VARIABLE n_l_c : numéro de la ligne de la case actuelle ou départ = 1
        #   VARIABLE n_c_c : numéro de la colonne de la case actuelle ou départ = 1
        #
        #   DEBUT
        #       <partie instructions>
        #       POUR i ALLANT_DE 0 A l_c_c {PAR_PAS_DE 1}
        #           # On compare les coordonnées de la case actuelle avec les coordonnées de la case choisie dans
        #           la liste 'liste_coordonnees_cases' afin de voir si les coordonnées sont identiques.
        #           SI  n_l_c == liste_coordonnees_cases[i][0] ET n_c_c == liste_coordonnees_cases[i][1] ALORS
        #               BREAK
        #               # (L'algorithme s'arrête lorsqu'il a trouvé la case contenant ses propres coordonnées.)
        #           SINON
        #               # L'algorithme saute d'une case à l'autre en suivant les coordonnées qu'elle contient en
        #               changeant les coordonnées de la case actuelle
        #                n_l_c = liste_coordonnees_cases[i][0]
        #                n_c_c = liste_coordonnees_cases[i][1]
        #           FIN_SI
        #       FIN_POUR
        #   FIN


if __name__ == '__main__':
    unittest.main()
