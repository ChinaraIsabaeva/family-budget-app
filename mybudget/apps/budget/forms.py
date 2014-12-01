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
            'name': TextInput(attrs={'class': 'form-input', 'placeholder': u'Название'}),
            'monthly_replenishment': TextInput(attrs={'class': 'form-input', 'placeholder': u'Месячное пополнение'}),
        }

        labels = {
            'cash': u'Наличными',
            'account': u'Счет'
        }


class ExpensesForm(ModelForm):
    class Meta:
        model = Expenses
        fields = ['name', 'amount', 'envelope']
        widgets = {
            'name': TextInput(attrs={'class': 'form-input', 'placeholder': u'Название'}),
            'amount': TextInput(attrs={'class': 'form-input', 'placeholder': u'Сумма'})
        }

        labels = {
            'envelope': u'Конверт'
        }

