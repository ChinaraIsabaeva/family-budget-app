# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Envelopes.account'
        db.alter_column(u'budget_envelopes', 'account_id', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['general.Accounts']))

    def backwards(self, orm):

        # Changing field 'Envelopes.account'
        db.alter_column(u'budget_envelopes', 'account_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['general.Accounts'], null=True))

    models = {
        u'general.accounts': {
            'Meta': {'object_name': 'Accounts'},
            'current_amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '7', 'decimal_places': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'general.envelopes': {
            'Meta': {'ordering': "['name']", 'object_name': 'Envelopes'},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['general.Accounts']"}),
            'cash': ('django.db.models.fields.BooleanField', [], {}),
            'current_amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'monthly_replenishment': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
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