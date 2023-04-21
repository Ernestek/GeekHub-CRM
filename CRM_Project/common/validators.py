from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_name(value):
    if not all(c.isalpha() or c == '-' or c == ' ' for c in value):
        raise ValidationError(
            _(f'{value} contains invalid characters'),
            params={'value': value},
        )
