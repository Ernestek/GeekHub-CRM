from rest_framework import serializers

from projects.serializers.users_in_project import UsersShortInfoSerializers
from tasks.models import UserTask


class UserTasksInProjectSerializer(serializers.ModelSerializer):
    user = UsersShortInfoSerializers()
    class Meta:
        model = UserTask
        fields = (
            'id',
            'user',
            'title',
            'status',
            'created_at',
        )
