from django.conf.urls import patterns, include, url

from django.contrib import admin



admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'mybudget.finplanner.views.home'),
    url(r'^form/', 'mybudget.finplanner.views.forms'),
    url(r'^forms/expense_form/', 'mybudget.finplanner.views.expense_form'),
    url(r'^expenses/', 'mybudget.finplanner.views.expenses'),
    url(r'^reserves/', 'mybudget.finplanner.views.reserves'),
    url(r'^submitted/', 'mybudget.finplanner.views.submitted'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),

)
