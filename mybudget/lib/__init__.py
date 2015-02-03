from django.db.models import Sum

from mybudget.apps.budget.models import Envelopes, Incomes, RegularMonthlyExpenses


def disposable_income():
    incomes = Incomes.objects.all().aggregate(total=Sum('amount'))
    regular_expenses = RegularMonthlyExpenses.objects.all().aggregate(total=Sum('amount'))
    envelopes = Envelopes.objects.all().filter(closed=False).aggregate(total=Sum('monthly_replenishment'))
    if incomes['total'] is None:
        incomes_total = 0
    else:
        incomes_total = incomes['total']
    if regular_expenses['total'] is None:
        regular_expenses_total = 0
    else:
        regular_expenses_total = regular_expenses['total']
    if envelopes['total'] is None:
        envelopes_total = 0
    else:
        envelopes_total = envelopes['total']
    available_amount = incomes_total - regular_expenses_total - envelopes_total
    return available_amount