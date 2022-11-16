import json
import unittest
import time
from bs4 import BeautifulSoup
import requests
from requests_tor import RequestsTor
import pymysql.cursors


class UnitTestsDataMiningWikipediaWithClearWeb(unittest.TestCase):
    # ok
    def test_extract_the_title_of_the_topic(self):
        print("test_extract_the_title_of_the_topic")

        url = 'https://en.wikipedia.org/wiki/Outline_of_artificial_intelligence'

        # Request the content of a page from the url
        html = requests.get(url)

        time.sleep(3)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.content, 'html.parser')

        if soup.select_one("#firstHeading") is not None:
            print("title : " + str(soup.select_one("#firstHeading").text))

    # ok
    def test_extract_the_body_content_of_the_topic(self):
        print("test_extract_the_title_of_the_topic")

        url = 'https://en.wikipedia.org/wiki/Outline_of_artificial_intelligence'

        # Request the content of a page from the url
        html = requests.get(url)

        time.sleep(3)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.content, 'html.parser')

        if soup.select_one("#bodyContent") is not None:
            print("content : " + str(soup.select_one("#bodyContent").text))


class UnitTestsDataMiningWikipediaWithDarkWeb(unittest.TestCase):
    # ok
    def test_extract_the_pages_for_prix_scientifiques_into_mysql(self):
        print("test_extract_the_pages_for_prix_scientifiques_into_mysql")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        urls = [
            "https://fr.wikipedia.org/wiki/Cat%C3%A9gorie:Prix_scientifique",
            "https://fr.wikipedia.org/wiki/Cat%C3%A9gorie:Laur%C3%A9at_de_prix_scientifique",
            "https://fr.wikipedia.org/wiki/Cat%C3%A9gorie:Distinction_en_arch%C3%A9ologie",
            "https://fr.wikipedia.org/wiki/Cat%C3%A9gorie:R%C3%A9compense_d%27astronomie",
            "https://fr.wikipedia.org/wiki/Cat%C3%A9gorie:Prix_Georges-Lema%C3%AEtre",
            "https://fr.wikipedia.org/wiki/Cat%C3%A9gorie:Distinction_en_biochimie",
            "https://fr.wikipedia.org/wiki/Cat%C3%A9gorie:Distinction_en_biologie",
            "https://fr.wikipedia.org/wiki/Cat%C3%A9gorie:Distinction_en_chimie",
            "https://fr.wikipedia.org/wiki/Cat%C3%A9gorie:Prix_de_communication_scientifique",
            "https://fr.wikipedia.org/wiki/Cat%C3%A9gorie:Prix_d%27%C3%A9conomie",
            "https://fr.wikipedia.org/wiki/Cat%C3%A9gorie:Prix_scientifique_f%C3%A9minin",
            "https://fr.wikipedia.org/wiki/Cat%C3%A9gorie:Distinction_en_g%C3%A9ographie",
            "https://fr.wikipedia.org/wiki/Cat%C3%A9gorie:Distinction_en_g%C3%A9ologie",
            "https://fr.wikipedia.org/wiki/Cat%C3%A9gorie:Distinction_en_histoire_des_sciences",
            "https://fr.wikipedia.org/wiki/Cat%C3%A9gorie:Humaniste_de_l%27Ann%C3%A9e",
            "https://fr.wikipedia.org/wiki/Cat%C3%A9gorie:Prix_en_th%C3%A9orie_de_l%27information",
            "https://fr.wikipedia.org/wiki/Cat%C3%A9gorie:Distinction_en_informatique",
            "https://fr.wikipedia.org/wiki/Cat%C3%A9gorie:Distinction_en_ing%C3%A9nierie",
            "https://fr.wikipedia.org/wiki/Cat%C3%A9gorie:Prix_Kondratiev",
            "https://fr.wikipedia.org/wiki/Cat%C3%A9gorie:Distinction_en_linguistique",
            "https://fr.wikipedia.org/wiki/Cat%C3%A9gorie:Distinction_en_math%C3%A9matiques",
            "https://fr.wikipedia.org/wiki/Cat%C3%A9gorie:M%C3%A9daille_John-Scott",
            "https://fr.wikipedia.org/wiki/Cat%C3%A9gorie:M%C3%A9daille_Kondratiev",
            "https://fr.wikipedia.org/wiki/Cat%C3%A9gorie:Distinction_en_m%C3%A9decine",
            "https://fr.wikipedia.org/wiki/Cat%C3%A9gorie:Prix_en_m%C3%A9t%C3%A9orologie",
            "https://fr.wikipedia.org/wiki/Cat%C3%A9gorie:Membre_de_la_National_Inventors_Hall_of_Fame",
            "https://fr.wikipedia.org/wiki/Cat%C3%A9gorie:Distinction_en_pal%C3%A9ontologie",
            "https://fr.wikipedia.org/wiki/Cat%C3%A9gorie:Distinction_en_philosophie",
            "https://fr.wikipedia.org/wiki/Cat%C3%A9gorie:Distinction_en_physique",
            "https://fr.wikipedia.org/wiki/Cat%C3%A9gorie:M%C3%A9daille_polaire",
            "https://fr.wikipedia.org/wiki/Cat%C3%A9gorie:Distinction_en_science_politique",
            "https://fr.wikipedia.org/wiki/Cat%C3%A9gorie:Prix_Galien",
            "https://fr.wikipedia.org/wiki/Cat%C3%A9gorie:Prix_Le_roi_est_nu",
            "https://fr.wikipedia.org/wiki/Cat%C3%A9gorie:Distinction_en_psychologie",
            "https://fr.wikipedia.org/wiki/Cat%C3%A9gorie:Prix_Shaw",
            "https://fr.wikipedia.org/wiki/Cat%C3%A9gorie:Distinction_en_sociologie",
            "https://fr.wikipedia.org/wiki/Cat%C3%A9gorie:Prix_scientifique_par_pays",
            "https://fr.wikipedia.org/wiki/Cat%C3%A9gorie:Prix_scientifique_en_Allemagne",
            "https://fr.wikipedia.org/wiki/Cat%C3%A9gorie:Prix_scientifique_en_Autriche",
            "https://fr.wikipedia.org/wiki/Cat%C3%A9gorie:Prix_scientifique_en_Belgique",
            "https://fr.wikipedia.org/wiki/Cat%C3%A9gorie:Prix_scientifique_au_Br%C3%A9sil",
            "https://fr.wikipedia.org/wiki/Cat%C3%A9gorie:Prix_scientifique_au_Canada",
            "https://fr.wikipedia.org/wiki/Cat%C3%A9gorie:Prix_scientifique_en_Chine",
            "https://fr.wikipedia.org/wiki/Cat%C3%A9gorie:Prix_scientifique_au_Danemark",
            "https://fr.wikipedia.org/wiki/Cat%C3%A9gorie:Prix_scientifique_en_Espagne",
            "https://fr.wikipedia.org/wiki/Cat%C3%A9gorie:Prix_scientifique_aux_%C3%89tats-Unis",
            "https://fr.wikipedia.org/wiki/Cat%C3%A9gorie:Prix_scientifique_en_Finlande",
            "https://fr.wikipedia.org/wiki/Cat%C3%A9gorie:Prix_scientifique_en_France",
            "https://fr.wikipedia.org/wiki/Cat%C3%A9gorie:Prix_scientifique_en_Hongrie",
            "https://fr.wikipedia.org/wiki/Cat%C3%A9gorie:Prix_scientifique_en_Inde",
            "https://fr.wikipedia.org/wiki/Cat%C3%A9gorie:Prix_scientifique_en_Isra%C3%ABl",
            "https://fr.wikipedia.org/wiki/Cat%C3%A9gorie:Prix_scientifique_en_Italie",
            "https://fr.wikipedia.org/wiki/Cat%C3%A9gorie:Prix_scientifique_au_Japon",
            "https://fr.wikipedia.org/wiki/Cat%C3%A9gorie:Prix_scientifique_au_Mexique",
            "https://fr.wikipedia.org/wiki/Cat%C3%A9gorie:Prix_scientifique_en_Norv%C3%A8ge",
            "https://fr.wikipedia.org/wiki/Cat%C3%A9gorie:Prix_scientifique_au_Pakistan",
            "https://fr.wikipedia.org/wiki/Cat%C3%A9gorie:Prix_scientifique_en_Pologne",
            "https://fr.wikipedia.org/wiki/Cat%C3%A9gorie:Prix_scientifique_au_Royaume-Uni",
            "https://fr.wikipedia.org/wiki/Cat%C3%A9gorie:Prix_scientifique_en_Russie",
            "https://fr.wikipedia.org/wiki/Cat%C3%A9gorie:Prix_scientifique_en_Su%C3%A8de",
            "https://fr.wikipedia.org/wiki/Cat%C3%A9gorie:Prix_scientifique_en_Suisse",
            "https://fr.wikipedia.org/wiki/Cat%C3%A9gorie:Prix_Prince-Mahidol",
            "https://fr.wikipedia.org/wiki/Cat%C3%A9gorie:Prix_scientifique_au_Vatican"
        ]

        i = 1

        for url in urls:
            print("url : " + url)

            rt = RequestsTor()

            html_with_tor = rt.get(url, headers=headers)

            time.sleep(3)

            soup = BeautifulSoup(html_with_tor.content, 'html.parser')

            if soup.find('div', {'class': 'mw-category-group'}) is not None:
                all_div = soup.find_all('div', {'class': 'mw-category-group'})

                for div in all_div:
                    if div.find('a') is not None:
                        all_a = div.find_all('a')

                        for a in all_a:
                            prix_scientifique = a.get('title').lower().replace('catégorie:', '')

                            url_prix_scientifique = "https://fr.wikipedia.org" + a.get('href')

                            dataset_prix_scientifique = {
                                "prix_scientifique": prix_scientifique,
                                "url_prix_scientifique": url_prix_scientifique
                            }

                            connection = pymysql.connect(
                                host='localhost',
                                port=3306,
                                user='root',
                                password='8h0NEJkEf3lyCBUoPQwCHSu@@@@@@@',
                                db='prix_scientifiques',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor
                            )

                            with connection.cursor() as cursor:
                                try:
                                    sql = "INSERT INTO prix_scientifiques " \
                                          "(prix_scientifique, url_prix_scientifique) " \
                                          "VALUE (%s, %s)"

                                    cursor.execute(sql, (
                                        dataset_prix_scientifique.get('prix_scientifique'),
                                        dataset_prix_scientifique.get('url_prix_scientifique')
                                    )
                                    )

                                    connection.commit()

                                    print(str(i) + " The record is stored : prix_scientifiques : "
                                          + str(dataset_prix_scientifique))

                                    connection.close()
                                except Exception as e:
                                    print("The record already exists : " + str(e))
                                    connection.close()

                            i += 1

    # non ok
    def test_extract_the_pages_for_conjectures_scientifiques_into_mysql(self):
        print("test_extract_the_pages_for_conjectures_scientifiques_into_mysql")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        urls = [
            "https://fr.wikipedia.org/wiki/Liste_de_conjectures_math%C3%A9matiques",
            "https://fr.wikipedia.org/wiki/Probl%C3%A8mes_non_r%C3%A9solus_en_math%C3%A9matiques",
            "https://fr.wikipedia.org/wiki/Conjecture_d%27Erd%C5%91s",
            "https://fr.wikipedia.org/wiki/Probl%C3%A8mes_de_Hilbert",
            "https://fr.wikipedia.org/wiki/Probl%C3%A8mes_du_prix_du_mill%C3%A9naire",
            "https://fr.wikipedia.org/wiki/Probl%C3%A8mes_de_Landau",
            "https://fr.wikipedia.org/wiki/Probl%C3%A8mes_de_Smale"
        ]

        i = 1

        for url in urls:
            print("url : " + url)

            rt = RequestsTor()

            html_with_tor = rt.get(url, headers=headers)

            time.sleep(3)

            soup = BeautifulSoup(html_with_tor.content, 'html.parser')

            if soup.find('a') is not None:
                all_a = soup.find_all('a')

                for a in all_a:
                    print(a)

                    try:
                        conjecture_scientifique = a.text

                        url_conjecture_scientifique = "https://fr.wikipedia.org" + a.get('href')

                        dataset_conjecture_scientifique = {
                            "conjecture_scientifique": conjecture_scientifique,
                            "url_conjecture_scientifique": url_conjecture_scientifique
                        }

                        connection = pymysql.connect(
                            host='localhost',
                            port=3306,
                            user='root',
                            password='8h0NEJkEf3lyCBUoPQwCHSu@@@@@@@',
                            db='conjectures_scientifiques',
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor
                        )

                        with connection.cursor() as cursor:
                            try:
                                sql = "INSERT INTO conjectures_scientifiques " \
                                      "(conjectures_scientifiques, url_conjectures_scientifiques) " \
                                      "VALUE (%s, %s)"

                                cursor.execute(sql, (
                                    dataset_conjecture_scientifique.get('conjectures_scientifiques'),
                                    dataset_conjecture_scientifique.get('url_conjectures_scientifiques')
                                )
                                               )

                                connection.commit()

                                print(str(i) + " The record is stored : conjectures_scientifiques : "
                                      + str(dataset_conjecture_scientifique))

                                connection.close()
                            except Exception as e:
                                print("The record already exists : " + str(e))
                                connection.close()

                        i += 1
                    except Exception as e:
                        print('error main : ' + str(e))


class UnitTestsDataMiningWikipediaForGasWithDarkWeb(unittest.TestCase):
    # ok
    # https://en.wikipedia.org/wiki/List_of_countries_by_natural_gas_proven_reserves
    def test_extract_the_list_of_countries_by_natural_gas_proven_reserves(self):
        print("test_extract_the_list_of_countries_by_natural_gas_proven_reserves")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://en.wikipedia.org/wiki/List_of_countries_by_natural_gas_proven_reserves"

        rt = RequestsTor()

        html_with_tor = rt.get(url, headers=headers)

        soup = BeautifulSoup(html_with_tor.content, 'html.parser')

        if soup.find_all('tbody')[0].find('tr') is not None:
            all_tr = soup.find_all('tbody')[0].find_all('tr')

            for tr in all_tr:
                all_td = tr.find_all('td')

                country = ''
                us_eia_start_of_2021_in_kilo_cubic_meter = ''
                opec_start_of_2018_in_kilo_cubic_meter = ''
                bp_start_of_2018_in_kilo_cubic_meter = ''
                other_in_kilo_cubic_meter = ''
                production_in_kilo_cubic_meter_per_year_in_2020 = ''
                number_of_years_of_production_in_reserve = ''

                for a in range(0, len(all_td)):
                    if a == 0:
                        country += all_td[a].text.replace('\n', '').replace('\u00a0', '').replace('\u202f*', '')
                    elif a == 1:
                        us_eia_start_of_2021_in_kilo_cubic_meter += all_td[a].text.replace('\n', '').replace(',', '')\
                            .replace(' (2022)', '').replace(' (2020)', '')
                    elif a == 2:
                        opec_start_of_2018_in_kilo_cubic_meter += all_td[a].text.replace('\n', '').replace(',', '')
                    elif a == 3:
                        bp_start_of_2018_in_kilo_cubic_meter += all_td[a].text.replace('\n', '').replace(',', '')
                    elif a == 4:
                        other_in_kilo_cubic_meter += all_td[a].text.replace('\n', '').replace(',', '')
                    elif a == 5:
                        production_in_kilo_cubic_meter_per_year_in_2020 += all_td[a].text.replace('\n', '')\
                            .replace(' (2019)', '')
                    elif a == 6:
                        number_of_years_of_production_in_reserve += all_td[a].text.replace('\n', '').replace('-', '')

                element = {
                    'country': country,
                    'us_eia_start_of_2021_in_kilo_cubic_meter': us_eia_start_of_2021_in_kilo_cubic_meter,
                    'opec_start_of_2018_in_kilo_cubic_meter': opec_start_of_2018_in_kilo_cubic_meter,
                    'bp_start_of_2018_in_kilo_cubic_meter': bp_start_of_2018_in_kilo_cubic_meter,
                    'other_in_kilo_cubic_meter': other_in_kilo_cubic_meter,
                    'production_in_kilo_cubic_meter_per_year_in_2020': production_in_kilo_cubic_meter_per_year_in_2020,
                    'number_of_years_of_production_in_reserve': number_of_years_of_production_in_reserve
                }

                element_data_json = json.dumps(element)

                print(element_data_json + ',')

    # ok
    # https://en.wikipedia.org/wiki/List_of_countries_by_natural_gas_production
    def test_extract_the_list_of_countries_by_natural_gas_production(self):
        print("test_extract_the_list_of_countries_by_natural_gas_production")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://en.wikipedia.org/wiki/List_of_countries_by_natural_gas_production"

        rt = RequestsTor()

        html_with_tor = rt.get(url, headers=headers)

        soup = BeautifulSoup(html_with_tor.content, 'html.parser')

        if soup.find_all('tbody')[1].find('tr') is not None:
            all_tr = soup.find_all('tbody')[1].find_all('tr')

            for tr in all_tr:
                all_td = tr.find_all('td')

                rank = ''
                country = ''
                continent = ''
                annual_natural_gas_production_in_million_cubic_meter = ''
                date_of_information = ''

                for a in range(0, len(all_td)):
                    if a == 0:
                        rank += all_td[a].text.replace('\n', '').replace('\u00a0', '').replace('\u202f*', '')
                    elif a == 1:
                        country += all_td[a].text.replace('\n', '').replace(',', '')\
                            .replace(' (2022)', '').replace(' (2020)', '').replace('\u00a0', '')
                    elif a == 2:
                        continent += all_td[a].text.replace('\n', '').replace(',', '')
                    elif a == 3:
                        annual_natural_gas_production_in_million_cubic_meter += all_td[a].text.replace('\n', '').replace(',', '')
                    elif a == 4:
                        date_of_information += all_td[a].text.replace('\n', '').replace(',', '').replace(' est.', '')

                element = {
                    'rank': rank,
                    'country': country,
                    'continent': continent,
                    'annual_natural_gas_production_in_million_cubic_meter':
                        annual_natural_gas_production_in_million_cubic_meter,
                    'date_of_information': date_of_information
                }

                element_data_json = json.dumps(element)

                print(element_data_json + ',')

    # ok
    # https://en.wikipedia.org/wiki/List_of_countries_by_natural_gas_consumption
    def test_extract_the_list_of_countries_by_natural_gas_consumption(self):
        print("test_extract_the_list_of_countries_by_natural_gas_consumption")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://en.wikipedia.org/wiki/List_of_countries_by_natural_gas_consumption"

        rt = RequestsTor()

        html_with_tor = rt.get(url, headers=headers)

        soup = BeautifulSoup(html_with_tor.content, 'html.parser')

        if soup.find_all('tbody')[0].find('tr') is not None:
            all_tr = soup.find_all('tbody')[0].find_all('tr')

            for tr in all_tr:
                all_td = tr.find_all('td')

                country_region = ''
                natural_gas_consumption_in_million_cubic_meter_per_year = ''
                date_of_information = ''

                for a in range(0, len(all_td)):
                    if a == 0:
                        country_region += all_td[a].text.replace('\n', '').replace('\u00a0', '').replace('\u202f*', '')
                    elif a == 1:
                        natural_gas_consumption_in_million_cubic_meter_per_year += all_td[a].text.replace('\n', '')\
                            .replace(',', '').replace(' (2022)', '').replace(' (2020)', '').replace('\u00a0', '')
                    elif a == 2:
                        date_of_information += all_td[a].text.replace('\n', '').replace(',', '').replace(' est.', '')

                element = {
                    'country_region': country_region,
                    'natural_gas_consumption_in_million_cubic_meter_per_year':
                        natural_gas_consumption_in_million_cubic_meter_per_year,
                    'date_of_information': date_of_information
                }

                element_data_json = json.dumps(element)

                print(element_data_json + ',')

    # ok
    # https://en.wikipedia.org/wiki/List_of_countries_by_natural_gas_exports
    def test_extract_the_list_of_countries_by_natural_gas_exports(self):
        print("test_extract_the_list_of_countries_by_natural_gas_exports")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://en.wikipedia.org/wiki/List_of_countries_by_natural_gas_exports"

        rt = RequestsTor()

        html_with_tor = rt.get(url, headers=headers)

        soup = BeautifulSoup(html_with_tor.content, 'html.parser')

        if soup.find_all('tbody')[0].find('tr') is not None:
            all_tr = soup.find_all('tbody')[0].find_all('tr')

            for tr in all_tr:
                all_td = tr.find_all('td')

                country_region = ''
                natural_gas_exports_in_cubic_meter_per_year = ''
                date_of_information = ''

                for a in range(0, len(all_td)):
                    if a == 0:
                        country_region += all_td[a].text.replace('\n', '').replace('\u00a0', '').replace('\u202f*', '')
                    elif a == 1:
                        natural_gas_exports_in_cubic_meter_per_year += all_td[a].text.replace('\n', '')\
                            .replace(',', '').replace(' (2022)', '').replace(' (2020)', '').replace('\u00a0', '')
                    elif a == 2:
                        date_of_information += all_td[a].text.replace('\n', '').replace(',', '').replace(' est.', '')

                element = {
                    'country_region': country_region,
                    'natural_gas_exports_in_cubic_meter_per_year': natural_gas_exports_in_cubic_meter_per_year,
                    'date_of_information': date_of_information
                }

                element_data_json = json.dumps(element)

                print(element_data_json + ',')

    #
    # https://en.wikipedia.org/wiki/List_of_countries_by_natural_gas_imports
    def test_extract_the_list_of_countries_by_natural_gas_imports(self):
        print("test_extract_the_list_of_countries_by_natural_gas_imports")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/51.0.2704.103'
        }

        url = "https://en.wikipedia.org/wiki/List_of_countries_by_natural_gas_imports"

        rt = RequestsTor()

        html_with_tor = rt.get(url, headers=headers)

        soup = BeautifulSoup(html_with_tor.content, 'html.parser')

        if soup.find_all('tbody')[1].find('tr') is not None:
            all_tr = soup.find_all('tbody')[1].find_all('tr')

            for tr in all_tr:
                all_td = tr.find_all('td')

                country_region = ''
                natural_gas_imports_in_cubic_meter_per_year = ''
                date_of_information = ''

                for a in range(0, len(all_td)):
                    if a == 0:
                        country_region += all_td[a].text.replace('\n', '').replace('\u00a0', '').replace('\u202f*', '')
                    elif a == 1:
                        natural_gas_imports_in_cubic_meter_per_year += all_td[a].text.replace('\n', '')\
                            .replace(',', '').replace(' (2022)', '').replace(' (2020)', '').replace('\u00a0', '')
                    elif a == 2:
                        date_of_information += all_td[a].text.replace('\n', '').replace(',', '').replace(' est.', '')

                element = {
                    'country_region': country_region,
                    'natural_gas_imports_in_cubic_meter_per_year': natural_gas_imports_in_cubic_meter_per_year,
                    'date_of_information': date_of_information
                }

                element_data_json = json.dumps(element)

                print(element_data_json + ',')


class UnitTestsDataMiningWikipediaForCoalWithDarkWeb(unittest.TestCase):
    # ok
    # https://en.wikipedia.org/wiki/List_of_countries_by_coal_reserves
    def test_extract_the_list_of_countries_by_coal_reserves(self):
        print("test_extract_the_list_of_countries_by_coal_reserves")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://en.wikipedia.org/wiki/List_of_countries_by_coal_reserves"

        rt = RequestsTor()

        html_with_tor = rt.get(url, headers=headers)

        soup = BeautifulSoup(html_with_tor.content, 'html.parser')

        if soup.find_all('tbody')[2].find('tr') is not None:
            all_tr = soup.find_all('tbody')[2].find_all('tr')

            for tr in all_tr:
                all_td = tr.find_all('td')

                rank = ''
                country = ''
                anthracite_and_bituminous_in_millions_tonnes = ''
                anthracite_and_bituminous_in_percentage = ''
                subbituminous_and_lignite_in_millions_tonnes = ''
                subbituminous_and_lignite_in_percentage = ''
                total_in_millions_tonnes = ''
                total_in_percentage = ''

                for a in range(0, len(all_td)):
                    if a == 0:
                        rank += all_td[a].text.replace('\n', '').replace('\u00a0', '').replace('\u202f*', '').replace(',', '')
                    elif a == 1:
                        country += all_td[a].text.replace('\n', '').replace(',', '')\
                            .replace(' (2022)', '').replace(' (2020)', '').replace('\u00a0', '').replace(',', '')
                    elif a == 2:
                        anthracite_and_bituminous_in_millions_tonnes += all_td[a].text.replace('\n', '').replace(',', '')
                    elif a == 3:
                        anthracite_and_bituminous_in_percentage += all_td[a].text.replace('\n', '').replace(',', '')
                    elif a == 4:
                        subbituminous_and_lignite_in_millions_tonnes += all_td[a].text.replace('\n', '').replace(',', '')
                    elif a == 5:
                        subbituminous_and_lignite_in_percentage += all_td[a].text.replace('\n', '')\
                            .replace(' (2019)', '').replace(',', '')
                    elif a == 6:
                        total_in_millions_tonnes += all_td[a].text.replace('\n', '').replace('-', '').replace(',', '')
                    elif a == 7:
                        total_in_percentage += all_td[a].text.replace('\n', '').replace('-', '').replace(',', '')

                element = {
                    'rank': rank,
                    'country': country,
                    'anthracite_and_bituminous_in_millions_tonnes': anthracite_and_bituminous_in_millions_tonnes,
                    'anthracite_and_bituminous_in_percentage': anthracite_and_bituminous_in_percentage,
                    'subbituminous_and_lignite_in_millions_tonnes': subbituminous_and_lignite_in_millions_tonnes,
                    'subbituminous_and_lignite_in_percentage': subbituminous_and_lignite_in_percentage,
                    'total_in_millions_tonnes': total_in_millions_tonnes,
                    'total_in_percentage': total_in_percentage
                }

                element_data_json = json.dumps(element)

                print(element_data_json + ',')

    # ok
    # https://en.wikipedia.org/wiki/List_of_countries_by_coal_production
    def test_extract_the_list_of_countries_by_coal_production(self):
        print("test_extract_the_list_of_countries_by_coal_production")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://en.wikipedia.org/wiki/List_of_countries_by_coal_production"

        rt = RequestsTor()

        html_with_tor = rt.get(url, headers=headers)

        soup = BeautifulSoup(html_with_tor.content, 'html.parser')

        if soup.find_all('tbody')[0].find('tr') is not None:
            all_tr = soup.find_all('tbody')[0].find_all('tr')

            for tr in all_tr:
                all_td = tr.find_all('td')

                country = ''
                year_2020_in_millions_tonnes = ''
                year_2019_in_millions_tonnes = ''
                year_2018_in_millions_tonnes = ''
                year_2017_in_millions_tonnes = ''
                year_2016_in_millions_tonnes = ''
                year_2015_in_millions_tonnes = ''
                year_2014_in_millions_tonnes = ''
                year_2013_in_millions_tonnes = ''
                year_2007_in_millions_tonnes = ''

                for a in range(0, len(all_td)):
                    if a == 0:
                        country += all_td[a].text.replace('\n', '').replace('\u00a0', '').replace('\u202f*', '')\
                            .replace(',', '')
                    elif a == 1:
                        year_2020_in_millions_tonnes  += all_td[a].text.replace('\n', '').replace(',', '')\
                            .replace(' (2022)', '').replace(' (2020)', '').replace('\u00a0', '').replace(',', '')
                    elif a == 2:
                        year_2019_in_millions_tonnes += all_td[a].text.replace('\n', '').replace(',', '')
                    elif a == 3:
                        year_2018_in_millions_tonnes += all_td[a].text.replace('\n', '').replace(',', '')
                    elif a == 4:
                        year_2017_in_millions_tonnes += all_td[a].text.replace('\n', '').replace(',', '')
                    elif a == 5:
                        year_2016_in_millions_tonnes += all_td[a].text.replace('\n', '')\
                            .replace(' (2019)', '').replace(',', '')
                    elif a == 6:
                        year_2015_in_millions_tonnes += all_td[a].text.replace('\n', '').replace('-', '')\
                            .replace(',', '')
                    elif a == 7:
                        year_2014_in_millions_tonnes += all_td[a].text.replace('\n', '').replace('-', '')\
                            .replace(',', '')
                    elif a == 8:
                        year_2013_in_millions_tonnes += all_td[a].text.replace('\n', '').replace('-', '')\
                            .replace(',', '')
                    elif a == 9:
                        year_2007_in_millions_tonnes += all_td[a].text.replace('\n', '').replace('-', '')\
                            .replace(',', '')

                element = {
                    'country': country,
                    'year_2020_in_millions_tonnes': year_2020_in_millions_tonnes,
                    'year_2019_in_millions_tonnes': year_2019_in_millions_tonnes,
                    'year_2018_in_millions_tonnes': year_2018_in_millions_tonnes,
                    'year_2017_in_millions_tonnes': year_2017_in_millions_tonnes,
                    'year_2016_in_millions_tonnes': year_2016_in_millions_tonnes,
                    'year_2015_in_millions_tonnes': year_2015_in_millions_tonnes,
                    'year_2014_in_millions_tonnes': year_2014_in_millions_tonnes,
                    'year_2013_in_millions_tonnes': year_2013_in_millions_tonnes,
                    'year_2007_in_millions_tonnes': year_2007_in_millions_tonnes,
                }

                element_data_json = json.dumps(element)

                print(element_data_json + ',')

    # ok
    # https://en.wikipedia.org/wiki/Coal
    def test_extract_the_list_of_countries_by_coal_consumption(self):
        print("test_extract_the_list_of_countries_by_coal_consumption")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://en.wikipedia.org/wiki/Coal"

        rt = RequestsTor()

        html_with_tor = rt.get(url, headers=headers)

        soup = BeautifulSoup(html_with_tor.content, 'html.parser')

        if soup.find_all('tbody')[4].find('tr') is not None:
            all_tr = soup.find_all('tbody')[4].find_all('tr')

            for tr in all_tr:
                all_td = tr.find_all('td')

                country = ''
                year_2008_in_millions_tonnes = ''
                year_2009_in_millions_tonnes = ''
                year_2010_in_millions_tonnes = ''
                year_2011_in_millions_tonnes = ''
                year_2012_in_millions_tonnes = ''
                year_2013_in_millions_tonnes = ''
                year_2014_in_millions_tonnes = ''
                year_2015_in_millions_tonnes = ''
                year_2016_in_millions_tonnes = ''
                share = ''

                for a in range(0, len(all_td)):
                    if a == 0:
                        country += all_td[a].text.replace('\n', '').replace('\u00a0', '').replace('\u202f*', '')\
                            .replace(',', '')
                    elif a == 1:
                        year_2008_in_millions_tonnes  += all_td[a].text.replace('\n', '').replace(',', '')\
                            .replace(' (2022)', '').replace(' (2020)', '').replace('\u00a0', '').replace(',', '')
                    elif a == 2:
                        year_2009_in_millions_tonnes += all_td[a].text.replace('\n', '').replace(',', '')
                    elif a == 3:
                        year_2010_in_millions_tonnes += all_td[a].text.replace('\n', '').replace(',', '')
                    elif a == 4:
                        year_2011_in_millions_tonnes += all_td[a].text.replace('\n', '').replace(',', '')
                    elif a == 5:
                        year_2012_in_millions_tonnes += all_td[a].text.replace('\n', '')\
                            .replace(' (2019)', '').replace(',', '')
                    elif a == 6:
                        year_2013_in_millions_tonnes += all_td[a].text.replace('\n', '').replace('-', '')\
                            .replace(',', '')
                    elif a == 7:
                        year_2014_in_millions_tonnes += all_td[a].text.replace('\n', '').replace('-', '')\
                            .replace(',', '')
                    elif a == 8:
                        year_2015_in_millions_tonnes += all_td[a].text.replace('\n', '').replace('-', '')\
                            .replace(',', '').split(" = ")[1]
                    elif a == 9:
                        year_2016_in_millions_tonnes += all_td[a].text.replace('\n', '').replace('-', '')\
                            .replace(',', '').split(" = ")[1]
                    elif a == 10:
                        share += all_td[a].text.replace('\n', '').replace('-', '').replace(',', '')

                element = {
                    'country': country,
                    'year_2008_in_millions_tonnes': year_2008_in_millions_tonnes,
                    'year_2009_in_millions_tonnes': year_2009_in_millions_tonnes,
                    'year_2010_in_millions_tonnes': year_2010_in_millions_tonnes,
                    'year_2011_in_millions_tonnes': year_2011_in_millions_tonnes,
                    'year_2012_in_millions_tonnes': year_2012_in_millions_tonnes,
                    'year_2013_in_millions_tonnes': year_2013_in_millions_tonnes,
                    'year_2014_in_millions_tonnes': year_2014_in_millions_tonnes,
                    'year_2015_in_millions_tonnes': year_2015_in_millions_tonnes,
                    'year_2016_in_millions_tonnes': year_2016_in_millions_tonnes,
                    'share': share
                }

                element_data_json = json.dumps(element)

                print(element_data_json + ',')

    # ok
    # https://en.wikipedia.org/wiki/Coal
    def test_extract_the_list_of_countries_by_coal_exports(self):
        print("test_extract_the_list_of_countries_by_coal_exports")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://en.wikipedia.org/wiki/Coal"

        rt = RequestsTor()

        html_with_tor = rt.get(url, headers=headers)

        soup = BeautifulSoup(html_with_tor.content, 'html.parser')

        if soup.find_all('tbody')[5].find('tr') is not None:
            all_tr = soup.find_all('tbody')[5].find_all('tr')

            for tr in all_tr:
                all_td = tr.find_all('td')

                country = ''
                year_2008_in_millions_tonnes = ''

                for a in range(0, len(all_td)):
                    if a == 0:
                        country += all_td[a].text.replace('\n', '').replace('\u00a0', '').replace('\u202f*', '')\
                            .replace(',', '')
                    elif a == 1:
                        year_2008_in_millions_tonnes  += all_td[a].text.replace('\n', '').replace(',', '')\
                            .replace(' (2022)', '').replace(' (2020)', '').replace('\u00a0', '').replace(',', '')

                element = {
                    'country': country,
                    'year_2008_in_millions_tonnes': year_2008_in_millions_tonnes
                }

                element_data_json = json.dumps(element)

                print(element_data_json + ',')

    #
    # https://en.wikipedia.org/wiki/Coal
    def test_extract_the_list_of_countries_by_coal_imports(self):
        print("test_extract_the_list_of_countries_by_coal_imports")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/51.0.2704.103'
        }

        url = "https://en.wikipedia.org/wiki/Coal"

        rt = RequestsTor()

        html_with_tor = rt.get(url, headers=headers)

        soup = BeautifulSoup(html_with_tor.content, 'html.parser')

        if soup.find_all('tbody')[6].find('tr') is not None:
            all_tr = soup.find_all('tbody')[6].find_all('tr')

            for tr in all_tr:
                all_td = tr.find_all('td')

                country = ''
                year_2018_in_millions_tonnes = ''

                for a in range(0, len(all_td)):
                    if a == 0:
                        country += all_td[a].text.replace('\n', '').replace('\u00a0', '').replace('\u202f*', '')\
                            .replace(',', '')
                    elif a == 1:
                        year_2018_in_millions_tonnes  += all_td[a].text.replace('\n', '').replace(',', '')\
                            .replace(' (2022)', '').replace(' (2020)', '').replace('\u00a0', '').replace(',', '')

                element = {
                    'country': country,
                    'year_2018_in_millions_tonnes': year_2018_in_millions_tonnes
                }

                element_data_json = json.dumps(element)

                print(element_data_json + ',')


class UnitTestsDataMiningWikipediaForOilWithDarkWeb(unittest.TestCase):
    # ok
    # https://en.wikipedia.org/wiki/List_of_countries_by_proven_oil_reserves
    def test_extract_the_list_of_countries_by_proven_oil_reserves(self):
        print("test_extract_the_list_of_countries_by_proven_oil_reserves")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://en.wikipedia.org/wiki/List_of_countries_by_proven_oil_reserves"

        rt = RequestsTor()

        html_with_tor = rt.get(url, headers=headers)

        soup = BeautifulSoup(html_with_tor.content, 'html.parser')

        if soup.find_all('tbody')[1].find('tr') is not None:
            all_tr = soup.find_all('tbody')[1].find_all('tr')

            for tr in all_tr:
                all_td = tr.find_all('td')

                country = ''
                us_eia_in_millions_barrels = ''
                opec_in_millions_barrels = ''
                bp_in_millions_barrels = ''
                others_in_millions_barrels = ''
                oil_production_in_year_2020_in_barrel_per_day = ''
                years_of_production_in_reserve = ''

                for a in range(0, len(all_td)):
                    country = tr.find('th').find_all('a')[0].text.replace('\n', '').replace('\u00a0', '')\
                        .replace('\u202f*', '').replace(',', '').replace(' *', '')

                    if a == 0:
                        us_eia_in_millions_barrels += all_td[a].text.replace('\n', '').replace(',', '')\
                            .replace(' (2022)', '').replace(' (2020)', '').replace('\u00a0', '')\
                            .replace(',', '').replace('[10] ', '').replace('[11] ', '').replace('[12] ', '')\
                            .replace('[13] ', '').replace('[14] ', '')
                    elif a == 1:
                        opec_in_millions_barrels += all_td[a].text.replace('\n', '').replace(',', '')\
                            .replace('[10] ', '').replace('[11] ', '').replace('[12] ', '')\
                            .replace('[13] ', '').replace('[14] ', '')
                    elif a == 2:
                        bp_in_millions_barrels += all_td[a].text.replace('\n', '').replace(',', '')\
                            .replace('[10] ', '').replace('[11] ', '').replace('[12] ', '')\
                            .replace('[13] ', '').replace('[14] ', '')
                    elif a == 3:
                        others_in_millions_barrels += all_td[a].text.replace('\n', '').replace(',', '')\
                            .replace('[10] ', '').replace('[11] ', '').replace('[12] ', '')\
                            .replace('[13] ', '').replace('[14] ', '')
                    elif a == 4:
                        oil_production_in_year_2020_in_barrel_per_day += all_td[a].text.replace('\n', '')\
                            .replace(' (2019)', '').replace(',', '').replace('[10] ', '').replace('[11] ', '')\
                            .replace('[12] ', '').replace('[13] ', '').replace('[14] ', '')
                    elif a == 5:
                        years_of_production_in_reserve += all_td[a].text.replace('\n', '').replace('-', '')\
                            .replace(',', '')

                element = {
                    'country': country,
                    'us_eia_in_millions_barrels': us_eia_in_millions_barrels,
                    'opec_in_millions_barrels': opec_in_millions_barrels,
                    'bp_in_millions_barrels': bp_in_millions_barrels,
                    'others_in_millions_barrels': others_in_millions_barrels,
                    'oil_production_in_year_2020_in_barrel_per_day': oil_production_in_year_2020_in_barrel_per_day,
                    'years_of_production_in_reserve': years_of_production_in_reserve
                }

                element_data_json = json.dumps(element)

                print(element_data_json + ',')

    # ok
    # https://en.wikipedia.org/wiki/List_of_countries_by_oil_production
    def test_extract_the_list_of_countries_by_oil_production(self):
        print("test_extract_the_list_of_countries_by_oil_production")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://en.wikipedia.org/wiki/List_of_countries_by_oil_production"

        rt = RequestsTor()

        html_with_tor = rt.get(url, headers=headers)

        soup = BeautifulSoup(html_with_tor.content, 'html.parser')

        if soup.find_all('tbody')[0].find('tr') is not None:
            all_tr = soup.find_all('tbody')[0].find_all('tr')

            for tr in all_tr:
                all_td = tr.find_all('td')

                country = ''
                oil_production_in_year_2021_in_barrel_per_day = ''
                oil_production_per_capita_in_year_2017_in_barrel_per_day_per_million_people = ''

                for a in range(0, len(all_td)):
                    if a == 0:
                        country += all_td[a].text.replace('\n', '').replace(',', '')\
                            .replace(' (2022)', '').replace(' (2020)', '').replace('\u00a0', '')\
                            .replace(',', '').replace('[10] ', '').replace('[11] ', '').replace('[12] ', '')\
                            .replace('[13] ', '').replace('[14] ', '').replace(' (OPEC)', '')
                    elif a == 1:
                        oil_production_in_year_2021_in_barrel_per_day += all_td[a].text.replace('\n', '')\
                            .replace(',', '')\
                            .replace('[10] ', '').replace('[11] ', '').replace('[12] ', '')\
                            .replace('[13] ', '').replace('[14] ', '')
                    elif a == 2:
                        oil_production_per_capita_in_year_2017_in_barrel_per_day_per_million_people += all_td[a]\
                            .text.replace('\n', '').replace(',', '')\
                            .replace('[10] ', '').replace('[11] ', '').replace('[12] ', '')\
                            .replace('[13] ', '').replace('[14] ', '')

                element = {
                    'country': country,
                    'oil_production_in_year_2021_in_barrel_per_day': oil_production_in_year_2021_in_barrel_per_day,
                    'oil_production_per_capita_in_year_2017_in_barrel_per_day_per_million_people':
                        oil_production_per_capita_in_year_2017_in_barrel_per_day_per_million_people,
                }

                element_data_json = json.dumps(element)

                print(element_data_json + ',')

    # ok
    # https://en.wikipedia.org/wiki/List_of_countries_by_oil_consumption
    def test_extract_the_list_of_countries_by_oil_consumption(self):
        print("test_extract_the_list_of_countries_by_oil_consumption")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://en.wikipedia.org/wiki/List_of_countries_by_oil_consumption"

        rt = RequestsTor()

        html_with_tor = rt.get(url, headers=headers)

        soup = BeautifulSoup(html_with_tor.content, 'html.parser')

        if soup.find_all('tbody')[0].find('tr') is not None:
            all_tr = soup.find_all('tbody')[0].find_all('tr')

            for tr in all_tr:
                all_td = tr.find_all('td')

                rank = ''
                country_or_region = ''
                oil_consumption_in_barrel_per_day = ''
                year = ''
                percentage = ''

                for a in range(0, len(all_td)):
                    if a == 0:
                        rank += all_td[a].text.replace('\n', '').replace(',', '')\
                            .replace(' (2022)', '').replace(' (2020)', '').replace('\u00a0', '')\
                            .replace(',', '').replace('[10] ', '').replace('[11] ', '').replace('[12] ', '')\
                            .replace('[13] ', '').replace('[14] ', '').replace(' (OPEC)', '').replace('[5]', '')
                    elif a == 1:
                        country_or_region += all_td[a].text.replace('\n', '')\
                            .replace(',', '')\
                            .replace('[10] ', '').replace('[11] ', '').replace('[12] ', '')\
                            .replace('[13] ', '').replace('[14] ', '').replace('\u00a0', '').replace('[5]', '')
                    elif a == 2:
                        oil_consumption_in_barrel_per_day += all_td[a]\
                            .text.replace('\n', '').replace(',', '')\
                            .replace('[10] ', '').replace('[11] ', '').replace('[12] ', '')\
                            .replace('[13] ', '').replace('[14] ', '').replace('[5]', '')
                    elif a == 3:
                        year += all_td[a]\
                            .text.replace('\n', '').replace(',', '')\
                            .replace('[10] ', '').replace('[11] ', '').replace('[12] ', '')\
                            .replace('[13] ', '').replace('[14] ', '').replace(' est.', '').replace('[5]', '')
                    elif a == 4:
                        percentage += all_td[a]\
                            .text.replace('\n', '').replace(',', '')\
                            .replace('[10] ', '').replace('[11] ', '').replace('[12] ', '')\
                            .replace('[13] ', '').replace('[14] ', '').replace('[5]', '')

                element = {
                    'rank': rank,
                    'country_or_region': country_or_region,
                    'oil_consumption_in_barrel_per_day': oil_consumption_in_barrel_per_day,
                    'year': year,
                    'percentage': percentage
                }

                element_data_json = json.dumps(element)

                print(element_data_json + ',')

    # ok
    # https://en.wikipedia.org/wiki/List_of_countries_by_oil_exports
    def test_extract_the_list_of_countries_by_oil_exports(self):
        print("test_extract_the_list_of_countries_by_oil_exports")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://en.wikipedia.org/wiki/List_of_countries_by_oil_exports"

        rt = RequestsTor()

        html_with_tor = rt.get(url, headers=headers)

        soup = BeautifulSoup(html_with_tor.content, 'html.parser')

        if soup.find_all('tbody')[0].find('tr') is not None:
            all_tr = soup.find_all('tbody')[0].find_all('tr')

            for tr in all_tr:
                all_td = tr.find_all('td')

                country_or_region = ''
                oil_exports_in_barrel_per_day = ''
                date_of_information = ''

                for a in range(0, len(all_td)):
                    if a == 0:
                        country_or_region += all_td[a].text.replace('\n', '').replace(',', '')\
                            .replace(' (2022)', '').replace(' (2020)', '').replace('\u00a0', '')\
                            .replace(',', '').replace('[10] ', '').replace('[11] ', '').replace('[12] ', '')\
                            .replace('[13] ', '').replace('[14] ', '').replace(' (OPEC)', '').replace('[5]', '')\
                            .replace(' est.', '')
                    elif a == 1:
                        oil_exports_in_barrel_per_day += all_td[a].text.replace('\n', '')\
                            .replace(',', '')\
                            .replace('[10] ', '').replace('[11] ', '').replace('[12] ', '')\
                            .replace('[13] ', '').replace('[14] ', '').replace('\u00a0', '').replace('[5]', '')\
                            .replace(' est.', '')
                    elif a == 2:
                        date_of_information += all_td[a]\
                            .text.replace('\n', '').replace(',', '')\
                            .replace('[10] ', '').replace('[11] ', '').replace('[12] ', '')\
                            .replace('[13] ', '').replace('[14] ', '').replace('[5]', '')\
                            .replace(' est.', '')

                element = {
                    'country_or_region': country_or_region,
                    'oil_exports_in_barrel_per_day': oil_exports_in_barrel_per_day,
                    'date_of_information': date_of_information
                }

                element_data_json = json.dumps(element)

                print(element_data_json + ',')

    # ok
    # https://en.wikipedia.org/wiki/List_of_countries_by_oil_imports
    def test_extract_the_list_of_countries_by_oil_imports(self):
        print("test_extract_the_list_of_countries_by_oil_imports")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://en.wikipedia.org/wiki/List_of_countries_by_oil_imports"

        rt = RequestsTor()

        html_with_tor = rt.get(url, headers=headers)

        soup = BeautifulSoup(html_with_tor.content, 'html.parser')

        if soup.find_all('tbody')[1].find('tr') is not None:
            all_tr = soup.find_all('tbody')[1].find_all('tr')

            for tr in all_tr:
                all_td = tr.find_all('td')

                country_or_region = ''
                crude_oil_imports_in_barrel_per_day = ''
                year_of_information = ''

                for a in range(0, len(all_td)):
                    if a == 0:
                        country_or_region += all_td[a].text.replace('\n', '').replace(',', '')\
                            .replace(' (2022)', '').replace(' (2020)', '').replace('\u00a0', '')\
                            .replace(',', '').replace('[10] ', '').replace('[11] ', '').replace('[12] ', '')\
                            .replace('[13] ', '').replace('[14] ', '').replace(' (OPEC)', '').replace('[5]', '')\
                            .replace(' est.', '').replace('[3]', '').replace('[4]', '')
                    elif a == 1:
                        crude_oil_imports_in_barrel_per_day += all_td[a].text.replace('\n', '')\
                            .replace(',', '')\
                            .replace('[10] ', '').replace('[11] ', '').replace('[12] ', '')\
                            .replace('[13] ', '').replace('[14] ', '').replace('\u00a0', '').replace('[5]', '')\
                            .replace(' est.', '').replace('[3]', '').replace('[4]', '')
                    elif a == 2:
                        year_of_information += all_td[a]\
                            .text.replace('\n', '').replace(',', '')\
                            .replace('[10] ', '').replace('[11] ', '').replace('[12] ', '')\
                            .replace('[13] ', '').replace('[14] ', '').replace('[5]', '')\
                            .replace(' est.', '').replace('[3]', '').replace('[4]', '')

                element = {
                    'country_or_region': country_or_region,
                    'crude_oil_imports_in_barrel_per_day': crude_oil_imports_in_barrel_per_day,
                    'year_of_information': year_of_information
                }

                element_data_json = json.dumps(element)

                print(element_data_json + ',')

    # ok
    # https://en.wikipedia.org/wiki/List_of_countries_by_net_oil_exports
    def test_extract_the_list_of_countries_by_net_oil_exports(self):
        print("test_extract_the_list_of_countries_by_net_oil_exports")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://en.wikipedia.org/wiki/List_of_countries_by_net_oil_exports"

        rt = RequestsTor()

        html_with_tor = rt.get(url, headers=headers)

        soup = BeautifulSoup(html_with_tor.content, 'html.parser')

        if soup.find_all('tbody')[0].find('tr') is not None:
            all_tr = soup.find_all('tbody')[0].find_all('tr')

            for tr in all_tr:
                all_td = tr.find_all('td')

                rank = ''
                country = ''
                exports_in_barrel_per_day = ''
                year_for_export_data = ''
                imports_in_barrel_per_day = ''
                year_for_import_data = ''
                net_exports_in_barrel_per_day = ''
                domestic_production_in_year_2016 = ''

                for a in range(0, len(all_td)):
                    if a == 0:
                        rank += all_td[a].text.replace('\n', '').replace(',', '')\
                            .replace(' (2022)', '').replace(' (2020)', '').replace('\u00a0', '')\
                            .replace(',', '').replace('[10] ', '').replace('[11] ', '').replace('[12] ', '')\
                            .replace('[13] ', '').replace('[14] ', '').replace(' (OPEC)', '').replace('[5]', '')\
                            .replace(' est.', '')
                    elif a == 1:
                        country += all_td[a].text.replace('\n', '')\
                            .replace(',', '')\
                            .replace('[10] ', '').replace('[11] ', '').replace('[12] ', '')\
                            .replace('[13] ', '').replace('[14] ', '').replace('\u00a0', '').replace('[5]', '')\
                            .replace(' est.', '')
                    elif a == 2:
                        exports_in_barrel_per_day += all_td[a]\
                            .text.replace('\n', '').replace(',', '')\
                            .replace('[10] ', '').replace('[11] ', '').replace('[12] ', '')\
                            .replace('[13] ', '').replace('[14] ', '').replace('[5]', '').replace(' est.', '')
                    elif a == 3:
                        year_for_export_data += all_td[a]\
                            .text.replace('\n', '').replace(',', '')\
                            .replace('[10] ', '').replace('[11] ', '').replace('[12] ', '')\
                            .replace('[13] ', '').replace('[14] ', '').replace(' est.', '').replace('[5]', '')\
                            .replace(' est.', '')
                    elif a == 4:
                        imports_in_barrel_per_day += all_td[a]\
                            .text.replace('\n', '').replace(',', '')\
                            .replace('[10] ', '').replace('[11] ', '').replace('[12] ', '')\
                            .replace('[13] ', '').replace('[14] ', '').replace('[5]', '').replace(' est.', '')
                    elif a == 5:
                        year_for_import_data += all_td[a]\
                            .text.replace('\n', '').replace(',', '')\
                            .replace('[10] ', '').replace('[11] ', '').replace('[12] ', '')\
                            .replace('[13] ', '').replace('[14] ', '').replace('[5]', '').replace(' est.', '')
                    elif a == 6:
                        net_exports_in_barrel_per_day += all_td[a]\
                            .text.replace('\n', '').replace(',', '')\
                            .replace('[10] ', '').replace('[11] ', '').replace('[12] ', '')\
                            .replace('[13] ', '').replace('[14] ', '').replace('[5]', '').replace(' est.', '')
                    elif a == 7:
                        domestic_production_in_year_2016 += all_td[a]\
                            .text.replace('\n', '').replace(',', '')\
                            .replace('[10] ', '').replace('[11] ', '').replace('[12] ', '')\
                            .replace('[13] ', '').replace('[14] ', '').replace('[5]', '').replace(' est.', '')\
                            .replace(' 2017', '')

                element = {
                    'rank': rank,
                    'country': country,
                    'exports_in_barrel_per_day': exports_in_barrel_per_day,
                    'year_for_export_data': year_for_export_data,
                    'imports_in_barrel_per_day': imports_in_barrel_per_day,
                    'year_for_import_data': year_for_import_data,
                    'net_exports_in_barrel_per_day': net_exports_in_barrel_per_day,
                    'domestic_production_in_year_2016': domestic_production_in_year_2016
                }

                element_data_json = json.dumps(element)

                print(element_data_json + ',')


class UnitTestsDataMiningWikipediaForUranium(unittest.TestCase):
    # ok
    # https://en.wikipedia.org/wiki/List_of_countries_by_uranium_reserves
    def test_extract_the_list_of_countries_by_uranium_reserves(self):
        print("test_extract_the_list_of_countries_by_uranium_reserves")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://en.wikipedia.org/wiki/List_of_countries_by_uranium_reserves"

        rt = RequestsTor()

        html_with_tor = rt.get(url, headers=headers)

        soup = BeautifulSoup(html_with_tor.content, 'html.parser')

        if soup.find_all('tbody')[0].find('tr') is not None:
            all_tr = soup.find_all('tbody')[0].find_all('tr')

            for tr in all_tr:
                all_td = tr.find_all('td')

                country = ''
                reserves_as_of_2019_in_tonnes = ''
                historical_production_to_2014_in_tonnes = ''

                for a in range(0, len(all_td)):
                    country = tr.find('th').find_all('a')[0].get('title').replace('\n', '').replace('\u00a0', '')\
                        .replace('\u202f*', '').replace(',', '').replace(' *', '')

                    if a == 0:
                        reserves_as_of_2019_in_tonnes += all_td[a].text.replace('\n', '').replace(',', '')\
                            .replace(' (2022)', '').replace(' (2020)', '').replace('\u00a0', '')\
                            .replace(',', '').replace('[10] ', '').replace('[11] ', '').replace('[12] ', '')\
                            .replace('[13] ', '').replace('[14] ', '')
                    elif a == 1:
                        historical_production_to_2014_in_tonnes += all_td[a].text.replace('\n', '').replace(',', '')\
                            .replace('[10] ', '').replace('[11] ', '').replace('[12] ', '')\
                            .replace('[13] ', '').replace('[14] ', '')

                element = {
                    'country': country,
                    'reserves_as_of_2019_in_tonnes': reserves_as_of_2019_in_tonnes,
                    'historical_production_to_2014_in_tonnes': historical_production_to_2014_in_tonnes
                }

                element_data_json = json.dumps(element)

                print(element_data_json + ',')

    # ok
    # https://en.wikipedia.org/wiki/List_of_countries_by_uranium_production
    def test_extract_the_list_of_countries_by_uranium_production(self):
        print("test_extract_the_list_of_countries_by_uranium_production")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/51.0.2704.103'
        }

        url = "https://en.wikipedia.org/wiki/List_of_countries_by_uranium_production"

        rt = RequestsTor()

        html_with_tor = rt.get(url, headers=headers)

        soup = BeautifulSoup(html_with_tor.content, 'html.parser')

        if soup.find_all('tbody')[0].find('tr') is not None:
            all_tr = soup.find_all('tbody')[0].find_all('tr')

            for tr in all_tr:
                all_td = tr.find_all('td')

                rank = ''
                country_or_region = ''
                uranium_production_in_2018_in_tonnes = ''
                percentage_of_world_production_in_2018 = ''

                for a in range(0, len(all_td)):
                    if a == 0:
                        rank += all_td[a].text.replace('\n', '').replace(',', '')\
                            .replace(' (2022)', '').replace(' (2020)', '').replace('\u00a0', '')\
                            .replace(',', '').replace('[10] ', '').replace('[11] ', '').replace('[12] ', '')\
                            .replace('[13] ', '').replace('[14] ', '').replace('[2]', '').replace('[3]', '')
                    elif a == 1:
                        country_or_region += all_td[a].text.replace('\n', '').replace(',', '')\
                            .replace('[10] ', '').replace('[11] ', '').replace('[12] ', '')\
                            .replace('[13] ', '').replace('[14] ', '').replace('\u00a0', '').replace('[2]', '')\
                            .replace('[3]', '')
                    elif a == 2:
                        uranium_production_in_2018_in_tonnes += all_td[a].text.replace('\n', '').replace(',', '')\
                            .replace('[10] ', '').replace('[11] ', '').replace('[12] ', '')\
                            .replace('[13] ', '').replace('[14] ', '').replace('[2]', '').replace('[3]', '')
                    elif a == 3:
                        percentage_of_world_production_in_2018 += all_td[a].text.replace('\n', '').replace(',', '')\
                            .replace('[10] ', '').replace('[11] ', '').replace('[12] ', '')\
                            .replace('[13] ', '').replace('[14] ', '').replace('[2]', '').replace('[3]', '')

                element = {
                    'rank': rank,
                    'country_or_region': country_or_region,
                    'uranium_production_in_2018_in_tonnes': uranium_production_in_2018_in_tonnes,
                    'percentage_of_world_production_in_2018': percentage_of_world_production_in_2018
                }

                element_data_json = json.dumps(element)

                print(element_data_json + ',')

    # ok
    # https://www.worldatlas.com/articles/the-leading-uranium-consuming-countries-in-the-world.html
    def test_extract_the_list_of_countries_by_uranium_consumption(self):
        print("test_extract_the_list_of_countries_by_uranium_consumption")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/51.0.2704.103'
        }

        url = "https://www.worldatlas.com/articles/the-leading-uranium-consuming-countries-in-the-world.html"

        rt = RequestsTor()

        html_with_tor = rt.get(url, headers=headers)

        soup = BeautifulSoup(html_with_tor.content, 'html.parser')

        if soup.find_all('tbody')[0].find('tr') is not None:
            all_tr = soup.find_all('tbody')[0].find_all('tr')

            for tr in all_tr:
                all_td = tr.find_all('td')

                rank = ''
                country_or_region = ''
                uranium_consumption_in_2015_in_thousands_of_tonnes = ''

                for a in range(0, len(all_td)):
                    if a == 0:
                        rank += all_td[a].text.replace('\n', '').replace(',', '')\
                            .replace(' (2022)', '').replace(' (2020)', '').replace('\u00a0', '')\
                            .replace(',', '').replace('[10] ', '').replace('[11] ', '').replace('[12] ', '')\
                            .replace('[13] ', '').replace('[14] ', '').replace('[2]', '').replace('[3]', '')
                    elif a == 1:
                        country_or_region += all_td[a].text.replace('\n', '').replace(',', '')\
                            .replace('[10] ', '').replace('[11] ', '').replace('[12] ', '')\
                            .replace('[13] ', '').replace('[14] ', '').replace('\u00a0', '').replace('[2]', '')\
                            .replace('[3]', '')
                    elif a == 2:
                        uranium_consumption_in_2015_in_thousands_of_tonnes += all_td[a].text.replace('\n', '').replace(',', '')\
                            .replace('[10] ', '').replace('[11] ', '').replace('[12] ', '')\
                            .replace('[13] ', '').replace('[14] ', '').replace('[2]', '').replace('[3]', '')

                element = {
                    'rank': rank,
                    'country_or_region': country_or_region,
                    'uranium_consumption_in_2015_in_thousands_of_tonnes':
                        uranium_consumption_in_2015_in_thousands_of_tonnes
                }

                element_data_json = json.dumps(element)

                print(element_data_json + ',')

    # ok
    # https://www.worldstopexports.com/uranium-exports-by-country/
    def test_extract_the_list_of_countries_by_natural_uranium_exports(self):
        print("test_extract_the_list_of_countries_by_natural_uranium_exports")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/51.0.2704.103'
        }

        url = "https://www.worldstopexports.com/uranium-exports-by-country/"

        html = requests.get(url, headers=headers)

        soup = BeautifulSoup(html.content, 'html.parser')

        if soup.find_all('ol')[0].find('li') is not None:
            all_li = soup.find_all('ol')[0].find_all('li')

            for li in all_li:
                country_or_region = ""
                highest_dollar_value_worth_during_2021 = ""
                percentage_of_exports_during_2021 = ""

                country_or_region += li.text.split(':')[0]
                highest_dollar_value_worth_during_2021 += li.text.split(': ')[1].split(' (')[0]
                percentage_of_exports_during_2021 += li.text.split(': ')[1].split(' (')[1].replace(')', '').split('%')[0]

                element = {
                    'country_or_region': country_or_region,
                    'highest_dollar_value_worth_during_2021': highest_dollar_value_worth_during_2021,
                    'percentage_of_exports_during_2021': percentage_of_exports_during_2021
                }

                element_data_json = json.dumps(element)

                print(element_data_json + ',')

    # ok
    # https://www.worldstopexports.com/uranium-exports-by-country/
    def test_extract_the_list_of_countries_by_enriched_uranium_exports(self):
        print("test_extract_the_list_of_countries_by_enriched_uranium_exports")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/51.0.2704.103'
        }

        url = "https://www.worldstopexports.com/uranium-exports-by-country/"

        html = requests.get(url, headers=headers)

        soup = BeautifulSoup(html.content, 'html.parser')

        if soup.find_all('ol')[1].find('li') is not None:
            all_li = soup.find_all('ol')[1].find_all('li')

            for li in all_li:
                country_or_region = ""
                highest_dollar_value_worth_during_2021 = ""
                percentage_of_exports_during_2021 = ""

                country_or_region += li.text.split(':')[0]
                highest_dollar_value_worth_during_2021 += li.text.split(': ')[1].split(' (')[0]
                percentage_of_exports_during_2021 += li.text.split(': ')[1].split(' (')[1].replace(')', '').split('%')[0]

                element = {
                    'country_or_region': country_or_region,
                    'highest_dollar_value_worth_during_2021': highest_dollar_value_worth_during_2021,
                    'percentage_of_exports_during_2021': percentage_of_exports_during_2021
                }

                element_data_json = json.dumps(element)

                print(element_data_json + ',')

    # ok
    # https://www.worldstopexports.com/uranium-exports-by-country/
    def test_extract_the_list_of_countries_by_depleted_uranium_exports(self):
        print("test_extract_the_list_of_countries_by_depleted_uranium_exports")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/51.0.2704.103'
        }

        url = "https://www.worldstopexports.com/uranium-exports-by-country/"

        html = requests.get(url, headers=headers)

        soup = BeautifulSoup(html.content, 'html.parser')

        if soup.find_all('ol')[2].find('li') is not None:
            all_li = soup.find_all('ol')[2].find_all('li')

            for li in all_li:
                country_or_region = ""
                highest_dollar_value_worth_during_2021 = ""
                percentage_of_exports_during_2021 = ""

                country_or_region += li.text.split(':')[0]
                highest_dollar_value_worth_during_2021 += li.text.split(': ')[1].split(' (')[0].replace(',', '')
                percentage_of_exports_during_2021 += li.text.split(': ')[1].split(' (')[1].replace(')', '').split('%')[0]

                element = {
                    'country_or_region': country_or_region,
                    'highest_dollar_value_worth_during_2021': highest_dollar_value_worth_during_2021,
                    'percentage_of_exports_during_2021': percentage_of_exports_during_2021
                }

                element_data_json = json.dumps(element)

                print(element_data_json + ',')

    # not ok
    # https://www.worldstopexports.com/uranium-exports-by-country/
    def test_extract_the_list_of_countries_by_major_uranium_companies(self):
        print("test_extract_the_list_of_countries_by_depleted_uranium_exports")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/51.0.2704.103'
        }

        url = "https://www.worldstopexports.com/uranium-exports-by-country/"

        html = requests.get(url, headers=headers)

        soup = BeautifulSoup(html.content, 'html.parser')

        if soup.find_all('ul')[9].find('li') is not None:
            all_li = soup.find_all('ul')[9].find_all('li')

            companies = []

            for i in range(0, len(all_li)):
                companies.append(all_li[i].text)

            element = {
                'companies': companies
            }

            element_data_json = json.dumps(element)

            print(element_data_json + ',')

    # ok
    # https://www.worldstopexports.com/us-uranium-imports-by-supplying-country/
    def test_extract_the_list_of_countries_exporting_natural_uranium_imports_to_america(self):
        print("test_extract_the_list_of_countries_exporting_natural_uranium_imports_to_america")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/51.0.2704.103'
        }

        url = "https://www.worldstopexports.com/us-uranium-imports-by-supplying-country/"

        html = requests.get(url, headers=headers)

        soup = BeautifulSoup(html.content, 'html.parser')

        if soup.find_all('ol')[1].find('li') is not None:
            all_li = soup.find_all('ol')[1].find_all('li')

            for li in all_li:
                country_or_region = ""
                highest_dollar_value_worth_during_2021 = ""
                percentage_of_imports_to_america_during_2021 = ""

                country_or_region += li.text.split(':')[0]
                highest_dollar_value_worth_during_2021 += li.text.split(': ')[1].split(' (')[0].replace(',', '')
                percentage_of_imports_to_america_during_2021 += li.text.split(': ')[1].split(' (')[1].replace(')', '')\
                    .split('%')[0]

                element = {
                    'country_or_region': country_or_region,
                    'highest_dollar_value_worth_during_2021': highest_dollar_value_worth_during_2021,
                    'percentage_of_imports_to_america_during_2021': percentage_of_imports_to_america_during_2021
                }

                element_data_json = json.dumps(element)

                print(element_data_json + ',')

    # ok
    # https://www.worldstopexports.com/us-uranium-imports-by-supplying-country/
    def test_extract_the_list_of_countries_exporting_enriched_uranium_imports_to_america(self):
        print("test_extract_the_list_of_countries_exporting_enriched_uranium_imports_to_america")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/51.0.2704.103'
        }

        url = "https://www.worldstopexports.com/us-uranium-imports-by-supplying-country/"

        html = requests.get(url, headers=headers)

        soup = BeautifulSoup(html.content, 'html.parser')

        if soup.find_all('ol')[0].find('li') is not None:
            all_li = soup.find_all('ol')[0].find_all('li')

            for li in all_li:
                country_or_region = ""
                highest_dollar_value_worth_during_2021 = ""
                percentage_of_imports_to_america_during_2021 = ""

                country_or_region += li.text.split(':')[0]
                highest_dollar_value_worth_during_2021 += li.text.split(': ')[1].split(' (')[0].replace(',', '')
                percentage_of_imports_to_america_during_2021 += li.text.split(': ')[1].split(' (')[1].replace(')', '')\
                    .split('%')[0]

                element = {
                    'country_or_region': country_or_region,
                    'highest_dollar_value_worth_during_2021': highest_dollar_value_worth_during_2021,
                    'percentage_of_imports_to_america_during_2021': percentage_of_imports_to_america_during_2021
                }

                element_data_json = json.dumps(element)

                print(element_data_json + ',')

    # not ok
    # https://www.statista.com/statistics/1147442/imports-of-uranium-to-eu-by-country/
    def test_extract_the_list_of_countries_exporting_natural_uranium_imports_of_uranium_to_eu(self):
        print("test_extract_the_list_of_countries_exporting_natural_uranium_imports_of_uranium_to_eu")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/51.0.2704.103'
        }

        url = "https://www.statista.com/statistics/1147442/imports-of-uranium-to-eu-by-country/"

        html = requests.get(url, headers=headers)

        print(html.content)

        soup = BeautifulSoup(html.content, 'html.parser')

        countries = []
        imports_of_natural_uranium_to_the_eu_in_2020 = []

        # countries
        if soup.find('g', {'class': 'highcharts-axis-labels highcharts-xaxis-labels'}) is not None:
            all_text = soup.find('g', {'class': 'highcharts-axis-labels highcharts-xaxis-labels'}).find_all('text')

            for tag_text in all_text:
                countries.append(tag_text.text)

        # imports_of_natural_uranium_to_the_eu_in_2020
        if soup.find('g', {'class': 'highcharts-label highcharts-data-label highcharts-data-label-color-0'}) is not None:
            all_g = soup.find_all('g', {'highcharts-label highcharts-data-label highcharts-data-label-color-0'})

            for tag_g in all_g:
                countries.append(tag_g.find('text').find('tspan')[0])

        for i in range(0, len(countries)):
            country = countries[i]
            import_of_natural_uranium_to_the_eu_in_2020 = imports_of_natural_uranium_to_the_eu_in_2020[i]

            element = {
                'country': country,
                'import_of_natural_uranium_to_the_eu_in_2020': import_of_natural_uranium_to_the_eu_in_2020,
            }

            element_data_json = json.dumps(element)

            print(element_data_json + ',')


class UnitTestsDataMiningWikipediaForElectricity(unittest.TestCase):
    # ok
    # https://en.wikipedia.org/wiki/List_of_countries_by_electricity_production
    def test_extract_the_list_of_countries_by_electricity_production(self):
        print("test_extract_the_list_of_countries_by_electricity_production")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://en.wikipedia.org/wiki/List_of_countries_by_electricity_production"

        rt = RequestsTor()

        html_with_tor = rt.get(url, headers=headers)

        soup = BeautifulSoup(html_with_tor.content, 'html.parser')

        if soup.find_all('tbody')[0].find('tr') is not None:
            all_tr = soup.find_all('tbody')[0].find_all('tr')

            for tr in all_tr:
                all_td = tr.find_all('td')

                country = ''
                electricity_production_in_gwh = ''
                year = ''

                for a in range(0, len(all_td)):
                    country = tr.find('th').text.replace('\n', '').replace('\u00a0', '')\
                        .replace('\u202f*', '').replace(',', '').replace(' *', '')

                    if a == 0:
                        electricity_production_in_gwh += all_td[a].text.replace('\n', '').replace(',', '')\
                            .replace(' (2022)', '').replace(' (2020)', '').replace('\u00a0', '')\
                            .replace(',', '').replace('[10] ', '').replace('[11] ', '').replace('[12] ', '')\
                            .replace('[13] ', '').replace('[14] ', '').replace('[1]', '')
                    elif a == 1:
                        if "]" in all_td[a].text.replace('\n', '').replace(',', ''):
                            year += all_td[a].text.replace('\n', '').replace(',', '').split(']')[1]
                        else:
                            year += all_td[a].text.replace('\n', '').replace(',', '')

                element = {
                    'country': country,
                    'electricity_production_in_gwh': electricity_production_in_gwh,
                    'year': year
                }

                element_data_json = json.dumps(element)

                print(element_data_json + ',')

    # ok
    # https://en.wikipedia.org/wiki/List_of_countries_by_electricity_consumption
    def test_extract_the_list_of_countries_by_electricity_consumption(self):
        print("test_extract_the_list_of_countries_by_electricity_consumption")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://en.wikipedia.org/wiki/List_of_countries_by_electricity_consumption"

        rt = RequestsTor()

        html_with_tor = rt.get(url, headers=headers)

        soup = BeautifulSoup(html_with_tor.content, 'html.parser')

        if soup.find_all('tbody')[0].find('tr') is not None:
            all_tr = soup.find_all('tbody')[0].find_all('tr')

            for tr in all_tr:
                all_td = tr.find_all('td')

                rank = ''
                country_or_region = ''
                total_electricity_consumption_in_gwh_per_year = ''
                year_of_data = ''
                source = ''
                population = ''
                as_of = ''
                average_electrical_power_per_capita_expressed_in_kwh_per_year = ''
                average_electrical_power_per_capita_expressed_in_watts = ''

                for a in range(0, len(all_td)):
                    if a == 0:
                        rank += all_td[a].text.replace('\n', '').replace(',', '')\
                            .replace(' (2022)', '').replace(' (2020)', '').replace('\u00a0', '')\
                            .replace('\u202f*', '')\
                            .replace(',', '').replace(' *', '').replace('[10] ', '').replace('[11] ', '')\
                            .replace('[12] ', '')\
                            .replace('[13] ', '').replace('[14] ', '').replace('[1]', '').replace('\u2014', '')
                    elif a == 1:
                        country_or_region += all_td[a].text.replace('\n', '').replace(',', '')\
                            .replace(' (2022)', '').replace(' (2020)', '').replace('\u00a0', '')\
                            .replace('\u202f*', '')\
                            .replace(',', '').replace(' *', '').replace('[10] ', '').replace('[11] ', '')\
                            .replace('[12] ', '')\
                            .replace('[13] ', '').replace('[14] ', '').replace('[1]', '')
                    elif a == 2:
                        total_electricity_consumption_in_gwh_per_year += all_td[a].text.replace('\n', '').replace(',', '')\
                            .replace(' (2022)', '').replace(' (2020)', '').replace('\u00a0', '')\
                            .replace('\u202f*', '')\
                            .replace(',', '').replace(' *', '').replace('[10] ', '').replace('[11] ', '')\
                            .replace('[12] ', '')\
                            .replace('[13] ', '').replace('[14] ', '').replace('[1]', '')
                    elif a == 3:
                        year_of_data += all_td[a].text.replace('\n', '').replace(',', '')\
                            .replace(' (2022)', '').replace(' (2020)', '').replace('\u00a0', '')\
                            .replace('\u202f*', '')\
                            .replace(',', '').replace(' *', '').replace('[10] ', '').replace('[11] ', '')\
                            .replace('[12] ', '')\
                            .replace('[13] ', '').replace('[14] ', '').replace('[1]', '').replace(' est.', '')
                    elif a == 4:
                        source += all_td[a].text.replace('\n', '').replace(',', '')\
                            .replace(' (2022)', '').replace(' (2020)', '').replace('\u00a0', '')\
                            .replace('\u202f*', '')\
                            .replace(',', '').replace(' *', '').replace('[10] ', '').replace('[11] ', '')\
                            .replace('[12] ', '')\
                            .replace('[13] ', '').replace('[14] ', '').replace('[1]', '')\
                            .replace('[6]', '').replace('[5]', '').replace('[4]', '')
                    elif a == 5:
                        population += all_td[a].text.replace('\n', '').replace(',', '')\
                            .replace(' (2022)', '').replace(' (2020)', '').replace('\u00a0', '')\
                            .replace('\u202f*', '')\
                            .replace(',', '').replace(' *', '').replace('[10] ', '').replace('[11] ', '')\
                            .replace('[12] ', '')\
                            .replace('[13] ', '').replace('[14] ', '').replace('[1]', '')
                    elif a == 6:
                        as_of += all_td[a].text.replace('\n', '').replace(',', '')\
                            .replace(' (2022)', '').replace(' (2020)', '').replace('\u00a0', '')\
                            .replace('\u202f*', '')\
                            .replace(',', '').replace(' *', '').replace('[10] ', '').replace('[11] ', '')\
                            .replace('[12] ', '')\
                            .replace('[13] ', '').replace('[14] ', '').replace('[1]', '').replace(' est.', '')
                    elif a == 7:
                        average_electrical_power_per_capita_expressed_in_kwh_per_year += all_td[a].text\
                            .replace('\n', '').replace(',', '')\
                            .replace(' (2022)', '').replace(' (2020)', '').replace('\u00a0', '')\
                            .replace('\u202f*', '')\
                            .replace(',', '').replace(' *', '').replace('[10] ', '').replace('[11] ', '')\
                            .replace('[12] ', '')\
                            .replace('[13] ', '').replace('[14] ', '').replace('[1]', '')
                    elif a == 8:
                        average_electrical_power_per_capita_expressed_in_watts += all_td[a].text\
                            .replace('\n', '').replace(',', '')\
                            .replace(' (2022)', '').replace(' (2020)', '').replace('\u00a0', '')\
                            .replace('\u202f*', '')\
                            .replace(',', '').replace(' *', '').replace('[10] ', '').replace('[11] ', '')\
                            .replace('[12] ', '')\
                            .replace('[13] ', '').replace('[14] ', '').replace('[1]', '')

                element = {
                    'rank': rank,
                    'country_or_region': country_or_region,
                    'total_electricity_consumption_in_gwh_per_year': total_electricity_consumption_in_gwh_per_year,
                    'year_of_data': year_of_data,
                    'source': source,
                    'population': population,
                    'as_of': as_of,
                    'average_electrical_power_per_capita_expressed_in_kwh_per_year':
                        average_electrical_power_per_capita_expressed_in_kwh_per_year,
                    'average_electrical_power_per_capita_expressed_in_watts':
                        average_electrical_power_per_capita_expressed_in_watts
                }

                element_data_json = json.dumps(element)

                print(element_data_json + ',')

    # ok
    # https://en.wikipedia.org/wiki/List_of_countries_by_electricity_exports
    def test_extract_the_list_of_countries_by_electricity_exports(self):
        print("test_extract_the_list_of_countries_by_electricity_exports")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://en.wikipedia.org/wiki/List_of_countries_by_electricity_exports"

        rt = RequestsTor()

        html_with_tor = rt.get(url, headers=headers)

        soup = BeautifulSoup(html_with_tor.content, 'html.parser')

        if soup.find_all('tbody')[1].find('tr') is not None:
            all_tr = soup.find_all('tbody')[1].find_all('tr')

            for tr in all_tr:
                all_td = tr.find_all('td')

                rank = ''
                country_or_region = ''
                electricity_exports_in_gwh = ''
                date_of_information = ''

                for a in range(0, len(all_td)):
                    if a == 0:
                        rank += all_td[a].text.replace('\n', '').replace(',', '')\
                            .replace(' (2022)', '').replace(' (2020)', '').replace('\u00a0', '')\
                            .replace('\u202f*', '')\
                            .replace(',', '').replace(' *', '').replace('[10] ', '').replace('[11] ', '')\
                            .replace('[12] ', '')\
                            .replace('[13] ', '').replace('[14] ', '').replace('[1]', '').replace('\u2014', '')
                    elif a == 1:
                        country_or_region += all_td[a].text.replace('\n', '').replace(',', '')\
                            .replace(' (2022)', '').replace(' (2020)', '').replace('\u00a0', '')\
                            .replace('\u202f*', '')\
                            .replace(',', '').replace(' *', '').replace('[10] ', '').replace('[11] ', '')\
                            .replace('[12] ', '')\
                            .replace('[13] ', '').replace('[14] ', '').replace('[1]', '')
                    elif a == 2:
                        electricity_exports_in_gwh += all_td[a].text.replace('\n', '').replace(',', '')\
                            .replace(' (2022)', '').replace(' (2020)', '').replace('\u00a0', '')\
                            .replace('\u202f*', '')\
                            .replace(',', '').replace(' *', '').replace('[10] ', '').replace('[11] ', '')\
                            .replace('[12] ', '')\
                            .replace('[13] ', '').replace('[14] ', '').replace('[1]', '')
                    elif a == 3:
                        date_of_information += all_td[a].text.replace('\n', '').replace(',', '')\
                            .replace(' (2022)', '').replace(' (2020)', '').replace('\u00a0', '')\
                            .replace('\u202f*', '')\
                            .replace(',', '').replace(' *', '').replace('[10] ', '').replace('[11] ', '')\
                            .replace('[12] ', '')\
                            .replace('[13] ', '').replace('[14] ', '').replace('[1]', '').replace(' est.', '')

                element = {
                    'rank': rank,
                    'country_or_region': country_or_region,
                    'electricity_exports_in_gwh': electricity_exports_in_gwh,
                    'date_of_information': date_of_information,
                }

                element_data_json = json.dumps(element)

                print(element_data_json + ',')

    # ok
    # https://en.wikipedia.org/wiki/List_of_countries_by_electricity_imports
    def test_extract_the_list_of_countries_by_electricity_imports(self):
        print("test_extract_the_list_of_countries_by_electricity_imports")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://en.wikipedia.org/wiki/List_of_countries_by_electricity_imports"

        rt = RequestsTor()

        html_with_tor = rt.get(url, headers=headers)

        soup = BeautifulSoup(html_with_tor.content, 'html.parser')

        if soup.find_all('tbody')[0].find('tr') is not None:
            all_tr = soup.find_all('tbody')[0].find_all('tr')

            for tr in all_tr:
                all_td = tr.find_all('td')

                country_or_region = ''
                electricity_imports_in_gwh = ''
                date = ''

                for a in range(0, len(all_td)):
                    if a == 2:
                        country_or_region += all_td[a].text.replace('\n', '').replace(',', '')\
                            .replace(' (2022)', '').replace(' (2020)', '').replace('\u00a0', '')\
                            .replace('\u202f*', '')\
                            .replace(',', '').replace(' *', '').replace('[10] ', '').replace('[11] ', '')\
                            .replace('[12] ', '')\
                            .replace('[13] ', '').replace('[14] ', '').replace('[1]', '').replace('\u2014', '')
                    elif a == 3:
                        electricity_imports_in_gwh += all_td[a].text.replace('\n', '').replace(',', '')\
                            .replace(' (2022)', '').replace(' (2020)', '').replace('\u00a0', '')\
                            .replace('\u202f*', '')\
                            .replace(',', '').replace(' *', '').replace('[10] ', '').replace('[11] ', '')\
                            .replace('[12] ', '')\
                            .replace('[13] ', '').replace('[14] ', '').replace('[1]', '')
                    elif a == 4:
                        date += all_td[a].text.replace('\n', '').replace(',', '')\
                            .replace(' (2022)', '').replace(' (2020)', '').replace('\u00a0', '')\
                            .replace('\u202f*', '')\
                            .replace(',', '').replace(' *', '').replace('[10] ', '').replace('[11] ', '')\
                            .replace('[12] ', '')\
                            .replace('[13] ', '').replace('[14] ', '').replace('[1]', '').replace(' est.', '')

                element = {
                    'country_or_region': country_or_region,
                    'electricity_imports_in_gwh': electricity_imports_in_gwh,
                    'date': date,
                }

                element_data_json = json.dumps(element)

                print(element_data_json + ',')


class UnitTestsDataMiningWikipediaForChemistryWithDarkWeb(unittest.TestCase):
    # ok
    # https://en.wikipedia.org/wiki/Abundance_of_elements_in_Earth%27s_crust
    def test_extract_the_abundance_of_chemical_elements(self):
        print("test_extract_the_abundance_of_chemical_elements")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://en.wikipedia.org/wiki/Abundance_of_elements_in_Earth%27s_crust"

        i = 1

        rt = RequestsTor()

        html_with_tor = rt.get(url, headers=headers)

        time.sleep(3)

        soup = BeautifulSoup(html_with_tor.content, 'html.parser')

        if soup.find('tbody').find('tr') is not None:
            all_tr = soup.find('tbody').find_all('tr')

            for tr in all_tr:
                all_td = tr.find_all('td')

                atomic_number = ''
                name = ''
                symbol = ''
                darling = ''
                barbalace = ''
                webelements = ''
                israel_science_and_technology = ''
                crc = ''
                average_annual_production_by_extraction = ''

                for a in range(0, len(all_td)):
                    if a == 0:
                        atomic_number += all_td[a].text.replace('\n', '')
                    elif a == 1:
                        name += all_td[a].text.replace('\n', '')
                    elif a == 2:
                        symbol += all_td[a].text.replace('\n', '')
                    elif a == 3:
                        darling += all_td[a].text.replace('\n', '')
                    elif a == 4:
                        barbalace += all_td[a].text.replace('\n', '')
                    elif a == 5:
                        webelements += all_td[a].text.replace('\n', '')
                    elif a == 6:
                        israel_science_and_technology += all_td[a].text.replace('\n', '')
                    elif a == 7:
                        crc += all_td[a].text.replace('\n', '')
                    elif a == 8:
                        average_annual_production_by_extraction += all_td[a].text.replace('\n', '')

                element = {
                    'atomic_number': atomic_number,
                    'name': name,
                    'symbol': symbol
                }

                abundance_by_source = {
                    'darling': darling,
                    'barbalace': barbalace,
                    'webelements': webelements,
                    'israel_science_and_technology': israel_science_and_technology,
                    'crc': crc
                }

                element_data = {
                    'element': element,
                    'abundance_by_source': abundance_by_source,
                    'average_annual_production_by_extraction': average_annual_production_by_extraction
                }

                element_data_json = json.dumps(element_data)

                print(element_data_json + ',')

    # ok
    # https://en.wikipedia.org/wiki/List_of_chemical_elements
    def test_extract_the_list_of_chemical_elements(self):
        print("test_extract_the_list_of_chemical_elements")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://en.wikipedia.org/wiki/List_of_chemical_elements"

        i = 1

        rt = RequestsTor()

        html_with_tor = rt.get(url, headers=headers)

        time.sleep(3)

        soup = BeautifulSoup(html_with_tor.content, 'html.parser')

        if soup.find_all('tbody')[0].find('tr') is not None:
            all_tr = soup.find_all('tbody')[0].find_all('tr')

            for tr in all_tr:
                all_td = tr.find_all('td')

                atomic_number = ''
                symbol = ''
                name = ''
                origin_of_name = ''
                group = ''
                period = ''
                block = ''
                standard_atomic_weight_in_dalton = ''
                density_in_g_per_cubic_meter = ''
                melting_point_in_kelvin = ''
                boiling_point_in_kelvin = ''
                specific_heat_capacity_in_joule_per_kilogram_per_kelvin = ''
                electronegativity = ''
                abundance_in_earth_crust = ''
                origin = ''
                phase_at_room_temperature = ''

                for a in range(0, len(all_td)):
                    if a == 0:
                        atomic_number += all_td[a].text.replace('\n', '').replace('\u2013', '')\
                            .replace('\u00d7', '*').replace('\u2212', '^-')
                    elif a == 1:
                        symbol += all_td[a].text.replace('\n', '').replace('\u2013', '').replace('\u00d7', '*')\
                            .replace('\u2212', '^-')
                    elif a == 2:
                        name += all_td[a].text.replace('\n', '').replace('\u2013', '').replace('\u00d7', '*')\
                            .replace('\u2212', '^-')
                    elif a == 3:
                        origin_of_name += all_td[a].text.replace('\n', '').replace('\u2013', '')\
                            .replace('\u00d7', '*').replace('\u2212', '^-')
                    elif a == 4:
                        group += all_td[a].text.replace('\n', '').replace('\u2013', '').replace('\u00d7', '*')\
                            .replace('\u2212', '^-')
                    elif a == 5:
                        period += all_td[a].text.replace('\n', '').replace('\u2013', '').replace('\u00d7', '*')\
                            .replace('\u2212', '^-')
                    elif a == 6:
                        block += all_td[a].text.replace('\n', '').replace('\u2013', '').replace('\u00d7', '*')\
                            .replace('\u2212', '^-')
                    elif a == 7:
                        standard_atomic_weight_in_dalton += all_td[a].text.replace('\n', '').replace('\u2013', '')\
                            .replace('\u00d7', '*').replace('\u2212', '^-')
                    elif a == 8:
                        density_in_g_per_cubic_meter += all_td[a].text.replace('\n', '').replace('\u2013', '')\
                            .replace('\u00d7', '*').replace('\u2212', '^-')
                    elif a == 9:
                        melting_point_in_kelvin += all_td[a].text.replace('\n', '').replace('\u2013[k]', '')\
                            .replace('\u2013', '').replace('\u00d7', '*').replace('\u2212', '^-')
                    elif a == 10:
                        boiling_point_in_kelvin += all_td[a].text.replace('\n', '').replace('\u2013', '')\
                            .replace('\u00d7', '*').replace('\u2212', '^-')
                    elif a == 11:
                        specific_heat_capacity_in_joule_per_kilogram_per_kelvin += all_td[a].text.replace('\n', '')\
                            .replace('\u2013', '').replace('\u00d7', '*').replace('\u2212', '^-')
                    elif a == 12:
                        electronegativity += all_td[a].text.replace('\n', '').replace('\u2013', '')\
                            .replace('\u00d7', '*').replace('\u2212', '^-')
                    elif a == 13:
                        abundance_in_earth_crust += all_td[a].text.replace('\n', '').replace('\u2013', '')\
                            .replace('\u00d7', '*').replace('\u2212', '^-')
                    elif a == 14:
                        origin += all_td[a].text.replace('\n', '').replace('\u2013', '').replace('\u00d7', '*')\
                            .replace('\u2212', '^-')
                    elif a == 15:
                        phase_at_room_temperature += all_td[a].text.replace('\n', '').replace('\u2013', '')\
                            .replace('\u00d7', '*').replace('\u2212', '^-')

                element = {
                    'atomic_number': atomic_number,
                    'symbol': symbol,
                    'name': name
                }

                element_data = {
                    'element': element,
                    'origin_of_name': origin_of_name,
                    'group': group,
                    'period': period,
                    'block': block,
                    'standard_atomic_weight_in_dalton': standard_atomic_weight_in_dalton,
                    'density_in_g_per_cubic_meter': density_in_g_per_cubic_meter,
                    'melting_point_in_kelvin': melting_point_in_kelvin,
                    'boiling_point_in_kelvin': boiling_point_in_kelvin,
                    'specific_heat_capacity_in_joule_per_kilogram_per_kelvin': specific_heat_capacity_in_joule_per_kilogram_per_kelvin,
                    'electronegativity': electronegativity,
                    'abundance_in_earth_crust': abundance_in_earth_crust,
                    'origin': origin,
                    'phase_at_room_temperature': phase_at_room_temperature
                }

                element_data_json = json.dumps(element_data)

                print(element_data_json + ',')

    # ok
    # https://en.wikipedia.org/wiki/Roles_of_chemical_elements
    def test_extract_the_roles_of_chemical_elements(self):
        print("test_extract_the_roles_of_chemical_elements")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://en.wikipedia.org/wiki/Roles_of_chemical_elements"

        i = 1

        rt = RequestsTor()

        html_with_tor = rt.get(url, headers=headers)

        time.sleep(3)

        soup = BeautifulSoup(html_with_tor.content, 'html.parser')

        if soup.find_all('tbody')[0].find('tr') is not None:
            all_tr = soup.find_all('tbody')[0].find_all('tr')

            for tr in all_tr:
                all_td = tr.find_all('td')

                atomic_number = ''
                symbol = ''
                name = ''
                period = ''
                group = ''
                roles_in_nature_in_non_living_and_living = ''
                roles_in_technology_in_old_and_new = ''

                for a in range(0, len(all_td)):
                    if a == 0:
                        atomic_number += all_td[a].text.replace('\n', '').replace('\u2013', '')\
                            .replace('\u00d7', '*').replace('\u2212', '^-').replace('\u00a0', '')
                    elif a == 1:
                        symbol += all_td[a].text.replace('\n', '').replace('\u2013', '').replace('\u00d7', '*')\
                            .replace('\u2212', '^-').replace('\u00a0', '')
                    elif a == 2:
                        name += all_td[a].text.replace('\n', '').replace('\u2013', '').replace('\u00d7', '*')\
                            .replace('\u2212', '^-').replace('\u00a0', '')
                    elif a == 3:
                        period += all_td[a].text.replace('\n', '').replace('\u2013', '')\
                            .replace('\u00d7', '*').replace('\u2212', '^-').replace('\u00a0', '')
                    elif a == 4:
                        group += all_td[a].text.replace('\n', '').replace('\u2013', '').replace('\u00d7', '*')\
                            .replace('\u2212', '^-').replace('\u00a0', '')
                    elif a == 5:
                        roles_in_nature_in_non_living_and_living += all_td[a].text.replace('\n', '')\
                            .replace('\u2013', '').replace('\u00d7', '*')\
                            .replace('\u2212', '^-').replace('\u00a0', '')
                    elif a == 6:
                        roles_in_technology_in_old_and_new += all_td[a].text.replace('\n', '')\
                            .replace('\u2013', '').replace('\u00d7', '*')\
                            .replace('\u2212', '^-').replace('\u00a0', '')

                element_data = {
                    'atomic_number': atomic_number,
                    'symbol': symbol,
                    'name': name,
                    'period': period,
                    'group': group,
                    'roles_in_nature_in_non_living_and_living': roles_in_nature_in_non_living_and_living,
                    'roles_in_technology_in_old_and_new': roles_in_technology_in_old_and_new
                }

                element_data_json = json.dumps(element_data)

                print(element_data_json + ',')


if __name__ == '__main__':
    unittest.main()
