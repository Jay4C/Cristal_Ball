import unittest
import time
import warnings
from selenium import webdriver
from Screenshot import Screenshot_Clipping
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class UnitTestsWebAutomationAimntBoutique(unittest.TestCase):
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
        browser.get('https://www.aimant-boutique.fr/account')

        time.sleep(15)

        # Insert the "Adresse email" input
        adresse_email_input = browser.find_element_by_xpath(
            '//*[@id="email"]'
        )
        adresse_email_input.send_keys(".@outlook.fr")
        time.sleep(10)

        # Insert the "Mot de passe" input
        mot_de_passe_input = browser.find_element_by_xpath(
            '//*[@id="passwort"]'
        )
        mot_de_passe_input.send_keys("")
        time.sleep(10)

        # Click on the "Se connecter" button
        identifiez_vous_button = browser.find_element_by_xpath(
            '/html/body/div[1]/div[3]/section/div/div/div[4]/div[2]/div/form/div[5]/button'
        )
        identifiez_vous_button.click()
        time.sleep(10)

    def test_changer_de_mode_paiement(self):
        print('test_changer_de_mode_paiement')

        # informations bancaires
        numero_carte = 5
        cvv = 2
        date_expiration_mois = 9
        date_expiration_annee = 2

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
        browser.get('https://www.aimant-boutique.fr/account')

        time.sleep(15)

        # Insert the "Adresse email" input
        adresse_email_input = browser.find_element_by_xpath(
            '//*[@id="email"]'
        )
        adresse_email_input.send_keys(".@outlook.fr")
        time.sleep(10)

        # Insert the "Mot de passe" input
        mot_de_passe_input = browser.find_element_by_xpath(
            '//*[@id="passwort"]'
        )
        mot_de_passe_input.send_keys("")
        time.sleep(10)

        # Click on the "Se connecter" button
        identifiez_vous_button = browser.find_element_by_xpath(
            '/html/body/div[1]/div[3]/section/div/div/div[4]/div[2]/div/form/div[5]/button'
        )
        identifiez_vous_button.click()
        time.sleep(15)

        # Go to https://www.aimant-boutique.fr/account/payment
        browser.get("https://www.aimant-boutique.fr/account/payment")
        time.sleep(10)

        # Click on the "Kreditkarte" button
        kreditkarte_button = browser.find_element_by_xpath(
            '/html/body/div[1]/div[3]/section/div/div/div/div[3]/div/form/div[1]/div/div[1]/div[1]/input'
        )
        kreditkarte_button.click()
        time.sleep(10)

        # Down in 5 times
        n = 5
        actions = ActionChains(browser)
        actions.send_keys(Keys.DOWN * n)
        actions.perform()

        time.sleep(10)

        # Click on the "Karteninhaber" button
        karteninhaber_input = browser.find_element_by_xpath(
            '/html/body/div[1]/div[3]/section/div/div/div/div[3]/div/form/div[1]/div/div[1]/div[5]/div/div[4]/input'
        )
        karteninhaber_input.clear()
        karteninhaber_input.send_keys("Mr Jason ALOYAU")
        time.sleep(10)

        # Click on the "Kartennummer" button
        kartennummer_input = browser.find_element_by_xpath(
            '//*[@id="cardpan"]'
        )
        kartennummer_input.clear()
        kartennummer_input.send_keys(numero_carte)
        time.sleep(10)

        # Click on the "Gültig Bis month" button
        gultig_bis_month_select = browser.find_element_by_xpath(
            '/html/body/select/option[' + str(date_expiration_mois + 1) + ']'
        )
        gultig_bis_month_select.click()
        time.sleep(10)

        # Click on the "Gültig Bis year" button
        gultig_bis_year_select = browser.find_element_by_xpath(
            '/html/body/select/option[' + str(date_expiration_annee - 2019) + ']'
        )
        gultig_bis_year_select.click()
        time.sleep(10)

        # Click on the "Prüfziffer" button
        prufziffer_input = browser.find_element_by_xpath(
            '//*[@id="cardcvc2"]'
        )
        prufziffer_input.clear()
        prufziffer_input.send_keys(cvv)
        time.sleep(10)

        # Click on the "Modifier" button
        modifier_button = browser.find_element_by_xpath(
            '/html/body/div[1]/div[3]/section/div/div/div/div[3]/div/form/div[2]/input'
        )
        modifier_button.click()
        time.sleep(10)

    def test_acheter_un_article(self):
        print('test_acheter_un_article')

        url_article = "https://www.aimant-boutique.fr/ferrite/parallelepipedes-aimantes/cuboide-150.0-x-100.0-x-20.0-mm-y35-ferrite"

        ob = Screenshot_Clipping.Screenshot()

        # informations bancaires
        numero_carte = 22
        cvv = 2
        date_expiration_mois = 9
        date_expiration_annee = 2

        quantite = 1

        path_folder = "1_Annee_2021\\Commande_1"

        full_path_folder = "A:\\2_Personnel\\1_Recurrentes\\3_Mes_Achats_En_Ligne\\17_Aimant_Boutique\\2_Mes_Commandes\\" + path_folder

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
        browser.get(url_article)
        print("page opened")
        time.sleep(15)

        # selectionner la quantite
        quantite_input = browser.find_element_by_xpath(
            '/html/body/div[1]/div[3]/section/div/div/div[1]/div[1]/div[3]/div/form/div/div/input'
        )
        quantite_input.clear()
        quantite_input.send_keys(quantite)
        print("quantite_input inserted")
        time.sleep(10)

        # screenshot
        ob.full_Screenshot(browser, save_path=full_path_folder, image_name='Page_1.png')
        print("screenshot Page_1.png")
        time.sleep(10)

        # Click "Ajouter au panier" button
        ajouter_au_panier_button = browser.find_element_by_xpath(
            "/html/body/div[1]/div[3]/section/div/div/div[1]/div[1]/div[3]/div/form/div/button"
        )
        ajouter_au_panier_button.click()
        print("ajouter_au_panier_button clicked")
        time.sleep(10)

        # Click "Valider la commande" button
        valider_la_commande_button = browser.find_element_by_xpath(
            "/html/body/div[1]/div[3]/header/div/div[2]/div/div/div[5]/a[1]"
        )
        valider_la_commande_button.click()
        print("valider_la_commande_button clicked")
        time.sleep(10)

        # Insert the "Adresse email" input
        adresse_email_input = browser.find_element_by_xpath(
            '//*[@id="email"]'
        )
        adresse_email_input.send_keys(".@outlook.fr")
        print("adresse_email_input inserted")
        time.sleep(10)

        # Insert the "Mot de passe" input
        mot_de_passe_input = browser.find_element_by_xpath(
            '//*[@id="passwort"]'
        )
        mot_de_passe_input.send_keys("")
        print("mot_de_passe_input inserted")
        time.sleep(10)

        # screenshot
        ob.full_Screenshot(browser, save_path=full_path_folder, image_name='Page_2.png')
        print("screenshot Page_2.png")
        time.sleep(10)

        # Click on the "Se connecter" button
        identifiez_vous_button = browser.find_element_by_xpath(
            '/html/body/div[1]/div[3]/section/div/div/div[4]/div[2]/div/form/div[5]/button'
        )
        identifiez_vous_button.click()
        time.sleep(10)


if __name__ == '__main__':
    unittest.main()
