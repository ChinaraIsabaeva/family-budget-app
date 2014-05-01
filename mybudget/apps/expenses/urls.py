__author__ = 'dachee'
from django.conf.urls import patterns, url
from django.contrib import admin
from .views import ExpenseCreate
admin.autodiscover()

urlpatterns = patterns('mybudget.apps.expenses.views',
    url(r'', 'expenses'),
    url(r'^add/', ExpenseCreate.as_view, name='expenses add'),

)