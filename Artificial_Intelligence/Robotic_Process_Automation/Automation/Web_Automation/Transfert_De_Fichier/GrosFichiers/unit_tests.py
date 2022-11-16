import subprocess
import unittest
import time
import warnings
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


class UnitTestsWebAutomationTransferNowWithoutHeadless(unittest.TestCase):
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
        browser.get('https://www.grosfichiers.com/')

        time.sleep(5)

    # ok
    def test_send_one_transfer_for_developpeur_python(self):
        print("test_send_one_transfer_for_developpeur_python")

        votre_adresse_email = ""
        nom_expediteur = ""
        email_destinataire = ""
        objet = "Candidature spontanée pour un emploi en tant que développeur Python " \
                "en contrat à durée indéterminée à temps plein - "
        message = """Bonjour,

Je vous envoie mon CV pour postuler pour un emploi en tant que développeur Python.

En attendant votre retour, je vous prie de croire, mes salutations les plus sincères.


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
        browser.get('https://www.grosfichiers.com/')

        time.sleep(10)

        # Click on the 'Poursuivre' button
        poursuivre_button = browser.find_element_by_xpath(
            '//*[@id="rgpd_ok_btn"]'
        )
        poursuivre_button.click()
        print("poursuivre_button.click()")

        time.sleep(5)

        # Click on the "file_upload" button
        file_upload_input = browser.find_element_by_xpath(
            '/html/body/div[3]/div/div/div[2]/div/form/div[1]/div[3]/input'
        )
        file_upload_input.send_keys(
            file_upload
        )
        print("file_upload_input.send_keys()")

        time.sleep(7)

        # Click on the "demarrer_transfert_fichiers" button
        try:
            demarrer_transfert_fichiers_button = browser.find_element_by_xpath(
                '/html/body/div[3]/div/div/div[2]/div/form/div[3]/h2[1]'
            )
            demarrer_transfert_fichiers_button.click()
            print("demarrer_transfert_fichiers_button.click()")

            time.sleep(7)
        except Exception as e:
            print('error demarrer_transfert_fichiers : ' + str(e))

        # Display "Transfert terminé" text
        transfert_termine_text = browser.find_element_by_xpath(
            '//*[@id="_2_num"]'
        ).text
        print("transfert_termine_text : " + str(transfert_termine_text))

        time.sleep(7)

        # Click on the "Composez votre message" button
        composez_votre_message_button = browser.find_element_by_xpath(
            '/html/body/div[3]/div/div/div[2]/div/form/div[5]/h2'
        )
        composez_votre_message_button.click()
        print("composez_votre_message_button.click()")

        time.sleep(7)

        # Insert the "Votre nom" text
        votre_nom_text = browser.find_element_by_xpath(
            '//*[@id="sender_name"]'
        )
        votre_nom_text.send_keys(nom_expediteur)
        print("votre_nom_text.send_keys()")

        time.sleep(7)

        # Insert the "Votre email" text
        votre_email_text = browser.find_element_by_xpath(
            '//*[@id="sender_email"]'
        )
        votre_email_text.send_keys(votre_adresse_email)
        print("votre_email_text.send_keys()")

        time.sleep(7)

        # Insert the "Email du destinataire" text
        email_destinataire_text = browser.find_element_by_xpath(
            '//*[@id="recipient_email_array"]'
        )
        email_destinataire_text.send_keys(email_destinataire)
        print("email_destinataire_text.send_keys()")

        time.sleep(7)

        # Click on the "return_receipt_box" button
        return_receipt_box_button = browser.find_element_by_xpath(
            '//*[@id="return_receipt_box"]'
        )
        return_receipt_box_button.click()
        print("return_receipt_box_button.click()")

        time.sleep(7)

        # Insert the "Objet de l'email" text
        objet_email_text = browser.find_element_by_xpath(
            '//*[@id="email_object"]'
        )
        objet_email_text.send_keys(objet)
        print("objet_email_text.send_keys()")

        time.sleep(7)

        # Insert the "Contenu" text
        contenu_text = browser.find_element_by_xpath(
            '//*[@id="email_content"]'
        )
        contenu_text.send_keys(message)
        print("contenu_text.send_keys()")

        time.sleep(7)

        # Click on the "Envoyez votre message et vos fichiers" button
        envoyez_votre_message_button = browser.find_element_by_xpath(
            '//*[@id="_4_send"]'
        )
        envoyez_votre_message_button.click()
        print("envoyez_votre_message_button.click()")

        time.sleep(7)

        # Display "Félicitations et merci d'utiliser notre service !" text
        felicitations = browser.find_element_by_xpath(
            '/html/body/div[3]/div/div/div[1]/h1'
        ).text
        print('felicitations : ' + str(felicitations))

        time.sleep(7)

    # ok
    def test_send_several_transfers_for_developpeur_python(self):
        print("test_send_several_transfers_for_developpeur_python")

        emails = [

        ]

        for email in emails:
            votre_adresse_email = ""
            nom_expediteur = ""
            email_destinataire = email.lower()
            objet = "Candidature spontanée pour un emploi en tant que développeur Python " \
                    "en contrat à durée indéterminée à temps plein - "
            message = """Bonjour,

Je vous envoie mon CV pour postuler pour un emploi en tant que développeur Python.

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
            browser = webdriver.Firefox(
                executable_path='..\\..\\geckodriver.exe'
            )

            time.sleep(5)

            # maximize window
            browser.maximize_window()

            time.sleep(5)

            # open
            browser.get('https://www.grosfichiers.com/')

            time.sleep(10)

            try:
                # Click on the 'Poursuivre' button
                poursuivre_button = browser.find_element_by_xpath(
                    '//*[@id="rgpd_ok_btn"]'
                )
                poursuivre_button.click()
                print("poursuivre_button.click()")

                time.sleep(5)

                # Click on the "file_upload" button
                file_upload_input = browser.find_element_by_xpath(
                    '/html/body/div[3]/div/div/div[2]/div/form/div[1]/div[3]/input'
                )
                file_upload_input.send_keys(
                    file_upload
                )
                print("file_upload_input.send_keys()")

                time.sleep(7)

                # Click on the "demarrer_transfert_fichiers" button
                try:
                    demarrer_transfert_fichiers_button = browser.find_element_by_xpath(
                        '/html/body/div[3]/div/div/div[2]/div/form/div[3]/h2[1]'
                    )
                    demarrer_transfert_fichiers_button.click()
                    print("demarrer_transfert_fichiers_button.click()")

                    time.sleep(7)
                except Exception as e:
                    print('error demarrer_transfert_fichiers : ' + str(e))

                # Display "Transfert terminé" text
                transfert_termine_text = browser.find_element_by_xpath(
                    '//*[@id="_2_num"]'
                ).text
                print("transfert_termine_text : " + str(transfert_termine_text))

                time.sleep(7)

                # Click on the "Composez votre message" button
                composez_votre_message_button = browser.find_element_by_xpath(
                    '/html/body/div[3]/div/div/div[2]/div/form/div[5]/h2'
                )
                composez_votre_message_button.click()
                print("composez_votre_message_button.click()")

                time.sleep(7)

                # Insert the "Votre nom" text
                votre_nom_text = browser.find_element_by_xpath(
                    '//*[@id="sender_name"]'
                )
                votre_nom_text.send_keys(nom_expediteur)
                print("votre_nom_text.send_keys()")

                time.sleep(7)

                # Insert the "Votre email" text
                votre_email_text = browser.find_element_by_xpath(
                    '//*[@id="sender_email"]'
                )
                votre_email_text.send_keys(votre_adresse_email)
                print("votre_email_text.send_keys()")

                time.sleep(7)

                # Insert the "Email du destinataire" text
                email_destinataire_text = browser.find_element_by_xpath(
                    '//*[@id="recipient_email_array"]'
                )
                email_destinataire_text.send_keys(email_destinataire)
                print("email_destinataire_text.send_keys()")

                time.sleep(7)

                # Click on the "return_receipt_box" button
                return_receipt_box_button = browser.find_element_by_xpath(
                    '//*[@id="return_receipt_box"]'
                )
                return_receipt_box_button.click()
                print("return_receipt_box_button.click()")

                time.sleep(7)

                # Insert the "Objet de l'email" text
                objet_email_text = browser.find_element_by_xpath(
                    '//*[@id="email_object"]'
                )
                objet_email_text.send_keys(objet)
                print("objet_email_text.send_keys()")

                time.sleep(7)

                # Insert the "Contenu" text
                contenu_text = browser.find_element_by_xpath(
                    '//*[@id="email_content"]'
                )
                contenu_text.send_keys(message)
                print("contenu_text.send_keys()")

                time.sleep(7)

                # Click on the "Envoyez votre message et vos fichiers" button
                envoyez_votre_message_button = browser.find_element_by_xpath(
                    '//*[@id="_4_send"]'
                )
                envoyez_votre_message_button.click()
                print("envoyez_votre_message_button.click()")

                time.sleep(7)

                # Display "Félicitations et merci d'utiliser notre service !" text
                felicitations = browser.find_element_by_xpath(
                    '/html/body/div[3]/div/div/div[1]'
                ).text
                print('felicitations : ' + str(felicitations))

                time.sleep(10)

                browser.quit()
            except Exception as e:
                print('error : ' + str(e))

                browser.quit()

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
                except Exception as e:
                    print("error : " + str(e))


class UnitTestsWebAutomationTransferNowWithHeadless(unittest.TestCase):
    # ok
    def test_kill_some_processes(self):
        print("test_kill_some_processes")

        subprocess.call("taskkill /F /IM geckodriver.exe")
        subprocess.call("taskkill /F /IM firefox.exe")

    # ok
    def test_send_several_transfers_for_developpeur_python(self):
        print("test_send_several_transfers_for_developpeur_python")

        emails = [
        ]

        for email in emails:
            votre_adresse_email = ""

            nom_expediteur = ""

            email_destinataire = email.lower()

            objet = "Candidature spontanée pour un emploi en tant que développeur Python " \
                    "en contrat à durée indéterminée à temps plein - "

            message = """Bonjour,

Je vous envoie mon CV pour postuler pour un emploi en tant que développeur Python.

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
            browser.get('https://www.grosfichiers.com/')

            time.sleep(10)

            try:
                # Click on the 'Poursuivre' button
                poursuivre_button = browser.find_element_by_xpath(
                    '//*[@id="rgpd_ok_btn"]'
                )
                poursuivre_button.click()
                print("poursuivre_button.click()")

                time.sleep(5)

                # Click on the "file_upload" button
                file_upload_input = browser.find_element_by_xpath(
                    '/html/body/div[3]/div/div/div[2]/div/form/div[1]/div[3]/input'
                )
                file_upload_input.send_keys(
                    file_upload
                )
                print("file_upload_input.send_keys()")

                time.sleep(7)

                # Click on the "demarrer_transfert_fichiers" button
                try:
                    demarrer_transfert_fichiers_button = browser.find_element_by_xpath(
                        '/html/body/div[3]/div/div/div[2]/div/form/div[3]/h2[1]'
                    )
                    demarrer_transfert_fichiers_button.click()
                    print("demarrer_transfert_fichiers_button.click()")

                    time.sleep(7)
                except Exception as e:
                    print('error demarrer_transfert_fichiers : ' + str(e))

                # Display "Transfert terminé" text
                transfert_termine_text = browser.find_element_by_xpath(
                    '//*[@id="_2_num"]'
                ).text
                print("transfert_termine_text : " + str(transfert_termine_text))

                time.sleep(7)

                # Click on the "Composez votre message" button
                composez_votre_message_button = browser.find_element_by_xpath(
                    '/html/body/div[3]/div/div/div[2]/div/form/div[5]/h2'
                )
                composez_votre_message_button.click()
                print("composez_votre_message_button.click()")

                time.sleep(7)

                # Insert the "Votre nom" text
                votre_nom_text = browser.find_element_by_xpath(
                    '//*[@id="sender_name"]'
                )
                votre_nom_text.send_keys(nom_expediteur)
                print("votre_nom_text.send_keys()")

                time.sleep(7)

                # Insert the "Votre email" text
                votre_email_text = browser.find_element_by_xpath(
                    '//*[@id="sender_email"]'
                )
                votre_email_text.send_keys(votre_adresse_email)
                print("votre_email_text.send_keys()")

                time.sleep(7)

                # Insert the "Email du destinataire" text
                email_destinataire_text = browser.find_element_by_xpath(
                    '//*[@id="recipient_email_array"]'
                )
                email_destinataire_text.send_keys(email_destinataire)
                print("email_destinataire_text.send_keys()")

                time.sleep(7)

                # Click on the "return_receipt_box" button
                return_receipt_box_button = browser.find_element_by_xpath(
                    '//*[@id="return_receipt_box"]'
                )
                return_receipt_box_button.click()
                print("return_receipt_box_button.click()")

                time.sleep(7)

                # Insert the "Objet de l'email" text
                objet_email_text = browser.find_element_by_xpath(
                    '//*[@id="email_object"]'
                )
                objet_email_text.send_keys(objet)
                print("objet_email_text.send_keys()")

                time.sleep(7)

                # Insert the "Contenu" text
                contenu_text = browser.find_element_by_xpath(
                    '//*[@id="email_content"]'
                )
                contenu_text.send_keys(message)
                print("contenu_text.send_keys()")

                time.sleep(7)

                # Click on the "Envoyez votre message et vos fichiers" button
                envoyez_votre_message_button = browser.find_element_by_xpath(
                    '//*[@id="_4_send"]'
                )
                envoyez_votre_message_button.click()
                print("envoyez_votre_message_button.click()")

                time.sleep(7)

                # Display "Félicitations et merci d'utiliser notre service !" text
                felicitations = browser.find_element_by_xpath(
                    '/html/body/div[3]/div/div/div[1]'
                ).text
                print('felicitations : ' + str(felicitations))

                time.sleep(10)

                browser.quit()
            except Exception as e:
                print('error : ' + str(e))

                browser.quit()

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
    def test_send_several_transfers_for_ingenieur_energies_renouvelables(self):
        print("test_send_several_transfers_for_ingenieur_energies_renouvelables")

        emails = [
        ]

        for email in emails:
            votre_adresse_email = ""

            nom_expediteur = ""

            email_destinataire = email.lower()

            objet = "Candidature spontanée pour un emploi en tant qu'ingénieur en énergies renouvelables en contrat à durée indéterminée à temps plein - "

            message = """Bonjour,

Je vous envoie mon CV pour postuler à un emploi d’ingénieur en énergies renouvelables pour la fabrication de machines 
à énergie libre (https://github.com/Jay4C/Free-energy-devices / https://en.wikipedia.org/wiki/Zero-point_energy) 
à grande échelle.

En attendant votre retour, je vous prie de croire, mes salutations les plus sincères.


Ingénieur généraliste diplômé de l’Ecole Supérieure d'Ingénieurs Léonard de Vinci à Paris La Défense
Téléphone : """

            file_upload = "C:\\Users\\DELL\\Documents\\Outils\\Desktop_Automation" \
                          "\\CV_Jason_ALOYAU_[Ingenieur_Energies_Renouvelables].pdf"

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
            browser.get('https://www.grosfichiers.com/')

            time.sleep(10)

            try:
                # Click on the 'Poursuivre' button
                poursuivre_button = browser.find_element_by_xpath(
                    '//*[@id="rgpd_ok_btn"]'
                )
                poursuivre_button.click()
                print("poursuivre_button.click()")

                time.sleep(5)

                # Click on the "file_upload" button
                file_upload_input = browser.find_element_by_xpath(
                    '/html/body/div[3]/div/div/div[2]/div/form/div[1]/div[3]/input'
                )
                file_upload_input.send_keys(
                    file_upload
                )
                print("file_upload_input.send_keys()")

                time.sleep(7)

                # Click on the "demarrer_transfert_fichiers" button
                try:
                    demarrer_transfert_fichiers_button = browser.find_element_by_xpath(
                        '/html/body/div[3]/div/div/div[2]/div/form/div[3]/h2[1]'
                    )
                    demarrer_transfert_fichiers_button.click()
                    print("demarrer_transfert_fichiers_button.click()")

                    time.sleep(7)
                except Exception as e:
                    print('error demarrer_transfert_fichiers : ' + str(e))

                # Display "Transfert terminé" text
                transfert_termine_text = browser.find_element_by_xpath(
                    '//*[@id="_2_num"]'
                ).text
                print("transfert_termine_text : " + str(transfert_termine_text))

                time.sleep(7)

                # Click on the "Composez votre message" button
                composez_votre_message_button = browser.find_element_by_xpath(
                    '/html/body/div[3]/div/div/div[2]/div/form/div[5]/h2'
                )
                composez_votre_message_button.click()
                print("composez_votre_message_button.click()")

                time.sleep(7)

                # Insert the "Votre nom" text
                votre_nom_text = browser.find_element_by_xpath(
                    '//*[@id="sender_name"]'
                )
                votre_nom_text.send_keys(nom_expediteur)
                print("votre_nom_text.send_keys()")

                time.sleep(7)

                # Insert the "Votre email" text
                votre_email_text = browser.find_element_by_xpath(
                    '//*[@id="sender_email"]'
                )
                votre_email_text.send_keys(votre_adresse_email)
                print("votre_email_text.send_keys()")

                time.sleep(7)

                # Insert the "Email du destinataire" text
                email_destinataire_text = browser.find_element_by_xpath(
                    '//*[@id="recipient_email_array"]'
                )
                email_destinataire_text.send_keys(email_destinataire)
                print("email_destinataire_text.send_keys()")

                time.sleep(7)

                # Click on the "return_receipt_box" button
                return_receipt_box_button = browser.find_element_by_xpath(
                    '//*[@id="return_receipt_box"]'
                )
                return_receipt_box_button.click()
                print("return_receipt_box_button.click()")

                time.sleep(7)

                # Insert the "Objet de l'email" text
                objet_email_text = browser.find_element_by_xpath(
                    '//*[@id="email_object"]'
                )
                objet_email_text.send_keys(objet)
                print("objet_email_text.send_keys()")

                time.sleep(7)

                # Insert the "Contenu" text
                contenu_text = browser.find_element_by_xpath(
                    '//*[@id="email_content"]'
                )
                contenu_text.send_keys(message)
                print("contenu_text.send_keys()")

                time.sleep(7)

                # Click on the "Envoyez votre message et vos fichiers" button
                envoyez_votre_message_button = browser.find_element_by_xpath(
                    '//*[@id="_4_send"]'
                )
                envoyez_votre_message_button.click()
                print("envoyez_votre_message_button.click()")

                time.sleep(7)

                # Display "Félicitations et merci d'utiliser notre service !" text
                felicitations = browser.find_element_by_xpath(
                    '/html/body/div[3]/div/div/div[1]'
                ).text
                print('felicitations : ' + str(felicitations))

                time.sleep(10)

                browser.quit()
            except Exception as e:
                print('error : ' + str(e))

                browser.quit()

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
    def test_send_several_transfers_for_renewable_energy_engineer(self):
        print("test_send_several_transfers_for_renewable_energy_engineer")

        emails = [

        ]

        for email in emails:
            votre_adresse_email = ""

            nom_expediteur = ""

            email_destinataire = email.lower()

            objet = "Spontaneous application for a job as a renewable energy engineer on a full-time contract " \
                    "of indefinite duration - Mr Jason ALOYAU"

            message = """Hello, 

I am sending you my resume to apply for a job as a renewable energy engineer for manufacturing free energy machines 
(https://github.com/Jay4C/Free-energy-devices / https://en.wikipedia.org/wiki/Zero-point_energy) on a large scale.

While waiting for your return, please believe, my most sincere greetings.

Jason ALOYAU
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
            browser.get('https://www.grosfichiers.com/')

            time.sleep(10)

            try:
                # Click on the 'Poursuivre' button
                poursuivre_button = browser.find_element_by_xpath(
                    '//*[@id="rgpd_ok_btn"]'
                )
                poursuivre_button.click()
                print("poursuivre_button.click()")

                time.sleep(5)

                # Click on the "file_upload" button
                file_upload_input = browser.find_element_by_xpath(
                    '/html/body/div[3]/div/div/div[2]/div/form/div[1]/div[3]/input'
                )
                file_upload_input.send_keys(
                    file_upload
                )
                print("file_upload_input.send_keys()")

                time.sleep(7)

                # Click on the "demarrer_transfert_fichiers" button
                try:
                    demarrer_transfert_fichiers_button = browser.find_element_by_xpath(
                        '/html/body/div[3]/div/div/div[2]/div/form/div[3]/h2[1]'
                    )
                    demarrer_transfert_fichiers_button.click()
                    print("demarrer_transfert_fichiers_button.click()")

                    time.sleep(7)
                except Exception as e:
                    print('error demarrer_transfert_fichiers : ' + str(e))

                # Display "Transfert terminé" text
                transfert_termine_text = browser.find_element_by_xpath(
                    '//*[@id="_2_num"]'
                ).text
                print("transfert_termine_text : " + str(transfert_termine_text))

                time.sleep(7)

                # Click on the "Composez votre message" button
                composez_votre_message_button = browser.find_element_by_xpath(
                    '/html/body/div[3]/div/div/div[2]/div/form/div[5]/h2'
                )
                composez_votre_message_button.click()
                print("composez_votre_message_button.click()")

                time.sleep(7)

                # Insert the "Votre nom" text
                votre_nom_text = browser.find_element_by_xpath(
                    '//*[@id="sender_name"]'
                )
                votre_nom_text.send_keys(nom_expediteur)
                print("votre_nom_text.send_keys()")

                time.sleep(7)

                # Insert the "Votre email" text
                votre_email_text = browser.find_element_by_xpath(
                    '//*[@id="sender_email"]'
                )
                votre_email_text.send_keys(votre_adresse_email)
                print("votre_email_text.send_keys()")

                time.sleep(7)

                # Insert the "Email du destinataire" text
                email_destinataire_text = browser.find_element_by_xpath(
                    '//*[@id="recipient_email_array"]'
                )
                email_destinataire_text.send_keys(email_destinataire)
                print("email_destinataire_text.send_keys()")

                time.sleep(7)

                # Click on the "return_receipt_box" button
                return_receipt_box_button = browser.find_element_by_xpath(
                    '//*[@id="return_receipt_box"]'
                )
                return_receipt_box_button.click()
                print("return_receipt_box_button.click()")

                time.sleep(7)

                # Insert the "Objet de l'email" text
                objet_email_text = browser.find_element_by_xpath(
                    '//*[@id="email_object"]'
                )
                objet_email_text.send_keys(objet)
                print("objet_email_text.send_keys()")

                time.sleep(7)

                # Insert the "Contenu" text
                contenu_text = browser.find_element_by_xpath(
                    '//*[@id="email_content"]'
                )
                contenu_text.send_keys(message)
                print("contenu_text.send_keys()")

                time.sleep(7)

                # Click on the "Envoyez votre message et vos fichiers" button
                envoyez_votre_message_button = browser.find_element_by_xpath(
                    '//*[@id="_4_send"]'
                )
                envoyez_votre_message_button.click()
                print("envoyez_votre_message_button.click()")

                time.sleep(7)

                # Display "Félicitations et merci d'utiliser notre service !" text
                felicitations = browser.find_element_by_xpath(
                    '/html/body/div[3]/div/div/div[1]'
                ).text
                print('felicitations : ' + str(felicitations))

                time.sleep(10)

                browser.quit()
            except Exception as e:
                print('error : ' + str(e))

                browser.quit()

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
    def test_send_several_transfers_for_demande_devis_bornage_parcelle(self):
        print("test_send_several_transfers_for_demande_devis_bornage_parcelle")

        emails = [

        ]

        for email in emails:
            votre_adresse_email = ""

            nom_expediteur = ""

            email_destinataire = email.lower()

            objet = "Demande de devis pour un bornage d'une parcelle dans la commune de Viarmes (95270) - "

            message = """Bonjour,

Je voudrai borner une parcelle sise dans la commune de Viarmes (95270), et je joins en pièce jointe 
le plan de situation dont la référence cadastrale est : E 162.

Pourriez-vous m'établir un devis pour savoir le coût total et définitif des opérations de bornage devant être menées 
sur la parcelle s'il vous plaît ?

Très bonne journée à vous,


Adresse de facturation : 
Email : 
Phone : """

            file_upload = "A:\\2_Personnel\\2_Non_Recurrentes\\9_Transactions_Immobilieres_Personnelles" \
                          "\\2__France__Ile_De_France__Viarmes__Terrain__168_m2\\1_Extrait_Matrice_Cadastrale" \
                          "\\Extrait_Plan_E_162_Viarmes.pdf"

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
            browser.get('https://www.grosfichiers.com/')

            time.sleep(10)

            try:
                # Click on the 'Poursuivre' button
                poursuivre_button = browser.find_element_by_xpath(
                    '//*[@id="rgpd_ok_btn"]'
                )
                poursuivre_button.click()
                print("poursuivre_button.click()")

                time.sleep(5)

                # Click on the "file_upload" button
                file_upload_input = browser.find_element_by_xpath(
                    '/html/body/div[3]/div/div/div[2]/div/form/div[1]/div[3]/input'
                )
                file_upload_input.send_keys(
                    file_upload
                )
                print("file_upload_input.send_keys()")

                time.sleep(7)

                # Click on the "demarrer_transfert_fichiers" button
                try:
                    demarrer_transfert_fichiers_button = browser.find_element_by_xpath(
                        '/html/body/div[3]/div/div/div[2]/div/form/div[3]/h2[1]'
                    )
                    demarrer_transfert_fichiers_button.click()
                    print("demarrer_transfert_fichiers_button.click()")

                    time.sleep(7)
                except Exception as e:
                    print('error demarrer_transfert_fichiers : ' + str(e))

                # Display "Transfert terminé" text
                transfert_termine_text = browser.find_element_by_xpath(
                    '//*[@id="_2_num"]'
                ).text
                print("transfert_termine_text : " + str(transfert_termine_text))

                time.sleep(7)

                # Click on the "Composez votre message" button
                composez_votre_message_button = browser.find_element_by_xpath(
                    '/html/body/div[3]/div/div/div[2]/div/form/div[5]/h2'
                )
                composez_votre_message_button.click()
                print("composez_votre_message_button.click()")

                time.sleep(7)

                # Insert the "Votre nom" text
                votre_nom_text = browser.find_element_by_xpath(
                    '//*[@id="sender_name"]'
                )
                votre_nom_text.send_keys(nom_expediteur)
                print("votre_nom_text.send_keys()")

                time.sleep(7)

                # Insert the "Votre email" text
                votre_email_text = browser.find_element_by_xpath(
                    '//*[@id="sender_email"]'
                )
                votre_email_text.send_keys(votre_adresse_email)
                print("votre_email_text.send_keys()")

                time.sleep(7)

                # Insert the "Email du destinataire" text
                email_destinataire_text = browser.find_element_by_xpath(
                    '//*[@id="recipient_email_array"]'
                )
                email_destinataire_text.send_keys(email_destinataire)
                print("email_destinataire_text.send_keys()")

                time.sleep(7)

                # Click on the "return_receipt_box" button
                return_receipt_box_button = browser.find_element_by_xpath(
                    '//*[@id="return_receipt_box"]'
                )
                return_receipt_box_button.click()
                print("return_receipt_box_button.click()")

                time.sleep(7)

                # Insert the "Objet de l'email" text
                objet_email_text = browser.find_element_by_xpath(
                    '//*[@id="email_object"]'
                )
                objet_email_text.send_keys(objet)
                print("objet_email_text.send_keys()")

                time.sleep(7)

                # Insert the "Contenu" text
                contenu_text = browser.find_element_by_xpath(
                    '//*[@id="email_content"]'
                )
                contenu_text.send_keys(message)
                print("contenu_text.send_keys()")

                time.sleep(7)

                # Click on the "Envoyez votre message et vos fichiers" button
                envoyez_votre_message_button = browser.find_element_by_xpath(
                    '//*[@id="_4_send"]'
                )
                envoyez_votre_message_button.click()
                print("envoyez_votre_message_button.click()")

                time.sleep(7)

                # Display "Félicitations et merci d'utiliser notre service !" text
                felicitations = browser.find_element_by_xpath(
                    '/html/body/div[3]/div/div/div[1]'
                ).text
                print('felicitations : ' + str(felicitations))

                time.sleep(10)

                browser.quit()
            except Exception as e:
                print('error : ' + str(e))

                browser.quit()

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


if __name__ == '__main__':
    unittest.main()
