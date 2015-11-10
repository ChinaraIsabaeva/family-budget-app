# -*- coding: utf-8 -*-

from django.forms import ModelForm, TextInput, ModelChoiceField, Form

from .models import Expenses, RegularMonthlyExpenses
from mybudget.apps.envelopes.models import Envelopes


class RegularExpensesForm(ModelForm):
    class Meta:
        model = RegularMonthlyExpenses
        fields = '__all__'


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
    envelope = ModelChoiceField(queryset=Envelopes.objects.all().order_by('name'))