# -*- coding: utf-8 -*-

from django.contrib import admin

# Register your models here.
from mybudget.envelopes.models import Envelopes

admin.site.register(Envelopes)