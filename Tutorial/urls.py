from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Tutorial.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^polls/', include('polls.urls')),
    # include() references the given urlsConf and passes only of the rest of the url string
    url(r'^admin/', include(admin.site.urls)),
)


# /polls/index/3 hits here first
# it matches the first url, which then calls polls.urls with shortend /index/3