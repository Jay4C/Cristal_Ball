import unittest
import pdfkit


class UnitTestsLettreProcurationForGitHub(unittest.TestCase):
    #
    def test_lettre_de_procuration(self):
        print('test_lettre_de_procuration')

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

    <title>Lettre de procuration</title>
  </head>
  <body>
    <!-- Container -->
    <div class="container">
        <!-- Lettre de procuration -->
        <div class="card text-center">
          <div class="card-header">
            Lettre de procuration
          </div>
          <div class="card-body">
            <!-- Destinataire -->
            <div class="card text-center">
              <div class="card-header">
                Destinataire
              </div>
              <div class="card-body">
                <h6>Nom ou raison sociale : La Poste </h6>
                <h6>Adresse postale : </h6>
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
                Fait à , le 04 Octobre 2022.
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
                Procuration
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
                   Je soussigné(e) … (prénom et nom), né(e) le … à … et demeurant à l’adresse …, déclare donner 
                   pouvoir par la présente à Madame / Monsieur … (prénom et nom), né(e) le … à … et résidant au … 
                   afin de me représenter conformément à mes intérêts auprès de vos services.
                </h6>
                
                <br>
                
                <h6>
                    Cette procuration est valable à compter de ce jour jusqu’au …. Le mandataire sera en droit de 
                    réaliser les actes suivants en mon nom propre : 
                    <br>
                    - Récupérer les courriers ;
                    <br>
                    - Signer les actes attachés à la récupération des courriers.
                </h6>
                
                <br>
                
                <h6>
                    Pour faire valoir ce que de droit.
                </h6>
              </div>
            </div>
            <!-- Message -->
            
            <br>
            <br>
            
            <!-- Signature -->
            <div class="card text-center">
              <div class="card-header">
                Signature du mandant
              </div>
              <div class="card-body">
                Lu et approuvé par .
                <br>
                Bon pour mandat.
                <br>
                <br>
                <br>
                <br>
                <br>
              </div>
            </div>
            <!-- Signature -->
            
            <br>
            <br>
            
            <!-- Signature du bénéficiaire -->
            <div class="card text-center">
              <div class="card-header">
                Signature du bénéficiaire 
              </div>
              <div class="card-body">
                Bon pour acceptation.
                <br>
                <br>
                <br>
                <br>
                <br>
                <br>
              </div>
            </div>
            <!-- Signature du bénéficiaire -->

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
            'header-center': 'Lettre de procuration',
        }

        pdfkit.from_string(
            body,
            "Procuration\\lettre_procuration.pdf",
            options=options
        )


if __name__ == '__main__':
    unittest.main()
