import subprocess
import unittest
import time
import warnings
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.action_chains import ActionChains


class UnitTestsWebAutomationOutlookWithoutHeadless(unittest.TestCase):
    # ok
    def test_open_one_page(self):
        print("test_open_one_page")

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
        browser.get('https://outlook.live.com/owa/')

        time.sleep(5)

    # ok
    def test_se_connecter(self):
        print("test_se_connecter")

        username = ".@outlook.fr"

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
        email_input.send_keys(username)
        email_input.send_keys(Keys.ENTER)
        print("email_input inserted")

        time.sleep(5)

        password_input = browser.find_element_by_xpath(
            '//*[@id="i0118"]'
        )
        password_input.clear()
        password_input.send_keys(password)
        password_input.send_keys(Keys.ENTER)
        print("password_input inserted")

        time.sleep(5)

        # click on the checkbox "Ne plus afficher ce message"
        ne_plus_afficher_ce_message_checkbox = browser.find_element_by_xpath(
            '//*[@id="KmsiCheckboxField"]'
        )
        ne_plus_afficher_ce_message_checkbox.click()
        print("ne_plus_afficher_ce_message_checkbox.click()")

        time.sleep(5)

        # click on the button "Non"
        non_button = browser.find_element_by_xpath(
            '//*[@id="idBtn_Back"]'
        )
        non_button.click()
        print("non_button.click()")

        time.sleep(15)

    # ok
    def test_get_one_code_wetransfer(self):
        print("test_get_one_code_wetransfer")

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

        time.sleep(5)

        password_input = browser.find_element_by_xpath(
            '//*[@id="i0118"]'
        )
        password_input.clear()
        password_input.send_keys("")
        password_input.send_keys(Keys.ENTER)
        print("password_input inserted")

        time.sleep(5)

        # click on the checkbox "Ne plus afficher ce message"
        ne_plus_afficher_ce_message_checkbox = browser.find_element_by_xpath(
            '//*[@id="KmsiCheckboxField"]'
        )
        ne_plus_afficher_ce_message_checkbox.click()
        print("ne_plus_afficher_ce_message_checkbox.click()")

        time.sleep(5)

        # click on the button "Non"
        non_button = browser.find_element_by_xpath(
            '//*[@id="idBtn_Back"]'
        )
        non_button.click()
        print("non_button.click()")

        time.sleep(15)

        # Retrieve the code
        code = browser.find_element_by_xpath(
            "/html/body/div[3]/div/div[2]/div[2]/div[1]/div/div/div[3]/div[2]/div/div[1]/div[3]/div/div/div/div"
            "/div/div[2]/div/div/div/div/div[2]/div/div[1]/span"
        ).text.replace('Votre code est : ', '')
        print('code : ' + str(code))

        time.sleep(5)

        # click on the button "Sélectionner tous les messages"
        selectionner_tous_les_messages_button = browser.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div[2]/div[1]/div/div/div[3]/div[2]/div/div[1]/div[1]/div[1]/div/div[1]'
            '/div/i[2]'
        )
        selectionner_tous_les_messages_button.click()
        print("selectionner_tous_les_messages_button.click()")

        # click on the button "Vider Prioritaire"
        vider_prioritaire_button = browser.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div[2]/div[1]/div/div/div[3]/div[1]/div/div/div/div/div/div[1]/div[1]/button'
        )
        vider_prioritaire_button.click()
        print("vider_prioritaire_button.click()")

        time.sleep(5)

        # click on the button "Ok"
        ok_button = browser.find_element_by_xpath(
            '//*[@id="ok-1"]'
        )
        ok_button.click()
        print("ok_button.click()")

        time.sleep(5)

        # click on the button "Mon profile"
        mon_profile_button = browser.find_element_by_xpath(
            '/html/body/div[3]/div/div[1]/div/div[1]/div[3]/div[1]/button/div/div[2]/div/div/div/div/div/div[2]/img'
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

        time.sleep(5)

        browser.quit()

    # ok
    def test_kill_some_processes(self):
        print("test_kill_some_processes")

        subprocess.call("taskkill /F /IM geckodriver.exe")
        subprocess.call("taskkill /F /IM firefox.exe")


class UnitTestsWebAutomationOutlookWithoutHeadlessForSendingEmails(unittest.TestCase):
    # ok
    def test_send_one_email_for_applying_for_a_job_as_ingenieur_energies_renouvelables(self):
        print("test_send_one_email_for_applying_for_a_job_as_ingenieur_energies_renouvelables")

        email = "@gmail.com"

        envoye_a = email.lower()

        objet = "Candidature spontanée pour un emploi en tant qu'ingénieur en énergies renouvelables en contrat " \
                "à durée indéterminée à temps plein - "

        message = """Bonjour,

Vu les articles L1211-1 à L1273-6 du code du travail concernant le contrat de travail,

Conformément au troisième degré de l'article L1221-19 du code du travail, je vous envoie mon CV pour postuler pour un emploi en contrat cadre à durée indéterminée en tant qu'ingénieur en énergies renouvelables pour la fabrication de machines à énergie libre (https://github.com/Jay4C/Free-energy-devices) afin d'alimenter vos appareils énergivores sans avoir besoin d'être branché sur le réseau public d'électricité, de consommer des énergies primaires fossiles et de consommer des énergies telles que l'énergie solaire, l'énergie éolienne, l'énergie géothermique et l'énergie hydraulique.

En attendant votre décision, je vous prie de croire, mes salutations les plus sincères.


Ingénieur généraliste diplômé de l'École Supérieure d'Ingénieurs Léonard de Vinci
Téléphone : """

        file_upload = "C:\\Users\\DELL\\Documents\\Outils\\Desktop_Automation" \
                      "\\[Ingenieur_Energies_Renouvelables].pdf"

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
        browser.get('https://outlook.live.com/owa/')
        print("browser.get('https://outlook.live.com/owa/')")

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

        time.sleep(5)

        password_input = browser.find_element_by_xpath(
            '//*[@id="i0118"]'
        )
        password_input.clear()
        password_input.send_keys("")
        password_input.send_keys(Keys.ENTER)
        print("password_input inserted")

        time.sleep(5)

        # click on the checkbox "Ne plus afficher ce message"
        ne_plus_afficher_ce_message_checkbox = browser.find_element_by_xpath(
            '//*[@id="KmsiCheckboxField"]'
        )
        ne_plus_afficher_ce_message_checkbox.click()
        print("ne_plus_afficher_ce_message_checkbox.click()")

        time.sleep(5)

        # click on the button "Non"
        non_button = browser.find_element_by_xpath(
            '//*[@id="idBtn_Back"]'
        )
        non_button.click()
        print("non_button.click()")

        time.sleep(15)

        # click on the button "Nouveau courrier"
        nouveau_courrier_button = browser.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div[2]/div[1]/div/div/div[1]/div[1]/div[2]/div/div/button'
        )
        nouveau_courrier_button.click()
        print("nouveau_courrier_button.click()")

        time.sleep(10)

        # Insert the email sender
        envoye_a_input = browser.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div[2]/div[1]/div/div/div[3]/div[2]/div/div[2]/div[1]/div/div/div'
            '/div[1]/div[1]/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/input'
        )
        envoye_a_input.clear()
        envoye_a_input.send_keys(envoye_a)
        time.sleep(2)
        envoye_a_input.send_keys(Keys.ENTER)
        print("envoye_a_input inserted")

        time.sleep(7)

        # Insert the subject
        for i in range(0, 1000):
            try:
                subject_input = browser.find_element_by_xpath(
                    '//*[@id="TextField' + str(i) + '"]'
                )
                subject_input.clear()
                subject_input.send_keys(objet)
                time.sleep(2)
                subject_input.send_keys(Keys.TAB)
                print("subject_input inserted")
                break
            except Exception as e:
                print('error subject_input TextField' + str(i) + ' : ' + str(e))

        time.sleep(7)

        # Insert the message
        try:
            actions = ActionChains(browser)
            actions.send_keys(message)
            actions.perform()
            print("message_input inserted")
        except Exception as e:
            print('error message_input : ' + str(e))

        time.sleep(15)

        # Insert the file
        try:
            file_input = browser.find_element_by_xpath(
                "/html/body/div[3]/div/div[2]/div[2]/div[1]/div/div/div[3]/div[1]/div/span/input[1]"
            )
            file_input.send_keys(
                file_upload
            )
            print("file_input inserted")
        except Exception as e:
            print('error file_input : ' + str(e))

        time.sleep(15)

        # click on the button "Envoyer"
        try:
            envoyer_button = browser.find_element_by_xpath(
                '/html/body/div[3]/div/div[2]/div[2]/div[1]/div/div/div[3]/div[2]/div/div[2]/div[1]'
                '/div/div/div/div[1]/div[3]/div[2]/div[1]/div/div/span/button[1]'
            )
            envoyer_button.click()
            print("envoyer_button.click()")
        except Exception as e:
            print('error envoyer_button : ' + str(e))

        time.sleep(10)


class UnitTestsWebAutomationOutlookWithHeadlessForSendingEmailsForJobs(unittest.TestCase):
    # ok
    def test_send_one_email_for_applying_for_a_job_as_ingenieur_energies_renouvelables(self):
        print("test_send_one_email_for_applying_for_a_job_as_ingenieur_energies_renouvelables")

        email = "@gmail.com"

        envoye_a = email.lower()

        objet = "Candidature spontanée pour un emploi en tant qu'ingénieur en énergies renouvelables en contrat " \
                "à durée indéterminée à temps plein - "

        message = """Bonjour,

Vu les articles L1211-1 à L1273-6 du code du travail concernant le contrat de travail,

Conformément au troisième degré de l'article L1221-19 du code du travail, je vous envoie mon CV pour postuler pour un emploi en contrat cadre à durée indéterminée en tant qu'ingénieur en énergies renouvelables pour la fabrication de machines à énergie libre (https://github.com/Jay4C/Free-energy-devices) afin d'alimenter vos appareils énergivores sans avoir besoin d'être branché sur le réseau public d'électricité, de consommer des énergies primaires fossiles et de consommer des énergies telles que l'énergie solaire, l'énergie éolienne, l'énergie géothermique et l'énergie hydraulique.

En attendant votre décision, je vous prie de croire, mes salutations les plus sincères.


Ingénieur généraliste diplômé de l'École Supérieure d'Ingénieurs Léonard de Vinci
Téléphone : 00.33.7.49.16.33.29"""

        file_upload = "C:\\Users\\DELL\\Documents\\Outils\\Desktop_Automation" \
                      "\\[Ingenieur_Energies_Renouvelables].pdf"

        time.sleep(5)

        warnings.filterwarnings(
            action="ignore",
            message="unclosed",
            category=ResourceWarning
        )

        time.sleep(5)

        # with Firefox
        options = Options()
        options.headless = True
        browser = webdriver.Firefox(
            executable_path='..\\..\\geckodriver.exe',
            options=options
        )

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get('https://outlook.live.com/owa/')
        print("browser.get('https://outlook.live.com/owa/')")

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

        time.sleep(5)

        password_input = browser.find_element_by_xpath(
            '//*[@id="i0118"]'
        )
        password_input.clear()
        password_input.send_keys("")
        password_input.send_keys(Keys.ENTER)
        print("password_input inserted")

        time.sleep(5)

        # click on the checkbox "Ne plus afficher ce message"
        ne_plus_afficher_ce_message_checkbox = browser.find_element_by_xpath(
            '//*[@id="KmsiCheckboxField"]'
        )
        ne_plus_afficher_ce_message_checkbox.click()
        print("ne_plus_afficher_ce_message_checkbox.click()")

        time.sleep(5)

        # click on the button "Non"
        non_button = browser.find_element_by_xpath(
            '//*[@id="idBtn_Back"]'
        )
        non_button.click()
        print("non_button.click()")

        time.sleep(15)

        print('Nouveau courrier pour ' + str(envoye_a))

        # click on the button "Nouveau courrier"
        nouveau_courrier_button = browser.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div[2]/div[1]/div/div/div[1]/div[1]/div[2]/div/div/button'
        )
        nouveau_courrier_button.click()
        print("nouveau_courrier_button.click()")

        time.sleep(10)

        # Insert the email sender
        envoye_a_input = browser.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div[2]/div[1]/div/div/div[3]/div[2]/div/div[2]/div[1]/div/div/div'
            '/div[1]/div[1]/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/input'
        )
        envoye_a_input.clear()
        envoye_a_input.send_keys(envoye_a)
        time.sleep(2)
        envoye_a_input.send_keys(Keys.ENTER)
        print("envoye_a_input inserted")

        time.sleep(7)

        # Insert the subject
        for i in range(0, 1000):
            try:
                subject_input = browser.find_element_by_xpath(
                    '//*[@id="TextField' + str(i) + '"]'
                )
                subject_input.clear()
                subject_input.send_keys(objet)
                time.sleep(2)
                subject_input.send_keys(Keys.TAB)
                print("subject_input inserted")
                break
            except Exception as e:
                print('error subject_input TextField' + str(i) + ' : ' + str(e))

        time.sleep(7)

        # Insert the message
        try:
            actions = ActionChains(browser)
            actions.send_keys(message)
            actions.perform()
            print("message_input inserted")
        except Exception as e:
            print('error message_input : ' + str(e))

        time.sleep(15)

        # Insert the file
        try:
            file_input = browser.find_element_by_xpath(
                "/html/body/div[3]/div/div[2]/div[2]/div[1]/div/div/div[3]/div[1]/div/span/input[1]"
            )
            file_input.send_keys(
                file_upload
            )
            print("file_input inserted")
        except Exception as e:
            print('error file_input : ' + str(e))

        time.sleep(15)

        # click on the button "Envoyer"
        try:
            envoyer_button = browser.find_element_by_xpath(
                '/html/body/div[3]/div/div[2]/div[2]/div[1]/div/div/div[3]/div[2]/div/div[2]/div[1]'
                '/div/div/div/div[1]/div[3]/div[2]/div[1]/div/div/span/button[1]'
            )
            envoyer_button.click()
            print("envoyer_button.click()")
        except Exception as e:
            print('error envoyer_button : ' + str(e))

        time.sleep(10)

        # click on the button "Mon profile"
        mon_profile_button = browser.find_element_by_xpath(
            '/html/body/div[3]/div/div[1]/div/div[1]/div[3]/div[1]/button/div/div[2]/div/div/div/div/div/div[2]/img'
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

        time.sleep(5)

        browser.quit()
        print('browser.quit()')

        time.sleep(5)

    # ok
    def test_send_several_emails_for_applying_for_a_job_as_developpeur_python(self):
        print("test_send_several_emails_for_applying_for_a_job_as_developpeur_python")

        emails = [

        ]

        objet = "Candidature spontanée pour un emploi en tant que développeur python en contrat à durée indéterminée à temps plein - "

        message = """Bonjour,

Je vous envoie mon CV pour postuler pour un emploi en contrat cadre à durée indéterminée en tant que développeur python.

En attendant votre décision, je vous prie de croire, mes salutations les plus sincères.


Ingénieur généraliste diplômé de l'École Supérieure d'Ingénieurs Léonard de Vinci
Téléphone : 00.33.7.49.16.33.29"""

        file_upload = "C:\\Users\\DELL\\Documents\\Outils\\Desktop_Automation\\CV_De_Jason_ALOYAU_[Developpeur_Python].pdf"

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
        # options = options
        browser = webdriver.Firefox(
            executable_path='..\\..\\geckodriver.exe'
        )

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get('https://outlook.live.com/owa/')
        print("browser.get('https://outlook.live.com/owa/')")

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

        time.sleep(5)

        password_input = browser.find_element_by_xpath(
            '//*[@id="i0118"]'
        )
        password_input.clear()
        password_input.send_keys("")
        password_input.send_keys(Keys.ENTER)
        print("password_input inserted")

        time.sleep(5)

        # click on the checkbox "Ne plus afficher ce message"
        ne_plus_afficher_ce_message_checkbox = browser.find_element_by_xpath(
            '//*[@id="KmsiCheckboxField"]'
        )
        ne_plus_afficher_ce_message_checkbox.click()
        print("ne_plus_afficher_ce_message_checkbox.click()")

        time.sleep(5)

        # click on the button "Non"
        non_button = browser.find_element_by_xpath(
            '//*[@id="idBtn_Back"]'
        )
        non_button.click()
        print("non_button.click()")

        time.sleep(15)

        for email in emails:
            envoye_a = email.lower()

            print('Nouveau courrier pour ' + str(envoye_a))

            # click on the button "Nouveau courrier"
            nouveau_courrier_button = browser.find_element_by_xpath(
                '/html/body/div[3]/div/div[2]/div[2]/div[1]/div/div/div[1]/div[1]/div[2]/div/div/button'
            )
            nouveau_courrier_button.click()
            print("nouveau_courrier_button.click()")

            time.sleep(7)

            # Insert the email sender
            envoye_a_input = browser.find_element_by_xpath(
                '/html/body/div[3]/div/div[2]/div[2]/div[1]/div/div/div[3]/div[2]/div/div[2]/div[1]/div/div/div'
                '/div[1]/div[1]/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/input'
            )
            envoye_a_input.clear()
            envoye_a_input.send_keys(envoye_a)
            time.sleep(2)
            envoye_a_input.send_keys(Keys.ENTER)
            time.sleep(2)
            envoye_a_input.send_keys(Keys.TAB)
            print("envoye_a_input inserted")

            time.sleep(7)

            # Insert the subject
            try:
                actions_subject = ActionChains(browser)
                actions_subject.send_keys(objet)
                time.sleep(2)
                actions_subject.send_keys(Keys.TAB)
                actions_subject.perform()
                print("subject_input inserted")
            except Exception as e:
                print('error subject_input : ' + str(e))

            time.sleep(7)

            # Insert the message
            try:
                actions_message = ActionChains(browser)
                actions_message.send_keys(message)
                actions_message.perform()
                print("message_input inserted")
            except Exception as e:
                print('error message_input : ' + str(e))

            time.sleep(15)

            # Insert the file
            try:
                file_input = browser.find_element_by_xpath(
                    "/html/body/div[3]/div/div[2]/div[2]/div[1]/div/div/div[3]/div[1]/div/span/input[1]"
                )
                file_input.send_keys(
                    file_upload
                )
                print("file_input inserted")
            except Exception as e:
                print('error file_input : ' + str(e))

            time.sleep(15)

            # click on the button "Envoyer"
            try:
                envoyer_button = browser.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div[2]/div[1]/div/div/div[3]/div[2]/div/div[2]/div[1]'
                    '/div/div/div/div[1]/div[3]/div[2]/div[1]/div/div/span/button[1]'
                )
                envoyer_button.click()
                print("envoyer_button.click()")
            except Exception as e:
                print('error envoyer_button : ' + str(e))

            time.sleep(15)

        time.sleep(5)

        # click on the button "Mon profile"
        mon_profile_button = browser.find_element_by_xpath(
            '/html/body/div[3]/div/div[1]/div/div[1]/div[3]/div[1]/button/div/div[2]/div/div/div/div/div/div[2]/img'
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

        time.sleep(5)

        browser.quit()
        print('browser.quit()')

        time.sleep(5)

    # ok
    def test_send_several_emails_for_applying_for_a_job_as_developpeur_python_v1(self):
        print("test_send_several_emails_for_applying_for_a_job_as_developpeur_python_v1")

        emails = [

        ]

        objet = "Candidature spontanée pour un emploi en tant que développeur python en contrat à durée indéterminée à temps plein - "

        message = """Bonjour,

Je vous envoie mon CV pour postuler pour un emploi en contrat cadre à durée indéterminée en tant que développeur python.

En attendant votre décision, je vous prie de croire, mes salutations les plus sincères.


Diplôme d'ingénieur généraliste de l'École Supérieure d'Ingénieurs Léonard de Vinci
Téléphone : """

        file_upload = "C:\\Users\\DELL\\Documents\\Outils\\Desktop_Automation\\[Developpeur_Python].pdf"

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
        # options = options
        browser = webdriver.Firefox(
            executable_path='..\\..\\geckodriver.exe'
        )

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get('https://outlook.live.com/owa/')
        print("browser.get('https://outlook.live.com/owa/')")

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

        time.sleep(5)

        password_input = browser.find_element_by_xpath(
            '//*[@id="i0118"]'
        )
        password_input.clear()
        password_input.send_keys("")
        password_input.send_keys(Keys.ENTER)
        print("password_input inserted")

        time.sleep(5)

        # click on the checkbox "Ne plus afficher ce message"
        ne_plus_afficher_ce_message_checkbox = browser.find_element_by_xpath(
            '//*[@id="KmsiCheckboxField"]'
        )
        ne_plus_afficher_ce_message_checkbox.click()
        print("ne_plus_afficher_ce_message_checkbox.click()")

        time.sleep(5)

        # click on the button "Non"
        non_button = browser.find_element_by_xpath(
            '//*[@id="idBtn_Back"]'
        )
        non_button.click()
        print("non_button.click()")

        time.sleep(15)

        for email in emails:
            envoye_a = email.lower()

            print('Nouveau courrier pour ' + str(envoye_a))

            # click on the button "Nouveau courrier"
            nouveau_courrier_button = browser.find_element_by_xpath(
                '/html/body/div[3]/div/div[2]/div[2]/div[1]/div/div/div[1]/div[1]/div[2]/div/div/button'
            )
            nouveau_courrier_button.click()
            print("nouveau_courrier_button.click()")

            time.sleep(7)

            # Insert the email sender
            envoye_a_input = browser.find_element_by_xpath(
                '/html/body/div[3]/div/div[2]/div[2]/div[1]/div/div/div[3]/div[2]/div/div[2]/div[1]/div/div/div'
                '/div[1]/div[1]/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/input'
            )
            envoye_a_input.clear()
            envoye_a_input.send_keys(envoye_a)
            time.sleep(2)
            envoye_a_input.send_keys(Keys.ENTER)
            time.sleep(2)
            envoye_a_input.send_keys(Keys.TAB)
            print("envoye_a_input inserted")

            time.sleep(7)

            # Insert the subject
            try:
                actions_subject = ActionChains(browser)
                actions_subject.send_keys(objet)
                time.sleep(2)
                actions_subject.send_keys(Keys.TAB)
                actions_subject.perform()
                print("subject_input inserted")
            except Exception as e:
                print('error subject_input : ' + str(e))

            time.sleep(7)

            # Insert the message
            try:
                actions_message = ActionChains(browser)
                actions_message.send_keys(message)
                actions_message.perform()
                print("message_input inserted")
            except Exception as e:
                print('error message_input : ' + str(e))

            time.sleep(15)

            # Insert the file
            try:
                file_input = browser.find_element_by_xpath(
                    "/html/body/div[3]/div/div[2]/div[2]/div[1]/div/div/div[3]/div[1]/div/span/input[1]"
                )
                file_input.send_keys(
                    file_upload
                )
                print("file_input inserted")
            except Exception as e:
                print('error file_input : ' + str(e))

            time.sleep(15)

            # click on the button "Envoyer"
            try:
                envoyer_button = browser.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div[2]/div[1]/div/div/div[3]/div[2]/div/div[2]/div[1]'
                    '/div/div/div/div[1]/div[3]/div[2]/div[1]/div/div/span/button[1]'
                )
                envoyer_button.click()
                print("envoyer_button.click()")
            except Exception as e:
                print('error envoyer_button : ' + str(e))

            time.sleep(15)

        time.sleep(5)

        # click on the button "Mon profile"
        mon_profile_button = browser.find_element_by_xpath(
            '/html/body/div[3]/div/div[1]/div/div[1]/div[3]/div[1]/button/div/div[2]/div/div/div/div/div/div[2]/img'
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

        time.sleep(5)

        browser.quit()
        print('browser.quit()')

        time.sleep(5)


class UnitTestsWebAutomationOutlookWithHeadlessForSendingEmailsForBusiness(unittest.TestCase):
    # ok
    def test_send_several_emails_for_integration_api(self):
        print("test_send_several_emails_for_integration_api")

        username = ".@outlook.fr"
        password = ""

        emails = [
            "@gmail.com"
        ]

        objet = "Prestation de service pour l'intégration d'API - Société Holomorphe (Paris)"

        message = """Bonjour,

Suite à notre conversation téléphonique, je vous communique mes coordonnées pour vous proposer mes prestations de service pour l'intégration d'API pour vos besoins.

En attendant votre décision, je vous prie de croire, mes salutations les plus sincères.


Président de la société Holomorphe
Diplôme d'ingénieur généraliste de l'École Supérieure d'Ingénieurs Léonard de Vinci à Paris La Défense
Téléphone : 
Prestation de service pour l'intégration d'API : https://github.com/Jay4C/Holomorphe_Company/tree/main/Sales_of_digital_contents/Integration_API
Informations générales : https://www.societe.com/societe/holomorphe-883632556.html"""

        time.sleep(5)

        warnings.filterwarnings(
            action="ignore",
            message="unclosed",
            category=ResourceWarning
        )

        time.sleep(5)

        # with Firefox
        options = Options()
        options.headless = True
        browser = webdriver.Firefox(
            executable_path='..\\..\\geckodriver.exe',
            options=options
        )

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get('https://outlook.live.com/owa/')
        print("browser.get('https://outlook.live.com/owa/')")

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
        email_input.send_keys(username)
        email_input.send_keys(Keys.ENTER)
        print("email_input inserted")

        time.sleep(5)

        password_input = browser.find_element_by_xpath(
            '//*[@id="i0118"]'
        )
        password_input.clear()
        password_input.send_keys(password)
        password_input.send_keys(Keys.ENTER)
        print("password_input inserted")

        time.sleep(5)

        # click on the checkbox "Ne plus afficher ce message"
        ne_plus_afficher_ce_message_checkbox = browser.find_element_by_xpath(
            '//*[@id="KmsiCheckboxField"]'
        )
        ne_plus_afficher_ce_message_checkbox.click()
        print("ne_plus_afficher_ce_message_checkbox.click()")

        time.sleep(5)

        # click on the button "Non"
        non_button = browser.find_element_by_xpath(
            '//*[@id="idBtn_Back"]'
        )
        non_button.click()
        print("non_button.click()")

        time.sleep(15)

        for email in emails:
            envoye_a = email.lower()

            print('Nouveau courrier pour ' + str(envoye_a))

            # click on the button "Nouveau courrier"
            nouveau_courrier_button = browser.find_element_by_xpath(
                '/html/body/div[3]/div/div[2]/div[2]/div[1]/div/div/div[1]/div[1]/div[2]/div/div/button'
            )
            nouveau_courrier_button.click()
            print("nouveau_courrier_button.click()")

            time.sleep(7)

            # Insert the email sender
            try:
                envoye_a_input = browser.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div[2]/div[1]/div/div/div[3]/div[2]/div/div[2]/div[1]/div/div/div'
                    '/div[1]/div[1]/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/input'
                )
                envoye_a_input.clear()
                envoye_a_input.send_keys(envoye_a)
                time.sleep(2)
                envoye_a_input.send_keys(Keys.ENTER)
                time.sleep(2)
                envoye_a_input.send_keys(Keys.TAB)
                print("envoye_a_input inserted")
            except Exception as e:
                print("error envoye_a_input : " + str(e))

            time.sleep(7)

            # Insert the subject
            try:
                actions_subject = ActionChains(browser)
                actions_subject.send_keys(objet)
                time.sleep(2)
                actions_subject.send_keys(Keys.TAB)
                actions_subject.perform()
                print("subject_input inserted")
            except Exception as e:
                print('error subject_input : ' + str(e))

            time.sleep(7)

            # Insert the message
            try:
                actions_message = ActionChains(browser)
                actions_message.send_keys(message)
                actions_message.perform()
                print("message_input inserted")
            except Exception as e:
                print('error message_input : ' + str(e))

            time.sleep(7)

            # click on the button "Envoyer"
            try:
                actions_envoyer = ActionChains(browser)
                time.sleep(1)
                actions_envoyer.send_keys(Keys.TAB)
                time.sleep(1)
                actions_envoyer.send_keys(Keys.TAB)
                time.sleep(1)
                actions_envoyer.send_keys(Keys.TAB)
                time.sleep(3)
                actions_envoyer.send_keys(Keys.ENTER)
                actions_envoyer.perform()
                print("envoyer_button.click()")
            except Exception as e:
                print('error envoyer_button : ' + str(e))

            time.sleep(15)

        time.sleep(5)

        # click on the button "Mon profile"
        try:
            mon_profile_button = browser.find_element_by_xpath(
                '/html/body/div[3]/div/div[1]/div/div[1]/div[3]/div[1]/button/div/div[2]/div/div/div/div/div/div[2]/img'
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

            time.sleep(5)
        except Exception as e:
            print('error button Mon Profile : ' + str(e))

        browser.quit()
        print('browser.quit()')

        time.sleep(5)

    # ok
    def test_send_several_emails_for_applying_for_financements_machine_gravitationnelle(self):
        print("test_send_several_emails_for_applying_for_financements_machine_gravitationnelle")

        username = ".@outlook.fr"

        password = ""

        emails = [
            "@gmail.com"
        ]

        objet = "Demande de financement pour tester une machine gravitationnelle – Société Holomorphe (Paris)"

        message = """Bonjour,

Suite à notre conversation téléphonique, je vous communique mes coordonnées pour ma demande de financement pour tester ma machine gravitationnelle.

Après, ma machine gravitationnelle est considérée comme une machine à énergie libre pour la production d'électricité.

Les informations de ma machine gravitationnelle sont disponibles au public au lien suivant : https://github.com/Jay4C/Holomorphe_Company/tree/main/Sales_of_digital_contents/Fundamental_researches/Chas_Campbell_Gravitational_Engine

De plus, j'ai trois versions de ma machine gravitationnelle dotée d'une puissance électrique de 10 kilowatts, 100 kilowatts et 1 mégawatt avec un coût respectif de 3000 euros TTC, 9000 euros TTC et 55000 euros TTC.

D'ailleurs, je mets en pièce jointe le chiffrage de la version 1 de ma machine gravitationnelle pour ma demande de financement pour tester ma machine gravitationnelle dotée d'une puissance électrique de 10 kilowatts.

Ma question est : seriez-vous en mesure de financer ma machine gravitationnelle de 10 kilowatts pour confirmer son fonctionnement s'il vous plaît ?

En attendant votre décision, je vous prie de croire, mes sincères salutations.

Monsieur 
Président de la société Holomorphe
Ingénieur généraliste diplômé à l'Ecole Supérieure d'Ingénieurs Léonard de Vinci à Paris La Défense
Adresse du siège social : 31 Avenue de Ségur 75007 Paris
Téléphone : 
Informations générales : https://www.societe.com/societe/holomorphe-883632556.html
YouTube : https://www.youtube.com/channel/UClK7qVMGyLGEE0uPy7LFGlA"""

        file_upload = "C:\\Users\\DELL\\Documents\Outils\Desktop_Automation\\Chiffrage_Machine_Gravitationnelle.xls"

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
        # options = options
        browser = webdriver.Firefox(
            executable_path='..\\..\\geckodriver.exe'
        )

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get('https://outlook.live.com/owa/')
        print("browser.get('https://outlook.live.com/owa/')")

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
        email_input.send_keys(username)
        email_input.send_keys(Keys.ENTER)
        print("email_input inserted")

        time.sleep(5)

        password_input = browser.find_element_by_xpath(
            '//*[@id="i0118"]'
        )
        password_input.clear()
        password_input.send_keys(password)
        password_input.send_keys(Keys.ENTER)
        print("password_input inserted")

        time.sleep(5)

        # click on the checkbox "Ne plus afficher ce message"
        ne_plus_afficher_ce_message_checkbox = browser.find_element_by_xpath(
            '//*[@id="KmsiCheckboxField"]'
        )
        ne_plus_afficher_ce_message_checkbox.click()
        print("ne_plus_afficher_ce_message_checkbox.click()")

        time.sleep(5)

        # click on the button "Non"
        non_button = browser.find_element_by_xpath(
            '//*[@id="idBtn_Back"]'
        )
        non_button.click()
        print("non_button.click()")

        time.sleep(15)

        for email in emails:
            envoye_a = email.lower()

            print('Nouveau courrier pour ' + str(envoye_a))

            # click on the button "Nouveau courrier"
            try:
                nouveau_courrier_button = browser.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div[2]/div[1]/div/div/div[1]/div[1]/div[2]/div/div/button'
                )
                nouveau_courrier_button.click()
                print("nouveau_courrier_button.click()")

                time.sleep(7)
            except Exception as e:
                print('error nouveau_courrier_button : ' + str(e))

            # Insert the email sender
            try:
                envoye_a_input = browser.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div[2]/div[1]/div/div/div[3]/div[2]/div/div[2]/div[1]/div/div/div'
                    '/div[1]/div[1]/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/input'
                )
                envoye_a_input.clear()
                envoye_a_input.send_keys(envoye_a)
                time.sleep(2)
                envoye_a_input.send_keys(Keys.ENTER)
                time.sleep(2)
                envoye_a_input.send_keys(Keys.TAB)
                print("envoye_a_input inserted")

                time.sleep(7)
            except Exception as e:
                print("error envoye_a_input : " + str(e))

            # Insert the subject
            try:
                actions_subject = ActionChains(browser)
                actions_subject.send_keys(objet)
                time.sleep(2)
                actions_subject.send_keys(Keys.TAB)
                actions_subject.perform()
                print("subject_input inserted")
            except Exception as e:
                print('error subject_input : ' + str(e))

            time.sleep(7)

            # Insert the file
            try:
                file_input = browser.find_element_by_xpath(
                    "/html/body/div[3]/div/div[2]/div[2]/div[1]/div/div/div[3]/div[1]/div/span/input[1]"
                )
                file_input.send_keys(
                    file_upload
                )
                print("file_input inserted")
            except Exception as e:
                print('error file_input : ' + str(e))

            time.sleep(15)

            # Insert the message
            try:
                actions_message = ActionChains(browser)
                actions_message.send_keys(message)
                actions_message.perform()
                print("message_input inserted")
            except Exception as e:
                print('error message_input : ' + str(e))

            time.sleep(15)

            # click on the button "Envoyer"
            try:
                actions_envoyer_button = ActionChains(browser)
                actions_envoyer_button.send_keys(Keys.TAB)
                time.sleep(2)
                actions_envoyer_button.send_keys(Keys.TAB)
                time.sleep(2)
                actions_envoyer_button.send_keys(Keys.TAB)
                time.sleep(3)
                actions_envoyer_button.send_keys(Keys.ENTER)
                actions_envoyer_button.perform()
                print("actions_envoyer_button clicked")
            except Exception as e:
                print('error message_input : ' + str(e))

            time.sleep(15)

        time.sleep(5)

        try:
            # click on the button "Mon profile"
            mon_profile_button = browser.find_element_by_xpath(
                '/html/body/div[3]/div/div[1]/div/div[1]/div[3]/div[1]/button/div/div[2]/div/div/div/div/div/div[2]/img'
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

            time.sleep(5)
        except Exception as e:
            print('error Mon profile : ' + str(e))

        browser.quit()
        print('browser.quit()')

        time.sleep(5)

    # ok
    def test_send_several_emails_for_connection_partnership_hydrogen(self):
        print("test_send_several_emails_for_connection_partnership_hydrogen")

        username = ".@outlook.fr"

        password = ""

        emails = [
            "@gmail.com"
        ]

        objet = 'Mise en relation auprès du partenaire de la brique "Méthanation" / Connection with the partner ' \
                'of the brick "Methanation" / '

        message = """Version française :

Bonjour,

Suite à notre dernier échange téléphonique concernant la valorisation du dioxyde de carbone par méthanation, je vous communique un partenaire qui se consacre sur la fabrication de réacteur de méthanation afin de combiner le dioxyde de carbone avec le dihydrogène pour produire du méthane de synthèse suivant la réaction chimique de Sabatier.

La société à contacter est : Société Khimod, filiale du Groupe Alcen / Monsieur Olivier BOUCHARD / 28, Bld Kellermann F-75013 Paris / Tel : +33 (0)1 83 75 92 28 / 'obouchard@khimod.com', / khimod.com

De plus, je travaille sur une machine gravitationnelle pour la production d'électricité sans émission de gaz à effet et non intermittente et ma machine gravitationnelle se base sur les brevets suivants :
Brevet FR2717240A1 intitulé "Dispositif de transmission d’énergie gravitationnelle à un système de production d’énergie mécanique ou électrique" dont l'inventeur est Poirier Gerard Francois Pierre.
Brevet FR2461125A1 intitulé "Moteur gravitationnel produisant de l’énergie en utilisant des poids déséquilibrés glissant sur des supports radiaux pour créer un mouvement rotatif perpétuel" dont l'inventeur est Piens Marc.
Brevet WO1982004174A2 intitulé "Mouvement perpétuel"dont l'inventeur est Johann dit Jean Schyns.
Brevet US3625089A intitulé "Appareil à roue gravitationnelle"dont l'inventeur est Edward Rutkove.

Je mets en pièce jointe un diagramme de partenariat pour la valorisation du dioxyde de carbone par méthanation.

Théoriquement pour pouvoir convertir une tonne de dioxyde de carbone par an en méthane de synthèse, il faut produire environ 500 mètres cubes de dihydrogène gazeux par heure.

Mes questions sont :
Pouvez-vous me donner l'énergie consommée par votre générateur d'hydrogène pour produire un mètre cube de dihydrogène gazeux par heure s'il vous plaît ?
Pouvez-vous me donner la surface et la hauteur nécessaire pour installer votre générateur d'hydrogène pour produire un mètre cube de dihydrogène gazeux par heure s'il vous plaît ?
Avez-vous des partenaires pour valoriser le dioxygène produit par votre générateur d'hydrogène s'il vous plaît ?

Dans l'attente de votre retour, je vous prie de croire, mes sincères salutations.


Président de la société Holomorphe
Ingénieur généraliste diplômé à l'Ecole Supérieure d'Ingénieurs Léonard de Vinci à Paris La Défense
Adresse du siège social : 31 Avenue de Ségur 75007 Paris
Téléphone : 
SIREN : 883632556
GitHub : Jay4C

English version :

Hello,

Following our last telephone exchange concerning the valorization of carbon dioxide by methanation, I am giving you a partner who is dedicated to the manufacture of methanation reactor in order to combine carbon dioxide with dihydrogen to produce synthetic methane according to the chemical reaction of Sabatier.

The company to contact is: Khimod company, a subsidiary of the Alcen group / Mr. Olivier Bouchard / 28, BLD Kellermann F-75013 Paris / Tel: +33 (0) 1 83 75 92 28 / 'obouchard@khimod.com', / khimod.com

In addition, I work on a gravitational machine for the production of electricity without any emission of greenhouse gases and operational every day without stop, and my gravitational machine is based on the following patents:
Patent FR2717240A1 entitled "Gravitational energy transmission device to a mechanical or electrical energy production system" whose the inventor is Poirier Gerard Francois Pierre.
Patent FR2461125A1 entitled "Gravitational motor producing energy using unbalanced weights slipping on radial supports to create a perpetual rotary movement" whose the inventor is Piens Marc.
Patent WO1982004174A2 entitled "Perpetual movement" whose the inventor is Johann says Jean Schyns.
Patent US3625089A entitled "Gravitational wheel device" whose the inventor is Edward Rutkove.

I attached a partnership diagram for the valorization of carbon dioxide by methanation.

Theoretically to be able to convert a ton of carbon dioxide per year in synthetic methane, about 500 cubic meters of gaseous dihydrogen per hour must be produced.

My questions are:
Can you give me the energy consumed by your hydrogen generator to produce a cubic meter of gaseous dihydrogen per hour please ?
Can you give me the surface and the height required to install your hydrogen generator to produce a cubic meter of gaseous dihydrogen per hour please ?
Do you have partners to value the oxygen produced by your hydrogen generator please ?

Looking forward to your return, I beg you to believe, my sincere greetings.


President of the company Holomorphe
General engineer graduated at the School of Engineers Leonard de Vinci in Paris La Defense
Head office address: 31 Avenue de Ségur 75007 Paris
Phone: 00.33.7.45.75.27.00
SIREN: 883632556
GitHub: Jay4C"""

        file_upload = "C:\\Users\\DELL\\Documents\\Outils\\Desktop_Automation\\Partenaires_Syngas_English.png"

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
            executable_path='..\\..\\geckodriver.exe'
        )

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get('https://outlook.live.com/owa/')
        print("browser.get('https://outlook.live.com/owa/')")

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
        email_input.send_keys(username)
        email_input.send_keys(Keys.ENTER)
        print("email_input inserted")

        time.sleep(7)

        password_input = browser.find_element_by_xpath(
            '//*[@id="i0118"]'
        )
        password_input.clear()
        password_input.send_keys(password)
        password_input.send_keys(Keys.ENTER)
        print("password_input inserted")

        time.sleep(7)

        # click on the checkbox "Ne plus afficher ce message"
        ne_plus_afficher_ce_message_checkbox = browser.find_element_by_xpath(
            '//*[@id="KmsiCheckboxField"]'
        )
        ne_plus_afficher_ce_message_checkbox.click()
        print("ne_plus_afficher_ce_message_checkbox.click()")

        time.sleep(5)

        # click on the button "Non"
        non_button = browser.find_element_by_xpath(
            '//*[@id="idBtn_Back"]'
        )
        non_button.click()
        print("non_button.click()")

        time.sleep(15)

        for email in emails:
            envoye_a = email.lower()

            print('Nouveau courrier pour ' + str(envoye_a))

            # click on the button "Nouveau courrier"
            nouveau_courrier_button = browser.find_element_by_xpath(
                '/html/body/div[3]/div/div[2]/div[2]/div[1]/div/div/div/div/div/div[1]/div[2]/div/div/button'
            )
            nouveau_courrier_button.click()
            print("nouveau_courrier_button.click()")

            time.sleep(7)

            # Insert the email sender
            try:
                envoye_a_input = browser.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div[2]/div[1]/div/div/div[3]/div[2]/div/div[2]/div[1]/div/div/div'
                    '/div[1]/div[1]/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/input'
                )
                envoye_a_input.clear()
                envoye_a_input.send_keys(envoye_a)
                time.sleep(2)
                envoye_a_input.send_keys(Keys.ENTER)
                time.sleep(2)
                envoye_a_input.send_keys(Keys.TAB)
                print("envoye_a_input inserted")
            except Exception as e:
                print("error envoye_a_input : " + str(e))

            time.sleep(7)

            # Insert the subject
            try:
                actions_subject = ActionChains(browser)
                actions_subject.send_keys(objet)
                time.sleep(2)
                actions_subject.send_keys(Keys.TAB)
                actions_subject.perform()
                print("subject_input inserted")
            except Exception as e:
                print('error subject_input : ' + str(e))

            time.sleep(7)

            # Insert the file
            try:
                file_input = browser.find_element_by_xpath(
                    "/html/body/div[3]/div/div[2]/div[2]/div[1]/div/div/div[3]/div[1]/div/span/input[1]"
                )
                file_input.send_keys(
                    file_upload
                )
                print("file_input inserted")
            except Exception as e:
                print('error file_input : ' + str(e))

            time.sleep(15)

            # Insert the message
            try:
                actions_message = ActionChains(browser)
                actions_message.send_keys(message)
                actions_message.perform()
                print("message_input inserted")
            except Exception as e:
                print('error message_input : ' + str(e))

            time.sleep(7)

            # click on the button "Envoyer"
            try:
                actions_envoyer = ActionChains(browser)
                time.sleep(1)
                actions_envoyer.send_keys(Keys.TAB)
                time.sleep(1)
                actions_envoyer.send_keys(Keys.TAB)
                time.sleep(3)
                actions_envoyer.send_keys(Keys.ENTER)
                actions_envoyer.perform()
                print("envoyer_button.click()")
            except Exception as e:
                print('error envoyer_button : ' + str(e))

            time.sleep(15)

        time.sleep(5)

        # click on the button "Mon profile"
        try:
            mon_profile_button = browser.find_element_by_xpath(
                '/html/body/div[3]/div/div[1]/div/div[1]/div[3]/div[1]/button/div/div[2]/div/div/div/div/div/div[2]/img'
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

            time.sleep(5)
        except Exception as e:
            print('error button Mon Profile : ' + str(e))

        browser.quit()
        print('browser.quit()')

        time.sleep(5)


class UnitTestsWebAutomationOutlookWithHeadlessForSendingEmailsForBusinessInCO2(unittest.TestCase):
    # ok
    def test_send_several_emails_for_demande_partenariat_valorisation_co2(self):
        print("test_send_several_emails_for_demande_partenariat_valorisation_co2")

        username = ".@outlook.fr"

        password = ""

        emails = [
            "jay1993izi@gmail.com"
        ]

        objet = "Demande de partenariat pour la valorisation du dioxyde de carbone par méthanation – Société Holomorphe (Paris)"

        message = """Bonjour,

Je vous communique mes coordonnées pour ma demande de partenariat pour la valorisation du dioxyde de carbone par méthanation.

Après, la production de méthane de synthèse sera vendue aux fournisseurs de gaz naturel par le biais du réseau de gaz naturel, et la vente de cette production sera répartie équitablement entre les partenaires du projet quel que soit leur niveau d'investissement.

Puis, je travaille sur une machine gravitationnelle considérée comme une machine à énergie libre pour la production d'électricité.

Ensuite, je mets en pièce jointe les informations de ma machine gravitationnelle et le concept de la valorisation du dioxyde de carbone par méthanation.

Ainsi, j'aurai besoin de savoir la quantité de dioxyde de carbone émise dans l'atmosphère depuis vos installations pour calculer la puissance électrique nécessaire du projet et sa rentabilité, et j'aurai également besoin d'obtenir la surface d'occupation disponible de vos installations pour installer les différentes briques technologiques (machine gravitationnelle, générateur à eau atmosphérique, générateur d'hydrogène gazeux, générateur de dioxyde de carbone atmosphérique, réacteur de méthanation ...).

Mes questions sont :
Quelle est la quantité totale annuelle de dioxyde de carbone émise par vos installations s'il vous plaît ?
Quelle est la surface d'occupation disponible de vos installations pour installer les différentes briques technologiques s'il vous plaît ?

En attendant votre décision, je vous prie de croire, mes sincères salutations.


Président de la société Holomorphe
Ingénieur généraliste diplômé à l'Ecole Supérieure d'Ingénieurs Léonard de Vinci à Paris La Défense
Adresse du siège social : 31 Avenue de Ségur 75007 Paris
Téléphone : 
Numéro SIREN de la société Holomorphe : 883632556"""

        file_upload = "C:\\Users\\DELL\\Documents\\Outils\\Desktop_Automation\\Informations_Projet_Methanation.xls"

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
            executable_path='..\\..\\geckodriver.exe'
        )

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get('https://outlook.live.com/owa/')
        print("browser.get('https://outlook.live.com/owa/')")

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
        email_input.send_keys(username)
        email_input.send_keys(Keys.ENTER)
        print("email_input inserted")

        time.sleep(5)

        password_input = browser.find_element_by_xpath(
            '//*[@id="i0118"]'
        )
        password_input.clear()
        password_input.send_keys(password)
        password_input.send_keys(Keys.ENTER)
        print("password_input inserted")

        time.sleep(5)

        # click on the checkbox "Ne plus afficher ce message"
        ne_plus_afficher_ce_message_checkbox = browser.find_element_by_xpath(
            '//*[@id="KmsiCheckboxField"]'
        )
        ne_plus_afficher_ce_message_checkbox.click()
        print("ne_plus_afficher_ce_message_checkbox.click()")

        time.sleep(5)

        # click on the button "Non"
        non_button = browser.find_element_by_xpath(
            '//*[@id="idBtn_Back"]'
        )
        non_button.click()
        print("non_button.click()")

        time.sleep(15)

        for email in emails:
            envoye_a = email.lower()

            print('Nouveau courrier pour ' + str(envoye_a))

            # click on the button "Nouveau courrier"
            nouveau_courrier_button = browser.find_element_by_xpath(
                '/html/body/div[3]/div/div[2]/div[2]/div[1]/div/div/div[1]/div[1]/div[2]/div/div/button'
            )
            nouveau_courrier_button.click()
            print("nouveau_courrier_button.click()")

            time.sleep(7)

            # Insert the email sender
            try:
                envoye_a_input = browser.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div[2]/div[1]/div/div/div[3]/div[2]/div/div[2]/div[1]/div/div/div'
                    '/div[1]/div[1]/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/input'
                )
                envoye_a_input.clear()
                envoye_a_input.send_keys(envoye_a)
                time.sleep(2)
                envoye_a_input.send_keys(Keys.ENTER)
                time.sleep(2)
                envoye_a_input.send_keys(Keys.TAB)
                print("envoye_a_input inserted")
            except Exception as e:
                print("error envoye_a_input : " + str(e))

            time.sleep(7)

            # Insert the subject
            try:
                actions_subject = ActionChains(browser)
                actions_subject.send_keys(objet)
                time.sleep(2)
                actions_subject.send_keys(Keys.TAB)
                actions_subject.perform()
                print("subject_input inserted")
            except Exception as e:
                print('error subject_input : ' + str(e))

            time.sleep(7)

            # Insert the file
            try:
                file_input = browser.find_element_by_xpath(
                    "/html/body/div[3]/div/div[2]/div[2]/div[1]/div/div/div[3]/div[1]/div/span/input[1]"
                )
                file_input.send_keys(
                    file_upload
                )
                print("file_input inserted")
            except Exception as e:
                print('error file_input : ' + str(e))

            time.sleep(15)

            # Insert the message
            try:
                actions_message = ActionChains(browser)
                actions_message.send_keys(message)
                actions_message.perform()
                print("message_input inserted")
            except Exception as e:
                print('error message_input : ' + str(e))

            time.sleep(7)

            # click on the button "Envoyer"
            try:
                actions_envoyer = ActionChains(browser)
                time.sleep(1)
                actions_envoyer.send_keys(Keys.TAB)
                time.sleep(1)
                actions_envoyer.send_keys(Keys.TAB)
                time.sleep(3)
                actions_envoyer.send_keys(Keys.ENTER)
                actions_envoyer.perform()
                print("envoyer_button.click()")
            except Exception as e:
                print('error envoyer_button : ' + str(e))

            time.sleep(15)

        time.sleep(5)

        # click on the button "Mon profile"
        try:
            mon_profile_button = browser.find_element_by_xpath(
                '/html/body/div[3]/div/div[1]/div/div[1]/div[3]/div[1]/button/div/div[2]/div/div/div/div/div/div[2]/img'
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

            time.sleep(5)
        except Exception as e:
            print('error button Mon Profile : ' + str(e))

        browser.quit()
        print('browser.quit()')

        time.sleep(5)

    # ok
    def test_send_several_emails_for_request_carbon_credits(self):
        print("test_send_several_emails_for_request_carbon_credits")

        username = ".@outlook.fr"

        password = ""

        """
        "@gmail.com"
        """

        emails = [
        ]

        objet = "Request for carbon credits - Holomorphe company"

        message = """Good morning,

Today, I am working on two kind of projects by removing carbone dioxide from air.

The first type of project is the valorization of carbone dioxide by producing synthetic methane, and the second type of project is the carbon dioxide sequestration.

My question is :
Does your organization certify these two kind of projects for the removal of carbon dioxide from air in order to deliver carbon credits for my company please ?

While waiting for your answer, please believe, my sincere greetings.


President of the Holomorphe company
General engineer graduated from the Leonardo da Vinci School of Engineering in Paris La Défense
Headquarters address: 31 Avenue de Ségur 75007 Paris
SIREN : 883632556
Telephone : 
Github : Jay4C"""

        time.sleep(5)

        warnings.filterwarnings(
            action="ignore",
            message="unclosed",
            category=ResourceWarning
        )

        time.sleep(5)

        # with Firefox
        options = Options()
        options.headless = True
        browser = webdriver.Firefox(
            executable_path='..\\..\\geckodriver.exe',
            options=options
        )

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get('https://outlook.live.com/owa/')
        print("browser.get('https://outlook.live.com/owa/')")

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
        email_input.send_keys(username)
        email_input.send_keys(Keys.ENTER)
        print("email_input inserted")

        time.sleep(5)

        password_input = browser.find_element_by_xpath(
            '//*[@id="i0118"]'
        )
        password_input.clear()
        password_input.send_keys(password)
        password_input.send_keys(Keys.ENTER)
        print("password_input inserted")

        time.sleep(5)

        # click on the checkbox "Ne plus afficher ce message"
        ne_plus_afficher_ce_message_checkbox = browser.find_element_by_xpath(
            '//*[@id="KmsiCheckboxField"]'
        )
        ne_plus_afficher_ce_message_checkbox.click()
        print("ne_plus_afficher_ce_message_checkbox.click()")

        time.sleep(5)

        # click on the button "Non"
        non_button = browser.find_element_by_xpath(
            '//*[@id="idBtn_Back"]'
        )
        non_button.click()
        print("non_button.click()")

        time.sleep(15)

        for email in emails:
            envoye_a = email.lower()

            print('Nouveau courrier pour ' + str(envoye_a))

            # click on the button "Nouveau courrier"
            nouveau_courrier_button = browser.find_element_by_xpath(
                '/html/body/div[3]/div/div[2]/div[2]/div[1]/div/div/div[1]/div[1]/div[2]/div/div/button'
            )
            nouveau_courrier_button.click()
            print("nouveau_courrier_button.click()")

            time.sleep(7)

            # Insert the email sender
            try:
                envoye_a_input = browser.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div[2]/div[1]/div/div/div[3]/div[2]/div/div[2]/div[1]/div/div/div'
                    '/div[1]/div[1]/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/input'
                )
                envoye_a_input.clear()
                envoye_a_input.send_keys(envoye_a)
                time.sleep(2)
                envoye_a_input.send_keys(Keys.ENTER)
                time.sleep(2)
                envoye_a_input.send_keys(Keys.TAB)
                print("envoye_a_input inserted")
            except Exception as e:
                print("error envoye_a_input : " + str(e))

            time.sleep(7)

            # Insert the subject
            try:
                actions_subject = ActionChains(browser)
                actions_subject.send_keys(objet)
                time.sleep(2)
                actions_subject.send_keys(Keys.TAB)
                actions_subject.perform()
                print("subject_input inserted")
            except Exception as e:
                print('error subject_input : ' + str(e))

            time.sleep(7)

            # Insert the message
            try:
                actions_message = ActionChains(browser)
                actions_message.send_keys(message)
                actions_message.perform()
                print("message_input inserted")
            except Exception as e:
                print('error message_input : ' + str(e))

            time.sleep(7)

            # click on the button "Envoyer"
            try:
                actions_envoyer = ActionChains(browser)
                time.sleep(1)
                actions_envoyer.send_keys(Keys.TAB)
                time.sleep(1)
                actions_envoyer.send_keys(Keys.TAB)
                time.sleep(3)
                actions_envoyer.send_keys(Keys.ENTER)
                actions_envoyer.perform()
                print("envoyer_button.click()")
            except Exception as e:
                print('error envoyer_button : ' + str(e))

            time.sleep(15)

        time.sleep(5)

        # click on the button "Mon profile"
        try:
            mon_profile_button = browser.find_element_by_xpath(
                '/html/body/div[3]/div/div[1]/div/div[1]/div[3]/div[1]/button/div/div[2]/div/div/div/div/div/div[2]/img'
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

            time.sleep(5)
        except Exception as e:
            print('error button Mon Profile : ' + str(e))

        browser.quit()
        print('browser.quit()')

        time.sleep(5)

    # ok
    def test_send_several_emails_for_artificial_sequestration_of_co2(self):
        print("test_send_several_emails_for_artificial_sequestration_of_co2")

        username = ".@outlook.fr"

        password = ""

        # jay1993izi@gmail.com

        emails = [
        ]

        objet = 'Request for partnership for the artificial sequestration of carbone dioxide for selling carbon ' \
                'credits – Holomorphe company'

        message = """Hello,

I am looking for a partnership with your company for capturing carbon dioxide from air in order to sequestrate carbone dioxide into big tanks with a length of one kilometer and a diameter of 2.16 meters. The big tanks will be vertically buried into the soil, and we need approximately an area of 150 square kilometers to sequestrate 10 billions tons of carbone dioxide.

With a price of one carbone credit at 100 euros per ton of carbone dioxide buried permanently into the soil, we can reach 1 trillion euros for sequestrating 10 billions tons of carbone dioxide permanently into the soil.

In addition, I work on a gravitational machine for the production of electricity without any emission of greenhouse gases and operational every day without stop, and my gravitational machine is based on the following patents:
Patent FR2717240A1 entitled "Gravitational energy transmission device to a mechanical or electrical energy production system" whose the inventor is Poirier Gerard Francois Pierre.
Patent FR2461125A1 entitled "Gravitational engine producing energy using unbalanced weights slipping on radial supports to create a perpetual rotary movement" whose the inventor is Piens Marc.
Patent WO1982004174A2 entitled "Perpetual movement" whose the inventor is Johann says Jean Schyns.
Patent US3625089A entitled "Gravitational wheel device" whose the inventor is Edward Rutkove.

Besides, I advise that we should work together in a country that doesn't require a license for producing electricity for our internal needs with any amout of electrical power and primary energy source of the power plant and has not the death penalty, and I listed these countries :
Africa (South africa, Mozambique, Namibia)
Asia (Armenia, Cambodia, Georgia, Kazakhstan, Uzbekistan)
Europe (Albania, Roumania, Finland, Montenegro, Czech Republic, Switzerland, Kosovo)
Oceania (Nauru, New-Zeland, Samoa, Vanuatu)
America (Argentina, Chile, Dominican republic, Ecuador, Cayman islands, British virgin islands, Anguilla, Montserrat)

I am open to new ideas, and I am also looking for one or two associate(s) for setting up a non-profit organization in Switzerland exempt from corporation tax for the protection of environment by creating a volontary carbone market with our own methodologies and protocols based on the artificial sequestration of carbone dioxide in order to issue carbon credits by ourselves for our projects.

My question is :
Can you develop a direct air capture technology with a performance of one million tons of carbone dioxide captured from air per year please ?

Looking forward to your return, I beg you to believe, my sincere greetings.


President of the company Holomorphe
General engineer graduated at the School of Engineers Leonard de Vinci in Paris La Defense
Head office address: 31 Avenue de Ségur 75007 Paris
Phone : 
Siren : 883632556
GitHub : Jay4C"""

        time.sleep(5)

        warnings.filterwarnings(
            action="ignore",
            message="unclosed",
            category=ResourceWarning
        )

        time.sleep(5)

        # with Firefox
        options = Options()
        options.headless = True
        browser = webdriver.Firefox(
            executable_path='..\\..\\geckodriver.exe',
            options=options
        )

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get('https://outlook.live.com/owa/')
        print("browser.get('https://outlook.live.com/owa/')")

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
        email_input.send_keys(username)
        email_input.send_keys(Keys.ENTER)
        print("email_input inserted")

        time.sleep(5)

        password_input = browser.find_element_by_xpath(
            '//*[@id="i0118"]'
        )
        password_input.clear()
        password_input.send_keys(password)
        password_input.send_keys(Keys.ENTER)
        print("password_input inserted")

        time.sleep(5)

        # click on the checkbox "Ne plus afficher ce message"
        ne_plus_afficher_ce_message_checkbox = browser.find_element_by_xpath(
            '//*[@id="KmsiCheckboxField"]'
        )
        ne_plus_afficher_ce_message_checkbox.click()
        print("ne_plus_afficher_ce_message_checkbox.click()")

        time.sleep(5)

        # click on the button "Non"
        non_button = browser.find_element_by_xpath(
            '//*[@id="idBtn_Back"]'
        )
        non_button.click()
        print("non_button.click()")

        time.sleep(15)

        for email in emails:
            envoye_a = email.lower()

            print('Nouveau courrier pour ' + str(envoye_a))

            # click on the button "Nouveau courrier"
            nouveau_courrier_button = browser.find_element_by_xpath(
                '/html/body/div[3]/div/div[2]/div[2]/div[1]/div/div/div[1]/div[1]/div[2]/div/div/button'
            )
            nouveau_courrier_button.click()
            print("nouveau_courrier_button.click()")

            time.sleep(7)

            # Insert the email sender
            try:
                envoye_a_input = browser.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div[2]/div[1]/div/div/div[3]/div[2]/div/div[2]/div[1]/div/div/div'
                    '/div[1]/div[1]/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/input'
                )
                envoye_a_input.clear()
                envoye_a_input.send_keys(envoye_a)
                time.sleep(2)
                envoye_a_input.send_keys(Keys.ENTER)
                time.sleep(2)
                envoye_a_input.send_keys(Keys.TAB)
                print("envoye_a_input inserted")
            except Exception as e:
                print("error envoye_a_input : " + str(e))

            time.sleep(7)

            # Insert the subject
            try:
                actions_subject = ActionChains(browser)
                actions_subject.send_keys(objet)
                time.sleep(2)
                actions_subject.send_keys(Keys.TAB)
                actions_subject.perform()
                print("subject_input inserted")
            except Exception as e:
                print('error subject_input : ' + str(e))

            time.sleep(7)

            # Insert the message
            try:
                actions_message = ActionChains(browser)
                actions_message.send_keys(message)
                actions_message.perform()
                print("message_input inserted")
            except Exception as e:
                print('error message_input : ' + str(e))

            time.sleep(7)

            # click on the button "Envoyer"
            try:
                actions_envoyer = ActionChains(browser)
                time.sleep(1)
                actions_envoyer.send_keys(Keys.TAB)
                time.sleep(1)
                actions_envoyer.send_keys(Keys.TAB)
                time.sleep(3)
                actions_envoyer.send_keys(Keys.ENTER)
                actions_envoyer.perform()
                print("envoyer_button.click()")
            except Exception as e:
                print('error envoyer_button : ' + str(e))

            time.sleep(15)

        time.sleep(5)

        # click on the button "Mon profile"
        try:
            mon_profile_button = browser.find_element_by_xpath(
                '/html/body/div[3]/div/div[1]/div/div[1]/div[3]/div[1]/button/div/div[2]/div/div/div/div/div/div[2]/img'
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

            time.sleep(5)
        except Exception as e:
            print('error button Mon Profile : ' + str(e))

        browser.quit()
        print('browser.quit()')

        time.sleep(5)

    # ok
    def test_send_several_emails_for_producing_diamonds_from_co2(self):
        print("test_send_several_emails_for_producing_diamonds_from_co2")

        username = ".@outlook.fr"

        password = ""

        # jay1993izi@gmail.com

        emails = [
        ]

        objet = 'Request about your technology for producing diamonds from carbone dioxide - Holomorphe company'

        message = """Hello,

I am looking for a partnership with your company for capturing carbon dioxide from air in order to produce saleable diamonds in laboratory.

In addition, I work on a gravitational machine for the production of electricity without any emission of greenhouse gases and operational every day without stop, and my gravitational machine is based on the following patents:
Patent FR2717240A1 entitled "Gravitational energy transmission device to a mechanical or electrical energy production system" whose the inventor is Poirier Gerard Francois Pierre.
Patent FR2461125A1 entitled "Gravitational engine producing energy using unbalanced weights slipping on radial supports to create a perpetual rotary movement" whose the inventor is Piens Marc.
Patent WO1982004174A2 entitled "Perpetual movement" whose the inventor is Johann says Jean Schyns.
Patent US3625089A entitled "Gravitational wheel device" whose the inventor is Edward Rutkove.

Then, I would like to power your technology with electricity for free and earn money from our partnership by selling diamonds produced from thin air and carbone credits with a volontary carbone market.

My questions are :
How many carats of saleable diamonds could we produce per hour with your technology and the amount of energy needed please ?
How many carats of saleable diamonds could we sell per month and the average amount of monthly turnover please ?

Looking forward to your return, I beg you to believe, my sincere greetings.


President of the company Holomorphe
General engineer graduated at the School of Engineers Leonard de Vinci in Paris La Defense
Head office address: 31 Avenue de Ségur 75007 Paris
Phone : 
Siren : 883632556
GitHub : Jay4C"""

        time.sleep(5)

        warnings.filterwarnings(
            action="ignore",
            message="unclosed",
            category=ResourceWarning
        )

        time.sleep(5)

        # with Firefox
        options = Options()
        options.headless = True
        browser = webdriver.Firefox(
            executable_path='..\\..\\geckodriver.exe',
            options=options
        )

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get('https://outlook.live.com/owa/')
        print("browser.get('https://outlook.live.com/owa/')")

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
        email_input.send_keys(username)
        email_input.send_keys(Keys.ENTER)
        print("email_input inserted")

        time.sleep(5)

        password_input = browser.find_element_by_xpath(
            '//*[@id="i0118"]'
        )
        password_input.clear()
        password_input.send_keys(password)
        password_input.send_keys(Keys.ENTER)
        print("password_input inserted")

        time.sleep(5)

        # click on the checkbox "Ne plus afficher ce message"
        ne_plus_afficher_ce_message_checkbox = browser.find_element_by_xpath(
            '//*[@id="KmsiCheckboxField"]'
        )
        ne_plus_afficher_ce_message_checkbox.click()
        print("ne_plus_afficher_ce_message_checkbox.click()")

        time.sleep(5)

        # click on the button "Non"
        non_button = browser.find_element_by_xpath(
            '//*[@id="idBtn_Back"]'
        )
        non_button.click()
        print("non_button.click()")

        time.sleep(15)

        for email in emails:
            envoye_a = email.lower()

            print('Nouveau courrier pour ' + str(envoye_a))

            # click on the button "Nouveau courrier"
            nouveau_courrier_button = browser.find_element_by_xpath(
                '/html/body/div[3]/div/div[2]/div[2]/div[1]/div/div/div[1]/div[1]/div[2]/div/div/button'
            )
            nouveau_courrier_button.click()
            print("nouveau_courrier_button.click()")

            time.sleep(7)

            # Insert the email sender
            try:
                envoye_a_input = browser.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div[2]/div[1]/div/div/div[3]/div[2]/div/div[2]/div[1]/div/div/div'
                    '/div[1]/div[1]/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/input'
                )
                envoye_a_input.clear()
                envoye_a_input.send_keys(envoye_a)
                time.sleep(2)
                envoye_a_input.send_keys(Keys.ENTER)
                time.sleep(2)
                envoye_a_input.send_keys(Keys.TAB)
                print("envoye_a_input inserted")
            except Exception as e:
                print("error envoye_a_input : " + str(e))

            time.sleep(7)

            # Insert the subject
            try:
                actions_subject = ActionChains(browser)
                actions_subject.send_keys(objet)
                time.sleep(2)
                actions_subject.send_keys(Keys.TAB)
                actions_subject.perform()
                print("subject_input inserted")
            except Exception as e:
                print('error subject_input : ' + str(e))

            time.sleep(7)

            # Insert the message
            try:
                actions_message = ActionChains(browser)
                actions_message.send_keys(message)
                actions_message.perform()
                print("message_input inserted")
            except Exception as e:
                print('error message_input : ' + str(e))

            time.sleep(7)

            # click on the button "Envoyer"
            try:
                actions_envoyer = ActionChains(browser)
                time.sleep(1)
                actions_envoyer.send_keys(Keys.TAB)
                time.sleep(1)
                actions_envoyer.send_keys(Keys.TAB)
                time.sleep(3)
                actions_envoyer.send_keys(Keys.ENTER)
                actions_envoyer.perform()
                print("envoyer_button.click()")
            except Exception as e:
                print('error envoyer_button : ' + str(e))

            time.sleep(15)

        time.sleep(5)

        # click on the button "Mon profile"
        try:
            mon_profile_button = browser.find_element_by_xpath(
                '/html/body/div[3]/div/div[1]/div/div[1]/div[3]/div[1]/button/div/div[2]/div/div/div/div/div/div[2]/img'
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

            time.sleep(5)
        except Exception as e:
            print('error button Mon Profile : ' + str(e))

        browser.quit()
        print('browser.quit()')

        time.sleep(5)

    # ok
    def test_send_several_emails_for_partnership_for_selling_carbon_credits(self):
        print("test_send_several_emails_for_partnership_for_selling_carbon_credits")

        # with Firefox
        options = Options()
        options.headless = False

        username = ".@outlook.fr"

        password = ""

        # @gmail.com

        emails = [
            '@gmail.com'
        ]

        objet = 'Request for a partnership for selling carbon credits by removing CO2 from thin air - Holomorphe company'

        message = """Hello,

Actually, I am looking for a partnership with your company for capturing carbon dioxide from air in order to sell carbon credits.

Today, I am working on an innovative technology for producing electricity by using permanent magnets without greenhouse gases emmissions.

After, I would like to power your technology with electricity for free and earn money from our partnership by selling carbone credits into a volontary carbone market.

My questions are :
How many tons of carbon dioxide can your technology extract per year please (tons/year of CO2) ?
How many electrical powers does your technology need to operate please (watts/ton/year) ?
How many square meters does your technology need to be installed please (m^2/ton/year) ?
What is the height of your technology please (meter) ?
What does your technology do with carbon dioxide (bricks, chemical products ...) ?

Looking forward to your return, I beg you to believe, my sincere greetings.


President of the company Holomorphe
General engineer graduated at the School of Engineers Leonard de Vinci in Paris La Defense
Head office address: 31 Avenue de Ségur 75007 Paris
Phone : 
Siren : 883632556
GitHub : Jay4C
LinkedIn : """

        time.sleep(5)

        warnings.filterwarnings(
            action="ignore",
            message="unclosed",
            category=ResourceWarning
        )

        time.sleep(5)

        browser = webdriver.Firefox(
            executable_path='..\\..\\geckodriver.exe',
            options=options
        )

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get('https://outlook.live.com/owa/')
        print("browser.get('https://outlook.live.com/owa/')")

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
        email_input.send_keys(username)
        email_input.send_keys(Keys.ENTER)
        print("email_input inserted")

        time.sleep(5)

        password_input = browser.find_element_by_xpath(
            '//*[@id="i0118"]'
        )
        password_input.clear()
        password_input.send_keys(password)
        password_input.send_keys(Keys.ENTER)
        print("password_input inserted")

        time.sleep(5)

        # click on the checkbox "Ne plus afficher ce message"
        ne_plus_afficher_ce_message_checkbox = browser.find_element_by_xpath(
            '//*[@id="KmsiCheckboxField"]'
        )
        ne_plus_afficher_ce_message_checkbox.click()
        print("ne_plus_afficher_ce_message_checkbox.click()")

        time.sleep(5)

        # Click on the button "Non"
        non_button = browser.find_element_by_xpath(
            '//*[@id="idBtn_Back"]'
        )
        non_button.click()
        print("non_button.click()")

        time.sleep(15)

        for email in emails:
            envoye_a = email.lower()

            print('Nouveau courrier pour ' + str(envoye_a))

            # click on the button "Nouveau courrier"
            nouveau_courrier_button = browser.find_element_by_xpath(
                '/html/body/div[3]/div/div[2]/div[2]/div[1]/div/div/div/div/div/div[1]/div[2]/div/div/button'
            )
            nouveau_courrier_button.click()
            print("nouveau_courrier_button.click()")

            time.sleep(7)

            # Insert the email sender
            try:
                actions_email = ActionChains(browser)
                time.sleep(3)
                actions_email.send_keys(email)
                time.sleep(3)
                actions_email.send_keys(Keys.ENTER)
                time.sleep(3)
                actions_email.send_keys(Keys.TAB)
                time.sleep(3)
                actions_email.perform()
                print("email_input inserted")
            except Exception as e:
                print('error email_input : ' + str(e))

            time.sleep(7)

            # Insert the subject
            try:
                actions_subject = ActionChains(browser)
                time.sleep(3)
                actions_subject.send_keys(objet)
                time.sleep(3)
                actions_subject.send_keys(Keys.TAB)
                time.sleep(3)
                actions_subject.perform()
                print("subject_input inserted")
            except Exception as e:
                print('error subject_input : ' + str(e))

            time.sleep(7)

            # Insert the message
            try:
                actions_message = ActionChains(browser)
                time.sleep(3)
                actions_message.send_keys(message)
                time.sleep(3)
                actions_message.perform()
                print("message_input inserted")
            except Exception as e:
                print('error message_input : ' + str(e))

            time.sleep(7)

            # click on the button "Envoyer"
            try:
                actions_envoyer = ActionChains(browser)
                time.sleep(3)
                actions_envoyer.send_keys(Keys.TAB)
                time.sleep(3)
                actions_envoyer.send_keys(Keys.TAB)
                time.sleep(3)
                actions_envoyer.send_keys(Keys.TAB)
                time.sleep(3)
                actions_envoyer.send_keys(Keys.ENTER)
                actions_envoyer.perform()
                print("envoyer_button.click()")
            except Exception as e:
                print('error envoyer_button : ' + str(e))

            time.sleep(15)

        time.sleep(5)

        # click on the button "Mon profile"
        try:
            mon_profile_button = browser.find_element_by_xpath(
                '/html/body/div[3]/div/div[1]/div/div[1]/div[3]/div[1]/button/div/div[2]/div/div/div/div/div/div[2]/img'
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

            time.sleep(5)
        except Exception as e:
            print('error button Mon Profile : ' + str(e))

        browser.quit()
        print('browser.quit()')

        time.sleep(5)

    # ok
    def test_send_several_emails_for_request_to_be_part_in_a_voluntary_carbon_market(self):
        print("test_send_several_emails_for_request_to_be_part_in_a_voluntary_carbon_market")

        # with Firefox
        options = Options()
        options.headless = True

        username = ".@outlook.fr"

        password = ""

        """
        "@gmail.com"
        """

        emails = [

        ]

        objet = "Request for a registration in your voluntary carbon market as a project leader - Holomorphe company"

        message = """Hello,

Today, I am working on projects for removing carbon dioxide from thin air with ready-to-use technologies built by my partners, and the goal of the partnership between my company and my partners is to sell carbon credits in a voluntary carbon market.

Actually, I am building an innovative technology for producing electricity by harnessing magnetic energy from permanent magnets without greenhouse gases emmissions.

Besides, the locations of the projects will certainly be in the following countries :
Africa (South africa, Mozambique, Namibia)
Asia (Armenia, Cambodia, Georgia, Kazakhstan, Uzbekistan)
Europe (Albania, Romania, Finland, Montenegro, Czech Republic, Switzerland, Kosovo, Jersey)
Oceania (Nauru, New Zealand, Samoa, Vanuatu)
America (Argentina, Chile, Dominican republic, Ecuador, Cayman islands, British virgin islands, Anguilla, Montserrat)

My question is :
Can my company and my partners be part in your voluntary carbon market to sell carbon credits to your buyers please ?

While waiting for your answer, please believe, my sincere greetings.


President of the Holomorphe company
General engineer graduated from the Leonardo da Vinci School of Engineering in Paris La Défense
Headquarters address: 31 Avenue de Ségur 75007 Paris
SIREN : 883632556
Telephone : 
Github : Jay4C
LinkedIn : """

        time.sleep(5)

        warnings.filterwarnings(
            action="ignore",
            message="unclosed",
            category=ResourceWarning
        )

        time.sleep(5)

        browser = webdriver.Firefox(
            executable_path='..\\..\\geckodriver.exe',
            options=options
        )

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get('https://outlook.live.com/owa/')
        print("browser.get('https://outlook.live.com/owa/')")

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
        email_input.send_keys(username)
        email_input.send_keys(Keys.ENTER)
        print("email_input inserted")

        time.sleep(5)

        password_input = browser.find_element_by_xpath(
            '//*[@id="i0118"]'
        )
        password_input.clear()
        password_input.send_keys(password)
        password_input.send_keys(Keys.ENTER)
        print("password_input inserted")

        time.sleep(5)

        # click on the checkbox "Ne plus afficher ce message"
        ne_plus_afficher_ce_message_checkbox = browser.find_element_by_xpath(
            '//*[@id="KmsiCheckboxField"]'
        )
        ne_plus_afficher_ce_message_checkbox.click()
        print("ne_plus_afficher_ce_message_checkbox.click()")

        time.sleep(5)

        # click on the button "Non"
        non_button = browser.find_element_by_xpath(
            '//*[@id="idBtn_Back"]'
        )
        non_button.click()
        print("non_button.click()")

        time.sleep(15)

        for email in emails:
            envoye_a = email.lower()

            print('Nouveau courrier pour ' + str(envoye_a))

            # click on the button "Nouveau courrier"
            nouveau_courrier_button = browser.find_element_by_xpath(
                '/html/body/div[3]/div/div[2]/div[2]/div[1]/div/div/div/div/div/div[1]/div[2]/div/div/button'
            )
            nouveau_courrier_button.click()
            print("nouveau_courrier_button.click()")

            time.sleep(7)

            # Insert the email sender
            try:
                actions_email = ActionChains(browser)
                time.sleep(3)
                actions_email.send_keys(email)
                time.sleep(3)
                actions_email.send_keys(Keys.ENTER)
                time.sleep(3)
                actions_email.send_keys(Keys.TAB)
                time.sleep(3)
                actions_email.perform()
                print("email_input inserted")
            except Exception as e:
                print('error email_input : ' + str(e))

            time.sleep(7)

            # Insert the subject
            try:
                actions_subject = ActionChains(browser)
                time.sleep(3)
                actions_subject.send_keys(objet)
                time.sleep(3)
                actions_subject.send_keys(Keys.TAB)
                time.sleep(3)
                actions_subject.perform()
                print("subject_input inserted")
            except Exception as e:
                print('error subject_input : ' + str(e))

            time.sleep(7)

            # Insert the message
            try:
                actions_message = ActionChains(browser)
                time.sleep(3)
                actions_message.send_keys(message)
                time.sleep(3)
                actions_message.perform()
                print("message_input inserted")
            except Exception as e:
                print('error message_input : ' + str(e))

            time.sleep(7)

            # click on the button "Envoyer"
            try:
                actions_envoyer = ActionChains(browser)
                time.sleep(3)
                actions_envoyer.send_keys(Keys.TAB)
                time.sleep(3)
                actions_envoyer.send_keys(Keys.TAB)
                time.sleep(3)
                actions_envoyer.send_keys(Keys.TAB)
                time.sleep(3)
                actions_envoyer.send_keys(Keys.ENTER)
                actions_envoyer.perform()
                print("envoyer_button.click()")
            except Exception as e:
                print('error envoyer_button : ' + str(e))

            time.sleep(15)

        time.sleep(5)

        # click on the button "Mon profile"
        try:
            mon_profile_button = browser.find_element_by_xpath(
                '/html/body/div[3]/div/div[1]/div/div[1]/div[3]/div[1]/button/div/div[2]/div/div/div/div/div/div[2]/img'
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

            time.sleep(5)
        except Exception as e:
            print('error button Mon Profile : ' + str(e))

        browser.quit()
        print('browser.quit()')

        time.sleep(5)


class UnitTestsWebAutomationOutlookWithHeadlessForSendingEmailsForBusinessInElectricity(unittest.TestCase):
    # ok
    def test_send_several_emails_for_selling_electricity(self):
        print("test_send_several_emails_for_selling_electricity")

        # with Firefox
        options = Options()
        options.headless = False

        username = ".@outlook.fr"

        password = ""

        # @gmail.com

        emails = [
            '@gmail.com'
        ]

        objet = 'Request for selling electricity to your company - '

        message = """Hello,

Today, I am working on an innovative technology for producing electricity by harnessing magnetic energy from permanent magnets without greenhouse gases emmissions.

My technology doesn't require oil, gas, coal, solar energy, wind energy, geothermal energy or hydraulic energy to operate, and it has no parts in motion.

After, I would like to sell electricity to your company through the public electricity grid, and I can sell you some products for generating electricity.

My questions are :
Can I sell electricity to your company please ?
Does your company prefer to buy technologies for producing electricity please ?

Looking forward to your return, I beg you to believe, my sincere greetings.


General engineer graduated at the School of Engineers Leonard de Vinci in Paris La Defense
Head office address: Geneva in Switzerland
Phone : 0
GitHub : Jay4C
LinkedIn : """

        time.sleep(5)

        warnings.filterwarnings(
            action="ignore",
            message="unclosed",
            category=ResourceWarning
        )

        time.sleep(5)

        browser = webdriver.Firefox(
            executable_path='..\\..\\geckodriver.exe',
            options=options
        )

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get('https://outlook.live.com/owa/')
        print("browser.get('https://outlook.live.com/owa/')")

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
        email_input.send_keys(username)
        email_input.send_keys(Keys.ENTER)
        print("email_input inserted")

        time.sleep(5)

        password_input = browser.find_element_by_xpath(
            '//*[@id="i0118"]'
        )
        password_input.clear()
        password_input.send_keys(password)
        password_input.send_keys(Keys.ENTER)
        print("password_input inserted")

        time.sleep(5)

        # click on the checkbox "Ne plus afficher ce message"
        ne_plus_afficher_ce_message_checkbox = browser.find_element_by_xpath(
            '//*[@id="KmsiCheckboxField"]'
        )
        ne_plus_afficher_ce_message_checkbox.click()
        print("ne_plus_afficher_ce_message_checkbox.click()")

        time.sleep(5)

        # Click on the button "Non"
        non_button = browser.find_element_by_xpath(
            '//*[@id="idBtn_Back"]'
        )
        non_button.click()
        print("non_button.click()")

        time.sleep(15)

        for email in emails:
            envoye_a = email.lower()

            print('Nouveau courrier pour ' + str(envoye_a))

            # click on the button "Nouveau courrier"
            nouveau_courrier_button = browser.find_element_by_xpath(
                '/html/body/div[3]/div/div[2]/div[2]/div[1]/div/div/div/div/div/div[1]/div[2]/div/div/button'
            )
            nouveau_courrier_button.click()
            print("nouveau_courrier_button.click()")

            time.sleep(7)

            # Insert the email sender
            try:
                actions_email = ActionChains(browser)
                time.sleep(3)
                actions_email.send_keys(email)
                time.sleep(3)
                actions_email.send_keys(Keys.ENTER)
                time.sleep(3)
                actions_email.send_keys(Keys.TAB)
                time.sleep(3)
                actions_email.perform()
                print("email_input inserted")
            except Exception as e:
                print('error email_input : ' + str(e))

            time.sleep(7)

            # Insert the subject
            try:
                actions_subject = ActionChains(browser)
                time.sleep(3)
                actions_subject.send_keys(objet)
                time.sleep(3)
                actions_subject.send_keys(Keys.TAB)
                time.sleep(3)
                actions_subject.perform()
                print("subject_input inserted")
            except Exception as e:
                print('error subject_input : ' + str(e))

            time.sleep(7)

            # Insert the message
            try:
                actions_message = ActionChains(browser)
                time.sleep(3)
                actions_message.send_keys(message)
                time.sleep(3)
                actions_message.perform()
                print("message_input inserted")
            except Exception as e:
                print('error message_input : ' + str(e))

            time.sleep(7)

            # click on the button "Envoyer"
            try:
                actions_envoyer = ActionChains(browser)
                time.sleep(3)
                actions_envoyer.send_keys(Keys.TAB)
                time.sleep(3)
                actions_envoyer.send_keys(Keys.TAB)
                time.sleep(3)
                actions_envoyer.send_keys(Keys.TAB)
                time.sleep(3)
                actions_envoyer.send_keys(Keys.ENTER)
                actions_envoyer.perform()
                print("envoyer_button.click()")
            except Exception as e:
                print('error envoyer_button : ' + str(e))

            time.sleep(15)

        time.sleep(5)

        # click on the button "Mon profile"
        try:
            mon_profile_button = browser.find_element_by_xpath(
                '/html/body/div[3]/div/div[1]/div/div[1]/div[3]/div[1]/button/div/div[2]/div/div/div/div/div/div[2]/img'
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

            time.sleep(5)
        except Exception as e:
            print('error button Mon Profile : ' + str(e))

        browser.quit()
        print('browser.quit()')

        time.sleep(5)

    # ok
    def test_send_several_emails_for_selling_electricity_by_partnership(self):
        print("test_send_several_emails_for_selling_electricity_by_partnership")

        # with Firefox
        options = Options()
        options.headless = False

        username = ".@outlook.fr"

        password = ""

        # @gmail.com

        emails = [
            '@gmail.com'
        ]

        objet = 'Request for a partnership for selling electricity - M.  '

        message = """Hello,

Today, I am working on an innovative technology for producing electricity by harnessing magnetic energy from permanent magnets without greenhouse gases emissions.

My technology doesn't require oil, gas, coal, solar energy, wind energy, geothermal energy or hydraulic energy to operate, and it has no parts in motion.

After, I would like to sell electricity in partnership with your company through the public electricity grid from your point of injection.

My questions are :
Can we sell electricity in partnership from your point of injection please ?
How much electrical power can we inject into the public electricity grid from your point of injection please ?

Looking forward to your return, I beg you to believe, my sincere greetings.

Mr.  
General engineer graduated at the School of Engineers Leonard de Vinci in Paris La Defense
Head office address: Geneva in Switzerland
Phone : 
GitHub : Jay4C
LinkedIn :  """

        time.sleep(5)

        warnings.filterwarnings(
            action="ignore",
            message="unclosed",
            category=ResourceWarning
        )

        time.sleep(5)

        browser = webdriver.Firefox(
            executable_path='..\\..\\geckodriver.exe',
            options=options
        )

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get('https://outlook.live.com/owa/')
        print("browser.get('https://outlook.live.com/owa/')")

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
        email_input.send_keys(username)
        email_input.send_keys(Keys.ENTER)
        print("email_input inserted")

        time.sleep(5)

        password_input = browser.find_element_by_xpath(
            '//*[@id="i0118"]'
        )
        password_input.clear()
        password_input.send_keys(password)
        password_input.send_keys(Keys.ENTER)
        print("password_input inserted")

        time.sleep(5)

        # click on the checkbox "Ne plus afficher ce message"
        ne_plus_afficher_ce_message_checkbox = browser.find_element_by_xpath(
            '//*[@id="KmsiCheckboxField"]'
        )
        ne_plus_afficher_ce_message_checkbox.click()
        print("ne_plus_afficher_ce_message_checkbox.click()")

        time.sleep(5)

        # Click on the button "Non"
        non_button = browser.find_element_by_xpath(
            '//*[@id="idBtn_Back"]'
        )
        non_button.click()
        print("non_button.click()")

        time.sleep(15)

        for email in emails:
            envoye_a = email.lower()

            print('Nouveau courrier pour ' + str(envoye_a))

            # click on the button "Nouveau courrier"
            nouveau_courrier_button = browser.find_element_by_xpath(
                '/html/body/div[3]/div/div[2]/div[2]/div[1]/div/div/div/div/div/div[1]/div[2]/div/div/button'
            )
            nouveau_courrier_button.click()
            print("nouveau_courrier_button.click()")

            time.sleep(7)

            # Insert the email sender
            try:
                actions_email = ActionChains(browser)
                time.sleep(3)
                actions_email.send_keys(email)
                time.sleep(3)
                actions_email.send_keys(Keys.ENTER)
                time.sleep(3)
                actions_email.send_keys(Keys.TAB)
                time.sleep(3)
                actions_email.perform()
                print("email_input inserted")
            except Exception as e:
                print('error email_input : ' + str(e))

            time.sleep(7)

            # Insert the subject
            try:
                actions_subject = ActionChains(browser)
                time.sleep(3)
                actions_subject.send_keys(objet)
                time.sleep(3)
                actions_subject.send_keys(Keys.TAB)
                time.sleep(3)
                actions_subject.perform()
                print("subject_input inserted")
            except Exception as e:
                print('error subject_input : ' + str(e))

            time.sleep(7)

            # Insert the message
            try:
                actions_message = ActionChains(browser)
                time.sleep(3)
                actions_message.send_keys(message)
                time.sleep(3)
                actions_message.perform()
                print("message_input inserted")
            except Exception as e:
                print('error message_input : ' + str(e))

            time.sleep(7)

            # click on the button "Envoyer"
            try:
                actions_envoyer = ActionChains(browser)
                time.sleep(3)
                actions_envoyer.send_keys(Keys.TAB)
                time.sleep(3)
                actions_envoyer.send_keys(Keys.TAB)
                time.sleep(3)
                actions_envoyer.send_keys(Keys.TAB)
                time.sleep(3)
                actions_envoyer.send_keys(Keys.ENTER)
                actions_envoyer.perform()
                print("envoyer_button.click()")
            except Exception as e:
                print('error envoyer_button : ' + str(e))

            time.sleep(15)

        time.sleep(5)

        # click on the button "Mon profile"
        try:
            mon_profile_button = browser.find_element_by_xpath(
                '/html/body/div[3]/div/div[1]/div/div[1]/div[3]/div[1]/button/div/div[2]/div/div/div/div/div/div[2]/img'
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

            time.sleep(5)
        except Exception as e:
            print('error button Mon Profile : ' + str(e))

        browser.quit()
        print('browser.quit()')

        time.sleep(5)

    # ok
    def test_send_several_emails_for_injecting_electricity_into_the_network(self):
        print("test_send_several_emails_for_injecting_electricity_into_the_network")

        # with Firefox
        options = Options()
        options.headless = False

        username = ".@outlook.fr"

        password = ""

        # @gmail.com

        emails = [
            '@gmail.com'
        ]

        objet = 'Request for injecting electricity into your electricity transport network - '

        message = """Hello,

Today, I am working on an innovative technology for producing electricity by harnessing magnetic energy from permanent magnets without greenhouse gases emissions.

My technology doesn't require oil, gas, coal, solar energy, wind energy, geothermal energy or hydraulic energy to operate, and it has no parts in motion.

After, I will like to sell electricity to some electricity providers through the public electricity grid from your electricity transport network.

My questions are :
Can you send me the conditions and requirements for injecting electricity into your electricity transmission system please ?
Can you send me the list of GPS coordinates of the route of your electricity transmission network in CSV or JSON or Web API format in open source please ?

Looking forward to your return, I beg you to believe, my sincere greetings.


General engineer graduated at the School of Engineers Leonard de Vinci in Paris La Defense
Head office address: Geneva in Switzerland
Phone : 
GitHub : Jay4C
LinkedIn :  """

        time.sleep(5)

        warnings.filterwarnings(
            action="ignore",
            message="unclosed",
            category=ResourceWarning
        )

        time.sleep(5)

        browser = webdriver.Firefox(
            executable_path='..\\..\\geckodriver.exe',
            options=options
        )

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get('https://outlook.live.com/owa/')
        print("browser.get('https://outlook.live.com/owa/')")

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
        email_input.send_keys(username)
        email_input.send_keys(Keys.ENTER)
        print("email_input inserted")

        time.sleep(5)

        password_input = browser.find_element_by_xpath(
            '//*[@id="i0118"]'
        )
        password_input.clear()
        password_input.send_keys(password)
        password_input.send_keys(Keys.ENTER)
        print("password_input inserted")

        time.sleep(5)

        # click on the checkbox "Ne plus afficher ce message"
        ne_plus_afficher_ce_message_checkbox = browser.find_element_by_xpath(
            '//*[@id="KmsiCheckboxField"]'
        )
        ne_plus_afficher_ce_message_checkbox.click()
        print("ne_plus_afficher_ce_message_checkbox.click()")

        time.sleep(5)

        # Click on the button "Non"
        non_button = browser.find_element_by_xpath(
            '//*[@id="idBtn_Back"]'
        )
        non_button.click()
        print("non_button.click()")

        time.sleep(15)

        for email in emails:
            envoye_a = email.lower()

            print('Nouveau courrier pour ' + str(envoye_a))

            # click on the button "Nouveau courrier"
            nouveau_courrier_button = browser.find_element_by_xpath(
                '/html/body/div[3]/div/div[2]/div[2]/div[1]/div/div/div/div/div/div[1]/div[2]/div/div/button'
            )
            nouveau_courrier_button.click()
            print("nouveau_courrier_button.click()")

            time.sleep(7)

            # Insert the email sender
            try:
                actions_email = ActionChains(browser)
                time.sleep(3)
                actions_email.send_keys(email)
                time.sleep(3)
                actions_email.send_keys(Keys.ENTER)
                time.sleep(3)
                actions_email.send_keys(Keys.TAB)
                time.sleep(3)
                actions_email.perform()
                print("email_input inserted")
            except Exception as e:
                print('error email_input : ' + str(e))

            time.sleep(7)

            # Insert the subject
            try:
                actions_subject = ActionChains(browser)
                time.sleep(3)
                actions_subject.send_keys(objet)
                time.sleep(3)
                actions_subject.send_keys(Keys.TAB)
                time.sleep(3)
                actions_subject.perform()
                print("subject_input inserted")
            except Exception as e:
                print('error subject_input : ' + str(e))

            time.sleep(7)

            # Insert the message
            try:
                actions_message = ActionChains(browser)
                time.sleep(3)
                actions_message.send_keys(message)
                time.sleep(3)
                actions_message.perform()
                print("message_input inserted")
            except Exception as e:
                print('error message_input : ' + str(e))

            time.sleep(7)

            # click on the button "Envoyer"
            try:
                actions_envoyer = ActionChains(browser)
                time.sleep(3)
                actions_envoyer.send_keys(Keys.TAB)
                time.sleep(3)
                actions_envoyer.send_keys(Keys.TAB)
                time.sleep(3)
                actions_envoyer.send_keys(Keys.TAB)
                time.sleep(3)
                actions_envoyer.send_keys(Keys.ENTER)
                actions_envoyer.perform()
                print("envoyer_button.click()")
            except Exception as e:
                print('error envoyer_button : ' + str(e))

            time.sleep(15)

        time.sleep(5)

        # click on the button "Mon profile"
        try:
            mon_profile_button = browser.find_element_by_xpath(
                '/html/body/div[3]/div/div[1]/div/div[1]/div[3]/div[1]/button/div/div[2]/div/div/div/div/div/div[2]/img'
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

            time.sleep(5)
        except Exception as e:
            print('error button Mon Profile : ' + str(e))

        browser.quit()
        print('browser.quit()')

        time.sleep(5)

    # ok
    def test_send_several_emails_for_request_authorization_production_electricity_switzerland(self):
        print("test_send_several_emails_for_request_authorization_production_electricity_switzerland")

        username = ".@outlook.fr"

        password = ""

        emails = [
            "@gmail.com"
        ]

        objet = "Request for setting up a power plant in your municipality - "

        message = """Hello,

Under the energy law,

Today, I am working on the Chas Campbell devices based on the gravitational energy.

This technology permits to produce electricity thanks to the gravitational energy of a flywheel or an other gravity wheel.

This kind of technology has not emissions to the atmosphere, water or land, and doesn't need wind, hydro, biomass, waste (including waste heat), bio-fuel, geothermal, fuel cells, tidal, temperature inversion or convection or even solar to operate.

I would like to know the requirements for setting up a power plant in your municipality.

My question is :
Do you have a form to fill for submitting a request for setting up a power plant in your municipality please ?

Please find attached a document about the Chas Campbell gravitational engine.

While waiting for your return, please believe, my sincere greetings.


Telephone : """

        file_upload = "C:\\Users\\DELL\\Documents\\Outils\\Desktop_Automation\\Chas_Campbell_Gravitational_Engine.pdf"

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
            executable_path='..\\..\\geckodriver.exe'
        )

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get('https://outlook.live.com/owa/')
        print("browser.get('https://outlook.live.com/owa/')")

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
        email_input.send_keys(username)
        email_input.send_keys(Keys.ENTER)
        print("email_input inserted")

        time.sleep(5)

        password_input = browser.find_element_by_xpath(
            '//*[@id="i0118"]'
        )
        password_input.clear()
        password_input.send_keys(password)
        password_input.send_keys(Keys.ENTER)
        print("password_input inserted")

        time.sleep(5)

        # click on the checkbox "Ne plus afficher ce message"
        ne_plus_afficher_ce_message_checkbox = browser.find_element_by_xpath(
            '//*[@id="KmsiCheckboxField"]'
        )
        ne_plus_afficher_ce_message_checkbox.click()
        print("ne_plus_afficher_ce_message_checkbox.click()")

        time.sleep(5)

        # click on the button "Non"
        non_button = browser.find_element_by_xpath(
            '//*[@id="idBtn_Back"]'
        )
        non_button.click()
        print("non_button.click()")

        time.sleep(15)

        for email in emails:
            envoye_a = email.lower()

            print('Nouveau courrier pour ' + str(envoye_a))

            # click on the button "Nouveau courrier"
            nouveau_courrier_button = browser.find_element_by_xpath(
                '/html/body/div[3]/div/div[2]/div[2]/div[1]/div/div/div[1]/div[1]/div[2]/div/div/button'
            )
            nouveau_courrier_button.click()
            print("nouveau_courrier_button.click()")

            time.sleep(7)

            # Insert the email sender
            try:
                envoye_a_input = browser.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div[2]/div[1]/div/div/div[3]/div[2]/div/div[2]/div[1]/div/div/div'
                    '/div[1]/div[1]/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/input'
                )
                envoye_a_input.clear()
                envoye_a_input.send_keys(envoye_a)
                time.sleep(2)
                envoye_a_input.send_keys(Keys.ENTER)
                time.sleep(2)
                envoye_a_input.send_keys(Keys.TAB)
                print("envoye_a_input inserted")
            except Exception as e:
                print("error envoye_a_input : " + str(e))

            time.sleep(7)

            # Insert the subject
            try:
                actions_subject = ActionChains(browser)
                actions_subject.send_keys(objet)
                time.sleep(2)
                actions_subject.send_keys(Keys.TAB)
                actions_subject.perform()
                print("subject_input inserted")
            except Exception as e:
                print('error subject_input : ' + str(e))

            time.sleep(7)

            # Insert the file
            try:
                file_input = browser.find_element_by_xpath(
                    "/html/body/div[3]/div/div[2]/div[2]/div[1]/div/div/div[3]/div[1]/div/span/input[1]"
                )
                file_input.send_keys(
                    file_upload
                )
                print("file_input inserted")
            except Exception as e:
                print('error file_input : ' + str(e))

            time.sleep(15)

            # Insert the message
            try:
                actions_message = ActionChains(browser)
                actions_message.send_keys(message)
                actions_message.perform()
                print("message_input inserted")
            except Exception as e:
                print('error message_input : ' + str(e))

            time.sleep(7)

            # click on the button "Envoyer"
            try:
                actions_envoyer = ActionChains(browser)
                time.sleep(1)
                actions_envoyer.send_keys(Keys.TAB)
                time.sleep(1)
                actions_envoyer.send_keys(Keys.TAB)
                time.sleep(3)
                actions_envoyer.send_keys(Keys.ENTER)
                actions_envoyer.perform()
                print("envoyer_button.click()")
            except Exception as e:
                print('error envoyer_button : ' + str(e))

            time.sleep(15)

        time.sleep(5)

        # click on the button "Mon profile"
        try:
            mon_profile_button = browser.find_element_by_xpath(
                '/html/body/div[3]/div/div[1]/div/div[1]/div[3]/div[1]/button/div/div[2]/div/div/div/div/div/div[2]/img'
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

            time.sleep(5)
        except Exception as e:
            print('error button Mon Profile : ' + str(e))

        browser.quit()
        print('browser.quit()')

        time.sleep(5)
    
    # ok
    def test_send_several_emails_for_partenariats_vente_electricite(self):
        print("test_send_several_emails_for_partenariats_vente_electricite")

        username = ".@outlook.fr"
        password = ""

        emails = [
            "@gmail.com"
        ]

        objet = "Demande de partenariat pour la vente d'électricité sur le réseau public d'électricité - Monsieur  "

        message = """Bonjour,

Je travaille sur une machine gravitationnelle considérée comme une machine à énergie libre pour la production d'électricité, et je suis à la recherche de partenaires possédant du foncier raccordable au réseau public d'électricité.

Après, la vente d'électricité sur le réseau public d'électricité sera vendue à des fournisseurs d'électricité par les partenaires.

Puis, la vente d'électricité sera répartie équitablement entre les partenaires quel que soit leur niveau d'investissement sur le projet avec un accord préalable sur la rentabilité du projet.

Ensuite, les différentes vues de la conception assistée par ordinateur de ma machine gravitationnelle sont disponibles au public au lien suivant : https://github.com/Jay4C/Holomorphe_Company/tree/main/Sales_of_digital_contents/Computer_aided_design/Gravitational_Engine

Ma question est : est-ce possible d'être en partenariat auprès de votre société pour la vente d'électricité s'il vous plaît ?

En attendant votre décision, je vous prie de croire, mes salutations les plus sincères.

Monsieur 
Diplôme d'ingénieur généraliste de l'École Supérieure d'Ingénieurs Léonard de Vinci à Paris La Défense
Téléphone : """

        time.sleep(5)

        warnings.filterwarnings(
            action="ignore",
            message="unclosed",
            category=ResourceWarning
        )

        time.sleep(5)

        # with Firefox
        options = Options()
        options.headless = True
        browser = webdriver.Firefox(
            executable_path='..\\..\\geckodriver.exe',
            options=options
        )

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get('https://outlook.live.com/owa/')
        print("browser.get('https://outlook.live.com/owa/')")

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
        email_input.send_keys(username)
        email_input.send_keys(Keys.ENTER)
        print("email_input inserted")

        time.sleep(5)

        password_input = browser.find_element_by_xpath(
            '//*[@id="i0118"]'
        )
        password_input.clear()
        password_input.send_keys(password)
        password_input.send_keys(Keys.ENTER)
        print("password_input inserted")

        time.sleep(5)

        # click on the checkbox "Ne plus afficher ce message"
        ne_plus_afficher_ce_message_checkbox = browser.find_element_by_xpath(
            '//*[@id="KmsiCheckboxField"]'
        )
        ne_plus_afficher_ce_message_checkbox.click()
        print("ne_plus_afficher_ce_message_checkbox.click()")

        time.sleep(5)

        # click on the button "Non"
        non_button = browser.find_element_by_xpath(
            '//*[@id="idBtn_Back"]'
        )
        non_button.click()
        print("non_button.click()")

        time.sleep(15)

        for email in emails:
            envoye_a = email.lower()

            print('Nouveau courrier pour ' + str(envoye_a))

            # click on the button "Nouveau courrier"
            nouveau_courrier_button = browser.find_element_by_xpath(
                '/html/body/div[3]/div/div[2]/div[2]/div[1]/div/div/div[1]/div[1]/div[2]/div/div/button'
            )
            nouveau_courrier_button.click()
            print("nouveau_courrier_button.click()")

            time.sleep(7)

            # Insert the email sender
            try:
                envoye_a_input = browser.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div[2]/div[1]/div/div/div[3]/div[2]/div/div[2]/div[1]/div/div/div'
                    '/div[1]/div[1]/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/input'
                )
                envoye_a_input.clear()
                envoye_a_input.send_keys(envoye_a)
                time.sleep(2)
                envoye_a_input.send_keys(Keys.ENTER)
                time.sleep(2)
                envoye_a_input.send_keys(Keys.TAB)
                print("envoye_a_input inserted")
            except Exception as e:
                print("error envoye_a_input : " + str(e))

            time.sleep(7)

            # Insert the subject
            try:
                actions_subject = ActionChains(browser)
                actions_subject.send_keys(objet)
                time.sleep(2)
                actions_subject.send_keys(Keys.TAB)
                actions_subject.perform()
                print("subject_input inserted")
            except Exception as e:
                print('error subject_input : ' + str(e))

            time.sleep(7)

            # Insert the message
            try:
                actions_message = ActionChains(browser)
                actions_message.send_keys(message)
                actions_message.perform()
                print("message_input inserted")
            except Exception as e:
                print('error message_input : ' + str(e))

            time.sleep(5)

            # click on the button "Envoyer"
            try:
                actions_envoyer = ActionChains(browser)
                time.sleep(1)
                actions_envoyer.send_keys(Keys.TAB)
                time.sleep(1)
                actions_envoyer.send_keys(Keys.TAB)
                time.sleep(1)
                actions_envoyer.send_keys(Keys.TAB)
                time.sleep(2)
                actions_envoyer.send_keys(Keys.ENTER)
                actions_envoyer.perform()
                print("envoyer_button.click()")
            except Exception as e:
                print('error envoyer_button : ' + str(e))

            time.sleep(15)

        time.sleep(5)

        # click on the button "Mon profile"
        try:
            mon_profile_button = browser.find_element_by_xpath(
                '/html/body/div[3]/div/div[1]/div/div[1]/div[3]/div[1]/button/div/div[2]/div/div/div/div/div/div[2]/img'
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

            time.sleep(5)
        except Exception as e:
            print('error button Mon Profile : ' + str(e))

        browser.quit()
        print('browser.quit()')

        time.sleep(5)


class UnitTestsWebAutomationOutlookWithHeadlessForSendingEmailsForOthersDemands(unittest.TestCase):
    # ok
    def test_send_emails_to_aeroclubs_in_ile_de_france(self):
        print("test_send_emails_to_aeroclubs_in_ile_de_france")

        # with Firefox
        options = Options()
        options.headless = False

        username = ".@outlook.fr"

        password = ""

        # @gmail.com

        emails = [
            '@gmail.com'
        ]

        objet = 'Demande de tarifs sur la licence PPL international - '

        message = """Bonjour,

Je voudrai avoir les tarifs sur la licence PPL international afin de pouvoir naviguer en aéronef au niveau international.

Mes questions sont :
Quel est le montant TTC pour un forfait PPL s'il vous plaît ?
Quel est le montant TTC pour un droit d’entrée à l’aéro-club s'il vous plaît ?
Quel est le montant TTC pour une adhésion annuelle s'il vous plaît ?
Quel est le montant TTC pour une préparation du théorique PPL s'il vous plaît ?
Quel est le montant TTC pour un cours sur simulateur s'il vous plaît ?
Quel est le montant TTC pour un kit pilote complet (Cartes de navigation édition IGN Nord Ouest 1/500000ième, Cartes de Radionavigation édition SIA 1/1000000ième Nord et Sud, Complément aux cartes Aéronautiques édition SIA, Guide VFR édition SIA, (disponible en ligne sur décision du SIA), Règle de navigation SIA, Manuel du Pilote Privé dernière édition (Ed.  Maxima), Livret de progression PPL, Carnet de Vol DGAC conforme EASA, Planchette de vol avec volet et feuillets pour cartes VAC, Log de Nav, Casque de Pilote efficace et robuste) s'il vous plaît ?
Quel est le montant TTC pour un vol solo à l'heure s'il vous plaît ?
Quel est le montant TTC pour un vol en double commande à l'heure s'il vous plaît ?

Très bonne journée à vous,


Téléphone : 
GitHub : Jay4C
LinkedIn : 
Région : Ile-de-france"""

        time.sleep(5)

        warnings.filterwarnings(
            action="ignore",
            message="unclosed",
            category=ResourceWarning
        )

        time.sleep(5)

        browser = webdriver.Firefox(
            executable_path='..\\..\\geckodriver.exe',
            options=options
        )

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get('https://outlook.live.com/owa/')
        print("browser.get('https://outlook.live.com/owa/')")

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
        email_input.send_keys(username)
        email_input.send_keys(Keys.ENTER)
        print("email_input inserted")

        time.sleep(5)

        password_input = browser.find_element_by_xpath(
            '//*[@id="i0118"]'
        )
        password_input.clear()
        password_input.send_keys(password)
        password_input.send_keys(Keys.ENTER)
        print("password_input inserted")

        time.sleep(5)

        # click on the checkbox "Ne plus afficher ce message"
        ne_plus_afficher_ce_message_checkbox = browser.find_element_by_xpath(
            '//*[@id="KmsiCheckboxField"]'
        )
        ne_plus_afficher_ce_message_checkbox.click()
        print("ne_plus_afficher_ce_message_checkbox.click()")

        time.sleep(5)

        # Click on the button "Non"
        non_button = browser.find_element_by_xpath(
            '//*[@id="idBtn_Back"]'
        )
        non_button.click()
        print("non_button.click()")

        time.sleep(15)

        for email in emails:
            envoye_a = email.lower()

            print('Nouveau courrier pour ' + str(envoye_a))

            # click on the button "Nouveau courrier"
            nouveau_courrier_button = browser.find_element_by_xpath(
                '/html/body/div[2]/div/div[2]/div[2]/div[1]/div/div/div/div/div/div[1]/div[2]/div/div/button'
            )
            nouveau_courrier_button.click()
            print("nouveau_courrier_button.click()")

            time.sleep(7)

            # Insert the email sender
            try:
                actions_email = ActionChains(browser)
                time.sleep(3)
                actions_email.send_keys(email)
                time.sleep(3)
                actions_email.send_keys(Keys.ENTER)
                time.sleep(3)
                actions_email.send_keys(Keys.TAB)
                time.sleep(3)
                actions_email.perform()
                print("email_input inserted")
            except Exception as e:
                print('error email_input : ' + str(e))

            time.sleep(7)

            # Insert the subject
            try:
                actions_subject = ActionChains(browser)
                time.sleep(3)
                actions_subject.send_keys(objet)
                time.sleep(3)
                actions_subject.send_keys(Keys.TAB)
                time.sleep(3)
                actions_subject.perform()
                print("subject_input inserted")
            except Exception as e:
                print('error subject_input : ' + str(e))

            time.sleep(7)

            # Insert the message
            try:
                actions_message = ActionChains(browser)
                time.sleep(3)
                actions_message.send_keys(message)
                time.sleep(3)
                actions_message.perform()
                print("message_input inserted")
            except Exception as e:
                print('error message_input : ' + str(e))

            time.sleep(7)

            # click on the button "Envoyer"
            try:
                actions_envoyer = ActionChains(browser)
                time.sleep(3)
                actions_envoyer.send_keys(Keys.TAB)
                time.sleep(3)
                actions_envoyer.send_keys(Keys.TAB)
                time.sleep(3)
                actions_envoyer.send_keys(Keys.TAB)
                time.sleep(3)
                actions_envoyer.send_keys(Keys.ENTER)
                actions_envoyer.perform()
                print("envoyer_button.click()")
            except Exception as e:
                print('error envoyer_button : ' + str(e))

            time.sleep(15)

        time.sleep(5)

        # click on the button "Mon profile"
        try:
            mon_profile_button = browser.find_element_by_xpath(
                '/html/body/div[2]/div/div[1]/div/div[1]/div[3]/div[1]/button/div/div[2]/div/div/div/div/div/div[2]/img'
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

            time.sleep(5)
        except Exception as e:
            print('error button Mon Profile : ' + str(e))

        browser.quit()
        print('browser.quit()')

        time.sleep(5)


if __name__ == '__main__':
    unittest.main()
