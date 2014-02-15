from django.conf.urls import patterns, include, url
from mybudget.finplanner.views import ReserveCreate, ReserveUpdate, ReserveDelete, ExpenseCreate
from django.contrib import admin



admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'mybudget.finplanner.views.home'),
    url(r'^expenses/$', 'mybudget.finplanner.views.expenses'),
    url(r'^expenses/add/$', ExpenseCreate.as_view(), name='expense_add'),
    url(r'^reserves/$', 'mybudget.finplanner.views.reserves'),
    url(r'^reserves/add/$', ReserveCreate.as_view(), name='reserve_add'),
    url(r'^reserves/(?P<pk>\d+)/$', ReserveUpdate.as_view(), name='reserves_update'),
    url(r'^reserves/(?P<pk>\d+)/delete/$', ReserveDelete.as_view(), name='reserves_delete'),
    url(r'^admin/', include(admin.site.urls)),

)
