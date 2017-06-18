from django.conf.urls import include, url
from django.contrib import admin

from mybudget.general.views import HomeView

admin.autodiscover()

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),

    #app urls
    url(
        r'expenses/', include('mybudget.expenses.urls', namespace='expenses')
    ),
    url(
        r'envelopes/', include(
            'mybudget.envelopes.urls',
            namespace='envelopes')
    ),

    # admin page
    url(r'^admin/', include(admin.site.urls), name='admin'),
    url(r'^i18n/', include('django.conf.urls.i18n')),
]
