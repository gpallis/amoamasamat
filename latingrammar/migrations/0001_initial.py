# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'LatinConjugation'
        db.create_table('latingrammar_latinconjugation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('latingrammar', ['LatinConjugation'])

        # Adding model 'LatinVerb'
        db.create_table('latingrammar_latinverb', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('present', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('infinitive', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('perfect', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('pastparticiple', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('conjugation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['latingrammar.LatinConjugation'])),
        ))
        db.send_create_signal('latingrammar', ['LatinVerb'])

        # Adding model 'LatinTense'
        db.create_table('latingrammar_latintense', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('latingrammar', ['LatinTense'])

        # Adding model 'LatinTable'
        db.create_table('latingrammar_latintable', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('conjugation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['latingrammar.LatinConjugation'])),
            ('tense', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['latingrammar.LatinTense'])),
            ('person1', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('person2', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('person3', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('person4', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('person5', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('person6', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('latingrammar', ['LatinTable'])


    def backwards(self, orm):
        # Deleting model 'LatinConjugation'
        db.delete_table('latingrammar_latinconjugation')

        # Deleting model 'LatinVerb'
        db.delete_table('latingrammar_latinverb')

        # Deleting model 'LatinTense'
        db.delete_table('latingrammar_latintense')

        # Deleting model 'LatinTable'
        db.delete_table('latingrammar_latintable')


    models = {
        'latingrammar.latinconjugation': {
            'Meta': {'object_name': 'LatinConjugation'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'latingrammar.latintable': {
            'Meta': {'object_name': 'LatinTable'},
            'conjugation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['latingrammar.LatinConjugation']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'person1': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'person2': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'person3': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'person4': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'person5': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'person6': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'tense': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['latingrammar.LatinTense']"})
        },
        'latingrammar.latintense': {
            'Meta': {'object_name': 'LatinTense'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'latingrammar.latinverb': {
            'Meta': {'object_name': 'LatinVerb'},
            'conjugation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['latingrammar.LatinConjugation']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'infinitive': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'pastparticiple': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'perfect': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'present': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['latingrammar']