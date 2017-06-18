from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.decorators import login_required

from mybudget.envelopes.views import EnvelopeCreate, EnvelopeUpdate, EnvelopeListView


admin.autodiscover()

urlpatterns = [
    url(
        r'all/$',
        login_required(EnvelopeListView.as_view()),
        name='all'
    ),
    url(
        r'(?P<pk>\d+)/update/$',
        login_required(EnvelopeUpdate.as_view()),
        name='envelope_update'
    ),
    url(
        r'create/$',
        login_required(EnvelopeCreate.as_view()),
        name='envelope_create'
    ),
    # url(r'select/$', 'envelope_select', name='envelope_select'),
]



