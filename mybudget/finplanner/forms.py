from django.forms import ModelForm
from mybudget.finplanner.models import Expenses


class ExpensesForm(ModelForm):
    class Meta:
        model = Expenses
