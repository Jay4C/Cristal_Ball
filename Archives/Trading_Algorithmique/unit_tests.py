import unittest


class UnitTestsTradingAlgorithmique(unittest.TestCase):
    def test_place_orders(self):
        print('test_place_orders')

    def test_decision_making(self):
        print('test_decision_making')

        # Fluctuating variables in the time
        # World population
        world_population = 0


class UnitTestsMonthlyAccountingWritings(unittest.TestCase):
    def test_list_all_open_positions(self):
        print("test_list_all_open_positions")

    def test_list_all_closed_positions(self):
        print("test_list_all_closed_positions")

    def test_list_all_money_deposits_during_this_month(self):
        print("test_list_all_money_deposits_during_this_month")

    def test_list_all_money_withdrawal_of_this_month(self):
        print("test_list_all_money_withdrawal_of_this_month")


class UnitTestsHistoricalMovementsInMySQL(unittest.TestCase):
    def test_store_the_open_positions(self):
        print("test_store_the_open_positions")

    def test_store_the_closed_positions(self):
        print("test_store_the_closed_positions")

    def test_store_the_money_deposits(self):
        print("test_store_the_money_deposits")

    def test_store_the_money_withdrawals(self):
        print("test_store_the_money_withdrawals")


if __name__ == '__main__':
    unittest.main()
