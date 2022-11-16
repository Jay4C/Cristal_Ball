import subprocess
import unittest
import time
import warnings
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.firefox.options import Options


class UnitTestsWebAutomationFreelancerCom(unittest.TestCase):
    # ok
    def test_kill_some_processes(self):
        print("test_kill_some_processes")

        subprocess.call("taskkill /F /IM geckodriver.exe")
        subprocess.call("taskkill /F /IM firefox.exe")

    # ok
    def test_se_connecter(self):
        print("test_se_connecter")

        email = ".@outlook.fr"

        password = ""

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
        browser.get('https://www.freelancer.com/login')
        print("browser.get('https://www.freelancer.com/login')")

        time.sleep(15)

        email_input = browser.find_element_by_xpath(
            '/html/body/app-root/app-logged-out-shell/app-login-page/fl-container/fl-bit/app-login'
            '/app-credentials-form/form/fl-input[1]/fl-bit/fl-bit/fl-bit/input'
        )
        email_input.clear()
        email_input.send_keys(email)
        print('email_input.send_keys(email)')

        time.sleep(5)

        password_input = browser.find_element_by_xpath(
            '/html/body/app-root/app-logged-out-shell/app-login-page/fl-container/fl-bit/app-login'
            '/app-credentials-form/form/fl-input[2]/fl-bit/fl-bit/fl-bit/input'
        )
        password_input.clear()
        password_input.send_keys(password)
        print('password_input.send_keys(password)')

        time.sleep(5)

        log_in_button = browser.find_element_by_xpath(
            '/html/body/app-root/app-logged-out-shell/app-login-page/fl-container/fl-bit/app-login'
            '/app-credentials-form/form/app-login-signup-button/fl-button/button'
        )
        log_in_button.click()
        print("log_in_button.click()")

        time.sleep(5)

    # ok
    def test_extract_all_project_links_from_the_first_page(self):
        print('test_extract_all_project_links_from_the_first_page')

        email = ".@outlook.fr"

        password = ""

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
        browser.get('https://www.freelancer.com/login')
        print("browser.get('https://www.freelancer.com/login')")

        time.sleep(15)

        email_input = browser.find_element_by_xpath(
            '/html/body/app-root/app-logged-out-shell/app-login-page/fl-container/fl-bit/app-login'
            '/app-credentials-form/form/fl-input[1]/fl-bit/fl-bit/fl-bit/input'
        )
        email_input.clear()
        email_input.send_keys(email)
        print('email_input.send_keys(email)')

        time.sleep(5)

        password_input = browser.find_element_by_xpath(
            '/html/body/app-root/app-logged-out-shell/app-login-page/fl-container/fl-bit/app-login'
            '/app-credentials-form/form/fl-input[2]/fl-bit/fl-bit/fl-bit/input'
        )
        password_input.clear()
        password_input.send_keys(password)
        print('password_input.send_keys(password)')

        time.sleep(5)

        log_in_button = browser.find_element_by_xpath(
            '/html/body/app-root/app-logged-out-shell/app-login-page/fl-container/fl-bit/app-login'
            '/app-credentials-form/form/app-login-signup-button/fl-button/button'
        )
        log_in_button.click()
        print("log_in_button.click()")

        time.sleep(60)

        # Load the first "project" page
        first_project_page = "https://www.freelancer.com/search/projects?projectLanguages=en,fr&projectSkills=9,13," \
                             "37,39,42,43,55,254,305,329,334,335,440,463,472,509,686,1422,1596,2134&page=1"
        browser.get(first_project_page)
        print("browser.get(first_project_page)")

        time.sleep(60)

        all_fl_list_item = browser.find_elements_by_tag_name(
            'fl-list-item'
        )
        print('extract all_a')

        time.sleep(10)

        i = 0

        for a in all_fl_list_item:
            try:
                if a.find_element_by_tag_name('fl-bit')\
                        .find_element_by_tag_name('fl-bit')\
                        .find_element_by_tag_name('fl-bit')\
                        .find_element_by_tag_name('fl-bit')\
                        .find_element_by_tag_name('fl-link')\
                        .find_element_by_tag_name('a') \
                        .get_attribute("href") is not None:
                    project = a.find_element_by_tag_name('fl-bit')\
                        .find_element_by_tag_name('fl-bit')\
                        .find_element_by_tag_name('fl-bit')\
                        .find_element_by_tag_name('fl-bit')\
                        .find_element_by_tag_name('fl-link')\
                        .find_element_by_tag_name('a') \
                        .get_attribute("href")
                    print(str(i) + " _ " + project)
                    i += 1
            except Exception as e:
                print('error for all_a : ' + str(e))

        time.sleep(5)

    # ok
    def test_propose_offer_for_one_project(self):
        print('test_propose_offer_for_one_project')

        email = ".@outlook.fr"

        password = ""

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
        browser.get('https://www.freelancer.com/login')
        print("browser.get('https://www.freelancer.com/login')")

        time.sleep(15)

        email_input = browser.find_element_by_xpath(
            '/html/body/app-root/app-logged-out-shell/app-login-page/fl-container/fl-bit/app-login'
            '/app-credentials-form/form/fl-input[1]/fl-bit/fl-bit/fl-bit/input'
        )
        email_input.clear()
        email_input.send_keys(email)
        print('email_input.send_keys(email)')

        time.sleep(5)

        password_input = browser.find_element_by_xpath(
            '/html/body/app-root/app-logged-out-shell/app-login-page/fl-container/fl-bit/app-login'
            '/app-credentials-form/form/fl-input[2]/fl-bit/fl-bit/fl-bit/input'
        )
        password_input.clear()
        password_input.send_keys(password)
        print('password_input.send_keys(password)')

        time.sleep(5)

        log_in_button = browser.find_element_by_xpath(
            '/html/body/app-root/app-logged-out-shell/app-login-page/fl-container/fl-bit/app-login'
            '/app-credentials-form/form/app-login-signup-button/fl-button/button'
        )
        log_in_button.click()
        print("log_in_button.click()")

        time.sleep(30)

        # Open the project
        link_project = "https://www.freelancer.com/projects/django/django-Project-33847396/details"
        browser.get(link_project)
        print('browser.get(link_project)')

        time.sleep(15)

        # Insert 'Ce projet sera livré dans' input text
        ce_projet_sera_livre_dans_input = browser.find_element_by_xpath(
            '//*[@id="periodInput"]'
        )
        ce_projet_sera_livre_dans_input.clear()
        ce_projet_sera_livre_dans_input.send_keys('8')
        print("ce_projet_sera_livre_dans_input.send_keys('8')")

        time.sleep(5)

        # Insert 'Décrivez votre proposition' input text
        decrivez_votre_proposition_input = browser.find_element_by_xpath(
            '//*[@id="descriptionTextArea"]'
        )
        decrivez_votre_proposition_input.clear()
        decrivez_votre_proposition_input.send_keys(
            """Hello,
Firstly, I am Python developper and I can use another programming languages such as Java, JavaScript, Visual Basic and more.
After, I can write computing programs for digitalizing everything to achieve any goals by using the Gantt methodology and I can do remotely from anywhere what you need for your digital project.
Besides, I have a GitHub account : https://www.github.com/Jay4C and you can call me at  to discuss more and more about your project.
Kind regards,
"""
        )
        print('decrivez_votre_proposition_input.send_keys')

        time.sleep(10)

        # Budget maximal de l'offre
        budget_maximal_de_l_offre_text = browser.find_element_by_xpath(
            '/html/body/app-root/app-logged-in-shell/div/fl-container/div/div/app-project-view'
            '/app-project-view-details/fl-page-layout/main/fl-container/fl-page-layout-single/fl-grid/fl-col[1]'
            '/fl-card/fl-bit/fl-bit[1]/fl-bit/fl-bit/fl-card-header-right/fl-bit/app-project-details-budget'
            '/fl-bit/fl-text[1]/div'
        ).text.split(' – ')[1].split(' ')[0]
        print('budget_maximal_de_l_offre_text : ' + str(budget_maximal_de_l_offre_text))

        time.sleep(5)

        # Insert 'Montant de l'offre' input text
        montant_de_l_offre_input = browser.find_element_by_xpath(
            '//*[@id="bidAmountInput"]'
        )
        montant_de_l_offre_input.click()
        montant_de_l_offre_input.clear()
        montant_de_l_offre_input.send_keys("")
        action = ActionChains(browser)
        action.send_keys(Keys.BACKSPACE * 20).perform()
        montant_de_l_offre_input.send_keys(budget_maximal_de_l_offre_text)
        print('montant_de_l_offre_input.send_keys(budget_maximal_de_l_offre_text)')

        time.sleep(5)

        # Click the "Faire une offre" button
        faire_une_offre_button = browser.find_element_by_xpath(
            "/html/body/app-root/app-logged-in-shell/div/fl-container/div/div/app-project-view/app-project-view-details"
            "/fl-page-layout/main/fl-container/fl-page-layout-single/fl-grid/fl-col[1]/app-project-details-freelancer"
            "/app-bid-form/fl-card/fl-bit/fl-bit[2]/fl-bit[2]/fl-button/button"
        )
        faire_une_offre_button.click()
        print('faire_une_offre_button.click()')

        time.sleep(5)

    # ok
    def test_propose_offer_for_some_projects_from_static_urls(self):
        print('test_propose_offer_for_some_projects_from_static_urls')

        email = ".@outlook.fr"

        password = ""

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
        browser.get('https://www.freelancer.com/login')
        print("browser.get('https://www.freelancer.com/login')")

        time.sleep(15)

        email_input = browser.find_element_by_xpath(
            '/html/body/app-root/app-logged-out-shell/app-login-page/fl-container/fl-bit/app-login'
            '/app-credentials-form/form/fl-input[1]/fl-bit/fl-bit/fl-bit/input'
        )
        email_input.clear()
        email_input.send_keys(email)
        print('email_input.send_keys(email)')

        time.sleep(5)

        password_input = browser.find_element_by_xpath(
            '/html/body/app-root/app-logged-out-shell/app-login-page/fl-container/fl-bit/app-login'
            '/app-credentials-form/form/fl-input[2]/fl-bit/fl-bit/fl-bit/input'
        )
        password_input.clear()
        password_input.send_keys(password)
        print('password_input.send_keys(password)')

        time.sleep(5)

        log_in_button = browser.find_element_by_xpath(
            '/html/body/app-root/app-logged-out-shell/app-login-page/fl-container/fl-bit/app-login'
            '/app-credentials-form/form/app-login-signup-button/fl-button/button'
        )
        log_in_button.click()
        print("log_in_button.click()")

        time.sleep(30)

        links_project = [
            'https://www.freelancer.com/projects/virtual-assistant/Virtual-Assitant-33847704/details',
            'https://www.freelancer.com/projects/wordpress/Optimize-Wordpress-Website-PageSpeed/details',
            'https://www.freelancer.com/projects/excel/Compile-organize-data-from-the/details',
            'https://www.freelancer.com/projects/virtual-assistant/Virtual-assistant-request-wedding-photos/details',
            'https://www.freelancer.com/projects/javascript/Care-Control-Vue/details'
        ]

        for link_project in links_project:
            # Open the project
            browser.get(link_project)
            print('browser.get(link_project)')

            time.sleep(15)

            try:
                # Insert 'Ce projet sera livré dans' input text
                ce_projet_sera_livre_dans_input = browser.find_element_by_xpath(
                    '//*[@id="periodInput"]'
                )
                ce_projet_sera_livre_dans_input.clear()
                ce_projet_sera_livre_dans_input.send_keys('8')
                print("ce_projet_sera_livre_dans_input.send_keys('8')")

                time.sleep(5)

                # Insert 'Décrivez votre proposition' input text
                decrivez_votre_proposition_input = browser.find_element_by_xpath(
                    '//*[@id="descriptionTextArea"]'
                )
                decrivez_votre_proposition_input.clear()
                decrivez_votre_proposition_input.send_keys(
                    """Hello,
Firstly, I am Python developper and I can use another programming languages such as Java, JavaScript, Visual Basic and more.
After, I can write computing programs for digitalizing everything to achieve any goals by using the Gantt methodology and I can do remotely from anywhere what you need for your digital project.
Besides, I have a GitHub account : https://www.github.com/Jay4C and you can call me at  to discuss more and more about your project.
Kind regards,
"""
                )
                print('decrivez_votre_proposition_input.send_keys')

                time.sleep(10)

                # Budget maximal de l'offre
                budget_maximal_de_l_offre_text = browser.find_element_by_xpath(
                    '/html/body/app-root/app-logged-in-shell/div/fl-container/div/div/app-project-view'
                    '/app-project-view-details/fl-page-layout/main/fl-container/fl-page-layout-single/fl-grid/fl-col[1]'
                    '/fl-card/fl-bit/fl-bit[1]/fl-bit/fl-bit/fl-card-header-right/fl-bit/app-project-details-budget'
                    '/fl-bit/fl-text[1]/div'
                ).text.split(' – ')[1].split(' ')[0]
                print('budget_maximal_de_l_offre_text : ' + str(budget_maximal_de_l_offre_text))

                time.sleep(5)

                # Insert 'Montant de l'offre' input text
                montant_de_l_offre_input = browser.find_element_by_xpath(
                    '//*[@id="bidAmountInput"]'
                )
                montant_de_l_offre_input.click()
                montant_de_l_offre_input.clear()
                montant_de_l_offre_input.send_keys("")
                action = ActionChains(browser)
                action.send_keys(Keys.BACKSPACE * 20).perform()
                montant_de_l_offre_input.send_keys(budget_maximal_de_l_offre_text)
                print('montant_de_l_offre_input.send_keys(budget_maximal_de_l_offre_text)')

                time.sleep(5)

                # Click the "Faire une offre" button
                faire_une_offre_button = browser.find_element_by_xpath(
                    "/html/body/app-root/app-logged-in-shell/div/fl-container/div/div/app-project-view"
                    "/app-project-view-details/fl-page-layout/main/fl-container/fl-page-layout-single/fl-grid"
                    "/fl-col[1]/app-project-details-freelancer/app-bid-form/fl-card/fl-bit/fl-bit[2]/fl-bit[2]"
                    "/fl-button/button"
                )
                faire_une_offre_button.click()
                print('faire_une_offre_button.click()')

                time.sleep(5)
            except Exception as e:
                print('error link_project : ' + str(e))

    # ok
    def test_propose_offer_for_projects_from_urls_from_the_first_page_projects(self):
        print('test_propose_offer_for_projects_from_urls_from_the_first_page_projects')

        email = ".@outlook.fr"

        password = ""

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
        browser.get('https://www.freelancer.com/login')
        print("browser.get('https://www.freelancer.com/login')")

        time.sleep(15)

        email_input = browser.find_element_by_xpath(
            '/html/body/app-root/app-logged-out-shell/app-login-page/fl-container/fl-bit/app-login'
            '/app-credentials-form/form/fl-input[1]/fl-bit/fl-bit/fl-bit/input'
        )
        email_input.clear()
        email_input.send_keys(email)
        print('email_input.send_keys(email)')

        time.sleep(5)

        password_input = browser.find_element_by_xpath(
            '/html/body/app-root/app-logged-out-shell/app-login-page/fl-container/fl-bit/app-login'
            '/app-credentials-form/form/fl-input[2]/fl-bit/fl-bit/fl-bit/input'
        )
        password_input.clear()
        password_input.send_keys(password)
        print('password_input.send_keys(password)')

        time.sleep(5)

        log_in_button = browser.find_element_by_xpath(
            '/html/body/app-root/app-logged-out-shell/app-login-page/fl-container/fl-bit/app-login'
            '/app-credentials-form/form/app-login-signup-button/fl-button/button'
        )
        log_in_button.click()
        print("log_in_button.click()")

        time.sleep(60)

        # Load the first "project" page
        first_project_page = "https://www.freelancer.com/search/projects?projectLanguages=en,fr&projectSkills=9,13," \
                             "37,39,42,43,55,254,305,329,334,335,440,463,472,509,686,1422,1596,2134&page=" + str(1)
        browser.get(first_project_page)
        print("browser.get(first_project_page)")

        time.sleep(60)

        all_fl_list_item = browser.find_elements_by_tag_name(
            'fl-list-item'
        )
        print('extract all_a')

        time.sleep(10)

        links_project = []

        for a in all_fl_list_item:
            try:
                if a.find_element_by_tag_name('fl-bit')\
                        .find_element_by_tag_name('fl-bit')\
                        .find_element_by_tag_name('fl-bit')\
                        .find_element_by_tag_name('fl-bit')\
                        .find_element_by_tag_name('fl-link')\
                        .find_element_by_tag_name('a') \
                        .get_attribute("href") is not None:
                    link_project = a.find_element_by_tag_name('fl-bit')\
                        .find_element_by_tag_name('fl-bit')\
                        .find_element_by_tag_name('fl-bit')\
                        .find_element_by_tag_name('fl-bit')\
                        .find_element_by_tag_name('fl-link')\
                        .find_element_by_tag_name('a') \
                        .get_attribute("href")
                    links_project.append(link_project)
                    print("links_project.append(link_project) : " + link_project)
                    time.sleep(5)
            except Exception as e:
                print('error for all_a : ' + str(e))

        time.sleep(10)

        for link in links_project:
            # Open the project
            browser.get(link)
            print('browser.get(link)')

            time.sleep(15)

            try:
                # Insert 'Ce projet sera livré dans' input text
                ce_projet_sera_livre_dans_input = browser.find_element_by_xpath(
                    '//*[@id="periodInput"]'
                )
                ce_projet_sera_livre_dans_input.clear()
                ce_projet_sera_livre_dans_input.send_keys('8')
                print("ce_projet_sera_livre_dans_input.send_keys('8')")

                time.sleep(5)

                # Insert 'Décrivez votre proposition' input text
                decrivez_votre_proposition_input = browser.find_element_by_xpath(
                    '//*[@id="descriptionTextArea"]'
                )
                decrivez_votre_proposition_input.clear()
                decrivez_votre_proposition_input.send_keys(
                    """Hello,
Firstly, I am Python developper and I can use another programming languages such as Java, JavaScript, Visual Basic and more.
After, I can write computing programs for digitalizing everything to achieve any goals by using the Gantt methodology and I can do remotely from anywhere what you need for your digital project.
Besides, I have a GitHub account : https://www.github.com/Jay4C and you can call me at  to discuss more and more about your project.
Kind regards,
"""
                )
                print('decrivez_votre_proposition_input.send_keys')

                time.sleep(10)

                # Budget maximal de l'offre
                budget_maximal_de_l_offre_text = browser.find_element_by_xpath(
                    '/html/body/app-root/app-logged-in-shell/div/fl-container/div/div/app-project-view'
                    '/app-project-view-details/fl-page-layout/main/fl-container/fl-page-layout-single'
                    '/fl-grid/fl-col[1]/fl-card/fl-bit/fl-bit[1]/fl-bit/fl-bit/fl-card-header-right/fl-bit'
                    '/app-project-details-budget/fl-bit/fl-text[1]/div'
                ).text.split(' – ')[1].split(' ')[0]
                print('budget_maximal_de_l_offre_text : ' + str(budget_maximal_de_l_offre_text))

                time.sleep(5)

                # Insert 'Montant de l'offre' input text
                montant_de_l_offre_input = browser.find_element_by_xpath(
                    '//*[@id="bidAmountInput"]'
                )
                montant_de_l_offre_input.click()
                montant_de_l_offre_input.clear()
                montant_de_l_offre_input.send_keys("")
                action = ActionChains(browser)
                action.send_keys(Keys.BACKSPACE * 20).perform()
                montant_de_l_offre_input.send_keys(budget_maximal_de_l_offre_text)
                print('montant_de_l_offre_input.send_keys(budget_maximal_de_l_offre_text)')

                time.sleep(5)

                # Click the "Faire une offre" button
                faire_une_offre_button = browser.find_element_by_xpath(
                    "/html/body/app-root/app-logged-in-shell/div/fl-container/div/div/app-project-view"
                    "/app-project-view-details/fl-page-layout/main/fl-container/fl-page-layout-single/fl-grid"
                    "/fl-col[1]/app-project-details-freelancer/app-bid-form/fl-card/fl-bit/fl-bit[2]/fl-bit[2]"
                    "/fl-button/button"
                )
                faire_une_offre_button.click()
                print('faire_une_offre_button.click()')

                time.sleep(5)
            except Exception as e:
                print('error link : ' + str(e))

        time.sleep(5)


if __name__ == '__main__':
    unittest.main()
