from django.shortcuts import render, get_list_or_404, redirect
from django.views.generic.edit import CreateView
from django.contrib import messages
from django.db.models import Sum
from .models import Expenses
from .forms import ExpensesForm
from mybudget.lib import *

# Create your views here.


def expenses(request):
    date = datetime.datetime.today().strftime('%B %Y')
    my_expenses = get_list_or_404(Expenses.objects.filter(date__range=(start_date(), datetime.datetime.today())))
    expenses_sum = Expenses.objects.filter(date__range=(start_date(),
                                                        datetime.datetime.today())).aggregate(Sum('amount'))['amount__sum']
    return render(request, 'expenses.html', {'expenses': my_expenses, 'expenses_sum': expenses_sum, 'date': date})


class ExpenseCreate(CreateView):
    form_class = ExpensesForm
    fields = '__all__'
    template_name = 'expenseform.html'
    success_url = '/expenses/add/'

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Data updated')
        return redirect(self.success_url)
