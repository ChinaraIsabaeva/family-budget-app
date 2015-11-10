# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL("INSERT into general_accounts (id, name, current_amount) select id, name, current_amount from budget_accounts; "),
        migrations.RunSQL("INSERT into general_incomes (id, name, amount, account_id) select id, name, amount, account_id from budget_incomes; "),
    ]
