# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Subset'
        db.delete_table('englishgrammar_subset')

        # Removing M2M table for field conjugations on 'Subset'
        db.delete_table('englishgrammar_subset_conjugations')

        # Removing M2M table for field tenses on 'Subset'
        db.delete_table('englishgrammar_subset_tenses')


    def backwards(self, orm):
        # Adding model 'Subset'
        db.create_table('englishgrammar_subset', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('englishgrammar', ['Subset'])

        # Adding M2M table for field conjugations on 'Subset'
        db.create_table('englishgrammar_subset_conjugations', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('subset', models.ForeignKey(orm['englishgrammar.subset'], null=False)),
            ('englishconjugation', models.ForeignKey(orm['englishgrammar.englishconjugation'], null=False))
        ))
        db.create_unique('englishgrammar_subset_conjugations', ['subset_id', 'englishconjugation_id'])

        # Adding M2M table for field tenses on 'Subset'
        db.create_table('englishgrammar_subset_tenses', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('subset', models.ForeignKey(orm['englishgrammar.subset'], null=False)),
            ('englishtense', models.ForeignKey(orm['englishgrammar.englishtense'], null=False))
        ))
        db.create_unique('englishgrammar_subset_tenses', ['subset_id', 'englishtense_id'])


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
            'properties': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'noun_set'", 'blank': 'True', 'to': "orm['sharedgrammar.NounProperty']"}),
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
            'object_excludes': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'object_excludes_set'", 'blank': 'True', 'to': "orm['sharedgrammar.NounProperty']"}),
            'object_requires': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'object_requires_set'", 'blank': 'True', 'to': "orm['sharedgrammar.NounProperty']"}),
            'pastparticiple': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'perfect': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'present': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'subject_excludes': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'subject_excludes_set'", 'blank': 'True', 'to': "orm['sharedgrammar.NounProperty']"}),
            'subject_requires': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'subject_requires_set'", 'blank': 'True', 'to': "orm['sharedgrammar.NounProperty']"}),
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