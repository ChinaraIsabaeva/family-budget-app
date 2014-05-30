__author__ = 'mybudget'
from datetime import datetime
from django import forms
from django.forms.extras.widgets import SelectDateWidget
from mybudget.apps.main.models import Category


class ReportForm(forms.Form):
    start_date = forms.DateField(widget=SelectDateWidget(years=range(2013, 2023, 1)), initial=datetime.today())
    end_date = forms.DateField(widget=SelectDateWidget(years=range(2013, 2023, 1)), initial=datetime.today())
    category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label=None)

    def __unicode__(self):
        return u'%s, %s, %s' % (self.start_date, self.end_date, self.category)
