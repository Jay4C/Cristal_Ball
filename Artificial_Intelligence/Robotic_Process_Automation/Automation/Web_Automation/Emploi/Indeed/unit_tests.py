import subprocess
import unittest
import time
import warnings
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

api_key = ""


class UnitTestsWebAutomationIndeedWithoutHeadless(unittest.TestCase):
    # ok
    def test_open_one_page(self):
        print('test_open_one_page')

        url = "https://fr.indeed.com/rc/clk?jk=6355d95c160c2e37&fccid=ae4250aadf58a666&vjs=3"

        time.sleep(5)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(5)

        # with Firefox
        browser = webdriver.Firefox(
            executable_path='..\\..\\geckodriver.exe'
        )

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get(url)
        print("page opened")

        time.sleep(15)

        """
        # click on the "Paramètres des cookies" button
        parametres_cookies_button = browser.find_element_by_xpath(
            "/html/body/div[5]/div[3]/div[1]/div/div[2]/div/button[1]"
        )
        parametres_cookies_button.click()

        time.sleep(10)

        # click on the "confirmer" button
        confirmer_button = browser.find_element_by_xpath(
            "/html/body/div[5]/div[2]/div/section/div[5]/button"
        )
        confirmer_button.click()

        time.sleep(10)
        """

    #
    def test_se_connecter(self):
        print('test_se_connecter')

        email = ".@outlook.fr"

        password = ""

        time.sleep(5)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(5)

        # with Firefox
        browser = webdriver.Firefox(executable_path='..\\..\\geckodriver.exe')

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get('https://secure.indeed.com/account/login?hl=fr_FR&co=FR&continue=https%3A%2F%2Ffr.indeed.com%2F&tmpl=desktop&service=my&from=gnav-util-homepage&jsContinue=https%3A%2F%2Ffr.indeed.com%2F&empContinue=https%3A%2F%2Faccount.indeed.com%2Fmyaccess')
        print("page opened")

        time.sleep(15)

        # click on the "Tout refuser" button
        tout_refuser_button = browser.find_element_by_xpath(
            '/html/body/div[2]/div[3]/div/div[1]/div/div[2]/div/button[2]'
        )
        tout_refuser_button.click()
        print("tout_refuser_button.click()")

        time.sleep(10)

        # Insert the email
        email_input = browser.find_element_by_xpath(
            '/html/body/div[1]/div[2]/main/div/div/div[2]/section/form/div[1]/span/input'
        )
        email_input.clear()
        email_input.send_keys(email)
        print("email_input.send_keys(email)")

        time.sleep(5)

        # click on the "Continer" button
        continuer_button = browser.find_element_by_xpath(
            '/html/body/div[1]/div[2]/main/div/div/div[2]/section/form/button'
        )
        continuer_button.click()
        print("continuer_button.click()")

        time.sleep(10)

        # Insert the password
        password_input = browser.find_element_by_xpath(
            '/html/body/div[1]/div[2]/main/div/div/div[2]/section/form/div[1]/span/input'
        )
        password_input.clear()
        password_input.send_keys(password)
        print("password_input.send_keys(password)")

        time.sleep(5)

        # click on the "Connexion" button
        connexion_button = browser.find_element_by_xpath(
            '/html/body/div[1]/div[2]/main/div/div/div[2]/section/form/button'
        )
        connexion_button.click()
        print("connexion_button.click()")

        time.sleep(10)

    # ok mais il faut modifier l'adresse ip
    def test_send_cv_for_one_ad_for_indeed_energie(self):
        print('test_send_cv_for_one_ad_for_indeed')

        url_ad = 'https://fr.indeed.com/voir-emploi?jk=b61b9d028cf994d4&from=serp&vjs=3'

        time.sleep(5)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(5)

        # with Firefox
        browser = webdriver.Firefox(executable_path='..\\geckodriver.exe')

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        try:
            # open
            browser.get(url_ad)
            print("page opened")

            time.sleep(15)

            continuer_pour_postuler_text = ""

            try:
                continuer_pour_postuler_text += browser.find_element_by_xpath(
                    '//*[@id="viewJobButtonLinkContainer"]'
                ).text
                print('continuer_pour_postuler_text : ' + str(continuer_pour_postuler_text))
            except Exception as e:
                print("error continuer_pour_postuler_text : " + str(e))
                continuer_pour_postuler_text = ""

            if continuer_pour_postuler_text == "Continuer pour postuler":
                # click on the "postuler" button
                postuler_button = browser.find_element_by_xpath(
                    '//*[@id="viewJobButtonLinkContainer"]'
                )
                postuler_button.click()
                print("postuler_button.click()")

                time.sleep(10)

                # get the window handle after a new window has opened
                window_1 = browser.window_handles[1]

                # switch on to new child window
                browser.switch_to.window(window_1)

                time.sleep(5)

                # click on the "Connexion" button
                connexion_button = browser.find_element_by_xpath(
                    '/html/body/div/div/div[2]/div[1]/a'
                )
                connexion_button.click()
                print("connexion_button.click()")

                time.sleep(10)

                # click on the "Paramètres des cookies" button
                autoriser_cookies_button = browser.find_element_by_xpath(
                    '//*[@id="onetrust-accept-btn-handler"]'
                )
                autoriser_cookies_button.click()
                print("autoriser_cookies_button.click()")

                time.sleep(5)

                # Insert the email
                email_input = browser.find_element_by_xpath(
                    '//*[@id="ifl-InputFormField-3"]'
                )
                email_input.clear()
                email_input.send_keys("jason.aloyau@outlook.fr")
                print("email_input.send_keys()")

                time.sleep(5)

                # click on the "Continuer" button
                continuer_button = browser.find_element_by_xpath(
                    '/html/body/div[1]/div[2]/main/div/div/div/section/form/button'
                )
                continuer_button.click()
                print("continuer_button.click()")

                time.sleep(10)

                # Insert the password
                password_input = browser.find_element_by_xpath(
                    '/html/body/div[1]/div[2]/main/div/div/div/section/form/div[1]/span/input'
                )
                password_input.clear()
                password_input.send_keys("0TRlyt8BlRgWLQ9A3VXn")
                print("password_input.send_keys()")

                time.sleep(5)

                # Click on the 'Connexion' button
                connexion_button = browser.find_element_by_xpath(
                    '/html/body/div[1]/div[2]/main/div/div/div/section/form/button'
                )
                connexion_button.click()
                print("connexion_button.click()")

                time.sleep(10)

                operation_reussie_text = browser.find_element_by_xpath(
                    "/html/body/div/div/h1"
                ).text
                print('operation_reussie_text : ' + str(operation_reussie_text))

                time.sleep(5)

                browser.quit()
            else:
                browser.quit()
        except Exception as e:
            print("error test_send_cv_for_one_ad_for_indeed : " + str(e))

            time.sleep(5)

            browser.quit()

            time.sleep(5)

            try:
                print("test_reboot")

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
                browser.get('http://www.tplinkmodem.net')
                print("browser.get('http://www.tplinkmodem.net')")

                time.sleep(15)

                password_input = browser.find_element_by_xpath(
                    "/html/body/div[3]/div[2]/div[2]/div[1]/div[2]/div[2]/div/div/div[1]/input[1]"
                )
                password_input.clear()
                password_input.send_keys("3tr8TxwAGkisligWI3gN8UuUnKMV2E")
                print("password_input.send_keys()")

                time.sleep(10)

                log_in_button = browser.find_element_by_xpath(
                    "/html/body/div[3]/div[2]/div[2]/div[1]/div[2]/div[3]/div/button"
                )
                log_in_button.click()
                print("log_in_button.click()")

                time.sleep(20)

                reboot_button = browser.find_element_by_xpath(
                    '//*[@id="topReboot"]'
                )
                reboot_button.click()
                print("reboot_button.click()")

                time.sleep(5)

                yes_button = browser.find_element_by_xpath(
                    '/html/body/div[7]/div/div[4]/div/div[2]/div/div[2]/button'
                )
                yes_button.click()
                print("yes_button.click()")

                time.sleep(120)

                browser.quit()
                print("browser.quit()")
            except Exception as e:
                print("error test_reboot : " + str(e))

    # ok mais il faut modifier l'adresse ip
    def test_send_cv_for_all_ad_for_indeed_energie(self):
        print('test_send_cv_for_all_ad_for_indeed_energie')

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        for i in range(0, 70):
            start = str(10*i)

            url_results = "https://fr.indeed.com/jobs?q=%C3%A9nergie&l=%C3%8Ele-de-France&start=" + start

            print("url_results : " + str(url_results))

            time.sleep(10)

            html = requests.get(url_results, headers=headers)

            soup = BeautifulSoup(html.content, 'html.parser')

            if soup.find("a", {"class": "tapItem"}) is not None:
                all_a = soup.find_all("a", {"class": "tapItem"})

                for a in all_a:
                    link = "https://fr.indeed.com" + a.get('href')

                    print("link of the ad : " + link)

                    time.sleep(5)

                    warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

                    time.sleep(5)

                    # with Firefox
                    browser = webdriver.Firefox(executable_path='..\\geckodriver.exe')

                    time.sleep(5)

                    # maximize window
                    browser.maximize_window()

                    time.sleep(5)

                    try:
                        # open
                        browser.get(link)
                        print("page opened")

                        time.sleep(15)

                        continuer_pour_postuler_text = ""

                        try:
                            continuer_pour_postuler_text += browser.find_element_by_xpath(
                                '//*[@id="viewJobButtonLinkContainer"]'
                            ).text
                            print('continuer_pour_postuler_text : ' + str(continuer_pour_postuler_text))
                        except Exception as e:
                            print("error continuer_pour_postuler_text : " + str(e))
                            continuer_pour_postuler_text = ""

                        if continuer_pour_postuler_text == "Continuer pour postuler":
                            # click on the "postuler" button
                            postuler_button = browser.find_element_by_xpath(
                                '//*[@id="viewJobButtonLinkContainer"]'
                            )
                            postuler_button.click()
                            print("postuler_button.click()")

                            time.sleep(10)

                            # get the window handle after a new window has opened
                            window_1 = browser.window_handles[1]

                            # switch on to new child window
                            browser.switch_to.window(window_1)

                            time.sleep(5)

                            # click on the "Connexion" button
                            connexion_button = browser.find_element_by_xpath(
                                '/html/body/div/div/div[2]/div[1]/a'
                            )
                            connexion_button.click()
                            print("connexion_button.click()")

                            time.sleep(10)

                            # click on the "Paramètres des cookies" button
                            autoriser_cookies_button = browser.find_element_by_xpath(
                                '//*[@id="onetrust-accept-btn-handler"]'
                            )
                            autoriser_cookies_button.click()
                            print("autoriser_cookies_button.click()")

                            time.sleep(5)

                            # Insert the email
                            email_input = browser.find_element_by_xpath(
                                '//*[@id="ifl-InputFormField-3"]'
                            )
                            email_input.clear()
                            email_input.send_keys("jason.aloyau@outlook.fr")
                            print("email_input.send_keys()")

                            time.sleep(5)

                            # click on the "Continuer" button
                            continuer_button = browser.find_element_by_xpath(
                                '/html/body/div[1]/div[2]/main/div/div/div/section/form/button'
                            )
                            continuer_button.click()
                            print("continuer_button.click()")

                            time.sleep(10)

                            # Insert the password
                            password_input = browser.find_element_by_xpath(
                                '/html/body/div[1]/div[2]/main/div/div/div/section/form/div[1]/span/input'
                            )
                            password_input.clear()
                            password_input.send_keys("0TRlyt8BlRgWLQ9A3VXn")
                            print("password_input.send_keys()")

                            time.sleep(5)

                            # Click on the 'Connexion' button
                            connexion_button = browser.find_element_by_xpath(
                                '/html/body/div[1]/div[2]/main/div/div/div/section/form/button'
                            )
                            connexion_button.click()
                            print("connexion_button.click()")

                            time.sleep(10)

                            operation_reussie_text = browser.find_element_by_xpath(
                                "/html/body/div/div/h1"
                            ).text
                            print('operation_reussie_text : ' + str(operation_reussie_text))

                            time.sleep(5)

                            browser.quit()
                        else:
                            browser.quit()
                    except Exception as e:
                        print("error test_send_cv_for_one_ad_for_indeed : " + str(e))

                        time.sleep(5)

                        browser.quit()

                        time.sleep(5)

                        try:
                            print("test_reboot")

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
                            browser.get('http://www.tplinkmodem.net')
                            print("browser.get('http://www.tplinkmodem.net')")

                            time.sleep(15)

                            password_input = browser.find_element_by_xpath(
                                "/html/body/div[3]/div[2]/div[2]/div[1]/div[2]/div[2]/div/div/div[1]/input[1]"
                            )
                            password_input.clear()
                            password_input.send_keys("")
                            print("password_input.send_keys()")

                            time.sleep(10)

                            log_in_button = browser.find_element_by_xpath(
                                "/html/body/div[3]/div[2]/div[2]/div[1]/div[2]/div[3]/div/button"
                            )
                            log_in_button.click()
                            print("log_in_button.click()")

                            time.sleep(20)

                            reboot_button = browser.find_element_by_xpath(
                                '//*[@id="topReboot"]'
                            )
                            reboot_button.click()
                            print("reboot_button.click()")

                            time.sleep(5)

                            yes_button = browser.find_element_by_xpath(
                                '/html/body/div[7]/div/div[4]/div/div[2]/div/div[2]/button'
                            )
                            yes_button.click()
                            print("yes_button.click()")

                            time.sleep(120)

                            browser.quit()
                            print("browser.quit()")
                        except Exception as e:
                            print("error test_reboot : " + str(e))
            else:
                print("no ads")


class UnitTestsWebAutomationIndeedWithHeadless(unittest.TestCase):
    # ok
    def test_kill_some_processes(self):
        print("test_kill_some_processes")

        subprocess.call("taskkill /F /IM geckodriver.exe")
        subprocess.call("taskkill /F /IM firefox.exe")

    #
    def test_send_cv_for_all_ad_for_indeed_with_headless(self):
        print('test_send_cv_for_all_ad_for_indeed_with_headless')

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/51.0.2704.103'
        }

        for i in range(2, 70):
            start = str(10*i)

            url_results = "https://fr.indeed.com/jobs?q=python&l=%C3%8Ele-de-France&jt=permanent&start=" + start

            print("url_results : " + str(url_results))

            time.sleep(10)

            html = requests.get(url_results, headers=headers)

            soup = BeautifulSoup(html.content, 'html.parser')

            if soup.find("a", {"class": "tapItem"}) is not None:
                all_a = soup.find_all("a", {"class": "tapItem"})

                for a in all_a:
                    link = "https://fr.indeed.com" + a.get('href')

                    print("link of the ad : " + link)

                    time.sleep(5)

                    warnings.filterwarnings(
                        action="ignore",
                        message="unclosed",
                        category=ResourceWarning
                    )

                    time.sleep(5)

                    # with Firefox
                    # options = Options()
                    # options.headless = True
                    # options=options
                    browser = webdriver.Firefox(
                        executable_path='..\\geckodriver.exe'
                    )

                    time.sleep(5)

                    # maximize window
                    browser.maximize_window()

                    time.sleep(5)

                    try:
                        # open
                        browser.get(link)
                        print("page opened")

                        time.sleep(15)

                        continuer_pour_postuler_text = ""

                        try:
                            continuer_pour_postuler_text += browser.find_element_by_xpath(
                                '//*[@id="viewJobButtonLinkContainer"]'
                            ).text
                            print('continuer_pour_postuler_text : ' + str(continuer_pour_postuler_text))
                        except Exception as e:
                            print("error continuer_pour_postuler_text : " + str(e))
                            continuer_pour_postuler_text = ""

                        if continuer_pour_postuler_text == "Continuer pour postuler":
                            # click on the "postuler" button
                            postuler_button = browser.find_element_by_xpath(
                                '//*[@id="viewJobButtonLinkContainer"]'
                            )
                            postuler_button.click()
                            print("postuler_button.click()")

                            time.sleep(10)

                            # get the window handle after a new window has opened
                            window_1 = browser.window_handles[1]

                            # switch on to new child window
                            browser.switch_to.window(window_1)

                            time.sleep(5)

                            # click on the "Connexion" button
                            connexion_button = browser.find_element_by_xpath(
                                '/html/body/div/div/div[2]/div[1]/a'
                            )
                            connexion_button.click()
                            print("connexion_button.click()")

                            time.sleep(10)

                            # click on the "Paramètres des cookies" button
                            autoriser_cookies_button = browser.find_element_by_xpath(
                                '//*[@id="onetrust-accept-btn-handler"]'
                            )
                            autoriser_cookies_button.click()
                            print("autoriser_cookies_button.click()")

                            time.sleep(5)

                            # Insert the email
                            email_input = browser.find_element_by_xpath(
                                '//*[@id="ifl-InputFormField-3"]'
                            )
                            email_input.clear()
                            email_input.send_keys("jason.aloyau@outlook.fr")
                            print("email_input.send_keys()")

                            time.sleep(5)

                            # click on the "Continuer" button
                            continuer_button = browser.find_element_by_xpath(
                                '/html/body/div[1]/div[2]/main/div/div/div/section/form/button'
                            )
                            continuer_button.click()
                            print("continuer_button.click()")

                            time.sleep(10)

                            try:
                                presence_h_captcha = browser.find_element_by_name(
                                    "h-captcha-response"
                                )
                                print("presence_h_captcha : " + str(presence_h_captcha))

                                time.sleep(5)

                                # extract data_site_key
                                data_site_key = browser.find_element_by_class_name(
                                    "pass-Captcha"
                                ).find_element_by_tag_name(
                                    "iframe"
                                ).get_attribute(
                                    "src"
                                ).replace(
                                    "&theme=light", ""
                                ).split("sitekey=")[1]
                                print("data_site_key : " + str(data_site_key))

                                # request http://2captcha.com/in.php
                                url_2captcha_in = "http://2captcha.com/in.php?key=" + str(api_key) \
                                               + "&method=hcaptcha" \
                                               + "&sitekey=" + str(data_site_key) \
                                               + "&pageurl=" + str(browser.current_url) \
                                               + "&json=1"

                                response_2captcha_in = requests.request("GET", url_2captcha_in)

                                id_captcha_in = response_2captcha_in.json()["request"]

                                print('id_captcha_in : ' + str(id_captcha_in))

                                time.sleep(25)

                                # request http://2captcha.com/res.php
                                url_2captcha_res = "http://2captcha.com/res.php?key=" + str(api_key) \
                                                   + "&action=get" \
                                                   + "&id=" + str(id_captcha_in)

                                response_2captcha_res = requests.request("GET", url_2captcha_res)

                                print('id_captcha_res : ' + str(response_2captcha_res))

                                # deleting display:none parameter
                                element = browser.find_element_by_name('h-captcha-response')
                                browser.execute_script("arguments[0].setAttribute('style', 'display: true')", element)

                                time.sleep(5)

                                # submit
                                browser.execute_script(
                                    'document.getElementsByName("h-captcha-response")[0].innerHTML="'
                                    + str(response_2captcha_res) + '";'
                                )

                                time.sleep(5)

                                browser.execute_script(
                                    'document.getElementById("emailform").submit();'
                                )
                            except Exception as e:
                                print("error presence_h_captcha : " + str(e))

                            try:
                                presence_connexion_button = browser.find_element_by_xpath(
                                    '/html/body/div[1]/div[2]/main/div/div/div/section/form/button'
                                ).text.replace(' ', '')
                                print("presence_connexion_button : " + str(presence_connexion_button))

                                if presence_connexion_button == "Connexion":
                                    # Insert the password
                                    password_input = browser.find_element_by_xpath(
                                        '/html/body/div[1]/div[2]/main/div/div/div/section/form/div[1]/span/input'
                                    )
                                    password_input.clear()
                                    password_input.send_keys("")
                                    print("password_input.send_keys()")

                                    time.sleep(5)

                                    # Click on the 'Connexion' button
                                    connexion_button = browser.find_element_by_xpath(
                                        '/html/body/div[1]/div[2]/main/div/div/div/section/form/button'
                                    )
                                    connexion_button.click()
                                    print("connexion_button.click()")

                                    time.sleep(10)
                                else:
                                    print("presence_connexion_button non")

                                try:
                                    operation_reussie_text = browser.find_element_by_xpath(
                                        "/html/body/div/div/h1"
                                    ).text
                                    print('operation_reussie_text : ' + str(operation_reussie_text))

                                    time.sleep(5)

                                    browser.quit()
                                except Exception as e:
                                    print('error operation_reussie_text : ' + str(e))

                                    try:
                                        code_verification = browser.find_element_by_xpath(
                                            '//*[@id="label-verification_input"]'
                                        ).text
                                        print('code_verification : ' + str(code_verification))

                                        if code_verification == "Code de vérification":
                                            # Outlook
                                            # Open a new window
                                            browser.execute_script("window.open('');")

                                            # Switch to the new window and open new URL
                                            browser.switch_to.window(browser.window_handles[2])

                                            time.sleep(5)

                                            # open
                                            browser.get('https://outlook.live.com/owa/')

                                            time.sleep(5)

                                            # click on the button "Connexion"
                                            connexion_button = browser.find_element_by_xpath(
                                                "/html/body/header/div/aside/div/nav/ul/li[2]/a"
                                            )
                                            connexion_button.click()
                                            print("connexion_button.click()")

                                            time.sleep(5)

                                            email_input = browser.find_element_by_xpath(
                                                '//*[@id="i0116"]'
                                            )
                                            email_input.clear()
                                            email_input.send_keys(".@outlook.fr")
                                            email_input.send_keys(Keys.ENTER)
                                            print("email_input inserted")

                                            time.sleep(10)

                                            password_input = browser.find_element_by_xpath(
                                                '//*[@id="i0118"]'
                                            )
                                            password_input.clear()
                                            password_input.send_keys("")
                                            password_input.send_keys(Keys.ENTER)
                                            print("password_input inserted")

                                            time.sleep(10)

                                            # click on the checkbox "Ne plus afficher ce message"
                                            ne_plus_afficher_ce_message_checkbox = browser.find_element_by_xpath(
                                                '//*[@id="KmsiCheckboxField"]'
                                            )
                                            ne_plus_afficher_ce_message_checkbox.click()
                                            print("ne_plus_afficher_ce_message_checkbox.click()")

                                            time.sleep(10)

                                            # click on the button "Non"
                                            non_button = browser.find_element_by_xpath(
                                                '//*[@id="idBtn_Back"]'
                                            )
                                            non_button.click()
                                            print("non_button.click()")

                                            time.sleep(15)

                                            # Retrieve the code
                                            code = browser.find_element_by_xpath(
                                                "/html/body/div[3]/div/div[2]/div[2]/div[1]/div/div/div[3]/div[2]"
                                                "/div/div[1]/div[3]/div/div/div/div/div/div[2]/div/div/div/div/div[2]"
                                                "/div/div[1]/span"
                                            ).text.replace('Votre code de vérification Indeed est : ', '')
                                            print('code : ' + str(code))

                                            time.sleep(5)

                                            # Switch to the last window
                                            browser.switch_to.window(browser.window_handles[1])

                                            time.sleep(5)

                                            code_input = browser.find_element_by_xpath(
                                                '//*[@id="verification_input"]'
                                            )
                                            code_input.clear()
                                            code_input.send_keys(str(code))
                                            code_input.send_keys(Keys.ENTER)
                                            print("code_input inserted")

                                            time.sleep(10)

                                            try:
                                                operation_reussie_text = browser.find_element_by_xpath(
                                                    "/html/body/div/div/h1"
                                                ).text
                                                print('operation_reussie_text : ' + str(operation_reussie_text))

                                                time.sleep(5)
                                            except Exception as e:
                                                print('error operation_reussie_text : ' + str(e))

                                            # Switch to the last window
                                            browser.switch_to.window(browser.window_handles[2])

                                            time.sleep(5)

                                            # click on the button "Sélectionner tous les messages"
                                            selectionner_tous_les_messages_button = browser.find_element_by_xpath(
                                                '/html/body/div[3]/div/div[2]/div[2]/div[1]/div/div/div[3]/div[2]/div'
                                                '/div[1]/div[1]/div[1]/div/div[1]/div/i[2]'
                                            )
                                            selectionner_tous_les_messages_button.click()
                                            print("selectionner_tous_les_messages_button.click()")

                                            time.sleep(5)

                                            # click on the button "Vider Prioritaire"
                                            vider_prioritaire_button = browser.find_element_by_xpath(
                                                '/html/body/div[3]/div/div[2]/div[2]/div[1]/div/div/div[3]'
                                                '/div[1]/div/div/div/div/div/div[1]/div[1]/button'
                                            )
                                            vider_prioritaire_button.click()
                                            print("vider_prioritaire_button.click()")

                                            time.sleep(5)

                                            # click on the button "Ok ou Tout supprimer"
                                            tout_supprimer_button = browser.find_element_by_xpath(
                                                '//*[@id="ok-7"]'
                                            )
                                            tout_supprimer_button.click()
                                            print("tout_supprimer_button.click()")

                                            time.sleep(5)

                                            # click on the button "Mon profile"
                                            mon_profile_button = browser.find_element_by_xpath(
                                                '/html/body/div[3]/div/div[1]/div/div[1]/div[3]/div[1]/button'
                                                '/div/div[2]/div/div/div/div/div/div[2]/img'
                                            )
                                            mon_profile_button.click()
                                            print("mon_profile_button.click()")

                                            time.sleep(5)

                                            # click on the button "Se déconnecter"
                                            se_deconnecter_button = browser.find_element_by_xpath(
                                                '//*[@id="mectrl_body_signOut"]'
                                            )
                                            se_deconnecter_button.click()
                                            print("se_deconnecter_button.click()")

                                            time.sleep(10)

                                            browser.quit()
                                        else:
                                            browser.quit()

                                            try:
                                                print("test_reboot")

                                                time.sleep(5)

                                                warnings.filterwarnings(action="ignore", message="unclosed",
                                                                        category=ResourceWarning)

                                                time.sleep(5)

                                                # with Firefox
                                                options = Options()
                                                options.headless = True
                                                browser = webdriver.Firefox(
                                                    executable_path='..\\geckodriver.exe',
                                                    options=options
                                                )

                                                time.sleep(5)

                                                # maximize window
                                                browser.maximize_window()

                                                time.sleep(5)

                                                # open
                                                browser.get('http://www.tplinkmodem.net')
                                                print("browser.get('http://www.tplinkmodem.net')")

                                                time.sleep(15)

                                                password_input = browser.find_element_by_xpath(
                                                    "/html/body/div[3]/div[2]/div[2]/div[1]/div[2]/div[2]/div/div/div[1]/input[1]"
                                                )
                                                password_input.clear()
                                                password_input.send_keys("")
                                                print("password_input.send_keys()")

                                                time.sleep(10)

                                                log_in_button = browser.find_element_by_xpath(
                                                    "/html/body/div[3]/div[2]/div[2]/div[1]/div[2]/div[3]/div/button"
                                                )
                                                log_in_button.click()
                                                print("log_in_button.click()")

                                                time.sleep(20)

                                                reboot_button = browser.find_element_by_xpath(
                                                    '//*[@id="topReboot"]'
                                                )
                                                reboot_button.click()
                                                print("reboot_button.click()")

                                                time.sleep(5)

                                                yes_button = browser.find_element_by_xpath(
                                                    '/html/body/div[7]/div/div[4]/div/div[2]/div/div[2]/button'
                                                )
                                                yes_button.click()
                                                print("yes_button.click()")

                                                time.sleep(120)

                                                browser.quit()
                                                print("browser.quit()")
                                            except Exception as e:
                                                print("error test_reboot : " + str(e))
                                    except Exception as e:
                                        print('error code_verification : ' + str(e))

                                        browser.quit()

                                        try:
                                            print("test_reboot")

                                            time.sleep(5)

                                            warnings.filterwarnings(action="ignore", message="unclosed",
                                                                    category=ResourceWarning)

                                            time.sleep(5)

                                            # with Firefox
                                            options = Options()
                                            options.headless = True
                                            browser = webdriver.Firefox(
                                                executable_path='..\\geckodriver.exe',
                                                options=options
                                            )

                                            time.sleep(5)

                                            # maximize window
                                            browser.maximize_window()

                                            time.sleep(5)

                                            # open
                                            browser.get('http://www.tplinkmodem.net')
                                            print("browser.get('http://www.tplinkmodem.net')")

                                            time.sleep(15)

                                            password_input = browser.find_element_by_xpath(
                                                "/html/body/div[3]/div[2]/div[2]/div[1]/div[2]/div[2]/div/div/div[1]/input[1]"
                                            )
                                            password_input.clear()
                                            password_input.send_keys("")
                                            print("password_input.send_keys()")

                                            time.sleep(10)

                                            log_in_button = browser.find_element_by_xpath(
                                                "/html/body/div[3]/div[2]/div[2]/div[1]/div[2]/div[3]/div/button"
                                            )
                                            log_in_button.click()
                                            print("log_in_button.click()")

                                            time.sleep(20)

                                            reboot_button = browser.find_element_by_xpath(
                                                '//*[@id="topReboot"]'
                                            )
                                            reboot_button.click()
                                            print("reboot_button.click()")

                                            time.sleep(5)

                                            yes_button = browser.find_element_by_xpath(
                                                '/html/body/div[7]/div/div[4]/div/div[2]/div/div[2]/button'
                                            )
                                            yes_button.click()
                                            print("yes_button.click()")

                                            time.sleep(120)

                                            browser.quit()
                                            print("browser.quit()")
                                        except Exception as e:
                                            print("error test_reboot : " + str(e))
                            except Exception as e:
                                print("error presence_connexion_button : " + str(e))

                                browser.quit()

                                try:
                                    print("test_reboot")

                                    time.sleep(5)

                                    warnings.filterwarnings(action="ignore", message="unclosed",
                                                            category=ResourceWarning)

                                    time.sleep(5)

                                    # with Firefox
                                    options = Options()
                                    options.headless = True
                                    browser = webdriver.Firefox(
                                        executable_path='..\\geckodriver.exe',
                                        options=options
                                    )

                                    time.sleep(5)

                                    # maximize window
                                    browser.maximize_window()

                                    time.sleep(5)

                                    # open
                                    browser.get('http://www.tplinkmodem.net')
                                    print("browser.get('http://www.tplinkmodem.net')")

                                    time.sleep(15)

                                    password_input = browser.find_element_by_xpath(
                                        "/html/body/div[3]/div[2]/div[2]/div[1]/div[2]/div[2]/div/div/div[1]/input[1]"
                                    )
                                    password_input.clear()
                                    password_input.send_keys("")
                                    print("password_input.send_keys()")

                                    time.sleep(10)

                                    log_in_button = browser.find_element_by_xpath(
                                        "/html/body/div[3]/div[2]/div[2]/div[1]/div[2]/div[3]/div/button"
                                    )
                                    log_in_button.click()
                                    print("log_in_button.click()")

                                    time.sleep(20)

                                    reboot_button = browser.find_element_by_xpath(
                                        '//*[@id="topReboot"]'
                                    )
                                    reboot_button.click()
                                    print("reboot_button.click()")

                                    time.sleep(5)

                                    yes_button = browser.find_element_by_xpath(
                                        '/html/body/div[7]/div/div[4]/div/div[2]/div/div[2]/button'
                                    )
                                    yes_button.click()
                                    print("yes_button.click()")

                                    time.sleep(120)

                                    browser.quit()
                                    print("browser.quit()")
                                except Exception as e:
                                    print("error test_reboot : " + str(e))
                        else:
                            browser.quit()
                    except Exception as e:
                        print("error test_send_cv_for_one_ad_for_indeed : " + str(e))

                        browser.quit()

                        try:
                            print("test_reboot")

                            time.sleep(5)

                            warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

                            time.sleep(5)

                            # with Firefox
                            options = Options()
                            options.headless = True
                            browser = webdriver.Firefox(
                                executable_path='..\\geckodriver.exe',
                                options=options
                            )

                            time.sleep(5)

                            # maximize window
                            browser.maximize_window()

                            time.sleep(5)

                            # open
                            browser.get('http://www.tplinkmodem.net')
                            print("browser.get('http://www.tplinkmodem.net')")

                            time.sleep(15)

                            password_input = browser.find_element_by_xpath(
                                "/html/body/div[3]/div[2]/div[2]/div[1]/div[2]/div[2]/div/div/div[1]/input[1]"
                            )
                            password_input.clear()
                            password_input.send_keys("")
                            print("password_input.send_keys()")

                            time.sleep(10)

                            log_in_button = browser.find_element_by_xpath(
                                "/html/body/div[3]/div[2]/div[2]/div[1]/div[2]/div[3]/div/button"
                            )
                            log_in_button.click()
                            print("log_in_button.click()")

                            time.sleep(20)

                            reboot_button = browser.find_element_by_xpath(
                                '//*[@id="topReboot"]'
                            )
                            reboot_button.click()
                            print("reboot_button.click()")

                            time.sleep(5)

                            yes_button = browser.find_element_by_xpath(
                                '/html/body/div[7]/div/div[4]/div/div[2]/div/div[2]/button'
                            )
                            yes_button.click()
                            print("yes_button.click()")

                            time.sleep(120)

                            browser.quit()
                            print("browser.quit()")
                        except Exception as e:
                            print("error test_reboot : " + str(e))
            else:
                print("no ads")


if __name__ == '__main__':
    unittest.main()
