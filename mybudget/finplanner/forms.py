from django.forms import ModelForm, TextInput
from mybudget.finplanner.models import *


class ExpensesForm(ModelForm):
    class Meta:
        model = Expenses
        widgets = {'amount': TextInput}

class IncomesForm(ModelForm):
    class Meta:
        model = Incomes
        widgets = {'amount': TextInput}

class ReservesForm(ModelForm):
    class Meta:
        model = Reserves
        widgets = {'amount': TextInput}


