from django.urls import path
from django.urls import include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

from .views import LoginView

app_name = 'account'

router = DefaultRouter()

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    # path('api-token-auth/', obtain_auth_token, name='api-token-auth'),
]
