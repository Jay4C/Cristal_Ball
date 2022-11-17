import unittest
import pdfkit
from PyPDF2 import PdfFileWriter, PdfFileReader


class UnitTestsDemandeAutorisationExploiterInstallationProductionElectricitePassTechParis(unittest.TestCase):
    # ok
    def test_demande_autorisation_exploiter_installation_production_electricite_pass_tech(self):
        print("test_demande_autorisation_exploiter_installation_production_electricite_pass_tech")

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
                Demande d'autorisation d'exploiter une installation de production d'électricité
            </title>
          </head>
          <body>
            <!-- container -->
            <div class="container">

                <br>
                
                <!-- Informations générales de la société Holomorphe -->
                <div class="card text-center">
                  <div class="card-header">
                    Informations générales du pétitionnaire
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
                    Contact du pétitionnaire
                  </div>
                  <div class="card-body">
                    <!-- Informations personnelles -->
                    <table class="table table-striped table-bordered">
                        <thead>
                            <tr>
                                <th scope="col">Personne à contacter</th>
                                <th scope="col">Adresse du siège social</th>
                                <th scope="col">Téléphone</th>
                                <th scope="col">Email</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>
                                    
                                </td>
                                <td>
                                    31 Avenue de Ségur 75007 Paris
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
                <!-- Contact -->
                
                <br>

                <!-- Destinataire -->
                <div class="card text-center">
                  <div class="card-header">
                    Destinataire
                  </div>
                  <div class="card-body">
                    Bureau des réseaux électriques et de la réglementation de l’énergie
                    <br>
                    Direction générale de l’énergie et du climat
                    <br>
                    Ministère de l’environnement, de l’énergie et de la mer
                    <br>
                    Tour Séquoia
                    <br>
                    92055 La Défense Cedex
                  </div>
                </div>
                <!-- Destinataire -->
                
                <br>
                
                <!-- Objet -->
                <div class="card text-center">
                  <div class="card-header">
                    Objet
                  </div>
                  <div class="card-body">
                    Demande d'autorisation d'exploiter une installation de production d'électricité en utilisant 
                    l'énergie potentielle de pesanteur avec une machine gravitationnelle
                  </div>
                </div>
                <!-- Objet -->
                
                <br>
                
                <!-- Message -->
                <div class="card text-center">
                  <div class="card-header">
                    Message
                  </div>
                  <div class="card-body">
                    Bonjour,
                    <br>
                    <br>
                    Vu les articles L311-5 à L311-9 du code de l'énergie concernant l'autorisation d'exploiter 
                    une installation de production d'électricité,
                    <br>
                    Vu les articles R311-1 à R311-11-1 du code de l'énergie concernant l'autorisation d'exploiter 
                    une installation de production d'électricité,
                    <br>
                    Vu le code de l'environnement,
                    <br>
                    Vu le code de la propriété intellectuelle,
                    
                    <br>
                    <br>
                    
                    Conformément à l'article R311-5 du code de l'énergie, cette demande d'autorisation d'exploiter 
                    une installation de production d'électricité en utilisant l'énergie potentielle de pesanteur 
                    avec une machine gravitationnelle est adressée au ministre chargé de l'énergie par le 
                    pétitionnaire en un seul exemplaire.
                    
                    <br>
                    <br>
                    
                    Les informations nécessaires à l'instruction de cette demande d'autorisation d'exploiter 
                    une installation de production d'électricité en utilisant l'énergie potentielle de pesanteur 
                    avec une machine gravitationnelle sont détaillées ci-après.
                    
                    <br>
                    <br>
                    
                    <!-- Note précisant les capacités techniques, économiques et financières du pétitionnaire -->
                    <div class="card text-center">
                      <div class="card-header">
                        Note précisant les capacités techniques, économiques et financières du pétitionnaire
                      </div>
                      <div class="card-body">
                        <!-- Capacités techniques -->
                        <div class="card text-center">
                          <div class="card-header">
                            Capacités techniques
                          </div>
                          <div class="card-body">
                            Le pétitionnaire exécute seul ses travaux, et éventuellement en compagnie de ses 
                            éventuels partenaires.
                            <br>
                            <br>
                            Après, le pétitionnaire posséde en général les moyens matériels suivants pour effectuer 
                            ses travaux :
                            <br>
                            - Un ordinateur portable équipé de plusieurs logiciels applicatifs spécifiques pour 
                            l'ingénierie.
                            <br>
                            - Un diable de manutention pouvant supporter une charge de 250 kilogrammes équipé de roues 
                            increvables.
                            <br>
                            - Une cantine métallique de 100 centimètres pouvant être installée sur un diable de 
                            manutention.
                            <br>
                            - Une perceuse pour percer des matériaux et visser des vis.
                            <br>
                            - Une scie sauteuse pour couper des matérieux (bois, métal ...).
                            <br>
                            - Plusieurs forêts pour le perçage de différents types de matériaux (bois, métal ...).
                            <br>
                            - Plusieurs clés plates.
                            <br>
                            - Plusieurs clés à douille.
                            <br>
                            - Plusieurs embouts de vissage.
                            <br>
                            - Plusieurs clés Allen.
                            <br>
                            - Plusieurs palettes de manutention.
                            <br>
                            - Plusieurs rallonges électriques.
                            <br>
                            - Un mètre.
                            <br>
                            - Plusieurs cordes de manutention.
                          </div>
                        </div>
                        <!-- Capacités techniques -->
                        
                        <br>
                        
                        <!-- Capacités économiques -->
                        <div class="card text-center">
                          <div class="card-header">
                            Capacités économiques
                          </div>
                          <div class="card-body">
                            L'immatriculation du pétitionnaire date depuis le 26 mai 2020.
                            <br>
                            Durant l'année 2020 et l'année 2021, le pétitionnaire n'a pas réalisé de chiffre d'affaires.
                          </div>
                        </div>
                        <!-- Capacités économiques -->
                        
                        <br>
                        
                        <!-- Capacités financières -->
                        <div class="card text-center">
                          <div class="card-header">
                            Capacités financières
                          </div>
                          <div class="card-body">
                            Le pétitionnaire finance ses projets en utilisant les moyens financiers suivants :
                            <br>
                            - Ses fonds propres.
                            <br>
                            - Les apports en compte courant d'associé.
                            <br>
                            - Les apports en nature.
                            <br>
                            - Les prêts bancaires octroyés auprès d'établissements financiers.
                            <br>
                            - Les subventions d'investissement.
                            <br>
                            - Les subventions d'exploitation.
                          </div>
                        </div>
                        <!-- Capacités financières -->
                      </div>
                    </div>
                    <!-- Note précisant les capacités techniques, économiques et financières du pétitionnaire -->
                    
                    <br>
                    
                    <!-- Caractéristiques principales de l'installation de production -->
                    <div class="card text-center">
                      <div class="card-header">
                        Caractéristiques principales de l'installation de production
                      </div>
                      <div class="card-body">
                        <!-- Capacité de production -->
                        <div class="card text-center">
                          <div class="card-header">
                            Capacité de production
                          </div>
                          <div class="card-body">
                            La capacité de production d'électricité de cette installation est égale à dix kilowatts.
                          </div>
                        </div>
                        <!-- Capacité de production -->
                        
                        <br>
                        
                        <!-- Energies primaires -->
                        <div class="card text-center">
                          <div class="card-header">
                            Energies primaires
                          </div>
                          <div class="card-body">
                            Les énergies primaires de cette installation de production d'électricité sont les 
                            suivantes :
                            <br>
                            - Energie électrique provenant de batteries électriques pour amorcer un moteur électrique.
                            <br>
                            - Energie potentielle de pesanteur provenant d'un volant d'inertie dont sa masse est 
                            complètement répartie sur son extrémité et son axe de rotation est perpendiculaire 
                            au champ de pesanteur.
                          </div>
                        </div>
                        <!-- Energies primaires -->
                        
                        <br>
                        
                        <!-- Techniques de production utilisées -->
                        <div class="card text-center">
                          <div class="card-header">
                            Technique de production utilisée
                          </div>
                          <div class="card-body">
                            La technique de production d'électricité utilisée par cette installation se base sur 
                            la création d'une machine gravitationnelle extrayant de l'énergie potentielle de 
                            pesanteur dû aux dimensionnements spécifiques de son volant d'inertie.
                            <br>
                            <br>
                            Après, cette machine gravitationnelle est composée des éléments suivants :
                            <br>
                            - Une batterie électrique.
                            <br>
                            - Un moteur électrique.
                            <br>
                            - Un volant d'inertie.
                            <br>
                            - Un générateur électrique.
                            <br>
                            - Un socle.
                            <br>
                            - Plusieurs poulies.
                            <br>
                            - Plusieurs courroies.
                            <br>
                            - Plusieurs paliers à roulements à billes.
                            <br>
                            - Plusieurs équipements électriques (interrupteurs, disjoncteur, régulateur ...).
                            <br>
                            - Plusieurs équipements mécaniques (tige filetée, rondelles, écrous, vis ...).
                            <br>
                            <br>
                            Puis, cette machine gravitationnelle est construite en suivant les idées publiées par les 
                            inventions tombées dans le domaine public qui sont les suivantes : 
                            <br>
                            - Brevet FR2717240A1 intitulé "Dispositif de transmission d’énergie gravitationnelle à 
                            un système de production d’énergie mécanique ou électrique" dont l'inventeur est Poirier 
                            Gerard Francois Pierre.
                            <br>
                            - Brevet FR2461125A1 intitulé "Moteur gravitationnel produisant de l’énergie en utilisant 
                            des poids déséquilibrés glissant sur des supports radiaux pour créer un mouvement 
                            rotatif perpétuel" dont l'inventeur est Piens Marc.
                            <br>
                            - Brevet WO1982004174A2 intitulé "Mouvement perpétuel" dont l'inventeur est Johann dit 
                            Jean Schyns.
                            <br>
                            - Brevet US3625089A intitulé "Appareil à roue gravitationnelle" dont l'inventeur est 
                            Edward Rutkove.
                            <br>
                            <br> 
                            Ensuite, cette machine gravitationnelle suit la théorie de Lawrence Chun Ning Tseung, 
                            la loi de la conservation de l'énergie et la théorie sur l'énergie mécanique du pendule 
                            simple.
                            <br>
                            <br>
                            De plus, il y a plusieurs dessins de cette machine gravitationnelle qui sont joints 
                            en annexe de cette demande d'autorisation d'exploiter une installation de production 
                            d'électricité.
                          </div>
                        </div>
                        <!-- Techniques de production utilisées -->
                        
                        <br>
                        
                        <!-- Rendements énergétiques -->
                        <div class="card text-center">
                          <div class="card-header">
                            Rendement énergétique
                          </div>
                          <div class="card-body">
                            Le rendement énergétique de cette installation de production d'électricité est inférieur à 
                            quatre-vingt-dix pour cent.
                          </div>
                        </div>
                        <!-- Rendements énergétiques -->
                        
                        <br>
                        
                        <!-- Durées de fonctionnement -->
                        <div class="card text-center">
                          <div class="card-header">
                            Durées de fonctionnement
                          </div>
                          <div class="card-body">
                            Les durées de fonctionnement en base, en semi-base et en pointe de cette installation de 
                            production d'électricité sont illimitées, sans prendre en compte la durée des éventuelles 
                            maintenances.
                          </div>
                        </div>
                        <!-- Durées de fonctionnement -->
                        
                        <br>
                        
                        <!-- Quantité de gaz à effet de serre émise par cette installation -->
                        <div class="card text-center">
                          <div class="card-header">
                            Quantité de gaz à effet de serre émise par cette installation
                          </div>
                          <div class="card-body">
                            Conformément aux articles L229-1 à L229-69 et D229-1 à R229-105 du code de 
                            l'environnement, la quantité de gaz à effet de serre émise par cette installation 
                            de production d'électricité est égale à zéro gramme.
                          </div>
                        </div>
                        <!-- Quantité de gaz à effet de serre émise par cette installation -->
                      </div>
                    </div>
                    <!-- Caractéristiques principales de l'installation de production -->
                    
                    <br>
                    
                    <!-- Localisation de l'installation de production -->
                    <div class="card text-center">
                      <div class="card-header">
                        Localisation de l'installation de production
                      </div>
                      <div class="card-body">
                        La localisation de l'installation de production d'électricité sera située à l'adresse suivante :
                        <br>
                        Pass Technologie SARL
                        <br>
                        26 Rue Louis Braille 75012 Paris
                      </div>
                    </div>
                    <!-- Localisation de l'installation de production -->
                    
                    <br>
                    
                    <!-- Note relative à l'efficacité énergétique de l'installation comparée aux meilleures 
                    techniques disponibles à un coût économiquement acceptable -->
                    <div class="card text-center">
                      <div class="card-header">
                        Note relative à l'efficacité énergétique de l'installation comparée aux meilleures 
                        techniques disponibles à un coût économiquement acceptable
                      </div>
                      <div class="card-body">
                        Vu les articles L100-1 A à L100-5 du code de l'énergie concernant les objectifs de la 
                        politique énergétique nationale pour répondre à l'urgence écologique et climatique,
                        <br>
                        Vu la directive 2012/27/UE du Parlement européen et du Conseil du 25 octobre 2012 
                        relative à l'efficacité énergétique, modifiant les directives 2009/125/CE et 2010/30/UE et 
                        abrogeant les directives 2004/8/CE et 2006/32/CE,
                        <br>
                        Vu le règlement (UE) 2017/1938 du Parlement européen et du Conseil du 25 octobre 2017 
                        concernant des mesures visant à garantir la sécurité de l'approvisionnement en gaz 
                        naturel et abrogeant le règlement (UE) n° 994/2010,
                        <br>
                        Vu le protocole de Kyoto visant à la réduction des émissions de gaz à effet de serre,
                        <br>
                        Vu l'accord de Paris sur le climat concernant l'atténuation et l'adaptation au changement 
                        climatique,
                        <br>
                        <br>
                        Conformément aux objectifs d'efficacité énergétique, à la sécurité d'approvisionnement 
                        énergétique et à la lutte contre le réchauffement climatique dictés par certaines directives 
                        de l'Union européenne et certains accords internationaux, cette installation de production 
                        d'électricité présente des avantages significatives en matière d'efficacité énergétique, de la 
                        sécurité d'apprivisionnement énergétique et de la contribution à la lutte contre le 
                        réchauffement climatique énoncés par les points suivants :
                        <br>
                        - Aucune émission de gaz à effet de serre.
                        <br>
                        - Aucune consommation énergétique primaire fossile.
                        <br>
                        - Utilisation d'une énergie renouvelable provenant de l'énergie potentielle de pesanteur 
                        disponible sans interruption, de jour comme de nuit.
                        <br>
                        - Capacité de maintenir une autonomie énergétique dans les départements d'outre-mer.
                        <br>
                        - Capacité de favoriser l'émergence d'une économie compétitive et riche en emplois grâce 
                        à la mobilisation de toutes les filières industrielles, notamment celles de la croissance 
                        verte qui se définit comme un mode de développement économique respectueux de l'environnement, 
                        à la fois sobre et efficace en énergie et en consommation de ressources et de carbone, 
                        socialement inclusif, soutenant le potentiel d'innovation et garant de la compétitivité des 
                        entreprises.
                        <br>
                        - Capacité d'assurer la sécurité d'approvisionnement et de réduire la dépendance aux 
                        importations d'énergies fossiles.
                        <br>
                        - Capacité de préserver la santé humaine et l'environnement, en particulier en luttant 
                        contre l'aggravation de l'effet de serre et contre les risques industriels majeurs, 
                        en réduisant l'exposition des citoyens à la pollution de l'air.
                        <br>
                        - Capacité de garantir la cohésion sociale et territoriale en assurant un droit d'accès 
                        de tous les ménages à l'énergie sans coût excessif au regard de leurs ressources.
                        <br>
                        - Capacité de lutter contre la précarité énergétique.
                        <br>
                        - Capacité de contribuer à la mise en place d'une Union européenne de l'énergie, 
                        qui vise à garantir la sécurité d'approvisionnement et à construire une économie 
                        décarbonée et compétitive, au moyen du développement des énergies renouvelables, 
                        des interconnexions physiques, des moyens de flexibilité du système électrique, 
                        du soutien à l'amélioration de l'efficacité énergétique et de la mise en place 
                        d'instruments de coordination des politiques nationales.
                      </div>
                    </div>
                    <!-- Note relative à l'efficacité énergétique de l'installation comparée aux meilleures 
                    techniques disponibles à un coût économiquement acceptable -->
                    
                    <br>
                    
                    <!-- Destination prévue de l'électricité produite -->
                    <div class="card text-center">
                      <div class="card-header">
                        Destination prévue de l'électricité produite
                      </div>
                      <div class="card-body">
                        Vu les articles L315-1 à L315-8 du code de l'énergie concernant l'autoconsommation vis-à-vis 
                        des dispositions relatives à la production d'électricité,
                        <br>
                        Vu les articles D315-1 à R315-16 du code de l'énergie concernant l'autoconsommation vis-à-vis 
                        des dispositions relatives à la production d'électricité,
                        <br>
                        <br>
                        Conformément à l'article L315-1 du code de l'énergie, la destination prévue de l'électricité 
                        produite est destinée pour une opération d'autoconsommation individuelle pour les besoins 
                        propres du pétitionnaire et de son client par le biais d'une convention de mise à disposition 
                        de matériels.
                      </div>
                    </div>
                    <!-- Destination prévue de l'électricité produite -->
                    
                    <br>
                    
                    Dans l'attente de votre décision, je vous prie d'agréer, l'expression de mes sincères salutations.
                    
                    <br>
                    
                    Monsieur 
                  </div>
                </div>
                <!-- Message -->
                
                <br>
                
                <!-- Lieu, date et signature -->
                <div class="card text-center">
                  <div class="card-header">
                    Lieu, date et signature du pétitionnaire
                  </div>
                  <div class="card-body">
                    Fait à Paris, le 07 Mars 2022.
                    <br>
                    <br>
                    <br>
                    <br>
                    <br>
                    <br>
                    <br>
                  </div>
                </div>
                <!-- Lieu, date et signature -->
            </div>
            <!-- container -->
            
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
            'header-center': "Demande d'autorisation d'exploiter une installation de production d'électricité",
            'footer-right': '[page] sur [topage]',
            'footer-left': 'S.A.S.U.A.C.V. Holomorphe [SIREN : 883632556]'
        }

        path_wkthmltopdf = "C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe"
        config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
        pdfkit.from_string(body,
                           "Pass_Tech"
                           "\\Demande_Autorisation_Exploter_I_P_E_[SASU_Holomorphe].pdf",
                           configuration=config,
                           options=options)

    # ok
    def test_dossier_demande_autorisation_exploiter_installation_production_electricite_pass_tech(self):
        print("test_dossier_demande_autorisation_exploiter_installation_production_electricite_pass_tech")

        location = "Pass_Tech"

        output = PdfFileWriter()

        # demande_a_e_i_p_e_pass_tech
        demande_a_e_i_p_e_pass_tech = "A:\\1_Professionnel\\1_Holomorphe\\2_Archives\\2_Outils_Numeriques" \
                                      "\\Python__Flask__Cristal_Ball\\Test\\Service\\Archives\\Reporting" \
                                      "\\Corporate_Reporting\\Demarches_Administratives\\Autorisation_E_P_E" \
                                      "\\" + str(location) + \
                                      "\\Demande_Autorisation_Exploter_I_P_E_[SASU_Holomorphe].pdf"

        demande_a_e_i_p_e_pass_tech_pdf = PdfFileReader(open(demande_a_e_i_p_e_pass_tech, "rb"))

        for i in range(0, demande_a_e_i_p_e_pass_tech_pdf.getNumPages()):
            output.addPage(demande_a_e_i_p_e_pass_tech_pdf.getPage(i))

        # isometric
        isometric = "A:\\1_Professionnel\\1_Holomorphe\\2_Archives\\2_Outils_Numeriques" \
                      "\\Python__Flask__Cristal_Ball\\Test\\Service\\Archives\\Reporting" \
                      "\\Corporate_Reporting\\Demarches_Administratives\\Autorisation_E_P_E" \
                      "\\" + str(location) + "\\Isometric.pdf"

        isometric_pdf = PdfFileReader(open(isometric, "rb"))

        for i in range(0, isometric_pdf.getNumPages()):
            output.addPage(isometric_pdf.getPage(i))

        # face
        face = "A:\\1_Professionnel\\1_Holomorphe\\2_Archives\\2_Outils_Numeriques" \
              "\\Python__Flask__Cristal_Ball\\Test\\Service\\Archives\\Reporting" \
              "\\Corporate_Reporting\\Demarches_Administratives\\Autorisation_E_P_E" \
              "\\" + str(location) + "\\Face.pdf"

        face_pdf = PdfFileReader(open(face, "rb"))

        for i in range(0, face_pdf.getNumPages()):
            output.addPage(face_pdf.getPage(i))

        # droite
        droite = "A:\\1_Professionnel\\1_Holomorphe\\2_Archives\\2_Outils_Numeriques" \
              "\\Python__Flask__Cristal_Ball\\Test\\Service\\Archives\\Reporting" \
              "\\Corporate_Reporting\\Demarches_Administratives\\Autorisation_E_P_E" \
              "\\" + str(location) + "\\Droite.pdf"

        droite_pdf = PdfFileReader(open(droite, "rb"))

        for i in range(0, droite_pdf.getNumPages()):
            output.addPage(droite_pdf.getPage(i))

        # gauche
        gauche = "A:\\1_Professionnel\\1_Holomorphe\\2_Archives\\2_Outils_Numeriques" \
              "\\Python__Flask__Cristal_Ball\\Test\\Service\\Archives\\Reporting" \
              "\\Corporate_Reporting\\Demarches_Administratives\\Autorisation_E_P_E" \
              "\\" + str(location) + "\\Gauche.pdf"

        gauche_pdf = PdfFileReader(open(gauche, "rb"))

        for i in range(0, gauche_pdf.getNumPages()):
            output.addPage(gauche_pdf.getPage(i))

        # dessus
        dessus = "A:\\1_Professionnel\\1_Holomorphe\\2_Archives\\2_Outils_Numeriques" \
              "\\Python__Flask__Cristal_Ball\\Test\\Service\\Archives\\Reporting" \
              "\\Corporate_Reporting\\Demarches_Administratives\\Autorisation_E_P_E" \
              "\\" + str(location) + "\\Dessus.pdf"

        dessus_pdf = PdfFileReader(open(dessus, "rb"))

        for i in range(0, dessus_pdf.getNumPages()):
            output.addPage(dessus_pdf.getPage(i))

        # dessous
        dessous = "A:\\1_Professionnel\\1_Holomorphe\\2_Archives\\2_Outils_Numeriques" \
              "\\Python__Flask__Cristal_Ball\\Test\\Service\\Archives\\Reporting" \
              "\\Corporate_Reporting\\Demarches_Administratives\\Autorisation_E_P_E" \
              "\\" + str(location) + "\\Dessous.pdf"

        dessous_pdf = PdfFileReader( open(dessous, "rb"))

        for i in range(0, dessous_pdf.getNumPages()):
            output.addPage(dessous_pdf.getPage(i))

        # arriere
        arriere = "A:\\1_Professionnel\\1_Holomorphe\\2_Archives\\2_Outils_Numeriques" \
              "\\Python__Flask__Cristal_Ball\\Test\\Service\\Archives\\Reporting" \
              "\\Corporate_Reporting\\Demarches_Administratives\\Autorisation_E_P_E" \
              "\\" + str(location) + "\\Arriere.pdf"

        arriere_pdf = PdfFileReader(open(arriere, "rb"))

        for i in range(0, arriere_pdf.getNumPages()):
            output.addPage(arriere_pdf.getPage(i))

        # finally, write "output" to a real file
        file_location = "A:\\1_Professionnel\\1_Holomorphe\\2_Archives\\2_Outils_Numeriques" \
              "\\Python__Flask__Cristal_Ball\\Test\\Service\\Archives\\Reporting" \
              "\\Corporate_Reporting\\Demarches_Administratives\\Autorisation_E_P_E" \
              "\\" + str(location)
        output_stream = open(file_location
                             + "\\Dossier_D_A_E_I_P_E_[Holomorphe]_["
                             + str(location) + "]" + ".pdf", "wb")
        output.write(output_stream)
        output_stream.close()


if __name__ == '__main__':
    unittest.main()
