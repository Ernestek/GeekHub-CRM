from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from account.managers import UserManager
from common.validators import validate_name


class User(AbstractBaseUser, PermissionsMixin):
    objects = UserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    email = models.EmailField(_('email address'), unique=True)

    first_name = models.CharField(_('first name'), max_length=150, validators=[validate_name], blank=True)
    last_name = models.CharField(_('last name'), max_length=150, validators=[validate_name], blank=True)
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(_('staff status'), default=False)
    password_changed = models.BooleanField(_('password changed'), default=False)
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)
    phone_number = PhoneNumberField(_('phone number'), null=True, blank=True, )
    phone_number2 = PhoneNumberField(_('phone number 2'), null=True, blank=True)
    phone_number3 = PhoneNumberField(_('phone number 3'), null=True, blank=True)

    profile_image = models.ImageField(default='default.jpg', blank=True, )

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")
        db_table = 'users'

    def __str__(self):
        return self.email

    def clean(self):
        super().clean()

        phones = [phone for phone in [self.phone_number, self.phone_number2, self.phone_number3] if phone]
        if len(phones) != len(set(phones)):
            raise ValidationError('Phone numbers must be unique.')

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
