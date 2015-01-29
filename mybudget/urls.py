from django.conf.urls import patterns, include, url
from django.contrib import admin

from .views import ExpensesList, ExpenseUpdate, EnvelopeUpdate


admin.autodiscover()

urlpatterns = patterns('mybudget.views',
    # Examples:
    url(r'^$', 'home', name='home'),
    url(r'^envelopes/$', 'dashboard', name='envelopes'),
    url(r'^envelopes/(?P<pk>\d+)/update/$', EnvelopeUpdate.as_view(), name='envelope_update'),
    url(r'^envelopes/(?P<pk>\d+)/close/$', 'envelope_close', name='envelope_close'),
    url(r'^expenses/$', ExpensesList.as_view(), name='expenses'),
    url(r'^expenses/(?P<pk>\d+)/update/', ExpenseUpdate.as_view(), name='expense_update'),

    # admin page
    (r'^admin/', include(admin.site.urls)),
    (r'^i18n/', include('django.conf.urls.i18n')),
)
