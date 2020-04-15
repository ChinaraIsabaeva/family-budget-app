from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

from core.forms import LoginForm
from core.views import HomeView

admin.autodiscover()

urlpatterns = [
    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='login.html', form_class=LoginForm
        ),
        name='login'
    ),
    path(
        'logout/',
        auth_views.LogoutView.as_view(),
        name='logout'
    ),
    path('', login_required(HomeView.as_view()), name='home'),

    #app urls
    path(
        'expenses/', include('expenses.urls', namespace='expenses')
    ),
    path(
        'envelopes/', include('envelopes.urls', namespace='envelopes')
    ),

    # admin page
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
]
