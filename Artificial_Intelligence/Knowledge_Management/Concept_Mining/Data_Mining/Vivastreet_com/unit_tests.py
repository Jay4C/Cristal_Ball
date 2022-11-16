import unittest
import time
from bs4 import BeautifulSoup
import requests
import string


class UnitTestsVivastreet(unittest.TestCase):
    def test_extract_one_phone_number_from_vivastreet(self):
        url = 'https://www.vivastreet.com/annonces-service/paris-1er-ardt-75001/gardien-d-immeuble/47795152'

        # Request the content of a page from the url
        html = requests.get(url)

        time.sleep(3)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.content, 'html.parser')

        if soup.find("div", {"class", "vs-phone-button kiwii-font-weight-bold kiwii-position-relative"}) is None:
            print("sorry there is no phone number")

        else:
            phone_number = soup.find("div", {"class", "vs-phone-button kiwii-font-weight-bold kiwii-position-relative"}) \
                .find("span", {"class", "phone_link"}).get("data-phone-number")

            print("phone number : " + phone_number)

    def test_extract_all_phone_number_from_one_list_from_vivastreet(self):
        url = 'https://search.vivastreet.com/annonces/fr/t+1539?lb=new&search=1&start_field=1&select-this=00&searchGeoId=2&offer_type=offer&end_field='

        # Request the content of a page from the url
        html = requests.get(url)

        time.sleep(3)

        # Parse the content of html
        soup = BeautifulSoup(html.content, 'html.parser')

        if soup.find("ul", {"class", "list"}) is None:
            print("the list is empty")

        else:
            li_all = soup.find("ul", {"class", "list"}).find_all("li")

            for li in li_all:
                try:
                    url = li.find("div", {"class", "clad"}).find("a", {"class", "clad__wrapper"}).get("href")

                    # Request the content of a page from the url
                    phone_number_html = requests.get(url)

                    time.sleep(3)

                    # Parse the content of phone_number_html
                    phone_number_soup = BeautifulSoup(phone_number_html.content, 'html.parser')

                    if phone_number_soup.find("div",
                                              {"class",
                                               "vs-phone-button kiwii-font-weight-bold kiwii-position-relative"}) is None:
                        print("sorry there is no phone number")

                    else:
                        phone_number = phone_number_soup.find("div", {"class",
                                                                      "vs-phone-button kiwii-font-weight-bold kiwii-position-relative"}) \
                            .find("span", {"class", "phone_link"}).get("data-phone-number")

                        print("phone number : " + phone_number)

                except:
                    print("no phone number")

    def test_extract_all_phone_number_from_some_list_from_vivastreet(self):
        url_de_depart = 'https://www.vivastreet.com/annonces/ile-de-france/t+2'

        html_url_de_depart = requests.get(url_de_depart)

        # Parse the content of phone_number_html
        html_url_de_depart_soup = BeautifulSoup(html_url_de_depart.content, 'html.parser')

        if html_url_de_depart_soup.find('div', {'class': 'results-summary'}) is None:
            print('no counter')

        else:
            nombre_annonces = html_url_de_depart_soup.find('div', {'class': 'results-summary'}).text \
                .replace('annonces', '') \
                .replace('<h1>', '') \
                .replace('</h1>', '') \
                .replace('Annonces', '') \
                .replace(',', '') \
                .replace(' ', '') \
                .replace('\n', '') \
                .lower()

            for letter in string.ascii_lowercase:
                nombre_annonces = nombre_annonces.replace(letter, '')

            nombre_pages = int(round(int(nombre_annonces) / 25))

            for i in range(2, nombre_pages):

                url = url_de_depart[:-1] + str(i)

                print(url)

                phone_numbers = []

                # Request the content of a page from the url
                html = requests.get(url)

                time.sleep(3)

                # Parse the content of html
                soup = BeautifulSoup(html.content, 'html.parser')

                if soup.find("ul", {"class", "list"}) is None:
                    print("the list is empty")

                else:
                    li_all = soup.find("ul", {"class", "list"}).find_all("li")

                    for li in li_all:
                        try:
                            url = li.find("div", {"class", "clad"}).find("a", {"class", "clad__wrapper"}).get("href")

                            # Request the content of a page from the url
                            phone_number_html = requests.get(url)

                            time.sleep(3)

                            # Parse the content of phone_number_html
                            phone_number_soup = BeautifulSoup(phone_number_html.content, 'html.parser')

                            if phone_number_soup.find("div",
                                                      {"class",
                                                       "vs-phone-button kiwii-font-weight-bold kiwii-position-relative"}) is None:
                                print("sorry there is no phone number")

                            else:
                                phone_number = phone_number_soup.find("div", {"class",
                                                                              "vs-phone-button kiwii-font-weight-bold kiwii-position-relative"}) \
                                    .find("span", {"class", "phone_link"}).get("data-phone-number")

                                if phone_number in phone_numbers:
                                    print("phone number : " + phone_number + " already exists")

                                else:
                                    if phone_number[:2] == "06" or phone_number[:2] == "07":
                                        phone_numbers.append(phone_number)
                                        print("phone number : " + phone_number)

                        except:
                            print("no phone number")


if __name__ == '__main__':
    unittest.main()
