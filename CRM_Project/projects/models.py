from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from common.enums import ProjectStatus
from common.models import BaseModel
from partners.models import Partner

User = get_user_model()


class Project(BaseModel):
    name = models.CharField(_('name'), max_length=100)
    partner = models.ForeignKey(Partner, on_delete=models.SET_NULL, blank=True, null=True, related_name='project')
    users = models.ManyToManyField(User, blank=True, null=True, related_name='project')
    status = models.CharField(_('status'), max_length=20, choices=ProjectStatus.choices,
                              default=ProjectStatus.in_progress)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='project_owner',)
    summary = models.TextField(_('summary'), )

    def __str__(self):
        return self.name

    # def clean(self):
    #     if self.owner.id in self.users.values_list('id', flat=True):
    #         print(self.owner.id)
    #         print(self.users.values_list('id', flat=True))
    #         raise ValidationError('Owner cannot be in the users list.')

    # def save(self, *args, **kwargs):
    #     # check that the owner is not in the list of users
    #     self.full_clean()
    #
    #     super().save(*args, **kwargs)