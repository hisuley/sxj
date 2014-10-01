from django.conf.urls import patterns, url

urlpatterns = patterns('',
        url(r'display/$', 'blogpost.views.blogDisplay', name='display'),
        url(r'writenew/$', 'blogpost.views.blogWritenew', name='writenew'),
        url(r'edit//$', 'blogpost.views.blogEdit', name='edit'),
        url(r'delete/(?P<id>\d*)/$', 'blogpost.views.blogDelete', name='delete'),
        url(r'search/$', 'blogpost.views.blogSearch', name='search'),

)