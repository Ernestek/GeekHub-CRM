from django.contrib.auth import get_user_model
from rest_framework import serializers

from tasks.models import UserTask

User = get_user_model()


class UserTasksListSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.id', read_only=True)

    class Meta:
        model = UserTask
        fields = (
            'id',
            'user',
            'title',
            'status',
            'created_at',
        )


class UserTasksRetrieveSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.email', read_only=True)
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


# class UserMultipleChoiceField(serializers.MultipleChoiceField):SerializerMethSerializerMethodFieldodField
#     def to_representation(self, value):
#         return [str(pk) for pk in value]
#
#     def to_internal_value(self, data):
#         queryset = User.objects.all()
#         return [queryset.get(pk=pk) for pk in data]


class UserTaskCreateSerializer(serializers.ModelSerializer):
    # user = UserMultipleChoiceField(choices=User.objects.values_list('email', 'id'))
    # user = serializers.CharField(source='user')

    # user = serializers.SlugRelatedField(
    #     slug_field='full_name',
    #     queryset=User.objects.all().annotate(full_name=get_full_name),
    #     many=False,
    # )
    user_assigned = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = UserTask
        fields = (
            'user',
            'title',
            'text',
            'user_assigned',
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
    # user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = UserTask
        fields = (
            # 'title',
            # 'text',
            'status',
        )
    # def validate_user(self, value):
    #     user = value
    #     print(user)
    #
    # def create(self, validated_data):
    #     task = validated_data['id']
    #     task.save()
    #     return task


# class UserTaskSerializer(serializers.ModelSerializer):
#     user = serializers.CharField(source='user.email')
#
#     class Meta:
#         model = UserTask
#         fields = ['id', 'title', 'text', 'user']

    # def validate_status(self, value):
    #     if value not in [status[0] for status in UserTask.TasksStatus.choices]:
    #         raise serializers.ValidationError("Invalid status")
    #     return value