# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Subset'
        db.create_table('latingrammar_subset', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('latingrammar', ['Subset'])

        # Adding M2M table for field conjugations on 'Subset'
        db.create_table('latingrammar_subset_conjugations', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('subset', models.ForeignKey(orm['latingrammar.subset'], null=False)),
            ('latinconjugation', models.ForeignKey(orm['latingrammar.latinconjugation'], null=False))
        ))
        db.create_unique('latingrammar_subset_conjugations', ['subset_id', 'latinconjugation_id'])

        # Adding M2M table for field tenses on 'Subset'
        db.create_table('latingrammar_subset_tenses', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('subset', models.ForeignKey(orm['latingrammar.subset'], null=False)),
            ('latintense', models.ForeignKey(orm['latingrammar.latintense'], null=False))
        ))
        db.create_unique('latingrammar_subset_tenses', ['subset_id', 'latintense_id'])

        # Adding M2M table for field declensions on 'Subset'
        db.create_table('latingrammar_subset_declensions', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('subset', models.ForeignKey(orm['latingrammar.subset'], null=False)),
            ('latindeclension', models.ForeignKey(orm['latingrammar.latindeclension'], null=False))
        ))
        db.create_unique('latingrammar_subset_declensions', ['subset_id', 'latindeclension_id'])


    def backwards(self, orm):
        # Deleting model 'Subset'
        db.delete_table('latingrammar_subset')

        # Removing M2M table for field conjugations on 'Subset'
        db.delete_table('latingrammar_subset_conjugations')

        # Removing M2M table for field tenses on 'Subset'
        db.delete_table('latingrammar_subset_tenses')

        # Removing M2M table for field declensions on 'Subset'
        db.delete_table('latingrammar_subset_declensions')


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
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tenses': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['latingrammar.LatinTense']", 'symmetrical': 'False', 'blank': 'True'})
        }
    }

    complete_apps = ['latingrammar']