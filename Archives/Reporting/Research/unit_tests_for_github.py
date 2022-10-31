import unittest
import pdfkit


class UnitTestsResearchForGitHub(unittest.TestCase):
    # ok
    def test_cahier_des_charges_de_travaux_d_experimentation_n_machine(self):
        print('test_cahier_des_charges_de_travaux_d_experimentation_n_machine')

        body = """
<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" 
    href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css" 
    integrity="sha384-xOolHFLEh07PJGoPkLv1IbcEPTNtaed2xpHsD9ESMhqIYd0nLMwNLD69Npy4HI+N" 
    crossorigin="anonymous">

    <title>
        Cahier des charges de travaux d'experimentation sur la 'N machine'
    </title>
  </head>
  <body>
    <!-- Container -->
    <div class="container">
        <!-- Cahier des charges de travaux d'expérimentation sur la 'N machine' -->
        <div class="card text-center">
          <div class="card-header">
            Cahier des charges de travaux d'expérimentation sur la 'N machine'
          </div>
          <div class="card-body">
            <!-- Objectif -->
            <div class="card text-center">
              <div class="card-header">
                Objectif
              </div>
              <div class="card-body">
                <h6>
                    L'objectif des travaux d'expérimentation sur la 'N machine' est de rédiger un rapport scientfique 
                    décrivant le fonctionnement, les avantages et les inconvénients de la machine.
                </h6>
              </div>
            </div>
            <!-- Objectif -->

            <br>
            <br>

            <!-- Etat de l'art -->
            <div class="card text-center">
              <div class="card-header">
                Etat de l'art
              </div>
              <div class="card-body">
                <h6>
                    Dans un premier temps, le générateur d'électricité 'N machine' provient du paradoxe de Faraday qui 
                    est une expérience décrite pour la première fois par Michael Faraday, qui semble à première vue 
                    contredire sa loi d'induction.
                    
                    <br>
                    <br>
                    
                    Selon le montage du Michael Faraday, le dispositif expérimental se compose d'un aimant 
                    permanent cylindrique et d'un disque conducteur adjacent, tous deux disposés de manière à 
                    tourner autour d'un axe. L'axe de symétrie de l'aimant et du disque coïncide avec l'axe de 
                    rotation, et l'aimant a sa polarisation dans la direction axiale (c'est-à-dire que les pôles 
                    sont sur l'axe). La tension électrique est mesurée sur le disque entre l'axe et son bord ; à cet 
                    effet, des contacts glissants sont placés sur sa face externe et près de l'axe.
                    
                    <br>
                    <br>
                    
                    Après, la problèmatique du disque de Faraday montre que si l'on fait tourner le disque alors 
                    que l'aimant est au repos, une tension est produite aux bornes. Cela peut être décrit par la 
                    force de Lorentz ou la règle du flux (induction unipolaire). La tension aux bornes apparaît 
                    également lorsque le disque et l'aimant sont reliés mécaniquement et déplacés ensemble. Si, 
                    par contre, seul l'aimant est déplacé et que le disque est au repos, aucune tension aux bornes 
                    n'apparaît. Cela laissait Faraday perplexe car il supposait que tout ce qui importait pour que la 
                    tension se produise était que le disque se déplace contre l'aimant.
                    
                    <br>
                    <br>
                    
                    Ensuite, dans les années 70, un inventeur connu sous le nom de Bruce Depalma fit la découverte de 
                    la 'N machine' dont N siginfiant "à l'énième degré", parce qu'il considère que la machine a un 
                    potentiel de rendement presque illimité, et aussi parce qu'il suppose qu'un aimant se branche sur 
                    l'énergie d'une autre dimension. Il pense que les aimants créent une distorsion de l’éther, qui 
                    permet à l'énergie de l'espace de couler dans la machine, et il breveta sa 'N machine' dont le 
                    numéro de brevet est : WO1995008210A1.
                    
                    <br>
                    <br>
                    
                    Aujourd'hui, très peu de scientifiques se sont penchés sur cette machine, et cela est très 
                    compréhensible puisque la source d'énergie collectée par la 'N machine' vient en grande partie de 
                    de cette fameuse énergie communément appelée l'énergie de l'espace ou l'énergie quantique du vide 
                    ou l'énergie du point zéro, et cette source d'énergie est accessible gratuitement en tout point de 
                    l'univers.
                    
                    <br>
                    <br>
                    
                    Ainsi, le but de ce cahier des charges de travaux d'expérimentation est d'approfondir les 
                    connaissances sur la 'N machine' tant sur le plan énergétique, économique, écologique et social.
                </h6>
              </div>
            </div>
            <!-- Etat de l'art -->

            <br>
            <br>

            <!-- Tâches -->
            <div class="card text-center">
              <div class="card-header">
                Tâches
              </div>
              <div class="card-body">
                <h6>
                    Les travaux d'expérimentation se porteront sur un générateur d'électricité nommé 'N machine' qui 
                    a été fabriqué par Monsieur Jason ALOYAU.
                </h6>
                
                <br>
                <br>
                
                <table class="table table-bordered">
                  <thead>
                    <tr>
                        <th scope="col">
                            Numéro de tâche
                        </th>
                        <th scope="col">
                            Détail de la tâche
                        </th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                        <td>
                            1
                        </td>
                        <td>
                            Mesurer la tension de sortie, l'intensité de sortie et la puissance de sortie du générateur d'électricité
                            en fonction de la vitesse de rotation de l'arbre du générateur d'électricité
                        </td>
                    </tr>
                    <tr>
                        <td>
                            2
                        </td>
                        <td>
                            Mesurer la température du générateur d'électricité en fonction de la vitesse de rotation 
                            de l'arbre du générateur d'électricité
                        </td>
                    </tr>
                    <tr>
                        <td>
                            3
                        </td>
                        <td>
                            Etablir un coefficient de performance du générateur d'électricité en fonction de la 
                            vitesse de rotation de l'arbre du générateur d'électricité
                        </td>
                    </tr>
                    <tr>
                        <td>
                            4
                        </td>
                        <td>
                            Mesurer les champs magnétiques autour du générateur d'électricité avec un détecteur de 
                            champs magnétiques en fonction de la vitesse de rotation de l'arbre du générateur 
                            d'électricité
                        </td>
                    </tr>
                    <tr>
                        <td>
                            5
                        </td>
                        <td>
                            Décrire les perspectives du générateur d'électricité sur le plan énergétique
                        </td>
                    </tr>
                    <tr>
                        <td>
                            6
                        </td>
                        <td>
                            Décrire les perspectives du générateur d'électricité sur le plan économique
                        </td>
                    </tr>
                    <tr>
                        <td>
                            7
                        </td>
                        <td>
                            Décrire les perspectives du générateur d'électricité sur le plan écologique
                        </td>
                    </tr>
                    <tr>
                        <td>
                            8
                        </td>
                        <td>
                            Décrire les perspectives du générateur d'électricité sur le plan social
                        </td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
            <!-- Tâches -->

            <br>
            <br>

        </div>
        <!-- Cahier des charges de travaux d'expérimentation sur la 'N machine' -->
    </div>
    <!-- Container -->

    <!-- Option 1: jQuery and Bootstrap Bundle (includes Popper) -->
    <script src="https://cdn.jsdelivr.net/npm/jquery@3.5.1/dist/jquery.slim.min.js" 
    integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" 
    crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/js/bootstrap.bundle.min.js" 
    integrity="sha384-Fy6S3B9q64WdZWQUiU+q4/2Lc9npb8tCaSX9FK7E8HnRr0Jz8D6OP9dO5Vg3Q9ct" 
    crossorigin="anonymous"></script>
  </body>
</html>
        """

        options = {
            'page-size': 'A4',
            'footer-right': '[page] sur [topage]',
            'header-center': "Cahier des charges de travaux d'expérimentation de la 'N machine'",
        }

        pdfkit.from_string(
            body,
            "Research\\Cahier_des_charges_de_travaux_d_experimentation_n_machine.pdf",
            options=options
        )


if __name__ == '__main__':
    unittest.main()
