# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('envelopes', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expenses',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('amount', models.DecimalField(max_digits=8, decimal_places=2)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('envelope', models.ForeignKey(to='envelopes.Envelopes', on_delete=models.deletion.CASCADE)),
            ],
            options={
                'verbose_name': '\u0420\u0430\u0441\u0445\u043e\u0434',
                'verbose_name_plural': '\u0420\u0430\u0441\u0445\u043e\u0434\u044b',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RegularMonthlyExpenses',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('amount', models.DecimalField(max_digits=8, decimal_places=2)),
                ('account', models.ForeignKey(to='core.Accounts', null=True, on_delete=models.deletion.CASCADE)),
            ],
            options={
                'verbose_name': '\u041f\u043e\u0441\u0442\u043e\u044f\u043d\u043d\u044b\u0439 \u043c\u0435\u0441\u044f\u0447\u043d\u044b\u0439 \u0440\u0430\u0441\u0445\u043e\u0434',
                'verbose_name_plural': '\u041f\u043e\u0441\u0442\u043e\u044f\u043d\u043d\u044b\u0435 \u043c\u0435\u0441\u044f\u0447\u043d\u044b\u0435 \u0440\u0430\u0441\u0445\u043e\u0434\u044b',
            },
            bases=(models.Model,),
        ),
    ]
