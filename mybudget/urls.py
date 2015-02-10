from django.conf.urls import patterns, include, url
from django.contrib import admin

from .views import ExpenseUpdate, EnvelopeUpdate


admin.autodiscover()

urlpatterns = patterns('mybudget.views',
    # Examples:
    url(r'^$', 'home', name='home'),
    url(r'^envelopes/$', 'dashboard', name='envelopes'),
    url(r'^envelopes/(?P<pk>\d+)/update/$', EnvelopeUpdate.as_view(), name='envelope_update'),
    url(r'^expenses/$', 'expenses', name='expenses'),
    url(r'^expenses/regular/$', 'regular_expenses', name='regular_expenses'),
    url(r'^expenses/(?P<page>\d+)/$', 'expenses', name='expenses'),
    url(r'^expenses/(?P<pk>\d+)/update/$', ExpenseUpdate.as_view(), name='expense_update'),
    url(r'^expenses/(?P<envelope>\w.+)/$', 'expenses_by_envelope', name='filtered_expenses'),

    # admin page
    (r'^admin/', include(admin.site.urls)),
    (r'^i18n/', include('django.conf.urls.i18n')),
)
