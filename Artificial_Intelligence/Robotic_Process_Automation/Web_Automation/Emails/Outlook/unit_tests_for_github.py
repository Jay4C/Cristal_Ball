import time
import warnings
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.options import Options


class UnitTestsRPAOutlook(unittest.TestCase):
    # ok
    def test_send_one_email(self):
        print('test_send_one_email')

        my_email = ''
        my_password = ''

        url = "https://outlook.live.com/owa/"

        time.sleep(5)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(5)

        # With Firefox
        options = Options()
        options.headless = False
        browser = webdriver.Firefox(
            executable_path='M:\\1_Personnel\\1_Recurrentes\\3_Outils_Numeriques\\GitHub_Jay4C\\Cristal_Ball'
                            '\\geckodriver.exe',
            options=options
        )

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get(url)

        time.sleep(5)

        # Click on the 'Connexion' button
        connexion_button = browser.find_element(
            by=By.XPATH,
            value="/html/body/header/div/aside/div/nav/ul/li[2]/a"
        )
        connexion_button.click()
        print('connexion_button.click() clicked')

        time.sleep(5)

        # Insert my email
        email_input = browser.find_element(
            by=By.XPATH,
            value='//*[@id="i0116"]'
        )
        email_input.clear()
        email_input.send_keys(
            my_email
        )
        print("email inserted")

        time.sleep(5)

        # Click on the 'Suivant' button
        suivant_button = browser.find_element(
            by=By.XPATH,
            value='//*[@id="idSIButton9"]'
        )
        suivant_button.click()
        print('suivant_button.click() clicked')

        time.sleep(5)

        # Insert my password
        password_input = browser.find_element(
            by=By.XPATH,
            value='//*[@id="i0118"]'
        )
        password_input.clear()
        password_input.send_keys(
            my_password
        )
        print("password inserted")

        time.sleep(5)

        # Click on the 'Se connecter' button
        se_connecter_button = browser.find_element(
            by=By.XPATH,
            value='//*[@id="idSIButton9"]'
        )
        se_connecter_button.click()
        print('se_connecter_button.click() clicked')

        time.sleep(5)

        # Click on the 'Ne plus afficher ce message' button
        ne_plus_afficher_ce_message_button = browser.find_element(
            by=By.XPATH,
            value='//*[@id="KmsiCheckboxField"]'
        )
        ne_plus_afficher_ce_message_button.click()
        print('ne_plus_afficher_ce_message_button.click() clicked')

        time.sleep(5)

        # Click on the 'Non' button
        non_button = browser.find_element(
            by=By.XPATH,
            value='//*[@id="idBtn_Back"]'
        )
        non_button.click()
        print('non_button.click() clicked')

        time.sleep(7)

        email_contact = ''

        subject = 'Request of information for international shipping of screws'

        message = """Hello,

Do you ship your screws internationally please ?

Kind regards,"""

        # Click on the 'Nouveau courrier' button
        nouveau_courrier_button = browser.find_element(
            by=By.XPATH,
            value='/html/body/div[2]/div/div[2]/div[2]/div[1]/div/div/div/div/div/div[1]/div[2]/div/div/button/span'
        )
        nouveau_courrier_button.click()
        print('nouveau_courrier_button.click() clicked')

        time.sleep(7)

        # Insert the email contact
        action_email = ActionChains(browser)
        action_email.send_keys(email_contact)
        time.sleep(3)
        action_email.send_keys(Keys.TAB)
        time.sleep(3)
        action_email.perform()
        print("action_email.perform() performed")

        time.sleep(7)

        # Insert the subject
        for s in range(0, 1000):
            try:
                subject_input = browser.find_element(
                    by=By.XPATH,
                    value='//*[@id="TextField' + str(s) + '"]'
                )
                subject_input.send_keys(subject)
                print('subject_input.send_keys(subject) inserted')
                break
            except Exception as e:
                print('error subject_input : ' + str(e))

        time.sleep(7)

        # Insert the message
        action_message = ActionChains(browser)
        action_message.send_keys(Keys.TAB)
        time.sleep(3)
        action_message.send_keys(message)
        time.sleep(3)
        action_message.perform()
        print("action_message.perform() performed")

        time.sleep(7)

        # Click on the 'Envoyer' button
        try:
            envoyer_button = browser.find_element(
                by=By.XPATH,
                value='/html/body/div[2]/div/div[2]/div[2]/div[1]/div/span/div/div/div/div/div[1]/div[2]/button/span'
            )
            envoyer_button.click()
            print('envoyer_button.click() clicked')
        except Exception as e:
            print('error envoyer_button : ' + str(e))

        time.sleep(7)

        # Click on the 'Profile' button
        try:
            profile_button = browser.find_element(
                by=By.XPATH,
                value='/html/body/div[2]/div/div[1]/div/div[1]/div[3]/div[1]/button/div/div[2]/div/div/div/div/div/div[2]'
            )
            profile_button.click()
            print('profile_button.click() clicked')
        except Exception as e:
            print('error profile_button : ' + str(e))

        time.sleep(7)

        # Click on the 'Se déconnecter' button
        try:
            se_deconnecter_button = browser.find_element(
                by=By.XPATH,
                value='//*[@id="mectrl_body_signOut"]'
            )
            se_deconnecter_button.click()
            print('se_deconnecter_button.click() clicked')
        except Exception as e:
            print('error se_deconnecter_button : ' + str(e))

        time.sleep(7)

        browser.quit()
        print('browser.quit()')

    #
    def test_attach_one_attachment(self):
        print('test_attach_one_attachment')

        my_email = ''
        my_password = ''

        file = 'C:\\Users\\ALOYAU MARIA\\Dropbox\\1_Personnel\\1_Recurrentes\\3_Outils_Numeriques\\GitHub_Jay4C' \
               '\\Cristal_Ball\\Archives\\Reporting\\Human_Resources\\Resume\\Resume_For_Me' \
               '\\CV_De_Jason_ALOYAU_[Developpeur_Python]_v1.pdf'

        url = "https://outlook.live.com/owa/"

        time.sleep(5)

        warnings.filterwarnings(
            action="ignore",
            message="unclosed",
            category=ResourceWarning
        )

        time.sleep(5)

        # With Firefox
        options = Options()
        options.headless = False
        browser = webdriver.Firefox(
            executable_path='C:\\Users\\ALOYAU MARIA\\Dropbox\\1_Personnel\\1_Recurrentes\\3_Outils_Numeriques'
                            '\\GitHub_Jay4C\\Cristal_Ball\\geckodriver.exe',
            options=options
        )

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get(url)

        time.sleep(5)

        # Click on the 'Connexion' button
        connexion_button = browser.find_element(
            by=By.XPATH,
            value="/html/body/header/div/aside/div/nav/ul/li[2]/a"
        )
        connexion_button.click()
        print('connexion_button.click() clicked')

        time.sleep(5)

        # Insert my email
        email_input = browser.find_element(
            by=By.XPATH,
            value='//*[@id="i0116"]'
        )
        email_input.clear()
        email_input.send_keys(
            my_email
        )
        print("email inserted")

        time.sleep(5)

        # Click on the 'Suivant' button
        suivant_button = browser.find_element(
            by=By.XPATH,
            value='//*[@id="idSIButton9"]'
        )
        suivant_button.click()
        print('suivant_button.click() clicked')

        time.sleep(5)

        # Insert my password
        password_input = browser.find_element(
            by=By.XPATH,
            value='//*[@id="i0118"]'
        )
        password_input.clear()
        password_input.send_keys(
            my_password
        )
        print("password inserted")

        time.sleep(5)

        # Click on the 'Se connecter' button
        se_connecter_button = browser.find_element(
            by=By.XPATH,
            value='//*[@id="idSIButton9"]'
        )
        se_connecter_button.click()
        print('se_connecter_button.click() clicked')

        time.sleep(5)

        # Click on the 'Ne plus afficher ce message' button
        ne_plus_afficher_ce_message_button = browser.find_element(
            by=By.XPATH,
            value='//*[@id="KmsiCheckboxField"]'
        )
        ne_plus_afficher_ce_message_button.click()
        print('ne_plus_afficher_ce_message_button.click() clicked')

        time.sleep(5)

        # Click on the 'Non' button
        non_button = browser.find_element(
            by=By.XPATH,
            value='//*[@id="idBtn_Back"]'
        )
        non_button.click()
        print('non_button.click() clicked')

        time.sleep(15)

        # Click on the 'Nouveau courrier' button
        nouveau_courrier_button = browser.find_element(
            by=By.XPATH,
            value='/html/body/div[2]/div/div[2]/div[2]/div[1]/div/div/div/div/div/div[1]/div[2]/div/div/button/span'
        )
        nouveau_courrier_button.click()
        print('nouveau_courrier_button.click() clicked')

        time.sleep(7)

        # Attach one attachment
        attachment_file_input = browser.find_element(
            by=By.XPATH,
            value='/html/body/div[2]/div/div[2]/div[2]/div[2]/div[1]/div/div/div[3]/div/div/div[2]/div[1]/div/div/div/div[3]/input[1]'
        )
        attachment_file_input.clear()
        attachment_file_input.send_keys(
            file
        )
        print("file inserted")

        time.sleep(7)

    # ok
    def test_send_several_emails(self):
        print('test_send_several_emails')

        my_email = ''

        my_password = ''

        subject = 'Request of information for international shipping of screws'

        message = """Hello,

Do you ship your screws internationally please ?

Kind regards,"""

        emails_contacts = [
            '',
            ''
        ]

        url = "https://outlook.live.com/owa/"

        time.sleep(5)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(5)

        # With Firefox
        options = Options()
        options.headless = False
        browser = webdriver.Firefox(
            executable_path='M:\\1_Personnel\\1_Recurrentes\\3_Outils_Numeriques\\GitHub_Jay4C\\Cristal_Ball'
                            '\\geckodriver.exe',
            options=options
        )

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get(url)

        time.sleep(5)

        # Click on the 'Connexion' button
        connexion_button = browser.find_element(
            by=By.XPATH,
            value="/html/body/header/div/aside/div/nav/ul/li[2]/a"
        )
        connexion_button.click()
        print('connexion_button.click() clicked')

        time.sleep(5)

        # Insert my email
        email_input = browser.find_element(
            by=By.XPATH,
            value='//*[@id="i0116"]'
        )
        email_input.clear()
        email_input.send_keys(
            my_email
        )
        print("email inserted")

        time.sleep(5)

        # Click on the 'Suivant' button
        suivant_button = browser.find_element(
            by=By.XPATH,
            value='//*[@id="idSIButton9"]'
        )
        suivant_button.click()
        print('suivant_button.click() clicked')

        time.sleep(5)

        # Insert my password
        password_input = browser.find_element(
            by=By.XPATH,
            value='//*[@id="i0118"]'
        )
        password_input.clear()
        password_input.send_keys(
            my_password
        )
        print("password inserted")

        time.sleep(5)

        # Click on the 'Se connecter' button
        se_connecter_button = browser.find_element(
            by=By.XPATH,
            value='//*[@id="idSIButton9"]'
        )
        se_connecter_button.click()
        print('se_connecter_button.click() clicked')

        time.sleep(5)

        # Click on the 'Ne plus afficher ce message' button
        ne_plus_afficher_ce_message_button = browser.find_element(
            by=By.XPATH,
            value='//*[@id="KmsiCheckboxField"]'
        )
        ne_plus_afficher_ce_message_button.click()
        print('ne_plus_afficher_ce_message_button.click() clicked')

        time.sleep(7)

        # Click on the 'Non' button
        non_button = browser.find_element(
            by=By.XPATH,
            value='//*[@id="idBtn_Back"]'
        )
        non_button.click()
        print('non_button.click() clicked')

        time.sleep(15)

        for email_contact in emails_contacts:
            # Click on the 'Nouveau courrier' button
            nouveau_courrier_button = browser.find_element(
                by=By.XPATH,
                value='/html/body/div[2]/div/div[2]/div[2]/div[1]/div/div/div/div/div/div[1]/div[2]/div/div/button/span'
            )
            nouveau_courrier_button.click()
            print('nouveau_courrier_button.click() clicked')

            time.sleep(7)

            # Insert the email contact
            action_email = ActionChains(browser)
            action_email.send_keys(email_contact)
            time.sleep(3)
            action_email.send_keys(Keys.TAB)
            time.sleep(3)
            action_email.perform()
            print("action_email.perform() performed")

            time.sleep(7)

            # Insert the subject
            for s in range(0, 1000):
                try:
                    subject_input = browser.find_element(
                        by=By.XPATH,
                        value='//*[@id="TextField' + str(s) + '"]'
                    )
                    subject_input.send_keys(subject)
                    print('subject_input.send_keys(subject) inserted')
                    break
                except Exception as e:
                    print('error subject_input : ' + str(e))

            time.sleep(7)

            # Insert the message
            action_message = ActionChains(browser)
            action_message.send_keys(Keys.TAB)
            time.sleep(3)
            action_message.send_keys(message)
            time.sleep(3)
            action_message.perform()
            print("action_message.perform() performed")

            time.sleep(7)

            # Click on the 'Envoyer' button
            try:
                envoyer_button = browser.find_element(
                    by=By.XPATH,
                    value='/html/body/div[2]/div/div[2]/div[2]/div[1]/div/span/div/div/div/div/div[1]/div[2]/button/span'
                )
                envoyer_button.click()
                print('envoyer_button.click() clicked')
            except Exception as e:
                print('error envoyer_button : ' + str(e))

            time.sleep(7)

        time.sleep(7)

        # Click on the 'Profile' button
        try:
            profile_button = browser.find_element(
                by=By.XPATH,
                value='/html/body/div[2]/div/div[1]/div/div[1]/div[3]/div[1]/button/div/div[2]/div/div/div/div/div/div[2]'
            )
            profile_button.click()
            print('profile_button.click() clicked')
        except Exception as e:
            print('error profile_button : ' + str(e))

        time.sleep(7)

        # Click on the 'Se déconnecter' button
        try:
            se_deconnecter_button = browser.find_element(
                by=By.XPATH,
                value='//*[@id="mectrl_body_signOut"]'
            )
            se_deconnecter_button.click()
            print('se_deconnecter_button.click() clicked')
        except Exception as e:
            print('error se_deconnecter_button : ' + str(e))

        time.sleep(7)

        browser.quit()
        print('browser.quit()')

    # ok
    def test_close_all_firefox_processes(self):
        print('test_close_all_firefox_processes')
        import os
        os.system("taskkill /F /IM geckodriver.exe")
        os.system("taskkill /F /IM firefox.exe")


if __name__ == '__main__':
    unittest.main()
