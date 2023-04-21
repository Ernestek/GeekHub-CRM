from django.db import models
from django.utils.translation import gettext_lazy as _


class TasksStatus(models.TextChoices):
    in_progress = 'In progress', _('In progress')
    done = 'Done', _('Done')


class NotificationStatus(models.TextChoices):
    unread = 'unread', _('Unread')
    read = 'read', _('Read')


class ProjectStatus(models.TextChoices):
    in_progress = 'In progress', _('In progress')
    done = 'Done', _('Done')
