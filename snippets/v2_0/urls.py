from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = patterns('snippets.v2_0.views',
    url(r'^v2_0/snippets/$', 'snippet_list'),
    url(r'^v2_0/snippets/(?P<pk>[0-9]+)/$', 'snippet_detail'),
)

urlpatterns = format_suffix_patterns(urlpatterns)
