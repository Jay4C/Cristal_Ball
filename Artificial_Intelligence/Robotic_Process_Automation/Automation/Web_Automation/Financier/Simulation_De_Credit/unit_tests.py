import unittest
import time
import warnings
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


class UnitTestsWebAutomationSimulationDeCredit(unittest.TestCase):
    def test_simuler_sans_headless(self):
        print("test_simuler_sans_headless")

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
        browser.get('https://www.simulationdecredit.fr/')

        time.sleep(20)

        # click on 'continuer sans accepter' button
        continuer_sans_accepter_button = browser.find_element_by_xpath(
            '/html/body/div[2]/div[2]/div[1]/div/div/div/div/button/span'
        )
        continuer_sans_accepter_button.click()

        time.sleep(10)

        # insert montant_du_credit_input
        montant_du_credit_input = browser.find_element_by_xpath(
            '/html/body/div[1]/div[3]/div[1]/form/table/tbody/tr[1]/td[2]/input'
        )
        montant_du_credit_input.clear()
        montant_du_credit_input.send_keys('1000000')
        
        time.sleep(5)
        
        # insert duree
        duree_input = browser.find_element_by_xpath(
            '/html/body/div[1]/div[3]/div[1]/form/table/tbody/tr[3]/td[2]/input[1]'
        )
        duree_input.clear()
        duree_input.send_keys('20')

        time.sleep(5)

        # insert taux
        taux_input = browser.find_element_by_xpath(
            '/html/body/div[1]/div[3]/div[1]/form/table/tbody/tr[4]/td[2]/input'
        )
        taux_input.clear()
        taux_input.send_keys('1')

        time.sleep(5)

        # click on 'simuler' button
        simuler_button = browser.find_element_by_xpath(
            '/html/body/div[1]/div[3]/div[1]/form/table/tbody/tr[5]/td[2]/input'
        )
        simuler_button.click()

        time.sleep(10)

        # Mensualité text
        mensualite_text = browser.find_element_by_xpath(
            '/html/body/div[1]/div[3]/div[1]/div/div/dl/dd[1]'
        ).text
        print("mensualite_text : " + str(mensualite_text))

        time.sleep(5)

        # Coût du prêt text
        cout_du_pret_text = browser.find_element_by_xpath(
            '/html/body/div[1]/div[3]/div[1]/div/div/dl/dd[2]'
        ).text
        print("cout_du_pret_text : " + str(cout_du_pret_text))

        time.sleep(5)

        browser.close()

    def test_simuler_avec_headless(self):
        print("test_simuler_avec_headless")

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
        browser.get('https://www.simulationdecredit.fr/')

        time.sleep(20)

        # click on 'continuer sans accepter' button
        continuer_sans_accepter_button = browser.find_element_by_xpath(
            '/html/body/div[2]/div[2]/div[1]/div/div/div/div/button/span'
        )
        continuer_sans_accepter_button.click()

        time.sleep(10)

        # insert montant_du_credit_input
        montant_du_credit_input = browser.find_element_by_xpath(
            '/html/body/div[1]/div[3]/div[1]/form/table/tbody/tr[1]/td[2]/input'
        )
        montant_du_credit_input.clear()
        montant_du_credit_input.send_keys('1000000')

        time.sleep(5)

        # insert duree
        duree_input = browser.find_element_by_xpath(
            '/html/body/div[1]/div[3]/div[1]/form/table/tbody/tr[3]/td[2]/input[1]'
        )
        duree_input.clear()
        duree_input.send_keys('20')

        time.sleep(5)

        # insert taux
        taux_input = browser.find_element_by_xpath(
            '/html/body/div[1]/div[3]/div[1]/form/table/tbody/tr[4]/td[2]/input'
        )
        taux_input.clear()
        taux_input.send_keys('1')

        time.sleep(5)

        # click on 'simuler' button
        simuler_button = browser.find_element_by_xpath(
            '/html/body/div[1]/div[3]/div[1]/form/table/tbody/tr[5]/td[2]/input'
        )
        simuler_button.click()

        time.sleep(10)

        # Mensualité text
        mensualite_text = browser.find_element_by_xpath(
            '/html/body/div[1]/div[3]/div[1]/div/div/dl/dd[1]'
        ).text
        print("mensualite_text : " + str(mensualite_text))

        time.sleep(5)

        # Coût du prêt text
        cout_du_pret_text = browser.find_element_by_xpath(
            '/html/body/div[1]/div[3]/div[1]/div/div/dl/dd[2]'
        ).text
        print("cout_du_pret_text : " + str(cout_du_pret_text))

        time.sleep(5)

        browser.close()
        print("browser closed")


if __name__ == '__main__':
    unittest.main()
