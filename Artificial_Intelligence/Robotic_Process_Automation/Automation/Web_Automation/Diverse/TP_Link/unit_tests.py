import subprocess
import unittest
import time
import warnings
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


class UnitTestsWebAutomationTPLinkWithoutHeadless(unittest.TestCase):
    # ok
    def test_se_connecter(self):
        print("test_se_connecter")

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

        time.sleep(5)

    # ok
    def test_show_sms(self):
        print("test_show_sms")

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
        browser.get('http://www.tplinkmodem.net')
        print('page opened')

        time.sleep(15)

        password_input = browser.find_element_by_xpath(
            "/html/body/div[3]/div[2]/div[2]/div[1]/div[2]/div[2]/div/div/div[1]/input[1]"
        )
        password_input.clear()
        password_input.send_keys("")
        print('password_input inserted')

        time.sleep(5)

        log_in_button = browser.find_element_by_xpath(
            "/html/body/div[3]/div[2]/div[2]/div[1]/div[2]/div[3]/div/button"
        )
        log_in_button.click()
        print('log_in_button clicked')

        time.sleep(25)

        advanced_button = browser.find_element_by_xpath(
            '//*[@id="advanced"]'
        )
        advanced_button.click()
        print('advanced_button clicked')

        time.sleep(10)

        sms_button = browser.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[1]/div[1]/div[2]/div/ul/li[4]'
        )
        sms_button.click()
        print('sms_button clicked')

        time.sleep(10)

        inbox_button = browser.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[1]/div[1]/div[2]/div/ul/li[4]/ul/li[1]'
        )
        inbox_button.click()
        print('inbox_button clicked')

        time.sleep(10)

        refresh_button = browser.find_element_by_xpath(
            '/html/body/div[1]/div[4]/div[2]/div[1]/div[2]/form/div[1]/div/div[1]/label'
        )
        refresh_button.click()
        print('refresh_button clicked')

        time.sleep(10)

    # ok
    def test_recuperer_adresse_ip_v4_sans_headless(self):
        print("test_recuperer_adresse_ip_v4_sans_headless")

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
        print('page opened')

        time.sleep(15)

        password_input = browser.find_element_by_xpath(
            "/html/body/div[3]/div[2]/div[2]/div[1]/div[2]/div[2]/div/div/div[1]/input[1]"
        )
        password_input.clear()
        password_input.send_keys("")

        time.sleep(5)

        log_in_button = browser.find_element_by_xpath(
            "/html/body/div[3]/div[2]/div[2]/div[1]/div[2]/div[3]/div/button"
        )
        log_in_button.click()
        print('log_in_button clicked')

        time.sleep(20)

        ip_address_text = browser.find_element_by_xpath(
            "/html/body/div[1]/div[4]/div[2]/div[1]/div[2]/div/div/form/div[10]/input"
        ).text
        print('ip_address_text : ' + str(ip_address_text))

        time.sleep(10)

        log_out_button = browser.find_element_by_xpath(
            "/html/body/div[1]/div[1]/div/div[3]/a[2]"
        )
        log_out_button.click()
        print('log_out_button clicked')

        time.sleep(15)
        
        yes_out_button = browser.find_element_by_xpath(
            "/html/body/div[7]/div/div[4]/div/div[2]/div/div[2]/button"
        )
        yes_out_button.click()
        print('yes_out_button clicked')

        time.sleep(15)

        browser.close()
        print('browser closed')

        time.sleep(10)

    # ok
    def test_recuperer_messages_recus_sans_headless(self):
        print("test_recuperer_messages_recus_sans_headless")

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
        print('page opened')

        time.sleep(15)

        password_input = browser.find_element_by_xpath(
            "/html/body/div[3]/div[2]/div[2]/div[1]/div[2]/div[2]/div/div/div[1]/input[1]"
        )
        password_input.clear()
        password_input.send_keys("")

        time.sleep(5)

        log_in_button = browser.find_element_by_xpath(
            "/html/body/div[3]/div[2]/div[2]/div[1]/div[2]/div[3]/div/button"
        )
        log_in_button.click()
        print('log_in_button clicked')

        time.sleep(20)

        advanced_button = browser.find_element_by_xpath(
            '//*[@id="advanced"]'
        )
        advanced_button.click()

        time.sleep(5)

        sms_button = browser.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[1]/div[1]/div[2]/div/ul/li[4]'
        )
        sms_button.click()

        time.sleep(5)

        inbox_button = browser.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[1]/div[1]/div[2]/div/ul/li[4]/ul/li[1]'
        )
        inbox_button.click()

        time.sleep(5)

        for i in range(2):
            sms_received_button = browser.find_element_by_xpath(
                '/html/body/div[1]/div[4]/div[2]/div[1]/div[2]/form/table/tbody/tr[1]/td[2]'
            )
            sms_received_button.click()

            time.sleep(5)

            received_date = browser.find_element_by_xpath(
                '//*[@id="recvTime"]'
            ).text.replace(' ', '').replace('-', '').replace(':', '')
            browser.save_screenshot('A:\\2_Personnel\\2_Non_Recurrentes\\13_Operateurs_Telephoniques\\1_Free'
                                    '\\1_0769855065_0769038124_07\Messages_Recus\\' + received_date + ".png")

            time.sleep(5)

            back_button = browser.find_element_by_xpath(
                '//*[@id="back"]'
            )
            back_button.click()

            time.sleep(5)
            
            delete_sms_button = browser.find_element_by_xpath(
                '//*[@id="del_0"]'
            )
            delete_sms_button.click()

            time.sleep(5)

            yes_button = browser.find_element_by_xpath(
                '/html/body/div[7]/div/div[4]/div/div[2]/div/div[2]/button'
            )
            yes_button.click()

            time.sleep(15)

        """
        log_out_button = browser.find_element_by_xpath(
            "/html/body/div[1]/div[1]/div/div[3]/a[2]"
        )
        log_out_button.click()
        print('log_out_button clicked')

        time.sleep(15)

        yes_out_button = browser.find_element_by_xpath(
            "/html/body/div[7]/div/div[4]/div/div[2]/div/div[2]/button"
        )
        yes_out_button.click()
        print('yes_out_button clicked')

        time.sleep(15)

        browser.close()
        print('browser closed')

        time.sleep(10)
        """

    # ok
    def test_recuperer_messages_envoyes_sans_headless(self):
        print("test_recuperer_messages_envoyes_sans_headless")

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
        print('page opened')

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
        print('log_in_button clicked')

        time.sleep(20)

        advanced_button = browser.find_element_by_xpath(
            '//*[@id="advanced"]'
        )
        advanced_button.click()

        time.sleep(10)

        sms_button = browser.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[1]/div[1]/div[2]/div/ul/li[4]'
        )
        sms_button.click()

        time.sleep(10)

        sent_button = browser.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[1]/div[1]/div[2]/div/ul/li[4]/ul/li[3]'
        )
        sent_button.click()

        time.sleep(10)

        for i in range(1):
            sms_sent_button = browser.find_element_by_xpath(
                '/html/body/div[1]/div[4]/div[2]/div[1]/div[2]/form/table/tbody/tr[1]/td[5]/span[1]'
            )
            sms_sent_button.click()

            time.sleep(10)

            sent_date = browser.find_element_by_xpath(
                '//*[@id="recvTime"]'
            ).text.replace(' ', '').replace('-', '').replace(':', '')
            browser.save_screenshot('A:\\2_Personnel\\2_Non_Recurrentes\\13_Operateurs_Telephoniques\\1_Free'
                                    '\\1_0769855065_0769038124_07\\Messages_Envoyes\\' + sent_date + ".png")

            time.sleep(10)

            back_button = browser.find_element_by_xpath(
                '//*[@id="back"]'
            )
            back_button.click()

            time.sleep(10)

            delete_sms_button = browser.find_element_by_xpath(
                '//*[@id="del_0"]'
            )
            delete_sms_button.click()

            time.sleep(10)

            yes_button = browser.find_element_by_xpath(
                '/html/body/div[7]/div/div[4]/div/div[2]/div/div[2]/button'
            )
            yes_button.click()

            time.sleep(15)

            print('message ok : ' + str(i))

        log_out_button = browser.find_element_by_xpath(
            "/html/body/div[1]/div[1]/div/div[3]/a[2]"
        )
        log_out_button.click()
        print('log_out_button clicked')

        time.sleep(15)

        yes_out_button = browser.find_element_by_xpath(
            "/html/body/div[7]/div/div[4]/div/div[2]/div/div[2]/button"
        )
        yes_out_button.click()
        print('yes_out_button clicked')

        time.sleep(15)

        browser.close()
        print('browser closed')

        time.sleep(10)

    # ok
    def test_envoyer_un_sms_pour_rencontre_amoureuse(self):
        print("test_envoyer_un_sms_pour_rencontre_amoureuse")

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
        print('page opened')

        time.sleep(15)

        password_input = browser.find_element_by_xpath(
            "/html/body/div[3]/div[2]/div[2]/div[1]/div[2]/div[2]/div/div/div[1]/input[1]"
        )
        password_input.clear()
        password_input.send_keys("")
        print('password_input send_keys')

        time.sleep(10)

        log_in_button = browser.find_element_by_xpath(
            "/html/body/div[3]/div[2]/div[2]/div[1]/div[2]/div[3]/div/button"
        )
        log_in_button.click()
        print('log_in_button clicked')

        time.sleep(20)

        advanced_button = browser.find_element_by_xpath(
            '//*[@id="advanced"]'
        )
        advanced_button.click()
        print("advanced_button.click()")

        time.sleep(10)

        sms_button = browser.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[1]/div[1]/div[2]/div/ul/li[4]'
        )
        sms_button.click()
        print("sms_button.click()")

        time.sleep(10)

        new_message_button = browser.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[1]/div[1]/div[2]/div/ul/li[4]/ul/li[2]/a/span'
        )
        new_message_button.click()
        print("new_message_button.click()")

        time.sleep(10)

        phone_number_input = browser.find_element_by_xpath(
            '//*[@id="toNumber"]'
        )
        phone_number_input.clear()
        phone_number_input.send_keys("0749163329")
        print("phone_number_input inserted")

        time.sleep(10)

        text_input = browser.find_element_by_xpath(
            '//*[@id="inputContent"]'
        )
        text_input.clear()
        text_input.send_keys("""Hello, vu ton profil sur www.website.com, je suis un homme agé de 28 ans et 
je voudrai avancer avec une femme honnête, intelligente, scientifique. Je cherche à ce qu'on puisse 
s'adapter mutuellement pour plus de liberté, de bonheur et d'amour. Mon profil : www.github.com/Jay4C, 
très bonne journée à toi, Jason""")
        print("text_input inserted")

        time.sleep(10)

        send_button = browser.find_element_by_xpath(
            '//*[@id="send"]'
        )
        send_button.click()
        print("send_button.click()")

        time.sleep(10)

        log_out_button = browser.find_element_by_xpath(
            '//*[@id="topLogout"]'
        )
        log_out_button.click()
        print("log_out_button.click()")

        time.sleep(10)

        yes_button = browser.find_element_by_xpath(
            '/html/body/div[7]/div/div[4]/div/div[2]/div/div[2]/button'
        )
        yes_button.click()
        print("yes_button.click()")

        time.sleep(10)

        browser.close()
        print("browser closed")

    # ok
    def test_envoyer_un_sms(self):
        print("test_envoyer_un_sms")

        numero_de_telephone = "0033693047277"

        message = """Bjr Tracy, c'est Jason le garçon de tatie nini, çà va ? Je cherche une femme pour représenter mon 
        futur association caritative afin de renforcer les infrastructures publiques des communes de la Réunion avec 
        des briques de terre. Est-ce que tu serais enthousiaste de représenter une association stp ?"""

        if len(message) < 335:
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
            print('page opened')

            time.sleep(15)

            password_input = browser.find_element_by_xpath(
                "/html/body/div[3]/div[2]/div[2]/div[1]/div[2]/div[2]/div/div/div[1]/input[1]"
            )
            password_input.clear()
            password_input.send_keys("")
            print('password_input send_keys')

            time.sleep(10)

            log_in_button = browser.find_element_by_xpath(
                "/html/body/div[3]/div[2]/div[2]/div[1]/div[2]/div[3]/div/button"
            )
            log_in_button.click()
            print('log_in_button clicked')

            time.sleep(20)

            advanced_button = browser.find_element_by_xpath(
                '//*[@id="advanced"]'
            )
            advanced_button.click()
            print("advanced_button.click()")

            time.sleep(10)

            sms_button = browser.find_element_by_xpath(
                '/html/body/div[1]/div[2]/div[1]/div[1]/div[2]/div/ul/li[4]'
            )
            sms_button.click()
            print("sms_button.click()")

            time.sleep(10)

            new_message_button = browser.find_element_by_xpath(
                '/html/body/div[1]/div[2]/div[1]/div[1]/div[2]/div/ul/li[4]/ul/li[2]/a/span'
            )
            new_message_button.click()
            print("new_message_button.click()")

            time.sleep(10)

            phone_number_input = browser.find_element_by_xpath(
                '//*[@id="toNumber"]'
            )
            phone_number_input.clear()
            phone_number_input.send_keys(numero_de_telephone)
            print("phone_number_input inserted")

            time.sleep(10)

            text_input = browser.find_element_by_xpath(
                '//*[@id="inputContent"]'
            )
            text_input.clear()
            text_input.send_keys(message)
            print("text_input inserted")

            time.sleep(10)

            send_button = browser.find_element_by_xpath(
                '//*[@id="send"]'
            )
            send_button.click()
            print("send_button.click()")

            time.sleep(10)

            log_out_button = browser.find_element_by_xpath(
                '//*[@id="topLogout"]'
            )
            log_out_button.click()
            print("log_out_button.click()")

            time.sleep(10)

            yes_button = browser.find_element_by_xpath(
                '/html/body/div[7]/div/div[4]/div/div[2]/div/div[2]/button'
            )
            yes_button.click()
            print("yes_button.click()")

            time.sleep(10)

            browser.quit()
            print("browser.quit()")
        else:
            print('message trop long > 335 caracteres : ' + str(len(message)))

    # ok
    def test_activer_wifi_access_sans_headless(self):
        print("test_activer_wifi_access_sans_headless")

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
        print('page opened')

        time.sleep(15)

        password_input = browser.find_element_by_xpath(
            "/html/body/div[3]/div[2]/div[2]/div[1]/div[2]/div[2]/div/div/div[1]/input[1]"
        )
        password_input.clear()
        password_input.send_keys("")
        print("password inserted")

        time.sleep(10)

        log_in_button = browser.find_element_by_xpath(
            "/html/body/div[3]/div[2]/div[2]/div[1]/div[2]/div[3]/div/button"
        )
        log_in_button.click()
        print("log_in_button.click()")

        time.sleep(10)

        wireless_in_button = browser.find_element_by_xpath(
            "/html/body/div[1]/div[2]/div[1]/div[1]/div[2]/div/ul/li[3]/a"
        )
        wireless_in_button.click()
        print("wireless_in_button.click()")

        time.sleep(5)

        enable_checkbox = browser.find_element_by_xpath(
            "/html/body/div[1]/div[4]/div[2]/div[1]/div[2]/form/div[1]/div[1]/label[2]"
        )
        enable_checkbox.click()
        print("enable_checkbox.click()")

        time.sleep(5)

        save_button = browser.find_element_by_xpath(
            "//*[@id='save']"
        )
        save_button.click()
        print("save_button.click()")

        time.sleep(30)

        log_out_button = browser.find_element_by_xpath(
            "/html/body/div[1]/div[1]/div/div[3]/a[2]"
        )
        log_out_button.click()
        print('log_out_button clicked')

        time.sleep(10)

        yes_out_button = browser.find_element_by_xpath(
            "/html/body/div[7]/div/div[4]/div/div[2]/div/div[2]/button"
        )
        yes_out_button.click()
        print('yes_out_button clicked')

        time.sleep(10)

        browser.close()
        print('browser closed')

        time.sleep(10)

    # ok
    def test_reboot(self):
        try:
            print("test_reboot")

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
            browser.get('http://www.tplinkmodem.net')
            print("browser.get('http://www.tplinkmodem.net')")

            time.sleep(15)

            password_input = browser.find_element_by_xpath(
                "/html/body/div[3]/div[2]/div[2]/div[1]/div[2]/div[2]/div/div/div[1]/input[1]"
            )
            password_input.clear()
            password_input.send_keys("")
            print("password_input.clear()")

            time.sleep(10)

            log_in_button = browser.find_element_by_xpath(
                "/html/body/div[3]/div[2]/div[2]/div[1]/div[2]/div[3]/div/button"
            )
            log_in_button.click()
            print("log_in_button.click()")

            time.sleep(20)

            reboot_button = browser.find_element_by_xpath(
                '//*[@id="topReboot"]'
            )
            reboot_button.click()
            print("reboot_button.click()")

            time.sleep(5)

            yes_button = browser.find_element_by_xpath(
                '/html/body/div[7]/div/div[4]/div/div[2]/div/div[2]/button'
            )
            yes_button.click()
            print("yes_button.click()")

            time.sleep(120)

            browser.quit()
            print("browser.quit()")
        except Exception as e:
            print("error : " + str(e))


class UnitTestsWebAutomationTPLinkWithHeadless(unittest.TestCase):
    # ok
    def test_recuperer_adresse_ip_v4_avec_headless(self):
        print("test_recuperer_adresse_ip_v4_avec_headless")

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

        time.sleep(5)

        # open
        browser.get('http://www.tplinkmodem.net')
        print('page opened')

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
        print('log_in_button clicked')

        time.sleep(20)

        ip_address_text = browser.find_element_by_xpath(
            "/html/body/div[1]/div[4]/div[2]/div[1]/div[2]/div/div/form/div[10]/input"
        ).text
        print('ip_address_text : ' + str(ip_address_text))

        time.sleep(10)

        log_out_button = browser.find_element_by_xpath(
            "/html/body/div[1]/div[1]/div/div[3]/a[2]"
        )
        log_out_button.click()
        print('log_out_button clicked')

        time.sleep(15)

        yes_out_button = browser.find_element_by_xpath(
            "/html/body/div[7]/div/div[4]/div/div[2]/div/div[2]/button"
        )
        yes_out_button.click()
        print('yes_out_button clicked')

        time.sleep(15)

        browser.close()
        print('browser closed')

        time.sleep(10)

    # ok
    def test_recuperer_messages_recus_avec_headless(self):
        print("test_recuperer_messages_recus_avec_headless")

        nombre_de_sms = 2

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
        browser.get('http://www.tplinkmodem.net')
        print('page opened')

        time.sleep(15)

        password_input = browser.find_element_by_xpath(
            "/html/body/div[3]/div[2]/div[2]/div[1]/div[2]/div[2]/div/div/div[1]/input[1]"
        )
        password_input.clear()
        password_input.send_keys("")
        print('password_input inserted')

        time.sleep(5)

        log_in_button = browser.find_element_by_xpath(
            "/html/body/div[3]/div[2]/div[2]/div[1]/div[2]/div[3]/div/button"
        )
        log_in_button.click()
        print('log_in_button clicked')

        time.sleep(25)

        advanced_button = browser.find_element_by_xpath(
            '//*[@id="advanced"]'
        )
        advanced_button.click()
        print('advanced_button clicked')

        time.sleep(10)

        sms_button = browser.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[1]/div[1]/div[2]/div/ul/li[4]'
        )
        sms_button.click()
        print('sms_button clicked')

        time.sleep(10)

        inbox_button = browser.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[1]/div[1]/div[2]/div/ul/li[4]/ul/li[1]'
        )
        inbox_button.click()
        print('inbox_button clicked')

        time.sleep(10)

        for i in range(nombre_de_sms):
            sms_received_button = browser.find_element_by_xpath(
                '/html/body/div[1]/div[4]/div[2]/div[1]/div[2]/form/table/tbody/tr[1]/td[2]'
            )
            sms_received_button.click()

            time.sleep(10)

            received_date = browser.find_element_by_xpath(
                '//*[@id="recvTime"]'
            ).text.replace(' ', '').replace('-', '').replace(':', '')
            browser.save_screenshot('A:\\2_Personnel\\2_Non_Recurrentes\\13_Operateurs_Telephoniques\\1_Free'
                                    '\\1_0769855065_0769038124_07\Messages_Recus\\' + received_date + ".png")

            time.sleep(10)

            back_button = browser.find_element_by_xpath(
                '//*[@id="back"]'
            )
            back_button.click()

            time.sleep(10)

            delete_sms_button = browser.find_element_by_xpath(
                '//*[@id="del_0"]'
            )
            delete_sms_button.click()

            time.sleep(10)

            yes_button = browser.find_element_by_xpath(
                '/html/body/div[7]/div/div[4]/div/div[2]/div/div[2]/button'
            )
            yes_button.click()

            time.sleep(20)

            print('message ok : ' + str(i))

        log_out_button = browser.find_element_by_xpath(
            "/html/body/div[1]/div[1]/div/div[3]/a[2]"
        )
        log_out_button.click()
        print('log_out_button clicked')

        time.sleep(15)

        yes_out_button = browser.find_element_by_xpath(
            "/html/body/div[7]/div/div[4]/div/div[2]/div/div[2]/button"
        )
        yes_out_button.click()
        print('yes_out_button clicked')

        time.sleep(15)

        browser.close()
        print('browser closed')

        time.sleep(10)

    # ok
    def test_recuperer_messages_envoyes_avec_headless(self):
        print("test_recuperer_messages_envoyes_avec_headless")

        nombre_de_sms = 2

        time.sleep(5)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(5)

        # with Firefox
        options = Options()
        options.headless = True
        browser = webdriver.Firefox(executable_path='..\\..\\geckodriver.exe', options=options)

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get('http://www.tplinkmodem.net')
        print('page opened')

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
        print('log_in_button clicked')

        time.sleep(20)

        advanced_button = browser.find_element_by_xpath(
            '//*[@id="advanced"]'
        )
        advanced_button.click()

        time.sleep(10)

        sms_button = browser.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[1]/div[1]/div[2]/div/ul/li[4]'
        )
        sms_button.click()

        time.sleep(10)

        sent_button = browser.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[1]/div[1]/div[2]/div/ul/li[4]/ul/li[3]'
        )
        sent_button.click()

        time.sleep(10)

        for i in range(nombre_de_sms):
            sms_sent_button = browser.find_element_by_xpath(
                '/html/body/div[1]/div[4]/div[2]/div[1]/div[2]/form/table/tbody/tr[1]/td[5]/span[1]'
            )
            sms_sent_button.click()

            time.sleep(10)

            sent_date = browser.find_element_by_xpath(
                '//*[@id="recvTime"]'
            ).text.replace(' ', '').replace('-', '').replace(':', '')
            browser.save_screenshot('A:\\2_Personnel\\2_Non_Recurrentes\\13_Operateurs_Telephoniques\\1_Free'
                                    '\\1_0769855065_0769038124_07\\Messages_Envoyes\\' + sent_date + ".png")

            time.sleep(10)

            back_button = browser.find_element_by_xpath(
                '//*[@id="back"]'
            )
            back_button.click()

            time.sleep(10)

            delete_sms_button = browser.find_element_by_xpath(
                '//*[@id="del_0"]'
            )
            delete_sms_button.click()

            time.sleep(10)

            yes_button = browser.find_element_by_xpath(
                '/html/body/div[7]/div/div[4]/div/div[2]/div/div[2]/button'
            )
            yes_button.click()

            time.sleep(15)

            print('message ok : ' + str(i))

        log_out_button = browser.find_element_by_xpath(
            "/html/body/div[1]/div[1]/div/div[3]/a[2]"
        )
        log_out_button.click()
        print('log_out_button clicked')

        time.sleep(15)

        yes_out_button = browser.find_element_by_xpath(
            "/html/body/div[7]/div/div[4]/div/div[2]/div/div[2]/button"
        )
        yes_out_button.click()
        print('yes_out_button clicked')

        time.sleep(15)

        browser.close()
        print('browser closed')

        time.sleep(10)

    # ok
    def test_envoyer_un_sms_avec_headless(self):
        print("test_envoyer_un_sms_avec_headless")

        numero_de_telephone = ""

        message = """"""

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
        browser.get('http://www.tplinkmodem.net')
        print('page opened')

        time.sleep(15)

        password_input = browser.find_element_by_xpath(
            "/html/body/div[3]/div[2]/div[2]/div[1]/div[2]/div[2]/div/div/div[1]/input[1]"
        )
        password_input.clear()
        password_input.send_keys("")
        print('password_input send_keys')

        time.sleep(10)

        log_in_button = browser.find_element_by_xpath(
            "/html/body/div[3]/div[2]/div[2]/div[1]/div[2]/div[3]/div/button"
        )
        log_in_button.click()
        print('log_in_button clicked')

        time.sleep(20)

        advanced_button = browser.find_element_by_xpath(
            '//*[@id="advanced"]'
        )
        advanced_button.click()
        print("advanced_button.click()")

        time.sleep(10)

        sms_button = browser.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[1]/div[1]/div[2]/div/ul/li[4]'
        )
        sms_button.click()
        print("sms_button.click()")

        time.sleep(10)

        new_message_button = browser.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[1]/div[1]/div[2]/div/ul/li[4]/ul/li[2]/a/span'
        )
        new_message_button.click()
        print("new_message_button.click()")

        time.sleep(10)

        phone_number_input = browser.find_element_by_xpath(
            '//*[@id="toNumber"]'
        )
        phone_number_input.clear()
        phone_number_input.send_keys(numero_de_telephone)
        print("phone_number_input inserted")

        time.sleep(10)

        text_input = browser.find_element_by_xpath(
            '//*[@id="inputContent"]'
        )
        text_input.clear()
        text_input.send_keys(message)
        print("text_input inserted")

        time.sleep(10)

        send_button = browser.find_element_by_xpath(
            '//*[@id="send"]'
        )
        send_button.click()
        print("send_button.click()")

        time.sleep(10)

        log_out_button = browser.find_element_by_xpath(
            '//*[@id="topLogout"]'
        )
        log_out_button.click()
        print("log_out_button.click()")

        time.sleep(10)

        yes_button = browser.find_element_by_xpath(
            '/html/body/div[7]/div/div[4]/div/div[2]/div/div[2]/button'
        )
        yes_button.click()
        print("yes_button.click()")

        time.sleep(10)

        browser.close()
        print("browser closed")

    # ok
    def test_envoyer_des_sms_avec_headless(self):
        print("test_envoyer_des_sms_avec_headless")

        numeros_de_telephone = [

        ]

        message = """Slt çà va ? Il faut tjrs me téléphoner sur mon nouveau numéro de téléphone : 0745752700 pour que je sois rapide à répondre. """

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
        browser.get('http://www.tplinkmodem.net')
        print('page opened')

        time.sleep(15)

        password_input = browser.find_element_by_xpath(
            "/html/body/div[3]/div[2]/div[2]/div[1]/div[2]/div[2]/div/div/div[1]/input[1]"
        )
        password_input.clear()
        password_input.send_keys("")
        print('password_input send_keys')

        time.sleep(10)

        log_in_button = browser.find_element_by_xpath(
            "/html/body/div[3]/div[2]/div[2]/div[1]/div[2]/div[3]/div/button"
        )
        log_in_button.click()
        print('log_in_button clicked')

        time.sleep(20)

        advanced_button = browser.find_element_by_xpath(
            '//*[@id="advanced"]'
        )
        advanced_button.click()
        print("advanced_button.click()")

        time.sleep(10)

        sms_button = browser.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[1]/div[1]/div[2]/div/ul/li[4]'
        )
        sms_button.click()
        print("sms_button.click()")

        time.sleep(10)

        new_message_button = browser.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[1]/div[1]/div[2]/div/ul/li[4]/ul/li[2]/a/span'
        )
        new_message_button.click()
        print("new_message_button.click()")

        time.sleep(10)

        for telephone in numeros_de_telephone:
            numero_de_telephone = telephone

            phone_number_input = browser.find_element_by_xpath(
                '//*[@id="toNumber"]'
            )
            phone_number_input.clear()
            phone_number_input.send_keys(numero_de_telephone)
            print("phone_number_input inserted")

            time.sleep(10)

            text_input = browser.find_element_by_xpath(
                '//*[@id="inputContent"]'
            )
            text_input.clear()
            text_input.send_keys(message)
            print("text_input inserted")

            time.sleep(10)

            send_button = browser.find_element_by_xpath(
                '//*[@id="send"]'
            )
            send_button.click()
            print("send_button.click()")

            time.sleep(10)

        log_out_button = browser.find_element_by_xpath(
            '//*[@id="topLogout"]'
        )
        log_out_button.click()
        print("log_out_button.click()")

        time.sleep(10)

        yes_button = browser.find_element_by_xpath(
            '/html/body/div[7]/div/div[4]/div/div[2]/div/div[2]/button'
        )
        yes_button.click()
        print("yes_button.click()")

        time.sleep(10)

        browser.close()
        print("browser closed")

    # ok
    def test_activer_wifi_access_avec_headless(self):
        print("test_activer_wifi_access_avec_headless")

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

        time.sleep(5)

        # open
        browser.get('http://www.tplinkmodem.net')
        print('page opened')

        time.sleep(15)

        password_input = browser.find_element_by_xpath(
            "/html/body/div[3]/div[2]/div[2]/div[1]/div[2]/div[2]/div/div/div[1]/input[1]"
        )
        password_input.clear()
        password_input.send_keys("")
        print("password inserted")

        time.sleep(10)

        log_in_button = browser.find_element_by_xpath(
            "/html/body/div[3]/div[2]/div[2]/div[1]/div[2]/div[3]/div/button"
        )
        log_in_button.click()
        print("log_in_button.click()")

        time.sleep(10)

        wireless_in_button = browser.find_element_by_xpath(
            "/html/body/div[1]/div[2]/div[1]/div[1]/div[2]/div/ul/li[3]/a"
        )
        wireless_in_button.click()
        print("wireless_in_button.click()")

        time.sleep(5)

        enable_checkbox = browser.find_element_by_xpath(
            "/html/body/div[1]/div[4]/div[2]/div[1]/div[2]/form/div[1]/div[1]/label[2]"
        )
        enable_checkbox.click()
        print("enable_checkbox.click()")

        time.sleep(5)

        save_button = browser.find_element_by_xpath(
            "//*[@id='save']"
        )
        save_button.click()
        print("save_button.click()")

        time.sleep(30)

        log_out_button = browser.find_element_by_xpath(
            "/html/body/div[1]/div[1]/div/div[3]/a[2]"
        )
        log_out_button.click()
        print('log_out_button clicked')

        time.sleep(10)

        yes_out_button = browser.find_element_by_xpath(
            "/html/body/div[7]/div/div[4]/div/div[2]/div/div[2]/button"
        )
        yes_out_button.click()
        print('yes_out_button clicked')

        time.sleep(10)

        browser.close()
        print('browser closed')

        time.sleep(10)

    # ok
    def test_reboot_avec_headless(self):
        try:
            print("test_reboot_avec_headless")

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
            browser.get('http://www.tplinkmodem.net')
            print("browser.get('http://www.tplinkmodem.net')")

            time.sleep(15)

            password_input = browser.find_element_by_xpath(
                "/html/body/div[3]/div[2]/div[2]/div[1]/div[2]/div[2]/div/div/div[1]/input[1]"
            )
            password_input.clear()
            password_input.send_keys("")
            print("password_input.clear()")

            time.sleep(10)

            log_in_button = browser.find_element_by_xpath(
                "/html/body/div[3]/div[2]/div[2]/div[1]/div[2]/div[3]/div/button"
            )
            log_in_button.click()
            print("log_in_button.click()")

            time.sleep(20)

            reboot_button = browser.find_element_by_xpath(
                '//*[@id="topReboot"]'
            )
            reboot_button.click()
            print("reboot_button.click()")

            time.sleep(5)

            yes_button = browser.find_element_by_xpath(
                '/html/body/div[7]/div/div[4]/div/div[2]/div/div[2]/button'
            )
            yes_button.click()
            print("yes_button.click()")

            time.sleep(120)

            browser.quit()
            print("browser.quit()")
        except Exception as e:
            print("error reboot : " + str(e))

    # ok
    def test_kill_some_processes(self):
        print("test_kill_some_processes")

        subprocess.call("taskkill /F /IM geckodriver.exe")
        subprocess.call("taskkill /F /IM firefox.exe")


if __name__ == '__main__':
    unittest.main()
