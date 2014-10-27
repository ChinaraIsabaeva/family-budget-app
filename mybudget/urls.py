from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'mybudget.views.home', name='home'),
    url(r'^envelopes', 'mybudget.views.dashboard', name='envelopes'),

    # admin page
    (r'^admin/', include(admin.site.urls)),
)
