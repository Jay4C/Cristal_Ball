import json
from bs4 import BeautifulSoup
import requests
import time
import pymysql.cursors
import unittest
from validate_email import validate_email
import xlsxwriter


class UnitTestsDataMinerYellowPagesBangladesh(unittest.TestCase):
    def test_extract_email_from_one_result(self):
        print("test_extract_email_from_one_result")

    def test_extract_email_from_website_from_one_result(self):
        print("test_extract_email_from_website_from_one_result")

    def test_extract_each_email_from_one_page_of_results_for_one_activity_and_one_capital(self):
        print("test_extract_each_email_from_one_page_of_results_for_one_activity_and_one_capital")

    def test_extract_each_email_from_all_pages_of_results_for_one_activity_and_one_capital(self):
        print("test_extract_each_email_from_all_pages_of_results_for_one_activity_and_one_capital")

    def test_extract_each_email_from_all_pages_of_results_for_all_activities_and_all_capitals(self):
        print("test_extract_each_email_from_all_pages_of_results_for_all_activities_and_all_capitals")


if __name__ == '__main__':
    unittest.main()
