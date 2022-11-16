import tracemalloc
import unittest
import warnings
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import pymysql
import requests
from bs4 import BeautifulSoup
import xlsxwriter
import time
from torrequest import TorRequest


class UnitTestsDataMiningLegifrance(unittest.TestCase):
    def test_extract_articles_to_excel(self):
        url_du_sommaire = "https://www.legifrance.gouv.fr/affichCode.do?cidTexte=LEGITEXT000023983208&dateTexte=20200306"

        titre = "Code de l'énergie"

        # Request the content of a page from the url
        html = requests.get(url_du_sommaire)

        # Parse the content of html
        soup = BeautifulSoup(html.content, 'html.parser')

        if soup.find_all("span", {"class": "codeLienArt"}) is not None:
            articles = soup.find_all("span", {"class": "codeLienArt"})

            # Create a workbook and add a worksheet.
            workbook = xlsxwriter.Workbook(titre.replace(" ", "_") + '.xlsx')
            worksheet = workbook.add_worksheet("Articles")

            # Start from the first cell. Rows and columns are zero indexed.
            row = 0
            col = 0

            worksheet.write(row, col, "Articles")

            for article in articles:
                row += 1
                print(article.find("a").text)
                worksheet.write(row, col, article.find("a").text)

            workbook.close()

    def test_extract_text_of_one_article_of_one_code_in_force(self):
        print("test_text_of_one_article")

        url_of_one_article = "https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000030437933"

        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36 Edg/88.0.705.81',
            'referer': 'https://www.google.fr/',
            'authority': 'www.legifrance.gouv.fr',
            'method': 'GET',
            'path': url_of_one_article.replace("https://www.legifrance.gouv.fr", ""),
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'fr,fr-FR;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'cache-control': 'max-age=0',
            'cookie': 'visid_incap_1235873=TtIIancVSD27jnwuHQ1yDpgiPmAAAAAAQUIPAAAAAAA8+76C1vti3Fo3Ut2qItUj; incap_ses_466_1235873=Ir8HB9MSfDcDN5ov3pB3BpgiPmAAAAAA6q6ogRf3HiGNOrmqGgrMXw==; tarteaucitron=!id=a5b4d4cbb5dded9c-1ff2d8bb-aa998d65-5c5326d452f34ba28b3ff1c5!atinternet=true!hotjar=false; lf-demo-accueil=1; JSESSIONID=2A6A5311ECFF2DFF64EFF02FDA32EC8A; LB_APP_ROUTE=.4; LB_FRONT_ROUTE=.1.2; lf-demo-rr-codes=1; seeAbrogated-LEGITEXT000006074069=false; lf-demo-consult-codes-sommaire=1; seeAbrogated-LEGITEXT000006075116=false; seeAbrogated-LEGITEXT000006073984=false; nlbi_1235873=se4TXoAimnQAEhF5jJoYvAAAAADLJalA4a5VX/shfGeDCrg4',
            'dnt': '1',
            'if-none-match': '89dfa94b',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1'
        }

        # Request the content of a page from the url
        html_of_one_article = requests.get(url_of_one_article, headers=headers)

        # Parse the content of html_doc
        soup = BeautifulSoup(html_of_one_article.content, 'html.parser')

        if soup.find('article') is not None:
            text = soup.find('article')\
                .text\
                .replace('Versions', '')\
                .replace('Liens relatifs', '') \
                .replace('\t', '') \
                .replace('\r', '') \
                .replace('\n', '')
            print(text)
        else:
            print("no article")

    def test_extract_all_articles_from_one_code_in_force(self):
        print("test_extract_all_articles_from_one_code_in_force")

        url_of_one_code_in_force = "https://www.legifrance.gouv.fr/codes/texte_lc/LEGITEXT000006074069"

        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36 Edg/88.0.705.81',
            'referer': 'https://www.google.fr/',
            'authority': 'www.legifrance.gouv.fr',
            'method': 'GET',
            'path': url_of_one_code_in_force.replace("https://www.legifrance.gouv.fr", ""),
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'fr,fr-FR;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'cache-control': 'max-age=0',
            'cookie': 'visid_incap_1235873=TtIIancVSD27jnwuHQ1yDpgiPmAAAAAAQUIPAAAAAAA8+76C1vti3Fo3Ut2qItUj; incap_ses_466_1235873=Ir8HB9MSfDcDN5ov3pB3BpgiPmAAAAAA6q6ogRf3HiGNOrmqGgrMXw==; tarteaucitron=!id=a5b4d4cbb5dded9c-1ff2d8bb-aa998d65-5c5326d452f34ba28b3ff1c5!atinternet=true!hotjar=false; lf-demo-accueil=1; JSESSIONID=2A6A5311ECFF2DFF64EFF02FDA32EC8A; LB_APP_ROUTE=.4; LB_FRONT_ROUTE=.1.2; lf-demo-rr-codes=1; seeAbrogated-LEGITEXT000006074069=false; lf-demo-consult-codes-sommaire=1; seeAbrogated-LEGITEXT000006075116=false; seeAbrogated-LEGITEXT000006073984=false; nlbi_1235873=se4TXoAimnQAEhF5jJoYvAAAAADLJalA4a5VX/shfGeDCrg4',
            'dnt': '1',
            'if-none-match': '89dfa94b',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1'
        }

        time.sleep(3)

        # Request the content of a page from the url
        html = requests.get(url_of_one_code_in_force, headers=headers)

        print(html.text)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.content, 'html.parser')

        if soup.find('a', {'class': 'articleLink'}) is not None:
            all_articles = soup.find_all('a', {'class': 'articleLink'})

            for article in all_articles:
                title = "Article " + article.get('data-na')
                link = "https://www.legifrance.gouv.fr/codes/article_lc/" + article.get('id').replace('art', '')
                print(title + " : " + link)
        else:
            print("no a class articleLink")

    def test_extract_text_of_one_law(self):
        print('test_extract_text_of_one_law')

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url_of_one_law = "https://www.legifrance.gouv.fr/loda/id/JORFTEXT000038029184?tab_selection=lawarticledecree&searchField=ALL&query=*&searchProximity=&searchType=ALL&isAdvancedResult=&isAdvancedResult=&dateSignature=&datePublication=&nature=LOI&typeRecherche=date&dateVersion=16%2F01%2F2021&typePagination=DEFAUT&sortValue=SIGNATURE_DATE_DESC&pageSize=100&page=2&tab_selection=lawarticledecree#lois"

        # Request the content of a page from the url
        html_of_one_article = requests.get(url_of_one_law, headers=headers)

        # Parse the content of html_doc
        soup = BeautifulSoup(html_of_one_article.content, 'html.parser')

        title = ""
        text = ""

        if soup.find("h1", {'class': 'main-title'}) is not None:
            title += soup.find("h1", {'class': 'main-title'}).text
        else:
            print("no h1 class main-title")

        if soup.find("div", {'class': 'page-content'}) is not None:
            text += soup.find("div", {'class': 'page-content'}).text
        else:
            print("no div class page-content")

        print(title + " " + text)

    def test_extract_all_laws_from_one_consolidated_laws(self):
        print("test_extract_all_laws_from_one_search")

        cookie = "visid_incap_1235873=lUTwT3V3TS+mLMlge/Jy3AdOPmAAAAAAQUIPAAAAAABUdRnLRltJVGEq8Qm1zkND; incap_ses_466_1235873=vOP1D5KoPQmx5cIv3pB3BgdOPmAAAAAADm9/Oj/bR7QOydKalErswA==; tarteaucitron=!id=6007ec4d07ae1f86-38af0aec-d774188e-cf4513f115b317ff9cb62113!atinternet=true!hotjar=false; lf-demo-accueil=1; JSESSIONID=D412E97F9A9C4A26680A838C7D02E7FE; LB_APP_ROUTE=.5; LB_FRONT_ROUTE=.2.2; nlbi_1235873=I7HmQ1f1elnnJ2TtjJoYvAAAAADvCgXYI7urb38UiupI0281"

        before_url = "https://www.legifrance.gouv.fr/search/lois?tab_selection=lawarticledecree&searchField=ALL&query=*&searchProximity=&searchType=ALL&isAdvancedResult=&isAdvancedResult=&dateSignature=&datePublication=&nature=LOI&typeRecherche=date&dateVersion=02%2F03%2F2021&typePagination=DEFAUT&sortValue=SIGNATURE_DATE_DESC&pageSize=100&page="

        after_url = "&tab_selection=lawarticledecree#lois"

        url_of_all_laws_from_one_search = before_url + "2" + after_url

        headers_from_one_search = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36 Edg/88.0.705.81',
            'referer': 'https://www.google.fr/',
            'authority': 'www.legifrance.gouv.fr',
            'method': 'GET',
            'path': url_of_all_laws_from_one_search.replace("https://www.legifrance.gouv.fr", ""),
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'fr,fr-FR;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'cache-control': 'max-age=0',
            'cookie': cookie,
            'dnt': '1',
            'if-none-match': '89dfa94b',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1'
        }

        time.sleep(3)

        # Request the content of a page from the url
        html_of_one_article = requests.get(url_of_all_laws_from_one_search, headers=headers_from_one_search)

        # Parse the content of html_doc
        soup_from_one_search = BeautifulSoup(html_of_one_article.content, 'html.parser')

        number_of_pages = 0

        if soup_from_one_search.find("p", {"class": "nb-result head-filter-title"}) is not None:
            number_of_pages_with_coma = int(soup_from_one_search.find("p", {"class": "nb-result head-filter-title"})
                                            .text
                                            .replace(' résultat(s) trouvé(s)', '')
                                            ) / 100

            if int(str(number_of_pages_with_coma).split(".")[1][:1]) < 5:
                number_of_pages += round(number_of_pages_with_coma) + 1
                print('number_of_pages : ' + str(number_of_pages))

            elif int(str(number_of_pages_with_coma).split(".")[1][:1]) >= 5:
                number_of_pages += round(number_of_pages_with_coma)
                print('number_of_pages : ' + str(number_of_pages))

            for i in range(1, number_of_pages + 1):
                url_of_one_page = before_url + str(i) + after_url

                headers_of_one_page = {
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36 Edg/88.0.705.81',
                    'referer': 'https://www.google.fr/',
                    'authority': 'www.legifrance.gouv.fr',
                    'method': 'GET',
                    'path': url_of_one_page.replace("https://www.legifrance.gouv.fr", ""),
                    'scheme': 'https',
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'accept-encoding': 'gzip, deflate, br',
                    'accept-language': 'fr,fr-FR;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
                    'cache-control': 'max-age=0',
                    'cookie': cookie,
                    'dnt': '1',
                    'if-none-match': '89dfa94b',
                    'sec-fetch-dest': 'document',
                    'sec-fetch-mode': 'navigate',
                    'sec-fetch-site': 'none',
                    'sec-fetch-user': '?1',
                    'upgrade-insecure-requests': '1'
                }

                print(url_of_one_page)

                time.sleep(3)

                # Request the content of a page from the url
                html_of_one_article = requests.get(url_of_one_page, headers=headers_of_one_page)

                # Parse the content of html_doc
                soup_of_one_article = BeautifulSoup(html_of_one_article.content, 'html.parser')

                if soup_of_one_article.find("article", {"class": "result-item"}) is not None:
                    all_laws = soup_of_one_article.find_all("article", {"class": "result-item"})

                    for law in all_laws:
                        if law.find('h2', {'class': 'title-result-item'}) is not None:
                            title = law.find('h2', {'class': 'title-result-item'}).find('a').text
                            link = "https://www.legifrance.gouv.fr/loda/id/" + law.find('h2', {'class': 'title-result-item'}).get('data-id')
                            print(title + " : " + link)
                        else:
                            print("no h2 title-result-item")
                else:
                    print("no article result-item")
        else:
            print("no pages at all")

    def test_extract_text_of_one_article_of_one_consolidated_laws(self):
        print("test_extract_text_of_one_article_of_one_consolidated_laws")

        cookie = ""

        url_of_one_article_of_one_consolidated_laws = "https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000043179588"

        headers_of_one_article_of_one_consolidated_laws = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36 Edg/88.0.705.81',
            'referer': 'https://www.google.fr/',
            'authority': 'www.legifrance.gouv.fr',
            'method': 'GET',
            'path': url_of_one_article_of_one_consolidated_laws.replace("https://www.legifrance.gouv.fr", ""),
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'fr,fr-FR;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'cache-control': 'max-age=0',
            'cookie': cookie,
            'dnt': '1',
            'if-none-match': '89dfa94b',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1'
        }

        # Request the content of a page from the url
        html_of_one_article_of_one_consolidated_laws = requests.get(url_of_one_article_of_one_consolidated_laws, headers=headers_of_one_article_of_one_consolidated_laws)

        # Parse the content of html_doc
        soup_of_one_article_of_one_consolidated_laws = BeautifulSoup(html_of_one_article_of_one_consolidated_laws.content, 'html.parser')

        if soup_of_one_article_of_one_consolidated_laws.find('article') is not None:
            text = soup_of_one_article_of_one_consolidated_laws.find('article')\
                .text\
                .replace('Versions', '')\
                .replace('Liens relatifs', '') \
                .replace('\t', '') \
                .replace('\r', '') \
                .replace('\n', '')

            print(text)
        else:
            print("no article")

    def test_extract_all_articles_from_one_consolidated_law_in_force(self):
        print("test_extract_all_articles_from_one_consolidated_law_in_force")

        cookie = "visid_incap_1235873=lUTwT3V3TS+mLMlge/Jy3AdOPmAAAAAAQUIPAAAAAABUdRnLRltJVGEq8Qm1zkND; incap_ses_466_1235873=vOP1D5KoPQmx5cIv3pB3BgdOPmAAAAAADm9/Oj/bR7QOydKalErswA==; tarteaucitron=!id=6007ec4d07ae1f86-38af0aec-d774188e-cf4513f115b317ff9cb62113!atinternet=true!hotjar=false; lf-demo-accueil=1; JSESSIONID=D412E97F9A9C4A26680A838C7D02E7FE; LB_APP_ROUTE=.5; LB_FRONT_ROUTE=.2.2; nlbi_1235873=I7HmQ1f1elnnJ2TtjJoYvAAAAADvCgXYI7urb38UiupI0281"

        url_of_one_consolidated_law_in_force = "https://www.legifrance.gouv.fr/loda/id/JORFTEXT000043179225"

        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36 Edg/88.0.705.81',
            'referer': 'https://www.google.fr/',
            'authority': 'www.legifrance.gouv.fr',
            'method': 'GET',
            'path': url_of_one_consolidated_law_in_force.replace("https://www.legifrance.gouv.fr", ""),
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'fr,fr-FR;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'cache-control': 'max-age=0',
            'cookie': cookie,
            'dnt': '1',
            'if-none-match': '89dfa94b',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1'
        }

        time.sleep(3)

        # Request the content of a page from the url
        html_of_one_consolidated_law_in_force = requests.get(url_of_one_consolidated_law_in_force, headers=headers)

        # Parse the content of html_doc
        soup = BeautifulSoup(html_of_one_consolidated_law_in_force.content, 'html.parser')

        if soup.find('h4', {'class': 'name-article'}) is not None:
            all_articles = soup.find_all('h4', {'class': 'name-article'})

            for article in all_articles:
                title_of_the_article = article\
                    .find('a')\
                    .text\
                    .replace('\t', '') \
                    .replace('\r', '') \
                    .replace('\n', '')

                link_of_the_article = "https://www.legifrance.gouv.fr/loda/article_lc/" + article.get('data-anchor')

                print(title_of_the_article + " : " + link_of_the_article)
        else:
            print("no h4 class name-article")

    def test_extract_all_links_for_codes_in_force(self):
        print("test_extract_all_links_for_codes_in_force")

        url_of_codes = "https://www.legifrance.gouv.fr/liste/code?etatTexte=VIGUEUR&etatTexte=VIGUEUR_DIFF"

        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36 Edg/88.0.705.81',
            'referer': 'https://www.google.fr/',
            'authority': 'www.legifrance.gouv.fr',
            'method': 'GET',
            'path': url_of_codes.replace("https://www.legifrance.gouv.fr", ""),
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'fr,fr-FR;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'cache-control': 'max-age=0',
            'cookie': 'visid_incap_1235873=TtIIancVSD27jnwuHQ1yDpgiPmAAAAAAQUIPAAAAAAA8+76C1vti3Fo3Ut2qItUj; incap_ses_466_1235873=Ir8HB9MSfDcDN5ov3pB3BpgiPmAAAAAA6q6ogRf3HiGNOrmqGgrMXw==; tarteaucitron=!id=a5b4d4cbb5dded9c-1ff2d8bb-aa998d65-5c5326d452f34ba28b3ff1c5!atinternet=true!hotjar=false; lf-demo-accueil=1; JSESSIONID=2A6A5311ECFF2DFF64EFF02FDA32EC8A; LB_APP_ROUTE=.4; LB_FRONT_ROUTE=.1.2; lf-demo-rr-codes=1; seeAbrogated-LEGITEXT000006074069=false; lf-demo-consult-codes-sommaire=1; seeAbrogated-LEGITEXT000006075116=false; seeAbrogated-LEGITEXT000006073984=false; nlbi_1235873=se4TXoAimnQAEhF5jJoYvAAAAADLJalA4a5VX/shfGeDCrg4',
            'dnt': '1',
            'if-none-match': '89dfa94b',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1'
        }

        # Request the content of a page from the url
        html = requests.get(url_of_codes, headers=headers)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.content, 'html.parser')

        if soup.find('h2', {'class': 'title-result-item-code'}) is not None:
            all_h2 = soup.find_all('h2', {'class': 'title-result-item-code'})

            for h2 in all_h2:
                title = h2.find('a').text
                link = 'https://www.legifrance.gouv.fr/codes/texte_lc/' + h2.find('a').get('id').replace('id', '')
                print(title + ' : ' + link)
        else:
            print("no code")

    def test_extract_all_laws_for_energy_sector_from_all_codes_in_force(self):
        print("test_extract_all_laws_for_energy_sector_from_all_codes_in_force")

        cookie = "visid_incap_1235873=lUTwT3V3TS+mLMlge/Jy3AdOPmAAAAAAQUIPAAAAAABUdRnLRltJVGEq8Qm1zkND; incap_ses_466_1235873=vOP1D5KoPQmx5cIv3pB3BgdOPmAAAAAADm9/Oj/bR7QOydKalErswA==; tarteaucitron=!id=6007ec4d07ae1f86-38af0aec-d774188e-cf4513f115b317ff9cb62113!atinternet=true!hotjar=false; lf-demo-accueil=1; JSESSIONID=D412E97F9A9C4A26680A838C7D02E7FE; LB_APP_ROUTE=.5; LB_FRONT_ROUTE=.2.2; nlbi_1235873=I7HmQ1f1elnnJ2TtjJoYvAAAAADvCgXYI7urb38UiupI0281"

        keywords = [
            'énergie',
            'électricité',
            'électrique',
            'tension',
            'courant',
            'puissance'
        ]

        url_of_codes = "https://www.legifrance.gouv.fr/liste/code?etatTexte=VIGUEUR&etatTexte=VIGUEUR_DIFF"

        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36 Edg/88.0.705.81',
            'referer': 'https://www.google.fr/',
            'authority': 'www.legifrance.gouv.fr',
            'method': 'GET',
            'path': url_of_codes.replace("https://www.legifrance.gouv.fr", ""),
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'fr,fr-FR;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'cache-control': 'max-age=0',
            'cookie': cookie,
            'dnt': '1',
            'if-none-match': '89dfa94b',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1'
        }

        time.sleep(3)

        # Request the content of a page from the url
        html_of_codes = requests.get(url_of_codes, headers=headers)

        # Parse the content of html_doc
        soup_of_codes = BeautifulSoup(html_of_codes.content, 'html.parser')

        if soup_of_codes.find('h2', {'class': 'title-result-item-code'}) is not None:
            all_h2 = soup_of_codes.find_all('h2', {'class': 'title-result-item-code'})

            for i in range(0, len(all_h2) + 1):
                print("code numéro : " + str(i))

                title_of_the_code = all_h2[i].find('a').text

                link_of_the_code = 'https://www.legifrance.gouv.fr/codes/texte_lc/' \
                                   + all_h2[i].find('a').get('id').replace('id', '')

                headers_code = {
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36 Edg/88.0.705.81',
                    'referer': 'https://www.google.fr/',
                    'authority': 'www.legifrance.gouv.fr',
                    'method': 'GET',
                    'path': link_of_the_code.replace("https://www.legifrance.gouv.fr", ""),
                    'scheme': 'https',
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'accept-encoding': 'gzip, deflate, br',
                    'accept-language': 'fr,fr-FR;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
                    'cache-control': 'max-age=0',
                    'cookie': cookie,
                    'dnt': '1',
                    'if-none-match': '89dfa94b',
                    'sec-fetch-dest': 'document',
                    'sec-fetch-mode': 'navigate',
                    'sec-fetch-site': 'none',
                    'sec-fetch-user': '?1',
                    'upgrade-insecure-requests': '1'
                }

                time.sleep(3)

                # Request the content of a page from the url
                html_of_one_code = requests.get(link_of_the_code, headers=headers_code)

                # Parse the content of html_doc
                soup_of_one_code = BeautifulSoup(html_of_one_code.content, 'html.parser')

                if soup_of_one_code.find('a', {'class': 'articleLink'}) is not None:
                    all_articles = soup_of_one_code.find_all('a', {'class': 'articleLink'})

                    for article in all_articles:
                        title_of_the_article = "Article " + article.get('data-na') + " du " + title_of_the_code

                        link_of_the_article = "https://www.legifrance.gouv.fr/codes/article_lc/" + article\
                            .get('id').replace('art', '')

                        headers_article = {
                            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36 Edg/88.0.705.81',
                            'referer': 'https://www.google.fr/',
                            'authority': 'www.legifrance.gouv.fr',
                            'method': 'GET',
                            'path': link_of_the_article.replace("https://www.legifrance.gouv.fr", ""),
                            'scheme': 'https',
                            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                            'accept-encoding': 'gzip, deflate, br',
                            'accept-language': 'fr,fr-FR;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
                            'cache-control': 'max-age=0',
                            'cookie': cookie,
                            'dnt': '1',
                            'if-none-match': '89dfa94b',
                            'sec-fetch-dest': 'document',
                            'sec-fetch-mode': 'navigate',
                            'sec-fetch-site': 'none',
                            'sec-fetch-user': '?1',
                            'upgrade-insecure-requests': '1'
                        }

                        time.sleep(3)

                        # Request the content of a page from the url
                        html_of_one_article = requests.get(link_of_the_article, headers=headers_article)

                        # Parse the content of html_doc
                        soup_of_one_article = BeautifulSoup(html_of_one_article.content, 'html.parser')

                        if soup_of_one_article.find('article') is not None:
                            text = soup_of_one_article.find('article') \
                                .text \
                                .replace('Versions', '') \
                                .replace('Liens relatifs', '') \
                                .replace('\t', '') \
                                .replace('\r', '') \
                                .replace('\n', '')

                            for keyword in keywords:
                                if keyword in text:
                                    x = {
                                        'title_of_the_law': title_of_the_article,
                                        'url_of_the_law': link_of_the_article
                                    }

                                    try:
                                        # Connect to the database
                                        connection = pymysql.connect(
                                            host='localhost',
                                            port=3306,
                                            user='root',
                                            password='v2HJJzexYxlp0D0So77ztwMOKEKu97@@@@@@',
                                            db='laws_in_france',
                                            charset='utf8mb4',
                                            cursorclass=pymysql.cursors.DictCursor
                                        )

                                        with connection.cursor() as cursor:
                                            try:
                                                sql = "INSERT INTO `laws_for_energy_sector` (" \
                                                      "`title_of_the_law`, " \
                                                      "`url_of_the_law`) VALUE (%s, %s)"

                                                cursor.execute(sql, (
                                                    x.get('title_of_the_law'),
                                                    x.get('url_of_the_law')
                                                ))

                                                connection.commit()

                                                print(x.get('title_of_the_law') + ' : ok')

                                                connection.close()
                                            except Exception as e:
                                                print("The record already exists (" + x.get('title_of_the_law')
                                                      + ") : " + str(e))
                                                connection.close()
                                    except Exception as e:
                                        print("Problem connection MySQL : " + str(e))

                                    break
                                else:
                                    print('no keyword "' + keyword + '" for ' + title_of_the_article)
                        else:
                            print("no article")
                else:
                    print("no a class ")
        else:
            print("no code")

    def test_extract_all_laws_for_energy_sector_from_all_consolidated_laws(self):
        print("test_extract_all_laws_for_energy_sector_from_all_consolidated_laws")

        cookie = "visid_incap_1235873=lUTwT3V3TS+mLMlge/Jy3AdOPmAAAAAAQUIPAAAAAABUdRnLRltJVGEq8Qm1zkND; incap_ses_466_1235873=vOP1D5KoPQmx5cIv3pB3BgdOPmAAAAAADm9/Oj/bR7QOydKalErswA==; tarteaucitron=!id=6007ec4d07ae1f86-38af0aec-d774188e-cf4513f115b317ff9cb62113!atinternet=true!hotjar=false; lf-demo-accueil=1; JSESSIONID=D412E97F9A9C4A26680A838C7D02E7FE; LB_APP_ROUTE=.5; LB_FRONT_ROUTE=.2.2; nlbi_1235873=I7HmQ1f1elnnJ2TtjJoYvAAAAADvCgXYI7urb38UiupI0281"

        date_version = "02%2F03%2F2021"

        urls = [
            "https://www.legifrance.gouv.fr/search/lois?tab_selection=lawarticledecree&searchField=ALL&query=*&searchType=ALL&nature=ORDONNANCE&etatArticle=VIGUEUR&etatArticle=ABROGE_DIFF&etatTexte=VIGUEUR&etatTexte=ABROGE_DIFF&typeRecherche=date&dateVersion=" + date_version + "&typePagination=DEFAUT&sortValue=SIGNATURE_DATE_DESC&pageSize=100&page=",
            "https://www.legifrance.gouv.fr/search/lois?tab_selection=lawarticledecree&searchField=ALL&query=*&searchType=ALL&nature=LOI&etatArticle=VIGUEUR&etatArticle=ABROGE_DIFF&etatTexte=VIGUEUR&etatTexte=ABROGE_DIFF&typeRecherche=date&dateVersion=" + date_version + "&typePagination=DEFAUT&sortValue=SIGNATURE_DATE_DESC&pageSize=100&page=",
            "https://www.legifrance.gouv.fr/search/lois?tab_selection=lawarticledecree&searchField=ALL&query=*&searchType=ALL&nature=DECRET&etatArticle=VIGUEUR&etatArticle=ABROGE_DIFF&etatTexte=VIGUEUR&etatTexte=ABROGE_DIFF&typeRecherche=date&dateVersion=" + date_version + "&typePagination=DEFAUT&sortValue=SIGNATURE_DATE_DESC&pageSize=100&page=",
            "https://www.legifrance.gouv.fr/search/lois?tab_selection=lawarticledecree&searchField=ALL&query=*&searchType=ALL&nature=ARRETE&etatArticle=VIGUEUR&etatArticle=ABROGE_DIFF&etatTexte=VIGUEUR&etatTexte=ABROGE_DIFF&typeRecherche=date&dateVersion=" + date_version + "&typePagination=DEFAUT&sortValue=SIGNATURE_DATE_DESC&pageSize=100&page=",
            "https://www.legifrance.gouv.fr/search/lois?tab_selection=lawarticledecree&searchField=ALL&query=*&searchType=ALL&nature=DECRET_LOI&nature=CONSTITUTION&nature=DECISION&nature=CONVENTION&nature=DECLARATION&etatArticle=VIGUEUR&etatArticle=ABROGE_DIFF&etatTexte=VIGUEUR&etatTexte=ABROGE_DIFF&typeRecherche=date&dateVersion=" + date_version + "&typePagination=DEFAUT&sortValue=SIGNATURE_DATE_DESC&pageSize=100&page="
        ]

        keywords = [
            'énergie',
            'électricité',
            'électrique',
            'tension',
            'courant',
            'puissance'
        ]

        for url in urls:
            before_url = url

            after_url = "&tab_selection=lawarticledecree#lois"

            url_of_all_laws_from_one_search = before_url + "1" + after_url

            headers_from_one_consolidated_law = {
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36 Edg/88.0.705.81',
                'referer': 'https://www.google.fr/',
                'authority': 'www.legifrance.gouv.fr',
                'method': 'GET',
                'path': url_of_all_laws_from_one_search.replace("https://www.legifrance.gouv.fr", ""),
                'scheme': 'https',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'fr,fr-FR;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
                'cache-control': 'max-age=0',
                'cookie': cookie,
                'dnt': '1',
                'if-none-match': '89dfa94b',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'none',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1'
            }

            time.sleep(3)

            # Request the content of a page from the url
            html_from_one_consolidated_law = requests.get(url_of_all_laws_from_one_search, headers=headers_from_one_consolidated_law)

            # Parse the content of html_doc
            soup_from_one_consolidated_law = BeautifulSoup(html_from_one_consolidated_law.content, 'html.parser')

            number_of_pages = 0

            if soup_from_one_consolidated_law.find("p", {"class": "nb-result head-filter-title"}) is not None:
                number_of_pages_with_coma = int(soup_from_one_consolidated_law.find("p", {"class": "nb-result head-filter-title"})
                                                .text
                                                .replace(' résultat(s) trouvé(s)', '')
                                                ) / 100

                if int(str(number_of_pages_with_coma).split(".")[1][:1]) < 5:
                    number_of_pages += round(number_of_pages_with_coma) + 1
                    print('number_of_pages : ' + str(number_of_pages))

                elif int(str(number_of_pages_with_coma).split(".")[1][:1]) >= 5:
                    number_of_pages += round(number_of_pages_with_coma)
                    print('number_of_pages : ' + str(number_of_pages))

                for i in range(1, number_of_pages + 1):
                    url_of_one_page = before_url + str(i) + after_url

                    headers_of_one_article = {
                        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36 Edg/88.0.705.81',
                        'referer': 'https://www.google.fr/',
                        'authority': 'www.legifrance.gouv.fr',
                        'method': 'GET',
                        'path': url_of_one_page.replace("https://www.legifrance.gouv.fr", ""),
                        'scheme': 'https',
                        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                        'accept-encoding': 'gzip, deflate, br',
                        'accept-language': 'fr,fr-FR;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
                        'cache-control': 'max-age=0',
                        'cookie': cookie,
                        'dnt': '1',
                        'if-none-match': '89dfa94b',
                        'sec-fetch-dest': 'document',
                        'sec-fetch-mode': 'navigate',
                        'sec-fetch-site': 'none',
                        'sec-fetch-user': '?1',
                        'upgrade-insecure-requests': '1'
                    }

                    time.sleep(2)

                    # Request the content of a page from the url
                    html_of_one_page = requests.get(url_of_one_page, headers=headers_of_one_article)

                    # Parse the content of html_doc
                    soup_of_one_law = BeautifulSoup(html_of_one_page.content, 'html.parser')

                    if soup_of_one_law.find("article", {"class": "result-item"}) is not None:
                        all_laws = soup_of_one_law.find_all("article", {"class": "result-item"})

                        for law in all_laws:
                            if law.find('h2', {'class': 'title-result-item'}) is not None:
                                title_of_the_law = law.find('h2', {'class': 'title-result-item'}).find('a').text

                                link_of_the_law = "https://www.legifrance.gouv.fr/loda/id/" + law\
                                    .find('h2', {'class': 'title-result-item'})\
                                    .get('data-id')

                                headers_of_one_law = {
                                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36 Edg/88.0.705.81',
                                    'referer': 'https://www.google.fr/',
                                    'authority': 'www.legifrance.gouv.fr',
                                    'method': 'GET',
                                    'path': link_of_the_law.replace("https://www.legifrance.gouv.fr", ""),
                                    'scheme': 'https',
                                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                                    'accept-encoding': 'gzip, deflate, br',
                                    'accept-language': 'fr,fr-FR;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
                                    'cache-control': 'max-age=0',
                                    'cookie': cookie,
                                    'dnt': '1',
                                    'if-none-match': '89dfa94b',
                                    'sec-fetch-dest': 'document',
                                    'sec-fetch-mode': 'navigate',
                                    'sec-fetch-site': 'none',
                                    'sec-fetch-user': '?1',
                                    'upgrade-insecure-requests': '1'
                                }

                                time.sleep(2)

                                # Request the content of a page from the url
                                html_of_one_law = requests.get(link_of_the_law, headers=headers_of_one_law)

                                # Parse the content of html_doc
                                soup_of_one_law = BeautifulSoup(html_of_one_law.content, 'html.parser')

                                if soup_of_one_law.find('h4', {'class': 'name-article'}) is not None:
                                    all_articles = soup_of_one_law.find_all('h4', {'class': 'name-article'})

                                    for article in all_articles:
                                        title_of_the_article = article \
                                            .find('a') \
                                            .text \
                                            .replace('\t', '') \
                                            .replace('\r', '') \
                                            .replace('\n', '')

                                        link_of_the_article = "https://www.legifrance.gouv.fr/loda/article_lc/" + article.get(
                                            'data-anchor')

                                        headers_of_one_article_of_one_consolidated_law = {
                                            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36 Edg/88.0.705.81',
                                            'referer': 'https://www.google.fr/',
                                            'authority': 'www.legifrance.gouv.fr',
                                            'method': 'GET',
                                            'path': link_of_the_article.replace(
                                                "https://www.legifrance.gouv.fr", ""),
                                            'scheme': 'https',
                                            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                                            'accept-encoding': 'gzip, deflate, br',
                                            'accept-language': 'fr,fr-FR;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
                                            'cache-control': 'max-age=0',
                                            'cookie': cookie,
                                            'dnt': '1',
                                            'if-none-match': '89dfa94b',
                                            'sec-fetch-dest': 'document',
                                            'sec-fetch-mode': 'navigate',
                                            'sec-fetch-site': 'none',
                                            'sec-fetch-user': '?1',
                                            'upgrade-insecure-requests': '1'
                                        }

                                        time.sleep(2)

                                        # Request the content of a page from the url
                                        html_of_one_article_of_one_consolidated_law = requests.get(
                                            link_of_the_article,
                                            headers=headers_of_one_article_of_one_consolidated_law)

                                        # Parse the content of html_doc
                                        soup_of_one_article_of_one_consolidated_law = BeautifulSoup(
                                            html_of_one_article_of_one_consolidated_law.content, 'html.parser')

                                        if soup_of_one_article_of_one_consolidated_law.find('article') is not None:
                                            text_of_one_article = soup_of_one_article_of_one_consolidated_law.find('article') \
                                                .text \
                                                .replace('Versions', '') \
                                                .replace('Liens relatifs', '') \
                                                .replace('\t', '') \
                                                .replace('\r', '') \
                                                .replace('\n', '')

                                            for keyword in keywords:
                                                if keyword in text_of_one_article:
                                                    x = {
                                                        'title_of_the_law': title_of_the_article + " " + title_of_the_law,
                                                        'url_of_the_law': link_of_the_article
                                                    }

                                                    try:
                                                        # Connect to the database
                                                        connection = pymysql.connect(
                                                            host='localhost',
                                                            port=3306,
                                                            user='root',
                                                            password='v2HJJzexYxlp0D0So77ztwMOKEKu97@@@@@@',
                                                            db='laws_in_france',
                                                            charset='utf8mb4',
                                                            cursorclass=pymysql.cursors.DictCursor
                                                        )

                                                        with connection.cursor() as cursor:
                                                            try:
                                                                sql = "INSERT INTO `laws_for_energy_sector` (" \
                                                                      "`title_of_the_law`, " \
                                                                      "`url_of_the_law`) VALUE (%s, %s)"

                                                                cursor.execute(sql, (
                                                                    x.get('title_of_the_law'),
                                                                    x.get('url_of_the_law')
                                                                ))

                                                                connection.commit()

                                                                print(x.get('title_of_the_law') + ' : ok')

                                                                connection.close()
                                                            except Exception as e:
                                                                print("The record already exists (" + x.get(
                                                                    'title_of_the_law')
                                                                      + ") : " + str(e))
                                                                connection.close()
                                                    except Exception as e:
                                                        print("Problem connection MySQL : " + str(e))

                                                    break
                                                else:
                                                    print('no keyword "' + keyword + '" for '
                                                          + title_of_the_article + ' ' + title_of_the_law)
                                        else:
                                            print("no article")
                                else:
                                    print("no h4 class name-article")
                            else:
                                print("no h2 title-result-item")
                    else:
                        print("no article result-item")
            else:
                print("no pages at all")

    def test_list_all_codes(self):
        print("test_list_all_codes")

        url_of_codes = "https://www.legifrance.gouv.fr/liste/code?etatTexte=VIGUEUR&etatTexte=VIGUEUR_DIFF"

        cookie = "visid_incap_1235873=PnaDOi7ORzOIBHnk3EFgq1LRRWAAAAAAQUIPAAAAAACjFGyZQthBBu8sQKQ91fLx; incap_ses_466_1235873=sMnfVVouFwedcj5w4JB3BlLRRWAAAAAA4y5fqFVS4/U+APULYfxg0Q==; tarteaucitron=!id=8f3d75550072f014-8cb8f5cd-b6c2ecdd-ddb6ed7de7d245cd00fe2584!atinternet=true!hotjar=false; lf-demo-accueil=1; JSESSIONID=612CFB5D80C8E8B9E8E2023741773CB1; LB_APP_ROUTE=.1; LB_FRONT_ROUTE=.2.2; nlbi_1235873=j3kzUxTKfVXnc0K7jJoYvAAAAACmbDepvLNuQWsTWZsb9+uk"

        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36 Edg/88.0.705.81',
            'referer': 'https://www.google.fr/',
            'authority': 'www.legifrance.gouv.fr',
            'method': 'GET',
            'path': url_of_codes.replace("https://www.legifrance.gouv.fr", ""),
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'fr,fr-FR;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'cache-control': 'max-age=0',
            'cookie': cookie,
            'dnt': '1',
            'if-none-match': '89dfa94b',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1'
        }

        # Request the content of a page from the url
        html_of_codes = requests.get(url_of_codes, headers=headers)

        # Parse the content of html_doc
        soup_of_codes = BeautifulSoup(html_of_codes.content, 'html.parser')

        if soup_of_codes.find('h2', {'class': 'title-result-item-code'}) is not None:
            all_h2 = soup_of_codes.find_all('h2', {'class': 'title-result-item-code'})

            print("nombre de codes : " + str(len(all_h2)))

            for i in range(0, len(all_h2)):
                title_of_the_code = all_h2[i].find('a').text

                print("code numéro : " + str(i) + " : " + title_of_the_code)
        else:
            print("no code")

    def test_extract_articles_from_legifrance_to_excel(self):
        url_du_sommaire = "https://www.legifrance.gouv.fr/affichCode.do?cidTexte=LEGITEXT000005634379&dateTexte=20200310"

        titre = "Code de commerce"

        # Request the content of a page from the url
        html = requests.get(url_du_sommaire)

        # Parse the content of html
        soup = BeautifulSoup(html.content, 'html.parser')

        if soup.find_all("span", {"class": "codeLienArt"}) is not None:
            articles = soup.find_all("span", {"class": "codeLienArt"})

            # Create a workbook and add a worksheet.
            workbook = xlsxwriter.Workbook(titre.replace(" ", "_") + '.xlsx')
            worksheet = workbook.add_worksheet("Articles")

            # Start from the first cell. Rows and columns are zero indexed.
            row = 0
            col = 0

            worksheet.write(row, col, "Articles")

            for article in articles:
                row += 1
                print(article.find("a").text)
                worksheet.write(row, col, article.find("a").text)

            workbook.close()

    def test_extract_titreArt_from_legifrance(self):
        tracemalloc.start()

        url_article = "https://www.legifrance.gouv.fr/affichCodeArticle.do;jsessionid=983DC2F2905C4444813EFC9BF95ADC3C.tplgfr35s_3?idArticle=LEGIARTI000006419280&cidTexte=LEGITEXT000006070721&dateTexte=20200315"

        # Request the content of a page from the url
        html = requests.get(url_article)

        # Parse the content of html
        soup = BeautifulSoup(html.content, 'html.parser')

        if soup.find("div", {"class": "titreArt"}) is not None:
            print("article : " + soup.find("div", {"class": "titreArt"}).text)

        """
        snapshot = tracemalloc.take_snapshot()

        top_stats = snapshot.statistics('lineno')

        for stat in top_stats:
            print(stat)
        """

    def test_extract_histoArt_from_legifrance(self):
        url_article = "https://www.legifrance.gouv.fr/affichCodeArticle.do;jsessionid=983DC2F2905C4444813EFC9BF95ADC3C.tplgfr35s_3?idArticle=LEGIARTI000006419288&cidTexte=LEGITEXT000006070721&dateTexte=20200315&categorieLien=id&oldAction=&nbResultRech="

        # Request the content of a page from the url
        html = requests.get(url_article)

        # Parse the content of html
        soup = BeautifulSoup(html.content, 'html.parser')

        if soup.find("div", {"class": "histoArt"}) is not None:
            print("contenu : " + soup.find("div", {"class": "histoArt"}).text)

    def test_extract_corpsArt_from_legifrance(self):
        url_article = "https://www.legifrance.gouv.fr/affichCodeArticle.do;jsessionid=983DC2F2905C4444813EFC9BF95ADC3C.tplgfr35s_3?idArticle=LEGIARTI000006419288&cidTexte=LEGITEXT000006070721&dateTexte=20200315&categorieLien=id&oldAction=&nbResultRech="

        # Request the content of a page from the url
        html = requests.get(url_article)

        # Parse the content of html
        soup = BeautifulSoup(html.content, 'html.parser')

        if soup.find("div", {"class": "corpsArt"}) is not None:
            print("contenu : " + soup.find("div", {"class": "corpsArt"}).text)

    def test_display_all_href_of_each_block_of_articles_of_one_code_in_force_from_legifrance(self):
        url_summary = "https://www.legifrance.gouv.fr/affichCode.do;jsessionid=983DC2F2905C4444813EFC9BF95ADC3C.tplgfr35s_3?cidTexte=LEGITEXT000006070721&dateTexte=20200315"

        # Request the content of a page from the url
        html = requests.get(url_summary)

        # Parse the content of html
        soup = BeautifulSoup(html.content, 'html.parser')

        if soup.find("span", {"class": "codeLienArt"}) is not None:
            all_code_lien_art = soup.find_all("span", {"class": "codeLienArt"})

            for code_lien_art in all_code_lien_art:
                print("https://www.legifrance.gouv.fr/" + code_lien_art.find("a").get('href'))

    def test_display_all_href_titreArt_of_one_block_of_articles_of_one_code_in_force_from_legifrance(self):
        url_block_of_article = "https://www.legifrance.gouv.fr/affichCode.do;jsessionid=983DC2F2905C4444813EFC9BF95ADC3C.tplgfr35s_3?idSectionTA=LEGISCTA000006089696&cidTexte=LEGITEXT000006070721&dateTexte=20200315"

        # Request the content of a page from the url
        html = requests.get(url_block_of_article)

        # Parse the content of html
        soup = BeautifulSoup(html.content, 'html.parser')

        if soup.find("div", {"class": "titreArt"}) is not None:
            all_titreArt = soup.find_all("div", {"class": "titreArt"})

            for titreArt in all_titreArt:
                print("https://www.legifrance.gouv.fr/" + titreArt.find("a").get('href'))

    def test_display_titre_du_code(self):
        url_summary = "https://www.legifrance.gouv.fr/affichCode.do?cidTexte=LEGITEXT000006075116&dateTexte=20200315"

        # Request the content of a page from the url
        html_summary = requests.get(url_summary)

        # Parse the content of html
        soup_summary = BeautifulSoup(html_summary.content, 'html.parser')

        if soup_summary.find(id="breadcrumb") is not None:
            titre = soup_summary.find(id="breadcrumb")\
                .find("strong")\
                .text\
                .replace(" ", "")\
                .replace("'", "")\
                .replace("\t", "")

            print(len(titre))
            print(titre[:len(titre)-5])

    def test_display_all_href_titreArt_of_each_block_of_articles_of_one_code_in_force_from_legifrance(self):
        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        try:
            array_articles = []

            url_summary = "https://www.legifrance.gouv.fr/affichCode.do?cidTexte=LEGITEXT000006075116"

            time.sleep(3)

            # Request the content of a page from the url_summary
            html_summary = requests.get(url_summary)

            # Parse the content of html
            soup_summary = BeautifulSoup(html_summary.content, 'html.parser')

            if soup_summary.find("span", {"class": "codeLienArt"}) is not None:
                all_code_lien_art = soup_summary.find_all("span", {"class": "codeLienArt"})

                for code_lien_art in all_code_lien_art:
                    url_block_of_article = "https://www.legifrance.gouv.fr/" + code_lien_art.find("a").get('href')

                    time.sleep(3)

                    # Request the content of a page from the url
                    html_block_of_article = requests.get(url_block_of_article)

                    # Parse the content of html
                    soup_block_of_article = BeautifulSoup(html_block_of_article.content, 'html.parser')

                    if soup_block_of_article.find("div", {"class": "titreArt"}) is not None:
                        all_titre_art = soup_block_of_article.find_all("div", {"class": "titreArt"})

                        for titreArt in all_titre_art:
                            array_articles.append("https://www.legifrance.gouv.fr/" + titreArt.find("a").get('href'))

            print("length array_articles : " + str(len(array_articles)))

            for x in range(0, len(array_articles)):
                print("element : " + str(x))

                url_article = str(array_articles[x])

                time.sleep(3)

                # Request the content of a page from the url
                html_article = requests.get(url_article)

                # Parse the content of html
                soup_article = BeautifulSoup(html_article.content, 'html.parser')

                if soup_article.find("div", {"class": "titreArt"}) is not None:
                    print(x)
                    print(str(x) + "_" + soup_article.find("div", {"class": "titreArt"}).text.replace(":", "_")
                          .replace(" ", "_").replace("\n", "").replace("?", "").replace("/", "").replace("-", "_"))

                    array_articles.pop(x)

                else:
                    print('no titre article')

        except:
            print("problem")

    def test_make_a_tor_request_on_legifrance(self):
        with TorRequest() as tr:
            response = tr.get('http://ipecho.net/plain')
            print(response.text)  # not your IP address


class UniTestsDataMiningLegifranceWithRPA(unittest.TestCase):
    def test_open_browser_with_rpa(self):
        print('test_open_browser_with_rpa')

        url = "https://www.legifrance.gouv.fr/"

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        # with Firefox
        options = Options()
        options.headless = True
        browser = webdriver.Firefox(executable_path='..\\geckodriver.exe', options=options)

        time.sleep(10)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get(url)

        time.sleep(20)

    def test_extract_text_of_one_article_of_one_code_in_force_with_rpa(self):
        print('test_extract_text_of_one_article_of_one_code_in_force_with_rpa')

        url = "https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000031210068"

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        # with Firefox
        options = Options()
        options.headless = True
        browser = webdriver.Firefox(executable_path='..\\geckodriver.exe', options=options)

        time.sleep(10)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get(url)

        time.sleep(20)

        try:
            text_of_the_article = browser.find_element_by_xpath(
                "/html/body/div[1]/div/main/div/div[2]/div[4]/article"
            ).text \
                .replace('Versions', '') \
                .replace('Liens relatifs', '') \
                .replace('\t', '') \
                .replace('\r', '') \
                .replace('\n', '')

            print("text_of_the_article : " + text_of_the_article)
        except Exception as e:
            print('error text_of_the_article : ' + str(e))

        browser.close()

    def test_extract_title_of_one_article_of_one_code_in_force_with_rpa(self):
        print('test_extract_title_of_one_article_of_one_code_in_force_with_rpa')

        url = "https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000031210068"

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        # with Firefox
        options = Options()
        options.headless = True
        browser = webdriver.Firefox(executable_path='..\\geckodriver.exe', options=options)

        time.sleep(10)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get(url)

        time.sleep(20)

        try:
            title_of_the_article = browser.find_element_by_xpath(
                "/html/body/div[1]/div/main/div/div[2]/div[4]/article/div/div[1]/h2"
            ).text.replace(":", "_")\
                .replace(" ", "_") \
                .replace('é', 'e') \
                .replace('à', 'a') \
                .replace("\n", "") \
                .replace("?", "") \
                .replace("/", "") \
                .replace("-", "_")

            print("title_of_the_article : " + title_of_the_article)
        except Exception as e:
            print('error title_of_the_article : ' + str(e))

        browser.close()

    def test_extract_all_articles_from_one_code_in_force_with_rpa(self):
        print('test_extract_all_articles_from_one_code_in_force_with_rpa')

        url = "https://www.legifrance.gouv.fr/codes/texte_lc/LEGITEXT000006074075/2021-07-31/"

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        # with Firefox
        options = Options()
        options.headless = True
        browser = webdriver.Firefox(executable_path='..\\geckodriver.exe', options=options)

        time.sleep(10)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get(url)

        print("page opened")

        time.sleep(20)

        try:
            all_articles = browser.find_elements_by_class_name('articleLink')

            for i in range(0, len(all_articles)):
                title = str(i) + "_Article_" + all_articles[i].get_attribute('data-na')
                link = "https://www.legifrance.gouv.fr/codes/article_lc/" + all_articles[i].get_attribute('id').replace('art', '')
                print(title + " : " + link)
        except Exception as e:
            print("no a class articleLink : " + str(e))

        browser.close()

    def test_display_titre_du_code_with_rpa(self):
        print('test_display_titre_du_code_with_rpa')

        url = "https://www.legifrance.gouv.fr/codes/texte_lc/LEGITEXT000006074075/2021-07-31/"

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        # with Firefox
        options = Options()
        options.headless = True
        browser = webdriver.Firefox(executable_path='..\\geckodriver.exe', options=options)

        time.sleep(10)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get(url)

        print("page opened")

        time.sleep(20)

        try:
            titre_du_code = browser.find_element_by_xpath(
                "/html/body/div[1]/div/main/div/div[2]/div[1]/h1"
            ).text\
                .lower()\
                .replace(" ", "") \
                .replace('é', 'e') \
                .replace("'", "") \
                .replace("\t", "")

            print(len(titre_du_code))
            print(titre_du_code[:len(titre_du_code) - 5])
        except Exception as e:
            print("no titre_du_code : " + str(e))

        browser.close()

    def test_display_all_articles_from_one_code_in_force_with_rpa(self):
        print('test_display_all_articles_from_one_code_in_force_with_rpa')

        url = "https://www.legifrance.gouv.fr/codes/texte_lc/LEGITEXT000006074075/2021-07-31/"

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        # with Firefox
        browser = webdriver.Firefox(executable_path='..\\geckodriver.exe')

        time.sleep(10)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get(url)

        time.sleep(20)

        try:
            all_articles = browser.find_elements_by_class_name('articleLink')

            for i in range(0, len(all_articles)):
                warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

                # with Firefox
                browser_1 = webdriver.Firefox(executable_path='..\\geckodriver.exe')

                time.sleep(10)

                # maximize wind9ow
                browser_1.maximize_window()

                time.sleep(5)

                link = "https://www.legifrance.gouv.fr/codes/article_lc/" + all_articles[i].get_attribute('id').replace('art', '')

                browser_1.get(link)

                time.sleep(15)

                browser_1.close()
        except Exception as e:
            print("no articleLink : " + str(e))

        browser.close()


if __name__ == '__main__':
    unittest.main()
