from django import forms
from language_play.apps.wordphrase.models import Language


class SettingsForm(forms.Form):
    source_lang = forms.ModelChoiceField(
        label='',
        queryset=Language.objects.all(),
        empty_label=None,
    )
    destination_lang = forms.ModelChoiceField(label='',
        queryset=Language.objects.all().order_by('-id'),
        empty_label=None,
    )
    show_images = forms.BooleanField(label='Images', required=False)
    show_wordphrase = forms.BooleanField(label='Words', required=False)
    show_translations = forms.BooleanField(label='Translations', required=False)
