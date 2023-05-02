from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

User = get_user_model()


class UserRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'phone_number',
            'phone_number2',
            'phone_number3',
        )


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'phone_number',
            'phone_number2',
            'phone_number3',
        )

    def validate(self, attrs):
        first_name = attrs.get('first_name')
        last_name = attrs.get('last_name')
        phone_number = attrs.get('phone_number', None)
        phone_number2 = attrs.get('phone_number2', None)
        phone_number3 = attrs.get('phone_number3', None)

        # phones = [phone for phone in [phone_number, phone_number2, phone_number3] if phone]
        # if len(phones) != len(set(phones)):
        #     raise ValidationError(
        #         _('Phone numbers must be unique.')
        #     )

        if first_name == '':
            raise serializers.ValidationError(
                {'last_name': _('This field may not be blank.')},
                code="last_name",
            )

        if last_name == '':
            raise serializers.ValidationError(
                {'last_name': _('This field may not be blank.')},
                code="last_name",
            )

        return attrs


class SetProfileImageSerializer(serializers.ModelSerializer):
    profile_image = serializers.ImageField(max_length=None, required=False)

    class Meta:
        model = User
        fields = ('profile_image',)
