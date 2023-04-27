from django.contrib.auth import get_user_model
from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver

from notifications.models import Notification
from projects.models import Project
from tasks.models import UserTask

User = get_user_model()


@receiver(post_save, sender=UserTask)
def create_task_notification(sender, instance, created, **kwargs):
    if not instance.user == instance.user_assigned:
        if created:
            Notification.objects.create(
                user=instance.user,
                message=f"You have a new task: {instance.title} "
                        f"{instance.user_assigned} assigned the task",
            )
        else:
            if instance.user.is_staff:
                # # check if any fields were updated
                Notification.objects.create(
                    user=instance.user,
                    message=f"Task '{instance.title}' status has been changed to {instance.status}.",
                )


@receiver(m2m_changed, sender=Project.users.through)
def notify_project_users(sender, instance, action, pk_set, **kwargs):
    if action == 'post_add':
        for user_id in pk_set:
            user = User.objects.get(pk=user_id)
            Notification.objects.create(
                user=user,
                message=f'You have been added to the project {instance.name}'
            )
    elif action == 'post_remove':
        for user_id in pk_set:
            user = User.objects.get(pk=user_id)
            Notification.objects.create(
                user=user,
                message=f'You have been removed from the project {instance.name}'
            )
