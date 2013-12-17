# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Reserves.category'
        db.add_column(u'finplanner_reserves', 'category',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=5, to=orm['finplanner.Category']),
                      keep_default=False)

        # Adding field 'Reserves.date'
        db.add_column(u'finplanner_reserves', 'date',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2013, 12, 16, 0, 0)),
                      keep_default=False)

        # Adding field 'Category.type'
        db.add_column(u'finplanner_category', 'type',
                      self.gf('django.db.models.fields.IntegerField')(default=9),
                      keep_default=False)

        # Adding field 'Incomes.category'
        db.add_column(u'finplanner_incomes', 'category',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=5, to=orm['finplanner.Category']),
                      keep_default=False)

        # Adding field 'Incomes.date'
        db.add_column(u'finplanner_incomes', 'date',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2013, 12, 16, 0, 0)),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Reserves.category'
        db.delete_column(u'finplanner_reserves', 'category_id')

        # Deleting field 'Reserves.date'
        db.delete_column(u'finplanner_reserves', 'date')

        # Deleting field 'Category.type'
        db.delete_column(u'finplanner_category', 'type')

        # Deleting field 'Incomes.category'
        db.delete_column(u'finplanner_incomes', 'category_id')

        # Deleting field 'Incomes.date'
        db.delete_column(u'finplanner_incomes', 'date')


    models = {
        u'finplanner.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'type': ('django.db.models.fields.IntegerField', [], {'default': '9'})
        },
        u'finplanner.expenses': {
            'Meta': {'object_name': 'Expenses'},
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '19', 'decimal_places': '2'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'default': '5', 'to': u"orm['finplanner.Category']"}),
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'finplanner.incomes': {
            'Meta': {'object_name': 'Incomes'},
            'amount': ('django.db.models.fields.FloatField', [], {}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'default': '5', 'to': u"orm['finplanner.Category']"}),
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'periodicity': ('django.db.models.fields.IntegerField', [], {'default': '4'})
        },
        u'finplanner.reserves': {
            'Meta': {'object_name': 'Reserves'},
            'amount': ('django.db.models.fields.FloatField', [], {}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'default': '5', 'to': u"orm['finplanner.Category']"}),
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'periodicity': ('django.db.models.fields.IntegerField', [], {'default': '4'})
        }
    }

    complete_apps = ['finplanner']