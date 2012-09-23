# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding M2M table for field subject_requires on 'EnglishVerb'
        db.create_table('englishgrammar_englishverb_subject_requires', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('englishverb', models.ForeignKey(orm['englishgrammar.englishverb'], null=False)),
            ('nounproperty', models.ForeignKey(orm['sharedgrammar.nounproperty'], null=False))
        ))
        db.create_unique('englishgrammar_englishverb_subject_requires', ['englishverb_id', 'nounproperty_id'])

        # Adding M2M table for field subject_excludes on 'EnglishVerb'
        db.create_table('englishgrammar_englishverb_subject_excludes', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('englishverb', models.ForeignKey(orm['englishgrammar.englishverb'], null=False)),
            ('nounproperty', models.ForeignKey(orm['sharedgrammar.nounproperty'], null=False))
        ))
        db.create_unique('englishgrammar_englishverb_subject_excludes', ['englishverb_id', 'nounproperty_id'])

        # Adding M2M table for field object_requires on 'EnglishVerb'
        db.create_table('englishgrammar_englishverb_object_requires', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('englishverb', models.ForeignKey(orm['englishgrammar.englishverb'], null=False)),
            ('nounproperty', models.ForeignKey(orm['sharedgrammar.nounproperty'], null=False))
        ))
        db.create_unique('englishgrammar_englishverb_object_requires', ['englishverb_id', 'nounproperty_id'])

        # Adding M2M table for field object_excludes on 'EnglishVerb'
        db.create_table('englishgrammar_englishverb_object_excludes', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('englishverb', models.ForeignKey(orm['englishgrammar.englishverb'], null=False)),
            ('nounproperty', models.ForeignKey(orm['sharedgrammar.nounproperty'], null=False))
        ))
        db.create_unique('englishgrammar_englishverb_object_excludes', ['englishverb_id', 'nounproperty_id'])


    def backwards(self, orm):
        # Removing M2M table for field subject_requires on 'EnglishVerb'
        db.delete_table('englishgrammar_englishverb_subject_requires')

        # Removing M2M table for field subject_excludes on 'EnglishVerb'
        db.delete_table('englishgrammar_englishverb_subject_excludes')

        # Removing M2M table for field object_requires on 'EnglishVerb'
        db.delete_table('englishgrammar_englishverb_object_requires')

        # Removing M2M table for field object_excludes on 'EnglishVerb'
        db.delete_table('englishgrammar_englishverb_object_excludes')


    models = {
        'englishgrammar.englishconjugation': {
            'Meta': {'object_name': 'EnglishConjugation'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'englishgrammar.englishnoun': {
            'Meta': {'object_name': 'EnglishNoun'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'plural': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'properties': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['sharedgrammar.NounProperty']", 'symmetrical': 'False'}),
            'singular': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'translation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['latingrammar.LatinNoun']"})
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
            'object_excludes': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'object_excludes_set'", 'symmetrical': 'False', 'to': "orm['sharedgrammar.NounProperty']"}),
            'object_requires': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'object_requires_set'", 'symmetrical': 'False', 'to': "orm['sharedgrammar.NounProperty']"}),
            'pastparticiple': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'perfect': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'present': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'subject_excludes': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'subject_excludes_set'", 'symmetrical': 'False', 'to': "orm['sharedgrammar.NounProperty']"}),
            'subject_requires': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'subject_requires_set'", 'symmetrical': 'False', 'to': "orm['sharedgrammar.NounProperty']"}),
            'translation': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['latingrammar.LatinVerb']", 'unique': 'True'})
        },
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
        'sharedgrammar.nounproperty': {
            'Meta': {'object_name': 'NounProperty'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['englishgrammar']