# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accounts',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('current_amount', models.DecimalField(max_digits=7, decimal_places=2)),
            ],
            options={
                'verbose_name': 'Account',
                'verbose_name_plural': 'Accounts',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Incomes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('amount', models.DecimalField(max_digits=7, decimal_places=2)),
                ('account', models.ForeignKey(to='core.Accounts', null=True, on_delete=models.deletion.CASCADE)),
            ],
            options={
                'verbose_name': '\u0414\u043e\u0445\u043e\u0434',
                'verbose_name_plural': '\u0414\u043e\u0445\u043e\u0434\u044b',
            },
            bases=(models.Model,),
        ),
    ]
