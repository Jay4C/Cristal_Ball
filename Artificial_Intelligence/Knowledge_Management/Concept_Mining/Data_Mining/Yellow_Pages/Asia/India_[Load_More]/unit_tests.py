import time
from bs4 import BeautifulSoup
import requests
import pymysql.cursors
import unittest


class UnitTestsDataMinerYellowPagesIndia(unittest.TestCase):
    def test_extract_one_email_from_one_result(self):
        print("test_extract_one_email_from_one_result")

    def test_extract_emails_from_all_page_of_results_for_one_activity_and_capital(self):
        print("test_extract_emails_from_all_page_of_results_for_one_activity_and_capital")

    def test_extract_emails_from_all_page_of_results_for_all_activities_and_capitals(self):
        print("test_extract_emails_from_all_page_of_results_for_all_activities_and_capitals")


if __name__ == '__main__':
    unittest.main()
