# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table(u'finplanner_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('periodicity', self.gf('django.db.models.fields.IntegerField')(default=4)),
        ))
        db.send_create_signal(u'main', ['Category'])

        # Adding model 'Expenses'
        db.create_table(u'finplanner_expenses', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Category'])),
            ('amount', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'main', ['Expenses'])


    def backwards(self, orm):
        # Deleting model 'Category'
        db.delete_table(u'finplanner_category')

        # Deleting model 'Expenses'
        db.delete_table(u'finplanner_expenses')


    models = {
        u'main.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'periodicity': ('django.db.models.fields.IntegerField', [], {'default': '4'})
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