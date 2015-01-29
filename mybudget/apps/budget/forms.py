# -*- coding: utf-8 -*-

from django.forms import ModelForm, TextInput

from .models import RegularMonthlyExpenses, Envelopes, Expenses


class RegularExpensesForm(ModelForm):
    class Meta:
        model = RegularMonthlyExpenses


class EnvelopesForm(ModelForm):
    class Meta:
        model = Envelopes
        fields = ['name', 'monthly_replenishment', 'cash', 'account', 'closed', 'onetime_envelope', 'max_amount']
        widgets = {
            'name': TextInput(attrs={'class': 'form-input', 'placeholder': u'Название'}),
            'monthly_replenishment': TextInput(attrs={'class': 'form-input', 'placeholder': u'Месячное пополнение'}),
            'max_amount': TextInput(attrs={'class': 'form-input', 'placeholder': u'Максимальная сумма коверта'})
        }

        labels = {
            'cash': u'Наличными',
            'account': u'Счет',
            'closed': u'Закрыт',
            'onetime_envelope': u'Разовый'
        }

    def __init__(self, *args, **kwargs):
        super(EnvelopesForm, self).__init__(*args, **kwargs)
        if self.fields['cash'] is False:
            self.fields['account'].required = True
        if self.fields['onetime_envelope'] is True:
            self.fields['max_amount'].required = True


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
