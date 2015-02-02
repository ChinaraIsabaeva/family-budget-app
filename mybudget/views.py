# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum
from django.views.generic import ListView, UpdateView

from mybudget.lib import disposable_income

from apps.budget.forms import ExpensesForm, EnvelopesForm
from apps.budget.models import Envelopes, Incomes, Accounts, Expenses


def home(request):
    form = ExpensesForm(request.POST or None, initial={'envelope': '1'})
    envelopes = Envelopes.objects.all().order_by('cash', 'name')
    account = Accounts.objects.all().aggregate(total=Sum('current_amount'))
    if account['total'] is None:
        account_total = 0
    else:
        account_total = account['total']
    if form.is_valid():
        form.save()
        return redirect('/')
    else:
        form = ExpensesForm(initial={'envelope': '1'})
    return render(request, 'home.html',
                  {'form': form,
                  'envelopes': envelopes,
                  'account': account_total})


def dashboard(request):
    form = EnvelopesForm(request.POST or None, initial={'account': '1'})
    envelopes = Envelopes.objects.all().order_by('name', 'cash')
    income = Incomes.objects.all().aggregate(total=Sum('amount'))
    available_amount = disposable_income()
    if income['total'] is None:
        income_total = 0
    else:
        income_total = income['total']
    if form.is_valid():
        my_form = form.save(commit=False)
        my_form.current_amount = form.cleaned_data['monthly_replenishment']
        my_form.save()
        return redirect('/envelopes/')
    else:
        form = EnvelopesForm()
    return render(request, 'dashboard.html',
                  {'form': form,
                  'envelopes': envelopes,
                  'income': income_total,
                  'available_amount': available_amount})


class EnvelopeUpdate(UpdateView):
    model = Envelopes
    success_url = '/envelopes/'
    template_name = 'envelopes/envelope_update.html'
    form_class = EnvelopesForm

    def post(self, request, pk):
        envelope = Envelopes.objects.get(pk=pk)
        form = EnvelopesForm(request.POST or None, instance=envelope)
        if form.is_valid():
            envelope.save()
            return redirect('/envelopes/')
        else:
            message = "Envelope didn't update, some problem occurred"
            return redirect('/envelopes/', message=message)


class ExpensesList(ListView):
    model = Expenses
    queryset = Expenses.objects.all().order_by('-created_date', 'name')
    template_name = 'expenses/expenses.html'


class ExpenseUpdate(UpdateView):
    model = Expenses
    success_url = '/expenses/'
    template_name = 'expenses/expense_update.html'
    form_class = ExpensesForm

    def post(self, request, pk):
        expense = Expenses.objects.get(pk=pk)
        form = ExpensesForm(request.POST or None, instance=expense)
        if form.is_valid():
            expense.update()
            return redirect('/expenses/')
        else:
            message = "Expense didn't update, some problem occurred"
            return redirect('/expenses/', message=message)



