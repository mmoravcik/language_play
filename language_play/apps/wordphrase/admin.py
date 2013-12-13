from django.contrib import admin
from django.db.models import get_model

WordPhrase = get_model('wordphrase', 'WordPhrase')
Language = get_model('wordphrase', 'Language')
Picture = get_model('wordphrase', 'Picture')


class PictureInline(admin.TabularInline):
    model = Picture
    extra = 1


class WordPhraseAdmin(admin.ModelAdmin):
    inlines = (PictureInline, )


admin.site.register(Language)
admin.site.register(WordPhrase, WordPhraseAdmin)
admin.site.register(Picture)
