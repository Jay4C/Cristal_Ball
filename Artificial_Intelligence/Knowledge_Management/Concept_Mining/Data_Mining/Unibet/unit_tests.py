import unittest
import time
from bs4 import BeautifulSoup
from requests_tor import RequestsTor
import warnings
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


# unibet race url
global_url = "https://www.unibet.fr/turf/race/16-12-2021-R1-C7-deauville-prix-du-val-dorne.html"


class UnitTestsDataMiningUnibetDarkWeb(unittest.TestCase):
    def test_extract_the_prix_of_one_course(self):
        print("test_extract_the_prix_of_one_course")

        url = 'https://www.unibet.fr/turf/race/09-07-2021-R5-C10-saint-cloud-prix-de-chateau-thierry.html'

        headers = {
            'authority': 'www.unibet.fr',
            'method': 'GET',
            'path': url.replace("https://www.unibet.fr", ""),
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'fr,fr-FR;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'cache-control': 'max-age=0',
            'cookie': 'cookie-notification=true; sps-v3-cookie=4D14BCC4DA85C844FE3E262EAE547549.S.04',
            'dnt': '1',
            'sec-ch-ua': '" Not;A Brand";v="99", "Microsoft Edge";v="91", "Chromium";v="91"',
            'sec-ch-ua-mobile': '?0',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.64'
        }

        rt = RequestsTor()

        html_with_tor = rt.get(url, headers=headers)

        print(html_with_tor.content)

        soup = BeautifulSoup(html_with_tor.content, 'html.parser')

        if soup.find("span", {"class": "name"}) is not None:
            print("Prix : " + soup.find("span", {"class": "name"}).text)
        else:
            print("no prix")


class UnitTestsDataMiningUnibetRPAWebV1(unittest.TestCase):
    # ok
    def test_extract_the_prize_of_one_course_with_rpa_web(self):
        print("test_extract_the_prize_of_one_course_with_rpa_web")

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        url = global_url

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

        prize = str(browser.find_element_by_xpath("//span[@class='name']").text)
        print("prize : " + prize)

    # ok
    def test_extract_the_date_of_one_course_with_rpa_web(self):
        print("test_extract_the_date_of_one_course_with_rpa_web")

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        url = global_url

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

        date = str(browser.find_element_by_xpath("//span[@class='rank']").text)
        print("date : " + date)

    # ok
    def test_extract_the_pronostic_of_one_course_with_rpa_web(self):
        print("test_extract_the_pronostic_of_one_course_with_rpa_web")

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        url = global_url

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

        pronostic = str(browser.find_element_by_xpath("//span[@class='race-pronostic-inner']").text)
        print("pronostic : " + pronostic)

    # ok
    def test_extract_the_analyse_of_one_course_with_rpa_web(self):
        print("test_extract_the_pronostic_of_one_course_with_rpa_web")

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        url = global_url

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

        notre_prono_button = browser.find_element_by_xpath(
            "//a[@class='race-button btn-moreprono']"
        )
        notre_prono_button.click()

        time.sleep(5)

        notre_analyse = str(browser.find_element_by_xpath("//div[@class='pronostic']").text)
        print("notre_analyse : " + notre_analyse)

        time.sleep(5)

        notre_preferes = str(browser.find_element_by_xpath("//div[@class='favorites']").text)
        print("notre_preferes : " + notre_preferes)

        time.sleep(5)

        modal_close_button = browser.find_element_by_xpath(
            "//i[@class='fa fa-times ui-fa-close']"
        )
        modal_close_button.click()

        time.sleep(5)

        browser.close()

        time.sleep(5)

    # ok
    def test_extract_the_details_of_the_land_of_one_course_with_rpa_web(self):
        print("test_extract_the_details_of_the_land_of_one_course_with_rpa_web")

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        url = global_url

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

        details_of_the_land = str(browser.find_element_by_xpath("//p[@class='race-meta ui-mainview-block']").text)
        print("details_of_the_land : " + details_of_the_land)

        time.sleep(5)

    # ok
    def test_extract_the_type_of_the_course_of_one_course_with_rpa_web(self):
        print("test_extract_the_type_of_the_course_of_one_course_with_rpa_web")

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        url = global_url

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

        type_of_the_course = str(
            browser.find_element_by_xpath("//p[@class='race-meta ui-mainview-block']").text.lower().split(" - ")[0]
        )
        print("type_of_the_course : " + type_of_the_course)

        time.sleep(5)

    # ok
    def test_extract_the_amount_of_the_prize_of_one_course_with_rpa_web(self):
        print("test_extract_the_amount_of_the_prize_of_one_course_with_rpa_web")

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        url = global_url

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

        amount_of_the_prize = str(
            browser.find_element_by_xpath("//p[@class='race-meta ui-mainview-block']").text.lower().split(" - ")[1]
        )
        print("amount_of_the_prize : " + amount_of_the_prize)

        time.sleep(5)

    # ok
    def test_extract_the_distance_of_the_course_of_one_course_with_rpa_web(self):
        print("test_extract_the_distance_of_the_course_of_one_course_with_rpa_web")

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        url = global_url

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

        distance_of_the_course = str(
            browser.find_element_by_xpath("//p[@class='race-meta ui-mainview-block']").text.lower().split(" - ")[2].replace('m', '')
        )
        print("distance_of_the_course : " + distance_of_the_course)

        time.sleep(5)

    # ok
    def test_extract_the_number_of_racers_of_one_course_with_rpa_web(self):
        print("test_extract_the_number_of_racers_of_one_course_with_rpa_web")

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        url = global_url

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

        number_of_racers = str(
            browser.find_element_by_xpath("//p[@class='race-meta ui-mainview-block']").text.lower().split(" - ")[3]
                .replace(' partants', '')
        )
        print("number_of_racers : " + number_of_racers)

        time.sleep(5)

    # ok
    def test_extract_the_first_runner_of_one_course_with_rpa_web(self):
        print("test_extract_the_first_runner_of_one_course_with_rpa_web")

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        url = global_url

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

        if browser.find_element_by_xpath("//li[@class='runner-item runner']") is not None:
            first_runner = str(
                browser.find_elements_by_xpath("//li[@class='runner-item runner']")[0].text
            )
            print("first_runner : " + first_runner)
        else:
            print('')

        time.sleep(5)

    # ok
    def test_extract_the_cotes_direct_of_all_runners_of_one_course_with_rpa_web(self):
        print("test_extract_the_cotes_direct_of_all_runners_of_one_course_with_rpa_web")

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        url = global_url

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

        number_of_racers = int(
            browser.find_element_by_xpath("//p[@class='race-meta ui-mainview-block']").text.lower().split(" - ")[3].replace(' partants', '')
        )

        for i in range(1, number_of_racers + 1):
            num_pmu = browser.find_element_by_xpath(
                "/html/body/div/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]/div/div[3]/"
                "ul[2]/li/div/div[2]/ul/li[" + str(i + 1) + "]/div/div[1]/span"
            ).text

            cote_direct = browser.find_element_by_xpath(
                "/html/body/div/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]/div/div[3]"
                "/ul[2]/li/div/div[2]/ul/li[" + str(i + 1) + "]/div"
            ).find_element_by_class_name("price-live").text

            print("num_pmu : " + str(num_pmu) + " , cote_direct : " + str(cote_direct))

        time.sleep(5)

    # ok
    def test_extract_the_cotes_matin_of_all_runners_of_one_course_with_rpa_web(self):
        print("test_extract_the_cotes_matin_of_all_runners_of_one_course_with_rpa_web")

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        url = global_url

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

        number_of_racers = int(
            browser.find_element_by_xpath("//p[@class='race-meta ui-mainview-block']").text.lower().split(" - ")[3].replace(' partants', '')
        )

        runners = {}

        for i in range(1, number_of_racers + 1):
            num_pmu = browser.find_element_by_xpath(
                "/html/body/div/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]/div/div[3]/"
                "ul[2]/li/div/div[2]/ul/li[" + str(i + 1) + "]/div/div[1]/span"
            ).text

            cote_matin = browser.find_element_by_xpath(
                "/html/body/div[1]/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]/div/div[3]"
                "/ul[2]/li/div/div[2]/ul/li[" + str(i + 1) + "]/div"
            ).find_element_by_class_name("price-morning").text

            print("num_pmu : " + str(num_pmu) + " , cote_direct : " + str(cote_matin))

            if cote_matin != "NP":
                runners[num_pmu] = float(cote_matin)
            else:
                runners[num_pmu] = 200

        time.sleep(5)

        browser.close()

    # ok
    def test_extract_the_musique_of_all_runners_of_one_course_with_rpa_web(self):
        print("test_extract_the_musique_of_all_runners_of_one_course_with_rpa_web")

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        url = global_url

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

        number_of_racers = int(
            browser.find_element_by_xpath(
                "//p[@class='race-meta ui-mainview-block']"
            ).text.lower().split(" - ")[3].replace(' partants', '')
        )

        for i in range(1, number_of_racers + 1):
            num_pmu = browser.find_element_by_xpath(
                "/html/body/div/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]/div/div[3]/"
                "ul[2]/li/div/div[2]/ul/li[" + str(i + 1) + "]/div/div[1]/span"
            ).text

            musique = browser.find_element_by_xpath(
                "/html/body/div[1]/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]/div/div[3]"
                "/ul[2]/li/div/div[2]/ul/li[" + str(i + 1) + "]/div"
            ).find_element_by_class_name("musique").text

            print("num_pmu : " + str(num_pmu) + " , musique : " + str(musique))

        time.sleep(5)

    #
    def test_extract_the_poids_of_all_runners_of_one_course_with_rpa_web(self):
        print("test_extract_the_poids_of_all_runners_of_one_course_with_rpa_web")

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        url = global_url

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

        response_unibet = browser

        number_of_racers = int(
            response_unibet.find_element_by_xpath(
                "//p[@class='race-meta ui-mainview-block']"
            ).text.lower().split(" - ")[3].replace(' partants', '')
        )

        for i in range(1, number_of_racers + 1):
            num_pmu = response_unibet.find_element_by_xpath(
                "/html/body/div/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]/div/div[3]/"
                "ul[2]/li/div/div[2]/ul/li[" + str(i + 1) + "]/div/div[1]/span"
            ).text

            try:
                poids = response_unibet.find_element_by_xpath(
                    "/html/body/div[1]/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]/div/div[3]"
                    "/ul[2]/li/div/div[2]/ul/li[" + str(i + 1) + "]/div"
                ).find_element_by_class_name("weight").text.lower().replace(' ', '').replace('kg', '')

                print("num_pmu : " + str(num_pmu) + " , poids : " + str(poids))
            except Exception as e:
                print('error poids : ' + str(e))

        time.sleep(5)


class UnitTestsDataMiningUnibetRPAWebV2(unittest.TestCase):
    # ok
    def test_extract_all_courses_for_one_day_with_rpa_web(self):
        print("test_extract_all_courses_for_one_day_with_rpa_web")

        url = "https://www.unibet.fr/turf"

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
        print('browser.get(url)')

        time.sleep(20)

        all_courses = browser.find_elements_by_class_name(
            "race-link"
        )

        for course in all_courses:
            print("'" + str(course.get_attribute('href')) + "',")

        browser.quit()


if __name__ == '__main__':
    unittest.main()
