from django.db.models import Sum

from apps.budget.models import Envelopes, Incomes, Accounts, RegularMonthlyExpenses


def month_begin():
    envelopes_cash = Envelopes.objects.all().exclude(cash=False).aggregate(total=Sum('current_amount'))
    accounts_beginning = Accounts.objects.all().aggregate(total=Sum('current_amount'))
    regular_expenses = RegularMonthlyExpenses.objects.all().aggregate(total=Sum('amount'))
    incomes = Incomes.objects.all().aggregate(total=Sum('amount'))
    accounts_ending = accounts_beginning['total'] + incomes['total'] - regular_expenses['total'] - envelopes_cash['total']
    account = Accounts.objects.get(id=1)
    account.current_amount = accounts_ending
    account.save()
