from django.views.generic.edit import FormView
from django.views.generic.detail import DetailView
from django.views.generic.base import RedirectView
from django.core.urlresolvers import reverse
from django.utils.text import slugify

from language_play.apps.wordphrase.forms import SettingsForm
from language_play.apps.wordphrase.models import WordPhrase


class SettingsFormView(FormView):
    form_class = SettingsForm
    success_url = '/'
    template_name = 'home.html'

    def form_valid(self, form):
        self.request.session['source_lang'] = form.cleaned_data['source_lang'].id
        self.request.session['destination_lang'] = form.cleaned_data['destination_lang'].id

        self.request.session['show_images'] = form.cleaned_data['show_images']
        self.request.session['show_wordphrase'] = form.cleaned_data['show_wordphrase']
        self.request.session['show_translations'] = form.cleaned_data['show_translations']

        return super(SettingsFormView, self).form_valid(form)


class WordPhraseView(DetailView):
    model = WordPhrase

    def get_object(self, queryset=None):
        return self.model.objects.get(pk=self.kwargs['wordphrase_id'])

    def get_context_data(self, **kwargs):
        ctx = super(WordPhraseView, self).get_context_data()
        translations = self.object.translations.filter(language=self.request.session['destination_lang'])

        ctx['translations'] = translations
        ctx['show_images'] = self.request.session.get('show_images', True)
        ctx['show_wordphrase'] = self.request.session.get('show_wordphrase', True)
        ctx['show_translations'] = self.request.session.get('show_translations', True)

        return ctx


class GetRandomWordPhraseView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        wordphrase = WordPhrase.objects.filter(language=self.request.session['source_lang']).order_by('?')[0]
        params = dict(
            language_code=wordphrase.language.code,
            wordphrase_id=wordphrase.pk,
            wordphrase_text=slugify(wordphrase.text),
        )
        return reverse('wordphrase-detail', kwargs=params)