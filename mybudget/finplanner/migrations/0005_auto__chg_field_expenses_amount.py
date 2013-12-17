# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Expenses.amount'
        db.alter_column(u'finplanner_expenses', 'amount', self.gf('django.db.models.fields.FloatField')())

    def backwards(self, orm):

        # Changing field 'Expenses.amount'
        db.alter_column(u'finplanner_expenses', 'amount', self.gf('django.db.models.fields.IntegerField')())

    models = {
        u'finplanner.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        u'finplanner.expenses': {
            'Meta': {'object_name': 'Expenses'},
            'amount': ('django.db.models.fields.FloatField', [], {}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'default': '5', 'to': u"orm['finplanner.Category']"}),
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['finplanner']