from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.urls import path

from user import views
from .views import LoginView


app_name = 'user'

urlpatterns = [
    path('', views.index, name="index"),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(
        r'^logout/$',
        auth_views.logout,
        {'template_name': 'user/logout.html'},
        name='logout'
    ),
]
