from django.contrib.auth import authenticate
from drf_spectacular.utils import extend_schema, OpenApiResponse
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.views import APIView

from account.serializers.login import LoginSerializer


@extend_schema(
    tags=('Account',),
    description='Verifies authentication data and response token',
    responses={
        308: OpenApiResponse(description='User is redirected to the temporary password change page.'),
        400: OpenApiResponse(description='Invalid data.'),
    }
)
class LoginView(ObtainAuthToken):
    permission_classes = (AllowAny,)
    authentication_classes = [TokenAuthentication]
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(request, email=email, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            if not user.password_changed:
                return Response({
                    'token': token.key,
                    'message': 'password not changed',
                }, status=status.HTTP_308_PERMANENT_REDIRECT)
            return Response({'token': token.key})
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


