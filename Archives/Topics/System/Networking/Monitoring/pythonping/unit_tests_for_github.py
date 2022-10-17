import unittest
from pythonping import ping


class UnitTestsTopicsSystemNetworkingMonitoringPythonping(unittest.TestCase):
    # ok
    def test_1(self):
        print('test_1')
        ping('157.240.21.16', verbose=True)


if __name__ == '__main__':
    unittest.main()
