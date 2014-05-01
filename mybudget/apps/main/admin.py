from django.contrib import admin
from mybudget.apps.main.models import *

# Register your models here.
admin.site.register(Category)
admin.site.register(Reserves)
admin.site.register(Incomes)