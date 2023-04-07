
from django.urls import path
from .views import index
from . import views

urlpatterns = [
    path('', index, name='index'),
    path('home', views.home, name='home'),
    path('login', views.login, name='login'),
]
