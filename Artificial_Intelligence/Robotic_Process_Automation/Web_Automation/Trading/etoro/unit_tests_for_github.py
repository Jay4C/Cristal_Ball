import time
import warnings
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.options import Options


class UnitTestsRPATradingEtoro(unittest.TestCase):
    # ok
    def test_login(self):
        print('test_login')

        my_email = ''
        my_password = ''

        url = "https://www.etoro.com/login"

        time.sleep(7)

        warnings.filterwarnings(
            action="ignore",
            message="unclosed",
            category=ResourceWarning
        )

        time.sleep(7)

        # With Firefox
        options = Options()
        options.headless = False
        browser = webdriver.Firefox(
            executable_path='M:\\1_Personnel\\1_Recurrentes\\3_Outils_Numeriques\\GitHub_Jay4C\\Cristal_Ball'
                            '\\geckodriver.exe',
            options=options
        )

        time.sleep(7)

        # maximize window
        browser.maximize_window()

        time.sleep(7)

        # open
        browser.get(url)

        time.sleep(7)

        # Insert my email
        email_input = browser.find_element(
            by=By.XPATH,
            value='/html/body/ui-layout/div/et-layout-login/div/ng-view/et-login/et-login-sts/div/div/div/form/div[1]/input'
        )
        email_input.clear()
        email_input.send_keys(
            my_email
        )
        print("email inserted")

        time.sleep(7)

        # Insert my password
        password_input = browser.find_element(
            by=By.XPATH,
            value='/html/body/ui-layout/div/et-layout-login/div/ng-view/et-login/et-login-sts/div/div/div/form/div[2]/input'
        )
        password_input.clear()
        password_input.send_keys(
            my_password
        )
        print("password inserted")

        time.sleep(7)

        # Click on the '' button
        sign_in_button = browser.find_element(
            by=By.XPATH,
            value='/html/body/ui-layout/div/et-layout-login/div/ng-view/et-login/et-login-sts/div/div/div/form/button'
        )
        sign_in_button.click()
        print('sign_in_button.click() clicked')

        time.sleep(7)

    # ok
    def test_switch_to_virtual_account(self):
        print('test_switch_to_virtual_account')

        my_email = ''
        my_password = ''

        url = "https://www.etoro.com/login"

        time.sleep(7)

        warnings.filterwarnings(
            action="ignore",
            message="unclosed",
            category=ResourceWarning
        )

        time.sleep(7)

        # With Firefox
        options = Options()
        options.headless = False
        browser = webdriver.Firefox(
            executable_path='M:\\1_Personnel\\1_Recurrentes\\3_Outils_Numeriques\\GitHub_Jay4C\\Cristal_Ball'
                            '\\geckodriver.exe',
            options=options
        )

        time.sleep(7)

        # maximize window
        browser.maximize_window()

        time.sleep(7)

        # open
        browser.get(url)

        time.sleep(7)

        # Insert my email
        email_input = browser.find_element(
            by=By.XPATH,
            value='/html/body/ui-layout/div/et-layout-login/div/ng-view/et-login/et-login-sts/div/div/div/form/div[1]/input'
        )
        email_input.clear()
        email_input.send_keys(
            my_email
        )
        print("email inserted")

        time.sleep(7)

        # Insert my password
        password_input = browser.find_element(
            by=By.XPATH,
            value='/html/body/ui-layout/div/et-layout-login/div/ng-view/et-login/et-login-sts/div/div/div/form/div[2]/input'
        )
        password_input.clear()
        password_input.send_keys(
            my_password
        )
        print("password inserted")

        time.sleep(7)

        # Click on the 'Sign in' button
        sign_in_button = browser.find_element(
            by=By.XPATH,
            value='/html/body/ui-layout/div/et-layout-login/div/ng-view/et-login/et-login-sts/div/div/div/form/button'
        )
        sign_in_button.click()
        print('sign_in_button.click() clicked')

        time.sleep(10)

        # Click on the 'Switch to virtual' button
        switch_to_virtual_button = browser.find_element(
            by=By.XPATH,
            value='/html/body/ui-layout/div/et-layout-main/div/div[2]/div[1]/et-layout-sidenav/aside/div[3]/div[2]/a'
        )
        switch_to_virtual_button.click()
        print('switch_to_virtual_button.click() clicked')

        time.sleep(7)

        # Click on the 'Switch to virtual portfolio' button
        switch_to_virtual_portfolio_button = browser.find_element(
            by=By.XPATH,
            value='/html/body/div[9]/div[2]/div/et-dialog-container/et-portfolio-toggle-account/div/div[3]/a'
        )
        switch_to_virtual_portfolio_button.click()
        print('switch_to_virtual_portfolio_button.click() clicked')

        time.sleep(7)

    # ok
    def test_place_one_trade_for_eurusd_from_virtual_portfolio(self):
        print('test_place_one_trade_for_eurusd_from_virtual_portfolio')

        my_email = ''
        my_password = ''

        url = "https://www.etoro.com/login"

        market = 'https://www.etoro.com/markets/eurusd'

        position = 'sell'

        amount = '1000'

        time.sleep(7)

        warnings.filterwarnings(
            action="ignore",
            message="unclosed",
            category=ResourceWarning
        )

        time.sleep(7)

        # With Firefox
        options = Options()
        options.headless = False
        browser = webdriver.Firefox(
            executable_path='M:\\1_Personnel\\1_Recurrentes\\3_Outils_Numeriques\\GitHub_Jay4C\\Cristal_Ball'
                            '\\geckodriver.exe',
            options=options
        )

        time.sleep(7)

        # maximize window
        browser.maximize_window()

        time.sleep(7)

        # open
        browser.get(url)

        time.sleep(7)

        # Insert my email
        email_input = browser.find_element(
            by=By.XPATH,
            value='/html/body/ui-layout/div/et-layout-login/div/ng-view/et-login/et-login-sts/div/div/div/form/div[1]/input'
        )
        email_input.clear()
        email_input.send_keys(
            my_email
        )
        print("email inserted")

        time.sleep(7)

        # Insert my password
        password_input = browser.find_element(
            by=By.XPATH,
            value='/html/body/ui-layout/div/et-layout-login/div/ng-view/et-login/et-login-sts/div/div/div/form/div[2]/input'
        )
        password_input.clear()
        password_input.send_keys(
            my_password
        )
        print("password inserted")

        time.sleep(7)

        # Click on the 'Sign in' button
        sign_in_button = browser.find_element(
            by=By.XPATH,
            value='/html/body/ui-layout/div/et-layout-login/div/ng-view/et-login/et-login-sts/div/div/div/form/button'
        )
        sign_in_button.click()
        print('sign_in_button.click() clicked')

        time.sleep(15)

        # Click on the 'Switch to virtual' button
        switch_to_virtual_button = browser.find_element(
            by=By.XPATH,
            value='/html/body/ui-layout/div/et-layout-main/div/div[2]/div[1]/et-layout-sidenav/aside/div[3]/div[2]/a'
        )
        switch_to_virtual_button.click()
        print('switch_to_virtual_button.click() clicked')

        time.sleep(7)

        # Click on the 'Switch to virtual portfolio' button
        try:
            switch_to_virtual_portfolio_button = browser.find_element(
                by=By.XPATH,
                value='/html/body/div[9]/div[2]/div/et-dialog-container/et-portfolio-toggle-account/div/div[3]/a'
            )
            switch_to_virtual_portfolio_button.click()
            print('switch_to_virtual_portfolio_button.click() clicked')
        except Exception as e:
            print('error switch_to_virtual_portfolio_button for div 9 : ' + str(e))

            switch_to_virtual_portfolio_button = browser.find_element(
                by=By.XPATH,
                value='/html/body/div[10]/div[2]/div/et-dialog-container/et-portfolio-toggle-account/div/div[3]/a'
            )
            switch_to_virtual_portfolio_button.click()
            print('switch_to_virtual_portfolio_button.click() clicked')

        time.sleep(7)

        # open the market eurusd
        browser.get(market)

        time.sleep(10)

        # Click on the 'Trade' button
        trade_button = browser.find_element(
            by=By.XPATH,
            value='/html/body/ui-layout/div/et-layout-main/div/div[2]/div[2]/div[3]/div/ng-view/et-market/div/div/et-market-header/div/div[2]/trade-button/div'
        )
        trade_button.click()
        print('trade_button.click() clicked')

        time.sleep(7)

        # Insert the amount
        amount_input = browser.find_element(
            by=By.XPATH,
            value='//input[@data-etoro-automation-id="input"]'
        )
        amount_input.send_keys(
            '1'
        )

        time.sleep(2)

        actions_amount = ActionChains(browser)
        actions_amount.send_keys(Keys.BACKSPACE * 20)
        actions_amount.perform()

        time.sleep(2)

        amount_input.send_keys(
            amount
        )
        print("amount_input inserted")

        time.sleep(7)

        # Click on the 'Sell or buy' button
        position_button = browser.find_element(
            by=By.XPATH,
            value='//button[@data-etoro-automation-id="execution-' + str(position) + '-button"]',
        )
        position_button.click()
        print('position_button.click() clicked')

        time.sleep(7)

        # Click on the 'Leverage' button
        leverage_button = browser.find_element(
            by=By.XPATH,
            value='//tabtitle[@name="leverage"]'
        )
        leverage_button.click()
        print('leverage_button.click() clicked')

        time.sleep(7)

        # Click on the 'X30' button
        x30_button = browser.find_element(
            by=By.XPATH,
            value='//a[@data-etoro-automation-id="execution-regular-risk-selection-30"]'
        )
        x30_button.click()
        print('x30_button.click() clicked')

        time.sleep(7)

        # Click on the 'Open Trade' button
        open_trade_button = browser.find_element(
            by=By.XPATH,
            value='//button[@data-etoro-automation-id="execution-open-position-button"]'
        )
        open_trade_button.click()
        print('open_trade_button.click() clicked')

        time.sleep(7)


if __name__ == '__main__':
    unittest.main()
