from django.contrib.auth import authenticate
from django.core.mail import send_mail
from django.conf import settings
from drf_spectacular.utils import extend_schema
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken

# from .serializers import PasswordResetSerializer


@extend_schema(
    tags=['Login'],
)
class LoginView(ObtainAuthToken):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        email = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(request, email=email, password=password)
        if user.password_changed:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        elif not user.password_changed:
            return Response({'message': 'password not changed'})
        else:
            return Response({'error': 'Invalid credentials'}, status=400)

    def update(self, request, *args, **kwargs):
        ...

#
# class PasswordResetView(APIView):
#     serializer_class = PasswordResetSerializer
#
#     def post(self, request, *args, **kwargs):
#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         new_password = serializer.save()
#         subject = 'Password Reset Requested'
#         message = f'Your new password is {new_password}.'
#         from_email = settings.EMAIL_HOST_USER
#         recipient_list = [serializer.validated_data['email']]
#         send_mail(subject, message, from_email, recipient_list, fail_silently=False)
#         return Response({'detail': 'Password reset email has been sent.'})

#
# from django.contrib.auth.models import User
# from django.contrib.auth.tokens import default_token_generator
# from django.utils.encoding import force_bytes
# from django.utils.http import urlsafe_base64_encode
# from django.core.mail import send_mail
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from rest_framework.reverse import reverse
# from .serializers import ResetPasswordSerializer
#
# @api_view(['POST'])
# def reset_password(request):
#     email = request.data.get('email')
#     try:
#         user = User.objects.get(email=email)
#     except User.DoesNotExist:
#         return Response({'email': 'User with this email does not exist.'}, status=status.HTTP_400_BAD_REQUEST)
#
#     token = default_token_generator.make_token(user)
#     uid = urlsafe_base64_encode(force_bytes(user.pk))
#     reset_link = reverse('reset-password-confirm', args=[uid, token], request=request)
#     message = f'Click the link to reset your password: {reset_link}'