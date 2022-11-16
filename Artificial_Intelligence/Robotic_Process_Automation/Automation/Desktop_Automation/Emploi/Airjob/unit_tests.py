import unittest
import time
import requests
from bs4 import BeautifulSoup
from pywinauto.application import Application
import pywinauto.mouse
import pywinauto.keyboard


class UnitTestsDesktopAutomationAirjob(unittest.TestCase):
    def test_connect_to_my_account_from_one_ad(self):
        app = Application(backend="uia")

        url_ad = ""

        time.sleep(3)

        # Ouvrir l'application CCleaner
        app.start("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")

        time.sleep(6)

        pywinauto.keyboard.send_keys(url_ad)

        time.sleep(3)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(6)

        pywinauto.mouse.click(button="left", coords=(230, 460))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(500, 305))

        time.sleep(3)

        # Type the email
        pywinauto.keyboard.send_keys("")

        time.sleep(3)

        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Type the password
        pywinauto.keyboard.send_keys("")

        time.sleep(3)

        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(6)

        # click on Postuler
        pywinauto.mouse.click(button="left", coords=(230, 460))

        time.sleep(4)

        # click on CV
        pywinauto.mouse.click(button="left", coords=(900, 180))

        time.sleep(4)

        # select the file
        pywinauto.mouse.click(button="left", coords=(340, 50))
        time.sleep(3)
        pywinauto.keyboard.send_keys("C:\\Users\\DELL\\Documents")
        time.sleep(3)
        pywinauto.keyboard.send_keys('{ENTER}')
        time.sleep(3)
        pywinauto.mouse.click(button="left", coords=(300, 230))
        time.sleep(3)
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(4)

        # select the input for the message
        pywinauto.mouse.click(button="left", coords=(860, 260))

        time.sleep(4)

        # write the message
        pywinauto.keyboard.send_keys("""
Bonjour,
{ENTER 2}
Merci{VK_SPACE}beaucoup{VK_SPACE}pour{VK_SPACE}votre{VK_SPACE}offre{VK_SPACE}de{VK_SPACE}mission.
{ENTER 2}
Je{VK_SPACE}suis{VK_SPACE}disponible{VK_SPACE}tout{VK_SPACE}de{VK_SPACE}suite{VK_SPACE}pour{VK_SPACE}
analyser{VK_SPACE}le{VK_SPACE}cahier{VK_SPACE}des{VK_SPACE}charges{VK_SPACE}de{VK_SPACE}votre{VK_SPACE}
projet{VK_SPACE}afin{VK_SPACE}de{VK_SPACE}parvenir{VK_SPACE}à{VK_SPACE}répondre{VK_SPACE}parfaitement{VK_SPACE}
à{VK_SPACE}vos{VK_SPACE}attentes{VK_SPACE}s'il{VK_SPACE}vous{VK_SPACE}plaît.
{ENTER 2}
Très{VK_SPACE}bonne{VK_SPACE}journée{VK_SPACE}à{VK_SPACE}vous,
{ENTER 2}
Mr{VK_SPACE}{VK_SPACE}
{ENTER}
Président{VK_SPACE}de{VK_SPACE}la{VK_SPACE}société{VK_SPACE}Holomorphe
{ENTER}
Ingénieur{VK_SPACE}généraliste{VK_SPACE}diplômé{VK_SPACE}à{VK_SPACE}l'Ecole{VK_SPACE}Supérieur{VK_SPACE}
d'Ingénieurs{VK_SPACE}Léonard{VK_SPACE}de{VK_SPACE}Vinci{VK_SPACE}à{VK_SPACE}Paris{VK_SPACE}La{VK_SPACE}Défense
{ENTER}
Adresse{VK_SPACE}du{VK_SPACE}siège{VK_SPACE}social:{VK_SPACE}31{VK_SPACE}Avenue{VK_SPACE}de{VK_SPACE}
Ségur{VK_SPACE}75007{VK_SPACE}Paris
{ENTER}
SIRET:{VK_SPACE}https://www.societe.com/societe/holomorphe-883632556.html
{ENTER}
Téléphone:{VK_SPACE}
{ENTER}
Site{VK_SPACE}internet:{VK_SPACE}https://holomorphe.com
{ENTER}
Malt:{VK_SPACE}https://www.malt.fr/profile/jasonaloyau
{ENTER}
Github:{VK_SPACE}https://github.com/Jay4C
        """)

        time.sleep(4)

        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(4)

        # envoyer ma candidature
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(7)

        # revenir tout en haut de la page
        pywinauto.keyboard.send_keys('{PGUP 7}')

        time.sleep(3)

        # type on the url bar 2 times
        pywinauto.mouse.click(button="left", coords=(820, 50))
        time.sleep(2)
        pywinauto.mouse.click(button="left", coords=(820, 50))

        time.sleep(4)

        # erase the phrase (#postuler)
        pywinauto.keyboard.send_keys('{BACKSPACE 9}')

        time.sleep(4)

        # refresh the page
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(4)

        # Je me déconnecte
        pywinauto.mouse.click(button="left", coords=(1200, 230))

        time.sleep(4)

        # Close the browser
        pywinauto.keyboard.send_keys('%{F4}')

        time.sleep(5)

    def test_connect_to_my_account_from_several_ads(self):
        app = Application(backend="uia")

        urls_ad = [
            ""
        ]

        for url_ad in urls_ad:
            print(url_ad)

            time.sleep(3)

            # Ouvrir l'application CCleaner
            app.start("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")

            time.sleep(6)

            pywinauto.keyboard.send_keys(url_ad)

            time.sleep(3)

            # Press the 'Enter' button
            pywinauto.keyboard.send_keys('{ENTER}')

            time.sleep(6)

            pywinauto.mouse.click(button="left", coords=(230, 460))

            time.sleep(3)

            pywinauto.mouse.click(button="left", coords=(500, 305))

            time.sleep(3)

            pywinauto.keyboard.send_keys(".@holomorphe.com")

            time.sleep(3)

            pywinauto.keyboard.send_keys("{VK_TAB}")

            time.sleep(3)

            pywinauto.keyboard.send_keys("")

            time.sleep(3)

            pywinauto.keyboard.send_keys("{VK_TAB 2}")

            time.sleep(3)

            pywinauto.keyboard.send_keys('{ENTER}')

            time.sleep(6)

            # click on Postuler
            pywinauto.mouse.click(button="left", coords=(230, 460))

            time.sleep(4)

            # click on CV
            pywinauto.mouse.click(button="left", coords=(900, 180))

            time.sleep(4)

            # select the file
            pywinauto.mouse.click(button="left", coords=(340, 50))
            time.sleep(3)
            pywinauto.keyboard.send_keys("C:\\Users\\DELL\\Documents")
            time.sleep(3)
            pywinauto.keyboard.send_keys('{ENTER}')
            time.sleep(3)
            pywinauto.mouse.click(button="left", coords=(300, 230))
            time.sleep(3)
            pywinauto.keyboard.send_keys('{ENTER}')

            time.sleep(4)

            # select the input for the message
            pywinauto.mouse.click(button="left", coords=(860, 260))

            time.sleep(4)

            # write the message
            pywinauto.keyboard.send_keys("""
    Bonjour,
    {ENTER 2}
    Merci{VK_SPACE}beaucoup{VK_SPACE}pour{VK_SPACE}votre{VK_SPACE}offre{VK_SPACE}de{VK_SPACE}mission.
    {ENTER 2}
    Je{VK_SPACE}suis{VK_SPACE}disponible{VK_SPACE}tout{VK_SPACE}de{VK_SPACE}suite{VK_SPACE}pour{VK_SPACE}
    analyser{VK_SPACE}le{VK_SPACE}cahier{VK_SPACE}des{VK_SPACE}charges{VK_SPACE}de{VK_SPACE}votre{VK_SPACE}
    projet{VK_SPACE}afin{VK_SPACE}de{VK_SPACE}parvenir{VK_SPACE}à{VK_SPACE}répondre{VK_SPACE}parfaitement{VK_SPACE}
    à{VK_SPACE}vos{VK_SPACE}attentes{VK_SPACE}s'il{VK_SPACE}vous{VK_SPACE}plaît.
    {ENTER 2}
    Très{VK_SPACE}bonne{VK_SPACE}journée{VK_SPACE}à{VK_SPACE}vous,
    {ENTER 2}
    Mr{VK_SPACE}{VK_SPACE}
    {ENTER}
    Président{VK_SPACE}de{VK_SPACE}la{VK_SPACE}société{VK_SPACE}Holomorphe
    {ENTER}
    Ingénieur{VK_SPACE}généraliste{VK_SPACE}diplômé{VK_SPACE}à{VK_SPACE}l'Ecole{VK_SPACE}Supérieur{VK_SPACE}
    d'Ingénieurs{VK_SPACE}Léonard{VK_SPACE}de{VK_SPACE}Vinci{VK_SPACE}à{VK_SPACE}Paris{VK_SPACE}La{VK_SPACE}Défense
    {ENTER}
    Adresse{VK_SPACE}du{VK_SPACE}siège{VK_SPACE}social:{VK_SPACE}31{VK_SPACE}Avenue{VK_SPACE}de{VK_SPACE}
    Ségur{VK_SPACE}75007{VK_SPACE}Paris
    {ENTER}
    SIRET:{VK_SPACE}https://www.societe.com/societe/holomorphe-883632556.html
    {ENTER}
    Téléphone:{VK_SPACE}
    {ENTER}
    Site{VK_SPACE}internet:{VK_SPACE}https://holomorphe.com
    {ENTER}
    Malt:{VK_SPACE}https://www.malt.fr/profile/jasonaloyau
    {ENTER}
    Github:{VK_SPACE}https://github.com/Jay4C
            """)

            time.sleep(4)

            pywinauto.keyboard.send_keys("{VK_TAB}")

            time.sleep(4)

            # envoyer ma candidature
            pywinauto.keyboard.send_keys('{ENTER}')

            time.sleep(7)

            # type on the url bar 2 times
            pywinauto.mouse.click(button="left", coords=(820, 50))
            time.sleep(2)
            pywinauto.mouse.click(button="left", coords=(820, 50))

            time.sleep(4)

            # erase the phrase (#postuler)
            pywinauto.keyboard.send_keys('{BACKSPACE 9}')

            time.sleep(4)

            # refresh the page
            pywinauto.keyboard.send_keys('{ENTER}')

            time.sleep(4)

            # Je me déconnecte
            pywinauto.mouse.click(button="left", coords=(1200, 230))

            time.sleep(4)

            # Close the browser
            pywinauto.keyboard.send_keys('%{F4}')

            time.sleep(5)

    def test_up_from_the_bottom(self):
        print("test_up_from_the_bottom")

        app = Application(backend="uia")

        time.sleep(3)

        # Ouvrir l'application CCleaner
        app.start("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")

        time.sleep(3)

        pywinauto.keyboard.send_keys("https://www.airjob.fr/annonce/consultant-scrum-master-confirme-h-f")

        time.sleep(3)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        pywinauto.keyboard.send_keys('{DOWN 20}')

        time.sleep(3)

        pywinauto.keyboard.send_keys('{PGUP 7}')

    def test_connect_to_my_account_from_several_ads_from_one_result_page(self):
        app = Application(backend="uia")

        urls_ad = [
            ""
        ]

        for url_ad in urls_ad:
            print(url_ad)

            time.sleep(3)

            # Ouvrir l'application CCleaner
            app.start("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")

            time.sleep(6)

            pywinauto.keyboard.send_keys(url_ad)

            time.sleep(3)

            # Press the 'Enter' button
            pywinauto.keyboard.send_keys('{ENTER}')

            time.sleep(6)

            pywinauto.mouse.click(button="left", coords=(230, 460))

            time.sleep(3)

            pywinauto.mouse.click(button="left", coords=(500, 305))

            time.sleep(3)

            pywinauto.keyboard.send_keys(".@holomorphe.com")

            time.sleep(3)

            pywinauto.keyboard.send_keys("{VK_TAB}")

            time.sleep(3)

            pywinauto.keyboard.send_keys("")

            time.sleep(3)

            pywinauto.keyboard.send_keys("{VK_TAB 2}")

            time.sleep(3)

            pywinauto.keyboard.send_keys('{ENTER}')

            time.sleep(6)

            # click on Postuler
            pywinauto.mouse.click(button="left", coords=(230, 460))

            time.sleep(4)

            # click on CV
            pywinauto.mouse.click(button="left", coords=(900, 180))

            time.sleep(4)

            # select the file
            pywinauto.mouse.click(button="left", coords=(340, 50))
            time.sleep(3)
            pywinauto.keyboard.send_keys("C:\\Users\\DELL\\Documents")
            time.sleep(3)
            pywinauto.keyboard.send_keys('{ENTER}')
            time.sleep(3)
            pywinauto.mouse.click(button="left", coords=(300, 230))
            time.sleep(3)
            pywinauto.keyboard.send_keys('{ENTER}')

            time.sleep(4)

            # select the input for the message
            pywinauto.mouse.click(button="left", coords=(860, 260))

            time.sleep(4)

            # write the message
            pywinauto.keyboard.send_keys("""
    Bonjour,
    {ENTER 2}
    Merci{VK_SPACE}beaucoup{VK_SPACE}pour{VK_SPACE}votre{VK_SPACE}offre{VK_SPACE}de{VK_SPACE}mission.
    {ENTER 2}
    Je{VK_SPACE}suis{VK_SPACE}disponible{VK_SPACE}tout{VK_SPACE}de{VK_SPACE}suite{VK_SPACE}pour{VK_SPACE}
    analyser{VK_SPACE}le{VK_SPACE}cahier{VK_SPACE}des{VK_SPACE}charges{VK_SPACE}de{VK_SPACE}votre{VK_SPACE}
    projet{VK_SPACE}afin{VK_SPACE}de{VK_SPACE}parvenir{VK_SPACE}à{VK_SPACE}répondre{VK_SPACE}parfaitement{VK_SPACE}
    à{VK_SPACE}vos{VK_SPACE}attentes{VK_SPACE}s'il{VK_SPACE}vous{VK_SPACE}plaît.
    {ENTER 2}
    Très{VK_SPACE}bonne{VK_SPACE}journée{VK_SPACE}à{VK_SPACE}vous,
    {ENTER 2}
    Mr{VK_SPACE}{VK_SPACE}
    {ENTER}
    Président{VK_SPACE}de{VK_SPACE}la{VK_SPACE}société{VK_SPACE}Holomorphe
    {ENTER}
    Ingénieur{VK_SPACE}généraliste{VK_SPACE}diplômé{VK_SPACE}à{VK_SPACE}l'Ecole{VK_SPACE}Supérieur{VK_SPACE}
    d'Ingénieurs{VK_SPACE}Léonard{VK_SPACE}de{VK_SPACE}Vinci{VK_SPACE}à{VK_SPACE}Paris{VK_SPACE}La{VK_SPACE}Défense
    {ENTER}
    Adresse{VK_SPACE}du{VK_SPACE}siège{VK_SPACE}social:{VK_SPACE}31{VK_SPACE}Avenue{VK_SPACE}de{VK_SPACE}
    Ségur{VK_SPACE}75007{VK_SPACE}Paris
    {ENTER}
    SIRET:{VK_SPACE}https://www.societe.com/societe/holomorphe-883632556.html
    {ENTER}
    Téléphone:{VK_SPACE}
    {ENTER}
    Site{VK_SPACE}internet:{VK_SPACE}https://holomorphe.com
    {ENTER}
    Malt:{VK_SPACE}https://www.malt.fr/profile/jasonaloyau
    {ENTER}
    Github:{VK_SPACE}https://github.com/Jay4C
            """)

            time.sleep(4)

            pywinauto.keyboard.send_keys("{VK_TAB}")

            time.sleep(4)

            # envoyer ma candidature
            pywinauto.keyboard.send_keys('{ENTER}')

            time.sleep(7)

            # type on the url bar 2 times
            pywinauto.mouse.click(button="left", coords=(820, 50))
            time.sleep(2)
            pywinauto.mouse.click(button="left", coords=(820, 50))

            time.sleep(4)

            # erase the phrase (#postuler)
            pywinauto.keyboard.send_keys('{BACKSPACE 9}')

            time.sleep(4)

            # refresh the page
            pywinauto.keyboard.send_keys('{ENTER}')

            time.sleep(4)

            # Je me déconnecte
            pywinauto.mouse.click(button="left", coords=(1200, 230))

            time.sleep(4)

            # Close the browser
            pywinauto.keyboard.send_keys('%{F4}')

            time.sleep(5)

    def test_extract_all_pages_from_one_result_page(self):
        print("test_extract_all_pages_from_one_result_page")

        url_result_page = "https://www.airjob.fr/recherche/keywords:d%25C3%25A9veloppeur,,l:10,p:2"

        # Request the content of a page from the url
        html = requests.get(url_result_page)

        time.sleep(3)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.content, 'html.parser')

        if soup.find('div', {'class': 'un-resultat'}) is not None:
            print("offres ok")

            all_offre = soup.find_all('div', {'class': 'un-resultat'})

            i = 1

            for offre in all_offre:
                print("link " + str(i) + " : https://www.airjob.fr" + str(offre
                                                                           .find('a', {'class': 'resultat-titre'})
                                                                           .get('href')))

                i += 1
        else:
            print("no offres")

    def test_extract_all_pages_from_all_result_page(self):
        print("test_extract_all_pages_from_all_result_page")

        i = 1

        for x in range(2, 148):
            print("result page : " + str(x))

            url_result_page = "https://www.airjob.fr/recherche/keywords:d%25C3%25A9veloppeur,,l:10,p:" + str(x)

            # Request the content of a page from the url
            html = requests.get(url_result_page)

            time.sleep(3)

            # Parse the content of html_doc
            soup = BeautifulSoup(html.content, 'html.parser')

            if soup.find('div', {'class': 'un-resultat'}) is not None:
                print("offres ok")

                all_offre = soup.find_all('div', {'class': 'un-resultat'})

                for offre in all_offre:
                    print("link " + str(i) + " : https://www.airjob.fr" + str(offre
                                                                              .find('a', {'class': 'resultat-titre'})
                                                                              .get('href')))

                    i += 1
            else:
                print("no offres")

    def test_connect_to_my_account_from_several_ads_from_all_result_page(self):
        print("test_connect_to_my_account_from_several_ads_from_all_result_page")

        app = Application(backend="uia")

        i = 1

        # 149
        for x in range(1, 3):
            print("result page : " + str(x))

            url_result_page = "https://www.airjob.fr/recherche/keywords:d%25C3%25A9veloppeur,,l:10,p:" + str(x)

            # Request the content of a page from the url
            html = requests.get(url_result_page)

            time.sleep(3)

            # Parse the content of html_doc
            soup = BeautifulSoup(html.content, 'html.parser')

            if soup.find('div', {'class': 'un-resultat'}) is not None:
                print("offres ok")

                all_offre = soup.find_all('div', {'class': 'un-resultat'})

                for offre in all_offre:
                    print("link " + str(i) + " : https://www.airjob.fr" + str(offre
                                                                              .find('a', {'class': 'resultat-titre'})
                                                                              .get('href')))

                    i += 1

                    url_ad = "https://www.airjob.fr" + str(offre.find('a', {'class': 'resultat-titre'}).get('href'))

                    time.sleep(3)

                    app.start("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")

                    time.sleep(6)

                    pywinauto.keyboard.send_keys(url_ad)

                    time.sleep(3)

                    # Press the 'Enter' button
                    pywinauto.keyboard.send_keys('{ENTER}')

                    time.sleep(6)

                    pywinauto.mouse.click(button="left", coords=(230, 460))

                    time.sleep(3)

                    pywinauto.mouse.click(button="left", coords=(500, 305))

                    time.sleep(3)

                    pywinauto.keyboard.send_keys(".@holomorphe.com")

                    time.sleep(3)

                    pywinauto.keyboard.send_keys("{VK_TAB}")

                    time.sleep(3)

                    pywinauto.keyboard.send_keys("")

                    time.sleep(3)

                    pywinauto.keyboard.send_keys("{VK_TAB 2}")

                    time.sleep(3)

                    pywinauto.keyboard.send_keys('{ENTER}')

                    time.sleep(6)

                    # click on Postuler
                    pywinauto.mouse.click(button="left", coords=(230, 460))

                    time.sleep(4)

                    # click on CV
                    pywinauto.mouse.click(button="left", coords=(900, 180))

                    time.sleep(4)

                    # select the file
                    pywinauto.mouse.click(button="left", coords=(340, 50))
                    time.sleep(3)
                    pywinauto.keyboard.send_keys("C:\\Users\\DELL\\Documents")
                    time.sleep(3)
                    pywinauto.keyboard.send_keys('{ENTER}')
                    time.sleep(3)
                    pywinauto.mouse.click(button="left", coords=(300, 165))
                    time.sleep(3)

                    pywinauto.keyboard.send_keys('{ENTER}')

                    time.sleep(4)

                    # select the input for the message
                    pywinauto.mouse.click(button="left", coords=(860, 260))

                    time.sleep(4)

                    # write the message
                    pywinauto.keyboard.send_keys("""
                    Bonjour,
                    {ENTER 2}
                    Merci{VK_SPACE}beaucoup{VK_SPACE}pour{VK_SPACE}votre{VK_SPACE}offre{VK_SPACE}de{VK_SPACE}mission.
                    {ENTER 2}
                    Je{VK_SPACE}vous{VK_SPACE}prie{VK_SPACE}de{VK_SPACE}bien{VK_SPACE}vouloir{VK_SPACE}recevoir
                    {VK_SPACE}mon{VK_SPACE}CV{VK_SPACE}en{VK_SPACE}pièce{VK_SPACE}jointe.
                    {ENTER 2}
                    Très{VK_SPACE}bonne{VK_SPACE}journée{VK_SPACE}à{VK_SPACE}vous,
                    {ENTER 2}
                    Mr{VK_SPACE}{VK_SPACE}
                    {ENTER}
                    Malt:{VK_SPACE}https://www.malt.fr/profile/jasonaloyau
                    {ENTER}
                    Github:{VK_SPACE}https://github.com/Jay4C
                            """)

                    time.sleep(4)

                    pywinauto.keyboard.send_keys("{VK_TAB}")

                    time.sleep(4)

                    # envoyer ma candidature
                    pywinauto.keyboard.send_keys('{ENTER}')

                    time.sleep(7)

                    # revenir tout en haut de la page
                    pywinauto.keyboard.send_keys('{PGUP 7}')

                    time.sleep(4)

                    # type on the url bar 2 times
                    pywinauto.mouse.click(button="left", coords=(820, 50))
                    time.sleep(2)
                    pywinauto.mouse.click(button="left", coords=(820, 50))

                    time.sleep(4)

                    # erase the phrase (#postuler)
                    pywinauto.keyboard.send_keys('{BACKSPACE 9}')

                    time.sleep(4)

                    # refresh the page
                    pywinauto.keyboard.send_keys('{ENTER}')

                    time.sleep(4)

                    # Je me déconnecte
                    pywinauto.mouse.click(button="left", coords=(1200, 230))

                    time.sleep(4)

                    # Close the browser
                    pywinauto.keyboard.send_keys('%{F4}')

                    time.sleep(5)
            else:
                print("no offres")


if __name__ == '__main__':
    unittest.main()
