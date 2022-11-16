import unittest
from netaddr import *

# https://netaddr.readthedocs.io/en/latest/tutorial_01.html


class UnitTestsIPAddressSubnetsRanges(unittest.TestCase):
    # ok
    def test_Basic_operations(self):
        print('test_Basic_operations')

        ip = IPAddress('192.0.2.1')
        print(str(ip.version))
        print(repr(ip))
        print(ip)


if __name__ == '__main__':
    unittest.main()
