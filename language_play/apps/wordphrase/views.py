from language_play.apps.wordphrase.forms import SettingsForm
from django.views.generic.edit import FormView


class SettingsFormView(FormView):
    form_class = SettingsForm
    success_url = '/'
    template_name = 'home.html'

    def form_valid(self, form):
        self.request.session['source_lang'] = form.cleaned_data['source_lang'].id
        self.request.session['destination_lang'] = form.cleaned_data['destination_lang'].id
        self.request.session['hide_images'] = form.cleaned_data['hide_images']
        self.request.session['hide_words'] = form.cleaned_data['hide_words']

        return super(SettingsFormView, self).form_valid(form)