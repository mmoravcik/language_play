# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'WordPhrase'
        db.create_table(u'wordphrase_wordphrase', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('sounds', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('type', self.gf('django.db.models.fields.SmallIntegerField')(max_length=1)),
        ))
        db.send_create_signal(u'wordphrase', ['WordPhrase'])


    def backwards(self, orm):
        # Deleting model 'WordPhrase'
        db.delete_table(u'wordphrase_wordphrase')


    models = {
        u'wordphrase.wordphrase': {
            'Meta': {'object_name': 'WordPhrase'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sounds': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'type': ('django.db.models.fields.SmallIntegerField', [], {'max_length': '1'})
        }
    }

    complete_apps = ['wordphrase']