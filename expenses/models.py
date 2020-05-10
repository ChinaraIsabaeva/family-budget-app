# -*- coding: utf-8 -*-

from django.db import models, transaction

# Create your models here.
from envelopes.models import Envelopes


class RegularMonthlyExpenses(models.Model):
    name = models.CharField(max_length=255)
    amount = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )

    class Meta:
        verbose_name = 'Постоянный месячный расход'
        verbose_name_plural = 'Постоянные месячные расходы'
        ordering = ['name']

    def __str__(self):
        return '{name}'.format(name=self.name)


class Expenses(models.Model):
    name = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    envelope = models.ForeignKey(
        Envelopes,
        on_delete=models.CASCADE
    )
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Расход'
        verbose_name_plural = 'Расходы'
        ordering = ['-created_date', 'name']

    def __str__(self):
        return '{name}'.format(name=self.name)

    def save(self, *args, **kwargs):
        try:
            with transaction.atomic():
                envelope = Envelopes.objects.get(name=self.envelope)
                envelope.current_amount = envelope.current_amount - self.amount
                envelope.save()
                super(Expenses, self).save(*args, **kwargs)
                print('transaction goes!')
        except Exception as e:
            print(e)

    def get_absolute_url(self):
        return '/{id}/'.format(id=self.id)
