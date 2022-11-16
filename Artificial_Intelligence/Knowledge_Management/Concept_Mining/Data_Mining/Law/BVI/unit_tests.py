import time
import unittest
import requests
import os
from bs4 import BeautifulSoup


class UnitTestsDataMiningBVILaw(unittest.TestCase):
    # ok
    def test_dowload_one_file_from_web(self):
        print('test_dowload_one_file_from_web')

        # URL from which pdfs to be downloaded
        url = "https://bvi.gov.vg/sites/default/files/resources/food_security_and_sustainability_act_2022.pdf"

        # Requests URL and get response object
        response = requests.get(url)

        # Write content in pdf file
        pdf = open(
            url.replace("https://bvi.gov.vg/sites/default/files/resources/", ""), 'wb'
        )
        pdf.write(response.content)
        pdf.close()
        print("File downloaded")

    # ok
    def test_dowload_one_file_from_one_link(self):
        print('test_dowload_one_file_from_one_link')

        link = "http://www.bvi.gov.vg/content/food-security-and-sustainability-act-2022"

        html = requests.get(link)

        # Parse the content of html
        soup = BeautifulSoup(html.content, 'html.parser')

        if soup.find('div', {'class': 'field-name-field-file'}) is not None:
            url_pdf = soup.find('div', {'class': 'field-name-field-file'}).find('a').get('href')

            response = requests.get(url_pdf)

            pdf = open(
                url_pdf.replace("https://bvi.gov.vg/sites/default/files/resources/", ""), 'wb'
            )

            pdf.write(response.content)

            pdf.close()

            print("File downloaded")
        else:
            print('error div class field-name-field-file')

    # ok
    def test_show_all_links_for_pdf_from_one_page_result(self):
        print("test_show_all_links_for_pdf_from_one_page_result")

        url_result = "http://www.bvi.gov.vg/file-type/legislation?page=12"
        print("url_result : " + url_result)

        html = requests.get(url_result)

        soup = BeautifulSoup(html.content, 'html.parser')

        if soup.find("div", {'class': 'node'}) is not None:
            all_nodes = soup.find_all("div", {'class': 'node'})

            for node in all_nodes:
                url_law = "http://www.bvi.gov.vg" + node.find("a").get('href')
                print('url_law : ' + url_law)
        else:
            print('erro div class node')

    # ok
    def test_download_all_pdf_files_from_one_page_result(self):
        print("test_show_all_links_for_pdf_from_one_page_result")

        url_result = "http://www.bvi.gov.vg/file-type/legislation?page=12"

        print("url_result : " + url_result)

        html = requests.get(url_result)

        soup = BeautifulSoup(html.content, 'html.parser')

        if soup.find("div", {'class': 'node'}) is not None:
            all_nodes = soup.find_all("div", {'class': 'node'})

            for node in all_nodes:
                url_law = "http://www.bvi.gov.vg" + node.find("a").get('href')

                print('url_law : ' + url_law)

                html = requests.get(url_law)

                soup = BeautifulSoup(html.content, 'html.parser')

                if soup.find('div', {'class': 'field-name-field-file'}) is not None:
                    url_pdf = soup.find('div', {'class': 'field-name-field-file'}).find('a').get('href')

                    response = requests.get(url_pdf)

                    filename = url_pdf.replace("https://bvi.gov.vg/sites/default/files/resources/", "")\
                        .replace("%", "")\
                        .replace("-", "")\
                        .replace('.pdf', '') \
                        .replace("No", "")\
                        .replace(".", "").lower()[:20]

                    pdf = open(filename + ".pdf", 'wb')

                    pdf.write(response.content)

                    pdf.close()

                    print("File downloaded")
                else:
                    print('error div class field-name-field-file')
        else:
            print('erro div class node')

    # ok
    def test_download_all_pdf_files_from_one_page_result_into_one_directory(self):
        print("test_show_all_links_for_pdf_from_one_page_result")

        parent_dir = "C:\\Users\\DELL\\Documents\\Laws\\\Legislation_BVI"

        if os.path.isdir(parent_dir):
            print("Directory '% s' created" % parent_dir)

            url_result = "http://www.bvi.gov.vg/file-type/legislation?page=12"

            print("url_result : " + url_result)

            html = requests.get(url_result)

            soup = BeautifulSoup(html.content, 'html.parser')

            if soup.find("div", {'class': 'node'}) is not None:
                all_nodes = soup.find_all("div", {'class': 'node'})

                for node in all_nodes:
                    url_law = "http://www.bvi.gov.vg" + node.find("a").get('href')

                    print('url_law : ' + url_law)

                    html = requests.get(url_law)

                    soup = BeautifulSoup(html.content, 'html.parser')

                    if soup.find('div', {'class': 'field-name-field-file'}) is not None:
                        url_pdf = soup.find('div', {'class': 'field-name-field-file'}).find('a').get('href')

                        response = requests.get(url_pdf)

                        filename = url_pdf.replace("https://bvi.gov.vg/sites/default/files/resources/", "") \
                                       .replace("%", "") \
                                       .replace("-", "") \
                                       .replace('.pdf', '') \
                                       .replace("No", "") \
                                       .replace(".", "").lower()[:20]

                        pdf = open(parent_dir + "\\" + filename + ".pdf", 'wb')

                        pdf.write(response.content)

                        pdf.close()

                        print("File downloaded")
                    else:
                        print('error div class field-name-field-file')
            else:
                print('erro div class node')
        else:
            print('error parent_dir')

    # ok
    def test_download_all_pdf_files_from_all_pages_into_one_directory(self):
        print("test_show_all_links_for_pdf_from_one_page_result")

        parent_dir = "C:\\Users\\DELL\\Documents\\Laws\\\Legislation_BVI"

        if os.path.isdir(parent_dir):
            print("Directory '% s' created" % parent_dir)

            for i in range(0, 13):
                if i == 0:
                    url_result = "http://www.bvi.gov.vg/file-type/legislation"

                    print("url_result : " + url_result)

                    html = requests.get(url_result)

                    soup = BeautifulSoup(html.content, 'html.parser')

                    if soup.find("div", {'class': 'node'}) is not None:
                        all_nodes = soup.find_all("div", {'class': 'node'})

                        for node in all_nodes:
                            url_law = "http://www.bvi.gov.vg" + node.find("a").get('href')

                            print('url_law : ' + url_law)

                            html = requests.get(url_law)

                            soup = BeautifulSoup(html.content, 'html.parser')

                            if soup.find('div', {'class': 'field-name-field-file'}) is not None:
                                url_pdf = soup.find('div', {'class': 'field-name-field-file'}).find('a').get('href')

                                response = requests.get(url_pdf)

                                filename = url_pdf.replace("https://bvi.gov.vg/sites/default/files/resources/", "") \
                                               .replace("%", "") \
                                               .replace("-", "") \
                                               .replace('.pdf', '') \
                                               .replace("No", "") \
                                               .replace(".", "").lower()[:20]

                                pdf = open(parent_dir + "\\" + filename + ".pdf", 'wb')

                                pdf.write(response.content)

                                pdf.close()

                                print("File downloaded")
                            else:
                                print('error div class field-name-field-file')
                    else:
                        print('erro div class node')
                else:
                    url_result = "http://www.bvi.gov.vg/file-type/legislation?page=" + str(i)

                    print("url_result : " + url_result)

                    html = requests.get(url_result)

                    soup = BeautifulSoup(html.content, 'html.parser')

                    if soup.find("div", {'class': 'node'}) is not None:
                        all_nodes = soup.find_all("div", {'class': 'node'})

                        for node in all_nodes:
                            url_law = "http://www.bvi.gov.vg" + node.find("a").get('href')

                            print('url_law : ' + url_law)

                            html = requests.get(url_law)

                            soup = BeautifulSoup(html.content, 'html.parser')

                            if soup.find('div', {'class': 'field-name-field-file'}) is not None:
                                url_pdf = soup.find('div', {'class': 'field-name-field-file'}).find('a').get('href')

                                response = requests.get(url_pdf)

                                filename = url_pdf.replace("https://bvi.gov.vg/sites/default/files/resources/", "") \
                                               .replace("%", "") \
                                               .replace("-", "") \
                                               .replace('.pdf', '') \
                                               .replace("No", "") \
                                               .replace(".", "").lower()[:20]

                                pdf = open(parent_dir + "\\" + filename + ".pdf", 'wb')

                                pdf.write(response.content)

                                pdf.close()

                                print("File downloaded")
                            else:
                                print('error div class field-name-field-file')
                    else:
                        print('erro div class node')
        else:
            print('error parent_dir')


if __name__ == '__main__':
    unittest.main()
