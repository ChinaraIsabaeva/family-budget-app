# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand
from django.db.models import Sum
from django.db import transaction

from mybudget.apps.budget.models import Envelopes, Incomes, Accounts, RegularMonthlyExpenses


class Command(BaseCommand):

    def handle(self, *args, **options):
        """ Команда для расчета суммы счета на начало месяца. К текущей сумме счета прибавляется доход (ЗП)
        вычитаются все регулярные месячные расходы и месячная сумма наличных конвертов. Это сумма становится
        "текушей суммой" счета.
        """
        try:
            with transaction.atomic():
                accounts_beginning = Accounts.objects.all().aggregate(total=Sum('current_amount'))
                regular_expenses = RegularMonthlyExpenses.objects.all().aggregate(total=Sum('amount'))
                incomes = Incomes.objects.all().aggregate(total=Sum('amount'))
                accounts_ending = accounts_beginning['total'] + incomes['total'] - regular_expenses['total']
                account = Accounts.objects.get(id=1)
                account.current_amount = accounts_ending
                account.save()
                envelopes = Envelopes.objects.all()
                for envelope in envelopes:
                    if envelope.closed is False:
                        envelope.current_amount = envelope.current_amount + envelope.monthly_replenishment
                        envelope.save()
                print 'Done!'
        except:
            print 'Something goes wrong!'