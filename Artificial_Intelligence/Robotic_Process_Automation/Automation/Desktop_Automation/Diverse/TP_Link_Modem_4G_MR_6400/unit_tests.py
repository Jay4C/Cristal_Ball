import unittest
import time
from pywinauto.application import Application
import pywinauto.keyboard
import pywinauto.mouse
import pywinauto.base_wrapper
import pywinauto.timings


class UnitTestsDesktopAutomationTPLinkModem4GMR6400(unittest.TestCase):
    def test_activate_or_deactivate_wifi(self):
        print("test_activate_or_deactivate_wifi")

        app = Application(backend="uia")

        app.start("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")

        time.sleep(7)

        # Open the TP Link Modem Web Page
        pywinauto.keyboard.send_keys("http://tplinkmodem.net/")

        time.sleep(5)

        # Enter
        pywinauto.keyboard.send_keys("{ENTER}")

        time.sleep(5)

        # Enter the password
        pywinauto.keyboard.send_keys("")

        time.sleep(5)

        # Enter
        pywinauto.keyboard.send_keys("{ENTER}")

        time.sleep(5)

        # Click left on "Wireless" button
        pywinauto.mouse.click(button='left', coords=(270, 330))

        time.sleep(5)

        # Click left on "Enable" button
        pywinauto.mouse.click(button='left', coords=(700, 250))

        time.sleep(5)

        # Click left on "Save" button
        pywinauto.mouse.click(button='left', coords=(1090, 350))

        time.sleep(25)

        # Click left on "Log out" button
        pywinauto.mouse.click(button='left', coords=(1050, 130))

        time.sleep(5)

        # Click left on "Log out _ Yes" button
        pywinauto.mouse.click(button='left', coords=(750, 360))

        time.sleep(5)

        # Close the browser
        pywinauto.keyboard.send_keys('%{F4}')

        time.sleep(5)

    def test_show_sms(self):
        print("test_show_sms")

        app = Application(backend="uia")

        app.start("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")

        time.sleep(7)

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

    def test_copy_the_shine_code(self):
        print("test_copy_the_shine_code")

        app = Application(backend="uia")

        app.start("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")

        time.sleep(7)

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

        # Open a new onglet
        pywinauto.keyboard.send_keys("^t")

        time.sleep(5)

        # Paste the Shine code
        pywinauto.keyboard.send_keys("^v")

        time.sleep(5)

    def test_copy_the_ovh_code(self):
        print("test_copy_the_ovh_code")

        app = Application(backend="uia")

        app.start("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")

        time.sleep(7)

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

        # Copy the Ovh code
        pywinauto.mouse.double_click(button='left', coords=(1065, 320))
        pywinauto.keyboard.send_keys("+{LEFT}")
        pywinauto.keyboard.send_keys("^c")

        time.sleep(5)

        # Open a new onglet
        pywinauto.keyboard.send_keys("^t")

        time.sleep(5)

        # Paste the Ovh code
        pywinauto.keyboard.send_keys("^v")

        time.sleep(5)

    def test_effacer_sms(self):
        app = Application(backend="uia")

        # Open the Edge Application
        app.start("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")

        time.sleep(5)

        # Open the TP Link Modem Web Page
        pywinauto.keyboard.send_keys("http://tplinkmodem.net/")

        time.sleep(3)

        # Enter
        pywinauto.keyboard.send_keys("{ENTER}")

        time.sleep(5)

        # Enter the password
        pywinauto.keyboard.send_keys("")

        time.sleep(5)

        # Enter
        pywinauto.keyboard.send_keys("{ENTER}")

        time.sleep(5)

        # Click left on "Advanced" button
        pywinauto.mouse.click(button='left', coords=(750, 130))

        time.sleep(5)

        # Click left on "SMS" button
        pywinauto.mouse.click(button='left', coords=(250, 400))

        time.sleep(5)

        # Click left on Outbox button
        pywinauto.mouse.click(button='left', coords=(270, 380))

        time.sleep(5)

        for i in range(2):
            time.sleep(5)

            # Click left on Selection button
            pywinauto.mouse.click(button='left', coords=(500, 280))

            time.sleep(5)

            # Click left on delete button
            pywinauto.mouse.click(button='left', coords=(1100, 240))

            time.sleep(5)

            # Move to the yes button
            pywinauto.mouse.move(coords=(770, 360))

            time.sleep(5)

            # Click left on yes button
            pywinauto.mouse.click(button='left', coords=(770, 360))

            time.sleep(10)


if __name__ == '__main__':
    unittest.main()
