# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import RegularMonthlyExpenses, Incomes, Accounts, Envelopes, Expenses

# Register your models here.
admin.site.register(RegularMonthlyExpenses)
admin.site.register(Incomes)
admin.site.register(Accounts)
admin.site.register(Envelopes)
admin.site.register(Expenses)