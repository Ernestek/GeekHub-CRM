from django.db import models
from django.contrib.auth.models import User

from common.models import BaseModel
from partners.models import Partner


class Project(BaseModel):
    name = models.CharField(max_length=100)
    partner = models.ForeignKey(Partner, on_delete=models.SET_NULL)
    price = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    users = models.ManyToManyField(User, blank=True)
    status = models.BooleanField(default=True)
    owner = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name
