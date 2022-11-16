import subprocess
import time
import unittest
import warnings
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import requests
import os


class UnitTestsDataMiningJerseyLaw(unittest.TestCase):
    # ok
    def test_dowload_one_file_from_web(self):
        print('test_dowload_one_file_from_web')

        # URL from which pdfs to be downloaded
        url = "https://www.jerseylaw.je/laws/current/PDFs/07.025.pdf"

        # Requests URL and get response object
        response = requests.get(url)

        # Write content in pdf file
        pdf = open(
            url.replace("https://www.jerseylaw.je/laws/current/PDFs/", ""), 'wb'
        )
        pdf.write(response.content)
        pdf.close()
        print("File downloaded")

    # ok
    def test_dowload_one_file_from_one_link(self):
        print('test_dowload_one_file_from_one_link')

        link = "https://www.jerseylaw.je/laws/current/Pages/07.025.aspx"

        url_pdf = link.replace('Pages', 'PDFs').replace('aspx', 'pdf')
        # Requests URL and get response object
        response = requests.get(url_pdf)

        # Write content in pdf file
        pdf = open(
            url_pdf.replace("https://www.jerseylaw.je/laws/current/PDFs/", ""), 'wb'
        )
        pdf.write(response.content)
        pdf.close()
        print("File downloaded")

    # ok
    def test_show_the_number_of_pages_from_one_letter(self):
        print('test_show_the_number_of_pages_from_one_letter')

        url = "https://www.jerseylaw.je/laws/current/Pages/search.aspx?size=n_60_n&filters%5B0%5D%5Bfield%5D=TitleStartsWith&filters%5B0%5D%5Bvalues%5D%5B0%5D=A"

        time.sleep(5)

        warnings.filterwarnings(
            action="ignore",
            message="unclosed",
            category=ResourceWarning
        )

        time.sleep(5)

        # with Firefox
        options = Options()
        options.headless = True
        browser = webdriver.Firefox(
            executable_path='..\\..\\geckodriver.exe',
            options=options
        )

        time.sleep(5)

        # maximize window
        browser.maximize_window()
        print("browser.maximize_window()")

        time.sleep(5)

        # open
        browser.get(url=url)
        print("browser.get(url=url)")

        time.sleep(10)

        number_of_pages = 0

        if browser.find_element_by_xpath(
                "/html/body/form/div[3]/div/div[2]/span/main/div[1]/div/div/div[3]/div[3]/div/div/div[1]"
                "/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div[1]") is not None:
            content = browser.find_element_by_xpath(
                "/html/body/form/div[3]/div/div[2]/span/main/div[1]/div/div/div[3]/div[3]/div/div/div[1]"
                "/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div[1]")

            number_of_pages_with_coma = int(content
                                            .text
                                            .replace("Showing 1 - 60 out of ", "")
                                            ) / 60

            if int(str(number_of_pages_with_coma).split(".")[1][:1]) < 5:
                number_of_pages += round(number_of_pages_with_coma) + 1
                print('number_of_pages : ' + str(number_of_pages))
            elif int(str(number_of_pages_with_coma).split(".")[1][:1]) >= 5:
                number_of_pages += round(number_of_pages_with_coma)
                print('number_of_pages : ' + str(number_of_pages))
        else:
            print("error pages")

        time.sleep(3)

        browser.quit()
        print("browser.quit()")

    # ok
    def test_show_the_number_of_pages_for_all_letter(self):
        print('test_show_the_number_of_pages_for_all_letter')

        time.sleep(5)

        warnings.filterwarnings(
            action="ignore",
            message="unclosed",
            category=ResourceWarning
        )

        time.sleep(5)

        # with Firefox
        options = Options()
        options.headless = True
        browser = webdriver.Firefox(
            executable_path='..\\..\\geckodriver.exe',
            options=options
        )

        time.sleep(5)

        # maximize window
        browser.maximize_window()
        print("browser.maximize_window()")

        time.sleep(5)

        letters = [
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
            'U', 'V', 'W'
        ]

        for letter in letters:
            url = "https://www.jerseylaw.je/laws/current/Pages/search.aspx?size=n_60_n&filters%5B0%5D%5Bfield%5D" \
                  "=TitleStartsWith&filters%5B0%5D%5Bvalues%5D%5B0%5D=" + letter
            print('url : ' + str(url))

            time.sleep(5)

            # open
            browser.get(url=url)
            print("browser.get(url=url)")

            time.sleep(10)

            number_of_pages = 0

            if browser.find_element_by_xpath(
                    "/html/body/form/div[3]/div/div[2]/span/main/div[1]/div/div/div[3]/div[3]/div/div/div[1]"
                    "/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div[1]") is not None:
                content = browser.find_element_by_xpath(
                    "/html/body/form/div[3]/div/div[2]/span/main/div[1]/div/div/div[3]/div[3]/div/div/div[1]"
                    "/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div[1]")

                number_of_pages_with_coma = int(content
                                                .text
                                                .replace(' ', '')
                                                .split("of")[1]
                                                ) / 60

                if int(str(number_of_pages_with_coma).split(".")[1][:1]) < 5:
                    number_of_pages += round(number_of_pages_with_coma) + 1
                    print('number_of_pages : ' + str(number_of_pages))
                elif int(str(number_of_pages_with_coma).split(".")[1][:1]) >= 5:
                    number_of_pages += round(number_of_pages_with_coma)
                    print('number_of_pages : ' + str(number_of_pages))
            else:
                print("error pages")

        time.sleep(3)

        browser.quit()
        print("browser.quit()")

    # ok
    def test_show_all_links_for_pdf_from_one_letter_and_one_page(self):
        print("test_dowload_all_links_for_pdf_from_one_letter")

        letter = "A"

        url_letter = "https://www.jerseylaw.je/laws/current/Pages/search.aspx?size=n_60_n&filters%5B0%5D%5Bfield%5D=" \
              "TitleStartsWith&filters%5B0%5D%5Bvalues%5D%5B0%5D=" \
              + letter \
              + "&filters%5B0%5D%5Btype%5D=all&sort-field=RefinableString11&sort-direction=asc"
        print("url_letter : " + url_letter)

        time.sleep(5)

        warnings.filterwarnings(
            action="ignore",
            message="unclosed",
            category=ResourceWarning
        )

        time.sleep(5)

        # with Firefox
        options = Options()
        options.headless = True
        browser = webdriver.Firefox(
            executable_path='..\\..\\geckodriver.exe',
            options=options
        )

        time.sleep(5)

        # maximize window
        browser.maximize_window()
        print("browser.maximize_window()")

        time.sleep(5)

        # open
        browser.get(url=url_letter)
        print("browser.get(url=url_letter)")

        time.sleep(10)

        number_of_pages = 0

        if browser.find_element_by_xpath(
                "/html/body/form/div[3]/div/div[2]/span/main/div[1]/div/div/div[3]/div[3]/div/div/div[1]"
                "/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div[1]") is not None:
            content = browser.find_element_by_xpath(
                "/html/body/form/div[3]/div/div[2]/span/main/div[1]/div/div/div[3]/div[3]/div/div/div[1]"
                "/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div[1]")

            number_of_pages_with_coma = int(content
                                            .text
                                            .replace("Showing 1 - 60 out of ", "")
                                            ) / 60

            if int(str(number_of_pages_with_coma).split(".")[1][:1]) < 5:
                number_of_pages += round(number_of_pages_with_coma) + 1
                print('number_of_pages : ' + str(number_of_pages))
            elif int(str(number_of_pages_with_coma).split(".")[1][:1]) >= 5:
                number_of_pages += round(number_of_pages_with_coma)
                print('number_of_pages : ' + str(number_of_pages))
        else:
            print("error pages")

        url_page = "https://www.jerseylaw.je/laws/current/Pages/search.aspx?current=n_" \
                   + str(1) \
                   + "_n&size=n_60_n&filters%5B0%5D%5Bfield%5D=TitleStartsWith&filters%5B0%5D%5Bvalues%5D%5B0%5D=" \
                   + letter \
                   + "&filters%5B0%5D%5Btype%5D=all&sort-field=RefinableString11&sort-direction=asc"

        time.sleep(3)

        browser.get(url_page)
        print("browser.get(url_page)")

        time.sleep(15)

        all_law = browser.find_elements_by_class_name("resultRow")
        print('all_law = browser.find_elements_by_class_name("resultRow")')

        time.sleep(3)

        for law in all_law:
            print(law.find_element_by_tag_name('a').get_attribute('href'))

        time.sleep(3)

        browser.quit()
        print("browser.quit()")

    # ok
    def test_show_all_title_for_pdf_from_one_letter_and_one_page(self):
        print("test_show_all_title_for_pdf_from_one_letter_and_one_page")

        letter = "A"

        url_letter = "https://www.jerseylaw.je/laws/current/Pages/search.aspx?size=n_60_n&filters%5B0%5D%5Bfield%5D=" \
              "TitleStartsWith&filters%5B0%5D%5Bvalues%5D%5B0%5D=" \
              + letter \
              + "&filters%5B0%5D%5Btype%5D=all&sort-field=RefinableString11&sort-direction=asc"
        print("url_letter : " + url_letter)

        time.sleep(5)

        warnings.filterwarnings(
            action="ignore",
            message="unclosed",
            category=ResourceWarning
        )

        time.sleep(5)

        # with Firefox
        options = Options()
        options.headless = True
        browser = webdriver.Firefox(
            executable_path='..\\..\\geckodriver.exe',
            options=options
        )

        time.sleep(5)

        # maximize window
        browser.maximize_window()
        print("browser.maximize_window()")

        time.sleep(5)

        # open
        browser.get(url=url_letter)
        print("browser.get(url=url_letter)")

        time.sleep(10)

        number_of_pages = 0

        if browser.find_element_by_xpath(
                "/html/body/form/div[3]/div/div[2]/span/main/div[1]/div/div/div[3]/div[3]/div/div/div[1]"
                "/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div[1]") is not None:
            content = browser.find_element_by_xpath(
                "/html/body/form/div[3]/div/div[2]/span/main/div[1]/div/div/div[3]/div[3]/div/div/div[1]"
                "/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div[1]")

            number_of_pages_with_coma = int(content
                                            .text
                                            .replace("Showing 1 - 60 out of ", "")
                                            ) / 60

            if int(str(number_of_pages_with_coma).split(".")[1][:1]) < 5:
                number_of_pages += round(number_of_pages_with_coma) + 1
                print('number_of_pages : ' + str(number_of_pages))
            elif int(str(number_of_pages_with_coma).split(".")[1][:1]) >= 5:
                number_of_pages += round(number_of_pages_with_coma)
                print('number_of_pages : ' + str(number_of_pages))
        else:
            print("error pages")

        url_page = "https://www.jerseylaw.je/laws/current/Pages/search.aspx?current=n_" \
                   + str(1) \
                   + "_n&size=n_60_n&filters%5B0%5D%5Bfield%5D=TitleStartsWith&filters%5B0%5D%5Bvalues%5D%5B0%5D=" \
                   + letter \
                   + "&filters%5B0%5D%5Btype%5D=all&sort-field=RefinableString11&sort-direction=asc"

        time.sleep(3)

        browser.get(url_page)
        print("browser.get(url_page)")

        time.sleep(15)

        all_law = browser.find_elements_by_class_name("resultRow")
        print('all_law = browser.find_elements_by_class_name("resultRow")')

        time.sleep(3)

        laws_link = []

        for law in all_law:
            link = law.find_element_by_tag_name('a').get_attribute('href')
            laws_link.append(link)

        for law_link in laws_link:
            try:
                time.sleep(3)

                browser.get(law_link)
                print("browser.get(law_link)")

                time.sleep(15)

                title = browser.find_element_by_xpath(
                    "/html/body/form/div[3]/div/div[2]/div[4]/div/div/span/span[7]"
                ).text.replace(' ', '').replace('(', '').replace(')', '') + ".pdf"
                print("title : " + title)
            except Exception as e:
                print('error : ' + str(e))

            time.sleep(3)

        time.sleep(3)

        browser.quit()
        print("browser.quit()")

        time.sleep(3)

        print("run_ccleaner")
        os.system("set ccleaner='C:\\Program Files\\CCleaner\\CCleaner.exe'")
        os.system("start ccleaner /AUTO")

    # ok
    def test_dowload_all_pdf_from_one_letter(self):
        print("test_dowload_all_pdf_from_one_letter")

        letter = "A"
        directory = letter
        parent_dir = "C:\\Users\\DELL\\Documents\\Laws\\Legislation_Jersey"
        mode = 0o666
        path = os.path.join(parent_dir, directory)

        if not os.path.isdir(path):
            os.mkdir(path, mode)
            print("Directory '% s' created" % directory)

        url_letter = "https://www.jerseylaw.je/laws/current/Pages/search.aspx?size=n_60_n" \
                     "&filters%5B0%5D%5Bfield%5D=TitleStartsWith&filters%5B0%5D%5Bvalues%5D%5B0%5D=" + letter
        print("url_letter : " + url_letter)

        time.sleep(5)

        warnings.filterwarnings(
            action="ignore",
            message="unclosed",
            category=ResourceWarning
        )

        time.sleep(5)

        # with Firefox
        options = Options()
        options.headless = True
        browser = webdriver.Firefox(
            executable_path='..\\..\\geckodriver.exe',
            options=options
        )

        time.sleep(5)

        # maximize window
        browser.maximize_window()
        print("browser.maximize_window()")

        time.sleep(5)

        # open
        browser.get(url=url_letter)
        print("browser.get(url=url_letter)")

        time.sleep(15)

        number_of_pages = 0

        if browser.find_element_by_xpath("/html/body/form/div[3]/div/div[2]/span/main/div[1]/div/div/div[3]/div[3]/div/div/div[1]"
                "/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div[1]") is not None:
            content = browser.find_element_by_xpath("/html/body/form/div[3]/div/div[2]/span/main/div[1]/div/div/div[3]/div[3]/div/div/div[1]"
                "/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div[1]")

            number_of_pages_with_coma = int(content
                                            .text
                                            .replace("Showing 1 - 60 out of ", "")
                                            ) / 60

            if int(str(number_of_pages_with_coma).split(".")[1][:1]) < 5:
                number_of_pages += round(number_of_pages_with_coma) + 1
                print('number_of_pages : ' + str(number_of_pages))
            elif int(str(number_of_pages_with_coma).split(".")[1][:1]) >= 5:
                number_of_pages += round(number_of_pages_with_coma)
                print('number_of_pages : ' + str(number_of_pages))
        else:
            print("error pages")

        for i in range(1, number_of_pages + 1):
            url_page = "https://www.jerseylaw.je/laws/current/Pages/search.aspx?current=n_" \
                       + str(i) \
                       + "_n&size=n_60_n&filters%5B0%5D%5Bfield%5D=TitleStartsWith&filters%5B0%5D%5Bvalues%5D%5B0%5D=" \
                       + letter

            time.sleep(3)

            browser.get(url_page)
            print("browser.get(url_page)")

            time.sleep(15)

            all_law = browser.find_elements_by_class_name("resultRow")
            print('all_law = browser.find_elements_by_class_name("resultRow")')

            time.sleep(5)

            laws_link = []

            for law in all_law:
                link = law.find_element_by_tag_name('a').get_attribute('href')
                laws_link.append(link)

            time.sleep(5)

            for law_link in laws_link:
                try:
                    time.sleep(3)

                    browser.get(law_link)
                    print("browser.get(law_link)")

                    time.sleep(15)

                    title = browser.find_element_by_xpath(
                        "/html/body/form/div[3]/div/div[2]/div[4]/div/div/span/span[7]"
                    ).text.replace(' ', '').replace('(', '').replace(')', '') + ".pdf"
                    print("title : " + title)

                    url_pdf = law_link.replace('Pages', 'PDFs').replace('aspx', 'pdf')

                    response = requests.get(url_pdf)

                    filename = title + ".pdf"

                    pdf = open(path + "\\" + filename, 'wb')

                    pdf.write(response.content)

                    pdf.close()

                    print("File " + filename + " downloaded")

                    time.sleep(5)
                except Exception as e:
                    print('error : ' + str(e))

                time.sleep(5)

        time.sleep(5)

        browser.quit()
        print("browser.quit()")

        time.sleep(5)

        print("run_ccleaner")
        os.system("set ccleaner='C:\\Program Files\\CCleaner\\CCleaner.exe'")
        os.system("start ccleaner /AUTO")

    # ok
    def test_dowload_all_pdf_from_all_letters(self):
        print("test_dowload_all_pdf_from_all_letters")

        letters = []

        for letter in letters:
            directory = letter
            parent_dir = "A:\\2_Personnel\\2_Non_Recurrentes\\2_Cours\\38_Laws\\Legislation_Jersey"
            mode = 0o666
            path = os.path.join(parent_dir, directory)

            if not os.path.isdir(path):
                os.mkdir(path, mode)
                print("Directory '% s' created" % directory)
            else:
                print("Directory '% s' already created" % directory)

            url_letter = "https://www.jerseylaw.je/laws/current/Pages/search.aspx?size=n_60_n" \
                         "&filters%5B0%5D%5Bfield%5D=TitleStartsWith&filters%5B0%5D%5Bvalues%5D%5B0%5D=" + letter
            print("url_letter : " + url_letter)

            time.sleep(5)

            warnings.filterwarnings(
                action="ignore",
                message="unclosed",
                category=ResourceWarning
            )

            time.sleep(5)

            # with Firefox
            options = Options()
            options.headless = True
            browser = webdriver.Firefox(
                executable_path='..\\..\\geckodriver.exe',
                options=options
            )

            time.sleep(10)

            # maximize window
            browser.maximize_window()
            print("browser.maximize_window()")

            time.sleep(5)

            number_of_pages = 0

            # open
            while True:
                browser.get(url=url_letter)
                print("browser.get(url=url_letter)")

                time.sleep(15)

                if browser.find_element_by_xpath(
                        "/html/body/form/div[3]/div/div[2]/span/main/div[1]/div/div/div[3]/div[3]/div/div/div[1]"
                        "/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div[1]") is not None:
                    content = browser.find_element_by_xpath(
                        "/html/body/form/div[3]/div/div[2]/span/main/div[1]/div/div/div[3]/div[3]/div/div/div[1]"
                        "/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div[1]")

                    number_of_pages_with_coma = int(content
                                                    .text
                                                    .replace(' ', '')
                                                    .split("of")[1]
                                                    ) / 60

                    if int(str(number_of_pages_with_coma).split(".")[1][:1]) < 5:
                        number_of_pages += round(number_of_pages_with_coma) + 1
                        print('number_of_pages : ' + str(number_of_pages))
                        break
                    elif int(str(number_of_pages_with_coma).split(".")[1][:1]) >= 5:
                        number_of_pages += round(number_of_pages_with_coma)
                        print('number_of_pages : ' + str(number_of_pages))
                        break
                else:
                    print("error pages")

                time.sleep(5)

            for i in range(1, number_of_pages + 1):
                try:
                    url_page = "https://www.jerseylaw.je/laws/current/Pages/search.aspx?current=n_" \
                               + str(i) \
                               + "_n&size=n_60_n&filters%5B0%5D%5Bfield%5D=TitleStartsWith&filters%5B0%5D%5Bvalues%5D%5B0%5D=" \
                               + letter

                    time.sleep(3)

                    while True:
                        try:
                            browser.get(url_page)
                            print("browser.get(url_page)")

                            time.sleep(15)

                            if "Jersey" in browser.title:
                                print('"Jersey" in browser.title')
                                break
                        except Exception as e:
                            print('error browser.get(url_page) : ' + str(e))

                    all_law = browser.find_elements_by_class_name("resultRow")
                    print('all_law = browser.find_elements_by_class_name("resultRow")')

                    time.sleep(5)

                    laws_link = []

                    for law in all_law:
                        link = law.find_element_by_tag_name('a').get_attribute('href')
                        print('link : ' + str(link))
                        laws_link.append(link)

                    time.sleep(5)

                    for law_link in laws_link:
                        try:
                            time.sleep(3)

                            browser.get(law_link)
                            print("browser.get(law_link)")

                            time.sleep(20)

                            title = browser.find_element_by_xpath(
                                "/html/body/form/div[3]/div/div[2]/div[4]/div/div/span/span[7]"
                            ).text.replace(' ', '').replace('(', '').replace(')', '') + ".pdf"
                            print("title : " + title)

                            url_pdf = law_link.replace('Pages', 'PDFs').replace('aspx', 'pdf')

                            while True:
                                try:
                                    response = requests.get(url_pdf, timeout=60)

                                    time.sleep(10)

                                    if response.status_code == 200:
                                        filename = title[:20] + ".pdf"

                                        pdf = open(path + "\\" + filename, 'wb')

                                        pdf.write(response.content)

                                        pdf.close()

                                        print("File " + filename + " downloaded")

                                        time.sleep(5)

                                        break
                                except Exception as e:
                                    print('error response pdf file : ' + str(e))
                        except Exception as e:
                            print('error : ' + str(e))

                        time.sleep(5)
                except Exception as e:
                    print('error url_page : ' + str(e))
            time.sleep(5)

            browser.quit()
            print("browser.quit()")

            time.sleep(10)

            subprocess.call("taskkill /F /IM geckodriver.exe")
            subprocess.call("taskkill /F /IM firefox.exe")

            time.sleep(10)

            print("run_ccleaner")
            os.system("set ccleaner='C:\\Program Files\\CCleaner\\CCleaner.exe'")
            os.system("start ccleaner /AUTO")

            time.sleep(60)

    # ok
    def test_kill_some_processes(self):
        print("test_kill_some_processes")

        subprocess.call("taskkill /F /IM geckodriver.exe")
        subprocess.call("taskkill /F /IM firefox.exe")


if __name__ == '__main__':
    unittest.main()
