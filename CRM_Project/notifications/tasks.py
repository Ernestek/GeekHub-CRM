# from celery import shared_task
# from django.contrib.auth import get_user_model
#
# from notifications.models import Notification
#
# User = get_user_model()
#
#
# @shared_task(name='send_notify_project_users', queue='celery')
# def send_notify_project_users(instance, action, pk_set,):
#     if action == 'post_add':
#         for user_id in pk_set:
#             Notification.objects.create(
#                 user=User.objects.get(pk=user_id),
#                 message=f'You have been added to the project {instance.name}'
#             )
#     elif action == 'post_remove':
#         for user_id in pk_set:
#             Notification.objects.create(
#                 user=User.objects.get(pk=user_id),
#                 message=f'You have been removed from the project {instance.name}'
#             )
#
#
# @shared_task(name='send_create_task_notification', queue='celery')
# def send_create_task_notification(instance, created,):
#     if not instance.get('user') == instance.get('user_assigned'):
#         if created:
#             Notification.objects.create(
#                 user=instance.get('user'),
#                 message=f"You have a new task: {instance.get('title')} "
#                         f"{instance.get('user_assigned')} assigned the task",
#             )
#         else:
#             if instance.get('user__is_superuser'):
#                 Notification.objects.create(
#                     user=instance.get('user'),
#                     message=f'Admin made changes to the task "{instance.get("title")}" .',
#                 )
#             else:
#                 # # check if any fields were updated
#                 Notification.objects.create(
#                     user=instance.get('user'),
#                     message=f"Task '{instance.get('title')}' status has been changed to {instance.get('status')}.",
#                 )
