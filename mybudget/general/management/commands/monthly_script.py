# -*- coding: utf-8 -*-
import datetime
import logging

from django.core.management.base import BaseCommand
from django.db.models import Sum
from django.db import transaction, IntegrityError

from mybudget.envelopes.models import Envelopes
from mybudget.general.models import Incomes, Accounts
from mybudget.expenses.models import RegularMonthlyExpenses

logger = logging.getLogger(__name__)


class Command(BaseCommand):

    def handle(self, *args, **options):
        """ Команда для расчета суммы счета на начало месяца.
        К текущей сумме счета прибавляется доход (ЗП) и
        вычитаются все регулярные месячные расходы и
        месячная сумма наличных конвертов. Это сумма становится
        "текушей суммой" счета.
        """
        today = datetime.date.today()
        if today.day == 28:
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
            except IntegrityError as e:
                logger.error(e.message)