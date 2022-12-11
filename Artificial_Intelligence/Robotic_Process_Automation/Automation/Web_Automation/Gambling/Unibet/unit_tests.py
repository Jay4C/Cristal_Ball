import subprocess
import unittest
import time
import warnings
from selenium import webdriver
from Artificial_Intelligence.Machine_Learning.Supervised_Learning.PMU.pmu import PMUFinal


# unibet race url
global_url = ""


class Unit_Tests_Web_Automation_Unibet(unittest.TestCase):
    #
    def test_se_connecter(self):
        print("test_se_connecter")

        username = ""

        password = ""

        date_de_naissance = ""

        time.sleep(5)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(5)

        # with Firefox
        browser = webdriver.Firefox(executable_path='A:\\GitHub\\Cristal_Ball\\geckodriver.exe')

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get('https://www.unibet.fr/pari-sportif-poker')

        time.sleep(15)

        parametrer_button = browser.find_element_by_xpath(
            "//a[@class='ui-button ui-large ui-light ui-collapsible ui-collapsed params-button']"
        )
        parametrer_button.click()

        time.sleep(5)

        tout_refuser_button = browser.find_element_by_xpath(
            "//button[@class='ui-button ui-large ui-light']"
        )
        tout_refuser_button.click()

        time.sleep(10)

        email_input = browser.find_element_by_xpath(
            "//input[@name='username']"
        )
        email_input.clear()
        email_input.send_keys(username)

        time.sleep(5)

        password_input = browser.find_element_by_xpath(
            "//input[@name='password']"
        )
        password_input.clear()
        password_input.send_keys(password)

        time.sleep(5)

        date_de_naissance_input = browser.find_element_by_xpath(
            "//input[@id='form_login_input_id']"
        )
        date_de_naissance_input.clear()
        date_de_naissance_input.send_keys(date_de_naissance)

        time.sleep(5)

        connexion_button = browser.find_element_by_xpath(
            "//input[@value='Connexion'][@class='ui-button button-login']"
        )
        connexion_button.click()

        time.sleep(5)

    # simple gagnant :
    def test_selectionner_un_cheval_pour_un_simple_gagnant(self):
        print('test_selectionner_un_cheval_pour_un_simple_gagnant')

        url = global_url

        numero_cheval = 7

        time.sleep(1)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(1)

        # with Firefox
        browser = webdriver.Firefox(executable_path='A:\\GitHub\\Cristal_Ball\\geckodriver.exe')

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get(url)

        time.sleep(15)

        parametrer_button = browser.find_element_by_xpath(
            "//a[@class='ui-button ui-large ui-light ui-collapsible ui-collapsed params-button']"
        )
        parametrer_button.click()

        time.sleep(5)

        tout_refuser_button = browser.find_element_by_xpath(
            "//button[@class='ui-button ui-large ui-light']"
        )
        tout_refuser_button.click()

        time.sleep(10)

        simple_button = browser.find_element_by_xpath(
            "//a[@data-turf-category='SIMPLE']"
        )
        simple_button.click()

        time.sleep(5)

        runner_gagnant = browser.find_element_by_xpath(
            "/html/body/div/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]/div/div[3]/ul[2]/li/div"
            "/div[2]/ul/li[" + str(numero_cheval + 1) + "]/div/div[13]/i[1]"
        )
        runner_gagnant.click()

        time.sleep(5)

    def test_miser_un_simple_gagnant(self):
        print('test_miser_un_simple_gagnant')

        url = global_url

        numero_cheval = 7

        mise = 1

        time.sleep(1)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(1)

        # with Firefox
        browser = webdriver.Firefox(executable_path='A:\\GitHub\\Cristal_Ball\\geckodriver.exe')

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get(url)

        time.sleep(15)

        parametrer_button = browser.find_element_by_xpath(
            "//a[@class='ui-button ui-large ui-light ui-collapsible ui-collapsed params-button']"
        )
        parametrer_button.click()

        time.sleep(5)

        tout_refuser_button = browser.find_element_by_xpath(
            "//button[@class='ui-button ui-large ui-light']"
        )
        tout_refuser_button.click()

        time.sleep(10)

        simple_button = browser.find_element_by_xpath(
            "//a[@data-turf-category='SIMPLE']"
        )
        simple_button.click()

        time.sleep(5)

        runner_gagnant = browser.find_element_by_xpath(
            "/html/body/div/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]/div/div[3]/ul[2]/li/div"
            "/div[2]/ul/li[" + str(numero_cheval + 1) + "]/div/div[13]/i[1]"
        )
        runner_gagnant.click()

        time.sleep(5)

        mise_input = browser.find_element_by_xpath("//input[@name='stake']")
        mise_input.clear()
        mise_input.send_keys(str(mise))

        time.sleep(5)

        parier_button = browser.find_element_by_xpath(
            "//a[@id='turf_betslip_place']"
        )
        parier_button.click()

        time.sleep(5)

        email_input = browser.find_element_by_xpath(
            "//input[@id='login-username']"
        )
        email_input.clear()
        email_input.send_keys(".@outlook.fr")

        time.sleep(5)

        password_input = browser.find_element_by_xpath(
            "//input[@id='login-password']"
        )
        password_input.clear()
        password_input.send_keys("")

        time.sleep(5)

        date_de_naissance_input = browser.find_element_by_xpath(
            "//input[@id='dob_input']"
        )
        date_de_naissance_input.clear()
        date_de_naissance_input.send_keys("")

        time.sleep(5)

        me_connecter_button = browser.find_element_by_xpath(
            "//input[@value='Me connecter'][@class='ui-button button-login']"
        )
        me_connecter_button.click()

        time.sleep(5)

        parier_button = browser.find_element_by_xpath(
            "//a[@id='turf_betslip_place']"
        )
        parier_button.click()

        time.sleep(5)

        """
        confirmer_button = browser.find_element_by_xpath(
            "//a[@id='turf_betslip_confirm']"
        )
        confirmer_button.click()

        time.sleep(5)
        """

    # simple place :
    def test_selectionner_un_cheval_pour_un_simple_place(self):
        print('test_selectionner_un_cheval_pour_un_simple_gagnant')

        url = global_url

        numero_cheval = 7

        time.sleep(1)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(1)

        # with Firefox
        browser = webdriver.Firefox(executable_path='A:\\GitHub\\Cristal_Ball\\geckodriver.exe')

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get(url)

        time.sleep(15)

        parametrer_button = browser.find_element_by_xpath(
            "//a[@class='ui-button ui-large ui-light ui-collapsible ui-collapsed params-button']"
        )
        parametrer_button.click()

        time.sleep(5)

        tout_refuser_button = browser.find_element_by_xpath(
            "//button[@class='ui-button ui-large ui-light']"
        )
        tout_refuser_button.click()

        time.sleep(10)

        simple_button = browser.find_element_by_xpath(
            "//a[@data-turf-category='SIMPLE']"
        )
        simple_button.click()

        time.sleep(5)

        runner_gagnant = browser.find_element_by_xpath(
            "/html/body/div/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]/div/div[3]/ul[2]"
            "/li/div/div[2]/ul/li[" + str(numero_cheval + 1) + "]/div/div[13]/i[2]"
        )
        runner_gagnant.click()

        time.sleep(5)

    #
    def test_miser_un_simple_place(self):
        print('test_miser_un_simple_place')

        url = global_url

        numero_cheval = 7

        mise = 1

        time.sleep(1)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(1)

        # with Firefox
        browser = webdriver.Firefox(executable_path='A:\\GitHub\\Cristal_Ball\\geckodriver.exe')

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get(url)

        time.sleep(15)

        parametrer_button = browser.find_element_by_xpath(
            "//a[@class='ui-button ui-large ui-light ui-collapsible ui-collapsed params-button']"
        )
        parametrer_button.click()

        time.sleep(5)

        tout_refuser_button = browser.find_element_by_xpath(
            "//button[@class='ui-button ui-large ui-light']"
        )
        tout_refuser_button.click()

        time.sleep(10)

        simple_button = browser.find_element_by_xpath(
            "//a[@data-turf-category='SIMPLE']"
        )
        simple_button.click()

        time.sleep(5)

        runner_gagnant = browser.find_element_by_xpath(
            "/html/body/div/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]/div/div[3]/ul[2]"
            "/li/div/div[2]/ul/li[" + str(numero_cheval + 1) + "]/div/div[13]/i[2]"
        )
        runner_gagnant.click()

        time.sleep(5)

        mise_input = browser.find_element_by_xpath("//input[@name='stake']")
        mise_input.clear()
        mise_input.send_keys(str(mise))

        time.sleep(5)

        parier_button = browser.find_element_by_xpath(
            "//a[@id='turf_betslip_place']"
        )
        parier_button.click()

        time.sleep(5)

        email_input = browser.find_element_by_xpath(
            "//input[@id='login-username']"
        )
        email_input.clear()
        email_input.send_keys(".@outlook.fr")

        time.sleep(5)

        password_input = browser.find_element_by_xpath(
            "//input[@id='login-password']"
        )
        password_input.clear()
        password_input.send_keys("")

        time.sleep(5)

        date_de_naissance_input = browser.find_element_by_xpath(
            "//input[@id='dob_input']"
        )
        date_de_naissance_input.clear()
        date_de_naissance_input.send_keys("")

        time.sleep(5)

        me_connecter_button = browser.find_element_by_xpath(
            "//input[@value='Me connecter'][@class='ui-button button-login']"
        )
        me_connecter_button.click()

        time.sleep(5)

        parier_button = browser.find_element_by_xpath(
            "//a[@id='turf_betslip_place']"
        )
        parier_button.click()

        time.sleep(5)

        """
        confirmer_button = browser.find_element_by_xpath(
            "//a[@id='turf_betslip_confirm']"
        )
        confirmer_button.click()

        time.sleep(5)
        """

    # jumelé desordre gagnant :
    def test_selectionner_deux_chevaux_pour_un_jumele_desordre_gagnant(self):
        print('test_selectionner_deux_chevaux_pour_un_jumele_desordre_gagnant')

        url = global_url

        numero_cheval_1 = 5

        numero_cheval_2 = 7

        time.sleep(1)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(1)

        # with Firefox
        browser = webdriver.Firefox(executable_path='A:\\GitHub\\Cristal_Ball\\geckodriver.exe')

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get(url)

        time.sleep(15)

        parametrer_button = browser.find_element_by_xpath(
            "//a[@class='ui-button ui-large ui-light ui-collapsible ui-collapsed params-button']"
        )
        parametrer_button.click()

        time.sleep(5)

        tout_refuser_button = browser.find_element_by_xpath(
            "//button[@class='ui-button ui-large ui-light']"
        )
        tout_refuser_button.click()

        time.sleep(10)

        jumele_button = browser.find_element_by_xpath(
            "//a[@data-turf-category='JUMELE']"
        )
        jumele_button.click()

        time.sleep(5)

        gagnant_button = browser.find_element_by_xpath(
            "/html/body/div/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]/div/div[3]"
            "/div[1]/span[2]/a[1]"
        )
        gagnant_button.click()

        time.sleep(5)

        runner_gagnant_1 = browser.find_element_by_xpath(
            "/html/body/div/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]/div/div[4]/ul[2]"
            "/li/div/div[2]/ul/li[" + str(numero_cheval_1 + 1) + "]/div/div[11]/i"
        )
        runner_gagnant_1.click()

        time.sleep(5)

        runner_gagnant_2 = browser.find_element_by_xpath(
            "/html/body/div/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]/div/div[4]/ul[2]"
            "/li/div/div[2]/ul/li[" + str(numero_cheval_2 + 1) + "]/div/div[11]/i"
        )
        runner_gagnant_2.click()

        time.sleep(5)

    #
    def test_miser_un_jumele_desordre_gagnant(self):
        print('test_miser_un_jumele_desordre_gagnant')

        url = global_url

        numero_cheval_1 = 5

        numero_cheval_2 = 7

        mise = 1

        time.sleep(1)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(1)

        # with Firefox
        browser = webdriver.Firefox(executable_path='A:\\GitHub\\Cristal_Ball\\geckodriver.exe')

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get(url)

        time.sleep(15)

        parametrer_button = browser.find_element_by_xpath(
            "//a[@class='ui-button ui-large ui-light ui-collapsible ui-collapsed params-button']"
        )
        parametrer_button.click()

        time.sleep(5)

        tout_refuser_button = browser.find_element_by_xpath(
            "//button[@class='ui-button ui-large ui-light']"
        )
        tout_refuser_button.click()

        time.sleep(10)

        jumele_button = browser.find_element_by_xpath(
            "//a[@data-turf-category='JUMELE']"
        )
        jumele_button.click()

        time.sleep(5)

        gagnant_button = browser.find_element_by_xpath(
            "/html/body/div/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]/div/div[3]"
            "/div[1]/span[2]/a[1]"
        )
        gagnant_button.click()

        time.sleep(5)

        runner_gagnant_1 = browser.find_element_by_xpath(
            "/html/body/div/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]/div/div[4]/ul[2]"
            "/li/div/div[2]/ul/li[" + str(numero_cheval_1 + 1) + "]/div/div[11]/i"
        )
        runner_gagnant_1.click()

        time.sleep(5)

        runner_gagnant_2 = browser.find_element_by_xpath(
            "/html/body/div/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]/div/div[4]/ul[2]"
            "/li/div/div[2]/ul/li[" + str(numero_cheval_2 + 1) + "]/div/div[11]/i"
        )
        runner_gagnant_2.click()

        time.sleep(5)

        mise_input = browser.find_element_by_xpath("//input[@name='stake']")
        mise_input.clear()
        mise_input.send_keys(str(mise))

        time.sleep(5)

        parier_button = browser.find_element_by_xpath(
            "//a[@id='turf_betslip_place']"
        )
        parier_button.click()

        time.sleep(5)

        email_input = browser.find_element_by_xpath(
            "//input[@id='login-username']"
        )
        email_input.clear()
        email_input.send_keys(".@outlook.fr")

        time.sleep(5)

        password_input = browser.find_element_by_xpath(
            "//input[@id='login-password']"
        )
        password_input.clear()
        password_input.send_keys("")

        time.sleep(5)

        date_de_naissance_input = browser.find_element_by_xpath(
            "//input[@id='dob_input']"
        )
        date_de_naissance_input.clear()
        date_de_naissance_input.send_keys("")

        time.sleep(5)

        me_connecter_button = browser.find_element_by_xpath(
            "//input[@value='Me connecter'][@class='ui-button button-login']"
        )
        me_connecter_button.click()

        time.sleep(5)

        parier_button = browser.find_element_by_xpath(
            "//a[@id='turf_betslip_place']"
        )
        parier_button.click()

        time.sleep(5)

        """
        confirmer_button = browser.find_element_by_xpath(
            "//a[@id='turf_betslip_confirm']"
        )
        confirmer_button.click()

        time.sleep(5)
        """

    # jumele ordre :
    def test_selectionner_deux_chevaux_pour_un_jumele_ordre(self):
        print('test_selectionner_deux_chevaux_pour_un_jumele_ordre')

        url = global_url

        numero_cheval_1 = 1

        numero_cheval_2 = 3

        time.sleep(1)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(1)

        # with Firefox
        browser = webdriver.Firefox(executable_path='A:\\GitHub\\Cristal_Ball\\geckodriver.exe')

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get(url)

        time.sleep(15)

        parametrer_button = browser.find_element_by_xpath(
            "//a[@class='ui-button ui-large ui-light ui-collapsible ui-collapsed params-button']"
        )
        parametrer_button.click()

        time.sleep(5)

        tout_refuser_button = browser.find_element_by_xpath(
            "//button[@class='ui-button ui-large ui-light']"
        )
        tout_refuser_button.click()

        time.sleep(10)

        jumele_ordre_button = browser.find_element_by_xpath(
            "//a[@data-turf-category='JUMELE_ORDRE']"
        )
        jumele_ordre_button.click()

        time.sleep(5)

        runner_gagnant_1 = browser.find_element_by_xpath(
            "/html/body/div/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]/div/div[4]/ul[2]"
            "/li/div/div[2]/ul/li[" + str(numero_cheval_1 + 1) + "]/div/div[10]/i"
        )
        runner_gagnant_1.click()

        time.sleep(5)

        runner_gagnant_2 = browser.find_element_by_xpath(
            "/html/body/div/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]/div/div[4]/ul[2]"
            "/li/div/div[2]/ul/li[" + str(numero_cheval_2 + 1) + "]/div/div[10]/i"
        )
        runner_gagnant_2.click()

        time.sleep(5)

    #
    def test_miser_un_jumele_ordre(self):
        print('test_miser_un_jumele_ordre')

        url = global_url

        numero_cheval_1 = 1

        numero_cheval_2 = 3

        mise = 1

        time.sleep(1)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(1)

        # with Firefox
        browser = webdriver.Firefox(executable_path='A:\\GitHub\\Cristal_Ball\\geckodriver.exe')

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get(url)

        time.sleep(15)

        parametrer_button = browser.find_element_by_xpath(
            "//a[@class='ui-button ui-large ui-light ui-collapsible ui-collapsed params-button']"
        )
        parametrer_button.click()

        time.sleep(5)

        tout_refuser_button = browser.find_element_by_xpath(
            "//button[@class='ui-button ui-large ui-light']"
        )
        tout_refuser_button.click()

        time.sleep(10)

        jumele_ordre_button = browser.find_element_by_xpath(
            "//a[@data-turf-category='JUMELE_ORDRE']"
        )
        jumele_ordre_button.click()

        time.sleep(5)

        runner_gagnant_1 = browser.find_element_by_xpath(
            "/html/body/div/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]/div/div[4]/ul[2]"
            "/li/div/div[2]/ul/li[" + str(numero_cheval_1 + 1) + "]/div/div[10]/i"
        )
        runner_gagnant_1.click()

        time.sleep(5)

        runner_gagnant_2 = browser.find_element_by_xpath(
            "/html/body/div/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]/div/div[4]/ul[2]"
            "/li/div/div[2]/ul/li[" + str(numero_cheval_2 + 1) + "]/div/div[10]/i"
        )
        runner_gagnant_2.click()

        time.sleep(5)

        mise_input = browser.find_element_by_xpath("//input[@name='stake']")
        mise_input.clear()
        mise_input.send_keys(str(mise))

        time.sleep(5)

        parier_button = browser.find_element_by_xpath(
            "//a[@id='turf_betslip_place']"
        )
        parier_button.click()

        time.sleep(5)

        email_input = browser.find_element_by_xpath(
            "//input[@id='login-username']"
        )
        email_input.clear()
        email_input.send_keys(".@outlook.fr")

        time.sleep(5)

        password_input = browser.find_element_by_xpath(
            "//input[@id='login-password']"
        )
        password_input.clear()
        password_input.send_keys("")

        time.sleep(5)

        date_de_naissance_input = browser.find_element_by_xpath(
            "//input[@id='dob_input']"
        )
        date_de_naissance_input.clear()
        date_de_naissance_input.send_keys("")

        time.sleep(5)

        me_connecter_button = browser.find_element_by_xpath(
            "//input[@value='Me connecter'][@class='ui-button button-login']"
        )
        me_connecter_button.click()

        time.sleep(5)

        parier_button = browser.find_element_by_xpath(
            "//a[@id='turf_betslip_place']"
        )
        parier_button.click()

        time.sleep(5)

        """
        confirmer_button = browser.find_element_by_xpath(
            "//a[@id='turf_betslip_confirm']"
        )
        confirmer_button.click()

        time.sleep(5)
        """

    # trio :
    def test_selectionner_trois_chevaux_pour_un_trio_desordre(self):
        print('test_selectionner_trois_chevaux_pour_un_trio_desordre')

        url = global_url

        numero_cheval_1 = 1

        numero_cheval_2 = 3

        numero_cheval_3 = 7

        time.sleep(1)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(1)

        # with Firefox
        browser = webdriver.Firefox(executable_path='A:\\GitHub\\Cristal_Ball\\geckodriver.exe')

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get(url)

        time.sleep(15)

        parametrer_button = browser.find_element_by_xpath(
            "//a[@class='ui-button ui-large ui-light ui-collapsible ui-collapsed params-button']"
        )
        parametrer_button.click()

        time.sleep(5)

        tout_refuser_button = browser.find_element_by_xpath(
            "//button[@class='ui-button ui-large ui-light']"
        )
        tout_refuser_button.click()

        time.sleep(10)

        trio_button = browser.find_element_by_xpath(
            "//a[@data-turf-category='TRIO']"
        )
        trio_button.click()

        time.sleep(5)

        runner_gagnant_1 = browser.find_element_by_xpath(
            "/html/body/div/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]/div/div[4]"
            "/ul[2]/li/div/div[2]/ul/li[" + str(numero_cheval_1 + 1) + "]/div/div[10]/i"
        )
        runner_gagnant_1.click()

        time.sleep(5)

        runner_gagnant_2= browser.find_element_by_xpath(
            "/html/body/div/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]/div/div[4]/ul[2]"
            "/li/div/div[2]/ul/li[" + str(numero_cheval_2 + 1) + "]/div/div[10]/i"
        )
        runner_gagnant_2.click()

        time.sleep(5)

        runner_gagnant_3 = browser.find_element_by_xpath(
            "/html/body/div/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]/div/div[4]/ul[2]"
            "/li/div/div[2]/ul/li[" + str(numero_cheval_3 + 1) + "]/div/div[10]/i"
        )
        runner_gagnant_3.click()

        time.sleep(5)

    #
    def test_miser_un_trio_desordre(self):
        print('test_miser_un_trio_desordre')

        url = global_url

        numero_cheval_1 = 3

        numero_cheval_2 = 2

        numero_cheval_3 = 1

        mise = 1

        time.sleep(1)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(1)

        # with Firefox
        browser = webdriver.Firefox(executable_path='A:\\GitHub\\Cristal_Ball\\geckodriver.exe')

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get(url)

        time.sleep(15)

        parametrer_button = browser.find_element_by_xpath(
            "//a[@class='ui-button ui-large ui-light ui-collapsible ui-collapsed params-button']"
        )
        parametrer_button.click()

        time.sleep(5)

        tout_refuser_button = browser.find_element_by_xpath(
            "//button[@class='ui-button ui-large ui-light']"
        )
        tout_refuser_button.click()

        time.sleep(10)

        trio_button = browser.find_element_by_xpath(
            "//a[@data-turf-category='TRIO']"
        )
        trio_button.click()

        time.sleep(5)

        runner_gagnant_1 = browser.find_element_by_xpath(
            "/html/body/div/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]/div/div[4]/ul[2]"
            "/li/div/div[2]/ul/li[" + str(numero_cheval_1 + 1) + "]/div/div[10]/i"
        )
        runner_gagnant_1.click()

        time.sleep(5)

        runner_gagnant_2 = browser.find_element_by_xpath(
            "/html/body/div/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]/div/div[4]/ul[2]"
            "/li/div/div[2]/ul/li[" + str(numero_cheval_2 + 1) + "]/div/div[10]/i"
        )
        runner_gagnant_2.click()

        time.sleep(5)

        runner_gagnant_3 = browser.find_element_by_xpath(
            "/html/body/div/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]/div/div[4]/ul[2]"
            "/li/div/div[2]/ul/li[" + str(numero_cheval_3 + 1) + "]/div/div[10]/i"
        )
        runner_gagnant_3.click()

        time.sleep(5)

        mise_input = browser.find_element_by_xpath("//input[@name='stake']")
        mise_input.clear()
        mise_input.send_keys(str(mise))

        time.sleep(5)

        parier_button = browser.find_element_by_xpath(
            "//a[@id='turf_betslip_place']"
        )
        parier_button.click()

        time.sleep(5)

        email_input = browser.find_element_by_xpath(
            "//input[@id='login-username']"
        )
        email_input.clear()
        email_input.send_keys(".@outlook.fr")

        time.sleep(5)

        password_input = browser.find_element_by_xpath(
            "//input[@id='login-password']"
        )
        password_input.clear()
        password_input.send_keys("")

        time.sleep(5)

        date_de_naissance_input = browser.find_element_by_xpath(
            "//input[@id='dob_input']"
        )
        date_de_naissance_input.clear()
        date_de_naissance_input.send_keys("")

        time.sleep(5)

        me_connecter_button = browser.find_element_by_xpath(
            "//input[@value='Me connecter'][@class='ui-button button-login']"
        )
        me_connecter_button.click()

        time.sleep(5)

        parier_button = browser.find_element_by_xpath(
            "//a[@id='turf_betslip_place']"
        )
        parier_button.click()

        time.sleep(5)

        """
        confirmer_button = browser.find_element_by_xpath(
            "//a[@id='turf_betslip_confirm']"
        )
        confirmer_button.click()

        time.sleep(5)
        """

    # trio ordre :
    def test_selectionner_trois_chevaux_pour_un_trio_ordre(self):
        print('test_selectionner_trois_chevaux_pour_un_trio_ordre')

        url = global_url

        numero_cheval_1 = 1

        numero_cheval_2 = 3

        numero_cheval_3 = 7

        time.sleep(1)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(1)

        # with Firefox
        browser = webdriver.Firefox(executable_path='A:\\GitHub\\Cristal_Ball\\geckodriver.exe')

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get(url)

        time.sleep(15)

        parametrer_button = browser.find_element_by_xpath(
            "//a[@class='ui-button ui-large ui-light ui-collapsible ui-collapsed params-button']"
        )
        parametrer_button.click()

        time.sleep(5)

        tout_refuser_button = browser.find_element_by_xpath(
            "//button[@class='ui-button ui-large ui-light']"
        )
        tout_refuser_button.click()

        time.sleep(10)

        trio_ordre_button = browser.find_element_by_xpath(
            "//a[@data-turf-category='TRIO_ORDRE']"
        )
        trio_ordre_button.click()

        time.sleep(5)

        runner_gagnant_1 = browser.find_element_by_xpath(
            "/html/body/div/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]/div/div[4]/ul[2]"
            "/li/div/div[2]/ul/li[" + str(numero_cheval_1 + 1) + "]/div/div[10]/i"
        )
        runner_gagnant_1.click()

        time.sleep(5)

        runner_gagnant_2 = browser.find_element_by_xpath(
            "/html/body/div/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]/div/div[4]/ul[2]"
            "/li/div/div[2]/ul/li[" + str(numero_cheval_2 + 1) + "]/div/div[10]/i"
        )
        runner_gagnant_2.click()

        time.sleep(5)

        runner_gagnant_3 = browser.find_element_by_xpath(
            "/html/body/div/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]/div/div[4]/ul[2]"
            "/li/div/div[2]/ul/li[" + str(numero_cheval_3 + 1) + "]/div/div[10]/i"
        )
        runner_gagnant_3.click()

        time.sleep(5)

    #
    def test_miser_un_trio_ordre(self):
        print('test_miser_un_trio_ordre')

        url = global_url

        numero_cheval_1 = 1

        numero_cheval_2 = 3

        numero_cheval_3 = 5

        mise = 1

        time.sleep(1)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(1)

        # with Firefox
        browser = webdriver.Firefox(executable_path='A:\\GitHub\\Cristal_Ball\\geckodriver.exe')

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get(url)

        time.sleep(15)

        parametrer_button = browser.find_element_by_xpath(
            "//a[@class='ui-button ui-large ui-light ui-collapsible ui-collapsed params-button']"
        )
        parametrer_button.click()

        time.sleep(5)

        tout_refuser_button = browser.find_element_by_xpath(
            "//button[@class='ui-button ui-large ui-light']"
        )
        tout_refuser_button.click()

        time.sleep(10)

        trio_ordre_button = browser.find_element_by_xpath(
            "//a[@data-turf-category='TRIO_ORDRE']"
        )
        trio_ordre_button.click()

        time.sleep(5)

        runner_gagnant_1 = browser.find_element_by_xpath(
            "/html/body/div/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]/div/div[4]/ul[2]"
            "/li/div/div[2]/ul/li[" + str(numero_cheval_1 + 1) + "]/div/div[10]/i"
        )
        runner_gagnant_1.click()

        time.sleep(5)

        runner_gagnant_2 = browser.find_element_by_xpath(
            "/html/body/div/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]/div/div[4]/ul[2]"
            "/li/div/div[2]/ul/li[" + str(numero_cheval_2 + 1) + "]/div/div[10]/i"
        )
        runner_gagnant_2.click()

        time.sleep(5)

        runner_gagnant_3 = browser.find_element_by_xpath(
            "/html/body/div/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]/div/div[4]/ul[2]"
            "/li/div/div[2]/ul/li[" + str(numero_cheval_3 + 1) + "]/div/div[10]/i"
        )
        runner_gagnant_3.click()

        time.sleep(5)

        mise_input = browser.find_element_by_xpath("//input[@name='stake']")
        mise_input.clear()
        mise_input.send_keys(str(mise))

        time.sleep(5)

        parier_button = browser.find_element_by_xpath(
            "//a[@id='turf_betslip_place']"
        )
        parier_button.click()

        time.sleep(5)

        email_input = browser.find_element_by_xpath(
            "//input[@id='login-username']"
        )
        email_input.clear()
        email_input.send_keys(".@outlook.fr")

        time.sleep(5)

        password_input = browser.find_element_by_xpath(
            "//input[@id='login-password']"
        )
        password_input.clear()
        password_input.send_keys("")

        time.sleep(5)

        date_de_naissance_input = browser.find_element_by_xpath(
            "//input[@id='dob_input']"
        )
        date_de_naissance_input.clear()
        date_de_naissance_input.send_keys("")

        time.sleep(5)

        me_connecter_button = browser.find_element_by_xpath(
            "//input[@value='Me connecter'][@class='ui-button button-login']"
        )
        me_connecter_button.click()

        time.sleep(5)

        parier_button = browser.find_element_by_xpath(
            "//a[@id='turf_betslip_place']"
        )
        parier_button.click()

        time.sleep(5)

        """
        confirmer_button = browser.find_element_by_xpath(
            "//a[@id='turf_betslip_confirm']"
        )
        confirmer_button.click()

        time.sleep(5)
        """

    # 2 sur 4 :
    def test_selectionner_deux_chevaux_pour_un_2_sur_4(self):
        print('test_selectionner_deux_chevaux_pour_un_2_sur_4')

        url = global_url

        numero_cheval_1 = 1

        numero_cheval_2 = 4

        time.sleep(1)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(1)

        # with Firefox
        browser = webdriver.Firefox(executable_path='A:\\GitHub\\Cristal_Ball\\geckodriver.exe')

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get(url)

        time.sleep(15)

        parametrer_button = browser.find_element_by_xpath(
            "//a[@class='ui-button ui-large ui-light ui-collapsible ui-collapsed params-button']"
        )
        parametrer_button.click()

        time.sleep(5)

        tout_refuser_button = browser.find_element_by_xpath(
            "//button[@class='ui-button ui-large ui-light']"
        )
        tout_refuser_button.click()

        time.sleep(10)

        deux_sur_4_button = browser.find_element_by_xpath(
            "//a[@data-turf-category='2SUR4']"
        )
        deux_sur_4_button.click()

        time.sleep(5)

        runner_gagnant_1 = browser.find_element_by_xpath(
            "/html/body/div/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]"
            "/div/div[4]/ul[2]/li/div/div[2]/ul/li[" + str(numero_cheval_1 + 1) + "]/div"
        ).find_element_by_class_name("betchoice")
        runner_gagnant_1.click()

        time.sleep(5)

        runner_gagnant_2 = browser.find_element_by_xpath(
            "/html/body/div/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]/div/div[4]/ul[2]"
            "/li/div/div[2]/ul/li[" + str(numero_cheval_2 + 1) + "]/div"
        ).find_element_by_class_name("betchoice")
        runner_gagnant_2.click()

        time.sleep(5)

    #
    def test_miser_un_2_sur_4(self):
        print('test_miser_un_2_sur_4')

        url = global_url

        numero_cheval_1 = 5

        numero_cheval_2 = 7

        mise = 1

        time.sleep(1)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(1)

        # with Firefox
        browser = webdriver.Firefox(executable_path='A:\\GitHub\\Cristal_Ball\\geckodriver.exe')

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get(url)

        time.sleep(15)

        parametrer_button = browser.find_element_by_xpath(
            "//a[@class='ui-button ui-large ui-light ui-collapsible ui-collapsed params-button']"
        )
        parametrer_button.click()

        time.sleep(5)

        tout_refuser_button = browser.find_element_by_xpath(
            "//button[@class='ui-button ui-large ui-light']"
        )
        tout_refuser_button.click()

        time.sleep(10)

        deux_sur_4_button = browser.find_element_by_xpath(
            "//a[@data-turf-category='2SUR4']"
        )
        deux_sur_4_button.click()

        time.sleep(5)

        runner_gagnant_1 = browser.find_element_by_xpath(
            "/html/body/div/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]"
            "/div/div[4]/ul[2]/li/div/div[2]/ul/li[" + str(numero_cheval_1 + 1) + "]/div"
        ).find_element_by_class_name("betchoice")
        runner_gagnant_1.click()

        time.sleep(5)

        runner_gagnant_2 = browser.find_element_by_xpath(
            "/html/body/div/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]/div/div[4]/ul[2]"
            "/li/div/div[2]/ul/li[" + str(numero_cheval_2 + 1) + "]/div"
        ).find_element_by_class_name("betchoice")
        runner_gagnant_2.click()

        time.sleep(5)

        mise_input = browser.find_element_by_xpath("//input[@name='stake']")
        mise_input.clear()
        mise_input.send_keys(str(mise))

        time.sleep(5)

        parier_button = browser.find_element_by_xpath(
            "//a[@id='turf_betslip_place']"
        )
        parier_button.click()

        time.sleep(5)

        email_input = browser.find_element_by_xpath(
            "//input[@id='login-username']"
        )
        email_input.clear()
        email_input.send_keys(".@outlook.fr")

        time.sleep(5)

        password_input = browser.find_element_by_xpath(
            "//input[@id='login-password']"
        )
        password_input.clear()
        password_input.send_keys("")

        time.sleep(5)

        date_de_naissance_input = browser.find_element_by_xpath(
            "//input[@id='dob_input']"
        )
        date_de_naissance_input.clear()
        date_de_naissance_input.send_keys("")

        time.sleep(5)

        me_connecter_button = browser.find_element_by_xpath(
            "//input[@value='Me connecter'][@class='ui-button button-login']"
        )
        me_connecter_button.click()

        time.sleep(5)

        parier_button = browser.find_element_by_xpath(
            "//a[@id='turf_betslip_place']"
        )
        parier_button.click()

        time.sleep(5)

        """
        confirmer_button = browser.find_element_by_xpath(
            "//a[@id='turf_betslip_confirm']"
        )
        confirmer_button.click()

        time.sleep(5)
        """

    # quadri :
    def test_selectionner_trois_chevaux_pour_un_quadri_desordre(self):
        print('test_selectionner_trois_chevaux_pour_un_quadri_desordre')

        url = global_url

        numero_cheval_1 = 1

        numero_cheval_2 = 3

        numero_cheval_3 = 5

        numero_cheval_4 = 7

        time.sleep(1)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(1)

        # with Firefox
        browser = webdriver.Firefox(executable_path='A:\\GitHub\\Cristal_Ball\\geckodriver.exe')

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get(url)

        time.sleep(15)

        parametrer_button = browser.find_element_by_xpath(
            "//a[@class='ui-button ui-large ui-light ui-collapsible ui-collapsed params-button']"
        )
        parametrer_button.click()

        time.sleep(5)

        tout_refuser_button = browser.find_element_by_xpath(
            "//button[@class='ui-button ui-large ui-light']"
        )
        tout_refuser_button.click()

        time.sleep(10)

        quadri_button = browser.find_element_by_xpath(
            "//a[@data-turf-category='QUADRI']"
        )
        quadri_button.click()

        time.sleep(5)

        runner_gagnant_1 = browser.find_element_by_xpath(
            "/html/body/div/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]"
            "/div/div[4]/ul[2]/li/div/div[2]/ul/li[" + str(numero_cheval_1 + 1) + "]/div/div[10]/i"
        )
        runner_gagnant_1.click()

        time.sleep(5)

        runner_gagnant_2= browser.find_element_by_xpath(
            "/html/body/div/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]/div/div[4]/ul[2]"
            "/li/div/div[2]/ul/li[" + str(numero_cheval_2 + 1) + "]/div/div[10]/i"
        )
        runner_gagnant_2.click()

        time.sleep(5)

        runner_gagnant_3 = browser.find_element_by_xpath(
            "/html/body/div/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]/div/div[4]/ul[2]"
            "/li/div/div[2]/ul/li[" + str(numero_cheval_3 + 1) + "]/div/div[10]/i"
        )
        runner_gagnant_3.click()

        time.sleep(5)

        runner_gagnant_4 = browser.find_element_by_xpath(
            "/html/body/div/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]/div/div[4]/ul[2]"
            "/li/div/div[2]/ul/li[" + str(numero_cheval_4 + 1) + "]/div/div[10]/i"
        )
        runner_gagnant_4.click()

        time.sleep(5)

    #
    def test_miser_un_quadri_desordre(self):
        print('test_miser_un_quadri_desordre')

        url = global_url

        numero_cheval_1 = 1

        numero_cheval_2 = 2

        numero_cheval_3 = 3

        numero_cheval_4 = 4

        mise = 1

        time.sleep(1)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(1)

        # with Firefox
        browser = webdriver.Firefox(executable_path='A:\\GitHub\\Cristal_Ball\\geckodriver.exe')

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get(url)

        time.sleep(15)

        parametrer_button = browser.find_element_by_xpath(
            "//a[@class='ui-button ui-large ui-light ui-collapsible ui-collapsed params-button']"
        )
        parametrer_button.click()

        time.sleep(5)

        tout_refuser_button = browser.find_element_by_xpath(
            "//button[@class='ui-button ui-large ui-light']"
        )
        tout_refuser_button.click()

        time.sleep(10)

        quadri_button = browser.find_element_by_xpath(
            "//a[@data-turf-category='QUADRI']"
        )
        quadri_button.click()

        time.sleep(5)

        runner_gagnant_1 = browser.find_element_by_xpath(
            "/html/body/div/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]"
            "/div/div[4]/ul[2]/li/div/div[2]/ul/li[" + str(numero_cheval_1 + 1) + "]/div/div[10]/i"
        )
        runner_gagnant_1.click()

        time.sleep(5)

        runner_gagnant_2 = browser.find_element_by_xpath(
            "/html/body/div/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]/div/div[4]/ul[2]"
            "/li/div/div[2]/ul/li[" + str(numero_cheval_2 + 1) + "]/div/div[10]/i"
        )
        runner_gagnant_2.click()

        time.sleep(5)

        runner_gagnant_3 = browser.find_element_by_xpath(
            "/html/body/div/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]"
            "/div/div[4]/ul[2]/li/div/div[2]/ul/li[" + str(numero_cheval_3 + 1) + "]/div/div[10]/i"
        )
        runner_gagnant_3.click()

        time.sleep(5)

        runner_gagnant_4 = browser.find_element_by_xpath(
            "/html/body/div/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]"
            "/div/div[4]/ul[2]/li/div/div[2]/ul/li[" + str(numero_cheval_4 + 1) + "]/div/div[10]/i"
        )
        runner_gagnant_4.click()

        time.sleep(5)

        mise_input = browser.find_element_by_xpath("//input[@name='stake']")
        mise_input.clear()
        mise_input.send_keys(str(mise))

        time.sleep(5)

        parier_button = browser.find_element_by_xpath(
            "//a[@id='turf_betslip_place']"
        )
        parier_button.click()

        time.sleep(5)

        email_input = browser.find_element_by_xpath(
            "//input[@id='login-username']"
        )
        email_input.clear()
        email_input.send_keys(".@outlook.fr")

        time.sleep(5)

        password_input = browser.find_element_by_xpath(
            "//input[@id='login-password']"
        )
        password_input.clear()
        password_input.send_keys("")

        time.sleep(5)

        date_de_naissance_input = browser.find_element_by_xpath(
            "//input[@id='dob_input']"
        )
        date_de_naissance_input.clear()
        date_de_naissance_input.send_keys("")

        time.sleep(5)

        me_connecter_button = browser.find_element_by_xpath(
            "//input[@value='Me connecter'][@class='ui-button button-login']"
        )
        me_connecter_button.click()

        time.sleep(5)

        parier_button = browser.find_element_by_xpath(
            "//a[@id='turf_betslip_place']"
        )
        parier_button.click()

        time.sleep(5)

    # quadri ordre :
    def test_selectionner_trois_chevaux_pour_un_quadri_ordre(self):
        print('test_selectionner_trois_chevaux_pour_un_quadri_ordre')

        url = global_url

        numero_cheval_1 = 1

        numero_cheval_2 = 3

        numero_cheval_3 = 5

        numero_cheval_4 = 7

        time.sleep(1)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(1)

        # with Firefox
        browser = webdriver.Firefox(executable_path='A:\\GitHub\\Cristal_Ball\\geckodriver.exe')

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get(url)

        time.sleep(15)

        parametrer_button = browser.find_element_by_xpath(
            "//a[@class='ui-button ui-large ui-light ui-collapsible ui-collapsed params-button']"
        )
        parametrer_button.click()

        time.sleep(5)

        tout_refuser_button = browser.find_element_by_xpath(
            "//button[@class='ui-button ui-large ui-light']"
        )
        tout_refuser_button.click()

        time.sleep(10)

        quadri_ordre_button = browser.find_element_by_xpath(
            "//a[@data-turf-category='QUADRI_ORDRE']"
        )
        quadri_ordre_button.click()

        time.sleep(5)

        runner_gagnant_1 = browser.find_element_by_xpath(
            "/html/body/div/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]"
            "/div/div[4]/ul[2]/li/div/div[2]/ul/li[" + str(numero_cheval_1 + 1) + "]/div/div[10]/i"
        )
        runner_gagnant_1.click()

        time.sleep(5)

        runner_gagnant_2 = browser.find_element_by_xpath(
            "/html/body/div/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]/div/div[4]/ul[2]"
            "/li/div/div[2]/ul/li[" + str(numero_cheval_2 + 1) + "]/div/div[10]/i"
        )
        runner_gagnant_2.click()

        time.sleep(5)

        runner_gagnant_3 = browser.find_element_by_xpath(
            "/html/body/div/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]"
            "/div/div[4]/ul[2]/li/div/div[2]/ul/li[" + str(numero_cheval_3 + 1) + "]/div/div[10]/i"
        )
        runner_gagnant_3.click()

        time.sleep(5)

        runner_gagnant_4 = browser.find_element_by_xpath(
            "/html/body/div/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]"
            "/div/div[4]/ul[2]/li/div/div[2]/ul/li[" + str(numero_cheval_4 + 1) + "]/div/div[10]/i"
        )
        runner_gagnant_4.click()

        time.sleep(5)

    #
    def test_miser_un_quadri_ordre(self):
        print('test_miser_un_quadri_ordre')

        url = global_url

        numero_cheval_1 = 1

        numero_cheval_2 = 2

        numero_cheval_3 = 3

        numero_cheval_4 = 4

        mise = 1

        time.sleep(1)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(1)

        # with Firefox
        browser = webdriver.Firefox(executable_path='A:\\GitHub\\Cristal_Ball\\geckodriver.exe')

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get(url)

        time.sleep(15)

        parametrer_button = browser.find_element_by_xpath(
            "//a[@class='ui-button ui-large ui-light ui-collapsible ui-collapsed params-button']"
        )
        parametrer_button.click()

        time.sleep(5)

        tout_refuser_button = browser.find_element_by_xpath(
            "//button[@class='ui-button ui-large ui-light']"
        )
        tout_refuser_button.click()

        time.sleep(10)

        quadri_ordre_button = browser.find_element_by_xpath(
            "//a[@data-turf-category='QUADRI_ORDRE']"
        )
        quadri_ordre_button.click()

        time.sleep(5)

        runner_gagnant_1 = browser.find_element_by_xpath(
            "/html/body/div/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]"
            "/div/div[4]/ul[2]/li/div/div[2]/ul/li[" + str(numero_cheval_1 + 1) + "]/div/div[10]/i"
        )
        runner_gagnant_1.click()

        time.sleep(5)

        runner_gagnant_2 = browser.find_element_by_xpath(
            "/html/body/div/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]/div/div[4]/ul[2]"
            "/li/div/div[2]/ul/li[" + str(numero_cheval_2 + 1) + "]/div/div[10]/i"
        )
        runner_gagnant_2.click()

        time.sleep(5)

        runner_gagnant_3 = browser.find_element_by_xpath(
            "/html/body/div/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]"
            "/div/div[4]/ul[2]/li/div/div[2]/ul/li[" + str(numero_cheval_3 + 1) + "]/div/div[10]/i"
        )
        runner_gagnant_3.click()

        time.sleep(5)

        runner_gagnant_4 = browser.find_element_by_xpath(
            "/html/body/div/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]"
            "/div/div[4]/ul[2]/li/div/div[2]/ul/li[" + str(numero_cheval_4 + 1) + "]/div/div[10]/i"
        )
        runner_gagnant_4.click()

        time.sleep(5)

        mise_input = browser.find_element_by_xpath("//input[@name='stake']")
        mise_input.clear()
        mise_input.send_keys(str(mise))

        time.sleep(5)

        parier_button = browser.find_element_by_xpath(
            "//a[@id='turf_betslip_place']"
        )
        parier_button.click()

        time.sleep(5)

        email_input = browser.find_element_by_xpath(
            "//input[@id='login-username']"
        )
        email_input.clear()
        email_input.send_keys(".@outlook.fr")

        time.sleep(5)

        password_input = browser.find_element_by_xpath(
            "//input[@id='login-password']"
        )
        password_input.clear()
        password_input.send_keys("")

        time.sleep(5)

        date_de_naissance_input = browser.find_element_by_xpath(
            "//input[@id='dob_input']"
        )
        date_de_naissance_input.clear()
        date_de_naissance_input.send_keys("")

        time.sleep(5)

        me_connecter_button = browser.find_element_by_xpath(
            "//input[@value='Me connecter'][@class='ui-button button-login']"
        )
        me_connecter_button.click()

        time.sleep(5)

        parier_button = browser.find_element_by_xpath(
            "//a[@id='turf_betslip_place']"
        )
        parier_button.click()

        time.sleep(5)

        """
        confirmer_button = browser.find_element_by_xpath(
            "//a[@id='turf_betslip_confirm']"
        )
        confirmer_button.click()

        time.sleep(5)
        """

    # le deuzio :
    def test_selectionner_un_cheval_pour_un_deuzio(self):
        print('test_selectionner_un_cheval_pour_un_deuzio')

        url = global_url

        numero_cheval = 7

        time.sleep(1)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(1)

        # with Firefox
        browser = webdriver.Firefox(executable_path='A:\\GitHub\\Cristal_Ball\\geckodriver.exe')

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get(url)

        time.sleep(15)

        parametrer_button = browser.find_element_by_xpath(
            "//a[@class='ui-button ui-large ui-light ui-collapsible ui-collapsed params-button']"
        )
        parametrer_button.click()

        time.sleep(5)

        tout_refuser_button = browser.find_element_by_xpath(
            "//button[@class='ui-button ui-large ui-light']"
        )
        tout_refuser_button.click()

        time.sleep(10)

        deuzio_button = browser.find_element_by_xpath(
            "//a[@data-turf-category='DEUZIO']"
        )
        deuzio_button.click()

        time.sleep(5)

        runner_gagnant = browser.find_element_by_xpath(
            "/html/body/div/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]"
            "/div/div[3]/ul[2]/li/div/div[2]/ul/li[" + str(numero_cheval + 1) + "]/div/div[10]/i"
        )
        runner_gagnant.click()

        time.sleep(5)

    #
    def test_miser_sur_un_deuzio(self):
        print('test_miser_sur_un_deuzio')

        url = global_url

        numero_cheval = 7

        mise = 1

        time.sleep(1)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(1)

        # with Firefox
        browser = webdriver.Firefox(executable_path='A:\\GitHub\\Cristal_Ball\\geckodriver.exe')

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get(url)

        time.sleep(15)

        parametrer_button = browser.find_element_by_xpath(
            "//a[@class='ui-button ui-large ui-light ui-collapsible ui-collapsed params-button']"
        )
        parametrer_button.click()

        time.sleep(5)

        tout_refuser_button = browser.find_element_by_xpath(
            "//button[@class='ui-button ui-large ui-light']"
        )
        tout_refuser_button.click()

        time.sleep(10)

        deuzio_button = browser.find_element_by_xpath(
            "//a[@data-turf-category='DEUZIO']"
        )
        deuzio_button.click()

        time.sleep(5)

        runner_gagnant = browser.find_element_by_xpath(
            "/html/body/div/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]"
            "/div/div[3]/ul[2]/li/div/div[2]/ul/li[" + str(numero_cheval + 1) + "]/div/div[10]/i"
        )
        runner_gagnant.click()

        time.sleep(5)

        mise_input = browser.find_element_by_xpath("//input[@name='stake']")
        mise_input.clear()
        mise_input.send_keys(str(mise))

        time.sleep(5)

        parier_button = browser.find_element_by_xpath(
            "//a[@id='turf_betslip_place']"
        )
        parier_button.click()

        time.sleep(5)

        email_input = browser.find_element_by_xpath(
            "//input[@id='login-username']"
        )
        email_input.clear()
        email_input.send_keys(".@outlook.fr")

        time.sleep(5)

        password_input = browser.find_element_by_xpath(
            "//input[@id='login-password']"
        )
        password_input.clear()
        password_input.send_keys("")

        time.sleep(5)

        date_de_naissance_input = browser.find_element_by_xpath(
            "//input[@id='dob_input']"
        )
        date_de_naissance_input.clear()
        date_de_naissance_input.send_keys("")

        time.sleep(5)

        me_connecter_button = browser.find_element_by_xpath(
            "//input[@value='Me connecter'][@class='ui-button button-login']"
        )
        me_connecter_button.click()

        time.sleep(5)

        parier_button = browser.find_element_by_xpath(
            "//a[@id='turf_betslip_place']"
        )
        parier_button.click()

        time.sleep(5)

        """
        confirmer_button = browser.find_element_by_xpath(
            "//a[@id='turf_betslip_confirm']"
        )
        confirmer_button.click()

        time.sleep(5)
        """

    # le boulet :
    def test_selectionner_un_cheval_pour_un_boulet(self):
        print('test_selectionner_un_cheval_pour_un_boulet')

        url = global_url

        numero_cheval = 7

        time.sleep(1)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(1)

        # with Firefox
        browser = webdriver.Firefox(executable_path='A:\\GitHub\\Cristal_Ball\\geckodriver.exe')

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get(url)

        time.sleep(15)

        parametrer_button = browser.find_element_by_xpath(
            "//a[@class='ui-button ui-large ui-light ui-collapsible ui-collapsed params-button']"
        )
        parametrer_button.click()

        time.sleep(5)

        tout_refuser_button = browser.find_element_by_xpath(
            "//button[@class='ui-button ui-large ui-light']"
        )
        tout_refuser_button.click()

        time.sleep(10)

        boulet_button = browser.find_element_by_xpath(
            "//a[@data-turf-category='LEBOULET']"
        )
        boulet_button.click()

        time.sleep(5)

        runner_gagnant = browser.find_element_by_xpath(
            "/html/body/div/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]"
            "/div/div[3]/ul[2]/li/div/div[2]/ul/li[" + str(numero_cheval + 1) + "]/div/div[10]/i"
        )
        runner_gagnant.click()

        time.sleep(5)

    #
    def test_miser_sur_un_boulet(self):
        print('test_miser_sur_un_boulet')

        url = global_url

        numero_cheval = 7

        mise = 1

        time.sleep(1)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(1)

        # with Firefox
        browser = webdriver.Firefox(executable_path='A:\\GitHub\\Cristal_Ball\\geckodriver.exe')

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get(url)

        time.sleep(15)

        parametrer_button = browser.find_element_by_xpath(
            "//a[@class='ui-button ui-large ui-light ui-collapsible ui-collapsed params-button']"
        )
        parametrer_button.click()

        time.sleep(5)

        tout_refuser_button = browser.find_element_by_xpath(
            "//button[@class='ui-button ui-large ui-light']"
        )
        tout_refuser_button.click()

        time.sleep(10)

        deuzio_button = browser.find_element_by_xpath(
            "//a[@data-turf-category='DEUZIO']"
        )
        deuzio_button.click()

        time.sleep(5)

        runner_gagnant = browser.find_element_by_xpath(
            "/html/body/div/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]"
            "/div/div[3]/ul[2]/li/div/div[2]/ul/li[" + str(numero_cheval + 1) + "]/div/div[10]/i"
        )
        runner_gagnant.click()

        time.sleep(5)

        mise_input = browser.find_element_by_xpath("//input[@name='stake']")
        mise_input.clear()
        mise_input.send_keys(str(mise))

        time.sleep(5)

        parier_button = browser.find_element_by_xpath(
            "//a[@id='turf_betslip_place']"
        )
        parier_button.click()

        time.sleep(5)

        email_input = browser.find_element_by_xpath(
            "//input[@id='login-username']"
        )
        email_input.clear()
        email_input.send_keys(".@outlook.fr")

        time.sleep(5)

        password_input = browser.find_element_by_xpath(
            "//input[@id='login-password']"
        )
        password_input.clear()
        password_input.send_keys("")

        time.sleep(5)

        date_de_naissance_input = browser.find_element_by_xpath(
            "//input[@id='dob_input']"
        )
        date_de_naissance_input.clear()
        date_de_naissance_input.send_keys("")

        time.sleep(5)

        me_connecter_button = browser.find_element_by_xpath(
            "//input[@value='Me connecter'][@class='ui-button button-login']"
        )
        me_connecter_button.click()

        time.sleep(5)

        parier_button = browser.find_element_by_xpath(
            "//a[@id='turf_betslip_place']"
        )
        parier_button.click()

        time.sleep(5)

        """
        confirmer_button = browser.find_element_by_xpath(
            "//a[@id='turf_betslip_confirm']"
        )
        confirmer_button.click()

        time.sleep(5)
        """

    # mix 4 :
    def test_selectionner_trois_chevaux_pour_un_mix_4(self):
        print('test_selectionner_trois_chevaux_pour_un_quadri_ordre')

        url = global_url

        numero_cheval_1 = 1

        numero_cheval_2 = 2

        numero_cheval_3 = 3

        numero_cheval_4 = 4

        time.sleep(1)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(1)

        # with Firefox
        browser = webdriver.Firefox(executable_path='A:\\GitHub\\Cristal_Ball\\geckodriver.exe')

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get(url)

        time.sleep(15)

        parametrer_button = browser.find_element_by_xpath(
            "//a[@class='ui-button ui-large ui-light ui-collapsible ui-collapsed params-button']"
        )
        parametrer_button.click()

        time.sleep(5)

        tout_refuser_button = browser.find_element_by_xpath(
            "//button[@class='ui-button ui-large ui-light']"
        )
        tout_refuser_button.click()

        time.sleep(10)

        mix_4_button = browser.find_element_by_xpath(
            "//a[@data-turf-category='MIX4']"
        )
        mix_4_button.click()

        time.sleep(5)

        runner_gagnant_1 = browser.find_element_by_xpath(
            "/html/body/div/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]"
            "/div/div[4]/ul[2]/li/div/div[2]/ul/li[" + str(numero_cheval_1 + 1) + "]/div/div[10]/i"
        )
        runner_gagnant_1.click()

        time.sleep(5)

        runner_gagnant_2 = browser.find_element_by_xpath(
            "/html/body/div/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]"
            "/div/div[4]/ul[2]/li/div/div[2]/ul/li[" + str(numero_cheval_2 + 1) + "]/div/div[10]/i"
        )
        runner_gagnant_2.click()

        time.sleep(5)

        runner_gagnant_3 = browser.find_element_by_xpath(
            "/html/body/div/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]"
            "/div/div[4]/ul[2]/li/div/div[2]/ul/li[" + str(numero_cheval_3 + 1) + "]/div/div[10]/i"
        )
        runner_gagnant_3.click()

        time.sleep(5)

        runner_gagnant_4 = browser.find_element_by_xpath(
            "/html/body/div/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]"
            "/div/div[4]/ul[2]/li/div/div[2]/ul/li[" + str(numero_cheval_4 + 1) + "]/div/div[10]/i"
        )
        runner_gagnant_4.click()

        time.sleep(5)

    #
    def test_miser_un_mix_4(self):
        print('test_miser_un_mix_4')

        url = global_url

        numero_cheval_1 = 1

        numero_cheval_2 = 2

        numero_cheval_3 = 3

        numero_cheval_4 = 4

        mise = 1

        time.sleep(1)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(1)

        # with Firefox
        browser = webdriver.Firefox(executable_path='A:\\GitHub\\Cristal_Ball\\geckodriver.exe')

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get(url)

        time.sleep(15)

        parametrer_button = browser.find_element_by_xpath(
            "//a[@class='ui-button ui-large ui-light ui-collapsible ui-collapsed params-button']"
        )
        parametrer_button.click()

        time.sleep(5)

        tout_refuser_button = browser.find_element_by_xpath(
            "//button[@class='ui-button ui-large ui-light']"
        )
        tout_refuser_button.click()

        time.sleep(10)

        mix_4_button = browser.find_element_by_xpath(
            "//a[@data-turf-category='MIX4']"
        )
        mix_4_button.click()

        time.sleep(5)

        runner_gagnant_1 = browser.find_element_by_xpath(
            "/html/body/div/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]"
            "/div/div[4]/ul[2]/li/div/div[2]/ul/li[" + str(numero_cheval_1 + 1) + "]/div/div[10]/i"
        )
        runner_gagnant_1.click()

        time.sleep(5)

        runner_gagnant_2 = browser.find_element_by_xpath(
            "/html/body/div/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]"
            "/div/div[4]/ul[2]/li/div/div[2]/ul/li[" + str(numero_cheval_2 + 1) + "]/div/div[10]/i"
        )
        runner_gagnant_2.click()

        time.sleep(5)

        runner_gagnant_3 = browser.find_element_by_xpath(
            "/html/body/div/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]"
            "/div/div[4]/ul[2]/li/div/div[2]/ul/li[" + str(numero_cheval_3 + 1) + "]/div/div[10]/i"
        )
        runner_gagnant_3.click()

        time.sleep(5)

        runner_gagnant_4 = browser.find_element_by_xpath(
            "/html/body/div/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]"
            "/div/div[4]/ul[2]/li/div/div[2]/ul/li[" + str(numero_cheval_4 + 1) + "]/div/div[10]/i"
        )
        runner_gagnant_4.click()

        time.sleep(5)

        mise_input = browser.find_element_by_xpath("//input[@name='stake']")
        mise_input.clear()
        mise_input.send_keys(str(mise))

        time.sleep(5)

        parier_button = browser.find_element_by_xpath(
            "//a[@id='turf_betslip_place']"
        )
        parier_button.click()

        time.sleep(5)

        email_input = browser.find_element_by_xpath(
            "//input[@id='login-username']"
        )
        email_input.clear()
        email_input.send_keys(".@outlook.fr")

        time.sleep(5)

        password_input = browser.find_element_by_xpath(
            "//input[@id='login-password']"
        )
        password_input.clear()
        password_input.send_keys("")

        time.sleep(5)

        date_de_naissance_input = browser.find_element_by_xpath(
            "//input[@id='dob_input']"
        )
        date_de_naissance_input.clear()
        date_de_naissance_input.send_keys("")

        time.sleep(5)

        me_connecter_button = browser.find_element_by_xpath(
            "//input[@value='Me connecter'][@class='ui-button button-login']"
        )
        me_connecter_button.click()

        time.sleep(5)

        parier_button = browser.find_element_by_xpath(
            "//a[@id='turf_betslip_place']"
        )
        parier_button.click()

        time.sleep(5)

        """
        confirmer_button = browser.find_element_by_xpath(
            "//a[@id='turf_betslip_confirm']"
        )
        confirmer_button.click()

        time.sleep(5)
        """

    # mix S :
    def test_selectionner_un_cheval_pour_un_mix_s(self):
        print('test_selectionner_un_cheval_pour_un_mix_s')

        url = global_url

        numero_cheval = 1

        time.sleep(1)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(1)

        # with Firefox
        browser = webdriver.Firefox(executable_path='A:\\GitHub\\Cristal_Ball\\geckodriver.exe')

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get(url)

        time.sleep(15)

        parametrer_button = browser.find_element_by_xpath(
            "//a[@class='ui-button ui-large ui-light ui-collapsible ui-collapsed params-button']"
        )
        parametrer_button.click()

        time.sleep(5)

        tout_refuser_button = browser.find_element_by_xpath(
            "//button[@class='ui-button ui-large ui-light']"
        )
        tout_refuser_button.click()

        time.sleep(10)

        mixs_button = browser.find_element_by_xpath(
            "//a[@data-turf-category='MIXS']"
        )
        mixs_button.click()

        time.sleep(5)

        runner_gagnant = browser.find_element_by_xpath(
            "/html/body/div/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]/div"
            "/div[3]/ul[2]/li/div/div[2]/ul/li[" + str(numero_cheval + 1) + "]/div/div[10]/i"
        )
        runner_gagnant.click()

        time.sleep(5)

    #
    def test_miser_sur_un_mix_s(self):
        print('test_miser_sur_un_mix_s')

        url = global_url

        numero_cheval = 1

        mise = 1

        time.sleep(1)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(1)

        # with Firefox
        browser = webdriver.Firefox(executable_path='A:\\GitHub\\Cristal_Ball\\geckodriver.exe')

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get(url)

        time.sleep(15)

        parametrer_button = browser.find_element_by_xpath(
            "//a[@class='ui-button ui-large ui-light ui-collapsible ui-collapsed params-button']"
        )
        parametrer_button.click()

        time.sleep(5)

        tout_refuser_button = browser.find_element_by_xpath(
            "//button[@class='ui-button ui-large ui-light']"
        )
        tout_refuser_button.click()

        time.sleep(10)

        mixs_button = browser.find_element_by_xpath(
            "//a[@data-turf-category='MIXS']"
        )
        mixs_button.click()

        time.sleep(5)

        runner_gagnant = browser.find_element_by_xpath(
            "/html/body/div/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]/div"
            "/div[3]/ul[2]/li/div/div[2]/ul/li[" + str(numero_cheval + 1) + "]/div/div[10]/i"
        )
        runner_gagnant.click()

        time.sleep(5)

        mise_input = browser.find_element_by_xpath("//input[@name='stake']")
        mise_input.clear()
        mise_input.send_keys(str(mise))

        time.sleep(5)

        parier_button = browser.find_element_by_xpath(
            "//a[@id='turf_betslip_place']"
        )
        parier_button.click()

        time.sleep(5)

        email_input = browser.find_element_by_xpath(
            "//input[@id='login-username']"
        )
        email_input.clear()
        email_input.send_keys(".@outlook.fr")

        time.sleep(5)

        password_input = browser.find_element_by_xpath(
            "//input[@id='login-password']"
        )
        password_input.clear()
        password_input.send_keys("")

        time.sleep(5)

        date_de_naissance_input = browser.find_element_by_xpath(
            "//input[@id='dob_input']"
        )
        date_de_naissance_input.clear()
        date_de_naissance_input.send_keys("")

        time.sleep(5)

        me_connecter_button = browser.find_element_by_xpath(
            "//input[@value='Me connecter'][@class='ui-button button-login']"
        )
        me_connecter_button.click()

        time.sleep(5)

        parier_button = browser.find_element_by_xpath(
            "//a[@id='turf_betslip_place']"
        )
        parier_button.click()

        time.sleep(5)

        """
        confirmer_button = browser.find_element_by_xpath(
            "//a[@id='turf_betslip_confirm']"
        )
        confirmer_button.click()

        time.sleep(5)
        """

    # 5 sur 5 :
    def test_selectionner_cinq_chevaux_pour_un_5_sur_5_desordre(self):
        print('test_selectionner_cinq_chevaux_pour_un_5_sur_5_desordre')

        url = global_url

        numero_cheval_1 = 1

        numero_cheval_2 = 2

        numero_cheval_3 = 3

        numero_cheval_4 = 5

        numero_cheval_5 = 7

        time.sleep(1)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(1)

        # with Firefox
        browser = webdriver.Firefox(executable_path='A:\\GitHub\\Cristal_Ball\\geckodriver.exe')

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get(url)

        time.sleep(15)

        parametrer_button = browser.find_element_by_xpath(
            "//a[@class='ui-button ui-large ui-light ui-collapsible ui-collapsed params-button']"
        )
        parametrer_button.click()

        time.sleep(5)

        tout_refuser_button = browser.find_element_by_xpath(
            "//button[@class='ui-button ui-large ui-light']"
        )
        tout_refuser_button.click()

        time.sleep(10)

        cinq_sur_cinq_button = browser.find_element_by_xpath(
            "//a[@data-turf-category='5SUR5']"
        )
        cinq_sur_cinq_button.click()

        time.sleep(5)

        runner_gagnant_1 = browser.find_element_by_xpath(
            "/html/body/div/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]"
            "/div/div[4]/ul[2]/li/div/div[2]/ul/li[" + str(numero_cheval_1 + 1) + "]/div"
        ).find_element_by_class_name("betchoice")
        runner_gagnant_1.click()

        time.sleep(5)

        runner_gagnant_2= browser.find_element_by_xpath(
            "/html/body/div/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]/div/div[4]/ul[2]"
            "/li/div/div[2]/ul/li[" + str(numero_cheval_2 + 1) + "]/div"
        ).find_element_by_class_name("betchoice")
        runner_gagnant_2.click()

        time.sleep(5)

        runner_gagnant_3 = browser.find_element_by_xpath(
            "/html/body/div/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]/div/div[4]/ul[2]"
            "/li/div/div[2]/ul/li[" + str(numero_cheval_3 + 1) + "]/div"
        ).find_element_by_class_name("betchoice")
        runner_gagnant_3.click()

        time.sleep(5)

        runner_gagnant_4 = browser.find_element_by_xpath(
            "/html/body/div/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]/div/div[4]/ul[2]"
            "/li/div/div[2]/ul/li[" + str(numero_cheval_4 + 1) + "]/div"
        ).find_element_by_class_name("betchoice")
        runner_gagnant_4.click()

        time.sleep(5)

        runner_gagnant_5 = browser.find_element_by_xpath(
            "/html/body/div/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]/div/div[4]/ul[2]"
            "/li/div/div[2]/ul/li[" + str(numero_cheval_5 + 1) + "]/div"
        ).find_element_by_class_name("betchoice")
        runner_gagnant_5.click()

        time.sleep(5)

    #
    def test_miser_un_5_sur_5_desordre(self):
        print('test_miser_un_5_sur_5_desordre')

        url = global_url

        numero_cheval_1 = 1

        numero_cheval_2 = 3

        numero_cheval_3 = 5

        numero_cheval_4 = 7

        numero_cheval_5 = 9

        mise = 1

        time.sleep(1)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(1)

        # with Firefox
        browser = webdriver.Firefox(executable_path='A:\\GitHub\\Cristal_Ball\\geckodriver.exe')

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get(url)

        time.sleep(15)

        parametrer_button = browser.find_element_by_xpath(
            "//a[@class='ui-button ui-large ui-light ui-collapsible ui-collapsed params-button']"
        )
        parametrer_button.click()

        time.sleep(5)

        tout_refuser_button = browser.find_element_by_xpath(
            "//button[@class='ui-button ui-large ui-light']"
        )
        tout_refuser_button.click()

        time.sleep(10)

        cinq_sur_cinq_button = browser.find_element_by_xpath(
            "//a[@data-turf-category='5SUR5']"
        )
        cinq_sur_cinq_button.click()

        time.sleep(5)

        runner_gagnant_1 = browser.find_element_by_xpath(
            "/html/body/div/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]"
            "/div/div[4]/ul[2]/li/div/div[2]/ul/li[" + str(numero_cheval_1 + 1) + "]/div"
        ).find_element_by_class_name("betchoice")
        runner_gagnant_1.click()

        time.sleep(5)

        runner_gagnant_2 = browser.find_element_by_xpath(
            "/html/body/div/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]/div/div[4]/ul[2]"
            "/li/div/div[2]/ul/li[" + str(numero_cheval_2 + 1) + "]/div"
        ).find_element_by_class_name("betchoice")
        runner_gagnant_2.click()

        time.sleep(5)

        runner_gagnant_3 = browser.find_element_by_xpath(
            "/html/body/div/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]"
            "/div/div[4]/ul[2]/li/div/div[2]/ul/li[" + str(numero_cheval_3 + 1) + "]/div"
        ).find_element_by_class_name("betchoice")
        runner_gagnant_3.click()

        time.sleep(5)

        runner_gagnant_4 = browser.find_element_by_xpath(
            "/html/body/div/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]"
            "/div/div[4]/ul[2]/li/div/div[2]/ul/li[" + str(numero_cheval_4 + 1) + "]/div"
        ).find_element_by_class_name("betchoice")
        runner_gagnant_4.click()

        time.sleep(5)

        runner_gagnant_5 = browser.find_element_by_xpath(
            "/html/body/div/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]"
            "/div/div[4]/ul[2]/li/div/div[2]/ul/li[" + str(numero_cheval_5 + 1) + "]/div"
        ).find_element_by_class_name("betchoice")
        runner_gagnant_5.click()

        time.sleep(5)

        mise_input = browser.find_element_by_xpath("//input[@name='stake']")
        mise_input.clear()
        mise_input.send_keys(str(mise))

        time.sleep(5)

        parier_button = browser.find_element_by_xpath(
            "//a[@id='turf_betslip_place']"
        )
        parier_button.click()

        time.sleep(5)

        email_input = browser.find_element_by_xpath(
            "//input[@id='login-username']"
        )
        email_input.clear()
        email_input.send_keys(".@outlook.fr")

        time.sleep(5)

        password_input = browser.find_element_by_xpath(
            "//input[@id='login-password']"
        )
        password_input.clear()
        password_input.send_keys("")

        time.sleep(5)

        date_de_naissance_input = browser.find_element_by_xpath(
            "//input[@id='dob_input']"
        )
        date_de_naissance_input.clear()
        date_de_naissance_input.send_keys("")

        time.sleep(5)

        me_connecter_button = browser.find_element_by_xpath(
            "//input[@value='Me connecter'][@class='ui-button button-login']"
        )
        me_connecter_button.click()

        time.sleep(5)

        parier_button = browser.find_element_by_xpath(
            "//a[@id='turf_betslip_place']"
        )
        parier_button.click()

        time.sleep(5)

        """
        confirmer_button = browser.find_element_by_xpath(
            "//a[@id='turf_betslip_confirm']"
        )
        confirmer_button.click()

        time.sleep(5)
        """


class Unit_Tests_Web_Automation_Unibet_With_Artificial_Intelligence(unittest.TestCase):
    # 5 sur 5 :
    def test_miser_un_cinq_sur_cinq_desordre_avec_ia(self):
        print('test_miser_un_cinq_sur_cinq_desordre_avec_ia')

        global_scoring_runners_sorted = PMUFinal.global_scoring_runners(global_url)

        runner_1 = global_scoring_runners_sorted[0][0]

        runner_2 = global_scoring_runners_sorted[1][0]

        runner_3 = global_scoring_runners_sorted[2][0]

        runner_4 = global_scoring_runners_sorted[3][0]

        runner_5 = global_scoring_runners_sorted[4][0]

        numero_cheval_1 = int(runner_1)

        numero_cheval_2 = int(runner_2)

        numero_cheval_3 = int(runner_3)

        numero_cheval_4 = int(runner_4)

        numero_cheval_5 = int(runner_5)

        mise = 1

        time.sleep(1)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(1)

        # with Firefox
        browser = webdriver.Firefox(executable_path='A:\\GitHub\\Cristal_Ball\\geckodriver.exe')

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get(global_url)

        time.sleep(15)

        parametrer_button = browser.find_element_by_xpath(
            "//a[@class='ui-button ui-large ui-light ui-collapsible ui-collapsed params-button']"
        )
        parametrer_button.click()

        time.sleep(5)

        tout_refuser_button = browser.find_element_by_xpath(
            "//button[@class='ui-button ui-large ui-light']"
        )
        tout_refuser_button.click()

        time.sleep(10)

        cinq_sur_cinq_button = browser.find_element_by_xpath(
            "//a[@data-turf-category='5SUR5']"
        )
        cinq_sur_cinq_button.click()

        time.sleep(5)

        runner_gagnant_1 = browser.find_element_by_xpath(
            "/html/body/div/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]"
            "/div/div[4]/ul[2]/li/div/div[2]/ul/li[" + str(numero_cheval_1 + 1) + "]/div"
        ).find_element_by_class_name("betchoice")
        runner_gagnant_1.click()

        time.sleep(5)

        runner_gagnant_2 = browser.find_element_by_xpath(
            "/html/body/div/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]/div/div[4]/ul[2]"
            "/li/div/div[2]/ul/li[" + str(numero_cheval_2 + 1) + "]/div"
        ).find_element_by_class_name("betchoice")
        runner_gagnant_2.click()

        time.sleep(5)

        runner_gagnant_3 = browser.find_element_by_xpath(
            "/html/body/div/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]"
            "/div/div[4]/ul[2]/li/div/div[2]/ul/li[" + str(numero_cheval_3 + 1) + "]/div"
        ).find_element_by_class_name("betchoice")
        runner_gagnant_3.click()

        time.sleep(5)

        runner_gagnant_4 = browser.find_element_by_xpath(
            "/html/body/div/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]"
            "/div/div[4]/ul[2]/li/div/div[2]/ul/li[" + str(numero_cheval_4 + 1) + "]/div"
        ).find_element_by_class_name("betchoice")
        runner_gagnant_4.click()

        time.sleep(5)

        runner_gagnant_5 = browser.find_element_by_xpath(
            "/html/body/div/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]"
            "/div/div[4]/ul[2]/li/div/div[2]/ul/li[" + str(numero_cheval_5 + 1) + "]/div"
        ).find_element_by_class_name("betchoice")
        runner_gagnant_5.click()

        time.sleep(5)

        mise_input = browser.find_element_by_xpath("//input[@name='stake']")
        mise_input.clear()
        mise_input.send_keys(str(mise))

        time.sleep(5)

        parier_button = browser.find_element_by_xpath(
            "//a[@id='turf_betslip_place']"
        )
        parier_button.click()

        time.sleep(5)

        email_input = browser.find_element_by_xpath(
            "//input[@id='login-username']"
        )
        email_input.clear()
        email_input.send_keys(".@outlook.fr")

        time.sleep(5)

        password_input = browser.find_element_by_xpath(
            "//input[@id='login-password']"
        )
        password_input.clear()
        password_input.send_keys("")

        time.sleep(5)

        date_de_naissance_input = browser.find_element_by_xpath(
            "//input[@id='dob_input']"
        )
        date_de_naissance_input.clear()
        date_de_naissance_input.send_keys("")

        time.sleep(5)

        me_connecter_button = browser.find_element_by_xpath(
            "//input[@value='Me connecter'][@class='ui-button button-login']"
        )
        me_connecter_button.click()

        time.sleep(5)

        parier_button = browser.find_element_by_xpath(
            "//a[@id='turf_betslip_place']"
        )
        parier_button.click()

        time.sleep(5)

        confirmer_button = browser.find_element_by_xpath(
            "//a[@id='turf_betslip_confirm']"
        )
        confirmer_button.click()

        time.sleep(5)

    #
    def test_stop_firefox(self):
        print("test_stop_firefox")

        subprocess.call("taskkill /F /IM geckodriver.exe")
        subprocess.call("taskkill /F /IM firefox.exe")


class Unit_Tests_Web_Automation_Unibet_With_Artificial_IntelligenceV1(unittest.TestCase):
    # trio :
    def test_miser_un_trio_desordre_avec_ia(self):
        print('test_miser_un_trio_desordre_avec_ia')

        global_scoring_runners_sorted = PMUFinal.global_scoring_runners(global_url)

        runner_1 = global_scoring_runners_sorted[0][0]

        runner_2 = global_scoring_runners_sorted[1][0]

        runner_3 = global_scoring_runners_sorted[2][0]

        # begin to bet
        numero_cheval_1 = int(runner_1)

        numero_cheval_2 = int(runner_2)

        numero_cheval_3 = int(runner_3)

        mise = 1

        time.sleep(1)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(1)

        # with Firefox
        browser = webdriver.Firefox(executable_path='A:\\GitHub\\Cristal_Ball\\geckodriver.exe')

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get(global_url)

        time.sleep(15)

        parametrer_button = browser.find_element_by_xpath(
            "//a[@class='ui-button ui-large ui-light ui-collapsible ui-collapsed params-button']"
        )
        parametrer_button.click()

        time.sleep(5)

        tout_refuser_button = browser.find_element_by_xpath(
            "//button[@class='ui-button ui-large ui-light']"
        )
        tout_refuser_button.click()

        time.sleep(10)

        trio_button = browser.find_element_by_xpath(
            "//a[@data-turf-category='TRIO']"
        )
        trio_button.click()

        time.sleep(5)

        runner_gagnant_1 = browser.find_element_by_xpath(
            "/html/body/div/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]/div/div[4]/ul[2]"
            "/li/div/div[2]/ul/li[" + str(numero_cheval_1 + 1) + "]/div/div[10]/i"
        )
        runner_gagnant_1.click()

        time.sleep(5)

        runner_gagnant_2 = browser.find_element_by_xpath(
            "/html/body/div/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]/div/div[4]/ul[2]"
            "/li/div/div[2]/ul/li[" + str(numero_cheval_2 + 1) + "]/div/div[10]/i"
        )
        runner_gagnant_2.click()

        time.sleep(5)

        runner_gagnant_3 = browser.find_element_by_xpath(
            "/html/body/div/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]/div/div[4]/ul[2]"
            "/li/div/div[2]/ul/li[" + str(numero_cheval_3 + 1) + "]/div/div[10]/i"
        )
        runner_gagnant_3.click()

        time.sleep(5)

        mise_input = browser.find_element_by_xpath("//input[@name='stake']")
        mise_input.clear()
        mise_input.send_keys(str(mise))

        time.sleep(5)

        parier_button = browser.find_element_by_xpath(
            "//a[@id='turf_betslip_place']"
        )
        parier_button.click()

        time.sleep(5)

        email_input = browser.find_element_by_xpath(
            "//input[@id='login-username']"
        )
        email_input.clear()
        email_input.send_keys(".@outlook.fr")

        time.sleep(5)

        password_input = browser.find_element_by_xpath(
            "//input[@id='login-password']"
        )
        password_input.clear()
        password_input.send_keys("")

        time.sleep(5)

        date_de_naissance_input = browser.find_element_by_xpath(
            "//input[@id='dob_input']"
        )
        date_de_naissance_input.clear()
        date_de_naissance_input.send_keys("")

        time.sleep(5)

        me_connecter_button = browser.find_element_by_xpath(
            "//input[@value='Me connecter'][@class='ui-button button-login']"
        )
        me_connecter_button.click()

        time.sleep(5)

        parier_button = browser.find_element_by_xpath(
            "//a[@id='turf_betslip_place']"
        )
        parier_button.click()

        time.sleep(5)

        """
        confirmer_button = browser.find_element_by_xpath(
            "//a[@id='turf_betslip_confirm']"
        )
        confirmer_button.click()

        time.sleep(5)
        """

    # 2 sur 4 :
    def test_miser_un_2_sur_4_avec_ia(self):
        print('test_miser_un_2_sur_4_avec_ia')

        global_scoring_runners_sorted = PMUFinal.global_scoring_runners(global_url)

        runner_1 = global_scoring_runners_sorted[0][0]

        runner_2 = global_scoring_runners_sorted[1][0]

        numero_cheval_1 = int(runner_1)

        numero_cheval_2 = int(runner_2)

        mise = 1

        time.sleep(1)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(1)

        # with Firefox
        browser = webdriver.Firefox(executable_path='A:\\GitHub\\Cristal_Ball\\geckodriver.exe')

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get(global_url)

        time.sleep(15)

        parametrer_button = browser.find_element_by_xpath(
            "//a[@class='ui-button ui-large ui-light ui-collapsible ui-collapsed params-button']"
        )
        parametrer_button.click()

        time.sleep(5)

        tout_refuser_button = browser.find_element_by_xpath(
            "//button[@class='ui-button ui-large ui-light']"
        )
        tout_refuser_button.click()

        time.sleep(10)

        deux_sur_4_button = browser.find_element_by_xpath(
            "//a[@data-turf-category='2SUR4']"
        )
        deux_sur_4_button.click()

        time.sleep(5)

        runner_gagnant_1 = browser.find_element_by_xpath(
            "/html/body/div/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]"
            "/div/div[4]/ul[2]/li/div/div[2]/ul/li[" + str(numero_cheval_1 + 1) + "]/div"
        ).find_element_by_class_name("betchoice")
        runner_gagnant_1.click()

        time.sleep(5)

        runner_gagnant_2 = browser.find_element_by_xpath(
            "/html/body/div/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]/div/div[4]/ul[2]"
            "/li/div/div[2]/ul/li[" + str(numero_cheval_2 + 1) + "]/div"
        ).find_element_by_class_name("betchoice")
        runner_gagnant_2.click()

        time.sleep(5)

        mise_input = browser.find_element_by_xpath("//input[@name='stake']")
        mise_input.clear()
        mise_input.send_keys(str(mise))

        time.sleep(5)

        parier_button = browser.find_element_by_xpath(
            "//a[@id='turf_betslip_place']"
        )
        parier_button.click()

        time.sleep(5)

        email_input = browser.find_element_by_xpath(
            "//input[@id='login-username']"
        )
        email_input.clear()
        email_input.send_keys(".@outlook.fr")

        time.sleep(5)

        password_input = browser.find_element_by_xpath(
            "//input[@id='login-password']"
        )
        password_input.clear()
        password_input.send_keys("")

        time.sleep(5)

        date_de_naissance_input = browser.find_element_by_xpath(
            "//input[@id='dob_input']"
        )
        date_de_naissance_input.clear()
        date_de_naissance_input.send_keys("")

        time.sleep(5)

        me_connecter_button = browser.find_element_by_xpath(
            "//input[@value='Me connecter'][@class='ui-button button-login']"
        )
        me_connecter_button.click()

        time.sleep(5)

        parier_button = browser.find_element_by_xpath(
            "//a[@id='turf_betslip_place']"
        )
        parier_button.click()

        time.sleep(5)

        confirmer_button = browser.find_element_by_xpath(
            "//a[@id='turf_betslip_confirm']"
        )
        confirmer_button.click()

        time.sleep(5)

    # quadri :
    def test_miser_un_quadri_desordre_avec_ia(self):
        print('test_miser_un_quadri_desordre_avec_ia')

        global_scoring_runners_sorted = PMUFinal.global_scoring_runners(global_url)

        runner_1 = global_scoring_runners_sorted[0][0]

        runner_2 = global_scoring_runners_sorted[1][0]

        runner_3 = global_scoring_runners_sorted[2][0]

        runner_4 = global_scoring_runners_sorted[3][0]

        numero_cheval_1 = int(runner_1)

        numero_cheval_2 = int(runner_2)

        numero_cheval_3 = int(runner_3)

        numero_cheval_4 = int(runner_4)

        mise = 1

        time.sleep(1)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(1)

        # with Firefox
        browser = webdriver.Firefox(executable_path='A:\\GitHub\\Cristal_Ball\\geckodriver.exe')

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get(global_url)

        time.sleep(15)

        parametrer_button = browser.find_element_by_xpath(
            "//a[@class='ui-button ui-large ui-light ui-collapsible ui-collapsed params-button']"
        )
        parametrer_button.click()

        time.sleep(5)

        tout_refuser_button = browser.find_element_by_xpath(
            "//button[@class='ui-button ui-large ui-light']"
        )
        tout_refuser_button.click()

        time.sleep(10)

        quadri_button = browser.find_element_by_xpath(
            "//a[@data-turf-category='QUADRI']"
        )
        quadri_button.click()

        time.sleep(5)

        runner_gagnant_1 = browser.find_element_by_xpath(
            "/html/body/div/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]"
            "/div/div[4]/ul[2]/li/div/div[2]/ul/li[" + str(numero_cheval_1 + 1) + "]/div/div[10]/i"
        )
        runner_gagnant_1.click()

        time.sleep(5)

        runner_gagnant_2 = browser.find_element_by_xpath(
            "/html/body/div/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]/div/div[4]/ul[2]"
            "/li/div/div[2]/ul/li[" + str(numero_cheval_2 + 1) + "]/div/div[10]/i"
        )
        runner_gagnant_2.click()

        time.sleep(5)

        runner_gagnant_3 = browser.find_element_by_xpath(
            "/html/body/div/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]"
            "/div/div[4]/ul[2]/li/div/div[2]/ul/li[" + str(numero_cheval_3 + 1) + "]/div/div[10]/i"
        )
        runner_gagnant_3.click()

        time.sleep(5)

        runner_gagnant_4 = browser.find_element_by_xpath(
            "/html/body/div/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]"
            "/div/div[4]/ul[2]/li/div/div[2]/ul/li[" + str(numero_cheval_4 + 1) + "]/div/div[10]/i"
        )
        runner_gagnant_4.click()

        time.sleep(5)

        mise_input = browser.find_element_by_xpath("//input[@name='stake']")
        mise_input.clear()
        mise_input.send_keys(str(mise))

        time.sleep(5)

        parier_button = browser.find_element_by_xpath(
            "//a[@id='turf_betslip_place']"
        )
        parier_button.click()

        time.sleep(5)

        email_input = browser.find_element_by_xpath(
            "//input[@id='login-username']"
        )
        email_input.clear()
        email_input.send_keys(".@outlook.fr")

        time.sleep(5)

        password_input = browser.find_element_by_xpath(
            "//input[@id='login-password']"
        )
        password_input.clear()
        password_input.send_keys("")

        time.sleep(5)

        date_de_naissance_input = browser.find_element_by_xpath(
            "//input[@id='dob_input']"
        )
        date_de_naissance_input.clear()
        date_de_naissance_input.send_keys("")

        time.sleep(5)

        me_connecter_button = browser.find_element_by_xpath(
            "//input[@value='Me connecter'][@class='ui-button button-login']"
        )
        me_connecter_button.click()

        time.sleep(5)

        parier_button = browser.find_element_by_xpath(
            "//a[@id='turf_betslip_place']"
        )
        parier_button.click()

        time.sleep(5)

        confirmer_button = browser.find_element_by_xpath(
            "//a[@id='turf_betslip_confirm']"
        )
        confirmer_button.click()

        time.sleep(5)


if __name__ == '__main__':
    unittest.main()
