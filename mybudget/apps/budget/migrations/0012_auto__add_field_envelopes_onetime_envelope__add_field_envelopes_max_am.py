# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Envelopes.onetime_envelope'
        db.add_column(u'budget_envelopes', 'onetime_envelope',
                      self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Envelopes.max_amount'
        db.add_column(u'budget_envelopes', 'max_amount',
                      self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=2, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Envelopes.onetime_envelope'
        db.delete_column(u'budget_envelopes', 'onetime_envelope')

        # Deleting field 'Envelopes.max_amount'
        db.delete_column(u'budget_envelopes', 'max_amount')


    models = {
        u'general.accounts': {
            'Meta': {'object_name': 'Accounts'},
            'current_amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '7', 'decimal_places': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'general.envelopes': {
            'Meta': {'ordering': "['name']", 'object_name': 'Envelopes'},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['general.Accounts']", 'null': 'True'}),
            'cash': ('django.db.models.fields.BooleanField', [], {}),
            'closed': ('django.db.models.fields.BooleanField', [], {}),
            'current_amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_amount': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'monthly_replenishment': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'onetime_envelope': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'})
        },
        u'general.expenses': {
            'Meta': {'object_name': 'Expenses'},
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'envelope': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['general.Envelopes']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'general.incomes': {
            'Meta': {'object_name': 'Incomes'},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['general.Accounts']", 'null': 'True'}),
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '7', 'decimal_places': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'general.regularmonthlyexpenses': {
            'Meta': {'object_name': 'RegularMonthlyExpenses'},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['general.Accounts']", 'null': 'True'}),
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['general']