from rest_framework import serializers

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


class ProjectUpdateSerializer(serializers.ModelSerializer):
    # users = serializers.CharField(source='user')
    # users = serializers.IntegerField()
    class Meta:
        model = Project
        fields = (
            'name',
            'partner',
            'users',
            'status',
            'summary',
        )

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
