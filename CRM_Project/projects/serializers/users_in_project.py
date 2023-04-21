from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UsersShortInfoSerializers(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            'id',
            'full_name',
            'email',
            'phone_number',
        )

    def get_full_name(self, obj: User) -> str:
        return obj.get_full_name()
