import unittest


class Tests_Codingame_Inoco_26_03_2022(unittest.TestCase):
    def test_1(self):
        print("test_1")

        def closest(lst, K):
            return abs(lst[min(range(len(lst)), key=lambda i: abs(lst[i] - K))])

        # Driver code
        lst = [3.64, 5.2, 9.42, 9.35, 8.5, 8, -9.35]
        K = 9.1
        print(closest(lst, K))

    def test_2(self):
        # Remove Duplicates from a Python list using a For Loop
        duplicated_list = [5, 1, 1, 2, 1, 3, 4, 1, 2, 3, 4]
        deduplicated_list = list()
        for item in duplicated_list:
            if item not in deduplicated_list:
                deduplicated_list.append(item)
        print(deduplicated_list)

    def test_compute_closest_to_zero(self):
        print('test_compute_closest_to_zero')

        import numpy as np

        ts = np.random.random(10)

        if len(ts) == 0:
            return 0
        else:
            if 0 <= len(ts) <= 10000:
                def find_nearest(array, value):
                    array = np.asarray(array)
                    idx = (np.abs(array - value)).argmin()
                    return array[idx]

                value = 0

                return abs(find_nearest(ts, value))



if __name__ == '__main__':
    unittest.main()
