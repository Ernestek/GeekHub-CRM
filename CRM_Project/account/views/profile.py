from django.contrib.auth import get_user_model
from drf_spectacular.utils import extend_schema
from rest_framework import status, viewsets
from rest_framework.authtoken.models import Token, TokenProxy
from rest_framework.generics import RetrieveUpdateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView

from account.serializers.profile import UserRetrieveSerializer
from common.permissions import TemporaryPasswordChanged

User = get_user_model()


@extend_schema(
    tags=['Account'],
    description='User profile data'
)
class UserRetrieveView(RetrieveUpdateAPIView):
    serializer_class = UserRetrieveSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated, TemporaryPasswordChanged]
    queryset = User.objects

    def get_object(self):
        return self.request.user

    def get_queryset(self):
        queryset = super().get_queryset()

        return queryset.only(
            'email',
            'first_name',
            'last_name',
            'phone_number',
            'phone_number2',
            'phone_number3',
        )
