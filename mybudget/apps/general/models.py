# -*- coding: utf-8 -*-

from django.utils.translation import ugettext_lazy as _
from django.db import models


class Accounts(models.Model):
    name = models.CharField(max_length=255)
    current_amount = models.DecimalField(max_digits=7, decimal_places=2)

    class Meta:
        verbose_name = _(u'Счет')
        verbose_name_plural = _(u'Счета')

    def __unicode__(self):
        return u'%(name)s %(amount)s' % {'name': self.name, 'amount': self.current_amount}


class Incomes(models.Model):
    name = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=7, decimal_places=2)
    account = models.ForeignKey(Accounts, null=True)

    class Meta:
        verbose_name = u'Доход'
        verbose_name_plural = u'Доходы'

    def __unicode__(self):
        return u'%s' % self.amount


