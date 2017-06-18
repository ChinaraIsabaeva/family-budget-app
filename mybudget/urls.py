from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

from mybudget.general.forms import LoginForm
from mybudget.general.views import HomeView

admin.autodiscover()

urlpatterns = [
    url(
        r'^login/$',
        auth_views.LoginView.as_view(
            template_name='login.html', form_class=LoginForm
        ),
        name='login'
    ),
    url(
        r'^logout/$',
        auth_views.LogoutView.as_view(),
        name='logout'
    ),
    url(r'^$', login_required(HomeView.as_view()), name='home'),

    #app urls
    url(
        r'expenses/', include('mybudget.expenses.urls', namespace='expenses')
    ),
    url(
        r'envelopes/', include(
            'mybudget.envelopes.urls',
            namespace='envelopes')
    ),

    # admin page
    url(r'^admin/', include(admin.site.urls), name='admin'),
    url(r'^i18n/', include('django.conf.urls.i18n')),
]
