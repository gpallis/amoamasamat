# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Subset.dumb_field'
        db.add_column('latingrammar_subset', 'dumb_field',
                      self.gf('django.db.models.fields.CharField')(default='nothing', max_length=100),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Subset.dumb_field'
        db.delete_column('latingrammar_subset', 'dumb_field')


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
        },
        'latingrammar.subset': {
            'Meta': {'object_name': 'Subset'},
            'conjugations': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['latingrammar.LatinConjugation']", 'symmetrical': 'False', 'blank': 'True'}),
            'declensions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['latingrammar.LatinDeclension']", 'symmetrical': 'False', 'blank': 'True'}),
            'dumb_field': ('django.db.models.fields.CharField', [], {'default': "'nothing'", 'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'tenses': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['latingrammar.LatinTense']", 'symmetrical': 'False', 'blank': 'True'})
        }
    }

    complete_apps = ['latingrammar']