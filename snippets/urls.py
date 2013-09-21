from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^', include('snippets.v1_0.urls')),
    url(r'^', include('snippets.v2_0.urls')),
    url(r'^', include('snippets.v3_0.urls')),
    url(r'^', include('snippets.v3_1.urls')),
    url(r'^', include('snippets.v3_2.urls')),
    url(r'^', include('snippets.v4_0.urls')),
)
