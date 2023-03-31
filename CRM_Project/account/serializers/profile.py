from django.contrib.auth import get_user_model
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
