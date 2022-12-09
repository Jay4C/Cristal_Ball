import unittest
import pandas as pd


class UnitTestsDataAnalysisPandas(unittest.TestCase):
    # ok
    def test_1(self):
        print('test_1')

        df = pd.DataFrame({'A': [1, 2, 3]})
        print(df.head())


if __name__ == '__main__':
    unittest.main()
