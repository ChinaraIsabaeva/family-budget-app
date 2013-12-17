from django.shortcuts import render
from django.http import HttpResponseRedirect
from mybudget.finplanner.forms import *


# Create your views here.
def home(request):
    return render(request, 'home.html')


def forms(request):
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