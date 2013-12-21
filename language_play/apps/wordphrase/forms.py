from django import forms
from language_play.apps.wordphrase.models import Language


class SettingsForm(forms.Form):
    SOURCE_LANG_QUERYSET = Language.objects.all().order_by('id')
    DESTINATION_LANG_QUERYSET = Language.objects.all().order_by('-id')

    source_lang = forms.ModelChoiceField(
        label='',
        queryset=SOURCE_LANG_QUERYSET,
        empty_label=None,
    )

    destination_lang = forms.ModelChoiceField(label='to',
        queryset=DESTINATION_LANG_QUERYSET,
        empty_label=None,
    )

    show_images = forms.BooleanField(label='Images', required=False)
    show_wordphrase = forms.BooleanField(label='Words', required=False)
    show_translations = forms.BooleanField(label='Translations', required=False)
    next = forms.CharField(widget=forms.HiddenInput)
