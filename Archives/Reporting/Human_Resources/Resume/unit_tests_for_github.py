import unittest
import pdfkit


class UnitTestsReportingHumanResourcesResumeForGitHub(unittest.TestCase):
    # ok
    def test_resume(self):
        print('test_resume')

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

    <title>Resume</title>
  </head>
  <body>
    <!-- Container -->
    <div class="container">
        <!-- Développeur Python -->
        <div class="card text-center">
          <div class="card-header">
            Développeur Python
          </div>
          <div class="card-body">
            <table class="table table-bordered table-striped">
              <thead>
                <tr>
                  <th scope="col">Identité</th>
                  <th scope="col">Adresse postale</th>
                  <th scope="col">Téléphone</th>
                  <th scope="col">Email</th>
                  <th scope="col">Age</th>
                  <th scope="col">Nationalité</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>...</td>
                  <td>...</td>
                  <td>...</td>
                  <td>...</td>
                  <td>...</td>
                  <td>...</td>
                </tr>
              </tbody>
            </table>
            
            <br>
            <br>
            
            <!-- Compétences -->
            <div class="card text-center">
              <div class="card-header">
                Compétences
              </div>
              <div class="card-body">
                <table class="table table-bordered table-striped">
                  <thead>
                    <tr>
                      <th scope="col">Front-end</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td>
                        <ul>
                            <li></li>
                            <li></li>
                            <li></li>
                        </ul>
                      </td>
                    </tr>
                  </tbody>
                </table>
                
                <br>
                <br>
                
                <table class="table table-bordered table-striped">
                  <thead>
                    <tr>
                      <th scope="col">Back-end</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td>
                        <ul>
                            <li></li>
                            <li></li>
                            <li></li>
                        </ul>
                      </td>
                    </tr>
                  </tbody>
                </table>
                
                <br>
                <br>
                
                <table class="table table-bordered table-striped">
                  <thead>
                    <tr>
                      <th scope="col">Management</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td>
                        <ul>
                            <li></li>
                            <li></li>
                            <li></li>
                        </ul>
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
            <!-- Compétences -->
            
            <br>
            <br>
          
            <!-- Expériences -->
            <div class="card text-center">
              <div class="card-header">
                Expériences
              </div>
              <div class="card-body">
                <table class="table table-bordered table-striped">
                  <thead>
                    <tr>
                      <th>
                        Intitulé : ...
                        <br>
                        Période : ...
                        <br>
                        Statut professionnel : ..
                        <br>
                        Société : ...
                      </th>
                    </tr>
                  </thead>
                  <tbody>
                    <tbody>
                    <tr>
                      <td>
                        <ul>
                            <li></li>
                            <li></li>
                            <li></li>
                        </ul>
                      </td>
                    </tr>
                  </tbody>
                </table>
                
                <br>
                <br>
                
                <table class="table table-bordered table-striped">
                  <thead>
                    <tr>
                      <th>
                        Intitulé : ...
                        <br>
                        Période : ...
                        <br>
                        Statut professionnel : ..
                        <br>
                        Société : ...
                      </th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td>
                        <ul>
                            <li></li>
                            <li></li>
                            <li></li>
                        </ul>
                      </td>
                    </tr>
                  </tbody>
                </table>
                
                <br>
                <br>
                
                <table class="table table-bordered table-striped">
                  <thead>
                    <tr>
                      <th>
                        Intitulé : ...
                        <br>
                        Période : ...
                        <br>
                        Statut professionnel : ..
                        <br>
                        Société : ...
                      </th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td>
                        <ul>
                            <li></li>
                            <li></li>
                            <li></li>
                        </ul>
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
            <!-- Expériences -->
            
            <br>
            <br>
            
            <!-- Formations -->
            <div class="card text-center">
              <div class="card-header">
                Formations
              </div>
              <div class="card-body">
                <table class="table table-bordered table-striped">
                  <thead>
                    <tr>
                      <th>
                        Intitulé : ...
                        <br>
                        Période : ...
                        <br>
                        Centre de formation : ...
                      </th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td>
                        <ul>
                            <li></li>
                            <li></li>
                            <li></li>
                        </ul>
                      </td>
                    </tr>
                  </tbody>
                </table>
                
                <br>
                <br>
                
                <table class="table table-bordered table-striped">
                  <thead>
                    <tr>
                      <th>
                        Intitulé : ...
                        <br>
                        Période : ...
                        <br>
                        Centre de formation : ...
                      </th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td>
                        <ul>
                            <li></li>
                            <li></li>
                            <li></li>
                        </ul>
                      </td>
                    </tr>
                  </tbody>
                </table>
                
                <br>
                <br>
                
                <table class="table table-bordered table-striped">
                  <thead>
                    <tr>
                      <th>
                        Intitulé : ...
                        <br>
                        Période : ...
                        <br>
                        Centre de formation : ...
                      </th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td>
                        <ul>
                            <li></li>
                            <li></li>
                            <li></li>
                        </ul>
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
            <!-- Formations -->
            
            <br>
            
        </div>
        <!-- Développeur Python -->
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
            'footer-left': 'Développeur Python',
            'header-center': 'CV de ....',
        }

        pdfkit.from_string(
            body,
            "Resume\\resume.pdf",
            options=options
        )


if __name__ == '__main__':
    unittest.main()
