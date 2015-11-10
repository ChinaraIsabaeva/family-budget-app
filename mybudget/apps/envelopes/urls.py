from django.conf.urls import patterns, url
from django.contrib import admin

from .views import EnvelopeCreate, EnvelopeUpdate


admin.autodiscover()

urlpatterns = patterns('mybudget.apps.envelopes.views',

    url(r'^$', 'all_envelopes', name='envelopes'),
    url(r'(?P<pk>\d+)/update/$', EnvelopeUpdate.as_view(), name='envelope_update'),
    url(r'create/$', EnvelopeCreate.as_view(), name='envelope_create'),
)



