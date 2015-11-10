# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Account'
        db.create_table(u'budget_account', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('current_amount', self.gf('django.db.models.fields.DecimalField')(max_digits=7, decimal_places=2)),
        ))
        db.send_create_signal(u'budget', ['Account'])

        # Adding model 'RegularMonthlyExpenses'
        db.create_table(u'budget_regularmonthlyexpenses', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('amount', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=2)),
            ('account', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['budget.Account'], null=True)),
        ))
        db.send_create_signal(u'budget', ['RegularMonthlyExpenses'])

        # Adding model 'envelopes'
        db.create_table(u'budget_envelopes', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('current_amount', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=2)),
            ('monthly_replenishment', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=2)),
            ('cash', self.gf('django.db.models.fields.BooleanField')()),
            ('account', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['budget.Account'], null=True)),
        ))
        db.send_create_signal(u'budget', ['envelopes'])

        # Adding model 'Expenses'
        db.create_table(u'budget_expenses', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('amount', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=2)),
            ('envelope', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['budget.envelopes'])),
        ))
        db.send_create_signal(u'budget', ['Expenses'])

        # Adding model 'Incomes'
        db.create_table(u'budget_incomes', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('amount', self.gf('django.db.models.fields.DecimalField')(max_digits=7, decimal_places=2)),
            ('account', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['budget.Account'], null=True)),
        ))
        db.send_create_signal(u'budget', ['Incomes'])


    def backwards(self, orm):
        # Deleting model 'Account'
        db.delete_table(u'budget_account')

        # Deleting model 'RegularMonthlyExpenses'
        db.delete_table(u'budget_regularmonthlyexpenses')

        # Deleting model 'envelopes'
        db.delete_table(u'budget_envelopes')

        # Deleting model 'Expenses'
        db.delete_table(u'budget_expenses')

        # Deleting model 'Incomes'
        db.delete_table(u'budget_incomes')


    models = {
        u'budget.account': {
            'Meta': {'object_name': 'Account'},
            'current_amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '7', 'decimal_places': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'budget.envelopes': {
            'Meta': {'object_name': 'envelopes'},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['budget.Account']", 'null': 'True'}),
            'cash': ('django.db.models.fields.BooleanField', [], {}),
            'current_amount': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'monthly_replenishment': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'budget.expenses': {
            'Meta': {'object_name': 'Expenses'},
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'}),
            'envelope': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['budget.envelopes']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'budget.incomes': {
            'Meta': {'object_name': 'Incomes'},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['budget.Account']", 'null': 'True'}),
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '7', 'decimal_places': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'budget.regularmonthlyexpenses': {
            'Meta': {'object_name': 'RegularMonthlyExpenses'},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['budget.Account']", 'null': 'True'}),
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['budget']
