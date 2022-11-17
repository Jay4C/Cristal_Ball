import unittest
import pdfkit


class Contrat_Prestation_Service(unittest.TestCase):
    # ok
    def test_Contrat_Prestation_Service(self):
        print("test_Contrat_Prestation_Service")

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

            <title>Contrat de prestation de service</title>
          </head>
          <body>
            <!-- Container -->
            <div class="container">

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
                        Adresse du siège social : 31 Avenue de Ségur - ABC LIV Ségur - 75007 Paris / 
                        Siret : 88363255600014
                      </li>
                      <li class="list-group-item">
                        Registre du commerce et des sociétés : R.C.S. PARIS - Greffe du Tribunal de Commerce de PARIS
                      </li>
                      <li class="list-group-item">
                        Activités : Commerce de gros de produits chimiques - Edition de logiciels applicatifs / 
                        Code NAF : 4675Z
                      </li>
                      <li class="list-group-item">
                        Numero TVA intracommunataire : FR06883632556 / Président : Monsieur  / 
                        Date d'immatriculation : 26 Mai 2020
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
                                <th scope="col">Email</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>Monsieur </td>
                                <td>31 Avenue de Ségur 75007 Paris</td>
                                <td>07.49.16.33.29</td>
                                <td>jason.aloyau@outlook.fr</td>
                            </tr>
                        </tbody>
                    </table>
                  </div>
                </div>
                <!-- Contact -->

                <br>

                <!-- Contrat de prestation de service -->
                <div class="card text-center">
                  <div class="card-header">
                    Contrat de prestation de service
                  </div>
                  <div class="card-body">
                    <!-- Contractants -->
                    <div class="card text-center">
                      <div class="card-header">
                        Contractants
                      </div>
                      <div class="card-body">
                        Vu les articles 1145 à 1161 du code civil concernant la capacité et la représentation,
                        
                        <br>
                        
                        Vu les articles L123-1 à L123-11-8 du code de commerce concernant le registre du commerce 
                        et des sociétés,
                        
                        <br>
                        
                        Vu les articles R123-31 à R123-171-1 du code de commerce concernant le registre du commerce 
                        et des sociétés,
                        
                        <br>
                        
                        Vu les articles A123-12 à A123-80 du code de commerce concernant le registre du commerce 
                        et des sociétés,
                        
                        <br>
                        <br>

                        <!-- Prestataire -->
                        <div class="card text-center">
                          <div class="card-header">
                            Prestataire
                          </div>
                          <div class="card-body">
                            Dans le présent contrat de prestation de service, le prestataire est une personne morale 
                            désignée par les informations suivantes :
                            
                            <br>
                            
                            - Raison sociale : HOLOMORPHE, société par actions simplifiée unipersonnelle à capital 
                            variable
                            
                            <br>
                            
                            - Capital social : 100 euros
                            
                            <br>
                            
                            - Adresse du siège social : 31 Avenue de Ségur - ABC LIV Ségur - 75007 Paris
                            
                            <br>
                            
                            - Numéro SIRET : 88363255600014
                            
                            <br>
                            
                            - Registre du commerce et des sociétés : Registre du commerce et des sociétés de Paris 
                            / Greffe du tribunal de commerce de Paris
                            
                            <br>
                            
                            - Activités : Commerce de gros de produits chimiques / Édition de logiciels applicatifs
                            
                            <br>
                            
                            - Code NAF : 4675Z
                            
                            <br>
                            
                            - Numéro TVA intracommunataire : FR06883632556
                            
                            <br>
                            
                            - Président : Monsieur 
                            
                            <br>
                            
                            - Date d'immatriculation : 26 Mai 2020
                            
                            <br>
                            
                            - Numéro de téléphone : 
                            
                            <br>
                            <br>
                            
                            Conformément aux articles 1145 à 1161 du code civil, le prestataire est représenté par ... 
                            pour le le présent contrat de prestation de service.
                            
                            <br>
                            <br>
                            
                            Conformément aux articles L123-1 à L123-11-8 du code de commerce, le prestataire 
                            devra joindre une copie de son extrait Kbis datant de moins de trois mois par rapport à la 
                            date de signature du présent contrat de prestation de service et une copie d'une pièce 
                            d'identité de son représentant légal mentionné dans son extrait Kbis au présent contrat 
                            de prestation de service afin de prouver son immatriculation auprès du registre de 
                            commerce et des sociétés.
                          </div>
                        </div>
                        <!-- Prestataire -->
                        
                        <br>
                        
                        <!-- Client -->
                        <div class="card text-center">
                          <div class="card-header">
                            Client
                          </div>
                          <div class="card-body">
                            Dans le présent contrat de prestation de service, le client est une personne morale 
                            désignée par les informations suivantes :
                            
                            <br>
                            
                            - Raison sociale : ...
                            
                            <br>
                            
                            - Capital social : ...
                            
                            <br>
                            
                            - Adresse du siège social : ...
                            
                            <br>
                            
                            - Numéro SIRET : ...
                            
                            <br>
                            
                            - Registre du commerce et des sociétés : ...
                            
                            <br>
                            
                            - Activités : ...
                            
                            <br>
                            
                            - Code NAF : ...
                            
                            <br>
                            
                            - Numero TVA intracommunataire : ...
                            
                            <br>
                            
                            - Président : ...
                            
                            <br>
                            
                            - Date d'immatriculation : ...
                            
                            <br>
                            
                            - Numéro de téléphone : ...
                            
                            <br>
                            <br>
                            
                            Conformément aux articles 1145 à 1161 du code civil, le client est représenté par ... 
                            pour le présent contrat de prestation de service.
                            
                            <br>
                            <br>
                            
                            Conformément aux articles L123-1 à L123-11-8 du code de commerce, le client devra joindre 
                            une copie de son extrait Kbis datant de moins de trois mois par rapport à la date de 
                            signature du présent contrat de prestation de service et une copie d'une pièce d'identité 
                            de son représentant légal mentionné dans son extrait Kbis au présent contrat de prestation 
                            de service afin de prouver son immatriculation auprès du registre de commerce et des 
                            sociétés.
                          </div>
                        </div>
                        <!-- Client -->
                      </div>
                    </div>
                    <!-- Contractants -->

                    <br>

                    <h6>
                        Dans le présent contrat de prestation de service, il a été convenu ce qui suit:
                    </h6>

                    <br>

                    <!-- Articles -->
                    <div class="card text-center">
                      <div class="card-header">
                        Articles
                      </div>
                      <div class="card-body">
                        <!-- Article 1 - Nature de la mission -->
                        <div class="card text-center">
                          <div class="card-header">
                            Article 1 - Nature de la mission
                          </div>
                          <div class="card-body">
                            Vu les articles 1112 à 1187 du code civil conernant la formation du contrat,
                            
                            <br>
                            <br>
                            
                            Le client confie au prestataire une mission consistant à répondre aux besoins suivants :
                            
                            <br>
                            
                            - 
                            
                            <br>
                            
                            -
                            
                            <br>
                            <br>
                            
                            Le cas échéant, dans le cadre de cette mission, le prestataire peut s'engager à mettre ses 
                            collaborateurs à la disposition du client si cela est nécessaire pour la bonne exécution 
                            de la mission. Cependant, lesdits salariés resteront sous l'autorité et sous la 
                            responsabilité du prestataire pendant leur intervention chez le client.
                          </div>
                        </div>
                        <!-- Article 1 - Nature de la mission -->

                        <br>

                        <!-- Article 2 - Durée de la mission -->
                        <div class="card text-center">
                          <div class="card-header">
                            Article 2 - Durée de la mission
                          </div>
                          <div class="card-body">
                            Vu les articles 1210 à 1215 du code civil concernant la durée du contrat,
                            
                            <br>
                            <br>
                            
                            Le prestataire s'engage à accomplir la mission confiée par le client du présent contrat de 
                            prestation de service pendant une durée de ... jours calendaires du lundi au vendredi 
                            sans compter les jours fériés et les jours de week-end.
                            
                            <br>
                            <br>
                            
                            Toutefois, le client ne peut obtenir des dommages et intérêts lors du retard 
                            d'accomplissement de la mission par le prestataire même par cas forfuit et cas de force 
                            majeure.
                            
                            <br>
                            <br>
                            
                            De plus, chaque contractant ne peut mettre fin au présent contrat de prestation de service, 
                            sauf en cas de liquidation judiciaire.
                          </div>
                        </div>
                        <!-- Article 2 - Durée de la mission -->

                        <br>

                        <!-- Article 3 - Prix -->
                        <div class="card text-center">
                          <div class="card-header">
                            Article 3 - Prix
                          </div>
                          <div class="card-body">
                            Vu les articles L441-3 à L441-8 du code de commerce concernant la négociation et la 
                            formalisation de la relation commerciale,
                            
                            <br>
                            <br>
                            
                            Le client s'engage à payer un prix fixé en fonction d'un tarif journalier de ... euros 
                            hors taxes.
                            
                            <br>
                            <br>
                            
                            D'autre part, le client s'engage à rembourser au prestataire les éventuels frais de 
                            déplacement ou de séjour à l'hôtel qui seraient nécessités pour l'exécution de la mission. 
                            Ces frais seront engagés après accord écrit du client et ils devront être remboursés sur 
                            présentation des justificatifs.
                          </div>
                        </div>
                        <!-- Article 3 - Prix -->

                        <br>

                        <!-- Article 4 - Facturation et délai de paiement (Code de commerce) -->
                        <div class="card text-center">
                          <div class="card-header">
                            Article 4 - Facturation et délai de paiement
                          </div>
                          <div class="card-body">
                            Vu les articles L123-12 à L123-24 du code de commerce concernant les obligations comptables 
                            applicables à tous les commerçants,
                            
                            <br>
                            
                            Vu les articles L441-3 à L441-7 du code de commerce concernant les conventions écrites pour 
                            la négociation et la formalisation de la relation commerciale,
                            
                            <br>
                            
                            Vu les articles L441-9 à L441-16 du code de commerce concernant la facturation et les 
                            délais de paiement,
                            
                            <br>
                            
                            Vu les articles D441-5 à R441-10 du code de commerce concernant la facturation et les 
                            délais de paiement,
                            
                            <br>
                            
                            Vu les articles D123-235 à D123-236 du code de commerce concernant le numéro unique 
                            d'identification des entreprises,
                            
                            <br>
                            
                            Vu les articles 289-0 à 289 bis du code général des impôts concernant les obligations des 
                            redevables pour la taxe sur la valeur ajoutée par rapport aux factures,
                            
                            <br>
                            
                            Vu les articles 242 nonies à 242 nonies A de l'annexe 2 du code général des impôts 
                            concernant les obligations des redevables pour la taxe sur la valeur ajoutée par rapport 
                            aux factures,
                            
                            <br>
                            
                            Vu les articles 96 F à 96 I bis de l'annexe 3 du code général des impôts concernant les 
                            obligations des redevables pour la taxe sur la valeur ajoutée par rapport aux factures 
                            transmises par voie électronique,
                            
                            <br>
                            
                            Vu les articles 41 septies à 41 nonies de l'annexe 4 du code général des impôts concernant 
                            les obligations des redevables pour la taxe sur la valeur ajoutée par rapport aux factures 
                            transmises par voie électronique,
                            
                            <br>
                            
                            Vu les articles L102 B à L102 E du livre des procédures fiscales concernant l'obligation 
                            et les délais de conservation des documents,
                            
                            <br>
                            <br>
                            
                            Conformément à l'article L441-9 du code de commerce, le prestataire émettra une facture 
                            au client à la fin de la mission du présent contrat de prestation de service. Les factures 
                            émises au client par le prestataire du présent contrat de prestation de service seront 
                            émises par voie électronique au moyen d'une signature électronique. En cas d'erreur, 
                            une facture émise au client par le prestataire du présent contrat de prestation de service 
                            peut être annulée ou rectifiée.
                            
                            <br>
                            <br>
                            
                            Conformément à l'article L441-10 du code de commerce, le délai de paiement convenu entre les 
                            contractants du présent contrat de prestation de service pour régler les 
                            sommes dues ne peut dépasser trente jours après la date d'émission de la facture 
                            émise au client par le prestataire du présent contrat de prestation de service.
                            
                            <br>
                            <br>
                            
                            Conformément à l'article L123-22 du code de commerce et à l'article L102 B du livre des 
                            procédures fiscales, les factures émises au client par le prestataire du présent contrat 
                            de prestation de service seront établies en euros et en langue française, et devront être 
                            conservées pendant dix ans par les contractants.
                            
                            <br>
                            <br>
                            
                            Conformément à l'article 289 du code général des impôts et à l'article 242 nonies A de 
                            l'annexe 2 du code général des impôts, les factures émises au client par le prestataire 
                            du présent contrat de prestation de service comporteront un certain nombre de mentions 
                            obligatoires qui sont les suivantes :
                            
                            <br>
                            
                            - La date de l'émission de la facture qui est la date à laquelle elle est émise.
                            
                            <br>
                            
                            - La numérotation de la facture qui est le numéro unique basé sur une séquence 
                            chronologique continue et sans rupture.
                            
                            <br>
                            
                            - La date de la fin de la mission qui est le jour effectif de la fin d'exécution de la 
                            mission.
                            
                            <br>
                            
                            - L'identité du client qui comporte la dénomination sociale du client, 
                            l'adresse du siège social du client et l'adresse de facturation si différente du 
                            siège social.
                            
                            <br>
                            
                            - L'identité du prestataire qui comporte la dénomination sociale du prestataire suivie du 
                            numéro siren, l'adresse du siège social du prestataire, la forme juridique et le montant 
                            du capital social du prestataire.
                            
                            <br>
                            
                            - Le numéro individuel d'identification à la TVA du prestataire et du client professionnel.
                            
                            <br>
                            
                            - La désignation de la prestation qui comporte la prestation fournie.
                            
                            <br>
                            
                            - Le décompte détaillé de chaque prestation qui comporte le détail en quantité et prix.
                            
                            <br>
                            
                            - Le prix catalogue qui comporte le prix unitaire hors TVA de la prestation fournie.
                            
                            <br>
                            
                            - La majoration éventuelle de prix qui comporte les frais de transport ou d'emballage 
                            par exemple.
                            
                            <br>
                            
                            - Le taux de TVA légalement applicable et le montant total de la TVA correspondant.
                            
                            <br>
                            
                            - La mention suivante : "Rabais, ristourne, ou remise acquise à la date de la prestation 
                            de service et directement liée à cette opération : néant.".
                            
                            <br>
                            
                            - La somme totale à payer hors taxe (HT) et toutes taxes comprises (TTC).
                            
                            <br>
                            
                            - La date de paiement ou le délai de paiement qui est la date à laquelle le règlement 
                            doit intervenir.
                            
                            <br>
                            
                            - La mention suivante : "Escompte pour paiement anticipé : néant.".
                            
                            <br>
                            
                            - Les taux des pénalités de retard qui sont Exigibles en cas de non-paiement à la date de 
                            règlement.
                            
                            <br>
                            
                            - La mention suivante : "Les pénalités de retard sont exigibles sans qu'un rappel soit 
                            nécessaire.".
                            
                            <br>
                            
                            - La mention de l'indemnité forfaitaire de quarante euros pour frais de recouvrement, 
                            en cas de retard de paiement.
                            
                            <br>
                            
                            - La mention suivante : "Le paiement sera effectué en une seule fois par virement bancaire 
                            aux coordonnées bancaires du prestataire."
                            
                            <br>
                            
                            - Les coordonnées bancaires du prestataire.
                          </div>
                        </div>
                        <!-- Article 4 - Facturation et délais de paiement (Code de commerce) -->

                        <br>

                        <!-- Article 5 - Pénalités pour retard de paiement (Code de commerce, 
                        Code de procédure civile) -->
                        <div class="card text-center">
                          <div class="card-header">
                            Article 5 - Pénalités pour retard de paiement
                          </div>
                          <div class="card-body">
                            Vu les articles L441-10 à L441-16 du code de commerce concernant les délais de paiement,
                            
                            <br>
                            
                            Vu l'article L313-2 du code monétaire et financier concernant le taux de l'intérêt légal,
                            
                            <br>
                            
                            Vu l'article D313-1-A du code monétaire et financier concernant le taux de l'intérêt légal,
                            
                            <br>
                            
                            Vu le code de procédure civile,
                            
                            <br>
                            <br>
                            
                            Conformément à l'article L441-10 du code de commerce, tout retard de paiement de toute 
                            facture émise au client par le prestataire du présent contrat de prestation de service 
                            fera l'objet de pénalités de retard de paiement exigibles le jour suivant 
                            la date de règlement figurant sur toute facture émise au client par le prestataire du 
                            présent contrat de prestation de service ainsi que le montant de 
                            l'indemnité forfaitaire pour frais de recouvrement due au prestataire dans le cas où les 
                            sommes dues sont réglées après cette date. Les pénalités de retard de paiement de toute 
                            facture émise au client par le prestataire du présent contrat de prestation de service 
                            sont exigibles sans qu'un rappel soit nécessaire. Le client en situation de 
                            retard de paiement est de plein droit débiteur, à l'égard du prestataire, d'une indemnité 
                            forfaitaire pour frais de recouvrement, dont le montant est fixé par décret. Lorsque 
                            les frais de recouvrement exposés sont supérieurs au montant de cette indemnité 
                            forfaitaire, le prestataire peut demander une indemnisation complémentaire, sur 
                            justification.
                            
                            <br>
                            <br>
                            
                            Le taux de l'intérêt légal sera fixé à vingt pour cent (20%) pour tout calcul des 
                            pénalités de retard de paiement de toute facture émise au client par le prestataire du 
                            présent contrat de prestation de service.
                            
                            <br>
                            <br>
                            
                            La formule de calcul des pénalités de retard de paiement de toute facture émise au 
                            client par le prestataire du présent contrat de prestation de service est la suivante 
                            : [(taux d'intérêt légal fixé par le présent contrat de prestation de service) 
                            x (montant TTC de toute facture émise au client par le prestataire du présent contrat 
                            de prestation de service)] x [(nombre de jours de retard de paiement de toute facture 
                            émise au client par le prestataire du présent contrat de prestation de service)/365].
                            
                            <br>
                            <br>
                            
                            Le point de départ des pénalités de retard de paiement de toute facture émise au client 
                            par le prestataire du présent contrat de prestation de service est le lendemain 
                            de l'échéance de toute facture émise au client par le prestataire du présent contrat de 
                            prestation de service. Le point d'arrivée du calcul des pénalités de retard 
                            de paiement de toute facture émise au client par le prestataire du présent contrat de 
                            prestation de service est constitué par la date d'envoi du règlement de toute 
                            facture émise au client par le prestataire du présent contrat de prestation de service.
                          </div>
                        </div>
                        <!-- Article 5 - Pénalités pour retard de paiement (Code de commerce, 
                        Code de procédure civile) -->

                        <br>

                        <!-- Article 6 : Obligations du prestataire -->
                        <div class="card text-center">
                          <div class="card-header">
                            Article 6 : Obligations du prestataire
                          </div>
                          <div class="card-body">
                            Vu les articles 1304 à 1304-7 du code civil concernant l'obligation conditionnelle,
                            
                            <br>
                            <br>
                            
                            Il est rappelé que le prestataire est tenu à une obligation de moyens. 
                            Le prestataire doit donc exécuter sa mission conformément aux règles en vigueur dans sa 
                            profession et en se conformant à toutes les données acquises dans son domaine de compétence.
                            
                            <br>
                            <br>
                            
                            Le prestataire reconnaît que le client lui a donné une information complète sur ses 
                            besoins et sur les impératifs à respecter.
                            
                            <br>
                            <br>
                            
                            Le prestataire s'engage à se conformer au réglement intérieur et aux consignes de sécurité 
                            applicables chez le client.
                            
                            <br>
                            <br>
                            
                            Enfin, le prestataire s'engage à observer la confidentialité la plus totale en ce qui 
                            concerne le contenu de la mission et toutes les informations ainsi que tous les documents 
                            que le client lui aura communiqués.
                          </div>
                        </div>
                        <!-- Article 6 : Obligations du prestataire -->

                        <br>

                        <!-- Article 7 : Obligations du client -->
                        <div class="card text-center">
                          <div class="card-header">
                            Article 7 : Obligations du client
                          </div>
                          <div class="card-body">
                            Vu les articles 1304 à 1304-7 du code civil concernant l'obligation conditionnelle,
                            
                            <br>
                            <br>
                            
                            Afin de permettre au prestataire de réaliser la mission dans de bonnes conditions, le 
                            client s'engage à lui remettre tous les documents nécessaires dans les meilleurs délais.
                          </div>
                        </div>
                        <!-- Article 7 : Obligations du client -->

                        <br>

                        <!-- Article 8 : Responsabilité -->
                        <div class="card text-center">
                          <div class="card-header">
                            Article 8 : Responsabilité
                          </div>
                          <div class="card-body">
                            Vu les articles 1240 à 1244 du code civil concernant la responsabilité extracontractuelle 
                            en général,
                            
                            <br>
                            <br>
                            
                            La responsabilité du prestataire ne pourra être mise en cause qu'en cas de manquement à son 
                            obligation de moyens. 
                            
                            <br>
                            <br>
                            
                            En outre, le client ne pourra pas l'invoquer dans les cas suivants :
                            <br>
                            - si le client a omis de remettre au prestataire un document ou une information nécessaire 
                            pour la mission,
                            <br>
                            - en cas de force majeure ou d'autres causes indépendantes de la volonté du prestataire.
                          </div>
                        </div>
                        <!-- Article 8 : Responsabilité -->

                        <br>

                        <!-- Article 9 : Propriété intellectuelle -->
                        <div class="card text-center">
                          <div class="card-header">
                            Article 9 : Propriété intellectuelle
                          </div>
                          <div class="card-body">
                            Vu le code de la propriété intellectuelle,
                            
                            <br>
                            <br>
                            
                            Conformément à l'article L621-1 du code de la propriété intellectuelle, 
                            le prestataire reste exclusivement propriétaire des moyens mis en application par le 
                            prestataire pour l'accomplissement de la mission dans l'intérêt du client pendant le 
                            présent contrat de prestation de service.
                            
                            <br>
                            <br>
                            
                            Le client ne peut se prévaloir des droits des secrets des moyens mis en application par le 
                            prestataire pour l'accomplissement de la mission dans l'intérêt du client pendant le 
                            présent contrat de prestation de service.
                            
                            <br>
                            <br>
                            
                            Le prestataire peut exercer toutes actions en justice contre le client ou des tiers pour 
                            violation des secrets des moyens mis en application par le prestataire pour 
                            l'accomplissement de la mission dans l'intérêt du client pendant le présent contrat de 
                            prestation de service.
                            
                            <br>
                            <br>
                            
                            Conformément aux articles L615-1 à L615-22 du code de la propriété intellectuelle, 
                            le client ne peut se prévaloir d'exercer des actions en justice contre le prestataire 
                            pour contrefaçon des des moyens mis en application par le prestataire pour 
                            l'accomplissement de la mission dans l'intérêt du client pendant le présent contrat de 
                            prestation de service.
                            
                            <br>
                            <br>
                            
                            Lorsque la fin de la mission est à son terme, le client doit payer la facture lui étant 
                            émise par le prestataire afin d'obtenir les droits des produits créés par le prestataire 
                            avec les moyens mis en application par le prestataire pour l'accomplissement de la mission 
                            dans l'intérêt du client pendant le présent contrat de prestation de service.
                          </div>
                        </div>
                        <!-- Article 9 : Propriété intellectuelle -->

                        <br>

                        <!-- Article 10 - Protection du secret des affaires / Confidentialité (Code de commerce) -->
                        <div class="card text-center">
                          <div class="card-header">
                            Article 15 - Protection du secret des affaires / Confidentialité
                          </div>
                          <div class="card-body">
                            Vu les articles L151-1 à L154-1 du code de commerce concernant la protection du 
                            secret des affaires,
                            
                            <br>
                            
                            Vu les articles R152-1 à R153-10 du code de commerce concernant 
                            la protection du secret des affaires,
                            
                            <br>
                            <br>
                            
                            Comnformément à l'article L151-1 du code de commerce concernant l'information protégée, 
                            les moyens mis en application par le prestataire pour l'accomplissement de la mission 
                            dans l'intérêt du client pendant le présent contrat de prestation de service sont 
                            protégés au titre du secret des affaires.
                            
                            <br>
                            <br>
                            
                            Conformément aux articles L151-2 à L151-3 du code de commerce concernant la détention 
                            légitime et l'obtention licite d'un secret des affaires, le prestataire est l'unique 
                            détenteur légitime du secret des affaires des moyens mis en application par le prestataire 
                            pour l'accomplissement de la mission dans l'intérêt du client pendant le présent contrat 
                            de prestation de service.
                            
                            <br>
                            <br>
                            
                            Conformément aux articles L151-4 à L151-6 du code de commerce concernant l'obtention 
                            illicite, l'utilisation illicite et la divulgation illicite du secret des affaires, 
                            le client ne peut se prévaloir le droit d'obtenir, d'utiliser et de divulguer 
                            tout secret des affaires des moyens mis en application par le prestataire 
                            pour l'accomplissement de la mission dans l'intérêt du client pendant le présent contrat 
                            de prestation de service.
                            
                            <br>
                            <br>
                            
                            Conformément aux articles L152-1 à L152-8, L153-1 à L153-2, R152-1, R153-1 à R153-10 du 
                            code de commerce concernant les actions en prévention, en cessation ou en réparation 
                            d'une atteinte au secret des affaires et les mesures générales de protection du 
                            secret des affaires devant les juridictions civiles ou commerciales, le prestataire peut 
                            exercer des actions en justice contre le client ou des tiers pour atteinte au secret 
                            des affaires des moyens mis en application par le prestataire pour l'accomplissement 
                            de la mission dans l'intérêt du client pendant le présent contrat de prestation de service.
                          </div>
                        </div>
                        <!-- Article 10- Protection du secret des affaires / Confidentialité (Code de commerce) -->

                        <br>
                        
                        <!-- Article 11 - Droit applicable et juridiction compétente (Code de commerce) -->
                        <div class="card text-center">
                          <div class="card-header">
                            Article 11 - Droit applicable et juridiction compétente
                          </div>
                          <div class="card-body">
                            Vu les articles 1188 à 1192 du code civil concernant l'interprétation du contrat,
                            
                            <br>
                            
                            Vu les articles 1240 à 1252 du code civil concernant la responsabilité extracontractuelle,
                            
                            <br>
                            
                            Vu les articles L721-1 à L724-7 du code de commerce concernant le tribunal de commerce,
                            
                            <br>
                            
                            Vu les articles R721-1 à R724-21 du code de commerce concernant le tribunal de commerce,
                            
                            <br>
                            
                            Vu les articles A721-1 à A721-10 du code de commerce concernant le tribunal de commerce,
                            
                            <br>
                            
                            Vu l'article Annexe 7-1 du code de commerce,
                            
                            <br>
                            <br>
                            
                            Le présent contrat de prestation de service est assujetti au droit français.
                            
                            <br>
                            <br>
                            
                            Conformément aux articles L721-1 à L721-8 et R721-1 à R721-22 du code de commerce 
                            concernant l'institution et la compétence du tribunal de commerce, les contractants 
                            s'engagent à rechercher une solution amiable à tout différend né de l'application ou 
                            de l'interprétation du présent contrat de prestation de service. À défaut 
                            de solution amiable, le litige sera tranché par le tribunal de commerce de Paris.
                          </div>
                        </div>
                        <!-- Article 11 - Droit applicable et juridiction compétente -->
                      </div>
                    </div>
                    <!-- Articles -->

                    <br>                   

                    <!-- Signatures et cachets des cocontractants  -->
                    <div class="card text-center">
                      <div class="card-header">
                        Signatures et cachets des contractants
                      </div>
                      <div class="card-body">  
                        Vu les articles 1101 à 1231-7 du code civil concernant le contrat,
                        
                        <br>
                        
                        Vu les articles 1372 à 1377 du code civil concernant l'acte sous signature privée,
                        
                        <br>
                        <br>
                        
                        Conformément aux articles 1112 à 1187 et 1372 à 1377 du code civil, le présent contrat de 
                        prestation de service a été établi par acte sous signatures privées par les contractants.
                        
                        <br>
                        <br>
                        
                        <!-- Lieu et date des signatures et cachets des cocontractants (Code civil) -->
                        <div class="card text-center">
                          <div class="card-header">
                            Lieu et date des signatures et cachets des contractants
                          </div>
                          <div class="card-body">
                            En date du ... situé au ..., le présent contrat de prestation de service a été signé et 
                            tamponné par le prestataire et le client.
                          </div>
                        </div>
                        <!-- Lieu et date des signatures et cachets des cocontractants (Code civil) -->

                        <br>

                        <!-- Nombre d'exemplaires du présent contrat (Code civil) -->
                        <div class="card text-center">
                          <div class="card-header">
                            Nombre d'exemplaires du présent contrat
                          </div>
                          <div class="card-body">
                            Le présent contrat de prestation de service est fait en deux exemplaires 
                            dont l'un pour le prestataire et l'autre pour le client.
                          </div>
                        </div>
                        <!-- Nombre d'exemplaires du présent contrat (Code civil) -->

                        <br>

                        <!-- Approbation du présent contrat (Code civil) -->
                        <div class="card text-center">
                          <div class="card-header">
                            Approbation du présent contrat
                          </div>
                          <div class="card-body">
                            Le présent contrat de prestation de service a été lu et approuvé par le prestataire et le 
                            client.
                          </div>
                        </div>
                        <!-- Approbation du présent contrat (Code civil) -->

                        <br>

                        <!-- Signature et cachet du prestataire -->
                        <div class="card text-center">
                          <div class="card-header">
                            Signature et cachet du prestataire
                          </div>
                          <div class="card-body">
                            "Lu et approuvé"
                            <br>
                            <br>
                            <br>
                            <br>
                            <br>
                            <br>
                            <br>
                            <br>
                          </div>
                        </div>
                        <!-- Signature et cachet du prestataire -->

                        <br>

                        <!-- Signature et cachet du client -->
                        <div class="card text-center">
                          <div class="card-header">
                            Signature et cachet du client
                          </div>
                          <div class="card-body">
                            "Lu et approuvé"
                            <br>
                            <br>
                            <br>
                            <br>
                            <br>
                            <br>
                            <br>
                            <br>
                          </div>
                        </div>
                        <!-- Signature et cachet du client -->

                      </div>
                    </div>
                    <!-- Signatures et cachets des cocontractants  -->

                  </div>
                </div>
                <!-- Contrat de prestation de service -->

                <br>

            </div>
            <!-- Container -->

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
            'header-center': "Contrat de prestation de service",
            'footer-right': '[page] sur [topage]',
            'footer-left': 'Société Holomorphe [SIREN : 883632556]'
        }

        path_wkthmltopdf = "C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe"

        config = pdfkit.configuration(
            wkhtmltopdf=path_wkthmltopdf
        )

        pdfkit.from_string(
            body,
            "C_P_S\\C_P_S_[Societe_Holomorphe].pdf",
            configuration=config,
            options=options
        )


if __name__ == '__main__':
    unittest.main()
