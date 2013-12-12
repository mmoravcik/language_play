from django.contrib import admin
from django.db.models import get_model

WordPhrase = get_model('wordphrase', 'WordPhrase')


admin.site.register(WordPhrase)