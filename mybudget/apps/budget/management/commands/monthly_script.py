from django.core.management.base import BaseCommand
from django.db.models import Sum
from mybudget.apps.budget.models import Envelopes, Incomes, Accounts, RegularMonthlyExpenses


class Command(BaseCommand):
    can_import_settings = True

    def handle(self, *args, **options):
        """ Команда для расчета суммы счета на начало месяца. К текущей сумме счета прибавляется доход (ЗП)
        вычитаются все регулярные месячные расходы и месячная сумма наличных конвертов. Это сумма становится
        "текушей суммой" счета.
        """

        envelopes_cash = Envelopes.objects.all().exclude(cash=False).aggregate(total=Sum('monthly_replenishment'))
        accounts_beginning = Accounts.objects.all().aggregate(total=Sum('current_amount'))
        regular_expenses = RegularMonthlyExpenses.objects.all().aggregate(total=Sum('amount'))
        incomes = Incomes.objects.all().aggregate(total=Sum('amount'))
        accounts_ending = accounts_beginning['total'] + incomes['total'] - regular_expenses['total'] - envelopes_cash['total']
        account = Accounts.objects.get(id=1)
        account.current_amount = accounts_ending
        account.save()

