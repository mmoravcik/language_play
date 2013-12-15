from django.views.generic import TemplateView
from language_play.apps.wordphrase.models import WordPhrase
from language_play.apps.wordphrase.forms import LanguageForm


class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        ctx = super(HomeView, self).get_context_data()

        queryset = WordPhrase.objects.all()
        if 'source_lang' in self.request.session:
            queryset = queryset.filter(language=self.request.session['source_lang'])

        wordphrase = queryset.order_by('?')[0]
        translations = wordphrase.translations.all()

        ctx['wordphrase'] = wordphrase
        ctx['language_form'] = LanguageForm(initial={
            'source_lang':self.request.session.get('source_lang', ''),
            'destination_lang':self.request.session.get('destination_lang', '')
        })
        return ctx