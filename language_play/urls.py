from django.conf.urls.static import static
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.views.generic import TemplateView

admin.autodiscover()

from views import HomeView
from language_play.apps.wordphrase import views


urlpatterns = patterns('',
    # Examples:
    url(r'^$', HomeView.as_view(), name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^alphabet/slovak/$', TemplateView.as_view(template_name='alphabet/slovak.html'), name='alphabet-slovak'),
    url(r'^language/select/$', views.SettingsFormView.as_view(), name='language-select'),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
