from django.db import models


class WordPhrase(models.Model):
    WORD, PHRASE = 1, 2

    TYPE = (
        (WORD, 'Word'),
        (PHRASE, 'Phrase'),
    )

    text = models.CharField(max_length=255)
    language = models.ForeignKey('Language')
    sounds = models.CharField(max_length=255, null=True, blank=True)
    type = models.SmallIntegerField(max_length=1, choices=TYPE)

    def __unicode__(self):
        return self.text


class Language(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return "%s - %s" % (self.code, self.name)