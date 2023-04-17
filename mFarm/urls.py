from django.urls import path
from .views import index
from . import views

urlpatterns = [
    path('', index, name='index'),
    path('home', views.home, name='home'),
    path('login', views.loginPage, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('signup', views.signup, name='signup')
]
