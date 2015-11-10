# -*- coding: utf-8 -*-

from django.contrib import admin

# Register your models here.

from .models import RegularMonthlyExpenses, Expenses

admin.site.register(Expenses)
admin.site.register(RegularMonthlyExpenses)
