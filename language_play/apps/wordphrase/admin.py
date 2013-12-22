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

    def save_model(self, request, obj, form, change):
        obj.save()
        if obj.picture_set.all():
            for pic in obj.picture_set.all():
                for translation in obj.translations.all():
                    models.Picture.objects.filter(wordphrase=translation).delete()
                    translation.picture_set.add(pic)




admin.site.register(models.Language)
admin.site.register(models.WordPhrase, WordPhraseAdmin)
admin.site.register(models.Picture)