import unittest
import time
import requests
from bs4 import BeautifulSoup
from pywinauto.application import Application
import pywinauto.mouse
import pywinauto.keyboard


class UnitTestsDesktopAutomationFreelanceInfo(unittest.TestCase):
    def test_connect_to_my_account_from_one_ad(self):
        app = Application(backend="uia")

        url_ad = "https://www.freelance-info.fr/mission/developpeur-senior-fullstack-mobile-ionic-pwa-java-angular-1585426"

        # Ouvrir l'application Edge
        app.start("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")

        time.sleep(5)

        # Open the Freelance-info.fr
        pywinauto.keyboard.send_keys(url_ad)

        time.sleep(5)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(5)

        # Click on the screen
        pywinauto.mouse.click(button="left", coords=(500, 670))

        time.sleep(5)

        # Tab 2 times to reach "Postuler" button
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(5)

        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(5)

        # Click on "Email" input
        pywinauto.mouse.click(button="left", coords=(600, 450))

        time.sleep(5)

        # Insert the email
        pywinauto.keyboard.send_keys('.@holomorphe.com')

        time.sleep(5)

        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(5)

        # Insert the M_D_P
        pywinauto.keyboard.send_keys('')

        time.sleep(5)

        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(5)

        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(5)

        pywinauto.mouse.click(button="left", coords=(500, 670))

        time.sleep(5)

        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(5)

        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(5)

        pywinauto.mouse.click(button="left", coords=(1170, 85))

        time.sleep(5)

        # Close the browser
        pywinauto.keyboard.send_keys('%{F4}')

        time.sleep(5)

    def test_connect_to_my_account_from_several_ads(self):
        app = Application(backend="uia")

        urls_ad = [
            ""
        ]

        for url_ad in urls_ad:
            # Ouvrir l'application Edge
            app.start("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")

            time.sleep(5)

            # Open the Freelance-info.fr
            pywinauto.keyboard.send_keys(url_ad)

            time.sleep(5)

            # Press the 'Enter' button
            pywinauto.keyboard.send_keys('{ENTER}')

            time.sleep(5)

            # Click on the screen
            pywinauto.mouse.click(button="left", coords=(500, 670))

            time.sleep(5)

            # Tab 2 times to reach "Postuler" button
            pywinauto.keyboard.send_keys("{VK_TAB 2}")

            time.sleep(5)

            pywinauto.keyboard.send_keys('{ENTER}')

            time.sleep(5)

            # Click on "Email" input
            pywinauto.mouse.click(button="left", coords=(600, 450))

            time.sleep(5)

            # Insert the email
            pywinauto.keyboard.send_keys('.@holomorphe.com')

            time.sleep(5)

            pywinauto.keyboard.send_keys("{VK_TAB}")

            time.sleep(5)

            # Insert the M_D_P
            pywinauto.keyboard.send_keys('')

            time.sleep(5)

            pywinauto.keyboard.send_keys("{VK_TAB}")

            time.sleep(5)

            pywinauto.keyboard.send_keys('{ENTER}')

            time.sleep(5)

            pywinauto.mouse.click(button="left", coords=(500, 670))

            time.sleep(5)

            pywinauto.keyboard.send_keys("{VK_TAB}")

            time.sleep(5)

            pywinauto.keyboard.send_keys('{ENTER}')

            time.sleep(5)

            pywinauto.mouse.click(button="left", coords=(1170, 85))

            time.sleep(5)

            # Close the browser
            pywinauto.keyboard.send_keys('%{F4}')

            time.sleep(5)

    def test_connect_to_my_account_from_several_ads_from_all_result_page(self):
        print("test_connect_to_my_account_from_several_ads_from_all_result_page")

        i = 1

        # 770
        for x in range(1, 7):
            print("result page : " + str(x))

            url_result_page = "https://www.freelance-info.fr/missions?page=" + str(x)

            # Request the content of a page from the url
            html = requests.get(url_result_page)

            time.sleep(5)

            # Parse the content of html_doc
            soup = BeautifulSoup(html.content, 'html.parser')

            if soup.select("#offre") is not None:
                print("offres ok")

                all_offre = soup.select("#offre")

                for offre in all_offre:
                    time.sleep(5)

                    print("link " + str(i) + " : https://www.freelance-info.fr"
                          + offre.select_one("#titre-mission").find('a').get('href'))

                    app = Application(backend="uia")

                    time.sleep(5)

                    url_ad = "https://www.freelance-info.fr" + str(offre
                                                                   .select_one("#titre-mission")
                                                                   .find('a')
                                                                   .get('href'))

                    time.sleep(5)

                    # Ouvrir l'application Edge
                    app.start("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")

                    time.sleep(5)

                    # Open the Freelance-info.fr
                    pywinauto.keyboard.send_keys(url_ad)

                    time.sleep(5)

                    # Press the 'Enter' button
                    pywinauto.keyboard.send_keys('{ENTER}')

                    time.sleep(5)

                    # Click on the screen
                    pywinauto.mouse.click(button="left", coords=(500, 670))

                    time.sleep(5)

                    # Tab 2 times to reach "Postuler" button
                    pywinauto.keyboard.send_keys("{VK_TAB 2}")

                    time.sleep(5)

                    pywinauto.keyboard.send_keys('{ENTER}')

                    time.sleep(5)

                    # Click on "Email" input
                    pywinauto.mouse.click(button="left", coords=(600, 450))

                    time.sleep(5)

                    # Insert the email
                    pywinauto.keyboard.send_keys('.@holomorphe.com')

                    time.sleep(5)

                    pywinauto.keyboard.send_keys("{VK_TAB}")

                    time.sleep(5)

                    # Insert the M_D_P
                    pywinauto.keyboard.send_keys('')

                    time.sleep(5)

                    pywinauto.keyboard.send_keys("{VK_TAB}")

                    time.sleep(5)

                    pywinauto.keyboard.send_keys('{ENTER}')

                    time.sleep(5)

                    pywinauto.mouse.click(button="left", coords=(500, 670))

                    time.sleep(5)

                    pywinauto.keyboard.send_keys("{VK_TAB}")

                    time.sleep(5)

                    pywinauto.keyboard.send_keys('{ENTER}')

                    time.sleep(5)

                    pywinauto.mouse.click(button="left", coords=(1170, 85))

                    time.sleep(5)

                    # Close the browser
                    pywinauto.keyboard.send_keys('%{F4}')

                    time.sleep(5)

                    i += 1
            else:
                print("no offres")


if __name__ == '__main__':
    unittest.main()
