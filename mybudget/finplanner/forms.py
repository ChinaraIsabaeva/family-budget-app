from django.forms import ModelForm, TextInput, DateField
from django.forms.extras.widgets import SelectDateWidget
from mybudget.finplanner.models import *



class ExpensesForm(ModelForm):
    date = DateField(widget=SelectDateWidget(), initial=datetime.today())
    class Meta:
        model = Expenses
        widgets = {'amount': TextInput}

class IncomesForm(ModelForm):
    date = DateField(widget=SelectDateWidget(), initial=datetime.today())
    class Meta:
        model = Incomes
        widgets = {'amount': TextInput}

class ReservesForm(ModelForm):
    date = DateField(widget=SelectDateWidget(), initial=datetime.today())
    class Meta:
        model = Reserves
        widgets = {'amount': TextInput}


