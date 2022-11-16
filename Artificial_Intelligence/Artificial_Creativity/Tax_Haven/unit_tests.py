import unittest
import xlrd
import xlsxwriter
import os
import sounddevice as sd
from scipy.io.wavfile import write
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone
from datetime import datetime


class UnitTestsDataCreationTaxHaven(unittest.TestCase):
    def test_company_tax_haven_views_files(self):
        print("test_company_tax_haven_views_files")

        location = ("Offshore_Company_v1.xls")

        workbook = xlrd.open_workbook(location)

        sheet = workbook.sheet_by_name("Compare_Companies")

        f = open("company_views.txt", "a", encoding="utf-8")

        for x in range(1, 39):
            filename = "company_" + sheet.cell_value(x, 0) \
                                        .replace(" ", "_") \
                                        .replace("/", "_") \
                                        .replace("'", "_") \
                                        .replace("?", "").lower()[:-1]

            f.write('def ')
            f.write(filename)
            f.write('(request): \n')
            f.write('\t context = { \n')
            f.write('\t \t "data": [ \n')

            for y in range(1, 46):
                f.write('\t \t \t {"company": "' + str(sheet.cell_value(0, y)) + '", "value": "' + str(sheet.cell_value(x, y)) + '", "color": "table-active"}, \n')

            f.write('\t \t ], \n')
            f.write('\t \t "topic": "' + str(sheet.cell_value(x, 0)).replace("/", " ").replace("'", " ")
                    .replace("?", "") + '", \n')
            f.write('\t \t "comparison": "Company" \n')
            f.write('\t } \n')
            f.write('\t return render(request, "taxhaven/tax_haven_topic.html", context)')
            f.write('\n \n \n')

        f.close()

    def test_trust_tax_haven_views_files(self):
        print("test_trust_tax_haven_views_files")

        location = ("Offshore_Company_v1.xls")

        workbook = xlrd.open_workbook(location)

        sheet = workbook.sheet_by_name("Compare_Trusts")

        f = open("trust_views.txt", "a", encoding="utf-8")

        for x in range(1, 14):
            filename = "trust_" + sheet.cell_value(x, 0)\
                           .replace(" ", "_") \
                           .replace("/", "_") \
                           .replace("'", "_")\
                           .replace("?", "").lower()[:-1]

            f.write('def ')
            f.write(filename)
            f.write('(request):\n')
            f.write('\t context = {\n')
            f.write('\t \t "data": [\n')

            for y in range(1, 19):
                f.write('\t \t \t {"comparison": "' + str(sheet.cell_value(0, y)) + '", "value": "' + str(sheet.cell_value(x, y)) + '", "color": "table-active"},\n')

            f.write('\t \t ],\n')
            f.write('\t \t "topic": "' + str(sheet.cell_value(x, 0)).replace("/", " ").replace("'", " ")
                    .replace("?", "") + '",\n')
            f.write('\t \t "comparison": "Trust"\n')
            f.write('\t }\n')
            f.write('\t return render(request, "taxhaven/tax_haven_topic.html", context)')
            f.write('\n \n \n')

        f.close()

    def test_company_tax_haven_path_file(self):
        print("test_company_tax_haven_path_file")

        location = ("Offshore_Company_v1.xls")

        workbook = xlrd.open_workbook(location)

        sheet = workbook.sheet_by_name("Compare_Companies")

        f = open("compare_companies_paths.txt", "a", encoding="utf-8")

        for x in range(1, 39):
            t_b = "company_" + sheet.cell_value(x, 0)\
                           .replace(" ", "_")\
                           .replace("/", "_")\
                           .replace("'", "_")\
                           .replace("?", "").lower()[:-1]

            t_m = "company-" + sheet.cell_value(x, 0)\
                            .replace(" ", "-")\
                            .replace("/", "-")\
                            .replace("'", "-")\
                            .replace("?", "").lower()[:-1]

            f.write("path('" + t_m + "', views." + t_b + ", name='" + t_b + "'), \n")

        f.close()

    def test_trust_tax_haven_path_file(self):
        print("test_trust_tax_haven_path_file")

        location = ("Offshore_Company_v1.xls")

        workbook = xlrd.open_workbook(location)

        sheet = workbook.sheet_by_name("Compare_Trusts")

        f = open("compare_trusts_paths.txt", "a", encoding="utf-8")

        for x in range(1, 14):
            t_b = "trust_" + sheet.cell_value(x, 0)\
                           .replace(" ", "_")\
                           .replace("/", "_")\
                           .replace("'", "_")\
                           .replace("?", "").lower()[:-1]

            t_m = "trust-" + sheet.cell_value(x, 0)\
                            .replace(" ", "-")\
                            .replace("/", "-")\
                            .replace("'", "-")\
                            .replace("?", "").lower()[:-1]

            f.write("path('" + t_m + "', views." + t_b + ", name='" + t_b + "'), \n")

        f.close()

    def test_company_tax_haven_index_html_file(self):
        print("test_company_tax_haven_path_file")

        location = ("Offshore_Company_v1.xls")

        workbook = xlrd.open_workbook(location)

        sheet = workbook.sheet_by_name("Compare_Companies")

        f = open("compare_companies_index_html.txt", "a", encoding="utf-8")

        for x in range(1, 39):
            title = sheet.cell_value(x, 0)\
                           .replace("/", " ")\
                           .replace("'", " ")\
                           .replace("?", " ")

            t_m = "company-" + sheet.cell_value(x, 0)\
                            .replace(" ", "-")\
                            .replace("/", "-")\
                            .replace("'", "-")\
                            .replace("?", "").lower()[:-1]

            f.write('<a href="../tax-haven/' + t_m + '" class="list-group-item list-group-item-action"> \n')
            f.write('Company / ' + title + '\n')
            f.write('</a> \n')

        f.close()

    def test_trust_tax_haven_index_html_file(self):
        print("test_trust_tax_haven_index_html_file")

        location = ("Offshore_Company_v1.xls")

        workbook = xlrd.open_workbook(location)

        sheet = workbook.sheet_by_name("Compare_Trusts")

        f = open("compare_trusts_index_html.txt", "a", encoding="utf-8")

        for x in range(1, 14):
            title = sheet.cell_value(x, 0)\
                           .replace("/", " ")\
                           .replace("'", " ")\
                           .replace("?", " ")

            t_m = "trust-" + sheet.cell_value(x, 0)\
                            .replace(" ", "-")\
                            .replace("/", "-")\
                            .replace("'", "-")\
                            .replace("?", "").lower()[:-1]

            f.write('<a href="../tax-haven/' + t_m + '" class="list-group-item list-group-item-action"> \n')
            f.write('Trust / ' + title + '\n')
            f.write('</a> \n')

        f.close()

    def test_company_tax_haven_html_files(self):
        print("test_company_tax_haven_html_files")

        location = ("Offshore_Company_v1.xls")

        workbook = xlrd.open_workbook(location)

        sheet = workbook.sheet_by_name("Compare_Companies")

        for x in range(1, 39):
            title = sheet.cell_value(x, 0)\
                           .replace("/", " ")\
                           .replace("'", " ")\
                           .replace("?", " ")

            t_b = "company_" + sheet.cell_value(x, 0)\
                            .replace(" ", "_")\
                            .replace("/", "_")\
                            .replace("'", "_")\
                            .replace("?", "").lower()[:-1]

            f = open(t_b + ".html", "a", encoding="utf-8")

            f.write('''
            <!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">

    <title>Holomorphe - Tax haven</title>
  </head>
  <body>
    <div class="container">
      <!-- Header -->
      <!-- Typography : Holomorphe -->
      <h1 class="text-center">Holomorphe</h1>
      <!-- Typography : Holomorphe -->
      <!-- Header -->

      <br>

      <!-- Body -->
      <div class="card">
        <div class="card-header text-center">
            ''')

            # title
            f.write('Company / ' + title)

            f.write('''
            </div>
        <div class="card-body">
          <table class="table table-striped text-center">
            <thead>
              <tr>
                <th scope="col">Company</th>
                <th scope="col">
            ''')

            # title
            f.write(title)

            f.write('''
            </th>
              </tr>
            </thead>
            <tbody>
              {% for i in data %}
                <tr>
                  <td class="table-active">{{ i.company }}</td>
                  <td class="table-active">{{ i.value }}</td>
                </tr>
              {% endfor %}
            </tbody>
          </table>
        </div>
      </div>
      <!-- Body -->

      <br>

      <!-- Footer -->
      <div class="card">
        <div class="card-header text-center">
          Informations générales
        </div>
        <div class="card-body">
          <div class="list-group text-center">
            <a href="../mentions-legales" class="list-group-item list-group-item-action">
              Mentions légales
            </a>
            <a href="../conditions-generales-utilisation" class="list-group-item list-group-item-action">
              Conditions générales d'utilisation
            </a>
            <!--
            <a href="../conditions-generales-de-vente" class="list-group-item list-group-item-action">
              Conditions générales de ventes
            </a>
            -->
            <!--
            <a href="../politique-de-confidentialite" class="list-group-item list-group-item-action">
              Politique de confidentialité
            </a>
            -->
            <a href="../contact" class="list-group-item list-group-item-action">
              Contact
            </a>
          </div>
        </div>
      </div>
      <!-- Footer -->

      <br>

    </div>

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js" integrity="sha384-OgVRvuATP1z7JjHLkuOU7Xw704+h835Lr+6QL9UvYjZE3Ipu6Tp75j7Bh/kR0JKI" crossorigin="anonymous"></script>
  </body>
</html>
            ''')

            f.close()

    def test_trust_tax_haven_html_files(self):
        print("test_trust_tax_haven_html_files")

        location = ("Offshore_Company_v1.xls")

        workbook = xlrd.open_workbook(location)

        sheet = workbook.sheet_by_name("Compare_Trusts")

        for x in range(1, 14):
            title = sheet.cell_value(x, 0) \
                .replace("/", " ") \
                .replace("'", " ") \
                .replace("?", " ")

            t_b = "trust_" + sheet.cell_value(x, 0) \
                                   .replace(" ", "_") \
                                   .replace("/", "_") \
                                   .replace("'", "_") \
                                   .replace("?", "").lower()[:-1]

            f = open(t_b + ".html", "a", encoding="utf-8")

            f.write('''
                        <!doctype html>
            <html lang="en">
              <head>
                <!-- Required meta tags -->
                <meta charset="utf-8">
                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

                <!-- Bootstrap CSS -->
                <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">

                <title>Holomorphe - Tax haven</title>
              </head>
              <body>
                <div class="container">
                  <!-- Header -->
                  <!-- Typography : Holomorphe -->
                  <h1 class="text-center">Holomorphe</h1>
                  <!-- Typography : Holomorphe -->
                  <!-- Header -->

                  <br>

                  <!-- Body -->
                  <div class="card">
                    <div class="card-header text-center">
                        ''')

            # title
            f.write('Trust / ' + title)

            f.write('''
                        </div>
                    <div class="card-body">
                      <table class="table table-striped text-center">
                        <thead>
                          <tr>
                            <th scope="col">Trust</th>
                            <th scope="col">
                        ''')

            # title
            f.write(title)

            f.write('''
                        </th>
                          </tr>
                        </thead>
                        <tbody>
                          {% for i in data %}
                            <tr>
                              <td class="table-active">{{ i.trust }}</td>
                              <td class="table-active">{{ i.value }}</td>
                            </tr>
                          {% endfor %}
                        </tbody>
                      </table>
                    </div>
                  </div>
                  <!-- Body -->

                  <br>

                  <!-- Footer -->
                  <div class="card">
                    <div class="card-header text-center">
                      Informations générales
                    </div>
                    <div class="card-body">
                      <div class="list-group text-center">
                        <a href="../mentions-legales" class="list-group-item list-group-item-action">
                          Mentions légales
                        </a>
                        <a href="../conditions-generales-utilisation" class="list-group-item list-group-item-action">
                          Conditions générales d'utilisation
                        </a>
                        <!--
                        <a href="../conditions-generales-de-vente" class="list-group-item list-group-item-action">
                          Conditions générales de ventes
                        </a>
                        -->
                        <!--
                        <a href="../politique-de-confidentialite" class="list-group-item list-group-item-action">
                          Politique de confidentialité
                        </a>
                        -->
                        <a href="../contact" class="list-group-item list-group-item-action">
                          Contact
                        </a>
                      </div>
                    </div>
                  </div>
                  <!-- Footer -->

                  <br>

                </div>

                <!-- Optional JavaScript -->
                <!-- jQuery first, then Popper.js, then Bootstrap JS -->
                <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
                <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
                <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js" integrity="sha384-OgVRvuATP1z7JjHLkuOU7Xw704+h835Lr+6QL9UvYjZE3Ipu6Tp75j7Bh/kR0JKI" crossorigin="anonymous"></script>
              </body>
            </html>
                        ''')

            f.close()

    def test_modify_html_files(self):
        print("test_modify_html_files")

        directory_files = os.getcwd() + "\\HTML_Files"
        new_directory = os.getcwd() + "\\HTML_Files_Modified"

        for file in os.listdir(directory_files):
            with open(directory_files + '\\' + file, 'r', encoding='utf-8') as f:
                text = str(f.read())\
                    .replace('<!-- Typography : Holomorphe -->', '')\
                    .replace('<h1 class="text-center">Holomorphe</h1>', "{% include 'index/header.html' %}")

                with open(new_directory + '\\' + file, 'w', encoding='utf-8') as f1:
                    f1.write(text)
                    f1.close()

                f.close()


if __name__ == '__main__':
    unittest.main()
