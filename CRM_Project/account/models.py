from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models, transaction
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from account.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    objects = UserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    email = models.EmailField(_('email address'), unique=True)

    first_name = models.CharField(_('first name'), max_length=150, blank=True)
    last_name = models.CharField(_('last name'), max_length=150, blank=True)
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(_('staff status'), default=False)
    password_changed = models.BooleanField(_('password changed'), default=False)
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)
    phone_number = PhoneNumberField(_('phone number'), null=True, blank=True)
    phone_number2 = PhoneNumberField(_('phone number 2'), null=True, blank=True)
    phone_number3 = PhoneNumberField(_('phone number 3'), null=True, blank=True)
    
    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")
        db_table = 'users'

    def __str__(self):
        return self.email

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

from django.db.models.signals import post_save
from django.dispatch import receiver

from account.tasks import send_mail_for_registered_user


@receiver(post_save, sender=User)
def send_notification_on_user_create(sender, instance, created, **kwargs):
    if created and not instance.is_superuser:
        print(instance.id)
        transaction.on_commit(lambda: send_mail_for_registered_user.delay(user_email=instance.email))

