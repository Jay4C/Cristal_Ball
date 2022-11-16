import os
import unittest
import time
import warnings
from Screenshot import Screenshot_Clipping
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class UnitTestsWebAutomationLeroyMerlin(unittest.TestCase):
    def test_full_screenshot(self):
        print('test_full_screenshot')

        ob = Screenshot_Clipping.Screenshot()

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
        browser.get('https://www.unibet.fr/pari-sportif-poker')

        time.sleep(20)

        path_folder = "1_Annee_2021\\1_Gant_Anti_Epines"

        full_path_folder = "A:\\2_Personnel\\1_Recurrentes\\3_Mes_Achats_En_Ligne\\15_Leroy_Merlin\\2_Mes_Achats\\" \
                           + path_folder

        ob.full_Screenshot(browser, save_path=full_path_folder, image_name='Page_1.png')

        time.sleep(5)

        browser.close()

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
        browser.get('https://www.leroymerlin.fr/')

        time.sleep(15)

        # click on the "continuer sans accepter" button
        continuer_sans_accepter_button = browser.find_element_by_xpath(
            "/html/body/div[4]/div[3]/div/div/div[1]/div/button"
        )
        continuer_sans_accepter_button.click()

        time.sleep(5)

        # click on the "me connecter" button
        me_connecter_button = browser.find_element_by_xpath(
            "/html/body/div[1]/header/div[9]/div[3]/a"
        )
        me_connecter_button.click()

        time.sleep(5)

        # click on the "email" input
        email_input = browser.find_element_by_xpath(
            "/html/body/div[2]/div/div/div/div[2]/div[1]/form[1]/div/input"
        )
        email_input.clear()
        email_input.send_keys(".@outlook.fr")

        time.sleep(5)

        # Click on the "continuer" button
        continuer_button = browser.find_element_by_xpath(
            "/html/body/div[2]/div/div/div/div[2]/div[1]/form[1]/button"
        )
        continuer_button.click()

        time.sleep(5)

        # click on the "password" input
        password_input = browser.find_element_by_xpath(
            "/html/body/div[2]/div/div/div/div[2]/div[1]/form[2]/div[2]/input"
        )
        password_input.clear()
        password_input.send_keys("")

        time.sleep(5)

        # Click on the "Me connecter" button
        me_connecter_button_1 = browser.find_element_by_xpath(
            "/html/body/div[2]/div/div/div/div[2]/div[1]/form[2]/button"
        )
        me_connecter_button_1.click()

        time.sleep(5)

        print("ccleaner running")
        os.system("set ccleaner='C:\\Program Files\\CCleaner\\CCleaner.exe'")
        os.system("start ccleaner /AUTO")

        time.sleep(5)

    def test_acheter_un_produit(self):
        print("test_acheter_un_produit")

        ob = Screenshot_Clipping.Screenshot()

        # informations carte bancaire
        numero_de_la_carte = ""
        code_de_verification_de_la_carte = ""
        date_expiration_mois = 9

        path_folder = "1_Annee_2021\\1_Gant_Anti_Epines"

        full_path_folder = "A:\\2_Personnel\\1_Recurrentes\\3_Mes_Achats_En_Ligne\\15_Leroy_Merlin\\2_Mes_Achats\\" \
                           + path_folder

        url_produit = "https://www.leroymerlin.fr/produits/terrasse-jardin/outils-de-jardinage/protection-du-jardinier/gants-de-jardinage/gant-long-petits-epineux-rostaing-protectmax-bleu-taille-10-82218905.html"

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
        browser.get(url_produit)

        time.sleep(15)

        # screenshot
        ob.full_Screenshot(browser, save_path=full_path_folder, image_name='Page_1.png')

        time.sleep(10)

        ajouter_au_panier_button = browser.find_element_by_xpath(
            "/html/body/div[2]/div/section[1]/div/div[3]/div/section/div[5]/div[1]/form/div/div[2]/button"
        )
        ajouter_au_panier_button.click()

        time.sleep(10)

        # screenshot
        ob.full_Screenshot(browser, save_path=full_path_folder, image_name='Page_2.png')

        time.sleep(10)

        voir_mon_panier_button = browser.find_element_by_xpath(
            "/html/body/div[1]/div/div[1]/div/div/div[1]/div[2]/a[2]"
        )
        voir_mon_panier_button.click()

        time.sleep(10)

        # screenshot
        ob.full_Screenshot(browser, save_path=full_path_folder, image_name='Page_3.png')

        time.sleep(10)

        valider_mon_panier_button = browser.find_element_by_xpath(
            "/html/body/div[1]/section/div[1]/section/section[2]/div/section[2]/div[2]/button"
        )
        valider_mon_panier_button.click()

        time.sleep(10)

        # screenshot
        ob.full_Screenshot(browser, save_path=full_path_folder, image_name='Page_4.png')

        time.sleep(10)

        livraison_en_point_relais_button = browser.find_element_by_xpath(
            "/html/body/div[1]/section/div/div[1]/section[1]/div/section/ul[2]/li[2]"
        )
        livraison_en_point_relais_button.click()

        time.sleep(10)

        continuer_button = browser.find_element_by_xpath(
            "/html/body/div[1]/section/div/div[1]/section[2]/div/section[2]/div[2]/button"
        )
        continuer_button.click()

        time.sleep(10)

        email_input = browser.find_element_by_xpath(
            "/html/body/div[1]/section/div/div[1]/section[2]/div/section[2]/div[2]/button"
        )
        email_input.clear()
        email_input.send_keys(".@outlook.fr")

        time.sleep(10)

        continuer_button_1 = browser.find_element_by_xpath(
            "/html/body/div[1]/div/div/div[3]/div[1]/div[2]/div[1]/form[1]/button"
        )
        continuer_button_1.click()

        time.sleep(10)

        password_input = browser.find_element_by_xpath(
            "/html/body/div[1]/div/div/div[3]/div[1]/div[2]/div[1]/form[2]/div[2]/input"
        )
        password_input.clear()
        password_input.send_keys("")

        time.sleep(10)

        me_connecter_button = browser.find_element_by_xpath(
            "/html/body/div[1]/div/div/div[3]/div[1]/div[2]/div[1]/form[2]/button"
        )
        me_connecter_button.click()

        time.sleep(10)

        votre_code_postal_input = browser.find_element_by_xpath(
            "/html/body/div[1]/section/div/div[1]/form/section[1]/section[2]/div[1]/p[1]/input"
        )
        votre_code_postal_input.clear()
        votre_code_postal_input.send_keys("")

        time.sleep(10)

        ok_button = browser.find_element_by_xpath(
            "/html/body/div[1]/section/div/div[1]/form/section[1]/section[2]/div[1]/button"
        )
        ok_button.click()

        time.sleep(10)

        exo_monde_button = browser.find_element_by_xpath(
            "/html/body/div[1]/section/div/div[1]/form/section[1]/section[2]/div[2]/ul/li[3]"
        )
        exo_monde_button.click()

        time.sleep(10)

        civilite_checkbox = browser.find_element_by_xpath(
            "/html/body/div[1]/section/div/div[1]/form/section[1]/section[3]/div/fieldset/div/span/span[1]/input"
        )
        civilite_checkbox.click()

        time.sleep(10)

        adresse_postale_input = browser.find_element_by_xpath(
            "/html/body/div[1]/section/div/div[1]/form/section[1]/section[3]/div/p[3]/input"
        )
        adresse_postale_input.clear()
        adresse_postale_input.send_keys("")

        time.sleep(10)

        batiment_etage_code_input = browser.find_element_by_xpath(
            "/html/body/div[1]/section/div/div[1]/form/section[1]/section[3]/div/p[4]/input"
        )
        batiment_etage_code_input.clear()
        batiment_etage_code_input.send_keys("")

        time.sleep(10)

        lieu_dit_boite_postale = browser.find_element_by_xpath(
            "/html/body/div[1]/section/div/div[1]/form/section[1]/section[3]/div/p[5]/input"
        )
        lieu_dit_boite_postale.clear()
        lieu_dit_boite_postale.send_keys("")

        time.sleep(10)

        code_postal_input = browser.find_element_by_xpath(
            "/html/body/div[1]/section/div/div[1]/form/section[1]/section[3]/div/p[7]/input"
        )
        code_postal_input.clear()
        code_postal_input.send_keys("")

        time.sleep(10)

        # tab button
        n = 1
        actions = ActionChains(browser)
        actions.send_keys(Keys.TAB * n)
        actions.perform()

        time.sleep(10)

        # screenshot
        ob.full_Screenshot(browser, save_path=full_path_folder, image_name='Page_5.png')

        time.sleep(10)

        continuer_button_2 = browser.find_element_by_xpath(
            "/html/body/div[1]/section/div/div[1]/form/section[2]/div/section[2]/div[2]/button"
        )
        continuer_button_2.click()

        time.sleep(10)

        carte_bancaire_button = browser.find_element_by_xpath(
            "/html/body/div[1]/section/div/div[1]/form/section/div[1]/div[1]/input"
        )
        carte_bancaire_button.click()

        time.sleep(10)

        # screenshot
        ob.full_Screenshot(browser, save_path=full_path_folder, image_name='Page_6.png')

        time.sleep(10)

        regler_button = browser.find_element_by_xpath(
            "/html/body/div[1]/section/div/div[1]/form/section/div[1]/div[2]/div/button"
        )
        regler_button.click()

        time.sleep(10)

        titulaire_de_la_carte_button = browser.find_element_by_xpath(
            "/html/body/div/div[2]/form/table/tbody/tr[2]/td[2]/small/input"
        )
        titulaire_de_la_carte_button.clear()
        titulaire_de_la_carte_button.send_keys("")

        time.sleep(10)

        numero_de_la_carte_button = browser.find_element_by_xpath(
            "/html/body/div/div[2]/form/table/tbody/tr[3]/td[2]/small/input[3]"
        )
        numero_de_la_carte_button.clear()
        numero_de_la_carte_button.send_keys(numero_de_la_carte)

        time.sleep(10)

        code_de_verification_de_la_carte_button = browser.find_element_by_xpath(
            "/html/body/div/div[2]/form/table/tbody/tr[5]/td[2]/small[1]/input"
        )
        code_de_verification_de_la_carte_button.clear()
        code_de_verification_de_la_carte_button.send_keys(code_de_verification_de_la_carte)

        time.sleep(10)

        date_expiration_mois_select = browser.find_element_by_xpath(
            "/html/body/div/div[2]/form/table/tbody/tr[4]/td[2]/small/select[1]/option["
            + str(date_expiration_mois + 1) + "]"
        )
        date_expiration_mois_select.click()

        time.sleep(10)

        date_expiration_annee_select = browser.find_element_by_xpath(
            "/html/body/div/div[2]/form/table/tbody/tr[4]/td[2]/small/select[2]/option[2]"
        )
        date_expiration_annee_select.click()

        time.sleep(10)

        # screenshot
        ob.full_Screenshot(browser, save_path=full_path_folder, image_name='Page_7.png')

        time.sleep(10)

        oui_je_confirme_mon_paiement = browser.find_element_by_xpath(
            "/html/body/div/div[2]/form/table/tbody/tr[7]/td/small/input"
        )
        oui_je_confirme_mon_paiement.click()

        time.sleep(10)


if __name__ == '__main__':
    unittest.main()
