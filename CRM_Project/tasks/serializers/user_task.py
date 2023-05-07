from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.utils.translation import gettext_lazy as _

from projects.models import Project
from projects.serializers.users_in_project import UsersShortInfoSerializers
from tasks.models import UserTask

User = get_user_model()


class UserTasksListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTask
        fields = (
            'id',
            'title',
            'status',
            'created_at',
        )


class UserTasksRetrieveSerializer(serializers.ModelSerializer):
    user = UsersShortInfoSerializers()
    user_assigned = serializers.CharField(source='user.email', read_only=True)

    class Meta:
        model = UserTask
        fields = (
            'id',
            'title',
            'text',
            'status',
            'user',
            'user_assigned',
            'updated_at',
            'created_at',
        )


class UserTaskCreateSerializer(serializers.ModelSerializer):
    user_assigned = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = UserTask
        fields = (
            'user',
            'title',
            'text',
            'project',
            'user_assigned',
        )

    def validate(self, attrs):
        project_id = attrs.get('project', None)
        user_id = attrs.get('user').id
        if project_id:
            try:
                project = Project.objects.select_related('owner').prefetch_related('users').get(pk=project_id.id)
            except (Project.DoesNotExist, ValueError, TypeError, OverflowError):
                raise serializers.ValidationError(
                    {'project_id': _('Invalid project id')},
                    code='invalid_project_id',
                )

            if not any((user_id in project.users.values_list('id', flat=True), user_id == project.owner.id)):
                raise serializers.ValidationError(
                    {'user_id': _('This user is not on the project team')},
                    code='invalid_user_id',
                )

        return attrs


class MyTaskCreateSerializer(serializers.ModelSerializer):
    user_assigned = serializers.HiddenField(default=serializers.CurrentUserDefault())
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = UserTask
        fields = (
            'user',
            'title',
            'text',
            'user_assigned',
        )


class UserTasksUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTask
        fields = (
            'status',
        )
