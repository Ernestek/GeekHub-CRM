from django.contrib.auth import get_user_model
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
            if not User.objects.filter(pk=user_id).exists():
                raise serializers.ValidationError(
                    {'user_id': _('Invalid user id')},
                    code='invalid_user_id',
                )
        except OverflowError:
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

        # Checking the authorized user of the project owner
        if self.context['request'].user != project.owner:
            raise serializers.ValidationError(
                {'detail': _('You do not have permission to perform this action.')},
                code='permission_denied',
            )

        attrs['project'] = project
        return attrs

    def create(self, validated_data):
        project = validated_data['project']
        project.users.add(validated_data['user_id'])
        return project


class RemoveUserInProjectSerializer(serializers.Serializer):
    project_id = serializers.IntegerField(write_only=True)
    user_id = serializers.IntegerField(write_only=True)

    def validate(self, attrs):
        project_id = attrs['project_id']
        user_id = attrs['user_id']

        try:
            project = Project.objects.select_related('owner').get(pk=project_id)
        except (Project.DoesNotExist, ValueError, TypeError, OverflowError):
            raise serializers.ValidationError(
                {'project_id': _('Invalid project id')},
                code='invalid_project_id',
            )

        # Checking the authorized user of the project owner
        if self.context['request'].user != project.owner:
            raise serializers.ValidationError(
                {'detail': _('You do not have permission to perform this action.')},
                code='permission_denied',
            )

        if not (user_id in project.users.values_list('id', flat=True)):
            raise serializers.ValidationError(
                {'user_id': _('This user is not on the project team')},
                code='invalid_user_id',
            )

        attrs['project'] = project
        return attrs

    def create(self, validated_data):
        project = validated_data['project']
        project.users.remove(validated_data['user_id'])
        return project
