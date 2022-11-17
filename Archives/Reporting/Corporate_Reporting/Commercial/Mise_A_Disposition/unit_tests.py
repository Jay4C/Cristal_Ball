import unittest
import pdfkit


class Mise_A_Disposition(unittest.TestCase):
    # ok
    def test_mise_a_disposition(self):
        print("test_mise_a_disposition")

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

            <title>Convention de mise à disposition de matériels</title>
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
                                <th scope="col">E-mail professionnel</th>
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
                <!-- Contact -->

                <br>
                
                <!-- Convention de mise à disposition de matériels -->
                <div class="card text-center">
                  <div class="card-header">
                    Convention de mise à disposition de matériels
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
                        <!-- Emprunteur -->
                        <div class="card text-center">
                          <div class="card-header">
                            Emprunteur
                          </div>
                          <div class="card-body">
                            Dans la présente convention de mise à disposition de matériels, l'emprunteur est une 
                            personne morale désignée par les informations suivantes :
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
                            Conformément aux articles 1145 à 1161 du code civil, l'emprunteur est représenté par ... 
                            pour la présente convention de mise à disposition de matériels.
                            <br>
                            <br>
                            Conformément aux articles L123-1 à L123-11-8 du code de commerce, l'emprunteur 
                            devra joindre une copie de son extrait Kbis datant de moins de trois mois par rapport à la 
                            date de signature de la présente convention de mise à disposition de matériels et une 
                            copie d'une pièce d'identité de son représentant légal mentionné dans son extrait Kbis à 
                            la présente convention de mise à disposition de matériels afin de prouver son 
                            immatriculation auprès du registre de commerce et des sociétés.
                          </div>
                        </div>
                        <!-- Emprunteur -->
                        
                        <br>
                        
                        <!-- Prêteur -->
                        <div class="card text-center">
                          <div class="card-header">
                            Prêteur
                          </div>
                          <div class="card-body">
                            Dans la présente convention de mise à disposition de matériels, le prêteur est une 
                            personne morale désignée par les informations suivantes :
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
                            - Numéro de téléphone : 00.33.7.49.16.33.29
                            <br>
                            <br>
                            Conformément aux articles 1145 à 1161 du code civil, le prêteur est représenté par ... 
                            pour la présente convention de mise à disposition de matériels.
                            <br>
                            <br>
                            Conformément aux articles L123-1 à L123-11-8 du code de commerce, le prêteur 
                            devra joindre une copie de son extrait Kbis datant de moins de trois mois par rapport à la 
                            date de signature de la présente convention de mise à disposition de matériels et une 
                            copie d'une pièce d'identité de son représentant légal mentionné dans son extrait Kbis à 
                            la présente convention de mise à disposition de matériels afin de prouver son 
                            immatriculation auprès du registre de commerce et des sociétés.
                          </div>
                        </div>
                        <!-- Prêteur -->
                      </div>
                    </div>
                    <!-- Contractants -->

                    <br>
                        
                    <h6>
                        Dans la présente convention de mise à disposition de matériels, il a été convenu ce qui suit:
                    </h6>
                    
                    <br>
                    
                    <!-- Articles -->
                    <div class="card text-center">
                      <div class="card-header">
                        Articles
                      </div>
                      <div class="card-body">
                        <!-- Article 1 - Objet de la convention (Code civil) -->
                        <div class="card text-center">
                          <div class="card-header">
                            Article 1 - Objet de la convention
                          </div>
                          <div class="card-body">
                            Vu les articles L110-1 à L110-4 du code de commerce concernant l'acte de commerce,
                            <br>
                            <br>
                            Conformément à l'article L110-3 du code de commerce, le prêteur accepte de mettre à la 
                            disposition de l'emprunteur des matériels en vue de la valorisation du dioxyde de carbone 
                            par méthanation qui se déroulera au ... à partir du ... pendant une durée indéterminée.
                          </div>
                        </div>
                        <!-- Article 1 - Objet de la convention (Code civil) -->
                        
                        <br>
                        
                        <!-- Article 2 - Durée de la convention (Code civil) -->
                        <div class="card text-center">
                          <div class="card-header">
                            Article 2 - Durée de la convention
                          </div>
                          <div class="card-body">
                            Vu les articles 1210 à 1215 du code civil concernant la durée du contrat,
                            
                            <br>
                            
                            Vu les articles 1875 à 1891 du code civil concernant le prêt à usage ou le commodat,
                            
                            <br>
                            <br>
                            
                            Le prêteur s'engage à venir déposer les matériels mis à la disposition de l'emprunteur 
                            de la présente convention de mise à disposition de matériels en date du ... à ... 
                            pendant une durée indéterminée.
                            
                            <br>
                            <br>
                            
                            Conformément aux articles 1210 à 1211 du code civil, chaque contractant peut mettre 
                            fin dans les conditions prévues de la présente convention de mise à disposition de 
                            matériels à durée indéterminée.
                          </div>
                        </div>
                        <!-- Article 2 - Durée de la convention (Code civil) -->
                        
                        <br>
                        
                        <!-- Article 3 - Restitution du matériel mis à disposition (Code civil) -->
                        <div class="card text-center">
                          <div class="card-header">
                            Article 3 - Restitution des matériels mis à disposition
                          </div>
                          <div class="card-body">
                            Vu les articles 1372 à 1377 du code civil concernant l'acte sous signature privée,
                            <br>
                            Vu les articles 1708 à 1712 du code civil concernant les dispositions générales du contrat 
                            de louage,
                            <br>
                            Vu les articles 1875 à 1891 du code civil concernant le prêt à usage,
                            <br>
                            <br>
                            Conformément à l'article 1875 du code civil, au terme de la présente convention de mise 
                            à disposition de matériels, l'emprunteur s'engage à restituer les matériels lui étant mis 
                            à disposition par le prêteur de la présente convention de mise à disposition de matériels 
                            dans son état initial.
                            <br>
                            <br>
                            En date de la restitution des matériels mis à la disposition de l'emprunteur par le prêteur 
                            de la présente convention de mise à disposition de matériels, les contractants dresseront 
                            un état des lieux pour retour de matériel au site d'exploitation de l'emprunteur ayant 
                            installé les matériels mis à la disposition de l'emprunteur par le prêteur 
                            de la présente convention de mise à disposition de matériels. L'état des lieux pour retour 
                            de matériel sera daté, paraphé, signé et tamponné par les contractants en deux exemplaires 
                            dont l'un pour l'emprunteur et l'autre pour le prêteur par acte sous signatures privées.
                          </div>
                        </div>
                        <!-- Article 3 - Restitution du matériel mis à disposition (Code civil) -->
                        
                        <br>
                        
                        <!-- Article 4 - Convention à titre onéreux (Code civil, code de commerce) -->
                        <div class="card text-center">
                          <div class="card-header">
                            Article 4 - Prêt à usage à titre onéreux
                          </div>
                          <div class="card-body">
                            Vu les articles 1708 à 1712 du code civil concernant les dispositions générales du 
                            contrat de louage,
                            <br>
                            Vu les articles 1875 à 1879 du code civil concernant la nature du prêt à usage,
                            <br>
                            Vu les articles L410-1 à L490-14 du code de commerce concernant la liberté des 
                            prix et de la concurrence,
                            <br>
                            Vu les articles R410-1 à R490-10 du code de commerce concernant la liberté des 
                            prix et de la concurrence,
                            <br>
                            <br>
                            Conformément aux articles 1709 et 1875 du code civil, la présente convention de mise à 
                            disposition de matériels est consentie moyennant une somme d'argent d'un montant définitif 
                            et mensuel de ... euros hors taxes sur la valeur ajoutée, payable par l'emprunteur au 
                            prêteur au quinzième jour de chaque mois par virement bancaire envoyé au compte bancaire 
                            du prêteur dont les références d'identité bancaire sont les suivantes : 
                            <br>
                            - Titutalire du compte banciare : HOLOMORPHE
                            <br>
                            - Numéro de compte bancaire : 00002376620
                            <br> 
                            - IBAN : FR7616798000010000237662052
                            <br>
                            - BIC : TRZOFR21XXX
                            <br>
                            - Banque : Agent de paiement Shine 16798
                            <br>
                            <br>
                            Le prêteur joint en annexe son relevé d'identité bancaire avec la présente convention de 
                            mise à disposition de matériels.
                          </div>
                        </div>
                        <!-- Article 4 - Convention à titre onéreux (Code civil code de commerce) -->
                        
                        <br>
                        
                        <!-- Article 5 - Facturation et délai de paiement (Code de commerce) -->
                        <div class="card text-center">
                          <div class="card-header">
                            Article 5 - Facturation et délai de paiement
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
                            Conformément à l'article L441-9 du code de commerce, le prêteur émettra une facture 
                            périodique à l'emprunteur tous les mois au même jour de la date de signature de la présente 
                            convention de mise à disposition de matériels. Les factures émises à l'emprunteur par le 
                            prêteur de la présente convention de mise à disposition de matériels seront émises par 
                            voie électronique au moyen d'une signature électronique. En cas d'erreur, une facture 
                            émise à l'emprunteur par le prêteur de la présente convention de mise à disposition de 
                            matériels peut être annulée ou rectifiée.
                            <br>
                            <br>
                            Conformément à l'article L441-10 du code de commerce, le délai de paiement convenu entre les 
                            contractants de la présente convention de mise à disposition de matériels pour régler les 
                            sommes dues ne peut dépasser quarante-cinq jours après la date d'émission de la facture 
                            émise à l'emprunteur par le prêteur de la présente convention de mise à disposition de 
                            matériels.
                            <br>
                            <br>
                            Conformément à l'article L123-22 du code de commerce et à l'article L102 B du livre des 
                            procédures fiscales, les factures émises à l'emprunteur par le prêteur de la présente 
                            convention de mise à disposition de matériels seront établies en euros et en langue 
                            française, et devront être conservées pendant dix ans par les contractants.
                            <br>
                            <br>
                            Conformément à l'article 289 du code général des impôts et à l'article 242 nonies A de 
                            l'annexe 2 du code général des impôts, les factures émises à l'emprunteur par le prêteur 
                            de la présente convention de mise à disposition de matériels comporteront un certain nombre 
                            de mentions obligatoires qui sont les suivantes :
                            <br>
                            - La date de l'émission de la facture qui est la date à laquelle elle est émise.
                            <br>
                            - La numérotation de la facture qui est le numéro unique basé sur une séquence 
                            chronologique continue et sans rupture.
                            <br>
                            - La date de la mise à disposition de matériels qui est le jour effectif de la fin 
                            d'exécution de la mise à disposition de matériels.
                            <br>
                            - L'identité de l'emprunteur qui comporte la dénomination sociale de l'emprunteur, 
                            l'adresse du siège social de l'emprunteur et l'adresse de facturation si différente du 
                            siège social.
                            <br>
                            - L'identité du prêteur qui comporte la dénomination sociale du prêteur suivie du numéro 
                            siren, l'adresse du siège social du prêteur, la forme juridique et le montant du capital 
                            social du prêteur.
                            <br>
                            - Le numéro individuel d'identification à la TVA du prêteur et de l'emprunteur 
                            professionnel.
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
                            aux coordonnées bancaires du prêteur."
                            <br>
                            - Les coordonnées bancaires du prêteur.
                          </div>
                        </div>
                        <!-- Article 5 - Facturation et délais de paiement (Code de commerce) -->
                        
                        <br>
                        
                        <!-- Article 6 - Pénalités pour retard de paiement (Code de commerce, 
                        Code de procédure civile) -->
                        <div class="card text-center">
                          <div class="card-header">
                            Article 6 - Pénalités pour retard de paiement
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
                            facture émise à l'emprunteur par le prêteur de la présente convention de mise à disposition 
                            de matériels fera l'objet de pénalités de retard de paiement exigibles le jour suivant 
                            la date de règlement figurant sur toute facture émise à l'emprunteur par le prêteur de 
                            la présente convention de mise à disposition de matériels ainsi que le montant de 
                            l'indemnité forfaitaire pour frais de recouvrement due au prêteur dans le cas où les sommes 
                            dues sont réglées après cette date. Les pénalités de retard de paiement de toute facture 
                            émise à l'emprunteur par le prêteur de la présente convention de mise à disposition de 
                            matériels sont exigibles sans qu'un rappel soit nécessaire. L'emprunteur en situation de 
                            retard de paiement est de plein droit débiteur, à l'égard du prêteur, d'une indemnité 
                            forfaitaire pour frais de recouvrement, dont le montant est fixé par décret. Lorsque 
                            les frais de recouvrement exposés sont supérieurs au montant de cette indemnité 
                            forfaitaire, le prêteur peut demander une indemnisation complémentaire, sur justification.
                            <br>
                            <br>
                            Le taux de l'intérêt légal sera fixé à vingt pour cent (20%) pour tout calcul des 
                            pénalités de retard de paiement de toute facture émise à l'emprunteur par le prêteur de 
                            la présente convention de mise à disposition de matériels.
                            <br>
                            <br>
                            La formule de calcul des pénalités de retard de paiement de toute facture émise à 
                            l'emprunteur par le prêteur de la présente convention de mise à disposition de 
                            matériels est la suivante : [(taux d'intérêt légal fixé par la présente convention de mise 
                            à disposition de matériels) x (montant TTC de toute facture émise à l'emprunteur par le 
                            prêteur de la présente convention de mise à disposition de matériels)] x [(nombre de jours 
                            de retard de paiement de toute facture émise à l'emprunteur par le prêteur de la présente 
                            convention de mise à disposition de matériels)/365].
                            <br>
                            <br>
                            Le point de départ des pénalités de retard de paiement de toute facture émise à l'emprunteur 
                            par le prêteur de la présente convention de mise à disposition de matériels est le lendemain 
                            de l'échéance de toute facture émise à l'emprunteur par le prêteur de la présente convention 
                            de mise à disposition de matériels. Le point d'arrivée du calcul des pénalités de retard 
                            de paiement de toute facture émise à l'emprunteur par le prêteur de la présente convention 
                            de mise à disposition de matériels est constitué par la date d'envoi du règlement de toute 
                            facture émise à l'emprunteur par le prêteur de la présente convention de mise à disposition 
                            de matériels.
                          </div>
                        </div>
                        <!-- Article 6 - Pénalités pour retard de paiement (Code de commerce, 
                        Code de procédure civile) -->
                        
                        <br>
                        
                        <!-- Article 7 - Inventaire du matériel mis à disposition (Code civil) -->
                        <div class="card text-center">
                          <div class="card-header">
                            Article 7 - Inventaire des matériels mis à disposition
                          </div>
                          <div class="card-body">
                            Vu les articles 1372 à 1377 du code civil concernant l'acte sous signature privée,
                            <br>
                            Vu les articles 1708 à 1712 du code civil concernant les dispositions générales du contrat 
                            de louage,
                            <br>
                            Vu les articles 1875 à 1891 du code civil concernant le prêt à usage,
                            <br>
                            <br>
                            Conformément aux articles 1708, 1713, 1874 et 1875 du code civil, les matériels mis à la 
                            disposition de l'emprunteur par le prêteur de la présente convention de mise à disposition 
                            de matériels sont composés de :
                            <br>
                            - [Nombre][Nom du matériel] dont la valeur unitaire est égale à ... euros hors taxes sur 
                            la valeur ajoutée.
                            <br>
                            - [Nombre][Nom du matériel] dont la valeur unitaire est égale à ... euros hors taxes sur 
                            la valeur ajoutée.
                            <br>
                            <br>
                            Les matériels mis à la disposition de l'emprunteur par le prêteur de la présente 
                            convention de mise à disposition de matériels sont mis à disposition à compter de la date 
                            de signature de la présente convention de mise à disposition de matériels par les 
                            contractants en deux exemplaires dont l'un pour l'emprunteur et l'autre pour le prêteur, 
                            en bon état de présentation et de fonctionnement, état dans lequel l'emprunteur s'engage 
                            à les restituer à l'issue de la présente convention de mise à disposition de matériels.
                            <br>
                            <br>
                            En date de la mise à disposition des matériels à l'emprunteur par le prêteur 
                            de la présente convention de mise à disposition de matériels, les contractants dresseront 
                            un état des lieux pour prêt de matériel au site d'exploitation de l'emprunteur ayant 
                            installé les matériels mis à la disposition de l'emprunteur par le prêteur 
                            de la présente convention de mise à disposition de matériels. L'état des lieux pour prêt 
                            de matériel sera daté, paraphé, signé et tamponné par les contractants en deux exemplaires 
                            dont l'un pour l'emprunteur et l'autre pour le prêteur par acte sous signatures privées.                            
                          </div>
                        </div>
                        <!-- Article 7 - Inventaire du matériel mis à disposition (Code civil) -->
                        
                        <br>
                        
                        <!-- Article 8 - Utilisation du matériel mis à disposition (Code civil) -->
                        <div class="card text-center">
                          <div class="card-header">
                            Article 8 - Usage des matériels mis à disposition
                          </div>
                          <div class="card-body">
                            Vu les articles 1875 à 1891 du code civil concernant le prêt à usage,
                            <br>
                            Vu les articles L400-1 à L461-3 du code de l'énergie concernant les dispositions relatives 
                            au gaz,
                            <br>
                            Vu les articles R421-1 à D461-14 du code de l'énergie concernant les dispositions relatives 
                            au gaz,
                            <br>
                            Vu le code de commerce,
                            <br>
                            Vu le code du travail,
                            <br>
                            Vu le code de la recherche,
                            <br>
                            <br>
                            Conformément à l'article 1880 du code civil, l'usage des matériels mis à la disposition 
                            de l'emprunteur par le prêteur de la présente convention de mise à disposition de matériels 
                            est exclusivement servi pour la production d'un mélange gazeux de dihydrogène et de 
                            dioxygène afin de fournir du dihydrogène à un processus de valorisation du dioxyde de 
                            carbone par méthanation pour produire du méthane de synthèse grâce à la réaction de 
                            Sabatier.
                            <br>
                            <br>
                            Conformément aux articles L451-1 à L453-10 et R452-1 à D453-26 du code de l'énergie, 
                            l'emprunteur peut se prévaloir le droit d'injecter du méthane de synthèse produit par le 
                            processus susmentionné dans un réseau de gaz naturel.
                            <br>
                            <br>
                            Après, l'emprunteur ne peut se prévaloir le droit de tenir pour responsable le prêteur pour 
                            toute perte économique, sociale et environnementale que ce soit et de toute perte que ce 
                            soit dû à l'usage des matériels mis à la disposition de l'emprunteur par le prêteur de la 
                            présente convention de mise à disposition de matériels, même par cas fortuit ou force 
                            majeure.
                            <br>
                            <br>
                            Puis, l'emprunteur ne peut se prévaloir le droit d'effectuer toute recherche scientifique 
                            que ce soit et toute recherche que ce soit avec les matériels lui étant mis à disposition 
                            par le prêteur de la présente convention de mise à disposition de matériels, pour toute 
                            raison que ce soit et même en cas de force majeure.
                            <br>
                            <br>
                            Ensuite, l'emprunteur est tenu d'assurer la sécurité et le bon fonctionnement de son site 
                            d'exploitation ayant installé des matériels lui étant mis à disposition par le prêteur 
                            de la présente convention de mise à disposition de matériels avec du personnel 
                            qualifié pouvant effectivement assurer le maintien de la sécurité du site d'exploitation 
                            où les matériels lui étant mis à disposition par le prêteur de la présente convention de 
                            mise à disposition de matériels sont installés.
                          </div>
                        </div>
                        <!-- Article 8 - Utilisation du matériel mis à disposition (Code civil) -->
                        
                        <br>
                        
                        <!-- Article 9 - Engagements de l'emprunteur (Code civil) -->
                        <div class="card text-center">
                          <div class="card-header">
                            Article 9 - Engagements de l'emprunteur
                          </div>
                          <div class="card-body">
                            Vu les articles 1880 à 1887 du code civil concernant les engagements de l'emprunteur 
                            d'un prêt à usage,
                            <br>
                            <br>
                            Conformément à l'article 1880 du code civil, l'emprunteur est tenu de veiller 
                            raisonnablement à la garde et à la conservation des matériels lui étant mis à disposition 
                            par le prêteur de la présente convention de mise à disposition de 
                            matériels. L'emprunteur ne peut se servir des matériels lui étant mis à disposition par 
                            le prêteur de la présente convention de mise à disposition de 
                            matériels qu'à l'usage déterminé par la présente convention de mise à disposition de 
                            matériels; le tout à peine de dommages-intérêts, s'il y a lieu.
                            <br>
                            <br>
                            Conformément à l'article 1881 du code civil, si l'emprunteur emploie les matériels lui 
                            étant mis à disposition par le prêteur de la présente convention de mise à 
                            disposition de matériels à un usage autre que celui prévu par la présente convention 
                            de mise à disposition de matériels, ou pour un temps plus long que l'emprunteur ne le 
                            devait, l'emprunteur sera tenu de la perte arrivée des matériels lui étant mis à 
                            disposition par le prêteur de la présente convention de mise à disposition de matériels, 
                            même par cas fortuit.
                            <br>
                            <br>
                            Conformément à l'article 1885 du code civil, l'emprunteur ne peut pas retenir les 
                            matériels lui étant mis à disposition par le prêteur de la présente convention de mise à 
                            disposition de matériels par compensation de ce que le prêteur lui doit.
                          </div>
                        </div>
                        <!-- Article 9 - Engagements de l'emprunteur (Code civil) -->
                        
                        <br>
                        
                        <!-- Article 10 - Engagements du prêteur (Code civil) -->
                        <div class="card text-center">
                          <div class="card-header">
                            Article 10 - Engagements du prêteur
                          </div>
                          <div class="card-body">
                            Vu les articles 1888 à 1891 du code civil concernant les engagements de celui qui prête 
                            à usage,
                            <br>
                            <br>
                            Conformément à l'article 1888 du code civil, le prêteur ne peut retirer les matériels mis 
                            à la disposition de l'emprunteur de la présente convention de mise à disposition de matériels 
                            qu'après le terme convenu, ou, à défaut de convention, qu'après que les matériels mis à 
                            disposition ont servi à l'usage pour lequel ils ont été empruntés.
                            <br>
                            <br>
                            Conformément à l'article 1890 du code civil, pendant toute la durée de la présente 
                            convention de mise à disposition de matériels, le prêteur se tient disponible tous les 
                            jours à recevoir les demandes orales et écrites de l'emprunteur pour la conservation 
                            des matériels mis à dispostion à l'emprunteur par le prêteur de la présente 
                            convention de mise à disposition de matériels afin que l'emprunteur évite 
                            totalement quelque dépense extraordinaire, nécessaire et urgente que ce soit.
                            <br>
                            <br>
                            Conformément à l'article 1891 du code civil, les matériels mis à la disposition de 
                            l'emprunteur par le prêteur de la présente convention de mise à disposition de matériels 
                            ne présentent aucun défaut pour que les matériels mis à disposition puissent causer 
                            du préjudice à l'emprunteur.
                          </div>
                        </div>
                        <!-- Article 10 - Engagements du prêteur (Code civil) -->
                        
                        <br>
                        
                        <!-- Article 11 - Conservation du matériel mis à disposition -->
                        <div class="card text-center">
                          <div class="card-header">
                            Article 11 - Conservation des matériels mis à disposition
                          </div>
                          <div class="card-body">
                            Vu les articles 1880 à 1887 du code civil concernant les engagements de l'emprunteur,
                            <br>
                            <br>
                            Conformément à l'article 1880 du code civil, l'emprunteur ne peut se prévaloir le droit 
                            d'effectuer quelque travail que ce soit et quelque maintenance que ce soit sur les 
                            matériels lui étant mis à disposition par le prêteur de la présente convention de mise 
                            à disposition de matériels sans l'accord et la présence du prêteur. L'emprunteur est tenu de 
                            conserver raisonnablement les matériels lui étant mis à disposition par le prêteur de 
                            la présente convention de mise à disposition de matériels.
                          </div>
                        </div>
                        <!-- Article 11 - Conservation du matériel mis à disposition -->
                        
                        <br>
                        
                        <!-- Article 12 - Responsabilités (Code civil) -->
                        <div class="card text-center">
                          <div class="card-header">
                            Article 12 - Responsabilités
                          </div>
                          <div class="card-body">
                            Vu les articles 1880 à 1887 du code civil concernant les engagements de l'emprunteur 
                            d'un prêt à usage,
                            <br>
                            Vu le code des assurances,
                            <br>
                            <br>
                            L'emprunteur assume l'entière responsabilité des matériels lui étant mis à disposition par 
                            le prêteur de la présente convention de mise à disposition de matériels dès sa prise en 
                            charge et jusqu'à sa restitution. L'emprunteur est le seul responsable de tous dégâts 
                            causés aux matériels lui étant mis à disposition par le prêteur de la présente 
                            convention de mise à disposition de matériels ou du fait des matériels lui étant mis à 
                            disposition par le prêteur de la présente convention de mise à disposition de matériels et 
                            ce quelle qu'en soit la cause ou la nature. Tout matériel manquant ou dégradé mis à la 
                            disposition de l'emprunteur par le prêteur de la présente convention de mise à 
                            disposition de matériels devra être remplacé ou réparé par et à la charge de l'emprunteur. 
                            En cas de casse, de perte ou de vol, l'emprunteur s'engage à prévenir sans délai le prêteur 
                            et à effectuer les démarches nécessaires à la prise en charge du dommage par sa 
                            compagnie d'assurance.
                          </div>
                        </div>
                        <!-- Article 12 - Responsabilités (Code civil) -->
                        
                        <br>
                        
                        <!-- Article 13 - Assurances (Code des assurances) -->
                        <div class="card text-center">
                          <div class="card-header">
                            Article 13 - Assurances
                          </div>
                          <div class="card-body">
                            Vu les articles L100-1 à L195-1 du code des assurances concernant le contrat,
                            <br>
                            Vu les articles R111-1 à R195-1 du code des assurances concernant le contrat,
                            <br>
                            Vu les articles A111-1 à A160-4 du code des assurances concernant le contrat,
                            <br>
                            <br>
                            L'emprunteur s'engage à contracter les assurances nécessaires à couvrir les risques 
                            (notamment vol, dégât des eaux, incendie, évènements naturels ou tout acte de vandalisme) 
                            liés à l'utilisation des matériels lui étant mis à disposition par le prêteur de la présente 
                            convention de mise à disposition de matériels sur le lieu de l'activité de l'emprunteur.
                          </div>
                        </div>
                        <!-- Article 13 - Assurances (Code des assurances) -->
                        
                        <br>
                        
                        <!-- Article 14 - Propriété intellectuelle / Propriété industrielle 
                        (Code de la propriété intellectuelle) -->
                        <div class="card text-center">
                          <div class="card-header">
                            Article 14 - Propriété intellectuelle / Propriété industrielle
                          </div>
                          <div class="card-body">
                            Vu les articles 1875 à 1879 du code civil concernant la nature du prêt à usage,
                            
                            <br>
                            
                            Vu les articles L411-1 à L731-4 du code de la propriété intellectuelle concernant 
                            la propriété industrielle,
                            
                            <br>
                            
                            Vu les articles R611-1 à D631-2 du code de la propriété intellectuelle concernant 
                            la protection des inventions et des connaissances techniques,
                            
                            <br>
                            <br>
                            
                            Conformément à l'article 1877 du code civil, stipulant que le prêteur demeure propriétaire 
                            de la chose prêtée, les matériels mis à la disposition de l'emprunteur par le prêteur de la 
                            présente convention de mise à disposition de matériels restent la propriété du prêteur. 
                            La présente convention de mise à disposition de matériels n'implique aucun transfert 
                            de droits sur les matériels mis à la disposition de l'emprunteur par le prêteur.
                            
                            <br>
                            
                            L'emprunteur n'a pas le droit de céder les matériels lui étant mis à disposition par 
                            le prêteur ou de les sous-louer ou de les déplacer à un lieu autre que celui prévu par la 
                            présente convention de mise à disposition de matériels.
                            
                            <br>
                            <br>
                            
                            Conformément aux articles L611-1 à L615-22 du code de la propriété intellectuelle, 
                            le prêteur exploite de manière exhaustive les inventions tombées dans le domaine 
                            public dont les brevets sont les suivants :
                            
                            <br>
                            
                            - Brevet US4124463A intitulé "Cellule électrolytique" dont l'inventeur est Archie Blue.
                            
                            <br>
                            
                            - Brevet US5149407A intitulé "Procédé et appareil pour la production de gaz 
                            combustible et la libération accrue d’énergie thermique à partir de ce gaz" 
                            dont l'inventeur est Stanley Meyer.
                            
                            <br>
                            
                            - Brevet US4936961A intitulé "Procédé de production d’un gaz combustible" 
                            dont l'inventeur est Stanley Meyer.
                            
                            <br>
                            
                            - Brevet US4798661A intitulé "Circuit de contrôle de tension du générateur de 
                            gaz" dont l'inventeur est Stanley Meyer.
                            
                            <br>
                            
                            - Brevet CA1234773A intitulé "Générateur d’hydrogène à cavité résonnante 
                            qui fonctionne avec un potentiel électrique à tension pulsée" 
                            dont l'inventeur est Stanley Meyer.
                            
                            <br>
                            
                            - Brevet CA1234774A intitulé "Générateur d’hydrogène" 
                            dont l'inventeur est Stanley Meyer.
                            
                            <br>
                            
                            - Brevet WO1992007861A1 intitulé "Circuits de commande pour une 
                            pile produisant de l’hydrogène gazeux" dont l'inventeur est Stanley Meyer.
                            
                            <br>
                            <br>
                            
                            Conformément aux articles L615-1 à L615-22 du code de la propriété intellectuelle, 
                            le prêteur exploite de manière exhaustive les inventions susmentionnées pour la fabrication 
                            des matériels mis à la disposition de l'emprunteur par le prêteur de la présente 
                            convention de mise à disposition de matériels.
                            
                            <br>
                            
                            L'exploitation de ces inventions susmentionnées par le prêteur ne porte pas 
                            atteinte aux droits des propriétaires des brevets susmentionnés et ne constitue pas une 
                            contrefaçon de quelque manière que ce soit.
                            
                            <br>
                            <br>
                            
                            Conformément à l'article L621-1 du code de la propriété intellectuelle, 
                            le prêteur reste exclusivement propriétaire des secrets de fabrique des matériels mis à la 
                            disposition de l'emprunteur par le prêteur de la présente convention de mise à 
                            disposition de matériels.
                            
                            <br>
                            
                            L'emprunteur ne peut se prévaloir des droits des secrets de fabrique des matériels lui étant 
                            mis à disposition par le prêteur de la présente convention de mise à 
                            disposition de matériels.
                            
                            <br>
                            
                            Le prêteur peut exercer toutes actions en justice contre l'emprunteur ou des tiers pour 
                            violation des secrets de fabrique des matériels mis à la disposition de l'emprunteur par le 
                            prêteur de la présente convention de mise à disposition de matériels.
                            
                            <br>
                            <br>
                            
                            Conformément aux articles L615-1 à L615-22 du code de la propriété intellectuelle, 
                            l'emprunteur ne peut se prévaloir d'exercer des actions en justice contre le prêteur 
                            pour contrefaçon des matériels lui étant mis à disposition par le 
                            prêteur de la présente convention de mise à disposition de matériels. 
                          </div>
                        </div>
                        <!-- Article 14 - Propriété intellectuelle / Propriété industrielle 
                        (Code de la propriété intellectuelle) -->
                        
                        <br>
                        
                        <!-- Article 15 - Protection du secret des affaires / Confidentialité (Code de commerce) -->
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
                            les matériels mis à la disposition de l'emprunteur par le prêteur de la présente convention 
                            de mise à disposition de matériels sont protégés au titre du secret des affaires.
                            
                            <br>
                            <br>
                            
                            Conformément aux articles L151-2 à L151-3 du code de commerce concernant la détention 
                            légitime et l'obtention licite d'un secret des affaires, le prêteur est l'unique détenteur 
                            légitime du secret des affaires des matériels mis à la disposition de l'emprunteur par le 
                            prêteur de la présente convention de mise à disposition de matériels.
                            
                            <br>
                            <br>
                            
                            Conformément aux articles L151-4 à L151-6 du code de commerce concernant l'obtention 
                            illicite, l'utilisation illicite et la divulgation illicite du secret des affaires, 
                            l'emprunteur ne peut se prévaloir le droit d'obtenir, d'utiliser et de divulguer 
                            tout secret des affaires des matériels lui étant mis à disposition 
                            par le prêteur de la présente convention de mise à disposition de matériels.
                            
                            <br>
                            <br>
                            
                            Conformément aux articles L152-1 à L152-8, L153-1 à L153-2, R152-1, R153-1 à R153-10 du 
                            code de commerce concernant les actions en prévention, en cessation ou en réparation 
                            d'une atteinte au secret des affaires et les mesures générales de protection du 
                            secret des affaires devant les juridictions civiles ou commerciales, le prêteur peut 
                            exercer des actions en justice contre l'emprunteur ou des tiers pour atteinte au secret 
                            des affaires des matériels mis à la disposition de l'emprunteur par le prêteur de la 
                            présente convention de mise à disposition de matériels.
                          </div>
                        </div>
                        <!-- Article 15 - Protection du secret des affaires / Confidentialité (Code de commerce) -->
                        
                        <br>
                        
                        <!-- Article 16 - Exclusivité commerciale (Code de commerce) -->
                        <div class="card text-center">
                          <div class="card-header">
                            Article 16 - Exclusivité commerciale
                          </div>
                          <div class="card-body">
                            Vu les articles L330-1 à L330-3 du code de commerce concernant les clauses d'exclusivité,
                            <br>
                            Vu les articles R330-1 à R330-2 du code de commerce concernant les clauses d'exclusivité,
                            <br>
                            <br>
                            Conformément aux articles L330-1 à L330-2 du code de commerce, l'emprunteur ne peut se 
                            prévaloir le droit de faire usage d'objets semblables ou complémentaires en 
                            provenance d'un autre fournisseur par rapport aux matériels lui étant mis à disposition par 
                            le prêteur de la présente convention de mise à disposition de matériels.
                          </div>
                        </div>
                        <!-- Article 16 - Exclusivité commerciale (Code de commerce) -->
                        
                        <br>
                        
                        <!-- Article 17 - Pratiques anticoncurrentielles / Pratiques prohibées (Code de commerce) -->
                        <div class="card text-center">
                          <div class="card-header">
                            Article 17 - Pratiques anticoncurrentielles / Pratiques prohibées
                          </div>
                          <div class="card-body">
                            Vu les articles L420-1 à L420-7 du code de commerce concernant les pratiques 
                            anticoncurrentielles,
                            <br>
                            Vu les articles L442-1 à L442-11 du code de commerce concernant les pratiques 
                            commerciales déloyales entre entreprises,
                            <br>
                            Vu les articles L481-1 à L483-11 du code de commerce concernant les actions en 
                            dommages et intérêts du fait des pratiques anticoncurrentielles,
                            <br>
                            Vu les articles R420-1 à R420-5 du code de commerce concernant les pratiques 
                            anticoncurrentielles,
                            <br>
                            Vu les articles R442-1 à R442-4 du code de commerce concernant les pratiques 
                            commerciales déloyales entre entreprises,
                            <br>
                            Vu les articles R481-1 à R483-14 du code de commerce concernant les actions en dommages 
                            et intérêts du fait des pratiques anticoncurrentielles,
                            <br>
                            <br>
                            Le prêteur peut exercer des actions en dommages et intérêts contre l'emprunteur du fait des 
                            pratiques anticoncurrentielles, déloyales et prohibées commises par l'emprunteur envers le 
                            prêteur par rapport aux matériels mis à la disposition de l'emprunteur par le prêteur de la 
                            présente convention de mise à disposition de matériels.
                          </div>
                        </div>
                        <!-- Article 17 - Pratiques anticoncurrentielles / Pratiques prohibées (Code de commerce) -->
                        
                        <br>
                        
                        <!-- Article 18 - Pouvoirs d'enquête (Code de commerce) -->
                        <div class="card text-center">
                          <div class="card-header">
                            Article 18 - Pouvoirs d'enquête
                          </div>
                          <div class="card-body">
                            Vu les articles L450-1 à L450-10 du code de commerce concernant les pouvoirs d'enquête,
                            <br>
                            Vu les articles L461-1 à L464-10 du code de commerce concernant l'autorité de la 
                            concurrence,
                            <br>
                            Vu les articles R450-1 à R450-8 du code de commerce concernant les pouvoirs d'enquête,
                            <br>
                            Vu les articles R461-1 à R464-31 du code de commerce concernant l'autorité de la 
                            concurrence,
                            <br>
                            Vu les articles A450-1 à A450-3 du code de commerce concernant les pouvoirs d'enquête,
                            <br>
                            Vu les articles L110-1 à L191-1 du code de l'environnement concerannt les dispositions 
                            communes,
                            <br>
                            Vu les articles L501-1 à L597-46 du code de l'environnement concernant la prévention 
                            des pollutions, des risques et des nuisances,
                            <br>
                            Vu les articles R121-1 à D181-57 du code de l'environnement concernant les dispositions 
                            communes,
                            <br>
                            Vu les aticles D510-1 à R596-17 du code de l'environnement concernant la prévention 
                            des pollutions, des risques et des nuisances,
                            <br>
                            Vu le code du travail,
                            <br>
                            Vu le code de procédure pénale,
                            <br>
                            Vu le livre des procédures fiscales,
                            <br>
                            <br>
                            L'emprunteur est tenu de prévenir sans délai le prêteur en cas de toute enquête publique 
                            que ce soit, de toute enquête environnementale que ce soit, de toute enquête judiciaire 
                            que ce soit, de toute enquête administrative que ce soit, de toute enquête fiscale que ce 
                            soit et de toute enquête que ce soit sur son site d'exploitation ayant installé les 
                            matériels lui étant mis à disposition par le prêteur de la présente convention de mise à 
                            disposition de matériels pouvant impliquer les matériels lui étant mis à disposition par 
                            le prêteur de la présente convention de mise à disposition de matériels.
                          </div>
                        </div>
                        <!--Article 18 - Pouvoirs d'enquête (Code de commerce)  -->
                        
                        <br>
                        
                        <!-- Article 19 - Normes / Qualité (Code de l'environnement) -->
                        <div class="card text-center">
                          <div class="card-header">
                            Article 19 - Normes / Qualité
                          </div>
                          <div class="card-body">
                            Vu le code de l'environnement,
                            <br>
                            Vu la directive 2006/42/CE du Parlement européen et du Conseil du 17 mai 2006 relative 
                            aux machines et modifiant la directive 95/16/CE,
                            <br>
                            <br>
                            En application de l'annexe 1 de la directive 2006/42/CE du Parlement européen et du 
                            Conseil du 17 mai 2006 relative aux machines et modifiant la directive 95/16/CE, les 
                            matériels mis à la disposition de l'emprunteur par le prêteur de la présente 
                            convention de mise à disposition de matériels ont suivi un management de la qualité 
                            mettant en application les exigences essentielles de sécurité et de santé.
                          </div>
                        </div>
                        <!-- Article 19 - Normes / Qualité (Code de l'environnement) -->
                        
                        <br>
                        
                        <!-- Article 20 - Zone en atmosphère explosive (Code du travail, Code de l'environnement, 
                        Reglement UE) -->
                        <div class="card text-center">
                          <div class="card-header">
                            Article 20 - Zones atmosphères explosives
                          </div>
                          <div class="card-body">
                            Vu la directive 94/9/CE du Parlement européen et du Conseil du 23 mars 1994 concernant 
                            le rapprochement des législations des États membres pour les appareils et les systèmes 
                            de protection destinés à être utilisés en atmosphères explosibles,
                            <br>
                            Vu les articles L4111-1 à L4831-1 du code du travail concernant la santé et la sécurité 
                            au travail,
                            <br>
                            Vu les articles R4121-1 à R4822-1 du code du travail concernant la santé et la sécurité 
                            au travail,
                            <br>
                            <br>
                            Conformément à l'alinéa 4 de l'article premier de la directive 94/9/CE du Parlement 
                            européen et du Conseil du 23 mars 1994, les matériels mis à la disposition de l'emprunteur 
                            par le prêteur de la présente convention de mise à disposition de matériels pourraient 
                            exclusivement présenter un danger d'explosion lors de l'apparition de la molécule de 
                            dihydrogène. Ainsi, les matériels mis à la disposition de l'emprunteur par 
                            le prêteur de la présente convention de mise à disposition de matériels sont exclus 
                            du champ d'application de la directive 94/9/CE du Parlement européen et du Conseil du 
                            23 mars 1994.
                            <br>
                            <br>
                            Conformément aux articles L4111-1 à L4831-1 et R4121-1 à R4822-1 du code du travail, 
                            l'emprunteur est tenu d'évaluer les risques et de mettre en oeuvre les actions de 
                            prévention pour la santé et la sécurité des travailleurs sur son site d'exploitation 
                            par rapport aux matériels lui étant mis à disposition par le prêteur de la présente 
                            convention de mise à disposition de matériels.
                          </div>
                        </div>
                        <!-- Article 20 - Zone en atmosphère explosive (Code du travail, Code de l'environnement, 
                        Reglement UE) -->
                        
                        <br>
                        
                        <!-- Article 21 - Protection du personnel, des utilisateurs et de l'environnement par rapport 
                        au matériel mis à disposition -->
                        <div class="card text-center">
                          <div class="card-header">
                            Article 21 - Protection du personnel, des utilisateurs et de l'environnement des 
                            matériels mis à disposition
                          </div>
                          <div class="card-body">
                            Vu les articles L4111-1 à L4831-1 du code du travail concernant la santé et la sécurité 
                            au travail,
                            <br>
                            Vu les articles R4121-1 à R4822-1 du code du travail concernant la santé et la sécurité 
                            au travail,
                            <br>
                            Vu les articles L1331-1 à L1338-5 du code de la santé publique concernant la prévention 
                            des risques sanitaires liés à l'environnement et au travail,
                            <br>
                            Vu les articles L1340-1 à L1343-4 du code de la santé publique concernant la 
                            toxicovigilance,
                            <br>
                            Vu les articles R1331-1 à R1339-4 du code de la santé publique concernant la prévention 
                            des risques sanitaires liés à l'environnement et au travail,
                            <br>
                            Vu les articles R1340-1 à R1343-3 du code de la santé publique concernant 
                            la toxicovigilance,
                            <br>
                            <br>
                            Premièrement, l'emprunteur est tenu de mettre en place la prévention de certains risques 
                            d'exposition et des risques liés à certaines activités ou opérations par rapport à 
                            l'utilisation des matériels lui étant mis à disposition par le prêteur de la présente 
                            convention de mise à disposition de matériels sur son site d'exploitation ayant installé 
                            des matériels lui étant mis à disposition par le prêteur de la présente convention de mise 
                            à disposition de matériels.
                            <br>
                            <br>
                            Après, l'emprunteur est aussi tenu de s'équiper d'équipements de travail et moyens de 
                            protection par rapport à l'utilisation des matériels lui étant mis à disposition par le 
                            prêteur de la présente convention de mise à disposition de matériels sur son site 
                            d'exploitation ayant installé des matériels lui étant mis à disposition par le prêteur de 
                            la présente convention de mise à disposition de matériels.
                            <br>
                            <br>
                            Puis, l'emprunteur est également tenu de mettre en place la prévention des risques 
                            sanitaires liés à l'environnement, au travail et à la toxicovigilance par rapport à 
                            l'utilisation des matériels lui étant mis à disposition par le prêteur de la présente 
                            convention de mise à disposition de matériels sur son site d'exploitation ayant installé 
                            des matériels lui étant mis à disposition par le prêteur de la présente convention de mise 
                            à disposition de matériels.
                          </div>
                        </div>
                        <!-- Article 21 - Protection du personnel, des utilisateurs et de l'environnement par rapport 
                        au matériel mis à disposition -->
                        
                        <br>
                        
                        <!-- Article 22 - Prévention des pollutions, des risques et des nuisances -->
                        <div class="card text-center">
                          <div class="card-header">
                            Article 22 - Prévention des pollutions, des risques et des nuisances
                          </div>
                          <div class="card-body">
                            Vu les articles L120-1 à L127-10 et R121-1 à D128-19 du code de l'environnement concernant 
                            l'information et la participation des citoyens,
                            <br>
                            Vu les articles L220-1 à L229-69 et R221-1 à R229-102 du code de l'environnement concernant 
                            l'air et l'atmosphère,
                            <br>
                            Vu les articles L501-1 à L597-46 et D510-1 à R596-17 du code de l'environnement concernant 
                            la prévention des pollutions, des risques et des nuisances,
                            <br>
                            <br>
                            L'emprunteur est tenu de prendre des mesures essentielles et nécessaires pour prévenir les 
                            pollutions, les risques et les nuisances pouvant intervenir lors de l'usage des matériels 
                            lui étant mis à disposition par le prêteur de la présente convention de mise à disposition 
                            de matériels. Ces mesures doivent se tenir, de manière non exhaustive, au moins sur les 
                            points suivants :
                            <br>
                            - Information mise à la disposition des cityons pour les risques liés à l'environnement
                            <br>
                            - Participation des citoyens pour les risques liés à l'environnement
                            <br>
                            - Déclaration administrative pour établir une installation classée pour la protection de 
                            l'environnement
                            <br>
                            - Protection de l'air et de l'atmosphère
                            <br>
                            - Lutte contre l'effet de serre
                            <br>
                            - Protection des sites contre les sols pollués
                            <br>
                            - Protection contre les produits et les équipements à risques
                            <br>
                            - Prévention des risques naturels
                            <br>
                            - Prévention de la pollution sonore
                            <br>
                            - Protection du cadre de vie
                            <br>
                            - Prévention des nuisances visuelles
                            <br>
                            - Prévention des nuisances lumineuses
                            <br>
                            <br>
                            Les matériels mis à la disposition de l'emprunteur par le prêteur de la présente convention 
                            de mise à disposition de matériels ne présentent aucune nuisance atmosphérique, sonore, 
                            visuelle, lumineuse, corporelle et olfactive que ce soit.
                            <br>
                            <br>
                            Le mélange gazeux de dihydrogène et de dioxygène produit par les matériels mis à la 
                            disposition de l'emprunteur par le prêteur de la présente convention de mise à disposition 
                            de matériels pourrait présenter un danger d'explosion et un danger d'inflammation.
                          </div>
                        </div>
                        <!-- Article 22 - Prévention des pollutions, des risques et des nuisances -->
                        
                        <br>
                        
                        <!-- Article 23 - Machines (Reglement UE) -->
                        <div class="card text-center">
                          <div class="card-header">
                            Article 23 - Machines
                          </div>
                          <div class="card-body">
                            Vu la directive 2006/42/CE du Parlement européen et du Conseil du 17 mai 2006 relative 
                            aux machines et modifiant la directive 95/16/CE,
                            <br>
                            <br>
                            Conformément à l'article premier de la directive 2006/42/CE du Parlement européen et 
                            du Conseil du 17 mai 2006 relative aux machines et modifiant la directive 95/16/CE, 
                            les matériels mis à la disposition de l'emprunteur par le prêteur de la présente convention 
                            de mise à disposition de matériels respectent les exigences essentielles de sécurité et 
                            de santé les concernant, telles que définies à l'annexe 1 de la directive 2006/42/CE du 
                            Parlement européen et du Conseil du 17 mai 2006 relative aux machines et modifiant la 
                            directive 95/16/CE.
                          </div>
                        </div>
                        <!-- Article 23 - Machines (Reglement UE) -->
                        
                        <br>
                        
                        <!-- Article 24 - Equipements sous pression (Code de l'environnement, Reglement UE) -->
                        <div class="card text-center">
                          <div class="card-header">
                            Article 24 - Equipements sous pression
                          </div>
                          <div class="card-body">
                            Vu la directive 97/23/CE du Parlement européen et du Conseil du 29 mai 1997 relative 
                            au rapprochement des législations des États membres concernant les équipements sous 
                            pression,
                            <br>
                            Vu la directive 2006/42/CE du Parlement européen et 
                            du Conseil du 17 mai 2006 relative aux machines et modifiant la directive 95/16/CE,
                            <br>
                            <br>
                            Conformément au point 3.6 de l'article premier de la directive 97/23/CE du Parlement 
                            européen et du Conseil du 29 mai 1997, les matériels mis à la disposition de l'emprunteur 
                            par le prêteur de la présente convention de mise à disposition de matériels sont des 
                            équiquements qui relèveraient au plus de la catégorie 1 en application de l'article 9 
                            de la directive 97/23/CE du Parlement européen et du Conseil du 29 mai 1997 et qui sont 
                            visés par la directive 2006/42/CE du Parlement européen et du Conseil du 17 mai 2006 
                            relative aux machines et modifiant la directive 95/16/CE. Ainsi, les matériels mis 
                            à la disposition de l'emprunteur par le prêteur de la présente convention de mise à 
                            disposition de matériels sont exclus du champ d'application de la directive 97/23/CE 
                            du Parlement européen et du Conseil du 29 mai 1997.
                          </div>
                        </div>
                        <!-- Article 24 - Equipements sous pression (Code de l'environnement, Reglement UE) -->
                        
                        <br>
                        
                        <!-- Article 25 - Equipements de mesure (Reglement UE) -->
                        <div class="card text-center">
                          <div class="card-header">
                            Article 25 - Equipements de mesure
                          </div>
                          <div class="card-body">
                            Vu la directive 2004/22/CE du Parlement européen et du Conseil du 31 mars 2004 sur les 
                            instruments de mesure,
                            <br>
                            <br>
                            Conformément à l'article premier de la directive 2004/22/CE du Parlement européen 
                            et du Conseil du 31 mars 2004 sur les instruments de mesure, les matériels mis 
                            à la disposition de l'emprunteur par le prêteur de la présente convention de mise à 
                            disposition de matériels peuvent comprendre des instruments de mesure qui respectent les 
                            exigences essentielles de sécurité et de santé définies dans la directive 2004/22/CE du 
                            Parlement européen et du Conseil du 31 mars 2004.
                          </div>
                        </div>
                        <!-- Article 25 - Equipements de mesure (Reglement UE) -->
                        
                        <br>
                        
                        <!-- Article 26 - Basse tension et haute tension (Reglement UE) -->
                        <div class="card text-center">
                          <div class="card-header">
                            Article 26 - Basse tension / Haute tension
                          </div>
                          <div class="card-body">
                            Vu la directive 2014/35/UE du Parlement européen et du Conseil du 26 février 2014 
                            relative à l’harmonisation des législations des États membres concernant la mise 
                            à disposition sur le marché du matériel électrique destiné à être employé dans 
                            certaines limites de tension,
                            <br>
                            <br>
                            Conformément à l'annexe 2 de la directive 2014/35/UE du Parlement européen et du Conseil 
                            du 26 février 2014, les matériels mis à la disposition de l'emprunteur par le prêteur de 
                            la présente convention de mise à disposition de matériels sont destinés à être utilisé 
                            dans une atmosphère explosive au site d'exploitation de l'emprunteur. Ainsi, la directive 
                            2014/35/UE du Parlement européen et du Conseil du 26 février 2014 ne s'applique pas aux 
                            matériels mis à la disposition de l'emprunteur par le prêteur de la présente convention de 
                            mise à disposition de matériels.
                          </div>
                        </div>
                        <!-- Article 26 - Basse tension et haute tension (Reglement UE) -->
                        
                        <br>
                        
                        <!-- Article 27 - Compatibilité électromagnétique (Reglement UE) -->
                        <div class="card text-center">
                          <div class="card-header">
                            Article 27 - Compatibilité électromagnétique
                          </div>
                          <div class="card-body">
                            Vu la directive 2014/30/UE du Parlement européen et du Conseil du 26 février 2014 
                            relative à l’harmonisation des législations des États membres concernant la compatibilité 
                            électromagnétique,
                            <br>
                            <br>
                            Conformément au point (d) de l'alinéa 2 de l'article 2 de la directive 2014/30/UE du 
                            Parlement européen et du Conseil du 26 février 2014, les matériels mis à la disposition 
                            de l'emprunteur par le prêteur de la présente convention de mise à disposition de matériels 
                            sont des équiements dont les caractéristiques physiques impliquent par leur nature même 
                            qu’ils sont incapables de produire ou de contribuer à produire des émissions 
                            électromagnétiques qui dépassent un niveau permettant aux équipements hertziens et de 
                            télécommunications et aux autres équipements de fonctionner comme prévu; et qu’ils 
                            fonctionnent sans dégradation inacceptable en présence de perturbations 
                            électromagnétiques normalement présentes lors de l’usage prévu de la présente convention 
                            de mise à disposition de matériels. Ainsi, la directive 2014/30/UE du 
                            Parlement européen et du Conseil du 26 février 2014 ne s'applique pas aux matériels mis 
                            à la disposition de l'emprunteur par le prêteur de la présente convention de mise à 
                            disposition de matériels.
                          </div>
                        </div>
                        <!-- Article 27 - Compatibilité électromagnétique (Reglement UE) -->
                        
                        <br>
                        
                        <!-- Article 28 - Réglement REACH (Reglement UE) -->
                        <div class="card text-center">
                          <div class="card-header">
                            Article 28 - Réglement REACH
                          </div>
                          <div class="card-body">
                            Vu le règlement (CE) numéro 1907/2006 du Parlement européen et du Conseil du 18 décembre 
                            2006 concernant l'enregistrement, l'évaluation et l'autorisation des substances chimiques, 
                            ainsi que les restrictions applicables à ces substances (REACH), instituant une agence 
                            européenne des produits chimiques, modifiant la directive 1999/45/CE et abrogeant le 
                            règlement (CEE) numéro 793/93 du Conseil et le règlement (CE) numéro 1488/94 de la 
                            Commission ainsi que la directive 76/769/CEE du conseil et les directives 91/155/CEE, 
                            93/67/CEE, 93/105/CE et 2000/21/CE de la Commission,
                            <br>
                            <br>
                            Conformément à l'article 2 et à l'alinéa 9 de l'annexe 5 du règlement (CE) numéro 
                            1907/2006 du Parlement européen et du Conseil du 18 décembre 2006, certains matériels 
                            mis à la disposition de l'emprunteur par le prêteur par la présente convention de mise à 
                            disposition de matériels produisent des substances élémentaires de base telles que le 
                            dihydrogène et le dioxygène pour lesquelles les dangers et risques sont déjà bien connus et 
                            ces substances sont également des intermédiaires isolés restant sur le site d'exploitation 
                            de l'emprunteur. Ainsi, les contractants ne sont pas tenus de soumettre une demande 
                            d'enregistrement des substances susmentionnées auprès de l'agence européenne des produits 
                            chimiques en vertu du titre 2 du règlement (CE) numéro 1907/2006 du Parlement européen 
                            et du Conseil du 18 décembre 2006.
                            <br>
                            <br>
                            Conformément au règlement (CE) numéro 1907/2006 du Parlement européen et du Conseil du 
                            18 décembre 2006, l'emprunteur est tenu de soumettre toute demande administrative nécessaire 
                            pour des substances chimiques présentes sur son site d'exploitation et n'étant pas 
                            exemptées des titres 2, 5 et 6 du règlement (CE) numéro 1907/2006 du Parlement européen 
                            et du Conseil du 18 décembre 2006.
                          </div>
                        </div>
                        <!-- Article 28 - Réglement REACH (Reglement UE) -->
                        
                        <br>
                        
                        <!-- Article 29 - Substances dangereuses (Reglement UE) -->
                        <div class="card text-center">
                          <div class="card-header">
                            Article 29 - Substances dangereuses
                          </div>
                          <div class="card-body">
                            Vu la directive 2012/18/UE du Parlement européen et du Conseil du 4 juillet 2012 
                            concernant la maîtrise des dangers liés aux accidents majeurs impliquant des 
                            substances dangereuses, modifiant puis abrogeant la directive 96/82/CE du Conseil,
                            <br>
                            <br>
                            Conformément à l'article premier de la directive 2012/18/UE du Parlement européen et
                            du Conseil du 4 juillet 2012 concernant la maîtrise des dangers liés aux accidents 
                            majeurs impliquant des substances dangereuses, modifiant puis abrogeant la directive 
                            96/82/CE du Conseil, les matériels mis à la disposition de l'emprunteur par le prêteur de la 
                            présente convention de mise à disposition de matériels ne contiennent aucune substance 
                            dangereuse que ce soit.
                            <br>
                            <br>
                            Conformément aux articles 2 et 5 de la directive 2012/18/UE du Parlement européen et
                            du Conseil du 4 juillet 2012 concernant la maîtrise des dangers liés aux accidents 
                            majeurs impliquant des substances dangereuses, modifiant puis abrogeant la directive 
                            96/82/CE du Conseil, l'emprunteur est tenu de prendre toutes les mesures qui s'imposent 
                            pour prévenir les accidents majeurs et pour en limiter les conséquences pour la 
                            santé humaine et l'environnement au sein de son établissement où les matériels lui étant 
                            mis à disposition par le prêteur de la présente convention de mise à disposition de 
                            matériels sont installés.
                          </div>
                        </div>
                        <!-- Article 29 - Substances dangereuses (Reglement UE) -->
                        
                        <br>
                        
                        <!-- Article 30 - Résiliation de la convention (Code civil) -->
                        <div class="card text-center">
                          <div class="card-header">
                            Article 30 - Résiliation de la convention
                          </div>
                          <div class="card-body">
                            Vu les articles 1210 à 1215 du code civil concernant la durée du contrat,
                            <br>
                            Vu les articles L640-1 à L645-12 du code de commerce concernant la liquidation 
                            judiciaire et du rétablissement professionnel,
                            <br>
                            Vu les articles R640-1 à R645-25 du code de commerce concernant la liquidation judiciaire et 
                            du rétablissement professionnel,
                            <br>
                            <br>
                            Conformément à l'article 1210 du code civil et aux articles L640-1 à L640-6, 
                            R640-1 à R640-2 du code de commerce, chaque contractant peut, à tout moment et 
                            pour tout motif, résilier la présente convention de mise à disposition de matériels. Le 
                            contractant désireux de résilier la présente convention de mise à disposition de matériels 
                            devra notifier son intention à l'autre contractant par lettre recommandée avec accusé de 
                            réception quinze jours au moins avant la date retenue pour la résiliation.
                          </div>
                        </div>
                        <!-- Article 30 - Résiliation de la convention (Code civil) -->
                        
                        <br>
                        
                        <!-- Article 31 - Modification de la convention (Code civil) -->
                        <div class="card text-center">
                          <div class="card-header">
                            Article 31 - Modification de la convention
                          </div>
                          <div class="card-body">
                            Vu les articles 1100 à 1303-4 du code civil concernant les sources d'obligations,
                            <br>
                            Vu les articles 1875 à 1891 du code civil concernant le prêt à usage,
                            <br>
                            <br>
                            Conformément aux articles 1101 à 1231-7 du code civil concernant le contrat, toute 
                            modification apportée à la présente convention de mise à disposition de matériels devra 
                            faire l'objet d'un avenant dûment signé par les contractants.
                          </div>
                        </div>
                        <!-- Article 31 - Modification de la convention (Code civil) -->
                        
                        <br>
                        
                        <!-- Article 32 - Réglement des litiges (Code de commerce) -->
                        <div class="card text-center">
                          <div class="card-header">
                            Article 32 - Réglement des litiges
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
                            Conformément aux articles L721-1 à L721-8 et R721-1 à R721-22 du code de commerce 
                            concernant l'institution et la compétence du tribunal de commerce, les contractants 
                            s'engagent à rechercher une solution amiable à tout différend né de l'application ou 
                            de l'interprétation de la présente convention de mise à disposition de matériels. À défaut 
                            de solution amiable, le litige sera tranché par le tribunal de commerce de Paris.
                          </div>
                        </div>
                        <!-- Article 32 - Réglement des litiges (Code de commerce) -->
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
                        Conformément aux articles 1112 à 1187 et 1372 à 1377 du code civil, la présente convention 
                        de mise à disposition de matériels a été établie par acte sous signatures privées par 
                        les contractants.
                        <br>
                        <br>
                        <!-- Lieu et date des signatures et cachets des cocontractants (Code civil) -->
                        <div class="card text-center">
                          <div class="card-header">
                            Lieu et date des signatures et cachets des contractants
                          </div>
                          <div class="card-body">
                            En date du ... situé au ..., la présente convention de mise à disposition de matériels a 
                            été signée et tamponnée par l'emprunteur et le prêteur.
                          </div>
                        </div>
                        <!-- Lieu et date des signatures et cachets des cocontractants (Code civil) -->
    
                        <br>
                        
                        <!-- Nombre d'exemplaires de la présente convention (Code civil) -->
                        <div class="card text-center">
                          <div class="card-header">
                            Nombre d'exemplaires de la convention
                          </div>
                          <div class="card-body">
                            La présente convention de mise à disposition de matériels est faite en deux exemplaires 
                            dont l'un pour l'emprunteur et l'autre pour le prêteur.
                          </div>
                        </div>
                        <!-- Nombre d'exemplaires de la présente convention (Code civil) -->
    
                        <br>
                        
                        <!-- Approbation de la présente convention (Code civil) -->
                        <div class="card text-center">
                          <div class="card-header">
                            Approbation de la convention
                          </div>
                          <div class="card-body">
                            La présente convention de mise à disposition de matériels a été lue et approuvée 
                            par l'emprunteur et le prêteur.
                          </div>
                        </div>
                        <!-- Visa de la présente convention (Code civil) -->
    
                        <br>
                        
                        <!-- Signature et cachet de l'emprunteur -->
                        <div class="card text-center">
                          <div class="card-header">
                            Signature et cachet de l'emprunteur
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
                        <!-- Signature et cachet de l'emprunteur -->
    
                        <br>
                        
                        <!-- Signature et cachet du prêteur -->
                        <div class="card text-center">
                          <div class="card-header">
                            Signature et cachet du prêteur
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
                        <!-- Signature et cachet du prêteur -->
                                              
                      </div>
                    </div>
                    <!-- Signatures et cachets des cocontractants  -->
                    
                  </div>
                </div>
                <!-- Convention de mise à disposition de matériels -->
                
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
            'header-center': "Convention de mise à disposition de matériels",
            'footer-right': '[page] sur [topage]',
            'footer-left': 'Société Holomorphe [SIREN : 883632556]'
        }

        path_wkthmltopdf = "C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe"

        config = pdfkit.configuration(
            wkhtmltopdf=path_wkthmltopdf
        )

        pdfkit.from_string(
            body,
            "Mise_A_Disposition\\Mise_A_Disposition_De_Materiels_[Societe_Holomorphe].pdf",
            configuration=config,
            options=options
        )

        """
        <!--
        <!--  -->
        <div class="card text-center">
          <div class="card-header">
            
          </div>
          <div class="card-body">
            
          </div>
        </div>
        <!--  -->
        -->
        """

    # ok
    def test_etat_lieux_pret_materiels(self):
        print("test_etat_lieux_pret_materiels")

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

            <title>Etat des lieux pour prêt de matériel</title>
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
                                <th scope="col">E-mail professionnel</th>
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
                <!-- Contact -->

                <br>

                <!-- Etat des lieux pour prêt de matériels  -->
                <div class="card text-center">
                  <div class="card-header">
                    État des lieux pour prêt de matériels
                  </div>
                  <div class="card-body">
                    <!-- Contractants -->
                    <div class="card text-center">
                      <div class="card-header">
                        Contractants
                      </div>
                      <div class="card-body">
                        <!-- Emprunteur -->
                        <div class="card text-center">
                          <div class="card-header">
                            Emprunteur
                          </div>
                          <div class="card-body">
                            L'emprunteur est une personne morale désignée par les informations suivantes :
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
                          </div>
                        </div>
                        <!-- Emprunteur -->

                        <br>

                        <!-- Prêteur -->
                        <div class="card text-center">
                          <div class="card-header">
                            Prêteur
                          </div>
                          <div class="card-body">
                            Le prêteur est une personne morale désignée par les informations suivantes :
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
                            - Numéro de téléphone : 00.33.7.49.16.33.29
                          </div>
                        </div>
                        <!-- Prêteur -->
                      </div>
                    </div>
                    <!-- Contractants -->

                    <br>

                    <!-- Inventaire des matériels mis à disposition -->
                    <div class="card text-center">
                      <div class="card-header">
                        Inventaire des matériels mis à disposition
                      </div>
                      <div class="card-body">
                        <table class="table table-bordered">
                          <thead>
                            <tr>
                              <th scope="col">Désignations</th>
                              <th scope="col">Quantité</th>
                              <th scope="col">État général du matériel</th>
                              <th scope="col">Remarques</th>
                            </tr>
                          </thead>
                          <tbody>
                            <tr>
                              <td>
                                <br>
                                <br>
                                <br>
                                <br>
                                <br>
                              </td>
                              <td>
                                <br>
                                <br>
                                <br>
                                <br>
                                <br>
                              </td>
                              <td>
                                <br>
                                <br>
                                <br>
                                <br>
                                <br>
                              </td>
                              <td>
                                <br>
                                <br>
                                <br>
                                <br>
                                <br>
                              </td>
                            </tr>
                            <tr>
                              <td>
                                <br>
                                <br>
                                <br>
                                <br>
                                <br>
                              </td>
                              <td>
                                <br>
                                <br>
                                <br>
                                <br>
                                <br>
                              </td>
                              <td>
                                <br>
                                <br>
                                <br>
                                <br>
                                <br>
                              </td>
                              <td>
                                <br>
                                <br>
                                <br>
                                <br>
                                <br>
                              </td>
                            </tr>
                            <tr>
                              <td>
                                <br>
                                <br>
                                <br>
                                <br>
                                <br>
                              </td>
                              <td>
                                <br>
                                <br>
                                <br>
                                <br>
                                <br>
                              </td>
                              <td>
                                <br>
                                <br>
                                <br>
                                <br>
                                <br>
                              </td>
                              <td>
                                <br>
                                <br>
                                <br>
                                <br>
                                <br>
                              </td>
                            </tr>
                            <tr>
                              <td>
                                <br>
                                <br>
                                <br>
                                <br>
                                <br>
                              </td>
                              <td>
                                <br>
                                <br>
                                <br>
                                <br>
                                <br>
                              </td>
                              <td>
                                <br>
                                <br>
                                <br>
                                <br>
                                <br>
                              </td>
                              <td>
                                <br>
                                <br>
                                <br>
                                <br>
                                <br>
                              </td>
                            </tr>
                            <tr>
                              <td>
                                <br>
                                <br>
                                <br>
                                <br>
                                <br>
                              </td>
                              <td>
                                <br>
                                <br>
                                <br>
                                <br>
                                <br>
                              </td>
                              <td>
                                <br>
                                <br>
                                <br>
                                <br>
                                <br>
                              </td>
                              <td>
                                <br>
                                <br>
                                <br>
                                <br>
                                <br>
                              </td>
                            </tr>
                          </tbody>
                        </table>
                        
                        <br>
                        
                        <!-- Légende -->
                        <div class="card text-center">
                          <div class="card-header">
                            Légende
                          </div>
                          <div class="card-body">
                            <h6>
                                - N = Neuf
                                <br>
                                - BE = Bon état
                                <br>
                                - EU = État d'usage
                                <br>
                                - ME = Mauvais état
                            </h6>
                          </div>
                        </div>
                        <!-- Légende -->
                        
                        <br>
                        
                        <h6>
                            Les matériels ont-ils été essayé par les contractants lors de la récupération des 
                            matériels ? ...
                        </h6>
                      </div>
                    </div>
                    <!-- Inventaire des matériels mis à disposition -->

                    <br>                

                    <!-- Signatures et cachets des cocontractants  -->
                    <div class="card text-center">
                      <div class="card-header">
                        Signatures et cachets des contractants
                      </div>
                      <div class="card-body">
                        <!-- Lieu et date des signatures et cachets des cocontractants (Code civil) -->
                        <div class="card text-center">
                          <div class="card-header">
                            Lieu et date des signatures et cachets des contractants
                          </div>
                          <div class="card-body">
                            En date du ... situé au ..., le présent état des lieux pour prêt de matériels a été signé 
                            et tamponné par l'emprunteur et le prêteur.
                          </div>
                        </div>
                        <!-- Lieu et date des signatures et cachets des cocontractants (Code civil) -->

                        <br>

                        <!-- Nombre d'exemplaires (Code civil) -->
                        <div class="card text-center">
                          <div class="card-header">
                            Nombre d'exemplaires du présent état des lieux pour prêt de matériels
                          </div>
                          <div class="card-body">
                            Le présent état des lieux pour prêt de matériels est fait en deux exemplaires 
                            dont l'un pour l'emprunteur et l'autre pour le prêteur.
                          </div>
                        </div>
                        <!-- Nombre d'exemplaires (Code civil) -->

                        <br>

                        <!-- Approbation (Code civil) -->
                        <div class="card text-center">
                          <div class="card-header">
                            Approbation du présent état des lieux pour prêt de matériels
                          </div>
                          <div class="card-body">
                            Le présent état des lieux pour prêt de matériels a été lu et approuvé 
                            par l'emprunteur et le prêteur.
                          </div>
                        </div>
                        <!-- Approbation (Code civil) -->

                        <br>

                        <!-- Signature et cachet de l'emprunteur -->
                        <div class="card text-center">
                          <div class="card-header">
                            Signature et cachet de l'emprunteur
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
                        <!-- Signature et cachet de l'emprunteur -->

                        <br>

                        <!-- Signature et cachet du prêteur -->
                        <div class="card text-center">
                          <div class="card-header">
                            Signature et cachet du prêteur
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
                        <!-- Signature et cachet du prêteur -->

                      </div>
                    </div>
                    <!-- Signatures et cachets des cocontractants  -->

                  </div>
                </div>
                <!-- Etat des lieux pour prêt de matériels -->

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
            'header-center': "État des lieux pour prêt de matériels",
            'footer-right': '[page] sur [topage]',
            'footer-left': 'Société Holomorphe [SIREN : 883632556]'
        }

        path_wkthmltopdf = "C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe"

        config = pdfkit.configuration(
            wkhtmltopdf=path_wkthmltopdf
        )

        pdfkit.from_string(
            body,
            "Mise_A_Disposition\\Etat_Lieux_Pret_Materiels.pdf",
            configuration=config,
            options=options
        )

        """
        <!--
        <!--  -->
        <div class="card text-center">
          <div class="card-header">

          </div>
          <div class="card-body">

          </div>
        </div>
        <!--  -->
        -->
        """

    # ok
    def test_etat_lieux_retour_materiels(self):
        print("test_etat_lieux_retour_materiels")

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

            <title>Etat des lieux pour retour de matériels</title>
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
                                <th scope="col">E-mail professionnel</th>
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
                <!-- Contact -->

                <br>

                <!-- Etat des lieux pour retour de matériels  -->
                <div class="card text-center">
                  <div class="card-header">
                    État des lieux pour retour de matériels
                  </div>
                  <div class="card-body">
                    <!-- Contractants -->
                    <div class="card text-center">
                      <div class="card-header">
                        Contractants
                      </div>
                      <div class="card-body">
                        <!-- Emprunteur -->
                        <div class="card text-center">
                          <div class="card-header">
                            Emprunteur
                          </div>
                          <div class="card-body">
                            L'emprunteur est une personne morale désignée par les informations suivantes :
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
                          </div>
                        </div>
                        <!-- Emprunteur -->

                        <br>

                        <!-- Prêteur -->
                        <div class="card text-center">
                          <div class="card-header">
                            Prêteur
                          </div>
                          <div class="card-body">
                            Le prêteur est une personne morale désignée par les informations suivantes :
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
                            - Numéro de téléphone : 00.33.7.49.16.33.29
                          </div>
                        </div>
                        <!-- Prêteur -->
                      </div>
                    </div>
                    <!-- Contractants -->

                    <br>

                    <!-- Inventaire des matériels mis à disposition -->
                    <div class="card text-center">
                      <div class="card-header">
                        Inventaire des matériels mis à disposition
                      </div>
                      <div class="card-body">
                        <table class="table table-bordered">
                          <thead>
                            <tr>
                              <th scope="col">Désignations</th>
                              <th scope="col">Quantité</th>
                              <th scope="col">État général du matériel</th>
                              <th scope="col">Remarques</th>
                            </tr>
                          </thead>
                          <tbody>
                            <tr>
                              <td>
                                <br>
                                <br>
                                <br>
                                <br>
                                <br>
                              </td>
                              <td>
                                <br>
                                <br>
                                <br>
                                <br>
                                <br>
                              </td>
                              <td>
                                <br>
                                <br>
                                <br>
                                <br>
                                <br>
                              </td>
                              <td>
                                <br>
                                <br>
                                <br>
                                <br>
                                <br>
                              </td>
                            </tr>
                            <tr>
                              <td>
                                <br>
                                <br>
                                <br>
                                <br>
                                <br>
                              </td>
                              <td>
                                <br>
                                <br>
                                <br>
                                <br>
                                <br>
                              </td>
                              <td>
                                <br>
                                <br>
                                <br>
                                <br>
                                <br>
                              </td>
                              <td>
                                <br>
                                <br>
                                <br>
                                <br>
                                <br>
                              </td>
                            </tr>
                            <tr>
                              <td>
                                <br>
                                <br>
                                <br>
                                <br>
                                <br>
                              </td>
                              <td>
                                <br>
                                <br>
                                <br>
                                <br>
                                <br>
                              </td>
                              <td>
                                <br>
                                <br>
                                <br>
                                <br>
                                <br>
                              </td>
                              <td>
                                <br>
                                <br>
                                <br>
                                <br>
                                <br>
                              </td>
                            </tr>
                            <tr>
                              <td>
                                <br>
                                <br>
                                <br>
                                <br>
                                <br>
                              </td>
                              <td>
                                <br>
                                <br>
                                <br>
                                <br>
                                <br>
                              </td>
                              <td>
                                <br>
                                <br>
                                <br>
                                <br>
                                <br>
                              </td>
                              <td>
                                <br>
                                <br>
                                <br>
                                <br>
                                <br>
                              </td>
                            </tr>
                            <tr>
                              <td>
                                <br>
                                <br>
                                <br>
                                <br>
                                <br>
                              </td>
                              <td>
                                <br>
                                <br>
                                <br>
                                <br>
                                <br>
                              </td>
                              <td>
                                <br>
                                <br>
                                <br>
                                <br>
                                <br>
                              </td>
                              <td>
                                <br>
                                <br>
                                <br>
                                <br>
                                <br>
                              </td>
                            </tr>
                          </tbody>
                        </table>

                        <br>

                        <!-- Légende -->
                        <div class="card text-center">
                          <div class="card-header">
                            Légende
                          </div>
                          <div class="card-body">
                            <h6>
                                - N = Neuf
                                <br>
                                - BE = Bon état
                                <br>
                                - EU = État d'usage
                                <br>
                                - ME = Mauvais état
                            </h6>
                          </div>
                        </div>
                        <!-- Légende -->

                        <br>

                        <h6>
                            Les matériels ont-ils été essayé par les contractants lors de la récupération des 
                            matériels ? ......
                        </h6>
                      </div>
                    </div>
                    <!-- Inventaire des matériels mis à disposition -->

                    <br>                

                    <!-- Signatures et cachets des cocontractants  -->
                    <div class="card text-center">
                      <div class="card-header">
                        Signatures et cachets des contractants
                      </div>
                      <div class="card-body">
                        <!-- Lieu et date des signatures et cachets des cocontractants (Code civil) -->
                        <div class="card text-center">
                          <div class="card-header">
                            Lieu et date des signatures et cachets des contractants
                          </div>
                          <div class="card-body">
                            En date du ... situé au ..., le présent état des lieux pour retour de matériels a été signé 
                            et tamponné par l'emprunteur et le prêteur.
                          </div>
                        </div>
                        <!-- Lieu et date des signatures et cachets des cocontractants (Code civil) -->

                        <br>

                        <!-- Nombre d'exemplaires (Code civil) -->
                        <div class="card text-center">
                          <div class="card-header">
                            Nombre d'exemplaires du présent état des lieux pour retour de matériels
                          </div>
                          <div class="card-body">
                            Le présent état des lieux pour retour de matériels est fait en deux exemplaires 
                            dont l'un pour l'emprunteur et l'autre pour le prêteur.
                          </div>
                        </div>
                        <!-- Nombre d'exemplaires (Code civil) -->

                        <br>

                        <!-- Approbation (Code civil) -->
                        <div class="card text-center">
                          <div class="card-header">
                            Approbation du présent état des lieux pour retour de matériels
                          </div>
                          <div class="card-body">
                            Le présent état des lieux pour retour de matériels a été lu et approuvé 
                            par l'emprunteur et le prêteur.
                          </div>
                        </div>
                        <!-- Approbation (Code civil) -->

                        <br>

                        <!-- Signature et cachet de l'emprunteur -->
                        <div class="card text-center">
                          <div class="card-header">
                            Signature et cachet de l'emprunteur
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
                        <!-- Signature et cachet de l'emprunteur -->

                        <br>

                        <!-- Signature et cachet du prêteur -->
                        <div class="card text-center">
                          <div class="card-header">
                            Signature et cachet du prêteur
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
                        <!-- Signature et cachet du prêteur -->

                      </div>
                    </div>
                    <!-- Signatures et cachets des cocontractants  -->

                  </div>
                </div>
                <!-- Etat des lieux pour retour de matériels -->

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
            'header-center': "État des lieux pour retour de matériels",
            'footer-right': '[page] sur [topage]',
            'footer-left': 'Société Holomorphe [SIREN : 883632556]'
        }

        path_wkthmltopdf = "C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe"

        config = pdfkit.configuration(
            wkhtmltopdf=path_wkthmltopdf
        )

        pdfkit.from_string(
            body,
            "Mise_A_Disposition\\Etat_Lieux_Retour_Materiels.pdf",
            configuration=config,
            options=options
        )

        """
        <!--
        <!--  -->
        <div class="card text-center">
          <div class="card-header">

          </div>
          <div class="card-body">

          </div>
        </div>
        <!--  -->
        -->
        """


if __name__ == '__main__':
    unittest.main()
