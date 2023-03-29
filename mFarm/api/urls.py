from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

from . import views
from .views import LogoutView, ChangePasswordView, UpdateProfileView

urlpatterns = [
    path("", views.apiRoutes),
    path('register',views.RegisterView.as_view(),name="register"),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("farmers/", views.getFarmers),
    path("sacco", views.createSaco),
    path("saccos", views.getSacco),
    path("farmer/", views.addFarmer),
    path('change_password/<int:pk>/', ChangePasswordView.as_view(), name='api_change_password'),
    path('update_profile/<int:pk>/', UpdateProfileView.as_view(), name='api_update_profile'),
    path('logout/', LogoutView.as_view(), name='api_logout'),

]
