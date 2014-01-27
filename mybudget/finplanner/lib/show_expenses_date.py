__author__ = 'dachee'
import datetime



def show_expenses_start_date():
    date = datetime.date.today()
    if date.day > 27:
        start_date = datetime.date(date.year, date.month, 28)
    else:
        first_day_current_month = datetime.date(date.year, date.month, 1)
        last_day_previous_month = first_day_current_month - datetime.timedelta(days=1)
        start_date = datetime.date(last_day_previous_month.year, last_day_previous_month.month, 28)
    return start_date




