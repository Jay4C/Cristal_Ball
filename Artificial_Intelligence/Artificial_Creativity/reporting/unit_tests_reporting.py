import unittest


class UnitTestsDataCreationHolomorpheWebsiteReportingTable(unittest.TestCase):
    # ok
    def test_create__reporting_table_html(self):
        print("test_create__reporting_table_html")

        directory_name = "promotions_calendar"

        directory = "reporting\\" + directory_name

        columns = [
            "Jan",
            "Feb",
            "Mar",
            "Apr",
            "May",
            "Jun",
            "Jul",
            "Aug",
            "Sept",
            "Oct",
            "Nov",
            "Dec"
        ]

        rows = [
            "Promotion",
        ]

        number_of_columns = len(columns)

        number_of_rows = len(rows)

        print("number_of_columns : " + str(number_of_columns))

        print("number_of_rows : " + str(number_of_rows))

        # create urls.py
        with open(directory + '\\urls.py', "w") as file:
            file.write(
                "path('" + directory_name + "'," + "\n" +
                "\t" + "views." + directory_name + "," + "\n" +
                "\t" + "name='" + directory_name + "')," + "\n" +
                "path('generate_html_to_pdf_" + directory_name + "'," + "\n" +
                "\t" + "views.generate_html_to_pdf_" + directory_name + "," + "\n" +
                "\t" + "name='generate_html_to_pdf_" + directory_name + "'),"
            )

            file.close()

        # create views.py
        with open(directory + '\\views.py', "w") as file:
            file.write(
                "def " + directory_name + "(request):" + "\n" +
                "\t" + "return render(request, 'reporting/" + directory_name + ".html')" + "\n" + "\n" + "\n"
            )

            file.write(
                "def generate_html_to_pdf_" + directory_name + "(request):" + "\n" +
                "\t" + "company_name = request.POST.get('company_name').replace('\\t', ' ').replace('\\n', ' ').replace('\\r', ' ')" + "\n" +
                "\t" + "share_capital = request.POST.get('share_capital').replace('\\t', ' ').replace('\\n', ' ').replace('\\r', ' ')" + "\n" +
                "\t" + "head_office_address = request.POST.get('head_office_address').replace('\\t', ' ').replace('\\n', ' ').replace('\\r', ' ')" + "\n" +
                "\t" + "establishment_number = request.POST.get('establishment_number').replace('\\t', ' ').replace('\\n', ' ').replace('\\r', ' ')" + "\n" +
                "\t" + "register_of_trade_and_companies = request.POST.get('register_of_trade_and_companies').replace('\\t', ' ').replace('\\n', ' ').replace('\\r', ' ')" + "\n" +
                "\t" + "main_activities = request.POST.get('main_activities').replace('\\t', ' ').replace('\\n', ' ').replace('\\r', ' ')" + "\n" +
                "\t" + "activity_number = request.POST.get('activity_number').replace('\\t', ' ').replace('\\n', ' ').replace('\\r', ' ')" + "\n" +
                "\t" + "intra_community_vat_number = request.POST.get('intra_community_vat_number').replace('\\t', ' ').replace('\\n', ' ').replace('\\r', ' ')" + "\n" +
                "\t" + "president = request.POST.get('president').replace('\\t', ' ').replace('\\n', ' ').replace('\\r', ' ')" + "\n" +
                "\t" + "registration_date = request.POST.get('registration_date').replace('\\t', ' ').replace('\\n', ' ').replace('\\r', ' ')" + "\n"
            )

            for r in range(1, number_of_rows + 1):
                for c in range(1, number_of_columns + 1):
                    file.write(
                        "\t" + 'r' + str(r) + 'c' + str(c) + " = request.POST.get('" + 'r' + str(r) + 'c' + str(
                            c) + "').replace('\\t', ' ').replace('\\n', ' ').replace('\\r', ' ')" + "\n"
                    )

            file.write(
                "\n" +
                "\t" + "body = '<!doctype html>' + \\" + "\n" +
                "\t" + "\t" + "\t" + "'<html lang=" + '"' + "en" + '"' + ">' + \\" + "\n" +
                "\t" + "\t" + "\t" + "'<head>' + \\" + "\n" +
                "\t" + "\t" + "\t" + "'<meta charset=" + '"' + "utf-8" + '"' + ">' + \\" + "\n" +
                "\t" + "\t" + "\t" + "'<meta name=" + '"' + "viewport" + '" ' + "content=" + '"' + "width=device-width, initial-scale=1, shrink-to-fit=no" + '"' + ">' + \\" + "\n" +
                "\t" + "\t" + "\t" + "'<link rel=" + '"' + "stylesheet" + '"' + "' + \\" + "\n" +
                "\t" + "\t" + "\t" + "'href=" + '"' + "https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css" + '"' + "' + \\" + "\n" +
                "\t" + "\t" + "\t" + "'integrity=" + '"' + "sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" + '"' + "' + \\" + "\n" +
                "\t" + "\t" + "\t" + "'crossorigin=" + '"' + "anonymous" + '"' + ">' + \\" + "\n" +
                "\t" + "\t" + "\t" + "'<title>" + directory_name[0].upper() + directory_name[1:].replace("_",
                                                                                                         " ") + "</title>' + \\" + "\n" +
                "\t" + "\t" + "\t" + "'</head>' + \\" + "\n" +
                "\t" + "\t" + "\t" + "'<body>' + \\" + "\n" +
                "\t" + "\t" + "\t" + "'<div class=" + '"' + "container" + '"' + ">' + \\" + "\n" +
                "\t" + "\t" + "\t" + "'<div class=" + '"' + "card text-center" + '"' + ">' + \\" + "\n" +
                "\t" + "\t" + "\t" + "'<div class=" + '"' + "card-header text-center" + '"' + ">" + directory_name[
                    0].upper() + directory_name[1:].replace("_", " ") + "</div>' + \\" + "\n" +
                "\t" + "\t" + "\t" + "'<div class=" + '"' + "card-body" + '"' + ">'" + "\n" + "\n"
            )

            file.write(
                "\t" + "body += '<h6>Comapny name : ' + company_name + '</h6>' + \\" + "\n" +
                "\t" + "\t" + "\t" + "'<h6>Share capital : ' + share_capital + '</h6>' + \\" + "\n" +
                "\t" + "\t" + "\t" + "'<h6>Head office address : ' + head_office_address + '</h6>' + \\" + "\n" +
                "\t" + "\t" + "\t" + "'<h6>Establishment number : ' + establishment_number + '</h6>' + \\" + "\n" +
                "\t" + "\t" + "\t" + "'<h6>Register of Trade and Companies : ' + register_of_trade_and_companies + '</h6>' + \\" + "\n" +
                "\t" + "\t" + "\t" + "'<h6>Main activities : ' + main_activities + '</h6>' + \\" + "\n" +
                "\t" + "\t" + "\t" + "'<h6>Activity number : ' + activity_number + '</h6>' + \\" + "\n" +
                "\t" + "\t" + "\t" + "'<h6>Intra-community VAT number : ' + intra_community_vat_number + '</h6>' + \\" + "\n" +
                "\t" + "\t" + "\t" + "'<h6>President : ' + president + '</h6>' + \\" + "\n" +
                "\t" + "\t" + "\t" + "'<h6>Registration date : ' + registration_date + '</h6>' + \\" + "\n" +
                "\t" + "\t" + "\t" + "'<br>'" + "\n" + "\n"
            )

            file.write(
                "\t" + "body += '<br>'" + "\n" + "\n"
            )

            file.write(
                "\t" + "body += '<table class=" + '"' + "table table-striped table-bordered" + '"' + ">'" + " + \\" + "\n" +
                "\t" + "\t" + "\t" + "'<thead>'" + " + \\" + "\n" +
                "\t" + "\t" + "\t" + "'<tr>'" + " + \\" + "\n" +
                "\t" + "\t" + "\t" + "'<th scope=" + '"' + "col" + '"' + ">Details</th>'" + " + \\" + "\n"
            )

            for column in columns:
                file.write(
                    "\t" + "\t" + "\t" + "'<th scope=" + '"' + "col" + '"' + ">" + column + "</th>'" + " + \\" + "\n"
                )

            file.write(
                "\t" + "\t" + "\t" + "'</tr>'" + " + \\" + "\n" +
                "\t" + "\t" + "\t" + "'</thead>'" + " + \\" + "\n" +
                "\t" + "\t" + "\t" + "'<tbody>'" + " + \\" + "\n"
            )

            for r in range(1, number_of_rows + 1):
                file.write(
                    "\t" + "\t" + "\t" + "'<tr>'" + " + \\" + "\n" +
                    "\t" + "\t" + "\t" + "'<td>" + rows[r - 1] + "</td>'" + " + \\" + "\n"
                )

                for c in range(1, number_of_columns + 1):
                    file.write(
                        "\t" + "\t" + "\t" + "'<td>'" + " + " + 'r' + str(r) + 'c' + str(
                            c) + " + " + "'</td>'" + " + \\" + "\n"
                    )

                file.write(
                    "\t" + "\t" + "\t" + "'</tr>'" + " + \\" + "\n"
                )

            file.write(
                "\t" + "\t" + "\t" + "'</tbody>'" + " + \\" + "\n" +
                "\t" + "\t" + "\t" + "'</table>'" + "\n" + "\n"
            )

            file.write(
                "\t" + "body += '<br>' + \\" + "\n" +
                "\t" + "\t" + "\t" + "'</div>' + \\" + "\n" +
                "\t" + "\t" + "\t" + "'</div>' + \\" + "\n" +
                "\t" + "\t" + "\t" + "'</div>' + \\" + "\n" +
                "\t" + "\t" + "\t" + "'<br>' + \\" + "\n" +
                "\t" + "\t" + "\t" + "'<script src=" + '"' + "https://code.jquery.com/jquery-3.5.1.slim.min.js" + '"' + "' + \\" + "\n" +
                "\t" + "\t" + "\t" + "'integrity=" + '"' + "sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" + '"' + "' + \\" + "\n" +
                "\t" + "\t" + "\t" + "'crossorigin=" + '"' + "anonymous" + '"' + "></script>" + "' + \\" + "\n" +
                "\t" + "\t" + "\t" + "'<script src=" + '"' + "https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/js/bootstrap.bundle.min.js" + '"' + "' + \\" + "\n" +
                "\t" + "\t" + "\t" + "'integrity=" + '"' + "sha384-ho+j7jyWK8fNQe+A12Hb8AhRq26LrZ/JpcUGGOn+Y7RsweNrtN/tE3MoK7ZeZDyx" + '"' + "' + \\" + "\n" +
                "\t" + "\t" + "\t" + "'crossorigin=" + '"' + "anonymous" + '"' + "></script>" + "' + \\" + "\n" +
                "\t" + "\t" + "\t" + "'</body>" + "' + \\" + "\n" +
                "\t" + "\t" + "\t" + "'</html>'" + "\n" + "\n" +
                "\t" + "options = {" + "\n" +
                "\t" + "\t" + "'page-size': 'A4'," + "\n" +
                "\t" + "\t" + "'header-center': '" + directory_name[0].upper() + directory_name[1:].replace("_",
                                                                                                            " ") + "'," + "\n" +
                "\t" + "\t" + "'footer-left': 'Company : ' + company_name + ' [' + establishment_number + ']'," + "\n" +
                "\t" + "\t" + "'footer-right': '[page] sur [topage]'," + "\n" +
                "\t" + "\t" + "'encoding': 'UTF-8'," + "\n" +
                "\t" + "\t" + "'no-outline': None," + "\n" +
                "\t" + "\t" + "'custom-header': [" + "\n" +
                "\t" + "\t" + "\t" + "('Accept-Encoding', 'pdf')" + "\n" +
                "\t" + "\t" + "]" + "\n" +
                "\t" + "}" + "\n" + "\n" +
                "\t" + "# path_wkthmltopdf = 'static/reporting/static/wkhtmltopdf.exe'" + "\n" +
                "\t" + "# config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)" + "\n" +
                "\t" + "# output = pdfkit.from_string(body, output_path=False, configuration=config, options=options)" + "\n" + "\n" +
                "\t" + "output = pdfkit.from_string(body, output_path=False, options=options)" + "\n" + "\n" +
                "\t" + "response = HttpResponse(output, content_type='application/pdf')" + "\n" +
                "\t" + "response['Content-Disposition'] = 'attachment; filename=" + '"' + directory_name + ".pdf" + '"' + "'" + "\n" + "\n" +
                "\t" + "return response" + "\n"
            )

            file.close()

        # create reporting.html
        with open(directory + "\\" + directory_name + ".html", "w") as file:
            file.write(
                "<!DOCTYPE html>" + "\n" +
                '<html lang="en">' + "\n" +
                "<head>" + "\n" +
                "\t" + "<!-- Required meta tags -->" + "\n" +
                "\t" + '<meta charset="utf-8">' + "\n" +
                "\t" + '<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">' + "\n" + "\n" +
                "\t" + '<!-- Bootstrap CSS -->' + "\n" +
                "\t" + '<link rel="stylesheet"' + "\n" +
                "\t" + "\t" + 'href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css"' + "\n" +
                "\t" + "\t" + 'integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk"' + "\n" +
                "\t" + "\t" + 'crossorigin="anonymous">' + "\n" + "\n" +
                "\t" + '<!-- Code Ad -->' + "\n" +
                "\t" + "{% include 'index/codeAd.html' %}" + "\n" + "\n" +
                "\t" + "<!-- title -->" + "\n" +
                "\t" + "{% include 'index/title.html' %}" + "\n" +
                "</head>" + "\n" +
                "<body>" + "\n" +
                "\t" + '<div class="container">' + "\n" +
                "\t" + "\t" + '<!-- Code consent -->' + "\n" +
                "\t" + "\t" + "{% include 'index/consent.html' %}" + "\n" + "\n" +
                "\t" + "\t" + "<!-- Header -->" + "\n" +
                "\t" + "\t" + "{% include 'index/header.html' %}" + "\n" + "\n" +
                "\t" + "\t" + "<br>" + "\n" + "\n" +
                "\t" + "\t" + "<!-- ad1 -->" + "\n" +
                "\t" + "\t" + "{% include 'index/ad1.html' %}" + "\n" + "\n" +
                "\t" + "\t" + "<br>" + "\n" + "\n" +
                "\t" + "\t" + "<!-- Body -->" + "\n" + "\n" +
                "\t" + "\t" + "<!-- " + directory_name.replace('_', ' ')[0].upper() + directory_name.replace('_', ' ')[
                                                                                      1:] + " -->" + "\n" +
                "\t" + "\t" + '<div class="card text-center">' + "\n" +
                "\t" + "\t" + "\t" + '<div class="card-header">' + "\n" +
                "\t" + "\t" + "\t" + "\t" + '<h6>Reporting - ' + directory_name.replace('_', ' ')[
                    0].upper() + directory_name.replace('_', ' ')[1:] + '</h6>' + "\n" +
                "\t" + "\t" + "\t" + "\t" + '<br>' + "\n" +
                "\t" + "\t" + "\t" + "\t" + '<a class="btn btn-outline-secondary"' + "\n" +
                "\t" + "\t" + "\t" + "\t" + "\t" + 'href="https://github.com/Jay4C/Web-Automation/blob/master/Holomorphe_Website/unit_tests.py"' + "\n" +
                "\t" + "\t" + "\t" + "\t" + "\t" + 'role="button"' + "\n" +
                "\t" + "\t" + "\t" + "\t" + "\t" + 'target="_blank">Download this robot to fill this form by web automation</a>' + "\n" +
                "\t" + "\t" + "\t" + '</div>' + "\n" +
                "\t" + "\t" + "\t" + '<div class="card-body">' + "\n" +
                "\t" + "\t" + "\t" + "\t" + '<form action="{% url ' + "'generate_html_to_pdf_" + directory_name + "'" + ' %}" method="post">' + "\n" +
                "\t" + "\t" + "\t" + "\t" + "\t" + '{% csrf_token %}' + "\n" +
                "\t" + "\t" + "\t" + "\t" + "\t" + '<div class="card">' + "\n" +
                "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + '<div class="card-header">' + "\n" +
                "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + 'Company' + "\n" +
                "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + '</div>' + "\n" +
                "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + '<div class="card-body">' + "\n" +
                "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + '<div class="form-group row">' + "\n" +
                "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + '<label class="col-sm col-form-label">' + "\n" +
                "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + 'Company name :' + "\n" +
                "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + '</label>' + "\n" +
                "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + '<div class="col-sm">' + "\n" +
                "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + '<input type="text" class="form-control" name="company_name">' + "\n" +
                "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + '</div>' + "\n" +
                "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + '</div>' + "\n" +
                "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + '<div class="form-group row">' + "\n" +
                "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + '<label class="col-sm col-form-label">' + "\n" +
                "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + 'Share capital :' + "\n" +
                "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + '</label>' + "\n" +
                "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + '<div class="col-sm">' + "\n" +
                "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + '<input type="text" class="form-control" name="share_capital">' + "\n" +
                "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + '</div>' + "\n" +
                "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + '</div>' + "\n" +
                "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + '<div class="form-group row">' + "\n" +
                "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + '<label class="col-sm col-form-label">' + "\n" +
                "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + 'Head office address :' + "\n" +
                "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + '</label>' + "\n" +
                "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + '<div class="col-sm">' + "\n" +
                "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + '<input type="text" class="form-control" name="head_office_address">' + "\n" +
                "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + '</div>' + "\n" +
                "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + '</div>' + "\n" +
                "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + '<div class="form-group row">' + "\n" +
                "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + '<label class="col-sm col-form-label">' + "\n" +
                "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + 'Establishment number :' + "\n" +
                "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + '</label>' + "\n" +
                "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + '<div class="col-sm">' + "\n" +
                "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + '<input type="text" class="form-control" name="establishment_number">' + "\n" +
                "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + '</div>' + "\n" +
                "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + '</div>' + "\n" +
                "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + '<div class="form-group row">' + "\n" +
                "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + '<label class="col-sm col-form-label">' + "\n" +
                "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + 'Register of Trade and Companies :' + "\n" +
                "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + '</label>' + "\n" +
                "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + '<div class="col-sm">' + "\n" +
                "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + '<input type="text" class="form-control" name="register_of_trade_and_companies">' + "\n" +
                "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + '</div>' + "\n" +
                "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + '</div>' + "\n" +
                "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + '<div class="form-group row">' + "\n" +
                "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + '<label class="col-sm col-form-label">' + "\n" +
                "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + 'Main activities :' + "\n" +
                "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + '</label>' + "\n" +
                "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + '<div class="col-sm">' + "\n" +
                "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + '<input type="text" class="form-control" name="main_activities">' + "\n" +
                "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + '</div>' + "\n" +
                "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + '</div>' + "\n" +
                "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + '<div class="form-group row">' + "\n" +
                "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + '<label class="col-sm col-form-label">' + "\n" +
                "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + 'Activity number :' + "\n" +
                "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + '</label>' + "\n" +
                "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + '<div class="col-sm">' + "\n" +
                "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + '<input type="text" class="form-control" name="activity_number">' + "\n" +
                "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + '</div>' + "\n" +
                "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + '</div>' + "\n" +
                "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + '<div class="form-group row">' + "\n" +
                "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + '<label class="col-sm col-form-label">' + "\n" +
                "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + 'Intra-community VAT number :' + "\n" +
                "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + '</label>' + "\n" +
                "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + '<div class="col-sm">' + "\n" +
                "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + '<input type="text" class="form-control" name="intra_community_vat_number">' + "\n" +
                "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + '</div>' + "\n" +
                "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + '</div>' + "\n" +
                "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + '<div class="form-group row">' + "\n" +
                "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + '<label class="col-sm col-form-label">' + "\n" +
                "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + 'President :' + "\n" +
                "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + '</label>' + "\n" +
                "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + '<div class="col-sm">' + "\n" +
                "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + '<input type="text" class="form-control" name="president">' + "\n" +
                "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + '</div>' + "\n" +
                "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + '</div>' + "\n" +
                "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + '<div class="form-group row">' + "\n" +
                "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + '<label class="col-sm col-form-label">' + "\n" +
                "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + 'Registration date :' + "\n" +
                "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + '</label>' + "\n" +
                "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + '<div class="col-sm">' + "\n" +
                "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + '<input type="text" class="form-control" name="registration_date">' + "\n" +
                "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + '</div>' + "\n" +
                "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + '</div>' + "\n" +
                "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + '</div>' + "\n" +
                "\t" + "\t" + "\t" + "\t" + "\t" + '</div>' + "\n" + "\n" +
                "\t" + "\t" + "\t" + "\t" + "\t" + '<br>' + "\n" + "\n" +
                "\t" + "\t" + "\t" + "\t" + "\t" + "<!-- ad1 -->" + "\n" +
                "\t" + "\t" + "\t" + "\t" + "\t" + "{% include 'index/ad1.html' %}" + "\n" + "\n" +
                "\t" + "\t" + "\t" + "\t" + "\t" + '<br>' + "\n" + "\n"
            )

            file.write(
                "\t" + "\t" + "\t" + "\t" + "\t" + '<table class="table table-striped table-bordered">' + "\n" +
                "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + '<thead>' + "\n" +
                "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + '<tr>' + "\n"
                                                                          "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + '<th scope="col">Details</th>' + "\n"
            )

            for column in columns:
                file.write(
                    "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + '<th scope="col">' + "\n" +
                    "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + column + "\n" +
                    "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + '</th>' + "\n"
                )

            file.write(
                "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + '</tr>' + "\n" +
                "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + '</thead>' + "\n" +
                "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + '<tbody>' + "\n"
            )

            for r in range(1, number_of_rows + 1):
                file.write(
                    "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + '<tr>' + "\n" +
                    "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + '<td>' + "\n" +
                    "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + rows[r - 1] + "\n" +
                    "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + '</td>' + "\n"
                )

                for c in range(1, number_of_columns + 1):
                    file.write(
                        "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + '<td>' + "\n" +
                        "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + '<div class="form-group">' + "\n" +
                        "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + '<input type="text" class="form-control" name="' + 'r' + str(
                            r) + 'c' + str(c) + '">' + "\n" +
                        "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + '</div>' + "\n" +
                        "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + '</td>' + "\n"
                    )

                file.write(
                    "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + '</tr>' + "\n"
                )

            file.write(
                "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + '</tbody>' + "\n" +
                "\t" + "\t" + "\t" + "\t" + "\t" + '</table>' + "\n" + "\n"
            )

            file.write(
                "\t" + "\t" + "\t" + "\t" + "\t" + '<br>' + "\n" + "\n" +
                "\t" + "\t" + "\t" + "\t" + "\t" + "<!-- ad1 -->" + "\n" +
                "\t" + "\t" + "\t" + "\t" + "\t" + "{% include 'index/ad1.html' %}" + "\n" + "\n" +
                "\t" + "\t" + "\t" + "\t" + "\t" + '<br>' + "\n" + "\n"
            )

            file.write(
                "\t" + "\t" + "\t" + "\t" + "\t" + '<div class="row">' + "\n" +
                "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + '<div class="col-sm">' + "\n" +
                "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + '</div>' + "\n" +
                "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + '<div class="col-sm">' + "\n" +
                "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + '<button type="submit"' + "\n" +
                "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + 'class="btn btn-secondary"' + "\n" +
                "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + 'name="button_generate_html_to_pdf_' + directory_name + '">Submit</button>' + "\n" +
                "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + '</div>' + "\n" +
                "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + '<div class="col-sm">' + "\n" +
                "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + '</div>' + "\n" +
                "\t" + "\t" + "\t" + "\t" + "\t" + '</div>' + "\n" +
                "\t" + "\t" + "\t" + "\t" + '</form>' + "\n" +
                "\t" + "\t" + "\t" + '</div>' + "\n" +
                "\t" + "\t" + '</div>' + "\n" + "\n" +
                "\t" + "\t" + '<br>' + "\n" + "\n" +
                "\t" + "\t" + '<!-- ad1 -->' + "\n" +
                "\t" + "\t" + "{% include 'index/ad1.html' %}" + "\n" + "\n" +
                "\t" + "\t" + '<br>' + "\n" + "\n" +
                "\t" + "\t" + '<!-- Footer -->' + "\n" +
                "\t" + "\t" + "{% include 'index/footer.html' %}" + "\n" + "\n" +
                "\t" + "\t" + '<br>' + "\n" +
                "\t" + '</div>' + "\n" + "\n" +
                "\t" + '<!-- Optional JavaScript -->' + "\n" +
                "\t" + '<!-- jQuery first, then Popper.js, then Bootstrap JS -->' + "\n" +
                "\t" + '<script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"' + "\n" +
                "\t" + "\t" + 'integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj"' + "\n" +
                "\t" + "\t" + 'crossorigin="anonymous"></script>' + "\n" +
                "\t" + '<script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js"' + "\n" +
                "\t" + "\t" + 'integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo"' + "\n" +
                "\t" + "\t" + 'crossorigin="anonymous"></script>' + "\n" +
                "\t" + '<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js"' + "\n" +
                "\t" + "\t" + 'integrity="sha384-OgVRvuATP1z7JjHLkuOU7Xw704+h835Lr+6QL9UvYjZE3Ipu6Tp75j7Bh/kR0JKI"' + "\n" +
                "\t" + "\t" + 'crossorigin="anonymous"></script>' + "\n" + "\n" +
                "\t" + '<!-- blockadblock -->' + "\n" +
                "\t" + "{% include 'index/blockadblock.html' %}" + "\n" +
                "</body>" + "\n" +
                "</html>"
            )

            file.close()

        # create web automation business plan reporting
        with open(directory + "\\web_automation.py", "w") as file:
            file.write(
                'def test_generate_html_to_pdf_' + directory_name + '(self):' + "\n" +
                "\t" + 'print("test_generate_html_to_pdf_' + directory_name + '")' + "\n" + "\n" +
                "\t" + 'time.sleep(1)' + "\n" + "\n" +
                "\t" + 'warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)' + "\n" + "\n" +
                "\t" + 'time.sleep(1)' + "\n" + "\n" +
                "\t" + '# with Firefox' + "\n" +
                "\t" + "browser = webdriver.Firefox(executable_path='geckodriver.exe')" + "\n" + "\n" +
                "\t" + 'time.sleep(1)' + "\n" + "\n" +
                "\t" + '# maximize window' + "\n" +
                "\t" + 'browser.maximize_window()' + "\n" + "\n" +
                "\t" + 'time.sleep(1)' + "\n" + "\n" +
                "\t" + '# open the report' + "\n" +
                "\t" + "browser.get('https://holomorphe.com/reporting/" + directory_name + "')" + "\n" + "\n" +
                "\t" + 'time.sleep(5)' + "\n" + "\n" +
                "\t" + '# fill company name' + "\n" +
                "\t" + 'company_name = browser.find_element_by_name("company_name")' + "\n" +
                "\t" + 'company_name.clear()' + "\n" +
                "\t" + 'company_name.send_keys("company_name")' + "\n" + "\n" +
                "\t" + 'time.sleep(1)' + "\n" + "\n" +
                "\t" + '# fill share_capital' + "\n" +
                "\t" + 'share_capital = browser.find_element_by_name("share_capital")' + "\n" +
                "\t" + 'share_capital.clear()' + "\n" +
                "\t" + 'share_capital.send_keys("share_capital")' + "\n" +
                "\t" + 'time.sleep(1)' + "\n" + "\n" +
                "\t" + '# fill head_office_address' + "\n" +
                "\t" + 'head_office_address = browser.find_element_by_name("head_office_address")' + "\n" +
                "\t" + 'head_office_address.clear()' + "\n" +
                "\t" + 'head_office_address.send_keys("head_office_address")' + "\n" + "\n" +
                "\t" + 'time.sleep(1)' + "\n" + "\n" +
                "\t" + '# fill establishment_number' + "\n" +
                "\t" + 'establishment_number = browser.find_element_by_name("establishment_number")' + "\n" +
                "\t" + 'establishment_number.clear()' + "\n" +
                "\t" + 'establishment_number.send_keys("establishment_number")' + "\n" + "\n" +
                "\t" + 'time.sleep(1)' + "\n" + "\n" +
                "\t" + '# fill register_of_trade_and_companies' + "\n" +
                "\t" + 'register_of_trade_and_companies = browser.find_element_by_name("register_of_trade_and_companies")' + "\n" +
                "\t" + 'register_of_trade_and_companies.clear()' + "\n" +
                "\t" + 'register_of_trade_and_companies.send_keys("register_of_trade_and_companies")' + "\n" +
                "\t" + 'time.sleep(1)' + "\n" + "\n" +
                "\t" + '# fill main_activities' + "\n" +
                "\t" + 'main_activities = browser.find_element_by_name("main_activities")' + "\n" +
                "\t" + 'main_activities.clear()' + "\n" +
                "\t" + 'main_activities.send_keys("main_activities")' + "\n" +
                "\t" + 'time.sleep(1)' + "\n" + "\n" +
                "\t" + '# fill activity_number' + "\n" +
                "\t" + 'activity_number = browser.find_element_by_name("activity_number")' + "\n" +
                "\t" + 'activity_number.clear()' + "\n" +
                "\t" + 'activity_number.send_keys("activity_number")' + "\n" + "\n" +
                "\t" + 'time.sleep(1)' + "\n" + "\n" +
                "\t" + '# fill intra_community_vat_number' + "\n" +
                "\t" + 'intra_community_vat_number = browser.find_element_by_name("intra_community_vat_number")' + "\n" +
                "\t" + 'intra_community_vat_number.clear()' + "\n" +
                "\t" + 'intra_community_vat_number.send_keys("intra_community_vat_number")' + "\n" +
                "\t" + 'time.sleep(1)' + "\n" + "\n" +
                "\t" + '# fill president' + "\n" +
                "\t" + 'president = browser.find_element_by_name("president")' + "\n" +
                "\t" + 'president.clear()' + "\n" +
                "\t" + 'president.send_keys("president")' + "\n" +
                "\t" + 'time.sleep(1)' + "\n" + "\n" +
                "\t" + '# fill registration_date' + "\n" +
                "\t" + 'registration_date = browser.find_element_by_name("registration_date")' + "\n" +
                "\t" + 'registration_date.clear()' + "\n" +
                "\t" + 'registration_date.send_keys("registration_date")' + "\n" +
                "\t" + 'time.sleep(1)' + "\n" + "\n"
            )

            for r in range(1, number_of_rows + 1):
                for c in range(1, number_of_columns + 1):
                    file.write(
                        "\t" + '# fill ' + 'r' + str(r) + 'c' + str(c) + "\n" +
                        "\t" + 'r' + str(r) + 'c' + str(c) + ' = browser.find_element_by_name("' + 'r' + str(
                            r) + 'c' + str(c) + '")' + "\n" +
                        "\t" + 'r' + str(r) + 'c' + str(c) + '.clear()' + "\n" +
                        "\t" + 'r' + str(r) + 'c' + str(c) + '.send_keys("' + 'r' + str(r) + 'c' + str(
                            c) + '")' + "\n" + "\n"
                    )

            file.write(
                "\t" + '# submit' + "\n" +
                "\t" + 'submit = browser.find_element_by_name("button_generate_html_to_pdf_' + directory_name + '")' + "\n" +
                "\t" + 'submit.click()' + "\n" + "\n" +
                "\t" + 'time.sleep(5)' + "\n" + "\n" +
                "\t" + 'browser.quit()' + "\n"
            )

            file.close()

        # create button for index.html
        with open(directory + "\\button.html", "w") as file:
            file.write(
                "<!-- " + directory_name[0].upper() + directory_name[1:].replace("_", " ") + " -->" + "\n" +
                '<a href="../reporting/' + directory_name + '" class="list-group-item list-group-item-action">' + "\n" +
                "\t" + "Reporting - " + directory_name[0].upper() + directory_name[1:].replace("_", " ") + "\n" +
                '</a>'
            )

            file.close()


if __name__ == '__main__':
    unittest.main()
