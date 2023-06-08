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
                {'notification_id': _('Invalid notification id')},
                code='invalid_project_id',
            )

        # Checking if a notification belongs to a logged-in person
        if self.context['request'].user != notification.user:
            raise serializers.ValidationError(
                {'detail': _('You do not have permission to perform this action.')},
                code='permission_denied',
            )
        attrs['notification'] = notification
        return attrs

    def create(self, validated_data):
        notification = validated_data['notification']
        notification.read = not notification.read
        notification.save(update_fields=['read', 'updated_at'])
        return notification


