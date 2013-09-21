from django.conf.urls import patterns, url, include
from rest_framework.urlpatterns import format_suffix_patterns
from snippets.v4_0 import views

urlpatterns = patterns('',
    url(r'^v4_0/snippets/$', views.SnippetList.as_view()),
    url(r'^v4_0/snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += patterns('',
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
