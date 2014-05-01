from datetime import datetime
from django import forms
from django.forms.extras.widgets import SelectDateWidget
from .models import *


class IncomesForm(forms.ModelForm):
    date = forms.DateField(widget=SelectDateWidget(years=range(2013, 2023, 1)), initial=datetime.today())

    class Meta:
        model = Incomes
        widgets = {'amount': forms.TextInput}


class ReservesForm(forms.ModelForm):
    date = forms.DateField(widget=SelectDateWidget(years=range(2013, 2023, 1)), initial=datetime.today())

    class Meta:
        model = Reserves
        widgets = {'amount': forms.TextInput, 'name': forms.TextInput(attrs={'autofocus': 'autofocus'})}


class CategoriesForm(forms.ModelForm):

    class Meta:
        model = Category






