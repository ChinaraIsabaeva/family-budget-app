# -*- coding: utf-8 -*-

from django.db import transaction
from django.db.models import Sum
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import UpdateView, ListView, CreateView

from mybudget.envelopes.models import Envelopes
from mybudget.expenses.forms import ExpensesForm
from mybudget.expenses.models import RegularMonthlyExpenses, Expenses
from mybudget.general.models import Accounts


class ExpenseListView(ListView):
    model = Expenses
    template_name = 'expenses/expenses.html'
    paginate_by = 25
    context_object_name = 'expenses'

    def get_context_data(self, **kwargs):
        context = super(ExpenseListView, self).get_context_data(**kwargs)
        return context


class ExpenseUpdateView(UpdateView):
    model = Expenses
    template_name = 'expenses/expense_update.html'
    form_class = ExpensesForm

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        with transaction.atomic():
            form = self.get_form()
            envelope = Envelopes.objects.get(pk=self.object.envelope_id)
            expense_amount = self.object.amount
            envelope.current_amount = envelope.current_amount + expense_amount
            envelope.save()
            if envelope.cash is False:
                account = Accounts.objects.get(id=envelope.account.id)
                account.current_amount = account.current_amount + expense_amount
                account.save()
            if form.is_valid():
                form.save()
                return redirect(reverse('expenses:all'))
            else:
                return self.form_invalid(form)


class ExpenseCreateView(CreateView):
    model = Expenses
    form_class = ExpensesForm

    def get_success_url(self):
        return reverse('expenses:all')


class RegularExpenseListView(ListView):
    template_name = 'expenses/regular_expenses.html'
    model = RegularMonthlyExpenses
    context_object_name = 'expenses'

    def get_context_data(self, **kwargs):
        context = super(RegularExpenseListView, self).get_context_data(**kwargs)
        sum_regular_expenses = RegularMonthlyExpenses.objects.all().aggregate(
            total=Sum('amount')
        )
        context['sum'] = sum_regular_expenses
        return context
