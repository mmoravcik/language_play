from django.contrib import admin
from apps.wordphrase import models


class PictureInline(admin.TabularInline):
    model = models.Picture
    extra = 1


class PronunciationInline(admin.TabularInline):
    model = models.Pronunciation
    extra = 1


class WordPhraseAdmin(admin.ModelAdmin):
    inlines = (PictureInline, PronunciationInline,)
    list_filter = ('language', 'type',)


admin.site.register(models.Language)
admin.site.register(models.WordPhrase, WordPhraseAdmin)
admin.site.register(models.Picture)