from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.decorators import login_required

from mybudget.expenses import views


admin.autodiscover()

urlpatterns = [
    url(r'all/$', login_required(views.ExpenseListView.as_view()), name='all'),
    url(
        r'regular/$', login_required(views.RegularExpenseListView.as_view()),
        name='regular_expenses'
    ),
    url(
        r'(?P<pk>\d+)/update/$',
        login_required(views.ExpenseUpdateView.as_view()),
        name='expense_update'
    ),
    url(
        r'create/$', login_required(views.ExpenseCreateView.as_view()),
        name='expense_create'
    ),
]
