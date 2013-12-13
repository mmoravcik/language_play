# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding M2M table for field translations on 'WordPhrase'
        m2m_table_name = db.shorten_name(u'wordphrase_wordphrase_translations')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_wordphrase', models.ForeignKey(orm[u'wordphrase.wordphrase'], null=False)),
            ('to_wordphrase', models.ForeignKey(orm[u'wordphrase.wordphrase'], null=False))
        ))
        db.create_unique(m2m_table_name, ['from_wordphrase_id', 'to_wordphrase_id'])

        # Adding field 'Picture.wordphrase'
        db.add_column(u'wordphrase_picture', 'wordphrase',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['wordphrase.WordPhrase'], null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Removing M2M table for field translations on 'WordPhrase'
        db.delete_table(db.shorten_name(u'wordphrase_wordphrase_translations'))

        # Deleting field 'Picture.wordphrase'
        db.delete_column(u'wordphrase_picture', 'wordphrase_id')


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
            'text': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'translations': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'translations_rel_+'", 'null': 'True', 'to': u"orm['wordphrase.WordPhrase']"}),
            'type': ('django.db.models.fields.SmallIntegerField', [], {'max_length': '1'})
        }
    }

    complete_apps = ['wordphrase']