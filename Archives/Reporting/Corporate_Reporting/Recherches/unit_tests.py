import unittest
import pdfkit


class UnitTestsRecherches(unittest.TestCase):
    # ok
    def test_cahier_des_charges_travaux_recherches_developpement(self):
        print("test_cahier_des_charges_travaux_recherches_developpement")

        body = """
        <!doctype html>
        <html lang="en">
          <head>
            <!-- Required meta tags -->
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">

            <!-- Bootstrap CSS -->
            <link 
            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/css/bootstrap.min.css" 
            rel="stylesheet" 
            integrity="sha384-BmbxuPwQa2lc/FVzBcNJ7UAyJxM6wuqIj61tLrc4wSX0szH/Ev+nYRRuWlolflfl" 
            crossorigin="anonymous">

            <title>
                Cahier des charges des travaux de recherches et développements de l'électrolyseur à eau de Stanley Meyer
            </title>
          </head>
          <body>
            <div class="container">

                <br>

                <div class="card text-center">
                  <div class="card-header">
                    Informations générales de la société Holomorphe
                  </div>
                  <div class="card-body">
                    <ul class="list-group list-group-flush">
                      <li class="list-group-item">
                        Dénomination sociale : S.A.S.U. à capital variable HOLOMORPHE / Capital social : 100 euros
                        </li>
                      <li class="list-group-item">
                        Adresse du siège social : 31 Avenue de Ségur - ABC LIV Ségur - 75007 Paris 
                        / Siret : 88363255600014
                      </li>
                      <li class="list-group-item">
                        Registre du commerce et des sociétés : R.C.S. PARIS - Greffe du Tribunal de Commerce de PARIS
                      </li>
                      <li class="list-group-item">
                        Activités : Commerce de gros de produits chimiques - Edition de logiciels applicatifs 
                        / Code NAF : 4675Z
                      </li>
                      <li class="list-group-item">
                        Numero TVA intracommunataire : FR06883632556 / Président : Monsieur  
                        / Date d'immatriculation : 26 Mai 2020
                      </li>
                    </ul>
                  </div>
                </div>

                <br>
                
                <div class="card text-center">
                  <div class="card-header">
                    Contact
                  </div>
                  <div class="card-body">
                    <!-- Informations personnelles -->
                    <table class="table table-striped table-bordered">
                        <thead>
                            <tr>
                                <th scope="col">Personne à contacter</th>
                                <th scope="col">Adresse du siège social</th>
                                <th scope="col">Téléphone</th>
                                <th scope="col">E-mail professionnel</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>
                                     
                                </td>
                                <td>
                                    
                                </td>
                                <td>
                                    
                                </td>
                                <td>
                                    
                                </td>
                            </tr>
                        </tbody>
                    </table>
                  </div>
                </div>
                
                <br>
                
                <div class="card text-center">
                  <div class="card-header">
                    Objectif des travaux de recherches et développements de l'électrolyseur à eau de Stanley Meyer
                  </div>
                  <div class="card-body">
                    L'objectif principal des travaux de recherches et développements de l'électrolyseur à eau de 
                    Stanley Meyer est de calculer le rendement énergétique de l'électrolyseur à eau de Stanley Meyer.
                  </div>
                </div>

                <br>
                
                <div class="card text-center">
                  <div class="card-header">
                    Etat de l'art de l'électrolyseur à eau de Stanley Meyer
                  </div>
                  <div class="card-body">
                    Tout d'abord, l'électrolyseur à eau de Stanley Meyer se base sur le principe de la polarisation 
                    électronique de la molécule d'eau car la molécule d'eau est une molécule polaire.
                    <br>
                    <br>
                    Puis, son fonctionnement requiert un circuit électronique LC à la fréquence de résonance du circuit 
                    afin d'entamer un phénomène de résonance pour pouvoir créer une accumulation d'énergie sous forme 
                    électrique voire électromagnétique aux bornes du condensateur.
                    <br>
                    <br>
                    Lorsque cette énergie emmagasinée aux bornes du condensateur est supérieure à l'énergie de 
                    dissociation de la liaison covalente entre l'atome d'hydrogène et l'atome d'oxygène de la 
                    mocécule d'eau, l'atome d'hydrogène et l'atome d'oxygène sont respectivement attirés vers le 
                    pôle négatif et le pôle positif du condensateur électrique et nous obtenons une production de 
                    dihydrogène et dioxygène.
                    <br>
                    <br>
                    Selon les brevets de Stanley Meyer, la production du mélange gazeux de dihydrogène et de dioxygène 
                    s'augmente avec l'augmentation de la tension électrique aux bornes du condensateur à condition de 
                    rester à la fréquence de résonance du circuit électronique LC sans l'utilisation d'électrolyte.
                    <br>
                    <br>
                    Ainsi, nous devons retenir que l'électrolyseur à eau de Stanley Meyer est un circuit 
                    électronique LC dont le condensateur peut être configuré de différentes manières et l'eau est 
                    considéré comme un matériau diélectrique qui subit le phénomène de polarisation électronique 
                    et non pas le phénomène d'électrolyse.
                    <br>
                    <br>
                    Maintenant, le calcul du rendement énergétique de l'électrolyseur à eau de Stanley Meyer 
                    doit être effectué pour comprendre davantage cette technologie.
                  </div>
                </div>

                <br>
                <br>
                <br>
                <br>

                <div class="card text-center">
                  <div class="card-header">
                    Tâches à accomplir
                  </div>
                  <div class="card-body">
                    Toutes les expérimentations devront toujours être effectuées à la fréquence de résonance du circuit 
                    électronique LC de l'électrolyseur à eau de Stanley Meyer.
                    
                    <br>
                    <br>
                    
                    <table class="table table-striped table-bordered">
                        <thead>
                            <tr>
                                <th scope="col">
                                    Numéro de la tâche
                                </th>
                                <th scope="col">
                                    Nom de la tâche
                                </th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>
                                    1
                                </td>
                                <td>
                                    Démontrer mathématiquement la formule de l'inductance d'une bobine électrique 
                                    cylindrique.
                                </td>
                            </tr>
                            <tr>
                                <td>
                                    2
                                </td>
                                <td>
                                    Démontrer mathématiquement la formule de la capacité d'un condensateur électrique 
                                    plan en utilisant l'eau comme isolant ou matériau diélectrique en régime 
                                    sinusoïdal pouvant faire intervenir des termes en nombre complexe.
                                </td>
                            </tr>
                            <tr>
                                <td>
                                    3
                                </td>
                                <td>
                                    Démontrer mathématiquement la formule de la fréquence de résonance du circuit 
                                    électronnique LC de l'électrolyseur à eau de Stanley Meyer en régime sinusoïdal 
                                    sans partie négative pouvant faire intervenir des termes en nombre complexe.
                                </td>
                            </tr>
                            <tr>
                                <td>
                                    4
                                </td>
                                <td>
                                    Démontrer mathématiquement la tension électrique aux bornes du condensateur 
                                    électrique plan du circuit électronique LC de l'électrolyseur à eau de Stanley Meyer 
                                    en régime sinusoïdal sans partie négative pouvant faire intervenir des termes 
                                    en nombre complexe en fonction du temps et à la fréquence de résonance du 
                                    circuit électronique LC de l'électrolyseur à eau de Stanley Meyer.
                                </td>
                            </tr>
                            <tr>
                                <td>
                                    5
                                </td>
                                <td>
                                    Démontrer mathématiquement la charge électrique aux bornes du condensateur 
                                    électrique plan du circuit électronique LC de l'électrolyseur à eau de Stanley Meyer 
                                    en régime sinusoïdal sans partie négative pouvant faire intervenir des termes en 
                                    nombre complexe en fonction du temps et à la fréquence de résonance du circuit 
                                    électronique LC de l'électrolyseur à eau de Stanley Meyer.
                                </td>
                            </tr>
                            <tr>
                                <td>
                                    6
                                </td>
                                <td>
                                    Démontrer mathématiquement la quantité de matière d'électrons aux bornes du 
                                    condensateur électrique plan du circuit électronique LC de l'électrolyseur à eau 
                                    de Stanley Meyer en régime sinusoïdal sans partie négative pouvant faire 
                                    intervenir des termes en nombre complexe en fonction du temps et à la fréquence de 
                                    résonance du circuit électronique LC de l'électrolyseur à eau de Stanley Meyer.
                                </td>
                            </tr>
                            <tr>
                                <td>
                                    7
                                </td>
                                <td>
                                    Démontrer mathématiquement la quantité de matière de dihydrogène produite 
                                    aux bornes du condensateur électrique plan du circuit électronique LC de 
                                    l'électrolyseur à eau de Stanley Meyer en régime sinusoïdal sans partie négative 
                                    pouvant faire intervenir des termes en nombre complexe en fonction du temps et à la 
                                    fréquence de résonance du circuit électronique LC de l'électrolyseur à eau de 
                                    Stanley Meyer.
                                </td>
                            </tr>
                            <tr>
                                <td>
                                    8
                                </td>
                                <td>
                                    Démontrer mathématiquement la quantité d'énergie embarquée dans la quantité de 
                                    matière de dihydrogène produite aux bornes du condensateur électrique plan du 
                                    circuit électronique LC de l'électrolyseur à eau de Stanley Meyer en régime 
                                    sinusoïdal sans partie négative pouvant faire intervenir des termes en nombre 
                                    complexe en fonction du temps et à la fréquence de résonance du circuit 
                                    électronique LC de l'électrolyseur à eau de Stanley Meyer.
                                </td>
                            </tr>
                            <tr>
                                <td>
                                    9
                                </td>
                                <td>
                                    Démontrer mathématiquement le rendement énergétique de l'électrolyseur à eau de 
                                    Stanley Meyer en régime sinusoïdal sans partie négative pouvant faire intervenir 
                                    des termes en nombre complexe en fonction du temps et à la fréquence de résonance du 
                                    circuit électronique LC de l'électrolyseur à eau de Stanley Meyer.
                                </td>
                            </tr>
                            <tr>
                                <td>
                                    10
                                </td>
                                <td>
                                    Démontrer mathématiquement la température de fonctionnement de l'électrolyseur à 
                                    eau de Stanley Meyer en régime sinusoïdal sans partie négative pouvant faire 
                                    intervenir des termes en nombre complexe en fonction du temps et à la fréquence 
                                    de résonance du circuit électronique LC de l'électrolyseur à eau de Stanley Meyer.
                                </td>
                            </tr>
                            <tr>
                                <td>
                                    11
                                </td>
                                <td>
                                    Démontrer mathématiquement la pression de fonctionnement de l'électrolyseur à 
                                    eau de Stanley Meyer en régime sinusoïdal sans partie négative pouvant faire 
                                    intervenir des termes en nombre complexe en fonction du temps et à la fréquence 
                                    de résonance du circuit électronique LC de l'électrolyseur à eau de Stanley Meyer.
                                </td>
                            </tr>
                            <tr>
                                <td>
                                    12
                                </td>
                                <td>
                                    Calculer expérimentalement le rendement énergétique de l'électrolyseur à eau de 
                                    Stanley Meyer en régime sinusoïdal sans partie négative et à la fréquence de 
                                    résonance du circuit électronique LC de l'électrolyseur à eau de Stanley Meyer 
                                    avec une tension électrique d'entrée égale à 230 volts à 50/60 Hz en utilisant un 
                                    seul condensateur plan.
                                </td>
                            </tr>
                            <tr>
                                <td>
                                    13
                                </td>
                                <td>
                                    Calculer expérimentalement le rendement énergétique de l'électrolyseur à eau de 
                                    Stanley Meyer en régime sinusoïdal sans partie négative et à la fréquence de 
                                    résonance du circuit électronique LC de l'électrolyseur à eau de Stanley Meyer 
                                    avec une tension électrique d'entrée égale à 230 volts à 50/60 Hz en utilisant 
                                    deux condensateurs plan en dérivation.
                                </td>
                            </tr>
                            <tr>
                                <td>
                                    14
                                </td>
                                <td>
                                    Calculer expérimentalement le rendement énergétique de l'électrolyseur à eau de 
                                    Stanley Meyer en régime sinusoïdal sans partie négative et à la fréquence de 
                                    résonance du circuit électronique LC de l'électrolyseur à eau de Stanley Meyer 
                                    avec une tension électrique d'entrée égale à 230 volts à 50/60 Hz en utilisant 
                                    quatre condensateurs plan en dérivation.
                                </td>
                            </tr>
                            <tr>
                                <td>
                                    15
                                </td>
                                <td>
                                    Calculer expérimentalement le rendement énergétique de l'électrolyseur à eau de 
                                    Stanley Meyer en régime sinusoïdal sans partie négative et à la fréquence de 
                                    résonance du circuit électronique LC de l'électrolyseur à eau de Stanley Meyer 
                                    avec une tension électrique d'entrée égale à 230 volts à 50/60 Hz en utilisant 
                                    huit condensateurs plan en dérivation.
                                </td>
                            </tr>
                            <tr>
                                <td>
                                    16
                                </td>
                                <td>
                                    Calculer expérimentalement le rendement énergétique de l'électrolyseur à eau de 
                                    Stanley Meyer en régime sinusoïdal sans partie négative et à la fréquence de 
                                    résonance du circuit électronique LC de l'électrolyseur à eau de Stanley Meyer 
                                    avec une tension électrique d'entrée égale à 230 volts à 50/60 Hz en utilisant 
                                    seize condensateurs plan en dérivation.
                                </td>
                            </tr>
                            <tr>
                                <td>
                                    17
                                </td>
                                <td>
                                    Calculer expérimentalement le rendement énergétique de l'électrolyseur à eau de 
                                    Stanley Meyer en régime sinusoïdal sans partie négative et à la fréquence de 
                                    résonance du circuit électronique LC de l'électrolyseur à eau de Stanley Meyer 
                                    avec une tension électrique d'entrée égale à 230 volts à 50/60 Hz en utilisant 
                                    trente-deux condensateurs plan en dérivation.
                                </td>
                            </tr>
                            <tr>
                                <td>
                                    18
                                </td>
                                <td>
                                    Rédiger un rapport scientifique écrit dans la langue française et la langue 
                                    anglaise pour lister les résultats de chaque tâche confirmés au nom de votre 
                                    laboratoire.
                                </td>
                            </tr>
                            <tr>
                                <td>
                                    19
                                </td>
                                <td>
                                    Diffuser les rapports scientifiques en ligne sur un site internet dédié pour 
                                    le monde de l'énergie voire le monde de l'hydrogène dont le téléchargement du 
                                    rapport scientifique sera payant pour le compte de la société Holomorphe et votre 
                                    laboratoire.
                                </td>
                            </tr>
                        </tbody>
                    </table>
                  </div>
                </div>
                
                <br>
                
                <div class="card text-center">
                  <div class="card-header">
                    Documentations
                  </div>
                  <div class="card-body">
                      <div class="list-group text-center">
                        <a href="https://patents.google.com/patent/US5149407A/en" 
                        class="list-group-item list-group-item-action">
                          Procédés et appareils pour la production de gaz combustible et la libération accrue de 
                          énergie thermique provenant de ce gaz - US5149407A
                        </a>
                        <a href="https://patents.google.com/patent/US4936961A/en?oq=4_936_961" 
                        class="list-group-item list-group-item-action">
                            Procédé de production d’un gaz combustible - US4936961A
                        </a>
                        <a href="https://patents.google.com/patent/US4798661A/en?oq=US_4_798_661" 
                        class="list-group-item list-group-item-action">
                            Circuit de contrôle de tension du générateur de gaz - US4798661A
                        </a>
                        <a href="https://patents.google.com/patent/CA1234773A/en" 
                        class="list-group-item list-group-item-action">
                            Générateur d’hydrogène à cavité résonnante qui fonctionne avec une tension pulsée 
                            potentiel électrique - CA1234773A
                        </a>
                        <a href="https://patents.google.com/patent/CA1234774A/en" 
                        class="list-group-item list-group-item-action">
                            Système générateur d’hydrogène - CA1234774A
                        </a>
                        <a href="https://patents.google.com/patent/WO1992007861A1/en?oq=4_936_961" 
                        class="list-group-item list-group-item-action">
                            Circuits de commande et de commande pour une pile produisant de l’hydrogène gazeux - 
                            WO1992007861A1
                        </a>
                        <a href="https://patents.google.com/patent/US4124463A/en?oq=US4124463" 
                        class="list-group-item list-group-item-action">
                            Cellule électrolytique - US4124463A
                        </a>
                        <a 
                        href="https://holomorphe.com/chemical-products/fundamental-research-of-the-us-patent-us4936961a" 
                        class="list-group-item list-group-item-action">
                            Recherche fondamentale pour le brevet américain US4936961A
                        </a>
                        <a href="https://holomorphe.com/chemical-products/electronic_circuit_diagram_of_stanley_meyer_water_electrolyser" 
                        class="list-group-item list-group-item-action">
                            Schéma de circuit électronique du brevet US 5149407 (électrolyseur à eau de Stanley Meyer)
                        </a>
                        <a href="https://holomorphe.com/chemical-products/about_stanley_meyer" 
                        class="list-group-item list-group-item-action">
                            À propos de Stanley Meyer
                        </a>
                        <a href="https://holomorphe.com/chemical-products/theories_to_know_about_stanley_meyer_water_electrolyser" 
                        class="list-group-item list-group-item-action">
                            Quelques théories à connaître sur l’électrolyseur à eau Stanley Meyer
                        </a>
                        <a href="https://holomorphe.com/chemical-products/hydrogen_generator" 
                        class="list-group-item list-group-item-action">
                            Générateur d’hydrogène de la société Holomorphe
                        </a>
                        <a href="https://holomorphe.com" 
                        class="list-group-item list-group-item-action">
                            Société Holomorphe
                        </a>
                      </div>
                  </div>
                </div>
                
              </div>

              <br>

            </div>

            <br>

            <!-- Option 1: Bootstrap Bundle with Popper -->
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/js/bootstrap.bundle.min.js" integrity="sha384-b5kHyXgcpbZJO/tY9Ul7kGkf1S0CWuKcCD38l8YkeH8z8QjE0GmW1gYU5S9FOnJ0" crossorigin="anonymous"></script>
          </body>
        </html>
        """

        options = {
            'page-size': 'A4',
            'header-center': "Cahier des charges de travaux de recherches et développements \n de "
                             "l'électrolyseur à eau de Stanley Meyer",
            'footer-right': '[page] sur [topage]',
            'footer-left': 'S.A.S.U.A.C.V. Holomorphe [SIREN : 883632556]'
        }

        path_wkthmltopdf = "C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe"
        config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
        pdfkit.from_string(body,
                           "Recherches\\Cahier_Charges_Travaux_Recherches_Developpement_[SASU_Holomorphe].pdf",
                           configuration=config,
                           options=options)

    #
    def test_cahier_des_charges_travaux_mesures_experimentation(self):
        print("test_cahier_des_charges_travaux_mesures_experimentation")

        body = """
        <!doctype html>
        <html lang="en">
          <head>
            <!-- Required meta tags -->
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">

            <!-- Bootstrap CSS -->
            <link 
            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/css/bootstrap.min.css" 
            rel="stylesheet" 
            integrity="sha384-BmbxuPwQa2lc/FVzBcNJ7UAyJxM6wuqIj61tLrc4wSX0szH/Ev+nYRRuWlolflfl" 
            crossorigin="anonymous">

            <title>
                Cahier des charges des travaux de mesures expérimentales du générateur d'hydrogène par électrolyse 
                de l'eau de Stanley Meyer
            </title>
          </head>
          <body>
            <div class="container">

                <br>

                <div class="card text-center">
                  <div class="card-header">
                    Informations générales de la société Holomorphe
                  </div>
                  <div class="card-body">
                    <ul class="list-group list-group-flush">
                      <li class="list-group-item">
                        Dénomination sociale : S.A.S.U. à capital variable HOLOMORPHE / Capital social : 100 euros
                        </li>
                      <li class="list-group-item">
                        Adresse du siège social : 31 Avenue de Ségur - ABC LIV Ségur - 75007 Paris 
                        / Siret : 88363255600014
                      </li>
                      <li class="list-group-item">
                        Registre du commerce et des sociétés : R.C.S. PARIS - Greffe du Tribunal de Commerce de PARIS
                      </li>
                      <li class="list-group-item">
                        Activité principale : Commerce de gros de produits chimiques / Code NAF : 4675Z
                      </li>
                      <li class="list-group-item">
                        Numero TVA intracommunataire : FR06883632556 / 
                        Président : Monsieur  / 
                        Date d'immatriculation : 26 Mai 2020
                      </li>
                    </ul>
                  </div>
                </div>

                <br>

                <div class="card text-center">
                  <div class="card-header">
                    Contact
                  </div>
                  <div class="card-body">
                    <!-- Informations personnelles -->
                    <table class="table table-striped table-bordered">
                        <thead>
                            <tr>
                                <th scope="col">Personne à contacter</th>
                                <th scope="col">Adresse du siège social</th>
                                <th scope="col">Téléphone</th>
                                <th scope="col">E-mail professionnel</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>
                                     
                                </td>
                                <td>
                                    
                                </td>
                                <td>
                                    
                                </td>
                                <td>
                                    
                                </td>
                            </tr>
                        </tbody>
                    </table>
                  </div>
                </div>

                <br>

                <div class="card text-center">
                  <div class="card-header">
                    Objectif des travaux de mesures expérimentales du générateur d'hydrogène par électrolyse de 
                    l'eau de Stanley Meyer
                  </div>
                  <div class="card-body">
                    L'objectif principal des travaux de mesures expérimentales du générateur d'hydrogène par 
                    électrolyse de l'eau de Stanley Meyer est de calculer le rendement énergétique du générateur 
                    d'hydrogène par électrolyse de l'eau de Stanley Meyer.
                  </div>
                </div>

                <br>

                <div class="card text-center">
                  <div class="card-header">
                    Etat de l'art du générateur d'hydrogène par électrolyse de l'eau de Stanley Meyer
                  </div>
                  <div class="card-body">
                    Tout d'abord, le générateur d'hydrogène par électrolyse de l'eau de Stanley Meyer se base sur 
                    le principe de la polarisation électronique de la molécule d'eau car la molécule d'eau est une 
                    molécule polaire.
                    
                    <br>
                    <br>
                    
                    Puis, son fonctionnement requiert un circuit électronique LC série à la fréquence de résonance du 
                    circuit afin d'entamer un phénomène de résonance pour pouvoir créer une accumulation d'énergie sous 
                    forme électrique voire électromagnétique aux bornes du condensateur.
                    
                    <br>
                    <br>
                    
                    Lorsque cette énergie emmagasinée aux bornes du condensateur est supérieure à l'énergie de 
                    dissociation de la liaison covalente entre l'atome d'hydrogène et l'atome d'oxygène de la 
                    mocécule d'eau, l'atome d'hydrogène et l'atome d'oxygène sont respectivement attirés vers le 
                    pôle négatif et le pôle positif du condensateur électrique et nous obtenons une production de 
                    dihydrogène et dioxygène.
                    
                    <br>
                    <br>
                    
                    Selon les brevets de Stanley Meyer, la production du mélange gazeux de dihydrogène et de dioxygène 
                    s'augmente avec l'augmentation de la tension électrique aux bornes du condensateur à condition de 
                    rester à la fréquence de résonance du circuit électronique LC série sans l'utilisation 
                    d'électrolyte.
                    
                    <br>
                    <br>
                    
                    Ainsi, nous devons retenir que le générateur d'hydrogène par électrolyse de l'eau de Stanley Meyer 
                    possède un circuit électronique LC série dont le condensateur peut être configuré de différentes 
                    manières et la molécule d'eau est considérée comme un matériau diélectrique qui subit le phénomène 
                    de polarisation électronique.
                    
                    <br>
                    <br>
                    
                    Maintenant, le calcul du rendement énergétique du générateur d'hydrogène par électrolyse de 
                    l'eau de Stanley Meyer doit être effectué pour comprendre davantage cette technologie.
                  </div>
                </div>

                <br>
                <br>
                <br>
                <br>

                <div class="card text-center">
                  <div class="card-header">
                    Tâches à accomplir
                  </div>
                  <div class="card-body">
                    Toutes les expérimentations devront toujours être effectuées à la fréquence de résonance du circuit 
                    électronique LC série du générateur d'hydrogène par électrolyse de l'eau de Stanley Meyer.

                    <br>
                    <br>

                    <table class="table table-striped table-bordered">
                        <thead>
                            <tr>
                                <th scope="col">
                                    Numéro de la tâche
                                </th>
                                <th scope="col">
                                    Nom de la tâche
                                </th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>
                                    1
                                </td>
                                <td>
                                    Démontrer mathématiquement la formule de l'inductance d'une bobine électrique 
                                    cylindrique.
                                </td>
                            </tr>
                            <tr>
                                <td>
                                    2
                                </td>
                                <td>
                                    Démontrer mathématiquement la formule de la capacité d'un condensateur électrique 
                                    plan en utilisant l'eau comme isolant ou matériau diélectrique en régime 
                                    sinusoïdal pouvant faire intervenir des termes en nombre complexe.
                                </td>
                            </tr>
                            <tr>
                                <td>
                                    3
                                </td>
                                <td>
                                    Démontrer mathématiquement la formule de la fréquence de résonance du circuit 
                                    électronnique LC série du générateur d'hydrogène par électrolyse de l'eau de 
                                    Stanley Meyer en régime sinusoïdal sans partie négative pouvant faire intervenir 
                                    des termes en nombre complexe.
                                </td>
                            </tr>
                            <tr>
                                <td>
                                    4
                                </td>
                                <td>
                                    Démontrer mathématiquement la tension électrique aux bornes du condensateur 
                                    électrique plan du circuit électronique LC série du générateur d'hydrogène par 
                                    électrolyse de l'eau de Stanley Meyer en régime sinusoïdal sans partie négative 
                                    pouvant faire intervenir des termes en nombre complexe en fonction du temps et à 
                                    la fréquence de résonance du circuit électronique LC série du générateur 
                                    d'hydrogène par électrolyse de l'eau de Stanley Meyer.
                                </td>
                            </tr>
                            <tr>
                                <td>
                                    5
                                </td>
                                <td>
                                    Démontrer mathématiquement la charge électrique aux bornes du condensateur 
                                    électrique plan du circuit électronique LC série du générateur d'hydrogène par 
                                    électrolyse de l'eau de Stanley Meyer en régime sinusoïdal sans partie négative 
                                    pouvant faire intervenir des termes en nombre complexe en fonction du temps et à 
                                    la fréquence de résonance du circuit électronique LC série du générateur 
                                    d'hydrogène par électrolyse de l'eau de Stanley Meyer.
                                </td>
                            </tr>
                            <tr>
                                <td>
                                    6
                                </td>
                                <td>
                                    Démontrer mathématiquement la quantité de matière d'électrons aux bornes du 
                                    condensateur électrique plan du circuit électronique LC série du générateur 
                                    d'hydrogène par électrolyse de l'eau de Stanley Meyer en régime sinusoïdal 
                                    sans partie négative pouvant faire intervenir des termes en nombre complexe en 
                                    fonction du temps et à la fréquence de résonance du circuit électronique LC série 
                                    du générateur d'hydrogène par électrolyse de l'eau de Stanley Meyer.
                                </td>
                            </tr>
                            <tr>
                                <td>
                                    7
                                </td>
                                <td>
                                    Démontrer mathématiquement la quantité de matière de dihydrogène produite 
                                    aux bornes du condensateur électrique plan du circuit électronique LC série du 
                                    générateur d'hydrogène par électrolyse de l'eau de Stanley Meyer en régime 
                                    sinusoïdal sans partie négative pouvant faire intervenir des termes en nombre 
                                    complexe en fonction du temps et à la fréquence de résonance du circuit 
                                    électronique LC série du générateur d'hydrogène par électrolyse de l'eau de Stanley 
                                    Meyer.
                                </td>
                            </tr>
                            <tr>
                                <td>
                                    8
                                </td>
                                <td>
                                    Démontrer mathématiquement la quantité d'énergie embarquée dans la quantité de 
                                    matière de dihydrogène produite aux bornes du condensateur électrique plan du 
                                    circuit électronique LC série du générateur d'hydrogène par électrolyse de l'eau 
                                    de Stanley Meyer en régime sinusoïdal sans partie négative pouvant faire 
                                    intervenir des termes en nombre complexe en fonction du temps et à la fréquence de 
                                    résonance du circuit électronique LC série du générateur d'hydrogène par 
                                    électrolyse de l'eau de Stanley Meyer.
                                </td>
                            </tr>
                            <tr>
                                <td>
                                    9
                                </td>
                                <td>
                                    Démontrer mathématiquement le rendement énergétique du générateur d'hydrogène 
                                    par électrolyse de l'eau de Stanley Meyer en régime sinusoïdal sans partie 
                                    négative pouvant faire intervenir des termes en nombre complexe en fonction du 
                                    temps et à la fréquence de résonance du circuit électronique LC série du générateur 
                                    d'hydrogène par électrolyse de l'eau de Stanley Meyer.
                                </td>
                            </tr>
                            <tr>
                                <td>
                                    10
                                </td>
                                <td>
                                    Démontrer mathématiquement la température de fonctionnement du générateur 
                                    d'hydrogène par électrolyse de l'eau de Stanley Meyer en régime sinusoïdal 
                                    sans partie négative pouvant faire intervenir des termes en nombre complexe en 
                                    fonction du temps et à la fréquence de résonance du circuit électronique LC série 
                                    du générateur d'hydrogène par électrolyse de l'eau de Stanley Meyer.
                                </td>
                            </tr>
                            <tr>
                                <td>
                                    11
                                </td>
                                <td>
                                    Démontrer mathématiquement la pression de fonctionnement du générateur d'hydrogène 
                                    par électrolyse de l'eau de Stanley Meyer en régime sinusoïdal sans partie 
                                    négative pouvant faire intervenir des termes en nombre complexe en fonction du 
                                    temps et à la fréquence de résonance du circuit électronique LC série du générateur 
                                    d'hydrogène par électrolyse de l'eau de Stanley Meyer.
                                </td>
                            </tr>
                            <tr>
                                <td>
                                    12
                                </td>
                                <td>
                                    Calculer expérimentalement le rendement énergétique du générateur d'hydrogène 
                                    par électrolyse de l'eau de Stanley Meyer en régime sinusoïdal sans partie 
                                    négative et à la fréquence de résonance du circuit électronique LC série du 
                                    générateur d'hydrogène par électrolyse de l'eau de Stanley Meyer avec une 
                                    tension électrique d'entrée égale à 230 volts et à 50/60 Hz en utilisant un 
                                    seul condensateur plan.
                                </td>
                            </tr>
                            <tr>
                                <td>
                                    13
                                </td>
                                <td>
                                    Calculer expérimentalement le rendement énergétique du générateur d'hydrogène par 
                                    électrolyse de l'eau de Stanley Meyer en régime sinusoïdal sans partie négative 
                                    et à la fréquence de résonance du circuit électronique LC série du générateur 
                                    d'hydrogène par électrolyse de l'eau de Stanley Meyer avec une tension électrique 
                                    d'entrée égale à 230 volts et à 50/60 Hz en utilisant deux condensateurs plan en 
                                    dérivation.
                                </td>
                            </tr>
                            <tr>
                                <td>
                                    14
                                </td>
                                <td>
                                    Calculer expérimentalement le rendement énergétique du générateur d'hydrogène par 
                                    électrolyse de l'eau de Stanley Meyer en régime sinusoïdal sans partie négative et 
                                    à la fréquence de résonance du circuit électronique LC série du générateur 
                                    d'hydrogène par électrolyse de l'eau de Stanley Meyer avec une tension électrique 
                                    d'entrée égale à 230 volts et à 50/60 Hz en utilisant quatre condensateurs plan en 
                                    dérivation.
                                </td>
                            </tr>
                            <tr>
                                <td>
                                    15
                                </td>
                                <td>
                                    Calculer expérimentalement le rendement énergétique du générateur d'hydrogène par 
                                    électrolyse de l'eau de Stanley Meyer en régime sinusoïdal sans partie négative et 
                                    à la fréquence de résonance du circuit électronique LC série du générateur 
                                    d'hydrogène par électrolyse de l'eau de Stanley Meyer avec une tension électrique 
                                    d'entrée égale à 230 volts et à 50/60 Hz en utilisant huit condensateurs plan en 
                                    dérivation.
                                </td>
                            </tr>
                            <tr>
                                <td>
                                    16
                                </td>
                                <td>
                                    Calculer expérimentalement le rendement énergétique du générateur d'hydrogène par 
                                    électrolyse de l'eau de Stanley Meyer en régime sinusoïdal sans partie négative et 
                                    à la fréquence de résonance du circuit électronique LC série du générateur 
                                    d'hydrogène par électrolyse de l'eau de Stanley Meyer avec une tension électrique 
                                    d'entrée égale à 230 volts et à 50/60 Hz en utilisant seize condensateurs plan en 
                                    dérivation.
                                </td>
                            </tr>
                            <tr>
                                <td>
                                    17
                                </td>
                                <td>
                                    Calculer expérimentalement le rendement énergétique du générateur d'hydrogène par 
                                    électrolyse de l'eau de Stanley Meyer en régime sinusoïdal sans partie négative et 
                                    à la fréquence de résonance du circuit électronique LC série du générateur 
                                    d'hydrogène par électrolyse de l'eau de Stanley Meyer avec une tension électrique 
                                    d'entrée égale à 230 volts et à 50/60 Hz en utilisant trente-deux condensateurs 
                                    plan en dérivation.
                                </td>
                            </tr>
                            <tr>
                                <td>
                                    18
                                </td>
                                <td>
                                    Rédiger un rapport scientifique écrit dans la langue française et la langue 
                                    anglaise pour lister les résultats de chaque tâche confirmés au nom de votre 
                                    laboratoire.
                                </td>
                            </tr>
                            <tr>
                                <td>
                                    19
                                </td>
                                <td>
                                    Diffuser le rapport scientifique en ligne et accessible au public gratuitement sur 
                                    un site internet dédié pour le monde de l'énergie voire le monde de l'hydrogène.
                                </td>
                            </tr>
                        </tbody>
                    </table>
                  </div>
                </div>

                <br>

                <div class="card text-center">
                  <div class="card-header">
                    Documentations
                  </div>
                  <div class="card-body">
                      <div class="list-group text-center">
                        <a href="https://patents.google.com/patent/US5149407A/en" 
                        class="list-group-item list-group-item-action">
                          Procédés et appareils pour la production de gaz combustible et la libération accrue de 
                          énergie thermique provenant de ce gaz - US5149407A
                        </a>
                        <a href="https://patents.google.com/patent/US4936961A/en?oq=4_936_961" 
                        class="list-group-item list-group-item-action">
                            Procédé de production d’un gaz combustible - US4936961A
                        </a>
                        <a href="https://patents.google.com/patent/US4798661A/en?oq=US_4_798_661" 
                        class="list-group-item list-group-item-action">
                            Circuit de contrôle de tension du générateur de gaz - US4798661A
                        </a>
                        <a href="https://patents.google.com/patent/CA1234773A/en" 
                        class="list-group-item list-group-item-action">
                            Générateur d’hydrogène à cavité résonnante qui fonctionne avec une tension pulsée 
                            potentiel électrique - CA1234773A
                        </a>
                        <a href="https://patents.google.com/patent/CA1234774A/en" 
                        class="list-group-item list-group-item-action">
                            Système générateur d’hydrogène - CA1234774A
                        </a>
                        <a href="https://patents.google.com/patent/WO1992007861A1/en?oq=4_936_961" 
                        class="list-group-item list-group-item-action">
                            Circuits de commande et de commande pour une pile produisant de l’hydrogène gazeux - 
                            WO1992007861A1
                        </a>
                        <a href="https://patents.google.com/patent/US4124463A/en?oq=US4124463" 
                        class="list-group-item list-group-item-action">
                            Cellule électrolytique - US4124463A
                        </a>
                        <a 
                        href="https://github.com/Jay4C/Holomorphe_Company/blob/main/Research_and_development/Fundamental-research-of-the-us-patent-us4936961a-part-2.pdf" 
                        class="list-group-item list-group-item-action">
                            Recherche fondamentale pour le générateur d'hydrogène par électrolyse de l'eau de Stanley 
                            Meyer issu du brevet US4936961A
                        </a>
                        <a href="https://github.com/Jay4C/Holomorphe_Company/blob/main/Research_and_development/Electronic_circuit_diagram_of_stanley_meyer_water_electrolyser.pdf" 
                        class="list-group-item list-group-item-action">
                            Schéma du circuit électronique du générateur d'hydrogène par électrolyse de l'eau de 
                            Stanley Meyer issu du brevet US5149407
                        </a>
                        <a href="https://github.com/Jay4C/Holomorphe_Company/blob/main/Research_and_development/Stanley_meyer_patents.pdf" 
                        class="list-group-item list-group-item-action">
                            À propos de Stanley Meyer
                        </a>
                        <a href="https://github.com/Jay4C/Holomorphe_Company/blob/main/Research_and_development/Theories_to_know_about_stanley_meyer_water_electrolyser.pdf" 
                        class="list-group-item list-group-item-action">
                            Quelques théories à connaître sur le générateur d'hydrogène par électrolyse de l'eau de 
                            Stanley Meyer
                        </a>
                        <a href="https://github.com/Jay4C/Holomorphe_Company/blob/main/Research_and_development/Hydrogen_generator.pdf" 
                        class="list-group-item list-group-item-action">
                            Générateur d’hydrogène par électrolyse de l'eau de la société Holomorphe
                        </a>
                        <a href="https://github.com/Jay4C/Holomorphe_Company" 
                        class="list-group-item list-group-item-action">
                            Société Holomorphe
                        </a>
                      </div>
                  </div>
                </div>

              </div>

              <br>

            </div>

            <br>

            <!-- Option 1: Bootstrap Bundle with Popper -->
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/js/bootstrap.bundle.min.js" 
            integrity="sha384-b5kHyXgcpbZJO/tY9Ul7kGkf1S0CWuKcCD38l8YkeH8z8QjE0GmW1gYU5S9FOnJ0" 
            crossorigin="anonymous"></script>
          </body>
        </html>
        """

        options = {
            'page-size': 'A4',
            'header-center': "Cahier des charges des travaux de mesures expérimentales du générateur d'hydrogène "
                             "par \n électrolyse de l'eau de Stanley Meyer",
            'footer-right': '[page] sur [topage]',
            'footer-left': 'S.A.S.U.A.C.V. Holomorphe [SIREN : 883632556]'
        }

        path_wkthmltopdf = "C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe"
        config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
        pdfkit.from_string(body,
                           "Recherches\\Cahier_Charges_Travaux_Mesures_Experimentales_[SASUACV_Holomorphe].pdf",
                           configuration=config,
                           options=options)


if __name__ == '__main__':
    unittest.main()
