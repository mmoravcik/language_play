from language_play.apps.wordphrase.forms import SettingsForm


def wordphrase(request):
    return {
        'settings_form': SettingsForm(initial={
            'source_lang':request.session.get('source_lang', ''),
            'destination_lang':request.session.get('destination_lang', ''),
            'show_images':request.session.get('show_images', True),
            'show_wordphrase':request.session.get('show_wordphrase', True),
            'show_translations':request.session.get('show_translations', True),
        })
    }