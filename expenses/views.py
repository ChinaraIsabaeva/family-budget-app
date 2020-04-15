# -*- coding: utf-8 -*-

from django.db import transaction
from django.db.models import Sum
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import UpdateView, ListView, CreateView

from envelopes.forms import EnvelopeSelectForm
from envelopes.models import Envelopes
from expenses.forms import ExpensesForm
from expenses.models import RegularMonthlyExpenses, Expenses
from core.models import Accounts


class ExpenseListView(ListView):
    model = Expenses
    template_name = 'expenses/expenses.html'
    paginate_by = 25
    context_object_name = 'expenses'

    def get_queryset(self):
        queryset = super(ExpenseListView, self).get_queryset()
        if 'envelope' in self.request.GET.keys():
            envelope_id = self.request.GET.get('envelope')
            queryset = queryset.filter(envelope__id=envelope_id)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(ExpenseListView, self).get_context_data(**kwargs)
        context['form'] = EnvelopeSelectForm()
        if 'envelope' in self.request.GET.keys():
            context['form'] = EnvelopeSelectForm(
                initial={'envelope': self.request.GET.get('envelope')}
            )
            expenses = self.get_queryset()
            envelope_id = self.request.GET.get('envelope')
            context['expenses_total'] = expenses.aggregate(total=Sum('amount'))
            context['envelope'] = Envelopes.objects.get(id=envelope_id)
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
