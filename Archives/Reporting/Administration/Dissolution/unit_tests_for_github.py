import unittest
import pdfkit


class UnitTestsReportingAdministrationDissolutionForGitHub(unittest.TestCase):
    # ok
    def test_dissolution(self):
        print('test_dissolution')

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
              <li class="list-group-item">Dénomination sociale :  / Capital social:  euros</li>
              <li class="list-group-item">Adresse du siège social :  / Siret : </li>
              <li class="list-group-item">Registre du commerce et des sociétés : </li>
              <li class="list-group-item">Activités : / Code NAF : </li>
              <li class="list-group-item">Numero TVA intracommunataire :  / Président : / Date d'immatriculation : </li>
            </ul>
          </div>
        </div>
        <!-- Informations générales -->
        
        <br>
        <br>
        
        <!-- Procès-verbal de dissolution de la société -->
        <div class="card text-center">
          <div class="card-header">
            Procès-verbal de dissolution de la société
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
                ... demeurant au ..., actionnaire unique de la société ..., a pris les décisions concernant l'ordre du 
                jour suivant:
                <br>
                - Dissolution anticipée de la société ... ;
                - Nomination du liquidateur de la société ... ;
                - Rémunération du liquidateur de la société ... .
            </h6>
            
            <br>
            <br>
            
            <!-- Première résolution -->
            <div class="card text-center">
              <div class="card-header">
                Première résolution
              </div>
              <div class="card-body">
                L'actionnaire unique de la société ... décide de la dissolution anticipée de la société ... et sa 
                liquidation amiable conformément aux dispositions desarticles L237-1 à 237-13 du Code de commerce.
                
                <br>
                <br>
                
                La société ... subsistera pour les besoins de la liquidation de la société ... et jusqu'à la clôture 
                de celle-ci.
                
                <br>
                <br>
                
                Durantcette période, la dénomination sociale de la société ... sera suivie de la mention "société en 
                liquidation". Cette mention ainsi que le nom du liquidateur devront figurer sur tous les documents et 
                actes destinés au tiers.
                
                <br>
                <br>
                
                Le siège social de la liquidation de la société ... est fixé au ... .
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
                L'actionnaire unique de la société ... sera désigné en qualité de liquidateur de la société ... et 
                pour une durée de deux mois.
                
                <br>
                <br>
                
                Dans les deux mois de sa nomination, le liquidateur de la société ... doit faire un rapport sur la 
                situation comptable de la société ..., sur la poursuite des opérations de liquidation de la société ...
                et sur le délai nécessaire pour les terminer.
                
                <br>
                <br>
                
                L'actionnaire unique de la société ... décide que le liquidateur de la société ... n'a pas droit, 
                en contrepartie de l'exercice de son mandat, à une rémunération.
                
                <br>
                <br>
                
                ... déclare accepter ses fonctions de liquidateur de la société ... et certifie ne pas être sous le 
                coup des interdictions prévues par les lois et règlements en vigueur.
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
                L'actionnaire unique de la société ... donneau liquidateur de la société ... les pouvoirs les plus 
                étendus pour mener à bien sa mission, c'est-à-dire réaliser l'actif, payer le passif et répartir le 
                solde, sous réserve des dispositions des articles L237-1 et suivants du Code decommerce.
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
                Tous pouvoirs sont attribués au liquidateur de la société ... pour effectuer les formalités légales 
                afférentes aux décisions adoptées ci-dessus.
                
                <br>
                <br>
                
                L'ordre du jour étant épuisé, la séance est levée.
                
                <br>
                <br>
                
                De tout ce qui précède, il a été dressé le présent procès-verbal de dissolution de la société ... 
                signé par l'actionnaire unique de la société ... .
              </div>
            </div>
            <!-- Quatrième résolution -->
            
            <br>
            <br>
            
            <!-- L'actionnaire unique de la société -->
            <div class="card text-center">
              <div class="card-header">
                L'actionnaire unique de la société ...
              </div>
              <div class="card-body">
                ..., l'actionnaire unique de la société ... .
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
                Fait à ... (...), le ../../... .
                <br>
                Lu et approuvé.
              </div>
            </div>
            <!-- Date et lieu de l'approbation -->
          </div>
        </div>
        <!-- Procès-verbal de dissolution de la société -->
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
            'footer-left': 'Société ... [SIREN : ...]',
            'header-center': 'Procès-verbal de dissolution',
        }

        pdfkit.from_string(
            body,
            "Dissolution\\dissolution_.pdf",
            options=options
        )


if __name__ == '__main__':
    unittest.main()
