# coding: utf8
import unittest
import time
from bs4 import BeautifulSoup
import requests
from PIL import Image, ImageDraw


class UnitTestsTextToImages(unittest.TestCase):
    def test_create_one_image_from_text(self):
        img = Image.new('RGB', (700, 300), color=(255, 255, 255))

        text = '''
La loi répute pareillement actes de commerce :

1° Toute entreprise de construction, et tous achats, ventes et reventes de bâtiments pour la navigation intérieure et extérieure ;

2° Toutes expéditions maritimes ;

3° Tout achat et vente d'agrès, apparaux et avitaillements ;

4° Tout affrètement ou nolisement, emprunt ou prêt à la grosse ;

5° Toutes assurances et autres contrats concernant le commerce de mer ;

6° Tous accords et conventions pour salaires et loyers d'équipages ;

7° Tous engagements de gens de mer pour le service de bâtiments de commerce.
        '''

        number_of_caracters_of_text = len(text.replace('\t', ' ').replace('\n', ' '))
        number_of_caracters_per_line = 110
        number_of_lines = int(number_of_caracters_of_text / number_of_caracters_per_line)

        d = ImageDraw.Draw(img)

        for i in range(0, number_of_lines + 1):
            coordinate_y = 25 * i

            depart = 110 * i
            arrivee = 110 + 110 * i

            d.text((10, coordinate_y), text[depart:arrivee].replace('\t', ' ').replace('\n', ' '), fill=(0, 0, 0))

        img.save('new_image.png')

    def test_create_multiple_images_from_text(self):
        text = '''
        
        '''

        number_of_caracters_of_text = len(text.replace('\t', ' ').replace('\n', ' '))
        number_of_caracters_per_line = 110

        number_of_lines_with_coma = number_of_caracters_of_text/number_of_caracters_per_line
        number_of_lines = 0

        if int(str(number_of_lines_with_coma).split(".")[1][:1]) < 5:
            number_of_lines += round(number_of_lines_with_coma) + 1

        elif int(str(number_of_lines_with_coma).split(".")[1][:1]) >= 5:
            number_of_lines += round(number_of_lines_with_coma)

        number_of_lines_per_image = 10

        number_of_images_with_coma = number_of_lines/number_of_lines_per_image
        number_of_images = 0

        if int(str(number_of_images_with_coma).split('.')[1][:1]) < 5:
            number_of_images += round(number_of_images_with_coma) + 1

        elif int(str(number_of_images_with_coma).split(".")[1][:1]) >= 5:
            number_of_images += round(number_of_images_with_coma)

        l = 0

        for i in range(1, number_of_images + 1):
            img = Image.new('RGB', (700, 300), color=(255, 255, 255))
            d = ImageDraw.Draw(img)

            if l <= number_of_lines:
                for j in range(0, 10):
                    depart = 110 * l
                    arrivee = 110 + 110 * l
                    coordinate_y = 25 * j

                    if j < 9:
                        d.text((10, coordinate_y), text[depart:arrivee]
                               .replace('\t', ' ')
                               .replace('\n', ' ')
                               .replace(u"\u2018", "'")
                               .replace(u"\u2019", "'")
                               .replace(u"\u0153", "oe")
                               , fill=(0, 0, 0))
                        l += 1

                    elif j == 9:
                        d.text((10, coordinate_y), text[depart:arrivee]
                               .replace('\t', ' ')
                               .replace('\n', ' ')
                               .replace(u"\u2018", "'")
                               .replace(u"\u2019", "'")
                               .replace(u"\u0153", "oe")
                               , fill=(0, 0, 0))

                        l += 1

                        img.save("new_image_" + str(i) + '.png')

    def test_create_images_from_text_from_one_article_of_code_in_force_from_legifrance(self):
        def convert_text_to_images(text):
            number_of_caracters_of_text = len(text.replace('\t', ' ').replace('\n', ' '))
            number_of_caracters_per_line = 110

            number_of_lines_with_coma = number_of_caracters_of_text / number_of_caracters_per_line
            number_of_lines = 0

            if int(str(number_of_lines_with_coma).split(".")[1][:1]) < 5:
                number_of_lines += round(number_of_lines_with_coma) + 1

            elif int(str(number_of_lines_with_coma).split(".")[1][:1]) >= 5:
                number_of_lines += round(number_of_lines_with_coma)

            number_of_lines_per_image = 10

            number_of_images_with_coma = number_of_lines / number_of_lines_per_image
            number_of_images = 0

            if int(str(number_of_images_with_coma).split('.')[1][:1]) < 5:
                number_of_images += round(number_of_images_with_coma) + 1

            elif int(str(number_of_images_with_coma).split(".")[1][:1]) >= 5:
                number_of_images += round(number_of_images_with_coma)

            l = 0

            for i in range(1, number_of_images + 1):
                img = Image.new('RGB', (700, 300), color=(255, 255, 255))
                d = ImageDraw.Draw(img)

                if l <= number_of_lines:
                    for j in range(0, 10):
                        depart = 110 * l
                        arrivee = 110 + 110 * l
                        coordinate_y = 25 * j

                        if j < 9:
                            try:
                                d.text((10, coordinate_y), text[depart:arrivee]
                                       .replace('\t', ' ')
                                       .replace('\n', ' ')
                                       .replace(u"\u2018", "'")
                                       .replace(u"\u2019", "'")
                                       .replace(u"\u0153", "oe")
                                       .replace(u"\u2013", "-")
                                       , fill=(0, 0, 0))
                            except Exception as e:
                                print("Error conversion : " + str(e))

                            l += 1

                        elif j == 9:
                            try:
                                d.text((10, coordinate_y), text[depart:arrivee]
                                       .replace('\t', ' ')
                                       .replace('\n', ' ')
                                       .replace(u"\u2018", "'")
                                       .replace(u"\u2019", "'")
                                       .replace(u"\u0153", "oe")
                                       .replace(u"\u2013", "-")
                                       , fill=(0, 0, 0))
                            except Exception as e:
                                print("Error conversion : " + str(e))

                            l += 1
                            img.save("new_image_" + str(i) + '.png')

        url_article = "https://www.legifrance.gouv.fr/affichCodeArticle.do;jsessionid=2A2478953D4F2C1E867752E6DEECB6B5.tplgfr36s_2?idArticle=LEGIARTI000006419280&cidTexte=LEGITEXT000006070721&dateTexte=20200407"

        # Request the content of a page from the url
        html_article = requests.get(url_article)

        time.sleep(2)

        # Parse the content of html
        soup_article = BeautifulSoup(html_article.content, 'html.parser')

        if soup_article.find("div", {"class": "titreArt"}) is not None:
            intitule_article = soup_article.find("div", {"class": "titreArt"}).text\
                .replace('En savoir plus sur cet article...', '')\
                .replace('\t', ' ')\
                .replace('\n', '')

            if soup_article.find("div", {"class": "corpsArt"}) is not None:
                contenu_article = soup_article.find("div", {"class": "corpsArt"}).text\
                    .replace('\t', ' ')\
                    .replace('\n', '')

                convert_text_to_images(intitule_article + " : " + contenu_article)


if __name__ == '__main__':
    unittest.main()
