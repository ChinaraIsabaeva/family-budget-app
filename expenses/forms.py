# -*- coding: utf-8 -*-

from django.forms import ModelForm, TextInput, ModelChoiceField, Select

from envelopes.models import Envelopes
from expenses.models import Expenses, RegularMonthlyExpenses


class RegularExpensesForm(ModelForm):
    class Meta:
        model = RegularMonthlyExpenses
        fields = '__all__'


class ExpensesForm(ModelForm):
    envelope = ModelChoiceField(
        queryset=Envelopes.objects.all().order_by('name'),
        empty_label='-------',
        widget=Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Expenses
        fields = ['name', 'amount', 'envelope']
        widgets = {
            'name': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Название'
                }
            ),
            'amount': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Сумма'
                }
            )
        }

        labels = {
            'envelope': 'Конверт'
        }

    def __init__(self, *args, **kwargs):
        super(ExpensesForm, self).__init__(*args, **kwargs)
        message = 'Проебал что-то указать'
        for field in self.fields:
            self.fields[field].error_messages['required'] = message