from django.conf.urls import patterns, url

urlpatterns = patterns('snippets.v1_0.views',
    url(r'^v1_0/snippets/$', 'snippet_list'),
    url(r'^v1_0/snippets/(?P<pk>[0-9]+)/$', 'snippet_detail'),
)

