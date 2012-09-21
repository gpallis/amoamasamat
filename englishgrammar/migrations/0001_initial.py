# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'EnglishConjugation'
        db.create_table('englishgrammar_englishconjugation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('englishgrammar', ['EnglishConjugation'])

        # Adding model 'EnglishVerb'
        db.create_table('englishgrammar_englishverb', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('translation', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['latingrammar.LatinVerb'], unique=True)),
            ('present', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('infinitive', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('perfect', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('pastparticiple', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('conjugation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['englishgrammar.EnglishConjugation'])),
        ))
        db.send_create_signal('englishgrammar', ['EnglishVerb'])

        # Adding model 'EnglishTense'
        db.create_table('englishgrammar_englishtense', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('englishgrammar', ['EnglishTense'])

        # Adding model 'EnglishTable'
        db.create_table('englishgrammar_englishtable', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('conjugation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['englishgrammar.EnglishConjugation'])),
            ('tense', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['englishgrammar.EnglishTense'])),
            ('person1', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('person2', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('person3', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('person4', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('person5', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('person6', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('englishgrammar', ['EnglishTable'])


    def backwards(self, orm):
        # Deleting model 'EnglishConjugation'
        db.delete_table('englishgrammar_englishconjugation')

        # Deleting model 'EnglishVerb'
        db.delete_table('englishgrammar_englishverb')

        # Deleting model 'EnglishTense'
        db.delete_table('englishgrammar_englishtense')

        # Deleting model 'EnglishTable'
        db.delete_table('englishgrammar_englishtable')


    models = {
        'englishgrammar.englishconjugation': {
            'Meta': {'object_name': 'EnglishConjugation'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'englishgrammar.englishtable': {
            'Meta': {'object_name': 'EnglishTable'},
            'conjugation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['englishgrammar.EnglishConjugation']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'person1': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'person2': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'person3': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'person4': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'person5': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'person6': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'tense': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['englishgrammar.EnglishTense']"})
        },
        'englishgrammar.englishtense': {
            'Meta': {'object_name': 'EnglishTense'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'englishgrammar.englishverb': {
            'Meta': {'object_name': 'EnglishVerb'},
            'conjugation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['englishgrammar.EnglishConjugation']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'infinitive': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'pastparticiple': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'perfect': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'present': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'translation': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['latingrammar.LatinVerb']", 'unique': 'True'})
        },
        'latingrammar.latinconjugation': {
            'Meta': {'object_name': 'LatinConjugation'},
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

    complete_apps = ['englishgrammar']