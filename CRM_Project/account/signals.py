from django.contrib.auth import get_user_model
from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver

from account.tasks import send_mail_for_registered_user

User = get_user_model()


@receiver(post_save, sender=User)
def send_notification_on_user_create(sender, instance, created, **kwargs):
    if created and not instance.is_superuser:
        transaction.on_commit(lambda: send_mail_for_registered_user.delay(user_email=instance.email))
