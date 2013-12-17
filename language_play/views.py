from django.views.generic import TemplateView
from language_play.apps.wordphrase.models import WordPhrase
from language_play.apps.wordphrase.forms import SettingsForm


class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        ctx = super(HomeView, self).get_context_data()

        if not 'source_lang' in self.request.session:
            self.request.session['source_lang'] = SettingsForm.SOURCE_LANG_QUERYSET[0].id

        wordphrase = WordPhrase.objects.filter(language=self.request.session['source_lang']).order_by('?')[0]

        if not 'destination_lang' in self.request.session:
            self.request.session['destination_lang'] = SettingsForm.DESTINATION_LANG_QUERYSET[0].id

        translations = wordphrase.translations.filter(language=self.request.session['destination_lang'])

        ctx['wordphrase'] = wordphrase
        ctx['translations'] = translations
        ctx['show_images'] = self.request.session.get('show_images', True)
        ctx['show_wordphrase'] = self.request.session.get('show_wordphrase', True)
        ctx['show_translations'] = self.request.session.get('show_translations', True)

        ctx['language_form'] = SettingsForm(initial={
            'source_lang':self.request.session.get('source_lang', ''),
            'destination_lang':self.request.session.get('destination_lang', ''),
            'show_images':self.request.session.get('show_images', True),
            'show_wordphrase':self.request.session.get('show_wordphrase', True),
            'show_translations':self.request.session.get('show_translations', True),
        })
        return ctx