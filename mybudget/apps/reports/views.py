from django.shortcuts import render, get_list_or_404
from django.db.models import Sum
from .forms import ReportForm
from mybudget.apps.expenses.models import Expenses


def report(request):
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            category_id = form.cleaned_data['category'].id
            category = form.cleaned_data['category'].name
            start_date = form.cleaned_data['start_date'].strftime('%Y-%m-%d')
            end_date = form.cleaned_data['end_date'].strftime('%Y-%m-%d')
            shown_expenses = get_list_or_404(Expenses.objects.filter(date__range=(start_date, end_date),
                                                                     category_id=category_id))
            expenses_sum = Expenses.objects.filter(date__range=(start_date, end_date),
                                                   category_id=category_id).aggregate(Sum('amount'))['amount__sum']
            return render(request, 'report_show.html',
                          {'expenses': shown_expenses, 'category': category, 'expenses_sum': expenses_sum})
    else:
        form = ReportForm()
    return render(request, 'reports.html', {'form': form})