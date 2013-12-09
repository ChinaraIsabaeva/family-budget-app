from django.db import models

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


class Category(models.Model):
    name = models.CharField(max_length=150)


    def __unicode__(self):
        return self.name

    class Meta():
        verbose_name = u'Category'
        verbose_name_plural = u'Categories'


class Expenses(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category)
    amount = models.IntegerField()



