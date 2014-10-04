from django.conf.urls import patterns, url

urlpatterns = patterns('',
        url(r'list/$', 'blogpost.views.blogList', name='list'),
        url(r'writenew/$', 'blogpost.views.blogWritenew', name='writenew'),
        url(r'edit/(?P<id>\d*)/$', 'blogpost.views.blogEdit', name='edit'),
        url(r'delete/(?P<id>\d*)/$', 'blogpost.views.blogDelete', name='delete'),
        url(r'search/$', 'blogpost.views.blogSearch', name='search'),
        url(r'showdetail/(?P<id>\d*)/$', 'blogpost.views.blogShowDetail', name='showdetail')

)