from django.db import models
from datetime import datetime

# Create your models here.
PERIODICITY_YEAR = 1
PERIODICITY_HALF_YEAR = 2
PERIODICITY_QUARTER = 3
PERIODICITY_MONTH = 4
PERIODICITY_TWO_WEEK = 5
PERIODICITY_WEEK = 6
PERIODICITY_DAY = 7
PERIODICITY_CHOICES = (
    (PERIODICITY_YEAR, u'Yearly'),
    (PERIODICITY_HALF_YEAR, u'Half yearly'),
    (PERIODICITY_QUARTER, u'Quarterly'),
    (PERIODICITY_MONTH, u'Monthly'),
    (PERIODICITY_TWO_WEEK, u'Fortnightly'),
    (PERIODICITY_WEEK, u'Weekly'),
    (PERIODICITY_DAY, u'Daily'),
)


CATEGORY_TYPE_INCOMES = 8
CATEGORY_TYPE_EXPENSES = 9
CATEGORY_TYPE_RESERVES = 10
CATEGORY_TYPE_CHOICES = (
    (CATEGORY_TYPE_INCOMES, u'Incomes'),
    (CATEGORY_TYPE_EXPENSES, u'Expenses'),
    (CATEGORY_TYPE_RESERVES, u'Reserves')
)

class Category(models.Model):
    name = models.CharField(max_length=150)
    type = models.IntegerField(choices=CATEGORY_TYPE_CHOICES, default=CATEGORY_TYPE_EXPENSES)


    def __unicode__(self):
        return self.name

    class Meta():
        verbose_name = u'category'
        verbose_name_plural = u'categories'


class Expenses(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, limit_choices_to={'type': CATEGORY_TYPE_EXPENSES}, default=3)
    amount = models.FloatField()
    date = models.DateField()

    def __unicode__(self):
        return u'%s %s %s' % (self.name, self.amount, self.date)

    class Meta():
        verbose_name = u'expense'
        verbose_name_plural = u'expenses'
        ordering = ['date']


class Reserves(models.Model):
    name = models.CharField(max_length=255)
    periodicity = models.IntegerField(choices=PERIODICITY_CHOICES, default=PERIODICITY_MONTH)
    category = models.ForeignKey(Category, limit_choices_to={'type': CATEGORY_TYPE_RESERVES}, default=10)
    amount = models.FloatField()
    date = models.DateField()

    def __unicode__(self):
        return self.name

    class Meta():
        verbose_name_plural = u'reserves'
        ordering = ['date']


class Incomes(models.Model):
    name = models.CharField(max_length=255)
    periodicity = models.IntegerField(choices=PERIODICITY_CHOICES, default=PERIODICITY_MONTH)
    category = models.ForeignKey(Category, limit_choices_to={'type': CATEGORY_TYPE_INCOMES}, default=9)
    amount = models.FloatField()
    date = models.DateField()

    def __unicode__(self):
        return self.name

    class Meta():
        verbose_name_plural = u'incomes'
        ordering = ['date']