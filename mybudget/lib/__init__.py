__author__ = 'dachee'
import datetime


def start_date():
    date = datetime.date.today()
    if date.day > 27:
        start_date = datetime.date(date.year, date.month, 28)
    else:
        start_date = datetime.date(int((datetime.date.today()-datetime.timedelta(days=28)).strftime('%Y')), int((datetime.date.today()-datetime.timedelta(days=28)).strftime('%m')), 28)
    return start_date