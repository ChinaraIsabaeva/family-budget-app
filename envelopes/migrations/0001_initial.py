# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Envelopes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('current_amount', models.DecimalField(default=0, max_digits=8, decimal_places=2)),
                ('monthly_replenishment', models.DecimalField(max_digits=8, decimal_places=2)),
                ('cash', models.BooleanField(default=False)),
                ('closed', models.NullBooleanField()),
                ('onetime_envelope', models.NullBooleanField()),
                ('max_amount', models.DecimalField(null=True, max_digits=8, decimal_places=2, blank=True)),
                ('account', models.ForeignKey(to='core.Accounts', null=True, on_delete=models.deletion.CASCADE)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': '\u043a\u043e\u043d\u0432\u0435\u0440\u0442',
                'verbose_name_plural': '\u041a\u043e\u043d\u0432\u0435\u0440\u0442\u044b',
            },
            bases=(models.Model,),
        ),
    ]
