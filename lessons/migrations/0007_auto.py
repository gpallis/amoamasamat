# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding M2M table for field verb_unlocks on 'Level'
        db.create_table('lessons_level_verb_unlocks', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('level', models.ForeignKey(orm['lessons.level'], null=False)),
            ('englishverb', models.ForeignKey(orm['englishgrammar.englishverb'], null=False))
        ))
        db.create_unique('lessons_level_verb_unlocks', ['level_id', 'englishverb_id'])

        # Adding M2M table for field noun_unlocks on 'Level'
        db.create_table('lessons_level_noun_unlocks', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('level', models.ForeignKey(orm['lessons.level'], null=False)),
            ('englishnoun', models.ForeignKey(orm['englishgrammar.englishnoun'], null=False))
        ))
        db.create_unique('lessons_level_noun_unlocks', ['level_id', 'englishnoun_id'])


    def backwards(self, orm):
        # Removing M2M table for field verb_unlocks on 'Level'
        db.delete_table('lessons_level_verb_unlocks')

        # Removing M2M table for field noun_unlocks on 'Level'
        db.delete_table('lessons_level_noun_unlocks')


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
        'lessons.lesson': {
            'Meta': {'object_name': 'Lesson'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'lessons.level': {
            'Meta': {'object_name': 'Level'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level_number': ('django.db.models.fields.IntegerField', [], {}),
            'noun_unlocks': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['englishgrammar.EnglishNoun']", 'symmetrical': 'False'}),
            'number_of_questions': ('django.db.models.fields.IntegerField', [], {}),
            'question_generator': ('django.db.models.fields.CharField', [], {'default': "'threeWordSentence'", 'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'verb_unlocks': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['englishgrammar.EnglishVerb']", 'symmetrical': 'False'})
        },
        'sharedgrammar.nounproperty': {
            'Meta': {'object_name': 'NounProperty'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['lessons']