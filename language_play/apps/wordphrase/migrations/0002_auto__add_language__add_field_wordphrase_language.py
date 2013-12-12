# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Language'
        db.create_table(u'wordphrase_language', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'wordphrase', ['Language'])

        # Adding field 'WordPhrase.language'
        db.add_column(u'wordphrase_wordphrase', 'language',
                      self.gf('django.db.models.fields.related.ForeignKey')(default='', to=orm['wordphrase.Language']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Language'
        db.delete_table(u'wordphrase_language')

        # Deleting field 'WordPhrase.language'
        db.delete_column(u'wordphrase_wordphrase', 'language_id')


    models = {
        u'wordphrase.language': {
            'Meta': {'object_name': 'Language'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'wordphrase.wordphrase': {
            'Meta': {'object_name': 'WordPhrase'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['wordphrase.Language']"}),
            'sounds': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'type': ('django.db.models.fields.SmallIntegerField', [], {'max_length': '1'})
        }
    }

    complete_apps = ['wordphrase']