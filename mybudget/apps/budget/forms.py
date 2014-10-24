from django.forms import ModelForm

from .models import RegularMonthlyExpenses, Envelopes, Expenses


class RegularExpensesForm(ModelForm):
    class Meta:
        model = RegularMonthlyExpenses


class EnvelopesForm(ModelForm):
    class Meta:
        model = Envelopes
        fields = ['name', 'monthly_replenishment', 'cash']


class ExpensesForm(ModelForm):
    class Meta:
        model = Expenses
        fields = ['name', 'amount', 'envelope']

