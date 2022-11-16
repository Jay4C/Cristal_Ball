import unittest
import time
from pywinauto.application import Application
import pywinauto.keyboard
import pywinauto.mouse
import pywinauto.base_wrapper
import pywinauto.timings


class UnitTestsDesktopAutomationShine(unittest.TestCase):
    # ok
    def test_connect(self):
        print("test_connect")

        app = Application(backend="uia")

        app.start("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")

        time.sleep(6)

        pywinauto.keyboard.send_keys("https://app.shine.fr/")

        time.sleep(6)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(15)

        # Click on the screen
        pywinauto.mouse.click(button='left', coords=(600, 300))

        time.sleep(7)

        # Press the 'DOWN' button
        pywinauto.keyboard.send_keys('{DOWN}')

        time.sleep(15)

        # Click on the "Refuser" button
        pywinauto.mouse.click(button='left', coords=(670, 675))

        time.sleep(15)

        # Click on the "Se connecter" button
        pywinauto.mouse.click(button='left', coords=(180, 390))

        time.sleep(5)

        # Insert Phone
        pywinauto.keyboard.send_keys('')

        time.sleep(5)

        # Press the 'ENTER' button
        pywinauto.keyboard.send_keys("{ENTER}")

        time.sleep(5)

        # Insert Code
        pywinauto.keyboard.send_keys("")

        time.sleep(5)

        # Press the 'ENTER' button
        pywinauto.keyboard.send_keys("{ENTER}")

        time.sleep(5)

        # Press the 'Ctrl+T' button
        pywinauto.keyboard.send_keys("^t")

        time.sleep(5)

        # Open the TP Link Modem Web Page
        pywinauto.keyboard.send_keys("http://tplinkmodem.net/")

        time.sleep(5)

        # Enter
        pywinauto.keyboard.send_keys("{ENTER}")

        time.sleep(10)

        # Enter the password
        pywinauto.keyboard.send_keys("")

        time.sleep(5)

        # Enter
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

        # Copy the Shine code
        pywinauto.mouse.double_click(button='left', coords=(540, 320))
        pywinauto.keyboard.send_keys("+{LEFT}")
        pywinauto.keyboard.send_keys("^c")

        time.sleep(5)

        # Return to Shine app
        pywinauto.mouse.click(button='left', coords=(100, 10))

        time.sleep(5)

        # Click on the 'Code' input
        pywinauto.mouse.click(button='left', coords=(80, 500))

        time.sleep(5)

        # Paste the Shine code
        pywinauto.keyboard.send_keys("^v")

        time.sleep(5)

        # Enter
        pywinauto.keyboard.send_keys("{ENTER}")

        time.sleep(5)

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


if __name__ == '__main__':
    unittest.main()
