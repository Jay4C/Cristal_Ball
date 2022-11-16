import unittest
import time
from pywinauto.application import Application
import pywinauto.keyboard
import pywinauto.mouse
import pywinauto.base_wrapper
import pywinauto.timings
import os


class UnitTestsDesktopAutomationOvh(unittest.TestCase):
    # ok
    def test_connecter(self):
        print("test_connecter")

        app = Application(backend="uia")

        app.start("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")

        time.sleep(6)

        pywinauto.keyboard.send_keys("https://www.ovh.com/auth/?action=gotomanager&from=https://www.ovh.com/fr/&ovhSubsidiary=fr")

        time.sleep(3)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(10)

        # Click on the "Identifiant ou adresse e-mail" button
        pywinauto.mouse.click(button='left', coords=(370, 350))

        time.sleep(5)

        # Insert my 'Identifiant ou adresse e-mail'
        pywinauto.keyboard.send_keys('')

        time.sleep(5)

        # Tab to the password
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(10)

        # Insert password
        pywinauto.keyboard.send_keys('')

        time.sleep(5)

        # Tab to the "Se connecter" button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(5)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(5)

        # Open a new window
        pywinauto.keyboard.send_keys('^t')

        time.sleep(10)

        # Open a new window
        pywinauto.keyboard.send_keys('www.tplinkmodem.net')

        time.sleep(5)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(10)

        # Insert the password
        pywinauto.keyboard.send_keys('')

        time.sleep(5)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys("{ENTER}")

        time.sleep(10)

        # Click left on "Advanced" button
        pywinauto.mouse.click(button='left', coords=(740, 140))

        time.sleep(5)

        # Click left on "SMS" button
        pywinauto.mouse.click(button='left', coords=(260, 400))

        time.sleep(5)

        # Click left on "Inbox" button
        pywinauto.mouse.click(button='left', coords=(260, 280))

        time.sleep(5)

        # Click left on "Refresh" button
        pywinauto.mouse.click(button='left', coords=(1040, 240))

        time.sleep(5)

        # Click left on "SMS" icon
        pywinauto.mouse.click(button='left', coords=(550, 320))

        time.sleep(5)

        # Copy the Ovh code
        pywinauto.mouse.double_click(button='left', coords=(525, 340))
        # pywinauto.keyboard.send_keys("+{LEFT}")
        pywinauto.keyboard.send_keys("^c")
        pywinauto.keyboard.send_keys("^c")
        pywinauto.keyboard.send_keys("^c")

        time.sleep(5)

        # Return to Ovh app
        pywinauto.mouse.click(button='left', coords=(100, 10))

        time.sleep(5)

        # Click on the 'Code' input
        pywinauto.mouse.click(button='left', coords=(610, 540))

        time.sleep(5)

        # Paste the Ovh code
        pywinauto.keyboard.send_keys("^v")

        time.sleep(5)

        # Tab to the "Valider" button
        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(5)

        # Enter
        pywinauto.keyboard.send_keys("{ENTER}")

        time.sleep(10)

        # Return to TP Link Modem
        pywinauto.mouse.click(button='left', coords=(350, 10))

        time.sleep(5)

        # Click left on "Inbox" button
        pywinauto.mouse.click(button='left', coords=(260, 280))

        time.sleep(5)

        # Click left on "Refresh" button
        pywinauto.mouse.click(button='left', coords=(1040, 240))

        time.sleep(5)

        # Click left on "Select the sms" button
        pywinauto.mouse.click(button='left', coords=(500, 325))

        time.sleep(5)

        # Click left on "Delete" button
        pywinauto.mouse.click(button='left', coords=(1100, 240))

        time.sleep(5)

        # Click left on "Yes" button to delete all sms
        pywinauto.mouse.click(button='left', coords=(770, 360))

        time.sleep(5)

        # Click left on "Log out" button
        pywinauto.mouse.click(button='left', coords=(1050, 130))

        time.sleep(5)

        # Click left on "Log out _ Yes" button
        pywinauto.mouse.click(button='left', coords=(750, 360))

        time.sleep(5)

        # Close the onglet "TP Link Modem"
        pywinauto.keyboard.send_keys('^w')

        time.sleep(5)

        print("ccleaner running")
        os.system("set ccleaner='C:\\Program Files\\CCleaner\\CCleaner.exe'")
        os.system("start ccleaner /AUTO")

        time.sleep(5)


if __name__ == '__main__':
    unittest.main()
