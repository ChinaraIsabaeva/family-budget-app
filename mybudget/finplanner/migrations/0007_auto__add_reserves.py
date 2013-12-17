# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Reserves'
        db.create_table(u'finplanner_reserves', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('periodicity', self.gf('django.db.models.fields.IntegerField')(default=4)),
            ('amount', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'finplanner', ['Reserves'])


    def backwards(self, orm):
        # Deleting model 'Reserves'
        db.delete_table(u'finplanner_reserves')


    models = {
        u'finplanner.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        u'finplanner.expenses': {
            'Meta': {'object_name': 'Expenses'},
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '19', 'decimal_places': '2'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'default': '5', 'to': u"orm['finplanner.Category']"}),
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'finplanner.reserves': {
            'Meta': {'object_name': 'Reserves'},
            'amount': ('django.db.models.fields.FloatField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'periodicity': ('django.db.models.fields.IntegerField', [], {'default': '4'})
        }
    }

    complete_apps = ['finplanner']