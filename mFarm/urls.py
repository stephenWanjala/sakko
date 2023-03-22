
from django.urls import path
from .views import index
from . import views

app_name = "mFarm"

urlpatterns = [
    path('', index, name='index'),
    path("register/", views.register_request, name="register"),
    path("login/", views.login_request, name="login"),  # add login path to urls
    path("logout/", views.logout_request, name="logout")  # add logout path to urls
]
