import subprocess
import unittest
import time
import warnings
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options


class UnitTestsWebAutomationWeTransferWithoutHeadless(unittest.TestCase):
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
        browser.get('https://wetransfer.com/')

        time.sleep(5)

    # ok
    def test_send_one_email_with_one_file(self):
        print("test_send_one_email_with_one_file")

        envoye_a = ''

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
        browser.get('https://wetransfer.com/')

        time.sleep(10)

        # click on the button "Non merci"
        non_merci_button = browser.find_element_by_xpath(
            "/html/body/div[2]/div/div[2]/div[2]/div[2]/div[1]/div[3]/div[4]/button[3]"
        )
        non_merci_button.click()
        print("non_merci_button.click()")

        time.sleep(5)

        # click on the button "J'accepte"
        j_accepte_button = browser.find_element_by_xpath(
            "/html/body/div[2]/div/div[3]/div/div[2]/button"
        )
        j_accepte_button.click()
        print("j_accepte_button.click()")

        time.sleep(5)

        envoye_a_input = browser.find_element_by_xpath(
            "/html/body/div[2]/div/div[3]/div/div[1]/div[1]/div[2]/div[1]/div/div/input"
        )
        envoye_a_input.clear()
        envoye_a_input.send_keys(envoye_a)
        print("envoye_a_input inserted : " + str(envoye_a))

        time.sleep(5)

        votre_adresse_input = browser.find_element_by_xpath(
            "/html/body/div[2]/div/div[3]/div/div[1]/div[1]/div[2]/div[2]/input"
        )
        votre_adresse_input.clear()
        votre_adresse_input.send_keys("")
        print("votre_adresse_input inserted")

        time.sleep(5)

        titre_input = browser.find_element_by_xpath(
            "/html/body/div[2]/div/div[3]/div/div[1]/div[1]/div[2]/div[3]/div/input"
        )
        titre_input.clear()
        titre_input.send_keys(
            "Spontaneous application for a job as renewable energy engineer in full time contract - "
        )
        print("titre_input inserted")

        time.sleep(5)

        file_input = browser.find_element_by_xpath(
            "/html/body/div[2]/div/div[3]/div/div[1]/div[1]/div[1]/form/input[1]"
        )
        file_input.send_keys(
            "C:\\Users\\DELL\\Documents\\Outils\\Desktop_Automation"
            "\\Resume_Of_Jason_ALOYAU_[Renewable_energy_engineer].pdf"
        )
        print("file_input inserted")

        time.sleep(5)

        message_input = browser.find_element_by_xpath(
            "/html/body/div[2]/div/div[3]/div/div[1]/div[1]/div[2]/div[4]/div/textarea"
        )
        message_input.clear()
        message_input.send_keys(
"""
Hello,

Today, I am applying for a job as renewable energy engineer in full time contract for manufacturing free energy 
devices at big scale and I am available for a first exchange by phone and videoconference.

Please find attached my resume in PDF format.

In addition, you can have more information about free energy devices for electricity production without the need 
to use energy sources such as oil, coal, natural gas, nuclear, biomass, wind, sun, geothermal, hydraulic and wave 
energy and hydrothermal or hydrokinetic energy at the following link : https://github.com/Jay4C/Free-energy-devices
Free energy devices use zero point energy (https://en.wikipedia.org/wiki/Zero-point_energy) to operate.

While waiting for your return, please believe, my sincere greetings.


General engineer graduated from Leonard de Vinci Engineering School in Paris La Defense in France
Mailing address : 6 Avenue Leon Blum 93800 Epinay-sur-Seine (France)
Phone : 
"""
        )
        print("message_input inserted")

        time.sleep(10)

        # click on the button "Transférer"
        transferer_button = browser.find_element_by_xpath(
            "/html/body/div[2]/div/div[3]/div/div[2]/button[2]"
        )
        transferer_button.click()
        print("transferer_button.click()")

        time.sleep(5)

        # Outlook

        # Open a new window
        browser.execute_script("window.open('');")

        # Switch to the new window and open new URL
        browser.switch_to.window(browser.window_handles[1])

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
        email_input.send_keys("")
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

        # Switch to the last window
        browser.switch_to.window(browser.window_handles[0])

        time.sleep(5)

        code_input = browser.find_element_by_xpath(
            '/html/body/div[2]/div/div[3]/form/div[1]/div/input'
        )
        code_input.clear()
        code_input.send_keys(str(code))
        print("code_input inserted")

        time.sleep(5)

        # click on the button "Vérification"
        verification_button = browser.find_element_by_xpath(
            '/html/body/div[2]/div/div[3]/form/div[2]/button[2]'
        )
        verification_button.click()
        print("verification_button.click()")

        time.sleep(10)

        # Switch to the last window
        browser.switch_to.window(browser.window_handles[1])

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


class UnitTestsWebAutomationWeTransferWithHeadless(unittest.TestCase):
    # ok
    def test_send_one_email_with_one_file_with_headless_for_renewable_energy_engineer(self):
        print("test_send_one_email_with_one_file_with_headless_for_renewable_energy_engineer")

        envoye_a = '',

        objet = "Spontaneous application for a job as renewable energy engineer in full time contract - "

        message = """Hello, 

I am sending you my resume to apply for a job as a renewable energy engineer for manufacturing free energy machines 
(https://github.com/Jay4C/Free-energy-devices / https://en.wikipedia.org/wiki/Zero-point_energy) on a large scale.

While waiting for your return, please believe, my most sincere greetings.

 
General engineer graduated from Leonardo da Vinci Engineering School
Phone : """

        file_upload = "C:\\Users\\DELL\\Documents\\Outils\\Desktop_Automation" \
                      "\\Resume_Of_Jason_ALOYAU_[Renewable_energy_engineer].pdf"

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
        browser.get('https://wetransfer.com/')

        time.sleep(10)

        # click on the button "Non merci"
        non_merci_button = browser.find_element_by_xpath(
            "/html/body/div[2]/div/div[2]/div[2]/div[2]/div[1]/div[3]/div[4]/button[3]"
        )
        non_merci_button.click()
        print("non_merci_button.click()")

        time.sleep(5)

        # click on the button "J'accepte"
        j_accepte_button = browser.find_element_by_xpath(
            "/html/body/div[2]/div/div[3]/div/div[2]/button"
        )
        j_accepte_button.click()
        print("j_accepte_button.click()")

        time.sleep(5)

        envoye_a_input = browser.find_element_by_xpath(
            "/html/body/div[2]/div/div[3]/div/div[1]/div[1]/div[2]/div[1]/div/div/input"
        )
        envoye_a_input.clear()
        envoye_a_input.send_keys(envoye_a)
        print("envoye_a_input inserted : " + str(envoye_a))

        time.sleep(5)

        votre_adresse_input = browser.find_element_by_xpath(
            "/html/body/div[2]/div/div[3]/div/div[1]/div[1]/div[2]/div[2]/input"
        )
        votre_adresse_input.clear()
        votre_adresse_input.send_keys("")
        print("votre_adresse_input inserted")

        time.sleep(5)

        titre_input = browser.find_element_by_xpath(
            '//*[@id="displayName"]'
        )
        titre_input.clear()
        titre_input.send_keys(objet)
        print("titre_input inserted")

        time.sleep(5)

        file_input = browser.find_element_by_xpath(
            "/html/body/div[2]/div/div[3]/div/div[1]/div[1]/div[1]/form/input[1]"
        )
        file_input.send_keys(
            file_upload
        )
        print("file_input inserted")

        time.sleep(5)

        message_input = browser.find_element_by_xpath(
            '//*[@id="message"]'
        )
        message_input.clear()
        message_input.send_keys(
            message
        )
        print("message_input inserted")

        time.sleep(10)

        # click on the button "Transférer"
        transferer_button = browser.find_element_by_xpath(
            "/html/body/div[2]/div/div[3]/div/div[2]/button[2]"
        )
        transferer_button.click()
        print("transferer_button.click()")

        time.sleep(5)

        # Outlook

        # Open a new window
        browser.execute_script("window.open('');")

        # Switch to the new window and open new URL
        browser.switch_to.window(browser.window_handles[1])

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
        email_input.send_keys("")
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

        # Switch to the last window
        browser.switch_to.window(browser.window_handles[0])

        time.sleep(5)

        code_input = browser.find_element_by_xpath(
            '/html/body/div[2]/div/div[3]/form/div[1]/div/input'
        )
        code_input.clear()
        code_input.send_keys(str(code))
        print("code_input inserted")

        time.sleep(5)

        # click on the button "Vérification"
        verification_button = browser.find_element_by_xpath(
            '/html/body/div[2]/div/div[3]/form/div[2]/button[2]'
        )
        verification_button.click()
        print("verification_button.click()")

        time.sleep(20)

        # Display "Vous avez terminé!" text
        termine_text = browser.find_element_by_xpath(
            "/html/body/div[2]/div/div[3]/div/div[1]"
        ).text
        print("termine_text : " + str(termine_text))

        time.sleep(5)

        # Switch to the last window
        browser.switch_to.window(browser.window_handles[1])

        time.sleep(5)

        # click on the button "Sélectionner tous les messages"
        selectionner_tous_les_messages_button = browser.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div[2]/div[1]/div/div/div[3]/div[2]/div/div[1]/div[1]/div[1]/div/div[1]'
            '/div/i[2]'
        )
        selectionner_tous_les_messages_button.click()
        print("selectionner_tous_les_messages_button.click()")

        time.sleep(5)

        # click on the button "Vider Prioritaire"
        vider_prioritaire_button = browser.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div[2]/div[1]/div/div/div[3]/div[1]/div/div/div/div/div/div[1]/div[1]/button'
        )
        vider_prioritaire_button.click()
        print("vider_prioritaire_button.click()")

        time.sleep(7)

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
    def test_send_several_emails_with_one_file_with_headless_for_renewable_energy_engineer(self):
        print("test_send_several_emails_with_one_file_with_headless_for_renewable_energy_engineer")

        emails = [

        ]

        for email in emails:
            print('email : ' + email + ' starting')

            envoye_a = email

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
            browser.get('https://wetransfer.com/')

            time.sleep(10)

            # click on the button "Non merci"
            non_merci_button = browser.find_element_by_xpath(
                "/html/body/div[2]/div/div[2]/div[2]/div[2]/div[1]/div[3]/div[4]/button[3]"
            )
            non_merci_button.click()
            print("non_merci_button.click()")

            time.sleep(5)

            # click on the button "J'accepte"
            j_accepte_button = browser.find_element_by_xpath(
                "/html/body/div[2]/div/div[3]/div/div[2]/button"
            )
            j_accepte_button.click()
            print("j_accepte_button.click()")

            time.sleep(5)

            envoye_a_input = browser.find_element_by_xpath(
                "/html/body/div[2]/div/div[3]/div/div[1]/div[1]/div[2]/div[1]/div/div/input"
            )
            envoye_a_input.clear()
            envoye_a_input.send_keys(envoye_a)
            print("envoye_a_input inserted : " + str(envoye_a))

            time.sleep(5)

            votre_adresse_input = browser.find_element_by_xpath(
                "/html/body/div[2]/div/div[3]/div/div[1]/div[1]/div[2]/div[2]/input"
            )
            votre_adresse_input.clear()
            votre_adresse_input.send_keys("")
            print("votre_adresse_input inserted")

            time.sleep(5)

            titre_input = browser.find_element_by_xpath(
                "/html/body/div[2]/div/div[3]/div/div[1]/div[1]/div[2]/div[3]/div/input"
            )
            titre_input.clear()
            titre_input.send_keys(
                "Spontaneous application for a job as renewable energy engineer in full time contract - "
            )
            print("titre_input inserted")

            time.sleep(5)

            file_input = browser.find_element_by_xpath(
                "/html/body/div[2]/div/div[3]/div/div[1]/div[1]/div[1]/form/input[1]"
            )
            file_input.send_keys(
                "C:\\Users\\DELL\\Documents\\Outils\\Desktop_Automation"
                "\\Resume_Of_Jason_ALOYAU_[Renewable_energy_engineer].pdf"
            )
            print("file_input inserted")

            time.sleep(5)

            message_input = browser.find_element_by_xpath(
                "/html/body/div[2]/div/div[3]/div/div[1]/div[1]/div[2]/div[4]/div/textarea"
            )
            message_input.clear()
            message_input.send_keys(
"""
Hello,

Today, I am applying for a job as renewable energy engineer in full time contract for manufacturing free energy 
devices at big scale and I am available for a first exchange by phone and videoconference.

Please find attached my resume in PDF format.

In addition, you can have more information about free energy devices for electricity production without the need 
to use energy sources such as oil, coal, natural gas, nuclear, biomass, wind, sun, geothermal, hydraulic and wave 
energy and hydrothermal or hydrokinetic energy at the following link : https://github.com/Jay4C/Free-energy-devices
Free energy devices use zero point energy (https://en.wikipedia.org/wiki/Zero-point_energy) to operate.

While waiting for your return, please believe, my sincere greetings.


General engineer graduated from Leonard de Vinci Engineering School in Paris La Defense in France
Phone : 
"""
            )
            print("message_input inserted")

            time.sleep(10)

            # click on the button "Transférer"
            transferer_button = browser.find_element_by_xpath(
                "/html/body/div[2]/div/div[3]/div/div[2]/button[2]"
            )
            transferer_button.click()
            print("transferer_button.click()")

            time.sleep(5)

            # Outlook

            # Open a new window
            browser.execute_script("window.open('');")

            # Switch to the new window and open new URL
            browser.switch_to.window(browser.window_handles[1])

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
            email_input.send_keys("")
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

            # Switch to the last window
            browser.switch_to.window(browser.window_handles[0])

            time.sleep(5)

            code_input = browser.find_element_by_xpath(
                '/html/body/div[2]/div/div[3]/form/div[1]/div/input'
            )
            code_input.clear()
            code_input.send_keys(str(code))
            print("code_input inserted")

            time.sleep(5)

            # click on the button "Vérification"
            verification_button = browser.find_element_by_xpath(
                '/html/body/div[2]/div/div[3]/form/div[2]/button[2]'
            )
            verification_button.click()
            print("verification_button.click()")

            time.sleep(15)

            # Switch to the last window
            browser.switch_to.window(browser.window_handles[1])

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
                '/html/body/div[3]/div/div[2]/div[2]/div[1]/div/div/div[3]/div[1]/div/div/div/div/div/div[1]'
                '/div[1]/button'
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

            print('email : ' + email + ' ok')

    # ok
    def test_send_one_email_with_one_file_with_headless_for_developpeur_python(self):
        print("test_send_one_email_with_one_file_with_headless_for_developpeur_python")

        envoye_a = 'contact@appligos.fr',

        objet = "Candidature spontanée pour un emploi en tant que développeur Python " \
                "en contrat à durée indéterminée à temps plein -  "

        message = """Bonjour,

Je vous envoie mon CV pour postuler à un emploi en tant que développeur Python.

En attendant votre retour, je vous prie de croire, mes salutations les plus sincères.

 
Ingénieur généraliste diplômé de l'École Supérieure d'Ingénieurs Léonard de Vinci
Téléphone : """

        file_upload = "C:\\Users\\DELL\\Documents\\Outils\\Desktop_Automation" \
                      "\\[Developpeur_Python].pdf"

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
        browser.get('https://wetransfer.com/')

        time.sleep(10)

        # click on the button "Non merci"
        non_merci_button = browser.find_element_by_xpath(
            "/html/body/div[2]/div/div[2]/div[2]/div[2]/div[1]/div[3]/div[4]/button[3]"
        )
        non_merci_button.click()
        print("non_merci_button.click()")

        time.sleep(5)

        # click on the button "J'accepte"
        j_accepte_button = browser.find_element_by_xpath(
            "/html/body/div[2]/div/div[3]/div/div[2]/button"
        )
        j_accepte_button.click()
        print("j_accepte_button.click()")

        time.sleep(5)

        envoye_a_input = browser.find_element_by_xpath(
            "/html/body/div[2]/div/div[3]/div/div[1]/div[1]/div[2]/div[1]/div/div/input"
        )
        envoye_a_input.clear()
        envoye_a_input.send_keys(envoye_a)
        print("envoye_a_input inserted : " + str(envoye_a))

        time.sleep(5)

        votre_adresse_input = browser.find_element_by_xpath(
            "/html/body/div[2]/div/div[3]/div/div[1]/div[1]/div[2]/div[2]/input"
        )
        votre_adresse_input.clear()
        votre_adresse_input.send_keys("")
        print("votre_adresse_input inserted")

        time.sleep(5)

        titre_input = browser.find_element_by_xpath(
            '//*[@id="displayName"]'
        )
        titre_input.clear()
        titre_input.send_keys(objet)
        print("titre_input inserted")

        time.sleep(5)

        file_input = browser.find_element_by_xpath(
            "/html/body/div[2]/div/div[3]/div/div[1]/div[1]/div[1]/form/input[1]"
        )
        file_input.send_keys(
            file_upload
        )
        print("file_input inserted")

        time.sleep(5)

        message_input = browser.find_element_by_xpath(
            '//*[@id="message"]'
        )
        message_input.clear()
        message_input.send_keys(
            message
        )
        print("message_input inserted")

        time.sleep(10)

        # click on the button "Transférer"
        transferer_button = browser.find_element_by_xpath(
            "/html/body/div[2]/div/div[3]/div/div[2]/button[2]"
        )
        transferer_button.click()
        print("transferer_button.click()")

        time.sleep(5)

        # Outlook

        # Open a new window
        browser.execute_script("window.open('');")

        # Switch to the new window and open new URL
        browser.switch_to.window(browser.window_handles[1])

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
        email_input.send_keys("")
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

        # Switch to the last window
        browser.switch_to.window(browser.window_handles[0])

        time.sleep(5)

        code_input = browser.find_element_by_xpath(
            '/html/body/div[2]/div/div[3]/form/div[1]/div/input'
        )
        code_input.clear()
        code_input.send_keys(str(code))
        print("code_input inserted")

        time.sleep(5)

        # click on the button "Vérification"
        verification_button = browser.find_element_by_xpath(
            '/html/body/div[2]/div/div[3]/form/div[2]/button[2]'
        )
        verification_button.click()
        print("verification_button.click()")

        time.sleep(20)

        # Display "Vous avez terminé!" text
        termine_text = browser.find_element_by_xpath(
            "/html/body/div[2]/div/div[3]/div/div[1]"
        ).text
        print("termine_text : " + str(termine_text))

        time.sleep(5)

        # Switch to the last window
        browser.switch_to.window(browser.window_handles[1])

        time.sleep(5)

        # click on the button "Sélectionner tous les messages"
        selectionner_tous_les_messages_button = browser.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div[2]/div[1]/div/div/div[3]/div[2]/div/div[1]/div[1]/div[1]/div/div[1]'
            '/div/i[2]'
        )
        selectionner_tous_les_messages_button.click()
        print("selectionner_tous_les_messages_button.click()")

        time.sleep(5)

        # click on the button "Vider Prioritaire"
        vider_prioritaire_button = browser.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div[2]/div[1]/div/div/div[3]/div[1]/div/div/div/div/div/div[1]/div[1]/button'
        )
        vider_prioritaire_button.click()
        print("vider_prioritaire_button.click()")

        time.sleep(7)

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
    def test_send_several_emails_with_one_file_with_headless_for_developpeur_python(self):
        print("test_send_several_emails_with_one_file_with_headless_for_developpeur_python")

        emails = [

        ]

        i = 0

        for email in emails:
            envoye_a = email.lower()

            objet = "Candidature spontanée pour un emploi en tant que développeur Python " \
                    "en contrat à durée indéterminée à temps plein -  "

            message = """Bonjour,

Je vous envoie mon CV pour postuler à un emploi en tant que développeur Python.

En attendant votre retour, je vous prie de croire, mes salutations les plus sincères.

 
Ingénieur généraliste diplômé de l'École Supérieure d'Ingénieurs Léonard de Vinci
Téléphone : """

            file_upload = "C:\\Users\\DELL\\Documents\\Outils\\Desktop_Automation" \
                          "\\[Developpeur_Python].pdf"

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
            browser.get('https://wetransfer.com/')

            time.sleep(10)

            # click on the button "Non merci"
            non_merci_button = browser.find_element_by_xpath(
                "/html/body/div[2]/div/div[2]/div[2]/div[2]/div[1]/div[3]/div[4]/button[3]"
            )
            non_merci_button.click()
            print("non_merci_button.click()")

            time.sleep(5)

            # click on the button "J'accepte"
            j_accepte_button = browser.find_element_by_xpath(
                "/html/body/div[2]/div/div[3]/div/div[2]/button"
            )
            j_accepte_button.click()
            print("j_accepte_button.click()")

            time.sleep(5)

            envoye_a_input = browser.find_element_by_xpath(
                "/html/body/div[2]/div/div[3]/div/div[1]/div[1]/div[2]/div[1]/div/div/input"
            )
            envoye_a_input.clear()
            envoye_a_input.send_keys(envoye_a)
            print("envoye_a_input inserted : " + str(envoye_a))

            time.sleep(5)

            votre_adresse_input = browser.find_element_by_xpath(
                "/html/body/div[2]/div/div[3]/div/div[1]/div[1]/div[2]/div[2]/input"
            )
            votre_adresse_input.clear()
            votre_adresse_input.send_keys("")
            print("votre_adresse_input inserted")

            time.sleep(5)

            titre_input = browser.find_element_by_xpath(
                '//*[@id="displayName"]'
            )
            titre_input.clear()
            titre_input.send_keys(objet)
            print("titre_input inserted")

            time.sleep(5)

            file_input = browser.find_element_by_xpath(
                "/html/body/div[2]/div/div[3]/div/div[1]/div[1]/div[1]/form/input[1]"
            )
            file_input.send_keys(
                file_upload
            )
            print("file_input inserted")

            time.sleep(5)

            message_input = browser.find_element_by_xpath(
                '//*[@id="message"]'
            )
            message_input.clear()
            message_input.send_keys(
                message
            )
            print("message_input inserted")

            time.sleep(10)

            # click on the button "Transférer"
            transferer_button = browser.find_element_by_xpath(
                "/html/body/div[2]/div/div[3]/div/div[2]/button[2]"
            )
            transferer_button.click()
            print("transferer_button.click()")

            time.sleep(5)

            # Outlook

            # Open a new window
            browser.execute_script("window.open('');")

            # Switch to the new window and open new URL
            browser.switch_to.window(browser.window_handles[1])

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
            email_input.send_keys("")
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

            # Switch to the last window
            browser.switch_to.window(browser.window_handles[0])

            time.sleep(5)

            code_input = browser.find_element_by_xpath(
                '/html/body/div[2]/div/div[3]/form/div[1]/div/input'
            )
            code_input.clear()
            code_input.send_keys(str(code))
            print("code_input inserted")

            time.sleep(5)

            # click on the button "Vérification"
            verification_button = browser.find_element_by_xpath(
                '/html/body/div[2]/div/div[3]/form/div[2]/button[2]'
            )
            verification_button.click()
            print("verification_button.click()")

            time.sleep(20)

            # Display "Vous avez terminé!" text
            termine_text = browser.find_element_by_xpath(
                "/html/body/div[2]/div/div[3]/div/div[1]"
            ).text
            print("termine_text : " + str(termine_text))

            time.sleep(5)

            # Switch to the last window
            browser.switch_to.window(browser.window_handles[1])

            time.sleep(5)

            # click on the button "Sélectionner tous les messages"
            selectionner_tous_les_messages_button = browser.find_element_by_xpath(
                '/html/body/div[3]/div/div[2]/div[2]/div[1]/div/div/div[3]/div[2]/div/div[1]/div[1]/div[1]/div/div[1]'
                '/div/i[2]'
            )
            selectionner_tous_les_messages_button.click()
            print("selectionner_tous_les_messages_button.click()")

            time.sleep(5)

            # click on the button "Vider Prioritaire"
            vider_prioritaire_button = browser.find_element_by_xpath(
                '/html/body/div[3]/div/div[2]/div[2]/div[1]/div/div/div[3]/div[1]/div/div/div/div/div/div[1]/div[1]/button'
            )
            vider_prioritaire_button.click()
            print("vider_prioritaire_button.click()")

            time.sleep(7)

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

            i += 1

            if i % 30 == 0:
                print("test_reboot")

                try:
                    time.sleep(5)

                    warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

                    time.sleep(5)

                    # with Firefox
                    options = Options()
                    options.headless = True
                    browser = webdriver.Firefox(
                        executable_path='geckodriver.exe',
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
                    print('password_input.send_keys()')

                    time.sleep(10)

                    log_in_button = browser.find_element_by_xpath(
                        "/html/body/div[3]/div[2]/div[2]/div[1]/div[2]/div[3]/div/button"
                    )
                    log_in_button.click()
                    print('log_in_button.click()')

                    time.sleep(20)

                    reboot_button = browser.find_element_by_xpath(
                        '//*[@id="topReboot"]'
                    )
                    reboot_button.click()
                    print('reboot_button.click()')

                    time.sleep(5)

                    yes_button = browser.find_element_by_xpath(
                        '/html/body/div[7]/div/div[4]/div/div[2]/div/div[2]/button'
                    )
                    yes_button.click()
                    print('yes_button.click()')

                    time.sleep(120)

                    log_out_button = browser.find_element_by_xpath(
                        "/html/body/div[1]/div[1]/div/div[3]/a[2]"
                    )
                    log_out_button.click()
                    print('log_out_button.click()')

                    time.sleep(5)

                    yes_button = browser.find_element_by_xpath(
                        '/html/body/div[7]/div/div[4]/div/div[2]/div/div[2]/button'
                    )
                    yes_button.click()
                    print('yes_button.click()')

                    time.sleep(5)

                    browser.quit()
                    print('browser.quit()')
                except Exception as e:
                    print("error : " + str(e))

    # ok
    def test_kill_some_processes(self):
        print("test_kill_some_processes")

        subprocess.call("taskkill /F /IM geckodriver.exe")
        subprocess.call("taskkill /F /IM firefox.exe")


if __name__ == '__main__':
    unittest.main()
