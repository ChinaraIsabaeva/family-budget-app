# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-08-28 18:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('envelopes', '0003_auto_20170618_1325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='envelopes',
            name='closed',
            field=models.NullBooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='envelopes',
            name='onetime_envelope',
            field=models.NullBooleanField(default=True),
        ),
    ]