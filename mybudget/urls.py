from django.conf.urls import patterns, include, url
from django.contrib import admin
from mybudget.apps.main.views import ReserveCreate




admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'mybudget.apps.main.views.home'),
    url(r'^expenses/', include('mybudget.apps.expenses.urls', namespace='expenses')),
    url(r'^reports/', include('mybudget.apps.reports.urls')),
    url(r'^reserves/$', 'mybudget.apps.main.views.reserves'),
    url(r'^reserves/add/$', ReserveCreate.as_view(), name='reserve_add'),
    url(r'^admin/', include(admin.site.urls)),

)
