from django.conf.urls.static import static
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.views.generic import TemplateView

admin.autodiscover()

from language_play.apps.wordphrase import views


urlpatterns = patterns('',
    url(r'^$',
        TemplateView.as_view(template_name='home.html'),
        name='home'),
    url(r'^wordphrase/(?P<language_code>\w+)/(?P<wordphrase_id>\d+)/(?P<wordphrase_text>)[\w\-]+/$',
        views.WordPhraseView.as_view(),
        name='wordphrase-detail'),
    url(r'^wordphrase/list/(?P<language_id>\d+)/$',
        views.WordPhraseListView.as_view(),
        name='wordphrase-list'),
    url(r'^wordphrase/random/$',
        views.GetRandomWordPhraseView.as_view(),
        name='wordphrase-random'),
    url(r'^alphabet/slovak/$',
        TemplateView.as_view(template_name='alphabet/slovak.html'),
        name='alphabet-slovak'),
    url(r'^language/select/$',
        views.SettingsFormView.as_view(),
        name='language-select'),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
