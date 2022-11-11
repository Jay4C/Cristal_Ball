import unittest
import pdfkit


class UnitTestsReportingAdministrationDissolutionForGitHub(unittest.TestCase):
    # ok
    def test_dissolution_holomorphe(self):
        print('test_dissolution_holomorphe')

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

    <title>Dissolution</title>
  </head>
  <body>
    <!-- Container -->
    <div class="container">
        <!-- Informations générales -->
        <div class="card text-center">
          <div class="card-header">
            Informations générales
          </div>
          <div class="card-body">
            <ul class="list-group">
              <li class="list-group-item">
                Dénomination sociale : S.A.S.U. à capital variable HOLOMORPHE / 
                Capital social : 100 euros
              </li>
              <li class="list-group-item">
                Adresse du siège social : 31 Avenue de Ségur - ABC LIV Ségur - 75007 Paris / 
                Siret : 88363255600014 
              </li>
              <li class="list-group-item">
                Registre du commerce et des sociétés : R.C.S. PARIS - Greffe duTribunal de Commerce de PARIS
              </li>
              <li class="list-group-item">
                Activités : Commerce de gros de produits chimiques - Edition de logiciels applicatifs / 
                Code NAF : 4675Z
              </li>
              <li class="list-group-item">
                Numero TVA intracommunataire : FR06883632556 / 
                Président :  / 
                Date d'immatriculation : 26 Mai 2020
              </li>
            </ul>
          </div>
        </div>
        <!-- Informations générales -->

        <br>
        <br>

        <!-- Procès-verbal de dissolution de la S.A.S.U.A.C.V. HOLOMORPHE -->
        <div class="card text-center">
          <div class="card-header">
            Procès-verbal de dissolution de la S.A.S.U.A.C.V. HOLOMORPHE
          </div>
          <div class="card-body">
            <h6>
                Vu l'article 1844-7 du Code civil,
                
                <br>
                
                Vu les articles L237-1 à L237-13 du Code de commerce concernant les dispositions générales de la 
                liquidation,
                
                <br>
                
                Vu la loi n°2019-1479 du 28 décembre 2019 de finances pour 2020,
                
                <br>
                <br>
                
                Monsieur ... demeurant au ..., 
                actionnaire unique de la société par actions simplifiée unipersonnelle à capital variable HOLOMORPHE, 
                a pris les décisions concernant l'ordre du jour suivant:
                
                <br>
                
                - Dissolution anticipée de la société par actions simplifiée unipersonnelle à capital variable HOLOMORPHE ;
                <br>
                - Nomination du liquidateur de la société par actions simplifiée unipersonnelle à capital variable 
                HOLOMORPHE ;
                <br>
                - Rémunération du liquidateur de la société par actions simplifiée unipersonnelle à capital variable 
                HOLOMORPHE.
            </h6>

            <br>
            <br>

            <!-- Première résolution -->
            <div class="card text-center">
              <div class="card-header">
                Première résolution
              </div>
              <div class="card-body">
                L'actionnaire unique de la société par actions simplifiée unipersonnelle à capital variable HOLOMORPHE 
                décide de la dissolution anticipée de la société par actions simplifiée unipersonnelle à capital 
                variable HOLOMORPHE et sa liquidation amiable conformément aux dispositions des articles L237-1 à 
                237-13 du Code de commerce.

                <br>
                <br>

                La société par actions simplifiée unipersonnelle à capital variable HOLOMORPHE subsistera pour les 
                besoins de la liquidation et jusqu'à la clôture de celle-ci.

                <br>
                <br>

                Durant cette période, la dénomination sociale de la société par actions simplifiée unipersonnelle à 
                capital variable HOLOMORPHE sera suivie de la mention "société en liquidation". Cette mention ainsi 
                que le nom du liquidateur devront figurer sur tous les documents et actes destinés au tiers.

                <br>
                <br>

                Le siège social de la liquidation de la société par actions simplifiée unipersonnelle à capital 
                variable HOLOMORPHE est fixé au 6 Avenue Léon Blum 93800 Epinay-sur-Seine.
              </div>
            </div>
            <!-- Première résolution -->

            <br>
            <br>

            <!-- Deuxième résolution -->
            <div class="card text-center">
              <div class="card-header">
                Deuxième résolution
              </div>
              <div class="card-body">
                L'actionnaire unique de la société par actions simplifiée unipersonnelle à capital variable HOLOMORPHE 
                sera désigné en qualité de liquidateur de la société par actions simplifiée unipersonnelle à capital 
                variable HOLOMORPHE et pour une durée de deux mois.

                <br>
                <br>

                Dans les deux mois de sa nomination, le liquidateur de la société par actions simplifiée unipersonnelle 
                à capital variable HOLOMORPHE doit faire un rapport sur la situation comptable de la société par 
                actions simplifiée unipersonnelle à capital variable HOLOMORPHE, sur la poursuite des opérations de 
                liquidation de la société par actions simplifiée unipersonnelle à capital variable HOLOMORPHE et sur le 
                délai nécessaire pour les terminer.

                <br>
                <br>

                L'actionnaire unique de la société par actions simplifiée unipersonnelle à capital variable 
                HOLOMORPHE décide que le liquidateur de la société par actions simplifiée unipersonnelle à capital 
                variable HOLOMORPHE n'a pas droit, en contrepartie de l'exercice de son mandat, à une rémunération.

                <br>
                <br>

                Monsieur ... déclare accepter ses fonctions de liquidateur de la 
                société par actions simplifiée unipersonnelle à capital variable HOLOMORPHE et certifie ne pas 
                être sous le coup des interdictions prévues par les lois et règlements en vigueur.
              </div>
            </div>
            <!-- Deuxième résolution -->

            <br>
            <br>

            <!-- Troisième résolution -->
            <div class="card text-center">
              <div class="card-header">
                Troisième résolution
              </div>
              <div class="card-body">
                L'actionnaire unique de la société par actions simplifiée unipersonnelle à capital variable HOLOMORPHE 
                donne au liquidateur de la société par actions simplifiée unipersonnelle à capital variable HOLOMORPHE 
                les pouvoirs les plus étendus pour mener à bien sa mission, c'est-à-dire réaliser l'actif, 
                payer le passif et répartir le solde, sous réserve des dispositions des articles L237-1 et suivants du 
                Code decommerce.
              </div>
            </div>
            <!-- Troisième résolution -->

            <br>
            <br>

            <!-- Quatrième résolution -->
            <div class="card text-center">
              <div class="card-header">
                Quatrième résolution
              </div>
              <div class="card-body">
                Tous pouvoirs sont attribués au liquidateur de la société par actions simplifiée unipersonnelle à 
                capital variable HOLOMORPHE pour effectuer les formalités légales afférentes aux décisions adoptées 
                ci-dessus.

                <br>
                <br>

                L'ordre du jour étant épuisé, la séance est levée.

                <br>
                <br>

                De tout ce qui précède, il a été dressé le présent procès-verbal de dissolution de la société par 
                actions simplifiée unipersonnelle à capital variable HOLOMORPHE signé par l'actionnaire unique 
                de la société paractions simplifiée unipersonnelle à capital variable HOLOMORPHE.
              </div>
            </div>
            <!-- Quatrième résolution -->

            <br>
            <br>

            <!-- L'actionnaire unique de la société -->
            <div class="card text-center">
              <div class="card-header">
                L'actionnaire unique de la société par actions simplifiée unipersonnelle à capital variable HOLOMORPHE
              </div>
              <div class="card-body">
                Monsieur ..., l'actionnaire unique de la société par actions 
                simplifiée unipersonnelle à capital variable HOLOMORPHE.
              </div>
            </div>
            <!-- L'actionnaire unique de la société -->

            <br>
            <br>

            <!-- Date et lieu de l'approbation -->
            <div class="card text-center">
              <div class="card-header">
                Date et lieu de l'approbation
              </div>
              <div class="card-body">
                Fait à Paris (75007), le 26/06/2022.
                <br>
                Lu et approuvé.
              </div>
            </div>
            <!-- Date et lieu de l'approbation -->
          </div>
        </div>
        <!-- Procès-verbal de dissolution de la S.A.S.U.A.C.V. HOLOMORPHE -->
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
            'footer-left': 'Société HOLOMORPHE [SIREN : 883 632 556] ',
            'header-center': 'Procès-verbal de dissolution de la S.A.S.U.A.C.V. HOLOMORPHE',
        }

        pdfkit.from_string(
            body,
            "Dissolution_For_Me\\PV_Dissolution_Holomorphe.pdf",
            options=options
        )


if __name__ == '__main__':
    unittest.main()
