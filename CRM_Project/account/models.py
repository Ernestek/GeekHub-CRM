from django.db import models
from django.utils.translation import gettext_lazy as _

from common.models import BaseModel


class Profile(BaseModel):
    firstname = models.CharField(_('firstname'), max_length=100)
    lastname = models.CharField(_('lastname'), max_length=100)

    def __str__(self):
        return self.firstname, self.lastname


