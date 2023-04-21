from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

User = get_user_model()


class SetNewPasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(write_only=True, style={'input_type': 'password'})
    new_password = serializers.CharField(write_only=True, style={'input_type': 'password'},
                                         validators=[validate_password])

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError(
                _('Your old password was entered incorrectly. Please enter it again.')
            )
        return value

    def validate(self, attrs):
        old_password = attrs['old_password']
        new_password = attrs['new_password']

        if old_password == new_password:
            raise serializers.ValidationError(
                {'new_password': _('New password must not match the old password.')},
                code="password_match",
            )

        return attrs

    def create(self, validated_data):
        password = self.validated_data['new_password']
        user = self.context['request'].user
        user.set_password(password)
        user.password_changed = True
        user.save(update_fields=['password', 'password_changed'])
        return user

    class Meta:
        model = User
        fields = (
            'password'
        )
