from django.views.generic import TemplateView
from language_play.apps.wordphrase.models import WordPhrase


class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        ctx = super(HomeView, self).get_context_data()
        ctx['wordphrase'] = WordPhrase.objects.all().order_by('?')[0]
        return ctx