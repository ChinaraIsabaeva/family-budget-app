__author__ = 'mybudget'
from django.conf.urls import patterns, url
from django.contrib import admin
from .views import ExpenseCreate
admin.autodiscover()

urlpatterns = patterns('mybudget.apps.expenses.views',
    url(r'^add/$', ExpenseCreate.as_view(), name='expenses add'),
    url(r'^$', 'expenses', name='expenses'),

)