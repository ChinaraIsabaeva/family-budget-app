# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Expenses.date'
        db.add_column(u'finplanner_expenses', 'date',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2013, 12, 9, 0, 0)),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Expenses.date'
        db.delete_column(u'finplanner_expenses', 'date')


    models = {
        u'finplanner.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        u'finplanner.expenses': {
            'Meta': {'object_name': 'Expenses'},
            'amount': ('django.db.models.fields.IntegerField', [], {}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'default': "'week_expenses'", 'to': u"orm['finplanner.Category']"}),
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['finplanner']