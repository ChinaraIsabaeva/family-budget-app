from django.db.models import Sum
from core.models import Incomes
from envelopes.models import Envelopes
from expenses.forms import ExpensesForm
from expenses.models import RegularMonthlyExpenses
from core.utils import disposable_income


def get_aggregated_data(request):
    income = Incomes.objects.all().aggregate(total=Sum('amount'))
    available_amount = disposable_income()
    if income['total'] is None:
        income_total = 0
    else:
        income_total = income['total']

    total_envelopes = Envelopes.objects.filter(
        closed=False).aggregate(total=Sum('current_amount'))
    if total_envelopes['total'] is None:
        total_envelopes = 0
    else:
        total_envelopes = total_envelopes['total']

    total_envelopes_monthly = Envelopes.objects.filter(
        closed=False).aggregate(total=Sum('monthly_replenishment'))
    if total_envelopes_monthly['total'] is None:
        total_envelopes_monthly = 0
    else:
        total_envelopes_monthly = total_envelopes_monthly['total']

    sum_regular_expenses = RegularMonthlyExpenses.objects.all().aggregate(
        total=Sum('amount')
    )
    if sum_regular_expenses['total'] is None:
        sum_regular_expenses = 0
    else:
        sum_regular_expenses = sum_regular_expenses['total']

    context = {
        'available_amount': available_amount,
        'income': income_total,
        'total_envelopes': total_envelopes,
        'total_envelopes_monthly': total_envelopes_monthly,
        'total_regular': sum_regular_expenses
    }
    return context


def get_expense_form(request):
    form = ExpensesForm()
    return {'expense_form': form}
