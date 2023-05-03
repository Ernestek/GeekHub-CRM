from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.utils.translation import gettext_lazy as _

from projects.models import Project
from projects.serializers.users_in_project import UsersShortInfoSerializers
from tasks.models import UserTask
from tasks.serializers.user_search import UserSearchSerializer

User = get_user_model()


class UserTasksListSerializer(serializers.ModelSerializer):
    # user = UserSearchSerializer()

    class Meta:
        model = UserTask
        fields = (
            'id',
            # 'user',
            'title',
            'status',
            'created_at',
        )


class UserTasksRetrieveSerializer(serializers.ModelSerializer):
    user = UsersShortInfoSerializers()
    user_assigned = serializers.CharField(source='user.email', read_only=True)
    # user_assigned = UserSearchSerializer()

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
    project = serializers.IntegerField(required=False, allow_null=True)

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
        user_id = attrs.get('user')

        if project_id:
            try:
                project = Project.objects.select_related('owner').prefetch_related('users').get(pk=project_id)
            except (Project.DoesNotExist, ValueError, TypeError, OverflowError):
                raise serializers.ValidationError(
                    {'project_id': _('Invalid project id')},
                    code='invalid_project_id',
                )

            if not (user_id in project.users.values_list('id', flat=True)):
                raise serializers.ValidationError(
                    {'user_id': _('This user is not on the project team')},
                    code='invalid_user_id',
                )


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


# class UserMultipleChoiceField(serializers.MultipleChoiceField):
#     def to_representation(self, value):
#         return [str(pk) for pk in value]
#
#     def to_internal_value(self, data):
#         queryset = User.objects.all()
#         return [queryset.get(pk=pk) for pk in data]
#
#
# class UserTaskInProjectCreateSerializer(serializers.ModelSerializer):
#     user = UserMultipleChoiceField(choices=User.objects.filter(project_id='project.id').values_list('email', 'id'))
#     user_assigned = serializers.HiddenField(default=serializers.CurrentUserDefault())
#
#     class Meta:
#         model = UserTask
#         fields = (
#             'user',
#             'title',
#             'text',
#             'user_assigned',
#         )
