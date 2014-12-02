# -*- coding: utf-8 -*-

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

        envelopes = Envelopes.objects.all()
        for envelope in envelopes:
            envelope.current_amount = envelope.current_amount + envelope.monthly_replenishment
            envelope.save()


