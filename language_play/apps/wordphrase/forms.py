from django import forms
from language_play.apps.wordphrase.models import Language


class LanguageForm(forms.Form):
    source_lang = forms.ModelChoiceField(
        label='',
        queryset=Language.objects.all(),
        empty_label=None,
    )
    destination_lang = forms.ModelChoiceField(label='To',
        queryset=Language.objects.all().order_by('-id'),
        empty_label=None,
        widget=forms.HiddenInput(),
    )
