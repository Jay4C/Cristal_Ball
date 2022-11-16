import unittest
import time
import warnings
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


class UnitTestsDataMiningApecWithRPA(unittest.TestCase):
    # ok
    def test_extract_all_links_for_one_page_with_rpa_with_headless(self):
        print("test_extract_all_links_for_one_page_with_rpa_with_headless")

        url = "https://www.apec.fr/candidat/recherche-emploi.html/emploi?motsCles=%C3%A9nergie&page=0&lieux=711"

        warnings.filterwarnings(
            action="ignore",
            message="unclosed",
            category=ResourceWarning
        )

        # with Firefox
        options = Options()
        options.headless = True
        browser = webdriver.Firefox(
            executable_path='..\\geckodriver.exe',
            options=options
        )

        time.sleep(10)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get(url)
        print('browser.get(url)')

        time.sleep(20)

        refuser_tous_les_cookies_button = browser.find_element_by_id(
            "onetrust-reject-all-handler"
        )
        refuser_tous_les_cookies_button.click()
        print("refuser_tous_les_cookies_button.click()")

        time.sleep(7)

        conatiner_result = browser.find_element_by_class_name(
            "container-result"
        )

        all_div = conatiner_result.find_elements_by_tag_name('div')

        i = 0

        for div in all_div:
            try:
                if str(div.find_element_by_tag_name("a").get_attribute("href")) != 'None':
                    print("link " + str(i) + " : " + str(div.find_element_by_tag_name("a").get_attribute("href")))

                    i += 1
            except Exception as e:
                print("error link : " + str(e))

        time.sleep(5)

        browser.quit()

    # ok
    def test_extract_all_links_for_all_page_with_rpa_with_headless(self):
        print("test_extract_all_links_for_all_page_with_rpa_with_headless")

        for n in range(0, 238):
            url = "https://www.apec.fr/candidat/recherche-emploi.html/emploi?motsCles=%C3%A9nergie&page=" \
                  + str(n) \
                  + "&lieux=711"

            print('url_page : ' + str(url))

            warnings.filterwarnings(
                action="ignore",
                message="unclosed",
                category=ResourceWarning
            )

            # with Firefox
            options = Options()
            options.headless = True
            browser = webdriver.Firefox(
                executable_path='..\\geckodriver.exe',
                options=options
            )

            time.sleep(10)

            # maximize window
            browser.maximize_window()

            time.sleep(5)

            # open
            browser.get(url)
            print('browser.get(url)')

            time.sleep(15)

            refuser_tous_les_cookies_button = browser.find_element_by_id(
                "onetrust-reject-all-handler"
            )
            refuser_tous_les_cookies_button.click()
            print("refuser_tous_les_cookies_button.click()")

            time.sleep(7)

            conatiner_result = browser.find_element_by_class_name(
                "container-result"
            )

            all_div = conatiner_result.find_elements_by_tag_name('div')

            i = 0

            for div in all_div:
                try:
                    if str(div.find_element_by_tag_name("a").get_attribute("href")) != 'None':
                        print("link " + str(i) + " : " + str(div.find_element_by_tag_name("a").get_attribute("href")))

                        i += 1
                except Exception as e:
                    print("error link : " + str(e))

            time.sleep(5)

            browser.quit()


if __name__ == '__main__':
    unittest.main()
