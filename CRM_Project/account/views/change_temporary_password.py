from drf_spectacular.utils import extend_schema, OpenApiResponse
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from account.serializers.set_new_password import SetNewPasswordSerializer


@extend_schema(
    tags=('Account',),
    description='Use this endpoint if user authentication, but password not changed',
    responses={
        204: OpenApiResponse(description='User changed the temporary password, redirect to the main page.'),
    }
)
class ChangeTemporaryPasswordView(CreateAPIView):
    serializer_class = SetNewPasswordSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = request.user
        if not user.password_changed:
            user.auth_token.delete()
            token = Token.objects.create(user=user)
            serializer.save()
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_204_NO_CONTENT)
