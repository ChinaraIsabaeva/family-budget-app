from django.conf.urls import url
from django.contrib import admin

from mybudget.expenses import views


admin.autodiscover()

urlpatterns = [
    url(r'all/$', views.ExpenseListView.as_view(), name='all'),
    url(
        r'regular/$', views.RegularExpenseListView.as_view(),
        name='regular_expenses'
    ),
    url(
        r'(?P<pk>\d+)/update/$', views.ExpenseUpdateView.as_view(),
        name='expense_update'
    ),
    url(
        r'create/$', views.ExpenseCreateView.as_view(),
        name='expense_create'
    ),
]
