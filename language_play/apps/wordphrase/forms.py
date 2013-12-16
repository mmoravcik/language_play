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
    hide_images = forms.BooleanField(label='Hide images', required=False)
    hide_words = forms.BooleanField(label='Hide words', required=False)
