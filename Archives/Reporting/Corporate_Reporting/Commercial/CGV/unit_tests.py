import unittest
import pdfkit


class CGV(unittest.TestCase):
    # ok
    def test_cgv(self):
        print("test_cgv")

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

            <title>Conditions générales de ventes de contenu numérique non fourni sur un support matériel</title>
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

                <!-- Conditions générales de vente de contenu numérique non fourni sur un support matériel -->
                <div class="card text-center">
                  <div class="card-header">
                    Conditions générales de vente de contenu numérique non fourni sur un support matériel
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
                        <!-- Client -->
                        <div class="card text-center">
                          <div class="card-header">
                            Client
                          </div>
                          <div class="card-body">
                            Dans les présentes conditions générales de vente de contenu numérique non fourni sur un 
                            support matériel, le client est une personne morale agissant pour son activité principale 
                            et ayant un effectif salarial supérieur à six salariés, et désignée par les informations 
                            suivantes :
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
                            - Numéro TVA intracommunataire : ...
                            <br>
                            - Président : ...
                            <br>
                            - Date d'immatriculation : ...
                            <br>
                            - Numéro de téléphone : ...
                            <br>
                            <br>
                            Conformément aux articles 1145 à 1161 du code civil, le client est représenté par ... 
                            pour les présentes conditions générales de vente de contenu numérique non fourni sur un 
                            support matériel.
                            <br>
                            <br>
                            Conformément aux articles L123-1 à L123-11-8 du code de commerce, le client 
                            devra joindre une copie de son extrait Kbis datant de moins de trois mois par rapport à la 
                            date de signature des présentes conditions générales de vente de contenu numérique non 
                            fourni sur un support matériel et une copie d'une pièce d'identité de son représentant 
                            légal mentionné dans son extrait Kbis aux présentes conditions générales de vente de 
                            contenu numérique non fourni sur un support matériel afin de prouver son immatriculation 
                            auprès du registre de commerce et des sociétés.
                          </div>
                        </div>
                        <!-- Client -->

                        <br>

                        <!-- Vendeur -->
                        <div class="card text-center">
                          <div class="card-header">
                            Vendeur
                          </div>
                          <div class="card-body">
                            Dans les présentes conditions générales de vente de contenu numérique non fourni sur un 
                            support matériel, le vendeur est une personne morale désignée par les informations 
                            suivantes :
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
                            Conformément aux articles 1145 à 1161 du code civil, le vendeur est représenté par Monsieur 
                             pour les présentes conditions générales de vente de contenu numérique non 
                            fourni sur un support matériel.
                            <br>
                            <br>
                            Conformément aux articles L123-1 à L123-11-8 du code de commerce, le vendeur 
                            devra joindre une copie de son extrait Kbis datant de moins de trois mois par rapport à la 
                            date de signature des présentes conditions générales de vente de contenu numérique non 
                            fourni sur un support matériel et une copie d'une pièce d'identité de son représentant 
                            légal mentionné dans son extrait Kbis aux présentes conditions générales de vente de 
                            contenu numérique non fourni sur un support matériel afin de prouver son immatriculation 
                            auprès du registre de commerce et des sociétés.
                          </div>
                        </div>
                        <!-- Vendeur -->
                      </div>
                    </div>
                    <!-- Contractants -->

                    <br>

                    <h6>
                        Dans les présentes conditions générales de ventes de contenu numérique non fourni sur un 
                        support matériel, il a été convenu ce qui suit:
                    </h6>

                    <br>

                    <!-- Articles -->
                    <div class="card text-center">
                      <div class="card-header">
                        Articles
                      </div>
                      <div class="card-body">
                        <!-- Article 1 : Objet et champ d'application (Code de commerce) -->
                        <div class="card text-center">
                          <div class="card-header">
                            Article 1 : Objet et champ d'application
                          </div>
                          <div class="card-body">
                            Vu les articles L441-1 à L441-19 du code de commerce concernant la transparence dans la 
                            relation commerciale,
                            <br>
                            Vu les articles L111-1 à L141-2 du code de la consommation concernant l'information des 
                            consommateurs et pratiques commerciales, 
                            <br>
                            <br>
                            Conformément à l'article L441-1 du code de commerce et à l'article L111-1 du code de la 
                            consommation, les présentes conditions générales de vente de contenu numérique non fourni 
                            sur un support matériel constituent le socle de la négociation commerciale et sont 
                            systématiquement adressées ou remises au client pour lui permettre de passer commande.
                            <br>
                            <br>
                            Les conditions générales de vente décrites ci-après détaillent les droits et obligations 
                            du vendeur et de son client dans le cadre de la vente de contenu numérique non fourni 
                            sur un support matériel.
                            <br>
                            <br>
                            Toute acceptation du devis/bon de commande en ce compris la clause "Je reconnais avoir 
                            pris connaissance et j'accepte les conditions générales de vente ci-annexées" implique 
                            l'adhésion sans réserve du client aux présentes conditions générales de vente de contenu 
                            numérique non fourni sur un support matériel.
                          </div>
                        </div>
                        <!-- Article 1 : Objet et champ d'application (Code de commerce) -->

                        <br>

                        <!-- Article 2 : Prix (Code de commerce) -->
                        <div class="card text-center">
                          <div class="card-header">
                            Article 2 : Prix
                          </div>
                          <div class="card-body">
                            Vu le code de la consommation,
                            <br>
                            Vu le code général des impôts,
                            <br>
                            Vu les articles  du code de commerce concernant ,
                            <br>
                            <br>
                            Les prix des contenus numériques non fournis sur un support matériel vendus sont ceux en 
                            vigueur au jour de la prise de commande. 
                            <br>
                            <br>
                            Les prix des contenus numériques non fournis sur un support matériel vendus sont libellés 
                            en euros et calculés hors taxes. 
                            <br>
                            <br>
                            Par voie de conséquence, les prix des contenus numériques non fournis sur un support 
                            matériel vendus seront majorés du taux de TVA applicable au jour de la commande.
                            <br>
                            <br>
                            Le vendeur s'accorde le droit de modifier ses tarifs à tout moment. 
                            <br>
                            <br>
                            Toutefois, le vendeur s'engage à facturer les contenus numériques non fournis sur un support 
                            matériel commandées aux prix indiqués lors de l'enregistrement de la commande.
                          </div>
                        </div>
                        <!-- Article 2 : Prix (Code de commerce) -->

                        <br>
                        
                        <!-- Article 3 : Garantie (Code de la consommation / Code de commerce) -->
                        <div class="card text-center">
                          <div class="card-header">
                            Article 3 : Garantie
                          </div>
                          <div class="card-body">
                            Vu le code de commerce,
                            <br>
                            Vu le code de la consommation,
                            <br>
                            Vu le code civil,
                            <br>
                            <br>
                            Toute fourniture de contenu numérique non fourni sur un support matériel au client par le 
                            vendeur des présentes conditions générales de vente de contenu numérique non fourni sur un 
                            support matériel ne fera l'objet d'aucune garantie que ce soit.
                            <br>
                            <br>
                            Le vendeur ne vend en aucun cas que ce soit des contenus numériques non fournis sur un 
                            support matériel à caractère personnel, pornographique, violent, racial, dégradant, sexuel, 
                            raciste et illicite.
                          </div>
                        </div>
                        <!-- Article 3 : Garantie (Code de la consommation / Code de commerce) -->

                        <br>
                        
                        <!-- Article 4 : Rabais et ristournes (Code de commerce) -->
                        <div class="card text-center">
                          <div class="card-header">
                            Article 4 : Rabais et ristournes
                          </div>
                          <div class="card-body">
                            Vu le code de la consommation,
                            <br>
                            Vu le code de commerce,
                            <br>
                            Vu le code général des impôts,
                            <br>
                            <br>
                            Les tarifs proposés au client par le vendeur des présentes conditions générales de vente 
                            de contenu numérique non fourni sur un support matériel comprennent les rabais et 
                            ristournes que le vendeur serait amené à octroyer compte tenu de ses résultats ou de 
                            la prise en charge par le client de certains contenus numériques non fournis sur un support 
                            matériel.
                          </div>
                        </div>
                        <!-- Article 4 : Rabais et ristournes (Code de commerce) -->

                        <br>
                        
                        <!-- Article 5 : Escompte (Code de commerce) -->
                        <div class="card text-center">
                          <div class="card-header">
                            Article 5 : Escompte
                          </div>
                          <div class="card-body">
                            Vu le code de la consommation,
                            <br>
                            Vu le code de commerce,
                            <br>
                            Vu le code général des impôts,
                            <br>
                            <br>
                            Tout paiement anticipé de toute facture émise au client par le vendeur des présentes 
                            conditions générales de vente de contenu numérique non fourni sur un support matériel ne 
                            fera l'objet d'escompte.
                          </div>
                        </div>
                        <!-- Article 5 : Escompte (Code de commerce) -->

                        <br>
                        
                        <!-- Article 6 : Rétractation (Code de la consommation / Code de commerce) -->
                        <div class="card text-center">
                          <div class="card-header">
                            Article 6 : Rétractation
                          </div>
                          <div class="card-body">
                            Vu les articles L221-18 à L221-28 du code de la consommation concernant le droit de 
                            rétractation applicable aux contrats conclus à distance et hors établissement,
                            <br>
                            Vu le code de commerce,
                            <br>
                            <br>
                            Conformément à l'alinéa 13 de l'article L221-28 du code de la consommation, stipulant que 
                            le droit de rétractation ne peut être exercée pour les contrats de fourniture d'un contenu 
                            numérique non fourni sur un support matériel dont l'exécution a commencé après accord 
                            préalable exprès du consommateur et renoncement exprès à son droit de rétractation, le 
                            client ne peut se prévaloir le droit de rétractation de la fourniture d'un contenu 
                            numérique non fourni sur un support matériel par le vendeur dont l'exécution des présentes 
                            conditions générales de vente de contenu numérique non fourni sur un support matériel a 
                            commencé après accord préalable exprès du client et renoncement exprès à son droit de 
                            rétractation.
                          </div>
                        </div>
                        <!-- Article 6 : Rétractation (Code de la consommation / Code de commerce) -->

                        <br>
                        
                        <!-- Article 7 : Facturation et délai de paiement (Code de commerce) -->
                        <div class="card text-center">
                          <div class="card-header">
                            Article 7 : Facturation et délai de paiement
                          </div>
                          <div class="card-body">
                            Vu les articles L123-12 à L123-24 du code de commerce concernant les obligations comptables 
                            applicables à tous les commerçants,
                            <br>
                            Vu les articles L441-1 à L441-2 du code de commerce concernant les conditions générales 
                            de vente,
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
                            Conformément à l'article L441-9 du code de commerce, le vendeur émettra une facture 
                            au client lors de la date de signature des présentes conditions générales de vente de 
                            contenu numérique non fourni sur un support matériel. La facture émise au client par le 
                            vendeur des présentes conditions générales de vente de contenu numérique non fourni sur 
                            un support matériel sera émise par voie électronique au moyen d'une signature 
                            électronique. En cas d'erreur, une facture émise au client par le vendeur des présentes 
                            conditions générales de vente de contenu numérique non fourni sur un support matériel peut 
                            être annulée ou rectifiée.
                            <br>
                            <br>
                            Conformément à l'article L441-10 du code de commerce, le délai de paiement convenu entre les 
                            contractants des présentes conditions générales de vente de contenu numérique non fourni sur 
                            un support matériel pour régler les sommes dues ne peut dépasser trente jours 
                            après la date d'émission de la facture émise au client par le vendeur des présentes 
                            conditions générales de vente de contenu numérique non fourni sur un support matériel.
                            <br>
                            <br>
                            Conformément à l'article L123-22 du code de commerce et à l'article L102 B du livre des 
                            procédures fiscales, la facture émise au client par le vendeur des présentes conditions 
                            générales de vente de contenu numérique non fourni sur un support matériel sera 
                            établie en euros et en langue française, et devra être conservée pendant dix ans par les 
                            contractants.
                            <br>
                            <br>
                            Conformément à l'article 289 du code général des impôts et à l'article 242 nonies A de 
                            l'annexe 2 du code général des impôts, la facture émise au client par le vendeur des 
                            présentes conditions générales de vente de contenu numérique non fourni sur un support 
                            matériel comportera un certain nombre de mentions obligatoires qui sont les suivantes :
                            <br>
                            - La date de l'émission de la facture qui est la date à laquelle elle est émise.
                            <br>
                            - La numérotation de la facture qui est le numéro unique basé sur une séquence 
                            chronologique continue et sans rupture.
                            <br>
                            - La date de la vente de contenu numérique non fourni sur un support matériel qui est le 
                            jour effectif de la fin d'exécution de la vente de contenu numérique non fourni sur un 
                            support matériel.
                            <br>
                            - L'identité du client qui comporte la dénomination sociale du client, 
                            l'adresse du siège social du client et l'adresse de facturation si différente du 
                            siège social.
                            <br>
                            - L'identité du vendeur qui comporte la dénomination sociale du vendeur suivie du numéro 
                            siren, l'adresse du siège social du vendeur, la forme juridique et le montant du capital 
                            social du vendeur.
                            <br>
                            - Le numéro individuel d'identification à la TVA du vendeur et du client.
                            <br>
                            - La désignation de la prestation qui comporte la prestation fournie.
                            <br>
                            - Le décompte détaillé de chaque prestation qui comporte le détail en quantité et prix.
                            <br>
                            - Le prix catalogue qui comporte le prix unitaire hors TVA de la prestation fournie.
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
                            - Les taux des pénalités de retard qui sont exigibles en cas de non-paiement à la date de 
                            règlement.
                            <br>
                            - La mention suivante : "Les pénalités de retard sont exigibles sans qu'un rappel soit 
                            nécessaire.".
                            <br>
                            - La mention de l'indemnité forfaitaire de quarante euros pour frais de recouvrement, 
                            en cas de retard de paiement.
                            <br>
                            - La mention suivante : "Le paiement sera effectué en une seule fois par virement bancaire 
                            aux coordonnées bancaires du vendeur."
                            <br>
                            - Les coordonnées bancaires du vendeur.
                          </div>
                        </div>
                        <!-- Article 7 : Facturation et délai de paiement (Code de commerce) -->

                        <br>
                        
                        <!-- Article 8 : Modalités de paiement (Code de commerce) -->
                        <div class="card text-center">
                          <div class="card-header">
                            Article 8 : Modalités de paiement
                          </div>
                          <div class="card-body">
                            Vu le code de commerce,
                            <br>
                            Vu le code civil,
                            <br>
                            <br>
                            Le réglement de toute facture émise au client par le vendeur des présentes conditions 
                            générales de vente de contenu numérique non fourni sur un support matériel s'effectue par 
                            virement bancaire au compte bancaire du vendeur mentionné sur la facture accompagnée du 
                            relevé d'identité bancaire du compte bancaire du vendeur.
                          </div>
                        </div>
                        <!-- Article 8 : Modalités de paiement (Code de commerce) -->

                        <br>
                        
                        <!-- Article 9 : Pénalités pour retard de paiement (Code de commerce) -->
                        <div class="card text-center">
                          <div class="card-header">
                            Article 9 : Pénalités pour retard de paiement
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
                            facture émise au client par le vendeur des présentes conditions générales de vente de 
                            contenu numérique non fourni sur un support matériel fera l'objet de pénalités de retard 
                            de paiement exigibles le jour suivant la date de règlement figurant sur toute facture émise 
                            au client par le vendeur des présentes conditions générales de vente de contenu numérique 
                            non fourni sur un support matériel ainsi que le montant de l'indemnité forfaitaire pour 
                            frais de recouvrement due au vendeur dans le cas où les sommes dues sont réglées après 
                            cette date. Les pénalités de retard de paiement de toute facture émise au client par le 
                            vendeur des présentes conditions générales de vente de contenu numérique non fourni sur 
                            un support matériel sont exigibles sans qu'un rappel soit nécessaire. Le client en 
                            situation de retard de paiement est de plein droit débiteur, à l'égard du vendeur, d'une 
                            indemnité forfaitaire pour frais de recouvrement, dont le montant est fixé par décret. 
                            Lorsque les frais de recouvrement exposés sont supérieurs au montant de cette indemnité 
                            forfaitaire, le vendeur peut demander une indemnisation complémentaire, sur justification.
                            <br>
                            <br>
                            Le taux de l'intérêt légal sera fixé à vingt pour cent (20%) pour tout calcul des 
                            pénalités de retard de paiement de toute facture émise au client par le vendeur des 
                            présentes conditions générales de vente de contenu numérique non fourni sur un support 
                            matériel.
                            <br>
                            <br>
                            La formule de calcul des pénalités de retard de paiement de toute facture émise au client 
                            par le vendeur des présentes conditions générales de vente de contenu numérique non fourni 
                            sur un support matériel est la suivante : [(taux d'intérêt légal fixé par les présentes 
                            conditions générales de vente de contenu numérique non fourni sur un support matériel) x 
                            (montant TTC de toute facture émise au client par le vendeur des présentes conditions 
                            générales de vente de contenu numérique non fourni sur un support matériel)] x [(nombre de 
                            jours de retard de paiement de toute facture émise au client par le vendeur des présentes 
                            conditions générales de vente de contenu numérique non fourni sur un support matériel)/365].
                            <br>
                            <br>
                            Le point de départ des pénalités de retard de paiement de toute facture émise au client 
                            par le vendeur des présentes conditions générales de vente de contenu numérique non fourni 
                            sur un support matériel est le lendemain de l'échéance de toute facture émise au client 
                            par le vendeur des présentes conditions générales de vente de contenu numérique non fourni 
                            sur un support matériel. Le point d'arrivée du calcul des pénalités de retard 
                            de paiement de toute facture émise au client par le vendeur des présentes conditions 
                            générales de vente de contenu numérique non fourni sur un support matériel est constitué 
                            par la date d'envoi du règlement de toute facture émise au client par le vendeur des 
                            présentes conditions générales de vente de contenu numérique non fourni sur un support 
                            matériel.
                          </div>
                        </div>
                        <!-- Article 9 : Pénalités pour retard de paiement (Code de commerce) -->

                        <br>
                        
                        <!-- Article 10 : Livraison (Code de commerce) -->
                        <div class="card text-center">
                          <div class="card-header">
                            Article 10 : Livraison
                          </div>
                          <div class="card-body">
                            Vu le code de commerce,
                            <br>
                            Vu le code de la consommation,
                            <br>
                            Vu le code civil,
                            <br>
                            Vu le code des postes et des communications électroniques,
                            <br>
                            <br>
                            Conformément à l'alinéa 1 de l'article L32 du code des postes et des communications 
                            électroniques, la fourniture ou la livraison d'un contenu numérique non fourni sur un 
                            support matériel au client par le vendeur des présentes conditions de vente de contenu 
                            numérique non fourni sur un support matériel est effectuée par voie électronique.
                            <br>
                            <br>
                            Le délai de livraison indiqué lors de l'enregistrement de la commande n'est donné qu'à 
                            titre indicatif et n'est aucunement garanti.
                            <br>
                            <br>
                            Par voie de conséquence, tout retard raisonnable dans la livraison des contenus numériques 
                            non fournis sur un support matériel au client par le vendeur des présentes conditions de 
                            vente de contenu numérique non fourni sur un support matériel ne pourra pas donner lieu 
                            au profit du client à :
                            <br>
                            - l'allocation de dommages et intérêts ;
                            <br>
                            - l'annulation de la commande.
                            <br>
                            <br>
                            En cas de contenus numériques non fournis sur un support matériel manquants ou détériorés 
                            lors de la livraison, le client devra formuler toutes les réserves nécessaires sur le bon 
                            de commande à réception desdits contenus numériques non fournis sur un support matériel. 
                            Ces réserves devront être, en outre, confirmées par écrit dans les cinq jours suivant la 
                            livraison, par courrier recommandé avec accusé de réception ou par courrier électronique 
                            adressé au vendeur.
                          </div>
                        </div>
                        <!-- Article 10 : Livraison (Code de commerce) -->

                        <br>
                        
                        <!-- Article 11 : Clause résolutoire (Code de commerce / Code civil) -->
                        <div class="card text-center">
                          <div class="card-header">
                            Article 11 : Clause résolutoire
                          </div>
                          <div class="card-body">
                            Vu les articles 1224 à 1230 du code civil concernant la résolution,
                            <br>
                            <br>
                            Conformément à l'article 1224 du code civil, si dans les quinze jours qui suivent la 
                            mise en oeuvre de la clause "Pénalités pour retard de paiement", le client ne s'est pas 
                            acquitté des sommes restant dues, la vente sera résolue de plein droit et pourra ouvrir 
                            droit à l'allocation de dommages et intérêts au profit du vendeur.
                          </div>
                        </div>
                        <!-- Article 11 : Clause résolutoire (Code de commerce / Code civil) -->

                        <br>
                        
                        <!-- Article 12 : Protection du secret des affaires / Confidentialité (Code de commerce) -->
                        <div class="card text-center">
                          <div class="card-header">
                            Article 12 : Protection du secret des affaires / Confidentialité
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
                            les contenus numériques non fournis sur un support matériel vendus au client par le 
                            vendeur des présentes conditions générales de vente de contenu numérique non fourni sur 
                            un support matériel sont protégés au titre du secret des affaires.
                            <br>
                            <br>
                            Conformément aux articles L151-2 à L151-3 du code de commerce concernant la détention 
                            légitime et l'obtention licite d'un secret des affaires, le vendeur est l'unique détenteur 
                            légitime du secret des affaires des contenus numériques non fournis sur un support matériel 
                            vendus au client par le vendeur des présentes conditions générales de vente de contenu 
                            numérique non fourni sur un support matériel.
                            <br>
                            <br>
                            Conformément aux articles L151-4 à L151-6 du code de commerce concernant l'obtention 
                            illicite, l'utilisation illicite et la divulgation illicite du secret des affaires, 
                            le client ne peut se prévaloir le droit d'obtenir, d'utiliser et de divulguer 
                            tout secret des affaires des contenus numériques non fournis sur un support matériel 
                            vendus au client par le vendeur des présentes conditions générales de vente de contenu 
                            numérique non fourni sur un support matériel.
                            <br>
                            <br>
                            Conformément aux articles L152-1 à L152-8, L153-1 à L153-2, R152-1, R153-1 à R153-10 du 
                            code de commerce concernant les actions en prévention, en cessation ou en réparation 
                            d'une atteinte au secret des affaires et les mesures générales de protection du 
                            secret des affaires devant les juridictions civiles ou commerciales, le vendeur peut 
                            exercer des actions en justice contre le client ou des tiers pour atteinte au secret 
                            des affaires des contenus numériques non fournis sur un support matériel 
                            vendus au client par le vendeur des présentes conditions générales de vente de contenu 
                            numérique non fourni sur un support matériel.
                          </div>
                        </div>
                        <!-- Article 12 : Protection du secret des affaires / Confidentialité (Code de commerce) -->

                        <br>
                        
                        <!-- Article 13 : Pratiques anticoncurrentielles / Pratiques prohibées -->
                        <div class="card text-center">
                          <div class="card-header">
                            Article 13 : Pratiques anticoncurrentielles / Pratiques prohibées
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
                            Le vendeur peut exercer des actions en dommages et intérêts contre le client du fait des 
                            pratiques anticoncurrentielles, déloyales et prohibées commises par le client envers le 
                            vendeur par rapport aux présentes conditions générales de vente de contenu numérique 
                            non fourni sur un support matériel. 
                          </div>
                        </div>
                        <!-- Article 13 : Pratiques anticoncurrentielles / Pratiques prohibées -->

                        <br>
                        
                        <!-- Article 14 : Clause de propriété intellectuelle (Code de la propriété intellectuelle) -->
                        <div class="card text-center">
                          <div class="card-header">
                            Article 14 : Clause de propriété intellectuelle
                          </div>
                          <div class="card-body">
                            Vu les articles L341-1 à L343-7 du code de la propriété intellectuelle concernant les 
                            droits des producteurs de bases de données,
                            <br>
                            Vu l'article R341-1 du code de la propriété intellectuelle concernant les droits des 
                            producteurs de bases de données,
                            <br>
                            <br>
                            Conformément à l'article L341-1 du code de la propriété intellectuelle, le vendeur est 
                            pleinement le producteur de la base de données des contenus numériques non fournis sur un 
                            support matériel mis en vente auprès de son client par rapport aux présentes conditions 
                            générales de vente de contenu numérique non fourni sur un support matériel.
                            <br>
                            <br>
                            Conformément à l'article L342-1 du code de la propriété intellectuelle, lorsque le paiement 
                            de la facture émise au client par le vendeur des présentes conditions générales de vente 
                            de contenu numérique non fourni sur un support matériel est effectué, le vendeur transmet 
                            au client les contenus numériques vendus et non fournis sur un support matériel par voie 
                            électronique et autorise au client la réutilisation des contenus numériques non fournis sur 
                            un support matériel à des fins privées et commerciales que ce soit.
                          </div>
                        </div>
                        <!-- Article 14 : Clause de propriété intellectuelle (Code de la propriété intellectuelle) -->

                        <br>
                        
                        <!-- Article 15 : Clause de réserve de propriété (Code civil / Code de commerce) -->
                        <div class="card text-center">
                          <div class="card-header">
                            Article 15 : Clause de réserve de propriété
                          </div>
                          <div class="card-body">
                            Vu le code de commerce,
                            <br>
                            Vu le code civil,
                            <br>
                            Vu le code de la propriété intellectuelle,
                            <br>
                            <br>
                            Le client peut se prévaloir le droit de la propriété des contenus numériques vendus et 
                            non fournis sur un support matériel jusqu'au paiement intégral de la facture lui étant 
                            émise par le vendeur par rapport aux présentes conditions générales de vente de contenu 
                            numérique non fourni sur un support matériel.
                            <br>
                            <br>
                            Toutefois, le vendeur reste toujours propriétaire des contenus numériques vendus et 
                            non fournis sur un support matériel même après le paiement intégral par le client 
                            de la facture lui étant émise par le vendeur par rapport aux présentes conditions générales 
                            de vente de contenu numérique non fourni sur un support matériel.
                          </div>
                        </div>
                        <!-- Article 15 : Clause de réserve de propriété (Code civil / Code de commerce) -->

                        <br>
                        
                        <!-- Article 16 : Responsabilités (Code de la propriété intellectuelle) -->
                        <div class="card text-center">
                          <div class="card-header">
                            Article 16 : Responsabilités
                          </div>
                          <div class="card-body">
                            Vu le code civl,
                            <br>
                            Vu le code de commerce,
                            <br>
                            <br>
                            Tout usage que ce soit fait par le client des contenus numériques non fournis sur un 
                            support matériel au client par le vendeur des présentes conditions générales de vente de 
                            contenu numérique non fourni sur un support matériel est entièrement sous la responsabilité 
                            du client.
                            <br>
                            <br>
                            Le client ne peut se prévaloir le droit d'engager la responsabilité du vendeur des contenus 
                            numériques non fournis sur un support matériel au client par le vendeur des présentes 
                            conditions générales de vente de contenu numérique non fourni sur un support matériel pour 
                            toute raison que ce soit.
                          </div>
                        </div>
                        <!-- Article 16 : Responsabilités (Code de la propriété intellectuelle) -->

                        <br>
                        
                        <!-- Article 17 : Force majeure (Code civil) -->
                        <div class="card text-center">
                          <div class="card-header">
                            Article 17 : Force majeure
                          </div>
                          <div class="card-body">
                            Vu les articles 1217 à 1231-7 du code civil concernant l'inexécution du contrat,
                            <br>
                            <br>
                            Conformément à l'article 1218 du code civil, la responsabilité du vendueur ne pourra pas 
                            être mise en oeuvre si la non-exécution ou le retard dans l'exécution de l'une de ses 
                            obligations décrites dans les présentes conditions générales de vente de contenu numérique 
                            non fourni sur un support matériel découle d'un cas de force majeure. À ce titre, la force 
                            majeure s'entend de tout événement extérieur, imprévisible et irrésistible au sens de 
                            l'article 1218 du code civil.
                          </div>
                        </div>
                        <!-- Article 17 : Force majeure (Code civil) -->

                        <br>
                        
                        <!-- Article 18 : Protection des données à caractère personnel (Loi informatiques et libertés 
                        / RGPD) -->
                        <div class="card text-center">
                          <div class="card-header">
                            Article 18 : Protection des données à caractère personnel
                          </div>
                          <div class="card-body">
                            Vu la loi n°78-17 du 6 janvier 1978 relative à l'informatique, aux fichiers et aux libertés,
                            <br>
                            Vu le règlement (UE) 2016/679 du Parlement européen et du Conseil du 27 avril 2016 relatif 
                            à la protection des personnes physiques à l'égard du traitement des données à caractère 
                            personnel et à la libre circulation de ces données, et abrogeant la directive 95/46/CE,
                            <br>
                            <br>
                            Conformément à l'article 2 de la loi n°78-17 du 6 janvier 1978 relative à l'informatique, 
                            aux fichiers et aux libertés, le vendeur ne traite pas des données à caractère 
                            personnel du client ou des tiers de quelque manière que ce soit.
                            <br>
                            <br>
                            Le client est entièrement responsable de tout traitements automatisés en tout ou partie de 
                            données à caractère personnel, ainsi qu'aux traitements non automatisés de données à 
                            caractère personnel contenues ou appelées à figurer dans des fichiers.
                            <br>
                            <br>
                            Le vendeur ne donne pas son consentement pour tout traitement de ses données à caractère 
                            personnel par le client ou des tiers.
                          </div>
                        </div>
                        <!-- Article 18 : Protection des données à caractère personnel (Loi informatiques et libertés 
                        / RGPD) -->

                        <br>

                        <!-- Article 19 : Clause d’acceptation expresse de l’acheteur aux conditions générales de 
                        vente (Code de commerce / Code civil) -->
                        <div class="card text-center">
                          <div class="card-header">
                            Article 19 : Clause d’acceptation expresse du client aux conditions générales de 
                            vente de contenu numérique non fourni sur un support matériel
                          </div>
                          <div class="card-body">
                            Vu le code de commerce,
                            <br>
                            Vu le code civil,
                            <br>
                            Vu le code de la consommation,
                            <br>
                            <br>
                            Le client statue d'avoir lu et approuvé les présentes conditions générales de vente de 
                            contenu numérique non fourni sur un support matériel, et accepte expressément les présentes 
                            conditions générales de vente de contenu numérique non fourni sur un support matériel.
                          </div>
                        </div>
                        <!-- Article 19 : Clause d’acceptation expresse de l’acheteur aux conditions générales de 
                        vente (Code de commerce / Code civil) -->

                        <br>
                        
                        <!-- Article 20 : Modification des présentes conditions générales de vente (Code civil) -->
                        <div class="card text-center">
                          <div class="card-header">
                            Article 20 : Modification des présentes conditions générales de vente de contenu numérique 
                            non fourni sur un support matériel
                          </div>
                          <div class="card-body">
                            Vu les articles 1100 à 1303-4 du code civil concernant les sources d'obligations,
                            <br>
                            <br>
                            Conformément aux articles 1101 à 1231-7 du code civil concernant le contrat, toute 
                            modification apportée aux présentes conditions générales de vente de contenu numérique 
                            non fourni sur un support matériel devra faire l'objet d'un avenant dûment signé par les 
                            contractants.
                          </div>
                        </div>
                        <!-- Article 20 : Modification des présentes conditions générales de vente (Code civil) -->

                        <br>
                        
                        <!-- Article 21 : Réglement des litiges (Code de commerce) -->
                        <div class="card text-center">
                          <div class="card-header">
                            Article 21 : Réglement des litiges
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
                            de l'interprétation des présentes conditions générales de vente de contenu numérique 
                            non fourni sur un support matériel. À défaut de solution amiable, le litige sera tranché 
                            par le tribunal de commerce de Paris.
                          </div>
                        </div>
                        <!-- Article 21 : Réglement des litiges (Code de commerce) -->
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
                        Conformément aux articles 1112 à 1187 et 1372 à 1377 du code civil, les présentes conditions 
                        générales de ventes de contenu numérique non fourni sur un support matériel ont été établies 
                        par acte sous signatures privées par les contractants.
                        <br>
                        <br>
                        <!-- Lieu et date des signatures et cachets des cocontractants (Code civil) -->
                        <div class="card text-center">
                          <div class="card-header">
                            Lieu et date des signatures et cachets des contractants
                          </div>
                          <div class="card-body">
                            En date du ... situé au ..., les présentes conditions générales de ventes de contenu 
                            numérique non fourni sur un support matériel ont été signées et tamponnées par l'emprunteur 
                            et le prêteur.
                          </div>
                        </div>
                        <!-- Lieu et date des signatures et cachets des cocontractants (Code civil) -->

                        <br>

                        <!-- Nombre d'exemplaires des présentes conditions générales de vente (Code civil) -->
                        <div class="card text-center">
                          <div class="card-header">
                            Nombre d'exemplaires des présentes conditions générales de vente
                          </div>
                          <div class="card-body">
                            Les présentes conditions générales de vente de contenu numérique non fourni sur un 
                            support matériel sont faites en deux exemplaires dont l'un pour le client et l'autre pour 
                            le vendeur.
                          </div>
                        </div>
                        <!-- Nombre d'exemplaires des présentes conditions générales de vente (Code civil) -->

                        <br>

                        <!-- Approbation des présentes conditions générales de vente -->
                        <div class="card text-center">
                          <div class="card-header">
                            Approbation des présentes conditions générales de vente
                          </div>
                          <div class="card-body">
                            Les présentes conditions générales de vente de contenu numérique non fourni sur un 
                            support matériel ont été lues et approuvées par le client et le vendeur.
                          </div>
                        </div>
                        <!-- Approbation des présentes conditions générales de vente -->

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

                        <br>

                        <!-- Signature et cachet du vendeur -->
                        <div class="card text-center">
                          <div class="card-header">
                            Signature et cachet du vendeur
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
                        <!-- Signature et cachet du vendeur -->

                      </div>
                    </div>
                    <!-- Signatures et cachets des cocontractants  -->

                  </div>
                </div>
                <!-- Conditions générales de vente de contenu numérique non fourni sur un support matériel -->

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
            'header-center': "Conditions générales de vente de contenu numérique non fourni sur un support matériel",
            'footer-right': '[page] sur [topage]',
            'footer-left': 'Société Holomorphe [SIREN : 883632556]'
        }

        path_wkthmltopdf = "C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe"

        config = pdfkit.configuration(
            wkhtmltopdf=path_wkthmltopdf
        )

        pdfkit.from_string(
            body,
            "CGV\\CGV_[Societe_Holomorphe].pdf",
            configuration=config,
            options=options
        )


if __name__ == '__main__':
    unittest.main()
