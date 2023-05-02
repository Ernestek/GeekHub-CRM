from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _

from common.enums import ProjectStatus
from common.models import BaseModel
from common.validators import validate_users_in_project
from partners.models import Partner

User = get_user_model()


class Project(BaseModel):
    name = models.CharField(_('name'), max_length=100)
    partner = models.ForeignKey(Partner, on_delete=models.SET_NULL, blank=True, null=True, related_name='project')
    users = models.ManyToManyField(User, blank=True, related_name='project')
    status = models.CharField(_('status'), max_length=20, choices=ProjectStatus.choices,
                              default=ProjectStatus.in_progress)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='project_owner',)
    summary = models.TextField(_('summary'), )

    def __str__(self):
        return self.name
