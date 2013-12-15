from language_play.apps.wordphrase.forms import LanguageForm
from django.views.generic.edit import FormView


class LanguageFormView(FormView):
    form_class = LanguageForm
    success_url = '/'
    template_name = 'home.html'

    def form_valid(self, form):
        self.request.session['source_lang'] = form.cleaned_data['source_lang'].id
        self.request.session['destination_lang'] = form.cleaned_data['destination_lang'].id

        return super(LanguageFormView, self).form_valid(form)