import unittest


class UnitTestsDataCreationHolomorpheWebsiteSaleOfDatabaseOfMaths(unittest.TestCase):
    # ok
    def test_create__sale_of_database_of_maths_for_one_template_html(self):
        print("test_create__sale_of_database_of_maths_for_one_template_html")

        directory_name = ""

        directory = "database_\\" + directory_name

        # create urls.py
        try:
            with open(directory + '\\url.py', "w") as file:
                file.write(
                    "\t" + "path('sale_of_database_of_mathematics_about_" + directory_name + "'," + "\n" +
                    "\t" + "\t" + "views.sale_of_database_of_mathematics_about_" + directory_name + "," + "\n" +
                    "\t" + "\t" + "name='sale_of_database_of_mathematics_about_" + directory_name + "'),"
                )

                file.close()
        except Exception as e:
            print('error url : ' + str(e))

        # create views.py
        try:
            with open(directory + '\\views.py', "w") as file:
                file.write(
                    "def sale_of_database_of_mathematics_about_" + directory_name + "(request):" + "\n" +
                    "\t" + "return render(request, 'contents/sale_of_database_of_mathematics_about_"
                    + directory_name + ".html')" + "\n" + "\n"
                )

                file.close()
        except Exception as e:
            print('error views : ' + str(e))

        # create sale_of_database_of_mathematics_about_.html
        try:
            with open(directory + "\\sale_of_database_of_mathematics_about_" + directory_name + ".html", "w") as file:
                file.write(
                    "<!DOCTYPE html>" + "\n" +
                    '<html lang="en">' + "\n" +
                    "<head>" + "\n" +
                    "\t" + "<!-- Required meta tags -->" + "\n" +
                    "\t" + '<meta charset="utf-8">' + "\n" +
                    "\t" + '<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">'
                    + "\n" + "\n" +
                    "\t" + '<!-- Bootstrap CSS -->' + "\n" +
                    "\t" + '<link rel="stylesheet"' + "\n" +
                    "\t" + "\t" + 'href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css"'
                    + "\n" +
                    "\t" + "\t" + 'integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk"'
                    + "\n" +
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
                    "\t" + "\t" + "<br>" + "\n" + "\n" +
                    "\t" + "\t" + "<!-- Header -->" + "\n" +
                    "\t" + "\t" + "{% include 'index/header.html' %}" + "\n" + "\n" +
                    "\t" + "\t" + "<br>" + "\n" + "\n" +
                    "\t" + "\t" + "<!-- ad1 -->" + "\n" +
                    "\t" + "\t" + "{% include 'index/ad1.html' %}" + "\n" + "\n" +
                    "\t" + "\t" + "<br>" + "\n" + "\n"
                )

                file.write(
                    "\t" + "\t" + "<!-- Sale of database of mathematics -->" + "\n" +
                    "\t" + "\t" + '<div class="card text-center">' + "\n" +
                    "\t" + "\t" + "\t" + '<div class="card-header">' + "\n" +
                    "\t" + "\t" + "\t" + "\t" + 'Sale of database of mathematics about ' +
                    directory_name.replace('_', ' ') + "\n" +
                    "\t" + "\t" + "\t" + '</div>' + "\n" +
                    "\t" + "\t" + "\t" + '<div class="card-body">' + "\n" +
                    "\t" + "\t" + "\t" + "\t" + '<!-- Product -->' + "\n" +
                    "\t" + "\t" + "\t" + "\t" + '<div class="card">' + "\n" +
                    "\t" + "\t" + "\t" + "\t" + "\t" + '<div class="card-header">' + "\n" +
                    "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + 'Product' + "\n" +
                    "\t" + "\t" + "\t" + "\t" + "\t" + '</div>' + "\n" +
                    "\t" + "\t" + "\t" + "\t" + "\t" + '<div class="card-body">' + "\n" +
                    "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + 'The product is a JSON file with LaTeX writings about '
                                                              'mathematics.' + "\n" +
                    "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + '<br>' + "\n" +
                    "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + '<br>' + "\n" +
                    "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + 'You can see some data attributes in the image below.'
                    + "\n" +
                    "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + '<br>' + "\n" +
                    "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + '<br>' + "\n" +
                    "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + '<img src="/static/contents/static/data_attributes_'
                                                              'mathematics.png" class="img-fluid" alt="Responsive '
                                                              'image">' + "\n" +
                    "\t" + "\t" + "\t" + "\t" + "\t" + '</div>' + "\n" +
                    "\t" + "\t" + "\t" + "\t" + '</div>' + "\n" + "\n" +
                    "\t" + "\t" + "\t" + "\t" + "<br>" + "\n" + "\n" +
                    "\t" + "\t" + "\t" + "\t" + "<!-- Pricing -->" + "\n" +
                    "\t" + "\t" + "\t" + "\t" + '<div class="card">' + "\n" +
                    "\t" + "\t" + "\t" + "\t" + "\t" + '<div class="card-header">' + "\n" +
                    "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + 'Pricing' + "\n" +
                    "\t" + "\t" + "\t" + "\t" + "\t" + '</div>' + "\n" +
                    "\t" + "\t" + "\t" + "\t" + "\t" + '<div class="card-body">' + "\n" +
                    "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + 'One record costs 0.00999 euros without taxes.' + "\n" +
                    "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + '<br>' + "\n" +
                    "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + '<br>' + "\n" +
                    "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + 'Ask for one sample of ten records by sending an email at '
                                                              ' with the reference : '
                                                              'database_of_mathematics_about_' + directory_name + " !"
                    + "\n" +
                    "\t" + "\t" + "\t" + "\t" + "\t" + '</div>' + "\n" +
                    "\t" + "\t" + "\t" + "\t" + '</div>' + "\n" + "\n" +
                    "\t" + "\t" + "\t" + "\t" + "<br>" + "\n" + "\n" +
                    "\t" + "\t" + "\t" + "\t" + "<!-- Types of payment -->" + "\n" +
                    "\t" + "\t" + "\t" + "\t" + '<div class="card">' + "\n" +
                    "\t" + "\t" + "\t" + "\t" + "\t" + '<div class="card-header">' + "\n" +
                    "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + 'Types of payment' + "\n" +
                    "\t" + "\t" + "\t" + "\t" + "\t" + '</div>' + "\n" +
                    "\t" + "\t" + "\t" + "\t" + "\t" + '<div class="card-body">' + "\n" +
                    "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + '<ul class="list-group list-group-flush">' + "\n" +
                    "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + '<li class="list-group-item">Bank transfer</li>'
                    + "\n" +
                    "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + '</ul>' + "\n" +
                    "\t" + "\t" + "\t" + "\t" + "\t" + '</div>' + "\n" +
                    "\t" + "\t" + "\t" + "\t" + '</div>' + "\n" + "\n" +
                    "\t" + "\t" + "\t" + "\t" + "<br>" + "\n" + "\n" +
                    "\t" + "\t" + "\t" + "\t" + "<!-- Types of delivery -->" + "\n" +
                    "\t" + "\t" + "\t" + "\t" + '<div class="card">' + "\n" +
                    "\t" + "\t" + "\t" + "\t" + "\t" + '<div class="card-header">' + "\n" +
                    "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + 'Types of delivery' + "\n" +
                    "\t" + "\t" + "\t" + "\t" + "\t" + '</div>' + "\n" +
                    "\t" + "\t" + "\t" + "\t" + "\t" + '<div class="card-body">' + "\n" +
                    "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + '<ul class="list-group list-group-flush">' + "\n" +
                    "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + '<li class="list-group-item">File transfer '
                                                                     'service</li>' + "\n" +
                    "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + '<li class="list-group-item">Email</li>' + "\n" +
                    "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + '</ul>' + "\n" +
                    "\t" + "\t" + "\t" + "\t" + "\t" + '</div>' + "\n" +
                    "\t" + "\t" + "\t" + "\t" + '</div>' + "\n" +
                    "\t" + "\t" + "\t" + '</div>' + "\n" +
                    "\t" + "\t" + '</div>' + "\n" + "\n"
                )

                file.write(
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
        except Exception as e:
            print('error sale_of_database_of_mathematics_about_.html : ' + str(e))

        # create button for index.html
        try:
            with open(directory + "\\button.html", "w") as file:
                file.write(
                    "<!-- Sale of database of mathematics about " + directory_name.replace("_", " ") + " -->" + "\n" +
                    '<a href="../contents/sale_of_database_of_mathematics_about_' + directory_name
                    + '" class="list-group-item list-group-item-action">' + "\n" +
                    "\t" + "Sale of database of mathematics about " + directory_name.replace("_", " ") + "\n" +
                    '</a>'
                )

                file.close()
        except Exception as e:
            print('error button : ' + str(e))


if __name__ == '__main__':
    unittest.main()
