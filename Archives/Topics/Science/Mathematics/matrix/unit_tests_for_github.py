import unittest
from matrix import Matrix


class UnitTestsTopicsScienceMathematicsMatrix(unittest.TestCase):
    # ok
    def test_1(self):
        print('test_1')
        print(Matrix(4, 4))


if __name__ == '__main__':
    unittest.main()
