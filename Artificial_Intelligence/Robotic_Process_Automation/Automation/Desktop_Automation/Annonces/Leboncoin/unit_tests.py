import unittest
import time
from pywinauto.application import Application
import pywinauto.keyboard
import pywinauto.mouse


class UnitTestsDesktopAutomationLeboncoin(unittest.TestCase):
    def test_is64bit(self):
        print("test_is64bit")

        app = Application(backend="uia")

        # Ouvrir l'application Google Chrome
        app.start("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")
        print("is64bit : " + str(app.is64bit()))

    def test_send_message_for_work_office_from_one_ad_with_phone_number(self):
        url_ad = "https://www.leboncoin.fr/ar/?id=1749457525"

        app = Application(backend="uia")

        # Ouvrir l'application Google Chrome
        app.start("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")

        time.sleep(5)

        # Open the Outlook Application
        pywinauto.keyboard.send_keys(url_ad)

        time.sleep(5)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(10)

        # Clik side to the input "Votre nom"
        pywinauto.mouse.click(button='left', coords=(550, 310))

        time.sleep(5)

        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(5)

        # Write my name
        pywinauto.keyboard.send_keys("Mr{VK_SPACE}")

        time.sleep(5)

        # Clik on the input "Votre email"
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(5)

        # Write my email
        pywinauto.keyboard.send_keys("")

        time.sleep(5)

        #Click on the input "Votre message"
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(5)

        # Write my message
        pywinauto.keyboard.send_keys("""
        Bonjour, 
        {ENTER 2}
        Mes{VK_SPACE}questions{VK_SPACE}sont{VK_SPACE}les{VK_SPACE}suivantes{VK_SPACE}:
        {ENTER}
        -{VK_SPACE}Est-ce{VK_SPACE}que{VK_SPACE}le{VK_SPACE}bureau{VK_SPACE}peut{VK_SPACE}être{VK_SPACE}
        utilisé{VK_SPACE}comme{VK_SPACE}siège{VK_SPACE}social{VK_SPACE}s'il{VK_SPACE}vous{VK_SPACE}plaît{VK_SPACE}?
        {ENTER 2}
        -{VK_SPACE}Quel{VK_SPACE}est{VK_SPACE}le{VK_SPACE}montant{VK_SPACE}indicatif{VK_SPACE}de{VK_SPACE}la
        {VK_SPACE}taxe{VK_SPACE}foncière{VK_SPACE}des{VK_SPACE}propriétés{VK_SPACE}bâties{VK_SPACE}pour{VK_SPACE}
        ce{VK_SPACE}bureau{VK_SPACE}s'il{VK_SPACE}vous{VK_SPACE}plaît{VK_SPACE}?
        {ENTER 2}
        -{VK_SPACE}Est-ce{VK_SPACE}que{VK_SPACE}le{VK_SPACE}bureau{VK_SPACE}est{VK_SPACE}équipé{VK_SPACE}
        d'isolation{VK_SPACE}thermique{VK_SPACE}et{VK_SPACE}acoustique{VK_SPACE}s'il{VK_SPACE}vous{VK_SPACE}plaît
        {VK_SPACE}?
        {ENTER 2}
        -{VK_SPACE}Est-ce{VK_SPACE}qu'il{VK_SPACE}y{VK_SPACE}a{VK_SPACE}un{VK_SPACE}compteur{VK_SPACE}
        électrique{VK_SPACE}et{VK_SPACE}un{VK_SPACE}compteur{VK_SPACE}d'eau{VK_SPACE}dans{VK_SPACE}le{VK_SPACE}
        bureau{VK_SPACE}s'il{VK_SPACE}vous{VK_SPACE}plaît{VK_SPACE}?
        {ENTER 2}
        -{VK_SPACE}Est-ce{VK_SPACE}qu'il{VK_SPACE}y{VK_SPACE}a{VK_SPACE}un{VK_SPACE}lavabo{VK_SPACE}et{VK_SPACE}
        un{VK_SPACE}WC{VK_SPACE}dans{VK_SPACE}le{VK_SPACE}bureau{VK_SPACE}s'il{VK_SPACE}vous{VK_SPACE}plaît{VK_SPACE}?
        {ENTER 2}
        -{VK_SPACE}Est-ce{VK_SPACE}qu'il{VK_SPACE}faut{VK_SPACE}déclarer{VK_SPACE}le{VK_SPACE}bureau{VK_SPACE}
        avec{VK_SPACE}le{VK_SPACE}Cerfa{VK_SPACE}n°{VK_SPACE}11213*22{VK_SPACE}pour{VK_SPACE}la{VK_SPACE}taxe
        {VK_SPACE}sur{VK_SPACE}les{VK_SPACE}bureaux{VK_SPACE}en{VK_SPACE}région{VK_SPACE}Ile-de-France{VK_SPACE}
        chaque{VK_SPACE}année{VK_SPACE}s'il{VK_SPACE}vous{VK_SPACE}plaît{VK_SPACE}?
        {ENTER 2}
        Merci{VK_SPACE}pour{VK_SPACE}votre{VK_SPACE}retour.
        {ENTER 2}
        Cordialement,
        """)

        time.sleep(5)

        # Move to the "Envoyer" button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(5)

        # Click tne "Enter" button to send the message
        #pywinauto.keyboard.send_keys("{ENTER}")

        #time.sleep(10)

        #Close the browser
        #pywinauto.keyboard.send_keys('%{F4}')

    def test_send_message_for_work_office_from_a_ad_list_with_phone_number(self):
        urls_ad = [
            "",
            ""
        ]

        for url_ad in urls_ad:

            app = Application(backend="uia")

            # Ouvrir l'application Google Chrome
            app.start("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")

            time.sleep(5)

            # Open the Outlook Application
            pywinauto.keyboard.send_keys(url_ad)

            time.sleep(5)

            # Press the 'Enter' button
            pywinauto.keyboard.send_keys('{ENTER}')

            time.sleep(10)

            # Clik side to the input "Votre nom"
            pywinauto.mouse.click(button='left', coords=(550, 310))

            time.sleep(5)

            pywinauto.keyboard.send_keys("{VK_TAB}")

            time.sleep(5)

            # Write my name
            pywinauto.keyboard.send_keys("Mr{VK_SPACE}")

            time.sleep(5)

            # Clik on the input "Votre email"
            pywinauto.keyboard.send_keys("{VK_TAB}")

            time.sleep(5)

            # Write my email
            pywinauto.keyboard.send_keys("")

            time.sleep(5)

            # Click on the input "Votre message"
            pywinauto.keyboard.send_keys("{VK_TAB 2}")

            time.sleep(5)

            # Write my message
            pywinauto.keyboard.send_keys("""
                    Bonjour, 
                    {ENTER 2}
                    Mes{VK_SPACE}questions{VK_SPACE}sont{VK_SPACE}les{VK_SPACE}suivantes{VK_SPACE}:
                    {ENTER}
                    -{VK_SPACE}Est-ce{VK_SPACE}que{VK_SPACE}le{VK_SPACE}bureau{VK_SPACE}peut{VK_SPACE}être{VK_SPACE}
                    utilisé{VK_SPACE}comme{VK_SPACE}siège{VK_SPACE}social{VK_SPACE}s'il{VK_SPACE}vous{VK_SPACE}plaît{VK_SPACE}?
                    {ENTER 2}
                    -{VK_SPACE}Quel{VK_SPACE}est{VK_SPACE}le{VK_SPACE}montant{VK_SPACE}indicatif{VK_SPACE}de{VK_SPACE}la
                    {VK_SPACE}taxe{VK_SPACE}foncière{VK_SPACE}des{VK_SPACE}propriétés{VK_SPACE}bâties{VK_SPACE}pour{VK_SPACE}
                    ce{VK_SPACE}bureau{VK_SPACE}s'il{VK_SPACE}vous{VK_SPACE}plaît{VK_SPACE}?
                    {ENTER 2}
                    -{VK_SPACE}Est-ce{VK_SPACE}que{VK_SPACE}le{VK_SPACE}bureau{VK_SPACE}est{VK_SPACE}équipé{VK_SPACE}
                    d'isolation{VK_SPACE}thermique{VK_SPACE}et{VK_SPACE}acoustique{VK_SPACE}s'il{VK_SPACE}vous{VK_SPACE}plaît
                    {VK_SPACE}?
                    {ENTER 2}
                    -{VK_SPACE}Est-ce{VK_SPACE}qu'il{VK_SPACE}y{VK_SPACE}a{VK_SPACE}un{VK_SPACE}compteur{VK_SPACE}
                    électrique{VK_SPACE}et{VK_SPACE}un{VK_SPACE}compteur{VK_SPACE}d'eau{VK_SPACE}dans{VK_SPACE}le{VK_SPACE}
                    bureau{VK_SPACE}s'il{VK_SPACE}vous{VK_SPACE}plaît{VK_SPACE}?
                    {ENTER 2}
                    -{VK_SPACE}Est-ce{VK_SPACE}qu'il{VK_SPACE}y{VK_SPACE}a{VK_SPACE}un{VK_SPACE}lavabo{VK_SPACE}et{VK_SPACE}
                    un{VK_SPACE}WC{VK_SPACE}dans{VK_SPACE}le{VK_SPACE}bureau{VK_SPACE}s'il{VK_SPACE}vous{VK_SPACE}plaît{VK_SPACE}?
                    {ENTER 2}
                    -{VK_SPACE}Est-ce{VK_SPACE}qu'il{VK_SPACE}faut{VK_SPACE}déclarer{VK_SPACE}le{VK_SPACE}bureau{VK_SPACE}
                    avec{VK_SPACE}le{VK_SPACE}Cerfa{VK_SPACE}n°{VK_SPACE}11213*22{VK_SPACE}pour{VK_SPACE}la{VK_SPACE}taxe
                    {VK_SPACE}sur{VK_SPACE}les{VK_SPACE}bureaux{VK_SPACE}en{VK_SPACE}région{VK_SPACE}Ile-de-France{VK_SPACE}
                    chaque{VK_SPACE}année{VK_SPACE}s'il{VK_SPACE}vous{VK_SPACE}plaît{VK_SPACE}?
                    {ENTER 2}
                    Merci{VK_SPACE}pour{VK_SPACE}votre{VK_SPACE}retour.
                    {ENTER 2}
                    Cordialement,
                    """)

            time.sleep(5)

            # Move to the "Envoyer" button
            pywinauto.keyboard.send_keys("{VK_TAB}")

            time.sleep(5)

            # Click tne "Enter" button to send the message
            pywinauto.keyboard.send_keys("{ENTER}")

            time.sleep(10)

            # Close the browser
            pywinauto.keyboard.send_keys('%{F4}')

            time.sleep(10)

    def test_send_message_for_box_from_one_ad_without_phone_number(self):
        url_ad = "https://www.leboncoin.fr/ar/?id=1742468074"

        app = Application(backend="uia")

        # Ouvrir l'application Google Chrome
        app.start("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")

        time.sleep(5)

        # Open the Outlook Application
        pywinauto.keyboard.send_keys(url_ad)

        time.sleep(5)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(10)

        # Clik on the input "Votre nom"
        pywinauto.mouse.click(button='left', coords=(550, 310))

        time.sleep(5)

        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(5)

        # Write my name
        pywinauto.keyboard.send_keys("Mr{VK_SPACE}")

        time.sleep(5)

        # Clik on the input "Votre email"
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(5)

        # Write my email
        pywinauto.keyboard.send_keys("")

        time.sleep(5)

        # Click on the input "Votre message"
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(5)

        # Write my message
        pywinauto.keyboard.send_keys("""
        Bonjour, 
        {ENTER 2}
        Mes{VK_SPACE}questions{VK_SPACE}sont{VK_SPACE}les{VK_SPACE}suivantes{VK_SPACE}:
        {ENTER}
        -{VK_SPACE}Est-ce{VK_SPACE}que{VK_SPACE}le{VK_SPACE}box{VK_SPACE}est{VK_SPACE}acquérable{VK_SPACE}sans
        {VK_SPACE}remise{VK_SPACE}future{VK_SPACE}à{VK_SPACE}une{VK_SPACE}collectivité{VK_SPACE}territoriale
        {VK_SPACE}ou{VK_SPACE}une{VK_SPACE}telle{VK_SPACE}institution{VK_SPACE}publique{VK_SPACE}ou{VK_SPACE}
        privée{VK_SPACE}s'il{VK_SPACE}vous{VK_SPACE}plaît{VK_SPACE}?
        {ENTER 2}
        -{VK_SPACE}Quel{VK_SPACE}est{VK_SPACE}le{VK_SPACE}montant{VK_SPACE}indicatif{VK_SPACE}de{VK_SPACE}la
        {VK_SPACE}taxe{VK_SPACE}foncière{VK_SPACE}des{VK_SPACE}propriétés{VK_SPACE}bâties{VK_SPACE}pour{VK_SPACE}
        ce{VK_SPACE}box{VK_SPACE}s'il{VK_SPACE}vous{VK_SPACE}plaît{VK_SPACE}?
        {ENTER 2}
        -{VK_SPACE}Est-ce{VK_SPACE}qu'il{VK_SPACE}faut{VK_SPACE}déclarer{VK_SPACE}le{VK_SPACE}box{VK_SPACE}
        avec{VK_SPACE}le{VK_SPACE}Cerfa{VK_SPACE}n°{VK_SPACE}11213*22{VK_SPACE}pour{VK_SPACE}la{VK_SPACE}taxe
        {VK_SPACE}sur{VK_SPACE}les{VK_SPACE}bureaux{VK_SPACE}en{VK_SPACE}région{VK_SPACE}Ile-de-France{VK_SPACE}
        chaque{VK_SPACE}année{VK_SPACE}s'il{VK_SPACE}vous{VK_SPACE}plaît{VK_SPACE}?
        {ENTER 2}
        -{VK_SPACE}Est-ce{VK_SPACE}que{VK_SPACE}l'utilisation{VK_SPACE}d'outils{VK_SPACE}bruyants,{VK_SPACE}
        par{VK_SPACE}exemple,{VK_SPACE}une{VK_SPACE}perceuse,{VK_SPACE}une{VK_SPACE}meuleuse,{VK_SPACE}
        un{VK_SPACE}moteur{VK_SPACE}à{VK_SPACE}combustion{VK_SPACE}interne,{VK_SPACE}sur{VK_SPACE}une
        {VK_SPACE}durée{VK_SPACE}indéterminée{VK_SPACE}est{VK_SPACE}tolérée{VK_SPACE}dans{VK_SPACE}le{VK_SPACE}box
        {VK_SPACE}s'il{VK_SPACE}vous{VK_SPACE}plaît{VK_SPACE}?
        {ENTER 2}
        Merci{VK_SPACE}pour{VK_SPACE}votre{VK_SPACE}retour.
        {ENTER 2}
        Cordialement,
        """)

        time.sleep(5)

        # Move to the "Envoyer" button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(5)

        # Click tne "Enter" button to send the message
        pywinauto.keyboard.send_keys("{ENTER}")

        time.sleep(10)

        # Close the browser
        pywinauto.keyboard.send_keys('%{F4}')

    def test_send_message_for_box_from_a_ad_list_without_phone_number(self):
        urls_ad = [
            "https://www.leboncoin.fr/ar/?id=1754977093",
            "https://www.leboncoin.fr/ar/?id=1771039510"
        ]

        for url_ad in urls_ad:
            app = Application(backend="uia")

            # Ouvrir l'application Google Chrome
            app.start("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")

            time.sleep(5)

            # Open the Outlook Application
            pywinauto.keyboard.send_keys(url_ad)

            time.sleep(5)

            # Press the 'Enter' button
            pywinauto.keyboard.send_keys('{ENTER}')

            time.sleep(10)

            # Clik on the input "Votre nom"
            pywinauto.mouse.click(button='left', coords=(550, 323))

            time.sleep(5)

            pywinauto.keyboard.send_keys("{VK_TAB}")

            time.sleep(5)

            # Write my name
            pywinauto.keyboard.send_keys("Mr{VK_SPACE}")

            time.sleep(5)

            # Clik on the input "Votre email"
            pywinauto.keyboard.send_keys("{VK_TAB}")

            time.sleep(5)

            # Write my email
            pywinauto.keyboard.send_keys("")

            time.sleep(5)

            # Click on the input "Votre message"
            pywinauto.keyboard.send_keys("{VK_TAB}")

            time.sleep(5)

            # Write my message
            pywinauto.keyboard.send_keys("""
            Bonjour, 
            {ENTER 2}
            Mes{VK_SPACE}questions{VK_SPACE}sont{VK_SPACE}les{VK_SPACE}suivantes{VK_SPACE}:
            {ENTER}
            -{VK_SPACE}Est-ce{VK_SPACE}que{VK_SPACE}le{VK_SPACE}box{VK_SPACE}est{VK_SPACE}acquérable{VK_SPACE}sans
            {VK_SPACE}remise{VK_SPACE}future{VK_SPACE}à{VK_SPACE}une{VK_SPACE}collectivité{VK_SPACE}territoriale
            {VK_SPACE}ou{VK_SPACE}une{VK_SPACE}telle{VK_SPACE}institution{VK_SPACE}publique{VK_SPACE}ou{VK_SPACE}
            privée{VK_SPACE}s'il{VK_SPACE}vous{VK_SPACE}plaît{VK_SPACE}?
            {ENTER 2}
            -{VK_SPACE}Quel{VK_SPACE}est{VK_SPACE}le{VK_SPACE}montant{VK_SPACE}indicatif{VK_SPACE}de{VK_SPACE}la
            {VK_SPACE}taxe{VK_SPACE}foncière{VK_SPACE}des{VK_SPACE}propriétés{VK_SPACE}bâties{VK_SPACE}pour{VK_SPACE}
            ce{VK_SPACE}box{VK_SPACE}s'il{VK_SPACE}vous{VK_SPACE}plaît{VK_SPACE}?
            {ENTER 2}
            -{VK_SPACE}Est-ce{VK_SPACE}qu'il{VK_SPACE}faut{VK_SPACE}déclarer{VK_SPACE}le{VK_SPACE}box{VK_SPACE}
            avec{VK_SPACE}le{VK_SPACE}Cerfa{VK_SPACE}n°{VK_SPACE}11213*22{VK_SPACE}pour{VK_SPACE}la{VK_SPACE}taxe
            {VK_SPACE}sur{VK_SPACE}les{VK_SPACE}bureaux{VK_SPACE}en{VK_SPACE}région{VK_SPACE}Ile-de-France{VK_SPACE}
            chaque{VK_SPACE}année{VK_SPACE}s'il{VK_SPACE}vous{VK_SPACE}plaît{VK_SPACE}?
            {ENTER 2}
            -{VK_SPACE}Est-ce{VK_SPACE}que{VK_SPACE}l'utilisation{VK_SPACE}d'outils{VK_SPACE}bruyants,{VK_SPACE}
            par{VK_SPACE}exemple,{VK_SPACE}une{VK_SPACE}perceuse,{VK_SPACE}une{VK_SPACE}meuleuse,{VK_SPACE}
            un{VK_SPACE}moteur{VK_SPACE}à{VK_SPACE}combustion{VK_SPACE}interne,{VK_SPACE}sur{VK_SPACE}une
            {VK_SPACE}durée{VK_SPACE}indéterminée{VK_SPACE}est{VK_SPACE}tolérée{VK_SPACE}dans{VK_SPACE}le{VK_SPACE}box
            {VK_SPACE}s'il{VK_SPACE}vous{VK_SPACE}plaît{VK_SPACE}?
            {ENTER 2}
            Merci{VK_SPACE}pour{VK_SPACE}votre{VK_SPACE}retour.
            {ENTER 2}
            Cordialement,
            """)

            time.sleep(5)

            # Move to the "Envoyer" button
            pywinauto.keyboard.send_keys("{VK_TAB}")

            time.sleep(5)

            # Click tne "Enter" button to send the message
            pywinauto.keyboard.send_keys("{ENTER}")

            time.sleep(10)

            # Close the browser
            pywinauto.keyboard.send_keys('%{F4}')

    def test_send_message_for_single_room_from_one_ad_without_phone_number(self):
        url_ad = "https://www.leboncoin.fr/ar/?id=1797390700"

        app = Application(backend="uia")

        # Ouvrir l'application Google Chrome
        app.start("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")

        time.sleep(5)

        # Open the Outlook Application
        pywinauto.keyboard.send_keys(url_ad)

        time.sleep(5)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(10)

        # Clik side to the input "Votre nom"
        pywinauto.mouse.click(button='left', coords=(550, 335))

        time.sleep(5)

        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(5)

        # Write my name
        pywinauto.keyboard.send_keys("Mr{VK_SPACE}")

        time.sleep(5)

        # Clik on the input "Votre email"
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(5)

        # Write my email
        pywinauto.keyboard.send_keys("")

        time.sleep(5)

        #Click on the input "Votre message"
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(5)

        # Write my message
        pywinauto.keyboard.send_keys("""
        Bonjour, 
        {ENTER 2}
        Est-ce{VK_SPACE}que{VK_SPACE}le{VK_SPACE}bien{VK_SPACE}peut{VK_SPACE}être{VK_SPACE}utilisé{VK_SPACE}
        comme{VK_SPACE}siège{VK_SPACE}social{VK_SPACE}d'une{VK_SPACE}société{VK_SPACE}s'il{VK_SPACE}vous{VK_SPACE}
        plaît{VK_SPACE}?
        {ENTER 2}
        Cordialement,
        """)

        time.sleep(5)

        # Move to the "Envoyer" button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(5)

        # Click tne "Enter" button to send the message
        pywinauto.keyboard.send_keys("{ENTER}")

        time.sleep(10)

        #Close the browser
        pywinauto.keyboard.send_keys('%{F4}')

    def test_send_message_for_signle_room_from_a_ad_list_without_phone_number(self):
        urls_ad = [
            "",
        ]

        for url_ad in urls_ad:

            app = Application(backend="uia")

            # Ouvrir l'application Google Chrome
            app.start("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")

            time.sleep(5)

            # Open the Outlook Application
            pywinauto.keyboard.send_keys(url_ad)

            time.sleep(5)

            # Press the 'Enter' button
            pywinauto.keyboard.send_keys('{ENTER}')

            time.sleep(10)

            # Clik side to the input "Votre nom"
            pywinauto.mouse.click(button='left', coords=(550, 335))

            time.sleep(5)

            pywinauto.keyboard.send_keys("{VK_TAB}")

            time.sleep(5)

            # Write my name
            pywinauto.keyboard.send_keys("Mr{VK_SPACE}")

            time.sleep(5)

            # Clik on the input "Votre email"
            pywinauto.keyboard.send_keys("{VK_TAB}")

            time.sleep(5)

            # Write my email
            pywinauto.keyboard.send_keys("")

            time.sleep(5)

            # Click on the input "Votre message"
            pywinauto.keyboard.send_keys("{VK_TAB}")

            time.sleep(5)

            # Write my message
            pywinauto.keyboard.send_keys("""
                    Bonjour, 
                    {ENTER 2}
                    Est-ce{VK_SPACE}que{VK_SPACE}le{VK_SPACE}bien{VK_SPACE}peut{VK_SPACE}être{VK_SPACE}utilisé{VK_SPACE}
                    comme{VK_SPACE}siège{VK_SPACE}social{VK_SPACE}d'une{VK_SPACE}société{VK_SPACE}s'il{VK_SPACE}vous{VK_SPACE}
                    plaît{VK_SPACE}?
                    {ENTER 2}
                    Cordialement,
                    """)

            time.sleep(5)

            # Move to the "Envoyer" button
            pywinauto.keyboard.send_keys("{VK_TAB}")

            time.sleep(5)

            # Click tne "Enter" button to send the message
            pywinauto.keyboard.send_keys("{ENTER}")

            time.sleep(10)

            # Close the browser
            pywinauto.keyboard.send_keys('%{F4}')

            time.sleep(10)

    def test_send_message_for_signle_room_from_a_ad_list_with_phone_number(self):
        urls_ad = [
            "",
        ]

        for url_ad in urls_ad:

            app = Application(backend="uia")

            # Ouvrir l'application Google Chrome
            app.start("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")

            time.sleep(5)

            # Open the Outlook Application
            pywinauto.keyboard.send_keys(url_ad)

            time.sleep(5)

            # Press the 'Enter' button
            pywinauto.keyboard.send_keys('{ENTER}')

            time.sleep(10)

            # Clik side to the input "Votre nom"
            pywinauto.mouse.click(button='left', coords=(550, 200))

            time.sleep(5)

            pywinauto.keyboard.send_keys("{VK_TAB}")

            time.sleep(5)

            # Write my name
            pywinauto.keyboard.send_keys("Mr{VK_SPACE}")

            time.sleep(5)

            # Clik on the input "Votre email"
            pywinauto.keyboard.send_keys("{VK_TAB}")

            time.sleep(5)

            # Write my email
            pywinauto.keyboard.send_keys("")

            time.sleep(5)

            # Click on the input "Votre message"
            pywinauto.keyboard.send_keys("{VK_TAB 2}")

            time.sleep(5)

            # Write my message
            pywinauto.keyboard.send_keys("""
                    Bonjour, 
                    {ENTER 2}
                    Est-ce{VK_SPACE}que{VK_SPACE}le{VK_SPACE}bien{VK_SPACE}peut{VK_SPACE}être{VK_SPACE}utilisé{VK_SPACE}
                    comme{VK_SPACE}siège{VK_SPACE}social{VK_SPACE}d'une{VK_SPACE}société{VK_SPACE}s'il{VK_SPACE}vous{VK_SPACE}
                    plaît{VK_SPACE}?
                    {ENTER 2}
                    Cordialement,
                    """)

            time.sleep(5)

            # Move to the "Envoyer" button
            pywinauto.keyboard.send_keys("{VK_TAB}")

            time.sleep(5)

            # Click tne "Enter" button to send the message
            pywinauto.keyboard.send_keys("{ENTER}")

            time.sleep(10)

            # Close the browser
            pywinauto.keyboard.send_keys('%{F4}')

            time.sleep(10)

    def test_send_message_for_cave_from_one_ad_with_phone_number(self):
        url_ad = "https://www.leboncoin.fr/ar/?id=1749457525"

        app = Application(backend="uia")

        # Ouvrir l'application Google Chrome
        app.start("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")

        time.sleep(5)

        # Open the Outlook Application
        pywinauto.keyboard.send_keys(url_ad)

        time.sleep(5)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(10)

        # Clik side to the input "Votre nom"
        pywinauto.mouse.click(button='left', coords=(550, 310))

        time.sleep(5)

        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(5)

        # Write my name
        pywinauto.keyboard.send_keys("Mr{VK_SPACE}")

        time.sleep(5)

        # Clik on the input "Votre email"
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(5)

        # Write my email
        pywinauto.keyboard.send_keys("")

        time.sleep(5)

        #Click on the input "Votre message"
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(5)

        # Write my message
        pywinauto.keyboard.send_keys("""
        Bonjour, 
        {ENTER 2}
        Mes{VK_SPACE}questions{VK_SPACE}sont{VK_SPACE}les{VK_SPACE}suivantes{VK_SPACE}:
        {ENTER}
        -{VK_SPACE}Est-ce{VK_SPACE}que{VK_SPACE}le{VK_SPACE}bureau{VK_SPACE}peut{VK_SPACE}être{VK_SPACE}
        utilisé{VK_SPACE}comme{VK_SPACE}siège{VK_SPACE}social{VK_SPACE}s'il{VK_SPACE}vous{VK_SPACE}plaît{VK_SPACE}?
        {ENTER 2}
        -{VK_SPACE}Quel{VK_SPACE}est{VK_SPACE}le{VK_SPACE}montant{VK_SPACE}indicatif{VK_SPACE}de{VK_SPACE}la
        {VK_SPACE}taxe{VK_SPACE}foncière{VK_SPACE}des{VK_SPACE}propriétés{VK_SPACE}bâties{VK_SPACE}pour{VK_SPACE}
        ce{VK_SPACE}bureau{VK_SPACE}s'il{VK_SPACE}vous{VK_SPACE}plaît{VK_SPACE}?
        {ENTER 2}
        -{VK_SPACE}Est-ce{VK_SPACE}que{VK_SPACE}le{VK_SPACE}bureau{VK_SPACE}est{VK_SPACE}équipé{VK_SPACE}
        d'isolation{VK_SPACE}thermique{VK_SPACE}et{VK_SPACE}acoustique{VK_SPACE}s'il{VK_SPACE}vous{VK_SPACE}plaît
        {VK_SPACE}?
        {ENTER 2}
        -{VK_SPACE}Est-ce{VK_SPACE}qu'il{VK_SPACE}y{VK_SPACE}a{VK_SPACE}un{VK_SPACE}compteur{VK_SPACE}
        électrique{VK_SPACE}et{VK_SPACE}un{VK_SPACE}compteur{VK_SPACE}d'eau{VK_SPACE}dans{VK_SPACE}le{VK_SPACE}
        bureau{VK_SPACE}s'il{VK_SPACE}vous{VK_SPACE}plaît{VK_SPACE}?
        {ENTER 2}
        -{VK_SPACE}Est-ce{VK_SPACE}qu'il{VK_SPACE}y{VK_SPACE}a{VK_SPACE}un{VK_SPACE}lavabo{VK_SPACE}et{VK_SPACE}
        un{VK_SPACE}WC{VK_SPACE}dans{VK_SPACE}le{VK_SPACE}bureau{VK_SPACE}s'il{VK_SPACE}vous{VK_SPACE}plaît{VK_SPACE}?
        {ENTER 2}
        -{VK_SPACE}Est-ce{VK_SPACE}qu'il{VK_SPACE}faut{VK_SPACE}déclarer{VK_SPACE}le{VK_SPACE}bureau{VK_SPACE}
        avec{VK_SPACE}le{VK_SPACE}Cerfa{VK_SPACE}n°{VK_SPACE}11213*22{VK_SPACE}pour{VK_SPACE}la{VK_SPACE}taxe
        {VK_SPACE}sur{VK_SPACE}les{VK_SPACE}bureaux{VK_SPACE}en{VK_SPACE}région{VK_SPACE}Ile-de-France{VK_SPACE}
        chaque{VK_SPACE}année{VK_SPACE}s'il{VK_SPACE}vous{VK_SPACE}plaît{VK_SPACE}?
        {ENTER 2}
        Merci{VK_SPACE}pour{VK_SPACE}votre{VK_SPACE}retour.
        {ENTER 2}
        Cordialement,
        """)

        time.sleep(5)

        # Move to the "Envoyer" button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(5)

        # Click tne "Enter" button to send the message
        #pywinauto.keyboard.send_keys("{ENTER}")

        #time.sleep(10)

        #Close the browser
        #pywinauto.keyboard.send_keys('%{F4}')

    def test_send_message_for_apartment_for_etablishing_school_from_a_ad_list_without_phone_number(self):
        urls_ad = [
            "https://www.leboncoin.fr/ar/?id=1707656564",
            "https://www.leboncoin.fr/ar/?id=1774588493",
            "https://www.leboncoin.fr/ar/?id=1779436120",
            "https://www.leboncoin.fr/ar/?id=1786922999",
            "https://www.leboncoin.fr/ar/?id=1780284748",
            "https://www.leboncoin.fr/ar/?id=1779804835",
            "https://www.leboncoin.fr/ar/?id=1801523637",
            "https://www.leboncoin.fr/ar/?id=1793728216",
            "https://www.leboncoin.fr/ar/?id=1795912734",
            "https://www.leboncoin.fr/ar/?id=1783233252",
            "https://www.leboncoin.fr/ar/?id=1779484020"
        ]

        for url_ad in urls_ad:

            app = Application(backend="uia")

            # Ouvrir l'application Google Chrome
            app.start("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")

            time.sleep(5)

            # Open the Outlook Application
            pywinauto.keyboard.send_keys(url_ad)

            time.sleep(5)

            # Press the 'Enter' button
            pywinauto.keyboard.send_keys('{ENTER}')

            time.sleep(10)

            # Clik side to the input "Votre nom"
            pywinauto.mouse.click(button='left', coords=(550, 335))

            time.sleep(5)

            pywinauto.keyboard.send_keys("{VK_TAB}")

            time.sleep(5)

            # Write my name
            pywinauto.keyboard.send_keys("Mr{VK_SPACE}")

            time.sleep(5)

            # Clik on the input "Votre email"
            pywinauto.keyboard.send_keys("{VK_TAB}")

            time.sleep(5)

            # Write my email
            pywinauto.keyboard.send_keys("")

            time.sleep(5)

            # Click on the input "Votre message"
            pywinauto.keyboard.send_keys("{VK_TAB}")

            time.sleep(5)

            # Write my message
            pywinauto.keyboard.send_keys("""
                    Bonjour, 
                    {ENTER 2}
                    Est-ce{VK_SPACE}que{VK_SPACE}le{VK_SPACE}bien{VK_SPACE}peut{VK_SPACE}être
                    {VK_SPACE}utilisé{VK_SPACE}pour{VK_SPACE}ouvrir{VK_SPACE}un{VK_SPACE}établissement
                    {VK_SPACE}d'enseignement{VK_SPACE}supérieur{VK_SPACE}privé{VK_SPACE}délivrant{VK_SPACE}un
                    {VK_SPACE}diplôme{VK_SPACE}conférant{VK_SPACE}un{VK_SPACE}grade{VK_SPACE}de{VK_SPACE}
                    master{VK_SPACE}s'il{VK_SPACE}vous{VK_SPACE}plaît{VK_SPACE}?
                    {ENTER 2}
                    Cet{VK_SPACE}établissement{VK_SPACE}devra{VK_SPACE}être{VK_SPACE}une{VK_SPACE}école{VK_SPACE}d'ingénieur
                    {VK_SPACE}orientée{VK_SPACE}vers{VK_SPACE}le{VK_SPACE}domaine{VK_SPACE}de{VK_SPACE}l'énergie.
                    {ENTER 2}
                    Cordialement,
                    """)

            time.sleep(5)

            # Move to the "Envoyer" button
            pywinauto.keyboard.send_keys("{VK_TAB}")

            time.sleep(5)

            # Click tne "Enter" button to send the message
            pywinauto.keyboard.send_keys("{ENTER}")

            time.sleep(10)

            # Close the browser
            pywinauto.keyboard.send_keys('%{F4}')

            time.sleep(10)

    def test_send_message_for_apartment_for_etablishing_school_from_a_ad_list_with_phone_number(self):
        urls_ad = [
            "https://www.leboncoin.fr/ar/?id=1791981989",
            "https://www.leboncoin.fr/ar/?id=1726400299",
            "https://www.leboncoin.fr/ar/?id=1783418527",
            "https://www.leboncoin.fr/ar/?id=1784395462",
            "https://www.leboncoin.fr/ar/?id=1800656151",
            "https://www.leboncoin.fr/ar/?id=1784181020",
            "https://www.leboncoin.fr/ar/?id=1802366394",
            "https://www.leboncoin.fr/ar/?id=1775999284",
            "https://www.leboncoin.fr/ar/?id=1774481881",
            "https://www.leboncoin.fr/ar/?id=1801582046",
            "https://www.leboncoin.fr/ar/?id=1734043403",
            "https://www.leboncoin.fr/ar/?id=1719704232",
            "https://www.leboncoin.fr/ar/?id=1784358613",
            "https://www.leboncoin.fr/ar/?id=1785649917",
            "https://www.leboncoin.fr/ar/?id=1803227034",
            "https://www.leboncoin.fr/ar/?id=1788791512",
            "https://www.leboncoin.fr/ar/?id=1640108485",
            "https://www.leboncoin.fr/ar/?id=1780234725",
            "https://www.leboncoin.fr/ar/?id=1793290706",
            "https://www.leboncoin.fr/ar/?id=1787515760",
            "https://www.leboncoin.fr/ar/?id=1751530861",
            "https://www.leboncoin.fr/ar/?id=1777992548",
            "https://www.leboncoin.fr/ar/?id=1680564538",
            "https://www.leboncoin.fr/ar/?id=1752016154",
            "https://www.leboncoin.fr/ar/?id=1666296745",
            "https://www.leboncoin.fr/ar/?id=1791982038",
            "https://www.leboncoin.fr/ar/?id=1792025816",
            "https://www.leboncoin.fr/ar/?id=1797310134",
            "https://www.leboncoin.fr/ar/?id=1795166802",
            "https://www.leboncoin.fr/ar/?id=1791625551",
            "https://www.leboncoin.fr/ar/?id=1800484979",
            "https://www.leboncoin.fr/ar/?id=1777580783",
            "https://www.leboncoin.fr/ar/?id=1801532545",
            "https://www.leboncoin.fr/ar/?id=1753928008",
            "https://www.leboncoin.fr/ar/?id=1712894151",
            "https://www.leboncoin.fr/ar/?id=1802366225",
            "https://www.leboncoin.fr/ar/?id=1801713870",
            "https://www.leboncoin.fr/ar/?id=1795678972",
            "https://www.leboncoin.fr/ar/?id=1783064792",
            "https://www.leboncoin.fr/ar/?id=1801209099",
            "https://www.leboncoin.fr/ar/?id=1707232662",
            "https://www.leboncoin.fr/ar/?id=1765177033",
            "https://www.leboncoin.fr/ar/?id=1803339215",
            "https://www.leboncoin.fr/ar/?id=1788516340",
            "https://www.leboncoin.fr/ar/?id=1789202840",
            "https://www.leboncoin.fr/ar/?id=1799244901",
            "https://www.leboncoin.fr/ar/?id=1727019046",
            "https://www.leboncoin.fr/ar/?id=1802023283",
            "https://www.leboncoin.fr/ar/?id=1759159325",
            "https://www.leboncoin.fr/ar/?id=1795663131",
            "https://www.leboncoin.fr/ar/?id=1787752552",
            "https://www.leboncoin.fr/ar/?id=1796013713",
            "https://www.leboncoin.fr/ar/?id=1679884189",
            "https://www.leboncoin.fr/ar/?id=1802087554",
            "https://www.leboncoin.fr/ar/?id=1676377525",
            "https://www.leboncoin.fr/ar/?id=1750116551",
            "https://www.leboncoin.fr/ar/?id=1752033681",
            "https://www.leboncoin.fr/ar/?id=1776461078",
            "https://www.leboncoin.fr/ar/?id=1747043987",
            "https://www.leboncoin.fr/ar/?id=1799805910",
            "https://www.leboncoin.fr/ar/?id=1799806427",
            "https://www.leboncoin.fr/ar/?id=1787477978"
        ]

        for url_ad in urls_ad:

            app = Application(backend="uia")

            # Ouvrir l'application Google Chrome
            app.start("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")

            time.sleep(5)

            # Open the Outlook Application
            pywinauto.keyboard.send_keys(url_ad)

            time.sleep(5)

            # Press the 'Enter' button
            pywinauto.keyboard.send_keys('{ENTER}')

            time.sleep(10)

            # Clik side to the input "Votre nom"
            pywinauto.mouse.click(button='left', coords=(550, 200))

            time.sleep(5)

            pywinauto.keyboard.send_keys("{VK_TAB}")

            time.sleep(5)

            # Write my name
            pywinauto.keyboard.send_keys("Mr{VK_SPACE}")

            time.sleep(5)

            # Clik on the input "Votre email"
            pywinauto.keyboard.send_keys("{VK_TAB}")

            time.sleep(5)

            # Write my email
            pywinauto.keyboard.send_keys("")

            time.sleep(5)

            # Click on the input "Votre message"
            pywinauto.keyboard.send_keys("{VK_TAB 2}")

            time.sleep(5)

            # Write my message
            pywinauto.keyboard.send_keys("""
                    Bonjour, 
                    {ENTER 2}
                    Est-ce{VK_SPACE}que{VK_SPACE}le{VK_SPACE}bien{VK_SPACE}peut{VK_SPACE}être
                    {VK_SPACE}utilisé{VK_SPACE}pour{VK_SPACE}ouvrir{VK_SPACE}un{VK_SPACE}établissement
                    {VK_SPACE}d'enseignement{VK_SPACE}supérieur{VK_SPACE}privé{VK_SPACE}délivrant{VK_SPACE}un
                    {VK_SPACE}diplôme{VK_SPACE}conférant{VK_SPACE}un{VK_SPACE}grade{VK_SPACE}de{VK_SPACE}
                    master{VK_SPACE}s'il{VK_SPACE}vous{VK_SPACE}plaît{VK_SPACE}?
                    {ENTER 2}
                    Cet{VK_SPACE}établissement{VK_SPACE}devra{VK_SPACE}être{VK_SPACE}une{VK_SPACE}école{VK_SPACE}d'ingénieur
                    {VK_SPACE}orientée{VK_SPACE}vers{VK_SPACE}le{VK_SPACE}domaine{VK_SPACE}de{VK_SPACE}l'énergie.
                    {ENTER 2}
                    Cordialement,
                    """)

            time.sleep(5)

            # Move to the "Envoyer" button
            pywinauto.keyboard.send_keys("{VK_TAB}")

            time.sleep(5)

            # Click tne "Enter" button to send the message
            pywinauto.keyboard.send_keys("{ENTER}")

            time.sleep(10)

            # Close the browser
            pywinauto.keyboard.send_keys('%{F4}')

            time.sleep(10)

    def test_send_message_for_land_for_parking_cars_from_a_ad_list_with_phone_number(self):
        urls_ad = [

        ]

        for url_ad in urls_ad:

            app = Application(backend="uia")

            # Ouvrir l'application Google Chrome
            app.start("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")

            time.sleep(5)

            # Open the Outlook Application
            pywinauto.keyboard.send_keys(url_ad)

            time.sleep(5)

            # Press the 'Enter' button
            pywinauto.keyboard.send_keys('{ENTER}')

            time.sleep(10)

            # Clik side to the input "Votre nom"
            pywinauto.mouse.click(button='left', coords=(550, 200))

            time.sleep(5)

            pywinauto.keyboard.send_keys("{VK_TAB}")

            time.sleep(5)

            # Write my name
            pywinauto.keyboard.send_keys("Mr{VK_SPACE}")

            time.sleep(5)

            # Clik on the input "Votre email"
            pywinauto.keyboard.send_keys("{VK_TAB}")

            time.sleep(5)

            # Write my email
            pywinauto.keyboard.send_keys("")

            time.sleep(5)

            # Click on the input "Votre message"
            pywinauto.keyboard.send_keys("{VK_TAB 2}")

            time.sleep(5)

            # Write my message
            pywinauto.keyboard.send_keys("""
                    Bonjour, 
                    {ENTER 2}
                    Est-ce{VK_SPACE}que{VK_SPACE}le{VK_SPACE}terrain{VK_SPACE}peut{VK_SPACE}être
                    {VK_SPACE}utilisé{VK_SPACE}pour{VK_SPACE}stationner{VK_SPACE}des{VK_SPACE}voitures{VK_SPACE}
                    roulantes{VK_SPACE}de{VK_SPACE}manière{VK_SPACE}temporaire{VK_SPACE}s'il{VK_SPACE}vous{VK_SPACE}plaît{VK_SPACE}?
                    {ENTER 2}
                    Est-ce{VK_SPACE}que{VK_SPACE}le{VK_SPACE}terrain{VK_SPACE}peut{VK_SPACE}être{VK_SPACE}
                    clôturé{VK_SPACE}avec{VK_SPACE}des{VK_SPACE}grillages,{VK_SPACE}soit{VK_SPACE}des{VK_SPACE}
                    briques,{VK_SPACE}soit{VK_SPACE}des{VK_SPACE}sacs{VK_SPACE}remplis{VK_SPACE}de{VK_SPACE}
                    terre{VK_SPACE}pour{VK_SPACE}protèger{VK_SPACE}les{VK_SPACE}voitures{VK_SPACE}contre{VK_SPACE}
                    le{VK_SPACE}vol,{VK_SPACE}le{VK_SPACE}vandalisme{VK_SPACE}et{VK_SPACE}toutes{VK_SPACE}les{VK_SPACE}
                    situations{VK_SPACE}inconvenables{VK_SPACE}s'il{VK_SPACE}vous{VK_SPACE}plaît{VK_SPACE}?
                    {ENTER 2}
                    Cordialement,
                    """)

            time.sleep(5)

            # Move to the "Envoyer" button
            pywinauto.keyboard.send_keys("{VK_TAB}")

            time.sleep(5)

            # Click tne "Enter" button to send the message
            pywinauto.keyboard.send_keys("{ENTER}")

            time.sleep(10)

            # Close the browser
            pywinauto.keyboard.send_keys('%{F4}')

            time.sleep(10)

    def test_send_message_for_land_for_parking_cars_from_a_ad_list_without_phone_number(self):
        urls_ad = [

        ]

        for url_ad in urls_ad:

            app = Application(backend="uia")

            # Ouvrir l'application Google Chrome
            app.start("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")

            time.sleep(5)

            # Open the Outlook Application
            pywinauto.keyboard.send_keys(url_ad)

            time.sleep(5)

            # Press the 'Enter' button
            pywinauto.keyboard.send_keys('{ENTER}')

            time.sleep(10)

            # Clik side to the input "Votre nom"
            pywinauto.mouse.click(button='left', coords=(550, 200))

            time.sleep(5)

            pywinauto.keyboard.send_keys("{VK_TAB}")

            time.sleep(5)

            # Write my name
            pywinauto.keyboard.send_keys("Mr{VK_SPACE}")

            time.sleep(5)

            # Clik on the input "Votre email"
            pywinauto.keyboard.send_keys("{VK_TAB}")

            time.sleep(5)

            # Write my email
            pywinauto.keyboard.send_keys("")

            time.sleep(5)

            # Click on the input "Votre message"
            pywinauto.keyboard.send_keys("{VK_TAB}")

            time.sleep(5)

            # Write my message
            pywinauto.keyboard.send_keys("""
                    Bonjour, 
                    {ENTER 2}
                    Est-ce{VK_SPACE}que{VK_SPACE}le{VK_SPACE}terrain{VK_SPACE}peut{VK_SPACE}être
                    {VK_SPACE}utilisé{VK_SPACE}pour{VK_SPACE}stationner{VK_SPACE}des{VK_SPACE}voitures{VK_SPACE}
                    roulantes{VK_SPACE}de{VK_SPACE}manière{VK_SPACE}temporaire{VK_SPACE}s'il{VK_SPACE}vous{VK_SPACE}plaît{VK_SPACE}?
                    {ENTER 2}
                    Est-ce{VK_SPACE}que{VK_SPACE}le{VK_SPACE}terrain{VK_SPACE}peut{VK_SPACE}être{VK_SPACE}
                    clôturé{VK_SPACE}avec{VK_SPACE}des{VK_SPACE}grillages,{VK_SPACE}soit{VK_SPACE}des{VK_SPACE}
                    briques,{VK_SPACE}soit{VK_SPACE}des{VK_SPACE}sacs{VK_SPACE}remplis{VK_SPACE}de{VK_SPACE}
                    terre{VK_SPACE}pour{VK_SPACE}protèger{VK_SPACE}les{VK_SPACE}voitures{VK_SPACE}contre{VK_SPACE}
                    le{VK_SPACE}vol,{VK_SPACE}le{VK_SPACE}vandalisme{VK_SPACE}et{VK_SPACE}toutes{VK_SPACE}les{VK_SPACE}
                    situations{VK_SPACE}inconvenables{VK_SPACE}s'il{VK_SPACE}vous{VK_SPACE}plaît{VK_SPACE}?
                    {ENTER 2}
                    Cordialement,
                    """)

            time.sleep(5)

            # Move to the "Envoyer" button
            pywinauto.keyboard.send_keys("{VK_TAB}")

            time.sleep(5)

            # Click tne "Enter" button to send the message
            pywinauto.keyboard.send_keys("{ENTER}")

            time.sleep(10)

            # Close the browser
            pywinauto.keyboard.send_keys('%{F4}')

            time.sleep(10)


class UnitTestsDesktopAutomationLeboncoin1(unittest.TestCase):
    def test_send_message_for_work_office_from_one_ad_with_phone_number(self):
        url_ad = "https://www.leboncoin.fr/ar/?id=1749457525"

        app = Application(backend="uia")

        # Ouvrir l'application Google Chrome
        app.start("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")

        time.sleep(5)

        # Open the Outlook Application
        pywinauto.keyboard.send_keys(url_ad)

        time.sleep(5)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(10)

        # Clik side to the input "Votre nom"
        pywinauto.mouse.click(button='left', coords=(550, 310))

        time.sleep(5)

        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(5)

        # Write my name
        pywinauto.keyboard.send_keys("Mr{VK_SPACE}")

        time.sleep(5)

        # Clik on the input "Votre email"
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(5)

        # Write my email
        pywinauto.keyboard.send_keys("")

        time.sleep(5)

        # Click on the input "Votre message"
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(5)

        # Write my message
        pywinauto.keyboard.send_keys("""
        Bonjour, 
        {ENTER 2}
        Mes{VK_SPACE}questions{VK_SPACE}sont{VK_SPACE}les{VK_SPACE}suivantes{VK_SPACE}:
        {ENTER}
        -{VK_SPACE}Est-ce{VK_SPACE}que{VK_SPACE}le{VK_SPACE}bureau{VK_SPACE}peut{VK_SPACE}être{VK_SPACE}
        utilisé{VK_SPACE}comme{VK_SPACE}siège{VK_SPACE}social{VK_SPACE}s'il{VK_SPACE}vous{VK_SPACE}plaît{VK_SPACE}?
        {ENTER 2}
        -{VK_SPACE}Quel{VK_SPACE}est{VK_SPACE}le{VK_SPACE}montant{VK_SPACE}indicatif{VK_SPACE}de{VK_SPACE}la
        {VK_SPACE}taxe{VK_SPACE}foncière{VK_SPACE}des{VK_SPACE}propriétés{VK_SPACE}bâties{VK_SPACE}pour{VK_SPACE}
        ce{VK_SPACE}bureau{VK_SPACE}s'il{VK_SPACE}vous{VK_SPACE}plaît{VK_SPACE}?
        {ENTER 2}
        -{VK_SPACE}Est-ce{VK_SPACE}que{VK_SPACE}le{VK_SPACE}bureau{VK_SPACE}est{VK_SPACE}équipé{VK_SPACE}
        d'isolation{VK_SPACE}thermique{VK_SPACE}et{VK_SPACE}acoustique{VK_SPACE}s'il{VK_SPACE}vous{VK_SPACE}plaît
        {VK_SPACE}?
        {ENTER 2}
        -{VK_SPACE}Est-ce{VK_SPACE}qu'il{VK_SPACE}y{VK_SPACE}a{VK_SPACE}un{VK_SPACE}compteur{VK_SPACE}
        électrique{VK_SPACE}et{VK_SPACE}un{VK_SPACE}compteur{VK_SPACE}d'eau{VK_SPACE}dans{VK_SPACE}le{VK_SPACE}
        bureau{VK_SPACE}s'il{VK_SPACE}vous{VK_SPACE}plaît{VK_SPACE}?
        {ENTER 2}
        -{VK_SPACE}Est-ce{VK_SPACE}qu'il{VK_SPACE}y{VK_SPACE}a{VK_SPACE}un{VK_SPACE}lavabo{VK_SPACE}et{VK_SPACE}
        un{VK_SPACE}WC{VK_SPACE}dans{VK_SPACE}le{VK_SPACE}bureau{VK_SPACE}s'il{VK_SPACE}vous{VK_SPACE}plaît{VK_SPACE}?
        {ENTER 2}
        -{VK_SPACE}Est-ce{VK_SPACE}qu'il{VK_SPACE}faut{VK_SPACE}déclarer{VK_SPACE}le{VK_SPACE}bureau{VK_SPACE}
        avec{VK_SPACE}le{VK_SPACE}Cerfa{VK_SPACE}n°{VK_SPACE}11213*22{VK_SPACE}pour{VK_SPACE}la{VK_SPACE}taxe
        {VK_SPACE}sur{VK_SPACE}les{VK_SPACE}bureaux{VK_SPACE}en{VK_SPACE}région{VK_SPACE}Ile-de-France{VK_SPACE}
        chaque{VK_SPACE}année{VK_SPACE}s'il{VK_SPACE}vous{VK_SPACE}plaît{VK_SPACE}?
        {ENTER 2}
        Merci{VK_SPACE}pour{VK_SPACE}votre{VK_SPACE}retour.
        {ENTER 2}
        Cordialement,
        """)

        time.sleep(5)

        # Move to the "Envoyer" button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(5)

        # Click tne "Enter" button to send the message
        #pywinauto.keyboard.send_keys("{ENTER}")

        #time.sleep(10)

        #Close the browser
        #pywinauto.keyboard.send_keys('%{F4}')

    def test_send_message_for_work_office_from_a_ad_list_with_phone_number(self):
        urls_ad = [
            "",
            ""
        ]

        for url_ad in urls_ad:

            app = Application(backend="uia")

            # Ouvrir l'application Google Chrome
            app.start("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")

            time.sleep(5)

            # Open the Outlook Application
            pywinauto.keyboard.send_keys(url_ad)

            time.sleep(5)

            # Press the 'Enter' button
            pywinauto.keyboard.send_keys('{ENTER}')

            time.sleep(10)

            # Clik side to the input "Votre nom"
            pywinauto.mouse.click(button='left', coords=(550, 310))

            time.sleep(5)

            pywinauto.keyboard.send_keys("{VK_TAB}")

            time.sleep(5)

            # Write my name
            pywinauto.keyboard.send_keys("Mr{VK_SPACE}")

            time.sleep(5)

            # Clik on the input "Votre email"
            pywinauto.keyboard.send_keys("{VK_TAB}")

            time.sleep(5)

            # Write my email
            pywinauto.keyboard.send_keys(".@outlook.fr")

            time.sleep(5)

            # Click on the input "Votre message"
            pywinauto.keyboard.send_keys("{VK_TAB 2}")

            time.sleep(5)

            # Write my message
            pywinauto.keyboard.send_keys("""
                    Bonjour, 
                    {ENTER 2}
                    Mes{VK_SPACE}questions{VK_SPACE}sont{VK_SPACE}les{VK_SPACE}suivantes{VK_SPACE}:
                    {ENTER}
                    -{VK_SPACE}Est-ce{VK_SPACE}que{VK_SPACE}le{VK_SPACE}bureau{VK_SPACE}peut{VK_SPACE}être{VK_SPACE}
                    utilisé{VK_SPACE}comme{VK_SPACE}siège{VK_SPACE}social{VK_SPACE}s'il{VK_SPACE}vous{VK_SPACE}plaît{VK_SPACE}?
                    {ENTER 2}
                    -{VK_SPACE}Quel{VK_SPACE}est{VK_SPACE}le{VK_SPACE}montant{VK_SPACE}indicatif{VK_SPACE}de{VK_SPACE}la
                    {VK_SPACE}taxe{VK_SPACE}foncière{VK_SPACE}des{VK_SPACE}propriétés{VK_SPACE}bâties{VK_SPACE}pour{VK_SPACE}
                    ce{VK_SPACE}bureau{VK_SPACE}s'il{VK_SPACE}vous{VK_SPACE}plaît{VK_SPACE}?
                    {ENTER 2}
                    -{VK_SPACE}Est-ce{VK_SPACE}que{VK_SPACE}le{VK_SPACE}bureau{VK_SPACE}est{VK_SPACE}équipé{VK_SPACE}
                    d'isolation{VK_SPACE}thermique{VK_SPACE}et{VK_SPACE}acoustique{VK_SPACE}s'il{VK_SPACE}vous{VK_SPACE}plaît
                    {VK_SPACE}?
                    {ENTER 2}
                    -{VK_SPACE}Est-ce{VK_SPACE}qu'il{VK_SPACE}y{VK_SPACE}a{VK_SPACE}un{VK_SPACE}compteur{VK_SPACE}
                    électrique{VK_SPACE}et{VK_SPACE}un{VK_SPACE}compteur{VK_SPACE}d'eau{VK_SPACE}dans{VK_SPACE}le{VK_SPACE}
                    bureau{VK_SPACE}s'il{VK_SPACE}vous{VK_SPACE}plaît{VK_SPACE}?
                    {ENTER 2}
                    -{VK_SPACE}Est-ce{VK_SPACE}qu'il{VK_SPACE}y{VK_SPACE}a{VK_SPACE}un{VK_SPACE}lavabo{VK_SPACE}et{VK_SPACE}
                    un{VK_SPACE}WC{VK_SPACE}dans{VK_SPACE}le{VK_SPACE}bureau{VK_SPACE}s'il{VK_SPACE}vous{VK_SPACE}plaît{VK_SPACE}?
                    {ENTER 2}
                    -{VK_SPACE}Est-ce{VK_SPACE}qu'il{VK_SPACE}faut{VK_SPACE}déclarer{VK_SPACE}le{VK_SPACE}bureau{VK_SPACE}
                    avec{VK_SPACE}le{VK_SPACE}Cerfa{VK_SPACE}n°{VK_SPACE}11213*22{VK_SPACE}pour{VK_SPACE}la{VK_SPACE}taxe
                    {VK_SPACE}sur{VK_SPACE}les{VK_SPACE}bureaux{VK_SPACE}en{VK_SPACE}région{VK_SPACE}Ile-de-France{VK_SPACE}
                    chaque{VK_SPACE}année{VK_SPACE}s'il{VK_SPACE}vous{VK_SPACE}plaît{VK_SPACE}?
                    {ENTER 2}
                    Merci{VK_SPACE}pour{VK_SPACE}votre{VK_SPACE}retour.
                    {ENTER 2}
                    Cordialement,
                    """)

            time.sleep(5)

            # Move to the "Envoyer" button
            pywinauto.keyboard.send_keys("{VK_TAB}")

            time.sleep(5)

            # Click tne "Enter" button to send the message
            pywinauto.keyboard.send_keys("{ENTER}")

            time.sleep(10)

            # Close the browser
            pywinauto.keyboard.send_keys('%{F4}')

            time.sleep(10)

    def test_send_message_for_box_from_one_ad_without_phone_number(self):
        url_ad = "https://www.leboncoin.fr/ar/?id=1742468074"

        app = Application(backend="uia")

        # Ouvrir l'application Google Chrome
        app.start("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")

        time.sleep(5)

        # Open the Outlook Application
        pywinauto.keyboard.send_keys(url_ad)

        time.sleep(5)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(10)

        # Clik on the input "Votre nom"
        pywinauto.mouse.click(button='left', coords=(550, 310))

        time.sleep(5)

        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(5)

        # Write my name
        pywinauto.keyboard.send_keys("Mr{VK_SPACE}")

        time.sleep(5)

        # Clik on the input "Votre email"
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(5)

        # Write my email
        pywinauto.keyboard.send_keys(".@outlook.fr")

        time.sleep(5)

        # Click on the input "Votre message"
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(5)

        # Write my message
        pywinauto.keyboard.send_keys("""
        Bonjour, 
        {ENTER 2}
        Mes{VK_SPACE}questions{VK_SPACE}sont{VK_SPACE}les{VK_SPACE}suivantes{VK_SPACE}:
        {ENTER}
        -{VK_SPACE}Est-ce{VK_SPACE}que{VK_SPACE}le{VK_SPACE}box{VK_SPACE}est{VK_SPACE}acquérable{VK_SPACE}sans
        {VK_SPACE}remise{VK_SPACE}future{VK_SPACE}à{VK_SPACE}une{VK_SPACE}collectivité{VK_SPACE}territoriale
        {VK_SPACE}ou{VK_SPACE}une{VK_SPACE}telle{VK_SPACE}institution{VK_SPACE}publique{VK_SPACE}ou{VK_SPACE}
        privée{VK_SPACE}s'il{VK_SPACE}vous{VK_SPACE}plaît{VK_SPACE}?
        {ENTER 2}
        -{VK_SPACE}Quel{VK_SPACE}est{VK_SPACE}le{VK_SPACE}montant{VK_SPACE}indicatif{VK_SPACE}de{VK_SPACE}la
        {VK_SPACE}taxe{VK_SPACE}foncière{VK_SPACE}des{VK_SPACE}propriétés{VK_SPACE}bâties{VK_SPACE}pour{VK_SPACE}
        ce{VK_SPACE}box{VK_SPACE}s'il{VK_SPACE}vous{VK_SPACE}plaît{VK_SPACE}?
        {ENTER 2}
        -{VK_SPACE}Est-ce{VK_SPACE}qu'il{VK_SPACE}faut{VK_SPACE}déclarer{VK_SPACE}le{VK_SPACE}box{VK_SPACE}
        avec{VK_SPACE}le{VK_SPACE}Cerfa{VK_SPACE}n°{VK_SPACE}11213*22{VK_SPACE}pour{VK_SPACE}la{VK_SPACE}taxe
        {VK_SPACE}sur{VK_SPACE}les{VK_SPACE}bureaux{VK_SPACE}en{VK_SPACE}région{VK_SPACE}Ile-de-France{VK_SPACE}
        chaque{VK_SPACE}année{VK_SPACE}s'il{VK_SPACE}vous{VK_SPACE}plaît{VK_SPACE}?
        {ENTER 2}
        -{VK_SPACE}Est-ce{VK_SPACE}que{VK_SPACE}l'utilisation{VK_SPACE}d'outils{VK_SPACE}bruyants,{VK_SPACE}
        par{VK_SPACE}exemple,{VK_SPACE}une{VK_SPACE}perceuse,{VK_SPACE}une{VK_SPACE}meuleuse,{VK_SPACE}
        un{VK_SPACE}moteur{VK_SPACE}à{VK_SPACE}combustion{VK_SPACE}interne,{VK_SPACE}sur{VK_SPACE}une
        {VK_SPACE}durée{VK_SPACE}indéterminée{VK_SPACE}est{VK_SPACE}tolérée{VK_SPACE}dans{VK_SPACE}le{VK_SPACE}box
        {VK_SPACE}s'il{VK_SPACE}vous{VK_SPACE}plaît{VK_SPACE}?
        {ENTER 2}
        Merci{VK_SPACE}pour{VK_SPACE}votre{VK_SPACE}retour.
        {ENTER 2}
        Cordialement,
        """)

        time.sleep(5)

        # Move to the "Envoyer" button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(5)

        # Click tne "Enter" button to send the message
        pywinauto.keyboard.send_keys("{ENTER}")

        time.sleep(10)

        # Close the browser
        pywinauto.keyboard.send_keys('%{F4}')

    def test_send_message_for_box_from_a_ad_list_without_phone_number(self):
        urls_ad = [
            "https://www.leboncoin.fr/ar/?id=1754977093",
            "https://www.leboncoin.fr/ar/?id=1771039510"
        ]

        for url_ad in urls_ad:
            app = Application(backend="uia")

            # Ouvrir l'application Google Chrome
            app.start("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")

            time.sleep(5)

            # Open the Outlook Application
            pywinauto.keyboard.send_keys(url_ad)

            time.sleep(5)

            # Press the 'Enter' button
            pywinauto.keyboard.send_keys('{ENTER}')

            time.sleep(10)

            # Clik on the input "Votre nom"
            pywinauto.mouse.click(button='left', coords=(550, 323))

            time.sleep(5)

            pywinauto.keyboard.send_keys("{VK_TAB}")

            time.sleep(5)

            # Write my name
            pywinauto.keyboard.send_keys("Mr{VK_SPACE}")

            time.sleep(5)

            # Clik on the input "Votre email"
            pywinauto.keyboard.send_keys("{VK_TAB}")

            time.sleep(5)

            # Write my email
            pywinauto.keyboard.send_keys(".@outlook.fr")

            time.sleep(5)

            # Click on the input "Votre message"
            pywinauto.keyboard.send_keys("{VK_TAB}")

            time.sleep(5)

            # Write my message
            pywinauto.keyboard.send_keys("""
            Bonjour, 
            {ENTER 2}
            Mes{VK_SPACE}questions{VK_SPACE}sont{VK_SPACE}les{VK_SPACE}suivantes{VK_SPACE}:
            {ENTER}
            -{VK_SPACE}Est-ce{VK_SPACE}que{VK_SPACE}le{VK_SPACE}box{VK_SPACE}est{VK_SPACE}acquérable{VK_SPACE}sans
            {VK_SPACE}remise{VK_SPACE}future{VK_SPACE}à{VK_SPACE}une{VK_SPACE}collectivité{VK_SPACE}territoriale
            {VK_SPACE}ou{VK_SPACE}une{VK_SPACE}telle{VK_SPACE}institution{VK_SPACE}publique{VK_SPACE}ou{VK_SPACE}
            privée{VK_SPACE}s'il{VK_SPACE}vous{VK_SPACE}plaît{VK_SPACE}?
            {ENTER 2}
            -{VK_SPACE}Quel{VK_SPACE}est{VK_SPACE}le{VK_SPACE}montant{VK_SPACE}indicatif{VK_SPACE}de{VK_SPACE}la
            {VK_SPACE}taxe{VK_SPACE}foncière{VK_SPACE}des{VK_SPACE}propriétés{VK_SPACE}bâties{VK_SPACE}pour{VK_SPACE}
            ce{VK_SPACE}box{VK_SPACE}s'il{VK_SPACE}vous{VK_SPACE}plaît{VK_SPACE}?
            {ENTER 2}
            -{VK_SPACE}Est-ce{VK_SPACE}qu'il{VK_SPACE}faut{VK_SPACE}déclarer{VK_SPACE}le{VK_SPACE}box{VK_SPACE}
            avec{VK_SPACE}le{VK_SPACE}Cerfa{VK_SPACE}n°{VK_SPACE}11213*22{VK_SPACE}pour{VK_SPACE}la{VK_SPACE}taxe
            {VK_SPACE}sur{VK_SPACE}les{VK_SPACE}bureaux{VK_SPACE}en{VK_SPACE}région{VK_SPACE}Ile-de-France{VK_SPACE}
            chaque{VK_SPACE}année{VK_SPACE}s'il{VK_SPACE}vous{VK_SPACE}plaît{VK_SPACE}?
            {ENTER 2}
            -{VK_SPACE}Est-ce{VK_SPACE}que{VK_SPACE}l'utilisation{VK_SPACE}d'outils{VK_SPACE}bruyants,{VK_SPACE}
            par{VK_SPACE}exemple,{VK_SPACE}une{VK_SPACE}perceuse,{VK_SPACE}une{VK_SPACE}meuleuse,{VK_SPACE}
            un{VK_SPACE}moteur{VK_SPACE}à{VK_SPACE}combustion{VK_SPACE}interne,{VK_SPACE}sur{VK_SPACE}une
            {VK_SPACE}durée{VK_SPACE}indéterminée{VK_SPACE}est{VK_SPACE}tolérée{VK_SPACE}dans{VK_SPACE}le{VK_SPACE}box
            {VK_SPACE}s'il{VK_SPACE}vous{VK_SPACE}plaît{VK_SPACE}?
            {ENTER 2}
            Merci{VK_SPACE}pour{VK_SPACE}votre{VK_SPACE}retour.
            {ENTER 2}
            Cordialement,
            """)

            time.sleep(5)

            # Move to the "Envoyer" button
            pywinauto.keyboard.send_keys("{VK_TAB}")

            time.sleep(5)

            # Click tne "Enter" button to send the message
            pywinauto.keyboard.send_keys("{ENTER}")

            time.sleep(10)

            # Close the browser
            pywinauto.keyboard.send_keys('%{F4}')

    def test_send_message_for_single_room_from_one_ad_without_phone_number(self):
        url_ad = "https://www.leboncoin.fr/ar/?id=1797390700"

        app = Application(backend="uia")

        # Ouvrir l'application Google Chrome
        app.start("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")

        time.sleep(5)

        # Open the Outlook Application
        pywinauto.keyboard.send_keys(url_ad)

        time.sleep(5)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(10)

        # Clik side to the input "Votre nom"
        pywinauto.mouse.click(button='left', coords=(550, 335))

        time.sleep(5)

        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(5)

        # Write my name
        pywinauto.keyboard.send_keys("Mr{VK_SPACE}")

        time.sleep(5)

        # Clik on the input "Votre email"
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(5)

        # Write my email
        pywinauto.keyboard.send_keys(".@outlook.fr")

        time.sleep(5)

        #Click on the input "Votre message"
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(5)

        # Write my message
        pywinauto.keyboard.send_keys("""
        Bonjour, 
        {ENTER 2}
        Est-ce{VK_SPACE}que{VK_SPACE}le{VK_SPACE}bien{VK_SPACE}peut{VK_SPACE}être{VK_SPACE}utilisé{VK_SPACE}
        comme{VK_SPACE}siège{VK_SPACE}social{VK_SPACE}d'une{VK_SPACE}société{VK_SPACE}s'il{VK_SPACE}vous{VK_SPACE}
        plaît{VK_SPACE}?
        {ENTER 2}
        Cordialement,
        """)

        time.sleep(5)

        # Move to the "Envoyer" button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(5)

        # Click tne "Enter" button to send the message
        pywinauto.keyboard.send_keys("{ENTER}")

        time.sleep(10)

        #Close the browser
        pywinauto.keyboard.send_keys('%{F4}')

    def test_send_message_for_signle_room_from_a_ad_list_without_phone_number(self):
        urls_ad = [
            "",
        ]

        for url_ad in urls_ad:

            app = Application(backend="uia")

            # Ouvrir l'application Google Chrome
            app.start("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")

            time.sleep(5)

            # Open the Outlook Application
            pywinauto.keyboard.send_keys(url_ad)

            time.sleep(5)

            # Press the 'Enter' button
            pywinauto.keyboard.send_keys('{ENTER}')

            time.sleep(10)

            # Clik side to the input "Votre nom"
            pywinauto.mouse.click(button='left', coords=(550, 335))

            time.sleep(5)

            pywinauto.keyboard.send_keys("{VK_TAB}")

            time.sleep(5)

            # Write my name
            pywinauto.keyboard.send_keys("Mr{VK_SPACE}")

            time.sleep(5)

            # Clik on the input "Votre email"
            pywinauto.keyboard.send_keys("{VK_TAB}")

            time.sleep(5)

            # Write my email
            pywinauto.keyboard.send_keys(".@outlook.fr")

            time.sleep(5)

            # Click on the input "Votre message"
            pywinauto.keyboard.send_keys("{VK_TAB}")

            time.sleep(5)

            # Write my message
            pywinauto.keyboard.send_keys("""
                    Bonjour, 
                    {ENTER 2}
                    Est-ce{VK_SPACE}que{VK_SPACE}le{VK_SPACE}bien{VK_SPACE}peut{VK_SPACE}être{VK_SPACE}utilisé{VK_SPACE}
                    comme{VK_SPACE}siège{VK_SPACE}social{VK_SPACE}d'une{VK_SPACE}société{VK_SPACE}s'il{VK_SPACE}vous{VK_SPACE}
                    plaît{VK_SPACE}?
                    {ENTER 2}
                    Cordialement,
                    """)

            time.sleep(5)

            # Move to the "Envoyer" button
            pywinauto.keyboard.send_keys("{VK_TAB}")

            time.sleep(5)

            # Click tne "Enter" button to send the message
            pywinauto.keyboard.send_keys("{ENTER}")

            time.sleep(10)

            # Close the browser
            pywinauto.keyboard.send_keys('%{F4}')

            time.sleep(10)

    def test_send_message_for_signle_room_from_a_ad_list_with_phone_number(self):
        urls_ad = [
            "",
        ]

        for url_ad in urls_ad:

            app = Application(backend="uia")

            # Ouvrir l'application Google Chrome
            app.start("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")

            time.sleep(5)

            # Open the Outlook Application
            pywinauto.keyboard.send_keys(url_ad)

            time.sleep(5)

            # Press the 'Enter' button
            pywinauto.keyboard.send_keys('{ENTER}')

            time.sleep(10)

            # Clik side to the input "Votre nom"
            pywinauto.mouse.click(button='left', coords=(550, 200))

            time.sleep(5)

            pywinauto.keyboard.send_keys("{VK_TAB}")

            time.sleep(5)

            # Write my name
            pywinauto.keyboard.send_keys("Mr{VK_SPACE}")

            time.sleep(5)

            # Clik on the input "Votre email"
            pywinauto.keyboard.send_keys("{VK_TAB}")

            time.sleep(5)

            # Write my email
            pywinauto.keyboard.send_keys(".@outlook.fr")

            time.sleep(5)

            # Click on the input "Votre message"
            pywinauto.keyboard.send_keys("{VK_TAB 2}")

            time.sleep(5)

            # Write my message
            pywinauto.keyboard.send_keys("""
                    Bonjour, 
                    {ENTER 2}
                    Est-ce{VK_SPACE}que{VK_SPACE}le{VK_SPACE}bien{VK_SPACE}peut{VK_SPACE}être{VK_SPACE}utilisé{VK_SPACE}
                    comme{VK_SPACE}siège{VK_SPACE}social{VK_SPACE}d'une{VK_SPACE}société{VK_SPACE}s'il{VK_SPACE}vous{VK_SPACE}
                    plaît{VK_SPACE}?
                    {ENTER 2}
                    Cordialement,
                    """)

            time.sleep(5)

            # Move to the "Envoyer" button
            pywinauto.keyboard.send_keys("{VK_TAB}")

            time.sleep(5)

            # Click tne "Enter" button to send the message
            pywinauto.keyboard.send_keys("{ENTER}")

            time.sleep(10)

            # Close the browser
            pywinauto.keyboard.send_keys('%{F4}')

            time.sleep(10)

    def test_send_message_for_cave_from_a_list_of_ad_with_phone_number_for_electricity_station(self):
        url_ads = [
        ]

        for url_ad in url_ads:
            time.sleep(5)

            app = Application(backend="uia")

            # Ouvrir l'application Google Chrome
            app.start("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")

            time.sleep(5)

            # Open the Outlook Application
            pywinauto.keyboard.send_keys(url_ad)

            time.sleep(5)

            print(url_ad)

            time.sleep(5)

            # Press the 'Enter' button
            pywinauto.keyboard.send_keys('{ENTER}')

            time.sleep(10)

            # Clik side to the input "Votre nom"
            pywinauto.mouse.click(button='left', coords=(550, 310))

            time.sleep(5)

            pywinauto.keyboard.send_keys("{VK_TAB}")

            time.sleep(5)

            # Write my name
            pywinauto.keyboard.send_keys("Mr{VK_SPACE}")

            time.sleep(5)

            # Clik on the input "Votre email"
            pywinauto.keyboard.send_keys("{VK_TAB}")

            time.sleep(5)

            # Write my email
            pywinauto.keyboard.send_keys(".@outlook.fr")

            time.sleep(5)

            #Click on the input "Votre message"
            pywinauto.keyboard.send_keys("{VK_TAB 2}")

            time.sleep(5)

            # Write my message
            pywinauto.keyboard.send_keys("""
            Bonjour, 
            {ENTER 2}
            Est-ce{VK_SPACE}que{VK_SPACE}la{VK_SPACE}copropriété{VK_SPACE}est{VK_SPACE}d'accord{VK_SPACE}que{VK_SPACE}
            la{VK_SPACE}cave{VK_SPACE}soit{VK_SPACE}utilisée{VK_SPACE}pour{VK_SPACE}une{VK_SPACE}installation{VK_SPACE}
            de{VK_SPACE}production{VK_SPACE}d'électricité{VK_SPACE}en{VK_SPACE}vertu{VK_SPACE}du{VK_SPACE}3°{VK_SPACE}
            de{VK_SPACE}l'article{VK_SPACE}R311-2{VK_SPACE}du{VK_SPACE}Code{VK_SPACE}de{VK_SPACE}l'énergie{VK_SPACE}
            de{VK_SPACE}la{VK_SPACE}loi{VK_SPACE}française{VK_SPACE}s'il{VK_SPACE}vous{VK_SPACE}plaît{VK_SPACE}?
            {ENTER 2}
            Le{VK_SPACE}combustible{VK_SPACE}sera{VK_SPACE}l'hydrogène{VK_SPACE}gazeux.
            {ENTER 2}
            L'installation{VK_SPACE}sera{VK_SPACE}équipée{VK_SPACE}d'un{VK_SPACE}moteur{VK_SPACE}thermique{VK_SPACE}
            à{VK_SPACE}combustion{VK_SPACE}interne{VK_SPACE}à{VK_SPACE}piston.
            {ENTER 2}
            Est-ce{VK_SPACE}que{VK_SPACE}le{VK_SPACE}raccordement{VK_SPACE}au{VK_SPACE}réseau{VK_SPACE}public{VK_SPACE}
            d'électricité{VK_SPACE}en{VK_SPACE}vertu{VK_SPACE}des{VK_SPACE}articles{VK_SPACE}L341-1{VK_SPACE}à{VK_SPACE}
            L342-12{VK_SPACE}et{VK_SPACE}suivants{VK_SPACE}du{VK_SPACE}Code{VK_SPACE}de{VK_SPACE}l'énergie{VK_SPACE}
            de{VK_SPACE}la{VK_SPACE}loi{VK_SPACE}française{VK_SPACE}est{VK_SPACE}possible{VK_SPACE}depuis{VK_SPACE}
            cette{VK_SPACE}cave{VK_SPACE}s'il{VK_SPACE}vous{VK_SPACE}plaît{VK_SPACE}?
            {ENTER 2}
            Est-ce{VK_SPACE}que{VK_SPACE}vous{VK_SPACE}pourriez{VK_SPACE}m'envoyer{VK_SPACE}le{VK_SPACE}
            contact{VK_SPACE}de{VK_SPACE}la{VK_SPACE}copropriété{VK_SPACE}s'il{VK_SPACE}vous{VK_SPACE}plaît{VK_SPACE}?
            {ENTER 2}
            Ainsi,{VK_SPACE}je{VK_SPACE}vous{VK_SPACE}prie{VK_SPACE}de{VK_SPACE}m'adresser{VK_SPACE}vos{VK_SPACE}
            questions{VK_SPACE}et{VK_SPACE}vos{VK_SPACE}attentes{VK_SPACE}s'il{VK_SPACE}vous{VK_SPACE}plaît.
            {ENTER 2}
            Cordialement,
            """)

            time.sleep(5)

            # Move to the "Envoyer" button
            pywinauto.keyboard.send_keys("{VK_TAB}")

            time.sleep(5)

            # Click tne "Enter" button to send the message
            pywinauto.keyboard.send_keys("{ENTER}")

            time.sleep(10)

            #Close the browser
            pywinauto.keyboard.send_keys('%{F4}')

    def test_send_message_for_cave_from_a_list_of_ad_without_phone_number_for_electricity_station(self):
        url_ads = [
        ]

        for url_ad in url_ads:
            time.sleep(5)

            app = Application(backend="uia")

            # Ouvrir l'application Google Chrome
            app.start("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")

            time.sleep(5)

            # Open the Outlook Application
            pywinauto.keyboard.send_keys(url_ad)

            time.sleep(5)

            print(url_ad)

            time.sleep(5)

            # Press the 'Enter' button
            pywinauto.keyboard.send_keys('{ENTER}')

            time.sleep(12)

            # Clik side to the input "Votre nom"
            pywinauto.mouse.click(button='left', coords=(550, 360))

            time.sleep(5)

            pywinauto.keyboard.send_keys("{VK_TAB}")

            time.sleep(5)

            # Write my name
            pywinauto.keyboard.send_keys("Mr{VK_SPACE}")

            time.sleep(5)

            # Clik on the input "Votre email"
            pywinauto.keyboard.send_keys("{VK_TAB}")

            time.sleep(5)

            # Write my email
            pywinauto.keyboard.send_keys(".@outlook.fr")

            time.sleep(5)

            #Click on the input "Votre message"
            pywinauto.keyboard.send_keys("{VK_TAB}")

            time.sleep(5)

            # Write my message
            pywinauto.keyboard.send_keys("""
            Bonjour, 
            {ENTER 2}
            Est-ce{VK_SPACE}que{VK_SPACE}la{VK_SPACE}copropriété{VK_SPACE}est{VK_SPACE}d'accord{VK_SPACE}que{VK_SPACE}
            la{VK_SPACE}cave{VK_SPACE}soit{VK_SPACE}utilisée{VK_SPACE}pour{VK_SPACE}une{VK_SPACE}installation{VK_SPACE}
            de{VK_SPACE}production{VK_SPACE}d'électricité{VK_SPACE}en{VK_SPACE}vertu{VK_SPACE}du{VK_SPACE}3°{VK_SPACE}
            de{VK_SPACE}l'article{VK_SPACE}R311-2{VK_SPACE}du{VK_SPACE}Code{VK_SPACE}de{VK_SPACE}l'énergie{VK_SPACE}
            de{VK_SPACE}la{VK_SPACE}loi{VK_SPACE}française{VK_SPACE}s'il{VK_SPACE}vous{VK_SPACE}plaît{VK_SPACE}?
            {ENTER 2}
            Le{VK_SPACE}combustible{VK_SPACE}sera{VK_SPACE}l'hydrogène{VK_SPACE}gazeux.
            {ENTER 2}
            L'installation{VK_SPACE}sera{VK_SPACE}équipée{VK_SPACE}d'un{VK_SPACE}moteur{VK_SPACE}thermique{VK_SPACE}
            à{VK_SPACE}combustion{VK_SPACE}interne{VK_SPACE}à{VK_SPACE}piston.
            {ENTER 2}
            Est-ce{VK_SPACE}que{VK_SPACE}le{VK_SPACE}raccordement{VK_SPACE}au{VK_SPACE}réseau{VK_SPACE}public{VK_SPACE}
            d'électricité{VK_SPACE}en{VK_SPACE}vertu{VK_SPACE}des{VK_SPACE}articles{VK_SPACE}L341-1{VK_SPACE}à{VK_SPACE}
            L342-12{VK_SPACE}et{VK_SPACE}suivants{VK_SPACE}du{VK_SPACE}Code{VK_SPACE}de{VK_SPACE}l'énergie{VK_SPACE}
            de{VK_SPACE}la{VK_SPACE}loi{VK_SPACE}française{VK_SPACE}est{VK_SPACE}possible{VK_SPACE}depuis{VK_SPACE}
            cette{VK_SPACE}cave{VK_SPACE}s'il{VK_SPACE}vous{VK_SPACE}plaît{VK_SPACE}?
            {ENTER 2}
            Est-ce{VK_SPACE}que{VK_SPACE}vous{VK_SPACE}pourriez{VK_SPACE}m'envoyer{VK_SPACE}le{VK_SPACE}
            contact{VK_SPACE}de{VK_SPACE}la{VK_SPACE}copropriété{VK_SPACE}s'il{VK_SPACE}vous{VK_SPACE}plaît{VK_SPACE}?
            {ENTER 2}
            Ainsi,{VK_SPACE}je{VK_SPACE}vous{VK_SPACE}prie{VK_SPACE}de{VK_SPACE}m'adresser{VK_SPACE}vos{VK_SPACE}
            questions{VK_SPACE}et{VK_SPACE}vos{VK_SPACE}attentes{VK_SPACE}s'il{VK_SPACE}vous{VK_SPACE}plaît.
            {ENTER 2}
            Cordialement,
            """)

            time.sleep(5)

            # Move to the "Envoyer" button
            pywinauto.keyboard.send_keys("{VK_TAB}")

            time.sleep(5)

            # Click tne "Enter" button to send the message
            pywinauto.keyboard.send_keys("{ENTER}")

            time.sleep(10)

            #Close the browser
            pywinauto.keyboard.send_keys('%{F4}')

    def test_send_message_for_home_for_etablishing_school_from_a_ad_list_without_phone_number(self):
        urls_ad = [
        ]

        for url_ad in urls_ad:

            app = Application(backend="uia")

            # Ouvrir l'application Google Chrome
            app.start("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")

            time.sleep(5)

            # Open the Outlook Application
            pywinauto.keyboard.send_keys(url_ad)

            time.sleep(5)

            # Press the 'Enter' button
            pywinauto.keyboard.send_keys('{ENTER}')

            time.sleep(10)

            # Clik side to the input "Votre nom"
            pywinauto.mouse.click(button='left', coords=(550, 335))

            time.sleep(5)

            pywinauto.keyboard.send_keys("{VK_TAB}")

            time.sleep(5)

            # Write my name
            pywinauto.keyboard.send_keys("Mr{VK_SPACE}")

            time.sleep(5)

            # Clik on the input "Votre email"
            pywinauto.keyboard.send_keys("{VK_TAB}")

            time.sleep(5)

            # Write my email
            pywinauto.keyboard.send_keys(".@outlook.fr")

            time.sleep(5)

            # Click on the input "Votre message"
            pywinauto.keyboard.send_keys("{VK_TAB}")

            time.sleep(5)

            # Write my message
            pywinauto.keyboard.send_keys("""
                    Bonjour, 
                    {ENTER 2}
                    Est-ce{VK_SPACE}que{VK_SPACE}le{VK_SPACE}bien{VK_SPACE}peut{VK_SPACE}être
                    {VK_SPACE}utilisé{VK_SPACE}pour{VK_SPACE}ouvrir{VK_SPACE}un{VK_SPACE}établissement
                    {VK_SPACE}d'enseignement{VK_SPACE}supérieur{VK_SPACE}privé{VK_SPACE}délivrant{VK_SPACE}un
                    {VK_SPACE}diplôme{VK_SPACE}conférant{VK_SPACE}un{VK_SPACE}grade{VK_SPACE}de{VK_SPACE}
                    master{VK_SPACE}s'il{VK_SPACE}vous{VK_SPACE}plaît{VK_SPACE}?
                    {ENTER 2}
                    Cet{VK_SPACE}établissement{VK_SPACE}devra{VK_SPACE}être{VK_SPACE}une{VK_SPACE}école
                    {VK_SPACE}d'ingénieur
                    {VK_SPACE}orientée{VK_SPACE}vers{VK_SPACE}le{VK_SPACE}domaine{VK_SPACE}de{VK_SPACE}l'énergie.
                    {ENTER 2}
                    Est-ce{VK_SPACE}que{VK_SPACE}le{VK_SPACE}bien{VK_SPACE}est{VK_SPACE}proche{VK_SPACE}d'un{VK_SPACE}
                    transport{VK_SPACE}en{VK_SPACE}commun{VK_SPACE}en{VK_SPACE}direction{VK_SPACE}du{VK_SPACE}
                    centre-ville{VK_SPACE}s'il{VK_SPACE}vous{VK_SPACE}plaît{VK_SPACE}?
                    {ENTER 2}
                    Cordialement,
                    """)

            time.sleep(5)

            # Move to the "Envoyer" button
            pywinauto.keyboard.send_keys("{VK_TAB}")

            time.sleep(5)

            # Click tne "Enter" button to send the message
            pywinauto.keyboard.send_keys("{ENTER}")

            time.sleep(10)

            # Close the browser
            pywinauto.keyboard.send_keys('%{F4}')

            time.sleep(10)

    def test_send_message_for_home_for_etablishing_school_from_a_ad_list_with_phone_number(self):
        urls_ad = [

        ]

        for url_ad in urls_ad:

            app = Application(backend="uia")

            # Ouvrir l'application Google Chrome
            app.start("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")

            time.sleep(5)

            # Open the Outlook Application
            pywinauto.keyboard.send_keys(url_ad)

            time.sleep(5)

            # Press the 'Enter' button
            pywinauto.keyboard.send_keys('{ENTER}')

            time.sleep(10)

            # Clik side to the input "Votre nom"
            pywinauto.mouse.click(button='left', coords=(550, 200))

            time.sleep(5)

            pywinauto.keyboard.send_keys("{VK_TAB}")

            time.sleep(5)

            # Write my name
            pywinauto.keyboard.send_keys("Mr{VK_SPACE}")

            time.sleep(5)

            # Clik on the input "Votre email"
            pywinauto.keyboard.send_keys("{VK_TAB}")

            time.sleep(5)

            # Write my email
            pywinauto.keyboard.send_keys(".@outlook.fr")

            time.sleep(5)

            # Click on the input "Votre message"
            pywinauto.keyboard.send_keys("{VK_TAB 2}")

            time.sleep(5)

            # Write my message
            pywinauto.keyboard.send_keys("""
                    Bonjour, 
                    {ENTER 2}
                    Est-ce{VK_SPACE}que{VK_SPACE}le{VK_SPACE}bien{VK_SPACE}peut{VK_SPACE}être
                    {VK_SPACE}utilisé{VK_SPACE}pour{VK_SPACE}ouvrir{VK_SPACE}un{VK_SPACE}établissement
                    {VK_SPACE}d'enseignement{VK_SPACE}supérieur{VK_SPACE}privé{VK_SPACE}délivrant{VK_SPACE}un
                    {VK_SPACE}diplôme{VK_SPACE}conférant{VK_SPACE}un{VK_SPACE}grade{VK_SPACE}de{VK_SPACE}
                    master{VK_SPACE}s'il{VK_SPACE}vous{VK_SPACE}plaît{VK_SPACE}?
                    {ENTER 2}
                    Cet{VK_SPACE}établissement{VK_SPACE}devra{VK_SPACE}être{VK_SPACE}une{VK_SPACE}
                    école{VK_SPACE}d'ingénieur
                    {VK_SPACE}orientée{VK_SPACE}vers{VK_SPACE}le{VK_SPACE}domaine{VK_SPACE}de{VK_SPACE}l'énergie.
                    {ENTER 2}
                    Est-ce{VK_SPACE}que{VK_SPACE}le{VK_SPACE}bien{VK_SPACE}est{VK_SPACE}proche{VK_SPACE}d'un{VK_SPACE}
                    transport{VK_SPACE}en{VK_SPACE}commun{VK_SPACE}en{VK_SPACE}direction{VK_SPACE}du{VK_SPACE}
                    centre-ville{VK_SPACE}s'il{VK_SPACE}vous{VK_SPACE}plaît{VK_SPACE}?
                    {ENTER 2}
                    Cordialement,
                    """)

            time.sleep(5)

            # Move to the "Envoyer" button
            pywinauto.keyboard.send_keys("{VK_TAB}")

            time.sleep(5)

            # Click tne "Enter" button to send the message
            pywinauto.keyboard.send_keys("{ENTER}")

            time.sleep(10)

            # Close the browser
            pywinauto.keyboard.send_keys('%{F4}')

            time.sleep(10)

    def test_send_message_for_land_for_etablishing_prison_from_a_ad_list_without_phone_number(self):
        urls_ad = [
        ]

        for url_ad in urls_ad:
            app = Application(backend="uia")

            # Ouvrir l'application Google Chrome
            app.start("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")

            time.sleep(5)

            # Open the Outlook Application
            pywinauto.keyboard.send_keys(url_ad)

            time.sleep(5)

            # Press the 'Enter' button
            pywinauto.keyboard.send_keys('{ENTER}')

            time.sleep(10)

            # Clik side to the input "Votre nom"
            pywinauto.mouse.click(button='left', coords=(550, 335))

            time.sleep(5)

            pywinauto.keyboard.send_keys("{VK_TAB}")

            time.sleep(5)

            # Write my name
            pywinauto.keyboard.send_keys("Mr{VK_SPACE}")

            time.sleep(5)

            # Clik on the input "Votre email"
            pywinauto.keyboard.send_keys("{VK_TAB}")

            time.sleep(5)

            # Write my email
            pywinauto.keyboard.send_keys(".@outlook.fr")

            time.sleep(5)

            # Click on the input "Votre message"
            pywinauto.keyboard.send_keys("{VK_TAB}")

            time.sleep(5)

            # Write my message
            pywinauto.keyboard.send_keys("""
                    Bonjour, 
                    {ENTER 2}
                    Est-ce{VK_SPACE}que{VK_SPACE}le{VK_SPACE}terrain{VK_SPACE}peut{VK_SPACE}être{VK_SPACE}utilisé
                    {VK_SPACE}pour{VK_SPACE}construire{VK_SPACE}une{VK_SPACE}prison{VK_SPACE}en{VK_SPACE}
                    vertu{VK_SPACE}de{VK_SPACE}l'article{VK_SPACE}1382{VK_SPACE}du{VK_SPACE}Code{VK_SPACE}général
                    {VK_SPACE}des{VK_SPACE}impôts{VK_SPACE}s'il{VK_SPACE}vous{VK_SPACE}plaît{VK_SPACE}?
                    {ENTER 2}
                    En{VK_SPACE}combien{VK_SPACE}de{VK_SPACE}temps{VK_SPACE}pouvons-nous{VK_SPACE}
                    atteindre{VK_SPACE}l'hôpital{VK_SPACE}le{VK_SPACE}plus{VK_SPACE}proche{VK_SPACE}en{VK_SPACE}
                    voiture{VK_SPACE}depuis{VK_SPACE}le{VK_SPACE}terrain{VK_SPACE}s'il{VK_SPACE}vous{VK_SPACE}
                    plaît{VK_SPACE}?
                    {ENTER 2}
                    Est-ce{VK_SPACE}qu'il{VK_SPACE}y{VK_SPACE}a{VK_SPACE}des{VK_SPACE}transports{VK_SPACE}
                    en{VK_SPACE}commun{VK_SPACE}proche{VK_SPACE}du{VK_SPACE}terrain{VK_SPACE}en{VK_SPACE}
                    direction{VK_SPACE}du{VK_SPACE}centre-ville{VK_SPACE}s'il{VK_SPACE}vous{VK_SPACE}plaît{VK_SPACE}?
                    {ENTER 2}
                    Bien{VK_SPACE}cordialement,
                    """)

            time.sleep(5)

            # Move to the "Envoyer" button
            pywinauto.keyboard.send_keys("{VK_TAB}")

            time.sleep(5)

            # Click tne "Enter" button to send the message
            pywinauto.keyboard.send_keys("{ENTER}")

            time.sleep(10)

            # Close the browser
            pywinauto.keyboard.send_keys('%{F4}')

            time.sleep(10)

    def test_send_message_for_land_for_etablishing_prison_from_a_ad_list_with_phone_number(self):
        urls_ad = [
            ""
        ]

        for url_ad in urls_ad:
            app = Application(backend="uia")

            # Ouvrir l'application Google Chrome
            app.start("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")

            time.sleep(5)

            # Open the Outlook Application
            pywinauto.keyboard.send_keys(url_ad)

            time.sleep(5)

            # Press the 'Enter' button
            pywinauto.keyboard.send_keys('{ENTER}')

            time.sleep(10)

            # Clik side to the input "Votre nom"
            pywinauto.mouse.click(button='left', coords=(550, 200))

            time.sleep(5)

            pywinauto.keyboard.send_keys("{VK_TAB}")

            time.sleep(5)

            # Write my name
            pywinauto.keyboard.send_keys("Mr{VK_SPACE}")

            time.sleep(5)

            # Clik on the input "Votre email"
            pywinauto.keyboard.send_keys("{VK_TAB}")

            time.sleep(5)

            # Write my email
            pywinauto.keyboard.send_keys(".@outlook.fr")

            time.sleep(5)

            # Click on the input "Votre message"
            pywinauto.keyboard.send_keys("{VK_TAB 2}")

            time.sleep(5)

            # Write my message
            pywinauto.keyboard.send_keys("""
                    Bonjour, 
                    {ENTER 2}
                    Est-ce{VK_SPACE}que{VK_SPACE}le{VK_SPACE}terrain{VK_SPACE}peut{VK_SPACE}être{VK_SPACE}utilisé
                    {VK_SPACE}pour{VK_SPACE}construire{VK_SPACE}une{VK_SPACE}prison{VK_SPACE}en{VK_SPACE}
                    vertu{VK_SPACE}de{VK_SPACE}l'article{VK_SPACE}1382{VK_SPACE}du{VK_SPACE}Code{VK_SPACE}général
                    {VK_SPACE}des{VK_SPACE}impôts{VK_SPACE}s'il{VK_SPACE}vous{VK_SPACE}plaît{VK_SPACE}?
                    {ENTER 2}
                    En{VK_SPACE}combien{VK_SPACE}de{VK_SPACE}temps{VK_SPACE}pouvons-nous{VK_SPACE}
                    atteindre{VK_SPACE}l'hôpital{VK_SPACE}le{VK_SPACE}plus{VK_SPACE}proche{VK_SPACE}en{VK_SPACE}
                    voiture{VK_SPACE}depuis{VK_SPACE}le{VK_SPACE}terrain{VK_SPACE}s'il{VK_SPACE}vous{VK_SPACE}
                    plaît{VK_SPACE}?
                    {ENTER 2}
                    Est-ce{VK_SPACE}qu'il{VK_SPACE}y{VK_SPACE}a{VK_SPACE}des{VK_SPACE}transports{VK_SPACE}
                    en{VK_SPACE}commun{VK_SPACE}proche{VK_SPACE}du{VK_SPACE}terrain{VK_SPACE}en{VK_SPACE}
                    direction{VK_SPACE}du{VK_SPACE}centre-ville{VK_SPACE}s'il{VK_SPACE}vous{VK_SPACE}plaît{VK_SPACE}?
                    {ENTER 2}
                    Bien{VK_SPACE}cordialement,
                    """)

            time.sleep(5)

            # Move to the "Envoyer" button
            pywinauto.keyboard.send_keys("{VK_TAB}")

            time.sleep(5)

            # Click tne "Enter" button to send the message
            pywinauto.keyboard.send_keys("{ENTER}")

            time.sleep(10)

            # Close the browser
            pywinauto.keyboard.send_keys('%{F4}')

            time.sleep(10)

    def test_send_message_for_land_for_parking_cars_from_a_ad_list_with_phone_number(self):
        urls_ad = [
            ""
        ]

        for url_ad in urls_ad:

            app = Application(backend="uia")

            # Ouvrir l'application Google Chrome
            app.start("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")

            time.sleep(5)

            # Open the Outlook Application
            pywinauto.keyboard.send_keys(url_ad)

            time.sleep(5)

            # Press the 'Enter' button
            pywinauto.keyboard.send_keys('{ENTER}')

            time.sleep(10)

            # Clik side to the input "Votre nom"
            pywinauto.mouse.click(button='left', coords=(550, 200))

            time.sleep(5)

            pywinauto.keyboard.send_keys("{VK_TAB}")

            time.sleep(5)

            # Write my name
            pywinauto.keyboard.send_keys("Mr{VK_SPACE}")

            time.sleep(5)

            # Clik on the input "Votre email"
            pywinauto.keyboard.send_keys("{VK_TAB}")

            time.sleep(5)

            # Write my email
            pywinauto.keyboard.send_keys(".@outlook.fr")

            time.sleep(5)

            # Click on the input "Votre message"
            pywinauto.keyboard.send_keys("{VK_TAB 2}")

            time.sleep(5)

            # Write my message
            pywinauto.keyboard.send_keys("""
                    Bonjour, 
                    {ENTER 2}
                    Est-ce{VK_SPACE}que{VK_SPACE}le{VK_SPACE}terrain{VK_SPACE}peut{VK_SPACE}être
                    {VK_SPACE}utilisé{VK_SPACE}pour{VK_SPACE}stationner{VK_SPACE}des{VK_SPACE}voitures{VK_SPACE}
                    roulantes{VK_SPACE}de{VK_SPACE}manière{VK_SPACE}temporaire{VK_SPACE}s'il{VK_SPACE}vous{VK_SPACE}plaît{VK_SPACE}?
                    {ENTER 2}
                    Est-ce{VK_SPACE}que{VK_SPACE}le{VK_SPACE}terrain{VK_SPACE}peut{VK_SPACE}être{VK_SPACE}
                    clôturé{VK_SPACE}avec{VK_SPACE}des{VK_SPACE}grillages,{VK_SPACE}soit{VK_SPACE}des{VK_SPACE}
                    briques,{VK_SPACE}soit{VK_SPACE}des{VK_SPACE}sacs{VK_SPACE}remplis{VK_SPACE}de{VK_SPACE}
                    terre{VK_SPACE}pour{VK_SPACE}protèger{VK_SPACE}les{VK_SPACE}voitures{VK_SPACE}contre{VK_SPACE}
                    le{VK_SPACE}vol,{VK_SPACE}le{VK_SPACE}vandalisme{VK_SPACE}et{VK_SPACE}toutes{VK_SPACE}les{VK_SPACE}
                    situations{VK_SPACE}inconvenables{VK_SPACE}s'il{VK_SPACE}vous{VK_SPACE}plaît{VK_SPACE}?
                    {ENTER 2}
                    Cordialement,
                    """)

            time.sleep(5)

            # Move to the "Envoyer" button
            pywinauto.keyboard.send_keys("{VK_TAB}")

            time.sleep(5)

            # Click tne "Enter" button to send the message
            pywinauto.keyboard.send_keys("{ENTER}")

            time.sleep(10)

            # Close the browser
            pywinauto.keyboard.send_keys('%{F4}')

            time.sleep(10)

    def test_send_message_for_land_for_parking_cars_from_a_ad_list_without_phone_number(self):
        urls_ad = [

        ]

        for url_ad in urls_ad:
            app = Application(backend="uia")

            # Ouvrir l'application Google Chrome
            app.start("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")

            time.sleep(6)

            # Open the Outlook Application
            pywinauto.keyboard.send_keys(url_ad)

            time.sleep(5)

            # Press the 'Enter' button
            pywinauto.keyboard.send_keys('{ENTER}')

            time.sleep(10)

            # Clik side to the input "Votre nom"
            pywinauto.mouse.click(button='left', coords=(550, 335))

            time.sleep(5)

            pywinauto.keyboard.send_keys("{VK_TAB}")

            time.sleep(5)

            # Write my name
            pywinauto.keyboard.send_keys("Mr{VK_SPACE}")

            time.sleep(5)

            # Clik on the input "Votre email"
            pywinauto.keyboard.send_keys("{VK_TAB}")

            time.sleep(5)

            # Write my email
            pywinauto.keyboard.send_keys(".@outlook.fr")

            time.sleep(5)

            # Click on the input "Votre message"
            pywinauto.keyboard.send_keys("{VK_TAB}")

            time.sleep(5)

            # Write my message
            pywinauto.keyboard.send_keys("""
                    Bonjour, 
                    {ENTER 2}
                    Est-ce{VK_SPACE}que{VK_SPACE}le{VK_SPACE}terrain{VK_SPACE}peut{VK_SPACE}être
                    {VK_SPACE}utilisé{VK_SPACE}pour{VK_SPACE}stationner{VK_SPACE}des{VK_SPACE}voitures{VK_SPACE}
                    roulantes{VK_SPACE}de{VK_SPACE}manière{VK_SPACE}temporaire{VK_SPACE}s'il{VK_SPACE}vous{VK_SPACE}plaît{VK_SPACE}?
                    {ENTER 2}
                    Est-ce{VK_SPACE}que{VK_SPACE}le{VK_SPACE}terrain{VK_SPACE}peut{VK_SPACE}être{VK_SPACE}
                    clôturé{VK_SPACE}avec{VK_SPACE}des{VK_SPACE}grillages,{VK_SPACE}soit{VK_SPACE}des{VK_SPACE}
                    briques,{VK_SPACE}soit{VK_SPACE}des{VK_SPACE}sacs{VK_SPACE}remplis{VK_SPACE}de{VK_SPACE}
                    terre{VK_SPACE}pour{VK_SPACE}protèger{VK_SPACE}les{VK_SPACE}voitures{VK_SPACE}contre{VK_SPACE}
                    le{VK_SPACE}vol,{VK_SPACE}le{VK_SPACE}vandalisme{VK_SPACE}et{VK_SPACE}toutes{VK_SPACE}les{VK_SPACE}
                    situations{VK_SPACE}inconvenables{VK_SPACE}s'il{VK_SPACE}vous{VK_SPACE}plaît{VK_SPACE}?
                    {ENTER 2}
                    Cordialement,
                    """)

            time.sleep(5)

            # Move to the "Envoyer" button
            pywinauto.keyboard.send_keys("{VK_TAB}")

            time.sleep(5)

            # Click tne "Enter" button to send the message
            pywinauto.keyboard.send_keys("{ENTER}")

            time.sleep(10)

            # Close the browser
            pywinauto.keyboard.send_keys('%{F4}')

            time.sleep(10)

    def test_send_message_for_buying_cars_from_a_ad_list_with_phone_number(self):
        urls_ad = [
            ""
        ]

        for url_ad in urls_ad:
            app = Application(backend="uia")

            # Ouvrir l'application Google Chrome
            app.start("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")

            time.sleep(5)

            # Open the Outlook Application
            pywinauto.keyboard.send_keys(url_ad)

            time.sleep(5)

            # Press the 'Enter' button
            pywinauto.keyboard.send_keys('{ENTER}')

            time.sleep(10)

            # Clik side to the input "Votre nom"
            pywinauto.mouse.click(button='left', coords=(550, 200))

            time.sleep(5)

            pywinauto.keyboard.send_keys("{VK_TAB}")

            time.sleep(5)

            # Write my name
            pywinauto.keyboard.send_keys("Mr{VK_SPACE}")

            time.sleep(5)

            # Clik on the input "Votre email"
            pywinauto.keyboard.send_keys("{VK_TAB}")

            time.sleep(5)

            # Write my email
            pywinauto.keyboard.send_keys(".@outlook.fr")

            time.sleep(5)

            # Click on the input "Votre message"
            pywinauto.keyboard.send_keys("{VK_TAB 2}")

            time.sleep(5)

            # Write my message
            pywinauto.keyboard.send_keys("""
                    Bonjour, 
                    {ENTER 2}
                    Est-ce{VK_SPACE}que{VK_SPACE}votre{VK_SPACE}voiture{VK_SPACE}est{VK_SPACE}proche{VK_SPACE}
                    d'un{VK_SPACE}transport{VK_SPACE}en{VK_SPACE}commun{VK_SPACE}(tranway,{VK_SPACE}rer,{VK_SPACE}
                    ter,{VK_SPACE}métro,{VK_SPACE}bus,{VK_SPACE}bus{VK_SPACE}noctilien{VK_SPACE}...){VK_SPACE}de
                    {VK_SPACE}la{VK_SPACE}zone{VK_SPACE}1{VK_SPACE}à{VK_SPACE}5{VK_SPACE}de{VK_SPACE}la
                    {VK_SPACE}RATP/SNCF{VK_SPACE}à{VK_SPACE}pied{VK_SPACE}à{VK_SPACE}5{VK_SPACE}minutes
                    {VK_SPACE}s'il{VK_SPACE}vous{VK_SPACE}plaît{VK_SPACE}?
                    {ENTER 2}
                    Est-ce{VK_SPACE}que{VK_SPACE}le{VK_SPACE}moteur{VK_SPACE}tourne{VK_SPACE}toujours
                    {VK_SPACE}s'il{VK_SPACE}vous{VK_SPACE}plaît{VK_SPACE}?
                    {ENTER 2}
                    Cordialement,
                    """)

            time.sleep(5)

            # Move to the "Envoyer" button
            pywinauto.keyboard.send_keys("{VK_TAB}")

            time.sleep(5)

            # Click tne "Enter" button to send the message
            pywinauto.keyboard.send_keys("{ENTER}")

            time.sleep(10)

            # Close the browser
            pywinauto.keyboard.send_keys('%{F4}')

            time.sleep(10)

    def test_send_message_for_buying_cars_from_a_ad_list_without_phone_number(self):
        urls_ad = []

        for url_ad in urls_ad:
            app = Application(backend="uia")

            # Ouvrir l'application Google Chrome
            app.start("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")

            time.sleep(6)

            # Open the Outlook Application
            pywinauto.keyboard.send_keys(url_ad)

            print(url_ad)

            time.sleep(5)

            # Press the 'Enter' button
            pywinauto.keyboard.send_keys('{ENTER}')

            time.sleep(15)

            # Clik side to the input "Votre nom"
            pywinauto.mouse.click(button='left', coords=(550, 360))

            time.sleep(5)

            pywinauto.keyboard.send_keys("{VK_TAB}")

            time.sleep(5)

            # Write my name
            pywinauto.keyboard.send_keys("Mr{VK_SPACE}")

            time.sleep(5)

            # Clik on the input "Votre email"
            pywinauto.keyboard.send_keys("{VK_TAB}")

            time.sleep(5)

            # Write my email
            pywinauto.keyboard.send_keys(".@outlook.fr")

            time.sleep(5)

            # Click on the input "Votre message"
            pywinauto.keyboard.send_keys("{VK_TAB}")

            time.sleep(5)

            # Write my message
            pywinauto.keyboard.send_keys("""
                    Bonjour, 
                    {ENTER 2}
                    Est-ce{VK_SPACE}que{VK_SPACE}votre{VK_SPACE}voiture{VK_SPACE}est{VK_SPACE}proche{VK_SPACE}
                    d'un{VK_SPACE}transport{VK_SPACE}en{VK_SPACE}commun{VK_SPACE},{VK_SPACE}c'est-à-dire,
                    {VK_SPACE}tranway,{VK_SPACE}rer,{VK_SPACE}
                    ter,{VK_SPACE}métro,{VK_SPACE}bus,{VK_SPACE}bus{VK_SPACE}noctilien{VK_SPACE}de
                    {VK_SPACE}la{VK_SPACE}zone{VK_SPACE}1{VK_SPACE}à{VK_SPACE}5{VK_SPACE}de{VK_SPACE}la
                    {VK_SPACE}RATP/SNCF{VK_SPACE}à{VK_SPACE}pied{VK_SPACE}à{VK_SPACE}5{VK_SPACE}minutes{VK_SPACE}
                    s'il{VK_SPACE}vous{VK_SPACE}plaît{VK_SPACE}?
                    {ENTER 2}
                    Est-ce{VK_SPACE}que{VK_SPACE}votre{VK_SPACE}voiture{VK_SPACE}est{VK_SPACE}stationnée{VK_SPACE}
                    sur{VK_SPACE}la{VK_SPACE}voie{VK_SPACE}publique{VK_SPACE}sur{VK_SPACE}une{VK_SPACE}place
                    {VK_SPACE}gratuite{VK_SPACE}s'il{VK_SPACE}vous{VK_SPACE}plaît{VK_SPACE}?
                    {ENTER 2}
                    Est-ce{VK_SPACE}que{VK_SPACE}le{VK_SPACE}moteur{VK_SPACE}tourne{VK_SPACE}toujours
                    {VK_SPACE}correctement{VK_SPACE}s'il{VK_SPACE}vous{VK_SPACE}plaît{VK_SPACE}?
                    {ENTER 2}
                    Cordialement,
                    """)

            time.sleep(5)

            # Move to the "Envoyer" button
            pywinauto.keyboard.send_keys("{VK_TAB}")

            time.sleep(5)

            # Click tne "Enter" button to send the message
            pywinauto.keyboard.send_keys("{ENTER}")

            time.sleep(10)

            # Close the browser
            pywinauto.keyboard.send_keys('%{F4}')

            time.sleep(10)

    def test_send_message_for_cave_from_a_list_of_ad_with_phone_number_for_injecting_hydrogene_into_natural_gas_network(self):
        url_ads = [
        ]

        for url_ad in url_ads:
            time.sleep(5)

            app = Application(backend="uia")

            # Ouvrir l'application Google Chrome
            app.start("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")

            time.sleep(5)

            # Open the Outlook Application
            pywinauto.keyboard.send_keys(url_ad)

            time.sleep(5)

            print(url_ad)

            time.sleep(5)

            # Press the 'Enter' button
            pywinauto.keyboard.send_keys('{ENTER}')

            time.sleep(10)

            # Clik side to the input "Votre nom"
            pywinauto.mouse.click(button='left', coords=(550, 310))

            time.sleep(5)

            pywinauto.keyboard.send_keys("{VK_TAB}")

            time.sleep(5)

            # Write my name
            pywinauto.keyboard.send_keys("Mr{VK_SPACE}")

            time.sleep(5)

            # Clik on the input "Votre email"
            pywinauto.keyboard.send_keys("{VK_TAB}")

            time.sleep(5)

            # Write my email
            pywinauto.keyboard.send_keys(".@outlook.fr")

            time.sleep(5)

            #Click on the input "Votre message"
            pywinauto.keyboard.send_keys("{VK_TAB 2}")

            time.sleep(5)

            # Write my message
            pywinauto.keyboard.send_keys("""
            Bonjour, 
            {ENTER 2}
            Est-ce{VK_SPACE}que{VK_SPACE}la{VK_SPACE}copropriété,{VK_SPACE}le{VK_SPACE}préfet{VK_SPACE}et{VK_SPACE}
            les{VK_SPACE}autorités{VK_SPACE}compétentes{VK_SPACE}seront{VK_SPACE}d'accord{VK_SPACE}que{VK_SPACE}
            la{VK_SPACE}cave{VK_SPACE}soit{VK_SPACE}utilisée{VK_SPACE}en{VK_SPACE}tant{VK_SPACE}
            qu'installation{VK_SPACE}classée{VK_SPACE}pour{VK_SPACE}la{VK_SPACE}protection{VK_SPACE}de{VK_SPACE}
            l'environnement{VK_SPACE}en{VK_SPACE}vertu{VK_SPACE}du{VK_SPACE}Code{VK_SPACE}de{VK_SPACE}
            l'environnement{VK_SPACE}de{VK_SPACE}la{VK_SPACE}loi{VK_SPACE}française{VK_SPACE}s'il{VK_SPACE}
            vous{VK_SPACE}plaît{VK_SPACE}?
            {ENTER 2}
            Est-ce{VK_SPACE}que{VK_SPACE}la{VK_SPACE}cave{VK_SPACE}pourra{VK_SPACE}être{VK_SPACE}utilisée{VK_SPACE}
            pour{VK_SPACE}l'accès{VK_SPACE}et{VK_SPACE}le{VK_SPACE}raccordement{VK_SPACE}aux{VK_SPACE}réseaux{VK_SPACE}
            et{VK_SPACE}installations{VK_SPACE}de{VK_SPACE}gaz{VK_SPACE}naturel{VK_SPACE}en{VK_SPACE}vertu{VK_SPACE}
            des{VK_SPACE}articles{VK_SPACE}L451-1{VK_SPACE}à{VK_SPACE}L451-3,{VK_SPACE}L453-1{VK_SPACE}à{VK_SPACE}
            L453-10{VK_SPACE}et{VK_SPACE}suivants{VK_SPACE}du{VK_SPACE}Code{VK_SPACE}de{VK_SPACE}l'énergie{VK_SPACE}
            de{VK_SPACE}la{VK_SPACE}loi{VK_SPACE}française{VK_SPACE}s'il{VK_SPACE}vous{VK_SPACE}plaît{VK_SPACE}?
            {ENTER 2}
            Le{VK_SPACE}mélange{VK_SPACE}gazeux{VK_SPACE}de{VK_SPACE}dihydrogène{VK_SPACE}et{VK_SPACE}
            dioxygène{VK_SPACE}produit{VK_SPACE}par{VK_SPACE}électrolyse{VK_SPACE}de{VK_SPACE}l'eau{VK_SPACE}
            sera{VK_SPACE}injecté{VK_SPACE}dans{VK_SPACE}le{VK_SPACE}réseau{VK_SPACE}public{VK_SPACE}de{VK_SPACE}
            gaz{VK_SPACE}naturel{VK_SPACE}depuis{VK_SPACE}la{VK_SPACE}cave.
            {ENTER 2}
            Est-ce{VK_SPACE}que{VK_SPACE}la{VK_SPACE}cave{VK_SPACE}pourra{VK_SPACE}être{VK_SPACE}équipée{VK_SPACE}
            d'une{VK_SPACE}prise{VK_SPACE}de{VK_SPACE}courant{VK_SPACE}et{VK_SPACE}un{VK_SPACE}compteur{VK_SPACE}
            électrique{VK_SPACE}individuel{VK_SPACE}s'il{VK_SPACE}vous{VK_SPACE}plaît{VK_SPACE}?
            {ENTER 2}
            Est-ce{VK_SPACE}que{VK_SPACE}vous{VK_SPACE}pourriez{VK_SPACE}m'envoyer{VK_SPACE}le{VK_SPACE}
            contact{VK_SPACE}de{VK_SPACE}la{VK_SPACE}copropriété{VK_SPACE}s'il{VK_SPACE}vous{VK_SPACE}plaît{VK_SPACE}?
            {ENTER 2}
            Ainsi,{VK_SPACE}je{VK_SPACE}vous{VK_SPACE}prie{VK_SPACE}de{VK_SPACE}m'adresser{VK_SPACE}vos{VK_SPACE}
            questions{VK_SPACE}et{VK_SPACE}vos{VK_SPACE}attentes{VK_SPACE}s'il{VK_SPACE}vous{VK_SPACE}plaît.
            {ENTER 2}
            Cordialement,
            """)

            time.sleep(5)

            # Move to the "Envoyer" button
            pywinauto.keyboard.send_keys("{VK_TAB}")

            time.sleep(5)

            # Click tne "Enter" button to send the message
            pywinauto.keyboard.send_keys("{ENTER}")

            time.sleep(10)

            #Close the browser
            pywinauto.keyboard.send_keys('%{F4}')

    def test_send_message_for_cave_from_a_list_of_ad_without_phone_number_for_injecting_hydrogene_into_natural_gas_network(self):
        url_ads = [
        ]

        for url_ad in url_ads:
            time.sleep(5)

            app = Application(backend="uia")

            # Ouvrir l'application Google Chrome
            app.start("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")

            time.sleep(5)

            # Open the Outlook Application
            pywinauto.keyboard.send_keys(url_ad)

            time.sleep(5)

            print(url_ad)

            time.sleep(5)

            # Press the 'Enter' button
            pywinauto.keyboard.send_keys('{ENTER}')

            time.sleep(12)

            # Clik side to the input "Votre nom"
            pywinauto.mouse.click(button='left', coords=(550, 360))

            time.sleep(5)

            pywinauto.keyboard.send_keys("{VK_TAB}")

            time.sleep(5)

            # Write my name
            pywinauto.keyboard.send_keys("Mr{VK_SPACE}")

            time.sleep(5)

            # Clik on the input "Votre email"
            pywinauto.keyboard.send_keys("{VK_TAB}")

            time.sleep(5)

            # Write my email
            pywinauto.keyboard.send_keys(".@outlook.fr")

            time.sleep(5)

            #Click on the input "Votre message"
            pywinauto.keyboard.send_keys("{VK_TAB}")

            time.sleep(5)

            # Write my message
            pywinauto.keyboard.send_keys("""
            Bonjour, 
            {ENTER 2}
            Est-ce{VK_SPACE}que{VK_SPACE}la{VK_SPACE}copropriété,{VK_SPACE}le{VK_SPACE}préfet{VK_SPACE}et{VK_SPACE}
            les{VK_SPACE}autorités{VK_SPACE}compétentes{VK_SPACE}seront{VK_SPACE}d'accord{VK_SPACE}que{VK_SPACE}
            la{VK_SPACE}cave{VK_SPACE}soit{VK_SPACE}utilisée{VK_SPACE}en{VK_SPACE}tant{VK_SPACE}
            qu'installation{VK_SPACE}classée{VK_SPACE}pour{VK_SPACE}la{VK_SPACE}protection{VK_SPACE}de{VK_SPACE}
            l'environnement{VK_SPACE}en{VK_SPACE}vertu{VK_SPACE}du{VK_SPACE}Code{VK_SPACE}de{VK_SPACE}
            l'environnement{VK_SPACE}de{VK_SPACE}la{VK_SPACE}loi{VK_SPACE}française{VK_SPACE}s'il{VK_SPACE}
            vous{VK_SPACE}plaît{VK_SPACE}?
            {ENTER 2}
            Est-ce{VK_SPACE}que{VK_SPACE}la{VK_SPACE}cave{VK_SPACE}pourra{VK_SPACE}être{VK_SPACE}utilisée{VK_SPACE}
            pour{VK_SPACE}l'accès{VK_SPACE}et{VK_SPACE}le{VK_SPACE}raccordement{VK_SPACE}aux{VK_SPACE}réseaux{VK_SPACE}
            et{VK_SPACE}installations{VK_SPACE}de{VK_SPACE}gaz{VK_SPACE}naturel{VK_SPACE}en{VK_SPACE}vertu{VK_SPACE}
            des{VK_SPACE}articles{VK_SPACE}L451-1{VK_SPACE}à{VK_SPACE}L451-3,{VK_SPACE}L453-1{VK_SPACE}à{VK_SPACE}
            L453-10{VK_SPACE}et{VK_SPACE}suivants{VK_SPACE}du{VK_SPACE}Code{VK_SPACE}de{VK_SPACE}l'énergie{VK_SPACE}
            de{VK_SPACE}la{VK_SPACE}loi{VK_SPACE}française{VK_SPACE}s'il{VK_SPACE}vous{VK_SPACE}plaît{VK_SPACE}?
            {ENTER 2}
            Le{VK_SPACE}mélange{VK_SPACE}gazeux{VK_SPACE}de{VK_SPACE}dihydrogène{VK_SPACE}et{VK_SPACE}
            dioxygène{VK_SPACE}produit{VK_SPACE}par{VK_SPACE}électrolyse{VK_SPACE}de{VK_SPACE}l'eau{VK_SPACE}
            sera{VK_SPACE}injecté{VK_SPACE}dans{VK_SPACE}le{VK_SPACE}réseau{VK_SPACE}public{VK_SPACE}de{VK_SPACE}
            gaz{VK_SPACE}naturel{VK_SPACE}depuis{VK_SPACE}la{VK_SPACE}cave.
            {ENTER 2}
            Est-ce{VK_SPACE}que{VK_SPACE}la{VK_SPACE}cave{VK_SPACE}pourra{VK_SPACE}être{VK_SPACE}équipée{VK_SPACE}
            d'une{VK_SPACE}prise{VK_SPACE}de{VK_SPACE}courant{VK_SPACE}et{VK_SPACE}un{VK_SPACE}compteur{VK_SPACE}
            électrique{VK_SPACE}individuel{VK_SPACE}s'il{VK_SPACE}vous{VK_SPACE}plaît{VK_SPACE}?
            {ENTER 2}
            Est-ce{VK_SPACE}que{VK_SPACE}vous{VK_SPACE}pourriez{VK_SPACE}m'envoyer{VK_SPACE}le{VK_SPACE}
            contact{VK_SPACE}de{VK_SPACE}la{VK_SPACE}copropriété{VK_SPACE}s'il{VK_SPACE}vous{VK_SPACE}plaît{VK_SPACE}?
            {ENTER 2}
            Ainsi,{VK_SPACE}je{VK_SPACE}vous{VK_SPACE}prie{VK_SPACE}de{VK_SPACE}m'adresser{VK_SPACE}vos{VK_SPACE}
            questions{VK_SPACE}et{VK_SPACE}vos{VK_SPACE}attentes{VK_SPACE}s'il{VK_SPACE}vous{VK_SPACE}plaît.
            {ENTER 2}
            Cordialement,
            """)

            time.sleep(5)

            # Move to the "Envoyer" button
            pywinauto.keyboard.send_keys("{VK_TAB}")

            time.sleep(5)

            # Click tne "Enter" button to send the message
            pywinauto.keyboard.send_keys("{ENTER}")

            time.sleep(10)

            #Close the browser
            pywinauto.keyboard.send_keys('%{F4}')


class UnitTestsDesktopAutomationLeboncoinAuthentification(unittest.TestCase):
    def test_send_a_message_for_buying_a_land_for_gas_network_from_one_ad(self):
        print('test_send_a_message_for_buying_a_land_for_one_ad')

        time.sleep(5)

        url_ad = "https://www.leboncoin.fr/ventes_immobilieres/1921379087.htm?ac=558505705"

        app = Application(backend="uia")

        time.sleep(5)

        # Ouvrir l'application Internet Expllorer
        app.start("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")

        time.sleep(10)

        # open the ad
        pywinauto.keyboard.send_keys(url_ad)

        time.sleep(5)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(15)

        # Click on the "Envoyer un message" button
        pywinauto.mouse.click(button='left', coords=(1000, 400))

        time.sleep(15)

        # Click on the "Email" input
        pywinauto.mouse.click(button='left', coords=(600, 350))

        time.sleep(5)

        # Insert the 'Email'
        pywinauto.keyboard.send_keys('.@outlook.fr')

        time.sleep(5)

        # Press the 'TAB' button to 'M_D_P'
        pywinauto.keyboard.send_keys('{VK_TAB}')

        time.sleep(5)

        # Insert the 'M_D_P'
        pywinauto.keyboard.send_keys('')

        time.sleep(5)

        # Press the 'ENTER' button to connect
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(15)

        # Click on the "Votre telephone" input
        pywinauto.mouse.click(button='left', coords=(290, 290))

        time.sleep(5)

        # Insert the 'Votre telephone' value
        pywinauto.keyboard.send_keys('')

        time.sleep(5)

        # Press the 'TAB' button
        pywinauto.keyboard.send_keys('{VK_TAB}')

        time.sleep(5)

        # Insert the 'Votre message' value
        pywinauto.keyboard.send_keys("""
Bonjour,
{ENTER 2}
Tout{VK_SPACE}d'abord,{VK_SPACE}je{VK_SPACE}suis{VK_SPACE}en{VK_SPACE}train{VK_SPACE}de{VK_SPACE}monter{VK_SPACE}
un{VK_SPACE}projet{VK_SPACE}de{VK_SPACE}production{VK_SPACE}de{VK_SPACE}gaz{VK_SPACE}{(}hydrogène{VK_SPACE}et/ou
{VK_SPACE}méthane{VK_SPACE}de{VK_SPACE}synthèse{)}{VK_SPACE}directement{VK_SPACE}injectée{VK_SPACE}dans{VK_SPACE}
un{VK_SPACE}réseau{VK_SPACE}de{VK_SPACE}transport{VK_SPACE}de{VK_SPACE}gaz{VK_SPACE}naturel.
{ENTER 2}
Puis,{VK_SPACE}je{VK_SPACE}suis{VK_SPACE}à{VK_SPACE}la{VK_SPACE}recherche{VK_SPACE}d'un{VK_SPACE}terrain
{VK_SPACE}constructible{VK_SPACE}d'au{VK_SPACE}moins{VK_SPACE}1000{VK_SPACE}mètres{VK_SPACE}carrés{VK_SPACE}
raccordable{VK_SPACE}à{VK_SPACE}un{VK_SPACE}réseau{VK_SPACE}de{VK_SPACE}transport{VK_SPACE}de{VK_SPACE}gaz{VK_SPACE}
naturel.{VK_SPACE}Le{VK_SPACE}terrain{VK_SPACE}doit{VK_SPACE}se{VK_SPACE}situer{VK_SPACE}dans{VK_SPACE}la{VK_SPACE}
région{VK_SPACE}Ile-de-France.
{ENTER 2}
Mes{VK_SPACE}questions{VK_SPACE}sont:
{ENTER}
-{VK_SPACE}Est-ce{VK_SPACE}que{VK_SPACE}ce{VK_SPACE}bien{VK_SPACE}immobilier{VK_SPACE}est{VK_SPACE}propice
{VK_SPACE}pour{VK_SPACE}ce{VK_SPACE}type{VK_SPACE}de{VK_SPACE}projet{VK_SPACE}s'il{VK_SPACE}vous{VK_SPACE}plaît{VK_SPACE}?
{ENTER}
-{VK_SPACE}Est-ce{VK_SPACE}que{VK_SPACE}ce{VK_SPACE}bien{VK_SPACE}immobilier{VK_SPACE}est{VK_SPACE}viabilisable
{VK_SPACE}{(}électricité,{VK_SPACE}eau,{VK_SPACE}téléphone,{VK_SPACE}assainissement{VK_SPACE}...{)}{VK_SPACE}
s'il{VK_SPACE}vous{VK_SPACE}plaît{VK_SPACE}?
{ENTER}
-{VK_SPACE}Est-ce{VK_SPACE}possible{VK_SPACE}de{VK_SPACE}recevoir{VK_SPACE}le{VK_SPACE}numéro{VK_SPACE}cadastral
{VK_SPACE}de{VK_SPACE}la{VK_SPACE}parcelle{VK_SPACE}pour{VK_SPACE}demander{VK_SPACE}aux{VK_SPACE}gestionnaires
{VK_SPACE}de{VK_SPACE}réseau{VK_SPACE}de{VK_SPACE}transport{VK_SPACE}de{VK_SPACE}gaz{VK_SPACE}naturel{VK_SPACE}si
{VK_SPACE}le{VK_SPACE}terrain{VK_SPACE}pourrait{VK_SPACE}être{VK_SPACE}raccordé{VK_SPACE}à{VK_SPACE}leurs{VK_SPACE}
réseaux{VK_SPACE}de{VK_SPACE}gaz{VK_SPACE}s'il{VK_SPACE}vous{VK_SPACE}plaît{VK_SPACE}?
{ENTER 2}
Très{VK_SPACE}bonne{VK_SPACE}journée{VK_SPACE}à{VK_SPACE}vous,
{ENTER 2}
Monsieur{VK_SPACE}{VK_SPACE}
{ENTER}
Président{VK_SPACE}de{VK_SPACE}la{VK_SPACE}société{VK_SPACE}Holomorphe
{ENTER}
Ingénieur{VK_SPACE}généraliste{VK_SPACE}diplômé{VK_SPACE}à{VK_SPACE}l'E.S.I.L.V.{VK_SPACE}Paris{VK_SPACE}La{VK_SPACE}Défense
{ENTER}
Adresse{VK_SPACE}du{VK_SPACE}siège{VK_SPACE}social{VK_SPACE}:{VK_SPACE}31{VK_SPACE}Avenue{VK_SPACE}de{VK_SPACE}
Ségur{VK_SPACE}75007{VK_SPACE}Paris
{ENTER}
Téléphone{VK_SPACE}:{VK_SPACE}0749163329
{ENTER}
Site{VK_SPACE}internet{VK_SPACE}:{VK_SPACE}https://www.holomorphe.com
{ENTER}
Informations{VK_SPACE}générales{VK_SPACE}:{VK_SPACE}https://www.societe.com/societe/holomorphe-883632556.html
{ENTER}
GitHub{VK_SPACE}:{VK_SPACE}https://github.com/Jay4C
{ENTER}
YouTube{VK_SPACE}:{VK_SPACE}https://www.youtube.com/channel/UClK7qVMGyLGEE0uPy7LFGlA
{ENTER}
Datarade{VK_SPACE}:{VK_SPACE}https://datarade.ai/data-providers/holomorphe/profile
        """)

        time.sleep(5)

        # Press the 'TAB' button
        pywinauto.keyboard.send_keys('{VK_TAB}')

        time.sleep(5)

        # Press the 'ENTER' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(5)

        # Click on the "Jay4C" logo
        pywinauto.mouse.click(button='left', coords=(1180, 100))

        time.sleep(10)

        # Press the 'DOWN' button
        pywinauto.keyboard.send_keys('{DOWN 6}')

        time.sleep(5)

        # Click on the "Me déconnecter" button
        pywinauto.mouse.click(button='left', coords=(200, 425))

        time.sleep(10)

        # Close the browser
        pywinauto.keyboard.send_keys('%{F4}')

        time.sleep(5)

    def test_send_a_message_for_buying_a_land_for_gas_network_from_many_ads(self):
        print('test_send_a_message_for_buying_a_land_for_gas_network_from_many_ads')

        time.sleep(5)

        urls_ad = [
            "https://www.leboncoin.fr/ventes_immobilieres/1929898733.htm?ac=558505705",
            "https://www.leboncoin.fr/ventes_immobilieres/2000690112.htm?ac=558505705",
            "https://www.leboncoin.fr/ventes_immobilieres/1997070848.htm?ac=558505705",
            "https://www.leboncoin.fr/ventes_immobilieres/1969881329.htm?ac=558505705",
            "https://www.leboncoin.fr/ventes_immobilieres/1839656260.htm?ac=558505705",
            "https://www.leboncoin.fr/ventes_immobilieres/1927447077.htm?ac=558505705",
            "https://www.leboncoin.fr/ventes_immobilieres/1925778276.htm?ac=558505705",
            "https://www.leboncoin.fr/ventes_immobilieres/1977782252.htm?ac=558505705",
            "https://www.leboncoin.fr/ventes_immobilieres/1971876543.htm?ac=558505705",
            "https://www.leboncoin.fr/ventes_immobilieres/1962714902.htm?ac=558505705",
            "https://www.leboncoin.fr/ventes_immobilieres/1978413101.htm?ac=558505705",
            "https://www.leboncoin.fr/ventes_immobilieres/1941993937.htm?ac=558505705",
            "https://www.leboncoin.fr/ventes_immobilieres/1910162772.htm?ac=558505705",
            "https://www.leboncoin.fr/ventes_immobilieres/1956897941.htm?ac=558505705",
            "https://www.leboncoin.fr/ventes_immobilieres/1989623872.htm?ac=558505705",
            "https://www.leboncoin.fr/ventes_immobilieres/1948279308.htm?ac=558505705",
            "https://www.leboncoin.fr/ventes_immobilieres/1981564543.htm?ac=558505705",
            "https://www.leboncoin.fr/ventes_immobilieres/1793000769.htm?ac=558505705",
            "https://www.leboncoin.fr/ventes_immobilieres/1943156310.htm?ac=558505705",
            "https://www.leboncoin.fr/ventes_immobilieres/1943156294.htm?ac=558505705",
            "https://www.leboncoin.fr/ventes_immobilieres/1801245689.htm?ac=558505705",
            "https://www.leboncoin.fr/ventes_immobilieres/1906428851.htm?ac=558505705",
            "https://www.leboncoin.fr/ventes_immobilieres/1895708107.htm?ac=558505705",
            "https://www.leboncoin.fr/ventes_immobilieres/1880620571.htm?ac=558505705",
            "https://www.leboncoin.fr/ventes_immobilieres/1999593421.htm?ac=558505705",
            "https://www.leboncoin.fr/ventes_immobilieres/1997223998.htm?ac=558505705",
            "https://www.leboncoin.fr/ventes_immobilieres/1864248526.htm?ac=558505705",
            "https://www.leboncoin.fr/ventes_immobilieres/1801520521.htm?ac=558505705",
            "https://www.leboncoin.fr/ventes_immobilieres/1650167751.htm?ac=558505705",
            "https://www.leboncoin.fr/ventes_immobilieres/1981877718.htm?ac=558505705",
            "https://www.leboncoin.fr/ventes_immobilieres/1882705061.htm?ac=558505705",
            "https://www.leboncoin.fr/ventes_immobilieres/1978526515.htm?ac=558505705",
            "https://www.leboncoin.fr/ventes_immobilieres/1695973580.htm?ac=558505705",
            "https://www.leboncoin.fr/ventes_immobilieres/1884193575.htm?ac=558505705",
            "https://www.leboncoin.fr/ventes_immobilieres/2000204398.htm?ac=558505705",
            "https://www.leboncoin.fr/ventes_immobilieres/1962453820.htm?ac=558505705",
            "https://www.leboncoin.fr/ventes_immobilieres/1960118030.htm?ac=558505705",
            "https://www.leboncoin.fr/ventes_immobilieres/1993455361.htm?ac=558505705",
            "https://www.leboncoin.fr/ventes_immobilieres/1992631110.htm?ac=558505705",
            "https://www.leboncoin.fr/ventes_immobilieres/1991922782.htm?ac=558505705",
            "https://www.leboncoin.fr/ventes_immobilieres/1991922782.htm?ac=558505705",
            "https://www.leboncoin.fr/ventes_immobilieres/1990225289.htm?ac=558505705",
            "https://www.leboncoin.fr/ventes_immobilieres/1954322849.htm?ac=558505705",
            "https://www.leboncoin.fr/ventes_immobilieres/1947741148.htm?ac=558505705",
            "https://www.leboncoin.fr/ventes_immobilieres/1972592555.htm?ac=558505705"
        ]

        for url_ad in urls_ad:
            print("url_ad : " + url_ad)

            time.sleep(5)

            app = Application(backend="uia")

            time.sleep(5)

            # Ouvrir l'application Internet Expllorer
            app.start("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")

            time.sleep(10)

            # open the ad
            pywinauto.keyboard.send_keys(url_ad)

            time.sleep(5)

            # Press the 'Enter' button
            pywinauto.keyboard.send_keys('{ENTER}')

            time.sleep(20)

            # Click on the "Continuer sans accepter" button
            pywinauto.mouse.click(button='left', coords=(440, 690))

            time.sleep(10)

            # Click on the "Envoyer un message" button
            pywinauto.mouse.click(button='left', coords=(1000, 400))

            time.sleep(15)

            # Click on the "Email" input
            pywinauto.mouse.click(button='left', coords=(600, 350))

            time.sleep(5)

            # Insert the 'Email'
            pywinauto.keyboard.send_keys('.@outlook.fr')

            time.sleep(5)

            # Press the 'TAB' button to 'M_D_P'
            pywinauto.keyboard.send_keys('{VK_TAB}')

            time.sleep(5)

            # Insert the 'M_D_P'
            pywinauto.keyboard.send_keys('')

            time.sleep(5)

            # Press the 'ENTER' button to connect
            pywinauto.keyboard.send_keys('{ENTER}')

            time.sleep(15)

            # Click on the "Votre telephone" input
            pywinauto.mouse.click(button='left', coords=(290, 290))

            time.sleep(5)

            # Insert the 'Votre telephone' value
            pywinauto.keyboard.send_keys('')

            time.sleep(5)

            # Press the 'TAB' button
            pywinauto.keyboard.send_keys('{VK_TAB}')

            time.sleep(5)

            # Insert the 'Votre message' value
            pywinauto.keyboard.send_keys("""
Bonjour,
{ENTER 2}
Tout{VK_SPACE}d'abord,{VK_SPACE}je{VK_SPACE}suis{VK_SPACE}en{VK_SPACE}train{VK_SPACE}de{VK_SPACE}monter{VK_SPACE}
un{VK_SPACE}projet{VK_SPACE}de{VK_SPACE}production{VK_SPACE}de{VK_SPACE}gaz{VK_SPACE}{(}hydrogène{VK_SPACE}et/ou
{VK_SPACE}méthane{VK_SPACE}de{VK_SPACE}synthèse{)}{VK_SPACE}directement{VK_SPACE}injectée{VK_SPACE}dans{VK_SPACE}
un{VK_SPACE}réseau{VK_SPACE}de{VK_SPACE}transport{VK_SPACE}de{VK_SPACE}gaz{VK_SPACE}naturel.
{ENTER 2}
Puis,{VK_SPACE}je{VK_SPACE}suis{VK_SPACE}à{VK_SPACE}la{VK_SPACE}recherche{VK_SPACE}d'un{VK_SPACE}terrain
{VK_SPACE}constructible{VK_SPACE}d'au{VK_SPACE}moins{VK_SPACE}1000{VK_SPACE}mètres{VK_SPACE}carrés{VK_SPACE}
raccordable{VK_SPACE}à{VK_SPACE}un{VK_SPACE}réseau{VK_SPACE}de{VK_SPACE}transport{VK_SPACE}de{VK_SPACE}gaz{VK_SPACE}
naturel.{VK_SPACE}Le{VK_SPACE}terrain{VK_SPACE}doit{VK_SPACE}se{VK_SPACE}situer{VK_SPACE}dans{VK_SPACE}la{VK_SPACE}
région{VK_SPACE}Ile-de-France.
{ENTER 2}
Mes{VK_SPACE}questions{VK_SPACE}sont:
{ENTER}
-{VK_SPACE}Est-ce{VK_SPACE}que{VK_SPACE}ce{VK_SPACE}bien{VK_SPACE}immobilier{VK_SPACE}est{VK_SPACE}propice
{VK_SPACE}pour{VK_SPACE}ce{VK_SPACE}type{VK_SPACE}de{VK_SPACE}projet{VK_SPACE}s'il{VK_SPACE}vous{VK_SPACE}plaît{VK_SPACE}?
{ENTER}
-{VK_SPACE}Est-ce{VK_SPACE}que{VK_SPACE}ce{VK_SPACE}bien{VK_SPACE}immobilier{VK_SPACE}est{VK_SPACE}viabilisable
{VK_SPACE}{(}électricité,{VK_SPACE}eau,{VK_SPACE}téléphone,{VK_SPACE}assainissement{VK_SPACE}...{)}{VK_SPACE}
s'il{VK_SPACE}vous{VK_SPACE}plaît{VK_SPACE}?
{ENTER}
-{VK_SPACE}Est-ce{VK_SPACE}que{VK_SPACE}ce{VK_SPACE}bien{VK_SPACE}immobilier{VK_SPACE}est{VK_SPACE}proche{VK_SPACE}
d'une{VK_SPACE}gare{VK_SPACE}de{VK_SPACE}train{VK_SPACE}pour{VK_SPACE}les{VK_SPACE}voyageurs{VK_SPACE}s'il
{VK_SPACE}vous{VK_SPACE}plaît{VK_SPACE}?
{ENTER}
-{VK_SPACE}Est-ce{VK_SPACE}possible{VK_SPACE}de{VK_SPACE}recevoir{VK_SPACE}le{VK_SPACE}numéro{VK_SPACE}cadastral
{VK_SPACE}de{VK_SPACE}la{VK_SPACE}parcelle{VK_SPACE}pour{VK_SPACE}demander{VK_SPACE}aux{VK_SPACE}gestionnaires
{VK_SPACE}de{VK_SPACE}réseau{VK_SPACE}de{VK_SPACE}transport{VK_SPACE}de{VK_SPACE}gaz{VK_SPACE}naturel{VK_SPACE}si
{VK_SPACE}ce{VK_SPACE}bien{VK_SPACE}immobilier{VK_SPACE}pourrait{VK_SPACE}être{VK_SPACE}raccordé{VK_SPACE}à
{VK_SPACE}leurs{VK_SPACE}réseaux{VK_SPACE}de{VK_SPACE}gaz{VK_SPACE}s'il{VK_SPACE}vous{VK_SPACE}plaît{VK_SPACE}?
{ENTER 2}
Très{VK_SPACE}bonne{VK_SPACE}journée{VK_SPACE}à{VK_SPACE}vous,
{ENTER 2}
Monsieur{VK_SPACE}{VK_SPACE}
{ENTER}
Président{VK_SPACE}de{VK_SPACE}la{VK_SPACE}société{VK_SPACE}Holomorphe
{ENTER}
Ingénieur{VK_SPACE}généraliste{VK_SPACE}diplômé{VK_SPACE}à{VK_SPACE}l'E.S.I.L.V.{VK_SPACE}Paris{VK_SPACE}La{VK_SPACE}Défense
{ENTER}
Adresse{VK_SPACE}du{VK_SPACE}siège{VK_SPACE}social{VK_SPACE}:{VK_SPACE}31{VK_SPACE}Avenue{VK_SPACE}de{VK_SPACE}
Ségur{VK_SPACE}75007{VK_SPACE}Paris
{ENTER}
Téléphone{VK_SPACE}:{VK_SPACE}0749163329
{ENTER}
Site{VK_SPACE}internet{VK_SPACE}:{VK_SPACE}https://www.holomorphe.com
{ENTER}
Informations{VK_SPACE}générales{VK_SPACE}:{VK_SPACE}https://www.societe.com/societe/holomorphe-883632556.html
{ENTER}
GitHub{VK_SPACE}:{VK_SPACE}https://github.com/Jay4C
{ENTER}
YouTube{VK_SPACE}:{VK_SPACE}https://www.youtube.com/channel/UClK7qVMGyLGEE0uPy7LFGlA
{ENTER}
Datarade{VK_SPACE}:{VK_SPACE}https://datarade.ai/data-providers/holomorphe/profile
            """)

            time.sleep(5)

            # Press the 'TAB' button
            pywinauto.keyboard.send_keys('{VK_TAB}')

            time.sleep(5)

            # Press the 'ENTER' button
            pywinauto.keyboard.send_keys('{ENTER}')

            time.sleep(5)

            # Click on the "Jay4C" logo
            pywinauto.mouse.click(button='left', coords=(1180, 100))

            time.sleep(10)

            # Press the 'DOWN' button
            pywinauto.keyboard.send_keys('{DOWN 6}')

            time.sleep(5)

            # Click on the "Me déconnecter" button
            pywinauto.mouse.click(button='left', coords=(200, 425))

            time.sleep(10)

            # Close the browser
            pywinauto.keyboard.send_keys('%{F4}')

            time.sleep(5)


if __name__ == '__main__':
    unittest.main()
