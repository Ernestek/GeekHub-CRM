from django.contrib.auth.models import User
from django.urls import reverse
from django.conf import settings
from rest_framework import serializers
from rest_framework.authtoken.models import Token

#
# class PasswordResetSerializer(serializers.Serializer):
#     email = serializers.EmailField()
#     # token, created = Token.objects.get_or_create(user=email)
#     # url = f'{settings.BASE_URL}{reverse("admin:login")}{token}'
#
#     def validate_email(self, value):
#         try:
#             User.objects.get(email=value)
#         except User.DoesNotExist:
#             raise serializers.ValidationError('User with this email does not exist.')
#         return value
#
#     def save(self):
#         email = self.validated_data['email']
#         user = User.objects.get(email=email)
#         new_password = User.objects.make_random_password()
#         user.set_password(new_password)
#         user.save()
#         return new_password
