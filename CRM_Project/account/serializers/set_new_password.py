from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers


class RequestPasswordResetSerializer(serializers.Serializer):
    old_password = serializers.CharField()
    new_password = serializers.CharField()
    confirm_password = serializers.CharField(write_only=True, validators=[validate_password])

    def validate(self, attrs):
        pass
