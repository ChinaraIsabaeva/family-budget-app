# -*- coding: utf-8 -*-

from django.db import models, transaction

# Create your models here.
from mybudget.envelopes.models import Envelopes
from mybudget.general.models import Accounts


class RegularMonthlyExpenses(models.Model):
    name = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    account = models.ForeignKey(Accounts, null=True)

    class Meta:
        verbose_name = u'Постоянный месячный расход'
        verbose_name_plural = u'Постоянные месячные расходы'

    def __unicode__(self):
        return u'%s' % self.name


class Expenses(models.Model):
    name = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    envelope = models.ForeignKey(Envelopes)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = u'Расход'
        verbose_name_plural = u'Расходы'
        ordering = ['-created_date', 'name']

    def __unicode__(self):
        return u'%s' % self.name

    def save(self, *args, **kwargs):
        try:
            with transaction.atomic():
                envelope = Envelopes.objects.get(name=self.envelope)
                envelope.current_amount = envelope.current_amount - self.amount
                envelope.save()
                if envelope.cash is False:
                    account = Accounts.objects.get(id=envelope.account.id)
                    account.current_amount = account.current_amount - self.amount
                    account.save()
                super(Expenses, self).save(*args, **kwargs)
                print 'transaction goes!'
        except:
            'Something goes wrong!'

    def get_absolute_url(self):
        return '/%i/' % self.id