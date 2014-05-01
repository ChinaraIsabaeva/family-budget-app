__author__ = 'dachee'
from django.conf.urls import patterns, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('mybudget.apps.reports.views',
    url(r'', 'report'),

)