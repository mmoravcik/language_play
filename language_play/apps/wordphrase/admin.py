from django.contrib import admin
from django.db.models import get_model

WordPhrase = get_model('wordphrase', 'WordPhrase')
Language = get_model('wordphrase', 'Language')
Picture = get_model('wordphrase', 'Picture')


admin.site.register(Language)
admin.site.register(WordPhrase)
admin.site.register(Picture)