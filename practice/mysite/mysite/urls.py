from django.conf.urls import patterns, include, url
from django.contrib import admin
from blog.views import archive
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', archive)
)

urlpatterns += patterns('',
    (r'^pages/', include('django.contrib.flatpages.urls')),
)