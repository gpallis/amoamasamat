# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'LatinNoun'
        db.create_table('latingrammar_latinnoun', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nominativeSingular', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('genitiveSingular', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('declension', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['latingrammar.LatinDeclension'])),
        ))
        db.send_create_signal('latingrammar', ['LatinNoun'])

        # Adding model 'LatinNounTable'
        db.create_table('latingrammar_latinnountable', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('declension', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['latingrammar.LatinDeclension'])),
            ('nominativeSingular', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('vocativeSingular', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('accusativeSingular', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('genitiveSingular', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('dativeSingular', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('ablativeSingular', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('nominativePlural', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('vocativePlural', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('accusativePlural', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('genitivePlural', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('dativePlural', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('ablativePlural', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('latingrammar', ['LatinNounTable'])

        # Adding model 'LatinDeclension'
        db.create_table('latingrammar_latindeclension', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('latingrammar', ['LatinDeclension'])


    def backwards(self, orm):
        # Deleting model 'LatinNoun'
        db.delete_table('latingrammar_latinnoun')

        # Deleting model 'LatinNounTable'
        db.delete_table('latingrammar_latinnountable')

        # Deleting model 'LatinDeclension'
        db.delete_table('latingrammar_latindeclension')


    models = {
        'latingrammar.latinconjugation': {
            'Meta': {'object_name': 'LatinConjugation'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'latingrammar.latindeclension': {
            'Meta': {'object_name': 'LatinDeclension'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'latingrammar.latinnoun': {
            'Meta': {'object_name': 'LatinNoun'},
            'declension': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['latingrammar.LatinDeclension']"}),
            'genitiveSingular': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nominativeSingular': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'latingrammar.latinnountable': {
            'Meta': {'object_name': 'LatinNounTable'},
            'ablativePlural': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ablativeSingular': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'accusativePlural': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'accusativeSingular': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'dativePlural': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'dativeSingular': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'declension': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['latingrammar.LatinDeclension']"}),
            'genitivePlural': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'genitiveSingular': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nominativePlural': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'nominativeSingular': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'vocativePlural': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'vocativeSingular': ('django.db.models.fields.CharField', [], {'max_length': '100'})
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
            'present': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'transitive': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        }
    }

    complete_apps = ['latingrammar']