# -*- coding: utf-8 -*-

from django.forms import (
    Form, ModelForm, TextInput, ModelChoiceField,
    CheckboxInput, ValidationError, Select)

from mybudget.envelopes.models import Envelopes


class EnvelopesForm(ModelForm):
    class Meta:
        model = Envelopes
        fields = [
            'name',
            'monthly_replenishment',
            'closed',
            'onetime_envelope',
            'max_amount'
        ]
        widgets = {
            'name': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': u'Название'
                }
            ),
            'monthly_replenishment': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': u'Месячное пополнение'
                }
            ),
            'max_amount': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': u'Максимальная сумма конверта'
                }
            ),
            'onetime_envelope': CheckboxInput(attrs={'class': 'checkbox'}),
            'closed': CheckboxInput(attrs={'class': 'checkbox'})
        }

        labels = {
            'closed': u'Закрыт',
            'onetime_envelope': u'Разовый'
        }

    def clean_max_amount(self):
        cleaned_data = self.cleaned_data
        onetime_envelope = cleaned_data['onetime_envelope']
        max_amount = cleaned_data.get('max_amount', 0)
        if onetime_envelope:
            if max_amount is None:
                raise ValidationError(u"Максимальная сумма обязательна для разового конверта")
        return max_amount

    def __init__(self, *args, **kwargs):
        super(EnvelopesForm, self).__init__(*args, **kwargs)
        message = u'Проебал что-то указать'
        for field in self.fields:
            self.fields[field].error_messages['required'] = message


class EnvelopeSelectForm(Form):
    choices = Envelopes.objects.all()
    envelope = ModelChoiceField(
        queryset=Envelopes.objects.all().order_by('name'),
        widget=Select(attrs={'class': 'form-control max-width'}),
        empty_label=u'Выбрать конверт'
    )
