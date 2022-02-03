from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import login

urlpatterns = [
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('login/', login, name='login'),
]
