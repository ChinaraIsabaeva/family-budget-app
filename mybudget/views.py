# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.db.models import Sum

from mybudget.lib import disposable_income

from apps.budget.forms import ExpensesForm, EnvelopesForm
from apps.budget.models import Envelopes, Incomes, Accounts, Expenses


def home(request):
    form = ExpensesForm(request.POST or None)
    envelopes = Envelopes.objects.all().order_by('cash', 'name')
    account = Accounts.objects.all().aggregate(total=Sum('current_amount'))
    if form.is_valid():
        form.save()
        return redirect('/')
    else:
        form = ExpensesForm()
    return render(request, 'home.html',
                  {'form': form,
                  'envelopes': envelopes,
                  'account': account})


def dashboard(request):
    form = EnvelopesForm(request.POST or None)
    envelopes = Envelopes.objects.all().order_by('cash', 'name')
    income = Incomes.objects.all().aggregate(total=Sum('amount'))
    available_amount = disposable_income()
    if form.is_valid():
        my_form = form.save(commit=False)
        my_form.current_amount = form.cleaned_data['monthly_replenishment']
        my_form.save()
        return redirect('/envelopes')
    else:
        form = EnvelopesForm()
    return render(request, 'dashboard.html',
                  {'form': form,
                  'envelopes': envelopes,
                  'income': income,
                  'available_amount': available_amount})


def expenses(request):
    our_expenses = Expenses.objects.all().order_by('-created_date', 'name')
    if our_expenses is None:
        return
    return render(request, 'expenses.html', {'expenses': our_expenses})

