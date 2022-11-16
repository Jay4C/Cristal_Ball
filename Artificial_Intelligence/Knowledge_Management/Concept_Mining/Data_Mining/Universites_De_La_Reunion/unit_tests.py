import unittest
import requests
from bs4 import BeautifulSoup
import codecs

class UnitTestsUniversitesDeLaReunion(unittest.TestCase):
    def test_extract_emails_from_one_phone_book(self):
        try:
            url_phone_book = "https://annuaire.univ-reunion.fr/?structure=917"

            # Request the content of a page from the url
            html = requests.get(url_phone_book)

            # Parse the content of html
            soup = BeautifulSoup(html.content, 'html.parser')

            emails = []

            try:
                if soup.find("table", {"class": "results"}) is not None:
                    try:
                        if soup.find("table", {"class": "results"}).find("tr") is not None:
                            all_tr = soup.find("table", {"class": "results"}).find_all("tr")
                            for tr in all_tr:
                                try:
                                    if tr.find('td') is not None:
                                        td_email = tr.find_all('td')[1].text \
                                            .replace('document.write(rot13ToMail("', '') \
                                            .replace('"));', '')

                                        if td_email != "Information manquante":
                                            emails.append(codecs.encode(td_email, 'rot_13'))
                                    else:
                                        print("no tag td")
                                except Exception as e:
                                    print('exception tag td : ' + str(e))
                        else:
                            print("no tag tr")
                    except Exception as e:
                        print('exception tag tr : ' + str(e))
                else:
                    print("no tag table")

                for email in emails:
                    print(email)
            except Exception as e:
                print("Exception table tag : " + str(e))
        except Exception as e:
            print("url_phone_book : " + str(e))

    def test_extract_emails_from_phone_books(self):
        phone_books = [
            "https://annuaire.univ-reunion.fr/?structure=917",
            "https://annuaire.univ-reunion.fr/?structure=905ES",
            "https://annuaire.univ-reunion.fr/?structure=EBOI"
        ]

        emails = []

        for phone_book in phone_books:
            try:
                url_phone_book = phone_book

                # Request the content of a page from the url
                html = requests.get(url_phone_book)

                # Parse the content of html
                soup = BeautifulSoup(html.content, 'html.parser')

                try:
                    if soup.find("table", {"class": "results"}) is not None:
                        try:
                            if soup.find("table", {"class": "results"}).find("tr") is not None:
                                all_tr = soup.find("table", {"class": "results"}).find_all("tr")
                                for tr in all_tr:
                                    try:
                                        if tr.find('td') is not None:
                                            td_email = tr.find_all('td')[1].text \
                                                .replace('document.write(rot13ToMail("', '') \
                                                .replace('"));', '') \
                                                .lower()

                                            if td_email != "information manquante":
                                                emails.append(codecs.encode(td_email, 'rot_13'))
                                        else:
                                            print("no tag td")
                                    except Exception as e:
                                        print('exception tag td : ' + str(e))
                            else:
                                print("no tag tr")
                        except Exception as e:
                            print('exception tag tr : ' + str(e))
                    else:
                        print("no tag table")
                except Exception as e:
                    print("Exception table tag : " + str(e))
            except Exception as e:
                print("url_phone_book : " + str(e))

        for email in emails:
            print(email)


if __name__ == '__main__':
    unittest.main()
