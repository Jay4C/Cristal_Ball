import unittest


class UnitTestsInUse(unittest.TestCase):
    def test_1(self):
        print("test_1")

        class MathUtils:
            @staticmethod
            def average(a, b):
                return a + b / 2

        print(MathUtils.average(2, 1))

    def test_2(self):
        def remove_duplicates(products):
            return list(dict.fromkeys(products))

        def count_one_element_in_list(products, element):
            return products.count(element)

        def first_unique_product(products):
            list_unique_product = []

            for i in remove_duplicates(products):
                if count_one_element_in_list(products, i) == 1:
                    list_unique_product.append(i)

            if len(list_unique_product) > 0:
                return list_unique_product[0]
            else:
                return None

        # should print "Computer"
        print(first_unique_product(["Apple", "Computer", "Apple", "Bag"]))
        print(first_unique_product(["Apple", "Computer", "Apple", "Computer"]))

    def test_3(self):
        from collections import namedtuple

        def merge(*records):
            """
            :param records: (varargs list of namedtuple) The patient details.
            :returns: (namedtuple) named Patient, containing details from all records, in entry order.
            """

            Patient = namedtuple('Patient', ['date_of_birth', 'eye_color', 'hair_color'])

            return Patient(personal_details.date_of_birth, complexion.eye_color, complexion.hair_color)

        PersonalDetails = namedtuple('PersonalDetails', ['date_of_birth'])
        personal_details = PersonalDetails(date_of_birth='06-04-1972')

        Complexion = namedtuple('Complexion', ['eye_color', 'hair_color'])
        complexion = Complexion(eye_color='Blue', hair_color='Black')

        print(merge(personal_details, complexion))

    def test_4(self):
        print("test_4")

        import json
        from operator import itemgetter

        def same_value(products):
            from collections import defaultdict
            some_dict = {'abc': 'a', 'cdf': 'b', 'gh': 'a', 'fh': 'g', 'hfz': 'g'}
            new_dict = defaultdict(list)
            for k, v in some_dict.iteritems():
                new_dict[v].append(k)

        def sort_by_price_ascending(json_string):
            data = json.loads(json_string)

            sorted_by_price = sorted(data, key=itemgetter('price'))

            return json.dumps(sorted_by_price)

        print(sort_by_price_ascending(
            '[{"name":"eggs","price":1},{"name":"coffee","price":9.99},{"name":"rice","price":4.04}]')
        )

"""
-- Write only the SQL statement that solves the problem and nothing else
DELETE FROM orders
INNER JOIN customers
on orders.customerid = customers.id
WHERE (SELECT sum(balance) FROM customers) < 0
"""


if __name__ == '__main__':
    unittest.main()
