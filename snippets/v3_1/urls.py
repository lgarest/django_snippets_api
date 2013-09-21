from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from snippets.v3_1 import views

urlpatterns = patterns('',
    url(r'^v3_1/snippets/$', views.SnippetList.as_view()),
    url(r'^v3_1/snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)
