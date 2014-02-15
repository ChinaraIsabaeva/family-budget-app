from django.shortcuts import render, get_list_or_404, redirect
from django.db.models import Sum
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
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
            messages.info(request, "Data updates")
            return redirect('/expenses/add/')
    else:
        expenses_form = ExpensesForm()
    return render(request, 'home.html', {'expenses_form': expenses_form})


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
        messages.success(self.request, 'Data updates')
        return redirect(self.success_ulr)

    
class ReserveUpdate(UpdateView):
    model = Reserves
    fields = ['name']


class ReserveDelete(DeleteView):
    model = Reserves
    success_url = reverse_lazy('reserves-list')


def expenses(request):
    date = datetime.date.today().strftime('%B %Y')
    my_expenses = get_list_or_404(Expenses.objects.filter(date__range=(show_expenses_start_date(), datetime.date.today())))
    expenses_sum = Expenses.objects.filter(date__range=(show_expenses_start_date(), datetime.date.today())).aggregate(Sum('amount'))['amount__sum']
    return render(request, 'expenses.html', {'expenses': my_expenses, 'expenses_sum': expenses_sum, 'date': date})

class ExpenseCreate(CreateView):
    form_class = ExpensesForm
    fields = '__all__'
    template_name = 'expenseform.html'
    success_url = '/expenses/add/'

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Data updates')
        return redirect(self.success_url)