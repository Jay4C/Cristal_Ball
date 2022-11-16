import subprocess
import unittest
import time
import warnings
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import requests
from bs4 import BeautifulSoup


class UnitTestsWebAutomationAdecco(unittest.TestCase):
    # ok
    def test_kill_some_processes(self):
        print("test_kill_some_processes")

        subprocess.call("taskkill /F /IM geckodriver.exe")
        subprocess.call("taskkill /F /IM firefox.exe")

    # ok
    def test_se_connecter(self):
        print("test_se_connecter")

        time.sleep(5)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(5)

        # with Firefox
        browser = webdriver.Firefox(executable_path='..\\geckodriver.exe')

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get('https://espace-personnel.adecco.fr/Pages/login.aspx')

        time.sleep(15)

        strictement_necessaires_button = browser.find_element_by_xpath(
            "/html/body/div[3]/div[3]/div/div/div[2]/div/div/button[1]"
        )
        strictement_necessaires_button.click()

        time.sleep(10)

        se_connecter_button = browser.find_element_by_xpath(
            "/html/body/form/div[4]/div/div[2]/div[1]/table/tbody/tr[2]/td/table/tbody/"
            "tr/td/div/div/div/div[2]/div[1]/center/a"
        )
        se_connecter_button.click()

        time.sleep(10)

        email_input = browser.find_element_by_xpath(
            '/html/body/div/div/div/form/div[1]/div[1]/input'
        )
        email_input.clear()
        email_input.send_keys("..@gmail.com")

        time.sleep(10)

        password_input = browser.find_element_by_xpath(
            '/html/body/div/div/div/form/div[1]/div[2]/input'
        )
        password_input.clear()
        password_input.send_keys("")

        time.sleep(10)

        se_connecter_button = browser.find_element_by_xpath(
            '/html/body/div/div/div/div[2]/button'
        )
        se_connecter_button.click()

        time.sleep(10)

    # ok
    def test_send_my_cv_for_one_ad_without_headless(self):
        print("test_send_my_cv_for_one_ad_without_headless")

        url_ad = ''
        print("url_ad : " + url_ad)

        time.sleep(5)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(5)

        # with Firefox
        browser = webdriver.Firefox(executable_path='..\\geckodriver.exe')

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get(url_ad)
        print('browser.get(url_ad)')

        time.sleep(15)

        strictement_necessaires_button = browser.find_element_by_xpath(
            '//*[@id="onetrust-reject-all-handler"]'
        )
        strictement_necessaires_button.click()
        print("strictement_necessaires_button.click()")

        time.sleep(10)

        postuler_button = browser.find_element_by_xpath(
            '//*[@id="hypApplyJob"]'
        )
        postuler_button.click()
        print("postuler_button.click()")

        time.sleep(10)

        # get the window handle after a new window has opened
        window_after_1 = browser.window_handles[1]

        # switch on to new child window
        browser.switch_to.window(window_after_1)

        time.sleep(10)

        window_after_title = browser.title
        print(window_after_title)

        # refresh page
        browser.refresh()

        time.sleep(10)

        # Printing the URL
        get_url = browser.current_url
        print(get_url)

        se_connecter_et_postuler_button = browser.find_element_by_xpath(
            '//*[@id="LogButton"]'
        )
        se_connecter_et_postuler_button.click()
        print("se_connecter_et_postuler_button.click()")

        time.sleep(10)

        email_input = browser.find_element_by_xpath(
            '//*[@id="loginPage:j_id9:login-email"]'
        )
        email_input.clear()
        email_input.send_keys("..@gmail.com")
        print("email_input.send_keys()")

        time.sleep(10)

        password_input = browser.find_element_by_xpath(
            '//*[@id="loginPage:j_id9:password"]'
        )
        password_input.clear()
        password_input.send_keys("")
        print("password_input.send_keys()")

        time.sleep(10)

        se_connecter_button = browser.find_element_by_xpath(
            '//*[@id="loginButton"]'
        )
        se_connecter_button.click()
        print("se_connecter_button.click()")

        time.sleep(10)

        candidature_envoyee_text = browser.find_element_by_xpath(
            '/html/body/form/div[4]/div/div[1]/div/table/tbody/tr[2]/td/table/tbody/tr/td/div/div/div/div/a'
        ).text
        print(candidature_envoyee_text)

        time.sleep(10)

        profile_button = browser.find_element_by_xpath(
            '/html/body/form/div[4]/div/div[1]/div/table/tbody/tr[2]/td/table/tbody/tr/td/div/div/div/div/a'
        )
        profile_button.click()
        print("profile_button.click()")

        time.sleep(10)

        # switch on to new child window
        window_after_2 = browser.window_handles[2]
        browser.switch_to.window(window_after_2)

        time.sleep(10)

        window_after_2_title = browser.title
        print("window_after_2_title : " + window_after_2_title)

        # refresh page
        browser.refresh()

        time.sleep(10)

        # Printing the URL
        get_url = browser.current_url
        print("get_url window_after_2 : " + get_url)

        se_deconnecter_button = browser.find_element_by_xpath(
            '//*[@id="logoutLink"]'
        )
        se_deconnecter_button.click()
        print("se_deconnecter_button.click()")

        time.sleep(10)

        deconnecte_text = browser.find_element_by_xpath(
            '/html/body/form/div[4]/div/div/table/tbody/tr[1]/td/table/tbody/tr/td/div/div/div[1]/div/div[1]/center/h1'
        ).text
        print("deconnecte_text : " + deconnecte_text)

        time.sleep(10)

        # All windows related to driver instance will quit
        browser.quit()
        print("browser.quit()")

    # ok
    def test_send_my_cv_for_one_ad_with_headless(self):
        print("test_send_my_cv_for_one_ad_with_headless")

        url_ad = ''
        print("url_ad : " + url_ad)

        time.sleep(5)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(5)

        # with Firefox
        options = Options()
        options.headless = True
        browser = webdriver.Firefox(executable_path='..\\geckodriver.exe', options=options)

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get(url_ad)
        print('browser.get(url_ad)')

        time.sleep(15)

        strictement_necessaires_button = browser.find_element_by_xpath(
            '//*[@id="onetrust-reject-all-handler"]'
        )
        strictement_necessaires_button.click()
        print("strictement_necessaires_button.click()")

        time.sleep(10)

        postuler_button = browser.find_element_by_xpath(
            '//*[@id="hypApplyJob"]'
        )
        postuler_button.click()
        print("postuler_button.click()")

        time.sleep(10)

        # get the window handle after a new window has opened
        window_after_1 = browser.window_handles[1]

        # switch on to new child window
        browser.switch_to.window(window_after_1)

        time.sleep(10)

        window_after_title = browser.title
        print(window_after_title)

        # refresh page
        browser.refresh()

        time.sleep(10)

        # Printing the URL
        get_url = browser.current_url
        print(get_url)

        se_connecter_et_postuler_button = browser.find_element_by_xpath(
            '//*[@id="LogButton"]'
        )
        se_connecter_et_postuler_button.click()
        print("se_connecter_et_postuler_button.click()")

        time.sleep(10)

        email_input = browser.find_element_by_xpath(
            '//*[@id="loginPage:j_id9:login-email"]'
        )
        email_input.clear()
        email_input.send_keys("..@gmail.com")
        print("email_input.send_keys()")

        time.sleep(10)

        password_input = browser.find_element_by_xpath(
            '//*[@id="loginPage:j_id9:password"]'
        )
        password_input.clear()
        password_input.send_keys("")
        print("password_input.send_keys()")

        time.sleep(10)

        se_connecter_button = browser.find_element_by_xpath(
            '//*[@id="loginButton"]'
        )
        se_connecter_button.click()
        print("se_connecter_button.click()")

        time.sleep(10)

        candidature_envoyee_text = browser.find_element_by_xpath(
            '/html/body/form/div[4]/div/div[1]/div/table/tbody/tr[2]/td/table/tbody/tr/td/div/div/div/div/a'
        ).text
        print(candidature_envoyee_text)

        time.sleep(10)

        profile_button = browser.find_element_by_xpath(
            '/html/body/form/div[4]/div/div[1]/div/table/tbody/tr[2]/td/table/tbody/tr/td/div/div/div/div/a'
        )
        profile_button.click()
        print("profile_button.click()")

        time.sleep(10)

        # switch on to new child window
        window_after_2 = browser.window_handles[2]
        browser.switch_to.window(window_after_2)

        time.sleep(10)

        window_after_2_title = browser.title
        print("window_after_2_title : " + window_after_2_title)

        # refresh page
        browser.refresh()

        time.sleep(10)

        # Printing the URL
        get_url = browser.current_url
        print("get_url window_after_2 : " + get_url)

        se_deconnecter_button = browser.find_element_by_xpath(
            '//*[@id="logoutLink"]'
        )
        se_deconnecter_button.click()
        print("se_deconnecter_button.click()")

        time.sleep(10)

        deconnecte_text = browser.find_element_by_xpath(
            '/html/body/form/div[4]/div/div/table/tbody/tr[1]/td/table/tbody/tr/td/div/div/div[1]/div/div[1]/center/h1'
        ).text
        print("deconnecte_text : " + deconnecte_text)

        time.sleep(10)

        # All windows related to driver instance will quit
        browser.quit()
        print("browser.quit()")

    # ok
    def test_send_my_cv_for_several_ads_with_headless(self):
        print("test_send_my_cv_for_several_ads_with_headless")

        urls_ad = [
        ]

        for url_ad in urls_ad:
            print("url_ad : " + url_ad)

            time.sleep(5)

            warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

            time.sleep(5)

            # with Firefox
            options = Options()
            options.headless = True
            browser = webdriver.Firefox(executable_path='..\\geckodriver.exe', options=options)

            time.sleep(5)

            # maximize window
            browser.maximize_window()

            time.sleep(5)

            try:
                # open
                browser.get(url_ad)
                print('browser.get(url_ad)')

                time.sleep(15)

                strictement_necessaires_button = browser.find_element_by_xpath(
                    '//*[@id="onetrust-reject-all-handler"]'
                )
                strictement_necessaires_button.click()
                print("strictement_necessaires_button.click()")

                time.sleep(10)

                postuler_button = browser.find_element_by_xpath(
                    '//*[@id="hypApplyJob"]'
                )
                postuler_button.click()
                print("postuler_button.click()")

                time.sleep(10)

                # get the window handle after a new window has opened
                window_after_1 = browser.window_handles[1]

                # switch on to new child window
                browser.switch_to.window(window_after_1)

                time.sleep(10)

                window_after_title = browser.title
                print(window_after_title)

                # refresh page
                browser.refresh()

                time.sleep(10)

                # Printing the URL
                get_url = browser.current_url
                print(get_url)

                se_connecter_et_postuler_button = browser.find_element_by_xpath(
                    '//*[@id="LogButton"]'
                )
                se_connecter_et_postuler_button.click()
                print("se_connecter_et_postuler_button.click()")

                time.sleep(10)

                email_input = browser.find_element_by_xpath(
                    '//*[@id="loginPage:j_id9:login-email"]'
                )
                email_input.clear()
                email_input.send_keys("..@gmail.com")
                print("email_input.send_keys()")

                time.sleep(10)

                password_input = browser.find_element_by_xpath(
                    '//*[@id="loginPage:j_id9:password"]'
                )
                password_input.clear()
                password_input.send_keys("")
                print("password_input.send_keys()")

                time.sleep(10)

                se_connecter_button = browser.find_element_by_xpath(
                    '//*[@id="loginButton"]'
                )
                se_connecter_button.click()
                print("se_connecter_button.click()")

                time.sleep(10)

                candidature_envoyee_text = browser.find_element_by_xpath(
                    '/html/body/form/div[4]/div/div[1]/div/table/tbody/tr[2]/td/table/tbody/tr/td/div/div/div/div/a'
                ).text
                print(candidature_envoyee_text)

                time.sleep(10)

                profile_button = browser.find_element_by_xpath(
                    '/html/body/form/div[4]/div/div[1]/div/table/tbody/tr[2]/td/table/tbody/tr/td/div/div/div/div/a'
                )
                profile_button.click()
                print("profile_button.click()")

                time.sleep(10)

                # switch on to new child window
                window_after_2 = browser.window_handles[2]
                browser.switch_to.window(window_after_2)

                time.sleep(10)

                window_after_2_title = browser.title
                print("window_after_2_title : " + window_after_2_title)

                # refresh page
                browser.refresh()

                time.sleep(10)

                # Printing the URL
                get_url = browser.current_url
                print("get_url window_after_2 : " + get_url)

                se_deconnecter_button = browser.find_element_by_xpath(
                    '//*[@id="logoutLink"]'
                )
                se_deconnecter_button.click()
                print("se_deconnecter_button.click()")

                time.sleep(10)

                deconnecte_text = browser.find_element_by_xpath(
                    '/html/body/form/div[4]/div/div/table/tbody/tr[1]/td/table/tbody/tr/td/div/div/div[1]'
                    '/div/div[1]/center/h1'
                ).text
                print("deconnecte_text : " + deconnecte_text)

                time.sleep(10)

                # All windows related to driver instance will quit
                browser.quit()
                print("browser.quit()")
            except Exception as e:
                print('error : ' + str(e))

                # All windows related to driver instance will quit
                browser.quit()
                print("browser.quit()")

    # ok
    def test_send_my_cv_for_several_ads_with_headless_with_web_scraping(self):
        print("test_send_my_cv_for_several_ads_with_headless_with_web_scraping")

        i = 1

        # 6155
        for i1 in range(2, 3):
            url_result_page = "https://www.adecco.fr/resultats-offres-emploi?pageNum=" + str(i1)

            print("url_result_page : " + url_result_page)

            # Request the content of a page from the url
            html = requests.get(url_result_page)

            time.sleep(5)

            # Parse the content of html_doc
            soup = BeautifulSoup(html.content, 'html.parser')

            if soup.find("a", {'data-bind': "init,attr: { 'href': NavigationUrl }, click: $root.viewJobDetails.bind('    '.trimEnd())"}) is not None:
                urls_ad = soup.find_all("a", {'data-bind': "init,attr: { 'href': NavigationUrl }, click: $root.viewJobDetails.bind('    '.trimEnd())"})

                for url_ad in urls_ad:
                    print("url_ad : " + url_ad.get('href'))

                    time.sleep(5)

                    warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

                    time.sleep(5)

                    # with Firefox
                    options = Options()
                    options.headless = True
                    browser = webdriver.Firefox(executable_path='..\\geckodriver.exe', options=options)

                    time.sleep(5)

                    # maximize window
                    browser.maximize_window()

                    time.sleep(5)

                    try:
                        # open
                        browser.get(url_ad.get('href'))
                        print('browser.get(url_ad.get("href"))')

                        time.sleep(15)

                        strictement_necessaires_button = browser.find_element_by_xpath(
                            '//*[@id="onetrust-reject-all-handler"]'
                        )
                        strictement_necessaires_button.click()
                        print("strictement_necessaires_button.click()")

                        time.sleep(10)

                        postuler_button = browser.find_element_by_xpath(
                            '//*[@id="hypApplyJob"]'
                        )
                        postuler_button.click()
                        print("postuler_button.click()")

                        time.sleep(5)

                        # get the window handle after a new window has opened
                        window_after_1 = browser.window_handles[1]

                        # switch on to new child window
                        browser.switch_to.window(window_after_1)

                        time.sleep(5)

                        window_after_title = browser.title
                        print(window_after_title)

                        # refresh page
                        browser.refresh()

                        time.sleep(5)

                        # Printing the URL
                        get_url = browser.current_url
                        print(get_url)

                        se_connecter_et_postuler_button = browser.find_element_by_xpath(
                            '//*[@id="LogButton"]'
                        )
                        se_connecter_et_postuler_button.click()
                        print("se_connecter_et_postuler_button.click()")

                        time.sleep(10)

                        email_input = browser.find_element_by_xpath(
                            '//*[@id="loginPage:j_id9:login-email"]'
                        )
                        email_input.clear()
                        email_input.send_keys("..@gmail.com")
                        print("email_input.send_keys()")

                        time.sleep(5)

                        password_input = browser.find_element_by_xpath(
                            '//*[@id="loginPage:j_id9:password"]'
                        )
                        password_input.clear()
                        password_input.send_keys("")
                        print("password_input.send_keys()")

                        time.sleep(5)

                        se_connecter_button = browser.find_element_by_xpath(
                            '//*[@id="loginButton"]'
                        )
                        se_connecter_button.click()
                        print("se_connecter_button.click()")

                        time.sleep(10)

                        candidature_envoyee_text = browser.find_element_by_xpath(
                            '/html/body/form/div[4]/div/div[1]/div/table/tbody/tr[2]/td/table/tbody/tr/td/div/div/div/div/a'
                        ).text
                        print(candidature_envoyee_text)

                        time.sleep(5)

                        profile_button = browser.find_element_by_xpath(
                            '/html/body/form/div[4]/div/div[1]/div/table/tbody/tr[2]/td/table/tbody/tr/td/div/div/div/div/a'
                        )
                        profile_button.click()
                        print("profile_button.click()")

                        time.sleep(10)

                        # switch on to new child window
                        window_after_2 = browser.window_handles[2]
                        browser.switch_to.window(window_after_2)

                        time.sleep(5)

                        window_after_2_title = browser.title
                        print("window_after_2_title : " + window_after_2_title)

                        # refresh page
                        browser.refresh()

                        time.sleep(5)

                        # Printing the URL
                        get_url = browser.current_url
                        print("get_url window_after_2 : " + get_url)

                        se_deconnecter_button = browser.find_element_by_xpath(
                            '//*[@id="logoutLink"]'
                        )
                        se_deconnecter_button.click()
                        print("se_deconnecter_button.click()")

                        time.sleep(10)

                        deconnecte_text = browser.find_element_by_xpath(
                            '/html/body/form/div[4]/div/div/table/tbody/tr[1]/td/table/tbody/tr/td/div/div/div[1]'
                            '/div/div[1]/center/h1'
                        ).text
                        print("deconnecte_text : " + deconnecte_text)

                        time.sleep(5)

                        # All windows related to driver instance will quit
                        browser.quit()
                        print("browser.quit()")
                    except Exception as e:
                        print('error : ' + str(e))

                        # All windows related to driver instance will quit
                        browser.quit()
                        print("browser.quit()")

                    i += 1
            else:
                print("no offres")

    # ok
    def test_send_my_cv_for_several_ads_with_headless_with_web_scraping_for_ile_de_france(self):
        print("test_send_my_cv_for_several_ads_with_headless_with_web_scraping_for_ile_de_france")

        i = 1

        urls_departements = [
            # Paris (75)
            {
                'url_department': 'https://www.adecco.fr/resultats-offres-emploi/d-paris?pageNum=',
                'debut': 1,
                'fin': 81
            },
            # Seine-et-Marne (77)
            {
                'url_department': 'https://www.adecco.fr/resultats-offres-emploi/d-seine-et-marne?pageNum=',
                'debut': 1,
                'fin': 59
            },
            # yvelines (78)
            {
                'url_department': "https://www.adecco.fr/resultats-offres-emploi/d-yvelines?pageNum=",
                'debut': 1,
                'fin': 60
            },
            # Essonne (91)
            {
                'url_department': 'https://www.adecco.fr/resultats-offres-emploi/d-essonne?pageNum=',
                'debut': 1,
                'fin': 64
            },
            # Hauts-de-Seine (92)
            {
                'url_department': 'https://www.adecco.fr/resultats-offres-emploi/d-hauts-de-seine?pageNum=',
                'debut': 1,
                'fin': 81
            },
            # Seine-Saint-Denis (93)
            {
                'url_department': 'https://www.adecco.fr/resultats-offres-emploi/d-seine-saint-denis?pageNum=',
                'debut': 1,
                'fin': 40
            },
            # Val-de-Marne (94)
            {
                'url_department': 'https://www.adecco.fr/resultats-offres-emploi/d-val-de-marne?pageNum=',
                'debut': 1,
                'fin': 54
            },
            # val-d'oise (95)
            {
                'url_department': "https://www.adecco.fr/resultats-offres-emploi/d-val-d'oise?pageNum=",
                'debut': 1,
                'fin': 38
            }
        ]

        for url_departement in urls_departements:
            for i1 in range(url_departement.get('debut'), url_departement.get('fin') + 1):
                url_result_page = url_departement.get('url_department') + str(i1)

                print("url_result_page : " + url_result_page)

                # Request the content of a page from the url
                html = requests.get(url_result_page)

                time.sleep(5)

                # Parse the content of html_doc
                soup = BeautifulSoup(html.content, 'html.parser')

                if soup.find("a", {'data-bind': "init,attr: { 'href': NavigationUrl }, click: $root.viewJobDetails.bind('    '.trimEnd())"}) is not None:
                    urls_ad = soup.find_all("a", {'data-bind': "init,attr: { 'href': NavigationUrl }, click: $root.viewJobDetails.bind('    '.trimEnd())"})

                    for url_ad in urls_ad:
                        print("url_ad : " + url_ad.get('href'))

                        time.sleep(5)

                        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

                        time.sleep(5)

                        # with Firefox
                        options = Options()
                        options.headless = True
                        browser = webdriver.Firefox(executable_path='..\\geckodriver.exe', options=options)

                        time.sleep(5)

                        # maximize window
                        browser.maximize_window()

                        time.sleep(5)

                        try:
                            # open
                            browser.get(url_ad.get('href'))
                            print('browser.get(url_ad.get("href"))')

                            time.sleep(15)

                            strictement_necessaires_button = browser.find_element_by_xpath(
                                '//*[@id="onetrust-reject-all-handler"]'
                            )
                            strictement_necessaires_button.click()
                            print("strictement_necessaires_button.click()")

                            time.sleep(10)

                            postuler_button = browser.find_element_by_xpath(
                                '//*[@id="hypApplyJob"]'
                            )
                            postuler_button.click()
                            print("postuler_button.click()")

                            time.sleep(5)

                            # get the window handle after a new window has opened
                            window_after_1 = browser.window_handles[1]

                            # switch on to new child window
                            browser.switch_to.window(window_after_1)

                            time.sleep(5)

                            window_after_title = browser.title
                            print(window_after_title)

                            # refresh page
                            browser.refresh()

                            time.sleep(5)

                            # Printing the URL
                            get_url = browser.current_url
                            print(get_url)

                            se_connecter_et_postuler_button = browser.find_element_by_xpath(
                                '//*[@id="LogButton"]'
                            )
                            se_connecter_et_postuler_button.click()
                            print("se_connecter_et_postuler_button.click()")

                            time.sleep(10)

                            email_input = browser.find_element_by_xpath(
                                '//*[@id="loginPage:j_id9:login-email"]'
                            )
                            email_input.clear()
                            email_input.send_keys("..@gmail.com")
                            print("email_input.send_keys()")

                            time.sleep(5)

                            password_input = browser.find_element_by_xpath(
                                '//*[@id="loginPage:j_id9:password"]'
                            )
                            password_input.clear()
                            password_input.send_keys("")
                            print("password_input.send_keys()")

                            time.sleep(5)

                            se_connecter_button = browser.find_element_by_xpath(
                                '//*[@id="loginButton"]'
                            )
                            se_connecter_button.click()
                            print("se_connecter_button.click()")

                            time.sleep(20)

                            candidature_envoyee_text = browser.find_element_by_xpath(
                                '/html/body/form/div[4]/div/div[1]/div/table/tbody/tr[2]/td/table/tbody/tr/td/div/div/div/div/a'
                            ).text
                            print(candidature_envoyee_text)

                            time.sleep(5)

                            profile_button = browser.find_element_by_xpath(
                                '/html/body/form/div[4]/div/div[1]/div/table/tbody/tr[2]/td/table/tbody/tr/td/div/div/div/div/a'
                            )
                            profile_button.click()
                            print("profile_button.click()")

                            time.sleep(10)

                            # switch on to new child window
                            window_after_2 = browser.window_handles[2]
                            browser.switch_to.window(window_after_2)

                            time.sleep(5)

                            window_after_2_title = browser.title
                            print("window_after_2_title : " + window_after_2_title)

                            # refresh page
                            browser.refresh()

                            time.sleep(5)

                            # Printing the URL
                            get_url = browser.current_url
                            print("get_url window_after_2 : " + get_url)

                            se_deconnecter_button = browser.find_element_by_xpath(
                                '//*[@id="logoutLink"]'
                            )
                            se_deconnecter_button.click()
                            print("se_deconnecter_button.click()")

                            time.sleep(10)

                            deconnecte_text = browser.find_element_by_xpath(
                                '/html/body/form/div[4]/div/div/table/tbody/tr[1]/td/table/tbody/tr/td/div/div/div[1]'
                                '/div/div[1]/center/h1'
                            ).text
                            print("deconnecte_text : " + deconnecte_text)

                            time.sleep(5)

                            # All windows related to driver instance will quit
                            browser.quit()
                            print("browser.quit()")
                        except Exception as e:
                            print('error : ' + str(e))

                            # All windows related to driver instance will quit
                            browser.quit()
                            print("browser.quit()")

                        i += 1
                else:
                    print("no offres")


if __name__ == '__main__':
    unittest.main()
