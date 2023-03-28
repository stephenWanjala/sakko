from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

from . import views
from .views import LogoutView

urlpatterns = [
    path("", views.apiRoutes),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("farmers/", views.getFarmers),
    path("sacco", views.createSaco),
    path("saccos", views.getSacco),
    path("farmer/", views.addFarmer),
    path('logout/', LogoutView.as_view(), name='auth_logout'),


]
