# -*- coding: utf-8 -*-

from django.contrib import admin

# Register your models here.

from expenses.models import RegularMonthlyExpenses, Expenses


class RegularMonthlyExpensesAdmin(admin.ModelAdmin):
    list_display = ('name', 'amount')


admin.site.register(Expenses)
admin.site.register(RegularMonthlyExpenses, RegularMonthlyExpensesAdmin)
