from bs4 import BeautifulSoup
import requests
import time
import unittest


class UnitTestsDataMinerYellowPagesGrece(unittest.TestCase):
    def test_extract_email_from_one_result(self):
        print("test_extract_email_from_one_result")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://www.xo.gr/profile/profile-911644527/en/"

        time.sleep(3)

        # Request the content of a page from the url
        html = requests.get(url, headers=headers)

        print(html.content)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.content, 'html.parser')

        try:
            if soup.select_one("#profileWebSite") is not None:
                email = "info@" + soup \
                    .select_one("#profileWebSite") \
                    .get("href") \
                    .replace("www.", "") \
                    .replace("http://", "") \
                    .replace("https://", "") \
                    .split("/")[0]

                print("email : " + email)

            else:
                print('no email business')
        except Exception as e:
            print("error select a id profileWebSite : " + str(e))

    def test_extract_each_email_from_all_pages_of_results_for_one_activity_and_one_capital(self):
        print("test_extract_each_email_from_all_pages_of_results_for_one_activity_and_one_capital")

    def test_extract_each_email_from_all_pages_of_results_for_all_activities_and_all_capitals(self):
        print("test_extract_each_email_from_all_pages_of_results_for_all_activities_and_all_capitals")


if __name__ == '__main__':
    unittest.main()
