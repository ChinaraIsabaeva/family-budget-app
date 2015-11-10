# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL("INSERT into expenses_expenses (id, name, amount, envelope_id, created_date) (select id, name, amount, envelope_id, created_date from budget_expenses); "),
        migrations.RunSQL("INSERT into expenses_regularmonthlyexpenses (id, name, amount, account_id) (select id, name, amount, account_id from budget_regularmonthlyexpenses); ")
    ]
