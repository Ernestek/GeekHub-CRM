from django.contrib.auth import get_user_model
from drf_spectacular.utils import extend_schema, OpenApiResponse
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from account.serializers.password_reset import RequestPasswordResetSerializer
from account.serializers.password_reset import ConfirmPasswordResetSerializer
from account.tasks import send_email_for_password_reset


@extend_schema(
    tags=('Account',),
    description='Request password reset.',
    responses={
        204: OpenApiResponse(description='User will receive link if account exists.'),
        403: OpenApiResponse(description='User is blocked.'),
    }
)
class PasswordResetRequestView(CreateAPIView):
    permission_classes = (AllowAny,)
    authentication_classes = []
    serializer_class = RequestPasswordResetSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_model = get_user_model()
        try:
            user = user_model.objects.get(email__iexact=serializer.data['email'])

            if user.is_active and user.password_changed:
                send_email_for_password_reset.apply_async(args=(user.pk,))
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                return Response(status=status.HTTP_403_FORBIDDEN)

        except user_model.DoesNotExist:
            return Response(status=status.HTTP_204_NO_CONTENT)


@extend_schema(
    tags=('Account',),
    description='Check uid and token and set new password',
    responses={
        204: OpenApiResponse(description='Password was set.'),
    }
)
class PasswordResetConfirmView(CreateAPIView):
    serializer_class = ConfirmPasswordResetSerializer
    authentication_classes = []
    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
