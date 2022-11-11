import unittest
import pdfkit


class UnitTestsReportingHumanResourcesResumeForMe(unittest.TestCase):
    # ok
    def test_resume_developpeur_python_france(self):
        print('test_resume_developpeur_python_france')

        body = """
<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css" 
    integrity="sha384-xOolHFLEh07PJGoPkLv1IbcEPTNtaed2xpHsD9ESMhqIYd0nLMwNLD69Npy4HI+N" crossorigin="anonymous">

    <title>Resume</title>
  </head>
  <body>
    <!-- Container -->
    <div class="container">
        <!-- Développeur Python -->
        <div class="card text-center">
          <div class="card-header">
            Développeur Python
          </div>
          <div class="card-body">
            <table class="table table-bordered table-striped">
              <thead>
                <tr>
                  <th scope="col">Identité</th>
                  <th scope="col">Adresse postale</th>
                  <th scope="col">Téléphone</th>
                  <th scope="col">Email</th>
                  <th scope="col">Age</th>
                  <th scope="col">Nationalité</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>Monsieur </td>
                  <td></td>
                  <td></td>
                  <td></td>
                  <td>28 ans</td>
                  <td>Française</td>
                </tr>
              </tbody>
            </table>

            <br>
            <br>

            <!-- Compétences -->
            <div class="card text-center">
              <div class="card-header">
                Compétences
              </div>
              <div class="card-body">
                <table class="table table-bordered table-striped">
                  <thead>
                    <tr>
                      <th scope="col">Front-end</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td>
                        <ul>
                            <li>
                                Django web framework / 
                                Langage de balisage HTML / 
                                Langage CSS / 
                                Langage de programmation JavaScript
                            </li>
                            <li>
                                Librairie Bootstrap / 
                                LibrairieLeaflet.js / 
                                Librairie Vis.js / 
                                Librairie Artyom.js / 
                                LibrairieFlowchart.js / 
                                Librairie Babylon.js / 
                                Librairie Chart.js / 
                                Librairie MathJax
                            </li>
                            <li>
                                Serveur web Apache / 
                                Serveur web Nginx
                            </li>
                        </ul>
                      </td>
                    </tr>
                  </tbody>
                </table>

                <br>
                <br>

                <table class="table table-bordered table-striped">
                  <thead>
                    <tr>
                      <th scope="col">Back-end</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td>
                        <ul>
                            <li>
                                Langage de programmation Python / 
                                Framework Flask / 
                                Framework FastAPI / 
                                Librairie SQLAlchemy / 
                                Librairie unittests / 
                                Librairie BeautifulSoup / 
                                Librairie Selenium WebDriver / 
                                Librairie pymysql.cursors / 
                                Librairie requests / 
                                Librairie pdfkit / 
                                Librairie xlswriter / 
                                Librairie xlrd / 
                                Librairie pywinauto / 
                                Librairie Skidl / 
                                Librairie PyPDF2 / 
                                Librairie reportlab / 
                                Librairie pylatex / 
                                Librairie sympy / 
                                Librairie numpy / 
                                Librairie pandas / 
                                Librairie matplotlib / 
                                Librairie ahkab / 
                                Librairie email / 
                                Librairie smtplib / 
                                Librairieschemdraw / 
                                Librairie paramiko / 
                                Librairie imaplib / 
                                Librairie imap_tools / 
                                Librairie minimalmodbus / 
                                Librairie pyModbusTCP
                            </li>
                            <li>
                                Serveur de bases de données relationnelles MySQL / 
                                Serveur de bases de données documents MongoDB / 
                                Serveur de bases de données graphe de Neo4j
                            </li>
                            <li>
                                Carte embarquée Raspberry Pi / 
                                Système d’exploitation Raspbian
                            </li>
                            <li>
                                Logiciel de gestion de version Git / 
                                Gestion de mon compte GitHub : https://github.com/Jay4C / 
                                Docker
                            </li>
                            <li>
                                Logiciel FreeCAD / 
                                Logiciel KiCAD / 
                                Logiciel SonarQube
                            </li>
                            <li>
                                Windows / 
                                Linux / 
                                Ubuntu / 
                                Script Shell / 
                                Cron Job / 
                                Serveur privé virtuel
                            </li>
                        </ul>
                      </td>
                    </tr>
                  </tbody>
                </table>

                <br>
                <br>

                <table class="table table-bordered table-striped">
                  <thead>
                    <tr>
                      <th scope="col">Management</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td>
                        <ul>
                            <li>
                                Brainstorming / 
                                Logiciel FreeMind / 
                                Logiciel Pencil / 
                                Diagrammes UML / 
                                Logiciel Gaphor
                            </li>
                            <li>
                                Diagramme de Gantt / 
                                Logiciel GanttProject / 
                                Planification des étapes d'un projet
                            </li>
                            <li>
                                Management dela connaissance / 
                                Management de projet / 
                                Management des opérations / 
                                Management du changement / 
                                Management dela qualité
                            </li>
                            <li>
                                Analyse des besoins du client / 
                                Établissement d’un cahier des charges
                            </li>
                            <li>
                                Rédaction d'un support technique / 
                                Rédaction d'une base de données de connaissances
                            </li>
                            <li>
                                Droit français : "www.legifrance.gouv.fr" / 
                                Droit européen : "https://europa.eu/european-union/law/find-legislation_fr" / 
                                Droit international : "www.lexadin.nl"
                            </li>
                            <li>
                                Anglais écrit et oral [TOEIC : 840 points ; Date d'expiration : 11 Juillet 2020]
                            </li>
                        </ul>
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
            <!-- Compétences -->

            <br>
            <br>

            <!-- Expériences -->
            <div class="card text-center">
              <div class="card-header">
                Expériences
              </div>
              <div class="card-body">
                <table class="table table-bordered table-striped">
                  <thead>
                    <tr>
                      <th>
                        Intitulé :  Développeur Python
                        <br>
                        Période : Mai 2019 – Juin 2022 [3 ans et 1 mois]
                        <br>
                        Statut professionnel : Président
                        <br>
                        Société : Holomorphe - SIREN : 883 632 556 - Paris (75007)
                      </th>
                    </tr>
                  </thead>
                  <tbody>
                    <tbody>
                    <tr>
                      <td>
                        <ul>
                            <li>
                                Développement d'un site internet pour présenter la société disponible sur 
                                https://github.com/Jay4C/Holomorphe_Company/tree/main/holomorphefrontend (Python - 
                                Django web framework)
                            </li>
                            <li>
                                Développement d'un programme d'API disponible sur 
                                https://github.com/Jay4C/Holomorphe_Company/tree/main/holomorphebackend 
                                (Python - Librairie Flask API)
                            </li>
                            <li>
                                Développement de programmes informatiques pour gérer un serveur privé virtuel Linux 
                                Ubuntu hébergé chez OVH Cloud (Script Shell - Cron Job)
                            </li>
                            <li>
                                Développement d'applications Python pour créer des pièces mécaniques de précision pour 
                                les technologies de l'hydrogène avec le logiciel FreeCAD disponibles sur 
                                https://github.com/Jay4C/Python-Macros-For-FreeCAD (Python)
                            </li>
                            <li>
                                Développement d'applications Python pour l'automatisation de processus robotisés 
                                disponibles sur https://github.com/Jay4C/Web-Automation (Python - Librairie Selenium)
                            </li>
                            <li>
                                Développement d'une application Python pour récupérer toutes les parcelles convenables 
                                pour injecter du méthane desynthèse dans un réseau de gaz naturel en France 
                                (Python - Librairie requests - API Open data)
                            </li>
                            <li>
                                Développement de tests unitaires pour programmer des robots d'exploration de données 
                                disponibles sur https://github.com/Jay4C/Web-Scraping (Python - Librairie BeautifulSoup)
                            </li>
                            <li>
                                Développement de tests unitaires pour faire du mailing (Python - Librairie smtplib)
                            </li>
                            <li>
                                Développement de tests unitaires pour préparer des requêtes vers des API disponibles 
                                sur https://github.com/Jay4C/API (Python - Librairie requests)
                            </li>
                            <li>
                                Développement de tests unitaires pour faire des diagrammes decircuits électroniques 
                                disponibles sur 
                                https://github.com/Jay4C/Electronic_Circuit_Diagram_With_Python_Schemdraw 
                                (Python - Librairie schemdraw)
                            </li>
                            <li>
                                Développement detests unitaires pour fabriquer des circuits électroniques disponibles 
                                sur https://github.com/Jay4C/Electronic_Design_Automation_With_Python_Skidl 
                                (Python - Librairie Skidl)
                            </li>
                            <li>
                                Développement detests unitaires pour simuler des circuits électroniques disponibles sur
                                https://github.com/Jay4C/Electronic_Circuit_Simulation_With_Python 
                                (Python - Librairie ahkab - Librairie pyspice)
                            </li>
                        </ul>
                      </td>
                    </tr>
                  </tbody>
                </table>

                <br>
                <br>

                <table class="table table-bordered table-striped">
                  <thead>
                    <tr>
                      <th>
                        Intitulé : Développeur Python
                        <br>
                        Période : Octobre 2016 - Avril 2019 [30 mois]
                        <br>
                        Statut professionnel : Auto-entrepreneur
                        <br>
                        Société : Entreprise ALOYAU - SIREN : 823 502 222 - Saint-ouen (93400)
                      </th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td>
                        <ul>
                            <li>
                                Développement de tests unitaires pour paramétrer des trajectoires de bras-robot 
                                avec la carte Raspberry Pi (Python - Librairie RPi.GPIO)
                            </li>
                            <li>
                                Développement de tests unitaires pour concevoir des circuits électroniques sous 
                                le logiciel KiCAD orientés pour l'agriculture (Python - Librairie Skidl)
                            </li>
                            <li>
                                Développement de tests unitaires pour convertir des séries d'images en vidéos sur 
                                des machines afin de les diffuser sur YouTube (Python - Librairie matplotlib - 
                                Librairie cv2)
                            </li>
                        </ul>
                      </td>
                    </tr>
                  </tbody>
                </table>

                <br>
                <br>

                <table class="table table-bordered table-striped">
                  <thead>
                    <tr>
                      <th>
                        Intitulé : Développeur Python
                        <br>
                        Périodes : Avril 2015 - Juillet 2015 [4 mois] et Février 2016 - Juillet 2016 [6 mois]
                        <br>
                        Statut professionnel : Stagiaire
                        <br>
                        Société : Agronergy - SIREN : 792 570 137 - Paris (75018)
                      </th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td>
                        <ul>
                            <li>
                                Développement de programmes informatiques pour collecter des données énergétiques sur 
                                des chaudières avec la carte Raspberry Pi grâceau protocole Modbus 
                                (Python - Librairie minimalmodbus)
                            </li>
                            <li>
                                Développement de programmes informatiques pour stocker des données énergétiques issues 
                                de chaudières dans un serveur de base de données MySQL 
                                (Python - Librairie pymysql.cursors)
                            </li>
                            <li>
                                Développement de programmes informatiques pour piloter des chaudières à distance avec 
                                la carte Raspberry Pi (Python - Librairie pyModbusTCP)
                            </li>
                            <li>
                                Développement de programmes informatiques pour gérer un serveur privé virtuel Linux 
                                Ubuntu hébergé chez OVH Cloud (Script Shell - Cron Job)
                            </li>
                        </ul>
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
            <!-- Expériences -->

            <br>
            <br>

            <!-- Formations -->
            <div class="card text-center">
              <div class="card-header">
                Formations
              </div>
              <div class="card-body">
                <table class="table table-bordered table-striped">
                  <thead>
                    <tr>
                      <th>
                        Intitulé : Diplôme d'ingénieur généraliste
                        <br>
                        Période : Septembre 2013 - Août 2016 [3 ans]
                        <br>
                        Centre de formation : École Supérieure d'Ingénieurs Léonard de Vinci – Paris La Défense
                      </th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td>
                        <ul>
                            <li>
                                Nouvelles énergies / 
                                Informatique / 
                                Finance / 
                                Mécanique numérique
                            </li>
                            <li>
                                Veille technologique / 
                                Physique / 
                                Mathématiques / 
                                Economie / 
                                Management / 
                                Marketing / 
                                Comptabilité
                            </li>
                        </ul>
                      </td>
                    </tr>
                  </tbody>
                </table>

                <br>
                <br>

                <table class="table table-bordered table-striped">
                  <thead>
                    <tr>
                      <th>
                        Intitulé : Classes préparatoires aux grandes écoles PTSI-PT
                        <br>
                        Période : Août 2011 - Août 2013 [2 ans]
                        <br>
                        Centre de formation : Lycée Lislet Geoffroy à l'Ile de La Réunion
                      </th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td>
                        <ul>
                            <li>
                                Mathématiques / 
                                Chimie / 
                                Physique / 
                                Technologie / 
                                Sciences de l'ingénieur
                            </li>
                        </ul>
                      </td>
                    </tr>
                  </tbody>
                </table>

                <br>
                <br>

                <table class="table table-bordered table-striped">
                  <thead>
                    <tr>
                      <th>
                        Intitulé : Baccalauréat scientifique
                        <br>
                        Période : Août 2010 - Août 2011 [1 an]
                        <br>
                        Centre de formation : Lycée Roland Garros à l'Ile de La Réunion
                      </th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td>
                        <ul>
                            <li>
                                Sciences de l'ingénieur / 
                                Mathématiques / 
                                Physique / 
                                Chimie / 
                                Anglais / 
                                Français / 
                                Histoire
                            </li>
                        </ul>
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
            <!-- Formations -->

            <br>

        </div>
        <!-- Développeur Python -->
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
            'footer-left': 'Développeur Python',
            'header-center': 'CV de Monsieur ',
        }

        pdfkit.from_string(
            body,
            "Resume_For_Me\\CV_De__[Developpeur_Python].pdf",
            options=options
        )

    # ok
    def test_resume_developpeur_python_reunion(self):
        print('test_resume_developpeur_python_reunion')

        body = """
<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" 
    content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" 
    href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css" 
    integrity="sha384-xOolHFLEh07PJGoPkLv1IbcEPTNtaed2xpHsD9ESMhqIYd0nLMwNLD69Npy4HI+N" 
    crossorigin="anonymous">

    <title>Resume</title>
  </head>
  <body>
    <!-- Container -->
    <div class="container">
        <!-- Développeur Python -->
        <div class="card text-center">
          <div class="card-header">
            Développeur Python
          </div>
          <div class="card-body">
            <table class="table table-bordered table-striped">
              <thead>
                <tr>
                  <th scope="col">Identité</th>
                  <th scope="col">Adresse postale</th>
                  <th scope="col">Téléphone</th>
                  <th scope="col">Email</th>
                  <th scope="col">Age</th>
                  <th scope="col">Nationalité</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>Monsieur </td>
                  <td></td>
                  <td></td>
                  <td></td>
                  <td>28 ans</td>
                  <td>Française</td>
                </tr>
              </tbody>
            </table>

            <br>
            <br>

            <!-- Compétences -->
            <div class="card text-center">
              <div class="card-header">
                Compétences
              </div>
              <div class="card-body">
                <table class="table table-bordered table-striped">
                  <thead>
                    <tr>
                      <th scope="col">Front-end</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td>
                        <ul>
                            <li>
                                Django web framework / 
                                Langage de balisage HTML / 
                                Langage CSS / 
                                Langage de programmation JavaScript
                            </li>
                            <li>
                                Librairie Bootstrap / 
                                Librairie Leaflet.js / 
                                Librairie Vis.js / 
                                Librairie Artyom.js / 
                                LibrairieFlowchart.js / 
                                Librairie Babylon.js / 
                                Librairie Chart.js / 
                                Librairie MathJax
                            </li>
                            <li>
                                Serveur web Apache / 
                                Serveur web Nginx
                            </li>
                        </ul>
                      </td>
                    </tr>
                  </tbody>
                </table>

                <br>
                <br>

                <table class="table table-bordered table-striped">
                  <thead>
                    <tr>
                      <th scope="col">Back-end</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td>
                        <ul>
                            <li>
                                Langage de programmation Python / 
                                Framework Flask / 
                                Framework FastAPI / 
                                Librairie SQLAlchemy / 
                                Librairie unittests / 
                                Librairie BeautifulSoup / 
                                Librairie Selenium WebDriver / 
                                Librairie pymysql.cursors / 
                                Librairie requests / 
                                Librairie pdfkit / 
                                Librairie xlswriter / 
                                Librairie xlrd / 
                                Librairie pywinauto / 
                                Librairie Skidl / 
                                Librairie PyPDF2 / 
                                Librairie reportlab / 
                                Librairie pylatex / 
                                Librairie sympy / 
                                Librairie numpy / 
                                Librairie pandas / 
                                Librairie matplotlib / 
                                Librairie ahkab / 
                                Librairie email / 
                                Librairie smtplib / 
                                Librairie schemdraw / 
                                Librairie paramiko / 
                                Librairie imaplib / 
                                Librairie imap_tools / 
                                Librairie minimalmodbus / 
                                Librairie pyModbusTCP
                            </li>
                            <li>
                                Serveur de bases de données relationnelles MySQL / 
                                Serveur de bases de données documents MongoDB / 
                                Serveur de bases de données graphe de Neo4j
                            </li>
                            <li>
                                Carte embarquée Raspberry Pi / 
                                Système d'exploitation Raspbian
                            </li>
                            <li>
                                Logiciel de gestion de version Git / 
                                Gestion de mon compte GitHub : https://github.com/Jay4C / 
                                Docker
                            </li>
                            <li>
                                Logiciel FreeCAD / 
                                Logiciel KiCAD / 
                                Logiciel SonarQube
                            </li>
                            <li>
                                Windows / 
                                Linux / 
                                Ubuntu / 
                                Script Shell / 
                                Cron Job / 
                                Serveur privé virtuel
                            </li>
                        </ul>
                      </td>
                    </tr>
                  </tbody>
                </table>

                <br>
                <br>

                <table class="table table-bordered table-striped">
                  <thead>
                    <tr>
                      <th scope="col">Management</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td>
                        <ul>
                            <li>
                                Brainstorming / 
                                Logiciel FreeMind / 
                                Logiciel Pencil / 
                                Diagrammes UML / 
                                Logiciel Gaphor
                            </li>
                            <li>
                                Diagramme de Gantt / 
                                Logiciel GanttProject / 
                                Planification des étapes d'un projet
                            </li>
                            <li>
                                Management de la connaissance / 
                                Management de projet / 
                                Management des opérations / 
                                Management du changement / 
                                Management de la qualité
                            </li>
                            <li>
                                Analyse des besoins du client / 
                                Établissement d'un cahier des charges
                            </li>
                            <li>
                                Rédaction d'un support technique / 
                                Rédaction d'une base de données de connaissances
                            </li>
                            <li>
                                Droit français : "www.legifrance.gouv.fr" / 
                                Droit européen : "https://europa.eu/european-union/law/find-legislation_fr" / 
                                Droit international : "www.lexadin.nl"
                            </li>
                            <li>
                                Anglais écrit et oral [TOEIC : 840 points ; Date d'expiration : 11 Juillet 2020]
                            </li>
                        </ul>
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
            <!-- Compétences -->

            <br>
            <br>

            <!-- Expériences -->
            <div class="card text-center">
              <div class="card-header">
                Expériences
              </div>
              <div class="card-body">
                <table class="table table-bordered table-striped">
                  <thead>
                    <tr>
                      <th>
                        Intitulé :  Développeur Python
                        <br>
                        Période : Mai 2019 – Juin 2022 [3 ans et 1 mois]
                        <br>
                        Statut professionnel : Président
                        <br>
                        Société : Holomorphe - SIREN : 883 632 556 - Paris (75007)
                      </th>
                    </tr>
                  </thead>
                  <tbody>
                    <tbody>
                    <tr>
                      <td>
                        <ul>
                            <li>
                                Développement d'un site internet pour présenter la société disponible sur 
                                https://github.com/Jay4C/Holomorphe_Company/tree/main/holomorphefrontend (Python - 
                                Django web framework)
                            </li>
                            <li>
                                Développement d'un programme d'API disponible sur 
                                https://github.com/Jay4C/Holomorphe_Company/tree/main/holomorphebackend 
                                (Python - Librairie Flask API)
                            </li>
                            <li>
                                Développement de programmes informatiques pour gérer un serveur privé virtuel Linux 
                                Ubuntu hébergé chez OVH Cloud (Script Shell - Cron Job)
                            </li>
                            <li>
                                Développement d'applications Python pour créer des pièces mécaniques de précision pour 
                                les technologies de l'hydrogène avec le logiciel FreeCAD disponibles sur 
                                https://github.com/Jay4C/Python-Macros-For-FreeCAD (Python)
                            </li>
                            <li>
                                Développement d'applications Python pour l'automatisation de processus robotisés 
                                disponibles sur https://github.com/Jay4C/Web-Automation (Python - Librairie Selenium)
                            </li>
                            <li>
                                Développement d'une application Python pour récupérer toutes les parcelles convenables 
                                pour injecter du méthane desynthèse dans un réseau de gaz naturel en France 
                                (Python - Librairie requests - API Open data)
                            </li>
                            <li>
                                Développement de tests unitaires pour programmer des robots d'exploration de données 
                                disponibles sur https://github.com/Jay4C/Web-Scraping (Python - Librairie BeautifulSoup)
                            </li>
                            <li>
                                Développement de tests unitaires pour faire du mailing (Python - Librairie smtplib)
                            </li>
                            <li>
                                Développement de tests unitaires pour préparer des requêtes vers des API disponibles 
                                sur https://github.com/Jay4C/API (Python - Librairie requests)
                            </li>
                            <li>
                                Développement de tests unitaires pour faire des diagrammes decircuits électroniques 
                                disponibles sur 
                                https://github.com/Jay4C/Electronic_Circuit_Diagram_With_Python_Schemdraw 
                                (Python - Librairie schemdraw)
                            </li>
                            <li>
                                Développement detests unitaires pour fabriquer des circuits électroniques disponibles 
                                sur https://github.com/Jay4C/Electronic_Design_Automation_With_Python_Skidl 
                                (Python - Librairie Skidl)
                            </li>
                            <li>
                                Développement detests unitaires pour simuler des circuits électroniques disponibles sur
                                https://github.com/Jay4C/Electronic_Circuit_Simulation_With_Python 
                                (Python - Librairie ahkab - Librairie pyspice)
                            </li>
                        </ul>
                      </td>
                    </tr>
                  </tbody>
                </table>

                <br>
                <br>

                <table class="table table-bordered table-striped">
                  <thead>
                    <tr>
                      <th>
                        Intitulé : Développeur Python
                        <br>
                        Période : Octobre 2016 - Avril 2019 [30 mois]
                        <br>
                        Statut professionnel : Auto-entrepreneur
                        <br>
                        Société : Entreprise ALOYAU - SIREN : 823 502 222 - Saint-ouen (93400)
                      </th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td>
                        <ul>
                            <li>
                                Développement de tests unitaires pour paramétrer des trajectoires de bras-robot 
                                avec la carte Raspberry Pi (Python - Librairie RPi.GPIO)
                            </li>
                            <li>
                                Développement de tests unitaires pour concevoir des circuits électroniques sous 
                                le logiciel KiCAD orientés pour l'agriculture (Python - Librairie Skidl)
                            </li>
                            <li>
                                Développement de tests unitaires pour convertir des séries d'images en vidéos sur 
                                des machines afin de les diffuser sur YouTube (Python - Librairie matplotlib - 
                                Librairie cv2)
                            </li>
                        </ul>
                      </td>
                    </tr>
                  </tbody>
                </table>

                <br>
                <br>

                <table class="table table-bordered table-striped">
                  <thead>
                    <tr>
                      <th>
                        Intitulé : Développeur Python
                        <br>
                        Périodes : Avril 2015 - Juillet 2015 [4 mois] et Février 2016 - Juillet 2016 [6 mois]
                        <br>
                        Statut professionnel : Stagiaire
                        <br>
                        Société : Agronergy - SIREN : 792 570 137 - Paris (75018)
                      </th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td>
                        <ul>
                            <li>
                                Développement de programmes informatiques pour collecter des données énergétiques sur 
                                des chaudières avec la carte Raspberry Pi grâceau protocole Modbus 
                                (Python - Librairie minimalmodbus)
                            </li>
                            <li>
                                Développement de programmes informatiques pour stocker des données énergétiques issues 
                                de chaudières dans un serveur de base de données MySQL 
                                (Python - Librairie pymysql.cursors)
                            </li>
                            <li>
                                Développement de programmes informatiques pour piloter des chaudières à distance avec 
                                la carte Raspberry Pi (Python - Librairie pyModbusTCP)
                            </li>
                            <li>
                                Développement de programmes informatiques pour gérer un serveur privé virtuel Linux 
                                Ubuntu hébergé chez OVH Cloud (Script Shell - Cron Job)
                            </li>
                        </ul>
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
            <!-- Expériences -->

            <br>
            <br>

            <!-- Formations -->
            <div class="card text-center">
              <div class="card-header">
                Formations
              </div>
              <div class="card-body">
                <table class="table table-bordered table-striped">
                  <thead>
                    <tr>
                      <th>
                        Intitulé : Diplôme d'ingénieur généraliste
                        <br>
                        Période : Septembre 2013 - Août 2016 [3 ans]
                        <br>
                        Centre de formation : École Supérieure d'Ingénieurs Léonard de Vinci – Paris La Défense
                      </th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td>
                        <ul>
                            <li>
                                Nouvelles énergies / 
                                Informatique / 
                                Finance / 
                                Mécanique numérique
                            </li>
                            <li>
                                Veille technologique / 
                                Physique / 
                                Mathématiques / 
                                Economie / 
                                Management / 
                                Marketing / 
                                Comptabilité
                            </li>
                        </ul>
                      </td>
                    </tr>
                  </tbody>
                </table>

                <br>
                <br>

                <table class="table table-bordered table-striped">
                  <thead>
                    <tr>
                      <th>
                        Intitulé : Classes préparatoires aux grandes écoles PTSI-PT
                        <br>
                        Période : Août 2011 - Août 2013 [2 ans]
                        <br>
                        Centre de formation : Lycée Lislet Geoffroy à l'Ile de La Réunion
                      </th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td>
                        <ul>
                            <li>
                                Mathématiques / 
                                Chimie / 
                                Physique / 
                                Technologie / 
                                Sciences de l'ingénieur
                            </li>
                        </ul>
                      </td>
                    </tr>
                  </tbody>
                </table>

                <br>
                <br>

                <table class="table table-bordered table-striped">
                  <thead>
                    <tr>
                      <th>
                        Intitulé : Baccalauréat scientifique
                        <br>
                        Période : Août 2010 - Août 2011 [1 an]
                        <br>
                        Centre de formation : Lycée Roland Garros à l'Ile de La Réunion
                      </th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td>
                        <ul>
                            <li>
                                Sciences de l'ingénieur / 
                                Mathématiques / 
                                Physique / 
                                Chimie / 
                                Anglais / 
                                Français / 
                                Histoire
                            </li>
                        </ul>
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
            <!-- Formations -->

            <br>

        </div>
        <!-- Développeur Python -->
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
            'footer-left': 'Développeur Python',
            'header-center': 'CV de Monsieur ',
        }

        pdfkit.from_string(
            body,
            "Resume_For_Me\\CV_De__[Developpeur_Python]_v1.pdf",
            options=options
        )

    # ok
    def test_resume_ingenieur_energies_renouvelables(self):
        print('test_resume_ingenieur_energies_renouvelables')

        body = """
<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css" 
    integrity="sha384-xOolHFLEh07PJGoPkLv1IbcEPTNtaed2xpHsD9ESMhqIYd0nLMwNLD69Npy4HI+N" crossorigin="anonymous">

    <title>CV de  - Ingénieur en énergies renouvelables</title>
  </head>
  <body>
    <!-- Container -->
    <div class="container">
        <!-- Ingénieur en énergies renouvelables -->
        <div class="card text-center">
          <div class="card-header">
            Ingénieur en énergies renouvelables
          </div>
          <div class="card-body">
            <table class="table table-bordered table-striped">
              <thead>
                <tr>
                  <th scope="col">Identité</th>
                  <th scope="col">Adresse postale</th>
                  <th scope="col">Téléphone</th>
                  <th scope="col">Email</th>
                  <th scope="col">Age</th>
                  <th scope="col">Nationalité</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>Monsieur </td>
                  <td>Région Ile-de-France</td>
                  <td></td>
                  <td></td>
                  <td>28 ans</td>
                  <td>Française</td>
                </tr>
              </tbody>
            </table>

            <br>
            <br>

            <!-- Compétences -->
            <div class="card text-center">
              <div class="card-header">
                Compétences
              </div>
              <div class="card-body">
                <table class="table table-bordered table-striped">
                  <thead>
                    <tr>
                      <th scope="col">&Eacute;nergie</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td>
                        <ul>
                            <li>
                                Exploration de brevets tombés dans le domaine public afin d'exploiter des générateurs 
                                d'électricité non conventionnels
                            </li>
                            <li>
                                Conception assistée par ordinateur de générateurs d'électricité non conventionnels en 
                                exploitant des brevets tombés dans le domaine public
                            </li>
                            <li>
                                Chiffrage des pièces mécaniques de précision entrant dans la fabrication d'un 
                                générateur d'électricité non conventionnel en sollicitant des sous-traitants ayant 
                                un système de devis instantané en ligne
                            </li>
                            <li>
                                Développement de théories scientifiques pour démontrer théoriquement le fonctionnement 
                                de générateurs d'électricité non conventionnels et théoriser plusieurs puissances 
                                nominales en fonction des contraintes techniques, environnementales et économiques
                            </li>
                            <li>
                                Exploration de textes juridiques au niveau international pour la production 
                                d'électricité afin de pouvoir exploiter des générateurs d'électricité non 
                                conventionnels sans obligation de demande d'autorisation auprès des autorités chargées 
                                de l'énergie
                            </li>
                            <li>
                                Recherche de fournisseurs de pièces mécaniques de précision pouvant livrer au 
                                niveau international pour assurer la fabrication d'un générateur d'électricité non 
                                conventionnel localement depuis une installation de production d'électricité
                            </li>
                            <li>
                                Analyse du marché de l'énergie au niveau international pour trouver de nouvelles 
                                opportunités d'intégration de générateurs d'électricité non conventionnels sur le 
                                réseau public d'électricité
                            </li>
                            <li>
                                Recherche des autorités compétentes en matière d'énergie au niveau international
                            </li>
                            <li>
                                Rédaction de demande d'autorisation d'exploiter une installation de production 
                                d'électricité devant être adressée au ministère de la transition écologique
                            </li>
                        </ul>
                      </td>
                    </tr>
                  </tbody>
                </table>

                <br>
                <br>

                <table class="table table-bordered table-striped">
                  <thead>
                    <tr>
                      <th scope="col">Informatique</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td>
                        <ul>
                            <li>
                                Langage de balisage HTML / 
                                Librairie Bootstrap / 
                                Librairie MathJax /
                                Langage de programmation Python / 
                                Serveurs de bases de données MySQL, MongoDB, Neo4j / 
                                Logiciel Git / 
                                Logiciel FreeCAD / 
                                Logiciel KiCAD / 
                                Systèmes d'exploitation Windows, Linux, Raspbian / 
                                Carte Raspberry Pi
                            </li>
                        </ul>
                      </td>
                    </tr>
                  </tbody>
                </table>

                <br>
                <br>

                <table class="table table-bordered table-striped">
                  <thead>
                    <tr>
                      <th scope="col">Management</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td>
                        <ul>
                            <li>
                                Brainstorming / 
                                Logiciel FreeMind / 
                                Logiciel Pencil / 
                                Diagramme de Gantt / 
                                Logiciel GanttProject
                            </li>
                            <li>
                                Management de la connaissance / 
                                Management de projet / 
                                Management des opérations / 
                                Management du changement / 
                                Management de la qualité
                            </li>
                            <li>
                                Recherche de clients, fournisseurs et partenaires au niveau international / 
                                Prospection immobilière / 
                                Établissement d'un cahier des charges / 
                                Planification des étapes d'un projet / 
                                Rédaction d'une base de données de connaissances
                            </li>
                            <li>
                                Anglais écrit et oral [TOEIC : 840 points ; Date d'expiration : 11 Juillet 2020]
                            </li>
                        </ul>
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
            <!-- Compétences -->

            <br>
            <br>

            <!-- Expériences -->
            <div class="card text-center">
              <div class="card-header">
                Expériences
              </div>
              <div class="card-body">
                <table class="table table-bordered table-striped">
                  <thead>
                    <tr>
                      <th>
                        Intitulé : Ingénieur en énergies renouvelables
                        <br>
                        Période : Mai 2019 – Juin 2022 [3 ans et 1 mois]
                        <br>
                        Statut professionnel : Président
                        <br>
                        Société : Holomorphe - SIREN : 883 632 556 - Paris (75007)
                      </th>
                    </tr>
                  </thead>
                  <tbody>
                    <tbody>
                    <tr>
                      <td>
                        <ul>
                            <li>
                                Développement d'applications Python pour créer des pièces mécaniques de précision afin de  
                                concevoir un générateur d'hydrogène par électrolyse de l'eau combinant les inventions 
                                de Stanley Meyer et Archie Blue en utilisant le logiciel FreeCAD disponibles sur 
                                https://github.com/Jay4C/Python-Macros-For-FreeCAD/tree/master/Brevet_us_4_936_961_water_electrolyser_4 (Python)
                            </li>
                            <li>
                                Développement d'applications Python pour concevoir un projet industriel pour la 
                                production d'hydrogène gazeux par électrolyse de l'eau en utilisant le logiciel FreeCAD 
                                (Python)
                            </li>
                            <li>
                                Mise en application des directives européennes pour satisfaire les exigences 
                                techniques en matière de santé et de sécurité humaine concernant la compatibilité 
                                électromagnétique, les matériels électriques fonctionnant à basse tension, les 
                                matériels électriques fonctionnant à haute tension et les machines
                            </li>
                            <li>
                                Recherche de fournisseurs de prestations de certifications qualité pour examiner et 
                                certifier la conformité du générateur d'hydrogène par électrolyse de l'eau combinant 
                                les inventions de Stanley Meyer et Archie Blue
                            </li>
                            <li>
                                Recherche de fournisseurs de pièces mécaniques de précision proposant l'impression 3D, 
                                la découpe laser, la fabrication de circuits électroniques et la visserie
                            </li>
                            <li>
                                Chiffrage d'un projet industriel pour la production d'hydrogène gazeux par électrolyse 
                                de l'eau
                            </li>
                            <li>
                                Recherche de partenaires qui fabriquent des générateurs à eau atmosphérique, des 
                                systèmes de capture de dioxyde de carbone et des aéronefs électriques à décollage et 
                                atterissage vertical ayant besoin de réduire leur impact écologique tout en augmentant 
                                la performance de leurs activités
                            </li>
                            <li>
                                Développement d'applications Python pour créer des pièces mécaniques de précision afin de  
                                concevoir un génerateur électromagnétique sans partie mobile inventé par Thomas Bearden 
                                et ses collègues en utilisant le logiciel FreeCAD disponibles sur 
                                https://github.com/Jay4C/Python-Macros-For-FreeCAD/tree/master/Patent_US6362718B1_Motionless_Electromagnetic_Generator (Python)
                            </li>
                            <li>
                                Développement de tests unitaires pour fabriquer des circuits électroniques disponibles 
                                sur https://github.com/Jay4C/Electronic_Design_Automation_With_Python_Skidl 
                                (Python - Librairie Skidl)
                            </li>
                            <li>
                                Développement d'une application Python pour récupérer toutes les parcelles convenables 
                                pour injecter du méthane de synthèse dans un réseau de gaz naturel en France 
                                (Python - Librairie requests - API Open data)
                            </li>
                            <li>
                                Développement d'un programme d'API Rest pour suivre les tendances du marché de l'énergie 
                                disponible sur https://github.com/Jay4C/Holomorphe_Company/tree/main/holomorphebackend 
                                (Python - Librairie Flask API)
                            </li>
                        </ul>
                      </td>
                    </tr>
                  </tbody>
                </table>

                <br>
                <br>

                <table class="table table-bordered table-striped">
                  <thead>
                    <tr>
                      <th>
                        Intitulé : Ingénieur en énergies renouvelables
                        <br>
                        Période : Octobre 2016 - Avril 2019 [30 mois]
                        <br>
                        Statut professionnel : Auto-entrepreneur
                        <br>
                        Société : Entreprise ALOYAU - SIREN : 823 502 222 - Saint-ouen (93400)
                      </th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td>
                        <ul>
                            <li>
                                Développement de tests unitaires pour concevoir des circuits électroniques sous 
                                le logiciel KiCAD orientés pour la production d'électricité à partir d'ondes 
                                radio (Python - Librairie Skidl)
                            </li>
                            <li>
                                Développement de tests unitaires pour concevoir des circuits électroniques sous 
                                le logiciel KiCAD orientés pour l'agriculture afin de piloter des pompes à eau et 
                                récupérer des données issues de capteurs de température et pression 
                                (Python - Librairie Skidl)
                            </li>
                            <li>
                                Développement de tests unitaires pour paramétrer des trajectoires de bras-robot 
                                avec la carte Raspberry Pi pour extraire des composants électroniques contenant des 
                                métaux précieux (Python - Librairie RPi.GPIO)
                            </li>
                        </ul>
                      </td>
                    </tr>
                  </tbody>
                </table>

                <br>
                <br>

                <table class="table table-bordered table-striped">
                  <thead>
                    <tr>
                      <th>
                        Intitulé : Ingénieur en énergies renouvelables
                        <br>
                        Périodes : Avril 2015 - Juillet 2015 [4 mois] et Février 2016 - Juillet 2016 [6 mois]
                        <br>
                        Statut professionnel : Stagiaire
                        <br>
                        Société : Agronergy - SIREN : 792 570 137 - Paris (75018)
                      </th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td>
                        <ul>
                            <li>
                                Développement de programmes informatiques pour collecter des données énergétiques sur 
                                des chaudières biomasse et des compteurs d'énergie avec la carte Raspberry Pi grâce 
                                au protocole modbus (Python - Librairie minimalmodbus)
                            </li>
                            <li>
                                Développement de programmes informatiques pour stocker des données énergétiques issues 
                                de chaudières biomasse et des compteurs d'énergie dans un serveur de base de données 
                                MySQL (Python - Librairie pymysql.cursors)
                            </li>
                            <li>
                                Développement de programmes informatiques pour piloter des chaudières à distance avec 
                                la carte Raspberry Pi (Python - Librairie pyModbusTCP)
                            </li>
                        </ul>
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
            <!-- Expériences -->

            <br>
            <br>

            <!-- Formations -->
            <div class="card text-center">
              <div class="card-header">
                Formations
              </div>
              <div class="card-body">
                <table class="table table-bordered table-striped">
                  <thead>
                    <tr>
                      <th>
                        Intitulé : Diplôme d'ingénieur généraliste
                        <br>
                        Période : Septembre 2013 - Août 2016 [3 ans]
                        <br>
                        Centre de formation : École Supérieure d'Ingénieurs Léonard de Vinci – Paris La Défense
                      </th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td>
                        <ul>
                            <li>
                                Nouvelles énergies / 
                                Informatique / 
                                Finance / 
                                Mécanique numérique
                            </li>
                            <li>
                                Veille technologique / 
                                Physique / 
                                Mathématiques / 
                                Economie / 
                                Management / 
                                Marketing / 
                                Comptabilité
                            </li>
                        </ul>
                      </td>
                    </tr>
                  </tbody>
                </table>

                <br>
                <br>

                <table class="table table-bordered table-striped">
                  <thead>
                    <tr>
                      <th>
                        Intitulé : Classes préparatoires aux grandes écoles PTSI-PT
                        <br>
                        Période : Août 2011 - Août 2013 [2 ans]
                        <br>
                        Centre de formation : Lycée Lislet Geoffroy à l'Ile de La Réunion
                      </th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td>
                        <ul>
                            <li>
                                Mathématiques / 
                                Chimie / 
                                Physique / 
                                Technologie / 
                                Sciences de l'ingénieur
                            </li>
                        </ul>
                      </td>
                    </tr>
                  </tbody>
                </table>

                <br>
                <br>

                <table class="table table-bordered table-striped">
                  <thead>
                    <tr>
                      <th>
                        Intitulé : Baccalauréat scientifique
                        <br>
                        Période : Août 2010 - Août 2011 [1 an]
                        <br>
                        Centre de formation : Lycée Roland Garros à l'Ile de La Réunion
                      </th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td>
                        <ul>
                            <li>
                                Sciences de l'ingénieur / 
                                Mathématiques / 
                                Physique / 
                                Chimie / 
                                Anglais / 
                                Français / 
                                Histoire
                            </li>
                        </ul>
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
            <!-- Formations -->

            <br>

        </div>
        <!-- Développeur Python -->
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
            'footer-left': 'Ingénieur en énergies renouvelables',
            'header-center': 'CV de Monsieur ',
        }

        pdfkit.from_string(
            body,
            "Resume_For_Me\\CV_De__[Ingenieur_Energies_Renouvelables].pdf",
            options=options
        )

    # ok
    def test_resume_ouvrier_non_qualifie_manutention(self):
        print('test_resume_ouvrier_non_qualifie_manutention')

        body = """
<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" 
    content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" 
    href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css" 
    integrity="sha384-xOolHFLEh07PJGoPkLv1IbcEPTNtaed2xpHsD9ESMhqIYd0nLMwNLD69Npy4HI+N" 
    crossorigin="anonymous">

    <title>CV de  - Ouvrier non qualifié de manutention</title>
  </head>
  <body>
    <!-- Container -->
    <div class="container">
        <!-- Ouvrier non qualifié de manutention -->
        <div class="card text-center">
          <div class="card-header">
            Ouvrier non qualifié de manutention
          </div>
          <div class="card-body">
            <table class="table table-bordered table-striped">
              <thead>
                <tr>
                  <th scope="col">Identité</th>
                  <th scope="col">Adresse postale</th>
                  <th scope="col">Téléphone</th>
                  <th scope="col">Email</th>
                  <th scope="col">Age</th>
                  <th scope="col">Nationalité</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>Monsieur </td>
                  <td></td>
                  <td></td>
                  <td></td>
                  <td>28 ans</td>
                  <td>Française</td>
                </tr>
              </tbody>
            </table>

            <br>
            <br>

            <!-- Compétences -->
            <div class="card text-center">
              <div class="card-header">
                Compétences
              </div>
              <div class="card-body">
                <ul>
                    <li>
                        Sécuriser le périmètre d'intervention / 
                        Préparer le matériel adapté / 
                        Aménager des zones de stockage
                    </li>
                    <li>
                        Décharger des marchandises, des produits  / 
                        Démolir un élément d'ouvrage
                    </li>
                    <li>
                        Acheminer des marchandises en zone d'expédition, de stockage ou de production
                    </li>
                    <li>
                        Mélanger des produits d'assemblage / 
                        Réaliser et lisser les joints
                    </li>
                    <li>
                        Nettoyer des outils et du matériel de chantier / 
                        Ranger un chantier
                    </li>
                    <li>
                        Couper des éléments de ferraillage / 
                        Passer des gaines de réseaux électriques dans des conduits
                    </li>
                </ul>
              </div>
            </div>
            <!-- Compétences -->

            <br>
            <br>

            <!-- Expériences -->
            <div class="card text-center">
              <div class="card-header">
                Expériences
              </div>
              <div class="card-body">
                <table class="table table-bordered table-striped">
                  <thead>
                    <tr>
                      <th>
                        Intitulé : Ouvrier non qualifié de manutention
                        <br>
                        Période : Mai 2019 – Juin 2022 [3 ans et 1 mois]
                        <br>
                        Statut professionnel : Président
                        <br>
                        Société : Holomorphe - SIREN : 883 632 556 - Paris (75007)
                      </th>
                    </tr>
                  </thead>
                  <tbody>
                    <tbody>
                    <tr>
                      <td>
                        <ul>
                            <li>
                                Gestes et postures de manutention / 
                                Utilisation d'engins de manutention non motorisés (transpalette, diable)
                            </li>
                        </ul>
                      </td>
                    </tr>
                  </tbody>
                </table>

                <br>
                <br>

                <table class="table table-bordered table-striped">
                  <thead>
                    <tr>
                      <th>
                        Intitulé : Ouvrier non qualifié de manutention
                        <br>
                        Période : Octobre 2016 - Avril 2019 [2 ans et 6 mois]
                        <br>
                        Statut professionnel : Auto-entrepreneur
                        <br>
                        Société : Entreprise ALOYAU - SIREN : 823 502 222 - Saint-Ouen (93400)
                      </th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td>
                        <ul>
                            <li>
                                Gestes et postures de manutention / 
                                Utilisation d'engins de manutention non motorisés (transpalette, diable)
                            </li>
                        </ul>
                      </td>
                    </tr>
                  </tbody>
                </table>

                <br>
                <br>

                <table class="table table-bordered table-striped">
                  <thead>
                    <tr>
                      <th>
                        Intitulé : Ouvrier non qualifié de manutention
                        <br>
                        Périodes : Avril 2015 - Juillet 2015 [4 mois] et Février 2016 - Juillet 2016 [6 mois]
                        <br>
                        Statut professionnel : Stagiaire
                        <br>
                        Société : Agronergy - SIREN : 792 570 137 - Paris (75018)
                      </th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td>
                        <ul>
                            <li>
                                Utilisation de marteau-piqueur / 
                                Utilisation de chariot élévateur / 
                                Gestes et postures de manutention / 
                                Utilisation d'engins de manutention non motorisés (transpalette, diable)
                            </li>
                        </ul>
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
            <!-- Expériences -->

            <br>
            <br>

            <!-- Formations -->
            <div class="card text-center">
              <div class="card-header">
                Formations
              </div>
              <div class="card-body">
                <table class="table table-bordered table-striped">
                  <thead>
                    <tr>
                      <th>
                        Intitulé : Diplôme d'ingénieur généraliste
                        <br>
                        Période : Septembre 2013 - Août 2016 [3 ans]
                        <br>
                        Centre de formation : École Supérieure d'Ingénieurs Léonard de Vinci – Paris La Défense
                      </th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td>
                        <ul>
                            <li>
                                Nouvelles énergies / 
                                Informatique / 
                                Finance / 
                                Mécanique numérique
                            </li>
                        </ul>
                      </td>
                    </tr>
                  </tbody>
                </table>

                <br>
                <br>

                <table class="table table-bordered table-striped">
                  <thead>
                    <tr>
                      <th>
                        Intitulé : Classes préparatoires aux grandes écoles PTSI-PT
                        <br>
                        Période : Août 2011 - Août 2013 [2 ans]
                        <br>
                        Centre de formation : Lycée Lislet Geoffroy à l'Ile de La Réunion
                      </th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td>
                        <ul>
                            <li>
                                Mathématiques / 
                                Chimie / 
                                Physique / 
                                Technologie / 
                                Sciences de l'ingénieur
                            </li>
                        </ul>
                      </td>
                    </tr>
                  </tbody>
                </table>

                <br>
                <br>

                <table class="table table-bordered table-striped">
                  <thead>
                    <tr>
                      <th>
                        Intitulé : Baccalauréat scientifique
                        <br>
                        Période : Août 2010 - Août 2011 [1 an]
                        <br>
                        Centre de formation : Lycée Roland Garros à l'Ile de La Réunion
                      </th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td>
                        <ul>
                            <li>
                                Sciences de l'ingénieur / 
                                Mathématiques / 
                                Physique / 
                                Chimie / 
                                Anglais / 
                                Français / 
                                Histoire
                            </li>
                        </ul>
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
            <!-- Formations -->

            <br>

        </div>
        <!-- Développeur Python -->
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
            'footer-left': 'Ouvrier non qualifié de manutention',
            'header-center': 'CV de Monsieur ',
        }

        pdfkit.from_string(
            body,
            "Resume_For_Me\\CV_De__[Ouvrier_Non_Qualifie_De_Manutention].pdf",
            options=options
        )

    # ok
    def test_resume_formateur(self):
        print('test_resume_formateur')

        body = """
<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" 
    content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" 
    href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css" 
    integrity="sha384-xOolHFLEh07PJGoPkLv1IbcEPTNtaed2xpHsD9ESMhqIYd0nLMwNLD69Npy4HI+N" 
    crossorigin="anonymous">

    <title>CV de  - Formateur</title>
  </head>
  <body>
    <!-- Container -->
    <div class="container">
        <!-- Formateur -->
        <div class="card text-center">
          <div class="card-header">
            Formateur
          </div>
          <div class="card-body">
            <table class="table table-bordered table-striped">
              <thead>
                <tr>
                  <th scope="col">Identité</th>
                  <th scope="col">Adresse postale</th>
                  <th scope="col">Téléphone</th>
                  <th scope="col">Email</th>
                  <th scope="col">Age</th>
                  <th scope="col">Nationalité</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>Monsieur </td>
                  <td></td>
                  <td></td>
                  <td></td>
                  <td>28 ans</td>
                  <td>Française</td>
                </tr>
              </tbody>
            </table>

            <br>
            <br>

            <!-- Compétences -->
            <div class="card text-center">
              <div class="card-header">
                Compétences
              </div>
              <div class="card-body">
                <ul>
                    <li>
                        Définir les méthodes et outils pédagogiques d'une formation / 
                        Concevoir des modules de formation
                    </li>
                    <li>
                        Présenter et promouvoir une formation / 
                        Accueillir les personnes / 
                        Animer une formation
                    </li>
                    <li>
                        Évaluer le travail d'un stagiaire / 
                        Rechercher des financements, des partenariats  / 
                        Conduire un atelier de formation
                    </li>
                    <li>
                        Réaliser un bilan de compétences / 
                        Négocier un contrat / 
                        Sélectionner des fournisseurs, sous-traitants, prestataires
                    </li>
                </ul>
              </div>
            </div>
            <!-- Compétences -->

            <br>
            <br>

            <!-- Expériences -->
            <div class="card text-center">
              <div class="card-header">
                Expériences
              </div>
              <div class="card-body">
                <table class="table table-bordered table-striped">
                  <thead>
                    <tr>
                      <th>
                        Intitulé : Formateur
                        <br>
                        Période : Mai 2019 – Juin 2022 [3 ans et 1 mois]
                        <br>
                        Statut professionnel : Président
                        <br>
                        Société : Holomorphe - SIREN : 883 632 556 - Paris (75007)
                      </th>
                    </tr>
                  </thead>
                  <tbody>
                    <tbody>
                    <tr>
                      <td>
                        <ul>
                            <li>
                                Marché de l'emploi / 
                                Outils bureautiques / 
                                Outils multimédia / 
                                Technologies de l'information et de la communication (TIC)
                            </li>
                            <li>
                                Techniques de vente / 
                                Techniques commerciales / 
                                Electricité / 
                                Équipements de télécommunication
                            </li>
                            <li>
                                Informatique / 
                                Mécanique / 
                                Management / 
                                Marketing
                            </li>
                            <li>
                                Sciences de l'ingénieur / 
                                Mathématiques / 
                                Physiques / 
                                Energie
                            </li>
                            <li>
                                Finance / 
                                Commerce / 
                                Droit (Fiscal, Social, Environnement, Energie, Travail)
                            </li>
                        </ul>
                      </td>
                    </tr>
                  </tbody>
                </table>

                <br>
                <br>

                <table class="table table-bordered table-striped">
                  <thead>
                    <tr>
                      <th>
                        Intitulé : Formateur
                        <br>
                        Période : Octobre 2016 - Avril 2019 [2 ans et 6 mois]
                        <br>
                        Statut professionnel : Auto-entrepreneur
                        <br>
                        Société : Entreprise ALOYAU - SIREN : 823 502 222 - Saint-Ouen (93400)
                      </th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td>
                        <ul>
                            <li>
                                Marché de l'emploi / 
                                Outils bureautiques / 
                                Outils multimédia / 
                                Technologies de l'information et de la communication (TIC)
                            </li>
                            <li>
                                Techniques de vente / 
                                Techniques commerciales / 
                                Electricité / 
                                Équipements de télécommunication
                            </li>
                            <li>
                                Informatique / 
                                Mécanique / 
                                Management / 
                                Marketing
                            </li>
                            <li>
                                Sciences de l'ingénieur / 
                                Mathématiques / 
                                Physiques / 
                                Energie
                            </li>
                            <li>
                                Finance / 
                                Commerce / 
                                Droit (Fiscal, Social, Environnement, Energie, Travail)
                            </li>
                        </ul>
                      </td>
                    </tr>
                  </tbody>
                </table>

                <br>
                
              </div>
            </div>
            <!-- Expériences -->

            <br>
            <br>

            <!-- Formations -->
            <div class="card text-center">
              <div class="card-header">
                Formations
              </div>
              <div class="card-body">
                <table class="table table-bordered table-striped">
                  <thead>
                    <tr>
                      <th>
                        Intitulé : Diplôme d'ingénieur généraliste
                        <br>
                        Période : Septembre 2013 - Août 2016 [3 ans]
                        <br>
                        Centre de formation : École Supérieure d'Ingénieurs Léonard de Vinci – Paris La Défense
                      </th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td>
                        <ul>
                            <li>
                                Nouvelles énergies / 
                                Informatique / 
                                Finance / 
                                Mécanique numérique
                            </li>
                        </ul>
                      </td>
                    </tr>
                  </tbody>
                </table>

                <br>
                <br>

                <table class="table table-bordered table-striped">
                  <thead>
                    <tr>
                      <th>
                        Intitulé : Classes préparatoires aux grandes écoles PTSI-PT
                        <br>
                        Période : Août 2011 - Août 2013 [2 ans]
                        <br>
                        Centre de formation : Lycée Lislet Geoffroy à l'Ile de La Réunion
                      </th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td>
                        <ul>
                            <li>
                                Mathématiques / 
                                Chimie / 
                                Physique / 
                                Technologie / 
                                Sciences de l'ingénieur
                            </li>
                        </ul>
                      </td>
                    </tr>
                  </tbody>
                </table>

                <br>
                <br>

                <table class="table table-bordered table-striped">
                  <thead>
                    <tr>
                      <th>
                        Intitulé : Baccalauréat scientifique
                        <br>
                        Période : Août 2010 - Août 2011 [1 an]
                        <br>
                        Centre de formation : Lycée Roland Garros à l'Ile de La Réunion
                      </th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td>
                        <ul>
                            <li>
                                Sciences de l'ingénieur / 
                                Mathématiques / 
                                Physique / 
                                Chimie / 
                                Anglais / 
                                Français / 
                                Histoire
                            </li>
                        </ul>
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
            <!-- Formations -->

            <br>

        </div>
        <!-- Formateur -->
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
            'footer-left': 'Formateur',
            'header-center': 'CV de Monsieur ',
        }

        pdfkit.from_string(
            body,
            "/home/pop/Dropbox/1_Personnel/1_Recurrentes/3_Outils_Numeriques/GitHub/Cristal_Ball/Archives/Reporting"
            "/Human_Resources/Resume/Resume_For_Me/CV_De__[Formateur].pdf",
            options=options
        )


if __name__ == '__main__':
    unittest.main()
