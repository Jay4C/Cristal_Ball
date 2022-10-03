import unittest
import pdfkit


class UnitTestsLettreResiliationForGitHub(unittest.TestCase):
    # ok
    def test_lettre_de_resiliation_de_bail(self):
        print('test_lettre_de_resiliation_de_bail')

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

    <title>Resume</title>
  </head>
  <body>
    <!-- Container -->
    <div class="container">
        <!-- Lettre de résiliation de bail -->
        <div class="card text-center">
          <div class="card-header">
            Lettre de résiliation de bail
          </div>
          <div class="card-body">
            <!-- Destinataire -->
            <div class="card text-center">
              <div class="card-header">
                Destinataire
              </div>
              <div class="card-body">
                <h6>Nom ou raison sociale : CDC Habitat Social - Agence La Plaine Saint Denis</h6>
                <h6>Adresse postale : 221 Avenue du Président Wilson 93200 Saint-Denis</h6>
              </div>
            </div>
            <!-- Destinataire -->

            <br>
            <br>

            <!-- Expéditeur -->
            <div class="card text-center">
              <div class="card-header">
                Expéditeur
              </div>
              <div class="card-body">
                <h6>Nom ou raison sociale : </h6>
                <h6>Adresse postale : </h6>
                <h6>Téléphone : </h6>
                <h6>Email : </h6>
              </div>
            </div>
            <!-- Expéditeur -->

            <br>
            <br>

            <!-- Date et lieu d'envoi -->
            <div class="card text-center">
              <div class="card-header">
                Date et lieu d'envoi
              </div>
              <div class="card-body">
                Fait à , le 30 Novembre 2022.
              </div>
            </div>
            <!-- Date et lieu d'envoi -->
            
            <br>
            <br>

            <!-- Objet -->
            <div class="card text-center">
              <div class="card-header">
                Objet
              </div>
              <div class="card-body">
                Résiliation de bail
              </div>
            </div>
            <!-- Objet -->
            
            <br>
            <br>

            <!-- Message -->
            <div class="card text-center">
              <div class="card-header">
                Message
              </div>
              <div class="card-body">
                <h6>
                    Bonjour,
                </h6>
                 
                <br>
                
                <h6>
                   Je suis locataire du logement situé au  depuis le ... 
                   décembre 2019.
                </h6>
                
                <br>
                
                <h6>
                    Je vous fais part de mon intention de résilier le contrat de location pour le motif suivant : 
                    déménagement.    
                </h6>
                
                <br>
                
                <h6>
                    Je vous donne donc congé, lequel prendra effet, eu égard du délai de préavis de 1 mois prévu par la 
                    loi soit le ... décembre 2022. 
                    Je vous informe que ma nouvelle adresse sera la suivante : ... .
                </h6>
                
                <br>
                
                <h6>
                    Conformément à l'article 15 de la loi du 6 juillet 1989, je bénéficie, en effet, du droit à préavis 
                    réduit, en raison des circonstances suivantes : occupation d'un logement situé sur un territoire 
                    en zone tendue.    
                </h6>
                
                <br>
                
                <h6>
                    Je me tiens à votre disposition pour convenir d'un rendez-vous afin d'établir l'état des lieux de 
                    sortie.
                </h6>
                
                <br>
                
                <h6>
                    Dans l'attente de votre retour, je vous prie de croire, l'expression de mes sentiments distingués.
                </h6>
              </div>
            </div>
            <!-- Message -->
            
            <br>
            <br>
            
            <!-- Signature -->
            <div class="card text-center">
              <div class="card-header">
                Signature
              </div>
              <div class="card-body">
                Lu et approuvé par .
                <br>
                <br>
                <br>
                <br>
                <br>
                <br>
              </div>
            </div>
            <!-- Signature -->

            <br>

        </div>
        <!-- Lettre de résiliation de bail -->
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
            'header-center': 'Lettre de résiliation de bail',
        }

        pdfkit.from_string(
            body,
            "Resiliation\\lettre_resiliation_de_bail.pdf",
            options=options
        )

    # ok
    def test_lettre_de_resiliation_ohm_energie(self):
        print('test_lettre_de_resiliation_ohm_energie')

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

    <title>Resume</title>
  </head>
  <body>
    <!-- Container -->
    <div class="container">
        <!-- Lettre de résiliation de bail -->
        <div class="card text-center">
          <div class="card-header">
            Lettre de résiliation d'une offre d'électricité
          </div>
          <div class="card-body">
            <!-- Destinataire -->
            <div class="card text-center">
              <div class="card-header">
                Destinataire
              </div>
              <div class="card-body">
                <h6>Nom ou raison sociale : Ohm Energie - Service client</h6>
                <h6>Adresse postale : 10 rue de Penthièvre 75008 Paris</h6>
              </div>
            </div>
            <!-- Destinataire -->

            <br>
            <br>

            <!-- Expéditeur -->
            <div class="card text-center">
              <div class="card-header">
                Expéditeur
              </div>
              <div class="card-body">
                <h6>Nom ou raison sociale : </h6>
                <h6>Adresse postale : </h6>
                <h6>Téléphone : </h6>
                <h6>Email : </h6>
              </div>
            </div>
            <!-- Expéditeur -->

            <br>
            <br>

            <!-- Date et lieu d'envoi -->
            <div class="card text-center">
              <div class="card-header">
                Date et lieu d'envoi
              </div>
              <div class="card-body">
                Fait à , le 30 Novembre 2022.
              </div>
            </div>
            <!-- Date et lieu d'envoi -->

            <br>
            <br>

            <!-- Objet -->
            <div class="card text-center">
              <div class="card-header">
                Objet
              </div>
              <div class="card-body">
                Résiliation d'une offre d'électricité
              </div>
            </div>
            <!-- Objet -->

            <br>
            <br>

            <!-- Message -->
            <div class="card text-center">
              <div class="card-header">
                Message
              </div>
              <div class="card-body">
                <h6>
                    Bonjour,
                </h6>

                <br>

                <h6>
                   Je vous informe, par la présente, que je souhaite mettre fin à mon contrat d'électricité Ohm Énergie.
                </h6>

                <br>

                <h6>
                    Vous trouverez ci-dessous les informations nécessaires à la clôture de mon offre :
                    <br>
                    - le numéro de mon contrat/d'abonné : ............
                    <br>
                    - le relevé de mon compteur : ............
                </h6>

                <br>

                <h6>
                    Merci de traiter ma demande dès sa réception et de me confirmer par écrit le terme du contrat.
                </h6>

                <br>

                <h6>
                    Dans cette attente, je vous prie d'agréer, Madame, Monsieur, mes salutations respectueuses.   
                </h6>
              </div>
            </div>
            <!-- Message -->

            <br>
            <br>

            <!-- Signature -->
            <div class="card text-center">
              <div class="card-header">
                Signature
              </div>
              <div class="card-body">
                Lu et approuvé par .
                <br>
                <br>
                <br>
                <br>
                <br>
                <br>
              </div>
            </div>
            <!-- Signature -->

            <br>

        </div>
        <!-- Lettre de résiliation d'une offre d'électricité -->
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
            'header-center': "Lettre de résiliation d'une offre d'électricité",
        }

        pdfkit.from_string(
            body,
            "Resiliation\\lettre_resiliation_offre_electricité.pdf",
            options=options
        )

    # ok
    def test_lettre_de_resiliation_assurance_habitation(self):
        print('test_lettre_de_resiliation_assurance_habitation')

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

    <title>Resume</title>
  </head>
  <body>
    <!-- Container -->
    <div class="container">
        <!-- Lettre de résiliation de la police d'assurance habitation -->
        <div class="card text-center">
          <div class="card-header">
            Lettre de résiliation de la police d'assurance habitation numéro ...
          </div>
          <div class="card-body">
            <!-- Destinataire -->
            <div class="card text-center">
              <div class="card-header">
                Destinataire
              </div>
              <div class="card-body">
                <h6>Nom ou raison sociale : ALLIANZ IARD</h6>
                <h6>Adresse postale : 1 cours Michelet CS 30051 92076 PARIS LA DÉFENSE</h6>
              </div>
            </div>
            <!-- Destinataire -->

            <br>
            <br>

            <!-- Expéditeur -->
            <div class="card text-center">
              <div class="card-header">
                Expéditeur
              </div>
              <div class="card-body">
                <h6>Nom ou raison sociale : </h6>
                <h6>Adresse postale : </h6>
                <h6>Téléphone : </h6>
                <h6>Email : </h6>
              </div>
            </div>
            <!-- Expéditeur -->

            <br>
            <br>

            <!-- Date et lieu d'envoi -->
            <div class="card text-center">
              <div class="card-header">
                Date et lieu d'envoi
              </div>
              <div class="card-body">
                Fait à , le 30 Novembre 2022.
              </div>
            </div>
            <!-- Date et lieu d'envoi -->

            <br>
            <br>

            <!-- Objet -->
            <div class="card text-center">
              <div class="card-header">
                Objet
              </div>
              <div class="card-body">
                Résiliation de la police d'assurance habitation numéro ...
              </div>
            </div>
            <!-- Objet -->

            <br>
            <br>

            <!-- Message -->
            <div class="card text-center">
              <div class="card-header">
                Message
              </div>
              <div class="card-body">
                <h6>
                    Bonjour,
                </h6>

                <br>

                <h6>
                   Conformément aux dispositions de l’article L113-16 du Code des Assurances, je désire résilier 
                   le contrat d'assurance habitation numéro ... . Cette résiliation sera effective dans le délai d'un 
                   mois à compter de la présente notification pour le motif suivant :
                   <br>
                   - Changement de domicile
                </h6>

                <br>

                <h6>
                    Ci-joint à cette lettre l’état des lieux de sortie.
                </h6>

                <br>

                <h6>
                    Conformément à la Loi Hamon, je suis en droit de procéder à la résiliation de la police d'assurance 
                    habitation sans préavis puisque mon contrat a plus d’un an. Je souhaite que la résiliation prenne 
                    effet à compter du 30 Novembre 2022.
                </h6>

                <br>

                <h6>
                    Dans l'attente de votre retour, je vous prie de croire, l'expression de mes sentiments distingués.
                </h6>
              </div>
            </div>
            <!-- Message -->

            <br>
            <br>

            <!-- Signature -->
            <div class="card text-center">
              <div class="card-header">
                Signature
              </div>
              <div class="card-body">
                Lu et approuvé par .
                <br>
                <br>
                <br>
                <br>
                <br>
                <br>
              </div>
            </div>
            <!-- Signature -->

            <br>

        </div>
        <!-- Lettre de résiliation de la police d'assurance habitation -->
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
            'header-center': "Lettre de résiliation de la police d'assurance habitation",
        }

        pdfkit.from_string(
            body,
            "Resiliation\\lettre_resiliation_police_assurance_habitation.pdf",
            options=options
        )


if __name__ == '__main__':
    unittest.main()
