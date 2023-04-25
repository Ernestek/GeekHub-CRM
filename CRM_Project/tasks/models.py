from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from common.enums import TasksStatus
from common.models import BaseModel
from projects.models import Project

User = get_user_model()


class UserTask(BaseModel):
    title = models.CharField(_('title'), max_length=256)
    text = models.TextField(_('text'), )
    status = models.CharField(_('status'), max_length=12, choices=TasksStatus.choices,
                              default=TasksStatus.in_progress)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_task')
    user_assigned = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assigned_user_task')

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='user_task')

    def __str__(self):
        return self.title
