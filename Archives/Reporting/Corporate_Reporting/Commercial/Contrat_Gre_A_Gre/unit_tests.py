import unittest
import pdfkit


class Contrat_Gre_A_Gre(unittest.TestCase):
    def test_contrat_gre_a_gre(self):
        print("test_contrat_gre_a_gre")

        body = """
        <!doctype html>
        <html lang="en">
          <head>
            <!-- Required meta tags -->
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">

            <!-- Bootstrap CSS -->
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-BmbxuPwQa2lc/FVzBcNJ7UAyJxM6wuqIj61tLrc4wSX0szH/Ev+nYRRuWlolflfl" crossorigin="anonymous">

            <title>Contrat de vente de gré à gréd'un mélange gazeux de dihydrogène et de dioxygène</title>
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
                                <th scope="col">E-mail professionnel</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>Monsieur </td>
                                <td>31 Avenue de Ségur 75007 Paris</td>
                                <td></td>
                                <td>@holomorphe.com</td>
                            </tr>
                        </tbody>
                    </table>
                  </div>
                </div>

                <br>

                <div class="card text-center">
                  <div class="card-header">
                    Clauses
                  </div>
                  <div class="card-body">
                    <!-- Clause n°1 : Objet -->
                    <div class="card text-center">
                      <div class="card-header">
                          Clause n°1 : Objet
                      </div>
                      <div class="card-body">
                        Le contrat de vente de gré à gré d'un mélange gazeux de dihydrogène et de dioxygène par la 
                        société HOLOMORPHE à son client décrit ci-après détaille les droits et les obligations de 
                        la société HOLOMORPHE et de son client dans le cadre de la vente d'un mélange gazeux de 
                        dihydrogène et de dioxygène produit par électrolyse de l'eau par la société HOLOMORPHE à son 
                        client.
                        <br>
                        <br>
                        Toute vente d'un mélange gazeux de dihydrogène et de dioxygène accomplie par la société 
                        HOLOMORPHE à son client implique donc un commun accord sans réserve avec son client au présent
                        contrat de vente de gré à gré d'un mélange gazeux de dihydrogène et de dioxygène produit par 
                        électrolyse de l'eau par la société HOLOMORPHE à son client.
                      </div>
                    </div>

                    <br>

                    <!-- Clause n°2  : Prix -->
                    <div class="card text-center">
                      <div class="card-header">
                        Clause n°2 : Prix
                      </div>
                      <div class="card-body">
                        Le prix de vente du mélange gazeux de dihydrogène et de dioxygène par la société HOLOMORPHE 
                        à son client est en vigueur au jour de la date de signature du contrat de vente de gré à gré 
                        d'un mélange gazeux de dihydrogène et de dioxygène entre les parties du présent contrat.
                        <br>
                        <br>
                        Le prix de vente du mélange gazeux de dihydrogène et de dioxygène par la société HOLOMORPHE 
                        à son client est libellé en euros et calculé hors taxes. Par voie de conséquence, le prix de 
                        vente du mélange gazeux de dihydrogène et de dioxygène par la société HOLOMORPHE à son client 
                        sera majoré du taux de la taxe sur la valeur ajoutée en vertu de l'article  du code général 
                        des impôts du droit français.
                        <br>
                        <br>
                        Les frais de transport du mélange gazeux de dihydrogène et de dioxygène vendu par la société 
                        HOLOMORPHE à son client sont nuls pendant tout la durée du présent contrat entre les parties 
                        du présent contrat.
                        <br>
                        <br>
                        Le prix de vente du mélange gazeux de dihydrogène et de dioxygène par la société HOLOMORPHE 
                        à son client sera définitif pendant toute la durée du présent contrat entre les parties 
                        du présent contrat.
                        <br>
                        <br>
                        Le montant du prix de vente du mélange gazeux de dihydrogène et de dioxygène par 
                        la société HOLOMORPHE à son client est égal à trois euros le kilogramme pendant toute 
                        la durée du présent contrat entre les parties du contrat.
                      </div>
                    </div>

                    <br>

                    <!-- Clause n°  : Rabais et ristournes -->
                    <div class="card text-center">
                      <div class="card-header">
                        Clause n°  : Rabais et ristournes
                      </div>
                      <div class="card-body">
                        Les tarifs proposés comprennent les rabais et ristournes que la société ... 
                        (dénomination sociale) serait amenée à octroyer compte tenu de ses résultats ou de 
                        la prise en charge par l'acheteur de certaines prestations.
                      </div>
                    </div>

                    <br>

                    <!-- Clause n°  : Escompte -->
                    <div class="card text-center">
                      <div class="card-header">
                        Clause n°  : Escompte
                      </div>
                      <div class="card-body">
                        Aucun escompte ne sera consenti en cas de paiement anticipé 
                      </div>
                    </div>

                    <br>

                    <!-- Clause n°  : Modalités de paiement -->
                    <div class="card text-center">
                      <div class="card-header">
                        Clause n°  : Modalités de paiement
                      </div>
                      <div class="card-body">
                        Le règlement des commandes s'effectue :
                        <br>
                        - soit par chèque ;
                        <br>
                        - soit par carte bancaire ;
                        <br>
                        -le cas échéant, indiquer les autres moyens de paiement acceptés.
                        <br>
                        <br>
                        Lors de l'enregistrement de la commande, l'acheteur devra verser un acompte de 10% du 
                        montant global de la facture, le solde devant être payé à réception des marchandises.
                      </div>
                    </div>

                    <br>

                    <!-- Clause n° : Retard de paiement -->
                    <div class="card text-center">
                      <div class="card-header">
                        Clause n° : Retard de paiement
                      </div>
                      <div class="card-body">
                        En cas de défaut de paiement total ou partiel des marchandises livrées au jour de la 
                        réception, l'acheteur doit verser à la société ... (dénomination sociale) une pénalité de 
                        retard égale à trois fois le taux de l'intérêt légal.
                        <br>
                        Le taux de l'intérêt légal retenu est celui en vigueur au jour de la livraison des 
                        marchandises.
                        <br>
                        A compter du 1er janvier 2015, le taux d'intérêt légal sera révisé tous les 6 mois 
                        (Ordonnance n°2014-947 du 20 août 2014).
                        <br>
                        Cette pénalité est calculée sur le montant TTC de la somme restant due, et court à 
                        compter de la date d'échéance du prix sans qu'aucune mise en demeure préalable ne soit 
                        nécessaire.
                        <br>
                        En sus des indemnités de retard, toute somme, y compris l’acompte, non payée à sa date 
                        d’exigibilité produira de plein droit le paiement d’une indemnité forfaitaire de 40 euros 
                        due au titre des frais de recouvrement.
                        <br>
                        Articles 441-6, I alinéa 12 et D. 441-5 du code de commerce.
                      </div>
                    </div>
                    
                    <br>

                    <!-- Clause n° : Clause résolutoire -->
                    <div class="card text-center">
                      <div class="card-header">
                        Clause n° : Clause résolutoire
                      </div>
                      <div class="card-body">
                        Si dans les quinze jours qui suivent la mise en oeuvre de la clause "Retard de 
                        paiement", l'acheteur ne s'est pas acquitté des sommes restant dues, la vente sera 
                        résolue de plein droit et pourra ouvrir droit à l'allocation de dommages et intérêts au 
                        profit de la société ... (dénomination sociale).
                      </div>
                    </div>
                    
                    <br>

                    <!-- Clause n° : Clause de réserve de propriété -->
                    <div class="card text-center">
                      <div class="card-header">
                        Clause n° : Clause de réserve de propriété
                      </div>
                      <div class="card-body">
                        La société ... (dénomination sociale) conserve la propriété des biens vendus jusqu'au 
                        paiement intégral du prix, en principal et en accessoires.
                        <br>
                        À ce titre, si l'acheteur fait l'objet d'un redressement ou d'une liquidation judiciaire, la société ... 
                        (dénomination sociale) se réserve le droit de revendiquer, dans le cadre de la procédure 
                        collective, les marchandises vendues et restées impayées.
                      </div>
                    </div>
                    
                    <br>

                    <!-- Clause n° : Livraison -->
                    <div class="card text-center">
                      <div class="card-header">
                        Clause n° : Livraison
                      </div>
                      <div class="card-body">
                        La livraison est effectuée :
                        <br>
                        - soit par la remise directe de la marchandise à l'acheteur ;
                        <br>
                        - soit par l'envoi d'un avis de mise à disposition en magasin à l'attention de l'acheteur ;
                        <br>
                        - soit au lieu indiqué par l'acheteur sur le bon de commande.
                        <br>
                        <br>
                        Le délai de livraison indiqué lors de l'enregistrement de la commande n'est donné qu'à 
                        titre indicatif et n'est aucunement garanti.
                        <br>
                        <br>
                        Par voie de conséquence, tout retard raisonnable dans la livraison des produits ne 
                        pourra pas donner lieu au profit de l'acheteur à :
                        <br>
                        - l'allocation de dommages et intérêts ;
                        <br>
                        - l'annulation de la commande.
                        <br>
                        <br>
                        Le risque du transport est supporté en totalité par l'acheteur.
                        <br>
                        En cas de marchandises manquantes ou détériorées lors du transport, l'acheteur devra 
                        formuler toutes les réserves nécessaires sur le bon de commande à réception desdites 
                        marchandises.
                        <br>
                        Ces réserves devront être, en outre, confirmées par écrit dans les cinq jours 
                        suivant la livraison, par courrier recommandé AR.
                      </div>
                    </div>
                    
                    <br>

                    <!-- Clause n° : Force majeure -->
                    <div class="card text-center">
                      <div class="card-header">
                        Clause n° : Force majeure
                      </div>
                      <div class="card-body">
                        La responsabilité de la société ... (dénomination sociale) ne pourra pas être mise en 
                        oeuvre si la non-exécution ou le retard dans l'exécution de l'une de ses obligations 
                        décrites dans les présentes conditions générales de vente découle d'un cas de force majeure.
                        <br>
                        À ce titre, la force majeure s'entend de tout événement extérieur, imprévisible et 
                        irrésistible au sens de l'article 1148 du Code civil.
                      </div>
                    </div>
                    
                    <br>
                    
                    <!-- Clause n° : Assurance responsabilité civile professionnelle -->
                    <div class="card text-center">
                      <div class="card-header">
                        Clause n° : Assurance responsabilité civile professionnelle
                      </div>
                      <div class="card-body">
                      </div>
                    </div>
                    
                    <br>
                    
                    <!-- Clause n° : Fichier national des interdits à gérer -->
                    <div class="card text-center">
                      <div class="card-header">
                        Clause n° : Fichier national des interdits à gérer
                      </div>
                      <div class="card-body">
                      </div>
                    </div>
                    
                    <br>
                    
                    <!-- Clause n° : Protection du secret des affaires -->
                    <div class="card text-center">
                      <div class="card-header">
                        Clause n° : Protection du secret des affaires
                      </div>
                      <div class="card-body">
                      </div>
                    </div>
                    
                    <br>
                    
                    <!-- Clause n° : Clause d'exclusivité -->
                    <div class="card text-center">
                      <div class="card-header">
                        Clause n° : Clause d'exclusivité
                      </div>
                      <div class="card-body">
                      </div>
                    </div>
                    
                    <br>
                    
                    <!-- Clause n° : Bons carbone -->
                    <div class="card text-center">
                      <div class="card-header">
                        Clause n° : Bons carbone
                      </div>
                      <div class="card-body">
                      </div>
                    </div>
                    
                    <br>
                    
                    <!-- Clause n° : Pratiques anticoncurrentielles -->
                    <div class="card text-center">
                      <div class="card-header">
                        Clause n° : Pratiques anticoncurrentielles
                      </div>
                      <div class="card-body">
                      </div>
                    </div>
                    
                    <br>
                    
                    <!-- Clause n° :  -->
                    <div class="card text-center">
                      <div class="card-header">
                        
                      </div>
                      <div class="card-body">
                      </div>
                    </div>
                    
                    <br>
                    
                    <!-- Clause n° : Tribunal compétent -->
                    <div class="card text-center">
                      <div class="card-header">
                        Clause n° : Tribunal compétent
                      </div>
                      <div class="card-body">
                        Tout litige relatif à l'interprétation et à l'exécution des présentes conditions générales 
                        de vente est soumis au droit français.
                        <br>
                        À défaut de résolution amiable, le litige sera porté devant le Tribunal de commerce ... 
                        (lieu du siège social).
                      </div>
                    </div>
                    
                  </div>
                </div>
                
                <br>
                
                <!-- Signature des parties -->
                <div class="card text-center">
                  <div class="card-header">
                    Signature des parties
                  </div>
                  <div class="card-body">
                    Fait à Paris (75007), le 24 Septembre 2021
                    
                    <br>
                    
                    <!-- Signature du client -->
                    <div class="card text-center">
                      <div class="card-header">
                        Signature du client
                      </div>
                      <div class="card-body">
                        <br>
                        <br>
                        <br>
                        <br>
                        <br>
                        <br>
                        <br>
                      </div>
                    </div>
                    
                    <br>
                    
                    <!-- Signature du représentant légal de la société HOLOMORPHE -->
                    <div class="card text-center">
                      <div class="card-header">
                        Signature du représentant légal de la société HOLOMORPHE
                      </div>
                      <div class="card-body">
                        <br>
                        <br>
                        <br>
                        <br>
                        <br>
                        <br>
                        <br>
                      </div>
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
            'header-center': "Contrat de vente de gré à gré d'un mélange gazeux de dihydrogène et de dioxygène",
            'footer-right': '[page] sur [topage]',
            'footer-left': 'Société Holomorphe [SIREN : 883632556]'
        }

        path_wkthmltopdf = "C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe"
        config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
        pdfkit.from_string(body,
                           "Contrat_Gre_A_Gre\\Contrat_Gre_A_Gre_[Societe_Holomorphe].pdf",
                           configuration=config,
                           options=options)


if __name__ == '__main__':
    unittest.main()
