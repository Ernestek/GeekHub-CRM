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
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    # users = serializers.CharField(source='user')
    # users = serializers.IntegerField()
    class Meta:
        model = Project
        fields = (
            'owner',
            'name',
            'partner',
            'status',
            'summary',
        )

    # def validate(self, attrs):
    #     # проверяем, что владелец не находится в списке пользователей
    #     if attrs['owner'] in attrs.get('users', []):
    #         raise serializers.ValidationError(_('Owner cannot be in the users list.'))
    #     return attrs

    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.partner = validated_data.get('partner', instance.partner)
    #     instance.users = validated_data.get('users', instance.users)
    #     instance.status = validated_data.get('status', instance.status)
    #     instance.summary = validated_data.get('summary', instance.summary)
    #
    #     instance.save()
    #
    #     return instance
