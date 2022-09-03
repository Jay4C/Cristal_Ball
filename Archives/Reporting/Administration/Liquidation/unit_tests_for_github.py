import unittest
import pdfkit


class UnitTestsReportingAdministrationLiquidationForGitHub(unittest.TestCase):
    # ok
    def test_liquidation(self):
        print('test_liquidation')

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

    <title>Liquidation</title>
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
                Dénomination sociale : S.A.S.U. à capital variable ... / 
                Capital social :  euros
              </li>
              <li class="list-group-item">
                Adresse du siège social : ... / 
                Siret : ...
              </li>
              <li class="list-group-item">
                Registre du commerce et des sociétés : ...
              </li>
              <li class="list-group-item">
                Activités : ... / 
                Code NAF : ...
              </li>
              <li class="list-group-item">
                Numero TVA intracommunataire : ... / 
                Président : ... / 
                Date d'immatriculation : ...
              </li>
            </ul>
          </div>
        </div>
        <!-- Informations générales -->

        <br>
        <br>

        <!-- Procès-verbal de liquidation de la S.A.S.U.A.C.V. ... -->
        <div class="card text-center">
          <div class="card-header">
            Procès-verbal de liquidation de la S.A.S.U.A.C.V. ...
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

                ... demeurant au ..., actionnaire unique de la société par actions simplifiée unipersonnelle à 
                capital variable ..., a pris les décisions suivantes :

                <br>

                - Approbation des comptes de liquidation de la société par actions simplifiée unipersonnelle à capital 
                variable ... ;
                <br>
                - Répartition du solde de liquidation de la société par actions simplifiée unipersonnelle à capital 
                variable ... ;
                <br>
                - Constatation de la clôture des opérations de liquidation de la société par actions simplifiée 
                unipersonnelle à capital variable ... ;
                <br>
                - Pouvoir en vue d'accomplir les formalités pour le compte de la société par actions simplifiée 
                unipersonnelle à capital variable ... .
            </h6>

            <br>
            <br>

            <!-- Première résolution -->
            <div class="card text-center">
              <div class="card-header">
                Première résolution - Approbation des comptes de liquidation de la société par actions simplifiée 
                unipersonnelle à capital variable ...
              </div>
              <div class="card-body">
                ..., actionnaire unique de la société par actions simplifiée unipersonnelle à 
                capital variable ..., approuve les opérations de liquidation de la société par actions 
                simplifiée unipersonnelle à capital variable ... ainsi que les comptes définitifs de la société 
                par actions simplifiée unipersonnelle à capital variable ... qui en résultent, faisant ressortir 
                un solde ... de ... euros.
              </div>
            </div>
            <!-- Première résolution -->

            <br>
            <br>

            <!-- Deuxième résolution -->
            <div class="card text-center">
              <div class="card-header">
                Deuxième résolution - Répartition du solde de liquidation de la société par actions simplifiée 
                unipersonnelle à capital variable ...
              </div>
              <div class="card-body">
                L'actionnaire unique de la société par actions simplifiée unipersonnelle à capital variable ... 
                décide de répartir le solde ... de liquidation de la société par actions simplifiée unipersonnelle à 
                capital variable ... s'élevant à ... euros de la façon suivante : [« attribution au profit de 
                l'associé unique de la société par actions simplifiée unipersonnelle à capital variable ... 
                » en cas de boni ou « remboursement partiel des titres souscrits à hauteur de [Montant remboursé] 
                euros » en cas de mali].
              </div>
            </div>
            <!-- Deuxième résolution -->

            <br>
            <br>

            <!-- Troisième résolution -->
            <div class="card text-center">
              <div class="card-header">
                Troisième résolution - Constatation de la clôture des opérations de liquidation de la société par 
                actions simplifiée unipersonnelle à capital variable ...
              </div>
              <div class="card-body">
                L'associé unique de la société par actions simplifiée unipersonnelle à capital variable ... 
                donne quitus au liquidateur de la société par actions simplifiée unipersonnelle à capital variable 
                ... de sa gestion et le décharge de son mandat.

                <br>
                <br>

                L'associé unique de la société par actions simplifiée unipersonnelle à capital variable ... 
                constate la fin des opérations de liquidation de la société par actions simplifiée unipersonnelle 
                à capital variable ... et prononce la clôture définitive de la liquidation de la société 
                par actions simplifiée unipersonnelle à capital variable ... .

                <br>
                <br>

                Par conséquent, la société par actions simplifiée unipersonnelle à capital variable ... cesse 
                d'exister à compter de ce jour.
              </div>
            </div>
            <!-- Troisième résolution -->

            <br>
            <br>

            <!-- Quatrième résolution -->
            <div class="card text-center">
              <div class="card-header">
                Quatrième résolution - Pouvoir en vue d'accomplir les formalités pour le compte de la société par 
                actions simplifiée unipersonnelle à capital variable ...
              </div>
              <div class="card-body">
                L'actionnaire unique de la société par actions simplifiée unipersonnelle à capital variable ... 
                donne tous pouvoirs à ... pour effectuer les formalités légales afférentes aux 
                décisions adoptées ci-dessus.

                <br>
                <br>

                De tout ce qui précède, il a été dressé le présent procès-verbal de liquidation de la société par 
                actions simplifiée unipersonnelle à capital variable ... signé par l'actionnaire unique 
                de la société par actions simplifiée unipersonnelle à capital variable ... .
              </div>
            </div>
            <!-- Quatrième résolution -->

            <br>
            <br>

            <!-- L'actionnaire unique de la société -->
            <div class="card text-center">
              <div class="card-header">
                L'actionnaire unique de la société par actions simplifiée unipersonnelle à capital variable ...
              </div>
              <div class="card-body">
                ..., l'actionnaire unique de la société par actions simplifiée unipersonnelle à capital variable ... .
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
                Fait à ..., le ... .
                <br>
                Lu et approuvé.
              </div>
            </div>
            <!-- Date et lieu de l'approbation -->
          </div>
        </div>
        <!-- Procès-verbal de liquidation de la ... -->
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
            'footer-left': 'Société ... [SIREN : ...] ',
            'header-center': 'Procès-verbal de liquidation de la ...',
        }

        pdfkit.from_string(
            body,
            "/Liquidation/PV_Liquidation.pdf",
            options=options
        )


if __name__ == '__main__':
    unittest.main()
