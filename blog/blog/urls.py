from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^panel/$', 'panel.views.login', name='login'),
    url(r'^panel/logout/$', 'panel.views.logout', name='logout'),
    url(r'^panel/signin/$', 'panel.views.signin', name='signin'),
    url(r'^blogpost/', include('blogpost.urls')),
)
