from rest_framework import serializers
from django.utils.translation import gettext_lazy as _

from projects.models import Project
from projects.serializers.users_in_project import UsersShortInfoSerializers


class ProjectListSerializer(serializers.ModelSerializer):
    owner = UsersShortInfoSerializers()

    class Meta:
        model = Project
        fields = (
            'id',
            'name',
            'status',
            'owner',
        )


class ProjectRetrieveSerializer(serializers.ModelSerializer):
    owner = UsersShortInfoSerializers()
    users = UsersShortInfoSerializers(many=True)

    class Meta:
        model = Project
        fields = (
            'name',
            'partner',
            'users',
            'status',
            'owner',
            'summary',
            'created_at',
        )


class ProjectCreateSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Project
        fields = (
            'name',
            'partner',
            'users',
            'owner',
            'summary',
        )

    def validate(self, attrs):
        if attrs['owner'] in attrs.get('users', []):
            raise serializers.ValidationError(_('Owner cannot be in the users list.'))
        return attrs


class ProjectUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = (
            'name',
            'partner',
            'status',
            'summary',
        )

    # def validate(self, attrs):
    #     status = attrs.get('status', None)
    #
    #     if status == 'Done' and \
    #             any(task_status != 'Done' for task_status in self.instance.user_task.values_list('status', flat=True)):
    #         raise serializers.ValidationError('Status of this project cannot be updated to ready. '
    #                                           'The project has unfinished tasks')
    #
    #     return attrs
