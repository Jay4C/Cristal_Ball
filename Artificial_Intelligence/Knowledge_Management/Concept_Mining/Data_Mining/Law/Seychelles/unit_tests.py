import time
import unittest
import requests
import os
from bs4 import BeautifulSoup


class UnitTestsDataMiningLawSeychelles(unittest.TestCase):
    # ok
    def test_dowload_one_file_from_web(self):
        print('test_dowload_one_file_from_web')

        url_law = "https://greybook.seylii.org/w/se/CAP40"

        url_pdf = url_law + ".pdf"

        response_pdf = requests.get(url_pdf)

        pdf = open(url_pdf.replace("https://greybook.seylii.org/w/se/", ""), 'wb')
        pdf.write(response_pdf.content)
        pdf.close()
        print("File downloaded")

    # ok
    def test_dowload_one_file_from_consolidated_link(self):
        print('test_dowload_one_file_from_consolidated_link')

        url_consolidated_link = "https://seylii.org/sc/legislation/consolidated-act/40"

        html = requests.get(url_consolidated_link)

        soup = BeautifulSoup(html.content, 'html.parser')

        if soup.find("h1", {"class": "page-title"}) is not None:
            title = soup.find("h1", {"class": "page-title"}).text.replace(" ", "")

            url_law = "https://greybook.seylii.org/w/se/CAP" + url_consolidated_link.replace("https://seylii.org/sc/legislation/consolidated-act/", "")

            url_pdf = url_law + ".pdf"

            response_pdf = requests.get(url_pdf)

            filename = title + ".pdf"

            pdf = open(filename, 'wb')
            pdf.write(response_pdf.content)
            pdf.close()
            print("File downloaded")

    # ok
    def test_extract_all_links_from_one_letter(self):
        url_laws_seychelles_for_one_letter = "https://seylii.org/sc/legislation/laws-of-seychelles/C"

        html = requests.get(url_laws_seychelles_for_one_letter)

        soup = BeautifulSoup(html.content, 'html.parser')

        if soup.find_all("li", {"class": "views-row"}) is not None:
            all_li = soup.find_all("li", {"class": "views-row"})

            for li in all_li:
                link = "https://seylii.org" + li.find('a').get('href')
                print('link : ' + link)

    # ok
    def test_download_all_pdfs_from_one_letter(self):
        letter = "A"
        directory = letter
        parent_dir = "A:\\2_Personnel\\2_Non_Recurrentes\\2_Cours\\38_Laws\\Legislation_Seychelles"
        mode = 0o666
        path = os.path.join(parent_dir, directory)

        if not os.path.isdir(path):
            os.mkdir(path, mode)
            print("Directory '% s' created" % directory)
        else:
            print("Directory '% s' already created" % directory)

        url_laws_seychelles_for_one_letter = "https://seylii.org/sc/legislation/laws-of-seychelles/" + letter

        html = requests.get(url_laws_seychelles_for_one_letter)

        soup = BeautifulSoup(html.content, 'html.parser')

        if soup.find_all("li", {"class": "views-row"}) is not None:
            all_li = soup.find_all("li", {"class": "views-row"})

            for li in all_li:
                try:
                    link = "https://seylii.org" + li.find('a').get('href')

                    print('link : ' + link)

                    url_consolidated_link = "https://greybook.seylii.org/w/se/CAP" \
                                            + link.replace("https://seylii.org/sc/legislation/consolidated-act/", "")

                    html = requests.get(link)

                    soup = BeautifulSoup(html.content, 'html.parser')

                    if soup.find("h1", {"class": "page-title"}) is not None:
                        title = soup.find("h1", {"class": "page-title"}).text.replace(" ", "")

                        url_pdf = url_consolidated_link + ".pdf"

                        if "https://seylii.org/sc/legislation/consolidated-act/" in link:
                            response_pdf = requests.get(url_pdf)

                            filename = title + ".pdf"

                            pdf = open(path + "\\" + filename, 'wb')

                            pdf.write(response_pdf.content)

                            pdf.close()

                            print("File " + filename + " downloaded")
                except Exception as e:
                    print('error pdf : ' + str(e))

    # ok
    def test_download_all_pdfs_from_all_letters(self):
        print('test_download_all_pdfs_from_all_letters')

        letters = ['B', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'W']

        for letter in letters:
            directory = letter
            parent_dir = "A:\\2_Personnel\\2_Non_Recurrentes\\2_Cours\\38_Laws\\Legislation_Seychelles"
            mode = 0o666
            path = os.path.join(parent_dir, directory)

            if not os.path.isdir(path):
                os.mkdir(path, mode)
                print("Directory '% s' created" % directory)
            else:
                print("Directory '% s' already created" % directory)

            url_laws_seychelles_for_one_letter = "https://seylii.org/sc/legislation/laws-of-seychelles/" + letter

            html = requests.get(url_laws_seychelles_for_one_letter)

            soup = BeautifulSoup(html.content, 'html.parser')

            if soup.find_all("li", {"class": "views-row"}) is not None:
                all_li = soup.find_all("li", {"class": "views-row"})

                for li in all_li:
                    try:
                        link = "https://seylii.org" + li.find('a').get('href')

                        print('link : ' + link)

                        url_consolidated_link = "https://greybook.seylii.org/w/se/CAP" \
                                                + link.replace("https://seylii.org/sc/legislation/consolidated-act/",
                                                               "")

                        html = requests.get(link)

                        soup = BeautifulSoup(html.content, 'html.parser')

                        if soup.find("h1", {"class": "page-title"}) is not None:
                            title = soup.find("h1", {"class": "page-title"}).text.replace(" ", "")

                            url_pdf = url_consolidated_link + ".pdf"

                            if "https://seylii.org/sc/legislation/consolidated-act/" in link:
                                response_pdf = requests.get(url_pdf)

                                filename = title + ".pdf"

                                pdf = open(path + "\\" + filename, 'wb')

                                pdf.write(response_pdf.content)

                                pdf.close()

                                print("File " + filename + " downloaded")
                    except Exception as e:
                        print('error pdf : ' + str(e))


if __name__ == '__main__':
    unittest.main()
