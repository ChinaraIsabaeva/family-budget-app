# -*- coding: utf-8 -*-

from django.forms import ModelForm, TextInput

from .models import RegularMonthlyExpenses, Envelopes, Expenses


class RegularExpensesForm(ModelForm):
    class Meta:
        model = RegularMonthlyExpenses


class EnvelopesForm(ModelForm):
    class Meta:
        model = Envelopes
        fields = ['name', 'monthly_replenishment', 'cash', 'account']
        widgets = {
            'name': TextInput(attrs={'class': 'form-input', 'placeholder': u'Name'}),
            'monthly_replenishment': TextInput(attrs={'class': 'form-input', 'placeholder': u'Monthly_replenishment'}),
        }

        labels = {
            'cash': u'Cash',
            'account': u'Account'
        }


class ExpensesForm(ModelForm):
    class Meta:
        model = Expenses
        fields = ['name', 'amount', 'envelope']
        widgets = {
            'name': TextInput(attrs={'class': 'form-input', 'placeholder': u'Name'}),
            'amount': TextInput(attrs={'class': 'form-input', 'placeholder': u'Amount'})
        }

        labels = {
            'envelope': u'Envelope'
        }

