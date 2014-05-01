# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Category.periodicity'
        db.delete_column(u'finplanner_category', 'periodicity')


    def backwards(self, orm):
        # Adding field 'Category.periodicity'
        db.add_column(u'finplanner_category', 'periodicity',
                      self.gf('django.db.models.fields.IntegerField')(default=4),
                      keep_default=False)


    models = {
        u'main.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        u'main.expenses': {
            'Meta': {'object_name': 'Expenses'},
            'amount': ('django.db.models.fields.IntegerField', [], {}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.Category']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['main']