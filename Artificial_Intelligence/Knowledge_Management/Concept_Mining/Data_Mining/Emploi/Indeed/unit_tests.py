import time
import unittest
import pymysql
import requests
from bs4 import BeautifulSoup
import xlsxwriter

password = 'azerAZER123098,,,'


class UnitTestsDataMiningIndeed(unittest.TestCase):
    # ok
    def test_extract_email_company_from_one_page(self):
        print('test_extract_company_name_from_one_page')

        i = 0

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://fr.indeed.com/viewjob?jk=416f70f39be0ba29&q=d%C3%A9veloppeur+python&l=France&from=web&advn=4923530667854545&adid=380064358&ad=-6NYlbfkN0BcSgjHAloKFSb6oFQeDAHQMolsqTraflMY4y6oMn0jpfVGTOAHCKDjPhEGN6OAyfVtLG5hgCsQFUdF4Ozysp-x9Yd-yQm2AYwm1CXxdzm7OXadYQsg_eO9f2Y2dTvYTG-Tg08KbahDLjroIAxWv-vx2vYs9S_bxivwhR1Eu__BO3TP0vRvPqz3PU5sKOYGnqWSKFKkftGr_O3AfQg2uR0zSVhEpwWYOPyB_XcWRX2bEUEQsoi8nSf3rTkPxhAOIRf4Nqljsm7oZ_n_duwm1r4pHvCPBhrhYwfhJk9oT730gvx2F24KbZO3BPCbsTrSNZz_3d28aDCweWSi637w9yrhVx_5Ge9A9WWi7obz4LbJddpAowgJYbTyLv9XuLgscpI%3D&pub=4a1b367933fd867b19b072952f68dceb&vjs=3"

        html = requests.get(url, headers=headers)

        time.sleep(3)

        soup = BeautifulSoup(html.content, 'html.parser')

        prefixes = ['contact@', 'info@', 'hello@']

        suffixes = ['.net', '.fr', '.com']

        if soup.find("div", {"class": "jobsearch-InlineCompanyRating"}) is not None:
            email_company = soup.find("div", {"class": "jobsearch-InlineCompanyRating"}).text.lower().replace(" ", "")

            for prefixe in prefixes:
                for suffixe in suffixes:
                    print(str(i) + " _ email_company : " + prefixe + email_company + suffixe)

                    i += 1
        else:
            print("no email_company")

    # ok
    def test_extract_all_email_company_from_one_page_result(self):
        print('test_extract_all_email_company_from_one_page_result')

        i = 0

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://fr.indeed.com/jobs?q=d%C3%A9veloppeur+python&l=France&start=0"

        html = requests.get(url, headers=headers)

        time.sleep(3)

        soup = BeautifulSoup(html.content, 'html.parser')

        prefixes = ['contact@', 'info@', 'hello@']

        suffixes = ['.net', '.fr', '.com']

        if soup.find("span", {"class": "companyName"}) is not None:

            companies = soup.find_all("span", {"class": "companyName"})

            for company in companies:
                email_company = company.text.lower()\
                    .replace(" ", "")\
                    .replace("\t", "")\
                    .replace("\r", "")\
                    .replace("\n", "")

                for prefixe in prefixes:
                    for suffixe in suffixes:
                        print(str(i) + " _ email_company : " + prefixe + email_company + suffixe)

                        i += 1
        else:
            print("no email_company")

    # ok
    def test_extract_all_email_company_from_all_page_result_into_mysql(self):
        print('test_extract_all_email_company_from_all_page_result_into_mysql')

        i_1 = 0

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        for i in range(0, 250):
            url = "https://fr.indeed.com/jobs?q=d%C3%A9veloppeur+python&l=France&start=" + str(10*i)

            html = requests.get(url, headers=headers)

            time.sleep(5)

            soup = BeautifulSoup(html.content, 'html.parser')

            prefixes = ['contact@', 'info@', 'hello@']

            suffixes = ['.net', '.fr', '.com']

            if soup.find("span", {"class": "companyName"}) is not None:

                companies = soup.find_all("span", {"class": "companyName"})

                for company in companies:
                    company_name = company.text.lower()\
                        .replace(" ", "")\
                        .replace("\t", "")\
                        .replace("\r", "")\
                        .replace("\n", "")\
                        .replace("é", "e")\
                        .replace("è", "e")\
                        .replace("à", "a")\
                        .replace("ô", "o")\
                        .replace("ö", "o")\
                        .replace("î", "i")

                    for prefixe in prefixes:
                        for suffixe in suffixes:
                            email_company = prefixe + company_name + suffixe

                            x = {
                                'email': email_company
                            }

                            try:
                                connection = pymysql.connect(
                                    host='localhost',
                                    port=3306,
                                    user='root',
                                    password='azerAZER123098,,,',
                                    db='indeed',
                                    charset='utf8mb4',
                                    cursorclass=pymysql.cursors.DictCursor
                                )

                                with connection.cursor() as cursor:
                                    try:
                                        sql = "INSERT INTO `emails` (`emails`) VALUE (%s)"

                                        cursor.execute(sql, (
                                            x.get('email')
                                        ))

                                        connection.commit()

                                        print(str(i_1) + ' _ Email : ' + x.get('email') + ' : ok')

                                        connection.close()
                                    except Exception as e:
                                        print(str(i_1) + " _ The record already exists (email " + x.get('email')
                                              + ") : "
                                              + str(e))
                                        connection.close()
                            except Exception as e:
                                print(str(i_1) + " _ Problem connection MySQL : " + str(e))

                            i_1 += 1
            else:
                print("no email_company")

    # ok
    def test_extract_all_companies_from_all_page_result_into_mysql(self):
        print('test_extract_all_companies_from_all_page_result_into_mysql')

        i_1 = 0

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/51.0.2704.103'
        }

        for i in range(0, 68):
            url = "https://fr.indeed.com/emplois?q=%C3%A9nergie&l=%C3%8Ele-de-France&start=" + str(10*i)

            html = requests.get(url, headers=headers)

            time.sleep(5)

            soup = BeautifulSoup(html.content, 'html.parser')

            if soup.find("span", {"class": "companyName"}) is not None:

                companies = soup.find_all("span", {"class": "companyName"})

                for company in companies:
                    company_name = company.text.lower()\
                        .replace("\t", "")\
                        .replace("\r", "")\
                        .replace("\n", "")

                    x = {
                        'company': company_name
                    }

                    try:
                        connection = pymysql.connect(
                            host='localhost',
                            port=3306,
                            user='root',
                            password='azerAZER123098,,,',
                            db='indeed',
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor
                        )

                        with connection.cursor() as cursor:
                            try:
                                sql = "INSERT INTO `companies` (`company`) VALUE (%s)"

                                cursor.execute(sql, (
                                    x.get('company')
                                ))

                                connection.commit()

                                print(str(i_1) + ' _ Company : ' + x.get('company') + ' : ok')

                                connection.close()
                            except Exception as e:
                                print(str(i_1) + " _ The record already exists (company " + x.get('company')
                                      + ") : "
                                      + str(e))
                                connection.close()
                    except Exception as e:
                        print(str(i_1) + " _ Problem connection MySQL : " + str(e))

                    i_1 += 1
            else:
                print("no company")

    #
    def test_extract_all_ad_link_from_one_page(self):
        print('test_extract_all_ad_link_from_one_page')

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://fr.indeed.com/jobs?q=developpeur+python&l=%C3%8Ele-de-France&start=10"

        html = requests.get(url, headers=headers)

        time.sleep(3)

        soup = BeautifulSoup(html.content, 'html.parser')

        if soup.find("a", {"class": "tapItem"}) is not None:
            all_a = soup.find_all("a", {"class": "tapItem"})

            for a in all_a:
                link = "https://fr.indeed.com" + a.get('href')
                print("link of the ad : " + link)
        else:
            print("no ads")

    # ok
    def test_extract_all_ad_link_from_all_pages(self):
        print('test_extract_all_ad_link_from_all_pages')

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        for i in range(0, 63):
            start = str(10*i)

            url = "https://fr.indeed.com/jobs?q=d%C3%A9veloppeur%20python&l=%C3%8Ele-de-France&jt=permanent&start=" \
                  + start

            print(url)

            time.sleep(7)

            html = requests.get(url, headers=headers)

            soup = BeautifulSoup(html.content, 'html.parser')

            if soup.find("a", {"class": "tapItem"}) is not None:
                all_a = soup.find_all("a", {"class": "tapItem"})

                for a in all_a:
                    link = "https://fr.indeed.com" + a.get('href')

                    html_link = requests.get(link, headers=headers)

                    soup_link = BeautifulSoup(html_link.content, 'html.parser')

                    try:
                        if soup_link.find("div", {'class': 'jobsearch-JobInfoHeader-title-container'}) is not None:
                            if "python" in soup_link.find("div", {'class': 'jobsearch-JobInfoHeader-title-container'}).text.lower():
                                link_postuler = soup_link.select_one("#applyButtonLinkContainer").find("a").get('href')

                                html_link_postuler = requests.get(link_postuler, headers=headers)

                                soup_link_postuler = BeautifulSoup(html_link_postuler.content, 'html.parser')

                                if 'indeed' in soup_link_postuler.find('body').text.lower():
                                    print("yes python for link of the ad : " + link)
                                else:
                                    print("1 no python for link of the ad : " + link)
                            else:
                                print("2 no python for link of the ad : " + link)
                    except Exception as e:
                        print('error for ' + str(e))

                    time.sleep(7)
            else:
                print("no ads")

    # ok
    def test_extract_all_ad_link_from_all_pages_into_excel(self):
        print('test_extract_all_ad_link_from_all_pages_into_excel')

        filename = "urls_indeed.xlsx"

        workbook = xlsxwriter.Workbook(filename)

        worksheet_yes = workbook.add_worksheet('yes')

        worksheet_no = workbook.add_worksheet('no')

        worksheet_yes.write(0, 0, 'url')

        worksheet_no.write(0, 0, 'url')

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        i1 = 1

        i2 = 1

        for i in range(0, 63):
            start = str(10*i)

            url = "https://fr.indeed.com/jobs?q=d%C3%A9veloppeur%20python&l=%C3%8Ele-de-France&jt=permanent&start=" \
                  + start

            print(url)

            html = requests.get(url, headers=headers)

            soup = BeautifulSoup(html.content, 'html.parser')

            time.sleep(7)

            if soup.find("a", {"class": "jcs-JobTitle"}) is not None:
                all_a = soup.find_all("a", {"class": "jcs-JobTitle"})

                for a in all_a:
                    link = "https://fr.indeed.com" + a.get('href')

                    html_link = requests.get(link, headers=headers)

                    soup_link = BeautifulSoup(html_link.content, 'html.parser')

                    try:
                        if soup_link.find("h1", {'class': 'jobsearch-JobInfoHeader-title'}) is not None:
                            if "python" in soup_link.find("h1", {'class': 'jobsearch-JobInfoHeader-title'})\
                                    .text.lower():
                                print("yes python for link of the ad : " + link)
                                worksheet_yes.write(i1, 0, link)
                                i1 += 1
                            else:
                                print("no python for link of the ad : " + link)
                                worksheet_no.write(i2, 0, link)
                                i2 += 1
                    except Exception as e:
                        print('error for ' + str(e))

                    time.sleep(7)

            else:
                print("no ads")

        workbook.close()

    # ok
    def test_extract_all_ad_link_from_all_pages_into_mysql(self):
        print('test_extract_all_ad_link_from_all_pages_into_mysql')

        i_1 = 0

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/51.0.2704.103'
        }

        for i in range(0, 58):
            start = str(10*i)

            url = "https://fr.indeed.com/jobs?q=developpeur+python&l=%C3%8Ele-de-France&start=" + start

            print(url)

            time.sleep(5)

            html = requests.get(url, headers=headers)

            soup = BeautifulSoup(html.content, 'html.parser')

            if soup.find("a", {"class": "tapItem"}) is not None:
                all_a = soup.find_all("a", {"class": "tapItem"})

                for a in all_a:
                    link = "https://fr.indeed.com" + a.get('href')

                    x = {
                        'link': link
                    }

                    try:
                        connection = pymysql.connect(
                            host='localhost',
                            port=3306,
                            user='root',
                            password=password,
                            db='indeed',
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor
                        )

                        with connection.cursor() as cursor:
                            try:
                                sql = "INSERT INTO `links` (`link`) VALUE (%s)"

                                cursor.execute(sql, (x.get('link')))

                                connection.commit()

                                print(
                                    str(i_1)
                                    + ' _ link : '
                                    + x.get('link')
                                    + ' : ok'
                                )

                                connection.close()
                            except Exception as e:
                                print(
                                    str(i_1)
                                    + " _ The record already exists (link "
                                    + x.get('link')
                                    + ") : "
                                    + str(e)
                                )

                                connection.close()
                    except Exception as e:
                        print(str(i_1) + " _ Problem connection MySQL for table 'link' : " + str(e))

                    i_1 += 1
            else:
                print("no ads")

    # ok
    def test_extract_all_ad_link_from_all_pages_with_keywords_in_title_into_mysql(self):
        print('test_extract_all_ad_link_from_all_pages_with_keywords_in_title_into_mysql')

        i_1 = 0

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/51.0.2704.103'
        }

        for i in range(0, 58):
            start = str(10*i)

            url = "https://fr.indeed.com/jobs?q=developpeur+python&l=%C3%8Ele-de-France&start=" + start

            print(url)

            time.sleep(5)

            html = requests.get(url, headers=headers)

            soup = BeautifulSoup(html.content, 'html.parser')

            if soup.find("a", {"class": "tapItem"}) is not None:
                all_a = soup.find_all("a", {"class": "tapItem"})

                for a in all_a:
                    link = "https://fr.indeed.com" + a.get('href')

                    html_ad = requests.get(link, headers=headers)

                    soup_ad = BeautifulSoup(html_ad.content, 'html.parser')

                    if soup_ad.find("h1", {'class': 'jobsearch-JobInfoHeader-title'}) is not None:
                        title_ad = soup_ad.find("h1", {'class': 'jobsearch-JobInfoHeader-title'}).text.lower()

                        if "python" in title_ad:
                            x = {
                                'link': link
                            }

                            try:
                                connection = pymysql.connect(
                                    host='localhost',
                                    port=3306,
                                    user='root',
                                    password=password,
                                    db='indeed',
                                    charset='utf8mb4',
                                    cursorclass=pymysql.cursors.DictCursor
                                )

                                with connection.cursor() as cursor:
                                    try:
                                        sql = "INSERT INTO `links` (`link`) VALUE (%s)"

                                        cursor.execute(sql, (x.get('link')))

                                        connection.commit()

                                        print(
                                            str(i_1)
                                            + ' _ link : '
                                            + x.get('link')
                                            + ' : ok'
                                        )

                                        connection.close()
                                    except Exception as e:
                                        print(
                                            str(i_1)
                                            + " _ The record already exists (link "
                                            + x.get('link')
                                            + ") : "
                                            + str(e)
                                        )

                                        connection.close()
                            except Exception as e:
                                print(str(i_1) + " _ Problem connection MySQL for table 'link' : " + str(e))

                            i_1 += 1

                            time.sleep(3)
                        else:
                            print("no python in title_ad")
                    else:
                        print('no h1 class jobsearch-JobInfoHeader-title')
            else:
                print("no ads")

    # ok
    def test_extract_all_ad_link_from_all_pages_with_keywords_in_postuler_button_into_mysql(self):
        print('test_extract_all_ad_link_from_all_pages_with_keywords_in_postuler_button_into_mysql')

        i_1 = 0

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/51.0.2704.103'
        }

        for i in range(0, 63):
            start = str(10*i)

            url = "https://fr.indeed.com/jobs?q=d%C3%A9veloppeur%20python&l=%C3%8Ele-de-France&jt=permanent&start=" \
                  + start

            print(url)

            time.sleep(5)

            html = requests.get(url, headers=headers)

            soup = BeautifulSoup(html.content, 'html.parser')

            if soup.find("a", {"class": "tapItem"}) is not None:
                all_a = soup.find_all("a", {"class": "tapItem"})

                for a in all_a:
                    link = "https://fr.indeed.com" + a.get('href')

                    html_ad = requests.get(link, headers=headers)

                    soup_ad = BeautifulSoup(html_ad.content, 'html.parser')

                    if soup_ad.select_one("#jobsearch-ViewJobButtons-container") is not None:
                        postuler_button_ad = soup_ad.select_one("#jobsearch-ViewJobButtons-container").text.lower()

                        if "simplifié" in postuler_button_ad:
                            x = {
                                'link': link
                            }

                            try:
                                connection = pymysql.connect(
                                    host='localhost',
                                    port=3306,
                                    user='root',
                                    password=password,
                                    db='indeed',
                                    charset='utf8mb4',
                                    cursorclass=pymysql.cursors.DictCursor
                                )

                                with connection.cursor() as cursor:
                                    try:
                                        sql = "INSERT INTO `links` (`link`) VALUE (%s)"

                                        cursor.execute(sql, (x.get('link')))

                                        connection.commit()

                                        print(
                                            str(i_1)
                                            + ' _ link : '
                                            + x.get('link')
                                            + ' : ok'
                                        )

                                        connection.close()
                                    except Exception as e:
                                        print(
                                            str(i_1)
                                            + " _ The record already exists (link "
                                            + x.get('link')
                                            + ") : "
                                            + str(e)
                                        )

                                        connection.close()
                            except Exception as e:
                                print(str(i_1) + " _ Problem connection MySQL for table 'link' : " + str(e))

                            i_1 += 1

                            time.sleep(3)
                        else:
                            print("no simplifié in postuler_button_ad")
                    else:
                        print('no div id applyButtonLinkContainer')
            else:
                print("no ads")

    # ok
    def test_print_ten_multiplication(self):
        print('test_print_ten_multiplication')

        for i in range(0, 78):
            print(str(10*i))

    #
    def test_see_postuler_button_from_one_ad(self):
        print('test_see_postuler_button_from_one_ad')

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://fr.indeed.com/voir-emploi?cmp=WeTrouveIT&from=iaBackPress&jk=72f4367ffa5964d2&q=freelance%20informatique&t=D%C3%A9veloppeur%20Golang%20Exp%C3%A9riment%C3%A9%20Freelance&vjs=3"

        # Request the content of a page from the url
        html = requests.get(url, headers=headers)

        time.sleep(10)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.content, 'html.parser')

        if soup.find("div", {"class": "jobsearch-IndeedApplyButton-contentWrapper"}) is not None:
            title = soup\
                .find("div", {"class": "jobsearch-IndeedApplyButton-contentWrapper"})\
                .find('span')\
                .text

            if title == "Postuler":
                print("button Postuler ok")
            else:
                print("no button Postuler")

    #
    def test_extract_all_link_from_one_page_with_postuler_button(self):
        print('test_extract_all_link_from_all_pages_with_postuler_button')

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://fr.indeed.com/jobs?q=freelance+informatique&l=France&start=10"

        html = requests.get(url, headers=headers)

        time.sleep(10)

        soup = BeautifulSoup(html.content, 'html.parser')

        if soup.find("a", {"data-tn-element": "jobTitle"}) is not None:
            all_a = soup.find_all("a", {"data-tn-element": "jobTitle"})

            for a in all_a:
                link = "https://fr.indeed.com" + a.get('href')

                html = requests.get(link, headers=headers)

                time.sleep(10)

                soup = BeautifulSoup(html.content, 'html.parser')

                if soup.find("div", {"class": "jobsearch-IndeedApplyButton-contentWrapper"}) is not None:
                    title = soup \
                        .find("div", {"class": "jobsearch-IndeedApplyButton-contentWrapper"}) \
                        .find('span') \
                        .text

                    if title == "Postuler":
                        print("button Postuler ok : " + link)
                    else:
                        print("no button Postuler")
        else:
            print("no ads")

    #
    def test_extract_all_link_from_all_pages_with_postuler_button(self):
        print('test_extract_all_link_from_all_pages_with_postuler_button')

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        for i in range(0, 77):
            print('page : ' + str(i))

            start = str(10*i)

            url = "https://fr.indeed.com/jobs?q=freelance+informatique&l=France&start=" + start

            # Request the content of a page from the url
            html = requests.get(url, headers=headers)

            time.sleep(10)

            # Parse the content of html_doc
            soup = BeautifulSoup(html.content, 'html.parser')

            if soup.find("a", {"data-tn-element": "jobTitle"}) is not None:
                all_a = soup.find_all("a", {"data-tn-element": "jobTitle"})

                for a in all_a:
                    link = "https://fr.indeed.com" + a.get('href')

                    # Request the content of a page from the url
                    html = requests.get(link, headers=headers)

                    time.sleep(10)

                    # Parse the content of html_doc
                    soup = BeautifulSoup(html.content, 'html.parser')

                    if soup.find("div", {"class": "jobsearch-IndeedApplyButton-contentWrapper"}) is not None:
                        title = soup \
                            .find("div", {"class": "jobsearch-IndeedApplyButton-contentWrapper"}) \
                            .find('span') \
                            .text

                        if title == "Postuler":
                            print("button Postuler ok : " + link)
                        else:
                            print("no button Postuler")
            else:
                print("no ads")


if __name__ == '__main__':
    unittest.main()
