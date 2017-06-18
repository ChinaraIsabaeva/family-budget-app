# -*- coding: utf-8 -*-

from django.views.generic import TemplateView

from mybudget.envelopes.models import Envelopes
from mybudget.expenses.forms import ExpensesForm


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        envelopes = Envelopes.objects.exclude(closed=True).order_by('cash', 'name')
        context['envelopes'] = envelopes
        return context
