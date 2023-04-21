from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserRetrieveSerializer(serializers.ModelSerializer):
    # profile_image = serializers.ImageField(max_length=None, use_url=True, required=False)

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'phone_number',
            'phone_number2',
            'phone_number3',
            # 'profile_image',
        )


class UserUpdateSerializer(serializers.ModelSerializer):
    # first_name = serializers.CharField(max_length=None, default=False)
    # last_name = serializers.CharField(max_length=None, required=False)
    # phone_number = serializers.CharField(max_length=None, required=False)
    # phone_number2 = serializers.CharField(max_length=None, required=False)
    # phone_number3 = serializers.CharField(max_length=None, required=False)

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'phone_number',
            'phone_number2',
            'phone_number3',
        )


class SetProfileImageSerializer(serializers.ModelSerializer):
    profile_image = serializers.ImageField(max_length=None, required=False)

    class Meta:
        model = User
        fields = ('profile_image',)
