from django.contrib.auth import get_user_model
from django.db import models

from common.enums import NotificationStatus
from common.models import BaseModel

User = get_user_model()


class Notification(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    message = models.CharField(max_length=255)
    # status = models.CharField(max_length=20, choices=NotificationStatus.choices,
    #                           default=NotificationStatus.unread)
    read = models.BooleanField(default=False)

