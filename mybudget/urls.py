from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'mybudget.views.home'),
    url(r'^budget/$', 'mybudget.apps.budget.views.budget', name='budget'),

    (r'^admin/', include(admin.site.urls)),
)
