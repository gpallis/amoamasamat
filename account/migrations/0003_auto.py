# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing M2M table for field knownVerbs on 'UserProfile'
        db.delete_table('account_userprofile_knownVerbs')

        # Adding M2M table for field known_verbs on 'UserProfile'
        db.create_table('account_userprofile_known_verbs', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('userprofile', models.ForeignKey(orm['account.userprofile'], null=False)),
            ('englishverb', models.ForeignKey(orm['englishgrammar.englishverb'], null=False))
        ))
        db.create_unique('account_userprofile_known_verbs', ['userprofile_id', 'englishverb_id'])


    def backwards(self, orm):
        # Adding M2M table for field knownVerbs on 'UserProfile'
        db.create_table('account_userprofile_knownVerbs', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('userprofile', models.ForeignKey(orm['account.userprofile'], null=False)),
            ('englishverb', models.ForeignKey(orm['englishgrammar.englishverb'], null=False))
        ))
        db.create_unique('account_userprofile_knownVerbs', ['userprofile_id', 'englishverb_id'])

        # Removing M2M table for field known_verbs on 'UserProfile'
        db.delete_table('account_userprofile_known_verbs')


    models = {
        'account.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'known_verbs': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['englishgrammar.EnglishVerb']", 'symmetrical': 'False'}),
            'level': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'}),
            'xp': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'englishgrammar.englishconjugation': {
            'Meta': {'object_name': 'EnglishConjugation'},
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

    complete_apps = ['account']