# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.db.models import Sum
from django.db import transaction
from django.views.generic import UpdateView

from .models import RegularMonthlyExpenses, Expenses
from .forms import ExpensesForm
from mybudget.apps.general.models import Accounts
from mybudget.apps.envelopes.models import Envelopes
from mybudget.apps.envelopes.forms import EnvelopeSelectForm


def all_expenses(request):
    expenses = Expenses.objects.all().order_by('-created_date', 'name')
    form = EnvelopeSelectForm(request.POST or None)
    return render(request, 'expenses/expenses.html', {'expenses': expenses, 'form': form})


def expenses_by_envelope(request, envelope):
    selected_envelope = Envelopes.objects.get(name=envelope)
    filtered_expenses = Expenses.objects.all().filter(envelope=selected_envelope.id).order_by('-created_date')
    sum_filtered_expenses = filtered_expenses.aggregate(total=Sum('amount'))
    envelope_sum = selected_envelope.current_amount
    form = EnvelopeSelectForm(request.POST or None)
    return render(request, 'expenses/expenses_by_envelope.html',
                  {'expenses': filtered_expenses,
                   'expenses_sum': sum_filtered_expenses,
                   'envelope_name': selected_envelope,
                   'envelope_sum': envelope_sum,
                   'form': form})


class ExpenseUpdate(UpdateView):
    model = Expenses
    template_name = 'expenses/expense_update.html'
    form_class = ExpensesForm

    def post(self, request, pk):
        with transaction.atomic():
            expense = Expenses.objects.get(pk=pk)
            form = ExpensesForm(request.POST or None, instance=expense)
            envelope = Envelopes.objects.get(pk=expense.envelope_id)
            expense_amount = expense.amount
            envelope.current_amount = envelope.current_amount + expense_amount
            envelope.save()
            if envelope.cash is False:
                account = Accounts.objects.get(id=envelope.account.id)
                account.current_amount = account.current_amount + expense_amount
                account.save()
            if form.is_valid():
                form.save()
                return redirect(reverse('expenses:all'))


def regular_expenses(request):
    all_regular_expenses = RegularMonthlyExpenses.objects.all()
    sum_regular_expenses = RegularMonthlyExpenses.objects.all().aggregate(total=Sum('amount'))
    return render(request, 'expenses/regular_expenses.html',
                  {'expenses': all_regular_expenses, 'sum': sum_regular_expenses})