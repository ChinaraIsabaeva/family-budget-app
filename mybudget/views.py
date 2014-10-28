from django.shortcuts import render, redirect
from django.db.models import Sum

from mybudget.lib import disposable_income

from apps.budget.forms import ExpensesForm, EnvelopesForm
from apps.budget.models import Envelopes, Incomes, Accounts


def home(request):
    form = ExpensesForm(request.POST or None)
    envelopes = Envelopes.objects.all()
    income = Incomes.objects.all().aggregate(total=Sum('amount'))
    account = Accounts.objects.all().aggregate(total=Sum('current_amount'))
    available_amount = disposable_income()
    if form.is_valid():
        form.save()
        return redirect('/')
    else:
        form = ExpensesForm()
    return render(request, 'home.html',
                  {'form': form,
                  'envelopes': envelopes,
                  'income': income,
                  'account': account,
                  'available_amount': available_amount})


def dashboard(request):
    form = EnvelopesForm(request.POST or None)
    envelopes = Envelopes.objects.all()
    income = Incomes.objects.all().aggregate(total=Sum('amount'))
    account = Accounts.objects.all().aggregate(total=Sum('current_amount'))
    available_amount = disposable_income()
    if form.is_valid():
        form.save(commit=False)
        form.cleaned_data['current_amount'] = form.cleaned_data['monthly_replenishment']
        form.save()
        return redirect('/envelopes')
    else:
        form = EnvelopesForm()
    return render(request, 'dashboard.html',
                  {'form': form,
                  'envelopes': envelopes,
                  'income': income,
                  'account': account,
                  'available_amount': available_amount})


