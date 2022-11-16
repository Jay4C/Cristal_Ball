import unittest
import time
from pywinauto.application import Application
import pywinauto.keyboard
import pywinauto.mouse
import pywinauto.base_wrapper
import pywinauto.timings
import os


class UnitTestsDesktopAutomationGitHub(unittest.TestCase):
    def test_connecter_sans_outlook(self):
        print("test_connecter")

        time.sleep(6)

        app = Application(backend="uia")

        app.start("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")

        time.sleep(6)

        pywinauto.keyboard.send_keys("https://github.com/login")

        time.sleep(3)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(10)

        # Insert the 'Email' value
        pywinauto.keyboard.send_keys('.@outlook.fr')

        time.sleep(3)

        # Press the 'VK_TAB'
        pywinauto.keyboard.send_keys('{VK_TAB}')

        time.sleep(3)

        # Press the 'Password' value
        pywinauto.keyboard.send_keys('')

        time.sleep(3)

        # Press the 'VK_TAB'
        pywinauto.keyboard.send_keys('{VK_TAB}')

        time.sleep(3)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        print("ccleaner running")
        os.system("set ccleaner='C:\\Program Files\\CCleaner\\CCleaner.exe'")
        os.system("start ccleaner /AUTO")

        time.sleep(5)

    def test_connecter_avec_outlook(self):
        print("test_connecter")

        time.sleep(6)

        app = Application(backend="uia")

        app.start("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")

        time.sleep(6)

        pywinauto.keyboard.send_keys("https://github.com/login")

        time.sleep(3)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(10)

        # Insert the 'Email' value
        pywinauto.keyboard.send_keys('.@outlook.fr')

        time.sleep(3)

        # Press the 'VK_TAB'
        pywinauto.keyboard.send_keys('{VK_TAB}')

        time.sleep(3)

        # Press the 'Password' value
        pywinauto.keyboard.send_keys('')

        time.sleep(3)

        # Press the 'VK_TAB'
        pywinauto.keyboard.send_keys('{VK_TAB}')

        time.sleep(3)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(6)

        # Press the 'Ctrl+t' to open a new window
        pywinauto.keyboard.send_keys('^t')

        time.sleep(6)

        # Insert the 'Outlook page'
        pywinauto.keyboard.send_keys('https://outlook.live.com/owa/')

        time.sleep(3)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(6)

        # Click on the "Connexion" button
        pywinauto.mouse.click(button='left', coords=(1100, 100))

        time.sleep(3)

        # Insert the 'Email' value
        pywinauto.keyboard.send_keys('.@outlook.fr')

        time.sleep(3)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Insert the 'Paswword' value
        pywinauto.keyboard.send_keys('')

        time.sleep(3)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(6)

        # Click on the "First email" button
        pywinauto.mouse.click(button='left', coords=(370, 240))

        time.sleep(6)

        # Double-Click on the "Code" value
        pywinauto.mouse.double_click(button='left', coords=(465, 435))

        time.sleep(3)

        # Copy the 'Code' value
        pywinauto.keyboard.send_keys('^c')

        time.sleep(3)

        # Return on the "GitHub page"
        pywinauto.mouse.click(button='left', coords=(145, 10))

        time.sleep(3)

        # Paste the 'Code' value
        pywinauto.keyboard.send_keys('^v')

        time.sleep(3)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        # Return on the "Outlook page"
        pywinauto.mouse.click(button='left', coords=(400, 10))

        time.sleep(3)

        # Delete the "email code"
        pywinauto.mouse.click(button='left', coords=(320, 140))

        time.sleep(3)

        # Disconnect from "Outlook"
        pywinauto.mouse.click(button='left', coords=(1340, 95))

        time.sleep(3)

        # Click on the "Se déconnecter" button
        pywinauto.mouse.click(button='left', coords=(1310, 145))

        time.sleep(7)

        # Close the page
        pywinauto.keyboard.send_keys('^w')

        time.sleep(3)

        print("ccleaner running")
        os.system("set ccleaner='C:\\Program Files\\CCleaner\\CCleaner.exe'")
        os.system("start ccleaner /AUTO")

        time.sleep(5)


if __name__ == '__main__':
    unittest.main()
