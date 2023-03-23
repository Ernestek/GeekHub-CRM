from django.db import models
from account.models import User

from common.models import BaseModel
from partners.models import Partner


class Project(BaseModel):
    name = models.CharField(max_length=100)
    partner = models.ForeignKey(Partner, on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    users = models.ManyToManyField(User, blank=True, null=True)
    status = models.BooleanField(default=True)
    # owner = models.ForeignKey(User, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name
