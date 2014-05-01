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
        db.alter_column(u'finplanner_expenses', 'amount', self.gf('django.db.models.fields.DecimalField')(max_digits=19, decimal_places=2))


    models = {
        u'main.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'type': ('django.db.models.fields.IntegerField', [], {'default': '9'})
        },
        u'main.expenses': {
            'Meta': {'object_name': 'Expenses'},
            'amount': ('django.db.models.fields.FloatField', [], {}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'default': '5', 'to': u"orm['main.Category']"}),
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'main.incomes': {
            'Meta': {'object_name': 'Incomes'},
            'amount': ('django.db.models.fields.FloatField', [], {}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'default': '9', 'to': u"orm['main.Category']"}),
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'periodicity': ('django.db.models.fields.IntegerField', [], {'default': '4'})
        },
        u'main.reserves': {
            'Meta': {'object_name': 'Reserves'},
            'amount': ('django.db.models.fields.FloatField', [], {}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'default': '10', 'to': u"orm['main.Category']"}),
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'periodicity': ('django.db.models.fields.IntegerField', [], {'default': '4'})
        }
    }

    complete_apps = ['main']