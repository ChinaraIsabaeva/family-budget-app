from django.forms import ModelForm, TextInput, DateField
from django.forms.extras.widgets import SelectDateWidget
from datetime import datetime
from mybudget.finplanner.models import *



class ExpensesForm(ModelForm):
    date = DateField(widget=SelectDateWidget(years=range(2013, 2023, 1)), initial=datetime.today())
    class Meta:
        model = Expenses
        widgets = {'amount': TextInput, 'name': TextInput(attrs={'autofocus':'autofocus'})}

class IncomesForm(ModelForm):
    date = DateField(widget=SelectDateWidget(years=range(2013, 2023, 1)), initial=datetime.today())
    class Meta:
        model = Incomes
        widgets = {'amount': TextInput}

class ReservesForm(ModelForm):
    date = DateField(widget=SelectDateWidget(years=range(2013, 2023, 1)), initial=datetime.today())
    class Meta:
        model = Reserves
        widgets = {'amount': TextInput, 'name': TextInput(attrs={'autofocus':'autofocus'})}

class CategoriesForm(ModelForm):
    class Meta:
        model = Category



