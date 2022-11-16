import unittest
import time
import warnings
from selenium import webdriver


class UnitTestsWebAutomationSkrillWithoutHeadless(unittest.TestCase):
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
        browser.get('https://www.skrill.com/fr/')

        time.sleep(15)

    #
    def test_se_connecter(self):
        print("test_se_connecter")

        username_skrill = ""

        password_skrill = ""

        password_tp_link =''

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
        browser.get('https://www.skrill.com/fr/')

        time.sleep(10)

        # click on the button "Autoriser les cookies"
        autoriser_les_cookies_button = browser.find_element_by_xpath(
            '//*[@id="onetrust-accept-btn-handler"]'
        )
        autoriser_les_cookies_button.click()
        print("autoriser_les_cookies_button.click()")

        time.sleep(5)

        # click on the button "Connexion"
        connexion_button = browser.find_element_by_xpath(
            '//*[@id="login"]'
        )
        connexion_button.click()
        print("connexion_button.click()")

        time.sleep(15)

        email_input = browser.find_element_by_xpath(
            '//*[@id="user_authentication_email"]'
        )
        email_input.clear()
        email_input.send_keys(username_skrill)
        print("email_input inserted")

        time.sleep(5)

        mot_de_passe_input = browser.find_element_by_xpath(
            '//*[@id="user_authentication_password"]'
        )
        mot_de_passe_input.clear()
        mot_de_passe_input.send_keys(password_skrill)
        print("mot_de_passe_input inserted")

        time.sleep(5)

        # click on the button "Se connecter"
        se_connecter_button = browser.find_element_by_xpath(
            '/html/body/kl-root/kl-theme/ng-component/kl-login-main-layout/div/div[2]/main/ng-component/form/kl-login'
            '/article/form/kl-button/button'
        )
        se_connecter_button.click()
        print("se_connecter_button.click()")

        time.sleep(10)

        # click on the button "Envoyer un code par sms"
        envoyer_un_code_par_sms = browser.find_element_by_xpath(
            '/html/body/kl-root/kl-theme/ng-component/kl-login-main-layout/div/div[2]/main'
            '/lib-select-challenge-wrapper/lib-select-challenge/div/ps-card/ps-radio-group/ps-radio-button[1]'
            '/label/div[1]/div[1]'
        )
        envoyer_un_code_par_sms.click()
        print("envoyer_un_code_par_sms.click()")

        time.sleep(5)

        # click on the button "Suivant"
        suivant_button = browser.find_element_by_xpath(
            '/html/body/kl-root/kl-theme/ng-component/kl-login-main-layout/div/div[2]/main'
            '/lib-select-challenge-wrapper/lib-select-challenge/div/ps-card/div/button[1]'
        )
        suivant_button.click()
        print("suivant_button.click()")

        time.sleep(10)

        # Open a new window
        browser.execute_script("window.open('');")

        time.sleep(5)

        # Switch to the new window
        browser.switch_to.window(browser.window_handles[1])

        time.sleep(5)

        # open
        browser.get('http://www.tplinkmodem.net')

        time.sleep(10)

        password_input = browser.find_element_by_xpath(
            "/html/body/div[3]/div[2]/div[2]/div[1]/div[2]/div[2]/div/div/div[1]/input[1]"
        )
        password_input.clear()
        password_input.send_keys(password_tp_link)
        print('password_input inserted')

        time.sleep(5)

        log_in_button = browser.find_element_by_xpath(
            "/html/body/div[3]/div[2]/div[2]/div[1]/div[2]/div[3]/div/button"
        )
        log_in_button.click()
        print('log_in_button clicked')

        time.sleep(15)

        advanced_button = browser.find_element_by_xpath(
            '//*[@id="advanced"]'
        )
        advanced_button.click()
        print('advanced_button clicked')

        time.sleep(5)

        sms_button = browser.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[1]/div[1]/div[2]/div/ul/li[4]'
        )
        sms_button.click()
        print('sms_button clicked')

        time.sleep(5)

        inbox_button = browser.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[1]/div[1]/div[2]/div/ul/li[4]/ul/li[1]'
        )
        inbox_button.click()
        print('inbox_button clicked')

        time.sleep(5)

        sms_received_button = browser.find_element_by_xpath(
            '//*[@id="msg_0"]'
        )
        sms_received_button.click()
        print('sms_received_button.click()')

        time.sleep(10)

        # Retrieve the code
        code = browser.find_element_by_xpath(
            '//*[@id="msgContent"]'
        ).text.replace("Votre code d'authentification Skrill est ", '')
        print('code : ' + str(code))

        time.sleep(5)

        # Switch to the last window
        browser.switch_to.window(browser.window_handles[0])

        time.sleep(5)

        code_input_1 = browser.find_element_by_xpath(
            '//*[@id="ps-input-2"]'
        )
        code_input_1.clear()
        code_input_1.send_keys(str(code[0]))
        print("code_input_1 inserted")

        time.sleep(5)

        code_input_2 = browser.find_element_by_xpath(
            '//*[@id="ps-input-3"]'
        )
        code_input_2.clear()
        code_input_2.send_keys(str(code[1]))
        print("code_input_2 inserted")

        time.sleep(5)

        code_input_3 = browser.find_element_by_xpath(
            '//*[@id="ps-input-4"]'
        )
        code_input_3.clear()
        code_input_3.send_keys(str(code[2]))
        print("code_input_3 inserted")

        time.sleep(5)

        code_input_4 = browser.find_element_by_xpath(
            '//*[@id="ps-input-5"]'
        )
        code_input_4.clear()
        code_input_4.send_keys(str(code[3]))
        print("code_input_4 inserted")

        time.sleep(5)

        code_input_5 = browser.find_element_by_xpath(
            '//*[@id="ps-input-6"]'
        )
        code_input_5.clear()
        code_input_5.send_keys(str(code[4]))
        print("code_input_5 inserted")

        time.sleep(5)

        code_input_6 = browser.find_element_by_xpath(
            '//*[@id="ps-input-7"]'
        )
        code_input_6.clear()
        code_input_6.send_keys(str(code[5]))
        print("code_input_6 inserted")

        time.sleep(5)

        connectez_vous_button = browser.find_element_by_xpath(
            '/html/body/kl-root/kl-theme/ng-component/kl-login-main-layout/div/div[2]/main/lib-challenge-sms/div'
            '/ps-card/div/lib-verify-sms/div/form/div[2]/button[1]'
        )
        connectez_vous_button.click()
        print('connectez_vous_button.click()')

        time.sleep(10)

        # Switch to the new window
        browser.switch_to.window(browser.window_handles[1])

        time.sleep(5)

        inbox_button = browser.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[1]/div[1]/div[2]/div/ul/li[4]/ul/li[1]'
        )
        inbox_button.click()
        print('inbox_button clicked')

        time.sleep(5)


if __name__ == '__main__':
    unittest.main()
