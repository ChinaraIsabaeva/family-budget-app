from django.urls import path
from django.contrib import admin
from django.contrib.auth.decorators import login_required

from expenses import views

admin.autodiscover()

app_name = 'expenses'

urlpatterns = [
    path('all/', login_required(views.ExpenseListView.as_view()), name='all'),
    path(
        'regular/', login_required(views.RegularExpenseListView.as_view()),
        name='regular_expenses'
    ),
    path(
        '<int:pk>/update/',
        login_required(views.ExpenseUpdateView.as_view()),
        name='expense_update'
    ),
    path(
        'create/', login_required(views.ExpenseCreateView.as_view()),
        name='expense_create'
    ),
]
