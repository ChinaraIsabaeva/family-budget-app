__author__ = 'mybudget'
import datetime


def current_month_start_day(date):
    if date.day < 28:
        current_month_first_day = datetime.date(date.year, date.month, 1)
        previous_month_last_day = current_month_first_day - datetime.timedelta(1)
        start_day = datetime.date(previous_month_last_day.year, previous_month_last_day.month, 28)
    else:
        start_day = datetime.date(date.year, date.month, 28)
    return start_day


def current_month_last_day(date):
    if date.day < 28:
        last_day = datetime.date(date.year, date.month, 27)
    else:

        next_month_some_day = date - datetime.timedelta(4)
        last_day = datetime.date(next_month_some_day.year, next_month_some_day.month, 27)
    return last_day

def previous_month(date):
    previous_month_last_day = current_month_start_day(date) + datetime.timedelta(1)
    previous_month_start_day = datetime.date(previous_month_last_day.year, previous_month_last_day.month, 28)
    return previous_month_start_day


def next_month(date):
    next_month_start_day = current_month_last_day(date) + datetime.timedelta(1)
    return next_month_start_day


