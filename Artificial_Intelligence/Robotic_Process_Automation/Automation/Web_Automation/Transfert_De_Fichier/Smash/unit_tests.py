import subprocess
import unittest
import time
import warnings
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import os


class UnitTestsWebAutomationSmashWithoutHeadless(unittest.TestCase):
    # ok
    def test_open_one_page(self):
        print("test_open_one_page")

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
        browser.get('https://fromsmash.com/')

        time.sleep(5)

    # ok
    def test_send_one_transfer(self):
        print("test_send_one_transfer")

        email = ""

        expediteur = ""
        print('nouveau expediteur : ' + expediteur)

        objet = ""

        message = ""

        file = "C:\\Users\\DELL\\Documents\\Outils\\Desktop_Automation\\" \
               "[Developpeur_Python__Full_stack].pdf"

        time.sleep(5)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

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
        browser.get('https://fromsmash.com/')

        time.sleep(10)

        # Click on the "J'accepte" button
        j_accepte_button = browser.find_element_by_xpath(
            "/html/body/app-root/app-cgu/div/div/div/button"
        )
        j_accepte_button.click()
        print("j_accepte_button.click()")

        time.sleep(5)

        # Click on the "Refuser" button
        refuser_button = browser.find_element_by_xpath(
            "/html/body/app-root/app-cookie/div/div/div/button[2]"
        )
        refuser_button.click()
        print("refuser_button.click()")

        time.sleep(5)

        # Click on the "file_upload" button
        file_upload = browser.find_element_by_xpath(
            "/html/body/app-root/div[1]/app-uploader/app-layout/div[1]/app-landing/div/div/app-smash-file-drop"
            "/div/div/input"
        )
        file_upload.send_keys(file)
        print("file_upload.send_keys(file)")

        time.sleep(10)

        # Insert the email_input
        email_input = browser.find_element_by_xpath(
            '/html/body/app-root/div[1]/app-uploader/app-layout/div[1]/app-prepare/div/app-smash-file-drop/div/div'
            '/div/div/app-upload-parameters-box/div/div[2]/app-email-form/form/perfect-scrollbar/div/div[1]/div/div[1]'
            '/div/div[1]/app-smash-input/label/input'
        )
        email_input.clear()
        email_input.send_keys(email)
        print("email_input.send_keys(email)")

        time.sleep(5)

        # Insert the expediteur_input
        expediteur_input = browser.find_element_by_xpath(
            '/html/body/app-root/div[1]/app-uploader/app-layout/div[1]/app-prepare/div/app-smash-file-drop'
            '/div/div/div/div/app-upload-parameters-box/div/div[2]/app-email-form/form/perfect-scrollbar/div'
            '/div[1]/div/div[2]/app-smash-input-tag/div/div[1]/div/input'
        )
        expediteur_input.clear()
        expediteur_input.send_keys(expediteur)
        print("expediteur_input.send_keys(expediteur)")

        time.sleep(5)

        # Insert the objet_input
        objet_input = browser.find_element_by_xpath(
            '/html/body/app-root/div[1]/app-uploader/app-layout/div[1]/app-prepare/div/app-smash-file-drop/div/div'
            '/div/div/app-upload-parameters-box/div/div[2]/app-email-form/form/perfect-scrollbar/div/div[1]/div'
            '/div[3]/app-smash-input/label/input'
        )
        objet_input.clear()
        objet_input.send_keys(objet)
        print("objet_input.send_keys(objet)")

        time.sleep(5)

        # Insert the message_input
        message_input = browser.find_element_by_xpath(
            '/html/body/app-root/div[1]/app-uploader/app-layout/div[1]/app-prepare/div/app-smash-file-drop/div/div/div'
            '/div/app-upload-parameters-box/div/div[2]/app-email-form/form/perfect-scrollbar/div/div[1]/div'
            '/app-smash-input-message/div/textarea'
        )
        message_input.clear()
        message_input.send_keys(message)
        print("message_input.send_keys(message)")

        time.sleep(5)

        # Click on the "Envoyer" button
        envoyer_button = browser.find_element_by_xpath(
            '//*[@id="button-send-transfer-email"]'
        )
        envoyer_button.click()
        print("envoyer_button.click()")

        time.sleep(30)

        # Print the "voir_le_transfert_text" text
        voir_le_transfert_text = browser.find_element_by_xpath(
            '/html/body/app-root/div[1]/app-uploader/app-layout/div[1]/app-send/div/div/app-upload-progress/div'
            '/div[2]/div/div/label/a'
        ).text
        print("voir_le_transfert_text : " + str(voir_le_transfert_text))

        time.sleep(10)

        # Print the "voir_le_transfert_text" text
        icon_browser_text = browser.title
        print("icon_browser_text : " + str(icon_browser_text))

        time.sleep(10)

    # ok
    def test_send_many_transfers_for_freelance(self):
        print("test_send_many_transfers_for_freelance")

        mails = [
            ""
        ]

        for mail in mails:
            email = ""

            expediteur = mail
            print('nouveau expediteur : ' + expediteur)

            objet = "Candidature spontanée pour une mission en tant que développeur python en freelance - "

            message = """Bonjour,

Je vous communique mes coordonnées pour une mission en tant que développeur python.

Après, je suis disponible immédiatement, et je travaille en présentiel dans la région Ile-de-France et en télétravail pour les autres régions.

Puis, mon tarif journalier s'élève à 300 euros hors taxes, et je vous prie de bien vouloir m'envoyer vos cahiers des charges.

En attendant votre décision, je vous prie de croire, mes salutations les plus sincères.


Président de la société Holomorphe
Ingénieur généraliste diplômé de l'École Supérieure d'Ingénieurs Léonard de Vinci à Paris La Défense
Adresse du siège social : 31 Avenue de Ségur 75007 Paris
Téléphone : 
SIREN : 883632556
GitHub : https://www.github.com/Jay4C"""

            file = "C:\\Users\\DELL\\Documents\\Outils\\Desktop_Automation\\" \
                   "[Developpeur_Python__Full_stack].pdf"

            time.sleep(5)

            warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

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
            browser.get('https://fromsmash.com/')

            time.sleep(10)

            # Click on the "J'accepte" button
            j_accepte_button = browser.find_element_by_xpath(
                "/html/body/app-root/app-cgu/div/div/div/button"
            )
            j_accepte_button.click()
            print("j_accepte_button.click()")

            time.sleep(5)

            # Click on the "Refuser" button
            refuser_button = browser.find_element_by_xpath(
                "/html/body/app-root/app-cookie/div/div/div/button[2]"
            )
            refuser_button.click()
            print("refuser_button.click()")

            time.sleep(5)

            # Click on the "file_upload" button
            file_upload = browser.find_element_by_xpath(
                "/html/body/app-root/div[1]/app-uploader/app-layout/div[1]/app-landing/div/div/app-smash-file-drop"
                "/div/div/input"
            )
            file_upload.send_keys(file)
            print("file_upload.send_keys(file)")

            time.sleep(10)

            # Insert the email_input
            email_input = browser.find_element_by_xpath(
                '/html/body/app-root/div[1]/app-uploader/app-layout/div[1]/app-prepare/div/app-smash-file-drop/div/div'
                '/div/div/app-upload-parameters-box/div/div[2]/app-email-form/form/perfect-scrollbar/div/div[1]/div/div[1]'
                '/div/div[1]/app-smash-input/label/input'
            )
            email_input.clear()
            email_input.send_keys(email)
            print("email_input.send_keys(email)")

            time.sleep(5)

            # Insert the expediteur_input
            expediteur_input = browser.find_element_by_xpath(
                '/html/body/app-root/div[1]/app-uploader/app-layout/div[1]/app-prepare/div/app-smash-file-drop'
                '/div/div/div/div/app-upload-parameters-box/div/div[2]/app-email-form/form/perfect-scrollbar/div'
                '/div[1]/div/div[2]/app-smash-input-tag/div/div[1]/div/input'
            )
            expediteur_input.clear()
            expediteur_input.send_keys(expediteur)
            print("expediteur_input.send_keys(expediteur)")

            time.sleep(5)

            # Insert the objet_input
            objet_input = browser.find_element_by_xpath(
                '/html/body/app-root/div[1]/app-uploader/app-layout/div[1]/app-prepare/div/app-smash-file-drop/div/div'
                '/div/div/app-upload-parameters-box/div/div[2]/app-email-form/form/perfect-scrollbar/div/div[1]/div'
                '/div[3]/app-smash-input/label/input'
            )
            objet_input.clear()
            objet_input.send_keys(objet)
            print("objet_input.send_keys(objet)")

            time.sleep(5)

            # Insert the message_input
            message_input = browser.find_element_by_xpath(
                '/html/body/app-root/div[1]/app-uploader/app-layout/div[1]/app-prepare/div/app-smash-file-drop/div/div/div'
                '/div/app-upload-parameters-box/div/div[2]/app-email-form/form/perfect-scrollbar/div/div[1]/div'
                '/app-smash-input-message/div/textarea'
            )
            message_input.clear()
            message_input.send_keys(message)
            print("message_input.send_keys(message)")

            time.sleep(5)

            # Click on the "Envoyer" button
            envoyer_button = browser.find_element_by_xpath(
                '//*[@id="button-send-transfer-email"]'
            )
            envoyer_button.click()
            print("envoyer_button.click()")

            time.sleep(30)

            # Print the "voir_le_transfert_text" text
            voir_le_transfert_text = browser.find_element_by_xpath(
                '/html/body/app-root/div[1]/app-uploader/app-layout/div[1]/app-send/div/div/app-upload-progress/div'
                '/div[2]/div/div/label/a'
            ).text
            print("voir_le_transfert_text : " + str(voir_le_transfert_text))

            time.sleep(10)

            # Print the "voir_le_transfert_text" text
            icon_browser_text = browser.title
            print("icon_browser_text : " + str(icon_browser_text))

            time.sleep(10)

            browser.quit()
            print('browser.quit()')

            time.sleep(10)

    # ok
    def test_send_many_transfers_for_yoojo(self):
        print("test_send_many_transfers_for_yoojo")

        mails = [
            ""
        ]

        for mail in mails:
            email = ""

            destinataire = mail.replace('site-solocal.', '')

            print('nouveau destinataire : ' + destinataire)

            objet = "Conseil et assistance pour la conception et la fabrication de machine à énergie libre - "

            message = """Bonjour,

Je vous communique mes coordonnées pour vous apporter mes conseils et mes assistances pour la conception et la fabrication de machine à énergie libre pour la production d'électricité bas carbone.

Je travaille en présentiel en tant que particulier, et mon tarif horaire s'élève à 30 euros.

Vous pouvez voir une liste de machines à énergie libre aux liens suivants : https://github.com/Jay4C/Free-energy-devices et https://www.youtube.com/watch?v=PSEPVsnd1_M

En attendant votre décision, je vous prie de croire, mes salutations les plus sincères.


Ingénieur généraliste diplômé de l'École Supérieure d'Ingénieurs Léonard de Vinci à Paris La Défense
Téléphone : 
GitHub : https://www.github.com/Jay4C"""

            file = "C:\\Users\\DELL\\Documents\\Outils\\Desktop_Automation\\Isometric.pdf"

            time.sleep(5)

            warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

            time.sleep(5)

            # with Firefox
            options = Options()
            options.headless = False
            browser = webdriver.Firefox(
                executable_path='..\\..\\geckodriver.exe',
                options=options
            )

            time.sleep(5)

            # maximize window
            browser.maximize_window()

            time.sleep(5)

            # open
            browser.get('https://fromsmash.com/')

            time.sleep(10)

            # Click on the "J'accepte" button
            j_accepte_button = browser.find_element_by_xpath(
                "/html/body/app-root/app-cgu/div/div/div/button"
            )
            j_accepte_button.click()
            print("j_accepte_button.click()")

            time.sleep(5)

            # Click on the "Refuser" button
            refuser_button = browser.find_element_by_xpath(
                "/html/body/app-root/app-cookie/div/div/div/button[2]"
            )
            refuser_button.click()
            print("refuser_button.click()")

            time.sleep(5)

            # Click on the "file_upload" button
            file_upload = browser.find_element_by_xpath(
                "/html/body/app-root/div[1]/app-uploader/app-layout/div[1]/app-landing/div/div/app-smash-file-drop"
                "/div/div/input"
            )
            file_upload.send_keys(file)
            print("file_upload.send_keys(file)")

            time.sleep(10)

            # Insert the email_input
            email_input = browser.find_element_by_xpath(
                '/html/body/app-root/div[1]/app-uploader/app-layout/div[1]/app-prepare/div/app-smash-file-drop/div/div'
                '/div/div/app-upload-parameters-box/div/div[2]/app-email-form/form/perfect-scrollbar/div/div[1]/div/div[1]'
                '/div/div[1]/app-smash-input/label/input'
            )
            email_input.clear()
            email_input.send_keys(email)
            print("email_input.send_keys(email)")

            time.sleep(5)

            # Insert the expediteur_input
            expediteur_input = browser.find_element_by_xpath(
                '/html/body/app-root/div[1]/app-uploader/app-layout/div[1]/app-prepare/div/app-smash-file-drop'
                '/div/div/div/div/app-upload-parameters-box/div/div[2]/app-email-form/form/perfect-scrollbar/div'
                '/div[1]/div/div[2]/app-smash-input-tag/div/div[1]/div/input'
            )
            expediteur_input.clear()
            expediteur_input.send_keys(destinataire)
            print("expediteur_input.send_keys(destinataire)")

            time.sleep(5)

            # Insert the objet_input
            objet_input = browser.find_element_by_xpath(
                '/html/body/app-root/div[1]/app-uploader/app-layout/div[1]/app-prepare/div/app-smash-file-drop/div/div'
                '/div/div/app-upload-parameters-box/div/div[2]/app-email-form/form/perfect-scrollbar/div/div[1]/div'
                '/div[3]/app-smash-input/label/input'
            )
            objet_input.clear()
            objet_input.send_keys(objet)
            print("objet_input.send_keys(objet)")

            time.sleep(5)

            # Insert the message_input
            message_input = browser.find_element_by_xpath(
                '/html/body/app-root/div[1]/app-uploader/app-layout/div[1]/app-prepare/div/app-smash-file-drop/div/div/div'
                '/div/app-upload-parameters-box/div/div[2]/app-email-form/form/perfect-scrollbar/div/div[1]/div'
                '/app-smash-input-message/div/textarea'
            )
            message_input.clear()
            message_input.send_keys(message)
            print("message_input.send_keys(message)")

            time.sleep(5)

            # Click on the "Envoyer" button
            envoyer_button = browser.find_element_by_xpath(
                '//*[@id="button-send-transfer-email"]'
            )
            envoyer_button.click()
            print("envoyer_button.click()")

            time.sleep(30)

            # Print the "voir_le_transfert_text" text
            voir_le_transfert_text = browser.find_element_by_xpath(
                '/html/body/app-root/div[1]/app-uploader/app-layout/div[1]/app-send/div/div/app-upload-progress/div'
                '/div[2]/div/div/label/a'
            ).text
            print("voir_le_transfert_text : " + str(voir_le_transfert_text))

            time.sleep(10)

            # Print the "voir_le_transfert_text" text
            icon_browser_text = browser.title
            print("icon_browser_text : " + str(icon_browser_text))

            time.sleep(10)

            browser.quit()
            print('browser.quit()')

            time.sleep(10)

    # ok
    def test_send_many_transfers_for_selling_vmeg(self):
        print("test_send_many_transfers_for_selling_vmeg")

        mails = [
            ""
        ]

        i = 0

        for mail in mails:
            try:
                email = ""

                destinataire = mail.replace('site-solocal.', '')

                print('nouveau destinataire : ' + destinataire)

                objet = "Presentation of my vibrating magnet electromagnetic generator for the generation of electricity - "

                message = """Hello,
                
First of all, I built a machine called "Vibrating magnet electromagnetic generator" for the generation of electricity by extracting magnetic energy from some vibrating permanent magnets.

My invention doesn't require oil, gas, coal, solar energy, wind energy, geothermal energy or hydraulic energy to operate, and it has no parts in motion.

After, I can design my invention to your energy needs for the internal purposes of your company, and you can reach me at anytime at :  for asking me more information about my invention.

Besides, you can have a look to my invention in the attachment.

Looking forward for your return, please believe, my sincere greetings.


Phone : 
GitHub : https://www.github.com/Jay4C"""

                file = "C:\\Users\\DELL\\Documents\\Outils\\Desktop_Automation\\assembly_v1_1.png"

                time.sleep(5)

                warnings.filterwarnings(
                    action="ignore",
                    message="unclosed",
                    category=ResourceWarning
                )

                time.sleep(5)

                # with Firefox
                options = Options()
                options.headless = False
                browser = webdriver.Firefox(
                    executable_path='..\\..\\geckodriver.exe',
                    options=options
                )

                time.sleep(5)

                # maximize window
                browser.maximize_window()

                time.sleep(5)

                # open
                browser.get('https://fromsmash.com/')

                time.sleep(10)

                # Click on the "J'accepte" button
                j_accepte_button = browser.find_element_by_xpath(
                    "/html/body/app-root/app-cgu/div/div/div/button"
                )
                j_accepte_button.click()
                print("j_accepte_button.click()")

                time.sleep(5)

                # Click on the "Refuser" button
                refuser_button = browser.find_element_by_xpath(
                    "/html/body/app-root/app-cookie/div/div/div/button[2]"
                )
                refuser_button.click()
                print("refuser_button.click()")

                time.sleep(5)

                # Click on the "file_upload" button
                file_upload = browser.find_element_by_xpath(
                    "/html/body/app-root/div[1]/app-uploader/app-layout/div[1]/app-landing/div/div/app-smash-file-drop"
                    "/div/div/input"
                )
                file_upload.send_keys(file)
                print("file_upload.send_keys(file)")

                time.sleep(10)

                # Insert the email_input
                email_input = browser.find_element_by_xpath(
                    '/html/body/app-root/div[1]/app-uploader/app-layout/div[1]/app-prepare/div/app-smash-file-drop/div/div'
                    '/div/div/app-upload-parameters-box/div/div[2]/app-email-form/form/perfect-scrollbar/div/div[1]/div/div[1]'
                    '/div/div[1]/app-smash-input/label/input'
                )
                email_input.clear()
                email_input.send_keys(email)
                print("email_input.send_keys(email)")

                time.sleep(5)

                # Insert the expediteur_input
                expediteur_input = browser.find_element_by_xpath(
                    '/html/body/app-root/div[1]/app-uploader/app-layout/div[1]/app-prepare/div/app-smash-file-drop'
                    '/div/div/div/div/app-upload-parameters-box/div/div[2]/app-email-form/form/perfect-scrollbar/div'
                    '/div[1]/div/div[2]/app-smash-input-tag/div/div[1]/div/input'
                )
                expediteur_input.clear()
                expediteur_input.send_keys(destinataire)
                print("expediteur_input.send_keys(destinataire)")

                time.sleep(5)

                # Insert the objet_input
                objet_input = browser.find_element_by_xpath(
                    '/html/body/app-root/div[1]/app-uploader/app-layout/div[1]/app-prepare/div/app-smash-file-drop/div/div'
                    '/div/div/app-upload-parameters-box/div/div[2]/app-email-form/form/perfect-scrollbar/div/div[1]/div'
                    '/div[3]/app-smash-input/label/input'
                )
                objet_input.clear()
                objet_input.send_keys(objet)
                print("objet_input.send_keys(objet)")

                time.sleep(5)

                # Insert the message_input
                message_input = browser.find_element_by_xpath(
                    '/html/body/app-root/div[1]/app-uploader/app-layout/div[1]/app-prepare/div/app-smash-file-drop/div/div/div'
                    '/div/app-upload-parameters-box/div/div[2]/app-email-form/form/perfect-scrollbar/div/div[1]/div'
                    '/app-smash-input-message/div/textarea'
                )
                message_input.clear()
                message_input.send_keys(message)
                print("message_input.send_keys(message)")

                time.sleep(5)

                # Click on the "Envoyer" button
                envoyer_button = browser.find_element_by_xpath(
                    '//*[@id="button-send-transfer-email"]'
                )
                envoyer_button.click()
                print("envoyer_button.click()")

                time.sleep(30)

                try:
                    # Print the "voir_le_transfert_text" text
                    voir_le_transfert_text = browser.find_element_by_xpath(
                        '/html/body/app-root/div[1]/app-uploader/app-layout/div[1]/app-send/div/div/app-upload-progress/div'
                        '/div[2]/div/div/label/a'
                    ).text
                    print("voir_le_transfert_text : " + str(voir_le_transfert_text))
                except Exception as e:
                    print("error voir_le_transfert_text : " + str(e))

                time.sleep(10)

                # Print the "voir_le_transfert_text" text
                icon_browser_text = browser.title
                print("icon_browser_text : " + str(icon_browser_text))

                time.sleep(10)

                browser.quit()
                print('browser.quit()')

                time.sleep(10)

                i += 1

                if i % 30 == 0:
                    try:
                        print("test_reboot")

                        time.sleep(5)

                        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

                        time.sleep(5)

                        # with Firefox
                        browser = webdriver.Firefox(executable_path='geckodriver.exe')

                        time.sleep(5)

                        # maximize window
                        browser.maximize_window()

                        time.sleep(5)

                        # open
                        browser.get('http://www.tplinkmodem.net')

                        time.sleep(15)

                        password_input = browser.find_element_by_xpath(
                            "/html/body/div[3]/div[2]/div[2]/div[1]/div[2]/div[2]/div/div/div[1]/input[1]"
                        )
                        password_input.clear()
                        password_input.send_keys("")

                        time.sleep(10)

                        log_in_button = browser.find_element_by_xpath(
                            "/html/body/div[3]/div[2]/div[2]/div[1]/div[2]/div[3]/div/button"
                        )
                        log_in_button.click()

                        time.sleep(20)

                        reboot_button = browser.find_element_by_xpath(
                            '//*[@id="topReboot"]'
                        )
                        reboot_button.click()

                        time.sleep(5)

                        yes_button = browser.find_element_by_xpath(
                            '/html/body/div[7]/div/div[4]/div/div[2]/div/div[2]/button'
                        )
                        yes_button.click()

                        time.sleep(120)

                        browser.quit()
                    except Exception as e:
                        print("error : " + str(e))

                    time.sleep(10)

                    subprocess.call("taskkill /F /IM geckodriver.exe")
                    subprocess.call("taskkill /F /IM firefox.exe")

                    time.sleep(10)

                    print("run_ccleaner")
                    os.system("set ccleaner='C:\\Program Files\\CCleaner\\CCleaner64.exe'")
                    os.system("start ccleaner /AUTO")

                    time.sleep(60)
            except Exception as e:
                print('error main : ' + str(e))

                try:
                    print("test_reboot")

                    time.sleep(5)

                    warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

                    time.sleep(5)

                    # with Firefox
                    browser = webdriver.Firefox(executable_path='geckodriver.exe')

                    time.sleep(5)

                    # maximize window
                    browser.maximize_window()

                    time.sleep(5)

                    # open
                    browser.get('http://www.tplinkmodem.net')

                    time.sleep(15)

                    password_input = browser.find_element_by_xpath(
                        "/html/body/div[3]/div[2]/div[2]/div[1]/div[2]/div[2]/div/div/div[1]/input[1]"
                    )
                    password_input.clear()
                    password_input.send_keys("")

                    time.sleep(10)

                    log_in_button = browser.find_element_by_xpath(
                        "/html/body/div[3]/div[2]/div[2]/div[1]/div[2]/div[3]/div/button"
                    )
                    log_in_button.click()

                    time.sleep(20)

                    reboot_button = browser.find_element_by_xpath(
                        '//*[@id="topReboot"]'
                    )
                    reboot_button.click()

                    time.sleep(5)

                    yes_button = browser.find_element_by_xpath(
                        '/html/body/div[7]/div/div[4]/div/div[2]/div/div[2]/button'
                    )
                    yes_button.click()

                    time.sleep(120)

                    browser.quit()

                    time.sleep(10)

                    subprocess.call("taskkill /F /IM geckodriver.exe")
                    subprocess.call("taskkill /F /IM firefox.exe")

                    time.sleep(10)

                    print("run_ccleaner")
                    os.system("set ccleaner='C:\\Program Files\\CCleaner\\CCleaner64.exe'")
                    os.system("start ccleaner /AUTO")

                    time.sleep(60)
                except Exception as e:
                    print("error : " + str(e))

                time.sleep(10)

                subprocess.call("taskkill /F /IM geckodriver.exe")
                subprocess.call("taskkill /F /IM firefox.exe")

                time.sleep(10)

                print("run_ccleaner")
                os.system("set ccleaner='C:\\Program Files\\CCleaner\\CCleaner64.exe'")
                os.system("start ccleaner /AUTO")

                time.sleep(60)

    # ok
    def test_send_many_transfers_for_integrating_smwe_with_ice(self):
        print("test_send_many_transfers_for_integrating_smwe_with_ice")

        options = Options()
        options.headless = False

        mails = [
            ""
        ]

        i = 0

        for mail in mails:
            try:
                email = "j",

                destinataire = mail.replace('site-solocal.', '')

                print('nouveau destinataire : ' + destinataire)

                objet = "Candidature spontanée pour un poste en contrat à durée indéterminée en tant qu'ingénieur en nouvelles technologies d'hydrogène / Spontaneous application for a position on a permanent contract as an engineer in new hydrogen technologies – Jason ALOYAU"

                message = """Bonjour,

Tout d'abord, je vous communique mes coordonnées pour une candidature spontanée pour un poste en contrat à durée indéterminée en tant qu'ingénieur en nouvelles technologies d'hydrogène pour intégrer le générateur d'hydrogène gazeux par électrolyse de l'eau de Stanley Meyer sur vos machines thermiques.

Après, je serai très ravi d'intégrer une équipe au sein de votre entreprise pour concevoir, développer et intégrer le générateur d'hydrogène gazeux par électrolyse de l'eau de Stanley Meyer sur vos machines thermiques et vos processus.

Actuellement, je développe des générateurs d'hydrogène gazeux par électrolyse de l'eau de Stanley Meyer avec des scripts Python sous le logiciel FreeCAD, et je travaille essentiellement avec le langage de programmation Python pour mes programmes informatiques.

De plus, j'exploite les brevets numérotés US5149407, US4389981, EP0111573, US4798661, US4936961, US4124463 pour développer mes générateurs d'hyrogène gazeux par électrolyse de l'eau de Stanley Meyer.

Ainsi, vous pouvez trouver en pièce jointe une de mes conceptions d'un générateur industriel d'hydrogène gazeux par électrolyse de l'eau de Stanley Meyer.

En attendant votre décision, je vous prie de croire, mes sincères salutations.


Ingénieur généraliste diplômé à l'Ecole Supérieure d'Ingénieurs Léonard de Vinci à Paris La Défense
Téléphone : 
LinkedIn : https://www.linkedin.com/in/jason-aloyau-531727239/
GitHub : https://github.com/Jay4C/Python-Macros-For-FreeCAD/tree/master/Brevet_us_4_124_463_water_electrolyzer_3
YouTube : https://www.youtube.com/watch?v=tdqsBnzXrE8

---

Hello,

First of all, I am sending you my contact details for a spontaneous application for a position on a permanent contract as an engineer in new hydrogen technologies to integrate Stanley Meyer's hydrogen gas generator by water electrolysis on your thermal machines.

Afterwards, I will be very happy to integrate a team within your company to design, develop and integrate Stanley Meyer's hydrogen gas generator by electrolysis of water on your thermal machines and your processes.

Currently, I am developing Stanley Meyer water electrolysis hydrogen gas generators with Python scripts under FreeCAD software, and I mainly work with Python programming language for my computer programs.

In addition, I exploit the patents numbered US5149407, US4389981, EP0111573, US4798661, US4936961, US4124463 to develop my gaseous hydrogen generators by water electrolysis by Stanley Meyer.

Thus, you can find attached one of my designs for an industrial hydrogen gas generator by water electrolysis by Stanley Meyer.

Waiting for your decision, please believe, my sincere greetings.


General engineer graduated from the Leonardo da Vinci School of Engineering in Paris La Défense
Telephone: 
LinkedIn: https://www.linkedin.com/in/jason-aloyau-531727239/
GitHub: https://github.com/Jay4C/Python-Macros-For-FreeCAD/tree/master/Brevet_us_4_124_463_water_electrolyzer_3
YouTube: https://www.youtube.com/watch?v=tdqsBnzXrE8"""

                file = "C:\\Users\\DELL\\Documents\\Outils\\Desktop_Automation\\assembly_global_1.png"

                time.sleep(5)

                warnings.filterwarnings(
                    action="ignore",
                    message="unclosed",
                    category=ResourceWarning
                )

                time.sleep(5)

                # with Firefox
                browser = webdriver.Firefox(
                    executable_path='..\\..\\geckodriver.exe',
                    options=options
                )

                time.sleep(5)

                # maximize window
                browser.maximize_window()

                time.sleep(5)

                # open
                browser.get('https://fromsmash.com/')

                time.sleep(10)

                # Click on the "J'accepte" button
                j_accepte_button = browser.find_element_by_xpath(
                    "/html/body/app-root/app-cgu/div/div/div/button"
                )
                j_accepte_button.click()
                print("j_accepte_button.click()")

                time.sleep(5)

                # Click on the "Refuser" button
                refuser_button = browser.find_element_by_xpath(
                    "/html/body/app-root/app-cookie/div/div/div/button[2]"
                )
                refuser_button.click()
                print("refuser_button.click()")

                time.sleep(5)

                # Click on the "file_upload" button
                file_upload = browser.find_element_by_xpath(
                    "/html/body/app-root/div[1]/app-uploader/app-layout/div[1]/app-landing/div/div/app-smash-file-drop"
                    "/div/div/input"
                )
                file_upload.send_keys(file)
                print("file_upload.send_keys(file)")

                time.sleep(10)

                # Insert the email_input
                email_input = browser.find_element_by_xpath(
                    '/html/body/app-root/div[1]/app-uploader/app-layout/div[1]/app-prepare/div/app-smash-file-drop/div/div'
                    '/div/div/app-upload-parameters-box/div/div[2]/app-email-form/form/perfect-scrollbar/div/div[1]/div/div[1]'
                    '/div/div[1]/app-smash-input/label/input'
                )
                email_input.clear()
                email_input.send_keys(email)
                print("email_input.send_keys(email)")

                time.sleep(5)

                # Insert the expediteur_input
                expediteur_input = browser.find_element_by_xpath(
                    '/html/body/app-root/div[1]/app-uploader/app-layout/div[1]/app-prepare/div/app-smash-file-drop'
                    '/div/div/div/div/app-upload-parameters-box/div/div[2]/app-email-form/form/perfect-scrollbar/div'
                    '/div[1]/div/div[2]/app-smash-input-tag/div/div[1]/div/input'
                )
                expediteur_input.clear()
                expediteur_input.send_keys(destinataire)
                print("expediteur_input.send_keys(destinataire)")

                time.sleep(5)

                # Insert the objet_input
                objet_input = browser.find_element_by_xpath(
                    '/html/body/app-root/div[1]/app-uploader/app-layout/div[1]/app-prepare/div/app-smash-file-drop/div/div'
                    '/div/div/app-upload-parameters-box/div/div[2]/app-email-form/form/perfect-scrollbar/div/div[1]/div'
                    '/div[3]/app-smash-input/label/input'
                )
                objet_input.clear()
                objet_input.send_keys(objet)
                print("objet_input.send_keys(objet)")

                time.sleep(5)

                # Insert the message_input
                message_input = browser.find_element_by_xpath(
                    '/html/body/app-root/div[1]/app-uploader/app-layout/div[1]/app-prepare/div/app-smash-file-drop/div/div/div'
                    '/div/app-upload-parameters-box/div/div[2]/app-email-form/form/perfect-scrollbar/div/div[1]/div'
                    '/app-smash-input-message/div/textarea'
                )
                message_input.clear()
                message_input.send_keys(message)
                print("message_input.send_keys(message)")

                time.sleep(5)

                # Click on the "Envoyer" button
                envoyer_button = browser.find_element_by_xpath(
                    '//*[@id="button-send-transfer-email"]'
                )
                envoyer_button.click()
                print("envoyer_button.click()")

                time.sleep(30)

                try:
                    # Print the "voir_le_transfert_text" text
                    voir_le_transfert_text = browser.find_element_by_xpath(
                        '/html/body/app-root/div[1]/app-uploader/app-layout/div[1]/app-send/div/div/app-upload-progress/div'
                        '/div[2]/div/div/label/a'
                    ).text
                    print("voir_le_transfert_text : " + str(voir_le_transfert_text))
                except Exception as e:
                    print("error voir_le_transfert_text : " + str(e))

                time.sleep(10)

                # Print the "voir_le_transfert_text" text
                icon_browser_text = browser.title
                print("icon_browser_text : " + str(icon_browser_text))

                time.sleep(10)

                browser.quit()
                print('browser.quit()')

                time.sleep(10)

                i += 1

                if i % 30 == 0:
                    try:
                        print("test_reboot")

                        time.sleep(5)

                        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

                        time.sleep(5)

                        # with Firefox
                        browser = webdriver.Firefox(executable_path='geckodriver.exe')

                        time.sleep(5)

                        # maximize window
                        browser.maximize_window()

                        time.sleep(5)

                        # open
                        browser.get('http://www.tplinkmodem.net')

                        time.sleep(15)

                        password_input = browser.find_element_by_xpath(
                            "/html/body/div[3]/div[2]/div[2]/div[1]/div[2]/div[2]/div/div/div[1]/input[1]"
                        )
                        password_input.clear()
                        password_input.send_keys("")

                        time.sleep(10)

                        log_in_button = browser.find_element_by_xpath(
                            "/html/body/div[3]/div[2]/div[2]/div[1]/div[2]/div[3]/div/button"
                        )
                        log_in_button.click()

                        time.sleep(20)

                        reboot_button = browser.find_element_by_xpath(
                            '//*[@id="topReboot"]'
                        )
                        reboot_button.click()

                        time.sleep(5)

                        yes_button = browser.find_element_by_xpath(
                            '/html/body/div[7]/div/div[4]/div/div[2]/div/div[2]/button'
                        )
                        yes_button.click()

                        time.sleep(120)

                        browser.quit()
                    except Exception as e:
                        print("error : " + str(e))

                    time.sleep(10)

                    subprocess.call("taskkill /F /IM geckodriver.exe")
                    subprocess.call("taskkill /F /IM firefox.exe")

                    time.sleep(10)

                    print("run_ccleaner")
                    os.system("set ccleaner='C:\\Program Files\\CCleaner\\CCleaner64.exe'")
                    os.system("start ccleaner /AUTO")

                    time.sleep(60)
            except Exception as e:
                print('error main : ' + str(e))

                try:
                    print("test_reboot")

                    time.sleep(5)

                    warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

                    time.sleep(5)

                    # with Firefox
                    browser = webdriver.Firefox(executable_path='geckodriver.exe')

                    time.sleep(5)

                    # maximize window
                    browser.maximize_window()

                    time.sleep(5)

                    # open
                    browser.get('http://www.tplinkmodem.net')

                    time.sleep(15)

                    password_input = browser.find_element_by_xpath(
                        "/html/body/div[3]/div[2]/div[2]/div[1]/div[2]/div[2]/div/div/div[1]/input[1]"
                    )
                    password_input.clear()
                    password_input.send_keys("")

                    time.sleep(10)

                    log_in_button = browser.find_element_by_xpath(
                        "/html/body/div[3]/div[2]/div[2]/div[1]/div[2]/div[3]/div/button"
                    )
                    log_in_button.click()

                    time.sleep(20)

                    reboot_button = browser.find_element_by_xpath(
                        '//*[@id="topReboot"]'
                    )
                    reboot_button.click()

                    time.sleep(5)

                    yes_button = browser.find_element_by_xpath(
                        '/html/body/div[7]/div/div[4]/div/div[2]/div/div[2]/button'
                    )
                    yes_button.click()

                    time.sleep(120)

                    browser.quit()

                    time.sleep(10)

                    subprocess.call("taskkill /F /IM geckodriver.exe")
                    subprocess.call("taskkill /F /IM firefox.exe")

                    time.sleep(10)

                    print("run_ccleaner")
                    os.system("set ccleaner='C:\\Program Files\\CCleaner\\CCleaner64.exe'")
                    os.system("start ccleaner /AUTO")

                    time.sleep(60)
                except Exception as e:
                    print("error : " + str(e))

                time.sleep(10)

                subprocess.call("taskkill /F /IM geckodriver.exe")
                subprocess.call("taskkill /F /IM firefox.exe")

                time.sleep(10)

                print("run_ccleaner")
                os.system("set ccleaner='C:\\Program Files\\CCleaner\\CCleaner64.exe'")
                os.system("start ccleaner /AUTO")

                time.sleep(60)

    # ok
    def test_send_many_transfers_for_injecting_gas_from_biogas_site(self):
        print("test_send_many_transfers_for_injecting_gas_from_biogas_site")

        options = Options()
        options.headless = True

        mails = [
            ""
        ]

        i = 0

        for mail in mails:
            try:
                email = "",

                destinataire = mail.replace('site-solocal.', '')

                print('nouveau destinataire : ' + destinataire)

                objet = "Demande de partenariat pour la vente d'hydrogène gazeux par le biais du réseau de gaz naturel – Société Holomorphe (Paris) \ Partnership application for the sale of hydrogen gas through the natural gas network – Company Holomorphe (Paris)"

                message = """Bonjour,

Je vous communique mes coordonnées pour ma demande de partenariat pour la vente d'hydrogène gazeux par le biais du réseau de gaz naturel.

Après, la production d'hydrogène gazeux sera vendue aux fournisseurs de gaz naturel par le biais du réseau de gaz naturel, et la vente de cette production sera répartie équitablement entre les partenaires du projet quel que soit leur niveau d'investissement.

Puis, je travaille sur le générateur d'hydrogène gazeux par électrolyse de l'eau de Stanley Meyer.

Ensuite, je mets en pièce jointe un aperçu du générateur d'hydrogène gazeux par électrolyse de l'eau de la société Holomorphe.

Ainsi, j'aurai besoin de savoir la quantité d'hydrogène gazeux pouvant être injecter dans le réseau de gaz naturel depuis vos installations pour calculer la puissance électrique nécessaire du projet et sa rentabilité, et j'aurai également besoin d'obtenir la surface d'occupation disponible de vos installations pour installer les différentes briques technologiques (générateur à eau atmosphérique, générateur d'hydrogène gazeux ...).

Mes questions sont :
Quelle est la quantité totale annuelle d'hydrogène gazeux pur pouvant être injectées depuis vos installations s'il vous plaît ?
Quelle est la surface d'occupation disponible de vos installations pour installer les différentes briques technologiques s'il vous plaît ?

En attendant votre décision, je vous prie de croire, mes sincères salutations.


Président de la société Holomorphe
Ingénieur généraliste diplômé à l'Ecole Supérieure d'Ingénieurs Léonard de Vinci à Paris La Défense
Adresse du siège social : 31 Avenue de Ségur 75007 Paris
Téléphone : 
LinkedIn : https://www.linkedin.com/in/jason-aloyau-531727239/
GitHub : https://github.com/Jay4C/Python-Macros-For-FreeCAD/tree/master/Brevet_us_4_124_463_water_electrolyzer_3
YouTube : https://www.youtube.com/watch?v=tdqsBnzXrE8

---

Hello,

I am sending you my contact details for my partnership request for the sale of gaseous hydrogen through the natural gas network.

Afterwards, the hydrogen gas production will be sold to natural gas suppliers through the natural gas network, and the sale of this production will be distributed equitably among the project partners regardless of their level of investment.

Then, I work on Stanley Meyer's hydrogen gas generator by electrolysis of water.

Then, I attach an overview of the hydrogen gas generator by water electrolysis from the company Holomorphe.

Thus, I will need to know the quantity of hydrogen gas that can be injected into the natural gas network from your facilities to calculate the electrical power required for the project and its profitability, and I will also need to obtain the surface of available occupation of your facilities to install the various technological bricks (atmospheric water generator, hydrogen gas generator, etc.).

My questions are:
What is the total annual quantity of pure hydrogen gas that can be injected from your facilities please?
What is the available occupation surface of your facilities to install the different technological bricks please?

Waiting for your decision, please believe, my sincere greetings.


President of the Holomorphe
General engineer graduated from the Leonardo da Vinci School of Engineering in Paris La Défense
Head office address: 31 Avenue de Ségur 75007 Paris
Telephone: 
LinkedIn: https://www.linkedin.com/in/jason-aloyau-531727239/
GitHub: https://github.com/Jay4C/Python-Macros-For-FreeCAD/tree/master/Brevet_us_4_124_463_water_electrolyzer_3
YouTube: https://www.youtube.com/watch?v=tdqsBnzXrE8"""

                file = "C:\\Users\\DELL\\Documents\\Outils\\Desktop_Automation\\assembly_global_1.png"

                time.sleep(5)

                warnings.filterwarnings(
                    action="ignore",
                    message="unclosed",
                    category=ResourceWarning
                )

                time.sleep(5)

                # with Firefox
                browser = webdriver.Firefox(
                    executable_path='..\\..\\geckodriver.exe',
                    options=options
                )

                time.sleep(5)

                # maximize window
                browser.maximize_window()

                time.sleep(5)

                # open
                browser.get('https://fromsmash.com/')

                time.sleep(10)

                # Click on the "J'accepte" button
                j_accepte_button = browser.find_element_by_xpath(
                    "/html/body/app-root/app-cgu/div/div/div/button"
                )
                j_accepte_button.click()
                print("j_accepte_button.click()")

                time.sleep(5)

                # Click on the "Refuser" button
                refuser_button = browser.find_element_by_xpath(
                    "/html/body/app-root/app-cookie/div/div/div/button[2]"
                )
                refuser_button.click()
                print("refuser_button.click()")

                time.sleep(5)

                # Click on the "file_upload" button
                file_upload = browser.find_element_by_xpath(
                    "/html/body/app-root/div[1]/app-uploader/app-layout/div[1]/app-landing/div/div/app-smash-file-drop"
                    "/div/div/input"
                )
                file_upload.send_keys(file)
                print("file_upload.send_keys(file)")

                time.sleep(10)

                # Insert the email_input
                email_input = browser.find_element_by_xpath(
                    '/html/body/app-root/div[1]/app-uploader/app-layout/div[1]/app-prepare/div/app-smash-file-drop/div/div'
                    '/div/div/app-upload-parameters-box/div/div[2]/app-email-form/form/perfect-scrollbar/div/div[1]/div/div[1]'
                    '/div/div[1]/app-smash-input/label/input'
                )
                email_input.clear()
                email_input.send_keys(email)
                print("email_input.send_keys(email)")

                time.sleep(5)

                # Insert the expediteur_input
                expediteur_input = browser.find_element_by_xpath(
                    '/html/body/app-root/div[1]/app-uploader/app-layout/div[1]/app-prepare/div/app-smash-file-drop'
                    '/div/div/div/div/app-upload-parameters-box/div/div[2]/app-email-form/form/perfect-scrollbar/div'
                    '/div[1]/div/div[2]/app-smash-input-tag/div/div[1]/div/input'
                )
                expediteur_input.clear()
                expediteur_input.send_keys(destinataire)
                print("expediteur_input.send_keys(destinataire)")

                time.sleep(5)

                # Insert the objet_input
                objet_input = browser.find_element_by_xpath(
                    '/html/body/app-root/div[1]/app-uploader/app-layout/div[1]/app-prepare/div/app-smash-file-drop/div/div'
                    '/div/div/app-upload-parameters-box/div/div[2]/app-email-form/form/perfect-scrollbar/div/div[1]/div'
                    '/div[3]/app-smash-input/label/input'
                )
                objet_input.clear()
                objet_input.send_keys(objet)
                print("objet_input.send_keys(objet)")

                time.sleep(5)

                # Insert the message_input
                message_input = browser.find_element_by_xpath(
                    '/html/body/app-root/div[1]/app-uploader/app-layout/div[1]/app-prepare/div/app-smash-file-drop/div/div/div'
                    '/div/app-upload-parameters-box/div/div[2]/app-email-form/form/perfect-scrollbar/div/div[1]/div'
                    '/app-smash-input-message/div/textarea'
                )
                message_input.clear()
                message_input.send_keys(message)
                print("message_input.send_keys(message)")

                time.sleep(5)

                # Click on the "Envoyer" button
                envoyer_button = browser.find_element_by_xpath(
                    '//*[@id="button-send-transfer-email"]'
                )
                envoyer_button.click()
                print("envoyer_button.click()")

                time.sleep(30)

                try:
                    # Print the "voir_le_transfert_text" text
                    voir_le_transfert_text = browser.find_element_by_xpath(
                        '/html/body/app-root/div[1]/app-uploader/app-layout/div[1]/app-send/div/div/app-upload-progress/div'
                        '/div[2]/div/div/label/a'
                    ).text
                    print("voir_le_transfert_text : " + str(voir_le_transfert_text))
                except Exception as e:
                    print("error voir_le_transfert_text : " + str(e))

                time.sleep(10)

                # Print the "voir_le_transfert_text" text
                icon_browser_text = browser.title
                print("icon_browser_text : " + str(icon_browser_text))

                time.sleep(10)

                browser.quit()
                print('browser.quit()')

                time.sleep(10)

                i += 1

                if i % 30 == 0:
                    try:
                        print("test_reboot")

                        time.sleep(5)

                        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

                        time.sleep(5)

                        # with Firefox
                        browser = webdriver.Firefox(executable_path='geckodriver.exe')

                        time.sleep(5)

                        # maximize window
                        browser.maximize_window()

                        time.sleep(5)

                        # open
                        browser.get('http://www.tplinkmodem.net')

                        time.sleep(15)

                        password_input = browser.find_element_by_xpath(
                            "/html/body/div[3]/div[2]/div[2]/div[1]/div[2]/div[2]/div/div/div[1]/input[1]"
                        )
                        password_input.clear()
                        password_input.send_keys("")

                        time.sleep(10)

                        log_in_button = browser.find_element_by_xpath(
                            "/html/body/div[3]/div[2]/div[2]/div[1]/div[2]/div[3]/div/button"
                        )
                        log_in_button.click()

                        time.sleep(20)

                        reboot_button = browser.find_element_by_xpath(
                            '//*[@id="topReboot"]'
                        )
                        reboot_button.click()

                        time.sleep(5)

                        yes_button = browser.find_element_by_xpath(
                            '/html/body/div[7]/div/div[4]/div/div[2]/div/div[2]/button'
                        )
                        yes_button.click()

                        time.sleep(120)

                        browser.quit()
                    except Exception as e:
                        print("error : " + str(e))

                    time.sleep(10)

                    subprocess.call("taskkill /F /IM geckodriver.exe")
                    subprocess.call("taskkill /F /IM firefox.exe")

                    time.sleep(10)

                    print("run_ccleaner")
                    os.system("set ccleaner='C:\\Program Files\\CCleaner\\CCleaner64.exe'")
                    os.system("start ccleaner /AUTO")

                    time.sleep(60)
            except Exception as e:
                print('error main : ' + str(e))

                try:
                    print("test_reboot")

                    time.sleep(5)

                    warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

                    time.sleep(5)

                    # with Firefox
                    browser = webdriver.Firefox(executable_path='geckodriver.exe')

                    time.sleep(5)

                    # maximize window
                    browser.maximize_window()

                    time.sleep(5)

                    # open
                    browser.get('http://www.tplinkmodem.net')

                    time.sleep(15)

                    password_input = browser.find_element_by_xpath(
                        "/html/body/div[3]/div[2]/div[2]/div[1]/div[2]/div[2]/div/div/div[1]/input[1]"
                    )
                    password_input.clear()
                    password_input.send_keys("")

                    time.sleep(10)

                    log_in_button = browser.find_element_by_xpath(
                        "/html/body/div[3]/div[2]/div[2]/div[1]/div[2]/div[3]/div/button"
                    )
                    log_in_button.click()

                    time.sleep(20)

                    reboot_button = browser.find_element_by_xpath(
                        '//*[@id="topReboot"]'
                    )
                    reboot_button.click()

                    time.sleep(5)

                    yes_button = browser.find_element_by_xpath(
                        '/html/body/div[7]/div/div[4]/div/div[2]/div/div[2]/button'
                    )
                    yes_button.click()

                    time.sleep(120)

                    browser.quit()

                    time.sleep(10)

                    subprocess.call("taskkill /F /IM geckodriver.exe")
                    subprocess.call("taskkill /F /IM firefox.exe")

                    time.sleep(10)

                    print("run_ccleaner")
                    os.system("set ccleaner='C:\\Program Files\\CCleaner\\CCleaner64.exe'")
                    os.system("start ccleaner /AUTO")

                    time.sleep(60)
                except Exception as e:
                    print("error : " + str(e))

                time.sleep(10)

                subprocess.call("taskkill /F /IM geckodriver.exe")
                subprocess.call("taskkill /F /IM firefox.exe")

                time.sleep(10)

                print("run_ccleaner")
                os.system("set ccleaner='C:\\Program Files\\CCleaner\\CCleaner64.exe'")
                os.system("start ccleaner /AUTO")

                time.sleep(60)

    # ok
    def test_kill_some_processes(self):
        print("test_kill_some_processes")

        subprocess.call("taskkill /F /IM geckodriver.exe")
        subprocess.call("taskkill /F /IM firefox.exe")


if __name__ == '__main__':
    unittest.main()
