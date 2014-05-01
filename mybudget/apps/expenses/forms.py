from datetime import datetime
from django import forms
from django.forms.extras.widgets import SelectDateWidget
from .models import Expenses


class ExpensesForm(forms.ModelForm):
    date = forms.DateField(widget=SelectDateWidget(years=range(2013, 2023, 1)), initial=datetime.today())

    class Meta:
        model = Expenses
        widgets = {'amount': forms.TextInput, 'name': forms.TextInput(attrs={'autofocus': 'autofocus'})}