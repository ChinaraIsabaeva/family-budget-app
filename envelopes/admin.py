# -*- coding: utf-8 -*-

from django.contrib import admin

from envelopes.models import Envelopes


class EnvelopesAdmin(admin.ModelAdmin):
    list_display = ('name', 'current_amount', 'monthly_replenishment')


admin.site.register(Envelopes, EnvelopesAdmin)