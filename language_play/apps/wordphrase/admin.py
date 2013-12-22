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

    def save_related(self, request, form, formsets, change):
        super(WordPhraseAdmin, self).save_related(request, form, formsets, change)
        if form.instance.picture_set.all():
            for pic in form.instance.picture_set.all():
                for translation in form.instance.translations.all():
                    models.Picture.objects.filter(wordphrase=translation).delete()
                    translation.picture_set.add(pic)
                    translation.save()


admin.site.register(models.Language)
admin.site.register(models.WordPhrase, WordPhraseAdmin)
admin.site.register(models.Picture)