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
        browser = webdriver.Firefox(executable_path='..\\geckodriver.exe')

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get('https://www.transfernow.net/')

        time.sleep(5)

    # ok
    def test_send_one_transfer(self):
        print("test_send_one_transfer")

        votre_adresse_email = ""
        nom_expediteur = ""
        email_destinataire = ""
        objet = "Candidature spontanée pour un emploi en tant qu'ingénieur en énergies renouvelables en contrat à " \
                "durée indéterminée à temps plein - Monsieur "
        message = """Bonjour,

Je vous envoie mon CV pour postuler pour un emploi en tant qu'ingénieur en énergies renouvelables pour la fabrication 
de machines à énergie libre (https://github.com/Jay4C/Free-energy-devices / 
https://en.wikipedia.org/wiki/Zero-point_energy) à grande échelle.

En attendant votre retour, je vous prie de croire, mes salutations les plus sincères.


Ingénieur généraliste diplômé de l'École Supérieure d'Ingénieurs Léonard de Vinci 
Téléphone : """

        file_upload = "C:\\Users\\DELL\\Documents\\Outils\\Desktop_Automation" \
                      "\\[Ingenieur_Energies_Renouvelables].pdf"

        time.sleep(5)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(5)

        # with Firefox
        browser = webdriver.Firefox(
            executable_path='..\\geckodriver.exe'
        )

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get('https://www.transfernow.net/')

        time.sleep(10)

        # Click on the "croix" button
        croix_button = browser.find_element_by_xpath(
            '//*[@id="axeptio_main_button"]'
        )
        croix_button.click()
        print("croix_button.click()")

        time.sleep(5)

        # Click on the "file_upload" button
        file_upload_input = browser.find_element_by_xpath(
            "/html/body/div[1]/div[1]/div[6]/div/input[1]"
        )
        file_upload_input.send_keys(
            file_upload
        )
        print("file_upload_input.send_keys()")

        time.sleep(5)

        votre_adresse_email_input = browser.find_element_by_xpath(
            "/html/body/div[1]/div[1]/div[6]/div/div[1]/div[2]/div[1]/input"
        )
        votre_adresse_email_input.send_keys(
            votre_adresse_email
        )
        print("votre_adresse_email_input.send_keys()")

        time.sleep(5)

        nom_expediteur_input = browser.find_element_by_xpath(
            "/html/body/div[1]/div[1]/div[6]/div/div[1]/div[2]/div[2]/input"
        )
        nom_expediteur_input.send_keys(
            nom_expediteur
        )
        print("nom_expediteur_input.send_keys()")

        time.sleep(5)

        email_destinataire_input = browser.find_element_by_xpath(
            '//*[@id="react-select-uploaderRecipientsSelect-input"]'
        )
        email_destinataire_input.send_keys(
            email_destinataire
        )
        print("email_destinataire_input.send_keys()")

        time.sleep(5)

        objet_input = browser.find_element_by_xpath(
            '/html/body/div[1]/div[1]/div[6]/div/div[1]/div[2]/div[4]/input'
        )
        objet_input.send_keys(
            objet
        )
        print("objet_input.send_keys()")

        time.sleep(5)

        message_input = browser.find_element_by_xpath(
            '/html/body/div[1]/div[1]/div[6]/div/div[1]/div[2]/div[5]/textarea'
        )
        message_input.send_keys(
            message
        )
        print("message_input.send_keys()")

        time.sleep(20)

        # Click on the "croix" button
        transferer_button = browser.find_element_by_xpath(
            '//*[@id="uploaderStart"]'
        )
        transferer_button.click()
        print("transferer_button.click()")

        time.sleep(5)

    # ok
    def test_send_multi_transfers(self):
        print("test_send_multi_transfers")

        emails = [
        ]

        for email in emails:
            print("commencement du transfert pour email : " + str(email.lower()))

            votre_adresse_email = ""
            nom_expediteur = ""
            email_destinataire = email.lower()
            objet = "Candidature spontanée pour un emploi en tant qu'ingénieur en énergies renouvelables en contrat à " \
                    "durée indéterminée à temps plein - Monsieur "
            message = """Bonjour,

Je vous envoie mon CV pour postuler pour un emploi en tant qu'ingénieur en énergies renouvelables pour la fabrication 
de machines à énergie libre (https://github.com/Jay4C/Free-energy-devices / 
https://en.wikipedia.org/wiki/Zero-point_energy) à grande échelle.

En attendant votre retour, je vous prie de croire, mes salutations les plus sincères.


Ingénieur généraliste diplômé de l'École Supérieure d'Ingénieurs Léonard de Vinci 
Téléphone : """

            file_upload = "C:\\Users\\DELL\\Documents\\Outils\\Desktop_Automation" \
                          "\\[Ingenieur_Energies_Renouvelables].pdf"

            time.sleep(5)

            warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

            time.sleep(5)

            # with Firefox
            browser = webdriver.Firefox(
                executable_path='..\\geckodriver.exe'
            )

            time.sleep(5)

            # maximize window
            browser.maximize_window()

            time.sleep(5)

            # open
            browser.get('https://www.transfernow.net/')

            time.sleep(10)

            # Click on the "croix" button
            croix_button = browser.find_element_by_xpath(
                '//*[@id="axeptio_main_button"]'
            )
            croix_button.click()
            print("croix_button.click()")

            time.sleep(5)

            # Click on the "file_upload" button
            file_upload_input = browser.find_element_by_xpath(
                "/html/body/div[1]/div[1]/div[6]/div/input[1]"
            )
            file_upload_input.send_keys(
                file_upload
            )
            print("file_upload_input.send_keys()")

            time.sleep(5)

            votre_adresse_email_input = browser.find_element_by_xpath(
                "/html/body/div[1]/div[1]/div[6]/div/div[1]/div[2]/div[1]/input"
            )
            votre_adresse_email_input.send_keys(
                votre_adresse_email
            )
            print("votre_adresse_email_input.send_keys()")

            time.sleep(5)

            nom_expediteur_input = browser.find_element_by_xpath(
                "/html/body/div[1]/div[1]/div[6]/div/div[1]/div[2]/div[2]/input"
            )
            nom_expediteur_input.send_keys(
                nom_expediteur
            )
            print("nom_expediteur_input.send_keys()")

            time.sleep(5)

            email_destinataire_input = browser.find_element_by_xpath(
                '//*[@id="react-select-uploaderRecipientsSelect-input"]'
            )
            email_destinataire_input.send_keys(
                email_destinataire
            )
            print("email_destinataire_input.send_keys()")

            time.sleep(5)

            objet_input = browser.find_element_by_xpath(
                '/html/body/div[1]/div[1]/div[6]/div/div[1]/div[2]/div[4]/input'
            )
            objet_input.send_keys(
                objet
            )
            print("objet_input.send_keys()")

            time.sleep(5)

            message_input = browser.find_element_by_xpath(
                '/html/body/div[1]/div[1]/div[6]/div/div[1]/div[2]/div[5]/textarea'
            )
            message_input.send_keys(
                message
            )
            print("message_input.send_keys()")

            time.sleep(20)

            # Click on the "croix" button
            transferer_button = browser.find_element_by_xpath(
                '//*[@id="uploaderStart"]'
            )
            transferer_button.click()
            print("transferer_button.click()")

            time.sleep(20)

            print("transfert correct pour email : " + str(email.lower()))

    # ok
    def test_kill_some_processes(self):
        print("test_kill_some_processes")

        subprocess.call("taskkill /F /IM geckodriver.exe")
        subprocess.call("taskkill /F /IM firefox.exe")


class UnitTestsWebAutomationTransferNowWithHeadless(unittest.TestCase):
    # ok
    def test_send_multi_transfers_with_headless_for_france_ingenieur_energies_renouvelables(self):
        print("test_send_multi_transfers_with_headless_for_france_ingenieur_energies_renouvelables")

        emails = [
        ]

        for email in emails:
            print("commencement du transfert pour email : " + str(email.lower()))

            votre_adresse_email = ""
            nom_expediteur = ""
            email_destinataire = email.lower()
            objet = "Candidature spontanée pour un emploi en tant qu'ingénieur en énergies renouvelables " \
                    "en contrat à durée indéterminée à temps plein - Monsieur "
            message = """Bonjour,

Je vous envoie mon CV pour postuler pour un emploi en tant qu'ingénieur en énergies renouvelables pour la fabrication 
de machines à énergie libre (https://github.com/Jay4C/Free-energy-devices / 
https://en.wikipedia.org/wiki/Zero-point_energy) à grande échelle.

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

            try:
                # open
                browser.get('https://www.transfernow.net/')

                time.sleep(10)

                # Click on the "croix" button
                croix_button = browser.find_element_by_xpath(
                    '//*[@id="axeptio_main_button"]'
                )
                croix_button.click()
                print("croix_button.click()")

                time.sleep(5)

                # Click on the "file_upload" button
                file_upload_input = browser.find_element_by_xpath(
                    "/html/body/div[1]/div[1]/div[6]/div/input[1]"
                )
                file_upload_input.send_keys(
                    file_upload
                )
                print("file_upload_input.send_keys()")

                time.sleep(5)

                votre_adresse_email_input = browser.find_element_by_xpath(
                    "/html/body/div[1]/div[1]/div[6]/div/div[1]/div[2]/div[1]/input"
                )
                votre_adresse_email_input.send_keys(
                    votre_adresse_email
                )
                print("votre_adresse_email_input.send_keys()")

                time.sleep(5)

                nom_expediteur_input = browser.find_element_by_xpath(
                    "/html/body/div[1]/div[1]/div[6]/div/div[1]/div[2]/div[2]/input"
                )
                nom_expediteur_input.send_keys(
                    nom_expediteur
                )
                print("nom_expediteur_input.send_keys()")

                time.sleep(5)

                email_destinataire_input = browser.find_element_by_xpath(
                    '//*[@id="react-select-uploaderRecipientsSelect-input"]'
                )
                email_destinataire_input.send_keys(
                    email_destinataire
                )
                print("email_destinataire_input.send_keys()")

                time.sleep(5)

                objet_input = browser.find_element_by_xpath(
                    '/html/body/div[1]/div[1]/div[6]/div/div[1]/div[2]/div[4]/input'
                )
                objet_input.send_keys(
                    objet
                )
                print("objet_input.send_keys()")

                time.sleep(5)

                message_input = browser.find_element_by_xpath(
                    '/html/body/div[1]/div[1]/div[6]/div/div[1]/div[2]/div[5]/textarea'
                )
                message_input.send_keys(
                    message
                )
                print("message_input.send_keys()")

                time.sleep(20)

                # Click on the "croix" button
                transferer_button = browser.find_element_by_xpath(
                    '//*[@id="uploaderStart"]'
                )
                transferer_button.click()
                print("transferer_button.click()")

                time.sleep(20)

                print("transfert correct pour email : " + str(email.lower()))

                browser.quit()
            except Exception as e:
                time.sleep(5)

                print("transfert échoué pour email : " + str(email.lower()) + " - " + str(e))

                browser.quit()

                print("test_reboot")

                try:
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

    # ok
    def test_send_multi_transfers_with_headless_for_france_developpeur_python(self):
        print("test_send_multi_transfers_with_headless_for_france_developpeur_python")

        emails = [

        ]

        for email in emails:
            print("commencement du transfert pour email : " + str(email.lower()))

            votre_adresse_email = ""
            nom_expediteur = "Monsieur "
            email_destinataire = email.lower()
            objet = "Candidature spontanée pour un emploi en tant que développeur Python " \
                    "en contrat à durée indéterminée à temps plein - Monsieur "
            message = """Bonjour,

Je vous envoie mon CV pour postuler pour un emploi en tant que développeur Python.

En attendant votre retour, je vous prie de croire, mes salutations les plus sincères.


Ingénieur généraliste diplômé de l'École Supérieure d'Ingénieurs Léonard de Vinci 
Téléphone : """

            file_upload = "C:\\Users\\DELL\\Documents\\Outils\\Desktop_Automation" \
                          "\\CV_De_Jason_ALOYAU_[Developpeur_Python].pdf"

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
                executable_path='..\\geckodriver.exe'
            )

            time.sleep(5)

            # maximize window
            browser.maximize_window()

            time.sleep(5)

            try:
                # open
                browser.get('https://www.transfernow.net/')

                time.sleep(10)

                # Click on the "croix" button
                croix_button = browser.find_element_by_xpath(
                    '//*[@id="axeptio_main_button"]'
                )
                croix_button.click()
                print("croix_button.click()")

                time.sleep(5)

                # Click on the "file_upload" button
                file_upload_input = browser.find_element_by_xpath(
                    "/html/body/div[1]/div[1]/div[6]/div/input[1]"
                )
                file_upload_input.send_keys(
                    file_upload
                )
                print("file_upload_input.send_keys()")

                time.sleep(5)

                votre_adresse_email_input = browser.find_element_by_xpath(
                    "/html/body/div[1]/div[1]/div[6]/div/div[1]/div[2]/div[1]/input"
                )
                votre_adresse_email_input.send_keys(
                    votre_adresse_email
                )
                print("votre_adresse_email_input.send_keys()")

                time.sleep(5)

                nom_expediteur_input = browser.find_element_by_xpath(
                    "/html/body/div[1]/div[1]/div[6]/div/div[1]/div[2]/div[2]/input"
                )
                nom_expediteur_input.send_keys(
                    nom_expediteur
                )
                print("nom_expediteur_input.send_keys()")

                time.sleep(5)

                email_destinataire_input = browser.find_element_by_xpath(
                    '//*[@id="react-select-uploaderRecipientsSelect-input"]'
                )
                email_destinataire_input.send_keys(
                    email_destinataire
                )
                print("email_destinataire_input.send_keys()")

                time.sleep(5)

                objet_input = browser.find_element_by_xpath(
                    '/html/body/div[1]/div[1]/div[6]/div/div[1]/div[2]/div[4]/input'
                )
                objet_input.send_keys(
                    objet
                )
                print("objet_input.send_keys()")

                time.sleep(5)

                message_input = browser.find_element_by_xpath(
                    '/html/body/div[1]/div[1]/div[6]/div/div[1]/div[2]/div[5]/textarea'
                )
                message_input.send_keys(
                    message
                )
                print("message_input.send_keys()")

                time.sleep(20)

                # Click on the "transferer_button" button
                transferer_button = browser.find_element_by_xpath(
                    '//*[@id="uploaderStart"]'
                )
                transferer_button.click()
                print("transferer_button.click()")

                time.sleep(30)

                try:
                    c_est_termine_text = browser.find_element_by_xpath(
                        '/html/body/div[1]/div[1]/div[6]/div[1]/div/div[1]/div/div[1]'
                    ).text
                    print("c_est_termine_text : " + str(c_est_termine_text))
                except Exception as e:
                    print("error c_est_termine_text : " + str(e))

                time.sleep(5)

                print("transfert correct pour email : " + str(email.lower()))

                browser.quit()
            except Exception as e:
                time.sleep(5)

                print("transfert échoué pour email : " + str(email.lower()) + " - " + str(e))

                browser.quit()

                print("test_reboot")

                try:
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

    # ok
    def test_send_multi_transfers_with_headless_for_abroad(self):
        print("test_send_multi_transfers_with_headless_for_abroad")

        emails = [
        ]

        for email in emails:
            print("commencement du transfert pour email : " + str(email.lower()))

            votre_adresse_email = ""
            nom_expediteur = ""
            email_destinataire = email.lower()
            objet = "Spontaneous application for a job as a renewable energy engineer on a full-time contract " \
                    "of indefinite duration - "
            message = """Hello, 

I am sending you my resume to apply for a job as a renewable energy engineer for manufacturing free energy machines 
(https://github.com/Jay4C/Free-energy-devices / https://en.wikipedia.org/wiki/Zero-point_energy) on a large scale.

While waiting for your return, please believe, my most sincere greetings.


General engineer graduated from Leonardo da Vinci Engineering School
Phone : """

            file_upload = "C:\\Users\\DELL\\Documents\\Outils\\Desktop_Automation" \
                          "\\[Renewable_energy_engineer].pdf"

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
                executable_path='geckodriver.exe',
                options=options
            )

            time.sleep(5)

            # maximize window
            browser.maximize_window()

            time.sleep(5)

            try:
                # open
                browser.get('https://www.transfernow.net/')

                time.sleep(10)

                # Click on the "croix" button
                croix_button = browser.find_element_by_xpath(
                    '//*[@id="axeptio_main_button"]'
                )
                croix_button.click()
                print("croix_button.click()")

                time.sleep(5)

                # Click on the "file_upload" button
                file_upload_input = browser.find_element_by_xpath(
                    "/html/body/div[1]/div[1]/div[6]/div/input[1]"
                )
                file_upload_input.send_keys(
                    file_upload
                )
                print("file_upload_input.send_keys()")

                time.sleep(5)

                votre_adresse_email_input = browser.find_element_by_xpath(
                    "/html/body/div[1]/div[1]/div[6]/div/div[1]/div[2]/div[1]/input"
                )
                votre_adresse_email_input.send_keys(
                    votre_adresse_email
                )
                print("votre_adresse_email_input.send_keys()")

                time.sleep(5)

                nom_expediteur_input = browser.find_element_by_xpath(
                    "/html/body/div[1]/div[1]/div[6]/div/div[1]/div[2]/div[2]/input"
                )
                nom_expediteur_input.send_keys(
                    nom_expediteur
                )
                print("nom_expediteur_input.send_keys()")

                time.sleep(5)

                email_destinataire_input = browser.find_element_by_xpath(
                    '//*[@id="react-select-uploaderRecipientsSelect-input"]'
                )
                email_destinataire_input.send_keys(
                    email_destinataire
                )
                print("email_destinataire_input.send_keys()")

                time.sleep(5)

                objet_input = browser.find_element_by_xpath(
                    '/html/body/div[1]/div[1]/div[6]/div/div[1]/div[2]/div[4]/input'
                )
                objet_input.send_keys(
                    objet
                )
                print("objet_input.send_keys()")

                time.sleep(5)

                message_input = browser.find_element_by_xpath(
                    '/html/body/div[1]/div[1]/div[6]/div/div[1]/div[2]/div[5]/textarea'
                )
                message_input.send_keys(
                    message
                )
                print("message_input.send_keys()")

                time.sleep(20)

                # Click on the "croix" button
                transferer_button = browser.find_element_by_xpath(
                    '//*[@id="uploaderStart"]'
                )
                transferer_button.click()
                print("transferer_button.click()")

                time.sleep(20)

                print("transfert correct pour email : " + str(email.lower()))

                browser.quit()
            except Exception as e:
                time.sleep(5)

                print("transfert échoué pour email : " + str(email.lower()) + " - " + str(e))

                browser.quit()


if __name__ == '__main__':
    unittest.main()
