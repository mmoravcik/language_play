from django import forms
from language_play.apps.wordphrase.models import Language


class LanguageForm(forms.Form):
    source_lang = forms.ModelChoiceField(queryset=Language.objects.all(),
        empty_label=None)
    destination_lang = forms.ModelChoiceField(queryset=Language.objects.all(),
        empty_label=None)
