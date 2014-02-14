from django.shortcuts import render, get_list_or_404
from django.http import HttpResponseRedirect
from django.db.models import Sum
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.core.urlresolvers import reverse_lazy
from mybudget.finplanner.forms import *
from mybudget.finplanner.models import *
import datetime
from mybudget.finplanner.lib.show_expenses_date import show_expenses_start_date


# Create your views here.
def home(request):
    if request.method == 'POST':
        expenses_form = ExpensesForm(request.POST)
        if expenses_form.is_valid():
            expenses_form.save()
            return HttpResponseRedirect('/submitted/')
    else:
        expenses_form = ExpensesForm()
    return render(request, 'home.html',
                  {'expenses_form': expenses_form})


def expense_submitted(request):
    if request.method == 'POST':
        expenses_form = ExpensesForm(request.POST)
        if expenses_form.is_valid():
            expenses_form.save()
            return HttpResponseRedirect('/submitted/')
    else:
        expenses_form = ExpensesForm()
    return render(request, 'expense_submitted.html',
                  {'expenses_form': expenses_form})


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
        incomes_form = IncomesForm(request.POST)
        if incomes_form.is_valid():
            incomes_form.save()
            return HttpResponseRedirect('/submitted/')
    else:
        incomes_form = IncomesForm()
    return render(request, 'forms.html', {'incomes_form': incomes_form})


def reserves(request):
    reserves_sum = Reserves.objects.filter(category=10).aggregate(Sum('amount'))['amount__sum']
    buffer_sum = Reserves.objects.filter(category=11).aggregate(Sum('amount'))['amount__sum']
    return render(request, 'reserves.html', {'reserves_sum': reserves_sum, 'buffer_sum': buffer_sum})


class ReserveForm(FormView):
    template_name = 'reserveform.html'
    form_class = ReservesForm
    success_url = '/submitted/'

    def form_valid(self, form):
        form.save()
        return super(ReservesForm, self).form_valid(form)


class ReservesCreate(CreateView):
    model = Reserves
    fields = ['name']


class ReservesUpdate(UpdateView):
    model = Reserves
    fields = ['name']


class ReservesDelete(DeleteView):
    model = Reserves
    success_url = reverse_lazy('reserves-list')


def expenses(request):
    date = datetime.date.today().strftime('%B %Y')
    my_expenses = get_list_or_404(Expenses.objects.filter(date__range=(show_expenses_start_date(), datetime.date.today())))
    expenses_sum = Expenses.objects.filter(date__range=(show_expenses_start_date(), datetime.date.today())).aggregate(Sum('amount'))['amount__sum']
    return render(request, 'expenses.html', {'expenses': my_expenses, 'expenses_sum': expenses_sum, 'date': date})