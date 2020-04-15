from django.urls import path
from django.contrib import admin
from django.contrib.auth.decorators import login_required

from envelopes.views import EnvelopeCreate, EnvelopeUpdate, EnvelopeListView


admin.autodiscover()

app_name = 'envelopes'

urlpatterns = [
    path(
        'all/',
        login_required(EnvelopeListView.as_view()),
        name='all'
    ),
    path(
        '<int:pk>/update/',
        login_required(EnvelopeUpdate.as_view()),
        name='envelope_update'
    ),
    path(
        'create/',
        login_required(EnvelopeCreate.as_view()),
        name='envelope_create'
    ),
    # url(r'select/$', 'envelope_select', name='envelope_select'),
]
