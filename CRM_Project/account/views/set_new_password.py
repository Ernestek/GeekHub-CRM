from drf_spectacular.utils import extend_schema, OpenApiResponse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.generics import CreateAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response

from account.serializers.set_new_password import SetNewPasswordSerializer
from common.permissions import TemporaryPasswordChanged


@extend_schema(
    tags=('Account',),
    description='Check old password and set new password, new token',
    responses={
        201: OpenApiResponse(description='Password reset, set new token.')
    }
)
class SetNewPasswordView(CreateAPIView):
    serializer_class = SetNewPasswordSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated, TemporaryPasswordChanged]

    def get_object(self):
        obj = get_object_or_404(self.request.user, pk=self.kwargs["pk"])
        self.check_object_permissions(self.request, obj)
        return obj

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = request.user
        user.auth_token.delete()
        token = Token.objects.create(user=user)
        serializer.save()
        return Response({'token': token.key}, status=status.HTTP_201_CREATED)
