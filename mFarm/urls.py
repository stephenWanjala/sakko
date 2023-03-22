
from django.urls import path
from .views import index
from . import views

urlpatterns = [
    path('', index, name='index'),
    path("register", views.register_request, name="register")
]
