from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='home.html')),  # Directly render index.html file
    url(r'^admin/', include(admin.site.urls)),
    url(r'^sample1/', include('sample1.urls', 'sample1')),
    url(r'^sample2/', include('sample2.urls', 'sample2')),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
