from django.urls import path
from django.urls import include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

# from account.views import AuthenticationView

app_name = 'account'

router = DefaultRouter()

urlpatterns = [
    path('api-token-auth/', obtain_auth_token, name='api-token-auth'),
    # path('auth', AuthenticationView.as_view())
    # path('', include(router.urls)),
]
