from django.contrib import admin
from mybudget.finplanner.models import *

# Register your models here.
admin.site.register(Category)
admin.site.register(Expenses)
admin.site.register(Reserves)
admin.site.register(Incomes)