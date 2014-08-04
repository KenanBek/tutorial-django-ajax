from django.conf.urls import patterns, url

urlpatterns = patterns('sample1',
    url(r'^index/$', 'views.index', name='index'),
    url(r'^hello/$', 'views.hello', name='hello'),
)
