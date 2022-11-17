import unittest
import pdfkit


class UnitTestsFabrication(unittest.TestCase):
    def test_cahier_des_charges_travaux_fabrication_vic(self):
        print("test_cahier_des_charges_travaux_fabrication_vic")

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
                Cahier des charges de fabrication de transformateurs VIC
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
                                <th scope="col">
                                    Personne à contacter
                                </th>
                                <th scope="col">
                                    Adresse du siège social
                                </th>
                                <th scope="col">
                                    Téléphone
                                </th>
                                <th scope="col">
                                    E-mail professionnel
                                </th>
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
                    Objectif des travaux de fabrication de transformateurs du Voltage Intensifier Circuit (VIC)
                  </div>
                  <div class="card-body">
                    L'objectif des travaux de fabrication des transformateurs du Voltage Intensifier Circuit (VIC) 
                    est de fabriquer deux transformateurs dont la carcasse des transformateurs est en plastique nylon 
                    avec un diamètre extérieur maximal de 35 millimètres, une longueur maximale égale à 80 millimètres 
                    et un perçage de 10 millimètres de diamètre situé au centre de la carcasse et sur long de la 
                    longueur de la carcasse.
                  </div>
                </div>
                
                <br>

                <div class="card text-center">
                  <div class="card-header">
                    Tâches à accomplir
                  </div>
                  <div class="card-body">
                    La carcasse des deux transformateurs devra être fabriquée en plastique de type nylon PA12 
                    (https://www.sculpteo.com/fr/materiaux/materiaux-sls/materiau-plastique/) avec la conception de la 
                    pièce mécanique fournie en pièce jointe nommée "part_squelette_d35_l80_v1.stl" avec ce cahier 
                    des charges.
                      
                    <br>
                    <br>
                      
                    Les deux noyaux de bobinage de chaque carcasse possèdent un diamètre égal à 26 millimètres et 
                    une longueur égale à 37 millimètres.
                      
                    <br>
                    <br>
                    
                    Les fils devant être utilisés pour les bobinages seront des fils de cuivre émaillés 
                    (https://fr.rs-online.com/web/p/fils-de-cuivre/0357744).
                    
                    <br>
                    <br>
                    
                    Ces fils de cuivre émaillés devront être de type AWG 24 dont le diamètre est égal à 0.511 
                    millimètre, le nombre de spires par centimètre est égal à 19.60, la section est égale à 0.205
                    millimètres carrés et la résistance linéique est égale à 84.20 ohms par kilomètre.
                    
                    <br>
                    <br>
                    
                    Les deux transformateurs seront communément nommés le transformateur VIC_T1 et le transformateur 
                    VIC_T2.
                    
                    <br>
                    <br>
                    
                    La distance entre la pointe des fils de bobinages de chaque enroulement et le centre de la carcasse 
                    devra être égale 10 centimètres pour faciliter les branchements électriques et 
                    électroniques avec ces transformateurs.
                    
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
                                    Enrouler 200 tours de fils de cuivre émaillés de type AWG 24 sur le primaire du 
                                    transformateur VIC_T1 pouvant supporter une tension pouvant atteindre plusieurs 
                                    milliers de volts et une fréquence pouvant atteindre plusieurs milliers de hertzs 
                                    sur une durée indéterminée.
                                </td>
                            </tr>
                            <tr>
                                <td>
                                    2
                                </td>
                                <td>
                                    Enrouler 600 tours de fils de cuivre émaillés de type AWG 24 sur le secondaire du 
                                    transformateur VIC_T1 pouvant supporter une tension pouvant atteindre plusieurs 
                                    milliers de volts et une fréquence pouvant atteindre plusieurs milliers de hertzs 
                                    sur une durée indéterminée.
                                </td>
                            </tr>
                            <tr>
                                <td>
                                    3
                                </td>
                                <td>
                                    Enrouler 100 tours de fils de cuivre émaillés de type AWG 24 sur le primaire du 
                                    transformateur VIC_T2 pouvant supporter une tension pouvant atteindre plusieurs 
                                    milliers de volts et une fréquence pouvant atteindre plusieurs milliers de hertzs 
                                    sur une durée indéterminée.
                                </td>
                            </tr>
                            <tr>
                                <td>
                                    4
                                </td>
                                <td>
                                    Enrouler 100 tours de fils de cuivre émaillés de type AWG 24 sur le secondaire du 
                                    transformateur VIC_T2 pouvant supporter une tension pouvant atteindre plusieurs 
                                    milliers de volts et une fréquence pouvant atteindre plusieurs milliers de hertzs 
                                    sur une durée indéterminée.
                                </td>
                            </tr>
                            <tr>
                                <td>
                                    5
                                </td>
                                <td>
                                    Tester le fonctionnement du transformateur VIC_T1 avec une tension d'entrée au 
                                    primaire égale à 230 volts et 60 hertz en courant alternatif afin d'atteindre 
                                    une tension de sortie au secondaire égale à 690 volts et 60 hertz en courant 
                                    alternatif.
                                </td>
                            </tr>
                            <tr>
                                <td>
                                    6
                                </td>
                                <td>
                                    Tester le fonctionnement du transformateur VIC_T1 avec une tension d'entrée au 
                                    primaire égale à 230 volts et 10 kilohertz en courant alternatif afin d'atteindre 
                                    une tension de sortie au secondaire égale à 690 volts et 10 kilohertz en courant 
                                    alternatif.
                                </td>
                            </tr>
                            <tr>
                                <td>
                                    7
                                </td>
                                <td>
                                    Tester le fonctionnement du transformateur VIC_T1 avec une tension d'entrée au 
                                    primaire égale à 230 volts et 60 hertz en courant continu pulsé uniquement 
                                    positif afin d'atteindre une tension de sortie au secondaire égale à 690 volts et 
                                    60 hertz en courant continu pulsé uniquement positif.
                                </td>
                            </tr>
                            <tr>
                                <td>
                                    8
                                </td>
                                <td>
                                    Tester le fonctionnement du transformateur VIC_T1 avec une tension d'entrée au 
                                    primaire égale à 230 volts et 10 kilohertz en courant continu pulsé uniquement 
                                    positif afin d'atteindre une tension de sortie au secondaire égale à 690 volts et 
                                    10 kilohertz en courant continu pulsé uniquement positif.
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
                        <a href="https://holomorphe.com" 
                        class="list-group-item list-group-item-action">
                            Société Holomorphe
                        </a>
                        <a href="https://patents.google.com/patent/US5149407A/en" 
                        class="list-group-item list-group-item-action">
                          Procédés et appareils pour la production de gaz combustible et la libération accrue de 
                          énergie thermique provenant de ce gaz - US5149407A - Figure 9
                        </a>
                        <a href="https://holomorphe.com/chemical-products/voltage_intensifier_circuit" 
                        class="list-group-item list-group-item-action">
                            Voltage intensifier circuit (VIC)
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
            'header-center': "Cahier des charges de fabrication de transformateurs VIC",
            'footer-right': '[page] sur [topage]',
            'footer-left': 'S.A.S.U.A.C.V. Holomorphe [SIREN : 883632556]'
        }

        path_wkthmltopdf = "C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe"
        config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
        pdfkit.from_string(body,
                           "VIC\\Cahier_Charges_Transformateurs_VIC_[SASU_Holomorphe].pdf",
                           configuration=config,
                           options=options)


if __name__ == '__main__':
    unittest.main()
