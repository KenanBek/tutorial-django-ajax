from django.conf.urls import patterns, url

urlpatterns = patterns('sample2',
    url(r'index/$', 'views.index', name='index'),
)
