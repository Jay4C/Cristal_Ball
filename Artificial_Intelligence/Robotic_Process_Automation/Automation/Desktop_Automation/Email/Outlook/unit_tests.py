import codecs
import unittest
import time
import requests
from bs4 import BeautifulSoup
from pywinauto.application import Application
import pywinauto.keyboard
import pywinauto.mouse
import pymysql.cursors


class UnitTestsDesktopAutomationOutlook(unittest.TestCase):
    def test_connect(self):
        username = ""

        password = ""

        time.sleep(10)

        app = Application(backend="uia")

        # Ouvrir un navigateur web
        app.start("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")

        time.sleep(10)

        # Open the Outlook Application
        pywinauto.keyboard.send_keys("https://outlook.live.com/owa/")

        time.sleep(10)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(10)

        # Click on the 'Connexion' button
        pywinauto.mouse.click(button='left', coords=(1111, 100))

        time.sleep(10)

        # Type the email address
        pywinauto.keyboard.send_keys(username)

        time.sleep(10)

        # Type the Tab in 5 times
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(10)

        # Type the password
        pywinauto.keyboard.send_keys(password)

        time.sleep(10)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(10)

    def test_extract_email_of_the_sender(self):
        app = Application(backend="uia")

        # Ouvrir l'application Google Chrome
        app.start("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")

        time.sleep(5)

        # Open the Outlook Application
        pywinauto.keyboard.send_keys("https://outlook.live.com/owa/")

        time.sleep(5)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(5)

        # Click on the 'Connexion' button
        pywinauto.mouse.click(button='left', coords=(1250, 100))

        time.sleep(5)

        # Type the email address
        pywinauto.keyboard.send_keys('.@outlook.fr')

        time.sleep(5)

        # Type the Tab in 5 times
        pywinauto.keyboard.send_keys('{VK_TAB 5}')

        time.sleep(5)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(5)

        # Type the password
        pywinauto.keyboard.send_keys('')

        time.sleep(5)

        # Type the Tab in 3 times
        pywinauto.keyboard.send_keys('{VK_TAB 3}')

        time.sleep(5)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(10)

        for x in range(150):
            # 1 - Click on the first message
            pywinauto.mouse.click(button='left', coords=(450, 240))

            time.sleep(5)

            # pywinauto.mouse.click(button='left', coords=(400, 260))
            # time.sleep(3)

            # 2 - Click on the sender's email
            # pywinauto.mouse.click(button='left', coords=(450, 280))
            pywinauto.mouse.move(coords=(445, 275))

            time.sleep(15)

            # 3 - Click on the "Copy" button to copy the email
            pywinauto.mouse.click(button='left', coords=(700, 510))

            time.sleep(5)

            # 4 - Click on the Excel file icon to display the Excel file
            pywinauto.mouse.click(button='left', coords=(600, 870))

            time.sleep(5)

            # 5 - Click on the "Ctrl+V" buttons to paste the email
            pywinauto.keyboard.send_keys('^v')

            time.sleep(5)

            # 6 - Press the 'Enter' button
            pywinauto.keyboard.send_keys('{ENTER}')

            time.sleep(5)

            # 7 - Click on the Google Chrome icon to display Google Chrome
            pywinauto.mouse.click(button='left', coords=(550, 870))

            time.sleep(5)

            # 8 - Delete the message by clicking on the "Delete" button
            pywinauto.mouse.click(button='left', coords=(350, 140))

            time.sleep(10)

    def test_send_one_email(self):
        app = Application(backend="uia")

        # Ouvrir l'application Google Chrome
        app.start("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")

        time.sleep(5)

        # Open the Outlook Application
        pywinauto.keyboard.send_keys("https://outlook.live.com/owa/")

        time.sleep(5)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(5)

        # Click on the 'Connexion' button
        pywinauto.mouse.click(button='left', coords=(1111, 100))

        time.sleep(5)

        # Type the email address
        pywinauto.keyboard.send_keys('.@outlook.fr')

        time.sleep(5)

        # Type the Tab in 5 times
        pywinauto.keyboard.send_keys('{VK_TAB 5}')

        time.sleep(5)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(5)

        # Type the password
        pywinauto.keyboard.send_keys('')

        time.sleep(5)

        # Type the Tab in 3 times
        pywinauto.keyboard.send_keys('{VK_TAB 3}')

        time.sleep(5)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(15)

        # Click on the 'Nouveau courrier' button
        pywinauto.mouse.click(button='left', coords=(100, 140))

        time.sleep(5)

        # Click on the 'À' bar
        pywinauto.mouse.click(button='left', coords=(420, 200))

        time.sleep(5)

        # Type the mail's receiver
        pywinauto.keyboard.send_keys('@gmail.com')

        time.sleep(5)

        # Click on the 'Subject' bar
        pywinauto.mouse.click(button='left', coords=(360, 255))

        time.sleep(5)

        # Type the subject
        pywinauto.keyboard.send_keys('Hello ')

        time.sleep(5)

        # Click on the 'Message' bar
        pywinauto.mouse.click(button='left', coords=(360, 310))

        time.sleep(5)

        # Type the message
        pywinauto.keyboard.send_keys('Hello ')

        time.sleep(5)

        # Click on the 'Envoyer' button
        pywinauto.mouse.click(button='left', coords=(390, 140))

        time.sleep(10)

        # Click on the 'Profile' button
        pywinauto.mouse.click(button='left', coords=(1340, 95))

        time.sleep(5)

        # Click on the 'Se deconnecter' button
        pywinauto.mouse.click(button='left', coords=(1210, 295))

        time.sleep(5)

        # Click on the 'Fermer' button of Google Chrome
        pywinauto.mouse.click(button='left', coords=(1345, 10))

        time.sleep(5)

    def test_send_several_emails_from_a_list(self):
        app = Application(backend="uia")

        # Ouvrir l'application Google Chrome
        app.start("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")

        time.sleep(5)

        # Open the Outlook Application
        pywinauto.keyboard.send_keys("https://outlook.live.com/owa/")

        time.sleep(5)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(5)

        # Click on the 'Connexion' button
        pywinauto.mouse.click(button='left', coords=(1111, 100))

        time.sleep(5)

        # Type the email address
        pywinauto.keyboard.send_keys('.@outlook.fr')

        time.sleep(5)

        # Type the Tab in 5 times
        pywinauto.keyboard.send_keys('{VK_TAB 5}')

        time.sleep(5)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(5)

        # Type the password
        pywinauto.keyboard.send_keys('')

        time.sleep(5)

        # Type the Tab in 3 times
        pywinauto.keyboard.send_keys('{VK_TAB 3}')

        time.sleep(5)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(15)

        emails = [
            '@gmail.com',
            '..@gmail.com'
        ]

        for email in emails:
            # Click on the 'Nouveau courrier' button
            pywinauto.mouse.click(button='left', coords=(100, 140))

            time.sleep(5)

            # Click on the 'À' bar
            pywinauto.mouse.click(button='left', coords=(420, 200))

            time.sleep(5)

            # Type the mail's receiver
            pywinauto.keyboard.send_keys(email)

            time.sleep(5)

            # Click on the 'Subject' bar
            pywinauto.mouse.click(button='left', coords=(360, 255))

            time.sleep(5)

            # Type the subject
            pywinauto.keyboard.send_keys('Hello{VK_SPACE}')

            time.sleep(5)

            # Click on the 'Message' bar
            pywinauto.mouse.click(button='left', coords=(360, 310))

            time.sleep(5)

            # Type the message
            pywinauto.keyboard.send_keys('Hello{VK_SPACE}')

            time.sleep(5)

            # Click on the 'Envoyer' button
            pywinauto.mouse.click(button='left', coords=(390, 140))

            time.sleep(5)

        time.sleep(10)

        # Click on the 'Profile' button
        pywinauto.mouse.click(button='left', coords=(1340, 95))

        time.sleep(5)

        # Click on the 'Se deconnecter' button
        pywinauto.mouse.click(button='left', coords=(1210, 295))

        time.sleep(5)

        # Click on the 'Fermer' button of Google Chrome
        pywinauto.mouse.click(button='left', coords=(1345, 10))

        time.sleep(5)

    def test_display_emails_from_contacts_professionnel_database(self):
        id_activity = 19  # agence interim
        id_city = 2  # New-York

        emails = []

        connection = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            password='',
            db='contacts_professionnels',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )

        try:
            with connection.cursor() as cursor:
                try:
                    sql = "SELECT `email` FROM `emails` WHERE id_activite=%s AND id_capitale_du_monde=%s"
                    cursor.execute(sql, (id_activity, id_city))
                    results = cursor.fetchall()

                    for result in results:
                        emails.append(result.get('email'))

                    connection.close()

                except:
                    print("There is an error")

                for email in emails:
                    print("email : " + str(email))

        finally:
            print('done')

    def test_send_several_emails_from_a_database(self):
        app = Application(backend="uia")

        # Ouvrir l'application Google Chrome
        app.start("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")

        time.sleep(5)

        # Open the Outlook Application
        pywinauto.keyboard.send_keys("https://outlook.live.com/owa/")

        time.sleep(5)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(5)

        # Click on the 'Connexion' button
        pywinauto.mouse.click(button='left', coords=(1111, 100))

        time.sleep(5)

        # Type the email address
        pywinauto.keyboard.send_keys('.@outlook.fr')

        time.sleep(5)

        # Type the Tab in 5 times
        pywinauto.keyboard.send_keys('{VK_TAB 5}')

        time.sleep(5)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(5)

        # Type the password
        pywinauto.keyboard.send_keys('')

        time.sleep(5)

        # Type the Tab in 3 times
        pywinauto.keyboard.send_keys('{VK_TAB 3}')

        time.sleep(5)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(15)

        id_activity = 19  # agence interim
        id_city = 2  # New-York

        emails = []

        connection = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            password='',
            db='contacts_professionnels',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )

        try:
            with connection.cursor() as cursor:
                try:
                    sql = "SELECT `email` FROM `emails` WHERE id_activite=%s AND id_capitale_du_monde=%s"
                    cursor.execute(sql, (id_activity, id_city))
                    results = cursor.fetchall()

                    for result in results:
                        emails.append(result.get('email'))

                    connection.close()
                except Exception as e:
                    print("Error : " + str(e))

            for email in emails:
                if email not in (
                        'x'
                ):
                    # Click on the 'Nouveau courrier' button
                    pywinauto.mouse.click(button='left', coords=(100, 140))

                    time.sleep(5)

                    # Click on the 'À' bar
                    pywinauto.mouse.click(button='left', coords=(420, 200))

                    time.sleep(5)

                    # Type the mail's receiver
                    pywinauto.keyboard.send_keys(email)

                    time.sleep(5)

                    # Click on the 'Subject' bar
                    pywinauto.mouse.click(button='left', coords=(360, 255))

                    time.sleep(5)

                    # Type the subject
                    pywinauto.keyboard.send_keys(
                        'Free{VK_SPACE}energy{VK_SPACE}devices{VK_SPACE}for{VK_SPACE}producing{VK_SPACE}electricity')

                    time.sleep(5)

                    # Click on the 'Message' bar
                    pywinauto.mouse.click(button='left', coords=(360, 310))

                    time.sleep(5)

                    # Type the message
                    myMessage = (
                            "Hello," +
                            "{ENTER 2}" +
                            "Find{VK_SPACE}some{VK_SPACE}documents{VK_SPACE}about" +
                            "{VK_SPACE}free{VK_SPACE}energy{VK_SPACE}devices" +
                            "{VK_SPACE}for{VK_SPACE}producing{VK_SPACE}electricity{VK_SPACE}to{VK_SPACE}the" +
                            "{VK_SPACE}following" +
                            "{VK_SPACE}link{VK_SPACE}https://github.com/Jay4C/Free-energy-devices" +
                            "{ENTER 2}" +
                            "Kind{VK_SPACE}regards," +
                            "{ENTER 2}" +
                            "Jason{VK_SPACE}ALOYAU" +
                            "{ENTER 2}" +
                            "Phone{VK_SPACE}number{VK_SPACE}:{VK_SPACE}"
                    )
                    pywinauto.keyboard.send_keys(myMessage)

                    time.sleep(5)

                    # Click on the 'Envoyer' button
                    pywinauto.mouse.click(button='left', coords=(390, 140))

                    time.sleep(5)

        finally:
            print('done')

            time.sleep(10)

            # Click on the 'Profile' button
            pywinauto.mouse.click(button='left', coords=(1340, 95))

            time.sleep(5)

            # Click on the 'Se deconnecter' button
            pywinauto.mouse.click(button='left', coords=(1210, 295))

            time.sleep(5)

            # Click on the 'Fermer' button of Google Chrome
            pywinauto.mouse.click(button='left', coords=(1345, 10))

            time.sleep(5)

    def test_send_emails_from_phone_books_for_universites_de_la_reunion(self):
        phone_books = [
            "https://annuaire.univ-reunion.fr/?structure=917"
        ]

        emails = []

        for phone_book in phone_books:
            try:
                url_phone_book = phone_book

                # Request the content of a page from the url
                html = requests.get(url_phone_book)

                # Parse the content of html
                soup = BeautifulSoup(html.content, 'html.parser')

                try:
                    if soup.find("table", {"class": "results"}) is not None:
                        try:
                            if soup.find("table", {"class": "results"}).find("tr") is not None:
                                all_tr = soup.find("table", {"class": "results"}).find_all("tr")
                                for tr in all_tr:
                                    try:
                                        if tr.find('td') is not None:
                                            td_email = tr.find_all('td')[1].text \
                                                .replace('document.write(rot13ToMail("', '') \
                                                .replace('"));', '') \
                                                .lower()

                                            if td_email != "information manquante":
                                                emails.append(codecs.encode(td_email, 'rot_13'))
                                        else:
                                            print("no tag td")
                                    except Exception as e:
                                        print('exception tag td : ' + str(e))
                            else:
                                print("no tag tr")
                        except Exception as e:
                            print('exception tag tr : ' + str(e))
                    else:
                        print("no tag table")
                except Exception as e:
                    print("Exception table tag : " + str(e))
            except Exception as e:
                print("url_phone_book : " + str(e))

        app = Application(backend="uia")

        # Ouvrir l'application Google Chrome
        app.start("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")

        time.sleep(5)

        # Open the Outlook Application
        pywinauto.keyboard.send_keys("https://outlook.live.com/owa/")

        time.sleep(5)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(5)

        # Click on the 'Connexion' button
        pywinauto.mouse.click(button='left', coords=(1111, 100))

        time.sleep(5)

        # Type the email address
        pywinauto.keyboard.send_keys('.@outlook.fr')

        time.sleep(5)

        # Type the Tab in 5 times
        pywinauto.keyboard.send_keys('{VK_TAB 5}')

        time.sleep(5)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(5)

        # Type the password
        pywinauto.keyboard.send_keys('')

        time.sleep(5)

        # Type the Tab in 3 times
        pywinauto.keyboard.send_keys('{VK_TAB 3}')

        time.sleep(5)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(15)

        for email in emails:
            if email not in [
                ".@univ-reunion.fr",
                ".@ac-reunion.fr"
            ]:
                # Click on the 'Nouveau courrier' button
                pywinauto.mouse.click(button='left', coords=(100, 140))

                time.sleep(5)

                # Click on the 'À' bar
                pywinauto.mouse.click(button='left', coords=(420, 200))

                time.sleep(5)

                # Type the mail's receiver
                pywinauto.keyboard.send_keys(email)

                time.sleep(5)

                # Click on the 'Subject' bar
                pywinauto.mouse.click(button='left', coords=(360, 255))

                time.sleep(5)

                # Type the subject
                pywinauto.keyboard.send_keys("Demande{VK_SPACE}d'informations{VK_SPACE}au{VK_SPACE}"
                                             "sujet{VK_SPACE}d'une{VK_SPACE}sous-traitance{VK_SPACE}"
                                             "de{VK_SPACE}recherche{VK_SPACE}et{VK_SPACE}développement")

                time.sleep(5)

                # Click on the 'Message' bar
                pywinauto.mouse.click(button='left', coords=(360, 310))

                time.sleep(5)

                # Type the message
                pywinauto.keyboard.send_keys(
                    """
                    Bonjour,
                    {ENTER 2}
                    Vu{VK_SPACE}le{VK_SPACE}Code{VK_SPACE}de{VK_SPACE}la{VK_SPACE}recherche,
                    {ENTER}
                    Vu{VK_SPACE}l'article{VK_SPACE}L100-4{VK_SPACE}du{VK_SPACE}Code{VK_SPACE}de{VK_SPACE}
                    l'énergie{VK_SPACE}concernant{VK_SPACE}la{VK_SPACE}politique{VK_SPACE}énergétique{VK_SPACE}nationale,
                    {ENTER}
                    Vu{VK_SPACE}l'article{VK_SPACE}244{VK_SPACE}quater{VK_SPACE}B{VK_SPACE}du{VK_SPACE}Code{VK_SPACE}
                    général{VK_SPACE}des{VK_SPACE}impôts{VK_SPACE}concernant{VK_SPACE}le{VK_SPACE}crédit{VK_SPACE}
                    d'impôt{VK_SPACE}pour{VK_SPACE}dépenses{VK_SPACE}de{VK_SPACE}recherche{VK_SPACE}effectuées
                    {VK_SPACE}par{VK_SPACE}les{VK_SPACE}entreprises{VK_SPACE}industrielles{VK_SPACE}et
                    {VK_SPACE}commerciales{VK_SPACE}ou{VK_SPACE}agricoles ,
                    {ENTER}
                    Vu{VK_SPACE}le{VK_SPACE}Code{VK_SPACE}de{VK_SPACE}la{VK_SPACE}propriété{VK_SPACE}intellectuelle,
                    {ENTER 2}
                    Tout{VK_SPACE}d'abord,{VK_SPACE}la{VK_SPACE}société{VK_SPACE}HOLOMORPHE{VK_SPACE}est{VK_SPACE}
                    en{VK_SPACE}phase{VK_SPACE}d'immatriculation{VK_SPACE}dont{VK_SPACE}la{VK_SPACE}vocation
                    {VK_SPACE}première{VK_SPACE}est{VK_SPACE}de{VK_SPACE}commercialiser{VK_SPACE}des{VK_SPACE}
                    produits{VK_SPACE}chimiques{VK_SPACE}tels{VK_SPACE}que{VK_SPACE}le{VK_SPACE}dihydrogène{VK_SPACE}
                    et{VK_SPACE}l'huile{VK_SPACE}de{VK_SPACE}pyrolyse{VK_SPACE}à{VK_SPACE}partir{VK_SPACE}de{VK_SPACE}
                    déchets{VK_SPACE}plastiques.
                    {ENTER 2}
                    Dans{VK_SPACE}le{VK_SPACE}cadre{VK_SPACE}de{VK_SPACE}ses{VK_SPACE}futures{VK_SPACE}recherches
                    {VK_SPACE}et{VK_SPACE}développements{VK_SPACE}scientifiques{VK_SPACE}et{VK_SPACE}
                    technologiques{VK_SPACE}pour{VK_SPACE}l'innovation,{VK_SPACE}j'aurais{VK_SPACE}quelques{VK_SPACE}
                    questions{VK_SPACE}concernant{VK_SPACE}l'encadrement{VK_SPACE}et{VK_SPACE}la{VK_SPACE}mise{VK_SPACE}
                    en{VK_SPACE}place{VK_SPACE}des{VK_SPACE}dépenses{VK_SPACE}de{VK_SPACE}recherche{VK_SPACE}dans
                    {VK_SPACE}votre{VK_SPACE}établissement{VK_SPACE}par{VK_SPACE}une{VK_SPACE}entreprise
                    {VK_SPACE}commerciale.
                    {ENTER 2}
                    Mes{VK_SPACE}questions{VK_SPACE}sont{VK_SPACE}les{VK_SPACE}suivantes.
                    {ENTER 2}
                    -{VK_SPACE}Est-ce{VK_SPACE}que{VK_SPACE}votre{VK_SPACE}établissement{VK_SPACE}met{VK_SPACE}en
                    {VK_SPACE}place{VK_SPACE}un{VK_SPACE}contrat{VK_SPACE}de{VK_SPACE}sous-traitance{VK_SPACE}de
                    {VK_SPACE}recherche{VK_SPACE}et{VK_SPACE}développement{VK_SPACE}s'il{VK_SPACE}vous{VK_SPACE}plaît
                    {VK_SPACE}?
                    {ENTER 2}
                    -{VK_SPACE}Est-ce{VK_SPACE}que{VK_SPACE}votre{VK_SPACE}établissement{VK_SPACE}possède{VK_SPACE}
                    des{VK_SPACE}espaces{VK_SPACE}de{VK_SPACE}stockage{VK_SPACE}pour{VK_SPACE}abriter{VK_SPACE}les
                    {VK_SPACE}inventions,{VK_SPACE}les{VK_SPACE}prototypes,{VK_SPACE}les{VK_SPACE}outils{VK_SPACE}et
                    {VK_SPACE}les{VK_SPACE}travaux{VK_SPACE}contre{VK_SPACE}le{VK_SPACE}vol{VK_SPACE}et{VK_SPACE}le
                    {VK_SPACE}sabotage{VK_SPACE}s'il{VK_SPACE}vous{VK_SPACE}plaît{VK_SPACE}?
                    {ENTER 2}
                    -{VK_SPACE}Est-ce{VK_SPACE}que{VK_SPACE}votre{VK_SPACE}établissement{VK_SPACE}restreint{VK_SPACE}
                    le{VK_SPACE}volume{VK_SPACE}et{VK_SPACE}la{VK_SPACE}masse{VK_SPACE}des{VK_SPACE}inventions,{VK_SPACE}
                    des{VK_SPACE}prototypes{VK_SPACE}et{VK_SPACE}des{VK_SPACE}outils{VK_SPACE}contre{VK_SPACE}
                    l'encombrement{VK_SPACE}et{VK_SPACE}le{VK_SPACE}poids{VK_SPACE}excessif{VK_SPACE}s'il{VK_SPACE}vous
                    {VK_SPACE}plaît{VK_SPACE}?
                    {ENTER 2}
                    -{VK_SPACE}Est-ce{VK_SPACE}que{VK_SPACE}votre{VK_SPACE}établissement{VK_SPACE}facture{VK_SPACE}
                    l'entrepôt{VK_SPACE}des{VK_SPACE}inventions,{VK_SPACE}des{VK_SPACE}prototypes,{VK_SPACE}des{VK_SPACE}outils
                    {VK_SPACE}et{VK_SPACE}des{VK_SPACE}travaux{VK_SPACE}à{VK_SPACE}l'entreprise{VK_SPACE}commerciale
                    {VK_SPACE}finançant{VK_SPACE}les{VK_SPACE}dépenses{VK_SPACE}de{VK_SPACE}recherches{VK_SPACE}s'il
                    {VK_SPACE}vous{VK_SPACE}plaît{VK_SPACE}?
                    {ENTER 2}
                    -{VK_SPACE}Comment{VK_SPACE}certifiez-vous{VK_SPACE}les{VK_SPACE}dépenses{VK_SPACE}de{VK_SPACE}
                    recherche{VK_SPACE}d'une{VK_SPACE}entreprise{VK_SPACE}commerciale{VK_SPACE}dans{VK_SPACE}votre{VK_SPACE}
                    établissement{VK_SPACE}s'il{VK_SPACE}vous{VK_SPACE}plaît{VK_SPACE}?
                    {ENTER 2}
                    -{VK_SPACE}Est-ce{VK_SPACE}que{VK_SPACE}l'entreprise{VK_SPACE}commerciale{VK_SPACE}devra{VK_SPACE}
                    rémunérer{VK_SPACE}vos{VK_SPACE}personnels{VK_SPACE}de{VK_SPACE}recherches{VK_SPACE}chargées{VK_SPACE}
                    des{VK_SPACE}recherches{VK_SPACE}financées{VK_SPACE}par{VK_SPACE}l'entreprise{VK_SPACE}
                    commerciale{VK_SPACE}s'il{VK_SPACE}vous{VK_SPACE}plaît{VK_SPACE}?
                    {ENTER 2}
                    -{VK_SPACE}Est-ce{VK_SPACE}que{VK_SPACE}les{VK_SPACE}salariés{VK_SPACE}d'une{VK_SPACE}entreprise
                    {VK_SPACE}commerciale{VK_SPACE}peuvent{VK_SPACE}venir{VK_SPACE}en{VK_SPACE}renfort{VK_SPACE}dans
                    {VK_SPACE}votre{VK_SPACE}établissement{VK_SPACE}pour{VK_SPACE}accompagner{VK_SPACE}vos{VK_SPACE}
                    personnels{VK_SPACE}de{VK_SPACE}recherches{VK_SPACE}sur{VK_SPACE}les{VK_SPACE}recherches{VK_SPACE}
                    financées{VK_SPACE}par{VK_SPACE}l'entreprise{VK_SPACE}commerciale{VK_SPACE}s'il{VK_SPACE}vous
                    {VK_SPACE}plaît{VK_SPACE}?
                    {ENTER 2}
                    -{VK_SPACE}Est-ce{VK_SPACE}que{VK_SPACE}l'entreprise{VK_SPACE}commerciale{VK_SPACE}devra{VK_SPACE}
                    souscrire{VK_SPACE}à{VK_SPACE}une{VK_SPACE}assurance{VK_SPACE}responsabilité{VK_SPACE}civile{VK_SPACE}
                    professionnelle{VK_SPACE}dans{VK_SPACE}le{VK_SPACE}cadre{VK_SPACE}des{VK_SPACE}recherches{VK_SPACE}
                    effectuées{VK_SPACE}au{VK_SPACE}sein{VK_SPACE}de{VK_SPACE}votre{VK_SPACE}établissement{VK_SPACE}
                    financées{VK_SPACE}par{VK_SPACE}l'entreprise{VK_SPACE}commerciale{VK_SPACE}s'il{VK_SPACE}vous
                    {VK_SPACE}plaît{VK_SPACE}?
                    {ENTER 2}
                    -{VK_SPACE}Est-ce{VK_SPACE}que{VK_SPACE}les{VK_SPACE}recherches{VK_SPACE}effectuées{VK_SPACE}dans
                    {VK_SPACE}votre{VK_SPACE}établissement{VK_SPACE}financées{VK_SPACE}par{VK_SPACE}une{VK_SPACE}
                    entreprise{VK_SPACE}commerciale{VK_SPACE}entrent{VK_SPACE}dans{VK_SPACE}la{VK_SPACE}propriété
                    {VK_SPACE}intellectuelle{VK_SPACE}de{VK_SPACE}l'entreprise{VK_SPACE}commerciale{VK_SPACE}s'il
                    {VK_SPACE}vous{VK_SPACE}plaît{VK_SPACE}?
                    {ENTER 2}
                    -{VK_SPACE}Est-ce{VK_SPACE}que{VK_SPACE}votre{VK_SPACE}établissement{VK_SPACE}utilise{VK_SPACE}un
                    {VK_SPACE}diagramme{VK_SPACE}de{VK_SPACE}Gantt{VK_SPACE}pour{VK_SPACE}suivre{VK_SPACE}l'avancement
                    {VK_SPACE}des{VK_SPACE}recherches{VK_SPACE}dans{VK_SPACE}un{VK_SPACE}Cloud{VK_SPACE}privé{VK_SPACE}
                    dont{VK_SPACE}votre{VK_SPACE}établissement{VK_SPACE}possède{VK_SPACE}les{VK_SPACE}serveurs
                    {VK_SPACE}Cloud{VK_SPACE}sans{VK_SPACE}prestataires{VK_SPACE}de{VK_SPACE}services{VK_SPACE}
                    s'il{VK_SPACE}vous{VK_SPACE}plaît{VK_SPACE}?
                    {ENTER 2}
                    Dans{VK_SPACE}l'attente{VK_SPACE}de{VK_SPACE}votre{VK_SPACE}retour,{VK_SPACE}je{VK_SPACE}vous{VK_SPACE}
                    prie{VK_SPACE}de{VK_SPACE}croire{VK_SPACE}mes{VK_SPACE}salutations{VK_SPACE}les{VK_SPACE}plus
                    {VK_SPACE}sincères.
                    {ENTER 2}
                    Jason{VK_SPACE}
                    {ENTER}
                    Président{VK_SPACE}de{VK_SPACE}HOLOMORPHE
                    {ENTER}
                    Siège{VK_SPACE}social{VK_SPACE}:{VK_SPACE}31{VK_SPACE}Avenue{VK_SPACE}de{VK_SPACE}Ségur{VK_SPACE}
                    75007{VK_SPACE}Paris
                    {ENTER}
                    Téléphone{VK_SPACE}:{VK_SPACE}00{VK_SPACE}33{VK_SPACE}7{VK_SPACE}51{VK_SPACE}04{VK_SPACE}61{VK_SPACE}25
                    """
                )

                time.sleep(5)

                # Click on the 'Envoyer' button
                pywinauto.mouse.click(button='left', coords=(390, 140))

                time.sleep(5)

        time.sleep(10)

        # Click on the 'Profile' button
        pywinauto.mouse.click(button='left', coords=(1340, 95))

        time.sleep(5)

        # Click on the 'Se deconnecter' button
        pywinauto.mouse.click(button='left', coords=(1210, 295))

        time.sleep(5)

        # Click on the 'Fermer' button of Google Chrome
        pywinauto.mouse.click(button='left', coords=(1345, 10))

        time.sleep(5)

    def test_delete_all_deleted_folders(self):
        app = Application(backend="uia")

        app.start("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")

        time.sleep(10)

        # Open the Outlook Application
        pywinauto.keyboard.send_keys("https://outlook.live.com/owa/")

        time.sleep(5)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(5)

        # Click on the 'Connexion' button
        pywinauto.mouse.click(button='left', coords=(1111, 100))

        time.sleep(5)

        # Type the email address
        pywinauto.keyboard.send_keys('.@outlook.fr')

        time.sleep(5)

        # Type the Tab in 5 times
        pywinauto.keyboard.send_keys('{VK_TAB 5}')

        time.sleep(5)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(5)

        # Type the password
        pywinauto.keyboard.send_keys('')

        time.sleep(5)

        # Type the Tab in 3 times
        pywinauto.keyboard.send_keys('{VK_TAB 3}')

        time.sleep(5)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(15)

        for i in range(39):
            time.sleep(5)

            # Move the mouse on a deleted folder
            pywinauto.mouse.move(coords=(125, 440))
            pywinauto.mouse.click(button='right', coords=(125, 440))

            time.sleep(10)

            # Click on the "Supprimer le dossier" folder
            pywinauto.mouse.move(coords=(200, 490))
            pywinauto.mouse.click(button='left', coords=(200, 490))

            time.sleep(10)

            # Click on the "Ok" folder
            pywinauto.keyboard.send_keys('{ENTER}')

            time.sleep(15)


if __name__ == '__main__':
    unittest.main()
