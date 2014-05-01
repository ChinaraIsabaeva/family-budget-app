# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Expenses'
        db.create_table(u'expenses_expenses', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(default=3, to=orm['main.Category'])),
            ('amount', self.gf('django.db.models.fields.FloatField')()),
            ('date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'expenses', ['Expenses'])


    def backwards(self, orm):
        # Deleting model 'Expenses'
        db.delete_table(u'expenses_expenses')


    models = {
        u'expenses.expenses': {
            'Meta': {'ordering': "['date']", 'object_name': 'Expenses'},
            'amount': ('django.db.models.fields.FloatField', [], {}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'default': '3', 'to': u"orm['main.Category']"}),
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'main.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'type': ('django.db.models.fields.IntegerField', [], {'default': '9'})
        }
    }

    complete_apps = ['expenses']