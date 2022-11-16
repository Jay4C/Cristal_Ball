import unittest
import time
from pywinauto.application import Application
import pywinauto.keyboard
import pywinauto.mouse
import pywinauto.base_wrapper
import pywinauto.timings

class UnitTestsDesktopAutomationBleachBit(unittest.TestCase):
    def test_is64bit(self):
        # Ouvrir l'application BleachBit
        app = Application(backend="uia")
        app.start("C:\\Program Files (x86)\\BleachBit\\bleachbit.exe")

        print("is64bit : " + str(app.is64bit()))

    def test_clean_my_pc(self):
        # Ouvrir l'application BleachBit
        app = Application(backend="uia")
        app.start("C:\\Program Files (x86)\\BleachBit\\bleachbit.exe")

        pywinauto.mouse.click(button='left', coords=(1000, 200))


if __name__ == '__main__':
    unittest.main()
