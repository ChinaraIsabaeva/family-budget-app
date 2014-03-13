from django.conf.urls import patterns, include, url
from django.contrib import admin
from .finplanner.views import ReserveCreate, ExpenseCreate




admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'mybudget.finplanner.views.home'),
    url(r'^expenses/$', 'mybudget.finplanner.views.expenses'),
    url(r'^expenses/add/$', ExpenseCreate.as_view(), name='expense_add'),
    url(r'^reserves/$', 'mybudget.finplanner.views.reserves'),
    url(r'^reserves/add/$', ReserveCreate.as_view(), name='reserve_add'),
    url(r'^reports/$', 'mybudget.finplanner.views.report'),
    url(r'^admin/', include(admin.site.urls)),

)
