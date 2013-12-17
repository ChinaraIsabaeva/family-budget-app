from django.conf.urls import patterns, include, url

from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'mybudget.finplanner.views.home'),
    url(r'^forms/$', 'mybudget.finplanner.views.forms'),
    url(r'^submitted/$', 'mybudget.finplanner.views.submitted'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
