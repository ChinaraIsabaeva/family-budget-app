from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'mybudget.views.home', name='home'),

    #app urls
    url(r'expenses/', include('mybudget.apps.expenses.urls', namespace='expenses')),
    url(r'envelopes/', include('mybudget.apps.envelopes.urls', namespace='envelopes')),


    # admin page
    (r'^admin/', include(admin.site.urls)),
    (r'^i18n/', include('django.conf.urls.i18n')),
)
