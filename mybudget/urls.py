from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'mybudget.views.home', name='home'),
    url(r'^envelopes', 'mybudget.views.dashboard', name='envelopes'),
    url(r'^expenses', 'mybudget.views.expenses', name='expenses'),

    # admin page
    (r'^admin/', include(admin.site.urls)),
    (r'^i18n/', include('django.conf.urls.i18n')),
)
