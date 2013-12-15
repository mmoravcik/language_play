from django.views.generic import TemplateView
from language_play.apps.wordphrase.models import WordPhrase
from language_play.apps.wordphrase.forms import LanguageForm


class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        ctx = super(HomeView, self).get_context_data()

        wordphrases = WordPhrase.objects.all()
        if 'source_lang' in self.request.session:
            wordphrases = wordphrases.filter(language=self.request.session['source_lang'])

        ctx['wordphrase'] = wordphrases.order_by('?')[0]
        ctx['language_form'] = LanguageForm(initial={
            'source_lang':self.request.session.get('source_lang', ''),
            'destination_lang':self.request.session.get('destination_lang', '')
        })
        return ctx