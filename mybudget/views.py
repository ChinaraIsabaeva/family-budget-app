# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.db.models import Sum

from mybudget.apps.envelopes.models import Envelopes
from mybudget.apps.expenses.forms import ExpensesForm
from apps.general.models import Accounts


def home(request):
    form = ExpensesForm(request.POST or None, initial={'envelope': '1'})
    envelopes = Envelopes.objects.exclude(closed=True).order_by('cash', 'name')
    account = Accounts.objects.all().aggregate(total=Sum('current_amount'))
    if account['total'] is None:
        account_total = 0
    else:
        account_total = account['total']
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'home.html',
                  {'form': form,
                  'envelopes': envelopes,
                  'account': account_total})




