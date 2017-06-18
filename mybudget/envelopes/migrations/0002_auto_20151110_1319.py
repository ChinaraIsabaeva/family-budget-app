# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('envelopes', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL("INSERT into envelopes_envelopes (id, name, current_amount, monthly_replenishment, cash, account_id, closed, onetime_envelope, max_amount) select id, name, current_amount, monthly_replenishment, cash, account_id, closed, onetime_envelope, max_amount from budget_envelopes; "),
    ]
