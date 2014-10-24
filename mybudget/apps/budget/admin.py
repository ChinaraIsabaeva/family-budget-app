from django.contrib import admin

from .models import RegularMonthlyExpenses, Incomes, Accounts

# Register your models here.
admin.site.register(RegularMonthlyExpenses)
admin.site.register(Incomes)
admin.site.register(Accounts)