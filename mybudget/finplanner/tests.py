from django.test import TestCase
import datetime
from mybudget.finplanner.lib.show_expenses_date import show_expenses_start_date
# Create your tests here.


class ExpensesDateMethodTests(TestCase):

    def test_different_years(self):
        date = datetime.date(2014, 1, 1)
        self.assertEqual(show_expenses_start_date(date).strftime('%Y, %m, %d'), '2013, 12, 28')

    def test_edge_one(self):
        date = datetime.date(2014, 1, 27)
        self.assertEqual(show_expenses_start_date(date).strftime('%Y, %m, %d'), '2013, 12, 28')

    def test_edge_two(self):
        date = datetime.date(2014, 1, 28)
        self.assertEqual(show_expenses_start_date(date).strftime('%Y, %m, %d'), '2014, 01, 28')

    def test_check_feb_one(self):
        date = datetime.date(2014, 2, 27)
        self.assertEqual(show_expenses_start_date(date).strftime('%Y, %m, %d'), '2014, 01, 28')

    def test_check_feb_two(self):
        date = datetime.date(2014, 2, 28)
        self.assertEqual(show_expenses_start_date(date).strftime('%Y, %m, %d'), '2014, 02, 28')


