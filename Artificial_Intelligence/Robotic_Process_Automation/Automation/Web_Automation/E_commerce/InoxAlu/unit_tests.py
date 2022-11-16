import unittest
import time
import warnings
from selenium import webdriver
from Screenshot import Screenshot_Clipping
from selenium.webdriver.firefox.options import Options


class UnitTestsWebAutomationInoxAlu(unittest.TestCase):
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
        browser.get('https://www.inoxalu.fr/')

        time.sleep(5)

        # Click on the "Se connecter" button
        se_connecter_button = browser.find_element_by_xpath(
            "/html/body/div[2]/form/header/div[2]/div/div[3]/a/span"
        )
        se_connecter_button.click()

        time.sleep(10)

        # Insert the "Adresse email" input
        adresse_email_input = browser.find_element_by_xpath(
            '//*[@id="ContentPlaceHolder1_txtEmailCnx"]'
        )
        adresse_email_input.send_keys(".@outlook.fr")
        time.sleep(10)

        # Insert the "Mot de passe" input
        mot_de_passe_input = browser.find_element_by_xpath(
            '//*[@id="ContentPlaceHolder1_txtMDP"]'
        )
        mot_de_passe_input.send_keys("")
        time.sleep(10)

        # Click on the "Identifiez-vous" button
        identifiez_vous_button = browser.find_element_by_xpath(
            '//*[@id="ContentPlaceHolder1_bCnx"]'
        )
        identifiez_vous_button.click()
        time.sleep(10)

    def test_acheter_un_produit_avec_headless(self):
        print("test_acheter_un_produit_avec_headless")

        ob = Screenshot_Clipping.Screenshot()

        # informations bancaires
        numero_carte = 5
        cvv = 2
        date_expiration_mois = 9
        date_expiration_annee = 2

        path_folder = "1_Annee_2021\\1__12_Tubes_Ronds_10x1_10cm_16_08_2021"

        full_path_folder = "A:\\2_Personnel\\1_Recurrentes\\3_Mes_Achats_En_Ligne\\14_Inoxalu\\2_Mes_Commandes\\" + path_folder

        url_produit = "https://www.inoxalu.fr/Article.aspx?itmID=401-inox-316l-marine-tubes-ronds-brut"

        quantite = 6

        longueur = 10

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
        print("browser.maximize_window() opened")

        time.sleep(5)

        # open
        browser.get(url_produit)
        print("page opened")

        time.sleep(15)

        # Select the "QUANTITÉ"
        quantite = browser.find_element_by_xpath(
            "/html/body/div[2]/form/main/div/div/div[2]/div/div[1]/div[2]/div/div[4]/div/div/select/option["
            + str(quantite)
            + "]"
        )
        quantite.click()
        time.sleep(10)
        print("quantite clicked")

        # Select the "Longueur en cm"
        longueur = browser.find_element_by_xpath(
            "/html/body/div[2]/form/main/div/div/div[2]/div/div[1]/div[2]/div/div[3]/div/select/option["
            + str(longueur - 9)
            + "]"
        )
        longueur.click()
        time.sleep(10)
        print("longueur clicked")

        # screenshot
        ob.full_Screenshot(browser, save_path=full_path_folder, image_name='Page_1.png')
        time.sleep(10)
        print("screenshot Page_1.png")

        # Click on the "Ajouter au panier" button
        ajouter_au_panier_button = browser.find_element_by_xpath(
            "/html/body/div[2]/form/main/div/div/div[2]/div/div[1]/div[2]/div/div[4]/div/button"
        )
        ajouter_au_panier_button.click()
        time.sleep(10)
        print("ajouter_au_panier_button clicked")

        # screenshot
        ob.full_Screenshot(browser, save_path=full_path_folder, image_name='Page_2.png')
        time.sleep(10)
        print("screenshot Page_2.png")

        # Click on the "Suivant" button
        suivant_1_button = browser.find_element_by_xpath(
            "/html/body/div[2]/form/main/div[2]/div/div[3]/div/table/tbody/tr/td[3]/input"
        )
        suivant_1_button.click()
        time.sleep(10)
        print("suivant_1_button clicked")

        # Insert the "Adresse email" input
        adresse_email_input = browser.find_element_by_xpath(
            '//*[@id="ContentPlaceHolder1_txtEmailCnx"]'
        )
        adresse_email_input.send_keys(".@outlook.fr")
        time.sleep(10)
        print("adresse_email_input inserted")

        # Insert the "Mot de passe" input
        mot_de_passe_input = browser.find_element_by_xpath(
            '//*[@id="ContentPlaceHolder1_txtMDP"]'
        )
        mot_de_passe_input.send_keys("")
        time.sleep(10)
        print("mot_de_passe_input inserted")

        # Click on the "Identifiez-vous" button
        identifiez_vous_button = browser.find_element_by_xpath(
            '//*[@id="ContentPlaceHolder1_bCnx"]'
        )
        identifiez_vous_button.click()
        time.sleep(10)
        print("identifiez_vous_button clicked")

        # screenshot
        ob.full_Screenshot(browser, save_path=full_path_folder, image_name='Page_3.png')
        time.sleep(10)
        print("screenshot Page_3.png")

        # Click on the "Suivant" button
        suivant_2_button = browser.find_element_by_xpath(
            "/html/body/div[2]/form/main/div[2]/div/div[3]/div/table/tbody/tr/td[3]/input"
        )
        suivant_2_button.click()
        time.sleep(10)
        print("suivant_2_button clicked")

        # screenshot
        ob.full_Screenshot(browser, save_path=full_path_folder, image_name='Page_4.png')
        time.sleep(10)
        print("screenshot Page_4.png")

        # Click on the "Suivant" button
        suivant_3_button = browser.find_element_by_xpath(
            "/html/body/div[2]/form/main/div[2]/div/div[4]/div/table/tbody/tr/td[3]/input"
        )
        suivant_3_button.click()
        time.sleep(10)
        print("suivant_3_button clicked")

        # Click on the "Livraison DPD à domicile" button
        livraison_a_domicile_button = browser.find_element_by_xpath(
            "/html/body/div[2]/form/main/div[2]/div/div[5]/div/section/div[1]/div[2]/blockquote/div/div[2]/input"
        )
        livraison_a_domicile_button.click()
        time.sleep(10)
        print("livraison_a_domicile_button clicked")

        # screenshot
        ob.full_Screenshot(browser, save_path=full_path_folder, image_name='Page_5.png')
        time.sleep(10)
        print("screenshot Page_5.png")

        """
        # Click on the "Livraison DPD en point relais" button
        livraison_point_relais_button = browser.find_element_by_xpath(
            "/html/body/div[2]/form/main/div[2]/div/div[5]/div/section/div[1]/div[3]/blockquote/div/div[2]/input"
        )
        livraison_point_relais_button.click()
        time.sleep(10)
        print('livraison_point_relais_button clicked')

        # Insert the "Entrer le code postal du lieu souhaité" input
        code_postal_input = browser.find_element_by_xpath(
            "/html/body/div[2]/form/main/div[2]/div/div[5]/div/section/div[1]/div[4]/div/div/div[2]/input"
        )
        code_postal_input.send_keys("93800")
        time.sleep(10)
        print('code_postal_input inserted')

        # Click on the "Rechercher un point Relais" button
        rechercher_un_point_relais_button = browser.find_element_by_xpath(
            "/html/body/div[2]/form/main/div[2]/div/div[5]/div/section/div[1]/div[4]/div/div/div[3]/input"
        )
        rechercher_un_point_relais_button.click()
        time.sleep(10)
        print('rechercher_un_point_relais_button clicked')
        
        # Click on the "H2a_boulangerie" button
        h2a_boulangerie_button = browser.find_element_by_xpath(
            "/html/body/div[2]/form/main/div[2]/div/div[5]/div/section/div[1]/div[4]/div/div[2]/table/tbody/tr[2]/td[1]/div/div[1]/div[1]/blockquote/p/input"
        )
        h2a_boulangerie_button.click()
        time.sleep(10)
        print('h2a_boulangerie_button clicked')
        """

        # Click on the "Conditions générales de vente" button
        cgv_button = browser.find_element_by_xpath(
            "/html/body/div[2]/form/main/div[2]/div/div[5]/div/section/div[1]/div[5]/p/span/input"
        )
        cgv_button.click()
        time.sleep(10)
        print("cgv_button clicked")

        # Click on the "Suivant" button
        suivant_4_button = browser.find_element_by_xpath(
            "/html/body/div[2]/form/main/div[2]/div/div[5]/div/section/div[2]/table/tbody/tr/td[3]/input"
        )
        suivant_4_button.click()
        time.sleep(10)
        print("suivant_4_button clicked")

        # Click on the "Carte bancaire" button
        carte_bancaire_button = browser.find_element_by_xpath(
            "/html/body/div[2]/form/main/div[2]/div/div[6]/div/div/div/div[1]/table/tbody/tr[9]/td/div/div[4]/input"
        )
        carte_bancaire_button.click()
        time.sleep(10)
        print("carte_bancaire_button clicked")

        # screenshot
        ob.full_Screenshot(browser, save_path=full_path_folder, image_name='Page_6.png')
        time.sleep(10)
        print("screenshot Page_6.png")

        # Click on the "Acheter" button
        acheter_button = browser.find_element_by_xpath(
            "/html/body/div[2]/form/main/div[2]/div/div[6]/div/div/div/div[2]/div/div/p/input"
        )
        acheter_button.click()
        time.sleep(15)
        print("acheter_button clicked")

        # Insert the "Numéro de carte bancaire" input
        numero_de_carte_bancaire_input = browser.find_element_by_xpath(
            "/html/body/div/table/tbody/tr/td/div[3]/table/tbody/tr/td/div/div/table/tbody/tr/td[2]/div[3]"
            "/form/table/tbody/tr[1]/td[2]/input"
        )
        numero_de_carte_bancaire_input.send_keys(numero_carte)
        time.sleep(10)
        print("numero_de_carte_bancaire_input inserted")

        # Click on the "date_expiration_mois_button" select
        date_expiration_mois_button = browser.find_element_by_xpath(
            "/html/body/div/table/tbody/tr/td/div[3]/table/tbody/tr/td/div/div/table/tbody/tr/td[2]/div[3]"
            "/form/table/tbody/tr[2]/td[2]/select[1]/option[" + str(date_expiration_mois + 1) + "]"
        )
        date_expiration_mois_button.click()
        time.sleep(10)
        print("date_expiration_mois_button clicked")

        # Click on the "date_expiration_annee_button" select
        date_expiration_annee_button = browser.find_element_by_xpath(
            "/html/body/div/table/tbody/tr/td/div[3]/table/tbody/tr/td/div/div/table/tbody/tr/td[2]/div[3]/form"
            "/table/tbody/tr[2]/td[2]/select[2]/option[" + str(date_expiration_annee - 2019) + "]"
        )
        date_expiration_annee_button.click()
        time.sleep(10)
        print("date_expiration_annee_button clicked")

        # Insert the "cvv" input
        cvv_input = browser.find_element_by_xpath(
            "/html/body/div/table/tbody/tr/td/div[3]/table/tbody/tr/td/div/div/table/tbody/tr/td[2]"
            "/div[3]/form/table/tbody/tr[3]/td[2]/input"
        )
        cvv_input.send_keys(cvv)
        time.sleep(10)
        print("cvv_input inserted")

        # screenshot
        ob.full_Screenshot(browser, save_path=full_path_folder, image_name='Page_7.png')
        time.sleep(10)
        print("screenshot Page_7.png")

        """
        # Click on the "Valider" button
        valider_button = browser.find_element_by_xpath(
            "/html/body/div/table/tbody/tr/td/div[3]/table/tbody/tr/td/div/div/table/tbody/tr/td[2]/div[3]"
            "/form/div[2]/table/tbody/tr/td[1]/input"
        )
        valider_button.click()
        time.sleep(10)
        print('valider_button clicked')
        """


if __name__ == '__main__':
    unittest.main()
