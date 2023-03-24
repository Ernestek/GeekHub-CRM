from django.utils.encoding import force_bytes
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_encode
from django.utils.http import urlsafe_base64_decode
from django.db.models.signals import post_save
from django.dispatch import receiver

from .tasks import send_mail_for_registered_user
from .models import User


@receiver(post_save, sender=User)
def send_notification_on_user_create(sender, instance, created, **kwargs):
    if created and not instance.is_superuser:
        send_mail_for_registered_user.delay(user=str(instance))


def encode_uid(pk):
    return force_str(urlsafe_base64_encode(force_bytes(pk)))


def decode_uid(pk):
    return force_str(urlsafe_base64_decode(pk))

