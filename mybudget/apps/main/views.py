import datetime

from django.shortcuts import render, get_list_or_404, redirect
from django.db.models import Sum
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages

from .forms import *
from .models import *
from mybudget.apps.expenses.forms import ExpensesForm
from mybudget.apps.expenses.models import Expenses
from mybudget.apps.reports.forms import ReportForm


def home(request):
    if request.method == 'POST':
        form = ExpensesForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "Data updates")
            return redirect('/expenses/add/')
    else:
        form = ExpensesForm()
    return render(request, 'home.html', {'form': form})


def reserves(request):
    reserves_sum = Reserves.objects.filter(category=10).aggregate(Sum('amount'))['amount__sum']
    buffer_sum = Reserves.objects.filter(category=11).aggregate(Sum('amount'))['amount__sum']
    return render(request, 'reserves.html', {'reserves_sum': reserves_sum, 'buffer_sum': buffer_sum})


class ReserveCreate(CreateView):
    form_class = ReservesForm
    fields = ['name', 'amount', 'category', 'periodicity', 'date']
    template_name = 'reserveform.html'
    success_ulr = '/reserves/'

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Data updated')
        return redirect(self.success_ulr)

    
class ReserveUpdate(UpdateView):
    model = Reserves
    fields = ['name']


class ReserveDelete(DeleteView):
    model = Reserves
    success_url = reverse_lazy('reserves-list')



