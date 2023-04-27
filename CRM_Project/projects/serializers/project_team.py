from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from django.utils.translation import gettext_lazy as _

from projects.models import Project

User = get_user_model()


class AddUserInProjectSerializer(serializers.Serializer):
    project_id = serializers.IntegerField(write_only=True)
    user_id = serializers.IntegerField(write_only=True)

    def validate(self, attrs):
        project_id = attrs['project_id']
        user_id = attrs['user_id']

        try:
            User.objects.only('id').get(pk=user_id)
        except (User.DoesNotExist, ValueError, TypeError, OverflowError):
            raise serializers.ValidationError(
                {'user_id': _('Invalid user id')},
                code='invalid_user_id',
            )
        try:
            project = Project.objects.select_related('owner').get(pk=project_id)
        except (Project.DoesNotExist, ValueError, TypeError, OverflowError):
            raise serializers.ValidationError(
                {'project_id': _('Invalid project id')},
                code='invalid_project_id',
            )

        if user_id == project.owner.id:
            raise serializers.ValidationError(
                {'user_id': _('Owner cannot be on the project team')},
                code='invalid_user_id',
            )
        attrs['project'] = project
        return attrs

    def create(self, validated_data):
        user_id = validated_data['user_id']
        project_id = validated_data['project_id']
        project = validated_data['project']

        # user = get_object_or_404(User, pk=user_id)
        # project = get_object_or_404(Project.objects.prefetch_related('users'), pk=project_id)
        # project.users.add(user)

        # project = Project.objects.select_related('owner').get(pk=project_id)
        project.users.add(user_id)
        return project
