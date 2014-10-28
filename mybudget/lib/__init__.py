from django.db.models import Sum

from mybudget.apps.budget.models import Envelopes, Incomes, Accounts, RegularMonthlyExpenses


def disposable_income():
    incomes = Incomes.objects.all().aggregate(total=Sum('amount'))
    regular_expenses = RegularMonthlyExpenses.objects.all().aggregate(total=Sum('amount'))
    envelopes = Envelopes.objects.all().aggregate(total=Sum('monthly_replenishment'))
    available_amount = incomes['total'] - regular_expenses['total'] - envelopes['total']
    return available_amount