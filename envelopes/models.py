# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.
from core.models import Accounts


class Envelopes(models.Model):
    name = models.CharField(max_length=255)
    current_amount = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        default=0
    )
    monthly_replenishment = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )
    cash = models.BooleanField(default=False)
    closed = models.NullBooleanField(default=False)
    onetime_envelope = models.NullBooleanField(default=True)
    max_amount = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = "конверт"
        verbose_name_plural = 'Конверты'
        ordering = ['name', 'cash']

    def __str__(self):
        return '{}'.format(self.name)

    @property
    def get_absolute_url(self):
        return '/{}/'.format(self.name)
