import datetime

from django.test import TestCase

from mybudget.lib import current_month_start_day

# Create your tests here.


class ExpensesDateMethodTests(TestCase):

    def test_different_years(self):
        date = datetime.date(2014, 1, 1)
        self.assertEqual(current_month_start_day(date).strftime('%Y, %m, %d'), '2013, 12, 28')

    def test_edge_one(self):
        date = datetime.date(2014, 1, 27)
        self.assertEqual(current_month_start_day(date).strftime('%Y, %m, %d'), '2013, 12, 28')

    def test_edge_two(self):
        date = datetime.date(2014, 1, 28)
        self.assertEqual(current_month_start_day(date).strftime('%Y, %m, %d'), '2014, 01, 28')

    def test_check_feb_one(self):
        date = datetime.date(2014, 2, 27)
        self.assertEqual(current_month_start_day(date).strftime('%Y, %m, %d'), '2014, 01, 28')

    def test_check_feb_two(self):
        date = datetime.date(2014, 2, 28)
        self.assertEqual(current_month_start_day(date).strftime('%Y, %m, %d'), '2014, 02, 28')


