import unittest
import time
import warnings
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui
import requests
import json
from Service.MachineLearning.SupervisedLearning.Forex import forex


class UnitTestsWebAutomationIqOptionWithoutHeadless(unittest.TestCase):
    # ok
    def test_se_connecter(self):
        print('test_se_connecter')

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
        browser.get('https://login.iqoption.com/fr/login')

        time.sleep(15)

        """
        # click on "c'est compris" button
        compris_button = browser.find_element_by_xpath("/html/body/div[6]/div/div/div/div/div/div[2]/div")
        compris_button.click()

        time.sleep(10)
        """

        # Insert the "email" input
        email_input = browser.find_element_by_xpath("/html/body/div[3]/div/div[1]/div/div/form/div[1]/div/div/input")
        email_input.clear()
        email_input.send_keys("")

        time.sleep(10)

        # Insert the "mot de passe" input
        mot_de_passe_input = browser.find_element_by_xpath("/html/body/div[3]/div/div[1]/div/div/form/div[2]/div/div/input")
        mot_de_passe_input.clear()
        mot_de_passe_input.send_keys("")

        time.sleep(10)

        # click on "se connecter" button
        se_connecter_button = browser.find_element_by_xpath("/html/body/div[3]/div/div[1]/div/div/form/button")
        se_connecter_button.click()

        time.sleep(30)

        # click on "J'accepte" button
        j_accepte_button = browser.find_element_by_xpath("/html/body/div[11]/div/div/div/div[1]/div[1]/div/div/div/button")
        j_accepte_button.click()

        time.sleep(10)

    # ok
    def test_show_the_coordinates_of_one_element(self):
        print("")

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
        browser.get('https://login.iqoption.com/fr/login')

        time.sleep(15)

        se_connecter_button = browser.find_element_by_xpath("/html/body/div[3]/div/div[1]/div/div/form/button")
        location = se_connecter_button.location
        print("location se_connecter_button : " + str(location))

    # non
    def test_click_with_coordinates(self):
        print("test_click_with_coordinates")

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
        browser.get('https://login.iqoption.com/fr/login')
        print("browser.get('https://login.iqoption.com/fr/login')")

        time.sleep(10)

        # click on "c'est compris" button
        compris_button = browser.find_element_by_xpath("/html/body/div[6]/div/div/div/div/div/div[2]/div")
        compris_button.click()

        time.sleep(10)

        # Insert the "email" input
        email_input = browser.find_element_by_xpath("/html/body/div[3]/div/div[1]/div/div/form/div[1]/div/div/input")
        email_input.clear()
        email_input.send_keys("")

        time.sleep(10)

        # Insert the "mot de passe" input
        mot_de_passe_input = browser.find_element_by_xpath(
            "/html/body/div[3]/div/div[1]/div/div/form/div[2]/div/div/input")
        mot_de_passe_input.clear()
        mot_de_passe_input.send_keys("")

        time.sleep(10)

        # click on "se connecter" button
        se_connecter_button = browser.find_element_by_xpath("/html/body/div[3]/div/div[1]/div/div/form/button")
        se_connecter_button.click()

        time.sleep(30)

        # click on "J'accepte" button
        j_accepte_button = browser.find_element_by_xpath(
            "/html/body/div[11]/div/div/div/div[1]/div[1]/div/div/div/button")
        j_accepte_button.click()

        time.sleep(10)

        # open 'https://eu.iqoption.com/traderoom'
        browser.get('https://eu.iqoption.com/traderoom')

        time.sleep(30)

        # Click on the "solde" button with coordinates
        # browser.execute_script("document.elementFromPoint(496, 304).click();")
        # browser.execute_script("el = document.elementFromPoint(496, 304); el.click();")
        # pointer_actions = PointerActions(browser)
        # pointer_actions.move_to(browser.find_element_by_tag_name('body'), 0, 0)
        # pointer_actions.move_by(x=700, y=400).click()
        actions = ActionChains(browser)
        actions.move_to_element_with_offset(browser.find_element_by_id('glcanvas'), 0, 0)
        actions.move_by_offset(750, 50).click().perform()

        time.sleep(10)


class UnitTestsWebAutomationIqOptionWithoutHeadlessForTrading(unittest.TestCase):
    # ok
    def test_trader_compte_apprentissage_without_headless_for_dell(self):
        print('test_trader_compte_apprentissage_without_headless_for_dell')

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
        browser.get('https://login.iqoption.com/fr/login')

        time.sleep(15)

        # Insert the "email" input
        email_input = browser.find_element_by_xpath("/html/body/div[3]/div/div[1]/div/div/form/div[1]/div/div/input")
        email_input.clear()
        email_input.send_keys("")

        time.sleep(10)

        # Insert the "mot de passe" input
        mot_de_passe_input = browser.find_element_by_xpath("/html/body/div[3]/div/div[1]/div/div/form/div[2]/div/div/input")
        mot_de_passe_input.clear()
        mot_de_passe_input.send_keys("")

        time.sleep(10)

        # click on "se connecter" button
        se_connecter_button = browser.find_element_by_xpath("/html/body/div[3]/div/div[1]/div/div/form/button")
        se_connecter_button.click()

        time.sleep(30)

        # click on "J'accepte" button
        j_accepte_button = browser.find_element_by_xpath("/html/body/div[11]/div/div/div/div[1]/div[1]/div/div/div/button")
        j_accepte_button.click()

        time.sleep(10)

        # open 'https://eu.iqoption.com/traderoom'
        browser.get('https://eu.iqoption.com/traderoom')

        time.sleep(35)

        # Click on the "solde" button with coordinates
        pyautogui.click(1180, 120)

        time.sleep(5)

        # Click on the "Compte d'apprentissage" button with coordinates
        pyautogui.click(1100, 320)

        time.sleep(5)

        # Click on the "Fermer" button with coordinates
        pyautogui.click(685, 525)

        time.sleep(10)

        for i in range(0, 1000):
            # Prices
            price_now = 0

            price_future = 0

            price_future += forex.ForexFinal.get_the_future_quote_eur_usd_global_final()

            # Retrieve the EUR_USD_rate price_now
            url = "https://www.freeforexapi.com/api/live?pairs=EURUSD"
            response = requests.request("GET", url)
            rate = json.loads(response.text)['rates']['EURUSD']['rate']
            print("EUR_USD_rate price_now : " + str(rate))
            price_now += rate

            if price_now - price_future >= 0:
                # Click on the "Somme input" button with coordinates
                pyautogui.click(1300, 200)

                time.sleep(5)

                # Clean on the "Somme input" button with coordinates
                pyautogui.press("backspace", presses=5)

                time.sleep(5)

                # Insert the value "Somme input"
                pyautogui.write("5000")

                time.sleep(5)

                # Click on the "Vendre" button with coordinates
                pyautogui.click(1300, 580)  # Vendre
            else:
                # Click on the "Somme input" button with coordinates
                pyautogui.click(1300, 200)

                time.sleep(5)

                # Clean on the "Somme input" button with coordinates
                pyautogui.press("backspace", presses=5)

                time.sleep(5)

                # Insert the value "Somme input"
                pyautogui.write("5000")

                time.sleep(5)

                # Click on the "Acheter" button with coordinates
                pyautogui.click(1300, 500)  # Acheter

            time.sleep(90)

            # Click on the "Fermer" button with coordinates
            pyautogui.click(1150, 200)

            time.sleep(5)

            # Click on the "Fermer tout" button with coordinates
            pyautogui.click(1110, 390)

            time.sleep(5)

    #
    def test_trader_compte_apprentissage_without_headless_for_hp(self):
        print('test_trader_compte_apprentissage_without_headless_for_hp')

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
        browser.get('https://login.iqoption.com/fr/login')

        time.sleep(15)

        # Insert the "email" input
        email_input = browser.find_element_by_xpath("/html/body/div[3]/div/div[1]/div/div/form/div[1]/div/div/input")
        email_input.clear()
        email_input.send_keys("")

        time.sleep(10)

        # Insert the "mot de passe" input
        mot_de_passe_input = browser.find_element_by_xpath("/html/body/div[3]/div/div[1]/div/div/form/div[2]/div/div/input")
        mot_de_passe_input.clear()
        mot_de_passe_input.send_keys("")

        time.sleep(10)

        # click on "se connecter" button
        se_connecter_button = browser.find_element_by_xpath("/html/body/div[3]/div/div[1]/div/div/form/button")
        se_connecter_button.click()

        time.sleep(30)

        # click on "J'accepte" button
        j_accepte_button = browser.find_element_by_xpath("/html/body/div[11]/div/div/div/div[1]/div[1]/div/div/div/button")
        j_accepte_button.click()

        time.sleep(10)

        # open 'https://eu.iqoption.com/traderoom'
        browser.get('https://eu.iqoption.com/traderoom')

        time.sleep(35)

        # Click on the "solde" button with coordinates
        pyautogui.click(1350, 125)

        time.sleep(5)

        # Click on the "Compte d'apprentissage" button with coordinates
        pyautogui.click(1350, 320)

        time.sleep(5)

        # Click on the "Fermer" button with coordinates
        pyautogui.click(770, 535)

        time.sleep(10)

        for i in range(0, 10):
            # Prices
            price_now = 0

            price_future = 0

            price_future += forex.ForexFinal.get_the_future_quote_eur_usd_global_final()

            # Retrieve the EUR_USD_rate price_now
            url = "https://www.freeforexapi.com/api/live?pairs=EURUSD"
            response = requests.request("GET", url)
            rate = json.loads(response.text)['rates']['EURUSD']['rate']
            print("EUR_USD_rate price_now : " + str(rate))
            price_now += rate

            if price_now - price_future >= 0:
                # Click on the "Somme input" button with coordinates
                pyautogui.click(1550, 200)

                time.sleep(5)

                # Clean on the "Somme input" button with coordinates
                pyautogui.press("backspace", presses=5)

                time.sleep(5)

                # Insert the value "Somme input"
                pyautogui.write("100")

                time.sleep(5)

                # Click on the "Vendre" button with coordinates
                # Vendre
                pyautogui.click(1550, 635)
            else:
                # Click on the "Somme input" button with coordinates
                pyautogui.click(1550, 200)

                time.sleep(5)

                # Clean on the "Somme input" button with coordinates
                pyautogui.press("backspace", presses=5)

                time.sleep(5)

                # Insert the value "Somme input"
                pyautogui.write("100")

                time.sleep(5)

                # Click on the "Acheter" button with coordinates
                # Acheter
                pyautogui.click(1550, 500)

            time.sleep(90)

            # Click on the "Fermer" button with coordinates
            pyautogui.click(1385, 200)

            time.sleep(5)

            # Click on the "Fermer tout" button with coordinates
            pyautogui.click(1350, 390)

            time.sleep(5)


if __name__ == '__main__':
    unittest.main()
