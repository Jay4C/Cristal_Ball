import pprint
import unittest
from pyktionary.models import Wiktionary


class UnitTestsInternetWWWHttpDynamicContentWikiPyktionary(unittest.TestCase):
    # ok
    def test_1(self):
        print('test_1')
        wik = Wiktionary()
        word = wik.word("oui")
        pprint.pprint(word, compact=True)


if __name__ == '__main__':
    unittest.main()
