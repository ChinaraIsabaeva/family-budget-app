from django.conf.urls import patterns, include, url
from mybudget.finplanner.views import ReservesCreate, ReservesUpdate, ReservesDelete
from django.contrib import admin



admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'mybudget.finplanner.views.home'),
    url(r'^expenses/$', 'mybudget.finplanner.views.expenses'),
    url(r'^reserves/$', 'mybudget.finplanner.views.reserves'),
    url(r'^reserves/add/$', ReservesCreate.as_view(), name='reserves_add'),
    url(r'^reserves/(?P<pk>\d+)/$', ReservesUpdate.as_view(), name='reserves_update'),
    url(r'^reserves/(?P<pk>\d+)/delete/$', ReservesDelete.as_view(), name='reserves_delete'),
    url(r'^admin/', include(admin.site.urls)),

)
