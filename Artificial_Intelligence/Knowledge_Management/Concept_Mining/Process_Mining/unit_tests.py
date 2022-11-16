import unittest
from usp.tree import sitemap_tree_for_homepage


class UnitTestsProcessMining(unittest.TestCase):
    def test_get_a_sitemap_of_a_website(self):
        print("test_get_a_sitemap_of_a_website")

        tree = sitemap_tree_for_homepage('https://www.holomorphe.com/')

        # all_pages() returns an Iterator
        for page in tree.all_pages():
            print(page)


if __name__ == '__main__':
    unittest.main()
