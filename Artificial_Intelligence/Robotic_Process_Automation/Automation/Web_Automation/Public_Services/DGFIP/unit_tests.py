import unittest
import time
import warnings
from selenium import webdriver

annee = "3_Annee_2022"
mois = "6_Juin_Pour_Mai"
mois_cvae = "2_Acompte_de_juin_2022_1329_AC"
mois_is = '2_Acompte_Juin_2571_SD'


class UnitTestsWebAutomationDGFIP(unittest.TestCase):
    # ok
    def test_open_one_page(self):
        print("test_open_one_page_for_dsn_test")

        url = 'https://www.impots.gouv.fr/accueil'

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
        print('browser.get(url)')

        time.sleep(15)

    # ok
    def test_se_connecter(self):
        print("test_se_connecter")

        # Credentials
        email = ""
        password = ""

        url = 'https://www.impots.gouv.fr/accueil'

        time.sleep(5)

        warnings.filterwarnings(
            action="ignore",
            message="unclosed",
            category=ResourceWarning
        )

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
        print('browser.get(url)')

        time.sleep(15)

        # click on the button 'Votre espace professionnel'
        espace_professionnel_button = browser.find_element_by_xpath(
            '/html/body/div[1]/div[2]/header/div/div[1]/div[2]/div/ul/li[2]/a'
        )
        espace_professionnel_button.click()

        time.sleep(10)

        # Insert the "Adresse électronique" text input
        adresse_electronique_text_input = browser.find_element_by_xpath(
            '//*[@id="ident"]'
        )
        adresse_electronique_text_input.clear()
        adresse_electronique_text_input.send_keys(email)

        time.sleep(5)

        # Insert the "Password" text input
        password_text_input = browser.find_element_by_xpath(
            '//*[@id="mdp"]'
        )
        password_text_input.clear()
        password_text_input.send_keys(password)

        time.sleep(5)

        # Click on the button 'Connexion'
        connexion_button = browser.find_element_by_xpath(
            '//*[@id="valider"]'
        )
        connexion_button.click()

        time.sleep(10)

    # ok
    def test_declarer_tva_neant(self):
        print("test_declarer_tva_neant")

        # Credentials
        email = ""
        password = ""

        url = 'https://www.impots.gouv.fr/accueil'

        time.sleep(5)

        warnings.filterwarnings(
            action="ignore",
            message="unclosed",
            category=ResourceWarning
        )

        time.sleep(5)

        # with Firefox
        browser = webdriver.Firefox(
            executable_path='..\\..\\geckodriver.exe'
        )

        time.sleep(5)

        # maximize window
        browser.maximize_window()
        print("browser.maximize_window()")

        time.sleep(5)

        # open
        browser.get(url)
        print('browser.get(url)')

        time.sleep(15)

        # click on the button 'Votre espace professionnel'
        espace_professionnel_button = browser.find_element_by_xpath(
            '/html/body/div[1]/div[2]/header/div/div[1]/div[2]/div/ul/li[2]/a'
        )
        espace_professionnel_button.click()
        print("espace_professionnel_button.click()")

        time.sleep(10)

        # Insert the "Adresse électronique" text input
        adresse_electronique_text_input = browser.find_element_by_xpath(
            '//*[@id="ident"]'
        )
        adresse_electronique_text_input.clear()
        adresse_electronique_text_input.send_keys(email)
        print("adresse_electronique_text_input.send_keys(email)")

        time.sleep(5)

        # Insert the "Password" text input
        password_text_input = browser.find_element_by_xpath(
            '//*[@id="mdp"]'
        )
        password_text_input.clear()
        password_text_input.send_keys(password)
        print("password_text_input.send_keys(password)")

        time.sleep(5)

        # Click on the button 'Connexion'
        connexion_button = browser.find_element_by_xpath(
            '//*[@id="valider"]'
        )
        connexion_button.click()
        print("connexion_button.click()")

        time.sleep(10)

        # Save screenshot
        browser.save_screenshot(
            "A:\\1_Professionnel\\1_Holomorphe\\1_Administration\\2_Gestion_Declarations_Administratives"
            "\\1_Recurrentes\\1_DGFIP\\9_Declaration_TVA\\"
            + annee
            + "\\"
            + mois
            + "\\Page_1.png"
        )
        print("Save screenshot Page_1.png")

        time.sleep(5)

        # Click on the button 'TVA'
        tva_button = browser.find_element_by_xpath(
            '/html/body/div[2]/div[2]/table/tbody/tr/td[2]/div[2]/table/tbody/tr[5]/td[2]/div/div[3]/ul/li[1]/a'
        )
        tva_button.click()
        print("tva_button.click()")

        time.sleep(10)

        # Save screenshot
        browser.save_screenshot(
            "A:\\1_Professionnel\\1_Holomorphe\\1_Administration\\2_Gestion_Declarations_Administratives"
            "\\1_Recurrentes\\1_DGFIP\\9_Declaration_TVA\\"
            + annee
            + "\\"
            + mois
            + "\\Page_2.png"
        )
        print("Save screenshot Page_2.png")

        time.sleep(5)

        # Click on the button 'Declarer'
        declarer_button = browser.find_element_by_xpath(
            '/html/body/div[2]/div[2]/table/tbody/tr/td[2]/div[2]/form/table[2]/tbody/tr/td[2]/input'
        )
        declarer_button.click()
        print("declarer_button.click()")

        time.sleep(5)

        # Switch to the new window
        window_after = browser.window_handles[1]
        browser.switch_to.window(window_after)
        print("browser.switch_to.window(window_after)")

        time.sleep(5)

        # Save screenshot
        browser.save_screenshot(
            "A:\\1_Professionnel\\1_Holomorphe\\1_Administration\\2_Gestion_Declarations_Administratives"
            "\\1_Recurrentes\\1_DGFIP\\9_Declaration_TVA\\"
            + annee
            + "\\"
            + mois
            + "\\Page_3.png"
        )
        print("Save screenshot Page_3.png")

        time.sleep(5)

        # Click on the button 'Mois en cours'
        mois_en_cours_button = browser.find_element_by_xpath(
            '//*[@id="periode0"]'
        )
        mois_en_cours_button.click()
        print("mois_en_cours_button.click()")

        time.sleep(5)

        # Save screenshot
        browser.save_screenshot(
            "A:\\1_Professionnel\\1_Holomorphe\\1_Administration\\2_Gestion_Declarations_Administratives"
            "\\1_Recurrentes\\1_DGFIP\\9_Declaration_TVA\\"
            + annee
            + "\\"
            + mois
            + "\\Page_4.png"
        )
        print("Save screenshot Page_4.png")

        time.sleep(5)

    # ok
    def test_declarer_rcm_neant(self):
        print("test_declarer_rcm_neant")

        # Credentials
        email = ""
        password = ""

        url = 'https://www.impots.gouv.fr/accueil'

        time.sleep(5)

        warnings.filterwarnings(
            action="ignore",
            message="unclosed",
            category=ResourceWarning
        )

        time.sleep(5)

        # with Firefox
        browser = webdriver.Firefox(
            executable_path='..\\..\\geckodriver.exe'
        )

        time.sleep(5)

        # maximize window
        browser.maximize_window()
        print("browser.maximize_window()")

        time.sleep(5)

        # open
        browser.get(url)
        print('browser.get(url)')

        time.sleep(15)

        # click on the button 'Votre espace professionnel'
        espace_professionnel_button = browser.find_element_by_xpath(
            '/html/body/div[1]/div[2]/header/div/div[1]/div[2]/div/ul/li[2]/a'
        )
        espace_professionnel_button.click()
        print("espace_professionnel_button.click()")

        time.sleep(10)

        # Insert the "Adresse électronique" text input
        adresse_electronique_text_input = browser.find_element_by_xpath(
            '//*[@id="ident"]'
        )
        adresse_electronique_text_input.clear()
        adresse_electronique_text_input.send_keys(email)
        print("adresse_electronique_text_input.send_keys(email)")

        time.sleep(5)

        # Insert the "Password" text input
        password_text_input = browser.find_element_by_xpath(
            '//*[@id="mdp"]'
        )
        password_text_input.clear()
        password_text_input.send_keys(password)
        print("password_text_input.send_keys(password)")

        time.sleep(5)

        # Click on the button 'Connexion'
        connexion_button = browser.find_element_by_xpath(
            '//*[@id="valider"]'
        )
        connexion_button.click()
        print("connexion_button.click()")

        time.sleep(10)

        # Save screenshot
        browser.save_screenshot(
            "A:\\1_Professionnel\\1_Holomorphe\\1_Administration\\2_Gestion_Declarations_Administratives"
            "\\1_Recurrentes\\1_DGFIP\\7_Declaration_I_D_R__Revenus_Capitaux_Mobiliers\\"
            + annee
            + "\\"
            + mois
            + "\\Page_1.png"
        )
        print("Save screenshot Page_1.png")

        time.sleep(5)

        # Click on the button 'Revenus de capitaux mobiliers'
        rcm_button = browser.find_element_by_xpath(
            '/html/body/div[2]/div[2]/table/tbody/tr/td[2]/div[2]/table/tbody/tr[5]/td[2]/div/div[3]/ul/li[5]/a'
        )
        rcm_button.click()
        print("rcm_button.click()")

        time.sleep(5)

        # Save screenshot
        browser.save_screenshot(
            "A:\\1_Professionnel\\1_Holomorphe\\1_Administration\\2_Gestion_Declarations_Administratives"
            "\\1_Recurrentes\\1_DGFIP\\7_Declaration_I_D_R__Revenus_Capitaux_Mobiliers\\"
            + annee
            + "\\"
            + mois
            + "\\Page_2.png"
        )
        print("Save screenshot Page_2.png")

        time.sleep(5)

        # Click on the button 'Declarer'
        declarer_button = browser.find_element_by_xpath(
            '/html/body/div[2]/div[2]/table/tbody/tr/td[2]/div[2]/form/table[2]/tbody/tr/td[2]/input'
        )
        declarer_button.click()
        print("declarer_button.click()")

        time.sleep(5)

        # Switch to the new window
        window_after = browser.window_handles[1]
        browser.switch_to.window(window_after)
        print("browser.switch_to.window(window_after)")

        time.sleep(5)

        # Save screenshot
        browser.save_screenshot(
            "A:\\1_Professionnel\\1_Holomorphe\\1_Administration\\2_Gestion_Declarations_Administratives"
            "\\1_Recurrentes\\1_DGFIP\\7_Declaration_I_D_R__Revenus_Capitaux_Mobiliers\\"
            + annee
            + "\\"
            + mois
            + "\\Page_3.png"
        )
        print("Save screenshot Page_3.png")

        time.sleep(5)

        # Click on the button 'Mois en cours'
        mois_en_cours_button = browser.find_element_by_xpath(
            '/html/body/main/div/div[2]/div/section/div[3]/div/form/table/tbody/tr[2]/td[1]/a'
        )
        mois_en_cours_button.click()
        print("mois_en_cours_button.click()")

        time.sleep(5)

        # Save screenshot
        browser.save_screenshot(
            "A:\\1_Professionnel\\1_Holomorphe\\1_Administration\\2_Gestion_Declarations_Administratives"
            "\\1_Recurrentes\\1_DGFIP\\7_Declaration_I_D_R__Revenus_Capitaux_Mobiliers\\"
            + annee
            + "\\"
            + mois
            + "\\Page_4.png"
        )
        print("Save screenshot Page_4.png")

        time.sleep(5)

    # ok
    def test_declarer_taxe_salaire_neant(self):
        print("test_declarer_taxe_salaire_neant")

        # Credentials
        email = ""
        password = ""

        url = 'https://www.impots.gouv.fr/accueil'

        time.sleep(5)

        warnings.filterwarnings(
            action="ignore",
            message="unclosed",
            category=ResourceWarning
        )

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
        print('browser.get(url)')

        time.sleep(15)

        # click on the button 'Votre espace professionnel'
        espace_professionnel_button = browser.find_element_by_xpath(
            '/html/body/div[1]/div[2]/header/div/div[1]/div[2]/div/ul/li[2]/a'
        )
        espace_professionnel_button.click()
        print("espace_professionnel_button.click()")

        time.sleep(10)

        # Insert the "Adresse électronique" text input
        adresse_electronique_text_input = browser.find_element_by_xpath(
            '//*[@id="ident"]'
        )
        adresse_electronique_text_input.clear()
        adresse_electronique_text_input.send_keys(email)
        print("adresse_electronique_text_input.send_keys(email)")

        time.sleep(5)

        # Insert the "Password" text input
        password_text_input = browser.find_element_by_xpath(
            '//*[@id="mdp"]'
        )
        password_text_input.clear()
        password_text_input.send_keys(password)
        print("password_text_input.send_keys(password)")

        time.sleep(5)

        # Click on the button 'Connexion'
        connexion_button = browser.find_element_by_xpath(
            '//*[@id="valider"]'
        )
        connexion_button.click()
        print("connexion_button.click()")

        time.sleep(10)

        # Save screenshot
        browser.save_screenshot(
            "A:\\1_Professionnel\\1_Holomorphe\\1_Administration\\2_Gestion_Declarations_Administratives"
            "\\1_Recurrentes\\1_DGFIP\\12_Declaration_Taxes_Sur_Les_Salaires\\"
            + annee
            + "\\"
            + mois
            + "\\Page_1.png"
        )
        print("Save screenshot Page_1.png")

        time.sleep(5)

        # Click on the button 'Taxe sur les salaires'
        tsls_button = browser.find_element_by_xpath(
            '/html/body/div[2]/div[2]/table/tbody/tr/td[2]/div[2]/table/tbody/tr[5]/td[2]/div/div[3]/ul/li[3]/a'
        )
        tsls_button.click()
        print("tsls_button.click()")

        time.sleep(5)

        # Save screenshot
        browser.save_screenshot(
            "A:\\1_Professionnel\\1_Holomorphe\\1_Administration\\2_Gestion_Declarations_Administratives"
            "\\1_Recurrentes\\1_DGFIP\\12_Declaration_Taxes_Sur_Les_Salaires\\"
            + annee
            + "\\"
            + mois
            + "\\Page_2.png"
        )
        print("Save screenshot Page_2.png")

        time.sleep(5)

        # Click on the button 'Quitter'
        quitter_button = browser.find_element_by_xpath(
            '/html/body/div[2]/div[2]/table/tbody/tr/td[1]/table/tbody/tr[1]/td/div/div/ul/li[6]/a'
        )
        quitter_button.click()
        print("quitter_button.click()")

        time.sleep(5)

        # Browser quit
        browser.quit()
        print("browser.quit()")

        time.sleep(5)

    # ok
    def test_declarer_cvae(self):
        print("test_declarer_cvae")

        # Credentials
        email = ""
        password = ""

        url = 'https://www.impots.gouv.fr/accueil'

        time.sleep(5)

        warnings.filterwarnings(
            action="ignore",
            message="unclosed",
            category=ResourceWarning
        )

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
        print('browser.get(url)')

        time.sleep(15)

        # click on the button 'Votre espace professionnel'
        espace_professionnel_button = browser.find_element_by_xpath(
            '/html/body/div[1]/div[2]/header/div/div[1]/div[2]/div/ul/li[2]/a'
        )
        espace_professionnel_button.click()
        print('espace_professionnel_button.click()')
        time.sleep(10)

        # Insert the "Adresse électronique" text input
        adresse_electronique_text_input = browser.find_element_by_xpath(
            '//*[@id="ident"]'
        )
        adresse_electronique_text_input.clear()
        adresse_electronique_text_input.send_keys(email)
        print('adresse_electronique_text_input.send_keys(email)')
        time.sleep(5)

        # Insert the "Password" text input
        password_text_input = browser.find_element_by_xpath(
            '//*[@id="mdp"]'
        )
        password_text_input.clear()
        password_text_input.send_keys(password)
        print('password_text_input.send_keys(password)')
        time.sleep(5)

        # Click on the button 'Connexion'
        connexion_button = browser.find_element_by_xpath(
            '//*[@id="valider"]'
        )
        connexion_button.click()
        print('connexion_button.click()')
        time.sleep(10)

        # Save screenshot
        browser.save_screenshot(
            "A:\\1_Professionnel\\1_Holomorphe\\1_Administration\\2_Gestion_Declarations_Administratives"
            "\\1_Recurrentes\\1_DGFIP\\8_Declaration_C_E_T\\2_C_V_A_E\\"
            + annee
            + "\\"
            + mois_cvae
            + "\\Page_1.png"
        )
        print("Save screenshot Page_1.png")
        time.sleep(5)

        # Click on the button 'CVAE'
        cvae_button = browser.find_element_by_xpath(
            '/html/body/div[2]/div[2]/table/tbody/tr/td[2]/div[2]/table/tbody/tr[5]/td[2]/div/div[3]/ul/li[4]/a'
        )
        cvae_button.click()
        print('cvae_button.click()')
        time.sleep(10)

        # Save screenshot
        browser.save_screenshot(
            "A:\\1_Professionnel\\1_Holomorphe\\1_Administration\\2_Gestion_Declarations_Administratives"
            "\\1_Recurrentes\\1_DGFIP\\8_Declaration_C_E_T\\2_C_V_A_E\\"
            + annee
            + "\\"
            + mois_cvae
            + "\\Page_2.png"
        )
        print("Save screenshot Page_2.png")
        time.sleep(5)

        # Click on the button 'Déclarer'
        declarer_button = browser.find_element_by_xpath(
            '/html/body/div[2]/div[2]/table/tbody/tr/td[2]/div[2]/form/table[2]/tbody/tr/td[2]/input'
        )
        declarer_button.click()
        print('declarer_button.click()')
        time.sleep(10)

        # Save screenshot
        browser.save_screenshot(
            "A:\\1_Professionnel\\1_Holomorphe\\1_Administration\\2_Gestion_Declarations_Administratives"
            "\\1_Recurrentes\\1_DGFIP\\8_Declaration_C_E_T\\2_C_V_A_E\\"
            + annee
            + "\\"
            + mois_cvae
            + "\\Page_3.png"
        )
        print("Save screenshot Page_3.png")
        time.sleep(5)

    # ok
    def test_declarer_is(self):
        print("test_declarer_is")

        # Credentials
        email = ""
        password = ""

        url = 'https://www.impots.gouv.fr/accueil'

        time.sleep(5)

        warnings.filterwarnings(
            action="ignore",
            message="unclosed",
            category=ResourceWarning
        )

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
        print('browser.get(url)')

        time.sleep(15)

        # click on the button 'Votre espace professionnel'
        espace_professionnel_button = browser.find_element_by_xpath(
            '/html/body/div[1]/div[2]/header/div/div[1]/div[2]/div/ul/li[2]/a'
        )
        espace_professionnel_button.click()
        print('espace_professionnel_button.click()')
        time.sleep(10)

        # Insert the "Adresse électronique" text input
        adresse_electronique_text_input = browser.find_element_by_xpath(
            '//*[@id="ident"]'
        )
        adresse_electronique_text_input.clear()
        adresse_electronique_text_input.send_keys(email)
        print('adresse_electronique_text_input.send_keys(email)')
        time.sleep(5)

        # Insert the "Password" text input
        password_text_input = browser.find_element_by_xpath(
            '//*[@id="mdp"]'
        )
        password_text_input.clear()
        password_text_input.send_keys(password)
        print('password_text_input.send_keys(password)')
        time.sleep(5)

        # Click on the button 'Connexion'
        connexion_button = browser.find_element_by_xpath(
            '//*[@id="valider"]'
        )
        connexion_button.click()
        print('connexion_button.click()')
        time.sleep(10)

        # Save screenshot
        browser.save_screenshot(
            "A:\\1_Professionnel\\1_Holomorphe\\1_Administration\\2_Gestion_Declarations_Administratives"
            "\\1_Recurrentes\\1_DGFIP\\2_Declaration_Impot_Societes\\"
            + annee
            + "\\"
            + mois_is
            + "\\Page_1.png"
        )
        print("Save screenshot Page_1.png")
        time.sleep(5)

        # Click on the button 'Impots sur les societes'
        is_button = browser.find_element_by_xpath(
            '/html/body/div[2]/div[2]/table/tbody/tr/td[2]/div[2]/table/tbody/tr[5]/td[2]/div/div[3]/ul/li[2]/a'
        )
        is_button.click()
        print('is_button.click()')
        time.sleep(10)

        # Save screenshot
        browser.save_screenshot(
            "A:\\1_Professionnel\\1_Holomorphe\\1_Administration\\2_Gestion_Declarations_Administratives"
            "\\1_Recurrentes\\1_DGFIP\\2_Declaration_Impot_Societes\\"
            + annee
            + "\\"
            + mois_is
            + "\\Page_2.png"
        )
        print("Save screenshot Page_2.png")
        time.sleep(5)

        # Click on the button 'Déclarer'
        declarer_button = browser.find_element_by_xpath(
            '/html/body/div[2]/div[2]/table/tbody/tr/td[2]/div[2]/form/table[2]/tbody/tr/td[2]/input'
        )
        declarer_button.click()
        print('declarer_button.click()')
        time.sleep(10)

        # Save screenshot
        browser.save_screenshot(
            "A:\\1_Professionnel\\1_Holomorphe\\1_Administration\\2_Gestion_Declarations_Administratives"
            "\\1_Recurrentes\\1_DGFIP\\2_Declaration_Impot_Societes\\"
            + annee
            + "\\"
            + mois_is
            + "\\Page_3.png"
        )
        print("Save screenshot Page_3.png")
        time.sleep(5)

    #
    def test_declarer_resultats_rsi(self):
        print("test_declarer_resultats_rsi")

        # Folder
        folder = "A:\\1_Professionnel\\1_Holomorphe\\1_Administration\\2_Gestion_Declarations_Administratives" \
                 "\\1_Recurrentes\\1_DGFIP\\3_Declaration_Liasse_Fiscale\\2_Regime_Simplifie\\1_Annee_2021_[DGFIP]"

        # Credentials
        email = ""
        password = ""

        url = 'https://www.impots.gouv.fr/accueil'

        time.sleep(5)

        warnings.filterwarnings(
            action="ignore",
            message="unclosed",
            category=ResourceWarning
        )

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
        print('browser.get(url)')

        time.sleep(15)

        # click on the button 'Votre espace professionnel'
        espace_professionnel_button = browser.find_element_by_xpath(
            '/html/body/div[1]/div[2]/header/div/div[1]/div[2]/div/ul/li[2]/a'
        )
        espace_professionnel_button.click()

        time.sleep(10)

        # Insert the "Adresse électronique" text input
        adresse_electronique_text_input = browser.find_element_by_xpath(
            '//*[@id="ident"]'
        )
        adresse_electronique_text_input.clear()
        adresse_electronique_text_input.send_keys(email)

        time.sleep(5)

        # Insert the "Password" text input
        password_text_input = browser.find_element_by_xpath(
            '//*[@id="mdp"]'
        )
        password_text_input.clear()
        password_text_input.send_keys(password)

        time.sleep(5)

        # Click on the button 'Connexion'
        connexion_button = browser.find_element_by_xpath(
            '//*[@id="valider"]'
        )
        connexion_button.click()

        time.sleep(10)

        # Screenshot
        n_page = 1
        browser.save_screenshot(folder + "Page_" + str(n_page) + ".png")
        n_page += 1

        time.sleep(5)

        # Click on the 'Resultat' button
        resultat_button = browser.find_element_by_xpath(
            "/html/body/div[2]/div[2]/table/tbody/tr/td[2]/div[2]/table/tbody/tr[5]/td[2]/div/div[3]/ul/li[6]/a"
        )
        resultat_button.click()

        time.sleep(5)

        # Screenshot
        browser.save_screenshot(folder + "Page_" + str(n_page) + ".png")
        n_page += 1

        # Click on the 'Declarer' button
        declarer_button = browser.find_element_by_xpath(
            "/html/body/div[2]/div[2]/table/tbody/tr/td[2]/div[2]/form/table[2]/tbody/tr/td[2]/input"
        )
        declarer_button.click()

        time.sleep(10)

        # Switch to the second window
        browser.switch_to.window(browser.window_handles[1])

        time.sleep(5)

        # Screenshot
        browser.save_screenshot(folder + "Page_" + str(n_page) + ".png")
        n_page += 1

        time.sleep(5)

        # Click on the 'Annee' button
        anne_button = browser.find_element_by_xpath(
            '//*[@id="periode1"]'
        )
        anne_button.click()

        time.sleep(10)


if __name__ == '__main__':
    unittest.main()
