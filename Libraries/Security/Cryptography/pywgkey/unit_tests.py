import subprocess
import unittest


class UnitTestspywgkey(unittest.TestCase):
    # ok
    def test_some_commands(self):
        print("test_some_commands")

        subprocess.call("python -m pywgkey --help")
        subprocess.call("python -m pywgkey test")
        subprocess.call("python -m pywgkey test -w")
        subprocess.call("python -m pywgkey test -b")


if __name__ == '__main__':
    unittest.main()
