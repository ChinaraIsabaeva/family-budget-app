from django.shortcuts import render, get_list_or_404
from django.http import HttpResponseRedirect
from django.db.models import Sum
from mybudget.finplanner.forms import *
from mybudget.finplanner.models import *


# Create your views here.
def home(request):
    reserves_sum = Reserves.objects.filter(category=10).aggregate(Sum('amount'))['amount__sum']
    buffer_sum = Reserves.objects.filter(category=11).aggregate(Sum('amount'))['amount__sum']
    if request.method == 'POST':
        expenses_form = ExpensesForm(request.POST)
        if expenses_form.is_valid():
            expenses_form.save()
            return HttpResponseRedirect('/submitted/')
    else:
        expenses_form = ExpensesForm()
    return render(request, 'home.html',
                  {'expenses_form': expenses_form, 'reserves_sum': reserves_sum, 'buffer_sum': buffer_sum})

def forms(request):
    return render(request, 'forms.html')


def expense_form(request):
    if request.method == 'POST':
        expenses_form = ExpensesForm(request.POST)
        if expenses_form.is_valid():
            expenses_form.save()
            return HttpResponseRedirect('/submitted/')
    else:
        expenses_form = ExpensesForm()
    return render(request, 'expenseform.html', {'expenses_form': expenses_form})


def income_form(request):
    if request.method == 'POST':
        expenses_form = ExpensesForm(request.POST)
        incomes_form = IncomesForm(request.POST)
        reserves_form = ReservesForm(request.POST)
        if expenses_form.is_valid():
            expenses_form.save()
            return HttpResponseRedirect('/submitted/')
        if incomes_form.is_valid():
            incomes_form.save()
            return HttpResponseRedirect('/submitted/')
        if reserves_form.is_valid():
            reserves_form.save()
            return HttpResponseRedirect('/submitted/')
    else:
        expenses_form = ExpensesForm()
        incomes_form = IncomesForm()
        reserves_form = ReservesForm()
    return render(request, 'forms.html', {
        'expenses_form': expenses_form, 'incomes_form': incomes_form, 'reserves_form': reserves_form
    })


def reserve_form(request):
    if request.method == 'POST':
        expenses_form = ExpensesForm(request.POST)
        incomes_form = IncomesForm(request.POST)
        reserves_form = ReservesForm(request.POST)
        if expenses_form.is_valid():
            expenses_form.save()
            return HttpResponseRedirect('/submitted/')
        if incomes_form.is_valid():
            incomes_form.save()
            return HttpResponseRedirect('/submitted/')
        if reserves_form.is_valid():
            reserves_form.save()
            return HttpResponseRedirect('/submitted/')
    else:
        expenses_form = ExpensesForm()
        incomes_form = IncomesForm()
        reserves_form = ReservesForm()
    return render(request, 'forms.html', {
        'expenses_form': expenses_form, 'incomes_form': incomes_form, 'reserves_form': reserves_form
    })


def submitted(request):
    return render(request, 'submitted.html')


def expenses(request):
    my_expenses = get_list_or_404(Expenses)
    expenses_sum = Expenses.objects.aggregate(Sum('amount'))['amount__sum']
    return render(request, 'expenses.html', {'expenses':my_expenses, 'expenses_sum': expenses_sum})