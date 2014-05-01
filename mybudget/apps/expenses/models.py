from django.db import models
from mybudget.apps.main.models import Category, CATEGORY_TYPE_EXPENSES

# Create your models here.


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
