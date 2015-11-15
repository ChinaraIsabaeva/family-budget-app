# -*- coding: utf-8 -*-

from django.forms import Form, ModelForm, TextInput, ModelChoiceField, CheckboxInput

from .models import Envelopes
from mybudget.apps.general.models import Accounts


class EnvelopesForm(ModelForm):
    account = ModelChoiceField(queryset=Accounts.objects.all(), empty_label=None)

    class Meta:
        model = Envelopes
        fields = ['name', 'monthly_replenishment', 'cash', 'account', 'closed', 'onetime_envelope', 'max_amount']
        widgets = {
            'name': TextInput(attrs={'class': 'form-input', 'placeholder': u'Название'}),
            'monthly_replenishment': TextInput(attrs={'class': 'form-input', 'placeholder': u'Месячное пополнение'}),
            'max_amount': TextInput(attrs={'class': 'form-input', 'placeholder': u'Максимальная сумма конверта'}),
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


class EnvelopeSelectForm(Form):
    envelope = ModelChoiceField(queryset=Envelopes.objects.all().order_by('name'))