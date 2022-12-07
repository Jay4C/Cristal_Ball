import unittest
import os


class UnitTestsDirectoryManagement(unittest.TestCase):
    # ok
    def test_remove_file(self):
        print("test_remove_file")

        directory = "A:\\GitHub\\My_Own_Data\\"
        file = "".replace("/", "\\")
        filename = directory + file
        os.remove(filename)

    # ok
    def test_remove_files(self):
        print("test_remove_files")

        directory = "A:\\GitHub\\My_Own_Data\\"

        files = [
        ]

        for file in files:
            try:
                filename = directory + file.replace("/", "\\")
                os.remove(filename)
            except Exception as e:
                print('error : ' + str(e))


if __name__ == '__main__':
    unittest.main()
