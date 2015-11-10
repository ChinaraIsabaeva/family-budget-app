# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import Incomes, Accounts

admin.site.register(Incomes)
admin.site.register(Accounts)