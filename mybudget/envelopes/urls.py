from django.conf.urls import url
from django.contrib import admin

from mybudget.envelopes.views import EnvelopeCreate, EnvelopeUpdate, EnvelopeListView


admin.autodiscover()

urlpatterns = [
    url(r'all/$', EnvelopeListView.as_view(), name='all'),
    url(r'(?P<pk>\d+)/update/$', EnvelopeUpdate.as_view(), name='envelope_update'),
    url(r'create/$', EnvelopeCreate.as_view(), name='envelope_create'),
    # url(r'select/$', 'envelope_select', name='envelope_select'),
]



