from django.db import models
from django.utils.translation import gettext_lazy as _


class TasksStatus(models.TextChoices):
    in_progress = 'In progress', _('In progress')
    done = 'Done', _('Done')


class ProjectStatus(models.TextChoices):
    in_progress = 'In progress', _('In progress')
    done = 'Done', _('Done')
