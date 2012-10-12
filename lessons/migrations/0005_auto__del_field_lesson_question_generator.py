# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Lesson.question_generator'
        db.delete_column('lessons_lesson', 'question_generator')


    def backwards(self, orm):
        # Adding field 'Lesson.question_generator'
        db.add_column('lessons_lesson', 'question_generator',
                      self.gf('django.db.models.fields.CharField')(default='threeWordSentence', max_length=100),
                      keep_default=False)


    models = {
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
            'number_of_questions': ('django.db.models.fields.IntegerField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['lessons']