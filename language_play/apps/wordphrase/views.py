from django.views.generic.edit import FormView
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.base import RedirectView
from django.core.urlresolvers import reverse
from django.utils.text import slugify

from apps.wordphrase.forms import SettingsForm
from apps.wordphrase.models import WordPhrase


class SettingsFormView(FormView):
    form_class = SettingsForm
    template_name = 'home.html'

    def form_valid(self, form):
        self.set_next_url(form)
        self.request.session['source_lang'] = form.cleaned_data['source_lang'].id
        self.request.session['destination_lang'] = form.cleaned_data['destination_lang'].id
        self.request.session['show_images'] = form.cleaned_data['show_images']
        self.request.session['show_wordphrase'] = form.cleaned_data['show_wordphrase']
        self.request.session['show_translations'] = form.cleaned_data['show_translations']

        return super(SettingsFormView, self).form_valid(form)

    def set_next_url(self, form):
        if self.request.session['source_lang'] == form.cleaned_data['source_lang'].id:
            self.success_url = form.cleaned_data['next']
        else:
            self.success_url = reverse('wordphrase-random')


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


class WordPhraseListView(ListView):
    model = WordPhrase

    def get_queryset(self):
        return self.model.objects.filter(language=self.kwargs['language_id'])


class GetRandomWordPhraseView(RedirectView):
    permanent = False

    def get_redirect_url(self, *args, **kwargs):
        wordphrase = WordPhrase.objects.filter(language=self.request.session['source_lang']).order_by('?')[0]
        params = dict(
            language_code=wordphrase.language.code,
            wordphrase_id=wordphrase.pk,
            wordphrase_text=slugify(wordphrase.text),
        )
        return reverse('wordphrase-detail', kwargs=params)