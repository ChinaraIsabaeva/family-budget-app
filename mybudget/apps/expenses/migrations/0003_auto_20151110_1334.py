# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0002_auto_20151110_1325'),
    ]

    operations = [
        migrations.RunSQL("DROP TABLE budget_accounts CASCADE; "),
        migrations.RunSQL("DROP TABLE budget_envelopes CASCADE; "),
        migrations.RunSQL("DROP TABLE budget_expenses CASCADE; "),
        migrations.RunSQL("DROP TABLE budget_incomes CASCADE; "),
        migrations.RunSQL("DROP TABLE budget_regularmonthlyexpenses CASCADE; "),
    ]
