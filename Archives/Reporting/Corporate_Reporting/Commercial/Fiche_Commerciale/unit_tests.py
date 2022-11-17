import unittest
import pdfkit


class Fiche_Commerciale_Holomorphe(unittest.TestCase):
    # ok
    def test_fiche_commerciale_digitalisation_programme_immobilier_v1(self):
        print("test_fiche_commerciale")

        body = """
        <!doctype html>
        <html lang="en">
          <head>
            <!-- Required meta tags -->
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
        
            <!-- Bootstrap CSS -->
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/css/bootstrap.min.css" 
            rel="stylesheet" integrity="sha384-BmbxuPwQa2lc/FVzBcNJ7UAyJxM6wuqIj61tLrc4wSX0szH/Ev+nYRRuWlolflfl" crossorigin="anonymous">
        
            <title>Fiche commerciale pour l'édition de logiciels applicatifs</title>
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
                      <li class="list-group-item">Dénomination sociale : S.A.S.U. à capital variable HOLOMORPHE / Capital social : 100 euros</li>
                      <li class="list-group-item">Adresse du siège social : 31 Avenue de Ségur - ABC LIV Ségur - 75007 Paris / Siret : 88363255600014</li>
                      <li class="list-group-item">Registre du commerce et des sociétés : R.C.S. PARIS - Greffe du Tribunal de Commerce de PARIS</li>
                      <li class="list-group-item">Activités : Commerce de gros de produits chimiques - Edition de logiciels applicatifs / Code NAF : 4675Z</li>
                      <li class="list-group-item">Numero TVA intracommunataire : FR06883632556 / Président : Monsieur  / Date d'immatriculation : 26 Mai 2020</li>
                    </ul>
                  </div>
                </div>
                
                <br>
                
                <div class="card text-center">
                  <div class="card-header">
                    Services proposés pour la digitalisation des programmes immobiliers
                  </div>
                  <div class="card-body">
                    <ul class="list-group"> 
                      <li class="list-group-item">Automatisation de la saisie des caractères d'un clavier / Automatisation du déplacement d'une souris</li>
                      <li class="list-group-item">Automatisation d'un parcours utilisateur sur une interface graphique d'un logiciel bureautique ou d'un navigateur web</li>
                      <li class="list-group-item">Exploration de données / Dématérialisation de formulaires administratives / Prospection commerciale des terrains constructibles</li>
                      <li class="list-group-item">Recherche de financements auprès des établissements financiers / Commercialisation des programmes immobiliers</li>
                      <li class="list-group-item">Conception de catalogues de plans de construction en 2D et 3D avec la technologie BIM / Obtention des autorisations administratives</li>
                      <li class="list-group-item">Gestion de projets des travaux et des démolitions coordonnée avec les différents intervenants du programme immobilier</li>
                      <li class="list-group-item">Accompagnement des gouvernements, des notaires, des pouvoirs publics pour le cadastre, les démarches administratives, les travaux publics et la sécurisation du stockage des données</li>
                      <li class="list-group-item">Robotisation des travaux de construction et démolition du programme immobilier / Trading algorithmique</li>
                    </ul>
                  </div>
                </div>

                <br>
                
                <div class="card text-center">
                  <div class="card-header">
                    Tarif journalier moyen
                  </div>
                  <div class="card-body">
                    888 € H.T.
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
                                <th scope="col">Nationalit&eacute;</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>
                                    Monsieur 
                                </td>
                                <td>
                                    31 Avenue de Ségur 75007 Paris
                                </td>
                                <td>07.49.16.33.29</td>
                                <td>jason.aloyau@holomorphe.com</td>
                                <td>Française</td>
                            </tr>
                        </tbody>
                    </table>
                  </div>
                </div>
                
                <br>
                
                <div class="card text-center">
                  <div class="card-header">
                    Partenaire
                  </div>
                  <div class="card-body">
                    <ul class="list-group">
                      <li class="list-group-item">Société Pass-Tech Pass Technologie SARL</li>
                    </ul>
                  </div>
                </div>
                
                <br>
                <br>
                <br>
                <br>
                
                <div class="card text-center">
                  <div class="card-header">
                    Lexique
                  </div>
                  <div class="card-body">
                    <!-- Automatisation robotisée des processus -->
                    <div class="card text-center">
                      <div class="card-header">
                        Automatisation robotisée des processus
                      </div>
                      <div class="card-body">
                        L'automatisation robotisée des processus (en anglais robotic process automation ou RPA) est 
                        <br>
                        une technologie de création de robots par apprentissage du comportement d'un usager sur une interface graphique.
                      </div>
                    </div>
                    <!-- Automatisation robotisée des processus -->
                    
                    <br>
                    
                    <!-- Exploration de données -->
                    <div class="card text-center">
                      <div class="card-header">
                        Exploration de données
                      </div>
                      <div class="card-body">
                        L’exploration de données, connue aussi sous l'expression de fouille de données, 
                        <br>
                        forage de données, prospection de données, data mining, ou encore extraction de connaissances 
                        <br>
                        à partir de données, a pour objet l’extraction d'un savoir ou d'une connaissance à partir de 
                        <br>
                        grandes quantités de données, par des méthodes automatiques ou semi-automatiques.
                      </div>
                    </div>
                    <!-- Exploration de données -->
                    
                    <br>
                    
                    <!-- Dématérialisation -->
                    <div class="card text-center">
                      <div class="card-header">
                        Dématérialisation
                      </div>
                      <div class="card-body">
                        La dématérialisation est le remplacement dans une entreprise ou une organisation de ses 
                        <br>
                        supports d'informations matériels (souvent en papier) par des fichiers informatiques et des ordinateurs.
                      </div>
                    </div>
                    <!-- Dématérialisation -->
                    
                    <br>
                    
                    <!-- Technologie BIM -->
                    <div class="card text-center">
                      <div class="card-header">
                        Technologie BIM
                      </div>
                      <div class="card-body">
                        BIM est le sigle anglais de Building Information Modeling, de Building Information Model, 
                        <br>
                        ou encore de Building Information Management, et le rétroacronyme de bâti immobilier modélisé. 
                        <br>
                        Il désigne les outils de modélisation des informations de la construction implémentés par des 
                        <br>
                        applications qui permettent la modélisation des données du bâtiment, d'une structure, d'un édifice ou d'un ouvrage.
                      </div>
                    </div>
                    <!-- Technologie BIM -->
                    
                    <br>
                    
                    <!-- Robotique industrielle -->
                    <div class="card text-center">
                      <div class="card-header">
                        Robotique industrielle
                      </div>
                      <div class="card-body">
                        La robotique industrielle est officiellement définie par l'Organisation Internationale 
                        <br>
                        de Normalisation (ISO) comme étant un système commandé automatiquement, multi-applicatif, 
                        <br>
                        reprogrammable, polyvalent, manipulateur et programmable sur trois axes ou plus.
                      </div>
                    </div>
                    <!-- Robotique industrielle -->
                    
                    <br>
                    
                    <!-- Trading algorithmique -->
                    <div class="card text-center">
                      <div class="card-header">
                        Trading algorithmique
                      </div>
                      <div class="card-body">
                        Le trading algorithmique, aussi appelé trading automatisé ou trading automatique, 
                        <br>
                        boîte noire de négociation (en anglais : black-box trading), effectué par des robots de 
                        <br>
                        trading ou robots traders est une forme de trading avec utilisation de plates-formes 
                        <br>
                        électroniques pour la saisie des ordres de bourse en laissant un algorithme décider des 
                        <br>
                        différents aspects de l'ordre, tel que l'instant d'ouverture ou de clôture (le timing), 
                        <br>
                        le prix ou le volume de l'ordre et ceci, dans de nombreux cas, sans la moindre intervention humaine.
                      </div>
                    </div>
                    <!-- Trading algorithmique -->
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
            'header-center': "Fiche commerciale pour la digitalisation des programmes immobiliers",
            'footer-right': '[page] sur [topage]',
            'footer-left': 'Société Holomorphe [SIREN : 883632556]'
        }

        path_wkthmltopdf = "C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe"
        config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
        pdfkit.from_string(body, "Fiche_Commerciale\\Fiche_Commerciale_[Societe_Holomorphe].pdf", configuration=config,
                           options=options)

    # ok
    def test_fiche_commerciale_digitalisation_programme_immobilier_v2(self):
        print("test_fiche_commerciale_digitalisation_programme_immobilier_v2")

        body = """
        <!doctype html>
        <html lang="en">
          <head>
            <!-- Required meta tags -->
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">

            <!-- Bootstrap CSS -->
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/css/bootstrap.min.css" 
            rel="stylesheet" integrity="sha384-BmbxuPwQa2lc/FVzBcNJ7UAyJxM6wuqIj61tLrc4wSX0szH/Ev+nYRRuWlolflfl" 
            crossorigin="anonymous">

            <title>Fiche commerciale pour l'édition de logiciels applicatifs</title>
          </head>
          <body>
            <div class="container">
                <!-- Informations générales de la société Holomorphe -->
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
                <!-- Informations générales de la société Holomorphe -->

                <br>

                <!-- Contact -->
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
                                <th scope="col">Nationalit&eacute;</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>
                                    Monsieur 
                                </td>
                                <td>
                                    31 Avenue de Ségur 75007 Paris
                                </td>
                                <td>07.49.16.33.29</td>
                                <td>jason.aloyau@holomorphe.com</td>
                                <td>Française</td>
                            </tr>
                        </tbody>
                    </table>
                  </div>
                </div>
                <!-- Contact -->

                <br>

                <!-- Prestations -->
                <div class="card text-center">
                  <div class="card-header">
                    Prestations de services d'édition de logiciels applicatifs pour la digitalisation des programmes 
                    immobiliers
                  </div>
                  <div class="card-body">
                    <ul class="list-group">
                      <li class="list-group-item">
                        Assurer la prospection commerciale des terrains constructibles
                      </li>
                      <li class="list-group-item">
                        Assurer la dématérialisation de formulaires administratives pour accomplir des démarches 
                        administratives
                      </li>
                      <li class="list-group-item">
                        Assurer la recherche des financements auprès des établissements financiers
                      </li>
                      <li class="list-group-item">
                        Assurer les demandes d'obtention des autorisations administratives
                      </li>
                      <li class="list-group-item">
                        Assurer la commercialisation des programmes immobiliers
                      </li>
                      <li class="list-group-item">
                        Automatiser un parcours utilisateur avec une fenêtre ouvrante d'un navigateur web en perdant 
                        la main sur l'ordinateur afin d'éviter de perturber le robot.
                      </li>
                      <li class="list-group-item">
                        Automatiser un parcours utilisateur avec une fenêtre ouvrante d'un logiciel bureautique en 
                        perdant la main sur l'ordinateur afin d'éviter de perturber le robot.
                      </li>
                      <li class="list-group-item">
                        Automatiser un parcours utilisateur avec une fenêtre fantôme d'un navigateur web en gardant 
                        la main sur l'ordinateur sans perturber le robot.
                      </li>
                      <li class="list-group-item">
                        Automatiser des collectes de données depuis une fenêtre fantôme d'un navigateur web en 
                        gardant la main sur l'ordinateur sans perturber le robot.
                      </li>
                      <li class="list-group-item">
                        Automatiser des traitements de données.
                      </li>
                      <li class="list-group-item">
                        Automatiser des générations de rapports.
                      </li>
                      <li class="list-group-item">
                        Automatiser des placements financiers sur les marchés financiers
                      </li>
                      <li class="list-group-item">
                        Accompagner des gouvernements, des notaires, des pouvoirs publics pour le cadastre, 
                        les démarches administratives, les travaux publics et la sécurisation du stockage des données
                      </li>
                      <li class="list-group-item">
                        Assurer la conception de catalogues de plans de construction en 2D et 3D avec la technologie 
                        BIM
                      </li>
                      <li class="list-group-item">
                        Assurer la gestion de projets des travaux et des démolitions coordonnée avec les différents 
                        intervenants du programme immobilier
                      </li>
                      <li class="list-group-item">
                        Assurer les travaux de construction et démolition des programmes immobiliers
                      </li>
                    </ul>
                  </div>
                </div>
                <!-- Prestations -->

                <br>

                <!-- Tarif -->
                <div class="card text-center">
                  <div class="card-header">
                    Tarif journalier moyen
                  </div>
                  <div class="card-body">
                    Le tarif journalier moyen est égal à 200 euros hors taxes pour des prestations de services 
                    d'édition de logiciels applicatifs pour la digitalisation des programmes immobiliers en télétravail 
                    uniquement.
                  </div>
                </div>
                <!-- Tarif -->

                <br>

                <!-- Lexique -->
                <div class="card text-center">
                  <div class="card-header">
                    Lexique
                  </div>
                  <div class="card-body">
                    <!-- Fenêtre fantôme -->
                    <div class="card text-center">
                      <div class="card-header">
                        Fenêtre fantôme
                      </div>
                      <div class="card-body">
                        Une fenêtre fantôme est une fenêtre d'un navigateur web ouverte par un robot d'automatisation 
                        qui s'ouvre dans un processus de l'ordinateur de manière totalement virtuel sans déranger 
                        l'utilisateur humain tout en laissant au robot d'exécuter des saisies de caractères et des 
                        déplacements de la souris.
                      </div>
                    </div>
                    <!-- Fenêtre fantôme -->

                    <br>

                    <!-- Automatisation robotisée des processus -->
                    <div class="card text-center">
                      <div class="card-header">
                        Automatisation robotisée des processus
                      </div>
                      <div class="card-body">
                        L'automatisation robotisée des processus (en anglais robotic process automation ou RPA) est 
                        une technologie de création de robots par apprentissage du comportement d'un usager sur une 
                        interface graphique.

                        <br>
                        <br>

                        <a class="btn btn-outline-secondary" 
                        href="https://fr.wikipedia.org/wiki/Automatisation_robotisée_des_processus" 
                        role="button" target="_blank">
                        Automatisation robotisée des processus
                        </a>
                      </div>
                    </div>
                    <!-- Automatisation robotisée des processus -->

                    <br>

                    <!-- Exploration de données -->
                    <div class="card text-center">
                      <div class="card-header">
                        Exploration de données
                      </div>
                      <div class="card-body">
                        L’exploration de données, connue aussi sous l'expression de fouille de données, 
                        forage de données, prospection de données, data mining, ou encore extraction de connaissances 
                        à partir de données, a pour objet l’extraction d'un savoir ou d'une connaissance à partir de 
                        grandes quantités de données, par des méthodes automatiques ou semi-automatiques.

                        <br>
                        <br>

                        <a class="btn btn-outline-secondary" 
                        href="https://fr.wikipedia.org/wiki/Exploration_de_données" 
                        role="button" 
                        target="_blank">
                        Exploration de données
                        </a>
                      </div>
                    </div>
                    <!-- Exploration de données -->

                    <br>

                    <!-- Dématérialisation -->
                    <div class="card text-center">
                      <div class="card-header">
                        Dématérialisation
                      </div>
                      <div class="card-body">
                        La dématérialisation est le remplacement dans une entreprise ou une organisation de ses 
                        supports d'informations matériels (souvent en papier) par des fichiers informatiques et des 
                        ordinateurs.

                        <br>
                        <br>

                        <a class="btn btn-outline-secondary" 
                        href="https://fr.wikipedia.org/wiki/Dématérialisation" 
                        role="button"
                        target="_blank">
                        Dématérialisation
                        </a>
                      </div>
                    </div>
                    <!-- Dématérialisation -->
                  </div>
                </div>
                <!-- Lexique -->

                <br>

                <!-- Liens utiles -->
                <div class="card text-center">
                  <div class="card-header">
                    Liens utiles
                  </div>
                  <div class="card-body">
                    <div class="list-group text-center">
                        <a class="list-group-item list-group-item-action" 
                        href="https://www.malt.fr/profile/jasonaloyau">
                            Profil Malt de Monsieur 
                        </a>
                        <a class="list-group-item list-group-item-action" 
                        href="https://holomorphe.com/application-software-editions/">
                            Site internet de la société Holomorphe
                        </a>
                        <a class="list-group-item list-group-item-action" 
                        href="https://www.societe.com/societe/holomorphe-883632556.html">
                            Informations générales de la société Holomorphe disponible sur Societe.com
                        </a>
                        <a class="list-group-item list-group-item-action" 
                        href="https://holomorphe.com/contents/resume_of_mr_jason_aloyau">
                            Curriculum vitae de Monsieur 
                        </a>
                        <a class="list-group-item list-group-item-action" 
                        href="https://www.youtube.com/channel/UClK7qVMGyLGEE0uPy7LFGlA">
                            Compte YouTube de la société Holomorphe
                        </a>
                        <a class="list-group-item list-group-item-action" 
                        href="https://github.com/Jay4C/Web-Automation">
                            Compte GitHub de Monsieur  / Web Automation / RPA
                        </a>
                    </div>
                  </div>
                </div>
                <!-- Liens utiles -->

                <br>

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
            'header-center': "Fiche commerciale pour la digitalisation des programmes immobiliers",
            'footer-right': '[page] sur [topage]',
            'footer-left': 'Société Holomorphe [SIREN : 883632556]'
        }

        path_wkthmltopdf = "C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe"

        config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)

        pdfkit.from_string(body,
                           "Fiche_Commerciale\\Fiche_Commerciale_DPI_[Societe_Holomorphe].pdf",
                           configuration=config,
                           options=options)

    # ok
    def test_fiche_commerciale_rpa_v1(self):
        print("test_fiche_commerciale_rpa_v1")

        body = """
        <!doctype html>
        <html lang="en">
          <head>
            <!-- Required meta tags -->
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">

            <!-- Bootstrap CSS -->
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/css/bootstrap.min.css" 
            rel="stylesheet" integrity="sha384-BmbxuPwQa2lc/FVzBcNJ7UAyJxM6wuqIj61tLrc4wSX0szH/Ev+nYRRuWlolflfl" 
            crossorigin="anonymous">

            <title>Fiche commerciale pour l'édition de logiciels applicatifs</title>
          </head>
          <body>
            <div class="container">

                <br>
                
                <!-- Prestations -->
                <div class="card text-center">
                  <div class="card-header">
                    Prestations de services d'édition de logiciels applicatifs pour l'automatisation des processus 
                    robotisés
                  </div>
                  <div class="card-body">
                    <ul class="list-group"> 
                      <li class="list-group-item">
                        Automatiser un parcours utilisateur avec une fenêtre ouvrante d'un navigateur web en perdant 
                        la main sur l'ordinateur afin d'éviter de perturber le robot
                      </li>
                      <li class="list-group-item">
                        Automatiser un parcours utilisateur avec une fenêtre ouvrante d'un logiciel bureautique en 
                        perdant la main sur l'ordinateur afin d'éviter de perturber le robot
                      </li>
                      <li class="list-group-item">
                        Automatiser un parcours utilisateur avec une fenêtre fantôme d'un navigateur web en gardant 
                        la main sur l'ordinateur sans perturber le robot
                      </li>
                      <li class="list-group-item">
                        Automatiser des collectes de données depuis une fenêtre fantôme d'un navigateur web en 
                        gardant la main sur l'ordinateur sans perturber le robot
                      </li>
                      <li class="list-group-item">
                        Automatiser des traitements de données
                      </li>
                      <li class="list-group-item">
                        Automatiser des générations de rapports
                      </li>
                    </ul>
                  </div>
                </div>
                <!-- Prestations -->

                <br>
                
                <!-- Tarif -->
                <div class="card text-center">
                  <div class="card-header">
                    Tarif journalier moyen
                  </div>
                  <div class="card-body">
                    200 € H.T. par jour pour des prestations de services d'édition de logiciels applicatifs pour 
                    l'automatisation des processus robotisés
                  </div>
                </div>
                <!-- Tarif -->
                                
                <br>
                
                <!-- Lexique -->
                <div class="card text-center">
                  <div class="card-header">
                    Lexique
                  </div>
                  <div class="card-body">
                    <!-- Fenêtre fantôme -->
                    <div class="card text-center">
                      <div class="card-header">
                        Fenêtre fantôme
                      </div>
                      <div class="card-body">
                        Une fenêtre fantôme est une fenêtre d'un navigateur web ouverte par un robot d'automatisation 
                        qui s'ouvre dans un processus de l'ordinateur de manière totalement virtuel sans déranger 
                        l'utilisateur humain tout en laissant au robot d'exécuter des saisies de caractères et des 
                        déplacements de la souris.
                      </div>
                    </div>
                    <!-- Fenêtre fantôme -->
                    
                    <br>
                    
                    <!-- Automatisation robotisée des processus -->
                    <div class="card text-center">
                      <div class="card-header">
                        Automatisation robotisée des processus
                      </div>
                      <div class="card-body">
                        L'automatisation robotisée des processus (en anglais robotic process automation ou RPA) est 
                        une technologie de création de robots par apprentissage du comportement d'un usager sur une 
                        interface graphique.
                        
                        <br>
                        <br>
                        
                        <a class="btn btn-outline-secondary" 
                        href="https://fr.wikipedia.org/wiki/Automatisation_robotisée_des_processus" 
                        role="button" target="_blank">
                        Automatisation robotisée des processus
                        </a>
                      </div>
                    </div>
                    <!-- Automatisation robotisée des processus -->

                    <br>

                    <!-- Exploration de données -->
                    <div class="card text-center">
                      <div class="card-header">
                        Exploration de données
                      </div>
                      <div class="card-body">
                        L’exploration de données, connue aussi sous l'expression de fouille de données, 
                        forage de données, prospection de données, data mining, ou encore extraction de connaissances 
                        à partir de données, a pour objet l’extraction d'un savoir ou d'une connaissance à partir de 
                        grandes quantités de données, par des méthodes automatiques ou semi-automatiques.
                        
                        <br>
                        <br>
                        
                        <a class="btn btn-outline-secondary" 
                        href="https://fr.wikipedia.org/wiki/Exploration_de_données" 
                        role="button" 
                        target="_blank">
                        Exploration de données
                        </a>
                      </div>
                    </div>
                    <!-- Exploration de données -->

                    <br>

                    <!-- Dématérialisation -->
                    <div class="card text-center">
                      <div class="card-header">
                        Dématérialisation
                      </div>
                      <div class="card-body">
                        La dématérialisation est le remplacement dans une entreprise ou une organisation de ses 
                        supports d'informations matériels (souvent en papier) par des fichiers informatiques et des 
                        ordinateurs.
                        
                        <br>
                        <br>
                        
                        <a class="btn btn-outline-secondary" 
                        href="https://fr.wikipedia.org/wiki/Dématérialisation" 
                        role="button"
                        target="_blank">
                        Dématérialisation
                        </a>
                      </div>
                    </div>
                    <!-- Dématérialisation -->
                  </div>
                </div>
                <!-- Lexique -->
                
                <br>
                
                <!-- Liens utiles -->
                <div class="card text-center">
                  <div class="card-header">
                    Liens utiles
                  </div>
                  <div class="card-body">
                    <div class="list-group text-center">
                        <a class="list-group-item list-group-item-action" 
                        href="https://www.malt.fr/profile/jasonaloyau">
                            Profil Malt de Monsieur 
                        </a>
                        <a class="list-group-item list-group-item-action" 
                        href="https://holomorphe.com/">
                            Site internet de la société Holomorphe
                        </a>
                        <a class="list-group-item list-group-item-action" 
                        href="https://www.societe.com/societe/holomorphe-883632556.html">
                            Informations générales de la société Holomorphe disponible sur Societe.com
                        </a>
                        <a class="list-group-item list-group-item-action" 
                        href="https://holomorphe.com/contents/resume_of_mr_jason_aloyau">
                            Curriculum vitae de Monsieur 
                        </a>
                        <a class="list-group-item list-group-item-action" 
                        href="https://www.youtube.com/channel/UClK7qVMGyLGEE0uPy7LFGlA">
                            Compte YouTube de la société Holomorphe
                        </a>
                        <a class="list-group-item list-group-item-action" 
                        href="https://github.com/Jay4C/Web-Automation">
                            Compte GitHub de Monsieur  / Web Automation / RPA
                        </a>
                    </div>
                  </div>
                </div>
                <!-- Liens utiles -->
                
                <br>
                
                <!-- Informations générales de la société Holomorphe -->
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
                <!-- Informations générales de la société Holomorphe -->
                
                <br>
                
                <!-- Contact -->
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
                                <th scope="col">Nationalit&eacute;</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>
                                    Monsieur 
                                </td>
                                <td>
                                    31 Avenue de Ségur 75007 Paris
                                </td>
                                <td>07.49.16.33.29</td>
                                <td>jason.aloyau@holomorphe.com</td>
                                <td>Française</td>
                            </tr>
                        </tbody>
                    </table>
                  </div>
                </div>
                <!-- Contact -->
                
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
            'header-center': "Fiche commerciale pour l'automatisation des processus robotisés",
            'footer-right': '[page] sur [topage]',
            'footer-left': 'Société Holomorphe [SIREN : 883632556]'
        }

        path_wkthmltopdf = "C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe"

        config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)

        pdfkit.from_string(body,
                           "Fiche_Commerciale\\Fiche_Commerciale_RPA_[Societe_Holomorphe].pdf",
                           configuration=config,
                           options=options)

    # ok
    def test_tableau_comparaison_electrolyseurs_a_eau(self):
        print("test_tableau_comparaison_electrolyseurs_a_eau")

        body = """
        <!doctype html>
        <html lang="en">
          <head>
            <!-- Required meta tags -->
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">

            <!-- Bootstrap CSS -->
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/css/bootstrap.min.css" 
            rel="stylesheet" integrity="sha384-BmbxuPwQa2lc/FVzBcNJ7UAyJxM6wuqIj61tLrc4wSX0szH/Ev+nYRRuWlolflfl" 
            crossorigin="anonymous">

            <title>Tableau comparatif des différents électrolyseurs à eau</title>
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
                      <li class="list-group-item">Dénomination sociale : S.A.S.U. à capital variable HOLOMORPHE / Capital social : 100 euros</li>
                      <li class="list-group-item">Adresse du siège social : 31 Avenue de Ségur - ABC LIV Ségur - 75007 Paris / Siret : 88363255600014</li>
                      <li class="list-group-item">Registre du commerce et des sociétés : R.C.S. PARIS - Greffe du Tribunal de Commerce de PARIS</li>
                      <li class="list-group-item">Activités : Commerce de gros de produits chimiques - Edition de logiciels applicatifs / Code NAF : 4675Z</li>
                      <li class="list-group-item">Numero TVA intracommunataire : FR06883632556 / Président : Monsieur  / Date d'immatriculation : 26 Mai 2020</li>
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
                                <th scope="col">E-mail</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>Monsieur </td>
                                <td>31 Avenue de Ségur 75007 Paris</td>
                                <td>07.49.16.33.29</td>
                                <td>jason.aloyau@holomorphe.com</td>
                            </tr>
                        </tbody>
                    </table>
                  </div>
                </div>
                
                <br>
                
                <div class="card text-center">
                  <div class="card-header">
                    Technologies de l'hydrogène utilisées par la société Holomorphe
                  </div>
                  <div class="card-body">
                    <div>
                        <a href="https://patents.google.com/patent/US5149407A/en" class="list-group-item list-group-item-action">
                          Processus et appareils de production d'hydrogène et de libération accrue d’énergie thermique à partir d'hydrogène - US 5,149,407 A
                        </a>
                        <a href="https://patents.google.com/patent/US4936961A/en?oq=4_936_961" class="list-group-item list-group-item-action">
                          Méthode de production d’hydrogène - US 4,936,961 A
                        </a>
                        <a href="https://patents.google.com/patent/US4798661A/en?oq=US_4_798_661" class="list-group-item list-group-item-action">
                          Circuit de contrôle de tension de générateur d'hydrogène - US 4,798,661 A
                        </a>
                        <a href="https://patents.google.com/patent/WO1992007861A1/en?oq=4_936_961" class="list-group-item list-group-item-action">
                          Un circuit de contrôle et de conduite pour une cellule productrice de gaz hydrogène - WO 1,992,007,861 A1
                        </a>
                        <a href="https://patents.google.com/patent/CA1234773A/en" class="list-group-item list-group-item-action">
                          Générateur d’hydrogène à cavité résonnante qui fonctionne avec un potentiel électrique à tension pulsée - CA 1,234,773 A
                        </a>
                        <a href="https://patents.google.com/patent/CA1234774A/en" class="list-group-item list-group-item-action">
                          Système générateur d’hydrogène - CA 1,234,774 A
                        </a>
                    </div>
                  </div>
                </div>

                <br>

                <div class="card text-center">
                  <div class="card-header">
                    Tableau comparatif des différents électrolyseurs à eau
                  </div>
                  <div class="card-body">
                    <table class="table">
                      <thead>
                        <tr>
                          <th scope="col">Nom</th>
                          <th scope="col">Consommation électrique par volume d'hydrogène produit théorique (kWh/Nm^3)</th>
                          <th scope="col">Puissance électrique nécessaire théorique (MW)</th>
                          <th scope="col">Surface d'installation théorique (m^2)</th>
                          <th scope="col">Matériaux utilisés</th>
                          <th scope="col">Température de fonctionnement théorique (°C)</th>
                          <th scope="col">Durée de vie théorique (h)</th>
                          <th scope="col">Débit théorique (m^3/h)</th>
                          <th scope="col">Ratio de débit par surface théorique (m^3/h)/m^2</th>
                          <th scope="col">Ratio de puissance par surface théorique (W/m^2)</th>
                          <th scope="col">Ratio de débit par puissance théorique (m^3/h)/W</th>
                          <th scope="col">Type d'électrolyte</th>
                          <th scope="col">Type d'eau</th>
                          <th scope="col">Rendement théorique (%)</th>
                        </tr>
                      </thead>
                      <tbody>
                        <tr>
                          <th scope="row">Electrolyseur alcalin</th>
                          <td>4,5</td>
                          <td>4</td>
                          <td>100</td>
                          <td>Anode (Ni, Co, Fe) / Cathode (Ni, C) / Séparatrice (Acier inoxydable)</td>
                          <td>90</td>
                          <td>80 000</td>
                          <td>800</td>
                          <td>8</td>
                          <td>40 000</td>
                          <td>0,0002</td>
                          <td>Soude (NaOH) – Liquide</td>
                          <td>Eau alcaline</td>
                          <td>77</td>
                        </tr>
                        <tr>
                          <th scope="row">Electrolyseur PEM</th>
                          <td>4,5</td>
                          <td>1</td>
                          <td>25</td>
                          <td>Anode (Platine) / Cathode (Iridium) / Séparatrice (Titane)</td>
                          <td>80</td>
                          <td>20 000</td>
                          <td>200</td>
                          <td>8</td>
                          <td>40 000</td>
                          <td>0,0002</td>
                          <td>Polymère solide</td>
                          <td>Eau pure</td>
                          <td>80</td>
                        </tr>
                        <tr>
                          <th scope="row">Electrolyseur SOEC</th>
                          <td>3,5</td>
                          <td>2,7</td>
                          <td>300</td>
                          <td>Anode (Ni+ZrO2) / Cathode (Nickel cofritté, Cobalt, Nickel de Cermet)</td>
                          <td>1000</td>
                          <td>100 000</td>
                          <td>750</td>
                          <td>2,5</td>
                          <td>9 000</td>
                          <td>0,00028</td>
                          <td>Electrolyte étanche au gaz</td>
                          <td>Vapeur</td>
                          <td>85</td>
                        </tr>
                        <tr>
                          <th scope="row">Electrolyseur de Stanley Meyer (Holomorphe - Conteneurisation Hydrog&egrave;ne)</th>
                          <td>0,00063</td>
                          <td>0,00004</td>
                          <td>13,85</td>
                          <td>Anode et cathode (acier inoxydable)</td>
                          <td>25</td>
                          <td>876 000</td>
                          <td>63,85</td>
                          <td>4,62</td>
                          <td>2,89</td>
                          <td>1,60</td>
                          <td>Aucun</td>
                          <td>Tous types d'eau (douce, salée, pluie, usée …)</td>
                          <td>478 860</td>
                        </tr>
                      </tbody>
                    </table>
                  </div>
                </div>

                <br>
                
                <div class="card text-center">
                  <div class="card-header">
                    Vidéos sur l'électrolyseur de Stanley Meyer
                  </div>
                  <div class="card-body">
                    <div>
                        <a href="https://www.youtube.com/watch?v=DcaSL0yQ6Kg" class="list-group-item list-group-item-action">
                            Le moteur à eau de Stanley Meyer
                        </a>
                        <a href="https://www.youtube.com/watch?v=staL1wr07Sg" class="list-group-item list-group-item-action">
                            Stanley Meyer explique la technologie du carburant d’eau
                        </a>
                        <a href="https://www.youtube.com/watch?v=xcF74Q_7kEI" class="list-group-item list-group-item-action">
                            Comment fonctionne le circuit de Stanley Meyer ?
                        </a>
                        <a href="https://www.youtube.com/watch?v=VrP3K400M7c" class="list-group-item list-group-item-action">
                            Conférence de Stanley Meyer
                        </a>
                    </div>
                  </div>
                </div>
                
                <br>

              </div>

              <br>

            </div>

            <br>

            <!-- Option 1: Bootstrap Bundle with Popper -->
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/js/bootstrap.bundle.min.js" 
            integrity="sha384-b5kHyXgcpbZJO/tY9Ul7kGkf1S0CWuKcCD38l8YkeH8z8QjE0GmW1gYU5S9FOnJ0" 
            crossorigin="anonymous">
            </script>
          </body>
        </html>
        """

        options = {
            'page-size': 'A4',
            'header-center': "Tableau comparatif des différents électrolyseurs à eau",
            'footer-right': '[page] sur [topage]',
            'footer-left': 'Société Holomorphe [SIREN : 883632556]'
        }

        path_wkthmltopdf = "C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe"
        config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
        pdfkit.from_string(body, "Fiche_Commerciale\\Comparaison_Electrolyseurs_A_Eau.pdf", configuration=config,
                           options=options)


class Fiche_Commerciale_VMEG_Electricity(unittest.TestCase):
    # ok
    def test_fiche_commerciale_vmeg_electricity(self):
        print("test_fiche_commerciale_vmeg_electricity")

        body = """
        <!doctype html>
        <html lang="en">
          <head>
            <!-- Required meta tags -->
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">

            <!-- Bootstrap CSS -->
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/css/bootstrap.min.css" 
            rel="stylesheet" 
            integrity="sha384-BmbxuPwQa2lc/FVzBcNJ7UAyJxM6wuqIj61tLrc4wSX0szH/Ev+nYRRuWlolflfl" 
            crossorigin="anonymous">

            <title>
                Sales of VMEG
            </title>
          </head>
          <body>
            <div class="container">
                <!-- General information of Entreprise individuelle ALOYAU -->
                <div class="card text-center">
                  <div class="card-header">
                    General information of Entreprise individuelle ALOYAU 
                  </div>
                  <div class="card-body">
                    <ul class="list-group list-group-flush">
                      <li class="list-group-item">
                        Name of the company : Entreprise individuelle ALOYAU
                      </li>
                      <li class="list-group-item">
                        Address of the registered office : Canton of Geneva in Switzerland 
                      </li>
                      <li class="list-group-item">
                        Registry of trade and companies : 
                        Registry of trade and companies of Geneva in Switzerland - 
                        Rue du Puits-Saint-Pierre 4 · 1204 Genève
                      </li>
                      <li class="list-group-item">
                        Activity : Production of electricity from renewable energy
                      </li>
                      
                      <li class="list-group-item">
                        President : Mr.  / 
                        Date of registration : Company in the process of registration
                      </li>
                    </ul>
                  </div>
                </div>
                <!-- General information of Entreprise individuelle ALOYAU -->

                <br>

                <!-- Contact -->
                <div class="card text-center">
                  <div class="card-header">
                    Contact
                  </div>
                  <div class="card-body">
                    <!-- Personal data -->
                    <table class="table table-striped table-bordered">
                        <thead>
                            <tr>
                                <th scope="col">
                                    Contact person
                                </th>
                                <th scope="col">
                                    Address of the registered office
                                </th>
                                <th scope="col">
                                    Telephone
                                </th>
                                <th scope="col">
                                    Email address
                                </th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>
                                    Mr. 
                                </td>
                                <td>
                                    Canton of Geneva in Switzerland
                                </td>
                                <td>
                                    00.33.7.45.75.27.00
                                </td>
                                <td>
                                    jason.aloyau@outlook.fr
                                </td>
                            </tr>
                        </tbody>
                    </table>
                    <!-- Personal data -->
                  </div>
                </div>
                <!-- Contact -->

                <br>

                <!-- Sales -->
                <div class="card text-center">
                  <div class="card-header">
                    Sales
                  </div>
                  <div class="card-body">
                    <ul class="list-group"> 
                      <li class="list-group-item">
                        Sale of electricity from renewable energy
                      </li>
                    </ul>
                  </div>
                </div>
                <!-- Sales -->

                <br>

                <!-- Pricing -->
                <div class="card text-center">
                  <div class="card-header">
                    Pricing
                  </div>
                  <div class="card-body">
                  <ul class="list-group"> 
                      <li class="list-group-item">
                        Sale of electricity from renewable energy : 0.05 CHF per kilowatthour without taxes.
                      </li>
                    </ul>
                  </div>
                </div>
                <!-- Pricing -->

                <br>

                <!-- Description of vibrating magnet electromagnetic generator -->
                <div class="card text-center">
                  <div class="card-header">
                    Description of vibrating magnet electromagnetic generator
                  </div>
                  <div class="card-body">
                    <!-- Electrical energy of vibrating magnet electromagnetic generator -->
                    <div class="card text-center">
                      <div class="card-header">
                        Electrical energy of one vibrating magnet electromagnetic generator
                      </div>
                      <div class="card-body">
                        <table class="table table-bordered">
                          <thead>
                            <tr>
                              <th scope="col">Details</th>
                              <th scope="col">Value</th>
                            </tr>
                          </thead>
                          <tbody>
                            <tr>
                              <td>Maximal voltage [Volts]</td>
                              <td>1000</td>
                            </tr>
                            <tr>
                              <td>Maximal current [Amps]</td>
                              <td>50</td>
                            </tr>
                            <tr>
                              <td>Maximal power [Watts]</td>
                              <td>50000</td>
                            </tr>
                            <tr>
                              <td>Frequency range [Hertz]</td>
                              <td>50 / 60</td>
                            </tr>
                          </tbody>
                        </table>
                      </div>
                    </div>
                    <!-- Electrical energy of vibrating magnet electromagnetic generator -->

                    <br>
                    
                    <!-- Dimensions of vibrating magnet electromagnetic generator -->
                    <div class="card text-center">
                      <div class="card-header">
                        Dimensions of one vibrating magnet electromagnetic generator
                      </div>
                      <div class="card-body">
                        <table class="table table-bordered">
                          <thead>
                            <tr>
                              <th scope="col">Details</th>
                              <th scope="col">Value</th>
                            </tr>
                          </thead>
                          <tbody>
                            <tr>
                              <td>Length [Millimeters]</td>
                              <td>Between 150 and 500</td>
                            </tr>
                            <tr>
                              <td>Width [Millimeters]</td>
                              <td>Between 150 and 500</td>
                            </tr>
                            <tr>
                              <td>Height [Millimeters]</td>
                              <td>Between 100 and 1000</td>
                            </tr>
                          </tbody>
                        </table>
                      </div>
                    </div>
                    <!-- Dimensions of vibrating magnet electromagnetic generator -->

                    <br>
                    
                    <!-- Primary energy of vibrating magnet electromagnetic generator -->
                    <div class="card text-center">
                      <div class="card-header">
                        Primary energy of vibrating magnet electromagnetic generator
                      </div>
                      <div class="card-body">
                        The primary energies of the electricity generation facilities are as follows :
                        <br>
                        - A variable magnetic field from an input coil.
                        <br>
                        - A steady magnetic field from permanent magnet.
                      </div>
                    </div>
                    <!-- Primary energy of vibrating magnet electromagnetic generator -->
                    
                    <br>
                    
                    <!-- Production technique used -->
                    <div class="card text-center">
                      <div class="card-header">
                        Production technique used
                      </div>
                      <div class="card-body">
                        The electricity production technique used by the installations is based on the creation of 
                        a vibrating magnet electromagnetic generator extracting magnetic energy from permanent magnets.
                        
                        <br>
                        <br>
                        
                        The vibrating magnet electromagnetic generator doesn't require oil, gas, coal, solar energy, 
                        wind energy, geothermal energy or hydraulic energy to operate, and it has no parts in motion.
                        
                        <br>
                        <br>
                        
                        After, this vibrating magnet electromagnetic generator is composed of the following elements :
                        <br>
                        - An input coil.
                        <br>
                        - A collector coil.
                        <br>
                        - Permanent magnets.
                        
                        <br>
                        <br>
                        
                        Then, this vibrating magnet electromagnetic generator is built following the ideas published by the 
                        inventions in the public domain which are as follows:
                        <br>
                        - Patent US6362718B1 entitled "Motionless electromagnetic generator" whose the inventors are : 
                         Stephen L. Patrick, Thomas E. Bearden, James C. Hayes, Kenneth D. Moore and James L. Kenny.
                        <br>
                        - Patent US3403323A entitled "Electrical energy translating devices and regulators using 
                        the same" whose the inventor is : Wanlass Leslie Kent.
                        <br>
                        - Patent DE3024814A1 entitled "Electrical energy generation and appts. - uses magnetic flux 
                        in permanent magnets in generator to produce pulsating magnetic flux in stationary body" 
                        whose the inventor is : Antrag Auf Nichtnennung.
                        <br>
                        - Patent US4006401A entitled "Electromagnetic generator" whose the inventor is : 
                        Eduardo Villasenor de Rivas.
                        <br>
                        - Patent US4077001A entitled "Electromagnetic convertor with stationary variable-reluctance 
                        members" whose the inventor is : Frank B. Richardson.
                        <br>
                        - Patent US5926083A entitled "Static magnet dynamo for generating electromotive force based 
                        on changing flux density of an open magnetic path" whose the inventor is : Keiichiro Asaoka.
                        <br>
                        - Patent US6246561B1 entitled "Methods for controlling the path of magnetic flux from a 
                        permanent magnet and devices incorporating the same" whose the inventor is : Charles J. Flynn.
                        
                        <br>
                        <br>
                        
                        Besides, this vibrating magnet electromagnetic generator follows the following theories :
                        <br>
                        - The theory of the superposition of magnetic fields.
                        <br>
                        - The law of energy conservation.
                        <br>
                        - The Lenz's law.
                        <br>
                        - The Faraday's law of electromagnetic induction
                      </div>
                    </div>
                    <!-- Production technique used -->
                    
                    <br>
                    
                    <!-- Energy efficiency -->
                    <div class="card text-center">
                      <div class="card-header">
                        Energy efficiency
                      </div>
                      <div class="card-body">
                        The energy efficiency of the power generation facilities is less than ninety percent.
                      </div>
                    </div>
                    <!-- Energy efficiency -->
                    
                    <br>
                    
                    <!-- Operating times -->
                    <div class="card text-center">
                      <div class="card-header">
                        Operating times
                      </div>
                      <div class="card-body">
                        The base, semi-base and peak operating times of the power generation facilities are unlimited, 
                        without taking into account the duration of any maintenance.
                      </div>
                    </div>
                    <!-- Operating times -->
                    
                    <br>
                    
                    <!-- Quantity of greenhouse gases emitted by the facilities -->
                    <div class="card text-center">
                      <div class="card-header">
                        Quantity of greenhouse gases emitted by the facilities
                      </div>
                      <div class="card-body">
                        The amount of greenhouse gas greenhouse emitted by this power generation facility is equal 
                        to zero grams.
                      </div>
                    </div>
                    <!-- Quantity of greenhouse gases emitted by the facilities -->
                    
                    <br>
                    
                    <!-- Note on the energy efficiency of the installation compared to the best techniques available at an economically cost acceptable -->
                    <div class="card text-center">
                      <div class="card-header">
                        Note on the energy efficiency of the installation compared to the best techniques available 
                        at an economically cost acceptable
                      </div>
                      <div class="card-body">
                        In accordance with the objectives of energy efficiency, security of energy supply and the 
                        fight against global warming dictated by certain directives of the European Union and certain 
                        international agreements, these electricity production facilities offer significant advantages 
                        in terms of energy efficiency, security of energy supply and contribution to the fight against 
                        global warming set out in the following points :
                        <br>
                        - No greenhouse gas emissions.
                        <br>
                        - No primary fossil energy consumption.
                        <br>
                        - Use of renewable energy coming from the magnetic energy of permanent magnets available without 
                        interruption, day and night.
                        <br>
                        - Ability to maintain energy autonomy in the overseas departments.
                        <br>
                        - Ability to promote the emergence of a competitive and job-rich economy through the 
                        mobilization of all sectors industries, particularly those of green growth, which is defined 
                        as a mode of economic development that respects the environment, both sober and efficient 
                        in energy and in the consumption of resources and carbon, socially inclusive, supporting the 
                        potential for innovation and guaranteeing the competitiveness of companies.
                        <br>
                        - Ability to ensure security of supply and reduce dependence on fossil fuel imports.
                        <br>
                        - Ability to preserve human health and the environment, in particular by combating the 
                        aggravation of the greenhouse effect and against major industrial risks, by reducing the 
                        exposure of citizens to air pollution.
                        <br>
                        - Ability to guarantee social and territorial cohesion by ensuring the right of access for 
                        all households to energy without excessive cost in relation to their resources.
                        <br>
                        - Ability to fight against fuel poverty.
                      </div>
                    </div>
                    <!-- Note on the energy efficiency of the installation compared to the best techniques available at an economically cost acceptable -->
                    
                    <br>
                    
                  </div>
                </div>
                <!-- Description of vibrating magnet electromagnetic generator -->

                <br>

                <!-- Useful links -->
                <div class="card text-center">
                  <div class="card-header">
                    Useful links
                  </div>
                  <div class="card-body">
                    <div class="list-group text-center">
                        <a class="list-group-item list-group-item-action" 
                        href="https://patents.google.com/patent/US6362718B1/en">
                            Patent US6362718B1 entitled "Motionless electromagnetic generator" whose the inventors are 
                            : Stephen L. Patrick, Thomas E. Bearden, James C. Hayes, Kenneth D. Moore and James L. 
                            Kenny.
                        </a>
                        <a class="list-group-item list-group-item-action" 
                        href="https://patents.google.com/patent/US3403323A/en?oq=us3403323">
                            Patent US3403323A entitled "Electrical energy translating devices and regulators using 
                            the same" whose the inventor is : Wanlass Leslie Kent.
                        </a>
                        <a class="list-group-item list-group-item-action" 
                        href="https://patents.google.com/patent/DE3024814A1/en?oq=de3024814">
                            Patent DE3024814A1 entitled "Electrical energy generation and appts. - uses magnetic flux 
                            in permanent magnets in generator to produce pulsating magnetic flux in stationary body" 
                            whose the inventor is : Antrag Auf Nichtnennung.
                        </a>
                        <a class="list-group-item list-group-item-action" 
                        href="https://patents.google.com/patent/US4006401A/en?oq=us4006401">
                            Patent US4006401A entitled "Electromagnetic generator" whose the inventor is : 
                            Eduardo Villasenor de Rivas.
                        </a>
                        <a class="list-group-item list-group-item-action" 
                        href="https://patents.google.com/patent/US4077001A/en?oq=us4077001">
                            Patent US4077001A entitled "Electromagnetic convertor with stationary variable-reluctance 
                            members" whose the inventor is : Frank B. Richardson.
                        </a>
                        <a class="list-group-item list-group-item-action" 
                        href="https://patents.google.com/patent/US5926083A/en?oq=us5926083">
                            Patent US5926083A entitled "Static magnet dynamo for generating electromotive force based 
                            on changing flux density of an open magnetic path" whose the inventor is : Keiichiro Asaoka.
                        </a>
                        <a class="list-group-item list-group-item-action" 
                        href="https://patents.google.com/patent/US6246561B1/en?oq=us6246561">
                            Patent US6246561B1 entitled "Methods for controlling the path of magnetic flux from a 
                            permanent magnet and devices incorporating the same" whose the inventor is : 
                            Charles J. Flynn.
                        </a>
                        <a class="list-group-item list-group-item-action" 
                        href="https://www.linkedin.com/in/jason-aloyau-531727239/">
                            's LinkedIn account
                        </a>
                        <a class="list-group-item list-group-item-action" 
                        href="https://github.com/Jay4C">
                            's GitHub account
                        </a>
                        <a class="list-group-item list-group-item-action" 
                        href="https://www.youtube.com/watch?v=HVHNYqeOi9o">
                            's YouTube account
                        </a>
                        <a class="list-group-item list-group-item-action" 
                        href="https://www.malt.fr/profile/jasonaloyau?overview=true">
                            's Malt account
                        </a>
                    </div>
                  </div>
                </div>
                <!-- Useful links -->

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
            'header-center': "Sale of electricity from renewable energy",
            'footer-right': '[page] sur [topage]',
            'footer-left': 'Entreprise individuelle ALOYAU'
        }

        path_wkthmltopdf = "C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe"

        config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)

        pdfkit.from_string(body,
                           "Fiche_Commerciale"
                           "\\VMEG_Electricity"
                           "\\Sale_of_electricity_[Entreprise_Individuelle_ALOYAU].pdf",
                           configuration=config,
                           options=options)


if __name__ == '__main__':
    unittest.main()
