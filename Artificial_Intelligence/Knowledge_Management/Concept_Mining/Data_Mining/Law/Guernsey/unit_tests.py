import time
import unittest
import requests
from bs4 import BeautifulSoup
import os


class UnitTestsDataMiningLawGuernsey(unittest.TestCase):
    # ok
    def test_dowload_one_file_from_web(self):
        print('test_dowload_one_file_from_web')

        url_pdf = "https://www.guernseylegalresources.gg/CHttpHandler.ashx?documentid=79528"

        response_pdf = requests.get(url_pdf)

        filename = url_pdf.replace("https://www.guernseylegalresources.gg/CHttpHandler.ashx?documentid=", "") + '.pdf'

        pdf = open(filename, 'wb')
        pdf.write(response_pdf.content)
        pdf.close()
        print("File downloaded")

    # ok
    def test_dowload_one_file_from_the_button(self):
        print('test_dowload_one_file_from_the_button')

        url_law = "https://www.guernseylegalresources.gg/laws/alderney/a/agriculture-and-horticulture/loi-relative-au-doryphore-anglic%C3%A9-colorado-beetle-1932-auregny-consolidated-text/"

        html = requests.get(url_law)

        soup = BeautifulSoup(html.content, 'html.parser')

        if soup.find("a", {"class": "docDownload"}) is not None:
            doc_download = soup.find("a", {"class": "docDownload"}).get("href")

            url_pdf = "https://www.guernseylegalresources.gg" + doc_download

            response_pdf = requests.get(url_pdf)

            filename = soup.find("a", {"class": "docDownload"}).get("title").replace(" ", "")[:15] + '.pdf'

            pdf = open(filename, 'wb')
            pdf.write(response_pdf.content)
            pdf.close()
            print("File downloaded")

    # ok
    def test_extract_all_links_from_one_letter_of_one_topic(self):
        url_topic = "https://www.guernseylegalresources.gg/laws/alderney/a/agriculture-and-horticulture/"

        html = requests.get(url_topic)

        soup = BeautifulSoup(html.content, 'html.parser')

        if soup.find_all("a", {"class": "childLink"}) is not None:
            all_a = soup.find_all("a", {"class": "childLink"})

            for a in all_a:
                link_law = "https://www.guernseylegalresources.gg" + a.get('href').replace('é', '%C3%A9')
                print('link_law : ' + link_law)

    # ok
    def test_extract_all_links_from_one_letter(self):
        url_letter = "https://www.guernseylegalresources.gg/laws/alderney/a/"
        print('url_letter : ' + url_letter)

        html = requests.get(url_letter)

        soup = BeautifulSoup(html.content, 'html.parser')

        if soup.find_all("a", {"class": "childLink"}) is not None:
            all_a = soup.find_all("a", {"class": "childLink"})

            for a in all_a:
                link_topic = "https://www.guernseylegalresources.gg" + a.get('href').replace('é', '%C3%A9')
                print('link_topic : ' + link_topic)

    # ok
    def test_dowload_all_pdf_files_from_guernsey_bailiwick_for_all_letters(self):
        print('test_dowload_all_pdf_files_from_guernsey_bailiwick_for_all_letters')

        letters = []

        from_ = "guernsey-bailiwick"

        for letter in letters:
            i = 0
            parent_dir = "A:\\2_Personnel\\2_Non_Recurrentes\\2_Cours\\38_Laws\\Legislation_Guernsey\\GuernseyBailiwick"
            mode = 0o666
            path = os.path.join(parent_dir, letter)

            if not os.path.isdir(path):
                os.mkdir(path, mode)
                print("Directory '% s' created" % path)
            else:
                print("Directory '% s' already created" % path)

            url_letter = "https://www.guernseylegalresources.gg/laws/" + from_ + "/" + letter + "/"

            print('url_letter : ' + url_letter)

            html_letter = requests.get(url_letter)

            soup_letter = BeautifulSoup(html_letter.content, 'html.parser')

            if soup_letter.find_all("a", {"class": "childLink"}) is not None:
                all_a_letter = soup_letter.find_all("a", {"class": "childLink"})

                for a_letter in all_a_letter:
                    link_topic = "https://www.guernseylegalresources.gg" + a_letter.get('href').replace('é', '%C3%A9')

                    print('link_topic : ' + link_topic)

                    html_topic = requests.get(link_topic)

                    soup_topic = BeautifulSoup(html_topic.content, 'html.parser')

                    if soup_topic.find_all("a", {"class": "childLink"}) is not None:
                        all_a_topic = soup_topic.find_all("a", {"class": "childLink"})

                        for a_topic in all_a_topic:
                            try:
                                link_law = "https://www.guernseylegalresources.gg" \
                                           + a_topic.get('href').replace('é', '%C3%A9')

                                print(str(i) + ' - link_law : ' + link_law)

                                html_law = requests.get(link_law)

                                soup_law = BeautifulSoup(html_law.content, 'html.parser')

                                if soup_law.find("a", {"class": "docDownload"}) is not None:
                                    doc_download = soup_law.find("a", {"class": "docDownload"}).get("href")

                                    url_pdf = "https://www.guernseylegalresources.gg" + doc_download

                                    response_pdf = requests.get(url_pdf)

                                    filename = str(i) + '_' + soup_law.find("a", {"class": "docDownload"}).get("title").replace(" ", "")[:15] + '.pdf'

                                    pdf = open(path + "\\" + filename, 'wb')

                                    pdf.write(response_pdf.content)

                                    pdf.close()

                                    print("File " + filename + " downloaded")

                                    i += 1

                                    time.sleep(5)
                            except Exception as e:
                                print("error link_law : " + str(e))

    # ok
    def test_dowload_all_pdf_files_from_alderney_for_all_letters(self):
        print('test_dowload_all_pdf_files_from_alderney_for_all_letters')

        letters = []

        from_ = "alderney"

        for letter in letters:
            i = 0
            parent_dir = "A:\\2_Personnel\\2_Non_Recurrentes\\2_Cours\\38_Laws\\Legislation_Guernsey\\Alderney"
            mode = 0o666
            path = os.path.join(parent_dir, letter)

            if not os.path.isdir(path):
                os.mkdir(path, mode)
                print("Directory '% s' created" % path)
            else:
                print("Directory '% s' already created" % path)

            url_letter = "https://www.guernseylegalresources.gg/laws/" + from_ + "/" + letter + "/"

            print('url_letter : ' + url_letter)

            html_letter = requests.get(url_letter)

            soup_letter = BeautifulSoup(html_letter.content, 'html.parser')

            if soup_letter.find_all("a", {"class": "childLink"}) is not None:
                all_a_letter = soup_letter.find_all("a", {"class": "childLink"})

                for a_letter in all_a_letter:
                    link_topic = "https://www.guernseylegalresources.gg" + a_letter.get('href').replace('é', '%C3%A9')

                    print('link_topic : ' + link_topic)

                    html_topic = requests.get(link_topic)

                    soup_topic = BeautifulSoup(html_topic.content, 'html.parser')

                    if soup_topic.find_all("a", {"class": "childLink"}) is not None:
                        all_a_topic = soup_topic.find_all("a", {"class": "childLink"})

                        for a_topic in all_a_topic:
                            try:
                                link_law = "https://www.guernseylegalresources.gg" \
                                           + a_topic.get('href').replace('é', '%C3%A9')

                                print(str(i) + ' - link_law : ' + link_law)

                                html_law = requests.get(link_law)

                                soup_law = BeautifulSoup(html_law.content, 'html.parser')

                                if soup_law.find("a", {"class": "docDownload"}) is not None:
                                    doc_download = soup_law.find("a", {"class": "docDownload"}).get("href")

                                    url_pdf = "https://www.guernseylegalresources.gg" + doc_download

                                    response_pdf = requests.get(url_pdf)

                                    filename = str(i) + '_' + soup_law.find("a", {"class": "docDownload"}).get("title").replace(" ", "")[:15] + '.pdf'

                                    pdf = open(path + "\\" + filename, 'wb')

                                    pdf.write(response_pdf.content)

                                    pdf.close()

                                    print("File " + filename + " downloaded")

                                    i += 1

                                    time.sleep(5)
                            except Exception as e:
                                print("error link_law : " + str(e))

    # ok
    def test_dowload_all_pdf_files_from_sark_for_all_letters(self):
        print('test_dowload_all_pdf_files_from_sark_for_all_letters')

        letters = []

        from_ = "sark"

        for letter in letters:
            i = 0
            parent_dir = "A:\\2_Personnel\\2_Non_Recurrentes\\2_Cours\\38_Laws\\Legislation_Guernsey\\Sark"
            mode = 0o666
            path = os.path.join(parent_dir, letter)

            if not os.path.isdir(path):
                os.mkdir(path, mode)
                print("Directory '% s' created" % path)
            else:
                print("Directory '% s' already created" % path)

            url_letter = "https://www.guernseylegalresources.gg/laws/" + from_ + "/" + letter + "/"

            print('url_letter : ' + url_letter)

            html_letter = requests.get(url_letter)

            soup_letter = BeautifulSoup(html_letter.content, 'html.parser')

            if soup_letter.find_all("a", {"class": "childLink"}) is not None:
                all_a_letter = soup_letter.find_all("a", {"class": "childLink"})

                for a_letter in all_a_letter:
                    link_topic = "https://www.guernseylegalresources.gg" + a_letter.get('href').replace('é', '%C3%A9')

                    print('link_topic : ' + link_topic)

                    html_topic = requests.get(link_topic)

                    soup_topic = BeautifulSoup(html_topic.content, 'html.parser')

                    if soup_topic.find_all("a", {"class": "childLink"}) is not None:
                        all_a_topic = soup_topic.find_all("a", {"class": "childLink"})

                        for a_topic in all_a_topic:
                            try:
                                link_law = "https://www.guernseylegalresources.gg" \
                                           + a_topic.get('href').replace('é', '%C3%A9')

                                print(str(i) + ' - link_law : ' + link_law)

                                html_law = requests.get(link_law)

                                soup_law = BeautifulSoup(html_law.content, 'html.parser')

                                if soup_law.find("a", {"class": "docDownload"}) is not None:
                                    doc_download = soup_law.find("a", {"class": "docDownload"}).get("href")

                                    url_pdf = "https://www.guernseylegalresources.gg" + doc_download

                                    response_pdf = requests.get(url_pdf)

                                    filename = str(i) + '_' + soup_law.find("a", {"class": "docDownload"}).get("title").replace(" ", "")[:15] + '.pdf'

                                    pdf = open(path + "\\" + filename, 'wb')

                                    pdf.write(response_pdf.content)

                                    pdf.close()

                                    print("File " + filename + " downloaded")

                                    i += 1

                                    time.sleep(5)
                            except Exception as e:
                                print("error link_law : " + str(e))


if __name__ == '__main__':
    unittest.main()
