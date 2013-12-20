from language_play.apps.wordphrase.forms import SettingsForm


def wordphrase(request):
    if not 'source_lang' in request.session:
        request.session['source_lang'] = SettingsForm.SOURCE_LANG_QUERYSET[0].id

    if not 'destination_lang' in request.session:
        request.session['destination_lang'] = SettingsForm.DESTINATION_LANG_QUERYSET[0].id

    return {
        'settings_form': SettingsForm(initial={
            'source_lang':request.session.get('source_lang',''),
            'destination_lang':request.session.get('destination_lang',''),
            'show_images':request.session.get('show_images', True),
            'show_wordphrase':request.session.get('show_wordphrase', True),
            'show_translations':request.session.get('show_translations', True),
        })
    }