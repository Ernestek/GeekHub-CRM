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
            Notification.objects.get(pk=notification_id)
        except (Notification.DoesNotExist, ValueError, TypeError, OverflowError):
            raise serializers.ValidationError(
                {'notification_id': _('Invalid project id')},
                code='invalid_project_id',
            )

        return attrs

    def create(self, validated_data):
        notification = Notification.objects.get(pk=validated_data['notification_id'])
        notification.read = not notification.read
        notification.save()
        return notification


