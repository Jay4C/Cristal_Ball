import unittest
import time
from pywinauto.application import Application
import pyautogui
import pywinauto.mouse
import pywinauto.keyboard


class UnitTestsDesktopAutomationCCleaner(unittest.TestCase):
    def test_is64bit(self):
        print("test_is64bit")

        app = Application(backend="uia")

        # Ouvrir l'application Google Chrome
        app.start("C:\\Program Files\\CCleaner\\CCleaner64.exe")

        print("is64bit : " + str(app.is64bit()))

    def test_clean_my_pc(self):
        app = Application(backend="uia")

        # Ouvrir l'application CCleaner
        app.start("C:\\Program Files\\CCleaner\\CCleaner64.exe")

        time.sleep(3)

        # Click on "Run Cleaner"
        pywinauto.mouse.move(coords=(1300, 650))


if __name__ == '__main__':
    unittest.main()
