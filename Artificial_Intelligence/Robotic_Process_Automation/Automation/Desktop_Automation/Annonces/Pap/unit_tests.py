import unittest
import time
from pywinauto.application import Application
import pywinauto.keyboard
import pywinauto.mouse


class UnitTestsDesktopAutomationPap(unittest.TestCase):
    def test_send_a_message_from_one_ad(self):
        url_ad = "https://www.pap.fr/annonces/bureaux-paris-16e-r427800161"

        app = Application(backend="uia")

        # Ouvrir l'application Google Chrome
        app.start("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")
        time.sleep(7)

        # Open the Pap Application
        pywinauto.keyboard.send_keys(url_ad)
        time.sleep(5)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')
        time.sleep(10)

        # Clik on the form
        pywinauto.mouse.click(button='left', coords=(1150, 230))
        time.sleep(3)

        # Go to the "Votre prénom" input
        pywinauto.keyboard.send_keys("{VK_TAB}")
        time.sleep(3)
        pywinauto.keyboard.send_keys("")

        # Go to the "Votre nom" input
        time.sleep(3)
        pywinauto.keyboard.send_keys("{VK_TAB}")
        time.sleep(3)
        pywinauto.keyboard.send_keys("")

        # Go to the "Votre email" input
        time.sleep(3)
        pywinauto.keyboard.send_keys("{VK_TAB}")
        time.sleep(3)
        pywinauto.keyboard.send_keys(".@outlook.fr")

        # Go to the "Votre téléphone" input
        time.sleep(3)
        pywinauto.keyboard.send_keys("{VK_TAB}")
        time.sleep(3)
        pywinauto.keyboard.send_keys("")

        # Go to the "Votre message" input
        time.sleep(3)
        pywinauto.keyboard.send_keys("{VK_TAB}")
        time.sleep(3)
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

        # Uncheck the "Je souhaite recevoir les annonces correspondant à ma recherche" checkbox
        time.sleep(3)
        pywinauto.keyboard.send_keys("{VK_TAB}")
        time.sleep(3)
        pywinauto.mouse.click(button='left', coords=(1000, 330))

        # Click on the "Envoyer votre message" button
        time.sleep(3)
        pywinauto.mouse.click(button='left', coords=(1000, 400))

        # Close the brower
        time.sleep(7)
        pywinauto.keyboard.send_keys('%{F4}')


if __name__ == '__main__':
    unittest.main()
