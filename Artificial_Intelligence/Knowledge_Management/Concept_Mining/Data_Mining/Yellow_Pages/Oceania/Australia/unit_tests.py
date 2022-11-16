import time
from bs4 import BeautifulSoup
import requests
import pymysql.cursors
import unittest


class UnitTestsDataMinerYellowPagesAustralia(unittest.TestCase):
    def test_extract_one_email_from_one_result(self):
        print("test_extract_one_email_from_one_result")

        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
            }

            url = "https://www.yellowpages.com.au/nsw/new-lambton/blackbutt-inn-13758594-listing.html?referredBy=www.yellowpages.com.au&context=businessTypeSearch"

            time.sleep(2)

            # Request the content of a page from the url
            html = requests.get(url, headers=headers)

            # Parse the content of html_doc
            soup = BeautifulSoup(html.content, 'html.parser')

            try:
                if soup.find("a", {"class": "contact contact-main contact-url"}) is not None:
                    email = "'info@" + soup \
                        .find("a", {"class": "contact contact-main contact-url"}) \
                        .get("href") \
                        .replace("www.", "") \
                        .replace("http://", "") \
                        .replace("https://", "") \
                        .split('/')[0] \
                        .replace('/', '') + "',"

                    print("email : " + email)
                else:
                    print("no email business")
            except Exception as e:
                print("error no a class contact contact-main contact-url : " + str(e))
        except Exception as e:
            print("error 1 : " + str(e))

    def test_extract_emails_from_all_page_of_results_for_one_activity_and_one_capital(self):
        print('test_extract_emails_from_all_page_of_results_for_one_activity_and_one_capital')

    def test_extract_emails_from_all_page_of_results_for_all_activities_and_capitals(self):
        print('test_extract_emails_from_all_page_of_results_for_all_activities_and_capitals')


if __name__ == '__main__':
    unittest.main()
