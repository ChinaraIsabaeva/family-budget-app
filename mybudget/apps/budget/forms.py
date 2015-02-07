# -*- coding: utf-8 -*-
import datetime

from django.forms import ModelForm, TextInput, ModelChoiceField, CheckboxInput, Form, DateField
from django.forms.extras.widgets import SelectDateWidget

from .models import RegularMonthlyExpenses, Envelopes, Expenses, Accounts


class RegularExpensesForm(ModelForm):
    class Meta:
        model = RegularMonthlyExpenses


class EnvelopesForm(ModelForm):
    account = ModelChoiceField(queryset=Accounts.objects.all(), empty_label=None)

    class Meta:
        model = Envelopes
        fields = ['name', 'monthly_replenishment', 'cash', 'account', 'closed', 'onetime_envelope', 'max_amount']
        widgets = {
            'name': TextInput(attrs={'class': 'form-input', 'placeholder': u'Название'}),
            'monthly_replenishment': TextInput(attrs={'class': 'form-input', 'placeholder': u'Месячное пополнение'}),
            'max_amount': TextInput(attrs={'class': 'form-input', 'placeholder': u'Максимальная сумма коверта'}),
            'cash': CheckboxInput(attrs={'class': 'checkbox'}),
            'onetime_envelope': CheckboxInput(attrs={'class': 'checkbox'}),
            'closed': CheckboxInput(attrs={'class': 'checkbox'})
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
        message = u'Проебал что-то указать'
        for field in self.fields:
            self.fields[field].error_messages['required'] = message


class ExpensesForm(ModelForm):
    envelope = ModelChoiceField(queryset=Envelopes.objects.all().order_by('name'), empty_label=None)

    class Meta:
        model = Expenses
        fields = ['name', 'amount', 'envelope']
        widgets = {
            'name': TextInput(attrs={'class': 'form-input', 'placeholder': u'Название'}),
            'amount': TextInput(attrs={'class': 'form-input', 'placeholder': u'Сумма'}),
        }

        labels = {
            'envelope': u'Конверт'
        }

    def __init__(self, *args, **kwargs):
        super(ExpensesForm, self).__init__(*args, **kwargs)
        message = u'Проебал что-то указать'
        for field in self.fields:
            self.fields[field].error_messages['required'] = message


class ExpenseSelectForm(Form):
    envelope = ModelChoiceField(queryset=Envelopes.objects.all().order_by('name'), empty_label=None)