from rest_framework import serializers

from tasks.models import UserTask
from tasks.serializers.user_search import UserSearchSerializer


class UserTasksInProjectSerializer(serializers.ModelSerializer):
    user = UserSearchSerializer()

    class Meta:
        model = UserTask
        fields = (
            'id',
            'user',
            'title',
            'status',
            'created_at',
        )
