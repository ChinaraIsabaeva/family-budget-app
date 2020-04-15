# -*- coding: utf-8 -*-

from django.utils.translation import ugettext_lazy as _
from django.db import models


class Accounts(models.Model):
    name = models.CharField(max_length=255)
    current_amount = models.DecimalField(max_digits=7, decimal_places=2)

    class Meta:
        verbose_name = _('Счет')
        verbose_name_plural = _('Счета')

    def __str__(self):
        return '{name} {amount}'.format(
            name=self.name,
            amount=self.current_amount
        )


class Incomes(models.Model):
    name = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=7, decimal_places=2)
    account = models.ForeignKey(
        Accounts,
        null=True,
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Доход'
        verbose_name_plural = 'Доходы'

    def __str__(self):
        return '{}'.format(self.amount)


