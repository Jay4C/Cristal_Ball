import time
import unittest
import requests
from bs4 import BeautifulSoup
from pywinauto.application import Application
import pywinauto.keyboard
import pywinauto.mouse
import pywinauto.base_wrapper
import pywinauto.timings
import os


class UnitTestsDesktopAutomationIndeed(unittest.TestCase):
    #
    def test_send_cv_for_one_ad_page(self):
        print('test_send_cv_for_one_ad_page')

        url_ad = "https://fr.indeed.com/viewjob?jk=770fa77865016858&q=d%C3%A9veloppeur+python&l=%C3%8Ele-de-France&tk=1g1if802ht1ct800&from=web&advn=9026446452388180&adid=386291162&ad=-6NYlbfkN0CPgv7UdRRdRmrf_Qze3J78TvWvcQlOHNV6Sf8HGtpS7Kn2ooKuDX86u4olrmRSBE0cagXJn2BdJCgmZvnWFwf6YJGSNM8-KF3cAPvDkF81N8NVfha7F1jrs-WJmC3InMZF8zZwAJTAZulRFjKGaZkVR8J2aYntCtA8E5z_ZYKGiYcu-8Pa7hE_sIBx2N-Yb59iWC1S_av93npGIDD77_UvjVn6OugbkKSkeD6JJfQXjxNmpi1EmQv0S0JlcKjqEi3Dv9BfAolCH4bm49u5774YNR9maS30ECcqJeWg2_yeHKmfn1JV0_AjbqfGTOrpyAv78l9pllv7BD0uWvV6nfDihrsmflhyfciwAjAL8ZHFtf1_go6yxsCP&pub=4a1b367933fd867b19b072952f68dceb&vjs=3"

        app = Application(backend="uia")

        app.start("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")

        time.sleep(7)

        # Insert the "url_ad"
        pywinauto.keyboard.send_keys(url_ad)

        time.sleep(5)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(10)

        # Click on the "Postuler" button
        pywinauto.mouse.click(button='left', coords=(400, 400))

        time.sleep(10)

        # Close the onglet
        pywinauto.keyboard.send_keys('^w')

        time.sleep(7)

    #
    def test_send_cv_for_all_ad_page_on_indeed(self):
        print("test_send_cv_for_all_ad_page")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        # 77
        for i in range(0, 2):
            print('page : ' + str(i))

            start = str(10 * i)

            url = "https://fr.indeed.com/jobs?q=freelance+informatique&l=France&start=" + start

            # Request the content of a page from the url
            html = requests.get(url, headers=headers)

            time.sleep(10)

            # Parse the content of html_doc
            soup = BeautifulSoup(html.content, 'html.parser')

            if soup.find("a", {"data-tn-element": "jobTitle"}) is not None:
                all_a = soup.find_all("a", {"data-tn-element": "jobTitle"})

                for a in all_a:
                    link = "https://fr.indeed.com" + a.get('href')

                    # Request the content of a page from the url
                    html = requests.get(link, headers=headers)

                    time.sleep(10)

                    # Parse the content of html_doc
                    soup = BeautifulSoup(html.content, 'html.parser')

                    if soup.find("div", {"class": "jobsearch-IndeedApplyButton-contentWrapper"}) is not None:
                        title = soup \
                            .find("div", {"class": "jobsearch-IndeedApplyButton-contentWrapper"}) \
                            .find('span') \
                            .text

                        if title == "Postuler":
                            print("button Postuler ok : " + link)

                            app = Application(backend="uia")

                            app.start("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")

                            time.sleep(7)

                            pywinauto.keyboard.send_keys(link)

                            time.sleep(7)

                            # Press the 'Enter' button
                            pywinauto.keyboard.send_keys('{ENTER}')

                            time.sleep(7)

                            # Click on the "Postuler" button
                            pywinauto.mouse.click(button='left', coords=(380, 330))

                            time.sleep(7)

                            # Insert "Prénom NOM"
                            pywinauto.keyboard.send_keys('{VK_SPACE}')

                            time.sleep(7)

                            # Tab 2 times to "Email"
                            pywinauto.keyboard.send_keys("{VK_TAB 2}")

                            time.sleep(7)

                            # Insert "Email"
                            pywinauto.keyboard.send_keys('.@outlook.fr')

                            time.sleep(7)

                            # Tab 1 time to "Numéro de téléphone"
                            pywinauto.keyboard.send_keys("{VK_TAB}")

                            time.sleep(7)

                            # Insert "Numéro de téléphone"
                            pywinauto.keyboard.send_keys('')

                            time.sleep(7)

                            # Tab 2 times to "Email"
                            pywinauto.keyboard.send_keys("{VK_TAB 2}")

                            time.sleep(7)

                            # Insert "Ville - France"
                            pywinauto.keyboard.send_keys('Paris{VK_SPACE}75')

                            time.sleep(7)

                            # Tab 1 time to "Intitulé du poste"
                            pywinauto.keyboard.send_keys("{VK_TAB}")

                            time.sleep(7)

                            # Insert "Intitulé du poste"
                            pywinauto.keyboard.send_keys('Développeur{VK_SPACE}intelligence{VK_SPACE}artificielle')

                            time.sleep(7)

                            # Tab 1 time to "Entreprise"
                            pywinauto.keyboard.send_keys("{VK_TAB}")

                            time.sleep(7)

                            # Insert "Entreprise"
                            pywinauto.keyboard.send_keys('Holomorphe')

                            time.sleep(7)

                            # Tab 1 time to "CV"
                            pywinauto.keyboard.send_keys("{VK_TAB}")

                            time.sleep(7)

                            # Press the 'Enter' button
                            pywinauto.keyboard.send_keys('{ENTER}')

                            time.sleep(7)

                            # Click on the file
                            pywinauto.mouse.click(button='left', coords=(300, 185))

                            time.sleep(7)

                            # Click on the "Ouvrir" button
                            pywinauto.mouse.click(button='left', coords=(500, 450))

                            time.sleep(7)

                            # Tab 8 times to "Continuer"
                            pywinauto.keyboard.send_keys("{VK_TAB 8}")

                            time.sleep(7)

                            # Press the 'Enter' button
                            pywinauto.keyboard.send_keys('{ENTER}')

                            time.sleep(7)

                            # Click on 'Ctrl+t' to open a new onlget
                            pywinauto.keyboard.send_keys('^t')

                            time.sleep(7)

                            # Open the Outlook Application
                            pywinauto.keyboard.send_keys("https://outlook.live.com/owa/")

                            time.sleep(7)

                            # Press the 'Enter' button
                            pywinauto.keyboard.send_keys('{ENTER}')

                            time.sleep(7)

                            # Click on the 'Connexion' button
                            pywinauto.mouse.click(button='left', coords=(1100, 100))

                            time.sleep(7)

                            # Type the email address
                            pywinauto.keyboard.send_keys('.@outlook.fr')

                            time.sleep(7)

                            # Tab 4 times to the 'Suivant' button
                            pywinauto.keyboard.send_keys('{VK_TAB 4}')

                            time.sleep(7)

                            # Press the 'Enter' button
                            pywinauto.keyboard.send_keys('{ENTER}')

                            time.sleep(7)

                            # Type the password
                            pywinauto.keyboard.send_keys('')

                            time.sleep(7)

                            # Type the Tab in 3 times
                            pywinauto.keyboard.send_keys('{VK_TAB 3}')

                            time.sleep(7)

                            # Press the 'Enter' button
                            pywinauto.keyboard.send_keys('{ENTER}')

                            time.sleep(7)

                            # Click on the 'Indeed Apply' button
                            pywinauto.mouse.click(button='left', coords=(370, 240))

                            time.sleep(7)

                            # Double-click on the code
                            pywinauto.mouse.double_click(button='left', coords=(540, 470))

                            time.sleep(7)

                            # Click on 'Ctrl+c'
                            pywinauto.keyboard.send_keys('^c')

                            time.sleep(7)

                            # Click on the first page
                            pywinauto.mouse.double_click(button='left', coords=(110, 10))

                            time.sleep(7)

                            # Click on the "code" input
                            pywinauto.mouse.double_click(button='left', coords=(490, 360))

                            time.sleep(7)

                            # Insert the code
                            pywinauto.keyboard.send_keys('^v')

                            time.sleep(7)

                            # Type the Tab in 4 times
                            pywinauto.keyboard.send_keys('{VK_TAB 4}')

                            time.sleep(7)

                            # Press the 'Enter' button
                            pywinauto.keyboard.send_keys('{ENTER}')

                            time.sleep(7)

                            # Peut etre
                            # Type the Tab in 1 time
                            pywinauto.keyboard.send_keys('{VK_TAB}')

                            time.sleep(7)

                            # Insert the experience
                            pywinauto.keyboard.send_keys('7')

                            time.sleep(7)

                            # Type the Tab in 1 time
                            pywinauto.keyboard.send_keys('{VK_TAB}')

                            time.sleep(7)

                            # Press the 'Enter' button
                            pywinauto.keyboard.send_keys('{ENTER}')

                            time.sleep(7)
                            # Peut etre

                            # Click on the screen
                            pywinauto.mouse.double_click(button='left', coords=(850, 460))

                            time.sleep(7)

                            # Type the Tab in 4 times
                            pywinauto.keyboard.send_keys('{VK_TAB 4}')

                            time.sleep(7)

                            # Press the 'Enter' button
                            pywinauto.keyboard.send_keys('{ENTER}')

                            time.sleep(7)

                            # Close the onglet
                            pywinauto.keyboard.send_keys('^w')

                            time.sleep(7)

                            # Click on the "Supprimer" button
                            pywinauto.mouse.double_click(button='left', coords=(320, 140))

                            time.sleep(7)

                            # Click on the 'Indeed Apply' button
                            pywinauto.mouse.click(button='left', coords=(370, 240))

                            time.sleep(7)

                            # Click on the 'Déplacer vers' button
                            pywinauto.mouse.click(button='left', coords=(800, 140))

                            time.sleep(7)

                            # Click on the 'Indeed' button
                            pywinauto.mouse.click(button='left', coords=(800, 280))

                            time.sleep(7)

                            # Click on the 'Profile' button
                            pywinauto.mouse.click(button='left', coords=(1340, 90))

                            time.sleep(7)

                            # Click on the 'Déconnexion' button
                            pywinauto.mouse.click(button='left', coords=(1300, 140))

                            time.sleep(7)

                            # Close the browser
                            pywinauto.keyboard.send_keys('%{F4}')

                            time.sleep(7)

                            print("ccleaner running")
                            os.system("set ccleaner='C:\\Program Files\\CCleaner\\CCleaner.exe'")
                            os.system("start ccleaner /AUTO")

                            time.sleep(7)
                        else:
                            print("no button Postuler")
            else:
                print("no ads")


if __name__ == '__main__':
    unittest.main()
