from django.conf.urls import patterns, url
from django.contrib import admin

from .views import ExpenseUpdate


admin.autodiscover()

urlpatterns = patterns('mybudget.apps.expenses.views',
    url(r'all/$', 'all_expenses', name='expenses'),
    url(r'regular/$', 'regular_expenses', name='regular_expenses'),
    url(r'(?P<pk>\d+)/update/$', ExpenseUpdate.as_view(), name='expense_update'),
    url(r'(?P<envelope>\w.+)/$', 'expenses_by_envelope', name='filtered_expenses'),
)


