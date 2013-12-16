# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding unique constraint on 'WordPhrase', fields ['text']
        db.create_unique(u'wordphrase_wordphrase', ['text'])


    def backwards(self, orm):
        # Removing unique constraint on 'WordPhrase', fields ['text']
        db.delete_unique(u'wordphrase_wordphrase', ['text'])


    models = {
        u'wordphrase.language': {
            'Meta': {'object_name': 'Language'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'wordphrase.picture': {
            'Meta': {'object_name': 'Picture'},
            'file': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'wordphrase': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['wordphrase.WordPhrase']", 'null': 'True', 'blank': 'True'})
        },
        u'wordphrase.wordphrase': {
            'Meta': {'object_name': 'WordPhrase'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['wordphrase.Language']"}),
            'sounds': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'translations': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'translations_rel_+'", 'null': 'True', 'to': u"orm['wordphrase.WordPhrase']"}),
            'type': ('django.db.models.fields.SmallIntegerField', [], {'default': '1', 'max_length': '1'})
        }
    }

    complete_apps = ['wordphrase']