from rest_framework import serializers
from django.utils.translation import gettext_lazy as _

from notifications.models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = (
            'id',
            'user',
            'message',
            'read',
            'created_at',
        )


class UnreadNotificationCountSerializer(serializers.Serializer):
    count = serializers.IntegerField()


class NotificationStatusUpdateSerializer(serializers.Serializer):
    notification_id = serializers.IntegerField(write_only=True)

    def validate(self, attrs):
        notification_id = attrs['notification_id']

        try:
            notification = Notification.objects.get(pk=notification_id)
        except (Notification.DoesNotExist, ValueError, TypeError, OverflowError):
            raise serializers.ValidationError(
                {'notification_id': _('Invalid project id')},
                code='invalid_project_id',
            )
        attrs['notification'] = notification
        return attrs

    def create(self, validated_data):
        validated_data['notification'].read = not validated_data['notification'].read
        validated_data['notification'].save()
        return validated_data['notification']


